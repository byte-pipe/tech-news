---
title: 'GitHub - rtk-ai/rtk: CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies · GitHub'
url: https://github.com/rtk-ai/rtk
site_name: github
content_file: github-github-rtk-airtk-cli-proxy-that-reduces-llm-token
fetched_at: '2026-04-23T11:59:16.246818'
original_url: https://github.com/rtk-ai/rtk
author: rtk-ai
description: CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies - rtk-ai/rtk
---

rtk-ai

 

/

rtk

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.9k
* Star33.1k

 
 
 
 
master
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

809 Commits
809 Commits
.claude
.claude
 
 
.github
.github
 
 
.rtk
.rtk
 
 
Formula
Formula
 
 
docs
docs
 
 
hooks
hooks
 
 
openclaw
openclaw
 
 
scripts
scripts
 
 
src
src
 
 
tests/
fixtures
tests/
fixtures
 
 
.gitignore
.gitignore
 
 
.release-please-manifest.json
.release-please-manifest.json
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
DISCLAIMER.md
DISCLAIMER.md
 
 
INSTALL.md
INSTALL.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README_es.md
README_es.md
 
 
README_fr.md
README_fr.md
 
 
README_ja.md
README_ja.md
 
 
README_ko.md
README_ko.md
 
 
README_zh.md
README_zh.md
 
 
SECURITY.md
SECURITY.md
 
 
build.rs
build.rs
 
 
install.sh
install.sh
 
 
release-please-config.json
release-please-config.json
 
 
View all files

## Repository files navigation

High-performance CLI proxy that reduces LLM token consumption by 60-90%

Website•Install•Troubleshooting•Architecture•Discord

English•Francais•中文•日本語•한국어•Espanol

rtk filters and compresses command outputs before they reach your LLM context. Single Rust binary, 100+ supported commands, <10ms overhead.

## Token Savings (30-min Claude Code Session)

Operation

Frequency

Standard

rtk

Savings

ls
 / 
tree

10x

2,000

400

-80%

cat
 / 
read

20x

40,000

12,000

-70%

grep
 / 
rg

8x

16,000

3,200

-80%

git status

10x

3,000

600

-80%

git diff

5x

10,000

2,500

-75%

git log

5x

2,500

500

-80%

git add/commit/push

8x

1,600

120

-92%

cargo test
 / 
npm test

5x

25,000

2,500

-90%

ruff check

3x

3,000

600

-80%

pytest

4x

8,000

800

-90%

go test

3x

6,000

600

-90%

docker ps

3x

900

180

-80%

Total

~118,000

~23,900

-80%

Estimates based on medium-sized TypeScript/Rust projects. Actual savings vary by project size.

## Installation

### Homebrew (recommended)

brew install rtk

### Quick Install (Linux/macOS)

curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh 
|
 sh

Installs to~/.local/bin. Add to PATH if needed:

echo
 
'
export PATH="$HOME/.local/bin:$PATH"
'
 
>>
 
~
/.bashrc 
#
 or ~/.zshrc

### Cargo

cargo install --git https://github.com/rtk-ai/rtk

### Pre-built Binaries

Download fromreleases:

* macOS:rtk-x86_64-apple-darwin.tar.gz/rtk-aarch64-apple-darwin.tar.gz
* Linux:rtk-x86_64-unknown-linux-musl.tar.gz/rtk-aarch64-unknown-linux-gnu.tar.gz
* Windows:rtk-x86_64-pc-windows-msvc.zip

Windows users: Extract the zip and placertk.exesomewhere in your PATH (e.g.C:\Users\<you>\.local\bin). Run RTK fromCommand Prompt,PowerShell, orWindows Terminal— do not double-click the.exe(it will flash and close). For the best experience, useWSLwhere the full hook system works natively. SeeWindows setupbelow for details.

### Verify Installation

rtk --version 
#
 Should show "rtk 0.28.2"

rtk gain 
#
 Should show token savings stats

Name collision warning: Another project named "rtk" (Rust Type Kit) exists on crates.io. Ifrtk gainfails, you have the wrong package. Usecargo install --gitabove instead.

## Quick Start

#
 1. Install for your AI tool

rtk init -g 
#
 Claude Code / Copilot (default)

rtk init -g --gemini 
#
 Gemini CLI

rtk init -g --codex 
#
 Codex (OpenAI)

rtk init -g --agent cursor 
#
 Cursor

rtk init --agent windsurf 
#
 Windsurf

rtk init --agent cline 
#
 Cline / Roo Code

rtk init --agent kilocode 
#
 Kilo Code

rtk init --agent antigravity 
#
 Google Antigravity

#
 2. Restart your AI tool, then test

git status 
#
 Automatically rewritten to rtk git status

The hook transparently rewrites Bash commands (e.g.,git status->rtk git status) before execution. Claude never sees the rewrite, it just gets compressed output.

Important:the hook only runs on Bash tool calls. Claude Code built-in tools likeRead,Grep, andGlobdo not pass through the Bash hook, so they are not auto-rewritten. To get RTK's compact output for those workflows, use shell commands (cat/head/tail,rg/grep,find) or callrtk read,rtk grep, orrtk finddirectly.

## How It Works

 Without rtk: With rtk:

 Claude --git status--> shell --> git Claude --git status--> RTK --> git
 ^ | ^ | |
 | ~2,000 tokens (raw) | | ~200 tokens | filter |
 +-----------------------------------+ +------- (filtered) ---+----------+

Four strategies applied per command type:

1. Smart Filtering- Removes noise (comments, whitespace, boilerplate)
2. Grouping- Aggregates similar items (files by directory, errors by type)
3. Truncation- Keeps relevant context, cuts redundancy
4. Deduplication- Collapses repeated log lines with counts

## Commands

### Files

rtk ls 
.
 
#
 Token-optimized directory tree

rtk 
read
 file.rs 
#
 Smart file reading

rtk 
read
 file.rs -l aggressive 
#
 Signatures only (strips bodies)

rtk smart file.rs 
#
 2-line heuristic code summary

rtk find 
"
*.rs
"
 
.
 
#
 Compact find results

rtk grep 
"
pattern
"
 
.
 
#
 Grouped search results

rtk diff file1 file2 
#
 Condensed diff

### Git

rtk git status 
#
 Compact status

rtk git log -n 10 
#
 One-line commits

rtk git diff 
#
 Condensed diff

rtk git add 
#
 -> "ok"

rtk git commit -m 
"
msg
"
 
#
 -> "ok abc1234"

rtk git push 
#
 -> "ok main"

rtk git pull 
#
 -> "ok 3 files +10 -2"

### GitHub CLI

rtk gh pr list 
#
 Compact PR listing

rtk gh pr view 42 
#
 PR details + checks

rtk gh issue list 
#
 Compact issue listing

rtk gh run list 
#
 Workflow run status

### Test Runners

rtk jest 
#
 Jest compact (failures only)

rtk vitest 
#
 Vitest compact (failures only)

rtk playwright 
test
 
#
 E2E results (failures only)

rtk pytest 
#
 Python tests (-90%)

rtk go 
test
 
#
 Go tests (NDJSON, -90%)

rtk cargo 
test
 
#
 Cargo tests (-90%)

rtk rake 
test
 
#
 Ruby minitest (-90%)

rtk rspec 
#
 RSpec tests (JSON, -60%+)

rtk err 
<
cmd
>
 
#
 Filter errors only from any command

rtk 
test
 
<
cmd
>
 
#
 Generic test wrapper - failures only (-90%)

### Build & Lint

rtk lint 
#
 ESLint grouped by rule/file

rtk lint biome 
#
 Supports other linters

rtk tsc 
#
 TypeScript errors grouped by file

rtk next build 
#
 Next.js build compact

rtk prettier --check 
.
 
#
 Files needing formatting

rtk cargo build 
#
 Cargo build (-80%)

rtk cargo clippy 
#
 Cargo clippy (-80%)

rtk ruff check 
#
 Python linting (JSON, -80%)

rtk golangci-lint run 
#
 Go linting (JSON, -85%)

rtk rubocop 
#
 Ruby linting (JSON, -60%+)

### Package Managers

rtk pnpm list 
#
 Compact dependency tree

rtk pip list 
#
 Python packages (auto-detect uv)

rtk pip outdated 
#
 Outdated packages

rtk bundle install 
#
 Ruby gems (strip Using lines)

rtk prisma generate 
#
 Schema generation (no ASCII art)

### AWS

rtk aws sts get-caller-identity 
#
 One-line identity

rtk aws ec2 describe-instances 
#
 Compact instance list

rtk aws lambda list-functions 
#
 Name/runtime/memory (strips secrets)

rtk aws logs get-log-events 
#
 Timestamped messages only

rtk aws cloudformation describe-stack-events 
#
 Failures first

rtk aws dynamodb scan 
#
 Unwraps type annotations

rtk aws iam list-roles 
#
 Strips policy documents

rtk aws s3 ls 
#
 Truncated with tee recovery

### Containers

rtk docker ps 
#
 Compact container list

rtk docker images 
#
 Compact image list

rtk docker logs 
<
container
>
 
#
 Deduplicated logs

rtk docker compose ps 
#
 Compose services

rtk kubectl pods 
#
 Compact pod list

rtk kubectl logs 
<
pod
>
 
#
 Deduplicated logs

rtk kubectl services 
#
 Compact service list

### Data & Analytics

rtk json config.json 
#
 Structure without values

rtk deps 
#
 Dependencies summary

rtk env -f AWS 
#
 Filtered env vars

rtk log app.log 
#
 Deduplicated logs

rtk curl 
<
url
>
 
#
 Truncate + save full output

rtk wget 
<
url
>
 
#
 Download, strip progress bars

rtk summary 
<
long command
>
 
#
 Heuristic summary

rtk proxy 
<
command
>
 
#
 Raw passthrough + tracking

### Token Savings Analytics

rtk gain 
#
 Summary stats

rtk gain --graph 
#
 ASCII graph (last 30 days)

rtk gain --history 
#
 Recent command history

rtk gain --daily 
#
 Day-by-day breakdown

rtk gain --all --format json 
#
 JSON export for dashboards

rtk discover 
#
 Find missed savings opportunities

rtk discover --all --since 7 
#
 All projects, last 7 days

rtk session 
#
 Show RTK adoption across recent sessions

## Global Flags

-u, --ultra-compact 
#
 ASCII icons, inline format (extra token savings)

-v, --verbose 
#
 Increase verbosity (-v, -vv, -vvv)

## Examples

Directory listing:

# ls -la (45 lines, ~800 tokens) # rtk ls (12 lines, ~150 tokens)
drwxr-xr-x 15 user staff 480 ... my-project/
-rw-r--r-- 1 user staff 1234 ... +-- src/ (8 files)
... | +-- main.rs
 +-- Cargo.toml

Git operations:

# git push (15 lines, ~200 tokens) # rtk git push (1 line, ~10 tokens)
Enumerating objects: 5, done. ok main
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
...

Test output:

# cargo test (200+ lines on failure) # rtk test cargo test (~20 lines)
running 15 tests FAILED: 2/15 tests
test utils::test_parse ... ok test_edge_case: assertion failed
test utils::test_format ... ok test_overflow: panic at utils.rs:18
...

## Auto-Rewrite Hook

The most effective way to use rtk. The hook transparently intercepts Bash commands and rewrites them to rtk equivalents before execution.

Result: 100% rtk adoption across all conversations and subagents, zero token overhead.

Scope note:this only applies to Bash tool calls. Claude Code built-in tools such asRead,Grep, andGlobbypass the hook, so use shell commands or explicitrtkcommands when you want RTK filtering there.

### Setup

rtk init -g 
#
 Install hook + RTK.md (recommended)

rtk init -g --opencode 
#
 OpenCode plugin (instead of Claude Code)

rtk init -g --auto-patch 
#
 Non-interactive (CI/CD)

rtk init -g --hook-only 
#
 Hook only, no RTK.md

rtk init --show 
#
 Verify installation

After install,restart Claude Code.

## Windows

RTK works on Windows with some limitations. The auto-rewrite hook (rtk-rewrite.sh) requires a Unix shell, so on native Windows RTK falls back toCLAUDE.md injection mode— your AI assistant receives RTK instructions but commands are not rewritten automatically.

### Recommended: WSL (full support)

For the best experience, useWSL(Windows Subsystem for Linux). Inside WSL, RTK works exactly like Linux — full hook support, auto-rewrite, everything:

#
 Inside WSL

curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh 
|
 sh
rtk init -g

### Native Windows (limited support)

On native Windows (cmd.exe / PowerShell), RTK filters work but the hook does not auto-rewrite commands:

#
 1. Download and extract rtk-x86_64-pc-windows-msvc.zip from releases

#
 2. Add rtk.exe to your PATH

#
 3. Initialize (falls back to CLAUDE.md injection)

rtk init 
-
g

#
 4. Use rtk explicitly

rtk cargo test
rtk git status

Important: Do not double-clickrtk.exe— it is a CLI tool that prints usage and exits immediately. Always run it from a terminal (Command Prompt, PowerShell, or Windows Terminal).

Feature

WSL

Native Windows

Filters (cargo, git, etc.)

Full

Full

Auto-rewrite hook

Yes

No (CLAUDE.md fallback)

rtk init -g

Hook mode

CLAUDE.md mode

rtk gain
 / analytics

Full

Full

## Supported AI Tools

RTK supports 12 AI coding tools. Each integration transparently rewrites shell commands tortkequivalents for 60-90% token savings.

Tool

Install

Method

Claude Code

rtk init -g

PreToolUse hook (bash)

GitHub Copilot (VS Code)

rtk init -g --copilot

PreToolUse hook — transparent rewrite

GitHub Copilot CLI

rtk init -g --copilot

PreToolUse deny-with-suggestion (CLI limitation)

Cursor

rtk init -g --agent cursor

preToolUse hook (hooks.json)

Gemini CLI

rtk init -g --gemini

BeforeTool hook

Codex

rtk init -g --codex

AGENTS.md + RTK.md instructions

Windsurf

rtk init --agent windsurf

.windsurfrules (project-scoped)

Cline / Roo Code

rtk init --agent cline

.clinerules (project-scoped)

OpenCode

rtk init -g --opencode

Plugin TS (tool.execute.before)

OpenClaw

openclaw plugins install ./openclaw

Plugin TS (before_tool_call)

Mistral Vibe

Planned (
#800
)

Blocked on upstream

Kilo Code

rtk init --agent kilocode

.kilocode/rules/rtk-rules.md (project-scoped)

Google Antigravity

rtk init --agent antigravity

.agents/rules/antigravity-rtk-rules.md (project-scoped)

For per-agent setup details, override controls, and graceful degradation, see theSupported Agents guide.

## Configuration

~/.config/rtk/config.toml(macOS:~/Library/Application Support/rtk/config.toml):

[
hooks
]

exclude_commands
 = [
"
curl
"
, 
"
playwright
"
] 
#
 skip rewrite for these

[
tee
]

enabled
 = 
true
 
#
 save raw output on failure (default: true)

mode
 = 
"
failures
"
 
#
 "failures", "always", or "never"

When a command fails, RTK saves the full unfiltered output so the LLM can read it without re-executing:

FAILED: 2/15 tests
[full output: ~/.local/share/rtk/tee/1707753600_cargo_test.log]

For the full config reference (all sections, env vars, per-project filters), see theConfiguration guide.

### Uninstall

rtk init -g --uninstall 
#
 Remove hook, RTK.md, settings.json entry

cargo uninstall rtk 
#
 Remove binary

brew uninstall rtk 
#
 If installed via Homebrew

## Documentation

* rtk-ai.app/guide— full user guide (installation, supported agents, what gets optimized, analytics, configuration, troubleshooting)
* INSTALL.md— detailed installation reference
* ARCHITECTURE.md— system design and technical decisions
* CONTRIBUTING.md— contribution guide
* SECURITY.md— security policy

## Privacy & Telemetry

RTK can collectanonymous, aggregate usage metricsonce per day. Telemetry isdisabled by defaultand requiresexplicit opt-in consent(GDPR Art. 6, 7) duringrtk initor viartk telemetry enable. This data helps us build a better product: identifying which commands need filters, which filters need improvement, and how much value RTK delivers. For the full list of fields, data handling, and contributor guidelines, seedocs/TELEMETRY.md.

What is collected and why:

Category

Data

Why

Identity

Salted device hash (SHA-256, not reversible)

Count unique installations without tracking individuals

Environment

RTK version, OS, architecture, install method

Know which platforms to support and test

Usage volume

Command count (24h), total commands, tokens saved (24h/30d/total)

Measure adoption and value delivered

Quality

Top 5 passthrough commands (0% savings), parse failure count, commands with <30% savings

Identify missing filters and weak ones to improve

Ecosystem

Command category distribution (e.g. git 45%, cargo 20%, js 15%)

Prioritize filter development for popular ecosystems

Retention

Days since first use, active days in last 30

Understand engagement and detect churn

Adoption

AI agent hook type (claude/gemini/codex), custom TOML filter count

Track integration coverage and DSL adoption

Configuration

Whether config.toml exists, number of excluded commands, project count

Understand user maturity and customization patterns

Features

Usage counts for meta-commands (gain, discover, proxy, verify)

Know which RTK features are valued vs unused

Economics

Estimated USD savings (based on API token pricing)

Quantify the value RTK provides to users

All data isaggregate counts or anonymized command names(first 3 words, no arguments). Top commands report only tool names (e.g. "git", "cargo"), never full command lines.

What is NOT collected:source code, file paths, command arguments, secrets, environment variables, personal data, or repository contents.

Manage telemetry:

rtk telemetry status 
#
 Check current consent state

rtk telemetry 
enable
 
#
 Give consent (interactive prompt)

rtk telemetry disable 
#
 Withdraw consent — stops all collection immediately

rtk telemetry forget 
#
 Withdraw consent + delete all local data + request server-side erasure

Override via environment:

export
 RTK_TELEMETRY_DISABLED=1 
#
 Blocks telemetry regardless of consent

## Star History

## StarMapper

## Core team

* Patrick Szymkowiak— FounderGitHub·LinkedIn
* Florian Bruniaux— Core contributorGitHub·LinkedIn
* Adrien Eppling— Core contributorGitHub·LinkedIn

## Contributing

Contributions welcome! Please open an issue or PR onGitHub.

Join the community onDiscord.

## License

MIT License - seeLICENSEfor details.

## Disclaimer

SeeDISCLAIMER.md.

## About

CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies

www.rtk-ai.app

### Topics

 rust

 cli

 productivity

 open-source

 developer-tools

 command-line-tool

 llm

 cost-reduction

 anthropic

 ai-coding

 claude-code

 token-optimization

 agentic-coding

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

33.1k

 stars
 

### Watchers

87

 watching
 

### Forks

1.9k

 forks
 

 Report repository

 

## Releases129

v0.37.2

 Latest

 

Apr 20, 2026

 

+ 128 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust92.1%
* Shell5.8%
* TypeScript1.8%
* Other0.3%