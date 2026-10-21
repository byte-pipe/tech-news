---
title: 'GitHub - wshobson/agents: Multi-harness agentic plugin marketplace for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Google Antigravity, and Pi · GitHub'
url: https://github.com/wshobson/agents
site_name: github
content_file: github-github-wshobsonagents-multi-harness-agentic-plugin
fetched_at: '2026-10-21T15:51:28.763927'
original_url: https://github.com/wshobson/agents
author: wshobson
description: Multi-harness agentic plugin marketplace for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Google Antigravity, and Pi - wshobson/agents
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

620 Commits
620 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
plugins
.agents/
plugins
 
 
.claude-plugin
.claude-plugin
 
 
.cursor-plugin
.cursor-plugin
 
 
.cursor/
rules
.cursor/
rules
 
 
.github
.github
 
 
docs
docs
 
 
evals
evals
 
 
plugins
plugins
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
.markdownlint.json
.markdownlint.json
 
 
AGENTS.md
AGENTS.md
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Plugins, agents, and skills for AI coding tools

Use one collection of plugins, agents, skills, and commands across Claude Code, OpenAI Codex CLI, Cursor, OpenCode, Antigravity CLI, GitHub Copilot, and Pi. A harness is the coding tool that loads and runs the components. Plugins cover Python and JavaScript development, code review, testing, infrastructure, security, and other work.

The catalog contains 94 plugins, including 92 local plugins and 2 external entries. The local source contains 202 agents, 185 skills, and 105 commands. The components share a Markdown source, with installation and capabilities adapted to each harness.

## Multi-harness support

Choose the harness you use and follow its setup route. Available components depend on the installation route and the harness's capabilities.

Tool

Installation

Components and limits

Claude Code

Plugin marketplace

Source agents, skills, and commands; plugin-specific hooks and MCP configuration

OpenAI Codex CLI

Native marketplace or generated artifacts

Native source skills; generated TOML agents and commands as skills use a separate route

Cursor

Plugin marketplace

Source agents, skills, and commands, with curated project rules

OpenCode

make install-opencode

Generated agents, skills, and commands, with translated tool permissions

Antigravity CLI

make install-antigravity

Generated plugins containing agents, skills, and commands

GitHub Copilot

make install-copilot

Generated agent profiles and skills; commands also become invocable skills

Pi

make install-pi

Generated skills and prompt templates; agents require a subagent extension

See thecapability matrixfor model mappings, tool permissions, hooks, and installation differences.

For individual skills, use askills-only installerand select your coding tool.

## Quick start

Choose a plugin for the work you do:

Plugin

Use it for

python-development

Python, Django, FastAPI, testing, and packaging

javascript-typescript

JavaScript and TypeScript development and project setup

developer-essentials

Code review, debugging, Git, and testing patterns

security-scanning

Security review, dependency checks, and code scanning

See theplugin catalogfor all 94 plugins and theusage guidefor commands and examples.

### Claude Code

Run these commands inside Claude Code to register the marketplace and install the Python development plugin:

/plugin marketplace add wshobson/agents
/plugin install python-development@claude-code-workflows

Then ask Claude to use the Python agents for your task, or run the plugin's scaffolding command:

/python-development:python-scaffold Create a FastAPI service with tests

### Codex CLI

Run these commands in a terminal with a current Codex CLI:

codex plugin marketplace add wshobson/agents
codex plugin add python-development@claude-code-workflows

The native Codex manifests expose source skills. The generated TOML agents and command-derived skills use a separate adapter path. Native installation also reads the original skill bodies, while generated copies split oversized bodies into reference files for the 8 KB budget. See theCodex setup detailsbefore choosing an installation route.

### Cursor

Cursor uses the committedplugin marketplace registry. Follow theCursor setup instructionsto add the marketplace and install a plugin.

### Skills only

Install an individual skill with GitHub CLI'sgh skillcommand or thenpx skillsinstaller. Select your coding tool when prompted. Both installers read skills from GitHub without cloning the repository and install them without the plugin's agents, commands, or hooks.

gh skill install wshobson/agents python-testing-patterns
npx skills add wshobson/agents --skill python-testing-patterns

gh skillrequires GitHub CLI 2.90 or later. Thenpxcommand requires Node.js and npm. Seeskills-only installationfor other agents, install scopes, and version pinning.

### Install from a clone

For OpenCode, Antigravity CLI, GitHub Copilot, and Pi, clone the repository and use the installer for your harness. Installuv, Python 3.12 or later, and the coding tool you want to use. The following clone command uses GitHub CLI:

gh repo clone wshobson/agents 
~
/agents

cd
 
~
/agents

Run the command for your tool. Each target generates the artifacts and links all local plugins into that tool's user configuration:

make install-opencode
make install-antigravity
make install-copilot
make install-pi

Pi's agents require its referencesubagentextension or a compatible extension. See theglobal install guidefor configuration paths and uninstall commands.

## What's inside

Component

Count

Purpose

Plugins

94

Installable groups of components, including 92 local plugins and 2 external entries

Agents

202

Instructions for specialist subagents that handle delegated work

Skills

185

Guidance and reference material that an agent loads when relevant

Commands

105

Named workflows you invoke, such as project scaffolding or a security scan

The agent, skill, and command counts cover local source files. External plugins provide their own components and installation requirements.

## How it works

A plugin groups related agents, skills, and commands underplugins/. For example,python-developmentcontains three agents, sixteen skills, and a scaffolding command. The chosen harness loads the installed components according to its own discovery and invocation rules.

Contributors maintain one Markdown source in the Claude Code plugin format. Native registries point to that source where supported, and adapters generate the formats needed by each harness. Commands may become skills or prompt templates, and agent formats, model choices, and tool permissions vary by harness.

Source agents specify model aliases such asopus,sonnet,haiku,fable, orinherit. Adapters map those aliases to each harness's model settings, including fixed defaults for someinheritentries. Seemodel configurationand theadapter mappings.

## Quality evaluation

The repository validates plugin structure, generated artifacts, and documentation. Contributors can run these checks from the repository root:

make generate-all
make validate STRICT=1
make garden

plugin-evalalso provides static skill checks without model calls. For example:

uv run --project plugins/plugin-eval plugin-eval score plugins/python-development/skills/python-testing-patterns --depth quick

The LLM judge and Monte Carlo layers are experimental and are not validated against human labels. Their scores describe model assessments and repeated simulations and do not prove that a task succeeds in a project. They require the optionalllmdependencies. Model calls useANTHROPIC_API_KEYwhen it is set and bill that API account. Otherwise they use your Claude Code login. See theevaluation guidefor setup and limits.

## Documentation map

Guide

Covers

Plugin catalog

Plugins by task and domain

Agents
 and 
skills

Available components and model configuration

Usage
 and 
tool setup

Commands, examples, and installation

Architecture
 and 
design details

Source layout and adapters

Quality evaluation
 and 
CLI verification

Checks and their limits

SeeCONTRIBUTING.mdto propose a change andauthoring conventionsto write plugin content.

## External memory integration

Pensyveremains an optional external Claude Code marketplace entry. Major7 Apps maintains Pensyve, and this repository's maintainer founded Major7 Apps. Its open-source runtime can run locally or on your own server.Pensyve Cloud closed on October 1, 2026, and its dashboard, API, and hosted MCP endpoints are unavailable. Use theself-hosting guidewhen configuring the runtime.

## License

The repository isMIT licensed. External plugins have their own licenses.

## Star history