---
title: nobuzz/README.md at main · adnanakil/nobuzz · GitHub
url: https://github.com/adnanakil/nobuzz/blob/main/README.md
site_name: hackernews_api
content_file: hackernews_api-nobuzzreadmemd-at-main-adnanakilnobuzz-github
fetched_at: '2026-08-22T06:00:22.505905'
original_url: https://github.com/adnanakil/nobuzz/blob/main/README.md
author: aakil
date: '2026-08-22'
description: A Claude Code skill (/debuzz) that pipes Claude's answers through Gemini to remove the BuzzFeed voice - nobuzz/README.md at main · adnanakil/nobuzz
tags:
- hackernews
- trending
---

adnanakil

 

/

nobuzz

Public

* NotificationsYou must be signed in to change notification settings
* Fork2
* Star35

 
 
 
 
 

## FilesExpand file tree

main
/

# README.md

Copy path
Blame
More file actions
Blame
More file actions
 

## Latest commit

 

## History

History
History
54 lines (33 loc) · 3.5 KB
main
/

# README.md

Copy path
Top

## File metadata and controls

* Preview
* Code
* Blame
54 lines (33 loc) · 3.5 KB
Raw
Copy raw file
Download raw file
Outline
Edit and raw actions

# NoBuzz

Obviously it's common knowledge by now that Anthropic has solely trained claude on old Buzzfeed articles (explaining its love for 90s nostalgia). So Claude and I built aClaude Codeskill (/debuzz) that takes Claude's last response and runs it through the Gemini CLI to translate it from talking like a millennial clickbait to regular English. We're thinking of calling it "Claudette" but Cat Wu is famously litigious so it's definitely absolutely not called "Claudette".

## The problem

Claudette is our solution to Claude being a great engineer with one incurable condition: it talks like it's delivering a TED talk about its own pull request. You ask why a test is flaky and you get a "load-bearing assumption," three numbered revelations, and a solemn note that the third one isthe most instructive yet. Nothing is ever just a bug. There is always a kicker.

This skill accepts that no amount of prompting fully cures this, and does the honest thing instead: it hands the response to a different model, Gemini (remember gemini from last summer?), whose only job is to say it like a human person. Claudette has pinky promised to print Gemini's translation verbatim, because letting Claude "tidy up" the translation reintroduces exactly the voice being removed.

## Before / after

Before (Claude):

Here's where it gets interesting: the retry logic isn't just a nice-to-have — it's - the - load-bearing - assumption - of - the - entire - sync - pipeline. Three things jumped out at me, and the third one is the most instructive yet. [...] And third — and this is the kicker — the dedupe key includes a timestamp, which means retries are never actually deduplicated.

After (/debuzz, colleague mode):

The sync pipeline's retry logic has three bugs.syncQueue.ts:142swallowsETIMEDOUTinstead of re-queuing the job. The backoff caps at 2 seconds, which is too low for mobile networks. And the dedupe key includes a timestamp, so retries are never deduplicated. Fix: strip the timestamp from the key, raise the cap to 30 seconds, and re-throw the timeout error.

## Install

git clone https://github.com/adnanakil/nobuzz
mkdir -p 
~
/.claude/skills
cp -r nobuzz/debuzz 
~
/.claude/skills/

Requirements:

* Claude Code
* TheGemini CLI(npm install -g @google/gemini-cli), authenticated — rungeminionce and use/auth, or setGEMINI_API_KEY.

## Usage

/debuzz [mode] [text]

Mode

Audience

What you get

colleague
 (default)

An engineer

Same content, every file path and code block intact, zero theatrics

manager

A technical-adjacent manager

What happened, why it matters, what's next — about a third the length, no code

director

An executive

Three to five sentences: outcome, impact, ask. Assumes thirty seconds of attention

With no text argument it translates Claude's previous reply. Paste text after the mode to translate that instead. It also triggers on natural phrases like "say that in normal english."

## How it works

No magic. Claudette writes its previous reply to a temp file, pipes it throughgemini -p "<plain-English style instructions>", and prints Gemini's output verbatim. If Gemini errors (usually auth), you see the actual error — Claude only offers its own rewrite as a clearly labeled fallback, because a debuzzer that quietly asks the buzzer to debuzz itself is how you end up with a load-bearing translation.

## License

MIT