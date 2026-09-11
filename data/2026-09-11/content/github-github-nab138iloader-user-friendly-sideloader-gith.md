---
title: 'GitHub - nab138/iloader: User friendly sideloader · GitHub'
url: https://github.com/nab138/iloader
site_name: github
content_file: github-github-nab138iloader-user-friendly-sideloader-gith
fetched_at: '2026-09-11T14:51:33.101617'
original_url: https://github.com/nab138/iloader
author: nab138
description: User friendly sideloader. Contribute to nab138/iloader development by creating an account on GitHub.
---

nab138

 

/

iloader

Public

* NotificationsYou must be signed in to change notification settings
* Fork197
* Star2.8k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

447 Commits
447 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
.vscode
.vscode
 
 
public
public
 
 
src-tauri
src-tauri
 
 
src
src
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
LICENSE-BRANDING
LICENSE-BRANDING
 
 
README.md
README.md
 
 
bun.lock
bun.lock
 
 
count_downloads.ts
count_downloads.ts
 
 
default.nix
default.nix
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
iloader-dark.svg
iloader-dark.svg
 
 
iloader.svg
iloader.svg
 
 
index.html
index.html
 
 
package.json
package.json
 
 
shell.nix
shell.nix
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.node.json
tsconfig.node.json
 
 
vite.config.ts
vite.config.ts
 
 
View all files

## Repository files navigation

 

Install SideStore (or other apps) and import your pairing file with ease

This repository andiloader.appare the only official ways to download iloader. There is also an unofficialHomebrew cask, an unofficialAUR package, and an unofficialFedora COPR repositorymaintained by the community. Do not download from any other sources or websites.

## How to use

* Install usbmuxd for your platformWindows:iTunesmacOS: IncludedLinux: Potentially included, if not, install via your package manager
* Windows:iTunes
* macOS: Included
* Linux: Potentially included, if not, install via your package manager
* Install the latest version for your platform from thereleasesNixOS: Use the flakegithub:nab138/iloader
* NixOS: Use the flakegithub:nab138/iloader
* Plug in your iDevice to your computer
* Open the app
* Sign into your Apple ID
* Select your action (e.g. install SideStore)

## Features

* Install SideStore (or LiveContainer + SideStore), import certificate and place rppairing+lockdown pairing files automatically
* Import any IPA
* Intelligent error suggestions to help resolve common issues
* Manage pairing files in apps like StikDebug, SideStore, Protokolle, etc
* See and revoke development certificates & app ids

## Troubleshooting

* If you are unable to solve an issue on your own, copy the full error message and ask on theidevice Discord serveroropen an issue.
* You can view app logs with the "View Logs." If nothing is showing up, change the log level to "Debug."
* If those logs aren't helpful, logs with additional are stored in the following locations:Windows:%APPDATA%\me.nabdev.iloader\logsmacOS:~/Library/Application Support/me.nabdev.iloader/logsLinux:~/.local/share/me.nabdev.iloader/logs/
* Windows:%APPDATA%\me.nabdev.iloader\logs
* macOS:~/Library/Application Support/me.nabdev.iloader/logs
* Linux:~/.local/share/me.nabdev.iloader/logs/

## Translating

iloader needs localization! If you speak another language and notice iloader does not support it or has mistakes, please consider contributing.

To update/edit an existing language, make a PR modifyingsrc/locales/<lang>.json.

To add a new language, add your language tosrc/i18next.ts, and insrc/localescopyen.jsonto a new file titled<langcode>.jsonand update the strings.

i18next.ts:

const
 
languages
 
=
 
[

 
[
"en"
,
 
"English"
]
,

 
[
"es"
,
 
"Español"
]
,

 
// Your language here...

]
 
as
 
const
;

You can also add your name to the translators section of the README.

Thank you for translating!

## Building from source

1. Installbun(orNode.js) andRust
2. Clone the repository andcdinto it
3. Runbun i(ornpm i)

For development with hot reload:bun tauri dev(ornpm run tauri dev)
Make a production build:bun tauri build(ornpm run tauri build)

## Credits

* Icon made byTransistor
* UI improved byStephenDev0
* idevicebyjkcoxsonfor communicating with iOS devices
* isideloadfor installing appsidevicebyjkcoxsoncrate is used to communicate with the deviceapple-codesign-quickbyDadoumfor codesigning and entitlementsImpactorbyclarationwas used as a reference for cryptography operations (converting certs to p12, etc.).SideloaderbyDadoumwas used as a reference for how apple private developer endpoints work
* idevicebyjkcoxsoncrate is used to communicate with the device
* apple-codesign-quickbyDadoumfor codesigning and entitlements
* Impactorbyclarationwas used as a reference for cryptography operations (converting certs to p12, etc.).
* SideloaderbyDadoumwas used as a reference for how apple private developer endpoints work
* idevice_pairwas used as a reference for pairing file management
* App made withtauri

## Translators

Thank you to everyone who has contributed translations! See theTranslatingsection if you would like to contribute as well.

* By3lish: Azerbaijani (az)
* TNT-333: German (de)
* basketshoe: Italian (it)
* baocreata: Vietnamese (vt)
* IamArayel: French (fr)
* kkula9999: Traditional & Simplified Chinese (zh_tw & zh_cn)
* sibwaze: Russian (ru)
* notmalicik: Română (ro)
* mirdukkkkk: Improved Russian (ru)
* okinaau: Arabic (ar)
* ChouChiu: Cantonese (zh_hk) & Improved Chinese (zh_tw & zh_cn)
* marcinmajsc: Polish (pl)
* ern775: Turkish (tr)
* canpng: Improved Turkish (tr)
* jazoppix: Spanish (es)
* eseiker: Korean (ko)
* seomin0610: Improved Korean (ko)
* Ordyan777: Armenian (am)
* kakik0u: Japanese (ja)
* lkspodmol: Czech (cs_cz)
* marcusherelammonstyle-cmd: Swedish (sv)
* MCI49312: Hungarian (hu)
* Kynonim: Indonesian (id)
* DD00031: Dutch (nl)
* Toritan123: Improved Japanese (ja)
* marcinmajsc: Improved Polish (pl)
* dleiferives: Greek (el)
* ShadowWLX: Improved French (fr)
* fkpcomposer: Brazilian Portuguese (pt_br)
* 474FrediFred: Swiss German (de_ch)

## License

Copyright (C) 2026 nab138

The source code of this repository is licensed under the MIT License. See theLICENSEfile for the full text.

Branding, logos, media assets, and the name “iloader” are not licensed under the MIT License and are subject to separate restrictions.

You may retain or use branding materials in forks, tutorials, or documentation if you include a clear link to either the official site (https://iloader.app) or the iloader source code repository (https://github.com/nab138/iloader) and do not imply official endorsement. SeeLICENSE-BRANDINGfor full details.

## Future Plans

* Checks for if device is in developer mode, has password set, etc
* Automatic anisette fallback
* Team selection when an account has multiple teams
* Auto-refresh installed appsMinimize to trayDetect installed appsRefresh apps automatically
* Minimize to tray
* Detect installed apps
* Refresh apps automatically
* Set a "default" account to automatically log into
* Import SideStore account info automatically
* Mount DDI and open sidestore after installation