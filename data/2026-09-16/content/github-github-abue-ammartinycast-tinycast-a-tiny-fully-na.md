---
title: 'GitHub - abue-ammar/tinycast: Tinycast — a tiny, fully native macOS launcher, hotkeys, and clipboard history. · GitHub'
url: https://github.com/abue-ammar/tinycast
site_name: github
content_file: github-github-abue-ammartinycast-tinycast-a-tiny-fully-na
fetched_at: '2026-09-16T15:21:39.019456'
original_url: https://github.com/abue-ammar/tinycast
author: abue-ammar
description: Tinycast — a tiny, fully native macOS launcher, hotkeys, and clipboard history. - abue-ammar/tinycast
---

abue-ammar

 

/

tinycast

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork251
* Star5.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

573 Commits
573 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
.vscode
.vscode
 
 
Scripts
Scripts
 
 
Tests
Tests
 
 
Tinycast.xcodeproj
Tinycast.xcodeproj
 
 
Tinycast
Tinycast
 
 
docs
docs
 
 
website
website
 
 
.gitignore
.gitignore
 
 
.swift-format
.swift-format
 
 
.swiftlint.yml
.swiftlint.yml
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTOR_LICENSE_AND_FEEDBACK_AGREEMENT.md
CONTRIBUTOR_LICENSE_AND_FEEDBACK_AGREEMENT.md
 
 
LICENSE
LICENSE
 
 
NOTICE.md
NOTICE.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
project.yml
project.yml
 
 
View all files

## Repository files navigation

# Tinycast

A tiny, fully native macOS launcher. One hotkey, everything you reach for all day, under 100 MB of
RAM.

SwiftUI and AppKit,zero third-party dependencies, no Electron and no telemetry. It alsoruns
real Raycast extensions, rendered as native SwiftUI. Free, open source, and staying that way.

For anything private, emailiabueammar@gmail.com.

## Support

Tinycast isfree, and it stays that way. If it earns a place in your daily flow, a one-off tip helps
keep it actively maintained. GitHub Sponsors isn't available in my country, so please support here:

Payments are handled securely byPolar.sh.

## Features

* App launcher— fuzzy-search and launch anything, pin favorites, see what's running, quit an app
or every app at once.
* Global hotkey— one shortcut summons the palette from anywhere.
* Per-app hotkeys— bind a key to an app; press it to toggle (focus/hide).
* Search Files— open files and folders from the folders you choose, through Spotlight, with no
index of our own.
* Clipboard history— text and images, searchable, pasted back into the app you were using.
* Calculator— do math, unit, live currency and crypto conversions inline, right in the palette.
* Quicklinks— turn a URL, search, file or deeplink into a command, with placeholders for typed
input, the clipboard or the date.
* Apple Shortcuts— search and run the shortcuts you built in the Shortcuts app, with aliases and
global hotkeys.
* Snippets— reusable Markdown templates with dynamic placeholders, arguments, nested references
and optional keyword expansion.
* Custom commands— run named shell commands through fuzzy search or their own global hotkeys.
* Window management— 34 Rectangle-style actions: halves, quarters, thirds, sizing, nudging,
display moves, fullscreen and Spaces.
* System actions— lock, sleep, restart, empty trash, toggle appearance, Bluetooth, mute, hidden
files, and more.
* Calendar and meetings— your next meeting on the empty palette and in the menu bar, one key to
join it, or let it join itself.
* Notes— an unlimited collection of plain Markdown files in one floating editor, searchable from
the palette.
* Emoji picker— a searchable emoji grid, one keystroke away.
* AI chat— use your own key or an installed AI account, chat from the palette. Off out of the box, like every AI feature.
* Quick Actions— fix grammar, rewrite, translate or summarize the selected text in any app.
* Raycast extensions— run the ones you already have natively, rendered as SwiftUI.
* Backup and import— export your settings to a file, or import your setup from Raycast.

## Install

First, add the tap:

brew trust --tap abue-ammar/tinycast 
#
 required for third-party taps

brew tap abue-ammar/tinycast

Then run the one line that matches your Mac:

Your Mac

Install

Apple silicon, macOS 26 or newer

brew install --cask tinycast

Intel, macOS 26

brew install --cask tinycast-universal

macOS 15 Sequoia 
(no longer maintained)

brew install --cask tinycast-sequoia

Not sure which you have?Apple menu → About This Mac.Homebrew checks too, and refuses the
wrong one.

Want early builds?brew install --cask tinycast@betaputsTinycast Beta.appbeside the stable
app, with its own settings and permissions. Apple silicon, macOS 26+.

Homebrew clears the macOS quarantine flag on every install and update, so there is nothing else to
run. Downloading a DMG fromReleasesinstead?
Tinycast is self-signed, so clear the flag once:xattr -dr com.apple.quarantine "/Applications/Tinycast.app".

## Permissions

Accessibility— needed when Tinycast pastes or expands text into another app, and the only
permission snippet keyword expansion needs. You're prompted when you first use a feature that needs
it; grant access inSystem Settings → Privacy & Security → Accessibility. Snippets ship
disabled, and keystrokes are matched locally, never stored and never sent anywhere.

## Using it

1. OpenSettings → Generaland record a global shortcut to summon Tinycast.
2. Press it anywhere → the palette floats in. Type to filter,↵to launch.
3. Tabswitches between Apps and Clipboard;↑/↓move,Escdismisses.
4. Settings → Shortcuts— search an app or custom command and record a global shortcut.
5. Settings → Snippets— enable the feature, then create templates with expansion keywords.

## Building from source

Seedocs/development.mdfor the toolchain, build, packaging, release and
website workflows.docs/indexes everything else — architecture, engineering
standards, the design system and one document per feature.

## Contributing

Important

Open an issue before you write code — this is mandatory.Get the bug or the feature agreed on
first; discussing it in the issue (or onDiscord) is strongly
encouraged. A PR that doesn't close an issue markedapprovedis closed automatically however good
the patch is, and the work is wasted. Docs-only fixes are the one exception.

Tinycast's feature set is deliberately closed, and "another launcher has it" is not a reason on its
own. Ask whether a feature is wanted before you ask for it.

ReadCONTRIBUTING.mdfirst — it covers the memory budget every PR is held to,
the before/after video requirement for visual changes, and why features get declined. Every PR fills
in thepull request template. Security issues go throughSECURITY.md, not the issue tracker.

Questions, ideas, or just want to follow along?Join the Discord.

## License

AGPL-3.0