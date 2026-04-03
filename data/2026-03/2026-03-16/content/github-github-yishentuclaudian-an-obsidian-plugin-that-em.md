---
title: 'GitHub - YishenTu/claudian: An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault · GitHub'
url: https://github.com/YishenTu/claudian
site_name: github
content_file: github-github-yishentuclaudian-an-obsidian-plugin-that-em
fetched_at: '2026-03-16T11:23:18.316393'
original_url: https://github.com/YishenTu/claudian
author: YishenTu
description: An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault - YishenTu/claudian
---

YishenTu

 

/

claudian

Public

* NotificationsYou must be signed in to change notification settings
* Fork233
* Star3.9k

 
 
 
 
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

513 Commits
513 Commits
.github/
workflows
.github/
workflows
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
.env.local.example
.env.local.example
 
 
.eslintrc.cjs
.eslintrc.cjs
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
Preview.png
Preview.png
 
 
README.md
README.md
 
 
esbuild.config.mjs
esbuild.config.mjs
 
 
jest.config.js
jest.config.js
 
 
manifest.json
manifest.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.jest.json
tsconfig.jest.json
 
 
tsconfig.json
tsconfig.json
 
 
versions.json
versions.json
 
 
View all files

## Repository files navigation

# Claudian

An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault. Your vault becomes Claude's working directory, giving it full agentic capabilities: file read/write, search, bash commands, and multi-step workflows.

## Features

* Full Agentic Capabilities: Leverage Claude Code's power to read, write, and edit files, search, and execute bash commands, all within your Obsidian vault.
* Context-Aware: Automatically attach the focused note, mention files with@, exclude notes by tag, include editor selection (Highlight), and access external directories for additional context.
* Vision Support: Analyze images by sending them via drag-and-drop, paste, or file path.
* Inline Edit: Edit selected text or insert content at cursor position directly in notes with word-level diff preview and read-only tool access for context.
* Instruction Mode (#): Add refined custom instructions to your system prompt directly from the chat input, with review/edit in a modal.
* Slash Commands: Create reusable prompt templates triggered by/command, with argument placeholders,@filereferences, and optional inline bash substitutions.
* Skills: Extend Claudian with reusable capability modules that are automatically invoked based on context, compatible with Claude Code's skill format.
* Custom Agents: Define custom subagents that Claude can invoke, with support for tool restrictions and model overrides.
* Claude Code Plugins: Enable Claude Code plugins installed via the CLI, with automatic discovery from~/.claude/pluginsand per-vault configuration. Plugin skills, agents, and slash commands integrate seamlessly.
* MCP Support: Connect external tools and data sources via Model Context Protocol servers (stdio, SSE, HTTP) with context-saving mode and@-mention activation.
* Advanced Model Control: Select between Haiku, Sonnet, and Opus, configure custom models via environment variables, fine-tune thinking budget, and enable Sonnet with 1M context window (requires Max subscription).
* Plan Mode: Toggle plan mode via Shift+Tab in the chat input. Claudian explores and designs before implementing, presenting a plan for approval with options to approve in a new session, continue in the current session, or provide feedback.
* Security: Permission modes (YOLO/Safe/Plan), safety blocklist, and vault confinement with symlink-safe checks.
* Claude in Chrome: Allow Claude to interact with Chrome through theclaude-in-chromeextension.

## Requirements

* Claude Code CLIinstalled (strongly recommend install Claude Code via Native Install)
* Obsidian v1.8.9+
* Claude subscription/API or Custom model provider that supports Anthropic API format (Openrouter,Kimi,GLM,DeepSeek, etc.)
* Desktop only (macOS, Linux, Windows)

## Installation

### From GitHub Release (recommended)

1. Downloadmain.js,manifest.json, andstyles.cssfrom thelatest release
2. Create a folder calledclaudianin your vault's plugins folder:/path/to/vault/.obsidian/plugins/claudian/
3. Copy the downloaded files into theclaudianfolder
4. Enable the plugin in Obsidian:* Settings → Community plugins → Enable "Claudian"

### Using BRAT

BRAT(Beta Reviewers Auto-update Tester) allows you to install and automatically update plugins directly from GitHub.

1. Install the BRAT plugin from Obsidian Community Plugins
2. Enable BRAT in Settings → Community plugins
3. Open BRAT settings and click "Add Beta plugin"
4. Enter the repository URL:https://github.com/YishenTu/claudian
5. Click "Add Plugin" and BRAT will install Claudian automatically
6. Enable Claudian in Settings → Community plugins

Tip: BRAT will automatically check for updates and notify you when a new version is available.

### From source (development)

1. Clone this repository into your vault's plugins folder:cd/path/to/vault/.obsidian/plugins
git clone https://github.com/YishenTu/claudian.gitcdclaudian
2. Install dependencies and build:npm install
npm run build
3. Enable the plugin in Obsidian:* Settings → Community plugins → Enable "Claudian"

### Development

#
 Watch mode

npm run dev

#
 Production build

npm run build

Tip: Copy.env.local.exampleto.env.localornpm installand setup your vault path to auto-copy files during development.

## Usage

Two modes:

1. Click the bot icon in ribbon or use command palette to open chat
2. Select text + hotkey for inline edit

Use it like Claude Code—read, write, edit, search files in your vault.

### Context

* File: Auto-attaches focused note; type@to attach other files
* @-mention dropdown: Type@to see MCP servers, agents, external contexts, and vault files@Agents/shows custom agents for selection@mcp-serverenables context-saving MCP servers@folder/filters to files from that external context (e.g.,@workspace/)Vault files shown by default
* @Agents/shows custom agents for selection
* @mcp-serverenables context-saving MCP servers
* @folder/filters to files from that external context (e.g.,@workspace/)
* Vault files shown by default
* Selection: Select text in editor, or elements in canvas, then chat—selection included automatically
* Images: Drag-drop, paste, or type path; configure media folder for![[image]]embeds
* External contexts: Click folder icon in toolbar for access to directories outside vault

### Features

* Inline Edit: Select text + hotkey to edit directly in notes with word-level diff preview
* Instruction Mode: Type#to add refined instructions to system prompt
* Slash Commands: Type/for custom prompt templates or skills
* Skills: Addskill/SKILL.mdfiles to~/.claude/skills/or{vault}/.claude/skills/, recommended to use Claude Code to manage skills
* Custom Agents: Addagent.mdfiles to~/.claude/agents/(global) or{vault}/.claude/agents/(vault-specific); select via@Agents/in chat, or prompt Claudian to invoke agents
* Claude Code Plugins: Enable plugins via Settings → Claude Code Plugins, recommended to use Claude Code to manage plugins
* MCP: Add external tools via Settings → MCP Servers; use@mcp-serverin chat to activate

## Configuration

### Settings

Customization

* User name: Your name for personalized greetings
* Excluded tags: Tags that prevent notes from auto-loading (e.g.,sensitive,private)
* Media folder: Configure where vault stores attachments for embedded image support (e.g.,attachments)
* Custom system prompt: Additional instructions appended to the default system prompt (Instruction Mode#saves here)
* Enable auto-scroll: Toggle automatic scrolling to bottom during streaming (default: on)
* Auto-generate conversation titles: Toggle AI-powered title generation after the first user message is sent
* Title generation model: Model used for auto-generating conversation titles (default: Auto/Haiku)
* Vim-style navigation mappings: Configure key bindings with lines likemap w scrollUp,map s scrollDown,map i focusInput

Hotkeys

* Inline edit hotkey: Hotkey to trigger inline edit on selected text
* Open chat hotkey: Hotkey to open the chat sidebar

Slash Commands

* Create/edit/import/export custom/commands(optionally override model and allowed tools)

MCP Servers

* Add/edit/verify/delete MCP server configurations with context-saving mode

Claude Code Plugins

* Enable/disable Claude Code plugins discovered from~/.claude/plugins
* User-scoped plugins available in all vaults; project-scoped plugins only in matching vault

Safety

* Load user Claude settings: Load~/.claude/settings.json(user's Claude Code permission rules may bypass Safe mode)
* Enable command blocklist: Block dangerous bash commands (default: on)
* Blocked commands: Patterns to block (supports regex, platform-specific)
* Allowed export paths: Paths outside the vault where files can be exported (default:~/Desktop,~/Downloads). Supports~,$VAR,${VAR}, and%VAR%(Windows).

Environment

* Custom variables: Environment variables for Claude SDK (KEY=VALUE format, supportsexportprefix)
* Environment snippets: Save and restore environment variable configurations

Advanced

* Claude CLI path: Custom path to Claude Code CLI (leave empty for auto-detection)

## Safety and Permissions

Scope

Access

Vault

Full read/write (symlink-safe via 
realpath
)

Export paths

Write-only (e.g., 
~/Desktop
, 
~/Downloads
)

External contexts

Full read/write (session-only, added via folder icon)

* YOLO mode: No approval prompts; all tool calls execute automatically (default)
* Safe mode: Approval prompt per tool call; Bash requires exact match, file tools allow prefix match
* Plan mode: Explores and designs a plan before implementing. Toggle via Shift+Tab in the chat input

## Privacy & Data Use

* Sent to API: Your input, attached files, images, and tool call outputs. Default: Anthropic; custom endpoint viaANTHROPIC_BASE_URL.
* Local storage: Settings, session metadata, and commands stored invault/.claude/; session messages in~/.claude/projects/(SDK-native); legacy sessions invault/.claude/sessions/.
* No telemetry: No tracking beyond your configured API provider.

## Troubleshooting

### Claude CLI not found

If you encounterspawn claude ENOENTorClaude CLI not found, the plugin can't auto-detect your Claude installation. Common with Node version managers (nvm, fnm, volta).

Solution: Find your CLI path and set it in Settings → Advanced → Claude CLI path.

Platform

Command

Example Path

macOS/Linux

which claude

/Users/you/.volta/bin/claude

Windows (native)

where.exe claude

C:\Users\you\AppData\Local\Claude\claude.exe

Windows (npm)

npm root -g

{root}\@anthropic-ai\claude-code\cli.js

Note: On Windows, avoid.cmdwrappers. Useclaude.exeorcli.js.

Alternative: Add your Node.js bin directory to PATH in Settings → Environment → Custom variables.

### npm CLI and Node.js not in same directory

If using npm-installed CLI, check ifclaudeandnodeare in the same directory:

dirname 
$(
which claude
)

dirname 
$(
which node
)

If different, GUI apps like Obsidian may not find Node.js.

Solutions:

1. Install native binary (recommended)
2. Add Node.js path to Settings → Environment:PATH=/path/to/node/bin

Still having issues?Open a GitHub issuewith your platform, CLI path, and error message.

## Architecture

src/
├── main.ts # Plugin entry point
├── core/ # Core infrastructure
│ ├── agent/ # Claude Agent SDK wrapper (ClaudianService)
│ ├── agents/ # Custom agent management (AgentManager)
│ ├── commands/ # Slash command management (SlashCommandManager)
│ ├── hooks/ # PreToolUse/PostToolUse hooks
│ ├── images/ # Image caching and loading
│ ├── mcp/ # MCP server config, service, and testing
│ ├── plugins/ # Claude Code plugin discovery and management
│ ├── prompts/ # System prompts for agents
│ ├── sdk/ # SDK message transformation
│ ├── security/ # Approval, blocklist, path validation
│ ├── storage/ # Distributed storage system
│ ├── tools/ # Tool constants and utilities
│ └── types/ # Type definitions
├── features/ # Feature modules
│ ├── chat/ # Main chat view + UI, rendering, controllers, tabs
│ ├── inline-edit/ # Inline edit service + UI
│ └── settings/ # Settings tab UI
├── shared/ # Shared UI components and modals
│ ├── components/ # Input toolbar bits, dropdowns, selection highlight
│ ├── mention/ # @-mention dropdown controller
│ ├── modals/ # Instruction modal
│ └── icons.ts # Shared SVG icons
├── i18n/ # Internationalization (10 locales)
├── utils/ # Modular utility functions
└── style/ # Modular CSS (→ styles.css)

## Roadmap

* Claude Code Plugin support
* Custom agent (subagent) support
* Claude in Chrome support
* /compactcommand
* Plan mode
* rewindandforksupport (including/forkcommand)
* !commandsupport
* Tool renderers refinement
* 1M Opus and Sonnet models
* Codex SDK integration
* Hooks and other advanced features
* More to come!

## License

Licensed under theMIT License.

## Star History

## Acknowledgments

* Obsidianfor the plugin API
* Anthropicfor Claude and theClaude Agent SDK

## About

An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault

### Topics

 productivity

 ide

 obsidian

 obsidian-plugin

 claude-code

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

3.9k

 stars
 

### Watchers

13

 watching
 

### Forks

233

 forks
 

 Report repository

 

## Releases11

1.3.69

 Latest

 

Mar 16, 2026

 

+ 10 releases

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript96.7%
* CSS3.0%
* JavaScript0.3%