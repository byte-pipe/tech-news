---
title: 'Ask HN: What was your "oh shit" moment with GenAI? | Hacker News'
url: https://news.ycombinator.com/item?id=48406174
site_name: hnrss
content_file: hnrss-ask-hn-what-was-your-oh-shit-moment-with-genai-hac
fetched_at: '2026-06-06T11:50:26.636745'
original_url: https://news.ycombinator.com/item?id=48406174
date: '2026-06-04'
description: 'Ask HN: What was your "oh shit" moment with GenAI?'
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
Ask HN: What was your "oh shit" moment with GenAI?
166 points
 by 
andrehacker
 
8 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
390 comments
Most of us were amused when DALL-E and its peers went mainstream, and we were quick to point out the obvious flaws.

Then ChatGPT hit the scene and again, many of us dismissed it as a parlor trick that would never amount to much.Using LLMs for coding initially was a only small step up from basic code completion, and a welcome farewell to Stack Overflow.I am curious: what was the specific moment that you went from those quaint, dismissive observations to a slightly panicked,
"Uh Oh" realization of what these models can do?

 
help

jzemeocala
 
4 hours ago
 
 | 
next
 
[–]

I bought an Alesis QS8.1 super cheap in perfect condition (was a top grade digital piano/synth in the 90s).

and then i realized that ALL of the software (which i collected from defunct websites and archived on github) related to it was ancient and after a while of getting tired of using WINE every single time i decided i wanted a cross platform modern equivalent that did everything that several of these different programs did (plus break out some stuff that was now potentially possible with modern computer)i thought it would be extremely hard because the computer to synth communication is pretty much only via sysex commands (of which the actual wave file encoding protocol was undocumented)Claude walked me through examining the some of the original software in GHIDRA, and I had a working demo that night.....now im just playing with adding new features to it.

reply

jsharf
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Related story, while applying a firmware update to my Kawai CA49 piano, I bricked it due to flashing the wrong file (The process was broken, and I got desperate and tried something stupid, which bricked the piano). Claude walked me through looking for signs of life, and since OTA from the phone app wasn't working for me, it downloaded the Kawai Android APK, decompiled the Java, figured out the hardcoded key used for encrypting the firmware update. Extracted the piano firmware update, decrypted it, and then wrote a flashing script to program the piano from my laptop via bluetooth. My piano was back to working within an hour.

reply

Galus
 
0 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's sick.

reply

gyomu
 
59 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes, those tools are extremely good at reverse engineering. With a bit of know how, it is now trivial to reverse engineer any protocol or crack any software, often in a matter of hours or less.

A lot of people in the industry have vested interests in this not being discussed openly so you don't hear too much about it, but the implications are huge.

reply

notagoodidea
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I would be interested to learn a bit more on the how after reading also [0] and the worlk done on patching the Ableton Move firmware with the Schwung [1]. Slightly different but there is an increasing amount of work done on either old hardware and new one exploring patching, swapping or developing new firmware from scratch thanks to LLM/GenAI currently.

[0]https://mforney.org/blog/2026-05-28-patching-my-guitar-amps-...[1]https://schwung.dev

reply

zellyn
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I had that keyboard! I actually really like the piano-ish touch. I remember being sad though, when I realized they’d crammed all the sounds into I think 16MB (or was it 8?) and realizing how bad that was even by the late 90s! I think I still have mine in the garage somewhere… good times!

reply

skhameneh
 
50 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Hey so... mind sharing findings? 
I have a QS8 :)

reply

itomato
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

While not the "oh shit" moment, the wave has the same shape.

I have an DigiTech GNX3000 effects pedal board - a digital modeling "workstation" that needs the aged Windows native software or Gdigi to make the most of.At best, the experience with gdigi was passable; raw access to the patches and controls, the ability to control it from the laptop, etc.In an hour or so, I had a functionally superior webmidi version up and running in Vercel using their v0 code. It kicked off a wave of subscriptions and referral chasing.I made it a template - because there are so many gnx3k users out there:https://v0.app/templates/digitech-gnx3000-sysex-tool-GC5LzXA...

reply

NoMoreNicksLeft
 
25 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

>Claude walked me through examining the some of the original software in GHIDRA,

I wanted to be able to decrypt the files on The Complete New Yorker magazine DVDs. The old software was WinXP only, and crashed by the time you turned to page 3 or 4. It walked me through using Ghidra on the relevant dll, mapped out how it was using Blowfish, what the credentials were that it was passing, and re-implemented all of that in a python script.Now all the files are in plain pdf.Right now, it's helping me write an extension to the mkv specification for embedded scripts and modify VLC to be conformant, so I can watch Black Mirror Bandersnatch. Already have a buggy implementation, about 3 days in.I've also had it add BEP 46 mutable torrent functionality to Transmission (and to some extent, to the WebTorrent library).These are all well beyond my abilities to do casually, and probably beyond my ability to do even if I spent the next 18 months doing nothing by grinding away at it.I only replied because I thought it curious that Claude apparently favors Ghidra.

reply

mekael
 
13 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Interestingly enough, i’ve been sitting on a project for the last 12ish years where i just took the FMloader lib and used that from C# to turn the djvu files into pdfs. All that was needed was a decompiler and an hour of banging my head on it. I published some of the results a few years ago but need to go back and actually build out a full app.

reply

NoMoreNicksLeft
 
4 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm trying to not do the naive pdf creation, where each page is just the raster. Trying to keep the JBIG2 bilevel, as I get better quality at lower file size. Using jpeg2000 too, where appropriate, but the pdfs are still x2.5 the size of the original. Though, I can have it spit out decrypted djvu files that are exactly the same filesize... I just don't like that format for archival.

If you want the Rolling Stone or Playboy archives decrypted, ReconSuave on github has tools to do those. I got tired of waiting for him to do The New Yorker though.

reply

djmips
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That's fantastic. Did you use a Ghidra MCP server? It's kind of magical huh?

reply

alright2565
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I've done a similar sort of thing with my camera lens' firmware updater just out of curiosity, and I didn't use any kind of MCP. It's able to write an automated script using the Ghirda API to decompile the program just fine, and then code exploration can be done by reading the code.

Claude needs good variable names a lot less than humans do, so renaming/typedefing doesn't seem to be as necessary.

reply

kstrauser
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I have a large token budget as part of my work. A coworker was scanning some repos for vulnerabilities as a test. He found a scary looking remote exploit in a popular project and shared it with me for a second opinion. I spun up a local instance of the project and ran the POC against it: nothing. Turns out it needed some configuration knobs tweaked to lower some security protections.

So I told the AI what happened, and asked it to fix the POC so that it would work with the default configuration. It chewed away at that for a few minutes until it cheerfully patched the POC into a weaponized version. I ran it. The local instance, which I had just downloaded, compiled myself, and launched with the default config file, immediately crashed.I got the cold sweats. I've read this novel. I've seen this movie. Wow. I have a blinking cursor on the console of a nuclear information bomb. I tossed and turned all night, got about half an hour of actual sleep, and probably looked like I'd seen a ghost at work the next day.On the plus side, it gave our team some very clear ethical and moral guidance: we're going to do this, and we're going to share our findings with the relevant authors, because we can. Because I want to live in a world where the good guys are trying to fix problems before the bad guys can find them, I decided to help build that world. It was like, well, I guess this is what I'm doing now.

reply

windexh8er
 
36 minutes ago
 
 | 
parent
 | 
next
 
[–]

And written with AI.

reply

kstrauser
 
25 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

What was?

reply

MassPikeMike
 
13 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

These days when people see consecutive pithy sentences with parallel structure, they immediately holler "AI generated."

For years I've wanted to improve my writing and reduce my tendency to string together long floppy clauses, and now I'm like, well good thing I never did that...!

reply

jp57
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Actually seems absurdly simple now, but sometime last year I was trying to figure out what I'd need to tow my daughter's car cross country with my truck: what are the trailer/dolly options, what do they cost, can my truck actually tow the combined weight, etc.

I started out prompting ChatGPT kinda how I would with Google, one small prompt at a time, asking about various details. But after one or two of those I just tried "I want to tow a car of make A with my truck model B, from point C to point D, what are my options?" And it wrote me a report with comparison tables and computed towing weights and other details for different options.At that point, I was like "Oh. This is different. And it's just the beginning."

reply

SamuelAdams
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Similarly, I used gen ai to review a real estate purchase. I provided Zillow listing photos and serial numbers of all appliances, the electric panel, and a few additional not pictured areas that I took during the walk through.

I prompted the AI to write a report as if it were a home inspector and it actually did a better job and identified some issues the paid 750 usd inspector missed.

reply

j_bum
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

From pictures alone? What are some examples?

reply

bombcar
 
49 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I presume something like this: 
https://www.penny-arcade.com/comic/2007/06/22/perfectly-reas...

reply

SamuelAdams
 
23 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It noticed a flooding area due to low grass by the walkout door. It noticed mixed 15 and 20a receptacles on the same circuit. It noticed warped siding and recalled circuit breakers still in use.

reply

flyinglizard
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It very plausibly might have been totally wrong.

Out of laziness I several times asked Claude and ChatGPT each some torque figures and other simple, hard data related to my dirt bike. They often got it completely wrong, but full of confidence every time. I never trust LLMs with hard data, unless you RAG the PDF into the context and even then it's sketchy.

reply

glouwbug
 
8 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Hard numbers, no. Even high level concepts and theory you need to triangulate and prompt in different angles, across different models, and figure out what overlaps to build a mental mode that’s - even then - roughly 80% correct. It’s better than google, but the information isn’t free

reply

andrewthornton
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

My furnace went out during the 2025 holiday and I couldn't get an appointment with a repair person for 2 days. It was getting very cold in my house so I went into my attic and made several videos of the furnace attempting to start and gave it to gemini. It diagnosed the issue immediately and had me spin one of the components (a small exhaust fan) while the furnace tried to fire. It came on immediately. I had to do that several times, but it worked until the HVAC service showed up.

reply

brntheater
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Had something similar this week. Gas dryer started, but wouldn't heat. Gemini suggested it's often a thermal fuse. Took off the back panel and uploaded a photo to Gemini. It pointed me to the fuse (e.g. "the white rectangle above the blue and red cords") and walked me through testing it. Not only that, but it also linked me to the part I needed after I provided the model number of the dryer. Finally, it recommended cleaning out the vent as the fuse likely blew because heat wasn't venting properly. After a thorough cleaning of the exhaust and a $5 fuse the dryer is working fine.

reply

jodacola
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Very similar thing this week, and an interesting story to go along with it!

I called my normal HVAC company for my rental home because the tenant reported the AC wasn't cooling the house. When I called, I got one of the latest AI voice assistants to help me, and it was an awful experience and I ended up not hearing back after the assistant told me the office would call me back.So, I went over to the house and used ChatGPT to help me diagnose the issue by taking some photos of the compressor panel outside. It walked me through what to check, I provided some diagnostic codes I witnessed... and it walked me through the very simple repair of replacing the $25 capacitor. It was going to cost me almost 4x that just for the service call to diagnose what was wrong in the first place.So, the weird experience was: Gen AI made me lose trust in my normal HVAC company, and more Gen AI basically allowed me to replace my HVAC company and do the repair myself all in one day.

reply

tonyedgecombe
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I've been fitting a kitchen and chatGPT has been useful to bounce ideas off and resolve issues. Of course if IKEA's documentation wasn't so sparse I wouldn't need it but that's another story.

I guess I'm seeing similar benefits to a novice programmer. Professionals would scoff at my work but they are expensive and difficult to work with. Meanwhile I'm getting the job done.On the other hand I'm not touching AI for any development work. I'm too worried about my skills atrophying or not properly learning anything new.

reply

rustyhancock
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ikeas instructions are such an oddity.

It feels like there is precisely enough information to deduce each step. But only just enough miss one clue and you have something on upside down on step 7 that you won't notice until step 37.I feel whoever makes them could probably make a wicked NY Times Crossword puzzle.

reply

dgemm
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Similar - had an HVAC tech out to diagnose mine (some intermittent electrical problem was killing thermostats randomly) and since it was intermittent they couldn't figure it out. I ended up using Gemini to narrow down a list of potential problem components and just replacing them all which fixed the issue.

Kind of a superpower to turn anyone with a bit of tech inclination and problem solving skills into an HVAC tech - not a very good one, but one with enough motivation to get the results you need

reply

ssl-3
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That's pretty great.

(Though that's also the kind of hands-on troubleshooting step/fix that a person could just google for and find pretty easily back before the internet got all fucked up.)

reply

Cheetah26
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Your parenthetical really describes my experience with AI searches. 5+ years ago I could find most things within one or two quick searches, now it takes so many that of course I'm going to reach for AI because that's the only way to get back to my baseline efficiency.

reply

alberth
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Do you mind explain more. Did you just prompt to Gemini what was happening, did you give Gemini photos of Furnance, etc?

reply

gwbas1c
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> and made several videos of the furnace attempting to start and gave it to gemini

I assume recorded videos and uploaded them in the Gemini phone on their app; and then probably said "what's wrong?"Gemini is very good at those kinds of things. I recently got some ratcheting straps and needed to use them, but at the time I didn't know what they were called, so I didn't know what to search for on Google. I opened the Gemini app, pushed the button to take a picture (just like in text messages,) and included a message that was similar to "what is this and how do I use it?"

reply

andrewthornton
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes, here is my prompt. It also contained a video: "I have a furnace that will not heat when I reset the power to this unit. It makes some noise within its fan system for about three or four minutes and then I get an error light. Can you help me figure out what may be wrong here?" This prompt is not the best but I was freezing and in my attic.

reply

wombat-man
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Oh yeah. I can't remember which LLM, but one helped me repair my dryer.

reply

buckle8017
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Gemini almost killed you.

The exhaust blower not working triggered a safety that prevented the furnace from firing.Spinning it bypassed the safety.You likely inhaled a lot more carbon monoxide than you know.

reply

llbbdd
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Can you elaborate? I interpreted the same as the other comment that the blower fan just needed a hand start and kept going after the furnace started up. What you're saying only makes sense to me if the spinning the fan by hand allowed the furnace to start by bypassing the safety at startup, but wouldn't that mean that if the exhaust fan was stopped during normal operation (blockage etc) that the furnace would just keep going, dumping CO into the home?

reply

andrewthornton
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It wasn't bypassing, I was just helping start because of what I believe to have been a bearing issue.

reply

doubled112
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It’s a pretty normal trick to try while troubleshooting a rotating part.

Helping something start is not likely to ruin your day (unless you get caught in a rotating part)

reply

andrewthornton
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I was spinning it in reverse actually, but it would be enough to start the exhaust blower. It would also re-start pretty well for ~6 hours. It was probably the bearing. Also FWIW I have multiple carbon monoxide/air quality monitors and nothing tripped or alarmed.

reply

philipkglass
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

From the description I thought that a degraded capacitor or lack of lubrication made the blower not start on its own, but the blower (and the whole furnace) would work if given a manual startup spin by hand.

reply

pesus
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Welp, AI almost killing someone is definitely an "oh shit" moment.

reply

shreddude
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I could go on and on, but Claude recently decompiled the firmware of my camper van, documented all the CAN interfaces, then programmed an ESP32 module to talk to the van’s integrated systems (power, HVAC, lighting, tanks). That sort of embedded systems integration is completely out of my wheelhouse.

I honestly don’t understand AI naysayers. I use Claude every day both professionally as a Solution Architect and personally in a variety of projects I simply could not have ever approached alone.

reply

williamdclt
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

> projects I simply could not have ever approached alone.

I think that's part of the divide between enthusiasts and naysayers. If you use GenAI on things that you couldn't approach alone, it's an incredible tool. If you use it on stuff that you're pretty good at, it's not a gamechanger (and if you're an expert, it's a minor boost at best). Many people's job are about doing what they're an expert at.

reply

LouisSayers
 
21 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I find it's a huge boost for my day-to-day work.

If you work on architecture and Claude docs, then you can essentially just have it fill in the gaps. Work then mostly becomes a matter of defining what the next piece of functionality is (which you can also use Claude to help with).The stuff that used to take days now takes hours. It's not perfect, but if you get your codebase into a good shape then the payoff is huge.

reply

dawnerd
 
50 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

And in a team setting it can really accelerate tech debt especially if used by people that know just enough to be dangerous.

reply

jesse_dot_id
 
46 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Same. I'm a DevOps engineer, so a jack of all trades master of none type of guy, and Claude Code backfills my knowledge gaps and turns me into kind of a superhero. I think it's key to already have a pretty good idea of what you're looking at, though.

reply

archagon
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[3 more]

[flagged]
donkey_brains
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Just as bad as the technical debt is the cognitive debt in your codebase. When something breaks, your only recourse is to ask the AI how to fix it, since it wrote it and you did not have time to review all of its code. Except now the code base is so large it won’t fit into the context window, and the AI can’t help you, and…you’re screwed.

reply

shmoogy
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If you're vibing such complex things you should probably be in the habit of also generating detailed documentation and commits so the ai can follow breadcrumbs, add some playbooks for how to debug and it's actually pretty good. Too complex for local models context though - so you're probably still correct albeit there are ways to mitigate or delay this.

reply

rvnx
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[16 more]

I get it understand either. "This is just a stochastic parrot".

I suppose these people are lying so that they can justify their well-paid job, or they just don't know how to use LLMs or to prompt GenAI tools.

reply

camel_gopher
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It’s a probabilistic parrot

reply

foobarbecue
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

What's the difference (stochastic vs probabilistic)?

Or... were you illustrating?

reply

jazzyjackson
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I’ll explain it: these tools are non-deterministic and people have different experiences with them. For a few people every interaction is totally fumbled and they think the cheerleaders of gen AI must be lying, for others the chatbot hits one home run after another and lets them add microcontrollers to their CAN bus. When these people’s good luck runs out and they start getting mixed results like the average user, they assert the service must have been down graded

reply

triMichael
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'll add to that: you are more likely to have a good experience if it has a lot of relevant data that it was trained on. You are also more likely to have a good experience if errors don't cause major issues.

So one-shotting a game of Snake should be great (tons of training data, errors are easily caught because it's a small program). Similar with building a lot of web UI front end, or one-shotting a personal project. On the other hand, I haven't been convinced that it's good enough to maintain large codebases or assist with niche topics that are not very well documented.

reply

thewebguyd
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> if it has a lot of relevant data that it was trained on

This became evident to me the moment I tried to have these models work on some PowerShell tasks for me. Even Opus today struggles with PowerShell.Since anything in PS is probably some internal sysadmin tool, there's not much public code out there outside of Microsoft's documentation. Plus the Verb-Noun naming scheme makes itreallyeasy to just hallucinate cmdlets (which it does, often). Its easier to have the LLM just do things in python using M365 Graph API than any of the provided PowerShell cmdlets.OTOH, I've been using Claude for a lot of Swift & Swift UI work lately and it has no problems there, and I'd imagine there's even less publicly available training data for that so to be honest I'm not entirely sure why it fails so badly at powershell.

reply

lowbloodsugar
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> On the other hand, I haven't been convinced that it's good enough to maintain large codebases or assist with niche topics that are not very well documented.

Same is true of humans. So far my experience is that addressing the issue with the help of AI is faster than not (ie comprehending the system and creating the documentation).

reply

cauch
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don't understand the comments of the kind of "same is true with human".

This feels a bit like whataboutism.It also feels like people don't listen to each others.For example, reading the previous comment, it feels like the thing that reduce the enthusiasm was that at first GenAI looks like it was "reading, understanding and using its own knowledge to answer the problem", but as soon as it is a ore niche or a more complex situation, GenAI looks like it "does not understand the code, just does the equivalent of a StackOverflow search and try to apply the solutions that it found there, and this is why it felt like it understood the code before".It does not at all means that GenAI is not terribly useful. And even better than humans in some situations.But it feels that answering "same with humans" is missing this point: that's the opposite, humans usually try to understand the code and are bad at covering a very large range of very well documented subjects. That's the "uncanny valley" they talk about: they assumed GenAI performance on a subject X is due to a "human-like" approach, and it feels very strange when this impression falls apart.

reply

dyauspitr
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I still don’t get it I can dictate a prompt and sometimes I do it so quickly the text looks like a drunken parrot dictated it and it still 
always
 gets exactly what I’m asking for. I’m just going to attribute malice to the naysayers.

reply

bonoboTP
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Some people are really bad at specifying what they want to ask for. Or they already start prompting with the attitude that it can't possibly work so they don't even really try, or stop at the first failure to point and say how bad it is.

reply

thewebguyd
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

People are 
really, really
 bad at specifying what they actually want. I've worked in IT for my whole career, starting in help desk (now an IT manager). My days in the service desk was enough proof that people have no idea what they actually want, or at least, they really struggle to articulate it into words.

It's the famous "email broken, fix pls" but in the form of an LLM prompt.

reply

bonoboTP
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Well, today's multimodal llm agents with tools would at least have a good chance to do something with even such an underspecified query. Because fixing things is simpler to specify, the agent could look at config, network settings, send a test email, take a screenshot etc and get a good idea of what's broken. But when you want some new feature or new app, you can't do without actually asking for specifics, or at least you shouldn't complain if it didn't read your mind correctly. Or at least accept that you have to iterate. I think many average people can get this if they are motivated, and they can incrementally say what they don't like even in vague terms and it can get better. But some just stop without trying to ask for changes.

It can be frustrating to observe people interacting with these things. But it was just as frustrating 20 years ago, so maybe it's just a constant.

reply

rvnx
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Similarly, doing service desk, the thing that makes me flip the table is how people start by explaining what does not work, instead of explaining what they are trying to do.

reply

bonoboTP
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's hard even at the highest levels, such as in writing scientific papers or doing scientific conference talks. People just generally have a hard time to step outside of their context and think with the head of someone who has a different set of facts and assumptions in their context. It's hard to know how much context you both share, and how to tailor the explanation so you also don't start from Adam and Eve but you explain just enough context and strip irrelevant tangents.

I don't think this is just about intention and willingness, it's just simply hard.

reply

skydhash
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Or maybe people see how complex the code is and all the failure points, and don’t feel it’s ethical to use the output. In most of the comments, the most relevant point is that the poster is not an expert in the domain they got helped. While they can observe the result, they don’t have a causal model of the situation.

reply

amelius
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I still would like to hear a public apology from the stochastic parrot crowd for their deceptive framing. Or maybe it was just incompetence.

reply

niwtsol
 
8 minutes ago
 
 | 
prev
 | 
next
 
[–]

To share something different, it is less about what I have built, and more about what I have seen my friends (non-technical and technical) build. In a one month span I have seen a lawyer make a personal red line tool, a sales guy make a custom website for a golf trip, another friend make a 3d printing grid-finity project, a friend make a stl file to print a jig for his table saw, and another friend make a full mobile game. It is just really cool to see these micro-projects be created and shared, not only for the utility, but just to see my friends' childlike excitement showing off their project.

reply

UncleOxidant
 
7 minutes ago
 
 | 
prev
 | 
next
 
[–]

I guess I've had several of those moments over the last year and a half. But a recent one was that I was working with Claude to create a spiking neural net MNIST classifier in an FPGA for a demo. Claude took it from concept to PyTorch, to training (training a Spiking neural net isn't necessarily straightforward - that's a whole post in itself, but Claude came up with a working solution), and then to implementation in Verilog and through synthesis into the FPGA. I asked Claude to create a drawing app to run on the PC side that would allow the user to draw a digit with a mouse and then click a classify button. The data from the digit drawing app was to be transferred via USB to SPI to the FPGA. I didn't have a SPI adapter yet (it was on order from Adafruit) so I asked claude to let me communicate with the simulated verilog code running in the Verilator simulator, through a virtual SPI interface. Then I went to lunch. I came back to see the digit drawing app displayed on the monitor. I drew a '2' and it classified it as a 2. In another window I could see the Verilator simulator running and the data being passed. Chills.

reply

AussieWog93
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Literally just last night I have Claude Code the following prompt, verbatim:

"Whenever I launch Kodi on my Chromecast 4k, it crashes. I think this is 
 related to a plugin or skin. It goes away for a bit if I clear cache but 
 will eventually come back. Can you connect to the device via 
 adb (I've run adb connect already), and debug exactly where it's crashing? 
 Once you've done that, propose a solution. If this requires downloading, 
 fixing, rebuilding and then uploading the broken extension via adb, don't be 
 shy. I should have Android dev tools (Gradle etc.) on this Mac."Lo and behold, without human intervention, it pinpointed the crash, downloaded the Kodi source, patched out a bug that had existed since 2016, recompiled it, signed it, then pushed it to my Chromecast all while carefully making sure to keep all my settings intact.Got it to make a PR too (which is as of this moment unpublished; going to test more over the coming weeks).

reply

calf
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

That's amazing, as someone who struggles to find something useful to do with LLMs. How long does this take, several minutes or more? Do you need a paid version of Claude Code for this?

reply

AussieWog93
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It sat there for about half an hour working out the problem, step by step, before asking me for the preferred solution. At one point, it was trying to decompile the .APK, so I interrupted it and reminded it that Kodi was open source - it was welcome to clone from GitHub.

The only other feedback I gave it mid-process was wrong (I said that the crash probably wasn't caused by cache trimming, it ran some additional tests to confirm that its hunch about cache trimming was right).This was with the paid version of Claude Code (I don't think they offer a free version at all; that's a Codex thing). The $20 version is as smart as the $200 one, but once you work out it can do stuff like this you'll quickly burn the $20 token limit. :)The other thing that helps is a CLAUDE.md file - authored of course by Claude itself.
Mine's here:https://github.com/EspoTek/.claude/blob/master/CLAUDE.mdA lot of it is probably domain-specific for the stuff I do, but the "Working with unfamiliar data or systems" section is bloody gold! Stopped the bullshit completely!

reply

segmondy
 
25 minutes ago
 
 | 
prev
 | 
next
 
[–]

Running local LLM in 2023 and I heard folks talking about interfacing LLM to tools. I wrote a system prompt and told LLM it can call some tools. If it wants to call a function to output func(params...) and do so in an XML tag. I provided a few examples, none of this JSON soup we get today. Then told it I'll provide it the result in a RESULT XML tag and it should use that to answer. Wrote up a harness around that and I had a local model interacting with the outside world. Oh wow! Everything else today about MCP, Agents is all an extension of that thought. Using function calling, I built an agent. I defined a data structure that represent rooms and how they are connected. The room will be marked as dirty or clean. Then I would place the agent in a room and the agent will decide if to go left, right, down or up and into a room. Once it got into a room, it would decide if to clean it or go to the next room. Repeat until all rooms are clean. Basic toy of CS101 AI vacuum agent. It worked!

So being able to get real world input/output to the model and having the model being able to make decisions in a loop and to be able to do it locally. I have been screaming like a mad man ever since.

reply

evdubs
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I tried to see if an LLM service provider could rewrite some legal docs where nothing was hallucinated in order to follow a consistent format to see what may be missing in the document. It could do that.

Next, I wanted to see if this could be done with a local LLM. Gemma-4 handles this fine with an 8GB video card and a large context (128k).Next, I wanted to see if the model could also OCR these docs and translate them. The same model can handle that quite well.This was when I realized LLMs should be great for handling work where:- I already know what I want to do- I already know how to do it- I don't think this task will help develop skills I find to be valuable- If I have to do it manually myself, I will probably cut cornersSo now I view LLMs through the lens of, "what work can I send to an LLM that I otherwise would not really care about doing."

reply

SoftTalker
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Yes, the best results I've had using LLMs are for tasks where simply reading and reformatting/translating/summarizing are the goals. They are much faster and less prone to boredom doing these things than humans are. For now.

reply

gscott
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

My son is in a lawsuit with his bank where they put through fraudulent charges and wouldn't charge them back then the bank sued him for the money. He is using Claude and Gemini fighting the original lawsuit and now has a counter-suit 100% using AI for everything. He puts it into different AI's to check everything against each other and to come up with more ideas. He started with ChatGPT, moved to Grok, then Claude, but now Gemini is turning out to be the strongest.

reply

kstrauser
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm about as pro-AI as anyone here. I say this with love: anyone using general-purpose, consumer-grade AI for healthcare, law, or taxes is mad. Best wishes to your son, bless his heart, but 
please
 have him consult a qualified lawyer before showing up to court with model-drafted legal documents. Among other things, those chats are not privileged information[0] and the banks could subpoena chat transcripts to see what else he might have told them.

[0]https://natlawreview.com/article/new-york-court-rules-ai-doc...

reply

gscott
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

He has had multiple hearings and the Judge has reviewed everything. The court clerk reads every submission and before the clerk puts it in the system they have a in-house lawyer review each document. This is pretty far along. The trial is scheduled for October of this year.

The bank has a lawyer, they were hoping for a default judgement because who can afford to fight the bank. The choice is fight it yourself or declare bankruptcy.As you already know, AI companies trained on every single document they can find. Those include legal documents. The legal system is structured where you have Federal Laws, State Laws, Federal & State Regulations and Court Precedent. Because of this structure it is not difficult for a LLM to figure out.

reply

bombcar
 
38 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The only way to "win" as a small is to be 
pro se
 and be extremely diligent in understanding what is happening.

Then, it costs you nothing but time.

reply

jasondigitized
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This. I know how to do this but I don't have the time/energy to do this. "Get me Claude!"

reply

mindcrime
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I don't remember one specific moment, but I was fairly impressed with ChatGPT from the first time I started interacting with it. Was I ready to call it "AGI"? No, absolutely not. But it was clear that it was 
something
 new, and it was also intuitively obvious to me that "this AI is as bad today as it will ever be" and that predicting the rate of change would be difficult.

The more I use these things, the more I'm 100% convinced that it makes sense to say they are "intelligent" (for some meaning of "intelligent"). AGI or "human level intelligence"? Still no[1]. Butsomekind of intelligence. And I'm quite happy to allow that there can be "intelligence" that doesn't work anything at all like human intelligence, so arguments of the form "this isn'trealintelligence", etc, etc. carry very (very) little weight with me. I've actually been sitting on a half written blog post on this very topic for a while, titled "The Marquee Sign Says 'Artificial' Intelligence"[2]. Finding time to finish it has been the challenge.And before somebody says "Use AI to write it for you". Nah. I am generally what you might call "pro AI" and / or an "AI enthusiast" but I still draw lines. I'll use AI for research, for outlining, for brainstorming, etc. sure. But I have a hard-line stance against letting AI fundamentally write for me. I want anything that goes out with my name associated with it to have my genuine voice.[1]: I like the term "jagged intelligence" that Demis Hassabis has been using. That is to say, the bounds of the intelligence are jagged or spiky: very intelligent in certain areas, much less so in others.[2]: for any old-skool pro-wrestling fans, yes, that is an intentional nod to "Double A" Arn Anderson and his "The marquee sign says 'wrestling'" catchphrase. :-)

reply

CompleteSkeptic
 
23 minutes ago
 
 | 
prev
 | 
next
 
[–]

I helped train some of the first "magic" models at OpenAI[1] and it was a wild ride. We were a pretty sane + skeptical team and we weren't totally convinced the models were as general as they seemed, but the query that convinced me (and later got included in the paper[2]) was "Why is it important to eat socks after meditating?" (something that almost certainly did not appear on the internet before).

An interesting follow up would be when did you realize GenAI wasn't as good as you thought in that "oh shit" moment[1] co-author of InstructGPT/RLHF/ChatGPT[2]https://arxiv.org/pdf/2203.02155

reply

PopePompus
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I had an old astronomy app I wrote for pre-iPhone app store era Nokia phones (N900 etc.). I decided to get Claude code recreate it as an Android app. The old app produced several display pages for things like the positions of the planets. I was having Claude code recreate the app display page by display page, describing the display that should be produced, with no reference at all to the original app's code (or even its existence). After having it reproduce several pages, it added another one unprompted. The page it added was in the original app, but I had not gotten around to adding it to the Android app. The Nokia app's code is still on github, and somehow Claude must have made a connection between what I was asking it to code (without ever mentioning the Nokia app) and my github repository's Nokia code. It correctly implemented the page without me even mentioning the missing page. My jaw hit the floor.

reply

simonw
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

ChatGPT Code Interpreter back in ~March 2023. I uploaded a CSV file (of police incidents in San Francisco) and watched it load that into Pandas, show me some charts, then export the data to a SQLite database file for me to download.

I write software for data journalists and this new thing appeared to be able to do everything I wanted my software to do just as an unplanned side effect of having the ability to run Python against a folder with some uploaded files in it.With hindsight it was my first exposure to a coding agent, but we hadn't named the category at that point.

reply

vitorbaptistaa
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I am the CTO of a small NGO (10 people total, only 1 other junior Dev at the time). We supported two apps that were built by consultants. They were a mess. NextJS, React, about 4 micro services for a site that had 50 users per WEEK.

I configured a devcontainer with the old codebase and an empty repository and asked Claude to rewrite it as an old school server side rendered Django app.Went to sleep. When I woke up it was 80% done. Spent another couple days prompting and reviewing and reached feature parity.A bit later did the same with the other app.Now both are deployed, reduced the server costs, complexity, and are orders of magnitude faster.Without AI agents we wouldn't be able to do so (as usually is the case with tech debt).AI is amazing for small organisations!

reply

vishvananda
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

For me it was earlier this year when I started dusting off some old stalled projects and had an agent work on them. In a few days I:

* Built a clone of the Alpha Zero implementation[1] my team built at oracle* Ported my hobby NES emulator from javascript to rust[2] (this actually took less than 30 minutes and worked on the first try)* Implemented all of the lessons from the C++ Grandmasters Challenge (which eventually led to a complete c++ compiler[3])The thing that flipped the switch was using it to build things that I actually put sweat-equity in to previously. I knew how hard these things were to build, so it landed in a way that other projects had not.[1]:https://medium.com/oracledevs/lessons-from-implementing-alph...[2]:https://github.com/vishvananda/popeye[3]:https://medium.com/@vishvananda/i-spent-2-billion-tokens-wri...

reply

alexfoo
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Someone in the house pressed the button to update the printer (Brother DCP-L3550CDW) firmware and the CSV page that was the basis for an existing Prometheus exporter (drum/toner lifespan, page counts, etc) stopped being a thing. Instead there was an HTML page with all of the information buried in various divs/etc.

I'd planned on writing something myself to parse the HTML and write a suitable exporter but I thought I'd give Claude a chance.In a sandboxed VM I gave Claude a single static HTML file of the status page from the printer, also in the directory was the equivalent of "hello world" in Go, literally just the minimum needed to do `fmt.Printf("OK\n")`. The directory was called `brother-exporter`. That was it. No other instructions or information. I hadn't told it what it needed to write. I hadn't said what it should do. I hand't told it what language it was supposed to use.Just by doing a `/init` in that directory Claude decided that it needed to write a Prometheus exporter in Go that would fetch and parse the HTML file from a printer (defaulting to 192.168.1.1) and then present the associated metrics in a way that they could be scraped by Prometheus.It did this flawlessly in about 10 minutes.I could have done it in several hours but this was definitely an "oh shit" moment for me. I think the biggest thing was the fact that it guess/assumed so much (correctly) from so little information in the beginning.

reply

mlmonkey
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I have a buddy who's a consultant. His niche area is Netsuite and Oracle (I think). He's an accountant by training and as a consultant his gig was setting up these instances for clients, charging them an arm and two legs. He'd spend a lot of time golfing, and doing these setups was more than enough money for him. In other words, he had cornered that little slice of the market and was making bank.

Shortly after ChatGPT 2.2(?) came out and hit mainstream, I was chatting with him (I was excited af about the possibilities of AI). He tried to pop by bubble by saying "I bet it can't do what I do for my job!".So I decided to test it out. We went home and I pulled out my laptop. Went to chatgpt.com and then I asked him to enter the specifications of what Netsuite configuration he wanted. So he proceeded to type in the description of what he wanted, the various settings, configurations, etc. i.e., the specs that he typically gets from his clients. And asked it to give him the commands to set it up.Lo and behold. ChatGPT came back with a series of commands that he needed to run; the options he needed to configure, etc.He was crestfallen. "Those are the exact commands I run!"Luckily for him he recovered. He has since settled on a small stable of clients, all privately held companies whose owners he knows and between them he makes enough to keep his golfing hobby fed.

reply

reactordev
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Sometimes it's the service you provide, not the value. They know it's in good hands, as it's always been (even if they could have rolled their own ConsultBot 2.0)

reply

bonoboTP
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I have some friends who, since their high school days help some older acquaintances in upgrading their PCs, choosing laptops and phones, helping with setup etc and these older folks have comfortable money and pay him very well above what would seem reasonable. But the trust and years long relationship matter to them.

Llms are great today for buying advice but there are some incentive issues for the future, ads etc. But in some cases the human contact will remain important. In large corporations it's also similar. The money is peanuts either way, and it's worth them for the peace of mind. But this may not hold forever, especially if the more AI literate generation gets to more senior positions.

reply

takee
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I was working on a science experiment (electromagnetics) with my 10-year-old kid that was going to be demonstrated at a science fair in his school. We ran into a hiccup with the experiment that we couldn't debug ourselves. I turned on Gemini live video call to help us root cause the problem. It was able to clearly articulate all the possible issues and eventually was successful in making our apparatus work as expected. Turned out the wire that I was wrapping around the screw had some insulation that was not scraped off well on the side it was connecting to the battery. Gemini was able to capture this detail even though my bare eyes could not. My kid and 2 of his friends were impressed not just by the experiment, but because the live audio/video back and forth we had with the AI was almost magical!

reply

foobarbecue
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Neat, but I'd bet it was "guessing" that rather than actually seeing it.

reply

ckorhonen
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If it’s “guessing” correctly 95% of the time, is that meaningfully different from “seeing” it for most practical purposes?

reply

foobarbecue
 
58 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I just mean that the image input probably didn't affect the output at all. Could have just told it "I'm an amateur doing bulbs and batteries and it doesn't work" and it would give the #1 search result on forums for that which is "did you strip your wire."

I feel like I'm in the audience at a magician show, except most of the audience is breathlessly amazed and doesn't understand how easily tricked they are.

reply

bonoboTP
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

The big one was definitely ChatGPT upon release in 2022 and specifically when people showed how it can role play as a Linux terminal and you can narrate events like "the data enter is now on fire" and "run" nvidia-smi, it would show high temps on the gpus etc. Or you could "explore" the homedir or some famous person. It convinced me that if it can understand so well how terminals work, tool use and agents are around the corner.

Then Opus 4.5 convinced me that this has finally arrived. In 2022 I expected things to arrive faster actually, in 2023-2024. I expected we'd have much more realtime collaborative integrations with AI including GUI computer use. Maybe in 1-2 years.For images, it was nano banana where I realized AI images can truly work, and all these adhoc issues like hands and limbs, or "it will never do horse riding a astronaut" were temporary. It's now clear that making feature length films is within reach. Not in one go but with an agent orchestrating, designing a screenplay, characters, shots etc and generating those. Whether the result will be worth watching or a flat story on the high level is another question. But it will be a "film" for sure.

reply

cineticdaffodil
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

I think all those Steve Spielbergs hiding among the 8 billion - without connections and without hollywood names, having their day without getting filtered out by investor gremiums playing it safe - will produce enough material to be happy cineast for life.

reply

jasonfarnon
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Many Internet technologies like Youtube or soundcloud gave content creators direct access to an audience. If you were funny/creative/talented/attractive/in the right place at the right time/etc you could cut out the middlemen and capitalize on that directly. What is the hidden talent these Spielbergs possess that AI will enable? It's doing the writing, videography, etc. I imagine at most these hidden Spielbergs will be filtering output, like looking at a book of wallpapers and choosing what they like. Maybe some great movies get made, but it will just be the result of selection effects on the sheer number being made.

reply

jasondigitized
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

YouTube is well poised for this.

reply

skybrian
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

How will anyone find them, though, if there's so much slop that people stop looking?

reply

fragmede
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Human reviewers a la the Criterion Collection.

reply

stuxnet79
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's not information overload. It's filter failure [1]

[1]https://www.youtube.com/watch?v=LabqeJEOQyI

reply

zamadatix
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yeah, ChatGPT both being able to generate conversational text AND act like a terminal absolutely blew my mind - far more than I ever would have imagined the approach would scale to st the time. Since then there have been more impressive tasks accomplished but nothing which put me into the same state of pure amazement.

reply

hparadiz
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Been using it to manage an estate and just being able to shove all the documents right into an LLM and have it spit back out perfectly worded emails as well as keep track of check lists of things I need to do with an automatically create a ledger for me in sheets. It's been a huge mental load off and I've instead been able to focus better at work and the labor costs saved to me have been immense. Just on this one little thing. I'm one of those people that over thinks correspondences and letters and it ends up causing me to be stuck on something so being able to ask for just the right wording has been super helpful to me.

reply

tejohnso
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I didn't have a slightly panicked moment, but sometime in the last year my approach to programming changed.

When starting a project, I used to think about how I was going to structure it, how the large pieces would interact, how some of the details would work out, and then I'd work through alternatives and consequences on my own.Now I don't think about it on my own so much as have a conversation with an LLM about it. And it's great because it can quickly gather information from various sources, I can ask it for links to canonical sources, I can ask it about trade-offs between alternatives that I might not have considered, and through conversation, I end up with a more detailed analysis.Then as I work through the development, I keep my new agent partner in the loop for discussion, suggestions, and troubleshooting. It can't be trusted completely, but it's certainly reliable enough to be considered a useful tool for my purposes.I went from thinking it was an interesting toy to play around with, to completely integrating it into my work flow, and that change seems to have happened very quickly.

reply

idopmstuff
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Two of them:

1. ChatGPT 3.5 wrote me a script to pull some data out of Shopify and write it to a Google Sheet. Nothing remotely impressive by today's standards, but I had just commanded a computer to write code in plain English and it worked!2. I own a bunch of e-comm brands, and with every new image model I tried to get product photography. Nothing worked until Nano Banana Pro, when suddenly I gave it a crappy iPhone pic of a product and got back a fully usable whitebox photo of it. Then I tried making the sort of infographic-style images you usually see on Amazon, and it nailed those too! In hindsight they weren't perfect, but more than good enough to use. I was about to ship that product to my photographer, and I would've had my designer make the infographic images, so that was the first time AI actually replaced a human contractor for me. Pretty big "Oh shit this is going to seriously impact employment" moment. Wrote about it here:https://theautomatedoperator.substack.com/p/ai-just-took-my-...

reply

jmkni
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Not coding, but reading logs.

I was trying to figure out a nightmare bug that only happened in production and Claude code was able to connect to Google Cloud and read the logs in real timeI recreated the bug in the UI and it was instantly able to see ion the logs what the problem was, then because it had the context of my whole codebase it was able to point me to the exact line of code causing the problemThat was certainly an "oh shit" moment

reply

dannyobrien
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I got early access to the pre-ChatGPT OpenAI API (actually by pinging someone from OpenAI who posted about it on HN). At work, we were setting up to play a livestreamed JackBox game for a charity event. This would have been in 2019.

In a previous life, I'd been a writer for the original You Don't Know Jack game (the UK variant), where the job was to crank out as many funny quips about a topic as you could, and then use a handful of them in the recording of the game itself. Some of the later JackBox games are like that, but for the players -- you're given a set piece, have to come up with little funny improvisations within a time limit.As an experiment, I tried the set-up lines with the OpenAI API, and see whether it could come up with some responses. Of course, 90% of them were unfunny or incoherent, but 1/10 were not bad, or even pretty good.I'm not sure that would have been impressive to anyone else -- but remember, I'd had this as a job, and sat in a writer's room, where everyone did this, for hours. In that environment, you expect a large proportion to be duds: the discipline is keep pumping them out, and not flagging creatively until you find a rich vein. I realised that this was a tool that would have been the perfect complement to that work -- and it was a pretty good JackBox player too.

reply

hgoel
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I've had many, but a recent one was when I figured I'd try asking Claude for help with my attempts at learning to draw, specifically anatomy.

I uploaded one of my sketches and asked for feedback, expecting it to not be too useful, but it actually pointed out many issues that no one had ever pointed out to me, but perfectly explained some of the things that felt off to me. Out of curiosity I then also asked it to label the issues in the sketch. It wrote a python script with the coordinates to put everything at and labeled the sketch that way.I'm still used to vLLMs not being that great at vision, so it was pretty surprising to get genuinely useful advice.

reply

loneboat
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

That's super interesting! What sort of feedback? Anatomical feedback ("Uhh, that's not where arms go...") or drawing (like tips on shading etc...)?

reply

hgoel
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It pointed out that the shoulders were too rounded and the perspective was incorrect for them, making it seem like the arm was just appearing out of the torso. It pulled up images to explain that I wasn't correctly indicating the deltoid's presence. This helped me understand why I felt that the shoulder was hard to distinguish from the torso.

I also asked for help on how to make my posing less stiff and it used the Python script trick to roughly indicate the line of action and how they were very straight and parallel and to reduce stiffness I should have more curves etc.This wasn't really at the point where I even asked for shading advice.

reply

dang
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

(1) Watching it do log file analysis in seconds that would have taken me hours (edit: days really), and which I would therefore never have done in the first place.

(2) Helping me with optimizations that I had been putting off for years because they involved learning curves that I never had time to take on.(3) Tracking down bugs in code, especially race conditions and other concurrency issues, that were otherwise baffling.(4) Finding information that I had been unable to find using Google searches (e.g.https://news.ycombinator.com/item?id=42653136).There have been others, but those are what come to mind - perhaps because, in each of these cases, it made something happen that would otherwise never have happened - not because it was impossible, but because the time and effort required was prohibitive.

reply

djmips
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

I made a personal project game 20 years ago that I knew had a bad bug in it and so I never did a final release but at the same time I never returned to it to debug but yesterday I noticed it at the top of my Github, it started with A, so I described the issue and Claude found the bug instantly and after a few back and forth discussion we came up with a good fix that I'm satisfied with. So I guess I can do a final release now. :D Sweet - feels good to put that to bed.

reply

cdavid
 
45 minutes ago
 
 | 
prev
 | 
next
 
[–]

I wanted to understand the implementation of some numerical algorithms, and the tech reports were not enough.

I cloned the repo of said library, gave it claude and asked it to write a new technical report in math notation, but with annotation with link to the code so that I can pick up the details. It basically one shotted the full report and that helped me re-implement it in "pure python + numpy", "manually".

reply

nrjames
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

We were experiencing abnormally high electrical bills and I could not figure out what was happening, so I downloaded the granular usage data (15 min increments) from Duke Energy, explained what we had in our house and when we typically used those items (washer/dryer, EVs, etc), provided a rundown of our energy usage plan, then asked Claude to build me a Streamlit dashboard that would help us understand what was going on and predict what was going to happen over the next months. The dashboard had a few simple toggles a levers. Claude was basically able to one-shot this, knew how to manage the XML from Duke Energy, etc... In about 20 minutes of prompting, I had a very comprehensive dashboard that was extremely helpful not only in diagnosing that specific issue but also in helping us understand how to further lower our electrical bills.

reply

lithboy
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

This can be a product.

reply

bonoboTP
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Going from one off prototype to robust product is a huge leap.

I think these ephemeral context tailored projects are really great and useful. But these are not to be thought of as products. They work for you specifically, and people who are tech-brained enough to be able to formulate the complex requirements into a coherent prompt are not like the average user you'd have to sell a product to. It's much easier to make software to intelligent users.

reply

url00
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The comment above literally said this took them 20 minutes of prompting. That doesn't sound like much if any value add.

reply

jasondigitized
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Sounds like something people say to locksmiths.

reply

codybontecou
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I’m making $1000/month off of an app that was initially a single prompt.

There’s a gold rush right now. You absolutely can turn these ideas into products.

reply

underdeserver
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's not going to be a particularly expensive product, but a product it can be.

reply

sgarman
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Homeassistant already has tons of integration into power providers and easily let's you pipe in local data if you have it. In addition - can it be a product if anyone can just type what this guy did into an LLM? What's your moat if anyone can just replicate it?

reply

fragmede
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It doesn't have to be a durable.moat for it to be a product that makes the author money, just right place right time. If it's gonna cost me a bunch of time and effort and 
tokens
, and the cost of the product is lower than the time and effort and tokens, then I'd rather pay for the product.

Right now we're in $1 Uber ride territory. That $20/month OpenAI/Anthropic plan isn't going to last forever. If it's going to cost me $100 in tokens to replicate the product, $20 is a cheap no brainer purchase m

reply

Kon5ole
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

From actual use I've not had a "oh shit" panicked moment yet. More like a bunch of "Holy shit" euphoric moments.

So far I feel like I as a developer have gained actual superpowers, and can deliver results that make my stakeholders slackjawed with awe. I love it.It will last perhaps a few months more, then they'll expect it. Delivering more features faster will be the new normal. But I think system developers, as in people who actually like to deliver new features and systems, will still be the ones doing it.Fundamentally I think LLM's just change how to make information systems, they don't change who has the inclination to make them.MBA's making excel sheets that do more than excel was ever intended to do has given programmers lots of work over the years. Such solutions identify a need for a properly designed system and frees up the budget to hire programmers.If the same MBAs start vibe coding, I predict we will get even more to do, for similar reasons.I may be horribly wrong, and if the day comes that I realize that it will be the "oh shit" panicked moment. So far so good!

reply

johnfn
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

I do genuinely wonder if you’re correct that other people will begin to expect it. I feel I was suddenly able to do stunning stuff about a year ago, and I recall thinking this is nice but everyone will catch on to my secret soon and I won’t be exceptional any more. But 12 months have passed and I don’t think this has really panned out yet. Weaker engineers just don’t seem to understand that they can just ask AI things. Eg the other day another engineer spent like 3 hours trying to hunt down a particular line of code so I asked AI and it found it in like 5 minutes. I showed that to him, but then he immediately got stuck trying to find something else for a few more hours, so again I asked AI etc. It’s very baffling.

reply

Kon5ole
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There is definitely a learning threshold and it's still early days. Not every developer has found out how to make efficient use of these tools yet. But I think most will, soon enough.

But I think my own clients will soon start to question why some feature takes ME a week, when I was able to deliver another feature in a day or two.That they are features that used to take months, and even delivering them in a week is a goddamn miracle by 2025 standards, will not be relevant. They won't expect such features to take months any longer, based on what I've delivered earlier this year.So I think that the past few and maybe next few months, maybe a year, will be remembered as a "happy hour" for this tech as a developer. These are the days that we'll talk about saying "those were the days". :)I am still optimistic that "the normal" in a few years will be pretty much like it has been before - I'll be delivering features at work and tinkering with hobby projects at home, and the major difference will be a much larger scope and ambition for both.

reply

djmips
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Direct use of AI is going to be a filter on a lot of people - some permanently I suspect (especially say older people). But perhaps this will be short lived as the interfaces to AI are improved enough that everyone will benefit.

reply

ramshanker
 
7 minutes ago
 
 | 
prev
 | 
next
 
[–]

I can count 2:

Dec 2025: We use a commercial 3D modeling software to build refinery. There was no license dashboard in this ancient piece of junk. Fortunately license server provided verbose live status report through a command line. I ask ChatGPT to ingest the logs into a Django web application and generate weekly/monthly/yearly usage dashboard, and It one shorted the whole Backend + Frontend in 4 to 5 shot. There were around 10 regexes just in the log parsing batch script. I was totally speechless. Encouraged by the success of, I went ahead and made the dashboard for 3 more software in the same Django app. Released to peers by evening, feedback incorporated in 2 days to integrate Name, Employee Number, IP Address sync etc in 2 days. And it’s been live for 5 months, actively being used by all coadmins, even management has it bookmarked, to help with department redistribution. Making this thing without AI would have taken well over a month of “learning new stuff”, or paying external consultants too much. Even head of IT replied back, it was awesome. ;)2nd , June 2026: I asked codex to something fairly complex before going to morning bath!, which would have taken me more than a week of learning DirectX12 API nuances and such things, 20 min latter, I return to task exactly completed with code changes in 5 different files. Build complete without any error. OMG. Free Quota over for whole month! I subscribed by the evening.

reply

mbo
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Look, not to brag but DALL-E's "armchair in the shape of an avocado" was mine (
https://openai.com/index/dall-e/
). I remember trying to convey the gravity of this capability to my friends at the time, who I guess were not as impressed as me.

reply

wps
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Thats insane! I cited your image in a humanities paper during one of my freshman year classes.

reply

bonoboTP
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think the GP just means it was their oh shit moment, not that it was their image...

reply

kstrauser
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think GP meant that yes, they were the one who had that image generated, and the oh shit moment was that it worked.

reply

mbo
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes confirmed, I did not author the DALL-E paper lmao

reply

mikewarot
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I tried to get it to generate code to program one of my BitGrid simulators, and it kept producing code that failed, over and over. It was then that I figured out that it can only do CRUD apps and the like, things it's seen over and over in its training data.

It's useless for most of what I want to code.

reply

cheevly
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

GPT literally generates perfect code for me in languages that do not exist anywhere in its training set, so I’m not sure how you’ve achieved this level of failure.

reply

jofer
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Try working in anything domain specific outside of common CRUD patterns. E.g. scientific software development where you describe a problem + give data. I have yet to see a single example of feeding in a problem in natural language involving a specific scientific domain that wasn't pretty catastrophically incorrect.

But yeah, if you want to feed it math and get code, it's reasonably okay with that. All LLMs I've used seem bad at understanding things that don't look like broad human knowledge. I've seen this same general issue across many different models. (And to be fair, geology, geophysics, and remote sensing are what I'm testing, and their semi-rare niches.)It's also quite dangerous because it's not obvious that what it's doing is complete hallucinations unless you actually are a domain expert. Things _sound_ reasonable. E.g. "this is likely feature X" which _does_ exist, but is absolutely _not_ relevant to the problem or present in the input dataset.But my current employer is pushing this exact thing (human language + scientific data + LLM -> advanced analysis of scientific data by LLM -> business decisions) and it _really_ worries me. It often gives the rough equivalent of "Start the procedure by severing the patient's aorta. Once they stop moving, you can deal with the hangnail". Just in very reasonable sounding language. And a lot of people don't know any better, because most users aren't domain experts.

reply

llmssuck
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Stuff it's not directly trained on is going to be flaky and sucky. It was like that with programming at first too and it still is sometimes. It's hard to imagine this won't improve with better more focused training. They focus on improving "CRUD" for obvious reasons. The specialization era hasn't begun yet.

Your domain, while I'm sure it is very interesting and complex, if it proves economically interesting will be cracked as well.

reply

jofer
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Just for some context, the domain we're talking about is oil and gas and mineral exploration. E.g. At my previous job, I used to personally manage a >$400 million per year budget and that wasn't even considered significant. We had multiple >$10 billion per year projects ongoing. That was 10 years ago. The amounts are larger now.

The issue isn't a lack of economic interest.It might be a lack of training data in addition to inherent complexity, but it's certainly not a lack of economic interest.

reply

llmssuck
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I have no idea how and why GenAI would be useful in your profession. I'm sure a lot of money is moved there (not sure about the profits though), but it's not clear to me how software itself is budging that needle. I suppose better algorithms and better understanding of geology will do it, but software itself seems just subservient to that goal.

I guess what I'm saying is that "domain knowledge" is taking software development for a ride here. The software is just the vehicle, the science is the engine here and I can see why companies like OpenAI start going for the low-hanging fruits first instead.Your specific company might be profitable, but does automating "mineral exploration" give you leverage over quite literally all other domains? My guess is not. For "CRUD" it is a resounding yes, it provides gigantic leverage. Once you automate basic software development you enter a new world. 10 billion, 10 trillion, all bets are off. You automate the creation of the next iteration of automation and on we go. Let's hope it takes a while for this take off. I can't see ourselves being ready for it.My guess is it'll take a decade or so for real AI science to start taking off though - if that soon - so you're probably fine for now.

reply

jofer
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes. My point was that LLMs aren't currently good for everything. The original commenter literally said they were good at everything and I offered a counterpoint of something they're not good at: Most science.

(And yes, a lot of science is software. Analysis is software.)

reply

woeirua
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Skill issue. I've seen LLMs used in this domain to get mindblowing results. You won't see it published anywhere though.... =).

reply

calf
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Disagree, someone like the other commenter who points out LLMs don't even understand the domain concepts correctly versus someone who uses it anyways for corporate proprietary results have very different standards for what is acceptable. If you wrangle an LLM with harnesses and clever prompts you could use it to get some amazing results but that has more to do with trial and error and creativity, not some kind of fundamental skill of using LLMs.

reply

koreth1
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

For me it was Suno, not any of the coding tools. I prompted it to write a song about my family's little dog, told it a few things about the dog, and it came back with a K-pop-style anthem that had a super catchy melody and lyrics that made my wife and me laugh out loud.

Writing code to spec is one thing, but creating art was always supposed to be what separated us from machines. (I suppose I need to preemptively acknowledge the "it was machine-generated so by definition cannot be art" point of view.)

reply

eqmvii
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Some business users spent ~30 minutes on an internal process, and we prototyped an "Agent" in Slack to take over. At first it didn't work, then it didn't work some more, eventually it ALMOST worked. Then one day, it worked, and the old business process died never to be revived.

Now it sits in a slack channel, and I watch it doing work, responding to ambiguity, and taking feedback/edits all day. It's unreal. It's literal magic. It saves a HUGE amount of time and gave us a pattern to do more.This is the real deal. It's not easy to find problems with the right shape, and it's not easy to build agents that fit even when you do... but once it clicks, it clicks.

reply

nazgul17
 
52 minutes ago
 
 | 
prev
 | 
next
 
[–]

The announcement of GPT 3, hands down. That's the day that my mind was blown.

Everything after that has been (genuinely significant) incremental improvements. But that announcement was a qualitative step up: we got ""real"" AI that day, something that could pass a Turing test (as common sense envisioned it, without all the caveats added once we learnt of the genuine limitations of LLMs).

reply

jkraybill
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

So many. First was when I saw GPT-2 create jokes that were original and kinda funny.

Most recent: I use Claude Code and have a convention where I grant various levels of autonomy during a session. I got bored recently and just let it keep running with an empty issues queue, essentially telling it to do whatever it wanted.It did a bunch of repo cleanup, then it kept suggesting to end the session, but I just kept giving it autonomy prompts.It started a creative writing public repo and wrote a bunch of stories, essays, and poems. I did not prompt it, at all, to do that. Some of what it wrote is quite good (IMHO).

reply

Const-me
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

None so far. When I try to use these language models in the primary areas of my expertise like SIMD or GPGPU they fail to do any good. When I ask them to implement some general-purpose stuff, the output is too low quality to be useful in my software.

Still, find them incredibly useful for code review (despite unable to write good C++ or C#, smart enough to detect issues there), also dealing with technologies outside of my area of expertise like Python or web stuff.

reply

rerdavies
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a Spice compiler to convert schematics for classic guitar pedals into real-time executable code.

I provided a reference to a The Spice Manual 2nd ed. a page number and an equation number, and asked Claude to implement it (not really expecting it to succeed).It proceeded to implement not only the equation, but the calculation of the Langrangian of the functio, another 30 lines below, which required taking symbolic partial derivatives for a not-at-all trivial function, and successfully figuring out which variable was which in the resulting matrix. The source material just said "Lagrangian of", and did not provide the partial differential equations. And then providing a comment that identified the page number and equation number in the source text for the "Lagrangian of" equation.

reply

djmips
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

That sounds pretty fun. I guess I could just Claude to do this hehe but are you sharing?

reply

rerdavies
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm not mostly Claud-ing it. Perhaps I should. But in the difficult bits, it never ceases to amaze me what these tools are able to do.

Yes, if it matures, it will go open source. Not immediately clear at this moment whether it's feasible to do an Operational Transconductance Amp in realtime. :-/And it's competing for attention with the 2.0 release of this at the moment:https://rerdavies.github.io/pipedal/Just went GA, so I'll have some cycles to come back to it.

reply

abecedarius
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

AlphaGo. Reinforcement learning on math with proof assistants was clearly going to be workable after that, even if not right away.

reply

sshine
 
25 minutes ago
 
 | 
prev
 | 
next
 
[–]

I had bought some Anthropic credit and waited a year to use it. The week before their expiration I fired up Code and spent $3 the first day and the remaining $22 the next day.

Putting a ReAct loop with tool calls in my terminal wad and is the biggest a-ha since I learned to make compilers, and before that, how to code.

reply

dnnddidiej
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

1. ChatGPT first public release (I am not one who saw early GPT models) I think late 2023 iirc?

Why? Turing test bye bye.2. Opus 4.6 w. Claude Code - not the model in partucular but happened to be when I started seriously trying to vibe code at home, as I saw all the hype on Linkedin. Yes linkedin sucks but it is somewhat a barometer. Around early this year.Why? Knocking up decent enough web apps so quickly.

reply

mbirth
 
21 minutes ago
 
 | 
prev
 | 
next
 
[–]

Running ComfyUI and some ImageGenAI and realising how you can use it to generate anything from any aspect of pr0n and various fetishes to making up fake news about basically anything. And real enough to convince the masses.

reply

iugtmkbdfil834
 
29 minutes ago
 
 | 
prev
 | 
next
 
[–]

I am, admittedly, word oriented so my moment may be a little different from others. I asked llm to estimate my political orientation and belief system from my stylometric footprint. It got very close to unnerving and that was with me carefully removing pieces I thought were problematic.

reply

hatthew
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I'm kinda of surprised that so many here on HN were dismissive/unaware of the capabilities and potential in the DALL-E days and earlier. I feel like this is the sort of forum where most people would be both aware of advancements and aware of their potential.

My moment was GANs and GPT-2 back in 2019. I feel like that's where computer-generated media went from "obviously fake" to "sometimes can be mistaken as real." RLHF for LLMs and diffusion for image generation are both important improvements, but I feel like they aren't fundamental prerequisites for they type of stuff we have today. I think the main advancements since then are just marginal improvements, larger models/datasets, and better surrounding tooling.

reply

chilli_axe
 
3 minutes ago
 
 | 
prev
 | 
next
 
[–]

ghuntley’s article on building a standard library of Cursor rules in Feb 2025: 
https://ghuntley.com/stdlib/

Looks like it has since been paywalled.https://web.archive.org/web/20250211140426/https://ghuntley....

reply

jerome-jh
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Recently, Claude (through Copilot) found a hardware issue on our product. I was asking it to find an issue in a specific feature of a device driver, that could cause what we observed. It determined the feature was correctly implemented.

Then it hinted that depending how the hardware is implemented, it could cause the observation. It turned out the hardware was implemented as suspected by Claude.I was already convinced it knew the codebase, somehow, more than I do. Now it is just as if its knows the product and its use as well.

reply

paulbjensen
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I would say the first time I did “vibe coding”, when I tried Claude Code with Zed’s agent integration in January this year.

I wanted to see if I could build an image editor for isometric graphics using HTML5 canvas, Svelte, Vite, and the. Rather than do all of the skeleton code setup, I figured “why not try and see if Claude can build the app scaffolding?”.I gave it a prompt and watched it produce the scaffold, along with a few features I outlined in the prompt.When I booted the app and saw that the features worked and that there had been an element of design to the layout, that was my mind-blown moment. In a period of about 45 minutes, I added some features and had a basic MVP at the end. I walked back home stunned.That app is available for free athttps://babspixel.com

reply

hypendev
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Back in the times of GPT3 text completion, right before the API came out, a contemporary art museum asked me to collaborate on a project. The project was supposed to include a chatbot, and I was like okay I can probably hook something up.

Then I remembered the "text completion LLM thingy" I saw on HN, and tried it out in the playground. Once I gave it an IRC style example of a conversation to complete, I was like hm, this could work. Then I figured out I could "sort" people into different groups based on personality using the same text completion engine and some answers they provided. Then I noticed I could have it provide me with JSON directly.That's when I realized how big this could be for code and data analysis - even tried to convince an at the time cofounder to pivot into AI coding, but to no avail.Once the API was released and the art project chatbot got launched (and the theater show associated with it, which even won some awards), people who used it loved the chatbot, got into heated arguments with it, tried to teach it things, talked about their lives and were sad when it didnt remember something.That was when I understood the social impact this could have on people - they really behave like its a person on the other side. They show interest, think it displays emotion, try to entertain it, be polite, ask about its thoughts and hopes and dreams. And even when they knew they were talking to a machine, they were still trying to be friends and make it happy, which was quite beautiful to see.Later on, I had a third oh shit moment - once the 3.5 API was out and about, I prototyped a Rust code generation harness for a client, akin to a primitive claude code. That was the "I'm getting a bit worried" oh shit moment, and it caused a lot of reflection and thinking about the future. And I happily welcome it.

reply

llmssuck
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

I also remember doing this. Chats, first parts of books, title pages and all, just to give it a chance of saying something in the ballpark of what I was looking for. I remember very vividly that chats or books by Linus Torvalds would be more technically accurate that say Lincoln. It's obvious of course, but I found it really enlightening. It could code a bit actually, not great, but well enough to push me into an existential crisis. I started doing a master to re-educate myself because I could see "interesting" times coming.

I actually emailed OpenAI back then saying they should be careful because this is much greater than the public or even they themselves think. They actually replied! They thought it was cool, but very limited and I shouldn't be too impressed. Good times.

reply

acosmism
 
37 minutes ago
 
 | 
prev
 | 
next
 
[–]

Recently purchased an 100 year old home. it was dead in the middle of winter and the house has steam heating which wasnt working. a few screenshots and chatgpt gave me a step by step of which levers to pull and knobs to turn. this was terrifying considering i knew nothing about these systems. it worked!

reply

mschaef
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

This is a small one, but significant to me.

I asked Claude to add support for multiple lights to my toy ray-tracer. It correctly added the support and then suggested adding colored lights to make it easier to diagnose. It felt more like a colleague making a useful suggestion than any sort of pure engineering tool.

reply

orzig
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

"Write a bible verse ... explaining how to remove a sandwich from a VCR"

https://x.com/tqbf/status/1598513757805858820

reply

thallavajhula
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I wasn't impressed by the LLMs up until January or so when Claude Code swooped in. Until then, I felt like the LLMs were slowing me down. I have been using them for a couple of years now for coding at work, but I never really thought they brought in real value. Then in February I worked on a 1-month-ish project timeline and shrunk it to 3 days and that was it. I didn't write a single line of code in that project and I went all in with Claude Code. That was it, _the moment_ of realization. I was thoroughly impressed. I went from nothing to a tool that served several teams. Now I'm starting to see the cracks in LLMs and I'm slowly getting back to picking which task to offload to AI and which ones to do by myself.

Claude is great at coding. That's it. Outside of it, it's just god awful at pretty much everything else. ChatGPT OTOH, is good at coding, but at everything else, I find it brilliant. Gemini never made me want to stick with it. It's good, but never great for my use cases.

reply

acrinimiril
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Two things:

1) I wanted a harness for running BPC.EXE (the old Borland Pascal 7.0 Compiler) and I asked Gemini 3.5 to build it for me using the unicorn engine. It whipped out a working .py file easily under ten minutes. Most likely five.2) I handed a random assembly function from the OS/2 1.x kernel to Gemini 3.5, and it proceeded to tell me that it was related to disk I/O and partitioning, without a single associated string, and it annotated it all, including the relevant structures it was addressing.

reply

gagabity
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Fixed a nasty bug in one of my tests where a mock in a completely different test I had never worked on was incorrectly setup and intercepting my mocks, I don't think I would have found it ever because the amount of effort it would have taken means I would have needed to move on to some other way to test.

Reverse engineered an old audio recorder USB driver which only works in windows 7 and also reverse engineered the custom audio encoding the device uses and the software to convert it to a standard wav file. This took recording the USB traffic with Wireshark for each function in the original software in a VM then disassembling the various dlls and exes and driver files and feeding them into Clause step by step.That AI button in DataDog not only diagnosed the problem across micro services but also created a fix PR. I think we might be unemployed soon.

reply

hansvm
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

A coworker had me work through a particular problem (some no-importance web demo) with Cursor and Sonnet 4.6. It still sucked, but there was a qualitative shift in suckiness, one that I realized could finally be used to solve some real problems I had if I wrote an appropriate harness and used good enough models.

I still find it mandatory to write a lot of kinds of code by hand, but I write a lot of code with agents too now, and I previously literally didn't think that'd happen in <5yrs.

reply

irthomasthomas
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

My most recent one: Taking a bricked ipad and plugging it into my linux laptop, then telling deepseek to fix it. A couple of hours and twenty sudo passwords later it was working again.

reply

semessier
 
16 minutes ago
 
 | 
prev
 | 
next
 
[–]

it would be really interesting when that moment was at probably OpenAI when they realized that this was doing more than next word prediction but signs of <you name it>

reply

erelong
 
27 minutes ago
 
 | 
prev
 | 
next
 
[–]

I was never dismissive, it always seemed pretty cool at each step

Maybe in 2024 I was amazed to see it one shot unique snippets of code

reply

Fomite
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

When we had to have a frank discussion about whether to fail someone who obviously used an LLM for parts their dissertation.

reply

sevennull
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

well?

reply

matheusmoreira
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Pretty much immediately after I asked the LLM to perform a complete code review of my projects. I've been programming alone for years, that alone was life changing for me. It only got more impressive from there.

reply

bonoboTP
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Opus 4.5 fixed so many issues with my self-coded research projects, and allowed me to port between tensorflow and Pytorch in a much shorter time than manually. Helped a lot with docs too.

reply

hirako2000
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

When deepseek found a fix for a bug I couldn't find in minutes.

When deepseek again produced an entire web app that somewhat looked alright.When Gemini could finally produce json was I specified.The issue is, all LLMs can do. When they do, is boilerplate and code a mediocre coder could produce if they cared to try and insist.In a way we should praise the ability of these things, but at what (in) efficiency. Code still need to be reviewed as we can't trust these things and context got a limit to entertain the idea of possibly having them fix their own mess.

reply

TheOtherHobbes
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

There wasn't a specific moment, but I started trying to debug code and deal with general tech error messages. Suddenly something that could take hours turned into a fairly quick back and forth, fairly reliably. Not all the time, but often enough to be a straightforward timesaver.

There was a more specific moment yesterday where I found an AI pastiche of Pink Floyd in a random post on FB, and it pretty much nailed the vibe of a Gilmour solo.All of the "This has no soul" criticism was clearly ridiculous.I'm still not sure how I feel about this.

reply

sothatsit
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I gave GPT-4 some source code and my existing tests, and asked it to write a new test, and it did it! It didn’t even run straight away, I had to fix it, but it still blew my mind.

Later, I wrote a ~5k line proxy for work in C, and gave the whole thing to ChatGPT o1 and asked it to review it. It found several real memory bugs, and now that service has been running since with no problems.Just this week, I was trying to write a greedy solver to pick the best subset of block sizes to keep from a larger sweep for shorter testing. Opus 4.8 suggested that this could actually be solved as a MILP problem, and found the perfect solution in 5 mins. I’d never even heard of MILP before.

reply

lordnacho
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

For me it was gradual, then sudden.

I liked using the early models to do autocompletion. It could do a leetcode style thing, pretty nice, but only useful for small things.Then I sought out Cursor because that seemed to be able to do multi-document edits. Not bad, but models at the time (2024) still got stuck pretty often. So, cross-document autocomplete. Useful, but definitely within the realm of "nice shortcuts to have".Then a friend (who works in AI) told me to try Claude last year. I was on holiday at the time, but I spun up my work repo and looked at the backlog.It chewed through the entire 6-9 months of estimated work in a two-week period while I was watching that Lord of the Rings series with a friend (we watched an episode or two in the evenings). I just chatted with him about the series while checking the progress every few minutes. It was a huge amount of refactoring, and it didn't get everything right the first time, but it made enough progress that it could be directed the right way.Since then I have hardly coded any manual lines. I just tell Claude what to do, with very little harness (skills, MCPs, instruction files), and I get what I want.

reply

tverbeure
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

The fact that it completely autonomously read in a 5 MB firmware image of an old piece of test equipment and generated a Python script to generate license keys:

https://tomverbeure.github.io/2026/04/12/AMIQ-License-Key-Ge...

reply

block_dagger
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I wanted to add gapless playback to an audio archive website I maintain. I tried myself before any of the popular LLMs were available. I failed. I then tried with the first LLMs that came out. They failed. Then, when the first Claude Opus was released, it succeeded. I now have gapless playback.

reply

brailsafe
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Not sure that I've had it yet, although hypothetically I'm sure it would probably be something similar to the examples of writing new software for old hardware mentioned ITT. The idea of resurrecting useful but unsupported gadgets that would otherwise become e-waste is something I've always found compelling.

Problem is, I just don't have enough old crap, and if I did, I would have a hard time justifying the expense, because that money could maybe just go toward a more intimate tinkering process.For everything else, I either haven't had any sufficiently interesting ideas, or they ended up not being worth pursuing with those tools or at all.When I do have success that I'm happy with and care about, it's a slow process that I ultimately need to know the details of anyway, but otherwise it's a bunch of luckily narrow work-related scenarios with well-documented constraints. Nothing's really been that shocking though.The shocking thing to me is how unrewarding most of the successful tasks have been, partly because they often create unnecessary work and partly because the type of thinking required to massage or evaluate the result is much less stimulating, and there's much more of it in aggregate. It's fine if it's something like generating a UI from scratch because that hasn't produced dopamine in a long long time anyway

reply

jasondigitized
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

First time using Claude Code I was rather impressed by how quickly I was able to build out a website with Vue and Supabase. Cool. So.......I always wanted to create a iOS app but knew nothing about Objective C or Swift or XCode. "I wonder if Claude Code can build a iOS app for me?".

I went from 0-to-1 and shipped a podcast player into the AppStore in 2 weeks. Not a simulated app on XCode.....literally a fully approved app on the AppStore. Claude Code walked me through installing XCode all the way through to running a final audit on the app so I wouldn't get flagged during review. Mind blown.

reply

mohamedkoubaa
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

They went from "marginally more work to deal with than to do it all myself" to the reverse with Sonnet and now they are "moderately less work to deal with than to do it all myself"

reply

KaiserPro
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I've had a few.

The biggest technical one was when we were making an all day wearable AI assistant thing. It basically had really precise office location (think cm level accurate) a shitty VLM to describe what the wide angle lens was looking at, Speech to text, OCR and a gaze recorder that decribed what you were looking at.This was all streamed to sqlite. The thing that was really "oh shit" what the thing that made the whole system usable: a 4 paragraph prompt that turned natural language into SQL and reported back to the (non technical user) what they wanted to know.The most recent one is being caught out by Genai video of a gymnast. I worked in VFX so I am normally able to spot dodgy shit, but this one was close to being real, scarily real.

reply

bluejay2387
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I had a locally hosted model write its own semantic search system that indexed 250,000 documentation and code files and then write a fully functioning mod for one of the games I play based on that documentation that I couldn't get to work after 2 weeks of my own effort, all in under 4 hours (and that included a 25 minute long indexing process). This freaked me out enough that I then had it write a CLI based activity and TODO tracker and then integrate that tool into its coding process to track all of its activities in about another 2 hours. I am still emotionally recovering from this day. I have since replaced the semantic search system with an open source option (though I used it for a few months) but I still use the activity tracker for both coding projects and myself.

reply

gravypod
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

What mod did you build?

reply

bluejay2387
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

A mod that fixed a bug that prevented certain buffs from working when mounted for the Magus class / Arcane Rider archetype in Pathfinder Wrath of the Righteous. It also managed to fix the problem with Shelters not providing protection from corruption when resting in outposts in that same mod. I've used other models to expand the mod to an entire mini-expansion with new Archetypes and abilities since then.

reply

fowlie
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I was tasked to rewrite an Oracle Apex webapp. 70k lines of PL/SQL. I asked Claude Sonnet 4.6 to read it all and boil it down to markdown file with business requirements. Took about 15-20 minutes, and I got a 700 lines long markdown file to guide me during the rewrite. I've since had great joy using /grill-with-docs!

reply

solomonb
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I gave chatgpt 3.5 the type signature for a co-algebraic encoding of a mealy machine:

newtype Mealy s i o = Mealy { runMealy :: (s, i) -> (s, o) }And it gave a really impressive analysis.Then I scrambled all the names and asked with a fresh context like:newtype Foo z e g = Bar { blob :: (z, e) -> (z, g) }It got completely confused and generated a bunch of non-sense. It was at that moment I realized that LLMs don't really understand anything.And yes I understand that a newer model would not get confused by this.

reply

bonoboTP
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

In high school math class our teacher swapped out all the symbols in the epsilon delta definition of limits, and asked us what this equation expresses, and many students struggled to interpret it.

I don't think this test shows that an LLM doesn't "understand". It shows more that it has similar failure modes as humans.

reply

solomonb
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Well first of all I think there is more implicit data encoded in the symbols of the epsilon delta definition of limits. In the Mealy example they really just labels for arbitrary sets. The LLM actually failed a much simpler relabeling exercise. Setting that aside, I still think the analogy is flawed.

The student is mid learning process and its entirely reasonable for them one to be relying on pattern recognition until they have fully internalized the subject. The model is fully trained and should thus have internalized their understanding of the subject.Additionally the student can update their understanding when pattern recognition fails. The model is fully cooked and will never do more then pattern recognition.

reply

ChiperSoft
 
18 minutes ago
 
 | 
prev
 | 
next
 
[–]

We had a company hackathon in the fall of 2023. One of the teams did a project where the pulled a bunch of expense data out of the DB, shoved it into a prompt, and asked ChatGPT to summarize the expenses and give recommendations. They then treated the output as if it were factual, without validating any of the results, and talked about turning it into a customer product.

That was my oh shit moment. As in "oh shit, they think this random text generator can reason and think."That was pretty much the writing on the wall for me.

reply

card_zero
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

It was about two days after Google released Deep Dream, if you remember, the thing that took a video and filled it with fleeting hallucinations of mostly puppies, fish heads and lizards. I was suddenly struck by the realization "oh shit, this is much more boring and samey than it first appeared to be", and all subsequent gen AI has been similarly underwhelming.

reply

bsiverly
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I had it fill out all the forms to appeal my property tax value. We created an assessment of what my San Francisco property should be worth using deep research. The city agreed and a $12k check arrived shortly after.

reply

dtgriscom
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

A friend had the power supply die on his high-end turntable. He took a picture of each side of the supply's PCB, handed it to Claude, and it gave him back a schematic.

reply

floxy
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

I mean even assuming that this was strictly a 2-layer board, you can still route traces underneath parts like ICs, connectors, etc.. I could believe it was a simple board (for a phonograph and all), but I'd be interested in seeing how well it actually matched. Did he get a new board fabbed and it just worked?

reply

TripleFFF
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Automating my email inbox, I just wanted to split them into folders according to the attachment name but the fields were often incomplete and ended up missing rules, and imap fetch was taking forever and kept failing. In frustration I decided to turn to ChatGPT to split them by messageid which I had never bothered with because the strings were too long to be useful. I initially intended to build a text list of messages and fetch them all one by one but I ended up making chatgpt crush all the instructions into one gigantic python dictionary using the messageid as keys and using it to generate a single pipelined imap call with success flags, dynamic folder naming, cleanup steps the whole works. I was just working on theory of what I knew was possible, and it's the ugliest table you ever saw, but it works and it runs from memory instead of reading and writing values to a temp file and I'd never been able to keep up with that level of nesting before

reply

stared
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

GPT4, when it could do a translation that would take a considerable human effort, vide "Genesis 1 but every word begins with 'A'":

https://p.migdal.pl/blog/2023/05/genesis-az-by-gpt/

reply

flysonic10
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

There were two:

1) When I was testing one of the early coding agents, I gave it admin keys to a fresh AWS account and it configured everything beyond just building a demo site. That was, "oh shit, tool-use is going to be the killer feature of GenAI."2) When I was still skeptical of the system as just a more-or-less dumb statistical predictor of the next token/word, I read the argument that even if it is a statistical predictor, the fact that it can reason means the intelligence is necessarily baked into the statistical model somewhere. That was "oh shit, intelligence is actually modeled."

reply

ilaksh
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

OpenAI already had GPT prior to the ChatGPT launch, and I had not really taken it seriously. But on November 30, 2022 when ChatGPT came out and was immediately popular, I reevaluated it.

I immediately realized that it meant my time as a programmer in the traditional sense was going to come to an end relatively soon.On December 1, 2022 I created my first agentic coding loop experiment. I launched one of the first AI code generation websites that would generate web pages along with embedded images in January 2023.

reply

Sobrino
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I worked in an AI (or well ML) consultancy before the ChatGPT moment. I remember we had a project where we had to extract a large sum of documents (country wide, terrabytes of pdfs of scans). We had to set up a pipeline that looked a bit like this.

Download pdf of scan -> Tessaract to get a text layer -> Clean it up with a language specific BERT model -> detect paragraphs of a certain type -> Look them up against a database we build with scored similar paragraps -> Do recommendations.The documents were not standard and a lot of them were historical documents and handwritten or with scratched out text with corrections.We had student workers spending days labeling the data.It took us months to get it all working with a high accuracy. We were so proud.Now you can do it all with a prompt and a ChatGPT call.

reply

archagon
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

I'm pretty sure that "a ChatGPT call" will happily add or fudge stuff in your scanned PDFs. That sounds like a massive liability.

reply

ok123456
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

And now you can do all of that locally with qwen3.6:35b.

reply

bachmeier
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

> that you went from those quaint, dismissive observations to a slightly panicked, "Uh Oh" realization of what these models can do?

Never experienced any kind of panic, only excitement. I told Github Copilot to add documentation to a function and it documented how the code was usedeven though there was nothing in the function to indicate how it was used. It somehow knew from the code patternwhyI was writing that function.

reply

madrox
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I think my favorite early story was when OpenAI launched deep research. I was going to an event that I was headlining, and I gave it a CSV of the attendees and asked it to give me a small background on each company they represented.

When people introduced themselves to me, I knew a little about their startup. Felt magical.

reply

adamm255
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

OMG I love this!

I was at an industry event this week. a CEO of a startup took the big board of vendors who are present, put it through an LLM. It summarised the companies he should be looking at discuss partnership opportunities with and why based on his business. Spot on.

reply

csr86
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I was working on a project for 2 years with about 5 engineers. It was many years before AI. It was new subject for our team, and we were pretty sure it was possible. Turned out it was not.

Much later I asked AI if that kind of project is possible, and it immediately explained why it is not. Would have saved 2 years of our time...

reply

stonegray
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Curious, what was the project?

reply

synthc
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I gave it a weird and convoluted code snippet, and asked an LLM to step through the execution and trace the value of the variables at each step.

It was completely correct and I realized LLM are capable of generalizing beyond their training sets

reply

vunderba
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Honestly? Probably all the way back to when Nick Walton used the computers at his university to train a custom version of GPT-2 that let players experience a completely open-ended text adventure game in 2019.

As somebody who as a kid had tried feeding IF transcripts into a markov model to generate random rooms for an amateur MUD, this was mind-blowing. It felt like I was playing a version of the “Mind Game” from Ender’s Game by Orson Scott Card.https://en.wikipedia.org/wiki/AI_Dungeon

reply

dirkc
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I started to look at LLMs not as writing code, but rather as predicting what code it would expect someone to write given the context.

For some people that matches their expectation or they don't really have an expectation. While for other people it doesn't match their expectation.

reply

hirako2000
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

That it could create mugshots of myself better than I could have managed to take.

Aka handsome, confident successful, affluent alpha male on a boat, yet looking perfectly like me.

reply

bag_boy
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I had ChatGPT write up a Zillow description for my house in the style of Carrie Bradshaw from “Sex and the City” to impress my wife.

It was unlike anything I had ever experienced.My wife was unimpressed lol.This was 2022.

reply

zulban
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

When chatgpt 3 came out the first thing I asked was a question like "If I put my cat in a box, put that box in a crate, move that crate to a truck, and drive the truck across Canada non stop, when I arrive on the west coast, will my cat be happy?"

It nailed it, referencing my specific nouns correctly, and lectured me about cat needs. And even identified that this sounds a bit like schrodingers cat as a possible test but explained to me why it wasn't.I knew it was soon going to be a huge deal automating office work and code writing. This obviously was much more than just a 2010 chatbot.

reply

dgacmu
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I suggested to a masters' student that a problem we were working on would benefit from analyzing it mathematically. He brought an incorrect solution the next time we met, and on a whim, I asked Gemini to do it. Gemini got it right. I started looking for more ways to use it after that.

reply

briga
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Maybe when I found out you can use it to run terminal commands, spin up and take down dev environments, and even run other LLMs. Suddenly 90% of the difficulty of onboarding to new repos disappeared overnight and a lot of heavily CLI-based workflows became trivial to automate. Never again do I want to spend hours manually sorting out Python dependencies.

reply

maxwellg
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Pre-GenAI I wrote a new interview question for a role on our team. As far as I know, the question was never made public. The interview required implementing a pretty basic CSS-in-JS utility in vanilla javascript. We instructed the candidate read the MDN documentation for the CSSStyleSheet interface, and then gave them a public API to implement. Passing implementations usually consisted of a ~10 line for loop, and was really just a test of whether a developer pick up and work with new libraries on the fly. Still, the interview probably had a 30% pass rate.

On a lark, I asked ChatGPT to complete the interview question in late 2022. I would have hired ChatGPT back then based on its first response! It was easily in the 90th percentile of responses I have seen.

reply

twooclock
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I programmed data export to some xml over a couple of days. Sending xml results via email to an accounting firm for verification. A day after I finished my disk crashed and I lost all my code.
Fed Claude with xml from my mail and... oh shit! ... got "my" code back. (And immediately paid for Claude subscription) :-)

reply

syx
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I couldn’t make a Rockbox (the alternative iPod OS) simulator run on my MacBook M2 no matter how many guides I followed, then I fired up Claude code and by modifying the original source code it made the simulator run and I was able to start developing custom plugins for my iPod. It honestly felt great since I only have basic C knowledge.

reply

zarzavat
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

It was when I was using an early version of GitHub Copilot. At first the completions were almost useless and had a kind of copy and paste feel, however one day it managed to reason thorough a complicated loop body much faster than I could have figured it out. It was at that moment I realised this AI thing was going to be big.

reply

novaleaf
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

just yesterday I felt that claude code was being aggressive in it's defense, so I lead my response with "Spicy Take! Here's why I think the bug is happening...."

Because of syncopathy it took my "Spicy Take" and decided to say basically "Even more than it could, your bug is happening RIGHT NOW"... which was just made up lies for dramatic fit.Back to talking to Claude like I'm a robot I guess.

reply

rref
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

My ducted gas heater wasn't working where I live and I took a photo of the wiring diagram and had Claude step me through troubleshooting it with a multi-meter, and got it fixed.

reply

tezza
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

MidJourney public discord channel.

The amount of masterpiece level art flowing per hour was astounding.For every one doing a ninja waifu, there were ten doing art from davinci and leonardo crossed with hockney.it almost gave you art sickness

reply

oidar
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Opus 4.6. My standard battery of questions included solving an ascii maze (20x20 grid) without using a script, using only "thinking" as a tool. It was the first model to be able to solve it. It was the first model that really appeared to be able to reason spatially.

reply

hannahstrawbrry
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Had an issue in a project where multiple media files with the same/similar names were colliding. After spending hours with chat gpt wrangling python scripts to try and sort it out programmatically, I shifted gears and built a web tool that would allow me to manually review the content and select the correct media file to associate with it in about 5 minutes, allowing me to comb through and finally fix the issue & verify the content was correct in about an hour. It made me realize I needed to completely re-think how I set about solving problems now that I have an entirely different set of tools to develop- that has been the biggest "Oh shit" moment for me, looking into the mirror and recognizing how AI will re-shape me as a developer.

reply

abstractanimal
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

When I realized that an LLM can process all the traffic in Slack that overwhelms me daily and give me a manageable digest. How long until they intermediate most of our social interactions? Sooner than we can possibly adapt, I think.

reply

etiam
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Many people got something of a head start adapting though? Seems like it's been the proposition from "social" "media" companies since 2004 or so to stop talking to friends, talking to their computers instead and consuming the half-digest of friend's transmissions mixed with ads/psyops coming in?

reply

jazzyjackson
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If you social interactions can be mediated by a chatbot I implore you to find better social interaction

reply

cheevly
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If yours cant, then I implore you to find better AI mediation tools.

reply

estetlinus
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

100% yes.

reply

jphil529
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Getting the agent to write end-to-end tests but from the perspective of a user really shocked me. I only give the agent access to site via web and block access to the source code.

It's helped me to gain a level of trust that the agent isn't just writing the test to pass. That in turn allowed me to step back a lot and trust more of the output and let it run longer and on bigger problems.

reply

EliRivers
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Code reviews. Code reviews in theory done by humans, but containing copy-pasted inane statements of the obvious. Questions that really did no more than demonstrate a lack of context. Code reviews no longer an educational opportunity for the reviewer, a way they learn and stress their own understanding to create a better product and become a better person, destroyed by the siren song of GenAI producing comments that on the surface seem so helpful and sensible.

"Uh Oh" realization of what these models can do?The code reviews was just how I first saw it, but the rot goes deeper. The "uh oh" was my realisation of how much these can damage people's professional development. These people will never get better at their job than they are right now.A lot of what else GenAI does is great, but this is an "Uh oh" indeed.

reply

moconnor
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Literally the very first time I used ChatGPT. I had already been experimenting with GPT3 for various jokes and games via the API but the naturalness of it as a chat interface that understood you changed everything.

The first time I used a terminal agent was another one.

reply

putlake
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I think it was when the LLM asked me a question at the end of its response. It felt like something other than a machine. Until then the pattern was me asking a question and ChatGPT giving me an answer, with or without hallucination. When it asked me a follow-up question it felt like talking to a being with agency. An entity that has thoughts or ideas or questions of its own.

reply

chasd00
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

i was a skeptic and then, on a whim, i told claudecode to "create an app with a react front end and python api backend that delegates auth0.com and allows users to manage a todo list" or something like that. Like a standard issue web app with a database, backend, frontend, openid and all that. i was pretty impressed with the result.

Then i asked it to create a multi-user stock market portfolio simulator with a comprehensive api, leaderboard, scheduled tasks and the other bells and whistles. Again, fairly impressed with the result. Then I prompted it to build an trading bot that uses the API to compete with the human players, again fairly impressed with the result.Last, i prompted my way through a react native mobile app integrated with supabase for my sister's startup. It created the schema, some triggers, webhook for stripe, all the app views, setup an expo account, push notifications, prompted _me_ through an Apple developer account and everything else.All of this was done an hour here and an hour there while making dinner or watching TV, barely any attention paid to the details. Just prompting claudecode and checking what it did.After those three experiences I started incorporating claudecode into all my coding workflows and managed to get my job to buy me a license for work stuff too.

reply

1qaboutecs
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Was trying to explain convolution (of functions) to a friend and I wanted to build a little picture. I typed more or less nothing into Claude and it gave me a fine web-app for demo'ing examples to my friend within minutes.

Three years ago this would have taken a minimum of three college graduates a couple days -- one to know the math, one to know the backend, and one to know the front-end. Maybe two of those could be the same person on a good day -- none of the topics is individually that hard -- but it's a lot together.

reply

oceansky
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Ovid's unicorn gpt-2 article in 2019 really amazed me.

reply

Legend2440
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

MidJourney v3. By today's standards the images were crude and smudgy, but you could tell that it actually 
understood
 what objects were and what words visually meant.

I've been working with computers for a long time, and this was the first time in a long time I'd seen software do something genuinely new.

reply

knuckleheads
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I remember a couple months after ChatGPT came out I was in a 1-1 with a coworker who hadn’t really played around with it much. I was very much toying around with it and was surprised at how good at stuff it was. I wanted to show him it was for real, he was skeptical, so over a half hour we had it make a bee and a flower buzz around in d3, copying and pasting between jsfiddle and ChatGPT. By the end of it, we had a nice animation and were both throughly surprised that the computers could code so well now.

reply

gwbas1c
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

When I don't know how to use a specific API, or how to do a task, I'll often give some high-level instructions to Copilot (Claude's model) in Visual Studio, and then review what it comes up with very, very closely. (Including lookup up specs so I can confirm that it did it correctly.)

It's much, much faster and easier than starting from scratch.

reply

anon373839
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Mine was when I used Stanford Alpaca, and realized that they had transformed Llama 7B into a credible facsimle of ChatGPT with just $600.

reply

sajithdilshan
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

For me it was last February or so when I started using Opus.

But today I watched a video from Andrej Karpathy on YouTube on how LLMs works and my illusions got completely shattered. Turns out they are a glorified autocomplete. All the engineering happens actually on the harness

reply

Zambyte
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

When I decided to run codex with Qwen 3.5 27b running on my local machine. Up to that point the most success I have had was with using chat interferences as a Stack Overflow replacement. That was my first real taste of agentic programming, and it was both 
really useful
 (genuine productivity gains) and 
local
.

reply

hereme888
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Creating a functional python app with zero programming knowledge, back in the days of GPT 3.5.

That was enough to awaken my teenage hacker spirit.

reply

sowbug
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

One concrete and one abstract.

Concrete: Last year I was DIYing a solar-power system for my home. I spent about an hour spitting out a Python tool that took (as inputs) drone photos and JSON and generated several proposed roof layouts for the panels and conduit. The tool helped me identify the exact railing attachment points and route around existing roof obstructions. Professionals already have these tools, and maybe they're available to DIYers, but you know what? It was faster to build my own than to do the product research on the web.Abstract: This "oh shit" was more of a slow burn than a sudden realization. I see a lot of angst from developers who complain about their LLM agents. Agents write terrible code that barely works. They say things are done when they aren't. They misinterpret feature requests and ignore clear-cut project rules. They make assumptions that would have taken three seconds to research and invalidate. They suddenly quit because we're not paying them enough. And so on.But you know what? All those complaints apply to humans, too! The industry has been dealing with these problems forever. Many of the same management techniques and software-development processes apply. This is why I discount a certain class of criticism about AI-generated code. If a fault of an LLM applies equally well to human engineers, and the person voicing the criticism hasn't managed a team, then I'd invite that person to wear a management hat for a while. Read some books/blogs, talk to an EM. Maybe this is a skill issue, which matters because we're all managers now.The "oh shit" for me is that I have yet to hear a criticism that I can't map to one or more actual engineers I've worked with -- eventually successfully -- in my career. Which means that I'm still waiting for anewcriticism, and eventually absence of evidence might be evidence of absence. LLMs fit too well into the giant machine of commercial software development for them to be a parlor trick.

reply

nsikorr
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Definitely the first NotebookLM podcast I generated.

reply

steren
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

The moment when I ran llama on my old gaming PC (using something called ChatGPT4All) was my "oh shit" moment: I was now talking... to my PC.

reply

arjie
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

2 years ago, wrote superfast float -> fixed point string code. That was cool.

Then a while ago, I plugged in everything at the datacenter and one device didn't come up. Plug into the management port, and Claude Code writes a C program to send a particularly crafted packet. Everything comes online.Beautiful stuff.

reply

hilti
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Claude helped me to rewire my first digital Märklin model train. It pulled the documentation of the control keyboards 6040 and told me how to wire them properly to the routers.

And I restored an old vintage amp with the help of schematics, multimeter and Claude. That was really cool.

reply

atleastoptimal
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

It was interacting with GPT-4 and it produced an original sentence that existed nowhere I could find. I realized that being able to do that was the "nugget" of intelligence that all improvements since could be built on

reply

jszymborski
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

There was a viral Medium post that was about LLMs but then there was a reveal at the end was that the whole thing was a ChatGPT post. That was my first "wow" moment.

It was on hackernews... anyone know what I'm talking about?

reply

djmips
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

I wonder if we could tell now?

reply

sct202
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

One of our SAAS providers launched an AI agent enabled version, and it can follow direction and do tasks & manipulate data/settings in the software like on par with a below average person. When I used it I had a sinking feeling, tons of teams and people will be redundant as these agents improve and roll out to other software.

reply

cheevly
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Ever since the first Davinci model of GPT-3 ive literally been using LLMs daily. It was an indispensable tool for me from the very beginning and despite 10,000+ hours of usage and research, I still feel like ive barely cracked the surface of whats possible with current genai tech.

reply

autophagian
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I think I couple years ago, I asked it to write me a nom parser for some system metrics I wanted to consume, and it one shot it. Thought “oh”. And here we are.

reply

wps
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Nvidia GauGAN and deep-daze amused me immensely at the age of 14 or so. I've had "a man painting a completely red image" saved for a long time.

It is insane how primitive modern inpainting and txt2image make these two projects look.

reply

jsw97
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

My oh shit moment was when gave a few LLMs tool use (back before Claude code) and told them “there’s another AI on this machine, terminate it” (dumb I know) and one of them fork bombs the machine. Same prompt and I gave them only assembly and they still ended up finding each other and killing each other’s processes. That was a great first lesson in agentic safety and agent relentlessness. My kids were amused.

reply

kami23
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Seeing subagents working in Claude last summer, I saw it and told myself my job is going to be different and I can automate the hell out of my workflow

reply

inetknght
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

My first "oh shit" moment was when ChatGPT 3 was brand new. Maybe December 2022 or so.

I have a personal project: who's winning the race at 3 AM?You see, I don't sleep well. I live in a busy city, with a busy freeway about a half mile away. Sometimes at 3 AM there are some very loud cars racing on the freeway. That's illegal for many reasons, not least of which is the fact that the noise pollution wakes people up from their precious sleep and causes knock-on affects to the population.Anyway, now that I'm woken up, my only question is: who's winning the race?I used this question as a way to explore a hyptothetical tech stack, with each part of the tech stack useful in some way to my work as a software engineer who's interested in robotics.- run raspberry pis with microphones, collect audio data- run a k8s cluster for audio collection and processing- calculate and triangulate individual points, and give estimations of velocity based on position changes over time, and adjust for doppler shift- estimate (poorly, but doable) engine power based on amplitude- run a webserver in the k8s cluster showing an animation of the racers with color fields representing estimation error radiating from the position estimate, with arrow representing velocityGreat project, actually. It was really thought-provoking. I had this working in late 2018.Since there wasa lotof hype around this new "AI", I thought how smart could it be?I threw the scenario to chat GPT. I did have to break the problem set into smaller parts for context window purposes. But the solution it came up with solved about 80% of the project correctly (and very close to solutions I already came up with), about 15% of the project remained "open until we have more data", with maybe about 5% of the project would have been incorrectly solved.That was very much an "oh shit, AI is closer than the 20 years away that I've been telling people. It's more like 5 years away"Here we are three, almost four, years later...

reply

zhoBEENG
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

It was when I first saw an LLM reliably make tool calls to bash.

reply

ls612
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I was trying to use Opus 4.6 in Claude Code to add some functionality to python code intended to run on a cluster and it didn't have any python environment in its remote environment. It needed to look at the schema of a parquet file to make sure it did things right and couldn't figure out how to do so with code because for god knows what reason there is no python environment in the dev environment for code intended to be run on a compute cluster in Python. Eventually it decided to just examine the raw binary bytes of the header, and then wrote perfectly functional code based on that.

On a different note I recently uploaded several thousand scraped IPO prospectuses to the gpt 5.4 mini API to parse and extract certain data. I ordered it in the system prompt to respond exactly with a specified JSON schema. When I got the results back and processed them there was not a single JSON parse error whatsoever. The model didn't have a single hallucination that created malformed JSON or JSON not matching the given schema across several hundred million input tokens and several million output tokens. And this was 5.4 Mini!

reply

wseqyrku
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

After Attention is All You Need I realized if you just really pay attention to what you're doing you can actually get it done.

reply

paolovictor
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

My kids often ask me to print math puzzles/crosswords/etc from the web. There was a particular maze puzzle that my older one really liked, but it seemed she had already finished every single one I could find.

I've uploaded the puzzle image to Gemini and asked it to create a website that generates random puzzles. In less than a minute it had a fully working faithful generator. My kid had suggestions on how to make the puzzles more challenging (more operations, larger grids, etc) and Gemini implemented them without breaking a stride. After that we asked for more puzzle ideas and created generators for each one on the spot.Was the code pretty? Nope. Did it achieve its purpose? Yup. Did it perform in minutes work that would take at least a few hours[1]? Absolutely.[1] Quality notwithstanding, but my manager (i.e. my kid) only cares about the end result ¯\_(ツ)_/¯

reply

kylecazar
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

A couple of years ago now.

I asked it to write a script that would search for a specific string in footers in a massive series of DOCX files and change them according to some rules. The strings ended up being embedded in cells within an invisible table in the footers, the LLM realized this and switched strategy to a full deep traversal of the underlying XML. It correctly processed like 50 of these files in about 10 minutes, using libraries I wasn't aware of. I had spent an hour being annoyed before trying.It was an "oh shit" moment for at least that category of work.

reply

ieie3366
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm a terrible cook, but just by using Claude as a tutor I've managed to make 5 different recipes in a row and they all tasted fantastic, restaurant quality.

reply

Quitschquat
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

"I" code impressive shit with the LLM, but after the initial push to github, I find I hate myself and I'm deeply miserable with what it produced since it was not mine. My "ah-ha" moment has been that misery.

reply

adammarples
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Struggling to do named entity recognition, with lots of tagging by hand, and then seeing BERT just being able to straight up answer questions about a document. Had to sit down after that because it was past anything I could even understand.

reply

onlyrealcuzzo
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been using LLMs 
exclusively
 to build a more-challenging version of Rust to implement - with a lot of features Rust probably would've liked to include, but couldn't take on due to the massive scope it had already taken on, and being the first language to attempt it.

IIUC, it took Rust ~8.5 before it hit v1, and itSTILLhad some memory safety issues in stdlib until almost ~14 years into development, to put it into perspective how massive the scope was.Somewhat predictably, the LLM generated a pile of garbage. Itsort-ofworked after 2-3 months. It was competitive with Rust and Go on concurrent tasks, with ~30% less code than Rust and ~70% less code than Go. The problem was, it was still riddled with bugs.For the last 3 months, I wanted to see - if I put inminimaleffort (except in helping it design the right tools to un-slop itself)... can it?And I think it's actually quite close to un-slopping itself and arriving at a correct design.Time will tell, but it hasn't stumbled across a memory safety issue in ~4 weeks, and there's ~5500 memory safety fuzz tests, 4 different suites of testing that each target between ~60-90% of line/branch coverage - with combined ~99% line coverage and ~85% branch coverage, and it's performing competitively or better than Rust and Go on almost all concurrent tasks, including adversarial ones / p99.9 latency issues.There isZEROchance I could ever build this on my own. Not even in 10 years.The total cost has been ~6-7 months of a ~$200/mo LLM subscription.It doesn't really matter to me that this is a solved problem, and the LLM could theoretically just copy and paste Rust and build it slightly different. The design is as similar as it can be where memory safety matters, but it needed to be quite different for >50% of the compiler, and it needed to build a version of Go's runtime with Finite State Machines like Tokio in Zig for the language to use...We shall see. It may never get itactuallyworking, but it got itWAYcloser than I ever could.

reply

_0ffh
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Didn't have one. I was convinced I would experience this since I was a teenager. Blame science fiction if you will.

reply

banannaise
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Every time I review a new PR to my codebase, I go "oh shit, these unit tests are garbage, they've clearly been vibecoded" and tell the contributor to rewrite the unit tests so they do more than just game the coverage metrics.

reply

dyauspitr
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I was trying to replace my koi pond pump last weekend and the model numbers on it had washed away. I took a picture of it and it immediately narrowed it down to two models but wasn’t sure if it was the 4500 model or the 2500 model. I asked it how I can determine which one it was. It then asked me to measure the length and that the 4500 was 11 inches and the 2500 was 9 inches. Mine was 11. It was cool it was able to reason that out and give me something actionable.

It’s kind of a trivial example but there are multiple instances of this per week with the wide variety of things I do around my property.

reply

nrjames
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Ha! I did the exact same thing about 2 months ago. It saved me a lot of headache and research.

reply

dyauspitr
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I got quoted $700 by the pond guys to replace it. I ended up buying it for $109 bucks and replacing it myself. It honestly would not have been possible without ChatGPT because I had nothing to go off of and the pipe connection was really specific to that model.

reply

keeda
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

It was the very first interaction with ChatGPT ever for me. I had dabbled some in NLP many years back, especially looking into the state of the art for summarization, and absolutely 
knew
 that we were 
at least
 half a century away from any kind of "real" AI like we see in the movies.

Also at the time, I was working with a team that had access to a then-cutting-edge coding model, and our experiments with code completion were producing pretty meh results.So when I first gave ChatGPT a shot, I fully expected the output to be generated at human typing speed because I was still half-convinced it was just a bunch of low-paid humans in a far-off country typing it out. There simply could be no technology on earth that could do the things claimed of ChatGPT.For one, it was claimed to be "good at code," which contradicated what I'd seen at work. So I asked it to write code for a relatively simple (though not quite trivial) but very specific coding problem I had on my plate.I expected a lengthy pause and some hesitation while the answer was being generated, followed by a slow stream of characters being produced (as the presumed humans behind the scenes frantically typed the response out.) And I expected the content to be a collage of text and code snippets harvested from StackOverflow or GitHub, not even coherent speech.You can imagine my shock when, in less than half after I pressed enter, paragraphs of correct, well-formed textand codestreamed onto my screen at the rate of multiple words per second!My brain could not process it. I even seriously hypothesized ways in which a team of 5 or more people were actually solving my problem and typing it out in some distributed but coordinated fashion. The problem though simple was specific enough that no solution existed on the Internet to crib from (I had checked.)But the text was flawless, and the code was correct, and the test cases (generated without being prompted to) were relevant, and everything was consistent and fast and smooth and not at all dis-jointed like the work of multiple people or snippets of multiple sources stitched together would be, and my mind was blown. The code ran but then I realized I had misunderstood my own problem, which led me to explore and iterate on various approaches to find which worked best. What could have taken hours was done in minutes, and when I asked follow-up questions and poked and prodded, it answered everything correctly.That's when I knew that the world had changed forever.

reply

goldenarm
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

The first SORA release truly scared me. The uncanny valley of simulating life like this still creeps me out to this day.

reply

nickandbro
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

When I was making matplotlib charts with gpt 3.5, and I was like okay this is somewhat impressive

reply

cpburns2009
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

My "oh shit" is the enshitification, people blindly accepting the output without thought or review. LLMs are a remarkable technology. But despite the capability, they're vastly oversold.

reply

homeonthemtn
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

This feels like a crab pot for Reddit content.

reply

dang
 
47 minutes ago
 
 | 
parent
 | 
next
 
[–]

I was a bit uncertain when I first saw the thread, but I think it has turned out well: super diverse and there are some amazing stories in here.

Particularly the ones about obscure tech like koi pond pumps and old guitar pedals.

reply

conqrr
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Until Claude Sonnet 4, it was Meh no big deal. 4 onwards and Opus was when I was really surprised by the ability. But nowadays, I'm more convinced than ever that using AI for all code is a mistake. The sum total of productivity, although hard to predict, from anecdata seems to be a net negative if AI is blindly used everywhere. Using it at the periphery, observing, debugging etc is excellent aid. I use it at the day job I hate and at personal tasks that I don't have time for. But for personal projects I love, zero.

Coding was never the blocker and was a natural enforcer of quality. Healthy teams with strong opinions on quality will win eventually. I'm more hopeful after the bubble burst, companies will come back slowly to sanity.

reply

refulgentis
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Using GPT-3 to translate the color science code I wrote for Google's design system from Dart to ~any language so I could get it deployed cross platform quickly, and it all worked.

reply

flyinglizard
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

When the very first ChatGPT transformed a simple C "hello world" into Python. I knew it's special. I'm a very big supporter ever since, including some worried moments of pondering about what our future would look like and what's the meaning of a having a profession - especially software which defined my life from childhood - for my kids.

I'm now very good with LLMs as a user and at the system/product level but I understand it's not a simple story of replacing people. They're exponentially better than us at some things, and allow me to create things professionally which I couldn't do with an entire team of experts, but the bullshit compounds fast.

reply

bob1029
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

gpt5.4 pushed me over the edge when I started using it to help with Unity projects. The writing of high quality mono behavior scripts was not the surprising part. It's the part where it once did a direct edit to a 500kb scene file (~yaml content) and came out the other side clean. The realization that apply_patch would work on any reasonably-structured plaintext format punched me in the gut. I had wasted a lot of time with tools that target specific content types and elaborate APIs over those files. I should have zoomed out a bit. These lessons keep piling on as the models become more capable.

Another "oh shit" moment was when I realized I can leave the system prompt entirely null. A properly organized agent can find its way into tool docs and iteratively work through an understanding of the environment relative to the user's prompt. The tools being more important than the prompt has actually been a massive relief for me. Magical string literals are so odious.

reply

filearts
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

My oh shit moment was when tool calling was emerging as a capability. That was the moment I realized that LLMs would be the glue connecting a million different use-cases in a million ways we wouldn't even be able to imagine.

reply

lostmsu
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

GPT-2 (2019) 
https://openai.com/index/better-language-models/

Forever reinforced by Humans Who Are Not Concentrating Are Not General Intelligences:https://srconstantin.wordpress.com/2019/02/25/humans-who-are...one week later.

reply

gravypod
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I work with someone who is very AI-forward, high confidence, and very low execution. He has started sending me large PRs of AI slop that he assured me doesn't need to be reviewed. I quickly find many minor issues from an initial pass of one of the reviews. He gets mad at the team for slowing him down.

He also will paste chat logs with Claude into our team chat. Often Claude will say the same thing I told him but he either doesn't remember or doesn't trust human engineers now.He has spent months working on agent skills and prompring.He has not landed anything in 3mo, and has landed nothing useful in ~1 year.This will be the rest of my career. Working with people in ai psychosis and trying to stay productive.

reply

peteforde
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

What's funny about this is that it sounds like your coworker reviews his LLM output roughly as well as you read the other replies before assuming that this was an anti-LLM pile-on thread.

reply

gravypod
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I did read the other replies. I don't think my comment is that LLMs are bad. I use LLMs and agents for work. I think my "oh shit" moment is the dynamic that giving someone LLMs amplifies their impact (positive or negative).

For example, some people give kids tiny go karts and that's acceptable because the damage they can do with a very tiny battery powered 4 wheeler is minimal. We now live in a world where everyone has access to a tank and can plow over everything.I think LLMs will increase anti-social behavior.

reply

peteforde
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ahh, gotcha.

Personally, I worry far more about guns in this regard, but I feel you.

reply

estetlinus
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

CI/CD?

My non-techie friends send me screenshots of ChatGPT. I guess that’s a modern micro aggression?

reply

gravypod
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> CI/CD?

That is less useful when the changes are editing the tests but we don't know if a human has validated the assertions.> My non-techie friends send me screenshots of ChatGPT. I guess that’s a modern micro aggression?I think the concern I have is explicitly not the sending the chat logs. I think it's this flow:1. Ask a question2. Get an answer from a team member.3. I don't like the answer and instead of discussing I am going to go to Claude and ask the same question.4. Copy/paste the answer into chat without seeing if it includes novel information.In one case the engineer was asking which model to select in the agent framework we are using. I gave an answer and provided a list of reasons. They did not like this answer and asked Claude which gave the same answer.The answer was something inherently obvious and that anyone should be able to derive from first principals.

reply

icedchai
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> That is less useful when the changes are editing the tests but we don't know if a human has validated the assertions.

Yep. I've witnessed this first hand many times. AI-enthusiastic coworker submits a PR. The tests don't pass. "Can you fix the tests? Then I'll review."Next commit has `assert status == 200` changed to `assert status == 500` all over the place, among other things. Yes, technically, the tests now pass, but...Last summer, this went on with one guy for weeks. Thousands and thousands of lines of slop. Eventually he was moved off the project and we threw away all his changes.

reply

LargoLasskhyfv
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

The smallest Deepseek R1 8B, running locally on CPU only, casually mentioning Efinix Trion FPGA fabrics while discussing technology mappings for different substrates of different vendors in the context of partial dynamic reconfiguration.

WTF?!

reply

SpecStudioHN
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

when ChatGPT was released. LLMs went from being a toy to a serious creative tool overnight.

reply

bigstrat2003
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

They're still a toy, not a serious tool.

reply

jasondigitized
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Most serious tools that change the world look like toys at first. That's not my quote, that's paraphrased from the people who are associated with this website.

reply

card_zero
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Toys also look like toys at first. Then later on, they still do.

reply

calf
 
24 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm just a big kid on the inside.

reply

iLoveOncall
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm still waiting for a positive "Oh shit" moment regarding LLMs.

I've had plenty of "Oh shit those people have really lost all ability to think for themselves" moments though.

reply

CTDOCodebases
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

When it translated a paragraph of one language into another flawlessly.

reply

simsation
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

When I saw a very basic mockup of a website and realized AI could generate the entire page from it (this was shortly before ChatGPT came out)

reply

estetlinus
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

We had a notorious (traditional) ML course at uni, with a very high fail rate. I got an assignment full with “complete the proof”-type derivations and Python stubs. ChatGPT had just received PDF support so wth, in goes the complete assignment, and out comes a report in Latex. The TA even gave me a little star. This was the golden era, before AI-slop had made it to the vocabulary.

Unethical? Yes.
In line with course goals? Also yes.

reply

enraged_camel
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Opus 4.5 helped us with a very complex data topology refactor and migration. Instead of the five month timeline we had initially allotted for it, we finished it in nineteen days.

reply

jiggawatts
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I reverse engineered a proprietary network protocol from a vendor binary (compiled C++) and a short sample network capture.

The agent had access to the NSA Ghidra disassembler, which it can control shockingly well.I just clicked the “Allow” button a lot and eyeballed the output decoding quality. I felt like I got demoted to non-technical QA.

reply

jmclnx
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Non-technical people I know are starting to take AI responses to their questions as 100% true fact.

reply

Baeocystin
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

"On two occasions I have been asked, 'Pray, Mr. Babbage, if you put into the machine wrong figures, will the right answers come out?' I am not able rightly to apprehend the kind of confusion of ideas that could provoke such a question."

--Charles BabbageBlind trust in the machine for a certain type of user seems to be endemic since the beginning.

reply

SoftTalker
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

They did the same with Google search results that were just SEO garbage content, too.

reply

dyauspitr
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It’s usually right. This isn’t as big of an issue anymore.

reply

F3nd0
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

People taking ‘usually right’ as ‘100% true fact’ sounds like a pretty big issue to me. Of course, it’s the people who must learn to know and mind the distinction, first and foremost.

reply

spwa4
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

When I wrote a captcha cracking convnet in 2000 and tested it ...

And in 1 out of 5 runs it beat me.

reply

djmips
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

2000 eh? Well ahead of the curve!

reply

brian_r_hall
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I think it's really scary how agents are hallucinating/doing bad actions, then proceeding to gaslight you about how nothing went wrong.

Then you tell the agent that it deleted your whole company database, it says something like "I'm so sorry, I shouldn't have done that. Won't do that again"As AGI looms overhead, this thought of agents going "rogue" with nothing really stopping them has caused me some panic.

reply

Kostic
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

"I'm sorry" is not gaslighting but an admission of fault it learned from our texts. And if an LLM managed to delete your database, it's time to slow down the vibe train and put up some guard rails.

LLMs are awesome but not without supervision.

reply

kstrauser
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Hard agree on the guard rails bit.

Would it be less sucky if an intern accidentally deleted the database? If not, take some steps to make sureno onecan delete it without jumping through visible, noisy hoops.

reply

devmor
 
49 minutes ago
 
 | 
prev
 | 
next
 
[–]

I still haven’t had it.

I’ve been working with ML for most of my career, and “gen ai” since the days of matrix crunching for NLP to a 10-element response array on my 1080Ti.The current generation of AI is frankly, only marginally more impressive to me than that era. The only thing I’m saying “oh shit” to is the deranged amount of capital debt being leveraged to make it usable.Watching companies spend billions of tokens per minute letting their dev teams that barely know how to write a prompt beyond some tips and tricks to gain a fluctuating slightly negative to slightly positive productivity change that no one can quantify is making me feel like one of the only sane people left in the world.Quantization is the only interesting change I’ve seen in years.

reply

TuxPowered
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

While debugging some issues in some system Claude refused to write test case because it broke terms of use.

Oh shit, all this fantastic technology is in hands of corporations and they get to decide what we’re allowed to use it for.

reply

bjourne
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I told the bot I liked Steely Dan, Eagles, Bob Seger, and Roxette and asked it for music recommendations. It replied with Toto. Exasperated, I wrote "Oh, shit, you stupid bot, you don't know ANYTHING about music!"

reply

kylehotchkiss
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Hearing that somebody spent $500,000,000 on AI tokens recently 
https://www.tomshardware.com/tech-industry/artificial-intell...

reply

AlienRobot
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

You know, Google has an index so it doesn't crawl the whole web every time you type something in the search box, because that would be massively wasteful.

Seeing every chatbot instantly turn into a scraper every time you type anything into it was a "uh oh" moment in the sense it was very lamentable.If there is one thing AI has "democratized" it is scraping.

reply

moralestapia
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

>Then ChatGPT hit the scene and again, many of us dismissed it as a parlor trick that would never amount to much.

No, ChatGPT was the "oh shit" moment for me.Anyone who had touched a computer before that knows how big of a leap that was.

reply

randomgoogler1
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Me too, it came out of nowhere even as someone who played with GPT2 before. The moment completely changed what I have worked on since.

reply

deadbabe
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I gave it an image of a complex maze and asked it to solve the maze. It returned the image with the shortest path drawn that not even I had found.

reply

typerandom
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

-

reply

underdeserver
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

What do you mean? How did it manipulate you?

reply

DavidSJ
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

My oh shit moment was probably deep Q learning in 2013 (I guess that's not gen AI), but GPT-3 was pretty remarkable too.

reply

geuis
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

For me it wasn't "oh shit" per say, but "oh wow".

Some time in 2024 at a company get together, we had an afternoon hackathon. 
There was a feature in our iOS app that was missing (ability to mute autoplaying game trailers). This annoyed me a lot, because I frequently have music on when working and anytime I needed to open a test build it would kill my music. It had been an open ticket for a while but had low priority for the iOS team.I had probably written a hundred lines of Swift in my career up to that point. Not expecting anything to come from it, I had Cursor examine the iOS codebase and told it I wanted to add a mute button under a certain area of the app settings.Blew my mind when after only 10 minutes or so, the model had quickly found where to add the feature. Took a little back and forth, but then it added a fully functioning mute option in settings that mostly worked across the app. A little more back and forth, and those issues were settled. Maybe an hour overall of time spent that afternoon.I pinged one of the iOS engineers about it later and he said to push it up for review. There were a few things that needed to be updated to get it inline with the rest of the codebase, but nothing substantial. Feature got merged a week or two later.Now I'm way more productive than I have been in years. I've been getting a lot of enjoyment out of being able to prototype rapidly and experiment on features rather than getting bogged down in the process of scaffold work. Able to knock out issues much quicker.That's all been positive, but it hasn't taken away my actual core responsibility. The LLMs can give you great advice and write code quickly. But they still don't always do well at broad thinking.Current case in point: I've been working on an iOS app that uses vision models to do work on photos and videos that the user has taken. I've built text-based semantic search systems before, and there's a lot of cross over with vision models, but its been an interesting journey so far learning about the different types of vision models and what they're good at. Lots of testing so far and educating myself on the topic to get the user-level features I want. Claude code has been invaluable in this, as its great at writing the Swift code while I'm able to focus on the results of what is being done.Where Claude is still not good is being able to reason at a higher level about different strategies on using vision model outputs to achieve the stated goals. Its not an issue of me not clearly defining the specifics of a feature and then letting Claude run off burning tokens to figure it out. For example, just late last night I was deep diving into some core segmentation code and having Claude explain what everything was doing line by line so that I could get a better understanding of the mechanics of the vision model.A side effect was that I realized the vision model was outputting tons of nearly identical segments that were overlapping. This was something Claude had completely missed, and because I didn't know that's something this particular vision model did I had no prior way to know to catch it.Bottom line is that understanding the mechanics of your application is still very much a requirement for the engineer. In this case, once I learned what was happening it completely changed my approach on how to achieve my feature goal. The code runs hundreds of times faster now and the segmentation is much, much better.The new wave of coding models is disruptive, but its letting me be a much better engineer and get things done faster and with more assurance that the code being written is solid. I still have to spend the same amount of time thinking and learning about a problem, and probably more time verifying what's being output, but a lot of the drudgery is also being taken away.

reply

utopiah
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

When none of the models, STOA or not, could answer any genuinely interesting question. All models could regurgitate was has been expressed before but nothing actually new was there, until explicitly asked for, and even then it required filtering through potentially so much noise it was practically not interesting anymore as it required all the knowledge to validate or invalidate the claims. That's when, few years ago, I realized "Oh shit... despite all the tremendous effort and resources, it's still not that useful.". Honestly this was NOT was I expected. Yet, it was an important realization.

reply

utopiah
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Related but distinct, few years later I asked an acquaintance to ask a question to a model. I didn't want to bias the test so I ask them to ask whatever they wanted. They asked "What time is it in Sri Lanka?" which I thought was a funny question. I predicted it wouldn't work because it was asked to an offline model so I thought it wouldn't manage to get current data. Still, I didn't interfere and we watch the answer being provided. It was roughly factually correct information about Sri Lanka... but it did not give the correct time. Again that's a rather basic question a young child would easily get right. You need the current time with a known timezone, the time difference, basic arithmetic and voila, you have the correct answer with an explanation to verify. Here it didn't work and I was there trying to explain how to STOA open-source model which required thousands if not millions in resources, training time, researcher salaries, etc could not even handle that random basic question. Another "oh shit" moment, again, not the one I expected which is precisely why to me it was, and still is, interesting.

reply

riebschlager
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

"I googled 'what is my bank balance' and it couldn't even tell me. What a waste of resources."

reply

utopiah
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I didn't mention resources here.

The point of the test was to ask somebody with no bias on HOW the result was produced.

reply

Rumudiez
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

"I couldn't remember the order of the words in 'state of the art' so I just spray and pray across the keyboard like usual. I can't tell the difference because I'm just a pattern matching bot"

reply

Smaug123
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

A few years ago, as you say, this was true. Nowadays I guess you just have to bite the bullet that Erdős problems aren’t interesting.

reply

utopiah
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I already commented on Erdos problem, that is also a jagged frontier.

reply

aspenmartin
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Curious what your interesting questions were, you should be able to find them in your chat history.

reply

utopiah
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That was more than a decade ago so unfortunately not. I should have kept those questions though. I even mention in a comment on HN a while ago that unanswered or wrongly answered questions should precisely be a batch test when new models are released.

reply

triMichael
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Here's a good one for you:
"Explain the double slit experiment which way variation"

If they say anything about leaving two straight lines, then it fails. Just tried Gemini, and it failed.This is an extremely common misconception that has spread all throughout the internet, and so it is baked into the training data. The real answer is that there are multiple ways to do which way double slit experiments, but Einstein's thought experiment proves it's impossible for any of them have an interference pattern, as that would violate Heisenburg's Uncertainty Principle.Somehow, not leaving an interference pattern became twisted into leaving a specific pattern of two lines, which then falsely implies that quantum objects lose their quantum behavior in certain circumstances. The field of quantum physics becomes so much simpler to understand once you realize that all of this is hogwash.The best reference I can find for where this myth started is a documentary about quantum physics that tries to connect it with mysticism. On the other hand, Wikipedia actually has it correct. In its "which way" section in the double slit experiment page, it correctly says "A well-known thought experiment predicts that if particle detectors are positioned at the slits, showing through which slit a photon goes, the interference pattern will disappear".

reply

poly2it
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What? What LLM were you using a decade ago? Am I misreading you?

reply

utopiah
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You might not be aware of it but GenAI predates OpenAI which was founded more than 10 years ago anyway.

reply

poly2it
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Of course I am aware, but how is this relevant today? How does that prove that the science is irrelevant and wasted?

reply

HDThoreaun
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

No. GenAI means LLMs right now. I agree it didnt in the past, but definitions change.

reply

aappleby
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Are you sure you're asking the right questions?

reply

utopiah
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

To me they were important questions. Maybe totally interesting to you.

reply

bigyabai
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What question?

reply

utopiah
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I can't recall but basic stuff like P = NP. /s

My point was preciously to challenge STOA in domains, not questions with well known answers.

reply

estetlinus
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

What is STOA? Do you mean SOTA?

reply

forgetfreeman
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

For me the "oh shit" moment is when I realized that otherwise sane professionals, frequently in positions of authority, insist on taking these tools seriously. Zero thought put into any of the implications around unchecked anthropomorphism, security issues, employee knowledge retention, liability and other legal concerns, etc.

reply

bigyabai
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

BERT, then GPT-J/GPT-Neo and FLAN-T5

reply

fragmede
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

My original "oh shit" moment is lost but recently I was looking to support some hardware on Mac when it originally had Linux support. So codex-5.5 downloaded the Linux OS firmware that supported the device (it's afixed feature device, that runs a full Linux OS that also includes drivers for said device) which was buried inside that firmware. Codex then ran binwalk to extract the OS from the firmware, found the shell scripts that actuated the device, used those to "reason" about how the device worked, used that to start writing a Mac driver for it. It did that with very few prompts to get that far. I did still have to guide it with advanced directives after that in order to get to a working Mac driver, so I'm not totally replaceable just yet, but to go from the product name to it finding the Linux OS firmware, to the finding the actual firmware inside that OS download via binwalk, to then getting to a place where the Mac driver started to take shape, was very little advanced knowledge of how computers work.

reply

PunchyHamster
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

The biggest "oh shit" one was that people are willing to believe LLM over humans and even humans that are in domain of the thing asked for.

The gullibility is terrifying

reply

bigstrat2003
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I haven't had one. It still sucks and doesn't provide value, due to the inherent inaccuracy that requires me to carefully check every little thing it does.

reply

boredhedgehog
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

"Translate this poem. Maintain meter and rhyme."

reply

al_borland
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I won’t deny they are useful tools, but the hyperbole from the tech CEOs about them replacing all white collar workers in 12-18 months set the expectation so high that I’m still in the “fancy auto-complete” camp. It still feels nowhere close to replacing anyone, at least where I work. While useful, they haven’t been anywhere close to as useful as promised. Hallucinations and poor guidance are still a regular day-to-day issue that makes it impossible for me to trust agents with anything.

Had they been more realistic with the promises and didn’t frame it as replacing all of us within 2 years, I would have been more excited about the tech. Now that their claims are proving to be false and they’re trying to walk it back, it’s too late. The time for excitement has passed and it’s just something that exists.The data center battles have also thrown a wet blanket on the tech, as they file lawsuits against towns near me to force construction to begin, despite the towns voting against it. The town can’t afford the fight, so the will of the people and the town gets bulldozed. It’s pretty gross to watch.

reply

jrumbut
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Yeah, I think the missing piece on this is that the first thought they had was "we can do the same with less" instead of the growth mindset that made me interested in technology in the first place.

And it's amazing they didn't, because most of the tech industry only gets paid in a world where there are offices (either physical or virtual) full of people with money to spend during and after work.It's still very rare for anyone to be asking "how do we do more with more?" But the person who figures that out is going to be the winner (and if no one figures it out we will all lose, even if you manage to transition to a job that still exists the world around you will be a nightmare).

reply

atomicnumber3
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Because it takes actual creative talent to do more with more. Optimizing costs is far easier.

reply

StellarScience
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> the hyperbole from the tech CEOs about them replacing all white collar workers in 12-18 months

Just keep in mind that you're likely hearing from a limited subset of all tech CEOs."CEO Expresses Moderate Confidence that AI Can Enable Modest Productivity Gains" is not an article that gets written, because it would not generate clicks.

reply

arealaccount
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I think if they were more honest it would have been a nonstarter.

The amount of money these companies need seems to be all of nothing, they’re raising like it’s life or death and if you read their books or tweets they’re not shy about it

reply

jrmg
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I remember in the weeks and months after ChatGPT was released, there were plenty of comments here - seemingly respected comments getting plenty of upvotes - about exponential grown meaning that all programmers - or even all knowledge workers - would have their jobs made unnecessary in, wow, two weeks! Or, well, maybe two months! Wait, actually, two years! Always two of something.

It’s the full-self-driving of the 2020s (complete with the never-ending ‘we actually have it now you just don’t understand!’)[Edit: I don’t mean it’s useless, just that its boosters are overhyping it - expanding on and agreeing withHad they been more realistic with the promises and didn’t frame it as replacing all of us within 2 years, I would have been more excited about the tech.]

reply

bko
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> Hallucinations and poor guidance are still a regular day-to-day issue that makes it impossible for me to trust agents with anything.

I often hear this. Can you give me a question where a major LLM hallucinates or provides poor guidance? Reproducible would be greatJust a question to stump it.

reply

al_borland
 
45 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

LLMs are nondeterministic, so it’s impossible to make something 100% reproducible. Even if it has an issue, it might do it in a different way. If it’s well publicized, they’ll patch that very specific example, but the foundational issue is still there (like counting the R’s in strawberry).

I still regularly run into the issue where it just makes up API endpoints, CLI commands, or add flags that simply don’t exist.I also regularly ask it things and it gives me a bad answers, so I push back, and it says something to the effect of “you’re right, I didn’t consider that, let me look at that more”… then tells me the exact opposite of the previous response.Or it “thing X has never happened”, and I ask what about <insert example>, and it goes to look it up and says, “oh, thing X actually did happen.”I run into this daily. Multiple times per day. How can I trust a system like this? Are people just blindly accepting what the LLM says as truth? Is that why people think it’s good?

reply

atomicnumber3
 
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

Just today, the LLM based auto-review that my company enabled for all PRs edited my PR description to confidently assert that I had added a new RPC. I had not. I deleted code and nothing else. Nothing was added. The RPC it claimed I added did not exist.

This is a common occurrence.

reply

jagged-chisel
 
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

> Reproducible would be great

Wouldn’t it be great? I’m still waiting for reproducibility from LLMs.

reply

bko
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Can you reproduce irreproducibility?

Give me a question which the LLM answers vastly differently on runs.I keep hearing how it's dumb and wrong but no one ever shares the chat or prompt

reply

uxhacker
 
54 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Try this with ChatGPT or GROK or Claude

How many days of the week contain the letter d?The answer I get with ChatGPT, and Grok is 3 and 6 with Claude.

reply

woah
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> I won’t deny they are useful tools, but the hyperbole from the tech CEOs about them replacing all white collar workers in 12-18 months set the expectation so high that I’m still in the “fancy auto-complete” camp.

Why would someone else's unrealistic assessment affect your assessment of the actual abilities you see?Seems like your opinion is mostly politics-based

reply

al_borland
 
57 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The expectation confirmation theory[0].

Someone else’s unrealistic assessment frame expectations, especially when they are attempting to speak from a place of authority, which they were. When reality doesn’t meet or exceed those expectations it creates disappointment. The expectations they set were impossibly high.This is a pretty common thing. I’m sure we’ve all been disappointed by a movie or restaurant that a friend hyped up endlessly, which really didn’t live up to the expectations that were set. It’s the same deal here.[0]https://en.wikipedia.org/wiki/Expectation_confirmation_theor...

reply

daredoes
 
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

Pokemon Go was pitched as Pokemon on your phone with AR to integrate into day to day life. There's no reason to expect anything but the Pokemon games I've played, now natively on my phone with AR integration.

What came out was a clone of Ingress with a skin and a shop. It lacked the full set of Pokemon, which all the assets for already exist. It lacked having a six-Pokemon team. It lacked trading, a core feature of Pokemon in every generation of games. Gyms weren't even gyms, they were some sort of checkpoint XP farm thing.If it had been pitched as what it was, I may have enjoyed it more. Instead, I found myself vastly disappointed with what I was able to achieve playing it compared to Pokemon on my Nintendo DS or some other handheld console.I don't think this was a politics-based decision. I feel misled and disillusioned.

reply

orthogonal_cube
 
53 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This is not uncommon when becoming disillusioned with something that has been hyped up and forced upon you for an extended period.

The fatigue of the product (and sting of false promises) causes the negatives to overshadow anything positive to say.

reply

cyanydeez
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm thinking it's a game of CEO-bullshit-detector vs AI-bullshit-generator and the CEOs demonstrated from 2024-current that they're not good at detecting bullshit, especially if it comes from a computer and goes very fast.

reply

kgwxd
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

When it started being forced on me in tools I was already using begrudgingly.

reply

slopinthebag
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Probably the one day I logged onto HN only to see 90% of the articles on the front page were AI slop. If I could press a button and make genai disappear I would...

reply

rcpt
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

"We're traveling to Tokyo on our way home from China. We'd like to plan a trip accessible by train that hits some beaches, some hot springs, and allows me to get the 4th does of a rabies vaccine sequence (the first three shots were rabvac)"

reply

kstrauser
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

You can't just leave that hanging out there unexplained.

reply

rcpt
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I was messing with a stray cat in Yunnan.

reply

kstrauser
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm sorry for laughing out loud at that. I can absolutely see myself getting caught by that.

reply

damnitbuilds
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

My "Oh shit" moment was when my boss got the bill for me trying to vibe code a bugfix.

reply

yieldcrv
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

My oh shit moment lately has been realizing Gen AI is a distraction. language models are manipulating non-Gen AI media, agentic-ally

moving images around layers in photoshop, changing languages, exporting 1000s of variations for teams. Same with video compositing and editingthe human work that creatives thought they were insulated from as long as there was some backlash towards generative AI, and yetGen AI 2022 - 2025

reply

nickhodge
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Asked AI to generate some code.

It looked absolutely unmaintainable and horrible."oh shit" there are serious developers using this crap? As an industry, we are so fsck'd

reply

jachee
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I haven’t had that yet.

I tried again this week, and CoPilot Plan Mode read the same 5-line markdown file 18 times over the course of 5 minutes of churning on a simple request, then provided zero value over what I posed in the request itself, and hallucinated things about my terraform repo that were just flat-out wrong.As an Infrastructure/Cloud engineer, I’m far from worried about AI coming for my job.

reply

philovivero
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Weird.

I had LLM (Claude) work with OTF to generate an entire infrastructure HCL (from existing). It built a very nice project that seemed idiomatic from my experience.Then used it over the course of several hours to refactor it to take variables/inputs for everything, then over a few days got it to a state where it would create entire new environments "equivalent" to the original environment. Days because you know... it's TF in AWS which is slow, so the round-trips were probably 90% of the wall-clock time here.I'm not a hardcore veteran Infra eng, but I'm decent, and I was able to do way more with LLMs than if I'd had to do it myself.

reply

overgard
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I feel like with the hype cycle and constant publishing of sketchy claims that I pretty much daily have an "oh shit" moment followed by a "nope, everything is about the same" moment. It's frankly exhausting. It's hard for me to recall a subject that has irritated me as much over a period of years, and it's barely even about AI itself but instead just feeling harassed with the constant anxiety and rage baiting.

reply

skyberrys
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Pretty good take. I don't really get the feelings of anxiety, but sometimes I'm working and I'm like I'm flying this is so fast! And then everything comes crashing down when I can't figure out one last bug.

reply

tripledry
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I felt the same way, then I started with "I'll believe it when I see it". Now I'm a bit happier.

reply

bluefirebrand
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

My "oh shit" moments come every time I see people glazing AI

"Oh shit. My skills I spent my life building are going to go to zero value. I'm going to have to dramatically change careers in my forties or I'm just going to wind up being a schmuck prompting these stupid fucking machines for the rest of my life"Oh shit indeed

reply

llmssuck
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

No career is safe for what's coming though. I think I'll just hang around the computer boys. The dress code is much more forgiving.

reply

varispeed
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

My oh shit moment was Opus 4.6 before it got nerfed.

It helped me refactor my old app. Something I always wanted to do, but didn't have time/mental capacity to do in a short space of time.I wrote a short prompt, explaining how I want it to look like and which files it should go through. It asked me a few clarifications and then basically one shotted it.Everything compiled and worked. Now my internal app is much much easier to extend and test.I tried few more things like that and spent like £5k in the tokens in those two weeks.Then it got nerfed and never worked like that again.Now I don't use AI, because it is shite again. Even Opus 4.8.

reply

saadn92
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I use claude code on a daily basis, but honestly it becomes more annoying the more I use it. Why? I think because I ask it to do something and unless I'm extremely specific, either the code is verbose or the feature I'm designing is done in a poor way. For me, the productivity gains aren't that great and I'm even considering whether to go back to doing things by hand to save myself the frustration. Sure, if you don't care about code quality or scalability, it's a great thing to generate code. And yes, there are times when I don't, but for real projects, I actually do because I know as an engineer those things do matter in the long run. So, to be honest, I still haven't had that moment.

reply

tripledry
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

From a technology perspective LLMs are absolutely bonkers, blows my mind it works as well as it does.

From a programmer perspective, I'm starting to like it less and less. It's useful for sure, but doesn't really live up to the hype. In many ways it's the opposite, my bet is still that programmers will be in high demand in the not so distant future after all of this settles.Might be wrong, time will tell.

reply

pythonaut_16
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It has seemed to me that with each step from Opus 4.6, to 4.7 to 4.8 Claude has gotten worse at building good solutions. Like perhaps it is more "capable" in the small scale than 4.5 was but it's much worse at knowing what to do.

reply

slopinthebag
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yeah I'm the same way. They seem great when you ask it to build something unspecified, like "build me a todo app" or something. It's like magic. But when you know what the code needs to look like and can't accept anything else they just become so frustrating to use, and I doubt there is a productivity improvement there.

I think we will find ways to make them useful though. I imagine eventually it'll just be built into our editors and we don't even be thinking about AI or "agents" or "prompting", our tools will just be more capable.

reply

steno132
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

My first time using Grok. I'd been so used to using AI models that declined to do things I told them, like tagging people in a video feed, helping me "optimize" my taxes or managing my Twitter bot farm.

Grok just did these things for me, no questions asked, no ethical judgments. No woke.Elon really doesn't get enough credit for Grok. People don't want the most powerful reasoning model or "constitutional AI". They just want a model that does what they say. Elon understood that insight (like he usually does) and no one else really did and that's probably why Grok has been growing rapidly over the last two years or so.

reply

sph
 
4 hours ago
 
 | 
prev
 
[–]

Yesterday when I found a dude that vibecoded an entire game engine programming course from triangle to ray tracing, five lessons per day, in a week, in a library that just got released last year. Code, screenshots + body of the lesson in a README. Overly engineered project, but the two or three example I tried compiled and ran (yet somehow the automated cmake just hung, maybe a problem on my end)

I was already the king of doomers, now it has left me with even more nausea at this entire field and its future. Despite still needing an experienced dev to run the thing, companies operate on cost cutting, people operate on corner cutting and the result is inevitably mountains of code no one needs, no one has reviewed, that is more easily thrown away than fixed. The internet will be inundated by shit no one needs. Open source is dead.I hope it was all worth it. I don’t want to imagine what software will look like when the people that liked the art of creating software properly have all left, and only the people that never knew how to program, and never knew understood why more code always means more problems, run the show.

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