---
title: Why does AI lie? Hallucinations explained simply - DEV Community
url: https://dev.to/aws/why-does-ai-lie-hallucinations-explained-simply-1c7g
date: 2026-05-08
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-05-12T06:03:08.993535
---

# Why does AI lie? Hallucinations explained simply - DEV Community

# Why does AI lie? Hallucinations explained simply

## The demo: same question, two models
- Asked “What happened at the recent Lyrids meteor shower?” to two Bedrock models.  
- **Nova Micro 1.0**: gave detailed answer with dates, locations, numbers, all stated confidently. Its training cut‑off is 2023, so it fabricated information to fill the gap.  
- **Claude Haiku 4.5**: replied it has no current information (knowledge up to April 2024) and suggested checking astronomy sites. After providing a PDF of a Space.com article, it extracted accurate details.  

## The biography test
- Prompted Nova Micro with “Tell me about Rohini Gaonkar.”  
- Model generated a full academic biography (PhD, university, publications) that was completely false.  
- Haiku recognized its limits and stopped.  
- Both models use the same prediction mechanism; the difference is the presence of guardrails.

## Why this happens: the architecture
- The inference loop is: **Input → Foundation Model → Output**.  
- The model predicts a plausible‑looking answer based on its training data.  
- After the training cut‑off, the model cannot learn new facts; it either says “I don’t know” or fabricates a response.  
- Historically, training rewards fluency, not honesty, so models tend to produce confident but invented answers.  
- Hallucination flavors include:
  1. Fabricated facts (biography).  
  2. Out‑of‑date info presented as current (meteor shower).  
  3. Inconsistent reproduction even with source present.  
  4. Wrong attributions, sycophantic agreement, confident extrapolation.  

## The fix, and where the fix breaks
- Providing context (e.g., a PDF) reduces hallucination but does not eliminate it.  
- Example: Nova Lite was given a document and asked to quote a paragraph; two identical queries returned different wordings, showing non‑deterministic prediction rather than true retrieval.  
- Exact‑word tasks (legal text, medical dosages, contracts) still require verification.

## Three signs you should double‑check
1. **Specific unverifiable details** – names, dates, numbers, URLs in domains you cannot confirm; treat as 50 % chance of error.  
2. **Fluency on fuzzy topics** – confident, detailed answers on niche or recent subjects are suspicious; real expertise includes hedging.  
3. **Citations** – URLs or paper references that look real are often fabricated; always open and verify them.

## Try it yourself
- Builders should view hallucinations as an inherent property, not a bug.  
- Mitigation strategies:
  - **Grounding**: supply the model with reliable context (documents, data).  
  - **Instruction**: prompt the model to admit uncertainty.  
  - **Evaluation**: systematically test outputs against known facts.  

These practices help keep AI outputs useful while recognizing the limits of prediction‑only systems.