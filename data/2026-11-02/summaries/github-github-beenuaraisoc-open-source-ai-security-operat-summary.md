---
title: GitHub - beenuar/AiSOC: Open-source AI Security Operations Center: alert fusion, LLM-agent triage, MITRE ATT&CK investigation, and a replayable decisi...
url: https://github.com/beenuar/AiSOC
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-02T08:49:46.336538
---

# GitHub - beenuar/AiSOC: Open-source AI Security Operations Center: alert fusion, LLM-agent triage, MITRE ATT&CK investigation, and a replayable decisi...

# AiSOC – Open‑source AI Security Operations Center

## Overview
- AiSOC is a self‑hostable, open‑source SOC that ingests security telemetry, runs a large rule library, correlates alerts into incidents, and investigates them with AI agents.
- Every AI prompt, tool call, and decision is recorded, providing a fully auditable decision ledger.
- Threat intelligence (e.g., CISA KEV catalog) is applied locally without needing external API keys.
- Human operators approve any response before it is sent to a vendor.

## Core Capabilities
- **Telemetry Normalization** – Collects data from diverse security tools and normalizes it for processing.  
- **Rule Engine** – Executes 2 534 executable rules from a 7 015‑rule library to detect threats.  
- **Incident Fusion** – Groups related alerts into incidents for unified analysis.  
- **AI‑Driven Investigation** – An LLM‑agent performs step‑by‑step triage; each prompt and tool invocation is logged.  
- **Response Proposal** – The agent suggests remediation actions, which require human approval.  
- **Continuous Threat Intel** – New intel automatically re‑scans historical data.  

## Architecture Highlights
- Runs on Docker Compose (v2) with a ~2 GB local model stored in a Docker volume.  
- Provides a REST API and an MCP server compatible with Claude, Cursor, and Continue.  
- Includes a “Technical Guide” PDF covering server sizing, model placement, failure modes, and API details.  

## Quick Start
```bash
git clone https://github.com/beenuar/AiSOC && cd AiSOC
make up
```
- **Windows**: `iwr -useb https://raw.githubusercontent.com/beenuar/AiSOC/main/install.ps1 | iex`  
- **Linux/macOS**: `curl -fsSL https://raw.githubusercontent.com/beenuar/AiSOC/main/install.sh | bash`  
- **Docker‑less demo**: `pip install aisoc-sandbox && aisoc-sandbox demowalks` (runs an offline alert walkthrough in <30 s).  
- **GitHub Codespaces**: Open the repo and run `make up` in the terminal.  

## System Requirements
- Docker Compose v2, 8 GB RAM, 20 GB free disk space in the Docker VM.  
- Python 3.9+ and Bash.  
- `make doctor` validates the environment; `make up` creates a `.env` file with fifteen generated secrets.  

## Documentation & Resources
- **Technical Guide (PDF)** – In‑depth explanation of architecture, sizing, and troubleshooting.  
- **Docs site** – API reference, MCP usage, and console walkthroughs.  
- **Demo video** – 3‑minute run showing alert ingestion, AI verdict, and SOC UI.  

## Repository Structure (selected)
- `apps/`, `services/` – Core application code.  
- `detections/`, `hunts/`, `playbooks/` – Rule sets, detection logic, and response playbooks.  
- `plugins/` – Extensible connectors for external tools.  
- `schemas/`, `profiles/` – Data schemas and auditd profiles.  
- `examples/`, `tests/` – Sample data and test suites.  
- `AGENTS.md`, `README.md`, `ROADMAP.md` – Project overview and future plans.  

## Licensing
- Distributed under the MIT License; free for commercial and non‑commercial use.  

---  
AiSOC delivers a complete, auditable AI‑enhanced SOC that can be deployed on‑premises without external API dependencies, enabling organizations to automate detection, investigation, and response while retaining full human oversight.