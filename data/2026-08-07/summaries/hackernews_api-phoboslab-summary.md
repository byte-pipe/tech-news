---
title: PhobosLab
url: https://phoboslab.org/log/2026/08/xibalba64-making-of
date: 2026-08-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-07T06:01:31.644438
---

# PhobosLab

# How to Make a Nintendo 64 Game in 2026 – Summary

## Overview
- After porting my JavaScript engine Impact to C, I used it to create **Xibalba 64**, a Wolfenstein‑like FPS for the N64.  
- Modretro will publish it as a physical cartridge for their modern N64 clone (M64).  
- This is only the second new N64 game released physically since the console’s commercial end (the first being *Xeno Crisis* in 2023).

## The Engine (high_impact)
- **high_impact** is the C port of the original Impact engine, featuring a modular “platform backend” (SDL2, Sokol) and interchangeable rendering backends (software, OpenGL, Metal).  
- This design lets the same game code run on many devices and makes it easy to add new platforms or renderers without touching core engine code.  
- The engine’s flexibility provides a solid foundation for an N64 target.

## N64 Hardware & Platform Library
- The N64 contains a 93 MHz big‑endian MIPS CPU plus two coprocessors: the Reality Display Processor (RDP) and the Reality Signal Processor (RSP), together forming the Reality Coprocessor (RCP).  
- Historically, Nintendo restricted RSP access to its proprietary libultra library; using it today risks copyright issues.  
- **Libdragon** serves as an open‑source “SDL for the N64,” offering sprite/triangle drawing, sound, controller input, and more.  
- I built a new high_impact platform backend on top of Libdragon in a few evenings; the game ran unmodified, albeit with modest performance.

## Development Environment
- Libdragon supplies the compiler toolchain and ROM‑building utilities; the preview branch is recommended over the lagging stable trunk.  
- Accurate emulation is now possible with the Ares core, which fully emulates RDP and RSP timing, though real‑hardware testing is still needed for memory‑bandwidth behavior.  
- For hardware testing I used a **SummerCart64** cartridge (USB‑C enabled) to upload ROMs directly from the PC via `sc64deployer`.  
- A cheap USB analog capture card and a small mpv script allowed low‑latency video capture of the N64 output on my desktop, enabling rapid compile‑and‑run cycles.

## Game Porting & Expansion
- The original Xibalba demo (2014) was a short WebGL‑based 3D shooter; for Xibalba 64 I expanded levels, enemies, and weapons to make a full game.  
- Although high_impact is 2D‑oriented, the game’s flat‑world design lets it be treated as 2D physics with a 3D rendering perspective.  
- Added a `vec3_t` type (union of `vec2_t` and explicit `x, y, z` fields) to satisfy both physics (2D) and rendering (3D) needs without extra conversion cost.  
- Ported existing assets in ~2 weeks; spent additional months refining the renderer and integrating Libdragon’s audio mixer and image loader.  
- Retained SDL2/Sokol backends for quick playtesting and implemented a hot‑reload system to update levels on the fly.

## Release & Significance
- Xibalba 64 will be sold as a cartridge with packaging and manual, marking a rare modern physical release for the legacy console.  
- The project demonstrates that with a modular engine, open‑source N64 libraries, and a modest hardware setup, creating new commercial‑grade N64 titles is feasible in 2026.