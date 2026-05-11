---
title: Training an LLM in Swift, Part 1: Taking matrix multiplication from Gflop/s to Tflop/s | Cocoa with Love
url: https://www.cocoawithlove.com/blog/matrix-multiplications-swift.html
date: 2026-05-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-12T06:03:17.599314
---

# Training an LLM in Swift, Part 1: Taking matrix multiplication from Gflop/s to Tflop/s | Cocoa with Love

# Training an LLM in Swift, Part 1: Taking matrix multiplication from Gflop/s to Tflop/s

## Introduction
- The article explores how to hand‑write and heavily optimise matrix‑multiplication kernels in Swift for training a GPT‑2‑compatible LLM.
- It demonstrates performance differences across Apple Silicon compute units: CPU, SIMD, AMX, and GPU (Metal).
- The goal is to show that a pure‑Swift implementation can approach or surpass the speed of a plain‑C reference.

## Reference implementation (llm.c)
- Uses a simple nested‑loop `matmul_forward` function that computes `out = inp * weight + bias`.
- Each inner iteration performs two floating‑point operations; a full training iteration requires roughly  
  `6 × N × D ≈ 0.2 trillion` FLOPs (with `N = 124,439,808` weights and `D = B·T = 256`).
- Baseline performance of the C code (compiled with `-O3`) is about 0.92 tokens/s and 0.174 training iterations/s (≈1 iteration every 7 s).

## Basic Swift translation
- The Swift version mirrors the C loops almost line‑by‑line, using native Swift arrays.
- Runtime checks are disabled (`-remove-runtime-asserts`) and the code is always run in Release mode to keep it comparable to the C version.
- Despite these measures, the initial Swift implementation is still “extremely slow”.

## Motivation and context
- The author rediscovered an old C++ image‑recognition thesis and felt limited by Python‑based ML frameworks that hide the actual computation.
- Andrej Karpathy’s `llm.c` (a ~1000‑line plain‑C GPT‑2 model) inspired a rewrite in Swift to gain full control over the low‑level math.
- This article is the first in a series that will later compare Apple’s ML frameworks and explore additional optimisation techniques.

## What follows in the series
- Subsequent parts will cover:
  - Using SIMD, AMX, and Metal to accelerate the kernels.
  - Profiling and benchmarking across different hardware units.
  - Integrating the optimised kernels into a complete training loop.
  - Comparing hand‑written kernels with Apple’s official ML libraries.