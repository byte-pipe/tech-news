---
title: Announcing DuckDB 1.5.0 – DuckDB
url: https://duckdb.org/2026/03/09/announcing-duckdb-150.html
date: 2026-03-13
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-13T03:14:34.435190
---

# Announcing DuckDB 1.5.0 – DuckDB

# Announcing DuckDB 1.5.0

## Overview
- Release version: **DuckDB v1.5.0** (codename “Variegata”), named after the Paradise shelduck (*Tadorna variegata*).
- Two active releases: v1.4 LTS (“Andium”) (supported until September 2026) and the new v1.5 (current).
- Next major release planned for September 2026: DuckDB 2.0.
- Full release notes are on the GitHub release page; installation instructions are on the installation page.
- Some extensions and client libraries (e.g., UI, Go, R, Java) may take a few days to become available due to extra review cycles.

## New Features

### Command‑Line Client
- Complete redesign with a new color palette (dark and light modes) and dynamic prompts showing the current database and schema.
- Customizable colors via the `.highlight_colors` command.
- Added convenience commands:
  - `.tables` – lists attached catalogs, schemas, tables, and columns.
  - `DESCRIBE` – shows column definitions for a specific table.
- Shortcut `_` allows inline access to the result of the previous query, avoiding re‑execution.
- Integrated pager that activates for result sets larger than 50 rows; navigation uses Page Up/Down (or Fn + Up/Down on macOS) and exits with `Q`.

### PEG‑Based Parser (experimental)
- Optional PEG parser can be enabled with `CALL enable_peg_parser();`.
- Provides better suggestions, clearer error messages, and extensibility for grammar extensions.
- Slight millisecond‑level performance overhead; intended to become the default parser in a future release.

### VARIANT Data Type
- Native support for a semi‑structured `VARIANT` type (inspired by Snowflake, available in Parquet since 2025).
- Stores typed binary data per row, offering superior compression and query performance compared to the text‑based `JSON` type.
- Example usage:
  - Create table with `VARIANT` column, insert heterogeneous values (integers, strings, arrays, objects).
  - Query `variant_typeof()` to inspect stored type.
  - Extract fields via dot notation or `variant_extract()` function.
- `VARIANT` can be read from Parquet files, preserving nested structures.

### Built‑in GEOMETRY Type
- (Mentioned in the TL;DR) Introduces a native `GEOMETRY` type for spatial data handling (details available in full release notes).

## Support and Future Roadmap
- v1.4 LTS will continue receiving updates until its end‑of‑life in September 2026.
- The upcoming DuckDB 2.0 release (targeted for September 2026) will bring additional major changes.

## Getting Started
- Install the new version via the official installation page.
- Be aware that some extensions (e.g., UI) and language bindings may have a short delay before they are released.
