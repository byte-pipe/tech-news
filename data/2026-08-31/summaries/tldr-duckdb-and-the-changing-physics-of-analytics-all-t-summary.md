---
title: DuckDB and the changing physics of analytics | All Things Distributed
url: https://www.allthingsdistributed.com/2026/08/duckdb-and-the-changing-physics-of-analytics.html
date: 2026-08-31
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-31T02:22:47.969396
---

# DuckDB and the changing physics of analytics | All Things Distributed

# DuckDB and the changing physics of analytics

## Overview
- Traditional data processing relied on separate, large‑scale systems (databases, warehouses, distributed query engines) because compute, memory, and network were limiting factors.  
- Modern hardware has reduced those constraints, allowing substantial analytics to run inside a single application process.  
- DuckDB exemplifies this shift, offering an in‑process analytical engine that complements AWS S3‑based data storage and is now part of AWS through the DuckLabs team.

## The “physics” of systems design
- Computer systems evolve by adapting to the relative speeds and capacities of memory, CPU, and network—what the author calls changing “physics.”  
- Historical examples:  
  - **Berkeley NOW** leveraged cheap CPUs and emerging network bandwidth for scalable clusters.  
  - **Xen hypervisor** exploited abundant CPU/memory to provide isolated VMs on commodity servers.  
  - **MonetDB/X100** re‑engineered query execution to fit data into CPU caches once disk I/O ceased to be the bottleneck.  
- Design ideas often cycle: concepts from 1960s mainframes (e.g., virtualization) reappear on modern servers when hardware conditions align.

## Why data processing has been a distributed problem
- Complex queries create data dependencies that demand fast, shared memory; parallelizing across many nodes introduces overhead and memory pressure.  
- When dataset size outpaces a single machine’s I/O bandwidth, the “physics” of the era forced a scale‑out approach.  
- Early‑2000s constraints (limited NIC/disk speed) led to:
  - **MapReduce** (Google) – partition‑and‑combine model for massive data.  
  - **Spark RDDs** – in‑memory distributed collections with lazy evaluation for better performance.

## Contributions of distributed query engines
- **Developer ergonomics:**  
  - MapReduce popularized a functional “map‑group‑by‑aggregate” pattern that made parallelism explicit.  
  - Spark introduced lazy operator chaining and DataFrames, letting developers write high‑level code while the engine handled task planning and distribution.  
- These abstractions let programmers ignore the underlying network, focusing on logic rather than execution details.

## The emerging in‑process analytics paradigm
- Declining cost of memory, faster CPUs, and high‑throughput local storage make it feasible to run analytical workloads directly where data resides (e.g., inside a Python, R, or Rust process).  
- DuckDB provides:
  - Full SQL support with vectorized execution.  
  - Zero‑configuration, embeddable engine that works on a single node but can query external data sources (Parquet, CSV, S3).  
  - Compatibility with existing data‑lake formats, allowing “bring‑the‑engine‑to‑the‑data” rather than moving data to a separate cluster.

## How DuckDB complements AWS S3
- S3 Files, S3 Tables, and S3 Vectors expose cloud‑stored data as if it were local, enabling DuckDB to scan and process data directly from S3 without a separate compute cluster.  
- This model reduces data movement, lowers latency, and simplifies pipelines: developers can write a single DuckDB query that reads from S3, performs complex analytics, and writes results back to S3.

## Why DuckLabs is joining AWS
- Integration with AWS accelerates the adoption of in‑process analytics at cloud scale.  
- AWS can provide managed services, security, and scaling primitives while preserving DuckDB’s lightweight, embeddable nature.  
- The partnership aims to blend the best of both worlds: the simplicity of DuckDB with the robustness and ecosystem of AWS.

## Takeaways
- The “physics” governing data systems are shifting; what once required massive distributed clusters can now be handled on a single machine.  
- DuckDB embodies this new reality, offering an efficient, embeddable SQL engine that works directly with modern storage layers like S3.  
- The DuckLabs‑AWS collaboration signals a broader industry move toward tighter integration of in‑process analytics within cloud platforms, reducing complexity and cost for data‑intensive applications.