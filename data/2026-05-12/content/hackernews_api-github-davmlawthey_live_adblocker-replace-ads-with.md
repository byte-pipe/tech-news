---
title: 'GitHub - davmlaw/they_live_adblocker: Replace Ads with They Live style slogans · GitHub'
url: https://github.com/davmlaw/they_live_adblocker
site_name: hackernews_api
content_file: hackernews_api-github-davmlawthey_live_adblocker-replace-ads-with
fetched_at: '2026-05-12T11:53:29.282269'
original_url: https://github.com/davmlaw/they_live_adblocker
author: tokenburner
date: '2026-05-12'
description: Replace Ads with They Live style slogans. Contribute to davmlaw/they_live_adblocker development by creating an account on GitHub.
tags:
- hackernews
- trending
---

davmlaw

 

/

they_live_adblocker

Public

 forked from 
uBlockOrigin/uBOL-home

* NotificationsYou must be signed in to change notification settings
* Fork2
* Star157

 
 
 
 
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

769 Commits
769 Commits
.github
.github
 
 
chromium
chromium
 
 
dist
dist
 
 
docs
docs
 
 
firefox
firefox
 
 
publish-extension @ bb920c7
publish-extension @ bb920c7
 
 
uBlock @ fa2de61
uBlock @ fa2de61
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.jshintrc
.jshintrc
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
eslint.config.mjs
eslint.config.mjs
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# They Live Adblocker

A fork ofuBlock Origin Litethat, instead ofhidingcosmetically-blocked ads,replacesthem with white tiles bearing slogans from John Carpenter's 1988 filmThey Live:OBEY,CONSUME,WATCH TV,SLEEP,SUBMIT,CONFORM,STAY ASLEEP,BUY,WORK,NO INDEPENDENT THOUGHT,DO NOT QUESTION AUTHORITY.

Each blocked ad gets a single phrase, picked at random from the list.

The idea is from a blog post I wrote in 2015 (and never got around to building):They Live adblock mode.

## Screenshot

## Install

Download the latestuBOLite_theylive.chromium.zipfrom theReleases page, extract it, then in Chromium / Chrome / Brave / Edge:

1. Openchrome://extensions
2. ToggleDeveloper modeon (top-right)
3. ClickLoad unpackedand select the extracted folder

Keep the folder around — the extension is loaded from that path.

### Make it actually replace ads

By default uBO Lite usesBasicfiltering mode, which blocks ads at the network layer. Network-blocked ads never produce a DOM element, so there's nothing to "they-live-ify" — you just get empty space, as with normal uBO Lite. To see the OBEY tiles:

1. Click the uBO Lite toolbar icon → cog (⚙) → Dashboard.
2. Set the filtering mode for the sites you care about toOptimalorComplete.
3. Reload.

## Building from source

Requires Node 22.

git clone --recursive https://github.com/davmlaw/they_live_adblocker

cd
 they_live_adblocker/uBlock
nvm use 22 
#
 or otherwise ensure Node >= 22

tools/make-mv3.sh chromium 
#
 or: firefox | edge | safari

The packaged extension lands inuBlock/dist/build/uBOLite.chromium/— load it as an unpacked extension.

## How it works

uBO Lite's cosmetic filtering normally injects CSS likeselector { display: none !important }to hide matched ad elements. This fork patches those injection sites to instead apply a white-box mask with a::afteroverlay whosecontentis read from adata-ubol-they-liveattribute, then walks the DOM (with a MutationObserver for late-loaded ads) to tag each matched element with a random phrase from the list.

Touched files in thedavmlaw/uBlocksubmodule:

* platform/mv3/extension/js/scripting/they-live.js(new)— phrase list, CSS generator, DOM tagging
* platform/mv3/extension/js/scripting/css-{specific,generic,procedural-api}.js— call sites
* platform/mv3/extension/js/scripting-manager.js— registersthey-live.jsahead of consumers

## Caveats

* Personal hobby fork;notan official uBlock Origin product. Don't file uBO issues against this.
* Forcing previously-hidden elements visible can occasionally shift page layout where the site's CSS assumed the ad slot collapsed.
* Custom user-defined cosmetic filters still hide normally (no OBEY treatment).
* Network-blocked ads (most of uBO Lite's blocking) don't get replaced — only cosmetic-filtered ones do.

## License

GPL-3.0, same as upstream uBlock Origin / uBO Lite.

## About

Replace Ads with They Live style slogans

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

157

 stars
 

### Watchers

0

 watching
 

### Forks

2

 forks
 

 Report repository

 

## Releases1

v0.1.0-theylive — first build

 Latest

 

May 11, 2026

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript97.0%
* CSS2.7%
* Other0.3%