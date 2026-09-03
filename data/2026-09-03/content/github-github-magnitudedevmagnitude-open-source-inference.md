---
title: 'GitHub - magnitudedev/magnitude: Open source inference server that runs the best local models for your hardware, plugged into the agent you already use. Works with Pi, OpenCode, Hermes, OpenClaw, Codex, Claude Code, Oh My Pi, and Cline. · GitHub'
url: https://github.com/magnitudedev/magnitude
site_name: github
content_file: github-github-magnitudedevmagnitude-open-source-inference
fetched_at: '2026-09-03T14:53:07.043387'
original_url: https://github.com/magnitudedev/magnitude
author: magnitudedev
description: Open source inference server that runs the best local models for your hardware, plugged into the agent you already use. Works with Pi, OpenCode, Hermes, OpenClaw, Codex, Claude Code, Oh My Pi, and Cline. - magnitudedev/magnitude
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 magnitudedev

 

/

magnitude

Public

* NotificationsYou must be signed in to change notification settings
* Fork136
* Star1.8k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

594 Commits
594 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.changeset
.changeset
 
 
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
cli
cli
 
 
design
design
 
 
desktop
desktop
 
 
docs
docs
 
 
inference
inference
 
 
info
info
 
 
packages
packages
 
 
patches
patches
 
 
scripts
scripts
 
 
web
web
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
AGENTS.md
AGENTS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
bun.lock
bun.lock
 
 
bunfig.toml
bunfig.toml
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
turbo.json
turbo.json
 
 
vitest.workspace.ts
vitest.workspace.ts
 
 
View all files

## Repository files navigation

# Magnitude

Run your agent on local models. Free, private, and offline.

Magnitude is an open source inference server that runs the best local models for your hardware, plugged into the agent you already use. It profiles your machine, recommends the models that fit, then downloads, tunes, and runs them. Works with Pi, OpenCode, Hermes, OpenClaw, Codex, Claude Code, Oh My Pi, and Cline, or use the built-in harness.

⭐ Help us reach more developers and grow the Magnitude community. Star this repo!

## Get started

Send this to your agent to walk through models and setup:

Set up local models for me with the Magnitude CLI. Install it with `npm i -g @magnitudedev/cli` (or my package manager), then run `magnitude docs onboarding` and follow the instructions.

Your agent will profile your hardware, walk you through the best local models for it, download the ones you pick, and switch itself over to them.

Magnitude supports macOS and Linux. Windows is supported through WSL.

Want to browse the models directly?

npm i -g @magnitudedev/cli
magnitude setup

The interactive setup lets you browse the recommended models and choose one yourself.

## Why Magnitude?

* Free to run:no token costs, API keys, or rate limits
* Fully private and offline:models, prompts, and files stay on your machine
* Agent-first setup:one prompt and your agent walks you through the rest
* Knows your hardware:profiles your chip, memory, and bandwidth
* Recommends what fits:the best models for your machine, with estimated tok/s
* Tuned end to end:speculative decoding, concurrency, all set for your machine
* Models on demand:loaded on request, unloaded when idle or memory fills
* Open source:Apache 2.0, yours to modify

## FAQ

### What is Magnitude?

An open source inference server that runs the best local models for your hardware, plugged into the agent you already use. It profiles your machine, recommends the models that fit, then downloads, tunes, and runs them.

### What hardware do I need?

There's no fixed minimum. Magnitude profiles your hardware and recommends the best models for your machine. More memory lets you run larger models.

### Why not just have my agent set up Ollama?

Your agent would be guessing. It doesn't know your hardware, which quant fits, or how fast it'll run. Magnitude gives it a catalog with recommendations computed for your machine, an onboarding flow that writes your harness config, and inference built for agent workloads. Models load just in time and unload when idle or memory gets tight.

### Which harnesses work with it?

Pi, OpenCode, Hermes, OpenClaw, Codex, Claude Code, Oh My Pi, and Cline. During setup, your agent connects your harness to the model you pick. Or use Magnitude's built-in harness.

### Do I need to manage Magnitude after setup?

No. It runs in the background, loads models when your agent needs them, and unloads them when idle or memory gets tight. Your agent can install or switch models through the Magnitude CLI anytime.

### Does my data go to the cloud?

No. Prompts, files, and models stay on your machine.

### Can it run completely offline?

Yes. Once Magnitude and a model are downloaded, no internet connection needed.

### Can I use models outside the catalog?

Yes. You candownload compatible GGUF models from Hugging Faceand use them in Magnitude.

## Learn more

* Documentation
* CLI reference
* Discord
* Report an issue

## License

Magnitude is licensed under theApache License 2.0.