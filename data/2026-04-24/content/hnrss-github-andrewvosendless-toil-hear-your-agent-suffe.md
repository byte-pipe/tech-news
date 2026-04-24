---
title: 'GitHub - AndrewVos/endless-toil: Hear your agent suffer through your code · GitHub'
url: https://github.com/AndrewVos/endless-toil
site_name: hnrss
content_file: hnrss-github-andrewvosendless-toil-hear-your-agent-suffe
fetched_at: '2026-04-24T19:51:27.488514'
original_url: https://github.com/AndrewVos/endless-toil
date: '2026-04-24'
description: Hear your agent suffer through your code. Contribute to AndrewVos/endless-toil development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

AndrewVos

 

/

endless-toil

Public

* NotificationsYou must be signed in to change notification settings
* Fork1
* Star110

 
 
 
 
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

20 Commits
20 Commits
.agents/
plugins
.agents/
plugins
 
 
.claude-plugin
.claude-plugin
 
 
.cursor-plugin
.cursor-plugin
 
 
assets
assets
 
 
plugins/
endless-toil
plugins/
endless-toil
 
 
.gitignore
.gitignore
 
 
README.md
README.md
 
 
regenerate-sounds.sh
regenerate-sounds.sh
 
 
View all files

## Repository files navigation

# Endless Toil

Hear your agent suffer through your code.

Endless Toil runs alongside your coding agent in real time, playing escalating recorded human groans as the code it reads starts to look more cursed.

Note: installing the plugin does not make it auto-activate in every thread by default. Start a new thread and ask Codex or Claude to useEndless Toil.

## Demo

## Use In Codex Desktop

Clone this repository somewhere on your machine, then open that directory in Codex Desktop.

1. OpenPlugins.
2. Search or browse forEndless Toil, then open its details.
3. Select the plus button orAdd to Codex.
4. If prompted, complete any setup steps.
5. Start a new thread and ask Codex to useEndless Toil.

## Use In Codex CLI

From Codex CLI, add this repository as a local marketplace root:

codex plugin marketplace add ./

Then open the plugin browser:

/plugins

Choose theEndless Toilmarketplace, installEndless Toil, restart Codex if needed, and invoke the plugin or its bundled skill from a new thread.

## Use In Claude CLI

Clone this repository somewhere on your machine, then start Claude from this repository root.

Add this repository as a local plugin marketplace:

/plugin marketplace add ./

Then install the plugin:

/plugin install endless-toil@endless-toil

Restart Claude Code if prompted, then invoke the bundled skill:

/endless-toil

## Use In Cursor

Clone this repository somewhere on your machine, then add it as a local Cursor plugin marketplace from Cursor.

InstallEndless Toil, restart Cursor if prompted, then ask Cursor Agent to use the bundled skill:

Use endless-toil while reading this code.

## Test Sounds

From this repository root:

python3 plugins/endless-toil/skills/endless-toil/scripts/test_sounds.py --list
python3 plugins/endless-toil/skills/endless-toil/scripts/test_sounds.py groan wail abyss

## Requirements

* Python 3.10+
* A local audio player:afplayon macOS, orpaplay,aplay, orffplayon Linux

If an audio player is unavailable, Endless Toil still prints scan results, but it will not play sounds.

## Source

Plugin structure and marketplace layout follow the OpenAI Codex and Claude Code plugin docs:

https://developers.openai.com/codex/pluginshttps://code.claude.com/docs/en/pluginshttps://github.com/cursor/plugins

## About

Hear your agent suffer through your code

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

110

 stars
 

### Watchers

0

 watching
 

### Forks

1

 fork
 

 Report repository

 

## Contributors1

* AndrewVosAndrew Vos

## Languages

* Python90.0%
* Shell10.0%