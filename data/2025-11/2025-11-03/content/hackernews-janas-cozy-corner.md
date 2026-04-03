---
title: Jana's cozy corner
url: https://jsteuernagel.de/posts/using-freebsd-to-make-self-hosting-fun-again/
site_name: hackernews
fetched_at: '2025-11-03T11:10:54.429130'
original_url: https://jsteuernagel.de/posts/using-freebsd-to-make-self-hosting-fun-again/
author: Jana
date: '2025-11-03'
description: Feeling like a kid in a candy store, once more
---

# Using FreeBSD to make self-hosting fun again

2025-11-01 -Feeling like a kid in a candy store, once more

As evident by my last blog post"A prison of my own making", I needed to change something about my relationship with technology.
How I was doing things didn't work anymore, but I also felt unable to change anything about it, as the way I was doing things seemed liketheway that I was supposed to use.

What I needed was a fresh start.
And I managed to find that fresh start in the BSD family of operating systems.

I had already givenFreeBSDandOpenBSDa try at the time and I liked what I saw.
OpenBSD had already established itself in my workflow as an easy to use and reliable router and general OS for single-purpose VMs.
But it isn't able to fullfill my needs for a multi-purpose system, where I'd want to run multiple separated workloads in something like a container or VM.
But FreeBSD could.

I know that I generally operate best by just committing to using a thing and then figuring out what I need, as I need it.
So I committed to using FreeBSD and found a really nice server to do just that on the Hetzner server auction.

I started setting it up withBastilleBSDfor jails andvm-bhyvefor VMs.
I didn't know how to do most things and felt kinda lost.
But there it was again, that feeling of excitement to learn something new, which got my into self-hosting in the first place.

After some trial and error I managed to find a setup that works for me.
As per usual, it deviates a bit from what might be the mostcommonsetup, but it's undoubtedlyme(I'll probably explain more about it in the future, when things have settled).

What I've come to appreciate about FreeBSD, and the BSD operating systems in general, is their simplicity and good documentation.
Most tasks are just a few commands to run via SSH and if that isn't the case, someone has probably written a decent wrapper around it.
If I need to find a piece of information, I still instinctively search online for it, just to be greeted by an online version of the corresponding man page.
So I could also have just gathered that information on the CLI,oh well.

I also love the focus on long-term compatibility.
I can find a solution to a problem in a forum post from 2008 and not even for a second do I have to doubt whether it will work, because it always does.
At the same time, that doesn't mean there are no new features.
The system doesn't feel old.

Sure, not everything was all roses and some of that was probably due to my way of just jumping into a problem and digging myself through it one step at a time, instead of reading up on it a lot beforehand.
For example I was confused for a long time about the release cycle of the base system and whether that somehow related to pkg and ports (It does not).
And I was not able to properly phrase the question in a way that would result in a helpful result while searching.
Luckily the BSD community has been nothing but kind and helpful so far.
I've had multiple people on the Fediverse offer their help and when I had a specific question, I would always get multiple solid answers explaining it to me.
Thanks to everyone that replied, it's genuinely a blast to feel like a newbie again!

I don't know whether I will actually stick with all of what I'm doing right now, in the long term.
But that's not important.
What is important is that I'm having fun, learning a new thing, right now.
I'll see what sticks long-term.

@Joel: See? I wrote a blog post! :D
