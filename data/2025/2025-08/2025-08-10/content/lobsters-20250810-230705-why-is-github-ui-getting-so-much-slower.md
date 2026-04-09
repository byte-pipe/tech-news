---
title: Why is GitHub UI getting so much slower?
url: https://yoyo-code.com/why-is-github-ui-getting-so-much-slower/
site_name: lobsters
fetched_at: '2025-08-10T23:07:05.933248'
original_url: https://yoyo-code.com/why-is-github-ui-getting-so-much-slower/
date: '2025-08-10'
description: Matyáš Racek's blog
tags: performance, web
---

I couldn't help but notice - GitHub UI has been getting slower and slower recently. Some things that were snappy before are
hellishly slow nowadays. GitHub is doing something weird and I just can't wrap my head around what's going on there.

You guys developing at GitHub, you're using GitHub to develop it, right? Do you not see this? What's going on?

Whenever I bump into slow website which drives me nuts, I open the devtools and profile it. Who knows, maybe I
find something to report and the problem will get fixed.

To give one representative example, here's a profile for switching from "Conversation" tab to
"Files changed" tab on a PR.

Before we look into the profile, notice that this takes over 5s. How is anything like that acceptable in 2025 is beyond me.

Now, if you dive deep into this, you'll see that GitHub usesTurboto preload next page and swap out the
content without page reload. This is usually done as a performance optimization, but here, we see something completely
absurd.

If you try this out at home and play around with it, you'll find out thatopening the "Files changed" link in a new tab is
actually 2x faster:

And not only that - the client side post-processing in the first profile actually takes longer than loading the html
from the server. This whole thing just doesn't make any sense.

The cherry on top is the new loading bar that just drives me absolutely nuts, because it reminds me how slow
the whole transition is:

Guys... can you just make the transition fast such that you don't need a new loading bar?
Like, what's the point of doing client side routing, when you just recreate the full page reload experience, but slower?The whole point of doing SPAs was to avoid this. Client side routing should be instant.

This is just one of many performance problems on GitHub. It didn't use to be that way. Trying to go through multiple PRs and
issues is just suffering now. Imagine you have 20 PRs to find out which one introduced a regression, and every click takes more than 5 seconds to show something.

Don't even get me started on the diff view itself - yes, the one that periodically freezes for 2 seconds while browsing through
large PR's - maybe it has something to do with the fact that it renders thousands of invisible plus buttons with the
same inlined svg icon:

Or, you know, maybe not trying to render100 000 DOM nodesin general would
also help.

The whole window freezes for 3 seconds when you resize the dev tools window because you want to profile
this thing.

## Does this ever improve?🔗

So, maybe, whensome of the popular issuesare related to performance, and GitHub has this seemingly related"Platform collaboration at scale"focus area in the roadmap, maybe this will change?

Let's look at the roadmap and see if we can findanythingrelatedtoperformance. Did you find something?

## Related🔗

* JavaScript style for optimal size
* Basic rules of JavaScript performance in the browser

11 April 2025

* #programming
