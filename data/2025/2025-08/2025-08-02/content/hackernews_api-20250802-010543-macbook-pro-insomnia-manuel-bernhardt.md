---
title: Macbook Pro Insomnia - Manuel Bernhardt
url: https://manuel.bernhardt.io/posts/2025-07-24-macbook-pro-insomnia
site_name: hackernews_api
fetched_at: '2025-08-02T01:05:43.060312'
original_url: https://manuel.bernhardt.io/posts/2025-07-24-macbook-pro-insomnia
author: Manuel Bernhardt
date: '2025-08-01'
published_date: '2025-07-24T20:38:38+00:00'
description: 'Update (01.08.2025): fixed broken link, typo, clarified problematic behaviour For a number of years now I have a MacBook Pro Silicon M1 Max. It worked beautifully. Then, seemingly out of nowhere, I started noticing that the battery drained over night when I left the notebook somewhere, not connected to power. This got worse and worse, up until the point that I&rsquo;ve had enough of it and I started doing some research.'
tags:
- hackernews
- trending
---

## Contents

Update (01.08.2025): fixed broken link, typo, clarified problematic behaviour

For a number of years now I have a MacBook Pro Silicon M1 Max. It worked beautifully.

Then, seemingly out of nowhere, I started noticing that the battery drained over night when I left the notebook somewhere, not connected to power. This got worse and worse, up until the point that I’ve had enough of it and I started doing some research.

On MacOS, the terminal commandpmset -g logshows the logs related to power management. Those are quite verbose and not so easy to read, so I wrote alittle toolto analyze the logs.

This was however only marginally useful. I tried tweaking the settings a little I read about (such astcpkeepalive, one by one, but without much effect.

More digging led me to learn aboutSleep Aidwhich displays wake events in a nicer way and also has a neat interface to change settings.

Sleep Aid settings dialog

In my case, the “Wake for maintenance” option was disabled, and Sleep Aid helpfully showed in the settings interface that this could lead to frequent wake up events. With the setting disabled, the Mac got into a kind of wake-up frenzy, instead of waking up and processing events in batch every hour. Enabling the setting again did the trick, and my MacBook Pro no longer loses all of its battery during the night when it isn’t plugged in.
