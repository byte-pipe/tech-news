---
title: A Key-Position Confound in no-cot-bench (and implications for interpreting looped transformers) — LessWrong
url: https://www.lesswrong.com/posts/ehF4kej38fkhb5cT3/a-key-position-confound-in-no-cot-bench-and-implications-for
date: 2026-10-02
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-02T16:36:30.163662
---

# A Key-Position Confound in no-cot-bench (and implications for interpreting looped transformers) — LessWrong

**A Key-Position Confound in no-cot-bench**

A recent benchmark for no-COT (no-co-Transferential reasoning) demonstrates that a looped transformer, Astra, performs exceptionally well on it. However, a confound in the no-COT benchmark design is identified that affects the reasoning depth of Astra models. This confound refers to the positioning of the prompt's "key" variable, which is assumed to be given at the beginning of the prompt.

**Impact on Benchmark Performance**

Correcting for this confound decreases GPT-6.1 Sol's no-COT reasoning depth by 16%, with the effect likely increasing as the dependent depth (sequence length) of the task increases. This indicates that the original benchmark might not accurately represent the true performance of no-COT reasoning tasks.

**Key Contributions**

A proposed solution addresses this confund by creating three key-related designs for the no-COT benchmark:

1. **Paired key-first/key-last**: Adapt existing serial state-tracking tasks and add a key-last variant for each task.
2. **Key-last**: Use state-dependent branching to prevent the model from precomputing key-space mappings before experiencing the key.
3. **Variants for two tasks**: Develop specific variants for each task to test the effectiveness of the proposed solutions.

**Conclusion**

The identified confound in the no-COT benchmark design, specifically at the "key" position, has a significant impact on model performance. The proposed solutions aim to mitigate this confound and provide a more accurate representation of no-COT reasoning tasks.