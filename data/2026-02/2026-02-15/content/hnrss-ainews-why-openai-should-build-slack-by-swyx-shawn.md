---
title: '[AINews] Why OpenAI Should Build Slack - by swyx (Shawn)'
url: https://www.latent.space/p/ainews-why-openai-should-build-slack
site_name: hnrss
content_file: hnrss-ainews-why-openai-should-build-slack-by-swyx-shawn
fetched_at: '2026-02-15T11:08:52.252832'
original_url: https://www.latent.space/p/ainews-why-openai-should-build-slack
author: swyx (Shawn)
date: '2026-02-14'
description: 'a quiet day lets us answer a Sam Altman question: what should he build next?'
tags:
- hackernews
- hnrss
---

AINews: Weekday Roundups

# [AINews] Why OpenAI Should Build Slack

### a quiet day lets us answer a Sam Altman question: what should he build next?

swyx (Shawn)
Feb 14, 2026
∙ Paid
31
2
2
Share

We’re still not overthe Sam Altman town hall; at the town hall he said “tell us what we should build, we’ll probably build it!” and today at Stanford Treehackshe saidanother thing about how he chooses projects: he thinks of himself as having made a career out of doing things people think are hard, but would be a big deal if it came true.

well okay, Sam: You Should Build Slack.It fits your criteria: it is hard for anyone else without the clout of OpenAI to pull off, it will be very well received by the tech community, and it is an obvious progression of ChatGPT for both yourEnterpriseandyour Coding push and build permanent entrenchment in your customers.

Slackrejected developer communityand went upmarket in 2019, thenSalesforce bought it for $27.7B in 2021, and ever since then Slack has been on a slow rachet up in prices and has struggled to introduce compelling new AI features (Slack AIis occasionally useful but impossible to discover/learn/personalize) while facingconstant outages. NPS feels low, and yet every organization in tech uses it.

Everything could be better. Developers routinely complain about Slack’s API costs and permissions (even 3rd or 4th Uber investor and famed vibe coder Jason Calacaniscomplained on the latest All In podcast). Founders routinely complain about the pricing. Slack users complain about channel fatigue and find the Recap tooling and notifications spam woefully inadequate. Huddles could offer far better realtime multimodal AI features.

Slack Connect is great though, definitely just clone that.

Sure,ChatGPT launched group chats3 months ago and probably the usage isn’t great outside of OpenAI. It’d be a mistake to think that repeatedhalf hearted attempts in consumer social AImeans that you can’t build a successful business social network if you took it as seriously as you do everything else. Microsoft did, and Teams is by all reports a solid success (aftera rocky start).

In the desktop wars, Anthropic has pursued a far more cohesive strategy than OpenAI: one app for Chat, Cowork, and Claude Code, with optional control of the browser via Claude in Chrome.

By contrast, OpenAI hasshipped the org chartto every user’s desktop: get ourchat app here, get ourbrowser apphere, get ourcoding appthere. Log in fresh every single time. Even doing a unification at some point probably still leaves you behind; you need to lead, not be a slow follower of what Anthropic already did.

“OpenAI Slack” is your chance to retake the initiative. Of course you’re going to be good at chat AI. Of courseyou care about the multiagentUX of the future. Why not build your own version of the existing multiagent UX we all know to work between humans? Heck, forgot you even hiredSlack CEO Denise Dresser in Dec. Great!

Oh another thing: I bet OpenAI employees would have 10,000 ideas to improve Slack if you owned your own Slack. After all,you guys use this thing more than email. The feedback dogfood loop on this one will be the craziest thing since Claude Code.

The killer part of course is that this couldalsobe the coding agent interface you always wanted anyway. The main remaining thing missing from the admittedly very good Codex app is the ability to be truly multiplayer. You haven’t felt the AGI until you havegiven your designer access to your coding agentand let him rip all night with you occasionally chiming in to guide things. You can see swarms of humans and swarms of agents all working together inGod’s given orchestration interface: chat.

Put another way, it is now time to layer a customer organization’s social graph and work graph onto ChatGPT, and then lather every interface with agents and AI in the way that OpenAI does best. The network effect makes it 10000x harder to leave you for a competitor, and sure, you could do it atop Slack as you currently do, but it’s easy to switch and won’t give you access to freelyreinvent the future of work.

To recap:

* Is it hard to do?yes for almost everyone except you
* Is it a big deal if you get it right?yes for us users, but an even bigger deal for your business
* Will you have lots of low hanging fruit to build new agentic interfaces and acontext graph/system of record to powerFrontierand everything else you do in SMB and Enterprise?yeah.

/fin

Feb 14 update:This header is usually at the start of the post, but since it is causing some confusion on HN andTwitter, I am moving it down. The editorial written above is always human written, the recaps below are human reviewed.

# AI News — Feb 13, 2026

AI News for 2/12/2026-2/13/2026. We checked 12 subreddits,544 Twittersand 24 Discords (256channels, and7993messages) for you. Estimated reading time saved (at 200wpm):675minutes.AINews’ websitelets you search all past issues. As a reminder,AINews is now a section of Latent Space. You canopt in/outof email frequencies!

It’s a pretty quiet day — thenew Dwarkesh-Dario podis worthwhile but hasn’t generated much new conversation on day 1, andOpenAI claimed a big resultin theoretical physics that is mostly getting questioned by some physicists. This means we get to go back to our backlog of mini-editorial ideas for AINews subscribers!

# AI Twitter Recap

MiniMax M2.5 open-sourcing: agent-native RL, speed/cost, and rapid ecosystem uptake

* MiniMax-M2.5 is now open source: MiniMax releasedMiniMax-M2.5weights + code, positioning it as an “agent-native” model trained withRL across hundreds of thousands of real-world environmentsfor coding, tool use, search, and office workflows (MiniMax announcement). vLLM highlights day‑0 support and reports key benchmark numbers:80.2% SWE‑Bench Verified,76.3% BrowseComp, plus claims around training scale (200k+ RL environments) and speed/cost characteristics (vLLM). SGLang similarly ships day‑0 support and frames the model as production-grade for “always-on” agents (lmsys).
* The practical headline is economics + throughput, not just score: MiniMax repeatedly markets“$1 per hour at 100 tps”(interpretable as a “long-horizon agent budget”), which shows up both in their own posts (MiniMax) and in community recaps emphasizing that low activated-parameter count makes self-hosting plausible (omarsar0). Early local runs suggest unusually strong on-device viability for its class: MLX users report ~50 tok/sshortly after release (pcuenq), and a singleM3 Ultra 512GBrun at6‑bitreports ~40 tok/swith ~186GBpeak memory (ivanfioravanti).
* Forge RL training system details leak into the narrative: A Zhihu-derived writeup summarizes MiniMax’s “Forge” RL stack as stillCISPO-like, usingprocess reward + completion-time reward, with infrastructure tricks likemulti-level prefix cacheand high rollout compute share (claimed~60%of compute) generatingmillions of trajectories/day(YouJiacheng). MiniMax leadership explicitly answers parameterization tradeoffs (“10B activeintentional”), claims proximity to “infinite agent scaling” withknowledge capacityas the limiter, and teases structural + pretraining innovation focus forM3(MiniMax reply).
* Independent reviews: “viable for multi-turn work” but token-hungry: A Chinese review thread claims M2.5 corrects M2.1’s imbalance (coding up, logic down), with overall improvements and better stability; it noteshigh token usage(nearly2× Sonnetin one comparison) but frames pricing/compute as making it usable day-to-day (ZhihuFrontier). Another summary calls it “≤Sonnet for coding, but close,” and emphasizes multi-turn viability as the key break from “toy” open models (teortaxesTex).
* Ecosystem uptake is immediate: weights mirrored and packaged across tooling (Hugging Face release pings, GGUF/quant drops, etc.), including Intel-hosted quantized artifacts like a2‑bit GGUFfor MiniMax‑M2 andINT4for Qwen3‑Coder‑Next (HaihaoShen).

GLM‑5 and the “near-frontier” open model wave: performance, infra constraints, and eval chatter

* GLM‑5 positioning: Together markets GLM‑5 as best-in-class open-source for long-horizon agents and systems engineering, quoting metrics like77.8% SWE‑Bench Verified,50.4% HLE w/ tools, and a MoE efficiency story with “DeepSeek Sparse Attention” (as described in the tweet) (Together). W&B promotes an interview claiming744B params, a “new RL framework,” and “fully open source under MIT” (as stated in the post) (W&B). Community members also notice dataset fingerprints like “truthy‑dpo” appearing in GLM‑5 outputs (jon_durbin).
* GLM‑5 qualitative review highlights: A detailed Zhihu-based comparison frames GLM‑5 as a substantial improvement over GLM‑4.7, especially on hallucination control, programming fundamentals, and character processing—but also more verbose/token-expensive and prone to “overthinking,” suggesting a trade between long-horizon reasoning and compute burn (ZhihuFrontier on GLM‑5).
* Benchmarks as a moving target: There’s persistent meta-discussion about whether leaderboards/evals are saturated or misleading. Examples: concerns that tokens/latency tradeoffs hide true capability; skepticism about inferring model size from TPS; and the observation that past “SWE‑bench saturation” claims were premature (jyangballin,teortaxesTex).
* Cross-checking with alternative evals: SWE‑rebench is cited as “brutal” for some recent releases and shows different relative rankings than SWE‑bench Verified; a caution is made to treat it as “additional signal” (maximelabonne).

Agent engineering in practice: file-based coordination, terminal-first workflows, and “agent OS” framing

* Claude Code “Agent Teams” internals are surprisingly simple: A reverse-engineering summary claims Claude Code’s multi-agent comms useJSON files on disk(inboxes under~/.claude/teams/inboxes/{agent}.json), with polling between turns and JSON-in-JSON protocol messages; the argument is that this is a pragmatic CLI design (no Redis/queues) and improves observability at the cost of atomicity/backpressure (peter6759).
* Terminal agents are becoming the default UX: Cline launchesCline CLI 2.0, an open-source terminal coding agent featuring a redesigned interactive TUI, parallel agents with isolated state, headless CI/CD mode, and broad editor support (ACP for Zed/Neovim/Emacs) (cline,cline details). Community framing: “open-source strikes back” due to free/low-barrier access to strong models (testingcatalog,dr_cintas). One Cline team member describes a full rewrite (Go → TypeScript) driven by architecture/UX pain and the need to run evals reliably (arafatkatze).
* Agent scaffolds may matter less than expected (for some horizons): METR-related discussion suggests Claude Code / Codex scaffolds don’t strongly outperform METR’s “simple OS scaffolds” on measured time horizons so far (nikolaj2030), with Ajeya Cotra noting surprise at the small delta (ajeya_cotra). In contrast, others note that for longer, harder tasks, scaffold choice can matter materially (e.g.,~10% successswings) (gneubig).
* “Agents as OS / filesystem as substrate”: Several posts converge on the idea that file systems are the natural environment for agents (observability, unstructured data manipulation). Box announces integration as a “cloud filesystem” into LangChain deepagents (levie). WebMCP pushes “browser is the API” for web automation without UI perception, with a DoorDash-like starter template (skirano).
* Key operational lesson: make codebases “agent-ready”: A crisp observation is that agents have “zero tolerance” for entropy humans route around; they treat dead code/outdated docs literally, forcing engineering hygiene that humans always needed but often deferred (dok2001).

RL/post-training research themes: process rewards, exploration, and rubric-based evaluation

* Length-Incentivized Exploration (LIE) for reasoning: A research summary introduces the “Shallow Exploration Trap” (long reasoning trajectories become exponentially unlikely under AR sampling), and proposes LIE: a length reward + redundancy penalty to encourage broader in-context exploration without filler. Reported gains includeAIME25 20.5%→26.7%in one setup and small but consistent improvements across other benchmarks/models (dair_ai).
* DPPO vs PPO and “trust region” framing: A long algorithm breakdown contrasts PPO’s token-ratio clipping with DPPO’s distribution-shift control via divergence measures (TV/KL), plus approximations (binary/top‑K) to reduce compute, arguing DPPO is more proportional on rare tokens and better constrains large probability-mass moves (TheTuringPost).
* Rubrics-as-rewards and evolving rubrics: A thread describesRLER(RL with evolving rubrics) in Dr. Tulu: seed rubrics with search-grounded criteria, maintain an evolving rubric buffer per prompt, and keep the most discriminative rubrics by reward variance to combat reward hacking and adapt evaluation on-policy (cwolferesearch). Separately, a take argues “rubrics as rewards” can beat verifiers-as-reward even in formal-verification settings, recommending verifiers in the loop/harness but not as the sole reward signal (davidad).
* ∆Belief‑RL / information-seeking agents: A new approach rewards actions by how much they increase belief in a target (logprob-based), aiming for long-horizon information seeking without a critic/reward model; claims include generalization from “20 questions” training to new tasks and continued improvement when scaling interaction time (ShashwatGoel7).
* Human simulation as an RL target: Stanford’sHumanLM+Humanualbenchmark propose training LLMs to simulate user responses accurately (human-centric evaluation, preference shaping, policy justification), positioning user simulation as a capability primitive for product/agent design (ShirleyYXWu).

Systems/infra and tooling: FP4 MoE kernels, faster ZeRO loads, model “skills,” and observability

* vLLM on GB300 + FP4 MoE acceleration: vLLM reports DeepSeek R1 onGB300with22.5K prefill TGSand3K decode TGS per GPU, claiming large improvements over Hopper, and highlights a recipe includingNVFP4 weightsandFlashInfer FP4 MoE kernel(VLLM_USE_FLASHINFER_MOE_FP4=1) plus disaggregated prefill and tuning notes (vllm_project).
* DeepSpeed ZeRO load-time fix: A rework moves tensor flattening from CPU to GPU, significantly improving multi-GPU load times for huge models under ZeRO 1+2 (StasBekman).
* Gemini “Skills” and multimodal tool calling: Google’s Gemini API work includes a “skills” repo teaser (osanseviero) and an Interactions API update enablingmultimodal function callingwhere tools can returnimagesand Gemini can process returned images natively (philschmid). AI Studio billing/upgrade UX is streamlined (upgrade to paid without leaving Studio, usage tracking, spend filters) (OfficialLoganK,GoogleAIStudio).
* Agent harness instrumentation: ArtificialAnalysis adds end-to-end speed tracking to their agent harnessStirrup, plus per-model breakdowns and tool-call latency metrics—explicitly treating wall-clock completion time as a first-class agent metric (ArtificialAnlys).
* Local fine-tuning & Apple Silicon workflows: Notable tooling for MLX: real-time transcription with Voxtral Mini 4B in MLX Swift (awnihannun), a no-code local fine-tuning tool exporting to Ollama (awnihannun), and a repo of MLX-LM LoRA examples including GRPO/ORPO/DPO variants (ActuallyIsaak).

“AI accelerates science” moment: GPT‑5.2 + QFT result and the scaffolding narrative

* OpenAI claims a novel theoretical physics result with GPT‑5.2: OpenAI announces a preprint showing a gluon interaction previously assumed not to occur can arise under a specific “half-collinear” regime, framed as AI-assisted discovery (OpenAI; preprint link is shared in-thread:arXiv pointer). Kevin Weil adds color: GPT‑5.2 Pro suggested a general formula; an internal scaffolded model thenproved it after ~12 hoursof continuous work (kevinweil). Discussion emphasizes that pattern-finding + sustained scaffolded reasoning is the differentiator, not just a single chat completion.
* Community reactions range from “significant journal-paper tier” to skepticism about interpretation: Some report physicists calling it a meaningful contribution roughly equivalent to a solid journal paper (polynoamial); others focus on the implications of long-duration productive reasoning and how to measure it in tokens/time (teortaxesTex). There’s also meta-discussion about how many employees (or outsiders) can actually evaluate the proof/result, underscoring the evaluation gap for domain-elite work (scaling01).

### Top tweets (by engagement)

* GitHub adds ability to disable PRs(joshmanders,jaredpalmer).
* OpenAI’s GPT‑5.2 physics announcement(OpenAI).
* MiniMax M2.5 open-source release(MiniMax).
* Cline CLI 2.0 launch / open-source terminal agent(cline,testingcatalog).
* “I am the bottleneck now” (agent-era productivity reflection)(thorstenball).
* Humanoid robotics hands progress (Figure)(adcock_brett).

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1. MiniMax-M2.5 Model Announcements and Details

* MiniMaxAI/MiniMax-M2.5 · Hugging Face(Activity: 531):MiniMaxAI has released the MiniMax-M2.5 model onHugging Face, which is noted for its advanced performance in coding, tool use, and office tasks. The model maintains a size of220 billionparameters, contrary to expectations of an increase to800 billionlike the GLM5 model. It offers a cost-effective operation at$1 per hourfor100 tokens per second, and is enhanced by the Forge reinforcement learning framework, which improves training efficiency and task generalization.Commenters express surprise at the model’s size remaining at220 billionparameters, highlighting its impressive performance despite not increasing in size. There is also anticipation for the release of aGGUFquantization format, which is not yet available.A user expressed surprise at the model’s size, noting that while they expected an increase to 800 billion parameters to compete with models like GLM5, the MiniMax-M2.5 remains at 220 billion parameters. This is considered impressive given its ‘frontier strength’, suggesting high performance despite the parameter count.Another user mentioned the model’s Q4_K_XL size, which is approximately 130GB. This size is significant as it places the model just beyond the capabilities of some hardware, indicating a need for more robust systems to fully utilize the model’s potential.There is anticipation for the release of FP4/AWQ, indicating that users are looking forward to further advancements or optimizations in the model’s performance or efficiency. This suggests a community eager for improvements that could enhance usability or reduce resource requirements.
* A user expressed surprise at the model’s size, noting that while they expected an increase to 800 billion parameters to compete with models like GLM5, the MiniMax-M2.5 remains at 220 billion parameters. This is considered impressive given its ‘frontier strength’, suggesting high performance despite the parameter count.
* Another user mentioned the model’s Q4_K_XL size, which is approximately 130GB. This size is significant as it places the model just beyond the capabilities of some hardware, indicating a need for more robust systems to fully utilize the model’s potential.
* There is anticipation for the release of FP4/AWQ, indicating that users are looking forward to further advancements or optimizations in the model’s performance or efficiency. This suggests a community eager for improvements that could enhance usability or reduce resource requirements.
* MiniMaxAI MiniMax-M2.5 has 230b parameters and 10b active parameters(Activity: 523):OpenHands has announced the release of the MiniMaxAI MiniMax-M2.5 model, which features230 billionparameters with10 billionactive parameters. This model is noted for its performance, ranking 4th in the OpenHands Index, and is13xmore cost-effective than Claude Opus. It excels in long-running tasks and issue resolution but requires improvements in generalization and task execution accuracy. The model is available for free on the OpenHands Cloud for a limited time.SourceCommenters are optimistic about the potential of a~160BREAP/REAM hybrid version, which could be optimized for machines with128GBof RAM, suggesting a focus on quantization and performance efficiency.The MiniMax-M2.5 model by Moonshot is notable for its architecture, which utilizes 230 billion parameters but only activates 10 billion at a time. This design choice is likely aimed at optimizing computational efficiency, allowing the model to perform well on less powerful hardware, such as GPUs that are not top-of-the-line. This approach could potentially offer a balance between performance and resource usage, making it accessible for more users.A comparison is drawn between MiniMax-M2.5 and other large models like GLM and Kimi. GLM has had to double its parameters to maintain performance, while Kimi has reached 1 trillion parameters. The implication is that MiniMax-M2.5 achieves competitive performance with fewer active parameters, which could be a significant advancement in model efficiency and scalability.The potential for further optimization through quantization is highlighted, suggesting that MiniMax-M2.5 could be made even more efficient. Quantization could reduce the model’s size and increase its speed, making it feasible to run on machines with 128GB of RAM while still leaving room for additional tasks such as deep-context tool use. This could make the model particularly attractive for users with limited computational resources.
* The MiniMax-M2.5 model by Moonshot is notable for its architecture, which utilizes 230 billion parameters but only activates 10 billion at a time. This design choice is likely aimed at optimizing computational efficiency, allowing the model to perform well on less powerful hardware, such as GPUs that are not top-of-the-line. This approach could potentially offer a balance between performance and resource usage, making it accessible for more users.
* A comparison is drawn between MiniMax-M2.5 and other large models like GLM and Kimi. GLM has had to double its parameters to maintain performance, while Kimi has reached 1 trillion parameters. The implication is that MiniMax-M2.5 achieves competitive performance with fewer active parameters, which could be a significant advancement in model efficiency and scalability.
* The potential for further optimization through quantization is highlighted, suggesting that MiniMax-M2.5 could be made even more efficient. Quantization could reduce the model’s size and increase its speed, making it feasible to run on machines with 128GB of RAM while still leaving room for additional tasks such as deep-context tool use. This could make the model particularly attractive for users with limited computational resources.
* Minimax M2.5 Officially Out(Activity: 765):Minimax M2.5 has been officially released, showcasing impressive benchmark results:SWE-Bench Verifiedat80.2%,Multi-SWE-Benchat51.3%, andBrowseCompat76.3%. The model is noted for its cost efficiency, with operational costs significantly lower than competitors like Opus, Gemini 3 Pro, and GPT-5. Specifically, running M2.5 at100 tokens per secondcosts$1 per hour, and at50 TPS, it costs$0.3 per hour, making it a cost-effective solution for continuous operation. More details can be found on theofficial Minimax page.Commenters highlight the potential game-changing nature of Minimax M2.5 due to its low operational costs compared to other models. There is also anticipation for the release of open weights on platforms like Hugging Face.The Minimax M2.5 model is highlighted for its cost-effectiveness, with operational costs significantly lower than competitors like Opus, Gemini 3 Pro, and GPT-5. Specifically, running M2.5 at 100 tokens per second costs $1 per hour, and at 50 tokens per second, it costs $0.3 per hour. This translates to an annual cost of $10,000 for four instances running continuously, making it a potentially disruptive option in terms of affordability.There is anticipation for the release of open weights on Hugging Face, which would allow for broader experimentation and integration into various applications. This suggests a community interest in transparency and accessibility for further development and benchmarking.The potential impact of Minimax M2.5 on existing models like GLM 5.0 and Kimi 2.5 is discussed, with some users suggesting that if the reported benchmarks are accurate, M2.5 could surpass these models in popularity due to its ease of use and cost advantages. This indicates a shift in preference towards models that offer better performance-to-cost ratios.
* The Minimax M2.5 model is highlighted for its cost-effectiveness, with operational costs significantly lower than competitors like Opus, Gemini 3 Pro, and GPT-5. Specifically, running M2.5 at 100 tokens per second costs $1 per hour, and at 50 tokens per second, it costs $0.3 per hour. This translates to an annual cost of $10,000 for four instances running continuously, making it a potentially disruptive option in terms of affordability.
* There is anticipation for the release of open weights on Hugging Face, which would allow for broader experimentation and integration into various applications. This suggests a community interest in transparency and accessibility for further development and benchmarking.
* The potential impact of Minimax M2.5 on existing models like GLM 5.0 and Kimi 2.5 is discussed, with some users suggesting that if the reported benchmarks are accurate, M2.5 could surpass these models in popularity due to its ease of use and cost advantages. This indicates a shift in preference towards models that offer better performance-to-cost ratios.

## Keep reading with a 7-day free trial

Subscribe toLatent.Spaceto keep reading this post and get 7 days of free access to the full post archives.

Start trial
Already a paid subscriber?
Sign in
Previous
A guest post by
swyx (Shawn)
