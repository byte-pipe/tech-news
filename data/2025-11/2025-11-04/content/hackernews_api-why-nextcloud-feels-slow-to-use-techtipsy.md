---
title: 'Why Nextcloud feels slow to use :: ./techtipsy'
url: https://ounapuu.ee/posts/2025/11/03/nextcloud-slow/
site_name: hackernews_api
fetched_at: '2025-11-04T11:09:17.529584'
original_url: https://ounapuu.ee/posts/2025/11/03/nextcloud-slow/
author: rpgbr
date: '2025-11-03'
published_date: '2025-11-03T06:00:00+02:00'
description: Nextcloud. I really want to like it, but it’s making it really difficult. I like what Nextcloud offers with its feature set and how easily it replaces a bunch of services under one roof (files, calendar, contacts, notes, to-do lists, photos etc.), but no matter how hard I try and how much I optimize its resources on my home server, it feels slow to use, even on hardware that is ranging from decent to good. Then I opened developer tools and found the culprit.
tags:
- hackernews
- trending
---

# Why Nextcloud feels slow to use

 2025-11-03



 #
ramblings
 

 #
self-hosting
 

 #
software development
 



Nextcloud.I really want to like it, but it’s making it really difficult.

I like what Nextcloud offers with its feature set and how easily it replaces a bunch of services under one roof (files,
calendar, contacts, notes, to-do lists, photos etc.), but no matter how hard I try and how much I optimize its resources
on my home server, it feels slow to use, even on hardware that is ranging from decent to good. Then I opened developer
tools and found the culprit.

It’s the Javascript.

On a clean page load, you will be downloading about15-20 MBof Javascript, which does compress down to about 4-5
MB in transit, but that is stilla huge amount of Javascript.For context, I consider 1 MB of Javascript to be on the
heavy side for a web page/app.

Yes, that Javascript will be cached in the browser for a while, but you will still be executing all of that on each
visit to your Nextcloud instance, and that will take a long time due to the sheer amount of code your browser now has to
execute on the page.

A significant contributor to this heft seems to be thecore-common.jsbundle, which based on its name seems to provide
some common functionality that’s shared across different Nextcloud apps that one can install. It’s coming in at4.71
MBat the time of writing.

Then you want notifications, right?NotificationsApp.chunk.mjsis here to cover you, at1.06 MB.

Then there are the app-specific views. The Calendar app is taking up5.94 MBto show a basic calendar view.

 Nextcloud Calendar app Javascript assets.


 This is what 14 MB of Javascript gets you, after about 30 seconds of loading on a poor connection.


Files app includes a bunch of individual scripts, such asEditorOutline(1.77 MB),previewUtils(1.17 MB),index(1.09 MB),emoji-picker(0.9 MBwhich I’ve never used!) and many smaller ones.

 Nextcloud Files app Javascript assets.


 This is what 18.8 MB of Javascript gets you. I waited for a whole minute for it to load in a real world poor internet
connectivity scenario.


Notes app with its basic bare-bones editor?4.36 MBfor thenotes-main.js!

 Nextcloud Notes app Javascript assets. This isn't even half of it!


 20.91 MB of Javascript, for this?


This means that even on an iPhone 13 mini, opening the Tasks app (to-do list), will take a ridiculously long time.
Imagine opening your shopping list at the store and having to wait 5-10 seconds before you see anything, even with a
solid 5G connection. Sounds extremely annoying, right?

I suspect that a lot of this is due to how Nextcloud is architected. There’s bound to be some hefty common libraries and
tools that allow app developers to provide a unified experience, but even then there is something seriously wrong with
the end result, the functionality to bundle size ratio is way off.

As a result, I’ve started branching out some things from Nextcloud, such as replacing the Tasks app with using a
privateVikunjainstance, and Photos to a privateImmichinstance. Vikunja
is not perfect, but its 1.5 MB of Javascript is an order of magnitude smaller compared to Nextcloud, making it feel
incredibly fast in comparison.

However, with other functionality I have to admit that the convenience of Nextcloud is enough to dissuade me from
replacing it elsewhere, due to the available feature set comparing well to alternatives.

For now.

I’m sure that there are some legitimate reasons behind the current state, and overworked development teams and
volunteers are unfortunately the norm in the industry, but it doesn’t take away the fact that the user experience and
accessibility suffers as a result.

I’d like to thankAlex Russellfor writing about web performance and why it
matters, with supporting evidence and actionable advice, it has changed how I view websites and web apps and has pushed
me to be better in my own work. I highly suggest reading his content, starting
withthe performance inequality gap series.It’s educational,
insightful and incredibly irritating once you learn how crap most things are and how careless a lot of development teams
are towards performance and accessibility.

Subscribe for more tech tips!

Subscribe to new posts viathe RSS feed.

Not sure what RSS is, or how to get started?Check this guide!

You can reach me viae-mailorLinkedIn.

If you liked this post, consider sharing it!

Random tech tips!

We get laptops with annoying cooling fans because we keep buying them

The coffee machine ran out of memory

How I fixed one hardware issue with another one

My very first career day

Turns out that I'm a 'prolific open-source influencer' now
