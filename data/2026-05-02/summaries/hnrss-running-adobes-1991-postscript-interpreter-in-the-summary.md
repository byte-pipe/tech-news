---
title: Running Adobe’s 1991 PostScript Interpreter in the Browser – pagetable.com
url: https://www.pagetable.com/?p=1854
date: 2026-05-01
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-02T08:47:46.275401
---

# Running Adobe’s 1991 PostScript Interpreter in the Browser – pagetable.com

# Running Adobe’s 1991 PostScript Interpreter in the Browser

## Overview
- The HP C2089A “PostScript Cartridge Plus” (1991) adds PostScript Level 2 support to LaserJet II/III using Adobe’s reference interpreter (v2010.118) stored in a 2 MB ROM.  
- Thirty‑five years later the ROM still implements a correct, current PostScript language.  
- The project **retro‑ps** emulates the original M68K hardware, fakes the LaserJet mainboard, and runs the interpreter either from the command line or in the browser (pagetable.com/retro-ps).  
- Users can drop a .ps file onto the page; the cartridge’s rasterizer renders it entirely client‑side, with no server involvement.

## Hardware details
- Host: LaserJet III formatter board with a Motorola 68000 CPU @ 8 MHz, 1 MB RAM (expandable to 4 MB).  
- Cartridge port maps external ROM into the CPU address space; memory‑mapped registers communicate with the print engine.  
- The C2089A cartridge supplies the PostScript interpreter, fonts, halftone tables, and banding logic from its ROM, using the formatter’s RAM for working memory.

## Emulator Internals
- Original constraints (300 DPI, fixed paper sizes, 0.25″ margin) are lifted; the emulator allows any DPI up to the cartridge’s clipping limit, arbitrary paper sizes, custom halftone frequencies, and no margin (the `--lj3` flag restores original limits).  
- **CPU and RAM**: Emulated 68020 sees up to 16 MB RAM, providing headroom for high‑DPI rendering without modifying the allocator.  
- **Mainboard and engine**: Only the cartridge ROM is present; the emulator supplies soft‑traps for printer‑model byte, IPC byte stream, engine‑status polling, and fakes the engine‑done interrupt to advance the state machine.  
- **Halftone scaling**: Adobe’s hand‑tuned 300 DPI halftone cell appears sparse at higher DPI; a DPI‑scaled `setscreen` prolog is injected to improve quality.  
- **Pixel ceiling**: The interpreter’s `clip` operator caps device pixels at ~16 000 per axis, limiting practical DPI (≈ 1450 DPI on Letter size).

## Future Work
- Emulate other cartridge ROMs, e.g., Pacific Page P·E.  
- Support LaserJet 4M and later models, which use an Intel i960 formatter with built‑in PostScript Level 2 ROM (no cartridge required).