---
title: How a 40-Line Fix Eliminated a 400x Performance Gap | QuestDB
url: https://questdb.com/blog/jvm-current-thread-user-time/
date: 2026-01-14
site: hackernews
model: llama3.2:1b
summarized_at: 2026-01-14T11:12:44.338009
screenshot: hackernews-how-a-40-line-fix-eliminated-a-400x-performance-ga.png
---

# How a 40-Line Fix Eliminated a 400x Performance Gap | QuestDB

**Understandings of the Original Code and BUG**

* The original code was for reading /proc/self/task/%d/stat to get thread CPU time on Linux.
* It involved a 55-line JMH benchmark, which reduced production code size by making `getCurrentThreadCpuTime()` faster due to improved caching efficiency.
* The deleted code performed the same task as the updated JMH benchmark and production code.

**Identifying the Main Issue**

* The main issue is that `clock_gettime()` was used while a 55-line benchmark had been added, reducing performance. This implies that the old implementation required significant time spent on reading /proc/self/task/%, which was replaced by the faster and more cache-friendly JMH benchmark.

**Breaking Down the Changes**

* Key points:
	1. The new file `os::snprintf_checked` changed the behavior of `/proc/self/task/%d/stat`.
	2. The old code inserted characters into the input string using `s = strrchr(stat, ')')`, while the updated JMH benchmark uses sscanf() to parse the string.
* Important details:
	1. The new file is likely a "snprintf_checked" function that ensures proper null-termination of the input string.
	2. The old code was appending characters and skipping whitespace using `s += '...'`.
	3. The JMH benchmark reduces the number of CPU seconds taken by 400x due to improved caching.

**Capturing the Key Findings in a Summary**

The summary below highlights the key findings:

* A significant gap exists between `/proc/self/task/%d/stat` read operation and JMH benchmark (~400x slower).
* The old implementation was appending characters to the input string using `s += '...'`, instead of using `sscanf()` for parsing.
* Improved code reads /proc/self/task/+/stat directly, reducing performance by potentially increasing cache misses.

I'll keep these points in mind as I generate the summary.
