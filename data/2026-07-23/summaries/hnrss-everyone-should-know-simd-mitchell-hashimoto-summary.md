---
title: Everyone Should Know SIMD – Mitchell Hashimoto
url: https://mitchellh.com/writing/everyone-should-know-simd
date: 2026-07-22
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-23T19:02:12.664905
---

# Everyone Should Know SIMD – Mitchell Hashimoto

# Everyone Should Know SIMD

## Background: What Is SIMD?

- SIMD lets a CPU operate on multiple data values in parallel, e.g., comparing several bytes with one instruction.  
- Any simple loop that processes bytes, characters, or array elements can be rewritten to handle chunks (e.g., 4‑ or 8‑byte vectors) instead of single items.  
- The speedup is proportional to the vector width, but only worthwhile when the loop processes hundreds or more elements.  
- Extreme SIMD projects exist, but everyday code can benefit from the much simpler, common pattern.

## The Common Shape

The typical “process N values at a time” SIMD routine follows five steps:

1. Broadcast needed constants and create any vector accumulators.  
2. Loop over the input in vector‑width chunks.  
3. Perform the desired comparison or arithmetic across all lanes simultaneously.  
4. Reduce the vector result or store it as required.  
5. Finish with a scalar tail that handles the remaining elements that don’t fill a full vector.

Repeated practice makes these steps feel as natural as writing a scalar loop.

## A Real Example

- **Problem:** Find the first codepoint ≤ 0xF in a slice of decoded Unicode codepoints.  
- **Scalar version:** A single `while` loop increments `end` one element at a time.  
- **SIMD version:** Uses Zig’s generic vector constructs (no CPU‑specific intrinsics) and follows the five‑step shape.  
- **Performance:** Up to 4× faster on ARM NEON, 8× on AVX2, 16× on AVX‑512; real‑world gains around 5× on an AVX2 desktop.

### Step 1 – Broadcast Constants

- `simd.lanes(u32)` returns the number of 32‑bit lanes the CPU can process (4, 8, or 16).  
- `@Vector(lanes, u32)` defines the vector type for that lane count.  
- `@splat(0xF)` creates a vector where every lane contains the constant `0xF`.  
- No accumulator is needed for this algorithm.

### Step 2 – Loop One Vector at a Time

- Loop condition `end + lanes <= cps.len` ensures a full vector can be loaded.  
- Inside the loop, `values = cps[end ..][0 .. lanes]` loads the next chunk into a vector.  
- `end += lanes` advances the index by the vector width.  
- Remaining elements that don’t fill a vector are left for the scalar tail.

### Step 3 – Perform the SIMD Operation

- `greater_than_threshold = values > threshold` performs a lane‑wise comparison in a single instruction.  
- The result is a boolean vector indicating which lanes exceed `0xF`.

### Step 4 – Reduce the Vector Result

- `@reduce(.And, greater_than_threshold)` checks if *all* lanes satisfy the condition; if so, the loop continues.  
- Otherwise, the vector is bit‑cast to an integer mask, the trailing zeros (`@ctz(~mask)`) locate the first failing lane, `end` is advanced accordingly, and the loop breaks.

### Step 5 – Scalar Tail

- After the vector loop, a regular scalar `while` processes any leftover elements that didn’t fit into a full vector.

## Recap of the Common Shape

- Broadcast constants → create vector type.  
- Loop over full vectors → load, advance index.  
- Execute SIMD operation → lane‑wise compute.  
- Reduce/store result → decide continuation or break.  
- Handle remainder with scalar code.

## Why Can’t the Compiler Do This Automatically?

- Compilers often lack enough information about data alignment, loop invariants, or desired vector width to generate optimal SIMD code automatically.  
- Explicit SIMD lets developers guarantee the exact behavior, handle edge cases, and achieve the maximum possible speedup.

## Everyone Should Know SIMD

- Understanding the five‑step pattern makes SIMD approachable for most developers.  
- Once mastered, writing SIMD code is comparable in effort to writing a normal loop.  
- Knowing SIMD empowers developers to write faster, more efficient programs without relying on obscure, niche optimizations.