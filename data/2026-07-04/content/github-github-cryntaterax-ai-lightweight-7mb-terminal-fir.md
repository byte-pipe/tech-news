---
title: 'GitHub - crynta/terax-ai: Lightweight (7MB) Terminal-first AI-native dev workspace · GitHub'
url: https://github.com/crynta/terax-ai
site_name: github
content_file: github-github-cryntaterax-ai-lightweight-7mb-terminal-fir
fetched_at: '2026-07-04T11:32:35.569510'
original_url: https://github.com/crynta/terax-ai
author: crynta
description: Lightweight (7MB) Terminal-first AI-native dev workspace - crynta/terax-ai
---

crynta

 

/

terax-ai

Public

* NotificationsYou must be signed in to change notification settings
* Fork856
* Star7.9k

 
 
 
 
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

516 Commits
516 Commits
.github
.github
 
 
.vscode
.vscode
 
 
docs
docs
 
 
nix
nix
 
 
public
public
 
 
scripts
scripts
 
 
src-tauri
src-tauri
 
 
src
src
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.gitignore
.gitignore
 
 
.size-limit.json
.size-limit.json
 
 
AGENTS.md
AGENTS.md
 
 
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
 
 
TERAX.md
TERAX.md
 
 
biome.json
biome.json
 
 
components.json
components.json
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
index.html
index.html
 
 
knip.json
knip.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
settings.html
settings.html
 
 
terax-icon.png
terax-icon.png
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.node.json
tsconfig.node.json
 
 
vite.config.ts
vite.config.ts
 
 
View all files

## Repository files navigation

# Terax

Lightweight Terminal-first AI-native dev workspace.

Website·Docs·Website's source code

Terax is a lightweight open-source terminal (ADE) built on Tauri 2 + Rust and React 19. A native PTY backend with a WebGL renderer, an agentic AI side-panel that runs against your own keys or fully local models, plus a code editor, file explorer, source control with a git graph, and a web preview pane built in. About 7-8 MB on disk. No telemetry. No account.

## Screenshots

Multi-tab terminal with WebGL rendering

Custom themes, presets, and background images

Web preview of local dev servers

Source control panel with git graph in history

Agentic AI workflow with edit diffs in the code editor

## Features

### Terminal

* xterm.js with WebGL renderer, multi-tab with background streaming
* GPU-accelerated block-based terminal with editor-like command input
* Native PTY backend viaportable-pty(zsh, bash, pwsh, fish, cmd)
* Split panels (horizontal and vertical)
* Inline search, link detection, true-color
* Per-tab workspace environments on Windows (Local, or any installed WSL distro)

### Code editor

* CodeMirror 6 (supports all popular languages - TS/JS, Rust, Python, Go, C/C++, Java, HTML/CSS, JSON, Markdown, etc.)
* Inline AI autocomplete with local model support
* AI edit diffs, accept or reject hunk by hunk
* Vim mode
* Ten built-in editor themes: Atom One, Aura, Copilot, GitHub Dark / Light, Gruvbox Dark, Nord, Tokyo Night, Xcode Dark / Light

### Source control

* Stage / unstage hunks, commit (Cmd+Enter / Ctrl+Enter), push with upstream awareness
* Branch display including detached HEAD state
* Git history pane with a real commit graph (lane rendering for merges and branches)
* Commit search and filter, click through to the remote commit page

### File explorer

* Catppuccin icon theme
* Fuzzy search, keyboard navigation, inline rename, context actions
* Attach files and selections directly to the AI side-panel

### Web preview

* Auto-detects local dev servers and opens them in a preview tab
* External URL preview via a native child webview

### Themes and customization

* Custom themes built in-app, switch between bundled presets and your own
* Create your own themes, share them or import from the community
* Background images with adjustable opacity and blur
* Editor theme is independent from the app theme

### AI

* BYOK providers:OpenAI, Anthropic, Google (Gemini), Groq, xAI (Grok), Cerebras, OpenRouter, DeepSeek, Mistral, plus any OpenAI-compatible endpoint
* Local / offline:LM Studio, MLX, Ollama
* Agentic workflow:plans, sub-agents, project memory viaTERAX.md, file read / write / edit / multi-edit / grep / glob, bash with approval gating, background processes
* Composer:snippets via#handle, files via@path, slash commands, voice input, attach-to-agent from explorer or selection
* Custom agentswith their own system prompt and tool subset
* Plan modefor multi-step work, generates and confirms before doing

## Install

Latest installers are on theReleasespage. Terax auto-updates from there.

### Windows notes

* On first launch Windows shows "Windows protected your PC" because Terax isn't code-signed yet. ClickMore infothenRun anyway.
* Default shell detection:pwsh.exe(PowerShell 7+) ->powershell.exe(Windows PowerShell 5.1) ->cmd.exe.
* WSL is a first-class workspace environment, not a wrapped subprocess.

### Linux notes

* Arch / AUR:yay -S terax-bin(orparu, etc.). Tracks the latest release.
* NixOS / Nix: use the official flake —nix profile install github:crynta/terax-ai(non-NixOS), or import the flake and addinputs.terax.packages.${pkgs.system}.teraxtoenvironment.systemPackages(NixOS). ThenixosModules.teraxoutput is also available for a simpler setup.
* AppImage:needs FUSE. Without it:./Terax_*.AppImage --appimage-extract-and-run. On Wayland with rendering glitches, tryWEBKIT_DISABLE_DMABUF_RENDERER=1. Otherwise the.deb/.rpmpackages link against the system GTK stack and tend to be smoother.

## Configure AI

1. OpenSettings -> AI.
2. Pick a provider and paste your API key. For local inference, point Terax at your LM Studio / MLX / Ollama endpoint.
3. Keys are written to the OS keychain viakeyring. They never touch disk or localStorage.

## Build from source

Prerequisites

* Rust (stable),https://rustup.rs
* Node 20+ andpnpm
* Tauri prerequisites for your platform,https://tauri.app/start/prerequisites/

Run

pnpm install
pnpm tauri dev 
#
 development

pnpm tauri build 
#
 production bundle

Checks

pnpm 
exec
 tsc --noEmit 
#
 frontend type-check

cd
 src-tauri 
&&
 cargo clippy --all-targets --locked -D warnings 
#
 Rust lint (matches CI)

cd
 src-tauri 
&&
 cargo 
test
 --locked 
#
 Rust tests

## Tech stack

Tauri 2, Rust,portable-pty, React 19, TypeScript, Vite, xterm.js, CodeMirror 6, Vercel AI SDK v6, Tailwind v4, shadcn/ui, Zustand.

## Contributing

Issues and PRs are welcome! Feel free to open issues, suggest features, or submit pull requests. SeeCONTRIBUTING.mdfor more details.

## License

Terax is licensed under the Apache-2.0 License. For more information on our dependencies, seeApache License 2.0.

## Star history

## About

Lightweight (7MB) Terminal-first AI-native dev workspace

terax.app

### Topics

 windows

 macos

 linux

 rust

 terminal

 ai

 reactjs

 code-editor

 agents

 xterm-js

 tauri

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
 

### Stars

7.9k

 stars
 

### Watchers

32

 watching
 

### Forks

856

 forks
 

 Report repository

 

## Releases14

Terax v0.8.2

 Latest

 

Jun 23, 2026

 

+ 13 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript79.4%
* Rust18.4%
* CSS1.0%
* Shell0.5%
* PowerShell0.2%
* JavaScript0.2%
* Other0.3%