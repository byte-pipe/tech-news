---
title: OpenFreeMap survived 100,000 requests per second
url: https://blog.hyperknot.com/p/openfreemap-survived-100000-requests
site_name: hackernews_api
fetched_at: '2025-08-10T07:04:43.500282'
original_url: https://blog.hyperknot.com/p/openfreemap-survived-100000-requests
author: Zsolt Ero
date: '2025-08-09'
description: Sorry Wplace.live
tags:
- hackernews
- trending
---

#### Share this post

 Thoughts while building
OpenFreeMap survived 100,000 requests per second
Copy link
Facebook
Email
Notes
More

# OpenFreeMap survived 100,000 requests per second

Zsolt Ero
Aug 09, 2025
4

#### Share this post

 Thoughts while building
OpenFreeMap survived 100,000 requests per second
Copy link
Facebook
Email
Notes
More
3
1
Share

I was about to post about how nice the last 10 months ofOpenFreeMaphave been. The architecture has really proven itself to be great, Cloudflare has agreed to sponsor the bandwidth, Hetzner servers are super stable as always, serving tiles from Btrfs proved to be a great choice, nginx is amazing, and life is good.

Then, out of the blue, I'm getting reports that some tiles are not loading, which normally means tile generation bugs, but not this time. I look into the nginx logs and see this:

2025/08/08 23:08:16 [crit] 1084275#1084275: *161914910 open() "/mnt/ofm/planet-20250730_001001_pt/tiles/8/138/83.pbf" failed (24: Too many open files) ...

This is weird. I've never seen anything like this. I check nload, and it shows huge traffic. I log into Cloudflare and I seeTHISfor the last 24 hours.

What?3 billion requests in 24 hours?What on Earth is that? Also, 215 TB of traffic from tiny, 70 kB files?

This much traffic would cost over $6 million per month on MapTiler and double that on Mapbox.

It's especially spiking in the last 5 minutes, where I'm seeing 30 million requests.

How much is that?

Wow, that's100,000 requests per second!

My first thoughts are:

* Wow.
* Wow, I'm surprised that the only bug I've heard about is some missing tiles. I mean, the service still seems to work? Somehow those empty tiles got cached by Cloudflare, but other than that, it still kind of works?

Looking at the Cloudflare dashboard, I can see that 96% of the requests were 200 OK; only 3.6% were broken (206 Partial Content).

So it seems that OpenFreeMap is mostly managing to serve 100,000 requests per second?

## But what is causing it?

Wplace.livehappened. Out of the blue, a new collaborative drawing website appeared, built from scratch using OpenFreeMap.

I don't know what it is, but the internet seems to be crazy about it. One thing is for sure: the traffic it generates is out of this world.

Wplace.live

I believe what is happening is that those images are being drawn by some script-kiddies. If I understand correctly, the website limited everyone to 1 pixel per 30 seconds, so I guess everyone was just scripting Puppeteer/Chromium to start a new browser, click a pixel, and close the browser, possibly with IP address rotation, but maybe that wasn't even needed.

Nice idea, interesting project, next time please contact me before.Neal.fundid the same before launchingInternet Roadtrip- they asked me if the traffic would be OK and even decided to sponsor the OpenFreeMap project with an amount that more than covers their bandwidth usage.

Sorry Wplace.live, I had to create my first-ever Cloudflare rule. As a single user, you broke the service for everyone.

I wonder if there is an automatic way to do this on Cloudflare, to limit traffic by referer or custom headers. It'd be great if this could be automatic, as I want to avoid this ever happening in the future. I hope I can script this via the API.

Finally, I want to say a huge thanks to Cloudflare for helping with the bandwidth. I haven't written about it yet, but when I contacted them back in November, they managed to get my bandwidth sponsorship status approved in 48 hours over a Saturday. Moreover, they connected me with some of their best engineers to discuss how OpenFreeMap could use their architecture even better. I've never seen a company of their size move as agilely as they did.

As the sole person running OpenFreeMap, I'm incredibly proud of these two numbers. First, that my architecture hit a 99.4% CDN cache rate, which is fantastic for a service with weekly data updates. And second, that my own servers successfully handled the remaining 1,000 requests per second.

## Update

I managed to contact the dev behind Wplace.live. He said they grew to 2 million users in a few days, out of the blue, so I totally understand them not being prepared for this kind of traffic. BTW, I'm amazed that their main architecture is holding up.

I offered to help them set up a self-hosted OpenFreeMap instance, which is the perfect fit for such use cases. They get the service for free, the public instance doesn't get the load, and everyone is happy.

Also, "only" having 2 million users confirms my belief that it's all just script-kiddies creating the load. 3 billion requests / 2 million users is an average of 1,500 req/user. A normal user might make 10-20 requests when loading a map, so these are extremely high, scripted use cases.

My recommendation to them is to remove the rules that force people to hack around with new browser sessions; it will just keep hammering their servers.

### Learnings

There are two learnings I'll write about in a next post.

1. I need to implement bandwidth limiting by referer. I'm looking into how to do this on Cloudflare. Nothing changes in the service; everything will still stay free and without registration, but every referer will be limited to a very high number, like 100 million requests per 24 hours or something similar. For native apps, I'll probably ask them to add a custom header identifying their app.
2. I'll need to improve my server config to fix those empty tiles. Even though I'm not expecting a load like this in the future, I think I found the culprit in the config that was causing the missing tiles.

If you find OpenFreeMap valuable, please considersponsoring on GitHub. To be fully transparent, the project currently runs on $500/month in donations. This is just enough to cover all infrastructure costs, which is fantastic. However, it means that new development happens in my limited free time. More support means more time I can spend coding, ensuring OpenFreeMap is ready for whatever comes next.

You can sponsor the project on GitHub athttps://github.com/sponsors/hyperknot

If you enjoyed this post, feel free to subscribe to this blog, or follow me onXorBluesky.

Subscribe
4

#### Share this post

 Thoughts while building
OpenFreeMap survived 100,000 requests per second
Copy link
Facebook
Email
Notes
More
3
1
Share
