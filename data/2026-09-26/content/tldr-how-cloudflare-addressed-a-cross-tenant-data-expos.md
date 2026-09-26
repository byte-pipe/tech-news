---
title: How Cloudflare addressed a cross-tenant data exposure vulnerability in Containers | Cloudflare Blog
url: https://blog.cloudflare.com/containers-cross-tenant-vulnerability
site_name: tldr
content_file: tldr-how-cloudflare-addressed-a-cross-tenant-data-expos
fetched_at: '2026-09-26T21:49:12.059604'
original_url: https://blog.cloudflare.com/containers-cross-tenant-vulnerability
date: '2026-09-26'
published_date: '2026-09-24T15:00:00.000Z'
description: External security researchers at Accomplish identified a vulnerability in Cloudflare Containers that could expose residual disk data from previous workloads. We explain how the issue worked, how we investigated it, and the steps we took to remediate it.
tags:
- tldr
---

On September 4, 2026, Oren Yomtov, a security researcher fromAccomplish, responsibly reported a vulnerability affectingCloudflare ContainersandCloudflare Sandboxes(which is built on Containers), through Cloudflare’sbug bounty program. Cloudflare has fully remediated the vulnerability, and we have no evidence that customer data has been compromised.

This post was prepared in collaboration with Oren Yomtov and the Accomplish security research team, whose detailed report and controlled testing helped us validate the issue and respond quickly.

Cloudflare Containers run workloads on multi-tenant infrastructure and automatically assign them to eligible servers; customers cannot select the underlying host. The researchers demonstrated that a customer with a Workers Paid account could recover residual disk blocks previously used by Containers on the same host. The technique could not target a particular customer, workload, host, or data, and residual data was not guaranteed to be present.

Cloudflare applied a fix across the Containers fleet, with no customer-side configuration changes required. Within the historical disk-I/O telemetry available to us, we identified no evidence of malicious exploitation. Activity we could attribute to the reported technique came from the researchers and Cloudflare engineers conducting authorized validation.

Here, we explain the underlying storage behavior, its potential impact, our investigation, and the actions we took in response.

## How container storage allocation works

Cloudflare Containers use Linux device mapper thin provisioning (dm-thin) to provide each container with a writable root disk. Each container lives inside a dedicated virtual machine powered by the Firecracker virtual machine monitor. Firecracker presents this disk to the virtual machine as /dev/vdc.

Thin provisioning allocates physical storage only when a virtual disk writes to a previously unmapped region. The affected storage pools used a 64 KiB thin-block size. When the thin volume backing a container's root disk was deleted, its physical blocks were returned to a pool that served workloads belonging to multiple customer accounts.

The affected pool configuration included the following option:

skip_block_zeroing

With this option configured, dm-thin skips zeroing newly allocated blocks before making them accessible. Consequently, when a previously-used 64 KiB block was reassigned, a full-block write replaced its previous contents, but a smaller write changed only the written portion. The remainder could retain data from the block’s previous owner.

## How the exploit worked

Reading an unmapped region of a new thin disk did not reveal residual data. For an unmapped region of the thin device,dm-thinreturned zeroes without allocating a physical block.

The proof of concept identified 64 KiB-aligned regions corresponding to free space in the guest’s ext4 filesystem and wrote one aligned 4 KiB block into each region.

When such a write reached an unmapped thin block, dm-thin allocated a physical 64 KiB block from the shared pool. The 4 KiB write replaced only that portion of the block, and because block zeroing was disabled, the remaining 60 KiB could retain data from a previous container.

A subsequent raw-device read could therefore observe bytes that the new container had never written.

The proof of concept performed the following steps:

1. Create a container using a Workers Paid account.
2. Open the writable root disk at/dev/vdc.
3. Read the disk and record a baseline.
4. Write one 4 KiB block into each selected 64 KiB region corresponding to ext4 free space.
5. Read the resulting blocks again.
6. Examine only the portions not overwritten by the new container.

The submission included counts, block offsets, sizes, checksum results, and truncated hash prefixes. Although the researchers recovered raw blocks to validate the issue, the materials provided to Cloudflare contained no third-party filenames, identifiers, credentials, hostnames, addresses, or recovered content values. As described below, the researchers have also confirmed that they securely deleted the recovered data.

## How the vulnerability was validated

The researchers used ext4 directory block checksums to distinguish blocks belonging to their own test filesystem created for the proof of concept from blocks originating from other filesystems.

When ext4 uses themetadata_csumfeature, directory block checksums incorporate values associated with the filesystem and inode.

Across six production placements, the researchers reported:

* All 5,614 testable directory blocks.
* Zero of those blocks were attributed to the researchers’ filesystem.
* 2,700 distinct foreign directory inodes identified through checksum analysis.

To validate the method, the researchers tested it against blocks they had deliberately created and deleted in the controlled test filesystem used for the proof of concept. The method correctly attributed all 162 blocks to that filesystem.

The researchers ultimately observed residual material on 18 of 24 placements and 20 of 22 underlying nodes across four continents. The recovered block types included directory structures, database pages, and structurally complete SQLite databases. The researchers reported using scripts that output only aggregate counts and format checks, not recovered file contents. The materials submitted to Cloudflare contained no recovered content values or third-party identifiers. The researchers subsequently confirmed that recovered data under their control remained confidential and was securely deleted following submission, consistent with Cloudflare’s HackerOne disclosure policy.

## Impact

The vulnerability would potentially have allowed for a customer with a Workers Paid account to recover residual data from storage blocks previously used by other customers’ Containers on the same underlying host.

A successful exploitation would have crossed the tenant-isolation boundary and could disclose filesystem metadata, directory structures, database pages, and application data.

However, an attacker could not select a particular victim or access an actively attached disk. Exposure depended on Cloudflare’s workload placement and which previously released blocksdm-thinreassigned. Moreover, the researchersdid notdemonstrate modification of another customer’s active data or impact to workload availability.

## How we mitigated the vulnerability

Our first mitigation was to removeskip_block_zeroingfrom thedm-thinpool configuration across the fleet. This restoreddm-thin’s default behavior of clearing newly allocated blocks before exposing them to a container. It stopped the reported technique, in which a small write triggered allocation and a larger read recovered residual data from the remainder of the block. The researchers independently confirmed that their proof of concept no longer worked after this change.

Zeroing new allocations did not sanitize blocks already mapped into existing thin devices. These mappings existed in running container disks and in each host’s cache of prepared dm-thin snapshots for OCI image layers. A new container could inherit mappings from a cached layer without allocating those blocks again, allowing residual bytes in unused regions, including ext4 free space, to remain readable through raw reads of/dev/vdc.

We therefore also retired all running container disks and removed cached image snapshots created before the mitigation. We drained hosts during off-peak hours, restarted the VMs on each host, and cleared each host's image cache so that disks and cached layers were recreated using zeroed allocations. We have completed this cleanup across the Containers fleet.

## No evidence of exploitation

As part of our response, we investigated whether other workloads showed activity consistent with the reported exploitation technique. We reviewed retained historical disk-I/O telemetry from our container infrastructure, using the researchers’ proof of concept and our internal reproduction as reference activity.

The proof of concept produced a characteristic relationship between writes and reads. When a 4 KiB write reached a previously unmapped region, it could trigger allocation of a reused 64 KiB storage block. With zeroing disabled, the remaining 60 KiB could retain data from a previous container. Subsequent reads could therefore recover substantially more data than the new container had overwritten.

Using these characteristics, we developed detection signatures and applied them to the historical telemetry available to us. We identified activity attributable to the researchers and Cloudflare engineers conducting authorized validation, and did not identify additional activity consistent with the reported technique.

We saw no evidence that this specific attack vector was exploited by anyone else.

## Cloudflare customers are protected

As we noted above, Cloudflare has patched this vulnerability and remediation does not require any further action by Cloudflare customers. In addition, we found no evidence of any malicious actor abusing this vulnerability.

## Moving quickly with transparency

We thank Oren Yomtov and the Accomplish security research team for their thorough research, responsible disclosure, and collaboration on this post. We encourage the Cloudflare community to submit any identified vulnerabilities to help us continually improve the security posture of our products and platform.

We also recognize that the trust you place in us is paramount to the success of your infrastructure on Cloudflare. We take these vulnerabilities very seriously and will continue to do everything in our power to mitigate impact. We deeply appreciate your continued support and trust in our platform, and remain committed not only to prioritizing security in all we do, but also acting swiftly and transparently whenever an issue arises.

## Timeline

* September 4, 15:26 UTC: Oren Yomtov fromAccomplishreported the issue throughHackerOne.
* September 4, 18:45 UTC: Cloudflare opened a security incident and confirmed the production setup that caused the flaw.
* September 4, 21:27 UTC: Cloudflare merged the runtime fix and its reuse test.
* September 4, 22:03 UTC: Cloudflare merged the changes for new and live pools.
* September 4, 23:15 UTC: Cloudflare started rolling out the changes.
* September 7, 06:13 UTC: Cloudflare completed rolling out the changes and began clearing old pool data.
* September 14, 10:50 UTC: The researchers reported that their proof of concept had stopped working.
* September 14, 12:52 UTC: Cloudflare awarded the researcher a bounty.
* September 19, 15:03 UTC: Cloudflare completed cleanup of all pre-mitigation cached snapshots across the affected fleet.

## Related tags

Containers
Developer Platform
Developers
Multi-tenant Security
Security
Vulnerabilities

Follow on Social Media

* Cloudflare
* Avishek Sarkar

## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.