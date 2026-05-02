---
title: Benchmarking How Workflow Execution Scales on Postgres | DBOS
url: https://www.dbos.dev/blog/benchmarking-workflow-execution-scalability-on-postgres
site_name: tldr
content_file: tldr-benchmarking-how-workflow-execution-scales-on-post
fetched_at: '2026-05-02T11:43:36.111444'
original_url: https://www.dbos.dev/blog/benchmarking-workflow-execution-scalability-on-postgres
date: '2026-05-02'
description: Benchmarking the workflow execution and workflow queueing scalability of a single Postgres server.
tags:
- tldr
---

When building adurable workflow execution system on Postgres, one of the most common questions we get is “does Postgres scale?” There are plenty of posts from top tech teams asserting thatPostgresdoes scale, but not all showhowits performance scales in practice.

In this blog post, we benchmark the scalability of a single Postgres server. We focus on the performance of Postgres writes as those are the bottleneck in workflow execution: a durable workflow has to write to the database multiple times to checkpoint its inputs, its outcome, and the outcome of each of its steps. First, we measure raw Postgres write throughput in a vacuum. Then we analyze the performance of two durable workflow workloads: one that starts workflows locally, and one that uses a Postgres-backed queue.

We find that Postgres scales even better than we expected: a single server can support a sustained throughput of 144K writes per second, or process 43K workflows per second. That translates to 12 billion writes or 4 billion workflows per day, more than enough for most use cases.

All benchmark code is open-sourcehere. All experiments were conducted on an AWS RDS db.m7i.24xlarge instance with 96 vCPUs, 384 GB of RAM, and 120K provisioned IOPS on an io2 volume.

### Postgres Point Write Performance

We first measure the maximum write throughput Postgres can sustain to a single table. We use a simple three-column table with a UUIDv7 primary key, a TEXT data field, and a timestamp:

Then we benchmark how many rows we can insert per second from a large number of async Python clients. Each row is inserted in a separate transaction:

Overall, we find a Postgres server can handle up to 144K of these writes per second. That’s a lot, equivalent to 12 billion writes per day.

To make sure we’re reaching the limits of Postgres scalability, we also analyzed the bottleneck that constrains further performance. We first checked top-line metrics like CPU and IOPS, but found they weren’t fully utilized. To find the real bottleneck, we then queried the built-in Postgrespg_stat_activitytable to inspect what each Postgres backend process was doing at each moment in time:

We found that the bottleneck was in flushing the Postgreswrite-ahead log (WAL)to disk. When performing a write, Postgres never directly modifies data pages on disk. Instead, it first appends a description of the write to the WAL, then flushes the WAL to disk (using thefsyncsystem call), then acknowledges the commit to the client. The actual data files are updated later in the background. This design maximizes performance as only the relatively cheap WAL write is done synchronously, while the more expensive disk updates are done in the background.

When looking at Postgres process activity, we found that at any point in time, exactly one process was flushing the WAL to disk (in agroup commit, so flushing the entire buffer, including data from other processes) and the vast majority of other processes were waiting on the WAL lock for their data to be flushed. The bottleneck in performance was how quickly Postgres could commit write transactions by flushing their WAL entries to disk. This is acommonly observed bottleneckfor extremely write-intensive workloads, as Postgres only has one WAL and every write needs to go through it.

### Durable Workflow Performance

We next measure the performance of Postgres-backed durable workflows. A durable workflow performs exactly two Postgres writes:

* One when it starts to create its database entry and record its inputs and initial status
* One when it completes to record its outcome and final status

If a workflow has steps, it also performs one write per step to checkpoint that step’s outcome.

In this benchmark, we evaluate simple no-op workflows with no steps:

We start many workflows concurrently from many async Python clients:

Overall, we find a single Postgres server can process up to 43K workflows per second. In other words, adding Postgres-backed durability to an application executing 43K workflows per second will not bottleneck its performance:

Like in the previous benchmark, we next looked for the bottleneck constraining further performance. Again, we found the bottleneck was in the WAL: how quickly Postgres could commit workflow INSERTs and UPDATEs by flushing their WAL entries to disk. This is unsurprising as both workloads are completely write-dominated. Two factors explain the difference between raw Postgres INSERT performance and workflow performance:

1. A workflow requires two writes, so 43K workflows per second is actually 86K Postgres writes per second.
2. The workflow_status table is much larger than the simple write benchmark table (31 columns versus 3, 9 indexes versus 1), so updates to that table require flushing much more data.

### Durable Queues Performance

We next measure the scalability of Postgres-backed queues. This is similar to the previous benchmark, but instead of directly executing workflows, clients enqueue them onto a Postgres queue. Workers then dequeue and execute them. This requires four Postgres writes per workflow:

* One write to enqueue the workflow, creating its database entry and recording its inputs and initial status
* One write to dequeue the workflow, updating its status (this write is batched with all other workflows dequeued by the same executor at the same time)
* One write when the dequeued workflow is started, updating its status
* One write when the workflow completes, recording its outcome and final status

Overall, we find a single Postgres server can process up to 12.1K queued workflows per second:

Again, we looked for the bottleneck in performance. Interestingly, the bottleneck this time was not in the WAL, but in lock contention in the workflow_status table. All client processes were enqueueing to or dequeueing from the same few rows at the head of the queue, and contention between them limited performance (despite optimizations like SKIP LOCKED). We hypothesize that this problem is exacerbated by Python being a relatively inefficient language, so many clients are needed to saturate Postgres–a faster language like Go would require fewer clients, and thus introduce less dequeue contention.

To eliminate the contention bottleneck, we also test distributing work across multiple queues (or, equivalently, multiple partitions of the same queue). We find that maximum achievable workflow throughput increases with the number of queues (with diminishing returns).Ultimately, with enough queues or partitions, queued workflows achieve a throughput of 30.6K workflows/sec. This is about two-thirds of the 43K workflows per second achieved when directly starting workflows, which makes sense as queued workflows require more writes (three non-batched and one batched versus two non-batched). At that scale, the database bottleneck again shifts to the WAL.

Overall, this benchmark shows that Postgres scales impressively well. In one second, a single Postgres server can perform 144K small writes or process 43K durable workflows. That translates to 12 billion writes or 4 billion workflows per day, enough for most applications. For more performance, a workload can shard across multiple Postgres servers to handle almost any load.

### Learn More

If you like building scalable, reliable systems, we’d love to hear from you. At DBOS, our goal is to make durable workflows as simple and performant as possible. Check it out:

* Quickstart:https://docs.dbos.dev/quickstart
* GitHub:https://github.com/dbos-inc
* Discord community:https://discord.gg/eMUHrvbu67