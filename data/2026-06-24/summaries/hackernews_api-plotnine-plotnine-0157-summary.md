---
title: Plotnine – plotnine 0.15.7
url: https://plotnine.org/
date: 2026-06-19
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-24T01:03:59.579964
---

# Plotnine – plotnine 0.15.7

# Plotnine – plotnine 0.15.7

## Overview
- Plotnine is a Python data‑visualisation package built on the grammar of graphics, mirroring the syntax of R’s ggplot2.  
- It supports creating anything from quick exploratory plots to polished, publication‑ready figures.

## Typical workflow (Anscombe’s Quartet example)
- **Single‑line plot**: load the dataset and call `ggplot(... ) + geom_point()` to produce a basic scatter plot.  
- **Sensible defaults**: legends, colour palettes, axis labels, and breaks are added automatically based on the data.  
- **Faceting**: `facet_wrap("dataset")` creates separate panels for each subset without writing loops, making colour encoding unnecessary.  
- **Layering**: add `geom_smooth(method="lm", se=False, fullrange=True)` to overlay linear‑model trend lines on each panel.  
- **Overriding defaults**: customise point colour, fill, size; line colour and thickness; axis breaks; coordinate limits; and add a title with `labs(title="Anscombe’s Quartet")`.  
- **Theming**: apply a theme such as `theme_tufte(base_family="Futura", base_size=16)` and fine‑tune elements (axis lines, ticks, panel spacing) via `theme()` for a personalized or brand‑consistent look.

## Core concepts
- **Grammar of graphics**: visualisations are built from data, aesthetic mappings, and geometric objects combined in layers.  
- **Declarative subsetting**: faceting repeats a plot across multiple panels automatically.  
- **Layer inheritance and overrides**: each layer inherits the base mapping but can modify aesthetics locally.  
- **Full customisation**: any visual attribute (colours, sizes, scales, themes) can be changed to suit the analyst’s needs.

## Getting started
- Install Plotnine (see the Installation section of the documentation).  
- Import with `from plotnine import *` and access example data via `plotnine.data`.  

## Additional information
- Links: view on PyPI, source code, license.  
- Developer: Hassan Kibirige.  
- Funded by: The Open Source Data Science Company.