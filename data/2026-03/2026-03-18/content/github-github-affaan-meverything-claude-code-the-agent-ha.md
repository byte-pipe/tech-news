---
title: 'GitHub - affaan-m/everything-claude-code: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. · GitHub'
url: https://github.com/affaan-m/everything-claude-code
site_name: github
content_file: github-github-affaan-meverything-claude-code-the-agent-ha
fetched_at: '2026-03-18T11:20:41.520004'
original_url: https://github.com/affaan-m/everything-claude-code
author: affaan-m
description: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. - affaan-m/everything-claude-code
---

affaan-m

 

/

everything-claude-code

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork11k
* Star84.3k

 
 
 
 
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

677 Commits
677 Commits
.agents/
skills
.agents/
skills
 
 
.claude-plugin
.claude-plugin
 
 
.claude
.claude
 
 
.codex
.codex
 
 
.cursor
.cursor
 
 
.github
.github
 
 
.opencode
.opencode
 
 
agents
agents
 
 
assets/
images
assets/
images
 
 
commands
commands
 
 
contexts
contexts
 
 
docs
docs
 
 
examples
examples
 
 
hooks
hooks
 
 
manifests
manifests
 
 
mcp-configs
mcp-configs
 
 
plugins
plugins
 
 
rules
rules
 
 
schemas
schemas
 
 
scripts
scripts
 
 
skills
skills
 
 
tests
tests
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.markdownlint.json
.markdownlint.json
 
 
.npmignore
.npmignore
 
 
.prettierrc
.prettierrc
 
 
.tool-versions
.tool-versions
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SPONSORING.md
SPONSORING.md
 
 
SPONSORS.md
SPONSORS.md
 
 
TROUBLESHOOTING.md
TROUBLESHOOTING.md
 
 
VERSION
VERSION
 
 
commitlint.config.js
commitlint.config.js
 
 
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
 
 
the-longform-guide.md
the-longform-guide.md
 
 
the-openclaw-guide.md
the-openclaw-guide.md
 
 
the-security-guide.md
the-security-guide.md
 
 
the-shortform-guide.md
the-shortform-guide.md
 
 
View all files

## Repository files navigation

Language:English |简体中文|繁體中文|日本語|한국어

# Everything Claude Code

50K+ stars|6K+ forks|30 contributors|5 languages supported|Anthropic Hackathon Winner

🌐 Language / 语言 / 語言

English|简体中文|繁體中文|日本語|한국어

The performance optimization system for AI agent harnesses. From an Anthropic hackathon winner.

Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development. Production-ready agents, hooks, commands, rules, and MCP configurations evolved over 10+ months of intensive daily use building real products.

Works acrossClaude Code,Codex,Cowork, and other AI agent harnesses.

## The Guides

This repo is the raw code only. The guides explain everything.

Shorthand Guide
Setup, foundations, philosophy. 
Read this first.

Longform Guide
Token optimization, memory persistence, evals, parallelization.

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

* Fixed instinct import content loss—parse_instinct_file()was silently dropping all content after frontmatter (Action, Evidence, Examples sections) during/instinct-import. Fixed by community contributor @ericcai0814 (#148,#161)

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

## 🚀 Quick Start

Get up and running in under 2 minutes:

### Step 1: Install the Plugin

#
 Add marketplace

/plugin marketplace add affaan-m/everything-claude-code

#
 Install plugin

/plugin install everything-claude-code@everything-claude-code

### Step 2: Install Rules (Required)

⚠️Important:Claude Code plugins cannot distributerulesautomatically. Install them manually:

#
 Clone the repo first

git clone https://github.com/affaan-m/everything-claude-code.git

cd
 everything-claude-code

#
 Install dependencies (pick your package manager)

npm install 
#
 or: pnpm install | yarn install | bun install

#
 macOS/Linux

./install.sh typescript 
#
 or python or golang or swift or php

#
 ./install.sh typescript python golang swift php

#
 ./install.sh --target cursor typescript

#
 ./install.sh --target antigravity typescript

#
 Windows PowerShell

.\install.ps1 typescript 
#
 or python or golang or swift or php

#
 .\install.ps1 typescript python golang swift php

#
 .\install.ps1 --target cursor typescript

#
 .\install.ps1 --target antigravity typescript

#
 npm-installed compatibility entrypoint also works cross-platform

npx ecc
-
install typescript

For manual install instructions see the README in therules/folder.

### Step 3: Start Using

#
 Try a command (plugin install uses namespaced form)

/everything-claude-code:plan 
"
Add user authentication
"

#
 Manual install (Option 2) uses the shorter form:

#
 /plan "Add user authentication"

#
 Check available commands

/plugin list everything-claude-code@everything-claude-code

✨That's it!You now have access to 25 agents, 108 skills, and 57 commands.

## 🌐 Cross-Platform Support

This plugin now fully supportsWindows, macOS, and Linux, alongside tight integration across major IDEs (Cursor, OpenCode, Antigravity) and CLI harnesses. All hooks and scripts have been rewritten in Node.js for maximum compatibility.

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

## 📦 What's Inside

This repo is aClaude Code plugin- install it directly or copy components manually.

everything-claude-code/
|-- .claude-plugin/ # Plugin and marketplace manifests
| |-- plugin.json # Plugin metadata and component paths
| |-- marketplace.json # Marketplace catalog for /plugin marketplace add
|
|-- agents/ # Specialized subagents for delegation
| |-- planner.md # Feature implementation planning
| |-- architect.md # System design decisions
| |-- tdd-guide.md # Test-driven development
| |-- code-reviewer.md # Quality and security review
| |-- security-reviewer.md # Vulnerability analysis
| |-- build-error-resolver.md
| |-- e2e-runner.md # Playwright E2E testing
| |-- refactor-cleaner.md # Dead code cleanup
| |-- doc-updater.md # Documentation sync
| |-- go-reviewer.md # Go code review
| |-- go-build-resolver.md # Go build error resolution
| |-- python-reviewer.md # Python code review (NEW)
| |-- database-reviewer.md # Database/Supabase review (NEW)
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
| |-- continuous-learning/ # Auto-extract patterns from sessions (Longform Guide)
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
| |-- project-guidelines-example/ # Template for project-specific skills
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
| |-- perl-patterns/ # Modern Perl 5.36+ idioms and best practices (NEW)
| |-- perl-security/ # Perl security patterns, taint mode, safe I/O (NEW)
| |-- perl-testing/ # Perl TDD with Test2::V0, prove, Devel::Cover (NEW)
| |-- autonomous-loops/ # Autonomous loop patterns: sequential pipelines, PR loops, DAG orchestration (NEW)
| |-- plankton-code-quality/ # Write-time code quality enforcement with Plankton hooks (NEW)
|
|-- commands/ # Slash commands for quick execution
| |-- tdd.md # /tdd - Test-driven development
| |-- plan.md # /plan - Implementation planning
| |-- e2e.md # /e2e - E2E test generation
| |-- code-review.md # /code-review - Quality review
| |-- build-fix.md # /build-fix - Fix build errors
| |-- refactor-clean.md # /refactor-clean - Dead code removal
| |-- learn.md # /learn - Extract patterns mid-session (Longform Guide)
| |-- learn-eval.md # /learn-eval - Extract, evaluate, and save patterns (NEW)
| |-- checkpoint.md # /checkpoint - Save verification state (Longform Guide)
| |-- verify.md # /verify - Run verification loop (Longform Guide)
| |-- setup-pm.md # /setup-pm - Configure package manager
| |-- go-review.md # /go-review - Go code review (NEW)
| |-- go-test.md # /go-test - Go TDD workflow (NEW)
| |-- go-build.md # /go-build - Fix Go build errors (NEW)
| |-- skill-create.md # /skill-create - Generate skills from git history (NEW)
| |-- instinct-status.md # /instinct-status - View learned instincts (NEW)
| |-- instinct-import.md # /instinct-import - Import instincts (NEW)
| |-- instinct-export.md # /instinct-export - Export instincts (NEW)
| |-- evolve.md # /evolve - Cluster instincts into skills
| |-- pm2.md # /pm2 - PM2 service lifecycle management (NEW)
| |-- multi-plan.md # /multi-plan - Multi-agent task decomposition (NEW)
| |-- multi-execute.md # /multi-execute - Orchestrated multi-agent workflows (NEW)
| |-- multi-backend.md # /multi-backend - Backend multi-service orchestration (NEW)
| |-- multi-frontend.md # /multi-frontend - Frontend multi-service orchestration (NEW)
| |-- multi-workflow.md # /multi-workflow - General multi-service workflows (NEW)
| |-- orchestrate.md # /orchestrate - Multi-agent coordination
| |-- sessions.md # /sessions - Session history management
| |-- eval.md # /eval - Evaluate against criteria
| |-- test-coverage.md # /test-coverage - Test coverage analysis
| |-- update-docs.md # /update-docs - Update documentation
| |-- update-codemaps.md # /update-codemaps - Update codemaps
| |-- python-review.md # /python-review - Python code review (NEW)
|
|-- rules/ # Always-follow guidelines (copy to ~/.claude/rules/)
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
|-- marketplace.json # Self-hosted marketplace config (for /plugin marketplace add)

## 🛠️ Ecosystem Tools

### Skill Creator

Two ways to generate Claude Code skills from your repository:

#### Option A: Local Analysis (Built-in)

Use the/skill-createcommand for local analysis without external services:

/skill-create 
#
 Analyze current repo

/skill-create --instincts 
#
 Also generate instincts for continuous-learning

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

### 🔬 Plankton — Write-Time Code Quality Enforcement

Plankton (credit: @alxfazio) is a recommended companion for write-time code quality enforcement. It runs formatters and 20+ linters on every file edit via PostToolUse hooks, then spawns Claude subprocesses (routed to Haiku/Sonnet/Opus by violation complexity) to fix issues the main agent missed. Three-phase architecture: auto-format silently (40-50% of issues), collect remaining violations as structured JSON, delegate fixes to a subprocess. Includes config protection hooks that prevent agents from modifying linter configs to pass instead of fixing code. Supports Python, TypeScript, Shell, YAML, JSON, TOML, Markdown, and Dockerfile. Use alongside AgentShield for security + quality coverage. Seeskills/plankton-code-quality/for full integration guide.

### 🧠 Continuous Learning v2

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

## 📋 Requirements

### Claude Code CLI Version

Minimum version: v2.1.0 or later

This plugin requires Claude Code CLI v2.1.0+ due to changes in how the plugin system handles hooks.

Check your version:

claude --version

### Important: Hooks Auto-Loading Behavior

⚠️For Contributors:Do NOT add a"hooks"field to.claude-plugin/plugin.json. This is enforced by a regression test.

Claude Code v2.1+automatically loadshooks/hooks.jsonfrom any installed plugin by convention. Explicitly declaring it inplugin.jsoncauses a duplicate detection error:

Duplicate hooks file detected: ./hooks/hooks.json resolves to already-loaded file

History:This has caused repeated fix/revert cycles in this repo (#29,#52,#103). The behavior changed between Claude Code versions, leading to confusion. We now have a regression test to prevent this from being reintroduced.

## 📥 Installation

### Option 1: Install as Plugin (Recommended)

The easiest way to use this repo - install as a Claude Code plugin:

#
 Add this repo as a marketplace

/plugin marketplace add affaan-m/everything-claude-code

#
 Install the plugin

/plugin install everything-claude-code@everything-claude-code

Or add directly to your~/.claude/settings.json:

{
 
"extraKnownMarketplaces"
: {
 
"everything-claude-code"
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
affaan-m/everything-claude-code
"

 }
 }
 },
 
"enabledPlugins"
: {
 
"everything-claude-code@everything-claude-code"
: 
true

 }
}

This gives you instant access to all commands, agents, skills, and hooks.

Note:The Claude Code plugin system does not support distributingrulesvia plugins (upstream limitation). You need to install rules manually:

#
 Clone the repo first

git clone https://github.com/affaan-m/everything-claude-code.git

#
 Option A: User-level rules (applies to all projects)

mkdir -p 
~
/.claude/rules
cp -r everything-claude-code/rules/common/
*
 
~
/.claude/rules/
cp -r everything-claude-code/rules/typescript/
*
 
~
/.claude/rules/ 
#
 pick your stack

cp -r everything-claude-code/rules/python/
*
 
~
/.claude/rules/
cp -r everything-claude-code/rules/golang/
*
 
~
/.claude/rules/
cp -r everything-claude-code/rules/php/
*
 
~
/.claude/rules/

#
 Option B: Project-level rules (applies to current project only)

mkdir -p .claude/rules
cp -r everything-claude-code/rules/common/
*
 .claude/rules/
cp -r everything-claude-code/rules/typescript/
*
 .claude/rules/ 
#
 pick your stack

### 🔧 Option 2: Manual Installation

If you prefer manual control over what's installed:

#
 Clone the repo

git clone https://github.com/affaan-m/everything-claude-code.git

#
 Copy agents to your Claude config

cp everything-claude-code/agents/
*
.md 
~
/.claude/agents/

#
 Copy rules (common + language-specific)

cp -r everything-claude-code/rules/common/
*
 
~
/.claude/rules/
cp -r everything-claude-code/rules/typescript/
*
 
~
/.claude/rules/ 
#
 pick your stack

cp -r everything-claude-code/rules/python/
*
 
~
/.claude/rules/
cp -r everything-claude-code/rules/golang/
*
 
~
/.claude/rules/
cp -r everything-claude-code/rules/php/
*
 
~
/.claude/rules/

#
 Copy commands

cp everything-claude-code/commands/
*
.md 
~
/.claude/commands/

#
 Copy skills (core vs niche)

#
 Recommended (new users): core/general skills only

cp -r everything-claude-code/.agents/skills/
*
 
~
/.claude/skills/
cp -r everything-claude-code/skills/search-first 
~
/.claude/skills/

#
 Optional: add niche/framework-specific skills only when needed

#
 for s in django-patterns django-tdd laravel-patterns springboot-patterns; do

#
 cp -r everything-claude-code/skills/$s ~/.claude/skills/

#
 done

#### Add hooks to settings.json

Copy the hooks fromhooks/hooks.jsonto your~/.claude/settings.json.

#### Configure MCPs

Copy desired MCP servers frommcp-configs/mcp-servers.jsonto your~/.claude.json.

Important:ReplaceYOUR_*_HEREplaceholders with your actual API keys.

## 🎯 Key Concepts

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

Skills are workflow definitions invoked by commands or agents:

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

Seerules/README.mdfor installation and structure details.

## 🗺️ Which Agent Should I Use?

Not sure where to start? Use this quick reference:

I want to...

Use this command

Agent used

Plan a new feature

/everything-claude-code:plan "Add auth"

planner

Design system architecture

/everything-claude-code:plan
 + architect agent

architect

Write code with tests first

/tdd

tdd-guide

Review code I just wrote

/code-review

code-reviewer

Fix a failing build

/build-fix

build-error-resolver

Run end-to-end tests

/e2e

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

Audit database queries

(auto-delegated)

database-reviewer

### Common Workflows

Starting a new feature:

/everything-claude-code:plan "Add user authentication with OAuth"
 → planner creates implementation blueprint
/tdd → tdd-guide enforces write-tests-first
/code-review → code-reviewer checks your work

Fixing a bug:

/tdd → tdd-guide: write a failing test that reproduces it
 → implement the fix, verify test passes
/code-review → code-reviewer: catch regressions

Preparing for production:

/security-scan → security-reviewer: OWASP Top 10 audit
/e2e → e2e-runner: critical user flow tests
/test-coverage → verify 80%+ coverage

## ❓ FAQ

How do I check which agents/commands are installed?

/plugin list everything-claude-code@everything-claude-code

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

Too many MCP servers eat your context. Each MCP tool description consumes tokens from your 200k window, potentially reducing it to ~70k.

Fix:Disable unused MCPs per project:

// In your project's .claude/settings.json

{
 
"disabledMcpServers"
: [
"
supabase
"
, 
"
railway
"
, 
"
vercel
"
]
}

Keep under 10 MCPs enabled and under 80 tools active.

Can I use only some components (e.g., just agents)?

Yes. Use Option 2 (manual installation) and copy only what you need:

#
 Just agents

cp everything-claude-code/agents/
*
.md 
~
/.claude/agents/

#
 Just rules

cp -r everything-claude-code/rules/common/
*
 
~
/.claude/rules/

Each component is fully independent.

Does this work with Cursor / OpenCode / Codex / Antigravity?

Yes. ECC is cross-platform:

* Cursor: Pre-translated configs in.cursor/. SeeCursor IDE Support.
* OpenCode: Full plugin support in.opencode/. SeeOpenCode Support.
* Codex: First-class support for both macOS app and CLI, with adapter drift guards and SessionStart fallback. See PR#257.
* Antigravity: Tightly integrated setup for workflows, skills, and flatten rules in.agent/.
* Claude Code: Native — this is the primary target.

How do I contribute a new skill or agent?

SeeCONTRIBUTING.md. The short version:

1. Fork the repo
2. Create your skill inskills/your-skill-name/SKILL.md(with YAML frontmatter)
3. Or create an agent inagents/your-agent.md
4. Submit a PR with a clear description of what it does and when to use it

## 🧪 Running Tests

The plugin includes a comprehensive test suite:

#
 Run all tests

node tests/run-all.js

#
 Run individual test files

node tests/lib/utils.test.js
node tests/lib/package-manager.test.js
node tests/hooks/hooks.test.js

## 🤝 Contributing

Contributions are welcome and encouraged.

This repo is meant to be a community resource. If you have:

* Useful agents or skills
* Clever hooks
* Better MCP configurations
* Improved rules

Please contribute! SeeCONTRIBUTING.mdfor guidelines.

### Ideas for Contributions

* Language-specific skills (Rust, C#, Kotlin, Java) — Go, Python, Perl, Swift, and TypeScript already included
* Framework-specific configs (Rails, FastAPI, NestJS) — Django, Spring Boot, Laravel already included
* DevOps agents (Kubernetes, Terraform, AWS, Docker)
* Testing strategies (different frameworks, visual regression)
* Domain-specific knowledge (ML, data engineering, mobile)

## Cursor IDE Support

ECC providesfull Cursor IDE supportwith hooks, rules, agents, skills, commands, and MCP configs adapted for Cursor's native format.

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

Shared

Via AGENTS.md at root (read by Cursor natively)

Skills

Shared + Bundled

Via AGENTS.md at root and 
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
 Optional: copy the global-safe defaults to your home directory

cp .codex/config.toml 
~
/.codex/config.toml

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

16

.agents/skills/
 — SKILL.md + agents/openai.yaml per skill

MCP Servers

4

GitHub, Context7, Memory, Sequential Thinking (command-based)

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

Skill

Description

tdd-workflow

Test-driven development with 80%+ coverage

security-review

Comprehensive security checklist

coding-standards

Universal coding standards

frontend-patterns

React/Next.js patterns

frontend-slides

HTML presentations, PPTX conversion, visual style exploration

article-writing

Long-form writing from notes and voice references

content-engine

Platform-native social content and repurposing

market-research

Source-attributed market and competitor research

investor-materials

Decks, memos, models, and one-pagers

investor-outreach

Personalized outreach, follow-ups, and intro blurbs

backend-patterns

API design, database, caching

e2e-testing

Playwright E2E tests

eval-harness

Eval-driven development

strategic-compact

Context management

api-design

REST API design patterns

verification-loop

Build, test, lint, typecheck, security

### Key Limitation

Codex doesnot yet provide Claude-style hook execution parity. ECC enforcement there is instruction-based viaAGENTS.md, optionalmodel_instructions_fileoverrides, and sandbox/approval settings.

### Multi-Agent Support

Current Codex builds support experimental multi-agent workflows.

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

## 🔌 OpenCode Support

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

✅ 25 agents

✅ 12 agents

Claude Code leads

Commands

✅ 57 commands

✅ 31 commands

Claude Code leads

Skills

✅ 108 skills

✅ 37 skills

Claude Code leads

Hooks

✅ 8 event types

✅ 11 events

OpenCode has more!

Rules

✅ 29 rules

✅ 13 instructions

Claude Code leads

MCP Servers

✅ 14 servers

✅ Full

Full parity

Custom Tools

✅ Via hooks

✅ 6 native tools

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

### Available Commands (31+)

Command

Description

/plan

Create implementation plan

/tdd

Enforce TDD workflow

/code-review

Review code changes

/build-fix

Fix build errors

/e2e

Generate E2E tests

/refactor-clean

Remove dead code

/orchestrate

Multi-agent workflow

/learn

Extract patterns from session

/checkpoint

Save verification state

/verify

Run verification loop

/eval

Evaluate against criteria

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
 everything-claude-code
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

## Cross-Tool Feature Parity

ECC is thefirst plugin to maximize every major AI coding tool. Here's how each harness compares:

Feature

Claude Code

Cursor IDE

Codex CLI

OpenCode

Agents

21

Shared (AGENTS.md)

Shared (AGENTS.md)

12

Commands

52

Shared

Instruction-based

31

Skills

102

Shared

10 (native format)

37

Hook Events

8 types

15 types

None yet

11 types

Hook Scripts

20+ scripts

16 scripts (DRY adapter)

N/A

Plugin hooks

Rules

34 (common + lang)

34 (YAML frontmatter)

Instruction-based

13 instructions

Custom Tools

Via hooks

Via hooks

N/A

6 native tools

MCP Servers

14

Shared (mcp.json)

4 (command-based)

Full

Config Format

settings.json

hooks.json + rules/

config.toml

opencode.json

Context File

CLAUDE.md + AGENTS.md

AGENTS.md

AGENTS.md

AGENTS.md

Secret Detection

Hook-based

beforeSubmitPrompt hook

Sandbox-based

Hook-based

Auto-Format

PostToolUse hook

afterFileEdit hook

N/A

file.edited hook

Version

Plugin

Plugin

Reference config

1.8.0

Key architectural decisions:

* AGENTS.mdat root is the universal cross-tool file (read by all 4 tools)
* DRY adapter patternlets Cursor reuse Claude Code's hook scripts without duplication
* Skills format(SKILL.md with YAML frontmatter) works across Claude Code, Codex, and OpenCode
* Codex's lack of hooks is compensated byAGENTS.md, optionalmodel_instructions_fileoverrides, and sandbox permissions

## 📖 Background

I've been using Claude Code since the experimental rollout. Won the Anthropic x Forum Ventures hackathon in Sep 2025 buildingzenith.chatwith@DRodriguezFX- entirely using Claude Code.

These configs are battle-tested across multiple production applications.

## Inspiration Credits

* inspired byzarazhangrui
* homunculus-inspired byhumanplane

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
* UsedisabledMcpServersin project config to disable unused ones

### Agent Teams Cost Warning

Agent Teams spawns multiple context windows. Each teammate consumes tokens independently. Only use for tasks where parallelism provides clear value (multi-module work, parallel reviews). For simple sequential tasks, subagents are more token-efficient.

## ⚠️Important Notes

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

## 💜 Sponsors

This project is free and open source. Sponsors help keep it maintained and growing.

Become a Sponsor|Sponsor Tiers|Sponsorship Program

## 🌟 Star History

## 🔗 Links

* Shorthand Guide (Start Here):The Shorthand Guide to Everything Claude Code
* Longform Guide (Advanced):The Longform Guide to Everything Claude Code
* Follow:@affaanmustafa
* zenith.chat:zenith.chat
* Skills Directory:awesome-agent-skills (community-maintained directory of agent skills)

## 📄 License

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
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

84.3k

 stars
 

### Watchers

440

 watching
 

### Forks

11k

 forks
 

 Report repository

 

## Releases10

ECC v1.8.0 — Harness Performance & Cross-Platform Reliability

 Latest

 

Mar 5, 2026

 

+ 9 releases

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

* JavaScript88.0%
* Python5.0%
* Shell4.7%
* TypeScript2.2%
* PowerShell0.1%