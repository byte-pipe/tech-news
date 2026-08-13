---
title: Guillaume Técher
url: https://guillaumetech.github.io/posts/jpg-scaling-chrome/
date: 2026-08-12
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-13T11:43:22.002730
---

# Guillaume Técher

# Why Tiny JPEGs Look Different in Chrome

## Observation
- Noticed a logo rendered thinner on a colleague’s computer (Chrome) compared to mine (Firefox).  
- Swapping the image for an SVG fixed the visual difference.  
- Curious about the underlying cause.

## Scaling down images can be wasteful
- Traditional approach: fully decompress JPEG, then scale down.  
- Example: a 2000 × 2000 JPEG (≈12 MB uncompressed) displayed at 20 × 20 (≈1.2 KB) wastes memory and processing.  
- Most of the original data is discarded during heavy down‑scaling.

## What information is lost when scaling down?
- High‑frequency details (rapid pixel‑to‑pixel changes) disappear first.  
- Example: a detailed tree becomes a simple green blob and brown stick when reduced to a tiny size.  
- Some high‑frequency information mixes into lower frequencies, but the majority is lost.

## How JPEG stores image data
- JPEG splits the image into 8 × 8 blocks and applies a Discrete Cosine Transform (DCT).  
- Each block’s frequency components are represented by coefficients:  
  - Low frequencies → flat colors (constant component).  
  - High frequencies → checkerboard‑like patterns (basis functions).  
- Lossy compression occurs later when coefficients are quantized, but that detail is not needed for the current discussion.

## Rendering a JPEG at 1/8 scale
- When shrinking by a factor of 8, each 8 × 8 block maps to a single pixel in the output.  
- Only low‑frequency coefficients are required; high‑frequency coefficients can be omitted.  
- This “partial IDCT scaling” reduces both memory usage and decoding time.  
- The technique works for any scaling ratio whose denominator is a power of 8 and can also be used for upscaling.

## How Chrome fits in
- Chrome uses the Skia graphics library, which relies on libjpeg‑turbo for JPEG decoding.  
- libjpeg‑turbo implements partial IDCT scaling, decoding only the needed low‑frequency data when the target size is small.  
- Chrome computes the nearest fraction with denominator 8, decodes at that scale, then applies a conventional down‑sampling step to reach the final size.  
- The observed thicker appearance resulted from decoding at one‑eighth scale, where only the constant component remained, removing edge softening and gradients.  
- A later correction notes that the final visual quality also depends on the subsequent scaling algorithm.

## Takeaway
- JPEG is optimized for photographic content, not for small icons or UI graphics.  
- Use vector formats (e.g., SVG) or lossless raster formats for icons to avoid unintended visual artifacts caused by JPEG’s scaling optimizations.