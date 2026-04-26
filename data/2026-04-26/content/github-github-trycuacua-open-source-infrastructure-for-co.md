---
title: 'GitHub - trycua/cua: Open-source infrastructure for Computer-Use Agents. Sandboxes, SDKs, and benchmarks to train and evaluate AI agents that can control full desktops (macOS, Linux, Windows). · GitHub'
url: https://github.com/trycua/cua
site_name: github
content_file: github-github-trycuacua-open-source-infrastructure-for-co
fetched_at: '2026-04-26T11:38:20.957485'
original_url: https://github.com/trycua/cua
author: trycua
description: Open-source infrastructure for Computer-Use Agents. Sandboxes, SDKs, and benchmarks to train and evaluate AI agents that can control full desktops (macOS, Linux, Windows). - trycua/cua
---

trycua

 

/

cua

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork883
* Star14.2k

 
 
 
 
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

3,178 Commits
3,178 Commits
.github
.github
 
 
.vscode
.vscode
 
 
blog
blog
 
 
changelog
changelog
 
 
demo
demo
 
 
docs
docs
 
 
examples
examples
 
 
img
img
 
 
libs
libs
 
 
notebooks
notebooks
 
 
scripts
scripts
 
 
skills/
gui-automation
skills/
gui-automation
 
 
tests
tests
 
 
.cursorignore
.cursorignore
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.lycheeignore
.lycheeignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.prettierignore
.prettierignore
 
 
.prettierrc.yaml
.prettierrc.yaml
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Development.md
Development.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE.md
LICENSE.md
 
 
Makefile
Makefile
 
 
Package.swift
Package.swift
 
 
README.md
README.md
 
 
TESTING.md
TESTING.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pyproject.toml
pyproject.toml
 
 
pyrightconfig.json
pyrightconfig.json
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

Build, benchmark, and deploy agents that use computers

## Choose Your Path

## Cua Driver - Background computer-use on macOS

Drive any native macOS appin the background— agents click, type, and verify without stealing the cursor, focus, or Space, even on non-AX surfaces like Chromium web content and canvas-based tools (Blender, Figma, DAWs, game engines). Use with the CLI or MCP server for Claude Code, Cursor, and custom clients. Every session records as a replayable trajectory.

/bin/bash -c 
"
$(
curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh
)
"

Full tool reference, architecture notes, and the Claude Code skill ship with the package:libs/cua-driver/README.md.

## Cua - Agent-Ready Sandboxes for Any OS

Build agents that see screens, click buttons, and complete tasks autonomously. One API for any VM or container image — cloud or local.

pip install cua

# Requires Python 3.11 or later

from
 
cua
 
import
 
Sandbox
, 
Image

# Same API regardless of OS or runtime

async
 
with
 
Sandbox
.
ephemeral
(
Image
.
linux
()) 
as
 
sb
: 
# or .macos() .windows() .android()

 
result
 
=
 
await
 
sb
.
shell
.
run
(
"echo hello"
)
 
screenshot
 
=
 
await
 
sb
.
screenshot
()
 
await
 
sb
.
mouse
.
click
(
100
, 
200
)
 
await
 
sb
.
keyboard
.
type
(
"Hello from Cua!"
)
 
await
 
sb
.
mobile
.
gesture
((
100
, 
500
), (
100
, 
200
)) 
# multi-touch gestures

Linux container

Linux VM

macOS

Windows

Android

BYOI (.qcow2, .iso)

Cloud (cua.ai)

✅

✅

✅

✅

✅

🔜 soon

Local (QEMU)

✅

✅

✅

✅

✅

✅

Get Started|Examples|API Reference

## CuaBot - Co-op computer-use for any agent

cuabotgives any coding agent a seamless sandbox for computer-use. Individual windows appear natively on your desktop with H.265, shared clipboard, and audio.

npx cuabot 
#
 Setup onboarding

#
 Run any agent in a sandbox

cuabot claude 
#
 Claude Code

cuabot openclaw 
#
 OpenClaw in the sandbox

#
 Run any GUI workflow in a sandbox

cuabot chromium
cuabot --screenshot
cuabot --type 
"
hello
"

cuabot --click 
<
x
>
 
<
y
>
 [button]

Built-in support foragent-browserandagent-device(iOS, Android) out of the box.

Get Started|Installation| First spotted atClawCon

## Cua-Bench - Benchmarks & RL Environments

Evaluate computer-use agents on OSWorld, ScreenSpot, Windows Arena, and custom tasks. Export trajectories for training.

#
 Install and create base image

cd
 cua-bench
uv tool install -e 
.
 
&&
 cb image create linux-docker

#
 Run benchmark with agent

cb run dataset datasets/cua-bench-basic --agent cua-agent --max-parallel 4

Get Started|Partner With Us|Registry|CLI Reference

## Lume - macOS Virtualization

Create and manage macOS/Linux VMs with near-native performance on Apple Silicon using Apple's Virtualization.Framework.

#
 Install Lume

/bin/bash -c 
"
$(
curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh
)
"

#
 Pull & start a macOS VM

lume run macos-sequoia-vanilla:latest

Get Started|FAQ|CLI Reference

## Packages

Package

Description

cuabot

Multi-agent computer-use sandbox CLI

cua-agent

AI agent framework for computer-use tasks

cua-sandbox

SDK for creating and controlling sandboxes

cua-computer-server

Driver for UI interactions and code execution in sandboxes

cua-bench

Benchmarks and RL environments for computer-use

lume

macOS/Linux VM management on Apple Silicon

lumier

Docker-compatible interface for Lume VMs

## Resources

* Documentation— Guides, examples, and API reference
* Blog— Tutorials, updates, and research
* Discord— Community support and discussions
* GitHub Issues— Bug reports and feature requests

## Contributing

We welcome contributions! See ourContributing Guidelinesfor details.

## License

MIT License — seeLICENSEfor details.

Third-party components have their own licenses:

* Kasm(MIT)
* OmniParser(CC-BY-4.0)
* Optionalcua-agent[omni]includes ultralytics (AGPL-3.0)

## Trademarks

Apple, macOS, Ubuntu, Canonical, and Microsoft are trademarks of their respective owners. This project is not affiliated with or endorsed by these companies.

Thank you to all ourGitHub Sponsors!

## About

Open-source infrastructure for Computer-Use Agents. Sandboxes, SDKs, and benchmarks to train and evaluate AI agents that can control full desktops (macOS, Linux, Windows).

cua.ai

### Topics

 windows

 macos

 swift

 agent

 apple

 virtualization

 operator

 desktop-automation

 hacktoberfest

 containerization

 cua

 manus

 lume

 windows-sandbox

 virtualization-framework

 ai-agent

 computer-use

 computer-use-agent

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

14.2k

 stars
 

### Watchers

53

 watching
 

### Forks

883

 forks
 

 Report repository

 

## Releases465

cua-driver-v0.0.7

 Latest

 

Apr 26, 2026

 

+ 464 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* HTML67.5%
* Python20.2%
* Swift6.6%
* TypeScript2.9%
* Shell1.7%
* JavaScript0.4%
* Other0.7%