---
title: Python 3.14 Is Here. How Fast Is It? - miguelgrinberg.com
url: https://blog.miguelgrinberg.com/post/python-3-14-is-here-how-fast-is-it
date: 2025-10-09
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-10T11:19:17.060745
screenshot: hackernews_api-python-3-14-is-here-how-fast-is-it-miguelgrinberg.png
---

# Python 3.14 Is Here. How Fast Is It? - miguelgrinberg.com

## Python 3.14 Performance Benchmark: A Recap of Key Findings
### Introduction

Python 3.14, the latest version of the popular language, may seem impressive after a brief wait. The release dates and official announcements around it highlight significant milestones in its development.

### Quick Word On Benchmarks

Benchmarking Python can be an entertaining pastime; however, they often yield misleading results due to generic tests that do not accurately reflect real-world applications.

### Testing Matrix

The following test matrix outlines the scope of testing:

* **6 Python versions**: CPython3.9, 3.10, 3.11, 3.12, 3.13, and 3.14
* **CPython-specific tests**: Pypy3.11, Node24 (a JavaScript interpreter), Rust1.90
* **Other test scripts**: Two functions for benchmarking Fibonacci numbers (`fibo.py` and `bubble.py`)
* **Threading modes**:
 + Single-threaded (4 threads)
 + Double-threaded (8 threads)

### Summary of Key findings

The tested code in this benchmark aimed to push the limits of performance. The results show that Python 3.14 has made steady progress with improvements, especially against older versions like CPython.

*   A thorough analysis revealed significant advancements across many categories.
*   Even for a moderate number of threads, improved performance is evident.
*   These statistics support claims that CPython 3.14 runs smoother and efficiently than its predecessors.
