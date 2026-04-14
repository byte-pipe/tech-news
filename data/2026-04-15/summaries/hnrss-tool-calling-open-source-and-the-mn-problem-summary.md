---
title: Tool calling, open source, and the M×N problem
url: https://www.thetypicalset.com/blog/grammar-parser-maintenance-contract
date: 2026-04-09
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-15T06:04:20.361509
---

# Tool calling, open source, and the M×N problem

# Tool calling, open source, and the M×N problem

## Problem statement
- Closed‑source models provide seamless tool calling via an invisible wire format.
- Open models expose the wire format; if an engine does not understand it, output becomes garbled (reasoning tokens in arguments, malformed JSON, missing calls).
- Developers must either wait for support or write their own parsers.

## Supporting a model
- Each model family encodes tool calls differently (e.g., gpt‑oss, DeepSeek, GLM5) with distinct token vocabularies, boundary markers, and argument serialization.
- To return a clean array of JSON tool calls, every inference engine (vLLM, SGLang, TensorRT‑LLM, transformers, etc.) implements a custom parser for each model.
- This creates an **M applications × N models** implementation burden.

## Pace of the problem
- Example: Gemma 4’s non‑standard format caused decoder stripping of reasoning tokens (vLLM #38855) and leakage of reasoning content into arguments (vLLM #39027).
- Llama.cpp had to abandon its generic autoparser and add a dedicated implementation (llama.cpp #21418).
- Training‑time format choices surface later as parser bugs.

## Limitations of generic parsers
- Simple heuristics (“find special tokens, extract JSON”) work for some formats but fail for others (e.g., Harmony’s attribute routing, GLM5’s `<arg_key>/<arg_value>` pairs).
- Wire formats are open‑ended design decisions made at training time; a generic parser cannot anticipate formats that have not yet been created.
- Consequently, generic parsers reduce but do not eliminate the per‑model tail where hard bugs remain (reasoning token leaks, token stripping, end‑of‑generation collisions).

## Missing separation
- Two independent responsibilities:
  1. **Grammar engines** (Outlines, XGrammar, llama.cpp grammar support) need to know where to apply generation constraints: envelope tokens, activation points for structured generation, and exit points.
  2. **Output parsers** in inference engines must reverse‑engineer the raw text into a clean API response.
- Both need the same model‑specific knowledge (boundary tokens, argument serialization, reasoning token behavior) but obtain it by separate reverse‑engineering efforts.
- This results in **N models × M implementations** of identical format knowledge, duplicated across different codebases and release cycles.

## Proposed solution
- Extract the shared format knowledge into a **declarative specification** (configuration) rather than hard‑coded logic.
- The spec would describe:
  - Wire format identifiers
  - Boundary token definitions
  - Argument serialization method
  - Reasoning token handling rules
- Grammar engines and parsers would consume the same spec; updating support for a new model would involve only updating the spec, not modifying multiple engines.

## Author
- Rémi Louf, CEO of dottxt. Follow @remilouf / @dottxtaif for work on structured generation and tool calling.