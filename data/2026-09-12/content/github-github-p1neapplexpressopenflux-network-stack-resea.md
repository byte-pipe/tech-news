---
title: 'GitHub - p1neappleXpress/OpenFlux: Network stack research tool. TCP tunnel with pluggable transports. · GitHub'
url: https://github.com/p1neappleXpress/OpenFlux
site_name: github
content_file: github-github-p1neapplexpressopenflux-network-stack-resea
fetched_at: '2026-09-12T01:21:58.338813'
original_url: https://github.com/p1neappleXpress/OpenFlux
author: p1neappleXpress
description: Network stack research tool. TCP tunnel with pluggable transports. - p1neappleXpress/OpenFlux
---

p1neappleXpress

 

/

OpenFlux

Public

* NotificationsYou must be signed in to change notification settings
* Fork82
* Star980

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

32 Commits
32 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.idea
.idea
 
 
network
network
 
 
socks5
socks5
 
 
transport
transport
 
 
tunnel
tunnel
 
 
utils
utils
 
 
.gitignore
.gitignore
 
 
COPYRIGHT
COPYRIGHT
 
 
LICENSE
LICENSE
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
README.ru.md
README.ru.md
 
 
build_android.sh
build_android.sh
 
 
build_ios.sh
build_ios.sh
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
main.go
main.go
 
 
universal-bypass-tool
universal-bypass-tool
 
 
View all files

## Repository files navigation

# OpenFlux

English|Русский

Network stack research tool. TCP tunnel with pluggable transports.

# Disclaimer

The author of OpenFluxdoes not encouragethe use of this project to bypass restrictions or violate the rules of any platform, andis not responsiblefor the final scenarios of how users apply this tool in real life or on the Internet. Any specific technical features of the application are nothing more than anarchitectural coincidence, createdwithout any intent.

The project isentirely non-commercial, containsno paid features, hidden subscriptions, or commercial benefit.

The authoris not responsiblefor forks, modifications, or derivative versions of OpenFlux created by third parties. Any changes added to a fork are the responsibility of its author.

The authoris not responsiblefor:

* Any use of OpenFlux by third parties
* Consequences caused by the use of forks and modifications
* Damage resulting from derivative versions
* Violations committed using forks

The original code is providedas is,without any warranties.

## Overview

Client (SOCKS5) --> Transport --> Exit Node --> Internet

## Requirements

1. Golang v. 1.26.3+ - is required for building desktop client / exit node binary (universal-bypass-tool);
2. Android Native Development Kit (NDK) v.27.0.12077973+ - is required for building Android client binary;
3. XCode v. 26.6+ - is required for building iOS client binary;
4. Linux VPS / VDS exit node.

## Overview

TCP packets are sent via Transport. Currently, there are two transports available:

1. Yandex - sends packets via Yandex Docs cursor messages;
2. Max - sends packets via WebRTC DataChannel
WARNING:* Do not useyour primary or important MAX account.
* Do not usean account whose deletion or loss of access would be critical.
* Usage via anexternal VPSmay lead toaccount restrictions.
* Therestriction may persistafter stopping OpenFlux.
* MAX transport should be consideredexperimentaluntil the blocking mechanism is understood.

Client side runs a SOCKS5 proxy, exit node decapsulates and forwards packets to destination point.

## Structure

universal-bypass-tool/
├── main.go
├── transport/
│ ├── transport.go # Transport interface
│ └── yandex/ # Yandex Docs backend
│ └── oneme/ # MAX Messenger backend
├── tunnel/
│ ├── tunnel.go # TCP tunnel core
│ ├── endpoint.go # Virtual NIC
│ └── rawsocket.go # Raw socket (exit node)
├── socks5/ # SOCKS5 server
├── network/ # Checksums, packet parsing
└── utils/ # Debug logging

## Build (desktop client / exit-node binary)

go mod tidy
go build -o universal-bypass-tool 
.

## Build for Android (client binary)

export
 ANDROID_NDK_HOME=
<
your Android NDK path
>

./build_android.sh

## Build for iOS (client binary)

export
 XCODE_PATH=
"
<your Xcode.app path>
"
 
#
 optional, defaults to /Applications/Xcode.app

./build_ios.sh

## Usage

### 1. Setting up exit node

1. You must have root access on exit node machine;
2. Only legacy Yandex document editor is supported (you can toggle this setting from the interface).

Setup commands for exit node:

sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
sudo ./universal-bypass-tool --exit-node --url 
"
YOUR_YANDEX_DOC_URL
"
 --debug

### 1. Setting up desktop client:

Setup commands for desktop client:

./universal-bypass-tool --client --url 
"
YOUR_YANDEX_DOC_URL
"
 --socks5 :1080 --debug

Then set up SOCKS5 proxy in your browser at localhost:1080.

## Flags

Flag

Default

Description

--client

Run as client

--exit-node

Run as exit node

--socks5

:1080

SOCKS5 listen address

--url

https://localhost

Document URL (Yandex Docs)

--maxToken

``

Auth token (Max)

--maxUid

``

User ID (Max)

--debug

false

Enable verbose logging

--transport

yandex

Select transport backend

## Implementing custom transports

You are free to implement theTransportinterface fromtransport/transport.goand register your custom transport in main.go switch block.

## License

This project is licensed under theGNU General Public License v3.0 or later.
SeeLICENSEfor the full text.

Third-party licenses are listed inNOTICE.

## Disclaimer

Educational use only. Test on your own machines and networks.