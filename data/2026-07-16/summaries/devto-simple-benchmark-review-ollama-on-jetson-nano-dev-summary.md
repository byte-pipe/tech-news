---
title: Simple Benchmark Review: Ollama on Jetson Nano - DEV Community
url: https://dev.to/annavi11arrea1/simple-benchmark-review-ollama-on-jetson-nano-5gee
date: 2026-07-12
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-07-16T03:39:50.192080
---

# Simple Benchmark Review: Ollama on Jetson Nano - DEV Community

# Simple Benchmark Review: Ollama on Jetson Nano – Summary

## Purpose and Context
- The author wanted a free, local AI app on a Jetson Nano to generate flashcards and quizzes from personal text.
- Benchmarking was needed to determine which LLM model and quantization level runs best on the Nano without crashing.
- A swap file was created to mitigate RAM limitations, and a quiz based on the OSI model was used as the test set (10 questions).

## Testing Approach
- Each model was run with several quantization formats (e.g., q2_K, q4_K_M, q5_K_M, q8_0).
- Accuracy was measured by the proportion of correctly answered quiz questions.
- Models that would not fit in the Nano’s GPU memory were omitted from testing.

## Results Overview
- **qwen2.5:3b-instruct** achieved 100 % accuracy across all tested quantizations (q4_K_M, q5_K_M, q8_0).
- **qwen3.5:2b** produced empty outputs (0 % accuracy) for both q4_K_M and q8_0.
- **llama3.2:3b-instruct** ranged from 40 % (q2_K) to 90 % (q4_K_M, q5_K_M, q8_0).
- **mistral:7b-instruct** varied from 80 % (q2_K, q5_K_M) to 100 % (q4_K_M).

## Key Takeaways
- Heavy quantization can degrade model quality, but some models retain full accuracy even at lower precision.
- For the author’s specific quiz‑generation use case, **qwen2.5:3b-instruct** is the clear winner.
- The benchmark is a high‑level, limited test (10 questions) and does not cover all possible use cases.
- The author plans to replace llama3.2:3b‑instruct with qwen2.5:3b‑instruct in their application.

## Open Questions
- How do other Nano users employ Ollama, and what benchmarks do they observe?
- Request for peer review to validate the methodology and results.