---
title: 'Cache TTL silently regressed from 1h to 5m around early March 2026, causing quota and cost inflation · Issue #46829 · anthropics/claude-code · GitHub'
url: https://github.com/anthropics/claude-code/issues/46829
site_name: hackernews_api
content_file: hackernews_api-cache-ttl-silently-regressed-from-1h-to-5m-around
fetched_at: '2026-04-12T19:39:31.182831'
original_url: https://github.com/anthropics/claude-code/issues/46829
author: lsdmtme
date: '2026-04-12'
description: Cache TTL appears to have silently regressed from 1h to 5m around early March 2026, causing significant quota and cost inflation Summary Analysis of raw Claude Code session JSONL files spanning Jan 11 – Apr 11, 2026 shows that Anthropic ...
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

# Cache TTL silently regressed from 1h to 5m around early March 2026, causing quota and cost inflation#46829

Closed as not planned
Closed as not planned
Cache TTL silently regressed from 1h to 5m around early March 2026, causing quota and cost inflation
#46829
Assignees
 
Labels
api:anthropic
area:cost
bug
Something isn't working
Something isn't working
has repro
Has detailed reproduction steps
Has detailed reproduction steps

## Description

seanGSISG
opened 
on 
Apr 12, 2026
Issue body actions

# Cache TTL appears to have silently regressed from 1h to 5m around early March 2026, causing significant quota and cost inflation

## Summary

Analysis of raw Claude Code session JSONL files spanning Jan 11 – Apr 11, 2026 shows that Anthropic appears to havesilently changed the prompt cache TTL default from 1 hour to 5 minutes sometime in early March 2026. Prior to this change, Claude Code was receiving 1-hour TTL cache writes — which we believe was the intended default. The reversion to 5-minute TTL has caused a20–32% increase in cache creation costsand a measurable spike in quota consumption for subscription users who have never previously hit their limits.

This appears directly related to the behavior described in#45756.

## Data

Session data extracted from~/.claude/projects/JSONL files acrosstwo machines(Linux workstation + Windows laptop, different accounts/sessions), totaling119,866 API callsfrom Jan 11 – Apr 11, 2026. Each assistant message includes ausage.cache_creation.ephemeral_5m_input_tokens/ephemeral_1h_input_tokensbreakdown that makes the TTL tier per-call observable. Having two independent machines strengthens the signal — both show the same behavioral shift at the same dates.

### Phase breakdown

Phase

Dates

TTL behavior

Evidence

1

Jan 11 – Jan 31

5m ONLY

ephemeral_1h
 absent/zero — likely predates 1h tier availability in the API

2

Feb 1 – Mar 5

1h ONLY

ephemeral_5m = 0
, 
ephemeral_1h > 0
 across 
33+ consecutive days
 on both machines — near-zero exceptions

3

Mar 6–7

Transition

First 5m tokens re-appear, small volumes, 1h still present

4

Mar 8 – Apr 11

5m dominant

5m tokens surge to majority; 1h becomes minority or disappears entirely

We believe Phase 2 represents Anthropic'sintended default behavior— 1h TTL was rolled out as the Claude Code standard around Feb 1 and held consistently for over a month across two independent machines on two different accounts. January's all-5m data most likely predates the 1h TTL tier being available in the API. The regression beganaround March 6–8, 2026.

No client-side changes were made between phases. The same Claude Code version and usage patterns were in place throughout. The TTL tier is set server-side by Anthropic.

### Day-by-day TTL data showing the regression (combined, both machines)

Date | 5m-create | 1h-create | Behavior
------------|------------|------------|----------
2026-02-01 | 0.00M | 1.70M | 1h ONLY ← 1h default begins
2026-02-09 | 0.00M | 7.95M | 1h ONLY
2026-02-15 | 0.00M | 13.61M | 1h ONLY ← heaviest day, 100% 1h
2026-02-28 | 0.00M | 16.15M | 1h ONLY ← 16M tokens, still 100% 1h
2026-03-01 | 0.00M | 0.12M | 1h ONLY
2026-03-04 | 0.00M | 8.12M | 1h ONLY
2026-03-05 | 0.00M | 6.55M | 1h ONLY ← last clean 1h-only day
 | | |
2026-03-06 | 0.29M | 0.22M | MIXED ← first 5m tokens reappear
2026-03-07 | 4.56M | 0.50M | MIXED ← 5m surging
2026-03-08 | 16.86M | 3.44M | MIXED ← 5m now dominant (83%)
2026-03-10 | 10.55M | 0.51M | MIXED
2026-03-15 | 19.47M | 1.84M | MIXED
2026-03-21 | 21.37M | 1.70M | MIXED ← 93% 5m
2026-03-22 | 13.48M | 2.85M | MIXED

The transition is visible to the day:March 6 is when 5m tokens first reappearafter 33 days of clean 1h-only behavior. By March 8, 5m tokens outnumber 1h by 5:1. This is consistent with a server-side configuration change being rolled out gradually then completing around March 8.

## Cost impact

Applying official Anthropic pricing (rates.json, updated 2026-04-09):

Combined dataset (119,866 API calls, two machines):

claude-sonnet-4-6(cache_write_5m = $3.75/MTok,cache_write_1h = $6.00/MTok,cache_read = $0.30/MTok):

Month

Calls

Actual cost

Cost with 1h TTL

Overpaid

% waste

Jan 2026

2,639

$78.99

$37.54

$41.45

52.5%

Feb 2026

27,220

$1,120.43

$1,108.11

$12.32

1.1%
 ← nearly 0 on 1h

Mar 2026

68,264

$2,776.11

$2,057.01

$719.09

25.9%

Apr 2026

21,743

$1,193.01

$1,016.78

$176.23

14.8%

Total

119,866

$5,561.17

$4,612.09

$949.08

17.1%

claude-opus-4-6(cache_write_5m = $6.25/MTok,cache_write_1h = $10.00/MTok,cache_read = $0.50/MTok):

Month

Calls

Actual cost

Cost with 1h TTL

Overpaid

% waste

Jan 2026

2,639

$131.65

$62.57

$69.08

52.5%

Feb 2026

27,220

$1,867.38

$1,846.85

$20.53

1.1%
 ← nearly 0 on 1h

Mar 2026

68,264

$4,626.84

$3,428.36

$1,198.49

25.9%

Apr 2026

21,743

$1,988.35

$1,694.64

$293.71

14.8%

Total

119,866

$9,268.97

$7,687.17

$1,581.80

17.1%

February — the month Anthropic was defaulting to 1h TTL — shows only1.1% waste(trace 5m activity from one machine on one day). Every other month shows 15–53% overpayment from 5m cache re-creations. The cost difference is explained entirely by TTL tier, not by usage volume. Thepercentage waste is identical across model tiers(17.1%) because it is driven purely by the 5m/1h token split, not by per-token price.

### Why 5m TTL is so expensive in practice

With 5m TTL, any pause in a session longer than 5 minutes causes the entire cached context to expire. On the next turn, Claude Code must re-upload that context as a freshcache_creationat the write rate, rather than acache_readat the read rate. The write rate is12.5× more expensivethan the read rate for Sonnet, and the same ratio holds for Opus.

For long coding sessions — which are the primary Claude Code use case — this creates a compounding penalty: the longer and more complex your session, the more context you have cached, and the more expensive each cache expiry becomes.

Over the 3-month period analyzed:

* 220M tokenswere written to the 5m tier
* Those same tokens generated5.7B cache reads— meaning they were actively being used
* Had those 220M tokens been on the 1h tier, re-accesses within the same hour would be reads ($0.30–0.50/MTok) instead of re-creations ($3.75–6.25/MTok)

## Quota impact

Users on Pro/subscription plans are quota-limited, not just cost-limited. Cache creation tokens count toward quota at full rate; cache reads are significantly cheaper (the exact coefficient is under investigation in#45756). The silent reversion to 5m TTL in March is the most likely explanation for why subscription users began hitting their 5-hour quota limits for the first time — including the author of this issue, who had never hit quota limits before March 2026.

## Hypothesis

The data strongly suggests that1h TTL was the intended default for Claude Codeand was in place as of early February 2026. Sometime between Feb 27 and Mar 8, 2026, Anthropic silently changed the default to 5m TTL — either intentionally as a cost-saving measure, or accidentally as an infrastructure regression.

Evidence supporting "1h was the intended default":

* Phase 2 (1h ONLY) showszero5m tokens across14 separate active daysspanning 3+ weeks — this is not noise or partial rollout, it is consistent deliberate behavior
* The February cost profile is the only month with 0% overpayment — it represents what users should have been paying all along
* The March reversion immediately produced the largest 5m-tier days in the entire dataset (30M tokens on Mar 22 alone), suggesting a sudden configuration flip rather than gradual drift
* Subscription users began hitting 5-hour quota limitsfor the first timein March — directly coinciding with the reversion

The most likely sequence of events:

1. ~Feb 1 and prior: Anthropic defaulted to 1h TTL for Claude Code subscription users
2. ~Mar 6: 5m tokens begin reappearing — gradual rollout of the change or partial infrastructure flip
3. ~Mar 8: 5m TTL becomes dominant — the regression is fully in effect across both tested machines and accounts
4. Mar 8+: Mixed behavior continues, suggesting either incomplete rollout, A/B testing, or regional infrastructure variance

The 33-day window of clean 1h-only behavior (Feb 1 – Mar 5) across two independent machines and two separate accounts makes this one of the strongest available signals that1h TTL was Anthropic's deliberate default, not a fluke.

## Request

1. Confirm or denywhether Anthropic made a server-side TTL default change in early February 2026 and reverted it in early March 2026
2. Clarify the intended TTL behaviorfor claude-code sessions — is 5m the intended default, or was 1h intended to be permanent?
3. Consider restoring 1h TTL as the defaultfor Claude Code sessions, or exposing it as a user-configurable option. The 5m TTL is disproportionately punishing for the long-session, high-context use case that defines Claude Code usage
4. Disclose quota counting behavior for cache_read tokens(ref[BUG] Pro Max 5x Quota Exhausted in 1.5 Hours Despite Moderate Usage#45756) so users can make informed decisions about their usage patterns

## Methodology

* Source: raw~/.claude/projects/**/*.jsonlsession files (Claude Code stores per-message API responses including fullusageobjects)
* Extraction: filtered fortype: "assistant"entries withmessage.usage.cache_creationfield
* No external tools or proxies involved — this data comes directly from Claude Code's own session logs
* Analysis tool:cnighswonger/claude-code-cache-fixquota-analysis --sourcemode (added to support this investigation)
* Pricing: official Anthropic rates fromrates.json(updated 2026-04-09)
Reactions are currently unavailable

## Metadata

## Metadata