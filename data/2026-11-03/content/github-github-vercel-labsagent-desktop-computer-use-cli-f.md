---
title: 'GitHub - vercel-labs/agent-desktop: Computer use CLI for AI agents · GitHub'
url: https://github.com/vercel-labs/agent-desktop
site_name: github
content_file: github-github-vercel-labsagent-desktop-computer-use-cli-f
fetched_at: '2026-11-03T06:07:23.376419'
original_url: https://github.com/vercel-labs/agent-desktop
author: vercel-labs
description: Computer use CLI for AI agents. Contribute to vercel-labs/agent-desktop development by creating an account on GitHub.
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

317 Commits
317 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.githooks
.githooks
 
 
.github
.github
 
 
apps/
docs
apps/
docs
 
 
assets
assets
 
 
benchmarks/
locator-resolution
benchmarks/
locator-resolution
 
 
crates
crates
 
 
docs
docs
 
 
npm
npm
 
 
probes
probes
 
 
scripts
scripts
 
 
skills
skills
 
 
src
src
 
 
tests
tests
 
 
.claude
.claude
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitleaks.toml
.gitleaks.toml
 
 
.gitleaksignore
.gitleaksignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONCEPTS.md
CONCEPTS.md
 
 
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
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
clippy.toml
clippy.toml
 
 
deny.toml
deny.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
View all files

## Repository files navigation

# agent-desktop

Computer use for AI agents: read and operate desktop apps through the OS accessibility tree.

A CLI and C library for macOS, Windows and Linux. A snapshot returns JSON with a ref for every element an agent can act on. The agent acts on a ref and snapshots again to check, with no pixel matching; the loop stays in your agent.

On macOS, CLI calls reuse a private command host for each snapshot namespace and binary build. It retains native accessibility objects so a removed row cannot silently resolve to a surviving row with the same identifier. The host exits after 15 idle minutes.TMPDIRmust be owned by the current user with mode0700; the standard macOS per-user temporary directory satisfies this requirement. Headless calls still prohibit foreground activation and synthesized input.

Snapshots, clipboard reads, screenshots, command output and debug artifacts can contain private desktop content. Keep them out of public logs and uploads. The optionalJEV helpersends screen descriptions to a configured model provider; it is separate from the native CLI. Seeprivacy and data handling.

## Installation

Install on macOS, Windows or Linux with npm:

npm install -g agent-desktop
agent-desktop version

Bun, Yarn and pnpm can install the same package. It includes native binaries and platform helpers for x64 and ARM64.
For direct execution without a JavaScript launcher, download the matching native archive fromGitHub Releasesand keep its helper beside the executable.

Official Homebrew and Scoop packages are being submitted; they are not yet available in the default catalogs.
The repository no longer maintains a custom Homebrew tap or Scoop bucket.

* macOSneeds Accessibility permission:agent-desktop permissions --guide.
* Windowsneeds no grant for apps at your terminal's integrity level.
* Linuxneeds the user's graphical session withat-spi2-core.

Seeinstallation and permissionsfor package-manager behavior, release archives, and building from source.

## Quick start

Observe, act on a ref, observe again. Any app name fromagent-desktop list-appsworks; Finder is the macOS example.
Each command prints one JSON envelope; a trimmed snapshot follows the commands.

agent-desktop snapshot --app Finder -i 
#
 interactive elements, each with a ref

agent-desktop click @s8f3k2p9:e8 
#
 act on a ref from that snapshot

agent-desktop snapshot --app Finder -i 
#
 observe again to verify

{
 
"version"
: 
"
2.5
"
,
 
"ok"
: 
true
,
 
"command"
: 
"
snapshot
"
,
 
"data"
: {
 
"app"
: 
"
Finder
"
,
 
"window"
: { 
"id"
: 
"
w-204749
"
, 
"title"
: 
"
Downloads
"
 },
 
"snapshot_id"
: 
"
s8f3k2p9
"
,
 
"ref_count"
: 
59
,
 
"complete"
: 
true
,
 
"tree"
: {
 
"role"
: 
"
window
"
,
 
"name"
: 
"
Downloads
"
,
 
"children"
: [
 { 
"role"
: 
"
treeitem
"
, 
"name"
: 
"
Documents
"
, 
"ref_id"
: 
"
@s8f3k2p9:e8
"
, 
"available_actions"
: [
"
Click
"
] }
 ]
 }
 }
}

* Refs belong to their snapshot.A bare@e8is rejected withINVALID_ARGS. When the UI changes, an action
returnsSTALE_REForAMBIGUOUS_TARGET: take a new snapshot and use its refs.
* Several windowsgiveAMBIGUOUS_TARGET;snapshotlists the candidate window ids inerror.details. Pass one
with--window-id.
* Dense apps:map first withsnapshot --skeleton --app Slack -i --compact, then drill into one region withsnapshot --root @s8f3k2p9:e3 -i --compact.
* Headless by default.Ref actions go through the accessibility API without moving the pointer or taking focus.
The global--headedflag allows physical input.
* PowerShell.Quote every ref ('@s8f3k2p9:e8'), because a bare@tokenis the splatting operator.

## For AI agents

The binary carries its own docs, matched to its version:

agent-desktop skills get desktop 
#
 the loop, refs, verification and retry rules

agent-desktop skills get platform 
#
 what differs on the OS you run on

agent-desktop 
<
command
>
 --help 
#
 flags for one command

Install the skill into an agent harness fromskills.sh:

npx skills add https://github.com/vercel-labs/agent-desktop --skill agent-desktop

Or add this to yourAGENTS.md:

Use 
`
agent-desktop
`
 to see and operate desktop apps. Before the first use, run

`
agent-desktop skills get desktop
`
 and 
`
agent-desktop skills get platform
`
, and follow them.

Every command prints one envelope withokand eitherdataorerror. An error carries acode, adispositionand usually asuggestion; retry only whenerror.disposition.retryissafe. The contract, error codes and exit codes are indocs/json-output.md.

## Commands

It ships 60 command names, 56 operational commands. The other four (key-down,key-up,mouse-down,mouse-up) refuse to run until a daemon can release a held key or button.

Group

Commands

Observe

snapshot
, 
find
, 
get
, 
is
, 
screenshot
, 
list-surfaces

Act on a ref

click
, 
double-click
, 
triple-click
, 
right-click
, 
type
, 
set-value
, 
clear
, 
focus
, 
select
, 
toggle
, 
check
, 
uncheck
, 
expand
, 
collapse
, 
scroll
, 
scroll-to

Keyboard and mouse

press
, 
hover
, 
drag
, 
mouse-move
, 
mouse-click
, 
mouse-wheel
, 
key-down
, 
key-up
, 
mouse-down
, 
mouse-up

Apps and windows

launch
, 
close-app
, 
list-apps
, 
list-windows
, 
list-displays
, 
focus-window
, 
resize-window
, 
move-window
, 
minimize
, 
maximize
, 
restore
, 
open-system-surface

Notifications

list-notifications
, 
dismiss-notification
, 
dismiss-all-notifications
, 
notification-action

Clipboard

clipboard-get
, 
clipboard-set
, 
clipboard-clear

Wait

wait

Sessions

session
, 
trace
, 
cursor-overlay

System

status
, 
permissions
, 
version
, 
batch
, 
skills

## Platform support

macOS

Windows

Linux

Accessibility tree

Yes

Yes

Yes (AT-SPI)

Click / type / keyboard

Yes

Yes

AT-SPI; X11 / GNOME keys

Mouse input

Yes

Yes

X11, 
--headed

Screenshot

Yes

Yes

X11 windows; Wayland portal

Clipboard

Yes

Yes

Yes; Wayland needs 
wl-clipboard

App & window management

Yes

Yes

Launch/list; X11 window control

Notifications

Yes

Yes

GNOME Shell

Shell surfaces (
open-system-surface
)

Planned

Yes

GNOME tray, Action Center

The Windows surface andlaunchnotes and the Linux X11 and Wayland notes are indocs/install.md.

agent-desktop skills get platformprints the full capability table for the OS you run on.

## Language bindings

Each release also shipslibagent_desktop_ffifor macOS, Linux and Windows, so a program can call the tool in process instead of starting the CLI for each command.agent-desktop skills get fficovers the entry points, memory ownership and threading rules.

import
 
ctypes

lib
 
=
 
ctypes
.
CDLL
(
"./lib/libagent_desktop_ffi.dylib"
)

lib
.
ad_adapter_create
.
restype
 
=
 
ctypes
.
c_void_p

lib
.
ad_adapter_destroy
.
argtypes
 
=
 [
ctypes
.
c_void_p
]

assert
 
lib
.
ad_init
(
6
) 
==
 
0
 
# AD_RESULT_OK when the header's AD_ABI_VERSION_MAJOR matches the library

adapter
 
=
 
lib
.
ad_adapter_create
()

lib
.
ad_adapter_destroy
(
adapter
)

## Development

Each platform adapter builds only on its own OS, so scope cargo to the host's packages. On macOS:

HOST_PKGS=(-p agent-desktop-core -p agent-desktop-macos -p agent-desktop -p agent-desktop-ffi)
cargo 
test
 
"
${HOST_PKGS[@]}
"

cargo clippy 
"
${HOST_PKGS[@]}
"
 --all-targets -- -D warnings

On Windows, replaceagent-desktop-macosin that list withagent-desktop-windows; on Linux, withagent-desktop-linux.CONTRIBUTING.mdlists every gate. Build from source:docs/install.md.

## Documentation

I want to...

Read

Fix an install problem, grant permissions, verify a download or build from source

docs/install.md

Parse the JSON envelope, error codes and exit codes

docs/json-output.md

Drive the tool as an AI agent

agent-desktop skills get desktop
 (
skills/agent-desktop/
)

Learn what differs on one OS

macOS
, 
Windows
, 
Linux

Call the C library

skills/agent-desktop-ffi/

Look up the vocabulary: refs, snapshots, sessions

CONCEPTS.md

Contribute and pass the gates

CONTRIBUTING.md

Read the engineering rules

AGENTS.md

Learn from past bugs and lessons

docs/solutions/

Find answers to common questions

docs/faq.md

Report a vulnerability

SECURITY.md

Get help

SUPPORT.md

## License

Apache-2.0