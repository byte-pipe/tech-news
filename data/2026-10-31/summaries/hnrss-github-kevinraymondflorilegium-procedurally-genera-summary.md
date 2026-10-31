---
title: GitHub - kevinraymond/florilegium: Procedurally generated Delft-blue floral page margins for LuaLaTeX, drawn in Lua · GitHub
url: https://github.com/kevinraymond/florilegium
date: 2026-10-30
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-10-31T19:04:05.774374
---

# GitHub - kevinraymond/florilegium: Procedurally generated Delft-blue floral page margins for LuaLaTeX, drawn in Lua · GitHub

# Summary of florilegium repository

## Overview
- Provides procedurally generated Delft‑blue floral page margins for LuaLaTeX.
- All graphics are created on‑the‑fly in Lua; no external images or assets are needed.
- Each page receives a unique garden that fills the free space left by the main text.

## Main documents
- **florilegium.tex** – hand‑authored composition where stems, leaves and flowers are placed manually.
- **florilegium‑grow.tex** – automatically grown garden that adapts to the page layout using a greedy space‑filling algorithm.
- Additional showcase files (showcase.tex, spread.tex) demonstrate extra features such as initials, seasonal changes, and visitor elements.

## Growth algorithm
- Starts with a seed that defines random parameters for primitives (petals, leaves, stems).
- Stems grow first; leaves open as nodes are passed; each stem ends in a flower.
- A greedy loop repeatedly finds the largest free disc in the remaining margin and grows a branch toward it, filling big holes early and small holes later.
- The growth sequence is recorded once while the page is laid out; the recorded frames can be rendered as animated GIF/MP4.

## Interactive features
- **Initials** – `\florilegiuminitial[5]{E}` draws a decorative initial using the outline of an OpenType glyph, with vines, leaves and flowers woven around it.
- **Section flowers** – `optionsections` adds a copper‑colored flower beside each numbered heading.
- **On‑demand bloom** – `\florilegiumbloom` places a flower at the line where the command appears; any motif can be requested.
- **Aging/seasonal change** – `optionaging` ages the garden from spring to autumn across the document; `\florilegiumage{0.8}` sets a specific age manually.
- **Visitors** – random butterflies, bees, snails and occasional birds appear in free spaces; can be disabled with `optionnovisitors`.

## Ink palette
- All colors are derived from a single hue (Delft blue, sepia, green, crimson, violet, teal).
- Shades are generated in OKLCH space, ensuring the lightest washes never become gray.

## Themes
- **Default theme** – organic shapes with watercolor washes.
- **geometric theme** (`theme=geometric`) – flat geometric primitives (kites, rhombi, star polygons) with solid tones; low‑poly birds and butterflies; crystals appear among flowers.
- **math theme** (`theme=math`) – replaces plants with mathematical figures (Apollonian gasket, Koch snowflake, Vogel’s disc, polyhedra, knots, Hilbert curves) and equations; figures are placed by size, largest first.

## Repository contents (selected)
- Lua source files: `florilegium.lua`, `grow.lua`, `theme-geometric.lua`, `theme-math.lua`, plus primitives (`flora.lua`, `ink.lua`, etc.).
- LaTeX package and example documents: `florilegium.sty`, `florilegium.tex`, `florilegium-grow.tex`, `showcase.tex`, `spread.tex`.
- Generated PDFs showing the margins, animations, and specimens.
- Supporting files: `README.md`, `LICENSE`, CI workflow, gallery of rendered pages.