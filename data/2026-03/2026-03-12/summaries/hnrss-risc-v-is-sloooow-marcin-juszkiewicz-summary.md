---
title: RISC-V is sloooow – Marcin Juszkiewicz
url: https://marcin.juszkiewicz.com.pl/2026/03/10/risc-v-is-sloooow/
date: 2026-03-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-12T03:16:15.620534
---

# RISC-V is sloooow – Marcin Juszkiewicz

# Summary of “RISC‑V is sloooow – Marcin Juszkiewicz”

## Triaging
- Reviewed Fedora‑RISC‑V tracker entries.  
- Reduced open items to 17 in the **NEW** state.  
- Attempted to address as many issues as possible.

## Fedora packaging
- Workflow: `fedpkg clone -a` → `fedpkg mockbuild -r fedora-43-riscv64`.  
- Inspected build logs when builds failed.  
- Submitted 86 pull requests covering packages from heavy (llvm15) to simple (iyfct).  
- Most PRs merged and built for Fedora 43; they are tracked via the `f43-updates` tag on Koji.

## Slowness
- Current RISC‑V hardware (e.g., StarFive VisionFive 2) yields very long build times.  
- Example build times for **binutils‑2.45.1‑4.fc43** on various architectures:

  - aarch64: 36 min (12 cores, 46 GB)  
  - i686: 25 min (8 cores, 29 GB)  
  - ppc64le: 46 min (10 cores, 37 GB)  
  - **riscv64: 143 min (8 cores, 16 GB)**  
  - s390x: 37 min (3 cores, 45 GB)  
  - x86_64: 29 min (8 cores, 29 GB)

- Milk‑V Megrez (another SBC) completed the same build in 58 min.  
- Builds are performed with LTO disabled to reduce memory usage.  
- Typical RISC‑V builders have 4–8 cores and 8–32 GB RAM, comparable to low‑end Arm Cortex‑A55 cores.  
- Upcoming hardware (UltraRISC UR‑DP1000, SpacemiT K3) may improve performance but will not fully solve the issue.

## Hardware needs for Fedora inclusion
- Goal: build the binutils package in under one hour with system‑wide LTO enabled.  
- Slow builders cause maintainers to complain and may lead developers to drop RISC‑V support, since Fedora releases wait for all architectures to finish.  
- Future builders must be rack‑mountable and manageable like standard servers; manual SBC maintenance in data centers is impractical.  
- Without meeting speed and manageability requirements, RISC‑V 64‑bit cannot become an official primary Fedora architecture.

## Continued use of QEMU for local testing
- Uses QEMU on an 80‑core AArch64 desktop to emulate riscv64.  
- Example: llvm15 builds in ~4 hours on the desktop vs. 10.5 hours on a Banana Pi BPI‑F3 builder.  
- QEMU is only for local builds/testing; Fedora performs native builds on actual hardware.  
- Anticipates much faster builds on high‑core‑count systems (e.g., Ampere One with 192/384 cores).

## Future plans
- Begin building Fedora 44; aim to standardize kernel images across builders (currently mixed versions).  
- LTO will remain disabled for now.  
- Plan to acquire faster builders and allocate heavy packages to them.

## Comments
- Readers can leave feedback on the author’s Mastodon post.  

*Books I read in 2025* (reference list omitted).