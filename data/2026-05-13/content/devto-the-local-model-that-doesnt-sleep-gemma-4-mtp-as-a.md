---
title: 'The Local Model That Doesn''t Sleep: Gemma 4 + MTP as a Marathon Engine - DEV Community'
url: https://dev.to/gde/the-local-model-that-doesnt-sleep-gemma-4-mtp-as-a-marathon-engine-4c9
site_name: devto
content_file: devto-the-local-model-that-doesnt-sleep-gemma-4-mtp-as-a
fetched_at: '2026-05-13T11:46:14.224567'
original_url: https://dev.to/gde/the-local-model-that-doesnt-sleep-gemma-4-mtp-as-a-marathon-engine-4c9
author: Ertuğrul Demir
date: '2026-05-08'
description: 'This is a submission for the Gemma 4 Challenge: Write About Gemma 4 I set the agent running just... Tagged with ai, gemma, devchallenge, gemmachallenge.'
tags: '#ai, #gemma, #devchallenge, #gemmachallenge'
---

Gemma 4 Challenge: Write about Gemma 4 Submission

This is a submission for theGemma 4 Challenge: Write About Gemma 4

I set the agent running just before midnight, did a quick mental count of my remaining API quota, and went to sleep. I was going to wake up to a finished job. That was the plan, anyway...

What I actually woke up to was a frozen terminal. The agent had stopped in the tenth minute. The remote service had gone down overnight and taken the whole job with it. The task I had given it was simple enough: scrape fifty documentation pages, cross-reference the data across sources, produce a structured summary. It had barely started before the infrastructure I had no control over just switched off.

The model wasn't failing. The problem wasn't intelligence. The problem was that I was building on a foundation I didn't own: a service that could go down, a quota that could run out, and no way to know which one was waiting for me in the morning.

I had always worked with local models on the side: trained them, tested them, liked them. But to be honest, I'd never trusted them much in the past for complex tasks. They were a hobby, not a solution. Too much babysitting required for a real workload. I had filed them under "interesting" and left them there. That frozen terminal moved them to a different folder.

For a long time, the gap between the proprietary giants and the open-source world felt like a canyon. You had the "God-models" in the closed gates: GPT, Claude, Gemini. They could reason through almost anything, but you had to play by their rules. If you wanted actual intelligence, you paid the subscription and accepted their rules.

But lately, that canyon is shrinking.

We're seeing a massive push from the open-weights community. Models like DeepSeek V4, Kimi K2.6, and GLM-5.1 are proving that high-end reasoning is becoming a commodity. The problem is the weight. Unless you're running a server farm or expensive rack, hosting a model at that scale is a logistical nightmare. Great to admire from a distance, but too heavy to actually build with.

Then came the sweet spot: Gemma 4 31B and Qwen 3.6 27B.

Suddenly, the math changed. These models aren't as smart as the trillion-parameter giants, but they fit. They fit on consumer-grade GPUs. They work offline. And they work for free, minus whatever your GPU costs in electricity...

But here is the thing: I don't think the goal of local models is to beat the cloud models at a game of IQ.

For a complex task, you still want the big guns. You want the most powerful model available to handle high-value iterations where precision is everything. That is a sprint.

But what happens when the task isn't a sprint? What happens when you need a model to work for six hours straight? To scrape a hundred pages, try fifty different reasoning paths, fail, pivot, and keep grinding until the job is done?

That is a marathon.

And in a marathon, intelligence is secondary to endurance.

The real advantage of a local setup isn't just privacy or cost. It is the fact that you have a little working engine that doesn't get tired. No rate limits. No monthly token quota. It is completely yours, and you can leave it running all night while you sleep.

The stamina was already there. Then, recently, the Gemma family got something new: a way to run faster without burning out. A marathon engine that also picks up pace doesn't just finish sooner. It fits more work into the same night.

### The Turbocharger (What is MTP?)

Before we get into the build, we need to talk about why this suddenly became possible. If you've been following the Gemma 4 release, you probably saw the termMTP(Multi-Token Prediction).

One thing worth naming up front: MTP isn't just a runtime trick bolted onto inference. It is a training objective. Google trained Gemma 4 from the ground up with auxiliary heads that predict multiple future tokens simultaneously. That structural choice is what lets the speculative-decoding pipeline below run so tightly integrated and efficient, far more so than older bolt-on drafters like Medusa or generic small-model speculative decoding.

On the surface, Google says it makes the models "up to 3x faster." But as a developer, you know that "faster" can mean a lot of things. In this case, it is not about making the GPU clock speed higher. It is about changing how the model actually thinks.

Standard LLMs are autoregressive. They produce one token at a time. It doesn't matter if the next word is completely predictable or a complex logic puzzle: the model spends the same amount of energy and time to generate that one single token. This is the latency bottleneck. Your GPU spends most of its time just moving parameters around, waiting to spit out one word.

MTP fixes this using a technique calledSpeculative Decoding.

Think of it as pairing a heavy target model (the 31B brain) with a lightweight "drafter." The drafter is autoregressive too. It just runs much faster because of its size, producing a short candidate sequence in the time the target would take to produce a single token.

For example, if the model is generating something as predictable as "Once upon a time," the words "in a galaxy far far away" are practically a given in some contexts. A standard model would still grind through each of those words one by one, spending the same compute on a cliché as it would on a genuine reasoning problem. The drafter generates the likely sequence quickly simply because of its small size.

Then the target model steps in. Instead of generating those tokens one by one, it verifies the entire draft in a single parallel forward pass. The same weight load that normally yields one token now yields a lot more (depending on the drafted sequence). If the drafter was fully right, you get the whole sequence accepted in the time it usually takes to generate one word, and the target even throws in one extra token of its own as a bonus. If the drafter was only partially right, the target accepts everything up to the first disagreement, swaps in its own token at that point, and the process continues. Either way, the output follows the same probability distribution as running the target model alone. The acceptance algorithm is a mathematical guarantee, not a heuristic.

The result is a massive win for local agents.

When you are building an agent that needs to iterate, research, and self-correct, you are basically running a loop of "Think → Act → Observe." If every "Think" step takes a minute, your agent is a snail. If MTP cuts that down to a matter of seconds, your agent becomes a real-time engine.

You get the pretty strong reasoning of a 31B model, but it's delivered at the speed of a much smaller one. For a "marathon" task, this is the difference between a project that takes a day and one that finishes by breakfast.

### The Engine Room

Now, the question is: how do you actually run this without your computer turning into a space heater?

When it comes to local inference, the landscape is usually split between two different philosophies. On one side, you have thellama.cppecosystem. This is the powerhouse of versatility. It’s the project that effectively democratized local LLMs, allowing us to run massive models on everything from MacBooks to old gaming PCs by utilizing GGUF and sophisticated memory offloading. If you need a model to run on a weird hardware configuration or want to lean on your system RAM,llama.cppis the tool for the job.

But for an endurance engine, versatility is secondary tothroughput.

That’s wherevLLMcomes in.

Whilellama.cppis built for the individual user's flexibility, vLLM is built for the scale of a serving engine. To understand why, you have to understand the "Double Penalty" of long context.

When you increase the context length of a model, you get hit twice. First, you have theCompute Cost: the model has to attend to every previous token, so the work increases as the sequence grows. Second, you have theMemory Cost: you have to store theKV Cache, the pre-computed Keys and Values for every past token, so the model does not have to recompute that history from scratch on every new step.

In a standard setup, this KV cache is stored in one contiguous block of VRAM. But in the real world, sequences have different lengths. This leads to massive memory fragmentation: you have "holes" in your VRAM that are too small to be used but too large to ignore. As your context grows, this waste grows with it. Eventually, your batch size collapses, and your GPU sits underutilized while your agent crawls.

PagedAttentionis vLLM's solution, and it's basically "Virtual Memory" for LLMs.

Instead of storing the KV cache as one giant chunk, PagedAttention splits it into fixed-size blocks, or "pages." It uses a page table to map logical tokens to physical memory blocks. This means the model can store the cache anywhere in VRAM, eliminating fragmentation and allowing it to pack requests tightly.

For a research agent that is reading fifty pages of documentation, this is the difference between the agent finishing the job and the system crashing with anOut of Memoryerror. It also enablesprefix caching: if your agent asks ten different questions about the same documentation, vLLM doesn't recompute the documentation ten times. It shares the same KV pages across all requests.

The best part is that we no longer have to wait for the community to "hack" MTP support into the codebase. vLLM launchedDay-0 supportfor Gemma 4 MTP.

They provided a ready-to-use Docker image, which effectively removes the "dependency hell" that usually comes with cutting-edge AI releases. You don't have to spend your afternoon wrestling with CUDA versions or Triton kernels. You pull the image, spin up the server, and you have a high-performance MTP engine running on consumer hardware.

Because vLLM provides anOpenAI-compatible API, the integration is seamless. The server sits there as a lightweight endpoint, and any tool, whether it's a custom Python script or an agentic orchestrator likepi, can talk to it using standard API calls.

You’ve effectively decoupled the "Brain" (the model) from the "Pilot" (the agent). The Brain lives in vLLM, optimized for raw speed and memory efficiency. The Pilot lives in your orchestration layer, focusing on the logic and the goal.

### Setting Up vLLM

Time to actually run the thing. This is where most local-model articles get bogged down in CUDA versions, Triton kernels, and Python env nightmares.Fine-tuning a model on Bronze Age tablets, I can handle. CUDA toolchain mismatches at 1 AM, I cannot.

Luckily, the vLLM team shipped a pre-release Docker image specifically for Gemma 4. If you’re on Hopper, you grabvllm/vllm-openai:gemma4-0505-cu129. On Blackwell, it’svllm/vllm-openai:gemma4-0505-cu130. One small but important gotcha: the standardvllm/vllm-openai:latesttag doesnotinclude MTP speculative decoding for Gemma 4 yet. If you pull the default image out of habit, the--speculative-configflag will silently get you nowhere.

docker pull vllm/vllm-openai:gemma4-0505-cu130

Enter fullscreen mode

Exit fullscreen mode

That’s dependency hell, gone in one command.

The next problem is fitting a 31B-parameter model on a single card. In native BF16, Gemma 4 31B eats a serious chunk of VRAM just to load the weights, before a single byte goes to the KV cache. That’s server-class hardware territory, not a workstation, and certainly not a single consumer card like the RTX 5090 with its 32GB of VRAM.

The trick isNVFP4, NVIDIA’s 4-bit floating-point format, native to Blackwell. NVIDIA published a quantized checkpoint,nvidia/gemma-4-31B-it-NVFP4, that drops the weights to roughly19GB. Stack an FP8 KV cache on top of that, and a 31B reasoning model fits comfortably on a consumer Blackwell card like the RTX 5090, with headroom left over for serving.

Here’s the actual launch command:

docker run 
--gpus
 all 
\

 
--privileged
 
--ipc
=
host 
-p
 8000:8000 
\

 
-v
 ~/.cache/huggingface:/root/.cache/huggingface 
\

 vllm/vllm-openai:gemma4-0505-cu130 nvidia/gemma-4-31B-it-NVFP4 
\

 
--kv-cache-dtype
 fp8 
\

 
--tensor-parallel-size
 1 
\

 
--enable-auto-tool-choice
 
\

 
--tool-call-parser
 gemma4 
\

 
--chat-template
 examples/tool_chat_template_gemma4.jinja 
\

 
--reasoning-parser
 gemma4 
\

 
--speculative-config
 
'{"model":"google/gemma-4-31B-it-assistant","num_speculative_tokens":4}'

Enter fullscreen mode

Exit fullscreen mode

A few lines worth calling out:

* --kv-cache-dtype fp8cuts the KV cache footprint roughly in half. Long contexts are still expensive, just half as expensive.
* The--tool-call-parser,--reasoning-parser, and--chat-templatetrio wires up Gemma 4’s native function calling and structuredthinking mode. We don’t need tools for the benchmark itself, but any agent that drives this engine afterwards will.
* The interesting line is the last one.--speculative-configis the switch that turns MTP on. Thetargetis the NVFP4 31B model doing the actual reasoning. Thedrafterisgoogle/gemma-4-31B-it-assistant, a0.5B-parametercompanion model that Google ships specifically as the speculative-decoding partner for the 31B. At roughly 60x smaller than the target, it generates draft tokens fast enough that the verification step costs almost nothing extra. It also shares the target model’s KV cache and feeds off its final-layer activations rather than building its own context from scratch, which is why the acceptance rate stays stable even as context grows.num_speculative_tokens: 4is the recommended starting point at this scale; vLLM’s own benchmarks suggest pushing up to 8 if your acceptance rate holds.

Once the container boots, vLLM exposes an OpenAI-compatible endpoint onlocalhost:8000. Anything that already speaks the OpenAI API talks to this. No new SDK, no custom wire protocol, no learning curve.

That’s the whole engine. Brain loaded, drafter wired up, KV cache paged. Now the only question worth answering is whether MTP actually earns its keep, or whether it’s another "up to 3x faster" line that quietly evaporates on real workloads.

That’s what the next section is for.

### Does MTP Actually Earn Its Keep?

I ran this on a dedicated Nvidia RTX PRO 6000 Blackwell 96GB instance rather than my local machine, and used the unquantized BF16 checkpoint. The PRO 6000 is a workstation card, not a consumer one — I picked it deliberately. Local inference benchmarking is noisy (background processes, thermal throttling, memory contention), and BF16 weights in a clean isolated environment let me measure the MTP mechanism itself without quantization or thermal effects muddying the numbers.

The trade-off worth naming: these numbers are not directly what a 5090 running NVFP4 will hit. The two setups pull in different directions — the PRO 6000 has more raw compute and memory bandwidth, but NVFP4 on Blackwell has native FP4 tensor cores and a much smaller memory footprint, which matters a lot for the bandwidth-bound decode step. Which curve ends up higher in absolute tok/s is an empirical question I haven't answered here. What does transfer is the shape: where MTP wins, where the gain narrows, and where it crosses over. If you want exact numbers for your card, run llama-benchy yourself with the config from the previous section.

The first test used vLLM’s own built-in benchmark tool,vllm bench serve. The setup was a controlled A/B: everything identical except the presence of--speculative-config. Three runs per arm, results averaged.

vllm bench serve 
\

 
--model
 google/gemma-4-31B-it 
\

 
--host
 localhost 
--port
 8000 
\

 
--dataset-name
 random 
\

 
--random-input-len
 1024 
--random-output-len
 1024 
\

 
--num-prompts
 100 
--max-concurrency
 32

Enter fullscreen mode

Exit fullscreen mode

Spec OFF:356 tok/s. Spec ON:642 tok/s. A consistent1.80xacross all three runs.

Butvllm bench serveanswers a different question than the one I was actually asking. It is built to stress-test a serving deployment: it saturates the server at concurrency 32, mixes request queues, and measures aggregate output across all users at once. That is exactly what you want if you are sizing a production API. It is not what you want if you are asking how fast a single agent thinks on a long task.

There is also a structural problem with the random dataset beyond just MTP. It is the only format that lets you pin exact input and output lengths. Andvllm bench servehas no mechanism to measure how performance changes as context grows, which is exactly what matters for a marathon task.

The question I actually needed to answer was different: how does per-request generation speed change as context grows from zero to 120k? Real text, real acceptance rates, one request at a time.

For that, I usedllama-benchy.

The Context Ladder

llama-benchy is a llama-bench style tool built for any OpenAI-compatible endpoint. The key differences fromvllm bench serveare threefold: it runs one request at a time, which is the actual solo-agent scenario; it uses real book text from Project Gutenberg, which gives the speculative drafter something meaningful to predict; and it sweeps across context depths, so you can see exactly how performance changes as the KV cache fills.

llama-benchy 
\

 
--base-url
 http://localhost:8000/v1 
\

 
--latency-mode
 generation 
--skip-coherence
 
\

 
--pp
 2048 
--tg
 480 
\

 
--depth
 0 1000 5000 10000 20000 50000 100000 120000 
\

 
--book-url
 https://www.gutenberg.org/files/2600/2600-0.txt 
\

 
--no-cache

Enter fullscreen mode

Exit fullscreen mode

Here is the full comparison across the context window, one request at a time:

Context depth

Spec ON (tok/s)

Spec OFF (tok/s)

Advantage

0 (fresh start)

52.5

22.3

2.4x

5k

46.2

21.7

2.1x

10k

40.3

21.3

1.9x

20k

38.3

20.6

1.9x

50k

27.0

19.7

1.4x

100k

19.1

18.4

~1.0x

120k

16.6

18.0

0.9x

As an additional test, I increasednum_speculative_tokensfrom 4 to 8 to see if performance would scale. While the 8-token configuration did improve throughput, the results showed clear diminishing returns in this dataset. Across most context lengths, doubling the speculative tokens only yielded a modest bump of roughly 2 to 3.5 tok/s over the 4-token setup, with the most noticeable gains in the 10k to 50k range.

The engine does not get tired. But past a certain point, the turbocharger becomes a drag.

Two things stand out. First, spec OFF is surprisingly stable: only a 19% drop across the entire 120k window, from 22.3 to 18.0 tok/s. The model's autoregressive baseline is memory-bandwidth bound and barely sensitive to context length on its own. Second, spec ON drops 68% over the same range, from 52.5 to 16.6 tok/s. The drafter overhead compounds with the growing attention cost: the shared KV cache it attends over gets larger with every token processed, and that cost grows whether or not the drafter is predicting well.

The crossover lands at around 100k tokens. At 120k, spec OFF is actually faster.

It is also worth noting that acceptance rate is workload-dependent. The vLLM bench reported an acceptance length of 3.54 out of 4 on random dataset tokens. The ladder benchmark on War and Peace text showed a consistent ~2.7 out of 4 across all context depths. The inversion is counterintuitive — you might expect coherent prose to be more predictable than random tokens — but vLLM's random dataset feeds uniform random vocab IDs as input, which is a fairly degenerate condition for an LLM to operate in. Models under high uncertainty have a documented tendency to fall back toward repetitive or low-entropy outputs, and that kind of output is exactly what a small drafter handles well. The two benchmarks also differ in concurrency and decode settings, which complicates a direct comparison further. The takeaway isn't that one number is wrong, it's that 3.54/4 isn't the figure that will generalize to a real workload. The 2.7/4 on coherent prose is closer to what an agent on real text will see.

One more thing worth naming: MTP only touches the generation side. Prefill is compute-bound and speculative decoding does nothing for it. For a read-heavy agent continuously ingesting new documents, the time spent waiting for the model to process each new chunk of context is unaffected by whether spec decode is on or off. That is the next constraint, and prefix caching is what addresses it: if the agent revisits the same source material across multiple reasoning steps, the cached KV pages are free.

For a typical agentic task in the short to medium context range, this is not a concern. The 2x+ advantage holds through 20k tokens and is still meaningful at 50k. But for a task designed to fill the full context window, the honest recommendation is to pick the configuration based on your expected average depth: spec ON for workloads that mostly stay under 50k, spec OFF if your agent spends most of its time deep in a 100k+ session. vLLM doesn't let you flip--speculative-configper request, so this is a server-launch decision, not a runtime one.

These numbers are also conservative in a second way: they come from near-default vLLM settings. There is meaningful headroom on top of both curves. The most impactful levers:

* NVFP4 weights + FP8 KV cache: the production setup from the previous section. Cuts weight footprint from ~62GB to ~19GB and halves KV cache memory, freeing headroom for larger batches or longer contexts.
* --enable-chunked-prefill: overlaps prefill computation with ongoing decode steps. Helps TTFT under load without touching throughput.
* Prefix caching: if the agent re-reads the same documents across multiple reasoning steps, vLLM shares KV pages across those requests instead of recomputing them. For a research loop that revisits the same source material, this is a significant multiplier.
* FlashInfer attention backend(--attention-backend flashinfer): optimized for Blackwell, can improve throughput over the default backend at longer context lengths where the attention step dominates.

### The Pilot

The benchmarks answer the speed question. The actual workflow question is: what do you point at this thing?

For the agent layer, I have been usingPi. Minimal terminal harness, tiny system prompt, fully extensible. No context bloat, no baked-in opinions about how your workflow should look. For marathon tasks where every token in the context window has to earn its place, lean tooling matters.

Pointing it at the local engine is one config file. Add this to~/.pi/agent/models.json:

{

 
"providers"
:
 
{

 
"vllm-gemma4"
:
 
{

 
"baseUrl"
:
 
"http://localhost:8000/v1"
,

 
"api"
:
 
"openai-completions"
,

 
"apiKey"
:
 
"none"
,

 
"models"
:
 
[

 
{

 
"id"
:
 
"google/gemma-4-31B-it"
,

 
"contextWindow"
:
 
128000

 
}

 
]

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Switch to it with/model. Pi talks to your local vLLM instance the same way it would talk to any cloud endpoint. The Brain and the Pilot stay fully decoupled: one handles raw inference speed, the other handles the logic and the goal.

Which left only one thing to find out: whether the whole stack actually holds up overnight.

### The Marathon

Couple days later. Same shape of task, slightly different flavor: point the agent at a pile of raw sources, papers, scattered docs, half-finished notes, and have it build a Karpathy-style LLM wiki out of them. Structured markdown files and entity pages, the whole thing knitting itself together as it went. The kind of job that rewards grinding: read, summarize, link, double back, refine. I pointed Pi at the local vLLM endpoint, set it running just before midnight, and went to sleep.

This time I woke up to a populatedwiki/directory. Forty-something markdown files, a few hundred wikilinks, and aconflicts.mdwhere the agent had flagged two sources disagreeing instead of silently picking a winner. No frozen terminal. No 12:10 AM service outage. The engine had just kept going through the night, on my desk, at whatever speed MTP and a 31B model could manage on consumer silicon.

That's what the marathon engine is actually for. Not to beat the cloud giants on a single hard reasoning step; it won't, and I don't ask it to. To be the thing that's still there at 3 AM, still working, when the clever model is down or rate-limited or metering every token. The "babysitting" problem I used to have with local models wasn't really about intelligence. It was about endurance, and a serving stack that didn't fall over. Both of those, finally, are being solved.

### Verdict

A year ago, "local model" and "marathon agent" did not belong in the same sentence. The hardware was wrong, the serving stack was wrong, and the speed was definitely wrong. The frontier was something you rented by the token, and that was the deal.

That deal is now negotiable.

The deal changed because the models got good enough and the serving stack finally got to acceptable levels; and MTP is a good bonus on top of that. The benchmarks back up the headline at the depths where most agentic work actually lives. From a fresh start through 50k tokens, speculative decoding delivers a consistent 1.4x to 2.4x speedup over the autoregressive baseline. That is shy of the "up to 3x" top-line number, but it is a measured, reproducible win on real prose, with a verification step that mathematically guarantees the same output distribution as the target model alone. The drafter does what it claims, the acceptance algorithm holds, and the engine stays honest.

A few caveats worth naming before the takeaways:

* The advantage is not flat across the context window.MTP shines early; gains narrow as the KV cache grows and the drafter overhead compounds with attention cost. Measure for your own workload before assuming the headline number applies everywhere.
* Spec decode only touches generation.Prefill is a separate problem. For read-heavy agents that re-ingest the same documents, prefix caching matters more than MTP.
* Acceptance rate is workload-dependent.Random benchmark tokens behaved differently from coherent prose in my tests. One number will not tell you what your stack actually does.

The takeaways:

* Use the giants for sprints.When precision on a single hard reasoning step is what you need, the trillion-parameter models still win. That is not changing for a while (Hope I am wrong).
* Use a local marathon engine for routine tasks.Anything that grinds: multi-hour scraping, knowledge-base construction, batch summarization, agent loops with dozens of self-correction steps. The economics flip the moment your task crosses the API quota line.
* vLLM + Gemma 4 + MTP is the current sweet spot.Not because it beats everything else on IQ, but because it is the first stack where consumer hardware, modern serving infrastructure, and decent generation speed all line up at the same time.
* Decouple Brain and Pilot.Keep inference (vLLM) separate from orchestration (Pi, or whatever you reach for). The Brain optimizes tokens per second. The Pilot optimizes getting the job done. Treating them as one thing is the bug behind half the local-agent frustrations I have seen.

The failed auto job that opened this post was not a failure of intelligence. It was a failure of foundation. Now there is a real alternative that fits on consumer hardware and runs without a token quota.

It is not the smartest model in the world. It is the one that works tirelessly and locally.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse