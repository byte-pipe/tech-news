---
title: 'GitHub - permissionlesstech/bitchat: bluetooth mesh chat, IRC vibes · GitHub'
url: https://github.com/permissionlesstech/bitchat
site_name: github
content_file: github-github-permissionlesstechbitchat-bluetooth-mesh-ch
fetched_at: '2026-07-25T11:28:19.077884'
original_url: https://github.com/permissionlesstech/bitchat
author: permissionlesstech
description: bluetooth mesh chat, IRC vibes. Contribute to permissionlesstech/bitchat development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 permissionlesstech

 

/

bitchat

Public

* NotificationsYou must be signed in to change notification settings
* Fork3.9k
* Star28k

 
 
 
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

982 Commits
982 Commits
.github/
workflows
.github/
workflows
 
 
Configs
Configs
 
 
bitchat.xcodeproj
bitchat.xcodeproj
 
 
bitchat
bitchat
 
 
bitchatShareExtension
bitchatShareExtension
 
 
bitchatTests
bitchatTests
 
 
docs
docs
 
 
localPackages
localPackages
 
 
relays
relays
 
 
scripts
scripts
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.periphery.baseline.json
.periphery.baseline.json
 
 
.periphery.yml
.periphery.yml
 
 
.swiftlint.yml
.swiftlint.yml
 
 
BRING_THE_NOISE.md
BRING_THE_NOISE.md
 
 
Justfile
Justfile
 
 
LICENSE
LICENSE
 
 
PRIVACY_POLICY.md
PRIVACY_POLICY.md
 
 
Package.resolved
Package.resolved
 
 
Package.swift
Package.swift
 
 
README.md
README.md
 
 
WHITEPAPER.md
WHITEPAPER.md
 
 
View all files

## Repository files navigation

## bitchat

A decentralized peer-to-peer messaging app with dual transport architecture: local Bluetooth mesh networks for offline communication and internet-based Nostr protocol for global reach. No accounts, no phone numbers, no central servers. It's the side-groupchat.

bitchat.free

📲App Store

## License

This project is released into the public domain. See theLICENSEfile for details.

## Features

* Dual Transport Architecture: Bluetooth mesh for offline + Nostr protocol for internet-based messaging
* Location-Based Channels: Geographic chat rooms using geohash coordinates over global Nostr relays
* Intelligent Message Routing: Automatically chooses best transport (Bluetooth → Nostr fallback)
* Decentralized Mesh Network: Automatic peer discovery and multi-hop message relay over Bluetooth LE
* Privacy First: No accounts, no phone numbers, no persistent identifiers
* Private Message End-to-End Encryption:Noise Protocolfor mesh, NIP-17 for Nostr
* IRC-Style Commands: Familiar/slap,/msg,/whostyle interface
* Universal App: Native support for iOS and macOS
* Emergency Wipe: Triple-tap to instantly clear all data
* Performance Optimizations: LZ4 message compression, adaptive battery modes, and optimized networking

## Technical Architecture

BitChat uses ahybrid messaging architecturewith two complementary transport layers:

### Bluetooth Mesh Network (Offline)

* Local Communication: Direct peer-to-peer within Bluetooth range
* Multi-hop Relay: Messages route through nearby devices (max 7 hops)
* No Internet Required: Works completely offline in disaster scenarios
* Noise Protocol Encryption: End-to-end encryption with forward secrecy
* Binary Protocol: Compact packet format optimized for Bluetooth LE constraints
* Automatic Discovery: Peer discovery and connection management
* Adaptive Power: Battery-optimized duty cycling

### Nostr Protocol (Internet)

* Global Reach: Connect with users worldwide via internet relays
* Location Channels: Geographic chat rooms using geohash coordinates
* 290+ Relay Network: Distributed across the globe for reliability
* NIP-17 Encryption: Gift-wrapped private messages for internet privacy
* Ephemeral Keys: Fresh cryptographic identity per geohash area

### Channel Types

#### mesh #bluetooth

* Transport: Bluetooth Low Energy mesh network
* Scope: Local devices within multi-hop range
* Internet: Not required
* Use Case: Offline communication, protests, disasters, remote areas

#### Location Channels (block #dr5rsj7,neighborhood #dr5rs,country #dr)

* Transport: Nostr protocol over internet
* Scope: Geographic areas defined by geohash precisionblock(7 chars): City block levelneighborhood(6 chars): District/neighborhoodcity(5 chars): City levelprovince(4 chars): State/provinceregion(2 chars): Country/large region
* block(7 chars): City block level
* neighborhood(6 chars): District/neighborhood
* city(5 chars): City level
* province(4 chars): State/province
* region(2 chars): Country/large region
* Internet: Required (connects to Nostr relays)
* Use Case: Location-based community chat, local events, regional discussions

### Direct Message Routing

Private messages useintelligent transport selection:

1. Bluetooth First(preferred when available)* Direct connection with established Noise session
* Fastest and most private option
2. Nostr Fallback(when Bluetooth unavailable)* Uses recipient's Nostr public key
* NIP-17 gift-wrapping for privacy
* Routes through global relay network
3. Smart Queuing(when neither available)* Messages queued until transport becomes available
* Automatic delivery when connection established

For detailed protocol documentation, see theTechnical Whitepaper.

## Setup

### Option 1: Using Xcode

cd
 bitchat
open bitchat.xcodeproj

To run on a device there're a few steps to prepare the code:

* Clone the local configs:cp Configs/Local.xcconfig.example Configs/Local.xcconfig
* Add your Developer Team ID into the newly createdConfigs/Local.xcconfigBundle ID would be set tochat.bitchat.<team_id>(unless you set to something else)
* Bundle ID would be set tochat.bitchat.<team_id>(unless you set to something else)
* Entitlements need to be updated manually (TODO: Automate):Search and replacegroup.chat.bitchatwithgroup.<your_bundle_id>(e.g.group.chat.bitchat.ABC123)
* Search and replacegroup.chat.bitchatwithgroup.<your_bundle_id>(e.g.group.chat.bitchat.ABC123)

### Option 2: Usingjust

brew install just

Want to try this on macos:just runwill set it up and run from source.
Runjust cleanafterwards to restore things to original state for mobile app building and development.

## Localization

* Base app resources live underbitchat/Localization/Base.lproj/. Add new copy toLocalizable.stringsand plural rules toLocalizable.stringsdict.
* Share extension strings are separate inbitchatShareExtension/Localization/Base.lproj/Localizable.strings.
* Prefer keys that describe intent (app_info.features.offline.title) and reuse existing ones where possible.
* Runxcodebuild -project bitchat.xcodeproj -scheme "bitchat (macOS)" -configuration Debug CODE_SIGNING_ALLOWED=NO buildto compile-check any localization updates.