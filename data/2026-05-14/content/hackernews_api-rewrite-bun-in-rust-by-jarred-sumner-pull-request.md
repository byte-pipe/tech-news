---
title: 'Rewrite Bun in Rust by Jarred-Sumner · Pull Request #30412 · oven-sh/bun · GitHub'
url: https://github.com/oven-sh/bun/pull/30412
site_name: hackernews_api
content_file: hackernews_api-rewrite-bun-in-rust-by-jarred-sumner-pull-request
fetched_at: '2026-05-14T19:35:05.875536'
original_url: https://github.com/oven-sh/bun/pull/30412
author: Chaoses
date: '2026-05-14'
description: 'Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one - Rewrite Bun in Rust by Jarred-Sumner · Pull Request #30412 · oven-sh/bun'
tags:
- hackernews
- trending
---

oven-sh

 

/

bun

Public

* NotificationsYou must be signed in to change notification settings
* Fork4.5k
* Star90.2k

## Conversation

 

Collaborator

### Jarred-SumnercommentedMay 8, 2026•edited

Blog post with details coming soon.

It passes Bun's pre-existing test suite on all platforms (and fixes several memory leaks and flaky tests), the binary size shrinks by 3 MB - 8 MB, the benchmarks are between neutral and faster - and most importantly, we now have compiler-assisted tools for catching & preventing memory bugs, which have costed the team an enormous amount of development & debugging time over the years.

The codebase is otherwise largely the same. The same architecture, the same data structures. Bun still uses few 3rd party libraries. No async rust.

To try this, run:

bun upgrade --canary

Please do file issues if you run into any. If this thread gets crazy I will lock it.

Note:

* Still some optimization work to do before this lands in non-canary version.
* Still some cleanup work to do (which will come in a series of follow-up PRs)

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
👍

856

 
Arron-Stothart, theoparis, nitish-singh07, Vanilagy, grok-rs, shashank-100, omerbenamram, jmjoy, Gawc1uuu, justjavac, and 846 more reacted with thumbs up emoji

 
👎

638

 
KaruroChori, rbozan, Partur-dev, playerx, TheOnlyArtz, criloz, vvzen, 0xHexE, pannapudi, debbie-drg, and 628 more reacted with thumbs down emoji

 
😄

265

 
0xD503, Natural-selection1, saolof, syyyr, uandere, savonarola, farebyting, samoylenkodmitry, dashed, nicklauri, and 255 more reacted with laugh emoji

 
🎉

179

 
Gowee, SimonLeclere, richardhenry, teamgroove, miniBill, zachkamran, seanparkross, muojp, thesofakillers, AdiY00, and 169 more reacted with hooray emoji

 
😕

115

 
blinry, playerx, mikelui, cxOrz, CelDaemon, Sayrix, umuoy1, pannapudi, Mirsario, notxorand, and 105 more reacted with confused emoji

 
❤️

121

 
He-Pin, PaulGrandperrin, joshlk, TomasHubelbauer, richardhenry, bmartynov, cameronapak, lu-zero, muojp, MAiKo26, and 111 more reacted with heart emoji

 
🚀

211

 
Dsaquel, theoparis, shimbaco, samhumeau, timfennis, LynchzDEV, tim-hm, corporatepiyush, jmjoy, yasink21, and 201 more reacted with rocket emoji

 
👀

295

 
Chaoses-Ib, dtinth, tigerza117, dominic-r, UnownPlain, PatrickMatthiesen, onkoe, theoparis, phgoh, rdnsan, and 285 more reacted with eyes emoji

 

All reactions

 
Loading

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Sign up for free

to join this conversation on GitHub
.
 Already have an account?
 
Sign in to comment

Add this suggestion to a batch that can be applied as a single commit.
This suggestion is invalid because no changes were made to the code.
Suggestions cannot be applied while the pull request is closed.
Suggestions cannot be applied while viewing a subset of changes.
Only one suggestion per line can be applied in a batch.
Add this suggestion to a batch that can be applied as a single commit.
Applying suggestions on deleted lines is not supported.
You must change the existing code in this line in order to create a valid suggestion.
Outdated suggestions cannot be applied.
This suggestion has been applied or marked resolved.
Suggestions cannot be applied from pending reviews.
Suggestions cannot be applied on multi-line comments.
Suggestions cannot be applied while the pull request is queued to merge.
Suggestion cannot be applied right now. Please check back later.