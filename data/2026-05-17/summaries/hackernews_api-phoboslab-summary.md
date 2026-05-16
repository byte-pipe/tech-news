---
title: PhobosLab
url: https://phoboslab.org/log/2026/05/n64-additive-blending
date: 2026-05-16
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-17T06:01:52.541463
---

# PhobosLab

# Additive Blending on the Nintendo 64

## Overview
- Explains why explosions and similar effects appear more vivid on the original PlayStation than on the Nintendo 64.  
- The N64 does support additive blending, but its lack of clamping causes color wrap‑around, making the effect look wrong.

## PlayStation blending
- PSX offers four blend modes; the simplest is `src + dst`.  
- Colors are added and then clamped to the maximum range (255 for 8‑bit, 31 for 5‑bit components).  
- This produces consistently brighter results, ideal for explosions, plasma beams, and magic spells.

## N64 blending problem
- The Reality Display Processor (RDP) uses a configurable “Color Combiner” similar to `glBlendFunc`.  
- Using `RDPQ_BLENDER((IN_RGB, IN_ALPHA, MEMORY_RGB, ONE))` performs additive blending, but the RDP does **not** clamp the result.  
- Example: adding sprite (171, 42, 226) to framebuffer (63, 141, 170) yields (234, 183, 140) where the blue channel wraps around instead of reaching 255.

## Proposed solution
1. **Render to a 32‑bit RGBA8888 buffer** while keeping sprite assets in 16‑bit RGBA5551 format.  
2. **Pre‑scale sprite intensity to 1/8** by abusing the fog‑alpha value, giving ample headroom for additive sums without overflow.  
3. **After rendering, convert the 32‑bit buffer to 16‑bit** for display, clamping each 8‑bit component to the 5‑bit range.  
4. Perform the conversion on the Reality Signal Processor (RSP) using its 128‑bit vector instructions, processing eight pixels at a time.  
   - CPU‑only conversion takes ~70 ms for a 320×240 frame.  
   - RSP implementation reduces this to ~3.1 ms.

## Implementation steps
- Initialise the display with a 16‑bit framebuffer (`DEPTH_16_BPP`).  
- Allocate a secondary 32‑bit surface (`FMT_RGBA32`) and set it as the RDP color image.  
- Set fog color to `(0, 0, 0, 256/8)` and configure the blender with `IN_RGB, FOG_ALPHA, MEMORY_RGB, ONE`.  
- Render the scene, drawing all additive‑blended sprites onto the 32‑bit target.  
- Invoke the RSP routine `rsp_rgba_8888_to_5551` to copy and clamp the 32‑bit buffer into the 16‑bit screen buffer.  
- Present the final 16‑bit framebuffer with `display_show`.

## Performance considerations
- Rendering to a 32‑bit buffer roughly doubles memory traffic because the RDP must read and write twice as many bytes from RDRAM.  
- Despite the overhead, the technique is viable for many applications.  
- Further optimizations are possible, such as rendering only the additive sprites to the 32‑bit buffer, using a lower resolution for that pass, and then compositing with the rest of the scene on the RSP.

## Resources
- Demo project illustrating the technique: `github.com/phoboslab/n64_addblend`.  
- Mention of the RSPL language, a C‑like language that compiles to RSP microcode, simplifying development without hand‑written MIPS assembly.