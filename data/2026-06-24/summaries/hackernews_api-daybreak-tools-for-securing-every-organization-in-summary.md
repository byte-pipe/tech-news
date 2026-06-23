---
title: Daybreak: Tools for securing every organization in the world | OpenAI
url: https://openai.com/index/daybreak-securing-the-world/
date: 2026-06-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-24T01:02:14.764536
---

# Daybreak: Tools for securing every organization in the world | OpenAI

# Daybreak: Tools for securing every organization in the world

## Overview of new announcements
- Expansion of **Daybreak** to democratize machine‑speed patching of vulnerable software, with models already generating patches for critical bugs in browsers, network gear, FreeBSD, and the Linux kernel.  
- Launch of an updated **Codex Security** plugin that embeds security‑engineer‑level workflows directly into developers’ tools.  
- Full release of **GPT‑5.5‑Cyber** to trusted defenders, achieving state‑of‑the‑art results on CyberGym (85.6% vs. 81.8% for GPT‑5.5).  
- Introduction of the **Daybreak Cyber Partner Program** to extend model access through partner products and services.  
- Creation of **Patch the Planet**, a collaboration with Trail of Bits, HackerOne, and open‑source maintainers (e.g., cURL, Go, Python, Sigstore, pyca/cryptography) to accelerate fixes from discovery to deployment.

## Cyber defense at an inflection point
- AI has shifted the bottleneck from vulnerability discovery to vulnerability patching.  
- Modern models can navigate large codebases, reason about attack paths, and surface hidden security issues, but defenders need tools to remediate quickly.  
- Effective protection requires the full remediation loop: validation, impact assessment, patch development, testing, coordinated disclosure, and deployment.  
- Democratizing advanced defensive AI is essential because software underpins critical infrastructure, business applications, and government networks.

## Codex Security: from findings to fixes
- Since the March research preview, Codex Security has scanned >30 million commits across >30 000 codebases.  
- Human reviewers marked >70 000 findings as fixed; >500 000 findings were automatically confirmed fixed.  
- Core premise: place a virtual security engineer beside every developer by integrating directly into Codex.  
- Updated plugin capabilities:
  - Deep scans of entire codebases, subsets, or specific commits.  
  - Generation of severity‑ranked reports, validation evidence, threat models, and targeted patches.  
  - Triage of existing findings from scanners, bug‑bounty reports, or ticketing systems and automated patch generation at scale.  
  - Export to vulnerability‑management tools via SARIF, CodeQL, etc., and integration with Codex CLI or the Codex app for automated pipelines.

## GPT‑5.5‑Cyber: pairing capability with permissiveness
- Updated model reduces unnecessary refusals while enhancing specialized cybersecurity performance.  
- Enables sustained analysis of large codebases: component identification, reachability analysis, controlled‑environment validation, patch creation, and evidence preparation for human review.  
- Benchmark results:
  - CyberGym: 85.6% success (single‑model) vs. 81.8% for GPT‑5.5.  
  - ExploitGym: 39.5% vs. 25.95% for GPT‑5.5.  
  - SEC‑bench Pro: (partial data provided, indicating superior performance).  
- Designed to support the complete remediation loop rather than merely increasing the number of findings.