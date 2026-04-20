---
title: An ode to houseplant programming 🪴
url: https://hannahilea.com/blog/houseplant-programming/
site_name: hnrss
content_file: hnrss-an-ode-to-houseplant-programming
fetched_at: '2026-03-01T19:09:24.084736'
original_url: https://hannahilea.com/blog/houseplant-programming/
date: '2026-02-27'
description: An ode to houseplant programming (2025)
tags:
- hackernews
- hnrss
---

# An ode to houseplant programming 🪴

28 Apr 2025

Recurse Center (RC)peerRyanrecently coined a phrase that I instantly
 fell in love with:houseplant programming.

In Ryan’s words:

[The tool I built] solves my idiosyncratic problems and may not address yours at all. That’s fine—take it as an ad to write tiny software just for yourself. Houseplant programming 🪴[2]![2]This isn’t an existing phrase as far as I know, but the closest I can think of is “barefoot developers” which a) is a little more granola than my vibe and b) is maybe tied up in some AI stuff. I guess this issituated softwarebut even smaller: I’m not building for dozens of users, I’m building for one user
 in particular.[source]

Houseplant programming: tiny software just for yourself.Perfection.

At the risk of overexplaining and thus cheapening the analogy, I feel the need to wax poetic.🪴

Blomsterfönstret

 by Carl Larsson, 1895. Public domain via Wikimedia Commons.


## When “It works on my machine” is the goal, not the excuse

Things I have found myself saying about some personal projects, almost apologetically:

* It works for me, but…
* It’s held together withstring and electrical tape and visibly disorganized wires…
* I have to domanual restarts after the power goes off…

In the world of houseplant programming none of these statements are apology-worthy.1In a workplace, about a project that is intended for
 productionization2and mass dissemination? Sure, production-ready code—code that has a job, or provides the infrastructure for a job—needs to be some
 flavor of robust and tested and reliable. For a project that lives in my house and does what I need it to and periodically needs a little extra help? No worries.

Aditya Athalye(another RC peer!) perfectly captures this vibe in the project description for his software projectshite:

shite’s job is to help me make my website:https://evalapply.org. Thus,shite’s scope, (mis)feature set, polish will always be
 production-grade, where production is “works on my machine(s)” :)[source]

Strong “Everything I do is the attitude of an award winner because I have won an award” energy:

Any code is production ready, if you redefine the scope of your production environment!

## Properties of houseplants, programmatic and chlorophyllous

Before we get to the self-reflective bit,3here is a non-exhaustive list of parallels between my houseplants and my houseplant programs:

* A happy home: I love having both plants and homemade projects in my living space. Sharing a space with them reminds me of things that I like about the world and about myself.

Exhibit A: Happy houseplants on a happy houseplant shelf.

Exhibit B: Happy flipdisc installation on a happy flipdisc shelf.

 Exhibit C: Happy
xbar
-based utilities for launching common tasks and starting music playback, on a happy menu bar on my laptop.


* Longevity: Like my plants, I love my little projects and I want them to thrive, and I baby them a little bit to get them started. But also, if they don’t work out? It isn’t a big deal, intothe great compost bin in the skyGithub they go, where a hard-won line or two may becompostedrecycled into a future project.

This cat once had a cactus tail. Now it has a spiderplant tail.

* Propagation: Clippings! I love to propagate my plants and share them with friends. Do you want a pilea or a spider plant or a nice philodendron? Let me know, I’ll hook you up! Similarly, do you want to set upyour own pen plotteror make some quick and easyscreenshot memes? Awesome, I try to document and share the code and steps for recreating most of my projects.That said, once a plant/code has taken up residence in your home, it is no longer my responsibility. While I’d love to hear about what you did to help it thrive, and if it starts looking sad I’ll gladly help you think through
 what might help, if it never thrives I’m probably not going to lose sleep over it.Besides, once you’ve gotten as far as propagating the code/plant I’ve given you, you’ll know about as much about the situation as I do—maybe more—and now we can explore the next steps together.
* Pet toxicity: Just like some plants,some projectsare practically poisonous to my cat and—if the cat had her way—should be rehomed with a pet-free pal.

* Universalization: I don’t care to engineer my houseplants to thrive in every environment—and similarly, I don’t feel a need to make my houseplant code fully generalizable, until there is a more specific reason
 to do so.
* Knowledge sharing: I love reading about other people’s houseplant projects. While I occasionally take code cuttings for my own home, mostly I just want to wander around and admire their houseplants and learn
 more about the woes they encountered when figuring out how to help their code/plants thrive.I do not need to propagate someone’s houseplant [code] in my own home in order to admire it; I can learn to consider a different fertilizer or communication protocol without transplanting their program into my own home.
* Capitalism: One person’s houseplants are another person’s plant nursery. One person’s houseplant code is another person’s B2B SaaS product. Enough said.
* Bugs: Soil gnats. Where do they even come from?! It is unknowable.Sometimes my weather station shows me the icon for snow, even though it is currently April and the temperature isn’t predicted to dip below 32. ¯\_(ツ)_/¯4

* Fun: It is really, really fun to grow plants.5It is really really fun to write code.6

## Not an idea, not yet a Platonic ideal

While I build software as a career, I also like to muck about with code in service of other goals. When sharing those other projects it has taken me a long time be able to talk about what my code does do without adding a zillion
 caveats about what the codedoes notdo.7

Why? I think somewhere along the line I picked up the unhealthy—and false!—assumption that it wasn’t worth sharing my code until it was ready to be reused easily by whoever was able to access it—specifically, not sharing that code
 until it was “production ready,” for some arbitrary and ever-growing definition of “production” that I neverquitefully defined for myself.8

In the last year or so when presenting personal projects I’ve taken to saying that they’re prototypes. Prototyping is a thing that makes sense to many folks in the field—it involves a first pass at trying to build something, with
 output thatwon’tbe optimized, might be hacked together with glue and dreams, and possibly even “only works on my machine”. But it’s proof that it is worth spending more time on something, ornotworth spending
 more time on something.9

The thing is, a lot of the personal projects I’ve built arenotprototypes, even if they share a lot of the same characteristics of a prototype: while they are a first-ish pass at bringing an idea to life, and theycouldbe turned into a more generalizable or generic Thing, they’re never designed to be more than that first pass with its context-specific configuration.

While rebranding some of the projects I’ve built as “prototypes” helped me feel better about sharing something not totally polished, I’ve also felt like the term somehow devalues what I’ve built. Sure, sometimes what I’ve builtisa prototype! But often, it isn’t. It’s a first pass, sure, but it’s just aweird little guyof an idea, and
 doesn’t need to promise to be any more than what it already is. Just existing is enough,and I’m not necessarily interested in developing it into a less-weird less-little guy!

Thus: houseplant programming. Tiny software for just myself.

## Epilogue: Bouquet programming 💐

I’m going to spare us all a further brainstorm of plant/code parallels, with the exception of one spin-off term:bouquet programming💐.

I’m hereby defining bouquet programming as one-off code that is written for one specific userto support one specific use-case, in a non-recurring way. By definition, it needs no maintenance and simply provides proof of
 what once was run. Examples of bouquet programming: an analysis script in support of a one-time plot, a scrappy proof-of-concept or aminimal reproducible example.

Bouquet programming is still worth writing home about (!) and sharing generously in the same ways as houseplant programming—or agricultural programming!—but is evenlesslikely to work off-the-shelf for a new application
 than houseplant code is, even if rerun by the same person who originally programmed it.

Examples of my own bouquet code: a script I used to scrape book cover images for generating miniature book covers as part of a physical gift, code run in service of helping a friendprepare timelapse videos of her marbling process, etc.

My Musidex, for which I wrote a semi-reusable script to convert a set of playlists into a set of album art, metadata, and QR code stickers.

## Bonus: Garden stakes for horticulturalist programmers

I made a status badge for houseplant repos—feel free to use it!

<a href="https://www.hannahilea.com/blog/houseplant-programming">
 <img alt="Static Badge" src="https://img.shields.io/badge/%F0%9F%AA%B4%20Houseplant%20-x?style=flat&amp;label=Project%20type&amp;color=1E1E1D">
</a>

And a bonus badge for bouquet programming:

<a href="https://www.hannahilea.com/blog/houseplant-programming">
 <img alt="Static Badge" src="https://img.shields.io/badge/&#x1F490;%20Bouquet%20-x?style=flat&amp;label=Project%20type&amp;color=1E1E1D">
</a>

Thanks toRyanfor the coinage and to AF for introducing me to strategies for recognizing and countering perfectionism.

### Footnotes

1. Should it be “houseplant programming” or “houseplant programming 🪴”? Unless Ryan weighs in definitively, I’ll keep using the two interchangeably.↩︎
2. What is “production code”? Everyone seems to have their own non-standardized definition, but in general, it is code that is being actively used by someone other than its creator, such that some flavor of stability and uptime
 is expected.Or, my favorite definition, by way of Reddit:“Production code has a phone number to call when it breaks”[source]↩︎
3. As if you didn’t know that was coming!↩︎
4. Okay, so bugs aren’t inherently specific to houseplant code, but still…↩︎
5. Except when it isn’t.↩︎
6. Except when computer is mistaek.↩︎
7. I’m actively trying to cut down, both for my current self and for my younger self. My younger self didn’t have the confidence of concrete professional proof that something she’d done meant she no longer had to prove herself so
 much—but she had just as much to share, and I wish she’d felt more empowered to take up more space in the world, rather than feeling cowed by the folks she was impressed by all around her.↩︎
8. If this is something you resonate with, I encourage you to look up “perfectionism” and some techniques for remedying it. Ditto “capitalism”. 🙃↩︎
9. As the kids say, fail fast.↩︎

* Created: 2025-04-28
* Type: Musing
* Tags: phytoid, houseplant-programming
