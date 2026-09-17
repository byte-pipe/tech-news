---
title: Astra uses some of its no-CoT capability in practice — LessWrong
url: https://www.lesswrong.com/posts/kaoeXZkWhNELmgbKg/astra-uses-some-of-its-no-cot-capability-in-practice
date: 2026-09-18
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-18T05:28:39.573479
---

# Astra uses some of its no-CoT capability in practice — LessWrong

# Astra uses some of its no‑CoT capability in practice — LessWrong

## Overview
- Astra achieves markedly higher scores on no‑CoT benchmarks (e.g., Neel Nanda’s nocot‑bench) than earlier OpenAI models.  
- This post investigates how much of that capability Astra actually employs during inference, focusing on the low‑effort reasoning setting (`reasoning_effort=low`).

## Main Findings
- **Shorter CoTs:** When `reasoning_effort=low`, Astra’s chain‑of‑thought (CoT) outputs contain far fewer tokens than those of other OpenAI models (Luna, Terra, Sol).  
- **Internal Reasoning:** On a representative “chain” task, Astra’s token counts align closely with minimal baseline solutions that list only intermediate numeric values, suggesting it performs the three rule types (halving, parity, threshold) in a single forward pass without verbalizing each step.  
- **Performance Limits:** Astra reliably solves chain tasks up to 6 steps correctly without any explicit CoT, matching or exceeding the no‑CoT performance of other models.  
- **Partial Exploitation:** Despite strong no‑CoT ability, Astra does not fully leverage it on the examined task under low‑effort settings, likely to avoid error amplification in multi‑step reasoning.

## Detailed Analysis

### 1. CoT Length Comparison
- Tested five task types (2 serial, 2 parallel, 1 search) at maximum difficulty, using only the answer output and `reasoning_effort=low`.  
- Token‑usage plot shows Astra consistently using the fewest reasoning tokens; other models produce longer CoTs, often verbalizing rule applications.

### 2. Case Study: Chain Task
- Example 3‑step chain task: start with 14, apply a series of conditional halving/doubling/subtractions.  
- Baseline minimal solution: “14, 7, 14, 7” (7–10 tokens).  
- Astra’s runs cluster 4–7 tokens above the lower baseline, indicating it likely outputs only the intermediate numbers plus minimal framing.  
- Other models’ token counts are higher, implying they articulate the rule‑application process.

### 3. No‑CoT Accuracy Table
| Model | Steps Solved Correctly (no‑CoT) |
|-------|---------------------------------|
| Astra | up to 6 steps (consistent) |
| Others | lower or comparable, with more variance |

## Implications
- High no‑CoT capability can be risky: operating near the capability boundary may increase error rates, especially when errors compound across steps.  
- Astra appears to balance internal reasoning with token‑efficiency, opting for concise internal computation rather than full externalization of reasoning.

## Conclusion
- Astra’s superior no‑CoT scores do not automatically translate into maximal exploitation of that ability in practice, at least under low‑effort settings.  
- Understanding how future models externalize reasoning can be aided by the token‑count analysis demonstrated here.

## Appendix A: Example Prompts (one per task type)
- **Chain (answer: 20)** – Prompt asks for final number after a long sequence of conditional arithmetic steps, requesting only “Answer: [ANSWER]”.  
- **Arithmetic (answer: 147682)** – Prompt presents a complex Python expression to evaluate, again requesting only the final numeric answer.  
- **Modes (answer: 1556)** – Prompt provides a list of arithmetic expressions and asks for the most common resulting value.  
- *(Two additional task‑type prompts omitted for brevity.)*