---
title: Python 3.14 Is Here. How Fast Is It? - miguelgrinberg.com
url: https://blog.miguelgrinberg.com/post/python-3-14-is-here-how-fast-is-it
date: 2025-10-09
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-11T11:21:33.043134
screenshot: hackernews_api-python-3-14-is-here-how-fast-is-it-miguelgrinberg.png
---

# Python 3.14 Is Here. How Fast Is It? - miguelgrinberg.com

## Python 3.14: A Leap Forward
### Summary of Key Points and Essential Details

Python 3.14, the latest release in the popular language, brings significant performance boosts over its predecessors. With a focus on improving performance, Pypy has replaced CPython for some benchmarks. This article provides an overview of how Python 3.14 compares to earlier versions, using benchmark tests to demonstrate its capabilities.

## Benchmarks Revisited
Benchmarks were initially shared in 2024, with the author indicating that these results should be viewed as a single data point rather than the definitive performance numbers. The author warns that generic benchmarks may not accurately reflect real-world usage, where various dependencies and implementations often contribute to performance disparities. Despite this caveat, Python 3.14 is considered to offer improved performance over its predecessors.

## Testing Matrix
The article presents a comprehensive testing matrix covering:

* **CPython versions**: Benchmarks comparing Pypy, Node.js, Rust, CPython on different versions.
* **Just-In-Time (JIT):** Compatibility with various environments for code execution.
* **Free-threading (FT)**: Single-threaded and multi-threaded performance comparisons.

Key points highlighted include:

- The test matrix provided spans six Python interpreters across three release cycles.
- The author emphasizes that benchmarks are meant to be representative rather than conclusive indicators of overall performance.
- Pypy's introduction and integration into the CPython codebase aim to enhance compatibility with existing projects.
