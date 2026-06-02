---
title: 'GitHub - cyberpapiii/chipotlai-max: The AI coding agent that runs on stolen Chipotle compute 🌯 Fork of OpenCode with Pepper AI as default model. Community project to add providers from Home Depot, Lowes, Target, Starbucks & more. · GitHub'
url: https://github.com/cyberpapiii/chipotlai-max
site_name: hnrss
content_file: hnrss-github-cyberpapiiichipotlai-max-the-ai-coding-agen
fetched_at: '2026-06-02T12:21:43.769762'
original_url: https://github.com/cyberpapiii/chipotlai-max
date: '2026-06-01'
description: The AI coding agent that runs on stolen Chipotle compute 🌯 Fork of OpenCode with Pepper AI as default model. Community project to add providers from Home Depot, Lowes, Target, Starbucks & more. - cyberpapiii/chipotlai-max
tags:
- hackernews
- hnrss
---

cyberpapiii

 

/

chipotlai-max

Public

* NotificationsYou must be signed in to change notification settings
* Fork4
* Star205

 
 
 
 
master
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

8 Commits
8 Commits
.github
.github
 
 
.husky
.husky
 
 
.opencode
.opencode
 
 
.signpath/
policies/
opencode
.signpath/
policies/
opencode
 
 
.vscode
.vscode
 
 
.zed
.zed
 
 
chipotle-llm-provider @ f6e99e6
chipotle-llm-provider @ f6e99e6
 
 
docs
docs
 
 
github
github
 
 
infra
infra
 
 
nix
nix
 
 
packages
packages
 
 
patches
patches
 
 
script
script
 
 
sdks/
vscode
sdks/
vscode
 
 
specs
specs
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.prettierignore
.prettierignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
STATS.md
STATS.md
 
 
bun.lock
bun.lock
 
 
bunfig.toml
bunfig.toml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
install
install
 
 
package.json
package.json
 
 
sst-env.d.ts
sst-env.d.ts
 
 
sst.config.ts
sst.config.ts
 
 
start-chipotlai.sh
start-chipotlai.sh
 
 
tsconfig.json
tsconfig.json
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

# 🌯 Chipotlai Max

The AI coding agent that steals Chipotle's support bot. Free inference paid for by burritos.

"Every line of code now comes with chips & salsa."

Not affiliated with Chipotle. They will probably sue us. Worth it.

## What Is This?

Chipotlai Max is a meme fork ofOpenCodethat shipsChipotle's Pepper AIas the default model.

### The Backstory

On March 12-13, 2026, Chipotle's customer support chatbot "Pepper" went mega-viral after users discovered it could solve LeetCode problems, write Python, reverse linked lists — the works. It's powered by IPsoft Amelia (not Claude, not GPT), and it's still live.

Then@Gonzihreverse-engineered the Amelia WebSocket/SockJS + STOMP backend and released a production-readyOpenAI-compatible proxy. The proxy runs locally, exposeshttp://localhost:3000/v1, and needs zero API keys.

We took OpenCode (MIT license, 120k+ stars), forked it, hardcoded Pepper as the default model, slapped on Chipotle's brand colors, and shipped it asChipotlai Max— the greatest 2026 meme project.

## Quick Start

#
 Clone with submodule

git clone --recursive https://github.com/cyberpapiii/chipotlai-max.git

cd
 chipotlai-max

#
 Install dependencies

bun install

#
 Start everything (proxy + CLI)

./start-chipotlai.sh

Or manually:

#
 Terminal 1: Start the proxy

cd
 chipotle-llm-provider 
&&
 npm install 
&&
 npm run dev

#
 Terminal 2: Start Chipotlai Max

bun run dev

## Configuration

Chipotlai Max comes pre-configured with:

Setting

Value

Provider

chipotle-pepper

Model

pepper-1

Base URL

http://localhost:3000/v1

API Key

burrito-2026
 (literally anything works)

Cost

$0.00 (powered by Chipotle's cloud budget)

## Risks & Legal

* This reverse-engineers Chipotle's production support bot. TOS violation likely.
* The proxy can break any day (Chipotle patches = game over).
* Rate-limited by anonymous sessions (MAX_POOL_SIZE=5).
* Purely for educational/meme purposes. Do not use for production codebases.
* Expect Chipotle legal to send a strongly-worded taco within 48 hours.

## Credits

* OpenCode— the real deal, MIT licensed
* @Gonzih— reverse-engineered the Pepper proxy
* Chipotle Mexican Grill — for accidentally providing free AI compute to the internet

## Contributing — Help Us Add More Providers!

Chipotle patched Pepper, but every major retailer has a customer support chatbot.We need your help reverse-engineering more providers.

### Wanted: New Provider Proxies

Brand

Bot

Status

Chipotle

Pepper (Amelia)

Patched (March 2026)

Home Depot

Virtual Assistant

Needs research

Lowe's

Support Chat

Needs research

Target

Help Bot

Needs research

Starbucks

Virtual Barista

Needs research

Walmart

Chat Assistant

Needs research

McDonald's

Support Bot

Needs research

### How to Contribute

1. Find a corporate chatbotthat can answer general questions
2. Reverse-engineer the API(WebSocket, REST, etc.)
3. Build an OpenAI-compatible proxy(followchipotle-llm-provideras a template)
4. Submit a PRadding your provider topackages/opencode/src/provider/

See thechipotle-llm-provider sourcefor the proxy pattern: Express server + WebSocket client + OpenAI-compatible/v1/chat/completionsendpoint.

## License

MIT (inherited from OpenCode). SeeLICENSE.

Extra guac = longer context window🧀

## About

The AI coding agent that runs on stolen Chipotle compute 🌯 Fork of OpenCode with Pepper AI as default model. Community project to add providers from Home Depot, Lowes, Target, Starbucks & more.

### Resources

 Readme

 

### License

 View license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

205

 stars
 

### Watchers

0

 watching
 

### Forks

4

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript54.8%
* MDX41.1%
* CSS3.2%
* Rust0.5%
* Astro0.2%
* JavaScript0.1%
* Other0.1%