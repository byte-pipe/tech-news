---
title: Introducing GPT-5.3-Codex-Spark | OpenAI
url: https://openai.com/index/introducing-gpt-5-3-codex-spark/
date: 2026-02-13
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-14T06:03:35.278112
---

# Introducing GPT-5.3-Codex-Spark | OpenAI

# Introducing GPT‑5.3‑Codex‑Spark

This article from OpenAI announces the research preview release of GPT‑5.3‑Codex‑Spark, a new, ultra-fast model designed for real-time coding. It is a smaller version of GPT‑5.3‑Codex and marks the first step in a partnership with Cerebras, leveraging their Wafer Scale Engine 3 for high-speed inference.

## Key Points:

* **Ultra-fast coding:** Codex-Spark is optimized for near-instant responses, delivering over 1000 tokens per second.
* **Real-time interaction:** It is specifically designed for interactive coding tasks, allowing for immediate edits, logic reshaping, and interface refinement.
* **Cerebras partnership:** The model runs on Cerebras' hardware, enabling low-latency serving.
* **Long-running tasks:** While new for real-time coding, Codex-Spark builds on the strengths of OpenAI's latest frontier models in handling long-running, autonomous tasks.
* **Context window:** At launch, it has a 128k context window and is text-only.
* **Rate limits:** During the research preview, Codex-Spark has its own rate limits separate from standard usage.
* **Performance:** Benchmarks show Codex-Spark performing strongly on software engineering tasks, completing them faster than GPT‑5.3‑Codex.
* **Latency improvements:** End-to-end latency improvements have been implemented across all models, reducing overhead and time-to-first-token.
* **Availability:** It is rolling out today as a research preview for ChatGPT Pro users in the Codex app, CLI, and VS Code extension, with API access for select partners to expand integration.
* **Future development:** OpenAI plans to introduce more capabilities over time, including larger models, longer context lengths, and multimodal input.
* **Safety:** Codex-Spark includes the same safety training as mainline models and has been evaluated for cybersecurity and biology capabilities, with no indication of reaching high capability thresholds in these areas.
* **Future vision:** Codex will evolve with two complementary modes: longer-horizon reasoning and real-time collaboration, eventually blending these modes for a more natural user experience.

## Speed and intelligence
Codex-Spark prioritizes speed for interactive work, allowing real-time collaboration and rapid iteration with near-instant responses. It maintains a lightweight default working style with minimal targeted edits and no automatic testing.

## Coding
GPT‑5.3‑Codex‑Spark demonstrates strong performance in software engineering tasks, completing them significantly faster than GPT‑5.3‑Codex.

## Latency improvements for all models
Significant improvements have been made to the request-response pipeline, including streamlined streaming, rewritten inference stack, and optimized session initialization, resulting in reduced overhead and faster time-to-first-token.

## Powered by Cerebras
The model leverages Cerebras' Wafer Scale Engine 3 for high-speed inference, providing a low-latency serving tier and seamless integration with OpenAI's production serving stack.

## Availability & details
Codex-Spark is available as a research preview for ChatGPT Pro users and a limited number of design partners via the API, with broader access planned in the coming weeks.

## What’s next
The development aims towards a future where Codex offers both long-horizon reasoning and real-time collaboration modes, seamlessly integrated for a more natural and efficient coding experience.
