---
title: 'Admission Control for Distributed LLM Inference: Cache-Aware Routing, GPU-Aware Signals, and When to Say No | Antonello Fratepietro'
url: https://www.fratepietro.com/2026/admission-control-distributed-llm-inference
site_name: tldr
content_file: tldr-admission-control-for-distributed-llm-inference-ca
fetched_at: '2026-10-23T15:40:33.735119'
original_url: https://www.fratepietro.com/2026/admission-control-distributed-llm-inference
author: Antonello Fratepietro
date: '2026-10-23'
published_date: '2026-10-23T00:00:00+02:00'
description: 'Most writing on distributed LLM inference is about routing: which GPU should serve this request. The other half of the problem is admission control: whether to accept a request now, queue it, or shed it. Here is the five-layer admission pipeline, how vLLM, SGLang, TensorRT-LLM, TGI, NVIDIA Dynamo, llm-d, Ray Serve, Mooncake, and Cognitora implement each layer, and why agentic workloads need admission at the agent level instead of the request level.'
tags:
- tldr
---

Spread an LLM across a fleet of GPUs and most of the engineering attention goes torouting: which replica should serve this request so it reuses a warm KV cache and lands on a GPU that is not already saturated. Cache-aware routing is now table stakes. SGLang’s router, NVIDIA Dynamo’s KV router, llm-d’s prefix-cache scorer, the GKE Inference Gateway, andCognitoraall do some version of it.

Routing assumes the clustercanserve the request somewhere. Under real traffic that assumption breaks several times a day: a batch job starts, an agent fans out forty parallel calls, a product launch triples the request rate. At that point the right question is not “where” but “whether, and when.”

Admission controlis the traffic-management and resource-governance layer that answers it. For every incoming generation request it decides one of three things:acceptit now,queueit, orshedit. The decision is based on available GPU memory (mostly KV cache), compute capacity, and concurrency limits. Without it, queues grow without bound, and the result is predictable: severe tail-latency spikes, memory exhaustion, and cascading timeouts as clients give up and retry into an already overloaded system.

This post treats admission control as a general concept, walks through the layers a serving stack needs, and looks at how the current inference engines and orchestrators implement each one. The last part covers agentic workloads, where request-level admission stops working and the unit of admission becomes the agent.

## 1. Three decisions, three components

Every request in a distributed inference stack passes through three decisions, usually made by different components:

* Admission(whether and when) protects the system as a whole: tenants, priority classes, and the latency SLO.
* Routing(where) uses cache locality and per-node load to pick the best replica.
* Scheduling(how, inside the engine) decides which requests join the next forward pass and what happens when KV memory runs out.

Each component only sees part of the picture. The engine knows its own KV blocks but not the rest of the fleet. The router knows the fleet but sees each node’s state a few hundred milliseconds late. The gateway knows tenants and SLOs but not which GPU holds which prefix. That is why admission control in practice is not one check but a stack of checks spread across all three, which section 5 walks through layer by layer.

## 2. Why LLM traffic breaks classical load balancing

For a stateless web service, admission control is mostly a solved problem: a concurrency limit per replica, a token bucket per client, and a retry policy. LLM inference breaks the assumptions behind those tools in four ways.

Request cost varies by orders of magnitude.A 50-token chat turn and a 120,000-token repository prompt are both “one request.” Their prefill cost differs by more than three orders of magnitude, and their KV cache footprint by the same factor. A concurrency limit of 64 requests means nothing when one of those 64 can occupy half the KV pool.

Output length is unknown at admission time.The decode phase grows KV memory one token at a time until the model emits a stop token. The engine has to admit a request before knowing how much memory it will eventually need. Engines either reserve for the worst case (safe but wasteful) or overcommit and evict later (efficient but disruptive).

Replicas are not interchangeable.With prefix caching, the replica that served turn 5 of an agent session holds 30,000 tokens of reusable KV state. Sending turn 6 anywhere else means recomputing all of it. Cache affinity makes some nodes much better for a given request than others, and that concentrates load on exactly those nodes.

Queued work goes stale.A request that waits 40 seconds in a queue will often be cancelled by its client before it starts. If the engine then runs its prefill anyway, the GPU spends compute on output nobody reads. The TGI maintainersput it plainlywhen users asked why the server returned “Model is overloaded”: refusing early is better than serving old requests in order, because those clients will most likely time out and the work is wasted.

The combined effect is thegoodput cliff. Push an LLM service past saturation and throughput (tokens per second) stays flat or even rises, while goodput (requests that finish within their SLO) collapses. Every request now waits behind every other request, so nobody meets their latency target. Admission control exists to keep the system on the left side of that cliff.

## 3. Cache-aware routing, and why it needs admission control

A quick recap of cache-aware routing, because it creates the hot spots that admission control has to manage.

The router hashes the prompt into fixed-size token blocks andchainsthe hashes so that the digest of blockicovers the entire prefix[0..i]. Because attention is causal, a replica can only reuse blockiif it also holds blocks0..i-1. The useful signal is therefore thelongest contiguous prefixa replica holds, not how many matching blocks it has scattered around. llm-d’sKV-cache indexer documentationhas a clean example: a pod holding blocks B3 and B4 without B0 to B2 scores zero.

Implementations differ in where that prefix knowledge comes from:

Every one of them thenblendsprefix overlap with load. Cognitora’s router, for example, scores each candidate as a weighted sum:

score(n) = 0.55 · kv_overlap + 0.25 · (1 − queue_depth/64)
 + 0.10 · (1 − power/peer_max_power) + 0.10 · free_kv_blocks/total_kv_blocks

llm-d does the same with a prefix-cache scorer, a KV-utilization scorer, and a queue scorer combined by weight, plus aprefix-cache-affinity-filterthat has a “TTFT load gate” to break stickiness when the sticky pods have become much slower than the rest.

The blend handles moderate imbalance. It does not handle saturation. When every replica is busy, the weighted sum still returns a winner: the least-bad node. The request is dispatched, joins a long local queue, and waits.Routing always picks a node. Admission control is the only layer allowed to pick none.

## 4. GPU-aware signals: what “busy” actually means

Admission control is only as good as its definition of load. Request count is the signal every generic load balancer has, and it is the weakest one for LLMs. The systems below use better ones:

* KV cache utilization: fraction of KV blocks in use. This is the closest signal to the actual memory limit. llm-d’s default saturation threshold is 0.8. Dynamo’s--active-decode-blocks-thresholdis typically set around 0.85.
* KV cache hit rate: fraction of prompt tokens served from cache. High utilization with a falling hit rate means the cache is churning, not working. This is the signal agent-level controllers rely on (section 6).
* Queued prefill tokens: total prompt tokens waiting for prefill. This predicts TTFT far better than request count, because prefill time scales with tokens. vLLM’smax_num_queued_tokensand Dynamo’s--active-prefill-tokens-thresholduse it.
* In-flight tokens: llm-d’stoken-load-scoreruses estimated tokens in flight instead of request count, normalized against a 4Mi-token threshold.
* Engine queue depth: requests waiting inside the engine scheduler. Cheap to read and fast to react, but blind to request size.
* Power and thermals: watts against a per-node cap, from NVML, ROCm SMI, or Redfish. Cognitora uses this as a soft filter that prefers under-cap nodes and as a routing term.
* Hardware capability: VRAM size and GPU vendor, so a 70B model never lands on a 24 GB card in a mixed fleet.

The pattern across all of them:measure load in the unit that actually runs out, which is KV memory and prefill tokens, not HTTP requests.

## 5. The five layers of an admission pipeline

An effective LLM gateway or serving engine applies admission control as a sequence of checks, ordered from cheapest to most expensive. Each layer rejects a different kind of request, and each one is cheaper to fail at than the next.

The order is not strict across products (some engines run the KV check after queueing, some gateways run priority before queue caps), but the layers are the same everywhere.

### 5.1 Request and validation layer

The first layer rejects requests that should never reach a GPU: malformed JSON, unknown models, missing or invalid credentials, oversized bodies, and parameters outside allowed limits. It costs microseconds and protects every layer behind it.

Examples from the systems I looked at:

* TGIvalidates in its Rust router before queueing:--max-stop-sequences,--max-best-of,--max-top-n-tokens, and--max-client-batch-sizeall bound what a single request can ask for. Violations return 422validationerrors.
* NVIDIA Dynamocaps request body size withDYN_HTTP_BODY_LIMIT_MB(192 MB by default), which matters once multimodal inputs carry images.
* Cognitoraruns auth (API key or OIDC) and a per-subject rate limit before any prefix hashing or routing work.
* Every OpenAI-compatible serverrejects unknown model names with 404 before touching the scheduler.

Rate limits per API key belong here too. They are not capacity-aware, but they stop a single client from monopolizing the queue before capacity-aware layers ever see the traffic.

### 5.2 Context-window and budget validation

The second layer checks whether the request can fit in the model at all:input_tokens + max_output_tokensagainst the model’s maximum sequence length. A request that fails here would eventually crash or be truncated, so rejecting it immediately is strictly better.

* vLLMrejects prompts whose length plus requestedmax_tokensexceedsmax_model_lenwith a 400 error. Ifmax_tokensis unset, it fills the remaining context.
* TGIenforces--max-input-tokensand--max-total-tokensper request and returns 422 on violation.
* Cognitorausesmax_tokensto derive each request’s implicit deadline (ttft_slo + max_tokens × tpot), so the budget feeds directly into SLO admission later.

This layer also deserves more attention than it usually gets, becausemax_output_tokensis the worst-case KV reservation. A client that sendsmax_tokens: 32000for a reply that ends after 200 tokens makes every conservative scheduler reserve or predict far more memory than it needs. SGLang’stuning guidecalls out exactly this case: low KV usage with a non-empty queue often means users send largemax_new_tokensand stop early. Tight per-route or per-tenant limits onmax_tokensincrease effective capacity without touching the GPU.

### 5.3 Token-budget and KV cache admission

The third layer asks the question that is unique to LLM serving:can the GPU hold this request’s KV cache right now, without triggering an out-of-memory error or evicting someone else?This happens inside the engine scheduler, on every iteration, and it is where the “unknown output length” problem lives. Engines take different positions on it.

vLLMcaps concurrency withmax_num_seqs(sequences per iteration) andmax_num_batched_tokens(tokens per iteration), and overcommits KV memory. When the pool runs out mid-decode, the schedulerpreemptsa running request and, in V1, recomputes it from scratch later (PreemptionMode.RECOMPUTE). Thetuning guiderecommends loweringmax_num_seqsormax_num_batched_tokenswhen preemption warnings show up. A newermax_num_active_seqslets you cap how many requests enter RUNNING without shrinking CUDA graph capture.

SGLangadmits requests based on a predictednew-token ratio: an estimate of how much each running request will still grow.--schedule-conservativenessscales that estimate. When the prediction is wrong and the pool fills, SGLangretractsrunning requests (--retraction-policy lengthorpriority). KV token usage below 0.9 with a non-empty queue means the scheduler is too conservative. FrequentKV cache pool is full. Retract requests.warnings mean it is too aggressive.

TensorRT-LLMmakes the tradeoff an explicit policy.GUARANTEED_NO_EVICT(the default) reserves enough KV for each admitted request to finish, so a started request is never paused.MAX_UTILIZATIONpacks requests aggressively and pauses them when memory runs out. Arecent benchmark reportmeasured MAX_UTILIZATION on v1.2.1 under KV oversubscription at a 40% throughput drop and 9x worse p99 TPOT, while the two policies were equivalent when the working set fit in the pool. The gap mostly disappeared on 1.3.0rc22, but the lesson holds: overcommitting memory only pays off while eviction stays rare.

At the fleet level, the same question gets asked with fleet-wide telemetry.NVIDIA Dynamo’sbusy thresholdsmark a worker as busy when its decode KV block utilization (--active-decode-blocks-threshold) or active prefill tokens (--active-prefill-tokens-threshold) cross a limit, and remove it from the candidate set.llm-d’s saturation detector does the same withkvCacheUtilThreshold(default 0.8) and engine queue depth. Two details from the Dynamo docs are worth copying:

* Decode-block thresholds only work if output tokens are counted (--router-track-output-blocks). Otherwise a long generation can fill KV without the router ever seeing the threshold crossed.
* The most common production symptom is a threshold that is accepted at startup but never fires, because worker load events are not reaching the frontend. Check telemetry before tuning.

Engine memory admission controlswho runs next, notwho waits. Every request that does not fit stays in a waiting queue, which brings us to layer four.

### 5.4 Queue-capacity backpressure

The fourth layer enforces a strict maximum on how much work can wait. Past that limit, new requests get a fast rejection (HTTP 429, 503, or 529, ideally withRetry-After) instead of joining a queue that only grows. This is the layer that prevents the unbounded-queue failure mode directly.

At the engine:

* TGI:--max-concurrent-requests(default 128) is a semaphore in the router. Request 129 gets HTTP 429 with"error_type": "overloaded". This has been in TGI since 2023 and was the first widely deployed example of “say no early” in an LLM server.
* vLLM: the waiting queue was unbounded for a long time (RFC #18826documents the OOM risk). Recent releases addmax_num_queued_reqs, which caps waiting plus running requests across all data-parallel ranks and returns HTTP 503 so a load balancer can retry elsewhere. A second knob,max_num_queued_tokens, caps the total prompt tokens waiting for prefill. The docs suggest sizing it astarget_TTFT × prefill_throughput, which turns a queue cap into aTTFT budget: if the backlog would take longer than your TTFT target to clear, new requests are rejected.
* SGLang:--max-queued-requestsaborts incoming requests when the waiting queue is full (the flag is ignored in disaggregation mode).

At the gateway:

* Ray Serveenforcesmax_ongoing_requestsper replica (default 5, a value LLM deployments always raise) andmax_queued_requestsper caller. Past the queue limit it raisesBackPressureError, mapped to HTTP 503 by default.BackpressureConfiglets you return 429 instead and attach aRetry-Afterheader.
* Cognitorakeeps a lock-free atomic counter per(model, role)pair, where role is prefill, decode, or both. A request takes a permit before dispatch. If the counter is atmax_queuethe request gets an immediate 429 with no buffering, and the permit is released automatically when the stream ends. Keying on role matters in disaggregated setups: long prompts count against the decode pool’s budget, short colocated ones against the shared pool, so a burst of long prompts cannot exhaust capacity for short chat turns.
* NVIDIA DynamoreturnsHTTP 529 (Overloaded)when registered workers exist but all of them are over a busy threshold, kept distinct from 503 (no workers at all). It also has--router-queue-threshold, whichdefersthe routing decision instead of rejecting: the request waits in the router and is routed later with fresher load metrics.

A fixed queue cap is simple and predictable. Its weakness is that the right number depends on the prompt length mix, which changes during the day. vLLM’s token-denominated cap and Dynamo’s utilization thresholds are both attempts to track that mix instead of guessing a constant.

### 5.5 Priority shedding and flow control

The fifth layer decideswhichtraffic gets the capacity that exists. Requests are sorted into tiers. Under heavy load, lower-priority or “sheddable” requests are dropped first so high-priority SLAs hold.

llm-d and the Kubernetes Gateway API Inference Extensionhave the most complete implementation. Behind a feature gate, the Endpoint Picker runs a fullflow controllayer. Theflow control guidedescribes the loop:

1. Requests are sorted into queues by flow (tenant or workload) and priority band.
2. A dispatcher picks the next request by strict priority, then by a fairness policy within the band.
3. Before dispatching, it asks the saturation detector whether the pool has room. If not, dispatch halts and the request stays in the gateway queue.

Requests withnegative priority are sheddable: they can be rejected or evicted when a band is full, while protected requests are never displaced. Every queued request has a TTL (defaultRequestTTL), and clients can shorten it with anx-llm-d-inference-ttlheader. A separatenoEndpointRequestTTLturns the queue into a waiting room for scale-from-zero, returning 503 instead of 429 when it expires.

The tuning advice gets at a central design question:where should the queue live?SetqueueDepthThresholdto 1 and nearly all queuing happens centrally in the gateway, which gives full control over priority, fairness, and late routing. Set it higher and the engines keep a small buffer, so continuous batching always has work. The guide calls the target a “healthy buffer”: enough queued work on the model servers to form efficient batches, and no more. Endpoints whose metrics are older thanmetricsStalenessThresholdcount asfully saturated, so if the gateway loses its view of the fleet, it stops dispatching instead of guessing.

Priority also exists inside the engines:

* vLLM--scheduling-policy priorityorders the waiting queue by request priority.
* SGLang--enable-priority-schedulinglets high-priority requests preempt running ones above a configurable priority gap. When--max-queued-requestsis hit, it aborts thelowest-priority waiting requestinstead of the new one if the new one outranks it.
* Dynamoacceptsnvext.agent_hints.priorityandstrict_priorityto order its router queue.

Policy can go beyond priority.Cognitorapolls a grid-intensity provider (static, Electricity Maps, or WattTime) and sheds requests markedX-CGN-Priority: lowwhile grid carbon intensity exceeds a threshold. Normal and high-priority traffic is always admitted, so deferrable batch work moves to cleaner hours without touching interactive traffic.

### 5.6 Beyond the five layers: SLO-feasibility admission

The five layers answer “is there room?” A sharper question is:can this specific request still meet its SLO?If not, rejecting it immediately is better for everyone, including the caller, who can retry elsewhere.

Mooncake(Moonshot AI’s serving system for Kimi) is the clearest production example. Its prefill and decode pools are disaggregated, and it measures load as SLO satisfaction: predicted TTFT against the TTFT target on prefill nodes, predicted time-between-tokens against the TBT target on decode nodes.Two findingsfrom the paper apply to any disaggregated system:

* Early rejection.Checking decode capacity only after prefill wastes the prefill compute of every request rejected at decode time. Mooncake evaluates the larger of the two pool loadsbeforeprefill starts.
* Prediction beats measurement.Early rejection based on current decode load produced anti-phase oscillation: prefill accepts a wave, decode fills up a few seconds later, the conductor rejects everything, decode drains, repeat. Mooncake fixed it by predicting decode load at the time the request would actually arrive there.

Cognitorahas a simpler version. The router estimates TTFT on the chosen node from its queue depth and per-replica concurrency, and returns 429 if the estimate exceeds the request’s deadline. It is a coarse model, but it rejects requests that are clearly doomed instead of queueing them behind a noisy neighbor.

Research systems push the idea further:

* SCORPIOuses a TTFT guard (least-deadline-first ordering plus rejection of unattainable requests) and a TPOT guard (admission based on per-request decode-speed budgets), reporting up to 14.4x goodput over throughput-oriented baselines.
* SLOs-Serveusessoftadmission: requests whose SLO is unattainable on one replica are routed to another or served best-effort instead of dropped.
* JITServe(NSDI 2026) schedules with imprecise request information and refines its estimates as generation progresses, giving each request just enough bandwidth to meet its SLO.
* Cascadecomputes a per-requestlatency budget(SLO minus predicted remaining service time) and uses it to drive both scheduling and KV tier decisions.

The shared idea:admission based on SLO feasibility, not utilization. Utilization tells you the GPU is busy. Feasibility tells you whether a specific request is worth starting.

## 6. Agentic workloads: changing the unit of admission

Everything above treats therequestas the unit of admission. For agents, that assumption breaks.

An agent is a long-lived, stateful loop: generate, call a tool, wait, generate again with a longer context. Between steps its KV cache sits idle in GPU memory while the tool runs. Request-level admission sees each step as an independent request and has no idea that the idle 40,000-token prefix belongs to an agent that will be back in two seconds.

### 6.1 Agent-level admission: CONCUR

CONCUR(Chen et al., PMLR 2026) names the resulting failuremiddle-phase thrashing. From trace analysis of DeepSeek-V3 agents in batch inference, it identifies three phases:

1. Warmup.Contexts are short and share prompt prefixes. KV hit rates approach 90%, and adding concurrency increases throughput.
2. Middle phase.Agents accumulate history. KV usage sits at 80% to 100% while the hit rate collapses. Paused agents lose their prefixes to LRU eviction while they wait on tools, then pay a full recompute when they resume. Recomputation accounted for 49.1% of end-to-end latency, and this phase covered more than 90% of execution time. Adding agents in this phasereducesthroughput.
3. Cooldown.Agents finish, memory frees up, and hit rates partially recover.

The important observation is that the GPU is not out of memory in the classical sense. It isthrashing: memory is full of state that gets evicted just before it would have been reused. Request-level controls do not fix it. In the paper’s measurements, SGLang’s hit rate fell to 35% at high concurrency, and a request-level admission cap still dropped to 32%.

CONCUR’s answer is to make theagentthe unit of admission and to regulate the number of active agents the way TCP regulates a congestion window, withAIMD(additive increase, multiplicative decrease). It sits as middleware between the agent framework and an unmodified serving engine, exposes three primitives (admit, pause, resume), and updates the active-agent windowWfrom two engine signals, KV usageUand cache hit rateH:

Two design choices stand out. Pausing happens only at step boundaries, between a generation and a tool call, so in-flight work is never interrupted. And the multiplicative cut is justified by the cost shape: recomputation scales quadratically with context length, so the controller should leave the thrashing regime quickly rather than gently. The reported result is up to 4.09x batch throughput on Qwen3-32B and 1.9x on DeepSeek-V3.

The paper targets batch agent inference, but the lesson generalizes to any serving stack running agents:cache hit rate is an admission signal, and the right number of concurrent agents is lower than the number of requests the KV pool can technically hold.

### 6.2 Branch-level admission: TAPER (PACE)

A related idea works at a finer granularity: inside a single request. Some reasoning and agent methods split one output into parallelbranchesthat decode concurrently (map, process, reduce). Executing every branch eagerly makes each shared decode step slower, which hurts every other request in the batch. A fixed cap on branches gives up the speedup that made branching worth doing.

TAPER(Gandhi, Hari, Dally, Kozyrakis; NeurIPS 2026), released as thePACEcodebase on top of an SGLang fork, makes branch admission a per-decode-step decision. Every active request is guaranteed one token per step. Extra branches are admitted only when their predicted latency cost, which the authors call thebranch externality, fits within the batch’s current slack budget, using a calibrated step-latency modelT = a + b·n_tokens + c·L_context. Because branches share the request’s prefix KV, expanding or shrinking the width needs no memory reclamation. On Qwen3-32B it reports 1.77x goodput over no branching and 1.48x over eager branching, with more than 95% SLO attainment.

CONCUR and TAPER bracket the same principle from two sides: admitagentsacross requests, and admitbrancheswithin a request, using live feedback instead of fixed caps.

### 6.3 A different “admission control”: agent memory (A-MAC)

The term also shows up in agent architectures with a completely different meaning, and it is worth separating the two to avoid confusion.

A-MAC(Adaptive Memory Admission Control, Workday AI, 2026) has nothing to do with GPU queues. It governswhat information gets written into an agent’s long-term memory store. Without it, agents either store everything, including hallucinated and obsolete facts, or rely on opaque LLM-driven memory policies that are expensive and hard to audit. A-MAC scores each candidate memory on five interpretable factors (future utility, factual confidence, semantic novelty, temporal recency, and a content-type prior) and admits it only if the weighted score clears a learned threshold. On the LoCoMo benchmark it reports an F1 of 0.583 with 31% lower latency than LLM-native memory systems, and the content-type prior turned out to be the most influential factor.

The connection to inference admission is indirect but real. Every memory an agent admits is retrieved into future prompts, so a noisy memory store becomes longer contexts, more prefill, and a larger KV footprint per step. Admission at the memory layer is upstream of admission at the GPU layer.

## 7. Side by side

## 8. Design lessons

Reading these systems together, a few rules come out consistently.

Order the checks from cheapest to most expensive.Validation and context checks cost microseconds and should run before any tokenization or routing. Queue and priority checks come before dispatch. The KV check happens in the engine. Mooncake’s early rejection is the same principle applied to disaggregation: a request rejected at decode time has already consumed prefill compute.

Admit before the first byte of a streaming response.Once a server has sent200 OKand opened a server-sent event stream, it can no longer return a 429. The client gets a broken stream instead of a clean retry signal.

Boundmax_tokens.It is the worst-case KV reservation. Tight defaults per route or tenant increase effective capacity for free.

Measure load in tokens and KV blocks.Request counts are easy to read and almost meaningless for LLMs. vLLM’smax_num_queued_tokens, Dynamo’s prefill-token threshold, and llm-d’s token-load scorer all moved to token-denominated signals for the same reason.

Watch hit rate, not only utilization.Full KV memory with a high hit rate is healthy. Full KV memory with a collapsing hit rate is thrashing, and adding work makes it worse. CONCUR’s control loop is built on exactly this distinction.

Decide where the queue lives.A queue in every engine gives the best batching but loses control over priority and placement: once a request sits in replica A’s queue, it cannot move to replica B when B frees up first. A central gateway queue keeps that flexibility. The llm-d “healthy buffer” setting is a good default.

Treat cache affinity as a load source.Prefix-aware routing concentrates hot sessions on a few replicas. Admission and routing must share load signals so that a sticky node at 95% KV utilization stops attracting traffic, even when it holds the perfect prefix.

Account for both pools in disaggregated serving.Prefill and decode saturate at different times. Admission needs a budget per role (Cognitora’s per-(model, role) counters, Dynamo’s separate prefill and decode thresholds) and ideally a prediction of decode load when the request will get there (Mooncake).

Use feedback and prediction to avoid oscillation.Telemetry is always a few hundred milliseconds to a few seconds old. Admission that reacts only to current load accepts a burst, overloads, rejects everything, and repeats. AIMD windows (CONCUR), predictive admission (Mooncake), deferral queues that route with fresh metrics (Dynamo), and hysteresis between thresholds all dampen the cycle.

Choose fail-open or fail-closed on purpose.When telemetry disappears, the admission layer has to pick one. llm-d treats stale metrics as saturated and stops dispatching, which protects GPUs but can halt traffic. Cognitora’s carbon admission fails open until the first successful poll, which keeps serving but loses the policy. Both are defensible. Leaving the choice to whatever the code happens to do is not.

Make rejections actionable.The status codes differ across systems: 429 (TGI, Cognitora, optionally Ray Serve and llm-d), 503 (vLLM, Ray Serve default, llm-d with no endpoints), 529 (Dynamo). What matters is that clients can telloverloaded, retry soonapart frominvalid, do not retry, that aRetry-Afterheader is present where possible, and that client SDKs retry with exponential backoff and jitter.

Let clients say what they can tolerate.Priority headers, sheddable classes, request TTLs (x-llm-d-inference-ttl), explicit deadlines, andX-CGN-Priority: lowall tell the system which requests can wait or be dropped. Batch jobs and evaluation runs should almost always be sheddable.

## 9. A practical starting point

If you run a fleet of vLLM replicas behind a cache-aware router, a reasonable first configuration maps one-to-one onto the five layers:

1. Validation: authenticate, rate-limit per API key, and cap body size and sampling parameters at the gateway.
2. Context and budget: setmax_model_lendeliberately and enforce per-routemax_tokensdefaults well below the context window.
3. KV and token budget: setmax_num_seqsandmax_num_batched_tokensfor your GPU and model, and watch the preemption counter. At the router, mark replicas busy at around 0.8 to 0.85 KV utilization.
4. Queue capacity: bound the engine queue withmax_num_queued_reqs(roughlydata_parallel_size × max_num_seqsplus a small buffer) andmax_num_queued_tokens = target_TTFT × measured_prefill_throughput. Return 429 or 529 withRetry-After.
5. Priority and flow: tag interactive traffic as protected and batch or evaluation jobs as sheddable, with a queue TTL shorter than the client timeout.

If agents make up a large share of traffic, add a sixth control: capconcurrent agents, not just concurrent requests, and lower the cap when the KV hit rate drops while utilization stays high.

Then alert ongoodput, not throughput: the percentage of requests meeting their TTFT and TPOT targets, alongside the rejection rate per layer and reason. And load-test past saturation on purpose. The behavior of a serving system at 150% of capacity says more about its design than its peak tokens-per-second number.

Related reading on this blog:LLM Inference: a learning roadmap,llama.cpp, vLLM, and SGLang: Three Approaches to LLM Inference,Cognitora v0.9.1: gossip discovery, live KV prefix, and a native engine, andGoogle Cloud agentic AI architecture: private inference networking.