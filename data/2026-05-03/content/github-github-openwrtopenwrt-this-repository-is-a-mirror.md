---
title: 'GitHub - openwrt/openwrt: This repository is a mirror of https://git.openwrt.org/openwrt/openwrt.git It is for reference only and is not active for check-ins. We will continue to accept Pull Requests here. They will be merged via staging trees then into openwrt.git. · GitHub'
url: https://github.com/openwrt/openwrt
site_name: github
content_file: github-github-openwrtopenwrt-this-repository-is-a-mirror
fetched_at: '2026-05-03T11:40:46.848551'
original_url: https://github.com/openwrt/openwrt
author: openwrt
description: This repository is a mirror of https://git.openwrt.org/openwrt/openwrt.git It is for reference only and is not active for check-ins. We will continue to accept Pull Requests here. They will be merged via staging trees then into openwrt.git. - openwrt/openwrt
---

openwrt

 

/

openwrt

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork12.3k
* Star26.5k

 
 
 
 
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

68,733 Commits
68,733 Commits
.devcontainer/
ci-env
.devcontainer/
ci-env
 
 
.github
.github
 
 
.vscode
.vscode
 
 
LICENSES
LICENSES
 
 
config
config
 
 
include
include
 
 
package
package
 
 
scripts
scripts
 
 
target
target
 
 
toolchain
toolchain
 
 
tools
tools
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
BSDmakefile
BSDmakefile
 
 
COPYING
COPYING
 
 
Config.in
Config.in
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
feeds.conf.default
feeds.conf.default
 
 
rules.mk
rules.mk
 
 
View all files

## Repository files navigation

OpenWrt Project is a Linux operating system targeting embedded devices. Instead
of trying to create a single, static firmware, OpenWrt provides a fully
writable filesystem with package management. This frees you from the
application selection and configuration provided by the vendor and allows you
to customize the device through the use of packages to suit any application.
For developers, OpenWrt is the framework to build an application without having
to build a complete firmware around it; for users this means the ability for
full customization, to use the device in ways never envisioned.

Sunshine!

## Download

Built firmware images are available for many architectures and come with a
package selection to be used as WiFi home router. To quickly find a factory
image usable to migrate from a vendor stock firmware to OpenWrt, try theFirmware Selector.

* OpenWrt Firmware Selector

If your device is supported, please follow theInfolink to see install
instructions or consult the support resources listed below.

An advanced user may require additional or specific package. (Toolchain, SDK, ...) For everything else than simple firmware download, try the wiki download page:

* OpenWrt Wiki Download

## Development

To build your own firmware you need a GNU/Linux, BSD or macOS system (case
sensitive filesystem required). Cygwin is unsupported because of the lack of a
case sensitive file system.

### Requirements

You need the following tools to compile OpenWrt, the package names vary between
distributions. A complete list with distribution specific packages is found in
theBuild System Setupdocumentation.

binutils bzip2 diff find flex gawk gcc-6+ getopt grep install libc-dev libz-dev
make4.1+ perl python3.7+ rsync subversion unzip which

### Quickstart

1. Run./scripts/feeds update -ato obtain all the latest package definitions
defined in feeds.conf / feeds.conf.default
2. Run./scripts/feeds install -ato install symlinks for all obtained
packages into package/feeds/
3. Runmake menuconfigto select your preferred configuration for the
toolchain, target system & firmware packages.
4. Runmaketo build your firmware. This will download all sources, build the
cross-compile toolchain and then cross-compile the GNU/Linux kernel & all chosen
applications for your target system.

### Related Repositories

The main repository uses multiple sub-repositories to manage packages of
different categories. All packages are installed via the OpenWrt package
manager calledopkg. If you're looking to develop the web interface or port
packages to OpenWrt, please find the fitting repository below.

* LuCI Web Interface: Modern and modular
interface to control the device via a web browser.
* OpenWrt Packages: Community repository
of ported packages.
* OpenWrt Routing: Packages specifically
focused on (mesh) routing.
* OpenWrt Video: Packages specifically
focused on display servers and clients (Xorg and Wayland).

## Support Information

For a list of supported devices see theOpenWrt Hardware Database

### Documentation

* Quick Start Guide
* User Guide
* Developer Documentation
* Technical Reference

### Support Community

* Forum: For usage, projects, discussions and hardware advise.
* Support Chat: Channel#openwrtonoftc.net.

### Developer Community

* Bug Reports: Report bugs in OpenWrt
* Dev Mailing List: Send patches
* Dev Chat: Channel#openwrt-develonoftc.net.

## License

OpenWrt is licensed under GPL-2.0

## About

This repository is a mirror ofhttps://git.openwrt.org/openwrt/openwrt.gitIt is for reference only and is not active for check-ins. We will continue to accept Pull Requests here. They will be merged via staging trees then into openwrt.git.

### Resources

 Readme

 

### License

 View license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

26.5k

 stars
 

### Watchers

597

 watching
 

### Forks

12.3k

 forks
 

 Report repository

 

## Releases42

v25.12.2

 Latest

 

Mar 27, 2026

 

+ 41 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* https://openwrt.org/donate

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C66.6%
* Makefile19.9%
* Shell6.9%
* Perl2.3%
* UnrealScript1.8%
* Pascal1.0%
* Other1.5%