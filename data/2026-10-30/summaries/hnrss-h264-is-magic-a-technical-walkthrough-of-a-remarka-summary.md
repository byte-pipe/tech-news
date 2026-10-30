---
title: H.264 is magic: a technical walkthrough of a remarkable technology.
url: https://sidbala.com/h-264-is-magic/
date: 2026-10-29
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-10-30T12:48:29.373280
---

# H.264 is magic: a technical walkthrough of a remarkable technology.

# H.264 is magic: a technical walkthrough of a remarkable technology

## Overview
- H.264 is the dominant video compression codec used everywhere (internet video, Blu‑ray, phones, cameras, drones, etc.).
- It is the product of more than 30 years of research aimed at minimizing the bandwidth needed for full‑motion video.
- The article explains, at a high level, the main ideas behind H.264 and how many of them apply to video compression in general.

## Why compress video?
- An uncompressed 1080p @ 60 Hz frame sequence needs about 370 MB per second (1920 × 1080 × 60 × 3 bytes).
- Storing raw video is impractical: a 50 GB Blu‑ray would hold only ~2 minutes, and even fast SSDs struggle with raw data rates.
- Compression reduces the amount of data that must be stored or transmitted.

## Why H.264 compression looks impressive
- Example: a 5‑second 60 fps H.264 clip of the Apple homepage is 175 KB, while a single PNG screenshot of the same page is 1015 KB.
- The video (300 frames) is roughly 1 500 × more efficient than the PNG because H.264 discards redundant and less important information.

## Core techniques used by H.264

### Lossy compression (shedding weight)
- H.264 is a lossy codec: it throws away bits that are not crucial for perceived visual quality.
- Unlike lossless formats such as PNG, which preserve every pixel exactly, H.264 keeps only the information that matters to the viewer.

### Information entropy
- Entropy measures the minimum number of bits required to represent the information in a dataset.
- Reducing redundancy (e.g., describing “10 heads in a row” as “10 heads”) lowers the bit count without changing the underlying information.
- H.264 employs entropy coding as a lossless step after other transformations.

### Frequency‑domain transformation
- Image data can be transformed from spatial (x‑y) coordinates to a frequency domain (freqX, freqY) using transforms such as the DCT.
- Low‑frequency components (smooth gradients) cluster near the center; high‑frequency components (fine details) lie toward the edges.
- By attenuating or discarding high‑frequency components, the codec reduces detail that the human eye is less sensitive to.

### Quantization
- After moving to the frequency domain, H.264 applies a mask that zeroes out or coarsens high‑frequency coefficients.
- This “quantization” step controls how much detail is retained; even at 2 % of the original entropy, visual differences are often imperceptible.
- Quantization is the primary mechanism for the lossy reduction of data size.

### Chroma subsampling (mentioned)
- The article begins to discuss chroma subsampling, exploiting the fact that the human visual system is less sensitive to color detail than to luminance detail.

## Takeaway
- H.264 achieves its remarkable compression ratios by combining lossy techniques (weight shedding, quantization) with lossless steps (entropy coding) and by exploiting human visual perception (frequency analysis, chroma subsampling).