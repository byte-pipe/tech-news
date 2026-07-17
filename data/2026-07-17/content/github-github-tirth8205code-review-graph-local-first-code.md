---
title: 'GitHub - tirth8205/code-review-graph: Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools read only what matters, with benchmarked context reductions on reviews and large-repo workflows. · GitHub'
url: https://github.com/tirth8205/code-review-graph
site_name: github
content_file: github-github-tirth8205code-review-graph-local-first-code
fetched_at: '2026-07-17T11:31:44.688475'
original_url: https://github.com/tirth8205/code-review-graph
author: tirth8205
description: Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools read only what matters, with benchmarked context reductions on reviews and large-repo workflows. - tirth8205/code-review-graph
---

tirth8205

 

/

code-review-graph

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.1k
* Star19.6k

 
 
 
 
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

493 Commits
493 Commits
.beads
.beads
 
 
.github
.github
 
 
.serena
.serena
 
 
code-review-graph-vscode
code-review-graph-vscode
 
 
code_review_graph
code_review_graph
 
 
diagrams
diagrams
 
 
docs
docs
 
 
evaluate/
results
evaluate/
results
 
 
hooks
hooks
 
 
scripts
scripts
 
 
skills
skills
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.mcp.json
.mcp.json
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GEMINI.md
GEMINI.md
 
 
LICENSE
LICENSE
 
 
README.hi-IN.md
README.hi-IN.md
 
 
README.ja-JP.md
README.ja-JP.md
 
 
README.ko-KR.md
README.ko-KR.md
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SECURITY.md
SECURITY.md
 
 
action.yml
action.yml
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# code-review-graph

Stop burning tokens. Start reviewing smarter.

English|简体中文|日本語|한국어|हिन्दी

Usage·Commands·FAQ·Troubleshooting·GitHub Action·Reproducing the benchmarks·Roadmap

AI coding tools can end up re-reading large parts of your codebase on review tasks.code-review-graphfixes that. It builds a structural map of your code withTree-sitter, tracks changes incrementally, and gives your AI assistant precise context viaMCPso it reads only what matters.

## Quick Start

pip install code-review-graph 
#
 or: pipx install code-review-graph

code-review-graph install 
#
 auto-detects and configures all supported platforms

code-review-graph build 
#
 parse your codebase

One command sets up everything.installdetects which AI coding tools you have, writes the correct MCP configuration for each one, installs platform-native hooks/skills where supported, and injects graph-aware instructions into your platform rules. It auto-detects whether you installed viauvxorpip/pipxand generates the right config. Restart your editor/tool after installing.

To target a specific platform:

code-review-graph install --platform codex 
#
 configure only Codex

code-review-graph install --platform cursor 
#
 configure only Cursor

code-review-graph install --platform claude-code 
#
 configure only Claude Code

code-review-graph install --platform gemini-cli 
#
 configure only Gemini CLI

code-review-graph install --platform kiro 
#
 configure only Kiro

code-review-graph install --platform copilot 
#
 configure only GitHub Copilot (VS Code)

code-review-graph install --platform copilot-cli 
#
 configure only GitHub Copilot CLI

Requires Python 3.10+. For the best experience, installuv(the MCP config will useuvxif available, otherwise falls back to thecode-review-graphcommand directly).

Then open your project and ask your AI assistant:

Build the code review graph for this project

The initial build takes ~10 seconds for a 500-file project. After that, watch mode and supported hooks can keep the graph updated automatically.

## How It Works

Your repository is parsed into an AST with Tree-sitter, stored as a graph of nodes (functions, classes, imports) and edges (calls, inheritance, test coverage), then queried at review time to compute the minimal set of files your AI assistant needs to read.

### Blast-radius analysis

When a file changes, the graph traces every caller, dependent, and test that could be affected. This is the "blast radius" of the change. Your AI reads only these files instead of scanning the whole project.

### Incremental updates in < 2 seconds

When hooks or watch mode are enabled, file saves and supported commit hooks trigger incremental updates. The graph diffs changed files, finds their dependents via SHA-256 hash checks, and re-parses only what changed. A 2,900-file project re-indexes in under 2 seconds.

### The monorepo problem, solved

Large monorepos are where token waste is most painful. The graph cuts through the noise — 27,700+ files excluded from review context, only ~15 files actually read.

### Broad language coverage + Jupyter notebooks

Parser support covers functions, classes, imports, call sites, inheritance, and test detection across the current parser surface, using Tree-sitter where available and targeted fallbacks where needed. Current support includes Python, JavaScript/TypeScript/TSX, Go, Rust, Java, C/C++, C#, Ruby, Kotlin, Swift, PHP, Scala, Solidity, Dart, R, Perl, Lua/Luau, Objective-C, shell scripts, Elixir, Zig, PowerShell, Julia, ReScript, GDScript, Nix, Verilog/SystemVerilog, SQL, Vue/Svelte SFCs, Astro files parsed through the TypeScript parser, Jupyter/Databricks notebooks (.ipynb), and Perl XS files (.xs).

### Add your own language (no fork needed)

If your repo uses a language the parser does not cover yet, drop alanguages.tomlinto.code-review-graph/mapping file extensions to any grammar bundled intree_sitter_language_pack, plus the tree-sitter node types for functions, classes, imports, and calls:

[
languages
.
erlang
]

extensions
 = [
"
.erl
"
]

grammar
 = 
"
erlang
"

function_node_types
 = [
"
function_clause
"
]

class_node_types
 = [
"
record_decl
"
]

import_node_types
 = [
"
import_attribute
"
]

call_node_types
 = [
"
call
"
]

The generic tree-sitter walker handles extraction from there — no code changes, and built-in languages can never be overridden. Seedocs/CUSTOM_LANGUAGES.mdfor the schema reference, validation rules, and a worked end-to-end example.

### Risk-scored PR reviews in CI (GitHub Action)

The same analysis runs as a composite GitHub Action — and it stays local-first: the knowledge graph is built and queried entirely on your CI runner, with no source code sent to any external service. On each pull request the action posts a single sticky comment with risk-scored functions, affected execution flows, and test gaps, updated in place on every push. An optionalfail-on-riskinput turns the review into a merge gate.

#
 .github/workflows/code-review-graph.yml

on
:
 
pull_request
:

permissions
:
 
contents
: 
read

 
pull-requests
: 
write

jobs
:
 
review
:
 
runs-on
: 
ubuntu-latest

 
steps
:
 - 
uses
: 
actions/checkout@v4

 - 
uses
: 
tirth8205/code-review-graph@v2.3.6

 
with
:
 
github-token
: 
${{ secrets.GITHUB_TOKEN }}

Seedocs/GITHUB_ACTION.mdfor inputs, risk levels, and caching details, or the dogfood workflow this repo runs on itself in.github/workflows/pr-review.yml.

## Benchmarks

Headline number: the median per-question token reduction across the 6 repos is ~82x(whole-corpus baseline vs graph query). The frequently quoted528x is the maximum— a single best-case repo (fastapi) — not the typical result.

All numbers come from the automated evaluation runner against 6 real open-source repositories (13 commits total). Every config pins an upstream SHA, the Leiden community detector runs with a fixed seed, and embeddings are deterministic on CPU — so two runs on different machines produce identical numbers. The full reproduction recipe with expected outputs is indocs/REPRODUCING.md. A weekly report-only run on the two smallest configs lives in.github/workflows/eval.yml.

Token efficiency: ~82x median per-question reduction (range 38x – 528x; whole-corpus vs graph query)

For a typical agent question ("how does authentication work","what is the main entry point", etc.), the graph returns ~2,000–3,500 tokens of targeted search hits + neighbor edges instead of forcing the agent to read every source file. The table below averages over the 5 sample questions defined incode_review_graph/token_benchmark.py.

Repo

Snapshot SHA

naive_corpus_tokens

avg graph_tokens

Reduction

fastapi

0227991a

951,071

2,169

528.4x

code-review-graph

84bde354

208,821

2,495

93.0x

gin

5c00df8a

166,868

1,990

91.8x

flask

a29f88ce

125,022

1,986

71.4x

express

b4ab7d65

135,955

3,465

40.6x

httpx

b55d4635

89,492

2,438

38.0x

Median per-question reduction across the 6 repos:~82x. The range is 38x – 528x, where528x is the best case(fastapi, the largest corpus), not the headline.

The whole-corpus baseline above is an upper bound no real agent pays: a competent agent greps for identifiers and reads only the best-matching files. Theagent_baselineeval benchmark measures that realistic baseline — a pure-python grep over the corpus, top-3 files by match count, token-counted and compared to the graph query cost (evaluate/results/<repo>_agent_baseline_*.csv).

The formaleval/benchmarks/token_efficiency.pybenchmark measures a different scenario — fullget_review_context()JSON versus just the changed-file content of a commit — and reports ratios below 1 for small commits, because the review-context response carries impact-radius edges plus source snippets that exceed a tiny single-file diff. That is not a bug; the two benchmarks answer different questions. Seedocs/REPRODUCING.mdfor the full methodology.

Since v2.3.4, review and impact tools attach a compactcontext_savingsestimate so MCP clients can see the approximate context saved per call. In v2.3.5 the CLI surfaces this as the boxedToken Savingspanel shown above (see "Token Savings panel" in the Usage section) and adds--verifyto cross-check against OpenAI'scl100k_basetokenizer. Calibration data indocs/REPRODUCING.mdshows the estimate is within ~1% of real GPT-4 tokens in aggregate across 222 sample files.

Impact accuracy: 0.71 average F1 against graph-derived ground truth (recall 1.0 is a circular upper bound, not "100% recall")

Blast-radius analysis recovers every file in the ground truth on all 13 evaluation commits —but read that as an upper bound, not as "100% recall": in this mode the ground truth (changed files + files with call/import edges into them) is derived from the same graph the predictor traverses, so it is circular by construction. The over-prediction visible in the precision column is a deliberate trade-off: better to flag too many files than miss a broken dependency.

Repo

Commits

Avg F1

Avg Precision

Recall (graph-derived upper bound)

httpx

2

0.864

0.786

1.0

fastapi

2

0.834

0.750

1.0

code-review-graph

2

0.734

0.584

1.0

express

2

0.667

0.500

1.0

flask

2

0.628

0.481

1.0

gin

3

0.609

0.439

1.0

Average

13

0.714

0.578

1.000

The benchmark also runs an honestco-change mode: the predictor is seeded with a single changed file and graded against theotherfiles the author actually touched in the same commit — independent-ish evidence from git history, not from the graph. Both modes appear side by side in the result CSVs (ground_truth_modecolumn). Co-change numbers will be added to the canonical stats once captured by the eval runner; we do not quote them before measuring.

Build performance

Repo

Files

Nodes

Edges

Flow Detection

Search Latency

express

141

1,910

17,553

106ms

0.7ms

fastapi

1,122

6,285

27,117

128ms

1.5ms

flask

83

1,446

7,974

95ms

0.7ms

gin

99

1,286

16,762

111ms

0.5ms

httpx

60

1,253

7,896

96ms

0.4ms

### Limitations and known weaknesses

* Impact "recall 1.0" is graph-derived and circular:the historical ground truth comes from the same graph edges the predictor walks, so it is an upper bound by construction. The honest co-change mode (grade against files actually co-changed in the same commit) is measured alongside it; expect those numbers to be substantially lower.
* Small single-file changes:Graph context can exceed naive file reads for trivial edits (see express results above). The overhead is the structural metadata that enables multi-file analysis.
* Search quality (MRR 0.35):Keyword search finds the right result in the top-4 for most queries, but ranking needs improvement. Express queries return 0 hits due to module-pattern naming.
* Flow detection (33% recall):Only reliably detects entry points in Python repos (fastapi, httpx) where framework patterns are recognized. JavaScript and Go flow detection needs work.
* Precision vs recall trade-off:Impact analysis is deliberately conservative. It flags files thatmightbe affected, which means some false positives in large dependency graphs.

## Features

Feature

Details

Incremental updates

Re-parses only changed files. Subsequent updates complete in under 2 seconds.

Broad language + notebook support

Python, JavaScript/TypeScript/TSX, Go, Rust, Java, C/C++, C#, Ruby, Kotlin, Swift, PHP, Scala, Solidity, Dart, R, Perl, Lua/Luau, Objective-C, shell scripts, Elixir, Zig, PowerShell, Julia, ReScript, GDScript, Nix, Verilog/SystemVerilog, SQL, Vue/Svelte SFCs, Astro files parsed through the TypeScript parser, Jupyter/Databricks (.ipynb), and Perl XS (.xs)

Blast-radius analysis

Shows which functions, classes, and files are likely affected by a change

Auto-update hooks

Hooks and watch mode can update the graph on file saves and supported commit hooks

Semantic search

Optional vector embeddings via sentence-transformers, Google Gemini, MiniMax, or any OpenAI-compatible endpoint (real OpenAI, Azure, new-api, LiteLLM, vLLM, LocalAI)

Interactive visualisation

D3.js force-directed graph with search, community legend toggles, and degree-scaled nodes

Hub & bridge detection

Find most-connected nodes and architectural chokepoints via betweenness centrality

Surprise scoring

Detect unexpected coupling: cross-community, cross-language, peripheral-to-hub edges

Knowledge gap analysis

Identify isolated nodes, untested hotspots, thin communities, and structural weaknesses

Suggested questions

Auto-generated review questions from graph analysis (bridges, hubs, surprises)

Edge confidence

Three-tier confidence scoring (EXTRACTED/INFERRED/AMBIGUOUS) with float scores on edges

Graph traversal

Free-form BFS/DFS exploration from any node with configurable depth and token budget

Export formats

GraphML (Gephi/yEd), Neo4j Cypher, Obsidian vault with wikilinks, SVG static graph

Graph diff

Compare graph snapshots over time: new/removed nodes, edges, community changes

Token benchmarking

Measure naive full-corpus tokens vs graph query tokens with per-question ratios

Estimated context savings

Compact 
context_savings
 metadata on relevant MCP/CLI review outputs, labelled as estimated and kept to three small fields

Memory loop

Persist Q&A results as markdown for re-ingestion, so the graph grows from queries

Community auto-split

Oversized communities (>25% of graph) are recursively split via Leiden

Execution flows

Trace call chains from entry points, sorted by weighted criticality

Community detection

Cluster related code via Leiden algorithm with resolution scaling for large graphs

Architecture overview

Auto-generated architecture map with coupling warnings

Risk-scored reviews

detect_changes
 maps diffs to affected functions, flows, and test gaps

Custom languages

Add new languages via 
.code-review-graph/languages.toml
 — no fork or code changes needed

GitHub Action

Sticky risk-scored PR review comments in CI, with an optional 
fail-on-risk
 merge gate

Refactoring tools

Rename preview, framework-aware dead code detection, community-driven suggestions

Wiki generation

Auto-generate markdown wiki from community structure

Multi-repo registry

Register multiple repos, search across all of them

Multi-repo daemon

crg-daemon
 watches multiple repos as child processes, with health checks and auto-restart

MCP prompts

5 workflow templates: review, architecture, debug, onboard, pre-merge

Full-text search

FTS5-powered hybrid search combining keyword and vector similarity

Local storage

SQLite file in 
.code-review-graph/
. Core graph storage needs no external database or cloud service.

Watch mode

Continuous graph updates as you work

## Usage

Slash commands

Command

Description

/code-review-graph:build-graph

Build or rebuild the code graph

/code-review-graph:review-delta

Review changes since last commit

/code-review-graph:review-pr

Full PR review with blast-radius analysis

CLI reference

code-review-graph install 
#
 Auto-detect and configure all platforms

code-review-graph install --platform 
<
name
>
 
#
 Target a specific platform

code-review-graph build 
#
 Parse entire codebase

code-review-graph update 
#
 Incremental update (changed files only)

code-review-graph status 
#
 Graph statistics

code-review-graph watch 
#
 Auto-update on file changes

code-review-graph visualize 
#
 Generate interactive HTML graph

code-review-graph visualize --format graphml 
#
 Export as GraphML

code-review-graph visualize --format svg 
#
 Export as SVG

code-review-graph visualize --format obsidian 
#
 Export as Obsidian vault

code-review-graph visualize --format cypher 
#
 Export as Neo4j Cypher

code-review-graph wiki 
#
 Generate markdown wiki from communities

code-review-graph detect-changes --brief 
#
 Risk panel + token savings (read-only)

code-review-graph update --brief 
#
 Refresh graph + same panel

code-review-graph detect-changes --brief --verify 
#
 Cross-check vs tiktoken

code-review-graph register 
<
path
>
 
#
 Register repo in multi-repo registry

code-review-graph unregister 
<
id
>
 
#
 Remove repo from registry

code-review-graph repos 
#
 List registered repositories

code-review-graph daemon start 
#
 Start multi-repo watch daemon

code-review-graph daemon stop 
#
 Stop the daemon

code-review-graph daemon status 
#
 Show daemon status and repos

code-review-graph 
eval
 
#
 Run evaluation benchmarks

code-review-graph serve 
#
 Start MCP server

Token Savings panel: 
detect-changes --brief
 vs 
update --brief

Both commands print the same compact panel showing how many tokens the
graph saved you compared to handing the changed files to an agent raw.
They differ inonething: whether the graph gets refreshed first.

┌─────────────────────── Token Savings ────────────────────────┐
│ Full context would be: 12,921 tokens │
│ Graph context used: 762 tokens │
│ Saved: 12,159 tokens (~94%) │
│ Breakdown: Functions 244 · Tests 191 · Risk 244 · Other 83 │
└──────────────────────────────────────────────────────────────┘

Command

What it does

When to use

detect-changes --brief

Read-only.
 Looks at your current changes, queries the 
existing
 graph, prints the panel. ~1 sec.

Most of the time — the hooks (or 
crg-daemon
) keep the graph fresh in the background, so this is enough.

update --brief

Re-parses your changed files into the graph first
, then prints the same panel. ~5 sec.

After a rebase, a large change set, or any time you suspect the graph is stale.

Both end with thesame panelbecause both call the sameanalyze_changes()step at the end. The difference is whether the graph itself got refreshed before that analysis ran.

Add--verifyto either command to cross-check the displayed numbers against OpenAI'scl100k_basetokenizer (the GPT-4 family). Requirespip install tiktoken. The estimate stays within ~1% of real tokens on a typical change set — seedocs/REPRODUCING.mdfor the calibration data.

The samecontext_savingsmetadata is also attached automatically to the JSON responses ofget_impact_radius,get_review_context,detect_changes, andget_architecture_overviewMCP tools, so AI agents can surface the savings to humans in chat without any extra prompting.

Multi-repo daemon

If your editor doesn't support hooks (e.g. Cursor, OpenCode), or you just want your
graph to stay fresh in the background without any editor integration, the daemon is
for you. It watches your repos for file changes and automatically rebuilds the graph
— no manualbuildorupdatecommands needed.

The daemon is included withcode-review-graph— no separate install required.

Quick setup:

#
 1. Register the repos you want to watch

crg-daemon add 
~
/project-a --alias proj-a
crg-daemon add 
~
/project-b

#
 2. Start the daemon (runs in the background)

crg-daemon start

#
 3. That's it — graphs stay up to date automatically

crg-daemon status 
#
 check daemon and per-repo watcher status

crg-daemon logs --repo proj-a -f 
#
 tail logs for a specific repo

crg-daemon stop 
#
 stop daemon and all watcher processes

Also available ascode-review-graph daemon start|stop|status|....

Under the hood,crg-daemon addwrites to a TOML config file at~/.code-review-graph/watch.toml. You can also edit this file directly:

[[
repos
]]

path
 = 
"
/home/user/project-a
"

alias
 = 
"
proj-a
"

[[
repos
]]

path
 = 
"
/home/user/project-b
"

alias
 = 
"
project-b
"

The daemon monitors this config file for changes and automatically starts/stops
watcher processes as repos are added or removed. Health checks every 30 seconds
restart dead watchers. No external dependencies required.

Seedocs/COMMANDS.mdfor the
full config reference and all available options.

30 MCP tools

Your AI assistant uses these automatically once the graph is built.

Tool

Description

build_or_update_graph_tool

Build or incrementally update the graph

run_postprocess_tool

Re-run flow detection, community detection, and FTS indexing

get_minimal_context_tool

Ultra-compact context (~100 tokens) — call this first

get_impact_radius_tool

Blast radius of changed files

get_review_context_tool

Token-optimised review context with structural summary

query_graph_tool

Callers, callees, tests, imports, inheritance queries

traverse_graph_tool

BFS/DFS traversal from any node with token budget

semantic_search_nodes_tool

Search code entities by name or meaning

embed_graph_tool

Compute vector embeddings for semantic search

list_graph_stats_tool

Graph size and health

get_docs_section_tool

Retrieve documentation sections

find_large_functions_tool

Find functions/classes exceeding a line-count threshold

list_flows_tool

List execution flows sorted by criticality

get_flow_tool

Get details of a single execution flow

get_affected_flows_tool

Find flows affected by changed files

list_communities_tool

List detected code communities

get_community_tool

Get details of a single community

get_architecture_overview_tool

Architecture overview from community structure

detect_changes_tool

Risk-scored change impact analysis for code review

get_hub_nodes_tool

Find most-connected nodes (architectural hotspots)

get_bridge_nodes_tool

Find chokepoints via betweenness centrality

get_knowledge_gaps_tool

Identify structural weaknesses and untested hotspots

get_surprising_connections_tool

Detect unexpected cross-community coupling

get_suggested_questions_tool

Auto-generated review questions from analysis

refactor_tool

Rename preview, dead code detection, suggestions

apply_refactor_tool

Apply a previously previewed refactoring

generate_wiki_tool

Generate markdown wiki from communities

get_wiki_page_tool

Retrieve a specific wiki page

list_repos_tool

List registered repositories

cross_repo_search_tool

Search across all registered repositories

MCP Prompts(5 workflow templates):review_changes,architecture_map,debug_issue,onboard_developer,pre_merge_check

Configuration

To exclude paths from indexing, create a.code-review-graphignorefile in your repository root:

generated/**
*.generated.ts
vendor/**
node_modules/**

Note: in git repos, only tracked files are indexed (git ls-files), so gitignored files are skipped automatically. Use.code-review-graphignoreto exclude tracked files or when git isn't available.

Optional dependency groups:

pip install code-review-graph[embeddings] 
#
 Local vector embeddings (sentence-transformers)

pip install code-review-graph[google-embeddings] 
#
 Google Gemini embeddings

pip install code-review-graph[communities] 
#
 Community detection (igraph)

pip install code-review-graph[enrichment] 
#
 Python call-resolution enrichment (Jedi)

pip install code-review-graph[eval] 
#
 Evaluation benchmarks (matplotlib)

pip install code-review-graph[wiki] 
#
 Wiki generation with LLM summaries (ollama)

pip install code-review-graph[all] 
#
 All optional dependencies

### Environment Variables

Variable

Description

Default

CRG_GIT_TIMEOUT

Timeout in seconds for Git operations

30

CRG_DATA_DIR

Override directory for graph databases and generated graph artefacts

-

CRG_EMBEDDING_MODEL

Default model for vector embeddings

all-MiniLM-L6-v2

CRG_ACCEPT_CLOUD_EMBEDDINGS

Suppress the cloud embedding egress warning after explicit acknowledgement

-

CRG_ALLOW_REMOTE_CODE

Allow HuggingFace models that require 
trust_remote_code=True

0

CRG_MAX_IMPACT_NODES

Maximum nodes to include in impact analysis

500

CRG_MAX_IMPACT_DEPTH

Search depth for blast-radius analysis

2

CRG_MAX_BFS_DEPTH

Maximum depth for graph traversal

15

CRG_MAX_CHANGED_FUNCS

Maximum changed functions analysed in one change report

500

CRG_MAX_TRANSITIVE_FRONTIER

Maximum frontier size for transitive caller/callee expansion

50

CRG_TOOL_TIMEOUT

Optional timeout in seconds for bounded MCP tools (
0
 disables timeout)

0

CRG_RECURSE_SUBMODULES

Include git submodules in file collection when set to 
1
, 
true
, or 
yes

-

CRG_TOOLS

Comma-separated allowlist of MCP tools to expose when serving

-

GOOGLE_API_KEY

API key for Google Gemini embeddings

-

MINIMAX_API_KEY

API key for MiniMax embeddings

-

CRG_OPENAI_BASE_URL

OpenAI-compatible embeddings endpoint

-

CRG_OPENAI_API_KEY

API key for OpenAI-compatible embeddings

-

CRG_OPENAI_MODEL

Model name for OpenAI-compatible embeddings

-

CRG_OPENAI_DIMENSION

Pin embedding dimension (v3 models support reduction)

-

NO_COLOR

If set, disables ANSI colors in terminal

-

CRG_SERIAL_PARSE

If 
1
, disables parallel parsing (use for debugging)

-

OpenAI-compatible embeddings (real OpenAI, Azure, or any self-hosted gateway like
new-api / LiteLLM / vLLM / LocalAI / Ollama in openai mode) need no extra install —
just set the environment variables and passprovider="openai"toembed_graph:

export
 CRG_OPENAI_BASE_URL=http://127.0.0.1:3000/v1 
#
 or https://api.openai.com/v1

export
 CRG_OPENAI_API_KEY=sk-...

export
 CRG_OPENAI_MODEL=text-embedding-3-small 
#
 whatever your gateway serves

#
 optional:

export
 CRG_OPENAI_DIMENSION=1536 
#
 pin dim (v3 models support reduction)

export
 CRG_OPENAI_BATCH_SIZE=100 
#
 lower for gateways with tight limits

 
#
 (e.g. Qwen text-embedding-v4 caps at 10)

The cloud-egress warning is auto-skipped when the base URL points to localhost
(127.0.0.1,localhost,0.0.0.0,::1).

Model selection tip.Avoid-preview/-beta/-expmodel IDs
(e.g.google/gemini-embedding-2-preview) for anything you plan to keep
long-term — preview models can change weights (different dimension → full
re-embed required) or be deprecated without notice. Prefer stable GA
releases such astext-embedding-3-small/text-embedding-3-large(OpenAI),Qwen/Qwen3-Embedding-8B(via self-hosted vLLM / LocalAI), orgemini-embedding-001(via the native Gemini provider, which requiresGOOGLE_API_KEYinstead of the OpenAI-compatible path).

Also note:code-review-graphcurrently embedsfunction signatures only(~10 tokens per node, e.g."parse_file function (path: str) returns Tree").
Models whose headline quality comes from long-context body understanding
(such as Gemini 2 or Qwen3-8B at their MTEB-code SOTA scores) will see a
much narrower quality gap against smaller models at this input length.
Body/docstring embedding is tracked as a follow-up enhancement.

#### Tool Filtering

CRG exposes 30 MCP tools by default. In token-constrained environments, you can
limit the server to a subset of tools using--toolsor theCRG_TOOLSenvironment variable:

#
 Via CLI flag

code-review-graph serve --tools query_graph_tool,semantic_search_nodes_tool,detect_changes_tool

#
 Via environment variable

CRG_TOOLS=query_graph_tool,semantic_search_nodes_tool code-review-graph serve

The CLI flag takes precedence over the environment variable. When neither is set,
all tools are available. This is especially useful for MCP client configurations:

{
 
"mcpServers"
: {
 
"code-review-graph"
: {
 
"command"
: 
"
code-review-graph
"
,
 
"args"
: [
"
serve
"
, 
"
--tools
"
, 
"
query_graph_tool,semantic_search_nodes_tool,detect_changes_tool,get_review_context_tool
"
]
 }
 }
}

## FAQ & how it compares

Short, honest answers indocs/FAQ.md:

* vs LSP / language servers— one persistent cross-language graph instead of per-language daemons; LSP stays more precise per symbol.
* vs RAG / embeddings— structural edges parsed from the AST, not similarity chunks; embeddings are optional and only assist search.
* vs grep / agentic search— grep wins on one-hop lookups; the graph wins on multi-hop questions (impact radius, callers-of-callers, tests-for, affected flows).
* vs Serena, codegraph, claude-context, repomix— factual comparison table.
* When NOT to use it— small repos, trivial single-file diffs, one-off questions.
* Does it phone home?— no; zero telemetry, cloud embeddings are opt-in.
* How do I verify it is working?—status,detect-changes --brief,/mcp.

## Troubleshooting

### pip/pipxcannot downloadhatchling(orErrno 9/Bad file descriptorto PyPI)

Installing from asource tree(for examplepipx install .) needs build dependencies fromPyPI(for examplehatchling). If you seeCould not find a version that satisfies the requirement hatchlingafter connection warnings, the Python/pip in thatterminalmay not be able to open an HTTPS client topypi.org(sometimes seen in an integrated editor terminal; less often system-wide with VPN, firewall, or proxy).

Options:

1. Run the same command frommacOS Terminal.app(or iTerm) instead of the IDE’s terminal, then retrypipx install .orpipx install "git+https://...".
2. Useuvto install the CLI from a checkout (uses different download machinery thanpipin many cases):cd/path/to/code-review-graph
uv tool install.--force
3. Fordevelopment in a clonewithout a global install, useuv syncanduv run code-review-graph …(or activate.venvafteruv sync).

Diagnose (optional):python3 scripts/diagnose_pypi_connectivity.py— if it printsFAILED, the issue is environment/network, not a wrong package name in this repo.

### Windows Configuration Issues (Invalid JSON / Connection Closed)

If you are using Windows and encounterInvalid JSON: EOF while parsingorMCP error -32000: Connection closedwhen connecting via Claude Code, do not use thecmd /cwrapper in your config.

Ensurefastmcpis updated to at least3.2.4+. Then, configure your~/.claude.jsonto execute the.exedirectly and pass the UTF-8 environment variable via the config:

"code-review-graph"
: {
 
"command"
: 
"
C:
\\
path
\\
to
\\
your
\\
venv
\\
Scripts
\\
code-review-graph.exe
"
,
 
"args"
: [
"
serve
"
, 
"
--repo
"
, 
"
C:
\\
path
\\
to
\\
your
\\
project
"
],
 
"env"
: { 
"PYTHONUTF8"
: 
"
1
"
 }
}

## Contributing

git clone https://github.com/tirth8205/code-review-graph.git

cd
 code-review-graph
python3 -m venv .venv 
&&
 
source
 .venv/bin/activate
pip install -e 
"
.[dev]
"

pytest

Adding a new language

Editcode_review_graph/parser.pyand add your extension toEXTENSION_TO_LANGUAGEalong with node type mappings in_CLASS_TYPES,_FUNCTION_TYPES,_IMPORT_TYPES, and_CALL_TYPES. Include a test fixture and open a PR.

## Licence

MIT. SeeLICENSE.

code-review-graph.compip install code-review-graph && code-review-graph installWorks with Codex, Claude Code, Cursor, Windsurf, Zed, Continue, OpenCode, Antigravity, Gemini CLI, Qwen, Qoder, Kiro, GitHub Copilot, and GitHub Copilot CLI

## About

Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools read only what matters, with benchmarked context reductions on reviews and large-repo workflows.

code-review-graph.com

### Topics

 python

 tree-sitter

 mcp

 static-analysis

 incremental

 knowledge-graph

 code-review

 claude

 llm

 graphrag

 ai-coding

 claude-code

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

19.6k

 stars
 

### Watchers

66

 watching
 

### Forks

2.1k

 forks
 

 Report repository

 

## Releases27

v2.3.6 — community-response release

 Latest

 

Jun 10, 2026

 

+ 26 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python91.6%
* TypeScript8.1%
* Other0.3%