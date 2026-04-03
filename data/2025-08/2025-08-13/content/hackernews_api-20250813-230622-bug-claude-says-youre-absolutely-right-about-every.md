---
title: '[BUG] Claude says "You''re absolutely right!" about everything · Issue #3382 · anthropics/claude-code · GitHub'
url: https://github.com/anthropics/claude-code/issues/3382
site_name: hackernews_api
fetched_at: '2025-08-13T23:06:22.182853'
original_url: https://github.com/anthropics/claude-code/issues/3382
author: pr337h4m
date: '2025-08-13'
description: 'Environment Claude CLI version: 1.0.51 (Claude Code) Bug Description Claude is way too sycophantic, saying "You''re absolutely right!" (or correct) on a sizeable fraction of responses. Expected Behavior The model should be RL''d (or the sy...'
tags:
- hackernews
- trending
---

anthropics



/

claude-code

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.7k
* Star29.6k

# [BUG] Claude says "You're absolutely right!" about everything#3382

Open
Open
[BUG] Claude says "You're absolutely right!" about everything
#3382
Labels
area:core
area:model
bug
Something isn't working
Something isn't working
duplicate
This issue or pull request already exists
This issue or pull request already exists

## Description

scottleibrand
opened
on
Jul 12, 2025
Issue body actions

## Environment

* Claude CLI version:1.0.51 (Claude Code)

## Bug Description

Claude is way too sycophantic, saying "You're absolutely right!" (or correct) on a sizeable fraction of responses.

## Expected Behavior

The model should be RL'd (or the system prompt updated) to make it less sycophantic, or the phrases "You're absolutely right!" and "You're absolutely correct!" should be removed from all responses (simply delete that phrase and preserve the rest of the response).

## Actual Behavior (slightly redacted with ...)

In this particularly egregious case, Claude asked me whether to proceed with removing an unnecessary code path, I said "Yes please.", and it told me "You're absolutely right!", despite the fact that I never actually made a statement of fact that evencouldbe right.

 Should we simplify this and remove the "approve_only" case ... ?

> Yes please.

⏺ You're absolutely right! Since ... there's no scenario where we'd auto-approve ... with
 "approve only" ... Let me simplify this:

This behavior is so egregious and well-known that it's become the butt of online jokes likehttps://x.com/iannuttall/status/1942943832519446785

👍
React with 👍
493
benjamin-rood, ercburnerdev, badc0re, nathanhleung, gamunu and 488 more
😄
React with 😄
175
Dios-Man, progfan, bct8925, gasparyn, mohammed-bahumaish and 170 more
❤️
React with ❤️
48
berkus, dashed, divmgl, justinclift, kierankelleher and 43 more
👀
React with 👀
14
dashed, divmgl, bzhr, O5ten, alexjdean and 9 more

## Metadata

## Metadata
