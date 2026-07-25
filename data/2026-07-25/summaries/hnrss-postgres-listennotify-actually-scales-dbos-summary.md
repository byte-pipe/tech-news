---
title: Postgres LISTEN/NOTIFY Actually Scales | DBOS
url: https://www.dbos.dev/blog/postgres-listen-notify-scalability
date: 2026-07-24
site: hnrss
model: llama3.2:1b
summarized_at: 2026-07-25T11:35:35.044578
---

# Postgres LISTEN/NOTIFY Actually Scales | DBOS

Postgres LISTEN/NOTIFY actually has a bad reputation due to perceived lack of scalability, but its limitations can be addressed with optimization and understanding of the underlying mechanism.

### Key Points:

*.POSTgres LISTEN/NOTIFY is a powerful tool for low-latency notifications, streams, and pub/sub in Postgres.
* The primary issue is not not scaling, but rather "unintuitive behavior" of NOTIFY's performance characteristics due to global locks.
* Optimization techniques have been demonstrated to achieve 60K writes per second with millisecond-scale latency on a single Postgres server.

### Low-Latency Streaming with LISTEN/NOTIFY

* The basic design of Stream creation and write is as follows: 
 + Create a streams table where each stream chunk (e.g., an LLM response token).
 + Write to streams by inserting into the table.
* Reading from the stream poses the issue with polling: finding the next chunk arrival.

### Polling Approach

* Proposed solution: use LISTEN/NOTIFY's ability to block waiting for a notification.
+ Readers wait for notifications and wake up immediately after new stream chunks arrive.

### The LISTEN/NOTIFY Exclusive Lock

* Underlying mechanism: Postgres takes a global exclusive lock during NOTIFY commit, ensuring transaction ordering.
* This lock is necessary due to notifications in transaction commit order to enforce guarantees of Postgres security mechanisms (e.g., locking and write ordering).
* However, it can significantly impact the database's performance if left unoptimized.

### Optimizing LISTEN/NOTIFY Performance

Recent initiatives have shown that optimizing this issue requires careful approach:

* Use transactions with smaller "warming-up" periods to avoid long lock durations.
* Employ techniques like LAG-based scheduling for stream chunks read during a single commit interval (as opposed to polling), or implementing the trigger solution that allows readers wait while listening for notifications without wasting resources to poll.

Overall, Postgres LISTEN/NOTIFY is not inherently scalable when relying on global locks. Nevertheless, by mastering its specific performance characteristics and designing smart optimizations, one can achieve remarkable high throughput for this highly concurrent and real-time system.