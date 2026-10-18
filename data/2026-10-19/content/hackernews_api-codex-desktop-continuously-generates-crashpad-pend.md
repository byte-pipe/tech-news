---
title: 'Codex Desktop continuously generates Crashpad pending dumps, growing without any limit: +5GB per day at least · Issue #25921 · openai/codex · GitHub'
url: https://github.com/openai/codex/issues/25921
site_name: hackernews_api
content_file: hackernews_api-codex-desktop-continuously-generates-crashpad-pend
fetched_at: '2026-10-19T09:16:25.964860'
original_url: https://github.com/openai/codex/issues/25921
author: AIorNot
date: '2026-10-18'
description: 'Summary Codex Desktop is continuously adding paired .dmp and _sidecar.json files under: ~/Library/Application Support/com.openai.codex/web/Crashpad/pending On my machine this directory grew to 4.9G and 54,504 files in one day. The count ...'
tags:
- hackernews
- trending
---

# Codex Desktop continuously generates Crashpad pending dumps, growing without any limit: +5GB per day at least#25921

Open
Open
Codex Desktop continuously generates Crashpad pending dumps, growing without any limit: +5GB per day at least
#25921
Labels
app
Issues related to the Codex desktop app
Issues related to the Codex desktop app
bug
Something isn't working
Something isn't working
performance

## Description

Jolg42
opened 
on Jun 2, 2026
Issue body actions

## Summary

Codex Desktop is continuously adding paired.dmpand_sidecar.jsonfiles under:

~/Library/Application Support/com.openai.codex/web/Crashpad/pending

On my machine this directory grew to4.9Gand54,504files in one day. The count continued increasing during investigation, so this appears to be active Crashpad dump generation rather than stale one-time leftovers.

The Codex Desktop app is still functional while this is happening. I can use the app, inspect the filesystem, and interact with GitHub from the same running session.

So the user-visible problem is not that Codex is fully crashing or unable to launch. The issue is that Crashpad is continuously generating pending dump/sidecar pairs in the background while the app remains usable, causing unbounded local disk growth.

I am not attaching minidumps publicly because they may contain memory, local paths, or private data. I can share the newest.dmpprivately if OpenAI maintainers provide a safe upload path.

## Environment

* Product: Codex Desktop app on macOS
* Codex app version:26.527.60818
* CFBundleVersion:3437
* Crashpad/Electron annotation observed from live process:prod=Codex_Mac,ver=148.0.7778.179
* macOS:26.3.1 (25D771280a)
* Architecture:arm64

## Observed evidence

Crashpad pending directory:

~/Library/Application Support/com.openai.codex/web/Crashpad/pending

Latest measurements:

4.9G ~/Library/Application Support/com.openai.codex/web/Crashpad/pending
54,504 files total
27,252 .dmp files
27,252 _sidecar.json files

Sampled pending file time range:

oldest sampled pending files: 2026-06-02 13:31:21 CEST
latest sampled pending files: 2026-06-02 21:08:24 CEST

During the investigation the count increased from53,444to54,064, then to54,504, which indicates the queue was still growing.

I also observed two Codexbrowser_crashpad_handlerprocesses running underPPID=1sinceSat May 30 11:47:50 2026, both using the same Crashpad database:

/Applications/Codex.app/.../Helpers/browser_crashpad_handler \
 --database=~/Library/Application Support/com.openai.codex/web/Crashpad \
 --annotation=plat=OS X \
 --annotation=prod=Codex_Mac \
 --annotation=ver=148.0.7778.179

The local app remained usable enough to inspect/report this, so the visible issue is not just a normal foreground app crash. It looks like Crashpad or a monitored helper process is repeatedly generating pending dumps without bounding, upload/processing cleanup, or rotation.

## Expected behavior

Crash reports should be bounded, uploaded/processed/rotated, or not continuously generated while the app remains usable.

## Actual behavior

Pending Crashpad reports accumulate rapidly and consume multiple GB of local disk space.

## Commands used to collect evidence

du -sh 
"
$HOME
/Library/Application Support/com.openai.codex/web/Crashpad/pending
"

find 
"
$HOME
/Library/Application Support/com.openai.codex/web/Crashpad/pending
"
 -maxdepth 1 -type f 
|
 wc -l

find 
"
$HOME
/Library/Application Support/com.openai.codex/web/Crashpad/pending
"
 -maxdepth 1 -type f \
 
|
 sed 
'
s/.*\.//
'
 
|
 sort 
|
 uniq -c 
|
 sort -nr

/usr/libexec/PlistBuddy -c 
'
Print :CFBundleShortVersionString
'
 /Applications/Codex.app/Contents/Info.plist
/usr/libexec/PlistBuddy -c 
'
Print :CFBundleVersion
'
 /Applications/Codex.app/Contents/Info.plist

sw_vers
uname -m

ps ax -o pid,ppid,lstart,command \
 
|
 grep -E 
'
browser_crashpad_handler|com.openai.codex/web/Crashpad
'
 \
 
|
 grep -v grep

## Related issues

This may be related to other Codex Desktop helper/process cleanup reports:

* Codex App update left old crashpad helper; relaunch could no-op until clean restart#25259: stale Crashpad helper after update/relaunch
* Codex App UI freezes: worker crashes, massive git/worktree errors, and concurrent orphaned app-server processes#11090: orphaned Codex processes and UI freezes
* Can't open app in Tahoe 26.2 (25C56)#10627: prior Crashpad/macOS startup reports
Reactions are currently unavailable

## Metadata

## Metadata