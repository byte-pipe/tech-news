---
title: 'GitHub - hesreallyhim/awesome-claude-code: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic · GitHub'
url: https://github.com/hesreallyhim/awesome-claude-code
site_name: github
content_file: github-github-hesreallyhimawesome-claude-code-a-curated-l
fetched_at: '2026-03-23T11:21:16.388795'
original_url: https://github.com/hesreallyhim/awesome-claude-code
author: hesreallyhim
description: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic - hesreallyhim/awesome-claude-code
---

hesreallyhim

 

/

awesome-claude-code

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.1k
* Star30.4k

 
 
 
 
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

901 Commits
901 Commits
.claude/
commands
.claude/
commands
 
 
.github
.github
 
 
README_ALTERNATIVES
README_ALTERNATIVES
 
 
assets
assets
 
 
data
data
 
 
docs
docs
 
 
resources
resources
 
 
scripts
scripts
 
 
templates
templates
 
 
tests
tests
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
THE_RESOURCES_TABLE.csv
THE_RESOURCES_TABLE.csv
 
 
acc-config.yaml
acc-config.yaml
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

### Pick Your Style:

# Awesome Claude Code

A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing yourClaude Codeworkflow.

## Latest Additions

* Claude Scientific SkillsbyK-Dense- "A set of ready-to-use Agent Skills for research, science, engineering, analysis, finance and writing." That's their description - modest, simple. That's how you can tell this is really one of the best skills repos on GitHub. If you've ever thought about getting a PhD... just read all of these documents instead. Also I think it IS an AI agent or something? Awesome.
* parrybyDmytro Onypko- Prompt injection scanner for Claude Code hooks. Scans tool inputs and outputs for injection attacks, secrets, and data exfiltration attempts. [NOTE: Early development phase but worth a look.].
* DippybyLily Dayton- Auto-approve safe bash commands using AST-based parsing, while prompting for destructive operations. Solves permission fatigue without disabling safety. Supports Claude Code, Gemini CLI, and Cursor.
* sudocodebyssh-randy- Lightweight agent orchestration dev tool that lives in your repo. Integrates with various specification frameworks. It's giving Jira.
* claude-tmuxbyNiels Groeneveld- Manage Claude Code within tmux. A tmux popup of all your Claude Code instances, enabling quick switching, status monitoring, session lifecycle management, with git worktree and pull request support.
* claude-espbyphiat- Go-based TUI that streams Claude Code's hidden output (thinking, tool calls, subagents) to a separate terminal. Watch multiple sessions simultaneously, filter by content type, and track background tasks. Ideal for debugging or understanding what Claude is doing under the hood without interrupting your main session.

## Contents

* Agent Skills 🤖General
* General
* Workflows & Knowledge Guides 🧠GeneralRalph Wiggum
* General
* Ralph Wiggum
* Tooling 🧰GeneralIDE IntegrationsUsage MonitorsOrchestratorsConfig Managers
* General
* IDE Integrations
* Usage Monitors
* Orchestrators
* Config Managers
* Status Lines 📊General
* General
* Hooks 🪝General
* General
* Slash-Commands 🔪GeneralVersion Control & GitCode Analysis & TestingContext Loading & PrimingDocumentation & ChangelogsCI / DeploymentProject & Task ManagementMiscellaneous
* General
* Version Control & Git
* Code Analysis & Testing
* Context Loading & Priming
* Documentation & Changelogs
* CI / Deployment
* Project & Task Management
* Miscellaneous
* CLAUDE.md Files 📂Language-SpecificDomain-SpecificProject Scaffolding & MCP
* Language-Specific
* Domain-Specific
* Project Scaffolding & MCP
* Alternative Clients 📱General
* General
* Official Documentation 🏛️General
* General

## Agent Skills 🤖

Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

### General

* AgentSysbyavifenesh- Workflow automation system for Claude with a group of useful plugins, agents, and skills. Automates task-to-production workflows, PR management, code cleanup, performance investigation, drift detection, and multi-agent code review. Includesagnixfor linting agent configurations. Built on thousands of lines of code with thousands of tests. Uses deterministic detection (regex, AST) with LLM judgment for efficiency. Used on many production systems.
* AI Agent, AI SpybyWhittaker & Tiwari- Members from the Signal Foundation with some really great tips and tricks on how to turn your operating system into an instrument of total surveillance, and why some companies are doing this really awesome thing. [warning: YouTube link].
* Book FactorybyRobert Guss- A comprehensive pipeline of Skills that replicates traditional publishing infrastructure for nonfiction book creation using specialized Claude skills.
* cc-devops-skillsbyakin-ozer- Immensely detailed set of skills for DevOps Engineers (or anyone who has to deploy code, really). Works with validations, generators, shell scripts and CLI tools to create high quality IaC code for about any platform you've ever struggled painfully to work with. Worth downloading even just as a source of documentation.
* Claude Code AgentsbyPaul - UndeadList- Comprehensive E2E development workflow with helpful Claude Code subagent prompts for solo devs. Run multiple auditors in parallel, automate fix cycles with micro-checkpoint protocols, and do browser-based QA. Includes strict protocols to prevent AI going rogue.
* Claude Codex Settingsbyfatih akyon- A well-organized, well-written set of plugins covering core developer activities, such as working with common cloud platforms like GitHub, Azure, MongoDB, and popular services such as Tavily, Playwright, and more. Clear, not overly-opinionated, and compatible with a few other providers.
* Claude Mountaineering SkillsbyDmytro Gaivoronsky- Claude Code skill that automates mountain route research for North American peaks. Aggregates data from 10+ mountaineering sources like Mountaineers.org, PeakBagger.com and SummitPost.com to generate detailed route beta reports with weather, avalanche conditions, and trip reports.
* Claude Scientific SkillsbyK-Dense- "A set of ready-to-use Agent Skills for research, science, engineering, analysis, finance and writing." That's their description - modest, simple. That's how you can tell this is really one of the best skills repos on GitHub. If you've ever thought about getting a PhD... just read all of these documents instead. Also I think it IS an AI agent or something? Awesome.
* Codex Skillbyklaudworks- Enables users to prompt codex from claude code. Unlike the raw codex mcp server, this skill infers parameters such as model, reasoning effort, sandboxing from your prompt or asks you to specify them. It also simplifies continuing prior codex sessions so that codex can continue with the prior context.
* Compound Engineering PluginbyEveryInc- A very pragmatic set of well-designed agents, skills, and commands, built around a discipline of turning past mistakes and errors into lessons and opportunities for future growth and improvement. Good documentation.
* Context Engineering KitbyVlad Goncharov- Hand-crafted collection of advanced context engineering techniques and patterns with minimal token footprint focused on improving agent result quality.
* Everything Claude CodebyAffaan Mustafa- Top-notch, well-written resources covering "just about everything" from core engineering domains. What's nice about this "everything-" store is most of the resources have significant standalone value and unlike some all-encompassing frameworks, although you can opt in to the author's own specific workflow patterns if you choose, the individual resources offer exemplary patterns in (just about) every Claude Code feature you can find (apologies to the Output Styles devotees).
* Fullstack Dev Skillsbyjeffallan- A comprehensive Claude Code plugin with 65 specialized skills covering full-stack development across a wide range of specific frameworks. Features 9 project workflow commands for Jira/Confluence integration and, notably, an interesting approach to context engineering via a/common-groundcommand that surfaces Claude's hidden assumptions about your project. This is a smart thing to do.
* read-only-postgresbyjawwadfirdousi- Read-only PostgreSQL query skill for Claude Code. Executes SELECT/SHOW/EXPLAIN/WITH queries across configured databases with strict validation, timeouts, and row limits. Supports multiple connections with descriptions for database selection.
* SuperpowersbyJesse Vincent- A strong bundle of core competencies for software engineering, with good coverage of a large portion of the SDLC - from planning, reviewing, testing, debugging... Well written, well organized, and adaptable. The author refers to them as "superpowers", but many of them are just consolidating engineering best practices - which sometimes does feel like a superpower when working with Claude Code.
* Trail of Bits Security SkillsbyTrail of Bits- A very professional collection of over a dozen security-focused skills for code auditing and vulnerability detection. Includes skills for static analysis with CodeQL and Semgrep, variant analysis across codebases, fix verification, and differential code review.
* TÂCHES Claude Code ResourcesbyTÂCHES- A well-balanced, "down-to-Earth" set of sub agents, skills, and commands, that are well-organized, easy to read, and a healthy focus on "meta"-skills/agents, like "skill-auditor", hook creation, etc. - the kind of things you can adapt to your workflow, and not the other way around.
* Web Assets Generator SkillbyAlon Wolenitz- Easily generate web assets from Claude Code including favicons, app icons (PWA), and social media meta images (Open Graph) for Facebook, Twitter, WhatsApp, and LinkedIn. Handles image resizing, text-to-image generation, emojis, and provides proper HTML meta tags.

## Workflows & Knowledge Guides 🧠

A workflow is a tightly coupled set of Claude Code-native resources that facilitate specific projects

### General

* AB MethodbyAyoub Bensalah- A principled, spec-driven workflow that transforms large problems into focused, incremental missions using Claude Code's specialized sub agents. Includes slash-commands, sub agents, and specialized workflows designed for specific parts of the SDLC.
* Agentic Workflow PatternsbyThibautMelen- A comprehensive and well-documented collection of agentic patterns from Anthropic docs, with colorful Mermaid diagrams and code examples for each pattern. Covers Subagent Orchestration, Progressive Skills, Parallel Tool Calling, Master-Clone Architecture, Wizard Workflows, and more. Also compatible with other providers.
* Blogging Platform Instructionsbycloudartisan- Provides a well-structured set of commands for publishing and maintaining a blogging platform, including commands for creating posts, managing categories, and handling media files.
* Claude Code Documentation MirrorbyEric Buess- A mirror of the Anthropic © PBC documentation pages for Claude Code, updated every few hours. Can come in handy when trying to stay on top of the ever-expanding feature-set of Dr. Claw D. Code, Ph.D.
* Claude Code Handbookbynikiforovall- Collection of best practices, tips, and techniques for Claude Code development workflows, enhanced with distributable plugins.
* Claude Code Infrastructure Showcasebydiet103- A remarkably innovative approach to working with Skills, the centerpiece of which being a technique that leverages hooks to ensure that Claude intelligently selects and activates the appropriate Skill given the current context. Well-documented and adaptable to different projects and workflows.
* Claude Code PMbyRan Aroussi- Really comprehensive and feature-packed project-management workflow for Claude Code. Numerous specialized agents, slash-commands, and strong documentation.
* Claude Code Repos IndexbyDaniel Rosehill- This is either the work of a prolific genius, or a very clever bot (or both), although it hardly matters because the quality is so good - an index of 75+ Claude Code repositories published by the author - and I'm not talking about slop. CMS, system design, deep research, IoT, agentic workflows, server management, personal health... If you spot the lie, let me know, otherwise please check these out.
* Claude Code System PromptsbyPiebald AI- All parts of Claude Code's system prompt, including builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact, Bash cmd, security review, agent creation, etc.). Updated for each Claude Code version.
* Claude Code Tipsbyykdojo- A nice variety of 35+ brief but information-dense Claude Code tips covering voice input, system prompt patching, container workflows for risky tasks, conversation cloning(!), multi-model orchestration with Gemini CLI, and plenty more. Nice demos, working scripts, a plugin, I'd say this probably has a little something for everyone.
* Claude Code Ultimate GuidebyFlorian BRUNIAUX- A tremendous feat of documentation, this guide covers Claude Code from beginner to power user, with production-ready templates for Claude Code features, guides on agentic workflows, and a lot of great learning materials, including quizzes and a handy "cheatsheet". Whether it's the "ultimate" guide to Claude Code will be up to the reader, but a valuable resource nonetheless (as with all documentation sites, make sure it's up to date before you bet the farm).
* Claude CodeProbyMax Ritter- Professional development environment for Claude Code with spec-driven workflow, TDD enforcement, cross-session memory, semantic search, quality hooks, and modular rules integration. A bit "heavyweight" but feature-packed and has wide coverage.
* claude-code-docsbyConstantin Shafranski- A mirror of the Anthropic© PBC documentation site for Claude/Code, but with bonus features like full-text search and query-time updates - a nice companion toclaude-code-docsfor up-to-the-minute, fully-indexed information so that Claude Code can read about itself.
* ClaudoPro Directorybyghost- Well-crafted, wide selection of Claude Code hooks, slash commands, subagent files, and more, covering a range of specialized tasks and workflows. Better resources than your average "Claude-template-for-everything" site.
* Context Primingbydisler- Provides a systematic approach to priming Claude Code with comprehensive project context through specialized commands for different project scenarios and development contexts.
* Design Review WorkflowbyPatrick Ellis- A tailored workflow for enabling automated UI/UX design review, including specialized sub agents, slash commands,CLAUDE.mdexcerpts, and more. Covers a broad range of criteria from responsive design to accessibility.
* Laravel TALL Stack AI Development Starter Kitbytott- Transform your Laravel TALL (Tailwind, AlpineJS, Laravel, Livewire) stack development with comprehensive Claude Code configurations that provide intelligent assistance, systematic workflows, and domain expert consultation.
* Learn Claude CodebyshareAI-Lab- A really interesting analysis of how coding agents like Claude Code are designed. It attempts to break an agent down into its fundamental parts and reconstruct it with minimal code. Great learning resource. Final product is a rudimentary agent with skills, sub-agents, and a todo-list in roughly a few hundred lines of Python.
* learn-faster-kitbyHugo Lau- A creative educational framework for Claude Code, inspired by the "FASTER" approach to self-teaching. Ships with a variety of agents, slash commands, and tools that enable Claude Code to help you progress at your own pace, employing well-established pedagogical techniques like active learning and spaced repetition.
* n8n_agentbykingler- Amazing comprehensive set of comments for code analysis, QA, design, documentation, project structure, project management, optimization, and many more.
* Project Bootstrapping and Task Managementbysteadycursor- Provides a structured set of commands for bootstrapping and managing a new project, including meta-commands for creating and editing custom slash-commands.
* Project Management, Implementation, Planning, and Releasebyscopecraft- Really comprehensive set of commands for all aspects of SDLC.
* Project Workflow Systembyharperreed- A set of commands that provide a comprehensive workflow system for managing projects, including task management, code review, and deployment processes.
* RIPER WorkflowbyTony Narlock- Structured development workflow enforcing separation between Research, Innovate, Plan, Execute, and Review phases. Features consolidated subagents for context-efficiency, branch-aware memory bank, and strict mode enforcement for guided development.
* Shipping Real Code w/ ClaudebyDiwank- A detailed blog post explaining the author's process for shipping a product with Claude Code, including CLAUDE.md files and other interesting resources.
* SimonebyHelmi- A broader project management workflow for Claude Code that encompasses not just a set of commands, but a system of documents, guidelines, and processes to facilitate project planning and execution.

### Ralph Wiggum

* awesome-ralphbyMartin Joly- A curated list of resources about Ralph, the AI coding technique that runs AI coding agents in automated loops until specifications are fulfilled.
* Ralph for Claude CodebyFrank Bria- An autonomous AI development framework that enables Claude Code to work iteratively on projects until completion. Features intelligent exit detection, rate limiting, circuit breaker patterns, and comprehensive safety guardrails to prevent infinite loops and API overuse. Built with Bash, integrated with tmux for live monitoring, and includes 75+ comprehensive tests.
* Ralph Wiggum MarketerbyMuratcan Koylan- A Claude Code plugin that provides an autonomous AI copywriter, integrating the Ralph loop with customized knowledge bases for market research agents. The agents do the research, Ralph writes the copy, you stay in bed. Whether or not you practice Ralph-Driven Development (RDD), I think these projects are interesting and creative explorations of general agentic patterns.
* ralph-orchestratorbymikeyobrien- Ralph Orchestrator implements the simple but effective "Ralph Wiggum" technique for autonomous task completion, continuously running an AI agent against a prompt file until the task is marked as complete or limits are reached. This implementation provides a robust, well-tested, and feature-complete orchestration system for AI-driven development. Also cited in the Anthropic Ralph plugin documentation.
* ralph-wiggum-bddbymarcindulak- A standalone Bash script for Behavior-Driven Development with Ralph Wiggum Loop. In principle, while running unattended, the script can keep code and requirements in sync, but in practice it still requires interactive human supervision, so it supports both modes. The script is standalone and can be modified and committed into your project.
* The Ralph PlaybookbyClayton Farr- A remarkably detailed and comprehensive guide to the Ralph Wiggum technique, featuring well-written theoretical commentary paired with practical guidelines and advice.

## Tooling 🧰

Tooling denotes applications that are built on top of Claude Code and consist of more components than slash-commands andCLAUDE.mdfiles

### General

* cc-sessionsbytoastdev- An opinionated approach to productive development with Claude Code.
* cc-toolsbyJosh Symonds- High-performance Go implementation of Claude Code hooks and utilities. Provides smart linting, testing, and statusline generation with minimal overhead.
* ccexpbynyatinte- Interactive CLI tool for discovering and managing Claude Code configuration files and slash commands with a beautiful terminal UI.
* cchistorybyeckardt- Like the shell history command but for your Claude Code sessions. Easily list all Bash or "Bash-mode" (!) commands Claude Code ran in a session for reference.
* cclogviewerbyBrad S.- A humble but handy utility for viewing Claude Code.jsonlconversation files in a pretty HTML UI.
* Claude Code TemplatesbyDaniel Avila- Incredibly awesome collection of resources from every category in this list, presented with a neatly polished UI, great features like usage dashboard, analytics, and everything from slash commands to hooks to agents. An awesome companion for this awesome list.
* Claude ComposerbyMike Bannister- A tool that adds small enhancements to Claude Code.
* Claude HubbyClaude Did This- A webhook service that connects Claude Code to GitHub repositories, enabling AI-powered code assistance directly through pull requests and issues. This integration allows Claude to analyze repositories, answer technical questions, and help developers understand and improve their codebase through simple @mentions.
* Claude Session RestorebyZENG3LD- Efficiently restore context from previous Claude Code sessions by analyzing session files and git history. Features multi-factor data collection across numerous Claude Code capacities with time-based filtering. Uses tail-based parsing for efficient handling of large session files up to 2GB. Includes both a CLI tool for manual analysis and a Claude Code skill for automatic session restoration.
* claude-code-toolsbyPrasad Chalasani- Well-crafted toolset for session continuity, featuring skills/commands to avoid compaction and recover context across sessions with cross-agent handoff between Claude Code and Codex CLI. Includes a fast Rust/Tantivy-powered full-text session search (TUI for humans, skill/CLI for agents), tmux-cli skill + command for interacting with scripts and CLI agents, and safety hooks to block dangerous commands.
* claude-starter-kitbyserpro69- This is a starter template repository designed to provide a complete development environment for Claude-Code with pre-configured MCP servers and tools for AI-powered development workflows. The repository is intentionally minimal, containing only configuration templates for three primary systems: Claude Code, Serena, and Task Master.
* claudekitbyCarl Rannaberg- Impressive CLI toolkit providing auto-save checkpointing, code quality hooks, specification generation and execution, and 20+ specialized subagents including oracle (gpt-5), code-reviewer (6-aspect deep analysis), ai-sdk-expert (Vercel AI SDK), typescript-expert and many more for Claude Code workflows.
* Container Usebydagger- Development environments for coding agents. Enable multiple agents to work safely and independently with your preferred stack.
* ContextKitbyCihat Gündüz- A systematic development framework that transforms Claude Code into a proactive development partner. Features 4-phase planning methodology, specialized quality agents, and structured workflows that help AI produce production-ready code on first try.
* recallbyzippoxer- Full-text search your Claude Code sessions. Runrecallin terminal, type to search, Enter to resume. Alternative toclaude --resume.
* Rulesyncbydyoshikawa- A Node.js CLI tool that automatically generates configs (rules, ignore files, MCP servers, commands, and subagents) for various AI coding agents. Rulesync can convert configs between Claude Code and other AI agents in both directions.
* run-claude-dockerbyJonas- A self-contained Docker runner that forwards your current workspace into a safe(r) isolated docker container, where you still have access to your Claude Code settings, authentication, ssh agent, pgp, optionally aws keys etc.
* stt-mcp-server-linuxbymarcindulak- A push-to-talk speech transcription setup for Linux using a Python MCP server. Runs locally in Docker with no external API calls. Your speech is recorded, transcribed into text, and then sent to Claude running in a Tmux session.
* SuperClaudebySuperClaude-Org- A versatile configuration framework that enhances Claude Code with specialized commands, cognitive personas, and development methodologies, such as "Introspection" and "Orchestration".
* tweakccbyPiebald-AI- Command-line tool to customize your Claude Code styling.
* Vibe-LogbyVibe-Log- Analyzes your Claude Code prompts locally (using CC), provides intelligent session analysis and actionable strategic guidance - works in the statusline and produces very pretty HTML reports as well. Easy to install and remove.
* viwo-clibyHal Shin- Run Claude Code in a Docker container with git worktrees as volume mounts to enable safer usage of--dangerously-skip-permissionsfor frictionless one-shotting prompts. Allows users to spin up multiple instances of Claude Code in the background easily with reduced permission fatigue.
* VoiceMode MCPbyMike Bailey- VoiceMode MCP brings natural conversations to Claude Code. It supports any OpenAI API compatible voice services and installs free and open source voice services (Whisper.cpp and Kokoro-FastAPI).

### IDE Integrations

* Claude Code Chatbyandrepimenta- An elegant and user-friendly Claude Code chat interface for VS Code.
* claude-code-ide.elbymanzaltu- claude-code-ide.el integrates Claude Code with Emacs, like Anthropic’s VS Code/IntelliJ extensions. It shows ediff-based code suggestions, pulls LSP/flymake/flycheck diagnostics, and tracks buffer context. It adds an extensible MCP tool support for symbol refs/defs, project metadata, and tree-sitter AST queries.
* claude-code.elbystevemolitor- An Emacs interface for Claude Code CLI.
* claude-code.nvimbygreggh- A seamless integration between Claude Code AI assistant and Neovim.
* Claudix - Claude Code for VSCodebyHaleclipse- A VSCode extension that brings Claude Code directly into your editor with interactive chat interface, session management, intelligent file operations, terminal execution, and real-time streaming responses. Built with Vue 3, TypeScript.

### Usage Monitors

* CC Usagebyryoppippi- Handy CLI tool for managing and analyzing Claude Code usage, based on analyzing local Claude Code logs. Presents a nice dashboard regarding cost information, token consumption, etc.
* ccflarebysnipeship- Claude Code usage dashboard with a web-UI that would put Tableau to shame. Thoroughly comprehensive metrics, frictionless setup, detailed logging, really really nice UI.
* ccflare ->better-ccflarebytombii- A well-maintained and feature-enhanced fork of the gloriousccflareusage dashboard by @snipeship (which at the time of writing has not had an update in a few months).better-ccflarebuilds on this foundation with some performance enhancements, extended provider support, bug fixes, Docker deployment, and more.
* Claude Code Usage MonitorbyMaciek-roboblog- A real-time terminal-based tool for monitoring Claude Code token usage. It shows live token consumption, burn rate, and predictions for token depletion. Features include visual progress bars, session-aware analytics, and support for multiple subscription plans.
* ClaudexbyKunwar Shah- Claudex - A web-based browser for exploring your Claude Code conversation history across projects. Indexes your codebase for full-text search. Nice, easy-to-navigate UI. Simple dashboard interface for high-level analytics, and multiple export options as well. (And completely local w/ no telemetry!).
* viberankbynikshepsvn- A community-driven leaderboard tool that enables developers to visualize, track, and compete based on their Claude Code usage statistics. It features robust data analytics, GitHub OAuth, data validation, and user-friendly CLI/web submission methods.

### Orchestrators

* Auto-ClaudebyAndyMik90- Autonomous multi-agent coding framework for Claude Code (Claude Agent SDK) that integrates the full SDLC - "plans, builds, and validates software for you". Features a slick kanban-style UI and a well-designed but not over-engineered agent orchestration system.
* Claude Code Flowbyruvnet- This mode serves as a code-first orchestration layer, enabling Claude to write, edit, test, and optimize code autonomously across recursive agent cycles.
* Claude Squadbysmtg-ai- Claude Squad is a terminal app that manages multiple Claude Code, Codex (and other local agents including Aider) in separate workspaces, allowing you to work on multiple tasks simultaneously.
* Claude Swarmbyparruda- Launch Claude Code session that is connected to a swarm of Claude Code Agents.
* Claude Task Masterbyeyaltoledano- A task management system for AI-driven development with Claude, designed to work seamlessly with Cursor AI.
* Claude Task Runnerbygrahama1970- A specialized tool to manage context isolation and focused task execution with Claude Code, solving the critical challenge of context length limitations and task focus when working with Claude on complex, multi-step projects.
* Happy CoderbyGrocerPublishAgent- Spawn and control multiple Claude Codes in parallel from your phone or desktop. Happy Coder runs Claude Code on your hardware, sends push notifications when Claude needs more input or permission, and costs nothing.
* sudocodebyssh-randy- Lightweight agent orchestration dev tool that lives in your repo. Integrates with various specification frameworks. It's giving Jira.
* The Agentic StartupbyRudolf Schmidt- Yet Another Claude Orchestrator - a collection of agents, commands, etc., for shipping production code - but I like this because it's comprehensive, well-written, and one of the few resources that actually uses Output Styles! +10 points!
* TSK - AI Agent Task Manager and Sandboxbydtormoen- A Rust CLI tool that lets you delegate development tasks to AI agents running in sandboxed Docker environments. Multiple agents work in parallel, returning git branches for human review.

### Config Managers

* claude-rules-doctorbynulone- CLI that detects dead.claude/rules/files by checking ifpaths:globs actually match files in your repo. Catches silent rule failures where renamed directories or typos in glob patterns cause rules to never apply. Features CI mode (exit 1 on dead rules), JSON output, and verbose mode showing matched files.
* ClaudeCTXbyJohn Fox- claudectx lets you switch your entire Claude Code configuration with a single command.

## Status Lines 📊

Status lines - Configurations and customizations for Claude Code's status bar functionality

### General

* CCometixLine - Claude Code StatuslinebyHaleclipse- A high-performance Claude Code statusline tool written in Rust with Git integration, usage tracking, interactive TUI configuration, and Claude Code enhancement utilities.
* ccstatuslinebysirmalloc- A highly customizable status line formatter for Claude Code CLI that displays model info, git branch, token usage, and other metrics in your terminal.
* claude-code-statuslinebyrz1989s- Enhanced 4-line statusline for Claude Code with themes, cost tracking, and MCP server monitoring.
* claude-powerlinebyOwloops- A vim-style powerline statusline for Claude Code with real-time usage tracking, git integration, custom themes, and more.
* claudia-statuslinebyHagan Franks- High-performance Rust-based statusline for Claude Code with persistent stats tracking, progress bars, and optional cloud sync. Features SQLite-first persistence, git integration, context progress bars, burn rate calculation, XDG-compliant with theme support (dark/light, NO_COLOR).

## Hooks 🪝

Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

### General

* BritfixbyTalieisin- Claude outputs American spellings by default, which can have an impact on: professional credibility, compliance, documentation, and more. Britfix converts to British English, with a Claude Code hook for automatic conversion as files are written. Context-aware: handles code files intelligently by only converting comments and docstrings, never identifiers or string literals.
* CC Notifybydazuiba- CCNotify provides desktop notifications for Claude Code, alerting you to input needs or task completion, with one-click jumps back to VS Code and task duration display.
* cchooksbyGowayLee- A lightweight Python SDK with a clean API and good documentation; simplifies the process of writing hooks and integrating them into your codebase, providing a nice abstraction over the JSON configuration files.
* Claude Code Hook Comms (HCOM)byaannoo- Lightweight CLI tool for real-time communication between Claude Code sub agents using hooks. Enables multi-agent collaboration with @-mention targeting, live dashboard monitoring, and zero-dependency implementation. [NOTE: At the time of posting, this resource is a little unstable - I'm sharing it anyway, because I think it's incredibly promising and creative. I hope by the time you read this, it is production-ready.].
* claude-code-hooks-sdkbybeyondcode- A Laravel-inspired PHP SDK for building Claude Code hook responses with a clean, fluent API. This SDK makes it easy to create structured JSON responses for Claude Code hooks using an expressive, chainable interface.
* claude-hooksbyJohn Lindquist- A TypeScript-based system for configuring and customizing Claude Code hooks with a powerful and flexible interface.
* ClaudiobyChristopher Toth- A no-frills little library that adds delightful OS-native sounds to Claude Code via simple hooks. It really sparks joy.
* DippybyLily Dayton- Auto-approve safe bash commands using AST-based parsing, while prompting for destructive operations. Solves permission fatigue without disabling safety. Supports Claude Code, Gemini CLI, and Cursor.
* parrybyDmytro Onypko- Prompt injection scanner for Claude Code hooks. Scans tool inputs and outputs for injection attacks, secrets, and data exfiltration attempts. [NOTE: Early development phase but worth a look.].
* TDD GuardbyNizar Selander- A hooks-driven system that monitors file operations in real-time and blocks changes that violate TDD principles.
* TypeScript Quality Hooksbybartolli- Quality check hook for Node.js TypeScript projects with TypeScript compilation. ESLint auto-fixing, and Prettier formatting. Uses SHA256 config caching for < 5ms validation performance during real-time editing.

## Slash-Commands 🔪

"Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

### General

* /create-hookbyOmri Lavi- Slash command for hook creation - intelligently prompts you through the creation process with smart suggestions based on your project setup (TS, Prettier, ESLint...).
* /linux-desktop-slash-commandsbyDaniel Rosehill- A library of slash commands intended specifically to facilitate common and advanced operations on Linux desktop environments (although many would also be useful on Linux servers). Command groups include hardware benchmarking, filesystem organisation, and security posture validation.

### Version Control & Git

* /analyze-issuebyjerseycheese- Fetches GitHub issue details to create comprehensive implementation specifications, analyzing requirements and planning structured approach with clear implementation steps.
* /commitbyevmts- Creates git commits using conventional commit format with appropriate emojis, following project standards and creating descriptive messages that explain the purpose of changes.
* /commit-fastbysteadycursor- Automates git commit process by selecting the first suggested message, generating structured commits with consistent formatting while skipping manual confirmation and removing Claude co-Contributorship footer.
* /create-prbytoyamarinyon- Streamlines pull request creation by handling the entire workflow: creating a new branch, committing changes, formatting modified files with Biome, and submitting the PR.
* /create-pull-requestbyliam-hq- Provides comprehensive PR creation guidance with GitHub CLI, enforcing title conventions, following template structure, and offering concrete command examples with best practices.
* /create-worktreesbyevmts- Creates git worktrees for all open PRs or specific branches, handling branches with slashes, cleaning up stale worktrees, and supporting custom branch creation for development.
* /fix-github-issuebyjeremymailen- Analyzes and fixes GitHub issues using a structured approach with GitHub CLI for issue details, implementing necessary code changes, running tests, and creating proper commit messages.
* /fix-issuebymetabase- Addresses GitHub issues by taking issue number as parameter, analyzing context, implementing solution, and testing/validating the fix for proper integration.
* /fix-prbymetabase- Fetches and fixes unresolved PR comments by automatically retrieving feedback, addressing reviewer concerns, making targeted code improvements, and streamlining the review process.
* /huskybyevmts- Sets up and manages Husky Git hooks by configuring pre-commit hooks, establishing commit message standards, integrating with linting tools, and ensuring code quality on commits.
* /update-branch-namebygiselles-ai- Updates branch names with proper prefixes and formats, enforcing naming conventions, supporting semantic prefixes, and managing remote branch updates.

### Code Analysis & Testing

* /checkbyrygwdn- Performs comprehensive code quality and security checks, featuring static analysis integration, security vulnerability scanning, code style enforcement, and detailed reporting.
* /code_analysisbykingler- Provides a menu of advanced code analysis commands for deep inspection, including knowledge graph generation, optimization suggestions, and quality evaluation.
* /optimizebyto4iki- Analyzes code performance to identify bottlenecks, proposing concrete optimizations with implementation guidance for improved application performance.
* /repro-issuebyrzykov- Creates reproducible test cases for GitHub issues, ensuring tests fail reliably and documenting clear reproduction steps for developers.
* /tddbyzscott- Guides development using Test-Driven Development principles, enforcing Red-Green-Refactor discipline, integrating with git workflow, and managing PR creation.
* /tdd-implementbyjerseycheese- Implements Test-Driven Development by analyzing feature requirements, creating tests first (red), implementing minimal passing code (green), and refactoring while maintaining tests.

### Context Loading & Priming

* /context-primebyelizaOS- Primes Claude with comprehensive project understanding by loading repository structure, setting development context, establishing project goals, and defining collaboration parameters.
* /initrefbyokuvshynov- Initializes reference documentation structure with standard doc templates, API reference setup, documentation conventions, and placeholder content generation.
* /load-llms-txtbyethpandaops- Loads LLM configuration files to context, importing specific terminology, model configurations, and establishing baseline terminology for AI discussions.
* /load_coo_contextbyMjvolk3- References specific files for sparse matrix operations, explains transform usage, compares with previous approaches, and sets data formatting context for development.
* /load_dango_pipelinebyMjvolk3- Sets context for model training by referencing pipeline files, establishing working context, and preparing for pipeline work with relevant documentation.
* /primebyyzyydev- Sets up initial project context by viewing directory structure and reading key files, creating standardized context with directory visualization and key documentation focus.
* /rsibyddisisto- Reads all commands and key project files to optimize AI-assisted development by streamlining the process, loading command context, and setting up for better development workflow.

### Documentation & Changelogs

* /add-to-changelogbyberrydev-ai- Adds new entries to changelog files while maintaining format consistency, properly documenting changes, and following established project standards for version tracking.
* /create-docsbyjerseycheese- Analyzes code structure and purpose to create comprehensive documentation detailing inputs/outputs, behavior, user interaction flows, and edge cases with error handling.
* /docsbyslunsford- Generates comprehensive documentation that follows project structure, documenting APIs and usage patterns with consistent formatting for better user understanding.
* /explain-issue-fixbyhackdays-io- Documents solution approaches for GitHub issues, explaining technical decisions, detailing challenges overcome, and providing implementation context for better understanding.
* /update-docsbyConsiliency- Reviews current documentation status, updates implementation progress, reviews phase documents, and maintains documentation consistency across the project.

### CI / Deployment

* /releasebykelp- Manages software releases by updating changelogs, reviewing README changes, evaluating version increments, and documenting release changes for better version tracking.
* /run-cibyhackdays-io- Activates virtual environments, runs CI-compatible check scripts, iteratively fixes errors, and ensures all tests pass before completion.

### Project & Task Management

* /create-commandbyscopecraft- Guides Claude through creating new custom commands with proper structure by analyzing requirements, templating commands by category, enforcing command standards, and creating supporting documentation.
* /create-planbytaddyorg- Generates comprehensive product requirement documents outlining detailed specifications, requirements, and features following standardized document structure and format.(Removed from origin)
* /create-prpbyWirasm- Creates product requirement plans by reading PRP methodology, following template structure, creating comprehensive requirements, and structuring product definitions for development.
* /do-issuebyjerseycheese- Implements GitHub issues with manual review points, following a structured approach with issue number parameter and offering alternative automated mode for efficiency.
* /prd-generatorbyDenis Redozubov- A Claude Code plugin that generates comprehensive Product Requirements Documents (PRDs) from conversation context. Invoke/create-prdafter discussing requirements and it produces a complete PRD with all standard sections including Executive Summary, User Stories, MVP Scope, Architecture, Success Criteria, and Implementation Phases.
* /project_hello_w_namebydisler- Creates customizable greeting components with name input, demonstrating argument passing, component reusability, state management, and user input handling.
* /todobychrisleyva- A convenient command to quickly manage project todo items without leaving the Claude Code interface, featuring due dates, sorting, task prioritization, and comprehensive todo list management.

### Miscellaneous

* /fixing_go_in_graphbyMjvolk3- Focuses on Gene Ontology annotation integration in graph databases, handling multiple data sources, addressing graph representation issues, and ensuring correct data incorporation.
* /mermaidbyGaloyMoney- Generates Mermaid diagrams from SQL schema files, creating entity relationship diagrams with table properties, validating diagram compilation, and ensuring complete entity coverage.
* /review_dcell_modelbyMjvolk3- Reviews old Dcell implementation files, comparing with newer Dango model, noting changes over time, and analyzing refactoring approaches for better code organization.
* /use-stepperbyzuplo- Reformats documentation to use React Stepper component, transforming heading formats, applying proper indentation, and maintaining markdown compatibility with admonition formatting.

## CLAUDE.md Files 📂

CLAUDE.mdfiles are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards

### Language-Specific

* AI IntelliJ Pluginbydidalgolab- Provides comprehensive Gradle commands for IntelliJ plugin development with platform-specific coding patterns, detailed package structure guidelines, and clear internationalization standards.
* AWS MCP Serverbyalexei-led- Features multiple Python environment setup options with detailed code style guidelines, comprehensive error handling recommendations, and security considerations for AWS CLI interactions.
* DroidconKotlinbytouchlab- Delivers comprehensive Gradle commands for cross-platform Kotlin Multiplatform development with clear module structure and practical guidance for dependency injection.
* EDSLbyexpectedparrot- Offers detailed build and test commands with strict code style enforcement, comprehensive testing requirements, and standardized development workflow using Black and mypy.(Removed from origin)
* Gisellebygiselles-ai- Provides detailed build and test commands using pnpm and Vitest with strict code formatting requirements and comprehensive naming conventions for code consistency.
* HASHbyhashintel- Features comprehensive repository structure breakdown with strong emphasis on coding standards, detailed Rust documentation guidelines, and systematic PR review process.
* Inklinebyinkline- Structures development workflow using pnpm with emphasis on TypeScript and Vue 3 Composition API, detailed component creation process, and comprehensive testing recommendations.
* JSBeebbymattgodbolt- Provides development guide for JavaScript BBC Micro emulator with build and testing instructions, architecture documentation, and debugging workflows.
* Lamoom PythonbyLamoomAI- Serves as reference for production prompt engineering library with load balancing of AI Models, API documentation, and usage patterns with examples.
* LangGraphJSbylangchain-ai- Offers comprehensive build and test commands with detailed TypeScript style guidelines, layered library architecture, and monorepo structure using yarn workspaces.
* Metabasebymetabase- Details workflow for REPL-driven development in Clojure/ClojureScript with emphasis on incremental development, testing, and step-by-step approach for feature implementation.
* SG Cars Trends Backendbysgcarstrends- Provides comprehensive structure for TypeScript monorepo projects with detailed commands for development, testing, deployment, and AWS/Cloudflare integration.
* SPybyspylang- Enforces strict coding conventions with comprehensive testing guidelines, multiple code compilation options, and backend-specific test decorators for targeted filtering.
* TPLbyKarpelesLab- Details Go project conventions with comprehensive error handling recommendations, table-driven testing approach guidelines, and modernization suggestions for latest Go features.

### Domain-Specific

* Course Builderbybadass-courses- Enables real-time multiplayer capabilities for collaborative course creation with diverse tech stack integration and monorepo architecture using Turborepo.
* Cursor Toolsbyeastlondoner- Creates a versatile AI command interface supporting multiple providers and models with flexible command options and browser automation through "Stagehand" feature.
* Guitarbysoramimi- Serves as development guide for Guitar Git GUI Client with build commands for various platforms, code style guidelines for contributing, and project structure explanation.
* Network ChroniclesbyFimeg- Presents detailed implementation plan for AI-driven game characters with technical specifications for LLM integration, character guidelines, and service discovery mechanics.
* Pareto MacbyParetoSecurity- Serves as development guide for Mac security audit tool with build instructions, contribution guidelines, testing procedures, and workflow documentation.
* pre-commit-hooksbyaRustyDev- This repository is about pre-commit-hooks in general, but theCLAUDE.mdand related.claude/documentation is exemplary. Thorough but not verbose. Unlike a lot ofCLAUDE.mdfiles, it doesn't primarily consist in shouting at Claude in all-caps. Great learning resource. Also, hooks.
* SteadyStartbysteadycursor- Clear and direct instructives about style, permissions, Claude's "role", communications, and documentation of Claude Code sessions for other team members to stay abreast.

### Project Scaffolding & MCP

* Basic Memorybybasicmachines-co- Presents an innovative AI-human collaboration framework with Model Context Protocol for bidirectional LLM-markdown communication and flexible knowledge structure for complex projects.
* claude-code-mcp-enhancedbygrahama1970- Provides detailed and emphatic instructions for Claude to follow as a coding agent, with testing guidance, code examples, and compliance checks.

## Alternative Clients 📱

Alternative Clients are alternative UIs and front-ends for interacting with Claude Code, either on mobile or on the desktop.

### General

* ClaudablebyEthan Park- Claudable is an open-source web builder that leverages local CLI agents, such as Claude Code and Cursor Agent, to build and deploy products effortlessly.
* claude-espbyphiat- Go-based TUI that streams Claude Code's hidden output (thinking, tool calls, subagents) to a separate terminal. Watch multiple sessions simultaneously, filter by content type, and track background tasks. Ideal for debugging or understanding what Claude is doing under the hood without interrupting your main session.
* claude-tmuxbyNiels Groeneveld- Manage Claude Code within tmux. A tmux popup of all your Claude Code instances, enabling quick switching, status monitoring, session lifecycle management, with git worktree and pull request support.
* crystalbystravu- A full-fledged desktop application for orchestrating, monitoring, and interacting with Claude Code agents.
* OmnarabyIshaan Sehgal- A command center for AI agents that syncs Claude Code sessions across terminal, web, and mobile. Allows for remote monitoring, human-in-the-loop interaction, and team collaboration.

## Official Documentation 🏛️

Links to some of Anthropic's terrific documentation and resources regarding Claude Code

### General

* Anthropic DocumentationbyAnthropic- The official documentation for Claude Code, including installation instructions, usage guidelines, API references, tutorials, examples, loads of information that I won't list individually. Like Claude Code, the documentation is frequently updated.
* Anthropic QuickstartsbyAnthropic- Offers comprehensive development guides for three distinct AI-powered demo projects with standardized workflows, strict code style guidelines, and containerization instructions.
* Claude Code GitHub ActionsbyAnthropic- Official GitHub Actions integration for Claude Code with examples and documentation for automating AI-powered workflows in CI/CD pipelines.

## Contributing🔝

### Recommend a new resource here!

Recommending a resource for the list is very simple, and the automated system handles everything for you. Please do not open a PR to submit a recommendation - the only person who is allowed to submit PRs to this repo is Claude.

Make sure that you have read the CONTRIBUTING.md document and CODE_OF_CONDUCT.md before you submit a recommendation.

For suggestions about the repository itself, pleaseopen a repository enhancement issue.

This project is released with a Code of Conduct. By participating, you agree to abide by its terms. And although I take strong measures to uphold the quality and safety of this list, I take no responsibility or liability for anything that might happen as a result of these third-party resources.

## Growing thanks to you

## License

This list is licensed underCreative Commons CC BY-NC-ND 4.0- this means you are welcome to fork, clone, copy and redistribute the list, provided you include appropriate attribution; however you are not permitted to distribute any modified versions or to use it for any commercial purposes. This is to prevent disregard for the licenses of the authors whose resources are listed here. Please note that all resources included in this list have their own license terms.

## About

A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

### Topics

 awesome

 awesome-list

 awesome-lists

 awesome-resources

 claude

 coding-assistant

 llm

 ai-workflows

 anthropic

 anthropic-claude

 coding-agents

 ai-workflow-optimization

 coding-assistants

 agent-skills

 claude-code

 agentic-code

 coding-agent

 agentic-coding

### Resources

 Readme

 

### License

 View license
 

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

30.4k

 stars
 

### Watchers

224

 watching
 

### Forks

2.1k

 forks
 

 Report repository

 

## Contributors18

+ 4 contributors

## Languages

* Python98.1%
* Makefile1.9%