---
title: Can Kafka Support Elastic Partitioning? – André Terroir
url: https://terroir.systems/can-kafka-support-elastic-partitioning/
site_name: tldr
content_file: tldr-can-kafka-support-elastic-partitioning-andré-terro
fetched_at: '2026-09-01T09:50:44.645993'
original_url: https://terroir.systems/can-kafka-support-elastic-partitioning/
date: '2026-09-01'
description: The Promise of Dynamic Partitioning Partitioning is a recurring challenge around building systems on top of Apache Kafka distributed message log. Some com...
tags:
- tldr
---

# Can Kafka Support Elastic Partitioning?

28 Aug, 2026

## The Promise of Dynamic Partitioning

Partitioning is a recurring challenge around building systems on top of Apache Kafka distributed message log. Some common issues are:

* The static partitioning model — changing the number of partitions and assignment of messages1to partitions is complicated as it leads to losing the ordering guarantees2. This leaves engineers with a bad trade-off. Over-partition and pay the cost of lower efficiency due to per-partition overhead and smaller batches. Under-partition and limit the ability to scale parallel processing as the load varies or grows over time.
* Imbalanced load — hot keys and partition skew result in uneven distribution of work across brokers and consumers. All consumers should be equally resourced to not fall behind or be under-utilized.
* Coupling of publishers and consumers — the maximum parallelism is limited by the number of partitions, which also determines the granularity of reprocessing, and the data batched together. Partitioning is the same for ingesting and processing data, even though these might be very different applications with different architectures.
* Message replay granularity — reprocessing records for a single key is not possible without reading the whole partition. A related problem is head-of-the-line blocking — a single non-processable record would stall consumption of a partition.

In 2026, these limitations might seem odd — with many modern databases, for example, determining the number of partitions and distributing the data between them is done automatically based on load.

These problems seemingly suggest a solution — dynamically managing partitioning of the data based on volume and load. If we extend the idea to allow for a different partition layout for consumers, then we could achieve decoupling and distribution of work across asymmetric, differently resourced consumers (e.g. spot nodes). There is a cost to pay — foregoing the per-partition ordering guarantee. However, one can argue, that what applications really care about is ordering of recordsper key. After all, different keys are assigned to a particular partition arbitrarily based on the key hash value and are otherwise unrelated.

Let's look at how the idea affects write (producer) and read (consumer) paths. First we explore the model of a partitioned distributed message log in the abstract and then consider the implications of the design for the implementation of Kafka.

## Dynamic Producer and Consumer Model

Maintaining key ordering for producers is rather straightforward: at any point in time a key must be assigned to exactly one leader broker, which establishes ordering. When partitions are split or merged, the brokers have to agree on the new data distribution, which is achieved via consensus (Kafka relies on Raft) and communicated to the clients. In a steady state brokers process published records for their owned partitions independently, each backed by its own set of replicas. Partitioning keys into ranges allows distributing data granularly among brokers — down to individual keys — based on the actual partition throughput, node load and capacity. By using key hashes, rather than keys directly, to define ranges we get even distribution also for skewed workloads biased to a particular part of the key-space.

Consumers are where things get interesting. Stateless consumers require that records for a given key are processed in order. For example, imagine calculating spending statistics for a user's transactions and updating them in a central storage. Stateful consumers additionally require locality — each record must be processed by the node that holds the state for its key. Imagine a partitioned cache built off a message log or a stateful stream processor that performs time-based aggregation.

The partitions that were merged or split are connected by a parent-child relationship and form a directed acyclic graph (DAG). To maintain ordering and avoid concurrent processing of reassigned keys, records from parent partitions must be processed before any records from child partitions. This could be disruptive and lead to temporarily reduced throughput during partition layout changes. Importantly, only the split/merged partitions are affected, making it acceptable, given relatively infrequent changes.

Locality is harder to achieve, as it requires moving the state, associated with relocated keys, to the new owner consumer. This is possible, of course, but the process is complex and expensive. Most importantly, the state is application-specific — taking this responsibility away would mean building a stream processing framework that would take care of managing state.

The problem of locality already arises with Kafka's static partitioning model when a partition is reassigned to a different consumer due to a failure or rebalancing. Kafka Streams solves it by using a compacted changelog topic to be able to rebuild local state quickly on a new node. Nevertheless, rebuilding of the state can still take considerable time, stalling processing. Standby replicas keep a copy of the state updated continuously, avoiding the need for recovery.3

One can imagine the same approach to be employed for redistributing state whenever the partitioning layout changes. It'll be harder to achieve the same efficiency, however. A consumer would have to process historical changelogs from all partitions that the keys from its owned range belonged to over time, sifting through potentially large amounts of irrelevant data.

## Client Assigned Partitions and Batching

Kafka clients are responsible for assigning messages to partitions. What might seem like an unusual approach at first glance is in fact an important deliberate design decision. Why wouldn't the server distribute the received records across partitions?

However, this is a deliberate design choice that affords Kafka significant efficiency gains4:

* Kafka operates entirely on a batch level. After a client has serialized a batch, brokers need not peek inside to store the data or serve it to consumers. This reduces overhead by multiple orders of magnitude compared to processing records one-by-one. Also, the overhead does not grow linearly with data volume — the higher the throughput, the larger the batch size.
* A message batch is transmitted directly from the producer client to the owning broker, without a need for coordination and routing of the data.
* The fact that a batch is opaque affords end-to-end compression of the data, both in-transit and on storage. The compression/decompression work is offloaded to the client producers/consumers, relieving the brokers of the additional work.
* Because the batches stored on disk are exactly the same data as transmitted over the network, they need not be parsed, allowing Kafka to make use of zero-copy IO. The batches are transmitted directly from disk to the network buffer using thesendfile5system call, without the overhead of copying data across the kernel/user space boundary.
* As the data is consumed in exactly the same form as it's stored on disk, reads make use of the filesystem page cache. This also enables an efficient fan-out to multiple concurrent consumers out of memory. Moreover, if the consumer lag is low, fresh batches fetched by the consumer are likely still in the cache, allowing reads to bypass disk entirely.

To preserve the benefits of end-to-end batching, the producers need to discover the partition layout changes and adjust the way data is partitioned before continuing processing. Each change would briefly disrupt producer progression and require repartitioning of the buffered in-flight data. But otherwise dynamic partitioning and operating at a batch level are not incompatible design choices.

## Do We Need Partitions?

So far, we have only explored the idea of dynamically changing the distribution of data into partitions, which would enable scaling of message ingestion and processing, while balancing load more evenly. However, this is not sufficient for decoupling scaling of producers and consumers, nor does it allow granular processing of messages for individual keys.

What if we do away with partitions altogether?6It's not hard to imagine each individual key getting its own partition. However, it would cost us all the efficiency benefits of batching outlined above. The throughput of individual keys would be simply too low to coalesce multiple records before publishing.

Another cost to pay for foregoing partitions is cheap tracking of consumer progression. Instead of one offset for each of relatively few partitions, an offset has to be stored for each key — in many cases, billions of values. The filesystem storage model will also require rethinking — the proliferation of small files would erase the benefits of sequential disk I/O.

For some applications, the ability to replay messages, isolate processing failures per key, and distribute keys across consumers independently of producer partitioning, might well be worth the cost.

Aren't message queues the solution? Not quite. Queues are a good fit when messages are expensive to process and independent, allowing for flexible distribution across consumers. However, the flip side is that per-message acknowledgements are expensive — reduced efficiency means lower supported throughput and shorter retention time. Messages are typically transient and not persisted long-term. Many message queues lack ordering guarantees. This includes Kafka's support for queues, which enables scaling of consumers beyond the number of partitions7.

While a per-key partitioned message log is a useful abstraction, and an interesting design problem, it involves a very different set of trade-offs than what motivated the design of Kafka.

## A Case Study: AWS Kinesis and Apache Flink

Kinesis is an interesting system to examine in the context of our discussion. It provides a persisted message log with the ordering guarantee per partition (shard), similar to Kafka, while supporting load-based dynamic partitioning8. The server relies on client-assigned partition keys to distribute data using key hash ranges. Kinesis allows partition splits and merges, creating parent-child relationships. The guarantee that records within each partition are processed in order is maintained by requiring the client to fully process parent shards before processing child shards.

Flink enables building stateful distributed stream processors with Kafka and Kinesis as sources. By respecting Kinesis' parent-child relationships when processing shards, the original order of records (events) is retained. Flink's state is partitioned independently of the source — this is the key for decoupling processing from the source data distribution. Messages are reshuffled, based on the state key hash9, into key groups, which are assigned to the task worker maintaining the state. The number of key groups — typically more granular than source shards — is determined by the maximum parallelism (128 by default). We get efficient processing, local with respect to the state, that remains undisrupted by source repartitioning and can be scaled independently.

The state is periodically collected from all workers into an externally persisted checkpoint, which is used to restore local state in the event of failure or rebalancing. For jobs with large state, recovery time could be significant, which disrupts processing, making latency less predictable, and limits how dynamically a Flink job can be scaled. Unlike Kafka Streams, Flink does not make use of standby replicas, which could take over without performing recovery or moving data.

While data reshuffling is not free and snapshot-based state management has its set of trade-offs, they do allow relieving the application of the burden of managing distributed state.

## Dynamic Partitioning in Databases

Distributed databases are constructed around a write-ahead (message) log (WAL), from which the materialized views and indexes of data are derived. They partition the data and replicate it across nodes for scaling, fault tolerance, and performance. There are many parallels between the problems that arise in databases and stateful stream processing systems. Dynamically managing data partitioning is one such problem. Let's explore briefly how databases solve it.

Range-based partitioning enables range queries and supports granular data distribution based on volume. In key-value stores, which do not support range queries, hashing key values allows distributing skewed workloads — such as time-based or sequential keys — more evenly. Consistent hashing is a simple approach that works well for evenly distributed data, while hash ranges allow for more granular and adaptive control over partitioning.

Most distributed SQL databases use range-based partitioning. This includes Amazon Aurora DSQL with range-based shards10. Google Spanner uses range-based splits, divided based on load down to a single row11, and allows manual control of split points12. CockroachDB starts from a single range and splits ranges upon reaching a preconfigured size[^cockroachdb-distribution] ("partition" in CockroachDB refers to higher-level geo-distribution and tiered archival storage of data13, unrelated to our discussion).

NoSQL and key-value stores generally rely on hash-based partitioning. Amazon DynamoDB distributes data by assigning partition key hash ranges to shards (partitions)14, which have fixed throughput and storage capacity. Reaching these limits triggers table repartitioning when reached15. Azure Cosmos DB distinguishes logical (one for each key value) and physical (mapped to key hash ranges) partitions — both are subject to an upper capacity limit16, with physical partitions determining available throughput. With hierarchical partition keys, Cosmos DB tracks on which partitions the data for a key prefix resides and collocates records. This enables scaling data distribution across multiple partitions, efficient cross-partition prefix queries, and tenant isolation.17

Repartitioning requires moving the data in the background, typically involving snapshot copying, log replay, and handover of ownership between partition leaders via consensus18. The mechanism is similar to rebalancing data when nodes join or leave a cluster. The process is transparent to clients but can take hours to complete19— data movement is throttled to avoid interference with ongoing requests served by the database.

## Can We Have it All? Virtual Partitions

So far, we've explored how dynamic partitioning could be adopted in a Kafka-like distributed message log, while preserving the strong per-key ordering guarantees and the efficiencies of end-to-end batching. We also considered what it would mean to eliminate partitions entirely and what it would cost. One limitation we haven't managed to address yet is the coupling of producers and consumers.

The structure of the Kafka message log — the number of partitions and the data batched together — is determined entirely by the producer. The number of partitions (P) is the upper boundary on the consumer parallelism (C): to maintain ordering, each partition is processed by a single consumer thread. Only whenPis divisible byCis the work distributed evenly; all other configurations will result in imbalanced load20. The largerP, the less imbalance — but also the smaller producer batches, and hence the lower efficiency, given the same batching interval.

Kafka's support for efficient fan-out suggests a solution: a serving layer that pulls the original log data and re-distributes it into virtual partitions, to match the optimal consumer parallelism. Serving nodes do not need to store a copy of the log, and would only persist metadata, like consumer progression offsets. Persistent and virtual partitions are mappedN×M, relying on range statistics to maintain even data distribution. Serving nodes can merge log partitions efficiently by preserving original batches — the per-key ordering is still maintained. Splitting log partitions is more expensive — the cost of parsing individual batch records has to be paid — but the work is isolated from storage brokers, and enables scaling of consumers beyond the number of partitions.

## Decoupled Serving

The two-layer architecture gives us optionality. Records can be shuffled across many granular virtual partitions, redistributed across a changing number of consumers, similarly to the approach taken by Flink. Or the number of virtual partitions can be fixed as the number of publisher partitions changes. Finally, embracing the idea of dynamic partitioning fully, the number of virtual partitions can be adjusted to the optimal number to match the number of consumer threads. The model allows for optimizing write and read paths separately.

Decoupling opens many possibilities to explore. The workload for providing a queue interface to the message log can be shifted away from the storage broker — with Kafka queues, the broker needs to wear the hat of a queue coordinator alongside its other responsibilities. Topic compaction can be moved away from the storage broker as well21. The architecture maps well to disaggregated storage — the serving layer can consume immutable log segments off storage, bypassing brokers. To enable per-key replay of message history, the serving layer can implement indexing and store records in a different data structure, such as an LSM tree. Different serving models don't need to be collocated and can be implemented by different systems. This would mean operating multiple different node types, but each simpler and with fewer responsibilities. Such an architecture isolates failures and enables independent optimization.

One can also imagine a system that would provide Kafka-compatible producer and consumer APIs, allowing independent migration of multiple integrations, while offering the benefits of dynamic data distribution to the client applications that adopt the new APIs.

## Partitioning in Contemporary Message Logs

It would be surprising if the ideas presented here had not been explored before. Indeed, a few practical systems recently adopted some aspects of the design discussed above.

In 2025, LinkedIn, where Kafka was created, announced Northguard, a new log storage system underway to replace it. It's not a surprise that Northguard uses a dynamic, range-based sharding approach instead of static, indexed partitions. An interesting detail is that ranges (partitions) are constrained by a binary buddy system in which splits divide a key space in half and merges can only coalesce previously split ranges. This means that partition boundaries are the same for different topics, enabling efficient cross-stream joins without reshuffling data. Another interesting approach is log striping: the unit of replication is a segment — a consecutive chunk of a log — rather than a partition, as in Kafka, which makes it possible to balance the load at a more granular level without moving data while maintaining high availability. When a new broker node joins a cluster, it can become a replica for new segments of existing partitions, immediately expanding the cluster's throughput and storage capacity. When nodes are lost, the active segments currently being appended to can be replicated quickly to different brokers, allowing the log to remain writable without sacrificing durability or consistency. Alongside Northguard, Xinfra was announced, an internal LinkedIn system which provides a pub/sub service abstracted over different brokers and multiple clusters and enabling migration from Kafka to Northguard. Xinfra can be seen as a realization of a decoupled serving layer idea, which abstracts over partitioning model for both consumers and producers and provides API compatibility layer.

Apache Pulsar's scalable topics2223(to be released later in 2026) distribute data into partitions (segments) using key hash ranges dynamically based on producer and consumer throughput while maintaining ordering (an unordered queue consumer model is also supported). Pulsar allows the number of consumers to exceed the number of partitions messages using key-based consumer message assignment (Key_Shared subscription type). Currently this costs producer batching24, but with scalable topics brokers will be able to redistribute messages within a batch. Pulsar's architecture decouples storage, delegated to Apache BookKeeper, allowing the broker, which serves both producers and consumers, to remain stateless. Pravega is another system (inactive as of August 2026) that implements dynamic range-based partitioning of a single message log25, which served as an inspiration for Pulsar's scalable topics.

## Wrapping Up

If we accept total order per-key as the guarantee, the model of dynamic partitioning is compatible with the semantics of a Kafka-like message log, but would require rethinking how partitions are modeled to track lineage as the partition layout changes. The producer protocol has to be restricted to enforce message assignment according to dynamically changing partition key space. The consumer processing must respect the ordering constraints imposed by the partition lineage DAG. The stateful consumer needs to be redesigned to deal with the movement of local state. Achieving scalability and elasticity imposes an efficiency cost in comparison to the simplicity of Kafka's statically partitioned batch-oriented log storage. Even if data distribution layout changes dynamically, tight coupling of producers and consumers remains a concern that could be addressed with virtual partitions. Decoupling the consumer layer unlocks support for alternative consumer models beyond virtual partitions, such as queues and message indexes.

1. Message, record and event are used as equivalent terms throughout the article.↩
2. When You Increase Kafka Partitions↩
3. Kafka Streams. Architecture↩
4. Apache Kafka. Design. Efficiency↩
5. sendfile(2) — Linux manual page↩
6. What If We Could Rebuild Kafka From Scratch?↩
7. KIP932. Queues for Kafka. Ordering↩
8. Amazon Kinesis Data Streams launches On-demand Advantage for instant throughput increases and streaming at scale↩
9. KeyGroupRangeAssignment↩
10. Dynamo, DynamoDB, and Aurora DSQL↩
11. Google Cloud Spanner. Schemas Overview↩
12. Google Cloud Spanner. Create and Manage Split Points↩
13. CockroachDB. Table Partitioning↩
14. Scaling DynamoDB: How partitions, hot keys, and split for heat impact performance (Part 3: Summary and best practices)↩
15. Partitions and data distribution in DynamoDB↩
16. Partitioning and horizontal scaling in Azure Cosmos DB↩
17. Hierarchical partition keys in Azure Cosmos DB↩
18. CockroachDB. Replication Layer↩
19. Hierarchical partition keys in Azure Cosmos DB↩
20. Highly composite number↩
21. Compaction Cost Signals in High-Volume Event Streams↩
22. Apache Pulsar. Scalable topics↩
23. Apache Pulsar. PIP-460: Scalable Topics (Topics v5)↩
24. Apache Pulsar. Subscription Types. Key_Shared↩
25. Pravega. Elastic Streams: Auto Scaling↩