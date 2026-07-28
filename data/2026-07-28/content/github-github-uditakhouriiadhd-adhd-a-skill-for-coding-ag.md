---
title: 'GitHub - UditAkhourii/adhd: ADHD — a skill for coding agents. Tree-of-thought with pruning, built on the Claude & Codex Agent SDK. Fans out parallel divergent thoughts under different cognitive frames, scores, prunes traps, deepens the survivors. The no-brainer skill for creative and interdisciplinary work. · GitHub'
url: https://github.com/UditAkhourii/adhd
site_name: github
content_file: github-github-uditakhouriiadhd-adhd-a-skill-for-coding-ag
fetched_at: '2026-07-28T11:43:11.015565'
original_url: https://github.com/UditAkhourii/adhd
author: UditAkhourii
description: ADHD — a skill for coding agents. Tree-of-thought with pruning, built on the Claude & Codex Agent SDK. Fans out parallel divergent thoughts under different cognitive frames, scores, prunes traps, deepens the survivors. The no-brainer skill for creative and interdisciplinary work. - UditAkhourii/adhd
---

UditAkhourii

 

/

adhd

Public

* NotificationsYou must be signed in to change notification settings
* Fork201
* Star2.5k

 
 
 
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

66 Commits
66 Commits
.github
.github
 
 
bench
bench
 
 
docs
docs
 
 
documentation
documentation
 
 
skills/
adhd
skills/
adhd
 
 
src
src
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.npmignore
.npmignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
EVALS.md
EVALS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SOURCE-SPEC.md
SOURCE-SPEC.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.bench.json
tsconfig.bench.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# ADHD — a skill for agents

### 🎮Join the ADHD Discord →

This is where the real-time thinking happens: frame design, eval problems, trap-hunting, and neurodivergence-inspired research on reasoning architectures. If you've got opinions on premature convergence, cognitive frames, or just want to argue about the next eval problem —come argue with us live.

👉Join the ADHD community →as a contributor, maintainer, early adopter, or just a member. One short form. We coordinate frame contributions, eval problems, integrations, and adopter onboarding there.

An architectural fix for premature convergence in autoregressive reasoning.

Linear Chain-of-Thought anchors on whatever it says first. Tree-of-Thought widens the search but still walks a single shared context, so the anchoring persists across branches.ADHD treats this as an architectural problem, not a prompting one— it spawns N isolated reasoning processes under deliberately distorted cognitive frames, with zero shared context during divergence, then runs a separate critic pass to score, cluster, prune traps, and deepen the survivors.

Reach for it ondesign decisions, fuzzy debugging, naming, API surface design, strategy, and any prompt of the shape"give me a few ways to…".

📄Preprint:ADHD: Parallel Divergent Ideation for Coding Agents· 👤Author:Udit Akhouri —@akhouriudit·LinkedIn

## Side-by-side: baseline vs ADHD

One eval problem, same model, two strategies. Full transcripts inbench/results.json.

Problem."We have a CLI that calls an LLM and it sometimes hangs for 90 seconds. Design the right retry/timeout/UX strategy."

🟦 Baseline (single-shot)

🟧 ADHD

Walks through fourtextbookpatterns:

1. Progressive timeout with staged UI (10s / 30s / 60s)
2. Fast-fail + exponential backoff retry
3. Hedged parallel requests
4. Streaming with keepalive

Lands on ahybridrecommendation — 15s first-token timeout, 30s between-token timeout, 90s absolute, one auto-retry. Sensible. Google SRE Book ch. 22. The answer a senior engineer gives in 30 seconds.

What's missing:no traps named, no acknowledgement that theusermight want to bail out of a slow request, no questioning of the "wait then retry the same model" frame.

Spawns 6 isolated frames, surfaces awide setof 30+ ideas acrosseconomic-incentive,async-control-surface,gamification,perceptual-distortion,collective-intelligence,redundancy-raceclusters, then:

* ★Non-obvious pick:"rage-quit = instant abort + branch to cheaper/faster model"— a button that pulses hotter the longer you wait. One click cancels and re-submits to Haiku-class. The thing baseline never considers:the slow model might just be the wrong model for this prompt.
* Plus shortlist: scout-fork to alternate endpoints at 30s; daemonize the CLI with ticket IDs; race 3 LLM replicas, cache the winner.
* 20 traps flagged with one-line reasons— including the cute "stream tokens in reverse" and "patience-token billing" ideas before they cost engineering time.

Independent LLM judge on this problem:breadth 9 vs 6, novelty 8 vs 3, trap detection ~8 vs ~2.Methodology indocumentation/evals.md.

## Featured

* 🔌Adopted byrepowire— the first OSS project to officially ship ADHD. Its maintainer ported the framework onto repowire's mesh-orchestrator primitives inPR #313(merged): frames become frame-shifted temp peers, the generator/critic split maps onto separate peers vs. the orchestrator's own turn, attribution viametadata.based-on(MIT).
* 📰The New Stackran a feature story on ADHD for Claude Code.
* 💬OpenClaw / multi-agent communityis independently testing it across agents. One tester:"I read it, installed it on two different agents… I actually love it. This is great. I thought this was gonna be another useless post. But no, it wasn't."
* 🔬 An independentevidence-based research review(11 sources, 8 validation rounds) was published against the method — findings tracked openly asissues #16–#18.

## Community

👉Join the ADHD community →as a contributor, maintainer, early adopter, or just a member. One short form. We coordinate frame contributions, eval problems, integrations, and adopter onboarding there.

## Early adopters

Projects that officially ship or integrate ADHD:

Project

What they did

Status

repowire

Ported ADHD onto repowire's mesh-orchestrator primitives — frames become frame-shifted temp peers, generator/critic split maps to separate peers vs. the orchestrator's turn. Ships in the default orchestrator template. (
PR #313
)

✅ Merged · MIT attribution

mstack

Vendored ADHD as the 
think
 plugin in their Claude plugin marketplace — wires the divergent-then-converge loop into mstack for architecture, naming, API design, and fuzzy debugging.

✅ Shipped · MIT attribution

zk-flow-oss

Adapted ADHD's 
IDEATION_FRAMES
 into their critique workflow (
src/workflows/critique.src.js
) as a pre-pass to reduce anchoring bias before review.

✅ Shipped · MIT attribution

han

Published an 
evidence-based research application
 of ADHD onto Han's plugin model — 11 sources, 8 validation rounds. Findings landed as issues 
#16
–
#18
.

✅ Research integration

app-library
 (yslee5005)

Built an 
expert-thinker
 MoAI agent on the ADHD pattern — tree-of-thought with isolated divergence and a separate critic pass.

✅ Shipped

striatum

Installer scaffold for Claude Code recommends 
npx skills add UditAkhourii/adhd
 for architecture, API design, and naming work.

✅ Shipped

awesome-prompts

Packaged the ADHD loop as a standalone prompt (
adhd_parallel_ideation_skill.txt
) for users without the skill installed.

✅ Shipped

nix-skills

Nix packaging of the ADHD skill (pinned to commit 
770834e
) for the Nix-based agent-skills ecosystem.

✅ Shipped

caioniehues/adhd

Fork with a customized 
SKILL.md
 that re-points install + docs to their own distribution while keeping upstream attribution.

✅ Fork · attribution

ktg-one/adhd

Fork used as a personal "codified model of how my brain works" — wired into the 
may-2026-kb
 knowledge base as a cognitive-architecture pattern.

✅ Fork · in use

wtfismyrepo

Uses ADHD as the explanation engine for codebase onboarding. The deterministic layer (import-graph PageRank, git-churn fragility, GitHub PR/issue signals) produces an analysis object that is formatted as an ADHD 
problem
 + 
context
. The ADHD diverge→score→cluster→deepen loop then generates onboarding angles across 12 codebase-specific frames (
new-grad
, 
archeologist
, 
security-researcher
, 
on-call-at-3am
, 
refactorer
, 
inversion
, …), scores them for fit to the developer's level + goal, prunes traps, and deepens the non-obvious pick into a full walkthrough. Ships the ADHD method in the Claude Code skill (
SKILL.md
) with zero extra deps — Claude runs the frames itself.

✅ Shipped · MIT attribution

mythify

Added trap-clause and alternatives guidance to its analysis prompt packet after evaluating ADHD's divergent-frames-then-critic pattern — surfaces "the one that looks good but isn't, and why" before a plan is committed to. (
PR #18
)

✅ Merged

godaudits

Shipped v2.11.0 adopting measurement and provenance discipline from an ADHD review — an independent refutation pass (
refute plan
/
apply
), severity-aware recall metrics, and attribution/limits tracking on eval results. (
PR #13
)

✅ Shipped

godplans

Shipped v1.8.0 turning its self-audit into an independent audit gate (separate scoring pass, isolated context) and adding a no-skill baseline control arm to its eval harness, inspired by ADHD's generator/critic split — while explicitly rejecting the novelty-scoring axis and randomized frame selection as unsuited to its own goals. (
PR #8
)

✅ Shipped

Claude1.0
 (Ro-Sama-33)

Installed the ADHD skill into 
.agents/skills/adhd/
. (
PR #16
)

✅ Installed

Shipping ADHD in your project? Open a PR adding it here, oropen an issueand we'll add you.

## Install

One command, auto-detects your agent (Claude Code, Cursor, Antigravity, Codex, Cline, Gemini CLI, Windsurf, and ~50 more):

npx skills add UditAkhourii/adhd

Then invoke explicitly with/adhd "your problem", or let it auto-trigger on ideation intents.

### Codex quick path

If the universal command above fails to register inside Codex (some Codex builds discover skills from a specific path), force the target:

npx skills add UditAkhourii/adhd -a codex -g

Or install manually into Codex's skills directory:

mkdir -p 
~
/.codex/skills/adhd
curl -fsSL https://raw.githubusercontent.com/UditAkhourii/adhd/main/skills/adhd/SKILL.md \
 -o 
~
/.codex/skills/adhd/SKILL.md

Restart Codex./adhd "design a rate limiter"should now route through the skill. The skill ships with a single-line description (≤600 chars) specifically because some Codex builds truncate or reject multi-line YAML block descriptions.

CLI and library installs, manual curl for other agents, and per-platform paths are indocumentation/install.md.

npm install -g adhd-agent 
#
 CLI

npm install adhd-agent 
#
 library

## Quickstart

adhd 
"
design a rate limiter that survives a leader election
"

adhd 
"
name this function
"
 --frames 3 --ideas 8 --top 2

import
 
{
 
run
,
 
renderText
 
}
 
from
 
"adhd-agent"
;

const
 
result
 
=
 
await
 
run
(
{
 
problem
: 
"How should we shard this queue under bursty load?"
,
 
framesPerRun
: 
5
,
 
topK
: 
3
 
}
)
;

console
.
log
(
renderText
(
result
)
)
;

// result.shortlist · result.nonObviousPick · result.traps · result.deepened · result.clusters

Full reference:documentation/api.md.

## How it works

A two-phase loop with a hard wall between the phases.

1. Diverge.Pick N cognitive frames. Spawn N parallel,isolatedAgent calls — each sees the problem plus one frame's vantage prompt, and a system prompt that forbids evaluation. Branches never see each other, so no anchoring.
2. Focus.A separate critic call scores every idea (novelty / viability / fit), flags traps with reasons, clusters by underlying angle, and deepens the top-K survivors into sketches with risks and first steps.

The generator-critic split ismechanical— separate LLM calls with opposite system prompts — not promised in one prompt. Deep dive:documentation/how-it-works.md. How it differs from CoT and ToT:documentation/vs-cot-and-tot.md.

## Results

Mean scores across 6 open-ended engineering problems (0–10), ADHD vs a single-shot baseline at the same model, judged by an independent LLM with a skeptical-staff-engineer prompt, A/B order randomized.

Dimension

ADHD

Baseline

Δ

Ratio

breadth

9.00

4.83

+4.17

1.9×

novelty

7.83

2.67

+5.17

2.9×

trap detection

9.50

1.83

+7.67

5.2×

actionability

9.50

6.50

+3.00

1.5×

builder usefulness

7.67

6.83

+0.83

1.1×

ADHD wins 5 of 6 problems.Biggest gap is trap detection — baselines rarely name the seductive-but-broken ideas. Methodology, limitations, and how to reproduce:documentation/evals.md.

## Documentation

Page

What's in it

Quickstart

First skill, CLI, and TypeScript runs with practical commands

Install

Every install path — skill, CLI, library, Agent SDK, per-platform

How it works

The two-phase loop + architecture (context, pruning, orchestration)

vs CoT & ToT

Structural comparison, the three load-bearing differences, frames vs personas

Frames

The 15 cognitive frames, how selection works, how to author your own

When to use

Use / don't use, why it shines on creative work, cost & speed

CLI & API

CLI flags, library types, using ADHD inside your own agent

Evals

Methodology, headline numbers, limitations, roadmap

Also:SKILL.md(the runnable skill) ·SOURCE-SPEC.md(original spec) ·CONTRIBUTING.md·the preprint.

## Star History

## Star History

## External reviews

* Han plugin compatibility analysisby@mxriverlynn— evidence-based review using Han's own/researchskill, 11 sources, 8 validation rounds. Findings tracked as issues#16,#17,#18.
* A measured duel vs. single-shotby Shichinomiya (@shichinomiya_s) — independent blind-scored benchmark (2 problems, LLM-as-judge, A/B positions swapped). ADHD won both, with the biggest gains in novelty (4.5→9.0) and trap detection (5.0→9.0), at a real cost of ~2.3× time and ~1.9× output.

## License

MIT License.

ADHD operationalizes theDivergent Ideationsource spec (SOURCE-SPEC.md). The runnable skill is atskills/adhd/SKILL.md.

## Contact

Udit Akhouri— author of the preprint and maintainer.

adhdstack.github.io·@akhouriudit·LinkedIn·researchudit@gmail.com·@UditAkhourii

Open to collaboration with research labs and applied-AI teams working on reasoning, planning, and agentic systems.