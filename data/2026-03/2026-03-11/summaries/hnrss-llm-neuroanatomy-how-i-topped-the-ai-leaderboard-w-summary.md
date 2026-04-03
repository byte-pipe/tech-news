---
title: LLM Neuroanatomy: How I Topped the AI Leaderboard Without Changing a Single Weight | David Noel Ng
url: https://dnhkng.github.io/posts/rys/
date: 2026-03-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-11T13:14:01.222770
---

# LLM Neuroanatomy: How I Topped the AI Leaderboard Without Changing a Single Weight | David Noel Ng

# LLM Neuroanatomy: How I Topped the AI Leaderboard Without Changing a Single Weight

## Introduction
- In mid‑2024 the HuggingFace Open LLM Leaderboard featured thousands of models competing on six benchmarks (IFEval, BBH, MATH Lvl 5, GPQA, MuSR, MMLU‑PRO).  
- My entry, **dnhkng/RYS‑XLarge**, reached #1 without any training, weight merging, or gradient updates.  
- The trick was to duplicate a specific block of seven middle layers in a 72‑billion‑parameter model and splice them back in, leaving every weight unchanged.  

## Clue #1 – Base64 Chatting
- I discovered that a 2023 LLM could decode a Base64‑encoded question, reason about it, and then re‑encode its answer in Base64.  
- Example:  
  - Prompt: “What is the capital of France? Answer in Base64!” → encoded string sent to the model.  
  - Model reply: “VGhlIGNhcGl0YWwg...”, which decodes to “The capital of France is Paris.”  
- This behavior suggests:  
  - Early transformer layers act as **translators**, converting any input format (English, Python, Mandarin, Base64) into an abstract internal representation.  
  - Late layers act as **re‑translators**, turning that abstract representation back into the required output format.  
  - The middle layers are hypothesized to perform **pure abstract reasoning** independent of the input encoding.  

## Clue #2 – The Goliath Anomaly
- In November 2023 a user released **Goliath‑120B**, a model built by interleaving layers from two fine‑tuned Llama‑2 70B models and feeding later‑layer outputs back into earlier‑layer inputs.  
- The layer schedule alternated blocks from the two source models (e.g., Xwin layers 0‑16, then Euryale layers 8‑24, etc.), creating cross‑connections that had never been seen during training.  
- Despite the unconventional wiring, the model functioned, showing that transformer layers are **more interchangeable** than expected and can handle out‑of‑order hidden states.  
- This experiment reinforced the idea that internal representations are **homogeneous** enough for layers to process inputs from non‑sequential sources.  

## Emerging Hypothesis
- Transformers possess a functional anatomy:  
  1. **Early layers** translate raw tokens into a language‑agnostic abstract space.  
  2. **Middle layers** serve as a reasoning cortex, operating in a universal internal language that tolerates architectural rearrangements.  
  3. **Late layers** translate the abstract reasoning back into the desired output format.  
- The success of both the Base64 experiment and Goliath suggests that the “processing units” for input and output may be smaller than the 16‑layer blocks used in Goliath, pointing to a finer‑grained modularity within the model.  

## How the Leaderboard Win Was Achieved
- Identified a block of seven middle layers that appeared to be part of the reasoning cortex.  
- Duplicated this block, inserting the copies back into the model without altering any weights.  
- The resulting model gained additional reasoning capacity, propelling it to the top of the leaderboard across all six benchmarks.  

## Takeaway
- Transformer architectures exhibit a surprising degree of **layer‑level flexibility** and **internal modularity**.  
- Simple structural modifications—such as duplicating middle layers—can dramatically improve performance without any additional training, revealing a new avenue for model scaling and interpretability research.