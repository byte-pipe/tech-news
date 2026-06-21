---
title: zeux.io - Zigzag decoding with AVX-512
url: https://zeux.io/2026/06/17/zigzag-decoding-avx512/
date: 2026-06-17
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-22T00:54:47.818440
---

# zeux.io - Zigzag decoding with AVX-512

# Zigzag decoding with AVX‑512

## Overview
- The article explores two AVX‑512‑specific tricks for decoding zigzag‑encoded integers, a format that maps signed deltas to unsigned values so that small magnitudes use few bits.  
- Zigzag decoding can be written branchlessly as `(v >> 1) ^ -(v & 1)`.  
- The author shows how to map this formula to SIMD, first with classic SSE/AVX2 style and then with AVX‑512 mask‑based predication.

## SIMD implementation basics
- For 32‑bit lanes the branchless formula translates to four instructions: shift right, mask low bit, negate mask (via subtraction from zero), and XOR.  
- On Zen 4 each instruction has 1‑cycle latency, giving a total latency of 3 cycles because the mask operation is independent of the shift.

## Using AVX‑512 masks
- Instead of the branchless arithmetic, the original ternary expression can be implemented with AVX‑512 execution masks:
  1. Test the low bit of each lane (`v & 1`).  
  2. Generate a mask where the bit is set (`_mm_test_epi32_mask`).  
  3. Shift right by one (`vpsrld`).  
  4. Conditionally XOR with `-1` (or subtract from `-1`) using the mask (`vpxord` with mask).  
- This reduces the instruction count from four to three:
  - `vptestmd` to create the mask.  
  - `vpsrld` for the shift.  
  - `vpxord{k1}` for the conditional inversion.

## Width considerations
- Masked XOR is only available for 32‑bit elements in AVX‑512.  
- For 16‑bit or 8‑bit lanes the conditional inversion can be expressed as `-1 - x`, using masked subtraction (`vpsubw`/`vpsubb`) which is supported for all widths.

## Performance discussion
- Instruction count drops by one, but actual speed depends on micro‑architectural details: latency, throughput, and mask handling costs.  
- On Zen 4 the masked XOR/subtract has the same latency as the unmasked version, so the main benefit is fewer decode‑decode dependencies and reduced uop count.  
- Real‑world gains will vary with data size, loop unrolling, and whether the constant `-1` vector can be reused.

## Take‑away
- AVX‑512’s test‑and‑mask instructions let you implement the ternary version of zigzag decoding with fewer instructions than the classic branchless arithmetic.  
- The technique works cleanly for 32‑bit integers; for smaller widths you substitute a masked subtraction.  
- Whether the mask‑based version is faster is architecture‑dependent, but it offers a concise, potentially more efficient alternative for high‑throughput vertex decoding.