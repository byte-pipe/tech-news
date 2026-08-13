---
title: Introducing Grok 4.6 | SpaceXAI
url: https://x.ai/news/grok-4-6
date: 2026-08-12
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-13T11:43:57.587436
---

# Introducing Grok 4.6 | SpaceXAI

# Introducing Grok 4.6

## Overview
- Successor to Grok 4.5, emphasizing long‑running agents and ambitious interactive/visual tasks.  
- Designed for complex, multi‑step workflows such as research, codebase analysis, and turning ideas into polished applications.  
- Available now in Cursor, Grok Build, API, and partner platforms (OpenRouter, Vercel, Cloudflare).  

## Performance Benchmarks
- Matches GPT‑5.6 Sol on the Artificial Analysis Intelligence Index (composite of nine benchmarks).  
- Scores (higher is better):  
  - AA Intelligence Index: 61 (Grok 4.6) vs 56 (GPT‑5.6 Sol)  
  - GDPVal‑AA v2: 1753 vs 1728 (GPT‑5.6 Sol)  
  - CursorBench v3.2: 69.9 % vs 67.2 % (GPT‑5.6 Sol)  
  - DeepSWE v1.1: 65.9 % vs 73 % (GPT‑5.6 Sol)  
  - FrontierCode v1.1 (Extended): 61.3 % vs 60.6 % (GPT‑5.6 Sol)  
  - Additional benchmarks (APEX‑Agents, Terminal‑Bench, APEX‑SWE, AA‑Briefcase, Harvey LAB) show Grok 4.6 generally outperforming Grok 4.5 and comparable to or exceeding GPT‑5.6 Sol.  

## Training Details
- Longer supplemental training run than Grok 4.5.  
- Curated model‑generated data for reasoning, advanced technical concepts, and high‑quality engineering content.  
- Improved optimizer and training recipe strengthened the foundation for supervised fine‑tuning (SFT) and reinforcement learning (RL) stages.  
- Used Grok 4.5 to regenerate SFT trajectories across reasoning, agent harnesses, and domains (STEM, software engineering, knowledge work); filtered problematic traces with model‑based checks.  

## Project Capabilities
- Excels at converting broad product ideas into functional first versions: research, architecture, core implementation, and iterative refinement.  
- Demonstrates self‑testing and verification on longer task sequences.  
- Produces stronger initial passes on visual and interactive projects, establishing structure and visual language in a single pass.  

## Safety and Evaluation
- Safeguards upgraded and calibrated to match expanded capabilities.  
- Safety stack aims to maximize utility while protecting against misuse in areas like vulnerability patching and AI research augmentation.  
- Conducted the widest‑ever pre‑deployment testing suite, plus extensive post‑deployment and third‑party evaluations.  

## Availability & Pricing
- Immediate access in Cursor and Grok Build; also via API and partner integrations.  
- Pricing: $2 per million input tokens, $6 per million output tokens; a “fast” variant costs twice as much.  
- Promotional offer: 2× included usage in Grok Build and Cursor for the first week.  

## Getting Started
- Create an API key through the SpaceXAI portal.  
- Consult API documentation to integrate Grok 4.6 into your stack.  
- Try Grok 4.6 for free in Grok Build at x.ai/build.  
- Installation script available via `curl -fsSL https://x.ai/cli/install.sh | bash`.