---
title: Converting old home movie DVDs into a private streaming site - DEV Community
url: https://dev.to/peter/converting-old-home-movie-dvds-into-a-private-streaming-site-5bmb
site_name: devto
content_file: devto-converting-old-home-movie-dvds-into-a-private-stre
fetched_at: '2026-04-09T11:24:57.276733'
original_url: https://dev.to/peter/converting-old-home-movie-dvds-into-a-private-streaming-site-5bmb
author: Peter Kim Frank
date: '2026-04-08'
description: A relative sent me a few DVDs containing really old home videos that were at one point saved to DVDs.... Tagged with tutorial, cloudflare, dvd, ripping.
tags: '#tutorial, #cloudflare, #dvd, #ripping'
---

A relative sent me a few DVDs containingreally oldhome videos that were at one point saved to DVDs. The problem is, I don't own a DVD player, and neither do most people in 2026. These discs were just sitting in a box, slowly becoming unplayable, holding memories nobody could actually watch (which is a real shame).

So I bought a cheap USB DVD drive on Amazon (~$25, an Amicool A11), and figured I'd rip the discs and put the videos somewhere my family could get to them. I'm a vibe coder at this point so I used Claude Code and put together a workflow to rip the discs and upload the videos to private streaming site my whole family can pull up on their phones.

Here's how we did it.

## What you need

On the software side, everything is free CLI tools installed through Homebrew:ddrescuefor ripping,ffmpegfor video conversion, andwranglerfor uploading to Cloudflare. Claude Code handled the commands — I mostly described what I wanted and swapped discs.

## Step one: make a safe copy of each disc

The first thing Claude Code suggested was making a bit-perfect copy of each disc before doing anything else. That way even if a disc gets scratched later, we have an exact digital duplicate.

The tool for this isddrescue(notdd). The difference: if a disc has scratches or bad spots,ddjust fails.ddrescueis smarter — it copies what it can, then goes back and retries the problem areas.

brew 
install 
ddrescue

Enter fullscreen mode

Exit fullscreen mode

There were a couple of macOS-specific gotchas that Claude Code figured out along the way. The disc drive doesn't show up indiskutil listlike a normal drive — you needdrutil statusto detect it. And ddrescue needs to be told the exact disc size, otherwise it thinks there's 9,223 petabytes of data to read (basically infinity). The size comes from the block count thatdrutilreports.

We wrapped all of this into a script so I could just run./rip.sh disc-01, wait about 10 minutes, swap the disc, and repeat. Each disc produced a ~4.3 GB.isofile — a perfect clone that I can keep forever as an archive.

## Step two: convert to something playable

Mount the ISO and you find aVIDEO_TSfolder full of.VOBfiles. That's the old DVD-Video format — fine for DVD players, useless for phones and browsers.

ffmpegconverts each clip to a modern H.264 MP4:

ffmpeg 
-i
 VTS_01_1.VOB 
\

 
-c
:v libx264 
-crf
 22 
\

 
-c
:a aac 
-b
:a 128k 
\

 
-movflags
 +faststart 
\

 clip-01.mp4

Enter fullscreen mode

Exit fullscreen mode

I didn't know any of these flags — Claude Code picked the settings and explained why each one matters (the-movflags +faststartone moves metadata to the front of the file so browsers can stream it without downloading the whole thing first). My discs had 13 to 21 clips each.

## Step three: put it online

You could upload these to YouTube (unlisted), Google Drive, or Dropbox and call it a day. But I liked the idea of having my own thing — files on storage I control, a simple site I can customize, no platform deciding to compress my videos or change their sharing features.

Claude Code set up the hosting on Cloudflare, which turned out to be free for this use case:

* Cloudflare R2stores the video files. It's object storage, like a hard drive in the cloud. You upload files with a CLI command and they just sit there.
* Cloudflare Pageshosts a simple website — one HTML file with a grid of video thumbnails.
* A smallPages Functionconnects the two, serving videos from R2 when you click play.

The upload was just a loop runningwrangler r2 object putfor each clip. Claude Code handled the commands while I did other things.

The one step I had to do manually in the Cloudflare dashboard was connecting the R2 bucket to the Pages site. Under the project's Settings > Bindings, I added an R2 binding so the site's code could actually read from the bucket. Took about 30 seconds but it's not something the CLI can do yet.

To lock it down to family only, there'sCloudflare Access— you add email addresses of people who should have access, and everyone else gets a login screen. Also free for small groups.

## The gallery

The site itself is a single HTML page. No React, no build step. Just a dark grid of thumbnails.

Claude Code added a couple of nice touches:

Lightweight thumbnails— instead of loading 47 video players on page load, each clip shows a tiny JPEG thumbnail (~5 KB) with a play button. Click it and the actual video loads. The page loads in under a second.

Hover preview— move your mouse across any thumbnail and it scrubs through the video, YouTube-style. This is done with sprite sheets — one image per clip containing 20 frames tiled horizontally (~40 KB each). No video data loads until you actually click play.

There's a small progress bar at the bottom of each thumbnail as you scrub so you can tell where you are in the clip.

The video manifest is just a JavaScript object that maps disc names to clip counts. When I rip a new disc, I add one line and redeploy.

## What it costs

Essentially nothing. Cloudflare R2 doesn't charge for bandwidth — when family streams a video, there's no per-GB fee. Storage is free up to 10 GB, and my 3-disc archive is about 8 GB of converted video. Even if I rip every disc in the box I'd be well under $1/month. For a family casually rewatching old home videos, this is basically a free setup.

## The rip script

Here's the script Claude Code and I ended up with. It auto-detects the disc, figures out the size, and runs a two-pass rip:

#!/usr/bin/env bash

set
 
-euo
 pipefail

if
 
[[
 
$# 
-lt
 1 
]]
;
 
then
 
echo
 
"Usage: 
$0
 <disc-label>"

 
exit 
1

fi

LABEL
=
"
$1
"

RAW_DIR
=
"
$(
dirname
 
"
$0
"
)
/raw"

LOG_DIR
=
"
$(
dirname
 
"
$0
"
)
/logs"

DISC
=
$(
drutil status 2>/dev/null | 
grep
 
"Name:"
 | 
awk
 
'{print $NF}'
)

if
 
[[
 
-z
 
"
$DISC
"
 
]]
;
 
then
 
echo
 
"No disc detected. Insert a disc and try again."

 
exit 
1

fi

BLOCKS
=
$(
drutil status 2>/dev/null 
\

 | 
grep
 
"Space Used:"
 
\

 | 
sed
 
's/.*blocks:[[:space:]]*//'
 
\

 | 
awk
 
'{print $1}'
)

DISC_SIZE
=
$((
 BLOCKS 
*
 
2048
 
))

diskutil unmountDisk 
"
$DISC
"
 2>/dev/null 
||
 
true

ddrescue 
-b
 2048 
-s
 
"
$DISC_SIZE
"
 
-n
 
"
$DISC
"
 
"
$RAW_DIR
/
${
LABEL
}
.iso"
 
"
$LOG_DIR
/
${
LABEL
}
.log"

ddrescue 
-b
 2048 
-s
 
"
$DISC_SIZE
"
 
-r
 3 
"
$DISC
"
 
"
$RAW_DIR
/
${
LABEL
}
.iso"
 
"
$LOG_DIR
/
${
LABEL
}
.log"

echo
 
"Done! 
$(
ls
 
-lh
 
"
$RAW_DIR
/
${
LABEL
}
.iso"
 | 
awk
 
'{print $5}'
)
"

Enter fullscreen mode

Exit fullscreen mode

Pop a disc in, run./rip.sh disc-04, swap, repeat. About 10 minutes per disc.

The whole project took about an hour of actual thinking work, and a few hours of waiting for discs to rip and videos to upload while I did other things. Claude Code handled the parts I didn't know — the ffmpeg flags, the Cloudflare Pages Function for video seeking, the sprite sheet math — and I handled the part it couldn't: physically swapping discs.

My mom can now watch her old home videos on her phone. That alone was worth it. And I can rest easy knowing these family memories are safely stored in the cloud.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse