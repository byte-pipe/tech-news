---
title: 'Branch Target Reuse, BTR: New Spectre V2 Attack Targeting JIT Compilers - Phoronix'
url: https://www.phoronix.com/news/Branch-Target-Reuse-BTR
site_name: tldr
content_file: tldr-branch-target-reuse-btr-new-spectre-v2-attack-targ
fetched_at: '2026-09-30T06:00:31.385382'
original_url: https://www.phoronix.com/news/Branch-Target-Reuse-BTR
date: '2026-09-30'
description: 'Branch Target Reuse, BTR: New Spectre V2 Attack Targeting JIT Compilers'
tags:
- tldr
---

# Branch Target Reuse, BTR: New Spectre V2 Attack Targeting JIT Compilers

Written by 
Michael Larabel
 in 
Linux Security
 on 29 September 2026 at 01:00 PM EDT. 
2 Comments

It's been a while since any new Spectre vulnerabilities have come to light but that's changing today. The embargo has now lifted on BTR, Branch Target Reuse as a new Spectre-V2 attack affecting just-in-time (JIT) compilers.
 
Security researchers at VUSec have announced today Branch Target Reuse as a Spectre-V2 attack in JIT engines affecting the Linux kernel with BPF, Oracle's GraalVM, and also the Mozilla SpiderMonkey JavaScript engine for Firefox.
 
BTR amounts to a speculative execute-after-free primitive with JIT compilers when not invalidating stale indirect branch prediction entries. One of the end-to-end exploits developed by VUSec is for leaking arbitrary memory on modern Intel CPUs in bypassing all enabled mitigations. All processors evaluated by the VUSec team were found to be impacted by Branch Target Reuse including Intel, AMD, and Arm hardware.
 
Hardware vendors are encouraging existing mitigation mechanisms. In July when this was privately disclosed, the Linux kernel landed patches to enabling Indirect Branch Predictor Barrier (IBPB) flush on BPF JIT allocations and support in the BPF kernel code for hardening against JIT spraying. Back in July I covered the kernel changes at the time in 
Linux 7.2-rc2 BPF Code Being Hardened Against JIT Spraying Attacks
. Thus no new Linux kernel mitigations out today as the BPF changes have been mainlined since July and also back-ported already to stable kernel versions.
 
For Oracle GraalVM, randomizing JIT code-cache locations is being done to hinder BTR. Mozilla is said to have evaluated IBPB-based mitigations for SpiderMonkey but instead prioritizing work on site isolation capabilities.
 
Those wanting to learn more about BTR can do so at 
VUSec.net
.