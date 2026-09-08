---
title: 'GitHub - MiaAI-Lab/DeepSeek-v4-Flash-DSpark-2x-DGX-Spark: DeepSeek-v4-Flash 0731 recipe for 2x DGX Sparks · GitHub'
url: https://github.com/MiaAI-Lab/DeepSeek-v4-Flash-DSpark-2x-DGX-Spark
site_name: github
content_file: github-github-miaai-labdeepseek-v4-flash-dspark-2x-dgx-sp
fetched_at: '2026-09-08T14:53:45.952783'
original_url: https://github.com/MiaAI-Lab/DeepSeek-v4-Flash-DSpark-2x-DGX-Spark
author: MiaAI-Lab
description: DeepSeek-v4-Flash 0731 recipe for 2x DGX Sparks. Contribute to MiaAI-Lab/DeepSeek-v4-Flash-DSpark-2x-DGX-Spark development by creating an account on GitHub.
---

MiaAI-Lab

 

/

DeepSeek-v4-Flash-DSpark-2x-DGX-Spark

Public

* NotificationsYou must be signed in to change notification settings
* Fork178
* Star1.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

401 Commits
401 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
docs
docs
 
 
files
files
 
 
lmcache
lmcache
 
 
patches
patches
 
 
recipe
recipe
 
 
results
results
 
 
scripts
scripts
 
 
tests
tests
 
 
vllm_patch_gb10
vllm_patch_gb10
 
 
.env.dspark.example
.env.dspark.example
 
 
.gitignore
.gitignore
 
 
AUDIT.md
AUDIT.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CREDITS.md
CREDITS.md
 
 
Dockerfile.gb10-dsv4-dspark
Dockerfile.gb10-dsv4-dspark
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build-dspark-vllm-runtime.sh
build-dspark-vllm-runtime.sh
 
 
docker-compose.dspark-nfs.override.yml
docker-compose.dspark-nfs.override.yml
 
 
docker-compose.dspark.yml
docker-compose.dspark.yml
 
 
docker-compose.stage-c.override.yml
docker-compose.stage-c.override.yml
 
 
dspark-numeric-knobs.sh
dspark-numeric-knobs.sh
 
 
image.png
image.png
 
 
logs-deepseek-v4-flash-dspark.sh
logs-deepseek-v4-flash-dspark.sh
 
 
pi-models.dspark.example.json
pi-models.dspark.example.json
 
 
prepare-dspark-model-cache.sh
prepare-dspark-model-cache.sh
 
 
smoke-deepseek-v4-flash-dspark.sh
smoke-deepseek-v4-flash-dspark.sh
 
 
start-deepseek-v4-flash-dspark.sh
start-deepseek-v4-flash-dspark.sh
 
 
start-tp3.sh
start-tp3.sh
 
 
status-deepseek-v4-flash-dspark.sh
status-deepseek-v4-flash-dspark.sh
 
 
stop-deepseek-v4-flash-dspark.sh
stop-deepseek-v4-flash-dspark.sh
 
 
validate-dspark-config.sh
validate-dspark-config.sh
 
 
View all files

## Repository files navigation

# DeepSeek V4 Flash Vision-Exp DSpark on 2x DGX Spark

byMia'a AI Lab

Two-node DGX Spark recipe fordeepseek-ai/DeepSeek-V4-Flash-Vision-Exp: vLLM TP=2,
DSpark speculative decoding,1M-tokenceiling,nvfp4_ds_mlaKV. Nativeimagesupport is a startup hotfix on the Anemll 0.1.1 runtime (ViT + Aligner
from the Vision-Exp checkpoint, OpenAIimage_url/<image>path</image>).
There isno video encoderin the official weights; GIF is a still frame.
The old Qwen3-VL sidecar / MCP path is removed.

Default image:ghcr.io/anemll/dspark-vllm-gx10:0.1.1

Numbers:results/RESULTS-2026-08-14.md(dated
tables, method, historical lanes). Checkpoint / encoder:docs/DEEPSEEK_V4_FLASH_0731.md.

## Quick start

Run everything from theheadnode. You need two DGX Sparks, RoCE/NCCL
working, and the same image on both. By default each node has its own
HuggingFace checkpoint (preparecopies onto the worker). SetDSPARK_WORKER_HF_NFS=1to keep weights only on the head: the worker
mounts that cache over NFSv4 on the ConnectX link (same pattern as
Qwen3.8-Flash-vLLM).

1. Envcp .env.dspark.example .env.dsparkSet at least:WORKER_HOST,MASTER_ADDR,NCCL_IB_HCA,NCCL_SOCKET_IFNAME(and matchingTP_/GLOO_IF names),VLLM_HOST_IP,WORKER_VLLM_HOST_IP,HF_CACHE.WORKER_HF_CACHEis the worker checkpoint path. WhenDSPARK_WORKER_HF_NFS=1,
it is the worker's local JIT overlay on the NFS mount.
If the worker checkout is not the same path, setWORKER_DIR/WORKER_SCRIPT_DIR.Example fabric (edit f0 vs f1 and GID for your ring):WORKER_HOST=10.0.0.2MASTER_ADDR=10.0.0.1VLLM_HOST_IP=10.0.0.1WORKER_VLLM_HOST_IP=10.0.0.2NCCL_IB_HCA=rocep1s0f1NCCL_SOCKET_IFNAME=enp1s0f1np1DSPARK_VLLM_IMAGE=ghcr.io/anemll/dspark-vllm-gx10:0.1.1Leave serving knobs at the defaults unless you mean to change them.
Meaningful on/off flags (ABLITERATED, thinking, hotfixes) are
listed under.env.dspark switches.
2. Image on both nodesdocker pull ghcr.io/anemll/dspark-vllm-gx10:0.1.1Repeat on the worker (or pull there via ssh). Start refuses to launch if
either node is missing the image.
3. Weights on the head./prepare-dspark-model-cache.sh --officialUse--abliteratedor--yes(readsABLITERATEDfrom.env.dspark).
Abliterated weights are gated (HF_TOKEN). Prepare forces HF
online even ifHF_HUB_OFFLINE=1, then you can serve offline.
DefaultDSPARK_WORKER_HF_NFS=0also downloads onto the worker. After
the cache is complete, keepHF_HUB_OFFLINE=1. SeeWorker weights over NFSto skip the
second copy.
4. Optional CPU gates(no GPU; will not measure tok/s)bash scripts/ci-validate.sh
5. Start(worker first, then head)./start-deepseek-v4-flash-dspark.shOne-shot bind override:./start-deepseek-v4-flash-dspark.sh --host 0.0.0.0 --port 9000.
After a reboot, dockerd may already have restored the ranks (restart: unless-stopped); start then exits3(already running), not 1. That is expected — do not./stopunless you want a cold start. systemd:SuccessExitStatus=3.Optionalthree Sparks (TP=3)is a separate launcher so.envcannot flip the 2-node path:./start-tp3.sh(needsWORKER2_HOST; seeOptional: three Sparks (TP=3)anddocs/TP3.md).
6. Check it is upcurl -fsS http://127.0.0.1:8888/v1/models
./smoke-deepseek-v4-flash-dspark.sh
./status-deepseek-v4-flash-dspark.shExpect"id": "deepseek-v4-flash-vision-exp"and"max_model_len": 1048576.
Boot log (trust the live numbers):Available KV cache memory: 17.04 GiB
GPU KV cache size: 2,331,430 tokens
Maximum concurrency for 1,048,576 tokens per request: 2.22x

API:http://HEAD_NODE_IP:8888/v1(VLLM_HOST=0.0.0.0by default).
Head-only tests:VLLM_HOST=127.0.0.1.

Day-to-day:./status-…,./logs-…,./stop-…. Disableearlyoomon both
hosts or it can kill vLLM under deep-context load.

## Default profile

Knob

Default

Image

ghcr.io/anemll/dspark-vllm-gx10:0.1.1

Checkpoint

official Vision-Exp @ 
86f746b36186f0e567729a5c06a8c918caba82a9
 (
ABLITERATED=0
)

Served name

deepseek-v4-flash-vision-exp

Context ceiling

MAX_MODEL_LEN=1048576
 (1M)

Concurrent seqs

MAX_NUM_SEQS=6

Batch tokens

MAX_NUM_BATCHED_TOKENS=8192

KV

nvfp4_ds_mla
, 
17.04 GiB / 2,331,430 tokens
 on this cluster (util 0.83; Vision-Exp ViT takes more weight RAM than 0731)

Spec

MTP_NUM_TOKENS=6
 (≥ 
dspark_block_size
 5 and divisible by Vision-Exp 
n_predict=3
)

Thinking

DEFAULT_THINKING=low
 (
off
 / 
low
 / 
high
 / 
max
)

Graphs

VLLM_USE_BREAKABLE_CUDAGRAPH=0
 (keep this; unset is slower)

start-*.shexportsGPU_MEMORY_UTILIZATIONfromGPU_MEMORY_UTILIZATION_TEXT. Do not setGPU_MEMORY_UTILIZATIONby hand.

max_model_lenandmax_num_seqsareceilings, not reservations. The
limit issum(live tokens) ≤ KV pool. Six normal agent turns fit; six
simultaneous full-1M requests do not. SeeHow the KV cache works.

Long coding / big prompts (optional, still 1M ceiling):

MAX_NUM_SEQS
=
4

MAX_NUM_BATCHED_TOKENS
=
16384

GPU_MEMORY_UTILIZATION_TEXT
=
0.87

## .env.dspark switches

Copy.env.dspark.example→.env.dspark. Start syncs
it to the worker.Restart both ranksafter a flip (./stop-…then./start-…). Do not setDSPARK_MODELorGPU_MEMORY_UTILIZATIONby hand.

NCCL/RoCE, CUDA arch, and compile knobs stay in the example file — they are
cluster wiring, not product switches. Full Anemll vs Stage-C matrix:docs/ENVS.md.

### Weights

Variable

Default

What it does

ABLITERATED

0

0
 = official 
deepseek-ai/DeepSeek-V4-Flash-Vision-Exp
 @ 
DSPARK_REVISION
. 
1
 = 
Keys abliterated
. Start and prepare pick the HF id from this flag. Gated; 
prepare --abliterated
 needs 
HF_TOKEN
.

DSPARK_REVISION

86f746b36186f0e567729a5c06a8c918caba82a9

Official Vision-Exp pin. Empty = tip of 
main
.

DSPARK_REVISION_ABLITERATED

empty

Abliterated pin. Empty = tip of that repo.

DSPARK_MODEL_OFFICIAL
 / 
DSPARK_MODEL_ABLITERATED

the two HF ids above

Override only if you intentionally swap the repo id. Do not point this at the 0731 ablit dump — that drops 
image_url
.

SERVED_MODEL_NAME

deepseek-v4-flash-vision-exp

Space-separated aliases; clients may send any alias as 
model
. Startup probes, warmup, and smoke use the first alias.

HF_HUB_OFFLINE

1

1
 after the hub cache is warm. Prepare forces online for the download.

DSPARK_WORKER_HF_NFS

0

0
 (default) = bind 
WORKER_HF_CACHE
 as a second copy (
prepare
 downloads on the worker). 
1
 = worker mounts head 
HF_CACHE
 over NFSv4 on ConnectX (no local checkpoint).

FlipABLITERATEDlike this:

#
 in .env.dspark

ABLITERATED=1

./prepare-dspark-model-cache.sh --yes 
#
 or --abliterated / --official

./stop-deepseek-v4-flash-dspark.sh
./start-deepseek-v4-flash-dspark.sh

--officialwritesABLITERATED=0;--abliteratedwrites1.

### Worker weights over NFS (optional)

Default isoff:DSPARK_WORKER_HF_NFS=0.preparedownloads the checkpoint
onto the worker as well.

SetDSPARK_WORKER_HF_NFS=1in.env.dsparkto skip that second Hub download.
Start then exports the headHF_CACHEvia NFSv4 onNCCL_SOCKET_IFNAME(ConnectX). A live exporter on that address is reused (for example Qwen'svllm-fn-nfs); otherwise start brings updspark-nfs. The worker Docker
volumedspark-hfmounts the share read-only. Triton, TileLang, vLLM,
FlashInfer, CuTe, and NCCL-FR caches stay on the worker host as overlays
underWORKER_HF_CACHE../stop-deepseek-v4-flash-dspark.sh --nfstears
down onlydspark-nfs, not Qwen's share.

DSPARK_WORKER_HF_NFS
=
1

#
 NFS_SERVER_IP=10.0.22.1 # optional; default is IPv4 on NCCL_SOCKET_IFNAME

If official Vision-Exp is already cached, overlay the 26 edited shards
(~87 GiB) instead of re-fetching the full ~157 GiB dump:

python3 scripts/overlay-vision-exp-ablit-cache.py

The 0731 abliterated freeze stays on branch0731-ablit.

Images: OpenAIimage_url(JPEG/PNG/GIF/WebP; GIF is still-frame). No video.
Images belong inusermessages only. A structuredimage/image_urlpart (or the raw<｜deepseek_image｜>token) onsystem,assistant,tool, orfunctionreturns HTTP 400. Tool/functiontextthat quotes<image>tags is allowed; putting a vision-tool result onrole: "tool"asimage_urlis not. That 400 is not retried by typical OpenAI clients, and
the rejected turn stays in history, so later messages keep failing until
that tool message is dropped (issue #178).
Put screenshots on auserturn instead. Default cap 8 images
(LIMIT_MM_PER_PROMPTis JSON{"image":8};image=8is converted). Example:

{
"model"
:
"
deepseek-v4-flash-vision-exp
"
,
"messages"
:[{
"role"
:
"
user
"
,
"content"
:[
 {
"type"
:
"
image_url
"
,
"image_url"
:{
"url"
:
"
data:image/jpeg;base64,...
"
}},
 {
"type"
:
"
text
"
,
"text"
:
"
What is in this picture?
"
}
]}]}

Update the pin like this:

#
 in .env.dspark

DSPARK_REVISION=
<
commit
>

./prepare-dspark-model-cache.sh --yes
./stop-deepseek-v4-flash-dspark.sh
./start-deepseek-v4-flash-dspark.sh

### Thinking, API

Variable

Default

What it does

DEFAULT_THINKING

low

off
 / 
low
 / 
high
 / 
max
. Request-level 
chat_template_kwargs
 still wins.

VLLM_HOST

0.0.0.0

127.0.0.1
 for head-only tests.

VLLM_PORT

8888

Or 
./start-… --port 9000
 for one launch.

An explicitthinking_token_budgetisoff unless you setDSPARK_ENABLE_ISSUE31_GPU_HOTFIX=1(then opt-in per request). Default
stock V2 rejects the field (HTTP 400).DEFAULT_THINKING=maxstill needs a
generousmax_tokensor that budget hotfix, or thinking won't end. SeeThinking-token budgets.

### Serve shape (not on/off, but the knobs that change the lane)

Variable

Default

What it does

MAX_MODEL_LEN

1048576

Per-request ceiling (1M). 
200000
 is the high-concurrency / Keys profile.

MAX_NUM_SEQS

6

Concurrent slots. 
16
 only with the 200K + Stage-C path.

MAX_NUM_BATCHED_TOKENS

8192

Prefill tokens per step. 
16384
 for big-prompt coding.

LONG_PREFILL_TOKEN_THRESHOLD

1024

Issue 
#27
 chunk cap. 
0
 lets one prefill eat the whole batch (decode starves). 
2048
 costs ~1.5 GB of head-node host RAM on GB10 (measured 2026-09-02), keep 1024.

DSPARK_MAX_INFLIGHT_PREFILLS

1

Issue 
#27
 in-flight partial prefills (1–3). Default 
1
 (strictly serialized): the post-#211 exact admission gate is live-qualified at 1 (decode-fairness spread 1.60–1.76×, zero preemptions, repeated fresh boots). 
2
 is an evidence-backed opt-in, operator-qualified post-r3 on TP=2 with 
LONG_PREFILL_TOKEN_THRESHOLD=1024
 (
#217
: 4 × 8K gate26 spread 1.50–1.57×, zero preemptions, TTFT spread 2.1–2.4× vs 4.1× at 
1
), trading admission serialization for TTFT/equity on admission-limited shapes. 
3
 remains an explicit opt-in: a separate, limited 
cap-3 sample
 improved 4 × 8K spread but worsened median TTFT on 8-wide bursts; it is not the same qualification as 
2
. The 2026-09-02 A/B that first favored 
2
 predates the r3 counting fix.

GPU_MEMORY_UTILIZATION_TEXT

0.835

Main GPU util / KV pool size. Larger = bigger KV pool.

LIMIT_MM_PER_PROMPT

{"image":8}

Max images per request (Vision-Exp native 
image_url
). 
image=8
 is converted to JSON for Anemll argparse. No video.

MTP_NUM_TOKENS

6

DSpark draft depth. Vision-Exp 
n_predict=3
 so k must be ≥ 5 and divisible by 3. Capture size = 
seqs * (k+1)
 padded up to a multiple of 8 (48 at 6×6).

VLLM_USE_BREAKABLE_CUDAGRAPH

0

Keep 0.
 Unset enables Anemll’s slower breakable graphs.

VLLM_PREFIX_CACHE_RETENTION_INTERVAL

4096

Issue 
#26
 SWA prefix-cache spacing. Leave unless you are debugging warm-cache hits.

### Hotfixes and diagnostics (on by default unless you skip)

Variable

Default

What it does

DSPARK_SUPPRESS_STOPS_IN_REASONING

1

0
 = client 
stop
 strings can fire inside 
<think>
 (blank 
content
).

DSPARK_SKIP_SUPPRESS_STOPS_HOTFIX

0

1
 = do not apply that patch at all.

DSPARK_SKIP_ISSUE22_HOTFIX

0

1
 = skip the 
nvfp4_ds_mla
 long-context decode fix. Don’t, on this recipe.

DSPARK_SKIP_HOTFIX

0

1
 = skip the six v0.27 perf backports only (#22 still applies).

DSPARK_SKIP_SPIN_WAIT_HOTFIX

0

1
 = leave vLLM shm 
busy_loop_s=1s
 (issue 
#79
 P-core spin on TP=2).

DSPARK_ISSUE43_SCHED_DIAG

0

1
 = one scheduler line per step in the vLLM log (mixed prefill/decode).

DSPARK_ENABLE_ISSUE31_GPU_HOTFIX

0

1
 = apply GPU 
thinking_token_budget
 at boot (fail-closed). Default stock V2; omit-field clients do not need this (
Issue #66
).

DSPARK_ENABLE_SP_INDEXER

0

1
 = sequence-parallel Lightning indexer for prefill chunks ≥ 
DSPARK_SP_INDEXER_MIN_KEYS
 (8192) compressed keys: each TP rank scores half the keys, exact top-k merge. Long-context TTFT lever (
docs/PATCHES.md
).

DSPARK_ENABLE_DEEPGEMM_SM121_ALIAS

0

1
 = alias DeepGEMM 
sm121_*
 indexer-logits headers to the shipped 
sm120_*
 so a cold JIT cache can compile on GB10.

DSPARK_ENABLE_C128A_PREFILL_CACHE

0

1
 = reuse C128A prefill index conversion across layers sharing the current metadata. Pinned Anemll 0.1.1 SM120 path; C4A/decode unchanged, no persistent buffers added (
details
).

ENABLE_VLLM_GB10_PATCH

0

1
 = experimental hybrid NVFP4 plugin (
--quantization modelopt_gb10_hybrid
).

Issue#21 / #26 / #27 / #43Python hotfixes always run at container start
(they are not skipped byDSPARK_SKIP_HOTFIX).#27+ the 1024 prefill cap
is why six huge cold prompts queue instead of starving decode.

### Stage-C only (no-ops on Anemll0.1.1)

These warnUnknown vLLM environment variableon the default image. They
matter only after you switchDSPARK_VLLM_IMAGEto Stage-Candmergedocker-compose.stage-c.override.yml:

VLLM_DSPARK_GPU_REJECTED_CONTEXT_MASK,VLLM_USE_B12X_WO_PROJECTION,VLLM_DSPARK_LOCAL_ARGMAX,VLLM_DSPARK_REPLICATE_MARKOV_W1,DSPARK_SLOT_CLAMP, and the rest of the commented Stage-C block in the
example. SeeOptional: Stage-C / 200K-16.

## What speed to expect

Full tables, method, and older lanes:results/RESULTS-2026-08-14.md.

On thedefault Anemll 1M/6stack:

Workload

What you should see

One chat, any prompt length through 128K

~62–83 decode tok/s after first token

Six short chats
 (hundreds of tokens), 1M still 
allowed

~160–190 tok/s aggregate
 (~30–37 per stream)

Six 
cold 32K–128K
 prompts at once

Prefills are chunked (issue #27), 
one in flight
 by default, the rest queue; 
DSPARK_MAX_INFLIGHT_PREFILLS=2
 opts into two overlapping prefills (pre-r3 A/B: 4 × 8K first tokens at 7.4 / 9.0 / 15.7 / 16.5 s vs 4.7 / 9.4 / 14.3 / 19.3 s at 
1
). ~8 tok/s decode floor while prefills run; 128K × 6 TTFT minutes

|Three Sparks (TP=3,./start-tp3.sh, 16 slots)| Decode ≈ +4–13 % per stream and≈ 200 tok/s aggregate at 16 streams; prefill 4–13 % slower to 64K and ≈ 22 % slower at 128K–256K (5.0 / 18.6 / 91 / 202 s TTFT at 8K / 32K / 128K / 256K vs 4.4 / 18.0 / 75 / 165 s on two nodes). SeeOptional: three Sparks (TP=3). |

That ~170–190 c=6 number issix streams generating, not six huge prefills.
Live 2026-08-14 on this cluster: 256 × c=6 =162agg; 128K × c=1 still75 tok/s/80 sTTFT.

Live 2026-09-02, same lane, sp-indexer on, capture 48, inflight 2
(docs/CLAUDE/ab-results-2026-09-03.md): 256 × c=1 =56tok/s
(8-trial median, 51–67), 256 × c=6 =139agg, 128K × c=1 TTFT78.5 s.
Decode is 15–25 % under the 14 Aug figures above and no.env.dsparkknob
accounts for it; treat the 14 Aug numbers as the best seen, not the norm.

315 / 205 tok/s(200K context, 16 slots) needs theStage-C + Keyspath. The ~182 1M/6 microbench was also measured with that Keys mask; the
sameballparkonshortprompts is already what Anemll does (1 Aug
256 × c=6 =191agg; 14 Aug =162). SettingVLLM_DSPARK_GPU_REJECTED_CONTEXT_MASK=1on Anemll0.1.1is ano-op(warning only). SeeOptional: Stage-C / 200K-16anddocs/ENVS.md.

Capture:docs/benchmarks.png.

## Thinking andmax_tokens

Important

The #31 GPU budget patch isopt-in at boot(DSPARK_ENABLE_ISSUE31_GPU_HOTFIX=1)
and then opt-in per request. Default is stock V2: do not sendthinking_token_budget. When enabled, counters stay on the GPU; omitting the
field does not inject a server-side default. Leave the flag at0unless a
client actually sends the field (Issue #66).

max_tokenscountsthink + answer(reasoning + visible response + tool
markup). WithDEFAULT_THINKING=max, a harness cap of 256/512/800 often
returnscontent: null/finish_reason: lengthbecause reasoning eats the
whole budget —maxships a checkpoint-level directive ("do not stop reasoning
until … no error remains undiscovered") and produced~50,000 reasoning chars
(~12.5k tokens) on a moderate promptin live measurement. So "sizemax_tokensaccordingly" meanstens of thousands of tokens, not a small bump. Raisemax_tokens, set thinkinglow/off, or — withDSPARK_ENABLE_ISSUE31_GPU_HOTFIX=1— send an explicitthinking_token_budget(seeThinking-token budgets) so reasoning is
hard-capped and the rest ofmax_tokensis left for the visible answer.

Clientstopstrings used to fire inside<think>. The recipe appliespatches/hotfix-dsv4-suppress-stops-in-reasoning.pyso they wait for</think>. Opt out:DSPARK_SUPPRESS_STOPS_IN_REASONING=0.

A tool call cut off bymax_tokensused to reportfinish_reason: "tool_calls"withinvalid JSONargumentsand silently poison the transcript (HTTP 400 on
the next turn). The recipe appliespatches/hotfix-dsv4-issue55-tool-truncation.pyso a truncated call reportsfinish_reason: "length"(not"tool_calls") and any
non-JSON-parseableargumentsare dropped. Clients that readlengthcan discard
the in-flight call and retry; normal model-stopped tool calls keepfinish_reason: "tool_calls". Harnesses thatignorefinish_reasonand
blindly replayargsfrom streaming deltas can still hit a 400 - verify your
client drops an in-progress tool call onfinish_reason: "length".

### Thinking-token budgets

max_tokenscapsallnew tokens (reasoning + visible answer + tool
markup).thinking_token_budgetcaps only the reasoning portion and forces a
single</think>at the boundary, leaving the rest ofmax_tokensavailable
for the visible answer or tool call. A budget of0disables reasoning for
that request. Natural</think>remains untouched.

The field is HTTP 400 on stock V2. SetDSPARK_ENABLE_ISSUE31_GPU_HOTFIX=1and
recreate the containers, then send it when a hard cap is required. Omitting it
keepsDEFAULT_THINKINGbehavior. Keepmax_tokenscomfortably above the
thinking budget so the answer has room.

{
 
"max_tokens"
: 
8192
,
 
"thinking_token_budget"
: 
1024
,
 
"temperature"
: 
0.6
,
 
"top_p"
: 
0.95
,
 
"chat_template_kwargs"
: {
"thinking"
: 
true
, 
"reasoning_effort"
: 
"
high
"
}
}

Inspectfinish_reasonandcompletion_tokens.length+ nullcontentmeans think ate the cap.

### Enabling the budget from a client

thinking_token_budgetneeds the boot flagandthe request field — the
server injects no default when the field is omitted. To turn it on, setDSPARK_ENABLE_ISSUE31_GPU_HOTFIX=1, recreate, then send it from the client:

curl / any OpenAI-compatible client— addthinking_token_budgetto the
request body.0disables reasoning for that one call;N>0caps reasoning atNgenerated tokens and leaves the rest ofmax_tokensfor the visible
answer:

curl :8888/v1/chat/completions -H 
'
Content-Type: application/json
'
 -d 
'
{

 "model":"deepseek-v4-flash-vision-exp",

 "messages":[{"role":"user","content":"Design a small rate limiter."}],

 "max_tokens":4096,

 "thinking_token_budget":1024,

 "temperature":0.6,"top_p":0.95,

 "chat_template_kwargs":{"thinking":true,"reasoning_effort":"high"}

}
'

pi— the budget needs the boot flagandthe pi model entry, sopi-models.dspark.example.jsonshipssupportsThinkingTokenBudget: falseto match the server default
(DSPARK_ENABLE_ISSUE31_GPU_HOTFIX=0). Copy it to~/.pi/agent/models.json;
once the boot flag is1, flip the capability on thedeepseek-v4-flash-vision-expmodel and pi attaches athinking_token_budgetwhenever thinking is enabled:

{
 
"id"
: 
"
deepseek-v4-flash-vision-exp
"
,
 
"reasoning"
: 
true
,
 
"compat"
: {
 
"supportsThinkingTokenBudget"
: 
true
,
 
"thinkingFormat"
: 
"
chat-template
"
,
 
"chatTemplateKwargs"
: {
 
"thinking"
: { 
"$var"
: 
"
thinking.enabled
"
 },
 
"reasoning_effort"
: { 
"$var"
: 
"
thinking.effort
"
, 
"omitWhenOff"
: 
true
 }
 }
 }
}

pi sizes the budget from per-level defaults (minimal1024 /low2048 /medium8192 /high16384), always leaving room for the answer; override
values with the pithinkingBudgetssetting. If the capability istruewhile
the boot flag is0, every pi request fails withthinking_token_budget is not yet supported by the V2 model runner— so keep the capabilityfalseunlessDSPARK_ENABLE_ISSUE31_GPU_HOTFIX=1.

## How the KV cache works (why 1M + concurrency is safe)

Knob

Meaning

This build

KV pool

Shared blocks after weights load

2,331,430 tokens / 17.04 GiB @ util 0.83

max_model_len

Per-request 
ceiling

1,048,576

max_num_seqs

Max 
active
 sequences

6

6 × 50k = 300k easy
6 × 200k = 1.2M fits
6 × 500k = 3.0M near/over pool
6 × 1M = 6.0M impossible — extras queue

The boot lineMaximum concurrency for 1,048,576 tokens … 2.22xonly means a
fewsimultaneous full-1Mrequests fit.

## If output garbles, loops, or leaks XML

Validatedirect:8888first, then the agent harness.

1. Same image digest on both nodes (docker image inspect $DSPARK_VLLM_IMAGE).
Compose must use/usr/local/bin/vllm(Anemll), not Stage-C/opt/env.
2. Full 0731 hub snapshot onhead and worker, includingencoding/encoding_dsv4.py.
3. Sendtemperature: 0for deterministic curls. Clear harness fallback lists
so another model cannot poison the transcript.

If direct vLLM is clean and the agent is not, fix the harness — do not switch
to fp8 or a smaller model to hide it.

## Optional: three Sparks (TP=3)

The default lane stays two nodes. A third DGX Spark is opt-in through its own
launcher, so nothing in.env.dsparkcan flip the 2-node path by accident.
Full details, fabric notes and the reasoning:docs/TP3.md.

Before the first boot(the launcher checks these, but does not do them):

* passwordless SSH from the head to spark3;
* the pinnedDSPARK_VLLM_IMAGEalready pulled on spark3 (≈ 19 GB; the
launcher exits with the exactdocker pullcommand otherwise);
* a ConnectX link head ↔ spark3 on its own/24(e.g.10.0.23.1↔10.0.23.3)
plus a LAN interface all three nodes share for the bootstrap (defaultenP7s7).

Spark3 needs no local checkpoint: it mounts the head's HF cache over NFS, and
the launcher creates its directory and syncs compose, env andpatches/.

#
 .env.dspark — in addition to the 2-node settings

WORKER2_HOST=10.0.0.3
WORKER2_VLLM_HOST_IP=10.0.0.3
WORKER2_NFS_SERVER_IP=10.0.23.1 
#
 head IP on the spark1<->spark3 link

WORKER2_NCCL_IB_HCA=rocep1s0f1 
#
 spark3's port facing the head

WORKER2_NCCL_SOCKET_IFNAME=enp1s0f1np1
WORKER2_TP_SOCKET_IFNAME=enp1s0f1np1
WORKER2_GLOO_SOCKET_IFNAME=enp1s0f1np1
TP3_MAX_NUM_SEQS=16 
#
 slots on the 3-node lane only

./start-tp3.sh 
#
 or: ./start-tp3.sh --max-num-seqs 16

scripts/validate_tp3.sh 127.0.0.1:8888 
#
 proves the shard, not just HTTP

./stop-deepseek-v4-flash-dspark.sh 
#
 tears down all three ranks

The first boot compiles for several minutes (empty JIT cache on spark3, new
shard shapes everywhere); wait for the health check rather than restarting.
Boot log must showDSv4 TP pad: heads 64 -> 72 for TP=3on every rank.

What you get:16 slots, about three times the KV cache (≈ 35 GiB per
rank, ≈ 5 M cached tokens), ≈ 200 tok/s aggregate at 16 streams and slightly
faster decode per stream.What it costs:prefill latency, 4–13 % up to
64K and ≈ 22 % at 128K–256K, because in DeepSeek's MLA every rank holds the
full latent KV and the indexer, so attention does not shrink with a third GPU,
while the head pad and the three-node all-reduce add work. Single-user
long-context work is better served by the 2-node lane.

## Optional: Stage-C / 200K-16

Historical overlay imagevllm-dspark-runtime:dspark-nvfp4-stage-c(./build-dspark-vllm-runtime.sh).Bothnodes need that image.
Mergedocker-compose.stage-c.override.yml—./start-*.shdoesnotadd that file by itself — and uncomment the
Stage-C block in.env.dspark.

Profile

Env

Published headline

Keep 1M / 6

MAX_MODEL_LEN=1048576
, 
MAX_NUM_SEQS=6
, Keys mask

~182 agg on a short-prompt microbench

High aggregate

MAX_MODEL_LEN=200000
, 
MAX_NUM_SEQS=16
, Keys mask

315 static / 205 staggered

Issue#27(LONG_PREFILL_TOKEN_THRESHOLD=1024, one in-flight long prefill)
stillserializeshuge cold prefills. Stage-C does not turn 6 × 128K into
six parallel 80 s reads. Details:results/RESULTS-2026-08-14.md,docs/PATCHES.md.

Compose is Anemll-shaped (/usr/local/bin/vllm, hotfixes under/usr/local/lib/...). Treat the first Stage-C boot as an experiment.

## Runtime flags (default compose)

* /usr/local/bin/vllm serve· TP=2 ·mp·nnodes 2
* --kv-cache-dtype nvfp4_ds_mla·--block-size 256
* --max-model-len 1048576·--max-num-seqs 6·--max-num-batched-tokens 8192
* --long-prefill-token-threshold 1024·--enable-chunked-prefill·--async-scheduling
* --max-cudagraph-capture-size=MAX_NUM_SEQS * (MTP_NUM_TOKENS + 1)padded to a multiple of 8 → 48 at 6×6 (plain 42 truncates to 40 and costs 12 % at c=6, measured 2026-09-02)
* --moe-backend flashinfer_b12x·--generation-config vllm
* DSpark:{"method":"dspark","num_speculative_tokens":6,"draft_sample_method":"probabilistic"}

This is theStage C padded NVFP4path (584-byte sparse-MLA envelope vianvfp4_ds_mla). It is not the abandoned 416-byte “true layout” experiment.

Optional GB10 hybrid plugin:ENABLE_VLLM_GB10_PATCH=1 ./start-…(--quantization modelopt_gb10_hybrid). Default off.

CI on every pull request and push tomain(.github/workflows/validate.yml)
isCPU-only(scripts/ci-validate.sh). Live tok/s still needs the 2× Spark pair.

### Strict Responses API verification

Statefulprevious_response_idcontinuation requires enabling the in-memory
store and its exact-source bounded-store backport:

VLLM_ENABLE_RESPONSES_API_STORE
=
1

DSPARK_RESPONSES_STORE_MAX_ENTRIES
=
256

Enabled startup is fail-closed on every rank; the default remains off. SeeBounded Responses API storefor
cap, LRU, failure, and restart semantics. The verifier treats a continuation
404 as configuration failure, not a stateless pass.

After the server is ready, run the dependency-free live verifier to check
Responses text/SSE, stateful tool continuation, strict JSON schema, reasoning,
invalid-field errors, appended multi-turn prefix reuse, and disconnect cleanup:

python3 scripts/verify-responses-api-live.py \
 --base-url http://127.0.0.1:8888/v1 \
 --model deepseek-v4-flash-vision-exp \
 --output results/responses-api-live.json

To exercise the terminal LRU contract, recreate every rank withDSPARK_RESPONSES_STORE_MAX_ENTRIES=2and add--store-capacity 2to the
command. The argument must equal the server cap; values are intentionally
limited to2..16to prevent an accidental large generation sweep.

The verifier above is the store/tool/cache and broad no-regression gate. Issue
#138 has a separate mode-strict verifier for statelessfull-history replay;
it always sendsstore: falseand never usesprevious_response_id. On stock
(default flag0), recreate the containers and pin the reported legacy item to
HTTP 400 while the complete canonical output replay remains HTTP 200:

python3 scripts/verify-issue138-responses-history-live.py \
 --base-url http://127.0.0.1:8888/v1 \
 --model deepseek-v4-flash-vision-exp \
 --expect-legacy rejected \
 --output results/issue138-stock.json

To test compatibility mode, setDSPARK_ENABLE_ISSUE138_RESPONSES_HISTORY_COMPAT=1in.env.dspark, stop and
start the pair so both containers are recreated, then require the same replay
to succeed by rerunning the command above with--expect-legacy acceptedand--output results/issue138-enabled.json.

The enabled run also checks assistant semantic continuity, the exact reported
four-item payload, six malformed/ambiguous neighbors that must remain HTTP 400,
and valid easy/canonical controls. Neither expected mode accepts the opposite
outcome. Changing the flag in either direction requires recreation, notdocker compose restart, because disabling it cannot undo bytes already
patched in a container writable layer.

The broad verifier run intentionally creates a ~21K-token appended conversation
and a forced client disconnect. Use--skip-multiturnor--skip-disconnectonly when the corresponding live behavior is outside the test scope.

## Files

Path

Purpose

results/RESULTS-2026-08-14.md

Dated benches and how to read them

.env.dspark.example

Cluster template

docker-compose.dspark.yml

Anemll serve (installs Vision-Exp encoder + hotfixes)

start-
 / 
stop-
 / 
status-
 / 
logs-
 / 
smoke-*.sh

Two-node ops (
stop --nfs
 also tears down 
dspark-nfs
, not Qwen's 
vllm-fn-nfs
)

prepare-dspark-model-cache.sh

Vision-Exp weights on both nodes (
--official
 / 
--abliterated
). With 
DSPARK_WORKER_HF_NFS=1
, head only; worker mounts over NFS.

files/nfs-share.sh
 / 
files/nfs-server/

NFSv4 exporter for the head HF cache (reuses a live share if one is already up)

docker-compose.dspark-nfs.override.yml

Worker: named NFS volume + local JIT overlays

scripts/overlay-vision-exp-ablit-cache.py

Hardlink official Vision-Exp blobs + copy the 26 ablit shards

scripts/benchmark-0731.py

Prompt × concurrency sweep

scripts/verify-responses-api-live.py

Strict Responses, store LRU, multi-turn cache, and disconnect gates

scripts/verify-issue138-responses-history-live.py

Mode-strict stock/enabled full-history replay gate

docs/ENVS.md

Anemll vs Stage-C env matrix

docs/PATCHES.md

Keys / #27 / #22 notes

patches/

Issue hotfixes applied at container start

docker-compose.stage-c.override.yml

Stage-C-only env injection

build-dspark-vllm-runtime.sh

Optional local Stage-C image

## Credits

Full list:CREDITS.md.

drowzeys ("Keys")— DSpark concurrency
patch, raggedquery_start_loc,nvfp4_ds_mlawiring.

@u1tra_instinct— abliterated Vision-Exp
weights (ABLITERATED=1), from the original repodrowzeys/keys-DeepSeekV4Flash-Vision-EXP-ablit.

Also:tonyd2wild, Rafael Caricio, Fraser Price,Anemll, MiaAI-Lab packaging.

Repo scripts/docs: this repo’sLICENSE. Overlay/runtime: Apache-2.0 / upstream
licenses. Weights and base images have their own terms.