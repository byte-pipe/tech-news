---
title: 'GitHub - Yeachan-Heo/oh-my-codex: OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much more. · GitHub'
url: https://github.com/Yeachan-Heo/oh-my-codex
site_name: github
content_file: github-github-yeachan-heooh-my-codex-omx-oh-my-codex-your
fetched_at: '2026-04-02T19:24:40.134166'
original_url: https://github.com/Yeachan-Heo/oh-my-codex
author: Yeachan-Heo
description: 'OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much more. - Yeachan-Heo/oh-my-codex'
---

Yeachan-Heo



/

oh-my-codex

Public

* NotificationsYou must be signed in to change notification settings
* Fork1k
* Star11.1k




 
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

1,204 Commits
1,204 Commits
.github
.github
 
 
crates
crates
 
 
docs
docs
 
 
missions
missions
 
 
playground
playground
 
 
prompts
prompts
 
 
skills
skills
 
 
src
src
 
 
templates
templates
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
COVERAGE.md
COVERAGE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
DEMO.md
DEMO.md
 
 
README.de.md
README.de.md
 
 
README.el.md
README.el.md
 
 
README.es.md
README.es.md
 
 
README.fr.md
README.fr.md
 
 
README.it.md
README.it.md
 
 
README.ja.md
README.ja.md
 
 
README.ko.md
README.ko.md
 
 
README.md
README.md
 
 
README.pl.md
README.pl.md
 
 
README.pt.md
README.pt.md
 
 
README.ru.md
README.ru.md
 
 
README.tr.md
README.tr.md
 
 
README.vi.md
README.vi.md
 
 
README.zh-TW.md
README.zh-TW.md
 
 
README.zh.md
README.zh.md
 
 
RELEASE_BODY.md
RELEASE_BODY.md
 
 
biome.json
biome.json
 
 
dist-workspace.toml
dist-workspace.toml
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.no-unused.json
tsconfig.no-unused.json
 
 
View all files

## Repository files navigation

# oh-my-codex (OMX)

Start Codex stronger, then let OMX add better prompts, workflows, and runtime help when the work grows.

Website:https://yeachan-heo.github.io/oh-my-codex-website/Docs:Getting Started·Agents·Skills·Integrations·Demo·OpenClaw guide

OMX is a workflow layer forOpenAI Codex CLI.

It keeps Codex as the execution engine and makes it easier to:

* start a stronger Codex session by default
* run one consistent workflow from clarification to completion
* invoke the canonical skills with$deep-interview,$ralplan,$team, and$ralph
* keep project guidance, plans, logs, and state in.omx/

## Recommended default flow

If you want the default OMX experience, start here:

npm install -g @openai/codex oh-my-codex
omx setup
omx --madmax --high

Then work normally inside Codex:

$deep-interview "clarify the authentication change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"

That is the main path.
Start OMX strongly, clarify first when needed, approve the plan, then choose$teamfor coordinated parallel execution or$ralphfor the persistent completion loop.

## What OMX is for

Use OMX if you already like Codex and want a better day-to-day runtime around it:

* a standard workflow built around$deep-interview,$ralplan,$team, and$ralph
* specialist roles and supporting skills when the task needs them
* project guidance through scopedAGENTS.md
* durable state under.omx/for plans, logs, memory, and mode tracking

If you want plain Codex with no extra workflow layer, you probably do not need OMX.

## Quick start

### Requirements

* Node.js 20+
* Codex CLI installed:npm install -g @openai/codex
* Codex auth configured
* tmuxon macOS/Linux if you later want the durable team runtime
* psmuxon native Windows if you later want Windows team mode

### A good first session

Launch OMX the recommended way:

omx --madmax --high

Then try the canonical workflow:

$deep-interview "clarify the authentication change"
$ralplan "approve the safest implementation path"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"

Use$teamwhen the approved plan needs coordinated parallel work, or$ralphwhen one persistent owner should keep pushing to completion.

## A simple mental model

OMX doesnotreplace Codex.

It adds a better working layer around it:

* Codexdoes the actual agent work
* OMX role keywordsmake useful roles reusable
* OMX skillsmake common workflows reusable
* .omx/stores plans, logs, memory, and runtime state

Most users should think of OMX asbetter task routing + better workflow + better runtime, not as a command surface to operate manually all day.

## Start here if you are new

1. Runomx setup
2. Launch withomx --madmax --high
3. Use$deep-interview "..."when the request or boundaries are still unclear
4. Use$ralplan "..."to approve the plan and review tradeoffs
5. Choose$teamfor coordinated parallel execution or$ralphfor persistent completion loops

## Recommended workflow

1. $deep-interview— clarify scope when the request or boundaries are still vague.
2. $ralplan— turn that clarified scope into an approved architecture and implementation plan.
3. $teamor$ralph— use$teamfor coordinated parallel execution, or$ralphwhen you want a persistent completion loop with one owner.

## Common in-session surfaces

Surface

Use it for

$deep-interview "..."

clarifying intent, boundaries, and non-goals

$ralplan "..."

approving the implementation plan and tradeoffs

$ralph "..."

persistent completion and verification loops

$team "..."

coordinated parallel execution when the work is big enough

/skills

browsing installed skills and supporting helpers

## Advanced / operator surfaces

These are useful, but they are not the main onboarding path.

### Team runtime

Use the team runtime when you specifically need durable tmux/worktree coordination, not as the default way to begin using OMX.

omx team 3:executor
"
fix the failing tests with verification
"

omx team status
<
team-name
>

omx team resume
<
team-name
>

omx team shutdown
<
team-name
>

### Setup, doctor, and HUD

These are operator/support surfaces:

* omx setupinstalls prompts, skills, config, and AGENTS scaffolding
* omx doctorverifies the install when something seems wrong
* omx hud --watchis a monitoring/status surface, not the primary user workflow

### Explore and sparkshell

* omx explore --prompt "..."is for read-only repository lookup
* omx sparkshell <command>is for shell-native inspection and bounded verification

Examples:

omx explore --prompt
"
find where team state is written
"

omx sparkshell git status
omx sparkshell --tmux-pane %12 --tail-lines 400

### Platform notes for team mode

omx teamneeds a tmux-compatible backend:

Platform

Install

macOS

brew install tmux

Ubuntu/Debian

sudo apt install tmux

Fedora

sudo dnf install tmux

Arch

sudo pacman -S tmux

Windows

winget install psmux

Windows (WSL2)

sudo apt install tmux

## Known issues

### Intel Mac: highsyspolicyd/trustdCPU during startup

On some Intel Macs, OMX startup — especially with--madmax --high— can spikesyspolicyd/trustdCPU usage while macOS Gatekeeper validates many concurrent process launches.

If this happens, try:

* xattr -dr com.apple.quarantine $(which omx)
* adding your terminal app to the Developer Tools allowlist in macOS Security settings
* using lower concurrency (for example, avoid--madmax --high)

## Documentation

* Getting Started
* Demo guide
* Agent catalog
* Skills reference
* Integrations
* OpenClaw / notification gateway guide
* Contributing
* Changelog

## Languages

* English
* 한국어
* 日本語
* 简体中文
* 繁體中文
* Tiếng Việt
* Español
* Português
* Русский
* Türkçe
* Deutsch
* Français
* Italiano
* Ελληνικά
* Polski

## Contributors

Role

Name

GitHub

Creator & Lead

Yeachan Heo

@Yeachan-Heo

Maintainer

HaD0Yun

@HaD0Yun

## Star History

## License

MIT

## About

OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much more.

### Resources

 Readme



### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

11.1k

 stars


### Watchers

36

 watching


### Forks

1k

 forks


 Report repository



## Releases76

v0.11.12

 Latest



Apr 2, 2026



+ 75 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* TypeScript91.5%
* Rust4.7%
* JavaScript2.7%
* Other1.1%
