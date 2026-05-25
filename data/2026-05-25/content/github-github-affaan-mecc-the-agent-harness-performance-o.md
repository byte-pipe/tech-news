---
title: 'GitHub - affaan-m/ECC: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. · GitHub'
url: https://github.com/affaan-m/ECC
site_name: github
content_file: github-github-affaan-mecc-the-agent-harness-performance-o
fetched_at: '2026-05-25T12:11:54.622780'
original_url: https://github.com/affaan-m/ECC
author: affaan-m
description: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. - affaan-m/ECC
---

affaan-m

 

/

ECC

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork29.7k
* Star192k

 
 
 
 
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

1,976 Commits
1,976 Commits
.agents
.agents
 
 
.claude-plugin
.claude-plugin
 
 
.claude
.claude
 
 
.codebuddy
.codebuddy
 
 
.codex-plugin
.codex-plugin
 
 
.codex
.codex
 
 
.cursor
.cursor
 
 
.gemini
.gemini
 
 
.github
.github
 
 
.kiro
.kiro
 
 
.opencode
.opencode
 
 
.qwen
.qwen
 
 
.trae
.trae
 
 
.vscode
.vscode
 
 
.zed
.zed
 
 
agents
agents
 
 
assets
assets
 
 
commands
commands
 
 
config
config
 
 
contexts
contexts
 
 
docs
docs
 
 
ecc2
ecc2
 
 
examples
examples
 
 
hooks
hooks
 
 
legacy-command-shims
legacy-command-shims
 
 
manifests
manifests
 
 
mcp-configs
mcp-configs
 
 
plugins
plugins
 
 
research
research
 
 
rules
rules
 
 
schemas
schemas
 
 
scripts
scripts
 
 
skills
skills
 
 
src/
llm
src/
llm
 
 
tests
tests
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.markdownlint.json
.markdownlint.json
 
 
.mcp.json
.mcp.json
 
 
.npmignore
.npmignore
 
 
.prettierrc
.prettierrc
 
 
.tool-versions
.tool-versions
 
 
.yarnrc.yml
.yarnrc.yml
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
COMMANDS-QUICK-REF.md
COMMANDS-QUICK-REF.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
EVALUATION.md
EVALUATION.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
REPO-ASSESSMENT.md
REPO-ASSESSMENT.md
 
 
RULES.md
RULES.md
 
 
SECURITY.md
SECURITY.md
 
 
SOUL.md
SOUL.md
 
 
SPONSORING.md
SPONSORING.md
 
 
SPONSORS.md
SPONSORS.md
 
 
TROUBLESHOOTING.md
TROUBLESHOOTING.md
 
 
VERSION
VERSION
 
 
WORKING-CONTEXT.md
WORKING-CONTEXT.md
 
 
agent.yaml
agent.yaml
 
 
commitlint.config.js
commitlint.config.js
 
 
ecc_dashboard.py
ecc_dashboard.py
 
 
eslint.config.js
eslint.config.js
 
 
install.ps1
install.ps1
 
 
install.sh
install.sh
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
pyproject.toml
pyproject.toml
 
 
the-longform-guide.md
the-longform-guide.md
 
 
the-security-guide.md
the-security-guide.md
 
 
the-shortform-guide.md
the-shortform-guide.md
 
 
yarn.lock
yarn.lock
 
 
View all files

## Repository files navigation

Language:English |Português (Brasil)|简体中文|繁體中文|日本語|한국어|Türkçe|Русский|Tiếng Việt|ไทย

# ECC

182K+ stars|28K+ forks|170+ contributors|12+ language ecosystems|Anthropic Hackathon Winner

Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ

English|Português (Brasil)|简体中文|繁體中文|日本語|한국어|Türkçe|Русский|Tiếng Việt|ไทย

The harness-native operator system for agentic work. From an Anthropic hackathon winner.

Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development. Production-ready agents, skills, hooks, rules, MCP configurations, and legacy command shims evolved over 10+ months of intensive daily use building real products.

Works acrossClaude Code,Codex,Cursor,OpenCode,Gemini,Zed,GitHub Copilot, and other AI agent harnesses.

ECC v2.0.0-rc.1 adds the public Hermes operator story on top of that reusable layer: start with theHermes setup guide, then review therc.1 release notesandcross-harness architecture.

 ECC Pro

Private repos · GitHub App · $19/seat/mo

 Sponsor

Fund the OSS · From $5/mo

Community

Discussions · Q&A · Show & Tell

 GitHub App

Install · PR audits · Free tier

OSS stays free.This repo is MIT-licensed forever. ECC Pro is the hosted GitHub App for private repos.SponsorsandPro subscribersfund the work — that's why a single maintainer ships weekly across 7 harnesses.

## The Guides

This repo is the raw code only. The guides explain everything.

Shorthand Guide
Setup, foundations, philosophy. 
Read this first.

Longform Guide
Token optimization, memory persistence, evals, parallelization.

Security Guide
Attack vectors, sandboxing, sanitization, CVEs, AgentShield.

Topic

What You'll Learn

Token Optimization

Model selection, system prompt slimming, background processes

Memory Persistence

Hooks that save/load context across sessions automatically

Continuous Learning

Auto-extract patterns from sessions into reusable skills

Verification Loops

Checkpoint vs continuous evals, grader types, pass@k metrics

Parallelization

Git worktrees, cascade method, when to scale instances

Subagent Orchestration

The context problem, iterative retrieval pattern

## What's New

### v2.0.0-rc.1 — Surface Refresh, Operator Workflows, and ECC 2.0 Alpha (Apr 2026)

* Dashboard GUI— New Tkinter-based desktop application (ecc_dashboard.pyornpm run dashboard) with dark/light theme toggle, font customization, and project logo in header and taskbar.
* Public surface synced to the live repo— metadata, catalog counts, plugin manifests, and install-facing docs now match the actual OSS surface: 60 agents, 232 skills, and 75 legacy command shims.
* Operator and outbound workflow expansion—brand-voice,social-graph-ranker,connections-optimizer,customer-billing-ops,ecc-tools-cost-audit,google-workspace-ops,project-flow-ops, andworkspace-surface-auditround out the operator lane.
* Media and launch tooling—manim-video,remotion-video-creation, and upgraded social publishing surfaces make technical explainers and launch content part of the same system.
* Framework and product surface growth—nestjs-patterns, richer Codex/OpenCode install surfaces, and expanded cross-harness packaging keep the repo usable beyond Claude Code alone.
* ECC 2.0 alpha is in-tree— the Rust control-plane prototype inecc2/now builds locally and exposesdashboard,start,sessions,status,stop,resume, anddaemoncommands. It is usable as an alpha, not yet a general release.
* Operator status snapshots—ecc status --markdown --write status.mdturns the local state store into a portable handoff covering readiness, active sessions, skill-run health, install health, pending governance events, and linked work items from Linear/GitHub/handoffs. Useecc work-items upsert ...for manual entries,ecc work-items sync-github --repo owner/repofor PR/issue queue state, andecc status --exit-codeto fail automation when readiness needs attention.
* Ecosystem hardening— AgentShield, ECC Tools cost controls, billing portal work, and website refreshes continue to ship around the core plugin instead of drifting into separate silos.

### v1.9.0 — Selective Install & Language Expansion (Mar 2026)

* Selective install architecture— Manifest-driven install pipeline withinstall-plan.jsandinstall-apply.jsfor targeted component installation. State store tracks what's installed and enables incremental updates.
* 6 new agents—typescript-reviewer,pytorch-build-resolver,java-build-resolver,java-reviewer,kotlin-reviewer,kotlin-build-resolverexpand language coverage to 10 languages.
* New skills—pytorch-patternsfor deep learning workflows,documentation-lookupfor API reference research,bun-runtimeandnextjs-turbopackfor modern JS toolchains, plus 8 operational domain skills andmcp-server-patterns.
* Session & state infrastructure— SQLite state store with query CLI, session adapters for structured recording, skill evolution foundation for self-improving skills.
* Orchestration overhaul— Harness audit scoring made deterministic, orchestration status and launcher compatibility hardened, observer loop prevention with 5-layer guard.
* Observer reliability— Memory explosion fix with throttling and tail sampling, sandbox access fix, lazy-start logic, and re-entrancy guard.
* 12 language ecosystems— New rules for Java, PHP, Perl, Kotlin/Android/KMP, C++, and Rust join existing TypeScript, Python, Go, and common rules.
* Community contributions— Korean and Chinese translations, biome hook optimization, video processing skills, operational skills, PowerShell installer, Antigravity IDE support.
* CI hardening— 19 test failure fixes, catalog count enforcement, install manifest validation, and full test suite green.

### v1.8.0 — Harness Performance System (Mar 2026)

* Harness-first release— ECC is now explicitly framed as an agent harness performance system, not just a config pack.
* Hook reliability overhaul— SessionStart root fallback, Stop-phase session summaries, and script-based hooks replacing fragile inline one-liners.
* Hook runtime controls—ECC_HOOK_PROFILE=minimal|standard|strictandECC_DISABLED_HOOKS=...for runtime gating without editing hook files.
* New harness commands—/harness-audit,/loop-start,/loop-status,/quality-gate,/model-route.
* NanoClaw v2— model routing, skill hot-load, session branch/search/export/compact/metrics.
* Cross-harness parity— behavior tightened across Claude Code, Cursor, OpenCode, and Codex app/CLI.
* 997 internal tests passing— full suite green after hook/runtime refactor and compatibility updates.

### v1.7.0 — Cross-Platform Expansion & Presentation Builder (Feb 2026)

* Codex app + CLI support— DirectAGENTS.md-based Codex support, installer targeting, and Codex docs
* frontend-slidesskill— Zero-dependency HTML presentation builder with PPTX conversion guidance and strict viewport-fit rules
* 5 new generic business/content skills—article-writing,content-engine,market-research,investor-materials,investor-outreach
* Broader tool coverage— Cursor, Codex, and OpenCode support tightened so the same repo ships cleanly across all major harnesses
* 992 internal tests— Expanded validation and regression coverage across plugin, hooks, skills, and packaging

### v1.6.0 — Codex CLI, AgentShield & Marketplace (Feb 2026)

* Codex CLI support— New/codex-setupcommand generatescodex.mdfor OpenAI Codex CLI compatibility
* 7 new skills—search-first,swift-actor-persistence,swift-protocol-di-testing,regex-vs-llm-structured-text,content-hash-cache-pattern,cost-aware-llm-pipeline,skill-stocktake
* AgentShield integration—/security-scanskill runs AgentShield directly from Claude Code; 1282 tests, 102 rules
* GitHub Marketplace— ECC Tools GitHub App live atgithub.com/marketplace/ecc-toolswith free/pro/enterprise tiers
* 30+ community PRs merged— Contributions from 30 contributors across 6 languages
* 978 internal tests— Expanded validation suite across agents, skills, commands, hooks, and rules

### v1.4.1 — Bug Fix (Feb 2026)

* Fixed instinct import content loss—parse_instinct_file()was silently dropping all content after frontmatter (Action, Evidence, Examples sections) during/instinct-import. (#148,#161)

### v1.4.0 — Multi-Language Rules, Installation Wizard & PM2 (Feb 2026)

* Interactive installation wizard— Newconfigure-eccskill provides guided setup with merge/overwrite detection
* PM2 & multi-agent orchestration— 6 new commands (/pm2,/multi-plan,/multi-execute,/multi-backend,/multi-frontend,/multi-workflow) for managing complex multi-service workflows
* Multi-language rules architecture— Rules restructured from flat files intocommon/+typescript/+python/+golang/directories. Install only the languages you need
* Chinese (zh-CN) translations— Complete translation of all agents, commands, skills, and rules (80+ files)
* GitHub Sponsors support— Sponsor the project via GitHub Sponsors
* Enhanced CONTRIBUTING.md— Detailed PR templates for each contribution type

### v1.3.0 — OpenCode Plugin Support (Feb 2026)

* Full OpenCode integration— 12 agents, 24 commands, 16 skills with hook support via OpenCode's plugin system (20+ event types)
* 3 native custom tools— run-tests, check-coverage, security-audit
* LLM documentation—llms.txtfor comprehensive OpenCode docs

### v1.2.0 — Unified Commands & Skills (Feb 2026)

* Python/Django support— Django patterns, security, TDD, and verification skills
* Java Spring Boot skills— Patterns, security, TDD, and verification for Spring Boot
* Session management—/sessionscommand for session history
* Continuous learning v2— Instinct-based learning with confidence scoring, import/export, evolution

See the full changelog inReleases.

## Quick Start

Get up and running in under 2 minutes:

### Pick one path only

Most Claude Code users should use exactly one install path:

* Recommended default:install the Claude Code plugin, then copy only the rule folders you actually want.
* Use the manual installer only ifyou want finer-grained control, want to avoid the plugin path entirely, or your Claude Code build has trouble resolving the self-hosted marketplace entry.
* Do not stack install methods.The most common broken setup is:/plugin installfirst, theninstall.sh --profile fullornpx ecc-install --profile fullafterward.

If you already layered multiple installs and things look duplicated, skip straight toReset / Uninstall ECC.

### Low-context / no-hooks path

If hooks feel too global or you only want ECC's rules, agents, commands, and core workflow skills, skip the plugin and use the minimal manual profile:

./install.sh --profile minimal --target claude

.\install.ps1 
--
profile minimal 
--
target claude

#
 or

npx ecc
-
install 
--
profile minimal 
--
target claude

This profile intentionally excludeshooks-runtime.

If you want the normal core profile but need hooks off, use:

./install.sh --profile core --without baseline:hooks --target claude

Add hooks later only if you want runtime enforcement:

./install.sh --target claude --modules hooks-runtime

### Find the right components first

If you are not sure which ECC profile or component to install, ask the packaged advisor from any project:

npx ecc consult 
"
security reviews
"
 --target claude

It returns matching components, related profiles, and preview/install commands. Use the preview command before installing if you want to inspect the exact file plan.

For production ML/MLOps workflows, keep the install opt-in and component-scoped:

npx ecc consult 
"
mlops training model deployment
"
 --target claude
npx ecc install --profile minimal --target claude --with capability:machine-learning

### Step 1: Install the Plugin (Recommended)

NOTE: The plugin is convenient, but the OSS installer below is still the most reliable path if your Claude Code build has trouble resolving self-hosted marketplace entries.

#
 Add marketplace

/plugin marketplace add https://github.com/affaan-m/ECC

#
 Install plugin

/plugin install ecc@ecc

### Naming + Migration Note

ECC now has three public identifiers, and they are not interchangeable:

* GitHub source repo:affaan-m/ECC
* Claude marketplace/plugin identifier:ecc@ecc
* npm package:ecc-universal

This is intentional. Anthropic marketplace/plugin installs are keyed by a canonical plugin identifier, so ECC usesecc@eccto keep tool names and slash-command namespaces short enough for strict Desktop/API validators. Older posts may still show the former long marketplace identifier; treat that as a legacy alias only. Separately, the npm package stayed onecc-universal, so npm installs and marketplace installs intentionally use different names.

### Step 2: Install Rules Only If You Need Them

WARNING:Important:Claude Code plugins cannot distributerulesautomatically.

If you already installed ECC via/plugin install,do not run./install.sh --profile full,.\install.ps1 --profile full, ornpx ecc-install --profile fullafterward. The plugin already loads ECC skills, commands, and hooks. Running the full installer after a plugin install copies those same surfaces into your user directories and can create duplicate skills plus duplicate runtime behavior.

For plugin installs, manually copy only therules/directories you want under~/.claude/rules/ecc/. Start withrules/commonplus one language or framework pack you actually use. Do not copy every rules directory unless you explicitly want all of that context in Claude.

Use the full installer only when you are doing a fully manual ECC install instead of the plugin path.

If your local Claude setup was wiped or reset, that does not mean you need to repurchase ECC. Start withnode scripts/ecc.js list-installed, then runnode scripts/ecc.js doctorandnode scripts/ecc.js repairbefore reinstalling anything. That usually restores ECC-managed files without rebuilding your setup. If the problem is account or marketplace access for ECC Tools, handle billing/account recovery separately.

#
 Clone the repo first

git clone https://github.com/affaan-m/ECC.git

cd
 ECC

#
 Install dependencies (pick your package manager)

npm install 
#
 or: pnpm install | yarn install | bun install

#
 Plugin install path: copy only ECC rules into an ECC-owned namespace

mkdir -p 
~
/.claude/rules/ecc
cp -R rules/common 
~
/.claude/rules/ecc/
cp -R rules/typescript 
~
/.claude/rules/ecc/

#
 Fully manual ECC install path (use this instead of /plugin install)

#
 ./install.sh --profile full

#
 Windows PowerShell

#
 Plugin install path: copy only ECC rules into an ECC-owned namespace

New-Item
 
-
ItemType Directory 
-
Force 
-
Path 
"
$HOME
/.claude/rules/ecc
"
 
|
 
Out-Null

Copy-Item
 
-
Recurse rules
/
common 
"
$HOME
/.claude/rules/ecc/
"

Copy-Item
 
-
Recurse rules
/
typescript 
"
$HOME
/.claude/rules/ecc/
"

#
 Fully manual ECC install path (use this instead of /plugin install)

#
 .\install.ps1 --profile full

#
 npx ecc-install --profile full

For manual install instructions see the README in therules/folder. When copying rules manually, copy the whole language directory (for examplerules/commonorrules/golang), not the files inside it, so relative references keep working and filenames do not collide.

### Fully manual install (Fallback)

Use this only if you are intentionally skipping the plugin path:

./install.sh --profile full

.\install.ps1 
--
profile full

#
 or

npx ecc
-
install 
--
profile full

If you choose this path, stop there. Do not also run/plugin install.

### Reset / Uninstall ECC

If ECC feels duplicated, intrusive, or broken, do not keep reinstalling it on top of itself.

* Plugin path:remove the plugin from Claude Code, then delete the specific rule folders you manually copied under~/.claude/rules/ecc/.
* Manual installer / CLI path:from the repo root, preview removal first:

node scripts/uninstall.js --dry-run

Then remove ECC-managed files:

node scripts/uninstall.js

You can also use the lifecycle wrapper:

node scripts/ecc.js list-installed
node scripts/ecc.js doctor
node scripts/ecc.js repair
node scripts/ecc.js uninstall --dry-run

ECC only removes files recorded in its install-state. It will not delete unrelated files it did not install.

If you stacked methods, clean up in this order:

1. Remove the Claude Code plugin install.
2. Run the ECC uninstall command from the repo root to remove install-state-managed files.
3. Delete any extra rule folders you copied manually and no longer want.
4. Reinstall once, using a single path.

### Step 3: Start Using

#
 Skills are the primary workflow surface.

#
 Existing slash-style command names still work while ECC migrates off commands/.

#
 Plugin install uses the canonical namespaced form

/ecc:plan 
"
Add user authentication
"

#
 Manual install keeps the shorter slash form:

#
 /plan "Add user authentication"

#
 Check available commands

/plugin list ecc@ecc

That's it!You now have access to 60 agents, 232 skills, and 75 legacy command shims.

### Dashboard GUI

Launch the desktop dashboard to visually explore ECC components:

npm run dashboard

#
 or

python3 ./ecc_dashboard.py

Features:

* Tabbed interface: Agents, Skills, Commands, Rules, Settings
* Dark/Light theme toggle
* Font customization (family & size)
* Project logo in header and taskbar
* Search and filter across all components

### Multi-model commands require additional setup

WARNING:multi-*commands arenotcovered by the base plugin/rules install above.

To use/multi-plan,/multi-execute,/multi-backend,/multi-frontend, and/multi-workflow, you must also install theccg-workflowruntime.

Initialize it withnpx ccg-workflow.

That runtime provides the external dependencies these commands expect, including:

* ~/.claude/bin/codeagent-wrapper
* ~/.claude/.ccg/prompts/*

Withoutccg-workflow, thesemulti-*commands will not run correctly.

## Cross-Platform Support

This plugin now fully supportsWindows, macOS, and Linux, alongside tight integration across major IDEs (Cursor, Zed, OpenCode, Antigravity) and CLI harnesses. All hooks and scripts have been rewritten in Node.js for maximum compatibility.

### Package Manager Detection

The plugin automatically detects your preferred package manager (npm, pnpm, yarn, or bun) with the following priority:

1. Environment variable:CLAUDE_PACKAGE_MANAGER
2. Project config:.claude/package-manager.json
3. package.json:packageManagerfield
4. Lock file: Detection from package-lock.json, yarn.lock, pnpm-lock.yaml, or bun.lockb
5. Global config:~/.claude/package-manager.json
6. Fallback: First available package manager

To set your preferred package manager:

#
 Via environment variable

export
 CLAUDE_PACKAGE_MANAGER=pnpm

#
 Via global config

node scripts/setup-package-manager.js --global pnpm

#
 Via project config

node scripts/setup-package-manager.js --project bun

#
 Detect current setting

node scripts/setup-package-manager.js --detect

Or use the/setup-pmcommand in Claude Code.

### Hook Runtime Controls

Use runtime flags to tune strictness or disable specific hooks temporarily:

#
 Hook strictness profile (default: standard)

export
 ECC_HOOK_PROFILE=standard

#
 Comma-separated hook IDs to disable

export
 ECC_DISABLED_HOOKS=
"
pre:bash:tmux-reminder,post:edit:typecheck
"

#
 Cap SessionStart additional context (default: 8000 chars)

export
 ECC_SESSION_START_MAX_CHARS=4000

#
 Disable SessionStart additional context entirely for low-context/local-model setups

export
 ECC_SESSION_START_CONTEXT=off

#
 Keep context/scope/loop warnings but suppress API-rate cost estimates

export
 ECC_CONTEXT_MONITOR_COST_WARNINGS=off

Windows PowerShell:

[
Environment
]::SetEnvironmentVariable(
'
ECC_CONTEXT_MONITOR_COST_WARNINGS
'
,
 
'
off
'
,
 
'
User
'
)

## What's Inside

This repo is aClaude Code plugin- install it directly or copy components manually.

ECC/
|-- .claude-plugin/ # Plugin and marketplace manifests
| |-- plugin.json # Plugin metadata and component paths
| |-- marketplace.json # Marketplace catalog for /plugin marketplace add
|
|-- agents/ # 60 specialized subagents for delegation
| |-- planner.md # Feature implementation planning
| |-- architect.md # System design decisions
| |-- tdd-guide.md # Test-driven development
| |-- code-reviewer.md # Quality and security review
| |-- security-reviewer.md # Vulnerability analysis
| |-- build-error-resolver.md
| |-- e2e-runner.md # Playwright E2E testing
| |-- refactor-cleaner.md # Dead code cleanup
| |-- doc-updater.md # Documentation sync
| |-- docs-lookup.md # Documentation/API lookup
| |-- chief-of-staff.md # Communication triage and drafts
| |-- loop-operator.md # Autonomous loop execution
| |-- harness-optimizer.md # Harness config tuning
| |-- cpp-reviewer.md # C++ code review
| |-- cpp-build-resolver.md # C++ build error resolution
| |-- fsharp-reviewer.md # F# functional code review
| |-- go-reviewer.md # Go code review
| |-- go-build-resolver.md # Go build error resolution
| |-- python-reviewer.md # Python code review
| |-- database-reviewer.md # Database/Supabase review
| |-- typescript-reviewer.md # TypeScript/JavaScript code review
| |-- java-reviewer.md # Java/Spring Boot code review
| |-- java-build-resolver.md # Java/Maven/Gradle build errors
| |-- kotlin-reviewer.md # Kotlin/Android/KMP code review
| |-- kotlin-build-resolver.md # Kotlin/Gradle build errors
| |-- harmonyos-app-resolver.md # HarmonyOS/ArkTS app development
| |-- rust-reviewer.md # Rust code review
| |-- rust-build-resolver.md # Rust build error resolution
| |-- pytorch-build-resolver.md # PyTorch/CUDA training errors
| |-- mle-reviewer.md # Production ML pipeline, eval, serving, and monitoring review
|
|-- skills/ # Workflow definitions and domain knowledge
| |-- coding-standards/ # Language best practices
| |-- clickhouse-io/ # ClickHouse analytics, queries, data engineering
| |-- backend-patterns/ # API, database, caching patterns
| |-- frontend-patterns/ # React, Next.js patterns
| |-- frontend-slides/ # HTML slide decks and PPTX-to-web presentation workflows (NEW)
| |-- article-writing/ # Long-form writing in a supplied voice without generic AI tone (NEW)
| |-- content-engine/ # Multi-platform social content and repurposing workflows (NEW)
| |-- market-research/ # Source-attributed market, competitor, and investor research (NEW)
| |-- investor-materials/ # Pitch decks, one-pagers, memos, and financial models (NEW)
| |-- investor-outreach/ # Personalized fundraising outreach and follow-up (NEW)
| |-- continuous-learning/ # Legacy v1 Stop-hook pattern extraction
| |-- continuous-learning-v2/ # Instinct-based learning with confidence scoring
| |-- iterative-retrieval/ # Progressive context refinement for subagents
| |-- strategic-compact/ # Manual compaction suggestions (Longform Guide)
| |-- tdd-workflow/ # TDD methodology
| |-- security-review/ # Security checklist
| |-- eval-harness/ # Verification loop evaluation (Longform Guide)
| |-- verification-loop/ # Continuous verification (Longform Guide)
| |-- videodb/ # Video and audio: ingest, search, edit, generate, stream (NEW)
| |-- golang-patterns/ # Go idioms and best practices
| |-- golang-testing/ # Go testing patterns, TDD, benchmarks
| |-- cpp-coding-standards/ # C++ coding standards from C++ Core Guidelines (NEW)
| |-- cpp-testing/ # C++ testing with GoogleTest, CMake/CTest (NEW)
| |-- django-patterns/ # Django patterns, models, views (NEW)
| |-- django-security/ # Django security best practices (NEW)
| |-- django-tdd/ # Django TDD workflow (NEW)
| |-- django-verification/ # Django verification loops (NEW)
| |-- laravel-patterns/ # Laravel architecture patterns (NEW)
| |-- laravel-security/ # Laravel security best practices (NEW)
| |-- laravel-tdd/ # Laravel TDD workflow (NEW)
| |-- laravel-verification/ # Laravel verification loops (NEW)
| |-- python-patterns/ # Python idioms and best practices (NEW)
| |-- python-testing/ # Python testing with pytest (NEW)
| |-- quarkus-patterns/ # Java Quarkus patterns (NEW)
| |-- quarkus-security/ # Quarkus security (NEW)
| |-- quarkus-tdd/ # Quarkus TDD (NEW)
| |-- quarkus-verification/ # Quarkus verification (NEW)
| |-- springboot-patterns/ # Java Spring Boot patterns (NEW)
| |-- springboot-security/ # Spring Boot security (NEW)
| |-- springboot-tdd/ # Spring Boot TDD (NEW)
| |-- springboot-verification/ # Spring Boot verification (NEW)
| |-- configure-ecc/ # Interactive installation wizard (NEW)
| |-- security-scan/ # AgentShield security auditor integration (NEW)
| |-- java-coding-standards/ # Java coding standards (NEW)
| |-- jpa-patterns/ # JPA/Hibernate patterns (NEW)
| |-- postgres-patterns/ # PostgreSQL optimization patterns (NEW)
| |-- nutrient-document-processing/ # Document processing with Nutrient API (NEW)
| |-- docs/examples/project-guidelines-template.md # Template for project-specific skills
| |-- database-migrations/ # Migration patterns (Prisma, Drizzle, Django, Go) (NEW)
| |-- api-design/ # REST API design, pagination, error responses (NEW)
| |-- deployment-patterns/ # CI/CD, Docker, health checks, rollbacks (NEW)
| |-- docker-patterns/ # Docker Compose, networking, volumes, container security (NEW)
| |-- e2e-testing/ # Playwright E2E patterns and Page Object Model (NEW)
| |-- content-hash-cache-pattern/ # SHA-256 content hash caching for file processing (NEW)
| |-- cost-aware-llm-pipeline/ # LLM cost optimization, model routing, budget tracking (NEW)
| |-- regex-vs-llm-structured-text/ # Decision framework: regex vs LLM for text parsing (NEW)
| |-- swift-actor-persistence/ # Thread-safe Swift data persistence with actors (NEW)
| |-- swift-protocol-di-testing/ # Protocol-based DI for testable Swift code (NEW)
| |-- search-first/ # Research-before-coding workflow (NEW)
| |-- skill-stocktake/ # Audit skills and commands for quality (NEW)
| |-- liquid-glass-design/ # iOS 26 Liquid Glass design system (NEW)
| |-- foundation-models-on-device/ # Apple on-device LLM with FoundationModels (NEW)
| |-- swift-concurrency-6-2/ # Swift 6.2 Approachable Concurrency (NEW)
| |-- mle-workflow/ # Production ML data contracts, evals, deployment, monitoring (NEW)
| |-- perl-patterns/ # Modern Perl 5.36+ idioms and best practices (NEW)
| |-- perl-security/ # Perl security patterns, taint mode, safe I/O (NEW)
| |-- perl-testing/ # Perl TDD with Test2::V0, prove, Devel::Cover (NEW)
| |-- autonomous-loops/ # Autonomous loop patterns: sequential pipelines, PR loops, DAG orchestration (NEW)
| |-- plankton-code-quality/ # Write-time code quality enforcement with Plankton hooks (NEW)
|
|-- commands/ # Maintained slash-entry compatibility; prefer skills/
| |-- plan.md # /plan - Implementation planning
| |-- code-review.md # /code-review - Quality review
| |-- build-fix.md # /build-fix - Fix build errors
| |-- refactor-clean.md # /refactor-clean - Dead code removal
| |-- quality-gate.md # /quality-gate - Verification gate
| |-- learn.md # /learn - Extract patterns mid-session (Longform Guide)
| |-- learn-eval.md # /learn-eval - Extract, evaluate, and save patterns (NEW)
| |-- checkpoint.md # /checkpoint - Save verification state (Longform Guide)
| |-- setup-pm.md # /setup-pm - Configure package manager
| |-- go-review.md # /go-review - Go code review (NEW)
| |-- go-test.md # /go-test - Go TDD workflow (NEW)
| |-- go-build.md # /go-build - Fix Go build errors (NEW)
| |-- skill-create.md # /skill-create - Generate skills from git history (NEW)
| |-- instinct-status.md # /instinct-status - View learned instincts (NEW)
| |-- instinct-import.md # /instinct-import - Import instincts (NEW)
| |-- instinct-export.md # /instinct-export - Export instincts (NEW)
| |-- evolve.md # /evolve - Cluster instincts into skills
| |-- prune.md # /prune - Delete expired pending instincts (NEW)
| |-- pm2.md # /pm2 - PM2 service lifecycle management (NEW)
| |-- multi-plan.md # /multi-plan - Multi-agent task decomposition (NEW)
| |-- multi-execute.md # /multi-execute - Orchestrated multi-agent workflows (NEW)
| |-- multi-backend.md # /multi-backend - Backend multi-service orchestration (NEW)
| |-- multi-frontend.md # /multi-frontend - Frontend multi-service orchestration (NEW)
| |-- multi-workflow.md # /multi-workflow - General multi-service workflows (NEW)
| |-- sessions.md # /sessions - Session history management
| |-- test-coverage.md # /test-coverage - Test coverage analysis
| |-- update-docs.md # /update-docs - Update documentation
| |-- update-codemaps.md # /update-codemaps - Update codemaps
| |-- python-review.md # /python-review - Python code review (NEW)
|-- legacy-command-shims/ # Opt-in archive for retired shims such as /tdd and /eval
| |-- tdd.md # /tdd - Prefer the tdd-workflow skill
| |-- e2e.md # /e2e - Prefer the e2e-testing skill
| |-- eval.md # /eval - Prefer the eval-harness skill
| |-- verify.md # /verify - Prefer the verification-loop skill
| |-- orchestrate.md # /orchestrate - Prefer dmux-workflows or multi-workflow
|
|-- rules/ # Always-follow guidelines (copy to ~/.claude/rules/ecc/)
| |-- README.md # Structure overview and installation guide
| |-- common/ # Language-agnostic principles
| | |-- coding-style.md # Immutability, file organization
| | |-- git-workflow.md # Commit format, PR process
| | |-- testing.md # TDD, 80% coverage requirement
| | |-- performance.md # Model selection, context management
| | |-- patterns.md # Design patterns, skeleton projects
| | |-- hooks.md # Hook architecture, TodoWrite
| | |-- agents.md # When to delegate to subagents
| | |-- security.md # Mandatory security checks
| |-- typescript/ # TypeScript/JavaScript specific
| |-- python/ # Python specific
| |-- golang/ # Go specific
| |-- swift/ # Swift specific
| |-- php/ # PHP specific (NEW)
| |-- arkts/ # HarmonyOS / ArkTS specific
|
|-- hooks/ # Trigger-based automations
| |-- README.md # Hook documentation, recipes, and customization guide
| |-- hooks.json # All hooks config (PreToolUse, PostToolUse, Stop, etc.)
| |-- memory-persistence/ # Session lifecycle hooks (Longform Guide)
| |-- strategic-compact/ # Compaction suggestions (Longform Guide)
|
|-- scripts/ # Cross-platform Node.js scripts (NEW)
| |-- lib/ # Shared utilities
| | |-- utils.js # Cross-platform file/path/system utilities
| | |-- package-manager.js # Package manager detection and selection
| |-- hooks/ # Hook implementations
| | |-- session-start.js # Load context on session start
| | |-- session-end.js # Save state on session end
| | |-- pre-compact.js # Pre-compaction state saving
| | |-- suggest-compact.js # Strategic compaction suggestions
| | |-- evaluate-session.js # Extract patterns from sessions
| |-- setup-package-manager.js # Interactive PM setup
|
|-- tests/ # Test suite (NEW)
| |-- lib/ # Library tests
| |-- hooks/ # Hook tests
| |-- run-all.js # Run all tests
|
|-- contexts/ # Dynamic system prompt injection contexts (Longform Guide)
| |-- dev.md # Development mode context
| |-- review.md # Code review mode context
| |-- research.md # Research/exploration mode context
|
|-- examples/ # Example configurations and sessions
| |-- CLAUDE.md # Example project-level config
| |-- user-CLAUDE.md # Example user-level config
| |-- saas-nextjs-CLAUDE.md # Real-world SaaS (Next.js + Supabase + Stripe)
| |-- go-microservice-CLAUDE.md # Real-world Go microservice (gRPC + PostgreSQL)
| |-- django-api-CLAUDE.md # Real-world Django REST API (DRF + Celery)
| |-- laravel-api-CLAUDE.md # Real-world Laravel API (PostgreSQL + Redis) (NEW)
| |-- rust-api-CLAUDE.md # Real-world Rust API (Axum + SQLx + PostgreSQL) (NEW)
|
|-- mcp-configs/ # MCP server configurations
| |-- mcp-servers.json # GitHub, Supabase, Vercel, Railway, etc.
|
|-- ecc_dashboard.py # Desktop GUI dashboard (Tkinter)
|
|-- assets/ # Assets for dashboard
| |-- images/
| |-- ecc-logo.png
|
|-- marketplace.json # Self-hosted marketplace config (for /plugin marketplace add)

## Ecosystem Tools

### Skill Creator

Two ways to generate Claude Code skills from your repository:

#### Option A: Local Analysis (Built-in)

Use the/skill-createcommand for local analysis without external services:

/skill-create 
#
 Analyze current repo

/skill-create --instincts 
#
 Also generate instincts for continuous-learning-v2

This analyzes your git history locally and generates SKILL.md files.

#### Option B: GitHub App (Advanced)

For advanced features (10k+ commits, auto-PRs, team sharing):

Install GitHub App|ecc.tools

#
 Comment on any issue:

/skill-creator analyze

#
 Or auto-triggers on push to default branch

Both options create:

* SKILL.md files- Ready-to-use skills for Claude Code
* Instinct collections- For continuous-learning-v2
* Pattern extraction- Learns from your commit history

### AgentShield — Security Auditor

Built at the Claude Code Hackathon (Cerebral Valley x Anthropic, Feb 2026). 1282 tests, 98% coverage, 102 static analysis rules.

Scan your Claude Code configuration for vulnerabilities, misconfigurations, and injection risks.

#
 Quick scan (no install needed)

npx ecc-agentshield scan

#
 Auto-fix safe issues

npx ecc-agentshield scan --fix

#
 Deep analysis with three Opus 4.6 agents

npx ecc-agentshield scan --opus --stream

#
 Generate secure config from scratch

npx ecc-agentshield init

What it scans:CLAUDE.md, settings.json, MCP configs, hooks, agent definitions, and skills across 5 categories — secrets detection (14 patterns), permission auditing, hook injection analysis, MCP server risk profiling, and agent config review.

The--opusflagruns three Claude Opus 4.6 agents in a red-team/blue-team/auditor pipeline. The attacker finds exploit chains, the defender evaluates protections, and the auditor synthesizes both into a prioritized risk assessment. Adversarial reasoning, not just pattern matching.

Output formats:Terminal (color-graded A-F), JSON (CI pipelines), Markdown, HTML. Exit code 2 on critical findings for build gates.

Use/security-scanin Claude Code to run it, or add to CI with theGitHub Action.

GitHub|npm

### Continuous Learning v2

The instinct-based learning system automatically learns your patterns:

/instinct-status 
#
 Show learned instincts with confidence

/instinct-import 
<
file
>
 
#
 Import instincts from others

/instinct-export 
#
 Export your instincts for sharing

/evolve 
#
 Cluster related instincts into skills

Seeskills/continuous-learning-v2/for full documentation.
Keepcontinuous-learning/only when you explicitly want the legacy v1 Stop-hook learned-skill flow.

## Requirements

### Claude Code CLI Version

Minimum version: v2.1.0 or later

This plugin requires Claude Code CLI v2.1.0+ due to changes in how the plugin system handles hooks.

Check your version:

claude --version

### Important: Hooks Auto-Loading Behavior

WARNING:For Contributors:Do NOT add a"hooks"field to.claude-plugin/plugin.json. This is enforced by a regression test.

Claude Code v2.1+automatically loadshooks/hooks.jsonfrom any installed plugin by convention. Explicitly declaring it inplugin.jsoncauses a duplicate detection error:

Duplicate hooks file detected: ./hooks/hooks.json resolves to already-loaded file

History:This has caused repeated fix/revert cycles in this repo (#29,#52,#103). The behavior changed between Claude Code versions, leading to confusion. We now have a regression test to prevent this from being reintroduced.

## Installation

### Option 1: Install as Plugin (Recommended)

The easiest way to use this repo - install as a Claude Code plugin:

#
 Add this repo as a marketplace

/plugin marketplace add https://github.com/affaan-m/ECC

#
 Install the plugin

/plugin install ecc@ecc

Or add directly to your~/.claude/settings.json:

{
 
"extraKnownMarketplaces"
: {
 
"ecc"
: {
 
"source"
: {
 
"source"
: 
"
github
"
,
 
"repo"
: 
"
affaan-m/ECC
"

 }
 }
 },
 
"enabledPlugins"
: {
 
"ecc@ecc"
: 
true

 }
}

This gives you instant access to all commands, agents, skills, and hooks.

Note:The Claude Code plugin system does not support distributingrulesvia plugins (upstream limitation). You need to install rules manually:

#
 Clone the repo first

git clone https://github.com/affaan-m/ECC.git

cd
 ECC

#
 Option A: User-level rules (applies to all projects)

mkdir -p 
~
/.claude/rules/ecc
cp -r rules/common 
~
/.claude/rules/ecc/
cp -r rules/typescript 
~
/.claude/rules/ecc/ 
#
 pick your stack

cp -r rules/python 
~
/.claude/rules/ecc/
cp -r rules/golang 
~
/.claude/rules/ecc/
cp -r rules/php 
~
/.claude/rules/ecc/

#
 Option B: Project-level rules (applies to current project only)

mkdir -p .claude/rules/ecc
cp -r rules/common .claude/rules/ecc/
cp -r rules/typescript .claude/rules/ecc/ 
#
 pick your stack

### Option 2: Manual Installation

If you prefer manual control over what's installed:

#
 Clone the repo

git clone https://github.com/affaan-m/ECC.git

cd
 ECC

#
 Copy agents to your Claude config

cp agents/
*
.md 
~
/.claude/agents/

#
 Copy rules directories (common + language-specific)

mkdir -p 
~
/.claude/rules/ecc
cp -r rules/common 
~
/.claude/rules/ecc/
cp -r rules/typescript 
~
/.claude/rules/ecc/ 
#
 pick your stack

cp -r rules/python 
~
/.claude/rules/ecc/
cp -r rules/golang 
~
/.claude/rules/ecc/
cp -r rules/php 
~
/.claude/rules/ecc/
cp -r rules/arkts 
~
/.claude/rules/ecc/

#
 Copy skills first (primary workflow surface)

#
 Recommended (new users): core/general skills only

mkdir -p 
~
/.claude/skills/ecc
cp -r .agents/skills/
*
 
~
/.claude/skills/ecc/
cp -r skills/search-first 
~
/.claude/skills/ecc/

#
 Optional: add niche/framework-specific skills only when needed

#
 for s in django-patterns django-tdd laravel-patterns springboot-patterns quarkus-patterns; do

#
 cp -r skills/$s ~/.claude/skills/ecc/

#
 done

#
 Optional: keep maintained slash-command compatibility during migration

mkdir -p 
~
/.claude/commands
cp commands/
*
.md 
~
/.claude/commands/

#
 Retired shims live in legacy-command-shims/commands/.

#
 Copy individual files from there only if you still need old names such as /tdd.

#### Install hooks

Do not copy the raw repohooks/hooks.jsoninto~/.claude/settings.jsonor~/.claude/hooks/hooks.json. That file is plugin/repo-oriented and is meant to be installed through the ECC installer or loaded as a plugin, so raw copying is not a supported manual install path.

Use the installer to install only the Claude hook runtime so command paths are rewritten correctly:

#
 macOS / Linux

bash ./install.sh --target claude --modules hooks-runtime

#
 Windows PowerShell

pwsh 
-
File .\install.ps1 
--
target claude 
--
modules hooks
-
runtime

That writes resolved hooks to~/.claude/hooks/hooks.jsonand leaves any existing~/.claude/settings.jsonuntouched.

If you installed ECC via/plugin install, do not copy those hooks intosettings.json. Claude Code v2.1+ already auto-loads pluginhooks/hooks.json, and duplicating them insettings.jsoncauses duplicate execution and cross-platform hook conflicts.

Windows note: the Claude config directory is%USERPROFILE%\\.claude, not~/claude.

#### Configure MCPs

Claude plugin installs intentionally do not auto-enable ECC's bundled MCP server definitions. This avoids overlong plugin MCP tool names on strict third-party gateways while keeping manual MCP setup available.

Use Claude Code's/mcpcommand or CLI-managed MCP setup for live Claude Code server changes. Use/mcpfor Claude Code runtime disables; Claude Code persists those choices in~/.claude.json.

For repo-local MCP access, copy desired MCP server definitions frommcp-configs/mcp-servers.jsoninto a project-scoped.mcp.json.

If you already run your own copies of ECC-bundled MCPs, set:

export
 ECC_DISABLED_MCPS=
"
github,context7,exa,playwright,sequential-thinking,memory
"

ECC-managed install and Codex sync flows will skip or remove those bundled servers instead of re-adding duplicates.ECC_DISABLED_MCPSis an ECC install/sync filter, not a live Claude Code toggle.

Important:ReplaceYOUR_*_HEREplaceholders with your actual API keys.

## Key Concepts

### Agents

Subagents handle delegated tasks with limited scope. Example:

---

name
: 
code-reviewer

description
: 
Reviews code for quality, security, and maintainability

tools
: 
["Read", "Grep", "Glob", "Bash"]

model
: 
opus

---

You are a senior code reviewer...

### Skills

Skills are the primary workflow surface. They can be invoked directly, suggested automatically, and reused by agents. ECC still ships maintainedcommands/during migration, while retired short-name shims live underlegacy-command-shims/for explicit opt-in only. New workflow development should land inskills/first.

# 
TDD Workflow

1
.
 Define interfaces first

2
.
 Write failing tests (RED)

3
.
 Implement minimal code (GREEN)

4
.
 Refactor (IMPROVE)

5
.
 Verify 80%+ coverage

### Hooks

Hooks fire on tool events. Example - warn about console.log:

{
 
"matcher"
: 
"
tool == 
\"
Edit
\"
 && tool_input.file_path matches 
\"\\\\
.(ts|tsx|js|jsx)$
\"
"
,
 
"hooks"
: [{
 
"type"
: 
"
command
"
,
 
"command"
: 
"
#!/bin/bash
\n
grep -n 'console
\\
.log' 
\"
$file_path
\"
 && echo '[Hook] Remove console.log' >&2
"

 }]
}

### Rules

Rules are always-follow guidelines, organized intocommon/(language-agnostic) + language-specific directories:

rules/
 common/ # Universal principles (always install)
 typescript/ # TS/JS specific patterns and tools
 python/ # Python specific patterns and tools
 golang/ # Go specific patterns and tools
 swift/ # Swift specific patterns and tools
 php/ # PHP specific patterns and tools
 arkts/ # HarmonyOS / ArkTS patterns and constraints

Seerules/README.mdfor installation and structure details.

## Which Agent Should I Use?

Not sure where to start? Use this quick reference. Skills are the canonical workflow surface; maintained slash entries stay available for command-first workflows.

I want to...

Use this surface

Agent used

Plan a new feature

/ecc:plan "Add auth"

planner

Design system architecture

/ecc:plan
 + architect agent

architect

Write code with tests first

tdd-workflow
 skill

tdd-guide

Review code I just wrote

/code-review

code-reviewer

Fix a failing build

/build-fix

build-error-resolver

Run end-to-end tests

e2e-testing
 skill

e2e-runner

Find security vulnerabilities

/security-scan

security-reviewer

Remove dead code

/refactor-clean

refactor-cleaner

Update documentation

/update-docs

doc-updater

Review Go code

/go-review

go-reviewer

Review Python code

/python-review

python-reviewer

Review F# code

(invoke 
fsharp-reviewer
 directly)

fsharp-reviewer

Review TypeScript/JavaScript code

(invoke 
typescript-reviewer
 directly)

typescript-reviewer

Develop HarmonyOS apps

(invoke 
harmonyos-app-resolver
 directly)

harmonyos-app-resolver

Audit database queries

(auto-delegated)

database-reviewer

Review production ML changes

mle-workflow
 skill + 
mle-reviewer
 agent

mle-reviewer

### Common Workflows

Slash forms below are shown where they remain part of the maintained command surface. Retired short-name shims such as/tddand/evallive inlegacy-command-shims/for explicit opt-in only.

Starting a new feature:

/ecc:plan "Add user authentication with OAuth"
 → planner creates implementation blueprint
tdd-workflow skill → tdd-guide enforces write-tests-first
/code-review → code-reviewer checks your work

Fixing a bug:

tdd-workflow skill → tdd-guide: write a failing test that reproduces it
 → implement the fix, verify test passes
/code-review → code-reviewer: catch regressions

Preparing for production:

/security-scan → security-reviewer: OWASP Top 10 audit
e2e-testing skill → e2e-runner: critical user flow tests
/test-coverage → verify 80%+ coverage

## FAQ

How do I check which agents/commands are installed?

/plugin list ecc@ecc

This shows all available agents, commands, and skills from the plugin.

My hooks aren't working / I see "Duplicate hooks file" errors

This is the most common issue.Do NOT add a"hooks"field to.claude-plugin/plugin.json.Claude Code v2.1+ automatically loadshooks/hooks.jsonfrom installed plugins. Explicitly declaring it causes duplicate detection errors. See#29,#52,#103.

Can I use ECC with Claude Code on a custom API endpoint or model gateway?

Yes. ECC does not hardcode Anthropic-hosted transport settings. It runs locally through Claude Code's normal CLI/plugin surface, so it works with:

* Anthropic-hosted Claude Code
* Official Claude Code gateway setups usingANTHROPIC_BASE_URLandANTHROPIC_AUTH_TOKEN
* Compatible custom endpoints that speak the Anthropic API Claude Code expects

Minimal example:

export
 ANTHROPIC_BASE_URL=https://your-gateway.example.com

export
 ANTHROPIC_AUTH_TOKEN=your-token
claude

If your gateway remaps model names, configure that in Claude Code rather than in ECC. ECC's hooks, skills, commands, and rules are model-provider agnostic once theclaudeCLI is already working.

Official references:

* Claude Code LLM gateway docs
* Claude Code model configuration docs

My context window is shrinking / Claude is running out of context

Too many MCP servers eat your context. Each MCP tool description consumes tokens from your 200k window, potentially reducing it to ~70k. SessionStart context is capped at 8000 characters by default; lower it withECC_SESSION_START_MAX_CHARS=4000or disable it withECC_SESSION_START_CONTEXT=offfor local-model or low-context setups.

Fix:Disable unused MCPs from Claude Code with/mcp. Claude Code writes those runtime choices to~/.claude.json;.claude/settings.jsonand.claude/settings.local.jsonare not reliable toggles for already-loaded MCP servers.

Keep under 10 MCPs enabled and under 80 tools active.

Can I use only some components (e.g., just agents)?

Yes. Use Option 2 (manual installation) and copy only what you need:

#
 Just agents

cp agents/
*
.md 
~
/.claude/agents/

#
 Just rules

mkdir -p 
~
/.claude/rules/ecc/
cp -r rules/common 
~
/.claude/rules/ecc/

Each component is fully independent.

Does this work with Cursor / OpenCode / Codex / Antigravity / GitHub Copilot?

Yes. ECC is cross-platform:

* Cursor: Pre-translated configs in.cursor/. SeeCursor IDE Support.
* Gemini CLI: Experimental project-local support via.gemini/GEMINI.mdand shared installer plumbing.
* OpenCode: Full plugin support in.opencode/. SeeOpenCode Support.
* Codex: First-class support for both macOS app and CLI, with adapter drift guards and SessionStart fallback. See PR#257.
* GitHub Copilot (VS Code): Instruction and prompt layer via.github/copilot-instructions.md,.vscode/settings.json, and.github/prompts/. SeeGitHub Copilot Support.
* Antigravity: Tightly integrated setup for workflows, skills, and flattened rules in.agent/. SeeAntigravity Guide.
* JoyCode / CodeBuddy: Project-local selective install adapters for commands, agents, skills, and flattened rules. SeeJoyCode Adapter Guide.
* Qwen CLI: Home-directory selective install adapter for commands, agents, skills, rules, and Qwen config. SeeQwen CLI Adapter Guide.
* Zed: Project-local selective install adapter for.zed/settings.json, flattened rules, commands, agents, and skills.
* Non-native harnesses: Manual fallback path for Grok and similar interfaces. SeeManual Adaptation Guide.
* Claude Code: Native — this is the primary target.

How do I contribute a new skill or agent?

SeeCONTRIBUTING.md. The short version:

1. Fork the repo
2. Create your skill inskills/your-skill-name/SKILL.md(with YAML frontmatter)
3. Or create an agent inagents/your-agent.md
4. Submit a PR with a clear description of what it does and when to use it

## Running Tests

The plugin includes a comprehensive test suite:

#
 Run all tests

node tests/run-all.js

#
 Run individual test files

node tests/lib/utils.test.js
node tests/lib/package-manager.test.js
node tests/hooks/hooks.test.js

## Contributing

Contributions are welcome and encouraged.

This repo is meant to be a community resource. If you have:

* Useful agents or skills
* Clever hooks
* Better MCP configurations
* Improved rules

Please contribute! SeeCONTRIBUTING.mdfor guidelines.

### Ideas for Contributions

* Language-specific skills (Rust, C#, Kotlin, Java) — Go, Python, Perl, Swift, TypeScript, and HarmonyOS/ArkTS already included
* Framework-specific configs (Rails, FastAPI) — Django, NestJS, Spring Boot, and Laravel already included
* DevOps agents (Kubernetes, Terraform, AWS, Docker)
* Testing strategies (different frameworks, visual regression)
* Domain-specific knowledge (ML, data engineering, mobile)

### Community Ecosystem Notes

These are not bundled with ECC and are not audited by this repo, but they are worth knowing about if you are exploring the broader Claude Code skills ecosystem:

* claude-seo— SEO-focused skill and agent collection
* claude-ads— Ad-audit and paid-growth workflow collection
* claude-cybersecurity— Security-oriented skill and agent collection

## Cursor IDE Support

ECC provides Cursor IDE support with hooks, rules, agents, skills, commands, and MCP configs adapted for Cursor's project layout.

### Quick Start (Cursor)

#
 macOS/Linux

./install.sh --target cursor typescript
./install.sh --target cursor python golang swift php

#
 Windows PowerShell

.\install.ps1 
--
target cursor typescript
.\install.ps1 
--
target cursor python golang swift php

### What's Included

Component

Count

Details

Hook Events

15

sessionStart, beforeShellExecution, afterFileEdit, beforeMCPExecution, beforeSubmitPrompt, and 10 more

Hook Scripts

16

Thin Node.js scripts delegating to 
scripts/hooks/
 via shared adapter

Rules

34

9 common (alwaysApply) + 25 language-specific (TypeScript, Python, Go, Swift, PHP)

Agents

48

.cursor/agents/ecc-*.md
 when installed; prefixed to avoid collisions with user or marketplace agents

Skills

Shared + Bundled

.cursor/skills/
 for translated additions

Commands

Shared

.cursor/commands/
 if installed

MCP Config

Shared

.cursor/mcp.json
 if installed

### Cursor Loading Notes

ECC does not install rootAGENTS.mdinto.cursor/. Cursor treats nestedAGENTS.mdfiles as directory context, so copying ECC's repo identity into a host project would pollute that project.

Cursor-native loading behavior can vary by Cursor build. ECC installs agents as.cursor/agents/ecc-*.md; if your Cursor build does not expose project agents, those files still work as explicit reference definitions instead of hidden global prompt context.

### Hook Architecture (DRY Adapter Pattern)

Cursor hasmore hook events than Claude Code(20 vs 8). The.cursor/hooks/adapter.jsmodule transforms Cursor's stdin JSON to Claude Code's format, allowing existingscripts/hooks/*.jsto be reused without duplication.

Cursor stdin JSON → adapter.js → transforms → scripts/hooks/*.js
 (shared with Claude Code)

Key hooks:

* beforeShellExecution— Blocks dev servers outside tmux (exit 2), git push review
* afterFileEdit— Auto-format + TypeScript check + console.log warning
* beforeSubmitPrompt— Detects secrets (sk-, ghp_, AKIA patterns) in prompts
* beforeTabFileRead— Blocks Tab from reading .env, .key, .pem files (exit 2)
* beforeMCPExecution / afterMCPExecution— MCP audit logging

### Rules Format

Cursor rules use YAML frontmatter withdescription,globs, andalwaysApply:

---

description
: 
"
TypeScript coding style extending common rules
"

globs
: 
["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx"]

alwaysApply
: 
false

---

## Codex macOS App + CLI Support

ECC providesfirst-class Codex supportfor both the macOS app and CLI, with a reference configuration, Codex-specific AGENTS.md supplement, and shared skills.

### Quick Start (Codex App + CLI)

#
 Run Codex CLI in the repo — AGENTS.md and .codex/ are auto-detected

codex

#
 Automatic setup: sync ECC assets (AGENTS.md, skills, MCP servers) into ~/.codex

npm install 
&&
 bash scripts/sync-ecc-to-codex.sh

#
 or: pnpm install && bash scripts/sync-ecc-to-codex.sh

#
 or: yarn install && bash scripts/sync-ecc-to-codex.sh

#
 or: bun install && bash scripts/sync-ecc-to-codex.sh

#
 Or manually: copy the reference config to your home directory

cp .codex/config.toml 
~
/.codex/config.toml

The sync script safely merges ECC MCP servers into your existing~/.codex/config.tomlusing anadd-onlystrategy — it never removes or modifies your existing servers. Run with--dry-runto preview changes, or--update-mcpto force-refresh ECC servers to the latest recommended config.

For Context7, ECC uses the canonical Codex section name[mcp_servers.context7]while still launching the@upstash/context7-mcppackage. If you already have a legacy[mcp_servers.context7-mcp]entry,--update-mcpmigrates it to the canonical section name.

Codex macOS app:

* Open this repository as your workspace.
* The rootAGENTS.mdis auto-detected.
* .codex/config.tomland.codex/agents/*.tomlwork best when kept project-local.
* The reference.codex/config.tomlintentionally does not pinmodelormodel_provider, so Codex uses its own current default unless you override it.
* Optional: copy.codex/config.tomlto~/.codex/config.tomlfor global defaults; keep the multi-agent role files project-local unless you also copy.codex/agents/.

### What's Included

Component

Count

Details

Config

1

.codex/config.toml
 — top-level approvals/sandbox/web_search, MCP servers, notifications, profiles

AGENTS.md

2

Root (universal) + 
.codex/AGENTS.md
 (Codex-specific supplement)

Skills

32

.agents/skills/
 — SKILL.md + agents/openai.yaml per skill

MCP Servers

6

GitHub, Context7, Exa, Memory, Playwright, Sequential Thinking (7 with Supabase via 
--update-mcp
 sync)

Profiles

2

strict
 (read-only sandbox) and 
yolo
 (full auto-approve)

Agent Roles

3

.codex/agents/
 — explorer, reviewer, docs-researcher

### Skills

Skills at.agents/skills/are auto-loaded by Codex:

Canonical Anthropic skills such asclaude-api,frontend-design, andskill-creatorare intentionally not re-bundled here. Install those fromanthropics/skillswhen you want the official versions.

Skill

Description

agent-introspection-debugging

Debug agent behavior, routing, and prompt boundaries

agent-sort

Sort agent catalogs and assignment surfaces

api-design

REST API design patterns

article-writing

Long-form writing from notes and voice references

backend-patterns

API design, database, caching

brand-voice

Source-derived writing style profiles from real content

bun-runtime

Bun as runtime, package manager, bundler, and test runner

coding-standards

Universal coding standards

content-engine

Platform-native social content and repurposing

crosspost

Multi-platform content distribution across X, LinkedIn, Threads

deep-research

Multi-source research with synthesis and source attribution

dmux-workflows

Multi-agent orchestration using tmux pane manager

documentation-lookup

Up-to-date library and framework docs via Context7 MCP

e2e-testing

Playwright E2E tests

eval-harness

Eval-driven development

everything-claude-code

Development conventions and patterns for the project

exa-search

Neural search via Exa MCP for web, code, company research

fal-ai-media

Unified media generation for images, video, and audio

frontend-patterns

React/Next.js patterns

frontend-slides

HTML presentations, PPTX conversion, visual style exploration

investor-materials

Decks, memos, models, and one-pagers

investor-outreach

Personalized outreach, follow-ups, and intro blurbs

market-research

Source-attributed market and competitor research

mcp-server-patterns

Build MCP servers with Node/TypeScript SDK

nextjs-turbopack

Next.js 16+ and Turbopack incremental bundling

product-capability

Translate product goals into scoped capability maps

security-review

Comprehensive security checklist

strategic-compact

Context management

tdd-workflow

Test-driven development with 80%+ coverage

verification-loop

Build, test, lint, typecheck, security

video-editing

AI-assisted video editing workflows with FFmpeg and Remotion

x-api

X/Twitter API integration for posting and analytics

### Key Limitation

Codex doesnot yet provide Claude-style hook execution parity. ECC enforcement there is instruction-based viaAGENTS.md, optionalmodel_instructions_fileoverrides, and sandbox/approval settings.

### Multi-Agent Support

Current Codex builds support stable multi-agent workflows.

* Enablefeatures.multi_agent = truein.codex/config.toml
* Define roles under[agents.<name>]
* Point each role at a file under.codex/agents/
* Use/agentin the CLI to inspect or steer child agents

ECC ships three sample role configs:

Role

Purpose

explorer

Read-only codebase evidence gathering before edits

reviewer

Correctness, security, and missing-test review

docs_researcher

Documentation and API verification before release/docs changes

## Zed Support

ECC provides Zed project support through a conservative.zedadapter for project-local settings, flattened rules, agents, commands, and skills.

./install.sh --profile minimal --target zed

.\install.ps1 
--
profile minimal 
--
target zed

The adapter writes ECC-managed files under.zed/and keeps BYOK/OpenRouter credentials out of the repo. Configure Zed account or API keys through Zed's own settings UI or your local user settings.

## OpenCode Support

ECC providesfull OpenCode supportincluding plugins and hooks.

### Quick Start

#
 Install OpenCode

npm install -g opencode

#
 Run in the repository root

opencode

The configuration is automatically detected from.opencode/opencode.json.

### Feature Parity

Feature

Claude Code

OpenCode

Status

Agents

PASS: 60 agents

PASS: 12 agents

Claude Code leads

Commands

PASS: 75 commands

PASS: 35 commands

Claude Code leads

Skills

PASS: 232 skills

PASS: 37 skills

Claude Code leads

Hooks

PASS: 8 event types

PASS: 11 events

OpenCode has more!

Rules

PASS: 29 rules

PASS: 13 instructions

Claude Code leads

MCP Servers

PASS: 14 servers

PASS: Full

Full parity

Custom Tools

PASS: Via hooks

PASS: 6 native tools

OpenCode is better

### Hook Support via Plugins

OpenCode's plugin system is MORE sophisticated than Claude Code with 20+ event types:

Claude Code Hook

OpenCode Plugin Event

PreToolUse

tool.execute.before

PostToolUse

tool.execute.after

Stop

session.idle

SessionStart

session.created

SessionEnd

session.deleted

Additional OpenCode events:file.edited,file.watcher.updated,message.updated,lsp.client.diagnostics,tui.toast.show, and more.

### Maintained Slash Entries

Command

Description

/plan

Create implementation plan

/code-review

Review code changes

/build-fix

Fix build errors

/refactor-clean

Remove dead code

/learn

Extract patterns from session

/checkpoint

Save verification state

/quality-gate

Run the maintained verification gate

/update-docs

Update documentation

/update-codemaps

Update codemaps

/test-coverage

Analyze coverage

/go-review

Go code review

/go-test

Go TDD workflow

/go-build

Fix Go build errors

/python-review

Python code review (PEP 8, type hints, security)

/multi-plan

Multi-model collaborative planning

/multi-execute

Multi-model collaborative execution

/multi-backend

Backend-focused multi-model workflow

/multi-frontend

Frontend-focused multi-model workflow

/multi-workflow

Full multi-model development workflow

/pm2

Auto-generate PM2 service commands

/sessions

Manage session history

/skill-create

Generate skills from git

/instinct-status

View learned instincts

/instinct-import

Import instincts

/instinct-export

Export instincts

/evolve

Cluster instincts into skills

/promote

Promote project instincts to global scope

/projects

List known projects and instinct stats

/prune

Delete expired pending instincts (30d TTL)

/learn-eval

Extract and evaluate patterns before saving

/setup-pm

Configure package manager

/harness-audit

Audit harness reliability, eval readiness, and risk posture

/loop-start

Start controlled agentic loop execution pattern

/loop-status

Inspect active loop status and checkpoints

/quality-gate

Run quality gate checks for paths or entire repo

/model-route

Route tasks to models by complexity and budget

### Plugin Installation

Option 1: Use directly

cd
 ECC
opencode

Option 2: Install as npm package

npm install ecc-universal

Then add to youropencode.json:

{
 
"plugin"
: [
"
ecc-universal
"
]
}

That npm plugin entry enables ECC's published OpenCode plugin module (hooks/events and plugin tools).
It doesnotautomatically add ECC's full command/agent/instruction catalog to your project config.

For the full ECC OpenCode setup, either:

* run OpenCode inside this repository, or
* copy the bundled.opencode/config assets into your project and wire theinstructions,agent, andcommandentries inopencode.json

### Documentation

* Migration Guide:.opencode/MIGRATION.md
* OpenCode Plugin README:.opencode/README.md
* Consolidated Rules:.opencode/instructions/INSTRUCTIONS.md
* LLM Documentation:llms.txt(complete OpenCode docs for LLMs)

## GitHub Copilot Support

ECC providesGitHub Copilot supportfor VS Code via Copilot Chat's native instruction and prompt file system — no extra tooling required.

### What's Included

Component

File

Purpose

Core instructions

.github/copilot-instructions.md

Always-loaded rules: coding style, security, testing, git workflow

VS Code settings

.vscode/settings.json

Per-task instruction files for code gen, test gen, review, and commit messages

Plan prompt

.github/prompts/plan.prompt.md

Phased implementation planning

TDD prompt

.github/prompts/tdd.prompt.md

Red-Green-Improve cycle

Code review prompt

.github/prompts/code-review.prompt.md

Quality and security review

Security review prompt

.github/prompts/security-review.prompt.md

Deep OWASP-aligned security analysis

Build fix prompt

.github/prompts/build-fix.prompt.md

Systematic build and CI error resolution

Refactor prompt

.github/prompts/refactor.prompt.md

Dead code cleanup and simplification

### Quick Start (GitHub Copilot)

The files are already in place — open any repo that contains this project and GitHub Copilot Chat will automatically pick up.github/copilot-instructions.md.
The committed.vscode/settings.jsonenableschat.promptFilesso VS Code can load the reusable prompts from.github/prompts/.

To use the workflow prompts in Copilot Chat:

1. Open the Copilot Chat panel in VS Code.
2. Click thepaperclip / attachicon and selectPrompt..., or type/and choose a prompt.
3. Select the prompt (e.g.plan,tdd,code-review).

### How It Works

GitHub Copilot in VS Code reads two types of files automatically:

* .github/copilot-instructions.md— repository-level instructions, always injected into every Copilot Chat request. Contains ECC's core coding standards, security checklist, testing requirements, and git workflow.
* .github/prompts/*.prompt.md— reusable prompt files users invoke on demand. Each prompt walks Copilot through a specific ECC workflow (plan → TDD → review → ship).

The.vscode/settings.jsonadds per-task instruction overlays so Copilot receives the right context depending on whether you are generating code, writing tests, reviewing a selection, or drafting a commit message.

### Feature Coverage

ECC Feature

Copilot equivalent

Coding standards

Always-on via 
copilot-instructions.md

Security checklist

Always-on + 
security-review
 prompt

Testing / TDD

Always-on + 
tdd
 prompt

Implementation planning

plan
 prompt

Code review

code-review
 prompt

Build error resolution

build-fix
 prompt

Refactoring

refactor
 prompt

Commit message format

Per-task instruction in 
settings.json

Hooks / automation

Not supported (Copilot has no hook system)

Agents / delegation

Not supported (Copilot has no subagent API)

### Limitations

GitHub Copilot does not have a hook system or a subagent API, so ECC's hook automations (auto-format, TypeScript check, session persistence, dev-server guard) and agent delegation are unavailable. The instruction and prompt layer still brings the full ECC coding philosophy — standards, security, TDD, and workflow — into every Copilot Chat session.

## Cross-Tool Feature Parity

ECC is thefirst plugin to maximize every major AI coding tool. Here's how each harness compares:

Feature

Claude Code

Cursor IDE

Codex CLI

OpenCode

GitHub Copilot

Agents

60

Shared (AGENTS.md)

Shared (AGENTS.md)

12

N/A

Commands

75

Shared

Instruction-based

35

6 prompts

Skills

232

Shared

10 (native format)

37

Via instructions

Hook Events

8 types

15 types

None yet

11 types

None

Hook Scripts

20+ scripts

16 scripts (DRY adapter)

N/A

Plugin hooks

N/A

Rules

34 (common + lang)

34 (YAML frontmatter)

Instruction-based

13 instructions

1 always-on file

Custom Tools

Via hooks

Via hooks

N/A

6 native tools

N/A

MCP Servers

14

Shared (mcp.json)

7 (auto-merged via TOML parser)

Full

N/A

Config Format

settings.json

hooks.json + rules/

config.toml

opencode.json

copilot-instructions.md + settings.json

Context File

CLAUDE.md + AGENTS.md

AGENTS.md

AGENTS.md

AGENTS.md

copilot-instructions.md

Secret Detection

Hook-based

beforeSubmitPrompt hook

Sandbox-based

Hook-based

Instruction-based

Auto-Format

PostToolUse hook

afterFileEdit hook

N/A

file.edited hook

N/A

Version

Plugin

Plugin

Reference config

2.0.0-rc.1

Instruction layer

Key architectural decisions:

* AGENTS.mdat root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode — GitHub Copilot uses.github/copilot-instructions.mdinstead)
* DRY adapter patternlets Cursor reuse Claude Code's hook scripts without duplication
* Skills format(SKILL.md with YAML frontmatter) works across Claude Code, Codex, and OpenCode
* Codex's lack of hooks is compensated byAGENTS.md, optionalmodel_instructions_fileoverrides, and sandbox permissions

## Background

I've been using Claude Code since the experimental rollout. Won the Anthropic x Forum Ventures hackathon in Sep 2025 with@DRodriguezFX— builtzenith.chatentirely using Claude Code.

These configs are battle-tested across multiple production applications.

## Token Optimization

Claude Code usage can be expensive if you don't manage token consumption. These settings significantly reduce costs without sacrificing quality.

### Recommended Settings

Add to~/.claude/settings.json:

{
 
"model"
: 
"
sonnet
"
,
 
"env"
: {
 
"MAX_THINKING_TOKENS"
: 
"
10000
"
,
 
"CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"
: 
"
50
"

 }
}

Setting

Default

Recommended

Impact

model

opus

sonnet

~60% cost reduction; handles 80%+ of coding tasks

MAX_THINKING_TOKENS

31,999

10,000

~70% reduction in hidden thinking cost per request

CLAUDE_AUTOCOMPACT_PCT_OVERRIDE

95

50

Compacts earlier — better quality in long sessions

ECC_CONTEXT_MONITOR_COST_WARNINGS

on

off for subscription users

Suppresses agent-facing API-rate estimate warnings while keeping context/scope/loop warnings

Switch to Opus only when you need deep architectural reasoning:

/model opus

### Daily Workflow Commands

Command

When to Use

/model sonnet

Default for most tasks

/model opus

Complex architecture, debugging, deep reasoning

/clear

Between unrelated tasks (free, instant reset)

/compact

At logical task breakpoints (research done, milestone complete)

/cost

Monitor token spending during session

If you use a Claude subscription and the context monitor's API-rate estimates are not useful, setECC_CONTEXT_MONITOR_COST_WARNINGS=off. This only suppresses the agent-facing cost warnings; it does not disable context exhaustion, scope, or loop warnings.

### Strategic Compaction

Thestrategic-compactskill (included in this plugin) suggests/compactat logical breakpoints instead of relying on auto-compaction at 95% context. Seeskills/strategic-compact/SKILL.mdfor the full decision guide.

When to compact:

* After research/exploration, before implementation
* After completing a milestone, before starting the next
* After debugging, before continuing feature work
* After a failed approach, before trying a new one

When NOT to compact:

* Mid-implementation (you'll lose variable names, file paths, partial state)

### Context Window Management

Critical:Don't enable all MCPs at once. Each MCP tool description consumes tokens from your 200k window, potentially reducing it to ~70k.

* Keep under 10 MCPs enabled per project
* Keep under 80 tools active
* Use/mcpto disable unused Claude Code MCP servers; those runtime choices persist in~/.claude.json
* UseECC_DISABLED_MCPSonly to filter ECC-generated MCP configs during install/sync flows

### Agent Teams Cost Warning

Agent Teams spawns multiple context windows. Each teammate consumes tokens independently. Only use for tasks where parallelism provides clear value (multi-module work, parallel reviews). For simple sequential tasks, subagents are more token-efficient.

## WARNING: Important Notes

### Token Optimization

Hitting daily limits? See theToken Optimization Guidefor recommended settings and workflow tips.

Quick wins:

// ~/.claude/settings.json

{
 
"model"
: 
"
sonnet
"
,
 
"env"
: {
 
"MAX_THINKING_TOKENS"
: 
"
10000
"
,
 
"CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"
: 
"
50
"
,
 
"CLAUDE_CODE_SUBAGENT_MODEL"
: 
"
haiku
"

 }
}

Use/clearbetween unrelated tasks,/compactat logical breakpoints, and/costto monitor spending.

### Customization

These configs work for my workflow. You should:

1. Start with what resonates
2. Modify for your stack
3. Remove what you don't use
4. Add your own patterns

## Community Projects

Projects built on or inspired by ECC:

Project

Description

EVC

Marketing agent workspace — 42 commands for content operators, brand governance, and multi-channel publishing. 
Visual overview
.

trading-skills

68 trading-themed Claude Code skills with pre-trade review prompts and risk gates inspired by market operators.

Built something with ECC? Open a PR to add it here.

## Sponsors

This project is free and open source. Sponsors help keep it maintained and growing.

Become a Sponsor|Sponsor Tiers|Sponsorship Program

## Star History

## Links

* Shorthand Guide (Start Here):The Shorthand Guide to Everything Claude Code
* Longform Guide (Advanced):The Longform Guide to Everything Claude Code
* Security Guide:Security Guide|Thread
* Follow:@affaanmustafa

## License

MIT - Use freely, modify as needed, contribute back if you can.

Star this repo if it helps. Read both guides. Build something great.

## About

The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

ecc.tools

### Topics

 productivity

 mcp

 developer-tools

 ai-agents

 claude

 llm

 anthropic

 claude-code

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

192k

 stars
 

### Watchers

948

 watching
 

### Forks

29.7k

 forks
 

 Report repository

 

## Releases12

ECC v1.10.0 — Surface Refresh, Operator Workflows, and ECC 2.0 Alpha

 Latest

 

Apr 5, 2026

 

+ 11 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* https://ecc.tools

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript60.2%
* Rust30.3%
* Python5.2%
* Shell3.1%
* TypeScript1.0%
* Swift0.1%
* Other0.1%