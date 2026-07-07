---
title: 'GitHub - MaximeRivest/riddle: The diary of Tom Riddle for the reMarkable Paper Pro — write with your pen, the page drinks your ink and answers in a flowing hand · GitHub'
url: https://github.com/MaximeRivest/Riddle
site_name: hackernews_api
content_file: hackernews_api-github-maximerivestriddle-the-diary-of-tom-riddle
fetched_at: '2026-07-07T12:02:27.468097'
original_url: https://github.com/MaximeRivest/Riddle
author: modinfo
date: '2026-07-06'
description: The diary of Tom Riddle for the reMarkable Paper Pro — write with your pen, the page drinks your ink and answers in a flowing hand - MaximeRivest/riddle
tags:
- hackernews
- trending
---

MaximeRivest

 

/

riddle

Public

* NotificationsYou must be signed in to change notification settings
* Fork55
* Star881

 
 
 
 
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

18 Commits
18 Commits
quill
quill
 
 
riddle
riddle
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# riddle — the diary of Tom Riddle, for the reMarkable Paper Pro

Write on the page with your pen. After a pause, the diarydrinks your ink—
your words fade into the paper — the page thinks for a moment, and an answer
writes itself back in a flowing hand, stroke by stroke, then fades away.

No screen glow, no keyboard, no chat UI. Just ink appearing on paper.

This is the diary fromthe demo.

### 🪄 New to this? Start here

You need areMarkable Paper Proin developer mode with a launcher installed.
If that sounds like a lot, it isn't —remagicwalks you through turning on developer mode and sets up everything with one
command. Come back here, drop riddle in, and start writing to Tom.

Already have xovi + AppLoad? Install from theremagiccatalog,grab the prebuilt bundle, orbuild from source.

### Install with remagic (easiest)

remagic install riddle 
#
 checksum-verified download → AppLoad

remagic config riddle 
#
 settings form in your browser (+ QR for phone)

Then inAppLoad: tapReload, thenThe Diary. Write, and rest your
pen. (Or install it from theStoreapp right on the tablet.)

### Install the prebuilt bundle

1. Grabriddle-<version>.zipfrom thelatest releaseand unzip it into a folder:unzip riddle-*.zip -d riddle
2. Copy the folder to your tablet:scp -O -r riddle root@10.11.99.1:/home/root/xovi/exthome/appload/
3. Add an API key:cp oracle.env.example oracle.envin that folder and put yourRIDDLE_OPENAI_KEYin it (any OpenAI-compatible key). Or skip it to usepi.
4. InAppLoad: tapReload, thenThe Diary. Write, and rest your pen.

⚠️This modifies your device.It runs as root, stops the vendor UI
(in takeover mode), and drives the e-ink engine directly. It has only been
tested on areMarkable Paper Pro(ferrari, aarch64, OS 3.26–3.27). It may
not work on other models or OS versions, and you use it entirely at your own
risk. Not affiliated with reMarkable AS. Keep SSH access working before you
install anything — that is your escape hatch.

## How it works

 pen (raw evdev, full 4096-level pressure, hardware event rate)
 │ strokes
 ▼
 riddle ── idle 2.8s → commit page → PNG ──► oracle (resident LLM process,
 │ streams reply sentence-by-sentence)
 ▼ strokes (Dancing Script → skeletonized to single-pixel pen paths)
 display backend
 ├── qtfb — windowed, inside xochitl (AppLoad app)
 └── quill — full takeover: xochitl stopped, vendor e-ink engine
 driven directly for instant ink (lowest latency there is)

* riddle/— the app (Rust). Pen input, ink surface, handwriting
synthesis (rasterize → Zhang-Suen thinning → stroke tracing → animated
replay), the oracle process manager, and both display backends.
* quill/— the takeover display host (C/C++). Anepfb-re-style QImage-constructor
interposition shim over the vendorlibqsgepaper.sowaveform engine,
exposed as a small C ABI (quill_init/quill_buffer/quill_swap)
that riddle links against with--features takeover. Also carries a small
family of demos (scribble, a pen-to-glass latency test, plus map, image,
and GIF renderers).

## Gestures

Do this

And

Write, then rest the pen

The diary drinks your ink and Tom replies

Flip the marker

Erase

Draw a large 
?

Summon the built-in guide

Tap five fingers at once

Leave the diary

Power button

The page turns to 
"The diary sleeps."
, then the tablet suspends; press again to wake exactly where you were

## The oracle (the "spirit" in the diary)

The diary's replies come from a vision LLM that reads your handwriting from the
committed page (sent as an inline PNG). There aretwo backends, chosen at
startup — pick whichever you have:

### Option A — any OpenAI-compatible API (easiest, zero setup)

Set an API key and riddle talks straight to an OpenAI-compatible/chat/completionsendpoint. Works with OpenAI, OpenRouter, Groq, a local
server — anything that speaks the format. No extra software on the tablet.

export
 RIDDLE_OPENAI_KEY=
"
sk-...
"
 
#
 required

export
 RIDDLE_OPENAI_BASE=
"
https://api.openai.com/v1
"
 
#
 optional (default)

export
 RIDDLE_OPENAI_MODEL=
"
gpt-4o-mini
"
 
#
 optional; must see images

export
 RIDDLE_OPENAI_REASONING=
"
low
"
 
#
 thinking models only

export
 RIDDLE_OPENAI_MAX_TOKENS=
"
2000
"
 
#
 runaway guard

Any vision-capable model works. On the tablet these live inoracle.envnext to the binary (seeoracle.env.example, or just runremagic config riddle— it has one-tap presets for OpenAI, OpenRouter,
and Gemini). Example with OpenRouter:

export
 RIDDLE_OPENAI_KEY=
"
$OPENROUTER_API_KEY
"

export
 RIDDLE_OPENAI_BASE=
"
https://openrouter.ai/api/v1
"

export
 RIDDLE_OPENAI_MODEL=
"
openai/gpt-4o-mini
"

Two gotchas with thinking models (Gemini 3.x, o-series): setRIDDLE_OPENAI_REASONING=lowfor faster first ink (some providers reject
the field on non-thinking models — leave it unset there), and keepRIDDLE_OPENAI_MAX_TOKENSroomy — hidden reasoning tokens count against it,
and a tight cap starves the visible reply.

Verify your setup before launching the diary:

riddle --oracle-test path/to/handwriting.png 
#
 prints the streamed reply

Measured ~0.9–1.1 s to first ink on-device. The HTTPS is built into riddle
(pure-Rust, no extra libraries).

### Option B — pi (the power path)

If you already runpi, riddle will use
a residentpi --mode rpcprocess kept warm (Node + your subscription auth
loaded once), so each turn pays only model latency. Used automatically whenRIDDLE_OPENAI_KEYisnotset.

Both stream the reply sentence-by-sentence, so the quill starts writing seconds
before the model finishes. The persona prompt lives inriddle/src/oracle.rs.

## Building

Cross-compiled from x86_64. Two flavours:

### Windowed (AppLoad/qtfb) — easiest

Requiresxovi + AppLoadon the device.

cd
 riddle
cargo build --release --target aarch64-unknown-linux-gnu

Install to/home/root/xovi/exthome/appload/riddle/withexternal.manifest.json,appload-launch.sh, and the binary.

### Takeover (instant ink) — the one from the demo

Requires the reMarkable SDK toolchain (~/rm-sdk-3.26) because the linked
vendor Qt libs need its glibc,andlibqsgepaper.sopulled fromyour own
device(it is proprietary and not distributed here):

cd
 quill 
&&
 ./build.sh 
#
 pulls libqsgepaper.so from the device over

 
#
 ssh, builds libquill.so + the demos

cd
 ../riddle 
&&
 ./build-takeover.sh
./scripts/make-bundle.sh 
#
 stages the AppLoad bundle in dist/riddle/

The stageddist/riddle/is self-contained (binary,libquill.so, launch
scripts, manifest) — copy it to/home/root/xovi/exthome/appload/riddle/, or publish it to the catalog withremagic publish dist/riddle. Launching via AppLoad (appload-launch.sh)
detaches into a transient systemd unit, stops xochitl, runs the diary, andalways restores xochitl on exit— exit with the power button, a 5-finger
tap, or SIGTERM. If anything wedges:ssh root@10.11.99.1 'systemctl start xochitl'.

## Fonts

The reply hand isDancing Script(SIL OFL 1.1 — seeriddle/fonts/OFL.txt).

## License

MIT for everything in this repository (seeLICENSE). The vendor libraries it
interposes (libqsgepaper.so, Qt) arenotincluded and must come from
your own device/SDK.

## About

The diary of Tom Riddle for the reMarkable Paper Pro — write with your pen, the page drinks your ink and answers in a flowing hand

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

881

 stars
 

### Watchers

4

 watching
 

### Forks

55

 forks
 

 Report repository

 

## Releases2

The Diary 0.2.0

 Latest

 

Jul 6, 2026

 

+ 1 release

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust63.0%
* C++18.1%
* C14.5%
* Shell4.4%