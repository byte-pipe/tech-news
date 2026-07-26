---
title: 'GitHub - amnezia-vpn/amnezia-client: Amnezia VPN Client (Desktop+Mobile) · GitHub'
url: https://github.com/amnezia-vpn/amnezia-client
site_name: github
content_file: github-github-amnezia-vpnamnezia-client-amnezia-vpn-clien
fetched_at: '2026-07-26T11:30:17.765823'
original_url: https://github.com/amnezia-vpn/amnezia-client
author: amnezia-vpn
description: Amnezia VPN Client (Desktop+Mobile). Contribute to amnezia-vpn/amnezia-client development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 amnezia-vpn

 

/

amnezia-client

Public

* NotificationsYou must be signed in to change notification settings
* Fork997
* Star13.1k

 
 
 
dev
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

2,931 Commits
2,931 Commits
.github
.github
 
 
client
client
 
 
cmake
cmake
 
 
common
common
 
 
deploy
deploy
 
 
docs
docs
 
 
ipc
ipc
 
 
metadata
metadata
 
 
recipes
recipes
 
 
service
service
 
 
.clang-format
.clang-format
 
 
.clang-format-ignore
.clang-format-ignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.gitpod.Dockerfile
.gitpod.Dockerfile
 
 
.gitpod.yml
.gitpod.yml
 
 
CMakeLists.txt
CMakeLists.txt
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README_RU.md
README_RU.md
 
 
THIRD_PARTY_LICENSES.md
THIRD_PARTY_LICENSES.md
 
 
conanfile.py
conanfile.py
 
 
version.h.in
version.h.in
 
 
View all files

## Repository files navigation

# Amnezia VPN

### The best client for self-hosted VPN

### English |Русский

Amneziais an open-source VPN client, with a key feature that enables you to deploy your own VPN server on your server.

### Website|Alt website link|Documentation|Troubleshooting

Tip

If theAmnezia websiteis blocked in your region, you can use anAlternative website link.

All releases

## Features

* Very easy to use - enter your IP address, SSH login, password and Amnezia will automatically install VPN docker containers to your server and connect to the VPN.
* Classic VPN-protocols: OpenVPN, WireGuard and IKEv2 protocols.
* Protocols with traffic Masking (Obfuscation): OpenVPN overCloakplugin, Shadowsocks (OpenVPN over Shadowsocks),AmneziaWGand XRay.
* Split tunneling support - add any sites to the client to enable VPN only for them or add Apps (only for Android and Desktop).
* Windows, MacOS, Linux, Android, iOS releases.
* Support for AmneziaWG protocol configuration onKeenetic beta firmware.

## Links

* https://amnezia.org- Project website |Alternative link (mirror)
* https://docs.amnezia.org- Documentation |Alternative link (mirror)
* https://www.reddit.com/r/AmneziaVPN- Reddit
* https://telegram.me/amnezia_vpn_en- Telegram support channel (English)
* https://telegram.me/amnezia_vpn_ir- Telegram support channel (Farsi)
* https://telegram.me/amnezia_vpn_mm- Telegram support channel (Myanmar)
* https://telegram.me/amnezia_vpn- Telegram support channel (Russian)
* Get Premium for 6 or 12 months

## Tech

AmneziaVPN uses several open-source projects to work:

* OpenSSL
* OpenVPN
* Qt
* LibSsh
* WireGuard
* Xray-core
* Conan
* and more...

## Help us with translations

Download the most actual translation files.

Go to"Actions" tab, click on the first line.
Then scroll down to the "Artifacts" section and download "AmneziaVPN_translations".

Unzip this file.
Each *.ts file contains strings for one corresponding language.

Translate or correct some strings in one or multiple *.ts files and commit them back to this repository into theclient/translationsfolder.
You can do it via a web-interface or any other method you're familiar with.

## Checking out the source code

Make sure to pull all submodules after checking out the repo.

git submodule update --init --recursive

## Hacking guide

Want to contribute? Welcome!

### Build requirements

* CMake
* Compiler and underlying build system, depending on the target:[Linux] Any ofmakeandgcc[Apple]XcodeorXcode command line tools[Windows]Visual Studio 2022orVS 2022 Build Tools[Android]Android SDKandNinja
* [Linux] Any ofmakeandgcc
* [Apple]XcodeorXcode command line tools
* [Windows]Visual Studio 2022orVS 2022 Build Tools
* [Android]Android SDKandNinja
* Qt 6.10+with the following modules:Core module for targeting platform (Desktop/Android/iOS)Qt 5 Compatibility moduleQt Remote Objects
* Core module for targeting platform (Desktop/Android/iOS)
* Qt 5 Compatibility module
* Qt Remote Objects
* Conanpackage managerOn MacOS is enough just to usehomebrewor install it in.venvin project rootOther systems must have it inPATH
* On MacOS is enough just to usehomebrewor install it in.venvin project root
* Other systems must have it inPATH
* (Optional) Installer dependencies:[Windows/Linux]Qt Installer Framework[Windows]WIX toolset
* [Windows/Linux]Qt Installer Framework
* [Windows]WIX toolset

### Building the project using scripts

* Run scripts located indeploydirectory
* Basically, if dependencies are located in default installation paths, the scripts will find them automatically.
* If they differ, specify them using the following variables:QT_INSTALL_DIR- Qt root installation folderQT_ROOT_PATH- Qt framework root directoryQIF_ROOT_PATH- Qt Installer Framework root pathANDROID_HOME- Path to Android SDK root folderand others. Check scripts for more
* QT_INSTALL_DIR- Qt root installation folder
* QT_ROOT_PATH- Qt framework root directory
* QIF_ROOT_PATH- Qt Installer Framework root path
* ANDROID_HOME- Path to Android SDK root folder
* and others. Check scripts for more

Unix-like:

#
 Build executables for the host platform

deploy/build.sh

#
 Or just

deploy/build.sh

#
 Build executables and installers for the host platform

deploy/build.sh --installer all

#
 Build Android APK and AAB

deploy/build.sh -t android --aab

#
 Call for help

deploy/build.sh -h

Windows:

::
 Build executables for Windows

deploy/build.bat

::
 Build executables with IFW installer for Windows

deploy/build.bat --installer ifw

::
 Build executables with IFW and WIX installer for Windows

deploy/build.bat --installer ifw --installer wix

::
 Or just

deploy/build.bat --installer all

### Developing the project in IDEs

* Basically, you can use any IDE that handles CMake and Qt kits properly to run configure and build steps, and to navigate through the code nicely. For example:Qt CreatorVisual Studio CodewithQt Extension Packand so on
* Qt Creator
* Visual Studio CodewithQt Extension Pack
* and so on
* To useXcode, you have to configure project first by usingcmake. The easiest way to do it is to useQt Creatorfor configuration. Then openAmneziaVPN.xcodeprojfile from the build folder by usingXcode. Note that none of the files changed are saved - the files actually getting changed in build directory. Copy them manually if necessary
* Android studiocould be used in the same way - just configure the project by usingcmakemanually or by usingQt Creator. Open<build-dir>/client/android-buildinAndroid studiothen. Do not forget to copy the changes - everything you do is saved under the build directory actually.

### Installing Android SDK

* Android SDK could be installed using the following methods:UsingQt Creator. UsePreferences->SDKsUsingAndroid studio. By default it installs necessarySDKsautomatically during the installationManually by usingsdk-manager. Checkthispage for details
* UsingQt Creator. UsePreferences->SDKs
* UsingAndroid studio. By default it installs necessarySDKsautomatically during the installation
* Manually by usingsdk-manager. Checkthispage for details

## License

This project is licensed under the GNU General Public License v3.0 (see LICENSE) and also includes third-party components distributed under their own terms (see THIRD_PARTY_LICENSES.md).

## Donate

Patreon:https://www.patreon.com/amneziavpn

Bitcoin: bc1qmhtgcf9637rl3kqyy22r2a8wa8laka4t9rx2mfUSDT BEP20: 0x6abD576765a826f87D1D95183438f9408C901bE4USDT TRC20: TELAitazF1MZGmiNjTcnxDjEiH5oe7LC9dXMR: 48spms39jt1L2L5vyw2RQW6CXD6odUd4jFu19GZcDyKKQV9U88wsJVjSbL4CfRys37jVMdoaWVPSvezCQPhHXUW5UKLqUp3TON: UQDpU1CyKRmg7L8mNScKk9FRc2SlESuI7N-Hby4nX-CcVmns

## Acknowledgments

This project is tested with BrowserStack.
We express our gratitude toBrowserStackfor supporting our project.