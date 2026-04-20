---
title: Alibaba's new open source Qwen3.5-Medium models offer Sonnet 4.5 performance on local computers | VentureBeat
url: https://venturebeat.com/technology/alibabas-new-open-source-qwen3-5-medium-models-offer-sonnet-4-5-performance
site_name: hnrss
content_file: hnrss-alibabas-new-open-source-qwen35-medium-models-offe
fetched_at: '2026-03-01T10:15:57.082429'
original_url: https://venturebeat.com/technology/alibabas-new-open-source-qwen3-5-medium-models-offer-sonnet-4-5-performance
date: '2026-02-28'
published_date: 2026-02-25T22:39-05:00
description: This leap is made possible by near-lossless accuracy under 4-bit weight and KV cache quantization, allowing developers to process massive datasets without server-grade infrastructure.
tags:
- hackernews
- hnrss
---

All Posts
Featured
Carl Franzen

 February 26, 2026


Credit: VentureBeat made with Google Gemini 3 Pro Image

Alibaba's now famed Qwen AI development team has done it again: a little more than a day ago, they released theQwen3.5 Medium Model seriesconsisting of four new large language models (LLMs) with support for agentic tool calling, three of which are available for commercial usage by enterprises and indie developers under the standard open source Apache 2.0 license:

* Qwen3.5-35B-A3B
* Qwen3.5-122B-A10B
* Qwen3.5-27B

Developers can download them now onHugging FaceandModelScope. A fourth model, Qwen3.5-Flash, appears to be proprietary and only available through theAlibaba Cloud Model Studio API, but still offers a strong advantage in cost compared to other models in the West (see pricing comparison table below).

But the big twist with the open source models is that they offer comparably high performance on third-party benchmark tests to similarly-sized proprietary models from major U.S. startups like OpenAI or Anthropic, actually beating OpenAI's GPT-5-mini and Anthropic's Claude Sonnet 4.5 — the latter model which wasjust released five months ago.

And, the Qwen teamsaysit has engineered these models to remain highly accurate even when "quantized," a process that reduces their footprint further by reducing the numbers by which the model's settings are stored from many values to far fewer.

Crucially, this release brings "frontier-level" context windows to the desktop PC. The flagship Qwen3.5-35B-A3B can now exceed a 1 million token context length on consumer-grade GPUs with 32GB of VRAM. While not something everyone has access to, this is far less compute than many other comparably-performant options.

This leap is made possible by near-lossless accuracy under 4-bit weight and KV cache quantization, allowing developers to process massive datasets without server-grade infrastructure.

### Technology: Delta force

At the heart of Qwen 3.5's performance is a sophisticated hybrid architecture. While many models rely solely on standard Transformer blocks, Qwen 3.5 integrates Gated Delta Networks combined with a sparse Mixture-of-Experts (MoE) system.The technical specifications for the Qwen3.5-35B-A3B reveal a highly efficient design:

* Parameter Efficiency: While the model houses 35 billion parameters in total, it only activates3 billionfor any given token.
* Expert Diversity: The MoE layer utilizes 256 experts, with 8 routed experts and 1 shared expert helping to maintain performance while slashing inference latency.
* Near-Lossless Quantization: The series maintains high accuracy even when compressed to 4-bit weights, significantly reducing the memory footprint for local deployment.
* Base Model Release: In a move to support the research community, Alibaba has open-sourced theQwen3.5-35B-A3B-Basemodel alongside the instruct-tuned versions.

### Product: Intelligence that 'thinks' first

Qwen 3.5 introduces a native "Thinking Mode" as its default state. Before providing a final answer, the model generates an internal reasoning chain—delimited by<think>tags—to work through complex logic.The product lineup is tailored for varying hardware environments:

* Qwen3.5-27B:Optimized for high efficiency, supporting a context length of over 800K tokens.
* Qwen3.5-Flash:The production-grade hosted version, featuring a default 1 million token context length and built-in official tools.
* Qwen3.5-122B-A10B:Designed for server-grade GPUs (80GB VRAM), this model supports 1M+ context lengths while narrowing the gap with the world's largest frontier models.

Benchmark results validate this architectural shift. The 35B-A3B model notably surpasses much larger predecessors, such as Qwen3-235B, as well as the aforementioned proprietary GPT-5 mini and Sonnet 4.5 in categories including knowledge (MMMLU) and visual reasoning (MMMU-Pro).

Alibaba Qwen3.5 Medium models benchmark comparison chart. Credit: Alibaba

### Pricing and API integration

For those not hosting their own weights, Alibaba Cloud Model Studio provides a competitive API for Qwen3.5-Flash.

* Input: $0.1 per 1M tokens
* Output: $0.4 per 1M tokens
* Cache Creation: $0.125 per 1M tokens
* Cache Read: $0.01 per 1M tokens

The API also features a granular Tool Calling pricing model, with Web Search at $10 per 1,000 calls and Code Interpreter currently offered for a limited time at no cost.

This makes Qwen3.5-Flash among the most affordable to run over API among all the major LLMs in the world. See a table comparing them below:

Model

Input

Output

Total Cost

Source

Qwen 3 Turbo

$0.05

$0.20

$0.25

Alibaba Cloud

Qwen3.5-Flash

$0.10

$0.40

$0.50

Alibaba Cloud

deepseek-chat (V3.2-Exp)

$0.28

$0.42

$0.70

DeepSeek

deepseek-reasoner (V3.2-Exp)

$0.28

$0.42

$0.70

DeepSeek

Grok 4.1 Fast (reasoning)

$0.20

$0.50

$0.70

xAI

Grok 4.1 Fast (non-reasoning)

$0.20

$0.50

$0.70

xAI

MiniMax M2.5

$0.15

$1.20

$1.35

MiniMax

MiniMax M2.5-Lightning

$0.30

$2.40

$2.70

MiniMax

Gemini 3 Flash Preview

$0.50

$3.00

$3.50

Google

Kimi-k2.5

$0.60

$3.00

$3.60

Moonshot

GLM-5

$1.00

$3.20

$4.20

Z.ai

ERNIE 5.0

$0.85

$3.40

$4.25

Baidu

Claude Haiku 4.5

$1.00

$5.00

$6.00

Anthropic

Qwen3-Max (2026-01-23)

$1.20

$6.00

$7.20

Alibaba Cloud

Gemini 3 Pro (≤200K)

$2.00

$12.00

$14.00

Google

GPT-5.2

$1.75

$14.00

$15.75

OpenAI

Claude Sonnet 4.5

$3.00

$15.00

$18.00

Anthropic

Gemini 3 Pro (>200K)

$4.00

$18.00

$22.00

Google

Claude Opus 4.6

$5.00

$25.00

$30.00

Anthropic

GPT-5.2 Pro

$21.00

$168.00

$189.00

OpenAI

### What it means for enterprise technical leaders and decision-makers

With the launch of the Qwen3.5 Medium Models, the rapid iteration and fine-tuning once reserved for well-funded labs is now accessible for on-premise development at many non-technical firms, effectively decoupling sophisticated AI from massive capital expenditure.

Across the organization, this architecture transforms how data is handled and secured. The ability to ingest massive document repositories or hour-scale videos locally allows for deep institutional analysis without the privacy risks of third-party APIs.

By running these specialized "Mixture-of-Experts" models within a private firewall, organizations can maintain sovereign control over their data while utilizing native "thinking" modes and official tool-calling capabilities to build more reliable, autonomous agents.

Early adopters on Hugging Face have specifically lauded the model’s ability to "narrow the gap" in agentic scenarios where previously only the largest closed models could compete.

This shift toward architectural efficiency over raw scale ensures that AI integration remains cost-conscious, secure, and agile enough to keep pace with evolving operational needs.

## More
