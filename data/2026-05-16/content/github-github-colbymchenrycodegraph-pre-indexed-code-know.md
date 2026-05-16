---
title: 'GitHub - colbymchenry/codegraph: Pre-indexed code knowledge graph for Claude Code — fewer tokens, fewer tool calls, 100% local · GitHub'
url: https://github.com/colbymchenry/codegraph
site_name: github
content_file: github-github-colbymchenrycodegraph-pre-indexed-code-know
fetched_at: '2026-05-16T11:25:03.485782'
original_url: https://github.com/colbymchenry/codegraph
author: colbymchenry
description: Pre-indexed code knowledge graph for Claude Code — fewer tokens, fewer tool calls, 100% local - colbymchenry/codegraph
---

colbymchenry

 

/

codegraph

Public

* NotificationsYou must be signed in to change notification settings
* Fork188
* Star2.1k

 
 
 
 
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

257 Commits
257 Commits
__tests__
__tests__
 
 
docs
docs
 
 
scripts
scripts
 
 
src
src
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
DELPHI-SUPPORT.md
DELPHI-SUPPORT.md
 
 
IMPLEMENTATION_PLAN.md
IMPLEMENTATION_PLAN.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
debug_python_ast.js
debug_python_ast.js
 
 
debug_python_ast2.js
debug_python_ast2.js
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
publish.js
publish.js
 
 
test_python_inheritance.js
test_python_inheritance.js
 
 
tsconfig.json
tsconfig.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

# CodeGraph

### Supercharge Claude Code with Semantic Code Intelligence

94% fewer tool calls · 77% faster exploration · 100% local

### Get Started

npx @colbymchenry/codegraph

Interactive installer configures Claude Code automatically

#### Initialize Projects

cd
 your-project
codegraph init -i

## Why CodeGraph?

When Claude Code explores a codebase, it spawnsExplore agentsthat scan files with grep, glob, and Read — consuming tokens on every tool call.

CodeGraph gives those agents a pre-indexed knowledge graph— symbol relationships, call graphs, and code structure. Agents query the graph instantly instead of scanning files.

### Benchmark Results

Tested across 6 real-world codebases comparing Claude Code's Explore agentwithandwithoutCodeGraph:

Average: 92% fewer tool calls · 71% faster

Codebase

With CG

Without CG

Improvement

VS Code
 · TypeScript

3 calls, 17s

52 calls, 1m 37s

94% fewer · 82% faster

Excalidraw
 · TypeScript

3 calls, 29s

47 calls, 1m 45s

94% fewer · 72% faster

Claude Code
 · Python + Rust

3 calls, 39s

40 calls, 1m 8s

93% fewer · 43% faster

Claude Code
 · Java

1 call, 19s

26 calls, 1m 22s

96% fewer · 77% faster

Alamofire
 · Swift

3 calls, 22s

32 calls, 1m 39s

91% fewer · 78% faster

Swift Compiler
 · Swift/C++

6 calls, 35s

37 calls, 2m 8s

84% fewer · 73% faster

Full benchmark details

All tests used Claude Opus 4.6 (1M context) with Claude Code v2.1.91. Each test spawned a single Explore agent with the same question.

Queries used:

Codebase

Query

VS Code

"How does the extension host communicate with the main process?"

Excalidraw

"How does collaborative editing and real-time sync work?"

Claude Code (Python+Rust)

"How does tool execution work end to end?"

Claude Code (Java)

"How does tool execution work end to end?"

Alamofire

"Trace how a request flows from Session.request() through to the URLSession layer"

Swift Compiler

"How does the Swift compiler handle error diagnostics?"

With CodeGraph — the agent usescodegraph_exploreand stops:

Codebase

Files Indexed

Nodes

Tool Uses

Tokens

Time

File Reads

VS Code (TypeScript)

4,002

59,377

3

56.6k

17s

0

Excalidraw (TypeScript)

626

9,859

3

57.1k

29s

0

Claude Code (Python+Rust)

115

3,080

3

67.1k

39s

0

Claude Code (Java)

—

—

1

40.8k

19s

0

Alamofire (Swift)

102

2,624

3

57.3k

22s

0

Swift Compiler (Swift/C++)

25,874

272,898

6

77.4k

35s

0

Without CodeGraph — the agent uses grep, find, ls, and Read extensively:

Codebase

Tool Uses

Tokens

Time

File Reads

VS Code (TypeScript)

52

89.4k

1m 37s

~15

Excalidraw (TypeScript)

47

77.9k

1m 45s

~20

Claude Code (Python+Rust)

40

69.3k

1m 8s

~15

Claude Code (Java)

26

73.3k

1m 22s

~15

Alamofire (Swift)

32

52.4k

1m 39s

~10

Swift Compiler (Swift/C++)

37

99.1k

2m 8s

~20

Key observations:

* With CodeGraph, the agentnever fell back to reading files— it trusted the codegraph_explore results completely
* Without CodeGraph, agents spent most of their time on discovery (find, ls, grep) before they could even start reading relevant code
* The Java codebase needed only1 codegraph_explore callto answer the entire question
* Cross-language queries (Python+Rust) worked seamlessly — CodeGraph's graph traversal found connections across language boundaries
* The Swift benchmark (Alamofire) traced a9-step call chainfromSession.request()toURLSession.dataTask()— CodeGraph's graph traversal at depth 3 captured the full chain in one explore call
* TheSwift Compilerbenchmark is the largest codebase tested (25,874 files, 272,898 nodes) — CodeGraph indexed it in under 4 minutes and the agent answered a complex cross-cutting question with6 explore calls and zero file readsin 35 seconds

## Key Features

Smart Context Building

One tool call returns entry points, related symbols, and code snippets — no expensive exploration agents

Full-Text Search

Find code by name instantly across your entire codebase, powered by FTS5

Impact Analysis

Trace callers, callees, and the full impact radius of any symbol before making changes

Always Fresh

File watcher uses native OS events (FSEvents/inotify/ReadDirectoryChangesW) with debounced auto-sync — the graph stays current as you code, zero config

19+ Languages

TypeScript, JavaScript, Python, Go, Rust, Java, C#, PHP, Ruby, C, C++, Swift, Kotlin, Dart, Svelte, Liquid, Pascal/Delphi

Framework-aware Routes

Recognizes web-framework routing files and links URL patterns to their handlers across 13 frameworks

100% Local

No data leaves your machine. No API keys. No external services. SQLite database only

## Framework-aware Routes

CodeGraph detects web-framework routing files and emitsroutenodes linked byreferencesedges to their handler classes or functions. Querying callers of a view/controller now surfaces the URL pattern that binds it.

Framework

Shapes recognized

Django

path()
, 
re_path()
, 
url()
, 
include()
 in 
urls.py
 (CBV 
.as_view()
, dotted paths)

Flask

@app.route('/path', methods=[...])
, blueprint routes

FastAPI

@app.get(...)
, 
@router.post(...)
, all standard methods

Express

app.get(...)
, 
router.post(...)
 with middleware chains

Laravel

Route::get()
, 
Route::resource()
, 
Controller@action
, tuple syntax

Rails

get '/x', to: 'users#index'
, hash-rocket 
=>
 syntax

Spring

@GetMapping
, 
@PostMapping
, 
@RequestMapping
 on methods

Gin / chi / gorilla / mux

r.GET(...)
, 
router.HandleFunc(...)

Axum / actix / Rocket

.route("/x", get(handler))

ASP.NET

[HttpGet("/x")]
 attributes on action methods

Vapor

app.get("x", use: handler)

React Router
 / 
SvelteKit

Route component nodes

## Quick Start

### 1. Run the Installer

npx @colbymchenry/codegraph

The installer will:

* Prompt to installcodegraphglobally (needed for the MCP server)
* Configure the MCP server in~/.claude.json
* Set up auto-allow permissions for CodeGraph tools
* Add global instructions to~/.claude/CLAUDE.md
* Optionally initialize your current project

### 2. Restart Claude Code

Restart Claude Code for the MCP server to load.

### 3. Initialize Projects

cd
 your-project
codegraph init -i

That's it! Claude Code will use CodeGraph tools automatically when a.codegraph/directory exists.

Manual Setup (Alternative)

Install globally:

npm install -g @colbymchenry/codegraph

Add to~/.claude.json:

{
 
"mcpServers"
: {
 
"codegraph"
: {
 
"type"
: 
"
stdio
"
,
 
"command"
: 
"
codegraph
"
,
 
"args"
: [
"
serve
"
, 
"
--mcp
"
]
 }
 }
}

Add to~/.claude/settings.json(optional, for auto-allow):

{
 
"permissions"
: {
 
"allow"
: [
 
"
mcp__codegraph__codegraph_search
"
,
 
"
mcp__codegraph__codegraph_context
"
,
 
"
mcp__codegraph__codegraph_callers
"
,
 
"
mcp__codegraph__codegraph_callees
"
,
 
"
mcp__codegraph__codegraph_impact
"
,
 
"
mcp__codegraph__codegraph_node
"
,
 
"
mcp__codegraph__codegraph_status
"
,
 
"
mcp__codegraph__codegraph_files
"

 ]
 }
}

Global Instructions Reference

The installer automatically adds these instructions to~/.claude/CLAUDE.md:

## 
CodeGraph

CodeGraph builds a semantic knowledge graph of codebases for faster, smarter code exploration.

### 
If 
`
.codegraph/
`
 exists in the project

**
NEVER call 
`
codegraph_explore
`
 or 
`
codegraph_context
`
 directly in the main session.
**
 These tools return large amounts of source code that fills up main session context. Instead, ALWAYS spawn an Explore agent for any exploration question (e.g., "how does X work?", "explain the Y system", "where is Z implemented?").

**
When spawning Explore agents
**
, include this instruction in the prompt:

> 
This project has CodeGraph initialized (.codegraph/ exists). Use 
`
codegraph_explore
`
 as your PRIMARY tool — it returns full source code sections from all relevant files in one call.

>

> 
**
Rules:
**

> 
1
.
 Follow the explore call budget in the 
`
codegraph_explore
`
 tool description — it scales automatically based on project size.

> 
2
.
 Do NOT re-read files that codegraph_explore already returned source code for. The source sections are complete and authoritative.

> 
3
.
 Only fall back to grep/glob/read for files listed under "Additional relevant files" if you need more detail, or if codegraph returned no results.

**
The main session may only use these lightweight tools directly
**
 (for targeted lookups before making edits, not for exploration):

|
 Tool 
|
 Use For 
|

|
------
|
---------
|

|
 
`
codegraph_search
`
 
|
 Find symbols by name 
|

|
 
`
codegraph_callers
`
 / 
`
codegraph_callees
`
 
|
 Trace call flow 
|

|
 
`
codegraph_impact
`
 
|
 Check what's affected before editing 
|

|
 
`
codegraph_node
`
 
|
 Get a single symbol's details 
|

### 
If 
`
.codegraph/
`
 does NOT exist

At the start of a session, ask the user if they'd like to initialize CodeGraph:

"I notice this project doesn't have CodeGraph initialized. Would you like me to run 
`
codegraph init -i
`
 to build a code knowledge graph?"

## How It Works

┌─────────────────────────────────────────────────────────────────┐
│ Claude Code │
│ │
│ "Implement user authentication" │
│ │ │
│ ▼ │
│ ┌─────────────────┐ ┌─────────────────┐ │
│ │ Explore Agent │ ──── │ Explore Agent │ │
│ └────────┬────────┘ └────────┬────────┘ │
│ │ │ │
└───────────┼────────────────────────┼─────────────────────────────┘
 │ │
 ▼ ▼
┌───────────────────────────────────────────────────────────────────┐
│ CodeGraph MCP Server │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │
│ │ Search │ │ Callers │ │ Context │ │
│ │ "auth" │ │ "login()" │ │ for task │ │
│ └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ │
│ │ │ │ │
│ └────────────────┼────────────────┘ │
│ ▼ │
│ ┌───────────────────────┐ │
│ │ SQLite Graph DB │ │
│ │ • 387 symbols │ │
│ │ • 1,204 edges │ │
│ │ • Instant lookups │ │
│ └───────────────────────┘ │
└───────────────────────────────────────────────────────────────────┘

1. Extraction—tree-sitterparses source code into ASTs. Language-specific queries extract nodes (functions, classes, methods) and edges (calls, imports, extends, implements).
2. Storage— Everything goes into a local SQLite database (.codegraph/codegraph.db) with FTS5 full-text search.
3. Resolution— After extraction, references are resolved: function calls → definitions, imports → source files, class inheritance, and framework-specific patterns.
4. Auto-Sync— The MCP server watches your project using native OS file events. Changes are debounced (2-second quiet window), filtered to source files only, and incrementally synced. The graph stays fresh as you code — no configuration needed.

## CLI Reference

codegraph 
#
 Run interactive installer

codegraph install 
#
 Run installer (explicit)

codegraph init [path] 
#
 Initialize in a project (--index to also index)

codegraph uninit [path] 
#
 Remove CodeGraph from a project (--force to skip prompt)

codegraph index [path] 
#
 Full index (--force to re-index, --quiet for less output)

codegraph sync [path] 
#
 Incremental update

codegraph status [path] 
#
 Show statistics

codegraph query 
<
search
>
 
#
 Search symbols (--kind, --limit, --json)

codegraph files [path] 
#
 Show file structure (--format, --filter, --max-depth, --json)

codegraph context 
<
task
>
 
#
 Build context for AI (--format, --max-nodes)

codegraph affected [files...] 
#
 Find test files affected by changes (see below)

codegraph serve --mcp 
#
 Start MCP server

### codegraph affected

Traces import dependencies transitively to find which test files are affected by changed source files.

codegraph affected src/utils.ts src/api.ts 
#
 Pass files as arguments

git diff --name-only 
|
 codegraph affected --stdin 
#
 Pipe from git diff

codegraph affected src/auth.ts --filter 
"
e2e/*
"
 
#
 Custom test file pattern

Option

Description

Default

--stdin

Read file list from stdin

false

-d, --depth <n>

Max dependency traversal depth

5

-f, --filter <glob>

Custom glob to identify test files

auto-detect

-j, --json

Output as JSON

false

-q, --quiet

Output file paths only

false

CI/hook example:

#!
/usr/bin/env bash

AFFECTED=
$(
git diff --name-only HEAD 
|
 codegraph affected --stdin --quiet
)

if
 [ 
-n
 
"
$AFFECTED
"
 ]
;
 
then

 npx vitest run 
$AFFECTED

fi

## MCP Tools

When running as an MCP server, CodeGraph exposes these tools to Claude Code:

Tool

Purpose

codegraph_search

Find symbols by name across the codebase

codegraph_context

Build relevant code context for a task

codegraph_callers

Find what calls a function

codegraph_callees

Find what a function calls

codegraph_impact

Analyze what code is affected by changing a symbol

codegraph_node

Get details about a specific symbol (optionally with source code)

codegraph_files

Get indexed file structure (faster than filesystem scanning)

codegraph_status

Check index health and statistics

## Library Usage

import
 
CodeGraph
 
from
 
'@colbymchenry/codegraph'
;

const
 
cg
 
=
 
await
 
CodeGraph
.
init
(
'/path/to/project'
)
;

// Or: const cg = await CodeGraph.open('/path/to/project');

await
 
cg
.
indexAll
(
{

 
onProgress
: 
(
p
)
 
=>
 
console
.
log
(
`
${
p
.
phase
}
: 
${
p
.
current
}
/
${
p
.
total
}
`
)

}
)
;

const
 
results
 
=
 
cg
.
searchNodes
(
'UserService'
)
;

const
 
callers
 
=
 
cg
.
getCallers
(
results
[
0
]
.
node
.
id
)
;

const
 
context
 
=
 
await
 
cg
.
buildContext
(
'fix login bug'
,
 
{
 
maxNodes
: 
20
,
 
includeCode
: 
true
,
 
format
: 
'markdown'
 
}
)
;

const
 
impact
 
=
 
cg
.
getImpactRadius
(
results
[
0
]
.
node
.
id
,
 
2
)
;

cg
.
watch
(
)
;
 
// auto-sync on file changes

cg
.
unwatch
(
)
;
 
// stop watching

cg
.
close
(
)
;

## Configuration

The.codegraph/config.jsonfile controls indexing:

{
 
"version"
: 
1
,
 
"languages"
: [
"
typescript
"
, 
"
javascript
"
],
 
"exclude"
: [
"
node_modules/**
"
, 
"
dist/**
"
, 
"
build/**
"
, 
"
*.min.js
"
],
 
"frameworks"
: [],
 
"maxFileSize"
: 
1048576
,
 
"extractDocstrings"
: 
true
,
 
"trackCallSites"
: 
true

}

Option

Description

Default

languages

Languages to index (auto-detected if empty)

[]

exclude

Glob patterns to ignore

["node_modules/**", ...]

frameworks

Framework hints for better resolution

[]

maxFileSize

Skip files larger than this (bytes)

1048576
 (1MB)

extractDocstrings

Extract docstrings from code

true

trackCallSites

Track call site locations

true

## Supported Languages

Language

Extension

Status

TypeScript

.ts
, 
.tsx

Full support

JavaScript

.js
, 
.jsx
, 
.mjs

Full support

Python

.py

Full support

Go

.go

Full support

Rust

.rs

Full support

Java

.java

Full support

C#

.cs

Full support

PHP

.php

Full support

Ruby

.rb

Full support

C

.c
, 
.h

Full support

C++

.cpp
, 
.hpp
, 
.cc

Full support

Swift

.swift

Full support

Kotlin

.kt
, 
.kts

Full support

Scala

.scala
, 
.sc

Full support (classes, traits, methods, type aliases, Scala 3 enums)

Dart

.dart

Full support

Svelte

.svelte

Full support (script extraction, Svelte 5 runes, SvelteKit routes)

Vue

.vue

Full support (script + script-setup extraction, Nuxt page/API/middleware routes)

Liquid

.liquid

Full support

Pascal / Delphi

.pas
, 
.dpr
, 
.dpk
, 
.lpr

Full support (classes, records, interfaces, enums, DFM/FMX form files)

## Troubleshooting

"CodeGraph not initialized"— Runcodegraph initin your project directory first.

Indexing is slow— Check thatnode_modulesand other large directories are excluded. Use--quietto reduce output overhead.

Indexing is slow / MCPdatabase is locked/ WASM fallback active—codegraphships with a WASM SQLite fallback for environments wherebetter-sqlite3(a native module, declared asoptionalDependencies) can't install. The fallback is 5-10x slower than the native backend and uses a journal mode that lets writers block readers, so MCP queries can also hitdatabase is lockedwhile indexing runs. Runcodegraph statusand look at theBackend:line:

* Backend: native— you're on the fast path, nothing to do.
* Backend: wasm— you're on the slow fallback. Common causes: missing C build tools, prebuilt binary unavailable for your Node version, or your Node version changed after install. Fix:#macOSxcode-select --install#installs the C compiler#Linux (Debian / Ubuntu)sudo apt install build-essential python3 make#Linux (RHEL / Fedora)sudo yum groupinstall"Development Tools"#Then rebuild on any platform:npm rebuild better-sqlite3#Or force-include as a hard dep:npm install better-sqlite3 --saveAfter the fix,codegraph statusshould showBackend: native.

MCP server not connecting— Ensure the project is initialized/indexed, verify the path in your MCP config, and check thatcodegraph serve --mcpworks from the command line.

Missing symbols— The MCP server auto-syncs on save (wait a couple seconds). Runcodegraph syncmanually if needed. Check that the file's language is supported and isn't excluded by config patterns.

## License

MIT

Made for the Claude Code community

Report Bug·Request Feature

## About

Pre-indexed code knowledge graph for Claude Code — fewer tokens, fewer tool calls, 100% local

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

2.1k

 stars
 

### Watchers

17

 watching
 

### Forks

188

 forks
 

 Report repository

 

## Releases1

v0.7.6

 Latest

 

May 13, 2026

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript95.4%
* JavaScript4.6%