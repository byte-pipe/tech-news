---
title: How to speed up the Rust compiler in September 2026 | Nicholas Nethercote
url: https://nnethercote.github.io/2026/09/30/how-to-speed-up-the-rust-compiler-in-september-2026.html
date: 2026-10-01
site: hnrss
model: llama3.2:1b
summarized_at: 2026-10-01T17:31:26.029545
---

# How to speed up the Rust compiler in September 2026 | Nicholas Nethercote

## Rust Compiler Performance

### Overall Progress

* Mean wall-time reduction: 4.57%
* Number of benchmark measurements: 629
* Number of improvements: 555
* Number of regressions: 74
* "Sea of Green" result: improvements in most benchmarks

### Notable Developments

* **rustdoc**: Significant speedup on Rustdoc benchmarks, with a gain of 18% on average.
* **Clippy**: Improved performance on various Clippy benchmarks, with a gain of 18% on average.
* **LLVM**: Upgrade to LLVM 23, resulting in a 1.2% mean wall-time reduction across all benchmarks.
* **Borrow Checker**: Improved precision and acceptability of programs with new borrow checker version (PoloniusAlpha).
* **Trait Solver**: Improved performance on certain traits-related tests, with some reductions of 1-3%.

### Summary

The Rust compiler has seen significant improvements in performance over the past two months. The "sea of green" result indicates that a large number of benchmarks have improved, with most regressions swamped by recent improvements. Notable developments include significant speedups on Rustdoc, Clippy, LLVM, and the borrow checker, as well as improvements in trait solver performance.