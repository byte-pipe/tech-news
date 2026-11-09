---
title: Our Looping Factory Cut DEV Page Load Time by 75% and Counting - DEV Community
url: https://dev.to/dailycontext/our-looping-factory-cut-dev-page-load-time-by-75-and-counting-1hnf
site_name: devto
content_file: devto-our-looping-factory-cut-dev-page-load-time-by-75-a
fetched_at: '2026-11-10T04:41:18.659831'
original_url: https://dev.to/dailycontext/our-looping-factory-cut-dev-page-load-time-by-75-and-counting-1hnf
author: Ben Halpern
date: '2026-11-09'
description: A month ago, an average web request on DEV took about 70 milliseconds inside Rails, with P99 response... Tagged with ai, agents, automation, architecture.
tags: '#ai, #agents, #automation, #architecture'
---

Drives 75% faster loads using OpenHands automation

A month ago, an average web request onDEVtook about 70 milliseconds inside Rails, with P99 response time coming in at over 1s much of the time. Today, across roughly 300,000 sampled requests a day in Better Stack,that number sits at 16 milliseconds.

Database time per request dropped from 39ms to under 12ms. View rendering fell from 12ms to 2.6ms. Redis time went from 7ms to 1.3ms. Over the last 30 days, we merged 475 pull requests intoForem. This is the type of work that is critical to scale and user experience, but always difficult to prioritize in the face of other progress that needs to happen.

These gains have been massive for user experience. No more intermittent slow downs, or trouble keeping up with high traffic peak times.This has been a solve for a decade's worth of pain.

We have been able to prioritize these performance improvements by designing a feedback loop and stepping away from the day-to-day on this project.

We accomplished this by spinning up a software factory and stepping out of the loop.

There is a trap in the first phase of agentic development that almost everyone hits. You stop typing syntax, which feels like leverage, only to discover you have promoted yourself to human middleware. You become the clipboard between dashboards and a terminal: nudging prompts, babysitting CI flakes, and rubber-stamping diffs all afternoon. You aren’t coding by hand, but you aren’t doing deep engineering either. You are an API endpoint with a pulse.

Getting out of that trap took weeks of building and reconfiguring autonomous loops on top ofOpenHandsand the Agent Client Protocol (ACP). The goal wasn’t just to make DEV faster. It was to separate systematic maintenance from the creative, bespoke projects that deserve human taste.

## Tending the annuals

InDesign for Churn, I argued that codebases are starting to look less like buildings and more like gardens. When writing code was expensive, durability was how you got your money’s worth. When rewriting is cheap, your investment goes into what doesn’t turn over: the soil, the beds, and the irrigation. Put strong contracts, schemas, and tests at the edges, and the code inside can churn continuously without disturbing the roots.

In early October, I did that gardening interactively with agents, shipping 31 PRs that brought average latency from 70ms down to 50ms. The wins were real, but every query audit still required me to start a session, paste context, and shepherd the branch home.

On October 19, we stood up a persistent self-hosted OpenHands hub and turned those habits into closed-loop systems. Since then, 444 pull requests have merged into Forem: 351 from autonomous loops (172performance PRs,93test-suite speedups,32Rust native rewrites,29dependency upgrades,20production error fixes, and5issue-to-PRs) alongside 93 bespoke PRs that I drove directly.

## Every configuration we broke along the way

You don’t get a working software factory from a cron job that says "make the app faster." We went through half a dozen configurations, each born from watching an earlier version fail.

From code reading to live telemetry.Our earliestperf-loopread Ruby files and guessed at bottlenecks, producing micro-optimizations that barely moved a graph. Everything changed when we wired Better Stack’s ClickHouse spans and a read-only Postgres gateway (forem-db-query) into each pre-flight snapshot, wrapped in a privacy guard. Once agents saw live sequential scans, unused indexes, and per-endpoint compute before touching a file, every PR had to justify itself against real traffic.

From one model to a cross-family router.We started pinned to Claude Opus 5.5 (claude-acp), syncing OAuth tokens from macOS Keychain. After hitting quota ceilings and token-refresh collisions, we built a three-provider router across Claude Opus 5.5, OpenAI’scodex-acp(GPT-6.1 Sol), and Google’s Gemini 4 Argon via the Antigravity CLI (agy), first tunneled over a reverse WebSocket to my Mac and then installed natively in Linux at Medium reasoning. Each loop rotates round-robin with an 8-hour cooldown cap, switching model families whenever a PR repair fails.

From shared checkouts to isolated worktrees.Running eight loops in parallel in one container exposed every sharp edge in Git and Linux. Parallel fetches triggeredgit gccollisions, a crashed boot left a stale.gitconfig.lock, and zombie processes piled up until we addedtinias PID 1. We moved every run into a detached-HEAD git worktree with self-healing lock cleanup, and put deterministic Python gates in front of every cron so full queues exit in two seconds with zero tokens spent.

From one loop to specialized beds.As easy SQL wins cleared, we split the work into orthogonal loops on 10-minute daytime ticks (7am-7pm ET, quarter-cadence on weekends) with 5/10/20/40-minute exponential back-off PR check-ins:

* perf-loopfor ActiveRecord queries, Redis caching, and view partials, enforcing category orthogonality across open PRs.
* rust-loopporting hot Ruby paths intogems/forem_nativeviamagnus, gated to one open PR so precompiled binaries never conflict, verified by 1,000-input differential specs.
* test-loopparsing 30 Knapsack RSpec shards to trimFactoryBotchurn and slow system specs.
* error-loopanddeps-loopwith strict filters that skip timeouts, ambiguous bugs, and patch noise.
* github-pr-reviewerandpr-merge-loop, where a second-lens auditor on a different model family checks blast radius and auto-merges low-risk performance and test PRs once CI passes.

## Systematic soil, bespoke fruit

The real payoff isn’t the 475 PR count, or even the 16ms response time. It’s what happened to those other 93 pull requests.

Because I wasn’t spending mornings hunting sequential scans or routing stack traces between tabs, I had headspace for deeper work. While the loops compacted queries and specs, I spent interactive sessions redesigning how our home feed evolves (adding targeting buckets, age diversity weights, and sticky repeat-visit configs), modernizing JavaScript delivery across four phases to shrinkapplication.jsby 71% andbase.jsby 55%, building an L1 local Redis cache, and crafting observability extensions to watch the whole system work.

Tending to this system and working on the high-leverage margins finally feels like a step past the awkward in-between of AI-supported software development as a meat router. The appropriate interplay between brownfield and greenfield projects and the tools for a more productive and creative day at work are here.

Submit

Preview

Dismiss