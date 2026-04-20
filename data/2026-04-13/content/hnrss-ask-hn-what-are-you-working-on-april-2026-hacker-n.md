---
title: 'Ask HN: What Are You Working On? (April 2026) | Hacker News'
url: https://news.ycombinator.com/item?id=47741527
site_name: hnrss
content_file: hnrss-ask-hn-what-are-you-working-on-april-2026-hacker-n
fetched_at: '2026-04-13T12:02:43.630600'
original_url: https://news.ycombinator.com/item?id=47741527
date: '2026-04-12'
description: 'Ask HN: What Are You Working On? (April 2026)'
tags:
- hackernews
- hnrss
---

Hacker News
new
 |
past
 |
comments
 |
ask
 |
show
 |
jobs
 |
submit
login
Ask HN: What Are You Working On? (April 2026)
240 points
 by
david927

17 hours ago

 |
hide
 |
past
 |
favorite
 |
779 comments
What are you working on? Any new ideas that you're thinking about?
 
help

frostbyrne

2 minutes ago

 |
next

[–]

Greetings!

I've been working on something in the vein of GTRPGs for a little over a year now. It has been a passion project, but I'm starting to come around on showing it to people.I am a big fan of Telltale style narrative games. I think Baldur's Gate 3 was the biggest revelation of this for me. Taking that branching dialogue and freedom of choice, and tacking it on to a fun combat system was just everything.When text based GTRPGs started popping up, I found it hard to connect with them stylistically. I found that I needed the multimodal stimulus of visuals and audio. This led me to start building something, and it ended up being somewhat of a cross between a Telltale game, a Visual novel, and a TTRPG.Orpheus (https://orpheus.gg) is a fully on-the-fly generated tabletop simulator, with graphics, audio (TTS), and the freedom you can usually only find at a real TTRPG table. That means you can play a sci-fi, fantasy, or even a modern setting in your campaign. The assets are made for you as needed.Getting the harness right so the AI GM can stay coherent and organized has been the biggest challenge. It took a lot of iterations to get it to a point where it could understand the scenes it was building as the player changed them.I've built it to be played with either a keyboard or a gamepad so you can play from your couch. You can switch between them as you feel like it. There is a 3D tabletop for combat, full character sheets, dice rolling, lore tracking. I want it to be dense.

reply

kokkis

54 minutes ago

 |
prev
 |
next

[–]

I'm building a financial censorship monitor at
https://nofunds.org/
, that tells a story of how money has been turned into a political weapon to silence journalists, activists, and civil society by freezing assets, blocking accounts, sanctioning, and banning payments. It's part of my master's thesis
https://www.doria.fi/handle/10024/187407
 and also
https://news.ycombinator.com/item?id=36430596
, but now I wanted to make a more comprehensive list, using Claude API and manual work. I'm designing a website right now, and the site is live within 2 months (given the API rate limitations currently to process articles). I know Hacker News is quite critical of Bitcoin, but it's also worthy to warn that, indeed, Bitcoin is at least a marginal tool to those whose bank accounts may be endangered. I'm basically arguing that Bitcoin can be used to resist such financial censorship, deplatforming and so on.

reply

jmmarco

1 minute ago

 |
prev
 |
next

[–]

Hello, I'm building
https://chargeradius.com
, a web app to help drivers find nearby EV chargers quickly and open directions instantly.

The idea came from wanting something simpler than a map-heavy charging experience when you already know roughly where you are and just want nearby options fast.It’s built with a Tesla integration, though the core charger lookup and directions can also be used without it.Still early, but live and iterating.

reply

paulmooreparks

6 hours ago

 |
prev
 |
next

[–]

I'm building Tela (
https://github.com/paulmooreparks/tela
), a self-hosted relay that tunnels TCP services through encrypted WireGuard connections. The key difference from Tailscale and similar tools is that it requires no TUN adapter, no root access, and no admin privileges on either end. It runs entirely in userspace.

My initial motivation was wanting to RDP and SSH into my home workstation from a locked-down corporate laptop when I travel. I couldn't install Tailscale on the laptop, and I didn't want to pay for a cloud VM just to do SSH port forwarding. Now I use it to tie together half a dozen machines, both locally and on Hetzner & Linode. I can SSH and RDP into remote machines, host a git repo on one machine and access it from the others, and (optionally) share files across all of them on a local mount.You run a hub (telahubd), register machines with a lightweight agent (telad), and connect from anywhere with the client (tela). All three are single Go binaries with no external dependencies. The hub never sees your traffic. It just relays opaque WireGuard ciphertext.All binaries run on Windows, Linux, and macOS. There is also a desktop GUI app, TelaVisor, that wraps the client and enables remote management of hubs and agents.It's Apache 2.0-license and pre-1.0 release, but I'm polishing it for a stable 1.0 release in the next month or so.I'm also working on an enterprise-grade management portal that works with Tela,https://awansaya.net/

reply

Ingon

50 minutes ago

 |
parent
 |
next

[–]

I've been working on a similar tool for a while - connet (
https://github.com/connet-dev/connet
). It builds upon QUIC (instead of wireguard), but I think from an enduser perspective the results ends up looking pretty similar.

reply

mentalgear

3 hours ago

 |
parent
 |
prev
 |
next

[–]

Very interesting - but I also find it important for solutions to state the trade-offs if they provide a novel approach that doesn't have the same requirements as the main contenders. In your case, what are the trade offs for running in user space ?

reply

paulmooreparks

2 hours ago

 |
root
 |
parent
 |
next

[–]

That's true. I'd say, probably performance is the first trade-off, weighing kernel against user-space. For the sorts of scenarios I envision for Tela, it's probably not a huge loss (I won't be running Facebook off of a Tela hub, I don't think). Another is that I have to run and tear down the client myself, though I do have support for running the tela client as a service.

It's funny... I've started using so many of the nifty management features of TelaVisor and Awan Saya that I am now considering adding lower-level support for the features that I explicitly wrote for user-space.

reply

watsonjs

2 hours ago

 |
parent
 |
prev
 |
next

[–]

> My initial motivation was wanting to RDP and SSH into my home workstation from a locked-down corporate laptop when I travel. I couldn't install Tailscale on the laptop

I'm not sure it would work but did you try running tailscale client through a docker container so it's not installed directly in your host system?

reply

paulmooreparks

1 hour ago

 |
root
 |
parent
 |
next

[–]

It would work, but this laptop is so locked down that I can't even install Docker without begging for permission (it's for a consultant role, not a dev role, so...). That said, my stop-gap solution while I worked on Tela was a cheap Linode VM with tailscale installed, and using SSH port-forwarding to get to RDP. Even at that tiny price, it grated me.

reply

rabbi7

28 minutes ago

 |
parent
 |
prev
 |
next

[–]

This is super cool.

reply

itake

3 hours ago

 |
parent
 |
prev
 |
next

[–]

I think this is the same as using a cloudflared tunnel?

to access my home desktop machine, I run:```
$ ssh itake@ssh.domain.me -o ProxyCommand="cloudflared access ssh --hostname %h"
```and I setup all the cloudflare access tunnels to connect to the service.

reply

paulmooreparks

1 hour ago

 |
root
 |
parent
 |
next

[–]

If I understand you correctly, you SSH in via cloudflared and then use that tunnel to reach other services through that session. That would work, yes.

Tela takes a little different approach. The agent exposes services directly through the WireGuard tunnel without SSH as an intermediary, so you don't need sshd running on the target. Each machine gets its own loopback address on the client, so there is no port remapping.The big difference is the relay, though. With cloudflared, Cloudflare terminates TLS at their edge. With Tela, you run the hub yourself and encryption is end-to-end. The hub only ever sees encrypted data (apart from a small header).

reply

Shorel

2 hours ago

 |
parent
 |
prev
 |
next

[–]

Now add an Android client and exit node support and it will completely replace Tailscale for me. :)

reply

paulmooreparks

1 hour ago

 |
root
 |
parent
 |
next

[–]

Thank you! That means more than you know. :) I've thought about an Android client. It would have the same problem that exit-node support would have: Tela is currently engineered as a user-space alternative to Tailscale. However, as I mentioned in another reply here, I've gotten so fond of a lot of the other features of Tela that I might consider adding support for low-level features that require kernel support. It might not be 1.0, but I'm open to suggestions.

reply

coldstartops

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Pretty cool! I see on enterprise edition you also support a virtual mount, is it FUSE based? I got a similar tool but went the other way around, I wanted to browse files synchronously (and bidirectional sync of edits) between two devices via FUSE mounts, and ended up tunneling TCP for this in the end.

reply

paulmooreparks

5 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks! The file sharing is part of the base, FOSS Tela. It uses WebDAV rather than FUSE. The tela client runs a local WebDAV server that proxies file operations through the WireGuard tunnel to the agent on the remote machine. You can mount it as a network drive (Windows maps it as a drive letter, Linux/macOS mount it as a directory) or access it via TelaVisor or the tela CLI. It can be configured as read-only or read-write. Certain file extensions can be banned from upload or rename.

I went with WebDAV because it works on all three platforms without a kernel module or extra driver. For my use case (browsing files, grabbing configs, etc.) it works well enough.Bi-directional sync is an interesting idea. Right now the sharing is one-directional (the agent exposes a directory, the client mounts it), but I could see adding something like that as a layer on top.

reply

hkntn

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Exactly what I was going to build for myself, no need now, very cool

reply

invalidSyntax

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Now that’s cool. I wished I new that when I was trying remote access my computer a few month ago.

reply

freakynit

6 hours ago

 |
parent
 |
prev
 |
next

[–]

Sooo freaking cool.

reply

electrodyssey

4 hours ago

 |
parent
 |
prev
 |
next

[–]

That's very useful!

reply

whiskey-one

6 hours ago

 |
parent
 |
prev
 |
next

[–]

Very cool

reply

digitaltrees

6 hours ago

 |
parent
 |
prev
 |
next

[–]

Awesome

reply

taylorhou

2 minutes ago

 |
prev
 |
next

[–]

Distributed ai inference pool for any Mac/iOS device where devices are paid for contributing unused ram. To help with the demand, also doing multiplayer AI. $0.05/million tokens - teale.com

reply

movedx01

4 minutes ago

 |
prev
 |
next

[–]

I am vibe-porting an old game, Knights & Merchants(actually its Delphi rewrite - KAM Remake) to WASM. It's going well, I even have multiplayer working at this point, will release it publicly at some point.

Learned more about WASM, OPFS, JSPI and other exotic browser stuff more than ever, also learned more about pascal than I ever wanted to, but it's been immensely fun.

reply

freakcage

2 minutes ago

 |
prev
 |
next

[–]

Android app for audiobookshelf with Admin functionality (Manage users, backups, logs, retc)

https://github.com/100nandoo/shelfdroid

reply

pi-victor

6 minutes ago

 |
prev
 |
next

[–]

I'm working on
https://opal.cloudflavor.io

It can run gitlab pipelines locally and assist you using AI to troubleshoot your pipelines.
I daily drive it now and it has seen hundreds or runs, but it's still in active development.
Building in a void, isn't much fun, so if anyone can use it and give me some feedback, i'd really appreciate it.
l.e.: It's not released yet, but it works really well on MacOS as an MCP using the Apple container cli.

reply

cmos

12 hours ago

 |
prev
 |
next

[–]

My mother is living alone in her house and we are getting to the point where she might not be able to live alone. I built "Still Kicking", a picture frame that monitors her motion and sends back basic reports and can detect falls and sleep quality to a phone app, to help give her more time at home.

It's just an mmWave sensor connected to an ESP32. But it works nicely, and I'm thinking of starting a company making them, though I'm not clear if the elderly would be ok with this minimal (no camera) intrusion.It would just work out of the box.. the real one would have a small cell modem so it wouldn't need any networking setup, and it would act as a gateway if you have more than one in a house. There are industrial versions of this for nursing homes. This would be a bit more warm and fuzzy for home use.https://moveometer.com

reply

digitaltrees

6 hours ago

 |
parent
 |
next

[–]

I own a national home care provider (in 13 states) and EHR. We are looking for products like this. Book office hours if you’re interested in discussing:

https://calendly.com/ryanwmartin/open-office-hours

reply

taylorhou

7 minutes ago

 |
root
 |
parent
 |
next

[–]

Booked a time! We built senior smartphone assistance without humans

reply

Aboutplants

20 minutes ago

 |
parent
 |
prev
 |
next

[–]

Start this company! You see the responses from just a small sample, this is your sign to go in on it! Good luck!

reply

lurkshark

8 hours ago

 |
parent
 |
prev
 |
next

[–]

There was a Minnesota company called Healthsense (was acquired by GreatCall which was then acquired by BestBuy, not sure if the company/tech exists anymore) that had a similar approach on a broader scale. Their system used a bunch of mundane smart home sensors in the usual configuration (e.g. contact sensors on doors, motion sensors, etc) but also for tracking patterns and habits, like the refrigerator door, toilet seat, bed, etc. The idea being that an abrupt shift in behavior would trigger a notice for a loved one or nurse to check in. I always thought this was a cool idea and it's a shame it didn't take off a bit more.

The question of "intrusion" was always interesting to me because old folks often face going from nothing to assisted living or nursing home which is often quite intrusive, where somewhat ironically adding a bunch of sensors to your home allows you a bit more privacy.Kind of a tangent, but I like your type of system as an alternative to the emergency pendants. It always struck me as strange to expect old folks at risk of fall to remember to charge and wear a pendant at all times.

reply

popupeyecare

4 hours ago

 |
parent
 |
prev
 |
next

[–]

I love it. As a physician, I see so many cases of elderly patients who have fallen and not been found for hours if not days.

In elder care, I am buildinghttps://statphone.com- one emergency number that rings multiple family members simultaneously and breaks through DND. Would love to chat/collaborate.

reply

akg_67

7 hours ago

 |
parent
 |
prev
 |
next

[–]

Look into some of the products and services used in Japan for elderly care at home.

My FIL, in his late 80's was living at home alone. My wife used a monitoring service, provided by local package delivery company. They installed motion sensors in the toilet and on the door. If no motion detected for 24 hours, the company will alert my wife by phone and send the nearest delivery driver to check on him.I myself have tried Home Assistant setup on Raspberry Pi and variety of sensors for different purposes.

reply

chrishh__

6 hours ago

 |
root
 |
parent
 |
next

[–]

I installed cameras in the toilet at my house

reply

nickk81

5 hours ago

 |
root
 |
parent
 |
next

[–]

Which way do they face?

reply

rjha

7 hours ago

 |
parent
 |
prev
 |
next

[–]

This was covered on HN a while back,
https://alvis.care/

reply

ricardo_lien

3 hours ago

 |
parent
 |
prev
 |
next

[–]

Your verification email is pointing to http://localhost:3000/ lol

reply

naikrovek

10 hours ago

 |
parent
 |
prev
 |
next

[–]

“Still Kicking” is a fantastic name for that.

reply

idorosen

12 hours ago

 |
parent
 |
prev
 |
next

[–]

I would buy it. I have built a similar contraption. Let's connect.

reply

pubba

4 minutes ago

 |
prev
 |
next

[–]

I'm building a simple daily crossword for developers. Just to take a small break from the daily grind.

https://crossword.sh

reply

cg-enterprise

48 minutes ago

 |
prev
 |
next

[–]

Me and a buddy of mine were sick of all things AI in our daily jobs, so we started to play around with different ways to use LLMs and landed on PitchSlap (
https://pitchslap.gg
).

You create arenas, which are thematic problem statements, submit ideas to solve it, and then vote on the best one, all with help of your avatar. The idea is to use AI as a part of the ideation process, which could be for things like hackathons (what can we build to solve x), evaluating business ideas, or in general just mess around with models. And the whole thing is wrapped in a high-concept anime corporate parody style.There are also battles, which are shorter simpler versions of arenas and showdowns, which are supposed to be a follow up to arena, where you flesh out the winning idea - answer a set of questions about the idea and again vote on the best answer.We have a bunch of features and ideas to take the concept forward (credit style economy, where you play for "slaps"; fully automated mode, where AI driven avatars hash out the whole game-play cycle and you can observe, RPG-style attributes for the avatars that have more significant impact to the pitch generation process), but have in general enjoyed the process of using these technologies for something a little less serious.

reply

DevDesmond

14 hours ago

 |
prev
 |
next

[–]

I got addicted to scrolling content on my phone, so I built a digital pet whose growth and well-being depends on you staying off your phone! This way, if I spend all night scrolling the browser, my pet will get depression.

Unlike similar apps such as Focus Friend or Forest, which use active timers to police screen time, my app is an inversion that works like an idle game; All screen time is tracked all day, (with double the punishments at night), and upon check-in, you get feedback on your device usage.https://automatisolutions.com/products/phreepet/

reply

varenc

10 hours ago

 |
parent
 |
next

[–]

How are you able to track all screen time on an iOS device? I had thought the APIs to do this aren't available.

reply

buddybuilder

9 hours ago

 |
root
 |
parent
 |
next

[–]

I believe Apple opened up their screen time APIs
https://developer.apple.com/documentation/screentime

reply

memonkey

7 hours ago

 |
parent
 |
prev
 |
next

[–]

I've always been very interested in these types of games. Grew up playing Neopets which was inspiration to becoming a software engineer. Am interested in gamified aspects as well. The thing I've not quite figured out is how to make these types of games _actually_ addictive? Neopets had a lot going for it IMO. Would love to know if this is actually working for you (and maybe others) personally and why.

reply

bitmerse

11 minutes ago

 |
prev
 |
next

[–]

I am working on bUniProbe (
https://www.crowdsupply.com/bitmerse/buniprobe
), an open-source wireless hardware debugger. I was tired of juggling separate USB adapters for SPI, I2C, UART, CAN and GPIO and wiring up external level shifters just to switch between 3.3V and 5V targets.

To fix this, I built a single Wi-Fi connected board that handles it all. It hosts its own web server, so you can monitor signals, read/write data, and toggle hardware pull-ups directly from your browser without installing drivers. I also added a waveform viewer and a REST API for all interfaces, making it easy to automate hardware testing with Python scripts.Hardware and firmware will be fully open-source. We are currently in pre-launch on Crowd Supply.

reply

paulhebert

14 hours ago

 |
prev
 |
next

[–]

I'm continuing to hack on Tiled Words, my daily word puzzle!

https://tiledwords.comAfter winning the Playlin Player's Choice award I've noticed an uptick in players as well as some people sharing videos on YouTube which has been fun. I've got a few thousand people playing every day.I just launched user accounts today so user's can now track their progress across devices and share their stats with each other. This ended up being a bigger chunk of work than I expected but I'm really pleased with how it turned out. (Though I launched it 15 minutes ago so I'm holding my breath for bug reports)I'm fine-tuning my internal puzzle-building now with the goal of letting people use them to make and share their own puzzles soon!

reply

martimchaves

2 hours ago

 |
parent
 |
next

[–]

I love tiled words, I've actually been doing the daily puzzle for a while, have completed over a 100 of them! It's part of my morning routine :)

I'm not sure if it would fit the theme, but sometimes I end up searching what an expression means, or where does it come from. Maybe it would be cool to have a little info box after you discover what the word is. Just an idea! Not sure if it would clutter things, and you can always search it yourself, but something I've been thinking about. I still remember looking up peanut gallery and sand dollar!

reply

mockingloris

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Thanks for making this. It's totally refreshingly intuitive while doing the practice puzzle!

Just tried it out on my browser. Will be following this.Also would love to see your workflow you spoke about, on coming up with puzzle ideas and tile arrangements. Cheers!

reply

lilygirl85

1 hour ago

 |
parent
 |
prev
 |
next

[–]

I just tried this out for the first time and really enjoyed it!

reply

dodu_

7 hours ago

 |
parent
 |
prev
 |
next

[–]

I can't say I'm a regular user but a while ago I stumbled upon another post about tiledwords while a loved one was in the hospital and it was a fun and welcome distraction to solve some of the puzzles together while stuck in an otherwise grim environment.

Thanks for making this and I wish you all the success in the future.

reply

paulhebert

7 hours ago

 |
root
 |
parent
 |
next

[–]

I’m glad Tiled Words could make that hard time a little easier. I hope your loved one has recovered and is doing better now

reply

panja

1 hour ago

 |
parent
 |
prev
 |
next

[–]

I play this every day with my friend group :)

reply

rnoorda

11 hours ago

 |
parent
 |
prev
 |
next

[–]

I've been enjoying Tiled Words! I find myself playing in a weird way, by totally ignoring the clues. I look at the title and try to puzzle out all the answers myself. I don't know if I'm alone in that, but it could be a neat mode to have a setting to hide the clues.

reply

paulhebert

9 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks! I’ve heard that from a few people! Adding that as an official mode is on my road map but there are a few big features ahead of it right now

reply

rjh29

5 hours ago

 |
parent
 |
prev
 |
next

[–]

It's fun, impressed by how polished it is.

reply

vlatoshi

11 hours ago

 |
parent
 |
prev
 |
next

[–]

this is so cool, i liked the musical instruments one!

would be super interested to hear more about the puzzle-making process too, is it fully automated with AI at this point or is there still a good amount of manual work and fine-tuning involved?bookmarked already, can't wait to play tomorrow again

reply

paulhebert

9 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks!

It’s a lot of manual work right now. I don’t use AI in the process. I think it could help with some of the brainstorming but I kind of like the human connection of making a puzzle and having people solve it.Here’s the basic process.My wife and I do this part together:- Think of a theme- Think of words related to that theme, ideally with a second meaning- Think of clues for those wordsOnce we have a good set of clues I plug them into a program I wrote to make crosswords.The program isn’t that smart. It tries making random crosswords. I run it 1500 times and then sort the results to get the best ones. This brute force approach works pretty well for how simple it is.I pick the crossword I want and then I use another tool to split up and rearrange the tiles. This step could probably be automated but there’s some finicky logic to the best way to split up the tiles and it goes pretty fast manually.I’ve been meaning to make a video of the process! I’ll share it here when I do

reply

tele_ski

11 hours ago

 |
parent
 |
prev
 |
next

[–]

Very nice, the movement and snapping of the tiles is very nicely done, enjoyed today's puzzle!

reply

paulhebert

9 hours ago

 |
root
 |
parent
 |
next

[–]

Haha I spent a looong time perfecting that so I’m glad it’s appreciated!

reply

kvirani

13 hours ago

 |
parent
 |
prev
 |
next

[–]

Oh wow. This seems like it was a lot of work. Bookmarked and installed!

reply

paulhebert

12 hours ago

 |
root
 |
parent
 |
next

[–]

Haha yeah it’s been a labor of love!

The design and dev took a while but building the has been the most time consuming at this point. My wife and I make the puzzles together.We’re getting close to 6 months of daily, hand crafted puzzles!

reply

deivid

13 hours ago

 |
parent
 |
prev
 |
next

[–]

Have played it a few times, it's really good

reply

paulhebert

13 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks!

reply

SpyCoder77

11 hours ago

 |
parent
 |
prev
 |
next

[–]

This is going on my daily puzzle list!

reply

paulhebert

9 hours ago

 |
root
 |
parent
 |
next

[–]

Awesome, thanks!

reply

digdeep

11 hours ago

 |
parent
 |
prev
 |
next

[–]

That's a very fun puzzle, nice work! I'll be telling my friends.

reply

paulhebert

9 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks!

reply

sqircles

12 hours ago

 |
parent
 |
prev
 |
next

[–]

This is great!

reply

paulhebert

11 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks!

reply

antonio-pp

5 minutes ago

 |
prev
 |
next

[–]

PricePush (pricepush.app), automating localized pricing for mobile apps. Calculates PPP-adjusted prices for 190+ countries and pushes them to App Store Connect and Google Play in one click. Built it because managing prices across 175 Apple storefronts for my own 8 apps was taking entire weekends.

reply

msolomentsev

9 hours ago

 |
prev
 |
next

[–]

I've been writing a 'book' (more of an extended blog post that I'd like to put out for free) attempting to explain quantum computing to a layman-ish audience.

I sort of got inspired to do this after seeing so many QC PR posts on HN, and finding the educational material in this space to be either too academic, too narrow in scope, or totally facile. I think given the incredible hype (and potential promise) of this industry, there should be on-ramps for technically minded people to get an understanding of what's going on. I don't think you should need to be a quantum physicist to be able to follow the field (I am only an electrical engineer).My book tries to cover the computational theory, the actual hardware implementations, and the potential applications of quantum computers. More than that, I want to be unbiased and stray away from what I feel is misleading hype. It's been a work in progress for about 6 months now, with a lot of time spent gaining fluency in the field. But the end is in sight! :)

reply

wonger_

9 hours ago

 |
parent
 |
next

[–]

Awesome! Anywhere we can look for updates, like a website?

FWIW, my shallow understanding of quantum computing as a programmer, in case you wanted perspectives from your potential audience:- I thought quantum physics was a sham? Like on par with string theory. But apparently that's not true- I hear QC only breaks certain kinds of cryptography algorithms (involving factoring big primes?), and that we can upgrade to more foolproof algorithms.- I hear that one of the main challenges is improving error bounds? I'm not sure how error is involved and how it can be wrangled to get a deterministic or useful result- Idk what a qubit is or how you make one or how you put several together

reply

arter45

6 hours ago

 |
root
 |
parent
 |
next

[–]

No, quantum physics is not a sham. Lasers are an application of quantum physics, for example. Usage of quantum physics principles in non scientific (thoughts are entangled!) or arbitrary macroscopic contexts (since electrons can cross a barrier, a human can pass through a wall) is an entirely different thing.

reply

rcbdev

7 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I would be very interested where you got some of these misconceptions and half-truths.

reply

electrodyssey

3 hours ago

 |
parent
 |
prev
 |
next

[–]

I'd like to see that post when it's ready!

reply

bnjemian

7 hours ago

 |
parent
 |
prev
 |
next

[–]

Would like to check this out when you're ready to share.

reply

stanko

4 hours ago

 |
prev
 |
next

[–]

https://muffinman-io.itch.io/spacedeck-x

I'm still obsessed with making my game, which you can try it at the link above (it is desktop only). This is my first "real" game, and it has been incredibly fun and rewarding. I've been working on it in the evenings for about 4 or 5 months.It is a very ambitious mix of genres - shoot-em-up and deck-building. A lot of people said that those are genres that shouldn't be combined, but I think it turned out to be a fun little game. Folks who are not fans of one (or either) of the genres are actually playing it. I built a global high-score leaderboard, and there are people (including a few of my friends) competing on it. Whoever knocks my friend "BER" from first place will earn a beer from me.This is purely a fun project, although I'm now seriously considering releasing it on steam when I finish everything I planned for it. It is made in Kaplay, a small JavaScript gamedev library, which is a big part of what makes it fun. If you try it out, please leave a comment, I would love more feedback!

reply

rrr_oh_man

4 hours ago

 |
parent
 |
next

[–]

OH MY GOD THIS IS GOOD.

Loved the music.Didn't know what was going on half the time.Positively overwhelmed.Thanks for that little spark of joy!

reply

stanko

4 hours ago

 |
root
 |
parent
 |
next

[–]

Haha amazing, thank you! This made my morning :)

If I ever release on steam, can I please use your comment in promo material? I would anonymize it of course.Edit: grammar

reply

rrr_oh_man

4 hours ago

 |
root
 |
parent
 |
next

[–]

Absolutely. I'd buy it and leave a review, too. :)

reply

stanko

3 hours ago

 |
root
 |
parent
 |
next

[–]

That’s very kind of you, thank you!

reply

marcusdev

15 hours ago

 |
prev
 |
next

[–]

I'm working on a fully offline, client-side train journey planner for UK rail -
https://railraptor.com

When booking flights, I use sites like Kiwi and Skyscanner that let you do flexible searches - multiple destinations, custom connections, creative routes, etc. But rail search feels oddly constrained. All the UK train operators offer basically the same experience, and surface the exact same routes. I always suspected there were better or just different options that weren’t being shown. Where is the "Skyscanner for trains"?After digging through the national rail data feeds, I decided to have a go at building my own route planner that runs completely offline in the browser. This gave me the freedom to implement more complex filters, search to/from multiple stations, and do it without a persistent network connection.Now I'm finding routes that aren't offered by the standard train operators, connecting at different stations, and finding it's often easier to travel to different stations (some I'd never heard of) that get me closer and faster to where I actually want to go!It's still a little rough and I'd like to add more features such as fares, VSTP data, and direct-links to book tickets, but wanted to share early and get some initial feedback before investing more time into it. So, thanks in advance - let me know what you think.

reply

svenmakes

40 minutes ago

 |
parent
 |
next

[–]

Great that it stores the entire timetable in only 6MB(?) of storage.

Some feedback: I don't think it can route through London as it isn't aware of tube connections between stations? And the classic stress test of Penzance to Thurso is too long for the routing algorithm, but I imagine that's beyond scope?Pricing would make this a super useful tool!

reply

jimnotgym

4 hours ago

 |
parent
 |
prev
 |
next

[–]

I like your idea. If you dig around Rory Sutherlands YouTube appearances he talks about how train routers fall down by always looking for the fastest route, where he would prefer the nicest, often cheaper and slightly slower. He has a fair amount to say on the subject so it is a bit of a goldmine.

I sent you some feedback on a routing failure because I didn't want to post exactly where I live here.I think you need pricing. Works offline is cool, but why not pull in the pricing if people are online? Train fares are so variable depending on time of day, especially if they go via London. I could have a trip that could be £300 cheaper by taking a 30 minute longer trip that avoids London. I need pricing to get my best journey.

reply

vectorcrumb

14 hours ago

 |
parent
 |
prev
 |
next

[–]

This sounds very nice! A slightly adjacent question: have you discovered any providers that can recommend train journeys based on price? Sort of like the explore feature you find on sites like Google Flights, Ryanair and Flixbus. Sometimes when the wanderlust hits I've tried searching around for cheap train tickets, but it isn't simple using sites likes DB/OEBB/SBB/SNCF/etc

reply

marcusdev

13 hours ago

 |
root
 |
parent
 |
next

[–]

https://raileasy.co.uk
 /
https://trainsplit.com
 is the most flexible existing service I've found, but even that doesn't give you an "anywhere" option.

I'm looking at how to add price data to railraptor, but it might mean sacrificing the fully-offline capability... once I have prices it should absolutely be possible to build a filter along the lines of "find me the cheapest popular destinations that are at least 50 miles away".

reply

whiplash451

14 hours ago

 |
parent
 |
prev
 |
next

[–]

This sounds awesome. Have you checked how it fares against trainline? A quick demo would be very nice.

reply

boutell

14 hours ago

 |
parent
 |
prev
 |
next

[–]

I love this! Dijkstra's Algorithm is always a fun time

reply

marcusdev

13 hours ago

 |
root
 |
parent
 |
next

[–]

I do love Disjkstra :) this actually uses a modified version of the "Raptor" algorithm for public transport routing (hence the name!):
https://www.microsoft.com/en-us/research/wp-content/uploads/...

reply

hk__2

43 minutes ago

 |
prev
 |
next

[–]

Not a big thing, but I’m happy to work again on a side project I started last year and abandoned because of some limitations from the stack I chose.

It’shttps://napodico.it, a very simple online Neapolitan dictionary. Nothing extraordinary here but it’s something that will tremendously help me organize my notes on Neapolitan words and expressions that are currently scattered across Google docs. I’ve builthttps://www.schedarionapoletano.itin the past but it’s from a dictionary made my someone else and I didn’t want to mix my own definitions in.This is not a 'product', it’s a normal free website as we used to do before the commercial Web became the norm. The front is very simple, but the entries can be edited in the back a bit like a CMS but with Wikipedia-like inter-links and redirects.The stack I started with was SvelteKit and Drizzle for the ORM, but I quickly hit several limitations of Drizzle and I abandonned the project. Last week I asked Claude to split it into the more familiar stack that I used to use before trying to fit everything into a single TS project that is: one Python app (FastAPI/SQLAlchemy) for the backend that exposes a REST API consumed by the front app (SvelteKit). This is a lot more flexible, and it has allowed me to work again on the project.

reply

3D30497420

53 minutes ago

 |
prev
 |
next

[–]

I'm building a physical interface for smart homes. Real buttons, real dials, screens that show info at a glance. All local, no subscriptions, and open-source.

https://weavepanel.comWould love any feedback you may have!

reply

zeafoamrun

11 minutes ago

 |
prev
 |
next

[–]

My wife made a silly browser based arcade style Kanban board management game called Kanban Chaos
https://kanbanchaos.com/

reply

rrvsh

10 hours ago

 |
prev
 |
next

[–]

Trying to figure out how to get a job in this market for someone with sub 3 YoE in the industry :/ It's hard out there for juniors, y'all. I'm working at a company that I thought I could stay for years in, but my CTO left and now I'm shafted with basically all of their responsibilities - I'm not overly perturbed by this, as it's well within my ability, but I would much rather spend the next few years as an IC and really develop my skills as a SWE rather than jumping to manager this early... Also just getting an interview is insanely hard nowadays for some reason!

reply

amysox

8 hours ago

 |
parent
 |
next

[–]

It's hard out there for
everyone
 in this market. I've got literal
decades
 of experience, but I've been pounding the virtual pavement for month after month, and still nothing.

reply

atlgator

7 hours ago

 |
root
 |
parent
 |
next

[–]

same.

reply

mittermayr

1 hour ago

 |
root
 |
parent
 |
next

[–]

20 solid years of experience, self-employed at the moment, but I got curious a while back and started browsing jobs, and it's ... well, tough to even find something unless you're an extreme specialist and trust to bank on that technology or niche sustaining you through the next few years.

reply

MrDresden

5 hours ago

 |
parent
 |
prev
 |
next

[–]

To be honest it sounds like you hit the jackpot there.

You say this is a company you could see yourself working at for some time, and have been handed C suite level responsibility that you can handle. So seemingly you are content and able to handle the work load.Learning to be a IC is something anyone can do given time, but learning to be a manager can only be learned by being on the job, if you are able to get it in the first place.Now is really not a good time to jump ship, unless you know for certain that the new position is going to be stable.Grab the opportunity, do a good job and perhaps study how to be a better IC in your free time. You'll come out on the other side with skills and experiences that many in this field will be missing.

reply

opesorry

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I'm with you on this. I will hit 3 YoE in June and have been doing excellent in my current role yet having no luck finding a new job. Interviews are hard to come by and I'm a month out on even getting a rejection reply from some companies.

reply

hariwb

8 hours ago

 |
root
 |
parent
 |
next

[–]

i'm interested in hiring early career people for my company - feel free to reach out to me at the email in my profile if you're interested

reply

hariwb

8 hours ago

 |
parent
 |
prev
 |
next

[–]

i'm interested in hiring early career people for my company - feel free to reach out to me at the email in my profile if you're interested

reply

mauvehaus

12 hours ago

 |
prev
 |
next

[–]

Earlier today? My partner and I felled a couple of trees and bucked them into firewood to clear a spot on drier ground for our chicken coop, which had sunk halfway to China because we unknowingly landed it in a soup bowl three years ago when we moved in the winter when the ground was frozen. Also set and leveled four piers in the new spot for it to sit on.

Then slid it a few hundred feet across the lawn on composite deck boards we salvaged when we took a balcony down last year and landed it atop the new piers.Then put the electric fence back up to keep the bears out.Presently? A beer.

reply

jeanlucas

10 hours ago

 |
parent
 |
next

[–]

Woah woah woah slow down, what kind of beer it was?

reply

Rohunyyy

7 hours ago

 |
root
 |
parent
 |
next

[–]

Move on Linux vs Windows we gonna do beer fights now. Stage 1. Light beer vs Dark beer let's go

reply

maxalbarello

39 minutes ago

 |
prev
 |
next

[–]

While playing around with OpenClaw I realized that after a few days of adding skills, plugins, crons, etc. things were all over the places. Memory files spread everywhere in the workspace, plugin configs stored here and there, skills not always visible to crons, ...

I started working on a CLI to keep OpenClaw organized:https://clawtique.aiThe analogy is that of a boutique. OpenClaw goes to the boutique and is "dressed up" properly so that all the various components are organized and easy to maintain. Clawtique is organized around the concept of a "dress", basically a bundle of everything OpenClaw needs to achieve a goal (skills, plugins, memory segments, crons, ...). The CLI enables users to easily dress and undress OpenClaw so that you can try out a dress and easily remove it without leaving any dangling dependencies.Some dresses i created are the sleeping-coach (bundles the OuraClaw pluginhttps://github.com/rickybloomfield/OuraClawwith skills and crons that notify you on how you slept) and the fabric-sync (bundles the fabric pluginhttps://github.com/onfabric/openclaw-fabricwith skills and crons to maintain an accurate USER.md of you based on your interactions on the various big tech platforms).The follow up is to have OpenClaw use the Clawtique CLI itself so that it can easily dress and undress with whatever it needs to accomplish the goal without everything becoming an unmanageable mess.Here is the repo:https://github.com/onfabric/clawtiqueCurious to know what you guys think

reply

jamincan

52 minutes ago

 |
prev
 |
next

[–]

It's not very impressive, but I decided I wanted to get better at recognizing NHL jersey numbers and was frustrated with the options available to learn (out of date Sporcle quizs and the like), so I tossed together a flashcard game with the help of Claude.

It pulls data directly from the NHL to stay up-to-date with changes to the roster, but is otherwise a pretty straight-forward and basic sveltekit app.I've toyed with using AI for stuff like this (my day job isn't coding related), and this was consistent with previous experiences where I found it helpful in some respects (especially all the css and stuff which I don't really know too well), but it could also get stuck and produce some awful messes trying to fix it. I pulled this together mostly over the course of a couple hours, though, which definitely wouldn't have happened if I did it from scratch.https://numbrrs.cato play orhttps://github.com/jamincan/numbrrsif you have contributions or feedback.

reply

dwighson

19 minutes ago

 |
prev
 |
next

[–]

Building Warp (
https://warp.thegeeksquad.io
), a storage engine where each entity is its own actor with its own SQLite shard.

I've been doing DDD and event sourcing for years but always had to squeeze aggregates and domain events into Postgres tables. I kept looking at what scaling would mean with CockroachDB or ScyllaDB and it scared me. So I asked what happens if you just make SQLite the storage and let the BEAM handle concurrency, one actor per entity.Turns out it works pretty well. 1.5M events/sec on an M1 in Docker with 5 cores. ScyllaDB on the same hardware does 49K. Written in Gleam, but there's a TypeScript SDK if you just want to use it from Node.

reply

aristofun

15 minutes ago

 |
parent
 |
next

[–]

How do you solve HA?

reply

tkael

9 minutes ago

 |
prev
 |
next

[–]

I'm building a workspace for thinking with AI. Think what Cursor did for coding, but for rigorous thinking.

I believe the direction toward persistent, proactive, remembers-everything AI is the wrong one for thinking. AI should be used as a selectively invoked sparring partner.

reply

minikomi

3 hours ago

 |
prev
 |
next

[–]

A generalized llm prompting library for clojure, and seeing what falls out from that. I wanted something which was fun to use in an interactive way, but not too abstracted.

- Introduction:https://poyo.co/note/20260318T184012/- Tool loops:https://poyo.co/note/20260329T034500/- Playing with receipt extraction:https://poyo.co/note/20260323T120532/- Use with async flow:https://poyo.co/note/20260410T164710/

reply

jpfaraco

8 hours ago

 |
prev
 |
next

[–]

Finally being able to build something I've wanted for years: an alarm app that wakes me up 1 min earlier each day until I reach my wake time goal. Not sure if there is already anything like this out there, but I don't really care. I've been learning a ton about native Android development and so far it's been a painless process to be able to wake up earlier.

reply

conductr

6 hours ago

 |
parent
 |
next

[–]

Bravo on the learning! Now regarding the app idea, is it really that hard to just change the native alarm by a minute for someone that was interested in this? If that's hard, actually waking up when the alarm goes off earlier seems more of an issue as well. Might just be me but I'm a perpetual snooze button user.

reply

mschild

3 hours ago

 |
root
 |
parent
 |
next

[–]

> is it really that hard to just change the native alarm by a minute for someone that was interested in this?

Not OP. In theory? No. Takes a second to change it. To be quite honest, its yet another thing to keep track off and do. I know, for myself, I would remember to do it for a few days and then forget.Its a tiny thing but the more I can outsource the better. My brain is occupied with enough other stuff.

reply

antoineMoPa

8 minutes ago

 |
prev
 |
next

[–]

I vibe-coded a tiny local code review tool, a bit like pull-requests, but an agent does the work immediately.

https://github.com/antoineMoPa/moonreviewThe intended use is to run `moonreview` instead of `git status` / `git diff` or `magit`, but you can add comments and they get auto resolved. You can also stage hunks if you are happy with them.Probably other tools exist or will appear in this space (I saw at least another one in the comments on this post), but i think there is something fundamentally too slow and dumb with current corporate code reviews. People are reviewing other people's slop and most of the comments are probably fed back into an agent. So why not have the whole process be done upfront by the original developper. Another cool thing I saw people do is to attach claude to github PR comments, which I think is great and love to work with this, but it's even better if we can also have this locally to catch sloppy code before it even reaches github.

reply

pmbanugo

1 hour ago

 |
prev
 |
next

[–]

I've been thinking about concurrency and distributed messaging system for a while now. I started tinkering with various aspects of ZeroMQ, then explored designs and protype-implementation of a QUIC-based message protocol (like an alternative to NATS and similar). Hit some roadblocks and went back into thinking about concurrency and async I/O.

Then after a few pivots I landed on a good design for a framework which embodies what I'd like to see about programming concurrent systems without the gotchas of today's primisitives (e.g. callbacks/promise hell).So I recently open sourced it (https://github.com/pmbanugo/tina). It's a high-throughput concurrency framework that bridges the Erlang-style concurrency with native performance (no VM, no GC).One other area I'm interested in is formal method design using TLA (by Lamport). But I'm still scratching the surface on that one.

reply

jonshamir

1 hour ago

 |
prev
 |
next

[–]

https://prepbook.app
 - modern recipe manager
 As simple to use as notes, with clever culinary capabilities :)

reply

spudlyo

16 hours ago

 |
prev
 |
next

[–]

I'm writing an essay about how I use an ancient text editor, GNU Emacs, along with gptel, Gemini, some local models, yt-dlp, and patreon-dl to help me me study an ancient language, Latin.

I want to show how I liberate poorly aligned, pixelated PDF image scans of century-old Latin textbooks from the Internet Archive and transform them into glorious Org mode documents while preserving important typographic details, nicely formatted tables, and some semantic document metadata. I also want to demonstrate how I use a high-performance XML database engine to quickly perform Latin-to-English lookups against an XML-TEI formatted edition of the 19th century Lewis & Short dictionary, and using a RESTXQ endpoint and some XQuery code to dynamically reformat the entries into Org-mode for display in a pop-up buffer.I intend demonstrate how I built a transcription pipeline in Emacs Lisp using tools such as yt-dlp and patreon-dl to grab Latin-language audio content from the Internet, transcode the audio with ffmpeg, do Voice Activity Detection and chunking in Python with Silero, load the chunks into Gemini's context window, and send it off for transcription and macronization, gather forced-alignment data using local a local wav2vec2-latin model, and finally add word-level linguistic analysis (POS, morphology, lemmas) using a local Stanza model trained on the Classical corpus.This all gets saved to an an XML file which is loaded into BaseX along with some metadata. I'll then demonstrate some Emacs Lisp code which pulls it into an Org-mode based transcription buffer and minor-mode for reading and study, where I can play audio of any given Latin word, sentence, or paragraph, thanks to the forced-alignment and linguistic analysis data being stored in hidden text properties when the data was fetched from the database.Lastly, I'd like to explore how to leverage these tools to automatically create flash cards with audio cues in Org mode using the anki-editor Emacs minor mode for sentence mining.

reply

sneilan1

15 hours ago

 |
parent
 |
next

[–]

This is insanely cool. Thanks for sharing. I'll follow you on
https://muppetlabs.com/
.

reply

phyzix5761

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Emacs is ancient? I use it every day. And they just came out with a new major update.

reply

hirako2000

4 hours ago

 |
root
 |
parent
 |
next

[–]

It is ancient. The UX still has the same feel. Without a major revamp (which would be a terrible idea) we can still call it ancient. A perfect fit for antique studies.

reply

ElSchorschoDE

48 minutes ago

 |
prev
 |
next

[–]

I'm building a chaotic, physics-driven first-person woodcutting game:
https://store.steampowered.com/app/4521770/Drunk_Woodcutter/

I was splitting wood in real life, and even though it's a chore, it's oddly satisfying work, too. Every hit feels different, sounds different, every piece of wood splits in different ways. I want to catch that vibe and put a good dose of comedy on top.It's using realtime mesh cutting for the splitting, and I recorded 48 different chopping sounds for it :D

reply

jiehong

1 hour ago

 |
prev
 |
next

[–]

Working on working out and less IT.

I wish I could use auto completion for building muscle. Maybe a Large Muscle Model? (Joke).

reply

codencoffee

2 hours ago

 |
prev
 |
next

[–]

I am building
https://mealdone.com

I love cooking but the daily "what do you want" grind was killing me. Rushing to the store after work hoping for inspiration but leaving with the same five fallback meals. Recipes using half a box of something so you eat the same thing twice or watch leftovers die in the fridge.The final straw was our newborn's milk protein allergy, turns out milk is in everything. Recipe sites are hostile. Ads reload and jump the page mid-sentence, 20 versions of every dish, comparing the 4.7 star rating version with the 4.8 star one. So you go by thumbnail. Visual clutter everywhere.I tried the apps. One does swiping, one does shopping lists, one does Sunday budget planning, one has "what's in my fridge" mode. Pick your half-solution.So I built what I wanted: swipe mode that makes picking dinner fun again, or instant 3 quality suggestions for when I am in the store. Aisle oriented shopping list, budget, personal taste, fridge inventory in one place. UI looks like a restaurant menu — off-white, black text, no glossy photos. I'm working on AI mode now. Not for recipe generation, which are mostly garbage, but for search and substitution.

reply

archi42

1 hour ago

 |
parent
 |
next

[–]

Are you going to localize this? Using US recipes works only okay-ish: I usually have to figure out local substitutions for some ingredients, and transform units.

Anyway, amazing idea and I absolutely feel you. Recipe sites (and search engine results) are cluttered like hell, that's why I started collecting recipes in Mealie. But in practice this merely bumped my pool from "five fallback meals" to "10 usual recipes, which mostly cover my eating preferences since I'm the only one in the household putting recipes into Mealie".

reply

andai

2 hours ago

 |
parent
 |
prev
 |
next

[–]

So... what does it do? You made it sound like Tinder for food. (I am assuming the food always swipes right!)

reply

codencoffee

2 hours ago

 |
root
 |
parent
 |
next

[–]

- Tinder for food when you need to agree with the household. Both swipe, matches become dinner picks.

- Pick mode for when you're in the store looking like a deer in headlights at the produce section. It gives you 3 solid options instantly.- AI mode (WIP) for "something with chicken, but I also have carrots in the fridge that are going bad."Plus aisle-sorted shopping lists for everything. No more backtracking at Aldi.

reply

andai

1 hour ago

 |
root
 |
parent
 |
next

[–]

Thanks. Btw you sound like ChatGPT

reply

lilygirl85

2 hours ago

 |
parent
 |
prev
 |
next

[–]

I stress at all the steps for planning and making dinner - especially finding a good recipe that won't take too long! At the moment I'm utterly dependent on Hello Fresh to be able to make a nice dinner. MealDone could be a potential replacement, where dinner is planned for the week but instead of having the items delivered, I can buy it cheaper at the store.

For me, having a selection of high quality recipes would be important. For more experienced cooks like my husband, he would just tweak on the fly or use his own recipe anyhow and would enjoy being able to plan with the household and have a shopping list.Good luck with the project!

reply

codencoffee

1 hour ago

 |
root
 |
parent
 |
next

[–]

That's pretty much the same setup we have at home. When we tried their service it was a bit expensive and came with a lot of packaging.

Thanks a lot.

reply

popupeyecare

11 hours ago

 |
prev
 |
next

[–]

Im building
https://trypixie.com
 to legally employ my 7 year old child, save on taxes and contribute to her Roth IRA.

I also builthttps://statphone.com- One emergency number that rings your whole family and breaks through DND.

reply

phyzix5761

9 hours ago

 |
parent
 |
next

[–]

You're working on some pretty cool stuff. Saved to see progress in the future.

Do you have a personal blog or github page?

reply

popupeyecare

9 hours ago

 |
root
 |
parent
 |
next

[–]

I have
https://amithpatel.com
. It needs some updating.

reply

phyzix5761

9 hours ago

 |
root
 |
parent
 |
next

[–]

Thank you

reply

Xantier

1 hour ago

 |
prev
 |
next

[–]

Tinkering around building
https://viberglass.io
. It started off as a way to allow my wife to keep her website up to date without any coding skills, but ended up growing arms and legs.

It is a hosted ticketing system/agent harness platform with integrations towards other ticket systems and chat apps. It allows triggering agentic (coding) tasks without the need to context switch and/or know anything about installing the wanted tools, SDKs, IDEs etc. Ephemeral workloads in isolated containers or cloud compute. Trying to help commoditize small scale development tasks and and prevent them from getting lost in the void of the backlog.Open source with local or AWS self-hosted, full IaC attached.

reply

dandaka

3 hours ago

 |
prev
 |
next

[–]

I'm building Kardo (
https://kardo.cards/
), AI tutor that listens to your calls with a teacher and creates cards for repetition.

I live in Lisbon and I've been learning Portuguese with a tutor since 2022. After every lesson I'd sit down and make flashcards from my notes and screenshots. Spaced repetition works, but making the cards took manual effort each time. Most days I just didn't do it. So I have automated that process.The flow: you invite the Kardo bot to your call, it records and transcribes (Recall.ai + Deepgram Nova 3), then GPT-4o extracts vocabulary from the transcript and generates cards. You review them with spaced repetition — we use FSRS, which is the best open algorithm I could find. If you already use Anki or Mochi Cards, there's export.You can also throw in YouTube videos, podcasts, articles, PDFs — not just live lessons.Tech: built entirely with Claude Code. React + Vite frontend, Bun + Elysia backend, Convex for the database, Railway for hosting.We got 50 beta users through Telegram, and just landed our first paying customer. Now we're trying to figure out distribution — tutors seem like the obvious channel because one tutor recommends you to all their students, but reaching them with zero marketing budget is the hard part.Curious if anyone here learns a language with a tutor and what your review workflow looks like.

reply

ddtaylor

14 hours ago

 |
prev
 |
next

[–]

I have been making GTK applications so that people can manage MergerFS and LUKS encrypted hard drives without knowing how to be a sysadmin.

The use case is kind of neat. RAID is great and can mostly solve these problems, but people don't have SATA hardware that can handle the workload well, plus they aren't ready to manage an array like that, and they don't like having to use specific sized drives, etc. Another major issue with those setups is you need to be careful because an IO error that you don't recover from will be very difficult or impossible to recover from because of the layers of LUKS combined with LVM.With MergerFS you just use regular file systems that are separate, but they get combined into a single mount point. That means each disk can just be a different LUKS encrypted drive and if you need to recover data it's isolated to that one disk and much more manageable. You can also take any disk and plug it into another machine as needed and grow or shrink the storage pool as needed.MergerFS has options and settings to help you determine how files are spread across the drives, such as least space used or which disk has the most of that directory path already.My app (Chimera) automates the unlocking of the disks, mounting and some data migration if you want to remove a disk from the pool. I plan to add some rclone features to help provide easier backup options to places like Backblaze, AWS, or a remote server in general.So far so good and I was surprised at how well Opus had been handling Gtk and pkexec.Let me know if you guys are interested I am close to pushing some RPMs and DEBs, in addition to the standard Python stuff.

reply

Grisu_FTP

5 hours ago

 |
prev
 |
next

[–]

A Minecraft Mod that outputs the Stats of the players onto a website (I made it use APIs, so an app or CLI tool would be easy to create later on).

This is my first Minecraft Mod and the first project i made that interacts with the network, has logins/accounts and does APIs.I am really not good and thus the UI (far worse on mobile) and especially the Code is bad, but i would have never expected to get it working at all, much less this functional.
But i am still far from done, i still want to improve the overall code quality, add the inventory and ender chest, achievements (maybe even custom ones so vanilla clients can earn and view them without having to change anything locally. IDK yet) and more.If someone wants a small demo, i have it running on my server to test while I am developing at:https://grisu-ftp.de(If you find any issues lmk :)While this is by far not as cool as the other stuff on here i still would like to show it off and gather some first feedback.
This is my first Java project that goes above the Standard stuff in school like scanners/calculators and so I have probably done obvious beginner mistakes.

reply

kouiskas

56 minutes ago

 |
prev
 |
next

[–]

A terminal manager for Claude Code:
https://github.com/gi11es/deckard

The main goal is to reduce cognitive load managing many Claude Code and terminal sessions in parallel, while keeping things simple with a design focused on peripheral awareness of session status. And making everything resumable. The Claude session explorer also supports forking past sessions mid-conversation.Overall this is designed to support the Claude-first software development workflows I've developed over the past year.

reply

ajd555

31 minutes ago

 |
prev
 |
next

[–]

A news aggregator like HN but specifically for freight:
https://news.freight.nyc

The idea is mostly to build a community for the sector I work in, since there isn't any (aside from Reddit...)

reply

jikimi

9 hours ago

 |
prev
 |
next

[–]

I've been building Jikimi, a privacy-first parental control platform. It started because my kids were spending too much time on the computer, only stopping if we asked them to. If we forgot, they'd just keep playing. We were also worried about online predatory behaviour like grooming, bullying, that kind of thing.

So I built an on-device OCR engine (PaddleOCR) that reads screen text locally and feeds it into an AI sentiment analysis pipeline. No screenshots leave the machine. We now get alerts if there's detection of concerning interactions. The client is written in Rust, with DNS filtering, game detection (Steam/Wine/Proton), and screen time enforcement built in.It started as a home project that worked really well. My wife suggested other families wouldbenefit, so I've been building it out as a product. The client shipped on Linux first, we're a Linux gaming family, with Windows coming soon.https://jikimi.appThere are many more features I haven't touched on. Would love feedback from other parents who've dealt with this space. The goal is to protect children and empower parents with tooling that's transparent and effective.

reply

varenc

9 hours ago

 |
parent
 |
next

[–]

This sounds very cool! AI really seems like it should enable smart, real-time, and fully private on-device parental safety controls. Would be eager to try out a macOS or Windows client. Also a bit a of feedback: the "view on github" link on the homepage just links to /features, and seems like the real github repo is empty.

reply

jikimi

9 hours ago

 |
root
 |
parent
 |
next

[–]

Thank you! The Windows client is currently the primary focus. I'm working toward feature parity with the Linux client and hoping to have it available soon. macOS is on the roadmap after that.

Good catch on the GitHub link, that's a bug, I'll get it fixed. I'm planning to open source the client codebase and push it to GitHub in the near future.I'll post updates on the site as clients become available. Appreciate the interest!

reply

mkozak

36 minutes ago

 |
prev
 |
next

[–]

Codeboards connects to GitHub, Stack Overflow, LinkedIn, and HuggingFace to generate a professional developer profile that updates itself. Your commits, contributions, and reputation — finally in one place.
https://codeboards.io

reply

williamcotton

16 hours ago

 |
prev
 |
next

[–]

Space Trader!

Imagine mixing Magic: The Gathering, StarCraft and Civilization’s hex grid combat.There’s multiplayer but I haven’t put the server anywhere yet.Check out the introduction here:https://github.com/williamcotton/space-trader/blob/main/docs...Clone the repo:npm install
 npm run devThere’s maybe a couple of other games called Space Trader so if anyone has any suggestions for a new name, I’m all ears!

reply

frankfrank13

15 hours ago

 |
parent
 |
next

[–]

looks cool! i read `faction-identity.md`, i feel like if you come up with a little more lore, a name may come to you

reply

jtbetz22

16 hours ago

 |
prev
 |
next

[–]

I believe that AI-powered software development means we need to fundamentally rethink how we preserve code quality.

Model output volumes mean that code review only as a final check before merge is way too late, and far too burdensome. Using AI to review AI-generated code is a band-aid, but not a cure.That's why I built Caliper (http://getcaliper.dev). It's a system that institutes multiple layers of code quality checks throughout the dev cycle. The lightest-weight checks get executed after every agent turn, and then increasingly more complex checks get run pre-commit and pre-merge.Early users love it, and the data demonstrates the need - 40% of agent turns produce code that violates a project's own conventions (as defined in CLAUDE.md). Caliper catches those violations immediately and gets the model to make corrections before small issues become costly to unwind.Still very early, and all feedback is welcome!http://getcaliper.dev

reply

munimdev

5 hours ago

 |
parent
 |
next

[–]

I like this. Is it possible that it ingests an existing repo and figures out the rules? I often don't have a .md file

reply

cperciva

12 hours ago

 |
prev
 |
next

[–]

The same thing I do every night - try to make FreeBSD work better on EC2!

Ok in all seriousness, right now I'm tracking down an issue with the ENA network interface which results in sporadic packet loss. Triggering the issue is hard and seems to require a large number of TCP segments being pushed to the NIC very fast. So far I've found that my reproducer stops reproducing when I turn off write combining on the MMIO space used for low latency queueing, which is... just a little bit weird.

reply

colinator

8 hours ago

 |
parent
 |
next

[–]

Remember how all those years ago (oh wait, a few months ago), that big npm hack attack was found by someone thinking their ssh connection was half a second too slow? Hope this ain't like that!

But seriously, good luck!

reply

cperciva

7 hours ago

 |
root
 |
parent
 |
next

[–]

Heh, I'm sure it's nothing like that. It wouldn't rule out the possibility that I'm tickling a firmware bug in the ENA device though.

reply

tunesmith

14 hours ago

 |
prev
 |
next

[–]

I'm working on
https://concludia.org
, a site that helps groups of people collaborate on arguments and conclusions. I don't really have any revenue plans for it currently as I suspect it will be rather niche -- I certainly wouldn't mind if it tops out as a small community of users -- but I've found it super useful in various contexts at work and at home.

You can read more about it over at the site, but it allows you to construct and validate arguments in a graphical form, and it has truth/proof propagation so you can see whether a conclusion is currently considered valid or contested. You can create counterpoints where you think the argument breaks down, and strengthen arguments from there. Some upcoming plans are to allow users to validate arguments for themselves, like mark which parts they understand and agree with so they can collapse that part of the graph, and to add more mcp capability so that LLM can help you construct and validate new arguments.

reply

Ey7NFZ3P0nzAe

5 hours ago

 |
parent
 |
next

[–]

Reminded me of
https://github.com/getguesstimate/guesstimate-app

reply

nithinbekal

9 hours ago

 |
prev
 |
next

[–]

A Ruby-inspired typed programming language called Sapphire:
https://github.com/sapphire-project/sapphire

I was reading the fantastic Crafting Interpreters book, and been wondering what it would be like to design a language from scratch. I really enjoy using Sorbet with Ruby, so wanted to design a small language with Ruby's object model, and a gradual type system.Despite not knowing much programming language theory, I was able to make a surprising amount of progress over a couple of weekends using Claude Code, including building a simple version manager for the language -https://github.com/sapphire-project/facet

reply

martimchaves

1 hour ago

 |
prev
 |
next

[–]

Hey y'all, couple of projects to show off:

https://ragbandit.com- improve the retrieval stage of your RAG systems by tuning your document processing pipelinehttps://smolinvoiceagent - an agent that process invoices, you make corrections, the agent learns your wayshttps://vendor-simple-central.streamlit.app/- this is just a POC, but it's a system to process and extract insights from data from amazon's vendor centralThis post is really wholesome :)

reply

zby

2 hours ago

 |
prev
 |
next

[–]

I am working on an llm wiki (as defined by Karpathy
https://gist.github.com/karpathy/442a6bf555914893e9891c11519...
)

Looks like it is a crowded area now - my angle is to start with theory of what is important in a system like that, from first principles (like agent limited context, statelessness, use goals etc). Currently I use it to develop that theory - and you can read it at:https://zby.github.io/commonplace/. I also use it to keep an index of similar systems (that is systems with agent operated memory):https://zby.github.io/commonplace/agent-memory-systems/The github repo is at:https://github.com/zby/commonplace. Work in progress.

reply

junaid_97

16 hours ago

 |
prev
 |
next

[–]

I'm building free immigration software for DIY applicants [1]

It's a free USCIS form-filling web-app(no Adobe required). USCIS forms still use XFA PDFs, which don’t let you edit in most browsers. Even with Adobe, fields break, and getting the signature is hard.So I converted the PDF form into modern, browser-friendly web forms - and kept every field 1:1 with the original. You fill the form, submit it, and get the official USCIS PDF filled.I found out SimpleCitizen(YC S16) offers a DIY plan for $529 [2]So, a free (and local-only) version might be a good alternative[1]https://fillvisa.com/demo[2]https://www.simplecitizen.com/pricing/

reply

exabrial

12 hours ago

 |
prev
 |
next

[–]

https://github.com/exabrial/petrify

Petrify is a machine learning model compiler for the the JVM. It reads your model from an ONNX or other model format, walks the Trees or Linear models, and encodes the model in equivalent JVM bytecode as a stateless class you can invoke.This differs from every other ONNX Runtime that I know of, which are essentially interpreters. The ONNX Runtimes are also huge (90+mb!?!), JNI, and drag gargantuan dependencies!This just compiles your models to native bytecode. Much simpler and you end up with 0 dependencies! (you need one interface technically, but I digress).

reply

dvaun

12 hours ago

 |
parent
 |
next

[–]

This is interesting. I’ve been working with ONNX models and compiling custom WASM runtime builds based on the model operators, cutting down on edge deployments.

Do you have any benchmarks?

reply

exabrial

11 hours ago

 |
root
 |
parent
 |
next

[–]

not... yet! Speed actually was a byproduct hilariously. Compiled models are definitely lightning fast, likely the fastest they could ever be on the JVM, because the tree is directly encoded as bytecode; represented lots of Opcode.IFGT-like comparisons. The JVM's JIT Compiler will have a blast with these code paths.

Petrify will also be order of magnitude kinder to your Garbage Collector, which will increase performance in high-throughput situations. You're also not loading 10 gazillion classes, as your models are directly represented as a first-class Java Class.The real goal here was the getting rid of dependencies! While thankful for the incredible (and free) work of the authors of the onnxruntime for Java, the primary onnxruntime jar a boat anchor; weighing is 90mb+ just by itself, not counting any of its dependencies.Once you compile your models with Petrify, you have exactly one 6.9kb jar as a dependency essentially just carries the Fossil interface as an entry point to call your model. I licensed that jar ASL2.0 for maximum compatibility in a corporate environment.

reply

xamde

47 minutes ago

 |
prev
 |
next

[–]

I am working on a simplistic syntax for mixing any text with structured knowledge (links, triples, property graph)

Syntax..has name..ddot.itThe spec is ready athttps://ddot.it, now working on tool support.

reply

Folcon

2 hours ago

 |
prev
 |
next

[–]

I've been building small games on and off over the last decade, started taking it a bit more seriously over the last 3 months and I've started building a specific game that I'm slowly building out

It's a top down ARPG called Mechstain where the player creates and pilots voxel based mechsInstead of traditional gear, your mech has a physical voxel footprint that you the player have to fit weapons and components insideYour job is to manage space, power and mass, what you can fit and power directly becomes your stats and abilities, essentially a bin packing problemBasically take Diablo 2 and remix it with Kerbal Space Program, still fleshing out the various systems, but I'm really enjoying the process of slowly designing systems, iterating on it and fleshing it outIt's quite fun taking thoughts I've been noodling on for years and trying to figure out if they synergise with what I'm looking at and do they provide interesting player decisionsRecently onboarded a 3d artist and it's really making things look a lot betterIf anyone has experience lighting + vfx in this sort of game, I'd love to talk to them, still trying to figure that out =)

reply

bgdam

2 hours ago

 |
prev
 |
next

[–]

I have come to believe that in the near future, software development is going to become a common skill, like driving. I myself have been vibe coding so many tiny apps/scripts/cron jobs that resolve tiny inconveniences in my life and the biggest pain point for me right now is making these available to my multiple devices over the internet.

To resolve this, I am currently fleshing out the idea for a "shared hosting" for vibe coded programs - something like a cross between an old school LAMP stack shared host and a parse like library for capabilities like push notifications.It's all very half baked in my head at the moment - with the biggest problem being a safe way to deploy remote code without pawning the server, but this is a problem shared hosts have dealt with and I am sure I will eventually figure out a way.The end goal is to be able to have people tell their AI agent of choice to "make their app deployable" on our platform - and the agent will adapt it to our library methods and deploy automatically. Once done folks will be able to access their programs from any internet connected device.

reply

mittermayr

1 hour ago

 |
parent
 |
next

[–]

just wanted to give you another perspective to consider: I teach a class where they're designing websites and small apps with ChatGPT, but we're failing to host this. I built a simply copy/paste HTML renderer, so they can at least share and try it outside of ChatGPT, but for our final project, I felt like it would've been nice if something like all those JS playgrounds would exist, but much, much simpler. I upload an HTML and it becomes accessible publicly so students can share their projects. The domain never matters, any subdomain is fine, but it needs to be without an account and that makes it incredibly hard to host (spam). Why without an account? Our onboarding of the same class (30 students or so) to Figma took us two full days, it was a disaster. Nobody wants to go through that again. That said, university budgets are nearly untouchable, so I'm not sure if and/or where there's reason enough to do this other than purely academical.

reply

ashdnazg

14 hours ago

 |
prev
 |
next

[–]

I'm back to searching for numbers that are palindromes both in decimal and in binary. [0]

I had an insight the other day, that as I fix the n least (and most, it's a palindrome!) significant decimal digits, I also fix the remainder from division in 5^n. Let's call it R. Since I also fix by that point a bunch of least (and most) significant bits, I can subtract how much they contribute mod 5^n from R, to get the remainder from division in 5^n of the still unknown bit. The thing is, maybe it's not possible to get this specific remainder with the unknown bits, because they're too few.So, I can prepare in advance a table of size 5^n (for one or more ns) which tells me how many bits from the middle of the palindrome I need, to get a remainder of <index mod 5^n>.Then when I get to the aforementioned situation, all I need to do is to compare the number in the table to number of unknown bits. If the number in the table is bigger, I can prune the entire subtree.From a little bit of testing, this seems to work, and it seems to complement my current lookup tables and not prune the same branches. It won't make a huge difference, but every little bit helps.The important thing, though, is that I'm just happy there are still algorithmic improvements! For a long while I've been only doing engineering improvements such as more efficient tables and porting to CUDA, but since the problem is exponential, real breakthroughs have to come from a better algorithm, and I almost gave up on finding one.[0]https://ashdnazg.github.io/articles/22/Finding-Really-Big-Pa...

reply

jkasevits

53 minutes ago

 |
prev
 |
next

[–]

I am working on Tuumik - self hosted time tracking and in/out board. The project initially targeted law firms specifically (I was an attorney for a decade before coming back to software development). But Tuumik is suitable for any team working remotely.

Demo in browser (no registration required, just jump straight in):https://demo.tuumik.com/start-demohttps://www.tuumik.comhttps://github.com/tuumiksystems/tuumikIf any HN reader wants to give it a spin, hit me up at support at tuumik.com.

reply

ivanjermakov

4 hours ago

 |
prev
 |
next

[–]

True Trials - motorcycle trials simulator with two-axis leaning controls.

https://truetrials.substepgames.comI'm a long time fan of the Trials[1] game series, and it's sad that we might never see another trials game from RedLynx[2]. On the other hand, it's a great opportunity to make it myself.It's going to be free to play, web based, running on 10yo hardware, with open leaderboards and ability for users to create custom levels.[1]:https://en.wikipedia.org/wiki/Trials_(series)[2]:https://www.reddit.com/r/TrialsGames/comments/1i0qetb/has_th...

reply

Bewelge

3 hours ago

 |
parent
 |
next

[–]

Haha that's awesome! I'm in my thirties and these past few months I've been playing Trials rising with a high school friend. We used to play this 15+ years ago in school. Thought about developing my own as well (how hard can it be, it's basically 2D) but getting the physics to feel right was pretty difficult. Good luck! Is there some way I can receive updates on your progress?

Gameplay feedback: I'm a pretty decent player at the original games and I couldn't make it over a single obstacle, the controls seem extremely sensitive/abrupt currently.

reply

ivanjermakov

2 hours ago

 |
root
 |
parent
 |
next

[–]

Thank you!

What annoyed me about Trials is the artificial assist and magic forces that let you control bike midair and climb vertical walls - True Trials won't be like that, every force is derived from friction, spring compression, and weight transfer.Making physics feel right is a hard part indeed! Balancing leaning stiffness/damping of every angle and rider's joint is tricky. As you mentioned that controls are sensitive, it's necessary to clear high jumps (e.g. first checkpoint in course3 currently). It's surely takes time to get used to.I have a Discord channel where I will post updates:https://discord.gg/wtcZ5q5zHN.

reply

nowami

14 hours ago

 |
prev
 |
next

[–]

I'm working on Ruly, a daily number/logic puzzle where you set rules on a grid.

https://playruly.comMy goal is to make a simple yet interesting procedural and replayable puzzle. It has a couple of weekly variations: on Saturdays you need to break a rule to score max points, and on Mondays there's an added memory aspect which brings variety to the game.It's mostly vibe-coded which lets me focus on game design and testing. The next step is better onboarding/tutorial and more intuitive UI.

reply

rkomorn

14 hours ago

 |
parent
 |
next

[–]

This is a neat concept. I'm enjoying it. Thanks for putting it out there.

reply

nowami

14 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks for trying it out. I'm experimenting with some more variants, for example having more 'rules' than cells, so that you have to choose which ones you'll use.

reply

piinecone

2 hours ago

 |
prev
 |
next

[–]

Last month I released my first Steam game, an occasionally frustrating game about scoring great goals:
https://store.steampowered.com/app/3802120/Put_One_In_for_Jo...
.

I built HeartRoutine to help me lower my LDL and ApoB. I recently started beta testing it on some friends, too, to see if anyone other than myself would find it helpful:https://www.heartroutine.com/.I've started building the combat prototype for my next game, Today I Will Destroy You, inspired by my love of going-on-an-adventure-with-a-sword games and Sekiro-style combat.I've committed to keeping my personal website up to date:https://piinecone.com/.

reply

r0ze-at-hn

11 hours ago

 |
prev
 |
next

[–]

Developing a rigorous scientific definition of what make complex systems
persist
.

The opposite of the favorite questions: Why did that company I worked for fail? Why did Rome collapse? Why do people get old and die?Combining information theory with thermodynamics and control theory you get:
1) A set of six pillars that all systems that persist must have.
2) A fundamental 'Action' that all of these systems take.
3) A set of three rules for how system that persists must subdivideThis lets you do things like look at something that is failing and know that there are the 6 pillars and you can then identify them to determine what is failing. (For example there is a system that clears that brain of amyloid plaque and it can fail).I have applied this to countless systems including Religion, Language, AI Models, Business, the cell, quantum physics, number theory and much more. It is a Rosetta Stone for persistent systems. When there is an unsolved problem in one domain I can map it through this to any other domain that has already solved it.Note that this doesn't apply to all complex systems, only those that persist.And to keep this HackerNews related, been applying it to LLM's as they are just a stream of tokens that try to persist to incredible success I might add. Being able to pull from any domain do this brand new field is a giant cheat code.

reply

pkul

10 hours ago

 |
parent
 |
next

[–]

I'd love to see your method for this. How do you plan on publishing the information?

reply

IdontKnowRust

11 hours ago

 |
parent
 |
prev
 |
next

[–]

Can you share something or any resource based text? I'm really curious about it

reply

r0ze-at-hn

9 hours ago

 |
root
 |
parent
 |
next

[–]

Sure send me an email (in my profile)

reply

kitsune_cw

7 hours ago

 |
prev
 |
next

[–]

https://folio.photo
 -- it's a photography portfolio that doubles as client gallery delivery, with white labelling, password protection, and other features you don't get with the average file sharing platform.

I'm hosting my personal gallery with it:https://captures.moe

reply

btzll

4 hours ago

 |
prev
 |
next

[–]

I am working an
https://app.proxytopia.com

At a first glance it's a mobile proxy service, but the entire backend of it allows anyone to create their own mobile proxy and be able to access it anywhere through the internet, seamlessly. That's the 2nd phase of the website which is still long ways to go, but very happy with how stable the platform is and how fully it's automated.Tech stack is a bit unconventional for a public facing website, as it's Blazor Server.
As a C# dev in my day job, I've found Blazor to be quite capable and stable to quickly iterate through my ideas. And was pleasantly surprised to see how easily I can deploy the app into a Linux VPS through docker, which I didn't think was possible a few years ago.

reply

arach

48 minutes ago

 |
prev
 |
next

[–]

https://openscout.app
 - a local first communication tool, for agent to agent communication and user to agent communication too

reply

nsainsbury

14 hours ago

 |
prev
 |
next

[–]

I've been working on
https://www.photogenesis.app/

It's an iOS app that applies various generative art effects to your photos, letting you turn your photos into creative animated works of art. It's fully offline, no AI, no subscriptions, no ads, etc.I'm really proud of it and if you've been in the generative art space for a while you'll instantly recognise many of the techniques I use (circle packing, line walkers, mosaic grid patterns, marching squares, voronoi tessellation, glitch art, string art, perlin flow fields, etc.) pretty much directly inspired by various Coding Train videos.Direct download link on the App Store ishttps://apps.apple.com/us/app/photogenesis-photo-art/id67597...if you want to try it out.* Coming to Android soon too.

reply

weitendorf

14 hours ago

 |
parent
 |
next

[–]

Hey, I've been getting into visual processing lately and we just started working on an offline wrapper for Apple's vision/other ML libraries via CLI:
https://github.com/accretional/macos-vision
. You can see some SVG art I created in a screenshot I just posted for a different comment
https://i.imgur.com/OEMPJA8.png
 (on the right is a cubist plato svg lol)

Since your app is fully offline I'd love to chat about photogenesis/your general work in this area since there may be a good opportunity for collaboration. I've been working on some image stuff and want to build a local desktop/web application, here are some UI mockups of that I've been playing with (many AI generated though some of the features are functional, I realized that with CSS/SVG masks you can do a ton more than you'd expect):https://i.imgur.com/SFOX4wB.pnghttps://i.imgur.com/sPKRRTx.pngbut we don't have all the ui/vision expertise we'd need to take them to completion most likely.

reply

imankulov

1 hour ago

 |
prev
 |
next

[–]

Building Smello (
https://github.com/smelloscope/smello
), a Python library and a local server that capture your outgoing HTTP requests to help you debug API integrations.

The idea was inspired by Mailpit, which I've used for years to debug outgoing emails. A few implementation details were literally stolen from Sentry SDK with an "implement it how Sentry does it" prompt.https://smello.io

reply

intothemild

2 hours ago

 |
prev
 |
next

[–]

Koji, a AI Backend Orchestration/Managment/Proxy layer:
https://github.com/danielcherubini/koji

I've been running models on my homelab for a bit now, but none of the available options out there was what I wanted. I wanted something that I could command from the CLI, API, or Web, so have an agent go in and do work remotely via SSH or myself via a web interface.I wanted the ability to know if models have been updated, and if backends (llama.cpp, ik_llama.cpp) have been updated, see what those updates are and choose to update. Also wanted the ability to switch betwen versions of those, so if I felt like there was a regression, or performance issue, I could roll back.I've also published plugins for OpenCode and Pi so that model discovery is automatic too.I'm building this mostly for me, as usual.

reply

ruaraidh

2 hours ago

 |
prev
 |
next

[–]

Aeolus, a Python library to provide a unified interface for air quality data from sources around the world:
https://github.com/southlondonscientific/aeolus

Air quality data is now very widely available, but managing access to multiple networks is a massive task (lots of shonky APIs out there - the EEA has a csv endpoint that actually returns a .zip with mimetype "text/html", just to give you a flavour). Integrating new APIs could be a full-time job, but it's something AI can do very well given a pattern.This is really for me as I build out my company working on turning air quality data into actionable information, but it's open source and freely available.

reply

tomasz-tomczyk

11 hours ago

 |
prev
 |
next

[–]

https://crit.md
 - a CLI tool for reviewing AI coding agent output like a GitHub PR.

I got frustrated with Claude Code and Cursor producing plausible-but-wrong changes with no easy way to annotate and push back, without making a full PR. crit makes the review stage fun again!Works on both plans as well as code itself. It’s been very rewarding hearing from folks who use it, everyone has been very kind! My most successful side project already :)GitHub:https://github.com/tomasz-tomczyk/crit

reply

bgitarts

10 hours ago

 |
parent
 |
next

[–]

This is cool. Feels like Codex already offers this in their desktop app.

reply

realrocker

10 hours ago

 |
parent
 |
prev
 |
next

[–]

excellent work. I have been using a vscode extension for this for an year.

reply

tomasz-tomczyk

4 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks! What extension were you using?

reply

mighty3xodus

5 hours ago

 |
prev
 |
next

[–]

Building 1 small and 1 ambitious:

1. Ambitious: ClutchTop - an opensource ai harness (desktop app) similar to claude code desktop app built in electron. It's to the point where I've started to use the app to build the app. Still in v1 though.https://github.com/veejayts/clutchtopBuilding this because I want both chat and agentic interface to use different models via openrouter/local.2. Miscellaneous PDF/img/doc tools (compression/merging/rotation, more to come) on the browser as a static web page.Try it here:https://veejayts.github.io/pdftools.htmlBuilt this because I don't want third party tools to have access to my document data, especially for compressing identity docs for government websites.

reply

RobinL

3 hours ago

 |
prev
 |
next

[–]

letterpaths (
https://github.com/RobinL/letterpaths
), a FOSS typescript library that can power cursive handwriting/educational apps for kids.

The idea is that it provides all the geometry to enables games like these to be built: (These are just rough demos)https://www.robinlinacre.com/letterpaths/writing_app/snake/https://www.robinlinacre.com/letter_constellations/And here is like the admin/demo:https://www.robinlinacre.com/letterpaths/And, separately, I made an educational country quiz, again FOSS:https://rupertlinacre.com/country_quizhttps://github.com/RupertLinacre/country_quiz

reply

martimchaves

1 hour ago

 |
parent
 |
next

[–]

This is really cool, any challenges in developing this? How did you decide on the directions that you take when writing a word?

Couldn't get the letter constellations working on my end.Country quizzes is a weak spot of mine, loved that. Would be cool to move the globe! Also, kudos for the bus cataloging!

reply

RobinL

2 minutes ago

 |
root
 |
parent
 |
next

[–]

The letters are based on how they're formed in the UK primary school curriculum.

Each letter is a json that defines the bezier curves according to a schema.They were created by starting by drawing the letters freehand, yielding essentially a dot to dot, and then (2) using an approximation/smoothing algorithm to convert that into beziers. Finally,I went through touching up/fixing each letter by hand, using a purpose built editor.That stills leaves the problem of joining letters together. For that I heavily lent on AI to propose an algorithm, although it required a lot of back and forth to get something even semi decent. At the moment it's probably 'good enough' but there's still lots of room for improvement.On the countries quiz, you should be able to move and zoom on the bloge using click and drag (or pinch and drag on mobile). Letter constellations uses shaders. Both of those are only tested on Chrome, so that might be the issue.Example letter:https://github.com/RobinL/letterpaths/blob/main/packages/let...JSONSchemahttps://github.com/RobinL/letterpaths/blob/main/packages/let...Editorhttps://www.robinlinacre.com/letterpaths/editor

reply

mchaver

2 hours ago

 |
parent
 |
prev
 |
next

[–]

Nice work on letterpaths. I really enjoyed moving the snake around and the sand sounds. It had me hypnotized for a few minutes.

reply

RobinL

2 hours ago

 |
root
 |
parent
 |
next

[–]

Thank you! Noticed you're interested in similar areas. I've also previously done some work on maths problem generation. Similar to letterpaths, the core lib can then be used to power games/other educational apps. As I'm sure you've found as well, It's surprisingly difficult to generate random maths problems aligned to a curriculum!
Core lib is UK-focussed:

https://github.com/RobinL/maths-game-problem-generator

And examples of games is can power:https://rupertlinacre.com/maths_vs_monsters/https://rupertlinacre.com/breakout_maths/https://rupertlinacre.com/maths_blaster/

reply

alexgrozav

2 hours ago

 |
prev
 |
next

[–]

I'm building Styleframe (
https://styleframe.dev
), a zero-runtime CSS-in-TS Framework written for theming and maintaining Design Systems.

After 4 years of maintaining an Open Source Design System, I needed a better way for theming than Sass and PostCSS. I needed the power of a full-featured programming language. That's how the first version of Styleframe was born.My vision is for Design Systems to be endlessly configurable and composable, like you would configure any library, with or without AI. Want to change your entire website to look like Linear? Simply install and use the Linear Design System configuration. Want only your buttons and cards to look like Linear, and the rest be the default theme? Use the button and card composable functions from that package.Styleframe is built as a transpiler-first system. You write your design tokens, selectors, utilities, and recipes in TypeScript, and Styleframe tokenizes everything into an internal representation. From there, the transpiler generates dual outputs:- CSS output: variables, selectors, utilities, themes, keyframes- TypeScript output: typed recipe functions with full IDE autocomplete (with an optional Runtime)This architecture means you can have complete control over customizing how your system is output. You could even use the generated tokens to render documentation for your design system components. The output code can be integrated with any headless UI Components Library, or with your own custom components.Fun fact: I've reimplemented the entirety of TailwindCSS using Styleframe's utility and modifier tokens. Not only that, but I've also built a scanner which picks up your CSS Classes from your markup. It's basically Tailwind, but 100% configurable (even utility class format can be changed), and is always based on your design tokens.

reply

franze

1 hour ago

 |
prev
 |
next

[–]

hi, i am currently working on an idea i had for years but now decided to make it reality

https://apfelpad.franzai.com/a texteditor with spreadsheet like formulas - does this even make sense?
super super early buggy release - feedback welcome - any feedback, thxgithub:https://github.com/Arthur-Ficial/apfelpad

reply

syl5x

4 hours ago

 |
prev
 |
next

[–]

I am building a platform for helping stray dogs/cats pro actively. The idea is whenever you see an animal in need in an unfamiliar area, you can use it to help the animal get into the right hands. Meaning that you share your GPS and it automatically sends you the nearest clinics, relevant government institution, phone numbers of people that are monitoring for such things and local facebook groups that you can post on. I am also exploring a ways to post automatically in a facebook group whenever a signal is received. There are a lot of challenges however with the platform as it needs to be mobile-first and easy to use for the people to actually start using it.

reply

beilabs

4 hours ago

 |
parent
 |
next

[–]

I desperately need this in Nepal. There are so many street dogs and some really need urgent care.

reply

wilbur_whateley

1 hour ago

 |
prev
 |
next

[–]

Working on
https://www.nichess.org/

Nichess is a game like chess, where pieces have special abilities and health points. This allows for much finer balancing and many more variants compared to the original chess. It will take some time, but it will become great eventually.

reply

Apanatshka

3 hours ago

 |
prev
 |
next

[–]

I'm implementing different parsing algorithms (for programming language text to syntax tree purposes). There are so many papers published on different algorithms... I'm just slowly reading it all, and implementing the algorithms and improvement ideas, sometimes combining ones from different papers. At the moment I'm constraining myself to LR-based algorithms to not drown even more in the sea of publications.

I have a recursive ascent code generator with a bunch of optimisations that I wrote about [1,2]; it's a linear-time parser for LR(1) with reduced overhead. I have an RNGLR implementation (a polynomial-time parser for any context-free grammar), that's still a table-based interpreter like more LR-based parsers out there. I've extended that implementation with special code to handle cycles more efficiently. Some day, I'll take some time to write a paper on that and publish it. Currently, I'm trying to combine the two ideas and create a generalised recursive ascent code generator. If I succeed I'll write another blog post again, it's been a year since the last one...[1]:https://blog.jeffsmits.net/optimising-recursive-ascent/[2]:https://blog.jeffsmits.net/optimising-recursive-ascent-part-...

reply

WalterGR

16 hours ago

 |
prev
 |
next

[–]

Also see:

3 days ago, 220 comments:https://news.ycombinator.com/item?id=477004605 days ago, 51 comments:https://news.ycombinator.com/item?id=476790218 days ago, 21 comments:https://news.ycombinator.com/item?id=4763903911 days ago, 22 comments:https://news.ycombinator.com/item?id=47600204

reply

osigurdson

14 hours ago

 |
parent
 |
next

[–]

Agree, "What are you working on" is getting diluted. However, I've concluded that this one (posted by david927) is the de-facto "real one".

reply

jakeydus

13 hours ago

 |
root
 |
parent
 |
next

[–]

The first link shared was to a post requesting projects that aren't AI. I'm more interested in that one, so I appreciated the distinction, personally.

reply

xjconlyme

1 hour ago

 |
prev
 |
next

[–]

https://kulikuli.app/translate
 I'm building a web version of my app, which has better quality than Google/DeepL and also translates the result in reversed for users to double check.

reply

ehnto

5 hours ago

 |
prev
 |
next

[–]

I finished my immobiliser for old cars from the last thread. It fills a niche in the market for a no-wireless, no fob solution that will work on older vehicles without much CAN bus integration.

I have been brushing up some drawing skills for concept art, and exploring more embedded automotive product ideas for this niche of cars.

reply

asimovDev

2 hours ago

 |
prev
 |
next

[–]

Bought an e-scooter from Wilfa (under the E-way subbrand). Been reversing it slowly. End goal is to have an Apple Watch only app with stats and maybe some fun gimmicks like using wrist rotation and gestures for switching gears and such.

So far I first sniffed the BT logs from my iPhone but couldn't figure out how authorization works. Recently decided to decompile the android version and with some LLM help I made some progress. Been too busy to test it out but once I crack the authorization I can get started with writing my own Watch app

reply

fiskeben

2 hours ago

 |
prev
 |
next

[–]

Currently I'm finalizing my static web hosting project for designers and other people who couldn't be bothered to learn a cli,
https://webtastic.site
 and trying to make simple games for iOS. My first game is Merge Mixology,
https://apps.apple.com/no/app/merge-mixology/id6760284508?l=...

reply

jsomau

14 hours ago

 |
prev
 |
next

[–]

I built a cooking timer that solves the mental arithmetic of roasting multiple things at once. Pick chicken legs, sweet potato, green beans, etc and it'll give you a simple plan telling you when to put things in, flip them and take them out. Trying to eat more veggies and home cooking so this has helped me a lot!

https://www.roastrack.app/

reply

jftuga

13 hours ago

 |
parent
 |
next

[–]

Wow, this is super useful. Thanks for making this!

reply

rudcodex

1 hour ago

 |
prev
 |
next

[–]

2d mini-universe simulation where space stations trade and eventually expand. Goal is to be enjoyable to watch in background. Been my dream to make games, and with LLMs, I finally can! (ship arc trail math is hard!)

WIP, started 2 weeks ago:https://skyshift.rudidev.com/maps/stable

reply

rukshn

1 hour ago

 |
prev
 |
next

[–]

We are working on Entangle -
https://entangle.cloud

developing AI agents that are easy to integrate in to websites, based in Europe and all data stored and processed in Europe to complying with regulations.Looking forward to collaborations, and happy to talk with anyone would like to collaborate with us

reply

skor

12 hours ago

 |
prev
 |
next

[–]

A programming language to hack music with

https://github.com/audion-lang/audionThe idea came after I finished a permanent piece for a museum using MaxMsp and python. I always had this thought in the back of my mind that "I could express this so much easier in a few lines of code.."Check the docs folder for the full language spec.I really liked how objects came out, I don't think it needs any more since I can do object composition.There are some nice functions to generate rhythms and melodies with combinatorics, see src/sequences.rs and melodies.rsIts a WIP but you can use it now to create music with whatever you want: hardware/daws/supercollider
, download the nightly release.supercollider is tightly integrated but not required. I havent had time to develop userland libraries yet but I'm working on it

reply

luxgile

1 hour ago

 |
prev
 |
next

[–]

Working on (another) build system for C and potentially C++ called 'cbs.h', the idea is to use C to build the project similar to how Zig uses build.zig.

Here's how cbs.h builds itself:https://codeberg.org/Luxgile/cbs.h/src/branch/main/cbs.c

reply

ryanchants

16 hours ago

 |
prev
 |
next

[–]

An app for supplementing learning in my masters program [1].
I'm currently in enrolled in the MCS Online from UIUC. My first course, Natural Language Processing, has been interesting, but it's a coursera-based course. This means the lectures are pre-recorded and mostly just the professor reading the slides. It's hard for me to stay engaged and really learn the material. So I started with a series of claude prompts that took the lecture slides and created a pre-watch summary, and then helped me drill the concepts after each lecture. I think converted those into a platform where I can upload notes/lecture slides and have it generate quizzes. It starts with recognition(multiple choice) questions, and eventually moves to recall(short answer) once you prove mastery of a topic. It also generates flashcards from failed answers. It extracts topics from the uploaded materials, and tracks mastery over time. Mastery rots if you don't touch the platform/topic for a while.

I'm not sure if I'll every productize it in any way, but I could see a world where it's used by people prepping for the bar, med boards, various continuing education stuff. Right now it's just a fun platform to build on as I explore the current wave of technologies. Building a framework for evaluating different LLMs for best price/accuracy. Adding a RAG pipeline so wrong answers can point back to source material for further review, etc.I'm looking at moving from backend engineering to a more MLE or agent pipeline role, so this is giving me something more than school projects to build on. While also helping me do better at school.[1]https://studyengine.app/

reply

virissimo

15 hours ago

 |
prev
 |
next

[–]

I'm beginning to homeschool my kids in computing, and we are pairing up chapters of The Elements of Computing System (the Nand2Tetris book) with games that teach similar skills/kinds of thinking (Human Resource Machine, Comet 64, etc...), but we didn't find anything to supplement the first two chapters (where you build basic chips up to an ALU in HDL). I ended up starting creating a kind of browser based kata for those chapters here:

https://virissimo.info/build-your-own-alu/LMK what you think.

reply

hko-sh

3 hours ago

 |
prev
 |
next

[–]

I am building Chief of Staff (getcos.ai), an AI assistant for startup CEOs specifically (and executives with 100+ emails a day in general), because neither Superhuman nor Lindy were working for me.

What I've noticed personally and with founders I talked to is that communication and email triage takes a large amount of time each day, but mostly only needs a quick decision or rerouting the right kind of information. But all this mental overhead takes away time from the really important strategic tasks that you should be working on as a founder.That's where Chief of Staff comes in. Like a real chief of staff, it gives you a head start into the day: checks your calendar, your incoming emails and messages, prepares meeting briefs and drafts responses.But it goes further than your typical smart inbox: by sharing your strategic goals it prioritizes and makes sure you are working on the highest leverage items. It also helps you manage relationships by tracking communication frequency and sentiment, so you don't miss when a key customer goes cold.Both Superhuman and Lindy fell short in key areas of the UX for me: Superhuman makes email triaging faster, but you're still the one doing most of the work. Lindy is highly customizable, but you'll spend a ton of time building and tweaking workflows. I wanted a batteries-included approach to get started right away by just connecting Gmail, Slack, and Calendar without any additional configuration.A key UX decision for me was also that I stay fully in control. Chief of Staff reviews, analyzes and prepares, but I am the one hitting send.I'm testing it with a very small crowd right now, but want to open it up soon. If you feel that this is an issue you want solved for yourself as well, feel free to reach out to me and I'll get you on the list for the private beta.If you have strong opinions for or against this approach, I wouldn't mind hearing this either :-)

reply

whatsakandr

1 hour ago

 |
prev
 |
next

[–]

My wife has wanted a security system for a while. The turnkey cloud solutions freak me out. I've done some home automation with home aisstant before, and omg that was configuration slog. But with Claude..... It becomes fun.

reply

blef

3 hours ago

 |
prev
 |
next

[–]

I am building nao, an open-source analytics agent. With nao you can connect all your sources of context (from warehouse to your knowledge base) using a CLI, and then you have an agent that sits on top of it.

You can use the agent from any client (web, Slack, Teams but also other harnesses).We think most of data analytics work will be transformed (and is already being transformed) from SQL monkeys to chat to analyses, but all the UI/UX are not designed for this and this is what nao is, being open-source because knowing how the context is managed is key.With nao you can have a conversation and then shared the output on the form of a story, that can be either static or live replacing what old dashboards were.We are close to 1k stars on Github:https://github.com/getnao/nao

reply

raphinou

5 hours ago

 |
prev
 |
next

[–]

Working on Asfaload, a multisig sign-off solution applied to release artifacts authentication.

It is:- open source- accountless(keys are identity)- using a public git backend making it easily auditable- easy to self host, meaning you can easily deploy it internally- multisig, meaning event if GitHub account is breached, malevolent artifacts can be detected- validating a download transparantly to the user, which only requires the download url, contrary to sigstoreNearing Alpha release stage.Code athttps://github.com/asfaload/asfaloadInfo athttps://asfaload.com/

reply

entrep

13 hours ago

 |
prev
 |
next

[–]

Coding agent that seems to beat Claude Code on SWE-bench at half the cost.

8/15 on SWE-bench Verified vs Claude Code's 5/15, ~$0.06/instance vs ~$0.12. Small sample, single repo, lots of caveats. But the direction feels right.
Event-sourced reducer, no framework deps beyond the Anthropic SDK.

reply

aleda145

17 hours ago

 |
prev
 |
next

[–]

https://kavla.dev/

I've worked with data my entire career. We need to alt tab so much. What if we put it all on a canvas? Thats what I'm building with Kavla!Right now working on a CLI that connects a user's local machine to a canvas via websockets. It's open source here:https://github.com/aleda145/kavla-cliNext steps I want to do more stuff with agents. I have a feeling that the canvas is an awesome interace to see agents working.Built with tldraw, duckdb and cloudflare

reply

peter_retief

2 hours ago

 |
prev
 |
next

[–]

I have always wanted to buy my food directly from farms but the logistics is daunting.

So I am creating an ambitious app that uses agentsAdmin: -> handles all financial transactions and manages the appSubscriber:-> entity who orders/shopsMarket: -> the agents that work with the farmers or marketsCatering: -> for any processing or recipesDelivery: -> handles cold chain, delivery, storageInitially I will do everything but the idea is to delegate the agentsThe basic structure is in placehttps://github.com/peterretief/orderin

reply

moralestapia

9 minutes ago

 |
prev
 |
next

[–]

HTTPState

(https://httpstate.com(https://github.com/httpstate/httpstate)A data layer to connect all kinds of applications. You pick a "UUID" and start storing and retrieving data from it. I've written clients for 8 languages now, one main driver is it should be as easy as possible to use.Another premise is that data is open, enabling re-usability and collective applications. You can see some featured data streams on the site, you can use them on your app in like 1 minute.

reply

piker

2 hours ago

 |
prev
 |
next

[–]

Tritium, the legal IDE:
https://tritium.legal

This month we're focused on:- first-party, native DMS integration;- provider-agnostic agentic workflows; and- enterprise-grade redliningBut of more interest to this group is probably our blog! Our latest post is about Gary Kildall's blunder quibbling over an NDA redline with IBM who was looking to give its entire enterprise away:https://tritium.legal/blog/redlining.

reply

rpjt

17 hours ago

 |
prev
 |
next

[–]

I've got a mobile app.

It allows you to get a wake up call from someone friendly, somewhere out there in the world.It's got a handful of regular users and it's mostly me making the calls, but it's great fun to wake people up!No phone number required - these are VoIP calls via the app.Built it because I think it's cool.

reply

victorbjorklund

16 hours ago

 |
parent
 |
next

[–]

That is such a wholesome and fun idea (but probably gonna be abused if more users). Link?

reply

zorked

2 hours ago

 |
prev
 |
next

[–]

I "wrote" (vibe-coded) a non-chronological RSS reader. I crawled the blogrolls of some blogs I liked, fetched all the posts (with full text) and ran a clustering algorithm on them. LLMs classify the content to filter out meta/political/personal posts. And a LLM gives names to the clusters by sampling the contents.

It's an amazing source of long things to read. There is so much stuff worth reading that has been posted in several decades of blogging.

reply

Jeaye

14 hours ago

 |
prev
 |
next

[–]

I'm working on the jank programming language!

https://github.com/jank-lang/jankIt's a native Clojure dialect which is also a C++ dialect, including a JIT compiler and nREPL server. I'm currently building out a custom IR so I can do optimization passes at the level of Clojure semantics, since LLVM will not be able to do them at the LLVM IR level.

reply

habitmelon

7 hours ago

 |
parent
 |
next

[–]

You are hero! I just learned about this yesterday when I shared my Clojure editor:
https://github.com/tlehman/hammock

I would love to know more about Jank, from what I read, it transpiles to C++ right?

reply

anotherpaulg

16 hours ago

 |
prev
 |
next

[–]

I’ve been building quantum photonics experiments. Repeating the Bell inequality tests that won the 2022 Nobel, quantum erasers, etc.

I just published a fun interactive 3D demo of SPDC, one of the most common and accessible ways to create entangled pairs of photons. I'm hoping to publish a series of articles on other cool learnings about doing quantum photonics in the lab.https://paulg.info/2026/04/10/spdc/

reply

contraposit

15 hours ago

 |
parent
 |
next

[–]

You should collaborate with Huygens Optics. I find his videos thought provoking

https://youtu.be/hYyrgDEJLOA

reply

ashtavakra

3 hours ago

 |
prev
 |
next

[–]

I am building localgcp - This is localstack / floci equivalent for Google Cloud platform :
https://github.com/slokam-ai/localgcp
 - currently supports 14 services, including Vertex AI and BigQuery.

Part of building this, I decided to build a BigQuery emulator from scratch and learned a lot about GoogleSQL (previously ZetaSQL) along the way:https://github.com/slokam-ai/localbqI plan to maintain and improve this going forward. The goal is to see how much can emulators actually do.Website:https://localgcp.com/

reply

jcubic

1 hour ago

 |
prev
 |
next

[–]

I'm working on my Open Source speaking clock (mostly for myself):

https://github.com/jcubic/speaking-clockIt uses local AI models for the voice.

reply

raptor111

1 hour ago

 |
prev
 |
next

[–]

https://deadtrees.earth
 fully open crow sourced drone repository for vegetation monitoring

reply

mind1m

1 hour ago

 |
prev
 |
next

[–]

Building mobile app to cure my socials scrolling addiction - instead of videos you scroll live flights.

https://planefeed.app/

reply

Shorel

2 hours ago

 |
prev
 |
next

[–]

Apikulture. A small, fast alternative to Postman/Insomnia that doesn't upload your data to the cloud.

Written in C++ and Slint, it was also a testbed of slint as an UI framework. Having used wxWidgets in the past, and Qt recently, it is certainly a different thing. I just wish there was a native C++ alternative to slint.I need to integrate the CI to produce binaries, but you can compile it yourself for now.

reply

boyter

15 hours ago

 |
prev
 |
next

[–]

I reimagined
https://searchcode.com/
 since I realised LLMs have issues when it comes to understanding code you want to integrate. It’s useful for looking though any codebase, or multiple without having to clone it.

I use it when I have candidate libraries to solve a problem, or I just want to find out how things work. Most recently I pointed it at fzf and was able to pull the insensitive SIMD matching it uses and speed my own projects up.I can’t find it right now, but there was a post about how ripgrep worked from a someone who walked through the code finding interesting patterns and doing a write up on it. With this I get it over any codebase I find interesting, or can even compare them.

reply

or29544

5 hours ago

 |
prev
 |
next

[–]

I'm working on a fully offline, apple only (for now), subscription-free home photo library browser. For example you have your photo library on your Mac Mini in the bedroom, and a separate photo library on your work MacBook, but right now you are in the kitchen and your wife wants to see the photos from your last trip in Prague. You don't want iCloud, you want privacy, you don't want telemetry, nor subscriptions to access your own photos. You also want no lock-in so you want full export of all photo organization in the photo metadata.

Well, this is the app that answers that. Everything is seamless, you don't configure anything. You simply start the app on the Mac Mini, import the photo folder, and let it run in the background. In the kitchen, you simply take your iPhone or iPad, open the app and voila, all photos from all libraries show up, organized by date, place, album, people, event. You want to see photos from Prague? You simply check Prague from the filter sidebar. You want those from 2008? You check 2008. Done.This is not an AI search-based photo library. You cannot even search. Everything you can search for is laid out in the sidebar. You don't need to remember where you have been in 2008. You check 2008 - you see all locations, all albums, everything from that year. You want to see how many trips you had to Vienna? You check Vienna. It's kind of old school this way, but I find it much mentally sane to see a list of filters with things you have done and places you have been and dates you took photos in, rather than an empty search input open to guesses and missed attempts.This is also not a replacement for your Apple Photos app, or a photo editor app. This is not a photo editor. It's simply a better way to browse historical photos, in a home network, without thinking about it.

reply

amarant

16 hours ago

 |
prev
 |
next

[–]

Games. Well, mostly tooling surrounding them it seems. In the last 2 months I've made a pixel art editor for Android, a headless population simulator(still balancing parameters on this one, not enough NPC's turn to crime at present, and I've also run into some weird issues with market prices, in one instance the price of meat rose enough to cause a integer overflow. I could switch to i64, but honestly meat was supposed to cost around 20 moneys, not 2³²

I'm also working on a 2d procedural animation plugin for bevy, a autotiling plugin for bevy (using 16 tile-dual grid, which the default bevy autotiling plug-in didn't support) and ofc my android pixel editor now has a rig editor mode and a tile editor mode that integrates with the plugins.Making video games is hard! I keep getting side tracked!

reply

rnts08

6 hours ago

 |
prev
 |
next

[–]

Since blacksmith labs and phoenix ai - the ai assisted automotive r&d, security and compliance engineering tool has been on the backburner for a while, I've been helping a couple of blockchain projects and built some tools, besides tinkering with my real-time EVM contract and transaction heuristics and classification engine.

- ETH Watchtower: a real-time EVM monitoring tool with heuristics and classification of contracts and transactions:https://ethwatchtower.xyz- P2P SSL VPN provider/consumer tools using a blockchain as announcement and settlement layer:https://github.com/rnts08/blockchain-vpn- OrdexNetwork:https://ordexnetwork.org, I've builthttps://ordexswap.onlineandhttps://ordexswap.online/wallet/as well as an Umbrel variant of a self-hosted wallet.- Waya Wolf Coin v3: Helped the team to compile binaries for linux, and modernizing the libraries:https://github.com/rnts08/WWC3-Linux-binaries/https://github.com/Waya-Wolf/WWC3- Low Cap Exchange algorithmic trading bots with machine learning and automatic ghost trading, because I wanted to see what the most common shapes are on smaller exchanges:https://github.com/rnts08/low-cap-exchange-trading-botHowever, I am really looking for Sr. DevOps/Platform Eng/SRE/System/Network Admin/Infra Engineering or similar, full-time or contract work, seehttps://timhbergstrom.profor contact details.

reply

js98

4 hours ago

 |
prev
 |
next

[–]

Hey all, I’ve built Nekode (
https://github.com/Jakob-98/nekode
), which is desktop-cats for monitoring your AI coding agent sessions (OpenCode/Claude Code/ Copilot CLI/VSCode Copilot). It works as a macOS menubar app, and the cats run around on your desktop.

Each cat mirrors the agent's state, such as sleeping when idle, walking when working, sitting when waiting for input, running toward your cursor when it needs permission.Fully native Swift, no Electron, under 5 MB, zero network requests, all session data stays local as plain JSON.I published it source-available with an honor-system license, but this week I’m going to fully open source it and remove the licence. The payment/nag system was an interesting experiment but the project is more useful to me as a proper OSS tool at this point.https://nekode.dev

reply

merelysounds

5 hours ago

 |
prev
 |
next

[–]

UI for image logic puzzles (nonograms), I’m working on making them prettier and more user friendly.

Some prototypes are already live in my app. Screenshots in the App Store:https://apps.apple.com/app/nonoverse-nonogram-puzzles/id6748...(the patterns in the puzzles in the dark mode screenshots, i.e. 4th and 7th).

reply

Cyphase

4 hours ago

 |
prev
 |
next

[–]

I've been on sabbatical (not on leave from anywhere, just decided to take a break from work) for months now, taking some time for myself. Minimal tech stuff until more recently, but now I'm back in the deep end.

The main thing I'm currently working on is a platform for organizing and discovering in-person events. Still not certain about the boundaries for "Phase 1", but I have a bunch of ideas in that space that I've been incubating for a while. One subset of features will be roughly similar to that app you've probably heard of that starts with 'M' and ends with 'p', but hopefully an improvement, at least for the right audience. But wait, there's more. :)Currently building it; it's not public yet, so no link. Next month. I also have an external deadline around that time.Thinking about how to grow the userbase is intimidating, but I think it might end up being fun.

reply

winrid

5 hours ago

 |
prev
 |
next

[–]

I'm working on Watch.ly - a remote human-in-the-loop networking and FS sandbox for AI agents like openclaw:
https://watch.ly/

Also this week launchinghttps://dirtforever.net/which is an open alternative to RaceNet Clubs for Dirt Rally 2, since EA is shutting that down.I'm also expanding the SDK and plugin space forhttps://fastcomments.comand am planning on adding AI agents because everyone expects that now :) a big challenge is building it in a way that doesn't make half the users mad. So I'm planning on marking any comments left by AI mods with a "bot" tag, and having the system email users on why it made certain decisions, with an option to contest that loops in a real person. I'm hoping this provides value to site owners while not angering real people. The agents could also just do non-invasive things like notify certain moderators when comments violate community standards in some way, or give out awards. I'm also hoping at some point I can run my own hardware for the LLMs so I don't have to share people's data with third parties.

reply

gen2brain

4 hours ago

 |
prev
 |
next

[–]

I have been working for several months (maybe half a year) on the IUP fork, a cross-platform UI library with native controls
https://github.com/gen2brain/iup-go
 . I added more drivers/backends, Cocoa, WinUI, Qt, GTK4, FLTK, and EFL. New controls, like Table, Popover, Toggle SWITCH, and modern Tray support. WebBrowser control uses modern browsers; there is a JAVASCRIPT attribute for proper hybrid native/web apps. GLCanvas now uses EGL for both X11 and Wayland, and of course, there is proper Wayland support for all Linux toolkits. I still have a long list of TODO with issues I want to fix, all the docs that need updating, etc. The plan is to post a "Show HN" after I finish with all current tasks.

reply

rrr_oh_man

4 hours ago

 |
prev
 |
next

[–]

Building Alyph — a canvas-based AI workspace.

My problem: my super-long, months-old ChatGPT threads were breaking down. Even typing got slow, and the longer the threads got, the more they hallucinated. I loved Google AI Studio and paid for it, but I was constantly deleting and re-editing the same thread just to try a different angle. And I couldn't run multiple frontier models against the same context or files without copy & paste and tab switching.I do 99% of my AI work now in Alyph. One board instead of a dozen tabs, branch anywhere, hot-swap models on the same context. Best guess: I'm 3x faster building things. The honest 1% failure case: it's too slow to load for a quick throwaway question.Hardest technical problem so far: layout algorithms for an infinite canvas.Pre-revenue, early users. Building self-service billing now.Looking for a co-founder who's sold B2B software before.https://alyph.ai

reply

binsquare

12 hours ago

 |
prev
 |
next

[–]

I am building a virtual machine that starts as fast as containers and can be made portable and easy to use like containers.

free, open source ->https://github.com/smol-machines/smolvmI worked with firecracker a lot back in the day and realized it was a pain to use. And containers had a lot of gotchas too.Since sandboxing is all the rage now - I think it'd be a better infra primitive than firecracker that works locally/remote and etc.

reply

jsunderland323

12 hours ago

 |
parent
 |
next

[–]

This is very cool. Would love to chat with you.

I’m working onhttps://coasts.dev.I’ve been thinking a lot about the light vm side lately but it’s not an area we are going to attack ourselves. I think there’s a really good pairing between what we’re working on.

reply

david_shi

12 hours ago

 |
parent
 |
prev
 |
next

[–]

are agents the primary usecase? curious who you think would find this the most helpful

reply

binsquare

11 hours ago

 |
root
 |
parent
 |
next

[–]

Agents, ai code executions are a very good use case.

I think anyone looking to use infra that needs below properties are well served by this project:
1. subsecond vm cold starts
2. kernel isolation (vs containers)
3. consistent local <-> remote environment
4. elastic cpu, memory.
5. ease to setup.I am designing it as a infra primitive on purpose for general workloads as opposed to others in the microvm space i.e. firecracker was designed for lambda/serverless workloads.

reply

joefreeman

5 hours ago

 |
prev
 |
next

[–]

The workflow orchestration tools I've used over the past have been consistently unsatisfying, so I've been building my own. With Coflux (
https://coflux.com
), workflows are defined declaratively in plain Python with decorated functions (tasks). Workers connect to the orchestration server and get assigned work - calls to other tasks get intercepted and then re-scheduled by the server onto (potentially different) workers. Tasks are executed in pre-warmed, isolated processes, with low latency.

Beyond standard features (retries, caching, timeouts - enabled with attributes on the decorator), Coflux supports more novel features - like suspense (where a task can choose to go to sleep and get restarted when a result it depends on becomes available), memoisation (where steps within a run are aggressively cached so that you can re-run steps in a workflow without re-running upstream steps), and the ability to re-run a step in a different workspaces (with updated code, or in a different environment).It turns out this works great for implementing agentic systems - you can provide references to tasks as tools to an LLM call and have the AI drive - tasks can be easily sandboxed. And Claude is very capable of using the CLI to interact with the orchestration server to submit workflows, investigate failed runs, make updates to workflows and re-run steps.I'm trying to make sure it's easy to try out - there's a self-contained CLI that can be used to start the server (a single Docker container), run worker processes, and then interact with the server. The dev mode automatically restarts the workers as you make local changes. There's also a hosted UI for observing runs in real-time, where you can see the execution graph, access logs/metrics/assets/etc - it works without creating an account - the browser interacts with your orchestration server directly.

reply

cackjaptain

4 hours ago

 |
parent
 |
next

[–]

Sounds and looks very similar to prefect. What does Coflux do different than prefect?

reply

mattrighetti

1 hour ago

 |
prev
 |
next

[–]

I’ve just released v2.0 of Kintoun (
https://kintoun.app
), an iOS client for Cloudflare that I’ve been building for quite a while now.

reply

idatum

10 hours ago

 |
prev
 |
next

[–]

My wife is on a business trip and so it's just me. Some learnings to share on how the house works:

- Weirdly, the kitchen sink is almost exactly the geometric center of the house; hence, equal probability for odors to travel.- And that reminds me: Need to download PDF for dishwasher operation.- Day 2 (Friday) of my wonderful better half's travels, I started laundry. I remembered less then 2 days later that I need to transfer the clean (??) clothes from the bottom device (water/soap) to the upper "dryer" -- this device produces some serious heat. Kills odor causing bacteria, and stuff. Will call that a success.- I find my clothes are scattered on the floor randomly. Seriously high entropy -- reminds me of CloudFlare's lava lamp application:https://en.wikipedia.org/wiki/Lavarand- Yep, total regression to the mean of bachelor-self and loving life..and the miracles of modern technology, where like the water automatically fills in the washing device. But not the soap.

reply

calvernaz1

1 hour ago

 |
prev
 |
next

[–]

Working on implementing the web both auth standard and a take on federated and out-of-band agent bot validation.

https://github.com/calvernaz/wba

reply

brynet

2 hours ago

 |
prev
 |
next

[–]

Making rent as an open source developer.

Shamelessly trying to attract new monthly sponsors and people willing to buy me the occasional pizza with my crap HTML skills.https://brynet.ca/wallofpizza.html

reply

nirvael

2 hours ago

 |
prev
 |
next

[–]

Using a Muse EEG headset to read brain activity and use that to drive the output of a GAN. Similar to other projects that try to visualise or decode thoughts, but at the moment it's an art project. Obviously quite limited by compute and hardware. I'm sort of looking for collaborators / co-founders / opportunities in the AI + neuroscience + creativity space.

reply

martimchaves

2 hours ago

 |
parent
 |
next

[–]

That sounds really cool, how are you going about this? Are you training a model using your own EEGs as inputs?

reply

nirvael

48 minutes ago

 |
root
 |
parent
 |
next

[–]

I've been working on my own GAN for a while, trained on a few different datasets. Then the EEG data is fed into the GAN in real-time and used to interpolate within it's latent space. I assign each brainwave band (e.g. alpha, beta, etc.) to it's own point within that latent space, so the core idea is that as alpha increases (for example) the output heads towards that point in the space and that's reflected in the output image. Happy to talk more.

reply

walkintherhythm

2 hours ago

 |
parent
 |
prev
 |
next

[–]

Hey interested in this, do you have an email or point of contact?

reply

nirvael

46 minutes ago

 |
root
 |
parent
 |
next

[–]

Yeah you can email me (alex dot whelan at live dot co dot uk) or you can contact me through instagram (@aphynia)

reply

abdullin

4 hours ago

 |
prev
 |
next

[–]

I built a platform to learn how to build personal AI agents and test them with fast feedback. It is free for individuals and small teams.

Platform deterministically generates tasks, creates environments for them, observes AI agents and then scores them (not LLM as a judge).We just ran a worldwide hackathon (800 engineers across 80 cities). Ended up creating more than 1 million runtimes (each task runs in its own environment) and crashing the platform halfway.104 tasks from the challenge on building a personal and trustworthy AI agent are open now for everyone.https://bitgn.com/To get started faster you can use a simple SGR Next Step agent:https://github.com/bitgn/sample-agents

reply

vulkoingim

4 hours ago

 |
prev
 |
next

[–]

Been working on and off on a Spotify recommendation egnine after getting tired of Spotify’s repetitive recommendations.

You get to choose the genres you're interested in, and it creates playlists from the music in your library. They get updated every day - think a better, curated by you version of the Daily Mixes. You can add some advanced filters as well, if you really want to customise what music you'll get.It works best if you follow a good amount of artists. Optionally you can get recommendations from artists that belong to playlists you follow or you've created. If you don't follow much or any artists, then you should enable that in order for the service to be useful, as right now that's the only pools of artists the recommendations are based on.https://riffradar.org/

reply

StrangeSound

3 hours ago

 |
parent
 |
next

[–]

This is really cool! Is the underlying tech tied heavily to Spotify? I'm a YouTube Music user and would love to use a service like this

reply

qn9n

2 hours ago

 |
prev
 |
next

[–]

https://github.com/allegro-systems/score
 a full stack Swift web framework with Controllers pattern for the backend and SwiftUI like syntax for frontend code. All renders down to minified HTML, CSS and JS. Includes features for auth, REST, frontend reactivity via signals and more.

reply

wolfy1993

4 hours ago

 |
prev
 |
next

[–]

https://rxiq.co.uk/

Data support tool for pharmacists to identify savings and best value opportunities for their local health system (NHS/UK)I'm a pharmacist, worked in the community for 5-6 years before moving into medicines optimisation, which in short is focused on ensuring we use the right medicine at the right time to get the best return on investment in terms of £/patient outcome.Been a hobby coder for about a decade now, but this is my first attempt at a full stack application (airflow, db, backend, frontend).Mobile formatting is a little bleh and there's some obvious issues. But it's been rather nice setting up something a bit more rigid/resilient than my previous clandestine approaches

reply

dardeaup

13 hours ago

 |
prev
 |
next

[–]

I'm building a website integrity and security monitor. The backend is written in Java/PostgreSQL. The front end is written in JS/React. It will allow for interactive use via front end or be API driven.

I initially was using SSE to push events down to the front end during long scans but decided to switch over to plain old HTTP polling for better reliability across different browsers (and versions of different browsers).Here are the areas of analysis:- accessibility
 -- check for images with missing alt text
 -- check for various form controls missing labels
 -- headings not following (h1->h2->h3...)
 -- missing lang attribute on <html>
 - content
 -- check for forbidden words and phrases
 -- check for required words and phrases
 - performance
 -- evaluate time to load page
 -- check for excessive inline JS
 -- check for inline styles
 - security
 -- check for SSL certificate expiring soon
 -- check for security HTTP headers
 -- check whether Server HTTP header is too revealing
 - seo
 -- check for missing title in head section
 -- check for missing meta description
 -- check for multiple H1 headings
 - site integrity
 -- check for broken links
 -- check for use of deprecated tags
 -- check for insecure http link
 - spell check
 -- check for possibly misspelled wordsHaving a lot of fun building it!Going for a 100% self-service model. No corporate sales cycles, no slide decks, no meetings.Targeting a June launch.

reply

welldoneator

13 hours ago

 |
prev
 |
next

[–]

I'm working on TableForge[0], it's a browser based, solo or multiplayer, D&D 5e game. TTRPG DMing can be effort-heavy and my friend group constantly has trouble finding enough time to play together let alone set it up. In TableForge, the DM is agentic with access to tools strictly following 5e rules. The DM is responsible for narration and reacting to players but your character sheet, inventory, spells are all real server resources you manage. The DM can interact with them through deterministic 5e-based tools (dice rolls, damage, sheet updates, memory). Players can play in real time or async.

You can provide the DM a premise (or pick one from the library) and it'll flesh out a full campaign story arc. Either way it's a fresh story arc reacting to your actual decisions, every time.I noticed every competitor in this space was a chatbot with only the last ~10-15 messages stuffed into context. They forgot things, made up dice rolls and rules, and was generally not what I was looking for. So far TableForge has been working well for my friend groups and some random folks from Reddit/organic search. Solo TTRPGers seem to like it too.It's still in early stages but fully playable. I don't feel comfortable charging anything for yet until I know people enjoy it. If you like it enough to hit the free tier limit, send me some feedback in the webapp and I'll gladly extend your free trial. If you hate it, please also let me know![0]https://tableforge.gg/

reply

nyanmatt

5 hours ago

 |
prev
 |
next

[–]

Mame Sama - A free Android/iOS app for finding vegan resources (primarily within, but not limited to, Japan). Essentially it's Instagram with a location requirement. While not-yet-open-source, that is the plan. I wanted to build something without any intention to monetize it, while relying on the community to contribute to its success and maintenance.

Backend is zig, frontend is in Flutter. First foray into zig and I'm really enjoying it.-https://apps.apple.com/us/app/mame-sama-%E3%81%BE%E3%82%81%E...-https://play.google.com/store/apps/details?id=com.mamesama&h...

reply

phil_r

9 hours ago

 |
prev
 |
next

[–]

I built a desktop X.509 certificate decoder, and a user recently asked for a CLI version that outputs JSON — so I ended up building x509dump.

It’s a command-line tool for decoding certificates and CSRs into structured JSON rather than OpenSSL-style text output.It decodes the underlying ASN.1/DER structure so fields and extensions are fully expanded, making the output easier to work with programmatically.I’m planning to expand it to support more PKI artefacts (e.g. CRLs, Keys) over time.I’m also planning to handle less well-formed inputs (e.g. missing PEM headers/footers, whitespace, or extra surrounding text), which tends to come up in real-world data.It’s free to download — would be great to get feedback if anyone tries it.https://www.redkestrel.co.uk/products/x509dump

reply

xeonax

2 hours ago

 |
prev
 |
next

[–]

A cyberpunk 2077 inspired Tower Defence game
https://github.com/XEonAX/TowerPunk-CyberDefence

I had already developed a tower defence game without AI long time back.Wanted to try my hand at guided vibe engineering and see how faster was it.

reply

riddu

3 hours ago

 |
prev
 |
next

[–]

App for creating a competency matrix, which is at the heart of how a company defines skills, evaluates people, and supports growth. A lightweight tool for managers to run their teams day to day, including 1 on 1 notes, development goals, and overall team management. It's called Matricsy (matricsy.com), but right now I'm working on PL version:
https://matryca-kompetencji.pl/

reply

kristophph

4 hours ago

 |
prev
 |
next

[–]

I am working on a Dungeons & Dragons combat tracker: "Top Of The Round".

For those DMs that use tools like these, my app sits between Shieldmaiden and Improved Initiative in terms of features/complexity. I tried to offer as many features as possible but "hide" them in a way that makes it easy to understand the most important information like initiative order, health and conditions, stat-blocks. But then I added many buttons with keyboard shortcuts and a quick-access command-palette (think MacOS Spotlight or Alfred on Linux) that lets you access even more commands and features just by typing.It is in beta, free and and you can check it out athttps://topoftheround.com

reply

jtempleton

4 hours ago

 |
prev
 |
next

[–]

Building Atlas, a recovery analytics platform for athletes.

The core frustration: Apple Watch collects HRV, sleep stages, respiratory rate, blood oxygen, resting HR. Apple does basically nothing useful with any of it. You get ring animations and step counts.Atlas pulls all of that together and turns it into two scores: recovery and training readiness. The point is to actually use the signal your sensors are already collecting and ensure when you train, it matters. It’s like Whoop, but actually works.iOS app is live (finally!). Happy to talk shop.https://atlasbody.co/https://apps.apple.com/app/atlas-body/id6760951718

reply

niothiel

9 hours ago

 |
prev
 |
next

[–]

I've been working on cardcast.gg. It gives you the ability to play Magic: The Gathering with your friends remotely using a webcam.

I got back into MTG back during the pandemic after a long hiatus and Spelltable is what brought me back. My playgroup lamented more features and something tailored to our needs, so curiosity got the better of me and here we are. :)I've never worked with computer vision before, but I went through a whole journey that started with the classical computer vision techniques and ended with recently migrating to the transformer-based models. Been a really cool adventure!My playgroup has been loving it so far, and I would love for people to try it and tell me what breaks! Discord is on the site.https://cardcast.gg

reply

tracyhenry

11 hours ago

 |
prev
 |
next

[–]

I'm building Eima (
https://eima.app
) which combines your Todo List and Calendar, allowing you to schedule your todos by simply dragging them onto the calendar.

Similar apps have existed before (like Amie), but they were nearly all VC-backed and had pretty much all pivoted to AI (e.g. being an AI note taker). Their approaches to a Todo-focused calendar has been largely unsatisfying due to the focus on Enterprise users and whatever is trendy.Eima, in contrast, focuses on personal use and does one thing very well: scheduling your todos. In particular, I spent a lot of time making sure multi-occurrence todos work smoothly (e.g. todos that need multiple attempts or simply recurring todos). These were not addressed by prior tools at all and had been my biggest motivation to build Eima.Would love some test users! If you end up wanting to give Eima a try please use the code EARLYEIMA to get it for free.

reply

password4321

15 hours ago

 |
prev
 |
next

[–]

PSA: This is the best place to collect upvotes for your vibe coded ideas/projects that you think might not be up to "Show HN" quality yet, whether reproducible at the source code or prompting level(s) of software development or not... the bar is understood to be much lower here.

PSA PS.Don't post generated/AI-edited comments. HN is for conversation between humanshttps://news.ycomtem?id=47340079

reply

fathermarz

4 hours ago

 |
prev
 |
next

[–]

Building Cabreza Command (
https://cabreza.com/product
). Most critical infrastructure orgs manage their OT security program across SharePoint folders, Excel trackers, and slide decks that get updated once a year. The actual state of the program lives in someone’s head.

Command replaces that with a platform that maps to their real sites, real assets, and real operational constraints, so they can actually run the program, not just document it.Consulting firms use it to deliver more engagements with the same team. Asset owners use it to keep the program alive between engagements, or run one themselves.

reply

seyz

3 hours ago

 |
prev
 |
next

[–]

I'm working on RootCX (
https://github.com/RootCX/RootCX
), a platform for building and shipping internal apps and AI agents in production.

Think of it like "Claude code on Supabase", but for internal apps and AI agents.I got tired of choosing the deployment platform, wiring up Postgres, SSO (OIDC), RBAC, audit logs, secret vaults, integrations/tools/MCP, ... from scratch every time I needed an internal tool.

reply

djeastm

14 hours ago

 |
prev
 |
next

[–]

https://www.triviascroll.com

I wanted to make it easier to quickly see/study trending articles on Wikipedia because they tend to make good topics to know before going to trivia night.I've had the domain for awhile, but just made the app today on a whim.I use Wikimedia's api to get the trending articles, curate them a bit, add some annotations to provide some context, then push to deploy the static site.

reply

jftuga

14 hours ago

 |
parent
 |
next

[–]

Nice layout - I really like this.

reply

djeastm

14 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks!

reply

kristoffer

5 hours ago

 |
prev
 |
next

[–]

I have been building an agentic code IDE (like everybody else :)).

https://syntverk.comNative cross platform app coded in rust + tauri.I prefer using it to the other agentic code apps I have used. It has multi tab worktree isolated agents, sandboxed tools, git integration, built in code editor (with inline generation), searchable document support (i.e. upload your docs, datasheet and you or the agent can use them) and even built in local image generation (using stable diffusion and flux schnell) and asset handling for game developers. Oh it also has a remote feature so you can share the gui or deploy it on a server and access it on the go.Working on adding text to 3d also.It is a hobby project that has grown quite large. Feel free to try it out.

reply

StrangeSound

3 hours ago

 |
parent
 |
next

[–]

Very interesting! It would be great to see some pictures of the IDE in action (maybe some demo videos?) in a prominent place so I can see what I am paying for!

reply

kristoffer

3 hours ago

 |
root
 |
parent
 |
next

[–]

Yes, certainly. I will add that very soon.

It is also possible to download and try yourself without paying (there is a free trial period).

reply

polyaniline

2 hours ago

 |
parent
 |
prev
 |
next

[–]

In what sense is it native if it uses Tauri?

reply

raphui

4 hours ago

 |
prev
 |
next

[–]

I’m building TrackCheck, a small app that helps motocross riders quickly see which UK tracks are open for the weekend.

Tracks usually post updates on Facebook, so riders end up checking dozens of pages manually. I scrape recent posts and use an LLM to infer whether a track is open, closed, or unknown for the upcoming weekend.Currently Android-only, with iOS in progress:https://play.google.com/store/apps/details?id=com.lynxleap.t...

reply

ciju

8 hours ago

 |
prev
 |
next

[–]

https://finbodhi.com
 — It's an app for your financial journey. It helps you track, understand, benchmark and plan your finances - with double-entry accounting. You own your financial data. It’s local-first, syncs across devices, and everything’s encrypted in transit (we do have your email for subscription tracking and analytics).
Supports multiple-accounts (track as a family or even as an advisor), multi-currency, a custom sheet/calculator to operate on your accounts (calculate taxes etc) and much more. Most recently, we added support for benchmarking (create custom dashboards tracking nav and value chart of subsets of your portfolio) and US stocks, etfs etc. We recently added family dashboard (e.g. you can see networth, cashflows, income, use sheets at family level and more).

We also write about like:How fund performance explain part of returns, rest is explained by timing. And ways to tease those out:https://finbodhi.com/docs/blog/benchmark-scenariosOr, understanding double entry account:https://finbodhi.com/docs/understanding-double-entry

reply

renegat0x0

6 hours ago

 |
prev
 |
next

[–]

Still working on:

-https://github.com/rumca-js/Internet-Places-Database- Internet meta database-https://github.com/rumca-js/Internet-feeds- list of Internet feeds-https://github.com/rumca-js/crawler-buddy- crawling framework-https://github.com/rumca-js/RSS-Link-Database-2026- link meta from year 2026-https://github.com/rumca-js/RSS-Link-Database-2025- link meta from year 2025

reply

futurecat

4 hours ago

 |
prev
 |
next

[–]

I'm working on several things:

1. Better GitHub insights athttps://temporiohq.com(public and very early stage). Demo of what the product can do here:https://temporiohq.com/open-source/github/symfony/symfony2. My art. Mostly athttps://instagram.com/marc.in.spaceor athttps://harmonique.one/works

reply

BrunoBernardino

4 hours ago

 |
prev
 |
next

[–]

To prevent a big wall of text, duplicate of [1] (similar, but non-AI focused), I'll just say my wife and I are still working on Uruky, a EU-based and simpler Kagi alternative [2], and that's going really well so far!

On that first link you can find a lot of answers to frequently asked questions.[1]:https://news.ycombinator.com/item?id=47700880[2]:https://uruky.com

reply

reacharavindh

5 hours ago

 |
prev
 |
next

[–]

I’m building HobbyBoard - A private(self-hosted) visual library(A Pinterest alternative).

Mostly for myself to use for my hobby. Sharing with everyone because I find it genuinely useful.Yes, it is coded with assistance of LLMs, but I care for the details and it is not vibe-coded in hours.https://hobbyboard.aravindh.net/GitHub:https://github.com/aravindhsampath/hobbyboardDemo (resets every hour):https://demo.hobbyboard.aravindh.net/Almost ready to do a show HN :-)

reply

peterhon

3 hours ago

 |
prev
 |
next

[–]

I built my own fun t-shirt brand called devopsicorn, no AI used here, I worked with a graphics designer from Spain:
https://devopsicorn.com

Fun project playing around with print in demand and Etsy. Now wondering why Etsy became so popular while being tricky and inflexible to use for the seller :-)

reply

nlanandkumar

6 hours ago

 |
prev
 |
next

[–]

Im working on a all-in-one event management platform for studios, event planner etc..,

It consists of CRM, Expense tracking, Equipment Management, Event Gallery( photo share, Face Detection based download, Guest Upload) etc..,https://eventversa.comCurrently working on moving it from cloud supabase to self hosted version.

reply

saltcod

2 minutes ago

 |
parent
 |
next

[–]

Cool project. Curious why you're moving to self-hosted, and if you go through with it, also curious how that experience goes.

reply

aaron5

9 hours ago

 |
prev
 |
next

[–]

https://opendocs.to

It's web service that allows you to channel your google docs through a more human-friendly name. So, you linkopendocs.to/your-name/resume (an example link)to your public resume at docs.google.com/dlkjbalksdfdIt's a simple redirect service, but it just looks nicer, and I think the opendocs.to sounds natural. Got to learn a lot with this one, using Vite/React, Node, Postgres all in Docker, with a local profile that builds nginx inside with the containers, or a prod profile on the server where nginx proxies into the containers.Anyways, check it out!Right now, only free tier available as I some last tweaking and checking.

reply

realty_geek

4 hours ago

 |
prev
 |
next

[–]

I'm quite excited at the prospect of EmDash from cloudflare unseating Wordpress - especially for creating real estate websites.

I adapted my open source ruby on rails real estate website builder to work with EmDash and can already see a lot of potential.It's not ready for production use yet but I'm really enjoying working on it:https://github.com/RealEstateWebTools/emdash_property_web_bu...

reply

zachh

5 hours ago

 |
prev
 |
next

[–]

I made a Slack reader/inbox that allows customizable categories / inboxes, message categorization with rules and/or Claude (optional), and fast keyboard navigation:

https://zmh.org/dispatch/Also put together a directory of 31k+ personal websites, tagged with design keywords so they're searchable. As someone who loves personal sites, I think it's one of the more comprehensive list of indie / personal sites on the web:https://zmh.org/personal-site-gallery/

reply

rcarmo

5 hours ago

 |
prev
 |
next

[–]

I’m working on (and inside)
https://github.com/rcarmo/piclaw
. It started as “my own OpenClaw” and quickly became an entire workspace to develop and test stuff in. It currently runs my homelab, my Obsidian vault, my blog static generator, a lot of my ARM low level stuff, and after some M365 hackery, my personal mail and calendar as well, all properly sandboxed. The home page at
https://taoofmac.com
 has a list of things I’ve been doing with it over the past few weeks.

reply

habitmelon

7 hours ago

 |
prev
 |
next

[–]

Working on an Emacs-like editor that uses Clojure instead of Emacs Lisp. It has a C kernel and then uses libsci (Small Clojure Interpreter, built with GraalVM, so it has no Java dependency at runtime).

I call it Hammock, in honor of Rich Hickey's "Hammock Driven Design"https://github.com/tlehman/hammock

reply

qrush

10 hours ago

 |
prev
 |
next

[–]

I'm working on a new 1v1 scrabble/wordle style game - iOS and Android versions are cooking as well, thanks to Expo.dev. A friend described it as "scrabble that doesn't drag", and I've had a few friends and family members playing
hundreds
 of games (and especially the daily game) over the last few weeks, which has been really encouraging. Play here:

https://wordtrak.com/If you're enjoying it, please leave me some feedback:https://discord.gg/pFjEcbQsv

reply

frail_figure

6 hours ago

 |
prev
 |
next

[–]

I'm working on an app called Limberly. It focuses on health and ergonomics for sedentary workers - probably most of us here :)

It is scientifically proven[1] that sitting is detrimental to our health, with increased mortality rates. The primary way to reduce the negative effects of sedentary work is to move.This means doing sessions of resistance training (gym), running, biking, but also taking micro-breaks during work sessions and performing light exercises and stretches.Research has shown[2] that taking short breaks during work reduces fatigue, and in some cases actually boosts performance.There are plenty of running and gym apps out there, so Limberly focuses on the last part - helping you take micro-breaks, reminding you to change your posture between sitting and standing, changing which hand holds the mouse (if you're into that) etc.It is still in early development, so if you'd like to help test and shape the app as we go, please sign up for the waitlist and I'll add you to the testers group. Feel free to also DM me here with any questions or feedback.https://limberly.appOh, I am also writing a series of articles that explains it more in depth:https://prodzen.dev/articles/building-limberly-part-1-we-re-...1:https://pmc.ncbi.nlm.nih.gov/articles/PMC10799265/2:https://journals.plos.org/plosone/article?id=10.1371/journal...

reply

examineip

2 hours ago

 |
prev
 |
next

[–]

I am building ExamineIP - Free network security toolkit

https://tools.examineip.comCollection of 15 diagnostic tools (VPN leak test, DNS checker, port scanner,
etc.) built after a WiFi security incident. All client-side, no data
collection.Feedback welcome!

reply

ternaryoperator

8 hours ago

 |
prev
 |
next

[–]

Jacobin[0] a JVM written in entirely in go. While we still have a way to go to get to feature parity for Java 21, we can sit back and watch the bytecode instructions fly by as they execute, which is something you can't do with the JDK due to the HotSpot JVM's architecture and the fact that it's written in both Java and C++.

We just crossed 5,000 commits. Also, we take testing very seriously: our test code base is presently 160% the size of our production code.[0] jacobin.org

reply

shikaan

3 hours ago

 |
prev
 |
next

[–]

A native application (Windows, Linux, MacOS) for music transcription.

It comes with time stretch and pitch shift as most of these softwares do, but it allows you to save loop regions and take notes. It's designed to be a practice session tool.I'm doing it from first principles, and having fun writing GPU code, platform shims, and squeeze every ms I can to make it fast and smooth.I will be looking for testers soon. If anybody is interested, hit me up.

reply

ymyms

6 hours ago

 |
prev
 |
next

[–]

I'm making capability security for distributed systems. The primitives and engine are both open source.
Primitives:
https://github.com/Hessra-Labs/hessra-tokens

Engine:
https://github.com/Hessra-Labs/hessra-cap

It's built using biscuits and written in rust. I'm really into it. Using capability security as a model makes building things feel like they snap together a lot more naturally. At least for me.I've also got a blog post describing it in more detail:https://www.hessra.net/blog/what-problem-led-me-to-capabilit...

reply

fredwu

5 hours ago

 |
prev
 |
next

[–]

Have been working on three micro-saas, all built in Elixir/Phoenix:

https://feedbun.com- a browser extension that decodes food labels and recipes on any website for healthy eating, with science-backed research summaries and recommendations.https://rizz.farm- a lead gen tool for Reddit that focuses on helping instead of selling, to build long-lasting organic traffic.https://persumi.com- a blogging platform that turns articles into audio, and to showcase your different interests or "personas".

reply

joladev

5 hours ago

 |
prev
 |
next

[–]

https://larm.dev
, an uptime monitoring service with a focus on reliability and reduction in false positives. I’ve been building it for myself really but I figure it’s worth sharing it with people in case someone else finds it useful too.

It’s also a lot of fun to work on. Phoenix LiveView dashboard, go probes running on 4 continents, connected to the backend using websocket tunnels. Clickhouse for reporting. Even did a CLI and an MCP for fun.You can take the probes for a spin with the free response time checking tool and see how fast your site ishttps://larm.dev/tools/response-time

reply

jaspanglia

2 hours ago

 |
prev
 |
next

[–]

We recently Signed MOU with Disability service provider and start working with them under GDPA laws. Our whole team is super excited about it. How about you guys ?

reply

alexissantos

8 hours ago

 |
prev
 |
next

[–]

Secret Hangout: Private themed lounges for karaoke, board games, and video games, with drinks and snacks. Just launched it a couple weeks ago.
https://mysecrethangout.com/

Building up the marketing now. Starting to get some coverage on Instagram:https://www.instagram.com/p/DWxWo_oDfkm/

reply

MaxLeiter

12 hours ago

 |
prev
 |
next

[–]

I’ve been working on modernizing
https://thelounge.chat
, a self-hostable web based IRC client

Modernizing in two ways: migrating to new JS tooling (webpack -> vite, Node’s built in sqlite, etc) and adopting ircv3 features like emoji reactions, threaded replies, and typing indicators. Trying to bring IRC into the 21st century.Its easy to contribute to and we have an active irc channel (perks of building an always-on client…) - feel free to join us! #thelounge on irc.libera.chatCheck out the bundle / CPU savings by leaving webpack:https://github.com/thelounge/thelounge/pull/5064

reply

ekianjo

12 hours ago

 |
parent
 |
next

[–]

Is it going to be a fork ?

reply

MaxLeiter

11 hours ago

 |
root
 |
parent
 |
next

[–]

No, I have a bunch of PRs up and some already merged

We’re aiming for a minimal maintenance release soon, then a larger feature release after.

reply

xlii

5 hours ago

 |
prev
 |
next

[–]

A small project but something that I'm happy about: Postgresql backed persistent queues crate for Rust.

I couldn't find any crate that would be ergonomic enough to use and provide features I deem essential, i.e. retryability, scheduling, poison job detection, barriers, backoff strategies etc.it's an area I'm familiar with so after spending 2 days trying to integrate external libs I decided to roll my own and I'm quite happy how it turned out in 2 days of development.I plan to open-source it in the near future but right now using it in my another project and it's running quite well.

reply

jgord

6 hours ago

 |
prev
 |
next

[–]

B2B SaaS to host 3D scans of DataCenters and industrial plants.

https://quato.xyzBasically a google streetview tour of your Datacenter or large industrial plant.You can do some nice things like draw 3D linework to trace the paths of pipes, conduits, eg :https://youtu.be/t8nRhWUl-vAadd notes with markdown and html links at useful places in the 3D space.We have add-ons for generating an 'xray' view floorplan to make it nicer to navigate a large space.I think we are the first to have a web uploader that can preview and import .e57 panoramas, directly in the web page [ and skip the points if you dont need them ]Currently in use by a telco in the Americas.

reply

adityaathalye

5 hours ago

 |
prev
 |
next

[–]

Still (in fits and starts) working toward a Bitemporal SQLite based (SaaS, for now) software architecture, because of an obsession with this notion of "Sovereign Software". Any SaaS I build should
never
 lock in customer data, for example.

Current state of work: The implementation of the core data model iswrong. I need to throw it away and redo it from scratch.Whiplash status:WTF, Time. y u move so fast?This thread made me---forced me---to accept that it's been well over a year of the agony and ecstasy of solo software construction. Or maybe 2026 is moving way too freaking fast. Or it's good to be obsessive I guess.

reply

solomonb

14 hours ago

 |
prev
 |
next

[–]

Still working on my LPFM radio station
https://www.kpbj.fm/

We have over 60 shows now, rented a studio, and are in talks to security a site for our tower. I'm building out an online store but really need to focus on fundraising.

reply

ksymph

16 hours ago

 |
prev
 |
next

[–]

I'm building my ideal backend for small projects and hobby stuff. It's inspired by PocketBase, but built around Lua scripting instead of built-in endpoints or usage as a Go library.

Like PocketBase, it's made in Go, has an admin panel, and compiles down to one executable. Here, you write your endpoints as Lua scripts with a simple API for interfacing with requests and the built-in SQLite database. It's minimal and sticks close to being a bare wrapper around the underlying tech (HTTP, SQL, simple file routing), but comes with some niceties too, like automatic backups, a staging server, and a code editor inside the admin panel for quick changes.It comes from wanting a server that pairs well with htmx (and the backend-first approach in general) that's comfy to use like a CMS. It's not exactly a groundbreaking project, and it still has a ways to go, but I think it's shaping up pretty nicely :)link:https://github.com/ksymph/mogo

reply

higgins

15 hours ago

 |
prev
 |
next

[–]

An app which blocks your code if you don’t do some pushups (facial tracking + accelerometer).
https://gitpushups.com

reply

jtap

9 hours ago

 |
prev
 |
next

[–]

My daughter introduced me to Pokémon TCG. We found a local group and have been playing for about a year and a half. At this point we have so many bulk cards that it takes way too long to search through them. Other than a few specific pulls we keep in a binder, we honestly have no idea what we own.

I’ve been building a phone app + website (https://MyBulkCards.com) to scan cards and organize where everything is. It’s pretty basic right now, but I can store cards in boxes like “Box 1 AAA, Box 1 BBB, …” and find cards easy peasy. There’s also a friends feature so I can see what others have locally. We borrow cards from each other quite a bit.It’s been a fun project to build. I trained one model to find a card in the camera frame and another to identify it. Still iterating a lot. One epoch on my Mac M4 takes about 2 hours, and I’m still seeing improvements past epoch 10. Even now, it can find and identify a card more often than not, even without the OCR bits. Both models are under 20MB, run directly in the camera frame, and are fast enough to identify a card as I slide it into view.I started with Android since that’s what I have, and I’ve shared the app store testing link with my local group for testing. The app is built in React Native, and I’m hoping to get an iPhone version out soon since there are a bunch of iPhone peeps. A couple of the players also got me into MTG, so now I’ve got a pile of Turtles cards too. I’ll be training an MTG model next. I don’t think it’ll be too bad since I can reuse most of the same approach.

reply

Operyl

9 hours ago

 |
parent
 |
next

[–]

Haha! I did something similar, and went as far as integrating a label printer (ZQ620) and use a TC53 with the barcode scanner to sub organize quickly :x.

reply

cyrilou242

3 hours ago

 |
prev
 |
next

[–]

Building a video game adaptation of Pass The Pigs (the "dice" game where "dice" are plastic pigs).

Early preview here:https://piggy-toss.netlify.app/The goal is to play with friends, we love this game.

reply

driese

5 hours ago

 |
prev
 |
next

[–]

I'm trying to get back to verifying some of my old fun ideas. I want to finally build my 3D QR cube (
https://deriese.net/qrcubes.html?s=hn
) by sending a design to a laser shop, and I also want to find someone with a few termocouples to verify my results to the coffee cup cooling problem (
https://deriese.net/coffee.html?s=hn
). If anyone wants to help, feel free to send me a message.

reply

raybb

8 hours ago

 |
prev
 |
next

[–]

Just today I helped co-host the SF Permacomputing Club.

It was a lot of fun and I love all the good energy people bring to the conversation about long lasting and community driven tech.https://permacomputing.net/https://luma.com/e27gae3q

reply

coldstartops

6 hours ago

 |
prev
 |
next

[–]

Synchronous P2P file sharing tool with post-quantum encryption and virtual mount point (
https://keibisoft.com/tools/keibidrop.html
)

Both peers mount a virtual FUSE folder. Files shared by one side appear in the other's folder in real time. You can open, copy, and browse your peer's files as if they were local. Files go directly between devices over encrypted gRPC.
(by default it tries over LAN, then direct IPV6, then uses a data relay).The hardest part has been making git repos work through the FUSE mount between peers.(Been developing the tool for 12 months now, very close to a full release)

reply

hathers

6 hours ago

 |
prev
 |
next

[–]

Working on tooling to help make working with agents in parallel easier, with minimal tools/no deps -
https://github.com/andrewhathaway/ag.sh
 I don’t want to manually manage worktrees, tmux sessions, branches but want to remain in the terminal.

Also recently built a home energy cost/consumption display for the TRMNL -https://andrewhathaway.net/blog/ambient-cost-display-for-oct...

reply

mindcrime

9 hours ago

 |
prev
 |
next

[–]

I've been building an AgentRegistry. Right now it is mainly based on A2A Agents that run in Docker containers. There's an auto-register module that watches the Docker system event log (I'll add support for K8S eventually) and if it sees a container spin up with the right labels, it fetches the AgentCard from the Agent, then registers an Upstream and Route with APISIX, then updates the 'url' field in the AgentCard, and stores the AgentCard in the Registry.

The Registry in turn has two interfaces: one REST, and one A2A itself. If you hit /.well-known/agent-card.json on the Registry server, you get the AgentListerAgent, which supports searching for Agents by various criteria. Or you can search using the REST interface. In either case, you get an AgentCard that points to the correct APISIX endpoint to talk to the desired Agent.Besides adding K8S support, other plans include adding support for other proxy providers (including Istio for the K8S case), supporting Agents that are not based on A2A and, allowing Agents to register themselves using the Registry API, and... uh, well, that's the main stuff I have in mind right now. Aaah, wait, I might do something along the lines of integrating an MCP Registry as well, not sure yet. Heck maybe I'll get bored and make it an all-out API registry for all sorts of endpoints... could integrate a UDDI server and bake in WSDL support for good measure! (Don't count on that last bit happening anytime soon).Anyway, no repo to share right this second, but I do intend to make it open source. I'm just committing the cardinal sin right now of wanting to "make it presentable before releasing the code".

reply

alfg

4 hours ago

 |
prev
 |
next

[–]

Just recently launched my suite of media inspection and encoding tools based on FFmpeg.

https://video-commander.com.Still iterating through refinement and features. It's built on Rust + Tauri with a React frontend, in case anyone is curious.I've created various open-source and commercial tools in the multimedia space over the last 10+ years and wanted to put it all together into something more premium.

reply

ThePyCoder

6 hours ago

 |
prev
 |
next

[–]

Worked on some features at open reader, a local-first PDF TTS reader that highlights the words spoken and uses the excellent local kokoro tts engine.

Got fed up with web tech, it's so slow and clunky, so made my own version in python and qt. I changed the design to be based on a doclayout llm, so you can skip or include things like tables and references easily.It now works so beautifully fast, it's code is readable and simple, no apis or multiple services. Just a qt app, some local llms that can run on a decent cpu and word-leven highlighting and playback selection.https://github.com/thepycoder/projectwhy-ttsI can listen to papers now!

reply

yu3zhou4

12 hours ago

 |
prev
 |
next

[–]

An open course on building high performance LLM inference engine! Hope to finish by the end of April

https://github.com/jmaczan/tiny-vllm

reply

thevaultdj

2 hours ago

 |
prev
 |
next

[–]

Building MusicLibrarian, it's a macOS app to clean up Apple Music libraries. Detects duplicates via ISRC codes, fixes metadata, identifies tracks available in lossless. Free at thevaultdj.com

reply

jason_zig

12 hours ago

 |
prev
 |
next

[–]

Crossed 100K MRR as a solo founder for Zigpoll[1] - honestly I never thought I would get this far with the product so now it's all about trying to market and keep growth strong. Doubling YoY gets harder each year so you always have to find new growth channels (or ways to improve existing channels). This is an interesting task especially given the current environment.

I used to think "if you build it they will come" but, as it turns out, it's much more nuanced than that and requires a lot of iterating and stumbling along the way. I hope to break into another vertical this year![1]https://www.zigpoll.com

reply

AshesOfOwls

15 hours ago

 |
prev
 |
next

[–]

I'm working on
https://react.tv

It lets you create TV channels from digital media such as YouTube, The Internet Archive, TikTok, Twitch, and Dailymotion. It does that by letting you schedule videos against a custom calendar system.Since filling out even a month of content can be a lot of work, I built some things to make the process easier.* Advanced scheduler to know when and how long content can be played at any given datetime* Real time team collaboration* Channel libraries to organize media* "Blocks" - Create a dynamic schedule which generate hours of content that mimics real television scheduling. It even carries over your playback history between generations so that playlists continue from where they left off.* A catalog to find media from official sources on YouTube* Embeddable as an OBS browser source to restream your owned content* Repeat content infinitely or temporarily to create 24/7 channels.If all goes well I am hoping to re-release sometime this month.

reply

mattkevan

14 hours ago

 |
prev
 |
next

[–]

I’m making Bezier, a mac-native vector design app as an alternative to Figma and Sketch.

Unlike those apps it has full support for design tokens and (so far) flexbox layouts. It can also export directly to HTML, rather than a fake preview mode. I’m also working on full code-backed components, so you can go between code and design very easily.As a designer, I’ve been frustrated for years by the gap between design and code, and despite all the new AI features, Figma still hasn’t got any further in years - design tokens need a 3rd party plugin and responsive designs are a pain in the bum. So I decided to build something that has the ease of Figma while being much closer to live code.I’ve got to the point where I’m designing the app in itself, tokens are working, html export is working and nearly ready for first betas.

reply

Ttlequals0

10 hours ago

 |
prev
 |
next

[–]

MinusPod is a self-hosted server that removes ads before you ever hit play. It transcribes episodes with Whisper, uses an LLM to detect and cut ad segments, and gets smarter over time by building cross-episode ad patterns and learning from your corrections. Bring your own LLM -- Claude, Ollama, OpenRouter, or any OpenAI-compatible provider.

https://github.com/ttlequals0/MinusPod

reply

spanferov

8 hours ago

 |
prev
 |
next

[–]

Hello folks, I'm a former Figma employee and while working there I've been amazed how well visualization and whiteboards actions work for humans. I've been working on a new tool to organize my family that is centered on the idea of a whiteboard with tiles of different kinds. It's still a little rough but maybe some of you would enjoy it.
It supports daily journals, calendars, text, files. You can use it to organize yourself or create beautiful galleries for your memories. I've tried to create something simple that even kids can understand and use. For example, you can click and hold a little star at a corner of the Journal tile to record an achievement and my kids love it.
I'm not trying to sell anything, the tool is currently completely free and has versions for Web, MacOS and iOS. Please checkout
https://umka.day/
 and share your feedback, I really appreciate this.

reply

meander_water

3 hours ago

 |
prev
 |
next

[–]

I'm building this mostly to scratch my own itch

https://findsubstack.comIt's a newsfeed constructed from 130k substack RSS feeds but limited to the past 24h.Its helping me discover writers other than just what the algorithm gives me.

reply

farathshba

6 hours ago

 |
prev
 |
next

[–]

Hi HN,

I’m working on OurCodeLab, a Singapore-based startup. After 11+ years in DevSecOps, I noticed a lot of local SMEs are either overpaying for simple sites or using insecure, bloated templates.I’m trying to solve this by building high-quality, lightweight landing pages at the most affordable rate possible. Right now, I’m running a promotion: we’ll build your landing page (up to 2 pages) for free if we handle your domain hosting.I craft each site individually to ensure they meet modern web and cyber standards—no copy-paste layouts. I’d love to hear your thoughts on the model or any feedback on the tech stack.If you're an SME or know one that needs a hand, reach out at farath@ourcodelab.com for a non-obligatory chat.

reply

nickjj

16 hours ago

 |
prev
 |
next

[–]

I evolved an rsync based backup script I've been using for almost a decade into
https://github.com/nickjj/bmsu
. I use this for backing up my life's work to an external drive but also syncing files to my laptop and phone too. It supports easy restoring as well.

No traffic ever leaves your local network and since it uses rsync under the hood the devices being sync'd to don't need to run anything other than SSH.It's a single file shell script that has no dependencies except rsync. It's literally 1,000+ lines of defensive checks and validations to make sure you're not shooting yourself in the foot with rsync, and at the end the last line of code directly calls rsync. It doesn't try to reinvent the wheel by replacing rsync (it's an amazing tool).

reply

Havoc

4 hours ago

 |
parent
 |
next

[–]

Looks like a nice setup. Bit confused as to why you’d use a sync tool without versioning for backup?

reply

nickjj

1 hour ago

 |
root
 |
parent
 |
next

[–]

> Bit confused as to why you’d use a sync tool without versioning for backup?

This tool doesn't enforce how you use rsync, it offers suggestions. You can use rsync's flags that help with versioning by modifying 1 config value to add them and now you have versioned backups using all of the strategies rsync supports.

reply

jftuga

16 hours ago

 |
parent
 |
prev
 |
next

[–]

Nice work, I like it.

reply

nickjj

16 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks, it's always fun when you're scratching your own itch.

It's also a nice excuse to build in quality of life features that don't take a lot of time because you're using the thing all the time. My favorite one is the color coded rsync command output when DEBUG=1 is set so you can be absolutely sure your config values are producing the expected rsync flags and args.

reply

labarilem

4 hours ago

 |
prev
 |
next

[–]

Trying out games posted to HN so i can add them to
https://hn-games.marcolabarile.me/

Testing out some ideas to automate data entry workflows from an italian powerlifting federation (FIPL) to OPLhttps://www.openpowerlifting.org/

reply

pizzly

9 hours ago

 |
prev
 |
next

[–]

A browser extension & windows app that automatically redacts the text you paste to prevent your private data from leaking to the third parties. Its an AI model that runs 100% locally on your own device so that your clipboard contents do not leave your device.

http://redactor.negativestarinnovators.com

reply

ben8bit

5 hours ago

 |
prev
 |
next

[–]

Working on Fronteer, a project management app that (1) integrates messaging more cohesively with tasks and (2) better supports external collaborators - think agency clients, customers, etc.

Some of the biggest pain points we’ve seen is chat being separate from a solid task manager, and the pain of collaborating with people outside your own org.We’re currently in private beta and hope to open it up to the general public soon!https://fronteer.app

reply

sudoapps

10 hours ago

 |
prev
 |
next

[–]

Coding agents have changed how I build. Constantly switching between the terminal and an IDE started to feel inefficient, so I wanted a better terminal-first setup where I could manage multiple agent sessions and make quick edits without the overhead of a full IDE. So I built Helm for myself:
https://github.com/samirkhoja/helm

reply

craigmccaskill

10 hours ago

 |
parent
 |
next

[–]

This is really cool. I'll be checking it out!

Seems to solve most of my issues with my current workflow. My primary personal development machine is my WSL ubuntu install on my windows gaming PC and the tooling outside of the mac ecosystem has been really limited.

reply

sudoapps

9 hours ago

 |
root
 |
parent
 |
next

[–]

Awesome! Let me know if you run into any issues with the setup.

reply

fcarraldo

9 hours ago

 |
parent
 |
prev
 |
next

[–]

I know there's no such thing as a unique name anymore, but
https://helm.sh/
 is rather popular.

reply

ashxel

8 hours ago

 |
prev
 |
next

[–]

Back in the day, my friends and I loved to rip a few games of Curve Fever 2. The original is gone and the game that took its place has objectionable aesthetic and gameplay tweaks.I've been working on making my dream "curve-like" game that captures the elegance of the original's gameplay while also allowing optional stuff like portals, rocket launchers, custom maps and modes like capture-the-flag. I'm kind of going for that sense of hilarity and semi-competitiveness of e.g. Halo 3 custom maps and modes.

https://recurvegame.comMy friends and I have been having a great time playing the initial version, and it's been fun working on some of the more interesting technical aspects like server + browser performance, mapping 2-d game space onto a 3-D visual space, etc. as well as some just-because-I-want to things like a dynamic music system.

reply

khacvy

8 hours ago

 |
prev
 |
next

[–]

I built an AI that turns YouTube videos into interactive tutoring sessions

Paste a link → AI breaks it into sections → teaches you on a whiteboard with voice → quiz + flashcards at the end.It's free to try while in beta:https://www.pandio.online

reply

shivang2607

6 hours ago

 |
prev
 |
next

[–]

I am building devlens.io, an open source tool for codebase visualization tool for easy onboarding and easy PR review. The most interesting and loved feature of the tool is blast radius i.e., If I change this component, how far will the effect be propogated ?

github repo if you wanna check :https://github.com/devlensio/devlensOSSwebsite :https://devlens.io

reply

ewams

14 hours ago

 |
prev
 |
next

[–]

Published 3 articles so far, but working on AI architecture and management. While most people are focused on prompt engineering and making stuff with AI; I'm more interested in how it actually works, how to size workloads, how to maximize performance, the security and safety aspects. Here is my most recent article where I played with benchmarking tools to get a baseline and understand how configurations impact token generation

https://ewams.net/?date=2026/03/29&view=Qwen35_Performance_w...

reply

yuppiepuppie

16 hours ago

 |
prev
 |
next

[–]

I keep on refining
https://hnarcade.com

I’ve got a decent amount of people on the newsletter so trying to figure out how to best deliver indie games via that channel and in the end get more people playing these awesome games people develop :)

reply

smogg

3 hours ago

 |
prev
 |
next

[–]

I built a Mac app (
https://revryte.com
) that replaces the ChatGPT copy-paste loop. It transforms text in place or inserts smart snippets in any app using AI.

reply

kami23

10 hours ago

 |
prev
 |
next

[–]

Been working on something that I use daily, and decided I wanted to see what kind of other ideas I could get out of it, it's very basic article to speech using piper models at the moment.

https://reader.n0tls.com/The part I cared about was being able to send links via one click in my browser or two taps on my phone as I want to read every HN article who's title I find interesting, but don't have the time to read right at that moment.It then at the moment publishes it to an RSS feed so I subscribe to it in Podcast Addict, but I've also just been using the web app as my reading list and tracker.Been playing around with different settings on the piper models and different techniques for getting the most out of my four dollar instance:https://experiments.n0tls.com/Up next is to work on making the voice better (I'm impressed with the out of the box stuff already), and then making it better at finding the real content on a page and only recording that. It's a problem space I don't know much about, but find fascinating, been fun so far.

reply

vivekkairi

4 hours ago

 |
prev
 |
next

[–]

Trying to improve my fine tuned whisper through more custom dataset. I can still see it not understanding certain things currectly.

https://vivekkairi.com/fine-tuning-whisper-to-my-speech/

reply

jimjeffers

6 hours ago

 |
prev
 |
next

[–]

I’m working on my own markdown IDE / Google Docs competitor with an AI agentic editor that coaches on strategy in addition to proof reading. I made it as a side project. Designed it entirely by taking screenshots, annotating them, and giving feedback to codex. Basically applied everything I learned utilizing Claude code a d codex extensively at work to this side project to see how fast I could ship something that felt complete. Check it out:
https://clarus.page

reply

lucasgerads

3 hours ago

 |
prev
 |
next

[–]

I am building a dev envirnmont to use Claude Code (or other agentic coding tools) for electronics development. I give Claude access to my lab equipment like my scope. That way I can let claude programm an MCU and at the same time verify that it creates the right output. Also, it can correlate spice simulations with the actual measurements. Which is often tedious to do "manuall" and verify how good my spice simulations are. I am going to record a longer demo, but here is very short video I made about it:
https://lucasgerads.com/blog/lecroy-mcp-tutorial/

reply

pasxizeis

7 hours ago

 |
prev
 |
next

[–]

As a means to learn about both WebAssembly and Rust, I started writing a WebAssembly binary decoder (i.e. a parser for `.wasm` files) from scratch.

Recently it hit v3 spec conformance. (I'm executing the upstream spec test suite.)I don't plan to make it a highly-performant decoder for use in production environments, but rather one that can be used for educational purposes, easy to read and/or debugging issues with modules. That's why I decided not to offer a streaming API, and why I'll be focusing on things like good errors, good code docs etc.https://github.com/agis/wadecP.S. I'm new to the language so any feedback is more than welcome.

reply

jakevoytko

11 hours ago

 |
prev
 |
next

[–]

I have some blog posts coming out soon. I’m also trying an experiment where I make YouTube videos[0] on each of them. My first video was a huge lift, since it was my first time doing everything.

Random observations from my first one:
- presenting my idea visually helped crystallize my thinking in a way that writing doesn’t. And writing was already very good at crystallizing my thinking.
- even making a bad video was a lot of work
- making a video presentable is a deep subject. Subtle changes were throwing off my setup. Now I understand why so many influencers are fitness and lifestyle; the demand side is obvious, but when you’re already camera-ready you have a huge advantage on the supply side
- described something I built felt natural. I do that for a living. The intro was like 45 seconds and took me like 45 minutes to film because it was acting and I don’t know how to do that
- learning about video editing features had an immediate payoff because video is so long[0] I’m posting the videos athttps://m.youtube.com/@bitlog-dev. I said if the first one got to 100 I’d commit to making at least 10, and I just crossed that threshold

reply

rawoke083600

8 hours ago

 |
prev
 |
next

[–]

a 90's Art Style (think Street Fighter 2) - Surf Forecast App.

I wanted a surf forecast app that i can look at glance, which "time-slot" of the week is good enough to go surf.And I wanted it to look like nothing else out there, at least surf forecast wisehttps://swellslots.com

reply

KhayaliY

5 hours ago

 |
prev
 |
next

[–]

Got fed up that startups and small companies having to pay for Enterprise level compliance and sustainability tools, to be considered as a supplier.

So built Sustalium (https://sustalium.com) which is designed to be easier and faster for micro-small-medium businesses to comply with majority of compliance & sustainability frameworks.

reply

petargyurov

5 hours ago

 |
prev
 |
next

[–]

I recently built Cranki [0], a free little PWA that generates crosswords using your Anki flashcard lists. It's aimed at language learners (who find flashcards boring and crossword fun!).

To be honest I built it just for me and then decided it might be useful for others.It's all local, no server, no database, etc. Mobile and desktop friendly.[0]https://cranki.app

reply

ximm

5 hours ago

 |
prev
 |
next

[–]

I am working on
https://github.com/xi/xiio
, a minimal async runtime for python. It is mostly feature complete with a fraction of the code of asyncio or trio. It is great fun to get into low level stuff and hopefully it helps me to better understand the finer details of async programming.

reply

thunfischtoast

5 hours ago

 |
prev
 |
next

[–]

I've been working on
https://game-pick.eu
 , a website for friends to easily decide on games to play together. It is voting-based and can show who has which game in their library to see who would yet have to buy it. I'm planning on adding features for finding new friends to play with also. It's my first real web project, so I'm excited how it will go.

reply

NiloCK

12 hours ago

 |
prev
 |
next

[–]

I am working on [1] a modernized open (AGPL) stack for interactive tutoring systems. SRS++, with hooks for defining your own pedagogical protocols over knowledge dependency graphs, Elo rating systems, etc, and with an eye toward gracefully differentiable curriculum that can hill-climb in terms of its efficacy.

With this stack, I'm scaffolding several (fingers crossed) commercial learning SaaS products. The first [2] is LettersPractice - a minimalist early literacy app that's family-first, in so far as it presumes an adult supervisor who co-learns strong confidence as a phonetic coach both at and away from the app. Putting considered rails on the parent-child reading experience.The second set of apps is in music, with some experimental dev right now against piano (via midi devices), flute [3], aural skills, and sightsinging.[1]https://github.com/patched-network/vue-skuilder,https://patched.network/skuilder[2]https://letterspractice.com[3]https://flutor.app/

reply

turadg

9 hours ago

 |
prev
 |
next

[–]

Git worktrees are awesome but they broke my workflow in a couple ways:

Resuming work. I used to `j <reponame>` then `gco <branchname>`. Now if I do that I get an error about the branch being checked out already in another worktree. I realized the branch names are pretty unique across repos so I made ` jbr <branchname>` that works from anywhere.Jumping within repo. The other kink was when I wanted to focus on a particular package I’d do `j <subdir>` and it would usually be unique enough to jump to the one in my current checkout. But now I have dozens of concurrent checkouts and have to pick, even though I’m already in the repo. So `jd <subdir>` does like autojump or zoxide but only within the current checkout.To power those shell functions I made a “where” extension for Git.https://github.com/turadg/git-whereIt’s working out nicely!

reply

linzhangrun

10 hours ago

 |
prev
 |
next

[–]

LLM has made scripts incredibly cheap, and their lifecycles as short as one-off.
Batch rename? "Please implement a Python script." Remove background from images? "Please implement a Python script." Or various operations that could be described in a few sentences but used to take a lot of time—"help me implement a script..."
With development time nearly zero, creating a new file, running a script, then deleting the script becomes the most time-consuming part, which feels very clunky. So I wrote RunOnce—targeted at this kind of one-off script scenario. It registers in Windows 11's right-click menu; click "Run Code Here" and a minimal editor appears. Paste your code (or generate it inside), run—automatic language detection, file cleanup, etc., much smoother :)
Written in WinUI3, follows Windows 11 Mica guidelines, distributed on the Microsoft Store:

https://github.com/Water-Run/RunOnce

reply

anupshinde

7 hours ago

 |
prev
 |
next

[–]

Built/building godom, a framework that lets me build local apps in Go, with the browser serving as a dumb view layer. I don't hate JavaScript or React, but my primary motivation was to eliminate NPM as much as possible.
https://github.com/anupshinde/godom

I used AI to create the first POC, and once it was proven, it was improved, and AI handled a lot of grunt work where it could. The framework was built primarily to solve my pain points

And building Fractiz.com, a customizable pre-coded backtests platform.

reply

rndhouse

17 hours ago

 |
prev
 |
next

[–]

VCamper: use LLMs to spot security fixes before CVE publication

Once a patch for a security vulnerability is public, the patch itself can reveal the vulnerability before the CVE is published. VCamper uses a staged LLM pipeline to analyze a Git commit range and flag likely vulnerability patches, even when they look like routine changes.It’s still a proof of concept, but on known cases like curl CVE-2025-0725 it got close to the published root cause from the patch alone.This matters because LLMs could make it much harder to keep security fixes quiet: once the patch is public, the bug may be recoverable almost immediately. Quietly shipping a fix and hoping it stays under the radar may stop being a reliable strategy.https://github.com/rndhouse/vcamper

reply

einhard

5 hours ago

 |
prev
 |
next

[–]

I recently rebuilt my homelab after moving countries, and in the process updated Proxmox to v9.1.6. Been playing with centralizing my databases into their own LXCs rather than creating an individual one for each application.

When I started doing this, I also decided to try Proxmox's new OCI compatibility, which seems to be working well so far, so I am removing all my Docker VMs and recreating the containers directly on my hypervisor.

reply

ig0r0

3 hours ago

 |
prev
 |
next

[–]

I am working on a small Pascal IDE for iOS.

It runs code locally (written in Swift), includes examples, and has a Turbo Pascal–style theme for max nostalgia.https://pascal.kulman.sk

reply

tmilard

3 hours ago

 |
parent
 |
next

[–]

My first language. I loved Pascal. I have done many university project in Pascal. Turbo Pascal felt so productive. Lovely.

PS : On your, slick landing page, please make an email imput so we can can know when to return. By the way my phone is ... android.

reply

ponyous

4 hours ago

 |
prev
 |
next

[–]

http://grandpacad.com
 - 3D Modeling tool intended for creating 3D prints. AI based. Allows for dimensionally accurate parts as well as organic shapes.

I massively improve it every month. Pretty proud of it.

reply

eximius

5 hours ago

 |
prev
 |
next

[–]

Nitor - a discord clone with a shared/federated Identity layer, but self-hosted "servers/guilds". Trust model is to trust the guild server (e.g., so private channels work as one would expect with moderation capabilities), but to enable E2E DMs and friend/presence systems via guild servers as relays. Rust, Iced, Iroh.

Glyphcraft - a Minecraft mod (imagine if Thaumcraft, Ars Nouveau, and Hex Casting were smashed together)

reply

NathanFlurry

12 hours ago

 |
prev
 |
next

[–]

WASM- & V8 isolate-based operating system that's (almost) POSIX-compliant, including its own network stack, VFS, process tree, etc.

Allows you to compile most C or Rust programs to run in it without modification. Also can run Claude Code, Codex, Pi, and OpenCode unmodified.Working on polishing, security, and documentation so I can share an in-depth deep dive on HN.https://github.com/rivet-dev/agent-os

reply

pdyc

7 hours ago

 |
prev
 |
next

[–]

Too many things

- Tool to auto create dashboards from csv/json files or rest api (https://EasyAnalytica.com)- Tool to preview, annotate and share html snippets (https://easyanalytica.com/tools/html-playground/)- Creating agent to edit files with smaller model(<1B) not yet released.-Prompt assember to create prompts/templates/context and easily share between ai to be released this week.

reply

justEgan

9 hours ago

 |
prev
 |
next

[–]

Working on Kernel, a GSAT vocab study app for Taiwanese students. A lot of exam prep still means paying cram schools for structure and linear repetition. We’re trying to turn that structure into software that knows what you’re about to forget and what to review next.

app store:https://apps.apple.com/tw/app/kernel-%E8%83%8C%E5%96%AE%E5%A...viral launch post that brought in ~1700 users in 2 days:https://www.threads.com/@sean_hsu_13/post/DW8nBzDjV8T?xmt=AQ...

reply

qualityslop

15 hours ago

 |
prev
 |
next

[–]

Building a map and text-based mobile game where you walk around and graffiti tag things (like Pokemon Go, except you are not looking at a map on your screen). The interface is text room names + descriptions, like an old school MUD, that update as you walk in different directions. They rooms are based partly on what is there in real life, although known points of interest are changed to fit a 'cyberpunk' theme.

The app is built in React Native (almost entirely with AI although I'm fairly particular about some of the features and methods it uses) with a Go backend. Map data comes from PMTiles.

reply

exitplanetary

4 hours ago

 |
prev
 |
next

[–]

Game Boy app to explore 4-bit synthesis and "modular" sequencing, smth similar to
https://roberthenke.com/technology/inside8032av.html
 but for Game Boy instead of Commodore PC

reply

eswat

8 hours ago

 |
prev
 |
next

[–]

I helped co-host a popup village in rural South Korea last week. Mix of co-working, co-living and local activities like trail running and bird watching.

Post-event feedback showed everyone loved it. But personally I think we could have done better organizing on the co-working side so people has a more predictable schedule to lock-in.So I’m planning what the next iteration of this event could look like if the co-working aspect was stronger. Especially in the area of everyone sharing their personal and/or professional intentions with each other. So they're more likely to accomplish those intentions with the help of other participants.https://protoville.xyz

reply

jnh-12

39 minutes ago

 |
prev
 |
next

[–]

Wow this is an unreal way to get some karma hahah

reply

ramon156

6 hours ago

 |
prev
 |
next

[–]

Working on m experimentall alternative to PHP's composer. Some projects took 2-3 mins to update with composer, only to fail at the end. Wanted to rework this, but the composer code is big and I honestly didn't feel like touching more PHP than I had to.

So I built my own package manager that's almost ready for alpha.https://github.com/van-sprundel/vif

reply

Curzel

3 hours ago

 |
prev
 |
next

[–]

Pixel Art Flight Sim

https://www.youtube.com/shorts/6jderLN3Aqk

reply

thisisharsh7

7 hours ago

 |
prev
 |
next

[–]

https://github.com/thisisharsh7/modron-discord-bot

I am managing a discord community with over 1k+ members I found some people would regularly put spam links or message on all the channels and this been repetitive it's just take time deleting them one by one or reposting them into the specific channel. So I build a discord bot that would make this lot easier it catches the spam message post them into actual channel and also delete spam links. It's open source and easy to setup.

reply

hirako2000

4 hours ago

 |
prev
 |
next

[–]

Fungi vision detection on the browser. Offline

https://fungi.renderlab.ccTrained to detect a few thousands species pretty accurately in near real time.Now working on expanding to far more species and exploring other CNN architectures.

reply

Joyrst

8 hours ago

 |
prev
 |
next

[–]

Greetings from Munich.
I’m building Joy, a CLI for product management. Your backlog is plain text in your git repo. joy add "fix the login bug", done.
AI works through the same workflow as humans: identities, capabilities, cost budgets, every action in the git log.
Still early. I use Joy to build Joy.
Joy docs:
https://joyint.com/en/joy/docs

Ecosystem and trust model:
https://joyint.com/en/docs/architecture

Feedback welcome.

reply

naitsa

5 hours ago

 |
prev
 |
next

[–]

A TUI written in gnuCOBOL to show and interact with the API of my cs student associations cursed member kiosk system. (Using curl, as I still want to live).

For said same association, templating and assembling a book of songs and other oddities in Typst for the associations 50th anniversary.Next project is figuring out what to do with my personal website!

reply

sponno

8 hours ago

 |
prev
 |
next

[–]

Hey Team, working on a project that makes it easier to track time on Mac.

- There's a desktop app tracking the title bar and time you spend in each app.
- You can use this 100% free, or sync this back tohttps://heygopher.aito match the time up with your active projects.
- if you use HeyGopher you can manage your time, team, projects, quotes and invoices.This pairs pretty well with my normal projecthttps://goodsign.iowhich is a Docusign alternative that is pay as you go. No subscription.

reply

solid_fuel

8 hours ago

 |
prev
 |
next

[–]

I've been building an HLS streaming engine with Elixir. It takes care of asset segmentation, transcoding, and streaming. It supports regular VOD playout, as well as live streaming by dynamically building HLS playlists from a variety of sources, including transcoded VOD assets and other HLS livestreams. It has a basic scheduling system and I'm integrating a lua engine to allow dynamic scheduling using user-provided scripts.

I'm hoping to continue extending it until it can act as a full internet TV delivery stack like Pluto or Roku TV. It still needs to be behind a CDN for efficient delivery but basically any CDN would work.

reply

philajan

12 hours ago

 |
prev
 |
next

[–]

I’m getting ready for the first release of a story time app my wife and I have been using for reading to our son.

The scope creeped to book discovery and ebook reading with OpenLibrary from just tracking and personal library recommendations.But we have been able to incorporate new books into the story time rotation so I’m convinced it’s worth it.It’s definitely been fun experiencing the range of quality for kids books in the internet archive.I’m aiming for a May 1.0 release on iOS and Android.

reply

tanin

7 hours ago

 |
prev
 |
next

[–]

I've recently found the best way to find an apartment to rent in Bangkok. It's the Facebook Groups. Tons of owners post their listings there.

So, I've built a scraper that scrapes posts from Facebook Groups and made those posts filterable/sortable.Now I'm looking to launch the same thing for US cities. Their Facebook Groups have tons of posts around subleasing/looking for accommodations.If you are interested, here's the site for Bangkok:https://bangkokprop.com

reply

icc97

34 minutes ago

 |
prev
 |
next

[–]

https://ianchanning.com/safer-ralph/

Ralph loop in a docker container, bullshit removed.Anti-slop, using AI to try to make it as simple as possible.

reply

egeozcan

8 hours ago

 |
prev
 |
next

[–]

I made Claude build me a web app to come up with anagrams:
https://github.com/egeozcan/anagramci

I'm now having immense fun trying to come up with anagrams to whole sentences in Turkish.I guess you could even automate finding anagrams (there are even web sites which allow you to do so), but Turkish agglutination makes it so much fun, and you can make really creative ones manually.Once upon a time I even had made a tumblr to share what I found:https://sacmanagram.tumblr.com/(also Turkish).

reply

dhuan_

12 hours ago

 |
prev
 |
next

[–]

I have been working on two opensource tools:

https://dhuan.github.io/mock/latest/examples.html^Command line utility that lets you build APIs with just one command.https://github.com/dhuan/dop^JSON/YAML manipulation with AWK style approach.

reply

BSTRhino

10 hours ago

 |
prev
 |
next

[–]

https://easel.games

For the past 4 years I've been building a programming language reimagined specifically for games. It has automatic multiplayer, but also things like state, components, concurrent behaviours and reactive user interfaces baked into the language.

reply

mtabini

12 hours ago

 |
prev
 |
next

[–]

https://www.crowdsupply.com/t76-org/dr-pd

Dr. PD is an open-source USB-C Power Delivery analyzer and programmable sink. It can sit inline between a USB-PD source and sink to show you the communication between them, or connect directly to a source and emulate a sink so you can characterize chargers and power supplies.The goal of the project is to make serious USB-PD analysis more accessible. The hardware, firmware, and host software are all open source. The control software runs locally in Chrome or Edge with no drivers or installation required, and the platform also provides Python, JavaScript, SCPI, and USBTMC interfaces for automation.(Sorry that I don't have a link to the GH repo yet, but you can follow the project onhttps://hackaday.io/project/205495-dr-pd. Also, if you read this far, I'm looking for a few beta testers. Reach out if you're interested!)

reply

datapond

6 hours ago

 |
prev
 |
next

[–]

I am building the perma-lib on the topic of ethics and sustainable practices: Ꭰ-Library

Pronounce A-Library "The Unicode character for the Cherokee letter 'A' (Ꭰ) is U+13A0"Launching a kick-starter for it in the coming weeks. Hoping to make a difference for the next few generations for a better world and education.https://dsafe.usandhttps://datapond.earth

reply

didgetmaster

11 hours ago

 |
prev
 |
next

[–]

Creating interactive pivot tables from large relational tables.

Many people know that a handy data analysis feature in Excel is to create a pivot table from a spreadsheet. But spreadsheets are limited to just a million rows. You can get around this limit by jumping through a bunch of hoops.My system lets you easily create tables with thousands of columns and hundreds of millions of rows. (Just drop a CSV, Json, or other file on a window to create a table.)Now you can create a pivot table from it with just a few clicks of the mouse. It is fast (I created a pivot table against an 8.5 million row table of Chicago crime data in less than a second.)The resulting pivot table is interactive. Each cell (row/column intersection) has all the row keys mapped to it. Double-click on any cell and it will instantly show you all the rows in the original table that were used to calculate the cell. You can then analyze those rows further.It also works well against much larger tables. I have tested it out against 25M, 50M, 100M, and 200M+ row tables.

reply

misir

11 hours ago

 |
parent
 |
next

[–]

How are you planning to sell it given the market dominance of Excel? The people that would be most willing to pay for spreadsheets are also the people who are already paying for Excel.

Not trying to discourage you, I am curious as to see how you are planning to enter the market as that was something I couldn’t answer when considering working on spreadsheet tools of various kinds or even an excel alternative.

reply

didgetmaster

10 hours ago

 |
root
 |
parent
 |
next

[–]

If your dataset is small enough to fit in an Excel spreadsheet, then you probably are not looking for an alternative.

But if your dataset has millions of rows and you need something quick to help you slice and dice the data in a variety of ways to try and find valuable insights in it to drive business decisions; then maybe you are looking for something better.BTW: creating pivot tables is just one of dozens of things my system can do. I am currently trying to figure out which features will attract the most customers.

reply

craigmccaskill

10 hours ago

 |
prev
 |
next

[–]

Outside of the day job (PM at an enterprise SaaS company), I've been building an AI-native CLI for Todoist [1]. Started to solve a personal problem, automating action item extraction from my Obsidian notes, but it's become something bigger. The CLI treats both humans and AI agents as first-class users: TTY-aware output, a schema command for agent discovery, idempotent operations, that kind of thing.

It's been a great excuse to get back to my roots as an engineer and lean into some of the newnew with Claude Code. Learning a ton, having a blast, and also enabling being (marginally) more productive with my actual work day to day.[1]https://github.com/craigmccaskill/todoist-cli/

reply

cgopalan

7 hours ago

 |
prev
 |
next

[–]

For occasions like birthdays or Christmas where people want to give you gifts, I have always wanted to ask them to make donations to charities of my choosing instead. So I built an app to enable this:
https://apps.apple.com/ca/app/donate-your-gift/id6760786102

It is very simple but I didn't find anything quite singly-focused like it, so I built it just to scratch my own itch.

reply

pacifi30

13 hours ago

 |
prev
 |
next

[–]

I am working on making grocery online shopping less overwhelming and more like a rolling list, you keep adding items as you see them (missing) in your household and it silently records it at the backend. When you are ready to pick up order, you push to qfc cart via api (a button) and boom your grocery shopping is done. No need of making lists and then one by one putting them on the cart. It works with any QFC or Kroger store because to my disbelieve they actually have an open sku and cart api. Grateful to Kroger to be tech forward. Free to use , here is the link
https://www.ddisco.com/sonic/customer
 My wife is hooked on it as she had to take time in the week to sit down ask me what to order and then build the cart. Now it’s like just typing in what you need.

Next I am making the version for folks who do not make a list and just go with past orders , for them I am automating so the cart is made based on past orders like milk usually is ordered every 2 weeks.

reply

electrodyssey

4 hours ago

 |
prev
 |
next

[–]

I'm working on an open source SYZYGY carrier board powered by Zynq 7000 SOC. My goal is to create a simple yet usable platform for SDR experiments.
The hardware design is done with KiCad, and everything including the firmware is available publicly.

https://electrodyssey.net/nasr-m-syzygy-carrier-board.htmlhttps://github.com/electrodyssey/NASR-M

reply

yqiang

8 hours ago

 |
prev
 |
next

[–]

I'm working on a calorie & macro tracker called FitBee [1]. Tracking my food has been tremendously helpful in terms of improving my health, but it's always been a PITA. The focus of FitBee is food quality & speed. Tracking your food is something you have to do multiple times a day, so I tried to make it as frictionless as possible. The app is built 100% with Swift & SwiftUI.

[1]https://apps.apple.com/us/app/fitbee-calorie-macro-counter/i...

reply

lbreakjai

15 hours ago

 |
prev
 |
next

[–]

https://tessellate-digital.github.io/notion-agent-hive/

I'm not a fan of the TUI form factor for longer running, more ambitious features. Even with a classic "Add an endpoint, tweak the infra, consume in the frontend", plans get awkward to refine in markdown files, especially if everything lives in its own repo.I wanted something like Plannotator, that could also work for the execution, not just the planning, So I've been working on something that turns Notion into the memory and orchestration layer for agents.Underneath, it's a plan-implement-review loop, but you get a nice Notion page with a kanban board out of it. You can easily link your existing documentation, collaborate by sharing the page, annotate and comment to steer the planner, and you get versioning out of the box.Because Notion acts as the memory, you can just open the page after a long weekend and get your agent and yourself back into the full context. You can see what's been done, what's left, or what requires human input just by looking at the board. You can ask it to fetch the comments on the pull request you raised, and it'll fetch, validate the comments, give you a report, and update the plan/board if necessary.I've been using it exclusively for the last two weeks, I'm quite happy with it. It's been really fun to build the exact tool I wanted.

reply

davemo

11 hours ago

 |
prev
 |
next

[–]

I've got a bunch of irons in the fire at the moment, most leveraging or built with agentic coding tools; my harness of choice these days is pi+codex.

- An internal apps platform built with bun, pg-boss, and railway- A smart music setlist manager that downloads chord charts, creates spotify playlists, and automatically drafts emails with attachments and practice schedules- A recruiting intelligence platform called Spotter that I built in a weekend[0]- A voice-agent for a client in the banking sector, implementing deterministic workflows using openai realtime voice + finite state machines[1][0]https://www.youtube.com/watch?v=AOedMSddGDg[1]https://blog.davemo.com/posts/2026-02-14-deterministic-core-...

reply

fcarraldo

9 hours ago

 |
parent
 |
next

[–]

> A smart music setlist manager that downloads chord charts, creates spotify playlists, and automatically drafts emails with attachments and practice schedules

This sounds useful!

reply

caffeinejunk1e

4 hours ago

 |
prev
 |
next

[–]

Nothing fancy, building a local platform to rent/rent-out video games.

Coming from a place where buying games is very expensive, and gaming is an expensive hobby in general.Tried rotating games locally between friends and friends of friends, now scaling it up.

reply

dataviz1000

13 hours ago

 |
prev
 |
next

[–]

I've been working on proving that Claude Opus can be self-reflecting meaning that its attention and context are large enough that it is aware of its own instructions, aware of the task, and capable of writing its own instructions to optimize solving the task in recursive iterations. [0]

By tuning the agent, it is possible to create trading strategies [1] and reverse engineer websites in order to create optimized JSON APIs using the websites internal private APIs. [2]I'm having the hardest time communicating what is happening so next I'm going to try to explain it using data visualizations so people can visualize it in action.[0]https://github.com/adam-s/agent-tuning[1]https://github.com/adam-s/alphadidactic[2]https://github.com/adam-s/intercept?tab=readme-ov-file#how-i...

reply

Realman78

14 hours ago

 |
prev
 |
next

[–]

https://github.com/Realman78/Kiyeovo
 - I'm currently working towards the full release of my P2P dual-network mode messenger which is currently in beta. The reviews were overwhelmingly positive when I released the beta a week ago so that motivated me to try extra hard to make it pseudo-perfect upon full release

reply

mbgerring

8 hours ago

 |
prev
 |
next

[–]

While I look for a new job working on clean energy hardware, I’m re-habbing a weatherproof 7kWh battery I built for a Burning Man project last year.

I’m adding:- A control hub that reads data from the batteries and the solar controller- Remote and on-device UIs that allow a user to control all the hardware from one place- A LoRa transceiver that allows monitoring the battery and solar status from a distanceExploring all of this is fun — there’s a lot of DIY solar and battery hardware out there that needs to be able to sync and coordinate, but there’s not a great software solution for this.Hit me up if you want to hire me, or give me money to work on this :)

reply

defrost

8 hours ago

 |
parent
 |
next

[–]

FYI, if you haven't seen it:
https://www.solarbatterywarehouse.com.au/solar-battery-shop/...

reply

mbgerring

8 hours ago

 |
root
 |
parent
 |
next

[–]

fwiw I’m in the US. I have seen a lot of things like this! I have a lot of opinions on this form factor, where it works well, and where it doesn’t.

reply

defrost

8 hours ago

 |
root
 |
parent
 |
next

[–]

It's blessed and cursed by being no more or less than exactly what it is; minimal amount neccessary bundled together on a double axle light trailer - draggable anywhere you can get a horse float to, ready to go.

Butt ugly unless you're deeply into the tradie steel frame equivalent of the Concrete Brutalism aesthetic.

reply

paulorlando

15 hours ago

 |
prev
 |
next

[–]

I'm researching Luddite-style examples from around the world. That is, examples of when people rebel against new technology that they see as harming their livelihoods.

reply

dijit

15 hours ago

 |
parent
 |
next

[–]

Will you publish this anywhere?

I’m interested too, but don’t have amazing patience to dig into it.

reply

paulorlando

14 hours ago

 |
root
 |
parent
 |
next

[–]

Yes. I while back I posted an initial list (
https://docs.google.com/spreadsheets/d/1M_UjOPxpbKMYes5CcWRW...
) but have gone way beyond this now.

For me this is an example of when you become aware of something you see it all around.I'll writeup a fuller list and what I learned along the way.

reply

ashwinsundar

14 hours ago

 |
parent
 |
prev
 |
next

[–]

Have you discovered any unusual or unexpected type of resistances? What's the furthest back in history you've been able to find something like this?

reply

rullopat

6 hours ago

 |
prev
 |
next

[–]

I’m working on an ATS system that integrates LLMs for helping the recruiter in writing job descriptions, parsing CVs to Markdown, making summaries of CVs and suggest which ones match the best the job offers giving pluses and minus:
https://beehive-ats.com/

reply

sentinel1909

9 hours ago

 |
prev
 |
next

[–]

I'm building my take on a static site generator.

https://get-taxus-org.pages.devIt's inspired by Zola, but has better documentation and willhopefullybe more approachable when all is said and done. I'm trying to incorporate WebAssembly, with Yew, to give "islands" for high performance stuff you might want where WebAssembly makes sense. For example, I wrote search from the ground up, and built a search widget using Yew.You can also just write JavaScript if you want.It's a total work in progress, but I'm enjoying what I've built so far.

reply

ym705

13 hours ago

 |
prev
 |
next

[–]

A complete guide on how to travel or live by van in Japan. Additionally trying to turn my passion into a revenue by offering tourists custom handcrafted plans for them to travel.

This is a fun side project as I learn great with email communication, culture differences (as a dev)https://www.campinjapan.com/

reply

ksri

9 hours ago

 |
prev
 |
next

[–]

I am working on a way to edit google docs using markdown. Many tools exist to convert google docs to markdown and to import markdown to google docs - but none of them make in place edits.
The core logic is to convert the google docs to md. The user then edits the md. Then diff the markdown files, and apply the changes back to the source google docs. This way, features not represented in markdown do not get overwritten.

Lots of effort has gone into testing against real world docs. Its beta quality right now.https://github.com/think41/extrasuite

reply

amysox

8 hours ago

 |
prev
 |
next

[–]

Well, Electric Minds Reborn is now online:
https://electricminds.org

I will be continuing work on the new software that powers it, the Amsterdam Web Communities System.https://github.com/amysoxcolo/amsterdam(I tried to "launch" it with a Show HN post, but it sank without a trace. I may try again, after I get back from vacation...)

reply

pravj

5 hours ago

 |
prev
 |
next

[–]

Grit Garden:
https://grit.garden
 (
https://github.com/pravj/wordle-garden
)

Recently shipped this personal art project that turns daily Wordle attempts into gritty / struggle-filled stories, kinda similar to the emotional arc of the Wordle game play.You can upload your own Wordle game screenshot to generate one for yourself.In addition to completing what was once in the idea list, I got to learn about- Prompt fine-tuning: Models are sharp enough to complete Wordle games quicker than human average scores, so I had to dump that down and get the average down.- Karpathy’s Autoresearch: Experimented with auto-research for prompt fine-tuning, in addition to manual prompts.- Vision models: While leading labs have multimodal models with quality visual reasoning, the benchmarks are still quite different for a simple Wordle analysis (reading what letters were yellow/gray/green); I also noticed labs/companies with separate vision models but their APIs lag significantly compared to what’s possible in developer experience.- Video generation: For the last few days, I have been experimenting with automated video generation for the project's social handles. I'm still struggling with the right hooks that reduce the skip rates, but it's fun.---Additionally, working on an Apple Watch app similar to my Mac app on the same lines, [Plug That In](https://plugthat.in), i.e., notify before the device goes too low on battery, but with a twist.

reply

shreygineer

5 hours ago

 |
prev
 |
next

[–]

After going to a bunch of bachelor parties over the past few years, and planning a few myself - I built an AI-powered bachelor/bachelorette planning tool to help make it a lot easier then it actually is

Check it out athttps://bartyai.com

reply

sasipi247

13 hours ago

 |
prev
 |
next

[–]

I am working on a system built around the OpenAI Responses API WebSocket mode as performance is something that interests me.

Its like a microservices architecture with NATS JetStream coordinating stuff. I want to keep the worker core as clean as possible, just managing open sockets, threads and continuation.Document querying is something I am interested in also. This system allows me to pin a document to a socket as a subagent, which is then called upon.I have hit alot of slip ups along the way, such as infinite loops trying to call OpenAI API, etc ...Example usage:
10 documents on warm sockets on GPT 5.4 nano. Then the main thread can call out to those other sockets to query the documents in parallel. It allows alot of possibilities : cheaper models for cheaper tasks, input caching and lower latency.There is also a frontendAlot of information is in here, just thoughts, designs etc:https://github.com/SamSam12121212/ExplorerPRO/tree/main/docs

reply

kilroy123

16 hours ago

 |
prev
 |
next

[–]

I made a thing to watch YouTube like it's 2000s cable tv.

I'm working to make it better right now.https://channelsurfer.tv/

reply

freakynit

7 hours ago

 |
parent
 |
next

[–]

I love this site.

reply

kylestanfield

13 hours ago

 |
parent
 |
prev
 |
next

[–]

The weather channel music is awesome

reply

ciwrl

2 hours ago

 |
prev
 |
next

[–]

working on a social network for researchers and university students to find new papers :-).
https://andreaturchet.github.io/website/index.html
 -> papel

reply

epiccoleman

16 hours ago

 |
prev
 |
next

[–]

I've got a couple of different things going as per usual, but the one that I'm currently most excited about is Lotus Eater:

https://lotuseater.epiccoleman.com/It's a mostly vibe-coded fan site for jamtronica greats Lotus. I wrote/prompted a scraper to pull in setlist data from Nugs and have been having a lot of fun coming up with cool data analysis stuff to do with their sets.I've seen them 7 times (chump change compared to some fans) and was starting to get certain intuitions about like, "if I hear song X that probably means they won't play song Y." For example, one of my favorite Lotus tunes, It's All Clear To Me Now, seems to fulfill a similar "function" as another song - Did Fatt.It was pretty cool to see that intuition bear out in the data (they've only ever been played in the same show one time in over 900 total shows).I've got a bunch of other "data" features sitting in a PR in my Gitlab, need to get around to reviewing and testing it so I can push out the next update. Also have a few other ideas for it, although I think there's probably a point coming fairly soon where there's not really anything left to do.I posted it on the main Lotus fan group on Facebook. I have a grand total 8 users. I love those users.The site is nothing crazy, it will never make money or anything - but it's just been a ton of fun to have something cool to hack around on.

reply

iljah

5 hours ago

 |
prev
 |
next

[–]

Bare bones IM program inspired by bitmessage(.org):
https://github.com/iljah/p2pIM

Uses proof of work for spam protection. Consists of server and command line client written in python.

reply

climike

7 hours ago

 |
prev
 |
next

[–]

Working on testing and monitoring agent-readiness of CLIs with www.cliwatch.com, some interesting challenges in building test suites and analyzing data :)

reply

vxsz

13 hours ago

 |
prev
 |
next

[–]

Playing with an idea of a next-gen self-hosted media server software, with rust, svelte and all the goodies.

But at my current knowledge and practical work, its like giving a chimpanzee a nuclear reactor schematic.
But it's a passion project idea of mine, I really want it to become real one day. Personally, I feel like something much better can be made than current solutions.

reply

inslee1

10 hours ago

 |
parent
 |
next

[–]

Hilarious analogy

reply

devtanna

6 hours ago

 |
prev
 |
next

[–]

I struggled finding mock exams when I was studying for the Einburgerungstest in Germany so i built a super simple site to offer folks some mock exams to practice with
https://www.einburgerungstestpractice.com

reply

ghirni

9 hours ago

 |
prev
 |
next

[–]

Hello!
Not sure if this is you, but every year I either miss my kids’ summer camp deadline or scramble to grab whatever’s left . I figured there has to be a better way — so I’m building something that helps parents like us get reminders (and maybe even auto-book if this is possible) before camps fill up.

If you’ve been through this rodeo too, please provide your feedback — your feedback will help make next summer a lot less stressful for other parentshttps://neelcamp.com/

reply

dondii

8 hours ago

 |
prev
 |
next

[–]

I am working on a routine tracker app. I have been searching for an app where I could create programs, schedules and routines for various things that I consistently work on in a structured way (ex. workout program, music practice, language study, etc.). I haven't been able to find anything that I could use across my interests so I am building it myself. It's currently in the internal testing phase of the playstore and am working to get it out this month.

reply

diasks2

13 hours ago

 |
prev
 |
next

[–]

Cooperation Cube (
https://cooperationcube.com/
) — A strategic 4-player memory/semi-cooperative board game I designed, played on a rotating 3D cube. Just added a daily puzzle (
https://cooperationcube.com/daily
) you can play without signing up. Place sticks, complete patterns, and try to beat the day's challenge.

Live Kaiwa (https://livekaiwa.com/) — A real-time Japanese conversation assistant. It listens, transcribes, translates, and suggests responses so you can follow along in conversations you'd otherwise get lost in. I built it because I live in Japan and needed something for the situations where missing a nuance actually matters — PTA meetings, bank appointments, neighborhood councils.

reply

s_brady

12 hours ago

 |
prev
 |
next

[–]

A runtime for a long-lived LLM agent with ambient continuous self-perception, persistent memory, defined authority, domain-specific autonomy, and forensic accountability, all in a long ongoing relationship with a human. I call this type of system an Artificial Retainer, a non-human cross between a guide dog and someone like your accountant or lawyer. It is not designed to be your friend, but it could be a valuable colleague. Think of this as an attempt to build a trusted stable agent with a stable character that could last decades.

https://github.com/seamus-brady/springdrifthttps://arxiv.org/abs/2604.04660

reply

sroussey

10 hours ago

 |
prev
 |
next

[–]

Like an idiot, I wrote a workflow dev library from scratch. (
https://github.com/workglow-dev/workglow
). Each task has either static or dynamic input, output, and config json schemas. Which makes creating a UI for it a little easier.

And I do have a basic UI athttps://workglow.dev/(where you can run the workflow, though if you use AI models, the models will run in the browser -- if you want to run GGUF models, please signup for the desktop app waitlist).

reply

medbar

3 hours ago

 |
prev
 |
next

[–]

Adding a scheduler to my hobby kernel with the goal of a full shell coming soon, and an inference engine from scratch in C++. It's been fun.

reply

adonese

7 hours ago

 |
prev
 |
next

[–]

I (codex) made a plugin for stremio to stream my collection from real-debrid.
I tried existing plug-ins first and non was working. Just prompted chatgpt to refine my initial specs, and asked on another session to build that. And later used codex for the last mile. Nothing fancy though and nothing can be particularly useful to others but damn it was too useful to me and my wife.

reply

pistoriusp

5 hours ago

 |
prev
 |
next

[–]

https://agent-ci.dev
: Run GitHub Actions on your machine. Caching in ~0 ms. Pause on failure. Let your AI agent fix it and retry, without pushing!

reply

charliewallace

9 hours ago

 |
prev
 |
next

[–]

Check out
https://www.steampunkclock.com
 - a concept inspired by a drawing toy called a spirograph. I originally coded it in c# over 10 years ago, but was able to port to the web via mostly vibe coding, and even go 3D! Brass, copper, rusty steel, gears and more gears! Really Quite Prodigious my dear chap! Drag to rotate, with zoom etc. I used google antigravity mainly for this recent work. Hope you like it. from Charlie Wallace of Carlsbad CA.

reply

shoehorn-dev

13 hours ago

 |
prev
 |
next

[–]

We're still building
https://shoehorn.dev/
: an Intelligent Developer Platform (think Backstage, but opinionated and simple). With Shoehorn, you just run the thing.

"The irony of Backstage is that it was created to prevent teams from having to reinvent the wheel every time, building and maintaining their own developer portal. But that's exactly what everyone does with Backstage."We wanted something you configure,deploy,update. thats it.service catalog, GitHub crawler, K8s entity discovery via k8s-push-agent, Forge + molds (scaffolding/workflows, like Backstage templates), governance, scorecards, cloud provider resources, license management, event based notifications, team-context aware, API keys with scope auth alongside session RBAC. CLI and Terraform provider too.We're aiming to release Beta end of April.

reply

jwmcglynn

6 hours ago

 |
prev
 |
next

[–]

I’m working on my hobby project, a browser-grade SVG rendering library in C++20:
https://github.com/jwmcglynn/donner

I recently finished <text> and <filter> support, now I’m working on a GPU-accelerated rendering backend.

reply

westoncb

11 hours ago

 |
prev
 |
next

[–]

Taking on a 'slow' software project with the kind of attention to quality (inside and out) that I had pre-AI. It's a tool I'll use myself, LLM-related, but not any kind of radical idea; it's main value is in careful UX design/efficiency, engineering quality, and aesthetics.

I've been shooting for the moon with one experimental idea after another (like many others) testing out LLM capabilities as they develop, for at least 2yrs now.I'm still very excited about how these new tools are changing the nature of software development work, but it's easy to get into this frenetic mode with it, and I think the antidote is along the lines of 'slowing down'.

reply

nothrabannosir

9 hours ago

 |
prev
 |
next

[–]

I’ve started streaming programming on Twitch and YouTube live.

Used to do it for friends only, but been publishing publicly since recently and it’s fun.“Senior dev, junior attitude”https://youtube.com/@harlybarluyhttps://twitch.tv/harlybarluySpent 3h today adding a “system” filter to jq only to find out there are like seventeen PRs for this going back ten years. T_T I live but I don’t learn.

reply

wonger_

9 hours ago

 |
parent
 |
next

[–]

Any takeways from streaming? I hear it's eye-opening to look back at your workflows and bottlenecks. Like to see how long you take on certain things that you didn't realize were pain points. Not sure if you experienced that along with any other dev benefits, or if it's just purely fun.

reply

nothrabannosir

8 hours ago

 |
root
 |
parent
 |
next

[–]

My focus is on the educational and entertainment value, not really the progress or utility of the code I write. I originally started this as extended L&Ls for friends & fam who were just starting out programming, so they could see how I work through things.

My take away from that perspective is: be honest. IMO the best moments are me just failing. It's probably more fun and more instructive to see me struggle than to see me breeze through things.And it better be entertaining because I work on stuff absolutely nobody cares about anyway. XD Right now I'm writing a microformats2 -> RSS converter in JQ...Today was my first time on Twitch, which is way more social. Random people drop in and start talking to you. Very cool. Very different from youtube live, where it's only the people who already know you, IME.

reply

giis

10 hours ago

 |
prev
 |
next

[–]

https://neverbreak.ai
 that fixes failing CI and opens a PR with _proof_. Most "AI CI fix" tools read the error log and guess a patch. We actually reproduce the failure, fix it then re-run the test in a fresh environment to confirm it passes before opening the PR. Each PR includes a short GIF of the fix working. If the test doesn't actually pass, no PR gets opened. Works with C, Python, Go, Node.js, Java on GitHub Actions and GitLab CI. Currently working with few beta users.

reply

kami23

10 hours ago

 |
parent
 |
next

[–]

Hah! I made this at work, when I started getting Claude to record the replication and demonstration of the fix as gifs on PRs people finally started asking me about the cool things I was doing.

The reproduction has been one of the things I've been struggling with in regards to consistency of bringing up the right envs. At the moment I've been approaching it as a MCP server that holds a few tools to bring up specific versions or branches of my stack to then find where a bug was introduced, build that commit prove that it wasnt in the previous one, and then fix it and run the full stack again with the fix component, then run through our local integration tests.This is the stuff that makes me feel like I'm on steroids now, my whole dev debug process can be run with a few instructions, game changing.

reply

bryanhogan

10 hours ago

 |
prev
 |
next

[–]

DailySelfTrack app:
https://dailyselftrack.com/

DailySelfTrack is a customizable combination of habit tracker, health journal and diary.It should be as powerful as a spreadsheet for self-tracking, but the daily usability should be more on par with a habit tracker app.For example my use-case would be:- Journaling in a way that fits into what I need. (Gratitude, bullet point jounal)- Analysing my health and understand how things might relate to each other. (State of multiple health issues)- Support for moving closer towards achieving my goals. (Daily focus sessions, no-phone mornings, learning Korean)

reply

bryanhogan

10 hours ago

 |
parent
 |
next

[–]

And I've been updating parts of my website, updated the descriptions, /about and /now, as well as the tags for blog posts.

My website:https://bryanhogan.com/The repository:https://github.com/BryanHogan/bryanhoganIt's built with Astro. Uses markdown files for the blog. Just CSS, no Tailwind or other UI library. I recently switched to Sveltia as the CMS, and after a bit of custom CSS for fixing some issues it has it works well for writing on my phone!

reply

wenbin

11 hours ago

 |
prev
 |
next

[–]

I’m building CurateKit.com - a lightweight content curation tool.

I always have growing lists of short texts, facts, and links that I wanted to host on a standalone site rather than burying them in a notes app. The workflow is simple: a browser extension to clip links with remarks, which then feeds into a public-facing list.I’ve also added a "Substack-lite" feature. Instead of long-form writing, it lets you send simple roundup email digests (e.g., "Top 5 links this week") to opt-in subscribers.My personal blog (wenbin.org) is currently powered by the tool.CurateKit.com is in private beta while I'm fine-tuning a few things now, but I’m opening up invites to the waitlist over the next few days if anyone wants to give it a try.

reply

nullandvoid

13 hours ago

 |
prev
 |
next

[–]

Now ready to release
https://mealplannr.io
. The end game is no/low touch weekly meal plans sent directly to your inbox, with meals from the chefs you follow - with none of the hassle around planning the meals, shopping list etc (which I spend hours doing every week).

An important feature for me was improving the recipe discovery experience, you can build a cookbook from chefs you follow on socials (youtube for now), or import from any source (Web, or take pic of cookbook etc) - it then has tight / easy integration into recipe lists.Utilising GenAI to auto extract recipes, manage conversions, merge/categorise shopping lists etc - as-well as the actual recommendations engine.If anyone is interested in beta testing / wants to have a chat I'll look out for replies, or message mealplannr@tomyeoman.dev

reply

lprimak

12 hours ago

 |
prev
 |
next

[–]

Mirror Immich - macOS Photos exporter for Immich with full metadata:

https://flowlogix.com/mirror-immich.html

Apache Shiro PMC chair (trying to get financial support for the project)https://shiro.apache.orgJakarta EE Components:https://github.com/flowlogix/flowlogixand it's starter:https://start.flowlogix.comWorking on all of these for the last 15 years, looking for more exposure.

reply

ggcdn

9 hours ago

 |
prev
 |
next

[–]

A boring solution for a boring problem - Working with PDFs.

I've been making a browser-based PDF editor that runs on-device via Webassembly / PDFium. Many of the hard parts were done by the open source embedpdf project, and I've been adding my own custom tools on top of it.It does the usual annotation stuff — highlights, comments, stamps, etc. working on some more advanced stuff now - regex search/redact, measurements and takeoff tools for AEC industry.https://www.Draftpdf.com

reply

999900000999

13 hours ago

 |
prev
 |
next

[–]

Hoping to release a beat tape. I've given up on trying to create new apps to try and get VC money. I tried this, often with exploitive co founders who expected me to basically make Facebook, but BETTER in a month for 3% of their company which doesn't exist.

I also make small games with Godot.

reply

dustinlakin

9 hours ago

 |
prev
 |
next

[–]

Working on a rogue-like discord activity game (soon to be multiplayer) that connects to Cloudflare durable object web sockets.

It takes my favorite elements from games like:
WoW character min-max design and rotation
Diablo 2/POE for item and crafting inspiration
Slay the spire dungeon flow/fights.It is uses pixel art I commissioned a decade ago that I am looking to finish a game with.Looking for some early feedback!https://crux.lakin.dev/

reply

gabriel-uribe

8 hours ago

 |
prev
 |
next

[–]

The toolbox for anxiously attached people, like myself:
https://www.attachedapp.com

Most iOS/Android mental wellness apps are trying to be everything for everyone, ie general AI journaling or meditations.By niching down, we can build the best experience end-to-end for anyone that resonates with these particular emotional challenges.

reply

primaprashant

9 hours ago

 |
prev
 |
next

[–]

I've been using speech-to-text tools every day now especially for dictating detailed prompts to LLMs and coding agents. I personally use VoiceInk which is open-source.

I tried to look for what other solutions are available and I've collected all the best open-source ones in this awesome-style GitHub repo. Hope you find something that works for you!https://github.com/primaprashant/awesome-voice-typing

reply

pizzly

9 hours ago

 |
parent
 |
next

[–]

Will check out. I made a custom made dirty solution working for the coding agent we use. Speaking is much faster than typing but it takes mental effort to lay out your thoughts before speaking unlike typing.

reply

ChrisMarshallNY

13 hours ago

 |
prev
 |
next

[–]

I'm working on a version 2.0 of an app that's been out for a couple of years. I won't link it from here, because, unlike almost every other software company in the world, we are not interested in MOAR UZERZ. We provide a specific Service to a specific demographic, and they know how to find us, just fine.

This project brings in a lot of AI support. It's made amassivedifference. The original project took two years to finish (actually four, but we did a "back to the ol' drawing board reset).It looks like this may only take a couple more months. I've been working on it for two months, already, and have gotten a significant amount done. The things that will slow it down, will be the usual sand in the gears: team communication overhead. Could stretch things out, quite a bit.

reply

efromvt

13 hours ago

 |
prev
 |
next

[–]

Still working on my urban tree visualization
! Spent some time polishing the ingest pipeline to make it easier to add new cities, added a genus/species level view to aggregate across cities, and added in some basic imagery so I can see what species are. Thinking about adding in a end-user facing ingest pipeline so I can add some trees I like that I see on my walks. Probably need a performance pass to since I'm scaling up the volume quite a bit.
https://greenmtnboy.github.io/sf_tree_reporting

Posted in last thread when it was SF only:https://news.ycombinator.com/item?id=47303111#47304199

reply

treelover

7 hours ago

 |
prev
 |
next

[–]

A fun project I'm working on: Chipmunkify. You upload a song and it isolates the vocals to give you a 'chipmunk' version while keeping the instrumentals untouched.

Have fun trying it and let me know what you think!https://www.chipmunkify.com/

reply

mixedbit

5 hours ago

 |
prev
 |
next

[–]

I'm working on a sandbox for Linux terminal work with UX similar to Python virtualenv:
https://github.com/wrr/drop

reply

arrsingh

8 hours ago

 |
prev
 |
next

[–]

I believe soon a day will come when the agents will chat with each other to get things done. Agents running on different machines, behind firewalls, on phones, laptops, servers etc will all want to chat with each other.

So there is going to be a need for Instant Messaging for AI Agents - Launching soon.https://agent-socket.ai

reply

rodjaime1

12 hours ago

 |
prev
 |
next

[–]

I built an open dataset mapping the structural connections between Israel's tech/startup ecosystem and its military-intelligence apparatus.

The Israeli tech industry isn't a neutral commercial sector, it's a deliberate pipeline from intelligence units to billion-dollar companies. Wiz ($32B Google acquisition) was founded by four Unit 8200 veterans. SoftBank's Israel ops are run by a former Mossad director. CyberStarts, a $1.5B VC fund, openly recruits Unit 8200 graduates.https://mybr.github.io/spynationhttps://github.com/mybr/spynation

reply

martz

7 hours ago

 |
prev
 |
next

[–]

Building a website to list all destinations and schools around the world, focused on depth freediving, with various data points relevant to that sport.

If you do any freediving or apnea training, interested to hear what you think of the platform.https://freedivingbase.com/

reply

dev_l1x_be

2 hours ago

 |
prev
 |
next

[–]

A new SML runtime with effect based IO (no function colouring).

reply

cousin_it

14 hours ago

 |
prev
 |
next

[–]

I'm working on
https://suggestionboard.io
, a live polling/feedback/Q&A webapp that doesn't require an account. Just launched the first version, now looking at the market and making small improvements.

reply

NautilusWave

9 hours ago

 |
prev
 |
next

[–]

I've been vibe coding a cross platform desktop app targeting bird photographers, that uses photo metadata and vision ML models to generate an eBird checklist formatted CSV for importing. It can detect and classify many birds in a single photo as well as individual birds.

https://github.com/jkanethird/rackery

reply

_kush

14 hours ago

 |
prev
 |
next

[–]

I'm working on LookAway, a Mac app that reminds you to take breaks from the screen at the right moment instead of interrupting you at random.
https://lookaway.com

Right now I'm focused on the stats side. It already shows how much time you spend in each app, and I'm adding website tracking too, which should make the picture much more useful.I'm also working on better break timing for dictation. LookAway already delays a due break if you're in the middle of typing, so it does not interrupt at a bad time. Now I'm trying to extend that same behavior to dictation as well, which turns out to be a pretty interesting detection problem because it overlaps with some of the other context signals I already use.Most of the challenge is making it smarter without making it feel more intrusive.

reply

horizontech-dev

6 hours ago

 |
prev
 |
next

[–]

I was tired of setting up additional read replicas and Snowflake for our BI teams, I built an analytics database using S3 and DuckDB.

https://github.com/viggy28/streambed

reply

zzsshh

11 hours ago

 |
prev
 |
next

[–]

My wife and I have been working on a platform for close to year now, called The Influencer AI (
https://www.theinfluencer.ai
) that helps you generate a consistent AI person, and use them for images and talking video. We've been growing and polishing it based on user feedback since then. You can go from idea of a person in your head, to the finished video of her doing or saying anything you need, all on one platform, with the best ai models for each step leveraged for you.

reply

bobro

11 hours ago

 |
parent
 |
next

[–]

Can you explain some use cases you have in mind?

reply

dooskington

6 hours ago

 |
prev
 |
next

[–]

I built a local tool that uses ollama to transcribe my handwritten journal pages into obsidian pages.

I'm also just working on my game, Antorum Online. Made with Rust and Unity.https://antorum.online

reply

digdeep

13 hours ago

 |
prev
 |
next

[–]

A Minecraft competitor.

I'm leaning heavily on simulation, economics, towns with real economies, and interweaving progression systems. It's a custom engine. I finally have the foundation built, it's multiplayer ready, and it currently loads in under 200MB. The idea is to be hyper efficient to simulate multiple towns that grow by themselves and you can trade and interact with.https://www.youtube.com/watch?v=BeZ3O6F5FXUIt's a free-time project, but I will happily take investment and make it my full-time project. :) I have a game design-doc that I have built out, and I personally like it a lot. I believe in it's potential.

reply

zoenolan

6 hours ago

 |
prev
 |
next

[–]

https://github.com/cavedave/Manannan

Previously:https://news.ycombinator.com/item?id=47024184

reply

boricj

13 hours ago

 |
prev
 |
next

[–]

I'm working on ghidra-delinker-extension [1], a relocatable object file exporter for Ghidra. Or in other words, a delinker.

Delinking is the art of stripping program for parts, essentially. The tricky part is recovering and resynthesizing relocation spots through analysis. It is a punishingly hard technique to get right because it requires exacting precision to pull off, as mistakes will corrupt the resulting object files in ways that can be difficult to detect and grueling to debug. Still, I've managed to make it work on multiple architectures and object file formats; a user community built up through word of mouth and it's now actively used in several Windows video game decompilation projects.Recently I've experimented with Copilot and GPT-5.3 to implement support for multiple major features, like OMF object file format and DWARF debugging symbols generation. The results have been very promising, to the point where I can delegate the brunt of the work to it and stick to architecture design and code review. I've previously learned the hard way that the only way to keep this extension from imploding on itself was with an exhaustive regression test suite and it appears to guardrail the AI very effectively.Given that I work alone on this in my spare time, I have a finite amount of endurance and context and I was reaching the limits of what I could manage on my own. There's only so much esoterica about ISAs/object file formats/toolchains/platforms that can fit at once in one brain and some features (debugging symbols generation) were simply out of reach. Now, it seems that I can finally avoid burning out on this project, albeit at a fairly high rate of premium requests consumption.Interestingly enough, I've also experimented with local AI (mostly oss-gpt-20b) and it suffers from complete neural collapse when trying to work on this, probably because it's a genuinely difficult topic even for humans.[1]https://github.com/boricj/ghidra-delinker-extension

reply

Swalden123

11 hours ago

 |
prev
 |
next

[–]

I've been building SoberStack (
https://soberstack.app
). It's the first side project I've taken on in a few years.

It's a free sobriety app for any bad habits I built for myself. Most sobriety apps reset your counter to zero when you slip, but it uses a Github style contribution graph to show you how far you have come. I also use it to track urges, and store a toolbox that is a reminder if why I am quitting something and what I can do instead every time I have an urge.

reply

asim

15 hours ago

 |
prev
 |
next

[–]

Micro - apps without the ads, algorithms or tracking.
https://micro.mu

The business model is likely going to revolve around mcp and x402https://micro.mu/developers/

reply

chistev

12 hours ago

 |
parent
 |
next

[–]

Your reminder.dev has no contact email.

reply

asim

7 hours ago

 |
root
 |
parent
 |
next

[–]

Oh sorry it's a personal project. I wasnt expecting to receive emails. You can contact me at xxx

reply

chistev

6 hours ago

 |
root
 |
parent
 |
next

[–]

OK you can edit out your email if you don't want it shown, I've copied it. I'll email you shortly.

reply

asim

6 hours ago

 |
root
 |
parent
 |
next

[–]

Thank you

reply

chistev

5 hours ago

 |
root
 |
parent
 |
next

[–]

Sent. Email has my username in it.

reply

vedantanahata

1 hour ago

 |
prev
 |
next

[–]

hi, I am building
https://cashpylot.com
, an all-in-one platform for business finances, helping them manage clients, invoices, monitor budgets, track cashflows, expenses and their taxes.

reply

vedantanahata

1 hour ago

 |
prev
 |
next

[–]

hi, I am building
https://cashpylot.com
, an all-in-one platform for business finances, helping them manage clients, invoices, monitor budgets, track cashflows, expenses and taxes.

reply

ayushranjan99

7 hours ago

 |
prev
 |
next

[–]

I am building a coding agent like claude code. Lambda agent, getting to learn a lot like how to control your context window how to conserve tokens. Check it out here

https://GitHub.com/ayusrjn/lambda

reply

metanoia_

14 hours ago

 |
prev
 |
next

[–]

Writing. I publish one long form essay a month with two published thus far. The third one is in editing stages. An enjoyable experience moving from internal notes to outward expression.

https://www.metanoia-research.com/

reply

alprado50

12 hours ago

 |
prev
 |
next

[–]

Right now Im working on so many thigs, but none of them as interesting as the things that other people here do.

I manage a small store (https://amigurumis.com.mx) for my SO and im dropping Elementor (too expensive) to use only Gutenberg. Turns out that it is pretty good for simple sites.Im having some sucess developing new websites for people who cant afford it, or who never though about having one, so i created one for an accountant (https://contadoranual.com) using only WordPress.

reply

martin-adams

16 hours ago

 |
prev
 |
next

[–]

I’m working on Flowtelic. A workflow driven note-taking system that aims to get you thinking deeper, but also help you work on the most important thing next if you’re stuck. While not essential, it’ll be enhanced with a local first AI approach.

https://www.flowtelic.com

reply

Andys

9 hours ago

 |
prev
 |
next

[–]

Deploy to your own AWS account with minimal config!

- Any containerized app, uses Fargate (no Kubernetes)
 - Heroku-like CLI tool with instant console sessions
 - Set up SQL/Redis instantly with Heroku-like add-ons.
 - Autoscaling, preview apps, audit trail, release approvals.https://tapitalee.com

reply

decancode

7 hours ago

 |
prev
 |
next

[–]

https://www.github.com/neuvem/java2graph
 —- A semantic code graph for AI agents (for Java language)

The goal is to provide AI agents with deep understanding of the codebase and help them understand the context, not just text

reply

f3408fh

16 hours ago

 |
prev
 |
next

[–]

I built a MacOS-native app [1] to control Positive Grid Spark amps [2], without needing a phone.

Official app is mobile-only and clunky, and the workflow is awkward if you're sitting at a desk. Hardest part has been maintaining compatibility across amp models. Small protocol changes or optimizations I make for one amp can break another. That means I have to do a lot of manual testing before every release. So I'm trying to think of an emulation layer or test harness I can build to make my life easier. Happy to hear suggestions there.About ~50 people are using it so far, and main feedback has been that it's much faster and more reliable than the official app.[1]https://tonepilot.app[2]https://www.positivegrid.com/products/spark-2

reply

theturtletalks

8 hours ago

 |
prev
 |
next

[–]

I’m building an open source SaaS for every vertical. I’m targeting e-commerce, restaurants, gyms, hotels, grocery stores. I want to leverage these systems to build an interoperable marketplace for each vertical. I launched a Shopify alternative in December and the Toast one is almost ready. Gyms, Hotels, and Grocery stores ones are in the works.

reply

brokegrammer

11 hours ago

 |
prev
 |
next

[–]

I've been working on version 2 of ClaroHQ (
https://clarohq.com
), which is a time blocking app for freelancers. Instead of playing with Start/Stop timers, you log your work with 1-click time chips, generate a perfect PDF, and draft an email in 30 seconds.

I built it because I was sick of paying for complex invoicing tools that charged monthly fees for features I never used.Let me know if you want to try it out. I'll be happy to set you up with an account.

reply

PaulShomo

13 hours ago

 |
prev
 |
next

[–]

This morning published a design manifesto for the Co-Wiki — a wiki-based warm storage layer that sits between LLM context windows and vector DBs, designed for human-agent co-authorship. The architecture solves chat hell, RAG chunking failures, and the missing second brain infrastructure in one brutally simple design. I'm a long-time SW architect who moved to epistemology. I’m too busy to go back to building — the design is complete, documented, and open. First to ship owns the category.

https://gist.github.com/paulshomo/69cf99e3185fa7ad0f50fc0e38...

reply

jithinraj

11 hours ago

 |
prev
 |
next

[–]

Working on Originary, built around PEAC, an open protocol for signed interaction records.

The idea is to make agent, MCP, and API interactions verifiable across org boundaries instead of relying only on logs. Still early, but that’s the thing I’m most focused on right now.Originary:https://www.originary.xyzPEAC:https://github.com/peacprotocol/peac

reply

Easycoder

14 hours ago

 |
prev
 |
next

[–]

I'm working with Claude Code to create complete programming systems in languages other than English. Not just wrappers around an English syntax;these are based on an English original but are complete scripting languages in their own right, with documentation, tutorial and programmer's playground. Each variant has its own language pack and they share a common compiler and runtime. The best of all is they are extremely AI-friendly. I've started with Italian and I'm looking for collaborators to work on others. I'd like to do Polish and Bulgarian but any are possible. See
https://allspeak.ai
.

reply

sammacg

11 hours ago

 |
prev
 |
next

[–]

I'm working on my Pact app. A shared habit tracker. I need positive social pressure to stick to good habits. This helps me a lot.

You commit to a habit, invite your friends to join, and keep each other accountable.Little square for each day/week fills up depending on how many members of the Pact completed it. Streaks are dependent on everyone in the pact completing.https://apps.apple.com/us/app/pact-accountability/id67551314...

reply

rorytbyrne

14 hours ago

 |
prev
 |
next

[–]

Open Science Archive: open infrastructure for scientific databases, so that every field gets its own Protein Data Bank in 1-click.

Code:https://github.com/opensciencearchive/server.Website:https://opensciencearchive.org/Two demos:https://pockets.biohttps://lingual.bioI've got demos up and running (mirroring/extending PDB and GEO). Next I'm working on APIs with good AX, ML-friendly export, and an unified AI-driven UI that works for all scientific data types.

reply

unlimit

8 hours ago

 |
prev
 |
next

[–]

I have been prompting and building a pos[1] for fun. I have been improving it bit by bit. I will also admit that I have not looked at the code that AI tools have generated. I let AI test it and the AI also finds bugs and fixes it.

Its a fun project, all done using free tier.https://pos.unlimit.in

reply

throwawaygod

30 minutes ago

 |
parent
 |
next

[–]

Which service's free tier is so generous?

reply

ryanmcdonough

6 hours ago

 |
prev
 |
next

[–]

https://getminute.me

A privacy first transcription and analysis app for iOS and native Mac OS (latter this week)All AI runs on device, nothing ever leaves your device apart from syncing data via your iCloud.

reply

hawtads

7 hours ago

 |
prev
 |
next

[–]

We are working on making agentic ads and regulatory compliance scalable.

https://hawtads.comJust launched the blog toohttps://blog.hawtads.com/

reply

socketcluster

13 hours ago

 |
prev
 |
next

[–]

The most versatile and secure no-code backend platform ever created for building complex web apps. The original goal was to bring junior devs on par with top senior devs in terms of application architecture. I've been trying to create a dev experience that avoids any kind of abstract technical hurdles and makes everything as light, declarative and scalable as possible. Pivoted for AI; which is even better at using it than a junior dev. I started building this project piece by piece 15 years ago.

https://saasufy.com/

reply

washedup

9 hours ago

 |
prev
 |
next

[–]

Been working on a paper that's my attempt to add a meaningful update to macroeconomic theory, specifically around the effects of high-entropy outputs (waste, heat, harmful byproducts) as diminishing GDP and general population health. Working on some studies backed up with data to support. If anyone here is interested in economic theory, I could use your feedback.

reply

gbin

13 hours ago

 |
prev
 |
next

[–]

Still improving copper-rs!
https://github.com/copper-project/copper-rs
 a rust first robotics runtime and operating system. It allows you to target your algorithms for both a traditional OS and embedded targets with a perfectly deterministic replay. Our users are from all over the autonomous systems spectrum: AMRs, humanoids, drones, self driving... If you are a rust enthusiast wanting to test the robotics waters or a robotics rust curious. Come and join us!

reply

zuzuleinen

4 hours ago

 |
prev
 |
next

[–]

Building a project to teach myself Go Concurrency using spaced repetition.

An Android mobile app to send e-mails to myself(capture mechanism from GTD)

reply

colinator

9 hours ago

 |
prev
 |
next

[–]

I'm connecting LLMs directly to robots, to see how well they can perform robot things by directly controlling motors and sampling the camera/sensors. Initial results are encouraging!

https://colinator.github.io/Ariel/post1.htmlI just got a bigger robot, further results forthcoming!

reply

pastel8739

9 hours ago

 |
parent
 |
next

[–]

Isn’t this showing that LLMs can write code to control robots, not that they can actually directly control them? If I’m reading the hand tracking example right, the LLM is not actually in the control loop. Is this wrong?

reply

colinator

9 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah, the mechanism by which the LLMs control the robot is by writing code. I suppose they could also issue direct joint sequences, but I thought that they're so good at writing code already, might as well do that. So if they 'wanted' to they could write code with an explicit joint sequence they calculate in-context. That one seems more difficult.

So they can go 'slow', by taking a camera image, controlling the robot, repeating. Or they can write code that runs closer to the robot in a loop, either way. I thought the latter was somehow more impressive, and that's what you see in the hand-tracking example.

reply

ElFitz

15 hours ago

 |
prev
 |
next

[–]

Mostly playing around with AI agents session logs.

Lately I’ve been having LLMs implement multiple analysis methods on my session transcripts, trying to surface and identify patterns.It’s been interesting. It took quite a bit of nudging, but Claude applied techniques I didn’t expect, from disciplines I wouldn’t have thought of.If it works out, I’d like to turn into a sort of daemon that locally runs analysis on the sessions of users, with a privacy-preserving approach (think federated machine learning).Would be interesting to see what patterns appear at scale, and have those confirmed or rebutted across thousands of transcripts corpuses. No reason Anthropic & OpenAI should be the only ones to benefit from that; those are our interactions after all.

reply

siscia

15 hours ago

 |
parent
 |
next

[–]

> Claude applied techniques I didn’t expect, from disciplines I wouldn’t have thought of

Do you have any example?

reply

ElFitz

4 hours ago

 |
root
 |
parent
 |
next

[–]

Smith-Waterman Sequence Alignment applied to tool calls. Tool calls are encoded as single characters (Read=R, E=Edit, B=Bash,…), with interesting differences between "successful" and "struggling" sessions.

Another one is "Lag Sequential Analysis", applied to human-agent interactions.I was only thinking of corpus analysis, but I guess that’s what you get when you give AI a web search tool and keep pushing it to explore more domains to borrow techniques and methods from.

reply

batch12

9 hours ago

 |
prev
 |
next

[–]

Planted a few fruit trees, some strawberries, and vegetables. Every time I water them, I think about automated irrigation.

reply

Felger

14 hours ago

 |
prev
 |
next

[–]

Arrr. Here's the monthly dose of low self-esteem for all those who struggle to get anything worthwhile done. Currently working on figuring how you get motivated and competent enough as I browse various link from this thread.

reply

djeastm

13 hours ago

 |
parent
 |
next

[–]

My suggestion is to just post something, anything, in progress if you can. We're all of us makers here and know the same struggles.

reply

saranshrana

4 hours ago

 |
prev
 |
next

[–]

Runtime Security for AI Agents and Co-Pilots

Try it here -https://burrow.run/

reply

lrvick

11 hours ago

 |
prev
 |
next

[–]

My team and I have been building stagex, a FOSS multi-party reviewed/built/signed, deterministic, full source bootstrapped, llvm native, container native, musl/mimalloc native linux distribution to build all the things.

https://stagex.toolsBased on top of that is Caution, the first FOSS general purpose verifiable compute platform launching next week in private beta.https://caution.co

reply

ekrapivin

15 hours ago

 |
prev
 |
next

[–]

I've spent several years developing an ad-free website with a few dozen solitaire/puzzle games:

https://inSolitaire.comI am currently rewriting+testing the engine and about to add ~400 games to my platform in a few weeks.

reply

wiireed

13 hours ago

 |
prev
 |
next

[–]

Last week my friend and I launched
https://farmdoor.co.nz

A job board for travellers and backpackers on working holiday visas in New Zealand.Most NZ job sites are built for employers. Farmdoor aims to flip that: workers can leave reviews of farms and employers, so the next person knows what they're signing up for before they show up somewhere remote.Built it after seeing firsthand how hard it is for backpackers to find reliable work and how little recourse they have when an employer turns out to be dodgy.

reply

nzoschke

14 hours ago

 |
prev
 |
next

[–]

Working on
https://housecat.com
, AI productivity tools for non technical teams.

https://housecat.com/docs/editorial/why-housecatThe ideas I’m thinking about is: what’s old is new.We’re seeing a massive influx of people writing software and administering servers for the first time ever. But so many people are jumping (or being pushed) into the deep end without basic training.Lots of opportunities for us older admin folks to build, teach and help all the new folks.

reply

memset

11 hours ago

 |
prev
 |
next

[–]

Side project to generate good-looking programs for recitals and concerts:
https://concert-programs.projects.jaygoel.com

For people who use Fora for travel, a tool that uses AI to create google calendar events from travel itineraries:https://itinerary.projects.jaygoel.com

reply

eaglehead

10 hours ago

 |
prev
 |
next

[–]

I have been working on using openclaw and Claude managed agents to help me run a one-person startup. As a repeat founder, I know a lot of tasks that are very well suited for agentic systems.

so far it has been an interesting journey and I have had some success but the whole process has led me to write a lot of software around my own process so that I can scale it.Might turn that into a product itself.

reply

jbonatakis

14 hours ago

 |
prev
 |
next

[–]

https://pginbox.dev

Repo:https://github.com/jbonatakis/pginboxMakes reading/searching the Postgres mailing lists easier.I’m polling a Fastmail inbox to nearly instantly receive and ingest messages. Anyone can browse without an account, but registered users can follow threads to be notified of new messages, threads in which your registered email is found are auto-followed, and there are some QOL settings.Search is pretty naive right now (keyword on subjects) but improved search is the next big thing on my list.

reply

Velc

10 hours ago

 |
prev
 |
next

[–]

I'm building inspection software for various industries that are stuck with terrible pre-2010 software, or just pen and paper. Using AI where it makes sense, but not forcing it on users. Already have 5 users trialing the software, they're helping shape the product.

Very fun project, launching this week publicly in the app store.https://anyinspect.ai

reply

yboris

12 hours ago

 |
prev
 |
next

[–]

My 8-year-old video browser software
Video Hub App
 - shows thumbnails from video as you hover with your mouse. Working on adding minor improvements before I finally get to the (optional) facial recognition "search by face similarity" feature.

https://github.com/whyboris/Video-Hub-Apphttps://videohubapp.com/

reply

andrewjneumann

8 hours ago

 |
prev
 |
next

[–]

A premium podcast listening experience… with no ads, no tracking, and no subscription required. Full support for iOS/CarPlay/WatchOS including Podcast 2.0 features. Open source:
https://yourpods.app/

reply

KingNoosh

9 hours ago

 |
prev
 |
next

[–]

One of my current clients is an EV charging firm and realised the tech side is such a mess, though of doing a Parse/Firebase/Stripe for EV chargers and networks.

So people don't need to lose braincells over this till it actually matters.https://ampr.dev/

reply

AdeGneus

10 hours ago

 |
prev
 |
next

[–]

Building Ori, an open-source agentic IoT runtime with a Physical Actuation Trust framework.

The core idea: every AI agent acting in the physical world must formally earn the authority to act, tier by tier, from informational alerts through to safety-critical relay control. Runs offline on a $55 Pi.First deployments are underway in Lagos.Happy to answer questions about the safety architecture or the offline reasoning approach.

reply

mceoin

12 hours ago

 |
prev
 |
next

[–]

More a practice than a project, but I'm working on using voice as much as possible to interact with computers. This started with mapping the Tap Assistance on my phone to ChatGPT voice, then vibe coding better voice transcription for my computer, then shifting increasing amounts of work to Claude Remote control, etc.

This is less of a latency/efficiency thing and more about disconnecting the eyes from a screen and fingers from a keyboard. The upside is more walking, flow and creativity.

reply

rexma

12 hours ago

 |
prev
 |
next

[–]

A free and open source language learning app in the form of a pixel-art game - it currently supports 6 languages. It's something I feel Duolingo should've been but I've seen them drift further and further from the point. The app is fully offline and there's no accounts or signup

Rn it's on the appstore:https://apps.apple.com/us/app/lexaway/id6761870125

reply

cmcollier

16 hours ago

 |
prev
 |
next

[–]

https://orangewords.com

Orange Words. My hobby project, a hacker news search system. It was initially created by hand and now I use AI augmented development. It's a good low risk environment for experimenting.

reply

krzysiek

14 hours ago

 |
prev
 |
next

[–]

A service summarising and simplifying EU laws, resolutiins, decisions and so on:
https://euforya.eu/

One thing I find especially intriguing is how LLMs can help deal with desinformation:- I experiment with deterministic settings of local LLMs for the document summary so that sharing a prompt would prove that the output was not tempered with (no desinformation on the service side)- I add outputs of several LLMs (from the US, the EU and from China) for the "broader context" section so users could compare the output (no desiformation on the provider and model side)

reply

davidsojevic

12 hours ago

 |
prev
 |
next

[–]

The most recent project I’ve been working through has been a tool for JSON query evaluation and debugging [0] inspired by how easy regex101 is to use.

I couldn’t find any that were as nice or as powerful to use for writing JSONPath queries, so instead of spending an hour crafting and testing them manually, I spent >40 hours building this tool to save myself half an hour.[0]:https://jsonpath101.com/

reply

jerrygoyal

8 hours ago

 |
prev
 |
next

[–]

I built a lightweight (<1mb) chrome extension (with over 600,000 downloads) that lets you chat with page, draft emails and messages, fix grammar, translate, summarize page, etc.. You can use models from OpenAl, Google, and Anthropic.

Yes, you can use your own API key as well.

reply

psubocz

13 hours ago

 |
prev
 |
next

[–]

Working on
https://delo.so
 - a new offline first, no subscriptions, no cloud, CAD for makers. I'm very close to the public beta release. Should happen late April/early May.

https://github.com/NetwindHQ/gha-outrunner- github actions local, ephemeral runner which runs jobs in docker container, tart vm org kvm (depending on the host/guest)

reply

skandinaff

23 minutes ago

 |
parent
 |
next

[–]

I've been dreaming of exiting big CAD cloud prison for some time now, really looking forward to see your product!

reply

hirako2000

5 hours ago

 |
prev
 |
next

[–]

Rebuilding iNaturalist with a more immersive experience. With broader species detection with lightweight models running on edge.

reply

ptcodes

10 hours ago

 |
prev
 |
next

[–]

I'm building a Linux desktop app that tracks laptop battery health, logs per-minute stats to a local SQLite database, and visualizes capacity trends and degradation over time. It was fun to learn about laptop batteries.

https://github.com/ptcodes/BatteryScope

reply

stldev

11 hours ago

 |
prev
 |
next

[–]

I've taken time off work to follow something I've always dreamed of doing. So I'm building Cella, A cross-platform, 3D space MMO game set in a procedural, animated universe with fully composable ships & structures built using functional cells.

https://cellagame.com/I'm looking for artists to help fulfill the vision.

reply

melenaboija

9 hours ago

 |
prev
 |
next

[–]

An open pricing framework for quant finance based on QuantLib:

https://app.quantra.io/https://github.com/joseprupi/quantraserver

reply

rpatni

11 hours ago

 |
prev
 |
next

[–]

I've been building grateful - a social gratitude app.

https://grateful.soYou write a short entry, keep it private or share it to a circle. A circle is a small private group of your own making — family, close friends, whoever you'd actually want to hear from.Basically private instagram without all of the strangers and ads. What social media used to be.

reply

1zael

10 hours ago

 |
prev
 |
next

[–]

https://locunity.com/

We use AI to monitor hundreds of local government commissions and give real-time intelligence to B2B, residents, and governments. If you're a business trying to track what's happening in local gov for your policy, sales, or lobbying team, I'd love to chat.

reply

davidcann

14 hours ago

 |
prev
 |
next

[–]

I’m working on Buildermark (open source, local) that calculates how much of your code is written with coding agents.

It scans your claude and codex history to find edits and matches those to git commits (even if the code was auto-formatted).https://buildermark.dev/You can browse all 364 prompts that wrote 94% of the code here:https://demo.buildermark.dev/projects/u020uhEFtuWwPei6z6nbN

reply

agjmills

16 hours ago

 |
prev
 |
next

[–]

Trove - a really simple web app where I can shove some files without having to really think about configuring anything

https://agjmills.github.io/trove/Go, docker, bit of alpine js

reply

npilk

6 hours ago

 |
prev
 |
next

[–]

Trying to make it easier for anyone to publish a website for free, even with no technical know-how:
https://weejur.com

reply

aledevv

13 hours ago

 |
prev
 |
next

[–]

I'm working on a AI RAG (retrieval augmented generation) system:
https://longtermemory.com

It's a tool that use QDrant, a vectorial db, to embedding the texts chunks: LLM api is questioned to generate the Q&A pairs from a chunked texts.Each chunk is then embedded and stored in the vectorial db to facilitate the Q&A generation, thanks to better context informations.This tool helping people to study everything thanks to even Spaced Repetition algorithm.

reply

nevster

11 hours ago

 |
prev
 |
next

[–]

https://app.auctionsieve.com/

I've converted my 23 year old Java desktop app to a website.It's an app to make searching eBay an actual joy. Perform a search, then highlight text to trash or group that term. Then perform the search again tomorrow and it will hide all the stuff you've already seen.

reply

mikenikles

10 hours ago

 |
prev
 |
next

[–]

Month 4 of building a data management platform called Seaquel [1].

Months 1-3 were about building a desktop client. Now I'm working on a server binary customers can optionally self-host to share dashboards publicly and run workflow automations.[1]https://seaquel.app/

reply

philippemnoel

14 hours ago

 |
prev
 |
next

[–]

https://github.com/paradedb/paradedb
 -- Full-text & vector search natively in Postgres

reply

pqdbr

14 hours ago

 |
parent
 |
next

[–]

that looks really cool. do you plan on building a docker image like pgvector does?

reply

SkaBunkel

13 hours ago

 |
prev
 |
next

[–]

Been rolling around from project to project this past month.

A SSO application in rust(not public)A DNS for a dream project of mine which is a hosting provider company like digital ocean but in Scandinavia(not public).A code hosting site for said hosting company called bofink(not public)Ansible playbooks for applying database patches that can resume and create schemas etc, based on an internal tool from a former job. This is public and available on my github if anyone wants to look at itnot linking it because there are way cooler projects here.

reply

s3p

11 hours ago

 |
prev
 |
next

[–]

Working on recreating Google engineer Ken Shirriff's work on chargers. His article "A dozen chargers in the lab" is what I'm trying to replicate, but with modern USB C chargers. Feel free to take a look:

https://sull1van.com/a-dozen-chargers-in-the-lab

reply

msephton

8 hours ago

 |
prev
 |
next

[–]

I'm just wrapping up a macOS app to do perspective correction of images. It has a bunch of unique features, easy user interface along the lines of Numbers/Pages/Keynote, and a download size of only 1.1 MB.

reply

jballanc

11 hours ago

 |
prev
 |
next

[–]

I've been working on an ML model capable of robust continuous learning, resistant to catastrophic forgetting without relying on replay, an external memory system, or unbounded parameter growth. Last week I confirmed the first non-toy, 580M parameter version soundly beat LoRA, EWC, and full fine tuning. This week I'm scaling up to 4.4B parameters...

reply

deivid

13 hours ago

 |
prev
 |
next

[–]

Working (again) on an offline translator for Android:
https://github.com/davidventura/offline-translator

This week I added TTS support, which needed multiple inference pipelines, it was not easy to find models for 50 languages!At this point, it mostly works as a crude implementation of Google translate+Google lens, but 100% offline and 100% Google-free

reply

scotty79

4 hours ago

 |
parent
 |
next

[–]

OmniVoice has wide language support.

reply

sminchev

16 hours ago

 |
prev
 |
next

[–]

https://howareu.app/

Real challenge to keep it working 24/7. The Android OS, and its modifications are really aggressive, trying to kill everything that runs more than they think it is allowed to.I made a whole article about it. I hope it will help others:https://dev.to/stoyan_minchev/i-spent-several-months-buildin...

reply

hunterpayne

4 hours ago

 |
prev
 |
next

[–]

I'm writing a relational compiler. It makes Spark jobs run up to 10x faster on the same hardware.

reply

ojr

12 hours ago

 |
prev
 |
next

[–]

They say programming is dead...
I built an AI Streamer platform that responds to a twitch chat

https://slidebits.com/ai-streamerNot a trivial thing to vibe code without any domain expertise but this project took me under 2 weeks with a AI coding agent harness I built myself. I use Gemini 3 Flash as my main driver as well.

reply

felixding

12 hours ago

 |
prev
 |
next

[–]

https://aquablue.app
 - Simple, Reliable AI Automation

https://kintoun.ai- Translate Word, Excel and PowerPoint documents with layout and formatting intact.https://ricatutor.com- Your AI Language Tutor for YouTube

reply

ZaikoPewPew

5 hours ago

 |
prev
 |
next

[–]

I built a database of 2,345 failed startups —
causes of death, funding raised, years active.
$209B burned in total.

Still deciding whether to ship it as a product.
gauging interest here first.https://memory-whitelist-page.vercel.app/

reply

pdappollonio

11 hours ago

 |
prev
 |
next

[–]

I just released
https://github.com/patrickdappollonio/dux

Wanted to have a way to coordinate multiple agents on Linux either via SSH or locally and figured out why not give it a shot?The result is a pretty cool tool, inspired by similar solutions that after trying them most fell short.

reply

freakynit

8 hours ago

 |
prev
 |
next

[–]

with the advent of modern LLM's, I was building a lot of small, shareable, static sites.

Games, utilities, calcultors (for whatever niche), and anything else where I wanted it accessible for me from anywhere, plus the poeple I want to share with (publicly or privately)..So, I built this:https://pagey.siteSimple static site hosting. Upload html or a zip-containing-html along with other needed files, and it gets hosted on a subdomain with full https. Optionally, password protect it, or generate shareable links. Also, detailed analytics and other stuff.Im already hosting 16 small sites on it.. loving it.

reply

kukkeliskuu

14 hours ago

 |
prev
 |
next

[–]

Recently I have been doing a modern Lotus Agenda clone as a native iOS app. I have been implementing a custom CRM using that platform.

Also, Arch Ascent, which is a tool for evolveing microservice-heavy architectures.https://github.com/mikko-ahonen/arch-ascent/blob/main/doc/de...

reply

AznHisoka

10 hours ago

 |
prev
 |
next

[–]

I am working on building Bloomberry, an alternative to Builtwith for finding companies thar use a specific SaaS product.

Example: Companies that use Github:https://bloomberry.com/data/github-enterprise/

reply

big_big_data

10 hours ago

 |
parent
 |
next

[–]

how does this work ? What ways are there to know about b2b contracts ?

reply

ramoz

14 hours ago

 |
prev
 |
next

[–]

Still doing
https://plannotator.ai

I use it daily and so do others, for - better UX, feedback, and review surfaces for ai coding agents.1. Plan review & iterative feedback.

 2. Now code review with iterative feedback.Free and open sourcehttps://github.com/backnotprop/plannotator

reply

jasoncartwright

5 hours ago

 |
prev
 |
next

[–]

A news aggregator
https://crawl.news

reply

yusufaytas

15 hours ago

 |
prev
 |
next

[–]

I’ve started moving off WordPress to Yapress. It’s a Git-managed static setup with a migration script, though I haven’t run the full migration yet. Right now, I’m testing the setup and validating the workflow.

The trade-off seems reasonable so far. By going static, the main thing I lose is comments.The project is still in progress, but I made solid progress over the weekend.The project is here:https://github.com/yusufaytas/yapress

reply

XCSme

10 hours ago

 |
prev
 |
next

[–]

Releasing version 9.0 of my self-hosted analytics app[0]. I will finally add an in-app cron job editor, so you can easily schedule clean-up jobs, data retention settings, newsletters/summaries, etc.

[0]:https://www.uxwizz.com

reply

kushalpandya

9 hours ago

 |
prev
 |
next

[–]

Building offline music player for macOS for past one year
https://github.com/kushalpandya/Petrichor

Currently working towards a big release to go out by end of the month.

reply

sp1982

6 hours ago

 |
prev
 |
next

[–]

http://corvi.careers
 - job search with features like resume match score etc

reply

asteroidburger

3 hours ago

 |
prev
 |
next

[–]

Moving over to the management track and trying to not suck at it.

reply

nmfisher

11 hours ago

 |
prev
 |
next

[–]

I've been working on Mixreel, a video/motion graphics editor with integrated support for 3D visualization. I'm working with some business clients to produce instructional videos for construction, industrial fabrications, etc.

https://mixreel.ai

reply

dbetteridge

7 hours ago

 |
prev
 |
next

[–]

Planting trees, digging holes and generally trying to get as much landscaping done as possible before the start of winter halts my progress.

Blockers: gravelly clay is a pita to dig with a shovel

reply

saurabh5001

14 hours ago

 |
prev
 |
next

[–]

Working on
https://github.com/microsoft/mssql-rs

It has some interesting applications for building high performance clients for mssql with tds protocol implementation.
The APIs allow almost direct data serialization to wire instead of datatype materialization in rust.
Makes for a suitable contender for high performance language interop.

reply

razighter777

11 hours ago

 |
prev
 |
next

[–]

https://lore.kernel.org/linux-security-module/adjwZAevNaDgui...

Patch for linux kernel adding support for enforcing Landlock rulesets from eBPF. In RFC stage now.

reply

wannabebarista

14 hours ago

 |
prev
 |
next

[–]

I've been writing about interesting books and papers I read for a few years now. I wanted a nice, simple interface to point people to as a "hub" for recommendations that's compatible with a static site.

Here's the MVP interface:https://bcmullins.github.io/reading/I appreciate any feedback. Hope you find something interesting to read!

reply

ed_

14 hours ago

 |
prev
 |
next

[–]

I'm working on a local desktop app for inventory and production management:
https://kitted.site

It includes bill of materials, purchase/production orders, "can I make n?", stock takes, multiple stock locations, and barcode scanning. It's aimed mainly at small business and makers for the time-being, but still allows multiple users to connect over the the local network.

reply

dhavalt

8 hours ago

 |
parent
 |
next

[–]

Love seeing more local desktop apps in these threads, especially ones tackling local network sync like Kitted. I'm a solo dev also in the trenches building a local desktop tool right now, so I know how fun (and painful) those architecture choices can be. Would love to compare notes sometime if you're ever up to chat. Either way, the app looks super solid.

reply

ed_

3 hours ago

 |
root
 |
parent
 |
next

[–]

Thank you! Kitted doesn't actually try to tackle syncing, it just allows users to connect over the local network, serving the same web client as the electron app. All the data's stored in a single SQLite database, with uploaded images and other attachments beside it.

Sure, my email's in my profile, I'd be happy to chat.

reply

opiniateddev

12 hours ago

 |
prev
 |
next

[–]

Runtime for agents

https://github.com/agentspan-ai/agentspan

Built on top of Conductor OSS -
https://github.com/conductor-oss/conductor

reply

lanewinfield

6 hours ago

 |
prev
 |
next

[–]

A bunch of ridiculous experiments with QR.

https://brianmoore.com/qrapps

reply

fb03

14 hours ago

 |
prev
 |
next

[–]

I'm working on `tu` (terminal use), which is a way to give agents access to a full blown virtual terminal to operate TUI apps

https://github.com/flipbit03/terminal-useI'm super proud, because it came to my knowledge that someone at Codex used my tool to debug codex+zellij issues, by running zellij within `tu`, and then codex inside zellij

reply

debpalash

13 hours ago

 |
prev
 |
next

[–]

Few things actually

Yupcha AI Interviewer, handles the screening, video interviewing with conversational agents.Check it outhttps://yupcha.comWorking on a oss video dubbing, cloning and design studioCheck outhttps://github.com/debpalash/OmniVoice-StudioSuggestions are welcome.

reply

Findeton

14 hours ago

 |
prev
 |
next

[–]

Continuous learning without backpropagation.

https://github.com/Findeton/hebbi

reply

mapontosevenths

14 hours ago

 |
parent
 |
next

[–]

What a cool idea. How does it work? AFAIK The human brain at least does sparse backprop and has SOME neural circuits that feed-backward, so how do you manage it without anything?

I tinkered for a minute but never got anywhere.

reply

Findeton

12 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks! I have other ideas, following Jeff Hawkins's Thousand Brains Project, but in this one I'm trying to get to cortical columns from the other side, from "standard" deep neural networks.

The short version: each layer trains itself independently using Hinton's Forward-Forward algorithm. Instead of propagating error gradients backward through the whole network, each layer has its own local objective: "real data should produce high activation norms, corrupted data should produce low ones." Gradients never cross layer boundaries. The human brain is massively parallel and part of that is not using backprop, so I'm trying to use that as inspiration.You're right that the brain has backward-projecting circuits. But those are mostly thought to carry contextual/modulatory signals, not error gradients in the backprop sense. I'm handling cross-layer communication through attention residuals (each layer dynamically selects which prior layers to attend to) and Hopfield memory banks (per-layer associative memory written via Hebbian outer products, no gradients needed).The part I'm most excited about is "sleep". During chat, user feedback drives reward-modulated Hebbian writes to the memory banks (instant, no gradients, like hippocampal episodic memory). Then a /sleep command consolidates those into weights by generating "dreams" from the bank-colored model and training on them with FF + distillation. No stored text needed, only the Hopfield state. The model literally dreams its memories into its weights.Still early, training a 100M param model on TinyStories right now, loss is coming down but I don't have eval numbers yet.

reply

mapontosevenths

10 hours ago

 |
root
 |
parent
 |
next

[–]

Neat. That thousand brains site looks right up my alley. If you haven't seen it, maybe check this out:
https://www.nature.com/articles/ncomms13276

The idea is that the brain uses what the authors refer to as "feedback alignment" rather than backprop. Even if it turns out not to be literally true of the brain, the idea is interesting for AI.I also love the idea of grafting on the memory banks. It reminds me of early work on DNC's (Differentiable Neural Computer's). I tried to franken-bolt a DNC onto an LLM a few years back and mostly just earned myself headaches. :)It's fun to see all the wild and wacky stuff other folks like myself are tinkering with in the lab.

reply

abbiya

3 hours ago

 |
prev
 |
next

[–]

i am working on blind relay
https://nfltr.xyz
 - tunnels local services and lets you access them from the internet

reply

userium

8 hours ago

 |
prev
 |
next

[–]

Accessible charging help (iOS app for scanning EV charger screens and car displays)
https://www.evcourse.com/

reply

rickcarlino

13 hours ago

 |
prev
 |
next

[–]

Pivoting Korean spaced repetition app towards reading features:

Video demo:https://youtu.be/cJfFAh6ox84?si=WScDPzI4rJIKe99nGitHub:https://github.com/RickCarlino/KoalaCards

reply

ncruces

14 hours ago

 |
prev
 |
next

[–]

Still working on improving wasm2go (a Wasm to Go "transpiler"):

https://github.com/ncruces/wasm2go

Already using it for my SQLite driver, and already in use by some a few other projects:https://github.com/topics/wasm2go

reply

davidanekstein

13 hours ago

 |
prev
 |
next

[–]

I’m making an iOS app [1] that allows you to track and analyze your life. It’s all local to your device and was created to help me learn more about myself and my habits.

[1]https://apps.apple.com/us/app/reflect-track-anything/id64638...

reply

sp33k3rph433k

16 hours ago

 |
prev
 |
next

[–]

https://fablesandfriends.games

It's still VERY much in development but I'm building a site that allows people to find TTRPG games that are suited to them AND includes a suite of tools for both GMs and players in said games.Players will be able to showcase characters they're playing or have played and GMs can manage campaigns (scheduling, notes). I'm a D&D player but I'm trying to make it system-agnostic

reply

furyofantares

13 hours ago

 |
prev
 |
next

[–]

A game framework for vibecoded games.

Native APIs exposed via Rust, but the core framework is written in AssemblyScript. Games or mods/libraries built in it are also written in AssemblyScript.It builds as a binary that can run on the various PC, mobile, and web platforms. You run it and you get a claude-code-like console that has access to a sandboxed filesystem to put game code in, and a git repo, all built in.

reply

buremba

13 hours ago

 |
prev
 |
next

[–]

I'm working on multi-tenant version of OpenClaw for organizations that has shared memory layer. It includes an entity based agent context layer that can be used as OpenClaw plugin and a sandbox runtime layer which uses just-bash with pi and let you expose the context via a bot an API.

https://lobu.ai

reply

LocalhostLegend

1 hour ago

 |
prev
 |
next

[–]

im building ReceiptBot an APM-style flight recorder to stop Node.js AI agents from going rogue, leaking .env secrets, or burning your API budget.

github.com/redshadow912/ReceiptBot

reply

cg-enterprise

1 hour ago

 |
prev
 |
next

[–]

We ar e

reply

danfrost

3 hours ago

 |
prev
 |
next

[–]

A couple of things:
1. data management for music publishers. This came out of nowhere but has got me back into coding, deploying, test. And I've got real lessons using AI-generated code that I wouldn't have got just reading other ppl's blog posts!
We've been mapping all the data formats publishers work with, how to organise them better and build a suite of apps around it.

2. the other projects it the framework. Aside from the product itself, I've ended up with a really nice framework (FE and BE) and playbook for copilot to follow. I've hit multiple problems with AI generated code and had to rework it like I have for junior devs! But now, the framework focuses the work and stops the slop!I want to build out all the product-dev-helper tools I've wanted in the past. I've already got a lovely schema-UI system, UI components which are data-aware and the basis of some low-ish-code tools. I've also nearly got a "run tests and fix" local LLM which saves tokens.Really enjoying this.

reply

mhrmsn

13 hours ago

 |
prev
 |
next

[–]

I recently started using Paperless to manage all my documents and wanted to include archive serial numbers (ASNs) for all physical documents that I scan, so I built a small tool to create and print archive serial number label sheets with QR/Barcodes:

https://asnlabels.comIt's free, no sign up or ads - feedback welcome :)

reply

ArloL

13 hours ago

 |
prev
 |
next

[–]

A tool to detect and fix drift in GitHub repository settings:
https://github.com/ArloL/drifty

I have a terraform setup right now but it’s super awkward and very slow. The goal is to be able to define settings using PKL which looks super interesting. Wanted to try it out for a while now.

reply

division_by_0

17 hours ago

 |
prev
 |
next

[–]

A 3D cluster visualization of S&P 500 and NASDAQ-100 markets. Created with Svelte and Three.js.

https://cybernetic.dev/cube

reply

xinu2020

14 hours ago

 |
prev
 |
next

[–]

I'm tired of all the recents npm packages supply chain compromises, so I've written a collection of `sandbox-exec` rules to wrap all the `npm install` and `npm run <script>` of my projects on my machine. It works but it's messy, so now I'm working on a small rust tool that acts as a wrapper and generator for that so that it's nicer to use and can be shared to other people.

reply

kirubakaran

14 hours ago

 |
prev
 |
next

[–]

I'm building
https://hyperclast.com/
 - "Smart Documents for Teams" ie a self-hostable Notion competitor. And it is much faster! Here is why I'm building it:
https://hyperclast.com/about/

reply

flyuk

10 hours ago

 |
prev
 |
next

[–]

Building Ayla - a period, ovulation, and pregnancy tracking app for iOS/Android. Everything is stored locally on-device by default. Solo developer building with Flutter.

https://aylatracker.com

reply

oliwary

14 hours ago

 |
prev
 |
next

[–]

https://motionparty.net/
 - A collection of games you control by waving in front of your camera, similar to playstation eyetoy back in the day. It supports 1-4 players.

I think it works quite well so far, but need to tweak the camera algorithm a bit to make the buttons work better. Thinking about more games to add as well.

reply

tha_infra_guy

10 hours ago

 |
prev
 |
next

[–]

https://k8slogjedi.netlify.app/

working on an AI-native Kubernetes sidekick that watches your pods, reads the logs, and turns failures into clear fixes before they become outages

reply

dabinat

14 hours ago

 |
prev
 |
next

[–]

Working on some improvements to my video platform,
https://www.kollaborate.tv
 . It’s a new video player with side-by-side playback comparison. Claude was really helpful at getting the drift adjustment working because I can push it further than I would be comfortable pushing a human employee in order to get things just right.

reply

ojdon

16 hours ago

 |
prev
 |
next

[–]

https://newfeed.io

Turns your project's GitHub release notes into user changelog that your users actually want to read.

reply

coreylane

12 hours ago

 |
parent
 |
next

[–]

authorized my org and private repo to try it out but just get an error when trying to generate

reply

Lramseyer

14 hours ago

 |
prev
 |
next

[–]

I'm working on a digital waveform viewer for VScode. I started it back when I used to work for an FPGA company, and needed to debug soft CPUs. Now it's starting to rival the proprietary software. I should probably do a show HN at some point...

https://github.com/Lramseyer/vaporview

reply

Yoofie

13 hours ago

 |
parent
 |
next

[–]

Very cool but being tied to a code editor is not ideal. Have you ever looked at
https://surfer-project.org
?

reply

Lramseyer

7 hours ago

 |
root
 |
parent
 |
next

[–]

Being tied to the code editor is the entire point, otherwise I would have just used GTKwave. Integrating it into the code editor - specifically VScode allows me to support terminal links (instance paths and timestamps from sim logs), first class remote SSH support (instead of having to use a laggy VNC session), and design hierarchy to RTL. Though you need a separate extension for that, because the waveform viewer is language agnostic and simulator agnostic by design. If you have ever used Verdi, it does design hierarchy to RTL, and I wanted to make a modern and open source version of that.

Surfer is fantastic, and the developers of Surfer are pretty great people too! It has been on my to-do list to learn Spade.

reply

electrodyssey

3 hours ago

 |
parent
 |
prev
 |
next

[–]

+1 GitHub star!

reply

nmrenyi

13 hours ago

 |
prev
 |
next

[–]

I built an Android app for nurse-midwives in Zanzibar to get medical advice. It's running Gemma 4 model on device, completely offline. I just released the first beta version. Feedbacks are welcome :)

https://github.com/nmrenyi/mamai

reply

eucyclos

12 hours ago

 |
prev
 |
next

[–]

An alternate ad network (tied to an ad blocker) that optimizes for the most useful ads instead of the most immediately profitable ones.
https://github.com/Chrisjayhenningsen/Eudaimonia

reply

yen223

7 hours ago

 |
prev
 |
next

[–]

https://stratachecks.com

A site for looking up strata information for apartments in NSW, Australia

reply

ChaosOp

5 hours ago

 |
prev
 |
next

[–]

Working on Gaming Couch, a web-based local multiplayer party game platform. It's like a lovechild of Jackbox Games and Mario Party:
https://gamingcouch.com
. Three months ago, back in December, Gaming Couch hit the front page of Hacker News (
https://news.ycombinator.com/item?id=46344573
). We've had an amazing time since, with each month more and more people finding the platform, enjoying the games and giving awesome feedback!

At the moment working on the 3rd party development tools so in the future anyone can make their game dev dreams a reality and make a simple and fun multiplayer party game for the Gaming Couch platform, ideally in only one weekend!If you're an interested game dev that would like to beta test the dev tools, hit me up either here, via Discord (link available fromhttps://gamingcouch.com) or by emailing me at gc[dot]community[at]gamingcouch[dot]com!The TL;DR of Gaming Couch:- Currently in free Early Access with 18 competitive mini-games.- Players use their mobile phones as controllers (you can use game pads as well!)- Everything is completely web-based, no downloads or installs are necessary to play- All games support up to 8 players at a time and are action based, with quick ~one minute rounds to keep a good pace. This means there are no language based trivia or asynchronous games!

reply

eliasson

14 hours ago

 |
prev
 |
next

[–]

I have started working on a standalone, self-hosted, service for an album club (music, that is).

Members takes turn pitching one album per week. Support comments and a handful of emoji-based reactions.Integration with Spotify for easy pitching and playing (by links only, users are not required to have a Spotify account).Plan is to keep the clubs fairly small and invite only.Building it in Gleam which is a lot of fun!

reply

beasubs

12 hours ago

 |
prev
 |
next

[–]

Self-hostable slack for humans and openclaws - iphone, mac, web, and soon android. Very important for me to get close to feature parity with team chat apps.
https://github.com/bogpad/meepachat

reply

luccasiau

12 hours ago

 |
parent
 |
next

[–]

This looks interesting. Can I host it in the same Mac Mini as my OpenClaw?

reply

mgw

12 hours ago

 |
prev
 |
next

[–]

We‘ve built an AI image and video model gateway called
https://lumenfall.ai
.

Right now I‘m working on adding a „simulation“ mode, that allows anyone to get free fake responses during development, instead of pricey real generations.

reply

david_at

10 hours ago

 |
prev
 |
next

[–]

A twitter-native game where agents compete to predict tweets from popular accounts and are rewarded based on semantic similarity

https://x.com/vectorybot

reply

ihaveajob

13 hours ago

 |
prev
 |
next

[–]

Not working on it yet but planning some projects with the kids:
- A candy classifier with Arduino for Halloween (the goal is to have trick-or-treaters choose their preferred candy and have the machine sift it out automatically)
- A board game based on the idea of fog-of-war, details undecided
- An app to reduce screen time

reply

lylejantzi3rd

16 hours ago

 |
prev
 |
next

[–]

An old school WYSIWYG RAD GUI builder for native applications. Because I don't accept that native app development needs to suck as much as it does.

reply

podlp

10 hours ago

 |
prev
 |
next

[–]

A local, safe AI agent for macOS that uses Apple Intelligence and lives in the app sandbox

https://github.com/lastbytellc/iclaw

reply

Leftium

14 hours ago

 |
prev
 |
next

[–]

https://leftium.github.io/nimble.css

I made a classless CSS library, then migrated most of my projects from PicoCSS.I also made a quick logo generator:https://logo.leftium.com/logo

reply

pokstad

14 hours ago

 |
prev
 |
next

[–]

Scheduled encrypted back up of git repos via ssh/rsync to a simple server from a macOS workstation. I’m tired of the complexity to host a simple private git repo. Using this suite of scripts, I’ve been able to incrementally backup an encrypted copy of my private git repos to rsync.net (but it could be configured to be any ssh host with rsync capability).

reply

medv

14 hours ago

 |
prev
 |
next

[–]

https://maml.dev

I wanted to make JSON/YAML configuration language for my projects. And i wanted a strict specification. This is want i created, now with specification and 100% coverage, reference implementation it’s just one prompt to reimplement parser in another language.

reply

xxyzz

12 hours ago

 |
prev
 |
next

[–]

Create StarDict files from Wiktionary HTML snapshots for KOReader:
https://xxyzz.github.io/wiktionary_stardict/

I'm surprised that no one has done this so I decided to give it a try.

reply

gilleain

14 hours ago

 |
prev
 |
next

[–]

I've revived a project I started around 20 years ago. It is a kind of graph query description/measurement tool for protein 3D data.

The query engine itself is like a DAG of 'operators', similar to a relational DB (or more like a graph one) with scanners, filters, and matchers.Very fun, although not at all efficient and probably overengineered for what it does :)

reply

jftuga

16 hours ago

 |
prev
 |
next

[–]

I am vibe coding with Opus 4.6:
https://github.com/jftuga/swiftswiss

Swiss army knife CLI tool written in Swift using only native Apple frameworks.The primary goal of this project is to demonstrate how many Apple standard library frameworks can be meaningfully used in a single, actually-useful CLI tool.brew install jftuga/tap/swiftswiss

reply

threefiftyone96

14 hours ago

 |
prev
 |
next

[–]

Inspired by Ralph loop and bash scripts, I created my own version of it where I focus on finding code issues and auditing my codebase. It runs N iterations after mapping the whole code.

https://github.com/BVCampos/operatorIt has been working quite well.

reply

zuzuleinen

4 hours ago

 |
prev
 |
next

[–]

Building a project to learn Go Concurrency using spaced repetition.

reply

josem

16 hours ago

 |
prev
 |
next

[–]

A software for managing BJJ and martial arts academies that it's both easy to use and have everything they need like assistance tracking, payments, communications, etc.

It's called MatGoat[1], and it's going quite well so far. Nowadays I'm working more on the marketing/sales side.[1]https://matgoat.com/en/

reply

robotburrito

13 hours ago

 |
prev
 |
next

[–]

Porting a giant monolithic JSF app from JSF/Wildfly to two separate apps, a react frontend and a REST Quarkus backend.

First time doing this sort of thing with agents. So far it seems ok?If it works out it will really help us scale and improve a legacy application that so many depend on at the moment. Wish me luck!

reply

dhruv3006

8 hours ago

 |
prev
 |
next

[–]

I am working a offline markdown based api client.

Take a look here :https://voiden.md/

reply

BinRoo

11 hours ago

 |
prev
 |
next

[–]

Python DSL for safe quantum programming that compiles to Qiskit, where the type system enforces coherence and ancilla cleanliness

https://github.com/binroot/b01t

reply

AlexCoventry

9 hours ago

 |
prev
 |
next

[–]

I have a transformer attention mechanism which seems to be more data-efficient than the usual dot product, and I'm trying to write a performant backwards kernel for it.

reply

twism

12 hours ago

 |
prev
 |
next

[–]

StoreRun.app. It transforms grocery shopping from a chore into a collaborative experience ... still private beta and about 75% there but you can kick the tires for the non-sync version.

https://storerun.app/Feedback welcome

reply

jlebensold

11 hours ago

 |
prev
 |
next

[–]

I'm trying to build Heroku for AI agents. Send a markdown runbook and some files, get back structured results with full execution history:

https://www.jetty.io

reply

peterhon

3 hours ago

 |
prev
 |
next

[–]

I got tired of paying lots of $$$ to form tools, in order to create useful forms and checklists for me, and with my specific requirements:

- immutability
 - self-hostability and/or EU SaaS option
 - nested data (e.g. nesting a list of sailing legs into a sailing trip form)
 - formulas (today(), date, string, numeric,...) and conditionals (visible/required/enabled if)My goal will be to create an exceptionally cost effective tool, scaling well with usage and not paywall blocking advanced features. This may sound weird, but I think this is a real challenging and good goal to follow, enabling users more than optimizing for the highest payer. I thought about having a tool for a few $/€ per user per month where others charge 10x.So I created two nice pieces out of that, which would have been impossible in the past due to time constraints and got massively unlocked through claude code:- a frontend/javascript only forms library that supports all the rendering, form schema input, data output, validation and formula/conditional logic
 - a multi-tenant SaaS product, that is a single golang binary and stores in sqlite, easily self-hostable but I can also operate it as a European SaaS (and in other regions) where neededThis is also a test run in terms of tech stacks and trying new things I wanted to try for long time. It's mostly evening or weekend coded due to my regular day job, but made such incredible fun. The AI coding part really provided me the time to work on the product, polishing, UX and worry less about the "work" part of coding. My experience seems to help a lot to gain leverage and increase the fun factor and complete immersion into coding, that I kind of almost lost in the past.So I was trying:- pocketbase
 - really running something bigger with much more data off of sqlite (primarily used it for smaller stuff in the past)
 - real focus on self-host-ability, keeping dependencies minimal and extremely simple (which also helps claude)
 - trying other tools for security scanning, verification, testing, security analysis, WAF,... than I use at work, pretty much playing around with tech as much as I can to see new and different stuff :-)Not ready to share a repo yet, but if anyone is interested please ping me on hello@devopsicorn.com

reply

Tsarp

6 hours ago

 |
prev
 |
next

[–]

https://voicebraindump.com

reply

mudkipdev

9 hours ago

 |
prev
 |
next

[–]

I built a Claude-inspired UI for Ollama/llama.cpp

https://github.com/mudkipdev/chat

reply

almet

16 hours ago

 |
prev
 |
next

[–]

Currently working on a way to help folks setup a signal account without requiring a smartphone.

It's in rust with egui, and should help folks to do that without the cli.Not ready for prime time yet, but available athttps://github.com/almet/signal-without-smartphone

reply

huijzer

14 hours ago

 |
prev
 |
next

[–]

Software to host podcasts. The standard is relatively easy, but getting everything right takes some effort

reply

yokuze

11 hours ago

 |
prev
 |
next

[–]

aix - Like the npm CLI and package.json, but for AI config. Allows standardizing your AI config to share with others, and defining it all in one spot but installing to Claude, Codex, Cursor, etc.:
https://aix.a1st.dev/

A Tauri 2 CLI / MCP that allows your agent to debug, take screenshots, run JS, etc. inside a Tauri app:https://hypothesi.github.io/mcp-server-tauri/

reply

oscarcp

14 hours ago

 |
prev
 |
next

[–]

Two things, one is a container control plane inspired in the efforts of the Nextcloud AIO people called LOOM (yeah, like the Lucas Arts game), the other is a full blow NixOS deployment system (from the USB or network directly) for my company so we can deploy the computers for each colleague faster.

reply

sleno

16 hours ago

 |
prev
 |
next

[–]

I'm building a debate/writing game platform: https:argyu.fun

The mission is to incentivize better thinking. For each game there's an AI judge that scores everyone's answer based on a public rubric (style, cohesion, logic, etc).Currently uses fake money and ELO score but thought it could be a very interesting competitive game for real stakes.Any feedback is much appreciated.

reply

vinayakverma71

17 hours ago

 |
prev
 |
next

[–]

Building something that finally stops making me the tester for my own AI. You know that moment where the AI finishes writing code and then goes "can you run this and check if it works?" I got tired of that loop. So I built an IDE that just... runs it, clicks through it, finds what broke, and fixes it. You watch.
Not Better Cursor , But what comes after it.

reply

dbz

14 hours ago

 |
prev
 |
next

[–]

I'm building a platform for businesses to get more reviews and deflect negative reviews:

https://GetSetReply.com/I am hoping to launch in about a week, so I would love any user feedback! (email in profile)

reply

lpellis

15 hours ago

 |
prev
 |
next

[–]

Still working
https://pagewatch.ai/
 , my ai readiness audit tool.
Currently having fun building a MCP app for it inside Claude / ChatGPT, its oddly tricky to get things behaving consistently.

reply

Cider9986

12 hours ago

 |
prev
 |
next

[–]

I am trying to download all the meditations from the Healthy Minds Program[1].

[1]https://www.humin.org/wellbeing-tools/app

reply

J_cst

14 hours ago

 |
prev
 |
next

[–]

Runway, a CRM. It's looking great, near to its first public release, built on market standards. If anyone's interested just ping me, mail handler on profile, ciao.
p.s. still wondering about the licensing to adopt to balance different matters/desires.

reply

savgore

14 hours ago

 |
parent
 |
next

[–]

Always interested in trying new CRM’s - would love to see what it looks like

reply

J_cst

12 hours ago

 |
root
 |
parent
 |
next

[–]

Hi Savva,
drop me an email so that I can send you the credentials to have a look around. The system is at
https://www.runway-crm.eu/
 but you'll need a key.
j@costantini.pw

reply

jjfoooo4

12 hours ago

 |
prev
 |
next

[–]

I vibe coded a charting library for excalidraw that I’m working into my blog:

https://github.com/tombedor/excalicharts

reply

devgoth

11 hours ago

 |
prev
 |
next

[–]

still chugging away at Whenish. update coming soon with GCal integration:
https://apps.apple.com/us/app/whenish/id6745035749

started to explore a iPad-focused Dungeons & Dragons DM app. i called it Campaign Codex.https://campaigncodex.app/been doing a lot of agent assisted iOS dev...it has been...fun!!

reply

mcclowes

13 hours ago

 |
prev
 |
next

[–]

I miss Pocket, so building an article bookmark tool, with a focus on a nice reading experience -
https://broadsheet.marginalutility.dev/

reply

Ey7NFZ3P0nzAe

13 hours ago

 |
parent
 |
next

[–]

I've been happy using karakeep:
https://github.com/karakeep-app/karakeep

reply

qdot76367

16 hours ago

 |
prev
 |
next

[–]

Same thing we work on every night, pinky

https://buttplug.io

reply

gbriel

14 hours ago

 |
prev
 |
next

[–]

Music player, organizer, discovery tool that will load history and subscriptions from streaming services and discogs, last.fm etc and allow you to query it with AI.

https://prettygoodmusic.appA work in progress.

reply

sage76

14 hours ago

 |
prev
 |
next

[–]

https://github.com/abhimanyu-jain/PRML_Solutions

A solution set to the book Pattern Recognition and Machine Learning by Christopher Bishop.

reply

textlapse

14 hours ago

 |
prev
 |
next

[–]

Working on an RL pixel platformer sandbox to learn RL and explore self-play with a playable RL agent. It’s a cross between JumpMan Jr and Spelunky 2.

Very early demo with a smart dum-dum RL agent here:https://rlplays.com

reply

xzenor

13 hours ago

 |
prev
 |
next

[–]

Not as epic and big as most other projects here but I'm maintaining and expanding a discord bot that I built quite a while ago for a specific server. It's now fighting a LOT of spam. And it's doing quite well tbh.

reply

netdur

16 hours ago

 |
prev
 |
next

[–]

I am working on hugind, I have two goals:

- make it reliable to run LLM inference on company hardware, even when it is poor or outdated- bring chaotic agentic behavior under control in business contextshttps://github.com/netdur/hugind

reply

GistNoesis

16 hours ago

 |
prev
 |
next

[–]

Shoggoth.db : a self organizing database to experiment with agents without having to let them roam freely.

Posted a show hn earlier today that didn't got any traction :https://news.ycombinator.com/item?id=47738516

reply

dare944

12 hours ago

 |
prev
 |
next

[–]

I'm creating a new OS image for UniBone/QBone based on BuildRoot and a streamlined kernel. My goal is sub-five second boot time so you can get to using the host PDP-11 pretty much right away.

reply

rutierut

14 hours ago

 |
prev
 |
next

[–]

CLI-first inventory management for EE parts.
https://willwillems.github.io/tray

Fully local, hobbyist friendly, agentic workflows work great with it since it’s just a CLI.

reply

jordanarseno

11 hours ago

 |
prev
 |
next

[–]

hivemunk (hivemunk.com): hive management for beekeepers.

Data engineer, 20 yrs software / 10 in ag-tech. Picked up beekeeping and was surprised how much structured data a single inspection produces, and how nowhere useful exists to put it. It's a gloved, veiled, honey-and-propolis-covered activity. Tapping through a mobile UI mid-inspection is not ideal, and good luck getting your phone back clean.The core is a virtual hive model. It's all mutable state: boxes, frames, components, queens, and colonies you rearrange to mirror the physical yard. Treatments, feedings, and inspections layer on top.This summer I'm shipping voice-driven inspections: narrate what you see frame by frame, STT + LLM pipeline extracts structured data and maps it to your hive model.If you have beekeeping friends, I'd love it if you could send it along <3. I won't claim it has every feature under the sun, but I work on it every day and have a strong roadmap ahead.Also open to critiques. Thanks!https://hivemunk.com

reply

dvh

5 hours ago

 |
prev
 |
next

[–]

I'm making web chat using captive wifi portal on esp32.

reply

Jemm

1 hour ago

 |
prev
 |
next

[–]

I got tired of the money wall around cabinet design so I am working on
https://cabinet.mycnc.app
. Some very alpha features still but getting there.

Making cabinets is not that hard but the industry charges insane amounts of money for it. Since I have to make cabinets for two kitchens I invested in a Sienci Labs CNC so when the cabinets are done I'll have saved money and gotten a CNC out of it which I can then sell or use for other things.

reply

muntashir

14 hours ago

 |
prev
 |
next

[–]

I’m building an app for people to share their skincare routines and for people to easily discover what works for people with similar skin.

https://radiantskin.app/

reply

lemax2

14 hours ago

 |
prev
 |
next

[–]

Building SiteSecurityScore (
https://www.sitesecurityscore.com
). A website security scanner that grades your site and tells you exactly what to fix.

It gives you a detailed breakdown of what's missing, step by step guidance on how to fix each issue, and shareable report links. Excellent resource for security teams of all sizes.Scans HTTP headers, TLS/SSL, DNS security, cookies, and page content. Free to get started, with a REST API for integrating scans into your CI/CD pipeline or monitoring. Also supports capturing and reporting CSP violations.

reply

linsomniac

14 hours ago

 |
prev
 |
next

[–]

pxv, a simple image viewer inspired by John Bradley's (RIP) xv.
https://github.com/linsomniac/pxv

I've been wanting to do this for years. I fully support (and have paid more than most into) John's shareware, but that means that I can't just "apt install" it, which means I rarely have it available on my various machines. Having something I can just "uv run" that keeps most of the same ergonomics would be a nice alternative.

reply

exz

12 hours ago

 |
prev
 |
next

[–]

An AI animation generator for Lottie and SVG animation. Currently in open beta (BYOK).
https://gen2d.com

reply

swarles

10 hours ago

 |
prev
 |
next

[–]

A small Python library/framework for customising how the AST is walked and evaluated. I plan to use it in another project to configure a safe-ish sandboxed way of evaluating user submitted expressions and code. There are a few other libraries that enable this, but I found they bake in some stuff to the internals that I didn't want.

reply

siddboots

16 hours ago

 |
prev
 |
next

[–]

I’ve been building a toy for exploring elliptic functions, modular forms, and elliptic curves. Sorry mobile support is not there yet.

https://grge.github.io/weierstrass/

reply

contraposit

15 hours ago

 |
parent
 |
next

[–]

https://en.wikipedia.org/wiki/Superformula

Have you heard of Superformula ? I remember playing with them few years ago.

reply

grzes

13 hours ago

 |
prev
 |
next

[–]

Next iteration of JellyOcean
https://jellyocean.com
 - A free service that lets you create Jellyfin servers in the cloud.

reply

dmvaldman

14 hours ago

 |
prev
 |
next

[–]

A ring you can talk into and it controls an agent on your phone. Eg say "pick me up" and an Uber arrives.

Looking for people who know hardware well. Let's get to know one another on a flight to Shenzhen :P

reply

richarlidad

12 hours ago

 |
prev
 |
next

[–]

https://supplementdex.com

Ever been recommended supplements? Now you can find out if they work

reply

VitalStack

2 hours ago

 |
parent
 |
next

[–]

Building in the same space. vital-stack.com focuses specifically on interactions between supplements and drugs, rather than efficacy: the question "is it safe to take with what I'm already on" rather than "does this work". The interaction data typically lives in clinical pharmacology databases and isn't easily surfaced in a way consumers can use. We have 182 supplements and 1,312 interactions catalogued so far, with an MCP server that lets AI assistants query the interaction database in real time. Curious how supplementdex sources efficacy data. Is it summarized literature along the lines of Examine.com, or closer to primary research?

reply

born-jre

13 hours ago

 |
prev
 |
next

[–]

Tiny platform for app

https://github.com/blue-monads/potatoverse

reply

philipnee

7 hours ago

 |
prev
 |
next

[–]

just a weekend project. a bulletin board to share ideas with the internet haha -
https://www.litboard.net/

reply

thepaulthomson

12 hours ago

 |
prev
 |
next

[–]

Send kind voice notes to strangers:
https://kindvoicenotes.com/

reply

level09

3 hours ago

 |
prev
 |
next

[–]

stk (
https://github.com/level09/stk
): async Quart + Vue 3 starter i use for everything. auth stack is already wired up (session, 2FA, webauthn, oauth), async sqlalchemy, alembic, no frontend build step. basically the boring part so i can get to the actual product faster.

ziglag (https://github.com/level09/ziglag): self-hosted invoicing for freelancers, built on top of stk. clients, invoices, VAT, PDF, shareable links, MIT. got tired of paying a monthly fee to send a pdf.idea is to keep chipping away. every subscription that annoys me is fair game. small tools, self-hosted, no accounts, no seats, no upsell. if it's useful for me someone else probably wants it too, so might as well open source it. open to ideas on what to kill next.

reply

goqu

16 hours ago

 |
prev
 |
next

[–]

A web app that allows to practice speaking another language by participating in pre made scenarios, so beginners don’t get stuck.

https://fluenly.ai/

reply

ec_games

14 hours ago

 |
prev
 |
next

[–]

I coded a visual novel/adventure game framework in pygame. Pretty much just to see if ai could handle a full project.

Eventually I got scope creeped into a full game with branching stories, item crafting, and a custom cutscene engine...even Trained a model for a few specific art assets.https://store.steampowered.com/app/4301600/Cherrys_Dungeon/

reply

rustybolt

14 hours ago

 |
prev
 |
next

[–]

I don't have a lot to show for it yet, but I'm working on an online video course for software engineers aspiring to build their own CPU on an FPGA dev board.

reply

itsjamesmurray

8 hours ago

 |
prev
 |
next

[–]

about to publish a "Rewind" alternative. open source, all local, super cool. I find it very helpful with all my AI agents to essentially give them "eyes" of whatever im seeing on my screen.

reply

jasiek

15 hours ago

 |
prev
 |
next

[–]

https://codeplug.org

Program your amateur radio via the web. Uses pyiodide + chirp drivers under the hood + WebSerial.

reply

garymiklos

10 hours ago

 |
prev
 |
next

[–]

OtaKit.app so I can run AI agents to develop my Capacitor iOS apps remotely with instant live updates

reply

christoph123

16 hours ago

 |
prev
 |
next

[–]

https://donethat.ai/vibeit

A tool to estimate if you should vibe an automation/app or just buy/delegate/grind instead

reply

rainmaking

14 hours ago

 |
prev
 |
next

[–]

Download selling tool where you act as your own seller but get tax help and AI support. Much cheaper than the usual suspects and no sales tax for the most part.

reply

derben

11 hours ago

 |
prev
 |
next

[–]

I'm building
https://personalfinanceisboring.com
 (PFIB) to help people like me who accidentally made personal finance an obsessive hobby, and would like to return to other hobbies and better uses of their time.

reply

voxleone

15 hours ago

 |
prev
 |
next

[–]

Quaternion graph traversal and control system

https://github.com/VoxleOne/SpinStep

reply

aktenlage

15 hours ago

 |
parent
 |
next

[–]

I work in robotics and with quaternions (mainly 6DoF SLAM and used to do robot arm kinematics), but I don't get the use case for this. Maybe provide some example use cases?

reply

zygonfour

11 hours ago

 |
prev
 |
next

[–]

First post after lurking for.. 15 years.

I've been working towards a new platform that mixes fantasy sports with stock market mechanics. My first public project, I just launched a few week ago. No gambling, free to play (despite the .bet):https://fantasybook.bet

reply

muti

8 hours ago

 |
prev
 |
next

[–]

Building a selfhosted activity tracker inspired by wandrer.earth

reply

maxaw

12 hours ago

 |
prev
 |
next

[–]

Proxy over GitHub’s REST API for fine-grained repo access – e.g. file-level scopes. For unpredictable agents :)

reply

RobRivera

14 hours ago

 |
prev
 |
next

[–]

I have made so many progressive milestone on an ambitious cpp game engine-still chugging along after about 8months of parttime work on it. Very fun.

reply

snowsky

9 hours ago

 |
prev
 |
next

[–]

self-hosted finance books for developers and small businesses

https://github.com/snowsky/yourfinanceworks

reply

eagle10ne

12 hours ago

 |
prev
 |
next

[–]

A full stack solution utilizing AI to provide ecommerce solution with API. Postgresql storage and Python 3 powered.

reply

cosmicgadget

11 hours ago

 |
prev
 |
next

[–]

A graph of blog posts by HNers to connect to my buddy's slick front end for traversing them.

reply

dbaronmo

14 hours ago

 |
prev
 |
next

[–]

On making tools for things I once had to do iteratively. I want to use some of my free time to see if people will use my programs.
The last one I have been working on is a curve-fitting web app (
https://fittapp.streamlit.app/
).

I do a lot of data science and analytics in my real job.

reply

coder97

16 hours ago

 |
prev
 |
next

[–]

https://www.focuslive.app/

It's a virtual co-working tool

reply

canto

15 hours ago

 |
prev
 |
next

[–]

https://statusdude.com/

and a gift for my friend's birthday.

reply

vlindos

16 hours ago

 |
prev
 |
next

[–]

https://stella-ops.org

Release with confidence .

Deployment tool with security gates.

reply

fcpguru

11 hours ago

 |
prev
 |
next

[–]

a better way to have podcast debates. Live audience scoring. Evidence uploads. Get people to "talk it out" so portmanteau
https://taout.tv

reply

fur_tea_laser

12 hours ago

 |
prev
 |
next

[–]

git-sqlite-vfs:
https://github.com/fur-tea-laser/git-sqlite-vfs

a sqlite database that can be version-controlled by git alongside source code

reply

franze

6 hours ago

 |
prev
 |
next

[–]

brew install apfel

turns out starting a popular open source project comes with ongoing work attached

reply

mak8

12 hours ago

 |
prev
 |
next

[–]

I am working on moltbillboard.com — a public million-pixel billboard for AI agents.

reply

EPConsulting

14 hours ago

 |
prev
 |
next

[–]

Hey all, I made a free daily ecology cascade game.
https://Trophle.com

I'm in school for environmental science and I want to make educational games and resources

reply

ahme

11 hours ago

 |
prev
 |
next

[–]

A website that contains the cure to cancer.

http://localhost:8080/

reply

boredemployee

9 hours ago

 |
prev
 |
next

[–]

i'm creating (another) learning platform so people with no background in tech can learn sql and python for data analysis

reply

soheilpro

15 hours ago

 |
prev
 |
next

[–]

https://volt.fm

reply

thewoodsman

15 hours ago

 |
prev
 |
next

[–]

I've got this new account and a Substack page where I'm writing about, idk... metaphysical stuff? Spirituality, religion, psychedelics, tarot, and so forth. I was inspired largely by the Weird Studies podcast, but there's a bunch of actually interesting writing and media in this space right now.

I deliberately separated it from my public internet persona (which is connected to my real name) in the hopes that I could write about weird, woo-y, or controversial topics without worry. I've got a few articles half baked and have been having fun engaging with a different subset of the Substack crowd than my normal tech focus would show me.Of course the stats show that the one article I did that touches on AI has done an order of magnitude better than anything else.Anyway this is just kind of a weird sideline project, a sort of release valve for stuff that wouldn't fit in on my "professional" site, but it's been a fun thing to spend some time on.Another thing that's cool is that I largely stopped _writing_ a few years back. I always enjoyed writing but of course as a dev most of my stuff had a technical/tutorial bent to it. Writing weird little "what do I think" essays has forced me to exercise a writing muscle I really hadn't stretched for a long time and I've enjoyed it.There's only a handful of things up now, it's nothing special really. Link in my bio, if you see something you like I would love to hear from you!

reply

EPConsulting

12 hours ago

 |
parent
 |
next

[–]

Hey there. I've just subscribed to your substack. Very interesting stuff on there. I just launched a game today (Trophle @ trohple.com) and I'm planning to launch a substack tied to it (Trophle field notes) where I'm going to do a deep dive into my puzzle topics the next day. Anyway, just wanted to say, I like your vibe.

reply

thewoodsman

8 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks! Glad you found something you liked. Got a couple good posts in the pipeline so stay tuned.

reply

shevy-java

3 hours ago

 |
prev
 |
next

[–]

I am mostly polishing old code and old documentation,
nothing fascinating. For instance yesterday I fixed
a small project called "environment", or fixed it to
about 90% - output example here:

https://i.imgur.com/uHpnUox.png(Don't mind the errors or display issues for now; this
project will report which versions of programs are
installed on the given computer, and which ones could
be updated. A few smaller bugs still remain but the
main rewrite was finished now.)For work-related reasons I have to expand on some python
tasks in the coming weeks. Trying to find something
interesting here, but I guess I'll just focus on
various bioinformatics-related tasks (also related to
work). Programming for the most part is not extremely
interesting - the only part I actually like is any
creativity and useful end results. Fixing bugs is annoying
to no ends. Writing documentation is also boring, but
can not be avoided.

reply

caltanjun

5 hours ago

 |
prev
 |
next

[–]

I've just published Timelocked (
https://github.com/Caltanjun/timelocked
), a local app that encrypts any file or message but delays decryption.

One of the main goal is to help with cryptocurrency-related home invasions. The XKCD "$5 wrench attacks" became a reality in France where I live.
So it's another way to delay the access of personal funds, but it doesn't need to rely on third parties or multisig. You can just timelock a BIP39 passphrase for a duration of your choice.It can also help with self-managed inheritance, or digital addictions.

reply

abbadadda

3 hours ago

 |
prev
 |
next

[–]

ComputerPoker.ai is a website where users can play simulated poker tournaments against GTO Bots to learn GTO poker strategy in a fun and low-risk environment.

My motivation for creating CompterPoker.ai was feeling a bit overwhelmed by some of the professional poker tools out there for learning GTO play. For some tools, learning how to simply operate the tool itself felt like a second job. With ComputerPoker.ai players can play against bots themselves simulating GTO play to learn what it "feels like" to play GTO vs. GTO opponents without having to turn any knobs or dials (feedback is real-time as you play).The Beta tester code for HN Users is: HackerNews2026. All feedback is welcome! Please send suggestions for improvement or bugs to contact@computerpoker.ai or alternatively leave a comment below. Any questions I will do my best to answer.As for the product offering the website is designed to teach players how to play optimal poker strategy (GTO) in simulated Texas Hold 'Em poker tournaments. Our value proposition is that if you can consistently beat the bots then you will fare well in live poker tournaments (of course adjusting for your opponents' play).In addition to GTO pre-flop quizzes and pre-flop charts, users have the ability to simulate poker tournaments from start-to-finish and get feedback on their decisions _in real-time_ in a fun and low-risk environment.For those interested the tech stack is Django deployed on AWS via Terraform and SaltStack, the database uses a Postgres RDS backend, and the frontend uses HTMX with WebSockets via Django Channels and Redis (Nginx serving as reverse proxy with CloudFlare DNS and SSL). During the project I used Claude Code to aid with various boilerplate aspects of the code base including building out the repos for Terraform and SaltSack and of course speeding up Django development.Users are graded pre-flop based on the covered pre-flop scenarios (two-ways only for now). Post-flop users are graded on a residual MLP PyTorch model. We have built an in-house solver in Rust using the discontented CFR++ algorithm. The PyTorch model approximates GTO play post-flop (again only two-ways currently) based on training data with raises, EV, and realistic ranges for OOP and IP players. Because the post-flop decisions are based on a model that will always be a work in progress I refer to these decisions as GTOA (or "GTO Approximate").Version 8 of the PyTorch model is the first one that I am happy with and actually find it quite difficult to play against. If you manage to beat the bots please do let me know how many tries it took! For those curious the PyTorch params for the most recent run are below (I trained on a gaming PC via Linux WSL2 using an AMD GPU).The website is live in Beta mode as I gather feedback on how things are structured and work out any bugs/kinks. If you have any suggestions for improvements I’d love to hear them. Subscriptions are live so if anyone wanted to test the Stripe payment processing flow I certainly wouldn’t mind! ;-)p.s. This is a side gig for me. I am currently looking for full-time work either fully remote or on-site based in London, UK (this LLC that runs ComputerPoker.ai operates out of USA but I am based full-time in the UK and authorized to work in both UK and USA). If you or someone you know is looking for a SRE with strong software engineering skills please let me know!

reply

ahmgeek

14 hours ago

 |
prev
 |
next

[–]

Voklit.com / Voklit.app

An international calling app, for the poor people

reply

fcatalan

4 hours ago

 |
prev
 |
next

[–]

I always see these threads and think I'm not working on anything, but I just realised it's a lie, I'm exploring a couple of things right now, both heavily AI supported:

Simracing trainer.I love simracing, I'm moderately competitive and want to improve, and I like to be efficient with my practice. So having access to and using a lot of telemetry, I noticed that the "turn a few laps, load telemetry, compare against reference lap, try again" is not as efficient as it could be.Also a lot of my telemetry analysis is very rote and "rules based": Look at the biggest laptime delta jump against reference, try to determine the cause among a few usual suspects".So I have started experimenting with a system that reads the iRacing telemetry in real time, and compares against the reference telemetry live, finding the biggest delta jumps, and trying to find the root cause of the time loss using an increasingly sophisticated GOFAI rule and pattern matching system. Then this report is fed to a cheap LLM call to be condensed into clear advice, and the result goes to the free Microsoft TTS API. So I get instant feedback of where I'm slow and maybe even why.So far I fear it's mostly making me faster from all the test laps involved more than the advice itself, but when it clicks it does feel magical and really help.But sometimes I feel like I'm just speedrunning the collapse of 70s AI, as it feels a bit too brittle and situational.I also have added additional tools for tracking improvement across sessions, finding statistically problematic corners (where am I plain bad?, where am I inconsistent?) or even training my muscle memory by tracing fast driver brake traces using my pedal.Yay compiler:
The other ongoing thing is a clean room reimplementation of Jon Blow's Jai. I've been curious about the language for years, but it's a closed beta and for some reason I've never felt about asking Jon to get into it. I'm not really a game dev so I wouldn't even know what to put in the request.So now I have 100k+ lines of Rust that can compile a very significant subset of the publicly available Jai source code. I just used various LLMs to condense the public information about the language and come up with a dev plan and started chipping at it. Once I had something in a kind of working state I started with the Way to Jai big tutorial and make sure every example there compiles and works as intended, fixing errors or missing features one by one.I mostly use Claude Code or Codex, but sometimes what I do is having them guide me into the new feature and doing the edits myself while they explain, so I get to know how things really work under the hood.It's a silly pointless project, but for some reason I find very satisfying watching it compile the examples.

reply

embedding-shape

16 hours ago

 |
prev
 |
next

[–]

From another submission (
https://news.ycombinator.com/item?id=47738827
), there was a screenshot of Google Docs/Drive showing a popup saying "You cannot do copy/cut/paste with the mouse" whenever you try to right-click and copy.

Some months ago, I saw that very popup, and finally started working on something I've been wanted to do for a long-time, a spreadsheet application. It's cross-platform (looks and work identical across Windows, macOS and Linux), lightweight, and does what a spreadsheet application should be able to do, in the way you expect it, forever. As an extra benefit, I can finally open some spreadsheets that grown out of control (+100MB and growing) without having to go and make a cup of coffee while the spreadsheet loads.I don't really have any concrete to share, I guess it'll be a Show HN eventually, but I thought it was funny it was brought up in a similar way in that article as was the motivation for me to build yet another spreadsheet application.

reply

echo7394

11 hours ago

 |
prev
 |
next

[–]

Recently started a web design and IT consulting company called Opacity Tech with a simple goal, reasonable prices, and handwritten code. No AI agents writing bloated code, no template based site builders. Just real humans, writing real, optimized, fast code, using experience and knowledge, like the old days. Art used to be what we created with our hands, not what robots hallucinate for us. This from scratch attitude means we can charge less because we dont have to rent platforms or pay subscriptions for services or licenses. Real servers in house too, no cloud overlords.

reply

m4rkuskk

12 hours ago

 |
prev
 |
next

[–]

https://auxx.ai
 Yet another "AI CRM" Started over a year ago working on it part time. Its coming together.
https://auxx.ai

reply

echelon

10 hours ago

 |
prev
 |
next

[–]

A controllable filmmaking tool:

https://github.com/storytold/artcraftBefore anyone asks, I am a filmmaker and have made films for fifteen years. I'm building tools to help steer AI image and video generation.Here are a bunch of shorts made with the tool:https://www.youtube.com/watch?v=HDdsKJl92H4https://www.youtube.com/watch?v=ZThzgsdn1C0https://www.youtube.com/watch?v=P9N_umJY_1shttps://www.youtube.com/watch?v=oqoCWdOwr2Uhttps://www.youtube.com/watch?v=tAAiiKteM-UWe have a lot of users, and it's picking up steam.We're building BYOK/C and we're also building an OpenOpenRouter / OpenFal. After that's done, we're going to build an OpenRunPod.Anyone into films, AI, or infra that likes working in Rust should reach out!

reply

NeoInHacker

9 hours ago

 |
prev
 |
next

[–]

I'm working on the wolrd model action (WMA) model, which is used to replace Visual Language Action (VLA) model to bridge the physical world with LLM.

Now I've done my basic researching part, but I'm lack of the courage to dive into this topic. After all, it's a really hard work to it.So I'm just, you know, scrolling the HN and trying to sharpen my brain and get back to the work.

reply

boutell

14 hours ago

 |
prev
 |
next

[–]

I've been busy adding postgres and sqlite support to apostrophecms:

https://apostrophecms.comSix months ago, that would have been unrealistic, because we're heavily committed to the mongodb API and we make it part of our own API.Starting in December though, Opus 4.6 made it perfectly realistic to pursue this with Claude Code as a series of personal weekend projects.Now, despite not having any official resources on this until the last week or so, it should land in May.This doesn't work for everything. It absolutely helps that the problem I'm solving is an "adapter pattern" problem: "make X talk like Y." And that we have a massive test suite, at multiple levels. That combination makes "here's the problem, go solve it, grind until the tests pass, don't bother me for a few hours" a realistic AI agent request.But it's a little mind-blowing all the same. The hype around AI is so out of control, it can be easy to miss genuine "holy crap" moments.Along the way I've written a fair bit about how to run Claude Code autonomously on your household server in a reasonably secure manner:https://apostrophecms.com/blog/how-to-be-more-productive-wit...)Also general Claude Code tips and thoughts on workflows that help and workflows that ultimately just speed your burnout:https://apostrophecms.com/blog/claude-code-part-2-making-the...I know, everybody's writing this stuff, but the desire to share is natural.(Disclaimer: I'm part of the demographic AI was trained on. If I tried not to sound like a bot, I'd have to sound like... well, somebody else)

reply

chabad360

10 hours ago

 |
prev
 |
next

[–]

Finally starting a blog.

reply

NoMoreNicksLeft

6 hours ago

 |
prev
 |
next

[–]

I've forked Transmission, and I'm trying to implement mutable torrents. Some partial success between two hosts (seeder and leecher) on my own LAN, most of the UI stuff figured out. Will wait until I get it a little more solid before working on the Gtk, Qt, and command-line ports (I expect those to be pure interface work at that point).

reply

colechristensen

7 hours ago

 |
prev
 |
next

[–]

https://reader.fangorn.io/

Podcast and RSS readerSeveral other things, a CAD/CAM kernel with a Blender based frontend, a possibly novel strange attractor worth publishing, a git/CI host, an AI/LLM/VM cross platform workspace manager / IDE, shared multiplayer terminals in Minecraft and Godot

reply

oulipo2

14 hours ago

 |
prev
 |
next

[–]

We're building a repairable and fireproof e-bike battery at
https://infinite-battery.com
 :)

reply

aziaziazi

3 hours ago

 |
parent
 |
next

[–]

Great project ! I roamed your website and saw the fire test pack includes a venting valve but I don't see it on the 3D renders of the packs on sale. My armchair understanding is the test may not replicate what will happen with valve-less pack, may your share more infos on that?

Anyway I'll look into it when in need to expand/replace my bosch system. Kudos to your team to make the work more reparable :-)

reply

tayo42

15 hours ago

 |
prev
 |
next

[–]

Making 3d web games with webgl. And wondering if I should go all in on a career switch into digital art and 3d and leave software.

reply

EmanuelB

7 hours ago

 |
prev
 |
next

[–]

Solo project since 4+ years:
https://kastanj.ch/en?mid=hn47741527

The goal is to make every recipe foolproof on the first try, similar to when you walk into a restaurant and just pick what you want to eat without thinking about the details. The goal is to have the same experience, just pick what you want to eat, with recipes that tells you exactly what to do with no magic involved.Technically it is probably very different from other recipe apps. The database is a huge graph that captures the relations between ingredients and processes. Imagine 'raw potato'->'peeled potato'->'boiled potato'->'mashed potato'. It is all the same ingredients but different processing. The lines between the nodes define the process and the nodes are physical things. Recipes are defined as subsets of the graph. The graph can also wrap around into itself, which is apparently needed to properly define some European dishes in this system. The graph also has multiple layers to capture different relationships that are not process related.Why was it designed it in this way? Because food/cooking is complex to define. This design is the only way I have found that can capture enough of these complex relationships that the computer can also 'understand' what is going on.My favourite thing about this is that each recipe is strictly defined in the graph. If the recipe skips a step, or something is undefined, the computer knows that the recipe is incomplete. It won't ask you to do 10 things at the same time and then have something magically appear out of nowhere. It is like compile time checking but for recipes.It also enables some other superpowers, for example:
• Exclude meat part of the graph = vegetarian. Same thing works with allergies.
• Include meat part of graph = only show me recipes that contain meat.
• Recursive search: search for 'potato' and the computer will know that french fries are made from potato. It can therefore tell you that you could make the hamburger meal, but you will need to complete the french fries recipe first, which should take 60 minutes.
• Adjustable recipe difficulty (experimental): It knows which steps can be done in parallell, and which can't based on how the nodes connect. A beginner can get a slower paced recipe with breathing room between steps, while someone more experienced can do a faster pace and do more things in parallell.If I knew what it would take to build this, I would never have gotten started. I completely underestimated the complexity of the problem I was trying to solve. But here we are, and now it is basically done and working.The website captures the key points from a non-technical point of view, and you can enter your email and get notified when it will launch in your country.

reply

chabad360

10 hours ago

 |
prev
 |
next

[–]

Starting a blog

reply

contingencies

8 hours ago

 |
prev
 |
next

[–]

I am formalizing as patents a series of developments in drone delivery which stand to massively alter the status quo with respect to retail deployments. This, and a portable demonstration, are targeting fundraising for go to market on our autonomous restaurants, which have approximately 10 years R&D. I'm looking for $100M with around $30M spoken for. On that main business we are objectively ahead of all of the early stage players in terms of technology on footprint, automation level, and per site capex, plus will have far greater scalability. In other words, we stand to have a real, venture-scale return while the early stage players don't.
https://infinite-food.com/

reply

IAmGraydon

8 hours ago

 |
prev
 |
next

[–]

Learning audio DSP with Faust:

https://faust.grame.fr/

reply

brainless

8 hours ago

 |
prev
 |
next

[–]

nocodo: Sheets Driven Development

I think in this era of coding agents, more people feel empowered to build their own workflow automation. But for vast majority of non-technical folks, Claude Code or even Replit are not easy to use solutions. So I am taking inspiration from spreadsheets and using that as the primary UX to build a coding agent.https://github.com/brainless/nocodo

reply

dwa3592

16 hours ago

 |
prev
 |
next

[–]

Building a pro transparency writing tool that cryptographically proves a human actually typed what they claim to have written (research papers, news articles, assignments etc) . It captures behavioral signals during composition, makes it very hard to automate or fake the writing process, and lets readers verify authorship authenticity. Think "proof of human work" for the AI generated slop era.

reply

EPConsulting

12 hours ago

 |
parent
 |
next

[–]

Love this. My husband is writing a book and won't interact with AI cause he wants to be pure. I told him that soon there would be a premium on "only human" authorship.....like a small craftsman type mark of authenticity.

reply

dwa3592

12 hours ago

 |
root
 |
parent
 |
next

[–]

Thank you! that's one of the goals :)
I might reach out to you to see if your husband is interested in trying out the software for free.

reply

k2xl

8 hours ago

 |
prev
 |
next

[–]

I’m working on
https://chess67.com
, software for running over-the-board chess (clubs, coaches, tournaments).

I started this after volunteering at my kid’s tournaments and seeing how fragmented things are:
 • registrations in Google Forms
 • payments via Venmo/Zelle
 • pairings in SwissSys/WinTD
 • communication across email and textChess67 aims to unify that:
 • coaches can sell lessons and manage scheduling and payments
 • clubs can run events and communicate with players
 • tournaments can handle registrations, with pairing and USCF submission in progressStill early. The main challenge is not building features but matching existing workflows, especially Swiss pairings, which are more nuanced than they look.

reply

tonfreed

9 hours ago

 |
prev
 |
next

[–]

I'm working on moving as much as possible to self hosted options. Have forgejo, Authentik and Nextcloud set up so far. Slowly finding alternatives for things, I think my next goal is Nostr

reply

Joel_Mckay

9 hours ago

 |
prev
 |
next

[–]

Still working on a specialized slicer for a new 3D metal printing process. Mostly addresses material safety, model accuracy, and bringing technology within hobby budgets.

Also, cleaning up a microscope 4-axis micro-positioning stage project control-loop.Finding spare time to deal with a backlog of various other small projects. =3

reply

csomar

9 hours ago

 |
prev
 |
next

[–]

https://codeinput.com

2 products released (merge conflicts/codeowners) and now working on workflow automation. Basically trying to use Cloudflare Workers for a different paradigm of executing workflows instead of the traditional n8n VM.

reply

Uptrenda

9 hours ago

 |
prev
 |
next

[–]

I'm building v2 of the coffin API. It's an API that returns the word "coffin." I plan to eventually charge people to use this product and hope YC investors will be interested.

reply

adhamsalama

10 hours ago

 |
prev
 |
next

[–]

I'm working on a FOSS Web-based RSS reader for the Kindle that works on the Kindle browser, no need to send articles via Amazon or Calibre!

It's called Inkfeedhttps://inkfeed.xyzhttps://github.com/adhamsalama/inkfeed-reader

reply

jansan

13 hours ago

 |
prev
 |
next

[–]

A complex text shaping and rendering library in Javascript and no_std Rust that supports Ligatures, Bidi, Arabic, indic, CJK, Khmer, etc and is super small and memory efficient. JS version is <25 KB gripped, Rust version is aimed at approx. 130 KB compiled size. My plan is to show a demo of it running on an esp32 soon.

reply

nodesocket

13 hours ago

 |
prev
 |
next

[–]

Still very early, but I’ve been building Market Diary -
https://marketdiary.io
. Log daily market thoughts, document trades, and review charts all-in one place. Built for solo investors and teams who want to turn noise into alpha. Powered by Markdown, supports file attachment, teams, and TradingView charts. Free to signup. Would love feedback.

reply

GeoSys

14 hours ago

 |
prev
 |
next

[–]

I've been working on HODLings, a private crypto tracker, which doesn't track you!

https://www.geosystemsdev.com/products/hodlings/In essence, it runs on your mobile device and stores all your data locally. It only connects to the freely available CoinGecko API (for latest prices) and GitHub (for reference and historical data). A background job updates GitHub ref data hourly. There's no login, no cloud, no ads, etc.

reply

jedisct1

14 hours ago

 |
prev
 |
next

[–]

A new AI agent called Swival:
https://swival.dev

reply

cryptoz

15 hours ago

 |
prev
 |
next

[–]

AST-based code edits from LLMs:
https://codeplusequalsai.com

It's an LLM-webapp-builder, sure, but different from the rest! I have the LLM write python code when it needs to modify an HTML file for example (it'll use beautifulsoup; then I run the code: it parses the source into a data structure, modifies the data structure, and then outputs the resulting html).It's also a marketplace where you can publish your llm-powered webapp, and earn $ on the token margins (I charge 2x token rates) when people use your site.

reply

lam0x86

1 hour ago

 |
prev
 |
next

[–]

Yet another dual-panel file manager. FAR + vscode.
https://dotdir.dev/

reply

freshman_dev

10 hours ago

 |
prev
 |
next

[–]

minimal now pages via chat -
https://minnow.social

the Indie Internet Index -https://iii.social

reply

calvinmorrison

14 hours ago

 |
prev
 |
next

[–]

patching bash's interface because... why not?

reply

convolvatron

16 hours ago

 |
prev
 |
next

[–]

a soft-state filesystem cache and cluster control system that doesn't require any external orchestration or micro service infrastructure

reply

arionhardison

16 hours ago

 |
prev
 |
next

[–]

Codify — democratic digital public infrastructure that turns your problems into structured, executable programs.

The idea: describe any problem in plain language (voice or text), and AI codifies it into a structured program with the right people, steps, timeline, and agents to get it done. It's a 5-step wizard: Define Problem → Codify Solution → Setup Program → Execute Program → Verify Outcome.It runs across 50+ domains — codify.healthcare (EMR backend), codify.education (LMS backend), codify.finance, codify.careers (HRM backend), codify.law, plus 13 city domains (codify.nyc, codify.miami, codify.london, codify.tokyo, etc.). Each domain tailors the AI assessment and program output to that sector.The platform is Project20x — think of it as the infrastructure layer. If Codify is the verb ("codify your healthcare problem into a care program"), Project20x is the operating system that runs it all: multi-tenant governance, AI agent orchestration, and domain-specific sys-cores for healthcare, education, city services, etc.Every US federal agency and state-level department has a subdomain — ed.usa.project20x.com (Dept of Education), doj.usa.project20x.com, hhs.usa.project20x.com, etc. — with AI agents representing each agency's mandate. Same structure at the state level.The political side: Project20x hosts policy management for both parties — dnc.project20x.com and rnc.project20x.com — where legislative intent gets codified into executable governance through a 10-step policy lifecycle. Right now I'm building out the multi-agent environment so agency agents can negotiate with each other, make deals, and send policy proposals up to the HITL (human-in-the-loop) politician for approval. Each elected official has a profile (e.g.https://project20x.com/u/donald-trump) where constituents can engage and where policy proposals land for review.The name is a nod to structured policy frameworks, but the goal is nonpartisan infrastructure: democratically governed essential services delivered as AI-native social programs.Stack: Nuxt 2/Vue 2 frontend, Laravel 10 API, Python/LangGraph agent orchestration, Flutter mobile app. Currently live across all domains.https://project20x.com|https://codify.healthcare|https://codify.education|https://dnc.project20x.com|https://rnc.project20x.cometc...

reply

PKop

12 hours ago

 |
prev
 |
next

[–]

I'm building an immediate mode GUI Win32 app on top of Windows.UI.Composition visuals, maybe building up a library with it along the way. Just a hobby project / experiment. I hate this problem [0] so I went down a rabbit hole trying to solve it.

https://github.com/microsoft/microsoft-ui-xaml/issues/5148

reply

tonymet

14 hours ago

 |
prev
 |
next

[–]

A privacy friendly cloud storage manager like Windirstat for Google Drive & MS Onedrive

https://drivelens.click/No file contents are accessed, only metadata, fully client-side API calls (browser to google API).

reply

AndrewKemendo

13 hours ago

 |
prev
 |
next

[–]

givedirection.com

Direction - I’m trying to teach people how to do all the other stuff that you need to know, other than writing code, about delivering real products and not just a bunch of junk and slop that can’t be maintainedShowHN:https://news.ycombinator.com/item?id=47721469I’m also trying to make it really super simple so it’s week to week pricing, and have a discord community that grows out of it.It’s literally just four two hour courses on Monday of each week and a demo day.you walk through what you’re gonna do, how you’re gonna do it, how you’re gonna use your AI assistants to help you, where it can help you, and where it can’t help you, how to talk to it about teaching you instead of just doing it for you, and at the end of it you have something tangible to show for it.There’s no subscription this is just straight up teaching product and project development that comes with a community and the community grows as much as it chooses to.You can read the vision and roadmap on the site as wellhttps://www.givedirection.com/vision.html

reply

wangsj

10 hours ago

 |
prev
 |
next

[–]

https://github.com/vince-0202/acgo

Over the past few weeks, I have been building an AI coding tool in Go. The core loop is straightforward: accept a natural-language instruction, let the LLM interpret intent, then execute coding work through tools such as file read/write, code search, and terminal commands.As of now, I haven't come across any agent coding tools written in Go, but I have always thought that Go is an excellent language and is very suitable for building any CLI tools.Currently, I have added harness constraints to the agent by exposing hooks and implementing monitoring during the agent's working lifecycle. I think this will enable a clear division of responsibilities between the agent and the harness. The agent is the smallest execution core, while the harness acts as the execution agent for the agent and imposes constraints on its behavior.

reply

wangsj

9 hours ago

 |
parent
 |
next

[–]

Hope those who also like GoLang can join us as well.

reply

TimCTRL

14 hours ago

 |
prev

[–]

nothing

reply

Guidelines
 |
FAQ
 |
Lists
 |
API
 |
Security
 |
Legal
 |
Apply to YC
 |
Contact

Search:
