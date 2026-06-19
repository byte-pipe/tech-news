---
title: To study how chips really work, MIT researchers built their own operating system | MIT News | Massachusetts Institute of Technology
url: https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610
date: 2026-06-16
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-20T02:40:54.856162
---

# To study how chips really work, MIT researchers built their own operating system | MIT News | Massachusetts Institute of Technology

# To study how chips really work, MIT researchers built their own operating system

## Overview
- MIT CSAIL introduced **Fractal**, a new operating‑system kernel designed to give researchers a clean, low‑noise view of processor internals.  
- The kernel acts as an “electron microscope” for microarchitectural studies and has already uncovered previously unknown behavior in Apple’s M1 chip.

## Problem with Existing Approaches
- Modern CPUs contain many internal structures (branch predictors, caches, TLBs) that are hard to observe because general‑purpose OSes (macOS, Linux) add scheduling, interrupts, and privilege management noise.  
- Researchers must patch kernels manually, leading to unstable and hard‑to‑reproduce experiments, especially on Apple platforms where such modifications are being deprecated.

## Fractal Design and Key Innovations
- **Bare‑metal boot**: Fractal runs directly on hardware with no other software, eliminating background activity.  
- **Multi‑privilege concurrency**: Allows the same code to switch between user and kernel privileges while staying in the same address space.  
- **Outer kernel thread**: A new construct that lives in a user process’s memory but executes with kernel privileges, providing precise control over privilege boundaries.  
- Supports x86_64, ARM64, and RISC‑V; includes POSIX system calls, a C library, and ports of tools such as vim, GCC, and dash to ease migration of existing experiments.  
- Codebase of ~31,000 lines, intended as reusable research infrastructure rather than a single experiment.

## Findings on Apple’s M1 Processor
- **CSV2 protection** works for the execute stage of indirect branch prediction, preventing user‑mode code from forcing kernel speculative execution of chosen targets.  
- The CPU still **fetches** the target into the instruction cache before protection activates, creating a side‑channel observable across privilege boundaries.  
- First evidence that **Phantom speculation** occurs on Apple Silicon, allowing ordinary instructions (including no‑ops) to be mis‑interpreted as branches, with speculative fetches crossing privilege levels.  
- Refuted earlier macOS‑based results: the conditional branch predictor on both performance and efficiency cores shows **no privilege isolation**, and prior observations were likely artifacts of macOS thread migration.  
- Demonstrated that with Fractal, the only variable affecting attack success is the privilege level, providing a true independent variable for experiments.

## Community Impact and Future Plans
- MIT disclosed the M1 findings to Apple; Apple’s engineers also examined Fractal, indicating mutual interest.  
- Goal: make Fractal a shared infrastructure akin to QEMU or FFmpeg for microarchitectural research, improving reliability and accuracy of results across the community.  
- External endorsement: USC assistant professor Mengyuan Li highlighted Fractal’s reduction of software noise and tighter control across privilege boundaries as a major advance for hardware experimentation.  
- Ongoing support from MIT, the National … (funding details truncated).