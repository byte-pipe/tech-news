---
title: TODOs aren’t for doing – Sophie Alpert
url: https://sophiebits.com/2025/07/21/todos-arent-for-doing
site_name: hackernews
fetched_at: '2025-07-23T04:07:26.590340'
original_url: https://sophiebits.com/2025/07/21/todos-arent-for-doing
author: todsacerdoti
date: '2025-07-23'
published_date: '2025-07-21T00:00:00.000Z'
---

## TODOs aren’t for doing

July 21, 2025

Some teams require that every TODO comment in a codebase gets logged in the bug tracker. Others automatically delete any “stale” TODO that has been in the codebase for over a year. Don’t do it!

TODO comments don’t need to get done in order to be valuable. If you have

// TODO: Write the second half of this file so next week's launch won't explode

then sure, you should probably track that somewhere.

But to me, a good TODO looks more like this:

// TODO: If the user triple-clicks this button, the click handler errors because [xyz]

Would this be the highest-priority thing on the backlog? Probably not. Most users won’t end up triple-clicking that button. But the// TODO:doesn’t need to be a plan to actually do something. Instead, it’s a note about “here’s an edge case that wasn’t handled” or a suggestion for a better structure that the author didn’t make time to implement — it captures a little slice of the author’s brain and gives a little window into the rich context they had at the time they wrote the code.

Sometimes TODOs are useful, sometimes they’re not, but well-placed TODOs can often answer a future reader’s “Am I totally missing something, or wouldn’t it better if this code was refactored like this?” — and answer it well enough to get past the hump of “Ehh, maybe I’ll just leave it the way it was in case the original author knew something I don’t.”
