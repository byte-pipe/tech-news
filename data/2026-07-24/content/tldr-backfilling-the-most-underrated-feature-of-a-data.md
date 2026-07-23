---
title: 'Backfilling: the most underrated feature of a data pipeline'
url: https://thesis.optoinvest.com/posts/backfilling-most-underrated-feature/
site_name: tldr
content_file: tldr-backfilling-the-most-underrated-feature-of-a-data
fetched_at: '2026-07-24T05:40:02.968733'
original_url: https://thesis.optoinvest.com/posts/backfilling-most-underrated-feature/
date: '2026-07-24'
description: 'Backfilling: the most underrated feature of a data pipeline (11 minute read)'
tags:
- tldr
---

# Backfilling: the most underrated feature of a data pipeline

Most data organizations design for one direction of time: forward. When a pipeline goes live, its job is to ingest whatever shows up - new filings, new prices, new transactions. That part gets attention, dashboards, and service level agreements. What gets far less attention is everything that existed before the pipeline did.

Backfilling is the feature that lets you give that same attention to the rest of your data. In my experience, teams often treat it as an afterthought patched on during a crisis. I decided to design for it from day one, and it’s made a real difference in how much time we spend fighting our own pipeline.

## What we mean by backfilling

Backfilling shows up in two forms, and they often get conflated.

The first is historical ingestion: loading data that already exists in the world as if you had been collecting it all along. Form ADV is a good example - the SEC has published decades of investment adviser filings. Backfilling here means treating 24 years of history with the same rigor as tomorrow’s filing, not as a one-time bulk import that gets “special-cased” and forgotten.

The second is migration: moving data that already lives in one of your own systems into a new one. This is the kind of backfill most engineers have scar tissue from. Organizations sink enormous budgets into “migrations,” and they are almost always painful, rarely fully complete, and leave behind a trail of engineers who never want to touch that codebase again.

I treat both as the same underlying problem, and that changes how you build.

## Migration code is production code

Our pipeline runs in three stages - extract, raw, transform. Extract pulls the filings as-is from the SEC. Raw lands them in table form, no cleanup. Transform is where we apply the cleaning, modeling, and merge logic that turns raw filings into usable data. It is these three stages that allow us to ingest from multiple sources, including backfilling historical data.

Engineers’ usual intuition when backfilling is to write a separate script, because it feels like a one-off job. They assume it’ll be quick and easy. Typically, the script walks through history, does its thing, and gets deleted - or, more realistically, gets left in a scripts/ folder to rot. Sound familiar?

That intuition is exactly what makes backfills fragile. The logic that ran once, under pressure, has never been tested with the same rigor as your production pipeline.

Instead, the incremental pipeline and the backfill should be treated as the same pipeline, not just similar ones. A config flag changes what data it looks at, not how it processes that data.

At Opto, we run this on Dagster, and its run config has been the mechanism that makes this practical. Our transform layer for Form ADV takes the same config object:

class
 
FormAdvTransformConfig
(
Config
):

 
full_refresh
:
 
bool
 
=
 
False

 
refresh_crd
:
 
list
[
str
]
 
|
 
None
 
=
 
None

From that object, we resolve one of three modes:

def
 
get_mode_from_config
(
config
:
 
FormAdvTransformConfig
)
 
->
 
FormAdvTransformMode
:

 
if
 
config
.
refresh_crd
:

 
return
 
FormAdvTransformMode
.
REFRESH_SINGLE

 
if
 
config
.
full_refresh
:

 
return
 
FormAdvTransformMode
.
FULL_REFRESH

 
return
 
FormAdvTransformMode
.
INCREMENTAL

Incremental- process only what changed since the last run. The default, and the cheapest.

Full refresh- rebuild everything from raw. This is our backfill: a schema change, a recovery, or genuinely loading history for the first time.

Single entity- reprocess one specific record on demand. Invaluable when a customer asks “why does this look stale?” and you need an answer in ten seconds, not a full pipeline run.

## Why this matters: the transform logic never has to know why it’s running

The contract is simple: regardless of mode, the output is always the same shape - batches of keys to process.

def
 
get_crds_to_process
(
config
,
 
session
)
 
->
 
list
[
list
[
str
]]:

 
if
 
config
.
refresh_crd
:

 
return
 
[
config
.
refresh_crd
]

 
if
 
config
.
full_refresh
:

 
all_crds
 
=
 
query_all_crds
(
session
)

 
return
 
chunk_into_batches
(
all_crds
,
 
batch_size
=
5000
)

 
crds
 
=
 
query_crds_with_source_date
(
session
,
 
partition_date
)

 
return
 
chunk_into_batches
(
crds
,
 
batch_size
=
5000
)

The transform loop downstream doesn’t branch on mode at all:

crd_batches
 
=
 
get_crds_to_process
(
config
,
 
session
)

for
 
batch_num
,
 
crd_batch
 
in
 
enumerate
(
crd_batches
):

 
process_batch
(
crd_batch
,
 
session
)

Once or forty thousand times, the loop runs the same processing logic either way. The code path you verify against a single CRD in refresh_crd mode is the same code path that runs against all 1.8M rows in a full refresh. There’s no separate “backfill logic” to have less confidence in.

## Backfills are safe because time is bi-temporal

None of this works if re-running a backfill can silently overwrite or corrupt what’s already there - that’s where bi-temporality does the heavy lifting (we won’t bore you with it again, seeThe two clocks your data needs). Every write carries a business time and a system time, so re-running a backfill just opens new system-time versions instead of destroying history:

session
.
write_to_ducklake
(

 
data
=
df
,

 
schema_name
=
"transform"
,

 
table_name
=
"form_adv_firm_identity"
,

 
mode
=
"bi-temporal-merge"
,

 
key_columns
=
[
"firm_crd_number"
],

 
value_columns
=
[
"legal_name"
,
 
"business_name"
,
 
...
],

 
date_column
=
"filing_date"
,

)

## Analyzing the results with MotherDuck

Once you have a system that’s resilient and keeps everyone on one standardized approach instead of a dozen ad hoc ones, you get to spend more time actually analyzing the data instead of babysitting the pipeline. For that, we have a secret weapon: the MotherDuck MCP server.

As mentioned above, raw is where the source dataset lands in table format with zero assumptions - the data as we received it. Some would call it bronze → silver → gold - I’m not the biggest fan of that framing, since it’s really a dbt-influenced convention that assumes your data already lives in table format. I think that assumption doesn’t hold for us - but that’s not the point of this post.

As mentioned above, raw is where the source dataset lands in table format with zero assumptions - the data as we received it. Some would call this bronze → silver → gold instead of extract → raw → transform - I’m not the biggest fan of that framing, since it’s really a dbt-influenced convention that assumes your data already lives in table format. I think that assumption doesn’t hold for us, but that’s not the point of this post.)

The goal for “raw” is simple: get the source dataset into table format with zero assumptions - the data as we received it.

A simple prompt gets us started: “Use the MotherDuck MCP server, focus on my database shared_sec_lakehouse_prod and the table transform.form_adv_firm_ownership, and analyze my data.”

### Key Observations

* The data is freshly full-refreshed - all 1.8M rows share the samesystem_valid_from(2026-07-04), indicating a recent full pipeline run.
* Ownership status is highly fragmented - 309 distinct values, many being comma-joined multi-role combinations. The top status categories (Member, Shareholder, Managing Member) account for <30% of non-null rows; 48% are null. This is a normalization opportunity if needed downstream.
* Temporal depth is excellent - 26 years of history with clear open/close patterns tracking real ownership changes over time.
* The volume growth trend is healthy - ownership records opened per year grew from ~30k in 2002 to ~114k in 2024, reflecting both market growth and improved SEC reporting requirements post-2012.

From there, we can push further and build on what the data already tells us: “Is there any data quality issues worth highlighting? Incompatible temporal rows? Duplicate rows? Empty rows that pollute the table?”

A few snippets of the answer:

### Temporal Gaps Between Versions - 8,137 cases

When an owner disappears and then reappears for the samefirm_crd_number+owner_key, there’s a gap between thevalid_toof the prior record andvalid_fromof the next.

Root cause breakdown:

* 82% have a differentvalue_hash- the person genuinely left and returned with updated data (name change, new role, etc.). Example: owner_key A1B2C3 closed under one name in 2001, then reappeared under a different name in 2024 - same owner_key, resolved via the pipeline’s person-matching logic. These are not bugs - they’re real-world ownership changes.
* 18% (1,441) have an identicalvalue_hash- the owner disappeared from one filing then reappeared unchanged in a later filing. These are likely SEC reporting gaps (a missed annual amendment, or a filing irregularity). The close/reopen accurately reflects what the SEC published.

Verdict: mostly inherent to the source data, not a pipeline bug. The 1,441 same-hash reappearances could be smoothed (treat as continuous if the gap is below a threshold), but that’s a design decision about whether to trust the SEC’s filing gaps or interpolate over them.

### Summary Scorecard

Dimension
Grade
Notes
Uniqueness
A
Zero duplicates on any key combination
Temporal integrity
A-
No overlaps; 8,137 gaps are source-inherent
Completeness (keys)
A
100% populated on firm_crd, owner_key, owner_name, owner_type
Completeness (values)
B
ownership_status 48% null, entity_in_which 76% null
Freshness
A
Data current through May 2026
Normalization
B-
ownership_status highly fragmented; entity identifiers only 73% coverage
Referential integrity
A
Zero orphans relative to firm_identity

The table is well-built. The issues are mostly inherent to SEC form data quality rather than pipeline bugs.

This is what lets us ship faster and with more confidence: instead of a data engineer manually profiling a 1.8M-row table by hand, we asked the MotherDuck MCP server and got the scorecard above back in minutes.

## The real payoff

A resilient pipeline is what buys us that time in the first place - time we can spend more productively analyzing the data. Paired with the MotherDuck MCP server, that combination has saved us a ton of time: we ship faster, and with more confidence in what we’re shipping.

For disclaimers, visithttps://www.optoinvest.com/disclaimers.

PUBLISHED ONJul 20, 2026Lucie Thimus