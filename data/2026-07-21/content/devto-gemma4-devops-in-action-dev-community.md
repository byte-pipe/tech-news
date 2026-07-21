---
title: Gemma4 DevOps In Action - DEV Community
url: https://dev.to/gde/gemma4-devops-in-action-10bl
site_name: devto
content_file: devto-gemma4-devops-in-action-dev-community
fetched_at: '2026-07-21T19:33:24.142022'
original_url: https://dev.to/gde/gemma4-devops-in-action-10bl
author: xbill
date: '2026-07-20'
description: In the last entry I got Gemma-4's 128-expert MoE running on an inf2.24xlarge and signed off with... Tagged with ai, aws, devops, llm.
tags: '#ai, #aws, #devops, #llm'
---

In the last entry I got Gemma-4's 128-expert MoE running on aninf2.24xlargeand signed off with acliffhanger: fitting it on a 2-core box "needs fp4 — a separate expedition." This is that expedition.It ended nowhere near where I thought it would:notwith fp4, andnoton the 8xlarge I wasaiming for, but on the smallest, cheapest Inferentia2 instance AWS sells — asingleinf2.xlargewith 16 GB of host RAM— running a26B-parameter model. Here's the refinement trail, dead endsincluded.

The finished port (see the previous article) served the 26B-A4B on a 24xlarge: 12 NeuronCores, 192 GBHBM, ~$6.49/hr on-demand. It worked, it was correct, and it wasoverkill for one user asking onequestion at a time.The whole point of a "4B-active" MoE is that it's cheap torun; it shouldn't needa datacenter-class box tohost. The goal: get it onto the bottom-tierinf2.xlarge— 2 cores, 32 GBHBM, and only16 GB of host RAM— at ~$0.76/hr. That's8.6× cheaper.

24xlarge (shipped)

inf2.xlarge (goal)

NeuronCores

12 (used 8)

2

HBM

192 GB

32 GB

Host RAM

768 GB

16 GB

On-demand

~$6.49/hr

~$0.76/hr

Two walls stood in the way: the model doesn't fit 32 GB of HBM at bf16, and it doesn't fit 16 GB of hostRAM thenormalway. I had to break both.

## Wall 1: the memory math, and why "A4B" doesn't save you

The experts are ~93% of the weight. At bf16 the 128 experts are ~45.6 GB — replicate that across TP=2and you're at ~22.8 GBper coreagainst a 16 GB budget. Top-8 routing reducescompute, notfootprint: all 128 experts must be resident. So the experts alone blow the box.

My first move was the obvious one —int8 the experts. NxD hasQuantizedColumnParallel/QuantizedRowParallel, and (from the prior article) int8-per-channel on this model isnumericallyperfect: token-for-token identical to fp32. Experts drop to ~11.4 GB/rank. Should fit.

It didn't.Could not load the model status=4 Allocation Failure—~3–4 GB overthe 16 GB core. Andinf2has no 4-core SKU to split the difference. My conclusion at the time, which I even wrote down: toclose that last 3–4 GB you needfp4experts.

## The fp4 rabbit hole (two of them, both dead ends)

I chased fp4 twice.

First,QuantizedColumnParalleladvertisesF4E2M1FN_X4. But its state_dict weight is apackeduint16microscaling format (32 fp4 → 8 uint16) produced byfrom_float/preshard_hook— nothinglike int8's five-line quantizer. Then I read the AWS docs plainly:NxD Inference quantization supportsINT8 and FP8 only.FP8 is 8-bit — same size as int8, so it doesn't help.QuantizedDtype.F4E2M1FN_X4existsas a constant but isn't a wired-up inference path.

Second, on the newest Neuron 2.31 stack (neuronx-cc 2.26, NxD 0.19) fp4 lookedlessabsent —there'sBLOCKWISE_SYMMETRIC,block_size,from_float. So I tried again, and hit the floor twice:

* The cleanQuantizedColumnParallelfp4 forward callsblockwise_scale_dequantize, which is aCPU-only torch reference(assert device == cpu) — it can't trace to a NeuronCore.
* The real device path wants theblockwise_mmNKI kernel, which NxD imports fromneuronxcc.nki._private.blockwise_mm— but 2.26 ships it under_pre_prod_kernels. Mispathed,
pre-prod, import fails.
* Swapping myDenseExpertsfor NxD'sExpertMLPs(which has fp4 packing) didn't help either: its
blockwise NKI pathkernel_asserts, and itsuse_torch_block_wise=Truepathcrashes torch-xla's
shape inference on a data-dependent index op.MoE routing that won't trace — the exact problem the
dense trick solved for compute, now back for quantization.

fp4 on inf2 is a wall in this SDK.I'd spent real time being sure it was the only door. It wasn'teven a door.

## The breakthrough: I was quantizing the wrong thing

Here's the reframe that unlocked it. I'd been staring at the experts because they're huge. But theexperts werealready int8when I OOM'd. The 3–4 GB I needed wasn't in the experts — it was in theweights I'd left in bf16. Chiefly one: thetiedlm_head, replicated at1.48 GB per rank.

The fix wasn'tsmaller experts. It was anall-int8 squeezeof everything still fat:

1. int8andshard thelm_head.QuantizedColumnParallel(gather_output=True)slices the 262k-row
head across ranks and quantizes it:1.48 GB → ~0.37 GB/rank.This was the single biggest lever, and
it had nothing to do with the experts.
2. int8 the shared dense MLP(the other half of the dual-path FFN): another ~0.27 GB/rank.
3. Keep the int8 experts.

Per-rank resident dropped to ~12–13 GB — comfortably under 16 GB. And the output was stillright:

Compiler status PASS · MB_TRACED
DEVICE_PARIS True
DEV GEN: 'The capital of France is Paris.'
prefill 232 ms · neff 26.7 GB

Enter fullscreen mode

Exit fullscreen mode

The 26B MoE ran on a2-coreinf2.8xlarge. The "not achievable without fp4" conclusion was rightthat fp4 was out — and wrong about everything else.

## Wall 2: the 8xlarge and the xlarge have the same HBM — but not the same host RAM

Here's the subtlety that trips everyone.inf2.8xlargeandinf2.xlargehave thesame 2 NeuronCoresand 32 GB HBM. The difference ishost RAM: 128 GB vs16 GB. My squeeze fit thedevice. Wouldit fit thehoston the cheapest box?

Compiling won't: the ModelBuilder trace holds an fp32 discovery model + a structure model + an fp32checkpoint dict —~180 GB peak.That OOMs even the 8xlarge's 128 GB (I added a 100 GB swapfile to getthecompilethrough, ~40 min). Butcompiling and deploying are different jobs.Deploying a savedneff doesn't need the model in host RAM at all — the transformer weights live on the device.

So the xlarge deploy is deliberatelyslim(deploy_sqz.py/optb_server_sqz.py):

* Structure(which layers are KV-shared, head dims, sliding window) comes from ameta-devicemodel instantiation —accelerate.init_empty_weights(), ~0 host RAM.
* Word embeddingscome from a standalone 1.48 GBembed_tokens.pttable, loaded once on the host.
* Theneffcarries every transformer weight on the device (torch.jit.load+ oneinitialize_with_saved_weights).
* A40 GB swapfileabsorbs the one-time neff-load peak.

Result on a stock 16 GBinf2.xlarge:

NEFF_LOADED in 112s
DEV GEN: 'The capital of France is Paris.'
PREFILL 250 ms

Enter fullscreen mode

Exit fullscreen mode

Host RSS peaked ~11 GB; swap was barely touched.Compile needs 180 GB; deploy needs a laptop's worth.A 26B model, on a box you'd hesitate to run a 7B on.

## The bug that turned Paris into a wall of spaces

Except the first slim run didn't say Paris. It said:

DEV GEN: ' '
DEVICE_PARIS False

Enter fullscreen mode

Exit fullscreen mode

The neff was proven (it made Paris at compile). So the deploy was feeding it something wrong. Repeatedidentical tokens is the fingerprint ofdegenerate, near-uniform logits— the classic symptom ofembeddings at the wrongmagnitude.

Gemma-4 doesn't use a plain embedding. It usesGemma4TextScaledWordEmbedding, whose forward is:

return
 
super
().
forward
(
input_ids
)
 
*
 
self
.
embed_scale
 
# embed_scale = hidden_size ** 0.5

Enter fullscreen mode

Exit fullscreen mode

The×√hidden_size(= √2816 ≈53) happensinside the embedding, and the model forward doesnotre-normalize — it just doeshidden_states = inputs_embeds. The neff was traced onscaledembeds. Myslim host path used a plaintorch.nn.Embeddingand fedunscaledones —53× too small.Everythingdownstream washed out to noise.

One line:

ie
 
=
 
emb
(
ids
)
 
*
 
(
hidden_size
 
**
 
0.5
)
 
# match Gemma4TextScaledWordEmbedding

Enter fullscreen mode

Exit fullscreen mode

DEV GEN: 'The capital of France is Paris.'. This is the same trap that bit the E2B slim server; when youmove embedding lookup to the host, you inherit whatever the model's embedding class was doing.

## Shipping it: 512/128, published, and a clean-pull proof

I recompiled a production512/128bucket build (512 total / 128 prompt tokens) — same recipe, ~40 minon an 8xlarge with swap, neff26.8 GB, re-validated on the xlarge (loads in 112 s, ~10 GB host peak,Paris). Then I wrapped it in a slim OpenAI-compatible server and published:

* Docker Hubxbill9/gemma4-optb-26b:xlarge— a thin image; the entrypoint pulls the ~28 GB of
artifacts from the HF repo on first start.
* HFxbill9/gemma-4-26B-A4B-it-inferentia2-xlarge(public) — neff + embedding table + config +
server + Dockerfile.

The final proof was the one that matters to anyone but me: acold, clean pull.Fresh spotinf2.xlarge, add swap,docker run, walk away.

READY
 
in
 
490.9
s
 
—
 
slim
 
int
8
-squeeze,
 
ModelBuilder
 
TP=
2
,
 
MAX=
512
 
BUCKET=
128

{
"role"
:
"assistant"
,
"content"
:
"The capital of France is Paris."
}

{
"response"
:
"AWS Inferentia is a purpose-built machine learning accelerator
 designed to provide high-performance, low-cost inference..."
}

Enter fullscreen mode

Exit fullscreen mode

(NoHF_TOKENneeded — the repo is public. The 490 s is one-time cold-EBS neff load, then it serves.)Terminated the box; net ongoing spend, zero.

## The honest caveat

Decode is~6 tok/s.That's the price of theDenseExpertstrick from the last article: computing all128 experts every token instead of the sparse top-8 — ~16× the necessary expert FLOPs, on 2 cores. It'scorrectand it'scheap to host; it is notfast. Making sparse routing actually trace underModelBuilder is the real next expedition, and (see the fp4 detour) "the vendor primitive exists" is notthe same as "it traces." For single-user, cost-sensitive, latency-tolerant serving of a 26B on a $0.76/hrbox, the tradeoff is the right one. For a chatbot under load, it isn't yet.

## Takeaways

1. When something's 3 GB over, don't assume it's the obvious 3 GB.I burned days on fp4 experts; the
fix was quantizing thereplicatedlm_headI'd never looked at. Profile the residency, don't eyeball
the architecture.
2. "Not supported" beats "not documented well."fp4 hasconstantsandpartial code pathsin NxD
0.19 that make it look one commit away. It isn't — the kernels are CPU-only refs or pre-prod. Read the
feature guide's supported list and believe it.
3. Compile-fit and deploy-fit are different budgets.A model that needs 180 GB of host RAM totracecan deploy on 16 GB, because the weights live on the device. Slim host loading + swap is what turns a
24xlarge model into an xlarge product.
4. Moving embedding lookup to the host means inheriting the embeddingclass.Gemma's×√Hscale is
insideGemma4TextScaledWordEmbedding; miss it and you get a confident wall of whitespace.
5. Ship the clean-pull proof."Works on my validated box" isn't a deliverable; "docker runon a
fresh spot instance says Paris" is.

## Artifacts

* Docker Hub:xbill9/gemma4-optb-26b:xlarge
* HF:xbill9/gemma-4-26B-A4B-it-inferentia2-xlarge(public)
* Recipe:tp_mb_moe_sqz.py(all-int8 squeeze: int8 experts + sharded int8lm_head+ int8 shared MLP)
·deploy_sqz.py/optb_server_sqz.py(slim host-embedding deploy)

A 26B mixture-of-experts, on the cheapest accelerator instance AWS rents, for the price of a large coffeeper day. Written with AI assistance in a Claude Code session; every log line quoted is from a real run onreal hardware.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse