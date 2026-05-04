---
title: Polars — Handling Schema Issues in Polars
url: https://pola.rs/posts/schema-evolution/
site_name: tldr
content_file: tldr-polars-handling-schema-issues-in-polars
fetched_at: '2026-05-05T00:51:33.562552'
original_url: https://pola.rs/posts/schema-evolution/
date: '2026-05-05'
description: DataFrames for the new era
tags:
- tldr
---

Back to blog

 

# Handling Schema Issues in Polars

 

ByThijs Nieuwdorpon Thu, 30 Apr 2026

 
 
 
 
 
 
 
 
 

You’ve built your data pipeline, and it runs without problems for months.
Until one day it fails.
The logs show a schema error traced back to a column that was added upstream.

Schema changes come in four shapes: a new column appears, an expected column disappears, a column’s type drifts, or a column is renamed, repurposed, or cast to an incompatible type.
The right fix depends on the shape and the storage format.
This post maps each shape to the Polars parameter that handles it, across CSV, multi-file Parquet, Delta Lake, and Apache Iceberg.

## The Four Shapes of Schema Change

Schema changes differ in kind.
Identifying the shape tells you which parameters to work with.

1. Additive.A new column appears in incoming data that was not present before.
Old records lack the column. New records carry it.
2. Subtractive.A column the schema expected is absent in one or more files or batches.
The column still exists in your expected schema. The data no longer provides it.
3. Type drift.A column exists in all sources but its dtype changed.
For example, an integer column widens fromInt32toInt64as the source data grows.
4. Breaking.A column is renamed, semantically repurposed, or cast to an incompatible type.
No parameter handles this automatically.
Fix them explicitly before reading or writing.

The table below maps each shape to the parameter that handles it, by format.
Note that we’ve excluded CSV: it has no embedded type metadata, so the problem there reduces to type inference, covered in the next section.

Shape
Multi-file Parquet (read)
Delta (write)
Iceberg (write)
Additive
schema={…}
 + 
missing_columns="insert"
schema_mode="merge"
update_schema()
Subtractive
missing_columns="insert"
schema_mode="merge"
update_schema()
Type drift
ScanCastOptions(integer_cast="upcast")
explicit cast
update_schema()
*
Breaking
explicit cast/rename
explicit cast/rename
rename: 
update_schema()
. Incompatible type: explicit cast

* Iceberg supports lossless type widening throughupdate_schema(). Type narrowing still requires explicit handling.

### CSV

CSV files carry no embedded schema.
Instead, Polars samples the first 100 rows to infer a dtype for every column and parse the schema this way.
If a value later in the file contradicts the inferred type, aComputeErroris raised at collect time:

import
 polars 
as
 pl

# sales.csv has 150 rows. Polars infers Int64 for 'price' from the first 100 rows.

# Row 101 has a decimal price that fails to parse as Int64.

df 
=
 pl
.
read_csv
(
"sales.csv"
)

# ComputeError: could not parse `10.50` as dtype `i64` at column 'price' (column number 2)

#

# You might want to try:

# - increasing `infer_schema_length` (e.g. `infer_schema_length=10000`),

# - specifying correct dtype with the `schema_overrides` argument

# - setting `ignore_errors` to `True`,

Four parameters cover the range of strategies to resolve this:

Parameter
What it does
When to use
schema_overrides={…}
Overrides inference for named columns. Infers the rest. Order-independent.
Production pipelines with known problem columns
schema={…}
Declares the full schema. Disables inference entirely. Position-sensitive.
Ingestion of external CSVs with a strict contract
infer_schema=False
Reads every column as 
String
Exploring an unfamiliar file before deciding on types
ignore_errors=True
Sets unparseable values to null and suppresses errors
When you accept silently nulling unparseable values

schema_overrides={…}is the right choice for most cases.
You provide a dictionary of column name to Polars dtype.
Polars uses these types for the named columns, infers the rest, and the column order in the dictionary does not matter.

df 
=
 pl
.
read_csv
(

 "sales.csv"
,

 schema_overrides
=
{
"price"
: pl.Float64},

)

# Output

# shape: (150, 2)

# ┌─────┬────────┐

# │ id ┆ price │

# │ --- ┆ --- │

# │ i64 ┆ f64 │

# ╞═════╪════════╡

# │ 1 ┆ 10.0 │

# │ … ┆ … │

# │ 101 ┆ 10.5 │

# │ … ┆ … │

# │ 150 ┆ 1500.0 │

# └─────┴────────┘

schema={…}takes a full column-to-type dictionary.
Every column must be listed in the order they appear in the file.

df 
=
 pl
.
read_csv
(

 "sales.csv"
,

 schema
=
{
"id"
: pl.Int64, 
"price"
: pl.Float64},

)

infer_schema=Falseturns off schema inference and reads all columns asStringvalues.
It allows you to parse the entire file without problems, leaving any casting to your code.
Use it when working with files whose schema you don’t know yet.

df 
=
 pl
.
read_csv
(

 "sales.csv"
,

 infer_schema
=
False
,

)

Lastly,ignore_errors=Trueconverts unparseable values to null and suppresses the error.
The column keeps its inferred type and the bad value is silently lost.
It’s better to avoid it in production, since it could cause data loss.

df 
=
 pl
.
read_csv
(

 "sales.csv"
,

 ignore_errors
=
True
,

)

These strategies allow you to create a DataFrame with a strict schema from files that don’t have metadata to help you.
Multi-file datasets bring a new set of problems, covered in the next section.

### Parquet

Parquet files carry type metadata, so we don’t have to infer data types like with CSV files.
Schema problems arise when datasets consist of multiple files with diverging schemas (this also applies to multi-file CSV datasets).
When you scan them with a glob pattern (a wildcard path likeevents_*.parquetthat matches multiple files), any divergence raises an error.

The first file Polars encounters from the glob sets the expected schema.
Any file that diverges from it raises an error.
The three shapes each produce a different error and take a different fix.

#### Additive

A later file has a column not in the expected schema.

# events_2023.parquet: id, value (loads first in this example; sets expected schema)

# events_2024.parquet: id, value, category (brings extra 'category')

df 
=
 pl
.
scan_parquet
(
"events_*.parquet"
).
collect
()

# SchemaError: extra column in file outside of expected schema: category,

# hint: specify this column in the schema, or pass extra_columns='ignore' in scan options.

To discard the new column,extra_columns="ignore"is the simplest fix:

df 
=
 pl
.
scan_parquet
(
"events_*.parquet"
, extra_columns
=
"ignore"
).
collect
()

To keep it and null-fill the files that predate it, pass a supersetschema={…}withmissing_columns="insert":

schema 
=
 {
"id"
:
 pl
.
Int64
,
 "value"
:
 pl
.
Int64
,
 "category"
:
 pl
.
String
}

df 
=
 pl
.
scan_parquet
(

 "events_*.parquet"
,

 schema
=
schema,

 missing_columns
=
"insert"
,

).
collect
()

# Output

# shape: (4, 3)

# ┌─────┬───────┬──────────┐

# │ id ┆ value ┆ category │

# │ --- ┆ --- ┆ --- │

# │ i64 ┆ i64 ┆ str │

# ╞═════╪═══════╪══════════╡

# │ 1 ┆ 10 ┆ null │ ← 2023 rows, no category

# │ 2 ┆ 20 ┆ null │

# │ 3 ┆ 30 ┆ A │ ← 2024 rows

# │ 4 ┆ 40 ┆ B │

# └─────┴───────┴──────────┘

#### Subtractive

A later file is missing a column from the expected schema.

# events_a.parquet: id, value, category (loads first, sets expected schema)

# events_b.parquet: id, value (category not yet present in this file)

df 
=
 pl
.
scan_parquet
(
"events_*.parquet"
).
collect
()

# ColumnNotFoundError: did not find column category,

# consider passing `missing_columns='insert'`

missing_columns="insert"null-fills the absent column.
No explicitschema={…}is needed when the superset-schema file always loads first.

df 
=
 pl
.
scan_parquet
(
"events_*.parquet"
, missing_columns
=
"insert"
).
collect
()

Alternatively, you can add an explicit supersetschema={…}:

schema 
=
 {
"id"
:
 pl
.
Int64
,
 "value"
:
 pl
.
Int64
,
 "category"
:
 pl
.
String
}

df 
=
 pl
.
scan_parquet
(

 "events_*.parquet"
,

 schema
=
schema,

 missing_columns
=
"insert"
,

).
collect
()

#### Type drift

A column exists in all files but the dtype differs across them.

To stay lazy and let Polars handle integer upcasting:

df 
=
 pl
.
scan_parquet
(

 "events_*.parquet"
,

 cast_options
=
pl.
ScanCastOptions
(integer_cast
=
"upcast"
),

).
collect
()

integer_cast="upcast"only widens.
If the first-loaded file holds the wider type (Int64), a later narrower file (Int32) is cast up cleanly.
If the first-loaded file is the narrower type (Int32), a laterInt64file would require narrowing, which can lose data, and is rejected.

ScanCastOptionslets you configure casting behavior per type, since what counts as safe differs: widening an integer is lossless, downcasting a float is not, and timezone shifts require explicit opt-in.
Note:ScanCastOptionsis currently marked as unstable and may emit aPolarsUnstableWarning.
The full set of parameters:

Parameter
Options
integer_cast
upcast
 (widen losslessly), 
forbid
float_cast
upcast
, 
downcast
, 
forbid
datetime_cast
nanosecond-downcast
, 
convert-timezone
, 
forbid
missing_struct_fields
insert
 (add nulls), 
raise
extra_struct_fields
ignore
, 
raise
categorical_to_string
allow
, 
forbid

When file order is unpredictable, or when you need to handle missing columns and type drift without providing an explicit schema, usepl.concatwithhow="diagonal_relaxed".
It scans each file separately and coerces types to a common supertype while aligning columns by name:

import
 glob

lfs 
=
 [pl
.
scan_parquet
(f)
 for
 f 
in
 glob
.
glob
(
"events_*.parquet"
)
]

df 
=
 pl
.
concat
(lfs, how
=
"diagonal_relaxed"
).
collect
()

To see the effect in isolation:

a 
=
 pl
.
LazyFrame
({
"id"
: [
1
, 
2
], 
"value"
: pl.
Series
([
10
, 
20
], dtype
=
pl.Int32)})

b 
=
 pl
.
LazyFrame
({
"id"
: [
3
, 
4
], 
"value"
: pl.
Series
([
30
, 
40
], dtype
=
pl.Int64), 
"category"
: [
"x"
, 
"y"
]})

pl
.
concat
([a, b], how
=
"diagonal_relaxed"
).
collect
()

# Output

# shape: (4, 3)

# ┌─────┬───────┬──────────┐

# │ id ┆ value ┆ category │

# │ --- ┆ --- ┆ --- │

# │ i64 ┆ i64 ┆ str │

# ╞═════╪═══════╪══════════╡

# │ 1 ┆ 10 ┆ null │

# │ 2 ┆ 20 ┆ null │

# │ 3 ┆ 30 ┆ x │

# │ 4 ┆ 40 ┆ y │

# └─────┴───────┴──────────┘

valuewas upcast fromInt32toInt64, and the missingcategorycolumn inais filled withnull.

This is order-independent and handles additive, subtractive, and type drift changes.
The fourhow=…modes:

Mode
Columns
Types
vertical
must match
must match
vertical_relaxed
must match
coerces to supertype
diagonal
fills missing with null
must match
diagonal_relaxed
fills missing with null
coerces to supertype

Usediagonal_relaxedwhen columns differ across files and types have drifted.

### Delta Lake

Delta Lake stores its schema in a transaction log: a sequence of JSON commit files that live next to the Parquet data and record every schema change and every add or remove of data files.write_deltaorsink_deltaupdates this log on every write.

#### Additive and subtractive

Delta Lake enforces schema strictness on every write by default.
If a new upstream field arrives in your batch, the append fails:

# Initial table has columns: id, value

initial 
=
 pl
.
DataFrame
({
"id"
: [
1
, 
2
], 
"value"
: [
10
, 
20
]})

initial
.
write_delta
(
"events_delta"
)

# New batch adds a column

new_batch 
=
 pl
.
DataFrame
({
"id"
: [
3
, 
4
], 
"value"
: [
30
, 
40
], 
"source"
: [
"web"
, 
"app"
]})

new_batch
.
write_delta
(
"events_delta"
, mode
=
"append"
)

# SchemaMismatchError: Cannot cast schema, number of fields does not match: 3 vs 2

For additive evolution, you can passschema_mode="merge":

new_batch
.
write_delta
(

 "events_delta"
,

 mode
=
"append"
,

 delta_write_options
=
{
"schema_mode"
: 
"merge"
},

)

# Output: old rows get null in 'source', new rows carry the value

# shape: (4, 3)

# ┌─────┬───────┬────────┐

# │ id ┆ value ┆ source │

# │ --- ┆ --- ┆ --- │

# │ i64 ┆ i64 ┆ str │

# ╞═════╪═══════╪════════╡

# │ 1 ┆ 10 ┆ null │

# │ 2 ┆ 20 ┆ null │

# │ 3 ┆ 30 ┆ web │

# │ 4 ┆ 40 ┆ app │

# └─────┴───────┴────────┘

The same parameter handles the subtractive case: a column the table already has is absent from the incoming batch.
Delta null-fills the missing column in the new rows.

# Table has columns: id, value, source

# New batch is missing 'source'

slim_batch 
=
 pl
.
DataFrame
({
"id"
: [
5
, 
6
], 
"value"
: [
50
, 
60
]})

slim_batch
.
write_delta
(

 "events_delta"
,

 mode
=
"append"
,

 delta_write_options
=
{
"schema_mode"
: 
"merge"
},

)

# Output: new rows get null in 'source'

# shape: (6, 3)

# ┌─────┬───────┬────────┐

# │ id ┆ value ┆ source │

# │ --- ┆ --- ┆ --- │

# │ i64 ┆ i64 ┆ str │

# ╞═════╪═══════╪════════╡

# │ 1 ┆ 10 ┆ null │

# │ 2 ┆ 20 ┆ null │

# │ 3 ┆ 30 ┆ web │

# │ 4 ┆ 40 ┆ app │

# │ 5 ┆ 50 ┆ null │

# │ 6 ┆ 60 ┆ null │

# └─────┴───────┴────────┘

Renames and incompatible types need an explicit cast or rename before writing.

#### Full replacement

For a full table replacement with a different schema, useschema_mode="overwrite":

replacement 
=
 pl
.
DataFrame
({
"product"
: [
"x"
, 
"y"
], 
"count"
: [
100
, 
200
]})

replacement
.
write_delta
(

 "events_delta"
,

 mode
=
"overwrite"
,

 delta_write_options
=
{
"schema_mode"
: 
"overwrite"
},

)

### Apache Iceberg

Iceberg stores its schema in a catalog: a metadata service that maps a table name likedb.eventsto the current schema and the list of data files in each snapshot.
TheSqlCatalogused below is a SQLite-backed local catalog, convenient for examples.
In production this is usually a Hive, Glue, or REST catalog running as a service.

Apache Iceberg was designed with schema evolution as a first-class concern.
Columns are tracked by a stable field ID rather than by name or position.
When you add a column, rename it, or widen its type through the catalog, existing data files are not rewritten.
The catalog records the mapping and read operations resolve it transparently.

Schema changes are declared throughtable.update_schema()between writes:

from
 pyiceberg
.
catalog
.
sql 
import
 SqlCatalog

from
 pyiceberg
.
schema 
import
 Schema

from
 pyiceberg
.
types 
import
 NestedField
,
 LongType
,
 StringType

catalog 
=
 SqlCatalog
(

 "default"
,

 **
{
"uri"
: 
"sqlite:///catalog.db"
, 
"warehouse"
: 
"file:///data/warehouse"
},

)

catalog
.
create_namespace
(
"db"
)

iceberg_schema 
=
 Schema
(

 NestedField
(
1
, 
"id"
, 
LongType
()),

 NestedField
(
2
, 
"value"
, 
LongType
()),

)

table 
=
 catalog
.
create_table
(
"db.events"
, schema
=
iceberg_schema)

# Write initial data

pl
.
DataFrame
({
"id"
: [
1
, 
2
, 
3
], 
"value"
: [
10
, 
20
, 
30
]}).
write_iceberg
(table, mode
=
"append"
)

# Evolve the schema through the catalog. No data files are rewritten.

with
 table
.
update_schema
()
 as
 update
:

 update
.
add_column
(
"category"
, 
StringType
())

# Append new data with the added column

pl
.
DataFrame
({
"id"
: [
4
, 
5
], 
"value"
: [
40
, 
50
], 
"category"
: [
"A"
, 
"B"
]}).
write_iceberg
(table, mode
=
"append"
)

# Read the full table

df 
=
 pl
.
scan_iceberg
(table).
collect
().
sort
(
"id"
)

print
(df)

# Output

# shape: (5, 3)

# ┌─────┬───────┬──────────┐

# │ id ┆ value ┆ category │

# │ --- ┆ --- ┆ --- │

# │ i64 ┆ i64 ┆ str │

# ╞═════╪═══════╪══════════╡

# │ 1 ┆ 10 ┆ null │

# │ 2 ┆ 20 ┆ null │

# │ 3 ┆ 30 ┆ null │

# │ 4 ┆ 40 ┆ A │

# │ 5 ┆ 50 ┆ B │

# └─────┴───────┴──────────┘

Old rows get null in the new column.pl.scan_icebergalways reads the current snapshot and resolves column additions automatically, without any extra parameter.

Because columns are tracked by field ID rather than name, renames are also handled throughupdate_schema()without rewriting data files.
Incompatible type changes still require explicit handling before writing, as with any format.

## Conclusion

For CSV, type inference is the main problem.
To resolve this, you can use:

* schema_overrides={…}to coerce columns you know to be a certain type, and still automatically infer the rest.
* schema={…}to enforce a full schema (which is column-ordered).
* infer_schema=Falseto turn off inference and read all columns asString.
* ignore_errors=Trueto set values that don’t fit the schema asnulland silence errors.

For multi-file Parquet, Polars has a parameter for each shape:

* missing_columns="insert"for additive and subtractive.
* ScanCastOptions(integer_cast="upcast")for type drift.
* diagonal_relaxedwhen both problems appear together.

For Delta Lake,schema_mode="merge"handles additive and subtractive evolution.
Renames and incompatible type changes still need explicit handling before the write.

For Iceberg, the format handles additive evolution, renames, and type widening through the catalog.pl.scan_icebergresolves them automatically at read time.
If schema evolution is a known requirement, Iceberg’s design pushes most of these parameters out of your code.