---
title: What is jj and why should I care? - Steve's Jujutsu Tutorial
url: https://steveklabnik.github.io/jujutsu-tutorial/introduction/what-is-jj-and-why-should-i-care.html
site_name: hackernews_api
content_file: hackernews_api-what-is-jj-and-why-should-i-care-steves-jujutsu-tu
fetched_at: '2026-04-15T06:00:12.105164'
original_url: https://steveklabnik.github.io/jujutsu-tutorial/introduction/what-is-jj-and-why-should-i-care.html
author: tigerlily
date: '2026-04-14'
tags:
- hackernews
- trending
---

# What isjjand why should I care?

jjis the name of the CLI forJujutsu. Jujutsu is a DVCS, or
"distributed version control system." You may be familiar with other DVCSes,
such asgit, and this tutorial assumes you're coming tojjfromgit.

So why should you care aboutjj? Well, it has a property that's pretty rare
in the world of programming: it is bothsimplerandeasierthangit, but
at the same time, it ismore powerful. This is a pretty huge claim! We're
often taught, correctly, that there exist tradeoffs when we make choices. And
"powerful but complex" is a very common tradeoff. That power has been worth it,
and so people flocked togitover its predecessors.

Whatjjmanages to do is create a DVCS that takes the best ofgit, the best
of Mercurial (hg), and synthesize that into something new, yet strangely
familiar. In doing so, it's managed to have a smaller number of essential tools,
but also make them more powerful, because they work together in a cleaner way.
Furthermore, more advancedjjusage can give you additional powerful tools in
your VCS sandbox that are very difficult withgit.

I know that sounds like a huge claim, but I believe that the rest of this
tutorial will show you why.

There's one other reason you should be interested in givingjja try: it has
agitcompatible backend, and so you can usejjon your own, without requiring anyone
else you're working with to convert too. This means that there's no real
downside to giving it a shot; if it's not for you, you're not giving up all of
the history you wrote with it, and can go right back togitwith no issues.