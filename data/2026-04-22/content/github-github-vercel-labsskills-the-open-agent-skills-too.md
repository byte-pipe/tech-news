---
title: 'GitHub - vercel-labs/skills: The open agent skills tool - npx skills · GitHub'
url: https://github.com/vercel-labs/skills
site_name: github
content_file: github-github-vercel-labsskills-the-open-agent-skills-too
fetched_at: '2026-04-22T20:04:27.353467'
original_url: https://github.com/vercel-labs/skills
author: vercel-labs
description: The open agent skills tool - npx skills. Contribute to vercel-labs/skills development by creating an account on GitHub.
---

vercel-labs

 

/

skills

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.3k
* Star15.4k

 
 
 
 
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

254 Commits
254 Commits
.github
.github
 
 
.husky
.husky
 
 
bin
bin
 
 
scripts
scripts
 
 
skills/
find-skills
skills/
find-skills
 
 
src
src
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
README.md
README.md
 
 
ThirdPartyNoticeText.txt
ThirdPartyNoticeText.txt
 
 
build.config.mjs
build.config.mjs
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# skills

The CLI for the open agent skills ecosystem.

SupportsOpenCode,Claude Code,Codex,Cursor, and41 more.

## Install a Skill

npx skills add vercel-labs/agent-skills

### Source Formats

#
 GitHub shorthand (owner/repo)

npx skills add vercel-labs/agent-skills

#
 Full GitHub URL

npx skills add https://github.com/vercel-labs/agent-skills

#
 Direct path to a skill in a repo

npx skills add https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines

#
 GitLab URL

npx skills add https://gitlab.com/org/repo

#
 Any git URL

npx skills add git@github.com:vercel-labs/agent-skills.git

#
 Local path

npx skills add ./my-local-skills

### Options

Option

Description

-g, --global

Install to user directory instead of project

-a, --agent <agents...>

Target specific agents (e.g., 
claude-code
, 
codex
). See 
Available Agents

-s, --skill <skills...>

Install specific skills by name (use 
'*'
 for all skills)

-l, --list

List available skills without installing

--copy

Copy files instead of symlinking to agent directories

-y, --yes

Skip all confirmation prompts

--all

Install all skills to all agents without prompts

### Examples

#
 List skills in a repository

npx skills add vercel-labs/agent-skills --list

#
 Install specific skills

npx skills add vercel-labs/agent-skills --skill frontend-design --skill skill-creator

#
 Install a skill with spaces in the name (must be quoted)

npx skills add owner/repo --skill 
"
Convex Best Practices
"

#
 Install to specific agents

npx skills add vercel-labs/agent-skills -a claude-code -a opencode

#
 Non-interactive installation (CI/CD friendly)

npx skills add vercel-labs/agent-skills --skill frontend-design -g -a claude-code -y

#
 Install all skills from a repo to all agents

npx skills add vercel-labs/agent-skills --all

#
 Install all skills to specific agents

npx skills add vercel-labs/agent-skills --skill 
'
*
'
 -a claude-code

#
 Install specific skills to all agents

npx skills add vercel-labs/agent-skills --agent 
'
*
'
 --skill frontend-design

### Installation Scope

Scope

Flag

Location

Use Case

Project

(default)

./<agent>/skills/

Committed with your project, shared with team

Global

-g

~/<agent>/skills/

Available across all projects

### Installation Methods

When installing interactively, you can choose:

Method

Description

Symlink
 (Recommended)

Creates symlinks from each agent to a canonical copy. Single source of truth, easy updates.

Copy

Creates independent copies for each agent. Use when symlinks aren't supported.

## Other Commands

Command

Description

npx skills list

List installed skills (alias: 
ls
)

npx skills find [query]

Search for skills interactively or by keyword

npx skills remove [skills]

Remove installed skills from agents

npx skills update [skills]

Update installed skills to latest versions

npx skills init [name]

Create a new SKILL.md template

### skills list

List all installed skills. Similar tonpm ls.

#
 List all installed skills (project and global)

npx skills list

#
 List only global skills

npx skills ls -g

#
 Filter by specific agents

npx skills ls -a claude-code -a cursor

### skills find

Search for skills interactively or by keyword.

#
 Interactive search (fzf-style)

npx skills find

#
 Search by keyword

npx skills find typescript

### skills update

#
 Update all skills (interactive scope prompt)

npx skills update

#
 Update a single skill by name

npx skills update my-skill

#
 Update multiple specific skills

npx skills update frontend-design web-design-guidelines

#
 Update only global or project skills

npx skills update -g
npx skills update -p

#
 Non-interactive (auto-detects scope: project if in a project, else global)

npx skills update -y

Option

Description

-g, --global

Only update global skills

-p, --project

Only update project skills

-y, --yes

Skip scope prompt (auto-detect: project if in a project dir, else global)

[skills...]

Update specific skills by name instead of all

### skills init

#
 Create SKILL.md in current directory

npx skills init

#
 Create a new skill in a subdirectory

npx skills init my-skill

### skills remove

Remove installed skills from agents.

#
 Remove interactively (select from installed skills)

npx skills remove

#
 Remove specific skill by name

npx skills remove web-design-guidelines

#
 Remove multiple skills

npx skills remove frontend-design web-design-guidelines

#
 Remove from global scope

npx skills remove --global web-design-guidelines

#
 Remove from specific agents only

npx skills remove --agent claude-code cursor my-skill

#
 Remove all installed skills without confirmation

npx skills remove --all

#
 Remove all skills from a specific agent

npx skills remove --skill 
'
*
'
 -a cursor

#
 Remove a specific skill from all agents

npx skills remove my-skill --agent 
'
*
'

#
 Use 'rm' alias

npx skills rm my-skill

Option

Description

-g, --global

Remove from global scope (~/) instead of project

-a, --agent

Remove from specific agents (use 
'*'
 for all)

-s, --skill

Specify skills to remove (use 
'*'
 for all)

-y, --yes

Skip confirmation prompts

--all

Shorthand for 
--skill '*' --agent '*' -y

## What are Agent Skills?

Agent skills are reusable instruction sets that extend your coding agent's capabilities. They're defined inSKILL.mdfiles with YAML frontmatter containing anameanddescription.

Skills let agents perform specialized tasks like:

* Generating release notes from git history
* Creating PRs following your team's conventions
* Integrating with external tools (Linear, Notion, etc.)

Discover skills atskills.sh

## Supported Agents

Skills can be installed to any of these agents:

Agent

--agent

Project Path

Global Path

Amp, Kimi Code CLI, Replit, Universal

amp
, 
kimi-cli
, 
replit
, 
universal

.agents/skills/

~/.config/agents/skills/

Antigravity

antigravity

.agents/skills/

~/.gemini/antigravity/skills/

Augment

augment

.augment/skills/

~/.augment/skills/

IBM Bob

bob

.bob/skills/

~/.bob/skills/

Claude Code

claude-code

.claude/skills/

~/.claude/skills/

OpenClaw

openclaw

skills/

~/.openclaw/skills/

Cline, Warp

cline
, 
warp

.agents/skills/

~/.agents/skills/

CodeBuddy

codebuddy

.codebuddy/skills/

~/.codebuddy/skills/

Codex

codex

.agents/skills/

~/.codex/skills/

Command Code

command-code

.commandcode/skills/

~/.commandcode/skills/

Continue

continue

.continue/skills/

~/.continue/skills/

Cortex Code

cortex

.cortex/skills/

~/.snowflake/cortex/skills/

Crush

crush

.crush/skills/

~/.config/crush/skills/

Cursor

cursor

.agents/skills/

~/.cursor/skills/

Deep Agents

deepagents

.agents/skills/

~/.deepagents/agent/skills/

Droid

droid

.factory/skills/

~/.factory/skills/

Firebender

firebender

.agents/skills/

~/.firebender/skills/

Gemini CLI

gemini-cli

.agents/skills/

~/.gemini/skills/

GitHub Copilot

github-copilot

.agents/skills/

~/.copilot/skills/

Goose

goose

.goose/skills/

~/.config/goose/skills/

Junie

junie

.junie/skills/

~/.junie/skills/

iFlow CLI

iflow-cli

.iflow/skills/

~/.iflow/skills/

Kilo Code

kilo

.kilocode/skills/

~/.kilocode/skills/

Kiro CLI

kiro-cli

.kiro/skills/

~/.kiro/skills/

Kode

kode

.kode/skills/

~/.kode/skills/

MCPJam

mcpjam

.mcpjam/skills/

~/.mcpjam/skills/

Mistral Vibe

mistral-vibe

.vibe/skills/

~/.vibe/skills/

Mux

mux

.mux/skills/

~/.mux/skills/

OpenCode

opencode

.agents/skills/

~/.config/opencode/skills/

OpenHands

openhands

.openhands/skills/

~/.openhands/skills/

Pi

pi

.pi/skills/

~/.pi/agent/skills/

Qoder

qoder

.qoder/skills/

~/.qoder/skills/

Qwen Code

qwen-code

.qwen/skills/

~/.qwen/skills/

Roo Code

roo

.roo/skills/

~/.roo/skills/

Trae

trae

.trae/skills/

~/.trae/skills/

Trae CN

trae-cn

.trae/skills/

~/.trae-cn/skills/

Windsurf

windsurf

.windsurf/skills/

~/.codeium/windsurf/skills/

Zencoder

zencoder

.zencoder/skills/

~/.zencoder/skills/

Neovate

neovate

.neovate/skills/

~/.neovate/skills/

Pochi

pochi

.pochi/skills/

~/.pochi/skills/

AdaL

adal

.adal/skills/

~/.adal/skills/

Note

Kiro CLI users:After installing skills, manually add them to your custom agent'sresourcesin.kiro/agents/<agent>.json:

{
 
"resources"
: [
"
skill://.kiro/skills/**/SKILL.md
"
]
}

The CLI automatically detects which coding agents you have installed. If none are detected, you'll be prompted to select
which agents to install to.

## Creating Skills

Skills are directories containing aSKILL.mdfile with YAML frontmatter:

---

name
: 
my-skill

description
: 
What this skill does and when to use it

---

# 
My Skill

Instructions for the agent to follow when this skill is activated.

## 
When to Use

Describe the scenarios where this skill should be used.

## 
Steps

1
.
 First, do this

2
.
 Then, do that

### Required Fields

* name: Unique identifier (lowercase, hyphens allowed)
* description: Brief explanation of what the skill does

### Optional Fields

* metadata.internal: Set totrueto hide the skill from normal discovery. Internal skills are only visible and
installable whenINSTALL_INTERNAL_SKILLS=1is set. Useful for work-in-progress skills or skills meant only for
internal tooling.

---

name
: 
my-internal-skill

description
: 
An internal skill not shown by default

metadata
:
 
internal
: 
true

---

### Skill Discovery

The CLI searches for skills in these locations within a repository:

* Root directory (if it containsSKILL.md)
* skills/
* skills/.curated/
* skills/.experimental/
* skills/.system/
* .agents/skills/
* .augment/skills/
* .bob/skills/
* .claude/skills/
* ./skills/
* .codebuddy/skills/
* .commandcode/skills/
* .continue/skills/
* .cortex/skills/
* .crush/skills/
* .factory/skills/
* .goose/skills/
* .junie/skills/
* .iflow/skills/
* .kilocode/skills/
* .kiro/skills/
* .kode/skills/
* .mcpjam/skills/
* .vibe/skills/
* .mux/skills/
* .openhands/skills/
* .pi/skills/
* .qoder/skills/
* .qwen/skills/
* .roo/skills/
* .trae/skills/
* .windsurf/skills/
* .zencoder/skills/
* .neovate/skills/
* .pochi/skills/
* .adal/skills/

### Plugin Manifest Discovery

If.claude-plugin/marketplace.jsonor.claude-plugin/plugin.jsonexists, skills declared in those files are also discovered:

// .claude-plugin/marketplace.json

{
 
"metadata"
: { 
"pluginRoot"
: 
"
./plugins
"
 },
 
"plugins"
: [
 {
 
"name"
: 
"
my-plugin
"
,
 
"source"
: 
"
my-plugin
"
,
 
"skills"
: [
"
./skills/review
"
, 
"
./skills/test
"
]
 }
 ]
}

This enables compatibility with theClaude Code plugin marketplaceecosystem.

If no skills are found in standard locations, a recursive search is performed.

## Compatibility

Skills are generally compatible across agents since they follow a
sharedAgent Skills specification. However, some features may be agent-specific:

Feature

OpenCode

OpenHands

Claude Code

Cline

CodeBuddy

Codex

Command Code

Kiro CLI

Cursor

Antigravity

Roo Code

Github Copilot

Amp

OpenClaw

Neovate

Pi

Qoder

Zencoder

Basic skills

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

allowed-tools

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

context: fork

No

No

Yes

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

Hooks

No

No

Yes

Yes

No

No

No

No

No

No

No

No

No

No

No

No

No

No

## Troubleshooting

### "No skills found"

Ensure the repository contains validSKILL.mdfiles with bothnameanddescriptionin the frontmatter.

### Skill not loading in agent

* Verify the skill was installed to the correct path
* Check the agent's documentation for skill loading requirements
* Ensure theSKILL.mdfrontmatter is valid YAML

### Permission errors

Ensure you have write access to the target directory.

## Environment Variables

Variable

Description

INSTALL_INTERNAL_SKILLS

Set to 
1
 or 
true
 to show and install skills marked as 
internal: true

DISABLE_TELEMETRY

Set to disable anonymous usage telemetry

DO_NOT_TRACK

Alternative way to disable telemetry

#
 Install internal skills

INSTALL_INTERNAL_SKILLS=1 npx skills add vercel-labs/agent-skills --list

## Telemetry

This CLI collects anonymous usage data to help improve the tool. No personal information is collected.

Telemetry is automatically disabled in CI environments.

## Related Links

* Agent Skills Specification
* Skills Directory
* Amp Skills Documentation
* Antigravity Skills Documentation
* Factory AI / Droid Skills Documentation
* Claude Code Skills Documentation
* OpenClaw Skills Documentation
* Cline Skills Documentation
* CodeBuddy Skills Documentation
* Codex Skills Documentation
* Command Code Skills Documentation
* Crush Skills Documentation
* Cursor Skills Documentation
* Firebender Skills Documentation
* Gemini CLI Skills Documentation
* GitHub Copilot Agent Skills
* iFlow CLI Skills Documentation
* Kimi Code CLI Skills Documentation
* Kiro CLI Skills Documentation
* Kode Skills Documentation
* OpenCode Skills Documentation
* Qwen Code Skills Documentation
* OpenHands Skills Documentation
* Pi Skills Documentation
* Qoder Skills Documentation
* Replit Skills Documentation
* Roo Code Skills Documentation
* Trae Skills Documentation
* Vercel Agent Skills Repository

## License

MIT

## About

The open agent skills tool - npx skills

skills.sh

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

15.4k

 stars
 

### Watchers

53

 watching
 

### Forks

1.3k

 forks
 

 Report repository

 

## Releases25

v1.5.1

 Latest

 

Apr 17, 2026

 

+ 24 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript90.5%
* JavaScript9.5%