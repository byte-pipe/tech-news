---
title: Darkbloom — Private AI Inference on Apple Silicon | Eigen Labs
url: https://darkbloom.dev
site_name: hnrss
content_file: hnrss-darkbloom-private-ai-inference-on-apple-silicon-ei
fetched_at: '2026-04-16T11:58:58.426131'
original_url: https://darkbloom.dev
author: Eigen Labs
date: '2026-04-16'
description: Darkbloom is a decentralized inference network that runs on idle Apple Silicon machines. Every node is hardware-verified and every prompt is end-to-end encrypted. OpenAI-compatible API. 50% cheaper than centralized alternatives.
tags:
- hackernews
- hnrss
---

Eigen Labs Research

# Private inference on idle Macs

We present Darkbloom, a decentralized inference network. AI compute today flows through three layers of markup — GPU manufacturers to hyperscalers to API providers to end users. Meanwhile,over 100 million Apple Silicon machinessit idle for most of each day. We built a network that connects them directly to demand. Operators cannot observe inference data. The API isOpenAI-compatible. Our measurements showup to 70% lower costscompared to centralized alternatives. Operators retain95% of revenue.

Use Darkbloom ↗

Start Earning ↗

Read the Paper ↗

User / App

encrypted

Coordinator

routes

Mac Studio

✓ verified

MacBook Pro

✓ verified

Mac Mini

✓ verified

response

01 — What this enables

For users

### Inference at half the cost

Idle hardware has near-zero marginal cost. That saving passes through to price. OpenAI-compatible API for chat, image generation, and speech-to-text. Every request is end-to-end encrypted.

Open Console ↗

For hardware owners

### Earn USD from idle Apple Silicon

Your Mac already has the hardware. Operators keep 100% of inference revenue. Electricity cost on Apple Silicon runs $0.01–0.03 per hour depending on workload. The rest is profit.

Start Earning ↗

02 — Motivation

The AI compute market has three layers of margin.

 NVIDIA sells GPUs to hyperscalers. AWS, Google, Azure, and CoreWeave mark them up and rent capacity to AI companies. AI companies mark them up again and charge end users per token. Each layer takes a cut. End users pay multiples of what the silicon actually costs to run.


Current supply chain

→

→

API providers

→

End users

 This concentrates both wealth and access. A small number of companies control the supply. Everyone else rents.

 Meanwhile, Apple has shipped over 100 million machines with serious ML hardware. Unified memory architectures. 273 to 819 GB/s memory bandwidth. Neural Engines. Machines capable of running 235-billion-parameter models. Most sit idle 18 or more hours a day. Their owners earn nothing from this compute.

That is not a technology problem. It is a marketplace problem.

The pattern is familiar. Airbnb connected idle rooms to travelers. Uber connected idle cars to riders. Rooftop solar turned idle rooftops into energy assets. In each case, distributed idle capacity undercut centralized incumbents on price because the marginal cost was near zero.

 Darkbloom does this for AI compute. Idle Macs serve inference. Users pay less because there is no hyperscaler in the middle. Operators earn from hardware they already own. Unlike those other networks, the operator cannot see the user's data.


100M+
Apple Silicon machines shipped since 2020

3x+
markup from silicon to end-user API price

18hrs
average daily idle time per machine

100%
of revenue goes to the hardware owner

03 — The Challenge

Other decentralized compute networks connect buyers and sellers. That is the easy part.

 The hard part is trust. You are sending prompts to a machine you do not own, operated by someone you have never met. Your company's internal data. Your users' conversations. Your competitive advantage, running on hardware in someone else's house.

 No enterprise will do this without guarantees stronger than a terms-of-service document.

Without verifiable privacy, decentralized inference does not work.

04 — Our Approach

## Access path elimination

We eliminate every software path through which an operator could observe inference data. Four independent layers, each independently verifiable.

Encryption

### Encrypted end-to-end

Requests are encrypted on the user's device before transmission. The coordinator routes ciphertext. Only the target node's hardware-bound key can decrypt.

Hardware

### Hardware-verified

Each node holds a key generated inside Apple's tamper-resistant secure hardware. The attestation chain traces back to Apple's root certificate authority.

Runtime

### Hardened runtime

The inference process is locked at the OS level. Debugger attachment is blocked. Memory inspection is blocked. The operator cannot extract data from a running process.

Output

### Traceable to hardware

Every response is signed by the specific machine that produced it. The full attestation chain is published. Anyone can verify it independently.

E2E Encryption

encrypted before it leaves your device

OS Integrity

SIP enforced · signed system volume · binary self-hash

Memory Isolation

Hypervisor.framework · Stage 2 page tables

Hardened Process

debugger blocked · no shell access

Your inference data

prompts · responses · model state

↑ operator is here — every path inward is eliminated

### The operator runs your inference. They cannot see your data.

Prompts are encrypted before they leave your machine. The coordinator routes traffic it cannot read. The provider decrypts inside a hardened process it cannot inspect. The attestation chain is public.

Read the paper ↗

05 — Implementation

## OpenAI-compatible API

Change the base URL. Everything else works. Streaming, function calling, all existing SDKs.

python

from
 openai
import
 OpenAI

client = OpenAI(
 base_url=
"https://api.darkbloom.dev/v1"
,
 api_key=
"your-api-key"

)

response = client.chat.completions.create(
 model=
"mlx-community/gemma-4-26b-a4b-it-8bit"
,
 messages=[{
"role"
:
"user"
,
"content"
:
"Hello!"
}],
 stream=
True

)

for
 chunk
in
 response:

print
(chunk.choices[0].delta.content, end=
""
)

Streaming
 — SSE, OpenAI format

Image generation
 — FLUX.2 on Metal

Speech-to-text
 — Cohere Transcribe

Large MoE
 — up to 239B params

06 — Results

## Cost comparison

Idle hardware has near-zero marginal cost, so the savings pass through. No subscriptions or minimums. Per-token pricing compared against OpenRouter equivalents.

Model
Input
Output
OpenRouter
Savings

Gemma 4 26B
4B active, fast multimodal MoE
$0.03
$0.20
$0.40
50%

Qwen3.5 27B
Dense, frontier reasoning
$0.10
$0.78
$1.56
50%

Qwen3.5 122B MoE
10B active, best quality
$0.13
$1.04
$2.08
50%

MiniMax M2.5 239B
11B active, SOTA coding
$0.06
$0.50
$1.00
50%

Prices per million tokens

#### Image Generation

$0.0015
per image
Together.ai: $0.003

#### Speech-to-Text

$0.001
per audio minute
AssemblyAI: $0.002

#### Platform Fee

0%
operators keep 100%
transparent

07 — Operator Economics

## Operator economics

Operators contribute idle Apple Silicon and earn USD. 100% of inference revenue goes to the operator. The only variable cost is electricity.

100%
revenue goes to you

~90%
profit margin

CLI

Mac App

#### Install via Terminal

Downloads the provider binary and configures a launchd service.

terminal
$
curl -fsSL https://api.darkbloom.dev/install.sh | bash

No dependencies
Auto-updates
Runs as launchd service

#### Native macOS Menu Bar AppIn Development

One-click install. Runs in your menu bar. Currently in active development — use the CLI for now.

Coming soon

Apple Silicon only
macOS 14+
Includes CLI + backend

### Earnings estimate

Select hardware to model projected operator earnings.

Machine

Chip

Memory

Hours per day:
18

Text
--
$0
$0 / year
Revenue
$0
Electricity
-$0

Image
--
$0
$0 / year
Revenue
$0
Electricity
-$0

Estimates only. Actual results depend on network demand and model popularity. Assumes you own the Mac.

### Read the research paper

Architecture specification, threat model, security analysis, and economic model for hardware-verified private inference on distributed Apple Silicon.

Download PDF ↗

Model Catalog

## Available models

Curated for quality. Only models worth paying for.

Gemma 4 26B
Google's latest — fast multimodal MoE, 4B active params
text

Qwen3.5 27B
Dense, frontier-quality reasoning (Claude Opus distilled)
text

Qwen3.5 122B MoE
ⓘ
10B active — best quality per token
text

MiniMax M2.5 239B
ⓘ
SOTA coding, 11B active, 100 tok/s on Mac Studio
text

Cohere Transcribe
2B conformer — best-in-class speech-to-text
audio
