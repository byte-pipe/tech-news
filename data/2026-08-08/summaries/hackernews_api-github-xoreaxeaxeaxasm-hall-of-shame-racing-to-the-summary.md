---
title: GitHub - xoreaxeaxeax/asm-hall-of-shame: Racing to the bottom of CPU performance · GitHub
url: https://github.com/xoreaxeaxeax/asm-hall-of-shame
date: 2026-08-07
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-08-08T11:33:24.679687
---

# GitHub - xoreaxeaxeax/asm-hall-of-shame: Racing to the bottom of CPU performance · GitHub

**Assembly Hall of Shame Summary**

The Assembly Hall of Shame is an analysis that focuses on instruction latency rather than optimization. The main goal is to identify which code executes at a lower fraction of clocks (or "cycles") and quantify this performance using the time it takes to execute the same piece of code on different CPU architectures.

**Methodology Overview**

* Identify the most resource-intensive instructions in assembly code.
* Run each instruction against multiple test cases and measure its execution time on various hardware platforms.
* Extract metrics for instruction frequency, such as the total number of cycles per instruction (CPUs).
* Compare these numbers across different CPUs to find the best-performing code.

**Current Champions**

The top CPU is the AMD Ryzen 7 5800H. Its single-instruction score, 198,002,498,236 cycles, is 62 seconds. This demonstrates a significant speed gap between this CPU and competitors when execution times are normalized for their respective CPUs.
 
Honorable Mentions

Although the presence of an unaligned ymm0 load suggests inefficient use of memory access patterns. Another example that broke fundamental design by utilizing non-posted operations to execute in CPU time.

**Rules**

* Measurements are normalized to the base clock frequency.
* Times include only instructions executed and do not account for interrupts, such as pausing, or virtualization events.
 
The assembly analysis highlights single-instruction execution capabilities across various CPUs, showing optimization strategies that were contrary to traditional performance goals but aimed at more efficient operation under different hardware contexts.