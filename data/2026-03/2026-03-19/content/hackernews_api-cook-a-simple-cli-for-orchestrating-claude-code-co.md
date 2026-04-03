---
title: cook — A simple CLI for orchestrating Claude Code, Codex, and OpenCode
url: https://rjcorwin.github.io/cook/
site_name: hackernews_api
content_file: hackernews_api-cook-a-simple-cli-for-orchestrating-claude-code-co
fetched_at: '2026-03-19T19:23:28.661667'
original_url: https://rjcorwin.github.io/cook/
author: staticvar
date: '2026-03-19'
description: 'Cook: A simple CLI for orchestrating Claude Code'
tags:
- hackernews
- trending
---

## * Primitives

Cook parses three categories of tokens:

#### * Work

A prompt. One agent call. The core unit.

#### * Loop operators

Wrap work with iteration:xN,review,ralph.

#### * Composition

Run parallel branches and resolve:vN,vs,pick.

Operators compose left to right. Each wraps everything to its left.

cook 
"work"
 x3 review 
# (work×3) → review loop

cook 
"work"
 review x3 
# (work → review loop) × 3

cook 
"work"
 review v3 pick 
# race 3, each with a review loop

## * Loop Operators

### repeat (xN)

xNruns work N times sequentially, each pass seeing the previous output.

cook 
"Add dark mode"
 x3 
# 3 sequential passes

cook 
"Add dark mode"
 repeat 3 
# long-form

cook 
"Add dark mode"
 x3 review 
# 3 passes, then a review loop

cook 
"Add dark mode"
 review x3 
# review loop repeated 3 times

### review

reviewadds a review→gate loop. After work, a reviewer checks quality and a gate decides DONE or ITERATE. On ITERATE, the iterate step runs, then review→gate repeats.

work

->

review

->

gate

->

iterate

<<

cook 
"Add dark mode"
 review 
# default prompts, up to 3 iterations

cook 
"Add dark mode"
 review 5 
# up to 5 iterations

Provide custom prompts afterreview, or use positional shorthand:

# Explicit

cook 
"Add dark mode"
 review \
 
"Review for accessibility"
 \
 
"DONE if WCAG AA, else ITERATE"

# Shorthand — same result

cook 
"Add dark mode"
 \
 
"Review for accessibility"
 \
 
"DONE if WCAG AA, else ITERATE"

# With iterate prompt and max-iterations

cook 
"Add dark mode"
 \
 
"Review for accessibility"
 \
 
"DONE if WCAG AA, else ITERATE"
 \
 
"Fix the issues"
 5

Use different agents or models per step:

cook 
"Add dark mode"
 review \
 --work-agent codex --work-model gpt-5-codex \
 --review-agent claude --review-model opus

### ralph

Ralph wraps a cook with an outer gate for task-list progression. The work prompt is self-directing — it reads project state to find the current task each time.

cook 
"Work on next task in plan.md"
 \
 ralph 5 
"DONE if all tasks complete, else NEXT"

# review gate per task, then ralph advances

cook 
"Work on next task in plan.md"
 \
 review 
"Code review"
 
"DONE if no High issues, else ITERATE"
 \
 ralph 5 
"DONE if all tasks complete, else NEXT"

The review gate decidesDONE(pass to ralph) orITERATE(fix and retry). The ralph gate decidesDONE(exit) orNEXT(advance to next task, reset iterations).

## * Composition Operators

Composition operators run multiple cooks in parallel isolated git worktrees, then combine the results with a resolver.

### versions (vN / race N)

vNruns N identical cooks in parallel worktrees.pickis the default resolver.

cook 
"Add dark mode"
 v3 
# 3 runs, pick the best

cook 
"Add dark mode"
 v3 
"least code wins"
 
# with pick criteria

cook 
"Add dark mode"
 race 3 
"least code wins"
 
# long-form alias

cook 
"Add dark mode"
 review v3 
"cleanest"
 
# race 3, each with a review loop

cook 
"Add dark mode"
 x3 v3 
"most complete"
 
# race 3, each with 3 passes

### vs

vsruns two different cooks in parallel worktrees. Each branch is a full cook — it can have its own loop operators.

cook 
"Implement auth with JWT"
 \
 vs \
 
"Implement auth with sessions"
 \
 pick 
"best security"

cook 
"Build with React"
 review 
"Check accessibility"
 
"DONE if WCAG AA"
 3 \
 vs \
 
"Build with Vue"
 review 
"Check bundle size"
 
"DONE if under 50kb"
 5 \
 merge 
"best developer experience"

### Resolvers

Resolver

Behavior

pick ["criteria"]

Pick one winner. Merge that branch. Default.

merge ["criteria"]

Synthesize all results into a fresh implementation.

compare

Write a comparison doc to 
.cook/compare-<session>.md
. No merge.

## * Configuration

Runcook initin your project root to scaffold configuration files:

cook init

This creates:

* COOK.md— project instructions and agent prompt template
* .cook/config.json— agent/model/sandbox defaults and per-step overrides
* .cook/Dockerfile— project dependencies for Docker sandbox mode
* .cook/logs/— session logs (gitignored)

Example.cook/config.json:

{
 "agent": "claude",
 "sandbox": "agent",
 "steps": {
 "work": { "agent": "codex", "model": "gpt-5-codex" },
 "review": { "agent": "claude", "model": "opus" }
 },
 "env": ["CLAUDE_CODE_OAUTH_TOKEN"]
}

### Sandbox Modes

Mode

Flag

Description

Agent
 (default)

--sandbox agent

Agents use their own OS-level sandboxes. No Docker required.

Docker

--sandbox docker

Agents run in a Docker container with restricted network access.

Note:OpenCode is only supported in Docker mode.

### Rate-limit recovery

When an agent hits a token quota or rate limit, cook automatically waits and retries instead of bailing. A countdown is shown in the TUI. Enabled by default.

cook 
"Build the feature"
 review --no-wait 
# disable: fail fast

Configure wait behavior in.cook/config.json:

{
 "retry": {
 "enabled": true,
 "pollIntervalMinutes": 5,
 "maxWaitMinutes": 360
 }
}