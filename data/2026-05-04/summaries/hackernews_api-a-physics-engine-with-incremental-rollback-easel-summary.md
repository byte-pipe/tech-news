---
title: A Physics Engine with Incremental Rollback • Easel
url: https://easel.games/blog/2026-rollback-physics
date: 2026-05-02
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-04T06:01:47.872058
---

# A Physics Engine with Incremental Rollback • Easel

# A Physics Engine with Incremental Rollback • Easel

## Overview
- Easel’s new custom physics engine enables large multiplayer worlds (e.g., a spaceship with thousands of objects) by snapshotting and rolling back only the objects that actually change each frame.  
- Typical frames involve fewer than 30 active objects, yielding a 30‑50× reduction in work compared to full‑world rollback, making expansive games feasible.

## Core Features

### Sleep
- Bodies are put to sleep immediately when their velocity falls within a small epsilon, eliminating the need for snapshotting or physics calculations until they wake.
- Gravity‑induced forces are tracked; a stack remains awake only if any body in it has unbalanced forces, otherwise it settles into equilibrium and sleeps.

### Spatial Indexing
- Uses a Bounding Volume Hierarchy (BVH) for broad‑phase collision detection, performing incremental rebalancing only when necessary.
- BVH stores collider categories, accelerating queries such as “find the nearest player” by filtering out irrelevant colliders.

### Stepping
- Provides a non‑bouncy character step integrated directly into the solver.
- Implemented via `ForcefulStep` with `restitution=0`; stepping is treated like position‑overlap correction, preventing bounce‑back while preserving knock‑back effects.
- Solver workflow:
  1. Solve ejection + stepping and velocity together, storing ejection velocity.  
  2. Remove ejection/stepping constraints, solve again, storing stabilized velocity.  
  3. Perform time‑of‑impact sweep with correct velocities.  
  4. Commit only the stabilized velocity at frame end, eliminating bounce.

### Continuous Collision Detection (CCD)
- Performs sweep‑and‑shape‑cast to catch fast‑moving objects (e.g., fireballs) that could be missed with per‑frame checks.
- Differences from other engines:
  - **Rapier**: integrates position early, possibly using wrong velocities for CCD; Easel delays integration until after impact time is known.
  - **Box2D 2.4**: resolves collisions first then backtracks; Easel stores enough data to integrate after impact time, avoiding early commitment.
  - **Box2D 3.0**: lacks dynamic‑to‑dynamic CCD, causing missed collisions that Easel handles correctly.

## Impact
- By limiting snapshot/rollback to active objects and optimizing sleep, BVH, stepping, and CCD, Easel makes large‑scale, hour‑long multiplayer experiences possible without prohibitive performance costs.