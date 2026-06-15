---
title: 'GitHub - tamnd/kage: Shadow any website for offline viewing, with the JavaScript stripped out · GitHub'
url: https://github.com/tamnd/kage
site_name: hackernews_api
content_file: hackernews_api-github-tamndkage-shadow-any-website-for-offline-vi
fetched_at: '2026-06-15T13:07:08.428758'
original_url: https://github.com/tamnd/kage
author: tamnd
date: '2026-06-14'
description: Shadow any website for offline viewing, with the JavaScript stripped out - tamnd/kage
tags:
- hackernews
- trending
---

tamnd

 

/

kage

Public

* NotificationsYou must be signed in to change notification settings
* Fork28
* Star1.2k

 
 
 
 
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

41 Commits
41 Commits
.github/
workflows
.github/
workflows
 
 
asset
asset
 
 
browser
browser
 
 
cli
cli
 
 
clone
clone
 
 
cmd/
kage
cmd/
kage
 
 
dataset
dataset
 
 
docs
docs
 
 
pack
pack
 
 
robots
robots
 
 
sanitize
sanitize
 
 
scripts
scripts
 
 
urlx
urlx
 
 
viewer
viewer
 
 
zim
zim
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.goreleaser.yaml
.goreleaser.yaml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
View all files

## Repository files navigation

# kage

kage(影, "shadow") clones a website into a folder you can browse offline, with every script stripped out. It opens each page in real headless Chrome, waits for the page to settle, snapshots the DOM a human would have seen, then deletes all the JavaScript and pulls the CSS, images, and fonts down to local paths. What lands on disk looks like the live site and runs no code.

Install•Quick start•Commands•Clone•Pack•Double-click app•Native window•How it works

You already know the problem. You hit "Save As" on a page you want to keep, and six months later you open it to find a blank screen, a spinner that never stops, or a copy that still tries to phone home to an analytics server that no longer exists. The page was never really yours. It was a thin client for someone else's JavaScript.

kage takes the other road. It drives a real browser, lets the page finish doing whatever it does, grabs the finished result, and then rips every script out of it. No tracking, no network calls, no surprises. Just.htmlfiles you can open straight off disk, hand to a friend, or pack into a single file and forget about for a decade.

Full docs and guides live atkage.tamnd.com.

## Install

go install github.com/tamnd/kage/cmd/kage@latest

Prefer a prebuilt binary? Grab an archive, a.deb/.rpm/.apk, or a checksum fromreleases. Or skip installing Chrome yourself and use the container image, which bundles Chromium:

docker run --rm -v 
"
$PWD
/out:/out
"
 ghcr.io/tamnd/kage clone paulgraham.com

kage drives a real browser, so it needs Chrome or Chromium on the host. It finds a system install on its own; point it somewhere specific with--chromeor theKAGE_CHROMEenvironment variable. The container needs nothing extra.

Shell completion ships in the box:kage completion bash|zsh|fish|powershell.

## Quick start

Let's mirror Paul Graham's essays so you can read them on a plane, on a laptop with no wifi, or in the year 2050 after the site has finally changed its design:

#
 1. Clone the site into $HOME/data/kage/paulgraham.com/

kage clone paulgraham.com

#
 2. Read it back offline in your browser

kage serve 
$HOME
/data/kage/paulgraham.com

#
 open http://127.0.0.1:8800

That's the whole loop. Every essay, every image, every stylesheet, frozen on your disk and runnable with zero network. The next two steps are optional but nice: collapse the whole thing into one file, and pop it open in its own window.

#
 3. Squeeze the mirror into a single shareable file

kage pack paulgraham.com 
#
 -> paulgraham.com.zim

kage open paulgraham.com.zim

#
 4. Or into one executable that *is* the site

kage pack paulgraham.com --format binary -o paulgraham
./paulgraham 
#
 serves itself, needs nothing installed

## Commands

Command

What it does

kage clone <url>

render a site in headless Chrome and write a browsable, script-free mirror

kage serve [dir]

preview a cloned folder over a local HTTP server

kage pack <mirror-dir>

collapse a mirror into one ZIM archive, a self-contained viewer binary, or a double-click app

kage open <file.zim>

serve a packed ZIM back for offline reading

## Clone

#
 The whole site, into $HOME/data/kage/<host>/

kage clone https://paulgraham.com

#
 Just the first 50 pages, two links deep, for a quick taste

kage clone paulgraham.com --max-pages 50 --max-depth 2

#
 Only one section of a bigger site

kage clone go.dev --scope-prefix /doc

#
 Pull in subdomains too, and scroll each page to trip lazy-loaded images

kage clone example.com --subdomains --scroll

#
 Come back next month and re-render in place to catch new essays

kage clone paulgraham.com --refresh

A clone is a polite, breadth-first crawl. It readsrobots.txt, seeds itself fromsitemap.xml, and stays on the seed host unless you tell it otherwise. It is also stubbornly idempotent: each page is keyed by the file it writes, so the same essay reached over http and https, with or without a trailing slash, gets fetched exactly once. Hit Ctrl-C and it saves its place on the way out; run it again and it picks up where it stopped.--refreshre-renders in place,--forcewipes the host and starts clean.

The flags you'll actually reach for:

Flag

Default

Meaning

-o, --out

$HOME/data/kage

Output root; the mirror lands in 
<out>/<host>/

-p, --max-pages

0

Stop after N pages (0 = no limit)

-d, --max-depth

0

How many links deep to follow (0 = no limit)

--scope-prefix

Only crawl paths starting with this prefix

--subdomains

false

Treat subdomains of the seed host as in scope

--exclude

Path prefixes to skip (repeatable)

--scroll

false

Auto-scroll each page to trigger lazy loading

--workers

4

How many pages to render at once

--no-robots

false

Ignore 
robots.txt
 (be nice)

-f, --force

false

Delete any existing mirror for the host first

--chrome

Path to the Chrome/Chromium binary

kage clone --helphas the rest, including render-timing, concurrency, and asset-size knobs.

### Serve

kage serveruns a tiny static file server over a cloned folder so links and assets resolve the way they would on a real host:

kage serve 
$HOME
/data/kage/paulgraham.com

#
 open http://127.0.0.1:8800

## Pack it into one file

A mirror is a folder, which is great for browsing and lousy for moving around. Copying thousands of little files is slow, and "here, have this directory" is a clumsy thing to hand someone.kage packcollapses the whole mirror into one artifact, and you choose the shape: an open ZIM archive, or a single executable thatisthe site.

### A single ZIM file

kage pack paulgraham.com 
#
 -> paulgraham.com.zim

kage open paulgraham.com.zim

ZIM is an open file format built for exactly this: a whole website (or a whole Wikipedia) squeezed into one compressed, indexed, read-only file. kage writes the entire mirror into it, text zstd-compressed and media stored as-is. It is the format behindKiwix, the offline-content project people use to carry Wikipedia, Stack Overflow, and Project Gutenberg onto boats, into classrooms with no internet, and onto a phone for a long flight. Because the format is a documented standard and not a kage invention, apaulgraham.com.zimyou make today will still open in any ZIM reader years from now.

So you are not locked into kage.kage openis the quickest way back in, but the very same file works across the wider Kiwix ecosystem:

kage open paulgraham.com.zim 
#
 read it back with kage

kiwix-serve paulgraham.com.zim 
#
 or serve it with Kiwix at http://localhost

You can also double-click the file in theKiwix desktop app, or load it onKiwix for Android or iOSto read your mirror on your phone. One caveat: kage writes a structurally valid archive with the standard metadata, but it does not build the full-text search index that Kiwix's own packs ship with, so browsing and clicking work everywhere while in-reader search is limited.

Packing is deterministic. The same mirror always produces a byte-identical file, with the archive UUID derived from the content instead of randomized, so a pack is safe to checksum and cache. A bare host name resolves against the default output directory, which is whykage pack paulgraham.comjust works right afterkage clone paulgraham.com.

### A self-contained binary

--format binaryglues the archive onto a copy of kage and hands you a single executable that serves the site offline when you run it. Whoever you send it to needs nothing installed: not kage, not a ZIM reader, nothing.

kage pack paulgraham.com --format binary -o paulgraham
./paulgraham

The appended archive is platform-independent; only the base executable carries the architecture. By default kage appends to itself, so you get a viewer for the machine you ran it on. Point--baseat a kage built for another OS (grab one from arelease; every platform ships one) to produce a viewer for that platform from your own machine. kage reads the base's executable header to figure out the target, so a Windows viewer automatically gets a.exename:

#
 Sitting on a Mac, build a Windows viewer

kage pack paulgraham.com --format binary --base kage-windows-amd64.exe 
#
 -> paulgraham.exe

The trade is size. The binary carries a whole kage, so it weighs around 13 MiB plus the site no matter how small the mirror is. When you only need the content, the ZIM is far leaner.

### A double-click app

A bare binary is great from a terminal, but double-click it in a file manager and the experience is rough: macOS opens a Terminal window behind the site, and on Windows a console flashes up next to it. Add--appand kage wraps the same viewer in a proper desktop app so a double-click just opens the site, no terminal, with the mirror's own favicon as the icon.

On macOS you get a real.appbundle:

kage pack paulgraham.com --app 
#
 -> paulgraham.app

open paulgraham.app 
#
 or double-click it in Finder

On Linux, point--baseat a Linux kage and you get anAppImage-style.AppDirwith a.desktoplauncher (Terminal=false, so no console). Ifappimagetoolis installed, kage folds it into a single double-clickable.AppImagefor you:

kage pack paulgraham.com --app --base kage-linux-amd64 
#
 -> paulgraham.AppDir (+ .AppImage)

kage finds the icon by digging the favicon out of the mirror (it prefers a largeapple-touch-icon.pngand falls back tofavicon.ico); pass--icon some.pngto override it. Pair--appwith awebviewbase (below) and the double-click opens a native window instead of the browser, which is the full "it's an app" effect.

Windows needs no bundle, because there a single.exealready is the app. The catch is the console window. The release ships akage_<version>_windows-gui_<arch>.zipwhose binary is linked for the GUI subsystem, so a viewer packed onto it opens with no console behind it:

#
 Build a console-free Windows viewer (from any OS)

kage pack paulgraham.com --format binary --base kage-windows-gui-amd64.exe 
#
 -> paulgraham.exe

## A real window, not a browser tab

By default a packed binary opens your system browser, which means the site shows up as yet another tab, address bar and all, next to the 47 you already have open. Build kage with thewebviewtag and it opens the site in its own window instead, backed by the operating system's WebView (WKWebView on macOS, WebView2 on Windows, WebKitGTK on Linux). Paul Graham's essays, offline, in something that looks and feels like a real app:

make build-webview 
#
 or: CGO_ENABLED=1 go build -tags webview ./cmd/kage

kage pack paulgraham.com --format binary --base bin/kage -o paulgraham
./paulgraham 
#
 opens a window, no browser in sight

This build needs cgo and links the platform WebView, so it stays opt-in. The default build is pure Go (CGO_ENABLED=0) and the prebuilt release binaries open the browser, which keeps the cross-compiled release simple.kage openhonours the same tag, so built with-tags webviewit shows a ZIM in a native window too.

## How it works

seed URL ─▶ headless Chrome ─▶ final DOM ─▶ strip JS ─▶ localise assets ─▶ disk
 (render) (snapshot) (sanitize) (rewrite links)

A pool of Chrome tabs renders pages; a separate pool fetches assets over plain HTTP. Every URL maps deterministically to a local path, so links get rewritten before the asset they point at has even finished downloading. The output looks like this:

paulgraham.com/
├── index.html # the home page, scripts stripped
├── greatwork.html # /greatwork.html, an essay
├── _kage/ # reserved: assets and crawl state
│ ├── paulgraham.com/site.css # localised stylesheet (url() rewritten)
│ ├── paulgraham.com/pg.png
│ └── state.json # visited set, for resuming
└── ...

packrides on the same idea: the mirror's links are already mirror-relative paths, and those map one-to-one onto the archive's content entries, so a click in a served page hits the right entry with no rewriting at all.

## Building from source

git clone https://github.com/tamnd/kage

cd
 kage
make build 
#
 -> bin/kage (pure Go, opens the browser)

make build-webview 
#
 -> bin/kage with the native-window viewer (needs cgo)

make 
test
 
#
 full suite, including the Chrome-driven end-to-end tests

make test-short 
#
 skip the tests that launch a browser

The repo is split by concern:

cmd/kage/ thin main: pins the main thread, then hands off to cli.Execute
cli/ the cobra command tree and flag wiring
clone/ the crawl: frontier, render workers, asset workers, resume state
browser/ headless Chrome control and DOM snapshotting
sanitize/ strip scripts, handlers, and javascript: URLs from the DOM
asset/ download and localise CSS, images, and fonts
urlx/ the deterministic URL-to-path mapping
zim/ a pure-Go ZIM reader and writer
pack/ mirror to ZIM or self-contained binary, and the offline HTTP handler
viewer/ present a served site: system browser, or native window (webview tag)
docs/ the tago documentation site

## Releasing

Push a version tag and GitHub Actions runs GoReleaser, which builds the archives, the.deb/.rpm/.apkpackages, a multi-arch GHCR image with Chromium bundled, checksums, SBOMs, and a cosign signature:

git tag v0.1.1
git push --tags

The image tag carries novprefix (ghcr.io/tamnd/kage:0.1.1). The Homebrew and Scoop steps self-disable until their tokens exist, so the first release works with no extra secrets.

## License

MIT. SeeLICENSE.

## About

Shadow any website for offline viewing, with the JavaScript stripped out

kage.tamnd.com

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

1.2k

 stars
 

### Watchers

4

 watching
 

### Forks

28

 forks
 

 Report repository

 

## Releases5

v0.2.1

 Latest

 

Jun 15, 2026

 

+ 4 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go97.2%
* Python1.8%
* Other1.0%