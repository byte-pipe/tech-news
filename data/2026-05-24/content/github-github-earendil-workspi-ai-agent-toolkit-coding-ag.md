---
title: 'GitHub - earendil-works/pi: AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods · GitHub'
url: https://github.com/earendil-works/pi
site_name: github
content_file: github-github-earendil-workspi-ai-agent-toolkit-coding-ag
fetched_at: '2026-05-24T11:30:56.756428'
original_url: https://github.com/earendil-works/pi
author: earendil-works
description: 'AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods - earendil-works/pi'
---

earendil-works

 

/

pi

Public

* NotificationsYou must be signed in to change notification settings
* Fork6.4k
* Star53.6k

 
 
 
 
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

4,275 Commits
4,275 Commits
.github
.github
 
 
.husky
.husky
 
 
.pi
.pi
 
 
packages
packages
 
 
scripts
scripts
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
AGENTS.md
AGENTS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
pi-test.bat
pi-test.bat
 
 
pi-test.ps1
pi-test.ps1
 
 
pi-test.sh
pi-test.sh
 
 
test.sh
test.sh
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

pi.devdomain graciously donated byexe.dev

New issues and PRs from new contributors are auto-closed by default. Maintainers review auto-closed issues daily. SeeCONTRIBUTING.md.

# Pi Agent Harness Mono Repo

This is the home of the pi agent harness project including our self extensible coding agent.

* @earendil-works/pi-coding-agent: Interactive coding agent CLI
* @earendil-works/pi-agent-core: Agent runtime with tool calling and state management
* @earendil-works/pi-ai: Unified multi-provider LLM API (OpenAI, Anthropic, Google, …)

To learn more about pi:

* Visit pi.dev, the project website with demos
* Read the documentation, but you can also ask the agent to explain itself

## Share your OSS coding agent sessions

If you use pi or other coding agents for open source work, please share your sessions.

Public OSS session data helps improve coding agents with real-world tasks, tool use, failures, and fixes instead of toy benchmarks.

For the full explanation, seethis post on X.

To publish sessions, usebadlogic/pi-share-hf. Read its README.md for setup instructions. All you need is a Hugging Face account, the Hugging Face CLI, andpi-share-hf.

You can also watchthis video, where I show how I publish mypi-monosessions.

I regularly publish my ownpi-monowork sessions here:

* badlogicgames/pi-mono on Hugging Face

## All Packages

Package

Description

@earendil-works/pi-ai

Unified multi-provider LLM API (OpenAI, Anthropic, Google, etc.)

@earendil-works/pi-agent-core

Agent runtime with tool calling and state management

@earendil-works/pi-coding-agent

Interactive coding agent CLI

@earendil-works/pi-tui

Terminal UI library with differential rendering

For Slack/chat automation and workflows seeearendil-works/pi-chat.

## Contributing

SeeCONTRIBUTING.mdfor contribution guidelines andAGENTS.mdfor project-specific rules (for both humans and agents).

## Development

npm install --ignore-scripts 
#
 Install all dependencies without running lifecycle scripts

npm run build 
#
 Build all packages

npm run check 
#
 Lint, format, and type check

./test.sh 
#
 Run tests (skips LLM-dependent tests without API keys)

./pi-test.sh 
#
 Run pi from sources (can be run from any directory)

## Supply-chain hardening

We treat npm dependency changes as reviewed code changes.

* Direct external dependencies are pinned to exact versions. Internal workspace packages remain version-ranged.
* .npmrcsetssave-exact=trueandmin-release-age=2to avoid same-day dependency releases during npm resolution.
* package-lock.jsonis the dependency ground truth. Pre-commit blocks accidental lockfile commits unlessPI_ALLOW_LOCKFILE_CHANGE=1is set.
* npm run checkverifies pinned direct deps, native TypeScript import compatibility, and the generated coding-agent shrinkwrap.
* The published CLI package includespackages/coding-agent/npm-shrinkwrap.json, generated from the root lockfile, to pin transitive deps for npm users.
* Release smoke tests usenpm run release:localto build, pack, and create isolated npm and Bun installs outside the repo before publishing.
* Local release installs, documented npm installs, andpi update --selfuse--ignore-scriptswhere supported.
* CI installs withnpm ci --ignore-scripts, and a scheduled GitHub workflow runsnpm audit --omit=devplusnpm audit signatures --omit=dev.
* Shrinkwrap generation has an explicit allowlist for dependency lifecycle scripts; new lifecycle-script deps fail checks until reviewed.

## License

MIT

## About

AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods

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

53.6k

 stars
 

### Watchers

192

 watching
 

### Forks

6.4k

 forks
 

 Report repository

 

## Releases222

v0.75.5

 Latest

 

May 23, 2026

 

+ 221 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript93.4%
* JavaScript5.8%
* CSS0.4%
* Shell0.3%
* C0.1%
* HTML0.0%