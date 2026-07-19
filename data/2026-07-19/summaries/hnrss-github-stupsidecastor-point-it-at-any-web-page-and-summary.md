---
title: GitHub - stupside/castor: Point it at any web page and it finds the video, extracts the stream, transcodes it and casts in real time to your TV. It ev...
url: https://github.com/stupside/castor
date: 2026-07-19
site: hnrss
model: llama3.2:1b
summarized_at: 2026-07-19T11:33:36.867500
---

# GitHub - stupside/castor: Point it at any web page and it finds the video, extracts the stream, transcodes it and casts in real time to your TV. It ev...

**Overview of Castor**

Castor is a command-line tool that transcodes and casts web videos to Smart TVs in real-time, allowing users to browse and cast content without leaving their terminal.

**Key Features**

* Extracts video streams from web pages
* Transcodes the stream for optimal quality display on television
* Burns auto-generated subtitles at the end of the video playback

**Installation and Setup**

* Requires a headless Chrome browser (e.g. Coredetached on Linux) in addition to other tools like FFmpeg and ffprobe
* Available on Docker image as `/mnt/castor`
* Optional installation via Homebrew or custom build from source requirements (Go 1.26+ and Cmake)
* Recommended use of a TV with internet connectivity on the same local network

**How it Works**

1. The tool extracts video streams from web pages using headless Chrome
2. Identifies optimal display settings for each stream to ensure highest quality
3. Transcodes the selected stream into a format accessible by television (e.g. H264, H265)
4. Burns auto-generated subtitles if available

**Tips and Variations**

* Using IMDB or TMDB IDs works only on web browsers with specific access control measures in place
* For more advanced features like searching titles or inspecting posters and metadata, users may need additional scripts to navigate the site