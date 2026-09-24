---
title: Gortex — code intelligence for your AI coding agent
url: https://gortex.dev
site_name: tldr
content_file: tldr-gortex-code-intelligence-for-your-ai-coding-agent
fetched_at: '2026-09-24T15:44:21.346043'
original_url: https://gortex.dev
date: '2026-09-24'
description: Gortex indexes a repo into an in-memory knowledge graph and serves it to coding agents over MCP, HTTP, and a web UI. A 21-tool MCP surface (100+ operations), 18 resources, 257 languages — one graph query replaces a stack of file reads, up to 50× fewer tokens per response.
tags:
- tldr
---

pane 1 — pitch

↵ read

# One call.not tenreads.

Gortex indexes your repository into an in-memory knowledge graph and serves it to your coding
 agent over MCP, HTTP, and a web UI. One graph query replaces a stack of file reads —up to 50× fewer tokensper response.257
 languages, a21-tool MCP surface, live editor-buffer overlays, speculative
 edits, dataflow, clone detection, graph-grounded PR review, and a 17-server LSP bridge.Built for19
 AI coding agentson macOS, Linux & Windows — one binary, zero services.

$ install
 ↵

15-min walkthrough →

$

curl -fsSL 
https://get.gortex.dev
 | sh

[copy]

21

domain tools

257

languages

19

agents wired

50
×

fewer tokens

pane 2 — session · 
agent@repo

●
 live

§01 · why
token accounting

## Stop paying your agent to re-read the same files.

A typical "make an edit" loop in Claude Code or Cursor does half a dozen Reads, a Grep,
 then
 maybe a Glob. Gortex answers the same question in one graph query — with callers, callees, imports,blast
 radius, and interface implementors attached.

without gortex
baseline

11,480

tokens / edit

* Read internal/watcher/watch.go (412 lines)
* Read internal/graph/patch.go (289 lines)
* Read internal/graph/types.go (603 lines)
* Grep "OnFileChange" across workspace
* Read 4 more files to resolve callers
* Guess at the interface it satisfies

with gortex
▶ explore

688

tokens / edit

* 7 symbols · 3 files · signatures + callers
* interface satisfied: graph.Patcher
* blast radius: 4 symbols, 2 tests
* no scan, no guessing, no re-reads
* live-synced via fsnotify watcher
* Δ−94.0%vs baseline

§02 · what's in the box
eighteen pillars

## A graph, a server, a daemon, and a hook — in one static binary.

Zero external dependencies. Everything runs in-process, in memory, on your laptop.
 Sigstore-signed releases, SLSA Level 3 build provenance, native macOS · Linux · Windows.

01
 knowledge graph 
core

Files, symbols, imports, calls, fields, decorators, generics, error contracts, modules (npm · pypi ·
 cargo · maven · go), SQL tables, channels, goroutines, flags, config keys, log/metric/pub-sub events,
 TODOs, licenses, owners — plus K8s resources, Kustomize overlays, Dockerfile images, dbt/SQLMesh models.
 Tarjan SCC, Leiden/Louvain communities, and a precomputed reach index forsub-millisecond
 blast-radiusqueries.

02
 257 languages 
parse

Three-tier extraction.~30bespoke tree-sitter (Go, TS, Python, Rust, Java,
 C#, Kotlin, Swift, C, C++, Ruby, Elixir, OCaml, …) for deep resolution,~60regex for niche/legacy,~165forest-backed signature-only — plus drop-in user
 grammars via.gortex.yaml, and Jupyter / Databricks notebooks indexed
 cell-by-cell.

03
 21 domain tools 
facade-v1

Named agents get a compact21-toolsurface by default; unnamed clients
 get a curatedcorepreset — ~34 workhorse tools eager, the rest of the
 175-tool catalogue onetools_searchcall away. Instruction profiles
 (core · localization · full) andGORTEX_TOOLStune the surface.explore,search,read,relations,trace,analyze(78 kinds),change,edit+16
 resources+ 3 prompts.

04
 semantic search 
default-on

Hybrid BM25 + vector, RRF fusion, continuous query-shape scoring. Default-on with a bakedGloVe-50dtable (3.8 MB embedded, CPU-only, zero deps);MiniLM / Ollama / OpenAIopt-in. HITS rerank, edge-provenance attenuation,
 first-class prose corpus, optionalaskagent (9 LLM providers). Publishedgortex eval: R@142.3%· R@555.1%· exact R@596.8%.

05
 live editor overlays 
shadow-graph

Shadow-graph sessions for unsaved buffers.overlay(push)stages an editor
 buffer; every subsequent tool call reads through a per-request view layered on the immutable base graph.changereturns the base↔overlay delta. Idle-TTL fail-safe;
 drift detection via git-blob SHA.

06
 speculative execution 
simulate

"What changes if I apply this edit?" — answered without touching disk.change(preview)turns an LSPWorkspaceEditinto an impact
 report;change(simulate)runs an ordered sequence with per-step diagnostics
 delta and cumulative blast-radius rollup.

07
 dataflow + taint 
cpg-lite

value_flow/arg_of/returns_toedges built at index time.trace(flow)returns ranked dataflow paths between two symbol IDs;trace(taint)runs
 pattern-driven source→sink sweeps for security audits — without ever loading a sandbox.

08
 clone detection 
minhash

Every substantial function body reduced to a 64-slot token-normalised MinHash signature at index time;
 LSH banding + Jaccard threshold emits symmetricsimilar_toedges.analyzesurfaces the "dead duplicates of live code" clone diagnostic
 (dead-only).

09
 structural + unsafe scan 
search(ast)

Cross-language tree-sitter S-expression search with bundled detectors (sql-string-concat,weak-crypto,hardcoded-secret, …).analyze(unsafe_patterns)fans seven detectors over the whole file set — Go panics, Rust unwrap/expect/panic!, JS/TS throw — in one
 call.

10
 concurrency + health 
analyze

Language-agnostic concurrency analyzers:analyze(race_writes)flags unguarded
 goroutine-reachable field writes,analyze(unclosed_channels)flags channels never
 closed.analyze(health_score)rolls coverage + complexity + recency + churn into one
 0–100 value and an A–F grade.

11
 diagnostics & code actions 
17 lsps

Wired to 17 language servers — gopls, tsgo, pyright, rust-analyzer, clangd, jdtls,
 kotlin-language-server, omnisharp, ruby-lsp, phpactor, sourcekit-lsp, …session(subscribe)pushes diagnostics deltas over MCP;change(code_actions)+refactor(apply_code_action)+refactor(fix_all)apply LSP-supplied fixes atomically.

12
 proactive notifications 
5 channels

Five per-session push channels — diagnostics, workspace readiness, daemon health, stale refs, and graph
 invalidation. Delta-filtered, initial replay, auto-cleanup on disconnect. The agent learns the graph
 changed without polling for it.

13
 context economy 
−27%

Round-trippableGCX1compact text — median−27.4%tokens vs JSON.exploregraded-fidelity manifests tier symbols under one budget;response(grep)/response(slice)re-cut a prior response without re-querying.

14
 cross-session memory 
persistent

Symbol-anchored development memories (remember/recall) compound across sessions and teammates; session notes survive
 context compactions; a repo-localnotebookcommits agent journal entries to
 git so they surface in PR review.

15
 http · mcp 2026 · daemon 
serve

Versioned/v1/*JSON API plus theMCP 2026 Streamable
 HTTPtransport (/mcp). A long-living daemon holds one graph for every
 editor window — live fsnotify, per-session isolation, launchd/systemd auto-start, ~200ms snapshot
 restore.

16
 graph-grounded PR review 
verdict

A deterministic correctness rulepack (NPE, thread-safety check-then-act, N+1, logic-error) runs over a
 changeset, graph-grounded to drop false positives →BLOCK / REVIEW / APPROVEwith line-anchored comments.pr(triage),pr(risk),pr(conflicts)(merge-order hotspots),publish_review(post)(secrets redacted). CLI:gortex prs · gortex review.

17
 cross-repo contracts 
+ temporal

Auto-detected across HTTP, gRPC, GraphQL, pub/sub topics (Kafka · NATS · Redis), WebSocket, env vars,
 OpenAPI,tRPC procedures, andTemporal workflows(Go + Java SDK), with framework-aware route
 passes forRails · Laravel · Vapor · Axum · Actix · Play · Drupal(analyze(route_frameworks)). Normalised to canonical IDs
 (http::GET::/api/users/{id}) and matched provider↔consumer across repos to
 flag orphans and mismatches.

18
 guarded edits + refactors 
drift-safe

edit(file)/edit(symbol)with abase_shadrift guard and expected-occurrences assertion; edits that introduce a
 new parse error are refused.refactor(rename),refactor(move),refactor(inline), andrefactor(delete)with a
 fixed-point orphan-propagation cascade.

§03 · architecture
cat ARCHITECTURE.txt

## Index. Serve. Watch.In-process.

No database to run. No container to orchestrate. One binary, one graph, two ports — and a
 Unix-socket daemon when you want to share it across editor windows.

gortex binary
 ── single static · ~20MB · CGO-on
 
│

 ├─ CLI (cobra) ────────────────────┐
 ├─ MCP Server (stdio + sse) ───────┤
 ├─ HTTP Server (:4747 /v1/*) ──────┤ ◀── web UI · IDE plugins · CI
 ├─ Overlay Sessions (shadow view) ─┤ ◀── unsaved editor buffers, MCP-session bound
 └─ Daemon (~/.gortex/server.sock) ─┤ ◀── shared graph for every editor window
 ▼
 
┌──────────────────────────┐

 
│ In-memory graph │

 
│ nodes · edges · index │

 
│ on-disk snapshot │

 
└──────────────▲───────────┘

 
│

 ┌─ Indexer ──► tree-sitter ◀── 257 langs ─┤
 │ + regex + forest tiers │
 ├─ Resolver ──► LSP · go/types · SCIP ─────┤ tier-aware: lsp_resolved → ast_resolved → ast_inferred → text_matched
 │ + cross-repo evidence gate │
 ├─ LSP Bridge ► 17 servers · diagnostics ──┤ session(subscribe) · change(code_actions) · refactor(fix_all)
 ├─ Watcher ───► fsnotify · debounced ──────┤ per-file patches
 └─ Clones ───► MinHash + LSH ──────────────┘ similar_to edges · dead-dup diagnostic

§04 · language coverage
257 languages · 3 tiers

## Speaks what your repo speaks.

Three-tier extraction: bespoke tree-sitter for deep resolution, regex for niche/legacy,
 forest-backed signature-only for the long tail.IMPLEMENTSinference for Go,
 TypeScript, Java, Rust, C#, Scala, Swift, and Protobuf — noextendskeyword required.

#

language · deep extraction

fns

methods

types

interfaces

calls

+

show named languages

· 11 categories · +165 more via forest

§05 · quickstart
three steps · runs anywhere

## Running in three commands.

macOS, Linux & Windows · amd64 + arm64. The installer detects your OS, downloads the
 signed release archive, verifies SHA256 (and cosign if installed), and puts the binary on yourPATH. No silent sudo.Re-runs upgrade in place.

01 · install

$
 curl -fsSL https://get.gortex.dev | sh

# windows: irm https://get.gortex.dev/install.ps1 | iex

# or: brew · scoop · .deb · .rpm · .apk

One-time machine setup:gortex installwrites user-level MCP wiring + skills
 + slash commands at~/.claude/and~/.gemini/.

02 · wire your agent

$
 cd ~/projects/myapp

$
 gortex init --analyze

# writes .mcp.json, CLAUDE.md,

# per-community SKILL.md, hooks

Auto-detects every agent in scope and writes a community-routing block to each —CLAUDE.md,AGENTS.md,.windsurfrules,GEMINI.md,.cursor/rules.

03 · serve + watch

$
 gortex daemon start --detach

# or: gortex mcp --watch (per-repo)

# or: gortex server --index .

Daemon runs in the background, supervises the graph for every tracked repo. Auto-start at login:gortex daemon install-service.

§06 · works with
19 first-class adapters

## Every coding agentyou already run.

Gortex is MCP-native. If your agent speaks the Model Context Protocol, it speaks Gortex.gortex initauto-detects each agent in scope and writes the right config.

Claude Code

slash commands, skills, hooks (PreToolUse, PreCompact, Stop, SessionStart)

● configured

Cursor

.cursor/mcp.json + .cursor/rules/gortex-communities.mdc

● configured

Kiro

.kiro/settings/mcp.json + steering + agent hooks

● configured

Windsurf

~/.codeium/mcp_config.json + .windsurfrules

● configured

VS Code / Copilot

.vscode/mcp.json + .github/copilot-instructions.md

● configured

Continue.dev

.continue/mcpServers/gortex.json + rules

● configured

Cline

cline_mcp_settings.json + .clinerules

● configured

OpenCode

.opencode/config.json + AGENTS.md routing

● configured

Antigravity

~/.gemini/antigravity mcp_config + Knowledge Item

● configured

Codex CLI

~/.codex/config.toml + AGENTS.md routing

● configured

Gemini CLI

~/.gemini/settings.json + GEMINI.md

● configured

Zed

settings.json context_servers + .rules

● configured

Aider

.aiderignore + CONVENTIONS.md communities

● configured

Kilo Code

mcp_settings.json + .kilocode/mcp.json

● configured

OpenClaw

~/.openclaw/openclaw.json mcp.servers

● configured

Hermes

~/.hermes config + profiles + skills + hooks

● configured

Oh My Pi

.omp/mcp.json mcpServers (detected via .omp dir or omp on PATH)

● configured

Pi

.pi/extensions/gortex/index.ts + AGENTS.md — self-contained TS extension

● configured

Kimi

.kimi-code/mcp.json + config.toml (UserPromptSubmit · PreToolUse · Stop · SubagentStart)

● configured

§07 · get started
exit 0

## Teach your agentwhat your code knows.

Open source underApache 2.0—freefor
 everyone, including commercial use, with patent grant.
 Zero dependencies. One static binary. Sigstore-signed, SLSA-3 build provenance, OpenSSF Scorecard tracked,
 VirusTotal 0/91.

$ git clone
 zzet/gortex ↵

15-min walkthrough →

releases ↗

on main · v0.62.0 · since v0.58

· indexer · resolver · sqlite hot-path perf sweep
+

· merkle parsed-source reuse · lazy clone sketches
+

· Terraform Lambda env vars as contract providers
+

· Java Type::new + qualified method references
+

· overloaded method refs bind the whole overload set
+

· .gitignore layered from git root to tracked root
+

· Visual Studio / MSBuild artifacts kept out of index
+

· review: test files exempt from coverage debt
+

· explore(localize) — terminality contract for "where"
+

· compact 21-tool MCP surface for named agents
+

· instruction profiles — core · localization · full
+

· gortex guide verb + gortex://guide resource
+

· Kimi + Pi adapters — 19 coding agents wired
+

main · ci passing · sigstore-signed · SLSA-3