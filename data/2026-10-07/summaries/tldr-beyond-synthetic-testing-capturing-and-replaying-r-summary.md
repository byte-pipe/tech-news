---
title: Beyond synthetic testing: Capturing and replaying real database workloads at Airbnb | Airbnb Engineering & Data Science
url: https://airbnb.tech/infrastructure/beyond-synthetic-testing-capturing-and-replaying-real-database-workloads-at-airbnb
date: 2026-10-07
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-07T06:01:18.106167
---

# Beyond synthetic testing: Capturing and replaying real database workloads at Airbnb | Airbnb Engineering & Data Science

# Beyond synthetic testing: Capturing and replaying real database workloads at Airbnb

## Introduction
- Airbnb relies on hundreds of MySQL‑compatible clusters handling millions of queries per second.  
- Scaling these databases requires accurate sizing, safe upgrades, and the ability to reproduce production incidents.  
- The article describes a unified system that captures live traffic and replays it offline for load‑testing, capacity planning, and risk mitigation.

## Challenges and motivation
- **Fragmented legacy solution**: each language client logged queries to Kafka, leading to high maintenance, poor scalability, and incomplete transaction information.  
- **Goals of the new system**  
  - Load‑test with authentic production traffic to right‑size clusters.  
  - Verify query compatibility across version upgrades or migrations by comparing results on different targets.  
  - Enable detailed performance debugging by replaying full SQL statements within their transactional context.  
- Required a single, client‑agnostic capture point without code changes; ProxySQL, the existing MySQL wire‑protocol proxy, was chosen.

## System architecture overview
- Three in‑house components: **Log Mover**, **Log Processor**, and **Log Replayer**.  
- Traffic flows through ProxySQL, which logs queries per‑cluster via configurable query rules.  
- Security: logs are encrypted in transit and at rest, access follows least‑privilege, and replays run only in production‑equivalent environments.

## Log Mover
- Deployed as a sidecar to each ProxySQL instance.  
- Monitors ProxySQL’s local binary log files and streams them to cloud object storage, preventing disk overflow.  
- Enables selective logging for a specific cluster during a defined test window.

## Log Processor
- Runs as an offline job that transforms raw logs into replayable datasets per cluster.  
- **Key processing steps**  
  - **Parsing, grouping, ordering**: decodes binary logs, separates queries by backend cluster, and reassembles statements to preserve original transaction order.  
  - **Timestamp‑based bucketing**: splits processed logs into five‑minute windows, allowing fine‑grained control of replay pace and throughput.  
  - **Metadata enrichment**: attaches timestamp, username, cluster, and schema information for easy lookup.  
  - **Query rewriting**: rewrites `INSERT` statements to embed the captured `last_insert_id`, ensuring deterministic behavior across databases that handle auto‑increment differently. This trade‑off sacrifices testing of native auto‑increment generation but eliminates false incompatibility signals.

## Log Replayer
- Users launch replay jobs via a web UI, specifying source cluster, time range, target endpoints, and replay mode.  
- Architecture consists of an API Server (control plane), a Replay Task Scheduler, and worker executors that stream the bucketed queries to the target databases at the desired rate.  
- Supports two replay modes (not detailed in the excerpt) to accommodate different testing scenarios.

## Outcomes
- Provides a reliable, production‑traffic‑driven load‑testing framework.  
- Detects subtle incompatibilities before migrations, reducing downtime risk.  
- Facilitates offline incident investigation and validation of fixes with full transactional context.  
- Centralizes capture and replay, eliminating the maintenance burden of language‑specific logging solutions.