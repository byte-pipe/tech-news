---
title: 'GitHub - vercel-labs/agent-browser: Browser automation CLI for AI agents · GitHub'
url: https://github.com/vercel-labs/agent-browser
site_name: github
content_file: github-github-vercel-labsagent-browser-browser-automation
fetched_at: '2026-11-06T12:28:13.304005'
original_url: https://github.com/vercel-labs/agent-browser
author: vercel-labs
description: Browser automation CLI for AI agents. Contribute to vercel-labs/agent-browser development by creating an account on GitHub.
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

810 Commits
810 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills/
technical-writer
.agents/
skills/
technical-writer
 
 
.claude-plugin
.claude-plugin
 
 
.github
.github
 
 
.husky
.husky
 
 
benchmarks
benchmarks
 
 
bin
bin
 
 
cli
cli
 
 
docker
docker
 
 
docs
docs
 
 
evals
evals
 
 
examples
examples
 
 
packages
packages
 
 
patches
patches
 
 
scripts
scripts
 
 
skill-data
skill-data
 
 
skills/
agent-browser
skills/
agent-browser
 
 
test
test
 
 
.claude
.claude
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.node-version
.node-version
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
agent-browser.schema.json
agent-browser.schema.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
View all files

## Repository files navigation

# agent-browser

Browser automation for AI agents: open pages, read them as an accessibility tree, and act on elements from the shell.

agent-browser is a native Rust CLI that gives an AI agent a browser it can drive one command at a time.snapshotreturns the page as compact text with a ref such as@e1for each element. The agent acts on a ref, reads the page again to check the result, and repeats. The browser stays open between commands, so each step is one short shell call.

## Install

npm install -g agent-browser
agent-browser install 
#
 download Chrome for Testing (first time only)

* Homebrew:brew install agent-browser, thenagent-browser install.
* Linux:agent-browser install --with-depsalso installs the browser's system libraries.
* No install:npx agent-browser open example.com.

Project installs, building from source,upgrade, anddoctorare covered inInstallation.

## Quick start

agent-browser open example.com
agent-browser snapshot -i 
#
 interactive elements, each with a ref

agent-browser click @e1 
#
 act on a ref from that snapshot

agent-browser get url 
#
 check the result

agent-browser close

The snapshot forexample.com:

- link "Learn more" [ref=e1]

* Refs describe the page at the time of the snapshot. After navigation or a DOM change, take a new snapshot before using refs again.
* CSS selectors, text, XPath, and semantic locators also work, for exampleagent-browser find role button click --name "Submit". SeeSelectors.
* A click fails, instead of reporting success, when the target is hidden, disabled, outside the viewport, or covered by another element such as a consent banner. Dismiss the covering element, take a new snapshot, and retry.

The full walkthrough is in thequick start.

## How it works

The CLI sends each command to a background daemon that starts on the first command and controls the browser over the Chrome DevTools Protocol. Each--sessiongets its own daemon and browser. By default, the daemon closes a headless browser and exits after one hour without commands, saving state first whensession persistenceis configured.

Chrome for Testing is the default browser. You can also attach to a running Chrome with--cdpor--auto-connect(CDP mode), select theLightpandaorObscuraengine with--engine, drive Mobile Safari in theiOS Simulator, or use a cloud browser provider such asBrowserbase,Browserless,Browser Use,Kernel, orAgentCore.

## For AI agents

The CLI ships skills that match its version:

agent-browser skills get core 
#
 the core loop, refs, waiting, and common workflows

agent-browser skills get core --ref commands 
#
 one reference, such as the full command list

agent-browser skills get core --full 
#
 adds the full command reference and templates

agent-browser skills list 
#
 specialized skills: electron, slack, dogfood, and more

Install the discovery skill into an agent harness fromskills.sh:

npx skills add vercel-labs/agent-browser

The installed skill is a thin stub that tells the agent to loadagent-browser skills get core, so its instructions always match the installed CLI. Or add this to yourAGENTS.md:

Use 
`
agent-browser
`
 for browser automation. Before the first use, run

`
agent-browser skills get core
`
 and follow it.

For MCP clients,agent-browser mcpstarts an MCP server over stdio. SeeMCP server.

## Commands

Runagent-browser --helpfor the full list, oragent-browser <command> --helpfor one command.

Group

Commands

Docs

Navigate and read

open
, 
back
, 
forward
, 
reload
, 
read
, 
snapshot
, 
get
, 
is

Core
, 
Snapshots

Interact

click
, 
dblclick
, 
fill
, 
type
, 
press
, 
keyboard
, 
hover
, 
focus
, 
select
, 
check
, 
uncheck
, 
scroll
, 
drag
, 
upload
, 
mouse
, 
find

Core
, 
Find elements

Wait

wait

Wait

Capture

screenshot
, 
pdf
, 
record
, 
download
, 
diff

Recording
, 
Diffing
, 
Files

Page and network state

cookies
, 
storage
, 
network
, 
set
, 
clipboard
, 
eval
, 
pushstate

Network
, 
Settings

Tabs, frames, and dialogs

tab
, 
frame
, 
dialog

Tabs and frames

Debug and performance

console
, 
errors
, 
highlight
, 
inspect
, 
trace
, 
profiler
, 
vitals
, 
react
, 
a11y

Debugging
, 
Profiler
, 
React

Sessions and auth

session
, 
state
, 
auth
, 
profiles
, 
confirm
, 
deny

Sessions
, 
Security

Agents and integrations

skills
, 
mcp
, 
webmcp
, 
flow
, 
chat
, 
batch
, 
plugin

Skills
, 
WebMCP
, 
Plugins

Observe

stream
, 
dashboard

Streaming
, 
Dashboard

Setup

install
, 
upgrade
, 
doctor
, 
connect
, 
close

Installation

Flags, environment variables, andagent-browser.jsonare documented inConfiguration.

## Platforms

Native binaries ship for macOS (ARM64, x64), Linux (ARM64, x64, glibc and musl), and Windows (x64). The npm package picks the right binary for the host.

## Development

Building from source requires Node.js 24 or later, pnpm 11 or later, and Rust:

pnpm install
pnpm build:source 
#
 builds the dashboard and the native CLI

pnpm link --global
agent-browser install

Run the Rust checks fromcli/:

cargo fmt -- --check
cargo clippy
cargo 
test

cargo 
test
 e2e -- --ignored --test-threads=1 
#
 launches real headless Chrome

AGENTS.mdlists the files to update with each change, the docs checks, and the release process.

## Documentation

* agent-browser.dev: introduction, guides, and reference
* CommandsandConfiguration
* Security: the auth vault, domain allowlists, action policies, and content boundaries
* Next.js and Vercelandeve: running agent-browser in Vercel Sandbox and eve agents
* Changelog

## License

Apache-2.0