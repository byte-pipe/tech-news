---
title: 'Fixing Delicate Cache Mismatches in a Brownfield SPA: A Pragmatic Solution - DEV Community'
url: https://dev.to/devteam/fixing-delicate-cache-mismatches-in-a-brownfield-spa-a-pragmatic-solution-dk9
site_name: devto
content_file: devto-fixing-delicate-cache-mismatches-in-a-brownfield-s
fetched_at: '2026-08-31T23:08:54.947883'
original_url: https://dev.to/devteam/fixing-delicate-cache-mismatches-in-a-brownfield-spa-a-pragmatic-solution-dk9
author: Ben Halpern
date: '2026-08-31'
description: How we eliminated subtle stylesheet caching glitches during deployments on DEV without a massive rewrite. Tagged with webdev, architecture, webperf, rails.
tags: '#webdev, #architecture, #webperf, #rails'
---

Details Forem's tricky edge-caching deployment fix

Building in public often means talking about shiny new features, but in mature production applications, the most critical engineering work is usuallybrownfield problem solving—iterating on top of years and years of code logic and/or production system decisions.

OnDEV(powered by the open-sourceForemcodebase), we have a hybrid architecture that blends Rails server rendering, Fastly edge caching, and lightweight client-side navigation (viaInstantClick). This setup delivers sub-100ms page transitions, but partial page swaps combined with aggressive edge caching create delicate deployment challenges.

We shipped a fixPR #23789which helps solve for an inherently delicate caching mismatch issue in web navigation. This is something that has existed practically since the beginning of DEV, and we have had several flakey fixes for the problem at times, but I feel good about this being a step in the right direction — albeit not a perfectly complete fix by any means.

## The Problem: Cache Mismatches Across Deployments

When we deploy new CSS updates, Rails generates new asset digest hashes (e.g.,views-v2.cssreplacesviews-v1.css).

1. Full Page Load:A user loads an updated homepage. The browser receives full HTML and loads the latestv2stylesheets in<head>.
2. Internal Navigation (Partial Page Swap):The user clicks an article link. Rather than performing a full browser reload, InstantClick requests the article in the background and swaps only the inner#page-contentcontainer into the existing DOM.
3. The Edge Cache Trap:DEV aggressively caches article HTML fragments at Fastly with surrogate keys. Many articles were cachedbeforethe latest deploy, meaning the cached HTML fragment still referencedv1stylesheets.

### Why the Previous Solution Was Fragile

To prevent pages from rendering with outdated CSS, we had previously added client-side logic to inspect the incoming page's expected stylesheet paths and swap<link rel="stylesheet">elements in the DOM dynamically.

In practice, this was brittle:

* When navigating from the fresh homepage (v2) to an older edge-cached article (v1), the client script comparedcurrentHref (v2) !== expectedHref (v1).
* It assumed the incoming page represented the "target" state and initiated aninvoluntary downgradeof the DOM back tov1stylesheets.
* Ifv1asset files had been pruned after deployment, the browser failed with 404s; if they loaded, new UI components suddenly broke because their updated CSS was ripped out mid-session.
* Attempting to asynchronously swap multiple stylesheet tags across both<head>and<body>introduced CSS cascade race conditions and flashes of unstyled content (FOUC).

## The Solution: Repurposing Internal Navigation Parameters

Instead of treating this as a client-side DOM mutation problem, we realized it was fundamentally acache partitioning problem.

For years, Forem has quietly passed an internal query parameter—?i=i—on background AJAX requests so Rails knows to render a lightweight partial layout instead of the full HTML document shell.

InPR #23789, we repurposed this parameter:

1. Combined Style Fingerprinting:On initial full-page load, Rails computes a deterministic 10-character hash from the combined digests of the core stylesheets (minimal,views, andcrayons) and places it on<body>asdata-style-fingerprint:

 
<body
 
...
 
data-style-fingerprint=
"cc9ed033eb"
>

Enter fullscreen mode

Exit fullscreen mode

1. Parameterizing Internal Navigation:When InstantClick preloads or fetches a link, it reads the active session's fingerprint and appends it to the internal URL:

 https://dev.to/user/post?i=cc9ed033eb

Enter fullscreen mode

Exit fullscreen mode

(Ifdata-style-fingerprintis missing—such as on tabs open during deploy cutover—it gracefully falls back to?i=i).

1. Natural Cache Partitioning at Fastly:Fastly's edge configuration already whitelistsiin its safe parameter list. Because the query parameter is part of the cache key:* When a user on av2session requests/post?i=v2_fingerprint, Fastly checks for a cachedv2fragment.
* If missing, Fastly fetches a fresh fragment from Rails compiled withv2styles.
* Stalev1cached fragments are simply bypassed and eventually expire naturally.
2. Deleting the DOM Swapping Logic:With cache partitioning in place, incoming partial fragments are guaranteed to match the active DOM's stylesheet version. Wecompletely deletedthe client-side stylesheet replacement script. The browser's active<link>tags remain static throughout the user session.

## Brownfield Development Takeaways

1. Solve at the Cache Layer, Not the DOM Layer:Trying to coordinate DOM mutations, asynchronous CSS loading, and cascade precedence in client-side JavaScript is almost always more fragile than letting the edge cache serve the right HTML version from the start.
2. Repurpose Existing Primitives:We didn't need a new router, an edge computing rewrite, or custom HTTP headers. Repurposing our existing?i=...internal parameter gave us exact cache keying with zero extra infrastructure overhead.
3. Pragmatic Improvements Over Perfect Rewrites:This fix doesn't magically prevent every theoretical edge-case during rolling deploys, but it definitively solves the most disruptive issue. The system is far less delicate, and we now have a clean, predictable pattern to build upon.

Happy coding!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse