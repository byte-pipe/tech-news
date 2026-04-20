---
title: '[BUG] Pro Max 5x Quota Exhausted in 1.5 Hours Despite Moderate Usage · Issue #45756 · anthropics/claude-code · GitHub'
url: https://github.com/anthropics/claude-code/issues/45756
site_name: hackernews_api
content_file: hackernews_api-bug-pro-max-5x-quota-exhausted-in-15-hours-despite
fetched_at: '2026-04-12T19:39:29.886148'
original_url: https://github.com/anthropics/claude-code/issues/45756
author: cmaster11
date: '2026-04-12'
description: Preflight Checklist I have searched existing issues and this hasn't been reported yet This is a single bug report (please file separate reports for different bugs) I am using the latest version of Claude Code What's Wrong? Pro Max 5x Quo...
tags:
- hackernews
- trending
---

anthropics



/

claude-code

Public

* NotificationsYou must be signed in to change notification settings
* Fork18.9k
* Star113k

# [BUG] Pro Max 5x Quota Exhausted in 1.5 Hours Despite Moderate Usage#45756

Open
Open
[BUG] Pro Max 5x Quota Exhausted in 1.5 Hours Despite Moderate Usage
#45756
Assignees

Labels
area:cost
bug
Something isn't working
Something isn't working
platform:wsl
Issue specifically occurs on WSL
Issue specifically occurs on WSL

## Description

molu0219
opened
on
Apr 9, 2026
Issue body actions

### Preflight Checklist

* I have searchedexisting issuesand this hasn't been reported yet
* This is a single bug report (please file separate reports for different bugs)
* I am using the latest version of Claude Code

### What's Wrong?

# Pro Max 5x Quota Exhausted in 1.5 Hours Despite Moderate Usage

## Summary

On a Pro Max 5x (Opus) plan, quota resets at a fixed interval. After reset, withmoderate usage(mostly Q&A, light development), quota was exhausted within 1.5 hours. Prior to reset, 5 hours ofheavy development(multi-file implementation, graphify pipeline, multi-agent spawns) consumed the previous quota window— but that was expected given the workload. The post-reset exhaustion was not.

Investigation reveals the likely root cause:cache_read tokens appear to count at full rate against the rate limit, negating the cost benefit of prompt caching for quota purposes.

## Environment

* Plan: Pro Max 5x
* Model: claude-opus-4-6 (1M context)
* Platform: Claude Code CLI on WSL2
* Session: Single continued session with 2 auto-compacts

## Data Collection Method

All data extracted from~/.claude/projects/*//*.jsonlsession files, specifically theusageobject on each API response:

{

"cache_read_input_tokens"
:
...,


"cache_creation_input_tokens"
:
...,


"input_tokens"
:
...,


"output_tokens"
:
...

}

## Measured Token Consumption

### Window 1: 15:00-20:00 (5 hours, heavy development)

Metric

Value

API calls

2,715

Cache read

1,044M tokens

Cache create

16.8M tokens

Input tokens

8.9k tokens

Output tokens

1.15M tokens

Peak context

966,078 tokens

Effective input (cache_read at 1/10)

121.8M tokens

Workload: Full feature implementation (Express server + iOS app), graphify knowledge graph pipeline, SPEC-driven multi-agent coordination. 2 auto-compacts as context hit ~960k.

### Window 2: 20:00-21:30 (1.5 hours, moderate usage)

Main session (vibehq):

Metric

Value

API calls

222

Cache read

23.2M tokens

Cache create

1.4M tokens

Input tokens

304 tokens

Output tokens

91k tokens

Peak context

182,302 tokens

Effective input (cache_read at 1/10)

2.8M tokens

Other sessions running (background, not actively used by user):

Session

API Calls

Cache Read

Eff Input

Output

token-analysis

296

57.6M

6.5M

145k

career-ops

173

23.1M

3.8M

148k

Total (all sessions)

691

103.9M

13.1M

387k

## The Problem

### If cache_read counts at 1/10 rate (expected):

Window 2 total: 13.1M effective tokens in 1.5 hours = 8.7M/hr

This should NOT exhaust a Pro Max 5x quota.For comparison, Window 1 consumed 24.4M effective tokens/hour during heavy development and used the previous quota window — but that was 2.8x more intense.

### If cache_read counts at full rate (suspected actual behavior):

Window 2 total: 103.9M + 1.4M + 387k = 105.7M tokens in 1.5 hours = 70.5M/hr

This would explain quota exhaustion, but meansprompt caching provides zero benefit for rate limiting.

## Context Size Progression

The session file shows context growing and compacting cyclically:

Segment 1: 32k → 783k (835 calls) → auto-compact
Segment 2: 39k → 966k (1,842 calls) → auto-compact
Segment 3: 55k → 182k (222 calls) → still active

Each API call sends thefull contextas input. With a 1M context window, calls near the compact threshold send ~960k tokens each. Even with prompt caching, if cache_read counts at full rate against quota, a single call costs ~960k quota tokens.

## Specific Issues

### 1. Cache read token accounting against rate limits

Expected: cache_read tokens should count at reduced rate (1/10) against rate limits, matching the reduced cost.

Observed: Quota exhaustion rate is consistent with cache_read counting at full rate.

Impact: On a 1M context window, each API call sends ~100-960k tokens. With 200+ calls per hour (normal for tool-heavy Claude Code usage), quota depletes in minutes regardless of caching.

### 2. Background sessions consume shared quota

Sessions left open in other terminals continue making API calls (compacts, retros, hook processing) even when the user is not actively interacting. These consume from the same quota pool.

In this case,token-analysis(296 calls) andcareer-ops(173 calls) were running without active user interaction but still consuming significant quota.

### 3. Auto-compact creates expensive spikes

Each auto-compact event results in one API call with thefull pre-compact context(~966k tokens) as cache_creation, followed by a fresh start. This means the most expensive single call happens automatically, without user action.

### 4. 1M context window amplifies the problem

Larger context window = more tokens per call = faster quota depletion. The 1M window is marketed as a feature but becomes counterproductive when cache_read tokens count at full rate against quota.

## Reproduction

1. Start Claude Code with Opus on Pro Max 5x
2. Have~/.claude/rules/with ~30 rule files (~19k tokens fixed overhead)
3. Work on a project with tool-heavy operations (file reads, builds, tests)
4. Observe context growing via/contextcommand
5. After 200-300 tool calls, check quota — it will be significantly depleted
6. Leave 2-3 other Claude Code sessions open in other terminals
7. After quota reset, observe quota depleting even with minimal active usage

## Expected Behavior

* cache_read tokens should count at their reduced rate (1/10) against rate limits
* Background/idle sessions should not consume significant quota
* Auto-compact should not create outsized quota spikes
* Pro Max 5x should sustain at least 2-3 hours of moderate Opus usage per quota window

## Actual Behavior

* Quota exhausted in 1.5 hours with moderate usage (8.7M effective tokens/hour)
* Background sessions consumed 78% of post-reset quota
* Total raw tokens sent (105.7M) is consistent with cache_read counting at full rate

## Suggested Improvements

1. Clarify cache_read quota accounting: Document whether cache_read tokens count at full or reduced rate against rate limits
2. Rate limit by effective tokens: Count cache_read at 1/10 rate for rate limiting, matching the cost reduction
3. Session idle detection: Don't count idle session overhead against quota, or warn users about open sessions
4. Quota visibility: Show real-time token consumption breakdown in Claude Code (cache_read vs cache_create vs input vs output)
5. Context-aware quota estimates: Before operations, estimate quota cost based on current context size

### What Should Happen?

The token usage cannot be consumed at this speed.

### Error Messages/Logs

### Steps to Reproduce

It's hard to reproduct but I can provdie the log.

### Claude Model

None

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

No response

### Claude Code Version

v2.1.97

### Platform

Anthropic API

### Operating System

Ubuntu/Debian Linux

### Terminal/Shell

WSL (Windows Subsystem for Linux)

### Additional Information

No response

Reactions are currently unavailable
Pinned by

bcherny
Pinned comment options
bcherny
on
Apr 12, 2026

Hey all, Boris from the Claude Code team here.We've been investigating these reports, and a few of the top issues we've found are:Prompt cache misses when using 1M token context window are expensive. Since Claude Code uses a 1 hour prompt cache window for the main agent, if you leave your computer for over an hour then continue a stale session, it's often a full cache miss. To improve this, we have shipped a few UX improvements (eg. to nudge you to /clear before continuing a long stale session), and are investigating defaulting to 400k context instead, with an option to configure your context window to up to 1M if preferred. To experiment with this now, try:CLAUDE_CODE_AUTO_COMPACT_WI…

View full comment

## Metadata

## Metadata
