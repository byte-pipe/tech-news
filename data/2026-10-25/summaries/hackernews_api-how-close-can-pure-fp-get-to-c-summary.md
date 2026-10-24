---
title: How close can pure FP get to C?
url: https://rtfeldman.com/fp-vs-c
date: 2026-10-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-25T02:57:25.304533
---

# How close can pure FP get to C?

# How close can pure FP get to C?

## Context and Motivation
- A DEFLATE library written in Lean 4 (lean‑zip) outperformed the Rust crate `miniz_oxide`, achieving higher throughput and smaller output.
- The same Lean implementation could not match the performance of `libdeflate`, a highly tuned C library that uses architecture‑specific SIMD.
- Roc is a new functional language (not a theorem prover) that emphasizes runtime speed and fast compilation.  
- The author used Roc’s `roc-deflate` package (by Niclas Ahden) to see how close a pure‑FP implementation could get to `libdeflate` on non‑streaming APIs, using the Silesia corpus for benchmarking.

## Benchmark Setup
- Two hardware platforms:  
  - Apple M1 MacBook Pro (2021)  
  - AMD Ryzen 9 3900X running Ubuntu (x64)  
- 144 individual compression runs covering all files in the Silesia corpus at compression levels L1, L2, and L3.  
- Each measurement is the median of 15 runs.  
- Comparison metric: megabytes per second (MB/s) of compression throughput.

## Overall Results
- **Median slowdown of `roc-deflate` vs. `libdeflate`:**  
  - 8.9 % slower on the Ryzen 3900X  
  - 2.6 % slower on the M1 MacBook Pro  
- Across all 144 benchmarks, `roc-deflate` was on average slower, but never more than ~10 % behind `libdeflate`.

## Detailed Performance (selected figures)

### L1 Compression (M1)
| File | libdeflate (MB/s) | roc-deflate (MB/s) |
|------|-------------------|--------------------|
| dickens | 230.57 | 202.92 |
| mozilla | 248.31 | 225.79 |
| mr | 312.26 | 277.57 |
| nci | 601.03 | 529.49 |
| ooffice | 169.98 | 153.99 |
| osdb | 284.01 | 257.14 |
| reymont | 281.14 | 245.80 |
| samba | 344.00 | 309.79 |
| sao | 160.21 | 145.28 |
| webster | 268.58 | 239.18 |
| x‑ray | 145.93 | 134.66 |
| xml | 476.83 | 419.07 |

### L2 Compression (Ryzen 3900X)
| File | libdeflate (MB/s) | roc-deflate (MB/s) |
|------|-------------------|--------------------|
| dickens | 161.68 | 143.60 |
| mozilla | 184.55 | 168.37 |
| mr | 204.86 | 182.07 |
| nci | 453.14 | 409.82 |
| ooffice | 128.05 | 118.08 |
| osdb | 203.10 | 185.41 |
| reymont | 207.66 | 183.69 |
| samba | 249.57 | 228.02 |
| sao | 112.78 | 105.68 |
| webster | 198.86 | 181.07 |
| x‑ray | 117.18 | 107.00 |
| xml | 352.59 | 323.17 |

### L3 Compression (M1)
| File | libdeflate (MB/s) | roc-deflate (MB/s) |
|------|-------------------|--------------------|
| dickens | 130.85 | 122.04 |
| mozilla | 169.26 | 158.29 |
| mr | 171.11 | 158.?? (data truncated) |
| … | … | … |

*(The full tables continue in the original article; the pattern shows roc‑deflate consistently within ~5‑10 % of libdeflate.)*

## Conclusions
- Pure functional implementations can approach the speed of highly optimized C code, achieving **under 10 % slower** performance on a wide range of real‑world data.
- On Apple silicon, the gap narrows further (≈2–3 % slower), suggesting that Roc’s compiler and runtime generate efficient machine code for modern architectures.
- While SIMD‑heavy hand‑tuned C libraries still hold a performance edge, the results demonstrate that functional languages focused on performance can be competitive without sacrificing safety or expressiveness.