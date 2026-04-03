---
title: I Built a Skill That Writes Your Specs For You - DEV Community
url: https://dev.to/dannwaneri/i-built-a-skill-that-writes-your-specs-for-you-1o2n
site_name: devto
content_file: devto-i-built-a-skill-that-writes-your-specs-for-you-dev
fetched_at: '2026-03-18T11:20:48.198614'
original_url: https://dev.to/dannwaneri/i-built-a-skill-that-writes-your-specs-for-you-1o2n
author: Daniel Nwaneri
date: '2026-03-17'
description: I Built a Skill That Writes Your Specs For You Julián Deangelis published a piece this... Tagged with productivity, webdev, claudecode, agentskills.
tags: '#productivity, #webdev, #claudecode, #agentskills'
---

# I Built a Skill That Writes Your Specs For You

Julián Deangelis published a piece this week that hit 194k+ views in days. The argument: AI coding agents don't fail because the model is weak. They fail because the instructions are ambiguous.

He called it Spec Driven Development. Four steps: specify what you want, plan how to build it technically, break it into tasks, implement one task at a time. Each step reduces ambiguity. By the time the agent starts writing code, it has everything it needs — what the feature does, what the edge cases are, what the tests should verify.

The piece is right. The problem is the workflow takes discipline most sessions don't have. Under deadline pressure, the spec step disappears and you're back to prompting directly.

So I built a skill that does the spec-writing for you.

## The silent decisions problem

Julián's example stuck with me:

"Add a feature to manage items from the backoffice."

The agent reads the codebase, picks a pattern, writes the feature. At first it looks fine. Then you click "add item" again and it inserts the same item twice. All the assumptions you thought were obvious were never in the prompt.

Which backoffice — internal or seller-facing? Should the operation be idempotent? Admin-only or all users? Which storage layer? Which error handling strategy?

Each one is a silent decision. The agent guesses. Some guesses are right. Some are wrong. And you don't find out which until the feature is in production behaving in ways you didn't expect.

The spec is what makes those decisions visible before the agent guesses. But writing a spec from scratch, for every feature, before every session — that's the friction that kills the habit.

## Generate first, flag assumptions inline

The standard approach to spec tools is Q&A: the tool asks clarifying questions before generating anything. What's the user role? What's the auth model? What should happen on error?

The problem with Q&A is you have to know what you don't know. If you knew exactly what questions to ask, you'd be close to having the spec already.

spec-writer takes a different approach. It generates the full spec immediately and marks every decision it made that you didn't specify:

Given 
an authenticated user requesting an export

When the export contains more than 1,000 rows [ASSUMPTION
:
 
async
 
for
 
large
 
exports]

Then 
the export is generated asynchronously and the user is notified by email

Enter fullscreen mode

Exit fullscreen mode

At the end, every assumption is collected into a prioritized list:

## Assumptions to review

1.
 Async generation for exports over 1,000 rows — Impact: HIGH
 Correct this if: your order volumes are low and synchronous is fine

2.
 Date range filter is required — Impact: MEDIUM
 Correct this if: the first version should export all orders with no filtering

Enter fullscreen mode

Exit fullscreen mode

Correcting a draft is faster than answering questions cold. The[ASSUMPTION: ...]tags show you exactly where the agent would have guessed wrong — before it guesses. That's the value. Not the spec itself. The visible assumptions.

## A real example

I ran it on something I'm actually building — CLI capture for Foundation, my knowledge commons project. Foundation currently captures Claude.ai browser conversations via a browser extension. Claude Code sessions live in~/.claude/projects/and disappear after 30 days. I needed to capture those too.

The prompt:

/spec-writer Add CLI capture for Claude Code sessions stored in ~/.claude/projects/

Enter fullscreen mode

Exit fullscreen mode

Here's a slice of what came back:

From the spec:

Given 
a developer with Claude Code sessions in ~/.claude/projects/

When 
they run the Foundation CLI capture command

Then 
a list of uncaptured sessions is displayed, sorted by most recent first

Given 
a session already in Foundation

When 
the developer runs capture again

Then 
that session does not appear in the review list

Given 
a malformed .jsonl file

When 
the capture command processes it

Then 
an error is logged for that file and processing continues on remaining sessions

Enter fullscreen mode

Exit fullscreen mode

From the plan:

CLI capture runs locally — it needs to read the local filesystem, which 
Cloudflare Workers cannot do. [ASSUMPTION: CLI capture is a local Node.js 
or Bun script that calls the Foundation API to insert sessions, rather 
than a Worker itself]

Enter fullscreen mode

Exit fullscreen mode

That assumption stopped me. I hadn't thought through the architecture split — Foundation runs on Cloudflare Workers, which can't read local filesystems. The skill surfaced it before I'd written a line of code.

The assumptions summary:

1.
 CLI capture is a local script calling the Foundation API, not a Worker
 Impact: HIGH
 Correct this if: you want a purely serverless approach

2.
 Manual curation before capture, not automatic bulk import
 Impact: HIGH
 Correct this if: you want automatic background capture

3.
 Session ID from .jsonl filename is the deduplication key
 Impact: MEDIUM
 Correct this if: session IDs are stored differently in your schema

4.
 No sensitive data scrubbing in v1
 Impact: MEDIUM
 Correct this if: your sessions contain credentials or keys

Enter fullscreen mode

Exit fullscreen mode

Four assumptions, two of them high-impact. The architecture one I would have hit mid-implementation. The sensitive data one I wouldn't have thought about until someone complained.

That's the value. Not the spec itself. The visible assumptions.

## How it fits into SDD

spec-writer gets you to Spec-First immediately, with no ceremony. One command, full output, correct the assumptions, hand to the agent.

Julián describes two levels beyond that. Spec-Anchored: the spec lives in the repo and evolves with the code. Spec-as-Source: the spec is the primary artifact, code is regenerated to match. If you want to move toward Spec-Anchored, save the output tospecs/feature-name.mdin your repo. The skill produces something worth keeping.

The methodology is Julián's. The skill is the friction remover.

## Install

mkdir
 
-p
 ~/.claude/skills
git clone https://github.com/dannwaneri/spec-writer.git ~/.claude/skills/spec-writer

Enter fullscreen mode

Exit fullscreen mode

Then:

/spec-writer [your feature description]

Enter fullscreen mode

Exit fullscreen mode

Works across Claude Code, Cursor, Gemini CLI, and any agent that supports the Agent Skills standard. The same SKILL.md file works everywhere.

The repo is atgithub.com/dannwaneri/spec-writer. The README has the full output format and a worked example.

The agents are getting better at implementing. The bottleneck was always specification — knowing what to build precisely enough that the agent doesn't have to guess. spec-writer doesn't remove that requirement. It makes it faster to satisfy.

The spec isn't the output. The assumptions are.

Built on the Spec Driven Development methodology — operationalized by tools likeGitHub Spec KitandOpenSpec. Julián Deangelis's writing on SDD at MercadoLibre was the direct inspiration.

Other skills:voice-humanizer— checks your writing against your own voice, not generic AI patterns.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (13 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse