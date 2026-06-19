---
title: Gribouille 0.3.0: Finer Guide Control and a Themed Compose – Mickaël CANOUIL
url: https://mickael.canouil.fr/posts/2026-06-15-gribouille-0-3/
date: 2026-06-15
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-20T02:41:31.710791
---

# Gribouille 0.3.0: Finer Guide Control and a Themed Compose – Mickaël CANOUIL

# Gribouille 0.3.0 – Finer Guide Control and a Themed Compose – Mickaël CANOUIL  

## Overview  
- Release narrows scope compared with 0.2 but adds several highly‑requested controls.  
- Main headline: **guides()** now hides axis ticks and legends without needing theme tweaks.  
- Additional highlights: `compose()` accepts a `theme:` parameter, `defer()` replaces `plot(..., defer: true)`, `geom‑area()` stacks by default, and `annotate()` can let marks overflow the panel.  

## Guide controls  
- `guides(x: none)` or `guides(y: none)` removes tick marks and tick labels on the specified axis while keeping the axis line, grid, and title.  
- To also drop the axis title, add `labs(x: none)` (or `labs(y: none)`).  
- `guides(none)` hides a specific legend; `guides(auto)` restores the default.  
- `guides(default: none)` sets the fallback for every aesthetic without an explicit guide, effectively removing all legends at once.  
- The new syntax replaces the removed `guide‑none()` function.  

## Radial guide controls  
- The same `guides()` syntax works with `coord‑radial`.  
- `guides(theta: none)` hides the full angular axis (arc, minor ticks, labels).  
- `guides(r: none)` hides only radial tick labels, leaving spokes and circles.  
- `guides(default: none)` also removes legends in radial plots.  

## Themed compose  
- `compose()` now has a `theme:` argument; the supplied theme styles the composition chrome (shared title, hoisted legend, panel tags) and propagates to any panel lacking its own theme.  
- The `defer()` helper replaces the former `plot(..., defer: true)`. Use `defer(plot, …)` instead.  
- Breaking change: panels inside a `compose()` no longer accept individual `width`/`height`; the composition determines cell sizes.  

## Area geometry defaults  
- `geom‑area()` now defaults to `stat: "align"` and `position: "stack"`.  
- `stat: "align"` automatically resamples groups with mismatched x‑values onto a shared grid before stacking, removing the need to specify these arguments manually.  

## Annotation overflow  
- `annotate()` gains a `clip:` argument (default `true`).  
- Setting `clip: false` allows marks to be drawn outside the panel limits, useful for corner insets, external labels, or decorative elements.  
- The change also fixes the previous silent drop of out‑of‑range annotations.  

## Under the hood  
- Most of the release consists of bug fixes rather than new features.  
- Legend layout received major attention; horizontal legends now correctly centre or right‑justify the key graphic when alignment is set to centre or right.