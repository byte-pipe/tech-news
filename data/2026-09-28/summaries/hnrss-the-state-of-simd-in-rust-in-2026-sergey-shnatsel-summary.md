---
title: "The state of SIMD in Rust in 2026 | Sergey \"Shnatsel\" Davidoff"
url: https://shnatsel.github.io/state-of-simd-rust-2026/
date: 2026-09-25
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-28T13:23:09.006544
---

# The state of SIMD in Rust in 2026 | Sergey "Shnatsel" Davidoff

# The state of SIMD in Rust in 2026 – Summary

## Introduction
- The author reports significant progress since the previous year’s survey and notes personal contributions to the SIMD ecosystem.
- After contributing to the most promising SIMD library, the author became a maintainer of **Fearless SIMD**.
- To avoid conflicts of interest, authors of other SIMD libraries (std::simd, wide, pulp, macerator) reviewed the draft; editorial control remained with the author.

## What is SIMD and why does it matter?
- Modern CPUs have abundant arithmetic units but a single instruction‑decode stage, leading to under‑utilisation of the arithmetic hardware.
- SIMD (single instruction, multiple data) feeds a batch of numbers to a single arithmetic instruction, allowing operations on vectors instead of scalars.
- On recent x86 CPUs vectors can be up to 512 bits, theoretically giving up to 8× speed‑up for f64 or 64× for u8, though real‑world results vary.

## SIMD instruction‑set landscape
- SIMD extensions are added after the base architecture and have distinct marketing names:
  - ARM 64: **NEON** (mandatory on all 64‑bit ARM cores)
  - WebAssembly: **128‑bit packed SIMD extension**
  - x86‑64: **SSE2** (baseline 128‑bit), later extensions include SSE 4.2, AVX, AVX2 (256‑bit), AVX‑512 (512‑bit)
- On x86‑64 the presence of a given extension cannot be assumed; the compiler defaults to SSE2 compatibility.

## Detecting CPU capabilities
- **Static targeting**: compile for a specific CPU feature set (e.g., `RUSTFLAGS='-C target-cpu=x86-64-v3'`) – suitable for controlled environments.
- **Function multiversioning**: compile multiple versions of a function for different SIMD levels and select at runtime based on `cpuid` checks.
- ARM’s NEON is mandatory on AArch64, simplifying detection. WebAssembly requires separate binaries (SIMD vs. non‑SIMD) and a JavaScript feature test.

## Ways to use SIMD in Rust
1. **Automatic vectorization** – write plain Rust and rely on the compiler to generate SIMD instructions.
2. **Portable SIMD abstractions** – use high‑level vector types such as `i32x4`, `f32x8`.
3. **Platform‑specific intrinsics** – call low‑level functions like `_mm_add_epi32` (x86) or `vaddq_u32` (NEON).

## Automatic vectorization
- Works best when code is written in a vector‑friendly style (e.g., iterating over `&[i32].as_chunks()`).
- Advantages:
  - No extra dependencies.
  - Automatically benefits from any instruction set the compiler supports.
- Drawbacks:
  - Unreliable for large or complex functions; compiler may fail to vectorize.
  - Performance varies with compiler version and surrounding code.
  - Floating‑point operations need special handling; Rust 1.98 introduced `algebraic_add` to allow safe re‑ordering.

### The `multiversion` crate
- Provides attribute‑based multiversioning: `#[multiversion(targets = "simd")]`.
- Small runtime overhead (≈ dozen instructions) can be noticeable for tiny functions.
- Recommendation: apply `#[multiversion]` to functions containing loops; use `#[inline(always)]` for small, leaf‑level functions.
- Allows explicit selection of CPU extensions, unlike other crates that target predefined SIMD levels.
- For AVX‑512, the crate only checks presence, not performance characteristics, which may lead to sub‑optimal choices.

## Portable SIMD abstractions
- Desired features:
  - Fixed‑width vectors (`f32x4`, `u8x16`) for predictable size.
  - Hardware‑width vectors that automatically use the widest available lane.
  - Generic over element type (e.g., same code works for `f32` and `f64`).
  - Generic over vector width (code works across `f32x4`, `f32x8`, `f32x16`).
- Production‑ready crates:
  - `std::simd` (nightly)
  - `fearless-simd`
  - `wide`
  - `pulp`
  - `macerator`

## Comparison of SIMD crates

| Feature                              | std::simd (nightly) | fearless‑simd | wide | pulp | macerator |
|--------------------------------------|--------------------|---------------|------|------|-----------|
| Fixed‑width vectors                  | ✅                | ✅            | ✅   | ✅   | ✅         |
| Hardware‑width vectors               | ✅ (crate)         | ✅ (crate)    | ✅   | ✅   | ✅         |
| Generic over element type            | ✅                | ✅            | ✅   | ✅   | ✅         |
| Generic over vector width             | ✅                | ✅            | ✅   | ✅   | ✅         |
| Built‑in multiversion support         | ✅                | ✅            | ❌   | ✅   | ❌         |

## Conclusions
- SIMD in Rust has matured considerably, with multiple viable abstraction layers and tooling for runtime feature detection.
- Automatic vectorization remains attractive for simple cases but requires careful coding and benchmarking.
- The `multiversion` crate fills a niche for fine‑grained control over CPU feature selection, though its overhead must be managed.
- Among portable SIMD libraries, `fearless‑simd` and `std::simd` offer the most complete feature sets, while `wide`, `pulp`, and `macerator` provide solid alternatives depending on project constraints.