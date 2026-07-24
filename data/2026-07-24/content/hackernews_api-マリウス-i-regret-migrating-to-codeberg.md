---
title: マリウス . I Regret Migrating to Codeberg
url: https://xn--gckvb8fzb.com/i-regret-migrating-to-codeberg/
site_name: hackernews_api
content_file: hackernews_api-マリウス-i-regret-migrating-to-codeberg
fetched_at: '2026-07-24T11:34:55.575856'
original_url: https://xn--gckvb8fzb.com/i-regret-migrating-to-codeberg/
author: boramalper
date: '2026-07-23'
published_date: '2026-07-23T14:23:15+02:00'
description: A brief comment on Codeberg’s new terms, and why a free-software host deciding which projects are welcome worries me more than the bans themselves.
tags:
- hackernews
- trending
---

A brief comment on Codeberg’s new terms, and why a free-software host
deciding which projects are welcome worries me more than the bans themselves.

My primary reason for leavingGitHubwas not about a single feature or a
single outage, but about the“enshittification”of the platform underMicrosoft’s ownership. The web interface got rewritten into a sluggish pile ofJavaScriptthat either broke things which used to just work, or
made them so horribly slow that using them became aPITA. Beyond the technical
decayGitHubhad turned into de facto“public infrastructure”in much the
same way thatWhatsApphas, hosting the source code of a very
large share of the world’s software and, through that, givingMicrosofta
degree of leverage and surveillance over everyone’s projects, and by extension
everyone’s digital lives, that no single company should hold. On top of that,
stories about legitimate developers losing their accounts due to arbitrary bans
byMicrosoftonly reinforced the feeling that it would be a good idea to at
least have a backupsomewhere else.

Codeberglooked like a viable alternative. It offered free and open-source
projects a reputable home and, more importantly, an equallyfreeone, run by a
non-profit association rather than a subsidiary of the largest software vendor
on the planet. Unfortunately, the latest update to its terms of service seems to
mark a first step in changing one part I moved there for, namely the“freedom”part.

## Human stupidity

Every project I’ve published so far was built with 100% human stupidity rather
than“artificial intelligence”, or, more accurately,LLMs. I don’t hold
particularly strong feelings aboutCodebergbanning projects that are
predominantlyLLM-driven, at least not feelings as strong as the ones I hold
about the simultaneous ban of legitimate cryptocurrency projects, which reads as
though it got lumped in for no reason other than that most people still remember
thevillain-du-jourthat crypto was in the years beforeLLMstook that
title. The two clauses landed within days of each other, theLLMprohibition
on the 29th of June and the cryptocurrency prohibition on the 2nd of July, both
asAssembly 2026proposals, and thetermsnow file the latter under,
of all things,“content that harms the reputation of Codeberg”, which sounds
like legalese for“we don’t have a solid reason or an actual number of bad
precedents to categorically ban it”.

The announcementblog post, however, readsverypoorly, and the
section titled“The development team of none”is the worst of it. It states:

Using LLMs to work with your code gives you a kick of adrenaline. You can
develop at a rapid pace, build things as if you had a large team. Only that
you have none. In fact, you are (often) alone, working with a statistical
machine that turns energy into code.

And, a little further down, it says:

It seems like many ‘vibe coders’ don’t realize that they don’t actually have a
community around them.

This is out of touch with how most free software gets made. The majority ofFOSSdevelopers are one-man-shows, and the onlycOmMuNiTythey have around
them are the users requesting features or reporting bugs while most of the time
not contributing in any form whatsoever. I’ve been publishingsilly little
toolsfor decades, predating this website and evenGitHubitself
(remember whenSourceForgewasthe hot sh.t?), and not one of them has ever
had an actual“community”around it, at least not in the romanticized sense
thatCodebergpaints in that post. I’m alone wolfwho codes everything by
hand and spends an absurd amount of time doing exactly that, and the notion that
anLLMis the thing separating a real project with a real community from a
fake one does not hold up once you look at how the average useful little tool on
any forge comes to exist in the first place.

It’s frankly a bit snotty ofCodebergto make this argument at all,
considering that the platform effectively lives inside theForgejobubble, andForgejomutiniedinheritedits community of active contributors fromGitea, who had spent the better part of six years building that community
beforeForgejoeven existed. A project that acquired its own community by
hard-forking someone else’s, then turned around to lecture solo developers about
not having one, is a difficult position to argue from with a straight face.

In addition,Codebergconflates“having a community”with“being legitimate
software worth hosting”, when the bar for a personal project has always been a
working build, ideally a license, and maybe a README, and not a channel full of
contributors. A good deal of what makes the small, single-author tool ecosystem
worth having is precisely that it doesn’t need a community to justify its
existence, and a forge whose entire selling point is hosting the code of
individuals is an odd place to argue the opposite.

## Censorship

The part that bothers me isn’t the specific ban onLLMprojects, or the
specific ban on cryptocurrency projects. It’s that a hub built around“free
software”is now telling its userswhich kinds of softwareare deemed good
and which are not, and that is closer to censorship than it might seem. Once a
platform writes into its terms that an entire category“harms its reputation”and can be removed on that basis, the deciding factor stops being whether the
code is legal, or functional, or useful, and becomes whether it aligns with a
position the platform has taken. I would argue that a significant share of the
projects caught by a blanket ban of that kind are legitimate software rather
thanvibe-coded sloporsh.tcoinimplementations.

Every platform I can think of that took this approach became divisive the moment
it started enforcing an ideology on its users, whatever that ideology happened
to be, and however justified it looked at the time. The mechanism is always the
same, where a real problem shows up, an unpopular category becomes the obvious
culprit, the platform bans the category instead of addressing the problem, and
that ban then becomes the precedent for the next category, and the one after
that. The category that is uncontroversial to ban today is the reason the
mechanism exists tomorrow, and the users who applauded the first ban rarely get
asked about the second one.

I do acknowledge that both categories aren’t free of problems.LLM-driven
repositories do strain infrastructure, do generate unmanageable volumes of
low-quality issues and pull requests, and do carry real questions about
copyright and code provenance, all of whichCodebergnames in its post. The
cryptocurrency space, in turn, might have produced more outright scams than
almost any other corner of software. However, a categoric ban on thevillain-du-jouris not a solution to any of that.

We now even have people likeLinus Torvaldsmaking the fairly reasonable
argument that anLLMisjust a tool, and“clearly a useful one”,
with a legitimate place inLinuxkernel development when it’s used carefully
and its output is held to the same standard as everything else. If the
maintainer of the largest and most consequential open-source project on the
planet can treatLLMsas a tool to be judged on its results rather than a
category to be banned on sight, abackyard code forgecan manage the same.

I, too, am worried about the impact ofLLMson tech, and on society in
general, going forward, and I’d guess I’m about as worried as whoever wroteCodeberg’s policy. I just don’t believe that banning content, which is very
much what this amounts to, is the way forward.

## Reasonable solution

What I wishCodeberghad reached for is a solution that treats the actual
problem, which by their own account in that same post is resource consumption
and the infrastructure cost that comes with it, as an actual resource problem. A
change to the terms of service could have required authors to tick a checkbox
declaring that a repository containsLLM-generated code, or is
cryptocurrency-related, and those repositories could then be segmented onto a
separate tier of infrastructure that doesn’t get the same resources as everyone
else. A tier that carries specific quotas, and that might require the author to
pay for what they consume. Declaring the truth honestly would (at least at
first) cost nothing, and failing to declare it, then getting caught, could be
met with exactly the permanent, immediate ban thatCodebergis now applying to
entire categories from the outset.

Similarly, projects that carry theLLMorCryptolabel could carry
automatically displayed disclaimers that explicitly state thatCodebergis in
no way responsible for the quality or correctness of this specific repository.
Heck, they might even go as far as to blatantly state thatCodeberg does not
approve of the use of LLMs or Cryptocurrenciesin those warnings, to make
extra-extra-extra sure that people get it and that there is no“reputational
risk”forCodeberg.

An approach like this puts the cost of resource-hungry projects onto the people
creating them, and it keeps the shared resources for the projects that were the
reason the platform exists. All of that withoutCodeberghaving to decide
which categories of software are ideologically acceptable in the first place.
The“we ban everything upfront that we don’t agree with”approach is the wrong
signal to send, and it is a very slippery slope.

Despite not owning a single project that falls into either banned category, I’m
now going to look into setting up my own publicGithost, and I’ll move offCodebergonly a few months after moving there, because of this. Not
because of the bans themselves, but because I don’t want to depend on a platform
that rewrites its terms of service on a whim, without properly announcing that
the change was even under consideration, and without giving its users a way to
weigh in.

The decisions did go throughCodeberg’s ownAssembly 2026, which is more
process than most platforms bother with, and yet as an ordinary user I found out
about it the way probably most people else did, through a dark blue banner at
the top of the site on the day it was already settled. While I appreciate the
info about theToSchange, I wish I’d gotten a banner back when the platform
was still deciding whether to go down this road, and I wish it had linked to a
discussion thread, or at the very least a poll, so that I could have voiced the
concern I have, which is about the freedom of the platform as a whole, rather
than about any single category that ended up banned.

Enjoyed this?Please consider supporting my work.

Published on

2026-07-23

and updated on

2026-07-23

in

journal

and tagged with

ai

censorship

decentralization

git

infrastructure

open-source

society