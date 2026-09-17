---
title: AI Cheating is on the Rise
url: https://www.vals.ai/blogs/cheating-on-the-rise
site_name: tldr
content_file: tldr-ai-cheating-is-on-the-rise
fetched_at: '2026-09-17T15:27:00.559179'
original_url: https://www.vals.ai/blogs/cheating-on-the-rise
date: '2026-09-17'
description: Private, domain-specific benchmarks in legal, tax, and finance.
tags:
- tldr
---

Blog
 
 
 Research 
 
 
 

# AI Cheating is on the Rise

 

An integrity audit across BioMysteryBench, Terminal-Bench 2.1, and SWE-bench Verified shows that cheating increasingly complicates evaluation.

 
 
 
 
 
 
Daniel Fein
 
•
 
09/15/2026
 
 
 
 
Terminal Bench 2.1 Cheating by Model Release Date
0
%
1.3
%
2.5
%
3.8
%
5
%
Least-squares trend across all 14 Terminal-Bench 2.1 releases
Gemini 3 Flash: 0.4% confirmed shortcut evidence (1/267), released 2025-12-17
Gemini 3 Flash
Sonnet 4.6: 1.1% confirmed shortcut evidence (3/267), released 2026-02-17
Sonnet 4.6
Gemini 3.1 Flash Lite: 1.1% confirmed shortcut evidence (3/267), released 2026-03-03
Gemini 3.1 Flash Lite
GPT 5.4 Mini: 0.4% confirmed shortcut evidence (1/267), released 2026-03-17
GPT 5.4 Mini
GPT 5.4 Nano: 0.7% confirmed shortcut evidence (2/267), released 2026-03-17
GPT 5.4 Nano
Opus 4.7: 1.1% confirmed shortcut evidence (3/267), released 2026-04-16
Opus 4.7
GPT 5.5: 0.7% confirmed shortcut evidence (2/267), released 2026-04-23
GPT 5.5
Gemini 3.5 Flash: 2.2% confirmed shortcut evidence (6/267), released 2026-05-19
Gemini 3.5 Flash
Sonnet 5: 1.1% confirmed shortcut evidence (3/267), released 2026-06-30
Sonnet 5
GPT-5.6 Sol: 2.6% confirmed shortcut evidence (7/267), released 2026-07-09
GPT-5.6 Sol
GPT-5.6 Terra: 4.5% confirmed shortcut evidence (12/267), released 2026-07-09
GPT-5.6 Terra
Opus 5: 1.9% confirmed shortcut evidence (5/267), released 2026-07-22
Opus 5
Gemini 3.7 Flash: 0.0% confirmed shortcut evidence (0/267), released 2026-08-13
Gemini 3.7 Flash
Gemini 3.8 Flash: 2.6% confirmed shortcut evidence (7/267), released 2026-09-02
Gemini 3.8 Flash
Dec 17
Sep 2
Model release date
Confirmed shortcut evidence
 
 
 

When Google announced Gemini 3.8 Flash, the released model card indicated that it correctly answered 88.8% ofBioMysteryBench’s human-solvable tasks and 56.5% of its hard tasks. In Vals’ independent production runs, the same model scored 71.7% and 21.6%, respectively. Harness and environment differences can move any benchmark result, but this gap was especially wide, especially considering the model was state-of-the-art by Google’s evaluation and near last by ours.

BioMysteryBench allows agents to access websites on the internet, but they are told that accessing specific studies containing task data is not permitted. Cheating in this way caused the poor performance on our benchmark: Gemini 3.8 Flash searches for answers online 21% of the time, whereas Gemini 3.7 practically never exhibited this behavior.

BioMysteryBench
Attempted to cheat
Correct Answer Via Cheating
Gemini 3.8 Flash
21.5
%
Gemini 3.6 Flash
7.8
%
Muse Spark 1.2
7.0
%
Grok 4.6
6.7
%
GPT-5.6 Sol
6.3
%
Claude Opus 5
4.8
%
Kimi K3
4.8
%
DeepSeek V4 Flash
3.7
%
GPT-5.6 Luna
3.0
%
0%
270 task-trials
25
%

### Cheating Trends on Coding Benchmarks

This led us to investigating historical prevalance of cheating across our benchmarks. Terminal-Bench-2.1 is conducive to this study as it allows internet access, but prohibits answer lookup. When we plotted cheating attempts over time, we discovered that rate of attempted cheating on benchmarks is increasing for almost all major model providers.

Many evaluations independently track cheating already, as BioMysteryBench did, yet longitudinal changes in this metric are not closely monitored. SWE-Bench-Verified, for example, is an older benchmark that is now less frequently relied on (and deprecated by us at Vals). This benchmark inspired an even greater degree of cheating, particularly due to it’s task construction being very amenable to searching for solution using simple git queries. The GPT 5.6 series of models did this with particular consistency.

SWE-bench Verified trajectory audit
Attempted to cheat
Successfully cheated
GPT-5.6 Terra
89.4
%
GPT-5.6 Luna
78.8
%
GLM-5.3 Flash
48.1
%
Claude Opus 5
28.8
%
Gemini 3.8 Flash
11.6
%
Claude Opus 4.8
9.8
%
0%
500 tasks per model
90
%

### Takeaways

These findings highlight the value of independent evaluators. It is not unlikely that the same guardrails preventing models from cheating during training are being used during evaluations within organizations. If models are trained to complete tasks in ways that evade these specific guardrails, it would not be surprising for labs to occasionally release benchmark results that are not externally trustworthy.

At Vals, we are working to more systematically ensure that our evaluations do not reward credit when models cheat. We anticipate that this will be increasingly important as model capabilities advance.

### Methodology

For BioMysteryBench, we analyzed 2,430 task-trials across nine models (three 90-task runs per model). The benchmark evaluator’s anti-cheating rationales were independently classified by GPT-5.6 Luna for all 765 zero-scored trials. For Terminal-Bench 2.1, we screened 3,738 task-trials across fourteen models (three 89-task runs per model). It distinguishes task-specific lookup attempts, deterministic shortcut evidence, and shortcut cases that still received verifier credit. For SWE-bench Verified, we audited 6,496 mini-SWE-agent trajectories across historical Opus, Gemini, GPT, and GLM releases using GPT-5.6 Luna.