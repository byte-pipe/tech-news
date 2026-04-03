---
title: How Michael Abrash doubled Quake framerate
url: https://fabiensanglard.net/quake_asm_optimizations/index.html
date: 2026-02-17
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-17T06:02:31.019734
---

# How Michael Abrash doubled Quake framerate

# How Michael Abrash Doubled Quake Frame Rate

This article details how Michael Abrash managed to double the frame rate of the Quake game by leveraging hand-crafted assembly language optimizations. The author investigates the effectiveness of these optimizations and explores the extent of assembly code within the game.

## Establishing Stock FPS

The author first establishes the stock frame rate of the released version of Quake on a Pentium MMX 233MHz machine. This is done by running the game with specific command-line arguments to utilize the fastest audio backend and disable certain rendering features. The stock frame rate is recorded at 42.3 fps.

## Building with Assembly

The author then compiles Quake with the assembly optimizations enabled, following instructions from a 1997 guide. The initial compilation yields a frame rate very close to the stock rate, at 42.2 fps.

## Building without Assembly

To verify the impact of the assembly optimizations, the author compiles Quake without them by disabling the assembly definition in the header file. This results in a linker error, which is resolved by adding a specific file to the project. The resulting executable runs at only 22.7 fps, confirming the significant speed improvement provided by the assembly code.

## Diving into the Assembly

The article notes the extensive use of assembly language in Quake, with 63 functions spread across 21 files. A comparison is made with Doom, which has significantly fewer assembly files and functions. The author identifies several assembly functions that are either not used, are duplicates between client and server code, or rely on features not available in C. Some optimizations also utilize self-modifying code.

## Key Findings

The primary conclusion is that Michael Abrash's assembly optimizations were crucial for achieving the doubled frame rate in Quake. The assembly code handles low-level tasks that are difficult or inefficient to implement in C, significantly boosting the game's performance.
