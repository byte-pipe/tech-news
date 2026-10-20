---
title: 'GitHub - sickn33/agentic-awesome-skills: AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack validation, and planning, backed by 2,600+ agentic skills. Includes CLI, local MCP, catalog, plugins, and Workbench. · GitHub'
url: https://github.com/sickn33/agentic-awesome-skills
site_name: github
content_file: github-github-sickn33agentic-awesome-skills-aas-core-is-t
fetched_at: '2026-10-20T15:34:54.543440'
original_url: https://github.com/sickn33/agentic-awesome-skills
author: sickn33
description: AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack validation, and planning, backed by 2,600+ agentic skills. Includes CLI, local MCP, catalog, plugins, and Workbench. - sickn33/agentic-awesome-skills
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

3,257 Commits
3,257 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
plugins
.agents/
plugins
 
 
.claude-plugin
.claude-plugin
 
 
.github
.github
 
 
apps
apps
 
 
assets
assets
 
 
data
data
 
 
docs
docs
 
 
docs_zh-CN
docs_zh-CN
 
 
plugins
plugins
 
 
schemas
schemas
 
 
scripts
scripts
 
 
skill_categorization
skill_categorization
 
 
skills
skills
 
 
supabase
supabase
 
 
tools
tools
 
 
verification
verification
 
 
.env.local.example
.env.local.example
 
 
.gitignore
.gitignore
 
 
.snyk
.snyk
 
 
.vercelignore
.vercelignore
 
 
AGENTS.md
AGENTS.md
 
 
CATALOG.md
CATALOG.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
LICENSE-CONTENT
LICENSE-CONTENT
 
 
PRIVACY.md
PRIVACY.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
START_APP.bat
START_APP.bat
 
 
TERMS.md
TERMS.md
 
 
design-qa.md
design-qa.md
 
 
funding.json
funding.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
skills_index.json
skills_index.json
 
 
vercel.json
vercel.json
 
 
walkthrough.md
walkthrough.md
 
 
View all files

## Repository files navigation

# AAS Core — Agentic Awesome Skills

Find reusable instructions for your project, inspect their complete files, and keep an exact skill set you can review and reuse.

Agentic Awesome Skills is a library of 2,715+ installableSKILL.mdplaybooks. AAS Core helps Codex or Claude search the complete local catalog, record the skills the agent chooses, and preview a plan you can inspect before changing a target. Core does not rank or recommend skills.

Current release: V19.11.0.AAS Core supports local catalog inspection, agent-owned selection, stack validation, and plan preview. Apply and recovery remain experimental.Read the AAS Core preview guidefor setup and exact trust boundaries.

This README tracksmain. Features listed underUnreleasedrequire a later release; the versioned guide describes the published package.

This is an independent community project, not affiliated with or endorsed by Google. Google, Antigravity, Gemini, and related names describe compatibility and install targets. The GitHub repository is canonical; thehosted catalogand browser-local Workbench are companion discovery and review surfaces.

## Table of Contents

* Watch the Introduction
* Support the Project
* AAS Core: Agent-First Preview
* Installation
* Choose Your Tool
* Recommended Specialized Plugins
* Bundles & Workflows
* Browse 2,715+ Skills
* Troubleshooting
* Stable Skills Manifest v1
* Contributing
* Community
* Credits & Sources
* Top Contributors
* Repo Contributors
* Star History
* License

## Watch the Introduction

A 40-second introduction to Agentic Awesome Skills. Press play to watch it here on GitHub.

AAS-onboarding-Flashing-Lights.mp4

If GitHub's player stalls,watch the video on the AAS website.

## Support the Project

Help keep the catalog open, maintained, and available to the builders who use it.

Support AAS

What it helps fund

♥ Sponsor AAS

Ongoing maintenance, reviews, and release work

Buy Me a Coffee

Small, direct contributions from the community

Every contribution helps us keep the skills curated, the tooling tested, and the catalog useful for the next project.

Security tooling support:Snyk.

AI compute & model credits:Atlas Cloud(supporting media generation workflows viaatlas-cloud-media).

This project is tested with BrowserStack.

For a complete setup through your first skill selection and installation preview, followCodex setuporClaude Code setup.

## AAS Core: Agent-First Preview

Codex or Claude inspects your project and chooses exact skills. Every current catalog skill is individually searchable, readable, and available for agent selection. The read-onlycompose_stacktool validates the chosen IDs and structure in memory; a client or theaasCLI can persistaas-stack.jsonand optional selection evidence.aas stack validatechecks the manifest, whileaas stack planwrites an immutable preview for your review. Manifests have a technical maximum of 128 skills; Core does not rank or recommend candidates or install skills in this supported preview path.

Important

Structural and identity validity does not certify semantic fit, compatibility, setup correctness, operational safety, or safety to apply. Apply and recovery require experimental opt-in and remain outside the supported preview.

TheWorkbenchreviews stack and plan artifacts in browser memory without accessing your filesystem. See theCore guidefor tool contracts, capability coverage, and limits.

## Installation

### From selection to use

Start with AAS Core in Codex or Claude. Configure the local MCP using theCodexorClaudeguide. With the MCP available, ask the agent to inspect your project, compare relevant skills, and save the exact selection. Then validate its manifest and review the resulting plan before any installation. The first configuration command previews a change and returns an approval digest:

npm 
exec
 --yes --ignore-scripts --package=agentic-awesome-skills@19.11.0 -- aas mcp configure \
 --host codex \
 --scope user \
 --config /absolute/path/to/codex/config.toml \
 --cache-root /absolute/path/to/aas-cache

Use--host claudeand its configuration path for Claude. TheCore setup guideexplains approval, reconnection, validation, and planning. To hand the reviewed IDs to the direct installer, useaas stack install-previewas described in themanifest handoff; that command only prepares a--dry-runpreview and does not apply a Core plan.

### Install selected skills directly

If you already know the IDs, preview a focused install into your host's skill directory:

npm 
exec
 --yes --ignore-scripts --package=agentic-awesome-skills@19.11.0 -- \
 agentic-awesome-skills --release 19.11.0 --path .agents/skills \
 --skills brainstorming,systematic-debugging --dry-run

Review the preview, then repeat without--dry-runwhen ready. The direct installer does not consume or apply a Core plan. Antigravity's watched skill directory can overload its context, so its default target requires a selected set, a filter, or an explicit--alloverride. See theinstallation guideandsecurity guidancefor other targets, auditing, and failure modes.

## Choose Your Tool

Use the path for your agent. Core setup is available for Codex and Claude; the other rows show direct install targets or plugin options.

Tool

Install

First Use

Claude Code

AAS Core local MCP preview
, direct install, or Claude plugin marketplace

Ask Claude to choose and compose an AAS stack

Cursor

npx agentic-awesome-skills --cursor

@brainstorming help me plan a feature

Gemini CLI

npx agentic-awesome-skills --gemini

Use brainstorming to plan a feature

Codex CLI

AAS Core local MCP preview
 or 
npx agentic-awesome-skills --codex

Ask Codex to choose and compose an AAS stack

Autohand Code

npx agentic-awesome-skills --path ~/.autohand/skills
 or 
--path .autohand/skills

Use brainstorming to plan a feature

Antigravity IDE

npx agentic-awesome-skills --antigravity --skills <ids> --dry-run

Ask an MCP-enabled agent to choose exact IDs first

Antigravity CLI (
agy
)

npx agentic-awesome-skills --agy

/brainstorming help me plan a feature

Kiro CLI

npx agentic-awesome-skills --kiro

Use brainstorming to plan a feature

Kiro IDE

npx agentic-awesome-skills --path ~/.kiro/skills

Use @brainstorming to plan a feature

GitHub Copilot

gh skill install sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md --agent github-copilot --scope user --pin v14.2.0
 (preview)

Ask Copilot to use brainstorming to plan a feature

OpenCode

npx agentic-awesome-skills --path .agents/skills --category development,backend --risk safe,none

opencode run @brainstorming help me plan a feature

AdaL CLI

npx agentic-awesome-skills --path .adal/skills

Use brainstorming to plan a feature

Custom path

npx agentic-awesome-skills --path ./my-skills

Depends on your tool

See the host guides, includingClaude Code,Cursor,Codex, andGemini CLI, for complete setup.

## Recommended Specialized Plugins

Choose a focused plugin for the domain you are working in. These packages are available for Claude Code and Codex; compatible bundles also have a standard Agent Plugins manifest. See theplugin guidefor installation and host support.

Plugin

Skills

Best for

AAS Web App Builder

10

Frontend and full-stack developers shipping modern web apps.

AAS Product Design Studio

10

Product UI, brand, portfolio, accessibility, and richer visual work.

AAS Security Engineer

10

Authorized security testing, audit, and hardening.

AAS Secure App Builder

9

Developers who want security embedded while building features.

AAS Documents & Presentations

9

Office files, document conversion, decks, and slide workflows.

AAS Data Analytics

10

Product analytics, SQL, dashboards, and experiments.

AAS Agent & MCP Builder

10

Agentic apps, MCP tools, RAG systems, and evaluation loops.

AAS QA & Test Automation

10

Test suites, browser automation, and QA stabilization.

AAS DevOps & Cloud

10

Infrastructure, deployments, and operational workflows.

AAS Accessibility & Inclusive UX

8

WCAG audits, automated scans, screen-reader checks, and accessible QA.

AAS API Platform Builder

10

API design, OpenAPI contracts, auth, security, load tests, and observability.

AAS SaaS Launch & Revenue

10

SaaS MVPs, pricing, payments, analytics, lifecycle, referrals, and SEO.

AAS AI Product & Evaluation Ops

10

AI product metrics, evals, tracing, experiments, and model-quality loops.

Browse theplugin roadmap,live plugin catalog, or generatedplugins/tree for the full set.

## Bundles & Workflows

Bundles suggest related skills; workflows describe the order to use them. They are guidance for selecting and running skills, not additional packages to install.

* Bundlesgroup skills by role or goal, such asWeb Wizard,Security Engineer, andOSS Maintainer.
* Workflowsgive ordered playbooks for planning, shipping, testing, and auditing;workflow metadatais available for integrations.
* If too many installed skills overload Antigravity, follow theselective activation guide. For other hosts, preview a smaller exact install or use the installer's--risk,--category, and--tagsfilters.

## Browse 2,715+ Skills

Explore the complete library in thehosted catalogorCATALOG.md. The canonical playbooks live inskills/;skills_index.jsonprovides machine-readable discovery. UseGetting StartedandUsagefor first steps, or theWorkbenchto inspect a saved Core stack and plan in your browser.

For narrower comparisons, seeClaude Code skills,Cursor skills, and thelibrary comparison.

## Troubleshooting

* Core setup and trust boundaries
* Installation and everyday use
* Windows context and truncation recovery
* Linux/macOS overload and selective activation
* Plugin compatibility and installation
* Security and antivirus alerts

## Stable Skills Manifest v1

Host integrations that load individualSKILL.mdfiles can useskills_index.json, thev1 schema, and thecompatibility mirror. This direct-host discovery manifest is separate fromaas-stack.jsonand the AAS Core catalog. Read thediscovery contractbefore integrating.

## Contributing

* Add new skills underskills/<skill-name>/SKILL.mdand followCONTRIBUTING.md.
* Start from theskill templateand runnpm run validatebefore a PR.
* Keep source PRs free of generated registry artifacts. Skill content and risky guidance require manual logic and safety review alongside automated checks.

## Community

* Discussionsfor questions, ideas, and examples.
* Issuesfor reproducible bugs and actionable improvements.
* Follow @AASkills_ on Xfor project updates and examples, or@sickn33for releases.
* CODE_OF_CONDUCT.mdfor community expectations;SECURITY.mdfor security reports.

## Credits & Sources

We stand on the shoulders of giants.

👉View the Full Attribution Ledger

Source credits stay here for attribution and auditability. Repository contributor credit lives separately inRepo Contributors.

Key source families include:

* Official AI platform and tool repositories
* Security, web, infrastructure, data, design, and automation communities
* Independent skill authors and open-source maintainers

Official Sources

### Official Sources

* Taasky: MIT-0 official source for thetaaskyskill - negotiate meeting times, prices and dates with another person or their agent through the hosted Taasky MCP server (no account or key). Offers and counters run on their own; every accept, reject or withdraw is confirmed by the person in Telegram first.
* fclairamb/solidping-plugin: MIT official source for thesolidpingskill - uptime checks across 40+ types, results, incidents, diagnosis and status pages through the hosted SolidPing MCP server, with every write confirmed by the person first. SolidPing itself is AGPL-3.0.
* Outreachgenie/outreachgenie-linkedin-mcp: MIT source foroutreachgenie-list-audit, a read-only saved-list and template audit with local Python reports. Connected use requires an OutreachGenie workspace and compatible MCP host.
* Aident-AI/aident-skill: MIT official source for theaident-loadoutskill - search actions across apps the user connected inAident Loadout, read live schemas, check connections and cost before running, and require approval for side effects, through the hosted Aident MCP server.
* SergiuPogor/curlshot-mcp: MIT official source for thecurlshotskill - web page screenshots, PDFs and scrolling videos, plus HTML/Markdown rendering, through the hosted CurlShot API or MCP server. The hosted service has separate terms.
* AltoRank/altorank: AGPL-3.0 official source for thealtorankskill - SEO/AI-search readiness audits, Search Console reads, keyword research and draft creation into a person-reviewed queue through the hosted AltoRank MCP server.
* getchordlabs/chord: MIT official source for thechord-onchain-tradingskill - DEX market data, best-route swap quotes and unsigned swap transactions on eight EVM chains through the Chord API; the skill never signs or sends. The hosted API and server have separate licensing.
* Krexa-xyz/skills: MIT-0 official source for thekrexaskill - turn a trading idea, post or video into fixed rules, backtest and paper-trade them, and request a user-approved live trading agent through Krexa's hosted MCP server.
* tuantqse90/moltnode-mcp: MIT official source for themoltnode-chain-readerskill - keyless JSON-RPC reads on 31 blockchains through MoltNode by Chord, plus Chord swap quotes with an unsigned transaction and simulation. The hosted gateway and server have separate licensing.
* arcmira/mcp: Apache-2.0 plugin source forarcmira-find-quotes, YouTube and podcast quote research with timestamped sources. The hosted service and server have separate licensing.
* Pazificateur69/tokenleak: Official tokenleak source for thetokenleakskill - token-lean working rules that cut the context a coding agent re-sends on every call (big reads, noisy logs, re-reads, serial calls), with a published A/B benchmark (MIT).
* beatra-ai/ai-headshot-generator-skill: Official Beatra source for theai-headshot-studioskill - paid, hosted work installed from a digest-pinned 0.1.7 archive byte-identical to commita8818c3with self-update disabled before first use (MIT-0).
* uxkin/agent: Official UXKIN source for the freeuxkin-researchskill — research real iOS app screens, user journeys and website design systems before designing UI (MIT).
* loootai/looot-skills: Official looot skills - search, price and run 2,500+ data API endpoints (work emails, company search, SERP, web pages) from one prepaid balance.
* CosmoBlk/email-marketing-bible: Official Email Marketing Bible source for theemail-marketing-bibleskill - data-backed email marketing for agents: automation flows, deliverability triage, copy de-slopping, AI email design, compliance and 19 industry playbooks, with ESP control via MCP behind explicit send-approval gates (MIT).
* lognorm/lognorm-mcp: MIT official source for thelognormskill — work a site's SEO and AI-visibility (GEO) backlog through the hosted LogNorm MCP server: audits, fixes, content and AI-answer tracking.
* NygenAnalytics/scarf: Official Scarf source for thescarf-single-cellskill - out-of-core single-cell RNA-seq analysis with Scarf's Zarr DataStore on local disk or object storage, immutable provenance-tracked artifacts, audited QC, clustering, markers and comparisons (BSD-3-Clause).
* anup-a/agent-artifacts: Official byagent source for thebyagentskill - publish agent-written Markdown or HTML as a shareable link with thebyagentCLI, read readers' line comments back, edit, republish to the same link and resolve; pages are public unless--privateand comment text is treated as untrusted data (MIT).
* prateeks367/voicemoat-skills: Official VoiceMoat source for eight Twitter/X and LinkedIn skills (write-in-my-voice,turn-this-into-a-thread,same-idea-both-platforms,repurpose-into-a-post,define-my-content-pillars,why-did-this-post-flop,get-seen-in-replies,draft-my-comments). They draft in your own voice, write threads, cross-post, repurpose long content, pick content pillars, diagnose a post that underperformed, and write replies and comments worth reading; each works from pasted text alone, and an optional paid VoiceMoat connector adds voice scoring and preview-gated publishing (MIT).
* cloudishai/skills: Official Cloudish source for thecloudishskill - deploy a Dockerfile, source folder, or existing image as a running container at a live URL, built server-side, with confirmation before the first deploy and before spending credits; uploads the build context and spends prepaid credits (MIT).
* voygr-tech/placecall: Official PlaceCall source for theplacecallskill - place real outbound phone calls to US businesses through the PlaceCall REST API (reservations, inquiries, quotes), follow the call and return the structured outcome and transcript; paid API, real calls ring real phones (MIT).
* gongdear/cline-pilot: Official source for thecline-pilotskill - proxy-drive Cline CLI coding tasks serially, monitor long runs against git/test evidence instead of self-report, relay decision points, and learn per-project-tag preferences in git-ignored private state (MIT).
* bosmdavid-gif/dropthehassle-skill: Official DropTheHassle source for thedropthehassle-publishskill - check that a folder is a finished static build, publish it to a free HTTPS link, hand the human the claim link and verify it is live; the agent never pays (MIT).
* busabase/skills: MIT source for thebusabaseskill — authorized MCP workspace operations, permission-aware ChangeRequests, and canonical-versus-pending readback.
* jcaiagent7143-ui/linkdigest-mcp: Official LinkDigest source for thelinkdigest-social-link-readerskill - read one public Xiaohongshu, Douyin, TikTok, YouTube, X or WeChat article link into text (transcript, image text, key points with checked quotes, coverage receipt) through the paid hosted LinkDigest API or MCP server with the user's own key (MIT).
* metalbear-co/skills: Official mirrord skills source for themirrordskill - run a local process inside a live Kubernetes pod's network, env and traffic, with confirmation before traffic-stealing or cluster-modifying steps (MIT).
* beatra-ai/viral-video-remake-skill: Official Beatra source for theviral-video-teardown-remakeskill - paid, hosted work installed from a digest-pinned 0.3.1 archive byte-identical to commit46f7875with self-update disabled before first use (MIT-0).
* beatra-ai/photo-to-anime-skill: Official Beatra source for theai-photo-restylerskill - paid, hosted work installed from a digest-pinned 0.1.4 archive byte-identical to commit87bc4c4with self-update disabled before first use (MIT-0).
* beatra-ai/ai-voice-cloning-skill: Official Beatra source for thevoice-cloning-studioskill - paid, hosted work installed from a digest-pinned 0.2.1 archive byte-identical to commit64923d9with self-update disabled before first use (MIT-0).
* beatra-ai/multilingual-voiceover-skill: Official Beatra source for theai-multilingual-dubbingskill - paid, hosted work installed from a digest-pinned 0.1.9 archive byte-identical to commit030ec84with self-update disabled before first use (MIT-0).
* beatra-ai/ai-voiceover-generator-skill: Official Beatra source for thevoiceover-narration-studioskill - paid, hosted work installed from a digest-pinned 0.1.9 archive byte-identical to commit0c44adfwith self-update disabled before first use (MIT-0).
* beatra-ai/ai-podcast-voiceover-skill: Official Beatra source for theai-podcast-voiceoverskill - paid, hosted work installed from a digest-pinned 0.1.7 archive byte-identical to commitddca11ewith self-update disabled before first use (MIT-0).
* beatra-ai/ai-image-generator-skill: Official Beatra source for theai-image-generation-studioskill - paid, hosted work installed from a digest-pinned 0.1.4 archive byte-identical to commit13c7b9bwith self-update disabled before first use (MIT-0).
* beatra-ai/ecommerce-product-images-skill: Official Beatra source for theecommerce-listing-image-setskill - paid, hosted work installed from a digest-pinned 0.2.0 archive byte-identical to commitef9056dwith self-update disabled before first use (MIT-0).
* beatra-ai/ai-poster-maker-skill: Official Beatra source for theposter-design-studioskill - paid, hosted work installed from a digest-pinned 0.1.3 archive byte-identical to commit7a6337fwith self-update disabled before first use (MIT-0).
* beatra-ai/ai-music-generator-skill: Official Beatra source for themusic-generation-studioskill - paid, hosted work installed from a digest-pinned 0.1.8 archive byte-identical to commitfee8fbfwith self-update disabled before first use (MIT-0).
* beatra-ai/ai-media-generator-skill: Official Beatra source for thebeatraskill - paid, hosted work installed from a digest-pinned 2.8.8 archive byte-identical to commit69afbfewith self-update disabled before first use (MIT-0).
* beatra-ai/ai-product-photography-skill: Official Beatra source for theproduct-photo-studioskill - paid, hosted work installed from a digest-pinned 0.2.0 archive byte-identical to commit1490364with self-update disabled before first use (MIT-0).
* beatra-ai/ai-logo-maker-skill: Official Beatra source for theai-logo-makerskill - paid, hosted work installed from a digest-pinned 0.1.7 archive byte-identical to commit89bf762with self-update disabled before first use (MIT-0).
* beatra-ai/lyrics-to-song-skill: Official Beatra source for thesuno-lyrics-to-songskill - paid, hosted work installed from a digest-pinned 0.2.0 archive byte-identical to commit2facaacwith self-update disabled before first use (MIT-0).
* vanshyadav1408/Omentir: Official Omentir source for theomentir-linkedin-outreachskill - LinkedIn prospecting and outreach through the hosted Omentir MCP server (OAuth): find and score leads, draft messages, and check campaigns, research and drafts only by default, never signs into LinkedIn (MIT).
* Spicy-API/nsfw-ai-skill: Official SpicyAPI source for thensfw-ai-spicyapiskill — adult (18+) image, image-to-video and image-edit generation through the SpicyAPI API with quote-before-spend and adults-only / consent rules (MIT).
* Atlas Cloud: Official source for theatlas-cloud-mediaskill — asynchronous image and video generation through the Atlas Cloud API.
* sandbaseai/cli: Official source for thesandbase-mcpskill - discover, inspect, and invoke 2,000+ AI models and APIs through a local MCP bridge with explicit schema and cost checks (Apache-2.0).
* vostride/agent-qa: Official Agent QA skills for authoring natural-language web and mobile tests, evidence-backed run triage, and scoped debug/fix workflows (FSL-1.1-ALv2, Apache-2.0 after two years).
* uizze/uizze: Official UIZZE source for the freeanti-ui-slopskill—product-specific UI references, design contracts, required states, and a hard finish gate grounded in 800,000+ real web and iOS screens (MIT).
* anthropics/skills: Official Anthropic skills repository - Document manipulation (DOCX, PDF, PPTX, XLSX), Brand Guidelines, Internal Communications.
* anthropics/claude-cookbooks: Official notebooks and recipes for building with Claude.
* Orkas-AI/Orkas-VideoStudio: Official source for thevideo-routerskill - choose and lock generation, deterministic composition, supplied-footage editing, or an automatic cross-modal production plan (MIT).
* remotion-dev/skills: Official Remotion skills - Video creation in React with 28 modular rules.
* vercel-labs/agent-skills: Vercel Labs official skills - React Best Practices, Web Design Guidelines.
* openai/skills: OpenAI Codex skills catalog - Agent skills, Skill Creator, Concise Planning.
* bekservice/Famulor-Skill: Official Famulor skill for tenant-safe operation of its hosted MCP server across assistants, communication history, campaigns, knowledge, automations, telephony, and workspace administration (MIT).
* supabase/agent-skills: Supabase official skills - Postgres Best Practices.
* microsoft/skills: Official Microsoft skills - Azure cloud services, Bot Framework, Cognitive Services, and enterprise development patterns across .NET, Python, TypeScript, Go, Rust, and Java.
* Simon-He95/markstream-vue: Official Markstream skill for installing streaming Markdown renderers across Vue, React, Svelte, Angular, Nuxt, Next.js, and Vue 2 applications (MIT).
* nowork-studio/NotFair: Official source for theseo-driftskill - dated SEO baselines and regression detection across rankings, indexation, metadata, directives, schema, and on-page elements (MIT).
* MiniMax-AI/cli: Official MiniMax CLI - text, image, video, speech, music, vision, and web-search workflows for MiniMax models and APIs.
* google-gemini/gemini-skills: Official Gemini skills - Gemini API, SDK and model interactions.
* apify/agent-skills: Official Apify skills - Web scraping, data extraction and automation.
* BuyWhere/buywhere-mcp: Official BuyWhere MCP server — search and compare products from Singapore, SEA, and US markets via Model Context Protocol.
* expo/skills: Official Expo skills - Expo project workflows and Expo Application Services guidance.
* huggingface/skills: Official Hugging Face skills - Models, Spaces, datasets, inference, and broader Hugging Face ecosystem workflows.
* longbridge/skills: Official Longbridge Securities skills - real-time quotes, charts, fundamentals, portfolio analysis, options, and market workflows for HK, US, A-share, and SG markets.
* makeev/alphai-claude-skills: Official AlphAI skills - stock briefs, market pulse, SEC Form 4 insider scans, two-ticker read-across, and news alerts through the hosted AlphAI MCP server (relevance-scored financial news, filing-verified earnings reads) (MIT).
* HasData/hasdata-cli: Official HasData CLI and API guidance for search, scraping, ecommerce, travel, jobs, local business, and structured web data workflows.
* runapi-ai/cli-skill: Official RunAPI CLI skill - generate AI images, videos, and music/audio from agent workflows, plus run other model API jobs.
* neondatabase/agent-skills: Official Neon skills - Serverless Postgres workflows and Neon platform guidance.
* prisma/skills: Official Prisma skills - Prisma Postgres setup, Prisma ORM, Prisma Compute deploys, and Client/CLI workflows.
* Skyvern-AI/skyvern: Official Skyvern browser automation skill — AI-powered browser control using Vision LLMs and computer vision for navigating sites, filling forms, and extracting structured data.
* scopeblind/scopeblind-gateway: Official Scopeblind MCP governance toolkit - Cedar policy authoring, shadow-to-enforce rollout, and signed-receipt verification guidance for agent tool calls.
* Forward-Future/loop-library: Official Loop Library skill - find, adapt, and design bounded AI-agent feedback loops with verification, stop rules, guardrails, and handoffs (MIT).
* agent-frontier/wgm: Official wgm protocol skill - governed build loops with triage, alignment, planning, deterministic backpressure, holdout-scenario judging, and handoff audits (MIT).
* Instant-Expert/skills: Official Instant Expert source for theask-human-expertskill - ask real executives, operators and domain experts a question for a written or voice answer or a short call, with a free test mode and the user's approval before every paid order (MIT-0).
* browser-act/skills: Official BrowserAct skills - authenticated browser automation, JavaScript-rendered extraction, screenshots, parallel session isolation, verification handling, and human handoff (MIT).
* masakaai/jet-browser: Official Jet Browser skill and Apache-2.0 source - isolated WPE WebKit sessions with ordered JSONL, native input, semantic DOM inspection, screenshots, and reproducible offline runtime checks.
* browserbase/skills: Official Browserbasecompetitor-analysisskill - Browserbase Search API competitor discovery, research lanes, matrices, screenshots, and HTML reports (MIT).
* dair-ai/dair-academy-plugins: Official DAIR Academy plugin skills imported as standalone skills - image generation, adaptive learning, lesson artifacts, LLM council deliberation, survey papers, wiki building, and YouTube study notes (MIT).
* weaviate/agent-skills: Official Weaviate skills - vector database operations, semantic and hybrid search, data imports, RAG cookbooks, agentic RAG, multimodal PDF search, and async client patterns (BSD-3-Clause).
* pilot-protocol/pilotprotocol: Official Pilot Protocol overlay network - agent addressing, encrypted P2P messaging, NAT traversal, and an installable agent app store (AGPL-3.0).
* Xquik-dev/x-twitter-scraper: Official Xquik skill for X data workflows - tweet search, user lookup, follower export, media downloads, MCP, webhooks, OpenAPI, and SDK setup (MIT).
* Modellix/modellix-plugin: Official Modellix skill - authenticated, paid AI image and video generation through the Modellix CLI (MIT).
* replynodes/replynodes-agent-skills: Official ReplyNodes source for theurl-to-markdownskill - fetch a public webpage as clean Markdown for reading, summarizing, quoting, or citing while preserving the source URL (MIT).
* beatra-ai/talking-avatar-video-skill: Official Beatra source for thetalking-avatar-videoskill - paid, hosted work installed from a digest-pinned 0.2.1 archive byte-identical to commit251c968with self-update disabled before first use (MIT-0).
* beatra-ai/beatra-skills: Official Beatra source for thebeatra-ai-video-studioskill - paid, hosted AI video generation, editing, and extension, installed from a digest-pinned 1.2.5 archive byte-identical to commit95d662fwith self-update disabled before first use (MIT-0).
* cohesivity-org/cohesivity-skill: Official Cohesivity skill - agent provisioned backend infrastructure covering Postgres, hosting, auth, realtime, storage, cron, email, and AI model APIs over one HTTP API (MIT).
* ASI2030/Fact-Check-X: Source for thefact-check-x-completeworkflow - claim-level AI answer comparison, citation-fidelity review, and public primary-source verification without bundled browser automation (Apache-2.0).
* happy520ai/unified-ai-system: Official source for theunified-ai-gatewayskill - governed Codex MCP tools for provider-free prompt enhancement, credential-free gateway health, readiness, fake-provider chat, knowledge, workflow, and workforce evidence (Apache-2.0).
* testdriverai/testdriverai: Official TestDriver source for thetestdriver-e2e-testingskill - author, run, and debug end-to-end tests that drive browsers and native apps in a real desktop sandbox with AI vision and natural-language element descriptions (Apache-2.0).
* HEOJUNFO/ai-film-crew: Official source for thefilm-crewskill - run a video idea past seven film-crew roles and get a shot list with one model-ready prompt per shot, plus prompt fixes and reroll diagnosis for Wan, LTX, Kling, Veo, Seedance, Hailuo, and Runway (MIT).
* hermes-labs-ai/lintlang: Official source for thelintlang-auditskill - deterministic, zero-LLM static auditing of agent instructions, tool definitions, and embedded Python prompts, reporting finding codes and locations without editing files or calling a model (Apache-2.0).
* target1m/traderspy-mcp: Official TraderSpy source for six crypto market research skills (traderspy-*) - market briefings, technical analysis, screening and backtests, AI signals, top-trader positioning, and position checks through the hosted, read-only TraderSpy MCP server (MIT).
* MohammadHijjawi97/since-cutoff: Official source for thesince-cutoffskill - lists which APIs of a project's pinned Python dependencies changed after the model's training cutoff, from a static diff of the two releases with no model calls, shows where the code uses them, and writes short AGENTS.md or CLAUDE.md notes (MIT).
* qrxcodes/qrx-mcp: Official QRX skill - turn a text prompt and a link into an artistic, branded QR code through the hosted QRX MCP server, checked to scan before it is returned (MIT).
* opencanviz/opencanviz-skills-repo: Official openCanviz source for theopencanviz-jsonskill - write an openCanviz video project as JSON with a standard-library Python builder and validator (text entrances, 22 scene transitions, motion presets, LaTeX math, plots, tables, rings, 22 example projects), then import it at opencanviz.com/create, where a free account builds and plays it as a narrated, animated explainer and the MP4 download needs a plan or a one-time export purchase (MIT).
* pangolin-spg/openclaw-skills: Source forpangolinfo-amazon-data-research.
* sendblue-api/sendblue-cli: Source forsendblue/sendblue-cli.

Community Contributors & Source Repositories

### Community Contributors

* timini/agentic-verification: MIT source for theagentic-verifyandagentic-test-auditskills - check a Python change by running every mutant of the changed lines and writing tests until they catch them, and audit a pytest suite for gaps, flaky and slow tests, and removal candidates checked on held-out mutants.
* UmarSiddiqui/obsess: MIT source for theobsessskill - a bounded perfectionist loop for one target that keeps the best evidence-backed attempt and stops on an attempt or time budget.
* openhook-dev/openhook-inbox: MIT source for theopenhookskill: disposable callback inboxes, event inspection and cursor-based waiting for authorized integration tests.
* huyanxius/logo-to-stickers: MIT source forlogo-to-stickers— brand marks become consistent paper-sticker characters with small visual stories, reference roles and fifteen real examples.
* moooai/takeout-coupon: MIT source for thetakeout-couponskill - Meituan, Ele.me/Taobao Shangou and JD Waimai hidden coupon feeds with verbatim taokouling codes and QR/H5 claim pages.
* moooai/trip-coupon: MIT source for thetrip-couponskill - Didi ride-hailing and hotel coupon feeds with verbatim codes and claim pages.
* moooai/movie-coupon: MIT source for themovie-couponskill - movie-ticket discount feeds for Chinese cinema platforms with verbatim codes and claim links.
* moooai/parcel-coupon: MIT source for theparcel-couponskill - courier and parcel-delivery coupon feeds with verbatim codes and claim pages.
* moooai/obtain-coupons-all-in-one: MIT source for theobtain-coupons-all-in-oneskill - one aggregated coupon feed across the four categories above.
* yumaheymans/carejobs-mcp: MIT source for thehealthcare-job-searchskill - US healthcare job and posted-pay lookup for nursing, CNA, allied health, therapy, imaging, pharmacy and physician roles through CareJobs.Now's free read-only MCP server or public CC BY 4.0 JSON endpoints.
* AshenJyy/antigravity-browser-bridge: Source for the Browser Bridge guide for authorized Edge/Chrome automation using a separately installed local extension and daemon (Apache-2.0).
* Reak-Z/mcd-secret-menu-lab: MIT community recipe-planning workflow for McDonald's China using an authorized MCP connection and explicit account-action boundaries.
* Kadajett/cockney: MIT source for thecockneyskill - terse Cockney-voiced replies and the smallest correct change (reuse, stdlib before dependencies, no speculative abstraction), switching to plain English for security and destructive-action warnings.
* estevecastells/awesome-copilot: MIT source for theinvokely-statisticsskill - find official statistical figures, series, comparisons and place rankings through the Invokely MCP server, and report each value with its period, unit and source citation. The originating contribution is open and unmerged upstream.
* morluto/rea: MIT source for thereverse-engineer-anythingskill - evidence-led native, managed, JavaScript/Electron, packaged, and browser investigations with explicit provider limits.
* stas4000/what-could-break: MIT source for thewhat-could-breakskill - find what a change breaks outside its own diff and prove the one fact that makes it safe by running real code. Includes material adapted from pstack by Lauren Tan (MIT).
* stas4000/tastegate: MIT source for thetastegateskill - pick a design direction, build on a craft floor, then render the page in headless Chromium at phone and desktop width and fail on overlap, sideways scroll, low contrast and AI-slop defaults. Direction rules derive from taste-skill (MIT) and the craft floor from impeccable (Apache-2.0).
* stefanautomateed/shipvela-codex: MIT source forshipvela-publish— owner-confirmed website publishing and exact deployment tracking through an already connected Shipvela account. The hosted service is proprietary and plan-limited.
* mdagnolops/1human-reels: MIT source for theagent-reelsskill - find credited animation and video references on 1human and consult a private library shared by a human and their creative agent; registration, saves, likes, comments and publication are state-changing and require prior owner authorization.
* alexyc9381/shark-skillandalexyc9381/court-skill: MIT sources for thesharkandcourtskills by Alex Chen (@nocodealex). Each is a panel of Claude sub-agents (investors, or a jury) that stress-tests an idea.
* ASCIT31/darkmoon-mcp-server: GPL-3.0 source for thedarkmoon-pentestskill — authorized autonomous pentest runs, status polling and findings triage on a self-hosted Darkmoon Pro instance through its MCP server.
* alapha888/session-handoff-kit: MIT source for thesession-handoffskill — structured handoff artifact for the next session, for use when context approaches capacity, before /clear or /compact, when switching tasks, or when ending a coding session.
* FlowLLM-AI/AxonX: Apache-2.0 source foraxonx— quantitative research plugin development, task execution, and artifact/lineage inspection through CLI and MCP.
* supercorp-ai/supercov: MIT source for thesupercovskill — line, branch and MC/DC coverage of a project's existing tests, used to write focused tests for the untested code.
* alapha888/agent-skills-en: MIT source fordeep-research-framework,five-axis-code-review,git-commit-message,meeting-notes, andtech-writing-proofread— concise English workflows for research reports, code review, commit messages, meeting minutes, and technical proofreading.
* Natchannnn/repository-engineering-skills: MIT source forrepo-foundationandrepo-native-refactor— repository-native implementation, contract-aware migrations, evidence-based review, and bounded cleanup.
* tomelias10/mcp-drift-check: MIT source for themcp-dependency-drift-auditskill — zero-execution review of mutable npm/npx package references in MCP configuration, with a manual static fallback and CI/SARIF guidance.
* wwewtech/chatexport-need-miner: Source for thechatexport-need-minerskill — community guidance and examples under MIT.
* socai-io/jev-social: Source for thejev-socialskill — read-only Jev/socai social research routing (MIT).
* work0r-ai/agent-kit: Source for theworkoraiskill — agent kit workflows (MIT).
* awss1i/assay: MIT source for theassayskill. Deterministic local QA that opens a web page you built in a real browser, drives every control, and reports where the page contradicts itself, with no tests to write, no API key, and no network.
* shitianfang/jev-use: Source for thejev-useskill - routing an agent loop's no-text judgment steps to the Jev judgment model via thejev_judge/jev_gateMCP tools, batched per state, with a typed escalation contract that hands writing and low-confidence steps back to the LLM (MIT).
* wwewtech/anti-slop-design: Source for theanti-slop-designskill - anti-AI-slop UI/UX engineering with token archetypes and a seven-axis quality gate (MIT).
* wwewtech/dali-short-address-commissioner: Source for thedali-short-address-commissionerskill — community guidance and examples under MIT.
* romankurnovskii/etemaro: Source of themeteora-dlmm-pool-screeningskill - read-only screening and ranking of Meteora DLMM pools from public APIs (MIT).
* wwewtech/eol-resistor-calculator: Source for theeol-resistor-calculatorskill — community guidance and examples under MIT.
* tubeagentkit/youtube-transcript-skills: Source for theyoutube-transcript-skillsskill - YouTube transcript fetching, video/channel search, channel browsing, and playlist extraction via the getyoutubetranscript.com API, free tier with no card required (MIT).
* wwewtech/esl-price-sync: Source for theesl-price-syncskill — community guidance and examples under MIT.
* Pranav-Nexus/antigravity-skill-porter: MIT source forskill-porter, adapted for conservative local bundle previews and complete support-file copying.
* 70v-Yoyo/md2video-audio-skill: Apache-2.0 community source formd2video-audio, converting Markdown into narrated MP4 video with synchronized slides and narration.
* wwewtech/marlin-bed-leveling: Source for themarlin-bed-levelingskill — community guidance and examples under MIT.
* onkarbadve/agy-auto: MIT community source foragy-auto, providing guarded Antigravity CLI permission automation with scoped approvals.
* wwewtech/oneroster-csv-validator: Source for theoneroster-csv-validatorskill — community guidance and examples under MIT.
* twoicewoo/awesome-copilot: Pinned MIT source for thebreak-ai-fix-loopsskill - bounded AI repair loops with stable failure fingerprints, real-path proof, negative controls, and rollback verification (MIT).
* chenli-yy/entropy-box-public: Source for theentropy-boxskill - grounded embodied-AI research and workflow assembly through Consult, Search, Lookup, Evidence, and the Panorama Graph, with public-service privacy and physical-system safety boundaries (CC BY 4.0).
* Junaid-PK/laravel-development-workflow: Source for thelaravel-development-workflowskill - root-cause Laravel bug fixes and repository-native feature work with regression coverage and risk-based verification (MIT).
* Sketchjar/stipple-agent-skills: Source for seven Stipple-backed document trust skills covering document forensics, identity-pack gaps, grounded extraction, citation checks, AI-text triage, adverse-media review, and AU/NZ tender matching, with explicit hosted-data and human-review boundaries (Apache-2.0).
* 263311487-ux/falsify: Source for thefalsifyskill - a scientific reasoning protocol for explicit hypotheses, adversarial checks, evidence grading, and calibrated conclusions (MIT).
* Ghost011118/project-state-governor: Source for theproject-state-governorskill - evidence-backed canonical project state across sessions, branches, reviews, and research cycles (Apache-2.0).
* sandbaseai/sandbase-skills: Source for themulti-source-searchskill - cross-validated research with explicit source diversity, confidence, conflicts, gaps, and an offline-checkable evidence ledger (Apache-2.0).
* sandbaseai/awesome-workbuddy: Source for theskill-security-auditskill - read-only-by-default review of Agent Skills, MCP servers, connectors, and extensions across permissions, provenance, credentials, data flow, and irreversible actions (CC0-1.0).
* alexprivalov/boost-asio-skill: Source for theboost-asio-proskill - version-aware async C++ networking with Boost.Asio and standalone Asio across coroutine, callback, and classicio_servicestyles (MIT).
* xiehuan123/dsh-deepread: Source for thedsh-deepreadskill - evidence-first analysis of articles, books, PDFs, and document sets with claim tracing, knowledge maps, and Feynman checks (MIT).
* xiehuan123/browser-extension-launch: Source for thebrowser-extension-launchskill - end-to-end Chrome extension product design, implementation, real-browser acceptance, packaging, and store-launch workflow (MIT).
* riffkit/skill: Official upstream source for theriffkitskill - short-form video riffing and UGC ad generation in nine natively generated languages (MIT).
* 5dive-ai/skills: Source for thecompile-knowledgeskill - durable, atomic, interlinked knowledge stores with explicit hygiene, provenance, expiry, and secret-handling boundaries (MIT).
* JanYork/using-lwc: Source for theusing-lwcskill - durable, source-grounded project memory with independently verified document and code graphs (Apache-2.0).
* saudademjj/luopan: Source for thetravel-plannerskill - Chinese-first travel itinerary planning with mandatory budget confirmation, source-traceable facts, workload-aware daily pacing, and rule self-checks (MIT).
* OJPalenzuela/agents-generator: Source for theagents-generatorskill - project-specificAGENTS.mdand companion rule generation with package-manager detection, monorepo handling, dry-run/update modes, backups, and validated commands (MIT).
* agentbody/skills: Source for thepeople-dataskill - LinkedIn and YouTube professional-profile and public business-contact research via the Agent Body MCP server (MIT).
* sudosubin/gh-attach: Source for thegh-attachskill - GitHub CLI uploads and downloads ofuser-attachments(screenshots, PDFs, zips, videos), producing repo-scoped URLs for PRs, issues, and READMEs, with GitHub Enterprise Server support (MIT).
* Continuum-AI-Corp/OrcaReplay: Source for theorca-replayskill - reading, replaying, and forking recorded coding-agent runs, so a question about what a past run did is answered from its trace rather than from memory (Apache-2.0).
* Continuum-AI-Corp/OrcaPromptVault: Source for thesystem-prompt-lookupskill - a dated archive of shipped AI products' system prompts and tool schemas, each labelled captured off the wire or reported by the model itself, so a claim about what an agent was instructed to do is answered from the artifact rather than from memory (AGPL-3.0).
* amElnagdy/review-skills: Source for thedebate-reviewandbabysit-prskills - two-model debate review of PRs/MRs with inline comments and automated babysitting of review rounds for GitHub, GitLab and Azure DevOps (MIT, docs-only — runtime not bundled).
* yylo-dev/yylo-skills: Source for 7 YYLO skills (ledger-tasks-yylo,plan-ledger-tasks-yylo,ralph-loop-yylo,understand-project-yylo,wiki-yylo,workflow-yylo,artifact-yylo) - repo-resident Kanban/task ledger, PDR planning, validated single-task execution loop, and wiki/workflow/artifact records with fail-closed Ledger boundaries (MIT, docs-only —scripts/kanban.shruntime not bundled).
* addyosmani/agent-skills: Source forconstraint-driven-development,interview-me,using-agent-skills— only names not already in the catalog (22/25 overlap with existing entries) (MIT).
* ayghri/i-have-adhd: Source for thei-have-adhdskill — ADHD-friendly output shaping (MIT).
* career-ops-hq/career-ops: Source for thecareer-opsskill — multi-CLI job-search command center (MIT, docs-only — Node runtime not bundled).
* zubair-trabzada/geo-seo-claude: Source for 14 GEO/SEO skills (geo-audit,geo-citability,geo-technical, …) — site audits and client reporting (MIT, docs-only;geo-updateself-installer excluded).
* BagelHole/DevOps-Security-Agent-Skills(compliance batch): Source for 19 governance/framework/continuity/auditing skills (MIT, docs-only).
* BagelHole/DevOps-Security-Agent-Skills(security batch): Source for 35 secrets, scanning, network, operations, and AI-security skills (MIT, docs-only).
* BagelHole/DevOps-Security-Agent-Skills(infrastructure batch): Source for 70 server, storage, database, networking, cloud, and local-AI infrastructure skills (MIT, docs-only).
* elementalsouls/Claude-BugHunter: Source for 83 bug-bounty/red-team skills (79 offensive withAUTHORIZED USE ONLY+ confirmation gates, 4 process skills) — recon, exploitation, and validation workflows across web, API, cloud, identity, and mobile attack surfaces (MIT, docs-only — helper scripts, commands, engine, and research assets not bundled).
* BagelHole/DevOps-Security-Agent-Skills(devops batch): Source for 39 CI/CD, orchestration, observability, release, and AI-ops skills (MIT, docs-only).
* amElnagdy/delegate-skills: Source for 18 delegation skills (delegate-setup+ 17 implementer relays for Claude/Codex/Cursor/OpenCode and 13 more) — multi-agent delegation and fleet orchestration with Node built-ins only, relay never commits (MIT, docs-only — runtime not bundled).
* zhaoxuya520/reverse-skill: Source for 43 security skills covering reverse engineering, binary analysis, offensive assessment orchestration, and threat-intelligence workflows, adapted with English metadata and upstream safety gates (MIT).
* abhinaykrupa/cowork-to-code-bridge: Source for thecowork-to-code-bridgeskill - consent-bound execution on the user's own machine with pinned provenance, narrow scopes, and explicit local-agent limitations (MIT).
* maleksaadi0109/hyprfedora: Source for thefedora-hyprland-installerskill - GPU-aware Fedora Hyprland installation, configuration, verification, repair, and removal workflows (MIT).
* merc1305/findMate: Source for thefind-complementary-foundersskill - private-first own-owner assessment, approved expiring profiles, and evidence-backed human founder matching (MIT).
* provencher/codex-skills: Source for theorchestrateskill - focused Codex multi-agent delegation with non-overlapping ownership, coordinator integration, and user-held approval gates (MIT).
* Phelan164/codex-howto: Source for themaintain-codex-wikiskill - review-first engineering knowledge with provenance, explicit capture and promotion, and deterministic structural checks (MIT).
* kotobuki09/instructree: Source for theinstructreeskill - local instruction-scope mapping, metadata and link validation, recursive Copilot import audits, and SARIF reports (MIT).
* 0xsarwagya/ontoly: Source for theontoly-software-graphskill - deterministic TypeScript software graphs, MCP-backed architecture review, request tracing, impact analysis, and dependency analysis (MIT).
* amElnagdy/guard-skills— Code Quality & Testing Guard Skills (by amElnagdy)
* cloudflare/security-audit-skill— Cloudflare Web Security Audit Skill (by Cloudflare)
* gooseworks-ai/goose-skills: Source for thecompetitor-ad-intelligenceandad-campaign-analyzerskills - evidence-labeled public ad research plus uncertainty-aware campaign diagnostics and bounded budget tests (MIT).
* supernovae-st/nika-agents: Official upstream source for thenikaskill and its deterministic, budget-aware AI workflow runner (MIT skill content; AGPL-3.0 engine).
* atdy/maoxuan-product-agent: Source for theproduct-decision-agentskill - Chinese-first product judgment across prioritization, growth, operations, data, delivery, and cross-functional collaboration, with 36 tested scenarios (MIT).
* hafiz-actyte/idea-autopsy: Source for theidea-autopsyskill - business-idea validation that hunts the one sentence that kills an idea before you build: kill-list check, five hard filters, free-AI one-prompt test, and live ad-market verification (MIT).
* cruisekkk/trading-ledger: Source for thetrading-ledgerskill - decision-quality trade journaling that captures entry thesis, plan, and emotion into the user's own Notion database (MIT).
* cruisekkk/time-ledger: Source for thetime-ledgerskill - natural-language time tracking parsed into the user's own Notion database with ask-instead-of-guessing reconciliation (MIT).
* mattpocock/skills: Source for 17 Matt Pocock workflow skills - codebase design, TDD, bug diagnosis, triage, PRDs, issues, prototyping, handoff, teaching, and skill-writing guidance (MIT).
* emilkowalski/skills: Source for Emil Kowalski design engineering skills - UI polish, motion review, animation standards, component craft, and high-taste frontend guidance (MIT).
* chaunsin/agent-skills: Source for thepre-release-reviewanddrizzle-migration-conflictskills - deploy-readiness audits and Drizzle Kit migration-conflict workflows (Apache-2.0).
* harshmaur/apify-reddit-scraper-skill: Source for theapify-reddit-scraperskill - Reddit posts, comments, subreddits and user profiles as structured data through theharshmaur/reddit-scraperApify Actor, with no Reddit API key, cost estimates before each run and date-window filters (MIT).
* addyosmani/agent-skills: Source for thebrowser-testing-with-devtoolsskill - Chrome DevTools MCP browser verification, profiling, network inspection, and frontend debugging guidance (MIT).
* stareezy-1/frontend-architecture-skill: Source for thefrontend-lighthouseskill - portable Lighthouse CI Core Web Vitals gates, performance budgets, and GitHub Actions reporting (MIT).
* bin1874/before-you-build-skill: Source for thebefore-you-buildskill - pre-coding product risk review across demand, alternatives, switching costs, channels, and validation steps (MIT).
* sparklingneuronics/sparkling-skills: Source for thedispatchskill - multi-CLI delegation from Claude Code to Codex, Antigravity, and Gemini agents (MIT).
* takeaseatventure/sql-sentinel: Source for thesql-sentinelskill - SQL warehouse cost and performance anti-pattern audits across BigQuery, Snowflake, Redshift, and Postgres (MIT).
* takeaseatventure/devops-skills: Source for thecron-doctorskill - cron expression diagnosis, validation, trap detection, and zero-dependency schedule analysis tooling (MIT).
* drogers0/gh-image: Source for thegh-imageskill - GitHub CLI image uploads that return canonicaluser-attachmentsembed URLs for PRs, issues, comments, and README screenshots (MIT).
* Genefold/arrowspace-skills: Source for thearrowspaceskill - spectral vector search using graph Laplacian eigenstructure for structurally aware retrieval (Apache-2.0).
* yaojingang/yao-meta-skill: Source for theyao-meta-skillskill - governed skill creation, refactoring, evaluation, packaging, review, and distribution workflows (MIT).
* connerkward/ckw-design-skill: Source for theckw-designskill - frontend design direction, design-system guidance, visual philosophy, spatial checks, usability review, and production UI polish workflows (MIT).
* connerkward/deterministic-design-skill: Source for thedeterministic-designskill - rendered UI layout and usability audits using deterministic measurement plus vision-judged review loops (MIT).
* connerkward/lookdev-auto-skill: Source for thelookdev-autoskill - automated visual tuning loops where a vision or video model rates rendered variants and suggests improvements (MIT).
* connerkward/lookdev-studio-skill: Source for thelookdevskill - human-in-the-loop visual and prose tuning through rendered variants, sliders, swatches, inline edits, and selection-driven refinement (MIT).
* connerkward/macos-screen-recorder-system-audio: Source for themacos-screen-recorderskill - macOS ScreenCaptureKit recording with system audio, CLI workflows, permission handling, and export guidance (MIT).
* connerkward/mcp-apple-notes: Source for theapple-notes-searchskill - semantic and keyword search, related-note discovery, bridge finding, entity threads, and cited synthesis across local Apple Notes via MCP (MIT).
* connerkward/screenstudio-alternative-skill: Source for thescreenstudio-altskill - open-source screen recording polish with auto-zoom, idle speed-up, cursor treatment, captions, and vertical export workflows (MIT).
* connerkward/web-media-getter-skill: Source for theweb-media-getterskill - unified search across free image, video, and GIF APIs with license-aware media selection guidance (MIT).
* xi-kari/crossframe-skill: Source for the CrossFrame Skill Suite - Chinese-canonical structural diagnosis, essay drafting, review, and companion workflows across relationships, organizations, institutions, public issues, and research notes (MIT).
* qinghui316/ecl-harness-engineer: Source for theecl-harness-engineerskill - ECL Agent Harness infrastructure for AI coding workflows, repository guidance, change tracking, lint checks, CI gates, and handoff docs (MIT).
* baskduf/FableCodex: Source for thecodex-fable5skill - Codex-native Fable-inspired workflow discipline for evidence-first implementation, goal tracking, review findings, verification gates, and prompt adaptation (AGPL-3.0-or-later).
* Suraj1235/open-dynamic-workflows: Source for theopen-dynamic-workflowsskill - open-source dynamic multi-agent workflow engine that plans, orchestrates, and adversarially verifies parallel AI coding agents across OpenCode, Codex, Antigravity, and VS Code (MIT).
* multica-ai/andrej-karpathy-skills: Source for theandrej-karpathyskill - English Karpathy-inspired LLM coding guidelines for simplicity, surgical changes, assumption surfacing, and verifiable success criteria (MIT).
* mskadu/opencode-agent-skills: Source for opencode behavior, permission, skill-suggestion, and smart Git automation skills.
* adelaidasofia/ai-brain-starter: Source for theingest-youtubeskill - YouTube transcript ingestion into markdown vaults with yt-dlp metadata, VTT cleanup, and capture-seed stubs (MIT).
* JDDavenport/context-kit: Source reference for thecontext-kitskill - local-first Personal Context Artifact setup, installer review, and private context hygiene for Claude Code and adjacent agent workflows.
* JunsW/feature-track: Source for thefeature-trackingskill - lightweight repository-native feature memory for current status, source-of-truth documents, decisions, risks, and cross-session handoff (MIT).
* JularDepick/user-thoughts.SKILL: Source for theuser-thoughtsskill - persistent project idea repository workflows for capturing decisions, tech stack notes, UI/UX rationale, and MDBASE-backed project memory (MIT).
* TheaDust/lore: Source for theloreskill - Markdown-only, zero-dependency long-term project memory for AI coding agents, with monorepo scopes, two-section platform mirrors, and stdlib Python helpers (MIT).
* rainmanjam/poka-yoke: Source for thepoka-yokeskill - software mistake-proofing through control, warning, detection, and source-inspection guardrails (MIT).
* ZeroPointRepo/youtube-skills: Source for theyoutube-fullskill - TranscriptAPI-backed YouTube transcripts, search, channel browsing, playlists, and cloud-safe video research workflows (MIT).
* ZeroPointRepo/zillow-skills: Source for theus-property-dataskill - U.S. property lookup, valuation, listing, tax, school, photo, and price-history guidance through the independent Zillapi API (MIT-0).
* Antheurus/anywrite: Source for theanywriteskill - low-context CLI access to Anytype's local API for objects, properties, files, search, chat, and other workspace operations (MIT).
* Antheurus/sshepherd: Source for thesshepherdskill - credential-isolated SSH operations, service control, logs, configuration changes, Postgres introspection, and declarative deploys through preconfigured aliases (MIT).
* ejentum/ejentum-mcp: Source for theejentum-reasoning-harnessskill - MCP cognitive harness modes for reasoning, code review, anti-deception checks, and memory-drift analysis (MIT).
* luoyuctl/agenttrace: Source for theagenttrace-session-auditskill - local AI coding-agent session audits for cost spikes, tool failures, latency gaps, anomalies, health gates, and session diffs (MIT).
* ohad6k/ditto: Source for thedittoskill - mines local coding-agent sessions into private, evidence-backed work, design, and writing profiles with dated source receipts (MIT).
* Necmttn/ax: Source for theax-extract-workflowskill - reconstruct workflow behind past coding-agent artifacts using local ax sessions, commits, skills, and tool traces (AGPL-3.0-only).
* Hanyuyuan6/remote-gpu-trainer: Source for theremote-gpu-trainerskill - rented and remote GPU job orchestration, monitoring, teardown safety, spot resilience, and DL-debug workflows (MIT).
* mturac/recsys-pipeline-architect: Source for therecsys-pipeline-architectskill - recommendation, ranking, and feed pipeline architecture using Source, Hydrator, Filter, Scorer, Selector, and SideEffect stages (MIT).
* aomi-labs/skills: Source for theaomi-transactskill — natural-language driver for the Aomi CLI with account-abstraction-first execution and simulate-then-sign across 25+ DeFi apps (MIT).
* mycelos-ai/bumblebee-skill: Source for thebumblebeeskill - multi-agent implementation workflows with repeatable planning, coding, review, and verification loops (MIT).
* demo112/yunqu-ai-skills: Source for WeChat official account, Xiaohongshu content strategy, and MCP tool development skills for Chinese-language platform workflows (MIT).
* tellmefrankie/news-engine: Source for thenews-sentiment-engineskill - news ingestion, sentiment analysis, and market/news intelligence workflows (MIT).
* Kench001/antigravity-awesome-skills: Source for therecursive-context-pruning-token-budgetingskill - context pruning, token budgeting, and long-session compression guidance (MIT).
* rich-elicitation: Source for therich-elicitationskill - asks clarifying questions in multiple rounds before starting ambiguous tasks.
* CodeShuX/mockhunter: Source for themock-hunterskill - Playwright-based live-page audits that classify visible values as real, mock, LLM-generated, hardcoded, broken, or unknown (MIT).
* commitshow/production-audit: Source for theproduction-auditskill - shipped-app readiness auditing across deployment health, RLS, webhooks, secrets exposure, grants, Stripe idempotency, and mobile UX.
* MohamedAbdallah-14/unslop: Source for theunslopskill - deterministic and LLM-assisted cleanup for AI-generated prose across CLI and agent tool workflows.
* monte-carlo-data/mc-agent-toolkit: Monte Carlo data observability skills — table health checks, change impact assessment, monitor creation, push ingestion, and SQL validation notebooks for dbt changes.
* openclaw/skills: Source for thedaily-giftskill - relationship-aware creative gift generation with editorial judgment, concept selection, and multi-format rendering.
* umutbozdag/agent-skills-manager: Source for themanage-skillsskill - cross-tool skill discovery, creation, editing, toggling, copying, moving, and deletion workflows across major agent coding tools.
* pumanitro/global-chat: Source for the Global Chat Agent Discovery skill - cross-protocol discovery of MCP servers and AI agents across multiple registries.
* bitjaru/styleseed: StyleSeed Toss UI and UX skill collection - setup wizard, page and pattern generation, design-token management, accessibility review, UX audits, feedback states, and microcopy guidance for professional mobile-first UI.
* yikuansun/PhotopeaAPI: Source for thephotopea-embedded-editorskill - Photopea embedding, host-page messaging, file I/O, scripting, and export workflows for web apps (MIT).
* milkomida77/guardian-agent-prompts: Source for the Multi-Agent Task Orchestrator skill - production-tested delegation patterns, anti-duplication, and quality gates for coordinated agent work.
* Elkidogz/technical-change-skill: Source for the Technical Change Tracker skill - structured JSON change records, session handoff, and accessible HTML dashboards for coding continuity.
* vipin-si/article-illustrations: Source for thearticle-illustrationsskill - Grav-style hand-drawn article illustrations with whiteboard sketches, sparse annotations, and visual metaphor QA guidance (MIT).
* 274326424/video-content-extractor: Source for thevideo-content-extractorskill - FFmpeg and Tesseract OCR workflows for extracting timestamped screen text and structured Markdown reports from MP4 videos (MIT).
* metrox-eth/quit-sponsor: Source for thequit-sponsorskill - evidence-based quit-smoking sponsorship for agents with persistent memory: 44-source cited protocols, sponsor decision tree, three-clause contract, wave protocol, slip attribution coaching, and a timestamped logbook (MIT).
* rmyndharis/antigravity-skills: For the massive contribution of 300+ Enterprise skills and the catalog generation logic.
* amartelr/antigravity-workspace-manager: Workspace Manager CLI companion to dynamically auto-provision subsets of skills across local development environments.
* obra/superpowers: The original "Superpowers" by Jesse Vincent.
* guanyang/antigravity-skills: Core Antigravity extensions.
* diet103/claude-code-infrastructure-showcase: Infrastructure and Backend/Frontend Guidelines.
* ChrisWiles/claude-code-showcase: React UI patterns and Design Systems.
* travisvn/awesome-claude-skills: Loki Mode and Playwright integration.
* Dimillian/Skills: Curated Codex skills focused on Apple platforms, GitHub workflows, refactoring, and performance (MIT).
* zebbern/claude-code-guide: Comprehensive Security suite & Guide (Source for ~60 new skills).
* morsechimwai/lemmaly: Source for thelemmaly,mathguard,invariant-guard, andcomplexity-cutsskills — algorithm-first discipline layer that forces AI coding agents to state Big-O, name the data structure, prove termination, and pick the right algorithm before writing the loop. Ships a deterministic CI scanner with 59 rules across 11 languages (Apache-2.0).
* alirezarezvani/claude-skills: Senior Engineering and PM toolkit.
* karanb192/awesome-claude-skills: A massive list of verified skills for Claude Code.
* VoltAgent/awesome-agent-skills: Curated collection of 1000+ official and community agent skills from leading development teams (MIT).
* zircote/.claude: Archived Claude Code dotfiles/config repo with a Shopify development skill reference.
* vibeforge1111/vibeship-spawner-skills: AI agents, integrations, maker tools, and other production-grade skill packs.
* coreyhaines31/marketingskills: Marketing skills for CRO, copywriting, SEO, paid ads, and growth (23 skills, MIT).
* iradoweck/antigravity-awesome-skills: Source for the GeminiIgnore FinOps skill -.geminiignoresetup patterns for context-window efficiency and token cost reduction.
* heyneuron/flowhunt-skill: Source for the FlowHunt automation discovery audit skill - workflow intake, tool-by-tool audit, and opportunity prioritization for productivity automation.
* Intelligent-Internet/II-Commons-Skills: Source for the II-Commons research skill - deterministic retrieval across arXiv, PubMed/PMC, and supported US policy corpora.
* AgriciDaniel/claude-seo: SEO workflow collection covering technical SEO, hreflang, sitemap, geo, schema, and programmatic SEO patterns.
* Leonxlnx/taste-skill: Frontend design taste skill collection covering premium UI generation, redesign audits, GSAP motion, Stitch design systems, minimalist and brutalist visual modes, and full-output enforcement.
* 2slides/slides-generation-2slides-skills: Source for the2slides-ppt-generatorskill - AI presentation generation, PDF deck creation, narration, theme search, and slide export workflows using the 2slides API (MIT).
* ch040602/mdpr-skill: Source for themdpr-skillskill - Codex-assisted MDPR presentation review, semantic hints, visual checks, theme candidates, and deterministic renderer boundaries (MIT).
* whoisabhishekadhikari/lovable-cleanup: Source for thelovable-cleanupskill — audits and strips Lovable scaffolding from Vite + React projects.
* sarveshtalele/linkedin-content-skill: Source for thelinkedin-content-generatorskill - LinkedIn post, carousel, newsletter, and content-calendar generation workflows with local feedback memory (MIT).
* mrprewsh/seo-aeo-engine: SEO/AEO content-growth system covering keyword research, content clustering, landing pages, blog structure, schema, internal linking, and audit workflows.
* jonathimer/devmarketing-skills: Developer marketing skills — HN strategy, technical tutorials, docs-as-marketing, Reddit engagement, developer onboarding, and more (33 skills, MIT).
* kepano/obsidian-skills: Obsidian-focused skills for markdown, Bases, JSON Canvas, CLI workflows, and content cleanup.
* lewiswigmore/agent-skills: Source for thevscode-extension-guide-enskill - VS Code extension development workflows, packaging, Marketplace publishing, TreeView, and webview patterns.
* mbenhard/unship: Source for theunshipskill - local workflow for comparing AI-generated UI variants in a real app, then keeping one option and cleaning up temporary alternatives (MIT).
* Silverov/yandex-direct-skill: Yandex Direct (API v5) advertising audit skill — 55 automated checks, A-F scoring, campaign/ad/keyword analysis for the Russian PPC market (MIT).
* vudovn/antigravity-kit: AI Agent templates with Skills, Agents, and Workflows (33 skills, MIT).
* affaan-m/everything-claude-code: Large Claude Code configuration and workflow collection from an Anthropic hackathon winner (MIT).
* whatiskadudoing/fp-ts-skills: Practical fp-ts skills for TypeScript – fp-ts-pragmatic, fp-ts-react, fp-ts-errors (v4.4.0).
* warmskull/idea-darwin: Darwinian idea-evolution workflow for structured ideation rounds, mutation, crossbreeding, critique, and lineage tracking.
* Slashworks-biz/idea-os: Source for theidea-osskill - five-phase pipeline (triage -> clarify -> research -> PRD -> plan) that turns raw ideas into a build-ready PRD and execution plan.
* webzler/agentMemory: Source for the agent-memory-mcp skill.
* rafsilva85/credit-optimizer-v5: Manus AI credit optimizer skill — intelligent model routing, context compression, and smart testing. Saves 30-75% on credits with zero quality loss. Audited across 53 scenarios.
* ndesv21/socialclaw: Source for the SocialClaw social media publishing skill - campaign scheduling and publishing across major social platforms with a single workspace API key.
* talivia-group/agent: Source for thetalivia-agent-kitskill - revenue-first website analytics through the official MCP server, with explicit confirmation for tracking and payment attribution changes (MIT).
* taisly/agent: Source for the Taisly Social Media Posting skill - Codex plugin, CLI, SDK, and official MCP server for publishing approved short-form videos to TikTok, Instagram Reels, YouTube Shorts, X, and Facebook (MIT).
* nickdesi/ZipAI: Source for thezipai-optimizerskill — ultra-dense prompt caching, semantic log pruning, AST-based code viewing, minified JSON payloads, and telegraphic output constraints for maximum token savings.
* Wittlesus/cursorrules-pro: Professional .cursorrules configurations for 8 frameworks - Next.js, React, Python, Go, Rust, and more. Works with Cursor, Claude Code, and Windsurf.
* nedcodes-ok/rule-porter: Bidirectional rule converter between Cursor (.mdc), Claude Code (CLAUDE.md), GitHub Copilot, Windsurf, and legacy .cursorrules formats. Zero dependencies.
* SSOJet/skills: Production-ready SSOJet skills and integration guides for popular frameworks and platforms — Node.js, Next.js, React, Java, .NET Core, Go, iOS, Android, and more. Works seamlessly with SSOJet SAML, OIDC, and enterprise SSO flows. Works with Cursor, Antigravity, Claude Code, and Windsurf.
* timwukp/agent-skills-best-practice: Source for thefsi-compliance-checkerskill - financial-services compliance triage for PCI-DSS v4.0 and MAS TRM control mapping (MIT).
* MojoAuth/skills: Production-ready MojoAuth guides and examples for popular frameworks like Node.js, Next.js, React, Java, .NET Core, Go, iOS, and Android.
* mishanefedov/skill-issue: Source for theskill-issueactivation-audit skill for grading SKILL.md trigger metadata, prompt matching, and collision clusters (MIT).
* wede-wx/atlas: Source for theatlas-contractandatlas-ledgergoal-integrity skills - contract, phase-check, final-audit, and project-ledger guardrails for long-running agent work (MIT).
* yehudalevy-collab/polis-protocol: Source for thepolis-protocolmulti-agent coordination skill with capability cards, routing history, and protocol amendments (MIT).
* connerlambden/helium-mcp: Source for thehelium-mcpskill — MCP server for news intelligence, media bias analysis, market data, options pricing, and semantic meme search.
* shmlkv/dna-claude-analysis: Personal genome analysis toolkit — Python scripts analyzing raw DNA data across 17 categories (health risks, ancestry, pharmacogenomics, nutrition, psychology, etc.) with terminal-style single-page HTML visualization.
* AlmogBaku/debug-skill: Interactive debugger skill for AI agents — breakpoints, stepping, variable inspection, and stack traces via thedapCLI. Supports Python, Go, Node.js/TypeScript, Rust, and C/C++.
* sendblue-api/sendblue-cli: Source for thesendblue-cli,sendblue-api, andsendblue-notifyskills — iMessage, SMS, and RCS messaging via Sendblue's CLI and HTTP API, plus "text me when X finishes" notification patterns for Claude Code hooks and/loop//schedulejobs (MIT).
* njerschow/textme: Source for thetextmeskill — local daemon bridging inbound iMessages (via Sendblue) to a Claude Code session on the user's machine, with voice notes, image input, code execution, and a phone-number whitelist (MIT).
* aptratcn/skill-audit: Pre-install security audit skill for detecting malicious, overprivileged, or suspicious third-party agent skills before installation (MIT).
* uberSKILLS: Design, test, and deploy Claude Code Agent Skills through a visual, AI-assisted workflow.
* christopherlhammer11-ai/tool-use-guardian: Source for the Tool Use Guardian skill — tool-call reliability wrapper with retries, recovery, and failure classification.
* christopherlhammer11-ai/recallmax: Source for the RecallMax skill — long-context memory, summarization, and conversation compression for agents.
* tsilverberg/webapp-uat: Full browser UAT skill — Playwright testing with console/network error capture, WCAG 2.2 AA accessibility checks, i18n validation, responsive testing, and P0-P3 bug triage. Read-only by default, works with React, Vue, Angular, Ionic, Next.js.
* Wolfe-Jam/faf-skills: AI-context and project DNA skills — .faf format management, AI-readiness scoring, bi-sync, MCP server building, and championship-grade testing (7 skills, MIT).
* fullstackcrew-alpha/privacy-mask: Local image privacy masking for AI coding agents. Detects and redacts PII, API keys, and secrets in screenshots via OCR + 47 regex rules. Claude Code hook integration for automatic masking. Supports Tesseract and RapidOCR. 100% offline (MIT).
* glukicov/slideops: Source for theslideopsskill - cited HTML slide decks generated from a repository, with a standard-library drift check that reports the day the slides stop matching the code (MIT).
* AvdLee/SwiftUI-Agent-Skill: SwiftUI best-practices skill for agent workflows (MIT).
* CloudAI-X/threejs-skills: Three.js-focused skill collection for agent-assisted 3D web work.
* K-Dense-AI/claude-scientific-skills: Scientific, research, engineering, finance, and writing skill suite (MIT).
* NotMyself/claude-win11-speckit-update-skill: Archived Speckit update skill for Claude Code (MIT).
* SHADOWPR0/beautiful_prose: Writing-quality skill for improving prose and reducing generic output.
* SHADOWPR0/security-bluebook-builder: Security documentation/buildbook skill for agent workflows.
* SeanZoR/claude-speed-reader: RSVP-style speed-reading helper for Claude responses (MIT).
* Shpigford/skills: General-purpose agent skills for common development tasks (MIT).
* ZhangHanDong/makepad-skills: Makepad app-development skills and references (MIT).
* czlonkowski/n8n-skills: n8n workflow-building skills for Claude Code (MIT).
* frmoretto/clarity-gate: Verification protocol for marking uncertainty and reducing hallucinated certainty in LLM-facing docs.
* fruitwyatt/puzzle-activity-planner: Puzzle activity-planning skill for classrooms, parties, and events with generator-link workflows.
* gokapso/agent-skills: Kapso/WhatsApp-oriented agent skills.
* huifer/WellAlly-health: Healthcare assistant project cited in release history as a source for health-focused agent capabilities (MIT).
* hyhmrright/brooks-lint: AI code-review skill grounded in classic software engineering books for design-smell, coupling, and architecture review.
* hyhmrright/logic-lens: AI code-review skill for formal logic inspection across bugs, race conditions, security risks, and API contract issues.
* ibelick/ui-skills: UI-polish skills for improving interfaces built by agents (MIT).
* jackjin1997/ClawForge: Resource hub of skills, MCP servers, and agent tooling for OpenClaw.
* jthack/ffuf_claude_skill: FFUF skill for web fuzzing workflows in Claude.
* kubestellar/console: KubeStellar Console multi-cluster Kubernetes dashboard withkc-agentMCP integration, AI-assisted operations, and built-in agent skills.
* MetcalfSolutions/Satori: Clinically informed wisdom companion blending psychology frameworks and wisdom traditions into a structured reflective partner.
* muratcankoylan/Agent-Skills-for-Context-Engineering: Context-engineering, multi-agent, and production agent-system skill collection (MIT).
* robzolkos/skill-rails-upgrade: Rails upgrade skill for agent-assisted migrations.
* sanjay3290/ai-skills: Apache-licensed collection of agent skills for AI coding assistants.
* scarletkc/vexor: Semantic search engine for files and code, referenced in release history.
* sstklen/infinite-gratitude: Multi-agent research skill from the AI Dojo series (MIT).
* TerminallyLazy/Tree-Ring-Memory: Source for thetree-ring-memoryskill — local-first memory lifecycle guidance for recall, evidence, audit, forgetting, consolidation, and privacy-safe agent memory operations (MIT).
* wrsmith108/linear-claude-skill: Linear issue/project/team management skill with MCP and GraphQL workflows (MIT).
* wrsmith108/varlock-claude-skill: Secure environment-variable management skill for Claude Code (MIT).
* xwmxcz/papers-skill: Source for thepapers-skillskill — academic research workflows over Semantic Scholar (200M+ papers) and arXiv, with citation lookup, arXiv PDF download, and PyMuPDF text extraction via a bundled Python CLI (MIT).
* zenlee123/routerbase-agent-skills: Source for therouterbase-model-gatewayskill — OpenAI-compatible RouterBase model gateway setup, model-routing plans, server-side credential handling, and fallback validation patterns (MIT-0).
* zarazhangrui/frontend-slides: Frontend slide-creation skills for web-based presentations (MIT).
* zxkane/aws-skills: AWS-focused Claude agent skills (MIT).
* UrRhb/agentflow: Kanban-driven AI development pipeline for orchestrating multi-worker Claude Code workflows with deterministic quality gates, adversarial review, cost tracking, and crash-proof execution (MIT).
* AgentPhone-AI/skills: AgentPhone plugin for Claude Code — API-first telephony workflows for AI agents, including phone calls, SMS, phone-number management, voice-agent setup, streaming webhooks, and tool-calling patterns.
* uxuiprinciples/agent-skills: Research-backed UX/UI agent skills for auditing interfaces against 168 principles, detecting antipatterns, and injecting UX context into AI coding sessions.
* voidborne-d/humanize-chinese: Chinese AI-text detection and humanization toolkit for scoring, rewriting, academic AIGC reduction, and style conversion workflows.
* voidborne-d/lambda-lang: Agent-to-agent coordination language with compact atoms for multi-agent messaging, orchestration, and structured coordination logs.
* davidondrej/skills: Source for David Ondrej agent workflow skills across orchestration, research, setup, skill authoring, and documentation workflows (MIT).
* LambdaTest/agent-skills: Production-grade agent skills for test automation — 46 skills covering E2E, unit, mobile, BDD, visual, and cloud testing across 15+ languages (MIT).
* flyingsquirrel0419/squirrel-skill: Full-cycle software development skill — plans, builds, tests, lints, fixes bugs, and writes production-grade docs. Auto-detects project state and adapts its 8-phase pipeline. Works on 9 AI coding agent platforms (Apache 2.0).
* CodeShuX/tokenwise: Source for thetokenwiseskill — measurement-driven Haiku/Sonnet/Opus router for Claude Code with per-task NDJSON logging, A/B test mode, and verified $-saved reports (MIT).
* anthony-chaudhary/dos-kernel: Source for thedos-verify-done-claimsskill — gates an agent's "done / shipped / fixed" claim on git ground truth (ancestry + the commit's own diff) via the deterministic DOS kernel's read-onlydos verify/dos commit-auditverbs (MIT).
* maxbaluev/accreted-intelligence: Source for theaccint-solveskill — routes coding-agent work through AccInt's MCP memory loop with retrieval, continuation frames, commitments, and outcome feedback (Apache 2.0).
* sergebulaev/linkedin-skills: Source for thelinkedin-post-writerskill - LinkedIn post drafting from 16 tested hook formulas mapped to engagement goals, with 2026 formatting rules and an AI-tell scrub pass, from a 10-skill LinkedIn bundle for Claude Code and Codex (MIT).
* Sharrmavishal/operating-kit: Source for thepre-ship-gateskill - a pre-deploy gate that walks the silent failure modes (migrations, feature flags, stale build cache, release pointer, staged rollout, missing env) and verifies the live revision instead of trusting deploy output (MIT).
* Ducksss/codex-profiles: Source for thecodex-profilesskill - Codex CLI/Desktop profile isolation around separateCODEX_HOMEdirectories, diagnostics, and account-context boundaries without copying auth tokens (MIT).
* kimtth/agent-pptify-kit: Source for thepptx-deck-creationskill - editable, production-ready PowerPoint deck creation with narrative planning, explicit layouts, asset guidance, and quality checks (MIT).
* Optim-Agent/optim-agent: Source for theoptim-agentskill - agent-guided optimization of configurable systems against measurable objectives (MIT).
* thecsdoctor/brendangregg-use-tsa-skill: Source for thebrendangregg-use-tsaskill - methodical performance troubleshooting and root-cause analysis with Brendan Gregg's USE and TSA methods, plus evidence-backed RCA and postmortem reporting (MIT).
* AntonioCardenas/generate-nanobanana: Source for thegenerate-nanobananaskill - image and video generation via Google's Gemini media models (Nano Banana 2 Lite/Standard/Pro, Gemini Omni Flash) with cost-approval gates before paid runs, real reference-image support, and a prompt/seed log beside every output (MIT).
* alfredtech2026/shopify-app-review-brief: Source for theshopify-review-triageskill - public-data-only P0–P3 triage of low-star Shopify App Store reviews into a source-linked brief, with an explicit needs-human-read bucket and first-pass vs. human-checked labeling (MIT).
* unslothai/unsloth: Source for theunsloth-finetuningskill - single-GPU VRAM sizing, LoRA/QLoRA configuration, chat-template and loss-masking correctness, GRPO/DPO post-training, and GGUF/merged export paths (Apache-2.0).
* jiawood2006/hermes-skills: MIT source for thede-ai-writerskill - Chinese AI-smell detection and de-AI rewriting from a 35-pattern catalog, with a deterministic AI-smell index and a deletion-first edit procedure that preserves every source fact.
* axelfreeman/marketing-mindset: Source for themarketing-mindsetskill - a marketer's decision framework for early-stage B2B and SaaS work: exchange checks, live-competitor benchmarking, pre-declared test volume floors, and channel kill rules (MIT).
* mnemoverse/agent-memory-discipline: Source for theagent-memory-disciplineskill, with backend-neutral rules for when an agent recalls from long-term memory before acting and when it saves decisions, corrections and failures afterwards (CC0-1.0).
* Search-3D/electron-drive-skill: Source for theelectron-drive-skillskill - launching and driving Electron apps under Playwright on a scratch profile (MIT).
* codegiveness/kernel-prompt: MIT source for thekernel-promptskill - harness-neutral prompt design that asks one round of user-only decisions, then returns an improved prompt for another agent without performing the task.

Inspirations & Additional Sources

### Inspirations

* f/awesome-chatgpt-prompts: Inspiration for the Prompt Library.
* leonardomso/33-js-concepts: Inspiration for JavaScript Mastery.

### Additional Sources

* agent-cards/skill: Manage prepaid virtual Visa cards for AI agents. Create cards, check balances, view credentials, close cards, and get support via MCP tools.

Catalog dashboard search, filters, shortlist, and discovery were originally contributed by@zinziedin#1111, then repaired and integrated through#1118under the repository's fork-safety policy.

## Top Contributors

Thanks to everyone who has helped build this project—especially the contributors below.

### Most Commits

Contributors ranked by the number of commits.

#

Contributor

Commits

1

 
@WHOISABHISHEKADHIKARI

36

2

 
@munir-abbasi

34

3

 
@Mohammad-Faiz-Cloud-Engineer

33

4

 
@zinzied

24

5

 
@beatra-ai

17

6

 
@Prince-1652

17

7

 
@ssumanbiswas

15

8

 
@FrancoStino

13

9

 
@Champbreed

10

10

 
@Dokhacgiakhoa

10

### Most Skills Added

Contributors ranked by the number of skills they added.

#

Contributor

Skills added

1

 
@FrancoStino

336

2

 
@WHOISABHISHEKADHIKARI

125

3

 
@Prince-1652

91

4

 
@sohamganatra

78

5

 
@ProgramadorBrasil

52

6

 
@nikolasdehor

35

7

 
@Ranjeet2063

20

8

 
@MMEHDI0606

20

9

 
@beatra-ai

17

10

 
@ShianMike

13

## Repo Contributors

Made withcontrib.rocks.(Image may be cached;view live contributorson GitHub.)

We officially thank the following contributors for their help in making this repository awesome!

## Star History

View the live Star History chart.

If Agentic Awesome Skills has been useful, consider ⭐ starring the repo!

## License

Original code and tooling are licensed under the MIT License. SeeLICENSE.

Original documentation and other non-code written content are licensed underCC BY 4.0, unless a more specific upstream notice says otherwise. Seedocs/sources/sources.mdfor attributions and third-party license details.

### Consolidated plugin packs

The focused offer unifies overlapping historical bundles with the AAS packs. Use theplugin migration guideto find replacements. Existing installations require a manual switch after verifying the destination; activation aliases do not create duplicate marketplace plugins. Changes on main become available through the next published release.