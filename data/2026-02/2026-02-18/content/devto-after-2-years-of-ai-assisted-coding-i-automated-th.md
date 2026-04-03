---
title: 'After 2 years of AI-assisted coding, I automated the one thing that actually improved quality: AI Pair Programming - DEV Community'
url: https://dev.to/yw1975/after-2-years-of-ai-assisted-coding-i-automated-the-one-thing-that-actually-improved-quality-ai-2njh
site_name: devto
content_file: devto-after-2-years-of-ai-assisted-coding-i-automated-th
fetched_at: '2026-02-18T11:19:47.761979'
original_url: https://dev.to/yw1975/after-2-years-of-ai-assisted-coding-i-automated-the-one-thing-that-actually-improved-quality-ai-2njh
author: Sakiharu
date: '2026-02-16'
description: After nearly 2 years of AI-assisted development — from ChatGPT 3.5 to Claude Code — I kept hitting... Tagged with ai, programming, discuss, automation.
tags: '#discuss, #ai, #programming, #automation'
---

After nearly 2 years of AI-assisted development — from ChatGPT 3.5 to Claude Code — I kept hitting the same problem: every model makes mistakes it can't catch. Inspired by pair programming and the Ralph Loop, I built a dual-agent workflow where one agent writes and another reviews. Last week, a PR written entirely by the two agents got merged into a 15k-star open source Electron project after 3 rounds of maintainer feedback. I don't write TypeScript.

## The problems I kept finding

I've been doing AI-assisted programming for almost 2 years now. Started with ChatGPT 3.5 generating snippets, moved through Claude, Cursor, TRAE, and eventually fell in love with Claude Code.From the very beginning, I noticed every model and every agent has its own characteristic problems. Not random bugs — consistent patterns of failure:

Claude Code skips error handling when context gets long. It's brilliant at architecture but gets sloppy on defensive code in later turns.Codex over-engineers abstractions but catches edge cases Claude misses.Gemini struggles with complex multi-file changes.Cursor has context dependency issues — works great in small scope, gets confused across files.

The severity varies, but the pattern is the same: a single agent can't reliably catch its own mistakes. It writes code AND judges whether that code is good — like grading your own exam.Every developer knows this problem has a name. It's called "why we do code review."

## Pair programming, but with AIs

Pair programming was formalized by Kent Beck as part of Extreme Programming (XP) in the late 1990s — one of the most influential practices to come out of the agile movement. The core idea is simple: two developers at one workstation, one drives, one navigates. The navigator catches mistakes in real time, questions design decisions, and keeps the big picture in focus. Research has consistently shown it produces fewer defects and better designs, despite appearing to "waste" half your developers.The same principle applies to AI agents. If one agent writes and another watches, you catch more bugs.So that's what I started doing — manually. Way back when I was using Claude (the chat version, before Claude Code), I would take Claude's output, paste it into ChatGPT, ask ChatGPT to review it, then bring the feedback back. Primitive, but it worked better than trusting either one alone.When Claude Code and Codex CLI came along, the workflow got more serious. Claude Code writes code, I copy the diffs to Codex, Codex reviews and flags issues, I bring the feedback back to Claude Code. Rinse and repeat.This manual cross-agent coordination worked. But it was slow, repetitive, and cognitively draining. The worst part: it was easy to skip when tired. You tell yourself "this change looks fine, I'll skip the review step" — and that's always the change that bites you.

## Automating the loop

Then I discovered the Ralph Loop (by Geoffrey Huntley) — the concept of wrapping a coding agent in an external loop so it keeps iterating. Powerful idea, and it gave me the push to automate my dual-agent workflow.But the Ralph Loop team has been transparent about some limitations. It works great for greenfield projects with clear completion criteria. It's harder with legacy codebases, complex refactoring, or multi-step tasks where you need checkpoints along the way.That matched my experience. I wasn't building new projects from scratch — I was forking and deeply modifying an existing large Electron app. I needed something that could handle ambiguity, maintainer feedback, and incremental consensus.So I built a structured loop: one agent (Claude Code) writes, another (Codex) reviews, they take turns, and neither moves forward until both agree. I sit in the middle as tech lead — setting scope, making architecture calls, breaking ties.The efficiency jumped immediately. Not because the agents got smarter, but because the review discipline became automatic instead of depending on my willpower at 2am.

## The real test: my first open source PR

I'd been using this workflow to fork AionUI (~15k ⭐ Electron + React app) into an internal AI assistant for my company. 30 commits, zero manual code. Full rebrand, core engine rewrite, database migration, CI/CD rebuild — the whole thing done through the dual-agent loop.During that work, the agents found a real upstream bug: orphan CLI processes that linger when you kill a conversation using ACP agents. I submitted a PR back to AionUI.The maintainer reviewed it and came back with 3 issues:

Double super.kill()race condition — needed an idempotent guardSwallowed errors— .catch(() => {}) should log warningstreeKill discrepancy— the PR description didn't match upstream's actual implementation

I pointed the two agents at the maintainer's feedback and let them work. The author agent analyzed the issues, wrote the fixes, ran tests (133/133 passing). The reviewer agent reviewed the diffs, verified correctness, confirmed types were clean. A few rounds of back-and-forth. I watched but didn't write code.Merged. "LGTM — all three review feedback items properly addressed."This was my first ever PR submitted and merged into someone else's project. I'm a 30-year software veteran — but I spent the last 25 years on product and business, not writing code. I don't write TypeScript. AI tools pulled me back into development, and the dual-agent loop made it possible for me to contribute real fixes to a real project.

## Independent convergence

After I posted about this, another developer (Hwee-Boon Yar, indie dev, also 30 years experience) shared a similar approach — a skill that shells out to a second agent for review, loops until the reviewer has nothing left to flag. Lighter than mine, works within a single session. Different trade-off, same core insight.Multiple people are independently arriving at this: one agent is not enough. You need a second pair of eyes.

## Limitations

This is not a magic solution. Here's what doesn't work:Agent crashes have no auto-recovery. When an agent dies mid-session, the loop stops. You restart manually. No self-healing yet.Wasted rounds. Sometimes the agents ping-pong — a fix introduces a new issue, review catches it, the next fix introduces another issue. You have to step in and reset scope.Context window — but with a twist. Quality degrades in long sessions, and when an agent compresses its context, information gets lost. But here's where the dual-agent setup actually helps: when one agent's context is compressed and loses details, the other agent still remembers. They don't share the same context window, so they don't lose the same information at the same time. This is an unexpected architectural advantage. I'm thinking about building shared memory management across agents in future versions — so they can explicitly share what each has forgotten.Two AIs can happily agree on a bad design. Without domain judgment from a human, this is just two agents rubber-stamping each other. The human arbiter is not optional.This is not autonomous development. It is structured AI-assisted development. The distinction matters.

## The deeper question

The AI coding conversation is too focused on generation and not enough on review. Everyone's benchmarking how fast and how much code models can produce. Nobody's asking: who checks it?If AI code needs structured critique — the same way human code has always needed code review — then the question is: how do you build review discipline into AI workflows?

## Just shipped v0.3.0

I've incorporated what I learned from the AionUI PR process and released a new version. Key stuff:

npm i -g ralph-lisa-loopWorks with Claude Code (Ralph) + Codex CLI (Lisa)Turn control, tag system, consensus protocol, policy checksAuto mode via tmux (experimental)Agent-agnostic in principle — any two CLI agents can fill the roles

Early stage. Using daily for real work, not demos.Repo:If you've been doing AI coding and hitting that frustrating "almost right, but not quite" problem — you're not alone. This might help, or at least give you ideas for your own approach.Happy to discuss. The failure modes are more interesting than the successes.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
