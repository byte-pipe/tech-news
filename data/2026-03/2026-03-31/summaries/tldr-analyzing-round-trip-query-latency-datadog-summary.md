---
title: Analyzing round trip query latency | Datadog
url: https://www.datadoghq.com/blog/analyzing-roundtrip-query-latency/
date: 2026-03-31
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-31T01:04:02.287217
---

# Analyzing round trip query latency | Datadog

# Analyzing round trip query latency | Datadog

## Overview
- Query timeouts often occur even when database metrics look normal.  
- Latency can stem from any hop between the application and the database (connection pools, load balancers, proxies).  
- Datadog’s correlated APM and Database Monitoring (DBM) data allow decomposition of round‑trip latency to pinpoint the source.

## Round‑trip latency vs. database time
- **Round‑trip latency** = total time from query issuance to response receipt, including network, proxies, and connection‑pool overhead.  
- **Database time** = time the database engine spends executing the query; excludes transport and decoding.  
- Many monitoring tools only see inside the database, missing external bottlenecks.

## Decomposing latency
- Visualize latency as a parent span (full query) with two child spans:  
  1. **Database execution**  
  2. **Everything else** (connection pool, proxy, network).  
- First step: determine which side dominates.  
  - If database time dominates → query optimization or scaling.  
  - If “everything else” dominates → investigate upstream components.

## Round‑trip overhead analysis view
- Shows a single metric **Round Trip Overhead** = round‑trip time ÷ database time.  
- Larger values indicate more time spent outside the database (e.g., 10× or 100× for highly optimized queries).  
- The view also breaks down the individual components for deeper inspection.

## Example: Under‑provisioned PgBouncer pool
1. PgBouncer sits in front of a PostgreSQL instance.  
2. Timeouts appear; the overhead view shows increased round‑trip time while database time stays flat.  
3. Diagnosis: PgBouncer host CPU saturation slows its single‑threaded event loop.  
4. Remedy: add another PgBouncer instance and a load balancer, avoiding unnecessary query‑level tuning.

## How Datadog links APM and DBM
- **APM tracer** (in application code) measures full round‑trip time, capturing all intermediate hops.  
- **Database Monitoring** reads database‑internal metrics (e.g., `pg_stat_statements.total_exec_time`) that stop timing once the DB finishes execution.  
- Comparing these distinct timeframes prevents mis‑attributing latency to the wrong layer.

## Takeaway
- Treat query latency as a composite metric, not a single number.  
- Use Datadog’s combined APM and DBM data to separate database execution from transport/processing overhead.  
- This approach quickly identifies whether to focus on query optimization, database scaling, or upstream infrastructure.

## Next steps
- Sign up for a 14‑day free trial of Datadog to apply the round‑trip overhead analysis in your environment.