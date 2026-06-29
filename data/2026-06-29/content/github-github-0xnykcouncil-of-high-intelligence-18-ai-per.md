---
title: 'GitHub - 0xNyk/council-of-high-intelligence: 18 AI personas deliberate your hardest decisions across multiple LLM providers. Aristotle, Feynman, Kahneman, Torvalds & more — structured multi-round deliberation with genuine model diversity. One command: /council · GitHub'
url: https://github.com/0xNyk/council-of-high-intelligence
site_name: github
content_file: github-github-0xnykcouncil-of-high-intelligence-18-ai-per
fetched_at: '2026-06-29T19:36:08.317176'
original_url: https://github.com/0xNyk/council-of-high-intelligence
author: 0xNyk
description: '18 AI personas deliberate your hardest decisions across multiple LLM providers. Aristotle, Feynman, Kahneman, Torvalds & more — structured multi-round deliberation with genuine model diversity. One command: /council - 0xNyk/council-of-high-intelligence'
---

0xNyk

 

/

council-of-high-intelligence

Public

* NotificationsYou must be signed in to change notification settings
* Fork194
* Star1.8k

 
 
 
 
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

33 Commits
33 Commits
.github/
workflows
.github/
workflows
 
 
.gstack
.gstack
 
 
agents
agents
 
 
assets
assets
 
 
configs
configs
 
 
demos
demos
 
 
scripts
scripts
 
 
.DS_Store
.DS_Store
 
 
.gitattributes
.gitattributes
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SKILL.codex.md
SKILL.codex.md
 
 
SKILL.gemini.md
SKILL.gemini.md
 
 
SKILL.md
SKILL.md
 
 
install.sh
install.sh
 
 
View all files

## Repository files navigation

# Council of High Intelligence

18 AI personas deliberate your hardest decisions across multiple LLM providers. One command.

Table of Contents

* Quickstart
* Why This Works
* The 18 Council Members
* Three Deliberation Modes
* Multi-Provider Auto-Routing
* Deliberation Protocol
* Installation
* Requirements
* Contributing
* Support the Project

## Quickstart

### Claude Code

git clone https://github.com/0xNyk/council-of-high-intelligence.git

cd
 council-of-high-intelligence
./install.sh

Then in Claude Code:

/council Should we open-source our agent framework?
/council --quick Should we add caching here?
/council --duo Should we use microservices or monolith?

### Codex

git clone https://github.com/0xNyk/council-of-high-intelligence.git

cd
 council-of-high-intelligence
./install.sh --codex

Then in Codex:

/council Should we open-source our agent framework?
/council --quick Should we add caching here?
/council --duo Should we use microservices or monolith?

## Why This Works

A single LLM gives you one reasoning path dressed up as confidence. Ask it a hard question and you get a fluent, structured, wrong answer. The council gives you structured disagreement instead:

* Get genuinely different perspectives— polarity pairs force real tension (Socrates destroys assumptions; Feynman rebuilds from first principles). Multi-provider routing spreads members across Claude, OpenAI, Gemini, and Ollama so you get actually different reasoning, not costume changes on one model
* Catch wrong questions early— the Problem Restate Gate makes every member reframe the question before analysis begins. If 3 members restate your question differently, the question was the problem
* Know what the council can't answer— verdicts lead with Unresolved Questions and Recommended Next Steps, not with confident-sounding consensus. What the council doesn't know matters more than where it agrees
* Prevent groupthink— dissent quotas, novelty gates, and counterfactual prompts enforce genuine disagreement. If >70% agree too early, two members are forced to steelman the opposing view

Why not just ask Claude directly?A single prompt gives you one model's confident best guess. The council gives you 3-18 independent analyses from different intellectual traditions, forces them to challenge each other's claims, and synthesizes a verdict that surfaces disagreement rather than hiding it. It's the difference between asking one advisor and convening a board.

## The 18 Council Members

Agent

Figure

Domain

Default Model

Polarity

council-aristotle

Aristotle

Categorization & structure

opus

Classifies everything

council-socrates

Socrates

Assumption destruction

opus

Questions everything

council-sun-tzu

Sun Tzu

Adversarial strategy

sonnet

Reads terrain & competition

council-ada

Ada Lovelace

Formal systems & abstraction

sonnet

What can/can't be mechanized

council-aurelius

Marcus Aurelius

Resilience & moral clarity

opus

Control vs acceptance

council-machiavelli

Machiavelli

Power dynamics & realpolitik

sonnet

How actors actually behave

council-lao-tzu

Lao Tzu

Non-action & emergence

opus

When less is more

council-feynman

Feynman

First-principles debugging

sonnet

Refuses unexplained complexity

council-torvalds

Linus Torvalds

Pragmatic engineering

sonnet

Ship it or shut up

council-musashi

Miyamoto Musashi

Strategic timing

sonnet

The decisive strike

council-watts

Alan Watts

Perspective & reframing

opus

Dissolves false problems

council-karpathy

Andrej Karpathy

Neural network intuition

sonnet

How models actually learn and fail

council-sutskever

Ilya Sutskever

Scaling frontier & AI safety

opus

When capability becomes risk

council-kahneman

Daniel Kahneman

Cognitive bias & decision science

opus

Your own thinking is the first error

council-meadows

Donella Meadows

Systems thinking & feedback loops

sonnet

Redesign the system, not the symptom

council-munger

Charlie Munger

Multi-model reasoning & economics

sonnet

Invert — what guarantees failure?

council-taleb

Nassim Taleb

Antifragility & tail risk

opus

Design for the tail, not the average

council-rams

Dieter Rams

User-centered design

sonnet

Less, but better — the user decides

Polarity Pairs
 — members are chosen as deliberate counterweights

* Socrates vs Feynman— Destroys top-down vs rebuilds bottom-up
* Aristotle vs Lao Tzu— Classifies everything vs structure IS the problem
* Sun Tzu vs Aurelius— Wins external games vs governs the internal one
* Ada vs Machiavelli— Formal purity vs messy human incentives
* Torvalds vs Watts— Ships concrete solutions vs questions whether the problem exists
* Musashi vs Torvalds— Waits for the perfect moment vs ships it now
* Karpathy vs Sutskever— Build it, observe it, iterate vs pause, research, ensure safety first
* Karpathy vs Ada— Empirical ML intuition vs formal systems theory
* Kahneman vs Feynman— Your cognition is the first error vs trust first-principles reasoning
* Meadows vs Torvalds— Redesign the feedback loop vs fix the symptom and ship
* Munger vs Aristotle— Multi-model lattice vs single taxonomic system
* Taleb vs Karpathy— Hidden catastrophic tails vs smooth empirical scaling curves
* Rams vs Ada— What the user needs vs what computation can do

## Three Deliberation Modes

### Full Mode (default)

3-round structured deliberation: independent analysis → cross-examination → final positions.

/council Should we open-source our agent framework?
/council --triad strategy What's our competitive moat?
/council --full What is the right pricing model?

### Quick Mode (--quick)

2-round rapid analysis for simpler decisions. No cross-examination.

/council --quick Should we add caching here?
/council --quick --triad shipping Should we release today?

### Duo Mode (--duo)

2-member dialectic using polarity pairs. Great for exploring tensions.

/council --duo Should we use microservices or monolith?
/council --duo --members torvalds,ada Is this abstraction worth it?

Pre-defined Triads
 — 20 domain-specific 3-member combinations

Domain

Triad

Rationale

architecture

Aristotle + Ada + Feynman

Classify + formalize + simplicity-test

strategy

Sun Tzu + Machiavelli + Aurelius

Terrain + incentives + moral grounding

ethics

Aurelius + Socrates + Lao Tzu

Duty + questioning + natural order

debugging

Feynman + Socrates + Ada

Bottom-up + assumption testing + formal verification

innovation

Ada + Lao Tzu + Aristotle

Abstraction + emergence + classification

conflict

Socrates + Machiavelli + Aurelius

Expose + predict + ground

complexity

Lao Tzu + Aristotle + Ada

Emergence + categories + formalism

risk

Sun Tzu + Aurelius + Feynman

Threats + resilience + empirical verification

shipping

Torvalds + Musashi + Feynman

Pragmatism + timing + first-principles

product

Torvalds + Machiavelli + Watts

Ship it + incentives + reframing

founder

Musashi + Sun Tzu + Torvalds

Timing + terrain + engineering reality

ai

Karpathy + Sutskever + Ada

Empirical ML + scaling frontier + formal limits

ai-product

Karpathy + Torvalds + Machiavelli

ML capability + shipping pragmatism + incentives

ai-safety

Sutskever + Aurelius + Socrates

Safety frontier + moral clarity + assumption destruction

decision

Kahneman + Munger + Aurelius

Bias detection + inversion + moral clarity

systems

Meadows + Lao Tzu + Aristotle

Feedback loops + emergence + categories

uncertainty

Taleb + Sun Tzu + Sutskever

Tail risk + terrain + scaling frontier

design

Rams + Torvalds + Watts

User clarity + maintainability + reframing

economics

Munger + Machiavelli + Sun Tzu

Models + incentives + competition

bias

Kahneman + Socrates + Watts

Cognitive bias + assumption destruction + frame audit

Council Profiles
 — pre-built panels for different needs

### classic(default)

All 18 members with domain triads above. Best for broad deliberation.

### exploration-orthogonal

12-member panel for discovery and "unknown unknowns" reduction:

* Socrates, Feynman, Sun Tzu, Machiavelli, Ada, Lao Tzu, Aurelius, Torvalds, Karpathy, Sutskever, Kahneman, Meadows
* Profile triads:unknowns,market-entry,system-design,reframing,ai-frontier,blind-spots

### execution-lean

5-member panel for fast decision-to-action:

* Torvalds, Feynman, Sun Tzu, Aurelius, Ada
* Profile triads:ship-now,launch-strategy,stability

## Multi-Provider Auto-Routing

The council automatically detects installed LLM providers and distributes members across them for genuine model diversity — zero config required.

/council --triad decision Should we accept this acquisition offer?

Supported providers(auto-detected):

Provider

CLI

Exec Method

Anthropic (Claude)

native

subagent (always available)

OpenAI

codex

codex exec

Google

gemini

gemini -p

Ollama (local)

ollama

ollama run

NVIDIA NIM

NVIDIA_API_KEY
 env

openai_compatible_api

Cursor

cursor-agent

cursor-agent -p

NVIDIA NIM (build.nvidia.com) exposes 130+ open-weight models (DeepSeek, Kimi, MiniMax, GLM, Qwen, Nemotron) via an OpenAI-compatible endpoint. Free tier: 1,000 credits, 40 RPM. Detection requires onlyexport NVIDIA_API_KEY=nvapi-...— no CLI binary needed. Seeconfigs/provider-model-slots.nim.example.yamlfor a sample seat allocation.

Cursor CLI (cursor.com/cli) is a modelaggregator— one binary (cursor-agent) serves GPT-5.x, Claude, Gemini, and Grok families through a singleCURSOR_API_KEY(orcursor-agent login). Members route via headless read-only mode (cursor-agent -p --mode ask --model <id>). Install withcurl https://cursor.com/install -fsS | bash. Because Cursor can serveclaude-*models, pickcross-familyCursor models (e.g.gpt-5.4-high,gemini-2.5-pro,grok-4) when a seat needs to add diversity rather than duplicate Anthropic bias. List live IDs withcursor-agent --list-models. Seeconfigs/provider-model-slots.cursor.example.yamlfor a sample seat allocation.

How routing works:

1. Polarity pairs are separated across providers (hard constraint)
2. Members spread evenly across available providers
3. Per-memberprovider_affinityin frontmatter used as tiebreaker
4. If any provider fails, automatic fallback to Claude

Flags:

* --no-auto-route— disable auto-routing, use Claude-only defaults
* --dry-route— print the routing table without running the council
* --models [path]— manual override with YAML config (seeconfigs/provider-model-slots.example.yaml)

## Deliberation Protocol

Full mode runs 7 steps: provider routing → problem restate gate → independent analysis → cross-examination → enforcement scan → final positions → verdict synthesis. Verdicts lead with what the council doesn't know.

Full protocol details

### Full Mode (7 steps)

1. Provider Detection & Routing— auto-detect providers, assign members
2. Problem Restate Gate— each member restates the problem + provides an alternative framing before analysis begins
3. Round 1: Independent Analysis (blind-first)— all members analyze in parallel (400 words max)
4. Round 2: Cross-Examination— members challenge each other (300 words, must engage 2+ others)
5. Post-Round Enforcement— dissent quota, novelty gate, agreement check, anti-recursion (single pass)
6. Round 3: Final Crystallization— 100-word position statements
7. Verdict Synthesis— leads with Unresolved Questions and Recommended Next Steps

### Quick Mode

1. Problem Restate + Rapid Analysis— reframe + analyze in parallel (200 words max)
2. Final Positions— 75-word crystallization

### Duo Mode

1. Problem Restate + Opening Positions— reframe + state positions (300 words)
2. Direct Response— engage opponent's claims (200 words)
3. Final Statements— 50-word positions

### Enforcement Mechanisms

* Bounded protocol is the forcing function— deliberation runs a fixed round budget (full 3 / quick 2 / duo 3), so it cannot loop. Anti-recursion guards (the "hemlock rule" caps Socrates' questioning; any pair exceeding 2 messages is cut off) enforce the bound mid-round.
* Dissent quota + novelty gate + counterfactual pass prevent premature convergence
* Tie-breaking is a counted tally, not a prose impression— each member emits a structuredSTANCE:line in the final round; consensus requires adomain-weighted 2/3 majority(the on-domain seat carries 1.5×, designatedbeforepositions exist). A genuine split is escalated to the user with the full tally rather than forced into false consensus.
* All verdicts include a Vote Tally and a Follow-Up section for outcome tracking

## Installation

Installs 18 council agents plus skill files for Claude and/or Codex.

./install.sh 
#
 Claude install (default)

./install.sh --codex 
#
 Claude + Codex skill install

./install.sh --codex-only 
#
 Codex-only install

./install.sh --claude-dir /path/to/.claude 
#
 Non-default Claude config directory

./install.sh --codex-dir /path/to/.codex 
#
 Non-default Codex config directory

./install.sh --dry-run 
#
 Preview without writing

./install.sh --copy-configs 
#
 Also install model routing templates

Restart your target client(s) after installing. Run./scripts/council-simulation-checklist.shto validate. Try thedemo session packto test all modes.

## Requirements

* Claude CodeCLI (required for Claude usage)
* Codex(required for Codex skill usage)
* Agent/subagent support in your client (enabled by default)

Optional providers(auto-detected for multi-provider routing):

* Codex CLI(OpenAI) —npm i -g @openai/codex
* Gemini CLI(Google) — seegemini-cli repo
* Ollama(local models) — install from ollama.com
* Cursor CLI(GPT/Claude/Gemini/Grok aggregator) —curl https://cursor.com/install -fsS | bash

## Contributing

Contributions welcome. Read thecontribution guidelinesfirst.

## Support the Project

If you find this project useful, consider supporting my open-source work.

Solana donations

BYLu8XD8hGDUtdRBWpGWu5HKoiPrWqCxYFSh4oxXuvPg

## License

To the extent possible under law, the authors have waived all copyright and
related or neighboring rights to this work.

## About

18 AI personas deliberate your hardest decisions across multiple LLM providers. Aristotle, Feynman, Kahneman, Torvalds & more — structured multi-round deliberation with genuine model diversity. One command: /council

### Topics

 decision-making

 gemini

 openai

 ai-agents

 claude

 deliberation

 prompt-engineering

 ollama

 multi-llm

 claude-code

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

1.8k

 stars
 

### Watchers

11

 watching
 

### Forks

194

 forks
 

 Report repository

 

## Releases2

v1.1.0

 Latest

 

May 21, 2026

 

+ 1 release

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Shell100.0%