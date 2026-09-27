---
title: 'GitHub - miuuyy/codex-chatgpt-web: Use ChatGPT Web (including Pro) as a native model in Codex — with context, tools, streaming and images, without using Codex quota. · GitHub'
url: https://github.com/miuuyy/codex-chatgpt-web
site_name: github
content_file: github-github-miuuyycodex-chatgpt-web-use-chatgpt-web-inc
fetched_at: '2026-09-27T15:32:15.562255'
original_url: https://github.com/miuuyy/codex-chatgpt-web
author: miuuyy
description: Use ChatGPT Web (including Pro) as a native model in Codex — with context, tools, streaming and images, without using Codex quota. - miuuyy/codex-chatgpt-web
---

miuuyy

 

/

codex-chatgpt-web

Public

* NotificationsYou must be signed in to change notification settings
* Fork951
* Star11.9k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

336 Commits
336 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
LICENSES
LICENSES
 
 
assets
assets
 
 
docs
docs
 
 
launcher
launcher
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.ja.md
README.ja.md
 
 
README.ko.md
README.ko.md
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SECURITY.md
SECURITY.md
 
 
TROUBLESHOOTING.md
TROUBLESHOOTING.md
 
 
bun.lock
bun.lock
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

 
 
 
 

macOS Intel·All releases

English·简体中文·日本語·한국어

Get started·What’s new·Architecture·Troubleshooting

Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota. Keep the same interface, tasks, images, and streaming.

Full harness mode connects ChatGPT to the current task’s files, terminal, tools, and approvals through MCP. Conversations stay tied to your Codex task, so you can keep working as the context grows.

## Get started

Available models:Free/Go →Luna / Think. Accounts with reasoning controls →Instant–High, plusExtra HighandProwhen available. The launcher detects what your account can use.

1. Install the launcherusing the download for your system above.
2. Sign in to ChatGPTin the embedded browser and run the browser smoke test.
3. Install modelsand restart Codex once. In automatic mode, choose a model ending in(Web). Pro versions have separate entries; Sol reasoning is selected through Effort. Zero Risk keeps its dedicated entry.
4. For coding with tools, openMCPin the launcher and complete the Full harness setup below.

The app includes its browser and runtime. No separate Chrome, Node, or Bun installation is needed.

Terminal install, updates & repair

Quit the launcher before updating. These installers select the platform and architecture, verify the published checksums, and preserve your ChatGPT profile and launcher settings.

macOS / Linux

curl -fsSL https://github.com/miuuyy/codex-chatgpt-web/releases/latest/download/install-launcher.sh 
|
 sh

Windows PowerShell

irm https:
//
github.com
/
miuuyy
/
codex
-
chatgpt
-
web
/
releases
/
latest
/
download
/
install-launcher.ps1
 
|
 iex

Models, modes & MCP setup

Automatic modes offer Luna/Think when the account has no reasoning selector; otherwise Instant–High, with Extra High and Pro available independently when exposed by the account.

Mode

Sending messages

Local Codex tools

Browser-only

Automatic

No

Full harness (With Automation)

Automatic

Yes, through MCP

Zero Risk

Paste and send manually

Yes, through a separate MCP connector

Zero Risk does not read or operate the ChatGPT page. Choose the model andCodex Zero Riskconnector yourself, paste and send the prepared prompt, then confirmSentin the launcher. Automatic models ending in(Web)expose their supported Effort choices in Codex. Instant and each Pro version have separate entries to preserve their context budgets; older saved model entries keep their original fixed mode.

### Full harness

Full mode connects ChatGPT's tool calls back to the current Codex task through the officialOpenAI tunnel-client. The tunnel is outbound: it does
not expose a public IP, open an inbound port, or require router forwarding.

The launcher'sMCPpage guides the complete setup. For the exact clicks, see thevideo walkthroughs.

Limits

SeeLimitsfor the current
ChatGPT message allowances forGPT-5.6 Sol ProandGPT-6 Astra. Context limits depend on
the account type and selected effort. Plus Medium/High uses a measured 90,000-token window, or
up to 270,000 tokens with experimental3× contextenabled, with native Codex compaction
supported throughout.

1. Finish the required setup, openMCP, create the Tunnel and regular API key, then pressConnect harness.
2. Enable ChatGPTDeveloper Modeand create a new Tunnel connector named exactlyCodex Native2, withAuthentication: NoneandAllow all actions.
3. RunVerify runtimeto confirm thatCodex Native2is attached and available.

Write/modify actions also require the ChatGPT workspace and its administrator policy to permit
them. Seedeveloper mode and MCP apps.
Unexpected approval prompts fail closed unless--auto-approve-tool-callsis explicitly enabled;
that option clicksAllow once, never a permanent grant.

Diagnostics & subagents

UseActivityfor safe local diagnostics andSettings → Run doctorfor end-to-end health.
Settings can also cancel a retained browser turn or remove the Codex integration before uninstall.Save chats in ChatGPTkeeps task conversations in ChatGPT history. Off by default; independent ofNew browser chat for each turn.
SetCODEX_CHATGPT_WEB_BROWSER_DIAGNOSTICS=1only when every browser checkpoint needs a screenshot.

New installs useCompatibility V1for cross-backend subagents.Nativepreserves Codex's own
feature settings and enables plaintext Web-to-Web V2 delegation. Restart Codex and start a new task
after changing the protocol:

codex-chatgpt-web subagents status
codex-chatgpt-web subagents compatibility-v1
codex-chatgpt-web subagents native

Requirements & security

* This is unofficial browser automation, not an OpenAI API. ChatGPT UI changes can break selectors;
drift fails explicitly instead of silently switching model or transport.
* Browser state is a sensitive login artifact, and the loopback listener is reachable by processes
running as the same local user. Never share the launcher profile; use a trusted workstation.
* Release packages currently target macOS 13+ (arm64/x64), Windows x64, and Linux x64. Runtime,
tests, and packaging are gated on all three in CI; account-bound browser and MCP flows use the
separaterelease validation.
* Builds are not yet platform-signed, so Gatekeeper or SmartScreen may warn. The installers verify
the published SHA-256 manifest before installation.

Read the completearchitectureandsecurity modelbefore enabling full mode. Report vulnerabilities throughSECURITY.md.

Temporary Chat is aChatGPT privacy mode; prompts are still processed by OpenAI.

Validation coverage:release validation.

This is independent software and is not affiliated with or endorsed by OpenAI. Use it only with
your own account and in accordance with applicableTerms of Useand workspace policies; it does not bypass authentication or access controls.

Run from source & develop

git clone https://github.com/miuuyy/codex-chatgpt-web.git 
&&
 \

cd
 codex-chatgpt-web 
&&
 \
bun run app

This source path requires Bun 1.4.0. The command installs locked dependencies and opens the app.

bun run app
bun run dev:launcher
bun run src/cli.ts dev status
bun run dev:chat compaction-lab 
"
Reply with exactly: DEV READY
"

bun run verify
bun run smoke:subagents
bun run app:package

dev:launcheruses a separate profile and account under~/.codex-chatgpt-web-dev.dev:chatexercises the real browser and compaction paths with explicit simulated tool results, without changing your normal Codex route. See theDEV chat harnessfor setup and commands.

## Star History

Troubleshooting·Security·Contributing·MIT license·CI

Also by me:ChatGPT Persona Voice— local, near-real-time custom voices for ChatGPT and Codex.