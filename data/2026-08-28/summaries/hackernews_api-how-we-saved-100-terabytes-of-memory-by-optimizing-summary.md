---
title: How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS cache | Cloudflare Blog
url: https://blog.cloudflare.com/dns-cache-memory-optimization-1111/
date: 2026-08-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-28T17:07:32.289221
---

# How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS cache | Cloudflare Blog

# How we saved 100 TB of memory by optimizing 1.1.1.1’s DNS cache

## Overview
- Big Pineapple (the engine behind 1.1.1.1, Gateway DNS, DNS Firewall, AS112, etc.) holds >250 billion DNS cache entries, so a single wasted byte equals >250 GB of RAM fleet‑wide.  
- Five successive memory‑layout changes cut the per‑entry footprint by >50%, freeing ~100 TB of RAM (the RAM of 130 Gen 13 servers).  
- The optimizations also improved performance: insert throughput +43 %, lookup latency –19 %.

## What is cached
- Cache starts empty; fills with query responses until a per‑datacenter entry limit is reached, then evicts older/less‑popular items.  
- When EDNS Client Subnet (ECS) is used, multiple responses for the same query are stored, increasing entry count and memory pressure.  
- Each entry consists of a **CacheKey** (qname, qtype, authenticated flag, tag) and a **CacheEntry** (timestamp, TTL, hit counter, vectors of answer/authority/additional records, errors, etc.).

## Benchmark methodology
- Filled the cache with synthetic entries matching production traffic mix (56 % A, 25 % AAAA, 19 % TXT, 1‑4 records per entry).  
- Tracked allocations via a custom wrapper around Rust’s system allocator, measuring per‑entry memory, insert throughput, and lookup latency.  
- Complemented synthetic tests with resident‑memory measurements on live instances during rollout.

## 1️⃣ Replace `Vec<T>`/`String` with fixed‑size containers
- `Vec<T>` stores pointer, length, **capacity** (8 bytes) and may over‑allocate heap space.  
- Cache entries never modify stored responses, so capacity is unnecessary.  
- Switched to `Box<[T]>` for vectors and `Box<str>` for strings, eliminating the capacity field (8 bytes each).  
- 8 fields per entry → 64 bytes saved per entry → >15 TB saved across the fleet.

## 2️⃣ Collapse multiple record lists into a single list with offsets
- Original design kept separate `Vec`s for answer, authority, additional sections (each with pointer + length).  
- New design stores one contiguous list and two `u16` offsets (2 bytes each) to mark section boundaries.  
- Saves 28 bytes per entry; also reduces padding because Rust aligns structs to the largest field.

## 3️⃣ Drop redundant record owners
- Most DNS records have an owner identical to the queried domain; storing it again is wasteful.  
- When owner equals the query name, the `owner` field is set to `None` and reconstructed from the cache key at read time (no heap allocation).  
- Only records with differing owners (e.g., CNAME chains) keep a full `Box<Name>`.  
- This reduces heap allocations for the majority of records.

## 4️⃣ Pack boolean flags into a bitfield
- Several separate `bool` fields caused extra padding for alignment.  
- Combined them into a single bitflag, shrinking the struct and removing associated padding bytes.

## 5️⃣ Optimize enum size for record data
- Rust enums occupy the size of their largest variant; the biggest DNS record type (NAPTR) is 136 bytes, inflating all `RecordData` enums.  
- Re‑engineered storage so that smaller variants do not inherit the full size of the largest one (details omitted in excerpt).  
- Resulted in additional memory savings per record.

## Resulting impact
- Total memory reclaimed: ~100 TB (≈130 Gen 13 servers’ RAM).  
- Insert throughput increased by 43 %; lookup latency decreased by 19 % due to fewer allocations and better memory locality.  
- Optimizations are especially beneficial in ECS‑heavy locations where multiple variants of the same query are cached.