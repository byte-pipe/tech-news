---
title: GitHub - robertcprice/nCPU: nCPU: model-native and tensor-optimized CPU research runtimes with organized workloads, tools, and docs · GitHub
url: https://github.com/robertcprice/nCPU
date: 2026-03-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-05T06:01:27.978978
---

# GitHub - robertcprice/nCPU: nCPU: model-native and tensor-optimized CPU research runtimes with organized workloads, tools, and docs · GitHub

# nCPU – Neural‑CPU Runtime on GPU

## Overview
- Implements a full 64‑bit ARM64 CPU entirely on GPU using PyTorch tensors for registers, memory, flags, and program counter.
- All ALU operations are performed by trained neural network models; no host‑CPU arithmetic is used during execution.
- Provides both **Neural Mode** (model inference for each instruction) and **Fast Mode** (native tensor ops) for different performance needs.

## Quick Start
- Install in editable mode: `pip install -e ".[dev]"`.
- Run a program: `python main.py --program programs/sum_1_to_10.asm`.
- Enable execution trace: `python main.py --program programs/fibonacci.asm --trace`.
- Inline assembly: `python main.py --inline "MOV R0, 42; HALT"`.
- Maximum speed (GPU tensor mode): `python main.py --binary firmware.bin --fast`.

## How It Works
- CPU state lives on GPU as PyTorch tensors:
  - 31 × 64‑bit registers (`torch.int64`), flat byte‑addressable memory (`torch.uint8`), flag tensors, and a tensor‑based program counter.
- Instruction decode, ALU dispatch, and state updates are performed on‑device.
- Each instruction routes through one or more neural models (e.g., `arithmetic.pt`, `multiply.pt`, `logical.pt`).

### Example Mapping
| Instruction | Neural Model(s) | Core Technique |
|-------------|----------------|----------------|
| ADD / SUB / INC / DEC | `arithmetic.pt` + `carry_combine.pt` | Kogge‑Stone carry‑lookahead (8 passes) |
| MUL | `multiply.pt` | Byte‑pair lookup table (up to 64 pairs) |
| DIV | `arithmetic.pt` | Restoring division via neural subtraction |
| AND / OR / XOR | `logical.pt` | Vectorized truth‑table lookup |
| SHL / SHR | `lsl.pt` / `lsr.pt` | Attention‑based bit routing |
| CMP | `arithmetic.pt` | Neural subtraction → flag generation |
| Math functions (sin, cos, sqrt, exp, log, atan2) | Dedicated trained models | Various deep‑network architectures |

- Achieves 100 % accuracy on integer arithmetic, verified by 347 automated tests.

## Model Inventory
- 23 neural models (~135 MB total); 13 are actively wired for core ISA operations.
- Includes models for arithmetic, logical ops, shifts, comparisons, and common math functions.
- Decode LLM uses `Qwen2.5‑Coder‑1.5B` LoRA, achieving 100 % accuracy in “real mode”.

## Performance (Apple Silicon, MPS backend)
| Operation | Mean Latency | Passes | Strategy |
|-----------|--------------|--------|----------|
| exp, log | 21 µs | 1 | Single‑pass MLP |
| mul | 21 µs | 1 | Batched byte‑pair LUT |
| and, or, xor | 21 µs | 1 | Vectorized truth table |
| sin, cos | 48 µs | 2 | Deep sine‑activated network |
| add, sub, cmp | 248 µs | 8 | Kogge‑Stone CLA |
| shl, shr | 434 µs | 3 | Batched attention routing |
| sqrt | 522 µs | 2+pad | Two‑stage MLP with Newton refinement |
| atan2 | 935 µs | 6+pad | Residual BatchNorm network |

- Model loading time: ~60 ms.
- Program execution: 136–262 µs per cycle (≈4,975 IPS) depending on instruction mix.

### Key Findings
- Multiplication (byte‑pair LUT) is ~12× faster than addition (carry‑lookahead), opposite of conventional CPUs.
- Carry‑lookahead via Kogge‑Stone reduces ADD/SUB/CMP latency from ~826 µs to ~248 µs (3.3× speedup).
- Vectorized attention reduces shift latency from ~2,833 µs to ~434 µs (6.5× speedup).
- Operations fall into O(1), O(log n), and O(n) latency tiers, mirroring classic algorithmic complexity.

## GPU‑Native Architecture
- No host‑CPU round‑trips; the entire fetch‑decode‑execute loop runs on GPU.
- Two execution modes:
  1. **Neural Mode** – every ALU operation uses model inference (`neural_execution=True`).
  2. **Fast Mode** – ALU uses native tensor ops (`torch.add`, `torch.mul`) for up to 1.35 M IPS at batch size 32,768.

### Metal Compute Kernels
- Native Metal implementations (`kernels/mlx/` and `kernels/rust_metal/`) provide zero‑CPU‑GPU synchronization.
- Includes full ARM64 decode/execute in Metal Shading Language and a DOOM benchmark.

## Instruction Set Architecture (ISA)
- Text assembly syntax (`ncpu.model`) supports typical ARM‑like instructions: MOV, ADD, SUB, MUL, DIV, AND, OR, XOR, SHL, SHR, INC, DEC, CMP, JMP, conditional jumps (JZ/JNZ, JS/JNS), and HALT.
- Binary ARM64 execution via `ncpu.neural` for loading pre‑compiled binaries.

## Resources
- Repository structure includes benchmarks, demos, docs, examples, kernels, models, programs, tests, and training scripts.
- Detailed model list in `seemodels/MODEL_INDEX.md`.
- Full research analysis available in the accompanying paper.
