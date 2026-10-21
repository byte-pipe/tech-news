---
title: Announcing DuckDB 2.0.0 LTS “Cinnamon Teal” – DuckDB
url: https://duckdb.org/2026/10/21/announcing-duckdb-200
site_name: hackernews_api
content_file: hackernews_api-announcing-duckdb-200-lts-cinnamon-teal-duckdb
fetched_at: '2026-10-21T22:06:17.894831'
original_url: https://duckdb.org/2026/10/21/announcing-duckdb-200
author: The DuckDB team
date: '2026-10-21'
published_date: '2026-10-21T00:00:00+00:00'
description: The DuckDB team is happy to announce that today we're releasing DuckDB version 2.0.0 LTS, codenamed “Cinnamon Teal” (Spatula cyanoptera). This is our biggest feature release so far, and it ships a polished version of the Quack protocol, asynchronous I/O, a first-class VARIANT type, agent mode, triggers, an extensible SQL parser and much more, built from close to 20,000 commits since DuckDB 1.5.
tags:
- hackernews
- trending
---

Search Shortcut 
cmd
 + 
k
 | 
ctrl
 + 
k

# Announcing DuckDB 2.0.0 LTS “Cinnamon Teal”

2026-10-21

14 min read

The DuckDB team

TL;DR: The DuckDB team is happy to announce that today we're releasing DuckDB version 2.0.0 LTS, codenamed “Cinnamon Teal” (Spatula cyanoptera). This is our biggest feature release so far, and it ships a polished version of the Quack protocol, asynchronous I/O, a first-classVARIANTtype, agent mode, triggers, an extensible SQL parser and much more, built from close to 20,000 commits since DuckDB 1.5.

We are proud to release DuckDB 2.0.0, codenamed“Cinnamon Teal”after theSpatula cyanoptera, a strikingly reddish-brown duck found in the western Americas.

WhileDuckDB 1.0was all about stability and backward compatibility, DuckDB 2.0 is above all a feature release.
In this blog post, we summarize the highlights and then walk through the breaking changes and how to migrate.
We showcased many of the new features in“A Preview of DuckDB v2.0”, which covers each one in more depth.
For the complete release notes, see therelease page on GitHub.

Tip To install the new version, please visit theinstallation page.
Some clients, such as the CLI and Python, are already available. Other client libraries (e.g., Go, R, Java) and some extensions can take a few days to release due to the extra changes and review rounds required.

With this release, there are currently three DuckDB lines available.
DuckDB 2.0 is a long-term support (LTS) release with support until at least October 2027.
The previous LTS release, version 1.4, is still supported until late November 2026.
To ensure a smooth transition and allow sufficient time for testing, we extended the support period of DuckDB 1.5 until March 2027, effectively also turning it into an LTS release.
For details, see therelease calendar.

To find your way around the documentation for all of the new features, we also published a“What's New in the Docs for 2.0”page that links each feature below to its documentation.

## DuckDB as a Server

DuckDB has been an in-process database since day one.
InDuckDB 1.5.3, released in May, we introduced the Quack protocol that lets you run DuckDB in a traditional client-server setup, along with thequackextension, which implements DuckDB's native protocol, so any DuckDB process canserve its databases.

### Quack andCONNECT

DuckDB 2.0.0 ships a polished version of the Quack protocol with substantial performance and stability improvements. It also introduces the newCONNECTstatementthat allows attaching and switching to a remote database in a single command for better ergonomics:

#### DuckDB server

CALL
 
quack_serve
(

 
token
 
=
 
'my_token'

);

CREATE
 
TABLE
 
events

 
(
date
 
DATE
,
 
name
 
VARCHAR
);

INSERT
 
INTO
 
events
 
VALUES

 
(
'2027-04-07'
,

 
'DuckCon #8'
);

 

quack:

#### DuckDB client

ATTACH
 
'quack:localhost'

 
AS
 
qk
 
(
TOKEN
 
'my_token'
);

CONNECT
 
qk
;

SELECT
 
*
 
FROM
 
events
;

┌────────────┬────────────┐

│
 
date
 
│
 
name
 
│

│
 
date
 
│
 
varchar
 
│

├────────────┼────────────┤

│
 
2027-04-07
 
│
 
DuckCon
 
#
8
 
│

└────────────┴────────────┘

 

For simplicity, this example runs the server and the client on the same machine. By default, the server only listens onlocalhost. To accept connections from other machines, keep the server onlocalhostand put it behind aTLS-terminating reverse proxy. Theallow_other_hostnameoption, which exposes the server directly, is only meant for testing.

TheCONNECTstatement is not limited to Quack: it points your session atany remote database that supports it, including PostgreSQL and MySQL. For these, the new remote pushdown optimizer ships queries directly to the remote server instead of pulling tables over the wire.

### Quack in the CLI

The CLI also has shortcuts for setting up a Quack client-server pair: the new-serveand-connectargumentsstart a Quack server or connect to one directly from the command line:

#### CLI server

duckdb
 
-serve

 

CREATE
 
TABLE
 
t
 
AS

 
SELECT
 
42
 
AS
 
x
;

 

quack:

#### CLI client

duckdb
 
-connect

 

FROM
 
t
;

┌───────┐

│
 
x
 
│

│
 
int32
 
│

├───────┤

│
 
42
 
│

└───────┘

 

## Performance

### Asynchronous I/O

DuckDB 2.0 introducesasynchronous I/Ofor reading Parquet and CSV files, as well asDuckDB's native storage format. The I/O layer now scales independently from the query processing layer, issuing reads in the background and keeping multiple requests in flight. This means far more parallelism for remote reads and dramatically faster queries on object storage such ass3://.

We described the design in detail in adedicated blog post.
In that post, we showed the network throughput over the course of a query with and without asynchronous I/O:

Network throughput. Higher utilization and shorter runtime are better.

### TheVARIANTType Becomes a First-Class Citizen

TheVARIANTtypestores semi-structured, schema-less data such as JSON while keeping the performance of columnar execution.
So you can think of it as JSON on steroids: aVARIANTcolumn can store differently shaped data in every row, but unlike JSON it is not a text format.

DuckDB 1.5 already introducedVARIANT, but DuckDB 2.0 fully integrates it. DuckDB 2.0 detects the common structure in your data and “shreds” it, so it compresses well and executes fast. The pipeline works end to end, from shredded execution straight out of storage to shreddedVARIANTreading and writing for Parquet, backed by a family ofvariant_*functions. For example:

CREATE
 
TABLE
 
events
 
(
payload
 
VARIANT
);

INSERT
 
INTO
 
events

VALUES

 
(
'{"user": {"id": 42, "tags": ["a", "b"]}}'
::
JSON
::
VARIANT
),

 
(
'{"event": "click", "x": 10, "y": 20}'
::
JSON
::
VARIANT
);

SELECT
 
variant_type
(
payload
),
 
variant_keys
(
payload
)

FROM
 
events
;

┌───────────────────────┬───────────────────────┐
│ variant_type(payload) │ variant_keys(payload) │
│ varchar │ varchar[] │
├───────────────────────┼───────────────────────┤
│ OBJECT │ [user] │
│ OBJECT │ [event, x, y] │
└───────────────────────┴───────────────────────┘

### Agent Mode in the CLI

Coding agents such as Claude Code, Codex and Cursor increasingly drive the DuckDB CLI on their users' behalf. The 2.0 CLI detects when it is being run by an agent and switches toagent mode: it prints compact Markdown tables instead of padded boxes, says clearly when a result was truncated, stops runaway queries early and reports errors as JSON.

Long-running SQL queries report their expected cost prior to running, so the agent can decide whether to wait. In our experiments on TPC-H, agent mode cut the amount of DuckDB output the model had to read by 59%. You can turn itonfor manual testing using the-agentflagor instruct your agent to turn itoffusing the-no-agentflag.

## Extensibility

### A Brand New SQL Parser

DuckDB has always used a parser derived from PostgreSQL's. In 2.0, our own modern, extensiblePEG-based parser, which debuted as an opt-in feature inDuckDB 1.5, becomes the default. Extensions can now hook into the grammar itself (an idea we first explored in ourresearch on runtime-extensible parsers), so expect extensions that expose entirely new SQL syntax. Error messages now come with precise source locations. For details, see thePEG parser documentation. The new parser is designed to be compatible with the old one, so you should not notice the swap. If you do, please file an issue. In the meantime, you can switch back to the old parser using thelegacy_parserextensionby runningSETenable_legacy_parser=true;.

The old parser had served DuckDB since its first commit in 2018. Its grammar was generated with YACC/Bison, which produces an LALR(1) parser, so as DuckSQL grew, even small additions could collide with existing rules and raiseshift/reduceorreduce/reduceconflicts. A PEG grammar avoids this by trying alternatives in the order they are written, so adding syntax no longer risks breaking unrelated rules. Python itself moved to a PEG-based parser inversion 3.9for the same flexibility.

### Write Extensions Once and Host Them Yourself

DuckDB 2.0 ships a revampedC API v2, which is considerably more powerful than its predecessor and exposes components such as file systems and table functions to extensions. Before marking it as stable, we would like to test it in the field, so please give it a try andsend us your feedback!

You can also register and host your own trusted extension repositories, so an organization can host and sign its own extensions and have them install and load just like the built-in ones:

SET
 
allow_extension_repositories
 
=
 
'allowed'
;

CREATE
 
EXTENSION
 
REPOSITORY
 
my_repo

 
WITH
 
PREFIX
 
'https://extensions.example.org'
;

INSTALL
 
AND
 
LOAD
 
my_ext
 
FROM
 
my_repo
;

A repository is a name, a URL prefix and one or more RSA public keys that are trusted to sign the extensions served from it. The prefix can point at anything DuckDB can read: a local path,https,s3, you name it. AtCREATEtime, DuckDB fetches the repository's public keys and pins them into the repository definition, printing each key's SHA-256 fingerprint so you can compare it against one published out of band.

This feature is still a work in progress and its syntax may change in future releases. For more details, see theExtension Repositories page.

### Core Extension Updates

DuckDB'score extensionsare also shipping several new features, fixes and performance optimizations. These are too numerous to all list here, so we only highlight a few of them and will cover them in dedicated blog posts in the coming weeks:

* We releasedDuckLake 1.1, including a new specification andreference implementation.
* TheIceberg extensionstrives to become a feature-complete implementation. To this end, it adds REST catalogATTACHoptionsthat derive a table's location from its namespace or load table metadata from themetadata-locationfile returned by the catalog. Further options control the URL prefix and the namespace separator.
* TheDelta extensioncan create Delta tables withCREATE TABLE(including partitioning and Delta table properties), supports time travel and improvesVARIANTsupport.

## SQL Features

### Triggers

DuckDB 2.0 delivers triggers: theCREATE TRIGGERstatementwithBEFOREandAFTERtriggers,FOR EACH ROWandFOR EACH STATEMENT, transition tables viaREFERENCING OLD/NEW TABLE, multiple triggers per event,RETURNINGon triggered tables andDROP TRIGGER. The classic use case is audit tables, where a trigger records what changed in response to a table modification. Some combinations, such asBEFORE ... FOR EACH ROWandUPDATE ... FOR EACH ROWtriggers, are not yet supported; see thelimitations.

CREATE
 
TRIGGER
 
trg_audit

 
AFTER
 
UPDATE
 
ON
 
target

 
REFERENCING

 
OLD
 
TABLE
 
AS
 
o

 
NEW
 
TABLE
 
AS
 
n

 
FOR
 
EACH
 
STATEMENT

 
INSERT
 
INTO
 
audit

 
SELECT
 
n.id
,
 
o.val
,
 
n.val

 
FROM
 
o
 
JOIN
 
n
 
ON
 
o.id
 
=
 
n.id
;

Triggers can also maintain materialized views incrementally! For example, to keep track of the average age of people per nationality in a tableage_statistics, you can use two triggers – one for insert and another for delete operations – and store the sum and the count alongside the average.

To see more details, click here.

CREATE
 
TABLE
 
people
 
(
name
 
VARCHAR
,
 
nationality
 
VARCHAR
,
 
age
 
INTEGER
);

CREATE
 
TABLE
 
age_statistics
 
(

 
nationality
 
VARCHAR
 
PRIMARY
 
KEY
,

 
sum_age
 
INTEGER
,

 
num_people
 
INTEGER
,

 
average_age
 
DOUBLE

);

 

On insertion, we aggregate the new rows per nationality and merge them intoage_statistics, adding a row for each new nationality:

CREATE
 
TRIGGER
 
people_insert

 
AFTER
 
INSERT
 
ON
 
people

 
REFERENCING
 
NEW
 
TABLE
 
AS
 
n

 
FOR
 
EACH
 
STATEMENT

 
MERGE
 
INTO
 
age_statistics
 
s

 
USING
 
(

 
SELECT
 
nationality
,
 
sum
(
age
)
 
AS
 
sum_age
,
 
count
(
*
)
 
AS
 
num_people

 
FROM
 
n

 
GROUP
 
BY
 
nationality

 
)
 
d

 
ON
 
s.nationality
 
=
 
d.nationality

 
WHEN
 
MATCHED
 
THEN
 
UPDATE
 
SET

 
sum_age
 
=
 
s.sum_age
 
+
 
d.sum_age
,

 
num_people
 
=
 
s.num_people
 
+
 
d.num_people
,

 
average_age
 
=
 
(
s.sum_age
 
+
 
d.sum_age
)
 
/
 
(
s.num_people
 
+
 
d.num_people
)

 
WHEN
 
NOT
 
MATCHED
 
THEN
 
INSERT

 
VALUES
 
(
d.nationality
,
 
d.sum_age
,
 
d.num_people
,
 
d.sum_age
 
/
 
d.num_people
);

 

On deletion, we subtract the deleted rows and drop a nationality once its last person has left:

CREATE
 
TRIGGER
 
people_delete

 
AFTER
 
DELETE
 
ON
 
people

 
REFERENCING
 
OLD
 
TABLE
 
AS
 
o

 
FOR
 
EACH
 
STATEMENT

 
MERGE
 
INTO
 
age_statistics
 
s

 
USING
 
(

 
SELECT
 
nationality
,
 
sum
(
age
)
 
AS
 
sum_age
,
 
count
(
*
)
 
AS
 
num_people

 
FROM
 
o

 
GROUP
 
BY
 
nationality

 
)
 
d

 
ON
 
s.nationality
 
=
 
d.nationality

 
WHEN
 
MATCHED
 
AND
 
s.num_people
 
=
 
d.num_people
 
THEN
 
DELETE

 
WHEN
 
MATCHED
 
THEN
 
UPDATE
 
SET

 
sum_age
 
=
 
s.sum_age
 
-
 
d.sum_age
,

 
num_people
 
=
 
s.num_people
 
-
 
d.num_people
,

 
average_age
 
=
 
(
s.sum_age
 
-
 
d.sum_age
)
 
/
 
(
s.num_people
 
-
 
d.num_people
);

 

Let's see people come and go:

INSERT
 
INTO
 
people
 
VALUES

 
(
'Alice'
,
 
'US'
,
 
34
),
 
(
'Bram'
,
 
'NL'
,
 
27
),
 
(
'Csilla'
,
 
'HU'
,
 
45
),

 
(
'Dave'
,
 
'US'
,
 
58
),
 
(
'Eva'
,
 
'NL'
,
 
19
),
 
(
'Femke'
,
 
'NL'
,
 
41
);

FROM
 
age_statistics
 
ORDER
 
BY
 
nationality
;

 

┌─────────────┬─────────┬────────────┬─────────────┐
│ nationality │ sum_age │ num_people │ average_age │
│ varchar │ int32 │ int32 │ double │
├─────────────┼─────────┼────────────┼─────────────┤
│ HU │ 45 │ 1 │ 45.0 │
│ NL │ 87 │ 3 │ 29.0 │
│ US │ 92 │ 2 │ 46.0 │
└─────────────┴─────────┴────────────┴─────────────┘

 

DELETE
 
FROM
 
people
 
WHERE
 
name
 
=
 
'Alice'
;

DELETE
 
FROM
 
people
 
WHERE
 
nationality
 
=
 
'HU'
;

FROM
 
age_statistics
 
ORDER
 
BY
 
nationality
;

 

┌─────────────┬─────────┬────────────┬─────────────┐
│ nationality │ sum_age │ num_people │ average_age │
│ varchar │ int32 │ int32 │ double │
├─────────────┼─────────┼────────────┼─────────────┤
│ NL │ 87 │ 3 │ 29.0 │
│ US │ 58 │ 1 │ 58.0 │
└─────────────┴─────────┴────────────┴─────────────┘

 

Triggers bring us one step closer to materialized views, a long-standing item in the“future work” section of our roadmap.

### SQL Dialect Additions

As always, DuckDB'sfriendly SQL dialectkeeps growing. A few favorites from this release cycle:

* The$variableshorthandlets you write$xin most places where an expression is allowed, instead ofgetvariable('x').
* Data-modifying CTEslet you useINSERT,UPDATE,DELETEandCOPYas pipeline steps.
* NEARESTjoinsturn top-k similarity search into a join clause, handy for vector and embedding workloads.
* Nested schemasallow schemas within schemas, e.g.,CREATE SCHEMA finance.reports.
* JSON mutation functionsjson_set,json_insert,json_replaceandjson_removereturn modified copies of JSON documents (see also ourblog post on JSON patches).

There is more: DuckDB 2.0.0 supports the SQL-standardFETCH FIRSTand allowsUNNESTin theGROUP BYclause. It also ensures well-definedMERGEandUPDATE ... FROMsemantics for cases when multiple rows are matched.

## Migrating to 2.0

DuckDB 2.0 comes with a small set of breaking changes. For most users, upgrading is straightforward, but complex deployments running many DuckDB processes need more care. The storage format is the most likely source of problems: DuckDB versions before 2.0 cannot read database files created by DuckDB 2.0. DuckDB 2.0 can still read and write your existing database files, and these remain readable by older versions. We recommend testing 2.0.0 on a shadow system before switching production over. And, if your workload is mission-critical, you may want to wait for the first patch release,coming in November.

For the full details, see themigration guide.

## Internals and Deprecations

### Compiler Requirements

Following DuckDB's long stint on C++11, DuckDB 2.0 nowrequires a C++17 compiler.

We also switched to Clang as the default compiler for our release builds. On Linux and macOS, both DuckDB and its core extensions are built with Clang. On Windows, the CLI is built with Clang, while most core extensions are still built with MSVC. We may move more Windows builds to Clang in the future, but this requires further changes.

### Timezones, Calendars and Collations Without ICU

Timezone-aware timestamps, calendars and collations have always been powered by the ICU library. In 2.0, the ICU library is gone entirely: theicuextensionnow implements timezones, calendars and collations itself, with the timezone data built directly from the IANA database and compressed down to around 45 kB.

Everything keeps working exactly as before, and the native implementation is also faster. If you find any issues, pleaselet us know!

### Deprecations

#### Lambda Syntax

The old single-arrow lambda syntax (x -> x + 1) is now disabled by default. Use the Python-style syntax instead:

SELECT
 
list_transform
([
1
,
 
2
,
 
3
],
 
lambda
 
x
:
 
x
 
+
 
1
);

You can temporarily re-enable the old syntax withSETlambda_syntax='enable_single_arrow';. Both the flag and the single-arrow syntax will be removed entirely in v2.1.

#### Amalgamation Builds

Theamalgamation build, which bundles DuckDB's entire source code into a single header and a single source file, is now deprecated. The amalgamation has grown too large to be realistically useful in most cases.

#### Gradual Phase-Out of macOS x86_64

We are gradually phasing outosx_amd64from the list of fully supportedplatforms.
For the time being, DuckDB andcore extensionsare still built and supported, butcommunity extensionsare no longer built for this platform. DuckDB 2.1 will stop supportingosx_amd64.

## Summary

These were a few highlights, but there are many more features and improvements in this release. There have been almost 20,000 commits by many contributors since DuckDB 1.5, shipping smaller features as well as performance and usability improvements. The fullrelease notes can be found on GitHub.

We would like to thank our community for the detailed issue reports and feedback that have driven this release, and our special thanks go to our contributors!

## Recent posts

All blog posts 

### Benchmarking DuckDB v2.0-dev on NVIDIA Vera

2026-10-16

3 min

Gábor Szárnyas

### From JSON Strings to Typed Columns

2026-10-16

6 min

The DuckDB team

### What Is Inside an Iceberg Table?

2026-10-13

12 min

The DuckDB team