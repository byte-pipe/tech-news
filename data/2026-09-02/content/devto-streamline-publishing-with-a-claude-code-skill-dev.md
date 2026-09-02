---
title: Streamline Publishing with a Claude Code Skill - DEV Community
url: https://dev.to/gde/streamline-publishing-with-a-claude-code-skill-1bdn
site_name: devto
content_file: devto-streamline-publishing-with-a-claude-code-skill-dev
fetched_at: '2026-09-02T14:58:58.568891'
original_url: https://dev.to/gde/streamline-publishing-with-a-claude-code-skill-1bdn
author: xbill
date: '2026-09-01'
description: A Claude Code skill that turns one markdown file into dev.to, AWS Builder Center, Medium and LinkedIn versions, checks them before they ship, and posts the ones with an API — plus the debugging tools for when a destination mangles something. Tagged with claudecode, writing, devtools, ai.
tags: '#claudecode, #writing, #devtools, #ai'
---

TL;DR:publishing-kitpackages the whole publishing lifecycle as a Claude Code skill. Write one markdown file, and it builds the dev.to, AWS Builder Center, Medium and LinkedIn versions, checks them, and posts the ones that have an API. This article, its cover and all four of its artifacts were produced by the thing the article is about — dogfooding all the way down. More on that at the end.

Publishing one technical article to four places involves a surprising amount of ceremony: making a cover at whatever size each destination wants, rendering tables to images because Medium's importer eats them, stripping emoji for AWS, checking that every number in the piece came from a real run, getting a long markdown file into a browser editor that has no API, remembering which organization the article routes to, and writing the announcement post afterwards — by which point you have four slightly different files and no idea which one is current.

I packaged all of that intopublishing-kit— a Claude Code skill and a set of small scripts — so you can just ask Claude to publish.

## What it does

The skill teaches Claude the publishing lifecycle; the scripts do the parts a language model should not be doing by hand.

* Build the artifacts:one source file becomes the dev.to markdown, the Builder Center
version with emoji stripped and the AWS disclaimer appended, Medium HTML with every table
rendered to a PNG, and a LinkedIn post.make-builder.py,make-medium.py,make-linkedin.py.
* Make the cover once:make-cover.py --flow --sizes devto,builderdraws the pipeline as an
illustration and renders it at every geometry the destinations demand, names the file by a hash
of its own bytes, and reports which type sizes survive a 320px feed card — which is the size a
cover is actually met at, and where a diagram with small labels turns to mush.
* Trace every number:check-facts.pypulls the prices, measurements and versions out of
your prose and reports which ones appear in no evidence file. It cannot tell you a figure is
true. It tells you which ones you are asserting from memory.
* Pre-flight:preflight.py --liveruns the lot and exits non-zero — cover committed and
matching HEAD, geometry right, front matter complete, no hard-wrapped paragraphs, and every
published URL fetched and compared byte for byte against your disk.
* Post where there is an API:publish-devto.py --createtakes the front matter as the
payload, so title, tags and cover ride along with the body, and--org-slugroutes it to a
community channel. No browser.
* Drive the editors that have none:AWS Builder Center and Medium are Chrome work, and the
skill knows the route — payload throughwindow.name, a checksum on both sides, an emptiness
assertion before the paste, and a landmark count after it.

It also encodes the hard-won details you would otherwise learn the day after publishing: that dev.to renders markdown with hard breakson, so a source wrapped at 95 columns arrives with a stray break in every paragraph; that dev.to does not host your cover but proxies it at 2.381:1, so a 1376x768 cover loses 95px off the top and bottom; that Medium dropsdata:URI images on paste, so the self-contained build arrives with no pictures at all; and that LinkedIn's Posts API cannot create a draft, becausePUBLISHEDis the only state it accepts on creation.

## Install

The fastest path is the plugin marketplace:

/plugin marketplace add xbill9/publishing-kit
/plugin 
install 
publishing@publishing-kit

Enter fullscreen mode

Exit fullscreen mode

Prefer the classic route? Clone it and symlink the skill:

git clone https://github.com/xbill9/publishing-kit

ln
 
-s
 
"
$PWD
/publishing-kit/skills/publishing"
 ~/.claude/skills/publishing

Enter fullscreen mode

Exit fullscreen mode

You will need Python 3 with Pillow for the cover and table rendering, a dev.to API key in~/.devto.key, and a public repo to hold the article directory — both the cover and the Medium images are fetched by URL when the page renders, so unpushed means broken.

Mostly you will not run these scripts yourself — Claude does, andSKILL.mdtells it where they are. When you do want one by hand, the paths differ by install method, so ask rather than remember:skill-footprint.py --whereprints the skill directory. From a clone it isskills/publishing; from a marketplace install it sits under aversion-numberedcache path, which means no invocation you write down survives an upgrade.

That version numbering matters if you plan to hack on the skill itself: installing takes asnapshot, andclaude plugin updatecompares version strings, so edits under the same version never reach your session. Symlink while you are iterating.

## What it looks like in practice

Once installed, you talk to Claude Code like this:

"Write this benchmark up and publish it to dev.to under aws-builders"

Claude writes the source article, generates the cover at both geometries, traces the numbers against your run artifacts, runs the pre-flight, tells you what failed, and — once it passes — posts it as a draft and hands you the link. Then:

"Now make the Medium and Builder Center versions"

It derives them, renders the tables to images, opens Chrome, and fills the editors. It stops at draft on every destination and hands back links. Publishing is your keystroke, not its.

## Debugging a publish that went sideways

This is the half that surprised me most, and where most of the skill's value ended up.

The page does not look like the file.Fetch what the destination actually serves rather than reasoning about what you pushed:

python3 ../../skills/publishing/scripts/check-links.py article.md

Enter fullscreen mode

Exit fullscreen mode

devto-publishing-kit.md (branch URLs)
 ok cover.77acc7c4.jpg: HTTP 200, bytes match disk
 ok img/cover.77acc7c4.jpg: HTTP 200, bytes match disk
 ok img/devto-publishing-kit-table-1.png: HTTP 200, bytes match disk

Enter fullscreen mode

Exit fullscreen mode

AFAILthere reads "HTTP 200 but the served bytes differ from disk", which is usually an image regenerated after its commit. Every other check in the kit reasons about local state — is the file there, is it tracked — and each of those can pass while the published URL serves something else.

The paragraphs look ragged.check-article.pyreports hard-wrapped paragraphs with the line number of the first one, andpublish-devto.pyunwraps on the way out so your repo copy stays readable at 95 columns and the published page does not.

An image is missing on Medium.You pasted-embed.html. Paste-hosted.html, which references real URLs Medium re-hosts, and commit the images first.

A number in the article has no artifact behind it.check-facts.pywill name it. Every untraced claim is one of three things: measured but never archived, arithmetic that should be labelled as arithmetic, or asserted from memory — and it is always the third one that turns out to be wrong.

## Under the hood

OneSKILL.md, a reference file for each destination's quirks, and a script per job. The skill decides when each one runs; the scripts are independently runnable and print what they did.

The bit worth stealing for your own skills isreferences/house-style.md. Voice, section order, the opener and closing formulas live in that one file, and nothing inSKILL.mdor the scripts depends on it. Swap it and the kit writes as somebody else.

skill-footprint.pymeasures the skill's own size and token cost, and emits the cost table and cover footer for articles like this one — because a figure that changes on every commit does not belong in prose you have to remember to update.

## Dogfooding: this article, and its cover 🐕🍖

Every artifact here came out of the kit. The cover was rendered bymake-cover.py, the Builder Center version was derived bymake-builder.py, the Medium build bymake-medium.py, and the dev.to draft posted bypublish-devto.py.

The two numbers on the cover are real, and both were found by using the kit on itself:

measured

dev.to, hard-wrapped paragraphs

47 of 62
 in a published article carried a stray break

Medium, images pasted as data URIs

0 of 4
 survived; from real URLs, 4 of 4

The first one had been happening to my articles for months. The second cost a full re-do the first time it happened. Neither is in the docs of either destination, and both are now checks.

The run also found five faults in the kit itself, which is the point of eating your own cooking:make-medium.pyhad another project's repo hardcoded as its default image base;check-article.pypassed a cover that was tracked but regenerated;make-cover.pylost a--tilevalue beginning with a hyphen toargparse;check-facts.pyread127.0.0.1as a version number; andunwrap()skipped block quotes, so this article's own TL;DR posted as five separate lines — while the check that should have caught it skipped block quotes too, and agreed.

## Links

* Repo:github.com/xbill9/publishing-kit(Apache-2.0)
* The skill:skills/publishing/SKILL.md
* This article's directory, with every artifact and the evidence behind every number:articles/publishing-kit-skill/
* Claude Code:claude.com/claude-code

Issues and PRs welcome. This is a third-party community project, not affiliated with dev.to, Medium, AWS or LinkedIn — and the destination behaviours described here were measured on 2026-08-31, so check them again before you trust them.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse