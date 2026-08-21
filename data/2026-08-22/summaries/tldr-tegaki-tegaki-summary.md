---
title: Tegaki | Tegaki
url: https://gkurt.com/tegaki/
date: 2026-08-22
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-22T06:00:39.212216
---

# Tegaki | Tegaki

# Tegaki Summary

## Overview
- Tegaki creates animated handwriting from any font.
- Provides tools for generating stroke data, bundling it, and rendering animations in various front‑end frameworks.

## Key Features
- **Generate**: CLI downloads Google Fonts, extracts glyph outlines, builds skeletons, and traces stroke paths with width and timing data.  
- **Bundle**: Packages stroke data with glyph metrics and timing information into a compact bundle.  
- **Render**: Ready‑to‑use components for React, Svelte, Vue, SolidJS, Astro, Web Components, or vanilla JS handle text layout, line wrapping, and smooth playback.  
- **Stream**: Supports animating handwriting for text streams from APIs, ideal for AI chat interfaces.

## Typical Workflow
- Use the generator CLI to create stroke data from a chosen font.  
- Bundle the data for efficient loading.  
- Drop the appropriate rendering component into the application.  
- Optionally stream animated text from an API for dynamic content.