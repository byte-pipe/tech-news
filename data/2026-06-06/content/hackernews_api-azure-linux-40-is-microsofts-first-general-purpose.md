---
title: Azure Linux 4.0 is Microsoft’s first general-purpose Linux
url: https://www.boxofcables.dev/azure-linux-4-0-is-microsofts-first-general-purpose-linux/
site_name: hackernews_api
content_file: hackernews_api-azure-linux-40-is-microsofts-first-general-purpose
fetched_at: '2026-06-06T11:34:33.102844'
original_url: https://www.boxofcables.dev/azure-linux-4-0-is-microsofts-first-general-purpose-linux/
author: haydenbarnes
date: '2026-06-05'
published_date: '2026-06-03T14:23:01.000Z'
description: Microsoft’s in-house Linux, the distribution that grew out of CBL-Mariner, just hit public preview as a general-purpose cloud OS you can run on any Azure VM and coming soon to WSL.
tags:
- hackernews
- trending
---

Microsoft shipped Azure Linux 4.0 intopublic previewat Build 2026, and for the first time you can run it on any Azure virtual machine, not just as the host underneath Azure Kubernetes Service. That sounds like a small distinction. But, this is the moment Microsoft's in-house Linux stops being a special-purpose appliance distro and becomes a general-purpose Linux distro.

I have been following this distribution since before it had a marketing name. So let me put 4.0 in context...

Photos from the Azure Linux 4 session at Microsoft Build 2026

## What I keep on about

Microsoft has built more than one Linux distribution. Back in February 2022 I went looking through Microsoft's package mirrors and foundCBL-Delridge, a Debian-based distro that powered Azure Cloud Shell. It was never announced.Mary Jo Foley wrote it up at ZDNetafter reading that post. By November 2022, Delridge was404: its apt repository went dark and Cloud Shell moved to Microsoft's other Linux: CBL-Mariner.

CBL stands for Common Base Linux, a whole family of internal distros named after Seattle geography. Delridge was the Debian one. Mariner was an RPM one, built from scratch with spec files borrowed fromPhoton OS, Fedora, andLinux From Scratch. Mariner is the one that survived. InMarch 2024 Microsoft renamed it Azure Linuxand renamed theGitHub repositoryto match.

So when I say Azure Linux, I mean the distribution that started internal development in September 2019, went public on GitHub in November 2020, hit 2.0 in April 2022, and has been the container host for AKS since 2023. None of that history was aimed at you running it on your own VM.

That is what changes now.

## What is actually new in 4.0

Azure Linux 4.0 isderived from Fedora, right now a Fedora 43 snapshot, rather than assembled package by package the way 1.0 through 3.0 were. Microsoft no longer maintains every spec file by hand. Instead it tracks Fedora upstream and applies declarative overlays, where every deviation from Fedora carries a written description of why it exists. The rendered spec files are checked into therepositoryso you can read exactly what Microsoft changed and why.

The component stack moved up accordingly:

* Kernel 6.18 LTS, Azure-tuned, with the Hyper-V integration and GPU and AI accelerator support you would expect from an Azure cloud kernel. Microsoft maintains its ownkernel forkand embeds its signing keys directly in the build.
* dnf5replacestdnf, Microsoft's lean C reimplementation of dnf inherited from Photon OS. This is the single most user-visible change. You now get standarddnf5tooling and the full plugin ecosystem instead of a Microsoft-specific package manager.
* glibc 2.42,systemd 258,OpenSSL 3.5(with post-quantum cryptography support),Python 3.14, andRPM 6.0with a modernized database backend and stronger signature verification.
* FIPS 140-3certification is in progress and slated for general availability.

Security is solid. SELinux is supported on every image, the kernel ships with hardening turned on (ASLR, stack protection, seccomp, and systemd service sandboxing), packages and repositories are cryptographically signed, and Microsoftpublishes SBOMsfor the supply chain.

## Why this is the next step

Here is the part that matters. For most of its life, Azure Linux was infrastructure you ran on without knowing it. It was the host OS for AKS nodes, the base image for Microsoft's own first-party services, the system distro that hostsWSLg. You did not pick it. It was underneath the thing you picked.

Azure Linux 4.0 is built to be picked. It runs across every Azure compute surface:

* Virtual machines and scale sets, deployable straight from theAzure Marketplacewith no additional OS licensing cost.
* Containers, with base, distroless, and language-runtime images on theMicrosoft Container Registry, built from the same supply chain as the VM images.
* AKS, where it has been the container host since 2023, now joined by Azure Container Linux, a Flatcar-based immutable variant that shares the same kernel for stricter compliance environments.
* WSL, so you can develop locally on the same Linux you deploy to production withwsl --install -d AzureLinux(soon, go try it on Azure first).

Databricks migrated more than 100,000 VMs and over a million CPU cores to Azure Linux. LinkedIn moved its infrastructure to Azure Linux. Azure Linux already runs behind AKS, Azure SQL, and Cosmos DB. The 4.0 preview takes that and gives it to everyone else.

## What makes Azure Linux different

There are a lot of cloud Linux distributions. Amazon has Amazon Linux. The Flatcar and CoreOS lineage offers immutable container hosts. Ubuntu and RHEL run nearly everywhere. So what is distinct here?

A few things stand out:

* The supply chain is auditable by design.Building on Fedora with declarative overlays means every change from upstream is documented in the repository. That is a stronger story than most distributions can tell about what is in their packages and why.
* It is minimal on purpose.Azure Linux ships only what cloud and server workloads need. There is no desktop, no GUI, no general-purpose sprawl. Thedistroless container imagestake this to its logical end: no shell, no package manager, almost nothing to exploit.
* Microsoft made a Linux distro.

## What it means for Linux

I havetracked Microsoft's open source arc for years. The short version: Azure started hosting Linux VMs in 2012, Satya Nadella said "Microsoft loves Linux" in 2014, Microsoft joined the Linux Foundation in 2016, shipped WSL the same year, cross-licensed 60,000 patents through the Open Invention Network in 2018, and by 2019 Linux was the majority operating system on Azure. Today more than two-thirds of customer cores on Azure run Linux.

Against that backdrop, a general-purpose Azure Linux is the logical next step. Microsoft went from consuming Linux, to shipping Linux internally, to shipping a Linux distribution anyone can run.

Another major vendor maintaining a distribution upstream-first against Fedora, contributing patches, and putting real money into supply-chain security work through OpenSSF and Alpha-Omega. More maintained distributions, built in the open, is good for everyone downstream.

From an undocumented Debian remix I had to reverse-engineer from a package mirror, to a Fedora-derived, FIPS-targeted, distroless-capable distribution you can deploy from a marketplace in two clicks. That is a long way in four years.

Microsoft ships Linux.