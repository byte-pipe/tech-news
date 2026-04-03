---
title: The Optimization Ladder - Cemrehan Çavdar
url: https://cemrehancavdar.com/2026/03/10/optimization-ladder/
date: 2026-03-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-15T06:01:52.800212
---

# The Optimization Ladder - Cemrehan Çavdar

# The Optimization Ladder – Cemrehan Çavdar

## Introduction
- Yearly benchmarks claim Python is 100× slower than C, sparking debates about relevance.
- The author reproduced two classic Benchmarks Game problems (n‑body, spectral‑norm) and added a JSON event pipeline to evaluate real‑world code.
- Experiments run on an Apple M4 Pro using CPython 3.13 as the baseline.

## Baseline Benchmark Results (CPython 3.13 vs. C gcc)
- **n‑body (50 M)**: 2.1 s vs. 372 s → 177× slower  
- **spectral‑norm (5500)**: 0.4 s vs. 350 s → 875× slower  
- **fannkuch‑redux (12)**: 2.1 s vs. 311 s → 145× slower  
- **mandelbrot (16000)**: 1.3 s vs. 183 s → 142× slower  
- **binary‑trees (21)**: 1.6 s vs. 33 s → 21× slower  

The goal is not to prove Python slow, but to show how much effort each optimization yields.

## Why Python Is Slow
- **Dynamic design**: Python allows runtime monkey‑patching, builtin replacement, and class hierarchy changes, forcing every operation to perform type checks and dispatch.
- **Object overhead**: A Python `int` occupies at least 28 bytes (reference count, type pointer, size, digit array) versus 4 bytes for a C `int`. Each arithmetic operation involves pointer dereferencing, slot lookup, possible allocation, and reference‑count updates.
- **GIL**: Does not affect single‑threaded performance; removing it (free‑threaded mode) actually slows single‑threaded code due to extra reference‑count handling.
- **Interpretation overhead**: CPython 3.11 introduced adaptive specialization (type‑specialized bytecodes) giving ~1.4× speedup. CPython 3.13 added an experimental copy‑and‑patch JIT, but early results show little gain.

## The Optimization Ladder

### Rung 0 – Upgrade CPython
- **Cost**: Change the Python version in the environment.
- **Reward**: Up to ~1.4× faster.
- **Results**:
  - 3.10 → 3.11: ~1.39× speedup on n‑body (adaptive specialization).
  - 3.13 adds modest gains; 3.14 shows slight regression.
  - Free‑threaded 3.14t is slower on single‑threaded workloads.

### Rung 1 – Alternative Runtimes (PyPy, GraalPy)
- **Cost**: Switch interpreter; no code changes.
- **Reward**: 6–66× faster.
- **Results**:
  - **PyPy**: n‑body 98 ms (13×), spectral‑norm 1,065 ms (13×).
  - **GraalPy**: n‑body 211 ms (5.9×), spectral‑norm 212 ms (66×).
- **Trade‑offs**:
  - Compatibility with C extensions may be slower.
  - GraalPy runs on the JVM, has slower startup and currently targets Python 3.12.

### Rung 2 – Mypyc (Ahead‑of‑Time Compilation)
- **Cost**: Add type annotations (often already present) and compile with `mypyc`.
- **Reward**: 2.4–14× faster.
- **Results**:
  - n‑body 518 ms (2.4×), spectral‑norm 990 ms (14×) compared to CPython 3.14.
- **Approach**: `mypyc` translates type‑annotated Python into C extensions, preserving Python semantics while eliminating dynamic dispatch for annotated variables.

*(Further rungs such as Cython, Rust bindings, or hand‑written C extensions are discussed later in the original article but are not covered in this excerpt.)*