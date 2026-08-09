---
title: 'GitHub - vitali87/code-graph-rag: The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases with the power of AI and knowledge graphs · GitHub'
url: https://github.com/vitali87/code-graph-rag
site_name: github
content_file: github-github-vitali87code-graph-rag-the-ultimate-rag-for
fetched_at: '2026-08-09T11:26:22.239993'
original_url: https://github.com/vitali87/code-graph-rag
author: vitali87
description: The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases with the power of AI and knowledge graphs - vitali87/code-graph-rag
---

vitali87

 

/

code-graph-rag

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork441
* Star2.7k

 
 
 
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

4,647 Commits
4,647 Commits
.github
.github
 
 
.vscode
.vscode
 
 
assets
assets
 
 
benchmarks
benchmarks
 
 
cgr
cgr
 
 
codebase_rag
codebase_rag
 
 
codec
codec
 
 
docs
docs
 
 
evals
evals
 
 
examples
examples
 
 
fixtures/
well_known_symbols
fixtures/
well_known_symbols
 
 
optimize
optimize
 
 
scripts
scripts
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
NEWS.md
NEWS.md
 
 
PYPI_README.md
PYPI_README.md
 
 
README.md
README.md
 
 
build_binary.py
build_binary.py
 
 
code-graph-rag-darwin-arm64.spec
code-graph-rag-darwin-arm64.spec
 
 
funding.json
funding.json
 
 
main.py
main.py
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
realtime_updater.py
realtime_updater.py
 
 
server.json
server.json
 
 
sonar-project.properties
sonar-project.properties
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Code-Graph-RAG

Code-Graph-RAG parses a multi-language codebase with Tree-sitter, builds a knowledge graph of its structure in Memgraph, and lets you query, edit, and optimise that code in plain English. It works across a monorepo of mixed languages under one unified graph schema.

## Latest News 🔥

* Ruby Support: Ruby joins the graph through a new pluggable ast-grep tier that adds a language from a single YAML pattern file, emittingModule,Function, andClassnodes plus import edges without a hand-written parser.
* Structural Search & Replace: Find and rewrite code by AST pattern with ast-grep, exposed as agent tools so you can match and transform structure across the whole codebase instead of relying on text or regex.
* Data-Flow Tracing: NewFLOWS_TOtaint edges follow values through assignments, function calls, and I/O sinks, with coverage across C#, Java, C, and Go.

SeeNEWS.mdfor the full history.

## What It Does

Point Code-Graph-RAG at a repository and it reads every source file, extracts functions, classes, methods, modules, and the relationships between them, and stores the result as an interconnected graph. Once the graph exists you can:

* Ask questions about the codebase in natural language and get answers grounded in the real structure.
* Retrieve the actual source of any function, class, or method by name or by intent.
* Edit code through the agent with AST-based surgical patching and a diff preview before anything changes.
* Optimise code against language best practices or your own coding standards.
* Find dead code by walking call and reference edges from entry points.
* Search and rewrite structurally by AST pattern with ast-grep.

## How It Works

The system has two components:

1. Multi-language parser.A Tree-sitter based parser reads the codebase and ingests functions, classes, methods, modules, and their relationships into Memgraph under a single language-agnostic schema.
2. RAG system(codebase_rag/). An interactive CLI that turns natural language into Cypher queries, retrieves matching code, and drives AI-powered editing and optimisation.

Source Code -> Tree-sitter Parser -> AST Analysis -> Memgraph Knowledge Graph
 |
User Query -> AI Model (Cypher Gen) -> Cypher Query -> Graph Results -> Response

See theArchitecture OverviewandGraph Schemafor the full picture.

## Supported Languages

Python, TypeScript, TSX, JavaScript, Rust, Go, Java, C, C++, C#, PHP, Lua, and Dart are fully supported. Scala is in development, and Ruby has structural support (modules, functions, classes, and imports) through the pluggable ast-grep tier. See theLanguage Supportmatrix for per-language capabilities.

## Installation

cgris published to PyPI. Install it system-wide with thetreesitter-full(all languages) andsemantic(vector search) extras:

#
 with uv (recommended)

uv tool install 
"
code-graph-rag[treesitter-full,semantic]
"

#
 or with pipx

pipx install 
"
code-graph-rag[treesitter-full,semantic]
"

You also need Docker (for Memgraph),cmake, andripgrep. Full prerequisites, source installs, and environment setup are in theInstallationguide.

## Quick Start

#
 Start the packaged Memgraph + Qdrant stack (no compose file needed)

cgr daemon up

#
 Parse a repository into the graph, then query it

cgr start --repo-path /path/to/repo --update-graph
cgr start --repo-path /path/to/repo

Repeat the first command for each repository you want indexed; the graph is
shared, and syncing one project leaves the others alone. To start over from an
empty graph, add--clean— it deleteseveryproject in the shared graph,
not just this one, and asks for confirmation first when other
projects would be destroyed.

TheQuick Startguide walks through parsing, querying, and exporting in five minutes.

## MCP Server

Code-Graph-RAG runs as anMCPserver so Claude Code and other MCP clients can query and edit your codebase directly. See theMCP Serverguide for setup.

## Documentation

Getting Started

* Installation
* Quick Start
* Configuration

User Guide

* CLI Reference
* Interactive Querying
* Code Optimisation
* Dead Code Detection
* Graph Export
* Real-Time Updates
* MCP Server

Architecture

* Overview
* Graph Schema
* Language Support
* Data-Flow Edges

Python SDK

* Overview
* Graph Loader
* Cypher Generator
* Semantic Search

Advanced

* Adding Languages
* Ignore Patterns
* Building Binaries
* Troubleshooting

## Enterprise Services

Code-Graph-RAG is open source and free to use. For organisations that need more, we offerfully managed cloud-hosted solutionsandon-premise deployments:

* Cloud-Hosted Deployment: Managed cloud infrastructure for both the graph database and the AI agent connection. Zero infrastructure overhead, so we handle scaling, updates, and availability while your team focuses on building.
* On-Premise & Air-Gapped Deployment: Deploy Code-Graph-RAG entirely within your own environment, including air-gapped networks. Full data sovereignty for regulated industries and security-sensitive organisations.

We also offer custom development, integration consulting, technical support contracts, and team training.

View plans & pricing at code-graph-rag.com

## Contributing

Please seeCONTRIBUTING.mdfor contribution guidelines. Good first PRs come from the TODO issues.

## Support

For issues or questions, check theTroubleshootingguide first, then open an issue.

## License

MIT. SeeLICENSE.