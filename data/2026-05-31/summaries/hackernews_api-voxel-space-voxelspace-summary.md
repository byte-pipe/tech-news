---
title: Voxel Space | VoxelSpace
url: https://s-macke.github.io/VoxelSpace/
date: 2026-05-31
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-31T06:01:33.954023
---

# Voxel Space | VoxelSpace

# VoxelSpace Summary

## History
- In 1992 CPUs were far slower and GPUs were not common; 3‑D games were rendered on the CPU with flat‑colored polygons.
- NovaLogic released *Comanche* (1992) using the Voxel Space engine, delivering detailed terrain textures, shading, and shadows—remarkable for its time.

## Render algorithm
- Voxel Space is a 2.5‑D technique similar to ray casting; it lacks full 3‑D freedom but is efficient for terrain rendering.

### Height map and color map
- Terrain is stored as a 1024 × 1024 one‑byte height map and a matching 1024 × 1024 one‑byte color map (periodic).
- Each map position holds a single height, so complex objects like buildings or trees cannot be represented.
- The color map already contains shading and shadows, so illumination does not need to be computed during rendering.

### Basic algorithm
- Render vertical columns by scanning the height and color maps from back to front (painter’s algorithm).
- Steps:
  1. Clear the screen.
  2. For each distance `z` from farthest to nearest:
     - Compute the map line that corresponds to the current depth, considering a 90° field of view.
     - Segment the line to match the screen width.
     - For each screen column:
       - Retrieve height and color from the maps.
       - Apply perspective scaling to the height.
       - Draw a vertical line with the retrieved color and scaled height.
- A minimal Python‑style implementation is provided in the article.

### Add rotation
- To view directions other than north, rotate the map coordinates using pre‑computed `sin(phi)` and `cos(phi)`.
- The rotated version updates both `x` and `y` increments while keeping the same column‑drawing logic.

## More performance
- **Front‑to‑back rendering**: Draw nearer columns first and use a y‑buffer to skip drawing hidden parts, reducing overdraw.
- **Level of Detail (LOD)**: Render finer detail up close and coarser detail at greater distances; step size (`dz`) increases with depth.
- Example code shows initialization of a `ybuffer`, front‑to‑back loop, and adaptive `dz` increment.

## Links
- The page provides a web demo and downloadable height/color maps for experimentation.