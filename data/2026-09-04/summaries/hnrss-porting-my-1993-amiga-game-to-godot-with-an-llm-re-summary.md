---
title: Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly — Babylonian Twins
url: https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/
date: 2026-09-03
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-04T07:25:48.573214
---

# Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly — Babylonian Twins

# Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly

## Background
- In 1993 I created *Babylonian Twins* on an Amiga 500 using pure 68000 assembly, with no OS assistance, direct hardware control, and limited resources due to sanctions in Iraq.  
- The game was the first commercial Iraqi game but remained largely unseen because of the collapse of Commodore and lack of publishers.  
- It was rediscovered in 2008 via an Amiga forum and later ported by the original team to iPhone in 2010 (≈34 000 lines of C++), achieving over two million downloads.  
- I did not participate in that port; I only gave feedback and made a few decisions.

## Why I tried again
- Earlier, an LLM struggled to interpret my binary level maps, requiring many hints.  
- With Claude Fable 5 I wanted to test whether a model with less exposure to Amiga assembly could reconstruct the code more autonomously.  
- I defined three conditional steps:  
  1. Port the 2010 C++ engine to Godot 4 (control case).  
  2. Rebuild the original 72 758 lines of 68000 assembly in Godot at the Amiga’s 50 Hz rate.  
  3. Combine the modern and original ports so the modern game can launch the 1993 version.  
- All three succeeded; the level format was generated in a single pass without my hints.

## How it was run
- Executed in Claude Code with terminal access, filesystem, and ability to edit files, run the assembler, build, launch, and read output.  
- Added command‑line flags to the rebuilt game for automated testing (level loading, pose setting, scripted input, state probing, screenshot capture).  
- Implemented two headless checks: script compilation and level‑build validation.  
- Used the real Amiga toolchain (vasm, FS‑UAE) for assembly verification; modern port required manual visual screenshot comparison.

## Step one: 34 000 lines of C++ in an evening
- **Timeline (UTC)**  
  - 22:23 – Created Godot 4 project scaffold, synced assets, set up TMX level pipeline.  
  - 22:44 – Both twins playable (collision, physics, camera, switching).  
  - 23:19 – All 38 entity types ported, full object roster live.  
  - 00:35 – Implemented full‑screen flow (menus, map, story, save, game flows).  
  - 02:15 – Exported to macOS, iOS, Android.  
- Result: a playable character in ~21 minutes, using the exact code I had written for the 2010 engine.  
- Refinement took three additional days to adjust jump arcs, trampoline timing, and hit detection, with extensive testing by my 13‑year‑old son, turning the process into a rewarding father‑son activity.

### Same units, same tick
- Game logic uses tile units (1 = 48 px) and runs at a fixed 60 Hz (iOS build).  
- Drag is applied multiplicatively each frame (`velocity.x *= 0.85`). Changing the tick rate alters friction and acceleration curves, so the original 50 Hz and modern 60 Hz versions keep separate hand‑tuned numbers.

### It didn’t use CharacterBody2D
- Instead of Godot’s `CharacterBody2D` and `move_and_slide()`, the port retained the original hand‑written movement code in a plain `Node2D`.  
- The 150‑line collision routine was copied line‑for‑line, preserving the “fudge numbers” and comments I added fifteen years ago.  

## Step two and three (brief)
- **Step two**: The LLM reconstructed the full 68000 assembly source, generated a Godot implementation that runs at the authentic 50 Hz, and verified binaries by assembling with `vasm` and diffing outputs.  
- **Step three**: Integrated the rebuilt 1993 version into the modern Godot project, allowing the player to launch either the contemporary or the original experience from the same executable.  

## Takeaways
- A modern LLM can parse and translate legacy assembly into a high‑level engine with minimal human guidance.  
- Maintaining original tick rates and physics formulas is crucial for preserving gameplay feel.  
- Directly porting hand‑crafted movement code can be preferable to using engine‑provided abstractions when exact behavior matters.  
- The process turned into an unexpected collaborative testing session with my son, highlighting the personal value of revisiting old projects.