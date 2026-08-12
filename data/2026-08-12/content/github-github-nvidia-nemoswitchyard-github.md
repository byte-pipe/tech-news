---
title: GitHub - NVIDIA-NeMo/Switchyard · GitHub
url: https://github.com/NVIDIA-NeMo/Switchyard
site_name: github
content_file: github-github-nvidia-nemoswitchyard-github
fetched_at: '2026-08-12T11:44:17.122365'
original_url: https://github.com/NVIDIA-NeMo/Switchyard
author: NVIDIA-NeMo
description: Contribute to NVIDIA-NeMo/Switchyard development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 NVIDIA-NeMo

 

/

Switchyard

Public

* NotificationsYou must be signed in to change notification settings
* Fork70
* Star599

 
 
 
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

214 Commits
214 Commits
.agents
.agents
 
 
.cargo
.cargo
 
 
.claude
.claude
 
 
.github
.github
 
 
.hooks
.hooks
 
 
assets
assets
 
 
benchmark
benchmark
 
 
crates
crates
 
 
dev-server
dev-server
 
 
docs
docs
 
 
examples
examples
 
 
scripts/
release
scripts/
release
 
 
switchyard
switchyard
 
 
switchyard_rust
switchyard_rust
 
 
tests
tests
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.commitlintrc.json
.commitlintrc.json
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.sir-merge-a-lot.yml
.sir-merge-a-lot.yml
 
 
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
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
DEVELOPMENT.md
DEVELOPMENT.md
 
 
INSTALLATION.md
INSTALLATION.md
 
 
LICENSE
LICENSE
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
mkdocs.yml
mkdocs.yml
 
 
mkdocs_hooks.py
mkdocs_hooks.py
 
 
pyproject.toml
pyproject.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Switchyard

Switchyard is a Rust proxy and library for LLM traffic. It routes requests
across providers, translates between OpenAI and Anthropic APIs, records
operational metrics, and provides typed, composable routing algorithms.

Why Switchyard?Point a coding agent such as Claude Code or Codex at an
open-source model. Switchyard translates between the OpenAI Chat, Anthropic
Messages, and OpenAI Responses formats, so the agent keeps speaking its native
API while the request is served by vLLM, NVIDIA NIM, Ollama, or any
OpenAI-compatible endpoint. The same proxy can spread traffic across several
models for A/B benchmarking, apply signal-driven stage routing, or run a custom
algorithm you write yourself.

## Features

* Protocol Translation: convert between OpenAI Chat, Anthropic Messages, and OpenAI Responses formats
* Multi-Backend Routing: random routing, LLM-as-classifier routing, signal-driven stage-router, or your own algorithm
* Operational Metrics: Prometheus metrics cover requests, errors, latency, tokens, and routing overhead

## Maturity

Switchyard is pre-alpha software that is evolving rapidly. The API and algorithms are expected to change significantly before we reach v1.0.

Warning

Experimental software. Not for production use.

## Quick Start

Choose the launcher path to run Claude Code, Codex CLI, or OpenClaw through
Switchyard. Choose the server path to run Switchyard as a standalone proxy.
Choose the library path to embed routing in your own Rust application.

### Launcher Path

Installuvif it is
not already available, then install the published Switchyard tool:

curl -LsSf https://astral.sh/uv/install.sh 
|
 sh

source
 
"
$HOME
/.local/bin/env
"

uv tool install --python 3.12 
"
nemo-switchyard[cli]
"

The coding agent you launch must also be installed and on yourPATH. This does
not install the standaloneswitchyard-serverbinary; use the Server Path for
that.

Set an OpenRouter key and launch against the packaged deployment:

export
 OPENROUTER_API_KEY=
"
your-openrouter-key
"
 
#
 pragma: allowlist secret

switchyard launch claude --model switchyard
switchyard launch codex --model switchyard
switchyard launch openclaw --model switchyard

To use your own native TOML deployment, pass its route ID and configuration:

switchyard launch claude --model my-route --config routes.toml

### Server Path

Use this path to install and run the standalone Rust proxy. InstallRust with Cargo, then install the
published binary:

cargo install --locked switchyard-server
switchyard-server --help

Cargo builds the release binary and installs it into~/.cargo/binby default.

Createroutes.tomlusing theGetting Started guide, then validate it
and start the server:

export
 OPENROUTER_API_KEY=
"
your-openrouter-key
"
 
#
 pragma: allowlist secret

switchyard-server --config routes.toml --dry-run
switchyard-server --config routes.toml --host 127.0.0.1 --port 4000

Verify the proxy in another terminal:

curl http://localhost:4000/health

For a complete configuration and a test request, followGetting Started.

### Library Path

switchyard-libsyembeds the routing algorithms in your own Rust application.
It never calls a model itself: an algorithm decides which target to use and
hands every model call back to you, so it drops into an existing proxy, gateway,
or agent runtime without owning an HTTP stack. Pair it withswitchyard-llm-clientwhen you want the calls made for you.

[
dependencies
]

switchyard-libsy
 = { 
git
 = 
"
https://github.com/NVIDIA-NeMo/Switchyard.git
"
 }

switchyard-protocol
 = { 
git
 = 
"
https://github.com/NVIDIA-NeMo/Switchyard.git
"
 }

SeeGetting Startedfor setup and the
algorithm list, or theswitchyard-libsycrate docs.

## Routing Strategies

Strategy

Use it when

Route 
type

LLM Classifier

Request content should decide whether a turn needs the weak or strong tier.

llm_classifier

Stage Router

Signals already in the conversation, such as tool results and errors, should route most turns without an extra model call.

stage_router

Escalation Router

Every turn runs on the weak tier first, and a judge reads that answer to decide whether to send the same request to the strong tier.

llm_classifier
 with 
mode = "escalation"

Random

You need a fixed traffic split for A/B tests, baselines, or cost experiments.

random

Apassthroughroute registers one target under one model ID with no routing
decision. See theRouting Overviewfor
the common route shape and self-hosted targets.

## Architecture

flowchart LR
 clients["Clients"]
 switchyard["Switchyard<br/>routing · translation · fallback"]
 backends["Model backends"]

 clients -->|"OpenAI / Anthropic API"| switchyard
 switchyard -->|"provider-native format"| backends

 
Loading

Clients keep their native OpenAI or Anthropic API format. Switchyard picks a
configured backend, forwards the request in that backend's own format, and
translates the response back into the shape the client expects. The server
accepts OpenAI Chat Completions, OpenAI Responses, and Anthropic Messages. Each
configured LLM client selects one upstream format.

## Documentation

* Getting Started: complete launcher and standalone server walkthroughs
* Core Concepts: LLM clients, targets, routes, model IDs, and routing algorithms
* Routing Overview: choose and configure a routing algorithm
* switchyard-server: server configuration, routing algorithms, and metrics
* switchyard-libsy: embed routing algorithms in a Rust application
* switchyard-protocol: provider-neutral request, response, and streaming types
* switchyard-translation: request, response, and stream translation

## Community

* Issues:GitHub Issues
* Code of Conduct:Code of Conduct

## License

Apache 2.0 License. Copyright NVIDIA Corporation.