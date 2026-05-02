---
title: 'NetHack 5.0.0: Release Notes'
url: https://nethack.org/v500/release.html
site_name: hackernews_api
content_file: hackernews_api-nethack-500-release-notes
fetched_at: '2026-05-02T19:55:14.485213'
original_url: https://nethack.org/v500/release.html
author: rsaarelm
date: '2026-05-02'
description: NetHack 5.0.0
tags:
- hackernews
- trending
---

## The NetHack DevTeam is announcing the release of NetHack 5.0.0 on
May 2, 2026

NetHack 5.0 is an enhancement to the dungeon exploration game NetHack,
which is a distant descendent of Rogue and Hack, and a direct descendent
of NetHack 3.6.NetHack 5.0.0 is a release of NetHack. As a .0 version, there may be some
bugs encountered. Constructive suggestions, GitHub pull requests, and bug
reports are all welcome and encouraged.Along with the game improvements and bug fixes, NetHack 5.0 strives to make
some general architectural improvements to the game or to its building
process. Among them, 5.0:Has its source code compliant with the C99 standard.Removes barriers to building NetHack on one platform and operating system,
 for later execution on another (possibly quite different) platform and/or
 operating system. That capability is generally known as "cross-compiling."
 See the file "Cross-compiling" in the top-level folder for more information
 on that.The build-time "yacc and lex"-based level compiler, the
 "yacc and lex"-based dungeon compiler, and the quest text file processing
 previously done by NetHack's "makedefs" utility, have been replaced with
 Lua text alternatives that are loaded and processed by the game during play.A list of over 3100 fixes and changes can be found in the game's sources
in the file doc/fixes5-0-0.txt. The text in there was written for the
development team's own use and is provided "as is". Some entries might be
considered "spoilers", particularly in the "new features" section.Existing saved games and bones files will not work with NetHack 5.0.0.Checksums (sha256) of binaries that you have downloaded from nethack.org
can be verified on Windows platforms using:certUtil -hashfile nethack-500-win-x64.zip SHA256orcertUtil -hashfile nethack-500-win-arm64.zip SHA256The following command can be used on most platforms to help confirm the location of
various files that NetHack may use:nethack --showpathsAs with all releases of the game, we appreciate your feedback. Please submit any
bugs using the problem report form. Also, please check the "known bugs" list
before you log a problem - somebody else may have already found it.Happy NetHacking!