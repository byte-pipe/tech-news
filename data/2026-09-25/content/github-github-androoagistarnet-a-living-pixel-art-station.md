---
title: 'GitHub - androoAGI/starnet: A living pixel-art station where real AI agents do real work. Local-first desktop agent harness - bring your own key, watch your crew actually run. · GitHub'
url: https://github.com/androoAGI/starnet
site_name: github
content_file: github-github-androoagistarnet-a-living-pixel-art-station
fetched_at: '2026-09-25T15:44:41.901568'
original_url: https://github.com/androoAGI/starnet
author: androoAGI
description: A living pixel-art station where real AI agents do real work. Local-first desktop agent harness - bring your own key, watch your crew actually run. - androoAGI/starnet
---

androoAGI

 

/

starnet

Public

* NotificationsYou must be signed in to change notification settings
* Fork79
* Star349

 
 
 
feat/harness-backend
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

10,316 Commits
10,316 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
dev
dev
 
 
docs
docs
 
 
frontend
frontend
 
 
gal
gal
 
 
loops
loops
 
 
output
output
 
 
qa
qa
 
 
scripts
scripts
 
 
shared
shared
 
 
sidecar
sidecar
 
 
src-tauri
src-tauri
 
 
test
test
 
 
website
website
 
 
.gitignore
.gitignore
 
 
.gitleaksignore
.gitleaksignore
 
 
CODE_MAP.md
CODE_MAP.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
INSTALL.md
INSTALL.md
 
 
LICENSE
LICENSE
 
 
NOTICE.md
NOTICE.md
 
 
PRIVACY.md
PRIVACY.md
 
 
README.md
README.md
 
 
RELEASE_NOTES.md
RELEASE_NOTES.md
 
 
SECURITY.md
SECURITY.md
 
 
TERMS.md
TERMS.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

A living pixel-art station where real AI agents do real work.

Download·Install guide·Run from source·Docs·Contributing

StarNet is a local-first desktop harness where you create AI agents, organize them into a
pixel-art space station, and watch them perform real work with real models and tools. The
station is not decoration — it is a projection of live runtime state, and the product contract
is literal:A room is a capability-scoped team,a hallway isan authorized handoff
lane, anda placed object is a real capability grant.
The layout you drawisthe workflow the agents run.

Start with one agent, then place bays or summon specialists to runmore, concurrently—
each agenuinely distinct, bounded agent runwith its own workspace and permissions.
The harness performsreal model calls, real tools, real costrather than animating a
simulation.

## Features

A crew, not a chatbot

Create agents with distinct classes, personas, and loadouts. Run several at once — each gets its own workspace, transcript, memory, and bounded permissions.

Bring your own models

Paste an OpenRouter key, or sign in with supported provider accounts (Anthropic, OpenAI, Google) — keys live in the OS keychain, never in the frontend.

Message it from anywhere

Wire agents to Telegram, Discord, Slack, Signal, or Matrix and talk to your station away from the desk.

Night Shift

Leave the station running and agents keep working inside an explicit, adjustable leash — every away-action is logged and reviewable.

Recipes, skills, schedules

Launch proven multi-step recipes, grant reusable skills, and put work on cron schedules with visible output.

Asks before it guesses

Task Briefs turn ambiguity into one concrete question with options — over any connected channel — instead of a silent wrong guess.

Finished work has a front door

Deliverables land in the OUTBOX as real files you open, not chat scrollback you archaeology.

MCP connectors

Attach Model Context Protocol servers and paste-a-key/OAuth connectors to extend what agents can touch.

Voice

Push-to-talk dictation in, one consistent station voice out.

Real ledgers

Spend, budgets, and run history persist on disk and are shown as-is.

## What is real

* Model calls stream through the local Node sidecar.
* Tools operate through explicit capability and consent checks.
* Agent memory, transcripts, spend records, tasks, and schedules persist on disk.
* Multiple agents run concurrently with separate workspaces and bounded permissions.
* The visual station projects the same runtime state the harness can prove.

StarNet does not simulate revenue, completed work, model activity, or spend. Its core product
law is thatthe interface must never assert state the harness cannot prove.

## Download

Desktop builds are published on theStarNet releases page.

Platform

Asset

Windows
 (10/11, 64-bit)

StarNet_<version>_x64-setup.exe

macOS — Apple Silicon
 (M1–M4)

StarNet_<version>_aarch64.dmg

macOS — Intel

StarNet_<version>_x64.dmg

Apple Silicon note:use the nativeaarch64DMG. Avoid thex64DMG on Apple Silicon:
it runs under Rosetta 2 rather than using the native architecture.

The public release train supports Windows and macOS. It refuses to stage a release unless the
Windows installer passes Authenticode and timestamp verification, both Mac builds pass
Developer ID checks and Apple notarization, and every updater artifact has a valid updater
signature. Those are pipeline requirements, not proof that a particular downloaded or installed
copy was tested on your machine;INSTALL.mdexplains what to verify and when to stop.
Linux packages are internal build artifacts only and are not a supported public release target.

Early release:Windows is the most-tested desktop target. macOS has less real-world
coverage. Broken? Tell us:androo.agi@gmail.com.

## Run from source

Requirements: Node.js 18+ (Node.js 22 matches CI), Git. Rust and theTauri prerequisitesonly for the desktop shell.

The sidecar uses Node core modules only, so it runs without installing anything:

git clone https://github.com/androoAGI/starnet.git

cd
 starnet
node sidecar/index.js

Openhttp://localhost:8787, then connect a provider —bring your own OpenRouter API key (BYOK)or use a supported OAuth sign-in. Provider requests leave your machine when you run an agent;
station state, transcripts, memory, and ledgers stay in the local StarNet workspace unless you
explicitly use a network tool or connector. SeePRIVACY.mdfor the full data map.

### Run free with a local model

No key, no account, no bill: installOllama, pull a model
(ollama pull llama3.1), and pickOLLAMAas the provider — on the first-run brain screen, or
later inSETTINGS → PROVIDERS. StarNet talks to Ollama on127.0.0.1:11434and only reports
it ready once it can list your local models. Honest caveat: local models are smaller than the
cloud ones, so expect slower and rougher work on long tasks.

For desktop development:

npm ci
npm run desktop:dev 
#
 dev shell

npm run desktop:build 
#
 build installers locally

## Coming from OpenClaw or Hermes?

StarNet can import an existing agent: point it at your on-disk OpenClaw or Hermes home and it
mints a StarNet agent from the persona, instructions, memory, and model it finds. API keys
never transfer — you re-enter those in the KEYS tab.

## Architecture

Path

Responsibility

frontend/

Vanilla JavaScript station world and desktop UI.

sidecar/

Local Node agent runtime: providers, tools, persistence, budgets, consent.

shared/

Additive cross-boundary event and schema contracts.

src-tauri/

Rust/Tauri desktop shell and bundled runtime.

test/

Unit, contract, integration, and release gates.

qa/

Live QA receipts, journeys, findings ledger, and release-readiness authority.

The frontend consumes real sidecar events over localhost HTTP/NDJSON and SSE. Secrets belong
to the local authority:Secrets are held by the sidecar / OS keychain, never in the frontend.

Start withdocs/INDEX.mdfor the living documentation. Older planning
documents remain in the repository as design history and are labeled accordingly.

## Testing

npm run test:fast 
#
 required merge gate

npm run test:http 
#
 live sidecar HTTP/E2E suite

npm 
test
 
#
 validation + world + fast + HTTP suites

npm run security:secrets 
#
 full-history secret scan; requires Gitleaks in PATH

The release aggregate isnpm run qa:ready. It is candidate-bound: any new commit invalidates
the prior READY receipt until the affected live gates are rerun.

## Contributing and security

Contributions are welcome — readCONTRIBUTING.mdand follow theCode of Conduct.

Do not report vulnerabilities in a public issue. FollowSECURITY.mdfor private
reporting instructions.

## License

StarNet is open source under theMIT License. Third-party components remain
under their original licenses — seeNOTICE.md.

The MIT License covers the code only.TheStarNetname, the logo, the station artwork
and sprites, and the rest of the project's brand identity are owned by Andrew Sims and arenotlicensed with it — no trademark or other brand rights are granted, expressly or by
implication.

MIT means you may fork, modify, and redistribute the code, including commercially. What you
may not do is ship it as StarNet: forks and derivatives must use their own name, logo, and
artwork, and must not present themselves as this project or as endorsed by it.