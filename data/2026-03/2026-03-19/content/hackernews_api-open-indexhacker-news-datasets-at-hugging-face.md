---
title: open-index/hacker-news · Datasets at Hugging Face
url: https://huggingface.co/datasets/open-index/hacker-news
site_name: hackernews_api
content_file: hackernews_api-open-indexhacker-news-datasets-at-hugging-face
fetched_at: '2026-03-19T11:17:39.194340'
original_url: https://huggingface.co/datasets/open-index/hacker-news
author: tamnd
date: '2026-03-14'
description: We’re on a journey to advance and democratize artificial intelligence through open source and open science.
tags:
- hackernews
- trending
---

Dataset Viewer
 
 
 
 

The dataset viewer should be available soon. Pleaseretry later.

 
 
 
 
 
 
 

# Hacker News - Complete Archive

Every Hacker News item since 2006, live-updated every 5 minutes

## What is it?

This dataset contains the completeHacker Newsarchive: every story, comment, Ask HN, Show HN, job posting, and poll ever submitted to the site. Hacker News is one of the longest-running and most influential technology communities on the internet, operated byY Combinatorsince 2007. It has become the de facto gathering place for founders, engineers, researchers, and technologists to share and discuss what matters in technology.

The archive currently spans from2006-10to2026-03-19 11:10 UTC, with47,328,806 itemscommitted. New items are fetched every 5 minutes and committed directly as individual Parquet files through an automated live pipeline, so the dataset stays current with the site itself.

We believe this is one of the most complete and regularly updated mirrors of Hacker News data available on Hugging Face. The data is stored as monthly Parquet files sorted by item ID, making it straightforward to query with DuckDB, load with thedatasetslibrary, or process with any tool that reads Parquet.

## What is being released?

The dataset is organized as one Parquet file per calendar month, plus 5-minute live files for today's activity. Every 5 minutes, new items are fetched from the source and committed directly as a single Parquet block. At midnight UTC, the entire current month is refetched from the source as a single authoritative Parquet file, and today's individual 5-minute blocks are removed from thetoday/directory.

data/
 2006/2006-10.parquet first month with HN data
 2006/2006-12.parquet
 2007/2007-01.parquet
 ...
 2026/2026-03.parquet most recent complete month
 2026/2026-03.parquet current month, ongoing til 2026-03-18
today/
 2026/03/19/00/00.parquet 5-min live blocks (YYYY/MM/DD/HH/MM.parquet)
 2026/03/19/00/05.parquet
 ...
 2026/03/19/11/10.parquet most recent committed block
stats.csv one row per committed month
stats_today.csv one row per committed 5-min block

Along with the Parquet files, we includestats.csvwhich tracks every committed month with its item count, ID range, file size, fetch duration, and commit timestamp. This makes it easy to verify completeness and track the pipeline's progress.

## Breakdown by today

The chart below shows items committed to this dataset by hour today (2026-03-19,4,462 itemsacross12 hours, last updated2026-03-19 11:15 UTC).

 00:00 ██████████████████████████████ 514
 01:00 █████████████████████████░░░░░ 432
 02:00 ████████████████████████████░░ 483
 03:00 ███████████████████████░░░░░░░ 409
 04:00 ██████████████████████░░░░░░░░ 377
 05:00 ████████████████████░░░░░░░░░░ 344
 06:00 ████████████████████░░░░░░░░░░ 359
 07:00 ██████████████████████░░░░░░░░ 391
 08:00 ██████████████████████░░░░░░░░ 383
 09:00 █████████████████████░░░░░░░░░ 375
 10:00 ██████████████████░░░░░░░░░░░░ 313
 11:00 ████░░░░░░░░░░░░░░░░░░░░░░░░░░ 82

## Breakdown by year

The chart below shows items committed to this dataset by year.

 2006 █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 62
 2007 █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 93.8K
 2008 ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 320.9K
 2009 ███░░░░░░░░░░░░░░░░░░░░░░░░░░░ 608.4K
 2010 ██████░░░░░░░░░░░░░░░░░░░░░░░░ 1.0M
 2011 ████████░░░░░░░░░░░░░░░░░░░░░░ 1.4M
 2012 ██████████░░░░░░░░░░░░░░░░░░░░ 1.6M
 2013 █████████████░░░░░░░░░░░░░░░░░ 2.0M
 2014 ███████████░░░░░░░░░░░░░░░░░░░ 1.8M
 2015 █████████████░░░░░░░░░░░░░░░░░ 2.0M
 2016 ████████████████░░░░░░░░░░░░░░ 2.5M
 2017 █████████████████░░░░░░░░░░░░░ 2.7M
 2018 ██████████████████░░░░░░░░░░░░ 2.8M
 2019 ████████████████████░░░░░░░░░░ 3.1M
 2020 ████████████████████████░░░░░░ 3.7M
 2021 ███████████████████████████░░░ 4.2M
 2022 █████████████████████████████░ 4.4M
 2023 ██████████████████████████████ 4.6M
 2024 ████████████████████████░░░░░░ 3.7M
 2025 █████████████████████████░░░░░ 3.9M
 2026 ██████░░░░░░░░░░░░░░░░░░░░░░░░ 943.4K

## How to download and use this dataset

You can load the full dataset, a specific year, or even a single month. The dataset uses the standard Hugging Face Parquet layout, so it works out of the box with DuckDB, thedatasetslibrary,pandas, andhuggingface_hub.

### Using DuckDB

DuckDB can read Parquet files directly from Hugging Face without downloading anything first. This is the fastest way to explore the data:

Thetypecolumn is stored as a small integer:1= story,2= comment,3= poll,4= pollopt,5= job. The"by"column (author username) must be quoted in DuckDB becausebyis a reserved keyword.

-- Top 20 highest-scored stories of all time

SELECT
 id, title, "by", score, url, 
time

FROM
 read_parquet(
'hf://datasets/open-index/hacker-news/data/*/*.parquet'
)

WHERE
 type 
=
 
1
 
AND
 title 
!=
 
''

ORDER
 
BY
 score 
DESC

LIMIT 
20
;

-- Monthly submission volume for a specific year

SELECT

 strftime(
time
, 
'%Y-%m'
) 
AS
 
month
,
 
count
(
*
) 
AS
 items,
 
count
(
*
) 
FILTER
 (
WHERE
 type 
=
 
1
) 
AS
 stories,
 
count
(
*
) 
FILTER
 (
WHERE
 type 
=
 
2
) 
AS
 comments

FROM
 read_parquet(
'hf://datasets/open-index/hacker-news/data/2024/*.parquet'
)

GROUP
 
BY
 
month

ORDER
 
BY
 
month
;

-- Most discussed stories by total comment count

SELECT
 id, title, "by", score, descendants 
AS
 comments, url

FROM
 read_parquet(
'hf://datasets/open-index/hacker-news/data/2025/*.parquet'
)

WHERE
 type 
=
 
1
 
AND
 descendants 
>
 
0

ORDER
 
BY
 descendants 
DESC

LIMIT 
20
;

-- Who posts the most Ask HN questions?

SELECT
 "by", 
count
(
*
) 
AS
 posts

FROM
 read_parquet(
'hf://datasets/open-index/hacker-news/data/*/*.parquet'
)

WHERE
 type 
=
 
1
 
AND
 title 
LIKE
 
'Ask HN:%'

GROUP
 
BY
 "by"

ORDER
 
BY
 posts 
DESC

LIMIT 
20
;

-- Track how often a topic appears on HN over time

SELECT

 
extract
(
year
 
FROM
 
time
) 
AS
 
year
,
 
count
(
*
) 
AS
 mentions

FROM
 read_parquet(
'hf://datasets/open-index/hacker-news/data/*/*.parquet'
)

WHERE
 type 
=
 
1
 
AND
 
lower
(title) 
LIKE
 
'%rust%'

GROUP
 
BY
 
year

ORDER
 
BY
 
year
;

-- Top linked domains, year over year

SELECT

 
extract
(
year
 
FROM
 
time
) 
AS
 
year
,
 regexp_extract(url, 
'https?://([^/]+)'
, 
1
) 
AS
 domain,
 
count
(
*
) 
AS
 stories

FROM
 read_parquet(
'hf://datasets/open-index/hacker-news/data/*/*.parquet'
)

WHERE
 type 
=
 
1
 
AND
 url 
!=
 
''

GROUP
 
BY
 
year
, domain
QUALIFY 
row_number
() 
OVER
 (
PARTITION
 
BY
 
year
 
ORDER
 
BY
 stories 
DESC
) 
<=
 
5

ORDER
 
BY
 
year
, stories 
DESC
;

### Usingdatasets

from
 datasets 
import
 load_dataset

# Stream the full history without downloading everything first

ds = load_dataset(
"open-index/hacker-news"
, split=
"train"
, streaming=
True
)

for
 item 
in
 ds:
 
print
(item[
"id"
], item[
"type"
], item[
"title"
])

# Load a specific year into memory

ds = load_dataset(
 
"open-index/hacker-news"
,
 data_files=
"data/2024/*.parquet"
,
 split=
"train"
,
)

print
(
f"
{
len
(ds):,}
 items in 2024"
)

# Load today's live blocks (updated every 5 minutes)

ds = load_dataset(
 
"open-index/hacker-news"
,
 name=
"today"
,
 split=
"train"
,
 streaming=
True
,
)

### Usinghuggingface_hub

from
 huggingface_hub 
import
 snapshot_download

# Download only 2024 data (about 1.5 GB)

snapshot_download(
 
"open-index/hacker-news"
,
 repo_type=
"dataset"
,
 local_dir=
"./hn/"
,
 allow_patterns=
"data/2024/*"
,
)

For faster downloads, installpip install huggingface_hub[hf_transfer]and setHF_HUB_ENABLE_HF_TRANSFER=1.

### Using the CLI

# Download a single month

huggingface-cli download open-index/hacker-news \
 data/2024/2024-01.parquet \
 --repo-type dataset --local-dir ./hn/

### Using pandas + DuckDB

import
 duckdb

conn = duckdb.connect()

# Score distribution: what does a "typical" HN story look like?

# type=1 is story (stored as integer: 1=story, 2=comment, 3=poll, 4=pollopt, 5=job)

df = conn.sql(
"""

 SELECT

 percentile_disc(0.50) WITHIN GROUP (ORDER BY score) AS p50,

 percentile_disc(0.90) WITHIN GROUP (ORDER BY score) AS p90,

 percentile_disc(0.99) WITHIN GROUP (ORDER BY score) AS p99,

 percentile_disc(0.999) WITHIN GROUP (ORDER BY score) AS p999

 FROM read_parquet('hf://datasets/open-index/hacker-news/data/*/*.parquet')

 WHERE type = 1

"""
).df()

print
(df)

## Dataset statistics

You can query the per-month statistics directly from thestats.csvfile included in the dataset:

SELECT
 
*
 
FROM
 read_csv_auto(
'hf://datasets/open-index/hacker-news/stats.csv'
)

ORDER
 
BY
 
year
, 
month
;

Thestats.csvfile tracks each committed month with the following columns:

Column

Description

year
, 
month

Calendar month

lowest_id
, 
highest_id

Item ID range covered by this file

count

Number of items in the file

dur_fetch_s

Seconds to fetch from the data source

dur_commit_s

Seconds to commit to Hugging Face

size_bytes

Parquet file size on disk

committed_at

ISO 8601 timestamp of when this month was committed

## Content breakdown

Hacker News has five item types. The vast majority of content is comments, followed by stories (which include Ask HN, Show HN, and regular link submissions). Jobs, polls, and poll options make up a small fraction.

Type

Count

Share

comment

41,317,357

87.2%

story

6,040,377

12.7%

job

18,071

0.0%

poll

2,240

0.0%

pollopt

15,449

0.0%

Of all stories submitted to Hacker News,84.8%link to an external URL. The rest are text-only posts: Ask HN questions, Show HN launches, and other self-posts where the discussion itself is the content.

The average story generates23.9 commentsin its discussion thread. The most-discussed story of all time received 9,275 comments, which gives a sense of how deep conversations can go on particularly controversial or interesting topics.

### Story scores

Scores on Hacker News follow a steep power law. Most stories receive only a few points, but a small number break out and reach the front page with hundreds or thousands of upvotes.

Metric

Value

Average score

1.5

Median score

0

Highest score ever

6,015

Stories with 100+ points

175,903

Stories with 1,000+ points

2,169

The median score of 0 reflects the fact that many stories are submitted but never gain traction. However, the long tail is where things get interesting: over 6,040,377 stories have been submitted, and the top 0.03% (those with 1,000+ points) represent the content that defined conversations across the technology industry.

### Most-shared domains

The domains most frequently linked from Hacker News stories tell a clear story about what the community values. GitHub dominates, reflecting HN's deep roots in open source and software development. Major publications like the New York Times and Ars Technica show the community's interest in journalism and long-form analysis.

#

Domain

Stories

1

github.com

197,669

2

www.youtube.com

134,831

3

medium.com

124,544

4

www.nytimes.com

77,678

5

en.wikipedia.org

54,401

6

techcrunch.com

54,185

7

twitter.com

50,542

8

arstechnica.com

47,066

9

www.theguardian.com

44,304

10

www.bloomberg.com

37,798

### Most active story submitters

These are the users who have submitted the most stories over the lifetime of Hacker News. Many of them have been active for over a decade, consistently curating and sharing content with the community.

#

User

Stories

1

rbanffy

36,778

2

Tomte

26,183

3

tosh

24,062

4

bookofjoe

20,588

5

mooreds

20,368

6

pseudolus

19,909

7

PaulHoule

19,025

8

todsacerdoti

18,880

9

ingve

17,056

10

thunderbong

15,978

11

jonbaer

14,167

12

rntn

13,410

13

doener

12,806

14

Brajeshwar

12,346

15

LinuxBender

11,058

## How it works

The pipeline is built in Go and usesDuckDBfor Parquet conversion. Historical data is sourced fromClickHouse; live data is fetched directly from theHN Firebase API.

Historical backfill.The pipeline iterates through every month from October 2006 to the most recent complete month. For each month, it queries the ClickHouse source with a time-bounded SQL query, exports the result as a Parquet file sorted byidusing DuckDB with Zstandard compression at level 22, and commits it to this repository along with an updatedstats.csvandREADME.md. Months already tracked instats.csvare skipped, making the process fully resumable.

Live polling.Every 5 minutes, the pipeline calls the HN Firebase API to fetch new items by ID range. Items are grouped into their 5-minute time windows, written as individual Parquet files attoday/YYYY/MM/DD/HH/MM.parquetusing DuckDB, and committed to Hugging Face immediately. Using the HN API directly means live blocks reflect real-time data with no indexing lag.

Day rollover.At midnight UTC, the entire current month is refetched from the ClickHouse source in a single query and written as an authoritative Parquet file. Today's individual 5-minute blocks are deleted from the repository in the same atomic commit. Refetching instead of merging ensures the monthly file is always complete and deduplicated, regardless of any local state.

## Thanks

The data in this dataset comes from theClickHouse Playground, a free public SQL endpoint maintained byClickHouse, Inc.that mirrors the officialHacker News Firebase API. ClickHouse uses Hacker News as one of their canonical demo datasets. Without their public endpoint, building and maintaining a complete, regularly updated archive like this would not be practical.

The original content is created by the Hacker News community and is operated byY Combinator. This is an independent mirror and is not affiliated with or endorsed by Y Combinator or ClickHouse, Inc.

# Dataset card for Hacker News - Complete Archive

## Dataset summary

This dataset is a complete mirror of theHacker Newsarchive, sourced from theClickHouse Playgroundwhich itself mirrors the officialHN Firebase API. The data covers every item ever posted to the site, from the earliest submissions in October 2006 through today.

The dataset is intended for research, analysis, and training. Common use cases include:

* Language model pretraining and fine-tuningon high-quality technical discussions
* Sentiment and trend analysisacross two decades of technology discourse
* Community dynamics researchon one of the internet's most influential forums
* Information retrievalbenchmarks using real-world questions and answers
* Content recommendationand ranking model development

## Dataset structure

### Data instances

Here is an example item from the dataset. This is a story submission with a link to an external URL:

{

 
"id"
:
 
1
,

 
"deleted"
:
 
0
,

 
"type"
:
 
1
,

 
"by"
:
 
"pg"
,

 
"time"
:
 
"2006-10-09T18:21:51+00:00"
,

 
"text"
:
 
""
,

 
"dead"
:
 
0
,

 
"parent"
:
 
0
,

 
"poll"
:
 
0
,

 
"kids"
:
 
[
15
,
 
234509
,
 
487171
]
,

 
"url"
:
 
"http://ycombinator.com"
,

 
"score"
:
 
57
,

 
"title"
:
 
"Y Combinator"
,

 
"parts"
:
 
[
]
,

 
"descendants"
:
 
0
,

 
"words"
:
 
[
"y"
,
 
"combinator"
]

}

And here is a comment, showing how discussion threads are connected via theparentfield:

{

 
"id"
:
 
15
,

 
"deleted"
:
 
0
,

 
"type"
:
 
2
,

 
"by"
:
 
"sama"
,

 
"time"
:
 
"2006-10-09T19:51:01+00:00"
,

 
"text"
:
 
"\"the way to get good software is to find ..."
,

 
"dead"
:
 
0
,

 
"parent"
:
 
1
,

 
"poll"
:
 
0
,

 
"kids"
:
 
[
17
]
,

 
"url"
:
 
""
,

 
"score"
:
 
0
,

 
"title"
:
 
""
,

 
"parts"
:
 
[
]
,

 
"descendants"
:
 
0
,

 
"words"
:
 
[
]

}

### Data fields

Every Parquet file shares the same schema, matching theHN APIitem format:

Column

Type

Description

id

uint32

Unique item ID, monotonically increasing across the entire site

deleted

uint8

1 if the item was soft-deleted by its author or by moderators, 0 otherwise

type

int8

Item type as an integer: 
1
=story, 
2
=comment, 
3
=poll, 
4
=pollopt, 
5
=job

by

string

Username of the author who created this item. Note: 
by
 is a reserved word in DuckDB and must be quoted as 
"by"

time

timestamp

When the item was created, in UTC

text

string

HTML body text. Used for comments, Ask HN posts, job listings, and polls

dead

uint8

1 if the item was flagged or killed by moderators, 0 otherwise

parent

uint32

The ID of the parent item. For comments, this points to either a story or another comment

poll

uint32

For poll options (
pollopt
), the ID of the associated poll

kids

list<uint32>

Ordered list of direct child item IDs (typically comments)

url

string

The external URL for link stories. Empty for text posts and comments

score

int32

The item's score (upvotes minus downvotes)

title

string

Title text for stories, jobs, and polls. Empty for comments

parts

list<uint32>

For polls, the list of associated poll option item IDs

descendants

int32

Total number of comments in the entire discussion tree below this item

words

list<string>

Tokenized words extracted from the title and text fields

### Data splits

Thedefaultconfiguration includes all historical monthly Parquet files. If you only need today's latest items, use thetodayconfiguration which includes only the 5-minute live blocks for the current day.

You can also load individual years or months by specifyingdata_files:

# Load just January 2024

ds = load_dataset(
"open-index/hacker-news"
, data_files=
"data/2024/2024-01.parquet"
, split=
"train"
)

# Load all of 2024

ds = load_dataset(
"open-index/hacker-news"
, data_files=
"data/2024/*.parquet"
, split=
"train"
)

## Dataset creation

### Curation rationale

Hacker News is one of the richest sources of technical discussion on the internet, but accessing the full archive programmatically has historically required either scraping the Firebase API item-by-item or working with incomplete third-party dumps. This dataset provides the complete archive in a standard, efficient format that anyone can query without setting up infrastructure.

By publishing on Hugging Face with Parquet files, the data becomes immediately queryable with DuckDB (viahf://paths), streamable with thedatasetslibrary, and downloadable in bulk. The 5-minute live update pipeline means researchers always have access to near-real-time data.

### Source data

All data is sourced from theClickHouse Playground, a public SQL endpoint maintained by ClickHouse that mirrors the official Hacker News Firebase API. The ClickHouse mirror is widely used for analytics demonstrations and contains the complete dataset.

The pipeline queries the ClickHouse endpoint month-by-month, exports each month as a Parquet file using DuckDB with Zstandard compression at level 22, and commits it to this Hugging Face repository. Already-committed months are tracked instats.csvand skipped on subsequent runs, making the process fully resumable.

### Data processing steps

The pipeline runs in three modes:

1. Historical backfill.Iterates through every month from October 2006 to the most recent complete month. For each month, it runs a SQL query against the ClickHouse source, writes the result as a Parquet file sorted byid, and commits it to Hugging Face along with an updatedstats.csvandREADME.md.
2. Live polling.After the historical backfill completes, the pipeline polls theHN Firebase APIevery 5 minutes for new items. It fetches all items with IDs greater than the last committed watermark, groups them into 5-minute time windows by item timestamp, and writes each window as atoday/YYYY/MM/DD/HH/MM.parquetfile committed to Hugging Face immediately. The HN API provides real-time data with no indexing lag.
3. Day rollover.At midnight UTC, the entire current month is refetched from the ClickHouse source in a single query and written as a fresh, authoritative Parquet file. Today's individual 5-minute blocks are deleted from the repository in the same atomic commit. This approach is more reliable than merging local blocks — the result is always complete and deduplicated, sourced directly from the origin.

All Parquet files useZstandard compression at level 22and are sorted byidfor efficient range scans. No filtering, deduplication, or transformation is applied to the data beyond what the source provides.

### Personal and sensitive information

This dataset contains usernames (byfield) and user-generated text content (text,titlefields) as they appear on the public Hacker News website. No additional PII processing has been applied. The data reflects what is publicly visible onnews.ycombinator.com.

If you find content in this dataset that you believe should be removed, please open a discussion on the Community tab.

## Considerations for using the data

### Social impact

By providing the complete Hacker News archive in an accessible format, we hope to enable research into online community dynamics, technology trends, and the evolution of technical discourse. The dataset can serve as training data for language models that need to understand technical discussions, or as a benchmark for information retrieval and recommendation systems.

### Discussion of biases

Hacker News has a well-documented set of community biases. The user base skews heavily toward software engineers, startup founders, and technology enthusiasts based in the United States. Topics related to Silicon Valley, programming languages, startups, and certain political viewpoints tend to receive disproportionate attention and engagement.

The moderation system (flagging, vouching, and moderator intervention) shapes what content survives and what gets killed. Stories and comments that violate community norms are flagged asdead, but this moderation reflects the values of the existing community rather than any objective standard.

We have not applied any additional filtering or quality scoring to the data. All items, including deleted and dead items, are preserved exactly as they appear in the source.

### Known limitations

* typeis an integer.The item type is stored as a TINYINT enum:1=story,2=comment,3=poll,4=pollopt,5=job. When writing DuckDB queries, useWHERE type = 1for stories rather thanWHERE type = 'story'.
* byis a reserved keyword in DuckDB.Always quote it with double quotes:"by".
* deletedanddeadare integers.They are stored as 0/1 rather than booleans.
* Comment text is HTML.Thetextfield contains raw HTML as stored by HN, not plain text. You may need to strip tags depending on your use case.
* Deleted items have sparse fields.When an item is deleted, most fields become empty, but theidanddeletedflag are preserved.
* Scores are point-in-time snapshots.The score reflects the value at the time the ClickHouse mirror last synced, not necessarily the final score.
* No user profiles.This dataset contains items only, not user profiles (karma, bio, etc.).
* Code content is HTML-escaped.Code snippets in comments use HTML entities and<code>tags rather than Markdown formatting.

## Additional information

### Licensing

The dataset is released under theOpen Data Commons Attribution License (ODC-By) v1.0. The original content is subject to the rights of its respective authors. Hacker News data is provided byY Combinator.

This is an independent community mirror. It is not affiliated with or endorsed by Y Combinator.

### Contact

For questions, feedback, or issues, please open a discussion on theCommunity tab.

Last updated: 2026-03-19 11:15 UTC

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Downloads last month
 
 
1,426