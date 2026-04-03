---
title: GitHub - chenglou/pretext · GitHub
url: https://github.com/chenglou/pretext
site_name: hnrss
content_file: hnrss-github-chengloupretext-github
fetched_at: '2026-03-30T11:26:06.035094'
original_url: https://github.com/chenglou/pretext
date: '2026-03-28'
description: Contribute to chenglou/pretext development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

chenglou

 

/

pretext

Public

* NotificationsYou must be signed in to change notification settings
* Fork596
* Star16k

 
 
 
 
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

265 Commits
265 Commits
.cursor/
rules
.cursor/
rules
 
 
.github/
workflows
.github/
workflows
 
 
accuracy
accuracy
 
 
benchmarks
benchmarks
 
 
corpora
corpora
 
 
pages
pages
 
 
scripts
scripts
 
 
shared
shared
 
 
src
src
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
DEVELOPMENT.md
DEVELOPMENT.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
RESEARCH.md
RESEARCH.md
 
 
STATUS.md
STATUS.md
 
 
TODO.md
TODO.md
 
 
bun.lock
bun.lock
 
 
oxlintrc.json
oxlintrc.json
 
 
package.json
package.json
 
 
thoughts.md
thoughts.md
 
 
tsconfig.build.json
tsconfig.build.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# Pretext

Pure JavaScript/TypeScript library for multiline text measurement & layout. Fast, accurate & supports all the languages you didn't even know about. Allows rendering to DOM, Canvas, SVG and soon, server-side.

Pretext side-steps the need for DOM measurements (e.g.getBoundingClientRect,offsetHeight), which trigger layout reflow, one of the most expensive operations in the browser. It implements its own text measurement logic, using the browsers' own font engine as ground truth (very AI-friendly iteration method).

## Installation

npm install @chenglou/pretext

## Demos

Clone the repo, runbun install, thenbun start, and open the/demosin your browser (no trailing slash. Bun devserver bugs on those)
Alternatively, see them live atchenglou.me/pretext. Some more atsomnai-dreams.github.io/pretext-demos

## API

Pretext serves 2 use cases:

### 1. Measure a paragraph's heightwithout ever touching DOM

import
 
{
 
prepare
,
 
layout
 
}
 
from
 
'@chenglou/pretext'

const
 
prepared
 
=
 
prepare
(
'AGI 春天到了. بدأت الرحلة 🚀'
,
 
'16px Inter'
)

const
 
{
 height
,
 lineCount 
}
 
=
 
layout
(
prepared
,
 
textWidth
,
 
20
)
 
// pure arithmetics. No DOM layout & reflow!

prepare()does the one-time work: normalize whitespace, segment the text, apply glue rules, measure the segments with canvas, and return an opaque handle.layout()is the cheap hot path after that: pure arithmetic over cached widths. Do not rerunprepare()for the same text and configs; that'd defeat its precomputation. For example, on resize, only rerunlayout().

If you want textarea-like text where ordinary spaces,\ttabs, and\nhard breaks stay visible, pass{ whiteSpace: 'pre-wrap' }toprepare():

const
 
prepared
 
=
 
prepare
(
textareaValue
,
 
'16px Inter'
,
 
{
 
whiteSpace
: 
'pre-wrap'
 
}
)

const
 
{
 height 
}
 
=
 
layout
(
prepared
,
 
textareaWidth
,
 
20
)

On the current checked-in benchmark snapshot:

* prepare()is about19msfor the shared 500-text batch
* layout()is about0.09msfor that same batch

We support all the languages you can imagine, including emojis and mixed-bidi, and caters to specific browser quirks

The returned height is the crucial last piece for unlocking web UI's:

* proper virtualization/occlusion without guesstimates & caching
* fancy userland layouts: masonry, JS-driven flexbox-like implementations, nudging a few layout values without CSS hacks (imagine that), etc.
* development timeverification (especially now with AI) that labels on e.g. buttons don't overflow to the next line, browser-free
* prevent layout shift when new text loads and you wanna re-anchor the scroll position

### 2. Lay out the paragraph lines manually yourself

Switch outpreparewithprepareWithSegments, then:

* layoutWithLines()gives you all the lines at a fixed width:

import
 
{
 
prepareWithSegments
,
 
layoutWithLines
 
}
 
from
 
'@chenglou/pretext'

const
 
prepared
 
=
 
prepareWithSegments
(
'AGI 春天到了. بدأت الرحلة 🚀'
,
 
'18px "Helvetica Neue"'
)

const
 
{
 lines 
}
 
=
 
layoutWithLines
(
prepared
,
 
320
,
 
26
)
 
// 320px max width, 26px line height

for
 
(
let
 
i
 
=
 
0
;
 
i
 
<
 
lines
.
length
;
 
i
++
)
 
ctx
.
fillText
(
lines
[
i
]
.
text
,
 
0
,
 
i
 
*
 
26
)

* walkLineRanges()gives you line widths and cursors without building the text strings:

let
 
maxW
 
=
 
0

walkLineRanges
(
prepared
,
 
320
,
 
line
 
=>
 
{
 
if
 
(
line
.
width
 
>
 
maxW
)
 
maxW
 
=
 
line
.
width
 
}
)

// maxW is now the widest line — the tightest container width that still fits the text! This multiline "shrink wrap" has been missing from web

* layoutNextLine()lets you route text one row at a time when width changes as you go:

let
 
cursor
 
=
 
{
 
segmentIndex
: 
0
,
 
graphemeIndex
: 
0
 
}

let
 
y
 
=
 
0

// Flow text around a floated image: lines beside the image are narrower

while
 
(
true
)
 
{

 
const
 
width
 
=
 
y
 
<
 
image
.
bottom
 ? 
columnWidth
 
-
 
image
.
width
 : 
columnWidth

 
const
 
line
 
=
 
layoutNextLine
(
prepared
,
 
cursor
,
 
width
)

 
if
 
(
line
 
===
 
null
)
 
break

 
ctx
.
fillText
(
line
.
text
,
 
0
,
 
y
)

 
cursor
 
=
 
line
.
end

 
y
 
+=
 
26

}

This usage allows rendering to canvas, SVG, WebGL and (eventually) server-side.

### API Glossary

Use-case 1 APIs:

prepare
(
text
: 
string
,
 
font
: 
string
,
 
options
?: 
{
 
whiteSpace
?: 
'normal'
 
|
 
'pre-wrap'
 
}
)
: 
PreparedText
 
// one-time text analysis + measurement pass, returns an opaque value to pass to `layout()`. Make sure `font` is synced with your css `font` declaration shorthand (e.g. size, weight, style, family) for the text you're measuring. `font` is the same format as what you'd use for `myCanvasContext.font = ...`, e.g. `16px Inter`.

layout
(
prepared
: 
PreparedText
,
 
maxWidth
: number
,
 
lineHeight
: number
)
: 
{
 
height
: 
number
,
 
lineCount
: 
number
 
}
 
// calculates text height given a max width and lineHeight. Make sure `lineHeight` is synced with your css `line-height` declaration for the text you're measuring.

Use-case 2 APIs:

prepareWithSegments
(
text
: 
string
,
 
font
: 
string
,
 
options
?: 
{
 
whiteSpace
?: 
'normal'
 
|
 
'pre-wrap'
 
}
)
: 
PreparedTextWithSegments
 
// same as `prepare()`, but returns a richer structure for manual line layouts needs

layoutWithLines
(
prepared
: 
PreparedTextWithSegments
,
 
maxWidth
: number
,
 
lineHeight
: number
)
: 
{
 
height
: 
number
,
 
lineCount
: 
number
,
 
lines
: 
LayoutLine
[
]
 
}
 
// high-level api for manual layout needs. Accepts a fixed max width for all lines. Similar to `layout()`'s return, but additionally returns the lines info

walkLineRanges
(
prepared
: 
PreparedTextWithSegments
,
 
maxWidth
: number
,
 
onLine
: 
(
line
: 
LayoutLineRange
)
 
=
>
 
void
)
: 
number
 
// low-level api for manual layout needs. Accepts a fixed max width for all lines. Calls `onLine` once per line with its actual calculated line width and start/end cursors, without building line text strings. Very useful for certain cases where you wanna speculatively test a few width and height boundaries (e.g. binary search a nice width value by repeatedly calling walkLineRanges and checking the line count, and therefore height, is "nice" too. You can have text messages shrinkwrap and balanced text layout this way). After walkLineRanges calls, you'd call layoutWithLines once, with your satisfying max width, to get the actual lines info.

layoutNextLine
(
prepared
: 
PreparedTextWithSegments
,
 
start
: 
LayoutCursor
,
 
maxWidth
: number
)
: 
LayoutLine
 
|
 
null
 
// iterator-like api for laying out each line with a different width! Returns the LayoutLine starting from `start`, or `null` when the paragraph's exhausted. Pass the previous line's `end` cursor as the next `start`.

type
 
LayoutLine
 
=
 
{

 
text
: string 
// Full text content of this line, e.g. 'hello world'

 
width
: number 
// Measured width of this line, e.g. 87.5

 
start
: 
LayoutCursor
 
// Inclusive start cursor in prepared segments/graphemes

 
end
: 
LayoutCursor
 
// Exclusive end cursor in prepared segments/graphemes

}

type
 
LayoutLineRange
 
=
 
{

 
width
: number 
// Measured width of this line, e.g. 87.5

 
start
: 
LayoutCursor
 
// Inclusive start cursor in prepared segments/graphemes

 
end
: 
LayoutCursor
 
// Exclusive end cursor in prepared segments/graphemes

}

type
 
LayoutCursor
 
=
 
{

 
segmentIndex
: 
number
 
// Segment index in prepareWithSegments' prepared rich segment stream

 
graphemeIndex
: number 
// Grapheme index within that segment; `0` at segment boundaries

}

Other helpers:

clearCache
(
)
: 
void
 
// clears Pretext's shared internal caches used by prepare() and prepareWithSegments(). Useful if your app cycles through many different fonts or text variants and you want to release the accumulated cache

setLocale
(
locale
?: 
string
)
: 
void
 
// optional (by default we use the current locale). Sets locale for future prepare() and prepareWithSegments(). Internally, it also calls clearCache(). Setting a new locale doesn't affect existing prepare() and prepareWithSegments() states (no mutations to them)

## Caveats

Pretext doesn't try to be a full font rendering engine (yet?). It currently targets the common text setup:

* white-space: normal
* word-break: normal
* overflow-wrap: break-word
* line-break: auto
* If you pass{ whiteSpace: 'pre-wrap' }, ordinary spaces,\ttabs, and\nhard breaks are preserved instead of collapsed. Tabs follow the default browser-styletab-size: 8. The other wrapping defaults stay the same:word-break: normal,overflow-wrap: break-word, andline-break: auto.
* system-uiis unsafe forlayout()accuracy on macOS. Use a named font.
* Because the default target includesoverflow-wrap: break-word, very narrow widths can still break inside words, but only at grapheme boundaries.

## Develop

SeeDEVELOPMENT.mdfor the dev setup and commands.

## Credits

Sebastian Markbage first planted the seed withtext-layoutlast decade. His design — canvasmeasureTextfor shaping, bidi from pdf.js, streaming line breaking — informed the architecture we kept pushing forward here.

## About

 No description, website, or topics provided.
 

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

16k

 stars
 

### Watchers

52

 watching
 

### Forks

596

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript89.4%
* HTML10.6%