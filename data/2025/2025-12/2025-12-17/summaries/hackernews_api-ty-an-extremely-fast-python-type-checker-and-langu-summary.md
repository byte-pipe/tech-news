---
title: ty: An extremely fast Python type checker and language server
url: https://astral.sh/blog/ty
date: 2025-12-16
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-17T11:20:07.210741
screenshot: hackernews_api-ty-an-extremely-fast-python-type-checker-and-langu.png
---

# ty: An extremely fast Python type checker and language server

**ty: A Fast Python Type Checker and Language Server**

**Introduction**
===============

The article introduces **ty**, an extremely fast Python type checker and language server written in Rust. It is designed to be an alternative to existing tools like mypy, Pyright, and Pylance.

**Key Features and Advantages**
=====================================

*   **Extreme Performance**: `ty` consists of "incremental" calculations, allowing for live updates in editors or long-lived processes.
*   **High Speed**: With caching disabled, `ty` is up to 10x and 60x faster than top-of-the-line Python type checkers.
*   **Correctness**: Features like first-class intersection types, advanced narrowing, and sophisticated reachability analysis ensure accurate feedback over assumptions about user intent.

**Implementation and Integrations**
=============================

*   **Built-in Rust**: `ty` is written in Rust, which enables performance and facilitates developer contributions under the MIT license.
*   **Open-source Development**: The core team built `ty` alongside hundreds of active contributors, allowing it to be run anywhere with valid Python code.

**Comparison to Other Tools**
=============================

| Tool              | Performance        | Accuracy      | Memory Usage |
|-------------------|--------------------|---------------|--------------|
| mypy            | Up to 8x faster     | Good          | Low         |
| Pyright        | Similar performance| Good          | Low         |
| Pylance         | Up to 5x faster    | Excellent     | High       |

**Example Usage**
===============

*   Install `ty` by running `uv tool install ty@latest`, or via the VS Code extension.
*   Edit a central file in your Python project and enable `ty` with `uv`.
*   Observe impressive speed gains using tools like Pyright and Pylance.

**Conclusion**
==========

The article concludes that **ty** is an exciting addition to the Python ecosystem, providing a high-performance type checker and language server. Its commitment to innovation and developer experience aligns it well with Astral's goals in building reliable tools for Python and other languages.
