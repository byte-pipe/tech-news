---
title: Running Adobe’s 1991 PostScript Interpreter in the Browser – pagetable.com
url: https://www.pagetable.com/?p=1854
site_name: hnrss
content_file: hnrss-running-adobes-1991-postscript-interpreter-in-the
fetched_at: '2026-05-02T08:46:43.155632'
original_url: https://www.pagetable.com/?p=1854
date: '2026-05-01'
description: Running Adobe's 1991 PostScript Interpreter in the Browser
tags:
- hackernews
- hnrss
---

TheHP C2089A “PostScript Cartridge Plus”, a 1991 add-on for the LaserJet II/III, adds PostScript Level 2 support through Adobe’s own reference interpreter (version 2010.118) on a 2 MB ROM.

Thirty-five years on, that ROM is still a current PostScript implementation: it renders the language correctly, and the language hasn’t changed. We have Ghostscript today, but this is Adobe’s own reference implementation! Old code is not always retro code: Why not use it productively today?

retro-pstakes that ROM, emulates the M68K it ran on, fakes the LaserJet mainboard around it, and runs the result on the command line — or in the browser atpagetable.com/retro-ps. Drop a.psfile onto the page; the cart’s own rasterizer renders it client-side. There is no server.

## Hardware details

The LaserJet III is the host. Its formatter board has a Motorola 68000 at 8 MHz, 1 MB of system RAM (expandable to 4 MB), a cartridge port that maps an external ROM into the CPU’s address space, and memory-mapped registers for talking to the print engine. The C2089A “PostScript Cartridge Plus” plugs into that cartridge. The PostScript interpreter, fonts, halftone, and banding all run from cart ROM, working out of formatter RAM.

## Emulator Internals

The cart was built to drive a LaserJet III: 300 DPI, fixed paper sizes, 0.25″ hardware margin. The PostScript interpreter inside is general — those constraints are the printer’s, not the language’s. retro-ps lifts them: any DPI up to the cart’s clip cap, any paper size, any halftone frequency, no margin. (--lj3puts the original constraints back.) A few things made that work:

* CPU and RAM.The emulator’s 68020 sees more memory than the original 68000 could address. 16 MB of RAM here. That headroom is what lets the cart render high-DPI pages without rewriting its allocator.
* No mainboard, no engine.We have the cart ROM, not the LaserJet’s mainboard ROM, and no print engine. The emulator stands in for the soft-traps the mainboard provides (printer-model byte, IPC byte stream, engine-status polling) and fakes the engine-done interrupt so the cart’s state machine moves on.
* Halftone scaling.Adobe hand-tuned the cart’s halftone cell for 300 DPI; above that the default cell renders too sparse and grayscale fills look chalky. We inject a DPI-scaledsetscreenprolog.
* Pixel ceiling.The PS interpreter’sclipoperator caps content at about 16,000 device pixels per axis. This is a limit in Adobe’s code; the practical DPI max scales with paper size (≈ 1450 DPI on Letter).

## Future Work

* Other cartridge ROMs.Pacific Page P·Ewould be the obvious next target.
* LaserJet 4M and later. Same Adobe code, different CPU: the 4-series formatter is Intel i960-based with PostScript Level 2 baked into the formatter ROM — no cartridge.