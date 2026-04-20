---
title: 'GitHub - manaflow-ai/cmux: Ghostty-based macOS terminal with vertical tabs and notifications for AI coding agents · GitHub'
url: https://github.com/manaflow-ai/cmux
site_name: github
content_file: github-github-manaflow-aicmux-ghostty-based-macos-termina
fetched_at: '2026-03-28T11:10:46.048211'
original_url: https://github.com/manaflow-ai/cmux
author: manaflow-ai
description: Ghostty-based macOS terminal with vertical tabs and notifications for AI coding agents - manaflow-ai/cmux
---

manaflow-ai



/

cmux

Public

* NotificationsYou must be signed in to change notification settings
* Fork760
* Star11k




 
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

1,893 Commits
1,893 Commits
.claude/
commands
.claude/
commands
 
 
.github
.github
 
 
AppIcon.icon
AppIcon.icon
 
 
Assets.xcassets
Assets.xcassets
 
 
CLI
CLI
 
 
GhosttyTabs.xcodeproj
GhosttyTabs.xcodeproj
 
 
Resources
Resources
 
 
Sources
Sources
 
 
cmuxTests
cmuxTests
 
 
cmuxUITests
cmuxUITests
 
 
daemon/
remote
daemon/
remote
 
 
design
design
 
 
docs
docs
 
 
ghostty @ bc9be90
ghostty @ bc9be90
 
 
homebrew-cmux @ a5f372e
homebrew-cmux @ a5f372e
 
 
node_modules
node_modules
 
 
scripts
scripts
 
 
skills
skills
 
 
tests
tests
 
 
tests_v2
tests_v2
 
 
vendor
vendor
 
 
web
web
 
 
.gitignore
.gitignore
 
 
.gitkeep
.gitkeep
 
 
.gitmodules
.gitmodules
 
 
.vercelignore
.vercelignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
PROJECTS.md
PROJECTS.md
 
 
Package.resolved
Package.resolved
 
 
Package.swift
Package.swift
 
 
README.ar.md
README.ar.md
 
 
README.bs.md
README.bs.md
 
 
README.da.md
README.da.md
 
 
README.de.md
README.de.md
 
 
README.es.md
README.es.md
 
 
README.fr.md
README.fr.md
 
 
README.it.md
README.it.md
 
 
README.ja.md
README.ja.md
 
 
README.km.md
README.km.md
 
 
README.ko.md
README.ko.md
 
 
README.md
README.md
 
 
README.no.md
README.no.md
 
 
README.pl.md
README.pl.md
 
 
README.pt-BR.md
README.pt-BR.md
 
 
README.ru.md
README.ru.md
 
 
README.th.md
README.th.md
 
 
README.tr.md
README.tr.md
 
 
README.uk.md
README.uk.md
 
 
README.vi.md
README.vi.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
README.zh-TW.md
README.zh-TW.md
 
 
THIRD_PARTY_LICENSES.md
THIRD_PARTY_LICENSES.md
 
 
TODO.md
TODO.md
 
 
bun.lock
bun.lock
 
 
cmux-Bridging-Header.h
cmux-Bridging-Header.h
 
 
cmux.entitlements
cmux.entitlements
 
 
ghostty.h
ghostty.h
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# cmux

A Ghostty-based macOS terminal with vertical tabs and notifications for AI coding agents

English |日本語|Tiếng Việt|简体中文|繁體中文|한국어|Deutsch|Español|Français|Italiano|Dansk|Polski|Русский|Bosanski|العربية|Norsk|Português (Brasil)|ไทย|Türkçe|ភាសាខ្មែរ|Українська

▶ Demo video·The Zen of cmux

## Features

### Notification rings

Panes get a blue ring and tabs light up when coding agents need your attention

### Notification panel

See all pending notifications in one place, jump to the most recent unread

### In-app browser

Split a browser alongside your terminal with a scriptable API ported from
agent-browser

### Vertical + horizontal tabs

Sidebar shows git branch, linked PR status/number, working directory, listening ports, and latest notification text. Split horizontally and vertically.

* Scriptable— CLI and socket API to create workspaces, split panes, send keystrokes, and automate the browser
* Native macOS app— Built with Swift and AppKit, not Electron. Fast startup, low memory.
* Ghostty compatible— Reads your existing~/.config/ghostty/configfor themes, fonts, and colors
* GPU-accelerated— Powered by libghostty for smooth rendering

## Install

### DMG (recommended)

Open the.dmgand drag cmux to your Applications folder. cmux auto-updates via Sparkle, so you only need to download once.

### Homebrew

brew tap manaflow-ai/cmux
brew install --cask cmux

To update later:

brew upgrade --cask cmux

On first launch, macOS may ask you to confirm opening an app from an identified developer. ClickOpento proceed.

## Why cmux?

I run a lot of Claude Code and Codex sessions in parallel. I was using Ghostty with a bunch of split panes, and relying on native macOS notifications to know when an agent needed me. But Claude Code's notification body is always just "Claude is waiting for your input" with no context, and with enough tabs open I couldn't even read the titles anymore.

I tried a few coding orchestrators but most of them were Electron/Tauri apps and the performance bugged me. I also just prefer the terminal since GUI orchestrators lock you into their workflow. So I built cmux as a native macOS app in Swift/AppKit. It uses libghostty for terminal rendering and reads your existing Ghostty config for themes, fonts, and colors.

The main additions are the sidebar and notification system. The sidebar has vertical tabs that show git branch, linked PR status/number, working directory, listening ports, and the latest notification text for each workspace. The notification system picks up terminal sequences (OSC 9/99/777) and has a CLI (cmux notify) you can wire into agent hooks for Claude Code, OpenCode, etc. When an agent is waiting, its pane gets a blue ring and the tab lights up in the sidebar, so I can tell which one needs me across splits and tabs. Cmd+Shift+U jumps to the most recent unread.

The in-app browser has a scriptable API ported fromagent-browser. Agents can snapshot the accessibility tree, get element refs, click, fill forms, and evaluate JS. You can split a browser pane next to your terminal and have Claude Code interact with your dev server directly.

Everything is scriptable through the CLI and socket API — create workspaces/tabs, split panes, send keystrokes, open URLs in the browser.

## The Zen of cmux

cmux is not prescriptive about how developers hold their tools. It's a terminal and browser with a CLI, and the rest is up to you.

cmux is a primitive, not a solution. It gives you a terminal, a browser, notifications, workspaces, splits, tabs, and a CLI to control all of it. cmux doesn't force you into an opinionated way to use coding agents. What you build with the primitives is yours.

The best developers have always built their own tools. Nobody has figured out the best way to work with agents yet, and the teams building closed products definitely haven't either. The developers closest to their own codebases will figure it out first.

Give a million developers composable primitives and they'll collectively find the most efficient workflows faster than any product team could design top-down.

## Documentation

For more info on how to configure cmux,head over to our docs.

## Keyboard Shortcuts

### Workspaces

Shortcut

Action

⌘ N

New workspace

⌘ 1–8

Jump to workspace 1–8

⌘ 9

Jump to last workspace

⌃ ⌘ ]

Next workspace

⌃ ⌘ [

Previous workspace

⌘ ⇧ W

Close workspace

⌘ ⇧ R

Rename workspace

⌘ B

Toggle sidebar

### Surfaces

Shortcut

Action

⌘ T

New surface

⌘ ⇧ ]

Next surface

⌘ ⇧ [

Previous surface

⌃ Tab

Next surface

⌃ ⇧ Tab

Previous surface

⌃ 1–8

Jump to surface 1–8

⌃ 9

Jump to last surface

⌘ W

Close surface

### Split Panes

Shortcut

Action

⌘ D

Split right

⌘ ⇧ D

Split down

⌥ ⌘ ← → ↑ ↓

Focus pane directionally

⌘ ⇧ H

Flash focused panel

### Browser

Browser developer-tool shortcuts follow Safari defaults and are customizable inSettings → Keyboard Shortcuts.

Shortcut

Action

⌘ ⇧ L

Open browser in split

⌘ L

Focus address bar

⌘ [

Back

⌘ ]

Forward

⌘ R

Reload page

⌥ ⌘ I

Toggle Developer Tools (Safari default)

⌥ ⌘ C

Show JavaScript Console (Safari default)

### Notifications

Shortcut

Action

⌘ I

Show notifications panel

⌘ ⇧ U

Jump to latest unread

### Find

Shortcut

Action

⌘ F

Find

⌘ G / ⌘ ⇧ G

Find next / previous

⌘ ⇧ F

Hide find bar

⌘ E

Use selection for find

### Terminal

Shortcut

Action

⌘ K

Clear scrollback

⌘ C

Copy (with selection)

⌘ V

Paste

⌘ + / ⌘ -

Increase / decrease font size

⌘ 0

Reset font size

### Window

Shortcut

Action

⌘ ⇧ N

New window

⌘ ,

Settings

⌘ ⇧ ,

Reload configuration

⌘ Q

Quit

## Nightly Builds

Download cmux NIGHTLY

cmux NIGHTLY is a separate app with its own bundle ID, so it runs alongside the stable version. Built automatically from the latestmaincommit and auto-updates via its own Sparkle feed.

Report nightly bugs onGitHub Issuesor in#nightly-bugs on Discord.

## Session restore (current behavior)

On relaunch, cmux currently restores app layout and metadata only:

* Window/workspace/pane layout
* Working directories
* Terminal scrollback (best effort)
* Browser URL and navigation history

cmux doesnotrestore live process state inside terminal apps. For example, active Claude Code/tmux/vim sessions are not resumed after restart yet.

## Star History

## Contributing

Ways to get involved:

* Follow us on X for updates@manaflowai,@lawrencecchen, and@austinywang
* Join the conversation onDiscord
* Create and participate inGitHub issuesanddiscussions
* Let us know what you're building with cmux

## Community

* Discord
* GitHub
* X / Twitter
* YouTube
* LinkedIn
* Reddit

## Founder's Edition

cmux is free, open source, and always will be. If you'd like to support development and get early access to what's coming next:

Get Founder's Edition

* Prioritized feature requests/bug fixes
* Early access: cmux AI that gives you context on every workspace, tab and panel
* Early access: iOS app with terminals synced between desktop and phone
* Early access: Cloud VMs
* Early access: Voice mode
* My personal iMessage/WhatsApp

## License

cmux is open source underAGPL-3.0-or-later.

If your organization cannot comply with AGPL, a commercial license is available. Contactfounders@manaflow.comfor details.

## About

Ghostty-based macOS terminal with vertical tabs and notifications for AI coding agents

cmux.com

### Topics

 tmux

 terminal

 amp

 opencode

 gemini

 codex

 ghostty

 claude-code

### Resources

 Readme



### License

 View license


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

11k

 stars


### Watchers

19

 watching


### Forks

760

 forks


 Report repository



## Releases27

v0.62.2

 Latest



Mar 14, 2026



+ 26 releases

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Swift76.4%
* Python16.8%
* TypeScript2.5%
* Shell2.0%
* Go1.8%
* C0.4%
* Other0.1%
