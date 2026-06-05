---
title: 'GitHub - MemPalace/mempalace: The best-benchmarked open-source AI memory system. And it''s free. · GitHub'
url: https://github.com/MemPalace/mempalace
site_name: github
content_file: github-github-mempalacemempalace-the-best-benchmarked-ope
fetched_at: '2026-06-05T12:03:50.124246'
original_url: https://github.com/MemPalace/mempalace
author: MemPalace
description: The best-benchmarked open-source AI memory system. And it's free. - MemPalace/mempalace
---

MemPalace

 

/

mempalace

Public

* NotificationsYou must be signed in to change notification settings
* Fork7.1k
* Star53.6k

 
 
 
 
develop
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

1,136 Commits
1,136 Commits
.agents/
plugins
.agents/
plugins
 
 
.claude-plugin
.claude-plugin
 
 
.codex-plugin
.codex-plugin
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
assets
assets
 
 
benchmarks
benchmarks
 
 
docs
docs
 
 
examples
examples
 
 
hooks
hooks
 
 
integrations/
openclaw
integrations/
openclaw
 
 
landing
landing
 
 
mempalace
mempalace
 
 
tests
tests
 
 
tools
tools
 
 
website
website
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
MISSION.md
MISSION.md
 
 
README.md
README.md
 
 
ROADMAP.md
ROADMAP.md
 
 
SECURITY.md
SECURITY.md
 
 
openarena-claim.txt
openarena-claim.txt
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# MemPalace

Local-first AI memory. Verbatim storage, pluggable backend, 96.6% R@5 raw on LongMemEval — zero API calls.

Caution

Beware of impostor sites.MemPalace has no other official websites. Theonlyofficial sources are thisGitHub repository, thePyPI package, and the docs atmempalaceofficial.com. Any other domain (including.tech,.net, or other.comvariants) is an impostor and may distribute malware. Details and timeline:docs/HISTORY.md.

Important

Claude Code sessions expire in 30 days without auto-save hooks wired.Read this →

Need the shortest recovery/setup path? Use theClaude Code retention setup checklist.

## What it is

MemPalace stores your conversation history as verbatim text and retrieves
it with semantic search. It does not summarize, extract, or paraphrase.
The index is structured — people and projects becomewings, topics
becomerooms, and original content lives indrawers— so searches
can be scoped rather than run against a flat corpus.

The retrieval layer is pluggable. The current default is ChromaDB; the
interface is defined inmempalace/backends/base.pyand alternative backends can be dropped in without touching the rest of
the system.

Nothing leaves your machine unless you opt in.

Architecture, concepts, and mining flows:mempalaceofficial.com/concepts/the-palace.

## Install

MemPalace ships a CLI, so install it in an isolated environment to avoid
PEP 668 errors on Debian/Ubuntu/Homebrew Pythons and to keep mempalace's
deps (chromadb,numpy,grpcio, …) from conflicting with anything
else in your global site-packages.

We recommenduv—uv tool installputs
themempalaceCLI in an isolated environment on your PATH:

uv tool install mempalace
mempalace init 
~
/projects/myapp

pipxworks the same way if you prefer it:pipx install mempalace.

Prefer plainpiponly inside an activated virtualenv where you
explicitly wantimport mempalaceavailable:

python -m venv .venv 
&&
 
source
 .venv/bin/activate
pip install mempalace

## Quickstart

#
 Mine content into the palace

mempalace mine 
~
/projects/myapp 
#
 project files

mempalace mine 
~
/.claude/projects/ --mode convos 
#
 Claude Code sessions (scope with --wing per project)

#
 Search

mempalace search 
"
why did we switch to GraphQL
"

#
 Load context for a new session

mempalace wake-up

For Claude Code, Gemini CLI, MCP-compatible tools, and local models, seemempalaceofficial.com/guide/getting-started.

## Benchmarks

All numbers below are reproducible from this repository with the commands
inbenchmarks/BENCHMARKS.md. Full
per-question result files are committed underbenchmarks/results_*.

LongMemEval — retrieval recall (R@5, 500 questions):

Mode

R@5

LLM required

Raw (semantic search, no heuristics, no LLM)

96.6%

None

Hybrid v4, held-out 450q (tuned on 50 dev, not seen during training)

98.4%

None

Hybrid v4 + LLM rerank (full 500)

≥99%

Any capable model

The raw 96.6% requires no API key, no cloud, and no LLM at any stage. The
hybrid pipeline adds keyword boosting, temporal-proximity boosting, and
preference-pattern extraction; the held-out 98.4% is the honest
generalisable figure.

The rerank pipeline promotes the best candidate out of the top-20
retrieved sessions using an LLM reader. It works with any reasonably
capable model — we have reproduced it with Claude Haiku, Claude Sonnet,
and minimax-m2.7 via Ollama Cloud (no Anthropic dependency). The gap
between raw and reranked is model-agnostic; we do not headline a "100%"
number because the last 0.6% was reached by inspecting specific wrong
answers, whichbenchmarks/BENCHMARKS.mdflags as teaching to the test.

Other benchmarks (full results inbenchmarks/BENCHMARKS.md):

Benchmark

Metric

Score

Notes

LoCoMo (session, top-10, no rerank)

R@10

60.3%

1,986 questions

LoCoMo (hybrid v5, top-10, no rerank)

R@10

88.9%

Same set

ConvoMem (all categories, 250 items)

Avg recall

92.9%

50 per category

MemBench (ACL 2025, 8,500 items)

R@5

80.3%

All categories

We deliberately do not include a side-by-side comparison against Mem0,
Mastra, Hindsight, Supermemory, or Zep. Those projects publish different
metrics on different splits, and placing retrieval recall next to
end-to-end QA accuracy is not an honest comparison. See each project's
own research page for their published numbers.

Reproducing every result:

git clone https://github.com/MemPalace/mempalace.git

cd
 mempalace
uv sync --extra dev 
#
 or: pip install -e ".[dev]"

#
 see benchmarks/README.md for dataset download commands

uv run python benchmarks/longmemeval_bench.py /path/to/longmemeval_s_cleaned.json

## Knowledge graph

MemPalace includes a temporal entity-relationship graph with validity
windows — add, query, invalidate, timeline — backed by local SQLite.
Usage and tool reference:mempalaceofficial.com/concepts/knowledge-graph.

## MCP server

29 MCP tools cover palace reads/writes, knowledge-graph operations,
cross-wing navigation, drawer management, and agent diaries. Installation
and the full tool list:mempalaceofficial.com/reference/mcp-tools.

## Agents

Each specialist agent gets its own wing and diary in the palace.
Discoverable at runtime viamempalace_list_agents— no bloat in your
system prompt:mempalaceofficial.com/concepts/agents.

## Auto-save hooks

Two Claude Code hooks save periodically and before context compression:mempalaceofficial.com/guide/hooks.

If you are installing under time pressure, start with theClaude Code retention setup checklist:
wire the hooks, back up existing JSONL transcripts, and backfill them withmempalace mine ~/.claude/projects/ --mode convos.

For per-message recall on top of the file-level chunks the hooks produce,
runmempalace sweep <transcript-dir>periodically — it stores one
verbatim drawer per user/assistant message, idempotent and resume-safe.

## Requirements

* Python 3.9+
* A vector-store backend (ChromaDB by default)
* ~300 MB disk for the embedding model. Onboarding (python -m mempalace.onboarding) offersembeddinggemma-300m(multilingual, 100+ languages, recommended) orall-MiniLM-L6-v2(English-only, ~30 MB). See the docstring atmempalace/embedding.pyfor details and migration notes.

No API key is required for the core benchmark path.

## Docs

* Getting started →mempalaceofficial.com/guide/getting-started
* CLI reference →mempalaceofficial.com/reference/cli
* Python API →mempalaceofficial.com/reference/python-api
* Full benchmark methodology →benchmarks/BENCHMARKS.md
* Release notes →CHANGELOG.md
* Corrections and public notices →docs/HISTORY.md

## Contributing

PRs welcome. SeeCONTRIBUTING.md.

## License

MIT — seeLICENSE.

## About

The best-benchmarked open-source AI memory system. And it's free.

mempalaceofficial.com/

### Topics

 python

 ai

 memory

 mcp

 llm

 chromadb

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

53.6k

 stars
 

### Watchers

308

 watching
 

### Forks

7.1k

 forks
 

 Report repository

 

## Releases8

v3.3.5 — integrity, recovery, and cross-process correctness

 Latest

 

May 10, 2026

 

+ 7 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python94.0%
* HTML2.2%
* CSS1.5%
* Shell1.0%
* Vue0.7%
* JavaScript0.4%
* TypeScript0.2%