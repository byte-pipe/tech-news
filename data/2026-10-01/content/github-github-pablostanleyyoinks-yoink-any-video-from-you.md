---
title: 'GitHub - pablostanley/yoinks: yoink any video from your terminal. no shady ads. · GitHub'
url: https://github.com/pablostanley/yoinks
site_name: github
content_file: github-github-pablostanleyyoinks-yoink-any-video-from-you
fetched_at: '2026-10-01T17:18:09.359199'
original_url: https://github.com/pablostanley/yoinks
author: pablostanley
description: yoink any video from your terminal. no shady ads. Contribute to pablostanley/yoinks development by creating an account on GitHub.
---

pablostanley

 

/

yoinks

Public

* NotificationsYou must be signed in to change notification settings
* Fork264
* Star2.8k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

29 Commits
29 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
assets
assets
 
 
src
src
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
tsup.config.ts
tsup.config.ts
 
 
View all files

## Repository files navigation

# yoinks

yoink any video. paste. yoink. done.

Download videos from YouTube, X/Twitter, Instagram, Threads, TikTok and
1,800+ other sites — right from your terminal. Paste a url, pick a
resolution (or audio-only mp3), done. No popups, no fake download buttons,
no sketchy redirects.

## Install

npm install -g yoinks

Or try it without installing anything:

npx yoinks

Requires Node 18+. Everything else (yt-dlp, ffmpeg) is fetched or bundled
automatically.

## Usage

$ yoinks https://youtu.be/dQw4w9WgXcQ 
#
 straight to the format picker

$ yoinks 
#
 prompts for a url

$ yoinks --theme light 
#
 force the light palette

yoinks takes over the terminal (full-screen, centered — and restores your
scrollback on exit). Pick a format with ↑/↓ (or j/k, or number keys) and
hit enter.escgoes back,^cquits. Or just use the mouse — the yoink
button, the format list and the footer hints are all clickable, and
clicking the logo takes you back home. Files are saved to~/Downloads,
and the file path is printed to your terminal when you're done.

The defaultautotheme uses your terminal's own foreground and background,
so it follows light and dark terminal themes without guessing. Press^tor
click the theme control in the footer to cycle throughauto,light, anddarkfor the current session. Use--theme auto,--theme light, or--theme darkto choose the starting theme for one launch.

## How it works

* Powered byyt-dlp. On first run,
yoinks downloads the standalone yt-dlp binary to~/.yoinks/bin—
no Python required. If you already have yt-dlp installed, it uses yours.
* ffmpeg (needed for merging high-res streams and mp3 extraction) is found
on your PATH, withffmpeg-staticas a bundled fallback.
* The UI isInk— React for the
terminal.

## Development

npm install
npm run build 
#
 bundle to dist/ with tsup

npm run dev 
#
 rebuild on change

node dist/cli.js 
<
url
>

npm run typecheck

To try it as a global command without publishing:npm link, then runyoinksanywhere.

## Roadmap

* --best/--mp3flags to skip the picker (scriptable mode)
* -o <dir>to choose the output folder
* Playlist / thread-with-multiple-videos support
* Clipboard detection: launch bare and auto-suggest the url you copied
* Self-update for the bundled yt-dlp binary (yt-dlp -U)
* Publish to npm (npm i -g yoinks/npx yoinks)
* curl yoinks.sh | shinstaller

## A note on fair use

yoinks is a personal-archiving tool. Downloading content may violate a
platform's terms of service — only download what you have the right to
keep, and be excellent to creators.

## License

MIT