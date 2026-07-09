---
title: iOS 27’s new RAW 9 engine promises to dramatically improve photo quality - 9to5Mac
url: https://9to5mac.com/2026/07/06/apple-overhauls-raw-photo-processing-with-ios-27-showcases-impressive-results/
date: 2026-07-10
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-10T09:10:47.002200
---

# iOS 27’s new RAW 9 engine promises to dramatically improve photo quality - 9to5Mac

# Summary of iOS 27’s new RAW 9 engine promises to dramatically improve photo quality

## Overview
- iOS 27 (along with macOS 27 and iPadOS 27) introduces RAW 9, the latest version of Apple’s system‑level RAW image‑processing pipeline.  
- RAW 9 is described by Apple as “its biggest update yet,” leveraging on‑device machine‑learning via the Apple Neural Engine.

## Key Improvements
- Combines demosaicing and denoising in a tiled Core ML model for higher‑quality rendering.  
- Enhances detail, sharpness, and color fidelity while significantly reducing noise, even on very high‑ISO images.  
- Works on legacy RAW files, allowing older photos to be reprocessed with the new engine.

## Technical Details
- Implemented as a Core Image extension; developers enable it through updated APIs.  
- Runs entirely on‑device, ensuring optimal performance without needing cloud processing.  
- Apple provides guidance on optimizing editing and export workflows for RAW 9.

## Demonstrated Results
- **Low‑noise Sony Alpha 7 II image:** RAW 9 yields sharper text and clearer fine details compared with RAW 8.  
- **High‑noise Canon 5D Mark III (ISO 51,200):** RAW 9 restores accurate colors and reveals specular highlights that RAW 8 could not.  
- **Fujifilm X‑T5 (ISO 12,800) with unconventional sensor pattern:** RAW 9 reduces color artifacts, improves texture detail, and makes small text more legible.

## Developer Guidance
- WWDC 26 session “Enhance RAW image processing with Core Image” covers enabling RAW 9, performance tuning, and export considerations.  
- Full session video is available for deeper technical insight.

## Additional Context
- Apple’s RAW pipeline already supports nearly 800 third‑party camera models via Core Image.  
- The article includes affiliate product recommendations and links to 9to5Mac’s social channels, but these are unrelated to the RAW 9 announcement.