---
title: 'Atlas Infinite: MongoDB''s Disaggregated Architecture'
url: https://muratbuffalo.blogspot.com/2026/10/atlas-infinite-mongodbs-disaggregated.html
site_name: tldr
content_file: tldr-atlas-infinite-mongodbs-disaggregated-architecture
fetched_at: '2026-10-11T13:38:41.112810'
original_url: https://muratbuffalo.blogspot.com/2026/10/atlas-infinite-mongodbs-disaggregated.html
date: '2026-10-11'
description: 'Atlas Infinite: MongoDB''s Disaggregated Architecture'
tags:
- tldr
---

### Atlas Infinite: MongoDB's Disaggregated Architecture

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-

October 10, 2026

Atlas Infinite, which dropped in public preview on September 29 alongside MongoDB 9.0, delivers a significant architectural update payload: compute-storage disaggregation.Separating compute from storage is not new, and there are well-known ways to do it. But what makes Atlas Infinite interesting is how MongoDB departs from the standard design to keep WiredTiger's efficiency and to ensure that the shared storage layer never sees customer data unencrypted.

I am giving a high level overview of the architecture here distilling fromthe MongoDB Engineering blog postby Abhishek Chauhan, who led the effort. For detailed coverage, I refer you to that post. It is a great read, and parts 2 and 3 will drop soon.

## Why not earlier, and why now

Disaggregated databases have existed for some time, so why did MongoDB wait? This is mainly because MongoDB didn't need disaggregation to scale out: when a workload outgrew one machine, sharding spread it across many nodes in a seamless manner.  MongoDB was among the first databases to ship sharding with automatic chunk balancing and routing. Since horizontal scaling has been a first-class feature for over a decade,  MongoDB never faced the single-node limit that pushed other systems toward  disaggregation early. That bought us time to do disaggregation right, without regressing on WiredTiger's performance or its security model.

Disaggregation is a good idea for several reasons anyways, and MongoDB adopted it to address customer needs. For one, storage gravity has become the  bottleneck for very large clusters. In Atlas's shared-nothing architecture, each node in a three-node replica set has its own disk with a full copy of the  data. That means, operations like growing storage, adding a replica, or restoring a backup, would require copying the whole dataset. On a large cluster  that can take hours when customers expect minutes. And since compute and  storage come bundled, needing more of one means paying for more of both. This  is why customers want compute and storage to scale independently. Disaggregation helps in right-sizing the customers and giving them flexibility for scaling. Finally,recent agentic development patternswant cheap snapshots,  clones, and branches of production data.

## How MongoDB departs from the traditional disaggregated design

The standard approach works something like this. Compute is stateless. It ships a physical redo log (a record of every change to every page) to a quorum-replicated log service. Page servers read that log and rebuild pages by replaying the changes, so they can produce any page as of any point in the log. Object storage sits underneath as the durable copy.

MongoDB adopted much of this approach, but it broke with the traditional design in several places in order to keep WiredTiger's performance characteristics and the security guarantees customers expect.

Let's start with WiredTiger, one of the most sophisticated storage engines in production. WiredTiger achieves high performance by deferring and batching work. It is built around checkpoint-based consistency: rather than logging each page modification one by one, it lets writes accumulate in memory. A page can absorb many mutations and get written to disk just once, at a checkpoint. This amortizes the cost of turning writes into readable state. (This is increasingly where the field is heading as modern engines keep converging on copy-on-write, multi-version, checkpointed designs.) Forcing WiredTiger to log every page change for disaggregation sake would cripple its efficiency.

Secondly, because WiredTiger is lock-free and parallel and evicts pages speculatively, there is no canonical page image: two nodes holding the same data hold different bytes. So "replicate the pages" has no single correct target to replicate toward, which breaks from the traditional disaggregated design.

Finally, MongoDB refused to let shared storage read customer data. A storage tier that rebuilds pages from a log must be able to read them, so security ends up resting on operational controls. The better approach is to treat unencrypted user data as toxic. Holding it is a big responsibility, so keep it encrypted for as much of its lifetime as you can. That matters most when storage is shared across tenants, where one mistake no longer stops at one customer.

Because MongoDB owns the engine, the server, and the cloud service, it could co-design across all three layers. While the traditional design makes storage smart (by reading the data and rebuilding any page on demand), MongoDB went the other way and made storage blind to preserve WiredTiger's efficiency and to guarantee that storage can never read customer data unencrypted.

## The architecture

Compute (primary, hot standby, and optional read replicas) runs queries and transactions and keeps only caches and recent changes, all of which can be rebuilt from storage if the node is lost. The shared storage layer, written in Rust, has three parts. A Log Service does only one thing, consensus on the log, which keeps it simple and steady. A Page Service spreads each customer's pages across many servers in every zone, with page materializers feeding it from the log. Object storage is responsible for long-term durability, organized by an Object Index Service.

Difference 1: two logs instead of one.A write is durable once the oplog, MongoDB's logical operation log, is on a majority of Log Service replicas across three zones. Separately, at checkpoint time, WiredTiger emits a phylog of physical page changes, mostly deltas. Page servers organize these by page after receiving them through the log service. This allows WiredTiger to keep its batching. Pages are written once per checkpoint, not once per change. Durability and page materialization are fully separate, with only the oplog on the critical path.

Difference 2: storage never sees your unencrypted data.In Atlas Infinite, data is encrypted on the compute node before any byte goes down, and decrypted only there, inside the customer's network, with keys the customer can hold and revoke. Storage can't see documents, collection names, indexes, or even tenant boundaries. Even obtaining root access to the whole storage fleet would yield an attacker only opaque bytes. Contrast this to the traditional design where storage must read data to rebuild pages, so security is partly "trust us" and partly "best intentions".

Difference 3: fresh replicas without page-level logging.In contrast to the traditional disaggregated approach where storage can build any page at any log point, in MongoDB pages only advance at checkpoints, so a replica reading only shared pages could potentially lag by seconds. This is easy to address however on the standby and read replica. Note that page servers build checkpoint-consistent pages from the phylog. On top of that, the compute node applies the oplog (as it arrives from the Log Service) to a local ingest table. Reads combine both to construct the fresh data. This way MongoDB gets millisecond replica lag while keeping checkpoint batching.

Finally, a word on availability. Every cluster has a hot standby, so a primary failure is a quick handoff rather than starting a new node. Data lives in three forms at once (the replicated log, the page servers, and object storage), the fleet is split into isolated cells so trouble in one can't cascade into the next, and recovery parallelizes across many machines rather than falling to one.

disaggregation

mongodb

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Popular posts from this blog

### The Safest Job from AI may be Writing

-

August 31, 2026

Today, tech folk are scrambling to change their workflows to meet newly inflated 5X productivity quotas, while getting pummeled under the cognitive debt of agent-generated code. With every new model release, the gap is widening and humans are becoming more of a bottleneck in the loop, approaching closer to obsolescence as "coders". While the programmer's job description is getting completely refactored, writing remains surprisingly unaffected. LLMs have gotten very good at generating code, but I am appalled at the absolute shit they spew as prose. They always follow the same robotic cadence and cliches, and sprinkle the same tired vocabulary all around. They take my broken yet soulful writing and transform it into a plastic soulless word slop in the name of improving prose. Their writing communicates no actual understanding and insight. I think we are all developing a visceral ick reaction to AI writing. It is trapped in the uncanny valley, and it may be stuck there for ...

Read more >>

### The Two Abstractions of System Design: Hide or Reduce

-

May 08, 2026

When talking about TLA+, I keep referring to "abstraction" as the most important thing to learn . And it is about the hardest to learn as well. But a contradiction has been bugging me. Aren't CS people already supposed to be good at abstraction? Isn't abstraction supposed to be at the root of OS, networking, software engineering? Abstract Data Types (ADTs) are a staple of every in CS curriculum. So why do I (and every other formal methods/modeling person) see such a large skill gap in abstraction, and flag it as the core, make-or-break skill for modeling? I think I finally get to the root of this cognitive disonance. There are two kinds of "abstraction" conflated under the same umbrella term. Modularity abstraction: This is the traditional abstraction taught in CS curricula as ADTs, APIs, layered design, etc. It is all about encapsulation, drawing boundaries, and hiding internals. Modeling abstraction: This is what I talk about when I talk about abstracti...

Read more >>

### The Agentic Self: Parallels Between AI and Self-Improvement

-

January 02, 2026

2025 was the year of the agent. The goalposts for AGI shifted; we stopped asking AI to merely "talk" and demanded that it "act". As an outsider looking at the architecture of these new agents and agentic system, I noticed something strange. The engineering tricks used to make AI smarter felt oddly familiar. They read less like computer science and more like … self-help advice . The secret to agentic intelligence seems to lie in three very human habits: writing things down, talking to yourself, and pretending to be someone else. They are almost too simple. The Unreasonable Effectiveness of Writing One of the most profound pieces of advice I ever read as a PhD student came from Prof. Manuel Blum, a Turing Award winner. In his essay "Advice to a Beginning Graduate Student", he wrote: "Without writing, you are reduced to a finite automaton. With writing you have the extraordinary power of a Turing machine." If you try to hold a complex argument enti...

Read more >>

### In Search of a Compositional Theory of Self-Stabilization

-

September 21, 2026

My quest for a principled solution for metastable failures has taken me back to my roots on self-stabilization, as this recent paper related the problem to composition of self-stabilizing systems.  But, my literature search for recent work on composing self-stabilizing systems didn't yield anything useful. The layered stabilization idea was already in place by the early 2000s, and nothing fundamental seems to have been added since. Frustrating. So I decided to attack the problem using the concrete example I have. I had composed a rely-guarantee TLA+ model of a retry storm as two components with contracts . That model reproduces metastable failure because the composition that worked from good states failed to work when a large shock removes the base case that let the two conditions hold each other up. Searching for  rely-guarantee based composition from every state, turned up a 2017 control theory paper by Kim, Arcak and Seshia, "A Small Gain Theorem for Parametric Assume-Gua...

Read more >>

### Learning about distributed systems: where to start?

-

June 10, 2020

This is definitely not a "learn distributed systems in 21 days" post. I recommend a principled, from the foundations-up, studying of distributed systems, which will take a good three months in the first pass, and many more months to build competence after that. If you are practical and coding oriented you may not like my advice much. You may object saying, "Shouldn't I learn distributed systems with coding and hands on? Why can I not get started by deploying a Hadoop cluster, or studying the Raft code." I think that is the wrong way to go about learning distributed systems, because seeing similar code and programming language constructs will make you think this is familiar territory, and will give you a false sense of security. But, nothing can be further from the truth. Distributed systems need radically different software than centralized systems do.  --A. Tannenbaum This quotation is literally the first sentence in my distributed systems syllabus. Inst...

Read more >>

### Building a Database on S3

-

March 04, 2026

Hold your horses, though. I'm not unveiling a new S3-native database. This paper is from 2008. Many of its protocols feel clunky today. Yet it nails the core idea that defines modern cloud-native databases: separate storage from compute. The authors propose a shared-disk design over Amazon S3, with stateless clients executing transactions. The paper provides a blueprint for serverless before the term existed. SQS as WAL and S3 as Pagestore The 2008 S3 was painfully slow, and 100 ms reads weren't unusual. To hide that latency, the database separates "commit" from "apply". Clients write small, idempotent redo logs to Amazon Simple Queue Service (SQS) instead of touching S3 directly. An asynchronous checkpoint by a client applies those logs to B-tree pages on S3 later. This design shows strong parallels to modern disaggregated architectures . SQS becomes the write-ahead log (WAL) and logstore. S3 becomes the pagestore. Modern Aurora follows a similar logic : t...

Read more >>

### Foundational distributed systems papers

-

February 27, 2021

I talked about the importance of reading foundational papers last week. To followup, here is my compilation of foundational papers in the distributed systems area. (I focused on the core distributed systems area, and did not cover networking, security, distributed ledgers, verification work etc. I even left out distributed transactions, I hope to cover them at a later date.)  I classified the papers by subject, and listed them in chronological order. I also listed expository papers and blog posts at the end of each section. Time and State in Distributed Systems Time, Clocks, and the Ordering of Events in a Distributed System. Leslie Lamport, Commn. of the ACM,  1978. Distributed Snapshots: Determining Global States of a Distributed System. K. Mani Chandy Leslie Lamport, ACM Transactions on Computer Systems, 1985. Virtual Time and Global States of Distributed Systems.  Mattern, F. 1988. Practical uses of synchronized clocks in distributed systems. B. Liskov, 1991. Exp...

Read more >>

### Cloudspecs: Cloud Hardware Evolution Through the Looking Glass

-

January 09, 2026

This paper (CIDR'26) presents a comprehensive analysis of cloud hardware trends from 2015 to 2025, focusing on AWS and comparing it with other clouds and on-premise hardware. TL;DR: While network bandwidth per dollar improved by one order of magnitude (10x), CPU and DRAM gains (again in performance per dollar terms) have been much more modest. Most surprisingly, NVMe storage performance in the cloud has stagnated since 2016. Check out the NVMe SSD discussion below for data on this anomaly. CPU Trends Multi-core parallelism has skyrocketed in the cloud. Maximum core counts have increased by an order of magnitude over the last decade. The largest AWS instance u7in now boasts 448 cores. However, simply adding cores hasn't translated linearly into value. To measure real evolution, the authors normalized benchmarks (SPECint, TPC-H, TPC-C) by instance cost. SPECint benchmarking shows that cost-performance improved roughly 3x over ten years. A huge chunk of that gain comes from AWS G...

Read more >>

### Specula: Scaling formal specifications for autonomous model checking of system code

-

August 12, 2026

Specula is an agentic system that automates the process of software bug finding through authoring and model-checking a spec for the code. It derives TLA+ specifications automatically from the code, checks code-spec conformance through trace validation, model checks the spec to find concurrency bugs, and reproduces the bug at the code layer by writing integration tests with precise timing. I remember reading the Daikon paper "Quickly detecting relevant program invariants" in 2000 and getting impressed by it, and here we are after 26 years, solving the end-to-end problem much better than I ever thought would be possible in a push-button manner in the year of our lord 2026. But somehow, I am still somewhat unsatisfied with the paper. This may be me being hypercritical and trying to get more out of the paper by arguing with it . So bear with me until I resolve (or learn to accept) these problems over time. I know many of the authors of the Specula work, and respect them, and I...

Read more >>

### Hints for Distributed Systems Design

-

October 02, 2023

This is with apologies to Butler Lampson, who published the " Hints for computer system design " paper 40 years ago in SOSP'83. I don't claim to match that work of course. I just thought I could draft this post to organize my thinking about designing distributed systems and get feedback from others. I start with the same  disclaimer Lampson gave. These hints are not novel, not foolproof recipes, not laws of design, not precisely formulated, and not always appropriate. They are just hints.  They are context dependent, and some of them may be controversial. That being said, I have seen these hints successfully applied in distributed systems design throughout my 25 years in the field, starting from the theory of distributed systems (98-01), immersing into the practice of wireless sensor networks (01-11), and working on cloud computing systems both in the academia and industry ever since. These heuristic principles have been applied knowingly or unknowingly and has proven...

Read more >>