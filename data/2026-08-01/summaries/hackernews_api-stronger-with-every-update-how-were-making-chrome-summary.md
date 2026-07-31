---
title: Stronger with every update: How we’re making Chrome and the web safer in the AI Era
url: https://blog.google/security/chrome-stronger-with-every-update/
date: 2026-07-31
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-01T03:10:11.107765
---

# Stronger with every update: How we’re making Chrome and the web safer in the AI Era

# Stronger with every update: How we’re making Chrome and the web safer in the AI Era

## Overview
- Large Language Models (LLMs) are transforming software security by automating vulnerability discovery at a scale beyond human expertise.  
- The Chrome Security Team deploys AI models to accelerate every stage of a bug’s life cycle—discovery, triage, fixing, and release—aiming for faster remediation and greater resilience.

## The Life of a Bug
1. The bug is found.  
2. The bug is triaged.  
3. The bug is fixed.  
4. A new Chrome update containing the fix is released.  
5. Chrome restarts and applies the update.  

The team’s objective is to compress the time required for each step.

## AI‑Powered Vulnerability Discovery
- **2023‑2025 milestones**  
  - 2023: Integrated LLMs to expand security fuzzing coverage.  
  - 2024: Partnered with Project Zero on *Naptime*, giving LLMs specialized research tools.  
  - 2025: Collaborated with DeepMind and Project Zero on *Big Sleep*, an AI agent that uncovered bugs in the V8 engine and graphics stack.  
- **Early 2026 breakthrough**  
  - Built a Gemini‑based agent that scanned the broader Chrome codebase, discovering a sandbox‑escape bug that had persisted for 13 years.  
- **Enhancements to the discovery pipeline**  
  - Model interoperability to combine strengths of open‑weight and proprietary models.  
  - Knowledge base containing all prior CVEs and Chrome’s complete Git history, extending LLM reasoning beyond its original training data.  
  - Encouragement of `SECURITY.md` files to clarify trust boundaries for the models.  
  - Introduction of a separate “critic” agent that consumes `SECURITY.md` content.  
  - Re‑running models multiple times to mitigate non‑determinism and capture improvements.  
- **Safety guardrails**  
  - Source code is analyzed only at rest on locked‑down machines without general internet access.  
  - Network requests are intercepted and allowed only via strict allowlists based on the initiating application.  
  - Models never run in unrestricted mode; sub‑agents are confined to designated source directories.  
- **Complementary role**  
  - AI detection augments existing fuzzing, which remains effective for long‑range interaction bugs.  
  - External researchers continue to be rewarded through the Chrome Vulnerability Reward Program (VRP); in 2026 the volume of external reports surpassed the total for 2025, prompting a VRP refocus toward submissions that complement internal AI findings.

## AI‑Assisted Triaging
- Traditional manual triage took 5–30 minutes per report; the new automated pipeline blends rule‑based logic with AI to boost throughput and accuracy.  
- **Four‑phase automated process**  
  1. **Noise filtering** – removes spam, duplicates, and ensures the report clearly describes a Chrome security issue.  
  2. **Reproduction** – validates a proof‑of‑concept, runs the bug on affected OS and browser versions, and attaches stack traces.  
  3. **Metadata enrichment** – adds introduction version, severity rating, and leverages `SECURITY.md` for contextual understanding; severity guidelines are now clearer for automatic application, though developers can adjust them.  
  4. **Automatic assignment** – routes the issue to the appropriate component and human owner.  
- Estimated savings of hundreds of developer hours each month, freeing the team to focus on higher‑level security priorities.

## AI‑Driven Fix Generation
- **Multi‑agent workflow**  
  - A fixing agent proposes multiple candidate patches.  
  - A critic agent evaluates candidates, selects the best fit, and produces supporting artifacts for developer review.  
  - The fixing and critic agents iterate in a loop that mirrors a code‑review process, enforcing Chromium, Google, and local style guidelines.  
  - Test‑writing agents generate cross‑platform tests for the fixes, eliminating weeks of manual effort.  
- **Impact**  
  - In Chrome milestones 149 and 150, 1,072 security bugs were fixed, exceeding the total number fixed across the previous 23 milestones combined.  

## Partnerships and Integrated Tools
- Ongoing collaboration with Google DeepMind and Project Zero on tools such as *Big Sleep* and *CodeMender*.  
- These AI‑driven tools are now natively integrated into Chrome’s continuous integration pipeline, reinforcing the security development lifecycle.