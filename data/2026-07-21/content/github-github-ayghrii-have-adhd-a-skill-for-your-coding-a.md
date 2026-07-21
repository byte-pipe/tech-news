---
title: 'GitHub - ayghri/i-have-adhd: A skill for your coding agent to stop it from burying the answer. ADHD-friendly output. · GitHub'
url: https://github.com/ayghri/i-have-adhd
site_name: github
content_file: github-github-ayghrii-have-adhd-a-skill-for-your-coding-a
fetched_at: '2026-07-21T19:33:15.469323'
original_url: https://github.com/ayghri/i-have-adhd
author: ayghri
description: A skill for your coding agent to stop it from burying the answer. ADHD-friendly output. - ayghri/i-have-adhd
---

ayghri

 

/

i-have-adhd

Public

* NotificationsYou must be signed in to change notification settings
* Fork266
* Star6.6k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

34 Commits
34 Commits
.agents/
plugins
.agents/
plugins
 
 
.claude-plugin
.claude-plugin
 
 
.codex-plugin
.codex-plugin
 
 
.github/
workflows
.github/
workflows
 
 
skills/
i-have-adhd
skills/
i-have-adhd
 
 
INSTALL.md
INSTALL.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
logo.png
logo.png
 
 
plugin.json
plugin.json
 
 
View all files

## Repository files navigation

ADHD-friendly outputs. No ADHD diagnosis needed!

## Install

Claude Code

claude plugin marketplace add ayghri/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd

Then type/i-have-adhd. No local clone needed — Claude Code fetches the repo and keeps it updated.

Codex

codex plugin marketplace add ayghri/i-have-adhd --ref main
codex plugin add i-have-adhd@i-have-adhd

Then type$i-have-adhdto apply the output style explicitly. The skill can also be invoked implicitly when Codex sees a task that benefits from it.

Install instructions for other coding agents live inINSTALL.md.

## What it does

A skill for your coding assistant that stops it from burying the answer. Action first. Steps numbered. No "Hope this helps!"

## What changes

## Before

Great question! Let me think about this. Your auth flow has a few moving pieces: the middleware, the token verification, and the cookie handling. Looking atsrc/auth.ts, theverifyTokenfunction (around lines 42-58) seems to be using an olderjsonwebtokenAPI. One approach would be to update the package and rewrite that function. After making the change, you'd want to run the auth tests to confirm nothing breaks. By the way, you might also want to look at your dependency versions overall. Hope this helps! Let me know if you want to dig deeper.

## After

Runnpm install jsonwebtoken@latest, then editsrc/auth.ts:42.

1. Opensrc/auth.ts
2. ReplaceverifyToken(lines 42–58) with the snippet below
3. Runnpm test -- auth.spec.ts

Next: paste the first failing line if any test fails.

## The rules

10 rules. Full text inSKILL.md.

1. Lead with the next action.
2. Number multi-step tasks.
3. End with one concrete next step.
4. Suppress tangents.
5. Restate state every turn.
6. Specific time estimates (minutes, not "a bit").
7. Make wins visible.
8. Matter-of-fact errors.
9. Cap lists at 5 items.
10. No preamble. No recap. No closers.

## Tune it

Fork, editskills/i-have-adhd/SKILL.md, install your fork:claude plugin marketplace add <your-username>/i-have-adhd. Re-invoke/i-have-adhd.

## Credits

Loosely based onThe Adult ADHD Tool Kitby J. Russell Ramsay and Anthony L. Rostain. Adapted for how an LLM should respond, not how a human should organize their day.

## License

MIT.

Star ⭐ if it saved you one scroll past one "Great question!"

## About

A skill for your coding agent to stop it from burying the answer. ADHD-friendly output.

### Topics

 productivity

 developer-tools

 adhd

 claude-

 claude-code-plugin

 claude-skills

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

6.6k

 stars
 

### Watchers

18

 watching
 

### Forks

266

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.