---
title: GitHub - yukiyokotani/office-open-xml-viewer · GitHub
url: https://github.com/yukiyokotani/office-open-xml-viewer
site_name: hnrss
content_file: hnrss-github-yukiyokotanioffice-open-xml-viewer-github
fetched_at: '2026-06-08T11:00:28.375924'
original_url: https://github.com/yukiyokotani/office-open-xml-viewer
date: '2026-06-07'
description: Contribute to yukiyokotani/office-open-xml-viewer development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

yukiyokotani

 

/

office-open-xml-viewer

Public

* NotificationsYou must be signed in to change notification settings
* Fork5
* Star172

 
 
 
 
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

854 Commits
854 Commits
.github/
workflows
.github/
workflows
 
 
.storybook
.storybook
 
 
docs/
images
docs/
images
 
 
packages
packages
 
 
rule-tests
rule-tests
 
 
rules
rules
 
 
site
site
 
 
src
src
 
 
tests/
smoke
tests/
smoke
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
mise.toml
mise.toml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
sgconfig.yml
sgconfig.yml
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.lib.json
tsconfig.lib.json
 
 
vite.config.ts
vite.config.ts
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

This entire codebase — Rust parsers, TypeScript renderers, tests, and tooling — was implemented byClaude(Anthropic's AI assistant) through iterative prompting. No human-written application code exists in this repository.

# office-open-xml-viewer

Demo (Storybook)

A browser-based viewer for Office Open XML documents that renders to an HTML Canvas element.
The parsers are written in Rust and compiled to WebAssembly; the renderers use the Canvas 2D API.
Each format also exposes a headless engine (DocxDocument/XlsxWorkbook/PptxPresentation) that renders into any caller-supplied canvas, so you can compose your own UI — scroll views, thumbnail grids, master-detail panes — instead of being locked into the built-in viewer. See theExamplessection inthe Storybook demo.

DOCX

XLSX

PPTX

npm install @silurus/ooxml

#
 or

pnpm add @silurus/ooxml

Bundler note: this package embeds.wasmfiles. With Vite addvite-plugin-wasm; with webpack useexperiments.asyncWebAssembly.

Bundle size note: the package is ESM-only (.mjs). npm'sUnpacked Sizesums all four entry bundles, including theopt-inmath engine (MathJax + STIX Two Math, ~3 MB). What actually lands in your app is much smaller — import only the format you need (e.g.@silurus/ooxml/pptx). The math engine is aseparate entry(@silurus/ooxml/math): it is bundledonly if you import it and pass it to a viewer(seeRendering equations). Viewers that never receive amathengine — and all xlsx usage — tree-shake the ~3 MB away entirely.

## Quick Start

import
 
{
 
DocxViewer
 
}
 
from
 
'@silurus/ooxml/docx'
;

import
 
{
 
XlsxViewer
 
}
 
from
 
'@silurus/ooxml/xlsx'
;

import
 
{
 
PptxViewer
 
}
 
from
 
'@silurus/ooxml/pptx'
;

// DOCX — caller provides the <canvas>

const
 
canvas
 
=
 
document
.
getElementById
(
'docx-canvas'
)
 
as
 
HTMLCanvasElement
;

const
 
docx
 
=
 
new
 
DocxViewer
(
canvas
)
;

await
 
docx
.
load
(
'/document.docx'
)
;

docx
.
nextPage
(
)
;

// XLSX — viewer manages its own <canvas> + tab bar

const
 
container
 
=
 
document
.
getElementById
(
'xlsx-container'
)
 
as
 
HTMLElement
;

const
 
xlsx
 
=
 
new
 
XlsxViewer
(
container
)
;

await
 
xlsx
.
load
(
'/workbook.xlsx'
)
;

// PPTX — caller provides the <canvas>

const
 
canvas
 
=
 
document
.
getElementById
(
'pptx-canvas'
)
 
as
 
HTMLCanvasElement
;

const
 
pptx
 
=
 
new
 
PptxViewer
(
canvas
)
;

await
 
pptx
.
load
(
'/deck.pptx'
)
;

pptx
.
nextSlide
(
)
;

### Rendering equations

OMML equations (m:oMath/m:oMathPara) in.docx/.pptxare rendered withMathJax+STIX Two Math.
That engine is ~3 MB, so it isopt-in: import themathengine from the separate@silurus/ooxml/mathentry and pass it to the viewer. Pass it and equations render;
omit it and the engine is referenced nowhere, so a bundlertree-shakes the ~3 MB
away entirely(equations are simply skipped). It is fully self-contained: no
network, no cross-origin requests.

import
 
{
 
DocxViewer
 
}
 
from
 
'@silurus/ooxml/docx'
;

import
 
{
 
math
 
}
 
from
 
'@silurus/ooxml/math'
;

const
 
canvas
 
=
 
document
.
getElementById
(
'docx-canvas'
)
 
as
 
HTMLCanvasElement
;

const
 
docx
 
=
 
new
 
DocxViewer
(
canvas
,
 
{
 math 
}
)
;
 
// ← equations now render

await
 
docx
.
load
(
'/paper-with-equations.docx'
)
;

The samemathengine works forPptxViewerand the headlessDocxDocument/PptxPresentationAPIs (which takemathin their options). xlsx has no equation
support and never references the engine.

Architecture diagram

flowchart TB
 subgraph build["🦀 Build-time (Rust → WebAssembly)"]
 direction LR
 docx_rs["packages/docx/parser/src/lib.rs"]
 xlsx_rs["packages/xlsx/parser/src/lib.rs"]
 pptx_rs["packages/pptx/parser/src/lib.rs"]
 docx_rs -- wasm-pack --> docx_wasm["docx_parser.wasm"]
 xlsx_rs -- wasm-pack --> xlsx_wasm["xlsx_parser.wasm"]
 pptx_rs -- wasm-pack --> pptx_wasm["pptx_parser.wasm"]
 end

 subgraph browser["🌐 Runtime (Browser)"]
 subgraph core_pkg["@silurus/ooxml-core (shared primitives)"]
 CORE["renderChart · resolveFill · applyStroke\nbuildCustomPath · autoResize · shared types"]
 end
 subgraph docx_pkg["@silurus/ooxml · docx"]
 DV["DocxViewer"] --> DD["DocxDocument"]
 DD --> DW["worker.ts\n〈Web Worker — parse only〉"]
 DD --> DR["renderer.ts\n〈Canvas 2D — main thread〉"]
 end
 subgraph xlsx_pkg["@silurus/ooxml · xlsx"]
 XV["XlsxViewer"] --> XB["XlsxWorkbook"]
 XB --> XW["worker.ts\n〈Web Worker — parse only〉"]
 XB --> XR["renderer.ts\n〈Canvas 2D — main thread〉"]
 end
 subgraph pptx_pkg["@silurus/ooxml · pptx"]
 PV["PptxViewer"] --> PP["PptxPresentation"]
 PP --> PW["worker.ts\n〈Web Worker — parse only〉"]
 PP --> PR["renderer.ts\n〈Canvas 2D — main thread〉"]
 end
 DR -. uses .-> CORE
 XR -. uses .-> CORE
 PR -. uses .-> CORE
 end

 docx_wasm --> DW
 xlsx_wasm --> XW
 pptx_wasm --> PW
 DR --> canvas["&lt;canvas&gt;"]
 XR --> canvas
 PR --> canvas

 
Loading

All three formats follow the same shape: the worker parses the.docx/.xlsx/.pptxarchive via WASM and posts a JSON model back to the main thread, where the renderer draws to the canvas. Rendering stays on the main thread so the canvas shares the document'sFontFaceSet— anOffscreenCanvasin a worker has its own font registry and would silently fall back to a system font, producing subtly different text measurements (and wrap positions) from the installed theme webfonts.@silurus/ooxml-coreholds the cross-format primitives that the three renderers all depend on: a unified chart renderer (bar / line / area / radar / waterfall), shape helpers (resolveFill,applyStroke,buildCustomPath,hexToRgba), theautoResizeviewer utility, and the shared type definitions.

### Key files

File

Role

packages/docx/parser/src/lib.rs

Rust WASM parser — DOCX ZIP → 
Document
 JSON

packages/xlsx/parser/src/lib.rs

Rust WASM parser — XLSX ZIP → 
Workbook
 JSON

packages/pptx/parser/src/lib.rs

Rust WASM parser — PPTX ZIP → 
Presentation
 JSON

packages/docx/src/renderer.ts

Canvas 2D rendering engine with text layout (main thread)

packages/xlsx/src/renderer.ts

Canvas 2D rendering engine with virtual scroll (main thread)

packages/pptx/src/renderer.ts

Canvas 2D rendering engine (main thread)

packages/*/src/worker.ts

Web Worker: WASM init and parsing only (one per format)

packages/*/src/viewer.ts

Public Viewer API — canvas lifecycle, navigation

packages/core/src/index.ts

Cross-format primitives — chart renderer, shape helpers, 
autoResize
, shared types

## Framework Examples

React 19

// React 19.1 — vite-plugin-wasm required in vite.config.ts

import
 
{
 
useEffect
,
 
useRef
,
 
useState
 
}
 
from
 
'react'
;

import
 
{
 
PptxViewer
 
}
 
from
 
'@silurus/ooxml/pptx'
;

export
 
function
 
PptxViewerComponent
(
{
 src 
}
: 
{
 
src
: 
string
 
}
)
 
{

 
const
 
canvasRef
 
=
 
useRef
<
HTMLCanvasElement
>
(
null
)
;

 
const
 
viewerRef
 
=
 
useRef
<
PptxViewer
 
|
 
null
>
(
null
)
;

 
const
 
[
slide
,
 
setSlide
]
 
=
 
useState
(
{
 
current
: 
0
,
 
total
: 
0
 
}
)
;

 
useEffect
(
(
)
 
=>
 
{

 
const
 
canvas
 
=
 
canvasRef
.
current
;

 
if
 
(
!
canvas
)
 
return
;

 
const
 
viewer
 
=
 
new
 
PptxViewer
(
canvas
,
 
{

 
onSlideChange
: 
(
i
,
 
total
)
 
=>
 
setSlide
(
{
 
current
: 
i
,
 total 
}
)
,

 
}
)
;

 
viewerRef
.
current
 
=
 
viewer
;

 
viewer
.
load
(
src
)
;

 
}
,
 
[
src
]
)
;

 
return
 
(

 
<
div
>

 
<
canvas
 
ref
=
{
canvasRef
}
 
style
=
{
{
 
width
: 
800
 
}
}
 
/>

 
<
button
 
onClick
=
{
(
)
 
=>
 
viewerRef
.
current
?.
prevSlide
(
)
}
>
‹ Prev
</
button
>

 
<
span
>
 
{
slide
.
current
 
+
 
1
}
 / 
{
slide
.
total
}
 
</
span
>

 
<
button
 
onClick
=
{
(
)
 
=>
 
viewerRef
.
current
?.
nextSlide
(
)
}
>
Next ›
</
button
>

 
</
div
>

 
)
;

}

Vue 3.5

<!--
 Vue 3.5 — useTemplateRef is a 3.5+ feature 
-->

<
script
 setup lang="ts">

import
 { 
useTemplateRef
, 
onMounted
, 
ref
 } 
from
 
'
vue
'
;

import
 { 
PptxViewer
 } 
from
 
'
@silurus/ooxml/pptx
'
;

const
 props 
=
 
defineProps
<{ src
:
 
string
 }>();

const
 canvas 
=
 
useTemplateRef
<
HTMLCanvasElement
>(
'
canvas
'
);

let
 viewer
:
 
PptxViewer
 
|
 
null
 
=
 
null
;

const
 current 
=
 
ref
(
0
);

const
 total 
=
 
ref
(
0
);

onMounted
(
async
 () 
=>
 {

 
viewer
 
=
 
new
 
PptxViewer
(
canvas
.
value
!
, {

 
onSlideChange
: (
i
, 
t
) 
=>
 { 
current
.
value
 
=
 
i
; 
total
.
value
 
=
 
t
; },

 });

 
await
 
viewer
.
load
(
props
.
src
);

});

</
script
>

<
template
>
 <
div
>
 <
canvas
 
ref
=
"
canvas
"
 
style
=
"
width
: 
800
px
"
 />
 <
button
 
@click
=
"
viewer?.prevSlide()
"
>‹ Prev</
button
>
 <
span
> {{ current + 1 }} / {{ total }} </
span
>
 <
button
 
@click
=
"
viewer?.nextSlide()
"
>Next ›</
button
>
 </
div
>
</
template
>

Angular 19

// Angular 19 — standalone component with signal-based state

import
 
{

 
Component
,
 
ElementRef
,
 
viewChild
,

 
signal
,
 
AfterViewInit
,

}
 
from
 
'@angular/core'
;

import
 
{
 
PptxViewer
 
}
 
from
 
'@silurus/ooxml/pptx'
;

@
Component
(
{

 
selector
: 
'app-pptx-viewer'
,

 
standalone
: 
true
,

 
template
: 
`

 <div>

 <canvas #canvas style="width: 800px"></canvas>

 <button (click)="prev()">‹ Prev</button>

 <span> {{ current() + 1 }} / {{ total() }} </span>

 <button (click)="next()">Next ›</button>

 </div>

 `
,

}
)

export
 
class
 
PptxViewerComponent
 
implements
 
AfterViewInit
 
{

 
canvasEl
 
=
 
viewChild
.
required
<
ElementRef
<
HTMLCanvasElement
>
>
(
'canvas'
)
;

 
current
 
=
 
signal
(
0
)
;

 
total
 
=
 
signal
(
0
)
;

 
private
 
viewer
?: 
PptxViewer
;

 
ngAfterViewInit
(
)
: 
void
 
{

 
this
.
viewer
 
=
 
new
 
PptxViewer
(
this
.
canvasEl
(
)
.
nativeElement
,
 
{

 
onSlideChange
: 
(
i
,
 
t
)
 
=>
 
{
 
this
.
current
.
set
(
i
)
;
 
this
.
total
.
set
(
t
)
;
 
}
,

 
}
)
;

 
this
.
viewer
.
load
(
'/deck.pptx'
)
;

 
}

 
prev
(
)
: 
void
 
{
 
this
.
viewer
?.
prevSlide
(
)
;
 
}

 
next
(
)
: 
void
 
{
 
this
.
viewer
?.
nextSlide
(
)
;
 
}

}

Add"allowSyntheticDefaultImports": trueand configure@angular-builders/custom-webpack(or useesbuildbuilder) with WASM support in your Angular workspace.

Svelte 5

<!-- Svelte 5 — runes syntax ($props, $state) -->

<
script
 
lang
=
"
ts
"
>

 
import
 { 
onMount
 } 
from
 
'
svelte
'
;

 
import
 { 
PptxViewer
 } 
from
 
'
@silurus/ooxml/pptx
'
;

 
let
 { src }
:
 { src
:
 
string
 } 
=
 
$props
();

 
let
 canvas
:
 
HTMLCanvasElement
;

 
let
 viewer
:
 
PptxViewer
;

 
let
 current 
=
 
$state
(
0
);

 
let
 total 
=
 
$state
(
0
);

 
onMount
(
async
 () 
=>
 {

 
viewer
 
=
 
new
 
PptxViewer
(
canvas
, {

 
onSlideChange
: (
i
, 
t
) 
=>
 { 
current
 
=
 
i
; 
total
 
=
 
t
; },

 });

 
await
 
viewer
.
load
(
src
);

 });

</
script
>

<
div
>
 <
canvas
 
bind:this
={
canvas
} 
style
=
"
width: 800px
"
></
canvas
>
 <
button
 
onclick
={() 
=>
 
viewer
?.
prevSlide
()}>‹ Prev</
button
>
 <
span
> {
current
 
+
 
1
} / {
total
} </
span
>
 <
button
 
onclick
={() 
=>
 
viewer
?.
nextSlide
()}>Next ›</
button
>
</
div
>

SolidJS 1.9

// SolidJS 1.9

import
 
{
 
createSignal
,
 
onMount
,
 
onCleanup
 
}
 
from
 
'solid-js'
;

import
 
{
 
PptxViewer
 
}
 
from
 
'@silurus/ooxml/pptx'
;

export
 
function
 
PptxViewerComponent
(
props
: 
{
 
src
: 
string
 
}
)
 
{

 
let
 
canvasEl
!
: 
HTMLCanvasElement
;

 
let
 
viewer
: 
PptxViewer
 
|
 
undefined
;

 
const
 
[
current
,
 
setCurrent
]
 
=
 
createSignal
(
0
)
;

 
const
 
[
total
,
 
setTotal
 
]
 
=
 
createSignal
(
0
)
;

 
onMount
(
async
 
(
)
 
=>
 
{

 
viewer
 
=
 
new
 
PptxViewer
(
canvasEl
,
 
{

 
onSlideChange
: 
(
i
,
 
t
)
 
=>
 
{
 
setCurrent
(
i
)
;
 
setTotal
(
t
)
;
 
}
,

 
}
)
;

 
await
 
viewer
.
load
(
props
.
src
)
;

 
}
)
;

 
onCleanup
(
(
)
 
=>
 
{
 
/* viewer?.destroy?.() */
 
}
)
;

 
return
 
(

 
<
div
>

 
<
canvas
 
ref
=
{
canvasEl
}
 
style
=
{
{
 
width
: 
'800px'
 
}
}
 
/>

 
<
button
 
onClick
=
{
(
)
 
=>
 
viewer
?.
prevSlide
(
)
}
>
‹ Prev
</
button
>

 
<
span
>
 
{
current
(
)
 
+
 
1
}
 / 
{
total
(
)
}
 
</
span
>

 
<
button
 
onClick
=
{
(
)
 
=>
 
viewer
?.
nextSlide
(
)
}
>
Next ›
</
button
>

 
</
div
>

 
)
;

}

Qwik 2

// Qwik 2.0 — dynamic import to keep WASM out of SSR bundle

import
 
{
 
component$
,
 
useSignal
,
 
useVisibleTask$
 
}
 
from
 
'@builder.io/qwik'
;

import
 
type
 
{
 
PptxViewer
 
as
 
PptxViewerType
 
}
 
from
 
'@silurus/ooxml/pptx'
;

export
 
const
 
PptxViewerComponent
 
=
 
component$
<
{
 
src
: 
string
 
}
>
(
(
{
 src 
}
)
 
=>
 
{

 
const
 
canvasRef
 
=
 
useSignal
<
HTMLCanvasElement
>
(
)
;

 
const
 
current
 
=
 
useSignal
(
0
)
;

 
const
 
total
 
=
 
useSignal
(
0
)
;

 
let
 
viewer
: 
PptxViewerType
 
|
 
undefined
;

 
// useVisibleTask$ runs only in the browser, never during SSR

 
useVisibleTask$
(
async
 
(
)
 
=>
 
{

 
if
 
(
!
canvasRef
.
value
)
 
return
;

 
const
 
{
 PptxViewer 
}
 
=
 
await
 
import
(
'@silurus/ooxml/pptx'
)
;

 
viewer
 
=
 
new
 
PptxViewer
(
canvasRef
.
value
,
 
{

 
onSlideChange
: 
(
i
,
 
t
)
 
=>
 
{
 
current
.
value
 
=
 
i
;
 
total
.
value
 
=
 
t
;
 
}
,

 
}
)
;

 
await
 
viewer
.
load
(
src
)
;

 
}
)
;

 
return
 
(

 
<
div
>

 
<
canvas
 
ref
=
{
canvasRef
}
 
style
=
{
{
 
width
: 
'800px'
 
}
}
 
/>

 
<
button
 
onClick$
=
{
(
)
 
=>
 
viewer
?.
prevSlide
(
)
}
>
‹ Prev
</
button
>

 
<
span
>
 
{
current
.
value
 
+
 
1
}
 / 
{
total
.
value
}
 
</
span
>

 
<
button
 
onClick$
=
{
(
)
 
=>
 
viewer
?.
nextSlide
(
)
}
>
Next ›
</
button
>

 
</
div
>

 
)
;

}
)
;

## Feature Support

### Word (.docx)

Category

Feature

Status

Document

Page rendering

✅

Page size and margins

✅

Headers / footers (default / first / even)

✅

Section breaks (continuous / nextPage / oddPage / evenPage)

✅

Text

Paragraphs

✅

Bold, italic, underline, strikethrough

✅

Font family, size, color

✅

Hyperlinks

✅

Superscript / subscript (
w:vertAlign
)

✅

Ruby annotations / furigana (
w:ruby
)

✅

Formatting

Paragraph alignment (left/center/right/justify)

✅

Line spacing (auto / atLeast / exact)

✅

Line grid (
w:docGrid
, §17.6.5)

✅

Margin collapsing between paragraphs

✅

Indents and tab stops

✅

Lists (bullet and numbered)

✅

Paragraph styles (Heading 1–9, Normal, custom)

✅

Table style 
w:pPr
 cascade (§17.7.6)

✅

Table style borders / shading / banding (
tblStylePr
, 
cnfStyle
, §17.4.7)

✅

Table of contents (TOC field) — dot leaders, right-aligned page numbers

✅

keepNext / keepLines / widowControl

✅

Elements

Tables (with borders, fills, merges, banding, alignment)

✅

Math equations (OMML 
m:oMath
 / 
m:oMathPara
, rendered via MathJax — opt-in 
@silurus/ooxml/math
)

✅

Images (inline and anchored, with text wrap)

✅

Text boxes / drawing shapes

✅

WMF / EMF metafile images (legacy vector)

❌ Not planned

Advanced

Footnote / endnote reference markers

✅

Track changes (
w:ins
 / 
w:del
 — author-coloured underline / strikethrough)

✅

Comments / footnote bodies (parsed, not yet rendered inline)

⚠️

Mail merge fields

❌ Not planned

Interaction

Text selection (transparent overlay, native copy)

✅

### Excel (.xlsx)

Category

Feature

Status

Workbook

Multiple sheets, sheet names

✅

Sheet tab colors (
<sheetPr><tabColor>
 — theme / tint / indexed / rgb)

✅

Cells

Text, number, boolean, error values

✅

Formula results (from cached 
<v>
)

✅

Dates (ECMA-376 date format codes)

✅

Rich text (per-run formatting)

✅

Formatting

Bold, italic, underline (
single
 / 
double
 / 
singleAccounting
 / 
doubleAccounting
), strikethrough

✅

Superscript / subscript (
vertAlign
)

✅

Font family, size, color

✅

Cell background color (solid + gradient)

✅

Pattern fills (
gray125
 / 
gray0625
 / 
lightGray
 / 
mediumGray
 / 
darkGray
 and the 12 
light*
 / 
dark*
 directional hatches)

✅

Borders (thin, medium, thick, hair, double, dashed, dotted, dashDotDot, …)

✅

Diagonal borders (
diagonalUp
 / 
diagonalDown
, single + double)

✅

Horizontal / vertical alignment

✅

Text wrapping

✅

Number formats (
0.00
, 
%
, 
#,##0
, custom date/time)

✅

Structure

Merged cells

✅

Frozen panes

✅

Row / column sizing (custom widths and heights)

✅

Hidden rows / columns

✅

Elements

Images (
<xdr:twoCellAnchor>
)

✅

Drawing shapes / text boxes (
xdr:sp
, 
xdr:txBody
)

✅

Charts (bar, line, area, radar, scatter / bubble)

✅

Chart markers (circle / square / diamond / triangle / x / plus / star / dot / dash, per-point 
<c:dPt>
 overrides)

✅

Chart data labels (
<c:dLbl>
 per-point with CELLRANGE / VALUE / SERIESNAME / CATEGORYNAME field references, position 
l
/
r
/
t
/
b
/
ctr
/
outEnd
)

✅

Chart error bars (
<c:errBars>
 X/Y direction, 
cust
 / 
fixedVal
 / 
stdErr
 / 
stdDev
 / 
percentage
, dashed/styled lines)

✅

Chart manual layout (
<c:title><c:layout>
 and 
<c:plotArea><c:layout>
)

✅

Sparklines (
x14:sparklineGroup
 — line / column / win-loss, with markers and high/low/first/last/negative highlights)

✅

Advanced

Conditional formatting (
cellIs
, 
colorScale
, 
dataBar
, 
iconSet
, 
top10
, 
aboveAverage
)

✅

Slicers (static, Office 2010 extension)

✅

Pivot tables

❌ Not planned

Data validation / comments

❌ Not planned

Interaction

Cell selection (single / range / row / column / all)

✅

Excel-style row / column header highlight on selection

✅

Shift+click to extend, Ctrl+C to copy as TSV

✅

Text selection inside cells (transparent overlay)

✅

onSelectionChange
 callback, 
getCellAt(x, y)
 API

✅

Zoom slider (Excel-style, right of the tab bar, 10–400% with 100% centered; 
showZoomSlider
 option)

✅

### PowerPoint (.pptx)

Category

Feature

Status

Slides

Slide rendering

✅

Slide layout / master inheritance

✅

Slide size (custom dimensions)

✅

Slide background (solid, gradient, image)

✅

Slide numbers

✅

Notes pages

❌

Animations / transitions

❌ Not planned

Element types

Shapes (
sp
)

✅

Pictures (
pic
)

✅

Groups (
grpSp
) with nested transforms

✅

Connectors (
cxnSp
)

✅

Tables (
tbl
 in 
graphicFrame
)

✅

Charts (bar, line, area, radar, waterfall)

✅

Charts (pie, doughnut)

✅

Charts (scatter — 
scatterStyle
 marker / line / smooth variants)

✅

Charts (bubble — 
bubbleSize
 per-point area scaling)

✅

SmartArt

❌

OLE objects

❌

Video / audio (poster + interactive playback)

✅

Ink / handwriting (
p:contentPart
, raster fallback)

✅

Shape geometry

130+ preset shapes (
prstGeom
)

✅

Custom geometry (
custGeom
) on shapes and pictures (clipping)

✅

Rotation and flip (flipH / flipV)

✅

3D preset shapes

❌

Fills

Solid fill (
solidFill
)

✅

Linear / radial gradient (
gradFill
)

✅

No fill (
noFill
)

✅

Pattern fill (
pattFill
) — 30 preset bitmaps incl. pct5–pct90 / horz / vert / cross / diag / grid / brick / check / trellis

✅

Image fill on shapes (
blipFill
 in 
sp
)

✅

Strokes

Solid line color and width

✅

Dash / dot styles

✅

Arrow heads (
headEnd
 / 
tailEnd
)

✅

Compound / double lines (`<a:ln cmpd="dbl

thinThick

Shape effects

Drop shadow (
outerShdw
)

✅

Glow (
glow
 — radius + colour)

✅

Inner shadow (
innerShdw
 — parsed; rendering follow-up)

⚠️

Soft edge (
softEdge
 — parsed; rendering follow-up)

⚠️

Reflection (
reflection
 — parsed; rendering follow-up)

⚠️

Bevel / 3D extrusion

❌

Text — characters

Bold, italic, strikethrough (incl. 
dblStrike
)

✅

Underline styles (
sng
 / 
dbl
 / 
dotted
 / 
dash
 / 
dashLong
 / 
dotDash
 / 
dotDotDash
 / 
wavy
 / 
wavyDbl
 and 
*Heavy
 variants)

✅

Per-run underline colour (
uFill
 / 
uFillTx
)

✅

Font family, size, color

✅

East Asian font (
rPr > a:ea
 — separate typeface for CJK glyphs)

✅

Caps transform (
all
 / 
small
)

✅

Letter spacing (
spc
)

✅

Superscript / subscript

✅

Hyperlinks (
hlinkClick
 — theme 
hlink
 colour + auto underline)

✅

Text shadow (
rPr > effectLst > outerShdw
)

✅

Text outline (
rPr > a:ln
)

✅

Math equations (OMML 
m:oMath
 / 
m:oMathPara
, incl. 
a14:m
 / 
mc:AlternateContent
; STIX Two Math via MathJax — opt-in 
@silurus/ooxml/math
)

✅

Text — paragraphs

Horizontal alignment (left / center / right / justify)

✅

Vertical anchor (top / center / bottom)

✅

Line spacing (
spcPct
, 
spcPts
)

✅

Space before / after paragraph

✅

Bullet points (character and auto-numbered)

✅

Tab stops

✅

Indent / margin

✅

Vertical text (
bodyPr@vert
 — vert / vert270 / eaVert)

✅

Right-to-left paragraph (
pPr@rtl
 — Arabic / Hebrew default alignment + browser bidi)

✅

Text — body

Text padding (insets)

✅

normAutoFit (shrink to fit)

✅

spAutoFit (expand box; suppresses wrap when text fits in one line)

✅

Word wrap / no wrap

✅

Multi-column text body (
numCol
 / 
spcCol
 — balanced flow)

✅

Theme object-default inheritance (
<a:objectDefaults><a:txDef|spDef>
 bodyPr fallback)

✅

Tables

Cells, rows, columns

✅

Cell merges (horizontal / vertical)

✅

Cell borders

✅

Cell fills (solid / gradient)

✅

Cell diagonal lines (
lnTlToBr
 / 
lnBlToTr
)

✅

Table theme styles (74 built-in PowerPoint presets)

✅

Theme

Scheme colors (dk1/lt1/accent1–6)

✅

Font scheme (
+mj-lt
, 
+mn-lt
)

✅

lumMod / lumOff / alpha transforms

✅

Interaction

Text selection (transparent overlay, native copy)

✅

A note on text selection.Across DOCX / PPTX / XLSX, text selection is currently implemented by rendering glyphs to the canvas while overlaying a transparent DOM layer that mirrors the canvas text positions for native browser selection. This dual-layer approach is a deliberate stop-gap: once the CanvasdrawElementAPI(proposed inWICG/html-in-canvas, currently in Chromium Origin Trial) ships across browsers, the project plans to migrate to a single DOM-as-source-of-truth pipeline where the canvas mirrors the DOM directly — eliminating the duplication while keeping z-order correctness and native selection / a11y.

## Companion packages

* packages/markdown/—@silurus/ooxml-markdownand theooxml-mdCLI convert.pptx/.docx/.xlsxto GitHub-flavoured markdown via the workspace WASM parsers. Same projection used by the MCP server (~21× smaller than the raw XML on the demo deck, ~8% bigger than a flat-text extractor). Includes a node20-based GitHub Action for bulk repo-wide conversion.
* packages/node/— Node-side parsers (@silurus/ooxml-node) exposingparsePptx/parseDocx/parseXlsx/parseXlsxAllSheetsagainst the workspace WASM artifacts, with no DOM or Web Worker dependency. Useful for CI checks, headless rendering pipelines, and CLI tools. Includes anooxml-thumbnailCLI (pptx-only first pass; requiresskia-canvas).
* packages/vscode-extension/— VS Code extension (ooxml-viewer) that registersCustomEditorProviders for.docx,.xlsx, and.pptx, and (opt-in) auto-installs and registers theooxml-mcp-serverso AI coding agents in the same window (Copilot Agent mode, Claude, …) can read those files via dedicated tools.
* packages/mcp-server/— Rust MCP server (ooxml-mcp-server) exposing the parsers as tools for AI agents (Claude, Copilot, Codex, etc.). Provides structured queries (docx_get_structure,xlsx_get_cell_range,pptx_get_slide_structure, …) so agents can inspect OOXML files without shelling out tounzip. Prebuilt binaries are attached to eachGitHub Releasefor macOS / Linux / Windows; the VS Code extension downloads them on demand.

## Development

#
 Install dependencies

pnpm install

#
 Build all WASM parsers (requires Rust + wasm-pack)

pnpm build:wasm

#
 Start Storybook dev server (port 6006)

pnpm storybook

#
 Type-check all packages

pnpm typecheck

#
 Run visual regression tests (local only — not run in CI)

pnpm vrt

#
 Adopt the current rendering as the new reference baseline

UPDATE_REFS=1 pnpm vrt

#
 Build the library

pnpm build

### WASM build (individual packages)

cd
 packages/docx/parser 
&&
 wasm-pack build --target web 
&&
 cp pkg/docx_parser_bg.wasm pkg/docx_parser.js ../src/wasm/

cd
 packages/xlsx/parser 
&&
 wasm-pack build --target web 
&&
 cp pkg/xlsx_parser_bg.wasm pkg/xlsx_parser.js ../src/wasm/

cd
 packages/pptx/parser 
&&
 wasm-pack build --target web 
&&
 cp pkg/pptx_parser_bg.wasm pkg/pptx_parser.js ../src/wasm/

## Security & Privacy

* Canvas-only rendering.Documents are decoded and drawn to anHTMLCanvasElement. No script, link, form, or other active content from the source file is executed or injected into the DOM.
* ZIP decompression cap.Each entry in the source archive is limited to 512 MiB of uncompressed output by default to block zip-bomb DoS. Override per viewer withmaxZipEntryBytes(bytes) — raise it for legitimate decks with large embedded media, lower it to tighten the budget for untrusted input:newPptxViewer(canvas,{maxZipEntryBytes:64*1024*1024});// 64 MiBSupported uniformly byDocxViewer,PptxViewer, andXlsxViewer. Zero / negative values fall back to the default.
* No network by default.The library does not send telemetry or analytics, and does not contact third-party services unless you ask it to. In particular, theme webfonts (and Office font metric substitutes for XLSX) arenotloaded from Google Fonts unless you passuseGoogleFonts: trueto the relevantViewer/load(...)options — supported uniformly byDocxViewer,PptxViewer, andXlsxViewer. Enabling that option causes the end-user's browser to send an HTTP request (IP and User-Agent) tofonts.googleapis.com, which may have GDPR implications for your application — consider self-hosting the required fonts via@font-faceinstead.
* XML parsing.Usesroxmltree, which does not resolve external entities (XXE-safe by default).

## License

MIT

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

172

 stars
 

### Watchers

0

 watching
 

### Forks

5

 forks
 

 Report repository

 

## Releases71

v0.50.1

 Latest

 

Jun 4, 2026

 

+ 70 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript49.8%
* Rust45.6%
* Astro2.1%
* JavaScript0.9%
* HTML0.5%
* CSS0.4%
* Other0.7%