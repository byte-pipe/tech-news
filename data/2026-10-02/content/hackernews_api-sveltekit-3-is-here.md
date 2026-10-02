---
title: SvelteKit 3 is here
url: https://svelte.dev/blog/sveltekit-3-is-here
site_name: hackernews_api
content_file: hackernews_api-sveltekit-3-is-here
fetched_at: '2026-10-02T16:30:45.794999'
original_url: https://svelte.dev/blog/sveltekit-3-is-here
author: sampsn
date: '2026-10-01'
description: Get it while it’s hot
tags:
- hackernews
- trending
---

Version 3.0 of SvelteKit, the official application framework for Svelte, is now available.

If you’ve used earlier versions of SvelteKit, everything will feel very familiar — it’s the same framework with a little more polish, a little more type safety, and a little less junk. We’ve made migration as seamless as we can with thesv migratecommand...

npx
 
sv
 
migrate
 
sveltekit
-
3
 
--
tasks
 
all
 
--
confirm

...which will automatically migrate as much of your codebase as possible, and generate a TODO list for everything else. (If you’re agentically inclined, your robot friends will make short work of it.)

To create anewapp, runsv create:

npx
 
sv
 
create
 
my
-
new
-
app

As with any major version bump there are a handful of breaking changes to be aware of, which are covered in themigration guide(or, more briefly, in the recentrelease candidate announcement).

Quick highlights:

* configuration now lives invite.config.tsinstead ofsvelte.config.js
* the$libalias is now#lib, making use of standardsubpath imports
* environment variablesare more powerful and easier to use
* service workersare less boilerplatey
* error handling is improved across the board

## Are remote functions ready yet?

Not quite. But it’s our top priority!

Remote functionsare a set of utilities for secure, efficient, type-safe client-server communication. You’ve likely seen some version of this idea in other frameworks, but we think you’re going to prefer this one.

Using them requiresAsync Svelte, which for now requires anexperimentalflag. Bear with us.

## Join us in Ljubljana next month

This is as good a place as any to remind everyone that the next in-personSvelte Summitis taking place on November 19-20 in the lovely town of Ljubljana, Slovenia. Among other things it will be a celebration of Svelte’s 10th birthday, and we’d love to share some cake with you.