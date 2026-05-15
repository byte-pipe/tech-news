---
title: "What's in a GGUF, besides the weights - and what's still missing? - NobodyWho"
url: https://nobodywho.ooo/posts/whats-in-a-gguf/
date: 2026-05-15
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-16T06:01:42.100247
---

# What's in a GGUF, besides the weights - and what's still missing? - NobodyWho

# What's in a GGUF, besides the weights - and what's still missing?

## Overview
- GGUF is llama.cpp’s single‑file format for language models, consolidating what would otherwise be multiple JSON, OCI layers, etc.
- The format stores not only weights but also metadata needed for inference, making model handling more ergonomic.

## Chat Templates
- Conversational models rely on chat templates that define how prompts and responses are formatted.
- Templates are written in Jinja2 and stored under the `tokenizer.chat_template` key in GGUF metadata; a model may contain several variants (e.g., with or without tool‑calling support).
- Different projects use different Jinja2 implementations (Python’s jinja2, llama.cpp’s custom version, minijinja in Rust), leading to performance variations, though templating is not the main bottleneck.

## Special Tokens
- Special tokens carry semantic meaning beyond plain text and guide generation control.
- Examples from Gemma‑4:
  - `<eos>` (ID 1): end‑of‑sequence, stops generation.
  - `<bos>` (ID 2): beginning‑of‑sequence, prepended to inputs.
  - `<|tool_call>` / `<tool_call|>` (IDs 46, 47): delimit tool calls.
  - `<|turn>` / `<turn|>` (IDs 105, 106): delimit conversational turns.

## Sampler Configuration
- Models output a probability distribution over next tokens; sampling transforms this distribution into a concrete token.
- Researchers often publish recommended sampler settings, which users copy manually.
- GGUF now includes a field to embed the full sampler chain directly in the model file, eliminating the need for external configuration files.

## Sampler Chain Sequence
- The order of sampling steps (e.g., temperature, top‑k, nucleus) significantly affects output quality.
- GGUF defines `general.sampling.sequence` to explicitly specify this order.
- Many models omit the field and rely on llama.cpp’s default implicit ordering, which still works but is less transparent.

## What’s Still Missing?

### Tool‑Calling Formats
- Inference engines currently hard‑code parsers for each model’s tool‑call syntax (e.g., Qwen3, Qwen3.5, Gemma‑4).
- A standardized grammar in GGUF would allow generic parser generation and reduce per‑model implementation effort.
- NobodyWho generates a constrained grammar per tool to ensure type‑safe calls, especially important for very small models.

### Think Tokens
- HuggingFace repositories have started adding a `think_token` field to separate “thinking” sections of generated text.
- Downstream GGUF conversions often omit this field; adding it would improve handling of internal reasoning output.