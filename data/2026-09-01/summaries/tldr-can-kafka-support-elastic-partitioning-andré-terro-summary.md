---
title: Can Kafka Support Elastic Partitioning? – André Terroir
url: https://terroir.systems/can-kafka-support-elastic-partitioning/
date: 2026-09-01
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-01T09:51:00.347743
---

# Can Kafka Support Elastic Partitioning? – André Terroir

# Can Kafka Support Elastic Partitioning?

## The Promise of Dynamic Partitioning
- Static partitioning in Kafka causes trade‑offs:  
  - Changing partition count breaks ordering guarantees.  
  - Over‑partitioning adds per‑partition overhead and smaller batches.  
  - Under‑partitioning limits parallelism when load grows.  
- Load imbalance appears as hot keys and partition skew, leading to uneven broker/consumer utilization.  
- Publisher‑consumer coupling forces the same partition layout for ingestion and processing, restricting granularity of reprocessing and causing head‑of‑line blocking.  
- Modern databases auto‑scale partitions, suggesting Kafka could benefit from a similar dynamic approach, even if it means giving up strict per‑partition ordering in favor of per‑key ordering.

## Dynamic Producer and Consumer Model
- **Producers:**  
  - A key is always owned by a single leader broker, preserving ordering per key.  
  - When partitions split/merge, brokers reach consensus (via Raft) and inform clients of the new layout.  
  - Using hash‑based ranges enables fine‑grained distribution based on throughput, node load, and capacity, handling skewed key spaces.  
- **Consumers:**  
  - Stateless consumers need ordered processing per key; stateful consumers also need locality (the node that holds the key’s state must process its records).  
  - Split/merged partitions form a DAG; parent partitions must be consumed before child partitions to keep ordering, causing temporary throughput dips during layout changes.  
  - Relocating state for moved keys is complex and expensive; it essentially requires a stream‑processing framework that manages state migration.  
  - Existing Kafka Streams solves locality with compacted changelog topics and standby replicas, but dynamic layout changes would require processing historic changelogs from multiple old partitions, increasing overhead.

## Client‑Assigned Partitions and Batching
- Kafka deliberately lets clients decide the target partition for each record, which yields several efficiency gains:  
  - **Batch‑oriented processing:** Brokers store and serve opaque batches without inspecting individual records, giving orders‑of‑magnitude lower overhead.  
  - **Direct producer‑to‑broker transmission:** No extra routing step is needed.  
  - **End‑to‑end compression:** Compression work stays on the client side, reducing broker CPU load.  
  - **Zero‑copy I/O:** Stored batches are sent to the network via `sendfile`, avoiding user‑space copies.  
  - **Page‑cache reads:** Consumers read the exact on‑disk format, allowing cache hits and efficient fan‑out to many consumers.  
- To keep these benefits, producers must be notified of partition‑layout changes, pause briefly, and re‑partition any in‑flight buffered data. Apart from this brief disruption, dynamic partitioning is compatible with Kafka’s batch‑centric design.

## Do We Need Partitions?
- The discussion so far assumes we only modify how data is distributed among existing partitions.  
- The article hints at questioning whether the partition abstraction itself is necessary when dynamic, key‑based routing and batching are already in place, but the argument is left unfinished.