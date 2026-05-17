---
title: 'GitHub - Light-Heart-Labs/DreamServer: Local AI anywhere, for everyone — LLM inference, chat UI, voice, agents, workflows, RAG, and image generation. No cloud, no subscriptions. · GitHub'
url: https://github.com/Light-Heart-Labs/DreamServer
site_name: github
content_file: github-github-light-heart-labsdreamserver-local-ai-anywhe
fetched_at: '2026-05-18T06:00:12.592281'
original_url: https://github.com/Light-Heart-Labs/DreamServer
author: Light-Heart-Labs
description: Local AI anywhere, for everyone — LLM inference, chat UI, voice, agents, workflows, RAG, and image generation. No cloud, no subscriptions. - Light-Heart-Labs/DreamServer
---

Light-Heart-Labs

 

/

DreamServer

Public

* NotificationsYou must be signed in to change notification settings
* Fork199
* Star1.1k

 
 
 
 
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

1,908 Commits
1,908 Commits
.claude/
commands
.claude/
commands
 
 
.github
.github
 
 
dream-server
dream-server
 
 
installer
installer
 
 
resources
resources
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitleaks.toml
.gitleaks.toml
 
 
.gitleaksignore
.gitleaksignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY_AUDIT.md
SECURITY_AUDIT.md
 
 
install.ps1
install.ps1
 
 
install.sh
install.sh
 
 
View all files

## Repository files navigation

# Dream Server

### Own your AI. One person, one dream, one machine at a time.

A handful of companies control the vast majority of global AI traffic — and with it, your data, your costs, and your uptime. Every query you send to a centralized provider is business intelligence you don’t own, running on infrastructure you don’t control, priced on terms you can’t negotiate.

If AI is becoming critical infrastructure, it shouldn’t be rented. Self-hosting local AI should be a sovereign human right, not a career choice.

Dream Server is the exit.A local-first AI stack — LLM inference, chat, voice, agents, workflows, RAG, image generation, and privacy tools — deployed on your hardware with a single command. No cloud required. No subscriptions required. No one watching. Cloud and hybrid API modes are optional when you choose them.

New here?Read theFriendly Guideorlisten to the audio version— a complete walkthrough of what Dream Server is, how it works, and how to make it your own. No technical background needed.

Current Platform Support

Platform

Status

Linux
 (NVIDIA + AMD + Intel Arc)

Supported
 — install and run today

Windows
 (NVIDIA + AMD)

Supported
 — install and run today

macOS
 (Apple Silicon)

Supported
 — install and run today

Tested Linux distros:Ubuntu 24.04/22.04, Debian 12, Fedora 41+, Arch Linux, CachyOS, openSUSE Tumbleweed. Other distros using apt, dnf, pacman, or zypper should also work —open an issueif yours doesn't.

Windows:Requires Docker Desktop with WSL2 backend. NVIDIA GPUs use Docker GPU passthrough; AMD Strix Halo runs through the platform-specific accelerated path documented in the Windows installer and support matrix.

macOS:Requires Apple Silicon (M1+) and Docker Desktop. llama-server runs natively with Metal GPU acceleration; all other services run in Docker.

See theSupport Matrixfor details.

## Why Dream Server?

Because running your own AI shouldn't require a CS degree and a weekend of debugging CUDA drivers. Right now, setting up local AI means stitching together a dozen projects, writing Docker configs from scratch, and praying everything talks to each other. Most people give up and go back to paying OpenAI.

We built Dream Server so you don't have to.

* One command— detects your GPU, picks the right model, generates credentials, launches everything
* Chatting in under 2 minutes— bootstrap mode gives you a working model instantly while your full model downloads in the background
* Full service stack, pre-wired— chat, agents, voice, workflows, search, RAG, image generation, privacy tools, observability, and developer tools. All talking to each other out of the box
* Fully moddable— every service is an extension. Drop in a folder, rundream enable, done

curl -fsSL https://raw.githubusercontent.com/Light-Heart-Labs/DreamServer/main/dream-server/get-dream-server.sh 
|
 bash

Openhttp://localhost:3000and start chatting.

API endpoint:Linux Docker installs expose llama-server onhttp://localhost:11434by default (OLLAMA_PORT) while containers usellama-server:8080. macOS native Metal and Windows native/Lemonade paths usehttp://localhost:8080unless overridden. Open WebUI stays onhttp://localhost:3000.

No GPU?Dream Server also runs in cloud mode — same full stack, powered by OpenAI/Anthropic/Together APIs instead of local inference:

./install.sh --cloud

Port conflicts?Every port is configurable via environment variables. See.env.examplefor the full list, or override at install time:

WEBUI_PORT=9090 ./install.sh

The DREAMGATE installer handles everything — GPU detection, model selection, service orchestration.

Manual install (Linux)

git clone https://github.com/Light-Heart-Labs/DreamServer.git

cd
 DreamServer/dream-server
./install.sh

Windows (PowerShell)

RequiresDocker Desktopwith WSL2 backend enabled.Install Docker Desktop first and make sure it is running before you start.

Open a normalPowerShellsession and run:

Set-ExecutionPolicy
 
-
Scope 
Process
 
-
ExecutionPolicy Bypass
git clone https:
//
github.com
/
Light
-
Heart
-
Labs
/
DreamServer.git
cd DreamServer
.\install.ps1

TheSet-ExecutionPolicycommand allows the installer script to run in the current session. It does not change your system-wide policy.
Running as Administrator is not recommended for the installer because user-level paths such as.opencode,data/, and.envcan be created with admin-owned permissions.

The installer detects your GPU, picks the right model, generates credentials, starts all services, and creates a Desktop shortcut to the Dashboard. Manage with.\dream-server\installers\windows\dream.ps1 status.

macOS (Apple Silicon)

Requires Apple Silicon (M1+) andDocker Desktop.Install Docker Desktop first and make sure it is running before you start.

git clone https://github.com/Light-Heart-Labs/DreamServer.git

cd
 DreamServer/dream-server
./install.sh

The installer detects your chip, picks the right model for your unified memory, launches llama-server natively with Metal acceleration, and starts all other services in Docker. Manage with./dream-macos.sh status.

See themacOS Quickstartfor details.

## What's In The Box

### Chat & Inference

* Open WebUI— full-featured chat interface with conversation history, web search, document upload, and30+ languages
* llama-server— high-performance LLM inference with continuous batching, auto-selected for your GPU; Linux Docker host API defaults tolocalhost:11434, native macOS/Windows paths uselocalhost:8080, and container API runs on8080
* LiteLLM— API gateway supporting local/cloud/hybrid modes
* TEI Embeddings— text embedding service for RAG and search workflows

### Voice

* Whisper— speech-to-text
* Kokoro— text-to-speech

### Agents & Automation

* Hermes Agent— optional local-first autonomous/browser agent with memory, skills, and a magic-link-gated proxy
* OpenClaw— optional autonomous AI agent framework
* n8n— workflow automation with 400+ integrations (Slack, email, databases, APIs)
* APE— Agent Policy Engine for auditing and governing autonomous tool calls
* OpenCode— browser-based AI coding assistant wired to the local stack
* Memory Shepherd— host/systemd helper for agent memory lifecycle management

### Knowledge & Search

* Qdrant— vector database for retrieval-augmented generation (RAG)
* SearXNG— self-hosted web search (no tracking)
* Perplexica— deep research engine
* Brave Search— optional paid Brave Search API integration

### Creative

* ComfyUI— node-based image generation

### Privacy & Ops

* Privacy Shield— PII scrubbing proxy for API calls
* Dashboard— real-time GPU metrics, service health, model management
* Dashboard API— service health, setup, status, metrics, and management API behind the dashboard
* Token Spy— token usage monitor for local and proxied LLM traffic
* Langfuse— optional LLM observability and tracing

## Hardware Auto-Detection

The installer detects your GPU and picks the optimal model automatically. No manual configuration is required for the default path.

The current model map supportsMODEL_PROFILE=qwenby default, plusMODEL_PROFILE=gemma4andMODEL_PROFILE=autofor Gemma 4 tiers where supported. Override tier selection with./install.sh --tier 3; override the model family withMODEL_PROFILE=gemma4 ./install.shorMODEL_PROFILE=auto ./install.sh.

### NVIDIA

Tier

VRAM

Qwen profile

Gemma 4 profile

Context

Example GPUs

0

< 8 GB or CPU-only fallback

Qwen3.5 2B (Q4_K_M)

Qwen3.5 2B (bootstrap-friendly minimum)

8K

Any GPU or CPU-only

1

8–11 GB

Qwen3.5 9B (Q4_K_M)

Gemma 4 E2B IT (Q4_K_M)

16K

RTX 4060, RTX 3060 12GB

2

12–20 GB

Qwen3.5 9B (Q4_K_M)

Gemma 4 E4B IT (Q4_K_M)

32K

RTX 3090, RTX 4080

3

20–40 GB

Qwen3 30B-A3B MoE (Q4_K_M)

Gemma 4 26B-A4B IT (Q4_K_M)

32K Qwen / 16K Gemma

RTX 4090, A6000

4

40+ GB

Qwen3 30B-A3B MoE (Q4_K_M)

Gemma 4 31B IT (Q4_K_M)

128K Qwen / 64K Gemma

A100, H100, multi-GPU

NV_ULTRA

90+ GB

Qwen3 Coder Next (Q4_K_M)

Gemma 4 31B IT (Q4_K_M)

128K

Multi-GPU A100/H100

### AMD Strix Halo (Unified Memory)

Tier

Unified RAM

Qwen profile

Gemma 4 profile

Context

Hardware

SH_COMPACT

64–89 GB

Qwen3 30B-A3B MoE (Q4_K_M)

Gemma 4 26B-A4B IT (Q4_K_M)

128K Qwen / 64K Gemma

Ryzen AI MAX+ 395 (64GB)

SH_LARGE

90+ GB

Qwen3 Coder Next (Q4_K_M)

Gemma 4 31B IT (Q4_K_M)

128K

Ryzen AI MAX+ 395 (96GB)

### Apple Silicon (Unified Memory, Metal)

Tier

Unified RAM

Qwen profile

Gemma 4 profile

Context

Example Hardware

0

< 16 GB

Qwen3.5 2B (Q4_K_M)

Qwen3.5 2B (bootstrap-friendly minimum)

8K

M1/M2 base (8GB)

1

16–24 GB

Qwen3.5 9B (Q4_K_M)

Gemma 4 E2B IT (Q4_K_M)

16K

M4 Mac Mini (16GB)

2

32 GB

Qwen3.5 9B (Q4_K_M)

Gemma 4 E4B IT (Q4_K_M)

32K

M4 Pro Mac Mini, M3 Max MacBook Pro

3

48 GB

Qwen3 30B-A3B MoE (Q4_K_M)

Gemma 4 26B-A4B IT (Q4_K_M)

32K Qwen / 16K Gemma

M4 Pro (48GB), M2 Max (48GB)

4

64+ GB

Qwen3 30B-A3B MoE (Q4_K_M)

Gemma 4 31B IT (Q4_K_M)

128K Qwen / 64K Gemma

M2 Ultra Mac Studio, M4 Max (64GB+)

### Intel Arc (Linux, SYCL)

Tier

VRAM

Qwen profile

Gemma 4 profile

Context

Example Hardware

ARC_LITE

6–11 GB

Qwen3.5 4B (Q4_K_M)

Gemma 4 E2B IT (Q4_K_M)

16K

Arc A380, Arc A750

ARC

12+ GB

Qwen3.5 9B (Q4_K_M)

Gemma 4 E4B IT (Q4_K_M)

32K

Arc A770 16GB, newer Arc GPUs

Override tier selection:./install.sh --tier 3

## Bootstrap Mode

No waiting for large downloads. Dream Server uses bootstrap mode by default:

1. Downloads a tiny 1.5B model in under a minute
2. You start chatting immediately
3. The full model downloads in the background
4. Hot-swap to the full model when it's ready — zero downtime

The installer pulls all services in parallel. Downloads are resume-capable — interrupted downloads pick up where they left off.

Skip bootstrap:./install.sh --no-bootstrap

## Switching Models

The installer picks a model for your hardware, but you can switch anytime:

dream model current 
#
 What's running now?

dream model list 
#
 Show all available tiers

dream model swap T3 
#
 Switch to a different tier

If the new model isn't downloaded yet, pre-fetch it first:

./scripts/pre-download.sh --tier 3 
#
 Download before switching

dream model swap T3 
#
 Then swap (restarts llama-server)

Already have a GGUF you want to use? Drop it indata/models/, updateGGUF_FILEandLLM_MODELin.env, and restart with the CLI:

dream restart llm

Or restart the container directly from the installeddream-serverdirectory:

docker compose restart llama-server

Rollback is automatic — if a new model fails to load, Dream Server reverts to your previous model.

## Extensibility

Dream Server is designed to be modded. Every service is an extension — a folder with amanifest.yamland acompose.yaml. The dashboard, CLI, health checks, and compose stack all discover extensions automatically.

extensions/services/
 my-service/
 manifest.yaml # Metadata: name, port, health endpoint, GPU backends
 compose.yaml # Docker Compose fragment (auto-merged into the stack)

dream 
enable
 my-service 
#
 Enable it

dream disable my-service 
#
 Disable it

dream list 
#
 See everything

The installer itself is modular — 6 libraries and 13 phases, each in its own file. Want to add a hardware tier, swap a default model, or skip a phase? Edit one file.

Full extension guide|Installer architecture

## dream-cli

ThedreamCLI manages your entire stack:

dream status 
#
 Health checks + GPU status

dream list 
#
 All services and their state

dream logs llm 
#
 Tail logs (aliases: llm, stt, tts)

dream restart [service] 
#
 Restart one or all services

dream start / stop 
#
 Start or stop the stack

dream mode cloud 
#
 Switch to cloud APIs via LiteLLM

dream mode 
local
 
#
 Switch back to local inference

dream mode hybrid 
#
 Local primary, cloud fallback

dream model swap T3 
#
 Switch to a different hardware tier

dream 
enable
 n8n 
#
 Enable an extension

dream disable whisper 
#
 Disable one

dream config show 
#
 View .env (secrets masked)

dream preset save gaming 
#
 Snapshot current config

dream preset load gaming 
#
 Restore it

## How It Compares

Other tools get you part of the way. Dream Server gets you the whole way.

Dream Server

Ollama + Open WebUI

LocalAI

Scope

Full AI stack — inference to agents to workflows

LLM + chat

LLM only

One-command install

Everything, auto-configured

LLM + chat only

LLM only

Hardware auto-detect + model selection

NVIDIA + AMD Strix Halo + Apple Silicon + Intel Arc + CPU/cloud fallback

No

No

AMD APU unified memory support

Platform-specific accelerated backend, selected by installer

Partial (Vulkan)

No

Autonomous AI agents

Hermes Agent / OpenClaw

No

No

Workflow automation

n8n (400+ integrations)

No

No

Voice (STT + TTS)

Whisper + Kokoro

No

No

Image generation

ComfyUI

No

No

RAG pipeline

Qdrant + embeddings

No

No

Extension system

Manifest-based, hot-pluggable

No

No

Multi-GPU

Yes (NVIDIA)

Partial

Partial

## Documentation

Quickstart

Step-by-step install guide with troubleshooting

Headless Setup

QR onboarding, first-boot setup, AP mode, mDNS, and local agent access

Hardware Guide

What to buy, tier recommendations

FAQ

Common questions and configuration

Extensions

How to add custom services

Installer Architecture

Modular installer deep dive

Changelog

Version history and release notes

Contributing

How to contribute

## Wall of Heroes

Dream Server exists because people chose to build instead of wait. Every contributor here is part of something bigger than code — a growing resistance against the idea that AI should be rented, gated, and controlled by the few. These are the founders of the sovereign AI movement, proving that one person, one machine, and one dream is enough.

Thanks tokyuz0foramd-strix-halo-toolboxes— pre-built ROCm containers for Strix Halo that saved us a lot of pain from having to build our own. And tolhlforstrix-halo-testing— the foundational Strix Halo AI research and rocWMMA performance work that the broader community builds on.

Tony363 (Tony Siu)cares deeply about our mission, and has been a vital ally in helping us gain visibility and support in the world. His greatest contributions are as a person who believes in local AI and empowerment for the masses and who wants to see us succeed.

### Community Builds

* halo-ai (bong-water-water-bong)— Bare-metal DreamServer rebuild for Strix Halo on Arch Linux. Zero containers, compiled from source, 89 tok/s. Proved Vulkan > ROCm for generation on gfx1151 and contributed kernel tuning research (amd_iommu=off, TTM page pool expansion) back to the ecosystem. Early DreamServer advocate who introduced us to the Lemonade SDK community and AMD developer team.

### Projects that make Dream Server possible

* llama.cpp (ggerganov)— LLM inference engine
* Qwen (Alibaba Cloud)— Default language models
* Open WebUI— Chat interface
* ComfyUI— Image generation engine
* FLUX.1 (Black Forest Labs)— Image generation model
* AMD ROCm— GPU compute platform
* AMD Strix Halo Toolboxes (kyuz0)— Pre-built ROCm containers for AMD inference
* Strix Halo Testing (lhl)— Foundational Strix Halo AI research and rocWMMA optimizations
* n8n— Workflow automation
* Qdrant— Vector database
* SearXNG— Privacy-respecting search
* Perplexica— AI-powered search
* LiteLLM— LLM API gateway
* Kokoro FastAPI (remsky)— Text-to-speech
* Speaches— Speech-to-text
* Strix Halo Home Lab— Community knowledge base

### The Resistance

* Yasin Bursali (yasinBursali)— DreamServer's most prolific contributor across 80+ merged PRs spanning every layer of the stack.Extensions portal: built the full extensions lifecycle system — catalog generator with CI freshness validation, dream host agent for container management outside Docker (timing-safe auth, core service protection, per-service locking, setup hook execution), extensions API with 16-check compose security scanner (blocks privileged mode, docker socket mounts, dangerous capabilities, host namespaces, non-localhost port bindings) plus atomic installs with path traversal and symlink protection, Extensions dashboard page with install/enable/disable/uninstall, and comprehensive API/host agent/runtime lifecycle documentation.Extensions library hardening: led three waves of 50+ PRs standardizing all 33 extension manifests — security hardening (localhost binding, credential requirements, session isolation), setup hooks, image digest pinning, healthcheck fixes (IPv4 migration, tool availability, health_port for split endpoints), port conflict resolution, README standardization, platform compatibility matrix, feature ID deduplication, and compose security scan bypass closures for bare ports and security_opt normalization.macOS portability: fixed Apple Silicon Neural Engine detection, unified memory VRAM gating, GPU_BACKEND=apple alignment, BSD/GNU sed compatibility (_sed_i), portable timestamps (_now_ms()), Bash 4+ guards with Homebrew re-exec, readiness sidecar for native llama-server, LaunchAgent host agent integration, and WSL2 host RAM detection.Dashboard API: added tiered Privacy Shield auth, migrated privacy-shield toggle from Docker socket to host agent API, populated null status fields (disk/system/inference), fixed n8n health detection with shared aiohttp sessions, forced IPv4 in health checker for WSL2, added GPU service inference fallback from nvidia-smi processes, handled thinking model<think>blocks, and fixed version endpoint to read from .env.Installer/CLI: replaced deprecated n8n basic auth with v2.x admin setup, preserved .env inode during model swap (cat > instead of mv), preserved VERSION across /etc/os-release sourcing, fixed dream-cli symlink resolution, prevented double-inclusion of extension compose files, added load_env to stop/start/restart, disabled ComfyUI compose when image generation is off, fixed COMPOSE_FLAGS word-splitting, added reverse-dependency check to dream disable, and added SEARXNG_SECRET to CI fixtures.Security: hardened ComfyUI with loopback binding and no-new-privileges, secured OpenCode with auto-generated passwords, removed API key from token-spy HTML, addedset -euo pipefailto the installer, and guarded nvidia-smi against [N/A] values on MIG/vGPU configurations.Observability (April 2026): added per-container CPU/memory stats endpoint to the host agent with Docker stats parsing and IEC unit handling, added read-only service logs endpoint scoped to dream-server containers via Docker Compose project label filtering, routed dashboard log viewing through host agent with status code clamping (502 for upstream errors) and Docker Compose label spoofing prevention, added per-service resource metrics aggregation endpoint with parallel fetch and split-TTL caching, added real-time bootstrap download progress tracking with background file-size monitor and atomic JSON status writes, added macOS native llama-server hot-swap with old-model rollback on health-check failure and PID reuse verification.CLI/Installer fixes: fixed dream-cli version display to read from .env instead of hardcoded 2.0.0, added user-extensions directory scanning to service registry with built-in-first deduplication, replaced compose-flags cache deletion with proper regeneration via resolve-compose-stack, fixed GPU assignment JSON generation for single-GPU NVIDIA systems, added compose syntax validation before container launch in phase 11, added dream_min version bounds to 15 extension manifests, and pre-created privacy-shield data directory in the installer
* Youness Yachouti (y-coffee-dev)— Designed and built the full-stack multi-GPU system: NVIDIA topology detection via nvidia-smi topo matrix parsing, four-phase GPU assignment algorithm with topology-aware service placement, docker-compose.multigpu.yml overlay generation, and the dashboard GPU Monitor page with per-GPU cards, SVG sparkline charts, topology visualization, and service assignment views. Added five dream gpu CLI subcommands (status, topology, assignment, validate, reassign) with --auto/--manual/--dry-run modes and bash tab completions. Rewrote lib/safe-env.sh to split on first = only, fixing base64 value truncation in .env parsing. Added GPU environment passthrough to dashboard-api, SDXL download guard for disabled ComfyUI, and ANSI escape stripping for nvidia-smi output. Contributed 345 lines of GPU-specific tests. Tested on real multi-GPU hardware including 4x RTX 4060 Ti, 4x RTX 4080, and 8x RTX 5060 Ti configurations.
* Tony363 (Tony Siu)— Raised dashboard-api test coverage to 95% with 3,500+ lines of tests across 14 files including comprehensive endpoint coverage for setup, privacy, workflows, updates, agents, and GPU monitoring, plus 7 BATS shell test suites covering logging, constants, path-utils, bootstrap-model, nvidia-topo, ui, and background-tasks. Added comprehensive architecture overview documentation (ARCHITECTURE.md) with Mermaid diagrams for service topology, installer pipeline, and compose layering. Fixed the pre-existing ThemeProvider CI failure that was blocking every PR frontend check. Reported the PyYAML import crash on Manjaro/Arch (resolve-compose-stack.sh) with clear root cause analysis. Drives developer outreach and ecosystem growth as head of Coffee and Code Philadelphia. Earlier work: hardened service-registry.sh against shell injection, improved PII scrubber with Luhn check, fixed token-spy settings persistence with atomic writes, fixed SSH command injection in session-manager.sh, narrowed broad exception catches across dashboard-api, and authored CLAUDE.md with project instructions and design philosophy. Built three AI-powered GitHub Actions workflows: consolidated code review with fork detection and protected file enforcement, label-gated issue-to-PR automation with 4-job pipeline (validate/implement/guardrails/create-pr) and prompt injection hardening (anti-injection preamble, 4000-char truncation, tool restrictions, secret scanning), and nightly AI scanners for code review/docs/autonomous scanning with budget caps and manual-only triggers. Fixed unified APU name fallback in GPU detection for Strix Halo. Prototyped a full Rust/Axum rewrite of the dashboard-api with 285 tests, constant-time auth middleware, 3-crate workspace, and ~25MB Docker image (work-in-progress — extension security features being ported). Fixed pipefail-safe hostname fallback in installer phase 13 for Arch/Manjaro compatibility
* latentcollapse (Matt C)— Security audit and hardening: OpenClaw localhost binding fix, multi-GPU VRAM detection, AMD dashboard hardening, and the Agent Policy Engine (APE) extension
* Igor Lins e Silva (igorls)— Stability audit fixing 9 infrastructure bugs: dynamic compose discovery in backup/restore/update scripts, Token Spy persistent storage and connection pool hardening, dotglob rollback fix, systemd auto-resume service correction, removed auth gate from preflight ports endpoint for setup wizard compatibility, added ESLint flat config for the dashboard, cleaned up unused imports and linting across the Python codebase, and resolved CI failures across dashboard and smoke tests
* Nino Skopac (NinoSkopac)— Token Spy dashboard improvements: shared metric normalization with parity tests, budget and active session tracking, configurable secure CORS replacing wildcard origins, and DB backend compatibility shim for sidecar migration
* Glexy (fullstackdev0110)— Added extension runtime check script for validating non-core service Docker state and optional HTTP health, wired it into the install summary phase and CI workflow with dedicated test suite and skip counter tracking, added troubleshooting documentation for extension runtime checks, added Linux portability documentation with support-matrix link and reinstall data writability check. Earlier work: fixed dream-cli chat port initialization bug, hardened validate.sh environment variable handling with safer quoting and .env parsing, removed allevalusage from installer/preflight env parsing, added a safe-env loader (lib/safe-env.sh) to prevent shell injection, unified all .env loading across 9 scripts to useload_env_file()eliminating duplicated parsers, added dream-cli status-json/config-validate/mode-summary commands, added extension manifest validation with versioned compatibility gating (dream_min/dream_max) for the v2 extension ecosystem, added comprehensive compatibility matrix documentation, added test suites with CI integration for manifest validation, health checks, env validation, and CPU-only path, made session-cleanup.sh portable across macOS/Linux (POSIX grep, stat, numfmt fallback), added --help flag to session-cleanup.sh, and fixed ShellCheck SC2086 warnings and SC2155 errors across health-check.sh, detect-hardware.sh, pre-download.sh, progress.sh, qrcode.sh, migrate-config.sh, llm-cold-storage.sh, session-manager.sh, and 07-devtools.sh, added Windows compose failure diagnostics with shared compose-diagnostics.ps1 library and reliable exit code handling across all dream.ps1 operations (start/stop/restart/update), added troubleshooting documentation for compose failures, expanded PowerShell lint CI coverage to Ubuntu+Windows matrix with root install.ps1 inclusion, and added secret-redaction warnings to Windows compose diagnostics output and install report documentation
* bugman-007— Parallelized health checks in dream status for 5–10× speedup using async gather with proper timeout handling, benchmark and test scripts, integrated backup/restore commands into dream-cli, added preset import/export with path traversal protection and archive validation, added preset diff command for comparing configurations with secret masking, quarantined broken edge quickstart instructions replacing them with supported cloud mode path, added SHA256 integrity manifests and verification for backups, added restore safety prompts requiring backup ID confirmation, added backup/restore round-trip integration test, added preset compatibility validation before load, added service registry tests to CI, added Python type checking with mypy, added disk space preflight checks to backup/restore with portable size estimation, and added session-level caching to compose flags resolution for performance, expanded dashboard-api test coverage for privacy, updates, and workflow endpoints, added structured logging to agent monitor replacing silent exception swallowing, added bash completion for dream-cli with dynamic backup ID resolution, added automatic pre-update backup with rollback command and health verification, fixed gitleaks CI to use OSS CLI instead of paid license action, added disk space preflight checks to backup/restore, and replaced disabled VAD patch with AST-based Python patcher for safe Whisper voice activity detection
* norfrt6-lab— Replaced 12+ silent exception-swallowing patterns with specific exception types and proper logging, added cross-platform system metrics (macOS/Windows) for uptime, CPU, and RAM, plus Apple Silicon GPU detection via sysctl/vm_stat
* boffin-dmytro— Added SHA256 integrity verification for GGUF model downloads with pre- and post-download checks, corrupt file detection with automatic re-download, fixed model filename casing mismatches, added network timeout hardening across 33+ HTTP operations preventing indefinite hangs, added port conflict and Ollama detection for the Linux installer matching macOS parity, fixed trap handler bugs in installer phases replacing explicit tmpfile cleanup for safe early-exit, added retry logic with error classification and exponential backoff for Docker image pulls, added a GPU detection progress indicator eliminating user anxiety during hardware scans, added Windows zip integrity validation with retry logic, added Docker image pull retry with timeout and post-pull validation viadocker inspect, added Intel Arc GPU detection and CPU-only default fallback replacing incorrect NVIDIA assumption, added compose stack validation during phase 02 catching syntax errors early, added background process tracking for FLUX model downloads with JSON-based task registry, and improved health check robustness with per-request timeout and adaptive exponential backoff, added unified cross-platform path resolution utilities with POSIX-portable disk space checks, added markdown local link validation for CI, added download robustness with exponential-backoff retry to macOS installer, added configurable health check timeouts to manifest schema solving slow-start services, added SHA256 checksum verification to restore operations with graceful fallback for older backups, added service dependency validation before compose up preventing missing-service failures, added comprehensive manifest schema validator, reduced installed footprint by excluding dev-only files via rsync, added strict error handling ('set -euo pipefail') to operational scripts, added doc link checker to CI, and added rsync progress indicators to backup/restore operations
* takutakutakkun0420-hue— Added log rotation to all base services preventing unbounded disk growth, and added open-webui startup dependency on llama-server health ensuring the UI never shows a broken state
* reo0603— Fixed Makefile paths after dashboard-api move and heredoc quoting bug in session-manager.sh SSH command, narrowed broad exception catches to specific types across dashboard-api, parallelized health checks for 17× faster execution, added compose.local.yaml for dashboard/open-webui/privacy-shield service dependencies, added .dockerignore files to all custom Dockerfiles reducing build context, fixed H2C smuggling vector in nginx proxy and added wss:// for HTTPS in voice agent, added comprehensive extension integration and hardware compatibility test suites, and hardened secret management with .gitignore patterns for key/pem/credential files and SQL identifier validation in token-spy
* Arifuzzaman Joy (Arifuzzamanjoy)— Pinned yq and docker-compose versions in the bootstrap Dockerfile replacing floating/latest/tags with reproducible ARG-based version pins, added Draft7Validator compatibility for jsonschema 3.x on Ubuntu 22.04/24.04, added compatibility blocks (dream_min version bounds) to 25 extension library manifests, added missing gpu_backends to 8 extension manifests, added cpu and none to the gpu_backends schema enum enabling CPU-only service declarations, fixed gpu_backends on 13+ extension manifests resolving schema validation failures, added missing required fields (icon, category, requirements, priority) to localai features, fixed env_vars schema compliance (name to key) in bark and rvc manifests, corrected privacy-shield service ID to match schema pattern, and fixed typo in baserow manifest tags
* nt1412— Wired dashboard-api agent metrics to Token Spy with background metrics collection, added TOKEN_SPY_URL/TOKEN_SPY_API_KEY env vars, fixed missing key_management.py in privacy-shield Dockerfile, and added ui_path to dashboard sidebar links so extension services open at their correct UI page
* evereq— Relocated docs/images to resources/docs/images for cleaner monorepo root
* championVisionAI— Added Alpine Linux (apk) and Void Linux (xbps) package manager support to the installer abstraction layer, hardened hardware detection with JSON output escaping and container/WSL2 detection, rewrote healthcheck.py with retries, HEAD-to-GET fallback, status code matching, and structured JSON output, hardened Docker phase with daemon start/retry logic and compose v1/v2 detection, added cross-platform python3/python command resolution with shared detection utility, and hardened env schema validation with robust .env parsing, enum validation, and line-number error reporting, added sim summary validation test suite with 10 test cases covering help, missing files, invalid JSON, and strict mode, hardened hardware detection with JSON output escaping and container/WSL2 detection, hardened healthcheck.py with retries and HEAD-to-GET fallback, hardened Docker phase with daemon start/retry and compose v1/v2 detection, fixed Windows python3/python command resolution, added extension audit workflow with 838-line Python auditor and 'dream audit' CLI command, added duplicate key detection to env validation, added compact JSON output mode and --help flag to hardware detection, and failed env validation on duplicate keys preventing silent config corruption
* buddy0323— Ported Windows installer phases 01-07 to native PowerShell decomposing the monolithic script into focused phase files, added Intel Arc SYCL tier map (ARC/ARC_LITE) with docker-compose.intel.yml overlay, detection logic, tier-map tests, and SHA256 verification, added Intel Arc oneAPI SYCL compose overlay with two-stage llama-sycl Dockerfile, added Intel Arc detection checks (lspci, Level Zero runtime, render nodes, group membership), and authored the Intel Arc support matrix documentation and setup guide
* blackeagle273— Enhanced macOS installer with idempotent .env and config generation preserving existing secrets across re-installs
* eva57gr— Fixed bash syntax error in Token Spy session-manager.sh SSH heredoc command, and unified port contract across installer, schema, compose, and manifests with canonical ports.json registry
* cycloarcane— Fixed unbound variable crash by guarding service-registry.sh sourcing in install-core.sh, health-check.sh, and 04-requirements.sh
* Rowan (rowanbelanger713)— Enhanced llama-server with configurable batch-size, threads, and parallel request knobs, added TTL caching and async threading to dashboard-api status endpoints, pooled httpx connections for LiteLLM, lazy-loaded React routes with memoized components, scoped CSS transitions to interactive elements, paused polling on hidden tabs, and split Vite output into vendor/icons chunks for faster loading
* gabsprogrammer— Designed and built the dashboard's "liquid metal" visual refresh with grouped service layout, token throughput signal charts, interactive SVG visualizations, collapsible sidebar, animated splash screen with full accessibility (ARIA dialog, prefers-reduced-motion, keyboard skip, low-performance device detection), and theme-aware CSS custom properties across all four themes. Fixed Windows PowerShell 5.1 parse errors by replacing Unicode em dashes, fixed dashboard-api extension catalog timeout, fixed health-check duplicate sr_load crash, fixed backup manifest .version JSON parsing, fixed llama-server default port fallback from 11434 to canonical 8080 in dream-preflight.sh, added set -euo pipefail, removed dead duplicate if/else branch, and added a 156-line preflight test suite with static analysis and runtime smoke tests
* onyxhat— Fixed missing variable initialization in installer scripts
If we missed anyone,open an issue. We want to get this right.

## License

Apache 2.0 — Use it, modify it, ship it. SeeLICENSE.

Built byLight Heart Labsand the growing resistance that refuses to rent what should be owned.

## About

Local AI anywhere, for everyone — LLM inference, chat UI, voice, agents, workflows, RAG, and image generation. No cloud, no subscriptions.

discord.gg/qGVygYada3

### Topics

 docker

 text-to-speech

 amd

 self-hosted

 nvidia

 speech-to-text

 workflow-automation

 ai-agents

 rag

 n8n

 llm

 llama-cpp

 comfyui

 local-ai

 open-webui

 strix-halo

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.1k

 stars
 

### Watchers

14

 watching
 

### Forks

199

 forks
 

 Report repository

 

## Releases2

Dream Server v2.0.0 — Strix Halo

 Latest

 

Mar 4, 2026

 

+ 1 release

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python43.3%
* Shell36.2%
* JavaScript9.2%
* PowerShell5.4%
* TypeScript3.0%
* HTML1.0%
* Other1.9%