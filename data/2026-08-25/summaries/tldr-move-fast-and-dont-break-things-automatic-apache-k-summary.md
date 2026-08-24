---
title: Move Fast And Don’t Break Things: Automatic Apache Kafka® Migrations With Orbit - WarpStream
url: https://www.warpstream.com/blog/orbit-kafka-auto-migration
date: 2026-08-25
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-25T06:05:23.488973
---

# Move Fast And Don’t Break Things: Automatic Apache Kafka® Migrations With Orbit - WarpStream

# Move Fast And Don’t Break Things: Automatic Apache Kafka® Migrations With Orbit - WarpStream

## Context and Challenges
- WarpStream provides a drop‑in Kafka replacement built on object storage, aiming for lower cost and simpler operations.  
- Migrating an existing Kafka cluster involves three parts: data, consumer offsets, and producers.  
- Data and consumer offsets are automatically replicated by Orbit, but moving producers has traditionally required a manual, coordinated downtime.

## What Orbit Already Solves
- Orbit continuously replicates topic data and consumer group offsets from any source Kafka cluster to WarpStream, preserving exact offsets.  
- Consumers can switch their bootstrap URL to WarpStream and resume processing without reprocessing, skipped records, or a shared cut‑over window.

## Difficulties with Manual Producer Migration
- The manual four‑step process (stop producers, wait for replication lag = 0, disable replication, restart producers) caused downtime and required all teams to move together.  
- Custom scripts, feature‑flag tricks, and ACL signals were ad‑hoc and not scalable across languages or teams.  
- Providing language‑specific “fat clients” was impractical for large enterprises.

## Orbit Auto Migration – Proxy‑Based Solution
- A lightweight proxy is built into each WarpStream Agent; it forwards Produce requests to the source Kafka cluster.  
- Teams update their bootstrap URLs to point to WarpStream early; agents forward writes until the migration is triggered.  
- Migration is initiated with a single UI button, automating the previous manual steps without operator intervention.

## Automated Migration Workflow
1. **Block producer traffic** – agents temporarily reject Produce requests; producers buffer and retry.  
2. **Wait for replication lag to reach zero** – ensures source and WarpStream copies are identical.  
3. **Sever the Orbit replication link** – source cluster no longer needed for the topic.  
4. **Unblock traffic** – agents accept Produce requests directly, completing the cut‑over.

## Topic State Machine
- **REJECT** – initial state; WarpStream rejects direct produces to keep the copy identical to the source.  
- **PROXY** – producers point to WarpStream; agents forward all Produce requests to the source cluster while replication continues.  
- **MIGRATING** – agents block traffic, wait for lag = 0, and cut the replication link.  
- **COMPLETE** – agents accept writes directly; the topic is fully migrated.

## Benefits
- Zero downtime and no restarts for producers.  
- No global maintenance window; each team migrates at its own pace.  
- Centralized control provides safe cut‑over, abort, and rollback capabilities.  
- Stateless agents mean any agent can handle any producer; no dedicated proxy tier is required.

## Operational Visibility
- The WarpStream UI displays migration status per topic (e.g., “produce paused”, “migration complete”).  
- Operators can monitor, abort, or roll back migrations at any stage, ensuring a transparent and controllable process.