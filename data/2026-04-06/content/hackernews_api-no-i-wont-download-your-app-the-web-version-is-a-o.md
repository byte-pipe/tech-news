---
title: No, I Won't Download Your App. The Web Version is A-OK. | Sid's Blog
url: https://www.0xsid.com/blog/wont-download-your-app
site_name: hackernews_api
content_file: hackernews_api-no-i-wont-download-your-app-the-web-version-is-a-o
fetched_at: '2026-04-06T19:26:52.277738'
original_url: https://www.0xsid.com/blog/wont-download-your-app
author: ssiddharth
date: '2026-04-06'
description: I won't download your app. The web version is a-ok
tags:
- hackernews
- trending
---

As someone who prefers using services via their websites, I’ve gotten terribly jaded lately. Almost everyone wants me, and by extension, you, to use their darn apps to consume content and off their web versions.

Whether it's the obvious social media apps or something as basic as parking, the app is the priority and the site the red-headed stepchild. And they aren't too subtle in the push either. It might be a modal covering half the web version with links to the App Store, an immediate popup after a bit of scrolling, or a header screaming “the app is 10x better,” but it's always there and it's always grating.

Let's not even go into the cases where the app is the only option to access the service. A minor annoyance for ordering food, but a major hassle when it's a public service or utility.

## Why the Hostility From Both Sides?

On principle, I like control over what I see and how I see it. Apps are super limited; while in a browser, I can do a lot of very nifty things to improve usability.

A service lacks a dark mode? I can use any number of user scripts. Reddit introduced a gaming section in the sidebar? Two-second fix that I bundled into my extension [1]. Between userscripts, ad-blockers, and custom extensions, I'm basically a god, swaggering through my realm.

This control, or lack thereof, also explains the app maker's adversarial stance towards users. They are often a black hole of dark patterns, and they'd like nothing getting in their way. Apps make it easier for them to push notifications, collect intrusive telemetry, and keep you inside their walled garden. A better user experience is the pitch but securing better user retention is the end goal.

## It's Mostly Just Text and Media

Most apps are just that. Text and media in a never-ending, all-consuming feed or a multi-page form, cleverly disguised by the user interface.

Excluding heavy 3D gaming or utilities that genuinely require deep integration with your phone's hardware (like accessing the LiDAR scanner for AR), what are we actually left with? A thin client whose main job is to fetch data from an API and render it onto native views.

Why do I need to download a 100+ MB app, give it permission to track my location, and let it run background processes just to browse through a restaurant menu, buy a ticket, or scroll through a list of posts? At the end of the day, it is almost always just JSON being parsed and rendered. Yet, companies insist on rebuilding their basic content as native shells just to claim a permanent square of real estate on my home screen.

## The Apps Aren't Even Good

If a service is going to pull you out of the browser, it should at least offer a polished, native experience. But more often than not, the app you just downloaded is a compromise.

Anyone who endured the iOS-specific shader compilation jank in early Flutter apps [2] knows exactly how grating this can be (this specific bug was fixed 2023ish fwiw). Before they swapped Skia out for the Impeller engine, I had to capture and ship precompiled shaders with my apps just to stop the UI from stuttering the first time an animation ran.

The result is often the uncanny valley of user interfaces. It’s not broken, but it is subtly different, sometimes janky. The scroll velocity doesn't quite match the rest of the OS. The swipe back gesture hesitates for a few milliseconds.

Human brains are remarkably good at detecting when a system's timing is off. This is how theXZ backdoorwas caught: an engineer noticed their SSH logins taking a fraction of a second longer than usual. It's not that unique -- my old FPS buddies could tell our server region just by firing a shot and feeling the lag. [3]

These micro interactions matter, because without that final layer of polish, the entire facade of a native experience falls apart. Not every app is like this, obviously, but enough of them are this way that it sours the entire experience.

## The Enshittification Loop

When that full-screen modal pops up demanding you download the app to read the rest of a thread, users choose the path of least resistance. They download and they move on.

To a PM staring at an analytics dashboard, I'm an acceptable casualty, an inconsequential minority. If degrading the web version successfully funnels 80% of users into the App Store, that PM gets a promotion and a big pay bump. As always, actions follow the incentive. Our demographic is simply too small to factor into their quarterly metrics.

This is the enshittification loop in its full glory, working exactly as intended. A service builds its initial audience on the open web because it's frictionless and indexable. Once the user base is sufficiently locked in, the web version is deliberately hobbled to force everyone into the native app. Once you're inside the app, the walls close in: you are now a captive audience for a feed full of ads that your ad-blocker can no longer touch.

There is no financial incentive to maintain a stellar web experience anymore. The browser, once the great universal platform, is increasingly being reduced to a top-of-funnel marketing channel for the App Store. The depressing part of it is that the numbers prove it works.

[1]https://gosinkit.com/

[2]https://blog.flutter.dev/whats-new-in-flutter-2-2-fd00c65e2039Search for "Preview: iOS shader compilation improvements"

[3]https://www.0xsid.com/blog/667mhz-machine