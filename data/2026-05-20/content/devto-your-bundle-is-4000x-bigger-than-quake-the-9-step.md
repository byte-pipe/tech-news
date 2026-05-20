---
title: Your bundle is 4000x bigger than Quake. The 9-step audit that fixes it. - DEV Community
url: https://dev.to/thegdsks/your-bundle-is-4000x-bigger-than-quake-the-9-step-audit-that-fixes-it-5cpb
site_name: devto
content_file: devto-your-bundle-is-4000x-bigger-than-quake-the-9-step
fetched_at: '2026-05-20T12:02:55.701344'
original_url: https://dev.to/thegdsks/your-bundle-is-4000x-bigger-than-quake-the-9-step-audit-that-fixes-it-5cpb
author: GDS K S
date: '2026-05-14'
description: In February 2026 a developer named daivuk shipped a playable Quake-like first person shooter in a 64... Tagged with webdev, performance, javascript, tutorial.
tags: '#webdev, #performance, #javascript, #tutorial'
---

Tactical deletions for Next.js and Vite

In February 2026 a developer named daivuk shipped a playable Quake-like first person shooter in a 64 kilobyte Windows executable. Multiple levels, four enemy types, textures, music, the whole game. The trick was not magic. He wrote a custom language and a custom virtual machine because the standard toolchain shipped too many features he did not use. Two extra kilobytes of generic runtime would have killed the fourth level.

That story sat with me for a week, because almost every web app I open is 30 to 60 times the size of QUOD. The page you are reading right now, by the time it finishes loading on Dev.to, weighs more than four hundred copies of QUOD running at once. The marketing page for the framework your app is built on is heavier than QUOD by three orders of magnitude. We have collectively forgotten what bytes cost.

This article is the audit playbook I use when a Next.js or Vite project crosses my desk and the Lighthouse score reads orange. Nine steps, in the exact order, with the commands, the expected output, and the typical wins. Everything you need to cut your bundle by 50 to 90 percent in a single afternoon. No "rewrite in Rust" theater. Just deletions.

## TL;DR

Step

What you run

Typical win

1. Baseline

npx next build
 then read the output table

knowing where you stand

2. Visualise

@next/bundle-analyzer
 or 
rollup-plugin-visualizer

the map

3. Kill date libraries

swap 
moment
 for 
date-fns
 or native 
Intl

50 to 90 KB

4. Kill icon sets

one import per icon, never the full pack

20 to 200 KB

5. Kill lodash

swap 
lodash
 for 
lodash-es
 or native

60 to 80 KB

6. Audit polyfills

drop IE 11 support; target ES2022

30 to 100 KB

7. Code-split routes

dynamic imports for non-critical pages

100 KB to 1 MB

8. Replace images

AVIF or modern WebP, properly sized

200 KB to 2 MB

9. Re-baseline

run step 1 again, write the number down

confidence

The numbers in the table come from documented case studies on web.dev, the HTTP Archive 2025 annual report, and the Vercel Next.js docs. Your mileage will vary. The order will not.

## 1. Baseline

You cannot improve what you have not measured. Before you touch anything, get an honest number.

# Next.js

npx next build

# read the "First Load JS" table at the bottom

# Vite

npx vite build

# read the dist/ output sizes

Enter fullscreen mode

Exit fullscreen mode

The number you want is "First Load JS shared by all," and then your largest individual route. Write both down. This number will be your accountability for the rest of the audit. If it does not go down by at least 30 percent by step 9, you skipped something or you have a genuinely small project, which is fine, you are done.

The HTTP Archive's 2025 annual web almanac reports a median JavaScript transfer size of 612 KB on desktop and 555 KB on mobile. If your number is meaningfully bigger than that, you have low hanging fruit. If it is meaningfully smaller, you are already ahead of most of the industry.

## 2. Visualise the bundle

A list of files is not a map. You need the map.

# Next.js

npm 
install
 
--save-dev
 @next/bundle-analyzer

# in next.config.js wrap your config with the analyzer

ANALYZE
=
true 
npm run build

# Vite

npm 
install
 
--save-dev
 rollup-plugin-visualizer

# add it to vite.config.ts

npx vite build

Enter fullscreen mode

Exit fullscreen mode

The analyzer opens a treemap in your browser. The treemap is the entire audit's source of truth. Every fat block is a question. Every question is one of the next seven steps.

Spend ten minutes here. Hover the rectangles. Find the ones that are unfamiliar. The ones you cannot explain are the ones that have the most byte fat.

## 3. Kill the date library

The single most common bundle bloat in the entire JavaScript ecosystem. Moment.js is 67 KB minified before gzip. day.js is 7 KB. date-fns with tree shaking can drop to 12 KB. NativeIntl.DateTimeFormatis zero.

// before

import
 
moment
 
from
 
'
moment
'

const
 
formatted
 
=
 
moment
(
date
).
format
(
'
YYYY-MM-DD
'
)

// after, native, zero bytes added

const
 
formatted
 
=
 
new
 
Intl
.
DateTimeFormat
(
'
en-CA
'
).
format
(
date
)

// or with date-fns, tree shakes cleanly

import
 
{
 
format
 
}
 
from
 
'
date-fns
'

const
 
formatted
 
=
 
format
(
date
,
 
'
yyyy-MM-dd
'
)

Enter fullscreen mode

Exit fullscreen mode

Run a global grep formomentanddayjsin your codebase. If you find moment, you have a 50 to 90 KB win sitting on the floor. The migration is mechanical and well documented.

## 4. Kill the icon set import

The second most common bundle bloat, especially in dashboards built on Material UI, Chakra, or any "we have icons" library. The trap is the default import.

// before, ships the entire icon set

import
 
{
 
Search
,
 
User
,
 
Menu
 
}
 
from
 
'
@mui/icons-material
'

// after, ships only the three icons

import
 
Search
 
from
 
'
@mui/icons-material/Search
'

import
 
User
 
from
 
'
@mui/icons-material/Person
'

import
 
Menu
 
from
 
'
@mui/icons-material/Menu
'

Enter fullscreen mode

Exit fullscreen mode

The default barrel import in many icon packs is the entire 2 MB of SVG. The per-icon import path ships only what you reference. Material UI's documentation explicitly warns about this. Many teams ignore it. Check yours.

For Lucide, Heroicons, theSVG and Phosphor, tree-shaking generally works correctly if your bundler is set up right. Verify it in the analyzer. If you see the full icon library in your treemap, the tree shake did not happen and you need to fix the import path.

## 5. Kill the utility library

Lodash is 70 KB. Most apps use seven functions from it. The fix is eitherlodash-eswith tree shaking, or replacing the seven functions with native equivalents.

// before

import
 
_
 
from
 
'
lodash
'

const
 
grouped
 
=
 
_
.
groupBy
(
items
,
 
'
category
'
)

const
 
unique
 
=
 
_
.
uniq
(
ids
)

// after, native

const
 
grouped
 
=
 
Object
.
groupBy
(
items
,
 
item
 
=>
 
item
.
category
)

const
 
unique
 
=
 
[...
new
 
Set
(
ids
)]

// or, tree shaken

import
 
groupBy
 
from
 
'
lodash-es/groupBy
'

import
 
uniq
 
from
 
'
lodash-es/uniq
'

Enter fullscreen mode

Exit fullscreen mode

Object.groupByshipped in 2024 and is widely available.Map.groupByis also there. The Set constructor handles uniqueness in one line. Underscore is even worse than lodash for the same reason. Check your dependency tree, find them, replace them, save bytes.

## 6. Audit the polyfill load

If your project supports browsers older than the last two years of Chrome, Safari, and Firefox, you are shipping polyfills you do not need. The.browserslistrcorbrowserslistfield in package.json governs this.

//
 
package.json
 
before

"browserslist"
:
 
[
"> 0.5%"
,
 
"last 2 versions"
,
 
"Firefox ESR"
,
 
"not dead"
]

//
 
package.json
 
after,
 
modern
 
targets
 
only

"browserslist"
:
 
[
"last 2 chrome versions"
,
 
"last 2 firefox versions"
,

 
"last 2 safari versions"
,
 
"last 2 edge versions"
]

Enter fullscreen mode

Exit fullscreen mode

The wins here vary by project. A React app that explicitly targets IE 11 ships about 50 KB more than the same app targeting last-two-versions. Vue and Svelte have similar ratios. Check the analyzer forcore-js,regenerator-runtime,@babel/runtime. Each of those is a polyfill bundle, and each shrinks meaningfully when you raise the target.

The honest tradeoff: if you serve enterprise customers stuck on Internet Explorer, you cannot do this. Almost everyone else can.

## 7. Code split by route

The biggest single lever. Most apps load every component on every page because the bundler does not know which routes need what. The fix is dynamic imports for non-critical paths.

// before, eager import

import
 
HeavyDashboard
 
from
 
'
./HeavyDashboard
'

// after, lazy

import
 
{
 
lazy
,
 
Suspense
 
}
 
from
 
'
react
'

const
 
HeavyDashboard
 
=
 
lazy
(()
 
=>
 
import
(
'
./HeavyDashboard
'
))

function
 
App
()
 
{

 
return 
(

 
<
Suspense
 
fallback
=
{
<
Spinner
 
/>
}
>

 
<
HeavyDashboard
 
/>

 
</
Suspense
>

 
)

}

Enter fullscreen mode

Exit fullscreen mode

In Next.js the App Router does most of this automatically per route. The wins come from splitting heavy components inside a route. A chart library, a markdown editor, a video player, a payment SDK. Each of those is a candidate.

Run the analyzer again after this step. The shared bundle should drop by 100 KB to a megabyte, depending on what you split. The page-specific bundles will be larger, but only loaded when needed.

## 8. Replace your images

Almost forgot the part where pictures of food account for 70 percent of the bytes on the average e-commerce page.

The 2026 image stack is straightforward. Serve AVIF with a WebP fallback and a JPEG fallback. Size them to the actual display dimensions, not the original camera resolution. Use the native<picture>element or a framework wrapper likenext/image.

<picture>

 
<source
 
srcset=
"hero.avif"
 
type=
"image/avif"
>

 
<source
 
srcset=
"hero.webp"
 
type=
"image/webp"
>

 
<img
 
src=
"hero.jpg"
 
alt=
"..."
 
width=
"1200"
 
height=
"630"
 
loading=
"lazy"
>

</picture>

Enter fullscreen mode

Exit fullscreen mode

The width and height attributes prevent layout shift and give the browser an early hint. The loading=lazy attribute defers off-screen images. The AVIF source typically shaves 30 to 50 percent off the file size compared to JPEG at the same quality.

A typical e-commerce site that does the full image audit drops its page weight by a megabyte or two. That single change moves Lighthouse scores more than the previous six steps combined.

## 9. Re-baseline and write the number down

Run step 1 again. Write the new number next to the old one. Compare.

If you ran all eight changes on a typical Next.js app with one heavy dashboard, an icon library, lodash, and unoptimized images, you should see the First Load JS drop from a starting point of 400 to 600 KB down to 100 to 200 KB. The Lighthouse performance score should jump 20 to 40 points. The Time to Interactive should fall by a full second on a throttled mid-range Android device.

If you did not get those wins, one of two things happened. Either your app is already lean, in which case congratulations, or you skipped a step. Run the analyzer again and find the rectangle that is still too big.

## The framework you can actually keep

The nine steps above are a one-time audit. The hard part is keeping the wins after the audit ends. Three rules I run on every project:

Rule 1: A bundle budget 
in 
CI.
 Bundle size has to be a number 
in 
a green or red box on every PR.
 npm 
install
 
--save-dev
 bundlewatch
 Add it to your 
test 
script. Set a max. Fail the build on regression.

Rule 2: A dependency review on every PR that touches package.json.
 Use the @sentry/bundle-analyzer or @next/bundle-analyzer 
in 
CI.
 Post the diff as a comment. The team will see it. The team will care.

Rule 3: A monthly 
"what got fat"
 report.
 Once a month, run the analyzer and look at the biggest rectangles.
 One of them will surprise you. Fix it.

Enter fullscreen mode

Exit fullscreen mode

Without these three rules the wins drift back inside six months. With them, the bundle stays at the size you decided it should be at the audit, indefinitely.

## The honest take

You are not going to ship your next SaaS in 64 KB. Nobody is asking you to. But the lesson from QUOD is not about the absolute number, it is about the constraint mindset. The standard toolchain ships every feature you do not use. Every dependency is a vote against your users on a slow connection. Every imported icon set is a tax on the laptop battery of the person reading your page on a flight.

The good news is that the audit pays back in hours, not weeks. The first time I ran this playbook on a real codebase, I cut a 540 KB First Load JS down to 168 KB in one afternoon. The before and after Lighthouse score difference would have taken six months of "performance work" if I had done it gradually. Doing it all in one focused sweep is dramatically faster.

The next time you reach for a 4 MB library to format a date, think about QUOD. Then think about whether your users would rather download your full app, or four hundred copies of QUOD running at the same time, with guns in them.

Question for the comments: what is the biggest single byte win you ever shipped, and what tool did you replace?

GDS K S·thegdsks.com· follow on X@thegdsks

Every byte in your bundle is a tiny vote against your users on a slow connection.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse