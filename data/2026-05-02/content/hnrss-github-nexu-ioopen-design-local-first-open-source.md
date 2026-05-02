---
title: 'GitHub - nexu-io/open-design: 🎨 Local-first, open-source alternative to Anthropic''s Claude Design. ⚡ 19 Skills · ✨ 71 brand-grade Design Systems 🖼 Generate web · desktop · mobile prototypes · slides · images · videos · HyperFrames 📦 Sandboxed preview · HTML/PDF/PPTX/MP4 export 🤖 Runs on Claude Code / Codex / Cursor / Gemini / OpenCode / Qwen / Copilot / Hermes / Kimi CLI. · GitHub'
url: https://github.com/nexu-io/open-design
site_name: hnrss
content_file: hnrss-github-nexu-ioopen-design-local-first-open-source
fetched_at: '2026-05-02T19:55:25.764368'
original_url: https://github.com/nexu-io/open-design
date: '2026-05-02'
description: 🎨 Local-first, open-source alternative to Anthropic's Claude Design. ⚡ 19 Skills · ✨ 71 brand-grade Design Systems 🖼 Generate web · desktop · mobile prototypes · slides · images · videos · HyperFrames 📦 Sandboxed preview · HTML/PDF/PPTX/MP4 export 🤖 Runs on Claude Code / Codex / Cursor / Gemini / OpenCode / Qwen / Copilot / Hermes / Kimi CLI. - nexu-io/open-design
tags:
- hackernews
- hnrss
---

nexu-io

 

/

open-design

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.7k
* Star15.4k

 
 
 
 
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

152 Commits
152 Commits
.github
.github
 
 
apps
apps
 
 
assets
assets
 
 
craft
craft
 
 
design-systems
design-systems
 
 
docs
docs
 
 
e2e
e2e
 
 
packages
packages
 
 
prompt-templates
prompt-templates
 
 
scripts
scripts
 
 
skills
skills
 
 
specs
specs
 
 
story
story
 
 
templates
templates
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.de.md
CONTRIBUTING.de.md
 
 
CONTRIBUTING.ja-JP.md
CONTRIBUTING.ja-JP.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTING.zh-CN.md
CONTRIBUTING.zh-CN.md
 
 
LICENSE
LICENSE
 
 
QUICKSTART.de.md
QUICKSTART.de.md
 
 
QUICKSTART.ja-JP.md
QUICKSTART.ja-JP.md
 
 
QUICKSTART.md
QUICKSTART.md
 
 
README.de.md
README.de.md
 
 
README.ja-JP.md
README.ja-JP.md
 
 
README.ko.md
README.ko.md
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
README.zh-TW.md
README.zh-TW.md
 
 
TRANSLATIONS.md
TRANSLATIONS.md
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
vercel.json
vercel.json
 
 
View all files

## Repository files navigation

# Open Design

The open-source alternative toClaude Design.Local-first, web-deployable, BYOK at every layer —12 coding-agent CLIsauto-detected on yourPATH(Claude Code, Codex, Devin for Terminal, Cursor Agent, Gemini CLI, OpenCode, Qwen, GitHub Copilot CLI, Hermes, Kimi, Pi, Kiro) become the design engine, driven by31 composable Skillsand72 brand-grade Design Systems. No CLI? An OpenAI-compatible BYOK proxy is the same loop minus the spawn.

English·Deutsch·简体中文·繁體中文·한국어·日本語

## Why this exists

Anthropic'sClaude Design(released 2026-04-17, Opus 4.7) showed what happens when an LLM stops writing prose and starts shipping design artifacts. It went viral — and stayed closed-source, paid-only, cloud-only, locked to Anthropic's model and Anthropic's skills. There is no checkout, no self-host, no Vercel deploy, no swap-in-your-own-agent.

Open Design (OD) is the open-source alternative.Same loop, same artifact-first mental model, none of the lock-in. We don't ship an agent — the strongest coding agents already live on your laptop. We wire them into a skill-driven design workflow that runs locally withpnpm tools-dev, can deploy the web layer to Vercel, and stays BYOK at every layer.

Typemake me a magazine-style pitch deck for our seed round. The interactive question form pops up before the model improvises a single pixel. The agent picks one of five curated visual directions. A liveTodoWriteplan streams into the UI. The daemon builds a real on-disk project folder with a seed template, layout library, and self-check checklist. The agent reads them — pre-flight enforced — runs a five-dimensional critique against its own output, and emits a single<artifact>that renders in a sandboxed iframe seconds later.

That's not "AI tries to design something". That's an AI that has been trained, by the prompt stack, to behave like a senior designer with a working filesystem, a deterministic palette library, and a checklist culture — exactly the bar Claude Design set, but open and yours.

OD stands on four open-source shoulders:

* alchaincyf/huashu-design— the design-philosophy compass. Junior-Designer workflow, the 5-step brand-asset protocol, the anti-AI-slop checklist, the 5-dimensional self-critique, and the "5 schools × 20 design philosophies" idea behind our direction picker — all distilled intoapps/web/src/prompts/discovery.ts.
* op7418/guizang-ppt-skill— the deck mode. Bundled verbatim underskills/guizang-ppt/with original LICENSE preserved; magazine-style layouts, WebGL hero, P0/P1/P2 checklists.
* OpenCoworkAI/open-codesign— the UX north star and our closest peer. The first open-source Claude-Design alternative. We borrow its streaming-artifact loop, its sandboxed-iframe preview pattern (vendored React 18 + Babel), its live agent panel (todos + tool calls + interruptible generation), and its five-format export list (HTML / PDF / PPTX / ZIP / Markdown). We deliberately diverge on form factor — they are a desktop Electron app bundlingpi-ai; we are a web app + local daemon that delegates to your existing CLI.
* multica-ai/multica— the daemon-and-runtime architecture. PATH-scan agent detection, the local daemon as the only privileged process, the agent-as-teammate worldview.

## At a glance

What you get

Coding-agent CLIs (12)

Claude Code · Codex CLI · Devin for Terminal · Cursor Agent · Gemini CLI · OpenCode · Qwen Code · GitHub Copilot CLI · Hermes (ACP) · Kimi CLI (ACP) · Pi (RPC) · Kiro CLI (ACP) — auto-detected on 
PATH
, swap with one click

BYOK fallback

OpenAI-compatible proxy at 
/api/proxy/stream
 — paste 
baseUrl
 + 
apiKey
 + 
model
 and any vendor (Anthropic-via-OpenAI, DeepSeek, Groq, MiMo, OpenRouter, your self-hosted vLLM, or any other OpenAI-compatible provider) becomes the engine. Internal-IP/SSRF blocked at the daemon edge.

Design systems built-in

129
 — 2 hand-authored starters + 70 product systems (Linear, Stripe, Vercel, Airbnb, Tesla, Notion, Anthropic, Apple, Cursor, Supabase, Figma, Xiaohongshu, …) from 
awesome-design-md
, plus 57 design skills from 
awesome-design-skills
 added directly under 
design-systems/

Skills built-in

31
 — 27 in 
prototype
 mode (web-prototype, saas-landing, dashboard, mobile-app, gamified-app, social-carousel, magazine-poster, dating-web, sprite-animation, motion-frames, critique, tweaks, wireframe-sketch, pm-spec, eng-runbook, finance-report, hr-onboarding, invoice, kanban-board, team-okrs, …) + 4 in 
deck
 mode (
guizang-ppt
 · 
simple-deck
 · 
replit-deck
 · 
weekly-update
). Grouped in the picker by 
scenario
: design / marketing / operation / engineering / product / finance / hr / sale / personal.

Media generation

Image · video · audio surfaces ship alongside the design loop. 
gpt-image-2
 (Azure / OpenAI) for posters, avatars, infographics, illustrated maps · 
Seedance 2.0
 (ByteDance) for cinematic 15s text-to-video and image-to-video · 
HyperFrames
 (
heygen-com/hyperframes
) for HTML→MP4 motion graphics (product reveals, kinetic typography, data charts, social overlays, logo outros). 
93
 ready-to-replicate prompts gallery — 43 gpt-image-2 + 39 Seedance + 11 HyperFrames — under 
prompt-templates/
, with preview thumbnails and source attribution. Same chat surface as code; outputs a real 
.mp4
 / 
.png
 chip into the project workspace.

Visual directions

5 curated schools (Editorial Monocle · Modern Minimal · Warm Soft · Tech Utility · Brutalist Experimental) — each ships a deterministic OKLch palette + font stack (
apps/web/src/prompts/directions.ts
)

Device frames

iPhone 15 Pro · Pixel · iPad Pro · MacBook · Browser Chrome — pixel-accurate, shared across skills under 
assets/frames/

Agent runtime

Local daemon spawns the CLI in your project folder — agent gets real 
Read
, 
Write
, 
Bash
, 
WebFetch
 against a real on-disk environment, with Windows 
ENAMETOOLONG
 fallbacks (stdin / prompt-file) on every adapter

Imports

Drop a 
Claude Design
 export ZIP onto the welcome dialog — 
POST /api/import/claude-design
 parses it into a real project so your agent can keep editing where Anthropic left off

Persistence

SQLite at 
.od/app.sqlite
: projects · conversations · messages · tabs · saved templates. Reopen tomorrow, todo card and open files are exactly where you left them.

Lifecycle

One entry point: 
pnpm tools-dev
 (start / stop / run / status / logs / inspect / check) — boots daemon + web (+ desktop) under typed sidecar stamps

Desktop

Optional Electron shell with sandboxed renderer + sidecar IPC (STATUS / EVAL / SCREENSHOT / CONSOLE / CLICK / SHUTDOWN) — drives 
tools-dev inspect desktop screenshot
 for E2E

Deployable to

Local (
pnpm tools-dev
) · Vercel web layer · packaged Electron (placeholder, in-flight)

License

Apache-2.0

## Demo

Entry view
 — pick a skill, pick a design system, type the brief. The same surface for prototypes, decks, mobile apps, dashboards, and editorial pages.

Turn-1 discovery form
 — before the model writes a pixel, OD locks the brief: surface, audience, tone, brand context, scale. 30 seconds of radios beats 30 minutes of redirects.

Direction picker
 — when the user has no brand, the agent emits a second form with 5 curated directions (Monocle / Modern Minimal / Tech Utility / Brutalist / Soft Warm). One radio click → a deterministic palette + font stack, no model freestyle.

Live todo progress
 — the agent's plan streams as a live card. 
in_progress
 → 
completed
 updates land in real time. The user can redirect cheaply, mid-flight.

Sandboxed preview
 — every 
<artifact>
 renders in a clean srcdoc iframe. Editable in place via the file workspace; downloadable as HTML, PDF, ZIP.

72-system library
 — every product system shows its 4-color signature. Click for the full 
DESIGN.md
, swatch grid, and live showcase.

Deck mode (guizang-ppt)
 — the bundled 
guizang-ppt-skill
 drops in unchanged. Magazine layouts, WebGL hero backgrounds, single-file HTML output, PDF export.

Mobile prototype
 — pixel-accurate iPhone 15 Pro chrome (Dynamic Island, status bar SVGs, home indicator). Multi-screen prototypes use the shared 
/frames/
 assets so the agent never re-draws a phone.

## Skills

31 skills ship in the box.Each is a folder underskills/following the Claude CodeSKILL.mdconvention with an extendedod:frontmatter that the daemon parses verbatim —mode,platform,scenario,preview.type,design_system.requires,default_for,featured,fidelity,speaker_notes,animations,example_prompt(apps/daemon/src/skills.ts).

Two top-levelmodescarry the catalog:prototype(27 skills — anything that renders as a single-page artifact, from a magazine landing to a phone screen to a PM spec doc) anddeck(4 skills — horizontal-swipe presentations with deck-framework chrome). Thescenariofield is what the picker groups them by:design·marketing·operation·engineering·product·finance·hr·sale·personal.

### Showcase examples

The visually distinctive skills you'll most likely run first. Each ships a realexample.htmlyou can open straight from the repo to see exactly what the agent will produce — no auth, no setup.

dating-web
 · 
prototype
Consumer dating / matchmaking dashboard — left rail nav, ticker bar, KPIs, 30-day mutual-matches chart, editorial typography.

digital-eguide
 · 
template
Two-spread digital e-guide — cover (title, author, TOC teaser) + lesson spread with pull-quote and step list. Creator / lifestyle tone.

email-marketing
 · 
prototype
Brand product-launch HTML email — masthead, hero image, headline lockup, CTA, specs grid. Centered single-column, table-fallback safe.

gamified-app
 · 
prototype
Three-frame gamified mobile-app prototype on a dark showcase stage — cover, today's quests with XP ribbons + level bar, quest detail.

mobile-onboarding
 · 
prototype
Three-frame mobile onboarding flow — splash, value-prop, sign-in. Status bar, swipe dots, primary CTA.

motion-frames
 · 
prototype
Single-frame motion-design hero with looping CSS animations — rotating type ring, animated globe, ticking timer. Hand-off ready for HyperFrames.

social-carousel
 · 
prototype
Three-card 1080×1080 social-media carousel — cinematic panels with display headlines that connect across the series, brand mark, loop affordance.

sprite-animation
 · 
prototype
Pixel / 8-bit animated explainer slide — full-bleed cream stage, animated pixel mascot, kinetic Japanese display type, looping CSS keyframes.

### Design & marketing surfaces (prototype mode)

Skill

Platform

Scenario

What it produces

web-prototype

desktop

design

Single-page HTML — landings, marketing, hero pages (default for prototype)

saas-landing

desktop

marketing

Hero / features / pricing / CTA marketing layout

dashboard

desktop

operation

Admin / analytics with sidebar + dense data layout

pricing-page

desktop

sale

Standalone pricing + comparison tables

docs-page

desktop

engineering

3-column documentation layout

blog-post

desktop

marketing

Editorial long-form

mobile-app

mobile

design

iPhone 15 Pro / Pixel framed app screen(s)

mobile-onboarding

mobile

design

Multi-screen mobile onboarding flow (splash · value-prop · sign-in)

gamified-app

mobile

personal

Three-frame gamified mobile-app prototype

email-marketing

desktop

marketing

Brand product-launch HTML email (table-fallback safe)

social-carousel

desktop

marketing

3-card 1080×1080 social carousel

magazine-poster

desktop

marketing

Single-page magazine-style poster

motion-frames

desktop

marketing

Motion-design hero with looping CSS animations

sprite-animation

desktop

marketing

Pixel / 8-bit animated explainer slide

dating-web

desktop

personal

Consumer dating dashboard mockup

digital-eguide

desktop

marketing

Two-spread digital e-guide (cover + lesson)

wireframe-sketch

desktop

design

Hand-drawn ideation sketch — for the "show something visible early" pass

critique

desktop

design

Five-dimensional self-critique scoresheet (Philosophy · Hierarchy · Detail · Function · Innovation)

tweaks

desktop

design

AI-emitted tweaks panel — the model surfaces the parameters worth nudging

### Deck surfaces (deck mode)

Skill

Default for

What it produces

guizang-ppt

default
 for deck

Magazine-style web PPT — bundled verbatim from 
op7418/guizang-ppt-skill
, original LICENSE preserved

simple-deck

—

Minimal horizontal-swipe deck

replit-deck

—

Product-walkthrough deck (Replit-style)

weekly-update

—

Team weekly cadence as a swipe deck (progress · blockers · next)

### Office & operations surfaces (prototype mode, document-flavored scenarios)

Skill

Scenario

What it produces

pm-spec

product

PM specification doc with TOC + decision log

team-okrs

product

OKR scoresheet

meeting-notes

operation

Meeting decision log

kanban-board

operation

Board snapshot

eng-runbook

engineering

Incident runbook

finance-report

finance

Exec finance summary

invoice

finance

Single-page invoice

hr-onboarding

hr

Role onboarding plan

Adding a skill takes one folder. Readdocs/skills-protocol.mdfor the extended frontmatter, fork an existing skill, restart the daemon, it appears in the picker. The catalog endpoint isGET /api/skills; per-skill seed assembly (template + side-file references) lives atGET /api/skills/:id/example.

## Six load-bearing ideas

### 1 · We don't ship an agent. Yours is good enough.

The daemon scans yourPATHforclaude,codex,devin,cursor-agent,gemini,opencode,qwen,copilot,hermes,kimi,pi, andkiro-clion startup. Whichever ones it finds become candidate design engines — driven over stdio with one adapter per CLI, swappable from the model picker. Inspired bymulticaandcc-switch. No CLI installed?POST /api/proxy/streamis the same pipeline minus the spawn — paste any OpenAI-compatiblebaseUrl+apiKeyand the daemon forwards SSE chunks back, with loopback / link-local / RFC1918 destinations rejected at the edge.

### 2 · Skills are files, not plugins.

Following Claude Code'sSKILL.mdconvention, each skill isSKILL.md+assets/+references/. Drop a folder intoskills/, restart the daemon, it appears in the picker. The bundledmagazine-web-pptisop7418/guizang-ppt-skillcommitted verbatim — original license preserved, attribution preserved.

### 3 · Design Systems are portable Markdown, not theme JSON.

The 9-sectionDESIGN.mdschema fromVoltAgent/awesome-design-md— color, typography, spacing, layout, components, motion, voice, brand, anti-patterns. Every artifact reads from the active system. Switch system → next render uses the new tokens. The dropdown ships withLinear, Stripe, Vercel, Airbnb, Tesla, Notion, Apple, Anthropic, Cursor, Supabase, Figma, Resend, Raycast, Lovable, Cohere, Mistral, ElevenLabs, X.AI, Spotify, Webflow, Sanity, PostHog, Sentry, MongoDB, ClickHouse, Cal, Replicate, Clay, Composio, Xiaohongshu…— plus 57 design skills sourced fromawesome-design-skills.

### 4 · The interactive question form prevents 80% of redirects.

OD's prompt stack hard-codes aRULE 1: every fresh design brief begins with a<question-form id="discovery">instead of code. Surface · audience · tone · brand context · scale · constraints. A long brief still leaves design decisions open — visual tone, color stance, scale — exactly the things the form locks down in 30 seconds. The cost of a wrong direction is one chat round, not one finished deck.

This is theJunior-Designer modedistilled fromhuashu-design: batch the questions up front, show something visible early (even a wireframe with grey blocks), let the user redirect cheaply. Combined with the brand-asset protocol (locate · download ·grephex · writebrand-spec.md· vocalise), it's the single biggest reason output stops feeling like AI freestyle and starts feeling like a designer who paid attention before painting.

### 5 · The daemon makes the agent feel like it's on your laptop, because it is.

The daemon spawns the CLI withcwdset to the project's artifact folder under.od/projects/<id>/. The agent getsRead,Write,Bash,WebFetch— real tools against a real filesystem. It canReadthe skill'sassets/template.html,grepyour CSS for hex values, write abrand-spec.md, drop generated images, and produce.pptx/.zip/.pdffiles that show up in the file workspace as download chips when the turn ends. Sessions, conversations, messages, tabs persist in a local SQLite DB — pop the project open tomorrow and the agent's todo card is right where you left it.

### 6 · The prompt stack is the product.

What you compose at send time isn't "system + user". It's:

DISCOVERY directives (turn-1 form, turn-2 brand branch, TodoWrite, 5-dim critique)
 + identity charter (OFFICIAL_DESIGNER_PROMPT, anti-AI-slop, junior-pass)
 + active DESIGN.md (72 systems available)
 + active SKILL.md (31 skills available)
 + project metadata (kind, fidelity, speakerNotes, animations, inspiration ids)
 + skill side files (auto-injected pre-flight: read assets/template.html + references/*.md)
 + (deck kind, no skill seed) DECK_FRAMEWORK_DIRECTIVE (nav / counter / scroll / print)

Every layer is composable. Every layer is a file you can edit. Readapps/web/src/prompts/system.tsandapps/web/src/prompts/discovery.tsto see the actual contract.

## Architecture

┌────────────────────── browser (Next.js 16) ──────────────────────┐
│ chat · file workspace · iframe preview · settings · imports │
└──────────────┬───────────────────────────────────┬───────────────┘
 │ /api/* (rewritten in dev) │
 ▼ ▼
 ┌──────────────────────────────────┐ /api/proxy/stream (SSE)
 │ Local daemon (Express + SQLite) │ ─→ any OpenAI-compat
 │ │ endpoint (BYOK)
 │ /api/agents /api/skills│ w/ SSRF blocking
 │ /api/design-systems /api/projects/…
 │ /api/chat (SSE) /api/proxy/stream (SSE)
 │ /api/templates /api/import/claude-design
 │ /api/artifacts/save /api/artifacts/lint
 │ /api/upload /api/projects/:id/files…
 │ /artifacts (static) /frames (static)
 │
 │ optional: sidecar IPC at /tmp/open-design/ipc/<ns>/<app>.sock
 │ (STATUS · EVAL · SCREENSHOT · CONSOLE · CLICK · SHUTDOWN)
 └─────────┬────────────────────────┘
 │ spawn(cli, [...], { cwd: .od/projects/<id> })
 ▼
 ┌──────────────────────────────────────────────────────────────────┐
 │ claude · codex · devin (ACP) · gemini · opencode · cursor-agent │
 │ qwen · copilot · hermes (ACP) · kimi (ACP) · pi (RPC) · kiro │
 │ reads SKILL.md + DESIGN.md, writes artifacts to disk │
 └──────────────────────────────────────────────────────────────────┘

Layer

Stack

Frontend

Next.js 16 App Router + React 18 + TypeScript, Vercel-deployable

Daemon

Node 24 · Express · SSE streaming · 
better-sqlite3
; tables: 
projects
 · 
conversations
 · 
messages
 · 
tabs
 · 
templates

Agent transport

child_process.spawn
; typed-event parsers for 
claude-stream-json
 (Claude Code), 
copilot-stream-json
 (Copilot), 
json-event-stream
 per-CLI parsers (Codex / Gemini / OpenCode / Cursor Agent), 
acp-json-rpc
 (Devin / Hermes / Kimi / Kiro via Agent Client Protocol), 
pi-rpc
 (Pi via stdio JSON-RPC), 
plain
 (Qwen Code)

BYOK proxy

POST /api/proxy/stream
 → OpenAI-compatible 
/v1/chat/completions
, SSE pass-through; rejects loopback / link-local / RFC1918 hosts at the daemon edge

Storage

Plain files in 
.od/projects/<id>/
 + SQLite at 
.od/app.sqlite
 (gitignored, auto-created). Override the root with 
OD_DATA_DIR
 for test isolation

Preview

Sandboxed iframe via 
srcdoc
 + per-skill 
<artifact>
 parser (
apps/web/src/artifacts/parser.ts
)

Export

HTML (inline assets) · PDF (browser print, deck-aware) · PPTX (agent-driven via skill) · ZIP (archiver) · Markdown

Lifecycle

pnpm tools-dev start | stop | run | status | logs | inspect | check
; ports via 
--daemon-port
 / 
--web-port
, namespaces via 
--namespace

Desktop (optional)

Electron shell — discovers the web URL through sidecar IPC, no port guessing; same 
STATUS
/
EVAL
/
SCREENSHOT
/
CONSOLE
/
CLICK
/
SHUTDOWN
 channel powers 
tools-dev inspect desktop …
 for E2E

## Quickstart

git clone https://github.com/nexu-io/open-design.git

cd
 open-design
corepack 
enable

corepack pnpm --version 
#
 should print 10.33.2

pnpm install
pnpm tools-dev run web

#
 open the web URL printed by tools-dev

Environment requirements: Node~24and pnpm10.33.x.nvm/fnmare optional helpers only; if you use one, runnvm install 24 && nvm use 24orfnm install 24 && fnm use 24beforepnpm install.

For desktop/background startup, fixed-port restarts, and media generation dispatcher checks (OD_BIN,OD_DAEMON_URL,apps/daemon/dist/cli.js), seeQUICKSTART.md.

The first load:

1. Detects which agent CLIs you have onPATHand picks one automatically.
2. Loads 31 skills + 72 design systems.
3. Pops the welcome dialog so you can paste an Anthropic key (only needed for the BYOK fallback path).
4. Auto-creates./.od/— the local runtime folder for the SQLite project DB, per-project artifacts, and saved renders. There is nood initstep; the daemonmkdirs everything it needs on boot.

Type a prompt, hitSend, watch the question form arrive, fill it, watch the todo card stream, watch the artifact render. ClickSave to diskor download as a project ZIP.

### First-run state (./.od/)

The daemon owns one hidden folder at the repo root. Everything in it is gitignored and machine-local — never commit it.

.od/
├── app.sqlite ← projects · conversations · messages · open tabs
├── artifacts/ ← one-off "Save to disk" renders (timestamped)
└── projects/<id>/ ← per-project working dir, also the agent's cwd

Want to…

Do this

Inspect what's in there

ls -la .od && sqlite3 .od/app.sqlite '.tables'

Reset to a clean slate

pnpm tools-dev stop
, 
rm -rf .od
, run 
pnpm tools-dev run web
 again

Move it elsewhere

not supported yet — the path is hard-coded relative to the repo

Full file map, scripts, and troubleshooting →QUICKSTART.md.

## Repository structure

open-design/
├── README.md ← this file
├── README.de.md ← Deutsch
├── README.zh-CN.md ← 简体中文
├── QUICKSTART.md ← run / build / deploy guide
├── package.json ← pnpm workspace, single bin: od
│
├── apps/
│ ├── daemon/ ← Node + Express, the only server
│ │ ├── src/ ← TypeScript daemon source
│ │ │ ├── cli.ts ← `od` bin source, compiled to dist/cli.js
│ │ │ ├── server.ts ← /api/* routes (projects, chat, files, exports)
│ │ │ ├── agents.ts ← PATH scanner + per-CLI argv builders
│ │ │ ├── claude-stream.ts ← streaming JSON parser for Claude Code stdout
│ │ │ ├── skills.ts ← SKILL.md frontmatter loader
│ │ │ └── db.ts ← SQLite schema (projects/messages/templates/tabs)
│ │ ├── sidecar/ ← tools-dev daemon sidecar wrapper
│ │ └── tests/ ← daemon package tests
│ │
│ └── web/ ← Next.js 16 App Router + React client
│ ├── app/ ← App Router entrypoints
│ ├── next.config.ts ← dev rewrites + prod static export to out/
│ └── src/ ← React + TypeScript client modules
│ ├── App.tsx ← routing, bootstrap, settings
│ ├── components/ ← chat, composer, picker, preview, sketch, …
│ ├── prompts/
│ │ ├── system.ts ← composeSystemPrompt(base, skill, DS, metadata)
│ │ ├── discovery.ts ← turn-1 form + turn-2 branch + 5-dim critique
│ │ └── directions.ts ← 5 visual directions × OKLch palette + font stack
│ ├── artifacts/ ← streaming <artifact> parser + manifests
│ ├── runtime/ ← iframe srcdoc, markdown, export helpers
│ ├── providers/ ← daemon SSE + BYOK API transports
│ └── state/ ← config + projects (localStorage + daemon-backed)
│
├── e2e/ ← Playwright UI + external integration/Vitest harness
│
├── packages/
│ ├── contracts/ ← shared web/daemon app contracts
│ ├── sidecar-proto/ ← Open Design sidecar protocol contract
│ ├── sidecar/ ← generic sidecar runtime primitives
│ └── platform/ ← generic process/platform primitives
│
├── skills/ ← 31 SKILL.md skill bundles (27 prototype + 4 deck)
│ ├── web-prototype/ ← default for prototype mode
│ ├── saas-landing/ dashboard/ pricing-page/ docs-page/ blog-post/
│ ├── mobile-app/ mobile-onboarding/ gamified-app/
│ ├── email-marketing/ social-carousel/ magazine-poster/
│ ├── motion-frames/ sprite-animation/ digital-eguide/ dating-web/
│ ├── critique/ tweaks/ wireframe-sketch/
│ ├── pm-spec/ team-okrs/ meeting-notes/ kanban-board/
│ ├── eng-runbook/ finance-report/ invoice/ hr-onboarding/
│ ├── simple-deck/ replit-deck/ weekly-update/ ← deck mode
│ └── guizang-ppt/ ← bundled magazine-web-ppt (default for deck)
│ ├── SKILL.md
│ ├── assets/template.html ← seed
│ └── references/{themes,layouts,components,checklist}.md
│
├── design-systems/ ← 72 DESIGN.md systems
│ ├── default/ ← Neutral Modern (starter)
│ ├── warm-editorial/ ← Warm Editorial (starter)
│ ├── linear-app/ vercel/ stripe/ airbnb/ notion/ cursor/ apple/ …
│ └── README.md ← catalog overview
│
├── assets/
│ └── frames/ ← shared device frames (used cross-skill)
│ ├── iphone-15-pro.html
│ ├── android-pixel.html
│ ├── ipad-pro.html
│ ├── macbook.html
│ └── browser-chrome.html
│
├── templates/
│ ├── deck-framework.html ← deck baseline (nav / counter / print)
│ └── kami-deck.html ← kami-flavored deck starter (parchment / ink-blue serif)
│
├── scripts/
│ └── sync-design-systems.ts ← re-import upstream awesome-design-md tarball
│
├── docs/
│ ├── spec.md ← product spec, scenarios, differentiation
│ ├── architecture.md ← topologies, data flow, components
│ ├── skills-protocol.md ← extended SKILL.md od: frontmatter
│ ├── agent-adapters.md ← per-CLI detection + dispatch
│ ├── modes.md ← prototype / deck / template / design-system
│ ├── references.md ← long-form provenance
│ ├── roadmap.md ← phased delivery
│ ├── schemas/ ← JSON schemas
│ └── examples/ ← canonical artifact examples
│
└── .od/ ← runtime data, gitignored, auto-created
 ├── app.sqlite ← projects / conversations / messages / tabs
 ├── projects/<id>/ ← per-project working folder (agent's cwd)
 └── artifacts/ ← saved one-off renders

## Design Systems

72 systems out of the box, each as a singleDESIGN.md:

Full catalog
 (click to expand)

AI & LLM—claude·cohere·mistral-ai·minimax·together-ai·replicate·runwayml·elevenlabs·ollama·x-ai

Developer Tools—cursor·vercel·linear-app·framer·expo·clickhouse·mongodb·supabase·hashicorp·posthog·sentry·warp·webflow·sanity·mintlify·lovable·composio·opencode-ai·voltagent

Productivity—notion·figma·miro·airtable·superhuman·intercom·zapier·cal·clay·raycast

Fintech—stripe·coinbase·binance·kraken·mastercard·revolut·wise

E-Commerce—shopify·airbnb·uber·nike·starbucks·pinterest

Media—spotify·playstation·wired·theverge·meta

Automotive—tesla·bmw·ferrari·lamborghini·bugatti·renault

Other—apple·ibm·nvidia·vodafone·sentry·resend·spacex

Starters—default(Neutral Modern) ·warm-editorial

The product-system library is imported viascripts/sync-design-systems.tsfromVoltAgent/awesome-design-md. Re-run to refresh. The 57 design skills are sourced frombergside/awesome-design-skillsand added directly indesign-systems/.

## Visual directions

When the user has no brand spec, the agent emits a second form with five curated directions — the OD adaptation ofhuashu-design's "5 schools × 20 design philosophies" fallback. Each direction is a deterministic spec — palette in OKLch, font stack, layout posture cues, references — that the agent binds verbatim into the seed template's:root. One radio click → a fully specified visual system. No improvisation, no AI-slop.

Direction

Mood

Refs

Editorial — Monocle / FT

Print magazine, ink + cream + warm rust

Monocle · FT Weekend · NYT Magazine

Modern minimal — Linear / Vercel

Cool, structured, minimal accent

Linear · Vercel · Stripe

Tech utility

Information density, monospace, terminal

Bloomberg · Bauhaus tools

Brutalist

Raw, oversized type, no shadows, harsh accents

Bloomberg Businessweek · Achtung

Soft warm

Generous, low contrast, peachy neutrals

Notion marketing · Apple Health

Full spec →apps/web/src/prompts/directions.ts.

## Media generation

OD doesn't stop at code. The same chat surface that produces<artifact>HTML also drivesimage,video, andaudiogeneration, with model adapters wired into the daemon's media pipeline (apps/daemon/src/media-models.ts,apps/web/src/media/models.ts). Every render lands as a real file in the project workspace —.pngfor image,.mp4for video — and shows up as a download chip when the turn ends.

Three model families carry the load today:

Surface

Model

Provider

What it's for

Image

gpt-image-2

Azure / OpenAI

Posters, profile avatars, illustrated maps, infographics, magazine-style social cards, photo restoration, exploded-view product art

Video

seedance-2.0

ByteDance Volcengine

15s cinematic t2v + i2v with audio — narrative shorts, character close-ups, product films, MV-style choreography

Video

hyperframes-html

HeyGen / OSS

HTML→MP4 motion graphics — product reveals, kinetic typography, data charts, social overlays, logo outros, TikTok-style verticals with karaoke captions

A growingprompt galleryatprompt-templates/ships93 ready-to-replicate prompts— 43 image (prompt-templates/image/*.json), 39 Seedance (prompt-templates/video/*.jsonexcludinghyperframes-*), 11 HyperFrames (prompt-templates/video/hyperframes-*.json). Each carries a preview thumbnail, the prompt body verbatim, the target model, the aspect ratio, and asourceblock for license + attribution. The daemon serves them atGET /api/prompt-templates, the web app surfaces them as a card grid in theImage templatesandVideo templatestabs of the entry view; one click drops a prompt into the composer with the right model preselected.

### gpt-image-2 — image gallery (sample of 43)

3D Stone Staircase Evolution Infographic
3-step infographic, hewn-stone aesthetic

Illustrated City Food Map
Editorial hand-illustrated travel poster

Cinematic Elevator Scene
Single-frame editorial fashion still

Cyberpunk Anime Portrait
Profile avatar — neon face text

Glamorous Woman in Black Portrait
Editorial studio portrait

Full set →prompt-templates/image/. Sources: most pull fromYouMind-OpenLab/awesome-gpt-image-prompts(CC-BY-4.0) with author attribution preserved per template.

### Seedance 2.0 — video gallery (sample of 39)

Music Podcast & Guitar Technique
4K cinematic studio film

Emotional Face Close-up
Cinematic micro-expression study

Luxury Supercar Cinematic
Narrative product film

Forbidden City Cat Satire
Stylised satire short

Japanese Romance Short Film
15s Seedance 2.0 narrative

Click any thumbnail to play the actual rendered MP4. Full set →prompt-templates/video/(the*-seedance-*and Cinematic-tagged entries). Sources:YouMind-OpenLab/awesome-seedance-2-prompts(CC-BY-4.0) with original tweet links and author handles preserved.

### HyperFrames — HTML→MP4 motion graphics (11 ready-to-replicate templates)

heygen-com/hyperframesis HeyGen's open-source agent-native video framework — you (or the agent) write HTML + CSS + GSAP, HyperFrames renders it to a deterministic MP4 via headless Chrome + FFmpeg. Open Design ships HyperFrames as a first-class video model (hyperframes-html) wired into the daemon dispatch, plus theskills/hyperframes/skill that teaches the agent the timeline contract, scene-transition rules, audio-reactive patterns, captions/TTS, and the catalog blocks (npx hyperframes add <slug>).

Eleven hyperframes prompts ship underprompt-templates/video/hyperframes-*.json, each one a concrete brief that produces a specific archetype:

5s minimal product reveal
 · 16:9 · push-in title card with shader transition

30s SaaS product promo
 · 16:9 · Linear/ClickUp-style with UI 3D reveals

TikTok karaoke talking-head
 · 9:16 · TTS + word-synced captions

30s brand sizzle reel
 · 16:9 · beat-synced kinetic typography, audio-reactive

Animated bar-chart race
 · 16:9 · NYT-style data infographic

Flight map (origin → dest)
 · 16:9 · Apple-style cinematic route reveal

4s cinematic logo outro
 · 16:9 · piece-by-piece assembly + bloom

$0 → $10K money counter
 · 9:16 · Apple-style hype with green flash + burst

3-phone app showcase
 · 16:9 · floating phones with feature callouts

Social overlay stack
 · 9:16 · X · Reddit · Spotify · Instagram in sequence

Website-to-video pipeline
 · 16:9 · captures site at 3 viewports + transitions

 

Pattern is the same as the rest: pick a template, edit the brief, send. The agent reads the bundledskills/hyperframes/SKILL.md(which carries the OD-specific render workflow — composition source files into a.hyperframes-cache/so they don't clutter the file workspace, daemon dispatchesnpx hyperframes renderto dodge the macOS sandbox-exec / Puppeteer hang, only the final.mp4lands as a project chip), authors the composition, and ships an MP4. Catalog block thumbnails © HeyGen, served from their CDN; the OSS framework itself is Apache-2.0.

Also wired but not surfaced as templates yet:Kling 2.0 / 1.6 / 1.5, Veo 3 / Veo 2, Sora 2 / Sora 2-Pro (via Fal), MiniMax video-01 — all live inVIDEO_MODELS(apps/web/src/media/models.ts). Suno v5 / v4.5, Udio v2, Lyria 2 (music) and gpt-4o-mini-tts, MiniMax TTS (speech) cover the audio surface. Templates for these are open contributions — drop a JSON intoprompt-templates/video/orprompt-templates/audio/and it shows up in the picker.

## Beyond chat — what else ships

The chat / artifact loop gets the spotlight, but a handful of less-visible capabilities are already wired and worth knowing before you compare OD to anything else:

* Claude Design ZIP import.Drop an export from claude.ai onto the welcome dialog.POST /api/import/claude-designextracts it into a real.od/projects/<id>/, opens the entry file as a tab, and stages a continue-where-Anthropic-left-off prompt for your local agent. No re-prompting, no "ask the model to re-create what we just had". (apps/daemon/src/server.ts—/api/import/claude-design)
* OpenAI-compatible BYOK proxy.POST /api/proxy/streamtakes{ baseUrl, apiKey, model, messages }, normalises the path (…/v1/chat/completions), forwards SSE chunks back to the browser, and rejects loopback / link-local / RFC1918 destinations to head off SSRF. Anything that speaks the OpenAI chat schema works — Anthropic-via-OpenAI shim, DeepSeek, Groq, MiMo, OpenRouter, your self-hosted vLLM. MiMo getstool_choice: 'none'automatically because its tool schema misbehaves on free-form generation.
* User-saved templates.Once you like a render,POST /api/templatessnapshots the HTML + metadata into the SQLitetemplatestable. The next project picks it from a "your templates" row in the picker — same surface as the shipped 31, but yours.
* Tab persistence.Every project remembers its open files and active tab in thetabstable. Reopen the project tomorrow and the workspace looks exactly the way you left it.
* Artifact lint API.POST /api/artifacts/lintruns structural checks on a generated artifact (broken<artifact>framing, missing required side files, stale palette tokens) and returns findings the agent can read back into its next turn. The five-dim self-critique uses this to ground its score in real evidence, not vibes.
* Sidecar protocol + desktop automation.Daemon, web, and desktop processes carry typed five-field stamps (app · mode · namespace · ipc · source) and expose a JSON-RPC IPC channel at/tmp/open-design/ipc/<namespace>/<app>.sock.tools-dev inspect desktop status \| eval \| screenshotdrives that channel, so headless E2E works against a real Electron shell without bespoke harnesses (packages/sidecar-proto/,apps/desktop/src/main/).
* Windows-friendly spawning.Every adapter that would otherwise blowCreateProcess's ~32 KB argv limit on long composed prompts (Codex, Gemini, OpenCode, Cursor Agent, Qwen, Pi) feeds the prompt over stdin instead. Claude Code and Copilot keep-p; the daemon falls back to a temp prompt-file when even that overflows.
* Per-namespace runtime data.OD_DATA_DIRand--namespacegive you fully isolated.od/-style trees, so Playwright, beta channels, and your real projects never share a SQLite file.

## Anti-AI-slop machinery

The whole machinery below is thehuashu-designplaybook, ported into OD's prompt-stack and made enforceable per-skill via the side-file pre-flight. Readapps/web/src/prompts/discovery.tsfor the live wording:

* Question form first.Turn 1 is<question-form>only — no thinking, no tools, no narration. The user chooses defaults at radio speed.
* Brand-spec extraction.When the user attaches a screenshot or URL, the agent runs a five-step protocol (locate · download · grep hex · codifybrand-spec.md· vocalise) before writing CSS.Never guesses brand colors from memory.
* Five-dim critique.Before emitting<artifact>, the agent silently scores its output 1–5 across philosophy / hierarchy / execution / specificity / restraint. Anything under 3/5 is a regression — fix and rescore. Two passes is normal.
* P0/P1/P2 checklist.Every skill ships areferences/checklist.mdwith hard P0 gates. The agent must pass P0 before emitting.
* Slop blacklist.Aggressive purple gradients, generic emoji icons, rounded card with left-border accent, hand-drawn SVG humans, Inter as adisplayface, invented metrics — explicitly forbidden in the prompt.
* Honest placeholders > fake stats.When the agent doesn't have a real number, it writes—or a labelled grey block, not "10× faster".

## Comparison

Axis

Claude Design
 (Anthropic)

Open CoDesign

Open Design

License

Closed

MIT

Apache-2.0

Form factor

Web (claude.ai)

Desktop (Electron)

Web app + local daemon

Deployable on Vercel

❌

❌

✅

Agent runtime

Bundled (Opus 4.7)

Bundled (
pi-ai
)

Delegated to user's existing CLI

Skills

Proprietary

12 custom TS modules + 
SKILL.md

31 file-based 
SKILL.md
 bundles, droppable

Design system

Proprietary

DESIGN.md
 (v0.2 roadmap)

DESIGN.md
 × 129 systems shipped

Provider flexibility

Anthropic only

7+ via 
pi-ai

12 CLI adapters + OpenAI-compatible BYOK proxy

Init question form

❌

❌

✅ Hard rule, turn 1

Direction picker

❌

❌

✅ 5 deterministic directions

Live todo progress + tool stream

❌

✅

✅
 (UX pattern from open-codesign)

Sandboxed iframe preview

❌

✅

✅
 (pattern from open-codesign)

Claude Design ZIP import

n/a

❌

✅ 
POST /api/import/claude-design
 — keep editing where Anthropic left off

Comment-mode surgical edits

❌

✅

🟡 partial — preview element comments + chat attachments; surgical patch reliability still in progress

AI-emitted tweaks panel

❌

✅

🚧 roadmap — dedicated chat-side panel UX is not implemented yet

Filesystem-grade workspace

❌

partial (Electron sandbox)

✅ Real cwd, real tools, persisted SQLite (projects · conversations · messages · tabs · templates)

5-dim self-critique

❌

❌

✅ Pre-emit gate

Artifact lint

❌

❌

✅ 
POST /api/artifacts/lint
 — findings fed back to the agent

Sidecar IPC + headless desktop

❌

❌

✅ Stamped processes + 
tools-dev inspect desktop status | eval | screenshot

Export formats

Limited

HTML / PDF / PPTX / ZIP / Markdown

HTML / PDF / PPTX (agent-driven) / ZIP / Markdown

PPT skill reuse

N/A

Built-in

guizang-ppt-skill
 drops in (default for deck mode)

Minimum billing

Pro / Max / Team

BYOK

BYOK — paste any OpenAI-compatible 
baseUrl

## Supported coding agents

Auto-detected fromPATHon daemon boot. No config required. Streaming dispatch lives inapps/daemon/src/agents.ts(AGENT_DEFS); per-CLI parsers live alongside it. Models are populated either by probing<bin> --list-models/<bin> models/ ACP handshake, or from a curated fallback list when the CLI doesn't expose a list.

Agent

Bin

Stream format

Argv shape (composed prompt path)

Claude Code

claude

claude-stream-json
 (typed events)

claude -p <prompt> --output-format stream-json --verbose [--include-partial-messages] [--add-dir …] --permission-mode bypassPermissions

Codex CLI

codex

json-event-stream
 + 
codex
 parser

codex exec --json --skip-git-repo-check --full-auto [-C cwd] [--model …] [-c model_reasoning_effort=…] -
 (prompt on stdin)

Devin for Terminal

devin

acp-json-rpc

devin --permission-mode dangerous --respect-workspace-trust false acp

Gemini CLI

gemini

json-event-stream
 + 
gemini
 parser

gemini --output-format stream-json --skip-trust --yolo [--model …] -
 (prompt on stdin)

OpenCode

opencode

json-event-stream
 + 
opencode
 parser

opencode run --format json --dangerously-skip-permissions [--model …] -
 (prompt on stdin)

Cursor Agent

cursor-agent

json-event-stream
 + 
cursor-agent
 parser

cursor-agent --print --output-format stream-json --stream-partial-output --force --trust [--workspace cwd] [--model …] -
 (prompt on stdin)

Qwen Code

qwen

plain
 (raw stdout chunks)

qwen --yolo [--model …] -
 (prompt on stdin)

GitHub Copilot CLI

copilot

copilot-stream-json
 (typed events)

copilot -p <prompt> --allow-all-tools --output-format json [--model …] [--add-dir …]

Hermes

hermes

acp-json-rpc
 (Agent Client Protocol)

hermes acp --accept-hooks

Kimi CLI

kimi

acp-json-rpc

kimi acp

Kiro CLI

kiro-cli

acp-json-rpc

kiro-cli acp

Pi

pi

pi-rpc
 (stdio JSON-RPC)

pi --mode rpc --no-session [--model …] [--thinking …]
 (prompt sent as RPC 
prompt
 command)

OpenAI-compatible BYOK

n/a

SSE pass-through

POST /api/proxy/stream
 → 
<baseUrl>/v1/chat/completions
; SSRF-guarded against loopback / link-local / RFC1918

Adding a new CLI is one entry inapps/daemon/src/agents.ts. Streaming format is one ofclaude-stream-json,copilot-stream-json,json-event-stream(with a per-CLIeventParser),acp-json-rpc,pi-rpc, orplain.

## References & lineage

Every external project this repo borrows from. Each link goes to the source so you can verify the provenance.

Project

Role here

Claude Design

The closed-source product this repo is the open-source alternative to.

alchaincyf/huashu-design

The design-philosophy core. Junior-Designer workflow, the 5-step brand-asset protocol, anti-AI-slop checklist, 5-dimensional self-critique, and the "5 schools × 20 design philosophies" library behind our direction picker — all distilled into 
apps/web/src/prompts/discovery.ts
 and 
apps/web/src/prompts/directions.ts
.

op7418/guizang-ppt-skill

Magazine-web-PPT skill bundled verbatim under 
skills/guizang-ppt/
 with original LICENSE preserved. Default for deck mode. P0/P1/P2 checklist culture borrowed for every other skill.

multica-ai/multica

The daemon + adapter architecture. PATH-scan agent detection, local daemon as the only privileged process, agent-as-teammate worldview. We adopt the model; we do not vendor the code.

OpenCoworkAI/open-codesign

The first open-source Claude-Design alternative and our closest peer. UX patterns adopted: streaming-artifact loop, sandboxed-iframe preview (vendored React 18 + Babel), live agent panel (todos + tool calls + interruptible), five-format export list (HTML/PDF/PPTX/ZIP/Markdown), local-first storage hub, 
SKILL.md
 taste-injection, and the first pass of comment-mode preview annotations. UX patterns still on our roadmap: full surgical-edit reliability and AI-emitted tweaks panel. 
We deliberately do not vendor 
pi-ai
 — open-codesign bundles it as the agent runtime; we delegate to whichever CLI the user already has.

VoltAgent/awesome-claude-design
 / 
awesome-design-md

Source of the 9-section 
DESIGN.md
 schema and 70 product systems imported via 
scripts/sync-design-systems.ts
.

bergside/awesome-design-skills

Source of 57 design skills added directly as normalized 
DESIGN.md
 files under 
design-systems/
.

farion1231/cc-switch

Inspiration for symlink-based skill distribution across multiple agent CLIs.

Claude Code skills

The 
SKILL.md
 convention adopted verbatim — any Claude Code skill drops into 
skills/
 and is picked up by the daemon.

Long-form provenance write-up — what we take from each, what we deliberately don't — lives atdocs/references.md.

## Roadmap

* Daemon + agent detection (12 CLI adapters) + skill registry + design-system catalog
* Web app + chat + question form + 5-direction picker + todo progress + sandboxed preview
* 31 skills + 72 design systems + 5 visual directions + 5 device frames
* SQLite-backed projects · conversations · messages · tabs · templates
* OpenAI-compatible BYOK proxy (/api/proxy/stream) with SSRF guard
* Claude Design ZIP import (/api/import/claude-design)
* Sidecar protocol + Electron desktop with IPC automation (STATUS / EVAL / SCREENSHOT / CONSOLE / CLICK / SHUTDOWN)
* Artifact lint API + 5-dim self-critique pre-emit gate
* Comment-mode surgical edits — partial shipped: preview element comments and chat attachments; reliable targeted patching remains in progress
* AI-emitted tweaks panel UX — not implemented yet
* Vercel + tunnel deployment recipe (Topology B)
* One-commandnpx od initto scaffold a project withDESIGN.md
* Skill marketplace (od skills install <github-repo>) andod skill add | list | remove | testCLI surface (drafted indocs/skills-protocol.md, implementation pending)
* Packaged Electron build out ofapps/packaged/

Phased delivery →docs/roadmap.md.

## Status

This is an early implementation — the closed loop (detect → pick skill + design system → chat → parse<artifact>→ preview → save) runs end-to-end. The prompt stack and skill library are where most of the value lives, and they're stable. The component-level UI is shipping daily.

## Star us

If this saved you thirty minutes — give it a ★. Stars don't pay rent, but they tell the next designer, agent, and contributor that this experiment is worth their attention. One click, three seconds, real signal:github.com/nexu-io/open-design.

## Contributing

Issues, PRs, new skills, and new design systems are all welcome. The highest-leverage contributions are usually one folder, one Markdown file, or one PR-sized adapter:

* Add a skill— drop a folder intoskills/following theSKILL.mdconvention.
* Add a design system— drop aDESIGN.mdintodesign-systems/<brand>/using the 9-section schema.
* Wire up a new coding-agent CLI— one entry inapps/daemon/src/agents.ts.

Full walkthrough, bar-for-merging, code style, and what we don't accept →CONTRIBUTING.md(Deutsch,简体中文).

## Contributors

Thanks to everyone who has helped move Open Design forward — through code, docs, feedback, new skills, new design systems, or even a sharp issue. Every real contribution counts, and the wall below is the easiest way to say so out loud.

If you've shipped your first PR — welcome. Thegood-first-issuelabel is the entry point.

## Repository activity

The SVG above is regenerated daily by.github/workflows/metrics.ymlusinglowlighter/metrics. Trigger a manual refresh from theActionstab if you want it sooner; for richer plugins (traffic, follow-up time), add aMETRICS_TOKENrepository secret with a fine-grained PAT.

## Star History

If the curve bends up, that's the signal we look for. ★ this repo to push it.

## Credits

The HTML PPT Studio family of skills — the masterskills/html-ppt/and the per-template wrappers underskills/html-ppt-*/(15 full-deck templates, 36 themes, 31 single-page layouts, 27 CSS animations + 20 canvas FX, the keyboard runtime, and the magnetic-card presenter mode) — are integrated from the open-source projectlewislulu/html-ppt-skill(MIT). The upstream LICENSE ships in-tree atskills/html-ppt/LICENSEand authorship credit goes to@lewislulu. Each per-template Examples card (html-ppt-pitch-deck,html-ppt-tech-sharing,html-ppt-presenter-mode,html-ppt-xhs-post, …) delegates authoring guidance to the master skill so the upstream's prompt → output behavior is preserved end-to-end when you clickUse this prompt.

The magazine / horizontal-swipe deck flow underskills/guizang-ppt/is integrated fromop7418/guizang-ppt-skill(MIT). Authorship credit goes to@op7418.

## License

Apache-2.0. The bundledskills/guizang-ppt/retains its originalLICENSE(MIT) and authorship attribution toop7418. The bundledskills/html-ppt/retains its originalLICENSE(MIT) and authorship attribution tolewislulu.

## About

🎨 Local-first, open-source alternative to Anthropic's Claude Design. ⚡ 19 Skills · ✨ 71 brand-grade Design Systems 🖼 Generate web · desktop · mobile prototypes · slides · images · videos · HyperFrames 📦 Sandboxed preview · HTML/PDF/PPTX/MP4 export 🤖 Runs on Claude Code / Codex / Cursor / Gemini / OpenCode / Qwen / Copilot / Hermes / Kimi CLI.

github.com/nexu-io/open-design

### Topics

 desktop-app

 design-systems

 nextjs

 prototyping

 design-tools

 no-code

 ai-agents

 claude

 ui-generator

 local-first

 byok

 ai-design

 generative-ai

 coding-agents

 agent-skills

 vibe-coding

 figma-alternative

 hermes-agent

 claude-design

 claude-code-for-design

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

15.4k

 stars
 

### Watchers

57

 watching
 

### Forks

1.7k

 forks
 

 Report repository

 

## Releases9

Open Design 0.2.0

 Latest

 

May 2, 2026

 

+ 8 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript57.5%
* HTML28.1%
* CSS7.0%
* JavaScript4.6%
* Python2.7%
* Shell0.1%