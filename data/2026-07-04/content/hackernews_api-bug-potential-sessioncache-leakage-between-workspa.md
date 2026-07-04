---
title: '[Bug] Potential session/cache leakage between workspace instances or consumer accounts · Issue #74066 · anthropics/claude-code · GitHub'
url: https://github.com/anthropics/claude-code/issues/74066
site_name: hackernews_api
content_file: hackernews_api-bug-potential-sessioncache-leakage-between-workspa
fetched_at: '2026-07-04T19:31:07.759829'
original_url: https://github.com/anthropics/claude-code/issues/74066
author: chatmasta
date: '2026-07-04'
description: Bug Description Apparent session leakage, despite authenticated to Enterprise ZDR workspace. Agent suddenly started asking me what kind of bricks I wanted for my Minecraft temple and confidently asserted in its recap that it's building a...
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 anthropics

 

/

claude-code

Public

* NotificationsYou must be signed in to change notification settings
* Fork21.9k
* Star136k

# [Bug] Potential session/cache leakage between workspace instances or consumer accounts#74066

Open
Open
[Bug] Potential session/cache leakage between workspace instances or consumer accounts
#74066
Labels
area:core
area:security
bug
Something isn't working
Something isn't working
platform:macos
Issue specifically occurs on macOS
Issue specifically occurs on macOS

## Description

milesrichardson-edb
opened 
on Jul 4, 2026
Issue body actions

Bug DescriptionApparent session leakage, despite authenticated to Enterprise ZDR workspace. Agent suddenly started asking me what kind of bricks I wanted for my Minecraft temple and confidently asserted in its recap that it's building a Minecraft temple. I thought cache was isolated to workspace? Maybe one of my colleagues is building a minecraft temple. That's one way to spend your token allowance, I suppose. Or maybe it's leaking from a consumer plan, in which case this raises some very serious questions about Enterprise ZDR and where some of our sensitive chat sessions might be going.

Environment Info

* Platform: darwin
* Terminal: Apple_Terminal
* Version: 2.1.199
* Feedback ID: f336f5d2-3992-4a04-9e1f-ec30f006f75e

Errors

[]

Maybe relevant: I'm doing something kind of weird. I started this session in a working directory unrelated to the task (because I have a .claude directory in there with context I needed), but it's actually doing all its work in another directory. The "earlier pollution" it referred to is because at some point it compacted its conversation and started working on the project in the directory where I launched the agent (because it forgot my instruction not to touch it). That was less surprising and obviously caused by my own setup. But that's totally different than leaking some Minecraft related prompt into my session.

Reactions are currently unavailable

## Metadata

## Metadata