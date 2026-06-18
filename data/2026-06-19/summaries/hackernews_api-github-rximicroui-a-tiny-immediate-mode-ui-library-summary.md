---
title: GitHub - rxi/microui: A tiny immediate-mode UI library · GitHub
url: https://github.com/rxi/microui
date: 2026-06-17
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-19T01:18:19.375083
---

# GitHub - rxi/microui: A tiny immediate-mode UI library · GitHub

# microui – tiny immediate‑mode UI library

## Overview
- Tiny, portable immediate‑mode UI library written in ANSI C (≈ 1100 source lines)
- Operates within a fixed‑size memory region; no dynamic memory allocation
- Rendering‑agnostic: only requires the ability to draw rectangles and text
- Designed for easy extension with custom controls and UI elements

## Features
- Built‑in controls: window, scrollable panel, button, slider, textbox, label, checkbox, word‑wrapped text
- Simple layout system for arranging controls
- Works with any rendering backend
- Minimal footprint and no external dependencies

## Example Code
```c
if (mu_begin_window(ctx, "My Window", mu_rect(10,10,140,86))) {
    mu_layout_row(ctx, 2, (int[]){60, -1}, 0);
    mu_label(ctx, "First:");
    if (mu_button(ctx, "Button1")) {
        printf("Button1 pressed\n");
    }
    mu_label(ctx, "Second:");
    if (mu_button(ctx, "Button2")) {
        mu_open_popup(ctx, "My Popup");
    }
    if (mu_begin_popup(ctx, "My Popup")) {
        mu_label(ctx, "Hello world!");
        mu_end_popup(ctx);
    }
    mu_end_window(ctx);
}
```
- Demonstrates typical immediate‑mode workflow: begin window, define layout, add controls, handle popups, end window.

## Usage
- Detailed instructions in `doc/usage.md`
- A complete example is provided in the `demo/` directory
- The library does **not** perform drawing; the user supplies input handling and renders the generated draw commands

## Contribution Guidelines
- The project aims to stay lightweight; adding custom controls is encouraged
- Large feature additions are unlikely to be merged
- Bug reports are welcome; pull requests adding major features may be rejected

## License
- Distributed under the MIT License (see `LICENSE`)

## Repository Statistics
- Stars: 6.3 k
- Forks: 384
- Watchers: 87
- Primary language: C (100 %)

*No official releases have been published.*