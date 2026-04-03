---
title: TurboQuant: Redefining AI efficiency with extreme compression
url: https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/
date: 2026-03-25
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-26T01:03:47.906839
---

# TurboQuant: Redefining AI efficiency with extreme compression

# TurboQuant: Redefining AI efficiency with extreme compression

## Overview
- Introduces three theoretically grounded quantization algorithms:
  - **TurboQuant** – primary compression method.
  - **Quantized Johnson‑Lindenstrauss (QJL)** – 1‑bit error‑correction trick.
  - **PolarQuant** – angle‑based representation to remove memory overhead.
- Targeted at reducing memory bottlenecks in key‑value (KV) caches and speeding up vector search for large language models (LLMs) and retrieval systems.
- Presented at ICLR 2026 (TurboQuant) and AISTATS 2026 (QJL, PolarQuant).

## How TurboQuant Works
1. **PolarQuant stage**
   - Randomly rotates vectors to simplify geometry.
   - Applies a high‑quality quantizer to each rotated component.
   - Captures the bulk of the information (most bits) as radius and angle values.
2. **QJL stage**
   - Uses a 1‑bit Johnson‑Lindenstrauss transform on the residual error from PolarQuant.
   - Provides a zero‑overhead bias correction, improving attention‑score accuracy.

## QJL: Zero‑overhead 1‑bit Trick
- Projects high‑dimensional data onto a single sign bit (+1 / –1) while preserving distances.
- Employs a special estimator that balances a high‑precision query with the low‑precision representation.
- Enables accurate attention calculations without extra memory.

## PolarQuant: “Angle” Compression
- Converts Cartesian coordinates to polar coordinates (radius + angle).
- Groups coordinate pairs recursively, reducing a d‑dimensional vector to one radius and several angles.
- Fixed, predictable angular grid eliminates the need for costly data‑normalization steps and removes traditional memory overhead.

## Experimental Results
- Benchmarks: LongBench, Needle‑In‑A‑Haystack, ZeroSCROLLS, RULER, L‑Eval using open‑source LLMs (Gemma, Mistral).
- **Performance**
  - Maintains dot‑product fidelity and recall while cutting KV memory by ≥ 6×.
  - Achieves loss‑less results on needle‑in‑haystack tasks; PolarQuant nearly loss‑less as well.
- **Bit‑width**
  - Quantizes KV cache to 3 bits without training or fine‑tuning, preserving model accuracy.
- **Speed**
  - 4‑bit TurboQuant yields up to 8× faster attention‑logit computation on H100 GPUs compared with 32‑bit unquantized keys.
  - Negligible runtime overhead; implementation is straightforward.

## Implications
- Enables large‑scale LLMs to operate with far smaller memory footprints, facilitating longer context windows and cheaper inference.
- Benefits any compression‑dependent application, especially search engines and AI systems relying on fast vector similarity lookups.