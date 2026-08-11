---
title: When Your VPS Never Had the Resources It Was Sold With - DEV Community
url: https://dev.to/pascal_cescato_692b7a8a20/when-your-vps-never-had-the-resources-it-was-sold-with-302o
site_name: devto
content_file: devto-when-your-vps-never-had-the-resources-it-was-sold
fetched_at: '2026-08-11T11:42:54.020966'
original_url: https://dev.to/pascal_cescato_692b7a8a20/when-your-vps-never-had-the-resources-it-was-sold-with-302o
author: Pascal CESCATO
date: '2026-08-05'
description: 'I needed a VPS to run CyberPanel. Simple enough: 1 vCPU, 1 GB RAM, 10 GB SSD, IPv6 only. CyberPanel... Tagged with networking, devops, vps, linux.'
tags: '#networking, #devops, #vps, #linux'
---

Debugging invisible hypervisor provisioning gaps

I needed a VPS to run CyberPanel. Simple enough: 1 vCPU, 1 GB RAM, 10 GB SSD, IPv6 only. CyberPanel needs IPv4, so I upgraded to the next tier: 2 vCPU, 2 GB RAM, 20 GB SSD, one IPv4 address.

What followed was two separate infrastructure failures in the same 24 hours, from the same provider, on the same instance. Neither was a Linux problem. Both were provisioning problems — the gap between what an offer promises and what actually gets attached to the virtual machine.

I'm not naming the provider. It's a small French hosting company, and the point of this article isn't to send traffic their way — it's the pattern itself, which is common enough in the VPS world to be worth documenting properly.

## Problem 1: IPv4 that went nowhere

The upgrade completed and the new IPv4 address showed up in the panel. Interface up, IP configured, default route present, ARP resolution to the gateway working:

88.151.197.1 lladdr 44:4c:a8:fb:ef:fd REACHABLE

Enter fullscreen mode

Exit fullscreen mode

But ICMP got no response at all, from the VPS or from the gateway itself:

88.151.197.112 > 88.151.197.1: ICMP echo request
(no reply)

Enter fullscreen mode

Exit fullscreen mode

IPv6 worked normally throughout. Everything on the guest side — interface, routing, ARP — was correct. That's a useful diagnostic signal in itself: when ARP resolves but ICMP is silent, the guest OS has done its job and the problem sits in the infrastructure layer above it — typically a MAC/IP binding on the hypervisor or virtual switch that hasn't been updated to match the new address.

It eventually got resolved, but with no explanation of what was actually changed on their side. At that point I'd lost most of a day to a connectivity problem on an instance that, on paper, was correctly configured from the first minute.

## Problem 2: the disk that was never there

With IPv4 finally working, I moved on to installing CyberPanel — the entire reason for the upgrade. A fresh Ubuntu install went fine until CyberPanel's dependency installation started throwingNo space left on device. So I checked:

root@panel:~#
 
lsblk

NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sda 8:0 0 3.5G 0 disk
├─sda1 8:1 0 2.5G 0 part /
├─sda14 8:14 0 4M 0 part
├─sda15 8:15 0 106M 0 part /boot/efi
└─sda16 259:0 0 913M 0 part /boot

Enter fullscreen mode

Exit fullscreen mode

The disk was 3.5 GB. Root partition, 2.5 GB. The offer promised 20 GB after the upgrade — and, as it turned out, the base 10 GB tier had never delivered more than a fraction of that either. This wasn't a side effect of the upgrade. It had been wrong from the start; the upgrade just moved the goalpost from 10 GB to 20 GB while the actual allocation stayed untouched.

This is where a lot of guides point you atgrowpartorresize2fs. Both are useless here, and understanding why matters:

resize2fsandgrowpartoperate at the bottom two layers. They can only extend a filesystem or partition into space that already exists on the virtual disk. If the disk itself is 3.5 GB, there is no unallocated space to grow into — the tools report success or do nothing, because there's genuinely nothing for them to do. The problem isn't in the guest OS. It's one layer below it, in what the hypervisor actually attached to the VM.

I opened a support ticket, included thelsblkoutput, and asked them to check the volume attachment.

The reply I got back attributed the disk shortfall to "the IPv6 to IPv4 upgrade" — as if provisioning a new IPv4 address could somehow shrink a virtual disk. It doesn't, and the two are unrelated at every layer shown in the diagram above. It reads less like a diagnosis and more like a convenient way to fold a second unresolved ticket into the first.

## Problem 3: "fixed" didn't mean fixed

The provider's answer was to ask me to check again — no diagnosis of their own. I did, and this time the disk was correct: 20 GB, as ordered. I replied "corrected, thanks," and the ticket was closed.

Later the same day, I reinstalled Ubuntu to get a clean baseline. The disk was wrong again — same as before the fix, not as after it:

root@panel:~#
 
date

Mon Aug 3 20:56:49 UTC 2026

root@panel:~#
 
lsblk

NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sda 8:0 0 3.5G 0 disk
├─sda1 8:1 0 2.5G 0 part /
├─sda14 8:14 0 4M 0 part
├─sda15 8:15 0 106M 0 part /boot/efi
└─sda16 259:0 0 913M 0 part /boot
sr0 11:0 1 4M 0 rom

Enter fullscreen mode

Exit fullscreen mode

Same 3.5 GB disk, same 2.5 GB root partition, hours after the ticket was marked resolved.

This is the part worth sitting with. A "fix" applied through a support ticket, on a running instance, doesn't necessarily touch the thing that's actually broken. If the underlying VM profile or provisioning template is wrong, a support agent can patch the live disk allocation by hand and call it closed — while the next rebuild pulls from the same broken template and reproduces the exact same fault. The fix fixed an instance, not the cause.

That's the practical lesson: if a resource-provisioning issue gets "corrected" on a live VPS, don't close the loop until you've verified it survives a rebuild. A one-off patch and a fixed template look identical from the support ticket. They don't look identical fromlsblk.

## What two failures in one day tell you

Individually, either of these could be dismissed as a one-off glitch. Together, they're more telling: two independent provisioning mismatches — disk and network — on the same instance, within the same upgrade cycle, one of which reappeared after being marked fixed. That pattern points to the provisioning pipeline itself, not to isolated bad luck.

## Commands worth knowing

If you land in a similar situation, these will tell you which layer you're actually dealing with:

lsblk 
# what Linux sees attached

fdisk 
-l
 
# partition table detail

df
 
-h
 
# filesystem usage

blockdev 
--getsize64
 /dev/sda 
# raw device size, bytes

ip addr 
# interface and IP state

ip route 
# routing table

ip neigh 
# ARP/NDP cache — gateway reachability

ping 
-c
 3 <gateway> 
# basic reachability test

Enter fullscreen mode

Exit fullscreen mode

Iflsblkandblockdev --getsize64already show a disk smaller than what you're paying for, don't touchgrowpartorresize2fs— you're not looking at a Linux problem. Ifip neighshows the gateway asREACHABLEbutpinggets nothing back, you're not looking at a Linux problem either. In both cases, the fix is on the other side of the hypervisor boundary, and no amount of guest-side troubleshooting will reach it.

## Takeaway

A VPS isn't physical hardware, but it's supposed to honor the same basic contract: the resources advertised should be the resources actually present. Before blaming Linux, a package, or your own configuration, check the layer underneath — and if a provider tells you something's fixed, verify it survives a rebuild before you believe it.

None of this required an unusual amount of digging —lsblk,ip neigh, a rebuild to double-check. Which is really the point: for roughly the same price, sometimes less, providers like OVH, Contabo, or Infomaniak offer configurations that don't require this kind of forensic work just to get the resources you paid for. Chasing the cheapest listed price has a cost. It's just not always visible until you've already lost a day to it.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (27 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse