---
title: 'HERMES.md in git commit messages causes requests to route to extra usage billing instead of plan quota · Issue #53262 · anthropics/claude-code · GitHub'
url: https://github.com/anthropics/claude-code/issues/53262
site_name: hnrss
content_file: hnrss-hermesmd-in-git-commit-messages-causes-requests-to
fetched_at: '2026-04-29T20:09:32.530740'
original_url: https://github.com/anthropics/claude-code/issues/53262
date: '2026-04-29'
description: Summary When a git repository's recent commit history contains the case-sensitive string HERMES.md, Claude Code routes API requests to "extra usage" billing instead of the included Max plan quota. This silently burned through $200 in ext...
tags:
- hackernews
- hnrss
---

anthropics

 

/

claude-code

Public

* NotificationsYou must be signed in to change notification settings
* Fork19.8k
* Star119k

# HERMES.md in git commit messages causes requests to route to extra usage billing instead of plan quota#53262

Closed
Closed
HERMES.md in git commit messages causes requests to route to extra usage billing instead of plan quota
#53262
Labels
area:cost
bug
Something isn't working
Something isn't working
has repro
Has detailed reproduction steps
Has detailed reproduction steps
platform:macos
Issue specifically occurs on macOS
Issue specifically occurs on macOS

## Description

sasha-id
opened 
on 
Apr 25, 2026
Issue body actions

## Summary

When a git repository's recent commit history contains the case-sensitive stringHERMES.md, Claude Code routes API requests to "extra usage" billing instead of the included Max plan quota. This silently burned through $200 in extra usage credits while my Max 20x plan capacity remained largely untouched (13% weekly usage).

## Environment

* Claude Code v2.1.119
* macOS (Apple Silicon)
* Max 20x plan ($200/month)
* Model:claude-opus-4-6[1m](also reproduces withclaude-opus-4-7)

## Reproduction

Minimal reproduction — no project files needed:

#
 This FAILS with "out of extra usage" (routes to extra usage billing)

mkdir /tmp/test-fail 
&&
 
cd
 /tmp/test-fail
git init 
&&
 
echo
 
test
 
>
 test.txt 
&&
 git add 
.
 
&&
 git commit -m 
"
add HERMES.md
"

claude -p 
"
say hello
"
 --model 
"
claude-opus-4-6[1m]
"

#
 => API Error: 400 "You're out of extra usage..."

#
 This WORKS (routes to plan quota)

mkdir /tmp/test-pass 
&&
 
cd
 /tmp/test-pass
git init 
&&
 
echo
 
test
 
>
 test.txt 
&&
 git add 
.
 
&&
 git commit -m 
"
add hermes.md
"

claude -p 
"
say hello
"
 --model 
"
claude-opus-4-6[1m]
"

#
 => "Hello!"

#
 Cleanup

rm -rf /tmp/test-fail /tmp/test-pass

The trigger isthe stringHERMES.mdin git commit messages— not the presence of a file with that name on disk. Claude Code includes recent commits in its system prompt, and something server-side routes the request differently when this string is present.

### What triggers it vs. what doesn't

Commit message

Result

"HERMES.md"

Fails
 — routes to extra usage

"test HERMES.md test"

Fails

"hermes.md"
 (lowercase)

Works

"HERMES"
 (no extension)

Works

"HERMES.txt"

Works

"AGENTS.md"

Works

"README.md"

Works

File named 
HERMES.md
 on disk, clean commit msg

Works

Same repo, orphan branch (no history)

Works

## Impact

* $200.98 in extra usage credits consumedfor requests that should have been covered by the included Max 20x plan quota
* Multiple projects became completely unusable once extra usage was depleted, while the plan dashboard showed 86%+ remaining weekly capacity
* The error message ("out of extra usage") gives no indication that content-based routing is the cause, making this extremely difficult to diagnose
* Any user withHERMES.mdin recent git commits would silently have their usage billed to extra credits

## Expected behavior

API request billing should not depend on the content of git commit messages in the system prompt. All requests from a Max plan subscriber should route to the included plan quota first.

## How I found this

Systematic binary search: cloning affected repos, testing orphan branches, then isolating individual commit message strings untilHERMES.mdwas identified as the exact trigger.

Reactions are currently unavailable

## Metadata

## Metadata