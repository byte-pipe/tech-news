---
title: Backfilling: the most underrated feature of a data pipeline
url: https://thesis.optoinvest.com/posts/backfilling-most-underrated-feature/
date: 2026-07-24
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-24T05:40:31.111634
---

# Backfilling: the most underrated feature of a data pipeline

# Backfilling: the most underrated feature of a data pipeline

## What backfilling means
- Appears in two forms that are often conflated:  
  1. **Historical ingestion** – loading data that existed before the pipeline (e.g., decades of SEC Form ADV filings) with the same rigor as new data.  
  2. **Migration** – moving data already stored in an internal system to a new one, a process that is usually painful and incomplete.  
- The author treats both as the same underlying problem and designs the pipeline accordingly.

## Migration code is production code
- The pipeline is split into three stages: **extract**, **raw**, and **transform**.  
- Instead of writing a one‑off script for backfills, the backfill runs through the same pipeline with a configuration flag that selects the mode.  
- Example modes (implemented via a Dagster config object):  
  - **Incremental** – process only new or changed records (default, cheapest).  
  - **Full refresh** – rebuild everything from raw; used for schema changes, recovery, or initial historical load.  
  - **Single entity** – reprocess a specific record on demand, useful for quick customer queries.

## Why this matters: transform logic stays unchanged
- The contract for the transform stage is identical regardless of mode: it receives batches of keys and processes them.  
- The same `process_batch` loop runs for a single record, a few thousand, or millions of rows, eliminating separate “backfill logic” that would be less tested.

## Backfills are safe because time is bi‑temporal
- Writes include both **business time** (the effective date of the data) and **system time** (when the row was written).  
- Re‑running a backfill creates new system‑time versions rather than overwriting existing rows, preserving full history.  
- This is achieved with a `bi-temporal-merge` mode when writing to DuckDB/Delta tables.

## Analyzing the results with MotherDuck
- The **raw** layer stores source data in table form with zero assumptions, avoiding the “bronze → silver → gold” framing that assumes pre‑existing tables.  
- Using the MotherDuck MCP server, the author inspected `transform.form_adv_firm_ownership` and noted:  
  - All 1.8 M rows share the same `system_valid_from` timestamp, confirming a recent full refresh.  
  - Ownership status values are highly fragmented (309 distinct values, many comma‑joined); only three categories cover <30 % of non‑null rows, and 48 % are null, indicating a normalization opportunity.  
  - The dataset spans 26 years, showing clear open/close patterns that track real ownership changes.  
  - Record volume has grown from ~30 k per year in 2002 to ~114 k in 2024, reflecting market growth and tighter SEC reporting after 2012.

## Takeaway
- Design backfilling into the pipeline from day one rather than as an afterthought.  
- Treat backfill code as production code, driven by configuration, so it receives the same testing and monitoring as the forward‑only pipeline.  
- Leverage bi‑temporal merges to keep history intact when re‑processing data.  
- A unified, resilient backfill approach reduces firefighting and frees time for deeper data analysis.