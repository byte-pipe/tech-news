---
title: "It's the memory latency, stupid · Pivot blog"
url: https://pivotlake.io/blog/its-the-memory-latency-stupid/
date: 2026-10-31
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-01T18:54:24.901786
---

# It's the memory latency, stupid · Pivot blog

# It’s the memory latency, stupid

## Why a “100 %” CPU can still be idle  
- CPUs appear fully utilized when the scheduler gives them all time slices, but they may spend most of that time waiting for data.  
- Memory accesses are orders of magnitude slower than internal CPU operations: a modern core can execute 4–8 instructions per nanosecond, while a DRAM read takes ~50–100 ns.  
- Consequently a CPU can perform 400–800 instructions for every RAM access, so any workload that constantly fetches from RAM will be throttled by latency rather than compute.

## Cache hierarchy and its role  
- **L1 cache** – ~1 ns latency, ~64 KB, ~4–8 instructions per access.  
- **L2 cache** – ~3–4 ns, ~1 MB, ~15–30 instructions per access.  
- **L3 cache** – ~10–15 ns, up to a few hundred MB, ~50–100 instructions per access.  
- **DRAM** – ~50–100 ns, GBs of capacity, ~400–800 instructions per access.  
- Caches keep frequently used data close to the core; their limited size forces algorithms to be cache‑friendly for good performance.

## Naïve GROUP BY example  
- A simple hash‑table aggregation (`count(*) GROUP BY UserID`) on the ClickBench “hits” table (99 M rows, ~17 M distinct users) was implemented with a single `HashMap`.  
- Each new key caused a “cold” cache miss, pulling the entry from RAM.  
- Measured on an AMD EPYC 9124 (16 cores, 128 GB DDR5) pinned to one core:  
  - Query time ≈ 3.6 s after warm‑up.  
  - `perf stat` showed **50.1 %** of cycles stalled on memory (`backend_bound_memory`).  
  - Only **16.1 %** of cycles were retiring useful micro‑ops.  
  - DRAM loads counted ≈ 76 M cache‑line fills → ~4.5 GB transferred from RAM during the query.

## Improving cache utilization with radix partitioning  
- The workload is split into two phases:  
  1. **Partitioning** – hash each key, take the top 12 bits (4096 partitions), and append the `(hash, key)` pair to a per‑partition `SlabVec`. This groups keys that will later fit into cache lines.  
  2. **Aggregation** – process each partition independently, allowing the hash table for a single partition to stay mostly in L1/L2 cache.  
- By limiting the working set per partition, the algorithm reduces DRAM accesses and increases the proportion of retiring cycles (results not shown in the excerpt but implied to be significantly better).

## Key take‑aways  
- High CPU utilization metrics can be misleading; memory latency is often the real bottleneck.  
- Understanding the cache hierarchy and designing algorithms that stay within cache limits is essential for database performance.  
- Simple changes such as radix partitioning can transform a memory‑bound workload into a compute‑bound one, dramatically lowering query latency.