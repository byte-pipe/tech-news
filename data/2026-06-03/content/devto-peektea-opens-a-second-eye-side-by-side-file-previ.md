---
title: peektea opens a second eye 👀 side-by-side file previews - DEV Community
url: https://dev.to/lovestaco/peektea-opens-a-second-eye-side-by-side-file-previews-n6j
site_name: devto
content_file: devto-peektea-opens-a-second-eye-side-by-side-file-previ
fetched_at: '2026-06-03T20:09:08.913671'
original_url: https://dev.to/lovestaco/peektea-opens-a-second-eye-side-by-side-file-previews-n6j
author: Athreya aka Maneshwar
date: '2026-06-02'
description: Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is... Tagged with webdev, programming, cli, beginners.
tags: '#webdev, #programming, #cli, #beginners'
---

Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is free and source-available on Github.Star git-lrcto help devs discover the project. Do give it a try and share your feedback.

Last time, I ended with a "what's next" list.

At the top of it:

Image previews inline: render images in the terminal via Kitty/iTerm protocols orchafa

Split-pane file preview: selected file content on the right, so you can peek without leaving

Today both of those ship.

Pressp. A preview panel opens on the right. Presspagain. It closes.

That's it. That's the whole feature from the outside.

The inside is more interesting.

## The preview panel

peektea now renders in two columns when preview is on.

Left: the file browser. Right: whatever's under the cursor.

It handles four cases:

* Text files: first N lines, tab-expanded, truncated to panel width
* Images: rendered inline viachafa
* Directories: lists the contents with the same dir/file styling as the browser
* Binary files: a[binary file]notice instead of garbage

The preview updates as you navigate.

Move the cursor, a new preview loads.

Navigate into a directory, it previews the new selection.

## Async loading with tea.Cmd

The preview can't block the TUI, reading a large file or running chafa takes time.

In Bubble Tea, anything that takes time is atea.Cmd: a function that runs off the main loop and returns a message when it's done.

type
 
previewMsg
 
struct
{
 
content
 
string
 
}

func
 
loadPreview
(
path
 
string
,
 
entry
 
os
.
DirEntry
,
 
width
,
 
height
 
int
)
 
tea
.
Cmd
 
{

 
return
 
func
()
 
tea
.
Msg
 
{

 
if
 
entry
.
IsDir
()
 
{

 
return
 
previewMsg
{
content
:
 
previewDir
(
path
,
 
width
,
 
height
)}

 
}

 
if
 
isImageExt
(
entry
.
Name
())
 
{

 
return
 
previewMsg
{
content
:
 
previewImage
(
path
,
 
width
,
 
height
)}

 
}

 
return
 
previewMsg
{
content
:
 
previewText
(
path
,
 
width
,
 
height
)}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

The model setspreviewLoading = trueand fires the command.

The panel showsloading….

When the goroutine finishes,previewMsgcomes back throughUpdateand the panel renders the result.

The TUI stays responsive the whole time, you can keep navigating while a slow preview loads.

## Image previews via chafa

chafa is a terminal image viewer that converts images into coloured Unicode blocks.

It respects--size WxHso the output fits exactly inside the preview panel.

func
 
previewImage
(
path
 
string
,
 
width
,
 
height
 
int
)
 
string
 
{

 
if
 
_
,
 
err
 
:=
 
exec
.
LookPath
(
"chafa"
);
 
err
 
!=
 
nil
 
{

 
return
 
"[image — install chafa for inline preview]"

 
}

 
out
,
 
err
 
:=
 
exec
.
Command
(
"chafa"
,

 
"--size"
,
 
fmt
.
Sprintf
(
"%dx%d"
,
 
width
,
 
height
),

 
path
,

 
)
.
Output
()

 
if
 
err
 
!=
 
nil
 
{

 
return
 
fmt
.
Sprintf
(
"[image preview failed: %v]"
,
 
err
)

 
}

 
return
 
strings
.
TrimRight
(
string
(
out
),
 
"
\n
"
)

}

Enter fullscreen mode

Exit fullscreen mode

If chafa isn't installed, the panel tells you so. No crash, no silent blank.

peektea initnow checks for chafa at the end of setup and prints the install command for your distro if it's missing.

## Binary detection

Opening a binary file as text gives you noise.

So before reading, peektea checks the first 512 bytes for null bytes, that's the standard heuristic used bygit diffand most editors.

func
 
isBinary
(
path
 
string
)
 
bool
 
{

 
f
,
 
err
 
:=
 
os
.
Open
(
path
)

 
if
 
err
 
!=
 
nil
 
{

 
return
 
false

 
}

 
defer
 
f
.
Close
()

 
buf
 
:=
 
make
([]
byte
,
 
512
)

 
n
,
 
_
 
:=
 
f
.
Read
(
buf
)

 
for
 
_
,
 
b
 
:=
 
range
 
buf
[
:
n
]
 
{

 
if
 
b
 
==
 
0
 
{

 
return
 
true

 
}

 
}

 
return
 
false

}

Enter fullscreen mode

Exit fullscreen mode

If it's binary, the preview says[binary file]and moves on.

## Terminal size and the adaptive left panel

To split the screen correctly, peektea needs to know how big it is.

Bubble Tea sends atea.WindowSizeMsgwhenever the terminal is resized.

The model storeswidthandheightand uses them to calculate panel dimensions on every render.

case
 
tea
.
WindowSizeMsg
:

 
m
.
width
 
=
 
msg
.
Width

 
m
.
height
 
=
 
msg
.
Height

Enter fullscreen mode

Exit fullscreen mode

The left panel width isn't fixed, it starts at a minimum of 50 chars and then expands to fit the longest filename in the current directory:

func
 
(
m
 
model
)
 
leftWidth
()
 
int
 
{

 
const
 
minWidth
 
=
 
50

 
w
 
:=
 
minWidth

 
for
 
_
,
 
e
 
:=
 
range
 
m
.
entries
 
{

 
nameW
 
:=
 
2
 
+
 
len
([]
rune
(
e
.
Name
()))

 
if
 
e
.
IsDir
()
 
{

 
nameW
++

 
}

 
if
 
nameW
 
>
 
w
 
{

 
w
 
=
 
nameW

 
}

 
}

 
// Always leave at least 30 chars for the preview panel.

 
if
 
max
 
:=
 
m
.
width
 
-
 
32
;
 
w
 
>
 
max
 
{

 
w
 
=
 
max

 
}

 
return
 
w

}

Enter fullscreen mode

Exit fullscreen mode

Navigate into a directory with long filenames and the left panel widens to accommodate. Navigate out and it shrinks back.

The preview panel takes whatever's left.

## The hint bar

One last small thing: the hint bar at the bottom of the left panel is pinned to the very last row of the terminal, not floating just below the last entry.

The panel counts how many lines the file list consumed and fills the gap with blank lines so the hint always sits at the floor.

Feels more like a proper pane and less like text that happened to end there.

## What's next

The list is getting shorter:

* Image previews inline✓
* Split-pane file preview✓
* Filter as you type— Bubble Tea'stextinputcomponent frombubblesis sitting there waiting
* Hidden file toggle— show/hide dotfiles

The model grows,Updatehandles new keys,Viewrenders the new state.

That's still the whole pattern. It still scales. The puns still never run dry.

AI agents write code fast. They also silently remove logic, change behavior, and introduce bugs — without telling you. You often find out in production.

git-lrc fixes this. It hooks into git commit and reviews every diff before it lands. 60-second setup. Completely free.

Any feedback or contributors are welcome! It's online, source-available, and ready for anyone to use.

⭐ Star it on GitHub:

## HexmosTech/git-lrc

### Free, Micro AI Code Reviews That Run on Commit

|🇩🇰 Dansk|🇪🇸 Español|🇮🇷 Farsi|🇫🇮 Suomi|🇯🇵 日本語|🇳🇴 Norsk|🇵🇹 Português|🇷🇺 Русский|🇦🇱 Shqip|🇨🇳 中文|

# git-lrc

## Free, Micro AI Code Reviews That Run on Commit

 

 
 
 
 
 
 
 
 

AI agents write code fast. They alsosilently remove logic, change behavior, and introduce bugs -- without telling you. You often find out in production.

git-lrcfixes this.It hooks intogit commitand reviews every diffbeforeit lands. 60-second setup. Completely free.

## See It In Action

See git-lrc catch serious security issues such as leaked credentials, expensive cloud
operations, and sensitive material in log statements

git-lrc-intro-60s.mp4

## Why

* 🤖AI agents silently break things.Code removed. Logic changed. Edge cases gone. You won't notice until production.
* 🔍Catch it before it ships.AI-powered inline comments show youexactlywhat changed and what looks wrong.
* 🔁Build a…

View on GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse