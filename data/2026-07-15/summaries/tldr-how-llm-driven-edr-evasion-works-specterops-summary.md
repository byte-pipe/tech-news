---
title: How LLM-driven EDR evasion works | SpecterOps
url: https://specterops.io/blog/2026/06/29/llm-powered-edr-analysis/
date: 2026-07-15
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-15T04:50:45.303073
---

# How LLM-driven EDR evasion works | SpecterOps

# Accelerating EDR Evasion with LLM‑Driven Analysis

## Introduction
- Author reflects on long‑standing hobby of reverse‑engineering EDR/AV engines and the slowdown caused by manual analysis.
- Recent availability of large language models (LLMs) prompted experimentation to accelerate evasion research.

## Disclosure Philosophy
- Red‑team evasion techniques are traditionally shared informally; the author argues for public disclosure to challenge industry assumptions.
- References Justin Elze’s blog on TrustedSec’s internal LLM use, noting parallel observations across the security community.
- Emphasizes that the post is not a vendor critique but a reality check on current industry resilience.

## Current Findings
- The “big 5” endpoint security products are increasingly vulnerable to LLM‑assisted reverse engineering.
- Simple harnesses can extract and analyze local detection rules, signatures, and models.
- Internal collections of vendor rules show repeated failures against SpecterOps tooling (Mythic agents, SCCMHunter, LDAP‑based Bloodhound detection).

## The “Day Shift” Harness
- **Model**: Started with OpenAI GPT‑5.4‑Cyber, later upgraded to GPT‑5.5‑Cyber.
- **Infrastructure**: Runs in Codex‑CLI inside a Docker container on a dedicated host (“Bishop”).
- **Core Files**:
  - `REPORT.md` – aggregates findings for human review.
  - `STATE.md` – tracks analysis progress and events.
  - `CODEMAP.md` – stores references to interesting disassembly regions.
  - `AGENTS.md` – provides instructions for the model on how to use the above files.
- **Execution Loop**: A Zsh script repeatedly invokes `codex‑dind exec` with a prompt that:
  1. Instructs the model to enumerate detections, hooks, mitigations, rules, and ML models in the target EDR.
  2. Requests extraction methods for raw content and documentation of model loading/behavior.
  3. Limits the model to local file access only.
- **Tooling Integration**: Binary Ninja is exposed via a simple MCP server for the model to query binary data.
- **Loop Benefits**: Clears the context window each iteration, preventing premature task termination and allowing the model to revisit prior markdown for new leads.

## Practical Demonstration with Cortex XDR
- Chosen for its “cool” features and as a representative of major EDR products.
- The harness was pointed at Cortex’s installation directories (`ProgramFiles` and `ProgramData`).
- Results included:
  - Identification of detection rules targeting SpecterOps tools.
  - Extraction of obfuscated/encrypted rule blobs.
  - Preliminary documentation of any embedded ML models and their risk‑rating logic.
- No full rule dump or decryption keys were released; only enough detail to prove the efficacy of state‑of‑the‑art LLMs in generating actionable evasion techniques.

## Conclusions
- LLMs can automate large portions of EDR reverse engineering, turning a labor‑intensive grind into a repeatable, fast loop.
- The simplicity of the “Day Shift” harness demonstrates that sophisticated multi‑agent orchestration is unnecessary for effective results.
- The industry must recognize that current detection models, especially those relying on static rule sets, are increasingly exposed to automated analysis and evasion.