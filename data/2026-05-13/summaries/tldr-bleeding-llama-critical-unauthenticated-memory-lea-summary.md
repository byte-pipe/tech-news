---
title: Bleeding Llama: Critical Unauthenticated Memory Leak in Ollama | Cyera Research
url: https://www.cyera.com/research/bleeding-llama-critical-unauthenticated-memory-leak-in-ollama
date: 2026-05-13
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-13T06:01:12.470023
---

# Bleeding Llama: Critical Unauthenticated Memory Leak in Ollama | Cyera Research

# Bleeding Llama: Critical Unauthenticated Memory Leak in Ollama

## TL;DR
- Critical vulnerability (CVE‑2026‑7482, CVSS 9.1) allows unauthenticated attackers to read the entire Ollama process memory.  
- Potentially impacts ~300 000 servers worldwide.  
- Leaked memory includes user prompts, system prompts, and environment variables.

## What Is Ollama?
- Open‑source platform for running large language models locally, avoiding cloud APIs.  
- Supports models such as Llama, Mistral, etc.  
- Popularity: ~170 k GitHub stars, >100 M Docker Hub pulls, widely adopted in enterprises.

## Model Creation in Ollama
- Two main APIs:  
  - **/api/pull** – downloads a pre‑built model from the registry.  
  - **/api/create** – builds a custom model from uploaded files, allowing custom system prompts, quantization, etc.  
- Files are uploaded via **/api/blobs/sha256:[digest]**; the SHA‑256 digest identifies the file content.  
- **/api/create** receives a JSON body referencing the uploaded blobs.

## GGUF (GPT‑Generated Unified Format)
- File format for storing LLMs efficiently.  
- Contains a header with version, tensor count, and metadata (e.g., `general.file_type`).  
- Supports numeric types F16 (float‑16) and F32 (float‑32).  
- Tensors are described by name, dimensions, data type, and offset to raw data.

## Quantization
- Reduces tensor precision to shrink memory and speed up inference.  
- F32 → F16 halves memory usage but loses some decimal precision.  
- F16 → F32 is lossless.

## Where the Bug Lives
- Ollama is written in Go but uses the `unsafe` package for low‑level memory operations.  
- Vulnerable path: **/api/create** handler (`server.CreateHandler`).  
- After request parsing, Ollama calls `convertModelFromFiles`, which eventually invokes `WriteTo` for each tensor during quantization.

## The Faulty `WriteTo` Logic
- `WriteTo` always converts source data to F32 first.  
- Calls `ggml.ConvertToF32` with three arguments: original buffer, source type, and `q.from`.  
- An out‑of‑bounds write occurs because `q.from` can be set beyond the actual buffer length, enabling arbitrary memory reads.  
- Unsafe pointer arithmetic bypasses Go’s memory safety, creating an unauthenticated memory leak.

## Impact
- An attacker can send a crafted **/api/create** request, trigger the out‑of‑bounds read, and dump the entire process memory.  
- Dumped data includes:  
  - All user‑submitted prompts and system prompts.  
  - Environment variables (potentially API keys, credentials, etc.).  
- No authentication is required; the endpoint is exposed by default on typical Ollama installations.

## Scope
- Estimated ~300 000 publicly reachable Ollama instances based on Docker Hub download statistics and GitHub activity.  
- Any deployment that enables the **/api/create** endpoint with file‑upload support is vulnerable.

## Mitigation & Recommendations
- Disable the **/api/create** endpoint or restrict it behind authentication and network firewalls.  
- Apply the forthcoming patched version that validates `q.from` and removes unsafe pointer usage.  
- Monitor logs for unusual **/api/create** requests with large or unexpected `quantize` parameters.  
- Rotate any credentials that may have been exposed in environment variables.

## Disclosure
- Coordinated disclosure with Ollama maintainers; a patch is expected within 30 days.