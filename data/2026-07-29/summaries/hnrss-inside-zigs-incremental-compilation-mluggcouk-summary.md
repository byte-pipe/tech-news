---
title: "Inside Zig's Incremental Compilation | mlugg.co.uk"
url: https://mlugg.co.uk/posts/incremental-compilation-internals/
date: 2026-07-28
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-29T12:32:18.498936
---

# Inside Zig's Incremental Compilation | mlugg.co.uk

# Inside Zig's Incremental Compilation

## Overview
- Implemented incremental compilation in the Zig compiler to recompile only changed functions/declarations and patch the binary, achieving rebuilds in 50–70 ms after an initial ~5 s build.  
- Feature matured from proof‑of‑concept to daily‑use across the Zig core team; fully usable on the master branch (awaiting release 0.17.0 for tagged versions).

## Demonstration
- Video shows rapid edits to **Fizzy**, a pixel editor, with rebuild times of 50–70 ms per change.  
- Requires Zig master because Zig 0.16.0 lacks necessary linker support.

## Processing Source Files
- **Pipeline (per file):**
  1. Read source from disk.  
  2. Parse into an AST.  
  3. Convert AST to **ZIR** (Zig Intermediate Representation, an untyped SSA‑form IR).  
- While generating ZIR, imports are discovered, causing the loop to repeat for all reachable files.  
- **Key properties:**
  - Pure function of file contents; no external state.  
  - Parse + AstGen for the whole compiler source take ~920 ms on a laptop (single‑threaded).  
  - ZIR can be written/read with a single `writev`/`readv` call—no extra serialization.  
- **Consequences:**  
  - Naturally embarrassingly parallel; each file can be processed as an independent task with only a mutex‑protected hash set for already‑seen paths.  
  - Incremental compilation is trivial: cache each file’s ZIR on disk and rebuild only when the source changes.  
- These optimizations have been default in Zig for years and are visible in the “AST Lowering” progress output.

## Semantic Analysis
- **Purpose:** Interpret ZIR, perform type checking, comptime evaluation, and produce the next IR stage for runtime functions.  
- **Terminology:** “container‑level declaration” = top‑level entity (function, global const, or global variable).  
- **Challenge:** Incremental handling is hardest here because analysis units depend on each other.  
- **Design for Incrementality:**  
  - Split compilation into **analysis units** that can be analyzed mostly independently, with dependencies captured in a graph.  
  - Zig defines four unit kinds:  
    1. Layout of a struct/union type.  
    2. Type of a container‑level declaration.  
    3. Value of a container‑level const declaration.  
    4. Body of a runtime function.  
- **Dependency tracking example (function `foo`):**  
  - Analyzes both branches because `cond` isn’t comptime‑known.  
  - Adds dependencies on the *type* of `global_0` and `global_1`.  
  - Adds a dependency on the *value* of `global_1` because it’s comptime‑known.  
  - Result: the function body depends on those types/values, so any change to them triggers reanalysis of `foo`.  

## Incremental Compilation Mechanics
- **Caching:** Each analysis unit’s result is stored on disk; on a rebuild the compiler checks file timestamps and the dependency graph to decide which units need recomputation.  
- **Parallelism:** Units without inter‑dependencies are processed concurrently on a thread pool.  
- **Rebuild speed:** Because only a tiny fraction of units change per edit, the compiler patches the binary directly, avoiding full relinking.

## Using Incremental Compilation
- To try it now, build with the master branch of Zig (or wait for 0.17.0).  
- The article’s final section (not reproduced here) provides command‑line flags and environment settings to enable the feature in user projects.

## Takeaways
- Zig’s incremental compilation combines fast, pure‑function file processing, disk‑cached ZIR, and a fine‑grained dependency graph of analysis units.  
- The design choices (data‑oriented structures, explicit unit types, minimal shared state) make the pipeline both parallelizable and cache‑friendly.  
- Real‑world impact: developers can iterate on complex applications with sub‑100 ms rebuilds, dramatically improving development turnaround.