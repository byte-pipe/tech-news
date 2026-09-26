---
title: GitHub - anthropics/claude-code-action · GitHub
url: https://github.com/anthropics/claude-code-action
site_name: github
content_file: github-github-anthropicsclaude-code-action-github
fetched_at: '2026-09-26T14:54:05.109990'
original_url: https://github.com/anthropics/claude-code-action
author: anthropics
description: Contribute to anthropics/claude-code-action development by creating an account on GitHub.
---

anthropics

 

/

claude-code-action

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.2k
* Star9k

 
 
 
Use this GitHub action with your project
Add this Action to an existing workflow or create a new one
View on Marketplace
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

804 Commits
804 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude
.claude
 
 
.github
.github
 
 
agent-approval-check
agent-approval-check
 
 
base-action
base-action
 
 
docs
docs
 
 
examples
examples
 
 
scripts
scripts
 
 
src
src
 
 
test
test
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
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
 
 
ROADMAP.md
ROADMAP.md
 
 
SECURITY.md
SECURITY.md
 
 
action.yml
action.yml
 
 
bun.lock
bun.lock
 
 
bunfig.toml
bunfig.toml
 
 
github-app-manifest.json
github-app-manifest.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# Claude Code Action

A general-purposeClaude Codeaction for GitHub PRs and issues that can answer questions and implement code changes. This action intelligently detects when to activate based on your workflow context—whether responding to @claude mentions, issue assignments, or executing automation tasks with explicit prompts. It supports multiple authentication methods including Anthropic direct API (API key or workload identity federation), Amazon Bedrock, Google Vertex AI, and Microsoft Foundry.

## Features

* 🎯Intelligent Mode Detection: Automatically selects the appropriate execution mode based on your workflow context—no configuration needed
* 🤖Interactive Code Assistant: Claude can answer questions about code, architecture, and programming
* 🔍Code Review: Analyzes PR changes and suggests improvements
* ✨Code Implementation: Can implement simple fixes, refactoring, and even new features
* 💬PR/Issue Integration: Works seamlessly with GitHub comments and PR reviews
* 🛠️Flexible Tool Access: Access to GitHub APIs and file operations (additional tools can be enabled via configuration)
* 📋Progress Tracking: Visual progress indicators with checkboxes that dynamically update as Claude completes tasks
* 📊Structured Outputs: Get validated JSON results that automatically become GitHub Action outputs for complex automations
* 🏃Runs on Your Infrastructure: The action executes entirely on your own GitHub runner (Anthropic API calls go to your chosen provider)
* ⚙️Simplified Configuration: Unifiedpromptandclaude_argsinputs provide clean, powerful configuration aligned with Claude Code SDK

## 📦 Upgrading from v0.x?

See ourMigration Guidefor step-by-step instructions on updating your workflows to v1.0. The new version simplifies configuration while maintaining compatibility with most existing setups.

## Quickstart

The easiest way to set up this action is throughClaude Codein the terminal. Just openclaudeand run/install-github-app.

This command will guide you through setting up the GitHub app and required secrets.

Note:

* You must be a repository admin to install the GitHub app and add secrets
* This quickstart method is only available for direct Anthropic API users. For AWS Bedrock, Google Vertex AI, or Microsoft Foundry setup, seedocs/cloud-providers.md.

## 📚 Solutions & Use Cases

Looking for specific automation patterns? Check ourSolutions Guidefor complete working examples including:

* 🔍 Automatic PR Code Review- Full review automation
* 📂 Path-Specific Reviews- Trigger on critical file changes
* 👥 External Contributor Reviews- Special handling for new contributors
* 📝 Custom Review Checklists- Enforce team standards
* 🔄 Scheduled Maintenance- Automated repository health checks
* 🏷️ Issue Triage & Labeling- Automatic categorization
* 📖 Documentation Sync- Keep docs updated with code changes
* 🔒 Security-Focused Reviews- OWASP-aligned security analysis
* 📊 DIY Progress Tracking- Create tracking comments in automation mode

Each solution includes complete working examples, configuration details, and expected outcomes.

## Documentation

* Solutions Guide-🎯 Ready-to-use automation patterns
* Migration Guide-⭐ Upgrading from v0.x to v1.0
* Setup Guide- Manual setup, custom GitHub apps, and security best practices
* Usage Guide- Basic usage, workflow configuration, and input parameters
* Custom Automations- Examples of automated workflows and custom prompts
* Configuration- MCP servers, permissions, environment variables, and advanced settings
* Experimental Features- Execution modes and network restrictions
* Cloud Providers- AWS Bedrock, Google Vertex AI, and Microsoft Foundry setup
* Capabilities & Limitations- What Claude can and cannot do
* Security- Access control, permissions, and commit signing
* FAQ- Common questions and troubleshooting

## 📚 FAQ

Having issues or questions? Check out ourFrequently Asked Questionsfor solutions to common problems and detailed explanations of Claude's capabilities and limitations.

## License

This project is licensed under the MIT License—see the LICENSE file for details.