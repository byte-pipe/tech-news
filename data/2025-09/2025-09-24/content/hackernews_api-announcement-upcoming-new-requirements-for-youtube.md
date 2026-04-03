---
title: '[Announcement] Upcoming new requirements for YouTube downloads · Issue #14404 · yt-dlp/yt-dlp · GitHub'
url: https://github.com/yt-dlp/yt-dlp/issues/14404
site_name: hackernews_api
fetched_at: '2025-09-24T19:10:55.039192'
original_url: https://github.com/yt-dlp/yt-dlp/issues/14404
author: phewlink
date: '2025-09-24'
description: Beginning very soon, you'll need to have the JavaScript runtime Deno installed to keep YouTube downloads working as normal. Why? Up until now, yt-dlp has been able to use its built-in JavaScript "interpreter" to solve the JavaScript chal...
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
* Fork10.2k
* Star128k

# [Announcement] Upcoming new requirements for YouTube downloads#14404

Open
#14157
Open
[Announcement] Upcoming new requirements for YouTube downloads
#14404
#14157
Labels
discussion/announcement
site:youtube

## Description

bashonly
opened
on
Sep 23, 2025
Issue body actions

### Beginning very soon, you'll need to have the JavaScript runtimeDenoinstalled to keep YouTube downloads working as normal.

## Why?

Up until now, yt-dlp has been able to use itsbuilt-in JavaScript "interpreter"to solve the JavaScript challenges that are required for YouTube downloads. But due torecent changes on YouTube's end, the built-in JS interpreter will soon be insufficient for this purpose. The changes are so drastic thatyt-dlp will need to leverage a proper JavaScript runtime in order to solve the JS challenges.

## What do I need to do?

### Everyone will need to installDeno.

yt-dlp will also need a few JavaScript components, andthismayrequire additional action from youdepending on how you installed yt-dlp:

* Official PyInstaller-bundled executable users (e.g.yt-dlp.exe,yt-dlp_macos,yt-dlp_linux, etc):No additional action required (besides having Deno). All the necessary JavaScript components will be bundled with these executables.
* No additional action required (besides having Deno). All the necessary JavaScript components will be bundled with these executables.
* PyPI package users (e.g. installed withpip,pipx, etc):Installand upgradeyt-dlp with thedefaultoptional dependency group included, e.g.:pip install -U "yt-dlp[default]"
* Installand upgradeyt-dlp with thedefaultoptional dependency group included, e.g.:pip install -U "yt-dlp[default]"
* Official zipimport binary users (theyt-dlpUnix executable):Run yt-dlp with an additional flag to allow Deno to downloadnpmdependencies--or--install yt-dlp's JS solver package in your Python environment. (The flag name and the package name are both still TBD.)
* Run yt-dlp with an additional flag to allow Deno to downloadnpmdependencies--or--install yt-dlp's JS solver package in your Python environment. (The flag name and the package name are both still TBD.)
* Third-party package users (e.g. installed withpacman,brew, etc):The action required will depend on how your third-party package repository decides to handle this change. But the options available for "official zipimport binary users" should work for you as well.
* The action required will depend on how your third-party package repository decides to handle this change. But the options available for "official zipimport binary users" should work for you as well.
👍
React with 👍
148
michealespinola, someziggyman, methbkts, pha1n0q, OnurKader and 143 more
👎
React with 👎
1
barracuda156
🎉
React with 🎉
16
DianaNites, paolobarbolini, fry69, aucampia, sigmaSd and 11 more
😕
React with 😕
30
nicolaasjan, FavoritoHJS, Mubelotix, m-doescode, ZoomRmc and 25 more
❤️
React with ❤️
38
pha1n0q, LostHisMarbles, DianaNites, brianpeiris, Frizlab and 33 more
👀
React with 👀
28
nicolaasjan, nakoo, jmbannon, litetex, EDM115 and 23 more

## Metadata

## Metadata
