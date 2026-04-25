---
title: 'GitHub - RooCodeInc/Roo-Code: Roo Code gives you a whole dev team of AI agents in your code editor. · GitHub'
url: https://github.com/RooCodeInc/Roo-Code
site_name: github
content_file: github-github-roocodeincroo-code-roo-code-gives-you-a-who
fetched_at: '2026-04-25T11:37:20.747975'
original_url: https://github.com/RooCodeInc/Roo-Code
author: RooCodeInc
description: Roo Code gives you a whole dev team of AI agents in your code editor. - RooCodeInc/Roo-Code
---

RooCodeInc

 

/

Roo-Code

Public

* NotificationsYou must be signed in to change notification settings
* Fork3.1k
* Star23.4k

 
 
 
 
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

7,056 Commits
7,056 Commits
.changeset
.changeset
 
 
.github
.github
 
 
.husky
.husky
 
 
.roo
.roo
 
 
.vscode
.vscode
 
 
apps
apps
 
 
locales
locales
 
 
packages
packages
 
 
releases
releases
 
 
schemas
schemas
 
 
scripts
scripts
 
 
src
src
 
 
webview-ui
webview-ui
 
 
.dockerignore
.dockerignore
 
 
.env.sample
.env.sample
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitconfig
.gitconfig
 
 
.gitignore
.gitignore
 
 
.nvmrc
.nvmrc
 
 
.prettierrc.json
.prettierrc.json
 
 
.rooignore
.rooignore
 
 
.roomodes
.roomodes
 
 
.tool-versions
.tool-versions
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
PRIVACY.md
PRIVACY.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
ellipsis.yaml
ellipsis.yaml
 
 
knip.json
knip.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
progress.txt
progress.txt
 
 
renovate.json
renovate.json
 
 
tsconfig.json
tsconfig.json
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

Get help fast →Join Discord• Prefer async? →Join r/RooCode

# Roo Code

Your AI-Powered Dev Team, Right in Your Editor

## What's New in v3.53.0

### The Roo Code plugin is not going away.

You may have seen therecent announcementthat Roo Code hit 3 million installs and the original team is going all-in on Roomote. We know that news was hard for a lot of you. This plugin means a lot to us and to you, and we hear you.

The good news:a community team has stepped up to carry Roo Code forward, and we're working with them on an official handoff so the plugin you rely on keeps getting maintained and improved.

What's new in this release:

* Add GPT-5.5 support via the OpenAI Codex provider.
* Add Claude Opus 4.7 support on Vertex AI.
* Add previous checkpoint navigation controls in chat so you can step back through prior checkpoints more easily.

🌐 Available languages

* English
* Català
* Deutsch
* Español
* Français
* हिंदी
* Bahasa Indonesia
* Italiano
* 日本語
* 한국어
* Nederlands
* Polski
* Português (BR)
* Русский
* Türkçe
* Tiếng Việt
* 简体中文
* 繁體中文
* ...

## What Can Roo Code Do For YOU?

* Generate Code from natural language descriptions and specs
* Adapt with Modes: Code, Architect, Ask, Debug, and Custom Modes
* Refactor & Debug existing code
* Write & Update documentation
* Answer Questions about your codebase
* Automate repetitive tasks
* Utilize MCP Servers

## Modes

Roo Code adapts to how you work:

* Code Mode: everyday coding, edits, and file ops
* Architect Mode: plan systems, specs, and migrations
* Ask Mode: fast answers, explanations, and docs
* Debug Mode: trace issues, add logs, isolate root causes
* Custom Modes: build specialized modes for your team or workflow

Learn more:Using Modes•Custom Modes

## Tutorial & Feature Videos

Installing Roo Code

Configuring Profiles

Codebase Indexing

Custom Modes

Checkpoints

Context Management

More quick tutorial and feature videos...

## Resources

* Documentation:The official guide to installing, configuring, and mastering Roo Code.
* YouTube Channel:Watch tutorials and see features in action.
* Discord Server:Join the community for real-time help and discussion.
* Reddit Community:Share your experiences and see what others are building.
* GitHub Issues:Report bugs and track development.
* Feature Requests:Have an idea? Share it with the developers.

## Local Setup & Development

1. Clonethe repo:

git clone https://github.com/RooCodeInc/Roo-Code.git

1. Install dependencies:

pnpm install

1. Run the extension:

There are several ways to run the Roo Code extension:

### Development Mode (F5)

For active development, use VSCode's built-in debugging:

PressF5(or go toRun→Start Debugging) in VSCode. This will open a new VSCode window with the Roo Code extension running.

* Changes to the webview will appear immediately.
* Changes to the core extension will also hot reload automatically.

### Automated VSIX Installation

To build and install the extension as a VSIX package directly into VSCode:

pnpm install:vsix [-y] [--editor
=<
command
>
]

This command will:

* Ask which editor command to use (code/cursor/code-insiders) - defaults to 'code'
* Uninstall any existing version of the extension.
* Build the latest VSIX package.
* Install the newly built VSIX.
* Prompt you to restart VS Code for changes to take effect.

Options:

* -y: Skip all confirmation prompts and use defaults
* --editor=<command>: Specify the editor command (e.g.,--editor=cursoror--editor=code-insiders)

### Manual VSIX Installation

If you prefer to install the VSIX package manually:

1. First, build the VSIX package:pnpm vsix
2. A.vsixfile will be generated in thebin/directory (e.g.,bin/roo-cline-<version>.vsix).
3. Install it manually using the VSCode CLI:code --install-extension bin/roo-cline-<version>.vsix

We usechangesetsfor versioning and publishing. Check ourCHANGELOG.mdfor release notes.

## Disclaimer

Please notethat Roo Code, Inc doesnotmake any representations or warranties regarding any code, models, or other tools provided or made available in connection with Roo Code, any associated third-party tools, or any resulting outputs. You assumeall risksassociated with the use of any such tools or outputs; such tools are provided on an"AS IS"and"AS AVAILABLE"basis. Such risks may include, without limitation, intellectual property infringement, cyber vulnerabilities or attacks, bias, inaccuracies, errors, defects, viruses, downtime, property loss or damage, and/or personal injury. You are solely responsible for your use of any such tools or outputs (including, without limitation, the legality, appropriateness, and results thereof).

## Contributing

We love community contributions! Get started by reading ourCONTRIBUTING.md.

## License

Apache 2.0 © 2025 Roo Code, Inc.

Enjoy Roo Code!Whether you keep it on a short leash or let it roam autonomously, we can’t wait to see what you build. If you have questions or feature ideas, drop by ourReddit communityorDiscord. Happy coding!

## About

Roo Code gives you a whole dev team of AI agents in your code editor.

roocode.com

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

23.4k

 stars
 

### Watchers

136

 watching
 

### Forks

3.1k

 forks
 

 Report repository

 

## Releases280

Release v3.53.0

 Latest

 

Apr 23, 2026

 

+ 279 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript98.7%
* Other1.3%