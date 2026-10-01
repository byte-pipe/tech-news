---
title: 'GitHub - tile-ai/tilelang: Domain-specific language designed to streamline the development of high-performance GPU/CPU/Accelerators kernels · GitHub'
url: https://github.com/tile-ai/tilelang
site_name: github
content_file: github-github-tile-aitilelang-domain-specific-language-de
fetched_at: '2026-10-01T17:18:08.861431'
original_url: https://github.com/tile-ai/tilelang
author: tile-ai
description: Domain-specific language designed to streamline the development of high-performance GPU/CPU/Accelerators kernels - tile-ai/tilelang
---

tile-ai

 

/

tilelang

Public

* NotificationsYou must be signed in to change notification settings
* Fork811
* Star8k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,993 Commits
1,993 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.claude/
skills
.claude/
skills
 
 
.github
.github
 
 
3rdparty
3rdparty
 
 
benchmark
benchmark
 
 
cmake
cmake
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
images
images
 
 
maint
maint
 
 
src
src
 
 
testing
testing
 
 
tilelang
tilelang
 
 
.clang-format
.clang-format
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.pymarkdown
.pymarkdown
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
THIRDPARTYNOTICES.txt
THIRDPARTYNOTICES.txt
 
 
VERSION
VERSION
 
 
format.sh
format.sh
 
 
pyproject.toml
pyproject.toml
 
 
requirements-dev.txt
requirements-dev.txt
 
 
requirements-lint.txt
requirements-lint.txt
 
 
requirements-test-cuda.txt
requirements-test-cuda.txt
 
 
requirements-test-metal.txt
requirements-test-metal.txt
 
 
requirements-test-rocm.txt
requirements-test-rocm.txt
 
 
requirements-test.txt
requirements-test.txt
 
 
requirements.txt
requirements.txt
 
 
version_provider.py
version_provider.py
 
 
View all files

## Repository files navigation

# Tile Language

Documentation·Installation·Examples·Releases·Contributing·TileLang (Ascend 950)

Tile Language (tile-lang) is a concise domain-specific language designed to streamline the development of high-performance GPU/CPU/NPU kernels (e.g., GEMM, Dequant GEMM, FlashAttention, LinearAttention). By employing a Pythonic syntax with an underlying compiler infrastructure on top ofTVM, tile-lang allows developers to focus on productivity without sacrificing the low-level optimizations necessary for state-of-the-art performance.

## Latest News

* 2026-09-30 —Ascend 950 backend:TileLang now officially supports Huawei Ascend 950 NPUs with native code generation, automatic scheduling and synchronization, SIMD/SIMT vector programming, etc. Explore the Ascend examples for GEMM, FlashAttention, and more.
* 2026-08-04 —TileLang LSP open sourced:published a Language Server Protocol implementation for TileLang with inlay hints for buffer shapes, dtypes, scopes, and inferred layouts, plus hover details and precise diagnostics.
* 2026-08-03 —TileLang v0.1.13:shipped the multi-backend language dialect, source locations in compiler diagnostics, new CUDA and Metal hardware paths, and a broad set of correctness fixes. This release removes several legacy APIs; read the compatibility notes before upgrading.
* 2026-07-30 —SM120 NVF4 block-scaled MMA:added an optimized Blackwell path forT.mma_gemm_blockscaledand a corresponding SM120 example.
* 2026-07-28 —Metal 4 cooperative-tensor GEMM:added cooperative-tensorT.gemmsupport for Apple M5, while retaining the simdgroup fallback for unsupported shapes and systems.

Earlier news (2025–2026)

### 2026

* 2026-07-28 —Source-aware compiler diagnostics:carried Python source locations into TIRX and surfaced them in compiler errors.
* 2026-07-24 —Multi-backend language dialect:reorganized the language layer around shared semantics with static CUDA, ROCm, and Metal dialects.
* 2026-07-23 —Block-causal attention for dLLM:added fixed-length and variable-length block-causal attention examples for diffusion language models.
* 2026-07-22 —IR Lower Trace:introduced a debugging tool for inspecting IR changes across every compiler pass and the final code-generation step.
* 2026-07-22 —DeepSeek V3.2 sparse MLA backward:selected the launch width adaptively from the head-block size.
* 2026-07-21 —DeepSeek V3.2 top-k optimization:improved the sparse-attention top-k selector's memory access pattern, delivering approximately 1.9× higher performance in the reported benchmark.
* 2026-07-16 —Compiler pass timing:added profiling for compiler passes with a configurable reporting threshold.
* 2026-07-12 —IKET profiler integration:added CUDA timeline instrumentation and profiling support.
* 2026-07-08 —TileLang v0.1.12:added the LLVM backend, tile scheduler, backend registry, pass visualizer, and expanded Blackwell support.
* 2026-07-06 —Pass Visualizer:introduced a structure-tree browser for inspecting compiler transformations.
* 2026-06-26 —Cross-host CUDA binary cache:enabled compiled CUDA binaries to be reused across compatible hosts.
* 2026-06-24 —Tile scheduler:introduced persistent tile-scheduling primitives for kernel authors.
* 2026-06-24 —Backend CodeGen registry:moved device andhost CodeGendispatch behind a backend registry.
* 2026-06-18 —LLVM backend:added CPU lowering and execution through LLVM.
* 2026-06-18 —Arbitrary-layout TMA lowering:enabled TMA transfers for swizzled shared-memory layouts.
* 2026-06-16 —Pass Diff:added compiler-pass IR comparison for debugging lowering changes.
* 2026-06-08 —TileLang v0.1.11:expanded scan, pipeline, backend, CUDA, ROCm, and Metal functionality.
* 2026-05-25 —Scan operators:introduced tile-level scan primitives.
* 2026-05-25 —TileLang v0.1.10:broadened AMD and Blackwell support, added initial Metal GEMM, improved Windows packaging, and expanded autotuning.
* 2026-05-24 —CDNA4 MXFP4:added FP4 E2M1 matrix-core support for AMD gfx950.
* 2026-05-22 —Metal simdgroup GEMM:added the first MetalT.gemmpath usingsimdgroup_matrixMMA.
* 2026-05-20 —Cluster copies:introducedT.copy_clusterfor TMA multicast and SM-to-SM cluster transfers.
* 2026-05-20 —TMA gather/scatter:addedtile::gather4andtile::scatter4support.
* 2026-05-20 —Native SM75 MMA GEMM:added FP16, INT8, and INT4 tensor-core paths for Turing GPUs.
* 2026-05-20 —TIRX migration:moved TileLang IR usage to TVM's TIRX representation.
* 2026-05-11 —Parallel autotuning:added pipelined compilation, grouped compilation, and multi-GPU benchmarking.
* 2026-05-07 —DeepSeek V4 operators:added TileLang examples for DeepSeek V4 workloads.
* 2026-05-06 —Windows support:added complete Windows build and runtime support with cross-platform fixes.
* 2026-04-28 —MXFP8 grouped GEMM:added block-scaled grouped GEMM examples with transposed-B support on Blackwell.
* 2026-04-25 —HISA sparse-attention indexer:added hierarchical sparse-attention indexing examples.
* 2026-04-24 —Blackwell MXFP8 block-scaled GEMM:added MXFP8 block-scaled matrix multiplication on SM100.
* 2026-04-22 —TileLang v0.1.9:delivered CuTe DSL GEMM V2, Metal code generation improvements, and build-without-host-toolchain support.
* 2026-04-22 —RDNA3/RDNA3.5 WMMA:added WMMA lowering for AMD gfx11 GPUs.
* 2026-04-20 —INT4T.gemm:added INT4 matrix multiplication to the CUDA GEMM path.
* 2026-04-17 —CUDA source kernels:introducedT.CUDASourceCodeKernelfor embedding custom CUDA source.
* 2026-04-15 —AutoDD frozen regions:added__freeze__annotations to preserve selected code during automatic delta debugging.
* 2026-03-27 —TMA stores:added store support toT.tma_copy.
* 2026-03-24 —Two-SM Blackwell kernels:added two-SM TMA, TMEM, and TCGEN5 MMA support.
* 2026-03-23 —AMD RDNA4:upgraded the ROCm path and added RDNA4 GPU support.
* 2026-03-22 —FlashAttention on SM100:added Blackwell FlashAttention examples.
* 2026-03-18 —Producer-consumer warp specialization:added automatic warp-specialized pipelines and theT.tma_copyAPI.
* 2026-03-12 —Eager-mode autotuning:enabled the autotuner with eager JIT kernels.
* 2026-03-10 —CPUT.gemm:added matrix multiplication support for the CPU target.
* 2026-03-05 —IR dump configuration:added a TileLang pass configuration for dumping intermediate IR.
* 2026-02-28 —CUDA cluster primitives:added cluster launch, query, synchronization, and barrier operations.
* 2026-02-28 —TCGEN5 MMA tensor-shared path:added the tensor-memory/shared-memory Blackwell GEMM path.
* 2026-02-24 —Host-toolchain-free builds:enabled installation without a host C/C++ toolchain when supported artifacts are available.
* 2026-02-23 —CuTe DSL GEMM V2:added SM90 and SM100 GEMM V2 support to the CuTe DSL backend.
* 2026-02-16 —TileLang v0.1.8:shipped dynamic pipeline improvements, logging documentation, richer layout representations, and AMD fixes.
* 2026-02-14 —Cross-CUDA release wheels:unified multiple CUDA versions behind a single wheel.
* 2026-02-14 —Hierarchical reductions:added hierarchical and warp-level reduction intrinsics.
* 2026-02-09 —CUDA runtime stubs:added lazy-loading CUDART and NVRTC stubs for CUDA 11, 12, and 13 compatible wheels.
* 2026-02-08 —Layout visualization improvements:improved rendering and inspection of TileLang layouts.
* 2026-02-02 —TileLang Puzzles:published ten progressively harder exercises for learning TileLang interactively.

### 2025

* 2025-12-18 —CuTe DSL backend:added compilation through NVIDIA CUTLASS CuTe DSL; follow ongoing work inissue #1454.
* 2025-12-17 —Z3 integration:integrated SMT-based symbolic reasoning into the TVM arithmetic analyzer.
* 2025-10-31 —Apache TVM FFI migration:moved the runtime interface toapache-tvm-ffito reduce host-side overhead.
* 2025-10-30 —TileLang v0.1.6.post2:published the final TileLang release compatible with Python 3.8.
* 2025-10-07 —Apple Metal backend:introduced Metal device support for Apple silicon.
* 2025-09-29 —Huawei Ascend adapters:published AscendC and Ascend NPU IR backend work in the external TileLang Ascend project.
* 2025-07-04 —2:4 sparse tensor cores:introducedT.gemm_spfor structured-sparse matrix multiplication.
* 2025-06-05 —NVRTC execution backend:added an NVRTC path to reduce compilation time for generated CUDA templates.
* 2025-04-14 —FlashMLA on AMD MI300X:published the optimized AMD implementation and accompanying documentation.
* 2025-03-03 —MLA decoding on H100:published the compact TileLang implementation, benchmarks, and optimization walkthrough.
* 2025-02-15 —WebGPU code generation:added the initial WebGPU backend.
* 2025-02-12 —TileLang v0.1.0:published the first v0.1 public release.
* 2025-02-10 —Debugging and layout tools:addedT.printand fragment-layout visualization workflows.
* 2025-01-20 —TileLang open sourced:made the project publicly available.

Seeall releasesfor complete changelogs and compatibility notes.

## Platform and Backend Support

TileLang is evolving into a multi-backend compiler (TileLang-X) built around a modular backend abstraction. See thebackend architecturefor the design, or ask a coding agent to use thebackend integration skillwhen porting TileLang to a new backend.

The currently supported backends are listed below.Primaryidentifies TileLang's core backend, whileSupportedandExperimentalbackends are implemented in the main repository.Ecosystemadapters live in separate repositories, are not included in TileLang release wheels, and may follow independent compatibility schedules. Prebuilt wheels are available for Linux x86-64/AArch64, Windows x86-64, and macOS arm64.

TileLang usesTargetobjects to represent compilation targets. The defaultautotarget detects CUDA, HIP, Metal, and Ascend devices; select an explicit target when compiling for another backend or architecture. See thetarget guidefor target syntax, architecture options, and backend-specific notes, or the corresponding adapter repository for installation and tested-device details.

Backend

Target

Platforms and hardware

Support level

Notes

NVIDIA CUDA

cuda

Linux x86-64/AArch64, Windows x86-64; code paths from SM70 through SM120

Primary

Release wheels and CI coverage; TMA, WGMMA, and TMEM features require the corresponding GPU architecture.

AMD ROCm/HIP

hip

Linux; CDNA and RDNA GPUs, including gfx942/gfx950 paths

Supported

Included in Linux wheels; a ROCm runtime is required. CI runs on a self-hosted gfx942 (MI300X) runner; gfx950 is not yet covered.

Huawei Ascend 950

ascend

Linux; Ascend 950 NPUs

Supported

Build from source with 
USE_ASCEND=ON
; requires CANN and 
torch_npu
. See the 
Ascend guide
.

Apple Metal

metal

macOS on Apple silicon

Supported

Release wheels and CI coverage; Metal 4 cooperative tensors are available on supported M5 systems.

LLVM CPU

llvm

Host CPUs

Experimental

Build from source with 
USE_LLVM=ON
; LLVM 15 or newer is required.

NVIDIA CuTe DSL

cutedsl

NVIDIA GPUs

Experimental

Requires 
nvidia-cutlass-dsl
.

WebGPU

webgpu

WebGPU runtimes

Experimental

Code generation and runtime integration are still evolving.

Huawei Ascend A2/A3

ascendc
 / 
pto
 / 
npuir

Ascend A2 and A3

Ecosystem

Developed in 
tilelang-ascend
 and the MLIR-based 
tilelang-mlir-ascend
.

MetaX MACA

maca

MetaX C500 and C600

Ecosystem

Developed in 
tilelang-metax
; requires the MACA software stack.

Moore Threads MUSA

musa

S5000, S4000, and M1000

Ecosystem

Developed in 
tilelang-musa
 and released independently.

HYGON

hcu

Linux; BW1000, BW1100, BW150 and K100_AI

Ecosystem

Developed in 
tilelang-hygon
; requires the DTK software stack.

Sunrise-AI TANG

tang

Sunrise S2 and S3

Ecosystem

Developed in 
tilelang-sunrise
. The TANG software stack is required.

## Installation

Install the latest stable release from PyPI:

pip install tilelang

Verify the installation:

python -c 
"
import tilelang; print(tilelang.__version__)
"

Nightly wheels provide recent features and fixes before the next stable release:

pip install tilelang --find-links https://tile-ai.github.io/whl/nightly

On AMD GPUs the same Linux wheels work out of the box: install a ROCm build of PyTorch first (e.g.pip install torch --index-url https://download.pytorch.org/whl/rocm7.0), thenpip install tilelang. A host ROCm installation is required at runtime; see theROCm notesin the installation guide.

Nightly builds may be less stable than official releases. For source builds, editable installs, Docker, ROCm setup, pip-provided CUDA toolchains, or a custom TVM checkout, follow the completeinstallation guide.

## Quick Start

The following example defines, compiles, runs, and verifies an FP16 GEMM kernel with FP32 accumulation and a fused ReLU epilogue. It uses PyTorch CUDA tensors; PyTorch uses the samecudadevice name on ROCm systems. TileLang selects the target automatically from the current environment.

import
 
torch

import
 
tilelang

import
 
tilelang
.
language
 
as
 
T

@
tilelang
.
jit

def
 
matmul_relu
(
A
, 
B
, 
block_M
: 
int
 
=
 
128
, 
block_N
: 
int
 
=
 
128
, 
block_K
: 
int
 
=
 
32
):
 
M
, 
N
, 
K
 
=
 
T
.
const
(
"M, N, K"
)
 
A
: 
T
.
Tensor
((
M
, 
K
), 
T
.
float16
)
 
B
: 
T
.
Tensor
((
K
, 
N
), 
T
.
float16
)
 
C
 
=
 
T
.
empty
((
M
, 
N
), 
T
.
float16
)

 
with
 
T
.
Kernel
(
T
.
ceildiv
(
N
, 
block_N
), 
T
.
ceildiv
(
M
, 
block_M
), 
threads
=
128
) 
as
 (
bx
, 
by
):
 
A_shared
 
=
 
T
.
alloc_shared
((
block_M
, 
block_K
), 
T
.
float16
)
 
B_shared
 
=
 
T
.
alloc_shared
((
block_K
, 
block_N
), 
T
.
float16
)
 
C_local
 
=
 
T
.
alloc_fragment
((
block_M
, 
block_N
), 
T
.
float32
)

 
T
.
clear
(
C_local
)
 
for
 
k
 
in
 
T
.
Pipelined
(
T
.
ceildiv
(
K
, 
block_K
), 
num_stages
=
3
):
 
T
.
copy
(
A
[
by
 
*
 
block_M
, 
k
 
*
 
block_K
], 
A_shared
)
 
T
.
copy
(
B
[
k
 
*
 
block_K
, 
bx
 
*
 
block_N
], 
B_shared
)
 
T
.
gemm
(
A_shared
, 
B_shared
, 
C_local
)

 
for
 
i
, 
j
 
in
 
T
.
Parallel
(
block_M
, 
block_N
):
 
C_local
[
i
, 
j
] 
=
 
T
.
max
(
C_local
[
i
, 
j
], 
0
)

 
T
.
copy
(
C_local
, 
C
[
by
 
*
 
block_M
, 
bx
 
*
 
block_N
])

 
return
 
C

M
 
=
 
N
 
=
 
K
 
=
 
1024

a
 
=
 
torch
.
randn
((
M
, 
K
), 
device
=
"cuda"
, 
dtype
=
torch
.
float16
)

b
 
=
 
torch
.
randn
((
K
, 
N
), 
device
=
"cuda"
, 
dtype
=
torch
.
float16
)

c
 
=
 
matmul_relu
(
a
, 
b
)

torch
.
testing
.
assert_close
(
c
, 
torch
.
relu
(
a
 @ 
b
), 
rtol
=
1e-2
, 
atol
=
1e-2
)

print
(
"GEMM + ReLU passed."
)

@tilelang.jitspecializes the kernel for the input shape and compile-time arguments on first use.T.Pipelinedstages global-to-shared transfers,T.gemmmaps the tile operation to the target backend, andT.Parallelexpresses the elementwise ReLU epilogue. Continue with thelanguage basics, then explore theGEMM examplesfor layouts, autotuning, and architecture-specific optimizations.

## Examples

* Start here:quickstartandelementwise kernels
* GEMM and quantization:GEMM,grouped GEMM,FP8 GEMM,dequantization GEMM, andblock-scaled GEMM
* Attention and sequence models:FlashAttention,Flash Decoding,block-sparse attention,linear attention, andGDN
* Model workloads:DeepSeek MLA,DeepSeek V3.2,DeepSeek V4, andDeepSeek mHC
* Architecture-specific kernels:AMD,TCGEN05, andSM120
* Compiler and debugging tools:analyzer,layout visualization,AutoDD, andIKET

Browse thecomplete examples directoryfor additional operators, tests, and architecture-specific implementations.

## Benchmark Summary

TileLang achieves exceptional performance across a variety of computational patterns. Comprehensive benchmark scripts and settings are available attilelang-benchmark. Below are selected results showcasing its capabilities:

* MLA Decoding Performance on H100
* Flash Attention Performance on H100
* Matmul Performance on GPUs (RTX 4090, A100, H100, MI300X)
* Dequantize Matmul Performance on A100

## Join the Discussion

Welcome to join our Discord community for discussions, support, and collaboration!

## Acknowledgments

We would like to express our gratitude to theTVMcommunity for their invaluable contributions. The initial version of this project was mainly developed byLeiWang1999,chengyupkuandnox-410with supervision from Prof.Zhi Yangat Peking University. Part of this work was carried out during an internship at Microsoft Research, where Dr. Lingxiao Ma, Dr. Yuqing Xia, Dr. Jilong Xue, and Dr. Fan Yang offered valuable advice and support. We deeply appreciate their mentorship and contributions.