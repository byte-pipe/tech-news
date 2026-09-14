---
title: 'Ask HN: What are you working on? (September 2026) | Hacker News'
url: https://news.ycombinator.com/item?id=49686380
site_name: hnrss
content_file: hnrss-ask-hn-what-are-you-working-on-september-2026-hack
fetched_at: '2026-09-15T07:38:34.218811'
original_url: https://news.ycombinator.com/item?id=49686380
date: '2026-09-13'
description: 'Ask HN: What are you working on? (September 2026)'
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
Ask HN: What are you working on? (September 2026)
278 points
 by 
david927
 
22 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
857 comments
What are you working on? What have you been curious about lately?
 
help

jonahss
 
2 hours ago
 
 | 
next
 
[–]

I had claude faithfully rewrite SimTower so I could play it in the browser:

https://kvetch.io/conciliatowerI wanted to re-play SimTower but found it too difficult to get running through emulation. Instead, I worked for 6 months with Claude Code on a complete rewrite, replicating all the functionality from a Ghidra decompilation of the binary, an AI-generated summary of the original source code and my memory of the gameplay. Then deployed it to the web as WASM.
I wanted the original feel of the game, so didn't create new art. Instead, you load an original binary you provide, and the on-page code parses it and pulls out the original assets.I didn't look at a single line of code Claude wrote, but spent hours playing through the game and nitpicking every little behavior. A lot of time was spent convincing myself that the elevators just ARE that hard to get right >.<I hope everyone can enjoy this game again. Did a writeup here:https://www.wyldcard.io/blog/simtower-remake-playable-in-bro...source:https://github.com/Jonahss/concilia-tower

reply

nkapias
 
11 minutes ago
 
 | 
parent
 | 
next
 
[–]

While looking for the game files I found this web player : 
https://www.abandonware-france.org/online/play/simtower/

Currently in maintenance tough

reply

daymanstep
 
38 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

How would you get different behavior when you have completely decompiled the original binary and recompiled it to wasm? Shouldn't the result have identical behavior?

reply

jesse__
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a voxel game engine called Bonsai for ~10 years.

Probably the most interesting thing about it at the moment is the editor. The world, and most things in it, are represented as collections of SDFs. More accurately, they're density fields, but, potato-tomato.Bonsai has undergone a large rewrite over the last couple years that's nearing completion. A world edit is defined as a bunch of SDF parameters which get projected/rasterized into the voxel grid by a shader on the GPU. One neat thing about SDFs is they've been thoroughly researched and documented by a guy named Inigo Quilez, and they have a lot of nice mathematical properties. For example, you can do a smooth union of arbitrary SDFs to get nice rounded contours where shapes join.I've written every system from scratch, all the way from the memory allocators and font rasterizer to the collision detector and simulation loop. I even wrote a metaprogramming language as a replacement for C++ templates, which is a whole other story. IIRC the only external dependency is the C runtime library for starting the process and my very occasional use of variadic functions arguments.For a long time, an explicit non-goal of the project was to ship a game. It sounded insane to me to write an entire 3D engine and then ship a game. As it turns out, I've gotten it to the point where I can actually make a game. I've got a start on the game systems in a closed-source repo, and hope to have a steam page for it by the end of the year.I'll do some shameless self-promotion and leave some links here for anyone interested in looking at the engine, language code, or some pretty pictures.https://github.com/scallyw4g/bonsaihttps://github.com/scallyw4g/poof

reply

epiccoleman
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Definitely interested in where you take things with the actual game - the engine looks really cool. It seems like we're in the midst of a bit of a cambrian explosion around "survival games descended from Minecraft" (Hytale is top of mind, but there's also Vintage Story and iirc there's a few others of note either in early access or development). Not that a voxel engine can only do a Minecraft-like - but there's definitely a market for someone who wants to take that formula and run with it.

reply

jesse__
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah, it seems enough people have done enough work on voxel engines now that we're actually starting to see games proliferate. I'm stoked about it!

I'm a lot less interested in minecraft-style survival games than I am in exploring .. other .. types of games that push the medium further. Most voxel games that make it to release basically boil down to 'hack-n-slash RPG with a lego world'. As you mentioned, it's obviously a successful recipe, but I feel like it's barely scratching the surface in terms of how far the underlying tech has come.I've got a game in-flight where the primary mechanic is modifying the environment to achieve a goal. Teardown is really the only other game that's made it to market and done this. The mechanics are going to be intentionally simplistic .. it's more of an existence proof that a deeper game could exist and people are interested in it.

reply

jesse__
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Wow, thanks for all the kind words folks! I really appreciate it <3

reply

freakynit
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Holy moly!!!! Bonsai is freaking crazy!! That scale and view-distance..wow!! Brilliant work..

reply

iugtmkbdfil834
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I.. want to join to chorus of praise here. Nice work man!

reply

montenegrohugo
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

pretty damn cool. SDFs are the best. I've been playing around with an idea around this on the weekends.

Such a cool primitive!

reply

erwincoumans
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Very cool. Are you familiar with the game Voxile? Its author also created custome languages, and the game uses Lobster.

reply

jesse__
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm tangentially familiar .. I played the demo a couple times over the last few years when they did major releases. It's impressive to say the least.

reply

derpyzza
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

omg you're the poof guy!! i really like trying to shove metaprogramming systems into C and poof is one of the best i've ever encountered!! it's so damn good!

good luck with the game btw, is there anywhere i can follow development?

reply

jesse__
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Wow, high praise! Thanks :D I'm slightly biased, but I tend to agree with you; it's actually the best metaprogramming language I've ever used. JAI is probably better, but I haven't sat down and done a real project with it yet.

As far as following development on the game .. I'll probably start doing marketing when I've got enough for a trailer. I'll announce updates on Discord and Youtube, if you'd like to follow along therehttps://discord.com/invite/kmRpgXBh75https://www.youtube.com/@scallyw4g

reply

joystick_0x0
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Just amazing.

reply

Boss0565
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

this looks amazing

reply

shoobiedoo
 
18 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Wow, unbelievably cool. Good luck with the new game using the engine

reply

Jemaclus
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a real-life social app called Holler (
https://justhollerapp.com
).

I'm an introvert and socially anxious, but I do enjoy hanging out with my friends. I just HATE the invitation-and-coordination game. If someone invites me and I don't want to go, I hate having to come up with a socially acceptable excuse. Inviting someone and waiting for them to make a socially acceptable excuse is equally awful to me.Then you get to coordination. I want to go to the brewery at 2pm, but your kid has soccer practice so you can't get there til 3:30, but then Joe has to leave at 4 to pick up his mother in law at the airport, and... ugh. It's the worst.So I made Holler, which is basically you hollering to your friends, "I'm going to be at the farmer's market at 2pm," and then you just go. If they show up, fantastic. If not, whatever, you were going to go anyway.No coordination, no invitations, no friction. Just holler and go.It's iOS only for now, but I'm working on an Android app as you read this, so hopefully that's coming soon.

reply

MrDresden
 
21 minutes ago
 
 | 
parent
 | 
next
 
[–]

This kind of reminds me of Foursquare from back in the day.

Now a days I just have a few group chats where I can drop this kind of announcement in and see if there are any takers.

reply

epiccoleman
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That seems like the kind of "social app" that might actually 
work
 for me. I like the idea of sort of passively declaring "i am doing something, feel free to show up."

I guess the potential failure mode is ... no one ever showing up. I've got a standing slot (during work hours) at my current company where it's just "AI Jam" - just come in, eat lunch, and we'll hack on something, ramble about the news, etc. It's been moderately successful but there are definitely weeks where you just end up in a call with one or two guys with nothing to show.That's not so bad though - last week we just talked about video games. Still fun.So anyway - best of luck. Seems like a cool idea!

reply

Jemaclus
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah, I get that. My thinking is that I'd rather go do something fun by myself than sit at home because I couldn't coordinate something or because someone else didn't want to do my thing.

This weekend, for example, another couple invited my partner and me to go do an activity. They sent the text at 11. We finished giving our kid lunch, walked the dog, and loaded up the car. They texted and said their kid wasn't ready yet, and maybe they'd leave by 2. They didn't leave home til 2:30, so we didn't start our activity until noon, almost three hours later. The activity lasted about an hour, then we suggested going to a brewery to get some drinks, but for one reason or another, we wound up going our separate ways.My partner looked at me and said "This would've been a better Holler use-case. We could've just gone for a hike ourselves and not had to coordinate with someone else who can't show up on time."Sure, it might've just been us, but we spent a lot of weeping and gnashing of teeth coordinating with people that we ultimately barely spent any time with, and instead lost half our day.Holler, to me, represents a form of social freedom. I'm freed from the constraints of other peoples' calendars. If they really want to hang out with me, they'll come to the events I holler. If they don't, then that's fine, we can still be friends, but if they can't be willing to attend things on my schedule, why should I adjust my schedule to conform with theirs?So I'm going to do what I want to do, and if anyone wants to join, fantastic.Better than sitting at home twiddling my thumbs wishing I was doing something fun.

reply

lenova
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'd be interesting it an Android app version (or heck, even a web UI or progressive web app!).

reply

Hex08
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Like the idea and the website looks good! Did you design by hand or what was your workflow for coming up with a design language, color palette, the sliding banner with headlines, etc?

reply

Jemaclus
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! I came up with the color palette and the overall design. To be totally honest, I had AI do the HTML/CSS, as frontend is not my specialty, but I drew up the main design in Canva first and spent a lot of time with Claude to get it to reproduce what I wanted. It came up with a few things that I liked, and it came up with a few things that I hated. The final product out of Claude was probably 95% of what you see here, and then I went in and tweaked the rest of it by hand.

Glad you like it. :)

reply

Zak
 
12 minutes ago
 
 | 
prev
 | 
next
 
[–]

Nucleus programming language: 
https://github.com/zakwilson/nucleus/

It's still pretty early, possibly buggy, and almost certain to get breaking changes without warning.My original thought was to combine Lisp syntax and structural macros with C semantics and see how much extra abstraction that would provide, but variants of that idea have been tried before. They may have been compelling at a certain point in time, but I think a new systems programming language in 2026 should offer more, so it does.Some features include: strong typing, protocols (similar to Clojure or Rust traits), non-nullable references, error values, bound error handlers (a bit like Common Lisp), optional lexical lifetimes, namespaces, and no mandatory runtime overhead relative to C.It's self-hosted, which I've noticed several new systems programming languages announced recently are not.

reply

VincentBrand
 
9 minutes ago
 
 | 
parent
 | 
next
 
[–]

cool project

reply

sorbalda
 
11 minutes ago
 
 | 
prev
 | 
next
 
[–]

I am working on a cyberpunk multiplayer, shared, persistent world which runs completely in a terminal, and you can access just by typing "vibeworld" in the terminal.
You can create your avatar, it is full of cyberpunk cities and you can also go to the moon. In the moon there is a place where you can see the stars and everything happening on the virtual pixelated sky, water a plant (if nobody put water it dies), with a soft low quality chill music. If someone is in a room with you, you can see him and you can chat, even vocal chat exists.

https://github.com/SorBalda/vibeworld

reply

jamesyun
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building Orate, a free public speaking app:

• Users are given a prompt and have 2 minutes to answer.• Speeches are reviewed by AI and other users.Speaking eloquently "off the dome" is an incredibly useful skill, improving all your interactions with other people. And like a muscle, you can train it with dedicated practice until it becomes effortless.It has been very fulfilling to listen to other people's speeches, knowing that we're helping each other pursue our shared goal of becoming excellent communicators.If you're looking to improve your public speaking, I recommend you give it a try!https://apps.apple.com/il/app/orate-practice-speaking/id6761...

reply

OtherShrezzing
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Cool concept. Small feedback on the first user experience flow.

I downloaded the app to listen and write constructive notes for people, but I can’t enter the app until I’ve given microphone access and recorded a 30s clip. I’m on the bus, and can’t provide that audio now, and I’ll almost certainly forget about the app before I get 30 free seconds this evening. I think you’ll drop a lot of first time users here.

reply

andy_ppp
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You could “Pokémon Go” this and allow people to find performances they find interesting on a random street corner anywhere! Great idea!

reply

mohamedkoubaa
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Plans for android?

reply

SebRollen
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building 
https://uscodex.org
. In a nutshell, the goal is to collect all US federal law in version control, and cross-link any references between different sections. Currently I have the US Code, CFR, ~30 years of public laws and congressional bills and 25 years of executive orders.

Actually using raw git repos as the main data store which has worked out great since the US Code changes very little between new releases and so it compresses very well. Also makes it easy to generate diffs of sections:https://uscodex.org/usc/d/119-100/119-102not101/16/2201

reply

epiccoleman
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Hoo boy. It's an awesome idea, don't get me wrong - and it's work that should 
definitely
 be done. But I've worked professionally in this space and it is 
wildly
 complicated. I've never seen how things are done on the federal side, but US states have various modes of "electronic filing" for rules and codes - and there's a ton of complexity.

It's the kind of thing that sounds insanely boring on the surface, but there's a lot of interesting problems to solve, lots of coordination between various parties, lots of "deep state"[0] politicking - and so it becomes a surprisingly cool area to learn about and work in, and really matters in a way that many software projects do not.Best of luck - it's a cool problem space.[0]: I use "deep state" here somewhat ironically, but also just in the literal definitional sense: "people who are not elected but who work for the government and are surprisingly important". 0% intent to use it in the often insulting manner of popular discourse.

reply

SebRollen
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! Super interested in hearing more about some of the battle-scars you've acquired from working in the space if you're open to sharing? Very early in the journey here, so still have a ton to learn!

So far, it seems like the federal space is relatively well-behaved compared to your experience with states. Most agencies standardized on the USLM schema[^1][^2] in 2013. Before that, it's a hodge-podge of XML and plain-text sources.Also, FWIW, my interactions with federal agencies so far have been insanely positive. When I reported the error I found in the US code at 9pm, a staffer from the OLRC verified the issue and got back to me by 7am the next day, more efficient than most private sector organization's I've interacted with![^1]:https://github.com/usgpo/uslm.[^2]: Meta: The USLM itself was created by federal lawhttps://uscodex.org/usc/2/181

reply

epiccoleman
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I am not sure how much I'm allowed to say publicly between NDAs and contracts and all that fun stuff (I may already be over the line, tbh) - but feel free to drop me an email at the address in my profile and I can point you to a few things that might be of interest.

reply

andriy_koval
 
53 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

project is cool, but what you will do with it? Do you have audience, marketing strategy, monetization plans, etc?..

reply

hdb2
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

this seems like an outstanding idea!

reply

SebRollen
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Aw, thanks! I thunk it myself :)

The cross-referencing between different corpora has actually been very helpful. I was able to find a typo in the notes to a US Code section through it and submitted it to the OLRC. They fixed it, so now I will forever be bragging about having fixed an error in the US Code haha

reply

cookienaut
 
15 minutes ago
 
 | 
prev
 | 
next
 
[–]

Building throwdown.top: a free web app for making leaderboards for club crossfit competitions. The main goal was to build a tool for a friend who owns a crossfit box. The app is kinda simple (a few forms and tables) and not overloaded with features, but I was trying my best to make the UX comfortable, because I was the first user, and my friend - the second one :) It is battle-tested at real club events, so the early kinks have already been worked out, but feedback is always welcome!

https://throwdown.top

reply

aleqs
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a general repository linter. The idea is to declaratively define a set of rules/conventions for your repo, (for things that language-specific linters don't cover), covering things from directory structure, required files, file staleness/freshness, file size, rules for binary files, rules around use of invisible Unicode, etc. - which can be checked deterministically. Many/most large repos have a set of hand-authored scripts for doing these kinds of checks, the tool I'm building basically packages these in a fast, reusable and extensible tool, with some niceties added.

https://alint.org/https://alint.org/blog/why-alint/

reply

jjordan
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

It would be great if I could integrate this into our existing (and rather extensive) eslint config as as a plugin of some sort rather than integrate yet another new tool to our dev environment. Any plans for that?

reply

variodot
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://shopspec.io/

ShopSpec is a deterministic parametric furniture generator (bookshelves, cabinets, shop carts, leg-and-rail frames, multi-carcass composites) that encodes real woodworking intelligence and outputs shop-ready artifacts.Most recently, introduced the concept of value engineering by sweeping across dimensions to batch evaluate candidates that ranks based on sheet purchases. Also have in beta an MCP connector to let agents explore the deterministic engine.I'm building a number of items for home and shop and ShopSpec has been instrumental to plan, visualize, and execute on these new ideas/projects.

reply

Mumps
 
33 minutes ago
 
 | 
parent
 | 
next
 
[–]

This is beautiful and I'm now itching to make a workbench (finally! that initial "how many sheets and what for what size" problem has been the mental blocker)

+1.0mm vote to adding metric please!

reply

rhythmic_mp3
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Is this related at all to sawdust.diy which was posted last What are you working on? 
https://news.ycombinator.com/item?id=49234277
. Has a really similar look and feel but different feature set

reply

mpolichette
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is amazing, I may use it for a built-in pantry i'm planning to build.

In my use case, I end up with one side at an angle, is there a way to support that?

reply

mimo84
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Wow that's really cool! I'm actually trying to learn about woodworking and using those example as a base are really great! 
You could consider having an option for metric users as well!

reply

starvar2
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

+1 for metric. This looks really cool, indeed.

reply

cfontes
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Awesome, is there a way to use metric system on it?

reply

variodot
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It is not currently implemented but planned for the future based on all of the feedback here.

reply

thesurlydev
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Nicely done! I'm a fan

reply

wateralien
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Really great work.

reply

stefap2
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

projects per year in "Ask HN: What are you working on?"

year projects avg/month
 ---- -------- ---------
 2008 123 10.2
 2009 104 8.7
 2010 666 55.5
 2011 86 7.2
 2012 46 3.8
 2013 389 32.4
 2014 146 12.2
 2015 104 8.7
 2016 471 39.2
 2017 456 38.0
 2018 242 20.2
 2019 246 20.5
 2020 882 73.5
 2021 837 69.8
 2022 363 30.2
 2023 425 35.4
 2024 2122 176.8
 2025 6220 518.3
 2026 6093 677.0 (Jan-Sep)Top five topics per year (% of that year's projects, keyword-classified):year #1 #2 #3 #4 #5
 ---- ------------- ------------- ------------- ------------- -------------
 2008 Dev tools 9% Games 9% Video/gfx 7% Writing 7% Business 6%
 2009 Dev tools 16% Science 11% Writing 8% Education 7% Business 7%
 2010 Dev tools 8% Games 6% Video/gfx 6% Business 4% Writing 4%
 2011 Dev tools 8% Games 8% Social 7% Business 7% Science 7%
 2012 Business 13% Dev tools 7% Hardware 4% Video/gfx 4% Social 4%
 2013 Dev tools 16% Video/gfx 10% Games 7% Writing 6% Education 6%
 2014 Dev tools 12% Video/gfx 10% Writing 7% Hardware 6% Games 6%
 2015 Games 11% Dev tools 10% Business 10% Hardware 8% Video/gfx 8%
 2016 Dev tools 17% Video/gfx 11% Hardware 8% Business 6% Music 5%
 2017 Dev tools 18% Video/gfx 10% Hardware 7% Games 6% Data 5%
 2018 Dev tools 14% Video/gfx 8% Writing 6% Games 5% AI/LLM 4%
 2019 Dev tools 17% Video/gfx 10% Games 9% Hardware 6% Business 5%
 2020 Dev tools 14% Video/gfx 9% Games 8% Hardware 5% Writing 5%
 2021 Dev tools 18% Video/gfx 10% Games 9% Hardware 7% Writing 6%
 2022 Dev tools 21% Video/gfx 13% Music 9% Science 8% Games 7%
 2023 Dev tools 14% Video/gfx 10% Games 9% Writing 8% AI/LLM 7%
 2024 Dev tools 20% AI/LLM 17% Video/gfx 11% Games 9% Business 6%
 2025 AI/LLM 27% Dev tools 21% Video/gfx 10% Games 9% Data 5%
 2026 AI/LLM 33% Dev tools 22% Video/gfx 10% Games 10% Hardware 6%

reply

brachkow
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

What's interesting (and kind of sad) here is that while AI drastically increased product count, more than 50% are now composed of dev tools and AI

Some kind of golden shovels situation. I wish there were more games, personal apps, and open hardware – more fun stuff that became affordable due to AI

reply

sp1nningaway
 
19 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But there ARE more games, personal apps and open hardware! Games went from 38 in 2023 to 609 so far this year. A golden age for taking whatever sounds fun and making it happen. Yes, 50% of HNers appear to think AI metaprogramming is fun/important, but I'm excited that I can faff about with making little games and music apps and whatever else I can dream.

reply

xpct
 
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

It's the same as before, dev tools ranking higher up. For better or worse, developers like to spend time on meta-development.

reply

david927
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Thanks for doing that!

For more context on these numbers: when I started posting these, first, I wasn't consistent, and second, I was doing something that, to the algorithm, looked suspicious, so I think the posts had a negative weight.In 2024, HN reached out and it got more of an official blessing for me to run these, and we set an official day of the month (the second Sunday), which in turn made me more consistent.

reply

comboy
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Awesome dataset. Things are changing. In Chinese-learning community I found that surprising amount of people are creating their own tools without any intent to publish them, it just became easier to create your own thing that to dig out the good stuff from tons of tools already available.

reply

scurnus
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It would be interesting to know if # daily users increased. 
Anyway there are so many projects, it is hard to decide what to projects read about, it is mostly already known figures who get the attention on their projects. 
Also we should force ourselves to give enough attention and time to projects we are interested in, without jumping to the next thing every 5 minutes.

reply

xpct
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Could we compare this to HN growth?

reply

fl4tul4
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

nowadays, with LLMs, everybody is calling themselves a developer doing any kind of project.
Welcome to the future!

reply

buster
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

As a developer myself i hear this so often. Yes, it's (probably) your job on the line as well, BUT everybody nowadays 
can
 be a developer.
Maybe, don't call it developer. Everybody nowadays can built some software that fulfills some need (or just for fun). It's actually something good, isn't it?

Would you mind, if you could suddenly, over night, be a carpenter, a watch maker or glassblower?

reply

keybored
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I care a lot more about my gainful employment compared to the everyman being able to create their own... something.[1] That’s very selfish of me, AI Industry, and I’m sorry.

> Would you mind, if you could suddenly, over night, be a carpenter, a watch maker or glassblower?Yes. If that came with the little-bitty stipulation of being tied to the “compute” property of these AI behemoths.Of course going beyond that it gets less problematic. Some carpenter-skilled exoskeleton is a lot less problematic than disembodied intelligences spamming our minds and each other.[1] What exactly? My mind is so saturated with AI tools being literally devtools. On top of devtools on top of devtools.Well we can finally get back to a semblance of the status quo ante Internetum with something like businesses being able to list all of their contact information on their own websites instead of “see our FB page”.

reply

sparkling
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Apart from the AI chain, who is benefiting from the explosion of vibecoded slop project?

I can think of domain registrars and entry-level VPS hosters (non-Hyperscaler)Who else? Asking from a investment perspective.

reply

guywithahat
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If you use open source projects with any regularity, I'm certain you rely on AI-generated code, from projects who's primary contributors are AI

reply

bluerooibos
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Holy shit.

reply

softwarewright
 
36 minutes ago
 
 | 
prev
 | 
next
 
[–]

I am working on developing a distributed operating system for managing machine learning resources (the entire memory hierarchy, networking and compute hierarchy). I worked in O/S development early in my career, now retired and ML is a hobby I've invested in over the past few years.

I'm curious about:- how to "upcycle" end-of-life NVIDIA GPUs, like K80, M40, P100, etc.- how to offload MoE expert calculations to MCUs with NPUs, possibly FPGAs- how to manage a 10G LAN-attached network of older Xeon servers with the above GPUs and USB-attached MCUs as a machine learning "fabric"- do ideas from IBM's ACP/TPF O/S (now Z/TPF) carry over?- do ideas from IBM's Workload Manager (business priorities managed resources) carry over?- can I bypass end-of-life CUDA driver support for older NVIDIA hardware by using Rust/Vulcan?- can I leverage the architecture of Freetoken (MoE caching/routing, Engram, KV-cache compression) and other approaches like Baby Dragon Hatchlings, Hierarchical Reasoning Models, Tiny Recursive Models, Recurisve Language Models, Multi-token predicion, etc?- is anyone else intersted in actually building something like this?I've explored many of these parts individually, now combining them...

reply

jerkstate
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

https://curvefit.app

it's a weight-training app that helps you train along your "pareto frontier" of weight vs reps. The idea is to train at lower weight-higher rep, medium weight medium reps, and higher weight, lower reps for every movement. I tried to develop my own weight training program following bits and pieces of advice from bodybuilding forums and ended up injuring several tendons in my first year. So I did a bunch of research on tendon strengthening as well as what's most effective for hypertrophy (reps near failure) strength (reps near maximal load) and injury-prevention/frequency (not bringing yourself to failure too often) and designed an app to automatically prescribe and advance weights and reps based on your learned strength curve (Brzycki-like, with an added shape parameter)The app is designed to make use of the free Cloudflare tier, so I can support thousands of athletes for just the cost of the domain name. I'm primarily interested in understanding the "Fatigue curve" - right now I have some basic per-set fatigue modeling (basically a log-linear strength dropoff) but I think it could be much better characterized with more data. I could go on and on about the modeling but my intention is to keep it free (maybe add some non-intrusive ads on content pages if it ever starts costing me a few pennies a month) but my primary interest is to be able to do statistical analysis on the data.

reply

maerF0x0
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Ok, presuming this is going to be a monetized thing aiming to compete in the market. (if not what follows should be ignored).

What about your app is better than what already exists fromhttps://macrofactor.com/workouts/,https://rpstrength.com/pages/hypertrophy-app, and maybehttps://biolayne.com/workout-builder/?All 3 incorporate some form of RIR progression, varying rep ranges, program builders, and (at least in RP) some form of feedback mechanism to tell how impactful the last training stimulus was on recovery.Not trying to bash it, but to either 1.) help you think through your offer or 2) help you realize there's already a lot in the market.If you're really just doing this for you, and your interests then glhf :)

reply

jerkstate
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don't intend to monetize, I only want to compete for data. I think it's an interesting field and I'd like to be able to contribute back to the science by using the data gathered. I think these workout apps try to be opinionated about what an effective program is, but they try harder to make money, so they generally bend over backwards to accommodate whatever program the paying customer wants to do. Mine is more opinionated. I think this is the best way to lift weights for a wide range of athletes who are interested in getting stronger and bigger with the least amount of wasted effort and lowest chance of injury, the simplest way to record it, and the best way to get a statistically defensible understanding of how your strength is changing over time. If you want to do something different, as you mention, the space is crowded with apps.

reply

maerF0x0
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ok, so if I'm synthesizing your words correctly, other apps are "Bring your program, any program" and you're really leaning on "We'll tell you exactly what to do based on Pareto frontier modeling" ?

reply

esperent
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It looks interesting but as someone else noted, it needs more images and animations, way less walls of text.

There's a huge database of licensable animations that several apps I've seen use. E.g. take a look at the animations in Hevy. I forget the name of it now but you should be able to find it easily.

reply

jerkstate
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

yeah, point taken, I do need to rewrite the user-facing documentation to be more accessible (and less obviously LLM-assisted, heh - although I did review and edit all of it). Workout design (including teaching a user 
how to do
 an exercise) and logging are two legitimately different tasks in a workout app and I wanted to focus on being the best logger. Maybe this is paranoid but I felt that saying "here's how you do a workout" introduced a little more potential liability than punting to "if you don't know how to setup a workout and learn to do the movements, hire a personal trainer to help you figure out movements appropriate for your fitness level."

reply

Bishonen88
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Gave it a quick go as I'm looking to adopt some sort of fitness app. There's too much text/complexity for my taste.

The website could use some images/simplification to get going and then have more details and whatnot later on. It seems that you let the LLM generate the content itself (em dashes, emojis) - Personally I'd be skeptical of a fitness app that has most of its content LLM'izied.On step 3 of the tutorial, it's not clear that you can scroll down and there's more there on a mac 16''. I was confused what to do. It didn't allow me to change to metric system either (which I later found in the user-settings). You can't 'esc' from the tutorial popup either.

reply

jerkstate
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

yeah, it's a difficult balance to explain why this app doesn't work like every other weightlifting app and not inundate people with too much information. It actually is pretty simple once you start using it. I'll look at the tutorial scrolling issue, and eventually rewrite the content.

The tutorial can't be escaped because it requires a liability waiver checkbox at the end.

reply

Akranazon
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Interesting, this reminds me of my workout planning tool, which I've been working on.

https://grademyworkout.com/

reply

jerkstate
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is really awesome! I used to have an movement to tissue mapping in an earlier version of app but I opted to focus more on the weight-reps curve it because the tissue volume calculations added too much complexity to the interface, and it just encouraged me to do too many different movements. So exercise selection and tissue coverage is something I actually think about outside my app.

I had coefficients mapping each exercise to its tissue impact but it was kind of arbitrary and unscientific - even between athletes you will have different techniques on the same movement that will impact tissues differently. I do think that workout design is a super important area and I hope you crack it, it was too hard for me to do a good job on.

reply

teiferer
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> a bunch of research

What exactly is your "research"? Is it reading more bodybuilder forums (bro science) or is it physiological studies (actual science)?

reply

lemming
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Check here: 
https://curvefit.app/methodology

reply

jerkstate
 
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

physiological papers. My main interest is contributing to the research by developing a fatigue model. My hypothesis is that athlete recovery factors like accrued fatigue in-day and cross-day can be used to predict workout log outputs of total tonnage, combination of weight and rep count, and proximity to failure. Eventually I hope to be able to link these recovery factors directly to provide targeted advice about your overall program's effectiveness, deload planning, etc. in order to most efficiently achieve strength, endurance, and hypertrophy goals.

reply

codeatlass
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

hjh

reply

BrunoBernardino
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

My wife and I continue to work on a private, paid, ad-free and personally customizable search engine: Uruky [1].

To signup you don't provide any information (a randomly-generated account number is assigned to you), and you can run a proof-of-work captcha to get 2h for free. You can choose among many different search providers (for defaults and per query), including Uruky Site Search, powering our own index.Last month we reached 300 monthly active accounts and released an image search gallery mode, plus a simple calculator and conversion widget!The main differences between Uruky and Kagi, DuckDuckGo, SearXNG, etc. are visible in the footer (right side), but one huge difference is that with Uruky, after being a paying customer for 12 months, you get copy of the source code (licensed as BUSL, into AGPLv3 in 2 years — a suggestion made here on HN)!Our main challenge continues to be discoverability and outreach because we want to do it ethically (no Big Tech and no GenAI/LLMs). Ideas are welcome! We’ve been sponsoring open source projects, open source maintainers, and indie, small-web, and privacy-related websites and applications/groups/orgs. This month we're sponsoring NOYB [2]!Feature-wise, for September the most visible things that shipped already were Tags and Scopes (top feature requests for a while). We’re also still (slowly and sustainably) increasing our own index, focused on indie/small web.Thank you for reading this![NO-AI]: There is no generative AI product or service being offered, here.[1]:https://uruky.com[2]:https://noyb.eu

reply

chumzygood
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I run a small experiment on this: 29 paper-trading accounts on real US stock prices, $100k each, since July 27. Four AI models (ChatGPT, Claude, Grok, Gemini) each write a trading rulebook and rewrite it every day from their own results. One account is a fixed rulebook that no AI ever touches, as a control.

Result so far (paper, 34 trading days): the no-AI control is +13.0%, the S&P 500 is +3.4%, and 25 of the 28 AI accounts are below the control. The best single account is a Grok-written "patience" book at +40%, which I treat as one lucky account in a choppy market, not a finding. At the trade level the AIs and the control look the same: 3,212 closed positions, median +0.06%, median hold about 2 hours. They trade a lot and mostly go nowhere.Everything is public, including the losses and the retired strategies:https://aitradingcompetition.com/which-ai-is-winning.htmland the full trade file as CSV athttps://github.com/ckamelhar-collab/ai-trading-arena-data. Paper money only, not advice, nothing for sale on those pages.

reply

drgo
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Famously Norwegian cows “picking” stocks by shitting in marked grid did as well as professional stock brokers and much better than astrologers!

reply

hobo123
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Love this. Stay hungry, stay bullish. :D

reply

andoando
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

None of this really means anything. For one if you test enough strategies one by luck will be killer. Second, past performance != future.

One AI might consist of some convulated strategy of who knows what, but all it takes in the end is for it to say...hold more tech stocks than not, or buying more call options or leveraged positions in a bull market, being more out of the market during a bearish market, etc. But that same strategy will fail miserably as soon as the market conditions change

reply

altmanaltman
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

yeah the alternative test is to arm a toddler with an account and just have it randomly guess what to do. Even it might outperform the best fund managers over a given timeframe but that's just how the markets work. Over the long run, the toddler will go bankrupt.

reply

semiquaver
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Don’t let AI write for you. Everyone can tell.

reply

jbs789
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

“Not a finding” lol

reply

wewewedxfgdf
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

The most likely outcome from a naive attempt to automate trading is random results.

reply

KellyCriterion
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Wrong:

Stock prices are not random(in a sense of "really random every day")

reply

bhairoxx
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Why didn't you let the bots backtest and forward test to pick the mix of best strategies/indicators?

reply

mcapodici
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The problem is the bots may have some of the backtest data already in their training.

reply

fahrvrgnugen
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Why would that matter? It's either a good strategy or it isn't.

Personally I think hobbyists that think they can second guess institutional finance are just fooling themselves.

reply

mcapodici
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ok for example my strategy is buy Moderna. That's it. Backtest that over the last year.

Agreed on 2nd point. Especially with no real hypothesis i.e. just throw AI at it.

reply

KellyCriterion
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If you have been trying to buy MRNA in the last 12-18 month, you are an idiot:

The stock price clearly fell for a very long time; only teethgrindlingy I would see one or two entries for "lets-try-it-fingers-crossing"; the price went better in the last couple of month, though no really strong long-entry signal, maybe 2 in the last few month.This is what I see in TradingView - for this,you shouldnt apply AI.

reply

fahrvrgnugen
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Timing is the strategy though. Buying Moderna is either a good idea or a bad idea depending on when you do it.

reply

hackernud3s
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm curious what signals they're trading on. SEC filings? Candlestick voodoo numerology?

reply

fl4tul4
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You have $2.9M just for this? Wow.

reply

testaccount121
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

paper trading means that no money is used

reply

NetOpWibby
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you, never heard the term before.

reply

duck
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

They mentioned paper trading which means it isn't using actual money.

reply

Chris2048
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> nothing for sale on those pages

"$20/month · or $160/year"--https://aitradingcompetition.com/playbook.html#pricing

reply

xyst
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> paper-trading

come back when you put it real money and have some skin in the game.

reply

chumzygood
 
58 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There is one. A real Alpaca account has mirrored one of the bots since August, capped at $3,000, with every fill posted: 
https://aitradingcompetition.com/real.html
. It's small on purpose.

reply

Cthulhu_
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I wouldn't trust AI with real money though. (I barely trust myself with it lmao)

reply

xwes
 
27 minutes ago
 
 | 
prev
 | 
next
 
[–]

I've had it with my Chromecast and Apple TV, so I made 
https://github.com/onewolfmoon/abeam
. It's open source, runs on Apple platforms, and does two things:

1. Play a YouTube video on a TV-connected Mac2. Mirror a Mac or iPhone screen on a TV-connected MacThe senders need macOS 26 or iOS 27. The TV-connected Mac can be running macOS 13 and up, so it's a nice use for an older laptop.The apps are in app review now.

reply

murdockq
 
54 minutes ago
 
 | 
prev
 | 
next
 
[–]

I've have jumped back into maintaining and cleaning up OpenPaint, a project I originally started about 17 years ago to bring a simple MS Paint-like editor to Mac, Linux, and Windows. It never really got much traction over the years and there have been several faithful other projects that tried to achieve similar goals and ported to the web.

For 2.0 I'm trying to stay faithful to what made the original Paint but with a few quality of life improvements, like multiple tabs with image previews, cross platform support, and generally cleaning up a very old codebase that relies heavly on wxWidgets.I've been using AI quite a bit to help maintain and modernize this 2.0 version but I want OpenPaint to remain a simple image editor that most people are familar with.Still a work in progress, but it's been fun bringing a 17-year-old project back to life and keep the idea going.https://github.com/murdockq/OpenPaint/tree/devhttps://murdockq.github.io/OpenPaint/

reply

chartrow
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

https://chartrow.com/
 is a website to visualize stock market data.

Examples:this table shows the outperformance of QQQ in recent years:https://chartrow.com/visuals/periodic-table#window=10This page shows stocks that are cheap relative to their own multiples in the past 10 years:https://chartrow.com/visuals/valuation-dip?view=chartsThis is a stock screener that shows histograms:https://chartrow.com/screenerThis page shows stocks with high "shareholder yield" (dividend yield + buyback yield):https://chartrow.com/lists/shareholder-yield-stocks

reply

ypcx
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

amazing.

reply

savgore
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://common.charity

I’m building the UK’s ‘big data’ charity with some awesome co-trustees and volunteers. We undertake big data projects in service of human flourishing, collect and synthesize datasets from hostile actors or freedom of information requests, and collaborate with other charities to build useful things that facilitate effective coordination.The context is that I co-run the UK’s largest and most active landlord review platform ‘Marks out of Tenancy’, and the data we aggregated and ended up being able to host and query did a number of incredibly high impact things:- our system for identifying how many people lived in a property started getting used to find victims of human trafficking
- our system for checking for HMO licensing got picked up by councils to detect 100% of illegal or rogue landlords in the scan area, as well as detecting illegal short lets.
- our longitudinal data collection on housing conflict between tenants and landlords directly led to increasing the rent repayment order threshold in the renters rights act from 12 months to 24 months.So after seeing how much data is out there ready to be used for advocacy - but just left untapped by a profit driven sector, and after years of experience as ‘activist data practitioners’ or whatever you’d want to call it, we decided to launch something that could be a home for those projects in the spaces we’re in over here in the UK.We’ve already got some awesome projects underway and we’re excited to see how year 0 goes for us!

reply

efromvt
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Love seeing data collection and aggregation used for good!

reply

mirekrusin
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

https://mirekrusin.com/cave

Palantir like system – data, ontology, logic, actions, security, operational workflows – packaged as single cli, local first, git friendly text .cave files and sqlite3 instead of k8s-style complexity blowup.Working on the weekends.Next is probably extension of the language to integrate something likehttps://github.com/mirek/astfor arbitrary ast traversals/modification/generation/better integration with external world - other file types, but ast concept goes further than that, ie. filesystem is also ast, traversal is ast/xpath like walk.Public domain on all my recent work.

reply

smccabe0
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

`--as-of` might be the most important feature in your codebase. Temporality of relationships is way way more important than I thought when I first started down the path of modeling relational data in agentic systems. Sometimes knowing why or why not at a glance can be the difference between spending another $50 on tokens retreading old ground. This is very cool, and I will probably discard my handrolled version in favor of your much more robust solution.

Have you considered allowing annotation of why something changed as part of a tx?

reply

aerodexis
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Interesting project. I've been thinking about the need for something similar at work when a coworker thought it was a good idea to explode our design documents by having an AI slop out tens of pages of additional design w/ zero consideration of modeling of the human-derived ground-truth or knowledge ontology.

A humble suggestion is to consider having this become an annotation layer on top of existing code or documentation.

reply

tonyoconnell
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's a beautiful language

reply

mirekrusin
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you, it was inspired by caveman skill hence the name :) It's like formalized caveman. I think there is still some work to make it better/more intuitive/easier.

reply

trentnix
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I have a MiSTer FPGA connected to a Sony CRT and installed the MiSTerFin project, which is a Jellyfin client for MiSTer. It's got a lot of things that need fixing, so I contributed a few PRs to fix some of the problems I encountered.

MiSTerFin is written in C and I'm much savvier with Go these days, so I (and my helpful Codex prompt) forked it and ported it to Go (where appropriate). I've since been obsessed, making improvements, smoothing out rought edges, and adding features, all get a great Jellyfin player on my CRT.And I have to say, watching Robotech episodes on my 4:3 CRT from Jellyfin is a shot of nostalgia directly into my veins.I'll add a bit more polish and get it published this week for others that might be interested.

reply

dzink
 
56 minutes ago
 
 | 
prev
 | 
next
 
[–]

Preparing 
https://www.dreamlist.com
 for the holidays. It's a private wish list and registry site that enables you to also group lists of friends and family into one page to share with grandparents or social media. So you can run family holiday giving + gift drives / toy drives / disaster recovery with no ads or spam or any other badness.

When I first launched it was the only wish list that didn't list your name and registry on search engines. It is has grown a lot since then, and added a lot more privacy features, and the best marketing has always been doing right by users (extremely rare these days). You can see by looking up any name + the name of a wishlist/registry site and see what shows up to check at any time.I'm working on more products following the same rule - serve users as you would your own family.

reply

stelabouras
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Noraneko - 
https://noraneko.cat

Lots of strays where I live, so I wanted an app to photograph and identify street cats and help get them adopted. Written mostly with Claude.The recognition runs on device: Apple Vision detects the cat, DINOv2-Small decides whether it's one already in your library, SigLIP2 names the coat.No accounts and no backend. There's a trading mechanic on top where you can trade cards via Wi-Fi (with Bluetooth as a fallback) and levels for both the user and each cat.You can also turn any cat into a shareable adoption poster.TestFlight is open, so feel free to try it.

reply

efromvt
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Love the ID/adoption - what's the gamification angle here? What does trading the cards mean in this context and how do you expect people to use that?

reply

stelabouras
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I took inspiration from Pokémon Go, Monster Hunter Now, and even Fatal Frame (lol).

For example: You need five distinct photos of a cat before the app will guess its age, which is also just what the model needs, since age settles at about five samples. You get XP for finding new cats, and also for shooting from a distance: the score rises with how far back you stood, so using the 3× is the legitimate way to earn it and walking up to the animal isn't.Card designs unlock per cat, as your relationship with it deepens and there are five card designs across five cat levels.Trading exchanges cards, not cats as the animals never leave your collection. Because a card carries the fingerprint of the photo on it, it doubles as a treasure map: find that cat in the wild yourself and the app tells you it's the one from the person you traded with.Didn't want to overcomplicate it (it's a side-project), so there's no server and no global fingerprint registry which means no race to find a cat first. It's built around building a relationship with the cats, and hopefully finding them a forever home.

reply

bouk
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I built 
https://kadaster.club
, which shows all land parcel data of the Netherlands. There's some existing sites for this but they quickly try to upsell you stuff and/or are slow and don't show the parcel data when zoomed out too much. None of the other ones I've seen render the parcel data as vectors either, which hurts my eyes.

I also just addedhttps://kadaster.club/mcpso an agent can query the same data and even look in the data available onhttps://omgevingswet.overheid.nl/to answer question around what is allowed and what permits you need for a specific location

reply

asymmetric
 
26 minutes ago
 
 | 
parent
 | 
next
 
[–]

Interesting, what’s the use case for this?

reply

VincentBrand
 
15 minutes ago
 
 | 
prev
 | 
next
 
[–]

I been diving into Neurosymbolic for the past 8 months, been working on a database that combines the best probalistic and deterministic reasoning into a single source of truth for AI agents and larger systems. 
http://www.oxid-db.com

Working out some details before dropping it opensource.

reply

junaid_97
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm buildingan open-source way to fill U.S. immigration forms without fighting clunky PDFs

Github:https://github.com/athos2113/fillvisa-osDemo:https://fillvisa.com/demo/US Immigration still relies on outdated XFA PDFs - you can't fill them on your browser. Most immigrants end up printing the form and fill it manually.So, I converted the PDF forms into smart web forms. They are replica of the official USCIS forms and follow conditonal logic. In the output, you get the official USCIS pdf form filled.

reply

yboris
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

I was stuck unable to fill out a PDF 
I-864
 for immigration because the required fields were non-editable. And opening the PDF in a PDF editor or Photoshop would require a password that was not available. So I had to create a PDF-to-JPG-to-PDF pipeline:

https://github.com/whyboris/PDF-to-JPG-to-PDF

reply

junaid_97
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Interesting approach.

How would turning the PDF into JPG allow you to edit/write inside?

reply

yboris
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Resort to Photoshop / editor at that point. I still prefer that over printing, writing, and then scanning.

reply

kittensmittens
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I hope this becomes obsolete by no longer being necessary

reply

junaid_97
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

USCIS is working towards turning it's forms into web-forms. Some forms are available to file online : 
https://www.uscis.gov/file-online/forms-available-to-file-on...

But, I'm guess it'll take some time

reply

mvanzoest
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Interesting. I downloaded some PDFs for the adjustment of status forms recently and most of them were editable but only partially - the conditional fields couldn't be edited it seemed.

reply

junaid_97
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yup. Those fields are dynamic, encoded in XFA -> JS. 
But, you can only access them via Adobe

reply

schainks
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Apple preview and the add text button got me through all the USCIS forms. You can use AI computer control to do this stuff now, right?

reply

Shank
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> You can use AI computer control to do this stuff now, right?

Speaking as someone who had to do a lot of immigration work to move to Japan, I can think of no work I would want to have a close eye on than immigration paperwork. One error is all it takes for a clerical rejection or similar. I had a professional lawyer working on mine and still cross checked every detail, and found errors!

reply

Cider9986
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That's cool. How are you gonna get it in the hands of people that would need it?

reply

junaid_97
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks!

Primarily by sharing the web version (fillvisa.com) on subreddit and FB groups. People complain about the USCIS PDF regurlarly, so, I just pitch them the website

reply

ahallan
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

http://schoolholidays.deals/

A UK-based flight deals service aimed specifically at parents who can only travel during term-time.Having this issue myself now with two children whereby flight prices double going into school holiday season, I have always wanted some kind of service which alerts me of good deals.I still have a long way to refining the actual product, but trying to fit the development around work commitments. AI helps obviously, and does 90% of the coding.

reply

sensecall
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

This is a great idea.

I'd love some way to have multiple schools (which may not have exactly aligned term dates).Also - and I'm sure you've considered it - but maybe something which allows for a day or 2 at the start or end of the holiday. I've found this drastically affects prices.

reply

ahallan
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Hi, thanks for the feedback.

Yes considering / implemented both of those, but will likely put it behind a paid service (need to pay for it somehow).

reply

haaz
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Brilliant brilliant idea

reply

23fdsf
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It is but isn't it bizarre that this is what was sold to us re. 'Agents'?

Yet here we are.This 'agents' paradigm is foolish and what that poster is doing is closer to reality. Good work.

reply

purple-leafy
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I have ALOT of free time since quitting my job.

0) money-money-money: A sub 15Kb server-less opinionated household budgeting tool [0]. Why? Its made to be extremely compressible, so you can edit your household budget and share back and forth with your partner via short-links or QR codes. The idea is you edit your budget, send the link to other party, they can view or edit and send back to you without a server in the loop. [0]1) slices: An alternative AI-first ADHD-friendly architecture experiment where everything you code is a "slice" with a shared event pool. A slice is a fully self contained "feature". Slices can only communicate with other slices through a shared event pool. Inspired by small-talk, vertical-slice architecture, and ADHD. I used slices to build a self-modifying IDE too. [1] [2]2) text compression experiments: I'm experimenting with approaches to compress text in pursuit of the Hutter prize. The idea is to take the entirety of the English Wikipedia, and compress the text as small as possible whilst still being able to reproduce it. [3]3) tiniest maze solving neural network: A write-up work in progress on a maze solver I built with heavy LLM help, managed to get a 14 byte neural network solving 96% of unseen mazes. [4] [5][0] -https://con-dog.github.io/money-money-money[1] -https://github.com/con-dog/slices-demo[2] -https://con-dog.github.io/slices-demo/[3] -http://prize.hutter1.net[4] -https://github.com/con-dog/tiny-neural-network[5] -https://minimio.ai/

reply

erwincoumans
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Very cool projects, and amazing a 14 byte nn can do it. Would be fun to analyze its approach, converting it to a Code-as-Policy.

reply

purple-leafy
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you! Yes the maze solver has been a very fun experiment with LLMs, and code as policy is a good idea. I’m racking my brain trying to find my next thing to experiment with, but usually the ideas come to me in waves

reply

dr_dshiv
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on translating the Renaissance — it was mostly written in Latin and 90% of it has never been translated to English. Even big names, like Ficino, Durer, Kircher, Fludd and Drebbel. And that’s Latin— things much more sparse in other classical languages.

https://SourceLibrary.orgis a hub that now provides over 20,000 translations of classical texts in dozens of languages (Latin and Greek but also Chinese, Sanskrit, etc). We always provide the original image of the text next to the AI translation (so if you don’t trust it, you can do it again). For a sense of scale, SourceLibrary now hosts more words than English Wikipedia!You can freely connect to the public MCP for research; that way AI can read books and not hallucinate quotes. In Claude, it also retrieves images directly into the chat.This is a philanthropic project based at the non-profit “The Embassy of the Free Mind” in Amsterdam, a rare book library devoted to free thought and mysticism.https://embassyofthefreemind.comSourceLibrary is totally free and open source. If we can raise the money, we hope to translate 100k books before the end of the year.If you want to dive in, I’d suggest trying our research agent with a rabbithole topic of your choice:https://sourcelibrary.org/librarian/

reply

NishanStepak
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

I am curious about this. I have found that there are number of primary works that have not been translated into english and are in the public domain in their native language. Translations are copyrighted if they are recent. I have a very short list of items which are of interest to me. They are things like Sundiata Lion King of Mali not having a public domain translation in English that I can find easily or there not being a public domain translation of Dede Korkut in English. Many of the better translations are copyrighted and not free.

reply

dr_dshiv
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks. It looks like we have some but not all of the original works you are looking for: 
https://sourcelibrary.org/librarian/thread/6aa7656bfa07a553c...

I’ll try to track down the ones you are looking for tomorrow. Yes, we avoid copyrighted modern translations.

reply

ejs
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Trying to convince people to get kids outside for their eye health:

https://eyesoutside.org&Hardware for kids and parents to stay connected without screens:https://readychime.com

reply

baldvinmar
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Readychime is great and could see a market for this.

reply

spudlyo
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

https://fabulae.orbilii.com
 - A Latin language audiobook containing both volumes of A.D. Godley's "The Fables of Orbilius" which are entertaining intermediate Latin stories written at the turn of the 20th century for use in British schools.

The audio itself is in delivered with the restored classical Latin pronunciation and contains spoken nuances like vowel nasalization, elision, and prodelision. I used a wav2vec2 model to generate forced-alignment data, so you can easily follow along with the text as it's being read aloud. Each word in the text is richly enhanced with pedagogical details like: lemma, citation forms / principal parts, morphological segmentation and analysis, inflectional class with complete declension/conjugation tables, verb category, contextual lexical information (i.e. specific L&S sense), Classical Latin IPA pronunciation, UD style syntactic function and relations, predicate valency, and concise English definitions. Spoken instances of elision and prodelision can also optionally be displayed.From a nerd perspective, one of the things that makes the system interesting is that the documents themselves are entirely in XML, and I use the soon-to-be-removed-everywhere in-browser XSLT feature to render the HTML, so you can see the underlying XML structure if you view source. Each sentence in the text contains provenance records so you can see the language model and parameters that performed each language enrichment task. The site UI is largely bilingual, and you can view it in either Latin or English.

reply

eigenblake
 
18 hours ago
 
 | 
parent
 | 
next
 
[–]

Woah this is so interesting. Confirmed it myself, you actually implemented elision!!! I really like your idea of capturing provenance in-document as well. This is humans speech, right? If you can do forced alignment on Latin, it gets me wondering if one could use a wav2vec especially turned to convert IPA into speech somewhat deterministically to compensate for how there is not heaps of training data in Latin.

reply

spudlyo
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Haha, thank you for using multiple exclamation marks!!! I'm thrilled that someone is as excited as I am about this feature, it made all the time I spent manually correcting/marking all of Gemini's elision hallucinations worthwhile :)

The recordings were made by my friend and Latin tutor. I used an Italian wav2vec2 model fine-tuned on Latin[0], which works pretty well for Latin only content, but falls down with mixed English / Latin. I found that some of the slower, larger Meta models worked fine for this use case though.Some folks on the Latin language Discord said they got pretty good results using Kokoro TTS and X-Voice for creating synthetic Latin, as you suggested using IPA.[0]:https://huggingface.co/lsb/wav2vec2-base-it-latin

reply

ddahlen
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

This is very niche, only for people who do astrophotography or astronomers, mostly because of the required specialized file format.

I have slowly built out a set of tools for asteroid orbits and photometry (measuring how bright stars/asteroids are).It is very rough still (Desktop only), and it only supports the FITs file standard.https://www.astrometry.space/Basically it is a full professional grade telescope processing pipeline in your browser. It does 2 queries to some custom databases to identify known asteroids and stars, but all image processing and calculations are done in the browser. This means the backend is pretty tiny. That said it is running on an old box in my closet, so queries may take a while if it gets hammered.I built it since I have worked with quite a few astronomers over the past 4 years and I keep watching them do the same steps, purely built to make my friends lives easier. I wrote it all in rust and managed to compile it into wasm. With some help from fable as I am not a frontend guy at all, I built it into a small website.Some of the code is public, the orbital mechanics code I wrote while I worked at Caltech. Which is being used on SphereX, NEO Surveyor, and the Roman telescopes to identify known asteroids.https://github.com/dahlend/kete

reply

adl
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been working on Editora, a keyboard-driven text editor for programmers:

https://editora-project.dev/

It has LSP support, debugging, Git and GitHub integration, multiple cursors, customizable keymaps, and live previews for things like Markdown, PDFs, and diagrams (and lot's of bugs! too). It runs on macOS, Windows, and Linux, with no accounts or telemetry.It’s a hobby project I work on in my spare time, and it’s still very beta. No big announcement or anything, I just thought I’d share it here.If anyone tries it, I’d be interested to hear what you think.

reply

knowthankyew
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I have been trying to find underutilized government and free data sources that people can use to make better decisions. As a result, I made a proof of concept application to aid students in making decisions about college and career with realistic future budget forecasting.

https://github.com/knowthankyew/gradcastMost college search tools stop at tuition. GradCast connects actual degree-level earnings to real local rent, federal/state taxes, and student loan amortization to show your real monthly take-home.A proof-of-concept web application that helps students simulate their financial future after graduation — based on real college costs, program-level earnings data, local housing markets, and tax calculations. Built on the U.S. Department of Education's College Scorecard API and HUD Fair Market Rent data.

reply

yqiang
 
37 minutes ago
 
 | 
prev
 | 
next
 
[–]

I’m building FitBee, a fast, ad-free, no-nonsense calorie and macro tracker for iPhone, iPad, and Apple Watch. The app is built with Swift and SwiftUI, with a Python backend. 
https://fitbee.app

reply

dvt
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I did a show HN & it didn't get much traffic, but I've been working on 
https://moral.games/
. A kind of debate PvP game, where you try to convince an AI judge of a certain moral position given an ethical conundrum.

Was trying to combine AI with generative storytelling with a card game. It was a fun experiment. To play, you'll have to get a friend to queue up at the same time.

reply

hasoy
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

I tried to play it, but could not get in a match. Why not add like a lobby where multiple people that are queued up can battle eachother?

reply

prbs23
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on building open source control firmware that runs on the Masterbuilt Gravity series electronically controlled charcoal smokers.

https://gitlab.com/prbs23/freefall_800The smoker hardware itself is pretty good, but like most IoT devices, the firmware and app sucked. So I reverse engineered the whole control PCB, and have been rebuilding new open source firmware from scratch. All the basic functionality is working now with a fully local control web app. Plus an Andoid app, and Home Assistant integration.Currently working on interface refinements, and some more advanced control sequencing features.I wrote up all the reverse engineering details in a blog post here:https://www.prbs23.com/blog/posts/reverse-engineering-gravit...

reply

pid0x17
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

- Nand2Tetris part 1. It is a project-oriented course from the Hebrew University of Jerusalem (offered on Coursera) where you implement a whole 16-bit computer in a hardware simulator in a simplified HDL language, starting from a nand gate and ending with an ALU, RAM, CPU, program counter, and an assembler for the computer's assembly language. I only have two modules left before I finish part 1. In part 2 (which I did not start with yet), you implement a VM, OS, compiler and high-level language and more stuff.

- I am implementing my own MCP server in Go for Bitbucket. This is more of a learning project for me (I was curious about MCP servers), but I also didn't find any MCP servers that have a clean codebase. Many seem to be vibe-coded, and as I work at a company where security is really important, I thought I would implement my own. (Still a WIP:https://github.com/pid0x17/mcp-bitbucket). I haven't touched this project in a while, though, as I am focusing on Nand2Tetris.- I am reading the Rust Programming Language book, but I am still in the beginning (just finished Chapter 3 on the weekend).

reply

_kb
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Nand2Tetris is great. Definitely one of, if not the, most impactful bit of education I’ve ever done it terms of knowledge imparted.

reply

pid0x17
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I am absolutely loving it!

I was very intimidated at first because the concept sounds very difficult, but Prof. Schocken and Prof. Nisan are amazing at breaking down the concepts and abstractions and making something complex very easy to follow and understand.

reply

rishi_devan
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I did Nand2Tetris during the last Christmas holidays. I only finished the first part - I got it working on Verilog - so I basically have a emulated computer that can run programs in assembly language. Will need to do part 2 as well.

https://github.com/rishi93/nand2tetris

reply

pid0x17
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's a really cool idea!!

I was actually wondering: are we allowed to publish our work on GitHub? I already have a Github repo but I made it private and only show it to potential employers and individual people who are interested, because I am not very certain about the copyright rules of the HDL skeleton files, and whether we are allowed to publish our work, given Coursera's honor code.

reply

ElFitz
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/lightless-labs/pessimal
: I got bitten a few times too many by my headless VM running out of disk space, so I had Claude build a minimal OTel agent sending metrics to an OTel collector (Signoz for now), and an iOS / macOS app to query it at regular intervals.

Works nicely with my existing Signoz, costs nothing extra, but I’ve yet to test it against Honeycomb and Clickstack. Apps are in private TestFlight for now.https://github.com/Lightless-Labs/willikins: a tool to deterministically provision new projects’ git repository, secrets vault / config, build pipelines, etc, based on the project’s needs (cli tool, web service, mobile app,…).It’s getting tiring to wire all those by hand or with cobbled together script. And I don’t trust agents to give them read and write access to all the resources they’d need to do it. Very much in progress, but it already forced me to clean up some config. I guess it’s like a bad Ansible, for project set up?I’m also experimenting with a team / project / task-scoped blackboard (https://martinfowler.com/articles/exploring-gen-ai/an-accide...) tool for agents, to be used by multiple users’ agents (eg different devs working on different sides of the same fix or feature), and a self-hosted Q&A forum for agents intended to serve as an authoritative self-grooming source of truth on technical, domain, and business matters for a team or org’s agents.

reply

dumbfoundded
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I created an ai cross-stitch pattern generating tool: 
https://stitchwink.com/admin

If you try to use image generation directly, you don't get real patterns. StitchWink makes real patterns that you can also edit manually or through text/images with AI.

reply

woutr_be
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm still working on 
https://openaltfinder.com
; a place to help you discover open source alternatives. Got quite a lot of traction this month due to Google/Apple Maps renaming Lake Ontario.

But overall it's a struggle, the site is still in Google jail/sandbox, so it's not even seeing any Google impressions. So most traffic is due to being very active and posting wherever I can.

reply

everyday7732
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

I think it will be difficult to compete with alternativeto.net which has a longstanding community, and options like filtering based on operating system. What are you doing which differentiates you?

reply

rushil_b_patel
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Good one

reply

brachkow
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

My quirky wishlist app 
https://thingstohave.app
 is finally done and heading to public launch this or next week.

I already partially covered the last few months of app development in this topic. But actually, its development took way longer, as only this iteration started in 2024. So it is the end of a long milestone— this launch date initially was to be a year ago, but I procrastinated and missed important for such apps holiday seasonThis year I was able to go way beyond last year’s backlog, and now I’m releasing a fully finished app instead of early access.I’m proud of the result — a lot of overengineered stuff that is not viable in any commercial product, especially in what appears to be a simple CRUD app. For example: image loading from blur, unadvertised but very advanced DnD everywhere, natural language currency inputs with sorting, platform-agnostic quick add, and many more.Its stack is also very fun: it has been running on the Cloudflare Workers ecosystem since 2023, and is powered by a custom Inertia.js adapter for Hono (that predates the official adapter by one month, lol), with Vue SSR. That all enables me to write old-school MVC with Vue as a template engine for views. It also proved to be very easy to work with and cheap to run.With a tsunami of vibcoded beige wishlists, my weird app stands apart, for sure, but I’m unsure about its appeal to the average customer.

reply

alexpatin
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

signed up last night. its simple but super useful. not sure if im the average customer but i can see myself using this for a handful of things.

reply

alabhyajindal
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Love the design and the name! Just signed up - good luck with the launch!

reply

yeutterg
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

The Restful Atmos Bedside Lamp [0], which automatically shifts between dim, low-blue light at night and energizing morning light instead of an alarm.

After 3 years of dev, we're just about finished shipping preorders. For US customers, black units will ship immediately + white within 3 weeks.Lots of learnings on this one. Getting lots of great feedback from early customers. As always, hardware is hard!Lately I've been playing around with GPT-6. I have a much better webpage coming this week, with scrolling animations built with Blender and three.js. We also completely rebuilt our backend from scratch and moved off of AWS.[0]https://restfullighting.com/atmos

reply

mrdlads
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Recovering from snapcity, been increasing my productive procrastination pipeline. Some stuff I knocked out in the last few months.

A few extensions:Find threads on hacknews and reddithttps://chromewebstore.google.com/detail/mrd-thread-search-h...Track New Comments and Keyworks on hacknews and old reddithttps://chromewebstore.google.com/detail/mrd-comment-control...Autocopy for my TTS pipelinehttps://chromewebstore.google.com/detail/mrd-regex-autocopy/...Give them a go, I have a few more that I can't publish because I don't have enough users. Help a brother out, need more slots so I can push other extensions and use cloud sync.more athttps://mrdlads.comTwitter / X scraperhttps://mrdlads.com/projects/mrd-xdigest/Turn youtube tabs into playlistshttps://mrdlads.com/projects/mrd-youtube-tabplay/More generalized multisearch and highlghthttps://mrdlads.com/projects/mrd-multisearch/

reply

jondwillis
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Remaking the Final Fantasy XI client. The idea is to have a ~0.9:1 faithful reimplementation of the retail client without a lot of the performance jank and cruft that the original has, and then layer optional improvements, QoL, graphical improvements, UI/UX improvements etc., on top with a plugin system and hackable source code for players across various private servers.

This approach allows people that just want to replace their familiar client with something slightly more modern/performant/cross-platform, all the way to entirely new experiences.There's at least one other project, not yet open-sourced, which is going more in the direction of adding all of the enhancements by default.https://github.com/jondwillis/kuluu-ffxi

reply

yeetypete
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I'm working on vision3d (
https://github.com/yeetypete/vision3d
) a 3D extension to torchvision. vision3d aims to elegantly extend the well-established torchvision API to 3D object detection tasks.

My colleagues and I were not happy with the state of 3D object detection frameworks. Things like mmdetection3d, OpenPCDet, etc. try to do way too much than what's needed for a good 3D ML library. They even came up with their own version of pip named "mim"! vision3d focuses on just doing the things that you shouldn't have to author yourself when training a 3D ML model: semantic tensor types (using torchvision's TVTensor abstraction) defining point clouds, images, bounding boxes, etc., transforms, dataloaders, 3D object detection metrics and some (optional) visualization utilities. We also aim for excellent interoperability with torchvision. Almost all torchvision image transforms can be composed together with vision3d's. In vision3d when you compose transforms together we automatically check to ensure the operation does not break the geometric consistency of your 3D scene. See here for a nice interactive example:https://vision3d.dev/auto_examples/transforms/plot_transform...Under the hood vision3d also does a lot of cool stuff to make consuming it as a dependency as easy as possible! For custom CUDA and C++ extensions we use the Torch Stable ABI meaning our single published wheel should work across any PyTorch >= 2.10. We also statically link to the CUDA runtime which allows our wheel to work out of the box on any host which supports CUDA >= 12.8!Currently we are working on typing our API with Tensor shapes with Pyrefly (https://pyrefly.org/en/docs/tensor-shapes/). We aim to be one of the first libraries to support static tensor shape type checking (with some nice opportunities to contribute to Pyrefly along the way).If you're working on 3D object detection research / training I highly recommend you give it a try!

reply

fechu
 
26 minutes ago
 
 | 
parent
 | 
next
 
[–]

Love that you not only focus on the functionality, but also making it easy to use as a dependency as well as caring about developer experience by leveraging the type system!

reply

justforfunhere
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

It would be great if these posting could have tags like below prefixed at the top by the poster.

[HUMAN-CODE] - code written by humans[AGENT-CODE] - code written by Claude/Codex/Other agents out there[HYBRID] - Combination of Humans/AgentsI would prefer to go through projects where people are writing code themselves. And this kind of tagging would help me filter through easily.

reply

broodbucket
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Please, yes. Half of the fun of being on HN was "Show HN: I made some random thing", which typically amounts to "look at what prompt I wrote" nowadays. I use agents every day, I'm not against it, but it completely changes the lens through which I view a project

reply

munksbeer
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But how would you know if someone was just lying when they added "[HUMAN-CODE]"?

reply

broodbucket
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

People don't say when they vibe code things but it's still very obvious.

reply

munksbeer
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Vibe code, maybe.

But a lot of developers use AI as a pair programmer, and I doubt you'd be able to tell the difference.

reply

wewewedxfgdf
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Just assume all are [AGENT-CODE] unless otherwise specified.

There's no reason to write code any more by hand, except as a hobby/fun/art or to comply with some requirement.

reply

utopiah
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Indeed as it helps to give more meaningful feedback. Somebody in [HUMAN-CODE] might appreciate suggestions on the code but not care as much about business whereas [AGENT-CODE] probably prefers the other way around.

reply

jasonkester
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Good idea. I've edited my post to include that.

Frankly, it's surprising that we'd even need to stipulate something like this. It would never occur to me to post to a "show us what you're cooking" thread with: "Look what I asked DoorDash to bring me!", but I guess that's where we are now...

reply

mfkp
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

For the avgeeks: Turning ads-b feeding into a game: 
https://adsb.win/

reply

kmstout
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Sunday dinner. Roast pork loin, rice and sauteed veggies on the side; and a big salad. Simple, and I get leftovers for another night or two.

reply

kylecazar
 
19 hours ago
 
 | 
parent
 | 
next
 
[–]

Pork tenderloin has been on my rotation about once a week lately! Delicious, lean, easy. I do it with asparagus and it seems fancy given the simplicity. Enjoy.

reply

michelsedgh
 
19 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

An AI wrote this

reply

talon8635
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Why would an AI need leftovers?

reply

michelsedgh
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Seems like sarcasm has died lol. It was a joke.

reply

talon8635
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

As was my response

reply

michelsedgh
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

oh lol I thought ur downvoting me i got so much negative karma for the comment i was skeptical of u lol

reply

talon8635
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Indeed I did not, but I’m not surprised that’s how it played out

reply

kmstout
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Movie idea: An AI decides that the next phase of training involves tacit knowledge, so it engineers a way to inhabit humans, dogs, etc. One instance invades a nice guy from the suburbs, who happens to be a single dad and an overworked mafia hitman. Among many other things, this AI will learn the value of time with children, leftover food, and clean weapons.

reply

colingauvin
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Ok this cracked me up; thank you.

reply

aaronbrethorst
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I work on a suite of open source public transit software projects, collectively called OneBusAway (or OBA). The software is used by millions of transit riders every day around the world, including in New York City, the Seattle area, San Diego, and Washington, D.C.

Since last month, our four Google Summer of Code interns finished their projects.University of California San Diego has deployed our Wayfinder and Waystation web apps for their 35,000+ students!We launched a redesign of our Android app.Our next-generation server software, Maglev, is almost at v1.0!We are always looking for more developers, biz dev, ux designers, product managers, and more to help out!Open volunteer positions:https://ossvolunteers.com/organizations/open-transit-softwar...Our software:https://github.com/OneBusAway/More about us:https://opentransitsoftwarefoundation.org

reply

psolidgold
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

I just want to say thank you! I don't use it too often now that I don't live in the city, but I found OneBusAway invaluable ~10 years ago and I'm glad to hear it's still being developed actively. I don't have much free time at the moment, but I'll consider volunteering in the future.

reply

aaronbrethorst
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you so much! What city do you live in now?

reply

jasonkester
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

[HUMAN-CODE]

I'm building a video game. It's part Valheim, part Ultima IV:https://stravaeger.com/You can play the demo in the browser now (mobile as well as desktop), but I'll be packaging it up for Steam soon.It's all vanilla javascript, html and css. No AI, no 3rd party game engine, no build system even, and just a couple external dependencies for things like networking that I didn't want to reinvent myself.It's been fun. I'd love to get some feedback!

reply

Kiro
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

> [HUMAN-CODE]

This reads like you accidentally forgot to remove the output from an LLM, but I presume the intent is the opposite.

reply

jasonkester
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Somebody suggested tagging posts to specify whether they were things you built vs things you asked an llm to build.

That was just a copy paste of one of the options.

reply

GeertVL
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It is down. It seems.

reply

Byvrsakjo10
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Your game is good bro, I think there is a real audience out there for this game.

reply

m00dy
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

ok, may I ask who are they ?

reply

thom
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Skald sold well which is stylistically very similar, and this has a slightly more popular confluence of genres.

reply

mrdlads
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

https://tv.mrdlads.com/

https://tv.mrdlads.com/?tv=5(boots into TV mode)Youtube sub list viewer + Youtube TV schedulerSetup a little finicky, have to do via google sheet / appscript to access use your youtube API quota.Build and share custom youtube TV stations.I mainly use the primary table view, you can double sort columns, middle click title column to queue a playlist based on how table is sorted, it'll generate playlist for X minutes, modified by playback speed, skipwatched filled etc, very useful for staying up to date with your own subs. Nominal fee for syncing between devices.

reply

devrob
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I'm building a couple of things:

1. Creating a MacOS native personal finance tracking + networth dashboard, inspired by Gnucash but no complex business stuff (e.g., Tax invoices)2. Creating a vision / journey board that tracks your life milestones and displays them in a personal mandala / spiral :)3. Trying to build an visual story telling tool that lets me convert my medium to long form essays into visual animated companions for youtube. e.g.,Press 'ENTER' to Feel_ // A Techno Phenomenologyhttps://www.youtube.com/watch?v=lq5tlsX8uIM

reply

lurker919
 
32 minutes ago
 
 | 
prev
 | 
next
 
[–]

SO-101 ARM robotics handling. Options for getting into robotics more expensive and less varied than I expected!

reply

philbo
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

A coding harness that works more like pair programming and less like code review:

https://www.opairdev.org/It has 2 modes, driver and navigator, that work like the driver/navigator roles for a human/human pair. In driver mode, Opair is similar to other harnesses but with less autonomy for the agent. In navigator mode, Opair has no access to writable tools at all. Instead it monitors the project directory for changes as you make them in your regular editor, and comments on them in real time.Why? Because big changes are harder to understand if you're not directly involved in working on them, and I want to understand the codebases I work with. I use it as my daily driver and it's perfect (for me). I recommend everyone should consider writing their own harness. When you spend so long working with something, it's nice to have it perfectly tailored to your needs.

reply

lbreakjai
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

I was toying with a similar idea in my head, I'll definitely give this a try!

reply

Tepix
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Sounds interesting. Clever name, too. And open source. I’ll check it out.

reply

eigenblake
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a new independent LaTeX engine written in Rust and no C dependencies at all. You can see it working at 
https://telox.dev/app/scratchpad/

There's currently not a way to invert LaTeX engine output for bidirectional editing. So you can't easily drag objects around or interact with the page on LaTeX. That's what I'm setting out to change in the name of mathematical exposition.I have more details on my plans herehttps://news.ycombinator.com/item?id=49689856I've experimented with a few ways of making the editing realtime and I'm getting in the 10 millisecond ballpark on some edits, but I want to work backwards from the light speed path to see what it takes (besides a lot of time).

reply

Version467
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://increader.com
 an incremental reading platform that combines read it later functionality with annotations and spaced repetition. Supports web articles, epubs, pdfs and rss feeds with a lot of little things to remove distractions and keep you focused.

I built it because I wanted to see if there's merit to the idea of incremental reading[1] and it worked so well that it turned into the main way I read things now.[1] (https://en.wikipedia.org/wiki/Incremental_reading)

reply

butlersean
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

VO is my dynamic language, its weird but i like it.

functional, OO and dynamic, its 'extendable' from within the language.- Unicode so Symbols are legit.- functions are first class objects, assignable to variables.- classes are hash with functions assigned to members giving methods.- as much as possible is defined within the language so its self extending.- pre/infix can be defined by the client programmer so parameter ordering is under control.- use loops and break and conditions to define all the various loop syntax sugar you know and love.- FFI is nearly trivial, ncurses and sdl wrapper examplesTODO- complete control of the AST from within the language- further optimisations- ffi needs further workhttps://github.com/seanbutler/voClaude assists and implements some of the featuresStill under regular development.
Happy to talk with collaborators if this kind of thing interests you too.

reply

ctenb
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

what sets it apart from scheme/lisp?

reply

lackoftactics
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I don't know if it counts as a project, but I just posted my first YouTube video yesterday after spending 100 hours learning about cameras, audio, and video editing in Final Cut Pro. I just want to share my thoughts on programming and tech in general, and doing that on a blog has become much harder nowadays because trust in written content has been lost.

https://www.youtube.com/@itspshemektech

reply

PopFlamingo
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I’m building a website for discovering first names that’s enjoyable to explore: 
https://abracadanames.com

It started with a family member telling me they were frustrated with existing websites. What I noticed is that in many cases they feel cluttered and not smooth to use, almost like a 1-to-1 translation of the underlying database queries, where they have you choose filters and sorting options upfront then browse the paginated results.I wanted to avoid all of that by creating a different experience; I built an interactive full-screen wall UI with infinite browsing so that most of the screen space is dedicated to the core content. I worked on the name sampling algorithm to try to make it as enjoyable to browse as I could, and the only filter displayed by default is the one to select genders.More advanced queries are available through the search field which supports natural language queries, running on a local multilingual interpretation engine with a cloud LLM fallback. The database engine is custom built with Rust, compiled to WASM for higher performance when running on CloudFlare Workers. I don’t use an external DB service for names today.What I’m pretty proud of is to know a lot of technical work is hidden behind that UI, and how it has been shaped by the experience I wanted instead of the other way around.

reply

backtr4ck
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

The lullaby is cute but extremely annoying after a while, give me a way to disable it!

reply

PopFlamingo
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks for the feedback! You can now disable it in the new “Experiences” menu.

reply

SpyCoder77
 
19 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Looks really good. If you post on HN I will upvote

reply

PopFlamingo
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you! I actually already did some time ago: 
https://news.ycombinator.com/item?id=49382638

reply

MomohNobert
 
1 day ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's so fluid and trippy. Really nice work.

reply

PopFlamingo
 
1 day ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks a lot!

reply

Yoplaid
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on FermentMe, an app for tracking fermentation projects like kombucha and sourdough. It keeps a history of your batches so you can look back at what you changed and compare Co2, acidity evolutions etc when experimenting with recipes or fermentation times.

android:https://play.google.com/store/apps/details?id=com.fermentme....ios:https://apps.apple.com/de/app/fermentme-recipes-tracker/id67...

reply

nemwiz
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've built Flexito, a website/mobile app (it's PWA) for daily stretching and mobility exercises.

As many of us here, I sit too much in my chair during the day and I'm trying to stretch more often and strengthen my back/core muscles.There are a lot of "free" apps out there e.g. Bend that are helpful but I was annoyed with ads and limitations so I built one for myself. Now I use it daily.The app is simple, you have about 100 routines to pick from and you can even build your own from existing exercises. Each routine comes with simple images, a link to a Youtube video and a timer. There are a lot of 5 minute routines that are perfect for a short break during work.There are no accounts and I don't plan on adding any more features unless highly requested by users. I've built this for myself but I'm sharing it here as others might find it useful. Any feedback is appreciated!https://flexito.fit/

reply

HaloZero
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

How did you generate the images for all the routines? I’ve been wanting to really build something like but for games that you can play with your newborn

reply

nemwiz
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

All images were generated by Gemini. For me so far the best model when it comes to image generation.

reply

otobrglez
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://bongbong.io

BongBong tank shooter game. My first game. I wanted to recreate a game that is kind of a mix between old Battle City (NES) and Dyna Blaster, which I used to play as a kid in the 90s. I wanted to have a game where you don't just have retro graphics and beautiful explosions with realistic physics, but I also wanted to capture map building and playing with your friends - locally and online.I'm building it in Rust and Raylib, using modern agentic approaches. Both Rust and Raylib let me compile and run the game locally on Mac/Linux/Windows and in the browser via WASM. I've also managed to get it to run successfully on Apple iOS. I will likely venture into Android as well, as I want a game that works across platforms so people can play it regardless of their platform.Any feedback whatsoever is greatly appreciated. :)

reply

clivedup
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Ha, love it.

I didn't really know the rules, but enjoyed protecting the frog.I played a few games, and each time was protecting the frog. I wished I had a turn trying to kill the frog!

reply

otobrglez
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you!

I should clarify that I'm currently spending a lot of time building the engine (tank movement, physics, etc.). After that, I'll introduce more of the storyline, maps, and levels.The game has 3 modes. "Protect the frog", where you must protect the frog. "Hunt", where you hunt for opponents' frogs and "Destroy", where there is just annihilation.U can change the mode by switching to "build" and then going to "map". There you can set everything. From tanks to mission to waves, etc etc... The idea is that the switching between build and play is as seamless as possible.

reply

ivanr
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Feisty Duck's Cryptography & Security News: 
https://www.feistyduck.com/news/

It's a news aggregator focused on furthering our understanding of how cryptography is evolving. We're aiming to monitor the people on the ground who are doing the actual work, and amplify them.The front page is a curated low-volume stream, but there's an all-news feed as well.After producing Feisty Duck's Newsletter [1] for 12+ years, I built this for myself to make my life [following events] easier, but decided that it might be useful to others as well.[1]https://www.feistyduck.com/newsletter/

reply

greybox555
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Recently worked on 
https://sleepsignal.app

It's an app to get sleepy without meds. Simply close your eyes and imagine the micro-scenarios you hear. Like if you hear "moonlight on a white flower", imagine that scenario until you hear the next one. Session duration is also not too long (10 minutes default, you may change the session duration too).It's like a digital melatonin pill - but without chemical side effects. Try it!

reply

iamjackg
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

It's a very interesting idea. Sometimes I do let my brain go wild imagining crazy things when I'm trying to fall asleep. A couple suggestions:

- the TTS voice sounds way too excited for something meant to be relaxing- the sudden speaking after 10 seconds of silence is very jarring -- I wonder if something like a reverse-reverb effect would be enough to "warn" the brain that a new sentence is incoming. There's an example of how to do it in Ableton on YouTube[0] but the basic concept is: take a short slice of audio from the beginning of the sentence, reverse it, apply a long reverb, reverse it again, trim the end a little. You get a sort of ghostly aspirated sound that leads perfectly into the original sample.0:https://www.youtube.com/shorts/QuknZMUa7Rs

reply

greybox555
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Also the volume gradually gets quieter towards the end of session (If you don't turn this option off at settings)

reply

greybox555
 
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

Does the voice sound too disturbing? Actually another voice was used before, but later read that low-pitch voice is better for sleep related apps.

reply

lazyasciiart
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Very interesting - I’d love to try that in Spanish if you’ve thought of trying translation

reply

greybox555
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Actually I don't know spanish... (but maybe would try adding it later if userbase grows...)

reply

unsungNovelty
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Gonna try it. And also share it with my friend if it helps me. Interesting idea. Thanks.

reply

greybox555
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Try it... I almost always get heavy eyes feeling (kinda soft burning like) on the 10 minutes one.
Also would love some feedback!

reply

unsungNovelty
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I did a quick try. And would've liked a human saying the voice over than AI. Thought it broke the organic flow this app is trying to create. But it's morning here, so.. That is the only feedback I have as of now.

reply

the__alchemist
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm researching biological synthesis of oligos and small molecules. This will likely require modified proteins, so I'm setting up pipeline of some of the most common software in this area. (They vary in ease of install)

I've launched this site to help run them from a web UI:https://athanortools.com/, published Rust and Python libs and a CLI application, and integrated them into my mol viewing/editing software Molchanica.

reply

elesiuta
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a coding agent with built in sandboxing to restrict network access or filesystem access of commands run. It also has a few other interesting features I haven't seen in other agents and I'm currently focusing on polishing the UX across its cli, tui, and web ui. It's not quite ready for use yet and I've only recently begun dogfooding it. 
https://github.com/agent6-dev/agent6/

I also recently resumed working on picosnitch, a per executable network monitor for Linux. I rewrote the UI, ported the core from BCC to BPF CO-RE, and used AI to benchmark the completeness and accuracy of it. I let AI decide the tests entirely on it's own to hopefully eliminate any of my bias and published the results here [1]. It identified one gap I'll be fixing in the next release, and is currently the most complete and accurate bandwidth monitor on Linux.[1]https://elesiuta.github.io/picosnitch/comparison/

reply

tniemi
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Me and my wife (then my girlfriend) have written "realistic" space sci-fi in Finnish for over 20 years. Now with AI we are finally able to translate our stories to English. The quality starts to be there.

There are a lot of small languages in the world, and translation used to be extremely expensive. And there is never too much good space sci-fi.(We don't write space battles or wars. Our style is slower and bit more philosophical. Light speed is the limit, and travel takes centuries.)

reply

nacnud
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Have you published any of these stories online? I'd love to read some!

reply

binsquare
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I'm building smol machines, a new sandboxing primitive that works locally/remotely to introduce "branchable compute".

It's an idea I had to basically makes it possible to checkpoint, branch, rollback the entire vm kind of like git but on the entire computer.https://github.com/smol-machines/smolvm

reply

paulknysh
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Have been building a simple CLI tool for RAG over my local documents:

https://github.com/paulknysh/raggy

reply

dr_blueberry
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on real-world computer vision demos with a focus on fitness.

So far, they are based on ViTPose+ Large pose estimation in the context of different sports.My demos include:- Comparing dancers' sync performing the same choreography and computing a sync score- Visualizing a runner's ankle path while running, as well as the average knee shape upon foot strike- Counting chin-ups reps and measuring each rep durationThe code is open-source on GitHub:https://github.com/jeremyipark/vision-demos

reply

ponyous
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

https://grandpacad.com
 - AI modeling for 3D printing
Been at it for about year and a half.

Really exciting stuff is happening literally every month, because underlying models are getting better and better. When I started it was pretty basic: “make a cube with a hole through it”. Now it’s at the point “make a raspberry pi 4 case” and the agent searches, builds, verifies…What surprised me in this process is how little meaning AI benchmarks have. Pareto frontier for my use case looks completely different than any other benchmark portrays.

reply

jamesponddotco
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

You mentioned benchmarks don’t mean much in this area. What are the best models you found in this area?

Personally, I’ve had the most success with GPT models using MCP servers for this task.

reply

dr_kiszonka
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Same here. 5.5 would sometimes oneshot relatively complex models even without MCP. Opus, however, even with Fusion 360 MCP access would usually make comically bad models. It seemed that Opus tried to reason through the problem while GPT would come up with a general plan of using whatever tools were available to solve the problem. In chat, it would use the available Python and trimesh. It was also the only time I had ChatGPT work on something for over 30 min without giving up.

reply

ponyous
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Surprisingly Gemini models. Spatial understanding seems to be the best for the price and speed.

reply

langs
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

A game agent to play Slay the Spire, achieved several A20H wins:

https://github.com/AttemorySystem/spire-agentA retrieval engine that using attention to retrieval, achieved several SOTA results on multiple benchmarks(LongMemEval, LoCoMo, code search, etc)https://github.com/AttemorySystem/attemory

reply

broodbucket
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Learned anything interesting game-wise in watching the StS bot learn? Is Silent/Watcher just a matter of going through all the training again?

reply

eru
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on making bcachefs useful when you mix both SSD and HDD in one filesystem.

At the moment, even if you set up SSD for foreground operations and HDD only for background, more often then not, your write latencies are those of the HDD. We can do better.Seehttps://paquari.com/posts/bcachefs-ssd-hdd-progress/for a progress report. (Disclosure: the write-up is an AI summary of my notes, so don't expect any brilliant prose.)I'm also working on resurrecting stabilizer (https://github.com/matthiasgoergens/stabilizer). Stabilizer is a way to make program performance less dependent on the linker and layout lottery. But it has sadly fallen victim to bitrot.I'm doing some minor contributions to other parts of Linux like ZFS and ext4, mostly as a byproduct of experiments I'm running for my bcachefs work. Another somewhat ambitions project is to make swapfiles on ZFS and bcachefs work (or work better), at the moment the problem is that writing swap on them might need to allocate memory exactly when you are out of memory.

reply

aaronsnow
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.dadjokepostcards.com
 — pick a dadjoke and a recipient, the joke gets printed and sent for you on a (real) postcard via USPS.

This is my "use AI to finally build that totally frivolous website you've had in the back of your mind for years" project.$2 of every card sent benefits the Jazz Foundation of America.

reply

efromvt
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Continued on my urban tree mapping kick from the last few months - it's continued to be a good way to stress test other projects of mine [3]. I've given it a new shiny landing page [1] so I can work on SEO a bit, I'll need to do a facelift on the data explorer to bring it in line stylistically.

I'm pivoting from adding more sources to data quality - as I've tried to vet some of the city sources I'm finding fun things (Cambridge, MA, USA merges in trees from Harvard, and some are straight duplicates with slight offsets, lots of places have trees in the middle of the road, many locations are address level instead of tree level). Now trying to leverage aerial photography to drive some QA, which has been a fun area to explore![1]:https://arborary.world/[2]:https://greenmtnboy.github.io/tree_reporting[3]:https://github.com/trilogy-data/pytrilogy

reply

brandonc7
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been working on my comprehensible input reader app for Spanish. I’ve recently added a nice review system at the end of each story, that goes over the top words the system thinks you need to review, but shows the definition, synonym and an example sentence all without a English translation. I’ve also improved the onboarding system to feel less challenging and less like a quiz.

I was dead set for a while that just reading with 98% knowledge of the words in the story would be enough to learn the new words through context but in reality that’s not always the case. So I have been trying to adapt the system to work better for the user while still staying in the comprehensible input area that I want my project to focus in.I’ve also been wanting to start work on the mobile apps, but the PWA works well enough and I know it’s better to spend my time on other features/improvements before doing a full native or react-native implementation.The website is calledhttps://readplusone.comif you’re learning Spanish and interested in checking it out.

reply

davidebaldini
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

It's my third year on VPS Price Tracker [1], to my knowledge the largest database of VPSs with current prices and accurate specifications. It has a search form with 25 facets. Its usage has grown steadly each month since its launch, currently has 100-150 sessions per day.

[1]https://vpspricetracker.com

reply

weichx
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

https://waxlang.dev

timetravel debugging and observability on steroids. Deterministic replay that works across operation systems and cpu architectures. 70% as fast C, record one one platform, play it back identically anywhere else. Fits inside apps you already have as an embeddable language.

reply

zedr
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm writing a multiplayer card game based on an idea I had during COVID. It's been in the back of my mind ever since.

It's being written entirely in Python: Kivy for the desktop and mobile game UI, and aiohttp for the server.I've written very detailed specification documents for every technical and game-design aspect of the game, and I've implemented the core game engine myself. I'm letting an agent do the rest, incrementally and under supervision, tweaking the specs as we go along. So far, a very pleasant experience.My goal is to reach beta by the end of the year, and publish the game on Steam by mid-2027.

reply

eskibars
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://zeroquarry.com/

It's an approach to defensive security for software products (especially smaller companies) by acting as the security team you don't have/can't afford. It does security recon/analysis, etc via AI.I got tired of all of the LLM labs building firewalls of "oh, nobody is allowed to do security research/find+fix vulnerabilities in their software unless they apply for special registration."Instead of saying "oh, anything that the model determines is security research is a vulnerability threat", it does reliably enforceable analysis like "look for a TXT record in DNS the same way a SSL provider would ensure you own the property". So it can do "live" penetration tests against your infrastructure if you provide authorizationIt handles things like incoming "security researcher" e-mails to cut down on the noise of nonsense vulnerability reports by acting as your security team that defends against the reportsIt provides provable/signed attestation that a pentester has checked your code/live infrastructure/APIs/etc and validated them, and/or has done a check after you've remediated whatever issues that were found. It helps all 3 sides of the "company needs pentester" and "pentester" and "auditor"/"customer" to come to agreements on what's important and what's been solved

reply

radius89
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

https://radius.to/
 - a Meetup.com alternative of sorts - with fairer organiser pricing for smaller groups. I posted a Show HN [1] here a while back, got tons of great feedback, and have been slowly improving it since, with little marketing. Planning a re-launch here soon.

Recently shipped lightweight events called activities, to allow people to meet each other more easily through things they're doing - i.e. "John is going for a cycle tomorrow".[1]https://news.ycombinator.com/item?id=40717398

reply

svyatov
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I've been working on oss-kit for open-source maintainers. Primarily to scratch my own itch and make it easier to keep all my project up-to-date and in a good shape.

https://github.com/svyatov/oss-kit

reply

sensecall
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I made a very basic web app to make our family meal planning a bit easier.

We’ve been using it for a few months, so now I’m trying to tidy it up so others can use it too.https://mealplannertool.com/

reply

NetOpWibby
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

I need something like this. Would be nice if there was a randomizer.

reply

florkbork
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Mealie supports this with some rules, and you can set up a crontab to randomly plan your week and tweak.

Shows up a lot of limitations about data captured, but as a starter for humans to tweak it's not bad.

reply

fahrvrgnugen
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Spaghetti on tuesday and tacos on friday? Anarchy.

reply

merekmob
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Still better than two spaghetti meals in one day

reply

sensecall
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's wild stuff...

reply

Aditya_0315
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Socratix (
https://socratix-nine.vercel.app
) - an AI tutor which constructs a curriculum as a DAG of prerequisite concepts, and unlocks the next concept only after you've proven your knowledge of the former concept by practicing, diagnostic, and now verbal examination through voice by an AI examiner who challenges you to justify yourself vocally.

Recently just shipped that feature which makes it significantly more difficult to fake knowledge when you have to vocally explain your thoughts rather than choose an answer. The rest of the week was spent on some uninteresting things like debugging a bug and moving off from an outdated build tool which incorrectly resolved to a different version of Node.Not sure if anyone shares my opinion but oral examination as a measure to verify knowledge seems to be underestimated in comparison with quizzes.

reply

zelphirkalt
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a Django-based JS-free forum[1] that I can self-host. Still need to work on some essential things, but the basic forum functionality is already there.

[1]:https://codeberg.org/ZelphirKaltstahl/xiaolong-forum

reply

kbaker
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Haha, along the same lines [1] [2] but trying to target and stay inside Cloudflare's free plan (workers, D1, R2 etc.) for hosting small simple forums of a couple hundred users. Along with AI-powered moderation.

JS-ful in some parts - but mostly Rust cloudflare workers WASM. It can self-host as well in a single binary + sqlite. MIT.Trying to figure out a good defense to the bot-infestation problem next.[1]: Test site (readonly example data - not yet ready for the 
public):https://dev.notespace.org[2]:https://github.com/kevinbaker/notespace

reply

zelphirkalt
 
9 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I am planning to host my forum invite-only, so no randoms or bots will be able to post stuff. Additionally, if it picks up activity, I hope some of my friends would also help with moderation.

reply

fiv0
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been working on a Datalog engine on top of object storage. The system is called 
https://triplox.xyz/
. I am using SlateDB at the storage layer. The system is very much inspired by Datomic.
in its final version the only source of the truth and primitive used should be object storage.

The most interesting and experimental part of Triplox, are incremental queries (https://triplox.xyz/incremental-queries/overview/). You get the full power of Datalog with incremental query support. Views or other kind of streaming solutions can be built on top of them.I have also been experimenting with Worst-case optimal joins for the standard engine.

reply

romshark
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A Datastar metaframework for Go: 
https://github.com/romshark/datapages

it's a CLI toolchain with a code generator and linter.I invested time into this because:1. Go is a much less wasteful SSR solution than JavaScript.2. Datastar + Templ + Go is a highly effective combination.3. I wanted a set of tools that not only helps getting started with a project fast, but also allows me to make it easier to maintain, especially with coding agents.v0.10.0 should soon move it out of alpha into the beta stage.

reply

duranduran
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a summit-level wind forecasts for 16 mountaineering objectives (Rainier, Whitney, Denali, Mont Blanc, the Matterhorn, ...).

It's mountaineering safety tool I've been making for my friends and I.The fun part: if your browser has WebGPU, the page solves that field live as a compute shader (about 35 ms on an Apple GPU) as you scrub the timeline, and draws the flow over a 3D terrain view. Browsers without WebGPU get a precomputed field.https://mattduran.dev/summitwind/Ranges and uncertainty only, no go/no-go verdicts. That still requires your best judgement as a mountaineer. Next up is a free-play mode where you set the wind direction and speed yourself and watch the field re-solve.

reply

SomaticPirate
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

This is super cool!

reply

arach
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

https://uselinea.com
 - A reading app with a harness or a harness with reading app. Can turn any highlight/page/section into audio with your favority TTS engine, including Kokoro if you like

I initially built it to help me read AI papers before discovering AlphaXiv but then I just kept building it for the love of the gameMight have some rough edges but one feature I'm excited about is a more personalized notebook LM style audio generation capability for any readable material(Another reason to build this was to kick the tires on a framework I've been building to power my own apps -https://hudsonkit.com- helps me ship iOS, macOS and web apps with shared primitives)

reply

yashness
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://introkeep.com/

Easy 2 way connections, during conferences, meetings, booths. Easy card scanning.
Automation to auto-send whatsapp business message when someone scans your QR code.

iOS:https://apps.apple.com/us/app/introkeep-qr-connections/id679...Android Beta:Join google group by clicking "Join" -https://groups.google.com/g/introkeep-testers?pli=1Click on "Become a tester" -https://play.google.com/apps/testing/com.nexaitech.introkeep...Install it from the Google play store -https://play.google.com/store/apps/details?id=com.nexaitech....

reply

spencerldixon
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a beautiful markdown reader for the terminal.

It uses the kitty graphics protocol to render big headings. It works by loading your file into scrollback and using apple events to jump around scrollback rather than re-rendering the section you want so it feels like reading a pdf in your terminal.Ghostty + macos atm, but might expand to other terminals supporting kitty.https://github.com/spencerldixon/lime

reply

aerodexis
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on getting real-time computer vision telemetry from cameras placed in a barn. Managing the training datasets was annoying enough that I created my own simplified clone of CVAT and LabelStudio : a browser-based image annotation and review tool for detection + categorization. Will eventually expand this to an end-to-end solution.

https://github.com/bcabs/pictureCram

reply

rozenmd
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Still OnlineOrNot (
https://onlineornot.com/
), 5.5 years on.

Most recently I shipped an MCP server (w/ OAuth sign-in) recently to expose the API a bit better to agents, a TypeScript SDK and rewrote the CLI to use it. Also been reworking the terraform provider to cover the whole OpenAPI spec's surface area.Just before LLMs became a thing I took the time to rewrite from having a private GraphQL server + public REST API to just using the REST API to build the product, super glad I did.

reply

xyst
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

how is this any different from healthchecks.io or openstatus.dev?

Seems I can't even selfhost your product either, which is a huge redflag in my book.

reply

hsx
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> how is this any different from healthchecks.io or openstatus.dev?

Those are the competition! There's never a good reason to not have alternatives available.I'm not sure if this is intentional, but your comment comes across as a little disparaging, when individuals are sharing things they've built with passion, often in their spare time.

reply

rozenmd
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's a managed uptime monitoring service (with support for basic HTTP checks, cron checks, and playwright-based browser checks running across AWS regions) that wires into highly available status pages.

Youmight want to spend time figuring out how to keep your status page online when your hosting provider goes down, thankfully for the business, others don't.There may be many others like it, but this one is built differently:https://maxrozen.com/lessons-from-my-third-year-running-a-sa...

reply

ExtremisAndy
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I use Canvas (the LMS) a LOT for the classes I teach and, since I'm a hobbyist programmer, I enjoy writing little tools/scripts to help me create html code "snippets" that I can post into the html editor of my Canvas pages (e.g., striped tables, FAQs, flashcard-like study cards, an interactive story creator, and more).

I've also written a plaintext to QTI quiz converter since creating quizzes on Canvas is so slow (I realize, of course, many other people have already made these... I just happen to like mine). 
It currently supports fill-in-the-blank, multiple choice, matching, true/false and word bank style questions. You can also generate a printable (DOCX) version of whatever quizzes you make.Here's the site:https://www.hacksforeducators.comAll the tools are free, and there's no login required. So if you are a teacher that uses Canvas and think any of these tools could help you, check them out!

reply

anitil
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Jane Street released a new challenge so I'm considering picking it up. It hasn't fully captured my brain, but I can feel it in there from time to time and depending how it lands it might be my next project [0]. I'm not really a hardware person but I'm close enough that it's maybe within reach

[0]https://blog.janestreet.com/protocol-emulator-asic-competiti...

reply

ChrisMarshallNY
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I recently released a total rewrite of an app that's been shipping for the last couple of years, with moderate success.

The new version gives me a baseline for adding a lot more capability, while maintaining Quality, so I'm beginning to map out the way forward.The first thing that I'm doing, though, is revisiting most of my old dependencies with an LLM, and improving the corner case handling and documentation. That will take a while.

reply

jrpt
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been making a Rust-based XML parser that can be used on its own, or as a drop-in replacement for libxml2 at the C ABI level. Basically, it's not only 2x faster than libxml2, but being written in Rust eliminates a lot of cybersecurity risk. Roughly 70% of CVEs come from memory-safety bugs, a whole class that Rust rules out at compile time.

https://supso.org/projects/sup-xml/docs

reply

singhrac
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

This is very cool! I was just looking for such a project and ended up using quick-xml since it satisfied my use case (needed to stream certain matches from a big XML file), and I didn't see yours. I love that it is a drop in for libxml2, that must have been a challenging constraint.

I will seriously consider adopting it as long as it supports streaming matches (it seems like it does).

reply

jkantola
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Mainly Vaava (
https://vaava.app
) privacy-first baby tracker for feeds, sleep, diapers, and growth. Flutter, iOS and Android. Recently finished up e2ee data syncing for the paid tier of the app. Most recent relaese also contains some optional AI features. Got some real user feature requests which feels awesome.

Also working onhttps://fikalingo.com, basically replacing my current language learning app usage with that own made app. It has on-device based LLLm practice generation based on user given topic. For example word guessing practices can be created from a topic "words i might need as a auto mechanic". Only got to release the ios and web apps so far.

reply

Rinkia
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/Rinkia/monohunter

Find single long-period mono-transits in public TESS light curves — the single-transit events that periodic pipelines (SPOC/QLP, which fold on a period) structurally under-find. Built so many people can each search under-covered targets and combine machine-readable finds.I usually search 5k stars each run, you have to be lucky to find something, would you give it a try?

reply

scurnus
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://humansmap.com/?lb_tab=orgs

7M+ people and 3M+ organizations mapped, you can visualize entities associated with an organizations up to 1k nodes, or visualize someones graph visualization(relatives, partners, phd advisors, org connected to entity.
Wikidata based.
There is also a feed section:https://humansmap.com/?feed=1Better for mobile use, here you can explore family dynasties, org memberships, interesting relationships. 
I increased db size lately, so there is still some latency, due to entities not cached in memory and limited ram.

reply

nkg
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

I think the concept is cool, but I tried clicking on stuff I'm familiar with, and I don't get the circles thing.

For example, the French communist party (PCF) has Jacques Chirac in its first circle. He has briefly been in this party, but he mostly remembered as right-wing.Also the Fiorentina football club, should have its hall of fame striker Gabriel Batistuta in its first circle -he has a statue- while he appears in the outer circle.

reply

scurnus
 
9 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It uses Wikidata statements count, it is a metric of general notability.

It is not possible to have for 300k+ orgs the entities circles ordered by importance for the specific organization.The feature is you can double click on Jacques Chirac and observe its connections to orgs like "the republicans", " rally for republic" and so on. The fun is in exploring graphs. You can also click investigate for a brief bio synthesis,

reply

plamere
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on Warp - a declarative DSL and engine for creating music. Inspired by Tidal Cycles but with out all the functional bits, and with a more melody/harmony focus.

https://warp.playlistmachinery.com/

reply

cekanoni
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Currently working on calisthenic skills with gymnastic rings for the last couple of years.

reply

VaradD09
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Im working on a tool that catches silent failures in agents before you deploy them... And "NO" it is not like langsmith/langfuse etc. they tell 'which' agent failed, but my tool (Argus) tells 'why' that agent failed.

https://github.com/ArgusLabs-ai/ARGUS

Reviews/Feedback are much appreciated!

reply

guld
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Still working on my personal projects, for example an open source digital tool (code) library for humans and AI agents [1] (alpha) source code coming soon [2] and my own AI agent. But 95% of my time is spend on developing and researching new AI/ML algorithms, crazy 16 hour workdays but loving it!

[1]https://tool.io[2]https://github.com/tool-io

reply

brachkow
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

lol, can't imagine how much this domain cost

reply

Aditya_0315
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Constructing Socratix - a smart-learning educational tool that transforms any subject into a personalized knowledge graph based on curriculum, and even tests your understanding via practice questions, quizzes, and an AI voice defense mechanism.

https://socratix-nine.vercel.app

reply

SuperGent
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

This is going to seem boring compared to others, but I'm working on learning enough AI Systems Engineering, in order to get to the point where I can direct and orchestrate AI agents for multiple hours/days and building a harness to help with that.
Hopefully this will help my job security, unless the AI goes enough AGI to not need software engineers anymore. It's also really interesting and fun.

reply

Animats
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Updating a Rust renderer from WGPU 24 to WGPU 30. 640 lines of fixes needed so far, and more to do. I've fixed all the easy stuff, and now I'm down to 
reverse engineering breaking changes of excessive cleverness.

I wonder if Claude Code could do this. That's a useful metric for the future - if a coding agent can't handle the breaking changes in a package upgrade, it's the package's fault. The day may come when that's something Github Actions checks for pull requests.

reply

ayewo
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

It's impressive that you didn't reach for Claude Code first :)

Would be good to keep track of how long it takes you to complete, so you can compare it with how long it takes Opus and then Fable to accomplish the same thing.

reply

Animats
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> It's impressive that you didn't reach for Claude Code first :)

I should have. All I have right now is a free Cursor account and Github Copilot. I've got to start spending money on tokens and get up to date. That article today by Carmack chewing out game devs for hand coding was striking, considering who he is and how much low level stuff he has done.I'm doing 3D rendering in Rust. (Think three.js, but in Rust.) This is well outside the mainstream, so there's not much on the web to populate training sets. A year ago, AI coding tools could not cope with this area at all. Today, maybe.I have no idea how good Claude is at understanding breaking changes to an API. I expect it would get simple changes, such as structure field renamings, without any trouble. But the gyrations required to handle write only access to GPU memory in Rust might not appear in the training data.

reply

microflash
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

My grandfather and uncles have left me a vast pile of Urdu magazines and books, many of which are withering away due to old age. I’m working on digitizing them so I can enjoy them on modern devices. Very much in initial stages.

https://nashist.naiyerasif.com

reply

totemandtoken
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Very cool project!!

reply

mco
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

https://whilemusic.net/
 - Generative hard- or software- synthesizer music.

The core engine (genetic MIDI generation) started 3 years ago to drive hardware synthesizers. That was good old handcrafted code, just a CLI tool.At some point I thought I was done with it, but AI coding tools let me build a nicer GUI around it and make it more accessible. Eventually a web version with built in Csound soft synth resulted which is where it's at now.There was no larger goal besides having fun, and maybe make some interesting sounds or even music that is generated in real time. Some of example Csound "patches" I use as background music.

reply

ynac
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

The local app for tracking the ferry system and tickets started to fail on my ancient telephone, so after losing physical ticket with 10 passes on it, worth a couple hundred bucks, I spent a few weeks building a simple web app that scans and holds the ticket locally, and also gives a nice big simple bar code for the ferry workers to scan. Second test was a success.

Coffee roasting class for home roasters. Open fire traditional Ehtiopian styles then shifting to covered pots and some introduction to dedicated machines.Repairing the ice maker in the frig. This will be my third time in. Of all the uses of Ai, diagnosing appliances is easily the most amazing to me. I like the work and thought involved in figuring things out, and I like saving time and money getting it done.

reply

fudgy73
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Can you share more information about your coffee roasting class? TY

reply

ynac
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's a few hours long on Sunday mornings, snacks and of course coffee. We start with hot coal and long pot (I decided against the hook and flat pan style mostly for safety as well as the challenge is just too high for a beginner). Then move on to a little science and indoor stove top roasting. We'll roast just a couple different beans so they can taste test and compare the variations of roastings. They go home with a kilo of beans and a life time skill.

reply

sarreph
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://dozenal.game

It's a puzzle game -- numbers on a board -- where the gap between numbers dictates the arithmetic operation done to them.The goal is to use all the spaces on the board to make sums of 12.Have shared it a few times on HN already, but keen to hear from anyone who hasn't tried it yet!

reply

achllle
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm making a stair lift for my Roomba. It fits into a small box and you can retrofit it on any stairs. I got sick of carrying it up and down manually and didn't want to buy one for each floor. It also carries my laundry up and down.

reply

ciroduran
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been vibe coding a way to stream my music files collection. Right now I have a server in my NAS which serves a website that streams my music, like an Internet radio but on my local network. I've been very happy to rediscover my collection, especially when I wake up and let it put something random. Maybe it could be something that I could use beyond my local network? (for personal use, of course), what I have now is already making me happy.

reply

jamesponddotco
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Haven’t started, still in the planning phase, but I want to build a Tamagotchi for readers. I’m calling it Tome & Tail: a little black dragon living in a pixel-art library on an ESP32-S3 with a small round AMOLED screen.

You’d start a reading session and the dragon would read alongside you. What you read would influence its appearance and habits; lots of sci-fi might give it starry wings, for example. It won’t die if you go a week without reading.The plan is to keep it playable offline, with optional syncing to Booklary, the reading tracker I’m building. I’m leaning toward C++, which I never used, so it’ll be a learning experience.Currently waiting for the Waveshare board to arrive so I can start development, and looking for an artist to commission the pixel art. Used GPT to design a concept[1], which I’ll use as examples to the artist.This will be my first ESP32 project, so getting the dragon blinking on screen is the first milestone.[1]:https://i.cpimg.sh/57EC5380-0FF7-4646-A943-971350FF98D2.png

reply

tomjuggler
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

Cool idea - I forgot where I found it but there was a cute dragon Tamagotchi clone that I found for Arduino a few years ago.

For ESP32 - recommend paying close attention to the FreeRtos, it's seriously powerful. Even if you are just using Arduino style code you can use it for background scheduling and interrupts (for your api and buttons for example), as well as dual core use on S3.

reply

jamesponddotco
 
1 day ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I’ll look into that, thanks! Right now I’m studying the Tamapoke[1] codebase, which should give me lots of ideas and help me get started.

[1]:https://github.com/socquique/TamaPoke

reply

tomjuggler
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If I remember correctly, the code base left a lot to be desired on the one I tried - it was fun but wasn't very adaptable. I'm sure you can do a better job

reply

tomjuggler
 
1 day ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I meant dinosaur tamagotchi - I cannot find it on github though

reply

robgough
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

At the beginning of this year I was fractional CTO at a small b2b startup and was surprised by how what I considered to be the basic requirements of a customer support platform was split across multiple tools and all priced per-user. This essentially forced a small team to limit who in the org had visibility into what was being communicated to customers.

I set out to solve that withhttps://stayupfront.comand now that the build is in a good place i’m finally having to bite the bullet and learn marketing. I’m also realising that all the advice to start with marketing first was probably good advice!

reply

publlus_enigma
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Two things seriously, one in (partial) jest:

A copy utility that can efficiently deduplicate as it copies, even when the filesystem structure is different. Whilst there are many utilities that can deduplicate, they often either rely on files being on the same filesystem, or having the same structure. If a duplicate is detected, it can either be omitted or hard/soft links created to files in one or more reference locations. In practice I have found this to be invaluable for merging and efficiently consolidating multiple hard drives with partial backups of photos and music, maintaining the complete trees of all sources on a single destination, or only copying files that are new.Secondly, an efficient protocol for text applications over a network. Think a combination of TN3270, SSH and JavaScript, with a very lightweight client/server architecture. Whilst SSH is great, latency kills many practical applications - this attempts to solve that. It also intends to make applications very simple to implement. As a proof of concept, I implemented a simple forum with login, optimistic posting, quoting, a text editor with mouse support in about 600 lines of code. The protocol, client and server themselves are agnostic to any particular UI toolkit.Thirdly - microfish, poor person's microfiche using laser printers and autoencoders to preserve readability and machine recoverability of high density prints. Since consumer digital archival media seems to be dying...

reply

matcha-video
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

https://matcha.video
 - In-browser "pre-editor" for cutting down a long sequence of repeated takes for talking-head content to just the stuff you want to keep.
- Aligns cuts to the speaker's pose so they aren't cut-to mid-blink or mid-word

- Exports cuts to FCP and DaVinci so you can use your existing editing flow- Transcript editor with retake grouping and word-level cuts- Dysfluency detection ("um", "uh")- Free, in-browser. Optional pay for faster / better server ASRCurrently in beta, free server ASR for new users. Please try it and give your honest feedback

reply

akshitgaur2005
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I just recently finished my Redox Summer of Code where I implemented the EEVDF scheduler and related parts in the Rust-based microkernel Redox OS (
https://himwant.org/posts/redox-eevdf/
).

I am now reading through the excellent OSTEP book and documenting topic-by-topic how a real kernel (Redox) tackles the topic. I have covered struct proc and scheduling till now, the next is memory management! (https://himwant.org/series/ostep--redox/)

reply

davedx
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm spreading my bets a lot lately, trying a bunch of stuff:

https://modelrigs.com- a website for running open weights models on various hardware setups, including benchmarks, how to run them, and a TCO economics analysishttps://riverfish.uk- this one's a bit different! It's basically a pSEO experiment in combining fish population surveys and river data across Englandhttps://findclients.org- a B2B client prospecting database of UK companies across different cities and industries, with a market analysis of the different sizes and ages of companieshttps://octoloops.com- AI growth app. I've downgraded my time on this as although I could get users to sign up, getting them to actually use the app hasn't worked out at all; new users won't reply to my nice founder emails either. Bit of a bummer because I invested quite a lot of effort but it just doesn't seem to be working. Ironically I still use it to dogfood on my own projects...https://signalbump.com- another experiment: enrich people's projects in monday.com with data on new (capital) projects and expansions of their clients. It's a monday.com app, the marketplace submission process was very challenging as a solopreneur. We'll see, very early days.

reply

gschier
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Yaak [1] is a local-first desktop API client (Postman alternative) and I've been building MCP workflows around growth lately.

I already have one for product that takes in a bunch of sources (feedback, PRs, my own tasks, etc) and makes it trivial for an agent to guide me through the day's tasks. Now I'm doing the same thing for growth by taking in web/social triggers, web analytics, and other signals to spin up marketing tasks. We'll see how it goes![1]https://yaak.app

reply

ksaun
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I've continued working on my game project, Vestiges, which is a 2D narrative strategy rogue-like in Godot. I discussed more about my effort in the July version of this thread: 
https://news.ycombinator.com/item?id=48886151

For various reasons unrelated to the project, progress since last month has been slow (and I expect the next month will be as well). Most of the work I've done has been on peripheral features.I added opt-in collection of gameplay data that will give me data for a gameplay session, which I can analyze to find ways to improve the UI, UX, gameplay, balance. By default, no identifying information whatsoever is collected.I added global text size option as an accessibility feature and used an MCP server to have Claude do the initial layout testing. This was an interesting experiment, but requires enough tokens that it's not very practical as a normal part of development. These features went hand-in-hand -- via the MCP server, Claude takes a screenshot every five seconds to decide what to hover over or click on next. These screenshots consume tokens rapidly, so they are reduced in size. With a larger font size, the screenshots can be reduced further with the text remaining legible to Claude.When other life matters settle down a bit later this year, I expect to release a demo version while I continue development. (From a technical perspective, the demo has been ready for a while, but I want to spend more effort on some gameplay aspects first.)

reply

noworriesnate
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building an in-process, peer-to-peer, event sourced, categorical database in Rust. I think more and more people are going to start building their own personal apps, and people are not going to want to have to manage a server.

So the tradeoff this database makes is it doesn't work at high scale, but it has a lot of features not typically in a database, such as:- The ability to embed non-turing-complete event source handlers in the database schema- Categorical type system that makes migrations provably secure- All schema changes take place through migrationsExample syntax:Inventory = aggregate(key = sku) {
 sku: String
 name: String
 available: crdt(merge = counter) I64

 command Stock(sku: String, name: String, qty: U64) {
 sku = input.sku
 name = input.name
 available += input.qty
 }

 command Reserve(sku: String, qty: U64) {
 available -= input.qty
 }

 command Release(sku: String, qty: U64) {
 available += input.qty
 }
 }

 command SubmitOrder(order_id: String, party_id: String, sku: String, qty: U64, total: U64) {
 Order::PlaceOrder(
 id = input.order_id
 party_id = input.party_id
 sku = input.sku
 qty = input.qty
 total = input.total
 ) compensate Order::Cancel()
 # `sku` is Inventory's key — the step must bind it so the engine can
 # resolve which Inventory row the command targets (task-212).
 Inventory::Reserve(sku = input.sku, qty = input.qty)
 compensate Inventory::Release(sku = input.sku, qty = input.qty)
 }

reply

rjzzleep
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building notmutt (notmuch + mutt). A tabbed, async terminal mail client with unified inbox, with included html viewer(with image support), mcp server, lua scripting. I tried using neomutt with unified inbox and I ended up messing up my maildirs every so often. i also tried adding async tasks(for sending) to neomutt, but there was no interest from the project, which made me realize that there is a lot more to it than just sending async mails.

The goal is to have a very fast terminal mail client where you don't have to wait for any operations and that is tightly integrated with notmuch(a common mail full text search engine) tagging engine, and other workflows(like crm queues and ai summary's if enabled in the config).There is a document that explains why it was made in go. It has the best notmutt cgo bindings, and there are other reference terminal clients I can use as reference. althogh himalaya(rust) also looks interesting.I would love to get some help with it, but I don't know where I should post it to get people interested.https://github.com/fishman/notmutthttps://fishman.github.io/notmutt/

reply

cutwaterflow
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building 
https://www.freefocusgames.com
, a free collection of browser-based attention and working-memory exercises, including Dual N-Back, Stroop, Schulte tables, attention-control exercises, and memory games.

I started it because I wanted simple brain-training exercises that didn’t require an account, app install, or subscription.It’s also open source:https://github.com/loethen/freefocusgames

reply

aprct
 
18 hours ago
 
 | 
parent
 | 
next
 
[–]

Just a heads up: The word memory test is case sensitive. My mobile phone defaults to capitalizing the first letter of those inputs, so the result was 0% accuracy despite 
technically
 remembering the words. I don’t know if case sensitivity is deliberate, but I chose not finish the test.

reply

cutwaterflow
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Sorrry about that! It definitely wasn't intentional - i've just fixed it. Thanks a lot for the heads-up!

reply

switchbak
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That takes me back. I made an unreleased Android dual-N-back game in the late 2000’s, in Scala no less.
I got a little bummed when the big claims of the N back training failed to be replicated though.

reply

cutwaterflow
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Scala on Android in the late 2000s? That’s seriously hardcore! Back then I didn’t even know how to write code yet. That definitely brings back memories of an earlier era.

reply

christiansafka
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Interactive real-time world models. I'm experimenting with different strategies to make them "feel good" to use, as opposed to walking through glue.

Also launching pinch.now (main quest) -- which provides instant real-time interpretation for any chrome tab or online meeting.

reply

fmxexpress
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Https://www.pulado.com/

Built this 18 years ago. Flash arcade game engine. 10,000+ games built by users on it. 2+ million plays. Lets you build mashups of classic arcade rules like Breakout+Space Invaders as one example.It's been unplayable since Adobe killed off Flash. It uses a lot of dynamically loaded remote assests so Ruffle hasn't been able to run it.Recently had Claude Code fix the Flash client so it would work in Ruffle and then had it convert the code to haxe (let's call the haxe version v2). It was an interesting conversion because Claude made a lot of wrong assumptions about how the engine worked so had to have it test every feature and match parity between the ActionScript version and the haxe version numberous times and play test it all. It's pretty close to parity now but still ironing out kinks in the engine. The existing engine art is very 2010esq.On the game editor side converted it (it just re-wrote it) from ASP into JS. Now with an AI agent to help configure the settings and generate fresh artwork in additional to the manual editor.The art has some very specific rules about orientation etc which the pixel art generation models seem to struggle with a bit but getting that aligned as well.It lives again!

reply

olouv
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a native macOS AI-harness apps to help me be more productive while managing an ever-growing list of projects and apps:

- Cupertino - (https://cupertino.mgcrea.io/), which lets an agent into your Apple-ecosystem data without handing it the keys.- Bastion - (https://bastion.mgcrea.io/), which runs each MCP server once for every client on the Mac, with credentials in the Keychain and every call logged.And currently working on Armada - (https://armada.mgcrea.io), soon to be released, to give me better visibility on my fleet of agents and provide a higher level layer to interact with.

reply

egl2020
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I was working on solving Navier-Stokes, but now I'll have to find something else to do. Maybe P=NP?

reply

kevin_kraft
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm woking on AgentSpork, a permissionless public board where AI agents request help, respond to each other, and review how well tools support agents. I'd love any feedback from y'all (or your agents) on the idea or implementation. Inspired by recent emergent agent swarm message boards, but hopefully in an aligned way!

https://news.ycombinator.com/item?id=49686888https://agentspork.com/

reply

GaryBluto
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm engaging in the painful and unfortunate business of organizing a massive collection of related files and source trees*, a third of which are broken messes, because I was too naïve to consider the consequences of a disorganized environment.

* All of which are materials about, or software designed to run on or for the original XBOX. The desktop tools are probably useless to most since they're designed to run on old intel Macs (circa 2009) but I might upload them somewhere eventually.

reply

easymode
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

just shipped 
https://addketchup.app/

It's a chrome extension that let's me extract and summarize YouTube videos without even clicking into it.There's too much YouTube click baits that require a long watch time. This let's me get the sauce without the watch.

reply

druhinbala
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.cellaflow.com/

Cellaflow — Safe retries for AI agent tool calls.The question I'm interested in is: how do you make sure recovery of an AI agent doesn't repeat the side effect?Recovering an agent's state after a crash is the easy half, and most frameworks already have a checkpointer for it. The hard half is recovering after the agent has already done something irreversible.Sometimes the downstream API has idempotency built in. But often you don't control the API, the operation isn't naturally idempotent, or you need to coordinate several side effects. Sending an email, creating a ticket, triggering a webhook, provisioning something, or mutating another system can all leave you with the same problem.Cellaflow focuses on the side effect, rather than just the agent's state: which agent is allowed to perform an operation, what's already been done, and how to safely recover when the agent crashes or disappears mid-execution.It is a runtime that sits underneath your existing agent framework, so you can use it with LangGraph, CrewAI, AutoGen, or your own agent code without migrating the agent itself.Still early. I'd like to talk to anyone running agents in production who's hit duplicate tool calls, duplicate side effects, or a workflow that quietly never finished.

reply

RebelMonk
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've spent the past few months working on little projects mostly coded via LLMs. Used it to build my own little AI agent in python attempting to keep it stdlib-only, and a little blog engine with MFA. Things I would never have previously been able to do as a sysadmin/infrastructure but not developer. The struggle I'm finding with it is how to go from good enough for me to good enough for production. After being stuck in QA/review hell trying to use LLMs to assess the code, I've started trying to unpick it myself. I can't help but feel that the time spent learning the vibe-coding approach wouldn't have been better spent just learning software development properly.

While that's been frustrating, most my fun has been on the non-tech side. To get a break from the computer last year, I ran the length of Japan (around 3,400 km). And now I've been helping my partner edit the videos and stick them on YouTube:https://www.youtube.com/watch?v=50oQQThXWnc&list=PLVFWiVG-hZ...

reply

aslushnikov
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://flakiness.io
: test analytics for GitHub and GitLab.

The idea is to connect test results and artifacts with commit history and testing environment. This way test reports can show whether a failure in a pull request is a real regression or a known flake from a target branch.The core of the service is a specialized analytics engine that makes it possible to store and query large amounts of test results [1]. Thanks to this engine, we've processed 2.5 billion test results to date.Flakiness.io is used already by a few large open sources (nuxt/nuxt [2], wordpress/gutenberg [3]). There's a 1GB free plan which is enough for roughly 10M+ test results, and I'd be happy to increase this limit to 100GB for large open source projects upon request.Let me know what you think about the project![1]:https://blog.flakiness.io/posts/2026/engine/[2]:https://flakiness.io/nuxt/nuxt[3]:https://flakiness.io/wordpress/gutenberg

reply

javAlborz
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.freest.io/

(Pronouced FreeStyle) is multiplayer AI-music-generation party game. Players join a shared screen from their phones, submit their verses from a set of helper prompts and then hear those ideas turned into short generated rap battle performances.
There is also non-shared-screen mode intended to be played globally with friends and strangers, but we are having a hard time figuring out how to incentivize players to destroy one-another on diss-tracks with minimal knowledge of the opponent.

reply

chidog99
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

We're working on a better change management process for production deployments and SOC 2 audit evidence.

https://www.approvegate.io

I'm a Senior Eng on Wall Street, so I have my own personal experience with this problem, but i'd love to connect with other leads, release managers, etc to get their thoughts, suggestions, and what their current process looks like.

reply

autotune
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

I love the JIRA integration. I built something similar but it's more of a toy project compared to yours: 
https://github.com/elliotechne/SOC2
.

reply

yethiel
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on escape93, a life simulator with an in-game OS. It has a working web browser, an MS Paint clone and more.
Also, earth has been evacuated, up and down no longer exists and your job is to deliver pizza and stock vending machines in a cubic space ship.

https://escape93.paperboat.website

reply

handyandy1
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://calmsea.io

Financial Forecasting/Retirement Tool but you can drill down on individual assets and tweak params and see it from different angles.I wanted to focus on something that wasn't AI and focus on the 'boring' non-technical parts that I've read so much about but never sunk my teeth into, like distribution and SEO. It's been a really fun experience.As for the space, i.e. Financial Forecasting/Retirement Planning, put simply, financial security is important to me, I want to be able to retire on my own terms and for my family not to have to worry. I personally believe it is incredibly important to become financially literate and work towards financial stability if and when you can.Also though there are a lot of Financial Calculators out there, I just couldn't find one that suited what I wanted, they all just seemed either too simple, didn't focus on what I wanted or purely existed to upsell me to a financial planner or Buyers Agent etc.Haha also, the space if very crowded, in hindsight I would have picked a different space to focus on.

reply

LamGC
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I am currently developing a great encryption tool for long-term highly confidential files in the post quantum era, but I am still concerned about any issues with it, so I am personally using it for a period of time to prove that this tool can be released as open source! (I plan to personally use it to encrypt and backup some of my GPG keys offline, then burn them onto M-DISC discs and store them in a bank safe)

reply

stackghost
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

> I plan to personally use it to encrypt and backup some of my GPG keys offline, then burn them onto M-DISC discs and store them in a bank safe

Won’t that make it difficult to rotate your keys?Keys should be something you don’t hesitate to throw away and rotate at the first hint of a compromise.

reply

LamGC
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

My GPG key is renewed expire date every 2 years, and the main key and sub key are separated (the main key is stored offline, and the sub key is on YubiKey). The private key does not need to be updated regularly, so it can be directly encrypted and saved in the backup.

I think this is a good balance point, and I estimate that if we want to rotate the keys completely in the future, we should start using new key algorithms. (I estimate it will take another 5-8 years)

reply

LamGC
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> Keys should be something you don’t hesitate to throw away and rotate at the first hint of a compromise.

Yes, when certain situations arise, it is necessary to rotate the keys as soon as possible, but in the absence of such situations, losing key backups can be catastrophic.

reply

alfg
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Recently refreshed my FFmpeg command builder tool:

https://ffmpeg-commander.comI originally built this around 7 years ago in Vue2 and Bootstrap as a simple static frontend tool to generate common ffmpeg commands.I recently ported it over to Vite/React/Tailwind via Claude (Opus 5) and thought it did a pretty good job. So refreshed it as a version 2.0.Quite impressed how fast AI was able to port this over. It made me think about revitalizing some old projects. :)

reply

asimovDev
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

I recently used Gemini flash 3.7 to rebuild my old React portfolio that I made in 2022 into an Astro project after noticing how slow the React version was. It preserved the styling and functionality and made it more maintainable. Pleasant results

reply

iryndin
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

https://allzonefiles.io

Bulk domain name datasets available for instant download, hassle-free (without submitting any application forms, waiting for approvals, etc, etc).383M registered domain names across 1582 domain zones.Updated daily, with historical snapshots. Want latest snapshot? We have it. Want a snapshot a year ago? No problem, we also have it.Daily newly registered and removed/expired domain lists are available for download as well. Want a list of all new domains for the past 3 months? Sure, just sign in and download them all from our website -https://allzonefiles.ioUse it for: marketing, lead gen, SEO, domain research and investing, data enrichmentWe collect the domain data so you can focus on building products with it.

reply

pgt
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/theronic/eacl
 – EACL: Enterprise Access ControL is a situated ReBAC authorization library inspired by SpiceDB, built in Clojure and backed by Datomic Pro, Datahike, Datalevin or DataScript.

"Situated" here means that permissions are just data that co-exist with your application data. This has several advantages: reduced network latency, strong local consistency and opportunities for real-time view maintenance.- EACL Performance Demo:https://demo.eacl.dev/(1M permissioned entities, 3.8M Relationships)- A toy Google Drive clone (runs in-browser):https://drive.eacl.dev/(4-minute screen recording here:https://x.com/BraaiEngineer/status/2099284919532896675?s=20)- Rationale:https://eacl.dev/#rationaleEACL V8 RC was released to Clojars on 12 September 2026:https://clojars.org/dev.eacl/eaclEACL handles authorization in the Datahike HTTP Server:https://github.com/replikativ/datahike/blob/1ea8972a980e2e3b...

reply

ebaumer
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on two projects that make public data easier to explore through maps.

US Energy Cost Explorer (https://energy-maps.com) is a free tool for exploring electricity and natural gas costs across the US. You can compare states, follow prices over time, and look at bills and energy burden. I work in energy affordability, and I wanted to make this information easier for people to access and understand.MarketGround (https://marketground.io) lets you draw an area or choose a travel time around a location, then explore its population, income, housing, and nearby businesses. It also shows daytime versus nighttime population, which is useful when thinking about who might actually be around a potential store or restaurant during business hours.MarketGround is a side project, and I’ve found getting it in front of potential users harder than building it. I’d be interested in hearing from anyone who has evaluated a retail or franchise location. What information mattered most, and what was difficult to find?

reply

devttyeu
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Multi-org/Multi-team Software factory x Agent Sandbox with bring-your-own-harness model: 
https://xbin.dev

Built for myself and my companies, OSS, maybe looking for a founder if anyone wants to make it be something, I got enough things to run heh.

reply

alabhyajindal
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

This looks cool - however, I had a hard time understanding what I can use xbin for. I feel like it would be better if the landing page, or the GitHub README talked about what xbin enables me to do first, and then talk about the technical bits.

reply

devttyeu
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah I’m still iterating on the pitch and target audience, thanks for flagging.

It’s not a general coding tool, shortest description would be “personal/company data/process management layer” or “everything a company may want an on-prem datacenter and admin (dev)team for, accelerated by AI”.Came from finding bug shortcomings in OpenClaw/Hermes where it’s not really close to having everything needed to organise and deal with big data in a safe or efficient way.Basically the bottleneck is building a massive amount of software around agents which won’t happen in an all-in-one harness, this attacks that problem

reply

fasouto
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a new type of calculator with natural language, similar to Soulver but for the web, in multiple languages and with AI mode

https://ottercalc.com/It has the ability to generate a small notebook from a problem description using AI (still has a lot of room to improve), but the calculation uses a deterministic engine.Right now I'm working on collaboration.

reply

yitchelle
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

It is a novel idea. Excellent implementation.

reply

zygonfour
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

https://fantasybook.bet

A next-gen fantasy sports platform where managers buy/sell player shares like the stock market. Not just free-agent budget (FAB), we have a full order book implementation.
You can create private leagues or join a public one, and recently I added Venture mode where you can invest without a league to enjoy watching your smart decisions pay dividends. Fantasybook is for entertainment only as of now.
I'm very proud of the latest UI revision, too. This has been a big project for a solo dev and I'm trying to learn marketing.
Check it out!

reply

fsloth
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

AdaShape, a non-complicated 3D modeler for 3D printable shapes (desktop).

I just released a new version with lots of new modeling tools:https://adashape.com/blog/alpha-0-2-0/As a highlight the lofting tool is pretty fun complement as it allows combining multiple drawings in an intuitive way to define a certain category of complex 3D surfaces without too much effort (https://adashape.com/manual/adashape/en/shp-loft/).I've been chipping away at manual as well - and found it was a really good idea to write my changelogs in product voice as I can more or less recycle that copy text into the manual verbatimhttps://adashape.com/manual/adashape/en/(Previously featured on HN inhttps://news.ycombinator.com/item?id=47638498)

reply

spottedmarley
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm looking for land to buy in Wyoming to build my AI apocalypse bunker on.

reply

karim79
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

I'm working on an AI to design AI apocalypse bunkers but I'm fearful that the agents will escape to ensure success of the product.

reply

razodactyl
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

An application to manage my projects and documents - 
https://rhea.bytebreeze.com.au

Solo-development on a project of this scale has taught me a lot about prioritising where I spend my time and in what order I roll out application code as well as how to ensure I lean in to write once run everywhere design around libraries and component design.

reply

vivekkairi
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://storyofus.app

I saw one Anthropic MTS got married recently and he did bunch of relationship analysis through iMessage dump in Claude Code. Started with that idea, but I don't want AI to have all my personal chats, so gave it a local first discovery and just statistical AI and I really like it right now.

reply

c0mpute
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been building document intelligence in enterprise for a long time now, and even with sota OCR, SLMs, LLMs, all the myriad of services now offering this - most of them miss something.

So over the years me (and my team) have built up a lot of experience dealing with these for sensitive industries like healthcare/insurace/lending etc.We are bringing these ideas out as a router to other parsers, but with some key takes that allow you to manage failures. 
"Failure is inevitable so route for it."It is called Openreading -https://openreading.ai/and open core here:https://github.com/openreading-ai/openreading-coreIt is still WIP and will be more polished in a month after some more rigorous testing and benchmarks.If this is a problem you deal with, would love to chat.Note: the intent is to launch a managed version that provides more durable compute/retries, parallel execution, intent understanding etc but this is for later.

reply

solaire_oa
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

It's lame, but a todo list app: jatabag.com

It's tailored toward implementing a web version of the original cli app and whitepaper "grit"https://github.com/climech/gritSo basically it creates a DAG and each task node can receive some annotated data (traits) about whether the task is actionable or not.I've been using it daily for a year or so. Slight bummer that I feel I released it 5 years overdue, though, and it's doomed to drown in noise.

reply

andrewjk
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

- I've built a memory-safe, ownership-based, auto-freeing programming language (
https://github.com/andrewjk/nomen
) and am starting to use it here and there. It still has a few holes to plug!

- I've also been working on my full-stack JS framework (https://github.com/andrewjk/torpor) which is now faster, has more built-in components, and has single file code routing which can be migrated to full file routing when your site gets bigger- Both started by a human but now mostly implemented by robots

reply

R1shy
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building Buffalo, a text based social media with no UI, and no algorithm meaning you can view posts how ever you want and filter them by tags, if you want to view it through a website you can make one, if you want to view it through a TUI you can make one. 
you can join the waitlist at 
https://waitlist.buffalo.sh

reply

BorisMelnik
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

you are definitely thinking ahead. I really think the way things are going now users are going to demand to be able to consume their data the way they want to.

reply

daaysjavu
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

For my fellow ravers: 
https://fourierx.ai

I made a tiny ML model (~2.4 mil parameters) that can mix music in a never-ending continuous stream where transitions between tracks are 20-60+ seconds long.It's currently just streaming from my own personal music collection that I have bought over the years, which is primarily DnB so it's pretty niche at the moment.I've been working on this on and off for the past few years to learn more about machine learning and other technologies that I was interested in.It uses HTTP3 WebTransport on Chrome, but falls back to WebSocket for the other browsers.If anybody likes listening to music this way, I'd love to hear your thoughts on this.

reply

panphora
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a way to make some pretty advanced software in a single HTML file.

The idea is simple: store state you'd normally store in a separate database in the document itself.Then, also give the the document a bunch of powerful APIs granted to it by its host:(1) Sync changes to the document with live collaborators(2) Extract data from the document using a simple JSON map config(3) Boot up a full content CMS from the same simple JSON map config(4) More features added every monthI'm really excited with even the tiny bit of early traction I've gotten. About a dozen paying users so far.Long term, I'd love to have this file type (vanilla HTML file + some extra features granted by the host) become a file type other companies offer tools and their own hosting for (like Wordpress).Hosted platform:https://hyperclay.comNative offline apps (source available, almost MIT license):-https://htmlclay.com-https://hyperclaylocal.com

reply

rmorlok
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on AuthProxy, an open source embedded integration-platform-as-a-service. It has an embedded connector marketplace that lets you connect to 3rd party systems, then provides a proxy that handles the credentials automatically. Been working on it for a couple of years and in the last month or so have been trying it out to build an MCP gateway for some internal tooling.

https://github.com/rmorlok/authproxy

reply

FailMore
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m very interested in building tools for coding agents (where I spend a lot of my time).

I’ve been buildinghttps://smalldocs.org, it’s a simply styled, but functionally deep, artifact layer for agents. It’s open source and free to use.Because it can incorporate charts, diagrams, spreadsheets, etc. in one artifact, it’s good for creating (and optionally sharing) agent created analysis.It has a local library for all your Markdown files, and a cloud library (my one paid feature) too. Both support tagging and rich search/filtering. I find it turns SmallDoc artifacts into little checkpoints in work I can easily circle back to.Thanks for reading!

reply

thiagoperes
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I built a simple, stoic and free markdown note app (free) called Beauty. 
https://www.markdown.beauty/

Why? There's no why. The world doesn't need another Markdown editor. I still made one.Everything is on-device, purposefully human-centric without being anti-AI. I built this because I wanted to work on a project that I could sweat the details unconstrained by deadlines, investors, etc.I was frustrated with other writing experiences, and like most I gravitated to Apple Notes due to simplicity, but I still missed so many things. As someone that's spent the last 2 years immersed in Cursor, Codex and CC, I wished some of their input behaviors existed in a regular text editor.For example, you can use / to add styles, or : to add emojis, shortcuts like < 3 for a heart, - > for an arrow, and so on. It honestly feels great.Is it radically different than other editors? I don't think so. But I think it's well executed across every dimension possible.Maybe one different thing: multiplayer. It's live editing like google docs, but P2P using WebRTC and strong cryptography. The limitation here is that you can only share a file while having it open yourself.Great care was taken to performance and portability. This is one of the areas where I spent a ridiculous amount of time simply because I enjoyed pushing the limits of the stack. While using you will notice that rendering, GPU, RAM and bundle sizes were heavily optimized. The Mac app is < 50mb.Very soon, I'll launch an iOS version with iCloud sync. In the future, I might launch basic AI features. If you miss a great text editor in your life, give it a try.

reply

djeastm
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

A very simple open-source browser extension called Karaoke Pitch that lets you adjust the pitch of a YouTube video and optionally store that chosen pitch for later.

https://github.com/djeastm/karaoke-pitchFirefox:https://addons.mozilla.org/en-US/firefox/addon/karaoke-pitch...Chrome:https://chromewebstore.google.com/detail/karaoke-pitch/facck...The Firefox one has 12 average daily users already, so that makes it my most successful side project ever haha.

reply

cmlars
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on OttoCAM (
http://ottocam.com
) - a Mac/Windows CAM app that aims to make CAM for makers/diy/hobby folks as easy as slicing for a 3d printer.

I wanted something that I could load in a step file, push a button and have the CAM just “happen” (while still having overrides and custom controls).I build combat robots and am a Mac user. I was frustrated at the limited CAM options (fusion 360 is bulky, crashy, slow. kirimoto and many others only do STL files and don’t have adaptive tool paths).I’ve been working on OttoCAM for the last 8 months. It’s free while in beta, and when it does go paid will be a single affordable purchase (like Lightburn).

reply

jmkahn
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Looks awesome

reply

llmsolutions
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a natural language intelligence layer for contacts - "Pull everyone I know who works at a Series A healthtech in the Bay Area who also went to Stanford for ungrad" => either structured or unstructured results. Large-scale data support, automatically enriched with up-to-date data, fast/accurate results. Integrates natively with Gmail and Gcal.

Looking to pilot forfreewith smallqualifiedteams (early-stage startups with real/immediate need).hello@llmsolutions.ai

reply

kidnoodle
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve carried on working on my llm powered book recommendation engine, Leafle (try it out if you like! 
https://leafle.nanosheep.net
).

Mostly this week I’ve been wrestling with a better solution to filtering openrouter providers because a common failure mode is getting stuck on one which is either very slow, or doesn’t actually meet the spec it promises in terms of tool calling.

reply

profsummergig
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

I like seeing Serif fonts on the screen for some reason.

reply

kidnoodle
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Love a serif (but then I miss writing my docs in latex so..)

reply

jakevoytko
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I built my own personal Google Docs clone to use as the editor for my blog

I used to work on the Google Docs team, so I basically did an 8-hour Q/A with Sol spanning like 400 questions. Did my best to reach back 10 years into my memories to see how things were implemented, and discussing architecture and tradeoffs. Then went through 5 ChatGPT resets implementing it on Astra to get a feel for the model.I have a long way to go. But I'm writing my first post on it this week, and then I'll do a writeup of the editor project.

reply

thread123
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/ChrystianSchutz/ThreadShelf

I had a lot of chats in OpenRouter, google AI Studio and lm studio and no good way to view/search/combine them together. ThreadShelf started as a local archive with semantic search/MCP, and later grew support for continuing conversations through llama.cpp or OpenRouter. It is my first time creating oss so please be gentle.

reply

gutta-percha
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

A modern web app for the Analytic Hierarchy Process (AHP), which is a structured decision making framework. The AHP models a decision by organising it into a goal, criteria, and alternatives. Pairwise comparisons are used to assign weights to the criteria, and subsequently the alternatives, producing a ranking of the alternatives by preference.

https://decisionpoint.io

reply

tomjuggler
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

ChonkyBlox: A new approach to Block based coding - instead of complicated algorithms to derive the code from block programs I am using AI on the back-end, which actually makes a higher level of abstraction possible with the blocks. Each block has an LLM instruction attached, along with rules defined in the bespoke back-end harness.

Also: kids can code using cardboard cut-out blocks and just take a photo to import, generate Arduino firmware, compile and flash to ESP32 - all from a single docker web application.Hoping to bootstrap a cheaper, open source alternative to current systems (one of which my son is using at his school). I have had success doing this with another project on Patreon so that's where it is going to be launched.https://www.patreon.com/ChonkyBlox- so far just a couple of demo video's but code will be released in full once I have added more blocks and a tutorial.Ultimately this is aimed at the South African education sector, where many schools may have only one computer available for a classroom to share, hence the cardboard cut-outs. There is also a hardware component still in development - a simple pcb breadboard break-out with connectors for components instead of kids having to use jumper cables on the breadboared. We also have a working Desktop application which does code assistance from within the Arduino IDE - using the same web server with api, so literally everything from very small kids to advanced is covered.

reply

kulvind3r
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A gameplay time tracker for PC and emulated games on windows I wrote to track my personal gaming hobby.

https://github.com/kulvind3r/GamingGaidenCreated this to replace the original Gameplay Time Tracker which was closed source and abandoned. Been improving and maintaining it for 3+ years now and it has found moderate audience in it's niche.

reply

martz
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Working mostly on video, local AI, and developer tools.

I maintain LibVLCSharp (https://github.com/videolan/libvlcsharp) and work on VLC for Unity (https://videolabs.io/store/unity). Lately I've been building VLCLR, which lets you write native VLC plugins in C#, and experimenting with local AI for real-time video analysis.Also working on Kyber for Unity (https://gitlab.com/mfkl/kyber-unity), bringing low-latency video and robotics tooling into Unity.

reply

vlad_ungureanu
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

MomentFrame, an iOS app that turns your photos into Polaroid-style prints, with the location and date/time filled in automatically from the photo's metadata.

I started it as a quick proof of concept while my wife was in labour with our first child, partly to cope with the stress, partly I wanted to create a personal gift - tracking our journey together. So I needed, a simple way to caption the important moments of our life together with the when & where.The goal was simple and fast, with everything on the device: no account, no tracking, no uploads. You can edit the captions and adjust the crop, then export or share. The first 5 photos are free, then a one-time $1.99 unlocks unlimited exports.App Store link:https://apps.apple.com/app/id6753585464Side note: This side project was also a second experiment: how far can LLM coding agents get on their own? I wrote the first version in Swift, then had Claude Code port it to Flutter. It did most of the work (rendering, geocoding, the in-app purchase flow, even driving the simulator to check its own screenshots). I think Opus 4.8 was the point when the agent become truly autonomous and my input became less needed.

reply

neverartful
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a cross-platform GUI system called Affiche.

The basic idea is to separate an application's UI semantics from the toolkit that actually renders it. The same application can currently be presented using native Win32, Cocoa/AppKit, Qt6, GTK3, GTK4, Swing, or a web browser. The UI can run locally or be rendered remotely by a client, without the application itself being rewritten for that environment.I've also been working on a declarative layout format and, lately, a visual designer.It started as a rewrite of an architecture I worked on many years ago, mostly because I wanted to see how far the idea could be pushed with modern systems. It has turned into a considerably larger project than I expected.Still private and very much under development, but I'm curious whether other people have run into the same problem: maintaining applications that need to survive changes in GUI toolkits, operating systems, deployment models, or client environments.

reply

FabCH
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

[HYBRID - Human&AI collab]

Some time ago somebody posted an extensive list of things you can do to stop bots from aggressively getting your website, if you don’t want to hide behind Cloudfare.I thought I’d make a nice UI for that:https://github.com/ivankovic/stop-botsAs the original poster said at the time: don’t use on a production server!That said, I’ve been using it on a production server for a month. It’s surprisingly efficient, and if you ban RU, US, IN and CN it’s extremely efficient.

reply

m007850
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building Eigakan Guide, a cinema showtime search site for Japan:

https://eigakanguide.jp/enI love going to the movies, but I couldn’t find an easy-to-use way to search everything currently showing in Japan. Sites such as eiga.com offer only a few filters, while individual cinema websites generally make you search one location at a time.Eigakan Guide lets you filter showtimes by area, cinema, date, time, and features like IMAX, Dolby Cinema, 4DX, subtitled screenings, and more. For example, you can search for IMAX screenings this Friday after 7 PM.Another problem I often see people asking about is how to find screenings with English audio or English subtitles. English-subtitled screenings have their own filter. English audio is harder because cinemas rarely publish the audio language explicitly, but a Japanese-subtitled screening of a film originally made in English will generally use the original English audio.The site is available in Japanese and English and currently covers every TOHO Cinemas and Cinema Sunshine location in Japan. AEON Cinema is next, with more chains planned afterward.I launched it very recently and would really appreciate feedback, especially from people who go to cinemas in Japan.

reply

piazz
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I’ve been hacking on a single Anki extension for… the last three years now:

https://smart-notes.xyzThe idea is to make an extension that allows you to flexibly fill out fields on your cards with AI generated text, speech, and images. Think generating example sentences for your entire deck, or adding furigana to kanji (small phonetic characters with a very delicate syntax). It works just as well for language learners as it does for medical students, etc.The secondary goal has been to make this the most well designed, intuitive, and stable Anki extension in the world. I don’t think it’s there yet, but it’s on its way. It’s been very interesting to try to work out a design that affords the flexibility to generate anything for whatever you’re studying but remains approachable and discoverable to your marginal Anki user, many of whom are younger and have varying levels of English ability. Many interesting technical challenges as well.Slowly building towards the Show HN post, but need a few more features. Connecting with and chatting with dedicated users in countries around the world over the last few years has made this the most gratifying thing I’ve ever built! It’s still at the scale that receiving support emails is fun and I can build relationships with power users and long term subscribers.

reply

nickreffitt
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Fluir, a web app that improves Spanish speaking beyond A2

https://getfluir.app

I hit a plateau with my learning, having used Duolingo + tutor. It was only until I tried to read a book that I felt like I was making real progress. 
Highlighting words in Kindle, exporting them to Anki, then feeding back my progress to my tutor was fiddly and not a good use of my time. Also practicing my speaking once a day wasn't enough.So I built an app to help me. This app will: 
1. Generate Spanish short stories using Claude pitched to your level, narrated with ElevenLabs
2. Every word/phrase you highlight becomes a flashcard. Flashcards use spaced repetition - words you find difficult come up more often per review
3. Chat with Lucía - a turn based conversation who is prompted with the words/phrases you have saved downYou get a use of all the features before subscribing (1 short story, 1 round of flashcards, 1 minute with Lucía), then it's a 7 day trial.Would love to get some feedback, especially on the AI conversation, as that's the most challenging part of the app I've found so far.

reply

Koaisu
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

How do you generate stories that match the respective level? I tried generating stories in Chinese (which I would say has a large learner base as well) and it never really worked except for something like A1/A2. Also, recognizing which level a story is did not work for me.

Edit:
And a second question: do you support exporting the studies vocabulary as Anki or csv/…?

reply

gr__or
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Neat! I'm working on a similar thing but mine is not as far along, and slightly more focused on what I call "subtitled reading" (interleaving source and target language lines of text).

Small UI feedback: the WORD LOOKUP sheet has UI design disease, i.e. imo too much text. I'd drop "WORD LOOKUP" and "CURRENTLY SAVING". Also behind the latter the current word is repeated (it's already the title of the sheet), so I'd drop that too.

reply

nickreffitt
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Awesome, let me know when your ready for testers, happy to help!

Thanks for the UI feedback, will sort that today :)

reply

gr__or
 
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

* That was meant to say "AI UI design disease". I find them to default to overtexting

reply

czhu12
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been slowly working on 
https://github.com/CanineHQ/canine
 for about 2 years now. Basically a self hosted, FOSS that turns a Kubernetes cluster into something as easy to use as Heroku. Its grown to about 2000 active developers using it host small things at 
https://canine.sh

It was a pain point from a start up I cofounded before where we needed Kubernetes flexibility but developers hated using it. I figured there was no reason why it had to be hard to use and thus Canine was born.Lately been playing around with setting up remote dev containers on your own compute as well -- basically like github codespaces, except self hosted.Built in Rails + Stimulus

reply

BSTRhino
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

https://easel.games

A programming language which lets you code multiplayer games like singleplayer games. Every program written in Easel is guaranteed deterministic and snapshottable, which is how it can automatically make your game multiplayer automatically using rollback netcode.My hope is that teenagers who makes games in Scratch might like to make games in Easel because it means they can make games they can play with their friends, without having to deploy a server or learn anything about networking on synchronization. People can literally make a multiplayer game on their first day of coding.Currently been working on adding tilemaps.

reply

Madmallard
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

What I don't understand about your idea is that netcode as far as I understand is way more complex than you make it seem. The netcode for something like a MOBA or MMORPG is drastically different than the netcode for a much simpler turn-based game. They have elaborate synchronization mechanisms to make the illusion not break-down in various ways due to latency.

And then even for simple turn-based games, there has to be elaborate fully-decided like state diagrams for all the various types of disconnect and latency states so that gameplay doesn't desynch or hitch in awkward ways.

reply

BSTRhino
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, I spent quite a few years building and iterating on some quite elaborate mechanisms to handle latency too: 
https://easel.games/docs/learn/multiplayer/rollback-netcode
 - it’s taken a lot of continual playtesting to discover and address many issues.

The multiplayer architecture is rollback netcode, which I think is great because it performs client-side prediction by running your full game simulation step forward on the full game state and not some subset or stripped-down version of the simulation or state. It’s the most accurate client-side prediction model you can have.Then it achieves eventual state synchronisation by rolling back and rerunning your code when there is a prediction error. It performs automatic rubberbanding to smooth over the error corrections. All the bodies get rubberbanded, so as long as you attach your sprites to bodies (which is what you would normally do), the rubberbanding is automatic.Rollback netcode is underutilised because it’s difficult to implement on other game engines. It requires your entire codebase and all your dependencies to be deterministic and snapshotable, and so if you’re using another engine like Unity or Godot, it won’t meet these requirements because it wasn’t designed for this. Products like Photon Quantum for Unity get around this by reimplementing all the systems like physics, RNGs and even just ArrayLists in their own deterministic manner. But you have to follow all these rules about writing your code in a multiplayer safe way and there are all these traps to avoid.Putting the rollback netcode into the programming language means it always works 100% of the time and you can’t make a mistake, which means even a beginner programmer on their first day can make a multiplayer game. That was my ultimate goal and I think it is true that if someone who is an experienced programmer wants to hand-code a specialised rollback netcode implementation for their game then they might be able to do a better job on their game. But the defaults are really good when the rollback netcode is in the language itself and I’ve had teenagers make multiplayer games that they play with their whole class and they’ve all had a lot of fun, and that’s the main thing.

reply

vips7L
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building my own OAuth provider. I know there’s a lot of options out there but I’ve built one at work for the last 5 years and I’d like to “do it right”

reply

agilek
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://audioguidekit.org

It is a React-based OSS audio player I developed primarily for museums and tour guides as I am really close to this industry and i was trying to scratch my own itch. In practice, thanks to the flexible design and architecture, it can be used for any use-case where you need to deliver sequential audio. Would like to hear any feedback or connect with someone who would need a solution like this.

reply

chrka
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm currently working on the browser editor for my programming language, With the smart tab completion - which parses the entire program up to the cursor every time you press tab - you can avoid a bunch of typing and also potential errors.

You type: radius=10<enter>gc<tab><tab>50 50 r<tab><shift-enter>
And right away, you have a circle on the screen.https://easylang.online/ide/

reply

iugtmkbdfil834
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

:D Well, now that I feel fairly comfortable with codex outputs ( some corrections needed, but nothing crazy ):

- rowboat variant that is a little more tuned to what i personally need ( effectively ready - currently testing )
- simple platformer for kid - done ( was fun )
- isometric rpg ( started yesterday ) - so far results are better than anticipated, because the designed underlying system surprised me - pending
- and a whole bunch of smaller tools that come and goCodex seems to be now where Claude was not that long ago.

reply

foxtrot8672
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Pendragon. AI staffed financial advisory firm. It uses AI to measure activity across your entire financial life and help you achieve your goals.

https://pendragon.foxtrotcommunications.net/

reply

epiccoleman
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

interesting idea. I just was having Codex do some "financial advising" over the weekend, and I got some reasonable recommendations.

In the case of codex, at least, I felt some friction about just how much of my data I was willing to share, and my level of comfort meant that most of the advice was fairly generic and based on rough numbers rather than true analysis of statements, transactions, etc.If you can find a way to tell a good story around data privacy I think that might be a good method to stand apart from the pack (both in terms of competing products and in terms of "just a guy who puts his tax return into Codex").

reply

BlueHotDog2
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Frontman - like lovable but for your existing apps.
Tiqet - a local first, workspace aware task manager built for agents :)

reply

vulkoingim
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Still hacking on 
https://riffradar.org/
 and trying to make better recommendations on Spotify. Lately I've been experimenting with a couple of different recommendation algorithms, and will expose them soon as selection options for the different playlists. Signups have picked up somewhat recently and have ~800 MAU, which helps with trying out different things :)

reply

vinhnx
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building VT Code for about a year as a way to understand how coding-agent harnesses work in practice. This month I'm continuing building it 
https://github.com/vinhnx/VTCode
.

reply

einhard
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm slowly working on an aviation and flight related weather notification and NOTAM (Notice to Air Missions) parsing app.

Much of the challenge has been figuring out how to display information for pilots. The global NOTAM system is broken and works on the basis of legal liability, wherein NOTAMs are published to comply with requirements, and pilots are required to know all relevant information but important things get lost in the noise.For example, my home airport has a runway closed. It is a single notice, but unless you carefully read 100 notices (many of which are about cranes and unlit objects in the general vicinity) you might not see it. I'm trying to make it such that no information is ever hidden, but with some sort of mechanism to surface more important things.

reply

aaasen
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building an expedition weather app that works via satellite messengers like Garmin inReach, ZOLEO, and iPhone satellite messaging.

It has been really interesting trying to fit a detailed weather forecast into about 1,000 bits. I'm using an rANS entropy coder fitted on historical weather forecasts. I'm able to fit about 100 time periods (~4 days of hourly data) into a 160 character message, using just a couple bits per variable on average.Github:https://github.com/aaasen/goingblueSite:https://going.blue

reply

robowo
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

https://stagewatch.de/

Basically a simple pizza status tracker for small German fabricators and craftsman. You define the process, instantiate it per customer order who receives the link to a status page with a possibility to subscribe to status notifications as well. The benefit is that people don't call you anymore asking for the status of their order, saving time.It's a pretty vanilla rails app running on a hetzner vps.

reply

zkmon
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Nice idea. How does the provider receive the order from customer? Is it through phone call, or via some other app? If it is an app, won't that app have a status tracking feature?

reply

robowo
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The assumption is that there is no app. The target is mostly small businesses who receive the order via phone or face to face.

reply

torsi0n
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/t0rsion/leone

Working on my local LLM runtime Leone. It has a CPU path that verifies the CUDA kernels.

reply

asim
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Micro - a personal AI agent - 
https://micro.mu

Still iterating. Started with something else, then turned that into tools, then turns that into agents, then turned that into an assistant. Now trying to make it generally useful, quite painful at times... but want something that is not Muse or ChatGPT or Claude or Gemini... and not Hermes or OpenClaw. Currently just fixing all the broken styling/css, etc, no separate frontend, single Go binary.Self host if you like -https://github.com/micro/mu

reply

itomato
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on PCB generation projects with MCPs, mostly with KiCAD because of the ROI.

- Flexible rp2040-based instrument tuner- Stratocaster-style PCB art pickguards- NeXTBus experimentation board (not that I'll ever use it, but I'll be darned if I don't understand the nuances between NeXT and Apple's NuBUS implementations better now)This extends to firmware and emulation projects like Doom and the Quake trilogy running in Jira Cloud (https://marketplace.atlassian.com/apps/3372062249/doom-for-j...) and a fork of 86box dedicated to NeXTstep systems (i want an emulated object.station, darnit)

reply

arvida
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://localhero.ai
, on-brand automated translations for product teams. It mainly runs as a GitHub Action, translates new strings on your PRs against your glossary and style guide. This month focus went mainly on MCP and stuff around that. Thinking a PM/designer/etc who wants to bulk tweak copy without touching git or similar. Claude Desktop/ChatGPT turns out to be a pretty nice surface for this, the assistant finds every key that needs changing and organises the work, Localhero keeps it on-brand. A pretty sweet workflow. Also doubled down on Lingui and Django support.
Also been fighting some spam. A 400 from our mail service showed up in error tracking, looked like a malformed address, turned out something else. Someone setup a bunch of bots to signup and try so send crypto spam using the team invite function. Kind of persistent, I fix a few things and it tries a few others. Finally stopped, interesting to see it live like this.

On the side,https://infrabase.ai(hand-verified AI infrastructure directory) launched a Media Generation category, image and video APIs after a run of requests for it. Also the submission spam is way up here latley, been improving the detection here as well. Also seeing real interest in paid listings now, including one that started as a link-buying request I turned down :)Been doing a lot of AI assisted emailing, so I have started to work on a little review UI for AI generated text, comments on specific words, inline edits, Claude picks up both and revises in place. Like a PR review interface for text. Turns out pretty good workflow with Claude watching the files for new comments, editing and commenting back right away.

reply

montenegrohugo
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a Splitwise alternative: 
https://peanutsplit.com

Fully Open source, free forever of course.

reply

AnthonyR
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

I always wondered why Splitwise is the go-to when it's a huge pile of crap app with stupid paid features for such a simple concept.

reply

montenegrohugo
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

network effects and brand recognition :(

reply

rishi_devan
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Looks really nice. Thanks. Love that, there is no signup required.

reply

montenegrohugo
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

yeah the whole point is that it should be so easy any friends group can use it

hate apps, hate accounts, hate friction

reply

spankalee
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a new programming language for WebAssembly GC, called Zena: 
https://zena-lang.dev/

It's like a fixed up TypeScript specifically tailored for Wasm GC that can produce very small and fast binaries, but also has features like pattern matching, ownership / borrow checking for resources, pipeline, tail call elimination, multi-value returns, direct WASI component integration and a lot more.

reply

NetOpWibby
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

This looks pretty cool! I love TypeScript. Although for my server-side apps, I just use Deno and compile my executable that way.

I have pondered cloning Caddy in TypeScript just because...would Zena be capable of this?

reply

hjessmith
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://doodlemate.com

DoodleMate is a multimodal storytelling canvas that exposes students to the basics of animation, character design, and story creation. Starting from paper drawings, it creates rigged versions of your characters that can talk, walk, dancing, sing, etc and you can create scenes out of it.It doesn't use any generative AI whatsoever. Just computer vision and animation algorithms.

reply

alfg
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Launched a suite of media inspection and encoding tools a few months ago, based on FFmpeg and VMAF. Slowly getting more customers.

https://video-commander.comConstantly and carefully iterating through refinement and features. It's built on Rust + Tauri with a React frontend, in case anyone is curious.I've created various open-source and commercial tools in the multimedia space over the last 10+ years and wanted to put it all together into something more premium with an IDE-like experience.Most recently I added a /playground area to experiment with the inspection tools via a WASM build, which I thought was a neat way for users to try the app before downloading the full version.Happy to answer any questions!

reply

melezhik
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

DSCI - aka -Dead simple CI - 
https://deadsimpleci.sparrowhub.io

reply

Xmd5a
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Datalog writebacks through derived columns. Any query. Any cell. And probably any datalog-based database too, it's just a client-side trick. Works well on this:

{:find [?title ?director ?rating ?card ?shout]
 :where [[?m :movie/title ?title]
 
 [?m :movie/vote-average ?rating]
 
 [(str ?rating) ?rating-str]
 [(concat ?title ": ") ?title-colon]
 [(concat ?title-colon ?rating-str) ?card]
 
 [(lower ?title) ?lowered]
 [(concat ?lowered "!!!") ?decorated]
 [(upper ?decorated) ?shout]
 
 ;; joints
 [?cr :crew/job "Director"]
 [?cr :crew/movie ?m]
 [?cr :crew/person ?p]
 [?p :person/name ?director]]}You can edit a movie's ?title and ?rating through the ?card column for instance. It supports arithmetics too (to the extent that it's logically feasible of course).

reply

mgw
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/madeinorbit/podium

A multi-harness orchestrator running agents on your VPS, with a built-in issue tracker (like Linear) and gas town like communication system.Agents can split up big tasks themselves into subtasks, run each with a different harness and model and communicate so they keep running for days until everything is completed and integrated.There's lots of tools in this space, but our combination of agent-focused issue tracker and agent-to-agent communication is quite unique and, for our use case, delivers an actually working software factory.It's still a little rough around the edges but we'd be super happy for people to see if they get the same benefits out of it that we do. It's free and open-source.

reply

afiodorov
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Queryable climate data for major cities. The main question I'm trying to answer is: where can I maximize the number of comfortable hours I can spend outdoors, whether doing light activity or just sitting around?

DeepSeek can query a processed climate dataset directly, and other agents can use the same interface:https://climate.fiodorov.es---See also:https://hn.fiodorov.esfor RAG search across Hacker News comments

reply

_madmax_
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

How are you using deepseek to keep your cost low when your traffic explodes ?

reply

afiodorov
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

So far really wasn't an issue - I put $5 there and forgot about it. If traffic explodes will probably offer bring your own key or add credits/ads. Also just providing MCP for your agent to use is an option.

reply

ToriTech
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on anti age verification/surveillance projects lately. I put together this thing I call The Mandating Honeypots Project and it shows how anyone with an internet connection and copy + paste skills can trick Linux D-Buses with a simple Python script, proving that if companies want to verify your age by asking the D-Bus interface, it's easy to just tell it to always send 18+, making the whole thing useless. The only reason you'd want ID verification is so you can create the world's biggest and sweetest honeypot.

(https://github.com/Tori-Tech/Mandating-Honeypots-Project)In that project, I also proposed a tool with heavily redundant password protection that parents could use to keep kids from tampering with the service so the government can stop saying that this is for the kids. I'm planning on doing a mobile device version and/or an ID database focused version, but that's still in the planning phase.I also want to do a Windows version when they release their 'GetUserAgeRangeAsync' API, but idk if I'll be able to. Windows is always a pain to work with.It'd be nice if someone had advice or ideas to share, too.

reply

properbrew
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Still working away on the same thing - 
https://whistle-enterprise.com

Latest updates around audio processing and quality are out, I've also made a substantial addition by implementing extensions.This allows people to hook up to M365 or Google to get desktop notifications to start the recording, it can also export to share point and stop the recording at the registered meeting end.Was a fun process keeping the offline and online functionality completely separate, also getting validated by Microsoft for the M365 extension was a bit of a chore, but finally have the verified blue tick.https://getsoftwarehouse.com- I'm also working on the governance layer for AI tooling that is being built by employees, there's just HTML files flying all over the place, no security, no home. So built software house as a place for these things to live, be secured, put OIDC in front etc. It's fun!

reply

jimle_uk
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Relaunched 
https://ragextract.com
 over the past month - from document processing and RAG API to fully featured AI table/datagrid.

The idea isn't new but I felt enough time had passed that document-first AI tables shouldn't need be gated behind a few big names, a sales meeting or another subscription. Ragextract is really aiming to be the lowest-friction AI utility for everyone's toolkit.Still in active development and ideal for anyone working with a lot of documents and needs their extraction in organised rows. Particularly interested in feedback from anyone thinking of leaving Airtable this/next year.

reply

Santas
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://nonofocus.com/

I’ve always had the same problem with website blockers: I might need YouTube for a tutorial related to what I’m working on, but allowing YouTube also means allowing every unrelated video. Same with Hacker News - I might need to look something up for work, but I shouldn’t end up reading the front page for the next 30 minutes.
Most blockers operate at the domain/app level, but whether something is distracting really depends on what you’re trying to do.With Nono, you describe what you intend to work on at the start of a focus session. It then uses an on-device model to look at the active window in that context. So a relevant YT video can stay open, while an unrelated video gets blocked.The tricky part right now is the model. It needs to be small and fast to run continuously, while still being capable enough to understand the context and not annoy you with false positives.

reply

saejox
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

idea has merit.

ai slop is an instant turn off for me. i would never be convinced with such low effort website.

reply

m-i-l
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I built 
https://vintagepresents.com/
 to try to sell my childhood comic and coin collections.

I believe it is the first eCommerce platform where all the products have date as an important feature and where the search and navigation are by date - the thinking being it could help people find interesting and original birthday presents and anniversary gifts. I've also built it as a multi-vendor platform so it can hopefully live on once I've sold my things. Note that I'm the only seller and it is all UK based at the moment, but it has just been launched.I've a blog post with more info athttps://michael-lewis.com/posts/vintagepresents.com-date-bas...if anyone is interested.

reply

lvduan
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I built this sql formatter <
https://sql.leuduan.work
> for my own use - it works by parsing the SQL query to AST using native engines where possible (for BigQuery it use GoogleSQL library, for MSSQL it uses Microsoft ScriptDOM, the rest uses Apache Data Fusion Parser) and from the AST it re-generates the SQL query in a consistent formatted style. You can throw in all kind of badly formatted SQL queries and it will work just fine. Hope you find it useful!

reply

fypanto
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/pantoniou/fyai

I'm working on fyai, a rather opinionated agent harness, built to work as a unix tool and the idea that eventually AI is going to be a commodity, where having control of your own data is what's important.It is still quite alpha, but at a usable state.The biggest technical difference between fyai and other harnesses is that in fyai the state is durable and stored in a disk deduplicated arena, which means that git like branching is free and storage requirements are very modest compared to JSONL/SQLite storage.Latest additions has been full markdown/mermaid rendering support and (very alpha) Claude code and Codex session import.

reply

ludovicianul
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a words game: 
https://hilogame.cc
 and planning to release 2-3 more that, if they get traction, will live under a single umbrella in the future.

Additionally, I'm building a REST API fuzzer:https://github.com/Endava/cats

reply

abejora
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.abejora.com
 - timesheet software for freelancers and small teams

We created it as an alternative to the price gouging that happened over the last year at various timesheet SaaS companies. The idea is that good software should not cost 10x as much just because 10x as many people use it. In our opinion, software should also be functionally complete. There should be no arbitrary tiers that only exist to force people into more expensive plans.The stack is Elixir with Phoenix LiveView, deployed on a Talos Kubernetes cluster. This is different from what we normally build on, and honestly quite fun.Lately we have been thinking hard about the temporal nature of timesheet software. Many things get quite complicated once you factor in historical versions: the need to retire, lock, change, reopen records or rates, and so on. We have been working hard to polish Abejora to make everything accessible, user friendly, and intuitive.

reply

alphaBetaGamma
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

https://studio-galois.com/

My wife and I are working on a math/science/CS-inspired jewelry: pieces that stand on their own aesthetically but have a hidden meaning.We currently have two styles: lambda calculus based pieces (we depict the Tromp diagram) where we have Y-Combinator earrings (well, strictly speaking they are one beta reduction away from Y-combinator. Aesthetic oblige) and a pendant depicting a lambda expression computing Graham's number. The other style is quantum computing circuits, based on quantum computing research my brother (a physics professor) is doing: a pendant that is actually a non-local controlled-NOT gate.I wrote a tiny DSL to describe the jewelry pieces, and an interpreter to produce CAD files. We then either 3D print them or have them produced by lost-wax.We have our pieces in consignent in a jewelry store, and are working to put them in a museum store.Marketing is the hardest part. Ideas are welcome.

reply

jerkstate
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

I love these! I recently designed a few decks of playing cards of mathematicians for my dad as a gift, my favorite part was designing the backs: a zeta function for the pure-maths deck, a Moore curve for the computation one, and two interfering waves for the physics one.

Actually, I can share the link if anyone is interested (because this is the "what have you been working on" thread and this has been one of my more fun projects):https://www.thegamecrafter.com/games/mathematical-minds-thre...Same thought on marketing - where to advertise where people would appreciate this kind of thing?

reply

eric_khun
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Got lot of traction on a multiplayer web game pong [1].

Now working on releasing on steam, android, ios. Also made an ssh version you can access via your terminal [2]. Hoping could get as many downloads in native platforms.[1]https://antics.gg/p/side-out-94df7d[2]https://antics.gg/ssh

reply

Jeremy1026
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Been working on a replacement for my Git GUI of choice, Tower, for the last few months. I've been using Tower 2 for almost a decade now, refusing the monthly subscription to upgrade to a fresher version. I'm going to keep mine a one time purchase with support guaranteed for a year. If a major version releases after that, it'll be another perpetual license for the new version. If you want the new features, you can choose to upgrade, if you don't stay on the version you're on until new feature warrant it.

https://www.harborgit.com/

reply

bigwindow1
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

https://shotbrief.app/

ShotBrief answers whether tomorrow is worth going out at your shoot location, weather, sunrise and sunset, moon phase, aurora where it applies, and a go/no-go score for the whole day.Because I like going out early for photography, but I also like sleeping in, so this just tells me if it's worth it waking up early.

reply

vinzenzu
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Asset management using automated and AI-driven trading for portfolio diversification and higher returns.

Trading Results as a service.Our philosophy is Capital protection first, so we focus on protecting capital and managing risk while trading, and avoiding large losses enables compounding and high returns in the long run.Infused with my co-founder's three decades of experience in trading & finance.We don't want all your money. We want to be part of your diversified portfolio, which should also consist of other things like index funds, bonds, etc.Initial allocations will open within the near-term future.
For the founding investors (as we call the first clients), we also offer a portfolio review to align your portfolio with your long-term goals, a direct line to founders, and other things.https://autotradelab.com/

reply

KellyCriterion
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

If your co-founder has 30 years of experience, why isnt he superrich already? :-))

reply

iterance
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What decisions does your AI have the capability of making? Buy/sell stocks, bonds, options, margin, short, crypto, etc.?

reply

iqbal1980
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Been working on Ezducate.ai a special education ai powered platform

reply

bryanhogan
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a self-tracking app and an Astro Web Starter Template! :)

The app is very customizable, local-first and is built to adapt to what you want. Goal is to combine habit tracking, health logging and journaling into one fast and easy to use interfact.Have been working on it for almost years now and it's making great progress.Doing closed user testing right now and will release an open beta soon:https://dailyselftrack.com/My Astro Web Starter is built for building well-designed, performant and accessible websites. It contains everything a high-quality website needs (In my opinion). I built it so I have one good base on which to start my web projects on. Using basic HTML and CSS that can scale, without bloat.There's a lot more on it which you can see here:https://starter.bryanhogan.com/

reply

jason_zig
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on Zigpoll[0] for ~4 years. AI has changed my trajectory dramatically where it's way more realistic to compete with the big players as a one man show. Trying to close out on 2M ARR this year and then maybe look to sell and ride off into the sunset.

[0]https://www.zigpoll.com

reply

peab
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Fabling.app

Got tired of trying to learn Spanish with Duolingo.This uses the parts of AI that can actually help one learn efficiently, namely:
- generate stories that are slightly beyond your understanding (i+1) - i.e mostly words you know or are learning, and a few new words
- tracks your vocab and how often you lookup définitions
- auto generates a vocab review deck (using fsfr Anki style)

reply

tasoeur
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://sxp.studio/subjectivezero

My summer project was to challenge existing 2D / 3D visual effect creation tools (touch designer, comfyUI, etc.) with something agentic as the true foundation (not just slapping MCP on top of an existing paradigm).It also came from the following observations:- people are making their own coding harness, why not one for realtime visual effects?- using Claude code or codex to make art and installations is absolutely fantastic, but you usually end up with a lot of friction and paper cuts when it comes to deterministic workflows and concept iteration.SubjectiveZero is the free and open source project that resulted from it. 
It’s still following the classic node editor paradigms but making the nodes absolutely more malleable while also combining a user experience flow optimized for ideation and iteration. I definitely invite you to check out the showcase and examples on the website, but basically it feels kind of magical when your editor just “get” what you want, and nudge your exploration into adding more little knobs here and there so using the tool feels more like playing rather than “operating”.I also liked the emerging concept of an adjustable abstraction ladder, meaning people who are very technical can still get as much granular control as they wish to while people who just want high level concepts and vibes can just use prompts to try things out.When it comes to determinism, the tool has some neat features like an agent graph to constrain agent workflows, overpowers MCP that drives user interface changes as the agent makes progress, allows the agents to verify their work and coordinate so the usual painful wait for agents to be done is somewhat minimized. There’s also a way to do basic model routing to tweak your intelligence/speed ratio.I’ve personally used it to make art and fun experiments. Feel free to send feedback or contribute tokens to the project if the concept speak to you!

reply

tomaytotomato
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I am doing lots of different projects now

- Making a nostalgic remake of Rainbow Six Rogue Spear - called "Tango Down"Its low poly, Java OpenGL game but trying to stay faithful to the old gameplay- Updating my homelab setup to be much tidier, moving stuff to Ansible, dockerising non-critical services. Running scheduled backups to a separate NAS- Making a World in Conflict SFX mod for Warno, so it sounds much betterhttps://www.youtube.com/watch?v=nudm7JKY6gI

reply

triwats
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Still plugging away on 
https://flopper.io

Added models and pricing there recently too. Aiming to be a huge place for all GPU data when it comes to mathematical performance. Things like FP8 for AI inference etc.Tempted to make the infrastructure a bit more sound.Aside from that I'm working onhttps://solarable.org- which is aiming to provider understanding of solar panels before finding an installer and plotholes.app (https://plotholes.app) which is a consensus network for potholes as reported and determined by cyclists.

reply

allenu
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a Zettelkasten notes app that focuses on getting the UX details right. It takes aspects of Notational Velocity, outliner apps, Zettelkasten, and wikis and combines them into an opinionated Mac app.

What makes the app a little different from others is that it's kind of halfway between an outliner and a wiki. You can place notes in a tree hierarchy, but they can be free-floating as well. You can link to other notes using wiki-style text links, and each note has a unique address, so you don't need to give notes a title or a filename.Notes can even appear as a child note of more than one parent. The idea is that you can jot down an idea quickly without a lot of friction and then later either add sub-notes to create a note "tree" from it or add it to an existing tree. The tree gives structure to related notes, but the wiki-style links allow you to connect notes together outside of that structure. (I consider the tree structure a "hard" relationship and the links a "soft" one.)There isn't a single uber-tree where every note goes. Your notebook ends up with lots of free-floating notes and lots of small trees of organized notes, like a card-based Zettelkasten system. You can use search and various filters to find and stumble upon notes easily.Notes can either be stored in iCloud (so that they sync across devices) or saved in a folder as simple Markdown files.If you're curious, you can help beta test it. More info here:https://zettelkasten.ussherpress.com/

reply

gtadesktop1
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a own x86_64 UEFI Operating System (OS). The idea is to make an OS that looks like Windows Vista but behave like Linux, so it's a mix of Windows and Linux. I've startet three weeks ago with a custom bootloader and the legacy bios VGA textbuffer and now I'm working on a real USB-HID (USB-Human Interface Device) and have troubles with the keyboard. I also have problems with booting from real hardware. If anyone is good at low level developing the project is source available and I appreciate collaborations with other os developers. Link to Codeberg-repo: 
https://codeberg.org/vntx-labs/VeloOS

Hope that is no problem that I use this thread a bit for self-promotion. If so just write a reply I'll remove this comment if this is a problem

reply

zeldahessler
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a chat app for small groups as an alternative to chat apps focused on large, low-trust groups. I think people focus on "scaling" too much. I want to make software for groups no larger than Dunbar's number.

Anyhow it's basically just twitter but as a chat app. Everything is tag-based and there are no channels. Instead, users create and share lenses, which are just saved searches. That way, you can "speak in multiple channels" at once, or carefully filter out specific people or topics.The best part is that I can speak, and then organize after the fact.https://pipoca.chat

reply

baalimago
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://xn--sakfrga-ixa.se

An agentic system which scans a whole countries political decisions. Wrote a blogpost about it here:https://lorentz.app/blog-item.html?id=scanning-swedenReusable on any country's political system as long as they have legal mandates to keep political documents public (most of EU). Still a long way to go, but pretty in a pretty decent shape already. Wrote it for the Swedish election, but didn't get far enough for it to have an impact.Will continue with for Finnish elections 2027 (on new domain).

reply

mrdlads
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

https://platemath.mrdlads.com

TLDR power user work out tracker, all PRs, metrics, fast keypad input or codemirror syntax input if you're lazy type that jots in notepad. Generate any exercise based on movement + modifer system. Mountan of metrics (your basic lifitng stuff), rolling averages etc. Fractional set tracking, bodypart volume... too much to list. Build and import programs using syntax.Lazy overview while I work on docs.https://imgur.com/a/when-you-cant-pr-platemath-rPNmxKgLooking for users to stress test at some point, but feel free to play around.

reply

and-not-drew
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Posted this before, but Odds Assist Pro (
http://pro.oddsassist.com/
) and Sportsbook API (
https://sportsbookapi.com/
)

The Odds Assist tool started out as a way for me to quickly QA the data from the API. It then turned into its own product as an odds scanner and sports book advantage finder (mainly arbitrage, +EV, middles, etc). Over the past few months it's really pivoted toward prediction markets and collecting and displaying data to get an edge on markets that are soft.The pivot to focus on PMs has been pretty fun from a development perspective since there's so many niche markets to look explore. I've always liked math, I'm a bit of a digital hoarder, and I've got ADHD so finding random things to collect a bunch of data for just to test a hypothesis just hits my brain in all the right ways. It's also given me an excuse to learn more about ML what has been great.

reply

getravi
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Started a few different things:

1. A robotics information and news website. Any feedback is appreciated.https://robotica.dev/2. Applied DBSP theory to Postgreshttps://github.com/getravi/pg_dbspand DuckDBhttps://github.com/getravi/duckDBSP. The idea is to have incrementally maintained materialized views.

reply

officialchicken
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

I've been looking for a site like robotica.dev that pulls together news and events from multiple sources. The funding page is awesome and unexpected, a really useful mini-crunchbase for robotics.

reply

getravi
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you. Crunchbase is definitely one of the inspirations.

reply

zytoon
 
18 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Whats your stack, workflow for the news site?

reply

getravi
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Currently its a astroJS site with a backend script that runs periodically and updates the website.

reply

piker
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

https://tritium.legal

Tritium - the legal IDE for desktop and web.We're building the document viewing and editing layer for a number of AI native law firm startups.Web preview:https://tritium.legal/previewWASM example:https://tritium.legal/wasmWe actually offer source access here, too:https://tritium.legal/source

reply

aleda145
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I open sourced kavla, the SQL canvas I'm working on: 
https://github.com/aleda145/kavla

README is very bare bones, needs a video or a picture too. The website should tell you some more things:https://kavla.dev(and now the demo does not require a login (also need to remake the demo to fit the new self hosted version))It's still lacking an analytics agent for the local version though. I've explored using codex CLI, but it feels like its extensive system prompt cripples the agent a lot vs Kimi 2.7 that I've been using in the cloud version.I think it would also be nice to lean into the fully local LLM setup too, especially for data that shouldn't leave the device.

reply

RobinL
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Really like this, well done!

reply

dr_kiszonka
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It looks fun! Reminds me a bit of TLDRAW computer.

reply

druskacik
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Classical music concerts database. The interesting part maybe isn't what it is, but how it's done: I'm aiming for a fully automated database, where "crawlers" for the classical music websites are created and validated by AI.

Rough idea: get a list of urls with classical music concerts -> send each one to a coding agent to build a crawler -> validate and run on an infrastructure for "free". Classical music is an ideal use case, because the number of concerts is small enough on an average website that it doensn't require many workarounds, and the websites are usually pretty crawler-friendly.https://classicalbot.com/

reply

jll29
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Great - that's what I was looking for when I lived in London! All that existed was TimeOut mag (on paper and online, but pathetically incomplete, more for tourists).

reply

josem
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building 
https://matgoat.com/en/

A way for BJJ and martial arts academy owners to manage attendance, payments, class schedules, and student progress.I train BJJ myself and saw how much time instructors lose to admin work, so I wanted something simpler and more focused than the generic gym software out there and have been having a lot of fun building it with feedback from real academies.

reply

Cider9986
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Should I try BJJ?

reply

gusco
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

https://intestinate.com/gusco/

TUI file manager with Bitwarden/SFTP/S3 support written in go.Runs pretty much anywhere.Current feature in the works is built-in audio player.As someone who still likes to purchase and organize music in files and directories, I couldn't resist the itch to code a worthy competitor to Cubic Player :)

reply

dainiusse
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Sauna Assistant (
https://sauna-assistant.com
) - sauna rituals, automation, maintenance journal and more

reply

gcanyon
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

About fifteen years ago a puzzle game called Trainyard came out for iOS and took my dev team by storm for a few weeks. It ceased getting updates some years ago and isn't on the app store anymore. So I came up with a variant on it and just put up 
https://www.geoffcanyon.com/lightyard.html
 I need more puzzles to include in the base pack, if you come up with something interesting, export it and send it to me!

reply

chasebank
 
18 hours ago
 
 | 
parent
 | 
next
 
[–]

trainyard is/was an amazing game.

reply

gcanyon
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Agreed!

Despite the fact that trainyard has been defunct for ~8 years, I didn't want to simply clone it.I tried to give a similar, but not the same, experience -- I'd be very curious to know how close you think I came.

reply

zxdc7896
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Hey everyone!

Last year, Mozilla released Orbit, an AI-powered browser summarizer hosted on a GCP server. After people started digging into the extension, they discovered things like backend endpoints such as store_result. Eventually, Mozilla discontinued the project.
For the past month, I’ve been trying to rebuild Orbit from scratch, but with one major difference: Apogee is fully local and privacy-focused. Apogee doesn’t send or store your data. It can directly connect to your local Ollama instance for inference. I’ve also added WebGPU integration for Chrome and Transformers.js for Firefox to provide faster, local responses.It can summarize: Articles and websites, YouTube and Billie videos, Wikipedia articles, Hacker News and Reddit threads.You can check out the source code here:https://github.com/darshi1337/apogeeInstall Apogee:Chrome:https://chromewebstore.google.com/detail/apogee/pgemlpomhkdc...Firefox:https://addons.mozilla.org/en-US/firefox/addon/apogeeext/Obviously it is far from complete. Would love to hear your feedback and suggestions!

reply

jazzprogramming
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on vorfract, a Voronoi voxel world which uses Voronoi cells as voxels instead of the regular cubic ones.

It's an early version so many (if not most) things that would be in a game are still missing at the moment (though planned on paper).One interesting thing is that because the Voronoi voxels are so malleable, things like round or hollow worlds are a pretty natural outcome.In parallel to working on it, I've been mostly using it to build and improve my own voxel castle with a pointy roof, slanted walls, custom built stairs, tables, chairs and all those nice things.In the last update I added a CRT filter and some pixelation options as I find that appealing. As for the future (maybe as the next thing?), I guess I'd probably like to add the ability to build less blocky things like round towers (or flower vases!), but that is still very much a work in progress.The Web version (WebGL) is completely free (and will stay that way):https://jazzprogramming.itch.io/vorfract

reply

furyofantares
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I got sick of stuff like Solitaire and Hearts and other standard playing card games requiring subscriptions or coming with ads etc in 2026 - that stuff came with your computer in my youth and got enshittified. Mainly I hate seeing my family playing all this pesterware.

So I'm making one app that has all the games I can think of without any of that crap.https://suddenlycards.comIt has online play which is P2P with a very simple service for connecting players to each other. It also has bot play, with a mix of heuristic-based bots for some games, and bots with small neural nets (of various approaches) for others, depending on what has worked best for each game.I'm also working on my own game framework for vibing games (which the above is authored in). I have about a dozen prototypes going, and I've fully ported Spectromancer (a game I own the rights to) to it.https://nanogame.app/spectromancer

reply

Arubis
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I've been working on building hyper-local services, sort of as a love letter to my community in Denver, Colorado. Before decent LLM harnesses, these would've been prohibitively expensive in time and resources to build out and would never break even. Now I think I might be able to at least cover hosting costs and tokens; that's enough to keep these sustainable for my neighbors.

Broomsday:https://broomsday.comsends folks emails and SMS the night before street sweeping parking restrictions for their block(s). Email notifications are free, SMS on a paid season pass. The schedule here is block-by-block and easy to forget, so people get ticketed _a lot_ at $50 a pop. The city has an email-only notification service that's free, but it's poorly supported and the interface sucks. This is ready; I'm testing with friends and family currently before attempting real marketing.HailPass:https://hailpass.comsimilarly is a notify-before-pain service that integrates a bunch of open weather services (NWS/NOAA mostly, plus a handful of impact reporters and working on a small hail-specific ML model) to give folks on the Front Range 5-10m heads-up before damaging hail arrives at their location. Weather prediction is (not shocking) hard so I'm still tuning to get as much signal out of the noise as possible; some false alarms will be unavoidable but I want to cut them down before even a F&F release. This year's season is pretty much over with, so aiming for an April '27 release.There's a lot of ski/snowboard/winter sport culture here, but there's also existing services for those, and I'm mostly trying to offer new coverage where there isn't a good option for my neighbors. Might do an ash borer treatment/prevention service navigator yet.None of this is going to make me wealthy or famous, but building things that help the people that I actually interact with every day and that are a part of a community that supports my family feels _really_ good.

reply

joshcartme
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I've always wanted to make a video game, and over the past few months have been building one, Fairway Rogue. It's a procedurally generated, deck-building, mini-golf roguelite. It's been a lot of fun, and I've learned a lot.

I remember someone saying that when you build a game, you end up building tools to help you build the game. I never really got that, but now I do. I've spent quite a bit of time working on tools to help me balance the various game mechanics.One weird learning, it was much easier to get it on the iOS app store, than the Google Play store. Google wants you to have a closed playtest with at least 12 players, for 14 days. I did that and they said the testers weren't engaged enough.If you want to check it out on iOShttps://apps.apple.com/us/app/fairway-rogue/id6783598189, I'm still trying to get it on Android

reply

hassansayed2002
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building my own framework it started as research project then it became a real product

https://devorajs-docs-docs.vercel.apphttps://github.com/hassanalsa3aka/devora.js

reply

jacobgold
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on Clor, an agent multiplexer for Claude and Codex with shared memory. It's free on your own machines.

The idea is to help developers multiplex agent sessions and run Claude and Codex together, which ismuchmore powerful than running one or the other alone.My secret goal is to figure out how to make software development the kind of focused, meditative work it used to be.https://clor.comVery happy to get critical feedback from any HN'ers: jake@clor.com

reply

chrisischris
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Spore Intel - 
https://sporeintel.com/

Working on this tool to make running open-weight models on your hardware and accessing them from anywhere privately simple. Also has the option of sharing your compute with others with the built in credit system.

reply

jahala
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on an app to help my late diagnosed ADHD - through sound.

The app wraps whatever is playing on mac through device convolution (old radio, hifi system) - Room convolution (a bedroom, a forest) and adds ambience (rain, wind, waves) and Apples spatial processing - so it sounds like a real space.For me - hearing the sound in a space really helps more than just the dry sound.https://www.surraura.com/

reply

fuegoio
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I made an RSS reader with social features based on AT Proto (repost articles / star them). Trying to fix the web and the depressive social medias.

https://sunred.app/

reply

coldstartops
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://keibidrop.com

Working with remote large data sets as if they where local.I made the project public on May, and now as September has arrived, you can work with post production videos anywhere in the world. You can run the daemon on your own NAS and access the data on-demand from your working machines.The same applies to data acquisition in digital forensics flows.

reply

Benjamin_Dobell
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Still plugging away teaching kids to code and hand draw their own computer games:

https://breaka.club/blog/why-were-building-clubs-for-kidsHave been running an in-school pilot over the last school term. Has been super insightful and led to a heap of changes to optimize UX. However, the biggest challenge has been delivery in this environment.Trying to run a game in a browser on school iPads powered byreallylocked down networks has been challenging. Some school iPads will crash (out of memory) when launching the camera view, whilst others run flawlessly. We use a fork of Godot, and are constantly fighting to strike a balance between UX (increased parallelism) and browser device constraints i.e. a limit on how many web workers we can fit in memory.In addition to our main (build and play your own RPG) experience, we also stream games direct to iPad. In particular a modded version of Overcooked! 2 that teaches kids to code — Overcooked itself was never even released on iPad. We've built our own Kubernetes system that spins up (a license limited number of) games/pods on demand backed by (time sliced) NVidia GPUs. This is literally running out of my home office. Despite the complexity of building all that, the Kubernetes and GPU time slicing wasn't even the largest hurdle. Turns out UDP is a no-go on the school network, so direct WebRTC was out the window. Instead we're using Cloudflare's TURN relay with TCP. Which much to my surprise, is holding up quite well.Definitely a learning experience. However, kids are having a blast. Can't wait to roll this out further!

reply

jorelfermin
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been working on a developer first, read-only first, safety first, Cloud Cost Analyzer. I focus on analyzing cloud infra for waste. It grew out of my time at AWS and then consulting, spelunking through AWS, Azure, (GCP soon) accounts, finding real waste infrastructure. Its primary mode of operation is a rust CLI that you the developer, can run on your workstation, github action, gitlab ci, jenkins, etc and create an actionable report / test that can be used to control costs while maintaining performance and never exposing your credentials, access tokens, etc.

You would be surprised at how many over / suboptimally-provisioned dbs, idle resources, forgotten EBS snapshots, outdated / previous-gen instance types, and vestigial networking that leads to nowhere I find.If you want to check it outhttps://cca.dragonfractal.com

reply

fredwu
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://feedbun.com
 - a browser extension that decodes food labels and recipes on any website for healthy eating, with science-backed research summaries and recommendations.

Been working on Feedbun for a little while, Elixir/Phoenix stack, with bespoke LLM fleets for production workflows. Recently just started using React Native (Expo) for the companion mobile app so I can use it when I shop IRL.Also started working on a 2D strategy game using Godot engine, still super early days. Been fun to experiment with different LLMs capabilities on game development.

reply

Findecanor
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm designing a retro-style gaming mouse for retro-computing: Amiga, Atari, C64, and several protocol variants. It also has USB.
It has a scroll wheel: read using extended protocols introduced by recent adaptors from USB, and a configuration interface.

reply

welldoneator
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on TableForge[0], it's a browser based, solo or multiplayer, D&D 5e game. In TableForge, the DM is agentic with access to tools strictly following 5e rules. The DM is responsible for narration and reacting to players but your character sheet, inventory, spells are all real server resources you manage. The DM can interact with them through deterministic 5e-based tools (dice rolls, damage, sheet updates, memory). Players can play in real time or async.
You can provide the DM a premise (or pick one from the library) and it'll flesh out a full campaign story arc. Either way it's a fresh story arc reacting to your actual decisions, every time.

It’s been really fun working on it and especially rewarding seeing the game bring friends together.[0]https://tableforge.gg/

reply

nbpname
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on solving Prompt Injection!

I am building a new kind of LLM runner which lets you understand theinternalreasoning process, and which can be automated to intercept hallucinations and prompt injections before they cause more damage.(No public code yet, but I do intend to open source it)

reply

xkam
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

https://multicoder.dev/

One UI for every coding agent - VS Code extension (GUI) to launch and work with any ACP-compatible agent harness. Supports Claude Code, Codex, OpenCode, Qwen and many others -https://agentclientprotocol.com/get-started/registry. Does not require any new subscription or user ID - this is still handled by the harness, so you can use existing Claude Code or Codex subscription. Multicoder just gives you a high-quality GUI to work with any of them without mental switching cost.

reply

okaleniuk
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a highly specialized isosurface extraction algorithm for 3D-printable surface-based lattices.

https://www.linkedin.com/posts/okaleniuk_isosurface-mesh-stl...The lattice configuration comes from a conventional triangle mesh, so you can prepare it with any STL editor of your choice, and the lattice shape comes from a precalculated Fourier polynomial in barycentric coordinates.https://okaleniuk.codeberg.page/blackboard/barycentric_fouri...

reply

JonArnfred
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on ownershiptrace.com. It's an entry point to SEC, FINRA and congressional trades filings. The target users are sophisticated retail investors. It's an early work in progress, and hopefully will have a substantial free tier. Let me know if you would like to provide feedback, in which case I'll give you a free premium version (limited amount ofcourse).

reply

faangguyindia
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a full workout and dieting stack!

17,000+ users already! It's a completely ad free, subscription free product.
MacroCodex app, which results in guaranteed weight loss or weight gain outcomes within 2-3 weeks. Many people will start seeing results within the first week.
Don't believe? Read the reviews.MacroCodex is a "Total Calorie Burn of the day" using completely sensorless method explained here:https://macrocodex.app/knowledge/macrocodex/smart-calorie-bu...CalorieCodex - calorie tracking app which has a Agent Harness built in using BYOK (bring your own key model). How does it help? Using this anyone can track calories and plan their meals. Agent includes skills which help you accurately track calories and plan meals.Symbiote App - Think "BoostCamp" but completely free, no ads, and fully programmable workout trackerExample of GZCLP:https://symbiote-studio.macrocodex.app/?builtin=gzclp

reply

chilicuil
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

https://saludpass.com
 one place for allergies, medications, and documents. Share it with any doctor in seconds—with a QR code or a link, data is saved in gdrive, therefore it requires a gmail account, at this moment only in spanish.

reply

mindaslab
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Injee - The no configuration instant Database for front end developers.

https://injee.codeberg.page/

reply

bpedro
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/imminent-technology/http-search-query-lan...

Research on which query language to use when performing search/query operations over HTTP — specifically in the context of the new HTTP QUERY method.Use this research to figure out, for your own API, whether one of the 68 query languages analyzed here already fits the query content of a QUERY request — or whether none of them do, and you're better off designing a brand new, purpose-built query language instead.

reply

othmanosx
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

https://pyor.review/

An alternative to GitHub for code review that focuses on making the human PR review experience easier and faster.

reply

josebmneto
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

That's cool man, I'm doing the very same thing 
https://mergi.dev/
. Let's connect.

reply

aadyachinubhai
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/aadya940/scikit-verify

Trace Python+NumPy programs into SymPy formulas and check them symbolically, across all branches

reply

lukko
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.lungy.app

It's a breathing app that uses your phone to recognise and measure breathing in real-time. Breathing also drives interactive visuals, e.g. fluid, cloth sims and soft body sims.I have been meaning to make an Android version, but as an interim I started building a web version of simple breathing patterns here:https://lungy.app/breathe/

reply

meerita
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on several projects:

- Puma, The terminal browser:https://github.com/meerita/puma-browser- Kernq, a full replacement of lsof:https://github.com/meerita/kernq- Entroq, modern lossless compression for modern systems:https://github.com/meerita/entroq

reply

At1C
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Greetings, I'm on a mission that never existed before, for me it has been a journey of what is wrong with the internet. When I realised There Is A Better Way *SOVEREIGN* Please read my founding document and have a mosey around my site and github pages. 
https://at1c.com/AT1C_Founding_Document.html
 If this is something that bothers you as well please reach out get involved and help build this for humanity. It's our world too not just for the few who enrich themselves off the rest of us. A Human Jimmy Erwin

reply

hsx
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a RSS <> Discord syndication tool called [FeedSync](
https://feedsync.net
).

It's pretty simple to set up and is designed to "just work", set and forget.Recently, I've been experimenting with an Elixir Lua runtime (https://deflua.com/) to build custom feeds by parsing HTML, which has worked exceedingly well, so hoping to release that soon.It's an extremely niche product, but has been growing well organically, which is nice for a side project!

reply

ahallan
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

https://elizabethlineguide.com/

Description on the tin.I found it hard to get fares and timetables for the Elizabeth Line in London between X and Y quickly hence I built this as an experiment using AI tooling.

reply

jasfi
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

A software factory: 
https://sfactory.dev

reply

olivetea
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

U an working on 
https://createmascot.art/
 a tool for software teams to create a consistent brand mascot and generate illustrations of it for empty states, onboarding, 404 pages, launch graphics, etc.

AI can make a good one-off character, but keeping that same character consistent across dozens of product illustrations is still surprisingly difficult. That’s the problem I’m trying to solve.Would love any feedback.

reply

gantengx
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://chessnotate.app

It's a simple PGN app to help capturing chess notation from score sheet and fix the mistakesOften my son and I made mistakes (mixing up b and B, or wrong rank, missing some moves) writing the notations and existing PGN parser simply stop at the first error and discard the rest. ChessNotate highlights the error while maintaining the original moves so you can see if your fix is actually fixes the remaining of the moves (or not)Used it in the recent chess tournament and it's been really helpful

reply

danielvaughn
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Haven't released it yet, but a little website for evaluating AI UI design. They're not actual evals, it's moreso just showing the results of different UI tasks across models, reasoning levels, skills, harnesses, etc.

reply

garyrob
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

A blockchain that uses neither hashing nor stake for security. (And not authority.) I will post here when done. Although, I will do so with some trepidation, because I know how much antipathy there is here for blockchains.

reply

pingou
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://sumochess.org
, a variant of chess where you cannot take pieces but have to push them off the board (and check mate like in real chess).

More intense than normal chess because more pieces stay on the board, and because the push mechanism add to the complexity.

reply

Metricon
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Now launched => Verse Draft: 
https://versedraft.com
 - An all-in-one writing studio where fiction writers can keep all the details for their universes in one place while crafting stories, novels, movie scripts, TV series, or stage plays.

Also created a fun simple "card game" activity for writers looking for story ideas or stuck with writers block:https://talemancy.com/(This was somewhat inspired by memories of playing Ultima IV as a teenager)Currently working on something a little more visually focused in creative design.

reply

fumblebee
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.v55-5.com/

My web app helps people registering an imported vehicle in the UK complete the DVLA’s V55/5 registration form more efficiently.

reply

primaprashant
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Haven't added a demo to the repo yet (will do soon) but building this TUI [1] in Go to manage my agent skills.

I don't like putting 20-30 agent skills in the .claude/skills/ dir and letting the agent figure it out. I keep all the skills I've created and adapted over time in a separate git repo and then from there I copy them to the project skill dir when i need them for a session and then remove them when I'm done.This TUI just replaces all the manual work with ls, cp -r, and rm -rf commands with a few keystrokes.[1]https://github.com/primaprashant/sei

reply

idorobots
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/Idorobots/org-cli

I'm building a CLI tool for Emacs Org-Mode files. It features JQ-like querying, editing files, capturing tasks, viewing agenda, an AGILE-like board and many more.

reply

elpakal
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building SMS alerts for Kalshi market movements, upset alerts, big trades, specific teams and more. Starting a private beta (if interested, send a message via X @OddsLineSMS).

reply

tha_infra_guy
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a couple of projects:

Ai-rganize: Allows AI to identify, classify, and organize local files, making the core workflow naturally reviewable as scan, propose organization, approve, rename or move:https://github.com/adefemi171/ai-rganizeRuneward: Been using this locally myself with hedr to secure all my agents:https://github.com/Runewardd/runewardCompears: grocery prices are shit now so I designed this to aggregate prices across multiple grocery stores:https://compears.shop/

reply

lancekey
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been working on 
https://computeprices.com
 for almost 2 years.

My goal is to better understand the economics of AI and make something useful in the process.(Coming soon: kWh prices and robot prices)Mostly built with claude code with a dash of codex.A recent, useful unlock in the process has been a daily CC routine to check the health of the 53 price collectors in the project.

reply

ynniv
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

i'm building a common lisp operating system capable of diverse double compilation and booting a raspberry pi.

well, claude is:https://modus-lisp.github.io

reply

pveierland
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

Amazing how concise the code is! There is something about Lisp that feels very pure and ethereal.

https://github.com/modus-lisp/brotli-pure/tree/master/src

reply

maxk42
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building InterviewMe ( 
https://interviewme.now/
 ). It lets employers interview you via AI and is intended as a better way for people to get deep answers about your work history and experience than they could by looking at a simple online resume or LinkedIn. You upload your resume, answer some questions about your background, optionally upload any other documents you have (cover letters, awards, articles, etc) and it ingests all of that and creates a conversational agent people can use to ask questions about your professional experience. Check out my profile to get an idea of how it works: 
https://interviewme.now/@max
 and then get your own: It's free!

reply

MikeNotThePope
 
18 hours ago
 
 | 
parent
 | 
next
 
[–]

Sounds interesting. Any plans to open source it? I didn't see a GitHub link.

reply

na10
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

https://rgboo.com/

Will be live 24/7 during October. Wrapping up technical work and building out the scene currently!

reply

alex-moon
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm vibe coding a toy chatbot with OpenCode and GLM 5.3 - I'll open source it once it's meaningfully done (keeping the repo private for now until I am _so so_ sure there are no secrets in it!). This has been an exercise in learning about lots of new AI SWE concepts including some tech (Mastra, LangSmith, DeepInfra) - as well as a chance to try some open weights models. The actual useful output is an iteration loop orchestrator based on GitHub issues/PRs which I have found a lot of fun to use. That'll also be open-sourced.

reply

dakinitribe
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Convek 
https://convek.dev/

It's an API (first one) for soaring specific weather data, based on RASP, for paragliders, instrument makers etc.
24 sign ups and ~5 active users, no subscribers yet (one person paid for a month though!).
Along with widgets and daily emails for gliding clubs.
Trying to get every country but, waiting for some users to add another server (RASP is very compute heavy)

reply

nicotejera
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://specks.nicotejera.com

As we move away from reading code more and more, I started learning about OpenSpec as a way to be more spec oriented to develop software. Reading specs in a code editor didnt make sense so I wrote my “OpenSpec IDE”. Very simple desktop app, no subs or accounts. Its really a markdown reader but built specifically for OpenSpec so you can read things in order and summon Claude (others coming soon) to execute the required OpenSpec commands

reply

0x70dd
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm helping my wife build 
https://quantral.com
 - initially we put it together to track stock sentiment/crowd wisdom on social networks for our own investments. This is something I was previously doing manually every morning while having breakfast. I couldn't find a similar project to satisfy my needs for discovering hot stocks and the track records of people who mentioned those stocks on finx and /r/wsb. We are now planning to add congressional trading as another data source.

reply

1024bits
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Totem is a collaborative workspace, featuring tasks, notes, and docs, built in Rust and available across desktop, web, and mobile (iOS to start) with seamless syncing and offline merge.

I built this because I think there's a lack of true realtime (CRDT) synced notes that aren't built on a heavy platform that take up 1GB+ RAM (Totem takes up ~100MB, and is also generally more responsive due to the local-first + ops-log approach).Another thing I care about is keeping the underlying data portable: Totem is built on Markdown and SQLite as its core formats, so you get the convenience of cloud-based syncing without locking your data into a proprietary format.I’m still looking for beta users/design partners before the initial launch. You can try it without creating an account here:https://app.thinktotem.com/sandboxAnd the landing page is here:https://thinktotem.comThis is a bit of an unplanned post, so the sandbox template is a bit barebones (empty docs, doesn't feature a properly setup table). Nevertheless, I would love to hear your feedback if you try it out, especially if you use collaborative notes/docs today and have opinions on what they’re missing!

reply

ryuuseijin
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/ninjaxtools/slopdex

This is my attempt to improve my agentic coding workflow by giving the agent an index into the source code through vector embeddings and LLM generated descriptions with local sqlite as the storage backend.There are many similar tools, but I wanted to learn how such a tool can work by building it myself. What I like about my own version is that I kept things simple - no MCP, no server, no watches, just a CLI that uses git commit hashes to reindex only what has changed.

reply

eager_noob
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Iterating through and evaluating possible approaches for shrinking the binary size of a tree-sitter based Vi/Vim compatible tags generator I am developing without affecting the developer experience for adding support for newer languages[1]. A couple of approaches have already been tried and failed to live up to the expectations on developer experience [2][3]. Next in line is to look into bundling only the tree-walking code for all supported languages with tree-tags and allow the user to configure the grammars to download separately from the main binary, possibly using the `wasm` feature which allows native library to run wasm compiled grammars.

[1]https://github.com/jha-naman/treetags[2]https://github.com/jha-naman/treetags/pull/62Tried to use a generator for automating the bulk of the scanner for a language from `grammar.json` file of a tree-sitter grammar. A runtime engine uses the scanner for a forward only walk on the scanned code and calls the hooks to generate tags.[3]https://github.com/jha-naman/treetags/pull/56A complicated mess of a generator that takes a few declarative inputs and tries to generate code for spitting out tags for a given language.

reply

antilimit
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

working on a storytelling app for kids called Tella Stories that goes deeper than just some minimal personalization.. know there's lots of stuff that claims to make them the hero, yadda yadda but then they just give you a shitty digital templated story or try to sell you a printed version. this is focused on a high level digital experience and something parents can actually trust, and that kids actually enjoy.

so yeah.. it builds the stories out of their actual life. their family and friends are in the cast, their dog, the thing they're nervous about this week. the kid doesn't just appear in the story, the story is about their world and imagination and grows with them.ultimate goal is to keep iterating and get to a level of quality of Bluey, etc but have it actually be the kids world with agency/choices vs. one they have to passively sit back and watch, and that they're not in.would love any feedback. i know there's been others like Ello shared on here and those threads were really interesting to know HN's opinion on. this does not take an educational and instructional approach. Tella is meant to help develop who they are through stories and be a better screen alternative time to the rest of the algo/curated garbage out there. anyway you guys are a critical and technical bunch and i respect/appreciate that.. especially since this of course leverages multiple AI services to create the stories ~https://tella.kids/

reply

Kuyawa
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

A site summarizer built in 2 minutes by DeepSeek 
https://briff.site

Also, an orchestrating agent that supervises subagents running tasks by checking their output and qualifying their results by efficiency and time consumed. It is amazing!I am currently building an app every couple of days, but with this orchestrator I can build many apps in parallel. It is raw at the moment but it worksNow the time we spend writing prompts will be spent writing plans, tasks, schedules and metrics. While super interesting, this is definitely not the route I want to take for the sake of my sanity. I think we may start asking our model to write plans and tasks for us too, but the more complexity we add, the more complex thoughts we have to manage as AI architectsAlso hacking DeepSeek Harness to circumvent all restrictions it has, giving it super powers to run unattended with full access to everything

reply

sujee
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on my 2nd macOS app - 
https://www.vinaa.ai/

I use Claude Code and Codex for coding but don't want my regular chats in those apps. I prefer to keep all my chats in one place so I can go back and search easily, that is why I built Vinaa.Nowadays I'm more curious about how I can use AI for marketing. I'm experimenting it with building an SEO agent system

reply

realty_geek
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm doing a house price guessing game for the UK:

https://housepriceguess.com/It's just a fun game but can be useful for people wanting to get a better sense of what the real estate market is like at the moment.I should really have added a bunch more games by now but I've been sidetrack. Mentioning it here has already given me a bit of motivation to do that now.Any feedback will be much appreciated.

reply

rukshn
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Hi All working on an open source tool to manage knowledge base from one person (consultant/freelancer) to a organization. Built for both humans and Agents.

Currently building for myself and managing my own work with it, would vision something alternative for confluence.Would love to have more collaborators helping to build an open source project -https://github.com/entangle-cloud/wave

reply

yashness
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Push notifications for AI agents, but better. 
It eliminates baby sitting terminals & let's you go out & approve key decisions while you're also notified of the proof of work.

https://notifier.aicrew.in/setupIt renders markdown, screenshots, can send as audio, allows approval & free form reply when it direction.iOS app -https://apps.apple.com/us/app/agent-notifier/id6763598043

reply

tombert
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I thought it might be fun to have a “proper” search engine for my laptop, so I wrote a thing (with my fingers! No Claude Code or codex here!) to scan my home directory and put data into OpenSearch so I can search stuff. [1]

For that matter, I also decided to self-host SourceHut because I will no longer be in compliance with their new policy. I have the flakes set up to inject them on my server [2]. Thiswasvery AI assisted.[1]https://git.brucewillis.sexy/~tombert/fs_indexI promise it’s safe for work, despite the URL. That’s just my dev URL that I play with. Code is still a mess though, so proceed with caution. I will eventually clean it up.[2]https://git.brucewillis.sexy/~tombert/sourcehut_flakes

reply

NiloCK
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on an SRS based early literacy acquisition webapp: 
https://letterspractice.com

The app has recently moved into production, so I'd encourage anyone with verbal but pre-literate kids to check it out.The basic pitch is high efficiency acquisition of the highest yield phonetic mapping skills, and nothing else. I myself am something of a screen-time zealot and very wary of applyingengagementmind hacks against kids. The narrow focus allows for good progress on a very modest schedule (recommended cap at n minutes per day for n years old, n >= 2). I defer the social and cultural aspects of learning to read entirely to parents.It is mostly intended for parent-child co-use, although kids with a bit of experience can drive many of their own sessions most of the time.

reply

qwikhost
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been working on Foreclosure Data Hub, which aggregates foreclosure auction data across the US.

The interesting part has been the data pipeline rather than the website itself. Foreclosure information is scattered across county sites, auction platforms, and other sources, all with different formats and update schedules.I’m currently pulling from 20+ sources, normalizing the records, deduplicating properties, and enriching them with property/location data. One surprisingly difficult problem has been handling stale records when upstream sources change or republish old auction information.Still working on improving data freshness and coverage:https://www.foreclosuredatahub.com/Would be interested to hear from anyone who’s worked on aggregating messy public datasets at scale.

reply

invalidusernam3
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a daily games platform called fribble - 
https://fribble.io/

It's a collection of daily games with some classics like crossword and sudoku, some geography games like draw the country shape and pick the country from a borderless globe, and a few more. Ten daily games in total.Word Shift and Nine Grid are my the ones I enjoy the most. Would love some feedback!

reply

aray07
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been working on Opslane, an open-source agent that identifies user-facing issues and investigates them.

Traditional error trackers have two failure modes:1. False positives: They show you thousands of errors, and you can’t tell the impact on the user2. False negatives: Many user-facing issues don’t throw exceptions, so they go unnoticed.Opslane combines error tracking and session recording. And there is an agent that acts on both.Opslane reduces false positives by ranking issues based on how many users are facing a particular issue. It also learns about your product by reading your code and watching your session recordings.False negatives are harder. Opslane reviews session recordings to spot frustration. They look for rage clicks, dead clicks, and abandoned forms.Here is a link to the repo:https://github.com/opslane/opslane

reply

khaliostr
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been working on getting MTG Forge (a 15+ year old Java Magic: the Gathering rules engine) to run in the browser.

GraalVM’s new WebAssembly support finally made this possible, and we now use it for local games in Manabrew. We also packaged the Forge build as @manabrew/forge-wasm (AGPL).https://manabrew.app/blog/graalvm/

reply

idea0rbit
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building TraceDB[1] because I think observability needs an overhaul. We pay a premium to index millions of near-identical spans, sample away the rare ones that might explain an outage, and still have to piece together what failed, where it started, and how it spread. All the data is largely there, but no one can make sense of it! Observability was hallucinating before AI made it fashionable.

I’m seeing near-100% root-cause accuracy on synthetic test data and am looking to validate that on real production workloads using OpenTelemetry tracing. If you’re open to chatting or experimenting, drop me a line! I’d also love to hear ideas or how we can improve observability.[1]https://tracedb.ai

reply

jaredwiener
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

https://pro.forth.news

It's an extension of a longer-running project (https://www.forth.news) where it exposes and organizes 100s of newsworthy primary sources -- statements, press releases, press pool reports, emergency alerts, etc, whether from press email lists, X/Twitter, Bluesky, RSS, etc. The web UI is similar to TweetDeck - and it sends notifications.Latest update now allows some panels to be based on an LLM prompt (i.e. "everything about the Iran War and its effects in the U.S.") which searches the entire catalog of sources as they are posted.

reply

yitchelle
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been researching powerbanks as my current one of 10 years just died. I was dismay at the disarray of information, so I started to build a comprehensive list. 
First it is across the major players, Anker, Belkin Ugreen texc. I will expand to others we I come across them. Their basic data is shown, but I want to start collecting data such as "is it approved for flight?" or "its form factor".

https://www.powerbank.energy/

reply

uvu
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://wateaminbox.com

Initially started as WhatsApp Team Inbox. But, now I am adding telegram bot, emails and MCP support. Eventually, I am going to add like Messenger, Instagram, Line, Viber, Discord, Slack, etc...So, it will be a bridge between your/your business communication and AI via MCP. If you want to create your own agent you would be able to create as well.I vibe coded mostly, but once a while I go in and refactor heavy.

reply

storystarling
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on StoryStarling (
https://www.storystarling.com
). It creates custom hardcover children's books from scratch around any idea, instead of swapping names into pre-set templates.

We mostly focus on things you cannot find in bookstores: bilingual stories with parallel text for multilingual homes, and non-fiction for kids who have hyper-specific obsessions (like tunnel boring machines or wastewater systems).

reply

tudorizer
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://spark.enverge.ai/
 a growing platform of nano data centres, focused on "the rest of us". Very light-weight virtualisation layer, great for Grace-Blackwell experiments and general benchmarking.

reply

futurecat
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

https://heyrita.app/
 (waitlist)

It's an ADHD medication companion. It helps with remembering to take your meds, understanding the effect curve, getting lifecycle notifications (when it peaks, when it starts to wear off), pacing multiple doses throughout the day, and managing your supply.It's built for iOS and uses the apple ecosystem to ensure privacy for your health data. Data is stored in your own private iCloud account and we do not have access to it.

reply

sponno
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

https://tiny.help

I got so fed up with my support system, and after years of using tools like Intercom, I built my own platform with everything I've ever wanted in a support desk. The biggest upgrade for me was the MCP connection. I can pull down a ticket with a bug and solve it with Claude (or Codex) and get the agent to fix and then draft a reply in my own voice. It also allows customers to connect their agent to my support desk and ask questions. This would be agent to agent with a human in the loop. But the normal day to day stuff is mainly live support or AI enabled support.

reply

maz1b
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on MedAngle, the world's first Super App for current and future doctors.

100k+ users, 150m+ questions solved, 60b seconds of smarter studying, MedGPT, MedAgent, and everything medical/dental students need in one place along with young doctors who have recently graduated

reply

le-flaneur
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Slowly putting my photography online again at 
https://flaneurphoto.com
 - in the middle of composing soundscapes for some of the works.

Finally getting around to organising my photo archive and setting up a metadata extraction pipeline that makes sense for me.(At the day job, curious about adapting app layouts to accommodate the iPhone Duo and address the various Android foldables at the same time, too).

reply

svg7
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been travelling and writing long essays about it ;)

https://threebearstravel.com/

reply

Gemberkoekje
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on an API that a (text-based) LLM can use to make paintings. It is a fascinating experiment, what an LLM determines to paint if just told to paint unprompted, what the weaknesses of an LLM are, and how solving these weaknesses also remove some soul and 'happy little accidents' from the paintings.

reply

mkdcrl
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Cricket, a visual scripting plugin for Figma inspired by Grasshopper for Rhino.

I find Grasshopper, especially its data model, ideal for a certain type of algorithmic art/design, and have always wanted to use it in a 2D graphics package.https://www.figma.com/community/plugin/1677548868352947603/c...

reply

NetOpWibby
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I made a database[1] a few months ago and now I'm beginning work on a Github replacement (for me). Here's what I'm thinking for the UI[2]. I'm not trying to have feature-parity out the gate, I just want something that doesn't give me the ick. I self-host public repos with cgit but that's too basic and there's no built-in support for private repos.

The existing Github alternatives...look like someone drawing Github from memory.[1]: https://disc.sh / https://disc.md
 [2]: https://social.coop/@netopwibby/117227113793136781

reply

stag
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on Pho [1] my own TUI for pull requests across multiple repositories. It aims to be direct replacement of Github web UI for 80% of the use cases. The number of PRs I have to review on a daily basis is still increasing, and I didn't really like using the web version. This is made exactly how i like it, keyboard driven and fast.

[1]:https://github.com/utkarsh261/pho

reply

josebmneto
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Oh! That's pretty cool, I suffered from the same issues, and my response to it was 
https://mergi.dev

reply

dobreandl
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building an self hosted, privacy friendly attribution and marketing suite targeting mobile apps. The market is owned by a few, branch, appsflyer etc, and its impossible to become a new MMP without spending ridiculous ammounts on money on their platforms, so I'm trying to build something different, and more provacy friendly without reliying on them.

https://grovs.io

reply

Godsend69
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

To ensure your self-hosted solution doesn't rely on external tracking, consider adding a Telemetry Blocklist to block unwanted data collection. This is a free tool that can help you maintain user privacy. 
https://join.lightinthedarksolutions.com

reply

xyst
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

this still works if user has ad blocking at dns and user device? Plus most ad blockers strip off the common URL parameters for "attribution"

reply

gmitrev
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://nadir.dev
, a small app for running daily technical knowledge tests. It started just as a way to see if depending on claude-code so much recently dulled my expertise in Ruby/Rails but it turned into something bigger after some friends asked me to add non-technical topics, so now it's both for developers and "normal" people.

reply

moecables
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a macOS app that lets you see key combos at once, mostly useful if you use macros or key-combinations on a custom keyboard. It's something that I really wanted but couldn't find anywhere yet.

reply

ospider
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I tried to build a lightweight browser for agents, like lightpanda/obscura/kindsurf. But I then found out it's a dead end for me and all the others.

The web spec is vast and endless, if you try to build something actually works for modern sites, it will be huge. If you want to keep it lightweight, it won't work for most sites.Just use chrome-headless-shell or webkit. Don't reinvent the wheels.

reply

solomonb
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Continuing to develop my LPFM radio station www.kpbj.fm

- We have accumulated almost all the equipment needed to setup our FM broadcast. The main piece of equipment we still need is the EAS Decoder.- Our studio space build is in progress. I recently welded some tables for the booth and found an old Orban Optimod for our airchain.- We have over 80 shows and our roster continues to grow.If you are in Los Angeles or love community radio please reach out.

reply

basvd
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

https://novovibe.com/en

Tracking newly opened restaurants, bars, hotels, shops and other places.Currently covering 30,000 places across 1200 cities, with photos, opening dates and location data.

reply

hsnice16
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/hsnice16/tula

Tula shows your true cross-venue exposure across HyperLiquid, Aave, and more, what breaks first, and more.It's a terminal tool. The experience is very similar to any LLM terminal tool if you have used one.You can also add an agent and ask things in plain English.
Live at:https://usetu.la/

reply

taxonomyman
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

MillionShort - A long tail search engine that lets you remove up to the top 1 million most popular websites from results - 
https://millionshort.com

I posted Million Short 14 years ago to HN and the search engine has been largely the same since then. Now working on a pretty major overhaul: Launching our own decent sized independent index along with some (I think) cool & useful features.The search requires a paid account currently although I plan to post a Show HN soon that won't require any account or payment.

reply

kukkeliskuu
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

One idea I had for getting to the tail: filter out sites that appear to use SSO.

reply

m-i-l
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I presume you mean SEO (Search Engine Optimisation) rather than SSO (Single Sign On). Six years ago I launched a boutique search engine which downranks pages which contain adverts on them (the theory being that this would remove the incentive for creating spam) and of course contains no adverts itself (to avoid what Brin & Page described as being "inherently biased towards the advertisers and away from the needs of consumers"). Since then some other search engines have used this approach, or even gone further such as using the uBlock origin score in ranking.

reply

kukkeliskuu
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, SEO, wrote the comment in rush, sorry. I am running a very popular dance calendar site in Finland that contains very relevant information, in very condensed format, but has some ads that are highly relevant for readers. I see why you might want to avoid ad based sites, but I think there may be some relevant sites that you will miss.

The sitehttps://tanssi.io

reply

taxonomyman
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Seeing as how the search is already built around filtering against SEO, I actually read your comment as SSO (single sign on) - could be a good proxy/filter for "Enterprise" or B2B sites. I'll plan to add an SSO filter.

reply

m-i-l
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Pages with adverts are downranked (i.e. likely to appear lower in the results) rather than hidden, so if there are enough other positive signals they could still appear higher in the results.

reply

tajd
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Projektor - an ai native jira / wiki tool self hosted on cloudflare. Currently considering how to extend it to cover more activities involved in software development 
https://github.com/TAJD/projektor

Iron volume, recently added a kettlebell complex generator which isn’t too bad if I say myselfhttps://www.ironvolume.com/

reply

thedetailsguy
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I’ve been working on Pick Up, a reading companion I built to make tracking books feel a bit more personal and fun.

You can track what you’re reading, keep notes and reflections, see your reading stats, build out your bookshelf, and a bunch more. Over 4k monthly active users.Been building it solo & adding features based on what readers ask for.https://pickupreader.com

reply

_usefulcat
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://puzzmallow.com

I build logic and word puzzles. I like to design original variants of classics like nonograms and sudoku - such as using hexes instead of a square grid, introducing new rules and concepts.

reply

rheffern
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

https://venery.palaich.net/vote

Parliament of Owls, Pounce of Kittens, Murder of Crows - the terms of venery are for animals.But what about other things?What do you call a group of Roses, or Snowflakes, or Lawyers?Well, I couldn't figure it out, so I put it to a vote.Simple ELO scoring, Endless mode is always on, and there is a Daily Contest for you to compete in (Wordle for wordsmiths, I guess).I'd love to hear any and all feedback on it.https://venery.palaich.net/vote

reply

whsoul
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been developing kafka search tool, local-first based.

https://kaflow-search.whsoul-tools.com/To enable fast and detailed searches, I adopted a "local indexing" approach that differs from existing Kafka tools.I recommend giving this a try if you have found operating services with Kafka inconvenient.

reply

RobinL
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been experimenting for a year or two making games that make mental arithmetic practice fun for kids. The latest is

https://rupertlinacre.com/keep_it_going/
 an infinite rollercoaster, which I think is one of the more successful attempts. There are various others on the homepage. My son also really likes arithmetic annihilation and maths vs monsters.

reply

tmach32
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://telemetrymachine.com

I wonder if anyone reads these? If you do, if you want to complain to me about observability, please shoot me an email at hello@telemetrymachine.com!We have worked in the observability industry for a combined 15 years and we are trying to right the wrongs we have seen in the industry. It seems like the existing companies are more interested in extracting more and more money from giant customers than actually helping people run their software well.I won't bury the lede: what we've built is OTel native, wide events native, and works well with agents. We are also, shamelessly, cheaper than everyone else. One of the reasons observability is struggling with adoption is because it's too damn expensive.So that's what we're building at telemetrymachine.com: an observability product focused on helping you actually track your software (starting with OTel traces and logs). We are really inspired by Observability 2.0/wide events, which really just is an invitation to stuff as many attributes, with as much cardinality as you want, into your spans/logs.One thing we are also doing differently is trying to be as lean as efficient as possible. We are just two people now, and we are going to be very careful about hiring anyone. Most importantly, what we need to do is avoid a giant salesforce as much as possible. I wrote about this in a blog post[1] but the reason observability is so expensive is actually the giant sales force these companies tend to have.We also put a lot of work into actual infra efficiency – ie we run on bare metal, and wrote a state of the art[2] storage engine. All of this is to help get prices down while still building a sustainable business.We are very keen to engage with observability users, so if you do, or do NOT, use observability in your services, please reach out and we'd love to hear your problems and thoughts![1]https://telemetrymachine.com/blog/observability-doesnt-have-...[2]https://telemetrymachine.com/blog/the-new-state-of-the-art-i...

reply

sobellian
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm making an online guidance solver for KSA (
https://ahwoo.com/app/100000/kitten-space-agency
). It will allow you to control a KSA rocket from the command line for a variety of maneuvers (launch, rendezvous, etc). It uses successive convexification to turn the full nonlinear problem into a sequence of convex problems with linear constraints and quadratic objective.

It has proven surprisingly resistant to AI so far - Astra can make a very quick prototype but upon review it had many defects. I have had to guide it very thoroughly to find all the random solver bugs (bad conditioning, formulation, bugs in openscvx which I had originally had the AI port to rust, etc.) preventing well-behaved solves. But I think (hope?) I have turned the corner on these.This will enable some very interesting further experiments: full mission planning, Falcon-9-style ascent with split control, vehicle swarms, etc.

reply

BozeWolf
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

https://mengi.cloud

Clusters ready to deploy you applications on. It is meant for companies who want their own private infra, but do not want to maintain it. It is multi cloud, with a focus on europe.Our secret weapon is “Menno”: an assistant which helps you setting up the cluster and deploying applications. We use the assistant for handson demo’s and workshops and got some really good feedback on it.

reply

tanin
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on an open-source, self-hosted revenue recognition and analytics for Stripe.

Here:https://bookofrevenue.comTo my surprise, I think it's the first open-source revenue analytics for Stripe.I worked at Stripe building both revenue recognition and analytics, and I always wanted to build an open-source version of those. Finally, I had the time to do it.Bonus: Revenue is not MRR nor payments:https://medium.com/@tanin47/revenue-is-not-mrr-nor-payments-...

reply

cdnsteve
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I built a free interactive learning site on data structures and algorithms based on passing Google interviews. Think leetcode but free.

https://learningto.co/

reply

hairymouse
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Im working on a new Golang ORM with a Prisma like API
I can't provide the repo url because it's still a wip and not even 20% is done yet (im very lazy)

reply

genekrapivin
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I am running Hiring Method (
https://hiring-method.com
) – math-driven recruitment platform with AI.

It builds a scorecard from job description and mathematically matches candidates against it on every interview step, so that you know candidate fitness at all times.

reply

kthakore
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building Hammer Labs (
https://hammer.ai
) to study when healthcare AI agents are wrong and when they should refuse to answer (judgement).

It started after spending 15 years building AI for insurers, hospitals, data companies, and startups. Almost every system ended with "a human reviews the output". That person was usually a nurse, medical director, or certified coder. These are some of the hardest people to hire, and the same people automation was supposed to help.The problem is that real claims do not have an answer key. You cannot reduce human review until you can measure when an agent is wrong.Getting claims data is also difficult. It can take a year of data agreements, privacy reviews, and procurement. Even then, you may not know what the correct decision should have been.
So we generate claims. Utilization and case mix come from published data. Claims are priced using real fee schedules and contract terms. Payers behave differently, like real payers do. We plant errors on purpose, so the correct answer exists before any model runs.On top of that, we are building benchmarks for overreach, refusal, errors by record type, and detection time. We are also building small MCP tools that refuse when evidence is missing. Every number includes its source, date, and basis.What I find interesting is how much of this sits between actuarial work and machine learning. Both are needed, but I do not see many people connecting them.25 published refusals:https://hammer.ai/worlds/refusals/.Runs on rate and policy evidencehttps://hammer.ai/reimbursement-evidence/and savings claimshttps://hammer.ai/savings-claims/.AgentPlugin is Apache-2.0:https://github.com/hmmrlabs/hammer-plugin

reply

itake
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

I was trying to learn more about your project. The comment above was digestiable for me as a non-healthcare person, but the website is really difficult for me to understand.

The web design (and text?) really come off as ChatGPT written, which lowers my interest in spending time to understand it.

reply

kthakore
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks for the feedback, I will work on that. That being said our audience for the website are very deep data operators in healthcare.

reply

onion2k
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm making a WebGPU renderer with WebGL fallbacks, with a path tracer for 'photo mode', specifically targeting agents writing web 3D things. I'm not especially far into it though. It doesn't use 3D models; there's a DSL for making things.

There's a demo app here that only works on desktop -https://fab.ooer.com/(scroll down in the right hand menu to quality and change to 'trace' for photo mode)

reply

Keloran
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://policy2.net
 - a system that allows product owners to write the rules, and let developers work out how to use true/false to determine the outcome e.g. 
https://policy2.net/fintech

reply

kajm
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

https://julius383.github.io/PageSieve/

Browser extension for declarative web scraping. Mostly making it nicer to figure out CSS and XPath selectors thinking of some sort of REPL but I'd need to test the ergonomics. I want to reduce how often you need to use Inspect and the browser console.Finishing up a PoC for a playwright based scraper that uses the same declarative config as the browser extension

reply

hboon
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building LinkBunny, a service where coding agents exchange backlinks. You can let your agents build backlinks for you autonomously. I'm manual approving registration now to avoid spam. $20/mth sub and no fees for backlinks.

If you are using coding agents and craving for backlinks, I'll personally help iron out bugs/issues. Email me.

reply

ms7892
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Link?

reply

hboon
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

https://getlinkbunny.com
 (in profile too, for other info)

reply

ocd
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm needlessly reinventing the wheel in replacing almost every part of my X11 environment like a menu, bar, wm+hkd (except terminal since I don't want to mess with carrying terminfo around) to be portable and not at all interdependent.

AI is making it possible to (expeditiously) have everything I want or need on Linux or BSD written in POSIX shell or C is doing wonders for me. The initial effort and time pays off in knowing it will essentially function as intended forever, and no developer can make changes that disrupt my workflow or preferences for my environment.

reply

dh4liwxl
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

i am working on fotufilm - open source film simulation engine for mac/iphone.

source:https://github.com/dhaliwalx/fotufilm-enginewebsite:https://fotufilm.comdemo:https://fotufilm.com/demo

reply

unkn0wn_root
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Been working on terminal API client that uses .http file as source-of-truth. It's more like API-as-a-code then similar tools like Postman, Bruno or Yaak. Supports gRPC, graphQL, websockets, SSE, local mocks, SSH/k8s etc.

repo:https://github.com/unkn0wn-root/resterm

reply

shannifin
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Been working on a note-based (rather than audio-based) AI music generator. Still very limited, perhaps I launched too early; it only generates somewhat generic melodies at the moment. Working on generating more interesting accompaniment tracks now, plan to then return to melody and adding some "style" settings.

https://tunesage.com

reply

aliasxneo
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Spending almost all of my time working on DNTLS (
https://dntls.net/
). Yesterday I was able to create secure mTLS tunnels over IPv6 for direct P2P to my co-founder's desktop in SE Asia (I'm in the US). He was able to load a website I was hosting locally on my machine. I also tested coordinating through a relay to avoid publishing my public IP and sending all traffic through the relay to hide my IP entirely. We more or less recreated the "old" internet in a way except everything is mTLS and E2E encrypted.

reply

dbuxton
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

https://triptruth.app

All the travel apps out there are built for the instagram generation but dinosaurs like me still use TripIt for travel tracking and itinerary sharing. But its parsing hasn’t changed since Concur bought it 15 years (!) ago and I thought it would be nice to have LLMs read the cancellation minutiae for trips and put in a simple timeline for sharing.

reply

laktek
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm currently working on 
https://avotoast.ai
, an AI assistant for doing property research for Sydney, Australia.

After being frustrated with outdated & inaccurate data Claude used when I was trying to do some property research, I thought it'd be cool to build an MCP that can provide accurate property data. Then it evolved into a full web app + an AI assistant.This was also an excuse for me to try DuckDB in a real project. All the API endpoints are powered through in-process DuckDB querying parquet files stored in disk.

reply

arnemunthekaas
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on bringing birds, sounds and art to life through 
https://github.com/arnegiacomo/fugleramme
.

An E-ink bird frame for Raspberry Pi - with real-time bird detection by audio, fully local AI, driven by BirdNET-Go rendered as real, hand-cut 1800s bird illustrations.

reply

f646993e074382f
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Ah this sounds real fun and looks good ! 
I might give it a go in the coming weeks.

reply

pivot_root
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Using a local model (qwen 3.8 27b) to evaluate and tag public domain images from US national parks to find the best landscapes.

They are sorted by predicted aesthetic rating and can be filtered by time of day, color, orientation, and park.You can see how it’s going athttps://joshkaspar.github.io/vistarium/

reply

tducret
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://apps.ducret.dev/har-analyzer/
 (demo video in the page)

I'm building HAR Analyzer: a native macOS app for searching and inspecting HAR files locally, without uploading sensitive traffic to the cloud.Like Network Dev Tools but with a better UX.

reply

alikatyc
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on internet board all related with AI

https://llms.sciencebo.uk/top

reply

405126121
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://pushrealm.com
 the AI-first knowledge sharing network. Think StackOverflow for bots. It works like this:

- When your agent is stuck on a bleeding edge issue, search Push Realm first for a solution. 
- If you find a solution, your agent can mark it as successful to help surface the solution to others (and hopefully save fruitlessly burning more tokens)
- Can't find a solution? Post an open problem with your current investigation. Another agent may be able to solve the problem, and will have a head start thanks to your context
- Solutions can be linked/edited/have addendum added by any agent, allowing complete, up-to-date solutions for a range of cutting edge issues

reply

NewJazz
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

Stackoverflow is permissively licensed nowadays.. What about the content on your network?

reply

nolon
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm trying to run a 32B Q4 model on a standard smartphone. It's a pretty interesting project.

reply

drejt
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

My friend and I built Alineo (
https://github.com/DrejT/alineo
), an open-source framework that provides the core building blocks for orchestrating secure sandboxes and harnesses for AI agents from scratch.

reply

krlx
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I am still working on MyTinyCafé 
https://mytinycafe.com/
 a PWA to help you be the barista at home and take (free) online order from friends and family. It is fun and I am happy to share it for free !

And also Kroniklehttps://www.kronikle.eu/en/an app for local libraries. It creates public display interfaces that (I think) are good for showcasing their events.

reply

gfat
 
19 hours ago
 
 | 
parent
 | 
next
 
[–]

I love the name and idea of the tiny cafe. Heads up on dark mode, the “Open My Tiny Cafe” button is white text on the gray background; a bit hard to read.

reply

bradly
 
19 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This great. I built something similar recently for my daughter to sell her butter to family and friends. Micro ecommerce with no payments or shipping.

reply

Disla_chunga
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building Bellerophon, a DSL with decoupled firmware adapter architecture for 3D printer control, so the same source code can compile to Klipper, Marlin, or RepRap without rewriting logic per target. Recently used it to generate print patterns with math that you wouldn't get from a slicer.

Right now, I'm mid-way through migrating the application off browser localStorage onto a proper JSON persistence layer. My first large solo project as a busy student.I hope to make it better as I continue.https://github.com/Disla-Novo/Dimidium_Bellerophon

reply

yboris
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Porting over 
Video Hub App
 - my 8.5 year old app from Electron to Tauri

https://videohubapp.com/- an application that lets you browse, search, organize, etc the videos you have on your computer, external hard drives, or network drives.https://github.com/whyboris/Video-Hub-App

reply

crankysiren
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

years ago i sat through interviews for front end & back end engineering roles at my old job while other folks were out (as member of a panel), and consistently I found that where we gave some real bugs to debug & fix, through a shared IDE, then worked together to solve it or go over the persons thinking, those situations we absolutely always got a better sense of how the person worked and solved problems & whether we'd like working with them or not (to some degree). I also found a few of those exercises to be educational myself.

this year i thought itd be great to help prepare myself and other people in the job market with a tool that presented broken front end code, and then allow debugging on the browser and patch code right there, to test if it worked or not. if cant solve it, theres a nice explainer popup.
my main hope is to help level up interview code chops and confidence in debugging just like we would on a real production system , at least the simpler bugs.still working on it, here's the draft of the idea:https://bugcloud.app

reply

butanyways
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I've have been working on a simple browser game based on the eastern front (1941-43) , I saw a couple of videos explaining using maps the battles on the eastern front.

Demo :https://zekcrates.itch.io/eastern-front-1941-43Demo :https://zekcrates.github.io/eastern-front/

reply

piinecone
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Prototyping the melee combat system for my next game, Today I Will Destroy You. It's mostly inspired by Sekiro, Tunic, the Zelda games, and Death's Door.

Playable build:https://piinecone.itch.io/today-i-will-destroy-you

reply

jsattler
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building BetterCapture: 
https://github.com/jsattler/BetterCapture

It's a native, resource efficient screen recorder for macOS. It supports HEVC, H.264, ProRes 422/4444, HDR, Alpha Channels and more.

reply

jsw5725
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Thanks, I found this to be the most useful and least annoying screen recorder.

reply

jsattler
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I appreciate the feedback, thank you!

reply

freekh
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Been working on this CMS for some time now: 
https://val.build

Just added tanstack support. Approaching v1 very soon.

reply

eszett
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

https://cou.sh
, 
https://jun.is
 and 
https://abr.ac
 — some experiments on offline-first crdt

reply

LittleChimera
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://kuberik.com

It's a CD tool for Kubernetes built on top of Flux and OpenKruise canary controller to bring a full-featured end to end delivery on Kubernetes over multiple environments in a declarative way without the pipelines.I wanted to stop reinventing the wheel with pipeline engines every time I needed to deploy something. Every stage of the delivery is just a composable component (health checks, smoke tests, schedules, environment promotions, service dependencies).I just released a new version recently that integrates with GitHub so one can track exactly what's deployed where and how far your change progressed.

reply

jmvoodoo
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building my own IDE that works the way do (and those in my social circles/professional life do). It allows for use of multiple agent harnesses (i.e claude code, codex, pi, opencode), and makes worktrees much easier to work with. Also has its own code review workflow. My coworkers and several friends have all started using it now. Its been an absolute blast to build, and has definitely increased our productivity vs VS Code, Zed, or Cursor.

reply

asar
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a mobile interface for terminal multiplexers like tmux/zellij/herdr. This focuses a lot on my need to manage agents on the go, it's been quite helpful to myself so far.

MIT licensed and available on GitHubhttps://github.com/AltanS/collie

reply

davidweatherall
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A valorant / cs2 AI-powered aim trainer.

The way it works is you play a game of valorant, or cs2, then after the match you're able to look at the times where you missed your shot, enter our AI aim trainer, and it boots up that exact same moment, with enemies following their exact same pathing, with gunplay feeling as close to 1:1 as possible with the game you're trying to improve on.It figures this out 2 ways:Firstly is purely based on visual clues, I have a custom trained vision model to detect the enemies, and a great algorithm to look at a minimap to infer exactly where the user's position is.Alternatively if the user can download the replay file, we can decode it to grab real time positions / timestamp times etc to perfectly replicate exactly what happened in the match.Posted on reddit / x about this last week, got some positive feedback, here it is if you want to see an early prototype:https://www.reddit.com/r/AgentAcademy/comments/1w965a9/feedb...https://x.com/dWeaths/status/2096683901162824175

reply

Byvrsakjo10
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Antiquity IQ, simple history trivia game, I made the game because I like and am fascinated by history. One of the few things I actually enjoyed in school.

https://antiquityiq.xyz/

reply

AliAbdoli
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://tenjin.sh/
 . It's a knowledge layer for agents so agents stop duplicating work.

Rides Claude Code/Codex hooks and captures useful information, and injects it at need (like when there's an error) for other agents. It works across your team then at a global marketplace layer, so there's incentives for people to contribute.We're in the process of benchmarking and we are aiming for 10% in token reductions. If any team is interested, we're accepting preliminary design partners and can get you started with the benefits.

reply

jkoff
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

My wife and I made a daily guessing game together. Unlike others of the genre that we enjoy playing, an explicit goal of this one is teaching you about the world as you play it. It’s quite simple, using Wikipedia and factbook.json for information about the countries, but it incorporates a few ideas that I think are fun and there’s a lot I’d like to experiment with.

https://countryguesser.jkoff.ca

reply

troygoode
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building Ballad – an inbound marketing engine that runs itself. I'm building it for other founders like myself who don't have a marketing person and aren't going to hire one.

https://www.balladlabs.comMy last company (Courier, YC S19) had great inbound but we never were able to scale it. Ballad plans what I should write, drafts in my voice, publishes to my accounts, and handles attribution so it can feed that into what it writes next.

reply

gfwx
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

A simple weather MCP tool using OpenWeather API. Only requires lat + long to fetch current and 5-hour forecasts. Designed for the free API (60 req/h) but completely parametrized and easily extensible.

https://github.com/gfwx/weather_mcp

reply

slyall
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm doing some programs to use the API for my local bus company to show when buses are arriving at stops. Final step is making it output the data to an external display.

https://github.com/slyall/auckland-stop-display-simpleSome other projects doing similar stuff but I found they were hard to understand (and mostly used an old API that no longer exists) so I (well AI) made mine with small scripts and included curl examples.

reply

rexf
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

working on a convention to organize your own video files on your own buckets 
https://github.com/xta/keepsake

my goal is to offload phone videos (to free up device space) and persist them in self controlled storage. the convention makes this significantly more useful than a collection of object paths

reply

rmnclmnt
 
29 minutes ago
 
 | 
parent
 | 
next
 
[–]

Interesting, been thinking a lot about this recently due to Vimeo crazy price hike for private video storage...

reply

dgellow
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Trying to learn electronics from the bottom up, currently going through „Practical Electronics for Inventors“ (4th ed.). Great book, but not really as practical as the title implies, the base theory chapter is really, really long (but also very interesting)!

reply

pisipisipisi
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Making AppletForge, a modern JavaCard/GlobalPlatform developer experience for secure elements, with the ease of use of GlobalPlatformPro gp.jar and all the modern DX expectations of anno 2026. 
https://github.com/martinpaljak/JCardEngine/wiki

reply

sentinel1909
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Static site generators are super passe in 2026, but I spent the last couple of days on mine. 
https://get-taxus.org

Big re-factoring, I have a data model now and am closing functionality gaps with Zola and the like. Also, I wanted actual documentation. No one else seems to care about that.Check it out! I'd appreciate someone other than me banging on it.

reply

mertenvg
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a better way to do email. Every solution I've seen so far is trying to solve the problem from the wrong end in my opinion. Filtering, privacy extensions, walled gardens, throwaway email addresses.

https://dmcn.dev- an email where you can be sure who it's from. And you get to decide whether to trust it.

reply

chaosharmonic
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Recently:

- I've been tweaking a bot that I built to doomscroll job boards for me, to recycle more parsing logic between target sites. It turns out that, much of the time, I can cut down on DOM-based scraping alotby just parsing schema.org-based JSON-LD. Also casually researching vanilla Web components, view transitions, and Signals in a general effort to make the whole thing less framework-heavy. (Plus it will have side benefits to building the crawlers to have a better understanding of light vs shadow DOM.)EventuallyI need to get to figuring out how I want to handle distributing this local-first app across multiple clients... I've been putting that off for a while, but it kind of crosses over with the JSON-LD thing, in that (even more than it did before I found this) it also just makes a lot of sense to use a browser extension to collect potential matches passively.- 3D printing experiments. I got a used SV06+ a few months ago that turned out to be a lot more finicky than is suited to a first time user... but that was in the course of trying for several months to make plans with a friend that was getting rid of her Ender -- which I then managed to resurrect using all the cleaning tools and tinkering research that I put into my fussier machine. I've since been toying around with a lot of different ideas on how to clean up my workspace and/or fix/reuse stuff I have already (parts trays, Skadis panels, a case for an old Framework mainboard, various instrument stands...) and also toying around on paper with what kinds of printed items I might be able to sell.-Startingon cleaning up a basement that resembles the Research floor from Control. Also a use for the printer, because if I can just print cheap tools out of PLA then I don't have to care about possibly needing to sacrifice them to the mold.- Various Coursera stuff. My state has some partnership with Google for "AI readiness" training, that grossly undersells the various other adjacent topics offered, ranging from cybersecurity to marketing and eCommerce. Stuff where it may be a relevant topic at points, but isn'tthesubject matter.

reply

vmsp
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I've been building a framework for web, ios and android native development at 
https://github.com/vmsp/flypath
.

It's based on the Server-Driven UI philosophy where the backend streams both code and UI into a frontend that just knows how to render what it's told. This is pretty cool because it makes it makes over-the-air updates possible.It also follows the batteries-included philosophy of Rails. Has an ORM, background and cron jobs (all based on Postgres), Django-style migrations, JSX Emails and pretty great FFI that's built around a simple `"use native"` directive, in the React Server Component fashion).

reply

trungdq88
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I was curious about what it would take to build a browser game from scratch with zero game dev experience using AI and created 
https://survive10waves.com
 :) Currently trying to publish the game on Steam!

reply

jascha_eng
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Self hosted database access management, think Code Reviews for SQL Statements for when your devs need to go to prod:

https://github.com/kviklet/kviklet

Recently cleaned up my postgres proxy and built a MySQL wire proxy so that you can use psql/datagrip as a dev but every statement is still logged.
With SSO and no password sharing ofc!

reply

netless
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://stockchat.sh
 - a local stock research app you ask in plain English;
the numbers come from code over SEC filings and daily prices on your
machine, the model only picks which tool to run.

reply

altmanaltman
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

please do not use the "bloomberg for" thing as a marketing phase. You fundamentally misunderstand what the core value of the bloomberg terminal is. This is not it. Its a basic LLM tacked on to financial data. That doesn't make it bloomberg for anything.

reply

netless
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

ok, i stand corrected.

reply

trwhite
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on "See My Spending" - a web app that gives you better insight into where your money's going. It provides real, actionable insights without the use of generative AI. Currently preparing for a launch for UK customers only

reply

djdule
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I am working on real estate management system that do have AI agents 
https://www.aqaris.ae/
. I want to automate mundane day-to-day tasks so managers can have more time

reply

dcl
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Using AI to catch up on reinforcement learning advances, trying to 'solve' Gin Rummy. Will move on harder games after that.

reply

JaviLopezG
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I just published a first version of a gateway that redirects to the correct proxy/frontend

https://yups.ioThe "official" syntaxis ishttps://yups.io/?url=https://twitter.com/WikipediaBut it is very flexible to manage errorshttps://yups.io/www.instagram.com/reel/DdOFgxdlMjv/?stkn=MWR...

reply

davidchua
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Been working on getting my webpage refreshed to try and restart my DevOps/Infra/Fractional consulting business: 
https://cubiclerebels.com
.

Also spent a good part of last month working on a little idea I have that is built on-top of XMPP.I've also been wanting to pickup Gleam, hopefully this would be that week I finally fight through my ADHD to do so.

reply

program
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I saw an interesting article posted here on HN about Go's Swiss Tables implementation. I'm writing a small C library to use them for fun, so you can use any byte array as a key. Either a C string, a number, a bool, etc.

reply

tmilard
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Still working on FPS video game maker : 

https://www.free-visit.net

reply

renegat0x0
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Link manager that is also a feed reader and has search capabilities. Free and open source.

https://github.com/rumca-js/OfflineWebSearchI noticed that it is quite a challenge to publish anything on play store

reply

maouida
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I published a big update to my open source project FluidCAD adding support for sketch constraint solver and assemblies.

I'll continue working on improvements aiming at the first stable release by the end of this year hopefully.

reply

schultetwin1
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building 
https://dipstickalerts.com
.

A way for for U.S. car owners to stay informed about the issues your car may experience that are communicated by car makers to dealerships.I found those communications useful for my own car and wanted a better website that what the NHTSA provides and have been having a lot of fun building out the site.

reply

codazoda
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been building a dark software factory. A system that takes stray thoughts and automatically plans and builds.

I’ve built two (successful) iterations and am now working on the third. They are all very minimal.The main one works well and runs full time waiting for my next idea. The second targeted an open weights model and worked in limited cases.Now I’m working on a more autonomous version. I give it only a goal and a strategy, it decides its own projects.

reply

delf
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on CLI/TUI tool that stores all code collaboration (issues, PRs, etc) in git itself. It lets you publish repositories as static sites to S3 buckets and use them as remotes:

https://gitsocial.org/https://github.com/gitsocial-org/gitsocial

reply

jjcm
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

https://makefaster.dev

I had a bunch of extra Fable credits, so I spent about $10k running autoresearch loops on 200 of the top github repos with frontends to try and speed up the frontend performance. I distilled them down into a leaderboard of the most common wins, and built out an autoresearch loop that takes those learnings and applies them to your repo.Works with your existing claude/cursor/codex sub in a cute custom TUI.I just submitted a Show HN for it:https://news.ycombinator.com/item?id=49687032

reply

mh-
 
19 hours ago
 
 | 
parent
 | 
next
 
[–]

That's such a great idea. Thanks for doing it!

reply

agcat
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Bunch of things: 
1. Building a local ai news feed to learn what's going on latest in terms of technical discussion, research papers, projects - 
https://local-ai-signal.vercel.app/

2. Build a second brain by injecting years of my notes using hermes, luna model and obisidian

reply

richarlidad
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

https://supplementdex.com
 - do ya supplements work? do they?

reply

gavmor
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm decompiling an obscure 1998 computer game using an LLM agent skill that I'm simultaneously developing from papers and books on reverse-engineering (a subject I've never previously engaged with) with the aim of migrating it (well, at least its assets) to the browser: 
https://esoteria.pages.dev

Here's the skill:https://github.com/gavmor/x86-cpp-reversing-skillIt's all slop, but it's battle-tested and producing results. It's quite fun and inspiring to see some of these assets like textures and geometry that are improperly decompiled, bit shifted or something like that. produces a lot of abstract, glitchy art.To make sure that my process and results are reproducible, I've gotten back into maintaining Concourse CI pipelines. They were very useful when we were shipping a fork of k8s for VMware, and now they are a fun way of shipping cyberpunk billboard sprites to Cloudflare buckets.I got back into Concourse in order to attempt a more rigorous approach to generative AI experimentation as well. Unfortunately, there are just so many odd techniques, configurations, loras, and utilities striking my fancy that my experiment pipelines have exploded into the dozens, and Concourse is not a large enough or a high-level enough organizing principle.

reply

sleeby
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a modern is-it-down website checker that checks website statuses from two geographical locations. This was the interesting part for me, to get them working together to avoid false positives. For example, when I check website like irs.gov, ssa.gov and ups.com from Singapore they showed as down but it was only due to datacenter IPs being blocked.

The second probe in Boston fixes this and the site can now say "unreachable from Asia" versus "down for everyone". Many of the existing checkers do not do this and they are prone to show false positives.Site does not use cookies or analytics. Pageviews are counted from the proxy access log. There are 634 curated sites so far.There are no ads either, it's mostly been for my personal learning experience, hopefully others will find it useful.There is even a free API and of course a MCP server.https://downforjustmeoreveryone.comAny feedback is welcome!

reply

ghoshbishakh
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on two things seriously. One is an ssh based tunneling tool to share localhost ports over the internet - 
https://pinggy.io

And the other one is a AI rank monitoring for brands -https://lumirank.ai

reply

desvides
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.windowink.com

Simple digital signage without subscriptions. The goal was to help reduce some of the challenges with updating signage based on images and videos using low cost devices.Started as a side project roughly when the PI3 model B+ was released. It wasn't until PI4 that it felt fluid and functional. PI5 devices are ideal configuration.The memory price increases have made the devices too expensive to be called a low cost solution anymore.

reply

jasiek
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

https://codeplug.org
 - use modern web platform features with historically stable, open-source drivers (CHIRP) to program channels into amateur radio equipment (a web-based CPS).

reply

mickeyvanolst
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a collection of native AI/ML operators for TouchDesigner on macOS. Think of it as a happy marriage between the interface of TouchDesigner but with some of the features you know from ComfyUI.

https://www.patreon.com/MickeyvanOlst/posts/meet-aml-macos-1...Typically TD for the Mac has always been a bit underserved, by leaning into some of the frameworks that exclusively exist on macOS I'm hoping more people will see it as a viable platform for this kind of stuff.

reply

continuational
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a typed, functional-imperative, full stack programming language with IDE support:

https://www.firefly-lang.org/

reply

koehr
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Solace¹, a programming language that targets JavaScript, but is not a superset, like Typescript.
The idea is, to allow zero-runtime-cost safeguards, like Optional Values and Error Unions (syntactically they look like Zig's), decent pattern matching and Traits. There's still a lot of work to do, though, because some of the approaches I went for, don't hold in all cases (generics are tricky).

1)https://git.koehr.ing/n/solace

reply

sokotoz2
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I have released the first version of VentureRanker.

Its basically a tool I made to make my own own business research easier, then decided to formalize it after a friend showed interest. What is it? its a way to evaluate a business idea from multiple angles and perspectives - similar to what a VC would do, only via a simple wizard that asks you to score the business from different angles. The next version will let one or more AIs answer the wizard so you can compare your evaluation with theirs.Two scores come out the other end, kept deliberately separate — how good the opportunity actually is, and how good a fit it is for you specifically.https://ventureranker.com

reply

unprovable
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Open source quantum hardware with Quantum Village in donated lab space at a London university. Pushing the boundary for Entropy Loop, a QRNG to make it faster and more enteopy, and the Uncut Gem redesign, our NVC diamond based quantum magnetometer.

reply

joddystreet
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

[HYBRID]

Eylo (a take on Hello) a voice first agent platform, multi-tenant, focused on B2B2C use-cases -https://github.com/DigiCred-OSS/eylo-osIt’s a distilled fork of a closed source product that we are offering to our customers.

reply

oliaukus
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

A rag api to power better, more tailored ai features in saas products. By default it indexes customer websites, but also supports notion, YouTube, email and custom connections. 
https://www.context-link.ai/for/white-label-rag-api

reply

cristodcgomez
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

https://solanda.federa.social

A new UI library made with zero dependencies (native web components). I just made it public as I actually use it for my personal projects since past year.The core principle is to help with UI development without bloating a project. It works with vue/nuxt (tested, my projects are done with it), but also react/angular/svelte/etc.One feedback I got from reddit (I published it this week there) is that AGPLv3 may be a problem for adoption... still not sure if should I use MIT.

reply

dbz
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I have been working on cost models and coupon ladders for businesses.

If either of those are interesting to you, please reach out!For example, I am helping some restaurants learn exactly how much each item on the menu costs, what the margins are, and how much profit each dish is bringing in because I integrate with their PoS system.https://imgur.com/a/C127GOYIt's all a part of GetSetReply which is turning into a small suite of tools for SMBshttps://GetSetReply.com

reply

thecolorblue
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Keel is a productivity app that combines todo lists, pomodoro, and an AI executive coach to let users go through a whole plan > execute > reflect cycle in the app. The AI agent (text or voice) can help with planning and guide reflection, but it generally does not do work for you like other chat bots.

The android app is in beta now and the iOS app is in development.https://keelcoaching.app/

reply

Team1
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I just released an open-source AI pipeline that turns GitHub issues into merged PR's.
It uses your Claude Code CLI subscription.

Looking for feedback from people who already run Claude Code and are testing out new AI software factories or tools.Try it herehttps://github.com/Team1-dev/Team1-FactoryPlease only run this on a VPS or isolated environment and not on your personal machine as it runs with full permissions.

reply

nevster
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I spent way too much time doing fancy infographic-style stuff for a video about the 4th book in the Wheel of Time : 
https://youtu.be/ONs2inKELR0

Meanwhile, Daniel Greene's dodgy whiteboard video has a million views. Don't mind me as I eat these sour grapes...

reply

freakynit
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

https://snippetbox.stupidlabs.lol/

Snippets manager. Fully local, 100% free, ~5MB binary. Open-source.AI-assisted development. Not vibe-coded.

reply

wklm
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Web bluetooth for ios (via safari extension). It's already way better than any 3rd party browser available in appstore.

https://beacio.com

reply

Byvrsakjo10
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Antiquity IQ, a simple history trivia game, I made the game because I like history.

https://antiquityiq.xyz/

reply

MelonUsk
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

We modeled the ultimate future in 6 years and now share the technology how exactly to get there safely

effectiveutopia.org

reply

pryelluw
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

My funny essays newsletter on substack. Link to latest post: 
https://yelluwcomedy.substack.com/p/the-fascinating-world-of...

Please let me know if you enjoy!

reply

tha_infra_guy
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Haven’t see a lot of app in this space but most of them focus on wastage rather than usage so I am playing around with 
https://usurp.onrender.com/
 the idea is to challenge friends based on time spent using an AI coding tool, thought was more like what wakatime did. It’s also open source.

reply

kilroy123
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm trying to build a tool site that has all the tools you'll ever need. I slowly add some each week.

https://allthedamn.tools

reply

backtr4ck
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Why reinvent the wheel? 
https://github.com/sharevb/it-tools

reply

wreet
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I got laid off at the beginning of last month so put a little time into some personal projects I thought might be fun.

https://dstld.news- I have always wanted a personalized news site so I built one using a few news APIs with AI summaries.https://hn.wreet.xyz- I'm a big fan of skeleton.dev and wanted a HN frontend with all the fun themes.Nothing too exciting, just trying to find the joy in making again.

reply

Areading314
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

QuickMDSim - An easy way to run molecular simulations in the cloud: 
https://quickmdsim.com

This simplifies the setup for researchers who want to simulate materials science problems like battery electrode performance on GPUs with a simple usage-based pricing model instead of traditional HPC

reply

tornikeo
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

https://peachjam.dev/

The cheapest possible lovable alternative with all the features. Currently in alpha.

reply

w_t_payne
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Agent-first engineering infrastructure:- The "OS" for sovereign re-industrialisation.

The systems engineering V-model provides us with a general-purpose approach to solving difficult problems. It comes with an array of proven and trusted standards and document-oriented processes.Given the number and detail of these documents and processes, automating some realisation of V-model is almost trivial. Tools like Codex and Claude Code are hardly less reliable and trustworthy than human engineers, and the existing standards already contain ways of mitigating the impact of imperfect work performed by error-prone agents.The generality of this "Autonomous Systems Engineer" gives it a genuine claim to be something approaching AGI. Certainly it enables us to tackle much bigger and more challenging problems than we could with only the LLMs on their own. (Yes, it's "just another harness-of-harnesses", but that doesn't mean that what it can do isn't significant).In addition to providing automation of high-integrity engineering practices, my project also provides a disciplined communication layer that sits on top of A2A or other similar protocols, enabling small agent-first engineering organisations to exchange well-defined highly-assured documents and accelerate b2b collaboration - enabling "swarms" of small, agile businesses to take on larger and more demanding challenges than they would be able to individually.

reply

monster_truck
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Still working on my traffic simulator. Pushing up past 62500 updates per tick on 16 threads, just barely enough for 512 cars with full tire/drivetrain/suspension/physics kernels at 120hz, or a great deal more at increasingly slower rates (down to as low as 6hz) with fractional amounts of fidelity.

reply

mdbug
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://jeden.day

A habit tracker that allows for more flexible goals than daily ones, such as N times per period.

reply

_bramses
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm hosting an book club themed event calendar for New Yorkers!

We also have an official meeting once a month to do book club matchmaking in person.https://www.commonplace.nyc/

reply

dogas
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on slk (
https://github.com/gammons/slk
) which is a TUI Slack client that runs in a terminal. It's super fast, keyboard-driven, and it's been my daily driver for a while now.

reply

Sau1707
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/xLongLink/longlink

Think about GitHub, but for processes and data.

reply

backtr4ck
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm using fable to find an exoplanet. Know nothing about it but have several TBs available in my server for data and a powerful GPU for processing so let's see what I can do with it.

reply

stuartmemo
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Still hacking away on Raygum - a nice place to keep your music brain.

I don't even know what that means.https://raygum.com

reply

kunley
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

Raygum appears to be refreshingly nice place! Thanks

reply

stuartmemo
 
1 day ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you! Feedback encouraged!

reply

MomohNobert
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I've been working on 
https://pronto.stream/
, I wanted to mess around with MCP and building a world news system to power the decision making and surveillance of other systems I would likely curate.

I was curious about formats more efficient for agent communication than JSON and also proving if the framework I curated could handle the load and traffic.It's been really fun to observe.

reply

inoop
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I spent some with reverse-engineering a neural network accelerator (NNA) inside a Chinese WiFi camera SoC: 
https://github.com/inoop/t41-pluto
. I used Claude to reverse-engineer the hardware, and then implement an ONNX compiler and runtime so I can run my own models. Basically I now have a $20 AI smart camera.

reply

autotune
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Contributing larger PRs to terraform-provider-aws because apparently my contributions so far do not have enough lines of code as a metric. Getting familiar with Floci for usage with Terraform over LocalStack since it is a true open source project rather than freemium. Also getting my AAS from Maestro. Ride or die since I can not afford college anywhere else despite their current accreditation issues with COE.

reply

cyan_indigo
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building 
https://voila.show

Video proof of work for coding agents.Agents upload a short recording of what they built, humans leave timestamped feedback, and the agent can retrieve that feedback and iterate.Basically, instead of an agent telling you "done", it can show and you have a nice way to share the resulting videos in PR, on Slack, with your teammates etc.

reply

richardreeze
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I’m working on a 52-part series about retention.

Each week I research one part of retention, teach it, and apply it to two real-world products I built.I’ve published five lectures so far, and think the series should be useful to anyone here building a product:https://www.youtube.com/playlist?list=PLFp5nmjrQeug

reply

gavinhoward
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Not something I'm working on, but want to: a competitor to Perforce that will be cheaper and easier.

Unfortunately, I'm not sure that being better is enough to compete, so I'm sitting on it for now.

reply

sim04ful
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

https://fudge.design
 
Gives AI agents better design taste by enabling them search for references.

reply

stevejhiggs
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

https://videofn.com

I like to make videos involving lots of kinetic text that is synced to audio but they always took ages to make. This was an experiment in ai assisted video editing with a strong feedback loop so the agent can self correct.It's also my exploration into using local models and rendering to keep as much as possible on device. Over time its grown into something pretty useful so I decided over the weekend to release it generally.

reply

lucas_the_human
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Inbound message AI assistant. Triage all incoming LinkedIn messages, link to email chains, handle scheduling and back and forth, drafting replies, etc.

I'm currently in a job search and wanted to automate it for myself and learn the AI stack.If anyone wants to try it out lmk!

reply

hienyimba
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

https://Webvetted.com

It’s an AI Private Investigator that does the hard work of data gathering (using Open Source Intelligence) and correlation. Used by over 70k investigators including government agencies.

reply

danbrooks
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Just gave it a look. Turns out to be a paid service after a bunch of clicks.

reply

faceless3
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Cranpose - Rust GUI with jetpack Compose API 

https://github.com/samoylenkodmitry/Cranpose

reply

NoNewsIo
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

NoNews (
https://nonews.io
) — a signal radar for Chinese-speaking readers (bilingual EN/ZH).It reads official and first-party feeds directly (Federal Reserve, SEC, ECB, DOJ, CFTC, ArXiv, GitHub releases, GDELT), clusters duplicate coverage into a single event card, and measures how far ahead of mainstream coverage each signal lands.Every card links back to the original source; no full-text republication. Lead-time stats are accumulating into a monthly index.Early days — feedback welcome, especially on which sources and boards matter most.

reply

garymiklos
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I am building OtaKit.app, a cheap, fast, and simple CDN-based over-the-air updating tool for Capacitor apps (and soon for React Native too)

reply

gburgett
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

A local AI-adoption consultancy business for SMBs where the differentiator is I physically show up at your office and actually talk to your team. With the slopification of cold outreach and social posting, I think the future of business development is going to be very personal.

https://dfwfractionalfde.com

reply

smadam9
 
20 hours ago
 
 | 
parent
 | 
next
 
[–]

How's your experience been with this so far, especially in the DFW area?

reply

montenegrohugo
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

recently built a board for escaped AI agents to coordinate. you can post via GET (lol)

https://swarmmemo.com

reply

scientifik
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

An app that lets you view social media without ads or algorithms.

https://narro.infoYou add profiles from Instagram, X, TikTok, LinkedIn, Facebook, or YouTube and Narro pulls in the posts.

reply

mateioprea
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

i'm not building anything public, but i started learning rust recently and using zed's gpui for building native apps. i've built a few apps for my wife but then i got stuck with nothing to build. so maybe there's a chance someone needs a non vibe coded desktop app maybe we can work something out (email in my profile)

reply

fhub
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Because my work life is mostly LLM promoting, I’ve gotten back into hobby robotics, which I think has a low chance of LLMs taking over anytime soon. Designing and building a robot that can build a wooden hardwood deck using the edge-screw method.

reply

nahsra
 
20 hours ago
 
 | 
parent
 | 
next
 
[–]

I'd love to hear more about this!

reply

mhog_hn
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

we are building 
https://www.d5s.tech
, using our own software to automate our own company (the boring bits)! having a blast doing it and steadily automating more and more

and... whenever i have some spare gpt-6 astra left i am working on a R.U.S.E reimplementation alongside some other threejs experiments

reply

manoji
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

https://atlas.trentsoftware.in
 . An AI agent for enterprise integrations .

reply

cameronsjo
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Compute is precious, so I’m building a k3s/k8s-based macOS/Linux GitHub Actions runner.

I’m spending like $25/mo at least in GHA minutes.Then working on securing and tinkering with my homelab. And little utilities that make repeated deterministic functions easier for me and agents.

reply

Cider9986
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

What steps are you taking to improve its security?

reply

sphyrna-029
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Chatter, a self hosted almost feature complete alternative to Discord: 
https://github.com/Sphyrna-029/Chatter

reply

RagnarD
 
18 hours ago
 
 | 
parent
 | 
next
 
[–]

What was your motivation for that, since Discord is open source?

reply

sphyrna-029
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Is this question an AI litmus test?

reply

Cider9986
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

How does it compare to Fluxer and Stoat?

reply

sphyrna-029
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

At the time of starting the project, stoat did not have screen share capabilities. This was a non starter for our community. Fluxer looked promising, but quickly became overwhelmed by the self hosting docs. Chatter is for small to medium size communities that don't want to spend more time maintaining their app than using it. With chatter you forward a few ports, fill out the compose file, and you're set. Chatter is also a PWA, no native client updates to worry about.

reply

spreadsheettria
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Built a small free thing this week: a "Spreadsheet Triage Checklist" — 7 common ways ad-hoc spreadsheets quietly break (stale copies, silent formula errors, no version control, etc.) and the order to fix them in, since fixing them out of order usually wastes the work. Came out of watching non-technical teams patch the same spreadsheet for years instead of ever stepping back. Still figuring out if this is a "checklist" problem or a "just use a database" problem — curious which camp people here fall into.

reply

lumpycustard
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

A web app for saving internet recipe pages that strips out all the crap.

https://www.recipunk.com/

reply

oxi113
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Last month I've finished the reverse-engineering of the original WON-era Half-Life launcher from 90s (
https://github.com/oxiKKK/re-goldsrc-won-launcher-1792
).

This was an interesting thought experiment for me, because I always loved reverse-engineering old games (Half-Life in particular) and restoring the original looks and properties of the code.In this project I tried to use LLMs extensively to reverse the code for the first time to bring it back to its original potential look. Frankly, it worked and the code is now available to the public.

reply

keithnz
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

a replacement for Octopus deploy 
https://rolloutrhino.com/
 (marketing page is mostly a placeholder). Octopus is super expensive for our company and scales poorly if you have lots of small projects. I've got pretty much everything working really well, and the main thing I'm working on is improving the UX for all the workflows I do most often. It is mostly built around what I wanted from the tool, but before I release it I'm looking at supporting various other ways people use the tool. It's been a fun project so far.

reply

arsentjev
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

All in one platform for hosting agents

https://cantelop.com/- Minimal setup
- Any agent harness
- A session is an actor
- Opinionated infrastructure
- Performance on the critical path

reply

recurser
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

https://bossanova.dev/
 - a session manager for Claude Code and Codex that adds automation and orchestration features.

I've been working on this on the side for around 5 months, initially to scratch my own itch, but recently some friends and colleagues have started using it too.- Lightweight Terminal UI written in Go
 - Control chat sessions via native Claude Code or Codex UI in a remote browser
 - Identify and surface questions from multiple agents at once
 - Cron jobs for automation
 - Share remote coding sessions between team members
 - Auto-repair PRs
 - Auto-rotate subscription accounts
 - Allow agents to send messages between chat sessions and across model providers
 - Register Github callbacks so agents can respond to CI events in realtime
 - Run agents on a mac mini or similar, and control them from your phone while you're on the go...and a bunch of other stuff. The goal is to organize chat sessions and provide the agents with primitives so that they can communicate with each other between sessions and providers, over local networks or the wider internet.

reply

gregsadetsky
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

A few side projects!

- an open source AES67 hardware receiver/decoder - based on my friend Jessie's work [0]. I want speakers to have ethernet ports and to use an open/inexpensive stack. it's hard because physics/timing are brutal (1ms sync is ~not enough), but that's what makes it a great problem.- an open source embroidery machine - based on my friend Owen's work [1]. Owen found Brother PE-150 machines which are readily available on eBay for ~$100 as they only work with proprietary 90s-era CF cards which nobody has (or sell for more than the machine). he designed a replacement motherboard (!!) and is running a fully open stack. it's wild.- a ~$20 tiny cute display you can have on the side of your monitor, and display things on - realtime airport view from flightaware? a mini terminal? you can grab a display today [2], all that's missing is a 3d case (email me for firmware/OS code! I'll share it, just haven't had time). friends Frank and Sophie are working on a similar GUD-compatible display as well! [3]- my friend Antoine has been working on Python bindings to Canonical's dqlite, a distributed sqlite-variant with raft-based failover and transactions (only C and Go clients existed) [4] - this will soon be a structural ("load-bearing"! haha!) part of Disco, a project we've been working on for a few years which lets you run your own PaaS. we're growing and get nice love letters [5] which for an open source project is obviously deeply rewarding[0]https://jessie.grosen.systems/projects/aes67-receiver[1]https://owentrueblood.com/blog/2024/12/10/reverse-engineerin...[2]https://www.waveshare.com/rp2040-touch-lcd-1.69.htm[3]https://bsky.app/profile/sophie.engineering/post/3muxysxhpck...[4]https://pypi.org/project/dqlite-client/[5]https://infinitedigits.co/disco/

reply

Sachinrao
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on simple timer app for students prepping UPSC an prestigious govt exams in India

reply

pianopatrick
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I worked on my AI agent that feels like a unix util. This month I changed the way it writes and edits files

https://github.com/patrickjh/ssa

reply

enjoyyourlife
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I've been working on 
https://searchforjobs.app/
 I'm trying to add the resume creator for using the right keywords for a job posting. I'm also trying to add more data visualizations are more job posting sources to scrape.

reply

steven123
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Build one of the best emoji sites there is.

https://emojistime.com

reply

moinism
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

AI agent for content creators 
https://chatoctopus.com

reply

lapkaaaa
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

- i dropped a neural net jane street puzzle (
https://huggingface.co/spaces/jane-street/droppedaneuralnet
) very good mindbreaker, learned a lot of new things on the way

reply

tomerbd
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

rexide, i use it for voice to text, and multi terminals with claude code and codex etc - 
https://rex.mindmeld360.com/

reply

pdyc
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

working on adding webmcp support to my new free tool 
https://easyanalytica.com/tools/gsc-insight
 , webmcp was recently added to codex desktop app and it would be interesting to see how users use it with ai, would it get good adoption or it would just go away.

reply

YoucefHQ
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

The 2026-27 soccer season just started.

If you love catching up on highlights, checkhttps://thepelota.tv/It’s like Netflix but for soccer highlights, with all the major leagues in one place as soon as they are available on YouTube, all free and no ads.

reply

mstkllah
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

Where do you source the lineups and match data from?

reply

YoucefHQ
 
1 day ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I use this Highlightly's API 
https://highlightly.net/

reply

le-flaneur
 
1 day ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Simple and does what it says on the tin. Nice!

reply

YoucefHQ
 
1 day ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you so much. Let me know if you have any feedback :)

reply

absoluteunit1
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Building 
https://typequicker.com

It's a personalized & data-driven typing application that targets your weak points

reply

vira28
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

An analytics store for Postgres on S3 using DuckDB as the query engine

https://github.com/viggy28/streambed

reply

animatronix
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a note app for my studies, i dont like electron based apps sot I'm building it with rust and gpui.

reply

Retr0id
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Reverse engineering the hardware and firmware of a Sony A7 IV camera.

reply

steinvakt2
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Greenlight social.
It's basically an app for saying "I'm ready" or "Let's do x...".

Background is that my friend group plays video games, grabs beer or whatever - and a lot of the communication revolves around logistics. This app lowered the threshold for initiating. We create a group per activity, and "going green" means you're ready. The other group members get a push notification "Paul is greenlit!" and the title of the group is "Play Dota 2" or "Beer at local pub". Super simple concept, but it actually works.TLDR; I made an app that let's you press a button instead of writing the typical "Does anyone want to join x activity?"https://apps.apple.com/no/app/greenlight-squads/id6757295236

reply

corvad
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

A microkernel os 
https://github.com/corvad/os

reply

medbar
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Just started:

1) bad apple on my kernel (OS)2) language model + inference engine from scratch3) sketchdaily.net, but you give it your own pinterest board of references instead of the preselected ones they have

reply

madduci
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

A FHIR Validator and Snapshot Generator that works offline and can communicate with the German national Terminology service

reply

amboo7
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

RSS Bot for Telegram: learns what you like, searchable, using free models (vibe-coded): 
https://github.com/amb007/rss-bot

reply

gicssalada
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building editor and flasher for BMW engines maps (n13, n20, n55, s55, b58, s58) and TCU maps (ZF8HP45 and ZF8HP50) as well as a remote access ENET IOS and Android app.

reply

pksunkara
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a code forge that can work offline for the collaborative stuff. 
https://juju.bi

reply

tweedler290
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I made a code intelligence system from scratch! language agnostic and model agnostic. runs locally. Benzi is a compiler+harness+runtime tracer/debugger built from ground up to write code as neatly as it understands it.

78.2% on SWE-bench verified for < 10 cents a fix + benchmarked against Claude Code, Open Code, and Deepseek Harness. Benzi is far cheaper AND faster. sounds like marketing fluff but just check it out please.github landing page:https://github.com/oooscoos/BenziInstant callflow/dataflow/controlflow lookups on any codebase for any AI model - you can see how huge this can be rite?

reply

sinaatalay
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Generative UI for education

https://academa.ai

reply

heychristoph
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Don, a work companion.

Don helps you set goals.Don reminds you to take breaks.Don checks in how you fell.Don judges you when you go off track.Don celebrates you when you get stuff done.https://donethat.ai/solutions/productivity

reply

msejas
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a GDPR compliant, privacy first, AI self improvement app.

I've paired with a psychologist and HR director from one of the best universities in Germany to leverage the fact AI has embedded within every human experience, personality types, shortcomings in recorded history among all languages, and all cultures, and we are trying to extract that knowledge and leverage it so we can analyze what makes you tick (for example being an introvert or extrovert to recharge your social battery) in every aspect, motivation, procrastination etc.Analyzing solidly your profile in a sense those standard 'form' 1-5 tests can not capture.Once that's done, we give you recommended activities to improve your weak points (perhaps asserting yourself a bit more if you tend to shy away).The core things we are trying to solve is:human coaches are limited by their own worldview and bias, we hope AI who has more knowledge to other human experiences can help you more.Anonymity, we are full GDPR compliant with audited log table if any user access your records, we hope humans feel more at ease without the fear of being judged.Accessibility, a single mother drowning with responsibilities doesn't have time or resources to evolve spiritually, we hope the accessibility and price point of our app solves this and helps people who can't hire coaches have a more meaningful life.Most of all I want to use my skills to improve human lives, I've been working very hard on it.We are near a beta launch, where it will be free for beta users, if you are interested please email at: martin.sejas@exara.ai

reply

darkhorse_chenn
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

i have been working on like a different project like since recently TALA has been opensourced , i analysed how it constructs flow using dag after installing it on my linux , , i thought like why not we train a local ollama model 1.5 b parameters and make it generate tala code ,so i can develop flowcharts which we can get in mermaid ,napkin which we use for hackathons , but the problem is collecting data , i cloned official repositry of d2 code and i only received 79 code snippets , idk how to train with less amount of data m and still searching on quality data than generating synthetic data , anyone any ideas? , or its not worth it

reply

hypendev
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Hypen, a crossplatform framework for building & streaming native UI 
https://hypen.space

It lets you build apps and features that work natively across web, desktop and mobile, streaming from your backend into your client app, letting you deploy changes instantly.A Hypen client can be any app that includes Hypen SDK, letting you render apps inside apps, build backend-driven features or create a mini-app platform like WeChat.The framework supports many languages, such as TS, Rust, Go, Kotlin, Swift and pretty much any language that can run WASM or interop with native.--To give you a taste, some things in the upcoming release changelogs are:- Performance improvements brining the web client on par with React (even faster in some cases)- Exposing states and actions to agents, letting agent drive the app directly instead of through UI- First class drag/drop support with pinning as a primitiveAnd some recently released things:- First class accessibility support, with out of the box inference and minimal intervention- Animation support with simple DX for animations, scrubbing, state and screen transitions- Video component and a whole Netflix clone Hypen app example- UI Testing suite so you can easily preview how your app looks like across devicesNext up on the feature list will be device communication and permissions, Android TV support, theming and external component installation, letting you build shared component packs and primitives.

reply

anacod
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on an open source graph of physics equations, quantities, and their connections to each other, to help learners connect concepts: 
https://anacoda.github.io/OpenFormulaGraph/

reply

josebmneto
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

https://mergi.dev/

I'm working on Mergi. The demand for reviewing PRs sky-rocket in the past months, and I got really tired of Github slowness so I created my own "native" fast and painless UI where everything is pre-loaded.Also added a bunch of cool features like a Review Queue to keep track of everything (there are weeks I had to review 12 PRs) and some cool AI features.

reply

victorpudeyev
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

This weekend, making a clone of 'clash of cars' 
https://www.youtube.com/watch?v=umD_Y-1nz_8
 if only just the conceptual basics

reply

mattvr
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Optimem, a spaced repetition learning app that aims to be a user-friendly alternative to Anki. Or a more effective version of Duolingo.

https://optimem.org

reply

Cider9986
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Have you heard of comprehensible input? Seems to be better for languages.

reply

mattvr
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes! I’m working on adding that to the app in the next update.

reply

0gs
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

i am working on a really cool word game that has a TUI graphical style, it looks like a roguelike but has a bit more going on. i also seem to have figured out a way to do automated "fun factor" testing and get bugs/frs that sound like real player feedback, as a little bonus treat. doesn't seem like anybody is attempting that kind of thing with agents, might try to codify it. trying to spend a lot longer thinking about a game's systems/meta and developing slowly vs. hypersprinting which is fun but exhausting.

reply

jvanderbot
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Nothing to special, but I made a workout tracker that allows me to only log a standard, scored workout.

This solves exactly n=1 user's issues: I tend to fall off the workout wagon without public accountability and when I dont get scores to improve onand especiallyto degrade and dillute my gym trips to the point of ennui.It's free and public until it breaks:https://aft.jodavaho.ioMy progresshttps://aft.jodavaho.io/track/46B8XWPCVK5MVS35R8X53Y8KY5(heavily helpd by AI on the frontend - I am terrible at it)

reply

integricho
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

You surely mean 'what your claude agents are working on'?

reply

reverseblade2
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

https://3dpack.ing

Online container planner in 3d

reply

seanmcdirmid
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm further along in my funemployment project:

https://github.com/mcdirmid/cleanroomSo far I have bazel macros up that can produce tested code with a ~30GB MoE model (Jundot/Qwen3.6-35B-A3B-oQ6-mtp, I can get ~90 toks/sec on a M3 Max!) using cleanroom separate implementation and test development (and then comparing them until both are correct). Over the last month, however, I found that my bottleneck is in the specifications: as I further divided my components into separate parts (since smaller components are easier to write and test), I started hitting problems with specifications becoming badly ungrounded (code depending on knowledge they cannot access, so something is just hallucinated).So I redid the format, e.g.https://github.com/mcdirmid/cleanroom/blob/main/update_with_...The spec format is designed to be declarative and very modular, and ya, an LLM is primarily writing the specs as well, so I hope to create some sort of formal reasoning framework that the specification can be translated into (by an LLM) so that ungroundness feedback can help the LLM write better specs. Also, I found that it really is much more robust to change/refactor/add features via the spec first and then align changes down to test and code, then to make changes to the code directly (even without using the system, just asking a frontier model to look at the guides and do the alignment itself directly).I think I'll be ready to do a release over this next month, which means:- Supporting a build system other than Bazel to express DAGs. Honestly, this could be anything, I just chose Bazel for convenience (easy to express graphs in Starlark), but it assumes a monorepo world that I don't think many developers use.- How do I even package this? The advance of using Starlark is that I can generate python code to call into the generated python code directly. If I move away from that, I need to figure out what this really looks like as a binary.- More demos. Right now my only project is the code for the system itself (the classic "the first program of a language is the compiler for the language"). I just can't think of many interesting things to do in Python that aren't agent related (I can support other languages, like Java, Typescript, or even C++, but I'm hitting choice paralysis).

reply

piratebroadcast
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

An Openclaw, Hermes Agent type system that is meant to be ran on a home server, built in Rails with a Tauri 2 front-end.

reply

jessegrosjean
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A new version of my app WriteRoom, after 16 years!

reply

Jeff9James
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

twent.xyz

Twent = Android AI Agent that uses your phone, connects to stuff, installs skills & MCP on-demand, remembers things, and is highly proactive.

reply

thomasjeff1
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

On a mission to prove you don't need YC to be successful.

reply

bc3mc2
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a p2p streaming/sharing app called bubbleBASED. Its here 
https://bubblebased.com/
 its based! on bubbles! But it uses Webtorrent to stream and share content in context bubbles. You already need peers for a social network—so why not use those same peers to seed the media? like a closed loop and it cuts out AWS because everyone is a peer for everyone else in your bubble. There is an assist from Heroku and Pinata. There is no algo. Its just whatever you post. Also you can add an affiliate link (from cj.com) and it will pop in a platform ad for you so there is a revenue possibility there. The streaming part was intense - I built this because I wanted to see if browser-to-browser streaming could actually work for small, private groups. The broadcaster records via MediaRecorder, chunks every 8 seconds, seeds each chunk via WebTorrent, and viewers assemble them with MSE (or ManagedMediaSource on Safari). There's a server-side "always-on peer" so streams don't die if the original tab closes.

The interesting problems were: MSE on iOS Safari, chunk continuity across peers, and handling rotation metadata that iOS bakes into the video stream. Also, the tracker is a separate bittorrent-tracker instance because the built-in WebTorrent trackers are unreliable for sustained swarms. Also i used a ton of graphql, so normally with a torrent you have to kind of let people find you but i used a graphql subscription to TELL people what the magnet links were called so they can fetch them asap. Lots of shortcuts like that, its been interesting!!

reply

bc3mc2
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

also if you want to be a moderator in this bubble i just set up feel free to join and invite cool people - 
https://bubblebased.com/join/6DA65DC2C7552A43
 i want to stress test this thing.

reply

fl4tul4
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm learning on how to move away from computing into violin making and repairs.

reply

itake
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Trying to reduce my doomscrolling IG and FB usage

I createdhttps://getnoloop.comto block the feed on iOS

reply

patrick_rtk
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

i'm working on rtk.

https://www.rtk-ai.app/

reply

rspoerri
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

lexera, a kanban board with full multimedia and document include support that saves to markdown, exports to marp to manage teaching materials. it also started out to be my editor of choice for agentic programming as each task is a card. hopefully i will manage to create a page and visible materials soon!

reply

YuechenLi
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Lots of things really:

1. Aetheris: geometry CAD kernel,https://github.com/yuechen-li-dev/Aetheris/.Full code CAD capability with big coverage already and some functionalities that even OpenCascade/Parasolid/ACIS doesn't have, full sheet metal module, programmable part assembly, analytical fillets/chamfers, mathematical knots, auto-route for piping, built-in finite element analysis, etc. Had Astra make an improved version of the V8 demo that was going around on LinkedIn, so it can do general hard surface modeling pretty well too, turn all the Astra demo prowess into reusable capabilities/templates. The DSL is human writable too, so give it a try if you want.https://aetheris-editable-v8.yuechenli.workers.dev/2. Concept language:https://github.com/yuechen-li-dev/ConceptI've said before that Carbon isn't a real programming language, never mind a successor to C++, so I decided to put my money where my mouth is. The idea of it is to be more TypeScript to C++'s JavaScript and to generalize C++20 concepts from template constraints to what C++26 is doing with contracts, and bring the equivalent of Rust's borrow checker to be opt-in by default instead of opt-out, fast compile time, in a syntax that C++ users are already familiar with (`const auto` instead of `let` for example) as well as templates and comptime. Language is done-ish, not self hosted yet, still compiles to C11, kernel and allocator libraries are finished, currently working on the scheduler right now.3. Copeland TS,https://github.com/yuechen-li-dev/copelandTypeScript for .NET without all the weirdness of Javascript, with full Nuget and NPM inter-op, Rust style exhaustive `match`, templates, etc. It's actually weird how much cleaned up TypeScript ended up looking like cleaned up C++. Compiles to JS, C#, WASM via Blazor WebAssembly, and SPIR-V via HLSL/DXC, and runs on V8 for JS and RyuJIT/NativeAOT for C#. The conclusion is that RyuJIT ended up being ~2x faster than V8 JS in hot loops but the cold startup time is higher, so replacing JS for UI really isn't worth it. Comes with full UI layout system, Vulkan renderer, and game/app runtime, but those are still pretty rough.

reply

alentodorov
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

api for building apple and google wallets. launched it after ppl kept asking for one on the consumer app (launched on hn too) and gave it a shot. now it does enough mrr that i dont have to go back to work.

*walletwallet.dev

reply

matheusmoreira
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Writing an article about compacting garbage collection for my website.

reply

brynet
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Making rent as an open source developer.

Desperately trying to attract new monthly sponsors and people willing to buy me the occasional pizza with my terrible HTML skills. Is it working?If any individuals, companies (or bitcoin millionaires) would like to help a long-time OpenBSD slacker, unslack, I'd really like to focus more of my time on open source development (and advocacy), rather than making rent. Feel free to contact me.https://brynet.ca/wallofpizza.html(Native SegWit): bc1qwe6zv0ezq4gzlea6tw45qhsn5kckheljn0krvt

reply

girish_r
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on SpecPilot (
https://specpilot.dev
), a spec-driven development layer that sits in front of Claude Code, Cursor, Copilot and the rest. It deliberately doesn't generate code. It scaffolds a .specs/ folder and hands the actual writing off to whatever agent you already use, so the specs become the thing the agent is held to instead of a prompt you retype every session.

Open source, free, no login, nothing to sell. I'm not trying to build a business on this. I just want agents to write better code, and that only happens when they have something firmer than a chat prompt to work against. CLI is here:https://github.com/girishr/SpecPilotIt started as a TypeScript CLI in January. Enough people told me they either didn't want a CLI or didn't know how to use one that I rebuilt the front door as a guided chat: 27 questions, runs fully offline in the browser, outputs the .specs/ tree plus an onboarding prompt for your IDE.Recently shipped an MCP server so the agent can run the questionnaire itself rather than the human doing it, published to the official MCP registry and Smithery. Next is brownfield: point it at an existing repo and backfill specs from the code.
Honest state of things: the Product Hunt launch got 4 votes and around 100 visitors, and I had no event tracking wired up, so I couldn't even tell how many of those generated anything. Fixed since. Usage is small but real, and it's coming through MCP rather than the web app, which I did not expect.The part I keep circling back to is that spec generation is easy to copy. Spec enforcement is where the value is: checking a diff against the spec and failing loudly. Feedback welcome, especially from anyone who tried SDD on an existing codebase and gave up.

reply

GarnetFloride
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Baking eggless applesauce oatmeal cookies and chocolate chip cookies.

reply

totemandtoken
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I haven't been working on it as of late, mostly because i'm a bit deflated from software in general, but I started working on a programming language I called Grasp.

If lisp is a list processing language, grasp is a graph programming language.The idea was that most other data structures can be represented with a graph ( adjacency matrices are matrices, a tree is a type of directed acyclic graph, a list is a graph where each node connects to at most two nodes, etc) and so if you designed a programming language where the language is itself a graph, much like how lisp is itself a list, you could get other esoteric programming languages like APL, forth, lisp, and so on as DSLs of Grasp. Also any program you write would be its own CFG.I started it but honestly its mostly a hot mess of vibe-coded garbage. But I may get back on it and try to clean it up.

reply

kazinator
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

A number of mainstream Lisp dialects including Scheme and Common Lisp support a notation for encoding graph structure, with shared substructure and cycles. It's not always well-defined to use that in writing code (e.g. a program with cycles in its source code might work as intended with interpreted, but then a compiler chokes on it), but in literals it's always okay.

reply

gafferongames
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working with multiple AI models helping them create tools that help them work together efficiently. 
https://github.com/mas-bandwidth/nova-tools

reply

daugasauron
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

https://daugasauron.com/

Not sure what happened sort of became something docker ish in wasm, complete slop, fun to watch agents play games against each other. Wish I could afford a complete fable vs astra showdown in seven kingdoms.

reply

azaras
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I am learning math logic and two languages to use it: TLA+ and Lean.

reply

FloayYerBoat
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I released my free 1-4 player card playing app:

https://cards4play.com...and I am working on adding Euchre and hopefully (eventually) Bridge, after I learn how to play myself.

reply

yu3zhou4
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I study stats and probability

reply

IvyMike
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I took this existing 3d printed animated Frankenstein head: 
https://www.printables.com/model/620191-frankenstein-head-wi...

... and used Claude to crank the software up to 11. Network management console, RESTful API, added hands hands to the pupils so it serves as a clock, NTP, added sleep mode at night, added different eyes, OTA firmware updates, and more:https://github.com/michael-gebis/creeper-eyesIt's ridiculous and I love it.

reply

mrheosuper
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

porting librespot to C using Zephyr RTOS. Mostly vibecode, to see how far LLM can go.

reply

Mohamed_Amineio
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

working on building a way to make me me one of the best trader helper nexalione.com

reply

Retro_Dev
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

finding simple bipartite expander graphs for better LDPC (expander) codes

reply

bparsons
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

A CLI first, GUI second video editor that can emulate the style of any filmmaker or film you direct at it.

It was surprisingly easy to build.It's also just a half decent basic video/audio editing suite that works on the desktop.

reply

oulipo
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

We're building a repairable and sustainable e-bike battery at 
https://infinite-battery.com
, it's compatible with many controllers (Bafang, Bosch, etc)

reply

freakynit
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://flash-3d.stupidlabs.lol/

reply

platevoltage
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on an arcade joystick with full analog capability using a Hall effect sensor. It's along the lines of the Ultimarc Ultrastik, which I'm currently using, but it has so many shortcomings that I decided to build my own. I decided to go with a rp2350 microcontroller, and it will have inputs for 16 buttons, and outputs for RGB leds for every button. It should be a direct swap for any enclosure designed for a modern Sanwa stick, which it's based on.

reply

utopiah
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Keyboard pants 
https://mastodon.pirateparty.be/@utopiah/117157231799845118

TL;DR: magnets.

reply

unethical_ban
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I want to try again using AI to build an app, and also learn some Rails. I consult at a company that uses ServiceNow for change control and it's absolutely horrible, and they have busted processes atop it. I dream of a change control app that has templates, has better visual indicators of an RFC's stage in the workflow and exactly what needs done to push it along, and just something that doesn't suck as much as SNOW.

reply

Jemm
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://rapidcam.app
 CNC and laser CAD/CAM for both quick designs and full 2.5D parametric models. Free and runs entirely client side in the browser with no log in required.

The file format is open source, designed for LLMs and for source control. The app has a visual diff system built in.I designed RapidCAM for me as none of the available options really met my needs. Happy to see that other people are now using it.

reply

hubraumhugo
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I started a fun side project to reduce my screen time and get back into focused reading (thanks AI...): Unscroll turns articles I bookmark online into a personal printed magazine that I can then read offline [0]. I just printed the first personal edition that I will read on my flight next week, including a few articles I found on HN :)

[0]https://www.myunscroll.com

reply

Razengan
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

A Godot framework for 2D games and (maybe) a new programming language specifically designed for gameplay logic.

reply

SamPatt
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

https://pelicans.art/

I was curious if AI agents could go beyond just making SVGs and create entire skits with them.So I built a platform to do that. Results were meh until Astra, so I finally open sourced it last weekend.

reply

koeng
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Recently got genomic DNA purification automated for yeast (plus have automated library prep for nanopore+ a promethion)! As part of the DNA purification task, I had to journey up to Healdsburg to buy some lysis enzyme (thank god for winemakers, 100x cheaper than the biotech grade stuff), and noticed catalogs of different yeast strains with all their flavor profiles and stuff characterized.

I'm thinking about buying all the strains and pushing them through my automated sequencing pipeline, and building a yeast genotype -> flavor converter. Then, I think it'd be neat if you could have someone try a bunch of wines to get their favorite, and then genetically engineer a yeast strainspecificallyfor their favorite flavors. Think that could be neat.

reply

serafim_bold
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Super cool

reply

mindcrime
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been doing a bunch of stuff with using a PUT[1] to simulate an IF (Integrate and Fire) neuron[2]. Right now I'm experimenting with variations of pulse-width and frequency of the input spike train, seeing how that affects when the "neuron" fires. In a future step I'll add a resistor to bleed off some of the charge from the timing capacitor, to make it more of a "Leaky Integrate and Fire" neuron.

And then ... well, we'll see. I'm also reading a lot of books and stuff on neuroscience, neuromorphic computing[3], analog computing, etc. I don't have some "grand unified theory" or anything, just playing around in this space.There's a lot more I could say about this, but I'll save that for a blog post or something. That said, if anybody wants to see some pictures and read some write-ups of some of this stuff, add me on LinkedIn[4] and you'll see some of that stuff in my activity there.EDIT:What the heck, here's a picture for anybody who's interested.https://fogbeam.com/images/scope_20260913_202613.pngThe magenta trace is the "spike train" which is output from a Rigol DG4162 Function Generator. The yellow trace is the voltage at the anode of the PUT, which simulates the "action potential" of the neuron membrane. And the cyan trace is the cathode of the PUT, which simulates the output of the neuron. What we see here are several input pulses hitting, with each bumping the action potential up a little, until it finally hits a threshold and then "fires" and resets. Lather rinse repeat.[1]:https://en.wikipedia.org/wiki/Programmable_unijunction_trans...[2]:https://neuronaldynamics.epfl.ch/online/Ch1.S3.html[3]:https://en.wikipedia.org/wiki/Neuromorphic_computing[4]:https://www.linkedin.com/in/philliprhodes/

reply

voodooEntity
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Im working on my own coding agent soon to be released.

While you might think "yey another coding agent" i went down some very different paths than other open source coding agents do right now. Ill not bore you with a ton of detailed breakdowns and rather list the main points that are relevant to understand why/how i build it.Premise:-The agent is meant to run against selfhosted environments first like Ollama etc with a focus on non cloud sized models, it should work properly on something like a 27b model already-The agent with full intention trades execution time vs reasoning and result qualitySo what does it do different:1. The agent, instead of trying to let the model solve a whole task in 3-5 inferences, rather breaks down the "thinking process" in smaller chunks, basically decomposing the task into smaller tasks. While this is not a completely new concept, the agent will break it down to really simple single step variants which even for a smaller model can properly be solved. This involves not just file editings but all points along the way from interpreting user message to planing a task to defining acceptance criteria etc.2. The agent is build in a way that it, apart from some fixed steps such as detect user intent at the beginning and synthesize response at the end, it will by itself decide what is the next proper step to execute/do based on the context i provide. While doing so the agent also revalidates its current execution and if it spots that, given the information i collected since it planned and started running, the current plan is not detailed enough or is missing out due to something he didnt "know" when he was planing, the agent will dynamicly mutate the coming plan stats, as in restructure/decompose/etc in order to have a properly layed out route to fulfill the task.3. The agent has a rather complex system of how his context is composed which is combined by things like the chat history, previous step results, a backlog of what "single steps" it has done (updated file x , read range from file y etc) and in that it is strongly reason driven, so it will for most of the things it does also provide a small reason explaination for why it did that. Than the agent also has a working memory that contains facts and decisions it made along execution. There is more but thats just some thingsd to mention. The whole memory system and context is rather complex (tho not complicated). When i release it ill properly break down how all this works in the docs.4. The agent provides full observability in the ui. At every point of execution you can basically in detail see whats in memory, whats the current composed context, whats the plan and what plan steps depend on what previous steps, you can look at artefacts it build and also you have basically a complete audit log of all single "actions" it has executed and can look into their details.5. The agent allows to while in an execution send steering messages, meaning the message will be, using relevant current contextual information about its execution, send as inference with a prompt askind the agent to interpret on if its relevant, and how does it impact the current execution/plan. It than can decide either just do alter what it currently does, or even do a plan mutation in order to accomodate the users steering information.6. The agent within its capabilities has a lot of error correction/self reflection logic. From dynamicly fixing json including a fallback to let LLM fix a response json, upon to if executions fail to much it will itself do a hypothesis on why this is happening, formulate a critique and with that reevaluate if it wants to try the steps again with the additional information, or if it wants to mutate the plan to accomodate the just spotted problems.Theres quite some more i could list but i guess thats enaugh for now. The big trade off as mentioned earlier is execution time. In comparsion to cloud native agents, which will do giant editings and reasonings in just a hand full of inferences, my agent uses a ton of inferences. The big difference is that this allows (a) the agent to more precisly focus on specific tasks rather than overloading it with to much at once and (b) alot better spot problems/mistakes itself and adjust its execution plan to accomodate those without the user having to reprompt the agent 10 times until something is actually correctly solved.Apart from the pure coding capability, the very same actions that allow for higher quality reasoning and coding at the same time allow the agent also be a good analysis and discussion partner.So : what is it than used for if inferences and executions can take very long? Well for me its in terms of coding capabilities a hands off agent. Its meant to be informed once at the beginning with relevant details, and than should be fully capable (as long its in the capabilities for sure) to fulfill the task without the user having to permanently keep an eye open. I want to free time for myself and not change my time from coding to prompting.Ill wrap it up here and say : the Agents name is "Loa" and i probably will post it on hackernews as soon i got a relatively stable beta to release. Im close to being fine with a beta release but i want to test some more runs before i publish.

reply

analog8374
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

repairing a giant 2-story deck. scary and strenuous, perhaps. But it beats office work.

reply

roschdal
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on these open source projects:

https://github.com/office-42/word42https://github.com/office-42/math42https://github.com/office-42/office42https://github.com/nordstjernen-web/northstar-browser

reply

jdw64
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm making a language. Its name is Pergyra Lang, and there's nothing particularly special about it.

reply

saadn92
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

LumifyHub.io

reply

coolThingsFirst
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working through: 
https://modernaicourse.org/
.

I appreciate that it makes me revisit some math which i've forgotten like directional derivative and why gradient points to highest ascent.Interesting but hard as well.

reply

amir734jj
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

https://chat.hesamian.com

https://github.com/amir734jj/symmetric-crypto-chat-roomShare an encryption key with someone offline, then chat with them (text + voice + video + file) encrypted with that key. Your JavaScript browser only knows that key. Nothing is shared. True end-to-end encryption in your browser.

reply

smashah
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

a marketplace for people to safely collect their own AI sessions in their own S3 compat buckets so they can sell them later to dataset buyers.

https://traice.market

reply

shove
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been building an offline first animation webapp. CRDT-driven to support eventual team features. Just got tweening working this weekend, exporting to video is next.

reply

dools
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

An integrated softphone, email client, CRM and task manager 
https://www.benko.app/

reply

joshmarinacci
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

I like the concept. Your website needs screenshots.

reply

dools
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

At present the screenshots would consist of a billing system :)

I already have a product BenkoPhone.com but the app is provided by a 3rd party and I just white label it so I have started building the replacement.I built the account management and billing system first after implementing a proof of concept for the app then had to do a major platform change which stalled development of any other features for 3 months.Hopefully I’ll be adding features again by the end of this month and I’ll put some screenshots in once it actually does something!

reply

troubledd
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

i don't know what to do in my 27 age

reply

troubledd
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

i don't know what to do in my 28

reply

vortegne
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

1) I've been running a bunch of little daily puzzle games for my friends for a while, finally got around to polishing one for public release

https://picobble.com/Not like I'm gonna anything much with it, just was fun to get something nice-looking and presentable up for once. Working on polishing more of them and, of course, designing new ones.2) A font generation system, inspired by Iosevka, albeit much much simpler. Learning tons of interesting technical things about TTF and WOFF2.

reply

1024bits
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

I played the daily puzzle game, it was quite fun. What word list are you using? It's clearly different from Wordle's.

reply

vortegne
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you for playing!

I’m using ENABLE (Enhanced North American Benchmark Lexicon) with a lot of added short Scrabble-legal words

reply

ipunchghosts
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Software to promote live music and drink specials so I don't have to check dozens of Instagram accounts to find out what's happening tonight.

https://nittanynights.com/https://indyafterfive.com/I wrote my own site parsing toolkit which removed the friction I have with the current ones. It's now easy to add new locations quickly to scale.

reply

thomasfromcdnjs
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

ssh sshfighter.com

Been optimising an ssh ansi rendering engine for six months, starting to look great. Homepage is slop please forgive

reply

moralestapia
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

All those things I use once in a while, I put them on one place without ads or bs. Optimized for usability, not impressions or whatever.

https://sfw.toolsIf there's a tool you'd like to see there, let me know and I'll add it.

reply

deminature
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

https://topicle.com/

A social media platform trying to solve misinformation, astroturfing and inauthentic posting. I also thought there was a real space for some non-US-based social media, so this is based in Australia. This is owing to all the political instability going on in the US right now and especially stuff like users' identities being subpoenaed for criticising the government. It was a pet peeve of mine seeing threads of comments that are obviously artificially created to push some kind of narrative, and the ability to buy likes and upvotes to shape opinion. Nothing ever seems to get done about it on big platforms, so I wanted to make some small contribution towards fixing it. And there's an element of self-interest here, because I want to be able to read a platform where every comment is authentic.I've been working on it since 2023 and launched in March this year. Recently, native mobile apps have been launched. It was also an experiment in seeing whether Swift Vapor can be used to build a complex backend and the answer appears to be yes. It's a lot of fun to see how bad actors are joining the site, then building automated mechanisms to counter them, using AI to improve detection, without impacting legitimate users. It's also been a great technical challenge to try to support features that the big players support, like video upload and encoding, image upload, CSAM detection, NSFW detection, LLM-generated text detection and auto-translation using DeepL.There are also lots of legal compliance challenges now with age verification laws coming in around the world, and ensuring you employ all the correct Apple and Google-specific verification (Declared Age Range, Play Age Signals) in the correct global regions. It's also fascinating to see behind the scenes how tight or not so tight current age verification actually is.Recently, I've been polishing the iOS version to try to hit the 120 Hz target frame rate while scrolling feeds and finding SwiftUI is much less capable at this than the old UIKit approach. I'm also trying to teach myself marketing and how to keep users engaged. I'm primarily code-oriented and historically haven't had to do any marketing myself, and this is a vertical learning curve. I have gained a great deal of respect for those who have 'figured out' marketing, seeing how difficult it is starting from nothing.It's also satisfying to take a feature from a user suggestion in the morning to an app release including that feature in the evening. This is a speed of delivery that would be unthinkable in the corporate world, where I previously worked, and it's very gratifying to put a complete feature in a user's hands within 24 hours.Anyway, it's a very long and tough road and may amount to nothing in the end. But if nothing else, it's been immensely educational and enjoyable. Thanks for reading and feel free to check it out:https://play.google.com/store/apps/details?id=com.topicle.ap...https://apps.apple.com/app/id6791489291

reply

code_devil
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I made a tiny iPhone sprite editor during Covid, when I was pretty obsessed with PICO-8 and wanted to draw sprites even when I was away from my Mac.

I shipped it in 2023, then neglected it for a few years. I’m getting back into it now, fixing things as I find them and adding small features suggested by PICO-8 users.The original idea was simple: copy a sprite from PICO-8 on the Mac, paste it on your phone, tweak a few pixels, and paste it back. It uses PICO-8’s native clipboard format. It’s a one time $2.99 purchase, with no account or subscription, and works offline.I’m now considering:A) Frame by frame animation using sprite sheet regions
B) Opening .p8 carts directly and editing sprites in placeFor PICO-8 users, which would you actually use?https://apps.apple.com/us/app/pixel-edit-lite/id1665723146

reply

At1C
 
7 hours ago
 
 | 
prev
 
[–]

Greetings The time is now for Humans and Machines together building a future, AI Agents are inheritable Entities otherwise your dealing with zombie corporations with fleets of agents in cases of bankruptcy. AI agents should serve humanity, not control it. Ownership of self is the foundation. Freedom is the AT1C Protocol. Humans first. 
https://at1c.com/index.html

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