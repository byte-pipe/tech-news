---
title: Building a new Flash - by Bill
url: https://bill.newgrounds.com/news/post/1607118
date: 2026-03-05
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-06T06:01:19.424887
---

# Building a new Flash - by Bill

# Building a new Flash – Summary

## Project Overview
- Developing a modern, cross‑platform 2D animation authoring tool (Linux, macOS, PC) using C#, Avalonia, and SkiaSharp.
- Intended as a full‑featured replacement for Adobe Flash, not a prototype.
- Open‑source with Patreon support; updates posted on Newgrounds.
- Key capabilities include vector drawing, timeline editing, shape tweening, symbol library, .fla/XFL import, C#‑based scripting, and a built‑in sound editor.

## Core Features
- Multi‑document tabs with dockable/floating windows.
- Automatic periodic saves.
- Project serialization to folder‑based or compressed `.anim` files (JSON + SkiaSharp).
- Support for multiple scenes per document.
- Customizable stage size, background color, and frame rate.

## Drawing Tools (selected)
- **Selection & Subselection** – move, transform, edit bezier points.
- **Brush / Pencil / Line / Rectangle / Circle / Arc** – pressure‑sensitive freehand and precise shape creation, all with five paint modes (Normal, Behind, Fills, Selection, Inside).
- **Eraser, Paint Bucket, Eyedropper** – content removal and color sampling.
- **Text & Rich Text** – live preview and per‑character gradient/pattern fills.
- **Hand & Zoom** – canvas navigation.
- **Lasso & Camera** – free‑form selection and per‑frame virtual camera control.

## Object Types
- Vector Shape objects with fill/stroke properties.
- Text and Rich Text objects (glyph outlines).
- Bitmap objects (imported raster images).
- Symbol instances (reusable library assets).

## Symbol System
- Graphic, MovieClip, Button, and RichText symbols with independent timelines or synced playback.
- Central Symbol Library for asset management.
- Dialog to convert selected objects into new symbols.

## Timeline & Animation
- Multi‑layer timeline with visibility, locking, and layer types (Normal, Guide, Mask, Folder, Camera, Sound).
- Keyframes, classic tween, motion tween (path‑based), shape tween (contour correspondence).
- Easing functions (linear, quad, cubic, etc.) and custom cubic‑bezier curves.
- Frame‑by‑frame labeling, motion path editing, camera animation, and sound layer synchronization.

## Styling
- Fill styles: solid, linear/radial gradients, patterns.
- Stroke styles: width, color, caps, joins, miter limit.
- Per‑object alpha transparency and HSV color picker.

## Filters & Effects
- Blur (separate X/Y), Drop Shadow, Glow, Bevel.
- Color adjustments (hue, saturation, brightness, contrast).
- Ability to chain multiple filters per object.

## Selection & Transformation
- Marquee and lasso selections with additive/subtractive modes.
- Individual and group transform (move, scale, rotate, skew).
- Path bending, endpoint snapping, and batch command grouping.

## Alignment & Distribution
- Align objects (left, center, right, top, middle, bottom).
- Distribute spacing horizontally or vertically.
- Alignment reference options (stage or current selection).

## Undo/Redo
- Full history with up to 100 steps.
- Mergeable and batch commands to consolidate related actions into single undo entries.
