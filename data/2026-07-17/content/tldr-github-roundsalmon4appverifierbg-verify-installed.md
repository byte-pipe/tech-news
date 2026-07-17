---
title: 'GitHub - RoundSalmon4/AppVerifierBG: Verify installed apps against shared signature hashes, the internal database, or a user-created database. · GitHub'
url: https://github.com/RoundSalmon4/AppVerifierBG
site_name: tldr
content_file: tldr-github-roundsalmon4appverifierbg-verify-installed
fetched_at: '2026-07-17T11:31:55.843904'
original_url: https://github.com/RoundSalmon4/AppVerifierBG
date: '2026-07-17'
description: Verify installed apps against shared signature hashes, the internal database, or a user-created database. - RoundSalmon4/AppVerifierBG
tags:
- tldr
---

RoundSalmon4

 

/

AppVerifierBG

Public

 forked from 
soupslurpr/AppVerifier

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork2
* Star75

 
 
 
 
feature/all-enhancements
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

827 Commits
827 Commits
.github
.github
 
 
.idea
.idea
 
 
app
app
 
 
fastlane/
metadata/
android/
en-US
fastlane/
metadata/
android/
en-US
 
 
gradle
gradle
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE.material-symbols.txt
LICENSE.material-symbols.txt
 
 
LICENSE.txt
LICENSE.txt
 
 
PRIVACY.md
PRIVACY.md
 
 
README.md
README.md
 
 
build.gradle.kts
build.gradle.kts
 
 
featherqrcode.png
featherqrcode.png
 
 
gradle.properties
gradle.properties
 
 
gradlew
gradlew
 
 
gradlew.bat
gradlew.bat
 
 
ic_launcher.svg
ic_launcher.svg
 
 
mask-icon.png
mask-icon.png
 
 
mask-icon.svg
mask-icon.svg
 
 
renovate.json
renovate.json
 
 
settings.gradle.kts
settings.gradle.kts
 
 
View all files

## Repository files navigation

# AppVerifier BG

Verify installed apps against shared signature hashes, the internal database, or a user-created database. This fork extends the original AppVerifier — still does everything the original does, plus the features below.

## Verification

Pasted hashes are checked for valid SHA-256 format and show a clear error if something's wrong. When verification fails, hashes are labeled "Expected" (what you pasted) and "Found" (on-device fingerprint) so you can tell which is which. Apps signed with debug certificates are flagged as insecure. Verification results use chip-based status indicators. The expected vs. found hash comparison has a collapsible toggle. Split APK bundles (.apks, .apkm, .xapk) and ZIP files containing a base APK are accepted — the base APK is extracted and verified the same way as a regular APK.

## App List

Every installed user app shows status icons for internal database matches, user database entries, clipboard verification, and shared text matches all at a glance. Sort by name, database status, debug builds, clipboard verified, or shared text — pick whichever you need from the dropdown and it only shows modes with matching data. A filter chip hides everything except mismatches. The default sort order can be set in settings. A search bar lets you filter by name or package name. Long-press an app with a user database entry or clipboard checkmark to remove it individually.

## Shared Text

Share verification info for several apps at once. Multiple entries separated by blank lines are accepted on receive. When opening shared text with multiple entries, the app list filters to show matching apps only, with icons indicating hash match status. You can bulk-add all verified matches to your database from the filtered list. AppVerifier also handlesACTION_SENDandACTION_VIEWintents so you can share text or APK files directly from other apps.

## Clipboard Verification

Verify from clipboard with a single button on the startup screen. Successful clipboard verifications add a blue checkmark in the app list. The checkmark can be toggled on or off in settings and cleared separately. Individual checkmarks can be removed by long-pressing the app in the list.

## Hash-Only Verification

Paste or share a SHA-256 hash on its own and AppVerifier BG will find every installed app signed with that certificate. Handy when someone shares just a hash without a package name. If multiple installed apps share the same signing key — common when a developer uses one certificate for all their apps — a picker lets you choose the right one. Only verify the app you actually got the hash for; a matching certificate doesn't mean every app from that developer is safe to trust. Works from the clipboard, shared text, or an intent from another app.

## User Database

Save an app's verification info so you can check it later without needing the shared text. Add entries one at a time from the verification screen or bulk-add from a shared text filtered list. Supports import and export in JSON, text, and YAML formats (auto-detected on import, choose on export). Import lets you combine with existing entries or replace them, and shows a summary of what changed. Entries can be removed individually by long-pressing the app in the list, or removed in batch from selection mode.

Plain text— entries separated by a blank line:

com.example.app
AA:BB:CC:DD:EE:FF:00:11:...

com.other.app
11:22:33:44:55:66:77:88:...

JSON— array of objects with packageName, hashes, and hasMultipleSigners:

[
 {
"packageName"
: 
"
com.example.app
"
, 
"hashes"
: [
"
AA:BB:CC:DD:EE:FF:00:11:...
"
], 
"hasMultipleSigners"
: 
false
}
]

YAML— documents separated by---:

packageName
: 
com.example.app

hashes
:
 - 
AA:BB:CC:DD:EE:FF:00:11:...

---

packageName
: 
com.other.app

hashes
:
 - 
11:22:33:44:55:66:77:88:...

## Combined Database Status

See internal and user database results side by side on the app list and verification screen. A setting lets you choose between both, internal only, or user database only.

## Privacy Guides Database

The internal database is extended with entries fromprivacyguides/verified-apps, updated with each build. The database download is verified against GitHub attestations before every build.

## Community Hashes

Nightly builds include a downloadable text file with hashes shared by users on the GrapheneOS forum. These are not added to the internal database — import them into your user database if you wish. Cross-verify against multiple sources before relying on any entry.

## Share All Apps

Share every installed app's verification info as text from the settings screen.

## Theme Customization

Follow system theme, or pick light or dark mode. An AMOLED black theme option replaces all surfaces with pure black for OLED screens. On Android 12+, a dynamic color scheme option pulls colors from your wallpaper. In standard mode, primary and secondary colors are customizable with 12 preset swatches each. MATCH info dialogs (source names, domains, verification methods) follow the chosen secondary color.

## Support

If you find AppVerifier BG useful, consider supporting development:

XMR:

For the original README with download, community, and contributing info seehttps://github.com/soupslurpr/AppVerifier.

This repo is mirrored toCodeberg. Releases and release assets are synced automatically.

## About

Verify installed apps against shared signature hashes, the internal database, or a user-created database.

### Topics

 android

 security

 mobile

 kotlin-android

 apk

 security-tools

### Resources

 Readme

 

### License

 ISC license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

75

 stars
 

### Watchers

3

 watching
 

### Forks

2

 forks
 

 Report repository

 

## Releases27

v0.7.0

 Latest

 

Jul 17, 2026

 

+ 26 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* buymeacoffee.com/RoundSalmon4

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Kotlin100.0%