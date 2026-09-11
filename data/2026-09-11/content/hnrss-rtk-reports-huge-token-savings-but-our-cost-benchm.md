---
title: RTK reports huge token savings, but our cost benchmarks disagree - Quesma Blog
url: https://quesma.com/blog/does-rtk-make-ai-coding-cheaper/
site_name: hnrss
content_file: hnrss-rtk-reports-huge-token-savings-but-our-cost-benchm
fetched_at: '2026-09-11T21:35:50.915428'
original_url: https://quesma.com/blog/does-rtk-make-ai-coding-cheaper/
author: Bartosz Kotrys, Jacek Migdal
date: '2026-09-11'
published_date: '2026-09-11T08:00:00.000Z'
description: We tested RTK (Rust Token Killer) with Claude Code on Fable 5.0, and OpenCode with DeepSeek V4 Pro 0813 on Terminal-Bench 2.1.
tags:
- hackernews
- hnrss
---

RTK(Rust Token Killer) filters and compresses terminal output before the AI agent reads it. With over 79k GitHub stars today, RTK is one of the most popular tools to make AI coding cheaper.

One X post sayingRTK could cut Claude Code tokens by up to 60%reached 313K views.

YetJetBrains’s SkillsBench run found no savings. TheREADMEhas a disclaimer:

RTK cuts up to 90% of the bash output your agent reads. […] it is not the same as cutting your bill by 90%.

So “less terminal output” is not the same as “cheaper AI coding”. It can help, be a no-op, or backfire (more turns or lower quality). In this post, we present our findings after several days and over $1,500 spent on tokens.

## How RTK works

RTK can rewrite Git, test, package and file commands the agent runs through its shell tool (Bashin Claude Code,bashin OpenCode). Each rewrite returns a terser version of the same output.

For example, RTK keeps file names, sizes and permissions (644meansrw-r—r—), but drops the owner and date:

$ ls -la /app/warriors

-rw-r--r-- 1 root root 824 Sep 13 2025 g2-clear.red
-rw-r--r-- 1 root root 487 Sep 13 2025 paper.red

$ rtk ls -la warriors/

644 g2-clear.red 824B
644 paper.red 487B

## Testing RTK on Terminal-Bench 2.1

RTK compresses terminal output, so we tested it onTerminal-Bench 2.1, a benchmark with heavy terminal interaction. We stayed on 2.1 rather than the newer3.0and4.0: agents pass most 2.1 tasks, while 3.0 and 4.0 are still a challenge. Cost only matters for tasks that pass.

We ran Claude Code with Fable 5.0, and OpenCode with DeepSeek V4 Pro 0813 through OpenRouter. Each task was scheduled five times without RTK and five times with it, on the same model route, platform and task-specific timeout.

After removing four Fable security tasks that got refusals, the final comparison covers 85 Fable tasks and 89 DeepSeek tasks, or 1,740 attempts.

## The first chart was promising

With RTK, costs fell by 5% for Fable and rose by 5% for DeepSeek.

Download as PNG

Claude Code · Fable 5.0
baseline
$596
$731
(84% pass rate)
RTK
$546
$698
(83% pass rate)
OpenCode · DeepSeek V4 Pro 0813
baseline
$26
$51
(71% pass rate)
RTK
$31
$54
(69% pass rate)
 Passed attempts
 Other attempts

Pass rates were lower with RTK: by 1% for Fable and 2% for DeepSeek. Both pass-rate gaps are small.

When we divided all spending, including failed attempts, by the number of passes, Fable was 3% cheaper with RTK, and DeepSeek was 7% more expensive.

Another way is to weight every task equally, because one expensive task can outweigh many cheap ones. We compared the mean of each task’s baseline attempts with the mean of its RTK attempts, then averaged those changes.

Download as PNG

RTK cost change vs baseline
Claude Code
Fable 5.0
−5%
+1%
OpenCode
DeepSeek V4 Pro 0813
+5%
+17%
-5%
0%
+5%
+10%
+15%
+20%
+25%
+30%
Claude Code
Fable 5.0
−5%
+1%
OpenCode
DeepSeek V4 Pro 0813
+5%
+17%
-5%
0%
+10%
+20%
+30%
Total bill change
Average change per task
95% confidence interval

On this task-level measure, Fable was 1% more expensive, with no clear difference from zero. DeepSeek’s task cost rose17% on average.

Accounting for failures does not change the trend. Across the 36 DeepSeek tasks where all ten attempts passed, the increase was still 18%.

## One task made the difference in the whole benchmark

Almost all of Fable’s savings with RTK came from one task:winning-avg-corewars. Both setups passed every attempt, but with RTK it finished in about half as many turns. Across the other tasks, the savings were less than 1%.

DeepSeek had the reverse result on that same task. Both setups passed every attempt, but RTK took more turns and cost more. Even without that task, costs remained higher with RTK.

## rtk gainis useless as a cost metric

RTK documentsrtk gainas raw minus filtered command output in bytes, divided by 4, not a count of billed tokens.

Across 445 DeepSeek RTK attempts, RTK reported349.2 million tokens saved, a 89% reduction.

Large reported token savings did not mean cheaper tasks.

Download as PNG

rtk gain
Average task-cost change
0%
large-scale-text-editing
57.3M
−19%
crack-7z-hash
38.9M
+28%
other 87 tasks
253.0M
+18%
rtk gain
large-scale-text-editing
57.3M
crack-7z-hash
38.9M
other 87 tasks
253.0M
Average task-cost change
0%
large-scale-text-editing
−19%
crack-7z-hash
+28%
other 87 tasks
+18%

Intrain-fasttext, the model requestedhead -1 train.txttwice. RTK credited 120.5 million tokens saved each time by comparing those limited reads with the whole file. Those two calls accounted for69% of the comparison’s savings counter, although the requested commands would never have returned the whole file.

Treatingrtk gainas money saved assumes the rest of the attempt would stay the same. RTK can change the agent’s next turns.rtk gaindoes not account for the cost of those turns.

This is where social posts go wrong:rtk gaincounts removed output, not money saved, and it can make a more expensive attempt look optimized.

## RTK bugs can bite you

One DeepSeekgit-multibranchattempt got stuck in a loop. The agent ran afindwith a flag thatrtk find0.45.0 did not support. The plugin rewrote it tortk find, which failed with “Usefinddirectly”. Every retry was rewritten again. RTKfixed thisin 0.46.0, after our runs.

Download as PNG

Agent
find
→
Plugin
rtk find
→
Error
Use 
find
 directly
339 consecutive errors
~12 min

The agent accumulated339 consecutive errorsbefore its timeout. It still passed the task, but costabout 9× as muchas the matching baseline attempt, which also passed. One outlier attempt; the trend holds without it.

## Terminal output is a small share of the bill

Without RTK, tool output made up about 11% of Fable’s input tokens and 40% of DeepSeek’s.

Download as PNG

Input without RTK
Fable 5.0
7%
4%
Remaining input
Terminal
 7%
Other tools
 4%
DeepSeek V4 Pro 0813
26%
14%
Remaining input
Terminal
 26%
Other tools
 14%

In the RTK attempts, 31% of Claude Code’s terminal calls and 51% of OpenCode’s terminal calls used RTK.

RTK rewrites only shell commands: its Claude Code hook matches theBashtool and its OpenCode plugin acts onbashcalls. Both platforms expose file reading and searching as separateRead,Grep, andGlobtools, whichbypass RTK. About half of Claude Code’s Bash calls already limited their own output withhead,tail, orwc.

In agentic coding, the context is cached after each turn, so later reads of terminal output mostly show up as cache reads. Those cost 1/10 of regular input tokens for Fable, and 1/30 for DeepSeek.

Download as PNG

Cache reads with RTK
Fable 5.0
DeepSeek V4 Pro 0813
Share of input tokens
94%
98%
Share of total bill
30%
26%

In DeepSeek, RTK reduced terminal-output characters by 9%, yet prompt tokens rose 9%. Uncached input fell 1% and cached input rose 9%. Model output, including reasoning, accounted for 56% of cost with RTK and 57% without it.

## Extra turns can erase the savings

When the agent took more turns, task cost usually rose with it.

Download as PNG

Claude Code · Fable 5.0
Turns, log scale
2
2
5
5
10
10
20
20
50
50
100
100
RTK
baseline
x = y
Cost ($), log scale
0.1
0.1
0.2
0.2
0.5
0.5
1
1
2
2
5
5
10
10
20
20
RTK
baseline
x = y
OpenCode · DeepSeek V4 Pro 0813
Turns, log scale
2
2
5
5
10
10
20
20
50
50
100
100
200
200
RTK
baseline
x = y
Cost ($), log scale
0.01
0.01
0.02
0.02
0.05
0.05
0.1
0.1
0.2
0.2
0.5
0.5
1
1
RTK
baseline
x = y

DeepSeek’s RTK attempts took more turns on 58 tasks, and 44 of them cost more. They took fewer turns on 28, and 23 of them cost less.

The average DeepSeek turn had 7% less input with RTK, but there were 18% more turns overall. Smaller turns did not add up to less total input.

One extra agent turn can cost more than the compression saved. It is the sametokenflationproblem in another form. JetBrains saw the same pattern on SkillsBench: RTK added turns at low effort and did not lower cost at high effort.

## RTK does not make AI coding cheaper

On Terminal-Bench 2.1, Fable’s savings depended on one task and did not hold across tasks. We do not recommend RTK as a generic cost-saving tool.

Individual transcripts show that current frontier models already use the terminal efficiently (just ~7% of Fable’s context was terminal output). Models use techniques likehead -nortail -nthemselves. RTK probably helped more with older models. Today it is a niche optimization, not a source of general savings.

Tested with RTK 0.45.0, Claude Code 2.1.220, OpenCode 1.18.25 and Harbor 0.20. Trajectories availableon requestfor follow-up research.Subscribefor future posts, including our planned benchmark ofHeadroom. Thanks to Piotr Migdał for his review and feedback.

### Knowledge vs wisdom: asking AI “What mushroom is that?”

AI mushroom identification from a photo with ChatGPT, Claude or Google Gemini: GPT-6 Astra, Gemini 3.8 Flash, Claude Fable 5.1, GPT-5.6 and GLM-5.3-Flash. Asked “What mushroom is that?” on 360 photos of poisonous species. Which warn, which get it right, which fail.

HN 

### Claude Code pricing: same tokens, same model, up to 40x the price

Claude Code buyer’s guide, August 2026: what Max, Team, and Enterprise cost, how to get the best deal, and how Uber and Shopify cap the spend.

Featured 

### Tokenflation: When “Hi” triggers 33 tool calls

Tokenflation: simple tasks consuming ever more context, reasoning, and tool calls without more useful output. We benchmarked 14 models; one answered “Hi” with 33 tool calls and an unsolicited commit.