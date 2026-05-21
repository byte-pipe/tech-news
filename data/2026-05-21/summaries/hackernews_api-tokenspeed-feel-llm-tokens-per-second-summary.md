---
title: tokenspeed — feel LLM tokens-per-second
url: https://mikeveerman.github.io/tokenspeed/
date: 2026-05-18
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-05-21T12:14:44.371002
---

# tokenspeed — feel LLM tokens-per-second

## Tokens Per Second (TPS) Benchmark for Local-LLM Models

This benchmark compares the efficiency of local-LLM models in generating text at different rates. The results are presented in terms of tokens per second.

### Modes and Rates

The benchmark includes four modes:

* Code (syntax-highlighted pseudo-code)
* Text (lorem ipsum prose for chatting or answering)
* Think (dim-italic reasoning sentences with code)
* Agent (alternating tool calls and code generation)

Four rates are tested starting from 30 tokens per second, incrementing by 5 tokens per second until reaching 800 tokens per second.

### Tokenization and Processing

The difference in token count between modes is striking and intentional. This discrepancy arises because no single vendor-specific encoder is used to tokenize the input; instead, an approximation based on BPE-style tokenization is employed.

## How Tokens Per Second Are Determined

This approximation takes into account:

1. Short words (often one token)
2. Longer identifiers (split into chunks)
3. Punctuation and operators (count as single tokens)

Code generation tends to produce more dense text, resulting in the same token count feeling different due to varying content types.

### Language Characteristics

The average 30 tokens per second corresponds approximately to about 23 words per second in English prose. This difference is expected across various language types because of their natural grammatical structures.

* The benchmark serves as a tool to expose this gap between perceived and actual text generation efficiency.
* It highlights the importance of accurately modeling tokenization and processing for effective local-LLM models.