---
title: 'GitHub - steipete/wacli: WhatsApp CLI · GitHub'
url: https://github.com/steipete/wacli
site_name: hnrss
content_file: hnrss-github-steipetewacli-whatsapp-cli-github
fetched_at: '2026-04-16T06:00:44.204528'
original_url: https://github.com/steipete/wacli
date: '2026-04-15'
description: WhatsApp CLI. Contribute to steipete/wacli development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

steipete



/

wacli

Public

* NotificationsYou must be signed in to change notification settings
* Fork187
* Star1.4k




 
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

55 Commits
55 Commits
.github
.github
 
 
cmd/
wacli
cmd/
wacli
 
 
docs
docs
 
 
internal
internal
 
 
.gitignore
.gitignore
 
 
.goreleaser-linux-windows.yaml
.goreleaser-linux-windows.yaml
 
 
.goreleaser.yaml
.goreleaser.yaml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# 🗃️ wacli — WhatsApp CLI: sync, search, send.

WhatsApp CLI built on top ofwhatsmeow, focused on:

* Best-effort local sync of message history + continuous capture
* Fast offline search
* Sending messages
* Contact + group management

This is a third-party tool that uses the WhatsApp Web protocol viawhatsmeowand is not affiliated with WhatsApp.

## Status

Core implementation is in place. Seedocs/spec.mdfor the full design notes.

## Recent updates (0.2.0)

* Messages: search/list includes display text for reactions, replies, and media types.
* Send:wacli send file --filenameto override the display name.
* Auth: optionalWACLI_DEVICE_LABEL/WACLI_DEVICE_PLATFORMenv overrides.

## Install / Build

Chooseoneof the following options.If you install via Homebrew, you can skip the local build step.

### Option A: Install via Homebrew (tap)

* brew install steipete/tap/wacli

### Option B: Build locally

* go build -tags sqlite_fts5 -o ./dist/wacli ./cmd/wacli

Run (local build only):

* ./dist/wacli --help

## Quick start

Default store directory is~/.wacli(override with--store DIR).

#
 1) Authenticate (shows QR), then bootstrap sync

pnpm wacli auth

#
 or: ./dist/wacli auth (after pnpm build)

#
 2) Keep syncing (never shows QR; requires prior auth)

pnpm wacli sync --follow

#
 Diagnostics

pnpm wacli doctor

#
 Search messages

pnpm wacli messages search
"
meeting
"

#
 Backfill older messages for a chat (best-effort; requires your primary device online)

pnpm wacli
history
 backfill --chat 1234567890@s.whatsapp.net --requests 10 --count 50

#
 Download media for a message (after syncing)

./wacli media download --chat 1234567890@s.whatsapp.net --id
<
message-id
>

#
 Send a message

pnpm wacli send text --to 1234567890 --message
"
hello
"

#
 Send a file

./wacli send file --to 1234567890 --file ./pic.jpg --caption
"
hi
"

#
 Or override display name

./wacli send file --to 1234567890 --file /tmp/abc123 --filename report.pdf

#
 List groups and manage participants

pnpm wacli groups list
pnpm wacli groups rename --jid 123456789@g.us --name
"
New name
"

## Prior Art / Credit

This project is heavily inspired by (and learns from) the excellentwhatsapp-cliby Vicente Reig:

* whatsapp-cli

## High-level UX

* wacli auth: interactive login (shows QR code), then immediately performs initial data sync.
* wacli sync: non-interactive sync loop (never shows QR; errors if not authenticated).
* Output is human-readable by default; pass--jsonfor machine-readable output.

## Storage

Defaults to~/.wacli(override with--store DIR).

## Environment overrides

* WACLI_DEVICE_LABEL: set the linked device label (shown in WhatsApp).
* WACLI_DEVICE_PLATFORM: override the linked device platform (defaults toCHROMEif unset or invalid).

## Backfilling older history

wacli syncstores whatever WhatsApp Web sends opportunistically. To try to fetcholdermessages, use on-demand history sync requests to yourprimary device(your phone).

Important notes:

* This isbest-effort: WhatsApp may not return full history.
* Yourprimary device must be online.
* Requests areper chat(DM or group).wacliuses theoldest locally stored messagein that chat as the anchor.
* Recommended--countis50per request.

### Backfill one chat

pnpm wacli
history
 backfill --chat 1234567890@s.whatsapp.net --requests 10 --count 50

### Backfill all chats (script)

This loops through chats already known in your local DB:

pnpm -s wacli -- --json chats list --limit 100000 \

|
 jq -r
'
.[].JID
'
 \

|

while

read
 -r jid
;

do

 pnpm -s wacli --
history
 backfill --chat
"
$jid
"
 --requests 3 --count 50

done

## License

SeeLICENSE.

## Maintainers

* Created by@steipete
* Currently maintained by@dinakars777

## About

WhatsApp CLI

wacli.sh

### Topics

 go

 cli

 whatsapp

### Resources

 Readme



### License

 View license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

1.4k

 stars


### Watchers

14

 watching


### Forks

187

 forks


 Report repository



## Releases5

v0.6.0

 Latest



Apr 14, 2026



+ 4 releases

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Go100.0%
