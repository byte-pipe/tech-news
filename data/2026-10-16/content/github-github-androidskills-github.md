---
title: GitHub - android/skills · GitHub
url: https://github.com/android/skills
site_name: github
content_file: github-github-androidskills-github
fetched_at: '2026-10-16T15:12:08.544913'
original_url: https://github.com/android/skills
author: android
description: Contribute to android/skills development by creating an account on GitHub.
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

81 Commits
81 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
plugins
.agents/
plugins
 
 
.claude-plugin
.claude-plugin
 
 
.codex-plugin
.codex-plugin
 
 
.github
.github
 
 
build-system/
agp/
agp-9-upgrade
build-system/
agp/
agp-9-upgrade
 
 
camera/
camerax
camera/
camerax
 
 
cars/
android-for-cars-parked-apps
cars/
android-for-cars-parked-apps
 
 
device-ai
device-ai
 
 
devtools/
android-cli
devtools/
android-cli
 
 
identity
identity
 
 
jetpack-compose
jetpack-compose
 
 
media/
media3-cast-integration
media/
media3-cast-integration
 
 
navigation
navigation
 
 
performance/
r8-analyzer
performance/
r8-analyzer
 
 
play
play
 
 
profilers/
android-profiler
profilers/
android-profiler
 
 
security
security
 
 
system
system
 
 
testing/
testing-setup
testing/
testing-setup
 
 
tv/
leanback-to-compose-tv-migration
tv/
leanback-to-compose-tv-migration
 
 
wear
wear
 
 
xr/
display-glasses-with-jetpack-compose-glimmer
xr/
display-glasses-with-jetpack-compose-glimmer
 
 
LICENSE.txt
LICENSE.txt
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

## Android skills

Android skillsare a dedicated repository ofAI-optimized, modular instructionsand
resources, to help agents better understand and execute specific patterns that follow the best
practices and guidance on Android development
fromdeveloper.android.com.

Android skills follow theopen-standard agent skills- markdown
files (SKILL.md) that provide a technical specification of a task, andground LLMswith
information on specialized domains and workflows.

Our Android skill development focuses onuse cases and workflows where evaluations show LLMs
underperform.
We aren't prioritizing well-established areas where LLMs are already proficient, such
as basic Jetpack Compose best practices.

To learn more, read the official documentation:

* Android skills
* Android CLI
* Android Studio

### Install Android skills

Use Android CLI to install a specific skill into the current directory:

android skills add r8-analyzer --project=.

Use Android CLI to install all Android skills to directories for all detected agents:

android skills add --all

If you don't have any existing agent directories and don't specify particular agents, the skills
will be installed for Gemini and Antigravity at~/.gemini/antigravity/skills.

Options:

* --all- Add all Android skills. If omitted, only theandroid-cliskill will be installed.
* --agent- A comma-separated list of agents to install the skill for. If omitted, the skill will be installed for all detected agents.
* --project- Path to a project root in which to install the skills.

To update all skills or specific ones, run:

android skills update --all
android skills update wear-compose-m3

### Install as an agent plugin

Claude Code:

/plugin install android-skills --marketplace android/skills

Codex:

codex plugin marketplace add android/skills
codex plugin add android-skills@android-skills

### Activate skills

Your agent automatically activates skills that are relevant to your task. To use a skill, prompt your agent to complete a task that is related to the skill, for example "Make my app UI edge-to-edge." The agent should automatically find and use the skill if it has been installed.

## Disclaimer

AI can make mistakes, so always double-check the results.

## Contributing

Submit a GitHub issue to provide feedback, report issues, or make new skill requests and changes.

Public contributions are not accepted at this time.

## License

Android Skills is licensed under theApache License 2.0. See theLICENSE.txtfile
for
details.

## Review our community guidelines

This project followsGoogle's Open Source Community Guidelines.