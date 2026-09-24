---
title: Gortex — code intelligence for your AI coding agent
url: https://gortex.dev
date: 2026-09-24
site: tldr
model: llama3.2:1b
summarized_at: 2026-09-24T15:49:45.392628
---

# Gortex — code intelligence for your AI coding agent

Here is a concise and informative summary of the article in Markdown format:

## Overview of Gortex

Gortex is an open-source code intelligence tool designed specifically for AI coding agents. It indexes a repository into an in-memory knowledge graph, serving it to the agent over MCP, HTTP, and a web UI. This reduces query latency to up to 50x fewer tokens per response.

### Key Features

* Built for AI coding agents on macOS, Linux, and Windows
* One binary, zero services
* Supports 257 languages, 19 tools, and 50 agents
* 17-server Last-Producer-First (LPF) bridge
* Domain tools (21 tools) with improved facades

### How it Works

1. A typical "make an edit" loop is replaced by a single graph query, reducing request latency to half a dozen reads.
2. Gortex answers the same question in one query, without scanning the same code files multiple times.
3. The agent receives the results in 688 tokens per edit, instead of 11,480.

### Benefits

* Reduced latency: up to 50x fewer tokens per response
* Improved performance: no scanning, no re-reading, and live-synced via fsnotify watcher
* Zero external dependencies: everything runs in-process, in memory, on the laptop
* Sigstore-signed releases, SLSA Level 3 build provenance, native macOS · Linux · Windows

## Architecture

* In-memory knowledge graph
* Core files, symbols, imports, calls, fields, decorators, generics, error contracts, modules (npm · pypi · cargo · Maven · Go), SQL tables, channels, goroutines, flags, config keys, log/metric/pub-sub events, TODOs, licenses, owners
* Tarjan SCC, Leiden/Louvain communities, precomputed reach index for sub-millisecond blast-radius queries
* Three-tier extraction for three languages: Go, Python, TypeScript