---
title: 'GitHub - garrytan/gstack: Use Garry Tan''s exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA · GitHub'
url: https://github.com/garrytan/gstack
site_name: github
content_file: github-github-garrytangstack-use-garry-tans-exact-claude
fetched_at: '2026-05-14T11:37:01.783511'
original_url: https://github.com/garrytan/gstack
author: garrytan
description: 'Use Garry Tan''s exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA - garrytan/gstack'
---

garrytan

 

/

gstack

Public

* NotificationsYou must be signed in to change notification settings
* Fork14.3k
* Star96.2k

 
 
 
 
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

275 Commits
275 Commits
.github
.github
 
 
agents
agents
 
 
autoplan
autoplan
 
 
benchmark-models
benchmark-models
 
 
benchmark
benchmark
 
 
bin
bin
 
 
browse
browse
 
 
browser-skills/
hackernews-frontpage
browser-skills/
hackernews-frontpage
 
 
canary
canary
 
 
careful
careful
 
 
claude
claude
 
 
codex
codex
 
 
context-restore
context-restore
 
 
context-save
context-save
 
 
contrib/
add-host
contrib/
add-host
 
 
cso
cso
 
 
design-consultation
design-consultation
 
 
design-html
design-html
 
 
design-review
design-review
 
 
design-shotgun
design-shotgun
 
 
design
design
 
 
devex-review
devex-review
 
 
docs
docs
 
 
document-release
document-release
 
 
extension
extension
 
 
freeze
freeze
 
 
gstack-upgrade
gstack-upgrade
 
 
gstack
gstack
 
 
guard
guard
 
 
health
health
 
 
hosts
hosts
 
 
investigate
investigate
 
 
land-and-deploy
land-and-deploy
 
 
landing-report
landing-report
 
 
learn
learn
 
 
lib
lib
 
 
make-pdf
make-pdf
 
 
model-overlays
model-overlays
 
 
office-hours
office-hours
 
 
open-gstack-browser
open-gstack-browser
 
 
openclaw
openclaw
 
 
pair-agent
pair-agent
 
 
plan-ceo-review
plan-ceo-review
 
 
plan-design-review
plan-design-review
 
 
plan-devex-review
plan-devex-review
 
 
plan-eng-review
plan-eng-review
 
 
plan-tune
plan-tune
 
 
qa-only
qa-only
 
 
qa
qa
 
 
retro
retro
 
 
review
review
 
 
scrape
scrape
 
 
scripts
scripts
 
 
setup-browser-cookies
setup-browser-cookies
 
 
setup-deploy
setup-deploy
 
 
setup-gbrain
setup-gbrain
 
 
ship
ship
 
 
skillify
skillify
 
 
supabase
supabase
 
 
sync-gbrain
sync-gbrain
 
 
test
test
 
 
unfreeze
unfreeze
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitlab-ci.yml
.gitlab-ci.yml
 
 
AGENTS.md
AGENTS.md
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
BROWSER.md
BROWSER.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DESIGN.md
DESIGN.md
 
 
ETHOS.md
ETHOS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SKILL.md
SKILL.md
 
 
SKILL.md.tmpl
SKILL.md.tmpl
 
 
TODOS.md
TODOS.md
 
 
USING_GBRAIN_WITH_GSTACK.md
USING_GBRAIN_WITH_GSTACK.md
 
 
VERSION
VERSION
 
 
actionlint.yaml
actionlint.yaml
 
 
bun.lock
bun.lock
 
 
conductor.json
conductor.json
 
 
connect-chrome
connect-chrome
 
 
package.json
package.json
 
 
setup
setup
 
 
slop-scan.config.json
slop-scan.config.json
 
 
View all files

## Repository files navigation

# gstack

"I don't think I've typed like a line of code probably since December, basically, which is an extremely large change." —Andrej Karpathy, No Priors podcast, March 2026

When I heard Karpathy say this, I wanted to find out how. How does one person ship like a team of twenty? Peter Steinberger builtOpenClaw— 247K GitHub stars — essentially solo with AI agents. The revolution is here. A single builder with the right tooling can move faster than a traditional team.

I'mGarry Tan, President & CEO ofY Combinator. I've worked with thousands of startups — Coinbase, Instacart, Rippling — when they were one or two people in a garage. Before YC, I was one of the first eng/PM/designers at Palantir, cofounded Posterous (sold to Twitter), and built Bookface, YC's internal social network.

gstack is my answer.I've been building products for twenty years, and right now I'm shipping more products than I ever have. In the last 60 days: 3 production services, 40+ shipped features, part-time, while running YC full-time. On logical code change — not raw LOC, which AI inflates — my 2026 run rate is~810× my 2013 pace(11,417 vs 14 logical lines/day). Year-to-date (through April 18), 2026 has already produced240× the entire 2013 year. Measured across 40 public + privategarrytan/*repos including Bookface, after excluding one demo repo. AI wrote most of it. The point isn't who typed it, it's what shipped.

The LOC critics aren't wrong that raw line counts inflate with AI. They are wrong that normalized-for-inflation, I'm less productive. I'm more productive, by a lot. Full methodology, caveats, and reproduction script:On the LOC Controversy.

2026 — 1,237 contributions and counting:

2013 — when I built Bookface at YC (772 contributions):

Same person. Different era. The difference is the tooling.

gstack is how I do it.It turns Claude Code into a virtual engineering team — a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production bugs, a QA lead who opens a real browser, a security officer who runs OWASP + STRIDE audits, and a release engineer who ships the PR. Twenty-three specialists and eight power tools, all slash commands, all Markdown, all free, MIT license.

This is my open source software factory. I use it every day. I'm sharing it because these tools should be available to everyone.

Fork it. Improve it. Make it yours. And if you want to hate on free open source software — you're welcome to, but I'd rather you just try it first.

Who this is for:

* Founders and CEOs— especially technical ones who still want to ship
* First-time Claude Code users— structured roles instead of a blank prompt
* Tech leads and staff engineers— rigorous review, QA, and release automation on every PR

## Quick start

1. Install gstack (30 seconds — see below)
2. Run/office-hours— describe what you're building
3. Run/plan-ceo-reviewon any feature idea
4. Run/reviewon any branch with changes
5. Run/qaon your staging URL
6. Stop there. You'll know if this is for you.

## Install — 30 seconds

Requirements:Claude Code,Git,Bunv1.0+,Node.js(Windows only)

### Step 1: Install on your machine

Open Claude Code and paste this. Claude does the rest.

Install gstack: rungit clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setupthen add a "gstack" section to CLAUDE.md that says to use the /browse skill from gstack for all web browsing, never use mcp__claude-in-chrome__* tools, and lists the available skills: /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review, /design-consultation, /design-shotgun, /design-html, /review, /ship, /land-and-deploy, /canary, /benchmark, /browse, /connect-chrome, /qa, /qa-only, /design-review, /setup-browser-cookies, /setup-deploy, /setup-gbrain, /retro, /investigate, /document-release, /codex, /cso, /autoplan, /plan-devex-review, /devex-review, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade, /learn. Then ask the user if they also want to add gstack to the current project so teammates get it.

### Step 2: Team mode — auto-update for shared repos (recommended)

From inside your repo, paste this. Switches you to team mode, bootstraps the repo so teammates get gstack automatically, and commits the change:

(cd 
~
/.claude/skills/gstack 
&&
 ./setup --team) 
&&
 
~
/.claude/skills/gstack/bin/gstack-team-init required 
&&
 git add .claude/ CLAUDE.md 
&&
 git commit -m 
"
require gstack for AI-assisted work
"

No vendored files in your repo, no version drift, no manual upgrades. Every Claude Code session starts with a fast auto-update check (throttled to once/hour, network-failure-safe, completely silent).

Swaprequiredforoptionalif you'd rather nudge teammates than block them.

### OpenClaw

OpenClaw spawns Claude Code sessions via ACP, so every gstack skill just works
when Claude Code has gstack installed. Paste this to your OpenClaw agent:

Install gstack: rungit clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setupto install gstack for Claude Code. Then add a "Coding Tasks" section to AGENTS.md that says: when spawning Claude Code sessions for coding work, tell the session to use gstack skills. Include these examples — security audit: "Load gstack. Run /cso", code review: "Load gstack. Run /review", QA test a URL: "Load gstack. Run /qa https://...", build a feature end-to-end: "Load gstack. Run /autoplan, implement the plan, then run /ship", plan before building: "Load gstack. Run /office-hours then /autoplan. Save the plan, don't implement."

After setup, just talk to your OpenClaw agent naturally:

You say

What happens

"Fix the typo in README"

Simple — Claude Code session, no gstack needed

"Run a security audit on this repo"

Spawns Claude Code with 
Run /cso

"Build me a notifications feature"

Spawns Claude Code with /autoplan → implement → /ship

"Help me plan the v2 API redesign"

Spawns Claude Code with /office-hours → /autoplan, saves plan

Seedocs/OPENCLAW.mdfor advanced dispatch routing and
the gstack-lite/gstack-full prompt templates.

### Native OpenClaw Skills (via ClawHub)

Four methodology skills that work directly in your OpenClaw agent, no Claude Code
session needed. Install from ClawHub:

clawhub install gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro

Skill

What it does

gstack-openclaw-office-hours

Product interrogation with 6 forcing questions

gstack-openclaw-ceo-review

Strategic challenge with 4 scope modes

gstack-openclaw-investigate

Root cause debugging methodology

gstack-openclaw-retro

Weekly engineering retrospective

These are conversational skills. Your OpenClaw agent runs them directly via chat.

### Other AI Agents

gstack works on 10 AI coding agents, not just Claude. Setup auto-detects which
agents you have installed:

git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git 
~
/gstack

cd
 
~
/gstack 
&&
 ./setup

Or target a specific agent with./setup --host <name>:

Agent

Flag

Skills install to

OpenAI Codex CLI

--host codex

~/.codex/skills/gstack-*/

OpenCode

--host opencode

~/.config/opencode/skills/gstack-*/

Cursor

--host cursor

~/.cursor/skills/gstack-*/

Factory Droid

--host factory

~/.factory/skills/gstack-*/

Slate

--host slate

~/.slate/skills/gstack-*/

Kiro

--host kiro

~/.kiro/skills/gstack-*/

Hermes

--host hermes

~/.hermes/skills/gstack-*/

GBrain (mod)

--host gbrain

~/.gbrain/skills/gstack-*/

Want to add support for another agent?Seedocs/ADDING_A_HOST.md.
It's one TypeScript config file, zero code changes.

## See it work

You: I want to build a daily briefing app for my calendar.
You: /office-hours
Claude: [asks about the pain — specific examples, not hypotheticals]

You: Multiple Google calendars, events with stale info, wrong locations.
 Prep takes forever and the results aren't good enough...

Claude: I'm going to push back on the framing. You said "daily briefing
 app." But what you actually described is a personal chief of
 staff AI.
 [extracts 5 capabilities you didn't realize you were describing]
 [challenges 4 premises — you agree, disagree, or adjust]
 [generates 3 implementation approaches with effort estimates]
 RECOMMENDATION: Ship the narrowest wedge tomorrow, learn from
 real usage. The full vision is a 3-month project — start with
 the daily briefing that actually works.
 [writes design doc → feeds into downstream skills automatically]

You: /plan-ceo-review
 [reads the design doc, challenges scope, runs 10-section review]

You: /plan-eng-review
 [ASCII diagrams for data flow, state machines, error paths]
 [test matrix, failure modes, security concerns]

You: Approve plan. Exit plan mode.
 [writes 2,400 lines across 11 files. ~8 minutes.]

You: /review
 [AUTO-FIXED] 2 issues. [ASK] Race condition → you approve fix.

You: /qa https://staging.myapp.com
 [opens real browser, clicks through flows, finds and fixes a bug]

You: /ship
 Tests: 42 → 51 (+9 new). PR: github.com/you/app/pull/42

You said "daily briefing app." The agent said "you're building a chief of staff AI" — because it listened to your pain, not your feature request. Eight commands, end to end. That is not a copilot. That is a team.

## The sprint

gstack is a process, not a collection of tools. The skills run in the order a sprint runs:

Think → Plan → Build → Review → Test → Ship → Reflect

Each skill feeds into the next./office-hourswrites a design doc that/plan-ceo-reviewreads./plan-eng-reviewwrites a test plan that/qapicks up./reviewcatches bugs that/shipverifies are fixed. Nothing falls through the cracks because every step knows what came before it.

Skill

Your specialist

What they do

/office-hours

YC Office Hours

Start here. Six forcing questions that reframe your product before you write code. Pushes back on your framing, challenges premises, generates implementation alternatives. Design doc feeds into every downstream skill.

/plan-ceo-review

CEO / Founder

Rethink the problem. Find the 10-star product hiding inside the request. Four modes: Expansion, Selective Expansion, Hold Scope, Reduction.

/plan-eng-review

Eng Manager

Lock in architecture, data flow, diagrams, edge cases, and tests. Forces hidden assumptions into the open.

/plan-design-review

Senior Designer

Rates each design dimension 0-10, explains what a 10 looks like, then edits the plan to get there. AI Slop detection. Interactive — one AskUserQuestion per design choice.

/plan-devex-review

Developer Experience Lead

Interactive DX review: explores developer personas, benchmarks against competitors' TTHW, designs your magical moment, traces friction points step by step. Three modes: DX EXPANSION, DX POLISH, DX TRIAGE. 20-45 forcing questions.

/design-consultation

Design Partner

Build a complete design system from scratch. Researches the landscape, proposes creative risks, generates realistic product mockups.

/review

Staff Engineer

Find the bugs that pass CI but blow up in production. Auto-fixes the obvious ones. Flags completeness gaps.

/investigate

Debugger

Systematic root-cause debugging. Iron Law: no fixes without investigation. Traces data flow, tests hypotheses, stops after 3 failed fixes.

/design-review

Designer Who Codes

Same audit as /plan-design-review, then fixes what it finds. Atomic commits, before/after screenshots.

/devex-review

DX Tester

Live developer experience audit. Actually tests your onboarding: navigates docs, tries the getting started flow, times TTHW, screenshots errors. Compares against 
/plan-devex-review
 scores — the boomerang that shows if your plan matched reality.

/design-shotgun

Design Explorer

"Show me options." Generates 4-6 AI mockup variants, opens a comparison board in your browser, collects your feedback, and iterates. Taste memory learns what you like. Repeat until you love something, then hand it to 
/design-html
.

/design-html

Design Engineer

Turn a mockup into production HTML that actually works. Pretext computed layout: text reflows, heights adjust, layouts are dynamic. 30KB, zero deps. Detects React/Svelte/Vue. Smart API routing per design type (landing page vs dashboard vs form). The output is shippable, not a demo.

/qa

QA Lead

Test your app, find bugs, fix them with atomic commits, re-verify. Auto-generates regression tests for every fix.

/qa-only

QA Reporter

Same methodology as /qa but report only. Pure bug report without code changes.

/pair-agent

Multi-Agent Coordinator

Share your browser with any AI agent. One command, one paste, connected. Works with OpenClaw, Hermes, Codex, Cursor, or anything that can curl. Each agent gets its own tab. Auto-launches headed mode so you watch everything. Auto-starts ngrok tunnel for remote agents. Scoped tokens, tab isolation, rate limiting, activity attribution.

/cso

Chief Security Officer

OWASP Top 10 + STRIDE threat model. Zero-noise: 17 false positive exclusions, 8/10+ confidence gate, independent finding verification. Each finding includes a concrete exploit scenario.

/ship

Release Engineer

Sync main, run tests, audit coverage, push, open PR. Bootstraps test frameworks if you don't have one.

/land-and-deploy

Release Engineer

Merge the PR, wait for CI and deploy, verify production health. One command from "approved" to "verified in production."

/canary

SRE

Post-deploy monitoring loop. Watches for console errors, performance regressions, and page failures.

/benchmark

Performance Engineer

Baseline page load times, Core Web Vitals, and resource sizes. Compare before/after on every PR.

/document-release

Technical Writer

Update all project docs to match what you just shipped. Catches stale READMEs automatically.

/retro

Eng Manager

Team-aware weekly retro. Per-person breakdowns, shipping streaks, test health trends, growth opportunities. 
/retro global
 runs across all your projects and AI tools (Claude Code, Codex, Gemini).

/browse

QA Engineer

Give the agent eyes. Real Chromium browser, real clicks, real screenshots. ~100ms per command. 
/open-gstack-browser
 launches GStack Browser with sidebar, anti-bot stealth, and auto model routing.

/setup-browser-cookies

Session Manager

Import cookies from your real browser (Chrome, Arc, Brave, Edge) into the headless session. Test authenticated pages.

/autoplan

Review Pipeline

One command, fully reviewed plan. Runs CEO → design → eng review automatically with encoded decision principles. Surfaces only taste decisions for your approval.

/learn

Memory

Manage what gstack learned across sessions. Review, search, prune, and export project-specific patterns, pitfalls, and preferences. Learnings compound across sessions so gstack gets smarter on your codebase over time.

### Which review should I use?

Building for...

Plan stage (before code)

Live audit (after shipping)

End users
 (UI, web app, mobile)

/plan-design-review

/design-review

Developers
 (API, CLI, SDK, docs)

/plan-devex-review

/devex-review

Architecture
 (data flow, perf, tests)

/plan-eng-review

/review

All of the above

/autoplan
 (runs CEO → design → eng → DX, auto-detects which apply)

—

### Power tools

Skill

What it does

/codex

Second Opinion
 — independent code review from OpenAI Codex CLI. Three modes: review (pass/fail gate), adversarial challenge, and open consultation. Cross-model analysis when both 
/review
 and 
/codex
 have run.

/careful

Safety Guardrails
 — warns before destructive commands (rm -rf, DROP TABLE, force-push). Say "be careful" to activate. Override any warning.

/freeze

Edit Lock
 — restrict file edits to one directory. Prevents accidental changes outside scope while debugging.

/guard

Full Safety
 — 
/careful
 + 
/freeze
 in one command. Maximum safety for prod work.

/unfreeze

Unlock
 — remove the 
/freeze
 boundary.

/open-gstack-browser

GStack Browser
 — launch GStack Browser with sidebar, anti-bot stealth, auto model routing (Sonnet for actions, Opus for analysis), one-click cookie import, and Claude Code integration. Clean up pages, take smart screenshots, edit CSS, and pass info back to your terminal.

/setup-deploy

Deploy Configurator
 — one-time setup for 
/land-and-deploy
. Detects your platform, production URL, and deploy commands.

/setup-gbrain

GBrain Onboarding
 — from zero to running gbrain in under 5 minutes. PGLite local, Supabase existing URL, or auto-provision a new Supabase project via Management API. MCP registration for Claude Code + per-repo trust triad (read-write/read-only/deny). 
Full guide
.

/sync-gbrain

Keep Brain Current
 — re-index this repo's code into gbrain via 
gbrain sources add
 + 
gbrain sync --strategy code
, refresh the 
## GBrain Search Guidance
 block in CLAUDE.md, and auto-remove guidance when the capability check fails. 
--incremental
 (default), 
--full
, 
--dry-run
. Idempotent; safe to re-run.

/gstack-upgrade

Self-Updater
 — upgrade gstack to latest. Detects global vs vendored install, syncs both, shows what changed.

### New binaries (v0.19)

Beyond the slash-command skills, gstack ships standalone CLIs for workflows that don't belong inside a session:

Command

What it does

gstack-model-benchmark

Cross-model benchmark
 — run the same prompt through Claude, GPT (via Codex CLI), and Gemini; compare latency, tokens, cost, and (optionally) LLM-judge quality score. Auth detected per provider, unavailable providers skip cleanly. Output as table, JSON, or markdown. 
--dry-run
 validates flags + auth without spending API calls.

gstack-taste-update

Design taste learning
 — writes approvals and rejections from 
/design-shotgun
 into a persistent per-project taste profile. Decays 5%/week. Feeds back into future variant generation so the system learns what you actually pick.

### Continuous checkpoint mode (opt-in, local by default)

Setgstack-config set checkpoint_mode continuousand skills auto-commit your work as you go with aWIP:prefix plus a structured[gstack-context]body (decisions, remaining work, failed approaches). Survives crashes and context switches./context-restorereads those commits to reconstruct session state./shipfilter-squashes WIP commits before the PR (preserving non-WIP commits) so bisect stays clean. Push is opt-in viacheckpoint_push=true— default is local-only so you don't trigger CI on every WIP commit.

### Domain skills + raw CDP escape hatch

Two new browser primitives compound the gstack agent over time:

* $B domain-skill save— agent saves a per-site note (e.g., "LinkedIn's Apply button lives in an iframe") that fires automatically next time it visits that hostname. Quarantined → active after 3 successful uses → optional cross-project promotion via$B domain-skill promote-to-global. Storage lives alongside/learn's per-project learnings file. Full reference:docs/domain-skills.md.
* $B cdp <Domain.method>— raw Chrome DevTools Protocol escape hatch for the rare case curated commands miss. Deny-default: methods must be explicitly added tobrowse/src/cdp-allowlist.tswith a one-line justification. Two-tier mutex serializes browser-scoped CDP calls against per-tab work. Output for data-exfil methods is wrapped in the UNTRUSTED envelope.

Want raw CDP with no rails, no allowlist, no daemon — just thin transport from agent to Chrome?browser-use/browser-harness-jsis a different philosophy (agent-authored helpers vs gstack's curated commands) and a good fit if you don't want gstack's security stack. The two can coexist: gstack's$B cdpand harness can both attach to the same Chrome via Playwright'snewCDPSession.

Deep dives with examples and philosophy for every skill →

### Karpathy's four failure modes? Already covered.

Andrej Karpathy'sAI coding rules(17K stars) nail four failure modes: wrong assumptions, overcomplexity, orthogonal edits, imperative over declarative. gstack's workflow skills enforce all four./office-hoursforces assumptions into the open before code is written. The Confusion Protocol stops Claude from guessing on architectural decisions./reviewcatches unnecessary complexity and drive-by edits./shiptransforms tasks into verifiable goals with test-first execution. If you already use Karpathy-style CLAUDE.md rules, gstack is the workflow enforcement layer that makes them stick across entire sprints, not just single prompts.

## Parallel sprints

gstack works well with one sprint. It gets interesting with ten running at once.

Design is at the heart./design-consultationbuilds your design system from scratch, researches what's out there, proposes creative risks, and writesDESIGN.md. But the real magic is the shotgun-to-HTML pipeline.

/design-shotgunis how you explore.You describe what you want. It generates 4-6 AI mockup variants using GPT Image. Then it opens a comparison board in your browser with all variants side by side. You pick favorites, leave feedback ("more whitespace", "bolder headline", "lose the gradient"), and it generates a new round. Repeat until you love something. Taste memory kicks in after a few rounds so it starts biasing toward what you actually like. No more describing your vision in words and hoping the AI gets it. You see options, pick the good ones, and iterate visually.

/design-htmlmakes it real.Take that approved mockup (from/design-shotgun, a CEO plan, a design review, or just a description) and turn it into production-quality HTML/CSS. Not the kind of AI HTML that looks fine at one viewport width and breaks everywhere else. This uses Pretext for computed text layout: text actually reflows on resize, heights adjust to content, layouts are dynamic. 30KB overhead, zero dependencies. It detects your framework (React, Svelte, Vue) and outputs the right format. Smart API routing picks different Pretext patterns depending on whether it's a landing page, dashboard, form, or card layout. The output is something you'd actually ship, not a demo.

/qawas a massive unlock.It let me go from 6 to 12 parallel workers. Claude Code saying"I SEE THE ISSUE"and then actually fixing it, generating a regression test, and verifying the fix — that changed how I work. The agent has eyes now.

Smart review routing.Just like at a well-run startup: CEO doesn't have to look at infra bug fixes, design review isn't needed for backend changes. gstack tracks what reviews are run, figures out what's appropriate, and just does the smart thing. The Review Readiness Dashboard tells you where you stand before you ship.

Test everything./shipbootstraps test frameworks from scratch if your project doesn't have one. Every/shiprun produces a coverage audit. Every/qabug fix generates a regression test. 100% test coverage is the goal — tests make vibe coding safe instead of yolo coding.

/document-releaseis the engineer you never had.It reads every doc file in your project, cross-references the diff, and updates everything that drifted. README, ARCHITECTURE, CONTRIBUTING, CLAUDE.md, TODOS — all kept current automatically. And now/shipauto-invokes it — docs stay current without an extra command.

Real browser mode./open-gstack-browserlaunches GStack Browser, an AI-controlled Chromium with anti-bot stealth, custom branding, and the sidebar extension baked in. Sites like Google and NYTimes work without captchas. The menu bar says "GStack Browser" instead of "Chrome for Testing." Your regular Chrome stays untouched. All existing browse commands work unchanged.$B disconnectreturns to headless. The browser stays alive as long as the window is open... no idle timeout killing it while you're working.

Sidebar agent — your AI browser assistant.Type natural language in the Chrome side panel and a child Claude instance executes it. "Navigate to the settings page and screenshot it." "Fill out this form with test data." "Go through every item in this list and extract the prices." The sidebar auto-routes to the right model: Sonnet for fast actions (click, navigate, screenshot) and Opus for reading and analysis. Each task gets up to 5 minutes. The sidebar agent runs in an isolated session, so it won't interfere with your main Claude Code window. One-click cookie import right from the sidebar footer.

Personal automation.The sidebar agent isn't just for dev workflows. Example: "Browse my kid's school parent portal and add all the other parents' names, phone numbers, and photos to my Google Contacts." Two ways to get authenticated: (1) log in once in the headed browser, your session persists, or (2) click the "cookies" button in the sidebar footer to import cookies from your real Chrome. Once authenticated, Claude navigates the directory, extracts the data, and creates the contacts.

Prompt injection defense.Hostile web pages try to hijack your sidebar agent. gstack ships a layered defense: a 22MB ML classifier bundled with the browser scans every page and tool output locally, a Claude Haiku transcript check votes on the full conversation shape, a random canary token in the system prompt catches session exfil attempts across text, tool args, URLs, and file writes, and a verdict combiner requires two classifiers to agree before blocking (prevents single-model false positives on Stack Overflow-style instruction pages). A shield icon in the sidebar header shows status (green/amber/red). Opt in to a 721MB DeBERTa-v3 ensemble viaGSTACK_SECURITY_ENSEMBLE=debertafor 2-of-3 agreement. Emergency kill switch:GSTACK_SECURITY_OFF=1. SeeARCHITECTURE.mdfor the full stack.

Browser handoff when the AI gets stuck.Hit a CAPTCHA, auth wall, or MFA prompt?$B handoffopens a visible Chrome at the exact same page with all your cookies and tabs intact. Solve the problem, tell Claude you're done,$B resumepicks up right where it left off. The agent even suggests it automatically after 3 consecutive failures.

/pair-agentis cross-agent coordination.You're in Claude Code. You also have OpenClaw running. Or Hermes. Or Codex. You want them both looking at the same website. Type/pair-agent, pick your agent, and a GStack Browser window opens so you can watch. The skill prints a block of instructions. Paste that block into the other agent's chat. It exchanges a one-time setup key for a session token, creates its own tab, and starts browsing. You see both agents working in the same browser, each in their own tab, neither able to interfere with the other. If ngrok is installed, the tunnel starts automatically so the other agent can be on a completely different machine. Same-machine agents get a zero-friction shortcut that writes credentials directly. This is the first time AI agents from different vendors can coordinate through a shared browser with real security: scoped tokens, tab isolation, rate limiting, domain restrictions, and activity attribution.

Multi-AI second opinion./codexgets an independent review from OpenAI's Codex CLI — a completely different AI looking at the same diff. Three modes: code review with a pass/fail gate, adversarial challenge that actively tries to break your code, and open consultation with session continuity. When both/review(Claude) and/codex(OpenAI) have reviewed the same branch, you get a cross-model analysis showing which findings overlap and which are unique to each.

Safety guardrails on demand.Say "be careful" and/carefulwarns before any destructive command — rm -rf, DROP TABLE, force-push, git reset --hard./freezelocks edits to one directory while debugging so Claude can't accidentally "fix" unrelated code./guardactivates both./investigateauto-freezes to the module being investigated.

Proactive skill suggestions.gstack notices what stage you're in — brainstorming, reviewing, debugging, testing — and suggests the right skill. Don't like it? Say "stop suggesting" and it remembers across sessions.

## 10-15 parallel sprints

gstack is powerful with one sprint. It is transformative with ten running at once.

Conductorruns multiple Claude Code sessions in parallel — each in its own isolated workspace. One session running/office-hourson a new idea, another doing/reviewon a PR, a third implementing a feature, a fourth running/qaon staging, and six more on other branches. All at the same time. I regularly run 10-15 parallel sprints — that's the practical max right now.

The sprint structure is what makes parallelism work. Without a process, ten agents is ten sources of chaos. With a process — think, plan, build, review, test, ship — each agent knows exactly what to do and when to stop. You manage them the way a CEO manages a team: check in on the decisions that matter, let the rest run.

### Voice input (AquaVoice, Whisper, etc.)

gstack skills have voice-friendly trigger phrases. Say what you want naturally —
"run a security check", "test the website", "do an engineering review" — and the
right skill activates. You don't need to remember slash command names or acronyms.

## Uninstall

### Option 1: Run the uninstall script

If gstack is installed on your machine:

~
/.claude/skills/gstack/bin/gstack-uninstall

This handles skills, symlinks, global state (~/.gstack/), project-local state, browse daemons, and temp files. Use--keep-stateto preserve config and analytics. Use--forceto skip confirmation.

### Option 2: Manual removal (no local repo)

If you don't have the repo cloned (e.g. you installed via a Claude Code paste and later deleted the clone):

#
 1. Stop browse daemons

pkill -f 
"
gstack.*browse
"
 
2>
/dev/null 
||
 
true

#
 2. Remove per-skill directories whose SKILL.md points into gstack/

find 
~
/.claude/skills -mindepth 1 -maxdepth 1 -type d 
!
 -name gstack 
2>
/dev/null 
|

while
 IFS= 
read
 -r dir
;
 
do

 link=
"
$dir
/SKILL.md
"

 [ 
-L
 
"
$link
"
 ] 
||
 
continue

 target=
$(
readlink 
"
$link
"
 
2>
/dev/null
)
 
||
 
continue

 
case
 
"
$target
"
 
in

 gstack/
*
|
*
/gstack/
*
)
 rm -f 
"
$link
"

 rmdir 
"
$dir
"
 
2>
/dev/null 
||
 
true

 ;;
 
esac

done

#
 3. Remove gstack

rm -rf 
~
/.claude/skills/gstack

#
 4. Remove global state

rm -rf 
~
/.gstack

#
 5. Remove integrations (skip any you never installed)

rm -rf 
~
/.codex/skills/gstack
*
 
2>
/dev/null
rm -rf 
~
/.factory/skills/gstack
*
 
2>
/dev/null
rm -rf 
~
/.kiro/skills/gstack
*
 
2>
/dev/null
rm -rf 
~
/.openclaw/skills/gstack
*
 
2>
/dev/null

#
 6. Remove temp files

rm -f /tmp/gstack-
*
 
2>
/dev/null

#
 7. Per-project cleanup (run from each project root)

rm -rf .gstack .gstack-worktrees .claude/skills/gstack 
2>
/dev/null
rm -rf .agents/skills/gstack
*
 .factory/skills/gstack
*
 
2>
/dev/null

### Clean up CLAUDE.md

The uninstall script does not edit CLAUDE.md. In each project where gstack was added, remove the## gstackand## Skill routingsections.

### Playwright

~/Library/Caches/ms-playwright/(macOS) is left in place because other tools may share it. Remove it if nothing else needs it.

Free, MIT licensed, open source. No premium tier, no waitlist.

I open sourced how I build software. You can fork it and make it your own.

We're hiring.Want to ship real products at AI-coding speed and help harden gstack?
Come work at YC —ycombinator.com/softwareExtremely competitive salary and equity. San Francisco, Dogpatch District.

## GBrain — persistent knowledge for your coding agent

GBrainis a persistent knowledge base for AI agents — think of it as the memory your agent actually keeps between sessions. GStack gives you a one-command path from zero to "it's running, my agent can call it."

/setup-gbrain

Three paths, pick one:

* Supabase, existing URL— your cloud agent already provisioned a brain; paste the Session Pooler URL, now this laptop uses the same data.
* Supabase, auto-provision— paste a Supabase Personal Access Token; the skill creates a new project, polls to healthy, fetches the pooler URL, hands it togbrain init. ~90 seconds end-to-end.
* PGLite local— zero accounts, zero network, ~30 seconds. Isolated brain on this Mac only. Great for try-first; migrate to Supabase later with/setup-gbrain --switch.

After init, the skill offers to register gbrain as an MCP server for Claude Code (claude mcp add gbrain -- gbrain serve) sogbrain search,gbrain put_page, etc. show up as first-class typed tools — not bash shell-outs.

Keeping the brain current.Run/sync-gbrainfrom any repo to re-index its code into gbrain (incremental by default,--fullfor a full reindex,--dry-runto preview). The skill registers the cwd as a federated source viagbrain sources add, runsgbrain sync --strategy code, and writes a## GBrain Search Guidanceblock to your project's CLAUDE.md so the agent prefersgbrain search/code-def/code-refsover Grep. The block is removed automatically if the capability check fails — no stale guidance pointing at tools that aren't installed.

Per-remote trust policy.Each repo on your machine gets one of three tiers:

* read-write— agent can search the brain AND write new pages back from this repo
* read-only— agent can search but never writes (best for multi-client consultants: search the shared brain, don't contaminate it with Client A's work while in Client B's repo)
* deny— no gbrain interaction at all

The skill asks once per repo. The decision is sticky across worktrees and branches of the same remote.

GStack memory sync (different feature, same private-repo infra).Optionally pushes your gstack state (learnings, CEO plans, design docs, retros, developer profile) to a private git repo so your memory follows you across machines, with a one-time privacy prompt (everything allowlisted / artifacts only / off) and a defense-in-depth secret scanner that blocks AWS keys, tokens, PEM blocks, and JWTs before they leave your machine.

gstack-brain-init

Full monty — every scenario, every flag, every bin helper, every troubleshooting step:USING_GBRAIN_WITH_GSTACK.md

Other references:docs/gbrain-sync.md(sync-specific guide) •docs/gbrain-sync-errors.md(error index)

## Docs

Doc

What it covers

Skill Deep Dives

Philosophy, examples, and workflow for every skill (includes Greptile integration)

Builder Ethos

Builder philosophy: Boil the Lake, Search Before Building, three layers of knowledge

Using GBrain with GStack

Every path, flag, bin helper, and troubleshooting step for 
/setup-gbrain

GBrain Sync

Cross-machine memory setup, privacy modes, troubleshooting

Architecture

Design decisions and system internals

Browser Reference

Full command reference for 
/browse

Contributing

Dev setup, testing, contributor mode, and dev mode

Changelog

What's new in every version

## Privacy & Telemetry

gstack includesopt-inusage telemetry to help improve the project. Here's exactly what happens:

* Default is off.Nothing is sent anywhere unless you explicitly say yes.
* On first run,gstack asks if you want to share anonymous usage data. You can say no.
* What's sent (if you opt in):skill name, duration, success/fail, gstack version, OS. That's it.
* What's never sent:code, file paths, repo names, branch names, prompts, or any user-generated content.
* Change anytime:gstack-config set telemetry offdisables everything instantly.

Data is stored inSupabase(open source Firebase alternative). The schema is insupabase/migrations/— you can verify exactly what's collected. The Supabase publishable key in the repo is a public key (like a Firebase API key) — row-level security policies deny all direct access. Telemetry flows through validated edge functions that enforce schema checks, event type allowlists, and field length limits.

Local analytics are always available.Rungstack-analyticsto see your personal usage dashboard from the local JSONL file — no remote data needed.

## Troubleshooting

Skill not showing up?cd ~/.claude/skills/gstack && ./setup

/browsefails?cd ~/.claude/skills/gstack && bun install && bun run build

Stale install?Run/gstack-upgrade— or setauto_upgrade: truein~/.gstack/config.yaml

Want shorter commands?cd ~/.claude/skills/gstack && ./setup --no-prefix— switches from/gstack-qato/qa. Your choice is remembered for future upgrades.

Want namespaced commands?cd ~/.claude/skills/gstack && ./setup --prefix— switches from/qato/gstack-qa. Useful if you run other skill packs alongside gstack.

Codex says "Skipped loading skill(s) due to invalid SKILL.md"?Your Codex skill descriptions are stale. Fix:cd ~/.codex/skills/gstack && git pull && ./setup --host codex— or for repo-local installs:cd "$(readlink -f .agents/skills/gstack)" && git pull && ./setup --host codex

Windows users:gstack works on Windows 11 via Git Bash or WSL. Node.js is required in addition to Bun — Bun has a known bug with Playwright's pipe transport on Windows (bun#4253). The browse server automatically falls back to Node.js. Make sure bothbunandnodeare on your PATH.

Claude says it can't see the skills?Make sure your project'sCLAUDE.mdhas a gstack section. Add this:

## gstack
Use /browse from gstack for all web browsing. Never use mcp__claude-in-chrome__* tools.
Available skills: /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review,
/design-consultation, /design-shotgun, /design-html, /review, /ship, /land-and-deploy,
/canary, /benchmark, /browse, /open-gstack-browser, /qa, /qa-only, /design-review,
/setup-browser-cookies, /setup-deploy, /setup-gbrain, /sync-gbrain, /retro, /investigate, /document-release,
/codex, /cso, /autoplan, /pair-agent, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade, /learn.

## License

MIT. Free forever. Go build something.

## About

Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

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

96.2k

 stars
 

### Watchers

589

 watching
 

### Forks

14.3k

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

 

 

## Languages

* TypeScript77.2%
* Go Template13.6%
* Shell6.3%
* JavaScript1.8%
* Other1.1%