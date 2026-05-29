---
title: 'GitHub - 0-AI-UG/cate: An infinite zoomable canvas for coding — editor, terminal, and browser panels in a spatial workspace. · GitHub'
url: https://github.com/0-AI-UG/cate
site_name: tldr
content_file: tldr-github-0-ai-ugcate-an-infinite-zoomable-canvas-for
fetched_at: '2026-05-29T12:07:01.701287'
original_url: https://github.com/0-AI-UG/cate
date: '2026-05-29'
description: An infinite zoomable canvas for coding — editor, terminal, and browser panels in a spatial workspace. - 0-AI-UG/cate
tags:
- tldr
---

0-AI-UG

 

/

cate

Public

* NotificationsYou must be signed in to change notification settings
* Fork41
* Star691

 
 
 
 
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

343 Commits
343 Commits
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
build
build
 
 
e2e
e2e
 
 
scripts
scripts
 
 
src
src
 
 
.gitignore
.gitignore
 
 
.nvmrc
.nvmrc
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.de.md
README.de.md
 
 
README.fr.md
README.fr.md
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
electron-builder.yml
electron-builder.yml
 
 
electron.vite.config.ts
electron.vite.config.ts
 
 
index.html
index.html
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
postcss.config.js
postcss.config.js
 
 
tailwind.config.ts
tailwind.config.ts
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.node.json
tsconfig.node.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

# Cate

English|Français|简体中文|Deutsch

A spatial desktop IDE with an infinite canvas for code, terminals, browsers, documents, AI agents, and git.

Current source version:v1.0.4

Cate is an Electron desktop app for arranging development tools in freeform space. Mix floating canvas panels with docked tabs and splits, detach panels into standalone windows, and keep multiple workspaces synced across sessions.

## Getting Started

Open any folder to create a workspace — Cate restores your canvas layout, panel positions, and open terminals every time you come back. Right-click the canvas to add panels, pressCmd+Kfor the command palette, or drag panels onto the dock to create tabs and splits.

No configuration files, no project setup — just point Cate at a directory and start working.

## Why Cate?

Alt-tab works fine — until you have 12 terminals, 6 files open, docs in another window, and notes scattered across desktops. At that point switching windows becomes the actual bottleneck.

Cate replaces that pile of windows withone persistent canvas per project. Terminals, editors, browsers, and notes sit where you put them, grouped how you think about them, and they're still there when you come back the next day.

Cate isnot a window manager replacement. Tiling/scrolling WMs (Hyprland, Niri, GlazeWM, KDE) are great if you mainly want to arrange OS windows. Cate is a spatial canvas around a single project's tools — closer to Figma's infinite canvas than to a WM.

## Features

### 🎨 Canvas & Layout

* Infinite canvas— zoom, pan, and arrange panels anywhere in freeform space. Pan with two-finger drag or right-click drag; zoom withCmd+scrollor the canvas controls.
* Dock system— drag floating panels onto the dock to create tabs and splits. Each dock zone (center, left, right, bottom) can hold multiple tabs with type-colored icons.
* Detached windows— pull panels or full dock layouts into separate OS windows.
* Saved layouts— name, save, load, and delete canvas arrangements (nodes and regions) from an in-app modal (Cmd+K → "Saved Layouts…").
* Multi-workspace sessions— keep several projects open and restore them on restart. Switch between workspaces from the sidebar.

### 💻 Code, Docs & Terminals

* Monaco Editor panels— full VS Code-grade editing with syntax highlighting, multi-cursor, find/replace, diff support, and Markdown Preview/Source mode with GFM rendering. Scratch editors persist unsaved content across sessions.
* Persistent editor buffers— file-backed models are reused across panels, and scratch editor content persists with the session.
* Document panels— native canvas viewers for PDFs, DOCX files, and images, with file type detection backed by magic-byte checks.
* Native terminals— xterm.js with WebGL rendering, backed bynode-ptyPTYs rooted in the active workspace. Shell auto-detection with graceful fallback if the configured shell is unavailable.
* Browser panels— embedded webview panels for previewing documentation, dev servers, or any URL. Context-isolated with hardened security settings.

### 🔧 Git & Source Control

* Git-aware file explorer— file tree with live filesystem watching, tracked/untracked dimming, search, and copy/paste for files and folders with collision-safe renaming.
* Source control sidebar— stage/unstage, branch management, worktrees, commit history, and inline diff views. Git monitor polls and surfaces changes automatically.
* Project-wide search— full-text search across workspace files with instant results.

### 🤖 AI Agent

* Pi Agent panel— run an in-app coding agent powered by@earendil-works/pi-agent-core, with chat threads, per-chat model restore, and workspace-aware panel placement.
* Provider auth & models— connect OAuth providers such as Anthropic, OpenAI Codex, and GitHub Copilot, or API-key providers such as OpenAI, Google Gemini, OpenRouter, Groq, Mistral, DeepSeek, and more.
* Marketplace & plan mode— install Pi extensions from the marketplace and use Cate's bundled plan-mode helper for agent-guided implementation planning.

### 🔍 Search & Navigation

* Canvas-wide search(Cmd+Shift+F) — Spotlight-style overlay that searches workspace files, live terminal scrollback, and open panel titles/paths in one place. Recent-focus ranked results with colored type-tile icons.
* Panel switcher(Ctrl+Space) — compact keyboard overlay for jumping between open canvas panels and centering the selected node.
* Command palette(Cmd+K) — quick access to commands, open panels, and workspace files. Unified Spotlight-style chrome across all overlays.

### 🖥️ Desktop Polish

* Auto-save & session restore— all panel state, positions, and open files persist automatically.
* Optional macOS native window tabs— group Cate windows in the system tab bar.
* Auto-update checks— checks GitHub releases and notifies when a new version is available.
* Crash resilience— Sentry diagnostics, session restore validation, shell fallback banners in the PTY, and guarded update/restart flows help prevent noisy or looping crash states.

## Install

If you just want to use Cate, download a prebuilt release — don't build from source. This repository currently targetsv1.0.4.

Platform

Formats

Link

macOS

DMG, ZIP (
arm64
, 
x64
)

Latest release

Windows

NSIS installer, ZIP (
x64
)

Latest release

Linux

AppImage, DEB, 
tar.gz
 (
x64
)

Latest release

macOS note:release builds are notarized and configured for hardened runtime. Unsigned local or test builds may require:

xattr -cr /Applications/Cate.app

Linux note:on Steam Deck or other read-only-root distros, prefer thetar.gzportable build. If the AppImage fails to launch, try--no-sandboxas a fallback (e.g../Cate.AppImage --no-sandbox).

## Build from Source

The steps below are forcontributors— use the prebuilt release above for daily use.

### Prerequisites

* Node.js20 or 22 LTS (see.nvmrc). Node 23+ is not supported;node-ptyhas no prebuilds and native compilation will fail.
* npm >= 9
* Python 3 and a C++ compiler (fornode-ptynative module)macOS: Xcode Command Line Tools (xcode-select --install)Debian/Ubuntu:sudo apt install build-essential python3Fedora/RHEL:sudo dnf install @development-tools gcc-c++ make python3Arch:sudo pacman -S base-devel pythonWindows:Visual Studio Build Tools(select the "Desktop development with C++" workload)
* macOS: Xcode Command Line Tools (xcode-select --install)
* Debian/Ubuntu:sudo apt install build-essential python3
* Fedora/RHEL:sudo dnf install @development-tools gcc-c++ make python3
* Arch:sudo pacman -S base-devel python
* Windows:Visual Studio Build Tools(select the "Desktop development with C++" workload)

### Setup

git clone https://github.com/0-AI-UG/cate.git

cd
 cate
npm install

### Development

npm run dev

This starts the Electron app with hot reload via electron-vite.

### Quality Checks

npm run typecheck
npm 
test
 
#
 unit tests (vitest)

npm run test:e2e 
#
 Playwright integration tests

For the Electron smoke test harness:

npm run test:smoke:electron

### Production Build

npm run build

### Package for Distribution

npm run package

#
 or target one platform:

npm run package:mac
npm run package:win
npm run package:linux

Packaged binaries will be in therelease/directory.

## Security & Packaging

Cate uses a context-isolated preload bridge for all IPC communication. Filesystem access is scoped to registered workspace roots, browser panels use hardened webview settings with disabled node integration, and the updater falls back to opening the GitHub release page when a verified installer path is unavailable. Workspace-scopedallowedRootsvalidation prevents terminals from spawning outside approved directories.

## Architecture

src/
├── agent/ # Embedded Pi coding-agent integration
│ ├── main/ # Agent process manager, auth, marketplace, session files
│ ├── renderer/ # Agent panel UI, chat thread, providers, model prefs
│ └── extensions/ # Bundled Cate plan-mode Pi extension
├── main/ # Electron main process
│ ├── ipc/ # IPC handlers (filesystem, git, terminal, menu, drag)
│ ├── analytics # Update/app event analytics helpers
│ ├── appContext # Shared main-process app state
│ ├── featureFlags # Runtime feature flags
│ ├── shellEnv # Login-shell environment capture
│ ├── shellResolver # Shell path resolution with fallback chain
│ ├── workspaceManager# Workspace lifecycle and session persistence
│ ├── workspaceRoots # Allowed-roots registration and validation
│ ├── windowRegistry # Window management (main, dock, detached)
│ ├── webSecurity # Webview hardening and CSP
│ ├── auto-updater # Update checks and release fetch
│ ├── sentry # Sentry integration
│ ├── store # electron-store persistence
│ ├── jsonFileStore # JSON-backed file persistence helpers
│ ├── menu # Application menu
│ └── sessionTrust # Session restore validation
├── preload/ # Context-isolated bridge exposed to the renderer
├── renderer/ # React 18 application
│ ├── assets/ # Renderer images and asset declarations
│ ├── canvas/ # Infinite canvas rendering, drag, resize, placement
│ ├── docking/ # Tabs, splits, detached dock windows, drag/drop
│ ├── drag/ # Cross-window drag-and-drop runtime and state
│ ├── panels/ # Terminal, Editor, Browser, Document, Git, Explorer,
│ │ # Projects, Canvas panel registry/components
│ ├── sidebar/ # Workspace, File Explorer, Source Control,
│ │ # Parallel Work, Project List, fileClipboard
│ ├── dialogs/ # Saved layouts and post-update feedback dialogs
│ ├── settings/ # Settings window sections and shortcut recorder
│ ├── ui/ # CommandPalette, GlobalSearch, NodeSwitcher,
│ │ # WelcomePage, ShortcutHintOverlay
│ ├── shells/ # Main, panel, and dock window shells
│ ├── stores/ # Zustand stores (canvas, app, dock, settings,
│ │ # shortcut, status, ui, update, url prompt)
│ ├── hooks/ # Custom React hooks (shortcuts, canvas interaction)
│ ├── lib/ # Utilities (coordinates, routing, terminal registry)
│ ├── workers/ # Monaco/editor workers
│ └── styles/ # Tailwind/global styles
└── shared/ # IPC channel definitions and shared TypeScript types

### Tech Stack

* Electron 41— desktop shell (Chromium + Node.js)
* React 18— UI framework with functional components and hooks
* Zustand 5— lightweight state management (no Redux/Context)
* Monaco Editor 0.52— code editing (VS Code's editor component)
* xterm.js 5.5 + node-pty 1.0— terminal emulator with WebGL renderer
* @earendil-works/pi packages— embedded coding-agent runtime, provider auth, and extension marketplace
* pdf.js + mammoth— native PDF and DOCX document rendering
* react-markdown + remark-gfm— Markdown preview with GitHub Flavored Markdown
* simple-git 3.27— git operations
* chokidar 4.0— filesystem watching
* @phosphor-icons/react— app iconography
* Tailwind CSS 3.4— styling
* electron-vite 5.0— bundling with HMR
* electron-builder 26— packaging and distribution
* electron-updater 6.8— update checks
* Sentry Electron 5— crash reporting and diagnostics
* Playwright— end-to-end integration tests
* Vitest— unit test runner

## Roadmap

Cate is under active development. For a detailed history of what changed in each release and a sense of where things are headed, see theCHANGELOG.

## Star History

## Contributing

SeeCONTRIBUTING.mdfor guidelines.

## License

MIT

## About

An infinite zoomable canvas for coding — editor, terminal, and browser panels in a spatial workspace.

cate.cero-ai.com

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

691

 stars
 

### Watchers

3

 watching
 

### Forks

41

 forks
 

 Report repository

 

## Releases46

v1.0.4

 Latest

 

May 28, 2026

 

+ 45 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript99.1%
* Other0.9%