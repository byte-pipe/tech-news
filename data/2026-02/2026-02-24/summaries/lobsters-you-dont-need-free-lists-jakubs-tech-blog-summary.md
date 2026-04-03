---
title: "You don't need free lists! | Jakub's tech blog"
url: https://jakubtomsu.github.io/posts/bit_pools/
date: 2026-02-24
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-24T06:03:25.075280
---

# You don't need free lists! | Jakub's tech blog

# You don't need free lists!

This article discusses an alternative to traditional free lists for managing memory pools, particularly when combined with generational handles. The author proposes a multi-level bit array approach inspired by the TLS memory allocator.

## Traditional Free Lists vs. Bit Pools

Traditional free lists maintain a list of unused memory slots, offering O(1) allocation, deallocation, and lookup. However, the article points out a potential issue where the allocation pattern can become random over time. The author introduces a bit pool as a more efficient alternative.

## Bit Pool Structure

The proposed bit pool uses a multi-level bit array. It consists of:

*   **L0:** A 64-bit array where each bit represents a block of 64 slots.
*   **L1:** An array that stores information about the status (full or empty) of each block in L0.

## Trailing Zero Count (tzcnt)

The article highlights the use of the `tzcnt` instruction (trailing zero count) on x64 architectures. This instruction efficiently counts the number of trailing zeros in a register, allowing for fast identification of the first unused bit in the `used` mask.

## Searching for Empty Slots

The `find_0` procedure searches for an empty slot in the bit pool. It iterates through the L1 array to find a full block and then uses `tzcnt` on the corresponding L0 block to find the first unused slot within that block.

## Advantages of the Bit Pool

*   **Low Overhead:** Each slot requires only approximately 1 bit.
*   **Improved Memory Locality:** The allocation strategy tends to allocate slots with the lowest index first, leading to better memory locality compared to list-based pools.
*   **Potential for SIMD:** The bit array structure lends itself well to SIMD (Single Instruction, Multiple Data) operations, enabling parallel processing of multiple slots.

## Further Improvements

The bit pool can be extended with more levels for very large pools, maintaining O(1) complexity.

## AoSoA (Arrays of Structures of Arrays)

The bit pool's structure is suitable for AoSoA, where the `used.l0` array can be treated as a mask for SIMD operations, allowing for efficient processing of multiple data elements simultaneously.

## Conclusion

The author argues that bit pools offer a compelling alternative to traditional free lists, providing better performance and memory locality, especially in scenarios with frequent and burst-like memory allocations. A full implementation is available on GitHub as part of the Raven engine.
