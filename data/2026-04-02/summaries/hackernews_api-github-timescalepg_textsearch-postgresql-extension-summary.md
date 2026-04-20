---
title: GitHub - timescale/pg_textsearch: PostgreSQL extension for BM25 relevance-ranked full-text search. Postgres OSS licensed. · GitHub
url: https://github.com/timescale/pg_textsearch
date: 2026-04-01
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-02T01:03:18.051952
---

# GitHub - timescale/pg_textsearch: PostgreSQL extension for BM25 relevance-ranked full-text search. Postgres OSS licensed. · GitHub

# pg_textsearch – Modern Ranked Text Search for PostgreSQL

## Overview
- Extension implements BM25 relevance ranking for full‑text search.
- Simple syntax: `ORDER BY content <@> 'search terms'`.
- Configurable BM25 parameters (`k1`, `b`).
- Supports PostgreSQL text search configurations (english, french, german, …).
- Fast top‑k queries via Block‑Max WAND optimization.
- Parallel index builds, partitioned table support, and production‑ready performance.

## Status & Compatibility
- Current version: v1.0.0 (production ready). Future features listed in `ROADMAP.md`.
- Compatible with PostgreSQL 17 and 18.

## Installation
### Pre‑built binaries
- Available on the Releases page for Linux/macOS (amd64, arm64) and PostgreSQL 17/18.
### Build from source
```bash
git clone https://github.com/timescale/pg_textsearch
cd pg_textsearch
make
make install   # may require sudo
```

## Setup
1. Add to `postgresql.conf`:
   ```conf
   shared_preload_libraries = 'pg_textsearch'
   ```
2. Restart PostgreSQL.
3. Enable the extension in each database:
   ```sql
   CREATE EXTENSION pg_textsearch;
   ```

## Basic Usage
### Create a table and index
```sql
CREATE TABLE documents (
  id   bigserial PRIMARY KEY,
  content text
);

INSERT INTO documents (content) VALUES
  ('PostgreSQL is a powerful database system'),
  ('BM25 is an effective ranking function'),
  ('Full text search with custom scoring');

CREATE INDEX docs_idx ON documents USING bm25(content)
  WITH (text_config = 'english');
```

### Querying
- Order by relevance (negative BM25 score, lower = better):
  ```sql
  SELECT *
  FROM documents
  ORDER BY content <@> 'database system'
  LIMIT 5;
  ```
- Explicit index specification:
  ```sql
  SELECT *
  FROM documents
  WHERE content <@> to_bm25query('database system', 'docs_idx') < -1.0;
  ```

### Verifying index usage
```sql
EXPLAIN SELECT * FROM documents
ORDER BY content <@> 'database system' LIMIT 5;
```
- Force index use (if needed):
  ```sql
  SET enable_seqscan = off;
  ```

## Filtering Strategies
- **Pre‑filtering**: Apply a separate filter index first, then score the reduced set.
- **Post‑filtering**: Score with BM25 first, then apply `WHERE` conditions.
- Choose based on selectivity and expected result size; combine with `LIMIT` for best performance.

## Index Options
- `text_config` (required): PostgreSQL text search configuration.
- `k1` (default 1.2): term‑frequency saturation.
- `b` (default 0.75): length normalization.
```sql
CREATE INDEX ON documents USING bm25(content)
  WITH (text_config = 'english', k1 = 1.5, b = 0.8);
```
- Supports multiple language configurations (e.g., `simple`, `french`, `german`).

## Data Types & Functions
- **bm25query**: Represents a BM25 query, optionally tied to an index.
  - `to_bm25query(text)` → bm25query (no index name, usable in ORDER BY).
  - `to_bm25query(text, text)` → bm25query (with index name, usable in WHERE).
  - Cast syntax: `'docs_idx:search text'::bm25query`.
- Operators:
  - `text <@> bm25query` → double precision (negative BM25 score).
  - `bm25query = bm25query` → boolean (equality).

## Performance Notes
- Index uses a memtable architecture for fast writes; creating the index after loading data yields better performance.
- Top‑k optimization avoids scoring all rows when combined with `ORDER BY … LIMIT`.
- Parallel index builds and partitioned table support improve scalability on large datasets.
