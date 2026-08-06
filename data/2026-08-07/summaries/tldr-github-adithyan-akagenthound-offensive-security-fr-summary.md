---
title: GitHub - adithyan-ak/AgentHound: Offensive security framework for AI agent infrastructure - recon, credential looting, model exfiltration, poisoning,...
url: https://github.com/adithyan-ak/agenthound
date: 2026-08-07
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-07T06:01:55.401424
---

# GitHub - adithyan-ak/AgentHound: Offensive security framework for AI agent infrastructure - recon, credential looting, model exfiltration, poisoning,...

# AgentHound – Offensive Security Framework for AI Agent Infrastructure

## Overview
- Open‑source framework that performs full‑stack offensive engagements on AI agent environments (recon, fingerprinting, credential looting, model inventory, inversion, poisoning, persistence).  
- Merges all discovered facts into a Neo4j graph to expose attack paths; described as “BloodHound for the agentic stack.”  
- Intended for authorized use only; modules are read‑only by default and require explicit dry‑run or consent for active exploitation.

## Core Capabilities
- **Full‑spectrum surface** – Scans MCP, A2A, model gateways, inference servers, vector stores, MLOps platforms, notebooks, and 12 agent client formats.  
- **Credential inventory** – Uses a LiteLLM master key to enumerate masked provider references, hashed virtual keys, and spend metadata; only real credential values are correlated.  
- **Model inventory** – Enumerates Ollama/vLLM models (names, digests, sizes, stable modelfile hashes, system‑prompt presence, fine‑tune signals). Optional raw modelfile capture via opt‑in.  
- **Model inversion** – Pure‑Go GGUF parser extracts likely fine‑tune vocabulary tokens from embedding matrices, adding training‑data residues as graph nodes.  
- **Active exploitation** – Supports tool/instruction poisoning, ContextForge‑managed MCP tool description rewriting, and malicious MCP server implants. Mutations are dry‑run by default with provider‑specific rollback state.  
- **RAG & vector‑store analysis** – Inventories Qdrant collections, Jupyter sessions, notebook trees; distinguishes anonymous vs. authenticated access.  
- **Cross‑protocol & credential‑chain path analysis** – 15 post‑processors compute credential chains, cross‑protocol pivots, and exfiltration routes across MCP and A2A.  
- **Indirect prompt injection modeling** – Treats injection as taint propagation; tracks untrusted‑input tools → tainted siblings → high‑impact sinks as graph edges.  
- **Detection & intelligence** – 19 pre‑built attack‑path queries, 35 detection rules, risk scoring (0‑100), and retest‑as‑diff; mapped to OWASP MCP/Agentic Top 10 and MITRE ATLAS.  
- **Extensibility** – New attacks added by implementing an action interface and registering the module; same SDK, lifecycle, and graph integration.

## Stack Planes Covered
- **Surface** – Discovery, validation, active ops across all layers.  
- **Agent clients** – 12 MCP client config formats plus instruction files (CLAUDE.md, AGENTS.md, .cursorrules).  
- **MCP** – Stdio/HTTP‑SSE servers, tools, resources, prompts, authentication; credential‑reach verification and tool‑description poisoning.  
- **A2A** – Agent cards, JWS verification, skills, delegation, authentication; cross‑protocol delegation analysis.  
- **LiteLLM** – Master‑key record, masked references, hashed virtual‑key metadata with spend context; cross‑service credential correlation.  
- **Ollama / vLLM** – Model metadata, stable hashes, system‑prompt detection, fine‑tune signals; optional raw file capture and GGUF extraction.  
- **Qdrant** – Collection stats, point counts, optional bounded payload samples; read‑only exposure analysis.  
- **MLflow** – Experiments, runs, registered models, artifact URIs; read‑only exposure analysis.  
- **Jupyter** – Sessions, bounded notebook trees; anonymous vs. authenticated exposure analysis.  
- **Open WebUI / LangServe** – Authentication posture, upstream/RAG credential inventory, exposure evidence; fingerprinting and read‑only credential inventory.

## By the Numbers
- 8 lifecycle CLI commands: `scan`, `discover`, `loot`, `extract`, `poison`, `implant`, `revert`, `campaign`.  
- 8 fingerprinters, 6 looters, 1 model‑inversion extractor, 2 poisoners, 1 implanter.  
- Graph schema: 23 node labels, 32 edge kinds (20 raw, 12 composite), 15 post‑processors.  
- Intelligence: 35 text‑detection rules, 7 YAML fingerprint rules, 1 code‑backed Jupyter detector, 19 pre‑built attack‑path queries; mapped to OWASP MCP Top 10, OWASP Agentic Top 10, MITRE ATLAS.  
- Distributed as a single static collector binary with no DB/UI/server dependencies; offline config‑only discovery possible.  
- Releases are Apache‑2.0, Cosign‑signed, with per‑archive SPDX SBOMs.

## Quick‑Start Workflow
1. **Start analysis server** – Docker Compose launches Neo4j, Postgres, and UI on `127.0.0.1:8080`.  
   ```bash
   curl -sSfL https://raw.githubusercontent.com/adithyan-ak/agenthound/main/docker/docker-compose.public.yml |
   docker compose -f - -p agenthound up -d --wait
   ```
2. **Install collector** – Single static binary placed in `~/.local/bin`.  
   ```bash
   curl -sSfL https://raw.githubusercontent.com/adithyan-ak/agenthound/main/install.sh | sh
   export PATH="$HOME/.local/bin:$PATH"
   ```
   *Alternative:* Homebrew (`brew install adithyan-ak/agenthound/agenthound`) or `go install` (Go 1.25+).  
3. **Run scans** – Offline, read‑only scans ingest results into the server.  
   - Normal scan: `agenthound scan --config --ingest http://127.0.0.1:8080`  
   - Deep scan (adds bounded nested‑project instruction discovery): `agenthound scan --config --deep --ingest http://127.0.0.1:8080`  
   - Use `--project-dir /path/to/project` to target non‑current directories.

## Safety & Authorization
- Modules are read‑only unless explicitly invoked for active exploitation.  
- Users must own or have written permission to assess the target infrastructure.  
- Documentation includes a “Safety & Authorization” section reinforcing responsible use.