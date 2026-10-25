---
title: 'GitHub - JetBrains/thinkrail: Vibe code with pi in a lightweight, real IDE that customises itself around the way you work — The Vibe You Need · GitHub'
url: https://github.com/JetBrains/thinkrail
site_name: github
content_file: github-github-jetbrainsthinkrail-vibe-code-with-pi-in-a-l
fetched_at: '2026-10-25T14:48:48.017121'
original_url: https://github.com/JetBrains/thinkrail
author: JetBrains
description: Vibe code with pi in a lightweight, real IDE that customises itself around the way you work — The Vibe You Need - JetBrains/thinkrail
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

554 Commits
554 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.changeset
.changeset
 
 
.github
.github
 
 
.husky
.husky
 
 
.pi/
prompts
.pi/
prompts
 
 
apps
apps
 
 
e2e
e2e
 
 
packages
packages
 
 
patches
patches
 
 
pi-extensions
pi-extensions
 
 
scripts
scripts
 
 
thinkrail-extensions
thinkrail-extensions
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
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
 
 
architecture.md
architecture.md
 
 
biome.json
biome.json
 
 
bun.lock
bun.lock
 
 
central-integration.md
central-integration.md
 
 
goal-and-requirements.md
goal-and-requirements.md
 
 
install.ps1
install.ps1
 
 
install.sh
install.sh
 
 
package.json
package.json
 
 
pi-compatibility.md
pi-compatibility.md
 
 
playwright.binary.config.ts
playwright.binary.config.ts
 
 
playwright.config.ts
playwright.config.ts
 
 
playwright.desktop.config.ts
playwright.desktop.config.ts
 
 
playwright.perf.config.ts
playwright.perf.config.ts
 
 
playwright.workflows.config.ts
playwright.workflows.config.ts
 
 
tsconfig.base.json
tsconfig.base.json
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

# ThinkRail

ThinkRail is the agentic IDE that gets better every time you use it — learning your project through
living specs today, and building its own capabilities tomorrow.

We built a rich interface around thepicoding agent, isolated work into separate workspaces, and gave the agent durable project knowledge
through living specs and reusable skills. Next, we're adding full extension support, so ThinkRail can
create the tools it needs based on how you actually work.

Website:thinkrail.ai·Blog:thinkrail.ai/blog

⭐ If you find ThinkRail useful, give it a star — it helps others discover it.

Apisession and the change it made, scoped to an isolated git-worktree workspace.

## What you get

* Isolated workspaces.Open any git repo as a project and cut workspaces from it asgit worktrees,
each with its own branch and working directory. Agents work in parallel without touching your
checkout; merge the good branch, delete the rest. You can also attach existing worktrees or explicitly
work in the project folder itself. Finished and dormant workspaces settle onto a per-project shelf on
their own — when their pull request merges or closes, or after a quiet week — and come back the moment
you work in them. The topbar shows where the active branch stands againstoriginand its pull request,
with the next step one click away: publish, push, or open a PR described from the plan, the commits,
your PR template, or an agent-written draft. Once a GitHub PR is open it shows the CI checks and review
decision, and lets you mark it ready, hand failing checks or a diverged branch to the agent, merge it
with the repository's last-used method, reopen it, or delete the remote branch.
* A real IDE around the agent.A splittable workbench of Monaco editor tabs, a Files tree with live git
change marks and a Changed view, terminals, and documents — all scoped to the active workspace. Leave
anchored review comments on files and diffs and send them to a chat as structured context, or open the
worktree in your installed IDE.
* Chats that stream like the engine thinks.Several concurrentpisessions per workspace, each with
its own model and live token and cost readout. Steer a running turn or queue a follow-up, delegate to
subagents, and work a shared plan the agent updates and you edit — each completed step can be committed
and reviewed on its own.
* Specs as ground truth.A connected graph ofSPEC.mdfiles lives beside the code; the agent reads,
searches, and maintains it through dedicatedspec_*tools, so intent survives the session. The
read-only Specs tool renders the graph as a tree in the workbench.
* Skills and workflows.Portable Agent Skills you already keep for other coding agents are read in
place, and bundled workflows guide project setup, design brainstorming, and shipping a pull request —
pushing the workspace branch and opening or updating its GitHub PR through your owngh.
* Agent tools beyond the shell.Web research, and inline diagrams, option comparisons and file previews
rendered right in the chat — when the agent proposes a UI change it shows a before/after mockup you can
comment on like a diff. Settings → Extensions lists the ThinkRail extensions the agent gets and lets you switch
each one off.
* MCP servers.Connect the MCP servers in yourpimcp.json(or add them, and a few presets, from
Settings): ThinkRail asks in the chat before calls the server does not mark read-only (or always allows
the tools you trust in a project), keeps servers a repository
defines off until you approve them, signs you in to OAuth servers from Settings, and shows each chat's
servers next to its background commands and subagents.
* Your providers, your credentials.Sign in withJetBrains AIor
connect any provider throughpi's own auth. ThinkRail has no accounts of its own.
* Desktop app or browser.A native desktop app, or thethinkrailCLI that opens the same app in your
browser. Both embed the same engine host; app state lives under~/.thinkrail.
* Your language.Settings → Language follows your system language or a language you pick; English and
Simplified Chinese are built in. Add a language ThinkRail doesn't ship yet by dropping a translateden.jsoninto~/.thinkrail/locales— it applies as you save. Agent replies and tool output stay as
the agent wrote them.

The project's spec graph as a tree, with the spec itself rendered alongside.

## Install

ThinkRail ships in two additive forms: a native desktop installer and the self-containedthinkrailCLI.
Both are published withSHA256SUMSon thereleases page.

### Desktop

Download thethinkrail-desktop-*asset for your platform:

* macOS (Apple Silicon)— open the DMG. There is no Intel desktop build.
* Windows x64— extract the complete setup ZIP, then run its setup executable in place, next to its
payload.
* Linux x64 / ARM64— extract the setup tarball and runinstaller. Desktop builds need glibc 2.38+
with GTK 3, WebKitGTK 4.1, Ayatana AppIndicator 3, and librsvg 2 — Ubuntu 24.04 or newer:sudo apt install libgtk-3-0 libwebkit2gtk-4.1-0 libayatana-appindicator3-1 librsvg2-2

Packaged stable and nightly desktop builds check for updates in the background and offer them inSettings → Updates:Download→Preparing update→Install & Restart. Nothing is applied until
you chooseInstall & Restart. ThinkRail then shows the installation's progress and log, closes, and
reopens on the new version. After the restart it tells you whether the update installed. If it didn't, it
explains why and offers to retry. The updater appears only when the package carries a valid HTTPS feed
identity; installations that predate that identity need one manual installation first.

### Command line

The installer downloads the right binary, verifies its SHA-256 checksum, and putsthinkrailon your PATH.

macOS / Linux(also Windows under Git Bash):

curl -fsSL https://raw.githubusercontent.com/JetBrains/thinkrail/main/install.sh 
|
 bash

Windows— the same command works from cmd and PowerShell:

powershell 
-
c 
"
irm https://raw.githubusercontent.com/JetBrains/thinkrail/main/install.ps1 | iex
"

Then runthinkrail, optionally with a git repo to open as a project:

thinkrail 
~
/code/my-repo

thinkrailneedsgiton your PATH and a model provider — sign in with JetBrains AI from the app or use
your own provider credentials.thinkrail --helplists the flags;thinkrail --versionprints the build.

Nightly builds, pinned versions, updates, and uninstall

The installer takes--channel stable|nightlyand--version; a pinned version must belong to the
selected channel:

curl -fsSL https://raw.githubusercontent.com/JetBrains/thinkrail/main/install.sh 
|
 bash -s -- --channel nightly
curl -fsSL https://raw.githubusercontent.com/JetBrains/thinkrail/main/install.sh 
|
 bash -s -- --channel stable --version 0.1.2
curl -fsSL https://raw.githubusercontent.com/JetBrains/thinkrail/main/install.sh 
|
 bash -s -- --channel nightly --version 0.2.0-nightly.10

On Windows the options are environment variables (THINKRAIL_CHANNEL,THINKRAIL_VERSION,THINKRAIL_PREFIX,THINKRAIL_NO_MODIFY_PATH):

$
env:
THINKRAIL_CHANNEL
=
'
nightly
'
; irm https:
//
raw.githubusercontent.com
/
JetBrains
/
thinkrail
/
main
/
install.ps1 
|
 iex 
#
 PowerShell

set 
"
THINKRAIL_CHANNEL=stable
"
 && set 
"
THINKRAIL_VERSION=0.1.2
"
 && powershell 
-
c 
"
irm https://raw.githubusercontent.com/JetBrains/thinkrail/main/install.ps1 | iex
"
 
#
 cmd

Installed stable and nightly CLI hosts periodically offerRun UpdateinSettings → Updates. It runs
the host machine'sthinkrail updatein the background — also when the UI is open in a browser on another
machine — and a successful update asks you to restart the host manually. You can runthinkrail updatedirectly on any platform: it re-runs the installer for the installed channel and replaces<prefix>/bin/thinkrail[.exe]; pass--channelor--versiononly for an explicit override.

thinkrail uninstallremoves the executable, the PATH entry the installer added, and the install metadata,
and asks whether to delete your~/.thinkrailapp state (kept by default —--remove-datadeletes it,-yskips the questions).

Prefer a manual install? Download a binary andSHA256SUMSfrom the releases page and verify the checksum.
For self-update to work, rename it tothinkrail(thinkrail.exeon Windows) and place it at<prefix>/bin/thinkrail[.exe]; a binary kept under its release filename or elsewhere must be replaced
manually or reinstalled with the script.

### Platform notes

Platform

Desktop

CLI

macOS Apple Silicon

DMG

signed binary

macOS Intel

no Electrobun build

not prebuilt — 
build from source

Windows x64

signed setup executable and app binaries

signed 
.exe

Linux x64 / ARM64

setup tarball, unsigned

unsigned

JetBrains signs the Windows CLI, the desktop setup executable, and every executable and DLL the desktop app
installs. The macOS CLI is signed but not yet notarized.
Signed and notarized desktop DMGs require the coordinated JetBrains service pipeline; older published DMGs
and locally built packages may still be unsigned and blocked by Gatekeeper. Linux artifacts are unsigned.

## Analytics & privacy

ThinkRail collects basic usage events — launches, chat creation, message sends, provider connections — tied to
a random installation ID. Usage analytics never include prompts, code, files, credentials, or account
identity. Error reports are also always sent, tied to the same installation ID, so we can fix crashes: the
error type and code and where in ThinkRail's own code it happened. They never include error messages, file
paths, names, URLs, or anything from your projects or extensions. Additional product
usage and how you found ThinkRail are shared only whileShare additional usage
datais on; the switch is offered at first launch and lives inSettings → Privacy. When launching from
the command line,thinkrail --no-analytics(orTHINKRAIL_NO_ANALYTICS=1) turns additional sharing off for
that run. With additional sharing on, a packaged build may open the ThinkRail blog in your browser once to
link your installation to the website visit that brought you here — only where you accepted marketing cookies on the
website or no consent is required — and that link expires after 30 days.

## Under the hood

ThinkRail is a thin host that runspiin-process and bridges it to a rich web UI.piowns models,
skills, compaction, cost, and session state; the app owns the workspace, the editor, and the wire — it
never assembles prompts behind your back. Three rings:

* Engine host—packages/server(+packages/shared): aBun.serveHTTP+WS host with one in-processpisession per chat, launched byapps/cliorapps/desktop.
* The wire—packages/contracts: the typed, versioned protocol between host and UI.
* UI client—apps/web: React 19 + Zustand + Tailwind v4, shipped independently; it dials a host over
the wire and depends on the contracts only.

goal-and-requirements.mdandarchitecture.mdare the
canonical product and design specs. ThinkRail is developed spec-first: aSPEC.mdsits beside every
module, and a change that moves a boundary, contract, or decision updates the spec in the same change.

## Developing ThinkRail

You needBun1.4.4 (the pinned package manager and runtime),Node.js≥ 22.19 (required by the
in-processpiengine), and an authenticatedpiprovider for agent work.

git clone https://github.com/JetBrains/thinkrail.git

cd
 thinkrail
bun install
bun run dev 
#
 host + web client together; Ctrl+C stops both

bun run --filter @thinkrail/cli dev 
#
 browser launcher

bun run build:binary 
#
 standalone CLI artifact

bun run desktop:dev 
#
 package and open the Electrobun app

bun run desktop:build 
#
 package without opening it

CONTRIBUTING.mdcovers the checks, the end-to-end suites, desktop packaging, and the
repository layout.

## Contributing

Contributions are welcome — seeCONTRIBUTING.md. This project and community are
governed by theCode of Conduct.

## License

Licensed under theApache License 2.0.