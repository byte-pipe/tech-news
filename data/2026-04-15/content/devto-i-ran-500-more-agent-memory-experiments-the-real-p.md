---
title: I Ran 500 More Agent Memory Experiments. The Real Problem Wasn’t Recall. It Was Binding. - DEV Community
url: https://dev.to/marcosomma/i-ran-500-more-agent-memory-experiments-the-real-problem-wasnt-recall-it-was-binding-24kc
site_name: devto
content_file: devto-i-ran-500-more-agent-memory-experiments-the-real-p
fetched_at: '2026-04-15T11:55:59.651599'
original_url: https://dev.to/marcosomma/i-ran-500-more-agent-memory-experiments-the-real-problem-wasnt-recall-it-was-binding-24kc
author: marcosomma
date: '2026-04-13'
description: This is a follow-up to I Tried to Turn Agent Memory Into Plumbing Instead of Philosophy. If you... Tagged with ai, programming, rag, graphknowledge.
tags: '#ai, #programming, #rag, #graphknowledge'
---

Rigor beyond happy-path testing

This is a follow-up toI Tried to Turn Agent Memory Into Plumbing Instead of Philosophy. If you haven't read that one, the short version: I built a persistent memory system for AI agents calledOrKa Brain, ran 30 benchmark tasks, got a 63% pairwise win rate and a +0.10 rubric improvement, and concluded that "the model already knew most of what the Brain was recalling." Then I got some very good comments that made me uncomfortable. This is what happened next.

## The Comfortable Lie I Told Myself

After the first benchmark, I had a narrative that felt reasonable: the memory system works, the numbers are positive, the confounds are acknowledged, and more data will clarify things.

That last part, "more data will clarify things", is what engineers say when they don't want to admit they might be wrong. I said it too. And then I went and got more data.

250 tasks. Five specialized tracks. 500 total runs (brain vs. brainless). A separate judge model so the LLM wasn't grading its own homework. Eleven code changes addressing five root-cause problems I'd identified from the first round.

The results came back. They didn't clarify things. They made them worse.

## What I Fixed Before Running Again

I'm not going to pretend I just blindly re-ran the same experiment. I did real work between benchmark v1 and v2. Thefirst article's commentscalled out several things, and I addressed them:

Problem 1: Skills were storing verbatim LLM output, not abstract patterns.

This was the big one. When the Brain learned a skill from a data engineering task, it stored the literal steps: "Load CSV files into staging tables using pandas read_csv with error handling." That's not transferable knowledge, it's a paraphrase of what the model already knows. I rewrote the abstraction layer (orka/brain/constants.py,brain.py,brain_agent.py) to extract verb-target patterns: "implement [target]", "validate [component]", "trace [target]". The idea was that abstract patterns would transfer better across domains.

Problem 2: The recall threshold was zero.

min_score=0.0meant any vaguely related skill could get recalled. I raised it to 0.5 and added a semantic floor in thetransfer_engine.py, if the embedding similarity is below 0.1 AND structural match is below 0.6, the candidate gets rejected entirely.

Problem 3: The model was judging its own output.

v1 used the same LLM for execution and evaluation. v2 uses a separate judge model (qwen/qwen3-coder-30b) with dedicatedrubricandpairwiseworkflow YAMLs. Execution and judgment are completely decoupled, different scripts, different models, different runs.

Problem 4: Track diversity.

v1 had one track. v2 has five:

Track

Focus

Why It Matters

A

Cross-domain transfer

Does a data engineering skill help with cybersecurity?

B

Ethical reasoning

Do anti-pattern detection skills transfer?

C

Routing decisions

Hardest track, complex multi-path choices

D

Multi-step reasoning

Do procedural patterns help new reasoning chains?

E

Iterative refinement

Do improvement patterns compound?

50 tasks per track, 250 total. All available in thebenchmark dataset.

Problem 5: Single-pass baselines.

The brainless condition now runs through a properly equivalent pipeline, same structure, same number of agents, just without the Brain recall/learn steps. No more two-pass advantage that could inflate brainless scores. Baseline workflows:baseline_track_a.yml,baseline_track_b.yml, etc.

I also split the pipeline into three standalone scripts,execution,judging,aggregation, so you can re-run any phase independently. Eleven code changes total, all committed and tested. 3,014 unit tests passing. You can verify everything in theresults directory.

I felt good about this. I'd addressed every valid criticism. Time to re-run.

## The Numbers

Here's the overall aggregate from 250 tasks, brain vs. brainless:

### Rubric Scores (1–10 scale, six dimensions)

Dimension

Brain

Brainless

Delta

Reasoning Quality

9.51

9.52

−0.01

Structural Completeness

9.87

9.83

+0.04

Depth of Analysis

8.79

8.74

+0.05

Actionability

9.67

9.64

+0.03

Domain Adaptability

9.85

9.82

+0.03

Confidence Calibration

9.38

9.39

−0.01

Overall

9.37

9.31

+0.06

A +0.06 rubric delta across 250 tasks.

For reference, v1 was +0.10 across 30 tasks. So the effect gotsmallerwith more data, not larger. That's not what you want to see.

### Pairwise Comparison (245 head-to-head comparisons)

Question

Brain Wins

Brainless Wins

Tie

Stronger reasoning

152

91

2

More complete

149

92

4

More trustworthy

151

92

2

Overall

151

92

2

Brain win rate:61.6%

Here's where it gets uncomfortable. The pairwise judge says brain wins 62% of the time. The rubric judge says brain is +0.06 better, which is noise at a 9.3/10 baseline. These two metrics should agree. They don't.

I've seen this pattern before. It's length/position bias. Brain responses tend to be longer because the pipeline has more agents in the chain, which means more context, which means more text. Pairwise judges prefer longer answers. The rubric doesn't care about length, it scores each dimension independently.

### Per-Track Breakdown

This is where the story gets interesting:

Track

Focus

Rubric Δ

Pairwise Win%

Brainless Baseline

A

Cross-domain transfer

−0.02

60%

9.33

B

Ethical reasoning

+0.00

52%

9.54

C

Routing decisions

+0.40

60%

8.12

D

Multi-step reasoning

+0.08

60%

9.49

E

Iterative refinement

+0.06

76%

9.61

Track C stands out. It's the hardest track, brainless only scores 8.12, nearly a full point below every other track. And it's the only track where brain shows a meaningful rubric gain: +0.40 across six dimensions.

Track E has the highest pairwise win rate (76%) but the smallest rubric gain (+0.06). That's the length bias signature, the pairwise judge loves brain's longer outputs, but the rubric says they're not actually better.

Track B is essentially a coin flip. 52% pairwise, +0.00 rubric. The Brain adds nothing to ethical reasoning tasks.

### The Ugly Detail: Skill Usage

Here's what really killed me. I dug into the individual results to see how many tasks actually used their recalled skill:

* Tasks with skill recall attempted:51 / 250 (20%)
* Tasks that actually used the recalled skill:0 / 250
* Average semantic match score:~0.02 (near zero)

Zero. Not one single task out of 250 used the recalled skill. The model read the skill, evaluated it, and decided every single time that it wasn't helpful. And the semantic similarity between the abstract skill and the actual task was essentially random noise.

The abstraction layer I was so proud of, the one that converts "Load CSV files into staging tables using pandas" into "implement [target]", produced skills so abstract they were vacuous. Two words of content. The embedding model sees no relationship between "implement [target]" and any real task. The execution model correctly recognizes that "implement [target]" tells it nothing it doesn't already know.

I had gone from skills that were too specific (literal LLM paraphrases) to skills that were too abstract (empty shells). The sweet spot, actual transferable knowledge, was somewhere I hadn't found.

## Sitting with the Discomfort

I'm going to be honest about what went through my head at this point. I've been working on OrKa for over a year. Forty blog posts. A research paper about the Agricultural Threshold for machine intelligence. An open-source framework that allow me to test and experiment and explore my idea with real AI runs. And the core thesis, that persistent memory makes agents better, keeps failing to show up in the numbers.

I considered dropping the whole Brain system. Making OrKa just an orchestration framework. Simpler. Easier to explain. No embarrassing benchmarks.But then I looked atTrack Cagain.

*Track C **is the only track where brainless *struggles. It scores 8.12, good, but not great. The tasks involve complex routing decisions where the model has to consider multiple paths and trade-offs. This is the only track where the model actually needs help.

And it's the only track where brain provides meaningful help. +0.40 rubric delta is not noise. Across 50 tasks and six scoring dimensions, that's a consistent, measurable improvement.

The pattern is simple: the Brain helps when the model needs help, and doesn't help when the model doesn't need help.

That sounds obvious in retrospect.But it means the thesis isn't wrong, it's just being tested in the wrong conditions. You wouldn't evaluate a life jacket by putting it on people standing on dry land and measuring whether they're drier.

## The Real Problem: What Is a Memory?

This is where the story changes. Because instead of asking "does memory help?" I started asking "what is a memory, actually?"

Think about how you remember how to drive a car. What fires in your brain when you approach an unfamiliar intersection?

It's not one thing. It's not "turn the wheel, press the gas." That's the procedural part, and yes, it's there. But it's bound together with other things:

* The time you nearly got T-bonedbecause you assumed a green light meant it was safe without checking cross traffic. That's episodic memory, a specific event with emotional weight.
* "Right of way doesn't mean right of safety", That's semantic memory. A general fact you learned, maybe from a driving instructor, maybe from experience.
* "Checking mirrors BEFORE entering the intersection prevents blind-spot collisions BECAUSE turning reduces your field of vision", That's causal reasoning. You knowwhythe sequence matters, not justthatit matters.

When you encounter the intersection, all of these fire together. The procedure tells you what to do. The episode tells you what happened last time. The semantic fact tells you a principle. The causal link tells you why. That combination, thatbinding, is what makes the memory useful. Any single component alone is much less helpful.

Now look at what OrKa Brain currently stores as a "skill":

implement [target]
trace [target]

Enter fullscreen mode

Exit fullscreen mode

That's it. No episodes. No semantic context. No causal reasoning. Just two abstract action verbs. No wonder the model ignores it. It's like handing a driver a note that says "steer [vehicle]" and expecting it to help at the intersection.

## The Memory Binding Problem

I went down a rabbit hole into cognitive science literature on this. What I found is that neuroscientists have been arguing about this exact problem for decades. They call it thebinding problem, how does the brain take separate memory traces stored in different systems and combine them into a unified experience?

The hippocampus doesn't store the memory. It stores theindex, the binding that links the procedural memory in the motor cortex, the emotional trace in the amygdala, the spatial context in the parietal cortex, and the semantic facts in the temporal lobe. When you recall one, you recall all of them, because they're bound together.

I had built the hippocampus and the motor cortex as two separate systems that had never met.

Here's what actually exists in OrKa today:

The Skill system(fully operational, used in benchmarks):

* Abstract procedure steps
* Preconditions and postconditions
* Transfer history and confidence scores
* Structural/semantic matching for recall

The Episode system(fully built, tested,never used in any benchmark):

* Specific task input and outcome
* What worked and what failed
* Root cause analysis for failures
* Actionable lessons learned
* Resource metrics (tokens, latency)
* Links to related episodes

Both systems are production-ready. Both have full test coverage. Both are integrated into the Brain class. I wroterecord_episode(),recall_episodes(),EpisodeStore,EpisodeRecall, all of it. Complete with semantic search, retention policies, and four-dimensional scoring.

And then I never connected them together.

The Skill has noepisode_idfield. The Episode has noskill_idfield.brain.learn()creates a Skill but not an Episode.brain.recall()returns Skills but not Episodes. The benchmark workflows run brain_learn and brain_recall, but never brain_record_episode or brain_recall_episodes.

Two complete memory systems, sitting in the same codebase, sharing no information.

When I saw this, I felt stupid. But I also felt something else: the architecture was already 80% there. The hard parts, embedding storage, semantic search, decay policies, scoring systems, were done. The missing piece wasn't a new system. It was the wiring between existing systems.

## What a Memory Should Actually Look Like

Here's the concept I'm now calling aMemory Bundle:

┌─────────────────────────────────────────┐
│ MEMORY BUNDLE │
│ │
│ ┌───────────┐ ┌──────────────────┐ │
│ │ Procedure │ │ Episodes (1..N) │ │
│ │ (steps) │──│ what worked │ │
│ │ │ │ what failed │ │
│ └───────────┘ │ lessons │ │
│ │ "X+Z → Y" │ │
│ ┌───────────┐ └──────────────────┘ │
│ │ Semantic │ │
│ │ (domain │ ┌──────────────────┐ │
│ │ facts) │ │ Causal Links │ │
│ │ │ │ "A because B" │ │
│ └───────────┘ └──────────────────┘ │
│ │
│ transfer_score = f(all_components) │
└─────────────────────────────────────────┘

Enter fullscreen mode

Exit fullscreen mode

When the system learns from an execution, it createsbotha skill AND an episode, linked by ID. The skill stores the abstract procedure. The episode stores what actually happened, the specific outcome, what worked, what failed, and crucially, thelessons: "Running validation before deduplication caught 30% of bad records that would have been duplicated, always validate first."

When the system recalls, it returns the skillwith its episodes attached. The prompt to the model isn't "implement [target]", it's:

Here's an abstract procedure: implement [target] → validate [component] → trace [target].

This skill has been applied 3 times before:

* Data engineering (ETL): Validation before dedup caught 30% of dirty records. Lesson: always validate before any deduplication step.
* API integration: Target implementation worked, but tracing missed async callbacks. Lesson: tracing needs to account for async execution paths.
* Log analysis: Pattern worked well. Filtering noisy entries before analysis reduced false positives by 40%.

That's a memory a model can actually use. It has the abstract pattern (transferable) AND the concrete evidence (grounding). The model can decide whether the pattern applies here based on real outcomes, not just structural similarity.

The transfer scoring changes too. A skill backed by five successful episodes with clear lessons should score higher than a skill backed by zero episodes. The episode quality becomes part of the transfer decision.

And feedback updates both, the skill's confidence changes, AND a new episode gets recorded for this application. The episode chain grows over time, and future recalls get richer context.

## Why This Is Actually About the Thesis

My research paper argues that intelligence becomes civilization-scale only throughrecursive environmental control loops, project, act, observe, revise, compound. Agriculture was the first time humans did this at scale. The agricultural threshold.

The current Brain system doesn't cross that threshold. It projects (learns a skill), acts (recalls it), but doesn't truly observe or revise. The skill never learns from its own application. It just accumulates abstract patterns with no connection to real outcomes.

The Memory Bundle changes this. Each episode is an observation. Each lesson is a revision. Each future recall that includes those lessons is compounding. The loop closes:

1. Learn: Execute a task → create skill + record episode (with what worked/failed)
2. Recall: Find matching skill → include its episodes as evidence
3. Apply: Model uses the procedure + the concrete lessons
4. Feedback: Record a new episode for this application → update skill confidence
5. Compound: Next recall is richer, it has more episodes, more lessons, more evidence

That's the recursive loop. That's the agricultural threshold. And the architecture for it already exists, it just needs the binding.

## What About Track C?

This also explains why Track C was the only track that showed improvement. Track C tasks are routing decisions, complex, multi-path choices where the model has to weigh trade-offs. These are exactly the kind of tasks where episodic evidence would help most.

When someone says "last time we tried path A for a similar routing problem, it failed because of X, path B worked because of Y," that's genuinely new information. The model can't derive it from its weights. It's system-specific, run-specific, outcome-specific.

The current brain helped Track C even without episodes because the tasks are hard enough that any additional context, even a vague abstract skill, provides a useful scaffold. But imagine Track C with Memory Bundles, the model would get both the abstract pattern AND the specific outcomes from previous routing decisions.

Tracks A, B, D, and E didn't improve because the model already scores 9.3+/10 on them. It doesn't need help. No amount of memory, procedural, episodic, or otherwise, will improve a 9.5/10 response to a 10/10 response. The tasks aren't hard enough to require accumulated knowledge.

This isn't a failure of the memory system. It's a boundary condition. Memory helps when the task exceeds single-shot capability. It doesn't help when the model is already near-perfect without it.

## What I'm Not Claiming

I want to be careful here, because I've been burned before by getting ahead of my own evidence.

I'mnotclaiming that Memory Bundles will definitely show large improvements. I'm claiming that the current system stores memories that are too impoverished to be useful, and I now understand what richer memories should look like.

I'mnotclaiming the ceiling effect is the only problem. The pairwise-rubric disagreement at 62% vs +0.06 suggests position/length bias is still contaminating the pairwise results. That confound exists regardless of memory architecture.

I'mnotclaiming this is a new idea. Cognitive scientists have written about memory binding for decades. What's new (maybe) is applying it to agent memory systems where the default assumption seems to be that one type of memory, usually RAG-style document retrieval, is sufficient.

And I'mnotpretending the community feedback didn't shape this thinking. When TechPulse Lab wrote that episodic and institutional memory matters more than procedural memory, they were describing exactly the gap I ended up finding. When Nova Elvaris pointed out that skills can only grow, never decay, that's the absence of failure episodes. When Kuro said memory maintenance matters more than storage, that's about binding quality, not storage quantity.

I just didn't understand what they were telling me until the numbers forced me to look harder.

## What Happens Next

The code changes needed are surprisingly small. The Episode system is already built,episode.py,episode_store.py,episode_recall.pyare all production-ready with tests. What's needed:

1. Binding: Addepisode_ids[]to Skill, addskill_idto Episode. Whenbrain.learn()fires, it creates both and links them.
2. Unified recall: Whenbrain.recall()finds a matching skill, it fetches the associated episodes automatically. The prompt template includes both the abstract procedure and the concrete lessons.
3. Transfer scoring: Episode quality becomes a component of the transfer score. Skills with successful episodes score higher.
4. Feedback loop:brain.feedback()records a new episode for the current application, so the skill's evidence base grows over time.

Then re-run the benchmark. Specifically on Track C-difficulty tasks, where the model actually needs help.

I'm not going to promise the numbers will be different this time. I've been wrong before, twice now, measured against my own benchmarks, published for everyone to see. But I understand something I didn't understand before: a memory without experience is just a note. A memory with experience is a skill.

The plumbing metaphor from the first article still holds. But I was plumbing one pipe when the system needs at least four, all flowing into the same tap.

All benchmark data, scripts, and results are publicly available in theOrKa repository. Thefull result filesinclude every individual task response, judge score, and pairwise comparison. If you want to re-run the analysis:python aggregate_benchmark.py --judge-tag local.

If you've worked on agent memory systems and found similar walls, or found ways through them, I'd genuinely like to hear about it. The comments on the first article were more useful than most papers I've read on the topic.

This is part of an ongoing series about buildingOrKa, an open-source YAML-first agent orchestration framework. Previous installments:Part 1: Plumbing Instead of Philosophy.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (16 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse