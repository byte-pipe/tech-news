---
title: GitHub - cisco-ai-defense/defenseclaw: Security Governance for Agentic AI · GitHub
url: https://github.com/cisco-ai-defense/defenseclaw
date: 2026-04-05
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-05T01:02:32.009008
---

# GitHub - cisco-ai-defense/defenseclaw: Security Governance for Agentic AI · GitHub

# DefenseClaw

## Overview
- DefenseClaw is an enterprise governance layer for OpenClaw AI agents, positioned between agents and the infrastructure they run on.
- It enforces the principle “nothing runs until it’s scanned,” automatically blocking dangerous actions.
- The system protects against malicious skills, compromised MCP servers, and unsafe generated code.

## Capabilities
- **Skill, MCP, and Plugin Scanning**
  - Uses Cisco AI Defense scanners and an AI bill‑of‑materials generator to produce a unified ScanResult.
  - Findings are severity‑ranked: HIGH/CRITICAL → auto‑block, MEDIUM/LOW → install with warning, clean → pass.
  - Results are logged to a SQLite audit store and forwarded to SIEM.

- **CodeGuard**
  - Built‑in static analysis engine that scans source files line‑by‑line with regex rules.
  - Detects hard‑coded credentials, dangerous execution calls, outbound networking, unsafe deserialization, SQL injection, weak cryptography, and path traversal.
  - Runs automatically during scans and is also available via a sidecar API (`POST /api/v1/scan/code`).

- **Runtime Inspection**
  - *Message Inspection*: proxies every LLM prompt/completion to detect secrets, PII, and injection patterns; can log or block based on mode.
  - *Tool Inspection*: evaluates each tool call against six rule categories (secret, command, sensitive‑path, c2, cognitive‑file, trust‑exploit).
    - For write/edit tools, CodeGuard also scans the content.
    - Verdicts are allow, alert, or block; HIGH/CRITICAL findings cancel the call in action mode.

## Architecture
| Component | Language | Role |
|----------|----------|------|
| CLI | Python 3.11+ | Operator‑facing tool for scanners, block/allow management, TUI dashboard |
| Gateway | Go 1.25+ | Central daemon providing REST API, WebSocket bridge to OpenClaw, policy engine, inspection pipeline, SQLite audit store, SIEM export |
| Plugin | TypeScript | Runs inside OpenClaw, intercepts tool calls, exposes `/scan`, `/block`, `/allow` slash commands |

- CLI and Plugin communicate with the Gateway via a local REST API.
- The Gateway connects to the OpenClaw Gateway over WebSocket (v3) for event subscription and enforcement.
- A built‑in guardrail proxy inspects all LLM traffic in real time.
- Detailed diagrams and data flows are in `docs/ARCHITECTURE.md`.

## Installation
### Prerequisites
- Python 3.10+ (`python3 --version`)
- Go 1.25+ (`go version`)
- Node.js 20+ for the plugin (`node --version`)
- Git (`git --version`)

### Steps
1. **Install OpenClaw**
   ```bash
   curl -fsSL https://openclaw.ai/install.sh | bash
   openclaw onboard --install-daemon
   ```
   Verify with `openclaw gateway status`.

2. **Install DefenseClaw**
   ```bash
   curl -LsSf https://raw.githubusercontent.com/cisco-ai-defense/defenseclaw/main/scripts/install.sh | bash
   defenseclaw init --enable-guardrail
   ```
   Platform‑specific guidance is in `docs/INSTALL.md`.

## Quick Start
- List installed components:
  `defenseclaw skill list`
  `defenseclaw mcp list`
  `defenseclaw plugin list`
- Scan a specific skill:
  `defenseclaw skill scan <skill-name>`
- Scan all installed skills:
  `defenseclaw skill scan all`
- Scan an MCP server:
  `defenseclaw mcp scan <server-name>`
- Scan a plugin:
  `defenseclaw plugin scan <plugin-name>`
