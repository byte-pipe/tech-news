---
title: Change Data Capture: Stop Copying 50M Rows to Move 5K Changes
url: https://podostack.com/p/change-data-capture-cdc-intro
date: 2026-04-03
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-03T01:03:06.148378
---

# Change Data Capture: Stop Copying 50M Rows to Move 5K Changes

# Change Data Capture: Stop Copying 50M Rows to Move 5K Changes

## Main idea
- Nightly ETL that copies whole tables wastes compute, network, and storage; only a tiny fraction of rows actually change.
- Change Data Capture (CDC) records INSERT, UPDATE, and DELETE events as they happen and streams only the deltas downstream.
- Result: target stays in sync with source while dramatically reducing cost and latency.

## CDC approaches

### 1. Timestamp‑based
- Add `created_at` and `updated_at` columns; query rows where `updated_at` > last watermark.
- **Pros:** simplest, no extra infrastructure, works on any database, quick to implement.
- **Cons:** misses hard deletes, invisible to bulk updates or schema changes, requires soft‑delete flag or periodic full reconciliation.
- **Best for:** low‑delete, controlled‑schema environments.

### 2. Trigger‑based
- Database triggers write every change to a shadow table.
- **Pros:** captures inserts, updates, deletes; can store before/after values.
- **Cons:** adds write overhead to OLTP, database‑specific code, fragile to schema alterations.
- **Best for:** moderate write workloads where deletes must be captured without external tooling.

### 3. Log‑based (gold standard)
- Reads the database’s write‑ahead log / binlog directly (e.g., via Debezium, Fivetran).
- **Pros:** zero impact on OLTP, captures all DML and DDL, near‑real‑time, scales to high throughput.
- **Cons:** requires additional infrastructure (Kafka, connectors), logical replication must be enabled, higher setup complexity.
- **Best for:** production‑grade pipelines needing reliable, low‑latency sync.

## Comparison table

| Aspect                | Timestamp | Trigger | Log‑based |
|-----------------------|-----------|---------|-----------|
| Deletes captured     | No (needs soft‑delete) | Yes | Yes |
| OLTP impact           | Query load | Extra writes per transaction | None |
| Latency               | Minutes   | Seconds | Seconds |
| Setup complexity      | Low       | Medium  | High |
| DDL changes visible   | No        | No      | Yes |
| Scale ceiling         | Medium    | Medium  | High |
| Typical tools         | Any SQL client | DB‑native triggers | Debezium, Fivetran, Kafka, etc. |

## CDC with Slowly Changing Dimensions (SCD)
- CDC feeds change events directly into SCD Type‑2 processes.
- Example workflow with log‑based CDC:
  1. Debezium emits an update event (e.g., customer moves to a new city).
  2. ETL marks the existing dimension row as expired (`valid_to = today`, `is_current = false`).
  3. ETL inserts a new row for the updated version (`valid_from = today`, `is_current = true`).
- Eliminates nightly full‑table scans; changes arrive within seconds.

## Takeaway
- Copying millions of rows to move a few thousand changes is inefficient.
- Choose the CDC method that matches your workload and operational constraints.
- For most production environments, log‑based CDC provides the most reliable, scalable solution despite its higher initial effort.
