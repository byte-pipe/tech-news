---
title: Kubernetes on Oxide: How Customer Needs Shaped Our Integrations | Oxide Computer Company
url: https://oxide.computer/blog/kubernetes-on-oxide
date: 2026-08-13
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-14T06:01:47.626431
---

# Kubernetes on Oxide: How Customer Needs Shaped Our Integrations | Oxide Computer Company

# Kubernetes on Oxide: How Customer Needs Shaped Our Integrations

## Background
- In late 2024 customers wanted to run Kubernetes on Oxide, but no supported integrations existed.  
- Kubernetes defines required infrastructure behavior through standard extension points; Oxide provides the necessary primitives via APIs.  
- I joined Oxide as the first Solutions Software Engineer to build software that solves customer problems, with the first task of simplifying Kubernetes deployment on Oxide.  
- Initial resources: a customer‑submitted pull request for a Rancher node driver and an early draft of RFD 493 (Initial Kubernetes Integrations).  

## Provisioning Integrations
- **Goal:** unblock the customer who submitted the Rancher driver and gain hands‑on experience creating clusters, revealing subsequent gaps.  
- **Approach:** develop integrations driven by real customer workflows rather than abstract design, resulting in three distinct provisioning solutions.

### Rancher Node Driver
- A Rancher node driver is a plugin that translates Rancher’s VM operations into Oxide API calls.  
- I learned Rancher and the driver, merged the pull request, added CI/CD and documentation, and released the first Oxide Kubernetes integration.  
- The driver enables Rancher users to provision Oxide instances as nodes in Rancher‑managed clusters.  

### Omni Infrastructure Provider
- Customers wanted to use Sidero Labs’ Omni with Talos Linux to provision clusters.  
- Partnered with Sidero Labs to build an Oxide infrastructure provider for Omni within a seven‑week deadline for a joint Oxide+Sidero KubeCon 2025 showcase.  
- Discovered a Talos issue: Oxide supplies cloud‑init data on a FAT12 filesystem, while Talos only probes ISO 9660, causing the user‑data to be ignored.  
- Implemented a temporary workaround by padding the user‑data to force an ISO 9660 superblock.  
- The integration was demonstrated at KubeCon, allowing Omni users to create Oxide‑based Talos nodes.  

### Cluster API Provider (CAPOx)
- Cluster API (CAPI) offers a native, provider‑extensible API for declarative cluster management, unlike Rancher or Omni.  
- Initially deferred due to limited demand and capacity; later revived as customer requests grew and the Solutions Software Engineering team expanded.  
- Teammates Josh and Brandon led the effort, releasing CAPOx, which lets operators create, scale, upgrade, and delete clusters via Kubernetes custom resources.  
- CAPOx leverages other Oxide components: the Packer plugin builds CAPI‑ready VM images, and the Oxide Cloud Controller Manager (CCM) integrates runtime behavior.  

## Instance Reconciliation
- Provisioning creates Oxide instances, but Kubernetes needs continuous reconciliation to keep `Node` objects in sync with the underlying infrastructure.  
- Implemented the Oxide Cloud Controller Manager (CCM) as the standard Kubernetes extension point for this purpose.  
- The CCM’s node controller synchronizes instance IDs, network addresses, and status (running, shut down, deleted) between Oxide and Kubernetes, enabling accurate node lifecycle handling.  
- Note: the CCM does not provision instances; it solely maintains state consistency.