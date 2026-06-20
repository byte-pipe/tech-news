---
title: 'GitHub - tw93/Pake: 🤱🏻 Turn any webpage into a desktop app with one command. · GitHub'
url: https://github.com/tw93/Pake
site_name: github
content_file: github-github-tw93pake-turn-any-webpage-into-a-desktop-ap
fetched_at: '2026-06-20T11:42:14.737233'
original_url: https://github.com/tw93/Pake
author: tw93
description: 🤱🏻 Turn any webpage into a desktop app with one command. - tw93/Pake
---

tw93

 

/

Pake

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork10.7k
* Star53.1k

 
 
 
 
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

2,126 Commits
2,126 Commits
.agents/
skills
.agents/
skills
 
 
.claude
.claude
 
 
.github
.github
 
 
bin
bin
 
 
dist
dist
 
 
docs
docs
 
 
scripts
scripts
 
 
src-tauri
src-tauri
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmignore
.npmignore
 
 
.npmrc
.npmrc
 
 
.pnpmrc
.pnpmrc
 
 
.prettierignore
.prettierignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS.svg
CONTRIBUTORS.svg
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
LICENSE-EXCEPTION
LICENSE-EXCEPTION
 
 
README.md
README.md
 
 
README_CN.md
README_CN.md
 
 
TRADEMARK.md
TRADEMARK.md
 
 
action.yml
action.yml
 
 
default_app_list.json
default_app_list.json
 
 
icns2png.py
icns2png.py
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
rollup.config.js
rollup.config.js
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
tsconfig.json
tsconfig.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

#### English|简体中文

# Pake

Turn any webpage into a desktop app with one command, supports macOS, Windows, and Linux

## Features

* 🎐Lightweight: Nearly 20 times smaller than Electron packages, typically around 5M
* 🚀Fast: Built with Rust Tauri, much faster than traditional JS frameworks with lower memory usage
* ⚡Easy to use: One-command packaging via CLI or online building, no complex configuration needed
* 📦Feature-rich: Supports shortcuts, immersive windows, drag & drop, style customization, ad removal

## Getting Started

* Beginners: Download ready-madePopular Packagesor useOnline Buildingwith no environment setup required
* Developers: InstallCLI Toolfor one-command packaging of any website with customizable icons, window settings, and more
* Advanced Users: Clone the project locally forCustom Development, or checkAdvanced Usagefor style customization and feature enhancement
* Troubleshooting: CheckFAQfor common issues and solutions

## Popular Packages

WeRead
 
Mac

Windows

Linux

Twitter
 
Mac

Windows

Linux

Grok
 
Mac

Windows

Linux

DeepSeek
 
Mac

Windows

Linux

ChatGPT
 
Mac

Windows

Linux

Gemini
 
Mac

Windows

Linux

YouTube Music
 
Mac

Windows

Linux

YouTube
 
Mac

Windows

Linux

LiZhi
 
Mac

Windows

Linux

ProgramMusic
 
Mac

Windows

Linux

Excalidraw
 
Mac

Windows

Linux

XiaoHongShu
 
Mac

Windows

Linux

🏂 You can download more applications from 
Releases
. 
Click here to expand the shortcuts reference!

Mac

Windows/Linux

Function

⌘
 + 
[

Ctrl
 + 
←

Return to the previous page

⌘
 + 
]

Ctrl
 + 
→

Go to the next page

⌘
 + 
↑

Ctrl
 + 
↑

Auto scroll to top of page

⌘
 + 
↓

Ctrl
 + 
↓

Auto scroll to bottom of page

⌘
 + 
r

Ctrl
 + 
r

Refresh Page

⌘
 + 
w

Ctrl
 + 
w

Hide window, not quit

⌘
 + 
-

Ctrl
 + 
-

Zoom out the page

⌘
 + 
=

Ctrl
 + 
=

Zoom in the Page

⌘
 + 
0

Ctrl
 + 
0

Reset the page zoom

⌘
 + 
L

Ctrl
 + 
L

Copy Current Page URL

⌘
 + 
⇧
 + 
⌥
 + 
V

Ctrl
 + 
Shift
 + 
V

Paste and Match Style

⌘
 + 
⇧
 + 
H

Ctrl
 + 
Shift
 + 
H

Go to Home Page

⌘
 + 
⌥
 + 
I

Ctrl
 + 
Shift
 + 
I

Toggle Developer Tools (Debug Only)

⌘
 + 
⇧
 + 
⌫

Ctrl
 + 
Shift
 + 
Del

Clear Cache & Restart

In addition, double-click the title bar to switch to full-screen mode. For Mac users, you can also use the gesture to go to the previous or next page and drag the title bar to move the window. The new menu also offers options for navigation, zoom, and window controls.

## Command-Line Packaging

#
 Install Pake CLI

pnpm install -g pake-cli

#
 Basic usage - automatically fetches website icon

pake https://github.com --name GitHub

#
 Advanced usage with custom options

pake https://weekly.tw93.fun --name Weekly --icon https://cdn.tw93.fun/pake/weekly.icns --width 1200 --height 800 --hide-title-bar

First-time packaging requires environment setup and may be slower, subsequent builds are fast. For complete parameter documentation, seeCLI Usage Guide. Don't want to use CLI? TryGitHub Actions Online Building.

## Development

Requires Rust>=1.85and Node>=22(recommended LTS;>=18also works). For detailed installation guide, seeTauri documentation. If unfamiliar with development environment, use the CLI tool instead.

#
 Install dependencies

pnpm i

#
 Local development [right-click to open debug mode]

pnpm run dev

#
 Build application

pnpm run build

For style customization, feature enhancement, container communication and other advanced features, seeAdvanced Usage Documentation.

## Developers

Pake's development can not be without these Hackers. They contributed a lot of capabilities for Pake. Also, welcome to follow them! ❤️

## Support

* The most direct way to support me is gettingMole for Mac, my paid Mac cleanup app.
* If Pake helped you,share itwith friends or give it a star.
* Got ideas or bugs? Open an issue or PR, feel free to contribute your best AI model.
* I have two cats, TangYuan and Coke. If you think Pake delights your life, you can feed themcanned food 🥩.

These lovely people already did 🐱

## License

Pake is open source under GPL-3.0, seeLICENSEandPake Output Exception; apps you build with Pake are entirely yours to use and distribute. If you fork Pake into your own product, to avoid confusion please give it a different name and credit Pake as the source.

## About

🤱🏻 Turn any webpage into a desktop app with one command.

### Topics

 windows

 macos

 linux

 rust

 package

 youtube

 desktop

 gemini

 claude

 tauri

 hight-performance

 no-electron

 chatgpt

### Resources

 Readme

 

### License

 GPL-3.0, Unknown licenses found
 

### Licenses found

GPL-3.0

LICENSE

 

Unknown

LICENSE-EXCEPTION

 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

53.1k

 stars
 

### Watchers

259

 watching
 

### Forks

10.7k

 forks
 

 Report repository

 

## Releases46

V3.11.10

 Latest

 

Jun 18, 2026

 

+ 45 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* https://cats.tw93.fun?name=Pake

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust94.2%
* Dockerfile5.2%
* TypeScript0.6%