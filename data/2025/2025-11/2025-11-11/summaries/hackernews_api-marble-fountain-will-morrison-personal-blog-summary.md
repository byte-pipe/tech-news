---
title: Marble Fountain :: Will Morrison — Personal Blog
url: https://willmorrison.net/posts/marble-fountain/
date: 2025-11-09
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-11T11:08:45.502094
screenshot: hackernews_api-marble-fountain-will-morrison-personal-blog.png
---

# Marble Fountain :: Will Morrison — Personal Blog

# Marble Fountain

**Project Overview**

This is a procedural generation project for printing an art piece using the Formlabs 3D printer. The system, called "Marble Fountain," uses random placement of points to create a complex structure, with a focus on maximizing motion within the volume of the printer.

**Tracks**

The initial track generator placed points at spaced intervals and drew a spline through them. However, this solution was limited as it produced a tube structure that was too straightforward and lacked sufficient complexity. The path solver was developed next to fit more parts into the volume, requiring a highly optimized solution that addressed issues such as:

* Choosing effective starting conditions on the track for better performance
* Modeling points within specified boundaries while maintaining even spacing and avoiding obstacles

**Path Solver Algorithm Variants**

Several algorithms were used to generate the track paths, each with noticeable impacts on the final shape of the structure. These included different initial conditional values that influenced the structure's overall appearance.

## Supports Generation**

The support generation algorithm was relatively simple, as it only required iterating from the top down and treating the supports' positions relative to the bottom of the printer. This solution proved effective in producing a functional build.

**Physical Properties**

1. **Velocity**: The marble motion involves managing velocity across various parts of the structure.
2. **Tracking System**: Ball movement through curved tracks creates complex motion patterns, requiring careful balance between speed and friction effects.
3. **Screw Mechanism**: Using balls suspended within a screw mechanism generates an unstable track that breaks down due to constant acceleration and torque.

**Key Insights**

1.  The system's performance relies on effective tracking algorithms with realistic constraints, particularly the use of turn radii and velocity management.
2.  Effective geometry development requires striking balance between maintaining accurate bounds and accommodating natural movements under physics.
3.  Systemic efficiency lies in minimizing track length and energy usage while maintaining sufficient flexibility to handle the inherent behaviors associated with real-world systems.
