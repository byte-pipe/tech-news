---
title: We ported the original Doom to SQL | CedarDB
url: https://cedardb.com/blog/sqldoom/
date: 2026-10-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-07T06:01:27.348344
---

# We ported the original Doom to SQL | CedarDB

# Summary of “We ported the original Doom to SQL | CedarDB”

## TL;DR
- The original 1993 Doom’s game logic and renderer have been fully implemented in SQL and run inside a database.
- The game loop runs at the authentic 35 Hz tick rate, while the renderer can produce a 320×200 frame buffer at up to 60 Hz on a laptop.
- Python is only used for timing, keyboard input, and displaying the bitmap returned by the database; multiplayer works as well.

## Gameplay Availability
- Playable now in deathmatch mode with four slots (first‑come‑first‑served) on EU and US servers.
- If all slots are taken, users join a queue; while waiting they can query live game state via SQL.

## Background & Motivation
- A previous project, **DOOMQL**, rendered ASCII‑art approximations of Doom at ~30 FPS but used raycasting, resembling Wolfenstein 3D.
- Doom’s true rendering relies on BSP trees for proper depth ordering, textures, arbitrary wall angles, and varying floor heights.
- The author revisited the challenge during parental leave and created **SQLDoom**, a faithful Doom implementation that runs entirely in SQL.

## Design Rules
1. Visual output must match the real Doom (far beyond DOOMQL’s fidelity).  
2. Gameplay feel must match the original Doom’s “raw fun.”  
3. Rendering must be pure SQL, outputting a table or bitmap with exact RGB values per pixel.  
4. The game loop must also be pure SQL; user‑defined functions inside the DB are allowed.  
5. A client in another language may handle input parsing, tick driving, and bitmap display only.

## Architecture Overview
- **Python client** (using pygame) handles:
  - Keyboard input
  - Timing (35 Hz tick generation)
  - Displaying the bitmap returned from the DB
- **SQL side** contains:
  - Game‑state tables (players, monsters, map geometry, etc.)
  - Game‑logic procedures (tick processing, AI, physics)
  - Renderer procedure (pure function converting state tables to an RGB bitmap)
- The logic runs at a fixed 35 Hz; rendering is decoupled and can be requested as often as the client desires.

```
Python (input/timing/display)
   ↕ run tic / request frame
SQL game logic   ↔   SQL renderer
   ↕
Game‑state tables
```

## Loading Doom Data
- Doom’s `.wad` format maps naturally to relational tables (VERTEXES, LINEDEFS, SIDEDEFS, SECTORS, THINGS, etc.).
- Importing the full Doom 1 data takes ~18 seconds on a laptop and required ~1 000 lines of Python.
- Example query renders a bird’s‑eye ASCII map of level E1M1 by walking each line segment in 32 steps and aggregating characters.

## Game Loop Details
- Original Doom used a fixed 35 Hz clock, giving each tick ~28.6 ms to process logic and draw one frame.
- SQLDoom preserves the 35 Hz tick rate for game logic, keeping all original constants valid.
- Rendering is independent: the client can request frames at any rate, interpolating the camera between ticks for smoother motion.
- Two performance budgets:
  1. Execute a tick every 28.6 ms (otherwise gameplay feels wrong).
  2. Render ≥ 35 FPS for smooth visual experience (lower rates are acceptable but less fluid).

### Tick Sequence (CedarScript)
- A scripted procedure (`doom_cs_clock`) determines a bitmask of actions to perform each tick.
- Conditional calls handle:
  - Special activations (e.g., doors, lifts)
  - Door movement
  - Player movement and turning
  - Death processing
  - Secret handling, pickups, weapon state, hitscan damage
  - Sound playback
  - Monster AI and actions
- The script re‑plans after world changes to keep the tick logic coherent.

## Key Takeaways
- Doom’s full game logic and rendering can be expressed in SQL, proving that complex, real‑time applications are possible within a relational database.
- Decoupling logic (fixed‑rate ticks) from rendering (client‑driven frames) allows the system to meet both timing constraints.
- The project demonstrates a novel use of CedarDB’s scripting language (CedarScript) and showcases the relational nature of Doom’s map data.