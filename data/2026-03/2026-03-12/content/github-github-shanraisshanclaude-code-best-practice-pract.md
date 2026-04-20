---
title: 'GitHub - shanraisshan/claude-code-best-practice: practice made claude perfect · GitHub'
url: https://github.com/shanraisshan/claude-code-best-practice
site_name: github
content_file: github-github-shanraisshanclaude-code-best-practice-pract
fetched_at: '2026-03-12T11:15:48.667798'
original_url: https://github.com/shanraisshan/claude-code-best-practice
author: shanraisshan
description: practice made claude perfect. Contribute to shanraisshan/claude-code-best-practice development by creating an account on GitHub.
---

shanraisshan



/

claude-code-best-practice

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.3k
* Star13.5k




 
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

164 Commits
164 Commits
!
!
 
 
.claude
.claude
 
 
.vscode
.vscode
 
 
best-practice
best-practice
 
 
changelog/
best-practice
changelog/
best-practice
 
 
development-workflows
development-workflows
 
 
implementation
implementation
 
 
orchestration-workflow
orchestration-workflow
 
 
presentation
presentation
 
 
reports
reports
 
 
tips
tips
 
 
.gitignore
.gitignore
 
 
.mcp.json
.mcp.json
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# claude-code-best-practice

practice makes claude perfect



Click on this badge to show the latest best practiceClick on this badge to show implementation in this repoClick on this badge to see the Command → Agent → Skill orchestration workflow

Boris Cherny on X (tweet 1·tweet 2·tweet 3)

## CONCEPTS

Feature

Location

Description

Commands

.claude/commands/<name>.md


 Knowledge injected into existing context — simple user-invoked prompt templates for workflow orchestration

Sub-Agents

.claude/agents/<name>.md


 Autonomous actor in fresh isolated context — custom tools, permissions, model, memory, and persistent identity

Skills

.claude/skills/<name>/SKILL.md


 Knowledge injected into existing context — configurable, preloadable, auto-discoverable, with context forking and progressive disclosure ·
Official Skills

Workflows

.claude/commands/weather-orchestrator.md

Hooks

.claude/hooks/


 Deterministic scripts that run outside the agentic loop on specific events

MCP Servers

.claude/settings.json
,
.mcp.json


 Model Context Protocol connections to external tools, databases, and APIs

Plugins

distributable packages

Bundles of skills, subagents, hooks, and MCP servers ·
Marketplaces

Settings

.claude/settings.json


 Hierarchical configuration system ·
Permissions
 ·
Model Config
 ·
Output Styles
 ·
Sandboxing
 ·
Keybindings
 ·
Fast Mode

Status Line

.claude/settings.json


 Customizable status bar showing context usage, model, cost, and session info

Memory

CLAUDE.md
,
.claude/rules/
,
~/.claude/rules/
,
~/.claude/projects/<project>/memory/


 Persistent context via CLAUDE.md files and
@path
 imports ·
Auto Memory
 ·
Rules

Checkpointing

automatic (git-based)

Automatic tracking of file edits with rewind (
Esc Esc
 or
/rewind
) and targeted summarization

CLI Startup Flags

claude [flags]

 Command-line flags, subcommands, and environment variables for launching Claude Code ·
Interactive Mode

AI Terms

 Agentic Engineering · Context Engineering · Vibe Coding

Best Practices

Official best practices ·
Prompt Engineering
 ·
Extend Claude Code

### 🔥 Hot

Feature

Location

Description

/btw

/btw

 Side chain conversations while Claude is working

Code Review


GitHub App (managed)

 Multi-agent PR analysis that catches bugs, security vulnerabilities, and regressions ·
Blog

Scheduled Tasks

/loop
, cron tools


 Run prompts on a recurring schedule (up to 3 days), set one-time reminders, poll deployments and builds

Voice Mode


/voice

 speak to prompt - /voice to activate

Simplify & Batch

/simplify
,
/batch

 Built-in skills for code quality and bulk operations — simplify refactors for reuse and efficiency, batch runs commands across files

Agent Teams


built-in (env var)

 Multiple agents working in parallel on the same codebase with shared task coordination

Remote Control

/remote-control
,
/rc

Continue local sessions from any device — phone, tablet, or browser ·
Headless Mode

Git Worktrees

built-in

 Isolated git branches for parallel development — each agent gets its own working copy

Ralph Wiggum Loop

plugin


 Autonomous development loop for long-running tasks — iterates until completion

Seeorchestration-workflowfor implementation details ofCommand → Agent → Skillpattern.

claude
/weather-orchestrator

Component

Role

Example

Command

Entry point, user interaction

/weather-orchestrator

Agent

Fetches data with preloaded skill (agent skill)

weather-agent
 with
weather-fetcher

Skill

Creates output independently (skill)

weather-svg-creator

## DEVELOPMENT WORKFLOWS

### 🔥 Hot

* Cross-Model (Claude Code + Codex) Workflow
* RPI
* Ralph Wiggum Loop

### Others

* Github Speckit· ★ 74k
* obra/superpowers· ★ 72k
* OpenSpec OPSX· ★ 28k
* get-shit-done (GSD)· ★ 25k
* Brian Casel (Creator of Agent OS) - 2026 Workflow· ★ 4k -it's overkill in 2026
* Human Layer RPI - Research Plan Implement· ★ 1.5k
* Andrej Karpathy (Founding Member, OpenAI) Workflow
* Boris Cherny (Creator of Claude Code) - Feb 2026 Workflow
* Peter Steinberger (Creator of OpenClaw) Workflow

## TIPS AND TRICKS

■Planning (2)

* always start withplan mode. ask Claude to interview you;ask the user a question
* always make a phase-wise gated plan, with each phase having multiple tests (unit, automation, integration). usecross-modelto review your plan

■Workflows (12)

* CLAUDE.mdshould target under200 linesper file.60 lines in humanlayer(still not 100% guaranteed).
* usemultiple CLAUDE.mdfor monorepos — ancestor + descendant loading
* use.claude/rules/to split large instructions
* usecommandsfor your workflows instead ofsub-agents
* have feature specificsub-agents(extra context) withskills(progressive disclosure) instead of general qa, backend engineer.
* memory.md, constitution.md does not guarantee anything
* avoid agent dumb zone, do manual/compactat max 50%. Use/clearto reset context mid-session if switching to a new task
* vanilla cc is better than any workflows with smaller tasks
* useskills in subfoldersfor monorepos
* use/modelto select model and reasoning,/contextto see context usage,/usageto check plan limits,/extra-usageto configure overflow billing,/configto configure settings
* always usethinking modetrue (to see reasoning) andOutput StyleExplanatory (to see detailed output with ★ Insight boxes) in/configfor better understanding of Claude's decisions
* use ultrathink keyword in prompts forhigh effort reasoning
* /renameimportant sessions (e.g. [TODO - refactor task]) and/resumethem later
* useEsc Esc or /rewindto undo when Claude goes off-track instead of trying to fix it in the same context
* commit often — try to commit at least once per hour, as soon as task is completed, commit.

■Workflows Advanced (6)

* use ASCII diagrams a lot to understand your architecture
* agent teams with tmuxandgit worktreesfor parallel development
* use/loopfor recurring monitoring — poll deployments, babysit PRs, check builds (runs up to 3 days)
* useRalph Wiggum pluginfor long-running autonomous tasks
* /permissionswith wildcard syntax (Bash(npm run *), Edit(/docs/**)) instead of dangerously-skip-permissions
* /sandboxto reduce permission prompts with file and network isolation

■Debugging (5)

* make it a habit to take screenshots and share with Claude whenever you are stuck with any issue
* use mcp (Claude in Chrome,Playwright,Chrome DevTools) to let claude see chrome console logs on its own
* always ask claude to run the terminal (you want to see logs of) as a background task for better debugging
* /doctorto diagnose installation, authentication, and configuration issues
* error during compaction can be resolved by using/modelto select a 1M token model, then running/compact
* use across-modelfor QA — e.g.Codexfor plan and implementation review

■Utilities (5)

* iTerm/Ghostty/tmuxterminals instead of IDE (VS Code/Cursor)
* Wispr Flowfor voice prompting (10x productivity)
* claude-code-voice-hooksfor claude feedback
* status linefor context awareness and fast compacting
* exploresettings.jsonfeatures likePlans Directory,Spinner Verbsfor a personalized experience

■Daily (3)

* updateClaude Code daily and start your day by reading thechangelog
* followr/ClaudeAI,r/ClaudeCodeon Reddit
* followBoris,Thariq,Cat,Lydia,Noah,Claude,Alex Alberton X

* Always use plan mode, give Claude a way to verify, use /code-review | 27/Dec/25●Tweet
* Ask Claude to interview you using AskUserQuestion tool (Thariq) | 28/Dec/25●Tweet
* Boris setup - 5 tips | 03/Jan/26●Tweet
* 10 tips for using claude code by team itself | 01/Feb/26●Tweet
* 12 ways how people are customizing their claudes | 12/Feb/26●Tweet
* Git Worktrees - 5 ways how boris is using | 21 Feb 2026●Tweet
* Seeing like an Agent - lessons from building Claude Code (Thariq) | 28 Feb 2026●Tweet
* AskUserQuestion + ASCII Markdowns (Thariq) | 28 Feb 2026●Tweet
* /loop — schedule recurring tasks for up to 3 days | 07 Mar 2026●Tweet
* Code Review — why fresh context windows catch bugs the original agent missed | 10 Mar 2026●Tweet
* /btw — side chain conversations while Claude works (Thariq) | 10 Mar 2026●Tweet

## ☠️ STARTUPS / BUSINESSES

Claude

Replaced

Code Review

Greptile
,
CodeRabbit
,
Devin Review
,
OpenDiff
,
Cursor BugBot

Voice Mode

Wispr Flow
,
SuperWhisper

Remote Control

OpenClaw

Cowork

OpenAI Operator
,
AgentShadow

Tasks

Beads

Plan Mode

Agent OS

Skills / Plugins

YC AI wrapper startups (
reddit
)

If you have answers, do let me know atshanraisshan@gmail.com

Memory & Instructions (4)

1. What exactly should you put inside your CLAUDE.md — and what should you leave out?
2. If you already have a CLAUDE.md, is a separate constitution.md or rules.md actually needed?
3. How often should you update your CLAUDE.md, and how do you know when it's become stale?
4. Why does Claude still ignore CLAUDE.md instructions — even when they say MUST in all caps? (reddit)

Agents, Skills & Workflows (6)

1. When should you use a command vs an agent vs a skill — and when is vanilla Claude Code just better?
2. How often should you update your agents, commands, and workflows as models improve?
3. Does giving your subagent a detailed persona improve quality? What does a "perfect persona/prompt" for research/QA subagent look like?
4. Should you rely on Claude Code's built-in plan mode — or build your own planning command/agent that enforces your team's workflow?
5. If you have a personal skill (e.g., /implement with your coding style), how do you incorporate community skills (e.g., /simplify) without conflicts — and who wins when they disagree?
6. Are we there yet? Can we convert an existing codebase into specs, delete the code, and have AI regenerate the exact same code from those specs alone?

Specs & Documentation (3)

1. Should every feature in your repo have a spec as a markdown file?
2. How often do you need to update specs so they don't become obsolete when a new feature is implemented?
3. When implementing a new feature, how do you handle the ripple effect on specs for other features?

## REPORTS

Report

Description

Agent SDK vs CLI System Prompts

Why Claude CLI and Agent SDK outputs may differ—system prompt architecture and determinism

Browser Automation MCP Comparison

Comparison of Playwright, Chrome DevTools, and Claude in Chrome for automated testing

Global vs Project Settings

Which features are global-only (
~/.claude/
) vs dual-scope, including Tasks and Agent Teams

Skills Discovery in Monorepos

How skills are discovered and loaded in large monorepo projects

Agent Memory Frontmatter

Persistent memory scopes (
user
,
project
,
local
) for subagents — enabling agents to learn across sessions

Advanced Tool Use Patterns

Programmatic Tool Calling (PTC), Tool Search, and Tool Use Examples

Usage, Rate Limits & Extra Usage

Usage commands (
/usage
,
/extra-usage
,
/cost
), rate limits, and pay-as-you-go overflow billing

LLM Day-to-Day Degradation

Why LLM performance varies day-to-day — infrastructure bugs, MoE routing variance, and psychology

Agents vs Commands vs Skills

When to use each extension mechanism — comparison table, resolution order, and worked example

## About

practice made claude perfect

### Topics

 best-practices

 claude-ai

 vibe-coding

 claude-code

 agentic-engineering

### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

13.5k

 stars


### Watchers

148

 watching


### Forks

1.3k

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors4

* shanraisshanShayan Rais
* claudeClaude
* neutmuteneutmute
* shayangdShayan Rais

## Languages

* HTML88.8%
* Python11.2%
