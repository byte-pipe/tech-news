---
title: 'GitHub - averygan/reclip: Download videos from almost any website. Lightweight, self-hosted media downloader with a clean web UI. · GitHub'
url: https://github.com/averygan/reclip
site_name: github
content_file: github-github-averyganreclip-download-videos-from-almost
fetched_at: '2026-09-01T15:24:55.310226'
original_url: https://github.com/averygan/reclip
author: averygan
description: Download videos from almost any website. Lightweight, self-hosted media downloader with a clean web UI. - averygan/reclip
---

averygan

 

/

reclip

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.3k
* Star7.5k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

19 Commits
19 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
assets
assets
 
 
static
static
 
 
templates
templates
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
app.py
app.py
 
 
docker-compose.yml
docker-compose.yml
 
 
docker-entrypoint.sh
docker-entrypoint.sh
 
 
reclip.sh
reclip.sh
 
 
requirements.txt
requirements.txt
 
 
View all files

## Repository files navigation

# ReClip

A self-hosted, open-source video and audio downloader with a clean web UI. Paste links from YouTube, TikTok, Instagram, Twitter/X, and 1000+ other sites — download as MP4 or MP3.

preview.mp4

## Features

* Download videos from 1000+ supported sites (viayt-dlp)
* MP4 video or MP3 audio extraction
* Quality/resolution picker
* Bulk downloads — paste multiple URLs at once
* Automatic URL deduplication
* Clean, responsive UI — no frameworks, no build step
* Single Python file backend (~150 lines)

## Quick Start

brew install yt-dlp ffmpeg 
#
 or apt install ffmpeg && pip install yt-dlp

git clone https://github.com/averygan/reclip.git

cd
 reclip
./reclip.sh

Openhttp://localhost:8899.

Or with Docker:

docker build -t reclip 
.
 
&&
 docker run -p 8899:8899 reclip

## Usage

1. Paste one or more video URLs into the input box
2. ChooseMP4(video) orMP3(audio)
3. ClickFetchto load video info and thumbnails
4. Select quality/resolution if available
5. ClickDownloadon individual videos, orDownload All

## Supported Sites

Anythingyt-dlp supports, including:

YouTube, TikTok, Instagram, Twitter/X, Reddit, Facebook, Vimeo, Twitch, Dailymotion, SoundCloud, Loom, Streamable, Pinterest, Tumblr, Threads, LinkedIn, and many more.

## Stack

* Backend:Python + Flask (~150 lines)
* Frontend:Vanilla HTML/CSS/JS (single file, no build step)
* Download engine:yt-dlp+ffmpeg
* Dependencies:2 (Flask, yt-dlp)

## Disclaimer

This tool is intended for personal use only. Please respect copyright laws and the terms of service of the platforms you download from. The developers are not responsible for any misuse of this tool.

## License

MIT