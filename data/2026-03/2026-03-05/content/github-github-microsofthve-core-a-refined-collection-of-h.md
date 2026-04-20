---
title: 'GitHub - microsoft/hve-core: A refined collection of Hypervelocity Engineering components (instructions, prompts, agents) to start your project off right, or upgrade your existing projects to get the most out of all Copilots · GitHub'
url: https://github.com/microsoft/hve-core
site_name: github
content_file: github-github-microsofthve-core-a-refined-collection-of-h
fetched_at: '2026-03-05T11:16:02.158817'
original_url: https://github.com/microsoft/hve-core
author: microsoft
description: A refined collection of Hypervelocity Engineering components (instructions, prompts, agents) to start your project off right, or upgrade your existing projects to get the most out of all Copilots - microsoft/hve-core
---

microsoft



/

hve-core

Public

* NotificationsYou must be signed in to change notification settings
* Fork64
* Star158




 
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

353 Commits
353 Commits
.cspell
.cspell
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.vscode
.vscode
 
 
collections
collections
 
 
docs
docs
 
 
extension
extension
 
 
plugins
plugins
 
 
scripts
scripts
 
 
.checkov.yaml
.checkov.yaml
 
 
.cspell.json
.cspell.json
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitleaksignore
.gitleaksignore
 
 
.markdownlint-cli2.jsonc
.markdownlint-cli2.jsonc
 
 
.markdownlint.json
.markdownlint.json
 
 
.npmrc
.npmrc
 
 
.release-please-manifest.json
.release-please-manifest.json
 
 
.syft.yaml
.syft.yaml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
codecov.yml
codecov.yml
 
 
justfile
justfile
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
release-please-config.json
release-please-config.json
 
 
View all files

## Repository files navigation

title

description

author

ms.date

ms.topic

keywords

estimated_reading_time

HVE Core

Hypervelocity Engineering prompt library for GitHub Copilot with constraint-based AI workflows and validated artifacts

Microsoft

2026-02-18

overview

hypervelocity engineering

prompt engineering

github copilot

ai workflows

custom agents

copilot instructions

rpi methodology

3

Hypervelocity Engineering (HVE) Core is an enterprise-ready prompt engineering framework for GitHub Copilot. Constraint-based AI workflows, validated artifacts, and structured methodologies that scale from solo developers to large teams.

Tip

Automated installation via thehve-core-installeragent in VS Code (~30 seconds)

## Overview

HVE Core provides specialized agents, reusable prompts, instruction sets, and skills with JSON schema validation. The framework separates AI concerns into distinct artifact types with clear boundaries, preventing runaway behavior through constraint-based design.

The RPI (Research → Plan → Implement) methodology structures complex engineering tasks into phases where AI knows what it cannot do, changing optimization targets from "plausible code" to "verified truth."

## Quick Start

### 1. Install

Install the VS Code extension from the Marketplace:

Need a different installation method? See theInstallation Guidefor CLI plugins, submodules, multi-root workspaces, and more.

### 2. Verify

Open GitHub Copilot Chat (Ctrl+Alt+I) and check that HVE Core agents appear in the agent picker. Look fortask-researcher,task-planner, andrpi-agent.

### 3. Try It

Select thememoryagent and type:

Remember that I'm exploring HVE Core for the first time.

The agent creates a memory file in your workspace. You now have a working HVE Core installation that responds to natural language.

Ready to go deeper? Follow theGetting Started Guide.

## Documentation

Full documentation is available athttps://microsoft.github.io/hve-core/.

Guide

Description

Getting Started

Setup and first workflow tutorial

RPI Workflow

Deep dive into Research, Plan, Implement

Contributing

Create custom agents, instructions, and prompts

Agents Reference

All available agents

Instructions Reference

All coding instructions

## What's Included

Component

Count

Description

Documentation

Agents

35

Specialized AI assistants for research, planning, and implementation

Agents

Instructions

68

Repository-specific coding guidelines applied automatically

Instructions

Prompts

40

Reusable templates for common tasks like commits and PRs

Prompts

Skills

2

Self-contained packages with cross-platform scripts and guidance

Skills

Scripts

N/A

Validation tools for linting, security, and quality

Scripts

## Prompt Engineering Framework

HVE Core provides a structured approach to prompt engineering with four artifact types, each serving a distinct purpose:

Artifact

Purpose

Activation

Instructions

Passive reference guidance applied by file pattern

Automatic via
applyTo
 glob

Prompts

Task-specific procedures with input variables

Manual via
/
 command

Agents

Specialized personas with tool access and constraints

Manual via agent picker

Skills

Executable utilities with cross-platform scripts

Read by Copilot on demand

### Key Capabilities

* Protocol patterns support step-based (sequential) and phase-based (conversational) workflow formats
* Input variables use${input:variableName}syntax with defaults and VS Code integration
* Subagent delegation provides a first-class pattern for tool-heavy work viarunSubagent
* Maturity lifecycle follows a four-stage model (experimental→preview→stable→deprecated)

Use theprompt-builderagent to create new artifacts following these patterns.

## Enterprise Validation Pipeline

All AI artifacts are validated through a CI/CD pipeline with JSON schema enforcement:

*.instructions.md → instruction-frontmatter.schema.json
*.prompt.md → prompt-frontmatter.schema.json
*.agent.md → agent-frontmatter.schema.json
SKILL.md → skill-frontmatter.schema.json

The validation system provides:

* Typed frontmatter validation provides structured error reporting.
* Pattern-based schema mapping enables automatic file type detection.
* Maturity enforcement ensures artifacts declare stability level.
* Link and language checks validate cross-references.

Runnpm run lint:frontmatterlocally before committing changes.

## Project Structure

.github/
├── agents/ # Specialized Copilot chat assistants
├── instructions/ # Repository-specific coding guidelines
├── prompts/ # Reusable prompt templates
├── skills/ # Self-contained executable packages
└── workflows/ # CI/CD pipeline definitions
docs/
├── getting-started/ # Installation and first workflow guides
├── rpi/ # Research, Plan, Implement methodology
├── contributing/ # Artifact authoring guidelines
└── architecture/ # System design documentation
extension/ # VS Code extension source
scripts/
├── collections/ # Collection validation and helper modules
├── extension/ # Extension packaging and preparation
├── lib/ # Shared utilities
├── linting/ # Markdown, frontmatter, YAML validation
├── plugins/ # Plugin generation
├── security/ # Dependency pinning and SHA checks
└── tests/ # Pester test suites

## Contributing

We appreciate contributions! Whether you're fixing typos or adding new components:

1. Read ourContributing Guide
2. Check outopen issues
3. Join thediscussion

## Responsible AI

Microsoft encourages customers to review its Responsible AI Standard when developing AI-enabled systems to ensure ethical, safe, and inclusive AI practices. Learn more atMicrosoft's Responsible AI.

## Legal

This project is licensed under theMIT License.

SeeSECURITY.mdfor the security policy and vulnerability reporting.

SeeGOVERNANCE.mdfor the project governance model.

## Trademark Notice

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow Microsoft's Trademark & Brand Guidelines. Use of Microsoft trademarks or logos in
modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or
logos are subject to those third-party's policies.

🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.

## About

A refined collection of Hypervelocity Engineering components (instructions, prompts, agents) to start your project off right, or upgrade your existing projects to get the most out of all Copilots

### Resources

 Readme



### License

 MIT license


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

158

 stars


### Watchers

7

 watching


### Forks

64

 forks


 Report repository



## Releases18

hve-core: v3.0.2

 Latest



Feb 21, 2026



+ 17 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors36

+ 22 contributors

## Languages

* PowerShell99.7%
* Other0.3%
