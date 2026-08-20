---
title: GitHub - vixhal-baraiya/microgpt-c: The most atomic way to train and inference a GPT in pure, dependency-free C · GitHub
url: https://github.com/vixhal-baraiya/microgpt-c
date: 2026-08-18
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-20T07:17:45.390895
---

# GitHub - vixhal-baraiya/microgpt-c: The most atomic way to train and inference a GPT in pure, dependency-free C · GitHub

# microGPT-C

## Overview
- Pure‑C, dependency‑free implementation of a character‑level transformer (GPT).  
- All components—forward pass, back‑propagation, Adam optimizer, and sampling—are contained in a single C file using only libc.  
- Trains on ~32 k names within seconds and can generate new names.

## Build and Run
- Compile and execute with `make run` or directly on any line‑separated corpus:  
  `./microgpt data/names.txt`  
- Supports macOS, Linux, Windows (MSYS2), ARM64 with NEON, and x86‑64 with AVX2; the Makefile automatically selects host‑appropriate flags.

## Training Progress (example)
- step 5 000 / 20 000 → loss 2.6036 (avg 2.2940)  
- step 10 000 / 20 000 → loss 1.9639 (avg 2.2564)  
- step 15 000 / 20 000 → loss 2.7007 (avg 2.2151)  
- step 20 000 / 20 000 → loss 2.3463 (avg 2.2201)

## Inference Samples
1. kayley  
2. maria  
3. arana  
4. shayan  
5. jayden  
6. saria  
7. kaylen  
8. amari  
9. alina  
10. mailyn  

## Model Characteristics
- 4 192 parameters.  
- Generalizes rather than memorizes: achieves ~2.205 nats/character on both training (20 000 names) and unseen (12 033 names) data, surpassing an interpolated trigram model with nearly five times more parameters.

## Implementation Details
- Training and inference use distinct forward functions:  
  - `gpt_forward` stores activations for back‑propagation.  
  - `gpt_forward_infer` provides a specialized single‑token path; its logits match the training path within fp32 rounding.  
- Further performance explanations are in `docs/PERFORMANCE.md`.

## Performance Benchmarks

| Machine               | Backend | Tokens/sec |
|-----------------------|---------|------------|
| Apple M5 Pro          | NEON    | 10,168,430 |
| AMD Ryzen 5 5600H     | AVX2    | 6,927,775 |