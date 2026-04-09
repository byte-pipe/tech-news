---
title: lsr: ls but with io_uring - rockorager.dev
url: https://rockorager.dev/log/lsr-ls-but-with-io-uring/
date: 2025-07-18
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-07-19T23:10:09.996288
---

# lsr: ls but with io_uring - rockorager.dev

**Benchmarks Analysis**

The author presents benchmarks for their implementation, `lsr`, using `ls` with and without the `io_uring` library. The goals are to measure performance and minimize system calls.

| Method | Time (µs) | Syscalls |
| --- | --- | --- |
| LSR | 372.6 ± 634.3 ± 22.1 ± 38.0 | 20, 28, 105, 848 |
| `ls` (traditional) | 1.4 ± 1.7 ± 4.7 ± 40.2 | 405, 675, 3,337, 30,396 |

**Market Indicators**

* Number of users: As the author observes, `lsr` may appeal to developers who value speed and efficiency.
* Revenue mentions: There are no explicit revenue mentions, but the benchmark results suggest a potential market for faster, more efficient storage systems.

**Technical Feasibility**

* Complexity: The implementation has several complex aspects, such as error handling, memory management, and synchronization using `io_uring`. Solo developers need expertise in these areas to maintain.
* Required skills: The author suggests that solo developers will need knowledge of C, Linux, and possibly a few extra areas like memory management and concurrency.
* Time investment: Completing the implementation, testing, and fine-tuning may require significant time.

**Business Viability Signals**

* Willingness to pay: There is no explicit revenue mention, but the author's performance guarantee (order of magnitude fewer syscalls) suggests a willingness to invest in their solution.
* Existing competition: The benchmark results suggest that there are alternatives available, and `lsr` may need to compete with these solutions.

**Actionable Insights for Solo Developers**

1. **Focus on efficiency**: Since `lsr` achieves an order of magnitude better performance than the baseline alternative (`eza`) without using `io_uring`, solo developers can prioritize performance optimization.
2. **Invest in a robust memory management system**: The Zig stdlib StackFallbackAllocator used by `lsr` indicates that memory management is crucial. Solo developers should consider implementing similar features to prevent potential issues with large datasets or memory-intensive computations.
3. **Plan for scalability**: As `lsr` scales up to larger directories, the `io_uring` bottleneck may become more apparent. Solo developers should anticipate potential bottlenecks and plan accordingly.

Extracted numbers:

* 138.7KB (size of GNU ls relative to `ls` built with ReleaseSmall)
* 790.3KB (`ls` with release libc)
