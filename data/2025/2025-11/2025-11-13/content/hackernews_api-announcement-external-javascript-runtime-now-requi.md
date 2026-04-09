---
title: '[Announcement] External JavaScript runtime now required for full YouTube support · Issue #15012 · yt-dlp/yt-dlp · GitHub'
url: https://github.com/yt-dlp/yt-dlp/issues/15012
site_name: hackernews_api
fetched_at: '2025-11-13T11:07:30.590553'
original_url: https://github.com/yt-dlp/yt-dlp/issues/15012
author: bertman
date: '2025-11-12'
description: 'This is a follow-up to #14404, which announced that yt-dlp will soon require an external JavaScript runtime (e.g. Deno) in order to fully support downloading from YouTube. With the release of yt-dlp version 2025.11.12, external JavaScrip...'
tags:
- hackernews
- trending
---

yt-dlp



/

yt-dlp

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork10.8k
* Star135k

# [Announcement] External JavaScript runtime now required for full YouTube support#15012

Open
Open
[Announcement] External JavaScript runtime now required for full YouTube support
#15012
Labels
discussion/announcement

## Description

bashonly
opened
on
Nov 12, 2025
Issue body actions

This is a follow-up to#14404, which announced that yt-dlp willsoonrequire an external JavaScript runtime (e.g. Deno) in order to fully support downloading from YouTube.

### With the release ofyt-dlp version2025.11.12, external JavaScript runtime support has arrived.

### All users who intend to use yt-dlp with YouTube are strongly encouraged to install one of the supported JS runtimes.

The following JavaScript runtimes are currently supported (in order of recommendation, from strongest to weakest):

1. ### Deno* recommended for most users
* https://deno.com/
* https://github.com/denoland/denonote:if downloading fromDeno's GitHub releases, getdenonotdenort
* note:if downloading fromDeno's GitHub releases, getdenonotdenort
* minimum Deno version supported by yt-dlp:2.0.0the latest version of Deno is strongly recommended
* the latest version of Deno is strongly recommended
2. ### Node* https://nodejs.org/
* minimum Node version supported by yt-dlp:20.0.0if using Node, the latest version (25+) is strongly recommended for security reasons
* if using Node, the latest version (25+) is strongly recommended for security reasons
3. ### QuickJS* https://bellard.org/quickjs/
* minimum QuickJS version supported by yt-dlp:2023-12-9if using QuickJS, version2025-4-26or later is strongly recommended for performance reasons
* if using QuickJS, version2025-4-26or later is strongly recommended for performance reasons
4. ### QuickJS-ng* https://quickjs-ng.github.io/quickjs/
* all versions are supported by yt-dlp; however,upstream QuickJSis recommended insteadfor performance reasons
5. ### Bun* https://bun.com/
* minimum Bun version supported by yt-dlp:1.0.31if using Bun, the latest version is strongly recommended
* if using Bun, the latest version is strongly recommended

Note that onlydenois enabled by default; all others are disabled by default for security reasons. Seethe EJS wiki pagefor more details.

In addition tothe JavaScript runtime, yt-dlp also requires theyt-dlp-ejscomponent in order to operate the JS runtime.

NOTE:This componentis already included in all of theofficial yt-dlp executables.Similarly, if you've installed & upgraded the yt-dlp Python package with thedefaultextra (yt-dlp[default]),then you already have the yt-dlp-ejs component.

If you've installed yt-dlp another way, then please refer tosection 2 of the EJS wiki pagefor more details.

Support for YouTube without a JavaScript runtime is now considered "deprecated." It does still work somewhat; however, format availability will be limited, and severely so in some cases (e.g. for logged-in users). Format availability without a JS runtime is expected to worsen as time goes on, and this will not be considered a "bug" but rather an inevitability for which there is no solution. It's also expected that, eventually, support for YouTube will not be possible at all without a JS runtime.

If you have questions, please refer to the EJS wiki page, the previous announcement's FAQ, and the README before commenting or opening a new issue:

* https://github.com/yt-dlp/yt-dlp/wiki/EJS
* [Announcement] Upcoming new requirements for YouTube downloads#14404
* https://github.com/yt-dlp/yt-dlp#dependencies
* https://github.com/yt-dlp/yt-dlp#general-options
* https://github.com/yt-dlp/yt-dlp#youtube-ejs
* https://github.com/yt-dlp/yt-dlp/wiki/EJS#plugins

## Notes to package maintainers

If you are maintaining a downstream package of yt-dlp, we offer the following guidance:

* Theyt-dlprepository, source tarball, PyPI source distribution and built distribution (wheel) are still licensed under The Unlicense (public domain); however,when theyt-dlp-ejspackage is built, it bundles code licensed under ISC and MIT.This is the primary reason whyyt-dlp-ejswas split off into aseparate repositoryandPyPI package
* Ifyt-dlpis packaged as a Python package in your repository,yt-dlp-ejswould ideally be packaged separately
* yt-dlp-ejsis technically anoptionalPython dependency of yt-dlp, but YouTube support is deprecated without it
* Each version ofyt-dlpwill be pinned to a specific version ofyt-dlp-ejsand yt-dlp will reject any otheryt-dlp-ejsversion.Refer to yt-dlp'spyproject.tomlfor the pinned version
* If your repository packagesyt-dlpas the zipimport binary instead of as a Python package, you can usemake yt-dlp-extrato build the zip executable withyt-dlp-ejsincluded. (The Makefile will look for theyt-dlp-ejswheel in thebuildsubdirectory, or the extracted built distribution in theyt_dlp_ejssubdirectory)
* deno,nodejs,quickjsand/orbunshould beoptionaldependencies ofyt-dlp. But again, YouTube support is deprecated withoutoneof them
* Whileyt-dlp-ejsand the external JavaScript runtimes are currently only used with YouTube, yt-dlp's usage of these may be expanded in the future (and necessarily so)

If this guidance is insufficient, or if you are a developer integrating yt-dlp into your software and you have further questions, please open anew GitHub issue.

👍
React with 👍
96
sovalyeler, liamengland1, pha1n0q, onmyouji, serdarth and 91 more
🎉
React with 🎉
31
pha1n0q, onmyouji, DianaNites, mateusneresrb, brandongalbraith and 26 more
❤️
React with ❤️
41
CetaceanNation, KeepBotting, Armster15, pointydev, Dvd-Znf and 36 more
🚀
React with 🚀
18
Dvd-Znf, pha1n0q, DianaNites, mateusneresrb, brandongalbraith and 13 more
👀
React with 👀
2
FavoritoHJS and arrowgent

## Metadata

## Metadata
