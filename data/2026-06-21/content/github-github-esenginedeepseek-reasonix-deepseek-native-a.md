---
title: 'GitHub - esengine/DeepSeek-Reasonix: DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running. · GitHub'
url: https://github.com/esengine/DeepSeek-Reasonix
site_name: github
content_file: github-github-esenginedeepseek-reasonix-deepseek-native-a
fetched_at: '2026-06-21T11:56:44.910885'
original_url: https://github.com/esengine/DeepSeek-Reasonix
author: esengine
description: DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running. - esengine/DeepSeek-Reasonix
---

esengine

 

/

DeepSeek-Reasonix

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star23.5k

 
 
 
 
main-v2
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

1,546 Commits
1,546 Commits
.githooks
.githooks
 
 
.github
.github
 
 
.reasonix/
commands
.reasonix/
commands
 
 
.signpath/
artifact-configurations
.signpath/
artifact-configurations
 
 
benchmarks
benchmarks
 
 
cmd
cmd
 
 
desktop
desktop
 
 
docs
docs
 
 
internal
internal
 
 
npm
npm
 
 
scripts
scripts
 
 
site
site
 
 
tools/
write_heartbeat
tools/
write_heartbeat
 
 
workers/
crash-report
workers/
crash-report
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
.goreleaser.yaml
.goreleaser.yaml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
REASONIX.md
REASONIX.md
 
 
dev
dev
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
prod_test
prod_test
 
 
reasonix.example.toml
reasonix.example.toml
 
 
View all files

## Repository files navigation

English·简体中文·Guide·Spec·Website·Discord

Important

Reasonix 1.0 is a ground-up rewrite in Go— this branch (main-v2) is the new default and where development happens now.
The earlier0.xTypeScript releases arelegacy, living on thev1branch (maintenance only).
See themigration guide.npm i -g reasonixstays the install command —1.0.0+ delivers the Go binary,0.xis the legacy TS build.

### A DeepSeek-native AI coding agent for your terminal.

A config- and plugin-driven harness — a single static Go binary, tuned around DeepSeek's prefix cache so token costs stay low across long sessions.

Important

Community · 加入社区— bilingual Discord for setup help (#help/#求助), workflow showcases, and feature ideas. →https://discord.gg/XF78rEME2D

## Features

* Config-driven.Providers, the agent, enabled tools, and plugins are all
declared inreasonix.toml. No hardcoded models.
* Multi-model & composable.DeepSeek ships as a preset; any
OpenAI-compatible endpoint is a config entry, not new code. Optionally run
two models together (executor + planner) in separate, cache-stable sessions.
* Plugin-driven.External tools run as subprocesses over stdio JSON-RPC
(MCP-compatible). Built-in tools self-register at compile time.
* Zero-friction distribution.CGO_ENABLED=0single binary; cross-compile
to six targets with one command. The only dependency is a TOML parser.

## Install

npm i -g reasonix 
#
 any OS; pulls the prebuilt native binary

brew install esengine/reasonix/reasonix 
#
 macOS

Prebuilt archives (darwin|linux|windows × amd64|arm64) andSHA256SUMSare on
everyGitHub release.

### Code signing

Windows builds are code-signed with a free certificate provided by theSignPath Foundation, with signing throughSignPath.io.

### Build from source

make build 
#
 -> bin/reasonix(.exe)

make cross 
#
 -> dist/ (darwin|linux|windows × amd64|arm64)

## Quick start

reasonix setup 
#
 config wizard → ./reasonix.toml

export
 DEEPSEEK_API_KEY=sk-... 
#
 or let setup save it to the credential store

reasonix 
#
 then run /init to generate AGENTS.md (project memory)

reasonix run 
"
implement the TODOs in main.go
"

reasonix run --model deepseek-pro 
"
add unit tests for this function
"

echo
 
"
explain this code
"
 
|
 reasonix run

## Configuration

A minimalreasonix.toml— one provider and a default model — is enough to start:

default_model
 = 
"
deepseek-flash
"

[[
providers
]]

name
 = 
"
deepseek-flash
"

kind
 = 
"
openai
"

base_url
 = 
"
https://api.deepseek.com
"

model
 = 
"
deepseek-v4-flash
"

api_key_env
 = 
"
DEEPSEEK_API_KEY
"

Resolution order isflag >./reasonix.toml> the user config file >
built-in defaults; starting withReasonix v1.8.1, the user file lives at~/.reasonix/config.tomlon macOS/Linux and%AppData%\reasonix\config.tomlon Windows. SeeConfiguration pathsfor migration details. Secrets come from the environment viaapi_key_env, are
never written to config files, and new keys default to the OS credential store
with a Reasonix-owned file fallback. Project.envfiles are read as a
compatibility override, but Reasonix does not write new keys there. Permissions, the sandbox, plugins (MCP), slash
commands,@references, and two-model setup are all in theGuide.

## Documentation

* Guide— configuration, permissions & sandbox, plugins
(MCP), slash commands,@references, two-model collaboration.
* Bot guide— connect Feishu, Lark, and WeChat bots
from the desktop app, then use approvals, YOLO, and commands from IM.
* Spec— engineering contract: architecture, registries,
data types, and roadmap.
* Migrating from 0.x— moving from the legacy
TypeScript releases to the 1.0 Go rewrite.
* Checkpoints & rewind— the snapshot-based edit
safety net (Esc-Esc //rewind).

## Star History

## Support

If Reasonix has been useful and you'd like to say thanks, you can. It stays a coffee, not a contract — donations don't buy feature priority or change how issues get triaged.

* International— PayPal:paypal.me/yuhuahui
* 国内— 微信支付（扫码）

## Acknowledgments

A small list of folks whose work has shaped Reasonix the most — measured
by both commit count and code volume.Listed alphabetically, no ordering
of importance.The full contributor graph is onGitHub.

* ctharvey
* dimasd-angga(Dimas D. Angga)
* Evan-Pycraft
* ForeverYoungPp
* GTC2080(TaoMu)
* kabaka9527
* lisniuse(Richie)
* wade19990814-hue
* wviana(Wesley Viana)

Also a separate thank-you toBernardxu123for designing the project logo, and toAIGC Linkfor promoting the project on XiaoHongShu.

MIT — seeLICENSEBuilt by the community atesengine/DeepSeek-Reasonix

## About

DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

reasonix.io/

### Topics

 agent

 cli

 typescript

 terminal

 tui

 developer-tools

 ink

 r1

 tool-use

 agent-framework

 ai-agent

 llm

 prompt-caching

 deepseek

 ai-coding

 coding-agent

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

23.5k

 stars
 

### Watchers

65

 watching
 

### Forks

1.4k

 forks
 

 Report repository

 

## Releases59

Reasonix Desktop v1.10.0

 Latest

 

Jun 20, 2026

 

+ 58 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go66.8%
* TypeScript23.3%
* CSS7.6%
* HTML0.8%
* Astro0.7%
* JavaScript0.4%
* Other0.4%