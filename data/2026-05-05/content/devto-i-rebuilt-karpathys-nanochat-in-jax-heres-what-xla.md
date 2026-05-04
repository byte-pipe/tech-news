---
title: I Rebuilt Karpathy's NanoChat in JAX. Here's What XLA Gets Right and What It Gets Dead Wrong. - DEV Community
url: https://dev.to/gde/i-rebuilt-karpathys-nanochat-in-jax-heres-what-xla-gets-right-and-what-it-gets-dead-wrong-4641
site_name: devto
content_file: devto-i-rebuilt-karpathys-nanochat-in-jax-heres-what-xla
fetched_at: '2026-05-05T00:51:24.941957'
original_url: https://dev.to/gde/i-rebuilt-karpathys-nanochat-in-jax-heres-what-xla-gets-right-and-what-it-gets-dead-wrong-4641
author: Omotayo Aina
date: '2026-05-01'
description: 'AI GDE TPU Sprint 2026 · Google TPU Research Cloud Quick summary: We ported Andrej Karpathy''s... Tagged with machinelearning, python, ai, deeplearning.'
tags: '#machinelearning, #python, #ai, #deeplearning'
---

AI GDE TPU Sprint 2026 · Google TPU Research Cloud

Quick summary:We ported Andrej Karpathy's NanoChat architecture from PyTorch to JAX and Flax NNX. The repo is about 12,400 lines across source and scripts. We trained a nano model (885K parameters) on TinyStories in under 10 minutes on a single GPU and served it through a streaming chat UI. XLA compilation eliminates Python overhead after a one-time upfront cost. The same code runs on TPU without modification. The catch: no vLLM, no Flash Attention 3, and painful debugging inside JIT-compiled functions. This post covers what worked, what did not, and when you should care.

The nanochat-jax transformer block. The ✦ symbol marks nanochat-specific components not present in standard GPT or LLaMA: Value Embeddings, Smear/Backout token mixing, per-layer learnable scalars, QK L2 normalization, and logit softcap.

## What This Project Is

Andrej Karpathy'sNanoChatis roughly 8,600 lines of PyTorch that tries to answer one question: what is the best ChatGPT you can train for $100? It ships with Flash Attention 3 on Hopper, the Muon optimizer (Newton-Schulz orthogonalization), FP8 mixed-precision, distributed training viaDistMuonAdamW, SFT, RL via GRPO, and a web chat UI. The model architecture packs in a lot of modern ideas: Grouped-Query Attention, RoPE positional encoding, parameterless RMSNorm, ReLU-squared activation, Value Embeddings, Smear/Backout token mixing, per-layer learnable scalars, QK L2 normalization, and logit softcap.

NanoChat-JAXis a faithful port of that architecture to JAX and Flax NNX. Two things motivated the port. First, we wanted scaling law instrumentation that the original does not have: the ability to sweep model size, data volume, and compute budget systematically and fit Chinchilla-style power laws to the results. Second, we wanted to run the same code on GPU and TPU without a device-specific codebase. JAX's XLA backend makes that possible. This project is part of the AI GDE TPU Sprint 2026, where Google TPU Research Cloud compute is available for exactly this kind of scaling experiment.

## Five NanoChat Architecture Components Worth Understanding

Most open-source GPT implementations stop at multi-head attention, an FFN, and RoPE. NanoChat adds five components that are not in the standard recipe. Understanding them matters because each one shows up in the JAX translation in a non-obvious way.

### Logit Softcap

NanoChat appliescap * tanh(logits / cap)to attention scores before the softmax. This clamps score magnitudes to the range[-cap, cap]and prevents the entropy collapse that happens at depth when very sharp attention distributions starve gradients. NanoChat uses a softcap value of 15.0; our JAX port uses 30.0, which is a deliberate divergence noted in the comparison table at the end of this post.

PyTorch:

scores
 
=
 
torch
.
matmul
(
q
,
 
k
.
transpose
(
-
2
,
 
-
1
))
 
*
 
self
.
attn_scale

if
 
self
.
logit_softcap
 
is
 
not
 
None
:

 
scores
 
=
 
self
.
logit_softcap
 
*
 
torch
.
tanh
(
scores
 
/
 
self
.
logit_softcap
)

scores
.
masked_fill_
(
~
mask
,
 
float
(
'
-inf
'
))

weights
 
=
 
F
.
softmax
(
scores
,
 
dim
=-
1
)

Enter fullscreen mode

Exit fullscreen mode

JAX:

scores
 
=
 
jnp
.
matmul
(

 
q
.
astype
(
jnp
.
float32
),

 
jnp
.
transpose
(
k_exp
.
astype
(
jnp
.
float32
),
 
(
0
,
 
1
,
 
3
,
 
2
))

)
 
*
 
self
.
attn_scale

if
 
self
.
logit_softcap
 
is
 
not
 
None
:

 
cap
 
=
 
float
(
self
.
logit_softcap
)

 
scores
 
=
 
cap
 
*
 
jnp
.
tanh
(
scores
 
/
 
cap
)

scores
 
=
 
jnp
.
where
(
combined_mask
,
 
scores
,
 
jnp
.
float32
(
-
1e9
))

weights
 
=
 
jax
.
nn
.
softmax
(
scores
,
 
axis
=-
1
)

Enter fullscreen mode

Exit fullscreen mode

Two differences stand out.jnp.wherereplacesmasked_fill_because JAX arrays are immutable: you cannot modify them in-place, so you select between two arrays instead. We also use-1e9instead of-inf. When an entire attention row is masked (as happens with padding tokens), JAX's softmax producesNaNon-infinput rather than handling it gracefully the way PyTorch does. Switching to-1e9fixes the issue cleanly; we hit this bug midway through the port.

### The Training Step as a Pure Function

In PyTorch, you write a loop: zero grads, forward, loss, backward, step. In Flax NNX, the entire training step becomes a pure function decorated with@nnx.jit:

@staticmethod

@nnx.jit

def
 
_train_step_jit
(

 
model
:
 
TransformerLM
,

 
optimizer
:
 
nnx
.
Optimizer
,

 
batch
:
 
dict
[
str
,
 
jax
.
Array
],

)
 
->
 
dict
[
str
,
 
jax
.
Array
]:

 
def
 
loss_fn
(
model
:
 
TransformerLM
)
 
->
 
tuple
[
jax
.
Array
,
 
dict
]:

 
logits
,
 
_
 
=
 
model
(
batch
[
"
input_ids
"
],
 
deterministic
=
False
)

 
loss
,
 
metrics
 
=
 
cross_entropy_loss
(

 
logits
=
logits
[:,
 
:
-
1
,
 
:],

 
labels
=
batch
[
"
labels
"
][:,
 
:
-
1
],

 
)

 
return
 
loss
,
 
metrics

 
(
loss
,
 
metrics
),
 
grads
 
=
 
nnx
.
value_and_grad
(
loss_fn
,
 
has_aux
=
True
)(
model
)

 
grad_norm
 
=
 
optax
.
global_norm
(
jax
.
tree
.
leaves
(
grads
))

 
optimizer
.
update
(
model
,
 
grads
)

 
return
 
{
"
loss
"
:
 
loss
,
 
"
grad_norm
"
:
 
grad_norm
,
 
**
metrics
}

Enter fullscreen mode

Exit fullscreen mode

nnx.value_and_gradreplaces theloss.backward()/optimizer.step()/optimizer.zero_grad()sequence. NNX extracts model parameters as a pytree, computes gradients as a matching pytree, and applies them through the optimizer. There is no gradient tape to manage, no.detach()to remember, and notorch.no_grad()context manager.

@nnx.jittraces the function once and compiles it to an XLA HLO program. Every subsequent call skips Python entirely and dispatches directly to the compiled kernel.

### Muon Optimizer: Newton-Schulz Inside XLA

Muon orthogonalizes each 2D weight gradient via Newton-Schulz iterations. The update rule isX_{t+1} = 1.5X - 0.5(XX^TX), repeated for a fixed number of steps. Since the full training step runs under@nnx.jit, this loop must be JIT-compilable. In PyTorch,torch.compileunrolls a Pythonforloop at trace time. In JAX, we usejax.lax.fori_loop:

def
 
newton_schulz_orthogonalize
(
G
:
 
jax
.
Array
,
 
steps
:
 
int
 
=
 
10
)
 
->
 
jax
.
Array
:

 
G
 
=
 
G
.
astype
(
jnp
.
float32
)

 
G
 
=
 
G
 
/
 
(
jnp
.
linalg
.
norm
(
G
)
 
+
 
1e-8
)

 
transpose
 
=
 
G
.
shape
[
0
]
 
>
 
G
.
shape
[
1
]

 
if
 
transpose
:

 
G
 
=
 
G
.
T

 
def
 
ns_step
(
_
,
 
X
):

 
A
 
=
 
X
 
@
 
X
.
T

 
return
 
1.5
 
*
 
X
 
-
 
0.5
 
*
 
(
A
 
@
 
X
)

 
G
 
=
 
jax
.
lax
.
fori_loop
(
0
,
 
steps
,
 
ns_step
,
 
G
)

 
if
 
transpose
:

 
G
 
=
 
G
.
T

 
return
 
G

Enter fullscreen mode

Exit fullscreen mode

jax.lax.fori_loopcompiles to a single XLA while-loop operation. The compiled program size stays constant regardless of iteration count, and changingstepsdoes not trigger recompilation. The tradeoff is that you cannot use Python control flow inside the loop body. Debugging meansjax.debug.printrather thanprint.

### Value Embeddings

Value Embeddings give each token a learned residual vector that is independent of context. Unlike input embeddings, which are used once at the bottom of the stack, value embeddings are added into the attention output at every layer. A single shared lookup table lives at the top-levelTransformerLMand gets passed by reference to each block:

# TransformerLM.__init__

if
 
cfg
.
use_value_embeddings
:

 
self
.
value_embed
 
=
 
ValueEmbedding
(
cfg
.
vocab_size
,
 
cfg
.
d_model
,
 
rngs
=
rngs
)

self
.
layers
 
=
 
nnx
.
List
([

 
TransformerBlock
(
cfg
,
 
layer_idx
=
i
,
 
value_embed
=
self
.
value_embed
,
 
rngs
=
rngs
)

 
for
 
i
 
in
 
range
(
cfg
.
n_layers
)

])

Enter fullscreen mode

Exit fullscreen mode

The table initializes near zero (scale1e-4), so the model starts as if value embeddings do not exist. Their contribution grows only as gradient descent drives the table weights away from zero. This no-op initialization pattern appears throughout nanochat: new components start inert and the optimizer learns to use them.

### Smear and Backout Token Mixing

Smear and Backout are cheap causal token-mixing operations. Smear blends each token with its immediate predecessor:x[t] = (1 - alpha) * x[t] + alpha * x[t-1], wherealpha = sigmoid(raw_alpha)is a learned per-feature vector of shape(d_model,). Backout then removes the correlation introduced by Smear from the attention output, preventing double-counting when that output is added back to the residual stream.

In JAX, the causal shift needs no Python loop:

x_prev
 
=
 
jnp
.
concatenate
(

 
[
jnp
.
zeros_like
(
x
[:,
 
:
1
,
 
:]),
 
x
[:,
 
:
-
1
,
 
:]],
 
axis
=
1

)

alpha
 
=
 
jax
.
nn
.
sigmoid
(
self
.
raw_alpha
.
get_value
())

x_smeared
 
=
 
x
 
+
 
alpha
 
*
 
(
x_prev
 
-
 
x
)

Enter fullscreen mode

Exit fullscreen mode

Bothraw_alphaandraw_betainitialize to-10.0.sigmoid(-10)is approximately5e-5, so at step 0 the Smear and Backout components have essentially zero effect on the forward pass. Their contribution grows only as the optimizer pushes these parameters away from their initialization.

### Depth-Aware Weight Initialization

Residual output projections (attentionout_projand FFNdown_proj) at layer indexlare scaled by1 / sqrt(2 * (l + 1)). This assigns progressively smaller initialization scales to deeper layers, which controls how much each layer can perturb the residual stream as depth increases. GPT-NeoX applies1 / sqrt(2 * n_layers)uniformly to all layers, giving every layer the same scale regardless of its position in the stack.

def
 
_init_weights_from_depth
(
self
)
 
->
 
None
:

 
for
 
layer_idx
,
 
layer
 
in
 
enumerate
(
self
.
layers
):

 
depth_scale
 
=
 
1.0
 
/
 
math
.
sqrt
(
2.0
 
*
 
(
layer_idx
 
+
 
1
))

 
layer
.
attention
.
out_proj
.
kernel
 
=
 
nnx
.
Param
(

 
layer
.
attention
.
out_proj
.
kernel
.
get_value
()
 
*
 
depth_scale

 
)

 
layer
.
ffn
.
down_proj
.
kernel
 
=
 
nnx
.
Param
(

 
layer
.
ffn
.
down_proj
.
kernel
.
get_value
()
 
*
 
depth_scale

 
)

Enter fullscreen mode

Exit fullscreen mode

In Flax NNX, parameter mutation works by calling.get_value(), applying the transform, and wrapping the result innnx.Param. There is noparam.data.mul_()equivalent.

## Getting It Running

# Clone and install

git clone https://github.com/ainaomotayo/nanochat-jax

cd 
nanochat-jax
pip 
install
 
-e
 
".[dev]"

# Download and preprocess TinyStories (saves vocab alongside HDF5)

python 
-m
 scripts.preprocess 
--dataset
 tinystories 
--output_dir
 data/

# Train the nano model (about 10 minutes on a GPU)

python 
-m
 scripts.train 
\

 
--model-size
 nano 
\

 
--data-path
 data/tinystories.h5 
\

 
--device
 gpu 
\

 
--steps
 2000

# Start the chat UI server

python 
-m
 scripts.chat_web 
\

 
--checkpoint
 checkpoints/tinystories_nano/latest 
\

 
--model-size
 nano 
\

 
--device
 gpu

# Open http://localhost:8000

Enter fullscreen mode

Exit fullscreen mode

The server loads the tokenizer fromdata/tinystories_vocab.json, restores weights from the checkpoint viaCheckpointManager, and serves an OpenAI-compatible streaming API at/v1/chat/completionsalongside the browser UI.

The chat UI with the trained nano model responding. Tokens stream to the browser via SSE. The orange warning banner appears when the server starts with random weights; it is absent here because a real checkpoint is loaded.

## The Numbers We Actually Measured

Training and validation loss for the nano model over 2,000 steps on TinyStories. The XLA compile happens on step 1 (about 35 seconds). Steady-state step time is 290ms. Final val_loss = 1.295, perplexity = 3.65.

We ran one confirmed training experiment. Every number in this table came from that run:

Metric

Value

Model preset

nano

Parameters

885,768

Dataset

TinyStories (180M tokens, 95-character vocabulary)

Device

GPU, bfloat16

Steps

2,000

Best validation loss

1.295

Perplexity

3.65

Total training time

9.7 minutes

Steady-state step time

290ms

First step time (includes XLA compile)

~35 seconds

Step 1 takes about 35 seconds because XLA traces and compiles the entire forward pass, backward pass, and Muon optimizer update into a single fused HLO program. Steps 2 through 2,000 average 290ms with no Python dispatch overhead. Over the full 2,000-step run, that 35-second compile adds roughly 3% to total training time.

Parameter counts for model sizes other than nano are estimates based on the architecture config. We have not run training at larger scales yet.

### Model Scale Presets

Five model presets from 885K (nano, confirmed from training) to approximately 6.7B parameters (xlarge, estimated from config). All presets share the same nanochat architecture.

Every preset uses GQA, ReLU-squared, QK normalization, logit softcap, Value Embeddings, Smear/Backout, and per-layer scalars. Only the dimensions change:

Preset

d_model

n_layers

n_heads

n_kv_heads

d_ff

Vocab

Max Seq

nano

128

4

4

4

512

256

64

small

512

6

8

8

2048

32000

2048

medium

1024

12

16

8

4096

32000

2048

large

2048

24

32

8

8192

32000

4096

xlarge

4096

32

32

8

16384

32000

4096

## Where JAX Has a Real Advantage

### Gradient bugs surface as errors, not silent failures

Thennx.value_and_gradpattern forces training into the shape(params, data) -> (loss, grads). During the port, we did not encounter forgottenzero_grad()calls, gradients leaking across accumulation steps, or missing.detach()on a loss component. Those bugs exist in PyTorch codebases and they manifest as training that runs but converges to a worse minimum, which is the hardest category of bug to diagnose because nothing crashes.

JAX's explicit PRNG threading viannx.Rngsalso makes reproducibility the default. Two runs with the same seed produce identical step-by-step losses without any extra flags. Achieving the same in PyTorch requirestorch.use_deterministic_algorithms(True), which disables several optimized kernels and hurts throughput.

### XLA compiles the whole training step, not just parts of it

When@nnx.jitcompiles a training step, XLA sees the full computation graph from the input tensor to the updated parameters. It can fuse operations that PyTorch's operator-level dispatch handles as separate kernel launches: attention softcap, masking, and softmax can become one kernel; RMSNorm and the linear projection that follows it can become another. After compilation, each step is a single kernel launch with no Python-level overhead between operations.

For the nano model at 290ms per step, that saved overhead is modest in absolute terms. The argument for XLA becomes stronger as model size grows and each kernel does proportionally more compute relative to the dispatch cost.

### TPU runs with a flag change, not a code change

python 
-m
 scripts.train 
--device
 gpu 
# local GPU

python 
-m
 scripts.train 
--device
 tpu 
# Google TPU Research Cloud

Enter fullscreen mode

Exit fullscreen mode

JAX's XLA backend compiles the same HLO program to both CUDA and TPU targets. There is notorch.xlabridge, no CUDA-specific memory management, and no device-specific attention kernel. For researchers with TPU Research Cloud access through the AI GDE program, this means developing on a GPU workstation and running scaling sweeps on TPU v4-8 pods without any porting step in between.

### The transformation system composes naturally

jit,grad,vmap, andhessianare all first-class JAX transformations that compose with each other. Becausetrain_stepis a pure function of(model_state, batch), you can apply any of them without restructuring the code.jax.hessianin particular lets you compute the full Hessian of the loss with respect to model parameters, which enables loss landscape geometry analysis at convergence. In PyTorch, getting there requirestorch.autograd.functional.hessianand considerably more scaffolding. We have not yet run these analyses on nanochat-jax, but the codebase is structured to support them directly.

## Where PyTorch Still Wins

Ecosystem.vLLM, DeepSpeed, PEFT, bitsandbytes, HuggingFace Transformers: none of these work with JAX. If your pipeline involves LoRA fine-tuning, vLLM inference, or HuggingFace benchmark evaluation, you are staying in PyTorch. No JAX-native equivalent of that integrated stack exists today.

Flash Attention.NanoChat uses Flash Attention 3 on Hopper hardware via Triton, which is a hand-optimized kernel that gets close to peak memory bandwidth. The JAX equivalent requires writing Pallas custom kernels, which is significantly harder and less mature. XLA's fused attention is capable but is not equivalent to FA3 for long sequences on Hopper GPUs.

Debugging.Inside a JIT-compiled JAX function, you cannot useprintorbreakpoint. You usejax.debug.print, and shape errors surface as abstract trace errors rather than concrete tensor shapes. We spent more time diagnosing shape mismatches in JAX than we would have in PyTorch for the same codebase.

Distributed training.NanoChat'sDistMuonAdamWwith ZeRO-2 sharding is production-tested for multi-GPU runs. NanoChat-JAX has ajax.shardingstub for data parallelism that exists in the codebase but has not been tested at scale.

FP8.PyTorch hastorch._scaled_mmfor FP8 matrix multiplications. JAX's FP8 support is still early. NanoChat-JAX does not implement FP8 training.

## Scaling Law Findings

The main research goal is systematic scaling experimentation. We built three experiment types into the codebase:scale_n(vary model size, fix data),scale_d(vary data, fix model), andscale_c(sweep compute budget, co-optimize model and data).

We fit the standard power lawL(N) = a * N^(-alpha)to validation loss as a function of non-embedding parameter count, using 600 training steps per model size on TinyStories.

Result:L = 3.29 * N^(-0.027)

The exponent alpha = 0.027 is much flatter than published values. Kaplan et al. (2020) measured alpha around 0.076 on WebText2 (~40B tokens). Hoffmann et al. (2022, Chinchilla) measured the parametric component at around 0.34 on MassiveText (~1.4T tokens). Three things explain the gap.

Training duration.600 steps does not bring larger models to convergence. The nano model is close to its loss floor at 600 steps; the small model (~35M parameters) is still in the steep part of its loss curve. With extended training, preliminary results show alpha rising toward the 0.07 to 0.12 range, which is closer to Kaplan's values.

Data scale.TinyStories is 180M tokens. The datasets used in published scaling laws are orders of magnitude larger. With limited data, larger models overfit before the power law can stabilize, which artificially flattens the scaling curve.

Character-level tokenization.Character models scale differently than subword models. A single character carries less information than a BPE token, which changes both the effective data scale and the compute requirements per unit of language modeling quality.

The Chinchilla analysis module (nanochat/scaling/analysis.py) implements the parametric loss modelL(N, D) = E + A/N^alpha + B/D^betawith 1,000-sample bootstrap confidence intervals. For a given compute budgetC = 6ND, it computes the optimal allocationN* ~ C^(beta/(alpha+beta)). Our current exponents are too noisy for reliable Chinchilla-optimal predictions. With TPU-scale compute, we plan to run fullscale_nandscale_csweeps and publish updated results.

## Practical Advice

Use JAX if you have TPU access and care about scaling experiments.The functional programming model makes it natural to express experiments as pure functions over configuration spaces. TPU portability costs nothing once you are writing JAX.jax.hessianandjax.vmapare real, stable APIs in JAX, not future roadmap items, and the nanochat-jax codebase is structured to use them directly.

Use PyTorch if you need the serving and fine-tuning stack.LoRA, vLLM, HuggingFace pipelines, Flash Attention 3: these are PyTorch-only today. The research advantages of JAX do not outweigh rebuilding that infrastructure from scratch for most applied teams.

Budget time for XLA compilation.The first step of any new model configuration takes 30 to 60 seconds. Always run a warmup step before starting any timing measurement. Never report first-step timing as representative of steady-state performance.

The port took about three focused weeks.Architecture translation (attention, FFN, norms, embeddings) was mechanical once we understood the Flax NNX API. The hard parts were making Muon JIT-compatible viafori_loop, tracing shape errors in the KV cache path, and implementing checkpoint serialization and SSE streaming without PyTorch-ecosystem conveniences.

## What Is Implemented vs What Is Not

Capability

nanochat (PyTorch)

nanochat-jax (JAX)

GQA + RoPE + parameterless RMSNorm

yes

yes

Logit softcap

yes (15.0)

yes (30.0)

Value Embeddings

yes

yes

Smear/Backout token mixing

yes

yes

Per-layer learnable scalars

yes

yes

Depth-aware weight initialization

yes

yes

Muon optimizer

yes, DistMuonAdamW with ZeRO-2

yes, single-device only

Flash Attention 3

yes, Hopper via Triton

no

FP8 training

yes

no

Distributed multi-GPU training

yes

no (stub)

SFT and RL via GRPO

yes

no

Streaming chat UI

yes

yes, via SSE

OpenAI-compatible API

yes

yes

Scaling law instrumentation

no

yes

TPU portability

no

yes

## Conclusion

NanoChat-JAX reproduces the nanochat architecture in JAX and Flax NNX: GQA, QK L2 normalization, logit softcap, Value Embeddings, Smear/Backout, per-layer scalars, and Muon. The nano model trains to val_loss 1.295 (perplexity 3.65) on TinyStories in under 10 minutes on a single GPU. The chat UI works and streams tokens via SSE from a FastAPI server.

XLA is a real tradeoff. You pay a one-time compile cost of around 35 seconds per new model configuration and get zero Python overhead on every subsequent step. TPU portability is one flag away. The ecosystem gap is equally real: no Flash Attention 3, no distributed optimizer, no PEFT or vLLM. For GPU-only practitioners who need those tools, the JAX advantages do not justify the rebuild cost.

The scaling law experiments are early. The measured exponent (alpha = 0.027 at 600 steps, rising with extended training) reflects the known limitations of short runs on a small dataset. Fullscale_nandscale_csweeps on TPU are planned for the AI GDE TPU Sprint 2026. Updated results with confidence intervals will be published when those runs complete.

Code:github.com/ainaomotayo/nanochat-jax

This work is part of the AI Google Developer Expert TPU Sprint 2026, with compute from the Google TPU Research Cloud program.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse