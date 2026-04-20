---
title: Introducing Composer 2 · Cursor
url: https://cursor.com/blog/composer-2
site_name: tldr
content_file: tldr-introducing-composer-2-cursor
fetched_at: '2026-03-22T19:12:58.129822'
original_url: https://cursor.com/blog/composer-2
author: Cursor Team
date: '2026-03-22'
description: Frontier-level coding with strong CursorBench results, higher token efficiency, and a faster default variant.
tags:
- tldr
---

Blog

/

research

Composer 2 is now available in Cursor.

It's frontier-level at coding and priced at $0.50/M input and $2.50/M output tokens, making it a new, optimal combination of intelligence and cost.

## #Frontier-level coding intelligence

We're rapidly improving the quality of our model. Composer 2 delivers large improvements on allbenchmarks we measure, including Terminal-Bench 2.01and SWE-bench Multilingual:

Model
CursorBench
Terminal-Bench 2.0
SWE-bench Multilingual
Composer 2
61.3
61.7
73.7
Composer 1.5
44.2
47.9
65.9
Composer 1
38.0
40.0
56.9

These quality improvements come from our first continued pretraining run, which provides a far stronger base to scale our reinforcement learning.

From this base, we train onlong-horizoncoding tasks throughreinforcement learning. Composer 2 is able to solve challenging tasks requiring hundreds of actions.

## #Try Composer 2

Composer 2 is priced at $0.50/M input and $2.50/M output tokens.

There is also afaster variant with the same intelligenceat $1.50/M input and $7.50/M output tokens, which has a lower cost than other fast models2. We're making fast the default option. See ourmodel docsfor full details.

On individual plans, Composer usage is part of astandalone usage poolwith generous usage included. Try Composer 2 today in Cursor or in the early alpha of ournew interface.

1. Terminal-Bench 2.0 is an agent evaluation benchmark for terminal use maintained by the Laude Institute. Anthropic model scores use the Claude Code harness and OpenAI model scores use the Simple Codex harness. Our Cursor score was computed using the officialHarbor evaluation framework(the designated harness for Terminal-Bench 2.0) with default benchmark settings. We ran 5 iterations per model-agent pair and report the average. More details on the benchmark can be found at the officialTerminal Bench website. For other models besides Composer 2, we took the max score between theofficial leaderboardscore and the score recorded running in our infrastructure.↩
2. Tokens per second (TPS) for all models are from a snapshot of Cursor traffic on March 18th, 2026. Token sizing for Composer and GPT models are similar. Anthropic tokens are ~15% smaller and the TPS number is normalized to reflect that. Similarly, output token price for non-Anthropic models was scaled to match the same ~15% change. Speed may vary depending on provider capacity and improvements over time.↩
