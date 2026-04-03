---
title: "Finding and Fixing Ghostty's Largest Memory Leak – Mitchell Hashimoto"
url: https://mitchellh.com/writing/ghostty-memory-leak-fix
date: 2026-01-10
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-01-11T11:26:37.450841
screenshot: hackernews_api-finding-and-fixing-ghostty-s-largest-memory-leak-m.png
---

# Finding and Fixing Ghostty's Largest Memory Leak – Mitchell Hashimoto

# Finding and Fixing Ghostty's Largest Memory Leak
=====================================================

## Overview of the Bug and Solution
-------------------------------------

A popular CLI application, Claude Code, started producing errors due to an excessive memory leak in Ghostty. The issue was caused by a logic bug around optimizing the scrollback optimization.

## Key Findings and Fixes
------------------------

1. **Memory Leaks**: A page is created directly with mmap, bypassing the main memory pool.
2. **Variable Size Pages**: Non-standard pages have variable sizes and cannot be reused.
3. **Logic Bug**: The bug caused an optimization to produce a logic error.

## Fixed Solution for Ghostty's Largest Memory Leak
-------------------------------------------------------

*   Merged the fix into an update (tip/nightly releases)
*   Tagged release: 1.3 is included with March updates

### PageList Update

*   Pages are now allocated from the main memory pool.
*   Non-standard pages are still used, but their allocation size is now fixed.

## Conclusion
--------------

Ghostty's largest memory leak has been found and fixed through a thorough analysis of its internal workings. The bug was triggered by an optimization error, which, when combined with limited conditions, led to excessive memory use. A new fix is available in the latest update (tip/nightly releases) for March.
