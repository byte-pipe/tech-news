---
title: Declarative Dragging
url: https://declarative-dragging.github.io/
date: 2026-11-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-09T16:01:11.839755
---

# Declarative Dragging

# Declarative Dragging

## Overview
- Drag‑and‑drop is powerful but often requires extensive code for geometry, feedback, and animation, discouraging many creators.  
- Declarative dragging flips the problem: developers specify the *future states* an element can reach by being dragged.  
- The system speculatively renders those states, extracts positions, and synthesizes a smooth drag interaction automatically.  
- Goal: let authors stay in their semantic model while the system turns model rules into tactile UI behavior.

## How it works
- **Model‑driven**: an author marks an element as draggable and lists accessible future model states.  
- An engine renders each state to a view tree, records the element’s position, and combines the results into a responsive drag‑and‑drop interaction.  
- **Dragology** is the library that implements this approach for SVG web interfaces.  
- The system is **composable**: simple drag behaviors can be combined, and modifiers (floating, snapping, transitions) can be layered to increase expressiveness.

## Dragology demos
- A gallery showcases interactive examples built with Dragology, including:
  - Algebra visualizations  
  - Twisted trees  
  - Bézier curve manipulation  
  - Braid structures  
  - Card piles  
  - Face morphing  
  - Trominoes  
  - Sprouting tree animations  

## Origin
- In 2022 Andrew prototyped a math‑tangibility game but felt the menu‑based transformations lacked tactile feel.  
- He sketched a primitive model‑driven dragging concept, which remained idle for two years.  
- In 2023, after discussing the idea with Josh during a Seattle walk, the concept resurfaced.  
- Josh’s work on order‑preserving tree maps needed a way to “pull” structures, leading him to build a library that evolved, with Andrew’s help, into declarative dragging.

## Since the paper
- **Josh**: uses Dragology for complex mathematical explorables, especially those showing parallel representations that update together in real time (e.g., permutation lab).  
- **Andrew**: integrates declarative dragging into existing tools, such as the Hazel programming environment where refactorings become tangible, and adapts the technique for a 3D math game using gamepad input.

## Citation
```
@inproceedings{horowitz2026declarative,
  title = {Declarative Dragging},
  author = {Horowitz, Joshua and Blinn, Andrew and Heer, Jeffrey},
  booktitle = {Proceedings of the 39th Annual ACM Symposium on User Interface Software and Technology (UIST '26)},
  year = {2026}
}
```