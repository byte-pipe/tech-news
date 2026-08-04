---
title: GitHub - leonickson1/Swiftlet · GitHub
url: https://github.com/leonickson1/Swiftlet
site_name: hnrss
content_file: hnrss-github-leonickson1swiftlet-github
fetched_at: '2026-08-04T11:46:12.661714'
original_url: https://github.com/leonickson1/Swiftlet
date: '2026-08-03'
description: Contribute to leonickson1/Swiftlet development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

leonickson1

 

/

Swiftlet

Public

* NotificationsYou must be signed in to change notification settings
* Fork4
* Star232

 
 
 
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

7 Commits
7 Commits
Sources
Sources
 
 
Tests/
SwiftletCoreTests
Tests/
SwiftletCoreTests
 
 
assets/
model-configs
assets/
model-configs
 
 
fixtures
fixtures
 
 
references
references
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
IPHONE.md
IPHONE.md
 
 
LICENSE
LICENSE
 
 
PLAN.md
PLAN.md
 
 
Package.resolved
Package.resolved
 
 
Package.swift
Package.swift
 
 
README.md
README.md
 
 
THIRD_PARTY_NOTICES.md
THIRD_PARTY_NOTICES.md
 
 
View all files

## Repository files navigation

# Swiftlet

Run 35B and 80B Qwen models on ordinary Apple devices, including iPhones.

Swiftlet is a Swift + Metal runtime for the Qwen3-Next and Qwen3.5/3.6 MoE
hybrid model family. It keeps only the small dense core of a model resident in
memory and streams the routed Mixture-of-Experts weights from storage on
demand. The result:

Model

Disk

Peak RAM

Decode speed (M5 Mac)

Qwen3.6-35B-A3B, 4-bit

18 GB

2.6 GB

7 to 11 tok/s

Qwen3-Next-80B-A3B, 4-bit

42 GB

4.3 GB

4.5 to 5 tok/s

The 35B also runs on an iPhone 17 in about 2.5 GB of RAM, at about 1 tok/s
today. Credit where due:ANEMLLshowed a 397B
MoE streaming on an iPhone 17 Pro as a proof of concept in early 2026.
Swiftlet's aim is the next step, making this class of model an installable
app on a base iPhone, with an open runtime anyone can build on.

Status: working end to end. Both models generate correct, validated output.
The current focus is kernel speed (the decode loop is dispatch bound, not
IO bound, so there is clear headroom). One expectation to set honestly: only
about 3B parameters are active per token, so these models chat and write
like large models but recall facts like small ones.

## Quick start: try it on a Mac

git clone https://github.com/leonickson1/Swiftlet.git 
&&
 
cd
 Swiftlet
swift build -c release

#
 Download the 35B container from Hugging Face (resumable):

.build/release/swiftlet-repack \
 --from-hf Leonickson/Qwen3.6-35B-A3B-qpack \
 --output 
~
/models/qwen3.6-35b.qpack

#
 Or the 80B (42 GB on disk, still only ~4.3 GB of RAM):

.build/release/swiftlet-repack \
 --from-hf Leonickson/Qwen3-Next-80B-A3B-qpack \
 --output 
~
/models/qwen3-next-80b.qpack

#
 Chat (applies the model chat template, disables the reasoning block,

#
 keeps conversation state so follow-ups prefill only the new turn):

.build/release/swiftlet chat 
~
/models/qwen3.6-35b.qpack \
 
"
Who wrote One Hundred Years of Solitude?
"
 
"
What language did he write it in?
"

#
 One-shot generation with stats:

.build/release/swiftlet generate 
~
/models/qwen3.6-35b.qpack \
 --gpu --chat --prompt 
"
Explain expert streaming in one paragraph.
"

#
 OpenAI-compatible server (loopback only):

.build/release/swiftlet-server --model 
~
/models/qwen3.6-35b.qpack --port 8080

The same command also repacks raw MLX checkpoints
(--from-hf mlx-community/...or--source /path/to/checkpoint).

Requirements: Apple Silicon, macOS 14+ or iOS 17+, free SSD space for the
container (18 GB for the 35B, 42 GB for the 80B).

## Try it on your phone

The 35B runs on iPhone insidePriv AI on the App Store:
open Settings, then Experimental Models, and download the model. It streams
from storage and chats on-device with no server involved.

The Experimental Models feature ships in the newest app version, which is
still in App Store review, so it may not appear for a couple of days. If you
want the phone experience today, build the app from source: the app is open
source atleonickson1/localLLM.
Clone this repo next to it asswiftlet, open the Xcode project, and run it
on your iPhone.

## How it works

These models activate only about 3B of their parameters per token. Each layer
routes every token to 10 of 512 experts (80B) or 8 of 256 (35B). Swiftlet:

* keeps the dense weights resident: attention, DeltaNet projections, routers,
shared experts, embeddings. About 1.3 GB (35B) or 2.5 GB (80B) at 4-bit;
* repacks the tens of thousands of routed experts into fixed-stride blobs in
a.qpackcontainer, so fetching one expert is exactly onepreadfrom
SSD, no mmap and no page-cache thrash;
* caches hot experts in a bounded pool with LFU plus recency eviction. Cache
size barely affects speed (measured 43 to 70 percent hit rates at the same
throughput), because Apple SSDs absorb the misses;
* runs the whole forward pass on Metal with runtime-compiled shaders, so no
Metal toolchain is needed at build time and the same code ships on iOS.

75 percent of the layers use Gated DeltaNet linear attention with a
fixed-size recurrent state, so there is no growing KV cache for those layers
at any context length.

## Four ways to use it

Swiftlet is a library first:

1. The Swift package.Add SwiftletCore to any macOS or iOS app and useSwiftletSessionfor chat with streaming deltas, conversation caching,
sampling with repetition control, and memory-pressure handling built in.
2. The CLI.swiftlet chatandswiftlet generatefor local use and
benchmarking,swiftlet-repackto build containers from MLX checkpoints
(including streaming straight from Hugging Face with resume).
3. The server.swiftlet-serverspeaks the OpenAI chat-completions API
on loopback, so any chat UI that talks to OpenAI-compatible endpoints can
use a streamed local model.
4. An app.Priv AIon iOS embeds SwiftletCore as its streamed-model engine. End users tap
Download and chat. Nothing here is terminal-only. The app itself is open
source atleonickson1/localLLMif you want to build it yourself (clone this repo next to it asswiftlet).

## Correctness

Every layer of the forward pass (Gated DeltaNet recurrence, gated GQA
attention, sparse MoE routing) is validated against mlx-lm reference
implementations with per-layer fixtures, in f32 and int4 quantized form.
Incremental decoding is verified against whole-sequence processing. Metal
kernels are tested against the exact CPU reference, and the fast and scalar
GPU kernels are verified to produce identical outputs. Containers are
byte-verifiable against their source checkpoints. Streaming placement never
changes model semantics: an expert answers identically from cache or disk.

swift 
test

## Relationship to TurboFieldfare

TurboFieldfareproved the
expert-streaming thesis for Gemma on Macs, and Swiftlet adopts several of its
published design lessons with gratitude: stream experts withpreadinto a
bounded slot pool instead of mmap, evict with LFU plus recency, pack experts
at fixed stride so one fetch is one read, install by routing downloaded bytes
straight into their final container positions, and compile shaders at
runtime.

Everything else is built here, from scratch, in about 10k lines of Swift and
Metal written against mlx-lm references rather than TurboFieldfare code:

* support for a different model family with a fundamentally different
architecture: the Qwen hybrid stack with Gated DeltaNet linear attention,
gated GQA, and high-sparsity MoE with a shared expert (TurboFieldfare runs
Gemma, a classical dense transformer);
* MLX affine int4/int8 group quantization compute in Metal, byte-addressed
kernels with 64-bit offsets for multi-gigabyte shards, a cooperative
simdgroup GEMV fast path, and explicit hazard management;
* a validated CPU reference implementation and the fixture infrastructure
that gates every kernel change;
* the.qpackcontainer and repacker, the resumable Hugging Face streaming
installer with stall recovery, and download cancellation;
* the chat session layer: template handling for thinking and non-thinking
Qwen variants, sampling with presence and frequency penalties and
minimum-length and sentence-completion stopping, conversation caching with
delta prefill, and iOS memory-pressure coordination;
* iPhone support end to end, including the app engine integration.

colibrìinformed the caching and
placement policy thinking. mlx-lm is the correctness reference throughout.

Swiftlet was built in collaboration withClaude Code.

## License

Apache 2.0. Model weights are downloaded separately and remain governed by
their own terms (Qwen models: Apache 2.0). See THIRD_PARTY_NOTICES.md.