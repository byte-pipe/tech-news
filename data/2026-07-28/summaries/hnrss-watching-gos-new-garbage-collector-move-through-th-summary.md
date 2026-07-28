---
title: "Watching Go's new garbage collector move through the heap - The Consensus"
url: https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html
date: 2026-07-25
site: hnrss
model: llama3.2:1b
summarized_at: 2026-07-28T11:50:27.202556
---

# Watching Go's new garbage collector move through the heap - The Consensus

# Watching Go's new garbage collector move through the heap
Go 1.26 made Green Tea the default GC, with perf optimization and a more detailed heap dump.

## Key Points:

* **Introduction to Green Tea**: A non-moving garbage collector introduced in Go 1.25, which struggles when dealing with sparse-page problems.
* **Cache-friendliness of perf**: Measures the performance of Go's garbage collection using `perf`.
* **Heap visualization**: Displays the heap structure and allocates objects of different sizes (small, medium, large).
* **Sparse-page problem**: A non-moving collector like Green Tea cannot reclaim sparse pages.

## Structs for Allocating Objects

In Go, memory allocation is done by allocating objects with the same size class (an object's size rounded up to the nearest size class) within contiguous chunks of 8KB pages.

## Objective-C Comparison

The objective-c code snippet provides a comparison between Go's `alloc` and `malloc` functions, using three different sizes: small, medium, and large. It then checks the heap address, walks the address space, and prints out when an object is hit.

## Observations:

* **Non-moving collector issue**: Green Tea cannot reclaim sparse pages due to its design.
* **GC behavior in Go 1.26**: The default garbage collection is modified to avoid non-moving collectors like Green Tea in Go 1.26.

## Takeaways

* Go's heap management relies on allocated objects being of the same size class within contiguous chunks.
* Green Tea, while introduced as a new GC, struggled with sparse-page problems and does not reclaim them due to its design.
* Observations about non-moving collectors like Green Tea are addressed, highlighting the challenges faced by these collectors in Go.