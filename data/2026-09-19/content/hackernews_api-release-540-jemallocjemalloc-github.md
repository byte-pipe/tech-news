---
title: Release 5.4.0 · jemalloc/jemalloc · GitHub
url: https://github.com/jemalloc/jemalloc/releases/tag/5.4.0
site_name: hackernews_api
content_file: hackernews_api-release-540-jemallocjemalloc-github
fetched_at: '2026-09-19T06:00:25.578654'
original_url: https://github.com/jemalloc/jemalloc/releases/tag/5.4.0
author: gkfasdfasdf
date: '2026-09-18'
description: Contribute to jemalloc/jemalloc development by creating an account on GitHub.
tags:
- hackernews
- trending
---

jemalloc

 

/

jemalloc

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.6k
* Star11.2k

 

# 5.4.0

Latest

Latest

 

Compare

# Choose a tag to compare

 

## Sorry, something went wrong.

 

 Filter

 
Loading

 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

## No results found

 

 
 

View all tags

 

guangli-dai

 released this

 

 17 Sep 18:31
 

 ·
 

 5 commits
 

 to dev
 since this release
 

 5.4.0
 

7a34f18

This release contains over 160 commits, focusing on the technical debtscleaning including refactorings, bug fixes, test coverage improvement, andoption cleanups. The release also includes portability improvements perupstream issues report.

New features:

* AddEXTENT_ALLOC_FLAG_PINNEDso custom extent-allocation hooks canmark non-reclaimable mappings, such as HugeTLB pages, for preferentialreuse outside the decay and purge pipeline. Add the mallctl interfacesstats.pinned,stats.arenas.<i>.pinned,stats.arenas.<i>.extents.<j>.npinned,stats.arenas.<i>.extents.<j>.pinned_bytes, andstats.arenas.<i>.mutexes.extents_pinned.{counter}to reportpinned-memory usage and mutex statistics. (@binliu19:be2de8c)
* Allow resuming per-CPU arena selection viathread.arena.(@Algunenano:68c35f6)
* Better align the contents of human-readable and JSON malloc statistics.(@spredolac:68fe1be,30b1a41,04aad97)
* Replace the runtimeexperimental_infallible_newoption with thecompile-time--enable-cxx-infallible-newoption, enablingcompiler-level optimizations and optimization in move constructors,and fix thenew(std::nothrow)contract (@spredolac:160ab9d,fe33667)

Incompatible changes:

* Adapt tcache fill and retention targets per bin to demand observedbetween GC events, replacing the fixed refill/flush policy. Removeseven legacy non-experimental controls:lg_tcache_nslots_mul,tcache_nslots_small_min,tcache_nslots_small_max,tcache_nslots_large,tcache_gc_delay_bytes,lg_tcache_flush_small_div, andlg_tcache_flush_large_div.Correspondingmalloc_confsettings are silently ignored, matchingopt.*mallctls return ENOENT, andtcache_ncached_maxremainssupported. (@spredolac:d13fe91)

Bug fixes:

* Preserveerrnoacrossfree,free_sized, andfree_aligned_sized,and acrossprocess_madvise-based page purging. (@spredolac:3a77966,86f0582)
* Fix numeric overflow checks in size classes. (@spredolac:6b24522)
* Accept NULL infree_sized()andfree_aligned_sized()(C23correctness). (@bigbruno:7ce8b91)
* Fix TSD lifecycle edge cases by 1) initializing thread-cache bins beforemarking the cache enabled, preventing reentrant bootstrap allocationsfrom using uninitialized state, and 2) avoiding TSD recreation for latedeallocations after thread teardown on generic-TSD platforms.(@fzakaria:54f22c8,@spredolac:fb5499a)
* UseO_CLOEXECwhen opening the THP sysfs file ininit_thp_state.(@ibookstein:d070554)
* Fix duplicateopt.stats_printandopt.stats_print_optsfields inmalloc_stats_printoutput. (@spredolac:dfe3a2e)
* Fix a potential deadlock duringarena_reset. (@guangli-dai:6957341)
* Fix a prof-sampling / guard-page interaction bug in the SAN. (@gctony:e36a0fa)

Optimizations and refactors:

* Modularize jemalloc's front end by extracting arena management,initialization, fork orchestration, and allocation dispatch fromjemalloc.c; untangle tcache/arena ownership; and consolidate theinternal header graph to eliminate circular dependencies. (@spredolac:ba1e2fe,8874597,9d75722,de9ad14, ...)
* Simplify ctl dispatch by refactoring arena helpers, internalizing animplementation-only control, replacing control-flow macros with typedhelpers, and organizingctl.cby subsystem. (@spredolac:9e14346,901365d,4e903a0,5bc8d6e)
* Cap the base-block growth heuristic to avoid virtual-memory exhaustionunder rare racy conditions. (@guangli-dai:2f4db8c)
* Move background-thread lifecycle and state operations into thebackground-thread module, clarifying ownership independently of PAC/HPAcallers. (@guangli-dai:f1f0792)
* Simplify the page-allocation boundary by replacing PAI vtable dispatchwith direct PAC/HPA calls, removing the obsoletepai_t/pai.habstraction, and moving deferred-work and decay orchestration out of thearena. (@guangli-dai:1dfa6f7,8edd101,d410f43)
* Refactor statistics collection and rendering into separategather/emission stages and descriptor-driven tables. (@spredolac:184f304,80c8fcb)
* Introduce an OS abstraction layer and move platform-dependentfile/process I/O, time, synchronization, CPU, virtual-memory, atfork,error-handling, profiling, thread-yield, and configuration-accessoperations out of allocator core code. (@guangli-dai:c4158ac,c8e2e01, ...)

Portability improvements:

* Replace thestd::__throw_bad_alloccall with standard C++ (#2900).(@lexprfuncall:1a15fe3)
* Makearena_suse a flexible array member (bin_t all_bins[]) for C99or newer. (@grueninger:300b58b)
* Fix rdtscp detection with--with-lg-vaddr. (@xinydev:e8a0d2b)
* Fixmalloc_getcpuon macOS to read the current CPU number correctly.(@Algunenano:5aabbc8)
* UseCLOCK_MONOTONICfor background-thread sleep to preventclock-rollback stalls, and detect monotonic-condvar support at configuretime. (@antonio2368:ebacec3,8361239)
* Fix compilation warnings on macOS. (@gctony:abb0a8a)
* Fix thread-exit TSD cleanup on MinGW builds. (@gctony:1e92317)
* Fix GCC 16 build warnings by removing-Wpedanticviolations in macroand function syntax and explicitly NUL-terminating profiling thread-namecopies to resolve-Wstringop-truncation. (@grueninger:5acdcee,c22d929,@jasonangelov:6a245e0)
* Parse PID-namespace symlinks without glibc-dependentstrtok/atol,and return identifiers asuint64_t. (@guangli-dai:278d90a)

 

### Contributors

 fzakaria, Algunenano, and 11 other contributors
 

 

Assets

3

 

 
Loading

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
👍

6

 
stevleibelt, adinosaur, aatifsyed, arakus, Ignition, and n-rodriguez reacted with thumbs up emoji

 
🎉

19

 
Kriskras99, JaySon-Huang, deadmarshal, kkocdko, Safari77, Tipuch, 0x130c, Wilfred, paolobarbolini, aatifsyed, and 9 more reacted with hooray emoji

 
❤️

6

 
kkocdko, tonisole, arakus, Ignition, n-rodriguez, and kaspermarstal reacted with heart emoji

 
👀

1

 
JaySon-Huang reacted with eyes emoji

 

All reactions

 
24 people reacted

 0
 

 

Join discussion