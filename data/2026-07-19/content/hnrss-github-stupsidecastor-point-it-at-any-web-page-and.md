---
title: 'GitHub - stupside/castor: Point it at any web page and it finds the video, extracts the stream, transcodes it and casts in real time to your TV. It even burns subtitles…. · GitHub'
url: https://github.com/stupside/castor
site_name: hnrss
content_file: hnrss-github-stupsidecastor-point-it-at-any-web-page-and
fetched_at: '2026-07-19T11:27:55.483726'
original_url: https://github.com/stupside/castor
date: '2026-07-19'
description: Point it at any web page and it finds the video, extracts the stream, transcodes it and casts in real time to your TV. It even burns subtitles…. - stupside/castor
tags:
- hackernews
- hnrss
---

stupside

 

/

castor

Public

* NotificationsYou must be signed in to change notification settings
* Fork12
* Star629

 
 
 
 
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

61 Commits
61 Commits
.github
.github
 
 
cmd
cmd
 
 
internal
internal
 
 
scripts
scripts
 
 
third_party
third_party
 
 
.dockerignore
.dockerignore
 
 
.envrc
.envrc
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
config.yaml
config.yaml
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
main.go
main.go
 
 
View all files

## Repository files navigation

# Castor

Smart TVs won't cast arbitrary web video, and screen mirroring is laggy and drops resolution. Castor casts the real stream instead, at full quality, from your terminal.

I built it because I couldn't cast web video from my laptop to my TV: no Chromecast, no AirPlay.

Point it at any web page and Castor finds the video, extracts the stream, transcodes it for your TV, and casts in real time. It also takes a direct stream URL or an IMDB/TMDB id, and can burn in auto-generated subtitles.

Runcastor castto browse and search titles, inspect posters and metadata, then cast, without leaving the terminal.

Note

How extraction works

Castor launches headless Chrome with a randomized fingerprint and stealth scripts to hide automation. It watches all network traffic over the Chrome DevTools Protocol to capture the video stream, then runs a short action pipeline: click the page, navigate into the largest iframe, solve a Cloudflare Turnstile if one appears, and click again as a fallback.

This works on most streaming sites but won't beat sophisticated bot protection.

## Installation

The recommended way to run Castor is thenative binary. It runs directly on your machine, so it shares your TV's network, which device discovery needs. It requiresChrome/Chromium(headless extraction),ffmpeg(transcoding), andffprobe(format detection) on yourPATH.Dockeris an optional alternative that bundles all three, but only works from a Linux host.

### Homebrew (macOS)

brew install --cask stupside/tap/castor

SeeQuick startto create the one-timeconfig.yaml(which TV, which sources). After that, casting is a single command, no URL, just an IMDB/TMDB id:

castor cast movie tt12300742

### From source

Needs Go 1.26+ and cmake (the whisper.cpp bindings are cgo and link a locally builtlibwhisper.a):

git clone --recurse-submodules https://github.com/stupside/castor.git

cd
 castor
make 
#
 builds libwhisper.a, then the castor binary

go installwon't work: the vendored whisper.cpp bindings come in through a localreplaceand need that prebuilt static lib.

### Docker (optional)

Warning

Docker can only reach your TV from a Linux host on the same LAN.Discovery is SSDP multicast and the TV streams back from Castor's replay server, and neither survives Docker's bridge network, so--network hostis required. But onDocker Desktop (macOS/Windows)--network hostis a silent no-op: the container lands on Docker Desktop's internal VM subnet (e.g.192.168.65.x), never your real LAN, soscanfinds nothing andcastfails withdevice "…" (type dlna) not foundeven though the TV is up.Nodocker runflag fixes this.On macOS/Windows, run thenative binaryinstead. Or point Docker at a Linux VM bridged onto your LAN (e.g. Lima +socket_vmnet), which is the only way a container gets a real address on your network.

On a Linux box or NAS on the same network as the TV, the prebuiltghcr.io/stupside/castorimage bundles Chrome, ffmpeg and ffprobe so you don't install them by hand:

#
 Discover devices (no config required)

docker run --rm --network host ghcr.io/stupside/castor:latest scan

#
 Cast a movie by id, mounting config.yaml and a persistent model cache

docker run --rm --network host \
 -v 
"
$PWD
/config.yaml:/config.yaml
"
 \
 -v castor-cache:/root/.cache \
 ghcr.io/stupside/castor:latest \
 cast movie tt12300742

The-v "$PWD/config.yaml:/config.yaml"mount is what makes this work: the container reads your device and sources fromconfig.yamlat/config.yaml, so run every command from the directory holding it. Thecastor-cachevolume keeps the auto-downloaded whisper models (~75 MB) between runs; swap:latestfor any release tag to pin a version.

## Supported devices

### DLNA / UPnP

Any TV implementing the DLNA/UPnPMediaRenderer:1profile works, which covers virtually every smart TV sold in the last decade:Samsung(tested),LG,Sony Bravia,Panasonic Viera,Philips,Hisense,TCL,VIZIO,Sharp. Networked players like Kodi, VLC, and Plex also work.

Runcastor scanto discover devices on your network.

### Chromecast

Warning

Experimental: implemented but untested. Contributions welcome.

## Quick start

Castorrequires aconfig.yamlin the current directory (or pass--config). Everything mechanical ships with working defaults, so a minimal file only has to saywhich device to cast toandwhich sources to cast from. ATMDB API keyis optional, needed only for the interactive browser.

#
 1. Find your TV's exact name

castor scan

Createconfig.yamlwith that name:

device
:
 
name
: 
"
Living Room TV
"
 
#
 exact name from `castor scan`

 
type
: 
dlna

sources
:
 - 
proxies
: 
["https://vidsrc-embed.ru"]

 
templates
:
 
movie
: 
"
/embed/movie/{itemID}
"

 
episode
: 
"
/embed/tv/{itemID}/{season}-{episode}
"

#
 tmdb:

#
 api_key: "<KEY>" # optional, only for the `castor cast` browser; free from https://www.themoviedb.org/settings/api

That's all you need to cast by id, the quickest path with no TMDB key:

#
 2. Cast a movie straight from an IMDB/TMDB id, resolved through your sources

castor cast movie tt12300742

Note

Sources can change.cast movieresolves the id against theproxiesyou set inconfig.yaml. These are external sites, so one can go offline or move without notice. If a cast stops resolving, update that entry in theproxieslist or add another.

Prefer to browse? Add atmdb.api_keyand runcastor castfor an interactive TUI. It first asks which device to cast to: every DLNA/UPnP renderer on your network, discovered on the fly and with your configured device pre-selected:

Then it opens a TMDB-backed browser: filter by genre, search, inspect posters and metadata, drill into a series' episodes, and cast the one you pick.

## Usage

#
 Interactive TMDB browser: search, pick a movie/episode, cast (needs tmdb.api_key)

castor cast

#
 Cast whatever video is playing on a web page

castor cast player https://example.com/watch/some-video

#
 Cast by IMDB/TMDB id, using the sources in your config

castor cast movie tt33028778
castor cast episode tt2699128 --season 1 --episode 3

#
 Cast a raw stream URL directly

castor cast url https://example.com/stream.m3u8

#
 Useful flags

castor cast movie --dry-run tt33028778 
#
 print found URLs without casting

castor --debug cast player https://... 
#
 verbose logging

castor scan 
#
 discover devices on the network

castor info 
#
 version / build info

## Configuration

Quick startcovers the required keys. Beyond those, everything mechanical (timeouts, probing, capture, transcoding, Chrome discovery) ships with working defaults. Override any of it inconfig.yaml, point at a different file with--config, drop secrets like your TMDB key into a git-ignored siblingconfig.local.yaml(it overlaysconfig.yaml), or setCASTOR_SECTION__FIELDenvironment variables.

The one opt-in worth calling out is auto-generated subtitles, burned into the video:

whisper
:
 
enable
: 
true 
#
 off by default

 
#
 language: "fr" # default: English

 
#
 model_path: "" # default: ggml-tiny.en (~75 MB, auto-downloaded)

## Disclaimer

Castor hosts no video and ships no content of its own. It's a general tool for casting a stream to your TV, not tied to any particular website. The sources in the exampleconfig.yamlare just that, examples; which sites you point it at, and staying within the law and their terms of use, is your responsibility. Only cast content you have the right to access.

## Contributing

SeeCONTRIBUTING.md.

## About

Point it at any web page and it finds the video, extracts the stream, transcodes it and casts in real time to your TV. It even burns subtitles….

### Topics

 streaming

 video

 iptv

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

629

 stars
 

### Watchers

2

 watching
 

### Forks

12

 forks
 

 Report repository

 

## Releases9

v1.4.1

 Latest

 

Jul 19, 2026

 

+ 8 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go92.8%
* JavaScript5.6%
* Other1.6%