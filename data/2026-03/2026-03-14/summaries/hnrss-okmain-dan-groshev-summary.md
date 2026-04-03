---
title: Okmain | Dan Groshev
url: https://dgroshev.com/blog/okmain/
date: 2026-03-09
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-14T06:03:14.548564
---

# Okmain | Dan Groshev

# Okmain – extracting a pleasant main colour from an image

## Problem
- Cards often need a solid background colour that reflects the image.
- Simple 1×1 resize (average in sRGB) yields dull, muddy colours even for vivid images.

## Approach
- Developed **Okmain**, a Rust library with a Python wrapper, that selects an “OK main” colour using several techniques:
  - Colour clustering
  - Averaging in Oklab colour space
  - Heuristic cluster sorting based on prominence

## Colour clustering
- Images usually contain several distinct colour groups; averaging all pixels loses vibrancy.
- Uses k‑means clustering on pixel colours (ignoring positions) with a maximum of four clusters.
- If clusters are too similar, the algorithm reduces the number of clusters.
- Example images show clear separation into sky, field, etc., and handling of cases with fewer than four distinct groups.

## Oklab colour space
- sRGB averaging is problematic because:
  1. Gamma correction is non‑linear, so linear operations give incorrect results.
  2. Perceived colour intensity is non‑linear, causing muddy mixes.
- Converting colours to Oklab, averaging there, then converting back to sRGB produces smoother, less brownish results.
- Demonstrated with gradient mixes where Oklab averaging yields a visually smoother transition.

## Cluster sorting (prominence heuristics)
- After clustering, the library ranks clusters to pick the most visually dominant colour.
- Three heuristics combined:
  1. **Pixel count** – larger clusters are more important.
  2. **Centrality** – pixels nearer the image centre receive higher weight (using a default radial mask).
  3. **Colour vividness** – Oklab chroma (saturation) used as a proxy for visual prominence.
- The weighted combination ensures foreground colours (e.g., a green subject) outrank background greys.

## Performance
- Goal: comparable speed to a 1×1 resize.
- Steps taken:
  - Down‑sample image by powers of two until ≤ 250 000 pixels, averaging in Oklab2; also removes noise.
  - De‑interleave RGB data into three separate float arrays for SIMD‑friendly processing.
  - Fixed four‑cluster limit fits into a SIMD register (f32x4).
  - Use K‑means++ initialization; full‑dataset passes are faster than mini‑batch for the reduced size.
  - Current implementation runs on multi‑megapixel images in ~100 ms on SSE2; AVX2 dispatch planned for further speedup.

## LLM development tangent
- Experimented with LLM agents (Opus 4.5/4.6) for auto‑generating parts of the library.
- Initial code was quickly produced but contained subtle bugs and poor vectorisation hints.
- Iterative debugging with `cargo asm` was token‑intensive; ultimately manual rewrites were required for quality.

## Availability
- Library published on **crates.io** (Rust) and **PyPI** (Python).
- Accompanied by documentation and the blog post describing the methodology.