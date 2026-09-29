---
title: Can your Postgres survive a bad query? | ClickHouse
url: https://clickhouse.com/blog/can-your-postgres-survive-a-bad-query
date: 2026-09-30
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-30T06:01:13.556211
---

# Can your Postgres survive a bad query? | ClickHouse

# Can your Postgres survive a bad query?

## Introduction
- Choosing a Postgres provider involves performance, pricing, extensions, and reliability.
- Reliability is defined as the ability to handle unexpected workloads without failure.
- Memory‑tuning problems and automated agents increase the risk of accidental overloads.

## Memory‑management limits in Postgres
- Postgres lacks a hard per‑query RAM cap; it only provides `work_mem` (default 4 MB) per **operation**.
- Each node in a query plan receives its own `work_mem` budget; hash‑based nodes get an additional multiplier (`hash_mem_multiplier`, default 2.0).
- Actual memory consumption can be many times the `work_mem` setting.

## Example schema and query
- Two tables (`wm_api_keys`, `wm_api_calls`) support a simple LLM inference service.
- A console view runs a `SELECT … GROUP BY … ORDER BY total_cost_usd DESC` query.
- With 2 000 keys and 30 000 calls the plan uses ~0.8 MB total memory, well under the default limit.

## Scaling effects
- After growth to 55 000 keys and 9 million calls:
  - Table size exceeds `min_parallel_table_scan_size`, triggering parallel workers.
  - Each worker builds its own copy of memory‑using nodes, roughly tripling RAM usage.
  - Nodes spill to disk because they exceed their per‑node `work_mem` caps.
  - Observed usage: ~33 MB RAM and ~23 MB temporary disk I/O per query execution.

## Parallel workers and memory multiplication
- Parallelism multiplies memory consumption because every worker has independent `work_mem` budgets.
- Hash nodes use `work_mem * hash_mem_multiplier`; with default values this can be 8 MB per worker.
- Raising `work_mem` to avoid spilling (e.g., to 8 MB) increases total RAM usage proportionally (≈68 MB across workers).

## Spilling behavior
- Spilling occurs when a node’s memory demand exceeds its allocated budget.
- Disk‑based spill is applied to hash aggregates and sorts, but not to all executor structures.

## Structures that do not spill
- Some executor allocations are kept entirely in memory with no disk fallback.
- Under pathological data distributions these structures can grow unchecked, leading to out‑of‑memory (OOM) failures regardless of `work_mem` settings.
- This limitation means that even well‑tuned queries can exceed memory limits in edge cases.

## Takeaways
- Postgres reliability is challenged by:
  - Per‑node memory budgeting rather than a global query cap.
  - Parallel workers multiplying memory consumption.
  - Select executor structures lacking spill support.
- Proper tuning requires awareness of how parallelism and hash multipliers affect total memory.
- Simply increasing `work_mem` may prevent spills but can raise overall RAM usage dramatically.
- Understanding and monitoring these factors is essential to prevent accidental OOM crashes in production workloads.