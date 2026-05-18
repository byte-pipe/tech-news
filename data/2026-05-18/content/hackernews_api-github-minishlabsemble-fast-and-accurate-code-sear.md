---
title: 'GitHub - MinishLab/semble: Fast and Accurate Code Search for Agents. Uses ~98% fewer tokens than grep+read · GitHub'
url: https://github.com/MinishLab/semble
site_name: hackernews_api
content_file: hackernews_api-github-minishlabsemble-fast-and-accurate-code-sear
fetched_at: '2026-05-18T12:11:39.906983'
original_url: https://github.com/MinishLab/semble
author: Bibabomas
date: '2026-05-17'
description: Fast and Accurate Code Search for Agents. Uses ~98% fewer tokens than grep+read - MinishLab/semble
tags:
- hackernews
- trending
---

MinishLab

 

/

semble

Public

* NotificationsYou must be signed in to change notification settings
* Fork89
* Star2k

 
 
 
 
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

81 Commits
81 Commits
.github/
workflows
.github/
workflows
 
 
assets/
images
assets/
images
 
 
benchmarks
benchmarks
 
 
src/
semble
src/
semble
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
CITATION.cff
CITATION.cff
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

## Fast and Accurate Code Search for AgentsUses ~98% fewer tokens than grep+read

Quickstart•MCP Server•Bash / AGENTS.md•CLI•Benchmarks

Semble is a code search library built for agents. It returns the exact code snippets they need instantly, using ~98% fewer tokens than grep+read. Indexing and searching a full codebase end-to-end takes under a second, with ~200x faster indexing and ~10x faster queries than a code-specialized transformer, at 99% of its retrieval quality (seebenchmarks). Everything runs on CPU with no API keys, GPU, or external services. Run it as anMCP serveror call it from the shell viaAGENTS.mdand any agent (Claude Code, Cursor, Codex, OpenCode, etc.) gets instant access to any repo.

## Quickstart

Your agent queries Semble in natural language (e.g."How is authentication handled?") and gets back only the relevant code snippets, without grepping or reading full files. Set it up as an MCP server or via AGENTS.md:

### MCP (Claude Code)

Add Semble to Claude Code (requiresuv):

claude mcp add semble -s user -- uvx --from 
"
semble[mcp]
"
 semble

Using Codex, OpenCode, or Cursor? SeeMCP Serverfor setup instructions.

### Bash / AGENTS.md

Install Semble, then add the snippet below to yourAGENTS.mdorCLAUDE.md:

pip install semble 
#
 Install with pip

uv tool install semble 
#
 Or install with uv

AGENTS.md / CLAUDE.md snippet

## 
Code Search

Use 
`
semble search
`
 to find code by describing what it does or naming a symbol/identifier, instead of grep:

​```bash
semble search "authentication flow" ./my-project
semble search "save_pretrained" ./my-project
semble search "save model to disk" ./my-project --top-k 10
​```

Use 
`
semble find-related
`
 to discover code similar to a known location (pass 
`
file_path
`
 and 
`
line
`
 from a prior search result):

​```bash
semble find-related src/auth.py 42 ./my-project
​```

`
path
`
 defaults to the current directory when omitted; git URLs are accepted.

If 
`
semble
`
 is not on 
`
$PATH
`
, use 
`
uvx --from "semble[mcp]" semble
`
 in its place.

### 
Workflow

1
.
 Start with 
`
semble search
`
 to find relevant chunks.

2
.
 Inspect full files only when the returned chunk is not enough context.

3
.
 Optionally use 
`
semble find-related
`
 with a promising result's 
`
file_path
`
 and 
`
line
`
 to discover related implementations.

4
.
 Use grep only when you need exhaustive literal matches or quick confirmation of an exact string.

Once installed, runsemble savingsto see how many tokens Semble has saved you. Note that for sub-agent support in Claude Code or Codex, you need the fullBash / AGENTS.mdsetup below.

Updating Semble

pip install --upgrade semble 
#
 with pip

uv tool upgrade semble 
#
 with uv

uv cache clean semble 
#
 for MCP users (restart your MCP client after)

## Main Features

* Fast: indexes an average repo in ~250 ms and answers queries in ~1.5 ms, all on CPU.
* Accurate: NDCG@10 of 0.854 on ourbenchmarks, on par with code-specialized transformer models, at a fraction of the size and cost.
* Token-efficient: returns only the relevant chunks, using~98% fewer tokens than grep+read.
* Zero setup: runs on CPU with no API keys, GPU, or external services required.
* MCP server: works with Claude Code, Cursor, Codex, OpenCode, and any other MCP-compatible agent.
* Local and remote: pass a local path or a git URL.

## MCP Server

Semble can run as an MCP server so agents can search any codebase directly. Repos are cloned and indexed on demand, and indexes are cached for the lifetime of the session. Local paths are watched for file changes and re-indexed automatically.

### Setup

Requiresuvto be installed.

#### Claude Code

claude mcp add semble -s user -- uvx --from 
"
semble[mcp]
"
 semble

#### Codex

Add to~/.codex/config.toml:

[
mcp_servers
.
semble
]

command
 = 
"
uvx
"

args
 = [
"
--from
"
, 
"
semble[mcp]
"
, 
"
semble
"
]

#### OpenCode

Add to~/.opencode/config.json:

{
 
"mcp"
: {
 
"semble"
: {
 
"type"
: 
"
local
"
,
 
"command"
: [
"
uvx
"
, 
"
--from
"
, 
"
semble[mcp]
"
, 
"
semble
"
]
 }
 }
}

#### Cursor

Add to~/.cursor/mcp.json(or.cursor/mcp.jsonin your project):

{
 
"mcpServers"
: {
 
"semble"
: {
 
"command"
: 
"
uvx
"
,
 
"args"
: [
"
--from
"
, 
"
semble[mcp]
"
, 
"
semble
"
]
 }
 }
}

### Tools

Tool

Description

search

Search a codebase with a natural-language or code query. Pass 
repo
 as a local directory path or an https:// git URL.

find_related

Given a file path and line number, return chunks semantically similar to the code at that location.

## Bash / AGENTS.md

An alternative to MCP is to invoke Semble via Bash. For Claude Code and Codex CLI, this is the only option for sub-agents, which cannot call MCP tools directly, though it can also be used alongside MCP for the top-level agent.

To add Bash support, append the following to yourAGENTS.mdorCLAUDE.md:

## 
Code Search

Use 
`
semble search
`
 to find code by describing what it does or naming a symbol/identifier, instead of grep:

​```bash
semble search "authentication flow" ./my-project
semble search "save_pretrained" ./my-project
semble search "save model to disk" ./my-project --top-k 10
​```

Use 
`
semble find-related
`
 to discover code similar to a known location (pass 
`
file_path
`
 and 
`
line
`
 from a prior search result):

​```bash
semble find-related src/auth.py 42 ./my-project
​```

`
path
`
 defaults to the current directory when omitted; git URLs are accepted.

If 
`
semble
`
 is not on 
`
$PATH
`
, use 
`
uvx --from "semble[mcp]" semble
`
 in its place.

## 
Workflow

1
.
 Start with 
`
semble search
`
 to find relevant chunks.

2
.
 Inspect full files only when the returned chunk is not enough context.

3
.
 Optionally use 
`
semble find-related
`
 with a promising result's 
`
file_path
`
 and 
`
line
`
 to discover related implementations.

4
.
 Use grep only when you need exhaustive literal matches or quick confirmation of an exact string.

Claude Code sub-agent: Claude Code also supports a dedicated sub-agent. Run this once in your project root:

semble init

#
 or, if semble is not on $PATH:

uvx --from 
"
semble[mcp]
"
 semble init

This writes.claude/agents/semble-search.md.

## CLI

Semble also ships as a standalone CLI. This is useful in scripts or anywhere you want search results without an MCP session.

#
 Search a local repo

semble search 
"
authentication flow
"
 ./my-project

#
 Search for a symbol or identifier

semble search 
"
save_pretrained
"
 ./my-project

#
 Search a remote repo (cloned on demand)

semble search 
"
save model to disk
"
 https://github.com/MinishLab/model2vec

#
 Limit results

semble search 
"
save model to disk
"
 ./my-project --top-k 10

#
 Find code similar to a known location

semble find-related src/auth.py 42 ./my-project

pathdefaults to the current directory when omitted; git URLs are accepted. Ifsembleis not on$PATH, useuvx --from "semble[mcp]" semblein its place.

Savings

semble savingsshows how many tokens semble has saved across all your searches:

semble savings 
#
 summary by period

semble savings --verbose 
#
 also show breakdown by call type

 Semble Token Savings
 ════════════════════════════════════════════════════════════════
 Period Calls Savings
 ────────────────────────────────────────────────────────────────
 Today 42 [███████████████░] ~58.4k tokens (95%)
 Last 7 days 287 [██████████████░░] ~312.4k tokens (90%)
 All time 1.4k [██████████████░░] ~1.2M tokens (89%)

Savings are calculated as follows: for each call, semble records the total character count of the unique files containing returned chunks and the character count of the snippets returned. Estimated tokens saved is(file chars − snippet chars) / 4(4 chars per token). This is a conservative estimate: the baseline is reading matched files in full, which is how coding agents often explore unfamiliar code.

Stats are stored in~/.semble/savings.jsonl.

Library usage

Semble can also be used as a Python library for programmatic access, useful when building custom tooling or integrating search directly into your own code.

from
 
semble
 
import
 
SembleIndex

# Index a local directory

index
 
=
 
SembleIndex
.
from_path
(
"./my-project"
)

# Index a remote git repository

index
 
=
 
SembleIndex
.
from_git
(
"https://github.com/MinishLab/model2vec"
)

# Search the index with a natural-language or code query

results
 
=
 
index
.
search
(
"save model to disk"
, 
top_k
=
3
)

# Find code similar to a specific result

related
 
=
 
index
.
find_related
(
results
[
0
], 
top_k
=
3
)

# Each result exposes the matched chunk

result
 
=
 
results
[
0
]

result
.
chunk
.
file_path
 
# "model2vec/model.py"

result
.
chunk
.
start_line
 
# 127

result
.
chunk
.
end_line
 
# 150

result
.
chunk
.
content
 
# "def save_pretrained(self, path: PathLike, ..."

## Benchmarks

We benchmark quality and speed across ~1,250 queries over 63 repositories in 19 languages (left), and token efficiency against grep+read at equivalent recall levels (right).

The quality benchmark (left) scores retrieval quality (NDCG@10) against total latency; semble achieves 99% of the quality of the 137M-parameterCodeRankEmbedHybrid while indexing 218x faster. The token efficiency benchmark (right) measures how many tokens each method needs to reach a given recall level; semble uses 98% fewer tokens on average and hits 94% recall at only 2k tokens, while grep+read needs a full 100k context window to reach 85%. Seebenchmarksfor per-language results, ablations, and full methodology.

## How it works

Semble splits each file into code-aware chunks usingtree-sitter, then scores every query against the chunks with two complementary retrievers: staticModel2Vecembeddings using the code-specializedpotion-code-16Mmodel for semantic similarity, andBM25for lexical matches on identifiers and API names. The two score lists are fused with Reciprocal Rank Fusion (RRF).

After fusing, results are reranked with a set of code-aware signals:

Ranking signals

* Adaptive weighting.Symbol-like queries (Foo::bar,_private,getUserById) get more lexical weight, while natural-language queries stay balanced between semantic and lexical retrievers.
* Definition boosts.A chunk that defines the queried symbol (aclass,def,func, etc.) is ranked above chunks that merely reference it.
* Identifier stems.Query tokens are stemmed and matched against identifier stems in a chunk, giving an additional weight to chunks that contain them. For example, queryingparse configboosts chunks containingparseConfig,ConfigParser, orconfig_parser.
* File coherence.When multiple chunks from the same file match the query, the file is boosted so the top result reflects broad file-level relevance rather than a single out-of-context chunk.
* Noise penalties.Test files,compat//legacy/shims, example code, and.d.tsdeclaration stubs are down-ranked so canonical implementations surface first.

Because the embedding model is static with no transformer forward pass at query time, all of this runs in milliseconds on CPU.

## License

MIT

## Citing

If you use Semble in your research, please cite the following:

@software
{
minishlab2026semble
,
 
author
 = 
{
{van Dongen}, Thomas and Stephan Tulkens
}
,
 
title
 = 
{
Semble: Fast and Accurate Code Search for Agents
}
,
 
year
 = 
{
2026
}
,
 
publisher
 = 
{
Zenodo
}
,
 
doi
 = 
{
10.5281/zenodo.19785932
}
,
 
url
 = 
{
https://github.com/MinishLab/semble
}
,
 
license
 = 
{
MIT
}

}

## About

Fast and Accurate Code Search for Agents. Uses ~98% fewer tokens than grep+read

minish.ai/packages/semble/introduction/

### Topics

 retrieval

 mcp

 embeddings

 code-search

 agents

 model-context-protocol

 mcp-server

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2k

 stars
 

### Watchers

11

 watching
 

### Forks

89

 forks
 

 Report repository

 

## Releases8

v0.1.7

 Latest

 

May 12, 2026

 

+ 7 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python99.7%
* Makefile0.3%