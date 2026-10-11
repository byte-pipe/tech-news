---
title: "Atlas Infinite: MongoDB's Disaggregated Architecture"
url: https://muratbuffalo.blogspot.com/2026/10/atlas-infinite-mongodbs-disaggregated.html
date: 2026-10-11
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-11T13:39:22.225274
---

# Atlas Infinite: MongoDB's Disaggregated Architecture

# Atlas Infinite: MongoDB's Disaggregated Architecture

## Overview
- Atlas Infinite entered public preview on September 29 with MongoDB 9.0, introducing compute‑storage disaggregation while preserving WiredTiger performance and ensuring storage never sees unencrypted customer data.  
- The summary follows the high‑level description from the MongoDB Engineering blog post by Abhishek Chauhan.

## Why Disaggregation Now
- MongoDB historically relied on sharding for horizontal scaling, so it did not need disaggregation to overcome single‑node limits.  
- Modern workloads face **storage gravity**: in a three‑node replica set each node stores a full copy, making storage expansion, replica addition, or backup restoration time‑consuming on large clusters.  
- Customers want compute and storage to scale independently, to avoid paying for unused resources and to enable cheap snapshots, clones, and branches of production data.

## How MongoDB Differs from Traditional Designs
- Traditional disaggregated systems make storage “smart”: a log service records every page change, and page servers rebuild pages on demand, requiring storage to read unencrypted data.  
- MongoDB’s approach keeps storage **blind** to user data, preserving WiredTiger’s checkpoint‑based batching and avoiding the need for a canonical page image.  
- By owning the engine, server, and cloud service, MongoDB could co‑design compute, log, page, and object layers to meet performance and security goals.

## Architectural Components
1. **Compute Layer** (primary, hot standby, optional read replicas)  
   - Executes queries and transactions.  
   - Holds only caches and recent changes; all state can be rebuilt from storage if a node fails.  

2. **Shared Storage Layer** (written in Rust)  
   - **Log Service**: provides consensus on the logical oplog; durability is achieved when the oplog is replicated across three zones.  
   - **Page Service**: spreads each tenant’s pages across many servers; receives physical page deltas (phylog) from WiredTiger at checkpoint time and materializes pages.  
   - **Object Storage & Object Index Service**: stores long‑term durable copies of data.

## Key Design Differences
- **Two‑log model**:  
  - *Logical oplog* for durability and replication (critical path).  
  - *Physical phylog* of page deltas emitted only at checkpoints, allowing WiredTiger to batch writes.  

- **End‑to‑end encryption**:  
  - Data is encrypted on the compute node before leaving it; decryption occurs only on the compute side with customer‑controlled keys.  
  - Storage never sees documents, collection names, indexes, or tenant boundaries, protecting against insider or breach threats.  

- **Replica freshness without page‑level logging**:  
  - Pages advance only at checkpoints, so a replica that reads only shared pages may lag by seconds.  
  - The compute node applies the oplog to a local ingest table; reads combine this with checkpoint‑consistent pages, achieving millisecond replica lag while retaining checkpoint batching.

## Availability and Recovery
- Each cluster includes a hot standby for rapid primary failover.  
- Data exists simultaneously in three forms: replicated oplog, page servers, and object storage.  
- The fleet is partitioned into isolated cells, preventing cascading failures, and recovery is parallelized across many machines rather than relying on a single node.

## Takeaway
Atlas Infinite delivers a purpose‑built disaggregated architecture that lets customers scale compute and storage independently, maintains WiredTiger’s high performance through checkpoint‑based batching, and enforces strong security by keeping storage blind to unencrypted data. This design addresses the operational bottlenecks of large‑scale clusters while providing fast replica recovery and robust availability.