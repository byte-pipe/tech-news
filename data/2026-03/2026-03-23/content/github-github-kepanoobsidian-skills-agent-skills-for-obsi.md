---
title: 'GitHub - kepano/obsidian-skills: Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI. · GitHub'
url: https://github.com/kepano/obsidian-skills
site_name: github
content_file: github-github-kepanoobsidian-skills-agent-skills-for-obsi
fetched_at: '2026-03-23T11:21:16.814700'
original_url: https://github.com/kepano/obsidian-skills
author: kepano
description: Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI. - kepano/obsidian-skills
---

kepano



/

obsidian-skills

Public

* NotificationsYou must be signed in to change notification settings
* Fork925
* Star16k




 
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

35 Commits
35 Commits
.claude-plugin
.claude-plugin
 
 
skills
skills
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

Agent Skills for use with Obsidian.

These skills follow theAgent Skills specificationso they can be used by any skills-compatible agent, including Claude Code and Codex CLI.

## Installation

### Marketplace

/plugin marketplace add kepano/obsidian-skills
/plugin install obsidian@obsidian-skills

### npx skills

npx skills add git@github.com:kepano/obsidian-skills.git

### Manually

#### Claude Code

Add the contents of this repo to a/.claudefolder in the root of your Obsidian vault (or whichever folder you're using with Claude Code). See more in theofficial Claude Skills documentation.

#### Codex CLI

Copy theskills/directory into your Codex skills path (typically~/.codex/skills). See theAgent Skills specificationfor the standard skill format.

#### OpenCode

Clone the entire repo into the OpenCode skills directory (~/.opencode/skills/):

git clone https://github.com/kepano/obsidian-skills.git
~
/.opencode/skills/obsidian-skills

Do not copy only the innerskills/folder — clone the full repo so the directory structure is~/.opencode/skills/obsidian-skills/skills/<skill-name>/SKILL.md.

OpenCode auto-discovers allSKILL.mdfiles under~/.opencode/skills/. No changes toopencode.jsonor any config file are needed. Skills become available after restarting OpenCode.

## Skills

Skill

Description

obsidian-markdown

Create and edit
Obsidian Flavored Markdown
 (
.md
) with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax

obsidian-bases

Create and edit
Obsidian Bases
 (
.base
) with views, filters, formulas, and summaries

json-canvas

Create and edit
JSON Canvas
 files (
.canvas
) with nodes, edges, groups, and connections

obsidian-cli

Interact with Obsidian vaults via the
Obsidian CLI
 including plugin and theme development

defuddle

Extract clean markdown from web pages using
Defuddle
, removing clutter to save tokens

## About

Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI.

### Topics

 cli

 skills

 opencode

 obsidian

 codex

 claude

 defuddle

 clawdbot

 openclaw

### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

16k

 stars


### Watchers

117

 watching


### Forks

925

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors12
