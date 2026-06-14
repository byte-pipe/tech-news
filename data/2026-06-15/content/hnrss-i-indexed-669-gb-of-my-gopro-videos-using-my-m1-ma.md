---
title: I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models | Hacker News
url: https://news.ycombinator.com/item?id=48528029
site_name: hnrss
content_file: hnrss-i-indexed-669-gb-of-my-gopro-videos-using-my-m1-ma
fetched_at: '2026-06-15T06:00:39.158617'
original_url: https://news.ycombinator.com/item?id=48528029
date: '2026-06-14'
description: I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models
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
I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models
149 points
 by 
iliashad
 
4 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
33 comments
TLDR: I had 2,207 GoPro videos, and I need to rewatch them to find interesting moments from my cycling journey. I built a project to index them locally on my M1 Max using open-source ML models, search for those moments, and send the best clips straight to my DaVinci Resolve timeline. I indexed 628 videos (668.68 GB, 15h 13m 18s of footage duration), more details in the metrics table in the last section of this article.

Full article: https://iliashaddad.com/blog/i-indexed-669-gb-of-my-gopro-videos-using-my-m1-max-computer

 
help

tontonius
 
1 minute ago
 
 | 
next
 
[–]

if anyone is interested in searching large video collections local and offline I suggest taking a look at Jumper 
https://docs.getjumper.io

comes with some nifty features like NLE- integrations, people search, MCP, API etcDisclaimer: one of the co-founders

reply

asenna
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Funny this is almost EXACTLY what I did a few days ago on the same machine using very similar techniques and was on the front-page of HN as well:

https://news.ycombinator.com/item?id=48222733https://blog.simbastack.com/indexed-a-year-of-video-locally/I wasn't familiar with your project though, interesting stuff.I'm trying to add more photography related features to Framedex but yeah there's so much we can do locally, exciting times.

reply

robrain
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

DaVinci 21 has indexing built-in (AI IntelliSearch). Not to diminish the work you did, but this is now available to many users (probably only Studio users since it has AI in the name)

reply

iliashad
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Yes, I didn’t look at it. But does it upload your videos to the cloud or process them locally? And does it allow to provide custom faces data to help labeling faces in your videos ?

I think Adobe premiere pro have it as well but cloud processed

reply

teovall
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The AI features in DaVinci Resolve are all processed locally. It does not currently have face tagging.

reply

robrain
 
52 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Haven’t tried it yet, and I don’t know if it matches OP’s requirements, but the blurb says “You can even search for individual faces”

https://www.blackmagicdesign.com/products/davinciresolve/wha...

reply

iliashad
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

That’s great to know, thank you!

reply

WarOnPrivacy
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I was surprised to learn that the

M1 Max CPU is an ARM/SoC, comparable to an 11th gen Intel i9Do I have it right? Would Windows ARM performance be similar for those cpu?ref:https://www.cpubenchmark.net/compare/4585vs4245/Apple-M1-Max...

reply

pachouli-please
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

It's also a bit apples (heh) to oranges for a handful of reasons, but most impactful

- "unified" ram makes all the system ram available as VRAM
- dedicated ai coaccelerator thingyBoth of these reasons allow the apple silicon chips to crush conventional cpus in these kind of AI model workload stuffsNo idea about what the windows arm stuff is capable of. I know they use Qualcomm snapdragon chips though.

reply

owldown
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

“Comparable” is maybe true if we are talking about single core performance, but for memory bandwidth, the M1 Max is about 8 times faster. Wider bus, lower latency, not even close.

reply

iliashad
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

To your question, I can’t deny or confirm that because I didn’t tried it this project over a Windows machine yet or a machine with this config

reply

Beijinger
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Does it work for porn collections too?

reply

pduggishetti
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

You'll need a lora for this, porn content rejection is heavy. Or you'll need a abliterated model, not sure if vision also works.

You might want to add something like yolo finetune to detect scenes + face recognition too.

reply

vorticalbox
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Vision still works perfectly fine in abliterated models.

reply

pduggishetti
 
46 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Never tried any of this for porn, just speaking out how I would go about it tbh!

reply

sarjann
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Asking the important questions

reply

fhdkweig
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The internet is for porn. 
https://www.youtube.com/watch?v=LTJvdGcb7Fs

reply

iliashad
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Why it’s always the same question? Hahah. I posted my project over Reddit and I got the same one hahah

reply

lifestyleguru
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Last time I tried whisper, it hallucinated an elaborate conversation from sounds of slapping and moaning and it took minutes to spit every single line of it.

reply

3eb7988a1663
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Parakeet has been trained to detect non-voice sounds and exclude that from identification, so you might have better luck with that family.

reply

supertroop
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Not sure if you’re being sarcastic but I think this is an interesting question. Would deep seek be useful here since it is local?

reply

fl0id
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

it is possible to use apple gpu with containers. either with podman + runkit + recent mesa or with recent vllm-metal from docker 
https://www.docker.com/blog/docker-model-runner-vllm-metal-m...

reply

iliashad
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

I was looking for a solution for this issue of running docker containers over MPS and utilizing their GPU power. I think this project will be the solution for it, I’ll try it very soon and add support for it. Thank you, much appreciated

reply

lgats
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

the link 
https://iliashaddad.com/blog/i-indexed-669-gb-of-my-gopro-vi...

reply

iliashad
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Thank you

reply

WhitneyLand
 
55 minutes ago
 
 | 
prev
 | 
next
 
[–]

I’d like to see embedding of actual video clips become practical in this type of workflow.

Frame level embedding it covering a lot, but can miss out on a lot of action related searches.

reply

rho138
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

This would fit most best as a “Show HN:” post :)

reply

culi
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

The title should link to the "full article". I wonder if OP's domain name is banned or something and they're doing this to get around it

reply

iliashad
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I tried to edit it and add Show HN, but it doesn't show the edited version. Thank you!

reply

iliashad
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I would love your feedback and suggestions for new improvements or features you wanna have, either in the source available version, the desktop app or blog post itself?

reply

nyxtom
 
13 minutes ago
 
 | 
prev
 | 
next
 
[–]

Now this ^^ is an awesome use case!

reply

m3kw9
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Grab frames, lower res, classify, combine meta data. Write to sql

reply

iliashad
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Not really. Grab frames, lower res, classify, combine metadata, transcribe the audio, convert those data (text, visual and audio) to embedding, save them over a vector DB and SQL DB. Which helped me to do semantic search, RAG, search using a screenshot of the video to find the exact the moment in the video plus search using an audio file as well. And other features unlocked with vector DB

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