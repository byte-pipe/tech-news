---
title: Release v0.31.0 · jj-vcs/jj · GitHub
url: https://github.com/jj-vcs/jj/releases/tag/v0.31.0
site_name: lobsters
fetched_at: '2025-07-03T23:06:32.353448'
original_url: https://github.com/jj-vcs/jj/releases/tag/v0.31.0
date: '2025-07-03'
description: A Git-compatible VCS that is both simple and powerful - Release v0.31.0 · jj-vcs/jj
tags: release, vcs
---

jj-vcs



/

jj

Public

* NotificationsYou must be signed in to change notification settings
* Fork563
* Star16.8k



# v0.31.0

Latest

Latest


Compare


Loading

ilyagr

 released this



 02 Jul 20:09


 v0.31.0


312c610

### About

jj is a Git-compatible version control system that is both simple and powerful. Seetheinstallation instructionsto get started.

### Breaking changes

* Revset expressions likehidden_id | description(x)nowsearch the specifiedhidden revision and its ancestorsas wellas all visible revisions.
* Commit templates no longer normalizedescriptionby appending final newlinecharacter. Usedescription.trim_end() ++ "\n"if needed.

### Deprecations

* Thegit.push-bookmark-prefixsetting is deprecated in favor oftemplates.git_push_bookmark, which supports templating. The old setting canbe expressed in template as"<prefix>" ++ change_id.short().

### New features

* Newchange_id(prefix)/commit_id(prefix)revset functions to explicitlyquery commits by change/commit ID prefix.
* Theparents()andchildren()revset functions now accept an optionaldepthargument. For instance,parents(x, 3)is equivalent tox---, andchildren(x, 3)is equivalent tox+++.
* jj evologcan now follow changes from multiple revisions such as divergentrevisions.
* jj diffnow accepts-T/--templateoption to customize summary output.
* Log node templates are now specified in toml rather than hardcoded.
* Templates now supportjson(x)function to serialize values in JSON format.
* The ANSI 256-color palette can be used when configuring colors. For example,colors."diff removed token" = { bg = "ansi-color-52", underline = false }will apply a dark red background on removed words in diffs.

### Fixed bugs

* jj file annotatecan now process files at a hidden revision.
* jj op log --op-diffno longer fails at displaying "reconcile divergentoperations."#4465
* jj util gc --expire=nownow passes the corresponding flag togit gc.
* change_id/commit_id.shortest()template functions now take conflictingbookmark and tag names into account.#2416
* Fixed lockfile issue on stale file handles observed with NFS.

### Packaging changes

* aarch64-windowsbuilds (release binaries andmainsnapshots) are now provided.

### Contributors

Thanks to the people who made this release happen!

* Anton Älgmyr (@algmyr)
* Austin Seipp (@thoughtpolice)
* Benjamin Brittain (@benbrittain)
* Cyril Plisko (@imp)
* Daniel Luz (@mernen)
* Gaëtan Lehmann (@glehmann)
* Gilad Woloch (@giladwo)
* Greg Morenz (@gmorenz)
* Igor Velkov (@iav)
* Ilya Grigoriev (@ilyagr)
* Jade Lovelace (@lf-)
* Jonas Greitemann (@jgreitemann)
* Josh Steadmon (@steadmon)
* juemrami (@juemrami)
* Kaiyi Li (@06393993)
* Lars Francke (@lfrancke)
* Martin von Zweigbergk (@martinvonz)
* Osama Qarem (@osamaqarem)
* Philip Metzger (@PhilipMetzger)
* raylu (@raylu)
* Scott Taylor (@scott2000)
* Vincent Ging Ho Yim (@cenviity)
* Yuya Nishihara (@yuja)



### Contributors

 thoughtpolice, mernen, and 21 other contributors



Assets

9




Loading

### Uh oh!

There was an error while loading.Please reload this page.






👍

16


roland-5, welovfree, cwfitzgerald, towry, Natural-selection1, liigo, tw4452852, karesztrk, joshuachp, pertsevds, and 6 more reacted with thumbs up emoji


🎉

25


scott2000, roland-5, glehmann, vic, 0xfeeddeadbeef, welovfree, ygohko, cwfitzgerald, towry, Natural-selection1, and 15 more reacted with hooray emoji


❤️

14


roland-5, BaconIsAVeg, ahmedragab20, welovfree, abusch, cwfitzgerald, towry, Natural-selection1, joshuachp, jihchi, and 4 more reacted with heart emoji


🚀

16


calebdw, roland-5, osamaqarem, welovfree, cwfitzgerald, towry, leaqigaie, Natural-selection1, joshuachp, Stef16Robbe, and 6 more reacted with rocket emoji



All reactions


46 people reacted

 0




Join discussion
