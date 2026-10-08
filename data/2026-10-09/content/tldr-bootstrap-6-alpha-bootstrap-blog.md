---
title: Bootstrap 6 Alpha | Bootstrap Blog
url: https://blog.getbootstrap.com/2026/10/08/bootstrap-6-alpha
site_name: tldr
content_file: tldr-bootstrap-6-alpha-bootstrap-blog
fetched_at: '2026-10-09T10:16:31.043633'
original_url: https://blog.getbootstrap.com/2026/10/08/bootstrap-6-alpha
author: Mark Otto
date: '2026-10-09'
description: Today we’re releasing the first alpha version of Bootstrap 6, a major overhaul to the project that modernizes and expands one of the most prolific open source…
tags:
- tldr
---

On this page…

##### On this page

Today we’re releasing the first alpha version of Bootstrap 6, a major overhaul to the project that modernizes and expands one of the most prolific open source design systems of all time. It’s been incredibly fun and rewarding to work on this over the past year, and I’m excited to share it with you.

Bootstrap 6 has been modernized from the ground up with the Sass module system, support for more native browser APIs and elements, ESM-only JavaScript plugins, and a slew of new CSS standards. We’ve broken this post into separate entries that we’ll publish one-by-one, starting with an overview of v6 and a spotlight on our new Sass & CSS implementation.

## Hold up…

You’re probably asking yourself, “Wtf, new Bootstrap? What is this, 2015?” And I don’t blame you. It’s been all quiet on the Bootstrap front for a long time while I’ve focused onPierre, especially with our work onDiffs,Trees, andCode Storage.

Throughout all of that, I’ve had several nagging ideas for Bootstrap despite humans not writing any more code thanks to AI. And yes, there are tons of design libraries from amazing developers now. Still, the reason we made Bootstrap in the first place has never been more relevant.

To help people build more software, faster and easier.

There’s never been more people building software than today, and I imagine that will continue to be true every day, for the rest of our lives. It’s already been installed over 1.75 billion times since its release in 2011. So, Bootstrap 6 is here to continue being an open source design system for anyone—human or AI, novice or pro.

We hope you love it, and thanks to everyone who’s supported the project over the years.

## Community appreciation

Before we get to the good parts, I want to thank my co-maintainer,Julien, for all the amazing work he’s put into Bootstrap over the last couple of years. Without him, I’d be underwater on reviews, dependencies, migrations, and more. He’s an absolute legend and Bootstrap owes him a tremendous amount of gratitude and appreciation.

Huge thanks to everyone who contributed to the v6 development branch as well:

@julien-deramond@coliff@pricop@ThomasLandauer@Rishikesh183@pardeyke@meenalsingh0@ifer47@Hashim1999164@fauzan171@claudiob@aljojoby9@VividLemon@cccabinet@Rawal27@jonnysp@kwy404@andreas-venturini

And most importantly, thanks to everyone who has backed Bootstrap onOpen Collectiveand every contributor who filed an issue, sent a patch, or argued with me in a pull request.

## Get started

Bootstrap 6 Alpha 1 is on npm and jsDelivr right now.

npm
 i
 bootstrap@6.0.0-alpha.1

Or grab it from the CDN. Be mindful that our JavaScript is ESM-only in v6, so the<script>tag needstype="module".

<
link
 href
=
"https://cdn.jsdelivr.net/npm/bootstrap@6.0.0-alpha.1/dist/css/bootstrap.min.css"
 rel
=
"stylesheet"
>

<
script
 type
=
"module"
 src
=
"https://cdn.jsdelivr.net/npm/bootstrap@6.0.0-alpha.1/dist/js/bootstrap.bundle.min.js"
></
script
>

Then read ourInstallorQuickstartpages. If you’re coming from v5, read the next section first, then themigration guide.

## Modern browser support

130+

130+

132+

18+

Bootstrap 6 requires Chrome and Edge 130, Firefox 132, and Safari 18.For comparison, v5 supported browsers as far back as Chrome and Firefox 60 and Safari 12. This new support floor is because we’re building with browser features that weren’t available a few years ago:light-dark(),:has(), container queries,oklch(),color-mix(), the native<dialog>element, and more. This means v6 includes no fallbacks, prefixes, or polyfills below that floor.

This doesn’t get us features like CSS Anchor Positioning, full pretty text support, or contrast color in Safari yet, but we expect to have a v7 sooner than our past major releases.

Bootstrap 5 remains available and supported if that floor doesn’t work for your project. v5.4.0 will be released as soon as we can before we share an end of life date for Bootstrap 5.

## Spotlight: CSS-first Sass modules

Updating Bootstrap to use Sass modules was a massive undertaking that couldn’t happen in v5 without some breaking changes. So we went big in v6.

Bootstrap 6 uses the@use/@forwardmodule system, andcustomization now happens via token maps. Sass is still used forprogrammaticcustomization (generating component variants, utilities, functions, etc), while allvisualcustomization happens with CSS.

Token mapsare Sass maps that house all our CSS variables for both global settings in:rootand on our individual components. This normalizes the path to customizing and focuses Bootstrap on the future of CSS, with a strong preprocessor foundation for managing large codebases. Nearly every Sass variable from v5 is now a CSS variable in a token map. This also means you can customize Bootstrap’s CSS variables at runtime, rather than just before compilation.

Here’s howthis approachlooks in a component likealert:

$alert-tokens
:
 ()
 !default
;

$alert-tokens
:
 defaults
(

 (

 --alert-padding-x
:
 var
(
--spacer
)
,

 --alert-border-radius
:
 var
(
--radius-5
)
,

 --alert-bg
:
 var
(
--theme-bg-subtle
,
 var
(
--bg-1
))
,

 // …

 ),

 $alert-tokens

);

@layer components 
{

 .
alert
 {

 @
include
 tokens
(
$alert-tokens
);

 // Rest of alert styles…

 }

}

Practically speaking, this means that virtually all our Sass variables from v5 are now CSS variables in a token map. The handful of remaining global Sass options now live in_config.scss,_colors.scss, and_theme.scss.

At the:rootlevel where we emit the most tokens programmatically with Sass functions:

$root-tokens
:
 ()
 !default
;

$root-tokens
:
 defaults
(

 (

 // Individually set CSS variables…

 )

 $root-tokens

);

// Most root tokens are loop-generated

@
each
 $key
, 
$value
 in
 $theme-bgs
 {

 $root-tokens
:
 map
.
set
(
$root-tokens
,
 --bg
-
#{
$key
},
 $value
);

}

Thedefaults()function ensures anyone who adds new tokens to a token map, or overrides an existing token value, gets just that in their output—a new CSS variable or a new value for an existing one. It merges rather than replaces, so you never have to redeclare a map to change one value in it, and you can add tokens of your own alongside ours. Speaking of, here’s how to customize those tokens in the new module system with token maps.

Import Bootstrap via@use ... withand start modifying un-namespaced token maps. You can override root tokens with the$root-tokensmap; components get their own unique token map named after the component. Additionally, this is how you customize the few global Sass variables we have left.

@
use
 "../node_modules/bootstrap/scss/bootstrap"
 with
 (

 // Manage global options

 $enable-smooth-scroll
:
 true,

 // Move the entire radius scale by changing its base

 $radius
:
 .25
rem
,

 // Modify global tokens

 $root-tokens
:
 (

 --spacer
: 
1.5
rem
,

 --focus-ring-width
: 
3
px
,

 )
,

 // Modify component tokens

 $alert-tokens
:
 (

 --alert-padding-x
: 
calc
(
var
(
--spacer
)
 *
 2
)
,

 --alert-border-radius
: 
var
(
--radius-8
)
,

 )
,

);

Notice that the tokens have nobsprefix here. In v5 the prefix was a Sass variable,$prefix, threaded through every declaration. In v6 we write custom properties unprefixed in the source and add the namespace with PostCSS at build time, so$prefixis gone and you configure the prefix in your PostCSS config instead.

The$radiusline is worth calling out, too. Our radius scale is derived from a single base value, so changing that one number moves all ten steps together and every component that reads them follows. Same story for$spacerand the spacing scale.

This gives us the most flexible system possible using both Sass and CSS, with the advantage of customizing either before or after compilation. Update global tokens in the browser, and downstream components update in real time. This is a massive improvement over v5’s hybrid Sass-CSS system, and one I hope you’ll love.

Radius
0.5rem
Spacer
1rem
Primary
Button
A token change reaches every component at once.

### Card

Padding follows the spacer, corners follow the radius.

CSS
.
token-demo
 {

 --bs-radius-5
:
 0.5
rem
;

 --bs-spacer
:
 1
rem
;

 --bs-primary-base
:
 var
(
--bs-blue-500
);

 --bs-primary-bg
:
 var
(
--bs-primary-base
);

 --bs-primary-bg-subtle
:
 light-dark(
var
(
--bs-blue-100
),
 var
(
--bs-blue-900
)
)
;

 --bs-primary-fg
:
 light-dark(
var
(
--bs-blue-600
),
 var
(
--bs-blue-400
)
)
;

 --bs-primary-border
:
 light-dark(
var
(
--bs-blue-300
),
 var
(
--bs-blue-600
)
)
;

}

## Prefixes

A super obvious and breaking change in v6 is moving from the infix to a prefix for our responsive utilities and component variants. Yes, this is a direct copy of how Tailwind does responsive, and yes, it’s better than what felt like a randomly positioned infix in v5.

Here’s a look at the before and after on some Bootstrap classes:

* .d-md-noneis now.md:d-none
* .col-lg-6is now.lg:col-6
* .opacity-50-hoveris now.hover:opacity-50
* .justify-content-md-endis now.md:justify-content-end
* .offcanvas-mdis now.md:drawer(rename intentional)

This change applies to all utilities, components, grid layouts, and more. It also include state modifiers like:hover,:focus, etc. Same ergonomics for all of them.

If you have custom Sass built on our breakpoint helpers,breakpoint-infix()is nowbreakpoint-prefix()and returns a prefix string, and theloop-breakpoints-upandloop-breakpoints-downmixins expose$prefixinstead of$infix.

## Modernizing

Bootstrap 6 has been overhauled to use as many of the latest browser-native features as possible, alongside updated build tooling. This makes Bootstrap more accessible, easier to customize, and primed for future browser updates. Alongside that, we’ve rewritten our source Sass around the modern module system and newer versions of Dart Sass.@importis deprecated and no longer supported for customization; use@useand@forwardinstead.

Sass files have also been reorganized, and several Sass files have been removed given the change to CSS variables for all visual customization, automatic color-mode adaptivity vialight-dark(), and more. We’ve also cleaned up the shenanigans around the_maps.scssfile,_variables.scssand_variables-dark.scss, both of which are no more.

On the HTML and CSS side of things, some highlights include:

* CSS layersfor predictable specificity across the entire framework, includingutilitiesas the top-most layer.
* oklch() colorsandcolor-mix()for perceptually uniform, themeable color palettes that automatically adjust to base color changes.
* light-dark()for native color mode support without duplicating styles and in the same property-value pairing.
* Range media querieslike(width >= 768px)replacing min-width/max-width hacks.
* Container queriesfor responsive design that adapts to the parent element instead of just the viewport. Includes mixins, helpers, and per-component changes.
* Native<details>and<summary>powering the accordion—no JavaScript needed
* Native<dialog>element behind the new Dialog component
* :where()selector to reduce specificity in complex selectors
* content-visibilitywithallow-discretetransitions, plusinterpolate-sizeand the::details-contentpseudo-element, so the accordion animates open and closed in pure CSS. Height animation on a disclosure widget used to mean measuring elements in JavaScript.
* @propertyto register the custom properties composed by our utility API as non-inheriting, preventing their values from leaking into children.

On the JS and tooling side:

* ESM-only plugins.There’s no UMD bundle and nowindow.bootstrapglobal anymore. What this means for you depends entirely on how you use our JavaScript, so here are the three cases.If you only use data attributes likedata-bs-toggle, addtype="module"to your script tag and you’re done—everything else keeps working.If you call our APIs from a CDN build, switch to an explicit import:import { Tooltip } from './bootstrap.bundle.min.js'.For modern ESM-based bundlers like Vite, Webpack, or Parcel, existing imports continue to work—import { Tooltip } from 'bootstrap'now tree shakes correctly whilesideEffectsmetadata preserves Data API listeners. Projects using CommonJSrequire()must migrate to ESM imports.
* If you only use data attributes likedata-bs-toggle, addtype="module"to your script tag and you’re done—everything else keeps working.
* If you call our APIs from a CDN build, switch to an explicit import:import { Tooltip } from './bootstrap.bundle.min.js'.
* For modern ESM-based bundlers like Vite, Webpack, or Parcel, existing imports continue to work—import { Tooltip } from 'bootstrap'now tree shakes correctly whilesideEffectsmetadata preserves Data API listeners. Projects using CommonJSrequire()must migrate to ESM imports.
* TypeScript.Our source is.tsnow, and we ship our own type declarations, so you can delete@types/bootstrapfrom your dependencies. Deep imports likebootstrap/js/src/alert.jsstill resolve.
* Rolldownreplaces both Rollup and Babel in our tooling. It strips TypeScript types and lowers syntax itself, removing an entire layer of build tooling from the repo. This only affects you if you build Bootstrap from source.
* Vitestrunning in real Chromium through Playwright, which replaced Karma.
* Astro 7for the docs, which has a new search experience with Pagefind, new pages, and updated navigation and layout.

## Built for humans and agents

Bootstrap 6 includes LLM-friendly documentation and skill files for all your agentic coding needs.

To be more efficient with agents, we have text-only versions of our documentation.llms.txtis a curated index of every documentation page with descriptions whilellms-full.txtis all of our documentation concatenated into one file.

Skills files have been added to the repositoryin a newskills/directory. Skills are playbooks for specific tasks, in this case for working with Bootstrap 6. To start, we’ve drafted skill files for migrating to v6, using Bootstrap with different build tools, authoring components, and more. Point your agent at the relevant file and it’ll follow the correct guidance from us maintainers instead of anything potentially outdated or incorrect.

## Two more things…

We’ve also updated the blog and Icons site with refreshed designs.

* The blog has a new homepage, search via Pagefind, new category pages, and new post layouts like the one you’re reading now.
* The Icons site has a new homepage, too—immediately oriented around the grid of icons. We’ve added search with PageFind here as well (including?tag=queries), new sidebar category navigation and category pages, plus a refreshed icon show page.

In addition, we’ve built out a new, private repository and package for sharing Bootstrap docs components across the main site, Icons, and Blog. It’s called@twbs/buiand gives us better control as maintainers over all the separate sites without having to fully commit to a monorepo.

## What’s next

This is an alpha, so things can still meaningfully change before beta. There will be more alphas before we start stabilizing through the beta and RC stages. Share any and all feedback you have and we’ll do our best to address:

* Use the v6 feedback category inGitHub Discussionsif you have a general question or feedback on the v6 release.
* File an issue inGitHub Issuesif you have a specific bug or feature request.
* Open apull requestwith your changes (it’s always a good idea to review in a discussion or issue first so we don’t waste anyone’s time!)

Thanks again to everyone who contributed, thanks for reading, and we hope you love Bootstrap 6!