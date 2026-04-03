---
title: "How I built a \"Magic Move\" animation engine for Excalidraw from scratch published - DEV Community"
url: https://dev.to/behruamm/how-i-built-a-magic-move-animation-engine-for-excalidraw-from-scratch-published-4lmp
date: 2026-01-12
site: devto
model: llama3.2:1b
summarized_at: 2026-01-13T11:20:26.094665
screenshot: devto-how-i-built-a-magic-move-animation-engine-for-exca.png
---

# How I built a "Magic Move" animation engine for Excalidraw from scratch published - DEV Community

### Summary

The article discusses the creation of a new animation engine for Excalidraw that enables the visualization of dynamic diagrams. The goal is to create "Keyless Animation" allowing users to sketch logic without creating multiple slides or having to manually animate each element.

**Main Points:**

* Implemented a core logic that identifies and categorizes elements based on their stable IDs and transition types (stable, entering, exiting).
* Used the Next.js framework and Excalidraw for building the engine.
* Developed an `acategorizeTransition` utility function to efficiently map elements between two states.

**Key Features:**

* **Diffing states:** Identifies elements that require movement or animation by marking them as stable (existing in both frames), entering (newly added or updated in frame B), and exiting (older element removed from frame A).
* **Interpolating properties:** Handles properties like numbers, colors, angles, and transforms for different types of objects.
* **Shortest path interpolation:** Enables animation across complex paths for specific object types.

**Technical Details:**

* CategorizeTransition uses a mapping function to efficiently categorize elements between two states.
* Identified stable transitions are stored in `stable`, entering transitions in `entering`, and exiting transitions in `exiting`.
* Calculates intermediate state for morphed elements using linear or shortest path interpolation depending on the object type.

### Summary Output

**Keyless Animation Engine:**

* Sketches logic with minimal user intervention
* Enables "Keyless" animation without manually animating each element
* Includes automatic identification and categorization of elements based on IDs and transition types
* Utilizes Next.js for building the engine
* Developed `acategorizeTransition` utility function for efficient mapping between states

Note: I've maintained the original formatting, style, and context of the provided text.
