---
title: 2x, not 10x: coding with LLMs in 2026
url: https://obryant.dev/p/2x-not-10x/
date: 2026-08-01
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-01T03:10:19.912543
---

# 2x, not 10x: coding with LLMs in 2026

# 2x, not 10x: coding with LLMs in 2026

## Main observations
- Over the past six months I’ve realized that even if LLMs were magical, I’d still question their value beyond simple tasks like writing unit tests.  
- LLMs are now reliable enough to be used in automated feedback loops, which drove their rapid adoption in 2026.  
- This reliability yields roughly a 2× productivity boost, but further model improvements are unlikely to produce another order‑of‑magnitude gain.

## Staircase hypothesis
- Think of LLM usefulness like climbing stairs: being tall enough to take one step is essential; being tall enough to skip two or three steps adds only marginal benefit.  
- Once LLMs can reliably handle “make a button that does X” and verify the result, additional performance gains have diminishing returns.

## How I use LLMs today
- **Draft generation**: I ask the model to produce a rough implementation, then iterate heavily on structure and readability.  
- **Verification loop**: I let the LLM test the button (or similar) and tell me whether the acceptance criteria are met.  
- **Documentation**: I give the explicit instruction “Never write READMEs, docstrings, or comments. I will write those myself later,” which dramatically improves the quality of generated code.

## Remaining limitations
- LLMs still struggle with higher‑level design questions such as:
  - “Is there a more maintainable way to structure this code?”  
  - “Does this documentation contain the right information and omit the unnecessary?”  
- Even with line‑level sloppiness, I consistently underestimate the time needed to refine the draft; a “working implementation” now feels like only 20 % complete rather than 80 %.

## Outlook and industry direction
- Expectation that future model upgrades will solve documentation and maintainability issues is uncertain; the staircase analogy suggests new capabilities may not translate into 10× gains.  
- Most productivity improvements will likely come from tooling, workflows, and sandboxed environments that align with current model strengths.  
- I’ve moved from using LLMs as a search‑engine replacement to interactive chat and declarative specifications, with sandboxing to avoid constant permission prompts.  
- “Vibe coding” (generating code without fully understanding it) is an experimental area I’m exploring outside work; its long‑term viability remains unclear, though specialized testing and tooling might eventually make black‑box LLM code safe for critical systems.

## Conclusion
- For now, I rely on handcrafted READMEs and manual refinement of LLM‑generated drafts.  
- The foreseeable productivity boost remains around 2×; achieving a 10× leap will probably require re‑architecting development processes around the existing capabilities of LLMs rather than waiting for purely model‑driven breakthroughs.