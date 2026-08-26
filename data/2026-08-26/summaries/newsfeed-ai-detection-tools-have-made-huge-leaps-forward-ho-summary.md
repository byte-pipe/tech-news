---
title: AI-detection tools have made huge leaps forward — how good are they? | Nature
url: https://www.nature.com/articles/d41586-026-02569-3
date: 2026-08-25
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-08-26T12:52:53.871169
---

# AI-detection tools have made huge leaps forward — how good are they? | Nature

# AI‑detection tools have made huge leaps forward — how good are they? | Nature  

## Overview  
- After years of poor performance, commercial AI‑detection tools such as **Pangram** and **GPTZero** now claim near‑perfect accuracy in distinguishing AI‑generated from human‑written text.  
- The tools are being adopted by scientific journals, conferences, pre‑print servers, universities, and even blogging platforms to enforce disclosure policies and curb cheating.  

## How the tools work  
- Early detectors relied on statistical cues (perplexity, burstiness) and often mis‑flagged human writing.  
- Newer models train on millions of human texts and AI‑generated “mirrors” of those texts, using machine‑learning classifiers that learn subtle, model‑specific patterns.  
- The resulting systems are black‑box classifiers that achieve extremely low false‑positive rates (≈0.004 %–0.02 % on large test sets).  

## Reported performance  

| Tool | Claimed false‑positive rate | Independent test results |
|------|-----------------------------|--------------------------|
| Pangram | 0.0041 % (English) | Zero false positives on 495 human texts (Epoch AI) |
| GPTZero | <1 % (internal), marketed 0.08 % | Zero false positives on Epoch AI test; 0 % in Karpinska’s study |
| Earlier detectors | High false‑positive rates | Frequently mis‑identified human text |

- Both tools excel at flagging *pure* AI‑generated passages (basic prompts).  
- When AI is prompted to imitate a specific author, about 8 % of passages can evade detection.  
- “Humanizer” tools that rewrite AI output increase both false‑negative and false‑positive rates.  

## Adoption in the research ecosystem  

- **AACR** uses Pangram to screen peer‑review reports; a reviewer admitted using an LLM after being caught.  
- **NeurIPS** rejected 18 % of submissions after Pangram screening.  
- **arXiv** offers a mirror site (alphaXiv) that displays Pangram verdicts for preprints.  
- **University of Chicago** applies the tool to student coursework.  
- **Substack** integrates Pangram so readers can see AI‑authorship labels on posts.  

## Limitations and ongoing challenges  

- The tools prioritize low false positives, which leads to higher false negatives (some AI‑generated text passes as human).  
- Rapid updates of large language models (e.g., OpenAI’s o1) can temporarily reduce detection accuracy until detectors are retrained.  
- Detecting blended human‑AI text remains difficult; current models are less reliable when AI output is heavily edited.  

## The AI‑detection “arms race”  

- Companies continuously update their models (GPTZero released 23 updates in a year; Pangram launched “Pangram 4” in July).  
- Researchers warn that as detection improves, AI‑generation and “humanizer” techniques will also evolve, requiring ongoing monitoring and norm‑setting.  

## Key take‑aways  

- Modern AI‑detection tools can reliably identify purely AI‑generated text with near‑zero false positives.  
- They are already embedded in scholarly publishing, conference review, pre‑print screening, and academic integrity workflows.  
- False negatives and mixed human‑AI writing remain problem areas, so detections should be treated as initial flags, not definitive judgments.  
- The field is in a rapid feedback loop: new LLMs → updated detectors → new evasion techniques → further detector upgrades.