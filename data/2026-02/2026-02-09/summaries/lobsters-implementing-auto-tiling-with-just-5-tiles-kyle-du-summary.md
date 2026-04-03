---
title: Implementing Auto Tiling With Just 5 Tiles - Kyle Dunbar’s Blog
url: https://kyledunbar.dev/2026/02/05/Implementing-auto-tiling-with-just-5-tiles.html
date: 2026-02-09
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-09T06:06:33.762354
---

# Implementing Auto Tiling With Just 5 Tiles - Kyle Dunbar’s Blog

# Implementing Auto Tiling With Just 5 Tiles - Kyle Dunbar’s Blog

This blog post details an implementation of an auto-tiling system using only 5 tiles, inspired by Nonsensical 2D's video. The core concept involves separating the tilemap into two layers: one for physical collisions and another for visual representation. By offsetting the visual layer, the visuals can be painted by their corners, requiring only 5 tiles (a corner, a side, opposing corners, an inward corner, and a full/middle piece).

## How it works

The system utilizes a 4-bit mask to represent the four neighboring tiles of a physical tile. Each permutation of this mask corresponds to a specific visual placement. The visual tiles are then placed based on the physical tile's neighbors, using the opposing corner representation. The 5 tiles can be rotated and flipped to generate the 16 different tile pieces.

## Godot Tooling

The implementation uses dual tilemap layers in Godot: one for physical tiles and one for visuals. A script attached to the physical tiles layer handles the auto-tiling logic.  A level management node and a separate script are used for saving and loading the level data.

## Saving

The level data is serialized into a dictionary containing "physical" and "visual" tilemaps. Each tilemap's cells are iterated, and data including position, source ID, atlas coordinates, and alternative ID (for rotation instructions) are stored in a dictionary. This data is then saved to `user://` to avoid read-only restrictions during runtime.

## Importing with EditorPlugin

An EditorPlugin is included to facilitate loading the saved level data back into the editor. This plugin adds an import button to the WorldMap inspector. When clicked, it reads the level data from `user://`, creates a new WorldMap node, applies the data, overwrites the existing scene in `res://`, and refreshes the editor's file system. This provides a convenient workflow for developers.

## Key Points

- **5-Tile System:** Achieves 16 tile variations using only 5 base tiles through rotation and flipping.
- **Dual Tilemaps:** Separates physical and visual tile data for flexible placement.
- **Bitmask Representation:** Uses a 4-bit mask to represent neighboring tile configurations.
- **Serialization and Deserialization:**  Serializes tilemap data to a dictionary for saving and deserializes it for loading.
- **EditorPlugin:** Provides an in-editor import functionality for seamless level loading.
- **Godot Specifics:**  The implementation is tailored for Godot, utilizing its scene management and file system structure.
