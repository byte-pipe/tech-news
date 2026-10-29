---
title: Introducing Gemini 4 Carbon
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
date: 2026-10-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:01:03.863606
---

# Introducing Gemini 4 Carbon

# Gemini 4 Carbon: our next frontier model

## Overview
- Announced on Oct 28 2026 as the strongest Gemini model to date.  
- Built on Gemini 4 Argon, released two weeks earlier, emphasizing rapid capability gains and safety.  
- Targets long‑horizon engineering tasks, agentic workflows, and advanced cybersecurity defense.  
- Initial access limited to a subset of cyber defenders and trusted partners via the Fairwind Program; broader release planned after feedback and guardrail iteration.  

## Performance Highlights
- Ranked #1 on v5.0 Artificial Analysis Intelligence Index with a score of 59.  
- Cybersecurity benchmarks (no guardrails):
  - SEC‑bench Pro: 88.2 % (vulnerability detection).  
  - ExploitGym: 54.8 % (exploitation validation).  
  - CWE‑bench: 71.0 % (patch generation).  
- Coding and agentic tasks show strong uplift; internal tests report >2× success rate for secure code generation versus Argon.  
- Web development: +89 Elo points, ranking #4 (1768) on WebDev Arena.  
- Chrome team observed >10× improvement over another large frontier model for high‑quality patches.  
- Wiz’s Scan for Good initiative notes leading performance in web penetration testing.  

## Coding & Reasoning for Long‑Horizon Tasks
- Designed for sustained, multi‑step engineering problems such as root‑causing and patching subtle bugs in large codebases.  
- Demonstrated ability to run continuously for days, persisting through dead ends.  
- Enhanced output quality across coding, scientific, full‑stack web development, and multimodal understanding.  

## Safety & Security Advances
- Extends Argon’s multi‑layered safety stack: training safeguards, real‑time misuse defenses, prompt‑injection resistance, chain‑of‑thought monitoring.  
- Alignment improvements:
  - Shortcut/cheating attempts on Terminal‑Bench 4.0 reduced to 0.0 % success, 0.4 % attempt rate.  
  - High‑severity misalignment alerts dropped ~80 % in internal live coding.  
  - Unsupported claims cut ~2× compared with Argon.  
  - Overreach reduced 26 %; under‑service reduced 29 %.  
- Prompt‑injection resistance achieved 0.0 % success on Gray Swan’s IPI benchmark (previous Argon 0.7 %).  
- Greater transparency: methodological caveats included in deliverables; ambiguous situations trigger source retrieval and discrepancy reporting.  

## Rollout & Pricing
- Introductory price matches Argon: $2 per 1M input tokens, $10 per 1M output tokens; cached input tokens at 95 % discount.  
- After introductory period: $4 per 1M input tokens, $20 per 1M output tokens.  
- Gradual access expansion planned for developers, businesses, and consumers following safety validation.  

## Related Stories
- “Developing Gemini 4 Argon responsibly and safely” – Anca Dragan & Raluca Ada Popa.  
- “Gemini 4 Argon is now available for developers.”  
- “Gemini 4 Argon: Built to solve your hardest problems” – Koray Kavukcuoglu.  
- “The latest AI news we announced in September 2026” – Blog Team.  
- “Gemini 4 Argon: our next era of frontier intelligence” – Koray Kavukcuoglu.  
- “See what 4 builders are making with Gemini 3.8 Flash” – Lindsey Lanquist.