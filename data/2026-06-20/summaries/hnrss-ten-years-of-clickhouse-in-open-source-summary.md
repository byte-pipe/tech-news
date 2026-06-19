---
title: Ten years of ClickHouse in open source
url: https://clickhouse.com/blog/open-source-10
date: 2026-06-15
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-20T02:40:24.758385
---

# Ten years of ClickHouse in open source

# Ten years of ClickHouse in open source

## Building in the open

- Defines four openness levels (0‑3); ClickHouse aims for level 3 with full contribution guidelines, CI, roadmap, testing, documentation, and user support.  
- Serves as a reference for building high‑performance databases: modular, orthogonal, well‑documented C++ code with extensive comments.  
- Acts as a learning resource for modern C++ (C++23) and software‑engineering practices (build systems, CI, code review, AI assistance).  
- Encourages experimental contributions (new allocators, compression, hash tables, formats, sorting algorithms) that are evaluated with production‑grade scrutiny.  
- Credits every contributor in changelogs and an internal `system.contributors` table; initial ideas are acknowledged even if rewritten.

## Before open source

### Prototypes and first commits

- First commit (May 29 2009) replaced slow libc time functions; preceded the existence of ClickHouse.  
- Originated from a web‑analytics pipeline built on MySQL, C++, and custom data structures that struggled with real‑time, high‑volume logs.  
- Rapid “try‑anything” approach explored many storage engines (TokuDB, LMDB, Judy, Hadoop) and compression libraries (LZO, QuickLZ).  
- Desired a flexible reporting system; investigated column‑oriented databases after reading mailing lists and blogs.  
- Tested extensions (Infobright, InfiniDB) and analytical DBs (Vertica, MonetDB, LucidDB) but they failed on 100 billion rows/day with 500 columns.  

### Early prototypes

- **OLAPServer** (Dec 2008 – Jan 2009): simple column‑oriented storage per day/website in binary files, lightweight compression, XML‑based query API; enabled instant analysis of global Internet logs.  
- **Metrage**: custom CRDT‑style data structure for incremental aggregation with background merges, replacing massive MySQL‑based aggregated reports; supported unique‑user, visit, and click‑map metrics.  
- Both prototypes proved functional and demonstrated the feasibility of a column‑oriented, high‑throughput analytical engine, laying the groundwork for ClickHouse.