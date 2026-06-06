---
title: 'GitHub - alibaba/open-code-review: Battle-tested at Alibaba''s scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in fine-tuned ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible. · GitHub'
url: https://github.com/alibaba/open-code-review
site_name: hackernews_api
content_file: hackernews_api-github-alibabaopen-code-review-battle-tested-at-al
fetched_at: '2026-06-06T11:50:09.057799'
original_url: https://github.com/alibaba/open-code-review
author: geoffbp
date: '2026-06-05'
description: 'Battle-tested at Alibaba''s scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in fine-tuned ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible. - alibaba/open-code-review'
tags:
- hackernews
- trending
---

alibaba

 

/

open-code-review

Public

* NotificationsYou must be signed in to change notification settings
* Fork132
* Star2.8k

 
 
 
 
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

73 Commits
73 Commits
.claude-plugin
.claude-plugin
 
 
.claude/
commands
.claude/
commands
 
 
.github
.github
 
 
bin
bin
 
 
cmd
cmd
 
 
examples
examples
 
 
imgs
imgs
 
 
internal
internal
 
 
pages
pages
 
 
plugins/
open-code-review
plugins/
open-code-review
 
 
scripts
scripts
 
 
skills/
open-code-review
skills/
open-code-review
 
 
.gitignore
.gitignore
 
 
.npmignore
.npmignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTING.zh-CN.md
CONTRIBUTING.zh-CN.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

The open source AI code review agent.

English |简体中文

## What is Open Code Review?

Open Code Review is an AI-powered code review CLI tool. It originated as Alibaba Group's internal official AI code review assistant — over the past two years, it has served tens of thousands of developers and identified millions of code defects. After thorough validation at massive scale, we incubated it into an open source project for the community. Simply configure a model endpoint to get started.

It reads Git diffs, sends changed files to a configurable LLM via an agent with tool-use capabilities, and generates structured review comments with line-level precision. The agent can read full file contents, search the codebase, inspect other changed files for context, and produce deep reviews — not just surface-level diff feedback.

## Why Open Code Review?

### The Problem with General-Purpose Agents

If you've used general-purpose agents like Claude Code with Skills for code review, you've likely encountered these pain points:

* Incomplete coverage— On larger changesets, agents tend to "cut corners," selectively reviewing only some files and missing others.
* Position drift— Reported issues frequently don't match the actual code location, with line numbers or file references drifting off target.
* Unstable quality— Natural-language-driven Skills are hard to debug, and review quality fluctuates significantly with minor prompt variations.

The root cause: a purely language-driven architecture lacks hard constraints on the review process.

### Core Design: Deterministic Engineering × Agent Hybrid

Open Code Review's core philosophy is to combine deterministic engineering with an agent, each handling what it does best.

Deterministic Engineering — Hard Constraints

For review steps thatmust not go wrong, engineering logic — not the language model — guarantees correctness:

* Precise file selection— Determines exactly which files need review and which should be filtered, ensuring no important change is missed.
* Smart file bundling— Groups related files into a single review unit (e.g.,message_en.propertiesandmessage_zh.propertiesare bundled together). Each bundle runs as a sub-agent with isolated context — a divide-and-conquer strategy that stays stable on very large changesets and naturally supports concurrent review.
* Fine-grained rule matching— Matches review rules to each file's characteristics, keeping the model's attention sharply focused and eliminating information noise at the source. Compared to purely language-driven rule guidance, template-engine-based rule matching is more stable and predictable.
* External positioning and reflection modules— Independent comment-positioning and comment-reflection modules systematically improve both the location accuracy and content accuracy of AI feedback.

Agent — Dynamic Decision-Making

The agent's strengths are concentrated where they matter most — dynamic decisions and dynamic context retrieval:

* Scenario-tuned prompts— Prompt templates deeply optimized for code review, improving effectiveness while reducing token consumption.
* Scenario-tuned toolset— Distilled from deep analysis of tool-call traces in large-scale production data — including call frequency distributions, per-tool repetition rates, and the impact of new tools on the overall call chain — resulting in a purpose-built toolset that is more stable and predictable for code review than a generic agent toolkit.

## How to Use

### CLI

#### Install

Via NPM (Recommended)

npm install -g @alibaba-group/open-code-review

After installation, theocrcommand is available globally.

From GitHub Release

Download the latest binary fromGitHub Releases:

#
 macOS (Apple Silicon)

curl -Lo ocr https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-darwin-arm64
chmod +x ocr 
&&
 sudo mv ocr /usr/local/bin/ocr

#
 macOS (Intel)

curl -Lo ocr https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-darwin-amd64
chmod +x ocr 
&&
 sudo mv ocr /usr/local/bin/ocr

#
 Linux (x86_64)

curl -Lo ocr https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-linux-amd64
chmod +x ocr 
&&
 sudo mv ocr /usr/local/bin/ocr

#
 Linux (ARM64)

curl -Lo ocr https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-linux-arm64
chmod +x ocr 
&&
 sudo mv ocr /usr/local/bin/ocr

#
 Windows (x86_64) — move ocr.exe to a directory in your PATH

curl -Lo ocr.exe https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-windows-amd64.exe

#
 Windows (ARM64) — move ocr.exe to a directory in your PATH

curl -Lo ocr.exe https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-windows-arm64.exe

From Source

git clone https://github.com/alibaba/open-code-review.git

cd
 open-code-review
make build
sudo cp dist/opencodereview /usr/local/bin/ocr

#### Quick Start

1. Configure LLM

You must configure an LLM before reviewing code.

#
 Option A: Interactive config

ocr config 
set
 llm.url https://api.anthropic.com/v1/messages
ocr config 
set
 llm.auth_token your-api-key-here
ocr config 
set
 llm.model claude-opus-4-6
ocr config 
set
 llm.use_anthropic 
true

#
 Option B: Environment variables (highest priority)

export
 OCR_LLM_URL=https://api.anthropic.com/v1/messages

export
 OCR_LLM_TOKEN=your-api-key-here

export
 OCR_LLM_MODEL=claude-opus-4-6

export
 OCR_USE_ANTHROPIC=true

Config is stored in~/.opencodereview/config.json.

It is also compatible with Claude Code environment variables (ANTHROPIC_BASE_URL,ANTHROPIC_AUTH_TOKEN,ANTHROPIC_MODEL) and parses~/.zshrc/~/.bashrcfor those exports.

Note for CC-Switch Users: If you are usingCC-Switchwithrouting serviceenabled, you can pointllm.urlto the CC-Switch proxy address without additional configuration:

* ForClaudeprovider: setllm.urltohttp://127.0.0.1:15721
* ForCodeXprovider: setllm.urltohttp://127.0.0.1:15721/v1
* Setllm.modelaccording to your provider settings
* llm.auth_tokencan be any value
* extra_bodysettings still apply

2. Test Connectivity

ocr llm 
test

3. Review

cd
 your-project

#
 Workspace mode — review all staged, unstaged, and untracked changes

ocr review

#
 Branch range — compare two refs

ocr review --from main --to feature-branch

#
 Single commit

ocr review --commit abc123

### Integrate with Coding Agents

OCR can be seamlessly integrated into AI coding agents as a slash command, enabling code review directly within your agent workflow.

#### Option 1: Install as a Skill

Usenpxto install the OCR skill into your project:

npx skills add alibaba/open-code-review --skill open-code-review

This installs theopen-code-reviewskill from theskills registry, which teaches your coding agent how to invokeocrfor code review, classify issues by priority, and optionally apply fixes.

#### Option 2: Install as a Claude Code Plugin

ForClaude Code, install the command plugin through the following command in Claude Code:

/plugin marketplace add alibaba/open-code-review
/plugin install open-code-review@open-code-review

This registers the/open-code-review:reviewslash command, which runs OCR and automatically filters and fixes issues.

#### Option 3: Copy the Command File Directly

For a quick setup without any package manager, simply copy the command file to use the/open-code-reviewslash command in Claude Code.

Project-level(shared with team via git):

mkdir -p .claude/commands
curl -o .claude/commands/open-code-review.md \
 https://raw.githubusercontent.com/alibaba/open-code-review/main/plugins/open-code-review/commands/review.md

User-level(personal global use across all projects):

mkdir -p 
~
/.claude/commands
curl -o 
~
/.claude/commands/open-code-review.md \
 https://raw.githubusercontent.com/alibaba/open-code-review/main/plugins/open-code-review/commands/review.md

Prerequisite: All integration methods require theocrCLI to be installed and an LLM configured. SeeInstallandConfigure LLMabove.

### CI/CD Integration

OCR can be integrated into CI/CD pipelines to automate code review on Merge Requests / Pull Requests.

The core command for CI integration:

ocr review \
 --from 
"
origin/main
"
 \
 --to 
"
origin/feature-branch
"
 \
 --format json

The--format jsonflag outputs machine-readable results suitable for parsing in CI scripts.

See theexamples/directory for integration examples:

* github_actions/— GitHub Actions integration example
* gitlab_ci/— GitLab CI integration example

## Commands

Command

Alias

Description

ocr review

ocr r

Start a code review

ocr rules check <file>

—

Preview which review rule applies to a file path

ocr config set <key> <value>

—

Set configuration values

ocr llm test

—

Test LLM connectivity

ocr viewer

ocr v

Launch WebUI session viewer on 
localhost:5483

ocr version

—

Show version info

### ocr reviewFlags

Flag

Shorthand

Default

Description

--repo

—

current dir

Git repository root

--from

—

—

Source ref (e.g., 
main
)

--to

—

—

Target ref (e.g., 
feature-branch
)

--commit

-c

—

Single commit to review

--preview

-p

false

Preview which files will be reviewed without running the LLM

--format

-f

text

Output format: 
text
 or 
json

--concurrency

—

8

Max concurrent file reviews

--timeout

—

10

Concurrent task timeout in minutes

--audience

—

human

human
 (show progress) or 
agent
 (summary only)

--rule

—

—

Path to custom JSON review rules

--max-tools

—

built-in

Max tool call rounds per file; only takes effect when greater than template default

--tools

—

—

Path to custom JSON tools config

## Examples

#
 Preview which files will be reviewed (no LLM calls)

ocr review --preview
ocr review -c abc123 -p

#
 Review workspace changes with default settings

ocr review

#
 Review branch diff with higher concurrency

ocr review --from main --to my-feature --concurrency 4

#
 Review a specific commit with verbose JSON output

ocr review --commit abc123 --format json --audience agent

#
 Use custom review rules

ocr review --rule /path/to/my-rules.json

#
 Preview which rule applies to a file

ocr rules check src/main/java/com/example/Foo.java
ocr rules check --rule custom.json src/main/resources/mapper/UserMapper.xml

#
 View review session history in browser

ocr viewer
ocr viewer --addr :3000

### Viewer security

The viewer serves session JSONL contents (LLM request messages and responses) over HTTP. It enforces a Host-header allowlist on every request: loopback names (localhost,127.0.0.0/8,::1) and the concrete bind host are always allowed. Wildcard binds (--addr :3000,--addr 0.0.0.0:3000) and other non-loopback Hostnames must be added via theOCR_VIEWER_ALLOWED_HOSTSenvironment variable (comma-separated):

OCR_VIEWER_ALLOWED_HOSTS=review.internal,ocr.lan ocr viewer --addr :3000

This blocks DNS-rebinding attacks against the local viewer.

## Review Rules

OCR resolves review rules using a four-layer priority chain. Each layer uses first-match-wins: if a file path matches a pattern, that rule is used; otherwise it falls through to the next layer.

Priority

Source

Path

Description

1 (highest)

--rule
 flag

User-specified path

CLI explicit override

2

Project config

<repoDir>/.opencodereview/rule.json

Per-project rules, can be committed to git

3

Global config

~/.opencodereview/rule.json

User-wide personal preferences

4 (lowest)

System default

Embedded 
system_rules.json

Built-in rules covering common languages and file types

### Rule File Format

Layers 1–3 share the same JSON format:

{
 
"rules"
: [
 {
 
"path"
: 
"
force-api/**/*.java
"
,
 
"rule"
: 
"
All new methods must validate required parameters for null values
"

 },
 {
 
"path"
: 
"
**/*mapper*.xml
"
,
 
"rule"
: 
"
Check SQL for injection risks, parameter errors, and missing closing tags
"

 }
 ]
}

* pathsupports**recursive matching and{java,kt}brace expansion.
* Within each layer, rules are evaluated in declaration order — the first match wins.
* If a rule file does not exist, it is silently skipped.

## Configuration Reference

Config file:~/.opencodereview/config.json

Key

Type

Example

llm.url

string

https://api.openai.com/v1/chat/completions

llm.auth_token

string

sk-xxxxxxx

llm.model

string

claude-opus-4-6

llm.use_anthropic

boolean

true
 | 
false

language

string

English
 | 
Chinese
 (default: Chinese)

telemetry.enabled

boolean

true
 | 
false

telemetry.exporter

string

console
 | 
otlp

telemetry.otlp_endpoint

string

OTLP collector address

telemetry.content_logging

boolean

Include prompts in telemetry

Environment variables take precedence over the config file.

### Environment Variables

Variable

Purpose

OCR_LLM_URL

LLM API endpoint URL

OCR_LLM_TOKEN

API key / auth token

OCR_LLM_MODEL

Model name

OCR_USE_ANTHROPIC

true
 = Anthropic, 
false
 = OpenAI

## Telemetry

OpenTelemetry integration for observability (spans, metrics). Disabled by default.

ocr config 
set
 telemetry.enabled 
true

ocr config 
set
 telemetry.exporter otlp
ocr config 
set
 telemetry.otlp_endpoint localhost:4317

Settelemetry.content_loggingto include LLM prompts and responses in exported data.

## Contributing

SeeCONTRIBUTING.mdfor development setup, coding guidelines, and how to submit pull requests.

## Star History

## License

Apache-2.0— Copyright 2026 Alibaba

## About

Battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in fine-tuned ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible.

alibaba.github.io/open-code-review/

### Topics

 agent

 code-review

 harness

 repository-level-context

 code-review-assistant

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

2.8k

 stars
 

### Watchers

6

 watching
 

### Forks

132

 forks
 

 Report repository

 

## Releases31

v1.1.21

 Latest

 

Jun 5, 2026

 

+ 30 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go70.7%
* TypeScript16.6%
* CSS4.0%
* JavaScript3.3%
* Shell2.7%
* HTML2.2%
* Makefile0.5%