---
title: 'GitHub - drumih/turbo-fieldfare: Gemma 4 26B-A4B inference in ~2 GB of RAM on any M-series MacBook · GitHub'
url: https://github.com/drumih/turbo-fieldfare
site_name: hackernews_api
content_file: hackernews_api-github-drumihturbo-fieldfare-gemma-4-26b-a4b-infer
fetched_at: '2026-07-29T19:31:33.808878'
original_url: https://github.com/drumih/turbo-fieldfare
author: gitpusher42
date: '2026-07-29'
description: Gemma 4 26B-A4B inference in ~2 GB of RAM on any M-series MacBook - drumih/turbo-fieldfare
tags:
- hackernews
- trending
---

drumih

 

/

turbo-fieldfare

Public

* NotificationsYou must be signed in to change notification settings
* Fork21
* Star708

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

12 Commits
12 Commits
.github
.github
 
 
Scripts
Scripts
 
 
Sources
Sources
 
 
Tests
Tests
 
 
docs
docs
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Package.resolved
Package.resolved
 
 
Package.swift
Package.swift
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
THIRD_PARTY_NOTICES.md
THIRD_PARTY_NOTICES.md
 
 
View all files

## Repository files navigation

# TurboFieldfare

Gemma 4 26B-A4B inference in about 2 GB of RAMA custom Swift + Metal runtime for any Apple Silicon Mac, even the 8 GB ones.

Quick start·Local server·Benchmarks·Contribute results·How it works·Experiments·References

Memory got expensive. So I gave a 26-billion-parameter model a ~2 GB budget.

TurboFieldfare runs the instruction-tunedGemma 4 26B-A4Bwithout loading the entire 14.3 GB model into memory. It keeps the shared
1.35 GB core and FP16 KV cache in memory, then streams only the experts needed
for each token from SSD. This is what lets the model run on Macs with 8 GB of
RAM.

The runtime, streaming installer, CLI, and native Mac app are written in Swift
and Metal. TurboFieldfare is model-specific rather than a wrapper around MLX or
llama.cpp. The curatedexperiment recordsummarizes 103 measured results across kernels, caching, I/O, prefill, and
decode.

## Try it

git clone https://github.com/drumih/turbo-fieldfare.git

cd
 turbo-fieldfare
swift build -c release
.build/release/TurboFieldfareMac

On the first run, Swift Package Manager downloads and builds the Swift packages
required by the tokenizer. The complete release build includes the foreground
Mac app and its sibling decode-service executable.

When the app opens, chooseDownloadand let TurboFieldfare fetch and repack
the pinned model (about 15 GB). Once it is ready, chooseLoad Model, type
your prompt, and pressGenerate.

## At a glance

Metric

Value

Model

Gemma 4 26B-A4B IT, 26B total parameters, about 3.88B active per token

Weights

MLX affine 4-bit, group 64; 8-bit router; 4-bit shared and routed experts

Memory

~2 GB of weights and 4K KV cache

Storage

About 14.3 GB for the installed text-only model

Hardware

Apple Silicon Mac; 8 GB of RAM

Platform

macOS 26, Metal 4, Swift 6.2

M2 measured decode

5.1-6.3 tok/s
 on an 8 GB M2 MacBook Air

M5 measured decode

31-35 tok/s
 on a 24 GB M5 Pro

The measured result is a reference point, not a performance ceiling. Prompt
length, generated length, page-cache state, and hardware all affect throughput.
To help measure another Apple Silicon Mac, follow thecommunity benchmark guide.

## Using TurboFieldfare

TurboFieldfare provides a native Mac app, a command-line interface, and an
experimental loopback OpenAI-compatible server. They use the same.gturbomodel directory, but only one model-owning product should run at a time.

The Swift package exposes six products:

Product

Purpose

TurboFieldfare

Swift library containing the runtime and Metal kernels

TurboFieldfareMac

Native Mac app for installation and generation

TurboFieldfareDecodeService

One-shot local model and Metal owner used by the Mac app

TurboFieldfareCLI

Command-line instruction chat and raw completion

TurboFieldfareServer

Loopback OpenAI-compatible Chat Completions server

TurboFieldfareRepack

Streaming model installer and install verifier

### Requirements

* An Apple Silicon Mac; the validated target is an 8 GB M2 MacBook Air
* macOS 26 with Metal 4
* Xcode 26 and Swift 6.2 or newer
* Enough free storage for the ~14.3 GB model installation
* An internet connection for the first model install

The package is arm64-only. Older macOS and Metal versions are not supported.

### Prompting the model

The Mac app treats what you type as an instruction and handles Gemma's chat
formatting automatically. Just describe the task and include any context the
model needs.

Generation defaults to temperature0.2, Top-K64, and Top-P0.95. Set
temperature to0for deterministic greedy output. The model can still repeat
itself or give incorrect answers, so check important results.

TurboFieldfare is text-only. The app and CLI support user and model messages
plus optional system guidance; they do not expose or execute tools. The
loopback server accepts function-tool declarations and returns
model-produced tool calls for the client to authorize and execute. Images,
audio, and video are not supported.

### Mac app

Clone the repository, then run the app from its root:

swift build -c release
.build/release/TurboFieldfareMac

Build the complete package so the app and its sibling decode service are both
available. When launched from this checkout, the app stores the model inscratch/gemma4.gturbo.

#### Install the model

On first launch, the app checks the available storage and shows the download
and installed sizes. ChooseDownloadto begin.

The installer never materializes the full source checkpoint. It streams the
required byte ranges from the pinned Hugging Face revision and repacks them
directly into the.gturbolayout as they arrive. This avoids a second full
checkpoint on disk and keeps scratch memory bounded.

The first installation transfers about 15 GB through bounded Hugging Face
range requests. Network speed and Hugging Face response times vary, so it can
take a while. The completed.gturboinstallation occupies about 14.3 GB and
is accepted only after its manifest and file hashes have been validated.
Installation does not load the model into memory.

#### Load and generate

After installation:

1. ChooseLoad Model.
2. Enter a prompt in the composer.
3. ChooseGenerate, or pressCommand+Return.
4. Use the stop button orEscapeto end generation early.

The status bar shows generation progress, decode speed, and memory use. Use the
right pane to configure sampling, context length, expert-cache slots, and
runtime options. SeeRuntime controlsfor details
and defaults.

### Command-line interface

The CLI uses an existing.gturboinstallation. If you installed the model
through the Mac app, it is already available atscratch/gemma4.gturbo.
Otherwise, install it from the command line:

swift run -c release TurboFieldfareRepack \
 --output scratch/gemma4.gturbo \
 --overwrite

Continue a cancelled or interrupted download:

swift run -c release TurboFieldfareRepack \
 --output scratch/gemma4.gturbo \
 --overwrite \
 --resume

Remove saved download state:

swift run -c release TurboFieldfareRepack \
 --discard-partial \
 --output scratch/gemma4.gturbo

The runtime accepts only a completed.gturbodirectory with a finalmanifest.json.

Verify an existing installation without loading the model:

swift run -c release TurboFieldfareRepack \
 --verify-install \
 --input-gturbo scratch/gemma4.gturbo

#### Instruction chat

Put chat messages in a JSON array and pass it with--messages-file:

[
 {
"role"
: 
"
user
"
, 
"content"
: 
"
Explain why chunked prefill reduces time to first token while keeping memory bounded.
"
}
]

swift run -c release TurboFieldfareCLI \
 --model scratch/gemma4.gturbo \
 --messages-file messages.json

This formats messages in the same way as the Mac app. The CLI response limit
is set with--max-new, which defaults to 1,024 tokens. The Mac app can
generate until the selected context window is full.

#### Raw completion

--promptis available for raw completion and reproducible comparisons. It
passes the text directly to the model without chat formatting. Use--messages-filefor instruction-response conversations.

swift run -c release TurboFieldfareCLI \
 --model scratch/gemma4.gturbo \
 --prompt 
"
The capital of France is
"
 \
 --max-new 64 \
 --temperature 0

This example deliberately requests a short greedy completion.

Common generation options include--max-context,--temperature,--top-k,--top-p,--repetition-penalty,--seed, and repeatable--stopstrings.
The public CLI uses production runtime defaults. Run the following command for
the complete option list:

swift run -c release TurboFieldfareCLI --help

Generated text goes to standard output. Timing statistics go to standard error;
add--quietto suppress that footer in scripts.

### Local OpenAI-compatible server

Build the server and point it at an installed model:

swift build -c release --product TurboFieldfareServer
.build/release/TurboFieldfareServer \
 --model scratch/gemma4.gturbo

It listens onhttp://127.0.0.1:8080/v1and supports Chat Completions,
streaming, function tools, and single-prefix prompt reuse. The client must
authorize and run every tool call. Keep the server on loopback; it has no
remote authentication or TLS.

SeeLocal serverfor a test request, Python and
OpenCode setup, prompt reuse, tool handling, and the supported API subset.

## Test and contribute

Run the public test suite serially:

Scripts/test.sh

Before starting a model run, close memory-heavy apps and checkmemory_pressure -Q. If it reports little free memory, postpone the run. Run
only one TurboFieldfare app, decode service, CLI, server, test, or other
local-model process at a time.

To contribute a comparable performance result, follow thecommunity benchmark guide.

## How the inference engine works

At each transformer layer, Metal computes attention and the router from
resident weights. The CPU uses the router's top-8 expert IDs to plan against
the layer's 16-slot LFU cache, then fills misses with bounded parallelpreadcalls into Metal-visible buffers. Metal computes the resident shared-expert
branch while those reads run, then combines the shared and routed outputs.

Prompt prefill uses chunks of up to 128 tokens so one fetched expert can serve
multiple rows. Generation repeats the routed layer loop one token at a time.
The installer applies the same bounded-memory rule: it repacks remote ranges
directly into.gturbowithout staging a full shard or tensor.

For a visual introduction to the model architecture, see Maarten Grootendorst'sA Visual Guide to Gemma 4.

System designexplains the.gturbolayout, memory
ownership, prefill, router handoff,cb1/io/cb2phases, Metal kernels, and
correctness invariants.

## Status and scope

TurboFieldfare currently includes:

* Remote streaming repack into the.gturbomodel format
* Instruction-tuned Gemma 4 26B-A4B with verified text-only chat formatting
* 4-bit MLX affine embedding, attention, shared-expert, and routed-expert
weights, with an 8-bit router
* Custom Metal kernels for quantized GEMV, attention, MoE, normalization,
RoPE, sampling, and production fusions
* SSD-backed routed-expert streaming with a bounded expert cache
* Chunked single-prompt prefill and token-by-token generation
* FP16 KV storage with bounded circular storage for 25 sliding-window layers
and linear storage for 5 full-attention layers
* Exact split-K/V decode attention with distinct normalized K and V paths
* A Swift library, streaming installer, command-line interface, loopback
OpenAI-compatible server, and native SwiftUI/AppKit Mac app with a one-shot
local decode service

Current scope is text-only inference from the pinned Gemma 4 26B-A4B
instruction checkpoint on Apple Silicon Macs with at least 8 GB of RAM.

### Future work

* Build iPhone and iPad apps, then measure inference speed and memory use on
mobile hardware.
* Benchmark more Apple Silicon Macs, especially the base 16 GB M4 Mac mini and
other 8 GB models.

## Experiments and technical documentation

Theexperiments that shaped TurboFieldfareexplain the largest wins, the plausible ideas that failed, and the early
results that reversed under stronger validation. The detailedexperiment recordkeeps all 103
audited entries as optional evidence.

Useful entry points:

* Local OpenAI-compatible server
* System design
* Benchmarks
* The experiments that shaped TurboFieldfare
* Experiment inventory and summaries
* Implementation references

## License and model terms

TurboFieldfare's source and documentation are licensed under theApache License 2.0.

Model weights are not included. The installer downloads them separately from
the pinned Hugging Face checkpoint, and the weights remain governed by their
source terms. SeeTHIRD_PARTY_NOTICES.mdfor the model
and Swift package license review.

TurboFieldfare is an independent research project. It is not affiliated with,
sponsored by, or endorsed by Google.

## Afterword and the project name

Thanks for checking out this project!

My name is Andrey Mikhaylov. You can find me onLinkedIn.
I am the author of TurboFieldfare and an iOS and Metal engineer. Most of my
work is with images, video, and on-device AI.

I dedicate this project to my wife, Sasha, the most supportive person I know.
She stands by me even through the hardest times. She loves wildlife, goes
birdwatching, and volunteers with our local birding community. Because of her,
I have also grown closer to birds and nature.

TurboFieldfare is named after the fieldfare, a member of the thrush family and
my favourite bird. It is not the most noticeable or brightly coloured bird, but
it definitely has a character and unique features of its own. I think the same
is true of this project: it may not be the most practical, but I built it with
my favourite tools, especially Metal, in my favourite field, on-device ML
inference. It definitely has its own character and unique features.

Next time you are outside, touch the grass and listen to the birds. Sometimes
it is the most beautiful thing you can do. And if you can, support your local
wildlife community. They do important work.

Thank you!