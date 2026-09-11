---
title: 5 Years Running Petabyte-Scale ClickHouse® | Tinybird
url: https://www.tinybird.co/blog/what-i-learned-operating-clickhouse
site_name: hnrss
content_file: hnrss-5-years-running-petabyte-scale-clickhouse-tinybird
fetched_at: '2026-09-11T21:35:50.196533'
original_url: https://www.tinybird.co/blog/what-i-learned-operating-clickhouse
date: '2026-09-07'
description: 'What I learned operating ClickHouse at scale: the wins, the failures, and the lessons that only come from production experience.'
tags:
- hackernews
- hnrss
---

I have been operating a ClickHouse® cluster at Tinybird since version 18.4. That was almost 6 years ago. I wrote my first blog post about how to use ClickHouse® toperform geospatial analysisalmost 8 years ago.

In that time, I've dealt with ClickHouse® daily, helped start a company that uses it, sent critical changes to the database project, and managed many petabyte-scale clusters. This ClickHouse review shares the lessons learned. Setting up a cluster is easy, the hard part is keeping it running. Let me go through the good and the bad parts, focusing on the problems you may find (so you can avoid them).

This ClickHouse review is probably useful for people handling ClickHouse® clusters, but not so much for others.

Important note, mainly for ClickHouse®, Inc lawyers: we have nothing to do with ClickHouse®, Inc. They are the sole maintainers of ClickHouse®, and ClickHouse® is a registered trademark owned by ClickHouse®, Inc. I offer my apologies for any errors contained herein and welcome the opportunity to rectify them promptly. We are merely small contributors ofnew engines,massive performance improvements,distributed joins, and some other things, and, of course, users of the open source version ourselves. I have huge respect for Alexey for starting the project, and for the many people working there.

## Architecture

The architecture ClickHouse® proposes for managing large ClickHouse clusters uses replicas and shards. Basically, you split your data into different buckets (e.g., perhash(user_id)), and every bucket goes to a shard. Then you have different replicas (copies of the data) for each shard.

This is a pretty standard and straightforward architecture, but it's starting to feel like the wrong approach for these kinds of systems. Many people now believe that you have to use cloud storage and separate compute from storage. I don't completely agree, but this approach does offer advantages for cluster management and reduced costs. I'll discuss this in more detail later.

A few years ago, we started with a pretty basic system with no shards, just replicas. We'd scale the replicas vertically to handle larger queries, and we'd add more replicas to handle more traffic. Cloud storage was not an option, so we used local SSD disks (to reduce latency). Adding shards would have been an option if we had to process more data in each query, but we end up not doing it because re-sharding was super hard and none of our customers had that need (well, they did, but if you are smart enough in your data schema design, you can put it off).

That configuration is pretty easy to handle; you add a load balancer in front of all the replicas and route the traffic coming from your app to a replica depending on the request type (I'll talk more about this later). We have an HTTP load balancer with some logic to handle instructions from the backend. So the backend (apps in the diagram) make decisions about where to send a particular request based on load, replica type, consistent hashing (to leverage caches, more on this inStorage), and many more things. I don't think you need all that for a basic install, but you’ll need some of it.

A quick note about HTTP: ClickHouse® offers a TCP connector with a native protocol, but we don't use it. It does not offer many advantages for the type of application we build, and HTTP allows us to use a lot of battle-tested tooling. If you're connecting from application code, you can use language-specific clients likePython, Java, or Go that handle both protocols.

This architecture can become really expensive, mainly because you need a replica of all the data in all the machines (depending on how you load balance and the availability you want to have). Say you have a 300TB table and you need to handle 1000 QPS. If each replica can manage 100 QPS, you'd need 10 replicas, so 300 * 10 = 3000TB. If you are using SSDs (more on storage later), you have a problem.

I always recommend having a replica just for writes, people call this compute-compute separation. We do this by default and handle the failover and everything in case of error or overload.

You might also decide to split the cluster into more replicas depending on the different workloads. If you have queries that need a particular p99 objective, for example, you may want to isolate those queries to a replica and keep it under 40% load so high percentiles stay stable. Real-time sub-second queries are expensive; forget about those cheap batch jobs running on spot instances. For more on optimizing ClickHouse® for these real-time workloads, see our guide onhigh-throughput streaming analytics.

The load balancer is the key to all of this. Any modern LB would do the job.

## Storage

ClickHouse® open source faces a significant challenge: limited support for cloud storage. Modern OLAP databases and data systems should leverage cloud storage for cost efficiency and independent scaling of compute and storage resources. Snowflake established this standard over a decade ago, and ClickHouse® (open source) lags behind, while other systems like StarRocks are way ahead.

Let me give you a quick tutorial on how storage works in ClickHouse® (and other databases). As I said, you can split your data into "buckets" and put each bucket in a shard. Each shard can have 1 or more replicas (copies) of the data.

The data can be stored locally, in which case every replica needs to copy all the data from other replicas. You insert data in one shard, and the data is replicated to others. In ClickHouse®, that's managed by a central system called Zookeeper.

The data can also be stored in a central system, like S3, in which case replicas can store the data there instead of on a local disk. Each replica could store a copy or simply point to other replica data (that's zero-copy replication).

There are a few cases where using cloud storage does not make sense (more on this, yes, later) but, in most cases, having compute-storage separation is the way to go. What I describe here, unless otherwise stated, uses cloud storage.

In ClickHouse®, you have all those options: local disk, storage, and the zero-copy replication mechanism that relies on cloud storage.

But this last one, zero-copy replication, was contributed by someone outside ClickHouse®, Inc., and it looks likethey don't like it. They have good reasons: it's buggy, you can lose data, it leaves garbage in S3, etc.. ClickHouse® Cloud has its own storage, but it's not open source. But, even with these limitations, it's still usable. In fact, it works pretty well if you are aware of the limitations.

To achieve cost-effective performance, we use a modified zero-copy feature (available in our private fork, something I’ll talk more about in the future, especially if you want to have your own), but you can use it as-is in the ClickHouse® open source repo. Ours includes some changes, operation limitations, and optimizations. We also employ local SSDs for caching, adjusting the cache size based on usage to optimize performance. For customers prioritizing low latency, we use a hot/cold storage architecture with local SSDs and S3. This approach provides the required low latency that S3 alone cannot deliver.

About costs: The way ClickHouse® stores data in S3 is ineffective; it uses a lot of write ops by default (tricks on how to make this better later on ingestion). This has to do with the fact that the ClickHouse® storage system was designed to be used with local storage where write operations are "free" (you are limited by IOPS, which are not free, of course). It uses A LOT of files to store data parts and uses the OS page cache as the cache, so it was not designed with tiered storage in mind. Don't worry, there are ways to make it better.

My general advice is: if you want to use storage-compute separation, use zero-copy replication, but keep an eye on it, because you could be losing data if you do some part operations. And of course, ClickHouse®, Inc. could remove the feature any time (they had actually planned to do it, but they decided not to). If you are not brave enough, go with a hot/cold or just with SSDs and keep a close eye on your costs.

About compression: use ZSTD(1) or maybe ZSTD(2) if you want to have a good compromise between speed and compression. It's better than LZ4 except for a few particular cases, but you can pick the compression per column basics. From time to time, test other compression formats (write speed, read speed, and compression ratio) just in case your data plays well with something that's not ZSTD.

## Upgrades

Upgrades are “easy” now. Well, as easy as updating a database cluster could be, which is never easy. The first update we did took us 3 hours with 2 weeks of preparation. With time, we learned how to do them without experiencing downtime, killing any app sending queries, or losing data. Then, we managed to do it without any performance degradation and finally as part of the CI/CD pipeline. It only took us 4 years to figure out. AFAIK, there is no other company doing this.

My general workflow advice for updating a cluster:

1. Add a new replica on the new version
2. Monitor the replicas' logs and check if something is wrong. You’ll have several heart attacks the first time because ClickHouse® loves to log some stuff that seems critical, but it’s not.
3. If you can avoid DDL changes like adding columns, data-skipping indices, or anything that modifies table structure, that's better.
4. It’s obvious, but do not use any new feature in the new replica until your cluster is up to date with the new version.
5. Send somereadtraffic to check if everything is fine (timing, memory, resource usage...)
6. Test writes/inserts
7. Now it’s time to move real traffic. If you are unsure, keep the replica for a few hours.
8. After that, start updating other replicas.

You can do that thanks to the backward-compatible replication protocol. We did a lot of work to keep the replication protocol backward compatible. Our CI pipeline tests upgrades, and we were able to detect problems before the ClickHouse® release happened (so we could send a PR). Fortunately, it's not happening anymore. It's way more stable now.

### Problems you'll find

* Rarely: Data storage format incompatible changes. It has happened to us 2-3 times in the last 2 years, we fixed at least 2, not aware of others. We noticed it because we have all the possible combinations of data types in our customer base. It's unlikely that you'll hit this issue in a regular deployment (not multi-tenant). In these cases, good luck, prepare yourself to dig deeper into the filesystem or recover a backup. Do not upgrade anything right away after the release; wait at least a month. Don’t use any experimental feature unless you know what you are doing.
* SQL behavior change. That's usually caused by bug fixes, but it can break your queries. Make sure you test your expected data correctly. You have the system.query_log with all the queries your cluster runs. Use it all the time.
* Performance changes. Sometimes for the better, sometimes for the worse. They are not usually bad, but test your queries for performance, otherwise, you'll need to roll back.
* Settings changes: this is something to take a look at really deeply, as you need to review the new ones and changes in the old ones. Pay attention to features that are disabled by default or flags that change. The changelog is usually a good way to understand what to look for, but you may want to have your CI pointing to the latest master build.

We have a somewhat complex system to validate that everything is fine before an upgrade:

* In CI, we run all the tests in different versions and run clusters with a mix of versions (so we know they can live together in the same cluster). This is something you should do as well.
* Once a day, we run all the queries our customers run with the next version to check everything is fine. When it's not, we fix it or ping the customer.
* We update clusters automatically if everything passes the tests.

In summary, updating your cluster requires building muscle. It doesn't happen overnight; it happens through repetition, suffering, and recovery.

## Configuration and testing

As I said before, keep track of the settings that change. At Tinybird, we have an automatic system for that. Pro tip: check for the diffs between versions in everything that looks like this in the source code:

An important note: if you want to operate ClickHouse® effectively, you need to read the source code. This wasn't necessary with other databases I worked with (I was CTO of a company managing hundreds of Postgres clusters), but I found it to be the case with ClickHouse®. Most of the biggest companies running ClickHouse® have patches upstream.

About testing: my recommendation is to have your CI run your app against the version you have in production, ClickHouse® master, and the next one you want to update to.Because you are testing your analytics queries, right?

Last but not least: Do not test a single instance; test against a cluster with at least two machines and the Zookeeper or ClickHouse® Keeper. The behavior is not the same; creating tables could fail easily, you'll have replication lag, and there are other small details you want to test.

I will talk about specific settings in the following sections

## Costs

The math for running a cluster is easy:

* Costs of the replicas/shards. The cost depends on the price of your infra, of course.
* At least 3 ZooKeeper replicas. It should be on a different machine/pod/whatever than the database. The reason is you want your ZK server to be as isolated as possible. If you have ZK in the same pod/machine and the machine gets overloaded, everything will be slow and eventually fail, leaving your tables in read-only mode (best scenario). A ZK problem means you are fucked.
* Storage: you need to decide where you are storing the data: locally, S3, or both, and crunch the numbers. There are some recommendations in the "storage" section, but you should take into account that disks can't be resized down, and in S3 you need to account for operation costs.
* Likely a load balancer. A small one is fine. You need HA, so a couple of them.
* Backup storage: Depending on the retention policy and the amount of data, this could be expensive.

How to decide how many cores you need: it depends a lot on your load and use case. There is no easy way, but as a rule of thumb, a 32-core machine can process around 5GB/s max (of uncompressed data) healthily.

About the people needed to handle the system: For a small cluster, a single part-time person is good enough. For loads with over 20k rows/s and people pushing changes, you may need a full-time person to handle the cluster and take a look at the crazy queries people are going to write. There is a difference of 3-4x in the hardware you need if you follow some basic rules. So, if you are not paying US salaries, having someone looking after the cluster pays off.

When you reach that point, hiring the right people becomes as critical as choosing the right hardware. Good ClickHouse® and data infrastructure engineers are hard to find, and generic hiring pipelines usually do a poor job at screening for this profile. If you do not have an internal recruiting function with deep experience in engineering roles, consider partnering withtop software development recruiterswho understand modern data infrastructure, failure modes, and on call realities so they can help you build a team that can actually run this in production.

Regardless, I don't recommend handling a cluster by yourself. You want to solve your analytics product requirements, not spend your time handling ClickHouse®. That’s why we created Tinybird, but if you have read this far, it means you want to DIY, and I feel you.

Let me clarify something: we created Tinybird ClickHouse because we wanted to build an analytics application without all the pain I'm describing. We do not offer ClickHouse® hosting; we solve the analytics problem. It's a narrower problem than a data warehouse solves, and we solve it much better. This Tinybird ClickHouse approach gives you the best of both worlds.

## Ingestion

This section is going to be fun.

Every single company handling ClickHouse® struggles with ingestion. They lose data (most of the time without knowing it), duplicate data, take the database down…

Ingestion is not just about inserts; it's a fine balance between many things:

* Merges
* Inserts
* Reads
* Mutations
* Table design

To design this well is an art.

Let me explain some basics about how ClickHouse® works: When you run an insert, it generates a new part. From time to time, those parts are merged in a background process, where from many "small" parts a larger one is generated. If you are familiar with Iceberg, this is the compaction process.

You want to have large parts so reads are faster (reads are faster if they need to get data from fewer parts). That's why you run merges. But if the parts are large, merges take a lot of time, CPU, and memory, so you need to find a balance. You'll find your cluster get's fucked up doing merges from time to time.

You might be thinking: let's make the insertion batches larger so it does not need to generate a lot of parts. That's exactly right, but larger parts mean more latency as you need to wait for more data. And it means more memory on inserts, so you'll end up with inserts running out of memory.

The typical situation is a query that uses all the CPU and/or IO, inserts start to pile up, memory grows, which leads to a wonderful OOM, and that means data loss.

More on table design later, but partitioning (or how you cluster those parts together) plays an interesting role here.

So my recommendation on this:

* Batch inserts (there is an async insert in ClickHouse®, but it's pretty limited), not too large, not too small. Do not generate too many parts per insert (I always aim to have just 1 per insert). If you can batch per partition and have different flush times, that's better (you don't need to update last month’s partitions every second).
* Run frequent inserts only on tables that need it.
* Use Compact parts if you use S3 (and even if you don’t). It saves a lot of write ops, and you won't reach S3 rate limits.
* Sometimes having a "small" hot disk saves you a lot of money as the writes and first merges will be done on that disk, so no S3 ops costs.
* Tweak max part size to avoid extra merges, but be careful not to make them too large.
* Teach your team about table partitioning. You can’t decouple table design from ingestion. A wrong partition key can kill the cluster, too many writes can kill the cluster, a badly designed materialized view…

Memory is going to be a big issue, especially if you use materialized views (and you should). An MV that's slightly wrong and uses more memory than needed OOMs the server. We have a system that disconnects MVs in those cases.

Other problems you will find:

* Tables in read-only mode: usually because the replica is starting, so wait a little bit and check before moving writes to it. Sometimes happens because of “unknown reasons”. One quick way to fix: drop the table, recreate it, and let replication do the job.
* Too many parts: when you are writing a high number of parts in each write. For example, you partition your table per day and insert 3 years of data. Again, try to write data that lands in one partition at a time.
* Too many parts, merges are slower than inserts. When you insert too fast and the merge queue grows too much. Increase the thread pool, backpressure ingestion based on this, or change settings to allow the queue to grow more.

Other things you'll need to deal with:

* Backpressure mechanism: Some people put Kafka before ClickHouse®. This does the job, but it could be super expensive. We developed a custom system, as Kafka was not the right choice for us: We are multi-tenant, costs would explode, and we need to tweak ingestion on a per-table basis. If you are in production, you have to have something like this, or else any small incident will lead to data loss.
* Sudden peaks: it happens, and you'll not have time to spin up a new replica or change the cluster size. So you'd need a queue that manages those peaks.
* Duplicated data: if an insert fails and you didn't design the system carefully, you'll end up with duplicated data, all the materialized views will be broken, and stats will be wrong. More on this later.

This is just the first part.Here's part 2, where I cover:

* Operating the cluster and monitoring (considerconnecting Grafana to ClickHouse®for visualization)
* Handling load
* Performance tweaks
* Other common issues