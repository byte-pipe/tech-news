---
title: Coding Models Are Doing Too Much | wh
url: https://nrehiew.github.io/blog/minimal_editing/
date: 2026-04-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-23T09:45:34.508620
---

# Coding Models Are Doing Too Much | wh

# Coding Models Are Doing Too Much | wh – Summary

## Overview
- AI coding assistants (Cursor, GitHub Copilot, Claude Code, Codex, etc.) are increasingly used for bug fixing.  
- A common issue observed is **over‑editing**: the model rewrites large portions of code even when only a minimal change is needed.  
- Over‑editing hampers code review, increases cognitive load, and can degrade codebase quality without being caught by tests.

## Over‑Editing Defined
- **Over‑editing** occurs when a model’s output is functionally correct but structurally diverges from the original more than the minimal fix requires.  
- Example: fixing an off‑by‑one error (`range(len(x) - 1)` → `range(len(x))`) should be a one‑line change, yet GPT‑5.4 rewrote the entire function, adding checks, conversions, and new plotting logic.

## Measuring Over‑Editing
- **Dataset**: 400 problems from BigCodeBench were programmatically corrupted (e.g., operator flips, boolean swaps) to create minimal, well‑defined fixes.  
- **Metrics**:
  - *Token‑level Levenshtein Distance*: computed on Python tokens, normalized by total token count, to capture the amount of code changed.  
  - *Relative Patch Score* \(S(M) = D_{\text{model}} - D_{\text{true}}\): compares model edit distance to the true minimal edit; values near zero indicate faithful editing.  
  - *Added Cognitive Complexity*: measures increase in understandability difficulty; the ideal increase is zero for minimal fixes.

## Experimental Findings
- Both reasoning‑enhanced and non‑reasoning models exhibit over‑editing, even among the latest frontier models.  
- Sample results (higher Pass@1 is better; lower Levenshtein and Cognitive Complexity are better):

| Model | Pass@1 | Normalized Levenshtein | Added Cognitive Complexity |
|-------|--------|------------------------|-----------------------------|
| GPT‑5.4 (Reasoning) | 0.723 | 0.395 | 2.313 |
| Claude Opus 4.6 (Reasoning) | 0.912 | 0.060 | 0.200 |
| Gemini 3.1 Pro (Reasoning) | 0.858 | 0.145 | 0.501 |
| GLM 5 High (Reasoning) | 0.859 | 0.099 | 0.320 |
| Qwen 3.6 Plus (Reasoning) | 0.858 | 0.145 | 0.048 |
| Kimi 2.5 (Reasoning) | 0.835 | 0.151 | 0.770 |
| DeepSeek R1 (Reasoning) | 0.820 | 0.232 | 0.673 |
| GPT‑5.4 (Non‑Reasoning) | 0.770 | 0.327 | 1.563 |
| Claude Opus 4.6 (Non‑Reasoning) | 0.900 | 0.079 | 0.313 |
| ... | ... | ... | ... |

- Even top‑performing models (e.g., Claude Opus 4.6) achieve low over‑editing scores, while others (GPT‑5.4) show substantial unnecessary changes.

## Implications
- Over‑editing is a **brown‑field failure**: it does not affect test outcomes but makes code reviews harder and can silently degrade maintainability.  
- Relying solely on test passing as a quality metric is insufficient; editors must also be evaluated on edit minimality and cognitive impact.  
- Future work should focus on training or prompting strategies that encourage **faithful editing**, reducing unnecessary rewrites while preserving correctness.