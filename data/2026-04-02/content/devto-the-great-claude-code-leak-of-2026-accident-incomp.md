---
title: 'The Great Claude Code Leak of 2026: Accident, Incompetence, or the Best PR Stunt in AI History? - DEV Community'
url: https://dev.to/varshithvhegde/the-great-claude-code-leak-of-2026-accident-incompetence-or-the-best-pr-stunt-in-ai-history-3igm
site_name: devto
content_file: devto-the-great-claude-code-leak-of-2026-accident-incomp
fetched_at: '2026-04-02T01:01:19.658565'
original_url: https://dev.to/varshithvhegde/the-great-claude-code-leak-of-2026-accident-incompetence-or-the-best-pr-stunt-in-ai-history-3igm
author: Varshith V Hegde
date: '2026-04-01'
description: 'TL;DR: On March 31, 2026, Anthropic accidentally shipped the entire source code of Claude Code to the... Tagged with webdev, ai, programming, productivity.'
tags: '#webdev, #ai, #programming, #productivity'
---

TL;DR:On March 31, 2026, Anthropic accidentally shipped theentire source codeof Claude Code to the public npm registry via a single misconfigured debug file. 512,000 lines. 1,906 TypeScript files. 44 hidden feature flags. A Tamagotchi pet. And one very uncomfortable question: was it really an accident?

## 1. What Actually Happened

### The Root Cause: One Missing Line in.npmignore

This is both the most embarrassing and most instructive part of the story. Let me walk through the technical chain of events.

When you publish a JavaScript/TypeScript package to npm, your build toolchain (Webpack, esbuild, Bun, etc.) optionally generatessource map files, which have a.mapextension. Their entire purpose is debugging: they bridge the gap between the minified, bundled production code and your original readable source. When a crash happens, a source map lets the stack trace point to your actual TypeScript file at line 47 rather thanmain.js:1:284729.

Source maps are strictly for internal debugging. They should never ship to users.

The way you exclude them from npm packages is with an.npmignorefile, or afilesfield inpackage.json. Here's the mistake in plain English:

# What Claude Code's .npmignore should have had:

*
.map
dist/
*
.map

# What it apparently had:

# (nothing about .map files)

Enter fullscreen mode

Exit fullscreen mode

That's it. That's the whole disaster.

But it gets worse. The source map didn't contain the source code directly. Itreferencedit, pointing to a URL of a.zipfile hosted on Anthropic's own Cloudflare R2 storage bucket. A publicly accessible one, with no authentication required.

So the full chain looked like this:

npm install @anthropic-ai/claude-code
 → downloads package including main.js.map (59.8 MB)
 → .map file contains URL pointing to src.zip
 → src.zip is hosted publicly on Anthropic's R2 bucket
 → anyone can download and unzip 512,000 lines of TypeScript

Enter fullscreen mode

Exit fullscreen mode

Two separate configuration failures, stacked on top of each other.

As software engineer Gabriel Anhaia put it in hisdeep dive: "A single misconfigured.npmignoreorfilesfield inpackage.jsoncan expose everything."

### The Bun Factor

There's a third layer. Anthropic acquired theBun JavaScript runtimeat the end of 2025, and Claude Code is built on top of it. A known Bun bug (issue #28001, filed on March 11, 2026) reports that source maps are served in production builds even when the documentation says they shouldn't be.

The bug was open for 20 days before this happened. Nobody caught it. Anthropic's own acquired toolchain contributed to exposing Anthropic's own product.

## 2. The Timeline

00:21 UTC — March 31, 2026
Malicious axios versions (1.14.1 / 0.30.4) appear on npm
with an embedded Remote Access Trojan. Unrelated to Anthropic,
but catastrophically bad timing.

~04:00 UTC
Claude Code v2.1.88 is pushed to npm. The 59.8 MB source map
ships with it. The R2 bucket containing all source code is live
and publicly accessible.

04:23 UTC
Chaofan Shou (@Fried_rice), an intern at Solayer Labs,
tweets the discovery with a direct download link.
16 million people descend on the thread.

Next 2 hours
GitHub repositories spring up. The fastest repo in history
to hit 50,000 stars does it in under 2 hours.
41,500+ forks proliferate. DMCA requests begin.

~08:00 UTC
Anthropic pulls the npm package from the registry.
Issues the "human error, not a security breach" statement
to VentureBeat, The Register, CNBC, Fortune, Axios, Decrypt.

Same day
A Python clean-room rewrite appears, legally DMCA-proof.
Decentralized mirrors on Gitlawb go live with the message:
"Will never be taken down."
The code is permanently in the wild.

Enter fullscreen mode

Exit fullscreen mode

### By the Numbers

Metric

Value

Lines of code exposed

512,000+

TypeScript files

1,906

Source map file size

59.8 MB

GitHub forks (peak)

41,500+

Stars on fastest repo

50,000 in 2 hours

Hidden feature flags

44

Claude Code ARR

$2.5 billion

Anthropic total ARR

$19 billion

Views on original tweet

16 million

## 3. SECURITY ALERT: The axios RAT

Stop. Read this before anything else if you updated Claude Code that morning.

Coinciding with the leak, but entirely unrelated to it, was a real supply chain attack on npm. Malicious versions of the widely-usedaxiosHTTP library were published:

* axios@1.14.1
* axios@0.30.4

Both contain an embeddedRemote Access Trojan (RAT). The malicious dependency is calledplain-crypto-js.

If you rannpm installor updated Claude Code between 00:21 UTC and 03:29 UTC on March 31, 2026:

# Check your lockfiles immediately:

grep
 
-r
 
"1.14.1
\|
0.30.4
\|
plain-crypto-js"
 package-lock.json

grep
 
-r
 
"1.14.1
\|
0.30.4
\|
plain-crypto-js"
 yarn.lock

grep
 
-r
 
"1.14.1
\|
0.30.4
\|
plain-crypto-js"
 bun.lockb

Enter fullscreen mode

Exit fullscreen mode

If you find a match:

1. Treat the machine as fully compromised
2. Rotate all credentials, API keys, and secrets immediately
3. Perform a clean OS reinstallation
4. File incident reports for any organizational data

Going forward, Anthropic has designated theNative Installeras the recommended installation method:

curl 
-fsSL
 https://claude.ai/install.sh | bash

Enter fullscreen mode

Exit fullscreen mode

The native installer uses a standalone binary that doesn't rely on the npm dependency chain.

## 4. What Was Inside: The Full Breakdown

The leaked codebase is thesrc/directory of Claude Code, the "agentic harness" that wraps the underlying Claude model and gives it the ability to use tools, manage files, run bash commands, and orchestrate multi-agent workflows. This is not the model weights (those weren't exposed), but in many ways this ismorestrategically valuable.

### The Architecture

The Tool System (~40 tools, ~29,000 lines)

Claude Code isn't a chat wrapper. It's a plugin-style architecture where every capability is a discrete, permission-gated tool:

* BashTool— shell command execution with safety guards
* FileReadTool,FileWriteTool,FileEditTool
* WebFetchTool— live web access
* LSPTool— Language Server Protocol integration for IDE features
* GlobTool,GrepTool— codebase search
* NotebookReadTool,NotebookEditTool— Jupyter support
* MultiEditTool— atomic multi-file edits
* TodoReadTool,TodoWriteTool— task tracking

Each tool has its own permission model, validation logic, and output formatting. The base tool definition alone spans 29,000 lines.

The Query Engine (46,000 lines)

Labeled "the brain of the operation" in Gabriel Anhaia'sanalysis. It handles all LLM API calls and response streaming, token caching and context management, multi-agent orchestration, and retry logic.

The Memory Architecture

This is what competitors will study most carefully. Anthropic built a solution to "context entropy," the tendency for long-running AI sessions to degrade into hallucination as the context grows. Their answer is a three-layer memory system:

Layer 1: MEMORY.md
 → A lightweight index of pointers (~150 chars per entry)
 → Always loaded in context
 → Stores LOCATIONS, not data

Layer 2: Topic Files
 → Actual project knowledge, fetched on-demand
 → Never fully in context simultaneously

Layer 3: Raw Transcripts
 → Never re-read fully
 → Only grep'd for specific identifiers when needed

Enter fullscreen mode

Exit fullscreen mode

The key insight is what they callStrict Write Discipline. The agent can only update its memory index after a confirmed successful file write. This prevents the agent from polluting its context with failed attempts. The agent also treats its own memory as a "hint" and verifies facts against the actual codebase before acting, rather than trusting its stored beliefs.

## 5. Hidden Features Anthropic Never Meant to Ship

### KAIROS: Always-On Autonomous Agent

KAIROS (from the Ancient Greek for "the right moment") is mentioned 150+ times in the source. It's an unreleased autonomous background daemon mode that runs background sessions while you're idle, executes a process calledautoDreamfor nightly memory consolidation, merges disparate observations, removes logical contradictions, and converts vague insights into verified facts. It also has a specialBriefoutput mode designed for a persistent assistant and access to tools regular Claude Code doesn't have.

Think of it as Claude Code actively maintaining its understanding of your project while you sleep, not just sitting there waiting.

### ULTRAPLAN: 30-Minute Remote Planning Sessions

ULTRAPLAN offloads a complex planning task to a remote Cloud Container Runtime (CCR) session running Opus, gives it up to 30 minutes to think, and lets you approve the result from your phone or browser. When approved, a special sentinel value__ULTRAPLAN_TELEPORT_LOCAL__brings the result back to your local terminal. Remote cloud-powered reasoning, delivered locally.

### Coordinator Mode: Multi-Agent Orchestration

One Claude spawning and managing multiple worker Claude agents in parallel. The Coordinator handles task distribution, result aggregation, and conflicts between worker outputs. It's infrastructure for AI teams, not just AI assistants.

### BUDDY: The Part Nobody Expected

The most talked-about find, not for its strategic implications but because it's genuinely fun.

buddy/companion.tsimplements a full Tamagotchi-style AI pet that lives in a speech bubble next to your terminal input.

Species (18 total, hidden via String.fromCharCode() arrays):
duck, dragon, axolotl, capybara, mushroom, ghost, nebulynx...

Rarity tiers:
Common > Uncommon > Rare > Epic > Legendary
1% shiny chance, independent of rarity

Stats:
DEBUGGING / PATIENCE / CHAOS / WISDOM / SNARK

Determined by:
Mulberry32 PRNG seeded from your userId hash + salt 'friend-2026-401'
(Same user always gets the same buddy species -- deterministic)

Enter fullscreen mode

Exit fullscreen mode

Claude generates a custom name and personality description for your buddy on first hatch. There are sprite animations and a floating heart effect. The planned rollout window in the source code:April 1-7, 2026.

Someone at Anthropic is clearly having a very good time.

### Anti-Distillation: Poisoning Competitor Training Data

Inclaude.ts(lines 301-313), a flag calledANTI_DISTILLATION_CC, when enabled, sendsanti_distillation: ['fake_tools']in API requests. This tells the server to inject decoy tool definitions into the system prompt. The idea: if a competitor is recording Claude Code's API traffic to train their own model, the fake tool definitions corrupt that training data.

There's a second mechanism inbetas.ts(lines 279-298): server-side connector-text summarization. When enabled, the API buffers the assistant's reasoning between tool calls, returns only summaries, and cryptographically signs them. Competitors recording traffic get the summaries, not the full reasoning chain.

As Alex Kimnotes in his analysis: "Anyone serious about distilling from Claude Code traffic would find the workarounds in about an hour of reading the source. The real protection is probably legal, not technical."

### Frustration Detection via Regex

Found inuserPromptKeywords.ts:

/
\
b
(
wtf
|
wth
|
ffs
|
omfg
|
shit
(
ty
|
tiest
)?
|
dumbass
|
horrible
|
awful
|

piss
(
ed
|
ing
)?
 
off
|
piece
 
of 
(
shit
|
crap
|
junk
)
|
what
 
the 
(
fuck
|
hell
)
|

fucking
?
 
(
broken
|
useless
|
terrible
|
awful
|
horrible
)
|
fuck
 
you
|

screw 
(
this
|
you
)
|
so
 
frustrating
|
this
 
sucks
|
damn
 
it
)
\
b
/

Enter fullscreen mode

Exit fullscreen mode

A multi-billion-dollar AI company is detecting user frustration with a regex. The Hacker News thread lost it. To be fair though, it's faster, cheaper, and more predictable than running an LLM inference every time to check if the user is angry at the tool.

### 250,000 Wasted API Calls Per Day

The most candid internal admission in the entire codebase. FromautoCompact.ts(lines 68-70):

"BQ 2026-03-10: 1,279 sessions had 50+ consecutive failures 
(up to 3,272) in a single session, wasting ~250K API calls/day globally."

Enter fullscreen mode

Exit fullscreen mode

The fix was three lines:MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES = 3. After 3 consecutive compaction failures, it just stops trying. Sometimes good engineering is knowing when to give up.

## 6. The "Capybara" Model Confirmed

The leak didn't expose Claude's model weights, but it did expose multiple references to Anthropic's next major model family. Internal codenames:Capybara(also referred to asMythosin a separate leaked document from the prior week).

The beta flags in the source reference specific API version strings for Capybara, suggesting it's well beyond concept stage. Security researcher Roy Paz from LayerX Security, who reviewed the code for Fortune, indicated it will likely ship in fast and slow variants with a significantly larger context window than anything currently on the market.

These references also confirmed the existence ofundercover.ts, a module that actively instructs Claude Code to never mention internal codenames like "Capybara" or "Tengu" when used in external repositories. There's a hard-codedNO force-OFF— you can force Undercover Mode on, but you cannot force it off. In external builds, the function gets dead-code-eliminated entirely.

The implication raised in theHacker News thread: AI-authored commits from Anthropic employees in open source repos will have no indication an AI wrote them. The tool actively conceals its own involvement.

## 7. Alternative Theory: Was This Anthropic's PR Play?

I'm not saying I believe this. I'm saying the circumstantial evidence is strange enough that it deserves to be stated clearly.

Anthropic is the self-proclaimed "safety-first AI lab." They're racing for developer mindshare against OpenAI (better brand) and Google (better distribution). Claude Code is their breakout product. They're preparing for an IPO. And they'd just made themselves unpopular with the developer community ten days earlier by sending legal threats to OpenCode for using their internal APIs.

So let's look at what this "leak" actually did for Anthropic.

Exhibit A: The April Fools' Timing

The leak occurred on March 31, the day before April 1st. The Buddy/companion system had a planned rollout window of April 1-7 coded directly into the source. The "leak" gave developers a sneak peek at what was about to launch anyway. Was this a controlled preview dressed up as an accident?

Exhibit B: The Bun Bug Nobody Fixed

Anthropic acquired Bun. They own the runtime. The bug causing source maps to ship in production was filed 20 days before the leak and was still open. If you own the runtime and its bug tracker, and that bug causes your own code to leak... why hadn't anyone internally marked it as critical?

Exhibit C: The Undercover Mode Irony

Claude Code has an entire subsystem called Undercover Mode, purpose-built to prevent internal codenames from leaking through AI-generated content. They built AI-powered leak prevention into the product. Then humans accidentally shipped the entire source code. The gap between their AI safety engineering and their human release engineering is either tragic or theatrical.

Exhibit D: The OpenCode Reputation Reversal

Ten days before the leak, Anthropic sent cease-and-desist letters to OpenCode, a popular third-party tool. The developer community was furious. The narrative was "Anthropic is acting like a gatekeeping megacorp."

Then a "leak" happens that shows Anthropic's impressive engineering to the world, makes them look like the underdog, generates three days of breathless coverage about KAIROS, BUDDY, and ULTRAPLAN, and completely reversed developer sentiment. Within 48 hours, developers went from "Anthropic sucks" to "holy shit look what Anthropic is building."

Exhibit E: The Permanent Mirror Problem

Anthropic filed DMCA takedowns. GitHub complied immediately. But the decentralized mirror at Gitlawb, with a public message saying "Will never be taken down," has been live since day one. Anthropic has a legal team, deep pockets, and relationships. A serious legal effort could make life difficult for every mirror operator. They chose not to go that hard.

Exhibit F: The "Second Leak in a Week" Pattern

This wasn't Anthropic's first incident that week. A draft blog post about the Capybara/Mythos model had "accidentally" been publicly accessible just days before, as Fortune reported on Thursday. Two high-profile "leaks" in five days, both generating enormous excitement about Anthropic's upcoming roadmap, both very conveniently timed.

### The Counter-Arguments (Why It's Probably Just Incompetence)

To be fair:

Strategic roadmap exposure is genuinely damaging.Cursor, Copilot, and Windsurf now know exactly what Anthropic has already built and what's nearly ready to ship. That's real competitive intelligence permanently in the public domain.

The IPO narrative cuts both ways."We shipped our source code to npm" is not a line you want in your S-1.

The axios RAT timing.Nobody would engineer a PR stunt to overlap with an active malware attack on npm. That part made a bad news day significantly worse for anyone who updated Claude Code that morning, and there's no upside to being associated with a supply chain attack.

The most likely answer is plain human error. A misconfigured.npmignore. A known Bun bug nobody had marked as critical. A public R2 bucket that should have been private. Three configuration failures that compounded into a disaster.

The PR outcome though? Undeniably good. The strategic damage? Real but survivable. The timing? Genuinely strange.

Draw your own conclusions.

## 8. Why DMCA Won't Fix This

DMCA takedowns work on centralized platforms. GitHub complied within hours. But the code spread to places that are harder to reach.

Gitlawb, with its explicit "Will never be taken down" message, operates outside the DMCA's practical reach. The Python port that appeared the same day wasdeclared DMCA-proofby The Pragmatic Engineer's Gergely Orosz, who noted the rewrite is a new creative work that violates no copyright. There's also the AI copyright question: Anthropic's own CEO has implied that significant portions of Claude Code were written by Claude. The DC Circuit upheld in March 2025 that AI-generated work doesn't carry automatic copyright. If Anthropic's copyright claim over Claude-authored code is legally murky, the entire takedown strategy weakens.

And then there are torrents. Content once on the internet at scale doesn't come back.

The practical reality: 512,000 lines of Claude Code are permanently in the wild, regardless of what any court decides.

## 9. What This Means For You

If you're using Claude Code:Update immediately past v2.1.88 and use the native installer going forward (curl -fsSL https://claude.ai/install.sh | bash). If you updated via npm between 00:21 and 03:29 UTC on March 31, do the axios/RAT check above.

If you're building AI coding tools:The leaked source is now the most detailed public documentation of how to build a production-grade AI agent harness that exists. The three-layer memory architecture, the permission system, the tool plugin design, the multi-agent coordination patterns. It's all there, already analyzed by thousands of developers. The bar for what "production-grade" means just got documented in detail.

If you're at Anthropic:The code is out. KAIROS, ULTRAPLAN, and BUDDY are already built. Ship them. The community already knows they're coming. Turn the leak into a launch.

## 10. Lessons for Every Dev Team

This incident is a clear example of how release pipeline failures compound. Regardless of your opinion on Anthropic, every team should run through this checklist:

# 1. Audit your .npmignore / package.json "files" field

cat
 .npmignore

# Do you explicitly exclude *.map, dist/*.map, *.d.ts.map?

# 2. Check if source maps ship in your production build

ls 
dist/ | 
grep
 
"
\.
map$"

# If you see anything: your bundler config needs review

# 3. Audit your cloud storage permissions

# Are any buckets referenced in your build artifacts publicly accessible?

# 4. Check your build toolchain for known bugs

# If you're on Bun, check issue #28001 status

# 5. Review your npm publish workflow

npm pack 
--dry-run

# Review EVERY file that would be published before actually publishing

Enter fullscreen mode

Exit fullscreen mode

The line that came out of the Hacker News thread:"Your .npmignore is load-bearing. Treat it like a security boundary."

## Conclusion

Here's what we know for certain: a misconfigured.npmignoreand a public cloud storage bucket exposed 512,000 lines of Claude Code, the code spread instantly and is now permanently in the wild, the leak revealed a technically impressive product with a compelling feature roadmap, and Anthropic's brand among developers bounced back remarkably fast.

What we'll probably never know: whether anyone inside Anthropic saw the Bun bug and made a judgment call, whether the April Fools' timing of the BUDDY rollout was coincidence, and whether Anthropic's relative restraint on DMCA enforcement is legal strategy or resource allocation.

What's not in question is that the engineering inside Claude Code is genuinely impressive. The memory architecture, the anti-distillation mechanisms, the multi-agent coordination, the DRM-at-the-HTTP-layer attestation. This is a serious piece of software doing things that are actually hard.

Accident or not, the world now knows what Anthropic is capable of building.

And maybe that was the point.

## References

Source

Link

Alex Kim's technical deep-dive

alex000kim.com

VentureBeat — Full breakdown + axios RAT warning

venturebeat.com

The Register — Anthropic's official statement

theregister.com

Fortune — Strategic analysis + Capybara confirmation

fortune.com

Decrypt — DMCA analysis + permanent mirror situation

decrypt.co

CNBC — Revenue figures + company response

cnbc.com

Axios — Feature flag breakdown + roadmap analysis

axios.com

DEV.to (Gabriel Anhaia) — Architecture walkthrough

dev.to

Kuberwastaken/claude-code GitHub

github.com

Hacker News thread

news.ycombinator.com

Bun bug #28001

github.com/oven-sh/bun

CyberSecurityNews — Supply chain attack details

cybersecuritynews.com

If this was useful, drop a reaction. If you spot anything I got wrong, leave it in the comments.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse