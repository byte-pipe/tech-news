---
title: 'GitHub - robertcprice/nCPU: nCPU: model-native and tensor-optimized CPU research runtimes with organized workloads, tools, and docs · GitHub'
url: https://github.com/robertcprice/nCPU
site_name: hnrss
content_file: hnrss-github-robertcpricencpu-ncpu-model-native-and-tens
fetched_at: '2026-03-05T06:00:37.491669'
original_url: https://github.com/robertcprice/nCPU
date: '2026-03-04'
description: 'nCPU: model-native and tensor-optimized CPU research runtimes with organized workloads, tools, and docs - robertcprice/nCPU'
tags:
- hackernews
- hnrss
---

robertcprice



/

nCPU

Public

* NotificationsYou must be signed in to change notification settings
* Fork10
* Star284




 
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

10 Commits
10 Commits
assets
assets
 
 
benchmarks
benchmarks
 
 
demos
demos
 
 
docs
docs
 
 
examples
examples
 
 
kernels
kernels
 
 
models
models
 
 
ncpu
ncpu
 
 
paper
paper
 
 
programs
programs
 
 
tests
tests
 
 
training
training
 
 
.gitignore
.gitignore
 
 
README.md
README.md
 
 
main.py
main.py
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
View all files

## Repository files navigation

A CPU that runs entirely on GPU — registers, memory, flags, and program counter are all tensors.Every ALU operation is a trained neural network.Addition uses Kogge-Stone carry-lookahead. Multiplication uses a learned byte-pair lookup table.Bitwise ops use neural truth tables. Shifts use attention-based bit routing. No hardcoded arithmetic.

## Quick Start

pip install -e
"
.[dev]
"

#
 Run a program — all arithmetic through trained neural networks

python main.py --program programs/sum_1_to_10.asm

#
 Run with execution trace

python main.py --program programs/fibonacci.asm --trace

#
 Inline assembly

python main.py --inline
"
MOV R0, 42; HALT
"

#
 GPU tensor mode (maximum speed, native tensor ops)

python main.py --binary firmware.bin --fast

## How It Works

The entire CPU lives on GPU. Registers, memory, flags, and the program counter are
PyTorch tensors. Instruction decode, ALU dispatch, and state updates all happen on-device
— nothing round-trips to the host CPU. Every ALU operation routes through a trained.ptmodel:

Instruction

Neural Model

How It Works

ADD R0, R1, R2

arithmetic.pt + carry_combine.pt

Kogge-Stone CLA (8 neural passes)

SUB R0, R1, R2

arithmetic.pt + carry_combine.pt

Two's complement + CLA

MUL R0, R1, R2

multiply.pt

Byte-pair LUT lookups (up to 64 pairs for 64-bit)

DIV R0, R1, R2

arithmetic.pt

Restoring division via neural subtraction

AND R0, R1, R2

logical.pt

Vectorized truth table (all 32 bits at once)

OR R0, R1, R2

logical.pt

Vectorized truth table

XOR R0, R1, R2

logical.pt

Vectorized truth table

SHL R0, R1, 4

lsl.pt

Attention-based bit routing per output position

SHR R0, R1, 2

lsr.pt

Attention-based bit routing

CMP R0, R1

arithmetic.pt

Neural subtraction → derive N/Z/C flags

INC R0

arithmetic.pt

Neural add 1

DEC R0

arithmetic.pt

Neural subtract 1

Math functions (sin, cos, sqrt, exp, log, atan2) also wired through trained models.

Result: 100% accuracy on integer arithmetic, verified by 347 automated tests.

## Trained Model Inventory

23 models (~135 MB total), 13 actively wired:

Component

Model

Accuracy

Wired

ADD/SUB/INC/DEC

Kogge-Stone CLA (carry_combine + full adder)

100%

Yes

MUL

Byte-pair LUT [256×256×16]

100%

Yes

AND/OR/XOR

Neural truth tables [7×4]

100%

Yes

LSL

Decomposed shift network

100%

Yes

LSR

Decomposed shift network

100%

Yes

CMP

Neural subtraction

100%

Yes

sin/cos

Sine-activated deep network

Trained

Yes

sqrt

Two-stage with Newton refinement

Trained

Yes

exp/log

4-layer MLP

Trained

Yes

atan2

6-layer residual with BatchNorm

Trained

Yes

Decode LLM

Qwen2.5-Coder-1.5B LoRA

100%

Yes (real mode)

Seemodels/MODEL_INDEX.mdfor full details.

## Performance

Benchmarked on Apple Silicon (MPS backend, PyTorch 2.10.0), 1,000 iterations per operation:

Operation

Latency (mean)

Sequential Passes

Strategy

exp, log

21 us

1

Single-pass MLP

mul

21 us

1

Batched byte-pair LUT gather

and, or, xor

21 us

1

Vectorized truth table lookup

sin, cos

48 us

2

Sine-activated deep network

add, sub, cmp

248 us

8 (CLA)

Kogge-Stone carry-lookahead

shl, shr

434 us

3 (batched)

Vectorized attention routing

sqrt

522 us

2 + batch pad

Two-stage BatchNorm MLP

atan2

935 us

6 + batch pad

Residual BatchNorm network

All models load in60ms. Programs execute at136--262 us/cycledepending on instruction mix (~4,975 IPS).

#
 Run benchmarks

python benchmarks/benchmark_neural.py

## Key Findings

Multiplication is 12x faster than addition, even with carry-lookahead. In conventional CPUs,
MUL is slower than ADD. In the neural CPU, it's inverted: the byte-pair LUT (21 us) has zero
sequential dependency, while the CLA adder (248 us) requires O(log n) carry-combine stages.
Before CLA, the gap was 38x (826 us with 32 ripple-carry passes).

Carry-lookahead works in neural networks.The Kogge-Stone parallel-prefix algorithm,
using a trained carry-combine network (100% accuracy on all 16 inputs), reduced ADD/SUB/CMP
from ~826 us to ~248 us --- a3.3x speedup. Classical hardware design principles transfer
directly to neural architectures.

Vectorization recovers most of the attention cost.Shift operations went from ~2,833 us
(64 sequential passes) to ~434 us (3 batched passes) --- a6.5x speedup.

O(1) / O(log n) / O(n) hierarchy.Operations fall into three tiers: O(1) single-pass
lookups (~21 us), O(log n) parallel-prefix carry (~248 us), and O(n) sequential passes
(sqrt ~522 us, atan2 ~935 us).

See theresearch paperfor detailed analysis.

## GPU-Native Architecture

The NeuralCPU is not a simulator that happens to use a GPU — itisa GPU program.
All CPU state lives permanently on-device as PyTorch tensors:

* Registers: 31 x 64-bit (torch.int64on GPU)
* Memory: Flat byte-addressable (torch.uint8on GPU)
* Flags: N, Z, C, V as GPU-resident tensors
* Program Counter: GPU tensor, incremented on-device

The CPU is 64-bit ARM64. Registers, addresses, and data paths are all 64-bit.
Instruction fetch, decode, execute, and writeback all happen on GPU. The ALU is a bank
of trained neural networks running as GPU inference. No host CPU arithmetic in the
execution loop.

### Two Execution Modes

Neural Mode(default) — Every ALU operation is a forward pass through a trained.ptmodel:

from

ncpu
.
model

import

CPU

cpu

=

CPU
(
neural_execution
=
True
)

cpu
.
load_program
(
"MOV R0, 7
\n
MOV R1, 6
\n
MUL R2, R0, R1
\n
HALT"
)

cpu
.
run
()

print
(
cpu
.
get_register
(
"R2"
))
# 42 (computed by neural byte-pair LUT)

Fast Mode(--fast) — Same GPU-resident architecture, but ALU usestorch.add/torch.mulinstead of model inference. Targets1.35M IPSat batch_size=32768 on Apple Silicon MPS:

from

ncpu
.
neural

import

NeuralCPU

cpu

=

NeuralCPU
(
fast_mode
=
True
)
# Native GPU tensor ops

cpu
.
load_binary
(
arm64_binary
)

### Metal Compute Kernels

For maximum throughput, thekernels/directory contains native Metal GPU implementations
that run the entire ARM64 fetch-decode-execute loop on GPU withzero CPU-GPU synchronization:

* MLX Metal(kernels/mlx/): Python interface to custom Metal compute kernels via Apple MLX.
Full ARM64 decode and execute in Metal Shading Language.
* Rust Metal(kernels/rust_metal/): Direct Metal API viaobjc2-metalwith PyO3 Python
bindings. Includes GPU-side syscall handling, basic block caching, neural dispatch, and
out-of-order execution. Ships with a native DOOM benchmark.

## ISA

### Text Assembly (ncpu.model)

Instruction

Format

Description

MOV

MOV Rd, imm/Rs

Load immediate or copy register

ADD

ADD Rd, Rs1, Rs2

Neural addition

SUB

SUB Rd, Rs1, Rs2

Neural subtraction

MUL

MUL Rd, Rs1, Rs2

Neural multiplication

DIV

DIV Rd, Rs1, Rs2

Neural division (restoring algorithm)

AND

AND Rd, Rs1, Rs2

Neural bitwise AND

OR

OR Rd, Rs1, Rs2

Neural bitwise OR

XOR

XOR Rd, Rs1, Rs2

Neural bitwise XOR

SHL

SHL Rd, Rs, imm/Rn

Neural shift left

SHR

SHR Rd, Rs, imm/Rn

Neural shift right

INC

INC Rd

Neural increment

DEC

DEC Rd

Neural decrement

CMP

CMP Rs1, Rs2

Neural compare (sets flags)

JMP

JMP label

Unconditional jump

JZ/JNZ

JZ/JNZ label

Jump if zero / not zero

JS/JNS

JS/JNS label

Jump if negative / not negative

HALT

HALT

Stop execution

### ARM64 Binary (ncpu.neural)

Full ARM64 instruction set — real binary encoding. The NeuralCPU decodes and executes
real ARM64 instructions with GPU-resident state.

## Project Structure

nCPU/
├── ncpu/
│ ├── neural/ # Full GPU neural CPU (ARM64, 12K lines)
│ │ ├── cpu.py # NeuralCPU — all state on GPU as tensors
│ │ └── neural_alu_bridge.py # Routes ops through trained models
│ ├── model/ # Model-based CPU (text assembly)
│ │ ├── cpu.py # CPU orchestrator
│ │ ├── neural_ops.py # Loads and runs .pt models
│ │ └── architectures.py # All model class definitions
│ └── tensor/ # Tensor-based ARM64 kernel
├── kernels/
│ ├── mlx/ # MLX Metal compute kernels (Python + Metal Shading Language)
│ └── rust_metal/ # Rust Metal GPU kernel (objc2-metal + PyO3 bindings)
│ └── src/ # Full ARM64 execute loop in Metal, zero GPU-CPU sync
├── models/ # 23 trained .pt models
│ ├── alu/ # arithmetic, carry_combine, multiply, divide, logical, compare
│ ├── shifts/ # lsl, lsr, asr, rol
│ ├── math/ # sincos, sqrt, exp, log, atan2, doom_trig
│ ├── decode_llm/ # Qwen2.5 LoRA adapter
│ └── MODEL_INDEX.md # Complete model status
├── demos/ # DOOM raycaster and other demos
├── programs/ # Assembly programs (.asm)
├── tests/ # 347 tests
├── docs/ # Architecture docs (neural mode + tensor mode)
├── benchmarks/ # Performance benchmarks
├── paper/ # Research paper
└── main.py # CLI entry point

## DOOM Raycaster Demo

A DDA raycaster that runsall arithmetic through trained neural networks. Every ADD, SUB, MUL,
and CMP is a forward pass through a real.ptmodel.

#
 Neural mode — every op through trained models (~2.5 FPS)

python demos/doom_raycaster.py

#
 Fast mode — native Python arithmetic (~5,000 FPS)

python demos/doom_raycaster.py --fast

#
 Side-by-side comparison (verifies identical output)

python demos/doom_raycaster.py --both

Fixed-point arithmetic (scale 1024) keeps everything in 32-bit integers, matching the
nCPU's integer-only ISA. Both modes execute identical algorithms and produce identical
frame output — the only difference is whether arithmetic routes through neural networks.

## Tests

pytest tests/ -v

#
 347 tests: decode, programs, registry, state, neural ops (incl. CLA + batch),

#
 neural bridge, math ops, architecture forward-pass, division

## License

MIT

## About

nCPU: model-native and tensor-optimized CPU research runtimes with organized workloads, tools, and docs

### Resources

 Readme



### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

284

 stars


### Watchers

2

 watching


### Forks

10

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors2

* robertcprice
* claudeClaude

## Languages

* Python58.7%
* Rust40.9%
* Other0.4%
