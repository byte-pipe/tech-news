---
title: 'GitHub - resumex/doom-over-dns: Play Doom entirely from DNS records. (PowerShell 7+) · GitHub'
url: https://github.com/resumex/doom-over-dns
site_name: hnrss
content_file: hnrss-github-resumexdoom-over-dns-play-doom-entirely-fro
fetched_at: '2026-03-27T11:20:16.002717'
original_url: https://github.com/resumex/doom-over-dns
date: '2026-03-23'
description: Play Doom entirely from DNS records. (PowerShell 7+) - resumex/doom-over-dns
tags:
- hackernews
- hnrss
---

resumex



/

doom-over-dns

Public

* NotificationsYou must be signed in to change notification settings
* Fork16
* Star395




 
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

1 Commit
1 Commit
TXTRecords
TXTRecords
 
 
managed-doom
managed-doom
 
 
.gitignore
.gitignore
 
 
Publish-DoomOverDNS.ps1
Publish-DoomOverDNS.ps1
 
 
README.md
README.md
 
 
Start-DoomOverDNS.ps1
Start-DoomOverDNS.ps1
 
 
demo.svg
demo.svg
 
 
View all files

## Repository files navigation

# DOOM Over DNS

At some point, a reasonable person asked "DNS resolves names to IP addresses, what else can it do?" The answer, apparently, is run DOOM.

DNS TXT records can hold arbitrary text. Cloudflare will serve them globally, for free, cached at the edge, to anyone who asks. They are not a file storage system. They were not designed to be a file storage system. Nobody at the IETF was thinking about them being used as a file storage system when they wrote RFC 1035. And yet here we are.

This project compresses the entirety of shareware DOOM, splits it into ~1,964 DNS TXT records across a single Cloudflare zone, and plays it back at runtime using nothing but a PowerShell script and public DNS queries. The WAD file never touches disk and the .NET game engine DLLs are loaded directly into memory.

It was always DNS.

# Quick Start

## Play

#
 1. Install PowerShell 7 (if you don't have it)

winget install Microsoft.PowerShell

#
 2. Play DOOM

.
\Start-DoomOverDNS.ps1

-
PrimaryZone
'
example.com
'

That's it. Everything else is fetched from DNS automatically usingResolve-DNSName.

## Upload

#
 1. Build the game engine

cd managed
-
doom
dotnet publish ManagedDoom
/
ManagedDoom.csproj
-
c Release
-f
 net8.
0

-
o
publish-out

#
 2. Load Cloudflare credentials

Import-Module
 .\TXTRecords\TXTRecords.psm1

Set-CFCredential

-
ApiToken (
Read-Host

'
API Token
'

-
AsSecureString)

#
 3. Upload to DNS

.
\Publish-DoomOverDNS.ps1

`


-
PublishDir
'
managed-doom\publish-out
'

`


-
WadPath
'
DOOM1.WAD
'

`


-
Zones
@
(
'
example.com
'
)

# Details

## Start-DoomOverDNS.ps1

Parameter

Default

Description

-PrimaryZone

(required)

DNS zone where
stripe-meta
 records live

-DnsServer

(system default)

Specific DNS resolver IP (e.g.
'1.1.1.1'
)

-WadName

'doom1'

WAD type:
doom1
,
doom
,
doom2
,
plutonia
,
tnt

-DoomArgs

''

Arguments forwarded to the engine (e.g.
'-warp 1 3 -skill 5'
)

-WadPrefix

'doom-wad'

DNS prefix for the WAD stripe

-LibsPrefix

'doom-libs'

DNS prefix for the DLL bundle stripe

Use-DnsServer '1.1.1.1'if records haven't propagated to your local resolver yet.

## Publish-DoomOverDNS.ps1

Parameter

Default

Description

-PublishDir

(required)

Path to
dotnet publish
 output directory

-WadPath

(required)

Path to the WAD file

-Zones

(required)

Ordered array of Cloudflare DNS zone names

-WadPrefix

'doom-wad'

DNS prefix for the WAD stripe

-LibsPrefix

'doom-libs'

DNS prefix for the DLL bundle stripe

-Force

$false

Skip confirmation prompts when overwriting

Uploading requires a Cloudflare API token withEdit zone DNSpermissions. Load it withSet-CFCredentialfrom theTXTRecordsmodule (see Quick Start above).

## Multi-zone striping

A Free zone holds 185 data chunks; Pro/Business/Enterprise hold 3,400. The WAD alone needs ~1,199 chunks, so Free-tier users need multiple domains. Pass them as an array to-Zonesand the module distributes chunks automatically. A single Pro zone fits everything.

## Resuming interrupted uploads

If an upload is interrupted,Publish-TXTStripesupports-Resume— it verifies the hash, finds the last good chunk, and picks up where it left off.

## managed-doom patches

Upstreammanaged-doomuses Native AOT, which can't be loaded viaAssembly.Load(). This fork converts it to a framework-dependent .NET 8 assembly with stream-based WAD loading and Win32 P/Invoke for windowing (no GLFW, no audio — uses built-inNullSound/NullMusicstubs).

## Components

managed-doom|Silk.NET|TrippyGL| DOOM1.WAD (id Software) |Cloudflare DNS API

## About

Play Doom entirely from DNS records. (PowerShell 7+)

### Resources

 Readme



### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

395

 stars


### Watchers

2

 watching


### Forks

16

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* C#93.8%
* PowerShell6.2%
