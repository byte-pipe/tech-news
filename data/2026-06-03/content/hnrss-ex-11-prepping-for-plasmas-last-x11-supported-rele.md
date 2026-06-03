---
title: 'EX-11: Prepping for Plasma’s Last X11-Supported Release – David Edmundson''s Web Log'
url: https://blog.davidedmundson.co.uk/blog/596/
site_name: hnrss
content_file: hnrss-ex-11-prepping-for-plasmas-last-x11-supported-rele
fetched_at: '2026-06-03T12:34:54.339984'
original_url: https://blog.davidedmundson.co.uk/blog/596/
date: '2026-06-02'
description: Preparing for KDE Plasma's Last X11-Supported Release
tags:
- hackernews
- hnrss
---

When we first announced the transition to Plasma Wayland, one ofMartin's slidesfrom stated, "It's done when it's done!"

That talk was 15 years ago!

Nothing in software is never truly "done", butas announced previouslywe are finally at a point where we're ready to retire the X11 and put all our focus on the future.

As of today, the Plasma X11 session you can log into has been officially removed, and we will start a mass cleanup of X11-specific code soon.

## When does it take effect?

This change will be included in Plasma 6.8, which will be released in around five months.

## What's Changed?

In Plasma 6.8, there will be no X11 session in the login screen. There will only be a Wayland session available to log into.

In 6.8, all X11-specific code paths in Plasma for Plasma Shell, System Settings, and device configuration will be gone.

## What's stayed the same?

XWayland support remains present. You can keep using your X11 applications, and our XWayland application support is second-to-none.

If you use KDE applications on another desktop environment, this change will have no effect. KDE applications will continue to work in X11 for the foreseeable future.

Plasma Login Manager will continue to be able to log you into X11 sessions of other desktop environments.

## What's Next?

The possibilities this opens up are very exciting. Until now, on the desktop side, we've had to target the lowest common denominator or be stuck trying to maintain two conflicting code paths. It was absolutely the right choice to do a gradual transition and approach things this way, but that approach has its limits.

Moving forward with a single code path going through Wayland is going to allow us to bring new performance improvements, memory optimisations, and brand new exciting features throughout Plasma.

## How Ready Are We?

Our internal metrics within KDE show that over 95% of users of Plasma 6.6 are on Wayland, with a gradual increase every release. The metrics also show that basically no one is testing or developing Plasma on X11 anymore. The platform was already, for all intents and purposes, abandoned by KDE contributors.

We have every reason to trust this metric data, as it is exactly in-line with what Sentry (our automatic crash reporting tool) reports for newly-encountered crashes shows.

For transparency, the one caveat in all of the above is that I've deliberately always focused on people using the latest Plasma release. We do still have a sizable chunk of users on X11 still using Plasma 5.27. Including them, the total Wayland adoption rate is about 76%. But back then, Wayland wasn't the default session type, so it's hardly a surprise those users are still on X11. Things have come a massively long way in the three years since Plasma 5.27 was released.

Anyone still using Plasma 5.27 — or any release older than Plasma 6.8 — won't be affected by what we do in Plasma 6.8, and nothing will be applied retroactively.

## Still Have Issues with Wayland on 6.7?

Whilst we have had full confidence since Plasma 6.0 that our Wayland session provides the better overall experience, we are aware that things don't behave exactly the same. Not everything works the same especially in specialised areas.

We are not expecting a completely seamless transition for everyone. Custom scripts, tools used and even workflows might have to change. But we are aiming to offer a transition where there is still a way to accomplish all your day-to-day tasks.

Plasma 6.7 is the last release that will include an X11 session, and it's coming out in just a few days. If you still have issues that force you back to X11 we would love to hear from you.

We can't promise to get everything fixed in time for 6.8, but we can promise to listen and be aware. People's remaining pain point are and will be on our radar, so please take this time to communicate them.