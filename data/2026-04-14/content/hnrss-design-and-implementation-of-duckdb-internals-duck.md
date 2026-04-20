---
title: Design and Implementation of DuckDB Internals – DuckDB
url: https://duckdb.org/library/design-and-implementation-of-duckdb-internals/
site_name: hnrss
content_file: hnrss-design-and-implementation-of-duckdb-internals-duck
fetched_at: '2026-04-14T11:57:27.943752'
original_url: https://duckdb.org/library/design-and-implementation-of-duckdb-internals/
author: Torsten Grust (University of Tübingen)
date: '2026-04-10'
published_date: '2026-03-19T00:00:00+00:00'
description: DuckDB is an in-process SQL database management system focused on analytical query processing. It is designed to be easy to install and easy to use. DuckDB has no external dependencies. DuckDB has bindings for C/C++, Python, R, Java, Node.js, Go and other languages.
tags:
- hackernews
- hnrss
---

# Design and Implementation of DuckDB Internals

Torsten Grust (University of Tübingen)

2026-03-19

This is a DuckDB-based course explaining the Design and Implementation of Database System Internals (“DiDi”).
The slides and auxiliary material are available in theGitHub repository.

## Overview

This lecture material has been developed byTorsten Grustto support a 15-week course for undergraduate students of
theDatabase Research Groupat
University of Tübingen (Germany).

## A Tour Through DuckDB's Internals

The course treads on a path through selected internals of theDuckDBrelational database system. 15 weeks
do not suffice to exhaustively discuss all interesting bits and pieces of the
DuckDB kernel. As of March 2026, the chapter layout reads as follows:

1. Welcome & Setup
2. The Query Performance Spectrum
3. Managing Memory + Grouped Aggregation
4. Sorting Large Tables
5. The ART of Indexing
6. Query Execution Plans and Pipelining
7. Vectorized Query Execution
8. Query Rewriting and Optimization

(You can also download theDiDi slides concatenated into a single deck)

You will need basic SQL skills to follow the course's red thread and
auxiliary material. There are few queries that go beyond the coreSELECT-FROM-WHERE-GROUP BY-HAVINGblock, however. Should
you require an introduction to the tabular data model and its
query language SQL, you may find the companion courseTabular Database Systemshelpful.

## Other Library Resources

Ubuntu Summit 2026

Talk

45 min

### DuckDB: Not Quack Science

2026-05-27

Gábor Szárnyas

AI Council 2026

Talk

### Super-Secret Next Big Thing for DuckDB

2026-05-12

Hannes Mühleisen

DuckLake v1.0

Podcast

55 min

### DuckLake v1.0 – Developer Discussion

2026-04-13

Pedro Holanda and Mark Raasveldt

			All library resources
