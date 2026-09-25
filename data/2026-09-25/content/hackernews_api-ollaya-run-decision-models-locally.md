---
title: Ollaya — Run decision models locally
url: https://ollaya.dev/
site_name: hackernews_api
content_file: hackernews_api-ollaya-run-decision-models-locally
fetched_at: '2026-09-25T21:59:45.172727'
original_url: https://ollaya.dev/
author: Ardakilic
date: '2026-09-25'
description: Ollaya downloads and serves open decision models on your own machine. Typed, calibrated answers in milliseconds — private and open source.
tags:
- hackernews
- trending
---

# Run decision models locally.

Ask typed questions about any text or JSON and get calibrated answers in milliseconds. Private, open source, on your own hardware.

Download
Browse models 
ollaya · zsh
$
ollaya
 run laya 
--preset
 triage \
"I was charged twice this month and want a refund."
Answers returned by the model
Question
Answer
Probability
intent
refund
1.00
is_urgent
no
0.87
frustration
1.59 / 3
 clearly annoyed
0.36
refund_requested
yes
0.88
churn_risk
no
0.89
$
Real output: routed to 
laya:en
, answered in 8.9 ms on an RTX 4090.

## Fast

Decisions in milliseconds.

A decision model answers in a single forward pass, with no token-by-token generation. On your own GPU, a five-question request to Laya takes about 10 ms, end to end through the HTTP API.

8–10ms

Laya on Ollaya

RTX 4090, five questions, end to end

236–276ms

TypeSafe Jev

Hosted API, median request

Every model, one scale 
· median latency, lower is better
* laya:multilingual8.1 ms
* laya:en9.6 ms
* gliclass14.7 ms
* nli20.4 ms
* decider:0.8b155 ms
* decider:2b190 ms
* TypeSafe Jevhosted API236–276 ms
0
100
200
300 ms

Ollaya: median of a five-question request through the HTTP API on an NVIDIA RTX 4090 (laya in fp16, the others in fp32). Jev: median request latency of the hosted API in third-party benchmarks (AbdelStark/jev-benchmarks,nibzard/decision-model-benchmark), which includes the network. Setups differ, so read it as an order-of-magnitude comparison.

## Drop-in compatible

Speaks TypeSafe's API.

Ollaya serves/v1/systemoneand/v1/modelswith TypeSafe's request and response shapes. The official TypeSafe Python SDK 0.7.1 works unchanged against a local server.

Request

# Point the TypeSafe SDK at Ollaya

export
 
TYPESAFE_BASE_URL
=
http://localhost:11435

export
 
TYPESAFE_API_KEY
=
local 
# any value works

export
 
TYPESAFE_DEFAULT_MODEL
=
laya

# …or call the compatible endpoint directly

curl
 http://localhost:11435/v1/systemone 
-d
 
'
{

 
"model"
:
 
"laya"
,

 
"state"
:
 
"Can I get an invoice for last month?"
,

 
"questions"
:
 
{

 
"intent"
:
 
{

 
"type"
:
 
"choice"
,

 
"instructions"
:
 
"What does the customer want?"
,

 
"criteria"
:
 
{

 
"invoice"
:
 
"Needs an invoice or receipt"
,

 
"refund"
:
 
"Wants money back"
,

 
"other"
:
 
"Anything else"

 
}

 
}

 
}

 
}
'

Response

{

 
"model"
:
 
"laya:en"
,

 
"answers"
:
 
{

 
"intent"
:
 
{

 
"type"
:
 
"choice"
,

 
"choice"
:
 
"invoice"
,

 
"confidence"
:
 
0.9547
,

 
"probabilities"
:
 
{

 
"invoice"
:
 
0.9698
,

 
"refund"
:
 
0.0172
,

 
"other"
:
 
0.013

 
}

 
}

 
}
,

 
"usage"
:
 
{

 
"input_tokens"
:
 
43
,

 
"output_tokens"
:
 
0

 
}

}

TypeSafe compatibility guide

## Open models

Open weights, ready to pull.

Start with Laya from Convai Innovations: an English model, a 100+ language model, a model fine-tuned for typed decisions, and a router that picks for you.

* layaOpen decision models from Convai Innovations. Typed, calibrated answers to choice, score and yes/no questions in a single forward pass, in English and 100+ languages.322m · 421m
* deciderDecoder decision models by Mapika on Qwen3.5: the answer is read from option-letter logits in one forward pass. The most accurate open decision model Ollaya ships.0.75b · 1.9b
* nliZero-shot classifiers by Moritz Laurer: every option becomes a hypothesis scored for entailment. The most accurate encoder model on typed decisions in our tests.396m · 435m
* gliclassInstruction-following zero-shot classifier by Knowledgator: all options of a question are scored in one pass, so cost barely grows with the number of options.439m
Browse all models 

More open decision models are planned: von, GGUF LLM-based decision models via llama.cpp.

## Your data stays yours

Private by default.

Tickets, emails and user messages are often the most sensitive data you have. With Ollaya they are scored where they already live.

* ### LocalRuns on your machine with ONNX Runtime, on the CPU or an NVIDIA GPU. The server listens on 127.0.0.1 by default.
* ### Open weightsWeights come from their authors’ Hugging Face repositories, pinned to a commit and checked against sha256. Ollaya never re-hosts them, and the runtime is Apache-2.0.
* ### No per-token feesRun as many decisions as your hardware can handle. No metering and no API bill.
* ### CalibratedProbabilities you can put thresholds on. Laya’s calibration error (ECE) is 0.081 after temperature fitting, vs 0.246 for Jev.

## Platforms

Runs where you work.

A desktop app and a command line for macOS, Windows and Linux, and a Docker image for servers. Every model runs on the CPU; an NVIDIA GPU on Linux, in WSL 2 or in Docker takes a request down to milliseconds.

Platform
Desktop app
Command line
GPU
macOS
Apple silicon
Desktop app
Menu bar app
.dmg
Command line
Install script
GPU
CPU only
Windows
10 and 11, x64
Desktop app
Desktop app
.exe or .msi
Command line
PowerShell script
GPU
CPU only
NVIDIA via WSL 2
Linux
x86-64
Desktop app
Desktop app
AppImage, .deb, .rpm
Command line
Install script
systemd service
GPU
NVIDIA, CUDA 13
Linux
ARM64
Desktop app
Not available
Command line
Install script
systemd service
GPU
CPU only
WSL 2
Linux on Windows
Desktop app
Not available
Command line
Install script
Same as Linux
GPU
NVIDIA, CUDA 13
Docker
amd64 and arm64
Desktop app
Not available
Command line
Image on GHCR
GPU
NVIDIA, CUDA 13
:cuda image, amd64
Install for your platform 

NVIDIA GPUs need driver R580 or newer; the installers fetch the CUDA libraries only when they find one. On Apple, AMD and Intel GPUs, models run on the CPU.

## Get up and running in minutes.

One binary, one command:ollaya run laya.

Download

macOS, Windows, Linux and Docker · Apache-2.0 ·GitHub