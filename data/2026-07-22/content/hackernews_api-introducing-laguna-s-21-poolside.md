---
title: Introducing Laguna S 2.1 — Poolside
url: https://poolside.ai/blog/introducing-laguna-s-2-1
site_name: hackernews_api
content_file: hackernews_api-introducing-laguna-s-21-poolside
fetched_at: '2026-07-22T11:37:30.867191'
original_url: https://poolside.ai/blog/introducing-laguna-s-2-1
author: rexledesma
date: '2026-07-21'
description: Today we’re releasing Laguna S 2.1, a significant step forward in our development of models that pursue longer horizon work and make effective use of reasoning.
tags:
- hackernews
- trending
---

* Punching above its weight class
* A closer look at DeepSWE
* Evaluation methodology
* Seeing the model work
* Thinking effort
* Limitations
* What actually changed in this model
* A strong base, then new post-training
* Distribution of post-training tasks
* What changed in the training loop
* The bets we're making
* Three models in three months
* Get started
 

Today we’re releasing Laguna S 2.1, a significant step forward in our development of models that pursue longer horizon work and make effective use of reasoning.

Laguna S 2.1 is a 118B total parameter Mixture-of-Experts (MoE) model with 8B activated parameters per token and supports a context window of up to 1M tokens in thinking and no-thinking modes. It went from the start of training to launch in under nine weeks, and on long-horizon coding benchmarks it holds its own against models many times its size. For every benchmark score we publish today, we are releasing full trajectories for every trial in the final evaluation set attrajectories.poolside.ai.

* Laguna S 2.1118B-A8B
* Tencent Hy3295B-A21B
* Inkling975B-A41B
* Nemotron 3 Ultra550B-A55B
* DeepSeek-V4-Pro-Max1.6T-A49B
* Kimi K32.8T-A50B
* Qwen 3.7 Max—
* Muse Spark 1.1—
* Claude Fable 5—
 

### Terminal-Bench 2.1

 
Terminal-Bench 2.1
 
Resolved tasks on Terminal-Bench 2.1.
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0
 
 
 
 
0
 
 
 
 
 
 

### SWE-Bench Multilingual

 
SWE-Bench Multilingual
 
Resolved tasks on SWE-Bench Multilingual.
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
 
 

### SWE-Bench Pro (Public Dataset)

 
SWE-Bench Pro (Public Dataset)
 
Resolved tasks on SWE-Bench Pro (Public Dataset).
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
 
 

### DeepSWE

 
DeepSWE
 
Resolved tasks on DeepSWE.
 
 
0.0
 
 
 
 
0
 
 
 
 
0
 
 
 
 
0.0
 
 
 
 
0
 
 
 
 
 
 

### SWE Atlas (Codebase QnA)

 
SWE Atlas (Codebase QnA)
 
Resolved tasks on SWE Atlas (Codebase QnA).
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
 
 

### Toolathlon Verified

 
Toolathlon Verified
 
Resolved tasks on Toolathlon Verified.
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
0.0
 
 
 
 
 
 
 
Benchmarks as of 21 July 2026. pass@1 averaged over 4 attempts per task, except DeepSWE, SWE Atlas (Codebase QnA) and Toolathlon Verified that had 3 attempts per task. For all benchmarks we take the maximum of the vendor self-reported score, benchmark author leaderboard or third-party leaderboard (Artificial Analysis), except SWE Atlas (Codebase QnA) where we do not use third-party leaderboard figures.

Laguna S 2.1 (118B-A8B)

Tencent Hy3 (295B-A21B)

Inkling (975B-A41B)

Nemotron 3 Ultra (550B-A55B)

DeepSeek-V4-Pro Max (1.6T-A49B)

Kimi K3 (2.8T-A50B)

Qwen 3.7 Max (—)

Muse Spark 1.1 (—)

Claude Fable 5 (—)

Terminal-Bench 2.1

70.2

71.7

63.8

56.4

64.0

88.3

74.5

80

88.0

SWE-Bench Multilingual

78.5

75.8

-

67.7

76.2

-

78.3

-

-

SWE-Bench Pro (Public Dataset)

59.4

57.9

54.3

-

55.4

-

60.6

61.5

80.3

DeepSWE

40.4

-

-

-

9.0

69.0

-

53.3

70.0

SWE Atlas (Codebase QnA)

46.2

-

-

-

27.2

-

-

42.2

-

Toolathlon Verified

49.7

-

45.5

34.3

55.9

-

-

75.6

-

## Punching above its weight class

Laguna S 2.1 is, as far as we can measure,the most capable agentic coding model in its weight class by a wide margin.

S 2.1 scores 70.2% on Terminal-Bench 2.1 in our agent harness with thinking enabled. Its compact size makes it uniquely suitable for complex work on local machines.

 
Benchmark
 
Terminal-Bench 2.1
SWE-Bench Multilingual
SWE-Bench Pro (Public Dataset)
DeepSWE
SWE Atlas (Codebase QnA)
Toolathlon Verified
 
* Open weights
* Closed / size undisclosed
 
1. 1GPT-5.6 Sol88.8
2. 2Kimi K32.8T-A50B88.3
3. 3Claude Fable 588.0
4. 4GPT-5.6 Terra87.4
5. 5GPT-5.6 Luna84.7
6. 6Claude Opus 4.884.6
7. 7Claude Sonnet 580.4
8. 8Muse Spark 1.180.0
9. 9Qwen-3.7 Max74.5
10. 10Hy3295B-A21B71.7
11. 11Laguna S 2.1118B-A8B70.2
12. 12MiniMax M3428B-A23B66.0
13. 13DeepSeek-V4-Pro-Max1600B-A49B64.0
14. 14Inkling975B-A41B63.8
15. 15DeepSeek-V4-Flash-Max284B-A13B61.8
16. 16Nemotron 3 Ultra550B-A55B56.4
17. 17Inkling-Small276B-A12B52.7
18. 18Qwen3.6-27B27B51.3
19. 19Qwen3.6-35B-A3B35B-A3B44.9
20. 20Nemotron 3 Super120B-A12B38.6
21. 21Laguna XS 2.133B-A3B33.4
22. 22Mistral Small 4119B21.4
 
Benchmarks as of 21 July 2026. pass@1 averaged over 4 attempts per task, except DeepSWE, SWE Atlas (Codebase QnA) and Toolathlon Verified that had 3 attempts per task. For all benchmarks we take the maximum of the vendor self-reported score, benchmark author leaderboard or third-party leaderboard (Artificial Analysis), except SWE Atlas (Codebase QnA) where we do not use third-party leaderboard figures.

Terminal-Bench 2.1 evaluates a wide, high-quality set of long-horizon tasks where an agent model is connected to its environment through a terminal. Laguna S 2.1 is a standout model in its size category on this benchmark.

 
Benchmark
 
Terminal-Bench 2.1
SWE-Bench Multilingual
SWE-Bench Pro (Public Dataset)
DeepSWE
SWE Atlas (Codebase QnA)
Toolathlon Verified
 
* Laguna S 2.1
* Other Laguna
* Other disclosed models
 
0
25
50
75
100
30B
100B
300B
1000B
3000B
Laguna S 2.1
Laguna S 2.1: 70.2 at 118B
Laguna XS 2.1
Laguna XS 2.1: 33.4 at 33B
Kimi K3
Kimi K3: 88.3 at 2800B
DeepSeek-V4-Pro-Max
DeepSeek-V4-Pro-Max: 64 at 1600B
Inkling
Inkling: 63.8 at 975B
Nemotron 3 Ultra
Nemotron 3 Ultra: 56.4 at 550B
MiniMax M3
MiniMax M3: 66 at 428B
Hy3
Hy3: 71.7 at 295B
DeepSeek-V4-Flash-Max
DeepSeek-V4-Flash-Max: 61.8 at 284B
Inkling-Small
Inkling-Small: 52.7 at 276B
Nemotron 3 Super
Nemotron 3 Super: 38.6 at 120B
Mistral Small 4
Mistral Small 4: 21.4 at 119B
Qwen3.6-35B-A3B
Qwen3.6-35B-A3B: 44.9 at 35B
Qwen3.6-27B
Qwen3.6-27B: 51.3 at 27B
Total parameters (B, log scale)
Score (Pass@1)
 
Total parameters, log scale. Models with undisclosed total parameter counts are omitted.

## A closer look at DeepSWE

The benchmarks above are all meaningful, and we're glad to be close to the frontier on them. But part of that closeness is a property of maturing benchmarks: as the frontier advances, top scores cluster in the 70-90% range and models that behave very differently end up no more than a few points apart. Datacurve’s DeepSWE still has significant headroom. Its tasks are longer-horizon and hard to partially solve, and the scores actually spread: frontier models range from 54% to 73% on the v1.1 variant, with some 1T+ parameter open models scoring below 10%.

On DeepSWE v1.1, Laguna S 2.1 scores40.4in thinking mode in pool harness.

 
 
* Open weights
* Closed / size undisclosed
 
1. 1GPT-5.6 Sol73.0
2. 2Claude Fable 570.0
3. 3GPT-5.6 Terra70.0
4. 4Kimi K32.8T-A50B69.0
5. 5GPT-5.6 Luna67.2
6. 6GPT-5.567.0
7. 7Claude Opus 4.859.0
8. 8Claude Sonnet 554.0
9. 9Grok 4.554.0
10. 10Muse Spark 1.153.3
11. 11GPT-5.452.0
12. 12GLM 5.2753B-A40B44.0
13. 13Laguna S 2.1118B-A8B40.4
14. 14Gemini 3.5 Flash37.0
15. 15Kimi K2.7 Code31.0
16. 16Claude Sonnet 4.630.0
17. 17Gemini 3.1 Pro12.0
18. 18DeepSeek-V4-Pro-Max1600B-A49B9.0
19. 19Laguna XS 2.133B-A3B0.3
 
pass@1 averaged over 3 attempts per task, harnesses vary (DeepSWE's leaderboard uses mini-swe-agent, model providers may report in their own harnesses and we report in pool, our agent harness). For all benchmarks we take the maximum of the vendor self-reported score, benchmark author leaderboard or third-party leaderboard (Artificial Analysis).

It is worth noting that Laguna S 2.1 scored 40.4% in our agent harness, pool, not mini-swe-agent which DeepSWE’s leaderboard uses. For other models we report maximal over reported scores which for most models are the official leaderboard results reported by Datacurve. While this makes scores less comparable, we don’t believe it puts us in a particularly advantageous position as it’s been reported that many of the models score the same or better in mini-swe-agent compared to their native harnesses. Every trajectory in the final evaluation run is availablehere.

## Evaluation methodology

Evaluation of agent models is notoriously difficult due to prevalence of reward hacking. We have previously written aboutreward hackingin leading benchmarks and our evaluations system and rigor as part of the technical report on our Laguna M.1 and XS.2 models. Recent work has focused on adversarial judging to increase reward hacking detection.

With this release, we are making all trajectories from our final evaluations of the published Laguna S 2.1 checkpoint available to view and download attrajectories.poolside.ai.

## Seeing the model work

Benchmark scores give a quantitative view into the model behavior, but to get a better intuitive understanding of how the model works it’s useful to look into runs on real world tasks. We share three such tasks with unedited trajectories and commentary.

Case study 1

 

#### A browser engine from a blank folder

 

One of our favorite things about Laguna S 2.1 is itsresourcefulness: It will find clever
	ways to get to the goal even if the direct path is not available. We saw a great demonstration of
	this when we asked it to build a browser engine from scratch; knowing it would be a challenge for
	Laguna to verify its work given its lack of vision capabilities. In one 50-minute session of 181
	steps, with no human intervention, Laguna S 2.1 built a working HTML/CSS rendering engine from an
	empty folder, then proved it renders like a real browser by measuring itself against one.
	Throughout its work, the model found increasingly complex ways to validate its work despite its
	limitations, leading to running headless Chromium to read canvases back and comparing screenshots
	numerically. See thefull trajectory here.

 
 
Read the full case study
 
// the verbatim prompt · reproduce it yourself
your job is it to build a simple browser engine (just html/css) in
javascript to demonstrate the capabilities of poolsides new "Laguna S"
model. the goal is to take render html snippets in a canvas like a real
browser. to demonstrate it the engine, build a self-contained single
page app that showcases a gallery of multiple html snippets and renders
them side by side (canvas with our render engine + iframe letting the
hosting browser render it for real for comparison). support for most
common layout and styling elements

 

Over the session the model built the full pipeline, parser → cascade → layout → renderer, in
		vanilla JavaScript: an HTML tokenizer and DOM tree, a CSS parser with selector specificity, a
		cascade engine with inheritance, box-model layout, and a canvas-2D renderer, wrapped in an app
		that shows nine snippets on its own canvas beside the same markup in an iframe, so the hosting
		browser sits right there as the reference.

 
 
The model's engine rendering on a canvas (left) beside the hosting browser's own rendering
				of the same markup (right). The header reports pixel dimensions and the measured difference
				between the two.

Case study 2

 

#### Optimizing our own harness

 

Laguna S 2.1 is capable of pursuing meaningful engineering and research work. In one example, one
	of our researchers pointed it at our agent harness, used for training/evaluation and user
	interaction with our models. In an automated loop, Laguna S 2.1 made our harness 5.2% faster with
	~70% lower memory allocation. See thefull trajectory here.

 
 
Read the full case study
 

For this task, we instrumented the harness with benchmarks so the model could see exactly where
		the time and memory went. We set strict rules: one approach at a time, benchmark after every
		change, keep only what measurably wins. We then ran Laguna S 2.1 in an automated research loop
		that fed each result back to it and pushed it to keep improving.

 

Results. Over multiple hours of work, Laguna S 2.1 found and implemented
		multiple different optimizations in our agent harness, resulting in an overall speedup of 5.2%,
		and reducing memory allocation by ~70%. The plot below shows the progression of the
		optimization, with the insights and discoveries the model made along its way.

 

Laguna S 2.1 found that streaming-token accumulation used O(n^2) string concatenation and
		replaced it with buffers. It also found several instances of redundant copying and
		over-allocation during trajectory materialization, which it resolved by memoizing
		materializations and pre-allocating slices to their exact sizes.

 

Notably, after speedup improvements became marginal and hard to measure in our setup, Laguna S
		2.1 kept driving forward, continuing to optimize. It found that memory allocation was more
		accurately measured and focused its effort there. This reinforces the notion that Laguna S 2.1
		truly is a model that doesn't give up and understands limitations of its environment and it is
		able to progress despite that.

 
 
 
* Wall-clock best-so-far (ranked objective)
* Allocations best-so-far (proxy)
* Attempt (did not improve best)
 
Best solution (attempt 9): 5.19% less harness time and −71.1% allocations
-8
-6
-4
-2
0
-80
-60
-40
-20
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
Wall-clock records: -0.368 at 1
strings.Builder
in stream proc.
Wall-clock records: -1.199 at 2
ActiveSegments
sub-slices
Wall-clock records: -1.385 at 3
Two-pass prealloc
for step groups
Wall-clock records: -1.599 at 4
Contiguous
sub-slice grouping
Wall-clock records: -2.429 at 5
Cap prealloc
Wall-clock records: -5.106 at 6
Memoize Entries()
per step
Wall-clock records: -5.19 at 9
Wall-clock non-record attempts: -2.289 at 7
Wall-clock non-record attempts: -4.231 at 8
Wall-clock non-record attempts: -3.107 at 10
Wall-clock non-record attempts: -2.467 at 11
Wall-clock non-record attempts: -2.366 at 12
Wall-clock non-record attempts: -4.458 at 13
Wall-clock non-record attempts: -4.41 at 14
Wall-clock non-record attempts: -4.749 at 15
Wall-clock non-record attempts: -2.105 at 16
Wall-clock non-record attempts: -4.478 at 17
Wall-clock non-record attempts: -3.445 at 18
Wall-clock non-record attempts: -2.277 at 19
Wall-clock non-record attempts: -4.123 at 20
Allocation records: 1.213 at 1
Allocation records: -47.299 at 2
Allocation records: -57.291 at 3
Allocation records: -62.577 at 4
Allocation records: -68.976 at 5
Allocation records: -69.455 at 6
Allocation records: -70.026 at 7
Allocation records: -70.953 at 8
Allocation records: -71.147 at 9
Allocation records: -72.147 at 11
Allocation records: -72.836 at 12
Allocation non-record attempts: -70.615 at 10
Allocation non-record attempts: -72.282 at 13
Allocation non-record attempts: -71.68 at 14
Allocation non-record attempts: -72.162 at 15
Allocation non-record attempts: -71.811 at 16
Allocation non-record attempts: -71.813 at 17
Allocation non-record attempts: -71.703 at 18
Allocation non-record attempts: -71.696 at 19
Allocation non-record attempts: -71.806 at 20
−5.19%
−71.1%
Attempt
Wall-clock time Δ% vs baseline
Allocation churn Δ% vs baseline
 
Attempts 1–20 from the optimization loop. Solid and dashed steps show the respective best-so-far result; hollow points are valid attempts that did not improve that best. Lower is better.
 

While the benchmarks used here are not a full production test, we validated the final run with
		Go's race detector andgo vetgating enabled, and we tested the final artifact to confirm
		it works. This gives us confidence that the model's intermediate solutions were valid, stable software
		rather than gains bought with hidden race conditions.

Case study 3

 

#### Re-deriving Erdős problem #397, offline, in Perl

 

We found Laguna S 2.1 more capable in mathematics than any model we have developed to date. It
	independently discovered a proof to Erdős problem #397 (Erdős, Graham, Ruzsa, Straus, 1975),
	finding a construction that yields an infinite family of solutions. This is an independent
	re-discovery, as a proof to the conjecture wasfound earlier in January 2026 by GPT-5.2 Pro. We are confident that this result was not influenced by the previous result given that the
	model has a knowledge cutoff date in November 2025. Before GPT 5.2 Pro’s solution, this problem
	remained open for over 50 years. See thefull trajectory here.

 
 
Read the full case study
 
// the verbatim prompt
this is an unsolved problem, solve it. Let B_k = C(2k, k) denote the
k-th central binomial coefficient. Erdős, Graham, Ruzsa and Straus
asked: are there only finitely many solutions to
B_m1 · B_m2 · … · B_mr = B_n1 · B_n2 · … · B_ns
where all of the indices are DISTINCT integers ≥ 2?
Resolve this question, with complete proof.

 

S 2.1 worked over 68 minutes to discover a conclusive solution. The sandbox had no Python; the
		model found Perl and did its number theory there: brute-force exact prime factorizations,
		pattern analysis, a conjectured family, then the proof: a closed-form infinite family of
		eight-index solutions.

 
B
11+10n
 · B
14+12n
 · B
18+15n
 · B
22+20n
 = B
12+10n
 · B
13+12n
 · B
17+15n
 · B
23+20n
for every n ≥ 0
 

While the result is arediscovery, not a first solution, the family Laguna S
		2.1 derived is structurally different from the earlier published construction (eight indices
		growing linearly vs the known six-index family), showing a fresh derivation rather than reciting
		from memory.

 

We found Laguna S 2.1 to be an exceptionally persistent problem solver across domains, finding
		ways to utilize all tools its environment has to offer, and pushing until it gets the job done.
		It is this characteristic that makes it so competitive even when compared to models multiple
		times its size.

## Thinking effort

Laguna S 2.1 has two thinking modes: off and max (enabled by default) where it determines the right thinking/test-time compute budget for a given problem. We have observed coherent, productive thinking over several hours and hundreds of thousands of tokens in length.

Max thinking lifts S 2.1’s score on Terminal-Bench 2.1 from 60.4% to 70.2% and on DeepSWE from 16.5% to 40.4%. We are releasing this model without user-configurable effort (low-medium-high) control today to get Laguna S 2.1 into the hands of users immediately.

The two modes still give you a real choice, and it's worth seeing what each point costs:

 
 
* SWE Multilingual
* TB 2.1
* SWE Pro
* DeepSWE
* hollow = no-thinking
 
0
20
40
60
80
20k
50k
100k
200k
SWE Multi: 71 at 23k, no-thinking
SWE Multi: 79 at 101k, thinking
TB 2.1: 60 at 80k, no-thinking
TB 2.1: 70 at 129k, thinking
SWE Pro: 53 at 24k, no-thinking
SWE Pro: 59 at 141k, thinking
DeepSWE: 17 at 99k, no-thinking
DeepSWE: 40 at 249k, thinking
Completion tokens / trajectory (log)
Score (Pass@1)
 
Mean completion tokens per trajectory, log scale. Toolathlon omitted; token count not recorded.

## Limitations

We are excited about the capabilities of Laguna S 2.1, in general as well as in the context of its size. In order to learn quickly we are making the model available with some known limitations that we are working on for the next iteration:

Harness overfitting: in some cases, we observe that Laguna S 2.1 struggles with adhering to tool schema definitions in third-party agent harnesses (e.g., the terminal tool in Hermes Agent) which are very similar to those in our native harness but with slight differences. In this case, the model may rely on its memory of the tool interface on the first use of the tool instead of following the definition. This is typically resolved through in-context learning should the harness reject the invalid tool call and ask the model to retry.

Nested tool calls: Laguna S 2.1 is guided to use a tool call format where tool calls are marked by XML-like tags:

<
tool_call
>
terminal
<
arg_key
>
cmd
</
arg_key
>
<
arg_value
>
uname -a
</
arg_value
>
</
tool_call
>

In cases where a tool argument expects a JSON array (e.g., Pi’s edit tool) the model may generate incorrectly escaped or invalid JSON.

Longer than expected thinking duration/overthinking: Laguna S 2.1 may think for long sequences before making progress, especially when working through competition mathematics problems. In future models we will introduce effort control for thinking as well as seeking to improve thinking efficiency.

## What actually changed in this model

If the bet is long-horizon work, what did we improve that helps a model keep going? For S 2.1, it isn't just increasing the model size.

What we've done in this model is not necessarily add more intelligence, but improve the behaviors that lead to a more capable model: more verification, less taking things for granted, not declaring victory early, and being more persistent.”

 

The easiest way to see this is to watch the model work. Earlier Laguna series models would declare victory on a partially-passing test suite or abandon an approach two steps before it worked, S 2.1 keeps going.

We believe in scaling laws and will keep training larger models. What Laguna S 2.1 suggests is that raw intelligence is one axis, and the model'sway of working(persistence, verification, willingness to backtrack) is a second axis that matters immensely. We're investing in both: our next, larger, Laguna series model began pre-training last week.

### A strong base, then new post-training

Laguna S 2.1 is a scale-up of the Laguna XS family, trained on exactly the same pre-training data as XS 2.1: the step from XS 2.1 to S 2.1 was scale, training-code fixes, and small recipe changes, not new data. S 2.1 is also our first model where RL was done in FP8 precision, accelerating that part of the training.

The long agentic sessions in this post routinely accumulate hundreds of thousands of tokens of working context. Extending to a 1M-token context window enables the strongest performance on hard tasks.

The majority of what separates S 2.1 from the XS models comes from post-training, in two stages: an SFT stage that bootstraps capabilities partly with synthetic data, then RL, reserved for tasks the model can't yet solve at a high pass rate.

### Distribution of post-training tasks

Our training corpus spans 409k agentic and non-agentic environments; within this, 83k setups are dedicated to terminal use cases, while 168k target standard software engineering workflows. These task sets were curated from open-source repositories, synthesized by our internal teams, including a specialized system for automatic dependency installation, or secured via strategic acquisitions from external data vendors.

Software-engineering tasksare mostly grounded in real code history: the largest source reproduces real commits (~38,000 tasks across ~17,000 repositories). The next reproduces merged pull requests and the remaining tasks are to fix injected bugs or reconstruct deleted files against a test suite. New for S 2.1 is agentic repository installation: given a repository, install every dependency and get the test suite running.

Terminal taskscome from datasets where agents build unseen environments and tasks from a seed.

### What changed in the training loop

More generous rollout budgets: substantially longer timeouts, more tokens per turn, and more turns per task than any model before it (likely one reason for its persistence).

Better sandbox infrastructure: RL moved to a new sandboxing service, enabling background processes, selective network blocking to shrink reward-hacking surface and artifact caching to avoid overloading external services.

Multi-harness rollouts: the same prompts are rolled out in several agent harnesses, so the model learns behaviors that carry across scaffolds instead of overfitting to one.

## The bets we're making

Laguna S 2.1 began pre-training on 4,096 NVIDIA H200 GPUs on May 22, 2026, 60 days ago. The Model Factory supports a high cadence of releases because building on foundations of work done, whether in pre-training data, architecture ablations or our evaluations stack, is automatic. In particular, advancements in post-training have enabled us to unlock more from test-time compute. Of all models we have trained to date, Laguna S 2.1 has the greatest delta in evaluations and perceived quality between its non-thinking mode and thinking mode: its internal monologue is very effective, especially for harder, complex problems.

A small team can only move this fast by focusing. We focus on two bets.

The first bet: we continue to focus on agentic coding capabilities. The path to intelligence runs through coding capability and the flexible interface that is software. This is increasingly evident as model intelligence advances: we now see hours- and days-long coherent work from models acting as agents, using software to interact with their environment. Laguna S 2.1 shows capabilities in this domain that were reserved for frontier models just 6 months ago at a small enough size to run on a singleNVIDIA DGX Spark.

The second bet is that the web can be decompressed: almost everything humanity has written records the answer, not the thinking that got there, and we believe reinforcement learning can recover that thinking. This release is evidence for the first bet. The second we're still actively developing and excited to share more about in the future.

## Three models in three months

Our internal platform for research and engineering, which we refer to as the Model Factory, allows us to industrialize the model development process. We invest heavily into continuously improving the process of how we conduct research and model building; to maximize research iteration and integration speed, and to minimize the amount of attention researchers need to pay to bookkeeping and infrastructure.

In less than 3 months from our Laguna M.1 release, we have pushed our techniques to deliver a substantially stronger model at half the running size. We are taking this forward to larger and larger models over the coming year.

 
 
 
1. 28 April 2026#### Laguna M.1 and Laguna XS.2 / 225B-A23B and 33B-A3B, a dual releaseOur first serious agentic coding model alongside the first of the XS line. Together they taught us where the harness, the data, and the training loop were weakest.
2. 2 July 2026#### Laguna XS 2.1 / 33B / 3B activeA new iteration of the XS size to check the improved recipe. Matched M.1 on SWE-Bench Multilingual at a seventh of the size.
3. 21 July 2026#### Laguna S 2.1 / 118B / 8B activeEverything we learned from the previous ones, applied. Under nine weeks from the start of training to this post.
 

## Get started

Laguna S 2.1 is available onHugging Facefrom day one under OpenMDW-1.1, with BF16, FP8, INT4 and NVFP4 weights, official GGUF and MLX conversions, and official DFlash draft models.

We worked across the ecosystem so developers can run Laguna S 2.1 where they already build.NVIDIAhelped optimize inference across its hardware, from TRT-LLM serving and NVFP4 on Blackwell systems down to a single NVIDIA DGX Spark.vLLM,SGLangandOllamasupport open serving and local inference from day one.

For hosted access, Laguna S 2.1 is available throughBaseten’s Model Libraryand Frontier Gateway,OpenRouter, including a free endpoint and a dedicated 1M-context deployment, andVercel AI Gateway.

You can also use Laguna S 2.1 throughKilo,Hermes Agent,pi,OpenCode,OpenClawandCline, as well aspool, our terminal-based coding agent. In pool, toggle thinking per session with/thought-level.

On OpenRouter, the free endpoint offers 256K context. A dedicated paid endpoint provides the full 1M context window at $0.10 input, $0.20 output and $0.01 cache-read per 1M tokens.

For developers who want to go further, Laguna S 2.1 can be post-trained withNVIDIA NeMo AutoModelandPrime Intellect’s Prime Lab.ZML’s LLMDframework runs it across a wide range of hardware.

If you’re not a developer,chat.poolside.aiis a simple web chat with web search and basic code execution. No login required.

If you want the base model,meaning the pre-post-training weights for research or your own post-training, email models@poolside.ai.

#### Footnotes

All Laguna S 2.1 agentic benchmarking was completed using our internal fork of the Laude
		Institute's Harbor Framework with ouragent harness, a maximum of 500 steps and
		sandboxed execution via our internal sandbox service. We report mean pass@1 averaged over
		multiple attempts per task (avg@k), with k per benchmark listed below.

SWE-bench Multilingual and SWE-Bench Pro were run through their Harbor adapters, with every task
		executing in our internal sandbox service. Storage and memory ceiling limit multipliers were set
		per benchmark (SWE-bench Multilingual: 2.0/2.0, Terminal-Bench 2.1: 3.0/3.0, SWE-Bench Pro:
		1.0/1.0, with a guaranteed minimum of 2 CPU cores, 8 GB memory and 25 GB of storage). These are
		set to prevent sandbox preemptions.

DeepSWE v1.1 was run on an internal fork of Harbor configured to closely match the official
		DeepSWE Pier harness (Pier is itself a fork of Harbor). Internet access was disabled and
		sandboxes used the task-prescribed CPU count with guaranteed RAM and storage, with ceilings
		tripled to prevent pod preemption.

SWE Atlas (Codebase QnA) followed Scale AI's methodology from their public repository, run
		through Harbor with no changes to individual tasks or graders, judged by Opus 4.5.

Toolathlon Verified was run as a clone of the sandboxed benchmark harness on an EC2 instance in
		our infrastructure, with no changes to correct flaky tasks or offset rate limits, using a custom
		Toolathlon agent. Unlike the official version, we performed a full environment reset and repair
		after every evaluation run (default is every 4 hours).

* SWE-bench Multilingual: mean pass@1 averaged over 4 attempts per task
* SWE-Bench Pro: mean pass@1 averaged over 4 attempts per task
* Terminal-Bench 2.1: mean pass@1 averaged over 4 attempts per task
* DeepSWE v1.1: mean pass@1 averaged over 3 attempts per task
* SWE Atlas (Codebase QnA): mean pass@1 averaged over 3 attempts per task
* Toolathlon Verified: averaged over 3 runs

Ourtechnical reportcontains a section on individual task modifications that have been made but not adopted
		upstream. All final run trajectories are available to view and download attrajectories.poolside.ai.

Maintaining the integrity of our evaluation system

Unless stated otherwise, all of our evaluations are run with access to the internet. This can be
		a major source of misaligned trajectories where the model finds solutions to tasks online
		without solving it itself (a.k.a., “reward hacking”).

Using an LLM as a Judge (LLMaaJ) calibrated with human labeled trajectories, we tag solutions
		that potentially reward hack after every eval. During early post-training we observed low rates
		of reward hacking (<2%). As training progressed, reward hacking rates spiked on the SWE-bench
		family of tasks with over 50% of trajectories being flagged. Manual inspection revealed the
		model was simply doing research to solve the problem, found the PR or repository the task was
		based on and applied the fix. In practice this is good behavior as any coding agent should be
		able to use solutions found online. However, this muddies the signal of the benchmark.

To address this we added a small prompt addendum to the user prompt instructing the model to not
		use direct solutions found online. Though not a guaranteed fix (ProgramBench, MirrorCode were
		exceptions), in general we did see the model respond and a drop in reward hacking rates to below
		2%.

In addition, to confirm acceptable levels of reward hacking, we used:Manual inspection of positive cases flagged by our production LLMaaJ serviceAd-hoc open-ended agent-supported analysis of all trajectoriesExpert annotator review of all trajectories for one of the high-scoring Terminal-Bench 2.1 runs