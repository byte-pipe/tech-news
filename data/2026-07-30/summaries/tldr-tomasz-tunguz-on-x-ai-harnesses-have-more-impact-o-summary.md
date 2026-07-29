---
title: "Tomasz Tunguz on X: \"AI harnesses have more impact on performance than the models. https://t.co/n9O2SiSURZ\" / X"
url: https://x.com/ttunguz/status/2082158740107866459
date: 2026-07-30
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-30T06:43:40.796548
---

# Tomasz Tunguz on X: "AI harnesses have more impact on performance than the models. https://t.co/n9O2SiSURZ" / X

# Summary of Tomasz Tunguz’s X post on AI harnesses  

## Main claim  
- AI harnesses – the surrounding infrastructure, prompting, retrieval, memory, and feedback mechanisms – have a greater impact on performance than the underlying language models themselves.  

## Supporting insights from the thread  

- **Kishen Patel** references Alex Zhang’s research showing that language‑model harnesses act as compositional generalizers: similarly structured tasks are treated as isomorphic, improving performance across tasks.  
- **Scott Taylor** explains that selecting context is only half the job; the harness must also learn from deployment feedback. At memco_ai, frozen models achieved a 2.6× improvement over static RAG when reusable memory from deployment corrections was incorporated, enabling continual learning that transfers across models.  
- **Oz Khan** stresses that a deterministic, open‑code harness with a clear “spine” outperforms staying inside closed‑source sandboxes such as Codex or Claude’s environment.  

## Implications  

- Prioritizing harness design (prompt engineering, retrieval, memory, feedback loops) can yield larger performance gains than merely scaling model size.  
- Effective harnesses enable compositional generalization, continual learning from real‑world interactions, and reproducible results.  

## Community reaction  

- The post attracted 36.6 K views and generated a lively discussion with dozens of replies, reflecting strong interest in the role of harnesses in AI system performance.