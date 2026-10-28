---
title: GitHub - elayadesign/ai-design-skills · GitHub
url: https://github.com/elayadesign/ai-design-skills
site_name: github
content_file: github-github-elayadesignai-design-skills-github
fetched_at: '2026-10-28T12:07:55.144960'
original_url: https://github.com/elayadesign/ai-design-skills
author: elayadesign
description: Contribute to elayadesign/ai-design-skills development by creating an account on GitHub.
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

8 Commits
8 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
skills/
landing-page-design
skills/
landing-page-design
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# AI Design Skills

A growing collection of design skills for AI coding tools — Claude Code, Cursor, Codex, Windsurf, and anything else that reads a markdown rules file.

Each skill is a self-contained folder. Install the ones you need.

## Skills

Skill

What it does

landing-page-design

Builds a landing page from scratch — intake questions, page structure, conversion copy, plus a full visual system (type, spacing, radius, motion)

More on the way.Upgrading an existing site instead of building new?That one lives in its own repo since it predates this collection.

## Install

Pick a skill from the table above, then swap<skill-name>below for its folder name.

Claude Code

mkdir -p .claude/skills
git clone https://github.com/elayadesign/ai-design-skills.git /tmp/ai-design-skills
cp -r /tmp/ai-design-skills/skills/
<
skill-name
>
 .claude/skills/

Then just ask, in plain language, for what that skill covers.

Cursor

mkdir -p .cursor/rules
curl -o .cursor/rules/
<
skill-name
>
.md \
 https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/
<
skill-name
>
/SKILL.md

Or paste the file intoSettings → Rules for AI.

Codex / Windsurf / other

Copy the skill'sSKILL.mdinto whatever your tool uses for project rules:

Tool

Path

Codex

AGENTS.md

Windsurf

.windsurfrules

Cline

.clinerules

Generic

paste into your system prompt

Claude.ai (no terminal)

Download the skill'sSKILL.mdand upload it to a Project, or attach it to a chat and say"follow this."

## Make it yours

Every skill's design values (fonts, colors, spacing, motion) live in one section near the bottom of its file. Fork this repo, edit that section, and the rest of the skill follows automatically.

## Credits

landing-page-designadapts content realism and motion ideas fromLeonxlnx/taste-skillby Leon Lin, MIT licensed. Details are at the end ofits SKILL.md.

## License

MIT. Use it, fork it, ship it, sell what you build with it. No attribution needed.