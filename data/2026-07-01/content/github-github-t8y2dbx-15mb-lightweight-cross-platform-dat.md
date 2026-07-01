---
title: 'GitHub - t8y2/dbx: 15MB, lightweight, cross-platform database client. Supports MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server and more.15MB，轻量级跨平台数据库客户端、数据库管理工具。支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、ClickHouse、SQL Server 等。 · GitHub'
url: https://github.com/t8y2/dbx
site_name: github
content_file: github-github-t8y2dbx-15mb-lightweight-cross-platform-dat
fetched_at: '2026-07-01T12:04:45.004864'
original_url: https://github.com/t8y2/dbx
author: t8y2
description: 15MB, lightweight, cross-platform database client. Supports MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server and more.15MB，轻量级跨平台数据库客户端、数据库管理工具。支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、ClickHouse、SQL Server 等。 - t8y2/dbx
---

t8y2

 

/

dbx

Public

* NotificationsYou must be signed in to change notification settings
* Fork687
* Star8k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

2,756 Commits
2,756 Commits
.cargo
.cargo
 
 
.github
.github
 
 
.husky
.husky
 
 
agents
agents
 
 
apps
apps
 
 
crates
crates
 
 
deploy
deploy
 
 
docs
docs
 
 
packages
packages
 
 
plugins
plugins
 
 
scripts
scripts
 
 
skills/
dbx
skills/
dbx
 
 
src-tauri
src-tauri
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.nvmrc
.nvmrc
 
 
.oxfmtrc.json
.oxfmtrc.json
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README-NIX.md
README-NIX.md
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SECURITY.md
SECURITY.md
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
rustfmt.toml
rustfmt.toml
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

60+ databases in 15 MB. Desktop & Docker self-hosting, with built-in AI assistant.

English |前往中文版本

## Why DBX?

### 🪶 15 MB, zero runtime bloat

No Java JRE. No Python venv. No bundled Chromium. DBX ships as a single small binary — download, install, connect. DBeaver needs Java; TablePlus is macOS-only. DBX runs everywhere with nothing extra.

### 🤖 AI that lives in your editor

Highlight a table, describe what you want, get SQL back — no copy-paste between tools. Works with Claude, OpenAI, or local models via Ollama. Built-in safety checks review AI-generated SQL before it runs.

### 🔌 MCP: your databases, AI-ready

DBX speaks the Model Context Protocol. Claude Code, Cursor, Windsurf, and other AI coding agents can query your databases through connections you already set up. One config, everywhere.

### 🌐 Desktop + Docker + Web

Native app on macOS, Windows, and Linux. Self-host via Docker for team access. Web version for browser-only environments. Same feature set. Same connections.

## Features

### 60+ Databases, One Tool

MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server, Oracle, Elasticsearch, Qdrant, Milvus, Weaviate, MariaDB, TiDB, OceanBase, openGauss, GaussDB, KWDB, KingBase, Vastbase, GoldenDB, Doris, SelectDB, StarRocks, Manticore Search, Redshift, DM, TDengine, XuguDB, CockroachDB, Access, HighGo, and more. Agent/JDBC-oriented profiles extend DBX to H2, Snowflake, Trino, PrestoSQL, Hive, DB2, Informix, Neo4j, Cassandra, BigQuery, Kylin, SunDB, and custom JDBC connections. New native and agent-driven drivers also cover Databricks, SAP HANA, Teradata, Vertica, Firebird, Exasol, YashanDB, GBase 8a/8s, Databend, RQLite, Turso, InfluxDB, QuestDB, IoTDB, etcd, ZooKeeper, Nacos, IRIS, and more. Message queue admin is also available for Pulsar, Kafka, and RocketMQ. All in a single ~15 MB app. No bundled Chromium.

### Query Editor

CodeMirror 6 with SQL syntax highlighting, metadata-aware autocomplete,Cmd+Enterexecution, selected SQL execution, SQL formatting, diagnostics, and 9 editor themes. Persistent query history, saved SQL snippets, tab restore, and SQL file execution keep repeat work close at hand.

### AI SQL Assistant

Describe what you want in plain language — get SQL back. DBX can explain queries, optimize SQL, fix errors, and run AI-generated SQL through built-in safety checks. Works with Claude, OpenAI, local models, or any OpenAI-compatible endpoint.

### Data Grid

Virtual-scrolled table that handles large result sets. Inline editing, SQL preview before save, WHERE / ORDER BY controls, DataGrip-style filters, LIKE / NOT LIKE context filters, sorting, full-text search, pagination, column resize, auto-fit, row numbers, zebra stripes, and full cell details. Export or copy as CSV, JSON, Markdown, XLSX, or INSERT statements.

### Schema Tools

* Schema browser— databases, schemas, tables, columns, indexes, foreign keys, triggers, with sidebar search & pin
* Object browser— grouped procedures, functions, views, and source editing where supported
* Table structure editor— reviewable column and index changes for supported engines
* ER diagram— visualize table relationships
* Schema diff— compare structures across connections
* Explain plan— visual query execution plan
* Field lineage— column-level lineage analysis
* Database search— find objects across large schemas

### Data Operations

* Table import— CSV, Excel
* Data transfer— migrate between databases
* Database export— full database dump
* Data compare— compare table data and review synchronization output
* SQL file execution— run.sqlfiles directly
* File preview— drag & drop Parquet, CSV, JSON to preview instantly (powered by DuckDB)
* Connection import— bring connection profiles from DBeaver or Navicat

### Specialized Browsers

* Redis— key pattern search, batch key operations, command runner, TTL editing, and all data types (String, Hash, List, Set, ZSet, Stream)
* MongoDB— document CRUD with pagination, Atlas & replica set URL connection

### Safety & Connectivity

SSH tunnel (key & password) · database and AI proxy settings · auto-reconnect on connection loss · confirmation dialogs for destructive operations · encrypted config export/import · color-coded connections · driver store and optional JDBC plugin

### Polished UI

Dark mode with native title bar sync · 9 editor themes · English, 简体中文 & Español · layout preferences · built-in auto-update

## AI Agent Integration (MCP)

DBX provides anMCP serverthat lets AI coding agents query your databases using connections already configured in DBX.

npx @dbx-app/mcp-server

Add to your.mcp.json:

{
 
"mcpServers"
: {
 
"dbx"
: { 
"command"
: 
"
npx
"
, 
"args"
: [
"
-y
"
, 
"
@dbx-app/mcp-server
"
] }
 }
}

Windows portable builds needDBX_DATA_DIRin the MCP config, pointing to thedatadirectory next toDBX.exe(the folder that containsdbx.db).

Works with Claude Code, Cursor, Windsurf, and any MCP-compatible agent. Supports listing connections, browsing tables, executing SQL, and opening tables directly in DBX's UI.

DBX also provides a dedicated CLI package for terminal, script, and Codex workflows:

npm install -g @dbx-app/cli

#
 or via Homebrew

brew tap t8y2/dbx 
&&
 brew install dbx-cli
dbx connections list --json
dbx query 
local
 
"
select 1
"
 --json

See theMCP server READMEandCLI READMEfor details.

## Install

Download the latest release from theReleasespage.

Homebrew (macOS):

brew install --cask dbx

Scoop (Windows):

scoop bucket add dbx https://github.com/t8y2/scoop-bucket
scoop install dbx

WinGet (Windows):

winget install t8y2.dbx

## Self-Hosted (Docker)

DBX provides a web version that can be deployed via Docker.

docker run -d --name dbx -p 4224:4224 -v dbx-data:/app/data t8y2/dbx

Or with Docker Compose. A ready-to-use example lives atdeploy/docker-compose.yml:

services
:
 
dbx
:
 
image
: 
t8y2/dbx

 
ports
:
 - 
"
4224:4224
"

 
volumes
:
 - 
dbx-data:/app/data

 
restart
: 
unless-stopped

volumes
:
 
dbx-data
:

Openhttp://localhost:4224in your browser. Multi-arch images (amd64 / arm64) are available.

To publish DBX under a reverse-proxy context path such as/dbx, set the
runtime base path and proxy the same prefix to the container:

environment
:
 - 
DBX_PUBLIC_BASE_PATH=/dbx

When building the frontend yourself with an absolute asset base, setVITE_DBX_BASE_PATH=/dbx/beforepnpm build.

## Getting Started

### Prerequisites

* Node.js>= 18
* pnpm
* Rust>= 1.77

#### System Dependencies

macOS:

No additional dependencies required.

Linux (Ubuntu/Debian):

sudo apt-get install -y libwebkit2gtk-4.1-dev libgtk-3-dev libappindicator3-dev librsvg2-dev patchelf libssl-dev

NIXOS/NIX :

See README-NIX.md

Windows:

No additional dependencies required.

### Development

make

makeinstalls root dependencies when needed and starts the local Tauri desktop development environment.

Tip

DuckDB compilation takes a while. If you're not working on DuckDB features,
skip it to speed up local builds:

#
 Fast checks (skip DuckDB)

make cargo-check-fast
make cargo-test-fast

#
 Tauri dev without DuckDB

make dev-fast

The--no-default-featuresflag only affects local development.
Release builds (pnpm tauri build) always include DuckDB.

Web version:

make dev-web 
#
 frontend

make dev-backend 
#
 backend

Documentation site:

make docs

The official DBX documentation site lives indocs/. If you want to improve the website content or documentation pages, edit the files underdocs/and runmake docsto preview the site locally.

JDBC agent driver development projects live inagents/:

cd
 agents
./gradlew 
test

Build artifacts fromagents/drivers/<db-type>/build/libs/are picked up by local driver install flows when available.

### Build

make package

The installer will be insrc-tauri/target/release/bundle/.

## Tech Stack

Layer

Technology

Framework

Tauri 2

Frontend

Vue 3
 + TypeScript

UI

shadcn-vue
 + Tailwind CSS

Editor

CodeMirror 6

Backend

Rust + 
sqlx
 / 
tiberius
 / 
redis-rs
 / 
mongodb

## Community

## FAQ

Is DBX free?

Yes. DBX is open source under Apache-2.0. All features are free.

Does DBX phone home?

No. DBX does not collect telemetry. The auto-update feature checks GitHub Releases for new versions — you can disable it in settings.

Can I use DBX without an internet connection?

Yes. The desktop app works fully offline. For air-gapped driver installs, download offline driver packages from the [Offline Drivers page](
https://dbxio.com/en/drivers
) on an internet-connected machine, transfer them to the offline machine, then import them in DBX from Settings > Driver Manager. AI features need network access to the model endpoint (or a local model via Ollama).

How is DBX different from DBeaver / TablePlus / Beekeeper Studio?

DBX is 15 MB with no runtime dependencies (no Java, no Python). It includes AI and MCP natively — not as plugins. It supports 60+ databases across desktop, Docker, and web from a single codebase.

What databases are supported?

MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server, Oracle, Elasticsearch, Qdrant, Milvus, Weaviate, MariaDB, TiDB, OceanBase, openGauss, GaussDB, KWDB, KingBase, Vastbase, GoldenDB, Doris, SelectDB, StarRocks, Manticore Search, Redshift, DM, TDengine, XuguDB, CockroachDB, Access, HighGo, and more. Agent/JDBC-oriented profiles extend support to H2, Snowflake, Trino, PrestoSQL, Hive, DB2, Informix, Neo4j, Cassandra, BigQuery, Kylin, SunDB, Databricks, SAP HANA, Teradata, Vertica, Firebird, Exasol, YashanDB, GBase 8a/8s, Databend, RQLite, Turso, InfluxDB, QuestDB, IoTDB, etcd, ZooKeeper, Nacos, IRIS, and custom JDBC connections. Message queue admin (Pulsar, Kafka, RocketMQ) is also supported.

How do I report a bug or request a feature?

Open an issue on 
GitHub Issues
.

## Contributors

## Star History

## License

Apache-2.0

## About

15MB, lightweight, cross-platform database client. Supports MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server and more.15MB，轻量级跨平台数据库客户端、数据库管理工具。支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、ClickHouse、SQL Server 等。

dbxio.com

### Topics

 mysql

 rust

 redis

 gui

 sql-server

 database

 mongodb

 vue

 clickhouse

 sqlite

 postgresql

 database-management

 tauri

 database-client

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

8k

 stars
 

### Watchers

26

 watching
 

### Forks

687

 forks
 

 Report repository

 

## Releases71

v0.5.42

 Latest

 

Jul 1, 2026

 

+ 70 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust34.1%
* TypeScript31.5%
* Vue24.5%
* Java7.7%
* Go1.0%
* JavaScript0.6%
* Other0.6%