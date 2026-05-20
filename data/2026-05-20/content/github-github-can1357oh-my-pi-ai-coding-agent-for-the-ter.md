---
title: 'GitHub - can1357/oh-my-pi: ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more · GitHub'
url: https://github.com/can1357/oh-my-pi
site_name: github
content_file: github-github-can1357oh-my-pi-ai-coding-agent-for-the-ter
fetched_at: '2026-05-20T12:02:49.857334'
original_url: https://github.com/can1357/oh-my-pi
author: can1357
description: ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more - can1357/oh-my-pi
---

can1357

 

/

oh-my-pi

Public

* NotificationsYou must be signed in to change notification settings
* Fork449
* Star5.2k

 
 
 
 
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

5,783 Commits
5,783 Commits
.github
.github
 
 
.omp
.omp
 
 
assets
assets
 
 
crates
crates
 
 
docs
docs
 
 
packages
packages
 
 
python
python
 
 
scripts
scripts
 
 
types/
assets
types/
assets
 
 
.fallowrc.jsonc
.fallowrc.jsonc
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.dockerignore
Dockerfile.dockerignore
 
 
Dockerfile.robomp
Dockerfile.robomp
 
 
Dockerfile.robomp.dockerignore
Dockerfile.robomp.dockerignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
bun.lock
bun.lock
 
 
bunfig.toml
bunfig.toml
 
 
package.json
package.json
 
 
rust-analyzer.toml
rust-analyzer.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.tools.json
tsconfig.tools.json
 
 
View all files

## Repository files navigation

A coding agent with the IDE wired in.omp.sh

Fork ofPiby@mariozechner

The most capable agent surface that ships. Continuously tuned by real-world use — complete out of the box, open all the way down.

40+providers ·32built-in tools ·13lsp ops ·27dap ops ·~27klines of Rust core.

## Install

macOS · Linux

curl -fsSL https://omp.sh/install 
|
 sh

Bun (recommended)

bun install -g @oh-my-pi/pi-coding-agent

Windows (PowerShell)

irm https:
//
omp.sh
/
install.ps1 
|
 iex

Pinned versions (mise)

mise use -g github:can1357/oh-my-pi

macOS · Linux · Windows · bun ≥ 1.3.14

## Every tool,benchmaxxed.

Edits that land on the first attempt. Reads that summarize files instead of dumping their content. Searches that return instantly. Pick any model — omp will get it right.

model

metric

what

Grok Code Fast 1

6.7% → 68.3%

Tenfold lift the moment the edit format stops eating the model alive.

Gemini 3 Flash

+5 pp

Over str_replace — beats Google's own best attempt at the format.

Grok 4 Fast

−61% tokens

Output collapses once the retry loop on bad diffs disappears.

MiniMax

2.1×

Pass rate more than doubles. Same weights, same prompt.

* read: summarized snippets · ideal defaults · selector hit rate
* search: fastest in the west
* lsp: everything your IDE knows, the agent knows
* prompts: adjusted relentlessly for each model

Read the full post ↗

## The Piyou love, withbatteries included.

Originally built onMario Zechner's wonderfulPi, omp adds everything you're missing.

### 01 · Code execution w/ tool-calling

Most harnesses give the agent a Python sandbox and call it done. Ours runs persistent Python and a Bun worker, and either kernel can call back into the agent's own tools — read, search, task — over a loopback bridge. The agent loads a CSV with tool.read from inside Python, charts it from JavaScript, and never leaves the cell.

### 02 · LSP wired into every write

Ask for a rename and you get a rename. The call goes through workspace/willRenameFiles, so re-exports, barrel files, and aliased imports update before the file moves. Everything your IDE knows, the agent knows.

### 03 · Drives a real debugger

A C binary segfaults: the agent attaches lldb, steps to the bad pointer, reads the frame. A Go service hangs: it attaches dlv and walks the goroutines. A Python process is wedged: debugpy, pause, inspect, evaluate. Most agents are still sprinkling print statements.

Watch the capture ↗

### 04 · Time-traveling stream rules

Your rules sit dormant until the model goes off-script. A regex match aborts the stream mid-token, injects the rule as a system reminder, and retries from the same point. You get course-correction without paying context tax on every turn. Injections survive compaction, so the fix sticks.

Watch the capture ↗

### 05 · First-class subagents

Split a job across workers and get typed results back. task fans out into isolated worktrees, each worker runs its own tool surface, and the final yield is a schema-validated object the parent reads directly. No prose to parse, no merge conflicts between siblings, no orphaned edits.

Watch the capture ↗

### 06 · Read a pdf on arxiv, why not?

web_search chains fourteen ranked providers and hands whatever URLs it finds straight to read. Arxiv PDFs, GitHub pages, Stack Overflow threads come back as structured markdown with anchors intact — the same tool surface you use on local files. Cite, follow, quote, never lose where you came from.

Watch the capture ↗

### 07 · Unapologetically native. Even on Windows.

Other agents shell out to rg, grep, find, and bash. On many machines those binaries don't exist, and on the ones where they do, every call costs a fork-exec round-trip. omp links the real implementations into the process. ripgrep, glob, find: in-process. brush is the bash, with sessions that survive across calls. The same omp binary runs on macOS, Linux, and Windows — no WSL bridge.

### 08 · Code review with priorities and a verdict

Get a clear verdict on whether the change ships, with every issue ranked P0 through P3 and scored for confidence. /review spawns dedicated reviewer subagents that sweep branches, single commits, or uncommitted work in parallel. You tackle what blocks release first; nothing important hides in a wall of prose.

### 09 · Hashline: edit by content hash

Perfect edits, fewer tokens. The model points at anchors instead of retyping the lines it wants to change, so whitespace battles and string-not-found loops just stop happening. Edit a stale file and the anchors diverge — we reject the patch before it corrupts anything. Grok 4 Fast spends 61% fewer output tokens on the same work.

### 10 · GitHub is just another filesystem

Other harnesses bolt on gh_issue_view, gh_pr_view, gh_search — each with its own parameters the agent has to learn and you have to debug. We skipped that. read already handles paths; PRs are paths. One interface to teach the model, one surface to keep correct.

### 11 · Hindsight: memory the agent curates

The agent remembers your codebase between sessions. It writes facts mid-run with retain, pulls them back with recall, and compresses each session into a mental model that loads on the first turn of the next one. Project-scoped by default, so what it learns about this repo stays with this repo.

### 12 · ACP: editor-drivable agent

Run omp inside Zed and you get the same agent you drive from the terminal — reading the buffer you're actually looking at, writing through the editor's save path, spawning shells in the editor's terminal. Destructive tools pause for a permission prompt you can answer once and forget. No bridge, no plugin, no second brain to keep in sync.

### 13 · Inherits what your other tools already wrote

Every other agent ships an importer and expects you to convert. omp reads the eight formats already on disk in their native shape — Cursor MDC, Cline .clinerules, Codex AGENTS.md, Copilot applyTo, and the rest. No migration script, no YAML-to-TOML port, no "supported subset" footnotes. The config your team wrote last quarter still works tonight.

### 14 · omp commit: atomic splits, validated messages

omp reads the working tree through git-overview, git-file-diff, and git-hunk, then splits unrelated changes into atomic commits ordered by their dependencies. Cycles are rejected before anything is written. Source files score above tests, docs, and configs, so the headline commit is the one that matters. Lock files are excluded from analysis entirely.

### 15 · Read PRs.Walk skills.Pull JSON out of subagents.

Ten internal schemes —pr://,issue://,agent://,skill://,rule://, and the rest — resolve transparently inside every FS-shaped tool the agent already calls.read pr://1428returns the same shape asread src/foo.ts.searchwalks a diff like a directory.agent://<id>/findings.0.pathpulls a field out of a subagent's output by path.

### 16 · Conflict resolution, made easy.

Each merge conflict becomes one URL. The agent writes@theirs,@ours, or@basetoconflict://Nand the file resolves cleanly. Bulk form:conflict://*.

Watch the capture ↗

### 17 · Preview, then accept.

ast_editreturns a(proposed)card with the replacement count. The change is staged. The agent callsresolvewith a reason; the TUI turns it into anAcceptcard and the disk move happens — atomic, all or nothing.

Watch the capture ↗

### 18 · Drives areal browser.Or your Slack?

Stealth's on by default, so pages see a normal user instead of a headless bot. The same API drives any Electron app in place — point it at Slack and the agent reads your DMs the way it reads the web.

## Whatever the task needs,it's already in the box.

32 tools live in the same namespace asreadandbash. Pin the active set with--tools read,edit,bash,…and the rest stay hidden but indexed —search_tool_bm25pulls them back in mid-session whentools.discoveryModesays so.

Files & search

* read— files, dirs, archives, SQLite, PDFs, notebooks, URLs, and internal://schemes through one path.
* write— create or overwrite a file, archive entry, or SQLite row.
* edit— hashline patches with content-hash anchors and stale-anchor recovery.
* ast_edit— structural rewrites previewed before apply, via ast-grep.
* ast_grep— structural code queries over 50+ tree-sitter grammars.
* search— regex over files, globs, and internal URLs.
* find— glob-based path lookup; reach forsearchwhen you need content matches.

Runtime

* bash— workspace shell, with optional PTY or background-job dispatch.
* eval— persistent Python and JavaScript cells with shared prelude and tool re-entry.
* recipe— invoke a target from a detected task runner — bun, just, make, cargo.
* ssh— one remote command against a configured host.

Code intelligence

* lsp— diagnostics, navigation, symbols, renames, code actions, raw requests.
* debug— drive a DAP session — breakpoints, stepping, threads, stack, variables.

Coordination

* task— fan out subagents in parallel, optionally workspace-isolated.
* irc— short prose between live agents in this process.
* todo_write— ordered mutations over the session todo list with phase tracking.
* job— wait on or cancel background jobs.
* ask— structured follow-up questions for interactive runs.

Outside the box

* browser— Puppeteer tabs over headless Chromium or CDP-attached apps.
* web_search— one query across configured providers, returning answer plus citations.
* github— GitHub CLI ops — repo, PR, issues, code search, Actions run-watch.
* generate_image— generate or edit raster images via Gemini image models.
* inspect_image— vision-model analysis of a local image file.
* render_mermaid— Mermaid source to terminal-friendly ASCII or PNG.

Memory & state

* checkpoint— mark conversation state for a later collapse-and-report.
* rewind— prune exploratory context, keep a concise report.
* retain— queue durable facts into the active Hindsight bank.
* recall— search the Hindsight bank for raw memories.
* reflect— ask Hindsight to synthesize an answer over the bank.

Misc

* calc— deterministic arithmetic — no model in the loop.
* resolve— apply or discard a queued preview action.
* search_tool_bm25— BM25 over the hidden tool index; activates top matches mid-session.

Setting-gated, off by default:github,calc,inspect_image,render_mermaid,checkpoint,rewind,search_tool_bm25,retain,recall,reflect. Flip them on once, scoped per project.

Full reference →

## Forty-plus providers, hundreds of models,one /model away.

Roles route work by intent.defaultfor normal turns.smolfor cheap subagent fan-out.slowfor deep reasoning.planfor plan mode.commitfor changelogs. Override at launch with--smol,--slow, or--plan; cycle through the configured models for the active role withCtrl+P. Swap the active model mid-session with the/modelslash command.

Auth tags below:oauthsigns in with your provider account,planroutes through a coding-plan subscription,localruns against a local server with the key optional.

### Frontier APIs

Direct APIs and gateways. Mix providers per role.

Anthropicoauth· OpenAI · OpenAI Codexoauth· Google Gemini · Google Antigravityoauth· xAI · Mistral · Groq · Cerebras · Fireworks · Together · Hugging Face · NVIDIA · OpenRouter · Synthetic · Vercel AI Gateway · Cloudflare AI Gateway · Perplexityoauth

### Coding plans

Subscription-routed./loginattaches the session.

Cursoroauth· GitHub Copilotoauth· GitLab Duo · Kimi Codeplan· Moonshot · MiniMax Coding Planplan· MiniMax Coding Plan CNplan· Alibaba Coding Planplan· Qwen Portal · Z.AI / GLM Coding Planplan· Xiaomi MiMo · Qianfan · NanoGPT · Venice · Kilo · ZenMux · OpenCode Go · OpenCode Zen

### Run it yourself

OpenAI-compatible/v1/models. Local instances skip the key.

Ollamalocal· Ollama Cloud · LM Studiolocal· llama.cpplocal· vLLMlocal· LiteLLM

### Four knobs that make routing useful

* Custom providers— Declare anything that speaksopenai-completions,openai-responses,openai-codex-responses,azure-openai-responses,anthropic-messages,google-generative-ai, orgoogle-vertexin~/.omp/agent/models.yml.
* Fallback chains— Per-role chains underretry.fallbackChains. When the primary throws 429s or hits a quota wall, the next entry takes the rest of the turn — restored on cooldown.
* Path-scoped roles— Nestpaths:undermodelRolesto pin a heavierdefaulton one repo without touching the global config. Closest path wins.
* Round-robin credentials— Stack API keys per provider and the runtime rotates with session affinity and per-credential backoff. Useful when one key would burn its quota by lunch.

Full provider & routing reference atomp.sh/docs/providers.

## Fourteen backends.One tool the agent already knows.

web_searchis built in, not bolted on.autowalks a fourteen-provider chain; pin one by name if you already pay for it. Behind every hit, site-aware extraction turns GitHub, registries, arXiv, Stack Overflow, and docs into structured markdown — anchors and link targets survive.

### Search providers

Fourteen backends. Pin one, or letautowalk the chain in order.

provider

auth

auto

chain

exa

EXA_API_KEY
 (or mcp)

brave

BRAVE_API_KEY

jina

JINA_API_KEY

kimi

MOONSHOT_API_KEY

zai

ZAI_API_KEY

anthropic

oauth

perplexity

PERPLEXITY_API_KEY

gemini

oauth

codex

oauth

tavily

TAVILY_API_KEY

parallel

PARALLEL_API_KEY

kagi

KAGI_API_KEY

synthetic

SYNTHETIC_API_KEY

searxng

self-hosted

### Specialised handlers

The agent gets structured content, not stripped HTML.

* Code hosts— github, gitlab
* Package registries— npm, PyPI, crates.io, Hex, Hackage, NuGet, Maven, RubyGems, Packagist, pub.dev, Go packages
* Research sources— arxiv, semantic scholar
* Forums— stack overflow, reddit, hn
* Docs— mdn, readthedocs, docs.rs

Pages convert to markdown with link structure intact. The agent can cite, follow, and quote without losing anchors.

### Security databases

Vuln lookups answer with vendor data, not blog summaries.

* NVD— national vulnerability database
* OSV— open source vuln feed
* CISA KEV— known exploited vulns

web_searchreference ↗

## Roughly~27,000lines of Rust, doing the work other harnesses shell out for.

Three crates, one platform-tagged N-API addon. Search, shell, AST, highlight, PTY, image decode, BPE counting — all in-process on the libuv pool. No fork/exec on the hot path.

* Crates:pi-natives,pi-shell,pi-ast
* Platforms:linux-x64,linux-arm64,darwin-x64,darwin-arm64,win32-x64

The table below is a per-module breakdown that intentionally omits glue and tests.

Module

What it does

Powered by

~LoC

shell

Embedded bash · persistent sessions · timeout/abort · custom builtins

brush-shell (vendored)

3,700

grep

Regex search · parallel/sequential · glob & type filters · fuzzy find

grep-regex · grep-searcher

1,900

keys

Kitty keyboard protocol with xterm fallback · PHF perfect-hash lookup

phf

1,490

text

ANSI-aware width · truncation · column slicing · SGR-preserving wrap

unicode-width · segmentation

1,450

summarize

Tree-sitter structural source summaries with elision controls

tree-sitter · ast-grep-core

1,040

ast

ast-grep pattern matching and structural rewrites

ast-grep-core

1,000

fs_cache

Mtime-keyed file cache shared by read · grep · lsp

in-tree

840

highlight

Syntax highlighting · 11 semantic categories · 30+ aliases

syntect

470

pty

Native PTY allocation for sudo · ssh interactive prompts

portable-pty

455

glob

Discovery with glob · type filters · mtime sort · gitignore respect

ignore · globset

410

workspace

Workspace walker with gitignore + AGENTS.md discovery in one pass

ignore · git2

385

appearance

Mode 2031 + native macOS dark/light via CoreFoundation FFI

core-foundation

270

power

macOS power-assertion API for idle/system/display-sleep prevention

IOKit FFI

270

task

Blocking work on libuv thread pool · cancellation · timeout · profiling

tokio · napi

260

fd

Filesystem walker for find-tool replacement

ignore

250

iso

Workspace isolation shim · apfs · btrfs · zfs · reflink · overlayfs · projfs · rcopy

pi-iso (PAL)

245

prof

Circular buffer profiler with folded-stack and SVG flamegraph output

inferno

240

ps

Cross-platform process-tree kill and descendant listing

libc · libproc · CreateToolhelp32Snapshot

195

image

Decode/encode PNG · JPEG · WebP · GIF · resize with 5 filters

image

190

clipboard

Text copy and image read from system clipboard · no xclip/pbcopy

arboard

80

tokens

O200k / Cl100k BPE token counting · both tables embedded

tiktoken-rs

65

html

HTML to Markdown with optional content cleaning

html-to-markdown-rs

50

## Four entry points:interactive,one-shot, RPC, and ACP.

Same engine, four wrappers.ompruns the TUI.omp -panswers a single prompt and exits. The Node SDK embeds the session in your process.omp --mode rpcandomp acphand the wheel to another program over stdio.

### Interactive — when in doubt, the agent asks

The TUI is the default surface. Tool calls render as cards, edits preview before they land, and ambiguity routes through theasktool — a structured option picker the agent can call mid-turn. The keyboard handles the rest.

The same prompt cards surface over ACP, so editors get the picker without writing one.

### SDK — embed in Node

@oh-my-pi/pi-coding-agent

Node and TypeScript hosts pull the engine in directly. The package exposesModelRegistry,SessionManager,createAgentSession, anddiscoverAuthStorage; the session emits typed events you subscribe to.

import
 
{
 
ModelRegistry
,
 
SessionManager
,
 
createAgentSession
,
 
discoverAuthStorage
 
}
 
from
 
"@oh-my-pi/pi-coding-agent"
;

const
 
auth
 
=
 
await
 
discoverAuthStorage
(
)
;

const
 
models
 
=
 
new
 
ModelRegistry
(
auth
)
;

await
 
models
.
refresh
(
)
;

const
 
{
 session 
}
 
=
 
await
 
createAgentSession
(
{

	
sessionManager
: 
SessionManager
.
inMemory
(
)
,

	
authStorage
: 
auth
,

	
modelRegistry
: 
models
,

}
)
;

await
 
session
.
prompt
(
"list .ts files"
)
;

### RPC — drive over stdio

omp --mode rpc

For non-Node embedders, or when you want process isolation. NDJSON commands in, response and event frames out.--mode rpc-uiadds tool cards, selectors, and dialogs asextension_ui_requestframes the host must answer.

$ omp --mode rpc --no-session
> {"id":"r1","type":"prompt","message":"list .ts files"}
< {"id":"r1","type":"response", ...}
> {"id":"r2","type":"set_model","provider":"anthropic","modelId":"sonnet-4.5"}
> {"id":"r3","type":"abort"}

### ACP — speak to editors

omp acp

TheAgent Client Protocolover JSON-RPC. When the editor advertises capabilities, tool I/O routes through it and writes are gated bysession/request_permission.

omp tool

ACP route

bash

terminal/create + terminal/output

read

fs/read_text_file

write

fs/write_text_file

edit, ast_edit, write, bash

session/request_permission

Full reference:omp.sh/docs/sdk.

## A harness worth keeping is one youdon'toutgrow.

Pick it up atomp.sh.

omp is a fork ofPibyMario Zechner, rewritten as a coding-first surface: sessions, subagents, slash commands, extensions — all TypeScript, all MIT, all onGitHub. Shape it from config, hook it from outside, or read the source when you need to.

### Primitives

An extension is a TypeScript module. Same tool API, same slash-command registry, same hotkey table, same TUI primitives the built-ins use. Nothing is reserved.

### Discovery

On first run omp inherits whatever is already on disk: rules, skills, and MCP servers from.claude,.cursor,.windsurf,.gemini,.codex,.cline,.github/copilot, and.vscode. No migration script.

### Extensibility

Ask omp to write the piece you're missing, then/reload-plugins. Keep it local, ship it in amarketplace, or publish it to npm.

## Philosophy

omp is a fork ofpi-monobyMario Zechner, extended with a batteries-included coding workflow.

Key ideas:

* Keep interactive terminal-first UX for real coding work
* Include practical built-ins (tools, sessions, branching, subagents, extensibility)
* Make advanced behavior configurable rather than hidden

## Development

### Debug Command

/debugopens tools for debugging, reporting, and profiling.

For architecture and contribution guidelines, seepackages/coding-agent/DEVELOPMENT.md.

## Monorepo Packages

Package

Description

@oh-my-pi/pi-ai

Multi-provider LLM client with streaming and model/provider integration

@oh-my-pi/pi-agent-core

Agent runtime with tool calling and state management

@oh-my-pi/pi-coding-agent

Interactive coding agent CLI and SDK

@oh-my-pi/pi-tui

Terminal UI library with differential rendering

@oh-my-pi/pi-natives

N-API bindings for grep, shell, image, text, syntax highlighting, and more

@oh-my-pi/omp-stats

Local observability dashboard for AI usage statistics

@oh-my-pi/pi-utils

Shared utilities (logging, streams, dirs/env/process helpers)

@oh-my-pi/swarm-extension

Swarm orchestration extension package

### Rust Crates

Crate

Description

pi-natives

Core Rust native addon (N-API 
cdylib
) used by 
@oh-my-pi/pi-natives
; aggregates the crates below

pi-shell

Embedded shell / PTY / process management split out of 
pi-natives
 (wraps 
brush-*
)

pi-ast

tree-sitter-based code summarizer and AST utilities (50+ language grammars)

pi-iso

Task isolation backend resolver: APFS clones, btrfs/zfs reflinks, overlayfs, projfs, rcopy

brush-core-vendored

Vendored fork of 
brush-shell
 for embedded bash execution

brush-builtins-vendored

Vendored bash builtins (cd, echo, test, printf, read, export, etc.)

## License

MIT. SeeLICENSE.

© 2025 Mario Zechner© 2025-2026 Can Bölük

made for terminals that stay open

* omp.sh
* GitHub
* Changelog
* npm
* Discord
* MIT

## About

⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more

omp.sh

### Topics

 rust

 cli

 typescript

 terminal

 mcp

 tui

 openai

 bun

 claude

 multi-provider

 coding-assistant

 ai-agent

 llm

 anthropic

 ai-coding-agent

### Resources

 Readme

 

### License

 MIT license
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

5.2k

 stars
 

### Watchers

15

 watching
 

### Forks

449

 forks
 

 Report repository

 

## Releases381

v15.1.8

 Latest

 

May 20, 2026

 

+ 380 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript80.9%
* Rust10.1%
* Python7.8%
* JavaScript0.6%
* CSS0.2%
* Shell0.1%
* Other0.3%