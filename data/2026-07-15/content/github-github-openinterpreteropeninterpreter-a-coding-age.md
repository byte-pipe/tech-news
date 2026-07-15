---
title: 'GitHub - openinterpreter/openinterpreter: A coding agent for low-cost models · GitHub'
url: https://github.com/openinterpreter/openinterpreter
site_name: github
content_file: github-github-openinterpreteropeninterpreter-a-coding-age
fetched_at: '2026-07-15T11:32:57.115383'
original_url: https://github.com/openinterpreter/openinterpreter
author: openinterpreter
description: A coding agent for low-cost models. Contribute to openinterpreter/openinterpreter development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 openinterpreter

 

/

openinterpreter

Public

* NotificationsYou must be signed in to change notification settings
* Fork5.6k
* Star65.1k

 
 
 
 
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

8,360 Commits
8,360 Commits
.codex
.codex
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.vscode
.vscode
 
 
bazel
bazel
 
 
codex-cli
codex-cli
 
 
codex-rs
codex-rs
 
 
docs-site
docs-site
 
 
docs
docs
 
 
logo
logo
 
 
patches
patches
 
 
scripts
scripts
 
 
sdk
sdk
 
 
third_party
third_party
 
 
tools
tools
 
 
.bazelignore
.bazelignore
 
 
.bazelrc
.bazelrc
 
 
.bazelversion
.bazelversion
 
 
.codespellignore
.codespellignore
 
 
.codespellrc
.codespellrc
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.markdownlint-cli2.yaml
.markdownlint-cli2.yaml
 
 
.mintignore
.mintignore
 
 
.npmrc
.npmrc
 
 
.prettierignore
.prettierignore
 
 
.prettierrc.toml
.prettierrc.toml
 
 
.worktreeinclude
.worktreeinclude
 
 
AGENTS.md
AGENTS.md
 
 
BUILD.bazel
BUILD.bazel
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
MODULE.bazel
MODULE.bazel
 
 
MODULE.bazel.lock
MODULE.bazel.lock
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
announcement_tip.toml
announcement_tip.toml
 
 
defs.bzl
defs.bzl
 
 
docs.json
docs.json
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
justfile
justfile
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
rbe.bzl
rbe.bzl
 
 
style.css
style.css
 
 
workspace_root_test_launcher.bat.tpl
workspace_root_test_launcher.bat.tpl
 
 
workspace_root_test_launcher.sh.tpl
workspace_root_test_launcher.sh.tpl
 
 
View all files

## Repository files navigation

# Open Interpreter

A coding agent optimized for low-cost models.Blog post ↗

### Installation

macOS and Linux:

curl -fsSL https://www.openinterpreter.com/install 
|
 sh

Windows:

irm https:
//
www.openinterpreter.com
/
install.ps1 
|
 iex

Then typeiorinterpreterin your terminal to start a session.

### Harness Emulation

Open Interpreter is a fork of OpenAI's Codex, with a focus on emulating the agent harness that gets the best performance out of low-cost models.

Use/harnessto switch the active harness:

> /harness

native
claude-code
claude-code-bare
zcode
kimi-cli
qwen-code
deepseek-tui
swe-agent
minimal

Read more in theharness docsandmodel provider docs.

### Computer Use

Open Interpreter ships with a QA skill that lets any model operate and test interfaces. It can drive web apps in a real browser withagent-browser, or operate and test native apps withtrycua.

### Features

* Runs commands inside native sandboxing on macOS, Linux, and Windows.
* Switches providers and models from the TUI with/model.
* Inspects or switches Rust-native model harnesses with/harness.
* Tests web and native apps through the built-in QA skill.
* Runs as anAgent Client Protocolagent for editors withinterpreter acp.
* Keeps config and session state local under~/.openinterpreter.
* Supportsexec, MCP, skills, hooks, permissions, andAGENTS.md.

### Documentation

* Terminal docs
* Quickstart
* Install guide
* Configuration
* CLI reference
* Harnesses
* Model providers
* Sandbox & approvals

Note

This is the new Rust version of Open Interpreter, based on Codex. Looking for the original Python project? It lives on as a community-maintained fork atendolith/open-interpreter.

### License

Apache-2.0

## About

A coding agent for low-cost models

openinterpreter.com/

### Topics

 rust

 acp

 kimi

 qwen

 deepseek

 coding-agent

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

65.1k

 stars
 

### Watchers

462

 watching
 

### Forks

5.6k

 forks
 

 Report repository

 

## Releases55

Open Interpreter 0.0.24

 Latest

 

Jul 14, 2026

 

+ 54 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust96.6%
* Python2.6%
* Starlark0.2%
* TypeScript0.2%
* Shell0.2%
* PowerShell0.1%
* Other0.1%