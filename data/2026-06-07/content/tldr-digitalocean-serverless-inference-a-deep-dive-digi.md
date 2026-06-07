---
title: 'DigitalOcean Serverless Inference: A Deep Dive | DigitalOcean'
url: https://www.digitalocean.com/blog/serverless-inference-deep-dive
site_name: tldr
content_file: tldr-digitalocean-serverless-inference-a-deep-dive-digi
fetched_at: '2026-06-07T19:33:25.761000'
original_url: https://www.digitalocean.com/blog/serverless-inference-deep-dive
date: '2026-06-07'
description: A deep dive into DigitalOcean Serverless Inference—how we built a scalable, API-first AI inference platform and the architecture powering it.
tags:
- tldr
---

©
 2026 
DigitalOcean, LLC.
Sitemap
.

Dark mode is coming soon.
Engineering

# DigitalOcean Serverless Inference: A Deep Dive

Bysmehta

* Updated:June 3, 2026
* 17 min read
<-
 
Back to blog home

## The Problem: Inference Gets Hard at Scale

If you’ve shipped an AI feature to production, you already know: the hard part isn’t making a model respond to a prompt. The hard part is making it respond more reliably, at scale, across multiple models, without burning through your budget.

The moment real users show up, you’re dealing with GPU resource contention, traffic unpredictability (a single enterprise customer can 10x your request volume overnight), latency-cost tradeoffs that shift constantly, and multi-model orchestration across text, vision, image, video, and audio — each with different API contracts and failure characteristics.

Most teams spend months just getting the infrastructure stable. We built DigitalOcean Serverless Inference so you don’t have to.

## What Serverless Inference Is

DigitalOcean Serverless Inference is a fully managed, API-first inference platform — 30+ foundation models across text, code, vision, image generation, video generation, and speech, all through a single API key, a single base URL, and pay-per-token pricing with no minimum commitments.

The core idea: Serverless Inference separates model consumption from infrastructure management.It automatically scales to handle incoming requests. Because it does not maintain sessions, each request must include the full context needed by the model. You interact with models through an API surface. We handle GPU allocation, scaling, and model lifecycle underneath.

### Single Endpoint, Every Mode

None
https://inference.do-ai.run

Authenticate with a Model Access Key (recommended — scoped to specific models, VPC-restrictable)

### OpenAI and Anthropic Compatible

The API is OpenAI-compatible. If you have existing code that calls OpenAI, switch to DigitalOcean by changing two lines — the base URL and the key:

Python
from openai import OpenAI
import os

client = OpenAI(
 base_url="https://inference.do-ai.run/v1/",
 api_key=os.getenv("MODEL_ACCESS_KEY"),
)
response = client.chat.completions.create(
 model="deepseek-v3.2",
 messages=[{"role": "user", "content": "Explain the CAP theorem."}],
)

We also support Anthropic-compatible patterns through the /v1/messages endpoint, so Claude Code and other agentic workflows work directly through DigitalOcean without vendor lock-in.

### Intelligent Routing, Built-in Tools, and More

Beyond basic inference, the platform includes an Inference Router for automatic multi-model routing, built-in tools for knowledge retrieval, MCP, and web search, prompt caching for cost reduction on repeated contexts, and reasoning for step-by-step thinking traces. We’ll cover each of these in detail later in this post.

### Colocated with Your Cloud

Unlike standalone inference providers, Serverless Inference is part of the DigitalOcean platform. Your inference workloads sit alongside databases, object storage, Kubernetes clusters, and VPCs — all under unified billing and access control. This is a structural advantage where DigitalOcean is unmatched.

## Architecture: How Requests Flow

Here’s what happens under the hood when your application sends a request:

None
Client Request
 → Cloudflare (edge proxying, DDoS protection, TLS)
 → Load Balancer(auth, validation)
 → Traefik (ingress routing on DOKS)
 → Intelligent Inference API (routing, billing)
 → Model Executor Service (provider translation)
 → Model Backend (Ray + vLLM for open-source,
 or provider API for OpenAI/Anthropic)
 → Streaming Response → Client
 → Kafka (billing events, telemetry)

### Load Balancer

Distributes traffic across the inference cluster and serves as the policy enforcement point. Every request is validated against the Model Access Key or DigitalOcean personal access token, with the load balancer resolving tenant identity and confirming the caller is authorized to use the requested model; VPC-bound keys are enforced, rejecting requests originating outside the restricted network. Per-account and per-model rate limits are also enforced via a regional Redis cache to protect platform stability and help prevent single-tenant resource exhaustion. Finally, before reaching any backend, request validation occurs against the model’s contract from the Model Catalog—the centralized source of truth—designed to ensure that requests with unsupported parameters or incorrect endpoint shapes are rejected deterministically with a clear error, preventing the frustrating experience of cryptic provider errors deep in the stack.

### Intelligent Inference API

The customer-facing entry point and policy enforcement layer. Every request passes through this service, where it handles authentication (validating Model Access Keys), request validation against the model’s contract, rate limiting (via Redis), billing metering (token counts dispatched to Kafka), and SSE streaming. It also orchestrates the Inference Router and built-in tool execution. Deployed as a stateless service on DigitalOcean Kubernetes Service (DOKS) with autoscaling.

### Model Executor Service — The Translation Layer

This is one of the most important — and least visible — parts of the platform.

Every model provider has quirks. Anthropic structures tool calls are different from OpenAI. Streaming event formats vary. Some providers support parameters that others silently ignore. Request schemas, error shapes, and response normalization all differ in subtle ways. If you’ve ever tried to build a multi-model application yourself, you’ve felt this pain — it’s a constant stream of provider-specific edge cases that break your code in production.

The Model Executor Service helps solve this by sitting between the Intelligent Inference API and every model backend. It translates a standardized request envelope into whatever provider-native format the backend expects, executes the call, then normalizes the response back into a consistent shape. Provider-specific quirks — streaming differences, parameter mappings, error translations — are absorbed here to prevent leaks to your application.

This is why every model on the platform works identically across the API endpoints (/chat/completions, /responses, and /messages (Anthropic Models Only)), regardless of who built the model or where it runs. You don’t need to know whether the model behind a request is hosted on our GPUs, served by OpenAI, or running on Anthropic’s infrastructure. The translation layer presents a single, consistent API contract for all of them.

### Model Runtime: Ray + vLLM

For DigitalOcean-hosted open-source models, the runtime layer is built on Ray (orchestration and scheduling across NVIDIA H100 GPU nodes) and vLLM (KV cache management, continuous batching, token generation). Ray multiplexes multiple models across shared GPU pools, so you pay for tokens consumed rather than GPU-hours reserved.

### Commercial Model Routing

For commercial models from OpenAI and Anthropic, the Model Executor Service handles the provider translation and forwards to the provider’s API. The response is normalized back through the same pipeline. This means you can call Claude Sonnet and DeepSeek V3.2 from the same application with the same key, the same endpoint, and get back identically structured responses.

### Billing Pipeline

Every request generates a usage event (model ID, token counts, metadata) written to regional Kafka. The billing pipeline consumes these asynchronously — it never sits in the critical request path, so billing latency doesn’t affect inference latency.

## Getting Started: From Zero to Inference

If you’ve used the OpenAI SDK before, you’ll be productive in minutes. Here’s a walkthrough from first API key to streaming responses.

### Step 1: Get Your Model Access Key

In theDigitalOcean Control Panel, clickINFERENCE → Manage → Model Access Keys. Create a key and export it:

Shell
export MODEL_ACCESS_KEY="your-model-access-key-here"

### Step 2: Chat Completions API

The most common endpoint. Send a POST to /v1/chat/completions with a model ID, messages, temperature, and token limit:

Shell
curl -X POST https://inference.do-ai.run/v1/chat/completions \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "llama3.3-70b-instruct",
 "messages": [{"role": "user", "content": "What is the capital of France?"}],
 "temperature": 0.7,
 "max_completion_tokens": 256
 }'

The same request using the Python OpenAI SDK:

Python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
 base_url="https://inference.do-ai.run/v1/",
 api_key=os.getenv("MODEL_ACCESS_KEY"),
)

resp = client.chat.completions.create(
 model="llama3.3-70b-instruct",
 messages=[
 {"role": "system", "content": "You are a helpful assistant."},
 {"role": "user", "content": "Tell me a fun fact about octopuses."}
 ],
)
print(resp.choices[0].message.content)

To switch models, change one parameter — “model”: “llama-4-maverick”. No SDK, endpoint, or auth changes needed.

### Step 3: Responses API

For newer integrations and multi-step tool use, use the Responses API at /v1/responses. It takes a single input field instead of a messages array:

Shell
curl -sS -X POST https://inference.do-ai.run/v1/responses \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "openai-gpt-oss-20b",
 "input": "What is the capital of France?",
 "max_output_tokens": 50,
 "temperature": 0.7,
 "stream": false
 }'

### Step 4: Streaming

For chatbots, code assistants, and interactive tools, set stream: true to receive tokens via Server-Sent Events as they’re generated. Using the same client from Step 2:

Python
stream = client.responses.create(
 model="openai-gpt-oss-20b",
 input="What is the capital of France?",
 max_output_tokens=50,
 temperature=0.7,
 stream = true
)
for chunk in stream:
 if chunk.choices[0].delta.content is not None:
 print(chunk.choices[0].delta.content, end="", flush=True)

### All API Endpoints

API

Type

Endpoint

Description

Models

Sync

/v1/models

List available models

Chat Comlpletions

Sync

/v1/chat/completions

Chat-style prompts (text + VLM)

Responses

Sync

/v1/responses

Multi-step tool use, stateful interactions

Messags

Sync

/v1/messages

Anthropic-compatible (Claude Code, agentic workflows)

Imag Generaton

Sync

/v1/images/generations

Text-to-image, up to 1 megapixel

Text-to-Speech

Sync

/v1/audio/speech

Text-to-speech (binary audio)

Embeddings

Sync

/v1/embeddings

Dense vector representations for search/RAG

Video

Async

/v1/video/generations

Text-to-video (MP4, 480p or 720p)

fl Models

Async

/v1/async-invoke

Image/TTS via fal models

For async video generation, results expire 2 hours after job completion.

## Prompt Caching

The sections above cover the basics of sending requests. Now let’s look at the platform features that can make production inference faster and cheaper — starting with prompt caching.

Prompt caching lets you cache context across requests so repeated prefixes are billed at a lower rate. This is critical for agentic workflows where 80–97% of input tokens repeat across sequential requests.

### Anthropic Models

Use cache_control with type: ephemeral and a ttl of 5m or 1h:

Shell
curl -X POST https://inference.do-ai.run/v1/chat/completions \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "anthropic-claude-4.6-sonnet",
 "messages": [{
 "role": "developer",
 "content": [{
 "type": "text",
 "text": "You are a helpful coding assistant with extensive knowledge of Python and cloud infrastructure.",
 "cache_control": {"type": "ephemeral", "ttl": "1h"}
 }]
 },
 {"role": "user", "content": "Write a Python function to validate email addresses."}],
 "max_completion_tokens": 1024
 }'

The response shows cache_created_input_tokens on the first call; subsequent calls show cache_read_input_tokens at reduced cost.

### OpenAI Models

For prompts with 1,024+ tokens, use prompt_cache_retention set to in_memory or 24h:

JSON
{
 "model": "gpt-4o-mini",
 "prompt_cache_retention": "24h",
 "messages": [...],
 "temperature": 0.2
}

### Open-Source Models

Prompt caching for DigitalOcean-hosted open-source models isnot currently supported. It is available only for Anthropic and OpenAI models at this time. Open-source model caching is on the roadmap as a high-priority investment.

## Reasoning

For models that support it, you can enable step-by-step thinking traces — useful for math, logic, coding, and complex analytical tasks.

Anthropic format— use a reasoning object with effort and optional max_tokens:

Shell
curl -X POST https://inference.do-ai.run/v1/chat/completions \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "anthropic-claude-opus-4.5",
 "messages": [{"role": "user", "content": "What is 27 * 453? Think step by step."}],
 "max_completion_tokens": 1192,
 "reasoning": {"effort": "high", "max_tokens": 1024}
 }'

The response includes reasoning_content (the thinking trace) alongside content (the final answer). If you omit max_tokens, the reasoning budget defaults to a percentage of max_completion_tokens: 20% for low, 50% for medium, 80% for high, 95% for max.

OpenAI format— use reasoning_effort directly (none, low, medium, high, max):

JSON
curl -X POST https://inference.do-ai.run/v1/chat/completions \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "anthropic-claude-4.6-sonnet",
 "messages": [
 {
 "role": "user",
 "content": "What is 27 * 453? Think step by step."
 }
 ],
 "max_completion_tokens": 8192,
 "reasoning_effort": "high"
 }'

## Multimodal Inference

Serverless Inference isn’t text-only. We support vision-language models, image generation, video generation, text-to-speech, and vector embeddings — all through the same API key and base URL.

### Vision-Language Models

VLMs accept text + image inputs (PNG, JPG, JPEG, WEBP as base64 or HTTPS URLs) and return text:

Shell
curl https://inference.do-ai.run/v1/chat/completions \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "nemotron-nano-12b-v2-vl",
 "messages": [{
 "role": "user",
 "content": [
 {"type": "text", "text": "What is shown in this image?"},
 {"type": "image_url", "image_url": {"url": "https://example.com/sample.jpg"}}
 ]
 }],
 "max_tokens": 512
 }'

### Image Generation

Generate images up to 1 megapixel. Always specify n and size:

Shell
curl https://inference.do-ai.run/v1/images/generations \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "stable-diffusion-3.5-large",
 "prompt": "A sunset over mountains",
 "n": 1,
 "size": "1024x1024",
 "quality": "auto",
 "response_format": "b64_json",
 "background": "auto",
 "output_format": "png"
 }'

### Text-to-Video (Asynchronous)

Submit a job, poll for status, download MP4 when complete. Output is 480p (9 seconds) or 720p (5 seconds). Videos expire 2 hours after completion:

Shell
curl -X POST https://inference.do-ai.run/v1/video/generations \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "wan2.2-t2v-a14b",
 "prompt": "A drone shot flying over a lush green valley at golden hour",
 "size": "1280x720",
 "fps": 16
 }'

The request returns a job ID and job status:

{
 "id": "job_abc123",
 "status": "processing"
}

Next, poll the result using the job ID:

curl https://inference.do-ai.run/v1/video/generations/job_abc123 \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY"

You can see the following when the job completes

{
 "created_at": 1777003604,
 "error": null,
 "id": "video_abc",
 "model": "wan2.2-t2v-a14b",
 "object": "video",
 "output": null,
 "status": "completed",
 "x_request_id": null
}

### Text-to-Speech

Shell
curl -sS https://inference.do-ai.run/v1/audio/speech \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "qwen3-tts-voicedesign",
 "input": "Welcome to DigitalOcean.",
 "voice": "alloy",
 "response_format": "mp3",
 "instructions": "Speak naturally."
 }' -o speech.mp3

DigitalOcean is one of the few platforms where all three are available serverlessly through the same API key and endpoint.

## Built-in Tools

Built-in tools are server-side integrations that extend what models can do during inference — without you managing tool orchestration. Add tool definitions to your API request, and the platform handles discovery, execution, and response integration automatically. They work with both the Chat Completions, Responses and Messages APIs.

### Knowledge Base Retrieval (RAG)

Let the model query your private data sources during inference:

Shell
curl -X POST https://inference.do-ai.run/v1/chat/completions \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "openai-gpt-4o",
 "messages": [{"role": "user", "content": "What features does DigitalOcean Inference offer?"}],
 "tools": [{"type": "knowledge_base_retrieval", "knowledge_base_id": "<your-kb-id>"}],
 "max_tokens": 1024
 }'

### Model Context Protocol (MCP)

Connect to remote MCP servers — authenticated or unauthenticated — for live data access:

Shell
curl -X POST https://inference.do-ai.run/v1/chat/completions \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "openai-gpt-4o",
 "messages": [{"role": "user", "content": "Fetch my DigitalOcean account info."}],
 "tools": [{
 "type": "mcp",
 "server_label": "digitalocean",
 "server_url": "https://accounts.mcp.digitalocean.com/mcp",
 "authorization": "Bearer $DIGITALOCEAN_API_TOKEN",
 "allowed_tools": ["account-get-information"]
 }],
 "tool_choice": "required",
 "max_tokens": 512
 }'

### Web Search

Give models access to real-time web content:

Shell
curl -X POST https://inference.do-ai.run/v1/responses \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "openai-gpt-4o",
 "input": "What are the latest DigitalOcean Droplet pricing changes?",
 "tools": [{"type": "web_search", "max_uses": 3, "max_results": 5}],
 "max_output_tokens": 1024
 }'

### Agentic Workflows (Claude Code)

We offer full Anthropic tool-use compatibility through /v1/messages. Set ANTHROPIC_BASE_URL tohttps://inference.do-ai.run/v1/messagesto run Claude Code and other agentic workflows on DigitalOcean:

Shell
curl https://inference.do-ai.run/v1/messages \
 -H "x-api-key: $MODEL_ACCESS_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "content-type: application/json" \
 -d '{
 "model": "anthropic-claude-4.6-sonnet",
 "max_tokens": 4096,
 "tools": [{
 "name": "read_file",
 "description": "Read a file from the local filesystem.",
 "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}
 }],
 "messages": [{"role": "user", "content": "Refactor the authentication logic in src/auth.ts."}]
 }'

### Pricing

(current as of May 2026)

Knowledge base retrieval and MCP incur no additional charges beyond standard per-token inference costs. Web search is $10 per 1,000 requests.

## Inference Router

We mentioned the Inference Router earlier as a key differentiator. Here’s how it works in practice.

The Inference Router classifies each incoming request against your configured tasks, then selects the best model from a pool. Each task has up to 3 models and a selection policy:Cost Efficiency(cheapest by token cost),Speed Optimization(fastest by TTFT),Manual Ranking(your specified order), orOptimal(DigitalOcean’s benchmarking, for pre-configured tasks).

Using it is a one-line change — prefix the router name with router: in the model field:

Shell
curl -X POST https://inference.do-ai.run/v1/chat/completions \
 -H "Authorization: Bearer $MODEL_ACCESS_KEY" \
 -H "Content-Type: application/json" \
 -d '{
 "model": "router:my-support-router",
 "messages": [{"role": "user", "content": "What are your support hours?"}],
 "stream": true
 }'

The response’s model field tells you which model was selected, and the x-model-router-selected-route header shows which task matched. If no task matches, fallback models handle the request. If a model is unavailable, the router fails over automatically.

For a complete walkthrough of building a real support bot with the Inference Router, seeInference Routing: Matching Models to Tasks, Not Just Requests.

## Production Operations

The production lifecycle is anchored by the seamless handoff betweenServerless Inference (SI)andDedicated Inference (DI), where the SI layer orchestrates calls to vLLM endpoints that serve as the high-performanceInference Engine.

To maintain stability during high-concurrency spikes, vLLM’s internal scheduler managesrequest queuingand batching, ensuring compute resources are saturated without being overwhelmed. This infrastructure is underpinned by a robust reliability framework.

High Service Level Objectives (SLOs) are enforced viaauto-pod healing- capability that automatically detects and recovers from node failures to ensure the system remains resilient and available at scale.

With the APIs and platform features covered, here’s how the system behaves in production.

### Observability

Every request generates telemetry automatically — no instrumentation required. View metrics in the Control Panel underINFERENCE → Serverless Inference → Analyze:

Category

Metics

Relabilty

Error rates (4xx/5xx), success rates, RPM

Latency

Time to first token (TTFT), end-to-end

Cost

Per-invocation, per-model spend

Usage

Token consumption by model

Rat Limiting

Throttled request/token counts

Multimodal

Image count, audio duration, cost by modality

### Failure Recovery

* Model failures:Ray reschedules on a healthy GPU node; clients should retry.
* Rate limits:HTTP 429 — implement exponential backoff.
* Provider failures:Standardized error responses for commercial model outages.
* Stream drops:Partial response delivered; retry the full request.
* Router failover:Automatic reroute to fallback models when primary is unavailable.

### Content Safety

Input guardrails block policy-violating prompts before inference begins. Output guardrails withhold violating content after generation.

## Economics

### Pay-Per-Token

A dedicated GPU costs the same at 5% utilization or 95%. Serverless Inference pools GPU capacity across all customers — you pay only for tokens consumed, not GPU-hours reserved.

### Pricing (per 1M tokens)

Model

DigitalOcean (Input/Output)

Competitor Range

Llama 4 Maverick

$0.250 / $0.800

Bedrock $0.24/$0.97

DeepSeek V3.2

$0.300 / $1.000

Bedrock $0.62/$1.85

Qwen3.5 397B

$0.550 / $3.500

Together AI $0.60/$3.60

SD 3.5 Large (image)

$0.065/image

Bedrock $0.08

Wan 2.2 T2V (720p video)

$0.31/video

TogetherAI $0.66

Qwen3 TTS

$0.020/1K tokens

Replicate: $0.02/1K tokens
 
ElevenLabs Multilingual V2 for $0.1/1K tokens

*Pricing reflects publicly listed rates as of May 29 2026. Competitor pricing is subject to change.

*Off-peak discounts of 5–10% apply during 10 PM – 4 AM PT on eligible open-source models.

## Security and Data Privacy

* Zero data retention:Synchronous outputs are never stored. Async video outputs expire after 2 hours. Inputs are never stored for training or logging.
* VPC supportwith model access keys restrictable to VPC networks.
* Key scopingto specific models and batch inference.
* Tiered billing:Spend caps by tier. Tier 1, Tier 2 (new users) gets open-source models only; Tier 3+ unlocks commercial models from OpenAI and Anthropic.

## What We Learned

Building this platform taught us things that no architecture diagram captures:

* Serverless Inference traffic is unpredictable.A single agentic integration can 10x volume overnight. A 200K-token request consumes more GPU memory than 1,000 short ones. Traditional autoscaling heuristics don’t apply.
* GPU utilization beats raw hardware.10 nodes at 80% utilization outperform 20 at 30%. Scheduling intelligence (Ray) and serving optimization at Inference engine (like vLLM) yield more effective capacity than adding hardware.
* Cold starts are infrastructure problems.Dominated by weight pre-staging, memory availability, and scheduling speed — not just model loading time.
* Streaming shapes everything.It affects load balancer timeouts, proxy design, billing metering, and error handling. It’s not a feature — it’s an architectural constraint.
* Developers want reliability, not infrastructure.The most consistent feedback we hear: make the API work, give clear errors, make billing transparent. The best inference infrastructure is the kind you never think about.

## What’s Next

* Open-source prompt caching— caching is live for Anthropic/OpenAI today; we plan to extend caching to open-source models.
* Expanded model catalog— we plan to extend caching models to include next-gen DeepSeek, Qwen, Llama families, plus speech-to-text.
* Multi-region— we plan to add EU regions to support General Data Protection Regulation (GDPR)-compliant workloads.
* Enhanced observability— we plan to add cache hit rates, latency histograms, SI logs.
* Router enhancements— we’re exploring router support for popular coding agents.

The above reflects our current plans and product direction, and is subject to change without notice. It is provided for informational purposes only and is not a commitment to deliver any material, feature, or functionality.

## Get Started

1. Create an accountatcloud.digitalocean.com
2. Create a Model Access KeyunderINFERENCE → Manage → Model Access Keys
3. Make your first requestusing the examples above
4. Explore the Model Playgroundto test models interactively

### About the author

smehta
Author
See author profile
See author profile

Share

* Engineering

### Start building today

From GPU-powered inference and Kubernetes to managed databases and storage, get everything you need to build, scale, and deploy intelligent applications.
Sign up

## Related Articles

Engineering

### The Inference Tax: How Prefix-Aware Routing Eliminates the Hidden Cost of LLMs at Scale

Piyush Srivastava
* June 1, 2026
* 13 min read

Read more

Engineering

### How We Built DigitalOcean Inference Router

Adil Hafeez
* May 20, 2026
* 14 min read

Read more

Engineering

### Your Model Doesn't Matter. Your Infrastructure Does.

adagonese
* May 13, 2026
* 7 min read

Read more