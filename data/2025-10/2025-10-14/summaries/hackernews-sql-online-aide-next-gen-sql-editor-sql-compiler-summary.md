---
title: SQL Online AiDE - Next gen SQL Editor | SQL Compiler
url: https://sqliteonline.com/
date: 2025-10-14
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-14T11:13:33.016268
screenshot: hackernews-sql-online-aide-next-gen-sql-editor-sql-compiler.png
---

# SQL Online AiDE - Next gen SQL Editor | SQL Compiler

## SQL Online AIDE - Next Gen SQL Editor | SQL Compiler

### Key Features and Benefits

* **Next-gen SQL Editor**: An Advanced Query Language (SQL) compiler for online queries.
* **Improved Editor Experience**: A well-designed user interface for easy query composition and execution.
* **Enhanced Security**: Enhanced password protection, data encryption, and auditing capabilities.

### Syntax Overview

The provided syntax consists of a series of lines separated by whitespace. Each line represents an individual component of the SQL statement.

#### Data Selection (X axis)

*   `SELECT`: Starts a new query.
*   `...`: Specifies the dataset to be queried (e.g., `example`).
*   `.../...`: Defines optional columns and attributes for query execution (e.g., `column_name / value`).

---

```sql
  -- X - column name, axis: x1, x2, ..xn Value: Number
-- L - column name, axis: l Value: Text
-- T - column name, axis: t Value: UnixTime Number
-- Axis Y:
-- Y - column name, axis: y1, y2, ..yn Value: Number
-- Y - color line: y_cFF00FF (HEX6)
-- Option:
-- C - color point: c Value: FF00FF (HEX6)
-- V - radius point: v Value: Number

  -- Example
  QLINE-SELECT example

  -- Example
  QAREA-SELECT example
```

### Data Visualization

*   `QAREA-SELECT`: Renders a series of rectangles for various fields, providing detailed statistics on data usage.
*   Additional options include `QBAR-SELECT` (bar chart) and `QPIE-SELECT` (pie chart).

---

```sql
  -- Example
  QLINE-SELECT example

  -- Example
  QBAR-SELECT example

  -- Example
  QPIE-SELECT example
```

### Bubble Chart

*   A special option for `QBAR-SELECT`.
*   Customizable color and radius.

---

```sql
  -- Example
  QBA-R-SELECT example
```

## History and About Sections

These lines follow a similar structure to the data selection section.

*   `History`: Displays past query logs.
*   `About`: Provides additional information about the online AIDE platform.
