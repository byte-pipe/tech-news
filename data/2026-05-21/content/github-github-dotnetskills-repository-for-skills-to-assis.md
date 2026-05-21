---
title: 'GitHub - dotnet/skills: Repository for skills to assist AI coding agents with .NET and C# · GitHub'
url: https://github.com/dotnet/skills
site_name: github
content_file: github-github-dotnetskills-repository-for-skills-to-assis
fetched_at: '2026-05-21T12:05:45.231278'
original_url: https://github.com/dotnet/skills
author: dotnet
description: Repository for skills to assist AI coding agents with .NET and C# - dotnet/skills
---

dotnet

 

/

skills

Public

* NotificationsYou must be signed in to change notification settings
* Fork165
* Star2k

 
 
 
 
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

444 Commits
444 Commits
.agents/
skills
.agents/
skills
 
 
.claude-plugin
.claude-plugin
 
 
.cursor-plugin
.cursor-plugin
 
 
.github
.github
 
 
.vscode
.vscode
 
 
docs
docs
 
 
eng
eng
 
 
plugins
plugins
 
 
tests
tests
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.markdownlint-cli2.jsonc
.markdownlint-cli2.jsonc
 
 
.vally.yaml
.vally.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
global.json
global.json
 
 
View all files

## Repository files navigation

# .NET Agent Skills

This repository contains the .NET team's curated set of core skills and custom agents for coding agents. For information about the Agent Skills standard, seeagentskills.io.

📊 Dashboard- Accuracy and efficiency scoring trends for contained plugins (https://dotnet.github.io/skills/)

## What's Included

Plugin

Description

dotnet

Collection of core .NET skills for handling common .NET coding tasks.

dotnet-data

Skills for .NET data access and Entity Framework related tasks.

dotnet-diag

Skills for .NET performance investigations, debugging, and incident analysis.

dotnet-msbuild

Comprehensive MSBuild and .NET build skills: failure diagnosis, performance optimization, code quality, and modernization.

dotnet-nuget

NuGet and .NET package management: dependency management and modernization.

dotnet-upgrade

Skills for migrating and upgrading .NET projects across framework versions, language features, and compatibility targets.

dotnet-maui

Skills for .NET MAUI development: environment setup, diagnostics, and troubleshooting.

dotnet-ai

AI and ML skills for .NET: technology selection, LLM integration, agentic workflows, RAG pipelines, MCP, and classic ML with ML.NET.

dotnet-template-engine

.NET Template Engine skills: template discovery, project scaffolding, and template authoring.

dotnet-test

Skills for running, diagnosing, and migrating .NET tests: test execution, filtering, platform detection, and MSTest workflows.

dotnet-aspnet

ASP.NET Core web development skills including middleware, endpoints, real-time communication, and API patterns.

dotnet11

Skills for new .NET 11 APIs and language features.

## Installation

### 🚀 Plugins - Copilot CLI / Claude Code

1. Launch Copilot CLI or Claude Code
2. Add the marketplace:/plugin marketplace add dotnet/skills
3. Install a plugin:/plugin install <plugin>@dotnet-agent-skills
4. Restart to load the new plugins
5. View available skills:/skills
6. View available agents:/agents
7. Update plugin (on demand):/plugin update <plugin>@dotnet-agent-skills

### VS Code / VS Code Insiders (Preview)

Important

VS Code plugin support is a preview feature and subject to change. You may need to enable it first.

Once configured, type/pluginsin Copilot Chat or use the@agentPluginsfilter in Extensions to browse and install plugins from the marketplace.

### Cursor

This repository is aCursor plugin marketplace. You can discover and install published plugins directly in Cursor:

1. Open the marketplace panel in Cursor
2. Search for.NETor browsecursor.com/marketplace
3. Install the desired plugins

For local development or unpublished changes, import plugins from a local checkout:

1. Copy or symlink your local checkout to~/.cursor/plugins/local/dotnet-agent-skills
2. Restart Cursor or runDeveloper: Reload Window

### Codex CLI

Skills in this repository follow theagentskills.ioopen standard
and are compatible withOpenAI Codex.

Install individual skills using theskill-installerCLI with the GitHub URL:

$ skill-installer install https://github.com/dotnet/skills/tree/main/plugins/
<
plugin
>
/skills/
<
skill-name
>

## Contributing

SeeCONTRIBUTING.mdfor contribution guidelines and how to add a new plugin.

## License

SeeLICENSEfor details.

## About

Repository for skills to assist AI coding agents with .NET and C#

### Topics

 agent-skills

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2k

 stars
 

### Watchers

17

 watching
 

### Forks

165

 forks
 

 Report repository

 

## Releases2

v1.0.0

 Latest

 

Apr 21, 2026

 

+ 1 release

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C#97.0%
* PowerShell2.1%
* JavaScript0.7%
* Shell0.1%
* HTML0.1%
* F#0.0%