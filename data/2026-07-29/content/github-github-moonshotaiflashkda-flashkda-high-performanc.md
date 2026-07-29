---
title: 'GitHub - MoonshotAI/FlashKDA: FlashKDA: high-performance Kimi Delta Attention kernels · GitHub'
url: https://github.com/MoonshotAI/FlashKDA
site_name: github
content_file: github-github-moonshotaiflashkda-flashkda-high-performanc
fetched_at: '2026-07-29T11:47:01.128351'
original_url: https://github.com/MoonshotAI/FlashKDA
author: MoonshotAI
description: 'FlashKDA: high-performance Kimi Delta Attention kernels - MoonshotAI/FlashKDA'
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 MoonshotAI

 

/

FlashKDA

Public

* NotificationsYou must be signed in to change notification settings
* Fork90
* Star888

 
 
 
master
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

9 Commits
9 Commits
benchmarks
benchmarks
 
 
csrc
csrc
 
 
cutlass @ 5c149f5
cutlass @ 5c149f5
 
 
docs
docs
 
 
flash_kda
flash_kda
 
 
tests
tests
 
 
.clangd.template
.clangd.template
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
BENCHMARK_GB200.md
BENCHMARK_GB200.md
 
 
BENCHMARK_H20.md
BENCHMARK_H20.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
config.yaml
config.yaml
 
 
setup.py
setup.py
 
 
setup_clangd.sh
setup_clangd.sh
 
 
View all files

## Repository files navigation

# FlashKDA

FlashKDA: Flash Kimi Delta Attention — high-performance KDA kernels built on CUTLASS

## News

* 2026-04-22— Deep-Dive Blog: the design decisions behind FlashKDA v1, read ithere.

## Requirements

* SM90 and above
* CUDA 12.9 and above
* PyTorch 2.4 and above

## Installation

git clone https://github.com/MoonshotAI/FlashKDA.git flash-kda

cd
 flash-kda
git submodule update --init --recursive
pip install -v --no-build-isolation 
.

By default, the build detects the current CUDA device and compiles for that architecture. For wheel or CI builds, compile all supported architectures explicitly:

FLASH_KDA_CUDA_ARCHS=all pip install -v --no-build-isolation 
.

Supported values areauto(default),all, or a comma-separated arch list such as90a,100a.

## Using FlashKDA as an FLA backend

Once installed, FlashKDA is auto-dispatched fromflash-linear-attention'schunk_kda. Seefla-org/flash-linear-attention#852for integration details.

Requirements

1. Installflash-linear-attention >= 0.5.0:pip install -U flash-linear-attention
2. Callchunk_kdaundertorch.inference_mode()importtorchfromfla.ops.kdaimportchunk_kdawithtorch.inference_mode():out,final_state=chunk_kda(q=q,k=k,v=v,g=g,beta=beta,scale=scale,initial_state=h0,output_final_state=True,use_gate_in_kernel=True,use_qk_l2norm_in_kernel=True,use_beta_sigmoid_in_kernel=True,safe_gate=True,A_log=A_log,dt_bias=dt_bias,lower_bound=lower_bound,transpose_state_layout=True,cu_seqlens=cu_seqlens,
 )

Opt out:setFLA_FLASH_KDA=0to fall back to the Triton path.

Debug dispatch:addlogging.basicConfig(level=logging.INFO)to see[FLA Backend] kda.chunk_kda -> flashkdaon hit, or... rejected: <reason>on miss.

## Performance

SeeBENCHMARK_H20.md.

## Tests

bash tests/test.sh

* tests/test_fwd.py— correctness tests (exact match against the torch reference; compared withflash-linear-attention)

## Kernel API

### flash_kda.fwd

flash_kda
.
fwd
(
q
, 
k
, 
v
, 
g
, 
beta
, 
scale
, 
out
, 
A_log
, 
dt_bias
, 
lower_bound
,
 
initial_state
=
None
, 
final_state
=
None
, 
cu_seqlens
=
None
)

Parameters:

Parameter

Dtype

Shape

Description

q

bf16

[B, T, H, K]

Query

k

bf16

[B, T, H, K]

Key

v

bf16

[B, T, H, V]

Value

g

bf16

[B, T, H, K]

Gate before activation

beta

bf16

[B, T, H]

Beta logits (pre-activation; sigmoid applied internally)

scale

float

scalar

scaling factor

out

bf16

[B, T, H, V]

Output tensor

A_log

fp32

[H]

Log-gate parameter

dt_bias

fp32

[H, K]

Gate bias

lower_bound

float

scalar

Gate lower bound (range from -5.0 to 0)

initial_state

bf16/fp32/None

[B, H, V, K]
 or 
[N, H, V, K]

(optional) Initial recurrent state

final_state

bf16/fp32/None

[B, H, V, K]
 or 
[N, H, V, K]

(optional, output) Final recurrent state

cu_seqlens

int64

[N+1]

(optional) Cumulative sequence lengths for variable-length batching

* Currently requiresK = V = 128.
* initial_state/final_stateacceptNone(stateless), bf16, or fp32 tensors. When both are provided, their dtypes must match.
* Whencu_seqlensis provided,Bmust be 1,Tis the total length across all sequences, andinitial_state/final_statehave shape[N, H, V, K].
* Whencu_seqlensisNone, each batch element is treated as an independent sequence, and the state shape is[B, H, V, K].

## Development

To set up IntelliSense (clangd) for the CUDA/C++ sources, run:

bash setup_clangd.sh

This generates a.clangdfile with the correct repository paths and installs the global clangdconfig.yamlto~/.config/clangd/.

## Citation

@misc
{
flashkda2026
,
 
title
=
{
FlashKDA: Flash Kimi Delta Attention
}
,
 
author
=
{
Yutian Chen, Zhiyuan Li, Yucheng Wang, Ming Wei
}
,
 
year
=
{
2026
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
\url{https://github.com/MoonshotAI/FlashKDA}
}
,
}