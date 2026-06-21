---
title: 'GitHub - mysk-research/loupe: A privacy-focused iOS app that raises awareness about what native apps can see · GitHub'
url: https://github.com/mysk-research/loupe
site_name: hackernews_api
content_file: hackernews_api-github-mysk-researchloupe-a-privacy-focused-ios-ap
fetched_at: '2026-06-21T11:56:48.062260'
original_url: https://github.com/mysk-research/loupe
author: Cider9986
date: '2026-06-20'
description: A privacy-focused iOS app that raises awareness about what native apps can see - mysk-research/loupe
tags:
- hackernews
- trending
---

mysk-research

 

/

loupe

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork36
* Star901

 
 
 
 
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

4 Commits
4 Commits
.github
.github
 
 
app-store
app-store
 
 
code
code
 
 
docs/
images
docs/
images
 
 
fastlane
fastlane
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
Gemfile
Gemfile
 
 
Gemfile.lock
Gemfile.lock
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Loupe

Loupe is an iOS and iPadOS app that gives you a hands-on tour of the device fingerprinting surface. It reads real values from public iOS APIs, the same ones any third-party app can call, and shows them to you raw. The point is simple: see what your iPhone quietly exposes, and why each reading helps an app recognize you again.

Trackers don't need your name, email, or location to recognize you online. Each reading isn't necessarily unique on its own, but together they form a fingerprint that follows you across apps and websites.

## How signals are organized

Loupe groups every reading into three tiers, reflecting the cost of access:

* Passive— visible to any app with no prompt at all (locale, time zone, screen, battery, and more).
* Needs Permission— readings that trigger an iOS prompt (contacts, photos, location, calendars).
* Advanced— clever side-channel uses of public APIs, such as URL-scheme probing viacanOpenURLand Keychain persistence across reinstalls.

## Privacy

Nothing Loupe reads leaves your device unless you explicitly export it. Values are shown raw, without aggregation or hashing. Nothing is uploaded, synced, or shared.

## A note on how this was built

Loupe was written almost entirely by AI coding tools.

## Building

You'll need Xcode 26 or newer.

1. Opencode/Loupe.xcodeproj.
2. Copycode/Config/Signing.local.xcconfig.exampletocode/Config/Signing.local.xcconfigand fill in your ownDEVELOPMENT_TEAMand bundle identifiers. This file is gitignored and never published.
3. Build and run on a device or simulator.

The project uses Xcode's buildable folders (folder references), so new Swift files are picked up automatically with no need to edit the project file.

### macOS

Loupe also builds for macOS. The Mac version is mostly complete, but a few things still need work before it's polished.

## Support the project

Loupe is free and open source. If it helped you see what apps can quietly learn about your device, the best way to support more work like this is to tryPsylo, our privacy-first browser for iPhone and iPad. Psylo gives you proxy-backed browsing, isolated tabs, and anti-fingerprinting protections.

You can also readwhy we built Psylo.

## License

Thesource codeis released under theMIT License.

The Loupe name and logo, the app icon, all other images and icons, and the design source files are © Mysk, all rights reserved, and are not covered by the MIT license.

## About

Loupe is made by Mysk.

* Website
* Blog
* X
* Mastodon

## About

A privacy-focused iOS app that raises awareness about what native apps can see

### Resources

 Readme

 

### License

 View license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

901

 stars
 

### Watchers

2

 watching
 

### Forks

36

 forks
 

 Report repository

 

## Releases

No releases published

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* patreon.com/mysk
* buymeacoffee.com/mysk
* https://apps.apple.com/app/id6741358035

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Swift98.7%
* Ruby1.3%