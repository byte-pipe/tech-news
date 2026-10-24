---
title: "Twelve years of distributed SQLite – Philip O'Toole"
url: https://philipotoole.com/twelve-years-of-distributed-sqlite/
date: 2026-10-24
site: hnrss
model: llama3.2:1b
summarized_at: 2026-10-24T14:34:21.503325
---

# Twelve years of distributed SQLite – Philip O'Toole

**2014: Introduction of rqlite**

* The need for a distributed SQLite system arose as a problem for a small amount of relational storage needs at a project called jut.ione.
* The solution used a Raft consensus protocol to replicate writes to a cluster, solving the problem of which node to hold the data.
* The first version of rqlite relied on goraph, InfluxDB, and etcd.

**Design Foundations**

* The design decision that mattered most was to use a CP (consensus protocol) system, where writes must go through a leader, be acknowledged by a majority, and rejected by a partitioned minority.
* rqlite was designed to be a general-purpose, open-source system that can run standalone or as a server.

**History**

* Two other projects, Expensify and Bedrock, had been replicating SQLite using Paxos protocols in the same vein.
* rqlite was the first project to combine Raft and SQLite, and it gained popularity quickly.
* It is now considered one of the most influential and successful projects in the category.

**2016: Raft Implementation**

* The design of rqlite was influenced by Hashicorp's Raft implementation of InfluxDB and etcd.
* The Raft design decision, to make a majority of writes acceptable, was retained in rqlite.

**Parallel Developments**

* Other projects, such as ActorDB, showed the effectiveness of implementing Raft-like protocols for SQLite replication.
* Canonicalbuiltdqliteto getLXD and MicroK8s embedded replicated stores with Raft, but rqlite remains the most standalone and general-purpose system.