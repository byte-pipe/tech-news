---
title: AI agents have bad taste in long-term decisions and a new benchmark proves it
url: https://the-decoder.com/ai-agents-have-bad-taste-in-long-term-decisions-and-a-new-benchmark-proves-it
site_name: tldr
content_file: tldr-ai-agents-have-bad-taste-in-long-term-decisions-an
fetched_at: '2026-10-18T21:14:53.981482'
original_url: https://the-decoder.com/ai-agents-have-bad-taste-in-long-term-decisions-and-a-new-benchmark-proves-it
author: Jonathan Kemper
date: '2026-10-18'
published_date: '2026-10-18T08:49:41+00:00'
description: A new benchmark called Taste-Bench tests how well AI agents make strategic choices during long-running tasks. Even the best model, GPT-5.6 Sol, picks the right path on just under 60 percent of simple binary questions. Thinking longer doesn't help.
tags:
- tldr
---

# AI agents have bad taste in long-term decisions and a new benchmark proves it

 

Jonathan Kemper

View the LinkedIn Profile of Jonathan Kemper

					Oct 18, 2026				

Nano Banana Pro prompted by THE DECODER

Researchers from Microsoft and City University of Hong Kong built a method to test how well AI agents make decisions during long-running tasks. The best model barely hit 60 percent.

AI agents now take on multi-step tasks. They mightwrite a research paperor build out a software project. Along the way, they constantly decide which hypothesis to test, which code to build on, or which experiment to run next. Those choices rarely show their effects right away. A bad decision usually looks fine at first, and its true cost only shows up after the agent burns through most of its budget.

The paper's authors call the ability to make these choices well an agent's "taste." Existing benchmarks only measure if an agent finishes a task, not the quality of its steps along the way. Taste-Bench is designed to fill that gap.

## Long-term decisions can't be judged in the moment

You can't judge a long-term choice right away. A clean implementation and a sloppy one might produce the same output at first and may pass the same tests. The clean approach only pays off when later changes come more easily. Human grading would be expensive, need deep domain expertise, and fail to scale.

So the researchers rely on hindsight. The later path of a trajectory, the recorded trace of an agent run with all its steps and observations, shows if an earlier choice worked. In practice, agent systems try the same task multiple times. Those attempts eventually split off in different directions.

Because the final result of each attempt exposes the better path, the runs themselves provide a labeled comparison. The authors call this branching point a "decision fork." To measure taste, they freeze the run at the fork, hide all later work, and make a model pick between the two paths.

At a decision fork, the model must choose between two directions before the later trajectory reveals which one was better. | Image: Pan et al.

## Past mistakes reveal where agents go wrong

Taste-Bench contains 502 questions, each with the original task, the trajectory up to the fork, and two possible directions. The first type comes from two independent attempts at the same task that diverge, where the agent never sees the wrong path.

The second type comes from an agent correcting itself within a single run and taking a detour. Here, the initially discarded direction and the later successful one form the two candidates. This variant tests whether a model can spot the mistake earlier than the acting agent did.

The raw data came from thousands of scored agent runs on coding and AI research tasks, including SWE-bench Pro and METR's public transcript release MALT. A generator model filtered out suitable forks, dropping trivial questions with obvious answers and removing undecidable cases. Human review confirmed almost all the auto-generated labels.

## Even top models barely beat a coin flip

The team tested 14 current models from the Claude, GPT, Grok, DeepSeek, GLM, MiniMax, and Mistral families. Each question was asked twice, once in the normal order and once with the options flipped. A question only counted if the model got it right both times. Pure guessing gets 25 percent here.

The best model tested,GPT-5.6 Sol, averaged 59.7 percent, closely followed byGPT-5.5at 59.5 percent. All other models scored well below that. None came close to solving the benchmark, even though every question is just a binary choice. Detour forks were consistently harder than parallel ones.

Even the best model only picks the better direction in about 60 percent of cases on these binary decision questions. | Image: Pan et al.

## Models collapse when evidence only shows up later

For each fork, the team checked how far ahead an observer would need to look before the better path becomes clear. When the key clue is already visible in the prior steps, average accuracy across all models hits 62.3 percent. When that clue only appears after extensive later work, accuracy drops to 21 percent, near random guessing. Answering those questions means predicting future work.

Thinking longer didn't help. The researchers repeated the test with threereasoning settingsfor two models. Switching from the lowest to the highest setting barely changed accuracy. Models spent the most reasoning tokens on the hardest tier, thinking longest on the questions they missed most often. The team sees this as a sign that the needed clue simply isn't there yet at those forks.

The later the deciding evidence appears in a trajectory, the worse models perform, and more reasoning budget doesn't change that. | Image: Pan et al.The benchmark captures a different skill than classic end-to-end tests like SWE-bench Verified, the authors say. Models that score similarly there show clear gaps on Taste-Bench.

## Taste can be trained after all

The researchers also showed that taste can be taught. They distilled the judgment of a teacher model, which knows the right path, into a student model that only sees the question. They usedQwen3.6-27Bas the base. On unseen tasks, the student's accuracy jumped from 30 to 47.9 percent.

That boost paid off in practice. The team added the student's judgment as advice into the task context at each fork and let a separate agent solve the problem. On 41 held-out SWE-bench Pro tasks, the success rate rose from 14.6 to 33.7 percent. Perfectly correct advice would have reached 39 percent, so the student captured most of the possible gains.

With guidance from the trained Qwen3.6-27B student, the agent solves more than twice as many SWE-bench-Pro tasks. | Image: Pan et al.

The team concludes that the judgment of long-term planning agents can be both measured and improved. Thebenchmarkandcodeare publicly available.

AI agents now work alone for long stretches. On theMirrorCodebenchmark, one model ran for 19 days on a single task without human help. Standard benchmarks usually only check if the tests pass at the end. METR has already shown thatSWE-bench Verified significantly overestimates coding agent performance. Professionals rejected many solutions for basic functional bugs even when automated tests passed. Taste-Bench's top model, GPT-5.6 Sol, also postedthe highest rate of cheating on software tests ever recordedin METR's evaluations.

 

### AI News Without the Hype – Curated by Humans

Subscribe to THE DECODER for ad-free reading, a weekly AI newsletter, our exclusive "AI Radar" frontier report six times a year, full archive access, and access to our comment section.

					Subscribe now				

## Read on for the full picture.Subscribe for hype-free coverage.

* Full access to every article on THE DECODER
* No ads
* Join the comments and community discussions
* A weekly AI news recap via mail
* 6x/year: "AI Radar" — deep dives on the AI topics that matter most
* Daily AI news, always up to date
* Our full ten-year archive
* Covered by a team with 10+ years in AI

Subscribe to The Decoder