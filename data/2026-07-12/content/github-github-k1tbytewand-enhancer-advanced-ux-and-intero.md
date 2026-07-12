---
title: 'GitHub - k1tbyte/Wand-Enhancer: Advanced UX and interoperability extension for Wand (WeMod) app · GitHub'
url: https://github.com/k1tbyte/Wand-Enhancer
site_name: github
content_file: github-github-k1tbytewand-enhancer-advanced-ux-and-intero
fetched_at: '2026-07-12T11:27:17.027412'
original_url: https://github.com/k1tbyte/Wand-Enhancer
author: k1tbyte
description: Advanced UX and interoperability extension for Wand (WeMod) app - k1tbyte/Wand-Enhancer
---

k1tbyte

 

/

Wand-Enhancer

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork18.5k
* Star6.5k

 
 
 
 
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

59 Commits
59 Commits
.githooks
.githooks
 
 
.github
.github
 
 
AsarSharp
AsarSharp
 
 
WandEnhancer
WandEnhancer
 
 
assets
assets
 
 
scripts
scripts
 
 
tools/
asar-fuses-bypass
tools/
asar-fuses-bypass
 
 
web-panel
web-panel
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE.md
LICENSE.md
 
 
README.md
README.md
 
 
Wand-Enhancer.sln
Wand-Enhancer.sln
 
 
build.cmd
build.cmd
 
 
build.ps1
build.ps1
 
 
build.sh
build.sh
 
 
View all files

## Repository files navigation

# WandEnhancer

#### An open-source interoperability tool designed to extend local client-side configurations and improve the UX of the Wand application.

🚨 IMPORTANT NOTICE: THIS PROJECT HAS NO OFFICIAL YOUTUBE TUTORIALS, GUIDES, OR PREBUILT EXECUTABLE DOWNLOADS. 🚨
There are no official videos showing how to install or use this tool. Scammers are creating fake tutorials using this project's name and placing malware/password stealers in the video descriptions. Official GitHub releases contain release notes only, not.exefiles. If you downloaded an.exeor archive from a YouTube link, a random website, or a third-party mirror, you did not get it from this project. We are not responsible for third-party downloads.

## 👾 Is it safe to use?

Yes. This project is entirely open-source, allowing anyone to audit the code. It operates strictly locally, does not require internet access, and makes zero network requests. It simply adjusts local client settings to enhance your user experience.

## 💫 What features are improved?

✅ Local environment configuration management✅ Automated compatibility adjustments for new client versions✅ Advanced layout and theme customization (Client-side only)✅ AI Features✅ Remote web panel (Remote Connect on mobile)

## 🌐 Remote Web Panel

WandEnhancer includes a built-inRemote Web Panelallowing you to control app features directly from your phone.

### Quick Start:

1. Ensure both your PC and phone are on thesame Wi-Fi network.
2. Hover over theConnectbutton in the top bar of WandEnhancer.
3. Scan the displayedQR codewith your phone's camera.

### Troubleshooting & Remote Access:

* Page isn't loading?First, ensure both your PC and phone are connected to thesame local network. Some routers and guest Wi-Fi networks enable client isolation/AP isolation, which blocks devices on the same SSID from reaching each other. If it still does not load, check Windows Firewall and allow inbound traffic on TCP port3223for your local network. If Windows marked your connection asPublic, switching it toPrivatecan also help.
* Using mobile data or a different network?If you want to use the panel over mobile data (LTE/5G) or from an entirely different network, you can useTailscaleor similar VPN tools.

## 👀 How to use?

This repository does not publish official compiled binaries. Build your own executable from your own fork using GitHub Actions.

1. Sign in to GitHub and fork this repository.
2. Open your fork, go to theActionstab, and enable workflows if GitHub asks you to.
3. Select theBuild executableworkflow.
4. ClickRun workflow, keep the default branch, and start the run.
5. Wait for the workflow to finish, open the completed run, and download the artifact.
6. Extract the artifact zip and runWandEnhancer.exeto apply local client modifications.

Here how you do it:

usage-guide.mp4

## 🧩 Custom scripts

You can inject your own JavaScript into Wand at patch time to tweak or fix things in the client UI. This reuses the same renderer injection the Remote Web Panel uses, so it requires theRemote Web Panelpatch to be enabled.

How to add a script

* In the patch dialog, add one or more.jsfiles (only existing.jsfiles are accepted),or
* Drop.jsfiles into arenderer-scripts/folder placed next to the patcher executable.

Then patch as usual — your scripts are bundled into the client and run inside Wand's window.

How it runs

* Each script runs inside Wand's renderer (full DOM access, plus Noderequire).
* It is wrapped so a thrown error is logged and never crashes Wand.
* It may runmore than onceper launch (on load and again shortly after), so guard one‑time work behind a global flag.
* A smallWandEnhancerhelper is available:WandEnhancer.log(...),WandEnhancer.remoteUrl,WandEnhancer.apiVersion.

Minimal example(hello.js)

// Injected scripts can run multiple times — guard one-time setup.

if
 
(
!
globalThis
.
__helloScriptInstalled
)
 
{

 
globalThis
.
__helloScriptInstalled
 
=
 
true
;

 
WandEnhancer
.
log
(
"Hello from my custom script!"
,
 
WandEnhancer
.
remoteUrl
)
;

 
new
 
MutationObserver
(
(
)
 
=>
 
{

 
const
 
dialog
 
=
 
document
.
querySelector
(
"ux-dialog:not([data-seen])"
)
;

 
if
 
(
dialog
)
 
{

 
dialog
.
setAttribute
(
"data-seen"
,
 
"1"
)
;

 
WandEnhancer
.
log
(
"A dialog opened."
)
;

 
}

 
}
)
.
observe
(
document
.
documentElement
,
 
{
 
childList
: 
true
,
 
subtree
: 
true
 
}
)
;

}

Scripts run with the same privileges as the Wand client. Only add scripts you trust and understand.

## 🛠️ How to build from source

Building from source on Windows requires a local development environment.

### Requirements

* CMake
* Node.jsandpnpm
* Visual Studio 2022orBuild Tools for Visual Studio 2022withMSBuild
* Visual StudioDesktop development with C++workload
* .NET Framework 4.8 desktop build tools / targeting pack

### Build steps

1. Clone this repository.
2. Install the requirements above and make surecmake,pnpm, andMSBuildare available.
3. Runbuild.cmdfrom Command Prompt or PowerShell.

The build script installs the web panel dependencies, builds the frontend, compiles the native helper with CMake, restores NuGet packages, and builds the WPF solution.

## ❓ Q&A

* Why is there no.exein GitHub Releases?Official releases are notes-only on purpose. The project no longer distributes prebuilt executables because unsigned or self-built patching tools are repeatedly reuploaded, mislabeled, and flagged by third-party scanners. Build the executable from your own fork using GitHub Actions instead.
* Official releases are notes-only on purpose. The project no longer distributes prebuilt executables because unsigned or self-built patching tools are repeatedly reuploaded, mislabeled, and flagged by third-party scanners. Build the executable from your own fork using GitHub Actions instead.
* Where do I download the executable?From your own fork'sActionsartifact after running theBuild executableworkflow. Do not download.exefiles from YouTube descriptions, random mirrors, Discord attachments, or issue comments.
* From your own fork'sActionsartifact after running theBuild executableworkflow. Do not download.exefiles from YouTube descriptions, random mirrors, Discord attachments, or issue comments.
* Why does Windows Defender or SmartScreen warn about my build?The GitHub Actions artifact is unsigned and uncommon, so Windows may warn even when the code was built directly from your fork. Review the source, verify the workflow logs, and only run binaries you built yourself.
* The GitHub Actions artifact is unsigned and uncommon, so Windows may warn even when the code was built directly from your fork. Review the source, verify the workflow logs, and only run binaries you built yourself.
* Can I use a binary built by someone else?You can, but you should treat it as untrusted. This repository cannot verify or support third-party builds.
* You can, but you should treat it as untrusted. This repository cannot verify or support third-party builds.
* Does this send data anywhere?The desktop patching work is local to your machine. The Remote Web Panel is served from your PC on your local network.
* The desktop patching work is local to your machine. The Remote Web Panel is served from your PC on your local network.

## 🖼️ Screenshots

## 📜 License

This project is licensed under the Apache-2.0 - see theLICENSEfile for details.

## ❤️ Support

If you find this project useful, you can support its development using any of the options below 🙌

Legal Disclaimer:This project is a third-party enhancement tool intended solely for educational, research, and local interoperability purposes. It does not distribute any proprietary code or bypass server-side validations. All modifications are performed locally to customize the user's interface.

## About

Advanced UX and interoperability extension for Wand (WeMod) app

gitlab.com/kitbyte/wand-enhancer

### Topics

 csharp

 wpf

 wand

 wemod

 wand-pro

 wand-enhancer

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

6.5k

 stars
 

### Watchers

57

 watching
 

### Forks

18.5k

 forks
 

 Report repository

 

## Releases18

1.0.9.3

 Latest

 

Jul 4, 2026

 

+ 17 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* patreon.com/kitbyte
* https://www.patreon.com/kitbyte/gift
* https://tronscan.org/#/address/TQdvau8pAy5Tg1Aa588tTcPCFgbcHtuoxc
* https://www.blockchain.com/explorer/addresses/btc/1EZKDcyU8REm9JW5xwXJqSpn5Xaq5yAWWX
* https://etherscan.io/address/0xd904d9d0557f88bbb1c4ab3582b4ca0d8a730e8d

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C#88.0%
* C5.8%
* PowerShell5.5%
* Other0.7%