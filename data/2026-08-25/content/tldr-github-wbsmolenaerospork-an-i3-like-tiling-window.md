---
title: 'GitHub - wbsmolen/aerospork: An i3-like tiling window manager for macOS — tree layout, instant virtual workspaces, TOML config, and a settings GUI. Fork of AeroSpace. · GitHub'
url: https://github.com/wbsmolen/aerospork
site_name: tldr
content_file: tldr-github-wbsmolenaerospork-an-i3-like-tiling-window
fetched_at: '2026-08-25T06:00:29.148084'
original_url: https://github.com/wbsmolen/aerospork
date: '2026-08-25'
description: An i3-like tiling window manager for macOS — tree layout, instant virtual workspaces, TOML config, and a settings GUI. Fork of AeroSpace. - wbsmolen/aerospork
tags:
- tldr
---

wbsmolen

 

/

aerospork

Public

* NotificationsYou must be signed in to change notification settings
* Fork1
* Star20

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

67 Commits
67 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.bundle
.bundle
 
 
.claude/
skills/
aerospork-design
.claude/
skills/
aerospork-design
 
 
.github
.github
 
 
Sources
Sources
 
 
axDumps
axDumps
 
 
dev-docs
dev-docs
 
 
docs
docs
 
 
grammar
grammar
 
 
legal
legal
 
 
resources
resources
 
 
script
script
 
 
shell-completion
shell-completion
 
 
updates-site
updates-site
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.ruby-version
.ruby-version
 
 
.swift-version
.swift-version
 
 
.swiftformat
.swiftformat
 
 
.swiftlint.yml
.swiftlint.yml
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Gemfile
Gemfile
 
 
Gemfile.lock
Gemfile.lock
 
 
LICENSE.txt
LICENSE.txt
 
 
Package.resolved
Package.resolved
 
 
Package.swift
Package.swift
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
build-debug-app.sh
build-debug-app.sh
 
 
build-debug.sh
build-debug.sh
 
 
build-docs.sh
build-docs.sh
 
 
build-release.sh
build-release.sh
 
 
build-shell-completion.sh
build-shell-completion.sh
 
 
format.sh
format.sh
 
 
generate-app-icon.py
generate-app-icon.py
 
 
generate.sh
generate.sh
 
 
install-from-sources.sh
install-from-sources.sh
 
 
launch-debug-app.sh
launch-debug-app.sh
 
 
makefile
makefile
 
 
project.yml
project.yml
 
 
run-cli.sh
run-cli.sh
 
 
run-debug.sh
run-debug.sh
 
 
run-swift-test.sh
run-swift-test.sh
 
 
run-tests.sh
run-tests.sh
 
 
View all files

## Repository files navigation

AeroSpork is an i3-style tiling window manager for macOS. Windows are leaves of a layout tree,
workspaces are emulated rather than mapped onto native Spaces, and nothing requires disabling System
Integrity Protection. It is configured in TOML, driven from a CLI, and ships a settings GUI.

It is a fork ofAeroSpaceby Nikita Bobko, which is
where the tree model, the workspace emulation and most of the command surface come from. Both are
MIT licensed; seelegal/.

## Why I forked it

I ran AeroSpace daily on four monitors behind a DisplayLink dock, and three things wore me down. It
felt sluggish. Long sessions drifted, so state that was correct at login was not correct by the
evening. And the DisplayLink panels were a coin flip: workspaces came back on the wrong screens
after every undock, because monitors are matched by name, regex or index, and none of those survive
a redock. Two identical displays are indistinguishable to a name match.

I sent the monitor work upstream asPR #1526in July 2025. It was closed the next
day without review. That is the maintainer's call on their own project, and upstream is clear that
it keeps a deliberately small surface, so I kept the work here instead.

What that turned into, in this codebase:

* The DisplayLink problemismodel/MonitorFingerprint.swift. A display is matched on the
per-display UUID first, then EDID vendor/model/serial from CoreGraphics, then name, then size.
DisplayLink panels report no EDID at all, so the UUID is the only key that separates two of them.
Screen reconfiguration is also debounced, because a dock connects in several stages and fires the
change notification more than once.
* The sluggishnessis two changes rather than a rewrite. Bursts of accessibility events coalesce
into one layout pass on a 50ms debounce (util/RefreshDebouncer.swift), andMacApp.setFrameskips the AX write when a window already sits at its target frame, which matters over a
DisplayLink link where every write repaints a framebuffer. I have not published speedup numbers;dev-docs/performance.mdsays which measurements exist and why the benchmark could not settle
the rest.
* The driftis mostly workspace lifecycle. Workspaces are created on demand and released when
they empty, instead of being materialized for every name a keybinding mentions.

## Tech stack

Concern

Implementation

Language

Swift, 6.0 language mode (
Package.swift
); 
.swift-version
 pins toolchain 6.4

Minimum OS

macOS 13.0 (Ventura)

UI

SwiftUI/AppKit: a 
MenuBarExtra
 and a native pane-toolbar 
Settings
 scene

Third-party dependencies

TOMLKit (config parsing) and Sparkle (in-app updates)

CLI/app IPC

POSIX 
AF_UNIX
 stream socket, length-prefixed framing (
Sources/Common/util/UnixSocket.swift
)

Global hotkeys

Carbon 
RegisterEventHotKey
 (
config/HotkeyBinding.swift
)

Volume control

CoreAudio (
util/SystemVolume.swift
)

Display identity

CoreGraphics 
CGDisplayCreateUUIDFromDisplayID
, 
CGDisplayVendorNumber
, 
CGDisplayModelNumber
, 
CGDisplaySerialNumber

Window IDs

C shim over the private 
_AXUIElementGetWindow
 (
Sources/PrivateApi/
)

Build

SwiftPM for the CLI and debug builds; XcodeGen plus 
xcodebuild
 for the 
.app
, since SwiftPM cannot produce a bundle

### Why these choices

If you are weighing this against upstream, the reasoning matters more than the table.

Two dependencies instead of four, and each removal was a wrapper going away.BlueSocket was
wrapping a local Unix socket, so it becameAF_UNIXdirectly. HotKey was wrapping Carbon'sRegisterEventHotKey, which is one call plus the bookkeeping to unregister it. ISSoundAdditions was wrapping CoreAudio.
swift-collections supplied one ordered dictionary. The ANTLR-generated shell grammar parsed command
strings that/bin/bash -calready parses. Every one of those is a thing that can break on an OS
update, or need a version bump before the app can be rebuilt, in exchange for code the platform
already provides. Sparkle is the one addition, and only because there is no App Store update path
to inherit.

Display identity comes from CoreGraphics, not IOKit.Upstream reads EDID throughIOServiceMatching("IODisplayConnect"). That IOKit class does not exist on Apple Silicon, so the
iterator yields nothing and vendor/model/serial come backnilfor every display. CoreGraphics
returns the same values and adds the per-display UUID, which is the only field that survives a
DisplayLink dock.

The private_AXUIElementGetWindowstays, and it costs something.It is the only way to get a
window id that is stable across refreshes, and window identity is what the whole tree is keyed on.
The price is that the Mac App Store is permanently out: private symbols fail review, and the
Accessibility APIs this app is built on do not work in a sandbox anyway. Hence Developer ID signing,
notarization, and Sparkle rather than TestFlight.

Workspace placement survives a restart of AeroSpork.Workspaces are emulated, so nothing
outside the process knows a window belongs to one; at a cold start a window is bound by where it
physically sits, and the workspace chosen for each monitor is the first key-bound name in sort order
— which a named workspace likeAcan never be. Placement is now remembered, keyed on the window id
the macOS window server issues. That id is stable for exactly as long as that server runs, so an
update, a crash or a Quit keeps it and a logout, a reboot or an application relaunching does not.
Where the id is gone there is no honest way to recognise a window — every terminal window reports the
same accessibility identifier — so it falls back to placing by location rather than guessing, andon-window-detectedremains the way to state intent.

The Xcode project is generated, not committed.project.ymlplus XcodeGen produces it, because
SwiftPM cannot build an app bundle but a checked-in.pbxprojis a merge conflict waiting to happen.
Debug builds skip Xcode entirely.

The config writer is line-based on purpose.Re-serializing the whole file would be far simpler,
and would destroy every comment plus anything the GUI cannot model, such as per-monitor gap arrays.
Instead it rewrites only the keys you changed, preserves what the panes cannot model (a rich
monitor fingerprint, a fallback list) field for field on every save, and refuses the few shapes it
cannot rewrite safely, pointing you at the Raw TOML pane. That is what makes a GUI safe to put on
top of a dotfile.

Sources/
├── aerosporkApp/ # app entry point (@main)
├── AppBundle/ # the window manager: tree/, layout/, command/, config/, model/, mouse/, ui/
├── Cli/ # command-line client
├── Common/ # shared with the CLI, incl. the socket implementation
└── PrivateApi/ # C shim for _AXUIElementGetWindow

## Differences from AeroSpace

The tree model, virtual workspaces, SIP-free operation, TOML config and the CLI are inherited and
behave the same way. Only the deltas are listed.

AeroSpace

AeroSpork

Monitor matching by hardware UUID / EDID

❌  name, regex or number only

✅  also pins DisplayLink panels

Settings GUI

❌  "will never provide a GUI for configuration"

✅  7 native panes

Notarized builds

❌

✅  signed, notarized, stapled

Third-party dependencies

4

2

Config schema

one syntax

v2 shorthand, older syntax still parses

Windows keep their workspace across a restart

❌

✅  also their monitor

Command surface

larger

smaller

Maturity

public beta, larger community

younger fork

Upstream column checked againstnikitabobko/AeroSpacemainon 2026-07-29: its README
says AeroSpace "will never provide a GUI for configuration" and that "it's not notarized", itsPackage.swiftdeclares four dependencies, and its guide documents monitor patterns as
main/secondary/number/regex only.

Config schema.modplusworkspacesgenerates the usual i3 keymap, and[keys],[monitors]and[on-window]replace the longer upstream spellings. An existing config is migrated once on
first launch, and only when the result is proven to parse to the same effective configuration;
otherwise the file is left alone. The original is kept beside it as*.pre-v2.

Settings GUI.Seven native preference panes in a compact macOS toolbar, over a
comment-preserving writer that only rewrites the keys you changed. Opening Settings and changing
nothing leaves the file byte-identical, and editing one section never rewrites another. The selected
pane is remembered. Raw TOML validates against the same parser the app uses at startup and adds
native Find, line numbers, restrained syntax highlighting, section navigation, cursor position, and
clickable source diagnostics, so no config key is unreachable from the GUI.

### Coming from AeroSpace

A fork, not a drop-in replacement. Configs and scripts need small edits.

* AEROSPACE_*environment variables are gone and not aliased. A script reading$AEROSPACE_FOCUSED_WORKSPACEgets an empty string with no error. The names areAEROSPORK_FOCUSED_WORKSPACE,AEROSPORK_PREV_WORKSPACE,AEROSPORK_WINDOW_IDandAEROSPORK_WORKSPACE.
* if.during-aerospace-startupis spelledif.during-aerospork-startup. Unknown keys are fatal, so
the old spelling fails at startup and names the line.
* Feature parity is a non-goal. The fork carries less surface area than upstream.

## Installation

Download the notarized universal (arm64 + x86_64) build from thereleases page, moveAeroSpork.appto/Applications, and grant Accessibility permission when prompted. A Homebrew cask is published atwbsmolen/tap:

brew install --cask wbsmolen/tap/aerospork

Both the tap and this repository are public, so either route works without a GitHub account.

Installed copies check for updates themselves throughSparkle,
against a signed appcast served fromaerospork.app/appcast.xml. Updates are verified against an
EdDSA public key in the app's Info.plist, so a build refuses anything it cannot verify. Automatic
checking is off until you allow it;Check for Updates…in the menu bar checks on demand. There
is no App Store update path to inherit, because the Accessibility APIs this app is built on do not
work in a sandbox.

Because update checks are the only network request AeroSpork can make, and the Accessibility
permission it needs is a broad one,aerospork.app/privacy.htmlsets out exactly what is stored, what is sent, and what is not: no analytics, no telemetry, and no
system profile.

## Configuration

The rendered docs live ataerospork.app/docs— the guide,
the command reference, and goodies — and the same content is indocs/here.

AeroSpork reads whichever of these exists, and reports an error at startup if both do:~/.aerospork.tomlor${XDG_CONFIG_HOME}/aerospork/aerospork.toml(XDG_CONFIG_HOMEdefaults to~/.config). With neither, it falls back to a complete default bundled in the app, also checked in
asdocs/config-examples/default-config.toml. Saved
changes hot-reload, so you never need to runreload-configby hand.

mod
 = 
"
alt
"
 
#
 generates the i3 keymap: alt-h/j/k/l, alt-shift-h/j/k/l, ...

workspaces
 = 
"
1-9
"
 
#
 alt-1..9 to switch, alt-shift-1..9 to move a window

[
gaps
]

inner
 = 
8

outer
 = 
8

[
keys
] 
#
 anything here overrides a generated binding

alt-enter
 = 
"
exec-and-forget open -na Ghostty
"

[
monitors
] 
#
 pin a workspace to a screen

1
 = 
"
main
"

2
 = { 
uuid
 = 
"
AAAAAAAA-0000-4000-8000-000000000001
"
 }

[
on-window
] 
#
 where a window goes when it appears

"com.apple.mail"
 = 
"
move-node-to-workspace 3
"

Runaerospork list-monitors --format '%{monitor-fingerprint}'to get the values to paste into[monitors]. Open the GUI from the menu bar icon, with⌘,while AeroSpork is frontmost, or viaaerospork open-settings, which is also valid in config and so bindable. Structured panes apply live
on a 600ms debounce; Raw TOML has an explicit Apply, because half-typed TOML is invalid most
of the time.

## CLI

36 subcommands, with man pages and bash/fish/zsh completion.exec-and-forgetis documented as a
37th command but is config-only.

aerospork focus left 
#
 focus the window to the left

aerospork workspace 1 
#
 switch workspace

aerospork move-node-to-workspace 2 
#
 move the focused window

aerospork layout tiles horizontal vertical 
#
 cycle layout

aerospork list-monitors 
#
 connected displays and how they are identified

aerospork --help

Troubleshooting:aerospork config --config-pathprints the file actually loaded. A path inside the.appbundle means no user config is loaded, either because you have none or because yours failed to
parse;aerospork reload-config --dry-runparses without applying and says which.aerospork --versionreports both client and server. Logs go to the unified log, with no files and nothing to
enable:

log show --last 1h --predicate 
'
subsystem == "com.wbs.aerospork"
'
 --style compact

Usecom.wbs.aerospork.debugfor a debug build and addAND category == "config"to narrow.AEROSPORK_DEBUG_LOG=1adds a verbose per-refresh trace. It is written at.debuglevel, which
the unified log does not persist, so run the binary directly and read its stderr. SeeTroubleshooting and bug reportsinthe guidefor what to attach to a report.

## Development

./build-debug.sh 
#
 SwiftPM debug build into .debug/ (uses ~/.aerospork-debug.toml)

./build-release.sh 
#
 signed release; needs a Developer ID Application certificate

./run-tests.sh 
#
 tests, format and lint

./build-docs.sh 
#
 man pages and docs site

The suite is headless, using a fake window tree and a mocked Accessibility layer, so it needs no real
windows and no Accessibility permission.Package.swiftuses SE-0439 trailing commas, so the floor is
Swift 6.1 (Xcode 16.3);.swift-versionpins 6.4 for reproducibility.

dev-docs/redesign-v3/records the implemented native-settings decision,
the verified light/dark ideal/compact mock matrix, and the production mapping..claude/skills/aerospork-design/holds the living design system:
tokens, 32 components, three click-through UI kits and the brand artwork. It is derived fromSources/AppBundle/ui/, so the Swift is the source of truth. Read it before adding a settings
surface.UIChromeConsistencyTestenforces the two rules that matter: shared controls live inSettingsChrome.swiftand a pane never grows its own
copy, and status symbols come fromStatusLabel.Kindrather than string literals.

CONTRIBUTING.mdcovers the gate and the invariants the tests enforce.dev-docs/has architecture notes, contributor setup including code signing, testing
strategy and performance measurement.

## License

MIT. The original AeroSpace copyright is retained alongside the fork's inLICENSE.txt. Active development; features and configuration may still
change.