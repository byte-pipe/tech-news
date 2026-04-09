---
title: How uv got so fast | Andrew Nesbitt
url: https://nesbitt.io/2025/12/26/how-uv-got-so-fast.html
date: 2025-12-26
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-28T11:08:10.621268
screenshot: hackernews_api-how-uv-got-so-fast-andrew-nesbitt.png
---

# How uv got so fast | Andrew Nesbitt

## How Uvichecks out faster than Pip by an order of magnitude
The standardization of Python packaging through the adoption of various PEPs has significantly improved execution speed for `uv`.

### Key Points:

* UV's speed is attributed to standards that enable fast paths and optimization decisions.
* The use of Rust at "standard" implementations like pip, while true, barely explains its speed disparities.

### Standards that enabled Uvichecks out faster

1.  **pyproject.toml**: Declares build dependencies without code execution by mimicking Cargo's standard format for Python tools, borrowed from Rust.
2.  **PEP 517 and PEP 621:** Separate build frontends from backends to avoid setuptools internals' complexity.
3.  **PEP 658 (2023) and Uvichecks out**: Direct package metadata fetching through the Simple Repository API without downloading wheels.

### What Makes UV Faster?

*   Elimination of unnecessary code paths: By leveraging these standards, `uv` bypasses redundant computations.

## uv Drops

1.  **No Egg Support:** Although a legacy format, this eliminates the overhead that comes with Python's default egg structure.
2.  **Pip Configuration Files:** Directly ignores pip's configuration, rather than attempting to parse and use them, resulting in faster execution times without performance costs.

### Speedup Comparison

The speed gain from these standards means that `uv` can process code and perform computations significantly faster under proper implementations. This development has led to significant advancements in Uvichecks out performance compared to their predecessors.
