---
title: "5x5 Pixel font for tiny screens (Maurycy's blog)"
url: https://maurycyz.com/projects/mcufont/
date: 2026-04-20
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-23T09:46:38.301120
---

# 5x5 Pixel font for tiny screens (Maurycy's blog)

# 5x5 Pixel font for tiny screens

## Overview
- A monospaced 5 × 5 pixel font that safely draws on a 6 × 6 grid.  
- Derived from lcamtuf’s 5 × 6 `font‑inline.h`, itself inspired by the ZX Spectrum 8 × 8 font.  
- Intended for ultra‑low‑resolution OLEDs and other tiny displays used with 8‑bit microcontrollers.

## Why 5 × 5 is the minimum usable size
- 2 × 2: impossible to convey any character.  
- 3 × 3: technically possible but unreadable.  
- 4 × 4: cannot render “E”, “M”, or “W” correctly.  
- 5 × 5: large enough for legible uppercase and distinct lowercase letters, while keeping the font compact.

## Benefits of a constant width
- String length on screen = 6 × (number of characters), simplifying layout calculations.  
- Prevents overflow issues (e.g., “8978” never exceeds the width of “1111”).  
- Enables compact, predictable UI designs on constrained displays.

## Memory footprint and MCU suitability
- Whole font occupies only 350 bytes.  
- Fits comfortably in AVR128DA28 (16 kB RAM) and similar 8‑bit MCUs.  
- Larger low‑resolution displays (e.g., 384 × 288) exceed MCU memory, but practical OLED sizes (160 × 128, 128 × 64) benefit from such a tiny, hand‑crafted font.

## Real‑pixel rendering
- Physical pixels are not perfect squares; sub‑pixel arrangement creates a pseudo‑dropshadow effect that smooths the appearance.  
- On monochrome screens the effect disappears, but the font remains clearer than expected.

## Exploring even smaller grids
- **3 × 5**: 32 768 possible glyphs (27 904 distinct). “M”, “W”, “Q” degrade, but “O” and zero stay distinct; useful when needing ~50 % more columns.  
- **3 × 4**: 4 096 glyphs (3 392 distinct). No separate upper/lower case; numbers lose some clarity but remain usable.  
- **3 × 3**: 512 glyphs (400 distinct). Numbers suffer; letters are recognizable but limited.  
- **2 × 3**: 64 glyphs (44 distinct). Most letters become unrecognizable; serves only as a curiosity.  
- **3 × 2** (aspect‑ratio flipped): improves horizontal detail; still readable with effort.  
- **2 × 2**: 16 possible patterns, 10 distinct after removing duplicates; enough for digits only, essentially a secret code rather than a font.

## Related resources
- `projects/mcufont/mcufont.h` – implementation of the 5 × 5 font.  
- `projects/mcufont/test.c` – preview program for the font.  
- lcamtuf’s original `font‑inline.h`.  
- Moonbench’s collection of tiny pixel‑art fonts.