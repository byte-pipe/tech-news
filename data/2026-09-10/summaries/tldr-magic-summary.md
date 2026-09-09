---
title: Magic
url: https://magic.dev/blog/pretraining
date: 2026-09-10
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-10T07:21:48.629066
---

# Magic

# Summary of Magic: >10x More Efficient Pretraining

## Overview
- The Magic team reports a new pretraining recipe that is more than ten times compute‑efficient than leading open‑weight base models.  
- Using ~50× fewer FLOPs, the model matches DeepSeek V4 Pro Base performance, costing roughly half of GPT‑3’s pretraining compute (~$0.5 M on GB200).  
- Scaling the approach 10× further (~$4 M) yields better perplexity than all publicly available open models.

## Compute Efficiency Gains
- Bits‑per‑byte (bpb) loss is used as the primary efficiency metric; lower values indicate better performance.  
- Compared to DeepSeek V4 Flash/Pro, Kimi K2, and Nemotron 3 Ultra, Magic’s recipe achieves:
  - 29×–48× lower bpb on private code repositories.  
  - 24×–45× lower bpb on held‑out research papers.  
  - Up to 127× lower bpb on held‑out math reasoning tasks.  
- Projected scaling laws suggest that training a model of comparable capability with DeepSeek’s recipe would cost >$100 M, highlighting the economic advantage of Magic’s method.

## Scaling Laws & Figures
- Figure 1 presents pretraining scaling laws (bpb vs. FLOPs) fitted to Magic’s runs, with dashed extensions projecting beyond the largest experiment.  
- The fitted curves demonstrate consistent compute efficiency improvements across all evaluated domains.  
- Figure 2 shows effective‑compute per research area, confirming that the recipe yields higher efficiency in computer science, engineering, math, and physics papers.  
- Figure 3 illustrates effective‑compute multipliers across domains, with values >1 favoring Magic’s recipe and values <1 favoring baseline models.

## Evaluation Methodology
- **Generalization:** Loss measured on held‑out data, including private codebases and recent low‑citation research papers. Duplicate content removed via token similarity thresholds.  
- **Knowledge Gaps:** Held‑out research sets are broken down by subject (e.g., computer science, engineering, math, physics) to pinpoint domain‑specific weaknesses.  
- **Inference Validation:** Log‑probabilities evaluated using both vLLM and SGLang on GB200/GB300 hardware; discrepancies cross‑checked with Fireworks’ in‑house engine.  
- **Parser Independence:** Evaluation data generated with a different parser/OCR than the one used in pretraining to avoid parser‑specific memorization.

## Results Across Domains
- **Private Code:** 29×–48× efficiency gains over leading models.  
- **Research Papers:** 24×–45× gains on general research, with domain‑specific multipliers ranging from 12× (math) to 120× (computer science).  
- **Reasoning Tasks:** Up to 127× lower bpb on held‑out math problems.  
- **Effective‑Compute Multipliers:** Across 167 domains, Magic’s recipe consistently outperforms baselines, especially in software engineering (SWE) and AI R&D tasks.

## Future Directions
- Continue scaling beyond the current 10× run to further reduce compute costs and improve performance.  
- Leverage the efficient pretraining foundation together with agentic reinforcement learning and long‑context capabilities to develop superhuman coding agents and automate AI R&D.  
- Refine data mixing strategies to balance high‑value domains (coding, AI research) against lower‑priority areas (local news, sports, law).  

The Magic team’s findings suggest that algorithmic improvements can dramatically lower the barrier to training large‑scale models, making trillion‑parameter research more accessible without massive hardware investments.