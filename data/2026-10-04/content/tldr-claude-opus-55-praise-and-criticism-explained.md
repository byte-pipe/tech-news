---
title: 'Claude Opus 5.5: Praise and Criticism Explained'
url: https://verityadaily.com/claude-opus-5-5-draws-praise-and-criticism-for-high-effort-r-2026
site_name: tldr
content_file: tldr-claude-opus-55-praise-and-criticism-explained
fetched_at: '2026-10-04T15:40:46.993831'
original_url: https://verityadaily.com/claude-opus-5-5-draws-praise-and-criticism-for-high-effort-r-2026
date: '2026-10-04'
published_date: '2026-10-03T13:08:23+05:30'
description: See why Claude Opus 5.5 earns praise and criticism for high-effort reasoning, with key strengths and concerns. Read the analysis.
tags:
- tldr
---

AI

October 3, 2026

# Claude Opus 5.5 Draws Praise—and Criticism—for High-Effort Reasoning

Set Claude Opus 5.5 to its default effort and you get a strong model. Set it to maximum and, by several of Anthropic's own numbers, you get a better one that thinks longer, answers slower and costs more per turn. That gap explains why the September 22, 2026 launch is drawing both praise and criticism. Praise goes to its long-horizon coding and to Anthropic's claim of lower cost per finished task. Criticism targets headline benchmarks run at the highest compute settings, harder budgeting, and migration work that teams moving off Opus 5 did not expect.

## The short version

Opus 5.5 looks like the most capable agentic model Anthropic has shipped, and its pricing undercuts Opus 5. Its best scores, though, measure how much inference compute you are willing to buy. Teams should judge it on cost and quality per completed task at the effort level they will run in production, not on the launch-day leaderboard.

## Why the conversation spiked this month

Timing matters. Anthropic released Opus 5.5 on September 22 and then shipped Sonnet 5.5 six days later as the faster, cheaper companion. That gave developers two new models to compare inside one week. Almost all the evidence so far comes from Anthropic, its early-access testers and fresh benchmark runs. No long-term independent studies exist yet.

The headline numbers are strong. Anthropic puts Opus 5.5 at 66.4% on Terminal-Bench 4.0, ahead of Fable 5.1 at 55.8% and Opus 5 at 52.3%, but that run used xhigh effort. When I read launch tables for Veritya Daily, the first column I look for is the effort setting, and here it changes how you read the results.

Benchmark

Opus 5.5 score

Effort setting

Default-effort score

Terminal-Bench 4.0

66.4%

xhigh

Not published

FrontierCode v1.1

54.4%

Maximum

54.6%

CursorBench 4.0

57.8%

Maximum

52.5%

OSWorld 2.1

81.8%

Headline config (generally maximum)

Not published

Chartography (with tools)

89.0%

Headline config (generally maximum)

Not published

GDPval-AA v2.1

1,846 Elo

Headline config

Not published

All figures are Anthropic-reported. The GDPval-AA result, which spans professional work across 44 occupations, comes from Artificial Analysis as cited by Anthropic. OurAI benchmark guideexplains how to read tables like this one.

## Driver one: cost per completed task

The pricing case is the most concrete part of the pitch. Standard API rates are $4 per million input tokens and $20 per million output, according to theOpus 5.5 platform documentation. That is a fifth cheaper than Opus 5's $5 and $25, and cache reads fall 60%, to 20 cents. Batch jobs run at half the regular rate. Fast Mode doubles the price to $8 and $40 in exchange for up to 2.5 times the speed.

Token prices are only half of the argument. Anthropic estimates a typical workload costs about 40% less than on Opus 5, because the model also uses fewer tokens per task. I call thisfinished-job pricing: the unit that matters is dollars per merged pull request or completed audit, not dollars per million tokens. One early tester's workflow reportedly made about 40% fewer calls and burned roughly half the tokens Opus 5 needed.

The catch sits in the same documentation. At xhigh and maximum effort, Opus 5.5 may think more per turn than Opus 5 did, so per-turn bills can rise even if per-task bills fall.

## Driver two: long-running agentic work

Anthropic is not positioning Opus 5.5 for quick question-and-answer use. It targets codebase migrations, audits and multi-step business workflows with repeated tool calls, supported by a 1-million-token context window and 128,000 output tokens (300,000 through the beta Batch API).

The tester anecdotes are dramatic. One reported auditing and fixing a 200,000-line codebase in under three hours, against more than 20 hours and 2.5 times the tokens on Opus 5. Another described finishing a 680,000-line migration in under a day. Anthropic's own HAProxy C-to-Rust rewrite took 9.5 hours, versus 12 for Fable 5.1, at 51% lower cost. These are vendor-published cases, not controlled trials. Read them as signals of direction, not as proof.

## The criticism: the effort-dial gap

The main objection is what I call the effort-dial gap: the distance between what Opus 5.5 scores when it is given maximum compute and what a typical user sees at the default medium setting. On CursorBench that gap is 5.3 points. On FrontierCode the default run scored slightly higher than the maximum run, which suggests extra reasoning does not always help.

Default performance still holds up. At default effort, Anthropic reports Opus 5.5 at 52.5% on CursorBench against 41.7% for GPT-5.6 Sol. For context on that rival, see our coverage ofGrok 4.6 and GPT-5.6 Sol.

Two more complications matter. First, Anthropic ran its evaluations with production safeguards switched on. When those safeguards intervened, some cybersecurity tasks were completed by Opus 4.8, and some biology and frontier-model-development tasks were completed by Opus 5. That makes direct comparisons with other labs harder. Second, migration is not plug-and-play.

Warning:Moving from Opus 5 can break existing integrations. Thinking cannot be disabled, forced tool use returns an error, and the older computer_20251124 tool is not accepted on the Claude API or Google Cloud. Text between tool calls may also land in thinking blocks rather than text blocks, and the model can refuse prompts that try to extract its internal reasoning.

## What developers are saying

Sentiment is enthusiastic but specific. On r/ClaudeCode, developers describe building nonstop in Claude Code since the release. On r/claude, users comparing medium and maximum effort report a large quality difference between the two, which supports the effort-dial critique from the user side.

Workflows on X show a pattern. Builders use Opus 5.5 for implementation, then bring in another frontier model for planning or review. Others run subagents in parallel to check design and code quality before consolidating one fix. On r/ClaudeAI, people show off overnight creative and production runs. These are impressive, but they are demos, not evaluations. Skeptics' strongest point comes from Anthropic's own tables, and Sonnet 5.5 sharpens it: Anthropic reports 70.6% on Terminal-Bench 4.0 for Sonnet 5.5 against 10.3% for Sonnet 5, a jump the company itself says needs matched test conditions before anyone draws firm conclusions.

## What this means for finance and tech teams

Pilot Opus 5.5 on one real, long task at medium effort, then rerun it at high effort and compare total cost, wall-clock time and review hours. Escalate effort only where it measurably cuts rework. Default to Sonnet 5.5 for short, high-volume calls. That split will save more money than any per-token discount.

Budget controls already exist. Anthropic added usage analytics, model-level entitlements and spend alerts for enterprises on July 2, 2026,per its admin announcement. Use them before anyone sets a team default to maximum. Individuals can test cheaply: Pro costs $20 a month, and Max costs $100 or $200 for 5x or 20x usage, according toClaude's pricing page. For a broader vendor view, ourGPT, Claude and Gemini comparison for product teamscovers the trade-offs.

Tip:Track one number per pilot: cost per accepted output. It folds in retries, latency and human review, which per-token pricing hides.

## Forecast through Q1 2027

These are my expectations, not reported facts. By the end of December 2026, independent replications of Terminal-Bench and CursorBench should show whether the default-effort numbers hold outside Anthropic's harness. I expect rivals to publish their own effort-tiered scores, which will make "at what setting?" the standard question for every launch. The longer-term test for Opus 5.5 is whether enterprises keep it on high effort after a full quarter of invoices, and the spend-alert data will show that before any benchmark does. We will track those replications in The Daily Brief and in ourClaude news guide.

## Related Reading

* Grok 4.7 and Claude Opus 5.5 Intensify September’s AI Release Rush
* 7 Ways AI Model Slowdowns Could Affect Investors and Developers
* How to Evaluate AI Tools Without Being Misled by Demos
* Why AI Model Releases Feel Nonstop as Providers Shorten Launch Cycles
* Alternatives: AI Release Tracker Alternatives: 9 Options Compared
* AI Tools vs Traditional Software: Which Is Better for Measurable ROI?
* Latest AI Technology News: Breakthroughs, Releases, and Business Impact
* How-To: How to Compare AI Model Release Pace (Step-by-Step)
* Veritya Daily — AI, Crypto, Finance & Tech News
* 8th Pay Commission Verdict Tracker: What Is Confirmed vs Pending — September 2026

The Daily BriefA daily email newsletter delivering the day's trending technology, cryptocurrency, and finance news every morning.

Explore The Daily Brief

Stay ahead.
 For daily AI, crypto, finance & tech coverage you can trust, 
Veritya Daily
 has you covered.