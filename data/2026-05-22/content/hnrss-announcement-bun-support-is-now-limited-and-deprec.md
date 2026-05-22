---
title: '[Announcement] Bun support is now limited and deprecated · Issue #16766 · yt-dlp/yt-dlp · GitHub'
url: https://github.com/yt-dlp/yt-dlp/issues/16766
site_name: hnrss
content_file: hnrss-announcement-bun-support-is-now-limited-and-deprec
fetched_at: '2026-05-22T19:34:59.781817'
original_url: https://github.com/yt-dlp/yt-dlp/issues/16766
date: '2026-05-22'
description: Due to foreseeable compatibility and security issues, yt-dlp's support for Bun as an ejs-compatible JavaScript runtime is being both limited and deprecated. As of the next yt-dlp and/or ejs release, only Bun versions 1.2.11 through 1.3.1...
tags:
- hackernews
- hnrss
---

yt-dlp

 

/

yt-dlp

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork13.8k
* Star164k

# [Announcement] Bun support is now limited and deprecated#16766

Open
Open
[Announcement] Bun support is now limited and deprecated
#16766
Labels
discussion/announcement
ejs/jsc
Related to the JS Challenge framework and/or EJS library
Related to the JS Challenge framework and/or EJS library

## Description

bashonly
opened 
on 
May 20, 2026
Issue body actions

Due to foreseeable compatibility and security issues, yt-dlp's support for Bun as anejs-compatible JavaScript runtime is being both limited and deprecated.

As of the next yt-dlp and/or ejs release, only Bun versions1.2.11through1.3.14will be supported. The rationale for this change is twofold:

1. The minimum required version is being raised from1.0.31to1.2.11because building theejspackage with a version earlier than1.2.0results in the ejs lockfile being ignored, which is a significant security concern for users when considering all of the recent npm supply chain attacks. Additionally, the support floor is being bumped to1.2.11instead of1.2.0because theejstest suite cannot be run with versions of Bun earlier than1.2.11.
2. Bun was recently rewritten in Rust using Claude, and its development seems to have taken a turn towards being fully vibe-coded. This is alarming and disappointing for a number of reasons, and frankly it seems like a future headache that we'd prefer to avoid. We are adding a support ceiling of version1.3.14, as that is the last release built from the original zig codebase.

Bun support will also be deprecated. This means that while yt-dlp will continue to support this narrower range of Bun versions for as long as they're able to meet the needs of yt-dlp and ejs, we reserve the right to completely drop support for Bun should it at any point become too burdensome to maintain.

Seethe EJS wiki articlefor more information about supported JavaScript runtimes, but note that it has not yet been updated to reflect the changes announced in this post.

Reactions are currently unavailable
Pinned by
 
bashonly
Pinned comment options
bashonly
on 
May 22, 2026

Before commenting, please ask yourself: Do I actually care about using bun with yt-dlp? Or am I here because I followed a link on hackernews and I love posting?

View full comment 

## Metadata

## Metadata