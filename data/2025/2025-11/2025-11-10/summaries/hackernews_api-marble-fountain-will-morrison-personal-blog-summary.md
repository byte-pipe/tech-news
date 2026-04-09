---
title: Marble Fountain :: Will Morrison — Personal Blog
url: https://willmorrison.net/posts/marble-fountain/
date: 2025-11-09
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-10T11:08:20.655905
screenshot: hackernews_api-marble-fountain-will-morrison-personal-blog.png
---

# Marble Fountain :: Will Morrison — Personal Blog

Here is a concise and informative summary of the text passage:

# Marble Fountain: A Procedural Art Piece Generator

**System Overview**

The author has created a procedural art piece generator called Marble Fountain, which utilizes algorithms to generate complex designs for 3D printing. Initially, a basic system was developed with randomly placed points and a spline drawing algorithm that limited its flexibility.

**Advanced Features**

To address this limitation, the solver is used to fit as much motion into the volume of the printer as possible. This involves creating a series of line segments connecting the top and bottom of the lift and generating alternative starting conditions for better results. Functions update positions over time to create followable paths.

**Tracking Mechanics**

* Points in each path stay within a bounding box
* Spacing is even among points
* The track follows a constant height (spline)
* Min and max turning radius limits determine path variations
* Repelling from other tracks and distant areas prevents tracking issues

**Velocity Control**

To handle velocity, the author sets a minimum turn radius for each section of the track while banking much more aggressively to prevent bearing off bearings. This design solution helps ensure smooth rotation and prevents speed buildup.

**Support Generation**

The support generation is relatively simple, as it involves iterating from top to bottom in 3D space and treating the supports as static elements that do not affect tracking mechanics.
