---
title: 'GitHub - cocoindex-io/cocoindex: Incremental engine for long horizon agents 🌟 Star if you like it! · GitHub'
url: https://github.com/cocoindex-io/cocoindex
site_name: github
content_file: github-github-cocoindex-iococoindex-incremental-engine-fo
fetched_at: '2026-05-04T12:21:14.248962'
original_url: https://github.com/cocoindex-io/cocoindex
author: cocoindex-io
description: Incremental engine for long horizon agents 🌟 Star if you like it! - cocoindex-io/cocoindex
---

cocoindex-io

 

/

cocoindex

Public

* NotificationsYou must be signed in to change notification settings
* Fork575
* Star7.8k

 
 
 
 
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

1,732 Commits
1,732 Commits
.cargo
.cargo
 
 
.claude
.claude
 
 
.github
.github
 
 
dev
dev
 
 
docs
docs
 
 
examples
examples
 
 
python
python
 
 
rust
rust
 
 
skills/
cocoindex
skills/
cocoindex
 
 
.env.lib_debug
.env.lib_debug
 
 
.gitignore
.gitignore
 
 
.lycheeignore
.lycheeignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
about.hbs
about.hbs
 
 
about.toml
about.toml
 
 
opencode.json
opencode.json
 
 
pyproject.toml
pyproject.toml
 
 
ruff.toml
ruff.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Your agents deservefresh context.

Star us ❤️ →···

CocoIndex turns codebases, meeting notes, inboxes, Slack, PDFs, and videos into live, continuously fresh context for your AI agents and LLM apps to reason over effectively — with minimal incremental processing. Get your production AI agent ready in 10 minutes with reliable, continuously fresh data — no stale batches, no context gap

Incremental· only the delta  ·Any scale· parallel by default  ·Declarative· Python, 5 min

Deutsch|English|Español|français|日本語|한국어|Português|Русский|中文

## Built with CocoIndex ❤️

See all 20+ examples · updated every week →

### Get started

pip install -U cocoindex

Declarewhatshould be in your target — CocoIndex keeps it in sync forever, recomputing only the Δ.

import
 
cocoindex
 
as
 
coco

from
 
cocoindex
.
connectors
 
import
 
localfs
, 
postgres

from
 
cocoindex
.
ops
.
text
 
import
 
RecursiveSplitter

@
coco
.
fn
(
memo
=
True
) 
# ← cached by hash(input) + hash(code)

async
 
def
 
index_file
(
file
, 
table
):
 
for
 
chunk
 
in
 
RecursiveSplitter
().
split
(
await
 
file
.
read_text
()):
 
table
.
declare_row
(
text
=
chunk
.
text
, 
embedding
=
embed
(
chunk
.
text
))

@
coco
.
fn

async
 
def
 
main
(
src
):
 
table
 
=
 
await
 
postgres
.
mount_table_target
(
PG
, 
table_name
=
"docs"
)
 
table
.
declare_vector_index
(
column
=
"embedding"
)
 
await
 
coco
.
mount_each
(
index_file
, 
localfs
.
walk_dir
(
src
).
items
(), 
table
)

coco
.
App
(
coco
.
AppConfig
(
name
=
"docs"
), 
main
, 
src
=
"./docs"
).
update_blocking
()

Run once to backfill. Re-run anytime — only the changed files re-embed.

Building with an AI coding agent?Drop in ourCocoIndex skillso your agent writes correct v1 code — concepts, APIs, patterns, all in one file.SeeUse with AI coding agentsfor install steps.

   
 

## React —for data engineering

See the React ↔ CocoIndex mental model →

## Incremental enginefor long-horizon agents

Data transformation for any engineer, designed for AI workloads —with a smart incremental engine foralways-fresh, explainable data.

## Whyincremental?

Your agents are only as good as the data they see.Batch pipelines drift stale. CocoIndex stays live — and only runs the Δ.

## What can youbuild?

See all 20+ examples · updated every week →

Working starters fromthe examples tree— clone, plug your source, ship.

Building something with CocoIndex?We want to see it.Tag@cocoindex_ioon X or drop a link in#showcaseon Discord. We'll boost it. 🥥

## Community

We aresoexcited to meet you.Every typo fix, new connector, doc tweak, or full-on rewrite makes CocoIndex better.Come hang out — big PRs and small ones, both welcome.

📝Read the contributing guide· 
 🐛good first issues· 
 💬Say hi on Discord

## CocoIndexEnterprise

### Large corpus —built for enterprise scale.

Incremental compute is the only way to keep large corpora fresh without re-embedding them every cycle.CocoIndex scales from a single repo to petabyte-scale stores — parallel by default, delta-only by design.

### Process once.Reconcile forever.

When a source changes, CocoIndex identifies the affected records, propagates the changeacross joins and lookups, updates the target, and retires stale rows —without touching anything that didn't change.

### Built on aRust engine.

The core is Rust — production-grade from day zero.Parallel chunking, zero-copy transforms where possible, and failure isolationso one bad record doesn't stall the flow.

Apache 2.0 · © CocoIndex contributors 🥥

## About

Incremental engine for long horizon agents 🌟 Star if you like it!

cocoindex.io

### Topics

 python

 rust

 real-time

 ai

 etl

 indexing

 data-engineering

 knowledge-graph

 help-wanted

 data-processing

 semantic-search

 change-data-capture

 ai-agents

 data-indexing

 rag

 llm

 context-engineering

 codebase-intelligence

 agentic-data-framework

 long-horizon-agent

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

7.8k

 stars
 

### Watchers

45

 watching
 

### Forks

575

 forks
 

 Report repository

 

## Releases196

v1.0.2

 Latest

 

Apr 29, 2026

 

+ 195 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python75.1%
* Rust24.4%
* Other0.5%