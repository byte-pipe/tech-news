---
title: AI Agent Failure Modes Beyond Hallucination - DEV Community
url: https://dev.to/maximsaplin/ai-agent-failure-modes-beyond-hallucination-208g
site_name: devto
content_file: devto-ai-agent-failure-modes-beyond-hallucination-dev-co
fetched_at: '2026-05-29T04:36:03.285899'
original_url: https://dev.to/maximsaplin/ai-agent-failure-modes-beyond-hallucination-208g
author: Maxim Saplin
date: '2026-05-22'
description: AI can make mistakes, models hallucinate, models make stuff up - those are well-known complaints. Yet... Tagged with ai, agents, vibecoding, programming.
tags: '#ai, #agents, #vibecoding, #programming'
---

Taxonomy of amnesia and recursive cost drift

AI can make mistakes, models hallucinate, models make stuff up - those are well-known complaints. Yet they are barely practical when it comes to agentic engineering. What does the knowledge that models make mistakes leave you with, except not trusting any output, or expecting every line to be double-checked, killing all the productivity?

I do use agentic tools a lot, and I am fascinated by how much they have improved over the past half year. At the same time, I am often pissed off by how badly many large tasks drift from common sense and the spirit of the task.

Lately, while reading plenty of material about AI agents, I pay more attention to what sort of failure modes people call out. Often those resonate with me heavily. It is gold when someone distills a pattern into a short characteristic of models or AI agents: the "jaggedness." This sort of knowledge helps build your own intuition around AI agent capabilities and reasonable ways to shape your work around agents. It helps with healthy expectations without buying into the over-sold dark factories and other made-up AI capability BS claims around us.

Below is my attempt to categorize and outline the failure modes called out in a few blog posts and conference talks that align with my observations.

## Failure Modes

Failure Mode

Few Words

Source

One-shotting

Tries to eat the whole app in one bite, runs out of context, and leaves a half-built mess.

Anthropic long-running agents
: "try to do too much at once...to one-shot the app."

Progress-as-completion

Sees activity in the repo and mistakes partial progress for the whole job being done.

Anthropic long-running agents
: "see that progress had been made, and declare the job done."

Cold-start amnesia

Fresh sessions inherit neither memory nor runbook, then waste time guessing what happened and how to check it.

Anthropic long-running agents
: "each new session begins with no memory"; "figuring out how to run the app."

Ugly wish-granting

You state a wish too loosely and the agent grants it literally, completely, and uglier than if you had never asked.

My observation: less like delegation, more like telling a genie your wish and getting the cursed version back.

Spec-deliverable confusion

Treats the temporary plan or design doc as part of the actual deliverable, bundling scaffolding with the thing it was supposed to build.

My observation: especially visible in plan-mode, e.g. asking to create and agent skill and it comes back with the planning artifact inside the skill.

Default-fill slop

Unspecified parts of the task get filled with mediocre training-prior defaults: cargo-cult code, safe UI, generic product choices.

Mario Zechner
: "If you leave blanks in your spec...it fills it in with the garbage"; 
Anthropic app harness
: "safe, predictable layouts."

Overengineering by default

Adds abstractions, duplication, backwards compatibility, and defense-in-depth because internet-shaped code taught it those moves.

Mario Zechner
: "agents...have learned complexity."

Working-memory rot

Important facts sit in the context but stop being reliably available as the window grows.

Random Labs Slate
: "the model's ability to attend...degrades as the context length grows."

Hidden harness control

The tool mutates context, prompts, tools, reminders, observability, and extensibility in ways the user cannot inspect or steer.

Mario Zechner
: "my context wasn't my context"; "zero observability...almost zero extensibility."

Lossy compaction

Compression keeps long runs alive by dropping state, sometimes exactly the state you needed.

Random Labs Slate
: "we can unpredictably lose important information."

Local patching

Each move looks locally reasonable while the global system gets harder to reason about.

Mario Zechner
: "every decision of an agent is local."

Summary-only handoff loss

Subagents isolate context, then pass back a neat summary instead of enough real state to integrate safely.

Random Labs Slate
: "fails to transfer information across context boundaries."

Async reconciliation failure

Parallel work creates the hard question of when results are final, which branch wins, and what actually composes.

Random Labs Slate
: "knowing when and how to reconcile results."

Blind N-step execution

Delegated chunks run too long without feedback; the agent discovers the wall only at the end.

Random Labs Slate
: "like navigating a maze blind."

Plan drag

Plans and task trees prevent early stopping until reality changes, then the structure itself resists adaptation.

Random Labs Slate
: "Markdown plans go stale"; "trading the flexibility...for rigidity."

Overdecomposition

Planner/implementer/reviewer stacks technically work, but add ceremony, latency, and inertia.

Random Labs Slate
: "It will sort of work, but you're going to hate its guts."

Validation interruption

Diagnostics injected mid-edit confuse the model before a coherent change exists.

Mario Zechner
: "you finish your work and then you check the errors."

False E2E completion

Unit tests or curl pass, but the actual user path is still broken.

Anthropic long-running agents
: "fail recognize that the feature didn't work end-to-end."

Functional but wrong

The result passes checks or sort of works, while still being awkward, unusable, overcomplicated, or against the spirit of the task.

Long-horizon agents
: "functionally OK but awkward, sloppy, or strangely overcomplicated"; "pass checks and still feel wrong."

Self-review softness

The agent grades its own mediocre work with confident praise and weak critique.

Anthropic app harness
: "confidently praising the work...obviously mediocre."

Modality blind spots

QA tooling misses bugs it cannot see, hear, or exercise like a real user.

Anthropic app harness
: "Claude can't actually hear."

## Why This Turns Into Fatigue

Two related problems do not quite belong in the failure-mode table, but they explain why the whole thing gets so tiring so fast.

First, generation outruns review. Mario's "slow the f.ck down" is not just a mood; it is an operational constraint. Once agents can produce code, tests, issues, and PRs faster than humans can read them, the bottleneck moves from typing to judgment. A review agent catches some issues, but it does not restore ownership. If nobody reads the code, nobody knows what is critical, and when users start screaming there is no human understanding left in the room.

Second, the same dynamic leaks outside your repo. AI issues, AI PRs, synthetic comments, generated docs, generic posts: some of them can be useful, but the channel fills with plausible text faster than people can sort it. That is the wider AI slop problem. The cognitive residue is fatigue, cynicism, AI brainrot, and eventually all-caps prompts begging the machine to stop being cute and do the actual job.

This is why "slow down" is not nostalgia or moral scolding. It is a practical rule: keep generated work inside reviewable bounds, use agents where verification is cheap, and preserve enough human understanding to say no.

## Fixes And What They Break

Fix

Helps with

Breaks / creates

Context reset

Long-task drift, context anxiety.

Handoff artifact becomes critical state. Bad handoff means bad next session.

Compaction

Keeps a long run going.

Drops important state unpredictably.

Feature list / task list

One-shotting, premature completion.

Rigid plans, stale status, checkbox theater.

Strict task tree

Early stopping, incomplete decomposition.

Low expressivity; hard to adapt when reality changes.

Subagents

Context isolation, parallel search.

Thin summaries, message-passing limits, merge problems.

Separate evaluator

Self-praise and weak review.

Evaluator still misses things; criteria can create rubric-shaped slop.

Browser / E2E testing

False completion from local checks.

Tool blind spots remain; perception limits remain.

User-owned minimal harness

Hidden vendor behavior, opacity, shallow extensibility.

Security, workflow design, and maintenance move back to the user.

## Sources

* Anthropic,"Effective harnesses for long-running agents", Nov 2025
* Anthropic,"Harness design for long-running application development", Mar 2026
* Random Labs,"Slate: moving beyond ReAct and RLM", Mar 2026
* Mario Zechner,"Building Pi in a World of Slop", AI Engineer conference talk, Apr 2026
* My earlier write-up,"Long-Horizon Agents Are Here. Full Autopilot Isn't.", Mar 2026

## P.S.>

Mario, the creator of Pi Agent, uses the word "f.ck" too often in his talk. I find myself in a similar position with all caps and lots of F.CK in my prompts. I guess that is the AI fatigue from too many AI outputs manifesting :)

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (19 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse