---
title: Turning a Gaussian Splat Into a Videogame | PlayCanvas Blog
url: https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/
date: 2026-04-23
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-27T06:03:05.646021
---

# Turning a Gaussian Splat Into a Videogame | PlayCanvas Blog

# Turning a Gaussian Splat Into a Videogame

## Overview
- Gaussian splatting creates photorealistic environments but lacks colliders, navmeshes, and lights, causing characters to float through walls.  
- The demo adds physics, lighting probes, a navmesh, NPCs, and a classic FPS loop, all running in a browser.  
- The scene is an indoor scan by artist Christoph Schindelar, used as the base splat.

## Build Steps

### Step 1 – Download a Splat
- Obtain a `.ply` or `.sog` splat from SuperSplat (Creative Commons licensed).  
- Import the file directly into a PlayCanvas project; no additional art‑direction needed.

### Step 2 – Convert to Streamed SOG
- Use the open‑source CLI `splat-transform` to export the splat as a streamed LOD folder with a manifest.  
- Streaming loads only the chunks near the camera, keeping performance high on both desktop and mobile.  
- A script (`scripts/streaming‑lod.mjs`) forces the required chunks to load before gameplay starts, eliminating pop‑in.

### Step 3 – Generate a Collision Mesh
- Run `splat‑transform` with the `-K` flag to voxelise the splat, flood‑fill from a seed position, and output a watertight `scene.collision.glb`.  
- Import the GLB as an invisible entity with a **Collision** (mesh) component and a static **Rigid Body** component.  
- This provides floor, wall, and bullet collisions without manual modelling.

### Step 4 – Bake a Lightness Grid
- Create a 1 m grid of probe positions above the floor.  
- For each probe, render six 16×16 faces of the splat to a low‑resolution off‑screen target and compute average luminance (Rec. 601 weights).  
- Store results in a JSON file (`lightness.json`, ~40 KB).  
- At runtime, dynamic objects sample this grid to set an `exposure` shader parameter, matching the splat’s baked lighting.

### Step 5 – Develop with the PlayCanvas VS Code Extension
- Write and iterate code (`character‑controller.js`, `npc‑ai.js`, etc.) in VS Code (or Cursor) using the PlayCanvas extension.  
- Saving triggers an automatic reload in the browser, giving a fast edit‑test cycle.

### Step 6 – Version Control with PlayCanvas + GitHub
- PlayCanvas provides built‑in versioning; the VS Code extension also lets you sync the project folder to a GitHub repo.  
- Add a `.pcignore` to exclude the cloud‑only `.git` folder.  
- This setup enables normal git workflows (commit, revert, branch) for a browser‑first engine.

### Step 7 – Generate a Navmesh
- Use the collision mesh as input for `recast‑navigation` to produce a navmesh for NPC pathfinding.  
- The navmesh is loaded at runtime, allowing AI‑controlled characters to navigate the environment correctly.  

## Play the Demo
- Open the published PlayCanvas project in a browser.  
- WASD moves, mouse aims, left‑click fires.  
- All scripts referenced in the article are included and ready to fork or remix.