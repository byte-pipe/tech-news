---
title: interblah.net - Self-updating screenshots
url: https://interblah.net/self-updating-screenshots
site_name: hackernews_api
content_file: hackernews_api-interblahnet-self-updating-screenshots
fetched_at: '2026-04-27T12:20:15.061434'
original_url: https://interblah.net/self-updating-screenshots
author: bjhess
date: '2026-04-26'
description: A blog by James Adam, of lazyatom.com fame.
tags:
- hackernews
- trending
---

I think this might be the neatest thing I’ve built inJellythat nobody will ever notice.

If you’ve ever maintained a help centre or documentation site for a web
application, you’ll know the particular misery of screenshots. You write a
lovely help article, carefully capture a screenshot of the feature you’re
documenting, crop it, maybe add a border and a shadow, upload it, and it looks
great. Then you change the UI slightly – tweak a colour, move a button,
update some copy – and suddenly every screenshot that includes that element
is stale. You know they’re stale. Your users might not notice, butyouknow, and it gnaws at you.

Or maybe that’s just me.

Either way, I decided to fix it. The help centre in Jelly has a build system
wherescreenshots are captured automatically from the running application,
and they update themselves whenever you rebuild.

## Markdown with a twist

The help articles are written in Markdown, which gets processed into HTML via
Redcarpet and then rendered as ERB views in the Rails app. So far, so
ordinary. But scattered through the Markdown are comments like this:

<!-- SCREENSHOT: acme-tools/inbox | element | selector=#inbox-brand-new-section -->

![The "Brand New" section](images/basics-brand-new-section.png ':screenshot')

That HTML comment is an instruction to the screenshot system. It says: “go to
the inbox page for the Acme Tools demo team, find the element matching#inbox-brand-new-section, and capture a screenshot of it.” The image tag
below it is where the result ends up.

## How it works

Under the hood, it’s a Rake task that fires up a headless Chrome browser via
Capybara and Cuprite. It scans every Markdown file for thoseSCREENSHOTcomments, groups them by team (so it only needs to log in once per team),
navigates to each URL, and captures the screenshot.

The capture modes are:

* element– screenshot a specific DOM element by CSS selector
* full_page– capture the whole page, optionally cropped to a height
* viewport– just what’s visible in the browser window

And there are a handful of options that handle the fiddly cases:

<!-- SCREENSHOT: nectar-studio/manage/rules | full_page | click=".rule-create-button" wait=200 crop=0,800 -->

That one navigates to the rules page,clicks a buttonto open a form, waits
200 milliseconds for the animation, then captures a full-page screenshot
cropped to a specific region. Theclickoption is the one that really makes
it sing – so many features live behind a button press or a popover, and being
able to capture those states automatically is wonderful.

There’s alsotorn– which applies a torn-paper edge effect via a CSS
clip-path – andhide, which temporarily hides elements you don’t want in
the shot (dev toolbars, cookie banners, that sort of thing).

## The satisfying bit

The whole pipeline runs with just this:

rails manual:build

That captures every screenshot and then builds all the help pages. When I
change the UI, I run that command and every screenshot updates to match. No
manual cropping, no “oh I forgot to update that one”, no slowly-diverging
screenshots that make the help centre look abandoned.

The markdown files live inpublic/manual/, organised by section – basics,
setup, advanced – and the build step processes them into ERB views inapp/views/help/, complete with breadcrumbs and section navigation, all generated
from the source markdown files.

This also makes it easy to update the help centre at the same time I’m working
on the feature; the code and the documentation live together and can be kept in
sync within the same PR or even commit.

## One of those “why didn’t I do this sooner” things

I put off building this for ages because it seemed like a lot of work for a
“nice to have”. Itwasa fair bit of work, honestly. Handling the edge cases
– elements that need scrolling into view, popovers that need clicking,
images that need cropping to avoid showing irrelevant content – took longer
than the happy path.

But now that it exists, I update the help centre far more often than I used to,
because the friction is almost gone. Change the UI, run the build,
commit the results. The screenshots are always current, and I never have to
open a browser and fumble around with the macOS screenshot tool.