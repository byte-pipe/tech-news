---
title: Python 3.15’s JIT is now back on track | Ken Jin’s Blog
url: https://fidget-spinner.github.io/posts/jit-on-track.html
date: 2026-03-17
site: hnrss
model: llama3.2:1b
summarized_at: 2026-03-18T11:42:47.570300
---

# Python 3.15’s JIT is now back on track | Ken Jin’s Blog

## Python 3.15’s JIT Is Back On Track

### Key Points

* The CPython JIT is faster than the standard interpreter on macOS AArch64 and x86_64 Linux by around 20-30% compared to a 100% speedup
* The numbers are preliminary and may not be accurate due to microbenchmarking limitations
* Performance has improved significantly since the original JIT in CPython 3.13-3.14, despite being slower than the interpreter

### Maintained Original Perspective

The new Python 3.15 JIT is back on track after a year of struggles, which were attributed to various factors, including changes in team dynamics and luck.

## The Journey to Success

### Part 1: Community-led JIT

* The earlier CPython JIT project was heavily reliant on internal expertise
* However, community stewardship led by Ken Jin brought about a new approach, prioritizing ease of use and contributor-friendly features
* A community plan set in motion by this effort outlined specific goals for optimization, including improving JIT speedup ratio

### Free-Threading Support and Bus Factor Reduction

* Previous version held only two active contributors across three stages ( frontend, middle-end, backend)
* Current version now has four active maintainers worldwide, with significant progress in addressing issues.
