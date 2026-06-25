---
title: 'GitHub - IceWhaleTech/CasaOS: CasaOS - A simple, easy-to-use, elegant open-source Personal Cloud system. · GitHub'
url: https://github.com/IceWhaleTech/CasaOS
site_name: github
content_file: github-github-icewhaletechcasaos-casaos-a-simple-easy-to
fetched_at: '2026-06-25T11:56:00.792193'
original_url: https://github.com/IceWhaleTech/CasaOS
author: IceWhaleTech
description: CasaOS - A simple, easy-to-use, elegant open-source Personal Cloud system. - IceWhaleTech/CasaOS
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 IceWhaleTech

 

/

CasaOS

Public

* NotificationsYou must be signed in to change notification settings
* Fork2k
* Star34.5k

 
 
 
 
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

688 Commits
688 Commits
.github
.github
 
 
api
api
 
 
build
build
 
 
cmd
cmd
 
 
common
common
 
 
conf
conf
 
 
drivers
drivers
 
 
interfaces
interfaces
 
 
internal
internal
 
 
model
model
 
 
pkg
pkg
 
 
route
route
 
 
service
service
 
 
types
types
 
 
.all-contributorsrc
.all-contributorsrc
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.goreleaser.debug.yaml
.goreleaser.debug.yaml
 
 
.goreleaser.yaml
.goreleaser.yaml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
DEVELOPING.md
DEVELOPING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
main.go
main.go
 
 
package.json
package.json
 
 
snapshot-dark.jpg
snapshot-dark.jpg
 
 
snapshot-light.jpg
snapshot-light.jpg
 
 
snapshot-mobile.png
snapshot-mobile.png
 
 
snapshot.png
snapshot.png
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# CasaOS - Your Personal Cloud

Connect with the community, establish autonomy, reduce the cost of SaaS, and MAXIMIZE the potential for a personalized copilot.Website|Demo|GitHub

## Why do you need Personal Cloud?

In 2020, the team noticed three important trends:

* The cost of computing power and storage was decreasing fast.
* A part of cloud computing was moving towards edge computing.
* The issue of consumer data asset ownership and attribution had been ignored.

Based on these trends, the team proposed a thought experiment internally: what if personal clouds were available under $100 in next five years? This personal cloud would provide a low-cost data collaboration solution as a personal data center, storing and managing data for creators and small organizations. A distributed collaborative computing network can be formed by personal servers located around the world. It could also control and connect all smart devices, providing cross-ecosystem local intelligent services.

Furthermore, the personal cloud could combine personal data to train personalized AI assistants. The idea is that this technology would be an effective way to solve the issue of consumer data asset ownership and , as well as provide a more affordable and efficient computing solution for individuals and small organizations.

If you think what we are doing is valuable. Pleasegive us a star ⭐andfork it 🤞!

## Features

* Friendly UI designed for home scenariosNo code, no forms, intuitive, design for humanity
* No code, no forms, intuitive, design for humanity
* Multiple hardware and base system supportZimaBoard, NUC, RPi, old computers, whatever is available.
* ZimaBoard, NUC, RPi, old computers, whatever is available.
* Selected apps in the app store, one-click installationNextcloud, HomeAssistant, AdGuard, Jellyfin, *arr and more!
* Nextcloud, HomeAssistant, AdGuard, Jellyfin, *arr and more!
* Easily install numerous Docker appsOver 100,000 apps from the Docker ecosystem can be easily installed
* Over 100,000 apps from the Docker ecosystem can be easily installed
* Elegant drive and file managementWhat you see is what you get. No technical background required.
* What you see is what you get. No technical background required.
* Well-designed system/app widgetsWhat you care about, at a glance. Resource usage, app status, and more!
* What you care about, at a glance. Resource usage, app status, and more!

## Getting Started

CasaOS fully supports ZimaBoard, Intel NUC, and Raspberry Pi. Also, more computers and development boards and fully compatible with Ubuntu, Debian, Raspberry Pi OS, and CentOS with one-liner installation.

### Hardware Compatibility

* amd64 / x86-64
* arm64
* armv7

### System Compatibility

Official Support

* Debian 12 (✅ Tested, Recommended)
* Ubuntu Server 20.04 (✅ Tested)
* Raspberry Pi OS (✅ Tested)

Community Support

* Elementary 6.1 (✅ Tested)
* Armbian 22.04 (✅ Tested)
* Alpine (🚧 Not Fully Tested Yet)
* OpenWrt (🚧 Not Fully Tested Yet)
* ArchLinux (🚧 Not Fully Tested Yet)

### Quick Setup CasaOS

Freshly install a system from the list above and run this command:

wget -qO- https://get.casaos.io 
|
 sudo bash

or

curl -fsSL https://get.casaos.io 
|
 sudo bash

### Update CasaOS

CasaOS can be updated from the User Interface (UI), viaSettings ... Update.

Alternatively it can be updated from a terminal session. To update from a terminal session, it must be done either from a secure shell (ssh) session to the device or from a directly attached terminal and keyboard to the device running CasaOS, this cannot be done from the terminal via the CasaOS User Interface (UI). To update to the latest release of CasaOS from a terminal session run this command:

wget -qO- https://get.casaos.io/update 
|
 sudo bash

or

curl -fsSL https://get.casaos.io/update 
|
 sudo bash

To determine version of CasaOS from a terminal session run this command:

casaos -v

### Uninstall CasaOS

v0.3.3 or newer

casaos-uninstall

Before v0.3.3

curl -fsSL https://get.icewhale.io/casaos-uninstall.sh 
|
 sudo bash

## Community

The word Casa comes from the Spanish word for "home". Project CasaOS originated as a pre-installed system for the crowdfunded productZimaBoardon Kickstarter.

After looking at many systems and software on the market, the team found no server system designed for home scenarios, sadly true.

So, we set out to build this open-source project to develop CasaOS with our own hands, everyone in the community, and you.

We believe that through community-driven collaborative innovation and open communication with global developers, we can reshape the digital home experience like never before.

A warm welcome for you to get help or share great ideas in theDiscord!

## Contributing

CasaOS is a community-driven open source project and the people involved are CasaOS users. That means CasaOS will always need contributions from community members just like you!

* Seehttps://wiki.casaos.io/en/contributefor ways of contributing to CasaOS
* Seehttps://wiki.casaos.io/en/contribute/developmentif you want to be involved in code contribution specifically

## Credits

Many thanks to everyone who has helped CasaOS so far!

Everyone's contribution is greatly appreciated. (Emoji Key)

老竭力
💻
 
📖
 
🤔
 
🚇
 
🚧
 
📦
 
💬
 
👀

link
💻
 
📖
 
🤔
 
🚇
 
🚧
 
💬
 
👀

太戈
💻
 
📖
 
🤔
 
🚇
 
🚧
 
🧑‍🏫
 
🛡️
 
💬
 
👀

Lauren
🤔
 
🔍
 
📆
 
💬
 
⚠️

John Guan
📝
 
🖋
 
📖
 
🤔
 
📋
 
🧑‍🏫
 
💬
 
👀

David Tippett
📖
 
🤔
 
💬

Skaya
🧑‍🏫
 
💬
 
✅
 
🌍

AuthorShin
⚠️
 
🐛
 
💬
 
🤔

baptiste313
🌍

DrMxrcy
⚠️
 
🤔
 
💬

Joooost
🤔

Vitaly Potyarkin
🤔

Bjørn Friese
🤔

Protektor
🐛
 
🤔
 
💬

llwaini
📆
 
⚠️
 
✅

CorrectRoadH
💻
 
📖

zhanghengxin
💻
 
📖

This project follows theall-contributorsspecification. Contributions of any kind are welcome!

## Changelog

Detailed changes for each release are documented in therelease notes.

## About

CasaOS - A simple, easy-to-use, elegant open-source Personal Cloud system.

casaos.zimaspace.com

### Topics

 docker

 golang

 home-automation

 iot

 vuejs

 self-hosted

 raspberry

 home-server

 home-cloud

 casaos

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

34.5k

 stars
 

### Watchers

203

 watching
 

### Forks

2k

 forks
 

 Report repository

 

## Releases97

v0.4.15

 Latest

 

Dec 19, 2024

 

+ 96 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go90.3%
* Shell9.4%
* Other0.3%