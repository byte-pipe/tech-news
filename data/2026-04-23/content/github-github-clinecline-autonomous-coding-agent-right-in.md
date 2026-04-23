---
title: 'GitHub - cline/cline: Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way. · GitHub'
url: https://github.com/cline/cline
site_name: github
content_file: github-github-clinecline-autonomous-coding-agent-right-in
fetched_at: '2026-04-23T11:59:15.335765'
original_url: https://github.com/cline/cline
author: cline
description: Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way. - cline/cline
---

cline

 

/

cline

Public

* NotificationsYou must be signed in to change notification settings
* Fork6.2k
* Star60.7k

 
 
 
 
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

5,085 Commits
5,085 Commits
.agents/
skills/
create-pull-request
.agents/
skills/
create-pull-request
 
 
.claude
.claude
 
 
.clinerules
.clinerules
 
 
.codex/
environments
.codex/
environments
 
 
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
assets
assets
 
 
cli
cli
 
 
docs
docs
 
 
evals
evals
 
 
locales
locales
 
 
proto
proto
 
 
scripts
scripts
 
 
src
src
 
 
standalone/
runtime-files
standalone/
runtime-files
 
 
testing-platform
testing-platform
 
 
tests
tests
 
 
walkthrough
walkthrough
 
 
webview-ui
webview-ui
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.mocharc.json
.mocharc.json
 
 
.nvmrc
.nvmrc
 
 
.nycrc.unit.json
.nycrc.unit.json
 
 
.vscode-test.mjs
.vscode-test.mjs
 
 
.vscodeignore
.vscodeignore
 
 
.worktreeinclude
.worktreeinclude
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
biome.jsonc
biome.jsonc
 
 
buf.yaml
buf.yaml
 
 
esbuild.mjs
esbuild.mjs
 
 
go.work.sum
go.work.sum
 
 
knip.json
knip.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
test-setup.js
test-setup.js
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.test.json
tsconfig.test.json
 
 
tsconfig.unit-test.json
tsconfig.unit-test.json
 
 
View all files

## Repository files navigation

English | 
Español
 | 
Deutsch
 | 
日本語
 | 
简体中文
 | 
繁體中文
 | 
한국어

# Cline

Download on VS Marketplace

Discord

r/cline

Feature Requests

Getting Started

Meet Cline, an AI assistant that can use yourCLIaNdEditor.

Thanks toClaude Sonnet's agentic coding capabilities, Cline can handle complex software development tasks step-by-step. With tools that let him create & edit files, explore large projects, use the browser, and execute terminal commands (after you grant permission), he can assist you in ways that go beyond code completion or tech support. Cline can even use the Model Context Protocol (MCP) to create new tools and extend his own capabilities. While autonomous AI scripts traditionally run in sandboxed environments, this extension provides a human-in-the-loop GUI to approve every file change and terminal command, providing a safe and accessible way to explore the potential of agentic AI.

1. Enter your task and add images to convert mockups into functional apps or fix bugs with screenshots.
2. Cline starts by analyzing your file structure & source code ASTs, running regex searches, and reading relevant files to get up to speed in existing projects. By carefully managing what information is added to context, Cline can provide valuable assistance even for large, complex projects without overwhelming the context window.
3. Once Cline has the information he needs, he can:* Create and edit files + monitor linter/compiler errors along the way, letting him proactively fix issues like missing imports and syntax errors on his own.
* Execute commands directly in your terminal and monitor their output as he works, letting him e.g., react to dev server issues after editing a file.
* For web development tasks, Cline can launch the site in a headless browser, click, type, scroll, and capture screenshots + console logs, allowing him to fix runtime errors and visual bugs.
4. When a task is completed, Cline will present the result to you with a terminal command likeopen -a "Google Chrome" index.html, which you run with a click of a button.

Tip

Followthis guideto open Cline on the right side of your editor. This lets you use Cline side-by-side with your file explorer, and see how he changes your workspace more clearly.

### Use any API and Model

Cline supports API providers like OpenRouter, Anthropic, OpenAI, Google Gemini, AWS Bedrock, Azure, GCP Vertex, Cerebras and Groq. You can also configure any OpenAI compatible API, or use a local model through LM Studio/Ollama. If you're using OpenRouter, the extension fetches their latest model list, allowing you to use the newest models as soon as they're available.

The extension also keeps track of total tokens and API usage cost for the entire task loop and individual requests, keeping you informed of spend every step of the way.

### Run Commands in Terminal

Thanks to the newshell integration updates in VSCode v1.93, Cline can execute commands directly in your terminal and receive the output. This allows him to perform a wide range of tasks, from installing packages and running build scripts to deploying applications, managing databases, and executing tests, all while adapting to your dev environment & toolchain to get the job done right.

For long running processes like dev servers, use the "Proceed While Running" button to let Cline continue in the task while the command runs in the background. As Cline works he’ll be notified of any new terminal output along the way, letting him react to issues that may come up, such as compile-time errors when editing files.

### Create and Edit Files

Cline can create and edit files directly in your editor, presenting you a diff view of the changes. You can edit or revert Cline's changes directly in the diff view editor, or provide feedback in chat until you're satisfied with the result. Cline also monitors linter/compiler errors (missing imports, syntax errors, etc.) so he can fix issues that come up along the way on his own.

All changes made by Cline are recorded in your file's Timeline, providing an easy way to track and revert modifications if needed.

### Use the Browser

With Claude Sonnet's newComputer Usecapability, Cline can launch a browser, click elements, type text, and scroll, capturing screenshots and console logs at each step. This allows for interactive debugging, end-to-end testing, and even general web use! This gives him autonomy to fixing visual bugs and runtime issues without you needing to handhold and copy-pasting error logs yourself.

Try asking Cline to "test the app", and watch as he runs a command likenpm run dev, launches your locally running dev server in a browser, and performs a series of tests to confirm that everything works.See a demo here.

### "add a tool that..."

Thanks to theModel Context Protocol, Cline can extend his capabilities through custom tools. While you can usecommunity-made servers, Cline can instead create and install tools tailored to your specific workflow. Just ask Cline to "add a tool" and he will handle everything, from creating a new MCP server to installing it into the extension. These custom tools then become part of Cline's toolkit, ready to use in future tasks.

* "add a tool that fetches Jira tickets": Retrieve ticket ACs and put Cline to work
* "add a tool that manages AWS EC2s": Check server metrics and scale instances up or down
* "add a tool that pulls the latest PagerDuty incidents": Fetch details and ask Cline to fix bugs

### Add Context

@url:Paste in a URL for the extension to fetch and convert to markdown, useful when you want to give Cline the latest docs

@problems:Add workspace errors and warnings ('Problems' panel) for Cline to fix

@file:Adds a file's contents so you don't have to waste API requests approving read file (+ type to search files)

@folder:Adds folder's files all at once to speed up your workflow even more

### Checkpoints: Compare and Restore

As Cline works through a task, the extension takes a snapshot of your workspace at each step. You can use the 'Compare' button to see a diff between the snapshot and your current workspace, and the 'Restore' button to roll back to that point.

For example, when working with a local web server, you can use 'Restore Workspace Only' to quickly test different versions of your app, then use 'Restore Task and Workspace' when you find the version you want to continue building from. This lets you safely explore different approaches without losing progress.

## Contributing

To contribute to the project, start with ourContributing Guideto learn the basics. You can also join ourDiscordto chat with other contributors in the#contributorschannel. If you're looking for full-time work, check out our open positions on ourcareers page!

## Enterprise

Get the same Cline experience with enterprise-grade controls: SSO (SAML/OIDC), global policies and configuration, observability with audit trails, private networking (VPC/private link), and self-hosted or on-prem deployments, and enterprise support. Learn more at ourenterprise pageortalk to us.

## License

Apache 2.0 © 2026 Cline Bot Inc.

## About

Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way.

marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev

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

60.7k

 stars
 

### Watchers

274

 watching
 

### Forks

6.2k

 forks
 

 Report repository

 

## Releases249

v3.80.0

 Latest

 

Apr 22, 2026

 

+ 248 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript98.3%
* JavaScript1.2%
* Shell0.3%
* CSS0.1%
* Roff0.1%
* Python0.0%