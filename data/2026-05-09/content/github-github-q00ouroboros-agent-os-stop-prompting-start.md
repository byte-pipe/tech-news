---
title: 'GitHub - Q00/ouroboros: Agent OS: Stop prompting. Start specifying. · GitHub'
url: https://github.com/Q00/ouroboros
site_name: github
content_file: github-github-q00ouroboros-agent-os-stop-prompting-start
fetched_at: '2026-05-09T11:49:39.097976'
original_url: https://github.com/Q00/ouroboros
author: Q00
description: 'Agent OS: Stop prompting. Start specifying. Contribute to Q00/ouroboros development by creating an account on GitHub.'
---

Q00

 

/

ouroboros

Public

* NotificationsYou must be signed in to change notification settings
* Fork365
* Star3.8k

 
 
 
 
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

1,078 Commits
1,078 Commits
.claude-plugin
.claude-plugin
 
 
.claude
.claude
 
 
.github
.github
 
 
.ouroboros
.ouroboros
 
 
commands
commands
 
 
crates/
ouroboros-tui
crates/
ouroboros-tui
 
 
docs
docs
 
 
examples
examples
 
 
hooks
hooks
 
 
scripts
scripts
 
 
skills
skills
 
 
src/
ouroboros
src/
ouroboros
 
 
tests
tests
 
 
tools
tools
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.mcp.json
.mcp.json
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Code-Review-Claude.md
Code-Review-Claude.md
 
 
Code-Review-Codex.md
Code-Review-Codex.md
 
 
HANDOFF.md
HANDOFF.md
 
 
LICENSE
LICENSE
 
 
README.ko.md
README.ko.md
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SECURITY.md
SECURITY.md
 
 
UNINSTALL.md
UNINSTALL.md
 
 
llms-full.txt
llms-full.txt
 
 
llms.txt
llms.txt
 
 
project-context.md
project-context.md
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

English|한국어|简体中文

◯ ─────────── ◯O U R O B O R O S◯ ─────────── ◯

Stop prompting. Start specifying.Agent OS for replayable, specification-first AI coding workflows

Quick Start·Why·Results·How It Works·Commands·Philosophy

Turn a vague idea into a verified, working codebase -- across Claude Code, Codex CLI, OpenCode, and Hermes.

Ouroboros is an Agent OS for AI coding: a local-first runtime layer that turns
non-deterministic agent work into a replayable, observable, policy-bound
execution contract. It replaces ad-hoc prompting with a structured
specification-first workflow: interview, crystallize, execute, evaluate,
evolve.

## Why Ouroboros?

Most AI coding fails at theinput, not the output. The bottleneck is not AI capability -- it is human clarity.

Problem

What Happens

Ouroboros Fix

Vague prompts

AI guesses, you rework

Socratic interview exposes hidden assumptions

No spec

Architecture drifts mid-build

Immutable seed spec locks intent before code

Manual QA

"Looks good" is not verification

3-stage automated evaluation gate

## Quick Start

Install— one command, everything auto-detected:

curl -fsSL https://raw.githubusercontent.com/Q00/ouroboros/main/scripts/install.sh 
|
 bash

Build— open your AI coding agent and go:

> ooo interview "I want to build a task management CLI"

Works with Claude Code, Codex CLI, GitHub Copilot CLI, OpenCode, Hermes, Gemini, and Kiro CLI. The installer detects Claude Code, Codex CLI, and Hermes CLI automatically and registers the MCP server. For OpenCode, Kiro, or GitHub Copilot CLI, runouroboros setup --runtime <opencode|kiro|copilot>after installation. The Copilot CLI runtime live-discovers its model catalog via the GitHub Copilot models API and lets you pick a default during setup.

Kiro CLI quick start

pip install 
'
ouroboros-ai[claude]
'

ouroboros setup 
#
 detects Kiro CLI and registers MCP server

Set runtime in.env:

OUROBOROS_RUNTIME=kiro

Then useooocommands inside a Kiro CLI session.

GitHub Copilot CLI quick start

gh auth login 
#
 one-time GitHub auth (used for live model discovery)

pipx install 
'
ouroboros-ai[mcp]
'
 
#
 or: uv tool install 'ouroboros-ai[mcp]'

ouroboros setup --runtime copilot 
#
 discovers models live, picks a default,

 
#
 registers MCP server in ~/.copilot/mcp-config.json

Restart your Copilot CLI session, then useooocommands inside it. Hyphenated Anthropic model IDs (claude-opus-4-6) used elsewhere in your config are auto-mapped to the dotted Copilot form (claude-opus-4.6) at runtime, so existing configs keep working when you switch backends.

See theGitHub Copilot CLI runtime guidefor full details.

Other install methods

Claude Code plugin only(no system package):

claude plugin marketplace add Q00/ouroboros 
&&
 claude plugin install ouroboros@ouroboros

Then runooo setupinside a Claude Code session.

pip / uv / pipx:

pip install ouroboros-ai 
#
 base

pip install ouroboros-ai[claude] 
#
 + Claude Code deps

pip install ouroboros-ai[litellm] 
#
 + LiteLLM multi-provider

pip install ouroboros-ai[mcp] 
#
 + MCP server/client support

pip install ouroboros-ai[tui] 
#
 + Textual terminal UI

pip install ouroboros-ai[all] 
#
 everything (claude + litellm + mcp + tui + dashboard)

ouroboros setup 
#
 configure runtime

Legacy compatibility:ouroboros-ai[dashboard]is still accepted as a compatibility alias while extras migrate.

See runtime guides:Claude Code·Codex CLI·Hermes·OpenCode·Kiro CLI·Gemini CLI·GitHub Copilot CLI

Uninstall

ouroboros uninstall

Removes all configuration, MCP registration, and data. SeeUNINSTALL.mdfor details.

Python >= 3.12 required.Seepyproject.tomlfor the full dependency list.

## What You Get

After one loop of the Ouroboros cycle, a vague idea becomes a verified codebase:

Step

Before

After

Interview

"Build me a task CLI"

12 hidden assumptions exposed, ambiguity scored to 0.19

Seed

No spec

Immutable specification with acceptance criteria, ontology, constraints

Evaluate

Manual review

3-stage gate: Mechanical (free) -> Semantic -> Multi-Model Consensus

What just happened?

interview -> Socratic questioning exposed 12 hidden assumptions
seed -> Crystallized answers into an immutable spec (Ambiguity: 0.15)
run -> Executed via Double Diamond decomposition
evaluate -> 3-stage verification: Mechanical -> Semantic -> Consensus

Useooo <cmd>inside your AI coding agent session, orouroboros init start,ouroboros run seed.yaml, etc. from the terminal.

The serpent completed one loop. Each loop, it knows more than the last.

## How It Compares

AI coding tools are powerful -- but they solve thewrong problemwhen the input is unclear.

Vanilla AI Coding

Ouroboros

Vague prompt

AI guesses intent, builds on assumptions

Socratic interview forces clarity 
before
 code

Spec validation

No spec -- architecture drifts mid-build

Immutable seed spec locks intent; Ambiguity gate (<= 0.2) blocks premature code

Evaluation

"Looks good" / manual QA

3-stage automated gate: Mechanical -> Semantic -> Multi-Model Consensus

Rework rate

High -- wrong assumptions surface late

Low -- assumptions surface in the interview, not in the PR review

## The Loop

The ouroboros -- a serpent devouring its own tail -- is not decoration. It IS the architecture:

 Interview -> Seed -> Execute -> Evaluate
 ^ |
 +---- Evolutionary Loop ----+

Each cycle does not repeat -- itevolves. The output of evaluation feeds back as input for the next generation, until the system truly knows what it is building.

Phase

What Happens

Interview

Socratic questioning exposes hidden assumptions

Seed

Answers crystallize into an immutable specification

Execute

Double Diamond: Discover -> Define -> Design -> Deliver

Evaluate

3-stage gate: Mechanical ($0) -> Semantic -> Multi-Model Consensus

Evolve

Wonder 
("What do we still not know?")
 -> Reflect -> next generation

"This is where the Ouroboros eats its tail: the output of evaluationbecomes the input for the next generation's seed specification."--reflect.py

Convergence is reached when ontology similarity >= 0.95 -- when the system has questioned itself into clarity.

### Ralph: The Loop That Never Stops

ooo ralphruns the evolutionary loop persistently -- across session boundaries -- until convergence is reached. Each step isstateless: the EventStore reconstructs the full lineage, so even if your machine restarts, the serpent picks up where it left off.

Ralph Cycle 1: evolve_step(lineage, seed) -> Gen 1 -> action=CONTINUE
Ralph Cycle 2: evolve_step(lineage) -> Gen 2 -> action=CONTINUE
Ralph Cycle 3: evolve_step(lineage) -> Gen 3 -> action=CONVERGED
 +-- Ralph stops.
 The ontology has stabilized.

## Commands

Inside AI coding agent sessions, useooo <cmd>skills. From the terminal, use theouroborosCLI.

Skill (
ooo
)

CLI equivalent

What It Does

ooo setup

ouroboros setup

Register runtime and configure project (one-time)

ooo interview

ouroboros init start

Socratic questioning -- expose hidden assumptions

ooo auto

ouroboros auto

Goal → A-grade Seed → execution handoff with bounded loops

ooo seed

(generated by interview)

Crystallize into immutable spec

ooo run

ouroboros run seed.yaml

Execute via Double Diamond decomposition

ooo evaluate

(via MCP)

3-stage verification gate

ooo evolve

(via MCP)

Evolutionary loop until ontology converges

ooo unstuck

(via MCP)

5 lateral thinking personas when you are stuck

ooo status

ouroboros status executions
 / 
ouroboros status execution <id>

Session tracking + (MCP-only) drift detection

ooo resume-session

ouroboros resume

List in-flight sessions and re-attach commands

ooo cancel

ouroboros cancel execution [<id>|--all]

Cancel stuck or orphaned executions

ooo ralph

(via MCP)

Persistent loop until verified

ooo tutorial

(interactive)

Interactive hands-on learning

ooo help

ouroboros --help

Full reference

ooo pm

(via MCP)

PM-focused interview + PRD generation

ooo qa

(via skill)

General-purpose QA verdict for any artifact

ooo update

ouroboros update

Check for updates + upgrade to latest

ooo brownfield

(via skill)

Scan and manage brownfield repo/worktree defaults

ooo publish

(skill/runtime surface; uses 
gh
 CLI)

Publish a Seed as GitHub Epic/Task issues for team workflows

Not all skills have direct CLI equivalents. Some (evaluate,evolve,unstuck,ralph,publish) are available through agent skills, runtime rules, or MCP tools rather than a directouroboros <subcommand>shell command./resumeis reserved for Claude Code's built-in session picker; useooo resume-sessionfor Ouroboros in-flight sessions.

See theCLI referencefor full details.

## The Nine Minds

Nine agents, each a different mode of thinking. Loaded on-demand, never preloaded:

Agent

Role

Core Question

Socratic Interviewer

Questions-only. Never builds.

"What are you assuming?"

Ontologist

Finds essence, not symptoms

"What IS this, really?"

Seed Architect

Crystallizes specs from dialogue

"Is this complete and unambiguous?"

Evaluator

3-stage verification

"Did we build the right thing?"

Contrarian

Challenges every assumption

"What if the opposite were true?"

Hacker

Finds unconventional paths

"What constraints are actually real?"

Simplifier

Removes complexity

"What's the simplest thing that could work?"

Researcher

Stops coding, starts investigating

"What evidence do we actually have?"

Architect

Identifies structural causes

"If we started over, would we build it this way?"

## Under the Hood

Architecture overview -- Python >= 3.12

src/ouroboros/
+-- bigbang/ Interview, ambiguity scoring, brownfield explorer
+-- routing/ PAL Router -- 3-tier cost optimization (1x / 10x / 30x)
+-- execution/ Double Diamond, hierarchical AC decomposition
+-- evaluation/ Mechanical -> Semantic -> Multi-Model Consensus
+-- evolution/ Wonder / Reflect cycle, convergence detection
+-- resilience/ 4-pattern stagnation detection, 5 lateral personas
+-- observability/ 3-component drift measurement, auto-retrospective
+-- persistence/ Event sourcing (SQLAlchemy + aiosqlite), checkpoints
+-- orchestrator/ Runtime abstraction layer (Claude Code, Codex CLI, OpenCode, Hermes)
+-- core/ Types, errors, seed, ontology, security
+-- providers/ LiteLLM adapter (100+ models)
+-- mcp/ MCP client/server integration
+-- plugin/ Plugin system (skill/agent auto-discovery)
+-- tui/ Terminal UI dashboard
+-- cli/ Typer-based CLI

Key internals:

* PAL Router-- Frugal (1x) -> Standard (10x) -> Frontier (30x) with auto-escalation on failure, auto-downgrade on success
* Drift-- Goal (50%) + Constraint (30%) + Ontology (20%) weighted measurement, threshold <= 0.3
* Brownfield-- Auto-detects config files across multiple language ecosystems
* Evolution-- Up to 30 generations, convergence at ontology similarity >= 0.95
* Stagnation-- Detects spinning, oscillation, no-drift, and diminishing returns patterns
* Agent OS runtime-- Replayable execution contract across capability discovery, policy, directives, event journal, and agent processes
* Runtime backends-- Pluggable abstraction layer (orchestrator.runtime_backendconfig) with first-class support for Claude Code, Codex CLI, OpenCode, and Hermes; same workflow spec, different execution engines

SeeArchitecturefor the full design document.

## From Wonder to Ontology

The philosophical engine behind Ouroboros

Wonder -> "How should I live?" -> "What IS 'live'?" -> Ontology-- Socrates

Every great question leads to a deeper question -- and that deeper question is alwaysontological: not"how do I do this?"but"what IS this, really?"

 Wonder Ontology
"What do I want?" -> "What IS the thing I want?"
"Build a task CLI" -> "What IS a task? What IS priority?"
"Fix the auth bug" -> "Is this the root cause, or a symptom?"

This is not abstraction for its own sake. When you answer"What IS a task?"-- deletable or archivable? solo or team? -- you eliminate an entire class of rework.The ontological question is the most practical question.

Ouroboros embeds this into its architecture through theDouble Diamond:

 * Wonder * Design
 / (diverge) / (diverge)
 / explore / create
 / /
* ------------ * ------------ *
 \ \
 \ define \ deliver
 \ (converge) \ (converge)
 * Ontology * Evaluation

The first diamond isSocratic: diverge into questions, converge into ontological clarity. The second diamond ispragmatic: diverge into design options, converge into verified delivery. Each diamond requires the one before it -- you cannot design what you have not understood.

Ambiguity Score: The Gate Between Wonder and Code

The Interview does not end when you feel ready -- it ends when themathsays you are ready. Ouroboros quantifies ambiguity as the inverse of weighted clarity:

Ambiguity = 1 - Sum(clarity_i * weight_i)

Each dimension is scored 0.0-1.0 by the LLM (temperature 0.1 for reproducibility), then weighted:

Dimension

Greenfield

Brownfield

Goal Clarity
 -- 
Is the goal specific?

40%

35%

Constraint Clarity
 -- 
Are limitations defined?

30%

25%

Success Criteria
 -- 
Are outcomes measurable?

30%

25%

Context Clarity
 -- 
Is the existing codebase understood?

--

15%

Threshold: Ambiguity <= 0.2-- only then can a Seed be generated.

Example (Greenfield):

 Goal: 0.9 * 0.4 = 0.36
 Constraint: 0.8 * 0.3 = 0.24
 Success: 0.7 * 0.3 = 0.21
 ------
 Clarity = 0.81
 Ambiguity = 1 - 0.81 = 0.19 <= 0.2 -> Ready for Seed

Why 0.2? Because at 80% weighted clarity, the remaining unknowns are small enough that code-level decisions can resolve them. Above that threshold, you are still guessing at architecture.

Ontology Convergence: When the Serpent Stops

The evolutionary loop does not run forever. It stops when consecutive generations produce ontologically identical schemas. Similarity is measured as a weighted comparison of schema fields:

Similarity = 0.5 * name_overlap + 0.3 * type_match + 0.2 * exact_match

Component

Weight

What It Measures

Name overlap

50%

Do the same field names exist in both generations?

Type match

30%

Do shared fields have the same types?

Exact match

20%

Are name, type, AND description all identical?

Threshold: Similarity >= 0.95-- the loop converges and stops evolving.

But raw similarity is not the only signal. The system also detects pathological patterns:

Signal

Condition

What It Means

Stagnation

Similarity >= 0.95 for 3 consecutive generations

Ontology has stabilized

Oscillation

Gen N ~ Gen N-2 (period-2 cycle)

Stuck bouncing between two designs

Repetitive feedback

>= 70% question overlap across 3 generations

Wonder is asking the same things

Hard cap

30 generations reached

Safety valve

Gen 1: {Task, Priority, Status}
Gen 2: {Task, Priority, Status, DueDate} -> similarity 0.78 -> CONTINUE
Gen 3: {Task, Priority, Status, DueDate} -> similarity 1.00 -> CONVERGED

Two mathematical gates, one philosophy:do not build until you are clear (Ambiguity <= 0.2), do not stop evolving until you are stable (Similarity >= 0.95).

## Contributing

git clone https://github.com/Q00/ouroboros

cd
 ouroboros
uv sync --all-groups 
&&
 uv run pytest

Issues·Discussions·Contributing Guide

## Star History

"The beginning is the end, and the end is the beginning."The serpent does not repeat -- it evolves.MIT License

## About

Agent OS: Stop prompting. Start specifying.

### Topics

 mcp

 ai-agent

 agent-os

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

3.8k

 stars
 

### Watchers

13

 watching
 

### Forks

365

 forks
 

 Report repository

 

## Releases81

v0.36.0

 Latest

 

May 7, 2026

 

+ 80 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python97.8%
* Rust1.4%
* Other0.8%