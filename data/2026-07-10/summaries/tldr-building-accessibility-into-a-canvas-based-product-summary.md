---
title: Building Accessibility Into a Canvas-Based Product | Figma Blog
url: https://www.figma.com/blog/building-accessibility-into-a-canvas-based-product/
date: 2026-07-10
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-10T09:10:09.737192
---

# Building Accessibility Into a Canvas-Based Product | Figma Blog

# Building accessibility into a canvas‑based product

## Overview
- Figma’s canvas renders with a single `<input>` element, giving the browser almost no accessibility tree.  
- To make the editor usable with screen readers and keyboards, the team built a **synthetic “Mirror DOM”** that stays in sync with the canvas’s scenegraph.

## Core components
- **Scenegraph** – the internal data structure of all design nodes that the canvas draws.  
- **Internal accessibility tree** – a cache that stores non‑visual information (role, label, hierarchy) for every layer, allowing incremental updates instead of full rebuilds.  
- **Mirror DOM (React component)** – renders invisible but spatially laid‑out DOM elements based on the internal tree; each component subscribes to a single layer’s summary.  
- **Bidirectional selection sync** – keeps system keyboard focus and canvas selection aligned, so Tab navigation and screen‑reader actions move focus to the correct node.  
- **Announcement system** – pushes live updates (nudges, tool changes, edits) to assistive technologies so users hear changes that sighted users see.

## Building the internal accessibility tree
- Generates an “accessible summary” for each layer (role, aria‑label, children).  
- Context‑aware: prototypes expose only end‑user content, while editing mode includes layout frames and editing controls.  
- Traverses the scenegraph top‑to‑bottom, flattening omitted nodes.  
- Updates surgically as edits occur, avoiding costly full recomputation.

## Mirror DOM details
- Implemented as a recursive React component (`ScreenReaderElement`) that reads the summary via `useAccessibleSummary`.  
- Elements are **not** visually hidden; they are positioned with CSS using each layer’s affine transform (offset, scale, rotation) so spatial information is available to assistive tools (screen magnifiers, voice control, high‑contrast outlines).  
- React’s diffing ensures only minimal DOM changes when the internal tree updates.

## Focus and selection coordination
- Focus denotes the element currently receiving keyboard input; selection denotes the item chosen for an action.  
- In the canvas, Tab changes the selected node without moving system focus, which would appear as a single navigation target to screen readers.  
- Two‑way sync ensures:
  - Clicking a canvas node moves system focus to the corresponding Mirror DOM element.  
  - Screen‑reader navigation updates the visible canvas selection.  
  - VoiceOver rotor and similar controls can select canvas nodes directly.

## Announcing dynamic changes
- Beyond exposing the DOM structure, the system emits live announcements for non‑navigational events (e.g., nudging, tool switches, edit confirmations) so screen‑reader users receive the same contextual feedback as sighted users.