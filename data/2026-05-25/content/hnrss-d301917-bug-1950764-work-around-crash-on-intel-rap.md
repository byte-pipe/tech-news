---
title: ⚙ D301917 Bug 1950764 - Work around crash on Intel Raptor Lake CPU.
url: https://phabricator.services.mozilla.com/D301917
site_name: hnrss
content_file: hnrss-d301917-bug-1950764-work-around-crash-on-intel-rap
fetched_at: '2026-05-25T19:34:54.763570'
original_url: https://phabricator.services.mozilla.com/D301917
date: '2026-05-22'
description: 'Bug 1950764: Work Around Crash on Intel Raptor Lake CPU'
tags:
- hackernews
- hnrss
---

Paths
* Table of Contentst
* Hide Panelf
* Keyboard Reference?
 Differential
 
 D301917
 

# Bug 1950764- Work around crash on Intel Raptor Lake CPU.Needs ReviewPublic

Authored by 
glandium
 on Thu, May 21, 9:16 PM.
* Edit Revision
* Update Diff
* Download Raw Diff
* Edit Parent Revisions
* Edit Child Revisions
* Edit Commits
* View Stack in Lando
* New Changes
* Subscribe
* Mute Notifications
* Flag For Later
Tags
None
Referenced Files
F71292195: D301917.1779822348.diff
Mon, May 25, 7:05 PM
2026-05-25 19:05:48 (UTC+0)
F71290126: D301917.1779820729.diff
Mon, May 25, 6:38 PM
2026-05-25 18:38:49 (UTC+0)
F71289376: D301917.1779820162.diff
Mon, May 25, 6:29 PM
2026-05-25 18:29:22 (UTC+0)
F71289196: D301917.1779820045.diff
Mon, May 25, 6:27 PM
2026-05-25 18:27:25 (UTC+0)
F71287225: D301917.1779818658.diff
Mon, May 25, 6:04 PM
2026-05-25 18:04:18 (UTC+0)
F71284846: D301917.1779817333.diff
Mon, May 25, 5:42 PM
2026-05-25 17:42:13 (UTC+0)
F71281125: D301917.1779814301.diff
Mon, May 25, 4:51 PM
2026-05-25 16:51:41 (UTC+0)
F71280929: D301917.1779814117.diff
Mon, May 25, 4:48 PM
2026-05-25 16:48:37 (UTC+0)
View All 90 Files
Subscribers
tnikkel

# Details

Reviewers 
gsvelto
 
Bugzilla Bug ID 
1950764
 

# Diff Detail

Repository 
rFIREFOXAUTOLAND firefox-autoland
 
Branch 
HEAD 

### Event Timeline

glandium
 created this revision.
Thu, May 21, 9:16 PM
2026-05-21 21:16:43 (UTC+0)
Herald
 added a project: 
secure-revision
. 
 · 
View Herald Transcript
Thu, May 21, 9:16 PM
2026-05-21 21:16:43 (UTC+0)
phab-bot
 published this revision for review.
Thu, May 21, 9:16 PM
2026-05-21 21:16:51 (UTC+0)
phab-bot
 changed the visibility from "
Custom Policy
" to "Public (No Login Required)".
phab-bot
 changed the edit policy from "
Custom Policy
" to "Restricted Project (Project)".
phab-bot
 removed a project: 
secure-revision
.
tnikkel
 added a subscriber: 
tnikkel
.
Thu, May 21, 9:26 PM
2026-05-21 21:26:57 (UTC+0)
Harbormaster
 completed remote builds in 
B972906: Diff 1280481
.
Thu, May 21, 9:46 PM
2026-05-21 21:46:07 (UTC+0)

# Revision ContentsChangeset List

* Files
* History
* Commits
* Similar
Path
Size
Cargo.lock
Cargo.toml
3 lines
third_party/
rust/
zlib-rs/
src/
deflate/
sym_buf.rs
13 lines
Diff
ID
Base
Description
Created
Lint
Unit
Base
Base
Diff 1
1280481
Thu, May 21, 9:16 PM
Show Diff
Commit
Tree
Parents
Author
Summary
Date
d78364d7772d
3327175aa99b
de92ee2e55a6
Mike Hommey
Bug 1950764 - Work around crash on Intel Raptor Lake CPU. r?gsvelto
Thu, May 21, 9:16 PM
* D275987Bug 1710940 - WIP Fix minidump-writer in isolated processes·Reviewers:gsveltoMon, May 25, 7:10 PM2026-05-25 19:10:00 (UTC+0)Author:cmartin
* ·Reviewers:gsvelto
* Mon, May 25, 7:10 PM2026-05-25 19:10:00 (UTC+0)
* D302385Bug 1710940 - Part 1: Redirect process inspection·Reviewers:Restricted Project,glandium,gsveltoMon, May 25, 7:09 PM2026-05-25 19:09:00 (UTC+0)Author:cmartin
* ·Reviewers:Restricted Project,glandium,gsvelto
* Mon, May 25, 7:09 PM2026-05-25 19:09:00 (UTC+0)
* D299690Bug 1892964 - Add FIDO2 / CTAP2 hmac-secret KEK tier to Lockstore r=simonf·Reviewers:simonfSat, May 23, 12:41 PM2026-05-23 12:41:53 (UTC+0)Author:bbeurdouche
* ·Reviewers:simonf
* Sat, May 23, 12:41 PM2026-05-23 12:41:53 (UTC+0)
* D293658Bug 2031063 - Persist TLS 0-RTT tokens for DoH/TRR server in pref for early startup. r=valentin,keeler,emz,#necko-reviewers·Reviewers:valentin,keeler,necko-reviewersFri, May 22, 12:19 PM2026-05-22 12:19:32 (UTC+0)Author:leggert
* ·Reviewers:valentin,keeler,necko-reviewers
* Fri, May 22, 12:19 PM2026-05-22 12:19:32 (UTC+0)
* D301760Bug 1894742 - Populate the InstallTime annotation without using InstallTime files·Reviewers:afranchukFri, May 22, 9:49 AM2026-05-22 09:49:00 (UTC+0)Author:gsvelto
* ·Reviewers:afranchuk
* Fri, May 22, 9:49 AM2026-05-22 09:49:00 (UTC+0)
* D301889Bug 1938333 - Update Rust crate dependencies for geckodriver 0.37.0.·Reviewers:geckodriver-reviewers,Sasha,jgrahamFri, May 22, 9:13 AM2026-05-22 09:13:57 (UTC+0)Author:whimboo
* ·Reviewers:geckodriver-reviewers,Sasha,jgraham
* Fri, May 22, 9:13 AM2026-05-22 09:13:57 (UTC+0)
* D297044Bug 1985968 - linux: record the signal emitter in a crash annotation r=gsvelto·Reviewers:gsveltoFri, May 22, 9:05 AM2026-05-22 09:05:55 (UTC+0)Author:schopin
* ·Reviewers:gsvelto
* Fri, May 22, 9:05 AM2026-05-22 09:05:55 (UTC+0)
* D299708Bug 1985968 - Wire up an extra payload when initiating crash generation r=gsvelto·Reviewers:gsveltoFri, May 22, 8:52 AM2026-05-22 08:52:21 (UTC+0)Author:schopin
* ·Reviewers:gsvelto
* Fri, May 22, 8:52 AM2026-05-22 08:52:21 (UTC+0)
* D299707Bug 1985968 - Move the Rust generated annotation enum into a common crate r=gsvelto·Reviewers:gsveltoFri, May 22, 8:46 AM2026-05-22 08:46:06 (UTC+0)Author:schopin
* ·Reviewers:gsvelto
* Fri, May 22, 8:46 AM2026-05-22 08:46:06 (UTC+0)

# Diff 1280481

View Options

# Cargo.lock

Loading...
View Options

# Cargo.toml

Loading...
View Options

# third_party/rust/zlib-rs/src/deflate/sym_buf.rs

Loading...
Log In to Comment
Privacy
 · 
Cookies
 · 
Legal