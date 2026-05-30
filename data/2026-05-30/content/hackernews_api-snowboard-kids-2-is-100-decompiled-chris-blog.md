---
title: Snowboard Kids 2 is 100% Decompiled | Chris' Blog
url: https://blog.chrislewis.au/snowboard-kids-2-is-100-decompiled/
site_name: hackernews_api
content_file: hackernews_api-snowboard-kids-2-is-100-decompiled-chris-blog
fetched_at: '2026-05-30T19:34:01.361628'
original_url: https://blog.chrislewis.au/snowboard-kids-2-is-100-decompiled/
author: GaggiX
date: '2026-05-26'
published_date: '2026-05-17T14:02:16-07:00'
description: Snowboard Kids 2 for the Nintendo 64 has reached 100% matching decompilation. A brief note on what that means, how we got here, and what comes next.
tags:
- hackernews
- trending
---

# Snowboard Kids 2 is 100% Decompiled

17 May, 2026

I’m very pleased to announce thatSnowboard Kids 2is 100% decompiled!

All of the game’s functions have now been implemented in C and compile to assembly that matches the original game. There’s still some occasional__asm__hackery,1and plenty of code needs better names and documentation, but every function now has a matching C implementation.

That matters because a matching decompilation turns the game from a pile of MIPS assembly into a codebase we can read, build, study, and modify. It should help with recompilation, asset extraction, modding, and generally understanding the mechanics of the N64’s greatest game.

Snowboard Kids 2 decompilation report from decomp.dev. Boxes represent different files.

## The journey

This project has been a little under two years in the making, with thefirst commitlanding in September 2024.

The circumstances surrounding the final matches were not quite what I expected when I started. I’m currently sitting in hospital with my newborn daughter. She’s doing fine, but needs some help eating. Decompilation has been a useful distraction and an enjoyable way to fill the quiet hours.

The path to decompiling any game, let alone a Nintendo 64 game, is not especially well documented. This project would not have been possible without the N64 decompilation Discord community, whose members have been incredibly generous with their time. I would particularly like to thankBl00D4NGEL,inspectredc,SlaveOfIDO, andqueueRAMfor their significant contributions to the project, especially across the final ten functions.

Leaderboard shared on discord for tracking work on the remaining Snowboard Kids 2 functions.

The community was more important than any model: people answered my dumb questions, explained tooling, and decompiled functions themselves. With that said, coding agents also greatly accelerated the decompilation effort, particularly Claude, GLM, and Codex. I don’t want to turn this into another AI blog post2, but I do have a couple of observations:

1. Based on my experience with the final ten functions, which were among the most difficult, the most effective model appeared to be Codex 5.5 xhigh. Historically Claude was more effective, and I expect this to keep changing, perhaps even by the time you read this.
2. Frontier models are now very effective at decompilation, but this comes at a cost. GLM has probably been the best value for money for this specific kind of work. If you want to try coding agents on your own decompilation project but are put off by high subscription fees, that is where I would start.

## What next?

Reaching 100% decompilation was not technically blocking the recompilation effort, but it was more interesting to me personally. With the decompilation finished, my next goal is to release a high-quality recompilation ofSnowboard Kids 2.

That’s already in a pretty good state thanks to help fromsonicdcerandDarioSamo, but there are still bugs to squash before I’m comfortable releasing it.

Screenshot from Snowboard Kids 2: Recompiled. Note the use of widescreen and expanded draw distance. This can lead to some visual quirks.

There’s also plenty of work left to do in the decompilation project itself. A 100% match doesn’t mean the source is perfectly understood. Many functions still have generated names, many structures need to be cleaned up, and graphics/audio assets are still mostly treated as binary blobs. The project is now in a much better place for that work, but the work still needs doing.

Finally, I’m interested in starting aSnowboard Kids1 decompilation. I think it would be very cool to have a ‘Super Snowboard Kids’3that combines both games and allows you to play all the original tracks on the second game’s more modern engine. I have no idea how feasible that ultimately is, but it’s a fun thing to think about.

If you’ve made it this far, you probably have an interest in decompilation andSnowboard Kids 2. Take a look at theSnowboard Kids 2 decompilation project. The README includes a list of good first tasks.

You can alsofollow me on Blueskyfor more Snowboard Kids 2 updates.

1. The project uses some targeted__asm__instructions to coerce variables into particular registers, ensure writes happen at the appropriate time, etc. Generally, these could be removed and the game would function in exactly the same way (albeit no longer byte-for-byte matching). Still, ideally this wouldn’t be needed at all, and the long-term goal is to remove them.↩︎
2. I havethree of those alreadyif you’re interested.↩︎
3. Trivia: this was actually the title ofSnowboard Kids 2in Japan!↩︎

<< Previous Post

|

Next Post >>