---
title: Automate agent development lifecycles with Gemini Enterprise | Google Cloud Blog
url: https://cloud.google.com/blog/topics/developers-practitioners/automate-agent-development-lifecycles-with-gemini-enterprise/
date: 2026-08-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-09T00:35:18.330942
---

# Automate agent development lifecycles with Gemini Enterprise | Google Cloud Blog

# Automate your agent development lifecycle using any coding agent

## Overview
- The blog post walks through building a production‑ready “Industry Watch” agent that compares semiconductor company press releases with SEC 8‑K filings.  
- It demonstrates the full agent lifecycle—setup, build, deploy, govern, evaluate, and publish—using the Agents CLI and Gemini Enterprise tools.  
- The goal is to eliminate the fragmented, prototype‑only workflow that forces developers to juggle multiple consoles and tools.

## Architecture: Why this needs an agent, not a chatbot
- The analyst’s question requires fresh data from two live sources (SEC EDGAR and GDELT/IR feeds) and a deterministic join; a static chatbot would hallucinate outdated or fabricated answers.  
- An agent architecture uses three deterministic FunctionTools to fetch disclosures, fetch public claims, and reconcile them, ensuring every claim is traceable to a real URL or accession number.  
- The model only narrates the results; the core logic runs in pure Python, preventing hallucination and protecting against poisoned inputs.

## Stage 1 – Teach your Agent Platform Skills
- Install the Agents CLI, which adds lifecycle skills (scaffolding, deployment, evaluation, publishing) to the coding assistant.  
- Use the Developer Knowledge MCP so the agent can look up current platform documentation instead of relying on stale training data.  
- Example command: `uvx google-agents-cli setup` followed by a prompt that installs the CLI and MCP, authenticates with the existing gcloud ADC, pins the project, and sets the region to `us-central1`.

## Stage 2 – Build the agent from a prompt
- **Scaffold**: Prompt the coding agent to create a prototype ADK agent named `industry-watch` with the desired sector‑intelligence focus.  
- **Add deterministic tools**: Describe three FunctionTools—`fetch_company_disclosures`, `fetch_public_claims`, and `reconcile_claims_vs_disclosures`. The coding agent generates `tools.py` with typed Python functions, including a proper SEC User‑Agent header and throttling for GDELT.  
- **Local test**: Run the scaffolded agent locally, ask “what changed for NVDA and AMD last week?”, and verify that the tool outputs are returned and grounded in source data.

## Stage 3 – Deploy to a Managed Runtime
- Deploy the prototype to **Agent Runtime** using `agents-cli deploy`, allowing autoscaling, cold‑start optimization, and zero‑cost idle periods.  
- Enable **AI Sessions** and a **Memory Bank** so the agent retains watch‑list, sector, and briefing format across multi‑turn interactions and separate sessions.  
- Move the deterministic join and scoring logic into the **code‑execution sandbox** to keep Python execution isolated from the LLM while preserving the same interface.

## Governance, Evaluation, and Publishing (brief)
- After deployment, lock down identity and add prompt‑injection screening to secure the agent.  
- Run automated pass/fail tests that check grounding, accuracy, and materiality scoring.  
- Publish the vetted agent within Gemini Enterprise so analysts can access it on demand.

## Key Takeaways
- The Agents CLI provides an end‑to‑end, opinionated workflow that keeps developers inside a single coding environment.  
- Deterministic FunctionTools eliminate hallucination and ensure every answer is auditable.  
- Managed runtimes, AI Sessions, and Memory Banks turn a local prototype into a reliable, stateful production service.  
- Gemini Enterprise’s platform integrates setup, security, testing, and publishing, reducing friction and keeping momentum in AI projects.