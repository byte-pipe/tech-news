---
title: How to Supervise AI Coding Agents Without Losing Your Mind - DEV Community
url: https://dev.to/battyterm/how-to-supervise-ai-coding-agents-without-losing-your-mind-53m4
site_name: devto
content_file: devto-how-to-supervise-ai-coding-agents-without-losing-y
fetched_at: '2026-04-08T11:23:52.578565'
original_url: https://dev.to/battyterm/how-to-supervise-ai-coding-agents-without-losing-your-mind-53m4
author: Batty
date: '2026-04-04'
description: Running one AI agent works great. Running three in parallel on the same repo? They overwrite files, skip tests, and declare victory on broken code. Here is the supervision pattern that fixed it. Tagged with ai, devtools, productivity, tutorial.
tags: '#ai, #devtools, #productivity, #tutorial'
---

Multi-agent isolation via Git worktrees

Running one AI coding agent on a task works great. You give it a focused problem, it writes code, you review it. Simple.

Now try running three in parallel on the same repo.

## What Goes Wrong

I've been running Claude Code, Codex, and Aider on real projects for months. The moment you scale from one agent to multiple, three things break immediately:

1. File conflicts.Two agents edit the same file simultaneously. One overwrites the other's work. Neither knows it happened. You find out when nothing compiles.

2. No quality gate.Agents declare tasks "done" when they've generated code — not when that code actually works. Without intervention, you end up with a pile of plausible-looking code that fails the test suite.

3. You become a full-time dispatcher.Instead of coding, you're tabbing between terminals, checking who's working on what, resolving conflicts, and manually running tests. The agents are working. You're not.

Each of these problems has a specific fix. None of them require new AI capabilities — they're supervision patterns you can implement with existing tools.

## Fix 1: Isolate Work with Git Worktrees

The file conflict problem disappears when each agent works in its own copy of the repo. Git worktrees give you exactly this:

# Create isolated workspaces for each agent

git worktree add .worktrees/agent-1
-b
 agent-1/task-1
git worktree add .worktrees/agent-2
-b
 agent-2/task-2
git worktree add .worktrees/agent-3
-b
 agent-3/task-3

Enter fullscreen mode

Exit fullscreen mode

Each agent gets its own directory, its own branch, its own working tree. They can't overwrite each other's files because they're literally working in different directories on different branches.

When an agent finishes, you merge its branch back to main. If there's a conflict, you resolve it once — not continuously while agents are working.

The practical limit is 3-5 parallel agents. Beyond that, the codebase itself becomes the bottleneck — too many concurrent changes for the merge step to absorb cleanly.

## Fix 2: Gate Everything on Tests

This is the single most impactful change. Before accepting any agent's output, run the test suite:

cd
 .worktrees/agent-1
cargo
test

# or npm test, pytest, etc.

echo

$?

# 0 = merge it, non-zero = send it back

Enter fullscreen mode

Exit fullscreen mode

If tests fail, the task isn't done. Send the failure output back to the agent and let it fix its own work. This creates a feedback loop that dramatically improves output quality.

What this eliminates:

* Code that compiles but doesn't work
* Regressions in existing functionality
* The "it looks right at a glance" trap

The key insight: you don't need a sophisticated evaluation framework. Your existing test suite — the one you already maintain — is the quality gate.exit 0means done. Everything else means try again.

I've seen this reduce the "agent broke something" rate by roughly 80%. The remaining 20% are cases where tests don't cover the affected behavior — a test coverage problem, not an agent problem.

## Fix 3: Structure the Dispatch

When you have multiple agents, someone needs to decide who works on what. If you let agents self-organize, you get duplicated work and priority inversions.

A Markdown kanban board is the simplest approach:

## Todo

-
 [ ] Add JWT authentication (#12)

-
 [ ] Write API endpoint tests (#13)

## In Progress

-
 [ ] Refactor database layer (#11) — agent-1

## Done

-
 [x] Fix login redirect (#10) — agent-2

Enter fullscreen mode

Exit fullscreen mode

The board is the single source of truth. An agent picks a task from Todo, moves it to In Progress, works on it, and moves it to Done when tests pass. No two agents work on the same task because the board makes assignments visible.

The format matters less than the constraint: one task per agent, visible state, no ambiguity about who's doing what.

## Putting It Together

The full supervision pattern:

1. Decomposework into independent tasks on a kanban board
2. Assignone task per agent
3. Isolateeach agent in its own git worktree
4. Gatecompletion on passing tests
5. Mergetested branches back to main, one at a time

This is what I builtBattyto automate. It's a Rust CLI that runs the supervision loop: launches agents in tmux panes, dispatches tasks from a Markdown kanban, isolates work in worktrees, and gates everything on tests. But the pattern works even if you do it manually.

The important thing isn't the tool — it's the constraints. Isolation prevents conflicts. Test gating prevents broken merges. Structured dispatch prevents duplicated work. Without these, more agents means more chaos. With them, more agents means more throughput.

## What Supervision Isn't

It's not fire-and-forget. You still review code before merging. You still watch for agents going off-track. You still decompose work into reasonable tasks.

It's closer to managing a team of junior developers than to pressing a button and getting code. The leverage is that you're supervising five parallel workstreams instead of doing one task yourself. That's a real productivity gain — but only if the supervision layer keeps things from falling apart.

The agents aren't going to get worse at coding. They're going to get better. What won't change is the need for isolation, quality gates, and structured coordination. Build those habits now.

Try it:cargo install batty-cli—GitHub|2-min demo

If you're running multiple agents and have found other supervision patterns that work, I'd love to hear about them in the comments.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (15 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
