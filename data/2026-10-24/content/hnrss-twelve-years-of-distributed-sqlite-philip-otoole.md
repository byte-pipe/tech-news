---
title: Twelve years of distributed SQLite – Philip O'Toole
url: https://philipotoole.com/twelve-years-of-distributed-sqlite/
site_name: hnrss
content_file: hnrss-twelve-years-of-distributed-sqlite-philip-otoole
fetched_at: '2026-10-24T14:29:58.984465'
original_url: https://philipotoole.com/twelve-years-of-distributed-sqlite/
date: '2026-10-24'
description: 'In September 2014 I published a short post announcing rqlite. The idea was simple: take SQLite, put a Raft log in front of it, and replicate every write to a cluster so that the loss of a node did not mean the loss of the data. The source went on GitHub that same weekend. As…'
tags:
- hackernews
- hnrss
---

In September 2014 I published ashort post announcingrqlite. The idea was simple: takeSQLite, put aRaft login front of it, and replicate every write to a cluster so that the loss of a node did not mean the loss of the data. Thesource went on GitHubthat same weekend. As far as I can tell, that was the first open-source system to combine Raft and SQLite. Nobody else was doing it, and for several years nobody else tried.

Today “distributed SQLite” is a category with a dozen projects in it, a few of them venture-funded, two of them acquired. Since the people now writing about the category tend to start the story around 2021, I thought I should write down the version that starts in 2014. I was there for all of it.

## 2014: rqlite

The need was concrete. A clustered systemI worked on at jut.ioneeded a small amount of relational storage, and the question of which node should hold it had no good answer. Replicating SQLite with a consensus protocol solved it. We went another way at work, butI kept building rqlitebecause the problem was general and the solution was small. The first version usedgoraft, the same libraryInfluxDBandetcdused at the time (I subsequently joined InfluxDB as a core developer around the same time). In early 2016 Ireplaced it withHashicorp’s Raft implementationwhich rqlite still uses.

The design decision that mattered most was made then and never changed. rqlite is aCP system. Writes must go through the leader, a majority must acknowledge, and a partitioned minority refuses writes. Everything else, theHTTP API, theread-consistency levels, thesnapshotting, followed from that.

## Before 2014, and alongside it

Two things deserve mention for honesty’s sake.Expensifyhad been replicating SQLite inside its own infrastructure for years with aPaxos-style protocol; they released it asBedrockin2016. And ActorDB, an Erlang system that gave each “actor” its own SQLite database replicated by Raft,appeared around the same time as rqlite. Neither was widely adopted outside its origin, but both show the idea was in the air. What rqlite did was make it a standalone, general-purpose, open-source thing anyone could run.

## 2017: dqlite

Canonicalbuiltdqliteto getLXDand later MicroK8s an embedded replicated store without running etcd.Mark Shuttleworthactually called me once, and we talked, hoping that rqlite could be made to work, but it never quite fit. dqlitebegan in Goand was rewritten in C with its own Raft library. It is the project most similar to rqlite in intent, and the main difference is of one of packaging: dqlite is a library you embed, rqlite is a server you run. Canonical’s need was a database inside their products: mine was a database beside anyone’s product.

## 2021: Litestream, and a change of approach

Ben Johnson(whom I worked with at InfluxDB) releasedLitestreaminearly 2021. Litestream does not use consensus at all. It watches the SQLiteWALand streams it toS3, giving you disaster recovery for a single-node SQLite database at almost no cost. Ben’s argument was that most applications do not need a cluster; they use one machine and need a way to recover if it dies. He was right about a great many applications, and the “SQLite is enough” movement of the next few years, with blog posts and conference talks, owes a lot to that argument.

Litestream and rqlite answer different questions. Litestream: what if the machine dies? rqlite: what if the machine dies and I cannot wait to restore? The first question is more common, the second is the one people have when they come to rqlite.

Fly.iohired Ben in 2022 and shippedLiteFS, which replicates SQLite at filesystem level with leases fromConsul. It was the first attempt to make replicated SQLite a platform feature rather than a thing you deploy. And in a final twist, Litestreaminspiredrqlite’s v8.0 approach to handling the SQLite WAL.

## 2022: forks and extensions

Two projects in 2022 took approaches that neither rqlite nor Litestream had.cr-sqliteaddedCRDTsto SQLite as an extension, so that multiple writers could diverge and merge without a leader. That is the AP corner of the design space, and it suits local-first applications where rqlite’s CP guarantees would be a hindrance.

libSQLforked SQLite itself. ChiselStrike, laterTurso, wanted to change things inside the engine that the SQLite project, which does not accept outside contributions, and would not change. On top of the fork they built a hosted service with replicas at the edge. Turso raised venture money on that, and in 2026Supabase acquired them.

Around the same time,SQLite Cloudappeared, offering hosted SQLite replicated with Raft. It is the project closest to rqlite’s original design, wrapped in a cloud service.

## 2022 onward: the platforms

CloudflareannouncedD1in 2022, SQLite as a serverless database inside their edge network, and later put SQLite storage insideDurable Objects. This is replicated SQLite as a managed product from a company that does not need to tell you how it works. Turso’s service is the same shape. The category had gone from “a thing you run” to “a thing you buy.”

## What the twelve years show

Three things, I think.

The core was right. SQLite as a storage engine, with replication added on the outside, has been reinvented by at least eight teams with different needs and different protocols. Nobody has found a reason to stop doing it.

The design space has three corners, and they appeared in order. Consensus first (rqlite, dqlite): one leader, strong consistency, a cluster. Streaming second (Litestream): one writer, cheap recovery, no cluster. Merge third (cr-sqlite, and parts of the local-first movement): many writers, eventual consistency. Each is correct for a different question, and most of the arguments are arguments between their users about which question is being asked.

And the money went to the platforms. rqlite, dqlite, and Litestream are open source and free. The projects that raised the capital or got acquired are the ones that turned replicated SQLite into a service with a bill. That is the usual fate of infrastructure ideas, and I do not mind it. But it is worth recording that the idea was open source for eight years before anyone sold it.

rqliteis still here. It does the same thing it did in 2014, a good deal better, and it is still the thing you reach for when you want a fault-tolerant relational database you can run yourself, understand fully, and not pay anyone for. Twelve years in, I am content with that position in the story.

Tags
#
 database
#
 distributed systems
#
 go
#
 open-source
#
 programming
#
 rqlite
#
 sqlite