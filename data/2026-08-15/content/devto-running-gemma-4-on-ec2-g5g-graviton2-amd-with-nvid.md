---
title: 'Running Gemma 4 on EC2 G5g: Graviton2 AMD with NVIDIA GPU - DEV Community'
url: https://dev.to/gde/running-gemma-4-on-ec2-g5g-graviton2-amd-with-nvidia-gpu-25ci
site_name: devto
content_file: devto-running-gemma-4-on-ec2-g5g-graviton2-amd-with-nvid
fetched_at: '2026-08-15T04:02:46.696522'
original_url: https://dev.to/gde/running-gemma-4-on-ec2-g5g-graviton2-amd-with-nvidia-gpu-25ci
author: xbill
date: '2026-08-13'
description: A field report on serving Gemma 4 E2B under vLLM on AWS G5g — the only aarch64 + SM 7.5 hardware there is. No published build covers that combination, AWS quietly solves half of it, and the thing that actually blocks you is 64 KiB of shared memory. Tagged with aws, vllm, cuda, machinelearning.
tags: '#aws, #vllm, #cuda, #machinelearning'
---

A field report on serving Google's Gemma 4 E2B on AWS EC2 **G5g* — a Graviton2 (aarch64)host with an NVIDIAT4G(Turing, SM 7.5) GPU. Three obstacles: anarch listnobodypublishes for this combination, aversion floorthat only the newest vLLM clears, and64 KiB of shared memorythat stops the model dead. Plus the seven things I documentedwrong before I had a box.*

Model

google/gemma-4-E2B-it
 (reference bf16 release)

Hardware

AWS EC2 
g5g.4xlarge
 — Graviton2 + 1x NVIDIA T4G, compute capability 
7.5
, 15,360 MiB

Base image

Deep Learning ARM64 AMI OSS Nvidia Driver GPU PyTorch 2.12 (Ubuntu 24.04)

Software

torch 2.12.0+cu132 · CUDA 13.2 · vLLM v0.27.2rc0 built from source for 
sm_75

Result

43.1 tok/s
 single-stream greedy, 329,579-token KV cache — after one patch to vLLM

G5g is the only instance AWS has ever shipped that puts an NVIDIA GPU behind a Gravitonhost. It launched in 2020, it never got a successor, and Graviton is now on its fifthgeneration without one.

That matters more than it sounds. The Arm-plus-CUDA world moved on to NVIDIA's own Arm CPU— Grace, paired with SM 9.0 and 10.0 parts. Turing stayed well supported, on x86. G5g isthe only hardware that is aarch64andcompute capability 7.5, and almost nobody publishesa build for that combination.

I put a rig on one anyway.The packaging problem was the quick part.Everything after it— a compiler that was not there, a version floor I did not expect, and 32 KiB of sharedmemory — took far longer, because none of it fails where you are looking.

## No published build covers aarch64 and SM 7.5 together

Start with the obvious candidate.vllm/vllm-openai:v0.27.1publishes both platforms underone tag, and you can read the arch lists straight out of the image config without pulling alayer:

docker buildx imagetools inspect vllm/vllm-openai:v0.27.1 
--format
 
'{{json .Image}}'

Enter fullscreen mode

Exit fullscreen mode

linux/amd64 7.5 8.0 8.6 8.9 9.0 10.0 12.0
linux/arm64 8.0 8.7 8.9 9.0 10.0 11.0 12.0

Enter fullscreen mode

Exit fullscreen mode

The one architecture this hardware needs is the only entry the two images disagree on. Thearm64 list is Ampere and up, because that is what ships as an Arm-plus-NVIDIA system: A100,Jetson Orin, GH200, Blackwell. Turing is not on that list and never will be.

Normally a missing target degrades to JIT from embedded PTX. Not here. The Dockerfile saysso, with a comment:

# Do not add +PTX here: vLLM filters torch's top-level PTX flag when it

# converts global gencode flags into per-kernel arch lists.

Enter fullscreen mode

Exit fullscreen mode

So it does not run slowly. It fails outright, withno kernel image is available forexecution on the device.

The rest of the ecosystem splits the same way. Check before you plan anything:

Artifact

7.5 on arm64

State

vllm/vllm-openai
 arm64

no

Current. Never had it.

nvcr.io/nvidia/pytorch
 arm64

through 24.10

Dropped by 24.12.

drikster80/vllm-aarch64

yes

Abandoned Sept 2024. vLLM 0.6.1, far too old for Gemma 4.

PyPI torch aarch64

no

Built for 9.0 / 10.0 / 12.0.

AWS ARM64 GPU DLAMI

yes

Maintained. PyTorch 2.2 through 2.12.

## AWS ships the one PyTorch that still has Turing

This is the finding that saves the whole exercise, and I nearly wrote it off. I had assumedPyTorch's aarch64 CUDA wheels lackedsm_75and that a from-source PyTorch build wascoming. That is true of the PyPI wheels. It is not true of AWS.

Read on two different DLAMIs, on the box:

torch
 
2.7
.
0
+
cu128
 
[
'
sm_75
'
,
 
'
sm_90
'
,
 
'
sm_100
'
,
 
'
sm_120
'
]

torch
 
2.12
.
0
+
cu132
 
[
'
sm_75
'
,
 
'
sm_80
'
,
 
'
sm_90
'
,
 
'
sm_100
'
,
 
'
sm_110
'
,
 
'
sm_120
'
]

Enter fullscreen mode

Exit fullscreen mode

AWS sells G5g, so AWS keeps Turing in the build — right through PyTorch 2.12 on CUDA 13.2,an image cut three months ago.PyTorch never needs building.Only vLLM's own kernels do,and CMake takes the arch list without argument:

-- CUDA target architectures: 7.5
CMake Warning: Pytorch version 2.11.0 expected for CUDA build, saw 2.12.0 instead.

Enter fullscreen mode

Exit fullscreen mode

That warning is worth reading twice, and I come back to it below.

## The PyTorch DLAMI has no compiler

Two things the DLAMI does not give you, neither of them documented anywhere I could find.

There is nonvcc. The image ships the driver and a torch built against CUDA, not thetoolkit. You need the keyring andcuda-toolkit-13-2from NVIDIA'ssbsarepo — not thex86 one, which is an easy reflex to get wrong on an Arm box.

And vLLM now wants Rust. Itsvllm-rsfrontend needssetuptools_rustplus a toolchain,and the failure is a bareModuleNotFoundError: No module named 'setuptools_rust'thrownfrom metadata generation, several minutes in.

## The newest vLLM was the only one that worked

No vLLM tag pins torch 2.12. They go 2.11, then jump to 2.13. I reasoned that building oldercode against a newer runtime was the safer direction, took v0.26.0, and spent an hour beingwrong about it.

It builds fine. It then dies on model load:

transformers.integrations.heterogeneity.configuration_utils.AmbiguousGlobalPerLayerAttributeError:
'head_dim' is a per-layer attribute and may vary across layers.

Enter fullscreen mode

Exit fullscreen mode

Gemma 4'shead_dimis not one number, and currenttransformersrefuses to hand out aglobal value for it. vLLM's config converter was still doing a flatgetattr(config, "head_dim", 0). Theper_layer_confighandling that copes with it landedinv0.27.2rc0— not v0.27.1, which I also checked. The newest tag was the only one thatworked.

If you take one process lesson from this: reach for the latest release first, and make theconstraint say out loud what stopped you when you fall back.

## Gemma 4's attention heads are not one size

With the build working the server still would not start, and this failure has nothing to dowith Arm or packaging. It is this model against this chip.

Gemma4 model has heterogeneous head dimensions
{'sliding_attention': 256, 'full_attention': 512}.
FA4 not available, forcing TRITON_ATTN backend.

Enter fullscreen mode

Exit fullscreen mode

Read that as a chain, because every link is load-bearing:

1. Gemma 4's sliding layers are 256 wide. Its global layers are512.
2. Only FA4 or Triton support heterogeneous head dims at all.
3. FA4 is not available, so vLLM forcesTRITON_ATTN.
4. That choice is not yours to make.VLLM_ATTENTION_BACKENDis not a recognised variable
in v0.27 — it logsUnknown vLLM environment variable detectedand carries on. I set it
twice before I read the warning.
5. Triton's unified attention kernel athead_size=512wants about 96 KiB of shared memory
per block.

## 64 KiB is the whole problem

Turing's shared memory is two numbers, and both are real. Thedefaultstatic limit per blockis 48 KiB — that is whattorch.cuda.get_device_properties().shared_memory_per_blockreports,49,152 bytes. A kernel that needs more has to opt in through the dynamic shared-memoryattribute, and even then it tops out at64 KiB. Ampere and later have 164 KiB and up.

Triton opts in, so it is measuring against the 64 KiB ceiling. It still does not fit:

triton.runtime.errors.OutOfResources: out of resource: shared memory,
Required: 98304, Hardware limit: 65536

Enter fullscreen mode

Exit fullscreen mode

Refused outright. Not slow, not degraded — the kernel will not launch, and it takes theengine down during CUDA graph capture, which is late enough that you have already watchedthe weights load and the KV cache get sized.

The fix is small. Shrink the KV tile until the query block and the K/V tiles fit inside thebudget, and drop the software pipeline to one stage. Gate it on pre-Ampere so it is a no-opon every other card:

if
 
current_platform
.
get_device_capability
()[
0
]
 
<
 
8
:

 
_smem_budget
 
=
 
60000

 
_esz
 
=
 
q
.
element_size
()

 
def
 
_fits
(
t
):
 
return 
(
BLOCK_M
 
+
 
2
 
*
 
t
)
 
*
 
head_size
 
*
 
_esz
 
<=
 
_smem_budget

 
while
 
TILE_SIZE_PREFILL
 
>
 
16
 
and
 
not
 
_fits
(
TILE_SIZE_PREFILL
):
 
TILE_SIZE_PREFILL
 
//=
 
2

 
while
 
TILE_SIZE_DECODE
 
>
 
16
 
and
 
not
 
_fits
(
TILE_SIZE_DECODE
):
 
TILE_SIZE_DECODE
 
//=
 
2

 
launch_num_stages
 
=
 
1

Enter fullscreen mode

Exit fullscreen mode

With that invllm/v1/attention/ops/triton_unified_attention.py, graphs capture, the enginecomes up in 76 seconds, and the model serves.This is not upstream.It lives on myinstance and has to be reapplied on any vLLM upgrade, which makes it the obvious thing tosend back.

## Most of the build is kernels that can never load

67 minutes on ag5g.4xlargeatMAX_JOBS=12, and the majority of it is FlashAttention.vLLM compiles FA2 and FA3regardless ofTORCH_CUDA_ARCH_LIST— I watched it grindthrough hundreds ofsm90Hopper instantiations on a build targeting 7.5 only. FA2 needssm80, FA3 needs sm90. Neither can ever load on this card.

ConstrainingVLLM_FA_CMAKE_GPU_ARCHESshould cut that dramatically. I did not try it,because by the time I understood what I was looking at the build was 45 minutes in andinterrupting it would have cost more than finishing.

## What I got wrong before I had hardware

I wrote the rig's documentation before provisioning anything. Seven claims in it were wrong,and every correction came off the machine rather than out of an argument. This is the part Iwould keep if I kept nothing else.

What I wrote

What the box said

PyTorch aarch64 lacks 
sm_75

AWS DLAMI has it, on both versions I checked

bfloat16 is a hard failure here

Torch upconverts; vLLM logs 
Casting torch.bfloat16 to torch.float16
 and proceeds

The backend is XFORMERS

TRITON_ATTN
, forced, not selectable

VLLM_ATTENTION_BACKEND
 picks it

Not a recognised variable. I had shipped dead config.

w4a16 needs sm80+ Marlin

The build compiled 
sm75_kernel_float16_u4b8_float16.cu.o

The GPU has 16 GB

15,360 MiB

/v1/completions
 returns an empty body

It returns 
': ok: ok: ok: ok'
 — garbage, not silence

That last one has teeth. If you health-check by testing for an empty response, this endpointpasses while producing nonsense. Use/v1/chat/completionsand read the text.

One claim is still standing only because I never tested it: whetherg5g.xlarge's 8 GiB ofhost RAM can stage 9.5 GiB of weights. Safetensors loading is mmap-backed, so I suspect itcan. It is labelled untested rather than stated as fact, which is where it should have beenall along.

## What it does once it runs

content
:
 
'
Site
 
Reliability
 
Engineering
 
(SRE)
 
is
 
a
 
discipline
 
that
 
applies

 
software
 
engineering
 
principles
 
to
 
infrastructure
 
and
 
operations

 
problems
 
to
 
create
 
highly
 
reliable,
 
scalable,
 
and
 
efficient
 
systems.'

finish_reason: stop usage
:
 
19 prompt / 32 completion / 51 total

Enter fullscreen mode

Exit fullscreen mode

Measure

Value

Throughput, single stream greedy

42.9 tok/s @ 64, 43.1 @ 256

KV cache

2.95 GiB, 329,579 tokens

Concurrency at 16k context

20.12x

GPU memory while serving

13,501 / 15,360 MiB

Engine init

76.4 s, graph capture 17 s

Memory bandwidth, measured

277.0 GB/s read · 234.3 GB/s copy (320.1 theoretical)

Before reading too much into 43 tok/s, note what the memory does. The T4G hasGDDR6, notHBM— 256-bit bus at 5,001 MHz, so 320 GB/s theoretical. I measured277 GB/son astreaming read (87% of peak) and 234 GB/s on a read-modify-write. Decode is bandwidth-bound,so 277 is the real ceiling. For scale, a TPU v5e is about 859 GB/s normalized and a v6e about1,638 — this part has roughly a third of one and a sixth of the other. It is a bandwidth-limitedcard behaving like a bandwidth-limited card.

Single run, single stream, no repeats and no variance figure. One sample per cell, and takenwith the clamped tiles, so it is a floor rather than a characterisation. My Inferentia portmeasured about 44 tok/s for E2B on one core, which is the same neighbourhood — but that is adifferent harness on different silicon and I would not put the two in one table.

## Troubleshooting quick reference

Symptom

Cause

no kernel image is available

Stock arm64 image. No 7.5, no PTX. Build from source.

OutOfResources: shared memory

Turing's 64 KiB against a 512-wide head. Clamp the tiles.

AmbiguousGlobalPerLayerAttributeError

vLLM older than v0.27.2rc0.

No module named 'setuptools_rust'

Missing Rust toolchain for 
vllm-rs
.

nvcc: not found

PyTorch DLAMI has no toolkit. Install 
cuda-toolkit-13-2
 (sbsa).

Unknown vLLM environment variable

You set 
VLLM_ATTENTION_BACKEND
. It does nothing.

Healthy endpoint, nonsense output

You checked 
/v1/completions
. Use chat completions.

## The short version

Take the AWS ARM64 GPU PyTorch DLAMI — it is the only maintained aarch64 stack that stillcarriessm_75. Addcuda-toolkit-13-2from the sbsa repo and a Rust toolchain, because theimage ships neither. Build vLLM v0.27.2rc0 or newer from source withTORCH_CUDA_ARCH_LIST=7.5anduse_existing_torch.py, and patch the Triton attention kernelto fit Turing's shared memory before you try to start it. Serve with--dtype float16and--kv-cache-dtype auto.

Nothing here failed loudly, and nothing failed where I was looking. The packaging gap I builtthe rig around was already solved by AWS; the thing that actually stopped me was 32 KiB ofshared memory and a model whose global attention heads are twice as wide as its sliding ones.Hardware this far off the mainstream will keep producing that shape of surprise — the fix isnot to reason harder about it, but to get to a box sooner and let it tell you.

Measured on EC2g5g.4xlargespot,us-east-1a. NVIDIA T4G, compute capability 7.5,15,360 MiB, driver 595.71.05. Deep Learning ARM64 AMI OSS Nvidia Driver GPU PyTorch 2.12(Ubuntu 24.04). torch 2.12.0+cu132, CUDA 13.2. vLLM 0.27.2rc1.dev0+g7f7a32cfe built fromv0.27.2rc0.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse