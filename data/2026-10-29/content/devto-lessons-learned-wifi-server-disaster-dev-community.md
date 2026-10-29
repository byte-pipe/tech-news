---
title: 'Lessons Learned: Wifi Server Disaster - DEV Community'
url: https://dev.to/annavi11arrea1/lessons-learned-wifi-server-disaster-16oc
site_name: devto
content_file: devto-lessons-learned-wifi-server-disaster-dev-community
fetched_at: '2026-10-29T20:59:59.747605'
original_url: https://dev.to/annavi11arrea1/lessons-learned-wifi-server-disaster-16oc
author: Anna Villarreal
date: '2026-10-28'
description: So there I was, figuring out how to set up all my social media for branded automated posting.... Tagged with beginners, webdev, learning.
tags: '#beginners, #webdev, #learning'
---

Classic tale of dev server scope creep

So there I was, figuring out how to set up all my social media for branded automated posting. Pinterest requires a privacy policy link to do certain things. No problem. I have that. Or at least I thought I did...

When I went to my site to grab the privacy policy link, it returned with some strange error I had never seen before. It was like 1003 or something like that. Complete and utter failure. Shocked, I reached for sentry (which I had been leaning on, of course) free tier used up. No more uptime monitoring enabled. I got too cozy. I go to the server, it's on and running, and appears functional. After some quick digging, I discovered it was wifi. The server was still running on wifi. I knew that, but I never experienced a disaster like this first hand.

Why is it on wifi, you ask? The original intention was for poking around, learning, and other activities not intended for a production server. 😂 it has snowballed into something with a tiny heartbeat. ****

Back to the why: it's sitting next to the switch that I have yet to configure. 2 switches actually. A juniper and a cisco. I am at a crossroads. The juniper would be free, but I was studying cisco. I started studying networking stuff but I've been very busy. And im not putting my desktop on wifi.

Want some sprinkles? The server is on the opposite side of the house, on a different floor, with lots of structure in between. I have 2 cat6a cables running down. We have about 25+ things that need internet, in that room alone. Have fun thinking about that.

Damnit! 😂 I wasn't ready yet! My plans have now changed. Tomorrow I attempt a network configuration. No one to hold my hand and walk me through the process here. Certain panic. Wish me luck.

My server that I have been working so hard on had an unplanned 2 hour outage while I updated it in a panic. This must be what it feels like to work in cybersecurity. Panic panic everywhere.

I have an actual big server (its old) but I haven't got it fully configured, and also I wanted my switch up. Its a big fat cycle of excuses. I can't continue like this. 😂😂😂

I guess I have to be a baby system admin now. This was not a part of my original plan. I swear I spend more time fixing problems (that I created) than anything else.

I fully updated my tiny server since it was already down, and turned off power saving. Its not enough, but if I'm lucky, I'll get a switch working tomorrow... maybe?

I also learned I need a redirect page for when my server is down for maintenence. Basic stuff if you think about it. I am but a single junior dev, don't shoot. XD

Side note: As I was explaining this to my significant other, first, his jaw dropped. Then, he busted out laughing because he said he was planning on "play with the wifi tomorrow." Then my jaw dropped.

Disasters.

Undoubtedly this should make for an interesting story, if nothing else.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse