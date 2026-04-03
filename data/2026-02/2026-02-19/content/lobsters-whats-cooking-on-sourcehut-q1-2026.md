---
title: What's cooking on SourceHut? Q1 2026
url: https://sourcehut.org/blog/2026-02-18-whats-cooking-q1-2026/
site_name: lobsters
content_file: lobsters-whats-cooking-on-sourcehut-q1-2026
fetched_at: '2026-02-19T06:00:38.969281'
original_url: https://sourcehut.org/blog/2026-02-18-whats-cooking-q1-2026/
date: '2026-02-19'
description: sourcehut is a network of useful open source tools for software project maintainers and collaborators, including git repos, bug tracking, continuous integration, and mailing lists.
tags: devops
---

Hello again! It’s a new year and time for a new quaterly update from SourceHut.
You may have read ourlast update in Q4 2025–
let us get you up to speed on how those plans have played out, and what’s coming
in the near future.

## Drew’s update

First up, I have an update on the pricing changes weproposed in
December: the new prices are now in effect for new customers. Existing
users are grandfathered into their current price-point, but there is a button on
yourbilling dashboardwhich will allow you to
opt-in to the new price point if you wish to support us by doing so (and lots of
love to everyone who asked for the ability to do that). If you cannot afford the
new prices, there is a special price that matches the earlier minimum price, and
of course as always if that’s still too much then we are happy to provide
financial aid for anyone who needs it.

Moving on, after last quarter’s focus on refactoring, I wanted to switch gears
to adding some new user-facing features for a while. The most obvious of these
changes is probably the new profile pages –here’s mine for
reference. Each user’s profile now includes tabs linking to your
resources (git repos, mailing lists, etc) across all services. We also added
avatars and pronouns to your profile details (add them here) to
show off here. We intend to be very sparing with avatars, by the way, to reduce
distractions on the user interface – right now there are no plans to show them
anywhere except for your profile page.

Another UI change I made was, finally, answering the long-awaited requests for
format=flowed support on the lists.sr.ht UI, with assistance on the style and
ironing out some bugs from Ember Sawady and aoife cassidy. Emails written with
format=flowed will now wrap properly and be much easier to read on mobile
devices in particular.

I’ve also seen through, with Simon Martin’s help, the rollout of “resource IDs”,
or rids, to our GraphQL APIs. The implementation is not totally complete, and we
could stand to add these to more resources, but they work and are providing some
useful functionality for the most commonly used API resources. RIDs are inspired
byULIDs– they are unique identifiers for resources on SourceHut which have
some useful properties:

* They are not predictable, preventing users from enumerating all resources by
enumerating the namespace of predictable IDs
* They are lexically sortable by the moment of their creation
* They are stable even when a resource is renamed or transfers ownership

This allows us to expand the GraphQL API with support for directly fetching
arbitrary resources by ID, perhaps reaching relatively deep into the graph, such
as fetching a specific comment on todo.sr.ht without going through the ticket
and the tracker first. Throughout the UI we have also started adding a subtle
copy of the resource ID for whatever you’re looking at, for exampleat the
bottom of git repo summary pages.

I intend to follow up on some earlier work in the coming quarter, for instance
adding more resource IDs to resources that make sense throughout our GraphQL
APIs. I’m also looking forward to working together with Simon on his coming work
to establish a project hub API, which unblocks some important work like
backreferences in the UI from resources to the projects that they belong to. I’d
also like to start accepting payments in GBP in this quarter, and there are some
tech debt goals that I’d be pleased to move the needle on.

But, the big thing I’m working on this quarter is organizations. It will be a
lot of work so I cannot promise that it will be done soon, but I’m pleased to
share that – finally – we are making progress on support for them.

## Conrad’s update

It’s one of those quarters where this write-up feels a bit therapeutic,
because at first glance, I didn’t get any of the things done that I had
planned. But sometimes you just have to take a step back and review, so let’s
do that!

As a follow-up to last quarter,sourcehut-migrategained support for
initializing databases, replacing the various-initdbPython scripts. That
concludes our Alembic replacement with all functionality restored!

Then there have been the usual, (mostly) invisible infrastructure updates. We
finally have a structured - and more importantly, ready-to-go in case of
emergencies - PXE-boot setup for our servers. So in case a server refuses to
boot from disk, we can quickly bring it back online for diagnosis and recovery
without having to hastily assemble DHCP configuration files. Kudos to Alpine
Linux for being so stable that I have kept this such a low priority for far too
long. I also at long last finalized and codified the monitoring of all our
baseboard management controllers via IPMI.

In software space, I have spent a significant amount of time refactoring
various Go packages, with the final (and yet to realize) goal of rewriting the
builds.sr.ht shell in Go, further reducing our Python usage.

And for the last item, I need to do something which I usually try to avoid:
making promises about future work. But in this case, it sort of provides the
backdrop, so here goes: I have been on the somewhat tedious quest to clean up
our SSH key database. It contains some surprising entries, mostly for historic
reasons. This is of course not very exciting for users, but the reason I am
doing this is because I am trying to refactor the SSH keys table. And this is
still not very exciting, but when this table has reached a state with which we
are content, I will use it as a blueprint for adding SSH deploy keys to
git.sr.ht. There, I said it. Now the game is on for the next quarter…

## Everyone else

SourceHut is 100% free and open source software, and the community is invited to
participate in its development. Let’s take a moment to acknowledge the work of
the volunteers who use and depend on SourceHut and sent along patches to improve
it over the past few months.

Once again, we have to thankSimon Martinfor his many
patches throughout the platform. This quarter, Simon added many useful features.
Thanks to him, one now has finer-grained control over how builds are submitted,
allowing one to whitelist or blacklist submissions from git.sr.ht to specific
branches or refs, or disable it altogether; a similar feature is now available
to tune build submissions for patches sent to mailing lists. He also added a
feature to builds.sr.ht that allows users to edit job tags after submission, to
organize your jobs post-facto. He’s also implemented multi-line selections for
paste.sr.ht, added more detailed software version information to our APIs, and
added links in the lists.sr.ht UI from superseded patchsets to the patchset that
supersedes them. Lots of great stuff, thanks Simon!

As usual we have a lot of updates from the community maintainers who keep your
builds.sr.ht images in good working order. Gary Kim shipped Fedora 43 and
oversaw the deprecation of Fedora 41, now end-of-life. CismonX released FreeBSD
15.x, and updated the image refresh schedule so that FreeBSD current is rebuilt
daily. Marek Marecki kindly shipped OpenBSD 7.8 support, and Achill Gilgenast
helped get Alpine 3.23 ready for use as well. Thank you, everyone!

Last, but not least, we’d like to thank Varun Narravula for a small patch which
addressed a bug that prevented todo.sr.ht tickets from being resolved via email.
There are a handful of other small bug fixes and minor improvements from many
other contributors as well – thank you to everyone who helped to make SourceHut
even better in the past few months.

« Proposed price increases for SourceHut
