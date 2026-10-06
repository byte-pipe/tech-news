---
title: Polars — Release of Polars 2.0
url: https://pola.rs/posts/release-polars-2/
site_name: hnrss
content_file: hnrss-polars-release-of-polars-20
fetched_at: '2026-10-06T17:04:45.935828'
original_url: https://pola.rs/posts/release-polars-2/
date: '2026-10-06'
description: DataFrames for the new era
tags:
- hackernews
- hnrss
---

Back to blog

 

# Release of Polars 2.0

 

ByRitchie Vinkon Tue, 6 Oct 2026

 
 
 
 
 
 
 
 
 

Today we are shipping Polars 2.0. In the earlier announcement post we went through the rationale of the version bump. This post we will discuss what features 2.0 brings. Even though we didn’t intend to make it a big feature release, it still packs a lot to get enthousiastic about.

Let’s go through the highlights of this release:

* our initial version of out-of-core (spill-to-disk) support is enabled,
* a lot of very core performance improvements,
* first class SQL support, which together with the performance improvements hasPolars leading DataFusion and DuckDB in TPC-H and TPC-DS1benchmarks,
* a newMapdtype, and
* stricter Polars on dtypes and explicitness, leading to faster feedback, and faster AI iteration.

## Performance and SQL as a first class citizen

Polars 2.0 will be the marking point where we will treat SQL as first class citizen. Polars SQL coverage has increased dramatically over last few months. We know we have been building a solid engine for the last couple of years. In Polars 2.0, we want to enable that to more workloads, including SQL. To make this performant, we shipped many improvements to our optimizer and engine. The highlights here join reordering, much better common-subplan-elimination and dynamic predicates/bloom filters.

To see how we perform on typical SQL benchmarks, we ran Polars SQL on data derived from TPC-H and TPC-DS1and ran it against the latest DuckDB release (1.5.6), DuckDB 2.0 alpha (2.0.0.dev2610011535) and the latest DataFusion release (54.0.0) on a c7a.4xlarge (16 vCPUs, 32GB RAM) and a c7a.metal (192 vCPUs, 384GB RAM). Every query ran 5 times in a hot setting, with a separate process per query and a 60 second timeout. The file cache was cleared between each engine/benchmark (not between queries). For every query we take the best of the 5 runs, and we compare engines on both the sum and the geometric mean of those query times.

The data is generated withtpcgen-cli parquetcompiled from source on commit99bedae. We looked at the default row-group sizes oftpcgen-cliand confirmed they are roughly similar to what Polarsscan_csvpiped throughsink_parquetand DuckdbCOPYproduce. The SQL queries were generated with DuckDB 1.5.6’stpch_queries()andtpcds_queries(). The data was stored on EBS.

The charts below show the runtime of each engine in seconds (lower is better), split by machine.

c7a.4xlarge (16 vCPUs, 32 GB)

c7a.metal (192 vCPUs, 384 GB)

Polars and both DuckDB versions completed all queries. DataFusion timed out on TPC-DS q72 (and once on q67) and ran out of memory on TPC-H q18 on c7a.4xlarge; those queries are excluded from the results above for all engines.

We observe that default Polars is fastest on all but one benchmarks. Polars has a constant overhead when we scale to 192 threads, which hurts small data queries. In fact we see that Polars limited to 32 cores is competitive or winning in all benchmarks. We have diagnosed the cause on our end and will hopefully fix this problem in the next release. More information on the benchmarks can be found in theappendix. We encourage you to replicate our results and have shared a repository for this benchmark here:https://github.com/pola-rs/polars-2.0-benchmark.

## Streaming engine and OOC as default

This is the one of the biggest impact changes of 2.0. Callingcollecton aLazyFramewill now default to the streaming engine, leading to massive memory and performance improvements on most queries. The reason this required a major version bump is that the streaming engine doesn’t guarantee row-order by default for certain operations (join,group_by,unpivot, etc.). If you require observable row-order in those operations, you can opt in to that by settingmaintain_order=True.

Out-of-core (spill to disk) is now enabled by default. It starts spilling at ~80% of RAM (this may need tuning). Operations that support out-of-core at this moment (sort, window functions, many expressions) can now start spilling to disk to finish a query. The default disk budget is 64GB. In the coming time we will enable out-of-core for joins and group-by’s as well.

These two changes will make Polars much more resillient in high-memory workloads for casual data practicioners. And with out-of-corejoinandgroup-byon our roadmap, this resilience will improve even more.

## New Map datatype

Polars now supports the ArrowMapTypedirectly as a PolarsMapdtype. You can think of aMapas a Python dictionary, mapping keys to values. Before 2.0 the ArrowMapTypewas read in Polars asList(Struct({"key": ..., "value": ...})).

df 
=
 pl
.
DataFrame
(

 {

 "user"
: [
"alice"
, 
"bob"
, 
"carol"
],

 "scores"
: pl.
Series
(

 [{
"math"
: 
90
, 
"art"
: 
75
}, {
"math"
: 
60
}, {}],

 dtype
=
pl.
Map
(pl.String, pl.Int64),

 ),

 "subject"
: [
"art"
, 
"art"
, 
"math"
],

 }

)

shape: (3, 3)

┌───────┬─────────────────────────┬─────────┐

│ user ┆ scores ┆ subject │

│ --- ┆ --- ┆ --- │

│ str ┆ map[str, i64] ┆ str │

╞═══════╪═════════════════════════╪═════════╡

│ alice ┆ {"math": 90, "art": 75} ┆ art │

│ bob ┆ {"math": 60} ┆ art │

│ carol ┆ {} ┆ math │

└───────┴─────────────────────────┴─────────┘

# Key lookups and dictionary-like methods:

df
.
select
(

 "user"
,

 pl.
col
(
"scores"
).map.
get
(
"math"
).
alias
(
"math"
), 
# fixed key

 pl.
col
(
"scores"
).map.
get
(pl.
col
(
"subject"
)).
alias
(
"by_subject"
), 
# key from another column

 pl.
col
(
"scores"
).map.
contains_key
(
"art"
).
alias
(
"has_art"
),

 pl.
col
(
"scores"
).map.
len
().
alias
(
"n"
),

 pl.
col
(
"scores"
).map.
keys
().
alias
(
"keys"
),

 pl.
col
(
"scores"
).map.
values
().
alias
(
"values"
),

)

┌───────┬──────┬────────────┬─────────┬─────┬─────────────────┬───────────┐

│ user ┆ math ┆ by_subject ┆ has_art ┆ n ┆ keys ┆ values │

│ --- ┆ --- ┆ --- ┆ --- ┆ --- ┆ --- ┆ --- │

│ str ┆ i64 ┆ i64 ┆ bool ┆ u32 ┆ list[str] ┆ list[i64] │

╞═══════╪══════╪════════════╪═════════╪═════╪═════════════════╪═══════════╡

│ alice ┆ 90 ┆ 75 ┆ true ┆ 2 ┆ ["math", "art"] ┆ [90, 75] │

│ bob ┆ 60 ┆ null ┆ false ┆ 1 ┆ ["math"] ┆ [60] │

│ carol ┆ null ┆ null ┆ false ┆ 0 ┆ [] ┆ [] │

└───────┴──────┴────────────┴─────────┴─────┴─────────────────┴───────────┘

As a supported dtype, the map type will now have dedicated expressions, like key lookups, iteration over values and other dictionary like methods.

## Stricter Polars

Polars aims to be strict and fail fast. Errors should ideally raise up-front, not 20 minutes into a pipeline. Implicit behavior on data-mismatches should be opt-in, not a default, since those mismatches can hide bugs. This strictness has become even more valuable with the rise of AI-driven development. Agents can validate a query’s structure early by callingcollect_schema(), which resolves types and catches schema-level mismatches without materializing any data. This ensures fast feedback, meaning agents and humans can iterate faster. Not all errors can be caught during compilation of the query plan, some depend on data. In these cases Polars defaults to stricter behavior to ensure inconsistencies are caught instead of silently producing different results. Seeprevious posts) with some examples in where Polars has gotten more strict.

## Last words

We are very excited that Polars 2.0 is out. Coming months we’ll improve on the road were in. Better out-of-core, better scaling at large CPU-counts and on Polars Cloud we aim to be the fastest distributed engine available. We also started working on GeoPolars and hope to deliver more news on this soon.
If you find any problem with our new release, please open an issue:https://github.com/pola-rs/polars/issues. And finally, to help you with upgrading to 2.0, we have postedmigration guide.

## Benchmark Appendix

The absolute numbers (in seconds) are below. The bold number is the fastest engine in each row; the darker the shading, the slower an engine is compared to the fastest. Polars with 32 threads was only run on c7a.metal.

Sum of query times

Geometric mean of query times

Polars also scales well with more cores on larger data. Moving from 16 to 192 vCPUs at SF100 makes Polars 3.8x faster on TPC-H and 2.2x faster on TPC-DS (by sum), compared to 3.2x and 1.9x for DuckDB 1.5.6, 2.2x and 1.5x for the DuckDB 2.0 alpha, and 1.7x and 1.0x for DataFusion. At SF10 the extra cores don’t help Polars with its default settings: it is equally fast on TPC-H and 1.8x slower on TPC-DS, while DuckDB 1.5.6 still gets 1.8x and 1.3x faster. Polars with 32 threads only ran on the c7a.metal, so it is not part of this comparison.

## Footnotes

1. These benchmarks are derived from TPC-H and TPC-DS Benchmarks and as such any results obtained are not comparable to published TPC-H and TPC-DS Benchmark results, as the results obtained do not comply with the TPC-H and TPC-DS Benchmarks.↩↩2