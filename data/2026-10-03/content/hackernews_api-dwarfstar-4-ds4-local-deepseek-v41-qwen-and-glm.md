---
title: 'DwarfStar 4 (ds4): Local DeepSeek V4.1, Qwen and GLM'
url: https://dwarfstar.sh/
site_name: hackernews_api
content_file: hackernews_api-dwarfstar-4-ds4-local-deepseek-v41-qwen-and-glm
fetched_at: '2026-10-03T21:59:23.400087'
original_url: https://dwarfstar.sh/
author: DwarfStar community
date: '2026-10-02'
description: Docs, benchmarks and setup notes for ds4, antirez's C inference engine for DeepSeek V4/V4.1, Qwen3.8 Flash Next and GLM 5.x on Metal, CUDA and ROCm.
tags:
- hackernews
- trending
---

DS4· LOCAL FRONTIER INFERENCE

 

# Run frontier open weights locally with ds4.

 

DwarfStar 4 is a narrow C inference engine for high-memory Mac,
 CUDA and ROCm machines. It supports DeepSeek V4 and V4.1 Flash,
 GLM 5.x and Qwen3.8 Flash Next, with text and vision models, local
 APIs, a CLI and a native agent in one stack.

 
 
Get started 
→
 
View on GitHub
 
 

SUPPORTED: DEEPSEEK V4 / V4.1 + GLM 5.x + QWEN3.8·MIT LICENSE·C / METAL / CUDA / ROCM·QWEN ON 64GB

 
 
 
 
 
 
ds4 · local session
 
 
 
 
 
$ ./ds4
DwarfStar 4 · DeepSeek V4 Flash · ds4f-q2
local backend ready · model loaded
> /read src/kvcache.c
1,412 lines loaded into context
> why can a prefix survive a server restart?
The KV cache is keyed by the SHA1 of the rendered
prompt prefix and persisted to disk, so a matching
prefix is reloaded instead of recomputed.
 
 
 
 
 
 
 
 
 
 
 

PRINCIPLE· LOCAL MODEL STACK

 
 
 

PHASE 1· THE GIANT

 

### A 284-billion-parameter star

 

DeepSeek V4 Flash is a large mixture-of-experts model. The usual
 path is remote serving; ds4 starts from the opposite constraint.

 
 
 

PHASE 2· THE COLLAPSE

 

### Compressed, not lobotomized

 

Asymmetric quantization targets the routed experts while preserving
 critical paths. The model becomes practical on high-memory machines.

 
 
 

PHASE 3· THE DWARF STAR

 

### Dense, resident, yours

 

The local engine exposes a CLI, HTTP APIs and a native agent, all
 sharing the same model state and cache.

 
How the collapse works →
 
 
 

SCROLL ▾

 
 
 
 
 
 
 
 
 

CORE 01

 

### Asymmetric 2-bit quantization

 
 

Compress the routed experts, keep critical shared paths precise.
 That is how the supported routed-MoE builds fit their target machines.

 
 
 
 
 
 

CORE 02

 

### KV cache as a disk citizen

 
 

Save long prefixes to SSD and resume by prompt hash. Restarts do
 not have to mean full re-prefill.

 
 
 
 
 
 

CORE 03

 

### One engine, three interfaces

 
 

Use./ds4for chat,./ds4-serverfor local
 APIs and./ds4-agentfor persistent coding sessions.

 
 
 
 
 
* SSD STREAMING
* TENSOR PARALLELISM
* SESSION BATCHING
* DSPARK + MTP
* VISION INPUT
* SSD STREAMING
* TENSOR PARALLELISM
* SESSION BATCHING
* DSPARK + MTP
* VISION INPUT
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
MODEL
 
DeepSeek V4 / V4.1
 
GLM 5.x · Qwen3.8
 
supported GGUF layouts only
 
asymmetric 2-bit + imatrix
 
 
 
 
load
 
 
 
 
 
ENGINE
 
ds4 engine
 
written in C
 
 
metal · cuda · rocm
 
 
parallel · batch · speculate
 
 
 
 
KV cache
 
RAM ⇄ SSD · survives restarts
 
 
 
 
serve
 
 
 
 
./ds4
 
interactive CLI
 
 
./ds4-server
 
OpenAI + Anthropic API
 
 
./ds4-agent
 
native coding agent
 
 
 
 
 
 
 
 
 
 
 
personal → distributed memory classes
 
 
 
 

RUNTIME MAP· SIMPLIFIED. SEEARCHITECTURE NOTESFOR THE FULL DRAWING.

 
 
 
 
 
 
 
 

STEP 1· FETCH THE WEIGHTS

 
 
 
 
ds4 · zsh
 
 
 
$
 git clone https://github.com/antirez/ds4
 
$
 cd ds4 && ./download_model.sh ds4f-q2
 
 
 
 
 

STEP 2· BUILD FOR YOUR BACKEND

 
 
 
 
ds4 · zsh
 
 
 
$
 make 
# macOS · Metal
 
$
 make cuda-spark 
# Linux · DGX Spark
 
 
 
 
 

STEP 3· TALK TO IT

 
 
 
 
ds4 · zsh
 
 
 
$
 ./ds4
 
$
 ./ds4-server --ctx 100000 
# or serve an API
 
 
 
 
 
 
 
 
 
 
 
 
 
PLATFORM
 
 
Apple Silicon
 
NVIDIA (DGX Spark / CUDA)
 
AMD Strix Halo (ROCm)
 
 
 
 
MEMORY
 
 
32 GB
 
64 GB
 
96 GB
 
128 GB
 
256 GB
 
512 GB
 
2 × 512 GB (two machines)
 
 
 
 
 

✓ Runs well

 

V4 Flash Q2 is the baseline. At 128 GB, GLM 5.3 Q2 and Qwen Q4 also fit; V4.1 Q2 streams from SSD.

 
./download_model.sh ds4f-q2 && make
 

REF· M5 MAX 128GB · 32K CTX: 34.4 T/S GEN · 557 T/S PREFILL

 
 

Estimates from theds4 benchmark table.
 Full guide inHardwareandInstallation.

 
 
 
 
 
 
 
 
 
 
Machine
 
Context
 
Prefill t/s
 
Generation t/s
 
 
 
 
 
M5 Max, 128 GB
 
 q2 · 2,048 tok

 
790.2
 
39.4
 
 
M5 Max, 128 GB
 
 q2 · 65,536 tok

 
398.5
 
27.6
 
 
DGX Spark, 128 GB
 
 q2 · 2,048 tok

 
825.8
 
18.1
 
 
DGX Spark, 128 GB
 
 q2 · 65,536 tok

 
823.0
 
13.8
 
 
 
 
All benchmarks 
→
 
 
 
 
 
 
 
OpenCode
 
Claude Code
 
Codex CLI
 
Pi
 

/v1/chat/completions 
·
 /v1/messages

·
 /v1/responses

 
 
 
 
 
 

## Own your local AI inference.

 

Start with the quickstart, check the hardware matrix, then connect
 your editor, agent or API client to the local server.

 
 
Get started 
→
 
Check hardware requirements