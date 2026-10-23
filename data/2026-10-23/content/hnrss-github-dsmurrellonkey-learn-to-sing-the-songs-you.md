---
title: 'GitHub - dsmurrell/onkey: Learn to sing the songs you love. A free, open-source singing trainer for Mac that listens to the music you play. · GitHub'
url: https://github.com/dsmurrell/onkey
site_name: hnrss
content_file: hnrss-github-dsmurrellonkey-learn-to-sing-the-songs-you
fetched_at: '2026-10-23T21:57:35.596266'
original_url: https://github.com/dsmurrell/onkey
date: '2026-10-22'
description: Learn to sing the songs you love. A free, open-source singing trainer for Mac that listens to the music you play. - dsmurrell/onkey
tags:
- hackernews
- hnrss
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

3 Commits
3 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
ISSUE_TEMPLATE
.github/
ISSUE_TEMPLATE
 
 
design
design
 
 
docs
docs
 
 
scripts
scripts
 
 
site
site
 
 
src-tauri
src-tauri
 
 
ui
ui
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LEGAL.md
LEGAL.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
THIRD_PARTY_NOTICES.md
THIRD_PARTY_NOTICES.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# OnKey

Learn to sing the songs you love.·singonkey.app

Saving shower singers from themselves since 2026.

Me singing along to a song OnKey learned from one play.The full demo, with sound.

OnKey is a free, open-source singing trainer for the Mac. Play a song in Spotify, Apple Music, or YouTube in a
browser, and sing along. The first time, you get the lyrics, and OnKey learns the singer's melody when the song
ends. After that, the notes scroll towards you, your pitch is drawn over them, and you get a score with a report on
every line.

OnKey doesn't provide, stream or download music. Your own music app plays it.

## Install

You need a Mac with Apple Silicon (M1 or later) and macOS 14.2 or later.

DownloadOnKey.dmg(from thelatest release), open it and drag OnKey to Applications.

Setup asks for the microphone, to hear you, and for system audio recording, to hear the music app. It also asks
whether OnKey may follow Spotify and Apple Music: chooseListen onlyand it follows songs by their sound alone.Getting startedwalks through it, and theFAQanswers the usual questions.

## How it works

When a song ends, OnKey learns it on your Mac: a model separates the lead vocal from the music, CREPE tracks the
singer's pitch, and the GAME note model turns it into one bar per syllable. On later plays it finds its place from
the music itself and tracks your voice live. Singing an octave down counts, and being a touch late isn't punished.How it worksandScoringhave
the details.

## Privacy

OnKey never saves the music it listens to. It analyses the sound in memory as it plays. Your recordings and the
songs it learns stay on your Mac (a take sung over speakers can contain some of the music). There's no account, no
analytics and no crash reporting.

These requests do go out:

* Shazam (Apple): a short signature of the music app's sound, not the audio and never your mic, to name a song
OnKey hasn't learned when the music app doesn't say what's playing.
* LRCLIB: the song's artist, title, album and length, to fetch lyrics.
* iTunes Search and Lookup (Apple): an artist and title, or the ID Shazam returned, for covers and the song's
length. The cover images come from Spotify's, Apple's or YouTube's image hosts.
* GitHub: a check for a new version a minute after launch and once a day, and its download.

Settings has a switch for Shazam, for lyrics and for the update check.Privacylists everything OnKey keeps and sends, andscripts/release-hosts.txtlists every web
address in a release.

## Using OnKey fairly

OnKey is for practising at home, with music you're entitled to play. Please:

* Keep what it learns to yourself. Its transcription of each song's melody is for your practice, so don't share or
publish it.
* To share a take, useShareon its page. It makes a short video of your voice and your pitch line, with no
music, and you can add the song from Instagram's own music library, which is licensed for this. Headphone takes
are best: sung on speakers, some of the song is in your recording. Don't post screen recordings with the music
playing.
* Use a licensed karaoke service for a bar or an event. OnKey's lyrics come from a free community database.
* Don't modify OnKey to save the music.

Rights holders can reach me athello@singonkey.app(LEGAL.md).

## Help

UseReport a problemin the app (Settings, the Help menu, or a take's page). It saves a zip of numbers and logs
on your Mac, with no audio and no recordings of you, for you to attach to anissueif you want to.Troubleshootingcovers the common problems. Questions, or a song
that's out of step? Ask inOnKey's Discord, or emailhello@singonkey.app.

## Building from source

If you'd rather not trust my build, you can build your own. You need an Apple Silicon Mac with the Xcode command
line tools, Rust, Node, and Python 3:

git clone https://github.com/dsmurrell/onkey 
&&
 
cd
 onkey
npm install 
&&
 npm --prefix ui install
python3 -m venv .venv 
&&
 .venv/bin/pip install -r scripts/requirements-models.txt
PYTHON=.venv/bin/python scripts/fetch-models.sh 
#
 downloads the models and checks them by SHA-256

npx tauri build

Your build runs on your own Mac. The one thing it can't do is ask Shazam to name a new song, which needs my Apple
signature. Spotify and Apple Music say what's playing themselves, so that only affects YouTube and Listen only.CONTRIBUTING.mdhas the details, the tests, and how to check a release's checksums. My
releases are signed with my Apple Developer ID and notarised by Apple (spctl -a -vv /Applications/OnKey.appshows who signed it).

## Licence and credits

MIT. SeeLICENSE. Modified versions can't be called OnKey or use its icon. If you build on OnKey's code,
a credit linking back here is appreciated.

OnKey learns songs with CREPE, GAME, wav2vec 2.0 and UVR's MDX-Net Karaoke 2. Thecreditslist each one, andTHIRD_PARTY_NOTICES.mdhas the full notices and licence texts.

OnKey is made byDaniel Murrell.