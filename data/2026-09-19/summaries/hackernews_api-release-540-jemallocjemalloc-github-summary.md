---
title: Release 5.4.0 · jemalloc/jemalloc · GitHub
url: https://github.com/jemalloc/jemalloc/releases/tag/5.4.0
date: 2026-09-18
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-19T06:01:38.438314
---

# Release 5.4.0 · jemalloc/jemalloc · GitHub

# jemalloc 5.4.0 Release Summary

## Overview
- Release includes over 160 commits.
- Focuses on technical debt cleanup: refactorings, bug fixes, test coverage improvement, option cleanups.
- Adds portability improvements based on upstream issue reports.

## New Features
- Added `EXTENT_ALLOC_FLAG_PINNED` so custom extent‑allocation hooks can mark non‑reclaimable mappings (e.g., HugeTLB pages) for preferential reuse outside decay and purge pipelines. New `mallctl` interfaces report pinned‑memory usage and related mutex statistics.
- Enabled resuming per‑CPU arena selection via `thread.arena`.
- Aligned human‑readable and JSON malloc statistics for consistency.
- Replaced runtime `experimental_infallible_new` option with compile‑time `--enable-cxx-infallible-new`, allowing compiler‑level optimizations and fixing the `new(std::nothrow)` contract.

## Incompatible Changes
- tcache fill and retention targets now adapt per bin based on observed demand, replacing the fixed refill/flush policy.
- Removed seven legacy non‑experimental controls (`lg_tcache_nslots_mul`, `tcache_nslots_small_min`, `tcache_nslots_small_max`, `tcache_nslots_large`, `tcache_gc_delay_bytes`, `lg_tcache_flush_small_div`, `lg_tcache_flush_large_div`). Corresponding `malloc_conf` settings are ignored, `opt.*mallctls` return `ENOENT`, and `tcache_ncached_max` remains supported.

## Bug Fixes
- Preserved `errno` across `free`, `free_sized`, `free_aligned_sized`, and process‑madvise‑based page purging.
- Fixed numeric overflow checks in size classes.
- Accepted `NULL` in `free_sized()` and `free_aligned_sized()` (C23 compliance).
- Resolved TSD lifecycle edge cases by initializing thread‑cache bins before marking the cache enabled and avoiding TSD recreation after thread teardown on generic‑TSD platforms.
- Used `O_CLOEXEC` when opening the THP sysfs file in `init_thp_state`.
- Fixed duplicate `opt.stats_print` fields in `malloc_stats_print` output.
- Fixed a potential deadlock during `arena_reset`.
- Fixed a profiler‑sampling / guard‑page interaction bug in the SAN.

## Optimizations and Refactors
- Modularized the front end: extracted arena management, initialization, fork orchestration, and allocation dispatch from `jemalloc.c`; untangled tcache/arena ownership; cleaned internal header graph.
- Simplified ctl dispatch: refactored arena helpers, internalized an implementation‑only control, replaced control‑flow macros with typed helpers, and reorganized `ctl.c` by subsystem.
- Capped the base‑block growth heuristic to avoid virtual‑memory exhaustion under rare racy conditions.
- Moved background‑thread lifecycle and state operations into a dedicated module.
- Simplified page‑allocation boundary by replacing PAI vtable dispatch with direct PAC/HPA calls, removing the obsolete `pai_t` abstraction, and moving deferred work and decay orchestration out of the arena.
- Refactored statistics collection into separate gather/emission stages with descriptor‑driven tables.
- Introduced an OS abstraction layer, moving platform‑dependent file/process I/O, time, synchronization, CPU, virtual‑memory, at‑fork handling, error handling, profiling, thread‑yield, and configuration access out of the allocator core.

## Portability Improvements
- Replaced `std::__throw_bad_alloc` call with standard C++.
- Made `arena_s` a flexible array member (`bin_t all_bins[]`) for C99 or newer.
- Fixed `rdtscp` detection with `--with-lg-vaddr`.
- Corrected `malloc_getcpu` on macOS to read the current CPU number properly.
- Used `CLOCK_MONOTONIC` for background‑thread sleep to prevent clock‑rollback stalls; detected monotonic condvar support at configure time.
- Fixed compilation warnings on macOS.
- Fixed thread‑exit TSD cleanup on MinGW builds.
- Resolved GCC 16 build warnings by removing `-Wpedantic` violations and explicitly NUL‑terminating profiling thread‑name copies.
- Parsed PID‑namespace symlinks without glibc‑dependent `strtok`/`atol`, returning identifiers as `uint64_t`.

## Contributors
- fzakaria, Algunenano, and 11 other contributors.