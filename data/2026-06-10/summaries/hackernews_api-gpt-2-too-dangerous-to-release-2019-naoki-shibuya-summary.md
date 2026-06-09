---
title: GPT-2: Too Dangerous To Release (2019) – Naoki Shibuya
url: https://naokishibuya.github.io/blog/2022-12-30-gpt-2-2019/
date: 2026-06-10
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-10T07:44:07.709220
---

# GPT-2: Too Dangerous To Release (2019) – Naoki Shibuya

# Summary of “GPT‑2: Too Dangerous To Release (2019) – Naoki Shibuya”

## 1 The Difference: GPT‑1 vs GPT‑2
- GPT‑1 demonstrated that a large, unsupervised pre‑training phase can enable zero‑shot task transfer; fine‑tuning only adds a final task‑specific adjustment.  
- GPT‑2 is a direct scale‑up of GPT‑1: same Transformer decoder architecture, but with far more parameters and a vastly larger, more diverse training corpus.  
- GPT‑2’s largest model contains **1.5 billion parameters** (≈10× GPT‑1) and was trained on **40 GB of web text**, yielding state‑of‑the‑art results on language modeling, reading comprehension, QA, and summarization.  

## 2 GPT‑2: 1.5B Release
- The paper describes four GPT‑2 model sizes; the biggest uses 48 decoder blocks with a model dimension of 1600.  
- Initially OpenAI withheld the 1.5 B model, citing concerns about malicious use, and released only a much smaller version for research.  
- After nine months, OpenAI released the full 1.5 B model, code, and weights, stating the release would help the community develop responsible publication norms.  
- Findings from the nine‑month observation period:  
  1. Human readers often find GPT‑2 outputs convincing.  
  2. The model can be fine‑tuned for harmful purposes.  
  3. Detecting GPT‑2‑generated text is difficult (≈95 % detection rate by RoBERTa, still imperfect).  
  4. No strong evidence of large‑scale misuse had emerged at that time.  
  5. Standards are needed for studying and mitigating bias.  

## 3 GPT‑2 vs ChatGPT
- By December 2022, ChatGPT demonstrated far stronger performance, suggesting GPT‑2’s perceived danger was limited in hindsight.  
- Lessons from GPT‑2 informed safety measures in ChatGPT, such as preventing impersonation.  
- New misuse scenarios (e.g., students using ChatGPT for assignments) are harder to block, and detection tools for academic cheating remain an ongoing challenge.  

## 4 References
- GPT‑1: *Generative Pre‑Trained Transformer* (2018)  
- GPT‑2: *Better Language Models and Their Implications* (paper, code, OpenAI)  
- ChatGPT: *Optimizing Language Models for Dialogue* (OpenAI)