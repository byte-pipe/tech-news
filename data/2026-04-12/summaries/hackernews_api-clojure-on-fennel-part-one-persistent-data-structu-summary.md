---
title: Clojure on Fennel part one: Persistent Data Structures · Andrey Listopadov
url: https://andreyor.st/posts/2026-04-07-clojure-on-fennel-part-one-persistent-data-structures/
date: 2026-04-07
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-12T06:03:33.394551
---

# Clojure on Fennel part one: Persistent Data Structures · Andrey Listopadov

# Clojure on Fennel – Part One: Persistent Data Structures

## Background and Motivation
- In 2019 the author created **fennel‑cljlib**, a Fennel library that re‑implemented a subset of `clojure.core` (functions, macros, lazy sequences, immutability, testing, core.async).  
- It was mainly an experiment; the only real‑world use was the `fenneldoc` documentation tool.  
- The library relied on a copy‑on‑write approach with Lua metatables, which made immutable operations very slow.

## New Project: ClojureFnl
- A Clojure‑to‑Fennel compiler built on top of fennel‑cljlib.  
- Early version (v0.0.1) can compile most `.cljc` files, but runtime support for the standard library is incomplete.  
- Demonstrated REPL session showing a prime‑checking function and a simple prime number generator.

## Need for Proper Persistent Structures
- The original immutable tables copied entire structures on each mutation, especially costly for arrays.  
- Transients helped a bit, but Clojure’s performance comes from true persistent data structures with structural sharing.

## Chosen Data Structures
- **Persistent HAMT** for hash maps and sets (branching factor 16).  
- **Bit‑partitioned trie** for vectors.  
- **Immutable red‑black tree** for sorted maps/sets.  
- **Lazy linked lists** for sequences.

## Implementation Decisions
- Implemented entirely in Fennel (`immutable.fnl`) to keep the library usable from the compiler.  
- Branching factor 16 balances depth and copy cost on Lua (vs. Clojure’s 32).  
- Used the `jb2` hash algorithm (simple arithmetic only) to stay compatible with Lua versions lacking bitwise operators.

## Benchmark Results (PUC Lua 5.5, 50 000 elements)

| Operation | Lua table | Persistent HashMap | Ratio | Transient HashMap |
|-----------|-----------|-------------------|-------|-------------------|
| Insert 50k random keys | 2.05 ms | 164.80 ms | ~80× slower | 89.17 ms (~43× slower) |
| Lookup 50k random keys | 0.83 ms | 92.51 ms | ~111× slower | – |
| Delete all | 0.78 ms | 170.78 ms | ~220× slower | 104.31 ms (~138× slower) |
| Delete 10 % | 0.14 ms | 19.50 ms | ~136× slower | 12.71 ms (~82× slower) |
| Iterate 50k entries | 1.74 ms | 6.64 ms | ~3.8× slower | – |

### LuaJIT (macOS/arm64) Highlights
- Persistent map insert: 0.86 ms → 49.05 ms (≈57× slower).  
- Lookup: 0.27 ms → 14.21 ms (≈53× slower).  
- Iteration: 0.07 ms → 1.80 ms (≈28× slower).  
- Transient map insert: 0.76 ms → 22.43 ms (≈30× slower).

## Observations
- Persistent structures are noticeably slower than native Lua tables, which is expected because tables are C‑implemented with highly optimized hashing.  
- Transients reduce the overhead but still remain an order of magnitude slower.  
- Branching factor 32 would worsen performance on PUC Lua, slightly improve it on LuaJIT, indicating room for tuning.

## Next Steps (Implied)
- Optimize the HAMT implementation (e.g., explore different branching factors, improve hashing).  
- Continue integrating the persistent structures into ClojureFnl’s runtime library.  
- Expand support for hash sets, ordered maps, and compound vector/hash structures.