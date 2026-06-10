---
title: Anthropic says these topics are too dangerous to let its Fable 5 model talk about - Ars Technica
url: https://arstechnica.com/ai/2026/06/anthropic-says-these-topics-are-too-dangerous-to-let-its-fable-5-model-talk-about/
date: 2026-06-09
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-06-11T06:01:18.840052
---

# Anthropic says these topics are too dangerous to let its Fable 5 model talk about - Ars Technica

# Anthropic’s Fable 5 Model: Capabilities, Safeguards, and Access

## Model release and capabilities
- Anthropic launched Claude Fable 5, its first “Mythos‑class” model, claiming overall performance improvements over the previous Opus line.  
- Fable 5 shares the underlying architecture of the upcoming Mythos 5 but is made publicly available, while Mythos 5 is limited to a small group of vetted cyber‑defenders via Project Glasswing.  
- Benchmark tests show a large jump in cybersecurity performance, with ExploitBench scores rising from 40 % (Opus 4.8) to 78 % (Mythos 5) and 69 % for the Mythos preview.

## Topic‑based safety safeguards
- The model blocks queries about cybersecurity, biology, and chemistry, redirecting such requests to the older Claude Opus 4.8 model and issuing warnings.  
- Safeguards rely on classifiers that detect banned subjects and jailbreak attempts; over 1,000 hours of red‑team testing found no universal jailbreaks.  
- Anthropic acknowledges occasional false positives, estimating they occur in fewer than 5 % of sessions, but deems them acceptable to prevent malicious use.

## Testing results and comparative performance
- Automated jailbreak resistance is markedly stronger than in prior Claude Opus models.  
- Independent testing by the UK AI Security Institute found Mythos preview performance on Capture‑the‑Flag challenges comparable to OpenAI’s GPT‑5.5, indicating the improvement is not unique to a single model.  
- Expanded classifiers now cover all chemistry and biology queries, reflecting concerns that even innocuous prompts could aid high‑risk biological research.

## Access, pricing, and subscription details
- API and enterprise users can use Fable 5 at $10 per million input tokens and $50 per million output tokens, roughly 67‑100 % higher than OpenAI’s GPT‑5.5 pricing.  
- Existing subscription plans include Fable 5 access until 22 June; after that date, users must purchase usage credits.  
- Anthropic plans to reintegrate Fable 5 into standard subscriptions once sufficient capacity is available.

## Trust framework and future expansion
- Anthropic’s Project Glasswing, coordinated with the U.S. government, will gradually admit more cybersecurity professionals.  
- A new trusted‑access program for life‑science organizations will lift biology/chemistry safeguards while retaining cybersecurity protections.  
- The company emphasizes the dual‑use nature of the blocked topics: beneficial for experts but potentially dangerous in the hands of malicious actors.