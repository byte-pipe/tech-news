---
title: SQLite as a document database
url: https://dgl.cx/2020/06/sqlite-json-support
date: 2026-08-24
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-30T06:03:16.505366
---

# SQLite as a document database

# SQLite as a document database – summary

## Main idea
- Recent SQLite versions (≥ 3.31.0) support **generated columns**, allowing JSON data to be stored in a plain TEXT column and automatically extracted into virtual or stored columns.
- This makes SQLite usable as an embedded document database, similar to PostgreSQL’s JSON features or Elastic, but without needing a separate server.

## How it works
- Create a table with a TEXT column for the raw JSON and a generated column that extracts a value using `json_extract`.
  ```sql
  CREATE TABLE t (
      body TEXT,
      d INT GENERATED ALWAYS AS (json_extract(body, '$.d')) VIRTUAL
  );
  ```
- Insert JSON directly:
  ```sql
  INSERT INTO t VALUES (json('{"d":"42"}'));
  ```
- Query using the generated column:
  ```sql
  SELECT * FROM t WHERE d = 42;
  ```

## Practical benefits
- **Validation at insert time**: malformed JSON triggers an error because the generated column relies on `json_extract`.
- **Enforcing presence of fields**: adding `NOT NULL` or other constraints to generated columns ensures required keys exist in the JSON.
- **Indexing**: virtual generated columns can be indexed, giving fast look‑ups on extracted fields.
  ```sql
  CREATE INDEX xid ON x(id);
  ```
- **Schema evolution**: start with a single JSON column, then add more generated columns and indexes as needed without altering existing data.

## Options and limitations
- **VIRTUAL vs STORED**:
  - `VIRTUAL` computes values on the fly; suitable for most cases.
  - `STORED` caches the extracted values but cannot be added later with `ALTER TABLE`.
- Adding generated columns after table creation is possible with `ALTER TABLE … ADD COLUMN … GENERATED ALWAYS AS (…) VIRTUAL`.

## Typical use case
- Store incoming webhook payloads as raw JSON, then progressively extract and index fields that become relevant, turning an unstructured stream into a queryable dataset.