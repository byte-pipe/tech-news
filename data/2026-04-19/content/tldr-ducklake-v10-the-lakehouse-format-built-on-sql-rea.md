---
title: 'DuckLake v1.0: The Lakehouse Format Built on SQL Reaches Production-Readiness – DuckLake'
url: https://ducklake.select/2026/04/13/ducklake-10/
site_name: tldr
content_file: tldr-ducklake-v10-the-lakehouse-format-built-on-sql-rea
fetched_at: '2026-04-19T11:34:46.224310'
original_url: https://ducklake.select/2026/04/13/ducklake-10/
author: The DuckDB team
date: '2026-04-19'
published_date: '2026-04-13T00:00:00+00:00'
description: We are happy to release DuckLake v1.0, a production-ready lakehouse format specification built on SQL. Its reference implementation, the ducklake DuckDB extension, is available as of today in DuckDB v1.5.2.
tags:
- tldr
---

# DuckLake v1.0: The Lakehouse Format Built on SQL Reaches Production-Readiness

The DuckDB team

2026-04-13

·

 23 min

TL;DR: We are happy to release DuckLake v1.0, a production-ready lakehouse format specification built on SQL. Its reference implementation, theducklakeDuckDB extension, is available as of today in DuckDB v1.5.2.

In May 2025, we published theDuckLake manifesto, where we explained what motivated us to work on DuckLake. Here's a quick recap: we basically outlined how, in our view, it makes much more sense to store all metadata of a lakehouse in adatabaserather than in scattered files in object storage. This is why we created DuckLake.

Themanifestois much more compelling, we recommend you read it!

Today, we are happy to announceDuckLake v1.0, almost a year after we released our first sketch of the specification. This is a production-ready release with guaranteed backward-compatibility. DuckLake v1.0 ships a stable specification, a feature-rich and fast reference implementation (the DuckDBducklakeextension), as well as a roadmap for future development.

## DuckLake at a Glance

If you're new here, you may be wondering: what is DuckLake? DuckLake is a lakehouse format, which allows you to store your data on object storage and access it as a database, similarly toDelta Lake with Unity CatalogandIceberg with Lakekeeper.

A key difference between other formats and DuckLake is that DuckLake stores all metadata in a database, which is commonly referred to as the catalog. This database can be any system that speaks SQL, supports primary keys and is able to persist data in tables. TheDuckLake specificationdefines the metadata tables needed for a specific version along with the supported data types and a reference on how to retrieve table metadata to perform operations on the lakehouse.

We also developed an implementation of the specification using DuckDB as the engine, the DuckDBducklakeextension. This extension implements all of the specification and supports three main catalogs: SQLite, PostgreSQL and DuckDB (yes, DuckDB can be a catalog too).

Over the last year, we kept working on the DuckLake specification internally and with the community. We enabledadding existing Parquet files without creating a deep copy, introducedIceberg compatibility, and rolled out support for thegeometryand thevarianttypes. We also released severalguidesandmigration scripts from DuckDB to DuckLake.

DuckLake unlocks several interesting use cases. Using theinliningfeature (using the catalog database to stage small updates) allows you tostream data into the data lake. Using its lightweight setup, you only need some storage and a public HTTPS endpoint to serve aread-only lakehouse without authentication. And in the context of DuckDB, it unlocks amultiplayersetup where multiple DuckDB instances can access the same DuckLake while coordinating through a central PostgreSQL catalog database.

## Adoption

We are delighted to see how quickly the community adopted DuckLake. TheducklakeDuckDB extension is now ranked among DuckDB'stop-10 core extensionsbased on the download statistics.

There are now DuckLake clients forApache DataFusion(byHotdata),Apache Spark(byMotherDuck) (byAndrew Witten),TrinoandPandas dataframe(mostly produced byagentic coding). MotherDuck also offers ahosted DuckLake service, where they manage both the catalog database and the data storage for you. Update (April 16): MotherDuck now supportsDuckLake v1.0.

We are very proud that DuckLake is already used in production at dozens of companies – see the collection of logos on ournew landing page. And there is even anO'Reilly DuckLake bookin the making!

For more DuckLake use cases and libraries, see theawesome-ducklake repository.

## What's New in DuckLake v1.0

First and foremost, DuckLake ships dozens of bugfixes to make the format robust for production deployments (see theappendix). We are particularly delighted that many contributions were made bycommunity membersand we would like to thank them for their work!

In the following, we show some key features of DuckLake v1.0 – available in theDuckDB v1.5.2that was also released today.

### Data Inlining

Data inlining is one of the flagship features of DuckLake. It basically enables performing small insert, delete and update operations in the catalog database, avoiding the proliferation of “the small file problem”. DuckLake v1.0 brings full inlining of updates and deletes. This feature is now on by default with a default threshold of 10 rows. If you want to find out more about this feature, head tothis blogwe published recently. In this example, we do an insert, delete and update and showcase how this does not create any new files in DuckLake. We thenCHECKPOINTto flush the inlined data to object storage.

CREATE
 
TABLE
 
lake.t
 
(
id
 
INT
,
 
status
 
VARCHAR
);

INSERT
 
INTO
 
lake.t
 
VALUES
 
(
1
,
 
'en route'
),
 
(
2
,
 
'shipped'
);

DELETE
 
FROM
 
lake.t
 
WHERE
 
id
 
=
 
1
;

UPDATE
 lake.t
 
SET
 
status
 
=
 
'delivered'
 
WHERE
 
id
 
=
 
2
;

FROM
 
ducklake_list_files
(
'lake'
,
 
't'
);
 
-- returns empty

CHECKPOINT
;
 
-- flushes data

### Sorted Tables

If you are often going to run queries against a high cardinality column, like an id or a timestamp, sorting is a great way to increase read query performance. Both row group and file pruning will be benefited for queries that push filters on the sorted keys. Sorted tables support column ordering but also arbitrary SQL expressions. The default approach will sort tables on compaction, flushing or insertion, but the latter one can be disabled to avoid hindering write performance.

CREATE
 
TABLE
 
lake.sorted_t
 
(
id
 
INT
,
 
payload
 
JSON
);

ALTER
 
TABLE
 
lake.sorted_t
 
SET
 
SORTED
 
BY
 
(
id
 
ASC
);

INSERT
 
INTO
 
lake.sorted_t
 

VALUES
 
 
(
33
,
 
{
'key'
:
 
'value'
}),

 
(
2
,
 
{
'key'
:
 
'value'
}),

 
(
42
,
 
{
'key'
:
 
'value'
}),

 
(
1
,
 
{
'key'
:
 
'value'
});

CHECKPOINT
;

FROM
 
lake.sorted_t
;

### Bucket Partitioning

Bucketing works by hashing the value of the target column and using the modulo, based on the number of buckets, to assign this value to a specific bucket. The bucket partitioning functionality uses the murmur3 hash implementation for full compatibility with Iceberg. If you want some of the benefits of partitioning but your column has a high cardinality, bucketing is a good alternative.

CALL
 
lake.
set_option
(
'data_inlining_row_limit'
,
 
0
);

CREATE
 
TABLE
 
lake.events
 
(

 
user_name
 
VARCHAR
,
 
event_type
 
VARCHAR
,
 
ts
 
TIMESTAMP
);

ALTER
 
TABLE
 
lake.events
 
SET
 
PARTITIONED
 
BY
 
(
bucket
(
8
,
 
user_name
));

INSERT
 
INTO
 
lake.events
 
VALUES

 
(
'alice'
,
 
'click'
,
 
'2024-01-01'
),

 
(
'bob'
,
 
'view'
,
 
'2024-01-01'
),

 
(
'charlie'
,
 
'click'
,
 
'2024-01-02'
);

EXPLAIN
 
ANALYZE
 
FROM
 
lake.events
 
WHERE
 
user_name
 
=
 
'alice'
;

### Type System: Geometry

Following up on the addition of theGEOMETRYdata type to DuckDB core, better geo stats have been enabled that allow for filter pushdown.GEOMETRYtypes can also now be nested in structs, lists and maps. In the following example, we showcase how a simple filter pushdown would work by using the&&operator, which checks overlapping bounding boxes of two geometries.

LOAD
 spatial
;

CALL
 
lake.
set_option
(
'data_inlining_row_limit'
,
 
0
);

CREATE
 
TABLE
 
lake.places
 
(
name
 
VARCHAR
,
 
location
 
GEOMETRY
);

INSERT
 
INTO
 
lake.places
 
VALUES
 
(
'Amsterdam'
,
 
ST_Point
(
4.9
,
 
52.37
));

INSERT
 
INTO
 
lake.places
 
VALUES
 
(
'London'
,
 
ST_Point
(
-0.12
,
 
51.51
));

SELECT
 
name

FROM
 
lake.places

WHERE
 
location

 
&&
 
ST_GeomFromText
(
'POLYGON((4 52, 5 52, 5 53, 4 53, 4 52))'
);

### Type System: Variant

Variant is a similar type to JSON but with some very distinctive qualities that make it a preferable alternative, namely: (i) it has support for many more types than JSON, for exampleDATEorTIMESTAMP; (ii) it is stored in a binary encoded format rather than a string; (iii) it can be shredded to primitive types, which allows for much better query performance (including filter and projection pushdown). We believeVARIANTwill eventually replaceJSONas the main type for semistructured data in database systems.

CREATE
 
TABLE
 
lake.events
 
(
id
 
INT
,
 
payload
 
VARIANT
);

INSERT
 
INTO
 
lake.events
 
VALUES
 
 
(
1
,
 
{
'user'
:
 
'alice'
,
 
'ts'
:
 
TIMESTAMP
 
'2024-01-01'
}),
 
 
(
2
,
 
{
'user'
:
 
'bob'
,
 
'ts'
:
 
TIMESTAMP
 
'2024-01-02'
,
 
'rand'
:
 
'value'
});

SELECT
 
*

FROM
 
lake.events

WHERE
 
payload.user
 
=
 
'bob'
;

### Deletion Vectors

Deletion vectors were introduced in the Iceberg v3 specification. While developing DuckLake we are also striving to keep compatibility with Iceberg at the data level. We therefore have implemented deletion vectors stored as Puffin files. These deletion vectors work in a similar way to delete files (which were already a part of the Iceberg specification).

This feature is experimental and we are planning some improvements for the upcoming DuckLake releases.

CREATE
 
TABLE
 
lake.t
 
(
id
 
INTEGER
);

CALL
 
lake.
set_option
(
'write_deletion_vectors'
,
 
true
,
 
table_name
 
=>
 
't'
);

INSERT
 
INTO
 
lake.t
 
FROM
 
range
(
100
);

DELETE
 
FROM
 
lake.t
 
WHERE
 
id
 
<
 
5
;

## The Future of DuckLake

Even though today we release DuckLake v1.0, the job is not yet done. We will continue releasing new DuckLake spec versions, and here we outline the current plans for DuckLake v1.1 and possible directions for DuckLake v2.0.

### DuckLake v1.1

There are two main features planned for DuckLake v1.1, which will require spec changes:

1. Variant Inlining.Currently, variant inlining only works for catalogs that natively support it (e.g., DuckDB). However, if the catalog does not support the Variant type, the table will never be inlined. We will design and implement the necessary specification changes that will allow this.
2. Multi-Deletion Vector Puffin Files.DuckLake v1.0 already supports single deletion vector puffin files, but we want to ensure that, similar to our current partial deletion files, DuckLake can store and read multiple deletion vectors in one file, thereby preserving time travel information while still minimizing the small file problem.

### DuckLake v2.0

DuckLake v2.0 is most likely not coming anytime soon, as we will focus on maturing our current feature set and guaranteeing the stability of our spec. Although we have a rough sense of the problems we want to tackle, community needs will also strongly drive our plans, so features may be added or reprioritized over time. Below is a list of the features we currently believe are important for DuckLake v2.0:

1. Git-like branching.Allowing users to create branches of their DuckLakes and merge changes between them. Similar to what Git is for code, but for data.
2. Permission-based roles.Defining roles and permissions to control access to DuckLake objects and operations. This is already possible by configuring Postgres and your S3 bucket correctly, but we want to make this easier to manage directly through DuckLake.
3. Incremental materialized views.Supporting materialized views that can be refreshed incrementally by applying tracked changes in DuckLake tables, rather than recomputing the full view.

## Conclusion

Today we released DuckLake v1.0, a stable specification for DuckLake, alongside the DuckDBducklakeextension compatible with this specification version. We are very happy with the progress that DuckLake has made in just one year, with some great community adoption and a great foundation for future improvements. If you want to hear more from the developers of DuckLake, make sure to check out ourpodcast episode on DuckLake v1.0:

## Appendix

This is all of the work that has gone into DuckLake since the v1.0 target was set; both from the community and the DuckDB Labs team. In this appendix we are listing 108 PRs that have been merged since the end of 2025. We have classified them so as to convey that the focus has always been making DuckLake stable and production ready, with 68 PRs merged focused on reliability and correctness, 12 focused on internal refactoring to lay the foundation for future developments and another 12 focused on performance improvements.

See the details of the release.

### User-Facing Features

PR

Title

Description

#642
 (@Alex-Monahan)

Ordered compaction and inlining

Data can now be sorted during compaction and when flushing inlined data using 
SET SORTED BY
 with column names

#743
 (@Alex-Monahan)

Sort expressions for compaction

SET SORTED BY
 now accepts arbitrary SQL expressions, not just column names; enables space-filling curve sorting for geo workloads

#780
 (@Alex-Monahan)

Sorted inserts

Inserts are automatically sorted when a table has 
SET SORTED BY
; can be disabled with 
sort_on_insert

#697
 (@pdet)

Automatic migration opt-in (
AUTOMATIC_MIGRATION
)

Attaching a newer DuckLake extension version no longer auto-migrates the catalog; migration is now explicit

#724
 (@pdet)

Settings function (
ducklake_settings()
)

New table function returning catalog DBMS type, extension version, and data path

#923
 (@pdet)

DATA_INLINING_ROW_LIMIT
 settable after attach

Inline row limit can be changed after attach and takes effect immediately

#775
 (@pdet)

Data inlining on by default

Small inserts (≤10 rows) stored inline in the catalog without configuration; includes full 
ALTER TABLE
 support for inlined tables

#737
 (@pdet)

Deletion inlining

Small deletes (≤ 
DATA_INLINING_ROW_LIMIT
) stored in catalog metadata instead of creating Parquet delete files

#877
 (@pdet)

Inline insertions in updates

UPDATE
 uses the inlining path when updated row count is within 
DATA_INLINING_ROW_LIMIT
; small updates no longer produce Parquet files

#734
 (@rgernhardt)

Maintenance functions return results

ducklake_flush_inlined_data
, 
ducklake_merge_adjacent_files
, and 
ducklake_rewrite_data_files
 now return result rows

#676
 (@Costa-SM)

Bucket transform table partitioning

Iceberg-compatible 
bucket(N, column)
 transform for partition pruning on high-cardinality columns; combinable with other partition transforms

#750
 (@Mytherin)

VARIANT type support

DuckLake tables support 
VARIANT
; shredded variant sub-fields get file statistics enabling file-skipping

#770
 (@Maxxen)

Geometry type improvements

GEOMETRY
 columns now store bounding-box stats per file; can be nested inside structs/lists/maps; supported in data inlining. Spatial file-level pruning is not yet implemented (TODO)

#878
 (@rgernhardt)

Metadata query logging

New 
DuckLakeMetadata
 log type records every metadata query with catalog, SQL text, and elapsed time

#910
 (@pdet)

Iceberg V3 deletion vectors (experimental)

Experimental read/write support for deletion vectors (roaring bitmaps in puffin files) as alternative to positional Parquet delete files

### Performance Improvements

PR

Title

Impact

#732
 (@rgernhardt)

COUNT(*)
 from metadata

COUNT(*)
 served from file row count stats instead of scanning Parquet files; 8×–258× speedup on S3-backed tables

#668
 (@redox)

Top-N dynamic filter file pruning

Uses min/max column statistics for more aggressive file skipping during query execution

#655
 (@utay)

Bulk delete API for orphaned file cleanup

More efficient cleanup of orphaned files via 
RemoveFiles
 bulk delete

#708
 (@pdet)

Remove 
partial_file_info
, replace with 
partial_max

Simpler schema for deletion tracking; reduces metadata size

#801
 (@suresh-summation)

Avoid parse-AST-serialize roundtrip in 
DuckLakeViewEntry::ToSQL()

~70× faster 
duckdb_views()
 queries

#806
 (@thalassemia)

More efficient 
AppendFiles

Avoids copying file vectors during bulk insert; reduces peak memory

#807
 (@thalassemia)

Use Appender API for DuckDB metadata writes

Dramatically faster bulk 
ducklake_add_data_files
; lower memory for large imports

#808
 (@thalassemia)

Eager/streaming metadata processing in 
add_data_files

Reduces peak memory for bulk imports with many files

#829
 (@jprafael)

Guard lock on all 
table_data_changes
 access

Prevents data races in concurrent write workloads

#868
 (@rgernhardt)

Cache 
GetInlinedDeletionTableName
 existence

Avoids extra metadata round-trip per query; critical for remote Postgres catalogs

#870
 (@jcolot)

Replace 
IN
 subqueries with 
LEFT JOIN
 in 
table_changes

Makes join strategy explicit; improves query plan predictability

#904
 (@rgernhardt)

Don't scan 
duckdb_tables()
 during Initialize

Faster attach; prevents failures caused by unrelated corrupted catalogs

### Reliability & Correctness

#### Concurrency & Transaction Safety

PR

Title

Impact

#846
 (@qsliu2017)

Fix inlined file deletes lost on concurrent commit retry

std::move
 emptied delete map on first attempt; retries silently lost deletions

#847
 (@pdet)

Fix 
BeginSnapshot
 for tables with different schema versions

Incorrect/errored reads across schema version boundaries

#897
 (@pdet)

Copy delete data to avoid snapshot_id corruption

Shared snapshot_id data mutated in-place during delete merges

#901
 (@pdet)

Make inline deletion flush retriable on conflict

Inlined data flush with concurrent writers could fail non-retriably

#906
 (@hello-world-bfree)

Detect concurrent insert+delete on same table

Silent duplicate rows in concurrent upsert workloads (MERGE INTO, delete-then-insert)

#920
 (@pdet)

Deterministic updates with duplicate row IDs

Non-deterministic update behavior when same row ID appeared multiple times in inlined data

#922
 (@pdet)

Fix local transaction deletion visibility

Deleted rows still visible within the same uncommitted transaction

#### Postgres & SQLite Catalog Backend

Fixes for non-DuckDB catalog backends. See also related refactoring (#748, #753, #754, #757) and performance (#868) work in their respective sections.

PR

Title

Impact

#849
 (@pdet)

Reinterpret BYTEA to Varchar for Postgres inlined data

Varchar stored as BYTEA in Postgres not correctly read back as VARCHAR

#903
 (@wideltann)

Escape single quotes in variant stats 
TrySerialize

SQL syntax error for variant stats when string values contained single quotes (Postgres catalogs)

#### Partitioning

PR

Title

Impact

#718
 (@pdet)

One compaction per partition group for rewrite

ducklake_rewrite_data_files
 generated wrong compaction plans for partitioned tables

#723
 (@pdet)

Add projection list with partitions to merge insert

INSERT INTO ... SELECT
 with MERGE missing columns on partitioned tables

#735
 (@gijshendriksen)

Fix 
add_data_files
 with multiple hive-partitioned columns

Failed with >1 hive partition column due to column ordering inconsistency

#764
 (@pdet)

Include identity columns with partitions

Identity/sequence columns omitted from partitioned table results

#811
 (@thalassemia)

Implicit cast + null for hive partition keys on Parquet import

add_data_files
 failed on non-VARCHAR partition columns; NULL partition keys unsupported

#812
 (@Mytherin)

Correctly handle NULL values in partitions

Internal error thrown when inserting NULL into a partition column

#850
 (@pdet)

Value comparison for boolean partition filters

Boolean partition filters used pointer comparison instead of value comparison

#856
 (@pdet)

merge_adjacent
 max option is global, not per-partition

max_file_count
 was evaluated per-partition instead of globally

#919
 (@pdet)

Fix inlined data flush over partitioned data

Inline delete flush not partition-aware; incorrect deletions on partitioned tables

#798
 (@pdet)

Skip hive partitioned columns from parquet files

Hive partition columns incorrectly read from Parquet data files

#992
 (@dentiny)

Fix duplicate partition key

Duplicate partition keys caused crash in copy-to-file operator

#### General

PR

Title

Impact

#675
 (@Costa-SM)

Fix integer underflow in value_count computation for nested columns

Incorrect statistics for nested column value counts

#682
 (@pdet)

Recursively normalize LIST child names from legacy formats

Compatibility with legacy Avro/Parquet formats

#689
 (@qsliu2017)

Implicit conversion unique_ptr in return

Build/type compatibility fix

#710
 (@pdet)

Fix change feed scan on compacted insertion files

Incorrect 
ducklake_table_changes()
 results on compacted tables

#711
 (@pdet)

Order deletions required for delete files

Positional delete files were incorrectly ordered

#714
 (@pdet)

Avoid extra column when doing type + extra change in same TX

Extra columns added when combining column type change with other changes

#715
 (@pdet)

Avoid double-adding inlined data stats

Stats counted twice for inlined data

#730
 (@pdet)

Fix autoload

DuckLake autoloading from DuckDB core was broken

#758
 (@Mytherin)

Fix deadlock in deletion inlining

Deadlock on nested DuckLake catalog metadata expansion

#768
 (@pdet)

Fix local transaction macro deletion

Macros created in local transactions not cleaned up on rollback

#772
 (@pdet)

Fix variant field order swap

Field ordering in variant types was incorrectly reversed

#822
 (@KumoSiunaus)

rewrite_data_files
 skips large files with delete files

Large files with delete files were silently skipped during rewrite

#839
 (@c-herrewijn)

delete_orphaned_files
 only deletes Parquet files

Could previously delete the catalog itself if it resided in the data path

#842
 (@jprafael)

Compaction handles 0-file output

Crash when all rows in a compaction source file had been deleted

#845
 (@pdet)

Fix table macro parsing

Table macros not parsed correctly in certain situations

#855
 (@pdet)

Reset view binding if binding fails

Failed views got stuck in broken state; all subsequent accesses threw misleading errors

#858
 (@pdet)

Update 
default_value_type
 in migration

Not updated after adding a column, causing downstream errors

#863
 (@pdet)

Cleanup separator in 
DATA_PATH

Trailing separator caused incorrect path construction

#866
 (@Flamefork)

Compaction ignores 
per_thread_output
 from lake config

Crash during compaction when 
per_thread_output
 was enabled lake-wide

#872
 (@pdet)

Fix schema + macro creation in same transaction

Creating schema and macro (or multiple macros) in same TX failed

#874
 (@pdet)

Fix S3 + 
disabled_filesystems = 'LocalFileSystem'

DuckLake failed on S3 when local FS was disabled

#896
 (@pdet)

DuckLake query plan serialization

Prepared statements and plan caching broken

#900
 (@pdet)

Generic catalog for view attach

Attaching DuckLake with views in non-default catalog failed

#914
 (@pdet)

Disallow reserved table names

Users could accidentally create tables conflicting with DuckLake internal names

#925
 (@pdet)

Fix missing mapping file when updating external file

Updates on external Parquet-backed tables failed due to missing row-ID mapping file

#926
 (@pdet)

Preserve original error at loading

Original attach/load error was swallowed and replaced with generic error

#765
 (@timbess)

Fix filter pushdown regression

Late materialization in optimizer bypassed DuckLake file-skipping filters

#799
 (@pdet)

Fixup error messages for migration

Confusing errors when catalog version mismatched

#939
 (@dentiny)

Fix rename failure exception message

Incorrect error message on rename failure

#941
 (@dentiny)

Fix SET NOT NULL error message

Incorrect error message for SET NOT NULL

#943
 (@dentiny)

Fix schema creation exception

Schema creation threw wrong exception type

#945
 (@dentiny)

Disallow column name to be internal name

Users could create columns conflicting with DuckLake internal column names

#958
 (@dentiny)

Fix drop table in single transaction

Dropping a table within the same transaction it was created failed

#960
 (@dentiny)

Fix dropping schema with table macros

Dropping a schema containing table macros failed

#962
 (@dentiny)

Fix repeated column update in one transaction

Multiple column updates in a single transaction produced incorrect results

#965
 (@dentiny)

Check transaction-local entities before drop

Dropping schema succeeded even when it contained transaction-local tables

#968
 (@dentiny)

Fix SQL string replacement for view

View catalog name placeholder replacement incorrect in certain cases

#972
 (@pdet)

Fixes for deletions

Missing directories for deletion files; broken name mapping for files without field_id; incorrect delete position during sorted inlining

#974
 (@dentiny)

Fix missing assignment for sort data

Sort data not propagated due to missing assignment in constructor

#976
 (@dentiny)

Delete deletion files for local table change

Deletion files not cleaned up for transaction-local table changes

#978
 (@pdet)

Attach or replace fix

ATTACH OR REPLACE
 not working correctly

#979
 (@pdet)

Fix migration issue of range tables from v0.3 to v0.4

Incorrect 
begin_snapshot
 for schema versions after migration

#981
 (@dentiny)

Fix multiple comments set in single transaction

Setting multiple comments in one transaction overwrote earlier ones

#985
 (@dentiny)

Fix macros cleanup on snapshot expiration

Macro-related tables not cleaned up during snapshot expiration

#987
 (@dentiny)

Cleanup variant stats table on compaction and snapshot expiration

Variant stats table rows not cleaned up during compaction/expiration

#989
 (@dentiny)

Fix set tag SQL

Setting a tag overwrote all key-value pairs for same table/column instead of just the matching key

#994
 (@dentiny)

Fix drop schema after no dependents

Drop schema incorrectly checked dropped tables instead of dropped views

### Internal Refactoring & Compatibility

PR

Title

Rationale

#657
 (@pdet)

Implement new checker for expressions as column defaults

Expression validation for column defaults

#671
 (@pdet)

Change schema tracking from global to table

Per-table schema isolation; cleaner catalog state management

#674
 (@redox)

Custom MultiFileReader for delete files

Improved efficiency in reading deletion information

#696
 (@pdet)

Partial deletion files and flushing

Supports partial deletion files; enables efficient flushing of accumulated deletion data

#742
 (@qsliu2017)

Metadata manager register refactor

Cleaner plugin architecture for multiple catalog backends

#748
 (@qsliu2017)

Refactor 
list_agg
 in queries

Postgres/SQLite compatibility in metadata queries

#753
 (@qsliu2017)

Inline data handling: decouple read vs. transform

Backend-specific type conversion; enables Postgres/SQLite inlining

#754
 (@qsliu2017)

Replace 
MAX_BY
 with 
DISTINCT ON ... ORDER BY

Postgres compatibility in catalog queries

#757
 (@qsliu2017)

Column aliases in internal queries

Prevents ambiguity in complex metadata joins

#786
 (@rgernhardt)

Default 
catalog_type
 to 
"duckdb"
 in settings

Consistent reporting across catalog backends

#803
 (@pdet)

Storage/catalog version field

Enables proper version-gated migrations

#827
 (@Mytherin)

Remove deprecated lambda syntax in 
add_data_files

Build/compatibility fix for updated DuckDB API

# Recent Posts

deep dive

### Data Inlining in DuckLake: Unlocking Streaming for Data Lakes

2026-04-02

Pedro Holanda

### Frozen DuckLakes for Multi-User, Serverless Data Access

2025-10-24

Mark Harrison (Madhive Data Engineering)

			All blog posts