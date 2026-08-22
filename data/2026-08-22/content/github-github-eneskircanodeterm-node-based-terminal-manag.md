---
title: 'GitHub - eneskirca/nodeterm: Node-based terminal manager for AI coding agents — tmux-backed terminals and parallel agent sessions as draggable nodes on an infinite pan/zoom canvas. macOS, Linux, and a browser Server Edition. · GitHub'
url: https://github.com/eneskirca/nodeterm
site_name: github
content_file: github-github-eneskircanodeterm-node-based-terminal-manag
fetched_at: '2026-08-22T19:21:15.408762'
original_url: https://github.com/eneskirca/nodeterm
author: eneskirca
description: Node-based terminal manager for AI coding agents — tmux-backed terminals and parallel agent sessions as draggable nodes on an infinite pan/zoom canvas. macOS, Linux, and a browser Server Edition. - eneskirca/nodeterm
---

eneskirca

 

/

nodeterm

Public

* NotificationsYou must be signed in to change notification settings
* Fork112
* Star1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,669 Commits
2,669 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
.superpowers/
sdd/
node-identity
.superpowers/
sdd/
node-identity
 
 
build
build
 
 
docs
docs
 
 
resources
resources
 
 
scripts
scripts
 
 
site
site
 
 
src
src
 
 
test
test
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
THIRD-PARTY-NOTICES.md
THIRD-PARTY-NOTICES.md
 
 
bootstrap-windows.bat
bootstrap-windows.bat
 
 
electron.vite.config.ts
electron.vite.config.ts
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
stale-frame.png
stale-frame.png
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.node.json
tsconfig.node.json
 
 
tsconfig.web.json
tsconfig.web.json
 
 
vitest.config.ts
vitest.config.ts
 
 
wt-dialog.png
wt-dialog.png
 
 
View all files

## Repository files navigation

# nodeterm

A node-based terminal manager — your terminals and agents on an infinite canvas.

Multiple real terminals live as draggable nodes on a single pan/zoom canvas, and every
project doubles as aTrello-style board of live Claude Code sessions. Built for
people with ADHD and scattered workflows: a spatial layout instead of a stack of
hidden tabs.

Download·Docs·Features·Build from source·Architecture·License

▶ 
Watch the 30-second tour with sound

## Why nodeterm

Stacked terminal tabs hide context — you lose track of what's running where. nodeterm
turns that into amap: every shell is a node you can place, group, label, and zoom
into. Sessions are spatial and persistent, so your mental model stays intact across
restarts. And because the app is built around a clean service seam, the same canvas runs
three ways — as thedesktop app for macOS and Linux, as aself-hosted browser appyou reach from anywhere (Server Edition), and aniOS companionthat attaches to the
same live sessions.

📚Full documentation lives atnodeterm.dev/docs— get
started, concepts, agents, remote access, troubleshooting.

## ✨ Features

### Everything is a node

Right-click the canvas to open aterminal— or an AIagent. Each runs in its own
persistent tmux session, next tosticky notes(link one to feed an agent context),Monaco editors,diff views, andweb/videonodes — arranged spatially, like a
map. Quit the app, evenrestart the machine— every session comes back.

### Know when an agent needs you

Hook-driven status — no output scraping: pulsingRUNNING / NEEDS YOUbadges,subagentcards with live transcripts, a per-nodecontext meter, and OS
notifications. Click the ping, answer the permission prompt right in the node, and get
told the moment the turn isdone. On a MacBook, agents live in thenotchtoo.

### One project, two views

Every project is a canvas —and also a kanban board. Cardsareyour live
sessions: drag them across columns while the agent keeps running, open a card into alive card modal(the real session + members, due date, priority, comments), and
assign teammates. Toggle with⌘⇧B.▶Watch the board video with sound

### Your sessions, anywhere

Pair your phonewith one QR —scan with the nodeterm iOS app— and thesame
live session continues in your pocket, E2E encryptedover the relay, not just your
LAN. The same canvas also runs self-hosted in any browser (Server Edition).

### Talk to your terminal

Hold⌘⌥and say it. On-deviceWhispertranscribes locally — review the text,
thenSend(nothing auto-submits). Your voice never leaves the machine.

### Node kinds

🖥Terminal(xterm + tmux, AI naming) · 🤖Agent(Claude Code / Codex / Gemini /
GitHub Copilot / opencode / Grok / custom) · 📝Sticky note(link to an agent as context) · 🗂Group(bind to agit worktreefor agent-per-branch) · ✏️Editor(Monaco, ⌘S) ·
🔀Diff· 🌐Web / Video

### More

* Session continuity (tmux)— terminals keep running across node remountsandfull
app restarts, including live processes; machine reboots restore scrollback and resume
agent sessions (claude --resume). The macOS appships its own tmux, so this works
with nothing installed; a tmux already on your system is always used in preference to it,
and terminals opened before an upgrade stay as they were until you refresh the node.
* Talk to your terminal— on-device Whisper dictation (hold ⌘⌥): speak, review, send.
* Agent superpowers—context linksso agent nodes read each other's transcripts
on demand; Claude-onlybranch a conversationandmanaged accountsfor several
logged-in Claude identities side by side; agents can drive the canvas (open nodes,
spawn teams, verify each other's work) via the built-in canvas-control CLI.
* Remote / SSH projects— open a project on a remote host over SSH; terminals, files,
git, and even the board run there while the canvas stays local.
* Source control— VS Code-style stage/unstage, discard, branch switch/create,
commit, push/sync/publish,worktrees, andghsign-in — backed by systemgit.
* GitHub Issues on Kanban– opt-in issue cards, exact label-to-column mapping,
All / GitHub / Sessions filtering, and two-way move, close, and reopen sync. Seesetup and security details.
* AI commit messages & terminal names— bring-your-own local agent CLI run read-only
on the staged diff or captured output.
* Your sessions, in your pocket—nodeterm mobile(iOS) attaches to the same live
tmux sessions: watch an agent work, answer a "needs you", or type into any terminal
from your phone — plus push notifications and a mobile board view.
* Power & sleep— while an agent is working, nodeterm keeps the machine from
idle-sleeping, and lets go the moment it finishes (on by default; toggle in the setup
tour or Settings → Behavior). No app can hold a machine awake through a closed lid —
for overnight runs keep the laptop open and plugged in, or run the agents on a box
that doesn't sleep via theServer Edition.
* Command palette(⌘K),file explorer(⌘⇧E),markdown view(⌘M),undo/redo, and a native macOS dark UI.
* Auto-update & in-app announcements— the app checks a self-hosted feed and
surfaces a "Restart to update" banner and product news.

### 🌍 Server Edition — nodeterm in your browser

The same canvas runs headless on a Linux (or macOS) host and is used from any browser —
so your terminals, editors, source control, board, and agents live on a server you reach
from anywhere. Single-user auth (password + secure cookie), a WebSocket bridge, and the
exact same renderer as the desktop app.

npm run server:dev 
#
 build + serve; open http://127.0.0.1:8443 and set a password

Terminals, files/editor/diff, the full git panel, the kanban board, and agent-status
badges all work in the browser today. Seedocs/SERVER.mdfor the
quickstart, security model, and current limitations.

#### 🔔 Get push notifications from any SSH host

The same server also runsheadlessas a background notification host: install it on any
Linux box you SSH into, and your phone getsRUNNING / NEEDS YOUpush + Live-Activity
coverage for the agents running there — withzero open ports(the hook server stays
loopback-only and push goes out over HTTPS under a grant your phone drops over SSH).

curl -fsSL https://raw.githubusercontent.com/eneskirca/nodeterm/main/scripts/install-server.sh 
|
 bash

One line installs, builds, and runs it as a systemd service (NODETERM_HEADLESS=1); re-run it
to update. See theheadless notification hostsection for details.

## 📦 Download

Grab the latest build fromnodeterm.dev— the download button
detects your platform. Everything is also listed atnodeterm.dev/releases:

* macOS—.dmgfor Apple Silicon and Intel (auto-updates), orHomebrew:brew tap nodeterm/tap
brew trust nodeterm/tap#Homebrew ≥6 refuses to load an untrusted tapbrew install --cask nodetermBoth first lines are required. On its own,brew install --cask nodetermonly searcheshomebrew/caskand reports the cask as not found; without the trust grant, Homebrew ≥6
fails rather than prompting. The cask tracks each promoted release, and the app updates
itself (electron-updater), sobrew upgradeis rarely needed for it.
* Linux (x64)— self-updatingAppImage, or a.debfor Debian/Ubuntu
(sudo apt install ./nodeterm-*.deb; updates are manual for.deb).
* iOS—nodeterm mobileon theApp Store.

## 🛠 Build from source

Requires Node.js 20+ on macOS or Linux (tmux recommended — it's what makes sessions
survive restarts). A source checkout doesnotcarry the bundled tmux: runnode scripts/build-tmux.mjsonce on macOS to build it intoresources/bin/tmux(the
release job does this automatically), or just install tmux yourself.

npm install 
#
 deps + rebuilds node-pty against Electron's ABI (postinstall)

npm run dev 
#
 dev mode with renderer HMR

npm run build 
#
 production build into out/

npm start 
#
 preview the production build

npm run typecheck 
#
 fastest correctness gate

npm 
test
 
#
 vitest unit + integration suite

npm run dist 
#
 local UNSIGNED .dmg into dist/ (smoke test)

npm run dist:linux 
#
 AppImage + .deb into dist/ (on a Linux host)

npm run server:dev 
#
 build + run the browser Server Edition (needs Node 22 + tmux)

## ⌨️ Keyboard shortcuts

These are the defaults — every one of them is remappable inSettings → Keyboard Shortcuts.

Shortcut

Action

⌘K

Command palette

⌘T
 / 
⌘⇧C

New terminal / New Claude Code

⌘⇧B

Toggle the kanban board

⌘W

Close the selected node

⌘Z
 / 
⌘⇧Z

Undo / Redo

⌘M

Toggle markdown view (terminal / editor)

Hold 
⌘⌥
 (
Ctrl+Alt
)

Dictate into the focused terminal

⌘⇧E

File explorer

⌘,

Settings · 
⌘/
 Shortcuts

Right-click

Actions menu (empty space or node)

## 🏗 Architecture

* Electron, three contexts—src/main(the Electron shell),src/preload(the only
bridge,window.nodeTerminal),src/renderer(React UI).src/sharedholds the types
and IPC channel names used by all three.
* CorePlatformseam— every service (PTY, workspace/settings, git, agents, hooks) lives
insrc/corebehind a small platform interface and never importselectron. Electron is
one implementation of that seam; the browser Server Edition (src/server) is another,
booting the exact same services over a WebSocket-RPC bridge (src/renderer/bridgefillswindow.nodeTerminalin the browser). One codebase, one renderer, multiple shells.
* TerminalTransportabstraction— the renderer depends only on this interface, never on
IPC or node-pty directly.LocalTransporttalks to the local host;RemoteTransporttalks
to a remote agent over SSH — so remote projects drop in without touching the canvas UI.
* React Flow is the single source of truthfor live nodes; projects persist serialized
nodes to disk, and tmux keeps sessions alive across restarts.
* Three surfaces— the desktop app, the browserServer Edition, and themobile companion(a separate SwiftUI repo) all ride the same core + transport seams.

Seedocs/SERVER.mdfor the Server Edition, and the design docs
underdocs/for deeper notes.

## 🤝 Contributing

Issues and pull requests are welcome.Start withCONTRIBUTING.md—
setup, the process-boundary rules, and the house rules that come up in review.CLAUDE.mdis the deep reference behind them (and is loaded automatically if
you work with an AI coding agent). Questions or bug reports are also happy atnodeterm.dev/support/support@nodeterm.dev. nodeterm is licensed under theBusiness Source License 1.1— you can use, modify,
and redistribute it freely, including in production, except offering it as a
competing product or service (seeLicense).

By submitting a contribution (pull request, patch, or code snippet), you agree
that it is licensed under the sameBUSL-1.1terms as the rest of
the project, and that the project may continue to relicense future versions
(including your contribution) as part of its normal licensing model.

## 📜 License

BUSL-1.1(Business Source License): you may
copy, modify, redistribute, and — under the Additional Use Grant — makeproduction
useof nodeterm; the one thing you may not do is offer it (hosted, embedded, or as a
standalone product/service) in a way thatcompeteswith nodeterm or with the
Licensor's products built on it. Each release automatically becomes plainMITfour
years after it is published. SeeLICENSEfor the full terms andTHIRD-PARTY-NOTICES.mdfor the bundled open-source
components. For a commercial license beyond the grant, contacteneskirca@gmail.com.

"Claude" and "Claude Code" are trademarks of Anthropic, and "Trello" is a trademark of
Atlassian; nodeterm is not affiliated with or endorsed by either.