---
title: RIP, vector database
url: https://turbopuffer.com/blog/rip-vector-database
site_name: hackernews_api
content_file: hackernews_api-rip-vector-database
fetched_at: '2026-10-01T23:02:15.874753'
original_url: https://turbopuffer.com/blog/rip-vector-database
author: razin
date: '2026-10-01'
description: turbopuffer is pushing the frontier of search. To do that, we have to fundamentally redesign our storage architecture so the vector index is no longer primary.
tags:
- hackernews
- trending
---

tpuf v3 is coming: follow along
turbopuffer v3 is coming: follow our progress

# RIP, vector database

September 30, 2026
•
Dan Harrison (Engineer)

We are changing turbopuffer's storage architecture to take search to the next
level. turbopuffer v3 changes how documents and indexes are laid out, written,
compacted, and queried in turbopuffer. It will allow us to make search faster in
every respect — including text, regex, and vector search — but it also lays the
foundation to move many more SQL queries to turbopuffer and make them fast.

turbopuffer launched as aserverless vector database (v1),
highly specialized to the task of serving extremely cheap and reasonably fast
vector searches. Object storage as the source of truth gave the economics, and
tiered NVMe SSD/memory caches gave the performance. The value of these
particular tradeoffs was validated by our earliest customers, including Cursor
and Notion.

turbopuffer evolved to have very strong text and regex search (v2), and is being
used for many non-search use cases, likeLinear's syncing engine.
The query engine has evolved along the way to support all of these query plans,
but the storage architecture has remained largely unchanged: the ANN vector
index was and still is the primary index around which all other indexes and
query plans revolve. This design has constrained several query plans, likeGROUP BYand aggregations.

We've pushed the vector-primary architecture as far as we can, and it's time to
move on. We're in the process of moving to a new primary index, and making ANN
"just another" secondary index. We thought it might be fun to open up the doors
and let you follow along.

For this first update, we'll set the stage with why we're doing this in the
first place. Walk with me on a short journey from tpuf v1 to today.

## v1: an ID and a vector

In the first version of turbopuffer, documents consisted of nothing but an ID
and a vector. The prevailing wisdom at the time was graph-based vector indexes,
but a hierarchical clustering index plays better with object storage. We started
withSPANN, and eventually migrated toSPFreshto support incremental indexing.
Vectors are clustered into groups, whose centroids are clustered in turn,
repeated to form a tree with a single root.

 ┌───────────────────┐
 │ root centroid │
 └───────────────────┘
 ╱ │ ╲
 ╱ │ ╲
┌───────────────────┐ ┌───────────────────┐ ┌───────────────────┐
│ leaf centroid │ │ leaf centroid │ │ leaf centroid │
└───────────────────┘ └───────────────────┘ └───────────────────┘
 ╱ ╲ ╱ ╲ ╱ ╲
 ╱ ╲ ╱ ╲ ╱ ╲
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│ vector │ │ vector │ │ vector │ │ vector │ │ vector │ │ vector │
└────────┘ └────────┘ └────────┘ └────────┘ └────────┘ └────────┘

 ┌───────────────┐
 │ root centroid │
 └───────────────┘
 ╱ │ ╲
 ╱ │ ╲
┌────────┐┌────────┐┌────────┐
│ leaf ││ leaf ││ leaf │
│centroid││centroid││centroid│
└────────┘└────────┘└────────┘
 ╱ ╲ ╱ ╲ ╱ ╲
┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐
│vec││vec││vec││vec││vec││vec│
└───┘└───┘└───┘└───┘└───┘└───┘

We implemented this on top of a storage layer presenting as a key-value map,
with sorted and unique keys. Each cluster is given aClusterId, and vectors
within each cluster are given a denseLocalId.

// leaf vectors

K::
Vector
(C0L0) = 
vec!
[
0.45
, 
0.32
, ...]
K::
Id
(C0L0) = 
7

K::
Vector
(C0L1) = 
vec!
[-
0.28
, 
0.96
, ...]
K::
Id
(C0L1) = 
13

// cluster centroid for C0 is itself clustered at the next level of the tree

K::
Vector
(C1L4) = 
vec!
[
0.64
, -
0.48
, ...]
K::
Id
(C1L4) = C0

As you can see above, everything is keyed byClusterIdandLocalId(e.g.C0L1), which together we call theANN address. This is what we mean when
we say the ANN index is the primary index.

## v2: attribute filtering and full-text search

Two new query plans marked the informal transition from turbopuffer v1 → v2:
attribute filtering and full-text search.

### Attribute filtering

Naturally, customers wanted to be able to add attribute values and filter vector
searches on them. Tomake filtering fast and high-recall, we modeled these
as an inverted index that maps an attribute value to the ANN address of the
documents that contain it.

K::
AttrIndex
(
"family"
, 
"Alcidae"
) 
->
 
vec!
[C0L3, C1L2, C1L3, ...]
K::
AttrIndex
(
"genus"
, 
"Fratercula"
) 
->
 
vec!
[C0L3, C1L2, C1L9, ...]

For projections (include_attributes), we also stored the document attributes
alongside the ID and the vector.

K::
Vector
(C0L0) = 
vec!
[
0.45
, 
0.32
, ...]
K::
Id
(C0L0) = 
7

K::
Attr
(C0L0, 
"family"
) = 
"Alcidae"

K::
Attr
(C0L0, 
"genus"
) = 
"Fratercula"

### Full-text search

BM25 full-text search was another obvious and much-demanded query plan. Similar
to attribute search, full-text search works by first finding the documents that
have the query term present (commonly called "postings"). For an FTS index, we
also include the(term count, document length)metadata necessary for BM25
scoring:

K::
FTS
(
"description"
, 
"Atlantic"
) 
->
 
vec!
[(C0L0, 
2
, 
37
), (C9L4, 
1
, 
42
), ...]
K::
Attr
(C0L0, 
"description"
) 
->
 
"A sharply dressed black-and-white seabird with a \
huge, multicolored bill, the Atlantic Puffin is often \
called the clown of the sea. It breeds in burrows on \
islands in the North Atlantic, and winters at sea."

Over time, we've shipped several other index structures and query engines:aggregations,regex search,fuzzy matching,sparse vector search, andattribute ordering— all built around the
same vector-primary storage layout.

## The problem with a vector primary index

The ANN primary index has largely remained intact until today for one simple
reason: it works really, really well for ANN search on object storage. On top of
this architecture, we've pushed vector search tosingle indexes of 100B+ vectors serving 200 ms p99 reads at 1k+ QPS.
Any significant change here risks introducing regressions in ANN performance.

However, this layout holds us back from being state-of-the-art for the
non-vector query shapes we support, in three main ways: storage amplification,
write amplification, and limited vectorization.

### Storage amplification

As described above, turbopuffer currently puts the full contents of each
document under its ANN address. When there is only one vector, the non-vector
data is stored alongside the vector only once.

However, for multi-vector representations of a document, such as document
nesting or late interaction, this means we have to duplicate the contents for
each vector. This is the reason for some of our more unfortunatelimits.

### Write amplification

Any time a document is inserted, updated, or deleted, SPFresh may rebalance the
vectors to ensure they remain well clustered (otherwise recall may suffer).
Because everything in a document is stored keyed by the ANN address of the
document's vector, this rebalancing cascades to moving the full document
contents, as well as any inverted (attribute and FTS) indexes that reference it.
Updating just one vector can move hundreds of attributes and their indexes.

This write amplification is large enough that our efforts to tune indexing
throughput have started to hit diminishing returns.

### Limited vectorization

Modern query engines arevectorized: they run tight
loops over blocks of values, which amortizes fixed per-block costs, compresses
better, keeps the CPU pipeline full, and unlocks SIMD. DuckDB, for example,
works in batches of 2,048 rows, ClickHouse up to ~65k, Lucene's posting blocks
are 256 docs, and our ANN index works best with clusters of around 100–200
documents. Every query plan has an optimal block size, but today they are all
constrained by the ANN primary index. A plan that wants blocks of thousands of
documents to keep the CPU saturated is still stuck at 100–200.

We've already documented how much this matters in turbopuffer. Our first version
of full-text search partitioned posting lists along ANN cluster boundaries, and
the median block held just ~1.5 postings. FTS v2reworked postingsinto fixed blocks of ~256, and the
index got 10x smaller and queries got up to 20x faster. Posting lists could do
that because they're stored separately and point at documents, so their layout
doesn't have to follow the clusters. Aggregations and other scans read the
documents themselves, and those are stored one block per cluster. As long as the
ANN address is the primary key, their block size is constrained to the cluster
size, even if they'd prefer something larger.

## RIP, primary vector index

The solution to these problems is simple: don't key on the ANN address. That is
precisely the change turbopuffer v3 makes. As you can imagine, it is not a
trivial change.

v3 is a new foundation that will unlock significant performance improvement on
all query plans, and we hit a major milestone earlier this month: 100% of CI
passes on turbopuffer v3. We started by focusing on correctness. Now we will
make it correctandfast. Watching benchmark numbers go down is great fun, so
we wanted to get you in at day zero of perf grinding. We will sharethe benchmarksin public over the coming weeks, as we work toward (and
beyond) performance parity before rolling out v3 to production.

## turbopuffer

turbopuffer is a fast search engine that hosts1T+documents, handles10M+ writes/s, and serves25k+ queries/s. We are ready for far more. We hope you'll trust us with your queries.

Get started
Company
Pricing
Merch
Press & media
System status
Support
Slack
Docs
Email
Sales
Follow
Blog
RSS
Events
© 2026 turbopuffer Inc.
Terms of service
Data Processing Agreement
Privacy Policy
Security & Compliance
Docs search
esc

## Guides

Quickstart
Get started with turbopuffer in minutes
Vector Search
Perform approximate nearest neighbor searches
Full-Text Search
Learn how to use BM25 full-text search
Hybrid Search
Combine vector and full-text search strategies

## API Docs

Write
Create, update, or delete documents
Query
Query documents with filters and ranking
Overview
Authentication, headers, and request encoding
Namespace metadata
Get metadata about a namespace