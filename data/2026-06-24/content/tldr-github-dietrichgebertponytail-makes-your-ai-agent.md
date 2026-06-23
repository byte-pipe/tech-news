---
title: 'GitHub - DietrichGebert/ponytail: Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. · GitHub'
url: https://github.com/DietrichGebert/ponytail
site_name: tldr
content_file: tldr-github-dietrichgebertponytail-makes-your-ai-agent
fetched_at: '2026-06-24T01:01:54.198409'
original_url: https://github.com/DietrichGebert/ponytail
date: '2026-06-24'
description: Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. - DietrichGebert/ponytail
tags:
- tldr
---

DietrichGebert

 

/

ponytail

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork2.6k
* Star51.7k

 
 
 
 
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

109 Commits
109 Commits
.agents
.agents
 
 
.claude-plugin
.claude-plugin
 
 
.clinerules
.clinerules
 
 
.codex-plugin
.codex-plugin
 
 
.cursor/
rules
.cursor/
rules
 
 
.github
.github
 
 
.kiro/
steering
.kiro/
steering
 
 
.openclaw/
skills
.openclaw/
skills
 
 
.opencode
.opencode
 
 
.windsurf/
rules
.windsurf/
rules
 
 
assets
assets
 
 
benchmarks
benchmarks
 
 
commands
commands
 
 
docs
docs
 
 
examples
examples
 
 
hooks
hooks
 
 
pi-extension
pi-extension
 
 
ponytail-mcp
ponytail-mcp
 
 
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
 
 
AGENTS.md
AGENTS.md
 
 
LICENSE
LICENSE
 
 
README.es.md
README.es.md
 
 
README.md
README.md
 
 
gemini-extension.json
gemini-extension.json
 
 
opencode.json
opencode.json
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# Ponytail

He says nothing. He writes one line. It works.

~54% less code (up to 94%) · ~20% cheaper · ~27% faster · 100% safeMeasured on real Claude Code sessions editing a real open-source repo (FastAPI + React), against the same agent with no skill. ~54% is the mean across 12 feature tasks (Haiku 4.5, n=4); it reaches 94% where an agent over-builds (a date picker) and is near zero where the code is already minimal. ponytail keeps every safety guard while a bare "write one-liners" prompt drops one. (The earlier single-shot benchmark reported 80-94% as a flat figure; against a fair agentic baseline that is the per-task ceiling, not the average.)Full writeup·reproduce it.

Español

You know him. Long ponytail. Oval glasses. Has been at the company longer than the version control. You show him fifty lines; he looks at them, says nothing, and replaces them with one.

Ponytail puts him inside your AI agent.

## Before / after

You ask for a date picker. Your agent installs flatpickr, writes a wrapper component, adds a stylesheet, and starts a discussion about timezones.

With ponytail:

<!-- ponytail: browser has one -->

<
input
 
type
="
date
"
>

More survivors inexamples/.

## Numbers

The honest measurement is a real agent doing real work: a headless Claude Code session editingtiangolo's full-stack-fastapi-template(a real FastAPI + React repo), scored on thegit diffit leaves behind. Twelve feature tickets, the same agent with and without the skill, n=4, Haiku 4.5.

vs no-skill baseline

LOC

tokens

cost

time

safe

ponytail

-54%

-22%

-20%

-27%

100%

caveman (terse-prose control)

-20%

+7%

+3%

+2%

100%

"YAGNI + one-liners" prompt

-33%

-14%

-21%

-30%

95%

ponytail is the only arm that cuts every metric, and the only one that stays fully safe while doing it. The cut is biggest where there is a real over-build trap (date picker 404 to 23 lines, color picker 287 to 23, because it reaches for a native<input>instead of a component) and near zero on code that is already minimal. Full method, per-task tables, and limitations:benchmarks/results/2026-06-18-agentic.md.

Older single-shot numbers (isolated generation)

Five everyday tasks, three models, three arms (no skill,caveman, ponytail), ten runs, median reported. One prompt, one completion, counting lines of the answer:

This showed80-94% less code.#126fairly pointed out that the bare-model baseline pads its answer with prose and options, so that gap is partly a conversational-baseline artifact. The agentic numbers above are the corrected, defensible version. Reproduce the single-shot run withnpx promptfoo eval -c benchmarks/promptfooconfig.yaml.

The rule was never "fewest tokens."It is: write only what the task needs, and never cut validation, error handling, security, or accessibility. The code ends up small because it is necessary, not golfed. Lower cost and latency are a side effect on the models that follow the ladder; a terse reasoning model that spends thinking tokens deliberating the rungs can go the other way (on GPT-5.5 it does).

## How it works

Before writing code, the agent stops at the first rung that holds:

1. Does this need to exist? → no: skip it (YAGNI)
2. Already in this codebase? → reuse it, don't rewrite
3. Stdlib does it? → use it
4. Native platform feature? → use it
5. Installed dependency? → use it
6. One line? → one line
7. Only then: the minimum that works

The ladder runsafterit understands the problem, not instead of it: it reads the code the change touches and traces the real flow before picking a rung. Lazy about the solution, never about reading.

Lazy, not negligent: trust-boundary validation, data-loss handling, security, and accessibility are never on the chopping block.

## Install

The most effort ponytail will ever ask of you:

The Claude Code and Codex plugins run two tiny Node.js lifecycle hooks, sonodeneeds to be on your PATH (note for Nix/nvm users: it must be on the non-interactive shell's PATH). If it isn't, the skills still work, the always-on activation just stays quiet instead of erroring on every prompt.

### Claude Code

/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail

The desktop app has no/plugincommand. Install it from the UI instead: Customize, the + by personal plugins, Create plugin and add marketplace, Add from repository, then enter the repo URL (thanks @NiklasDHahn, #98).

### Codex

codex plugin marketplace add DietrichGebert/ponytail
codex

Open/plugins, select the Ponytail marketplace, and install Ponytail. Then
open/hooks, review and trust its two lifecycle hooks, and start a new thread.

This same install also covers the Codex desktop app: restart the app after installing and it picks up the plugin.

### GitHub Copilot CLI

copilot plugin marketplace add DietrichGebert/ponytail
copilot plugin install ponytail@ponytail

In an interactive Copilot CLI session, use the slash equivalents:

/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail

Copilot CLI namespaces plugin commands by plugin name. For example:

/ponytail:ponytail ultra
/ponytail:ponytail-review

### Pi agent harness

pi install git:github.com/DietrichGebert/ponytail

### OpenCode

Run OpenCode from a checkout of this repo (the plugin reuses itshooks/andskills/), and add toopencode.json:

{ 
"plugin"
: [
"
./.opencode/plugins/ponytail.mjs
"
] }

Injects the ruleset every turn at the active level; adds the/ponytailcommands (seeCommands). OpenCode also auto-loads this repo'sAGENTS.md, so the rules hold even without the plugin. The plugin adds thelite/full/ultra/offlevels.

The./path resolves against your project'sopencode.json; to share one checkout across projects, point it at the absolute path of the.mjsinstead (it finds itshooks/andskills/relative to its own file).

The plugin path loads the ruleset everywhere, but the/ponytailcommands are separate files in.opencode/command/that OpenCode only discovers from your project or the global commands dir. To use them outside this checkout, link them once:ln -sf /absolute/path/to/ponytail/.opencode/command/* ~/.config/opencode/command/.

### Gemini CLI

gemini extensions install https://github.com/DietrichGebert/ponytail

Loads the ruleset as always-on context every session and registers the/ponytailcommands; theskills/ship too, activated when a task needs them.
The Gemini adapter intentionally does not ship a roothooks/hooks.json: Gemini auto-loads that path, while Ponytail's lifecycle hooks use Claude/Codex event names.

### Antigravity CLI

Google is renaming Gemini CLI to Antigravity CLI (theagybinary); the same extension installs there:

agy plugin install https://github.com/DietrichGebert/ponytail

It reuses this repo'sgemini-extension.json. One difference: Antigravity converts the/ponytailcommands into skills, so you type them into the chat (e.g./ponytail-reviewas a message) instead of picking them from a slash menu. Until the migration completes (around June 18, 2026),gemini extensions installstill works too. To run it as an always-on rule instead, drop the ruleset into.agents/rules/.

### CodeWhale

ReadsAGENTS.mdfrom the project root, zero setup. CopyAGENTS.mdto your project, or runcodewhalefrom a checkout of this repo. That's it.

### OpenClaw

clawhub install ponytail

Installs ponytail as an OpenClaw skill from ClawHub; the review, audit, debt, gain, and help skills install the same way (clawhub install ponytail-review, and so on). OpenClaw applies it on coding tasks and also exposes it as a/ponytailcommand. Without ClawHub, copy.openclaw/skills/ponytailinto~/.openclaw/skills/.

That was it. He'd be proud. He won't say it.

Active every session, with a handful of commands (seeCommands)./ponytail ultraexists for when the codebase has wronged you personally. Startup and mode-change text shows the current mode.

Set the level for every new session with thePONYTAIL_DEFAULT_MODEenv var (lite/full/ultra/off), or adefaultModefield in~/.config/ponytail/config.json(%APPDATA%\ponytail\config.jsonon Windows). The default isfull.

Cursor, Windsurf, Cline, GitHub Copilot (editor), Aider, Kiro, Zed, CodeWhale: copy the matching rules file from this repo (.cursor/rules/,.windsurf/rules/,.clinerules/,.github/copilot-instructions.md,AGENTS.md,.kiro/steering/).

Kiro: copy.kiro/steering/ponytail.mdto~/.kiro/steering/(global) or.kiro/steering/in your project.

GitHub Copilot CLI fallback (instruction-only mode): it readsAGENTS.mdand.github/copilot-instructions.mdin a project, or copy the rules into~/.copilot/copilot-instructions.mdto run ponytail in every project. This path keeps always-on guidance, but does not add plugin mode switches or hooks.

VS Code with the Codex extension readsAGENTS.md, which this repo ships, so it works from the repo root with no setup (~/.codex/AGENTS.mdmakes Codex global).

Which files map to which agent:Agent portability.

## Commands

Command

What it does

/ponytail [lite | full | ultra | off]

Set the intensity, or turn it off. No argument reports the current level.

/ponytail-review

Review the current diff for over-engineering, hands back a delete-list.

/ponytail-audit

Audit the whole repo for over-engineering, not just the diff.

/ponytail-debt

Harvest the 
ponytail:
 shortcuts you've deferred into a ledger, so "later" doesn't become "never".

/ponytail-gain

Show the measured impact scoreboard (less code, less cost, more speed) from the benchmark.

/ponytail-help

Quick reference for the commands above.

Commands need a skill-capable host (Claude Code, Codex, OpenCode, Gemini, pi). In Codex they're skills, invoke with@(@ponytail-review). The instruction-only adapters (Cursor, Windsurf, Cline, Copilot, Kiro, Antigravity) load the always-on ruleset without the commands.

## Development

When changing the compact rule text, keep the agent copies aligned:

node scripts/check-rule-copies.js
npm 
test

The OpenClaw skill package (.openclaw/skills/) is generated fromskills/; rerunnode scripts/build-openclaw-skills.jsafter changing a skill, the test suite fails if it is stale.

The correctness benchmark spawns Python for email and CSV checks;python3is tried beforepython. CSV checks needpandasinstalled locally.

## FAQ

Does it need a config file?No. An optional~/.config/ponytail/config.jsonorPONYTAIL_DEFAULT_MODEenv var can set the default level, but nothing is required.

What if I really need the 120-line cache class?You don't. Insist anyway and he'll build it. Slowly. Correctly. While looking at you.

Does it scale?The code you never wrote scales infinitely. Zero bugs, zero CVEs, 100% uptime since forever.

Why "ponytail"?You know exactly why.

## License

MIT. The shortest license that works.

## About

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

### Topics

 developer-tools

 ai-agents

 claude

 yagni

 llm

 prompt-engineering

 agent-skills

 cursor-rules

 claude-code

 claude-code-plugin

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

51.7k

 stars
 

### Watchers

125

 watching
 

### Forks

2.6k

 forks
 

 Report repository

 

## Releases10

v4.8.0: comprehension first, now with an MCP server

 Latest

 

Jun 23, 2026

 

+ 9 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript51.2%
* Python48.3%
* Other0.5%