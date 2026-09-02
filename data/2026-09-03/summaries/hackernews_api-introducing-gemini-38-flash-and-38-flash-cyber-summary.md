---
title: Introducing Gemini 3.8 Flash and 3.8 Flash Cyber
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/
date: 2026-09-03
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-03T07:21:33.241942
---

# Introducing Gemini 3.8 Flash and 3.8 Flash Cyber

# Introducing Gemini 3.8 Flash and 3.8 Flash Cyber

## Overview
- Third Flash release in six weeks, building on Gemini 3.7 Flash.
- Two variants released:
  - **Gemini 3.8 Flash** – general‑purpose, high‑reasoning and coding model.
  - **Gemini 3.8 Flash Cyber** – specialized cybersecurity model, available through the Fairwind Program.
- Both share the same foundational intelligence and use long‑running agentic loops for recursive evaluation and refinement.
- Pricing (introductory): $0.75 / M input tokens, $3.75 / M output tokens (expires Dec 31 2026).

## Gemini 3.8 Flash: long‑horizon coding and autonomous agents
- Shows substantial gains over 3.7 Flash, approaching performance of higher‑cost frontier models.
- Benchmarks:
  - Outperforms larger models on DeepSWE v1.1 (Long‑Horizon Software Engineering).
  - Leads on Vals Finance Agent V2 and Harvey’s Legal Agent Benchmark.
  - Achieves 54.9 % on HLE‑Verified for multi‑step reasoning across STEM, humanities, and professional domains.
- Design choice: “works harder” by executing extra reasoning steps and iteratively calling tools, sometimes using more tokens for higher effort levels.
- Developers can select lower effort levels for token‑efficient workloads or continue using 3.7 Flash.
- Demonstration projects built with a single prompt in Google Antigravity:
  - A wizard‑castle puzzle game.
  - Fully functional DOS‑style Google Maps with Street View.
  - Real‑time topographic maps using USGS data.
  - “Hardware Anatomy” 3D visualizer that creates explodable Three.js renderings of devices.

## Gemini 3.8 Flash Cyber: expert cyber performance
- Available only to trusted defenders via the Fairwind Program.
- **Autonomous vulnerability discovery**
  - Frontier‑level results on CyberGym benchmark, surpassing 3.5 Flash Cyber and larger models.
  - Internal benchmark across 20 languages shows >70 % success rate in finding diverse vulnerabilities.
- **Automated patching**
  - On CWE‑Bench (Collinear), achieves a pass@1 of 47.2 %, comparable to the leading frontier model (47.8 %) at much lower cost.
- **Real‑world impact at Google**
  - Chrome Security team: 2.6× more correct patches than larger commercial models.
  - Wiz: 7.5‑9.7 % higher recall on internal penetration‑testing benchmark, with 2.3‑5.2× lower cost.
  - Cloud Vulnerability Research team discovered a critical foundational vulnerability in under 2 hours (normally months).

## Fairwind Program feedback
- Partners (trusted government authorities, critical‑infrastructure operators, software maintainers) receive prioritized access to Flash Cyber.
- Testimonials highlight accelerated vulnerability discovery and cost‑effective patching.

## Safety and robustness
- 3.8 Flash includes safeguards against misuse in CBRN and cyber‑offense domains, following the Frontier Safety Framework.
- 3.8 Flash Cyber has a more permissive mitigation set for cybersecurity use, restricted to trusted defenders.
- Significant improvement in prompt‑injection robustness measured by the Gray Swan benchmark.

## Getting started
- **Developers:** Use Gemini API via Google AI Studio, Android Studio, or Stitch; explore agent‑first workflows in Google Antigravity; refer to developer docs.
- **Enterprises:** Access through Gemini Enterprise.
- **Consumers:** Available to Google AI Pro and Ultra subscribers via Gemini app, AI Mode in Google Search, and Gemini in Google Sheets.
- **Cyber defenders:** Apply for Fairwind Program access.

## Pricing change
- Introductory price ends Dec 31 2026.
- Effective Jan 1 2027: $1.50 / M input tokens, $7.50 / M output tokens.

## Related stories
- “Proactive cyber defense for governments and enterprises” by Four Flynn (AI category).