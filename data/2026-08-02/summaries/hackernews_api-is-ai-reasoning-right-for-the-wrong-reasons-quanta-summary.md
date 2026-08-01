---
title: Is AI Reasoning Right for the Wrong Reasons? | Quanta Magazine
url: https://www.quantamagazine.org/is-ai-reasoning-right-for-the-wrong-reasons-20260731/
date: 2026-08-01
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-02T06:01:37.133833
---

# Is AI Reasoning Right for the Wrong Reasons? | Quanta Magazine

# Is AI Reasoning Right for the Wrong Reasons?

## Introduction
- The author expresses bewilderment at the rapid swings in how AI “reasoning” is judged, from skepticism in 2024 to headline‑making successes in 2025‑2026 (e.g., OpenAI’s general‑purpose reasoning model solving a famous math problem, LRMs winning IMO medals, and collaborations with Terence Tao).  
- At the same time, research teams (Apple, Santa Fe Institute) have critiqued these models as producing “illusions of thinking” or relying on surface‑level shortcuts.

## Expert Insight from Melanie Mitchell
1. **Performance works:** LRMs achieve higher accuracy on reasoning benchmarks than standard LLMs.  
2. **Generated text isn’t faithful:** The chain‑of‑thought (CoT) text that LRMs emit does not reliably reflect the model’s internal computation.  
3. **Much of the text is unnecessary:** Large portions of the CoT can be removed without degrading the model’s answers.

## Chains of Thought: Origin and Growing Doubts
- **Origin:** CoT emerged in 2022 as a prompting hack (“think step‑by‑step”) and was later baked into LRMs (e.g., OpenAI’s o1) which generate and re‑feed these reasoning traces.  
- **Research challenges:**  
  - Substituting correct traces with incorrect or irrelevant ones often leaves performance unchanged (Kambhampati 2025).  
  - Training on correct traces still yields occasional invalid traces even when the final answer is correct.  
  - “Meaningless filler tokens” such as strings of dots can replace human‑readable CoT without harming performance (NYU 2024).  
  - Merrill (TTIC) states there is no guarantee the CoT is meaningful; Izmailov (Anthropic/NYU) doubts reinforcement learning even incentivizes faithful traces.

## Causal Impact of Thinking Steps
- A 2025 study by Northeastern University and UC Berkeley on open‑source LRMs found that **30 %–60 %** of the generated “thinking steps” have **minimal causal impact** on the final answer.  
- Removing half of these steps barely affects benchmark math performance.  
- Authors warn against assuming CoT prompts are directly linked to the model’s output.

## Overall Tension
- While LRMs demonstrate impressive problem‑solving feats, the evidence suggests that the visible chain‑of‑thought may be a superficial artifact rather than a genuine window into reasoning.  
- This creates a paradox where AI reasoning appears both effective and, at the same time, potentially “BS”—a core theme the article explores.