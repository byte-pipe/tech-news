---
title: Polars — Pre-release of Polars 2.0
url: https://pola.rs/posts/announcing-polars-2/
site_name: hnrss
content_file: hnrss-polars-pre-release-of-polars-20
fetched_at: '2026-09-03T14:53:23.369981'
original_url: https://pola.rs/posts/announcing-polars-2/
date: '2026-09-03'
description: Preview of Python Polars 2.0, bringing the streaming engine to all lazy queries
tags:
- hackernews
- hnrss
---

Back to blog

 

# Pre-release of Polars 2.0

 

ByRitchie Vinkon Wed, 2 Sept 2026

 
 
 
 
 
 
 
 
 

Today we are releasing the first release candidate for Polars 2.0. The definite 2.0 release will land in the following weeks. We don’t aim to make a big feature release of Polars 2.0. In fact we hope it to be a boring experience for you. The reason we bump this major version is that we can get rid of design decisions made in the past that currently block us and then we want to change defaults to more sensible settings that will benefit a greater audience. The biggest default change will be that allLazyFramequeries now will run on the streaming engine. Casual Polars users can therefore expect huge improvements in memory usage and performance. In aggregate we expect the streaming engine to be easily5x faster.

To help users transition to 2.0, we have posted a fullmigration guide. This post will cover a few of the highlights.

## Streaming engine as default

This is the biggest impact change of 2.0. Callingcollecton aLazyFramewill now default to the streaming engine, leading to massive memory and performance improvements on most queries for users. The reason this required a major version bump is that the streaming engine doesn’t guarantee row-order by default for certain operations (join,group_by,unpivot, etc.). If you require observable row-order in those operations, you can opt in to that by settingmaintain_order=True.

For users who want to keep using the “in-memory” engine as default, they can do so by setting the engine affinity.

lf 
=
 pl
.
LazyFrame
({
"k"
: [
2
, 
1
, 
0
], 
"v"
: [
"a"
, 
"b"
, 
"c"
]})

other 
=
 pl
.
LazyFrame
({
"k"
: [
0
, 
1
, 
2
], 
"r"
: [
"x"
, 
"y"
, 
"z"
]})

# 2.0: engine="auto" now resolves to the streaming engine.

# Row order is no longer guaranteed for joins, group_by, unpivot, ...

(

 lf

 .
join
(other, on
=
"k"
, how
=
"left"
)

 .
collect
()

)

# ┌─────┬─────┬─────┐

# │ k ┆ v ┆ r │ <- order may not match `lf`'s original row order

# └─────┴─────┴─────┘

# Opt in to observable order for this query:

(

 lf

 .
join
(other, on
=
"k"
, how
=
"left"
, maintain_order
=
"left"
)

 .
collect
()

)

# Or keep the old in-memory engine as the default, process-wide:

pl
.
Config
.
set_engine_affinity
(
"in-memory"
)

# ...or per query:

(

 lf

 .
join
(other, on
=
"k"
, how
=
"left"
)

 .
collect
(engine
=
"in-memory"
)

)

## Stricter Polars

Polars aims to be strict and fail fast. Errors should ideally raise up-front, not 20 minutes into a pipeline. Implicit behavior on data-mismatches should be opt-in, not a default, since those mismatches can hide bugs. This strictness has become even more valuable with the rise of AI-driven development. Agents can validate a query’s structure early by callingcollect_schema(), which resolves types and catches schema-level mismatches without materializing any data. This ensures fast feedback for the agents, meaning they can iterate faster. Not all errors can be caught during compilation of the query plan, some depend on data. In these cases Polars defaults to stricter behavior to ensure inconsistencies are caught instead of silently producing different results.

Below are a few examples where Polars has gotten more strict:

### is_inlossless type-coercion

If you run anis_inexpression on different data-types, Polars used to cast both types to their common supertype, even if that conversion was lossy
Below is an example with user-ids that can go wrong by silent data-type mismatches.

# Checking if a user ID matches a list of "flagged" account IDs

# (flagged_ids loaded from a JSON export, where large IDs became floats)

flagged_ids 
=
 pl
.
Series
([
9007199254740992.0
])

user_id 
=
 pl
.
Series
([
9007199254740993
])
 # Int64 -> a different ID, off by 1

user_id
.
is_in
(flagged_ids)

Before 2.0,user_idgets coerced toFloat64to matchflagged_ids. But 9007199254740993 sits above 2^53 (9007199254740992), the largest integer float64 can represent exactly, so it silently rounds down to 9007199254740992.0, giving a false positive.

In 2.0 this raises:InvalidOperationError: 'is_in' cannot check for Int64 values in List(Float64) data., users should explicitly cast to deal with lossy type conversion.

### Strict concatenation

Horizontal concat will now check lengths instead of silently filling withnull.

# Joining per-day transaction counts with per-day fraud-flag counts,

transactions 
=
 pl
.
DataFrame
({
"day"
: [
1
, 
2
, 
3
, 
4
, 
5
], 
"count"
: [
120
, 
98
, 
143
, 
87
, 
156
]})

# Upstream job for day 5 failed silently

fraud_flags 
=
 pl
.
DataFrame
({
"flagged"
: [
2
, 
0
, 
5
, 
1
]})
 # only 4 rows

pl
.
concat
([transactions, fraud_flags], how
=
"horizontal"
)

shape: (5, 2)

┌─────┬───────┬─────────┐

│ day ┆ count ┆ flagged │

│ 1 ┆ 120 ┆ 2 │

│ 2 ┆ 98 ┆ 0 │

│ 3 ┆ 143 ┆ 5 │

│ 4 ┆ 87 ┆ 1 │

│ 5 ┆ 156 ┆ null │ <- day 5 silently has no flag count

└─────┴───────┴─────────┘

In 2.0 this will raise with:

ShapeError: cannot concat dataframes with different heights in 'strict' mode

If padding is what you wanted, you have to explicitly opt-in to that withhow="horizontal_extend". Making that intention clear to the reader.

### Removal of casts in favor of dedicated methods/constructors

Another one worth mentioning is the removal of many casts that were ambiguous or should be applied via their dedicated parsing expression, leading to one obvious way to parse data.

#### Enums/Categoricals <> integers.

pl
.
Series
([
None
, 
1
, 
0
, 
2
], dtype
=
pl.UInt32).
cast
(pl.
Enum
([
"a"
, 
"b"
, 
"c"
]))

# ComputeError: casting from u32 to enum is not supported.

Use instead:.cat.to(dtype)for int → categorical,.cat.physical()for categorical → int.

#### Parsing Strings to temporal data-types

pl
.
Series
([
"2022-08-30"
]).
cast
(pl.Date)

# InvalidOperationError: casting from string to date is not supported.

Use instead:.str.to_date()/.str.to_datetime(). These allow you to apply a parsing format, giving you more control over how the data is parsed.

These were just a few examples, but we landed many more strictness improvements. See them all in the migration guide.

## Raising informative errors

We put a lot of effort into making sure you as user or your agent can continue if you used old parameters that are not supported anymore. We added two new typed exceptions for this;polars.exceptions.AttributeRemovedErrorandpolars.exceptions.ArgumentRemovedErrorthat handle removed attributes and methods and removed parameters respectively.

The error messages should point you to the new API instead. Below we show two examples.

>>>
 lf
.
melt
(id_vars
=
"a"
, value_vars
=
"b"
)

polars
.
exceptions
.
AttributeRemovedError
:
 `melt` was removed 
in
 version 
2.0
;

use `LazyFrame
.
unpivot` instead
,
 with
 `index` instead of `id_vars`

and
 `on` instead of `value_vars`

>>>
 df
.
join
(df, on
=
"a"
, join_nulls
=
True
)

polars
.
exceptions
.
ArgumentRemovedError
:
 the argument 
'join_nulls'
 for

'DataFrame.join'
 was deprecated 
in
 version 
1.24
 and
 has been removed

in
 2.0
.
0
.
 It was renamed to 
'nulls_equal'
 in
 version 
2.0
.

Most of the removed functionality has been deprecated for a long time and hopefully should not have affected your pipelines if you have stayed up to date. Reach out to us if you think we should have kept some functionality you relied on.

## Last words

Polars 2.0 is about better defaults (most importantly the streaming engine) and a better API. We hope this release is rather boring. We don’t gate new features behind major version bumps as we ship them as soon as their ready.

Don’t be mistaken, Polars 2.x will be much better than 1.x. There is a lot in flight that we haven’t talked publicly enough: proper out-of-core support for the streaming engine, a new IO-plugin design, what we think will be the fastest S3 reader out there, major SQL coverage improvements, a cost-based planner, join reordering, and the removal of mmap, which will make our pipelines fully async end to end.

Try the release candidate by installingpip install polars==2.0rc1. Give it a spin and reach out to us here:https://github.com/pola-rs/polars/issuesor contact us on discord:https://discord.gg/4UfP5cfBE7.