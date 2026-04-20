---
title: 'GitHub - danveloper/flash-moe: Running a big model on a small laptop · GitHub'
url: https://github.com/danveloper/flash-moe
site_name: hackernews_api
content_file: hackernews_api-github-danveloperflash-moe-running-a-big-model-on
fetched_at: '2026-03-22T19:12:55.650899'
original_url: https://github.com/danveloper/flash-moe
author: mft_
date: '2026-03-22'
description: Running a big model on a small laptop. Contribute to danveloper/flash-moe development by creating an account on GitHub.
tags:
- hackernews
- trending
---

danveloper



/

flash-moe

Public

* NotificationsYou must be signed in to change notification settings
* Fork103
* Star1k




 
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

144 Commits
144 Commits
docs
docs
 
 
metal_infer
metal_infer
 
 
paper
paper
 
 
.gitignore
.gitignore
 
 
CLAUDE.md
CLAUDE.md
 
 
README.md
README.md
 
 
expert_index.json
expert_index.json
 
 
progress.png
progress.png
 
 
progress.py
progress.py
 
 
repack_experts.py
repack_experts.py
 
 
results.tsv
results.tsv
 
 
View all files

## Repository files navigation

# Flash-MoE: Running a 397B Parameter Model on a Laptop

Read the paper— Full technical details, 90+ experiments, and the story of how an AI and a human built this in 24 hours.

Pure C/Metal inference engine that runsQwen3.5-397B-A17B(a 397 billion parameter Mixture-of-Experts model) on a MacBook Pro with 48GB RAM at4.4+ tokens/secondwith production-quality output including tool calling.

The entire 209GB model streams from SSD through a custom Metal compute pipeline. No Python. No frameworks. Just C, Objective-C, and hand-tuned Metal shaders.

## Results

Configuration

tok/s

Quality

Notes

4-bit experts, FMA kernel

4.36

Excellent

Current best. Full tool calling. 209GB on disk.

4-bit experts, baseline

3.90

Excellent

Before FMA kernel optimization.

2-bit experts, trust OS

5.74

Good*

120GB on disk. *Breaks JSON/tool calling.

2-bit peak single token

7.05

Good*

Warm cache burst. *Not suitable for tool use.

*2-bit quantization produces\name\instead of"name"in JSON output, making tool calling unreliable. 4-bit is the production configuration.

## Hardware

* Machine: MacBook Pro, Apple M3 Max
* Chip: 16-core CPU (12P + 4E), 40-core GPU, 16-core ANE
* Memory: 48 GB unified (~400 GB/s bandwidth)
* SSD: 1TB Apple Fabric,17.5 GB/s sequential read(measured)
* macOS: 26.2 (Darwin 25.2.0)

## Architecture

The model has 60 transformer layers: 45 GatedDeltaNet (linear attention) + 15 standard full attention. Each layer has 512 experts, of which K=4 are activated per token (plus one shared expert). Hidden dimension is 4096.

### Key Techniques

1. SSD Expert Streaming— Expert weights (209GB at 4-bit) are read from NVMe SSD on demand via parallelpread()with GCD dispatch groups. Only the K=4 active experts per layer are loaded (~6.75MB each). The OS page cache manages caching — no custom cache needed ("Trust the OS" principle). Inspired by Apple's "LLM in a Flash" paper.
2. FMA-Optimized Dequant Kernel— The inner loop of the 4-bit dequantized matrix-vector multiply rearranges the math from(nibble * scale + bias) * xtofma(nibble, scale*x, bias*x). Pre-computingscale*xandbias*xlets the GPU fused multiply-add unit do dequant+multiply in one instruction. 12% faster than the naive formulation.
3. Metal Compute Shaders— Hand-written Metal kernels for:* 4-bit and 2-bit dequantized matrix-vector multiply (tiled, SIMD-reduced, shared input cache, FMA-optimized)
* Fused SwiGLU activation
* RMS normalization (two-pass: sum-of-squares reduction + apply)
* Batched GPU attention (Q@K^T, softmax, scores@V) for full attention layers
* GPU RoPE (fused with Q deinterleave and K normalization)
* MoE combine + residual + sigmoid gate (fused kernel)
4. Deferred GPU Expert Compute— CMD3 (expert forward pass) is submitted without waiting. The GPU executes it while the CPU prepares the next layer. The combine + residual + norm are also on GPU, feeding directly into the next layer's attention projections.
5. Accelerate BLAS for Linear Attention— The GatedDeltaNet recurrence usescblas_sscal,cblas_sgemv, andcblas_sgerfor the 64-head × 128×128 state matrix update. 64% faster than scalar code.
6. Trust the OS— No custom expert cache. The OS page cache (~35GB) manages expert data caching via standard LRU. Every custom caching approach we tested (Metal LRU, malloc cache, LZ4 compressed cache) was slower due to GPU memory pressure or overhead. The page cache achieves ~71% hit rate naturally.

### Pipeline Per Layer (4.28ms average at 4-bit)

CMD3(prev) → CMD1: attention projections + delta-net [1.22ms GPU]
 → CPU: flush results [0.01ms CPU]
 → CMD2: o_proj + norm + routing + shared [0.55ms GPU]
 → CPU: softmax + topK routing [0.003ms]
 → I/O: parallel pread K=4 experts [2.41ms SSD]
 → CMD3: expert forward + combine + norm [0.04ms encode, DEFERRED]

### Unified Memory Constraint

On Apple Silicon, SSD DMA and GPU compute share the same memory controller and cannot be profitably overlapped. The GPU's dequant kernels are bandwidth-saturated at ~418 GiB/s. Even small background SSD DMA causes disproportionate GPU latency spikes through memory controller arbitration. The serial pipeline (GPU → SSD → GPU) is hardware-optimal.

## Quick Start

cd
 metal_infer
make

#
 4-bit inference (needs packed_experts/ directory)

./infer --prompt
"
Explain quantum computing
"
 --tokens 100

#
 2-bit inference (faster but breaks tool calling)

./infer --prompt
"
Explain quantum computing
"
 --tokens 100 --2bit

#
 Interactive chat with tool calling

./chat

#
 Per-layer timing breakdown

./infer --prompt
"
Hello
"
 --tokens 20 --timing

## Project Structure

metal_infer/
 infer.m # Complete inference engine (~7000 lines)
 shaders.metal # Metal compute kernels (~1200 lines)
 chat.m # Interactive chat TUI with tool calling
 tokenizer.h # C BPE tokenizer (single-header, 449 lines)
 main.m # MoE-only benchmark
 Makefile # Build system
 extract_weights.py # Creates model_weights.bin from safetensors
 repack_experts_2bit.py # 4-bit → 2-bit expert requantization
 train_predictor.py # Expert routing prediction analysis
 model_weights.bin # Non-expert weights (5.5GB, mmap'd)
 model_weights.json # Tensor manifest
 vocab.bin # Vocabulary for token decoding
 tokenizer.bin # Pre-exported BPE tokenizer data

repack_experts.py # 4-bit expert packing from safetensors
progress.py # Results visualization (Q2/Q4 tracks)
results.tsv # Experiment log (58 experiments)

## What We Tried (and What Worked)

### Kept

Approach

Result

Impact

FMA dequant kernel

GPU compute -12%

+12% tok/s

Trust OS page cache

Deleted Metal LRU → +38%

Foundational

GPU combine+norm in CMD3

Eliminates CPU round-trip

Pipeline

BLAS delta-net (Accelerate)

cpu_attn 0.78→0.28ms

+64% attn

F_NOCACHE for 2-bit

+3% from avoiding page thrash

2-bit only

GPU fused attention (RoPE)

+2% for full-attn layers

Small

C BPE tokenizer

180ms vs 3500ms startup

20x startup

Deferred CMD3 execution

GPU/CPU overlap

Pipeline

### Discarded (58 experiments, highlights)

Approach

Result

Why

LZ4 expert compression

-13%

Decompress overhead > warm cache savings

F_RDADVISE prefetch

net 0%

Unified memory: SSD DMA slows GPU -73%

Temporal expert prediction

-18%

25% hit rate, SSD bandwidth waste

MLP routing predictor

31% accuracy

Worse than temporal baseline

GPU LUT dequant kernel

-2%

Indirect register access serializes

GPU private buffer compression

-20% pipeline

Blit cost 4×7MB > matvec savings

Spin-poll GPU wait

-23%

CPU thermal competes with GPU

Expert file clustering

0%

NVMe ignores scatter at 7MB granularity

dispatch_io

-70%

dispatch_data management overhead

mmap expert files

-5x

Per-page fault overhead on cold data

Speculative early routing

-38%

Cache pollution + overhead

MTP speculative decoding

break-even

MoE I/O scales per-token (unlike dense)

## Safety

This is a primary development machine. The engine explicitly controls memory:

* Non-expert weights: 5.5GB (mmap'd, read-only)
* Metal scratch buffers: ~200MB
* Total: ~6GB, leaving 42GB for OS + page cache
* No OOM risk. Expert data streams from SSD on demand.
* No custom caches. Trust the OS.

## About

Running a big model on a small laptop

### Resources

 Readme



### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

1k

 stars


### Watchers

10

 watching


### Forks

103

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors2

* danveloperDan Woods
* claudeClaude

## Languages

* Objective-C59.4%
* C13.6%
* TeX9.7%
* Python8.7%
* Metal7.4%
* Shell0.8%
* Makefile0.4%
