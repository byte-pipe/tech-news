---
title: Pele · Mermaid diagrams as themeable SVG
url: https://pele.run/
site_name: hackernews_api
content_file: hackernews_api-pele-mermaid-diagrams-as-themeable-svg
fetched_at: '2026-10-18T14:17:54.701648'
original_url: https://pele.run/
author: dchest
date: '2026-10-17'
description: Pele is a lightweight open source library that renders Mermaid diagrams to SVG, themed with CSS variables.
tags:
- hackernews
- trending
---

# Pele is a lightweightopen sourcelibrary that rendersMermaiddiagrams to SVG,themed with CSS variables.

Write Mermaid syntax, Pele renders it to SVG. Try editing the example below.

Mermaid
1
flowchart
 
TD
2
 
A
[
Mermaid text
]
 
-->
 
B
{
Flowchart?
}
3
 
B
 
--
 Yes 
-->
 
C
[
Pele
]
4
 
B
 
--
 No 
-->
 
D
[
Mermaid
]
5
 
C
 
-->
 
E
([
SVG
])
6
 
D
 
-->
 
E
Pele
Open in 
Playground
Yes
No
Mermaid text
Flowchart?
Pele
Mermaid
SVG

Use CSS variables to set colors and fonts. Color changes apply without re-rendering.

CSS
1
.pele 
{
2
 
--pele-bg
: 
#fffcf0
;
3
 
--pele-fg
: 
#100f0f
;
4
 
--pele-muted
: 
#6f6e69
;
5
 
--pele-line
: 
#100f0f
;
6
 
--pele-surface
: 
#f2f0e5
;
7
 
--pele-surface-alt
: 
#e6e4d9
;
8
 
--pele-border
: 
#cecdc3
;
9
}
Pele
Themes
Variables
Light
Dark
Pele
Mermaid.js
Bundle size 
gzip
230 kB
1.6 MB
Render time
0.05–0.3 ms
6–82 ms
Direct dependencies
0
23
Small screens
Adapts the layout
Scales the diagram
Theming
CSS variables
Theme configuration

Add Pele to your app using theAPI.

npm
pnpm
yarn
bun
1
npm
 install pele
1
pnpm
 add pele
1
yarn
 add pele
1
bun
 add pele

Pass Mermaid syntax torender()and insert the returned SVG into your page.

1
import
 
{
 
render
 
}
 
from
 
'
pele
'
;
2
3
const
 
{
 
svg
 
}
 
=
 
render
(
`
flowchart LR
4
 A[Mermaid text] --> B[SVG]
`
)
;
5
6
document
.
querySelector
(
'
#diagram
'
)
.
innerHTML
 
=
 
svg
;