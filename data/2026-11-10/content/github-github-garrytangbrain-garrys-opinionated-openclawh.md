---
title: 'GitHub - garrytan/gbrain: Garry''s Opinionated OpenClaw/Hermes Agent Brain · GitHub'
url: https://github.com/garrytan/gbrain
site_name: github
content_file: github-github-garrytangbrain-garrys-opinionated-openclawh
fetched_at: '2026-11-10T04:41:08.484369'
original_url: https://github.com/garrytan/gbrain
author: garrytan
description: Garry's Opinionated OpenClaw/Hermes Agent Brain. Contribute to garrytan/gbrain development by creating an account on GitHub.
---

master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

13,728 Commits
13,728 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents
.agents
 
 
.claude-plugin
.claude-plugin
 
 
.codex-plugin
.codex-plugin
 
 
.gbrain-evals
.gbrain-evals
 
 
.github
.github
 
 
.gstack
.gstack
 
 
admin
admin
 
 
docs
docs
 
 
evals
evals
 
 
examples
examples
 
 
native/
locks
native/
locks
 
 
patches
patches
 
 
plugin-variants
plugin-variants
 
 
plugin
plugin
 
 
recipes
recipes
 
 
scripts
scripts
 
 
skills
skills
 
 
spec/
tla
spec/
tla
 
 
src
src
 
 
templates
templates
 
 
test
test
 
 
tests
tests
 
 
third-party/
company-brain
third-party/
company-brain
 
 
tools
tools
 
 
vendor
vendor
 
 
.env.testing.example
.env.testing.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitleaks.toml
.gitleaks.toml
 
 
.gitleaksignore
.gitleaksignore
 
 
AGENTS.md
AGENTS.md
 
 
BOOTSTRAP_FOR_AGENTS.md
BOOTSTRAP_FOR_AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DESIGN.md
DESIGN.md
 
 
INSTALL_FOR_AGENTS.md
INSTALL_FOR_AGENTS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
TODOS.md
TODOS.md
 
 
VERSION
VERSION
 
 
bun.lock
bun.lock
 
 
bunfig.toml
bunfig.toml
 
 
dbg-tmp.ts
dbg-tmp.ts
 
 
docker-compose.ci.yml
docker-compose.ci.yml
 
 
docker-compose.test.yml
docker-compose.test.yml
 
 
gbrain.yml
gbrain.yml
 
 
llms-full.txt
llms-full.txt
 
 
llms.txt
llms.txt
 
 
openclaw.plugin.json
openclaw.plugin.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

Give the agent you already use a memory you control.GBrain stores explicit facts with their sources, supports corrections and withdrawal, and makes the same memory available across your agents. Start with keyless memory and keyword retrieval; add semantic search, synthesis, and background enrichment when you need them.

GBrain is MIT-licensed and free to self-host; gbrain.io is optional paid hosting.

Tip

Need hosted? First time running an agent?Trygbrain.io, hosted GBrain, for the easiest experience: one brain for you and your team, connected to ChatGPT, Claude and Cursor, with nothing to install or keep online. Stuck? Emailsupport@gbrain.ioand a person will set it up with you, free.

Keep skills beside knowledge.New local brains include memory skills in their
content root. Agents can join an authorized catalog; only approved editors can
publish. Managed coding-agent installs add an owned native router; restart and
real-use verification are separate steps. Staged migration preserves sharing
choices and personal edits. Seeshared brain skills.

## Choose your setup

1. Add GBrain to my existing agent — recommended.Keep your agent's identity and save memory inside its environment. No new personal-agent identity or private repository is required. Start with the guide forGrok Bot,Muse, orCodex / Claude Code.Other harnesses.
2. Use the brain on my own computer from everywhere.One command publishes it over MCP on your Tailscale tailnet and keeps it running:gbrain mcp expose(add--funnelfor cloud agents such as Grok Bot, Muse and ChatGPT). Followuse your brain from anywhere over MCP.Say to your agent:"use my brain over mcp"—"put my brain on tailscale".
3. Connect my existing hosted brain.Followhosted harness accessto choose native OAuth or a private machine connection. For dashboard login, clients, and permissions, useMCP administrationwith the server's separate owner credential. Delegation is an explicit choice.

GrokBotand GrokBuildare different products. Muse's personal agent andMuse Codeare different products too. Muse already has native editable memory; GBrain adds an explicit, portable record with provenance and shared access. See each guide's dated evidence and remaining verification steps.

I'm Garry Tan, President and CEO of Y Combinator. I built GBrain to run my own AI agents. It's the production brain behind my OpenClaw and Hermes deployments:155,795 pages, 24,589 people, 5,340 companies, 66 cron jobs running autonomously. My agent ingests meetings, emails, tweets, voice calls, and original ideas while I sleep. It enriches every person and company it encounters. It fixes its own citations and consolidates memory overnight. I wake up smarter than when I went to bed — and so will you.

It works as a company brain too.Authenticated remote clients are constrained by source and operation grants plus visibility filters. Local files and shared database credentials are a different trust boundary: sources alone do not isolate those callers. The authorization tests exercise specific access paths, not a universal no-leak guarantee. Read thesharing boundariesandcompany-brain tutorialbefore setting up shared access.

Alongside keyword and semantic retrieval, GBrain offers two optional ways to use your stored knowledge:

* A synthesis layer that gives you the actual answer.Synthesized, well-cited prose across people, companies, deals, and ideas. Not "here are 10 chunks that mention your query"; an actual answer with citations and an explicit note on what the brain doesn't know yet. The gap analysis is the part that changes how you use the brain.
* A typed knowledge graph.Trusted local page writes extract supported references without LLM calls when auto-linking is enabled. Remoteput_pageedges arrive later, via sweeps, maintenance oradd_link. Ask "who works at acme-example?": walks are breadth-first, milliseconds on dense clusters (how). On BrainBench relationship questions, relationship retrieval lifts productionR@5 from 0.6626 to 0.7241(benchmark); 0.9791 is thegraph-oracle-parseupper bound, not a product score.

The point of building a 150K-page brain is to use it as a strategic moat. To never lose context. To query what's in your own head without re-reading it. The brain layer is what makes the moat usable. The 24/7 dream cycle is what keeps it sharp. Both run on your hardware, your DB, your keys.

It's easier to ship a daemon that runs 24/7 to ingest, enrich, and consolidate than it is to keep an agent in chat working hard. GBrain is that daemon, generalized. Install in 30 minutes. Your agent does the work. As my personal agent gets smarter, so does yours.

Start keyless.Your harness subscription and any separately configured model API usage are different costs. The optional personal-agent bootstrap takes about 15 minutes; always-on enrichment needs its own compute and API configuration.

Durable preferences and facts can be shared across agents; transient task and
harness configuration state stay local. Configured cloud embedding, reranking,
extraction, and synthesis providers can receive text, and the harness model sees
recalled memory even in keyless mode. Markdown export is not a full database
backup. Readmemory boundaries.

LLMs:fetchllms.txtfor the documentation map, orllms-full.txtfor the same map with core docs inlined in one fetch.Agents:start withAGENTS.md(orCLAUDE.mdif you're Claude Code).

## What this looks like

Say you have a meeting with Alice tomorrow. You want to walk in remembering what she works on, when you last talked, and what's still open between you. Here's what you'd type, and what you'd get back.

You ask:

"What do I need to know before my meeting with Alice tomorrow?"

Most personal-knowledge tools give you back a list of pages.Something like:

1. people/alice — Alice runs engineering at Acme...
2. meetings/2026-03-15-alice-q1 — Q1 product review with Alice...
3. meetings/2026-01-08-acme-kickoff — Kickoff meeting with Acme team...
4. customers/acme — Acme is a series-B fintech we work with...
5. notes/2026-04-22 — Quick chat with Alice about pricing...

Five pages you now have to open and read yourself to actually prepare. The tool found the right material, but it didn't do the work.

GBrain gives you back the answer, with sources:

Alice runs engineering at Acme (a series-B fintech). You last spoke
on April 22 in a quick pricing chat. Three things are still open
from that conversation:

1. She owes you the security review for the new tier
 (deadline was May 1; no update since).
2. You committed to pricing for a 500-seat tier
 (you sent it April 25; no response yet).
3. She mentioned they're hiring a CISO; you said you'd intro
 someone from your network.

Heads up: nothing's been added to the brain about Alice or Acme
since April 22, six weeks ago. She may have replied through email
or Slack DM, channels the brain doesn't see. Worth asking her to
catch up before assuming any of this is still current.

Every claim has a source page behind it. The "heads up" at the end tells you what the brain doesn't know yet, so you can ask Alice about it directly instead of being surprised. The brain just did your meeting prep.

This is the difference between a search engine and a brain. Search finds the pages. The brain reads them for you and writes the answer.

## Install

Tip

Fastest: hosted GBrain atgbrain.io, for any harness.One command launches a GBrain hosted on gbrain.io; Claude Code, Codex, ChatGPT, Cursor and every other AI you use connect to it, with nothing to keep online.

curl -sSL https://gbrainio.terminalwire.sh 
|
 bash
gbrainio terminal connect 
#
 in a new terminal

gbrainio workspace new 
#
 pick a plan in the browser

curl -fsSL https://bun.sh/install 
|
 bash 
#
 skip if Bun 1.4.4+ is installed

export
 PATH=
"
$HOME
/.bun/bin:
$PATH
"

bun install -g github:garrytan/gbrain#stable 
#
 the gbrain CLI only; no local brain

#
 Claude Code (an existing gbrain entry is kept):

(claude mcp get gbrain 
>
/dev/null 
2>&1
 
||
 claude mcp add --transport http --scope user gbrain https://gbrain.io/mcp) 
&&
 gbrain setup claude-code --instructions-only

#
 Codex (an existing gbrain entry is kept):

(codex mcp get gbrain 
>
/dev/null 
2>&1
 
||
 codex mcp add gbrain --url https://gbrain.io/mcp) 
&&
 gbrain setup codex --instructions-only

gbrain setup <harness> --instructions-onlytells the agent the brain is there; agents seldom call an MCP server nobody told them about. It writes thebrain-first blockinto~/.claude/CLAUDE.mdor Codex'sAGENTS.md(a non-emptyAGENTS.override.mdinstead when Codex has one) with a per-turn rule hook, and leaves the MCP entry alone; the same command with--no-instructionsadded takes them out.

The installer is a shell script for macOS and Linux; read it before you run it.

### Here's how to self-host it

GBrain is MIT-licensed and free to self-host. It needsBun 1.4.4 or newer; existing worker installs read theauthorization and queue upgrade guidebefore restarting on this version.

Warning

GBrain is NOT distributed on npm.The npmgbrainpackage is unrelated and
can shadow the real binary, so never runnpm install -g gbrainorbun add -g gbrain. Install only viabun install -g github:garrytan/gbrain#stable(the soaked stable channel;#latest-stableis the alpha line with every release)
orgit clone --branch stable+bun install && bun link. Installed by mistake?gbrain doctorgives the fix.
Schema not migrated (#218)? Rungbrain apply-migrations --yes --no-autopilot-install; if it exits 1, rungbrain doctor --json, not another--yes(wedged: relay its fix).

bun install -g github:garrytan/gbrain#stable
gbrain setup claude-code 
#
 or: gbrain setup codex

gbrain init --pglite --no-embedding 
#
 any other harness, or no agent

gbrain setupshows what it will write first (--dry-runpreviews,--removeundoes), creates a keyless brain only if none exists, wires MCP, hooks and a brain-first block in the agent's instruction file (--no-instructionsskips it), and smoke-tests them (setup guide). For any other coding agent, paste:

Add GBrain memory to this existing agent. Read and follow:
https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
Keep my current identity and instructions, start keyless, and show me the
search-mode choice. Verify a remember/recall round trip with real GBrain calls.

Postgres, thin clients, API keys and upgrades:docs/INSTALL.md. Agents:INSTALL_FOR_AGENTS.md. Memory-only walkthrough:give your coding agent a memory.

### CLI standalone (no agent)

gbrain init --pglite --no-embedding 
#
 keyless; no server, no Docker

gbrain import 
~
/notes/ --no-embed 
#
 index your markdown

gbrain search 
"
a phrase from a note
"
 --json
gbrain doctor 
#
 verify health

### Optional: a new personal agent

To have GBrain create anew persistent personal agentwith identity files and its own private GitHub repo, open Codex (CLI or ChatGPT desktop) or Claude Code in a new, empty folder and paste:

Read and follow every step of:
https://raw.githubusercontent.com/garrytan/gbrain/stable/BOOTSTRAP_FOR_AGENTS.md
Goal: set yourself up as my persistent personal agent in this folder, with gbrain
as your memory. Interview me before writing any identity file — never invent
answers. Ask before anything destructive. You are not done until
`gbrain bootstrap verify` exits 0.

The repo is not a complete backup; see thebootstrap guide. For the always-on version (24/7 ingestion and the overnight dream cycle on a server with 8GB+ RAM and its own API usage), run GBrain underOpenClaworHermesand point it atINSTALL_FOR_AGENTS.md; thepersonal-brain tutorialwalks it end to end.

### Connect GBrain to your AI client (MCP)

* Local stdio client:gbrain setup claude-codeorgbrain setup codexregistersgbrain serve(lists the memory verbs;--surface fulllists every tool) behind gbrain's launcher, so a session opened in a cloned repository never loads that repository'sbunfig.tomlor.env, and adds the brain-first instructions: agents seldom call a brain nobody told them about. Cursor, Windsurf and other stdio clients take"$(command -v gbrain)" serve --surface starter --advertise verbs.
* Plugins with curated skills:Codexcodex plugin marketplace add garrytan/gbrain@codex-plugin+codex plugin add gbrain@gbrain; Claude Code/plugin marketplace add garrytan/gbrain+/plugin install gbrain@gbrain.
* This brain from anywhere:gbrain mcp exposepublishes it on your Tailscale tailnet as a user service (--funnelfor cloud agents such as Grok Bot, Muse and ChatGPT).Guide.
* A brain on another host:gbrain connect https://your-host/mcp --token gbrain_xxx --install(add--agent codexfor Codex). Hosted brains usenative OAuth or a private handoff; dashboard, clients and permissions live inMCP administration.

Per-client guides:Claude Code·Codex·ChatGPT·Claude Desktop·Claude Cowork·Perplexity·Hermes·OpenClaw·opencode·Grok Build·Grok Bot·Muse·everything MCP.

## Two ways to query your brain

Raw retrieval (what most personal-knowledge tools ship) and a synthesis layer that gives you an actual answer. They serve different jobs.

#
 raw retrieval: top pages by hybrid score, no answer-generation call

gbrain search 
"
who's working on AI agents at portfolio companies?
"

#
 brain layer: synthesized answer with citations and gap analysis

gbrain think 
"
who's working on AI agents at portfolio companies?
"

gbrain searchreturns the top retrieved pages, ranked by hybrid scoring (vector + keyword + RRF + source-tier boost + reranker). Use it when you want raw material to skim: agent context windows, citation lookups, finding a specific quote.

Configured embedding and reranking providers can still receive text and charge
for retrieval. Keyless keyword search needs no model API; synthesis requires a
configured chat capability. Seememory boundaries.

Search also tells you when its results are incomplete because projections are
still rebuilding or a bounded vector scan ran short. Ask your agent"Check
whether my search index is ready"; seesearch readiness and recoverybefore treating an empty result as proof that a page is missing.

gbrain thinkruns the same retrieval, then composes a synthesized answer across the results with explicit citations to the source pages AND an honest note on what the brain doesn't know yet. The gap analysis is the differentiator: the answer tells you when a page is stale, when a claim is uncited, when two pages contradict each other, when there's a hole you should fill.

Say to your agent:"What do we know about acme-example?"—"Tell me about alice-example before my meeting tomorrow"—"Search for who's working on AI agents."Your agent routes these to the brain automatically; you never type the commands yourself.

Why it compounds.Pair the brain layer withfind_trajectoryand you get answers like"how have the company's metrics changed AND what does the team look like right now AND what did they promise / share AND when did we last meet AND what's the value-add I can offer here": well-scored, well-cited, in one shot. That's the strategic moat. That's why building a 150K-page brain is worth the effort.

gbrain agent run "..."exposes the same surface to a sub-agent through the Minions queue, with crash-safe two-phase persistence. Same answers, durable.

## How to get data in

Start with an explicit fact or a notes folder; opt into connectors, capture, and enrichment separately.

Already have a company knowledge repository?Say to your agent:“Connect our
existing company brain, preserve its files, and show me the import plan first.”Trygbrain sources demo company-brainwithout keys or private data, then inspect
your committed Markdown withgbrain sources inspect <path> --profile company-brain.
Thecompany-brain ingestion guidecovers
explicit destination approval, typed relationships, and resumable verification.
It does not enable embeddings, sharing, schedules, or curation automatically.

Say to your agent:"Remember this with its source"—"What should I import first?"

Data ingestion guidecovers files, conversations, connectors, Google data, and capture commands.

## Your brain's shape (schema packs)

Most personal-knowledge tools force one fixed layout: their idea of "notes" + "people" + "tags." Drop a Notion export or your own years-old Obsidian vault on top, and the agent doesn't know what aProjects/folder means or whetherReading/is people or sources.

gbrain doesn't have a fixed layout.It ships with bundled schema packs and lets you author your own when none fit:

* gbrain-base-v2(default) — 15-type DRY/MECE canonical taxonomy (14 canonical +notecatch-all):person,company,media,tweet,social-digest,analysis,atom,concept,source,deal,email,slack,writing,project,note. Subtypes/format/origin pushed to frontmatter.
* gbrain-base(legacy) — the wider 24-type layout. Stays bundled for back-compat; brains on it can upgrade viagbrain onboard --check --explain→gbrain jobs submit unify-types --params '{"target_pack":"gbrain-base-v2","apply":true}'(omit"apply":truefor a dry-run preview — that is the default).
* gbrain-recommended— extendsgbrain-basewith the 13 additional directories fromdocs/GBRAIN_RECOMMENDED_SCHEMA.md(source, place, trip, conversation, personal, civic, project, etc.). Activate withgbrain schema use gbrain-recommended.
* Your own pack—gbrain schema detectclusters your actual filesystem into proposed types,gbrain schema suggestruns an LLM pass over them, andgbrain schema review-candidates --applypromotes the ones you like. Three commands and the brain knows your shape. Authoring a successor pack (declaresmigration_from:so existing brains can opt in): seedocs/architecture/pack-upgrade-mechanism.md.

gbrain schema active 
#
 which pack is running, which tier set it

gbrain schema list 
#
 bundled + installed packs

gbrain schema detect 
#
 propose types matching your filesystem

gbrain schema suggest 
#
 LLM-refined proposals on top of detect

gbrain schema review-candidates 
#
 human gate: promote / rename / ignore

gbrain schema use my-pack 
#
 activate

Say to your agent:"My schema isn't matching my notes — propose new types from my corpus"—"Add a page type for lab results to my brain's schema."The schema-author skill runs the detect → suggest → review flow for you.

The active pack threads through every read + write path:parseMarkdowninfers page type from the pack's path prefixes;whoknowsscopes expert routing to types declaredexpert_routing: true;extract_factsruns only onextractable: truetypes. The retained search-cache key includes the pack name + version, but semantic result reuse is temporarily disabled. Switch packs and the brain re-interprets itself; switch back and nothing's lost.

Seven-tier resolution chain (per-call flag → env var → per-source DB key → brain-wide DB key →gbrain.yml→~/.gbrain/config.json→gbrain-basedefault). Full reference + authoring guide:docs/architecture/schema-packs.md.

## Tutorials

Step-by-step walkthroughs for getting the most out of GBrain. Each one takes you from zero to a working outcome, with concrete commands and real numbers.

* Set up your personal AI agent + brain from zero— the canonical full-stack install. Two GitHub repos, a Telegram bot, AlphaClaw on Render, OpenClaw + GBrain + Supabase. End-to-end in about 2 hours.
* Set up GBrain as your company brain— federated, multi-user, OAuth-scoped institutional memory for a 10-50 person team. About 90 minutes end-to-end.
* Auto-improve a skill withgbrain skillopt— treat aSKILL.mdas a trainable parameter. Generate a starter benchmark straight from the skill with--bootstrap-from-skill(or write your own), strengthen the judges, then watch the optimizer propose edits and keep only the ones that measurably score higher. ~20 minutes, ~$1 in API calls. Flag + cost + safety reference:docs/guides/skillopt.md.

More walkthroughs in progress: connecting an existing agent (Claude Code, Cursor, OpenClaw, Hermes) to a GBrain memory layer; setting up GBrain for VC dealflow with founder scorecards and meeting prep; migrating an existing Notion or Obsidian vault; indexing a codebase as a queryable code brain. Full tutorial index:docs/tutorials/.

Want to see a tutorial that isn't here yet?Open an issuedescribing the workflow you want documented.

## What it does (the loop)

 signal → search → respond → write → auto-link → sync
 (every (brain-first (informed (page + (typed edges (cron
 message) retrieval) by context) timeline) + backlinks) keeps fresh)

* Signal detector, after you opt in, captures durable ideas and entity mentions from substantive messages. Explicit remembering works without automatic capture; paid enrichment is a separate choice.
* Brain-first lookupbefore any external API call. The cheapest, fastest, most personal information source you have.
* Auto-linkextracts graph links for trusted local page writes. No LLM calls; pure pattern matching on page references such as[[people/alice-example]]. Unresolved extracted facts keep their provenance without inventing a backing page.
* Cron-driven enrichmentruns while you sleep: dedup people pages, fix citations, score salience, find contradictions, prep tomorrow's tasks.

The whole loop is described indocs/architecture/topologies.mdwith diagrams.

Say to your agent:"Set up autopilot"(installs the cron that runs the loop) —"Run dream"—"Did the dream cycle run?"

## Capabilities

GBrain combines keyword and semantic retrieval, typed graph traversal, optional cited synthesis, background jobs, and curated agent skills.

Say to your agent:"What search mode am I running?"—"Who works at acme-example?"—"What does my brain know about this project?"

Capability referencekeeps the commands, benchmark scope, cost controls, and feature-specific guides.

## Integrations

Data flowing into the brain. Each integration is a recipe — markdown + setup hints — that ships inrecipes/and is discoverable viagbrain integrations list.Say to your agent:"Set up voice calls into my brain"—"Wire my email and calendar into the brain"— your agent reads the recipe and walks the setup with you.

* Voice: Phone calls create brain pages via Twilio + OpenAI Realtime (or DIY STT+LLM+TTS). Setup recipe:recipes/twilio-voice-brain.md.
* Gmail + Calendar + Contacts (native): the google source kind syncs threads, events, and contacts through your own OAuth client and runs the open-loop engine on top (gbrain waiting). Setup:docs/guides/google-connect.md; recipes:recipes/email-to-brain.md,recipes/calendar-to-brain.md.
* Meeting notes + Slack channels (native): themeetingssource kind (Fireflies first) writes one page per meeting and theslacksource kind one page per channel per day, synced on a schedule, on brains with or without a Git repository. Setup:docs/guides/meeting-and-slack-sources.md.
* Email + calendar (webhooks): webhook handlers that route to brain signals.docs/integrations/meeting-webhooks.md.
* Embedding providers: Voyage (new-install default:voyage-4@ 1024d), OpenAI, OpenRouter, Google Gemini, Azure OpenAI, MiniMax, Alibaba DashScope, Zhipu, Ollama (local), llama.cpp llama-server (local), LM Studio, Together, and LiteLLM proxy. Pricing matrix + decision tree indocs/integrations/embedding-providers.md. Existing vectors are never converted by changing the default; use the explicitly approvedembedding migration.
* Rerankers: Voyagererank-3-litehosted (the default unlesssearch.reranker.modelis set; on inbalancedandtokenmax, sameVOYAGE_API_KEYas embeddings;gbrain config set search.reranker.model voyage:rerank-2.5restores the previous default), plus thellama-server-rerankerrecipe for fully-local cross-encoder rerank via llama.cpp running Qwen3-Reranker against the samegateway.rerank()seam. Setup walkthrough indocs/ai-providers/llama-server-reranker.md.
* Credential vault + gateway:gbrain credsmanages OAuth and API credentials in a local vault (recipes/credential-gateway.md); agent-side vault-aware secret distribution:docs/integrations/credential-gateway.md.
* MCP clients: every major MCP client is supported.docs/mcp/per-client setup.
* Memorable (procedural memory): optional, off by default. Your brain rememberswhathappened; Memorable makes your agent rememberhow— finished sessions become replayable procedures stored on your machine (in a standalone local store, or inside your brain database if you opt in), recalled when a similar task comes back. See the section below, anddocs/memorable-agents.mdfor the agent-facing detail.

### Memorable — remember how, not just what (optional)

Memorable stores replayable procedures from coding sessions. Its relay is off by
default and requires an explicit disclosure/consent step; it can send redacted
traces and query text off-machine. Read theMemorable integration guidefor installation, data flow, per-harness limitations, and removal.

Say to your agent:"Explain Memorable's data sharing before enabling it."

## Architecture

flowchart LR
 Repo[Markdown brain repos] --> Sync[Sync and parse]
 Sync --> Engine{Brain engine}
 Engine -->|default| PGLite[(PGLite)]
 Engine -->|shared or large| Postgres[(Postgres and pgvector)]
 Agent[AI agent or operator] --> Surface[CLI or MCP]
 Surface --> Ops[Contract-first operations]
 Ops --> Search[Hybrid retrieval]
 Ops --> Graph[Typed graph traversal]
 PGLite --> Search
 Postgres --> Search
 PGLite --> Graph
 Postgres --> Graph
 Search --> Synthesis[Synthesis and gap analysis]
 Graph --> Synthesis
 Synthesis --> Answer[Cited answer]

 
Loading

Two engines, one contract.PGLite (Postgres 17 via WASM, zero-config, default) for personal brains up to ~50K pages. Postgres + pgvector (Supabase or self-hosted) for shared, large or multi-machine brains. Both implement oneBrainEnginecontract (src/core/engine.ts); CLI and MCP share one op registry.

Canonical files preserve file-backed knowledge.Your brain repo holds the Markdown; the database is an index rebuildable from it, and git deletes become soft-deletes. DB-only pages, unresolved facts, history and operational state need a database backup:where your memory lives,system of record. Publish public subsets, share team mounts, or point a thin client at a colleague's brain. Topologies indocs/architecture/topologies.md.

Two organizational axes (brain ⊥ source).Abrainis a database (your personal brain, a team mount you joined). Asourceis a repo inside that brain. Routing uses.gbrain-sourcedotfiles and a 6-tier precedence chain. Diagrams indocs/architecture/brains-and-sources.md.

Why the graph matters.Vector search finds similar text; graph retrieval follows stored relationships. Extracted edges are evidence to inspect, not proof that a relationship is true. Graph freshness depends on the write path and maintenance described inmemory boundaries. Deep dive:retrieval architecture;entity recall.

## Troubleshooting

Start withgbrain doctor. For database access failures, usegbrain engine status --probeandgbrain db-repairbefore changing configuration.

Say to your agent:"Check my brain health and show me the repair plan before changing anything."

Troubleshooting referencecovers installation recovery, PGLite startup, embedding dimensions, locks, import failures, and sync.

## Docs

* docs/INSTALL.md— every install path, end to end
* docs/guides/bootstrap.md— the persistent-personal-agent bootstrap contract (interview, identity files, hooks, private repo, security posture, uninstall), plus local harness mode (gbrain bootstrap harness) for wiring framework-spawned Claude Code/Codex sessions to a running serve
* Anatomy of a page— frontmatter, timeline, facts;per-client facts
* docs/what-schemas-unlock.md— why schemas matter: 7 killer use cases, the structural argument for typed page kinds, the agent-co-curates pattern
* docs/schema-author-tutorial.md— 5-minute walkthrough: fork the bundled pack, add a custom type, backfill existing pages, prove the wiring viagbrain whoknows
* docs/architecture/— system design, topologies, retrieval theory
* docs/guides/— how-to runbooks (google connect, open loops, sub-agent routing, minion deployment, skill development, brain-first lookup, idea capture, diligence ingestion)
* docs/integrations/— connecting external data sources (voice, email, calendar, embedding providers)
* MCP task guide— deployment and per-client setup (Claude Desktop, Code, Cursor, ChatGPT, Perplexity, Cowork)
* MCP administration— owner dashboard access, client registration, OAuth, permissions, and token recovery
* Evalsandresearch— methods and results
* docs/ethos/— philosophy (thin harness, fat skills, markdown as recipes, origin story)
* AGENTS.md— entry point for non-Claude agents
* CLAUDE.md— entry point for Claude Code (deep operating context)
* CONTRIBUTING.md— contributor guide, test discipline, eval-capture mode
* SECURITY.md— install-path trust model, self-update integrity, automated scanning, OAuth threat model, hardening defaults

## Contributing

Runbun run testfor the fast loop,bun run verifyfor the pre-push gate,bun run ci:localto run the full Docker-backed CI stack locally. Detailed test discipline inCONTRIBUTING.md.

Community PRs are batched into release waves rather than merged one-by-one — see the community-PR-wave process indocs/RELEASING.md. Contributor attribution stays attached viaCo-Authored-By:trailers. We credit every accepted contribution inCHANGELOG.md.

If you find a bug or want a feature: open an issue first. Quick fixes (typo, doc bug, obvious regression) can go straight to a PR. Anything touching schema, retrieval ranking, MCP protocol, or the security boundary needs a design discussion in the issue first.

## License + credit

MIT. I built GBrain to run my OpenClaw and Hermes deployments — the production brain behind my AI agents.

Origin story:docs/ethos/ORIGIN.md.

Community PR contributors are credited inCHANGELOG.mdper release. Attribution for the retired provider's historical embedding and reranker integration remains in Git at6040075c6cb95be5881cc2e1b76ef7d71f4e5d29. Voyage AI for the asymmetric-encoding recipe template. Ramp Labs for the search quality improvements lineage.