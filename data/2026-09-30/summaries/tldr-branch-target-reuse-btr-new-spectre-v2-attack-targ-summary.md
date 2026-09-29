---
title: Branch Target Reuse, BTR: New Spectre V2 Attack Targeting JIT Compilers - Phoronix
url: https://www.phoronix.com/news/Branch-Target-Reuse-BTR
date: 2026-09-30
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-30T06:01:00.310884
---

# Branch Target Reuse, BTR: New Spectre V2 Attack Targeting JIT Compilers - Phoronix

# Branch Target Reuse, BTR: New Spectre V2 Attack Targeting JIT Compilers

## Overview
- The embargo on a new Spectre‑V2 variant, **Branch Target Reuse (BTR)**, has been lifted.
- BTR is a speculative execute‑after‑free primitive that exploits stale indirect branch prediction entries in just‑in‑time (JIT) compilers.

## Affected Technologies
- **Linux kernel**: BPF JIT engine.
- **Oracle GraalVM**: JIT code‑cache.
- **Mozilla SpiderMonkey**: JavaScript engine used in Firefox.

## Impact
- VUSec researchers demonstrated an end‑to‑end exploit that leaks arbitrary memory on modern Intel CPUs, bypassing all enabled mitigations.
- All tested processors—Intel, AMD, and Arm—were vulnerable to BTR.

## Mitigations and Vendor Responses
- **Linux kernel**:  
  - Patches landed in July to enable Indirect Branch Predictor Barrier (IBPB) flush on BPF JIT allocations.  
  - Added hardening against JIT spraying in the BPF code.  
  - No additional mitigations released now; changes are already mainlined and back‑ported.
- **Oracle GraalVM**:  
  - Randomizing JIT code‑cache locations to make BTR attacks harder.
- **Mozilla**:  
  - Evaluated IBPB‑based mitigations for SpiderMonkey but is focusing on site‑isolation improvements instead.

## Further Information
- Detailed technical data and the full research can be found at **VUSec.net**.