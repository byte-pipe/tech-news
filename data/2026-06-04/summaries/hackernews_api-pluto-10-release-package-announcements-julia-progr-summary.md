---
title: Pluto 1.0 release! - Package Announcements - Julia Programming Language
url: https://discourse.julialang.org/t/pluto-1-0-release/137296
date: 2026-06-03
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-04T06:56:25.640293
---

# Pluto 1.0 release! - Package Announcements - Julia Programming Language

# Pluto 1.0 release!

## Wait… what is Pluto?
- An interactive notebook environment for Julia aimed at scientific computing, teaching, and literate programming.  
- Key qualities:  
  - **Interactive** – cells are reactive like a spreadsheet and support buttons, sliders, etc.  
  - **Reproducible** – package management and execution order ensure notebooks run unchanged for others.  
  - **Accessible** – designed for beginners, with keyboard‑only, mouse‑only and touch‑only support.  
- Popularity: #1 starred Julia package on GitHub since 2021; used worldwide in online courses.  
- Installation: free, open‑source; run `import Pluto; Pluto.run()` in Julia.

## What’s new in Pluto?

### (1/10) Reproducibility & reliability
- Very stable; large courses (100+ students) install and run notebooks without issues.  
- ~2 500 automatic test cases, including UI tests with browsers.  
- Automatic per‑notebook package environment; packages added/removed as needed.  
- New tools: **GracefulPkg.jl** for mixed Julia versions, a **Project.toml editor**, and support for `Julia[sources]` to fetch GitHub packages reproducibly.

### (2/10) Sharing your work
- Export options: Julia code, PDF, and self‑contained HTML (includes source and environment, works offline since 2025).  
- Website generation: `static-export-template` creates sites from notebook repositories; **PlutoSliderServer.jl** serves instantly interactive Pluto‑based sites.  
- New service **pluto.land** lets users share HTML exports like a pastebin for Pluto notebooks.

### (3/10) Reactivity
- Cells react instantly to changes; new controls help manage long‑running computations.  
- **Disable cells** – prevents execution of a cell and any dependent cells, with reactive propagation.  
- **Confirmation before long runtimes** – prompts the user when a reactive chain may take significant time, allowing cancellation or adjustments.

### (4/10) Interactivity
- Expanded widget library in **PlutoUI.jl**: sliders, switches, buttons, dropdowns, multiselects, text fields, click‑for‑more, reading‑time calculator, wide cells, side‑margin cells, 2D layout tools, and widget composition.  
- **PlutoTeachingTools.jl** (co‑developed with educators) provides ready‑made interactive lecture and live‑homework components.  
- **Widgets API** – exposes JavaScript runtime, high‑performance Julia‑JS connection, and display system, enabling custom widget creation without adding a Pluto dependency.

### (5/10) Accessibility and localization
- Enhanced support for keyboard‑only, mouse‑only, touch‑only, visual accessibility, and screen readers.  
- Interface now available in 16 languages, including Chinese, Danish, German, Greek, English, Latin American Spanish, and others.

### (6/10) Education
- Continued focus on teaching tools and curriculum integration, building on the environment originally created for MIT’s Computational Thinking course.

### (7/10) AI tools
- Upcoming integrations that leverage AI to assist coding, suggest visualizations, and automate notebook generation.

### (8/10) Documentation
- Updated and expanded documentation, with clearer examples and tutorials for new and experienced users.

### (9/10) Editor tools
- Improvements to the notebook editor, including better error handling, UI refinements, and performance optimizations.

### (10/10) Ecosystem
- Growth of the Pluto ecosystem: more packages, community contributions, and third‑party tools that extend Pluto’s capabilities.

## Thank you!
- After six years of development, the author celebrates the release of Pluto 1.0, expresses pride in the community’s achievements, and invites users to enjoy the new, stable, and feature‑rich version.