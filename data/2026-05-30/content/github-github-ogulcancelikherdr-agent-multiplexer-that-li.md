---
title: 'GitHub - ogulcancelik/herdr: agent multiplexer that lives in your terminal. · GitHub'
url: https://github.com/ogulcancelik/herdr
site_name: github
content_file: github-github-ogulcancelikherdr-agent-multiplexer-that-li
fetched_at: '2026-05-30T19:33:57.748064'
original_url: https://github.com/ogulcancelik/herdr
author: ogulcancelik
description: agent multiplexer that lives in your terminal. Contribute to ogulcancelik/herdr development by creating an account on GitHub.
---

ogulcancelik

 

/

herdr

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork209
* Star3.2k

 
 
 
 
master
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

653 Commits
653 Commits
.codex/
skills/
herdr-pre-release-audit
.codex/
skills/
herdr-pre-release-audit
 
 
.githooks
.githooks
 
 
.github
.github
 
 
.pi
.pi
 
 
.zed
.zed
 
 
assets
assets
 
 
docs/
next
docs/
next
 
 
nix
nix
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
vendor
vendor
 
 
website
website
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SKILL.md
SKILL.md
 
 
build.rs
build.rs
 
 
clippy.toml
clippy.toml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
justfile
justfile
 
 
View all files

## Repository files navigation

# herdr

herdr.dev·install·quick start·supported agents·integrations·configuration·socket api

v.0.4.0.mp4

agent multiplexer that lives in your terminal.

workspaces, tabs, panes. mouse-native: click, drag, split. every agent at a glance: blocked, working, done. detach and reattach, agents keep running. no gui app, no electron, no mac-only native wrapper. you see the agent's own terminal, not someone's interpretation of it.

## install

curl -fsSL https://herdr.dev/install.sh 
|
 sh

or install with homebrew:

brew install herdr

or download the binary fromreleases. requires linux or macos.

## quick start

Start Herdr in the directory where the work lives:

herdr

Herdr starts or attaches to one background session server. Pressctrl+b, thenshift+nto create a workspace. Run an agent in the root pane. Pressctrl+b, thenvorminusto split panes,ctrl+b, thencto create a tab, andctrl+b, thenwto switch workspaces.

Pressctrl+b qto detach the client. The server and pane processes keep running. Open another terminal and runherdragain to reattach.

## core concepts

Server and client.By default,herdrattaches to a background server. Detaching closes only the client.herdr server stopstops the default server and kills its panes. Named sessions are separate server namespaces: useherdr session attach work,herdr session stop work, andherdr session listwhen you want fully separate runtime state.

Workspaces, tabs, panes.A workspace is the project-level container. Tabs group panes inside a workspace. Panes are real terminal processes, not rewritten agent views.

Copy.Herdr copies pane text, not the sidebar. Drag-select inside a pane, double-click a word or token, or pressprefix+[for keyboard copy mode. In copy mode, move withh/j/k/l,w/b/e, and{/}, start selection withvor Space, copy withyor Enter, and leave withqor Esc. In PuTTY and some SSH terminals, holdShiftwhile dragging to use the terminal's own selection, andShift+ right click to paste.

Update and restore.herdr updateinstalls a new binary, but a running server keeps using the old process until it is stopped or handed off. Runherdr server stopfor the default session, orherdr session stop <name>for a named session, then start Herdr again.herdr update --handoffis experimental and tries to move live panes, including foreground processes such as dev servers, from the old server to the new one. If[session] resume_agents_on_restore = trueis enabled and current official integrations are installed, supported agent panes can restart from their native agent sessions after a server restart or update.

Keybindings.Herdr uses explicit keybinding strings.prefix+nmeans press the configured prefix, thenn.ctrl+alt+n,cmd+k,alt+1, and function-key chords are direct terminal-mode shortcuts and do not need the prefix. Plain direct printable keys such asnsteal normal typing, so useprefix+nunless you intentionally want a modifier-gated direct binding.

Agent awareness.The sidebar shows blocked, working, done, and idle states. Detection works with process names and terminal output by default. Official integrations make state reporting and native agent session restore more reliable, but Herdr still works as a terminal multiplexer without them.

## update

Herdr notifies you when a new version is available. Run manually:

herdr update

herdr updateis for installs managed by Herdr's own installer. Homebrew and Nix installs update throughbrew upgrade herdror your Nix workflow. Seeinstall docsandsession state docsfor the full update, restart, restore, and handoff matrix.

## how it compares

tmux

gui managers

herdr

persistent sessions

✓

—

✓

detach / reattach

✓

—

✓

panes, tabs, workspaces

✓

✓

✓

agent awareness

—

✓

✓

lives in your terminal

✓

—

✓

real terminal views

✓

—

✓

mouse-native

—

✓

✓

lightweight binary

✓

—

✓

agents can orchestrate

?

?

✓

tmux gives you persistence and panes, but it was built before agents existed. gui managers show agent state, but they make you leave your terminal and use their wrapped view. herdr is persistence and awareness in one tool that stays out of your way.

## remote and attach

Herdr works over normal SSH. Run it on the remote host, detach, and reattach later:

ssh you@yourserver
herdr

You can also attach from your local terminal without opening a shell first:

herdr --remote workbox
herdr --remote ssh://you@yourserver:2222

Direct attach connects your current terminal to one server-owned terminal:

herdr agent attach 
<
target
>

herdr terminal attach 
<
terminal_id
>

Seepersistence and remote docsfor remote keybinding, named-session, and handoff details.

## agent awareness

the sidebar shows which agents are blocked, working, or done. workspaces roll up to their most urgent state so you can scan the full list at a glance.

states:

* 🔴blocked— agent needs input or approval
* 🟡working— agent is actively running
* 🔵done— work finished, you have not looked at it yet
* 🟢idle— done and seen

detection works by reading foreground process and terminal output. zero config, no hooks required. for agents that expose hooks, the socket api integration gives more robust state reporting.

## lives in your terminal

not a gui window, not a web dashboard, not electron. herdr runs inside whatever terminal you already use. single rust binary, no dependencies. works inside tmux.

## what you get

* workspaces— organized around git repos or folder names, each with its own tabs and panes
* tabs— first-class in the socket api and cli
* copy-friendly— drag-select pane text, double-click tokens, or use keyboard copy mode withprefix+[,h/j/k/l,{/},v, andy
* notifications— sounds and toasts for background events; tab-aware suppression
* 18 built-in themes— catppuccin, terminal, tokyo night, gruvbox, one, solarized, kanagawa, rosé pine, vesper, and light variants for the main palettes
* session persistence— pane processes survive client detach; sessions restore panes after full restart, with opt-in recent screen history

## agents can use herdr too

The local Unix socket lets agents create workspaces, split panes, spawn helpers, read output, and wait for state changes. Start with thesocket API docsandSKILL.md.

## supported agents

automatic detection works out of the box. process name matching plus terminal output heuristics.

agent

idle / done

working

blocked

pi

✓

✓

partial

claude code

✓

✓

✓

codex

✓

✓

✓

droid

✓

✓

✓

amp

✓

✓

✓

opencode

✓

✓

✓

grok cli

✓

✓

✓

hermes agent

✓

✓

✓

cursor agent

✓

✓

✓

antigravity cli

✓

✓

✓

kimi code cli

✓

✓

✓

github copilot cli

✓

✓

✓

qodercli

✓

✓

✓

kiro cli

✓

✓

—

detected but not fully tested: gemini cli, cline.

for agents outside the built-in list, herdr still works as a terminal multiplexer with workspaces, panes, and tiling. custom integrations can report agent labels over the socket api. see thesocket api docs.

### direct integrations

the built-in pi, omp, claude code, codex, opencode, hermes, and qodercli integrations forward semantic state to herdr over the socket api. install with:

herdr integration install pi
herdr integration install omp
herdr integration install claude
herdr integration install codex
herdr integration install opencode
herdr integration install hermes
herdr integration install qodercli

see theintegrations docsfor setup details.

## keybindings

Pressctrl+bto enter prefix mode. Default actions are prefix-first and tmux-like:

key

action

prefix+c

new tab

prefix+n
 / 
prefix+p

next / previous tab

prefix+1..9

switch tab

prefix+w

workspace navigation

prefix+g

session navigator

prefix+shift+n

new workspace

prefix+shift+g

new worktree

prefix+shift+w

rename workspace

prefix+shift+d

close workspace

prefix+h/j/k/l

focus pane

prefix+v
 / 
prefix+minus

split pane

prefix+x

close pane

prefix+b

toggle sidebar

prefix+z

zoom pane

prefix+r

resize mode

prefix+q

detach

Mouse is supported throughout. Resize mode usesh/lfor width,j/kfor height, andescto exit. Full syntax, optional actions, indexed bindings, and custom command bindings live in theconfiguration docs.

## configuration

config file:~/.config/herdr/config.toml

herdr --default-config 
#
 print full default config

In-app settings cover theme, sound, and toast preferences. Herdr writes logs under~/.config/herdr/; in persistent session mode,herdr-client.logandherdr-server.logare usually the useful files. Full configuration and logging details live in theconfiguration docs.

## docs

* quick start— first session, panes, copy, and named sessions
* install— install, update, Homebrew, and Nix
* session state— detach, restart restore, agent restore, and live handoff
* configuration— keybindings, themes, notifications, environment variables
* integrations— pi, omp, claude code, codex, opencode, hermes, qodercli integrations
* SKILL.md— reusable agent skill
* socket api— socket protocol and cli reference

## agent instructions

if you are an ai agent helping with this repository, readAGENTS.mdbefore making changes and readCONTRIBUTING.mdbefore opening issues or PRs.

## development

git clone https://github.com/ogulcancelik/herdr

cd
 herdr
cargo build --release
./target/release/herdr

just 
test
 
#
 unit tests

just check 
#
 formatting, tests, and maintenance checks

## license

Herdr is dual-licensed:

1. Open source: GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later).
2. Commercial: commercial licenses are available for organizations that cannot comply with AGPL.

Contact:hey@herdr.dev

## mandatory star history

## About

agent multiplexer that lives in your terminal.

herdr.dev

### Topics

 agent

 rust

 tmux

 cli

 terminal

 ai

 devtools

 tui

 developer-tools

 multiplexer

 workspace-manager

 codex

 ai-agents

 terminal-ui

 terminal-multiplexer

 coding-agents

 agent-orchestration

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
 

### Stars

3.2k

 stars
 

### Watchers

6

 watching
 

### Forks

209

 forks
 

 Report repository

 

## Releases42

v0.6.5

 Latest

 

May 29, 2026

 

+ 41 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust90.5%
* CSS1.7%
* MDX1.6%
* Python1.6%
* HTML1.4%
* TypeScript1.2%
* Other2.0%