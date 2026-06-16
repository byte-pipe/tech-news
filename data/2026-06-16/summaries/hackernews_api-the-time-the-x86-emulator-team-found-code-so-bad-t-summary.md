---
title: The time the x86 emulator team found code so bad that they fixed it during emulation - The Old New Thing
url: https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419
date: 2026-06-16
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-06-16T12:42:42.425276
---

# The time the x86 emulator team found code so bad that they fixed it during emulation - The Old New Thing

Here is a concise and informative summary of the article:

**Summary**

A colleague of Raymond Chen shared a story about an x86-32 processor emulator, which initially optimized memory management for stack allocation instead of using loops. The team was offended when they discovered this optimization, leading them to add special code to detect such functions and replace them with more efficient, loop-based implementation.

**Main Points**

* An x86-32 processor emulator on Windows included binary translation to emulate 64KB stack memory.
* To allocate 64KB of memory, the standard way was to perform a stack probe and subtract 65536 from the stack pointer.
* However, the compiler optimized this process by unrolling the loop into individual "write byte to memory" instructions, resulting in unnecessary code overhead.

**Key Details**

* The original problem had been solved using binary translation for many years without issue.
* The team added special debugging code to flag and replace such functions with more efficient loop-based implementations.
* This optimization required significantly less code than the original solution, demonstrating the impact of compiler optimizations on performance.

---

## Raymond Chen

Raymond has contributed significantly to Windows evolution, including his well-known "Old New Thing" website.

**Categories**

* History
* Technology
* Software Development