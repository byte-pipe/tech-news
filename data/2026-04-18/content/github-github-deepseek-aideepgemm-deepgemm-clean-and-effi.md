---
title: 'GitHub - deepseek-ai/DeepGEMM: DeepGEMM: clean and efficient FP8 GEMM kernels with fine-grained scaling · GitHub'
url: https://github.com/deepseek-ai/DeepGEMM
site_name: github
content_file: github-github-deepseek-aideepgemm-deepgemm-clean-and-effi
fetched_at: '2026-04-18T11:33:49.671734'
original_url: https://github.com/deepseek-ai/DeepGEMM
author: deepseek-ai
description: 'DeepGEMM: clean and efficient FP8 GEMM kernels with fine-grained scaling - deepseek-ai/DeepGEMM'
---

deepseek-ai



/

DeepGEMM

Public

* NotificationsYou must be signed in to change notification settings
* Fork871
* Star6.4k




 
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

188 Commits
188 Commits
.github/
workflows
.github/
workflows
 
 
csrc
csrc
 
 
deep_gemm
deep_gemm
 
 
scripts
scripts
 
 
tests
tests
 
 
third-party
third-party
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CMakeLists.txt
CMakeLists.txt
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build.sh
build.sh
 
 
develop.sh
develop.sh
 
 
install.sh
install.sh
 
 
setup.py
setup.py
 
 
View all files

## Repository files navigation

# DeepGEMM

DeepGEMM is a unified, high-performance tensor core kernel library that brings together the key computation primitives of modern large language models — GEMMs (FP8, FP4, BF16), fused MoE with overlapped communication (Mega MoE), MQA scoring for the lightning indexer, HyperConnection (HC), and more — into a single, cohesive CUDA codebase. All kernels are compiled at runtime via a lightweight Just-In-Time (JIT) module, requiring no CUDA compilation during installation.

DeepGEMM leverages some concepts fromCUTLASSandCuTe, but avoids heavy reliance on their templates or algebras. The library is designed for simplicity, with only a limited number of core kernel functions, making it a clean and accessible resource for learning NVIDIA GPU kernel optimization techniques.

Despite its lightweight design, DeepGEMM's performance matches or exceeds expert-tuned libraries across various matrix shapes.

## News

* 2026.04.16: Mega MoE, FP8xFP4 GEMM, FP4 Indexer, PDL, faster JIT compilation and more.Performance comparison will be posted later.Please see#304for more details.
* Performance comparison will be posted later.
* Please see#304for more details.
* 2025.09.28: DeepGEMM now supports scoring kernels (weighted ReLU MQA logits) for the lightning indexer for DeepSeek v3.2.Please see#200for more details.
* Please see#200for more details.
* 2025.07.20: DeepGEMM now supports both SM90/SM100, and has a full refactor with a low-CPU-overhead JIT CPP module.NVRTC and post-compilation SASS optimization are all disabled.NVRTC will be supported later.As NVCC 12.9 will automatically do the FFMA interleaving, all post optimizations will be no longer supported.Please see#112for more details.
* NVRTC and post-compilation SASS optimization are all disabled.
* NVRTC will be supported later.
* As NVCC 12.9 will automatically do the FFMA interleaving, all post optimizations will be no longer supported.
* Please see#112for more details.
* 2025.05.14: DeepGEMM now offers weight gradient kernels for dense and MoE backward! See#95for details.
* 2025.05.07: DeepGEMM now supports NVRTC with up to 10x compilation speedup! See#94for details. Please useDG_JIT_USE_NVRTC=1to enable it (may have performance loss with some cases).
* 2025.04.18: DeepGEMM now achieves up to1550 TFLOPSon H800! See#74,#78,#81,#86and340d988for details.

## Quick start

### Requirements

* NVIDIA SM90 or SM100 architecture GPU
* Python 3.8 or higher
* Compilers with C++20 support
* CUDA Toolkit:CUDA 12.3 or higher for SM90We highly recommend 12.9 or higher for the best performanceCUDA 12.9 or higher for SM100
* CUDA 12.3 or higher for SM90We highly recommend 12.9 or higher for the best performance
* We highly recommend 12.9 or higher for the best performance
* CUDA 12.9 or higher for SM100
* PyTorch 2.1 or higher
* CUTLASS 4.0 or higher (could be cloned by Git submodule)
* {fmt}library (could be cloned by Git submodule)

### Development

#
 Submodule must be cloned

git clone --recursive git@github.com:deepseek-ai/DeepGEMM.git

cd
 DeepGEMM

#
 Link some essential includes and build the CPP JIT module

cat develop.sh
./develop.sh

### Installation

cat install.sh
./install.sh

Then, importdeep_gemmin your Python project, and enjoy!

## Interfaces

#### Notices

This library provides optimized GEMM kernels for NVIDIA GPUs with a naming convention:D = C + A @ B. The input shape layout is NT (non-transposed A, transposed B). While the SM90 implementation supports only the NT memory layout (row-major, col-major), the SM100 implementation supports all memory layouts (NT, TN, NN, TT). For example,fp8_gemm_ntwill do aD = C + A @ B.T

For both architectures, the LHS scaling factor is required to have a TMA-aligned and transposed layout. And the data format for the scaling factor of SM90 and SM100 is different:

* SM90 requires scaling factors in FP32 format.
* SM100 requires scaling factors in packedUE8M0format, which packs 4 UE8M0 into a singletorch.int.

Please note that operations like input transposition or FP8 casting must be handled separately by the user, please implement or fuse them into prior kernels independently. While the library provides some simple PyTorch utility functions, these may result in slower performance, but our primary focus is on optimizing the GEMM kernels themselves.

#### Normal dense GEMMs (non-grouped)

To perform a basic non-grouped FP8 GEMM, call thefp8_gemm_{nt, nn, tn, tt}function. For more details, please refer to the function documentation.

#### Grouped GEMMs (contiguous layout)

Unlike traditional grouped GEMMs in CUTLASS, DeepGEMM groups only the M-axis, while N and K must remain fixed. This design is tailored for scenarios where experts in an MoE model share the same shape. For training forward passes or inference prefilling, where each expert may process a varying number of tokens, we concatenate these tokens into a single tensor, referred to as the "contiguous" layout. Note that each expert segment must be aligned to the GEMM M block size (get_mk_alignment_for_contiguous_layout()). For more information, please refer to them_grouped_fp8_gemm_{nt, nn}_contiguousfunction documentation.

We also provide a K-axis-grouped API for MoE weight backward (with M and N must remain fixed), please refer tok_grouped_fp8_gemm_tn_contiguousfor more information.

#### Grouped GEMMs (masked layout)

During the inference decoding phase, when CUDA graph is enabled and the CPU is unaware of the number of tokens each expert receives, we support masked grouped GEMMs. By providing a mask tensor, the kernel computes only the valid portions.

Usem_grouped_fp8_gemm_nt_maskedfor this purpose and consult the relevant documentation. An example usage is to use the output of low-latency kernels fromDeepEPas input.

#### V3.2 MQA kernels for the indexer

The kernel family has two versions, non-paged (for prefilling) and paged (for decoding).
Take the non-paged versionfp8_mqa_logitsas an example. It has 6 inputs:

* q, E4M3 tensor with shape[seq_len, num_heads, head_dim]
* kv, E4M3 tensor (shaped as[seq_len_kv, head_dim]) with float SF (shaped as[seq_len_kv])
* weights, float tensor with shape[seq_len, num_heads]
* cu_seq_len_k_startandcu_seq_len_k_end, int tensor with shape[seq_len]
* clean_logits, whether to clean the unfilled logits into-inf

The output tensor is shaped as[seq_len, seq_len_kv], indicating token-to-token logits.
For each tokeniinq, it will iterate all tokensjfrom[cu_seq_len_k_start[i], cu_seq_len_k_end[i]),
and calculate the logitout[i, j]as:

kv_j

=

kv
[
0
][
j
, :]
*

kv
[
1
][
j
].
unsqueeze
(
1
)
# [head_dim]

out_ij

=

q
[
i
, :, :] @
kv_j

# [num_heads]

out_ij

=

out_ij
.
relu
()
*

weights
[
i
, :]
# [num_heads]

out_ij

=

out_ij
.
sum
()
# Scalar

For more details and the paged versionfp8_paged_mqa_logits, please refer totests/test_attention.py.

#### Mega MoE

Mega MoE fuses and overlaps EP dispatch, linear 1 (FP8xFP4), SwiGLU, linear 2 (FP8xFP4), and EP combine into a single mega-kernel, overlapping NVLink communication and tensor core computation. It requires multi-process launch with symmetric memory. Usage:

# Allocate symmetric memory buffer

# NOTES: requires PyTorch >= 2.9

buffer

=

deep_gemm
.
get_symm_buffer_for_mega_moe
(

group
,
num_experts
,
num_max_tokens_per_rank
,
num_topk
,
hidden
,
intermediate_hidden

)

# Transform weights (FP4 with UE8M0 SF) into the required layout

transformed_l1
,
transformed_l2

=

deep_gemm
.
transform_weights_for_mega_moe
(
l1_weights
,
l2_weights
)

# Copy inputs into the buffer before each call

# You may fuse these into previous kernels

buffer
.
x
[:
num_tokens
].
copy_
(
x_fp8
)

buffer
.
x_sf
[:
num_tokens
].
copy_
(
x_sf
)

buffer
.
topk_idx
[:
num_tokens
].
copy_
(
topk_idx
)

buffer
.
topk_weights
[:
num_tokens
].
copy_
(
topk_weights
)

# Run the fused mega MoE kernel

y

=

torch
.
empty
((
num_tokens
,
hidden
),
dtype
=
torch
.
bfloat16
,
device
=
'cuda'
)

deep_gemm
.
fp8_fp4_mega_moe
(
y
,
transformed_l1
,
transformed_l2
,
buffer
)

For the full example with multi-process setup and benchmarking, please refer totests/test_mega_moe.py.

#### Utilities

The library provides some utility functions besides the above kernels:

* deep_gemm.set_num_sms/get_num_sms: set/get the maximum SM count to use
* deep_gemm.set_tc_util/get_tc_util: set/get an approximated tensor core utilization ratio
* deep_gemm.set_pdl/get_pdl: enable/disable Programmatic Dependent Launch (PDL)
* deep_gemm.set_mk_alignment_for_contiguous_layout/get_mk_alignment_for_contiguous_layout: set/get the group-level M/K alignment for contiguous layout
* deep_gemm.get_theoretical_mk_alignment_for_contiguous_layout: get the theoretical minimum M/K alignment
* deep_gemm.set_ignore_compile_dims: configure dimensions to ignore during JIT compilation
* deep_gemm.set_block_size_multiple_of: constrain block sizes to be multiples of a given value
* deep_gemm.transform_sf_into_required_layout: transform scaling factors into the required layout
* deep_gemm.get_tma_aligned_size: get the required TMA alignment size
* deep_gemm.get_mn_major_tma_aligned_tensor: get a MN-major TMA-aligned tensor
* deep_gemm.get_mn_major_tma_aligned_packed_ue8m0_tensor: get a MN-major TMA-aligned tensor (with packing FP32 into UE8M0)
* deep_gemm.get_k_grouped_mn_major_tma_aligned_packed_ue8m0_tensor: K-grouped GEMM packing kernel

The library also provides some environment variables, which may be useful:

* GeneralDG_JIT_DEBUG:0or1, print JIT debugging information,0by defaultDG_PRINT_CONFIGS:0or1, print selected configs for each shape,0by default
* DG_JIT_DEBUG:0or1, print JIT debugging information,0by default
* DG_PRINT_CONFIGS:0or1, print selected configs for each shape,0by default
* JIT cacheDG_JIT_CACHE_DIR: string, cache directory for compiled kernels,$HOME/.deep_gemmby default
* DG_JIT_CACHE_DIR: string, cache directory for compiled kernels,$HOME/.deep_gemmby default
* Compiler selectionDG_JIT_USE_NVRTC:0or1, use NVRTC instead of NVCC (faster compilation, may have lower performance for some cases),0by defaultDG_JIT_NVCC_COMPILER: string, NVCC compiler path; defaults totorch.utils.cpp_extension.CUDA_HOMEDG_JIT_CPP_STANDARD: integer, C++ standard version,20by default
* DG_JIT_USE_NVRTC:0or1, use NVRTC instead of NVCC (faster compilation, may have lower performance for some cases),0by default
* DG_JIT_NVCC_COMPILER: string, NVCC compiler path; defaults totorch.utils.cpp_extension.CUDA_HOME
* DG_JIT_CPP_STANDARD: integer, C++ standard version,20by default
* Compiler outputDG_JIT_PRINT_COMPILER_COMMAND:0or1, print compilation commands,0by defaultDG_JIT_PTXAS_VERBOSE:0or1, show detailed PTXAS output,0by defaultDG_JIT_PTXAS_CHECK:0or1, assert no local memory usage in compiled kernels,0by defaultDG_JIT_PRINT_LOAD_TIME:0or1, print kernel load time,0by default
* DG_JIT_PRINT_COMPILER_COMMAND:0or1, print compilation commands,0by default
* DG_JIT_PTXAS_VERBOSE:0or1, show detailed PTXAS output,0by default
* DG_JIT_PTXAS_CHECK:0or1, assert no local memory usage in compiled kernels,0by default
* DG_JIT_PRINT_LOAD_TIME:0or1, print kernel load time,0by default
* Debug and profilingDG_JIT_WITH_LINEINFO:0or1, embed source line info for profiling tools,0by defaultDG_JIT_DUMP_ASM:0or1, dump both PTX and SASS,0by defaultDG_JIT_DUMP_PTX:0or1, dump PTX output,0by defaultDG_JIT_DUMP_SASS:0or1, dump SASS output,0by defaultDG_COMM_KERNEL_DEBUG:0or1, zero symmetric buffer before each Mega MoE call for debugging,0by defaultDG_USE_NVIDIA_TOOLS:0or1, skip internal profiling when running under external NVIDIA tools,0by default
* DG_JIT_WITH_LINEINFO:0or1, embed source line info for profiling tools,0by default
* DG_JIT_DUMP_ASM:0or1, dump both PTX and SASS,0by default
* DG_JIT_DUMP_PTX:0or1, dump PTX output,0by default
* DG_JIT_DUMP_SASS:0or1, dump SASS output,0by default
* DG_COMM_KERNEL_DEBUG:0or1, zero symmetric buffer before each Mega MoE call for debugging,0by default
* DG_USE_NVIDIA_TOOLS:0or1, skip internal profiling when running under external NVIDIA tools,0by default
* Build optionsDG_SKIP_CUDA_BUILD:0or1, skip CUDA extension build during installation,0by defaultDG_FORCE_BUILD:0or1, force local build instead of downloading pre-built wheels,0by defaultDG_JIT_USE_RUNTIME_API:0or1, use CUDA Runtime API for kernel loading (requires CUDA runtime >= 12.8),0by default
* DG_SKIP_CUDA_BUILD:0or1, skip CUDA extension build during installation,0by default
* DG_FORCE_BUILD:0or1, force local build instead of downloading pre-built wheels,0by default
* DG_JIT_USE_RUNTIME_API:0or1, use CUDA Runtime API for kernel loading (requires CUDA runtime >= 12.8),0by default

For additional examples and details, please refer tothe test codeor review the corresponding Python documentation.

## Acknowledgement

DeepGEMM is inspired by theCUTLASSproject. Thanks and respect to the developers!

## License

This code repository is released underthe MIT License.

## Citation

@misc
{
deepgemm2025
,

title
=
{
DeepGEMM: clean and efficient BLAS kernel library on GPU
}
,

author
=
{
Chenggang Zhao and Zhean Xu and Liang Zhao and Jiashi Li and Chenhao Xu and Anyi Xu and Shengyu Liu and Kexing Zhou and Kuai Yu
}
,

year
=
{
2025
}
,

publisher
 =
{
GitHub
}
,

howpublished
 =
{
\url{https://github.com/deepseek-ai/DeepGEMM}
}
,
}

## About

DeepGEMM: clean and efficient FP8 GEMM kernels with fine-grained scaling

### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

6.4k

 stars


### Watchers

60

 watching


### Forks

871

 forks


 Report repository



## Releases6

v2.1.1.post3

 Latest



Oct 15, 2025



+ 5 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Cuda48.9%
* C++35.9%
* Python15.0%
* Other0.2%
