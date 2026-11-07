---
title: "Anthropic's AI acceleration is probably real — LessWrong"
url: https://www.lesswrong.com/posts/QgcgoMz7mviHL6Esr/anthropic-s-ai-acceleration-is-probably-real
date: 2026-11-08
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:03:47.459691
---

# Anthropic's AI acceleration is probably real — LessWrong

# Summary of “Anthropic’s AI acceleration is probably real — LessWrong”

## Is the acceleration real?
- METR researchers spent three months inside Anthropic and concluded that model capabilities grew about **2× faster** from Oct 2025‑Oct 2026 than from Mar 2024‑Oct 2025.  
- Public data (Epoch’s Capability Index) can reproduce most of this finding:
  1. Looking only at Anthropic’s public models shows a **1.42×** speed‑up after Oct 2025.  
  2. Re‑fitting the public scores with METR’s older frequentist method raises the estimate to **1.64×**.  
  3. Comparing METR’s internal AECI fits to the same models yields **1.76×**.  
  4. Adding Anthropic’s private models pushes the figure to the reported **1.91×**.  
- The first two steps rely solely on publicly available information, so the headline acceleration does not depend on trusting Anthropic’s internal data.  
- Distinguishing a genuine trend break from a one‑time jump requires Anthropic’s private model scores; the Opus 5.5 system card favored a one‑time jump, while METR’s full data favor a trend break.

## Is the acceleration because of AI?
- METR attributes roughly **80 %** of the speed‑up to AI‑driven acceleration of AI research itself.  
- Two independent triangulations support this:
  1. **Labor‑uplift surveys**: Slack polls of Anthropic staff report a **12×** productivity boost with the latest model. Converting this uplift via the power‑law relation used by Anthropic gives an overall R&D speed‑up of about **1.6×**, matching METR’s AI‑attributable factor.  
  2. **Greenblatt’s AI‑progress model**: A 7× labor uplift (well below the reported 12×) predicts a **1.61×** overall progress acceleration when accounting for diminishing returns and compute scaling, again close to METR’s estimate.  
- The convergence of informal staff surveys and formal structural models makes it plausible that AI is the primary driver of the observed acceleration.

## Will the acceleration continue?
- The author admits uncertainty: **“who the fuck knows?”** – no solid evidence is presented to predict future trends.

## Methodological notes and caveats
- METR’s report is heavily redacted; most of the analysis is unavailable to the public.  
- The public replication relies on Epoch’s Capability Index (ECI) and on re‑applying METR’s older statistical fitting method.  
- The distinction between a **trend break** and a **one‑time jump** hinges on Anthropic’s internal model data, which cannot be independently verified.  
- Staff‑reported uplift surveys are informal and may lack rigor, but their alignment with independent models adds credibility.  

## Overall takeaway
- Public evidence corroborates METR’s claim that Anthropic’s AI capabilities accelerated dramatically after Oct 2025.  
- The bulk of this acceleration is plausibly explained by AI‑driven productivity gains, consistent with both internal surveys and external progress models.  
- Future continuation of the acceleration remains highly uncertain.