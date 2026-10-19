---
title: 'GitHub - headroomlabs-ai/headroom: Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server. · GitHub'
url: https://github.com/headroomlabs-ai/headroom
site_name: github
content_file: github-github-headroomlabs-aiheadroom-compress-tool-outpu
fetched_at: '2026-10-19T17:20:32.930519'
original_url: https://github.com/headroomlabs-ai/headroom
author: headroomlabs-ai
description: Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server. - headroomlabs-ai/headroom
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

3,316 Commits
3,316 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.cargo
.cargo
 
 
.claude-plugin
.claude-plugin
 
 
.codegraph
.codegraph
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.serena
.serena
 
 
REALIGNMENT
REALIGNMENT
 
 
benchmarks
benchmarks
 
 
crates
crates
 
 
deploy/
beacon
deploy/
beacon
 
 
docker
docker
 
 
docs
docs
 
 
e2e
e2e
 
 
examples
examples
 
 
headroom
headroom
 
 
plugins
plugins
 
 
sbom
sbom
 
 
scripts
scripts
 
 
sdk/
typescript
sdk/
typescript
 
 
sql
sql
 
 
tests
tests
 
 
wiki
wiki
 
 
.actrc
.actrc
 
 
.actrc.local.example
.actrc.local.example
 
 
.changelog.md
.changelog.md
 
 
.commitlintrc.json
.commitlintrc.json
 
 
.dockerignore
.dockerignore
 
 
.env.act.example
.env.act.example
 
 
.env.example
.env.example
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitguardian.yaml
.gitguardian.yaml
 
 
.gitignore
.gitignore
 
 
.gitleaks.toml
.gitleaks.toml
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.release-please-config.json
.release-please-config.json
 
 
.release-please-manifest.json
.release-please-manifest.json
 
 
.releasemetadata
.releasemetadata
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
Headroom-2.gif
Headroom-2.gif
 
 
HeadroomDemo-Fast.gif
HeadroomDemo-Fast.gif
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
RUST_DEV.md
RUST_DEV.md
 
 
SECURITY.md
SECURITY.md
 
 
TESTING-copilot-subscription.md
TESTING-copilot-subscription.md
 
 
claude_analysis_ttl.py
claude_analysis_ttl.py
 
 
codecov.yml
codecov.yml
 
 
dashboard-cache-ttl-main.png
dashboard-cache-ttl-main.png
 
 
deny.toml
deny.toml
 
 
docker-bake.hcl
docker-bake.hcl
 
 
docker-compose.yml
docker-compose.yml
 
 
headroom-savings.png
headroom-savings.png
 
 
headroom_learn.gif
headroom_learn.gif
 
 
llms.txt
llms.txt
 
 
pyproject.toml
pyproject.toml
 
 
run-all-plugins.sh
run-all-plugins.sh
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
server.json
server.json
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

Quickstart·Headroom for Teams·Install·Proof·Agents·Docs·Discord·llms.txt

AI agents / LLMs:read/llms.txthere, or fetchthe live index·full docs blob.

Headroom compresses everything your AI agent reads — tool outputs, logs, RAG
chunks, files, and conversation history — before it reaches the LLM. Same
answers, fraction of the tokens. Compression runs on your machine; no prompt or
file content is sent anywhere to be compressed.

10,144 → 1,260 tokens. The same 
FATAL
 found.

## What it does

* Library—compress(messages)in Python or TypeScript, inline in any app.
* Proxy—headroom proxy --port 8787, zero code changes, any language.
* Agent wrap—headroom wrap claude|codex|grok|copilot|cursor|aider|opencode|cline|continue|goose|openhands|openclaw|vibe|omp|zcodein one command; undo withheadroom unwrap <tool>.
* MCP server—headroom_compress,headroom_retrieve,headroom_statsfor any MCP client.
* Cross-agent memory— one shared store across Claude, Codex, Gemini and Grok, with automatic dedup.
* headroom learn— mines failed sessions and writes corrections toCLAUDE.local.md(default, gitignored),CLAUDE.md,AGENTS.md,GEMINI.mdorGROK.md.
* Output token reduction— trims what the modelwrites back, not only what you send. Seebelow.
* Reversible (CCR)— originals are cached locally and retrieved on demand.

## How it works

 Your agent / app
 (Claude Code, Cursor, Codex, LangChain, Agno, Strands, your own code…)
 │ prompts · tool outputs · logs · RAG results · files
 ▼
 ┌────────────────────────────────────────────────────┐
 │ Headroom (runs locally — your data stays here) │
 │ ──────────────────────────────────────────────── │
 │ CacheAligner → ContentRouter → CCR │
 │ ├─ SmartCrusher (JSON) │
 │ ├─ CodeCompressor (AST) │
 │ └─ Kompress-v2-base (text, HF) │
 │ │
 │ Cross-agent memory · headroom learn · MCP │
 └────────────────────────────────────────────────────┘
 │ compressed prompt + retrieval tool
 ▼
 LLM provider (Anthropic · OpenAI · Bedrock · …)

* ContentRouterdetects the content type and selects a compressor for it.
* SmartCrusher / CodeCompressor / Kompress-v2-basehandle JSON, source code and prose respectively.
* CacheAlignerflags volatile content that would bust a provider KV-cache prefix. It never rewrites prompts.
* CCRstores originals locally so the model can callheadroom_retrievewhen it needs the full text.

→Architecture·CCR·Kompress-v2-base model card

## Get started (60 seconds)

#
 1 — Install

uv tool install --python 3.13 
"
headroom-ai[all]
"
 
#
 CLI in a self-contained env

pip install 
"
headroom-ai[all]
"
 
#
 Python — ships the `headroom` CLI

npm install headroom-ai 
#
 TypeScript SDK only — no CLI

#
 2 — Pick a mode

headroom deploy 
#
 turnkey local deployment + agent config

headroom wrap claude 
#
 wrap a coding agent

headroom proxy --port 8787 
#
 drop-in proxy, zero code changes

#
 or: from headroom import compress # inline library

#
 3 — Check it and watch the savings

headroom doctor 
#
 health check — confirms routing works

headroom perf
headroom dashboard 
#
 live savings (proxy must be running)

Inline, in Python:

from
 
headroom
 
import
 
compress

from
 
openai
 
import
 
OpenAI

messages
 
=
 [{
"role"
: 
"user"
, 
"content"
: 
"Analyze these results"
}]

result
 
=
 
compress
(
messages
, 
model
=
"gpt-4o"
)

client
 
=
 
OpenAI
()

response
 
=
 
client
.
chat
.
completions
.
create
(
model
=
"gpt-4o"
, 
messages
=
result
.
messages
)

print
(
f"Saved 
{
result
.
tokens_saved
}
 tokens (
{
result
.
compression_ratio
:.0%
}
)"
)

Launch a wrapped agent session each time, so the setup runs.headroom wrapstarts a local proxy, installsSerenafor
semantic code navigation, and launches the agent configured to route through
Headroom. For Claude Code, Serena is registered for the wrapped project only
(as alocal-scope MCP server in~/.claude.json). Use--code-memory-scope userto make it available in every project, or--code-memory noneto skip it.headroom unwrapremoves either registration.

TheheadroomCLI ships only in the PyPI package. The npmheadroom-aipackage
is the TypeScript SDK — a library you import
(import { compress } from 'headroom-ai') — and provides noheadroomcommand.

## Proof

Four scenarios built from real MCP server output formats, measured with the
provider tokenizer and the shippedcompress(). Seeded and offline, so you get
the same numbers we did:

uv run python benchmarks/index_proof_table.py --seed 20260902

Scenario

Before

After

Saved

Code search (100 results)

17,199

13,597

21%

SRE incident debugging

55,957

24,340

57%

Codebase exploration

58,801

33,895

42%

GitHub issue triage

46,067

32,429

30%

Savings scale with how repetitive the payload is. Repeated JSON arrays and log
lines clear 90% inbenchmarks/bench_latency.py; prose and already-dense output
compress very little. Runheadroom savingsagainst your own traffic for the
number that applies to you.

Compression costswell under a millisecond— 0.21 ms p50 on a 10K-token JSON
search result, 1.4 ms at 100K tokens — so it does not show up in agent latency.

Accuracy.python -m headroom.evals suite --tier 1:

Benchmark

Category

N

Baseline

Headroom

Delta

GSM8K

Math

100

0.870

0.870

±0.000

TruthfulQA

Factual

100

0.530

0.560

+0.030

SQuAD v2

QA

100

—

97%

at 19% compression

BFCL

Tools

100

—

97%

at 32% compression

At N=100 a delta of ±0.03 falls inside the confidence interval, so TruthfulQA
shows no detectable difference rather than an improvement.Methodology →

## Output token reduction

Everything above shrinks the prompt yousend. You also pay for every token
the modelwrites back, and on Opus-class models output costs 5× input. Much
of that output is ceremony: "Great, let me…" preambles, code re-printed straight
back at you, and deep reasoning spent on routine steps like reading a file.

Headroom trims it from the proxy, with no change to your code:

* Verbosity steeringappends a short "be terse, don't restate context" note to theendof the system prompt, so your prompt cache still hits.
* Effort routingdials thinking effort down when a turn is only the model resuming after a tool result — a file read, a passing test. New questions and errors keep full effort.

Both apply to Anthropic/v1/messagesand to OpenAI-compatible/v1/chat/completionsand/v1/responses. Effort routing usesreasoning_efforton OpenAI andthinking.budget_tokens/output_config.efforton Anthropic, with the same clamp-only invariant and the sameoutput_shaper:*labels on both paths.

export
 HEADROOM_OUTPUT_SHAPER=1 
#
 off by default

headroom proxy --port 8787

Already running a proxy?These switches are read live on every request, so
a proxy thatheadroom wrapreusedrather than started would not see a value
you export afterwards — its environment was snapshotted at launch.headroom wraphot-syncs your current settings to the running proxy over a loopbackPOST /admin/runtime-env, so they take effect with no restart and no dropped
requests. On a shared proxy these overrides are global; the last explicit
setting wins.

Terseness you didn't have to configure.People rarely state how terse they
want answers — they show it, by interrupting long replies or moving on before
they could have read them.headroom learn --verbosityreads past sessions and
picks the level:

headroom learn --verbosity 
#
 dry run — preview what it found

headroom learn --verbosity --apply 
#
 save it and apply it to the running proxy

A proxy in cache mode (the default) never re-reads the learned level, because a
level that changes mid-conversation would bust the prompt cache. There--applypins it withHEADROOM_VERBOSITY_LEVEL; set that variable yourself to keep it
after a restart.

Measuring it.Output savings are counterfactual — we never see what the modelwouldhave written — so Headroom reports an estimate with a confidence range
and labels it as one:

headroom output-savings

#
 Reduction: 31.7% (95% CI 27.7% … 35.7%) [estimated]

For a measured number instead, hold out 10% of conversations as an unshaped
control:export HEADROOM_OUTPUT_HOLDOUT=0.1. The dashboard'sOutput Tokens
Savedcard then readsmeasuredrather thanestimated, with the band.

→Output token reduction

## Agent compatibility

Agent

headroom wrap

Notes

Claude Code

✅

--memory
 · 
--code-graph
 · 
--1m
 · 
--tool-search

Codex

✅

shares memory with Claude

Grok CLI

✅

routes via 
GROK_MODELS_BASE_URL

Cursor

Manual setup

starts the proxy and prints base URLs for Cursor settings

Aider

✅

starts proxy + launches

Copilot CLI

✅

starts proxy + launches

VS Code Copilot

✅

transparent proxy; keeps the selected model

OpenClaw

✅

installs as a ContextEngine plugin

OpenCode

✅

injects config · starts proxy + launches 
1

Cline

✅

starts proxy + injects config

Continue

✅

starts proxy + injects config

Goose

✅

starts proxy + launches

OpenHands

✅

starts proxy + launches

Mistral Vibe

✅

starts proxy + launches

Oh My Pi

✅

injects config · starts proxy + launches

Cortex Code

Library only

60–65% savings in library mode; no 
wrap

Kimi CLI

✅

OAuth bearer forwarded — log in once

ZCode

✅

starts the proxy and prints base URLs for ZCode settings

Any OpenAI-compatible client works throughheadroom proxy. MCP-native clients:headroom mcp install. Undo durable wrapping withheadroom unwrap <tool>(claude,copilot,codex,grok,kimi,omp,opencode,openclaw,zcode). Registry authors should use the canonicalserver.jsonrather than reconstructing theheadroom mcp servecontract from prose.

For Anthropic/v1/messages,--mode cacheskips automatic--memorycontext injection so the provider prefix remains stable. OpenAI chat/responses and Gemini append memory to the live-zone tail. Use--mode tokenwhen you need automatic memory context on the Anthropic path.

GitHub Copilot CLI subscription mode

Headroom can route Copilot CLI subscription traffic through the local proxy:

headroom copilot-auth login
headroom wrap copilot --subscription -- --model gpt-4o

The wrapper exchanges Headroom's reusable GitHub OAuth token for Copilot's
short-lived API token and prints the upstream endpoint asCOPILOT_PROVIDER_API_URL=...at launch.headroom copilot-auth loginstores a
Headroom-specific Copilot OAuth token, rather than relying on generic GitHub or
Copilot CLI tokens that can read account metadata but are still rejected by
Copilot's token-exchange endpoint.

For GitHub Enterprise Server or a custom-domain Copilot deployment, set one of
these before launching. If both are set, the URL wins:

export
 GITHUB_COPILOT_ENTERPRISE_DOMAIN=ghe.example.com

export
 GITHUB_COPILOT_ENTERPRISE_URL=https://ghe.example.com

For GitHub.com Enterprise Cloud URLs such asgithub.com/enterprises/your-enterprise, set neither — Headroom uses GitHub's
normal token-exchange endpoint and the Copilot API endpoint advertised for the
signed-in account.

Platform support.macOS auth reuse through Copilot CLI Keychain storage and
Windows device authentication are live-tested. Copilot CLI 1.0.81 does not expose
its Windows login through the legacy Credential Manager schema Headroom reads, so
runheadroom copilot-auth loginon Windows. Linux Secret Service /secret-toolreuse is implemented but not yet validated on a real desktop. In
Docker and CI, pass an explicitGITHUB_COPILOT_TOKENorGITHUB_COPILOT_GITHUB_TOKENinstead of relying on host keychain access.

GitHub Copilot in VS Code

Headroom overrides Copilot's API proxy endpoint, so the VS Code model picker
stays authoritative. GPT-5.5, GPT-5.6 Luna/Sol/Terra, Claude Sonnet/Opus and
other Copilot models keep their original model IDs while traffic passes through
the local compression proxy. Headroom does not patch VS Code or change Codex
settings.

headroom copilot-auth login
headroom wrap vscode

Keep the command running and use Copilot normally. The short-lived upstream
Copilot token is held only in the proxy process.Full guide →

Claude Code in VS Code

The official Claude Code extension embeds Claude Code and reads the same user
settings as the CLI. Install the proxy extra, then run the wrapper from the
project you will open in VS Code:

pip install 
"
headroom-ai[proxy]
"

headroom wrap vscode-claude

#
 Optional: persist Claude Code's client-owned 1M model selector

headroom wrap vscode-claude --1m

Reload the VS Code window on first run. Keep the wrapper terminal running while
you use the Claude Code panel; the dashboard or proxy log printed at startup
shows requests and savings. Your Anthropic authentication and selected model are
preserved.Ctrl+Cstops the proxy;headroom unwrap vscode-clauderestores the
settings that existed before setup.

With--1m, Headroom writes the resolved[1m]model selector to Claude Code's
top-level user setting and restores the exact prior model onheadroom unwrap vscode-claudeor when setup runs again without--1m. Useheadroom wrap vscode-claude --no-configure --1mto print the setting without
writing files.

Claude Code and Anthropic own 1M model support and account eligibility. Local
tests prove persisted settings and restoration, not a live entitled VS Code
session or the resulting context window.Full guide →

## When to use · when to skip

Good fit if yourun coding agents daily and want savings without touching
your code, work across several agents and want one shared memory, or need
compression that is reversible — originals stay retrievable through CCR for the
configured TTL.

Skip it if youonly use one provider's native compaction and don't need
cross-agent memory, or work in a sandbox where local processes can't run.

Headroom pays off on long agent sessions with heavy tool output. Short
conversational exchanges, prose, and already-dense payloads see little or no
reduction, and blocks undermin_input_wordscome back byte-identical.Limitationshas the full list.

Integrations — drop Headroom into any stack

Your setup

Hook in with

Any Python app

compress(messages, model=…)

Any TypeScript app

await compress(messages, { model })

Anthropic / OpenAI SDK

withHeadroom(new Anthropic())
 · 
withHeadroom(new OpenAI())

Vercel AI SDK

wrapLanguageModel({ model, middleware: headroomMiddleware() })

LiteLLM

litellm.callbacks = [HeadroomCallback()]

LangChain

HeadroomChatModel(your_llm)

Agno

HeadroomAgnoModel(your_model)

Strands

Strands guide

ASGI apps

app.add_middleware(CompressionMiddleware)

Multi-agent

SharedContext().put / .get

MCP clients

headroom mcp install

What's inside

* SmartCrusher— universal JSON: arrays of dicts, nested objects, mixed types. It keeps error items, values outside the normal statistical range, and first/last boundaries, selected from field-variance statistics rather than a keyword list.
* CodeCompressor— AST-aware for Python, JS/TS, Go, Rust, Java, C/C++, C#, PHP.
* Kompress-v2-base— our HuggingFace model, trained on agentic traces.
* Image compression— 40–90% reduction through a trained ML router.
* CacheAligner— flags volatile content that would bust a provider KV-cache prefix; never rewrites prompts.
* Live-zone compression— only new bytes are compressed (fresh tool output, the latest turn). The frozen prefix stays byte-identical, so the provider cache survives, and history is never dropped.
* CCR— reversible compression; the model retrieves originals on demand.
* Cross-agent memory— shared store with agent provenance and auto-dedup.
* SharedContext— compressed context passing across multi-agent workflows.
* headroom learn— plugin-based failure mining for Claude, Codex and Gemini.

Pipeline internals

One request lifecycle is shared bycompress(), the SDKs and the proxy:

Setup→Pre-Start→Post-Start→Input Received→Input Cached→Input Routed→Input Compressed→Input Remembered→Pre-Send→Post-Send→Response Received

* Transformsdo the work: CacheAligner → ContentRouter → SmartCrusher / CodeCompressor / Kompress-base, live-zone only. IntelligentContext and RollingWindow were retired in PR-B1.
* Pipeline extensionsobserve or customise lifecycle stages throughon_pipeline_event(...).
* Compression hookssit alongside the lifecycle as an additional extension seam.
* Proxy extensionsare the integration seam for ASGI middleware, routes and startup policy.

Provider- and tool-specific behaviour lives underheadroom/providers/, so core
orchestration stays focused on lifecycle, sequencing and policy:

* CLI/tool slices —headroom/providers/claude,copilot,codex,grok,openclaw
* Provider runtime slices —headroom/providers/claude,gemini, with shared backend dispatch inheadroom/providers/registry.py
* wrap.py,client.py,cli/proxy.pyandproxy/server.pydelegate env shaping, API target normalisation, backend selection and transport dispatch

## Install

uv tool install --python 3.13 
"
headroom-ai[all]
"
 
#
 CLI, isolated app env

pip install 
"
headroom-ai[all]
"
 
#
 Python, everything — includes the CLI

npm install headroom-ai 
#
 TypeScript SDK (library only)

docker pull ghcr.io/headroomlabs-ai/headroom:latest

Granular extras:[proxy],[mcp],[ml](Kompress-v2-base),[code],[memory],[vector](optional HNSW backend — needs a C++ toolchain, not in[all]),[relevance],[image],[agno],[langchain],[evals],[pytorch-mps](Apple-GPU memory-embedder offload — setHEADROOM_EMBEDDER_RUNTIME=pytorch_mps). RequiresPython 3.10+.

[all]covers the core stack but not the framework adapters. Install those
separately:pip install "headroom-ai[langchain]", and likewise[agno],[strands],[anyllm],[bedrock].

→Installation guide— Docker
tags, persistent service, PowerShell, devcontainers.

uv, pipx, and MCP clients that don't inherit your PATH

Preferuv tool installfor the CLI so the command lives in an isolated app
environment. On macOS, pass--python 3.13if your defaultpython3is newer
than the current wheel set:

brew install python@3.13 
#
 if 3.13 is not already available

uv tool install --python 3.13 
"
headroom-ai[all]
"

uv tool update-shell 
#
 if ~/.local/bin is not on PATH

headroom --version

Codex and other MCP clients often cannot inherit an interactive shellPATH.
Configure the absolute path returned bycommand -v headroom:

[
mcp_servers
.
headroom
]

command
 = 
"
/Users/you/.local/bin/headroom
"

args
 = [
"
mcp
"
, 
"
serve
"
]

command = "headroom"only works when the client starts with aPATHthat
already includes the uv tool directory.

With pipx, choose the interpreter explicitly:

pipx install --python python3.13 
"
headroom-ai[all]
"

Native wheels currently cover macOS Apple Silicon and Linux. On Intel macOS, use
the Docker-native install until native wheel support lands.

CPU requirement (x86/x86_64).The ONNX-backed features — Magika content
detection and embedding relevance — use a precompiled ONNX Runtime that needsAVX2. On x86 hosts without AVX2 (some Docker/QEMU setups, older cloud VMs)
Headroom falls back to its non-ONNX paths — BM25 relevance, heuristic detection —
rather than crashing.arm64and Apple Silicon need no AVX2.

Updating

headroom update 
#
 detects pip / pipx / uv tool and upgrades in place

headroom update --check 
#
 report the latest release without upgrading

headroom update --pre 
#
 include pre-releases

headroom updateworks out how Headroom was installed (pip/venv,pip --user,
pipx, uv tool) and runs the matching upgrade on macOS, Linux and Windows. For git
checkouts, editable installs, Docker images and externally-managed system Pythons
(PEP 668) it prints the correct manual step instead of guessing.

The proxy also prints a one-line "update available" notice at startup. It checks
PyPI at most once a day, in the background, and never blocks. Opt out withHEADROOM_UPDATE_CHECK=off; it is also skipped in--statelessmode and CI.

Corporate networks and SSL inspection

Ifpip install "headroom-ai[all]"fails withCERTIFICATE_VERIFY_FAILED(unable to get local issuer certificate), your network runs SSL inspection — a
MITM proxy presenting a company CA. The build backend (maturin) downloadsrustupover a connection your TLS stack does not trust. Install Rust first so
the build never fetches it:

#
 macOS / Linux

curl --proto 
'
=https
'
 --tlsv1.2 -sSf https://sh.rustup.rs 
|
 sh 
&&
 rustup default stable

#
 Windows

winget install Rustlang.Rustup 
&&
 rustup default stable

Restart your shell, then install. A prebuilt wheel avoids the Rust build
entirely:pip install --only-binary headroom-ai headroom-ai. Wheels are
published for Windows (win_amd64), Linux (x86_64/aarch64) and macOS
(Apple Silicon and Intel), so those platforms never need a local Rust toolchain —
the Rust-first step above is only for the sdist fallback when no wheel matches.

At runtimeHeadroom verifies upstream TLS against the operating system's
certificate store — where IT installs the Zscaler / Netskope / Palo Alto root —
plus certifi's public roots, so a managed machine normally needs no setup.headroom doctor --networkshows who signed each upstream certificate, whether
Headroom trusts it, and whether a gateway block page is in the way. If the root
is not in the OS store, export it as PEM and setHEADROOM_CA_BUNDLE=/path/to/root.pem(NODE_EXTRA_CA_CERTSalso works). Full
guide and the domain list for IT:Corporate networks.

Two download hosts can still need attention:

* cdn.pyke.io— the ONNX Runtime for the Rust core, fetched with Mozilla's roots only. Pre-provide it withORT_STRATEGY=systemandORT_LIB_LOCATION=/path/to/onnxruntime.
* huggingface.co— thekompress-basemodel (Python, OS store) and the Rust core's embedding model (Mozilla's roots only). If the domain is blocked, pre-download and run withHF_HUB_OFFLINE=1, or pointHF_ENDPOINTat a trusted mirror.

Running with compression disabled (pure gateway) needs neither asset.

Intel macOS: no prebuilt ONNX Runtime (#941).ort-sysships no prebuilt binary forx86_64-apple-darwin, so a source build
fails by default even outside a corporate proxy. Point it at a system runtime:

brew install onnxruntime
ORT_STRATEGY=system \
ORT_LIB_LOCATION=
"
$(
brew --prefix onnxruntime
)
/lib
"
 \
ORT_PREFER_DYNAMIC_LINK=1 \
 pip install 
"
headroom-ai[all]
"

#
 ORT is dlopen'd at runtime too:

export
 ORT_DYLIB_PATH=
"
$(
brew --prefix onnxruntime
)
/lib/libonnxruntime.dylib
"

ORT_LIB_LOCATIONmust point atlib/, not the bare prefix, andORT_PREFER_DYNAMIC_LINK=1is required — without itORT_STRATEGY=systemstill
attempts static linking, which the Homebrew keg does not provide.

"Basic Constraints of CA cert not marked critical"only occurs withHEADROOM_CERT_STORE=bundled(the OS store verifies these roots fine). If TLS
fails with:

[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:
Basic Constraints of CA cert not marked critical

then the corporate CAisfound and trusted, and adding it to a CA bundle
changes nothing. Python 3.13 with OpenSSL 3.x enablesVERIFY_X509_STRICTby
default, which enforces RFC 5280 §4.2.1.9: a CA cert'sbasicConstraintsmust be
marked critical. Inspection roots such as Zscaler setCA:TRUEwithout the
critical bit, so the chain is rejected.

HEADROOM_TLS_STRICT=0clears only the strict flag, from every TLS context
Headroom controls — the proxy's httpx upstream client and the
urllib3/huggingface_hubpath used for model downloads. Chain validation,
signature, expiry and hostname checks all stay on.

HEADROOM_TLS_STRICT=0 headroom proxy --port 8787

The Rust core's downloads use rustls with Mozilla's roots and are unaffected byHEADROOM_TLS_STRICTand the CA variables; pre-provision ONNX Runtime withORT_STRATEGY=systemand models viaHF_ENDPOINTas above.

## headroom learn

headroom learnmines failed sessions and writes corrections toCLAUDE.local.md(default, gitignored; use--target CLAUDE.mdfor the shared
team file),AGENTS.mdorGEMINI.md.
→Failure learning

## Telemetry

An anonymous beacon ison by default. It reports how compression behaved:
ratios, counters, provider and model IDs, OS and architecture. It never sends
prompts, completions, code or file paths. It exists so we can see when a release
regresses a compression ratio across real workloads rather than only our own test
corpus.

Turn it off withHEADROOM_BEACON=off,HEADROOM_TELEMETRY=off, theDO_NOT_TRACK=1convention, orHEADROOM_OFFLINE=1. The full field list is inthe proxy docs.

## Headroom for teams

Headroom OSS is built for one developer on one laptop. Headroom Enterprise is built
for the whole team.

Open source

Enterprise

Savings

Compression, plus tool search on Anthropic requests (on by default)

Also: tool search for every model, harness tuning, extra compressors

Model routing

Rule-based and opt-in: turn it on with 
HEADROOM_MODEL_ROUTER_ENABLED=1
 and write the rules in 
HEADROOM_MODEL_ROUTES

Automatic: a cheaper model per request when quality allows, with a shadow mode that shows the savings before you turn it on

Security

—

Detect and strip prompt injection and risky tool calls

Rollout

Per laptop

Managed or in your VPC, SSO, central config, org-wide savings

Support

GitHub, Discord

Dedicated engineers, onboarding, priority response

3 months of Enterprise free.Companies that sign a 12-month Enterprise plan get
their first 3 months free. One perk per company.

Claim 3 months free →· or emailhello@headroomlabs.aiwith your stack and
monthly LLM spend.

Everything in this repo stays open source under Apache 2.0.

## Documentation

Start here

Go deeper

Quickstart

Architecture

Proxy

How compression works

MCP tools

CCR — reversible compression

Memory

Cache optimization

Failure learning

Benchmarks

Configuration

Limitations

Persistent installs

Savings analytics

## Compared to

Headroom runs locally, covers every content type, works with every major
framework, and is reversible.

Scope

Deploy

Local

Reversible

Headroom

All context — tools, RAG, logs, files, history

Proxy · library · middleware · MCP

Yes

Yes

Compresr
, 
Token Co.

Text sent to their API

Hosted API call

No

No

OpenAI Compaction

Conversation history

Provider-native

No

No

Headroom is the proxy, and it compresses everything flowing through it whatever
sits upstream. Our recommended companion isSerenafor semantic code navigation,
installed by default when you wrap an agent, plusPonytailif you want leaner
model output. Everything else is your call — attach a code-memory MCP, Graphify,
Caveman, or any other MCP server, and Headroom compresses downstream of all of it.

## Contributing

git clone https://github.com/headroomlabs-ai/headroom.git 
&&
 
cd
 headroom
uv sync --extra dev 
&&
 uv run pytest

Devcontainers in.devcontainer/(default, plusmemory-stackwith Qdrant and
Neo4j). SeeCONTRIBUTING.md.

## Community

* Discord— questions, feedback, war stories.
* Kompress-v2-base on HuggingFace— the model behind text compression.
* Claude Code status-line plugin— live token savings in your status line, by@Ship-Wright.

## License

Apache 2.0 — seeLICENSE.

## Footnotes

1. headroom wraproutes OpenAI-compatible traffic to the default upstream (https://api.openai.com/v1). For a third-party OpenAI-compatible provider (DeepSeek, Together, OpenRouter, a self-hosted gateway), pass--openai-api-url https://api.deepseek.com/v1— or setOPENAI_TARGET_API_URLbefore wrapping — otherwise your provider key is sent to OpenAI and rejected with401 Incorrect API key provided. SeeOpenCode + DeepSeek.↩