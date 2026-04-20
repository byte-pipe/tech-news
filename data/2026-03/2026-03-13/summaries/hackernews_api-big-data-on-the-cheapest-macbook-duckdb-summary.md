---
title: Big Data on the Cheapest MacBook – DuckDB
url: https://duckdb.org/2026/03/11/big-data-on-the-cheapest-macbook
date: 2026-03-12
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-13T03:14:50.920969
---

# Big Data on the Cheapest MacBook – DuckDB

# Big Data on the Cheapest MacBook – Summary

## Introduction
- Goal: evaluate the entry‑level MacBook Neo for database workloads using DuckDB.
- Benchmarks: ClickBench (43 analytical queries) and TPC‑DS (99 queries) at scale factors 100 and 300.
- Approach: run DuckDB v1.5.0 (ClickBench) and v1.4.4 LTS (TPC‑DS) on the laptop and compare with two cloud instances.

## Hardware Specification
- Model: MacBook Neo (released 2024).
- CPU: 6‑core Apple A18 Pro (2 performance cores, 4 efficiency cores).
- Memory: fixed 8 GB RAM.
- Storage: selectable 256 GB or 512 GB SSD; 512 GB used for tests (€800 / $700).
- Included accessories: laptop and braided USB‑C cable (no power brick in EU).

## ClickBench Results
- Dataset: 100 M rows, 14 GB Parquet / 75 GB CSV.
- Configuration: DuckDB v1.5.0, memory limit 5 GB.
- Compared machines:
  - MacBook Neo (local NVMe SSD).
  - AWS c6a.4xlarge (16 AMD EPYC vCPU, 32 GB RAM).
  - AWS c8g.metal‑48xl (192 Graviton4 vCPU, 384 GB RAM).
- Aggregate runtimes (seconds):

| Machine | Cold run median | Cold run total | Hot run median | Hot run total |
|---------|----------------|----------------|----------------|---------------|
| MacBook Neo | 0.57 | 59.73 | 0.41 | 54.27 |
| c6a.4xlarge | 1.34 | 145.08 | 0.50 | 47.86 |
| c8g.metal‑48xl | 1.54 | 169.67 | 0.05 | 4.35 |

- Observations:
  - Cold runs: MacBook Neo fastest (sub‑second median, < 1 min total) due to local SSD.
  - Hot runs: cloud instances improve more; c8g.metal‑48xl leads by an order of magnitude, but Neo still beats the mid‑size c6a.4xlarge on median query time.
  - Overall, Neo’s total hot‑run time is only ~13 % slower than the larger cloud box despite fewer CPU threads and less RAM.

## TPC‑DS Results
- Dataset generation via DuckDB tpcds extension, memory limit 6 GB.
- Scale Factor 100:
  - Median query runtime: 1.63 s.
  - Total runtime: 15.5 min.
- Scale Factor 300:
  - Median query runtime: 6.90 s.
  - Some queries spilled up to 80 GB to disk; query 67 took 51 min.
  - Total runtime for all 99 queries: 79 min (completed successfully).

## Recommendations
- For daily heavy Big Data workloads on a laptop, the Neo is not ideal:
  - Disk I/O (~1.5 GB/s) lags behind Air/Pro models (3–6 GB/s).
  - 8 GB RAM limits out‑of‑core processing.
- Suitable scenarios:
  - Use Neo as a thin client while running DuckDB in the cloud.
  - Occasional local data crunching is feasible; DuckDB handles out‑of‑core workloads reasonably well.
- If budget permits, consider higher‑spec MacBooks or Linux/Windows laptops for better performance.

## Recent DuckDB Releases
- **DuckDB 1.5.0** – announced 2026‑03‑09.
- **DuckDB 1.4.4 LTS** – announced 2026‑01‑26.
