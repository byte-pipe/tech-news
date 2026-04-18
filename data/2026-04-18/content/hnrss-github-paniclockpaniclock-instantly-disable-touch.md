---
title: 'GitHub - paniclock/paniclock: Instantly disable Touch ID and lock your Mac with one click or keyboard shortcut. · GitHub'
url: https://github.com/paniclock/paniclock/
site_name: hnrss
content_file: hnrss-github-paniclockpaniclock-instantly-disable-touch
fetched_at: '2026-04-18T11:34:31.350685'
original_url: https://github.com/paniclock/paniclock/
date: '2026-04-17'
description: Instantly disable Touch ID and lock your Mac with one click or keyboard shortcut. - paniclock/paniclock
tags:
- hackernews
- hnrss
---

paniclock

 

/

paniclock

Public

* NotificationsYou must be signed in to change notification settings
* Fork3
* Star222

 
 
 
 
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

55 Commits
55 Commits
.github
.github
 
 
PanicLock.xcodeproj
PanicLock.xcodeproj
 
 
PanicLock
PanicLock
 
 
PanicLockHelper
PanicLockHelper
 
 
Shared
Shared
 
 
assets
assets
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
ExportOptions.plist
ExportOptions.plist
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
View all files

## Repository files navigation

PanicLock is macOS menu bar utility that instantly disables Touch ID and locks the screen with a single click or closing your laptop lid.

PanicLock fills a gap macOS leaves open: there is no built-in way to instantly disable Touch ID when it matters. Biometrics are convenient day-to-day, and sometimes preferable when you need speed or want to avoid your password being observed. But in sensitive situations, law enforcement and border agents in many countries can compel a biometric unlock in ways they cannot with a password. PanicLock gives you a one-click menu bar button, a customizable hotkey, or an automatic lock-on-lid-close option that immediately disables Touch ID and locks your screen, restoring password-only protection without killing your session or shutting down.

## Features

* One-click panic lock— Click the menu bar icon or press a hotkey to instantly lock
* Lock on Close— Optionally lock and disable Touch ID when you close the lid
* Temporarily disables Touch ID— Forces password-only unlock
* Auto-restore— Original Touch ID settings restored after unlock
* Keyboard shortcut— Configure a global hotkey (e.g., ⌃⌥⌘L)
* Launch at login— Start automatically when you log in

## Install

### Homebrew

brew install paniclock/tap/paniclock

### Manual Download

Download the latest DMG from thereleases page.

## Requirements

* macOS 14.0 (Sonoma) or later
* Mac with Touch ID

## Usage

Action

Result

Left-click
 icon

Trigger panic lock immediately

Right-click
 icon

Open menu (Preferences, Uninstall, Quit)

### Lock on Close

When enabled in Preferences, closing your Mac's lid will automatically disable Touch ID and lock your screen. Touch ID stays disabled until you re-login with your password. If your screen locks for other reasons (screensaver, display sleep, etc.), Touch ID will still work as normal.

### First Launch

On first use, you'll be prompted for your admin password to install the privileged helper. This is a one-time setup.

## Building from Source

1. Clone this repository
2. OpenPanicLock.xcodeprojin Xcode
3. Set your Development Team in both targets (PanicLock and PanicLockHelper)
4. Update Team ID inInfo.plist(SMPrivilegedExecutables) andInfo-Helper.plist(SMAuthorizedClients)
5. Build and run

## Uninstall

Homebrew:

brew uninstall paniclock

From the app:Right-click → "Uninstall PanicLock..." → Enter admin password

Manual:

sudo launchctl bootout system/com.paniclock.helper
sudo rm -f /Library/PrivilegedHelperTools/com.paniclock.helper
sudo rm -f /Library/LaunchDaemons/com.paniclock.helper.plist
rm -rf /Applications/PanicLock.app

## How It Works

PanicLock uses a privileged helper (installed via SMJobBless) to modify Touch ID timeout settings:

1. Reads current timeout viabioutil -r -s
2. Sets timeout to 1 second viabioutil -w -s -o 1
3. Locks screen viapmset displaysleepnow
4. Restores original timeout after ~2 seconds

## Security

* Minimal privileges— Helper only runs 3 hardcoded commands (bioutil,pmset)
* Code-signed XPC— Helper verifies connecting app's bundle ID + team ID + certificate
* No network activity— App is 100% offline, no telemetry or analytics
* No data collection— Only stores preferences (icon style, keyboard shortcut)
* Open source— Full code available for audit

Note: PanicLock only disables Touch ID. If you have other unlock methods enabled, Apple Watch unlock, security keys, etc., your Mac can still be unlocked using those.

## Releasing

The release script handles building, signing, notarizing, and packaging:

./scripts/release.sh

Features:

* Extracts version from Xcode project automatically
* Signs with Developer ID for distribution outside the App Store
* Submits to Apple for notarization (can take minutes to hours)
* Creates a notarized DMG for distribution
* Supports parallel notarizations — each version gets its ownbuild/release/<version>/directory

Workflow:

1. BumpMARKETING_VERSIONin Xcode
2. Run./scripts/release.sh— builds and submits for notarization
3. Run again later to check status and continue when approved
4. Final output:build/release/<version>/PanicLock-<version>.dmg

## License

MIT License — SeeLICENSEfor details.

## Contributing

Contributions welcome! Please open an issue or pull request.

## About

Instantly disable Touch ID and lock your Mac with one click or keyboard shortcut.

paniclock.github.io/

### Topics

 macos

 apple

 locking

 security-tools

 privacy-tools

### Resources

 Readme

 

### License

 MIT license
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

222

 stars
 

### Watchers

2

 watching
 

### Forks

3

 forks
 

 Report repository

 

## Releases8

v1.0.9

 Latest

 

Apr 17, 2026

 

+ 7 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Swift72.6%
* Shell27.4%