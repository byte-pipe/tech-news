---
title: Introducing GPT-Live | OpenAI
url: https://openai.com/index/introducing-gpt-live/
date: 2026-07-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-09T15:21:32.488372
---

# Introducing GPT-Live | OpenAI

# Introducing GPT‑Live Summary

## Overview
- Launch of GPT‑Live, a new generation of voice models enabling natural, real‑time human‑AI conversation.  
- Built on a full‑duplex architecture that can listen and speak simultaneously, allowing acknowledgments (“mhmm”, “yeah”) and seamless back‑and‑forth.  
- Delegates complex tasks (web search, deep reasoning) to the latest frontier model (GPT‑5.5 at launch) while maintaining conversational flow.  
- Powers the updated ChatGPT Voice experience and will be extended to the API.

## Architectural Advances
### Continuous interaction
- Full‑duplex design processes input continuously while generating output.  
- Makes interaction decisions many times per second (speak, listen, pause, interrupt, invoke tools).  
- Enables more natural timing, live translation, and reduced latency.

### Delegation for deeper work
- Separates real‑time interaction (GPT‑Live) from intensive tasks handled by a background model (e.g., GPT‑5.5).  
- Allows the voice model to keep conversing while background reasoning or search occurs.  
- Supports seamless updates to newer frontier models.

## Versions and Rollout
- Two initial variants released today: **GPT‑Live‑1** and **GPT‑Live‑1 mini** for global ChatGPT users.  
- Planned API availability; developers and enterprises can sign up for notifications.  
- Different reasoning levels: Instant (fast), Medium, and High (more thorough) using GPT‑5.5 Instant or GPT‑5.5 Thinking models.

## Evaluations
- New human evaluations measured pleasantness, turn‑taking, interruptions, flow, and naturalness.  
- GPT‑Live‑1 and GPT‑Live‑1 mini strongly preferred over Advanced Voice Mode in 5–10 minute head‑to‑head tests.  
- Specific benchmarks:
  - GPQA: superior expert‑level scientific reasoning.  
  - BrowseComp: better agentic web search and hard‑to‑find information retrieval.  
  - τ³‑Voice Telecom (internal): improved performance on realistic multi‑turn telecom support tasks.

## New ChatGPT Voice Experience
- Over 150 million weekly voice users now receive:
  - **More natural conversations**: interrupt, pause, request slower speech; model acknowledges with verbal cues; nine remastered voices.  
  - **Smarter answers**: access to frontier models; selectable reasoning depth (Instant, Medium, High).  
  - **Better listening**: respects pauses, stays quiet on request, robust to background noise.  
  - **Visual answers**: rich cards for weather, stocks, sports, etc., alongside voice; continued support for search, memory, images, file uploads.

## Safety for Voice
- Designed with safety‑by‑default principles, extending safety advances from latest models.  
- Added dedicated safety training for voice‑specific risk areas and new safeguards.  
- Expanded safety testing to reflect real‑world voice usage scenarios.