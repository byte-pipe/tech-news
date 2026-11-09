---
title: 'GitHub - synchopate/llama-modchip: 🐋 Run 284B DeepSeek-V4-Flash (<59GiB RAM, 44.4 tok/s pp, 9.1-14.7 tok/s) & 30B MoEs (25-111 tok/s) on a pure 64GB CPU at 256K ctx (0 GPUs). SwiGLU-H2, Stockfish-PVS L3 & 13ms Claude Code restore. · GitHub'
url: https://github.com/synchopate/llama-modchip
site_name: hnrss
content_file: hnrss-github-synchopatellama-modchip-run-284b-deepseek-v
fetched_at: '2026-11-09T16:00:49.693462'
original_url: https://github.com/synchopate/llama-modchip
date: '2026-11-08'
description: 🐋 Run 284B DeepSeek-V4-Flash (<59GiB RAM, 44.4 tok/s pp, 9.1-14.7 tok/s) & 30B MoEs (25-111 tok/s) on a pure 64GB CPU at 256K ctx (0 GPUs). SwiGLU-H2, Stockfish-PVS L3 & 13ms Claude Code restore. - synchopate/llama-modchip
tags:
- hackernews
- hnrss
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

49 Commits
49 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
apple-silicon
apple-silicon
 
 
assets
assets
 
 
benchmarks
benchmarks
 
 
docs
docs
 
 
fedora
fedora
 
 
gateway
gateway
 
 
kv_cache
kv_cache
 
 
paper
paper
 
 
patches
patches
 
 
reviews
reviews
 
 
scripts
scripts
 
 
speculative
speculative
 
 
systemd
systemd
 
 
windows
windows
 
 
.gitignore
.gitignore
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
FAQ.md
FAQ.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
RELEASE_NOTES.md
RELEASE_NOTES.md
 
 
install.sh
install.sh
 
 
modchip
modchip
 
 
View all files

## Repository files navigation

# llama-modchip (v2.4.0)

### CPU-First Inference for 284B & 30B Mixture-of-Experts Models on 16–64 GB RAM

Quickstart·Quantization & Memory Specs·Supported Models·Supported Hardware·Leaderboard·Technical Paper (paper/)·Architecture·FAQ

284.33B
Total MoE params (13.17B active)

56.56 GiB
DeepSeek-V4 GGUF (1.71 bpw)

57.61 GiB
Peak VmRSS @ 256K ctx

44.36 tok/s
284B CPU prefill (16C Zen 5)

25.0–111.6 tok/s
30B MoE CPU decode (3.75 bpw)

13.1 ms
/dev/shm KV slot restore

0
GPUs required

Hardware Class

System RAM

Target Checkpoint

Throughput (0 GPUs)

Architecture & Memory Notes

Developer laptop / Mini-PC

16–32 GB

Nemotron-3.5-30B-A3B
 (
14.35 GiB
, 
3.75 bpw
)

25.0–60.4 tok/s

46 Mamba-2 SSM layers + 1.64 MB L3 PVS drafter; 256K context uses 432 MB KV

64 GB Desktop / Server

64 GB

DeepSeek-V4-Flash 284B
 (
56.56 GiB
, 
1.71 bpw
)

44.4 tok/s pp · 9.1–14.7 tok/s tg

Fits in 62.5 GiB usable Linux RAM (57.61 GiB VmRSS) with zero NVMe swap

Hybrid Desktop (CPU + 16 GB GPU)

32–64 GB

Nemotron-30B / Qwen3-30B
 (
3.75–4.25 bpw
)

80.80 tok/s

Hot attention/SSM trunk on GPU (
-ngl 99
), cold routed MoE experts in CPU RAM

8-Channel Workstation (Threadripper)

128 GB+

DeepSeek-284B / Nemotron-30B

111.62 tok/s
 (30B)

8-CCD AVX-512BW 
_1x8
 register tiling saturates 8-channel DDR5 bandwidth

## Overview

llama-modchipis a set ofggml/llama.cppkernel patches, quantization transcoders, and runtime tools designed to run sparse Mixture-of-Experts (MoE) checkpoints entirely in system RAM on x86_64 (AVX-512/AVX2) and ARM64 (NEON/SVE/ Apple Metal) processors:

1. Fitting 284BDeepSeek-V4-Flashinto 64 GB Physical RAM (56.56 GiBon disk,1.71 bpw):StandardUD-IQ1_Sbuilds ofDeepSeek-V4-Flash(284.33Btotal,13.17Bactive across 43 MLA layers and 256 routed experts) occupy76.87 GiB(82.5 GB), exceeding the ~62.5 GiB of usable RAM on a 64 GB Linux system and causing page-cache thrashing or OOM kills.llama-modchipreduces the checkpoint to56.56 GiB(60.73 GB) so the entire model plus a256KKV cache (57.61–58.9 GiBVmRSS) locks into RAM with zero swap. By default, all 6 routed experts per layer (Top-6) are evaluated without pruning.
2. CPU Cache & SIMD Kernel Patches (+77%prefill,+53%decode):Replaces single-column quantized matrix-vector loops during prompt prefill with a 4-level register (ZMMAVX-512BW) + L1D (32 KB) + L2 (1 MB) + L3 (64 MB) multi-column ({8,4,3,2}) tiling schedule (25.0 -> 44.36 tok/son 16-core Zen 5), register-stationaryMQA8FlashAttention, and non-temporal_MM_HINT_NTAMoE streaming so cold expert weights do not evict hot KV cache lines from L3.
3. Self-Speculative Drafting & Instant Agent Context Restore:Pairs a1.64 MBL2/L3 Zobrist n-gram drafter (Stockfish-PVS v2) with/dev/shmKV slot snapshots (13.1–32.6 msrestore time for 40-tool Claude Code prompts) and an$O(1)$speculative rollback fix fordeepseek4recurrent/MLA states.

## Quantization & Memory Breakdown

To answer the most common technical question upfront—exact bit-widths (bpw), base checkpoints, and what is compressed in each GGUF:

Checkpoint

Total / Active Params

Base Source

Disk Size (
GiB
 / 
GB
)

Effective 
bpw

Layer-by-Layer Tensor Allocation

Nemotron-3.5-30B-A3B-Q4_0

30.2B
 / 
3.0B

BF16 Official

17.59 GiB
 (
18.89 GB
)

4.50 bpw

Standard 
Q4_0
 across MoE + attention; 
F32
 norms & SSM conv/decay

Nemotron-3.5-30B-A3B-MXFP4

30.2B
 / 
3.0B

BF16 Official

15.95 GiB
 (
17.13 GB
)

4.25 bpw

GGML_TYPE_MXFP4
 (
E2M1
 + shared exponent) on routed MoE; 
Q4_0
/
Q8_0
 trunk

Nemotron-3.5-30B-A3B-Fractal-64

30.2B
 / 
3.0B

BF16 Official

14.35 GiB
 (
15.41 GB
)

3.75 bpw

Attention, Mamba-2 SSM & shared experts in 
Q4_0
/
Q8_0
/
F32
; cold routed MoE experts in hybrid 
Q4_0
 + 
Fractal-64
 (
Q2_0
, 64-weight block + 
BF16
 scale). Scores 
100/100
 on 
benchmarks/eval_quality_and_tools.py
.

DeepSeek-V4-Flash-0731-Fractal

284.33B
 / 
13.17B

Unsloth 
UD-IQ1_S
 (
76.87 GiB
 / 
82.5 GB
)

56.56 GiB
 (
60.73 GB
)

1.71 bpw

• 
Embeddings, Dense L0, 43 Shared Experts (
shexp
), MLA 
kv_a
 / 
q_a
 / 
wkv_b
:
 Preserved in 
Q4_K
 / 
Q5_K
 / 
F32
• 
MLA 
wq_b
 & 
attn_output
 (
wo_a
/
wo_b
):
 Transcoded to 
Fractal-64
 (
GGML_TYPE_Q2_0
, 
3.75 bpw
, 30B/64-block w/ 8 sub-scales & 
BF16
 scale)
• 
256 Routed MoE Experts (
ffn_*_exps
):
 Primarily 
IQ1_S
 (
1.5625 bpw
) with analytical 
SwiGLU-H2
 second-order scale matching; sensitive boundary layers preserved in 
IQ2_XXS
 (
2.06 bpw
) & 
IQ1_M
 (
1.75 bpw
) (
-20.31 GiB
 vs 
UD-IQ1_S
)

Note on MoE Expert Routing (Top-K):By default (v2.4.0 Lossless),DeepSeek-V4-Flashevaluatesall 6 routed experts + 1 shared expert (Top-6)per layer with zero expert dropping (1.00000logit cosine similarity vs the unpatched runtime on the same checkpoint). SettingLLAMA_MOE_TOP_K=5or4is an optional runtime flag for users who want to trade a small perplexity delta for higher decode throughput.

## Quickstart

### Linux & macOS (Automated Setup & Chat)

git clone https://github.com/synchopate/llama-modchip.git

cd
 llama-modchip
./modchip chat

### Direct Run (Pre-Compiled Linuxx86_64Binary + Hugging Face.gguf)

Compatibility Note (GGML_TYPE_Q2_0 = 40):Fractal-64models use custom block-64BF16-scale tensors (GGML_TYPE_Q2_0, type ID40) anddeepseek4/Stockfish-PVSkernels. Unpatchedllama.cpp, Ollama, or LM Studio binaries will reject them withunknown tensor type 40. Use./modchipabove or the standalone pre-compiled binary (llama-server-modchip-linux-x86_64, zero external.sodependencies) included in the Hugging Face repositories andGitHub Releasev2.4.0:

#
 1. For 30B Nemotron-3.5-A3B (14.35 GiB — runs in 16–32 GB RAM at 25–60.4 tok/s):

hf download Synchopate/NVIDIA-Nemotron-3.5-30B-A3B-Fractal-64-CPU-GGUF \
 llama-server-modchip-linux-x86_64 NVIDIA-Nemotron-3.5-30B-A3B-Fractal-64.gguf --local-dir 
.

chmod +x llama-server-modchip-linux-x86_64
./llama-server-modchip-linux-x86_64 -m NVIDIA-Nemotron-3.5-30B-A3B-Fractal-64.gguf -c 262144 -t 16 --port 8080

#
 2. For 284B DeepSeek-V4-Flash (56.56 GiB — fits in 64 GB RAM at 9.1–14.7 tok/s):

hf download Synchopate/DeepSeek-V4-Flash-0731-Fractal-64GB-CPU-GGUF --local-dir ./dsv4
chmod +x ./dsv4/llama-server-modchip-linux-x86_64
./dsv4/llama-server-modchip-linux-x86_64 -m ./dsv4/DeepSeek-V4-Flash-0731-Fractal-00001-of-00003.gguf -c 32768 -t 16 -fa on --port 8080

### Windows 10/11 (Hybrid GPU + CPU MoE Pack)

Openwindows/and runwindows/AVVIA_MODCHIP.bat(or./modchip startin Git Bash). It detects physical CPU cores, free RAM, and GPU VRAM (nvidia-smi), downloadsllama.cppCUDA 12.4 / Vulkan binaries, computes the--n-cpu-moesplit, and launches the Web Chat UI (http://127.0.0.1:8080).

./modchip
 Command

Description

./modchip chat

Interactive terminal chat with live 
tok/s
, TTFT, and 
Stockfish-PVS
 acceptance telemetry

./modchip web

Opens the Dark-Mode Web Chat & Live Telemetry HUD (
http://127.0.0.1:8787
)

./modchip bench

Runs a 30-second 2-stage speed test and prints a shareable CPU Benchmark Scorecard

./modchip claude

Launches Claude Code CLI (
40 tools
) wired to the local 256K engine (
18.9–32.6 ms
 warm restore)

./modchip eval

Runs the reproducible 100-Point Quality, Tool-Calling, Coding & 8.5K Needle Gate

./modchip quantize

Transcodes 
BF16
/
Q4_0
/
UD-IQ1_S
 GGUFs into 
Fractal-64
 (
3.75 bpw
) or 
Fractal-MXFP4
 (
4.25 bpw
)

./modchip status
 / 
stop

Inspects CPU readiness, 
2MB HugePages
, and 
/dev/shm
 IPC, or stops background services

### Hardware Readiness Check (Zero Model Download Required)

curl -sL https://raw.githubusercontent.com/synchopate/llama-modchip/main/scripts/check_cpu_readiness.py 
|
 python3

Submit your terminal scorecard via aGitHub Benchmark IssueorGitHub Discussionsto add your CPU to the leaderboard below.

## Supported Models & Model-Specific Optimizations

Each model family has a dedicated technical guide with mathematical derivations, operator-level latency profiles, and quality gate benchmarks:

Model Family

Total / Active Params

Disk (
GGUF
) & 
256K
 RAM (
VmRSS
)

Key Optimizations Implemented

Verified Speed (
16C Zen 5
 / Hybrid)

Detailed Guide

NVIDIA-Nemotron-3.5-30B-A3B
(
Fractal-64
 / 
MXFP4
 / 
Q4_0
)

30.2B
 / 
3.0B
(
23 SSM + 23 MoE + 6 GQA
)

14.35 – 17.59 GiB
(
15.4 – 21.7 GiB
 RSS)

• 
Block-64 
Fractal-64
 (
3.75 bpw
) & 
MXFP4
 (
4.25 bpw
)
 (
100/100
 Quality Gate)
• 
Stockfish-PVS v2 (M=7)
 + 
RouteCrack
 (
1.64 MB
 L2/L3 Zobrist TT)
• 
432 MB
 256K EAKV (
Q8_0/Q4_0
)
 + 
_MM_HINT_NTA
 L3 isolation
• 
18.9 ms
 
/dev/shm
 Slot-0 Restore
 (
~6,800x
 faster warm turns)

25.0 – 60.4 tok/s
 (
0 GPU
)
80.8 tok/s
 (
Vulkan Hybrid
)
111.6 tok/s
 (
Threadripper
)

Nemotron Guide

DeepSeek-V4-Flash-0731-Fractal
(
SwiGLU-H2 + Fractal-64
)

284.33B
 / 
13.17B
(
43L MLA + 256+1s MoE
)

56.56 GiB
 
(
-20.3 GiB
)
(
58.9 GiB
 RSS
 — fits in 
64 GB
)

• 
Analytical 2nd-Order 
SwiGLU-H2
 MoE + 
Fractal-64
 MLA Transcoding
• 
4-Level Register (
ZMM
 AVX-512BW) + L1D (
32KB
) + L2 (
1MB
) + L3 (
64MB
) Multi-Column (
{8,4,3,2}
) Prefill Tiling (
25.0 -> 44.36 tok/s
, 
+77%
)
• 
Register-Stationary AVX-512 
MQA8
 FlashAttention (
2.0x
) + AVX-512 
quantize_row_q8_K
• 
Optional 
$L_2$
-Quadrature MoE Pruning + L1-Local Gate-First SwiGLU (
10.74 tok/s
)
• 
SVD of 
wo_b * wo_a
 (
99.82%
 CosSim at 
-25%
 rank) & 
$O(1)$
 Rollback Fix

43.2–44.4 tok/s
 
(Prefill)
9.06–9.95 tok/s
 
(Lossless Top-6)
9.87–10.15 tok/s
 
(
Top-5 L2
)
10.41–10.74 tok/s
 
(
Top-4+SwiGLU
)
11.5–14.7 tok/s
 
(
PVS
)

DeepSeek-V4 Guide

Qwen3-30B-A3B
 & 
Qwen3-14B
(
Q3_K_M
 / 
Q4_K_M
)

30.5B
 / 
3.3B -> 1.7B
(
48L GQA
, 
128
 exp)

13.70 – 17.28 GiB
(
14.5 – 19.4 GiB
 RSS)

• 
Norm-Preserving Dynamic MoE Top-K (
8 -> 4
, 
+38.5%
 decode)
• 
3:1 Interleaved SWA Safety Lock (
LLAMA_SWA_STRIDE=4
)
• 
Windows 
11 GB VRAM + 16 GB RAM
 Hybrid Split (
--n-cpu-moe N
)

34.80 tok/s
 (
0 GPU
 Top-4)
50–58 tok/s
 (
14B
 RTX 2080 Ti)

Architecture §3.9

NVIDIA-Nemotron-H-8B-128K
(
Q8_0
 / 
Q4_K_M
)

8.0B
 Dense
(
48 SSM + 4 GQA
)

4.60 – 8.00 GiB
(
210 MB
 KV @ 
128K
)

• 
48-Layer Mamba-2 SSM Constant-Memory Backbone
• 
100% GPU VRAM Residency on 
8–11 GB
 Cards (
0 GB
 System RAM)

100+ tok/s
 (
RTX 2080 Ti
)
147.6 tok/s
 (
CPU pp512
)

Nemotron Guide

## Supported Chips & Processor-Specific Optimizations

Microarchitectural details and tuning flags for each processor and GPU hybrid are documented indocs/HARDWARE_OPTIMIZATIONS.md:

Processor / Platform

Verified Hardware

Hardware-Specific Optimizations Active

Platform Guide & Scripts

AMD Zen 5 (
Desktop / Mobile / Server
)

Ryzen 9 9955HX
, 
9950X
, 
EPYC 9005 Turin

• Single-cycle 512-bit 
AVX-512 (
VPDPBUSD
, 
VPRORVQ
, 
VBMI
, 
BF16
)
• 
48 KB
 L1D 3D Tiling (
TILE_I0=64
)
 on multi-head 
wo_a
 projections
• 
_MM_HINT_NTA
 Victim-L3 Isolation (
64 MB
)
 + 
2MB
 THP (
6.14 GB
 L2 STLB)

Hardware Guide §2.1
install.sh

AMD Zen 4 Multi-CCD (
Threadripper / EPYC
)

Threadripper PRO 7985WX
 (
64C/128T
, 
8 CCDs
, 
256 MB
 L3)

• 
Dynamic sysfs L3 CCD Topology Discovery
 (
scripts/llama_modchip.py
)
• 
Deterministic 
4C/CCD
 Stride (
-t 32
)
: avoids Infinity Fabric saturation (
+54%
 faster than 
-t 64
)

Hardware Guide §2.2
Issue #1

AMD 3D V-Cache + Radeon Vulkan Hybrid

Ryzen 9 7945HX3D
 (
128 MB
 L3) + 
RX 9070 XT 16GB
 (
RADV
)

• 
Tensor-Role Splitting (
-ngl 99 --n-cpu-moe N --load-mode none
)
• Native 
Vulkan 
SSM_SCAN
 + 
Fractal-MXFP4
 (
15.2 GB
) GPU Shaders
 (
80.8 tok/s
 at 256K)

Hardware Guide §2.3
FAQ.md
 Q8

Intel / AMD + NVIDIA RTX (
Windows 10/11
)

Core i9-9900K / 14900K
 + 
RTX 2080 Ti 11GB / 3090 / 4090

• 
Single-Cycle AVX2 
vpsllvd + vpmaddwd
 Sub-Scale Fusion
• 
Live-VRAM 
--n-cpu-moe
 Solver (
550 MB
 WDDM Reserve)
 + 
_WIN32
 
CreateFileMappingA

Windows Guide
windows/modchip_win.ps1

Apple Silicon (
M1 / M2 / M3 / M4
)

Apple M4 Max
 (
16C+40C
, 
64 GB
), 
M4 Pro
 (
14C+20C
, 
24 GB
)

• 
Zero-Copy Unified Memory Metal Shaders + ARM64 NEON/AMX
 (
238.9 GB/s
 DRAM BW on M4 Max)
• 
0
-Swap 
128K–256K
 Context Budgeting (
384 MB
 KV) + 
Stockfish-PVS v2

Apple Silicon Guide
Issue #8

ARM64 Cloud & Edge (
AWS Graviton / Ampere
)

AWS Graviton3 m7g.2xlarge
 (
8 vCPU Neoverse-V1
, 
32 MB
 L3)

• 
ARMv8.4-A DotProd (
SDOT
) + 256-Bit SVE
 + 1-vCPU-per-core pinning (
-t 8
)
• 
32 MB
 System Level Cache (
SLC
) retention (
44.97 tok/s
 decode)

Hardware Guide §1
Issue #2

AMD Zen 4 Compact Mini-PC (
Linux
)

Ryzen 7 8745H / 8745HS
 (
8C/16T
, 
16 MB
 L3 + 
Radeon 780M
)

• 
AVX-512 VNNI
 + 
16 MB
 L3 window auto-tuning (
19.48–23.38 tok/s
 on 
96 GB
 DDR5-5600)
• Optional 
Radeon 780M
 UMA iGPU offload

Fedora Guide
Issue #9

## Headline Benchmarks: Pure CPU & Hybrid Summary

### 1.DeepSeek-V4-Flash 284B(13.17BActive) on a64 GBZen 5 CPU (AMD Ryzen 9 9955HX,0 GPUs)

Operator-level profiling and mathematical derivations indocs/DEEPSEEK_V4_OPTIMIZATIONS.md(probabilities and KL-divergence measured relative to the unpatchedTop-6execution on the56.56 GiBFractal checkpoint):

Runtime Configuration (
DeepSeek-V4-Flash
, 
256K
 Context)

Prefill (
pp512
)

Pure Decode (
N=1
)

With 
Stockfish-PVS

Logit Cosine Sim

KL-Divergence (
$\Delta$
 PPL)

Top-1 / Top-3 Match

Unpatched 
UD-IQ1_S
 (
76.87 GiB
 / 
82.5 GB
)

OOM / Swap on 64 GB

5.91 tok/s
 (
169.3 ms
)

N/A 
(Rollback Bug)

1.00000
 
(Ref)

0.0000
 (
0.00%
)

100% / 100%

1. 
v2.4.0
 Lossless (
Top-6
 All Layers, Default, 
56.56 GiB
)

43.16 – 44.36 tok/s
 
(
+77.1%
)

9.06 – 9.95 tok/s

11.5 – 14.7 tok/s

1.00000

0.0000
 (
0.00%
 Bit-Exact)

100% / 100%

2. 
v2.4.0
 Sweet-Spot (
Top-5
 on 
il >= 3
, 
$L_2$
 Quadrature)

43.16 – 44.36 tok/s

9.68 – 9.87 tok/s

12.2 – 15.1 tok/s

0.99714

0.0042 nats
 (
+0.42%
 PPL)

95.8% / 100%

3. 
v2.4.0
 
Top-5 L2
 + Gate-First SwiGLU (
80/128
 
$L_2$
)

43.16 – 44.36 tok/s

10.15 tok/s
 (
98.5 ms
)

12.8 – 15.6 tok/s

0.99385

0.0531 nats

100% / 100%

4. 
v2.4.0
 Turbo 
10+
 (
Top-4 L2
 + Gate-First SwiGLU)

43.16 – 44.36 tok/s

10.12 – 10.74 tok/s
 (
93.2 ms
)

13.0 – 16.0 tok/s

0.99126

0.0281 – 0.0694 nats

100% / 100%

### 2.NVIDIA-Nemotron-3.5-30B-A3B(3.0BActive) at256KContext (AMD Ryzen 9 9955HX,0 GPUs)

Full ablation tables and100/100Quality Gate report indocs/NEMOTRON_OPTIMIZATIONS.md:

Quantization Profile

Disk Size

Idle 
VmRSS
 (
256K
)

Quality Gate (
100
 pts)

Prefill (
pp512
)

Base Decode (
N=1
)

Stockfish-PVS v2 (M=7)
 Refactoring

Baseline-Q4_0
 (
4.50 bpw
 Official GGUF)

17.59 GiB

21.41 GiB

100.0 / 100.0

241.0 – 306.8 tok/s

19.54 tok/s

40.91 avg / 45.43 peak tok/s

Fractal-MXFP4
 (
4.25 bpw
)

15.95 GiB

17.46 GiB

100.0 / 100.0

241.0 – 306.8 tok/s

26.08 tok/s
 (
+33.5%
)

48.39 avg / 60.40 peak tok/s
 
(
80.8
 Vulkan)

Fractal-64-BF16
 (
3.75 bpw
)

14.35 GiB

15.40 GiB
 (
-6.01 GiB
)

100.0 / 100.0

241.0 – 306.8 tok/s

25.02 tok/s
 (
+28.0%
)

48.39 avg / 60.40 peak tok/s
 
(
96.4%
 acc)

## Community CPU & Hybrid Leaderboard

Run./modchip bench(orwindows\BENCHMARK_PC.baton Windows) andSubmit Your Scorecard (GitHub Issue).

Hardware Platform (
CPU / SoC / Hybrid
)

Cores / Cache

Memory

Prefill (
tok/s
)

Decode — Prose / C++20

Decode — 
Stockfish M=7
 Burst

Config & Contributor

AMD Threadripper PRO 7985WX (
Zen 4
)

64C/128T
 (
8 CCDs
, 
256 MB
 L3)

256 GB
 8-Ch DDR5-6000 (
0 GPU
)

386.00
 
(
-t 32
)

73.84 – 80.14 tok/s
 
(
70.0%
 acc)

111.62 tok/s
 warm
 / 
80.14
 cold
 
(
-t 32
 4C/CCD)

@aifartist
 (
Issue #1
)

AMD Ryzen 9 7945HX3D + RX 9070 XT (
Hybrid
)

16C/32T
 (
128 MB
 3D V-Cache) + 
16 GB
 Vulkan

94 GB
 DDR5 + 
16 GB
 VRAM

563.00
 
(256K ctx)

75.10 tok/s
 
(
MXFP4
 15.2GB)

80.80 tok/s
 
(Vulkan 
SSM_SCAN
 + 
MXFP4
 MoE)

Community (RADV/Vulkan)
 (
FAQ.md
)

AMD Ryzen 9 9955HX (
Zen 5
)

16C/32T
 (
2 CCDs
, 
64 MB
 L3)

64 GB
 DDR5 (
0 GPU
)

241.0
 
(Peak 
306.8
)

25.02 – 34.5 tok/s
 
(
Fractal-64
 / 
MXFP4
)

48.39 avg / 60.40 peak
 
(
len 6.90
)

@synchopate
 (
docs/NEMOTRON_OPTIMIZATIONS.md
)

Apple M4 Max (
16C CPU + 40C GPU
)

16C
 (
ARM64 NEON
 + 
40C Metal
)

64 GB
 LPDDR5X-8533 (
238.9 GB/s
 BW)

~451.0
 
(Audit)

49.2 – 57.7 tok/s
 
(Prose / Code)

70.9 – 120.0 tok/s
 
(Agent / Refactor)

@jbeckman1974
 (
Issue #8
)

Apple M4 Pro (
14-Core SoC
)

14C CPU + 20C Metal

24 GB
 Unified (
0 Swap
)

256.0 – 549.0

47.0 – 48.0 tok/s
 
(128K)

49.0+ tok/s

@jarorosFork
 (
apple-silicon/
)

AWS Graviton3 
m7g.2xlarge
 (
ARM64 Neoverse-V1
)

8 vCPU
 (
32 MB
 L3, 
SVE-256
)

31 GB
 DDR5 (
0 GPU
)

101.67
 
(
-t 8
)

41.05 tok/s
 
(C++20)

44.97 tok/s
 
(Refactoring)

@gerchik
 (
Issue #2
)

AMD EPYC 7402P (
Zen 2 Rome
 · 
AVX2-only
)

24C/48T
 (
8 CCDs
, 
128 MB
 L3)

128 GB
 8-Ch DDR4 (
0 GPU
)

158.73
 
(
-t 24
)

27.29 tok/s
 
(C++20, 
567 ms
 TTFT)

31.22 tok/s
 
(Cold Run 1, 
66.7%
 acc)

@AdamKlob
 (
Issue #6
)

AMD Ryzen 9 9950X (
Zen 5 Desktop
)

16C/32T
 (
2 CCDs
, 
64 MB
 L3)

64 GB
 DDR5-6800 (
0 GPU
)

135.64
 
(v2.1 
Q4_0
)

20.78 tok/s
 
(C++20, 
526 ms
 TTFT)

24.67 tok/s
 
(Cold Run 1, 
66.5%
 acc)

@nadams
 (
Issue #5
)

AMD Ryzen 7 8745H w/ Radeon 780M (
Zen 4
)

8C/16T
 (
16 MB
 L3, 
AVX-512
)

96 GB
 DDR5-5600 (
0 GPU
, Arch)

128.81
 
(
-t 8
)

19.48 tok/s
 
(C++20, 
686 ms
 TTFT)

23.38 tok/s
 
(
69.8%
 PVS acc)

@arch-btw
 (
Issue #9
)

AMD Ryzen 5 7430U (
Zen 3 Mobile 15W
)

6C/12T
 (
16 MB
 L3, 
AVX2
)

32 GB
 DDR4-3200 (
0 GPU
, Pop!_OS)

59.03
 
(
-t 6
)

13.03 tok/s
 
(C++20, 
2072 ms
 TTFT)

15.57 tok/s
 
(
68.3%
 PVS acc)

@armadillu
 (
Issue #12
)

AMD Ryzen 7 5700U (
Zen 2 Mobile 15W
)

8C/16T
 (
8 MB
 L3, 
AVX2
)

64 GB
 DDR4 (
0 GPU
, Debian)

42.80
 
(
-t 8
)

12.92 tok/s
 
(C++20, 
1720 ms
 TTFT)

14.35 tok/s
 
(
66.5%
 PVS acc)

@JamesStallings
 (
Issue #10
)

Intel Core i9-11950H (
Tiger Lake-H
)

8C/16T
 (
24 MB
 L3, 
AVX-512
)

128 GB
 DDR4-3200 (
0 GPU
, Fedora)

85.39
 
(
-t 8
)

10.76 tok/s
 
(C++20, 
1106 ms
 TTFT)

13.37 tok/s
 
(
69.8%
 PVS acc)

@ELO-I
 (
Issue #11
)

Windows 11 Hybrid (
i9-9900K + RTX 2080 Ti 11GB
)

8C/16T
 (
16 MB
 L3) + 
11 GB
 CUDA

16 GB
 DDR4 + 
11 GB
 GDDR6

Auto CUDA 12.4

50–58 tok/s
 
(
14B
) / 30B Hybrid

100+ tok/s
 
(
Nemotron-H-8B
 128K)

windows/

AMD Ryzen 7 8745HS (
GEEKOM A8
)

8C/16T
 (
16 MB
 L3)

64 GB
 DDR5-5600

Verified Fedora 44

Verified (
ngram
)

Verified (
CPU
 & 
780M
)

@jarorosFork
 (
fedora/
)

DeepSeek-V4-Flash 284B
 on Ryzen 9 9955HX

16C/32T
 (
2 CCDs
, 
64 MB
 L3)

64 GB
 DDR5 (
58.9 GiB
 RSS @ 
256K
)

43.16 – 44.36 tok/s
 
(
32.6 ms
 Slot-0)

9.06 – 10.74 tok/s
 
(
13.17B
 active)

11.50 – 14.69 tok/s
 
(
94.5%
 PVS acc)

@synchopate
 (
docs/DEEPSEEK_V4_OPTIMIZATIONS.md
)

Repository Structure & Manual CMake Build Instructions

llama-modchip/
├── modchip # Unified CLI (setup | start | chat | bench | eval | quantize | web | claude | stop)
├── install.sh # Automated Installer (Linux)
├── README.md / ARCHITECTURE.md / FAQ.md # Overview, Full Mathematical Paper & Engineering FAQ
├── RELEASE_NOTES.md # v2.4.0 Release Notes
├── docs/
│ ├── NEMOTRON_OPTIMIZATIONS.md # Deep-dive on Nemotron-3.5-30B-A3B & Nemotron-H-8B optimizations
│ ├── DEEPSEEK_V4_OPTIMIZATIONS.md # Deep-dive on DeepSeek-V4-Flash 284B profiling, SVD & L2-quadrature MoE
│ └── HARDWARE_OPTIMIZATIONS.md # Chip-by-chip optimizations (Zen 5, Threadripper, Vulkan, CUDA, Metal, ARM64)
├── patches/
│ ├── deepseek-v4-flash-fractal-256k.patch # Unified v2.4.0 patch (DeepSeek-V4-Flash 284B + Nemotron-3.5 30B, Linux/macOS/Windows)
│ └── zen5-nemotron-256k-optimizations.patch # Standalone ggml/llama core patch for Nemotron-3.5
├── windows/ # Windows 10/11 Hybrid GPU+CPU MoE Pack (AVVIA_MODCHIP.bat, modchip_win.ps1)
├── apple-silicon/ # Apple M4 Pro (24 GB) Metal setup & 128K benchmarks
├── fedora/ # Fedora 44 / AMD Ryzen 7 8745HS (GEEKOM A8) all-in-one script
├── speculative/ # RouteCrack + Stockfish-PVS v2 (rc_stockfish.h, ngram-map.cpp)
├── benchmarks/ # eval_quality_and_tools.py (100-pt Quality Gate) & results/*.json
├── gateway/sse_gateway.py # Agentic SSE Proxy + Compact Tool Table + Dark-Mode Web Chat HUD (:8787)
└── scripts/ # build_fractal_moe_gguf.sh, transcode_dsv4.{c,py}, chat.py, llama_modchip.py

Nemotron Deep-Dive (docs/NEMOTRON_OPTIMIZATIONS.md)·DeepSeek-V4 284B Deep-Dive (docs/DEEPSEEK_V4_OPTIMIZATIONS.md)·Hardware & Chip Matrix (docs/HARDWARE_OPTIMIZATIONS.md)·Full Paper (ARCHITECTURE.md)·FAQ (FAQ.md)