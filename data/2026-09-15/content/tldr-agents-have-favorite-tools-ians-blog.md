---
title: Agents have favorite tools – Ian’s Blog
url: https://ianbarber.blog/2026/09/14/agents-have-favorite-tools
site_name: tldr
content_file: tldr-agents-have-favorite-tools-ians-blog
fetched_at: '2026-09-15T15:27:53.275689'
original_url: https://ianbarber.blog/2026/09/14/agents-have-favorite-tools
date: '2026-09-15'
published_date: '2026-09-15T04:23:47+00:00'
description: Agents have some pretty deep behavioral grooves around tools, annoyingly.
tags:
- tldr
---

# Agents have favorite tools

Written by

Ian

in

ML Infrastructure

A lot of people use coding agents like software engineers (forall kinds of things, it turns out), and adopt a dealing-with-humans mindset about how that works. If a model has a useful tool, and you give it another useful tool, then it gets the capabilities from both.

Largely that seems… not true? You can make a tool available, but then the model has to decide to use it, and often it just doesn’t. My recentfutzing with LSPsran pretty directly into this. One follow-up from there was to try the Python part ofSWE-Bench ProMax, a benchmark built around large, coordinated refactors. This is exactly the type of work where an LSP’sfind referencesshould come in handy.

Helpfully, Aaron Pollack pointed me at theCodeAnchor paper, whose authors had run into pretty much the same problem. They had tried giving their agent a call-graph tool and…

“we observed low tool-use rates: the agent typically relied on plain grep instead.”

Rather than retraining the model, they put the call-graph context into the relevant code itself, adding annotations like“used by: foo, bar”near the definition. I tried a variant of this by annotating not the code, but the grep results: when the agent searched for a symbol, the LSP found references and appended them to the grep output.

From looking at the failed traces, it was clear the annotations were working. Of the 99 files surfaced by them, all 99 were opened, and 92 got patches. This resulted in fewer turns, and it did seem to help with run-to-run variance, which was also a benefit the CodeAnchor folks saw: I had fewer runaway runs with the annotations than without.

The most common failure, though, was incomplete refactors. The model would find the core fix quickly, edit it correctly, then miss other files which also needed changing. The misses were ones the LSP didn’t really help with: they were about compliance with long, winding specs. It is possible to use LSP tools to help with these, but the model didn’t.

Injecting tool-derived context got rid of the adoption problem, buthowthe model behaved was still driven by its learned tool-use policy.

There is some interesting academic and non-academic work around this idea of tool use as a behavioral policy, and a surprisingly predictable one at that.BiasBustersshowed that models have strong preferences among functionally equivalent tools.AutoToolfound that tool calls tend to follow predictable sequences, and used previous agent trajectories to predict the next tool and bypass some inference entirely. On the non-academic side, whenSteve Yeggewas building the Beads CLI he let the agents hallucinate arguments and then just added them, so the tool naturally conformed to the expectations the model already had.

You can swap in tools which have roughly the same shape as ones models are familiar with, and you can add output to familiar tools to give them more information. But getting models to use new tools, or to use tools differently, seems much trickier.

The lab answer seems to be, once again: more RL then.

DeepSeek’sV4.1-Flash technical report, which we discussedyesterday, is particularly explicit about this. Their post-training approach is pretty standard: SFT, then RL, then on-policy distillation. What is new is automatically generating tasks and environments to train the agent with. They seed these from internal agent sessions that show poor model performance, and popular GitHub repositories:

“coding-agent sessions from internal employees and external partners … [and] public GitHub repositories that meet a star-count threshold.”

If you want models to get good at your tools: make sure they are really popular, or get a job at a lab and fail a lot.

agents
 
big-tech

## More posts

* ### Agents have favorite toolsSeptember 14, 2026
* ### Agents love prefillSeptember 13, 2026
* ### Test Time TrainingSeptember 2, 2026
* ### Chunky AgentsAugust 28, 2026