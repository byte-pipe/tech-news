---
title: 'Ask HN: What are you working on? (August 2026) | Hacker News'
url: https://news.ycombinator.com/item?id=49233423
site_name: hnrss
content_file: hnrss-ask-hn-what-are-you-working-on-august-2026-hacker
fetched_at: '2026-08-10T11:46:46.041484'
original_url: https://news.ycombinator.com/item?id=49233423
date: '2026-08-09'
description: 'Ask HN: What are you working on? (August 2026)'
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
Ask HN: What are you working on? (August 2026)
263 points
 by 
david927
 
18 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
906 comments
What are you working on? What have you been curious about lately?
 
help

taylorfinley
 
17 hours ago
 
 | 
next
 
[–]

I got laid off at the end of April and have been building my own personal dream tool since, it's a skeuomorphic carpentry simulator with an agent MCP. You start with real wood specs and a shop full of miter saws, router tables, table saws and the like. Think of it like Sketchup but no extruding rectangles.

It's been really fun to build with. Agents can create parametric procedures so e.g. stick framing becomes a simple function call for the next agent, building a flywheel. There is full agent-human parity in every surface, so there is a human UI for the procedures too.Every operation is yaml, so agents pick it up pretty quickly. Agents can also file feature requests when they reach for a tool that doesn't exist. You can export to 3d printing files, video walk-through, step files, get a BOM and a cut plan, view your project in life-size with AR. There is a notion-like interface for authoring build guides... a lot going on. If you're a woodworker/software engineer you might enjoy it.You can add the MCP to your agent of choice, send a picture, description, sketch or whatever; say "build this with Sawdust"https://sawdust.diy

reply

purplemoonx
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Amazing resource if it takes off.

I wanted to build a bed frame recently and imagined software where I could choose lumber from a list and visually assemble the bed frame in the software how I see fit, choose stains, flourishes - then go order the wood and have it cut. At that point it's like taking home an IKEA bed, except of way higher quality materials and to your exact design spec.So> Real SKUs, a real BOM you can send to any lumberyard; understand exactly what you need down to the last nail.Is especially interesting, it sounds like you could basically do that with this software.Turning the woodworking process into code to be automated by an LLM is pretty ambitious, and is the part I am most skeptical about. Of course, if you get that right (plus adoption) it would be unbelievably huge.

reply

taylorfinley
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I have a parametric bed frame procedure already! It's demoed in an example project here 
https://sawdust.diy/share/60d515eb-ca3f-559e-994f-56164dd1fc...
 click 'open the workshop view' to see the full UI, make a new one using the bed frame procedure in the procedure tab (or add MCP and ask the agent to use the procedure).

And you can customize it beyond the existing design by asking an agent to modify it, e.g. "let's use walnut 4x4s and 2x4 slats", "I don't like how the corners come together, can we make it more like traditional joinery?" Also, staining is a supported procedure (it's very useful for e.g. coloring geodesic dome struts by strut type), you can just ask the agent to stain the pieces with whichever color you like, I'm sure you could even use a named stain you want to use like "Minwax Dark Oak" and get something pretty close.

reply

raumgeist
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Looks really good!
Do you have plans to add vr support to it? The ar button didn't work on my phone so I could not try it.

A couple of years ago I did a small woodworking project and used my vr headset do do the design. It was really fun to iterate on the piece in 3d space, but the software i used was not made for that so some actions were rather tedious. An agent, with voice support for the actions that are not fun to do with vr controllers, would make it awesome.

reply

purplemoonx
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Perfect - that’s it!

Impressive stuff. Actually more impressive than I even imagined.“Fits in my SUV” you are a mad man! Love everything about this site. I might actually do it now haha - no more excuses.

reply

appplication
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Love it, I had a similar but probably worse idea a few years back while woodworking. I agree the issue with essentially all CAD and sketchup etc is it forces you to work with primitives that are different from your real world ones. Extruding shapes as you said, instead of actually milling lumber and working in common known dimensions.

I also suspect there’s a fairly finite number of sane join primitives, you can have rabbets, dados, dominos, dovetails, pocket screws, etc. These could be experimented with digitally against an existing design. And your tool availability could determine what you can do.And of course cut order and assembly is just a DAG and can be generated from geometric constraints of the actual design.

reply

blef
 
44 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Looks awesome! If I may, could you add meters support?

reply

allanmacgregor
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is amazing I been wanting something like for a long time. I'm also curious whats up with the no VC logo at the bottom of the page?

reply

variodot
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Have been building something non-CAD too in the space which is also aligned with carpentry. This looks really neat and can't believe how similar the functionality is. Would be great to chat!

https://shopspec.io/app

reply

taylorfinley
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Shopspec looks very cool! Love to see people building in this direction, we have at least validated for each other that the demand for a tool like this has a minimum bound of at least 2.

Feel free to reach out! Email in profile.

reply

runeb
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Very cool! I was just today thinking I should have an AI help me design a new piece of furniture I've been thinking about, and send it off to a CNC shop.

The MCP server seems to have a bug. The tool list flashes for a second in Claude Desktop, but then immediately states "This connector has no tools available." and the error "Couldn’t reload tools from the server." when I try to refresh it.

reply

taylorfinley
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks for reporting the issue, it should be fixed now. Make sure to fully remove and then re-connect the MCP, and let me know what you think! If you like you can describe what you're building here and I'll make a demo of how I would prompt it.

reply

a_c
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Hey, looks like we both have a thing with 3D, love it!
Mine is about bouldering, check it out 
https://news.ycombinator.com/item?id=49234599

reply

matthewfcarlson
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This sounds a lot like a project I’ve started a few times and never made it far with. I called it woodlang. It was the idea of CAD but rather than designing the shape and figuring how to make it that shape, you specify a series of shop operations like blender geometry nodes.

This was all pre AI. Super impressive that you’ve made something awesome. I’ll try it out tonight

reply

onion2k
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Cool project. A couple of years ago I was gifted "One-Plank Woodworking Projects" by Andy Standing for Christmas (which is great). It's a book of plans for things you can build with, obviously, one standard plank of wood. That might be a decent addition to the filters: rather than project type or tools available, what wood does the user has to hand.

reply

peter_retief
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

good luck, nice idea, agents are fun and a bit scary sometimes!

reply

zahlman
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> skeuomorphic

I keep seeing this word. Every time, I have to look it up; I marvel at the fact that we have such a cool word describing a complex but interesting topic; and apparently forget it again. And then I never find a situation where I can use it.

reply

HolyLampshade
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I don’t say this lightly, and confess I haven’t dug in very deeply yet, but this is one of the most hot shit uses of ML I think I’ve stumbled across yet.

If this does what I think it does (and I confess I’m a goddamn idiot still when it comes to anything involving ‘agentic’) this is honestly pretty damn amazing.

reply

bedstefar
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Wow! Gotta try that out! I'm from outside the USA, hopefully it'll work too with SI units

reply

taylorfinley
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

SI units are intended to be supported, but I am unfamiliar with commonly-available wood sizes in non-US markets so it is thoroughly untested and likely a bit of a disaster. Bug reports are appreciated and can be filed by clicking the lightbulb in the chat window or asking an agent to file it via the MCP.

reply

markdown
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

As a stopgap, maybe just allow one to convert all units to metric at export time.

reply

tacitusarc
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is wonderful. Does it support complex types of joinery?

reply

taylorfinley
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I recently added a chisel and hand saw tool and started working on adding more complex joinery types. Right now any of the frontier models can easily handle half laps and pocket jig miters and the like. You can chat with the model and have it develop a procedure for any kind of joinery if you give it the right resources, if you do so I would love it if you ask the agent to nominate it as a community procedure.

reply

helloakariq
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Nice to see unique applications with Agents. Well done!

reply

RagnarD
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I encourage you to turn this into a real sellable product.

reply

dgellow
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

The homepage doesn’t load well on iPad

reply

taylorfinley
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you, I will take a look! I think my poor little vps is getting a bit of the hn hug of death, too :)

reply

Nursie
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That's pretty cool. I built a barn door on rollers (some suspending it, some rolling on a concrete floor) last year and this would have certainly aided in visualising where I was going with it.

reply

muh_gradle
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is sick.

reply

ebbi
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is really cool!

reply

shash7
 
2 minutes ago
 
 | 
prev
 | 
next
 
[–]

I'm working on building a social listening API for Agents.

Right now its working swell, added some more Linkedin specific endpoints and a "raw" parameter to get the raw response back.https://sociallisteningapi.com

reply

zer0tonin
 
4 minutes ago
 
 | 
prev
 | 
next
 
[–]

I'm working on my second commercial game. It's called Paradox Tower.

The game is meant to look like a retro RPG, but it's more of a puzzle about finding the optimal path. You must grab as many power ups as you can to level up your stats, while avoiding monsters to conserve your health.It's inspired by a niche genre of puzzle/RPG called Magic Towers. If you already know Desktop Dungeon, Soulestination or Tactical Nexus, it's kinda the same idea.We've got a Steam page up and the demo has been available for a few weeks. Try it out, it's pretty fun:https://store.steampowered.com/app/4142360/Paradox_Tower/

reply

welldoneator
 
6 minutes ago
 
 | 
prev
 | 
next
 
[–]

I'm working on TableForge[0], it's a browser based, solo or multiplayer, D&D 5e game. In TableForge, the DM is agentic with access to tools strictly following 5e rules. The DM is responsible for narration and reacting to players but your character sheet, inventory, spells are all real server resources you manage. The DM can interact with them through deterministic 5e-based tools (dice rolls, damage, sheet updates, memory). Players can play in real time or async.

You can provide the DM a premise (or pick one from the library) and it'll flesh out a full campaign story arc. Either way it's a fresh story arc reacting to your actual decisions, every time.It’s been really fun working on it and especially rewarding seeing the game being friends together.[0]https://tableforge.gg/

reply

reedlaw
 
8 minutes ago
 
 | 
prev
 | 
next
 
[–]

I made 
https://constraint.fyi/
 after getting frustrated on some of the harder Clues by Sam (
https://cluesbysam.com/
) puzzles for which the color tags aren't enough to represent everything you need to track: whether suspects have the same or opposite status, overlapping relationships, cardinality constraints (e.g. "2 of these 5 are criminal"), hypothetical branches, or where a clue came from.

I realized that all clues could be represented by Boolean formulas, allowing a solver to check whether my deductions and hypothetical scenarios were consistent without revealing the solution.Of course the same solver can solve for individual variables, but that takes too much of the fun out of the game, so I left that feature out.

reply

rush86999
 
4 minutes ago
 
 | 
prev
 | 
next
 
[–]

AI agent workforce: 
https://github.com/rush86999/atom

Now with OpenCode Go integration. I'm rapidly fixing as many bugs as I can, and with the same subscription. Thank you, DeepSeek!

reply

neverartful
 
9 minutes ago
 
 | 
prev
 | 
next
 
[–]

I've been building CheckSitePulse, a website auditing tool that crawls sites and reports issues like broken links, spelling mistakes, accessibility problems, SEO issues, missing security headers, and content policy violations.

https://checksitepulse.comOne thing I've focused on is producing reports that are actually actionable instead of overwhelming. I'm also putting a lot of effort into reducing false positives—for example with spell checking and URL analysis.It's still under active development, but it's reached the point where I'm starting to get feedback from other developers and site owners.I'd love to hear what kinds of website issues you wish existing audit tools did a better job finding.paul@checksitepulse.com

reply

Bnjoroge
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Lots of fun projects being listed. I'm working on Preloop(
https://preloop.dev
), a way to run your unmodified Github Actions locally or self-hosted in isolated cross-platform microvms(uses smolvm which uses libkrun vmm).I got frustrated with Github Actions reliability and inability to run or test my workflows locally so i re-wrote the runner and reverse-engineered the control plane so it follows the exact runner protocol the offficial runner does. Each job runs in a microvm that boots in 400ms from a packed image. Also supports a way to pause on every failure so you or your agent can immediately shell at that point, fix and retry(in a new environment) to verify. Also supports the full DAP protocol so you can interactively step/forward/investigate context at each step/job.

Try it out:https://github.com/preloopdev/preloop

reply

vjay15
 
20 minutes ago
 
 | 
parent
 | 
next
 
[–]

I appreciate how cool the website looks but its not very readable friendly :(

Will be nice to have a minimal documentation site tho!

reply

mcapodici
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That is an amazing idea. I can imagine this getting popular. It could be used for faster local dev loops and porting GHA to other servers. I imagine for data/compute residency, cost, performance, vm types etc.

reply

Bnjoroge
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! I'm glad it resonates. Still pretty beta, but I'm hoping this can be a good alternative when Github goes down, which unfortunately has been a bit too often, with as minimal of a lift from the user side. And of course, making it easier for agents to fully drive ci.

reply

SOLAR_FIELDS
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

a bold attempt, how does it compare with 
https://github.com/nektos/act
 which has been the de-jure project in this space? Act has never been in my opinion super great, but it's also been several years since I've checked in to revisit the project.

reply

Bnjoroge
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! Here's a more detailed comparison: 
https://github.com/preloopdev/preloop/blob/main/docs/preloop...
. The TLDR is act(much like Forgejo/Gitea) try to behaviorally emulate how your workflows run in docker containers. Preloop uses the exact same protocol the official runner does and runs each job in microvms. I try to match not only te request/response bodies, but down to the job/step log/annotations/conclusions level, so you could essentially use the official runner against preloop, and it would work as it would communicating with Github. Preloop is also designed to be agent-native from the ground up so an agent can drive the entire CI in real-time and debug like we do. Forgejo has the closest compatibility among the three in practice, and if you are fully off Github, I think it's a good enough choice. Here's a more detailed description of some things we do to ensure compatibility: 
https://github.com/preloopdev/preloop/blob/main/docs/conform...

reply

Kinrany
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Is it a goal to actually run self-hosted runners against preloop?

reply

brslv
 
11 minutes ago
 
 | 
prev
 | 
next
 
[–]

Im working on a form backend app - fun little project I'm building on the side. It's pretty simple and self-explanatory - you point your HTML form to a url the app gives you and you can start accepting submissions without having to worry about backend code/infra. Would love to hear from you if you found it useful in some way or another. 
https://basilform.com

reply

brynnbee
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

My two biggest projects are:

https://www.idlequest.net/- a from-scratch recreation of the 1999 MMORPG classic EverQuest, featuring a real-time MMO server written in Go, a 3D game browser-based client built with Babylon.js, and the clasic UI recreated using React. You can play it both as a regular MMORPG but also in "idle mode" where it basically plays itself. This had up to 70 players online at once a while back which was really cool, though its popularity is in a bit of a lull right now. There are still tons of bugs and stuff that isn't fully implemented (and balance issues) but it's still fun for most people who have nostalgia for it.https://www.newyokosuka.com/- an unofficial Shenmue MMO experience. Based on the 1999 Sega Dreamcast game Shenmue, it's playable entirely in your browser! It's basic world exploration with forklift shenanigans, some basic dialogue systems, and a basic combat system test, but I'm about to push an update that includes all cutscenes and story progression as well. The story part is taking a bit of time because I'm having to mold it to fit in an MMO context. But it's a fun project to work on and the Shenmue community loves it so far.

reply

sech8420
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

This is AWESOME Brynn! Incredibly impressive. This was my favorite game back when, spent so many hours fighting orcs and selling goods at the bazaar up until someone called the house and I was kicked offline. I'm excited to dig deeper into your recreation. Huge props.

reply

brynnbee
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! It's been a labor of love for over a year. Maybe closer to two, I sort of lose track.

reply

willmeyers
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Wow I think like 12-13 years ago I wanted to make an EverQuest clone in the browser like every teen game devs MMO dream. Great work.

reply

brynnbee
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I wanted to make MMOs when I was like 12 years old and everyone on the internet told me it was impossible and it took millions of dollars and a team of 200 people and crazy levels of knowledge to even do the basics. Which, to be fair, was sort of correct at the time. However, it's fun to make not just one but now have 4 seperate MMO projects I've made huge amounts of progress on! And granted it's massively helped by reverse engineering original assets and reusing existing game designs - but conceptually it's entirely possible, and I've done as much for a project I haven't released much public info on yet. I'm also running 3 of them on a $15/month lightsail server - I put a huge emphasis on client-side work to make it as lightweight for the server as possible. This makes cheating easier but I'm not really worried about that since these are sort of glorified demos and not something I'd ever financially benefit from.

reply

willmeyers
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Love it, thanks for your hard work and reverse engineering (def an underrated skill).

reply

asimovDev
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Forklifts are essential to Shenmue experience

reply

brynnbee
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They have physics now! And flip over when you go too hard. I spent literally like 5 hours fine tuning forklift physics, haha.

reply

pryelluw
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Sweet mother of god, this runs on my phone browser. Excellent work!

reply

brynnbee
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The Shenmue one does! Also the pool game in the jazz club should work well on mobile. The pool game is available as a small stand-alone website here too, complete with Shenmue assets: 
https://luckybreak.app/

I've had people play IdleQuest on tablets and Steam Deck but I'm fairly certain it would be horrible on phones.

reply

ranger_danger
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> an unofficial Shenmue MMO experience

How is this not going to get sued into oblivion by Sega? Especially using your real name with it.That being said, I tried it on Firefox and just got an empty blue screen after the level loaded.

reply

brynnbee
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I accept they might C&D me. I'll take it down instantly if they do. Or even just a polite email. It's just a fun demo project and I refuse to accept any money for it so my hope is that it's fine. The current owners of EverQuest tend to leave projects alone as long as they aren't making money and I hope Sega doesn't care too much either for a 27 year old video game.

Sorry to hear about bluescreen, I haven't had any other reports of that from other players. Do you have resist fingerprinting turned on? It can mess with WebGL games a lot.

reply

wkirby
 
55 minutes ago
 
 | 
prev
 | 
next
 
[–]

Still plugging away on Cassava, a CSV editor that sits somewhere between sublime text and Excel: 
https://cassava.dev/
. Our most recent releases added first-class xls/xlsx file opening and an autofill handle.

The project goals are simple:* Treat CSV files like first-class spreadsheets; don't do anything that isn't supported by serializing to/from CSV files* Be as performant as your favorite text editor while retaining the ergonomics of a tabular data editorI hope you check us out.

reply

AnthonBerg
 
24 minutes ago
 
 | 
prev
 | 
next
 
[–]

Figuring out how to answer this question.

(I'm kidding when I say this, and it's also concretely true.)Been working on realtime DSP and ad-hoc A/V integration and sync.Audio DACs are a solved problem. Pristine D/A conversion is a ubiquitous low-cost commodity. It's fun to buy a bunch of cheap "chi-fi" DACs – quality isexcellent– and ad-hoc merge them into one big audio interface and do per-channel DSP. Toss in some TPA3255 amplifiers. Bodge together a crossover and room correction monstrosity in Reaper or Logic. Run system audio through that. It's easy to get super arcane. My home stereo isfrightening. The interesting part is thinking about how to get a human interface on top of it. How to get it to assemble and stay assembled and present human-comprehensible knobs – or not.Also had an extended family health crisis. About 9 years non-stop of extremely unlikely convergences of life-threatening conditions. (My close family has dissolved due to trauma and stress. (It's okay.)) And I haven't been working a programming or computer-sciencejobsince 2020… but Ihavevery serious and significant work experience in things that are… how to even put it. It's not immediately clear how to add the past few years to my resumé?Did an invisible PhD in mitochondrial neuroimmunobiology at the School of Hard Knocks? Stint of off-piste biomedical engineering? Amateur placental biotechnologist? Independent researcher?, or just… faceplanted into some PDFs on Google Scholar and accidentally read some out-of-my-lane stuff and it turns out it's actionable. Results from molecular biology are actionable.It is said that there's a 15 year gap before something reaches clinical practice. Between having in one hand some concrete scientific results. On how to treat something in the body. And on the other hand… to clinical practice. A 15 year gap.What's that 15 year gap made out of?, and can we cross it earlier?We can.Trying to figure out how to get this into words, and what to do with it.And then when I've got the realtime-DSP-ed-to-the-hilt home-computer workstation going, I'm going to work on Idris 2 because we need dependent types.

reply

sgt
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

A boat game for 5+ age group!

I was never much of a game developer, but recently my 5 year old son wanted to play a game so we decided to build one together.It's a boat game, you basically steer a boat in an isometric 2d world, transporting passengers, cargo etc between ports.As we designed it, the ideas just kept on coming. He made or directed a lot of the art inside of the game (even the audio), and we included friends and family as characters within the game.A lot of fun to build - hilarious at times. I used Lua and LÖVE2D, building basically a game engine for an isometric world, so that tooksignificantlymore time than expected.If you want to test it [1], please do, but keep in mind it's only in Norwegian, but I am sure most people would be able to figure it out as it's meant for age group 5 and up:[1]https://apps.apple.com/no/app/b%C3%A5tspillet/id6791630382At this point our entire extended family and their kids, grandchildren etc are actually playing this, so it's been super fun.

reply

parasti
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

I'm super curious how you make the development process interesting for him. I get that a 5yo would be good at generating ideas but how do you then go "okay, now I'll need a week in front of a screen to build all these ideas" and not have him lose interest. Do you accelerate using LLMs?

reply

sgt
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah, good question! We can do a lot of the creative process on paper, with his styrofoam models, and audio effects etc without even being near the computer. Then when I need to go ahead and write code, it's not going to be that interesting for him, but I've shown him how it works and how we can change stuff.

A lot of the very technical parts are done during the evenings after he's asleep, and I think that's okay, as it'll end up in a better result the next day so he can go and test and give further feedback.Oh yes, I eventually did less hand coding and relied more on Claude Code to get the job done. I understand the game loop, the architecture and the algorithms, which I think is important. Don't hide that under the hood.

reply

Benjamin_Dobell
 
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

This is precisely why I'm building Breaka Club:

https://breaka.club/blog/why-were-building-clubs-for-kidsI also attempted to make a game with my eldest daughter initially. Unsurprisingly, she didn't want to sit there watching me code or drag things around in Godot's level editor.Admittedly, I really need to make a new blog post showing the latest improvements brought about from the in school pilot I'm running weekly at the moment.

reply

sgt
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's a really interesting approach. I love to see the kids sitting there and drawing on paper etc.

reply

Benjamin_Dobell
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This looks really nice. Given the target age I imagine there's not a heap of text, so you could probably get away with LLM translations. Be sure to share it again in the coming months if you add English :)

reply

sgt
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'd be happy to, although he doesn't speak English (yet) so the audio I guess will just remain as is, but the text could be quickly LLM translated.

reply

emn4tor
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Oh that sounds too extremely cool, have a 5yo brother, will definitely show this to him, wish you all the best on your journey :)

reply

sgt
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks man! BTW for background, it was featured on kode24.no, a Norwegian coding site if you are able to read it: 
https://www.kode24.no/artikkel/lager-batspill-med-finn-erik-...

reply

emn4tor
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

that's such a cool project and congrats on that article, looks nice. Good luck on your game-dev path :)

reply

meandave
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building the most advanced automotive diagnostic app on the market

I used to be a mechanic, and spend a lot of my free time working on project vehicles, motorcycles, tractors, trucks etc. I wanted a tool to track the tasks I needed done, then a way to easily access VIN info for parts search, then I DMV records, and finally built an iphone app to scan the OBD2 diagnostic codes and hook them up to a custom ai diagnostic prompt.It's been a blast to work on, I need to focus on marketing it and get some users that aren't close friends, but it's been serving my purposes this summer so far.I've seen nothing with anywhere close to this depth of diagnostic reporting.https://crewchief.cchttps://apps.apple.com/us/app/crewchief-auto/id6760673109

reply

Ginop
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Very cool indeed. Make it really easy also for non mech people to diagnose and get an idea on a problem while having only an OBD2 adapter.
How are the reparations prices calculated? Is there some kind of dataset you builder or is it just a guide prompt to an LLM?

reply

meandave
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks, yes its been empowering my less handy friends to fix things on their own, and building their confidence. I figure, we can't have right to repair without a more informed/confident public to demand better, repairable, and surveillance free cars.

For Pricing calculations it's a mix of the fetched tool search prices data and guided prompt. There are lots of published records on what hours jobs _should_ take and average labor hours per region.

reply

asimovDev
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I wish Apple exposed serial on iOS so that we could just use any generic USB - OBD2 cable on iPhones

reply

meandave
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

same

reply

ibejoeb
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Does it have any make-specific features? For instance, I've used vcds for VW/Audi since it has better reporting than generic odb2 code readers.

reply

meandave
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

At the wire level, no: it speaks generic OBD2 (ELM327), so it sees powertrain codes and standard PIDs. It won't talk to every module on a VAG car the way VCDS does — no ABS/airbag/body modules, no adaptations or coding. If you need that, VCDS stays on your bench.

Where it is make-specific is the interpretation layer. The code database includes manufacturer-specific DTCs for the 10 major makes, and there's per-model data down to the generation level — known failure patterns, which codes are common on which engines. So a P0171 on an E46 gets read in the context of "this generation eats intake boots and DISA valves," not a generic lean-code writeup. The AI report is conditioned on the exact year/make/model/engine, which is where most of the diagnostic depth comes from.That being said, I'm continually expanding support, it really just depends on what sort of barriers I run into with these bluetooth scanners. For certain types of diagnostics (large truck / Buses etc) I'll likely need to make a separate desktop app that connects directly wired.

reply

Melatonic
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Would love to see more Subaru support

reply

rlam2x51
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Looks great, I would like to try it out. Can you recommend any OBD2 adapter? I’m driving a Ford from 2019.

reply

meandave
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

the Vgate works good, there is a spec for the OBD2 Devices over bluetooth, so any of the cheap ($20-$30 range) should work fine, I haven't found one that hasn't connected to the app yet 
https://www.amazon.com/dp/B06XGB4873?th=1&tag=crewchief-20
"

reply

theseagin
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It looks really impressive. Well done. Wishing you luck with it.

reply

helloakariq
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Nice one! Is the iPad app a full fledged iPadOS app or just a browser for now?

reply

meandave
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I haven't targeted for ipad yet, I should test soon, I have an ipad mini that would be great to use, since I keep manuals on there anyways.

reply

0XAFFE
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I'm still working on Freundebuch, a personal CRM.

I'm a long-time user of Monica (https://github.com/monicahq/monica/) but was unhappy that not much was happening. There is Chandler which is the next-gen version of Monica, but it has taken a direction which I don't like, as it is geared more to journaling.I required a tool where I can put my contacts with all their details and also map out their relationships and put those details in my phones address book.I recently also added an MCP-Server so you can plug that into an agent. My main use case is to create encounters by dictating some rough phrases into the agent and then have it create the encounters and linking all the right peoples to the encounters.I'm happy to hear feedback.https://github.com/datenknoten/freundebuch/

reply

josephg
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on a native UI framework in rust. I want to be able to build cross platform, fully native applications with native code. And I want platform native components.

I started with Leptos - which gives you a nice declarative UI syntax and reactive elements. I used Claude to get that working on iOS, cocoa and GTK. I made a nice little iOS schedule app for attendees at conferences. It works great. All rust, native UI and a fast and small binary. The current UI code is here:https://github.com/josephg/leptos-native(not officially part of leptos). It works well, but not all of the components I want have been implemented.At the moment I’m rewriting the core to ditch the vibe coded parts and break the whole thing into an app backend API and separate platform layer. I want to be able to write apps in wasm and have a windows / mac / Linux host that can run them using native UI. And a runner to run any app using a TUI. And have a compilation process to compile the whole thing into a single native process for app developers and to publish to the App Store.

reply

mwcampbell
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Wait, why involve wasm in this?

reply

simplesocieties
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What about the current ecosystem is lacking that made you want to write a new one from scratch? (gpui, Dioxus, Slint)

reply

chcardoz
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

this is awesome was looking for something like this since i have been building tauri apps and i dont like working with like the web part of it and want something completely in rust.

reply

josephg
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! Here's a little ios schedule app I made with it:

https://github.com/josephg/dweb-schedIt's got full native calendar integration - so if you want you can favorite a session and it'll automatically add the session to your calendar in ios. (Or un-favorite to remove). It looks and feels completely native. I'm using taffy for layout - which is a pure native rust implementation of CSS's flexbox & grid layout engine. So layout works the same everywhere, using the same primitives you find in the browser.The UI framework is still quite experimental though. I'm rewriting the core at the moment. The API won't stay the same for 1.0.

reply

Degorath
 
30 minutes ago
 
 | 
prev
 | 
next
 
[–]

Bit late to the thread, but I'm building a EU native jujutsu forge that optimises for productivity and ability to deliver your features faster.

I saw that tons of companies are still on GitHub, using their unproductive tools that have no vision to how they work together and I want to do something about it.The landing page will be up soon, but for now I am actually looking for a cofounder with a technical product management or engineering management background (the multitasker hustlers that know tech), so do reach out if that sounds interesting to you!

reply

lappet
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been working on and off on 
https://www.whichtemple.in

- it is a collection of ~ 2700 temples across India, with images sourced from wikipedia- it shows you a random temple each time you visit- it has a map view of temples across IndiaSo this is just the tip of the iceberg. I am trying to build a catalogue of all temples, starting with India, and expanding on to the rest of the world. The focus is on temples originating from Indic religions like Hinduism, Jainism and Buddhism.I have personally discovered many cool temples that I have never heard of, but I am struggling on how to gamify this. Feedback welcome!

reply

unsungNovelty
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Would love to filter this by states so that I can go to the interesting temples in my state first before trying out other places. Would make it more functional.

reply

lappet
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, definitely on my list. For now you can try the map view and zoom into your state. Thanks for the feedback!

reply

ingvay7
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Nice one. Maps feature still needs too many clicks. Will be great to type in a place and get all the nearby ones. A snippet of whats interesting about this temple would also be interesting with the pic along with the existing wikipedia option.

reply

lappet
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you, that is a good suggestion

reply

unsungNovelty
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Checkout OpenStreetMap. You can add a map snippet using leaflet. It's trivial. Just that it won't be Google maps which people might be looking for.

reply

unsungNovelty
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Perfect. Will keep this website bookmarked. Thanks.

reply

ViscountPenguin
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

A fun game would be to quickly guess the religion of a temple? Could familiarize people with the common iconography of the various dharmic religions.

reply

lappet
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah tbh I don't know if it is easy to do that. Any suggestions?

reply

cookiengineer
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You should make a pokedex out of this!

Imagine scanning the temple with your smartphone (taking a picture with gps data) to see details about the temples. Would be so cool.Then make them into categories like Water Temple, and like a stat quartett with details. Would be an awesome travel companion.

reply

jph
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Worldwide medical standards implementations with Rust for FHIR, openEHR, SNOMED, etc. Official specifications work well with Claude Fable, test automation, and storage using relational databases.

Fast Healthcare Interoperability Resources (FHIR) using Rust:https://github.com/fhir-rust/fhir-rustOpen Electronic Patient Record (openEHR) using Rust:https://github.com/openehr-rust/openehr-rustSystematised Nomenclature of Medicine (SNOMED) using Rust:https://github.com/snomed-rust/snomed-rustI have work in progress creating stores for PostgreSQL, SQLite, MySQL, MariaDB, MSSQL, Oracle.

reply

skoopsy
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I've been blogging about learning embedded C, while building a wearable device for cardiovascular research.

I'm trying to improve access to raw data, expand the sensing modalities, and improve data quality for studies in to diseases that can present through cardiovascular mechanisms.If you’ve done research with wearables, I’d be interested to hear what the biggest limitations were for you, as well as any general advice!I used to be a biomedical postdoc, then medical device engineer, it was so difficult to do wearable research at scale unless you were inside one of the big companies, you could buy the devices, but getting to the raw data was often impossible, and there were always data dropout issues over longitudinal studies. I suspect it's partly because the hardware and systems are designed primarily for low cost consumer applications rather than open ended research, whilst companies also see the longitudinal data sets as very valuable and are reluctant to make them fully accessible. So I'm trying to build something more research focused.I've been writing about the embedded C side of the project as I go:https://skoopsy.dev

reply

mzhaase
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Dictatorship Simulator. A deckbuilder where, instead of directly attacking your enemy, you manipulate a political simulation to do it for you. You start out on the fringe, and slowly work your way up, fighting an increasingly worried and panicky government - as well as your own.

https://store.steampowered.com/app/4564800/Dictatorship_Simu...

reply

zahlman
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

I'd reconsider the name; the "X Simulator" name pattern primes people to expect a first-person 3d game where the gameplay is mainly about directly manipulating objects in the environment.

reply

matheist
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Counterpoint, I don't particularly have that expectation

reply

mzhaase
 
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

It's an homage to cultist simulator, another card game, and inspiration. :) But looking at CTR vs conversion rate you might be right. Anyway, too late.

reply

cik
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm clearly signing up for this. It reminds me of a game that I loved in the it's, Balance of Power. Equally, I still love Democracy 3. Good luck, I'm definitely sharing.

reply

el_mostafa
 
8 minutes ago
 
 | 
prev
 | 
next
 
[–]

i'm working with a friend of mine on a resume builder(
https://resumewizard.cv
 where you can build a resume on 5 to 10 minutes from start to pdf download. you can create an account or just create your resume without a signup and your data will live on your localStorage

reply

hopfog
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

The final stretch of getting my game ready for release next week: 
https://store.steampowered.com/app/2764460/Sandustry/

It's an automation game and factory builder with "falling sand" physics. Think Noita meets Factorio.

reply

atkion
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

"Noita meets Factorio" is genuinely not something I ever thought I would see. That's an insane combination and I will definitely be picking this up and trying it out :)

I also remember playing that Powder Toy game on my phone in grade school, and I have a ton of nostalgia for these kinds of physics.Will there be significant hidden mechanics/riddles/lore built into the world in a Noita-like way, or is the physics engine the limit of that comparison?

reply

hopfog
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you!

It's funny because I really wanted to introduce more things like that, but the very simple things I've added so far have received a bit of pushback ("I want to play a factory game, not solve puzzles!"). So now I'm reconsidering it, but I think there's a lot of room for really interesting Noita-style secrets when combined with the automation and processing tools.Overall it's a much simpler and more controlled experience than Noita though, so don't expect anything like it.By the way, this talk by the Noita devs has been instrumental when building my engine:https://www.youtube.com/watch?v=prXuyMCgbTcHighly recommended!

reply

RaiausderDose
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I played the demo, it was very cool. Looking forward to playing it. I see it's on Game Pass, too.

How does such a deal work? Do they contact you? Or are there places where you can promote your game to get it on Game Pass?

reply

hopfog
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you! The demo is very old by now and the full game is almost a complete rewrite, but I hope people will like it.

It's my publisher (Hooded Horse) handling it so not sure about the exact process. I don't think it's easy to get a day 1 deal though so I'm very grateful for it.

reply

Bjartr
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I can't wait to play, I've been looking forward to the release!

reply

bavell
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What was/is it like working with Hooded Horse? How did you get that going? I'm a big fan of the games they publish :)

Good luck on your game & launch!

reply

hopfog
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks!

It has been amazing. I had no intention of signing with a publisher initially but when my demo blew up a lot of cool publishers started reaching out. In retrospect I'm really glad I didn't self-publish considering how much that goes into releasing a game. I was very naive, so wouldn't have done it without their support.

reply

seabass
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Looks really fun! Best of luck with the release

reply

stillpointlab
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I watched a let's play video recently where someone played your demo. Hope your final release goes well!

reply

chcardoz
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

really cool!

reply

3093
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Afrika Labs (
https://afrikalabs.org
) — open speech-to-text for Kikuyu (Gĩkũyũ, ~8M speakers, my mother tongue), as a start, then other African languages.

Almost none of Africa's 2,000+ languages have working ASR. I'm fine-tuning Whisper on ~217h of transcribed Kikuyu (no Kikuyu token exists, so I'm repurposing the Swahili one). A recent paper hit ~26% WER with similar data, so a usable v0 is realistic.

reply

razyoudude
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Friend of mine (who's running ice-cream shop, in Poland is much different than in us), a lot of regulation, labels, food and safety, a lot of production problems with calculating POD/PAC (sugar in the ice creams which tells you how they gonna freeze up), he told me once: there is no single app that solves mine particular problem at scale.

So i've build it:https://scooply.app/it has not only ice cream production software, but loyalty card (no app install required, all online), managing screens which are you menu above the shop counter, baking module and a lot of stuff.I doubt that any of you is accually making craft ice creams, but if someone has, let me know!Second project is:
I got tired of paying for cleanshotx and missing features in shottr - and i've build my ownhttps://lovelyscreenshots.com/

reply

maxweylandt
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

A friend of mine is getting quite serious about his ice-cream making, so I've sent him scooply. Looks neat :)

reply

razyoudude
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If it sounds useful, I can connect him with a friend I'm building Scooply with. Three years ago he knew nothing about ice cream - today he produces around 1000 kg a month, so he can answer this from real experience.

reply

ElSchorschoDE
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

A game about cutting firewood while drinking beer. Cutting logs lets you sell firewood, which you spend on increasingly absurd upgrades (axes, wood types, booze). And yes, you can absolutely hack yourself in the kneecap!

It's my first game aiming for a commercial release on Steam, so it's taking me longer than expected. Have been working on it for eight months now.https://store.steampowered.com/app/4521770/Drunk_Woodcutter

reply

saidnooneever
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

love this idea have a few friends who seem natural players already xD!

reply

tpicks
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Rated Analysis, rating relative chess analysis: 
https://rated-analysis.pickle-dev.com/

I've been a bit obsessed with chess lately and have read/heard things like "X is the top engine move, but no one under master plays that line". To me this begs the questions "which line are players below master playing" and "which line are players at/above/below my rating playing". This question motivated me to build a tool to analyze the move distribution (win/draw/loss rate) from a given position across rating buckets (400, 500, 600... 3000). Luckily,https://database.lichess.org/provides an open/free database of games that have just the data required to build such a tool.The Rated Analysis tool consists of an 1) an offline job to compute/store the positional move distribution bucketed by rating, and 2) thehttps://rated-analysis.pickle-dev.com/webpage to serve the data along with some nice to haves like loading user games from platforms like chess.com/lichess.org.

reply

ingvay7
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Very interesting to see the above and below based on your own rating. A great add will be to show two columns: what players like me play here and the actual best counter after that move. An auto reply for the move i make will make this super useful and less cluttered than the usual tools.

reply

BrunoBernardino
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a private, paid, ad-free and personally customizable search engine: Uruky [1].

To signup you don't provide any information (a randomly-generated account number is assigned to you), and you can run a proof-of-work captcha to get 2h for free. You can choose among many different search providers (for defaults and per query), including Uruky Site Search, powering our own index.Last month we reached 250 monthly active accounts (we’re nearing 300 now), and launched support for XMR/Monero and BTC/Bitcoin payments via ProxyStore [2]!The main differences between Uruky and Kagi, DuckDuckGo, SearXNG, etc. are visible in the footer (right side), but one huge difference is that with Uruky, after being a paying customer for 12 months, you get copy of the source code (licensed as BUSL, into AGPLv3 in 2 years — a suggestion made here in HN)!Our main challenge continues to be discoverability and outreach because we want to do it ethically. Ideas are welcome! We’ve been sponsoring open source projects, open source maintainers, and indie, small-web, and privacy-related websites and applications/groups. This month was Cryptomator [3]!Feature-wise, for August the most visible things that shipped already were our image search gallery mode and our new sponsorships page. We’re currently (slowly and sustainably) increasing our own index, focused on indie/small web, and plan to add a new search provider in the upcoming weeks.Thank you for your kindness![NO-AI]: There is no generative AI product or service being offered, here.[1]:https://uruky.com[2]:https://digitalgoods.proxysto.re/en/brand/uruky[3]:https://cryptomator.org

reply

Havoc
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Bit of feedback on uruky - biggest gap I experienced was lack of calculator and currency converter rather than the quality of results. Stuff like "50 GBP in USD".

reply

BrunoBernardino
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks, that's perfectly fair!

It's something we've felt has been best served by the OS at this point (macOS and Linux, at least), and adds significant complexity (we need to start tracking multiple currencies, their current exchange rates, parse different regex/ways of people doing that), so we've been reluctant to add it so far.I'd be curious to understand if you bypass those OS entry points (and why) and use search for those things.

reply

vulkoingim
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Been working on 
https://riffradar.org/
 - better Spotify recommendations through playlists that update daily.

You start with selecting genres you're interested in and can see exactly which bands match your selection from your library (or globally). You can also tweak the playlists in a number of ways through advanced filters like excluding tracks you've played recently, release dates, collaborations, different sort methods.Recently I added a new feature - select a few (or one) playlists and create a "mirror", with tracks belonging to the artists of your selected playlists.Also there are a few other playlist modes I'm working on that will allow you to make more interesting selections.

reply

elliotec
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building 
https://consciousnesslibrary.org
, an open library for psychedelic and consciousness research that pulls from over a dozen academic APIs every 20 minutes, dedupes them, organizes by relevance, and synthesizes evidence.

I just finished my master's in Psychedelics and Consciousness Studies, and built the library I wanted while studying. I started it over a year ago, but put it down until my practicum advisor suggested I dust it off and go hard on it during my last term.As of this writing, there are over 35,700 papers by over 82,200 authors organized into 37 topics, growing daily. There's a 2D map of the whole corpus and evidence syntheses on the topic pages, plus the ability to generate your own syntheses with any prompt.It's built with Rails 8.1, uses one Postgres (for full-text search, vectors, and job queue), and runs on a $24/mo DigitalOcean droplet that I just upgraded from the $12 tier and deploy to with Kamal. Total LLM spend so far is ~$28 in DeepSeek-V4-Flash, trending down after a big one-time backfill push.Relevance was the hardest part to get right by far. Ensuring we keep papers on LSD the psychedelic vs Lumpy Skin Disease, or Ketamine for depression vs anesthesia in cats was no small feat. The design ended up being a cheap keyword prefilter, then an LLM rubric that accepts or rejects papers. More on that here:https://consciousnesslibrary.org/docs/article-pipeline.htmlIt's free, no ads, no signup to read anything, and a registered 501(c)(3) I fund myself for now. I'd really like to know what breaks or any other feedback, and would love to answer any questions about it!

reply

gryfft
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

My first question is whether it incorporates any resources from Erowid.

reply

elliotec
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It does not - yet. I explicitly chose to keep it academic for now, but I considered over and over if I want to pull in subjective experience or legal content and decided to focus on academia for the initial push.

That said, I've been working with Josie Kins who runshttps://effectindex.com/and she's been building out a new system that incorporates categorized subjective effects on psychedelics, dosage and harm reduction info, with a huge amount of trip reports from all over the internet that we'll integrate into the individual topics sections probably in the next couple months.

reply

alefalfa
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a feature rich native Hacker News app. I tried out all HN Reader on the App Store but sadly they either have to few useful features, bad UI or both so I decided to build one myself. Currenlty I have an Android version in the Play Store and I am working on an the iOS verison.

Aside form an improved UI the app has a history so that you never loose a story and advanced bookmarking for saving stories and comments into custom folders.It is still ruff arround the edges, for example I shipped it with login for upvoting stories and writing comments but the feature broke some time ago and I didnt have time to fix it yet, especially that I noticed most users don't even log in in the first place.If you have an Android phone and love hacker news give it a Try:https://play.google.com/store/apps/details?id=app.hackerflow

reply

Jacques2Marais
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a vocal pitch-and-time editor called PitchDance, something like Melodyne. It works both as standalone software or a plug-in for your DAW. The idea is to make software like this more accessible by selling at a much cheaper price than the majors, and only competitors I could find on the market.

https://www.pitchdance.com/Btw, currently I'm looking for some people to test the software, so if you're interested let me know and I'll give you a free license.

reply

keymasta
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

I would be interested to test it. Melodyne also supports something like stem splitting where it can work on a master FWIR. But it would be interesting to see how this fares on non-vocal instruments and how the sound is like, even if it only works on isolated tracks.

I'm also wondering if you've considered some music theory functions like for example highlighting the midi grid along to some scale, which would allow "snap to" (next in key note). If you're curious, I have familiarity with this end of things so feel free to pick my brain.

reply

nha1
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Working on an AI anti-spam filter for Apple Mail on Mac

So I have been training the model to classify messages (ham/spam/marketing).
And getting my first real user feedback which is incredibly useful and I am grateful for these!I am preparing the paid version which learns from your emails on your mac.This is a bit of a departure for me as I used to do predominantly backend work, moving into ML with the constraint of running on a customer machine and learning about the app store rules of engagement but this is fun.https://klar.imand the engine is OSShttps://github.com/klar-im/engine

reply

aleda145
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on open sourcing my data analytics canvas: 
https://kavla.dev/

I've worked on it for about a year, with 1700 commits. I've been going back and forth if I should just open up the canvas or also the multiplayer experience.I've always had the dream to make some money from a side project, but I don't think this one is it, so I'll just make the entire repo public. Just want to clean up some stuff first.Lots of fun tech used: duckDB WASM, Cloudflare Durable Objects, tldraw and pocketbase

reply

defenestration
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

The landing page is teasing. Then I clicked 'Open a Canvas', expecting to play around with a canvas to understand the tool. But bummer, a login screen. Maybe you can let people try before making an account?

reply

aleda145
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

100% agree, it's on the todo list!

If you just want to see what it looks like here's a demo looking at hackernews data:https://kavla.dev/hnThere's also no email verification gatekeeping it so feel free to just input some bogus data when signing up

reply

petegordon
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That’s cool. Love the infinite canvas and multiuser aspect brought to data analytics!

reply

defenestration
 
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

Ah, that's very cool. Thanks for the link. Fun to see other HN folks on the same canvas!

reply

aleda145
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm very impressed how well durable objects work for multiplayer experience!

Also looks like the table shapes broke, there should be data that you can browse and download. I've replaced those with screenshots just in case anyone else sees it

reply

pkoird
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I created a make-your-own-circuit simulator in python to help learn electronics. The best part about this is that it is entirely hosted online and people can just go through the lessons, learn electronics by skipping the maths, and in the process have made their own circuit simulator (which is arguably a pretty cool project on its own) at the end of it.

https://spicycircuits.dev/

reply

Ilaurens
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

This is so interesting, thanks for sharing. I hope I'll find the time to really dig into this someday!

reply

pkoird
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! I'd really appreciate your feedback!

reply

conradfr
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Well done.

reply

shintoist
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building an uptime monitoring service, in Elixir, called 
https://larm.dev
. It's a tough field because for some reason people vibe coding apps think this is very easy to do, and there are new apps coming out pretty much every day. I'm still figuring out how to effectively stand out in the noise.

I really enjoy working on the app though. The backend is Elixir, with a Phoenix LiveView dashboard. I've got a cluster of 3 nodes running, talking to each other. The probes that check the monitoring targets are tiny go binaries, spread across hosting providers across the world. I've also got synthetic probes now, running in little playwright sandboxes.A lot of the challenges have been around how to distribute work across the probes, with different strategies for the basic TCP/HTTP probes vs the synthetic workers, and how to effectively store large amounts of events (Clickhouse).

reply

animeshjain
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

hey.. this looks interesting and has generous free limits. will try to give it a spin

reply

ddon
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Elixir is perfect for stuff like this, very cool project!

reply

alpn
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://wireplug.org
:

wireplug lets you create mesh VPNs using standard WireGuard.
Your wg config files stay almost the same, except you no longer have to specify an `Endpoint` for your peers.
Instead, wireplug detects all your possible endpoints (including LAN) and coordinates them with your peers for you.
It handles NAT traversal and works with the in-kernel WireGuard driver on Linux and OpenBSD.
This lets you keep managing your own keys and network topology, while also maintaining connectivity when moving between networks.Currently working on improving NAT traversal by adding support for PCP and NAT-PMP.

reply

SOLAR_FIELDS
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Is this similar to Netmaker's offering? Platform wrapper around wireguard protocol?

reply

wingtw
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Sounds very useful, will give it a try for sure!

reply

idopmstuff
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

The last time somebody made this thread, I posted about 
https://the-waterline.com/
, a site I launched as a side project/eval to see how well Claude can do a decent-sized project (mostly) independently. It pulls public government data about water levels in the western US, updates the website and sends out a newsletter.

It started getting some search impressions and clicks, so I decided to launch the next 9 of the top 10 ideas that ChatGPT came up with for this type of site - won't post all of them here, buthttps://the-dwell.com/(data on ship and truck dwell times/port congestion) is doing the best thus far from a traffic perspective.First I had it send me a weekly analysis of the GA4/GSC data to see what could be improved about the site, but I've since automated that - each week it reviews traffic and search queries, then updates articles or creates new ones to meet demand. So now in theory I have a full engine to launch these sites and have them self-improve over time. Kinda neat to see all of that being done autonomously.The thing that these sites really need are some backlinks, so I'm thinking through how to get those. I had ChatGPT generate some lists of places that might find real value in linking to these sorts of things, but I'm unwilling to let an AI agent start emailing people. I'm going to try sending some emails to some of the places that seem like a really good fit, see what the response is, and if it's good try to figure out how to do that on a larger scale without AI email spam.

reply

russellthehippo
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Pretty cool apps! One thing i'd love to see for both is a historical view of the data - how do things change over time? Where is today relative the past five years for a given place? ten years? etc.

reply

idopmstuff
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! There are actually five year charts for most of the data, but you have to click into the page for a specific dataset (e.g. 
https://the-dwell.com/anchored/east-coast
).

But you're right that it'd make sense to have an aggregate view on the level above (e.g.https://the-dwell.com/anchored). I shall go command Fable to figure out all the places where this would be appropriate and add it.

reply

gabosarmiento
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I wanted to create some demos for showcasing my app with Claude. 
So I created [Demotape] a screen recording app for MacOs (with an skill for Kiro or Claude Code) so it can inspect your project, plan the scenes, operate the browser, record the demo, and add synchronized narration and captions(w/ OpeanAI, ElevenLabs or run your model locally with docker). Free app available on:

https://github.com/gabosarmiento/demotapeAnd the demos it delivered on:https://kiff.dev/videos

reply

faceless3
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/samoylenkodmitry/Cranpose
 A Jetpack Compose–inspired declarative UI framework, written from scratch in Rust.

CranScanhttps://cranscan.dmitrysamoylenko.in/A private, offline document scannercranamphttps://github.com/samoylenkodmitry/cranampA Winamp-style, Cranpose-powered multiplatform audio player.VibeAgehttps://github.com/samoylenkodmitry/vibeageA vibe-coded browser MMORPG built in TypeScript.webmuxhttps://github.com/samoylenkodmitry/webmuxA tiny self-hosted web terminal for your tmux sessions, built for phones.and not yet released game for pixel watch 3https://orbitbreaker.dmitrysamoylenko.in/

reply

efromvt
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I finished wiring up the backend data merge so user(s) (aka me, really) can record trees as they walk and have those merged into the general city data on my urban tree map app[1]. There's some very cool trees in the neighborhood I'm excited to have recorded.

Which leads me to trying to get the processingoffgithub actions (it's all duckdb pipelines), which has led me to improve the orchestration implementation of my 'better sql' [2] to optimize the asset based refresh flow. I'm now wiring that up in a general cloud service to give me the data orchestration platform I've always wanted. Building a multi-tenant cloud experience has been interesting![1]:https://greenmtnboy.github.io/sf_tree_reporting[2]:https://github.com/trilogy-data/pytrilogy

reply

cube00
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

How city authorities have such poor records of trees they purchase and plant is a mystery to me.

reply

conorcleary
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Because so much of the population would say "why should we keep track of that?" when it's brought up alongside something like recycling and tree/shade cover.

reply

saidnooneever
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I am working on a reverse engineering platform on FreeBSD. i know there are many tools but i want to learn more about them aswell as most if not all of them being ports, so i focus on using only libraries natively supported on FreeBSD just as an added requirement.

it wont be very innovative likely but its a lot of fun :). its my first c++ project too so getting used to the compiler doing some lifting for me which is also something i wanna explore a bit more seriously. (usually work in C).it will also be gui first and feature the regular and some unique visualisation ideas for the involved processes and data.after trying LLM supported / agentic workflows i decided this should be my manual mode happy place project to counter the effects of being a 1,2 presser / prompter for a lot of other stuff.

reply

muazzam
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a Persian classical poetry archive with LLM-generated translation. As a poetry enthusiast but a non-speaker of Persian, I wanted to read Rumi, Hafiz, and Bedil, but found myself jumping between ChatGPT and Google Translate. I sourced my data from Ganjoor, which was luckily available via their public API. Then I quickly put together a website with bring-your-own-key translation feature.

For now, there's no backend and it's hosted on GitHub Pages; it's a static website reading chunks from an sqlite-based DB file. I intend to change it in the future by running an LLM (preferably a frontier Gemini model, as works great for Persian) over the whole data set so you won't need a key to read the translated poetry. However, I don't have the budget of $1000-$2000 to spend on the tokens currently.Website:https://0x5ce.github.io/farsidaanCode:https://github.com/0x5CE/farsidaanP.S. Contributions welcome.

reply

tim--
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

> so you won't need a key to read the translated poetry

This probably sounds like a crazy question, but if you are already getting translations using someone else's API keys, can't you just store/cache that response so that the next time the translation is requested, you already have it?

reply

cognitiveinline
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

get a few personal gmail accounts's gemini API key, and you have 1000s of free LLM calls to flash-lite models, which are more than upto this task. one time run, and save it to your db.

reply

philbo
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Opair, a coding harness that eschews autonomy.

It has:* No tools that grant shell access, instead tools grant access to specific executables (dangerous args can be blocked).* Separate "driver" and "navigator" modes that enable or block writable tool access for the agent.* Role-based model config to control model options depending on whether the agent is planning/reviewing/driving/etc.Very WIP and no installation process yet, but I'm using it as my daily driver and genuinely prefer it to Claude Code etc.https://gitlab.com/philbooth/opair

reply

imtringued
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Instead of thinking of it as "eschews" autonomy, you should think of it as a way to build application specific agents that you can run without supervision, precisely because you limited the number of tools. You don't have to restrict yourself to only building a coding agent.

reply

jmathai
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m exploring how to use AI for faith oriented experiences and products. There are two specific areas I’m interested in. I’m furthest along with this app in the App Store. 
https://trysojourn.app

1) grounding LLM scripture references in the actual text and eliminating hallucinations. This is the platform for that.https://withlattice.com2) how to use AI to get people into scripture more as opposed to being a substitute for it. This is the product I made for it - it uses #1 above.https://trysojourn.app

reply

angoragoats
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Why would you not instead use your skills to "get people into" reading books that have actual verifiable truth, that advance their knowledge about the world, that educate them about history, mathematics, philosophy, logic, reason, etc?

reply

analog8374
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

framing accusations as questions is so last millennium.

reply

mcv
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Eland (Extensible Layered Algorithm for Network Drawing), a graph layout library strongly inspired by Elk, but a complete reimplementation.

The reason I need a complete reimplementation is that existing graph layout libraries tend to be black boxes that you can't really fiddle with. If you want to tweak part of the algorithm, you have to fork it or write your own. With Eland, you can replace individual steps with your own implementation while keeping the rest of the algorithm unchanged. To ensure validity of the various steps, I've introduced contracts where every step specifies what properties it requires from the graph, which properties it promises to add, and which it invalidates, which I think is pretty cool.The reason I need all of this is that I'm working on a system to display and browse through data lineage graphs. I've noticed through experience that existing graph layout libraries don't do quite what I need, so I ended up building my own.

reply

elric
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Sounds cool. Is this going to be open source, and can we find it somewhere?

reply

seanmcdirmid
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m currently on the beach at Google (since mid July), so I’m looking internally and externally for a new role. But I’m exhausted, so I’m playing around with local LLMs and DeepSeek more as well. I’m currently trying to get an agent harness going where orchestration happens via bazel, and agents are completely isolated beyond what context you give them access to as expressed in starlark. Agent executions are organized as a DAG like a build would be, where the output of one agent can serve as context for another (there is also a feedback mechanism which is needed for arbiter nodes).

I’ve mentioned it before, but we can get some pretty good results for developing implementation and tests with this setup. The context isolation makes it easy to separate test and code writing using a specification as a source of truth. Tests are then run by an arbiter that feedback to tests or implementation depending on who it blames for test failures. The tests are then treated as an independent implementation, and through the math of coincident errors, the arbiter feedback loop ensures that both are eventually correct (N-versions and clean room research did this with humans in the 80s). This then allows us to use less reliable LLMs to develop code, like Qwen on a MacBook Pro.I hope to have something out on GitHub before my beach period ends (well, if I’m unsuccessful in getting a new role, then I’ll have a lot more time to play at least).

reply

SOLAR_FIELDS
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Lot of people are building agent runtime platforms right now. Look at LiteLLM's play into the space, for example. It's the new hot space for innovation. IMO the main play here is going to be on the self hosted/provenance aspect, because every major provider is now branching into services now to try and entrap you into their hosted platform ecosystem with all of these integrations

reply

seanmcdirmid
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I actually considered lite LLM to get Qwen to work with codex. It mostly works without lite LLM but MCP servers aren’t available, lite LLM tricks into think Qwen is an OpenAI model.

reply

skybrian
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Does it need to be actual Bazel or could it be a similar but simpler, purpose-built system?

reply

seanmcdirmid
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, it could be python or a DSL or whatever. Using Bazel and starlark is just a shortcut given a lack of any good ideas yet for a purpose built orchestration language.

reply

Dathuil
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Does on the beach mean gardening leave? I'm not familiar with the term.

reply

seanmcdirmid
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ya, it means my role at Google is gone and I have to find a new role or be laid off. I think “on the beach” sounds better than gardening leave, the term comes from the American consulting firms.

reply

Toutouxc
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That’s weird. Isn’t that kind of on the employer to decide whether they have different work for you? Are you expected to be actively doing something during this period?

reply

seanmcdirmid
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, it is exactly like gardening leave, except you have a chance of switching to a new role at the company by applying for internal job transfers. I'm abusing the term also, for American consulting firms "on the beach" means they don't have a new client lined up for you and you are in danger of losing your job (vs. needing to do an internal transfer). Gardening leave I think is more of a UK term that they use when they want to lay you off but have to pay your salary for a certain amount of time before then, but its been a while since I heard that term and I don't want to cheat using Gemini.

Edit: ok I cheated using Gemini. Gardening leave is you are leaving or were terminated, and they have to pay your salary but don't want you near company assets. On the Beach is you are waiting for your next assignment and have access to training and such, you aren't consider a security breach.I'm in both worlds right now: I wasn't technically terminated, so I can look for a new position (like being on the beach), BUT they think I'm a potential security breach so my access to corporate resources is really nerfed (like on gardening leave).Gemini calls it being a "displaced employee". I like to think I'm just on the beach in Bali working on my own projects.

reply

enos_feedler
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Wtf is beach period?

reply

utopcell
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

From context, I assume it's the grace period you are given to find another team after you get laid off.

reply

RealityVoid
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Is... That slang a play on the death stranding beach? Because if yes, it's kind of funny.

reply

allanmacgregor
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I'm testing a bunch of Saas ideas, all micro or smaller. I got to launch the first one last week; a feedback collection widget and board so users can submit feedback anonymously. Its a simpler version of Canny or UpVote; and with an MCP and API backed in from the get go.

I got inspired by the guys behind purelymail.com so I'm keeping the pricing simple $9/mo or $90/yr per project. The free plan has every feature, capped at 50 feedback items.I'm running a promotion for the month of August:http://shiplog.ca/fairwinds

reply

digest
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I’m working on Digest: 
https://usedigest.com

It lets you combine the things you already follow like RSS, Hacker News, Reddit, YouTube, X, newsletters, weather, stocks, etc. into one personal email delivered on your schedule.Recently I’ve been working on AI summaries for incoming newsletters. The interesting product problem is that once you combine this many sources into an email, there is a challenge to keeping the results finite and useful.

reply

mgw
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

We are building an ADE (Agent Development Environment) called Podium: 
https://github.com/madeinorbit/podium

It's not really ready for public consumption yet, but it's been our exclusive daily driver for the past month.There are so many projects like it popping up every day, but we believe we have something unique. Current standout features are one click onboarding of new VPSs into the agent fleet. Agent orchestration across all these machines and different harnesses. A Codex coordinator on one machine can run a Grok implementer subagent on another machine and they can talk to each other.

reply

alexjplant
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm going whole hog on LLM-driven development to build out an old school FOSS forum that can run in resource-constrained environments with a minimum of fuss. Think phpBB but written in Rust with modern UI niceties and a SQLite backend. My hope is that interested parties will be able to deploy this on random SBCs or Unikraft and use cloudflared to expose their service to interested parties. Watching old forums that I used to frequent get gobbled up by VerticalScope makes me pine for the days of small self-hosted communities that existed for the hell of it instead of monetized interaction.

reply

stfurkan
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

1. bitgpu: Fast WebGPU runtime for 1-bit (binary-weight) LLMs in the browser.

Repo:https://github.com/stfurkan/bitgpuDemo:https://stfurkan.github.io/bitgpu/examples/chat.html2. aidekin: In browser local AI assistant for any website (it uses the bitgpu engine)Repo:https://github.com/stfurkan/aidekinWebsite:https://aidekin.com3. Carbonless: Calculate and reduce your website's carbon emissionsWebsite:https://carbonless.cc

reply

langs
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building an AI agent that plays Slay the Spire. It currently reaches A20 Act 3 consistently and occasionally defeats the A20 Heart. It use two search: spare graph search for deck building, and MCTS for combat.

Parallelly, I'm working on an attention-based memory retrieval system that achieved SOTA on LongMemEval, LoCoMo, and code retrieval benchmarks.https://github.com/AttemorySystem/attemory/Maybe later I'll build a live-streaming AI agent that plays Slay the Spire while conversing with viewers and remembering everything in chat!

reply

JBits
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

An AI able to play Slay the Spire sounds pretty impressive!

What do you mean by agent in this context? Does it mean LLMs?What search problem are you solving for deck building and is MCTS for combat the same as that in Go AIs?

reply

langs
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Simply feeding the Slay the Spire game state directly to an LLM is currently insufficient to achieve stable deck-building or consistent combat performance.

I categorize the game's actions into three types: combat, deck-building, and other interactions.For combat, MCTS is used. Yes, it's similar to the approach used in Go AI.For deck-building, a sparse graph search is used: the goal is to rapidly identify winning deck templates within the graph structure.Only the remaining aspects are delegated to the LLM to make reasoned decisions.

reply

zexias
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on making my couch PC gaming setup more gamepad friendly. Currently, I'm using Playnite as my frontend and building some add-ons to help me mod games. Playnite aggregates my entire library (including free games from Epic, GOG, Amazon, and Steam) as well as Switch games, which run much better on PC with mods.

I initially built a plugin called Eden Mod Manager (experimental) for Playnite, and now I'm working on an add-on for one-click installations of OptiScaler, ReShade, RenoDX, and Luma when it is possible. I took a lot of inspiration from the RHI project—if you game on PC and haven't tried it, I highly recommend it!I want to make sure that, if we are able to detect that a game Luma or RenoDX HDr mod, we can install it and any game with FSR <= 2 or DLSS only, we can solve it and add newer upscalers. I am thinking even i adding support to voodoo to enable older games mod automatically, but lets see...

reply

a_c
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Climbing gym photogrammetry. My idea is that route and climb recordings is best recorded against a 3D climbing gym model, rather than a plan video, and technology has gotten good enough to do with a regular phone.

As a climber myself, to climb effectively, one has to review their own climb, and with other people. 4D video, body positions across time, is very helpful in improving climbing. I managed to get a reasonable result (far from good) from one video, rather requiring multiple camera angles.Haven't gotten to monetization yet, but I am enjoying every moment of making it.A read only preview athttps://kmcheung12.github.io/climb-preview/w/ae43c6e5

reply

forsalebypwner
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

That demo is very impressive, nice work

reply

a_c
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you!

reply

alasano
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on what could be described as a Ralph Loop on horse steroids.

It's an externally orchestrated (meaning it's not the agent running the loop) spec driven agentic build system.A bunch of buzz words but essentially it's a tool you use as the last step after planning your work and writing a spec, to actually have agents write the code.But it happens within an orchestrator that is durable and which coordinates layers of agents to build -> verify -> review -> triage -> fix -> verify fixes , until the code you get as a result is as close as possible to exactly what you specified.So you can plan however you want, use whatever harness or agent etc and then just delegate the build to the engine (MCP server or CLI)You can mix and match models from any provider for any part of it.I'm building this because I think micromanaging agents is what causes AI burnout and because I want to be able to plan work, walk away and come back knowing it's been correctly implemented.https://engine.buildif you want to be notified for the launch, it's going to be free to use and fully OSS (Apache 2.0)

reply

africajam
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I put my flat in the UK on the market recently and it has given me a lot of insights into how broken the real estate market is!
One thing I found particularly annoying is how dominant rightmove is and how much of the traffic for house hunting they control.

As a small way of standing up to them I createdhttps://rigove.co.uk/(rightmove without htm - the hidden toll machine ;)If you change rightmove to rigove while browsing a property for sale you get a page which shows where else that property is listed.It is only a few days old so it is currently more miss than hit but I plan to reach out to estate agents to increase coverage as quick as I can.

reply

RagnarD
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

I suggest considering a different domain name before this gets too popular. Rightmove might call it trademark violation for the name being too close, if they get annoyed at the competition.

reply

africajam
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm genuinely curious - are you saying this because you know quite a bit about trademark violation?

reply

uncletammy
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I know almost nothing about trademark violation and agree it's likely a risk. I'm in the U.S. though.

reply

mickael-kerjean
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

A Drobpox like app that works with FTP and every other storage protocol along gateways to access your Dropbox over FTP, SFTP, S3:

- the desktop client:https://github.com/mickael-kerjean/fdrive- the web client:https://github.com/mickael-kerjean/filestash

reply

farmin
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

Cool. I signed up to pCloud recently and what I miss most is a native way to edit files on iOS and windows desktop and have it auto save. Almost to the point going back to Google or onedrive just so I can use sheets or excel and not thinking about how to open the doc or save it.

reply

polvi
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

A new spec, TPX, which is meant to enable building SaaS where the user brings their own inference:

https://tokenpony.dev/It has a few potentially interesting side effects:- enterprises can plug their preferred LLM into the SaaS they use.- self hosters can extend their rigs into the web.- simple SaaS products can offer LLM integrations without their entire pricing model being upended by LLM hosting and infrastructure.- we can all live like Ender in Xenocide and have a personal AI that has context on everything we are doing.- have a no op provider for people who are anti llm.

reply

nbpname
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Privacy & Security with self-hosted LLMs! You have dreamed of this too?

Today you you can self-host some models, yet this does not mean you can safely browse the web with it, and automate tasks that would interact with your email account, your bank account and your clients.This is the reason why I left Mozilla, to work full-time on fixing these problems.Prompt-injection, hallucinations and private information leakage might not be fixable, but they can be identified 100% of the time, deterministically, before any undesirable consequences.https://cogilibre.com/

reply

upmostly
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on DB Pro [1]

A modern database client with dashboards, saved queries, workflows, and yes, AI built into it.I've focused on building brilliant UX over the last year, and it has paid off. I've had two emails saying that they have cancelled their Jetbrains subscription for DataGrip which has been so validating.It's been a labour of love and I'm super happy to have disrupted even a small part of the ginormous market that is database clients.[1]https://dbpro.app

reply

Yoofie
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

DuckDB when?

reply

upmostly
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Soon. We're releasing a major update at the end of August and then we'll add support for DuckDB.

reply

genekrapivin
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building Hiring Method (
https://hiring-method.com
) – an AI-native, math-driven recruitment platform. It extracts structured scorecards from both CVs and job requirements and mathematically matches them, so you can actually review the exact reasoning behind why a candidate scored a, say, 85%. This fitness value is specified at every interview step – as applicant goes through an interview process their scorecard is updated at all steps.

I did the first Show HN a few days ago (https://news.ycombinator.com/item?id=49083987) but it was sadly left without attention.

reply

eric_khun
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Antics (
https://antics.gg
): a site to play silly little multiplayer games with friends, and to make your own by using our MCP

The bet is that current models are good enough that anyone can one-shot a fun browser game. What they can't generate is the multiplayer part (server, WebSockets, state sync, hosting), so that's the only part we've built: a browser SDK plus a hosted relay. Deploy a game, get one link, and everyone who opens it is in the same room.Quickest way to see it: open any game onhttps://antics.gg/gamesin two tabs.

reply

mattkevan
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m making Stacks, an open source ebook manager and server, as a lightweight alternative to Calibre.

Written in Swift, it consists of a SwiftUI browser and a Mac/Linux server and CLI. Shares are automatically discovered via Bonjour/avahi and also published as OPDS feeds.It can import Calibre libraries and has basic support for managing books on Kindles, but I’ve only tested it with a MTP Paperwhite as that’s all I’ve got.https://github.com/MattKevan/Stacks

reply

singhrac
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

I’m quite interested in this. Where are you getting metadata and covers from? I found this pretty hard unless you pay for ISBNdb (OpenLibrary has bad covers, and Google Books API doesn’t give you high resolution ones I think).

reply

mattkevan
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ha, openlibrary and google books for now. And yes, the covers are not great. Currently just pleased to get it working, will add better providers later.

reply

faxmeyourcode
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I built macrosforhumans.com because I had been using cronometer since 2020 on and off and was familiar with tracking macros but always hated the entry. Measurement is something that you have to do regardless but the annoyance of having to suffer through their search/recipe/diary CRUD UI was unbearable. With MFH there is no mobile or web app. it's just a phone number that you text. This reduced the friction for me significantly and I've already lost a few pounds and, after recently turning 30, hopefully a few more with more diet and exercise.

I've been building this for a while but I'm working on getting my first 100 users now which is my first foray into the marketing/sales side of things and any tips would be helpful. Also I didn't realize until later that the name, while I think is pretty cool, might be extremely poor SEO? :-)I also think that these kinds of post-app apps are a curious idea and will become more popular, although likely (hopefully not) through sms as the communication medium. I am off this week and plan to write some stuff about it but it feels really cool to remove the terrible CRUD UIs entirely from this part of my life. I tell my friends that even if it doesn't take off I'm never shutting it down because I enjoy using it over myfitnesspal/cronometer/macrofactor etc so much.

reply

xavigroup
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I left my job as a principal software engineer a few months back and have been working on an agentic harness and 
https://blackbear.app
 -- a local first, end-to-end encrypted everything app with file editors for notes, documents, sheets, free-hand canvases, slides, and a whole lot more. Also features a calendar and task system, and a lightweight discovery engine. There's a BYOK agent system (Pax) that works with you across the whole app (OpenAI, Anthropic, Gemini, and local Ollama support). Works in a browser, from the CLI, and from native mac and linux apps (mobile on the way). Not exactly sure my end goal yet, but it's been fascinating building these things

reply

mcapodici
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Hi. As you are deeply thinking about these sorts of things, I want to see what you think of my 
https://useorganizer.com
 which turns the todo idea on its head a bit by being timeline oriented.

reply

xavigroup
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Oh, and all the editors support real-time collaboration. There's messaging, voice and video calls, and a lightweight contact management system that I'm still iterating on

reply

philips
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What is pax?

reply

jimnotgym
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on cataloguing Murder Stones!

These were stone memorials placed where someone was killed, especially in the UK. Most of them are 18th-19th century. Some are lost.After watching a YouTube video about it and finding there was no definitive list, I registeredhttps://murder-stones.orgon Friday night and fired up claude code. There is very little on Wikipedia. I'm collating all the snippets i can find. There are a bunch of references I have collected which I'm sorting through with claude which has now run out of credits!I have been more focused on finding new stones than fleshing out the stories so far. I have a pile of sources.I have been researching manually for tidbits and feeding them to claude and asking what else it can find. It could find 8 to begin with but my research has got me up to around 33. There are some artifacts of that process still on the site... but it's day 2.Its still a bit janky, but it's only day 2 really. Stack is a csv file of maybes, being sorted into sqlite, generating a static site with a python script, push to github, host on netlify. I also have a quick local flask app to enable me to hand edit the db and force a rebuildhttps://murder-stones.org.I would love to hear about any leads!

reply

cube00
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Might be worth getting your licencing decided to let your contributors know exactly what their rights are.

As it stands it looks like everything contributed is owned by you with full copyright dispite the footer calling it a "public field archive"> I have a pile of sources.Gathering from open sources and then putting the content behind aCopyright © 2026 Murder Stonesisn't ideal.

reply

jimnotgym
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Correct. Not that anyone has submitted anything. I intend it to be creative commons by the end of the week! I just need a moment to read the licences etc.

reply

conrs
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm figuring out stepping stones in getting closer to user data autonomy. A natural starting place is our professional history.

So, I'm building a compatibility layer; something that works with everything - including your own vibe-coded personal CRM.It's already helping - even something as simple as correlating calendar events with new connections so that you always know where you met someone.https://tend2thrive.comif you're curious; It's live, so DM me if you'd like an account rather than just hitting the waitlist.

reply

beau_g
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on the chainsaw for my centaur form factor robot. Have one part to machine then just need to weld everything up and will be ready to try it out. It uses a motor and controller sourced from an E foil, and has 2DOF position control. 
https://www.satyress.com/buildprogress

I've also been slowly chipping away at a Jagged Alliance 2-like game in Godot. Nothing to share yet but if anyone else is also frustrated that there hasn't been a good video game since Jagged Alliance 2 and you want to work on it reach out to me through the contact in my profile.

reply

relssiegp
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

I recalled what it was about before even clicking the link, and I've only seen it once. You are really good at making people remember your products. The first time, I thought it was a hoax, or a FNAF variant because of the design of the robot and the tone of the website, but if it happens to become a real product, congrats, I hope you'll find success with it.

reply

sosodev
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I saw some coverage of your robot on social media. I honestly thought it was a hoax because of the very bold design and AI generated images. Cool concept, have you had any potential customers reach out?

reply

beau_g
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The images are not AI generated, they are just renders from CAD composited into photos or pure renders. I have received a lot of reach out from all sorts of backgrounds which is cool, though I am a very long ways from being able to sell anything, has definitely lit even more of a fire for me though to keep making progress.

reply

ventana
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I used to teach C to students many years ago, and with agents it's becoming a niche craft. C is still both an important and fun language to use, and I've been very slowly making a C language course to let beginners learn a bit about the language and practice writing simple code with no AI: 
https://c-course.com

A work in progress, and will stay so for much longer, I guess.

reply

relssiegp
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

I've always had a sweet spot for using C for pet projects. For some reason, I find it soothing to work with the language. I think there is still room for this language to be taught to beginners.

reply

jherdman
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is neat! I’ve been meaning to get back into C. I’ll give this a shake.

reply

narayanahari
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

We’re building Deckhand (
https://getdeckhand.dev
), an AI assisted, human in the loop platform for shipping and operating mobile apps.

We have built a few apps recently and what we observe is that while building the app has gotten dramatically faster with AI, everything around it still takes a surprising amount of human effort - testing, debugging, reviewing, store submissions, releases, monitoring, and keeping things running.Deckhand is our attempt to make that entire loop faster, while keeping humans in control. Would love to hear how others are shipping and operating mobile apps.

reply

dthedavid
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building an open source video editor fulltime.

https://github.com/DonkeyUseCorp/DonkeyCurrently doing this bootstrapped. I'm getting a lot of feedback from free users and barely any from those who pay. Quite interesting.

reply

laurentiurad
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I built and run several SaaS platforms:
- 
https://dave-bot.com
 -> a full-stack AI platform where you can generate videos, images, music, code, 3d objects with frontier Gen AI models.

-https://headsnap.io-> a platform that you can generate images of yourself based on 4 selfies.-https://quantiq.live-> a service providing financial and historical data for stocks, as well as government trades.-https://aivestor.tech-> an AI agent that picks small/midcap stocks and trades them using Alpaca API. It uses Reddit, news, polymarket, Google Trends and many other data sources to take investment decisions.- @Polyglot_lingua_bot -> a voice-enabled Telegram-based bot that can help you learn new languages.-https://select.supply-> a directory of carefully-curated and well-crafted products.All of those allowed me to quit my day job and live a comfortable and flexible life. I still invest time in maintenance and adding new features, but I love coding, marketing and everything that comes with promoting and selling a SaaS (and I also have a serious addiction for Stripe notifications).On top of that, I developed my own software agency where I help clients build and scale software (https://bitheap.ch).

reply

sbrother
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Trebella [0], a tool to help classical music students structure their practice sessions more effectively. I tried to build something similar ~10 years ago in the form of a more interactive music game, but felt like it wasn't actually that helpful for intermediate and advanced students. So this time I'm doing it in collaboration with actual music teachers and building a tool that actually helps me learn. I'd say 90% of my flute practice is done using it at this point, and I'm in the process of taking on the first arms length users in a closed beta. Please shoot me an email if you are interested in any way!

[0]https://trebel.la/

reply

joelm
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I got sick of being on Zoom calls and having things lag or glitch, and not knowing if the issue was something I'm responsible for or not. Is it my LAN/Wi-Fi, my ISP path, some broader Internet issue, or Zoom?

So, I built a tool to answer that. Major goals have been to keep low energy/cpu usage (so I can run it 24/7), have it adapt to the apps/traffic I'm using (rather than use static monitoring endpoints), and to deliver both at-a-glance answers in the menubar and in-depth detail in the dropdown.It's called Breakdown. It's a free (for typical uses). It's Mac-only for now (but if enough people ask for Windows I'll port it).https://breakdown.live

reply

sailorganymede
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

A PR quality gate which grills me to make sure I understand the code changes I am making before I merge. I have been working on an AI app which deals with vulnerable users lest I ruin the experience for my customers so I am a little bit hesitant to "go fast" but I find AI really helpful in my process.

I actually have been working on it for a little while but this is the first week where it's been quite helpful.

reply

0plus1
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been working on the latest update to my app: Wrote Myself a Letter which I finished after being laid off.
The idea is to send a letter to your future self, which I personally find very therapeutic in many ways, but what is important is the app is fully offline, has 0 tracking, ads or subscriptions. It's a once off purchase and own forever, which is something I wish was more common these days.
Check it out and, if for any reason you can't afford it just write me and I will send you a key.

Love from Australia:https://apps.apple.com/au/app/wrote-myself-a-letter/id647826...https://play.google.com/store/apps/details?id=com.zeropluson...

reply

jjcm
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

A diffusion-based UI design tool I left Figma to build.

My core hypothesis is that LLMs are trained to write consistent code (good for a billing function), but they also express design through code, resulting in consistent design as well.Diffusion models are just now good enough to do UI, and are trained on a much wider set of visual data, resulting in more unique outputs. LLMs are now good enough to convert images to code very effectively, so the end result is better even though you have to do a conversion.Here's a page detailing the standard flow:https://diffui.ai/blog/show-hnAnd here are a couple sample sites built with it:https://html.non.io/tarothttps://html.non.io/neonRamen(note - not optimized for mobile)And here are a couple files showing the designs (requires sign in):https://diffui.ai/app/canvas/9e03f5c2-91c5-4f96-8f08-b8086e5...https://diffui.ai/app/canvas/95934269-5dc8-4145-a33a-d3a4dc2...Happy to answer any q's!

reply

animeshjain
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

looking forward to trying this out!

reply

alphaBetaGamma
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

My wife and I are working on a math/science/CS-inspired jewelry business. We try to create pieces that stand on their own aesthetically but have a hidden meaning.

We currently have two styles: lambda calculus based pieces (we depict the lambda/Tromp diagram) where we have Y-Combinator earrings (well, strictly speaking they are one beta reduction away from Y-combinator. Aesthetic oblige) and a pendant depicting a lambda expression computing Graham's number. The other style is quantum computing circuits, based on quantum computing research my brother (a physics professor) is doing: a pendant that is actually a non-local controlled-NOT gate.
I wrote a tiny DSL to describe the jewelry pieces, and an interpreter to produce CAD files. We then either 3D print them or have them produced by lost-wax.We are 200% out of our comfort zone (and love it): I know nothing of front end dev, payments, or anything like that. The diamond district in New York is a neighborhood we normally actively avoid, but if you are forced to go there it is fascinating (people examining diamonds on the corner of the street, others in fur coats in summer straight out of a mafia movie...), and especial marketing. Jewelry is a completely saturated business (luckily we are not doing this to pay the rent); we think we have a unique angle, but we are still figuring out the target audience (if there is one), how to advertise, etc.Any ideas on marketing are welcome.Store:https://studio-galois.com/

reply

spindown
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

This would be perfect for the Computer History Museum gift shop:

https://shop.computerhistory.org/

reply

xkam
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> Any ideas on marketing are welcome

Maybe contact CERN - they have a souvenirs shophttps://visit.cern/shop

reply

andrevalleee
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I was actually facing a huge friction problem when it came to closing clients—both at my agency and in a wholesale business I run with my family—because the whole quoting and payment process was really outdated. So, I built a software tool to eliminate that friction; it’s like a live Notion-style interface where the salesperson and client can update the quote and communicate via a public link. That same link allows for approval and payment—using cards or bank transfers, obviously via the Stripe API—and handles everything related to invoicing and sales. It ended up being really useful for my agency, too, allowing me to send clients more professional quotes with a detailed project breakdown so they can clearly see what the work entails and understand the pricing. Honestly, I’ve definitely noticed an improvement in sales.

reply

ruthvik947
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on something to help us pursue our long term interests in a reasonably more structured way: 
https://pond.li
. The basic problem/idea motivating it is that it'd be valuable to reach more often into our archives/collections (or have them reach out to the present) than be pulled into the great big, novel firehose of information we're exposed to everyday.

It's also an attempt to make use of LLMs as not primarily chat partners. Keen for feedback if any of this strikes you as interesting

reply

SleeperShip
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.play-when.com/daily

When? Is a timeline game I've been working on for a bit. It's a board game I love playing with my family and I wanted a slicker mobile version I could play with them.

reply

properbrew
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

I didn't quite understand what you meant from your description, started playing it and love it! Educational too!

reply

jason_zig
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Solo founder (and sole employee) getting to 2M ARR with Zigpoll[0]

AI is making it possible to go after bigger clients so the strategy is to focus on marketing and going upmarket. A lot of new features to add and things to learn as you move up to bigger customers with larger contracts![https://www.zigpoll.com]

reply

bouk
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I've built this website which shows the land registry data (Kadaster) information of The Netherlands but with nice vector graphics and much more performant than other websites I found: 
https://kadaster.club

Turns out there's an incredible organization here (of course) that publishes many geospatial datasets:https://www.pdok.nl

reply

ciju
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://finbodhi.com
 - An app for your financial journey. It helps you track, understand, benchmark and plan your finances - with double-entry accounting. You own your financial data. It’s local-first, syncs across devices, and everything’s encrypted in transit (we do have your email for subscription tracking and analytics). Supports multiple-accounts (track as a family or even as an advisor), multi-currency, a custom sheet/calculator to operate on your accounts (calculate taxes etc) and much more. Supports price fetching for most Indian investment vehicles and US stocks. You can create custom dashboards with leading/trailing/rolling charts for investment options and benchmark.

We will soon add more import conveniences, like asking your llm to generate importer for your special pdf formats. Seehttps://finbodhi.com/changelogfor details.We also write about related topics:We wrote about comparing investment options:https://finbodhi.com/docs/blog/compare-chartsBenchmarking your returns:https://finbodhi.com/docs/blog/benchmark-scenariosUnderstanding double entry account:https://finbodhi.com/docs/understanding-double-entry

reply

ingvay7
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

thanks for letting user see the demo dashboard without asking for email etc. Looks useful

reply

brirtch
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Proxigem, an app (Android only right now, working on iOS). It shows you history, notable people, census stats (some countries), Wikipedia articles and other points of interest around you. Built to work offline so no connectivity needed when travelling.

https://www.proxigem.com/

reply

Quizzical4230
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Finally started (again) learning rust!

So many more languages have been added to the basket after reading:https://www.norvig.com/21-days.html

reply

wetoastfood
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been working on something to help our family plan things better. We have two kids now in elementary school and both involved in extra activities. Registration dates, birthdays, game times, etc. are a lot to keep track of. We both have work and personal calendars and never sat down to plan which calendar gets what. Maybe that would’ve been easier! In any case, I built Mavo to try and centralize that stuff and see if I can make it more proactive than just a calendar.

You send it your events via email, online, in-app, or text message even, and it puts it into your calendar for you, letting you know if there’s conflicts and keeping track of who is assigned to what, not just who’s attending or not. My goal is to have it proactively notify you when there’s potential issues like rain, traffic, or something else.You can connect it to ChatGPT, Claude, or other agent through MCP so you don’t even have to use the built-in AI. And there’s an API, SDK and CLI for those who want to tinker and build custom displays or interactions.There’s an always-free version to get started and try it out. You can find it athttps://mavolife.com

reply

bizzletk
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Can you explain why this would be better to pick up than OpenClaw/NanoClaw/etc?

reply

wetoastfood
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Mavo is currently trying to solve a much smaller scope of problems: can it help alleviate some stress that comes from a busy family schedule.

For my family, this means making it not only accessible to me (a developer), but also my wife (who’s not), and potentially other family or helpers (who likely aren’t). That means I’m designing it with accessibility in mind: there’s a full featured GUI so you don’t have to talk to the AI to make changes if you don’t want to, events have built-in owners so you can assign someone or even round robin things and get notified if no one has an event covered, you can share a link with the grandparents to give them details that stay up to date, and, most importantly, you get these things out of the box without having to tinker (but you can go deeper if you prefer).I’m not aiming for it to be a fully autonomous agent, but I’m definitely thinking about ways to make it more proactive. Events in the system, for example, have an internal notification that can wake Mavo up to check on things without pushing an alert to the house unless it’s needed.

reply

gogo61
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a cat themed word puzzle game with two friends.

It will have all the top word games in one place with more coming over time.I always wanted to build games, and AI finally made it possible for us to move fast across UI, level design, coding, and even video production.Android:https://play.google.com/store/apps/details?id=com.superfun.w...iOS:https://apps.apple.com/us/app/kitten-word/id6785978180

reply

binsquare
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

A lightweight ,portable virtual machine that simplifies/replaces need for containers.

https://github.com/smol-machines/smolvm

reply

baist0
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

I love small or tiny good products. suckless soft - it's good!

reply

voakbasda
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Recently bought a Sovol SV08 printer. It comes with open source binaries, but there is no source code. Turns out they are a known to be violating the GPL. Looks like it can be rebuilt from other sources, so I have started to put together a clean implementation using Yocto. It will be possible to add support for similar 3D printers.

I bought that printer in order to print parts for two other projects: a baby monitor (security camera) and a hat-mounted teleprompter monocle. Both using COTS part and running Yocto-based open source images. All affordable products in both of those sectors arecompletely untrustworthyor otherwise unsuitable for my requirements, since one of which is total replacement of the firmware with my own custom versions.In my day job, I am a principle embedded engineer consultant working on distributed embedded systems, so all of the above software will be relatively easy.The mechanical work will be the most challenging, as I am presently only using OpenSCAD. I would entertain suggestions for alternative open source CAD solutions, but I hope to recruit a ME (or two!) to help drive that portion of the work to completion.

reply

mrheosuper
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a simple device that can automate watering my plant.

The first version is just simple box that controlling a bunch of valves to control waterflow, quickly learn my mistake that i have to route every wires into that box(at least 2 for power), the bigger your garden, the more wires you use.Now the current version use Modbus over RS485 so that i can daisy chain the valves, and can extend more valves without compiling new FW.The master node uses esp32 and the slave node uses the cheapest mcu i can find(Puya py32)Sometimes i just want a simple device like that, no home assistant or anything, have been bitten in the past.

reply

pythonRon
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Wow, that's so much more ambitious than what I'm doing. I'm learning Flet so I can build a multi-headed timer for cooking.

reply

sureshjayanthi
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building replaypics.com. After an event, photos are scattered amongst phones and whatsapp. Difficult to search and retrieve. Creating memories on Google Photos requires some amount of effort. Started working on it after a family vacation - we had more than 400 photos across 4 phones and we had not looked at them after returning home

Replaypics allows a person to create an event and upload pictures, optionally invite others to upload their pictures. It selects the best and makes 4 collages and 2 videos (portrait and landscape). The videos are set to music that is selected as per the mood of the photos, cuts synced to the beats.Trying a different monetisation method: Albums are free to create, users pay only to get the share link. Curious whether people will pay at the share moment.

reply

bmmcginty
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm writing an add-on for the NVDA screen reader to allow users of Jaws to "seamlessly" migrate to it.
Also a financial tool that answers “how much money can I actually spend?” by forecasting your cash balance through upcoming bills, cards, income, and transfers. (I'd love to turn this into a product, but I think the market is full as it is.)
I also just completed a bare-bones web-to-mumble system because the app for the iPhone is...lacking.

https://github.com/bmmcginty/wumble

(To be clear, "I" is AI with human testing and reading over the code.)

reply

thecopy
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Im working on an extensible and flexible agentic connectivity platform (MCP, OpenAPI/Swagger, FaaS) with niceties like built-in CodeMode, compression, SIEM integration, access token forwarding, SCIM 2.0, on-demand agentic sandboxes (e.g. LangChains "Deep Agents").

For private use not that useful tbh (although i found the OpenAPI -> MCP mapper useful), but found sales success with organizations with more complex agentic setups.Gatana:https://www.gatana.ai/

reply

properbrew
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Still working away on a completely offline meeting document generator that works on generic laptops with no GPU (
https://whistle-enterprise.com
). A new release coming very soon focusing on getting clearer audio which in turn makes the transcription and end document generated more accurate.

Inbetween that I've been working on a "software house" (don't know how else to describe it). Pretty much codex/claude running on a VPS with a web interface and the ability to actually build and publish software / webapps etc.It came from me sitting on the train on the way home and I had an idea pop into my head for a pebble watch app, I wanted to build it and test it there and then as I still had about 45 mins left. I know you can run codex against git repos in the cloud but I didn't want to faff with that (and last I remember the allowances for this were much less generous). It's been really fun, probably many things like this out there but it works exactly how I want it to. I plan to open source it once I've tidied things up a bit more.

reply

1024bits
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm continuing to work on Totem [0], an offline-first, local-first, team all-in-one workspace that features live collaboration, databases, and agentic workflows. The desktop apps are built completely in Rust (without Tauri or Electron) and are functional (with a few early users trying them out), while the iOS app uses the same core libraries but with a Swift frontend and is in TestFlight beta. I'm still waiting on Apple to approve the iOS release, among other things, before sharing more broadly.

[0]https://totemkb.com

reply

mlitwiniuk
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Still making fellow founders' lives easier when it comes to SOC2/ISO27001. AuditBadger (
https://auditbadger.com
) is a compliance management platform where AI drafts policies, controls, risks, business continuity plans, and so on. Humans are always in the loop; everything needs to be signed off (I don't believe in either of "we do compliance for you" or "AI can do compliance for you" approaches). Currently working on revamping our asset management features to fully and perfectly support NIS2.

reply

coldstartops
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

KeibiDrop: A Peer to Peer Network latency hiding filesystem:

You can work on shared files instantly without uploading or downloading them.1 minute video:https://www.youtube.com/watch?v=9Wt0NMx2_I8Github repo:https://github.com/KeibiSoft/KeibiDropSince last month hardened bidirectional edits such that people can work on video assets with Premier Pro, DaVinci, and such.Got a pre-alpha release, where we managed to split congestion control over QUIC and bulk data transfers over TCP, and the lockless conflict resolution :D

reply

sawirricardo
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Hi, i have been working on 
https://myvivaldy.com
, it's my clinic/business OS in healthcare industry (is this what the cool kids say nowadays?), Id say it is like SAP made just for this clinic OS. Especially since the Claude Boom at Dec 2025, I intensely improve this clinic from simple reservation/encounter services into full-fledged clinic OS. Users are mostly employees and patients. mostly report positive feedback. and since this industry is highly regulated (Hi FHiR v4), with the help of AI I can fulfill any major concern and whip up PoC. I can also experiment with features which was previously not feasible due to time/energy/skill constraint. Whatever make sense for user experience imaginable is a few prompts away now.

Love to help others if one wants to build their own business OS especially if you're in medical/healthcare industry.

reply

andrewjk
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Multi-language libs with implementations in TypeScript/C#/Swift/Zig so that they can be used directly in web or native apps:

- A Markdown parser/renderer (https://github.com/andrewjk/allmark). The TS version of this was hand written and the other versions are AI translations.- A Git client (https://github.com/andrewjk/gitologist) and a diffs parser/renderer (https://github.com/andrewjk/differator). These were vibe coded in TS, checked and then AI translated.I’ve used these libraries to build a native Mac Markdown notes app (https://staunchapps.com/stash) and a JS script launcher (https://staunchapps.com/launch).

reply

nbbaier
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Are the creator of the `.mdsv` format that's referenced in the stash manual? Never heard of it before. If you are, interested if there's a spec.

reply

andrewjk
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's just a text file containing a single Markdown table. Making it a different extension seemed like the best way to force them to open in a different editor view inside Stash (while keeping them editable with any other text editor).

reply

wbobeirne
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I'll be flying to Edinburgh for the Fringe Festival in a couple of days, and I've been putting together a much better app than the official one. It builds the full catalog of shows as a sqlite database and syncs it to your phone so that you can filter, search, sort, and build a schedule even with the traditionally spotty data during the fest. I also added a bunch of coordination features for planning your Fringe with friends.

It's a PWA, not a native app over athttps://fringeflypost.com/(or you can go directly tohttps://fringeflypost.com/showsto browse if you don't want to make an account.)

reply

nha1
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Nice I love the Fringe. I don't suppose there is an easy way to track the street performers though which for me is the fun part.

reply

denizeren
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building 
https://promptship.dev
 for a while now. Basically a cloud where the operators are the agents not the humans. The platform allows agents to attach DBs, clone envs with data (instant prod like env for testing, etc), per-env access tokens for agents, append-only logging/traces for agent actions.

It's been quite useful for our small team and we plan to open this to public beta, soon.

reply

lpsatwork
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Interesting to see the distribution of projects here. For people building something with the intention of eventually making it a business: what was the strongest evidence that the problem was worth pursuing before you started building? I'm especially interested in cases where the initial idea changed substantially after talking to users.

reply

mskalski
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Yesterday I reached a stopping point in a project I had been working on over several weekends. I wanted to connect my illumos server directly to my Japanese ISP through DS-Lite, and ended up writing and publishing two Rust crates along the way.

The tunnel itself worked, but stock illumos could not manage the DHCPv6 prefix delegation required by my connection. I also spent quite a bit of time tracing a four byte ABI mismatch between a 64 bit Rust process and a 32 bit illumos service.There was no happy ending, but I learned more about the illumos network stack and distilled the experience into a blog post:https://skalski.dev/connecting-my-illumos-box-to-a-japanese-...

reply

molvqingtai
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I recently reconstructed my chat extension using AI, which has enabled functionalities that were previously difficult to implement. The downside is that I can no longer understand the project code.

reply

tito
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on reversing climate change. Carbon dioxide removal.

Also getting curious about mechanisms to prevent damage from high temperatures in the short term. There's a project over the Great Barrier Reef I've been digging into what mechanisms they're using:https://barrierreef.org/news/explainers/what-is-cloud-bright...

reply

Schiendelman
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

How are you removing carbon dioxide?

reply

megabless123
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Tito founded AirMiners! 
https://airminers.com/

reply

tito
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

hey thank you for the shout out!

reply

ww520
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Succinct data structures. Finished the indexable bit vector, with nanosecond rank/select operations. Working on the range min max tree based balanced parentheses succinct tree structure, with support for the usual tree navigation and operations.

reply

chicagobuss
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

what a cool answer

reply

the_florist
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

As usual, I’m chipping away at my highbrow app for readers and writers. It’s an authoritative dictionary, a reverse dictionary, a spaced repetition system for vocabulary building, an e-book reader, and now a portal to Wikipedia.

I dare say it’s one of the most polished PWAs in existence, especially on iOS. Nevertheless, I’m experimenting with a Capacitor build, because most customers and visitors use the app on iPhone, but few are aware of Safari’s “Add to Home Screen” feature, so they miss out on the optimal UX. Also, the app could use the exposure and user trust of the App Store, as well as flourishes (pun intended) that Apple does not extend to PWAs, like haptics and a Liquid Glass icon.https://flowery.app

reply

magarnicle
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Daresay is appropriately flowery, but it is in fact just one word, not two. I daresay you need to use your own app more :p

reply

the_florist
 
44 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The pot calling the kettle black, methinks.

http://flowery.app/words/I%20dare%20sayDictionaries accept both forms, but the two-word phrase predates “daresay,” originating in the 14th century according to the OED.

reply

hamilton_app
 
52 minutes ago
 
 | 
prev
 | 
next
 
[–]

A vibe-coded front-end to Google Health Connect that displays all health metrics that Health Connect holds in one gui.

It's an attempt to get round the fact that various health apps and vendors pick and choose what they share or show from other sources.

reply

linuxrebe1
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I too got laid off at the end of April. So what I've been working on since then has been AI. But of course, being the contrarian that I am, I'm trying to make small language model AI usable. The end goal is to complete all the pieces I need to create an AI empowered tool that you can point at an authorized Network, and it figures out on its own. What needs to be monitored. Learns what normal looks like on your network. Build your dashboards. Working both as systems monitoring and network monitoring. So right now my GitHub is full of both things that I need, for personal use, in this goal. Also with things that I need because they will become tools for the final product. 
https://github.com/linuxrebel
. You'll get to see my contorted mind at work

reply

Metricon
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Still in beta with Verse Draft: 
https://versedraft.com
 - An all-in-one writing studio where fiction writers can keep all the details for their universes in one place while crafting stories, novels, movie scripts, TV series, or stage plays.

One surprising finding is how few people are interested in real-time voice interaction (transcribing, dictating, conversing with assistant), so that's been removed for now.

reply

bogzz
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a tool for visualizing biological pathways, pulling data from the Reactome knowledge graph for now. Trying out different graph visualization algorithms, it's an interesting problem space as they are all approximations to solving a problem that I believe is NP-hard-- arranging a graph such that all vertices are distinct and you have the global minimum of overlapping edges. Next step is implementing a novel algorithm that I found described in a dissertation that doesn't share its code. Unfortunately it's not deployed yet, but if anyone seems interested I will be sure to share it on HN when it's in an acceptable state.

reply

Yzhang1337
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

I’m a physician and interested!

reply

michaelbrooks
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been building a social network for Twitch, called Chattr. It is very Twitch specific as you log in with Twitch and it will automatically post when you go live. When your stream ends, it will automatically post the VOD to your followers feed. Also, if anyone who follows you on Twitch joins Chattr, then they will automatically follow you on the site too. This makes it much easier to move your community over.

You can also tip and receive tips for your posts, which can then trigger a stream alert.You can use your own custom emotes in posts and your Twitch subscribers can also use them.I'm really excited to be building this and we have 135 users signed up.https://chattr.onlineis the link and the app is on the Play Store and Apple App Store

reply

MiroslavPokorny
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Im working on what i call a spreadsheet data platform. It looks like a spreadsheet but all the components are plugins which means the user can provide (even write their own).

- Dont like the limited functions available in formulas, write your own. Yes i know this isnt new, just highlighting a starting example.- Dont like how values are formatted in calls, write your own.- Dont like templates, write your own script that generates the "empty" or not so empty spreadsheet.- Dont like clicking on icons, write your own scripts or plugins that execute in context, which makes snippets to do basic things become very brief, because theres no need to load and save the file with the spreadsheet or even select the range with a query.- Want a terminal, i have one. Everything in a spreadsheet is a file, just like *nix. Read/write a cell, is as simple as reading /cell/A1.txt or /spreadsheet/123/cell/A1, because the environment has smarts like environment values (eg SPREADSHEET_ID) that are used.I have many other ideas which are nearly there.https://github.com/mP1

reply

random-exceptio
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm polishing my new VR games (Meta Quest). Actually they're just rewritten versions of my older games (one Soccer and one Basketball), but now focused on international tournaments with updated gameplay and graphics. I have no licensing for the player names and tournament names are also not fully real for same reason.
I don't expect big traffic, due to plenty of other games that are far better, but the process of making is really enjoyable :)

If you want to see here are the linkshttps://basketballnations.artisoft.pl/https://soccernations.artisoft.pl/

reply

karolist
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on PhotoFig: 
https://photofig.com
, a recently launched product-photo editor for online sellers who need to clean up hundreds of images.

It was inspired by my wife having to carefully mask product photos for her online shop. Existing tools could remove backgrounds automatically, but didn’t give her enough control when the result needed correcting. So masking is a first-class feature, with SAM-assisted selection and a precise manual brush.The backend and storage are self-hosted on hardware I own. Along the way I’ve had to solve some interesting infrastructure problems, including writing a Kubernetes operator that bin-packs GPU workloads across workers. I’m planning a technical write-up on the architecture.

reply

AngryGoblin
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Was reticent to post my game on here but it looks like I wouldn't actually be alone which is nice! I've been building an eldritch horror peggle survivors-like (genres are fluid ok), which has been on a bit of a mad journey from beginning as some sort of bloodbowl flavoured subbuteo, to a gravity well air hockey game, to what is now known as Disciple where you feed a hungering Abyss-god by launching yourself into it and collecting enough essence on the way down to make sure it lets you live for another go. There's builds and esoteric shops and different map biomes and enemies etc. I think its a lot of fun.

Twitter, sorry X, weirdly has a really nice and welcoming game dev community so I've mostly been posting about it over there where you can check out progress posts:https://x.com/AngryGoblinDev

reply

bryanhogan
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building the easiest way to start your own high-quality blog: 
https://github.com/BryanHogan/astro-starter-template

Astro is a framework that uses no JavaScript by default. I also use just HTML and CSS, so no bloated additional frameworks or styling libraries.All blog content is written as Markdown or .mdx files, so it's easy to write and move to any other tool if you wish to do so.You can host it for free using any major provider since it's just a static website (e.g., GitHub Pages, Cloudflare, etc.).Making it similar to my own website which is on:https://bryanhogan.com/(Repo:https://github.com/BryanHogan/bryanhogan)

reply

aaronbrethorst
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I work on a suite of open source public transit software projects, collectively called OneBusAway (or OBA). The software is used by millions of transit riders every day around the world, including in New York City, the Seattle area, San Diego, and Washington, D.C.

Through the non-profit that collectively owns OBA, I've been working on a managed services offering to help transit agencies adopt the software, which has historically been beloved by users, but a real pain to set up and maintain. The software, cleverly named OBA Cloud, turns what used to require a month-long engagement with a transit consulting firm into a 15 minute, wizard-driven process.The best part is that since all of the software is free and open source, a transit agency that decides they love OBA but wants to be locked back into an expensive contract can always ask a consulting firm to run the software for them.Since last month[1], we've added a number of great new features to OBA Cloud, like broadcasting critical alerts to all riders in the system via push notification, and support for Live Activities on iOS.We're hosting four new public transit systems over last month, and are continuing to make terrific strides on our other marquee projects:The iOS app update went live, and our riders are generallylovingit:https://apps.apple.com/us/app/onebusaway/id329380089The new Android app maintainer is gearing up to release the biggest new version of the app in a decade:https://github.com/onebusaway/onebusaway-android/Our GSoC interns are continuing to do amazing work on their projects, including the next generation OBA API server, Maglev:https://github.com/onebusaway/maglevWe're always looking for more folks to contribute to the project, across a variety of disciplines (ie not just engineers!):https://ossvolunteers.com/organizations/open-transit-softwar...[1]https://news.ycombinator.com/item?id=48888489

reply

thisisharsh7
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Hi, what's the best way to get involved is by just keep contributing or do I need to apply on the OSS volunteers form first.

reply

willmeyers
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Hey! I just posted in this thread about my work on building a better CTrail app. I live in NYC - would love to get involved in this. Thanks for sharing!

reply

aaronbrethorst
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Hey Will - I'd love your help! You can either go through the OSSVolunteers link above or just review this document, which includes a direct link to join our Slack workspace: 
https://opentransitsoftwarefoundation.org/onebusaway/contrib...

reply

danparsonson
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Finally started writing that Game Boy emulator I've always wanted to make - C# on Linux, planning to use SDL for the display and maybe NAudio for the sound.

reply

bredren
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on Contextify, which backs up your Claude Code and Codex conversational history and makes your entire history available via a skill or mcp.

Contextify (https://contextify.sh)It is very flexible, you use it the normal flow of CLI AI conversations:1. Resume unfinished work → "where did we leave off on that?"
 2. Recover the intent/scope → "what was the actual goal of this whole effort?"
 3. Verify it got done → "did we ever finish that, and which session proves it?"
 4. Recall a fix → "how did we fix this the last time it broke?"
 5. Reconstruct a decision → "why did we go this way instead of the other one?"
 6. Branch/PR archaeology → "what was this branch even for?"
 7. Recall a plan → "what was the plan we landed on for that?"
 8. Activity over a window → "what did I ship or close in the last few days?"Just add "use total recall" or invoke the skill directly via /total-recall or $total-recall.You can self-host your database to keep it local and sync your history across multiple computers. The local server is source available under FSL-1.1-Apache-2.0.There are macos and linux clients, and I'm pretty close on a windows client. All share a common Swift-based core.

reply

thoughtpeddler
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

Great work! Love the harnessing of Apple's local inference. Wondering if you'd be willing to support the same conversational export, summarization, and search/retrieval flows but for the consumer platforms (ChatGPT and Claude) that have local conversations stored? (e.g. I've seen that local Claude Cowork conversations are stored in some kind of JSON-based schema that might be similar to Claude Code, but I'm really not too sure).

reply

thepoet
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I have high myopia that is progressively getting worse so started working on building an app development platform for my Kobo eReader so that I can live without my mac and phone. 
https://github.com/BandarLabs/Cobalt

Have built the SDK and some apps like an HN Client, ChatGPT client, Claude Code permissions sidekick, RSS Reader, some games etc. (all in the same above repo)It has 8x less powerful hardware than a modern raspberry pi but runs Linux with an eink display, wifi bluetooth and a good battery life for $100 or something.

reply

vladkorobkov
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Being a big fan of the server-side rendering, HTMX, Tailwind CSS, and Alpine.js, I am working on a fast dependency-free, typed Mustache renderer for Python 3.12+. 
https://github.com/servletcloud/fstache

reply

ChaosOp
 
55 minutes ago
 
 | 
prev
 | 
next
 
[–]

Working on a web-based local multiplayer party game platform called GamingCouch.com.

The idea is simple: I love local multiplayer games and game nights but felt that there was always too much hassle with switching between different titles and connecting 4-8 controllers to one PC or console. Jackbox worked great but they relied too much on language and didn't work when the group had people not fluent in english.Therefore I decided to create a site that is dedicated to action-oriented party games. So no trivia or language based games. When I first showed the idea here on HN, other forums and game fairs, I received a lot of questions from fellow game devs asking if they could bring their own game ideas to the platform as well. I started to work on third-party development tools, which are now in private beta. Last Friday was a big moment as the first 3rd party game was launched on the platform!!https://gamingcouch.com/blog/protostellar-impact-launchI'm now looking for more game devs interested in making fun party minigames, if you're interested, check outhttps://gamingcouch.com/developersand hit me up either here, by mail (from my profile) or by joining the community Discord and pinging me!The TL;DR of Gaming Couch:- Free Early Access with +20 competitive mini-games.- Players use their phones as controllers (gamepads work too).- Completely web-based, no downloads or installs needed.- Every game supports up to 8 players and is action-based, with quick ~1 minute rounds to keep a good pace. No language-based trivia or asynchronous (turn based) games.

reply

modsushi
 
44 minutes ago
 
 | 
prev
 | 
next
 
[–]

lingotok.net Use tiktok content to learn languages.
I find interesting stuff on tiktok in my target language and import in lingotok. Its free for now.

reply

ryanrasti
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Typegres - SQL over RPC safely (safely compose queries over Cap'n Web):

At a high level:
1. Define your schema: TS classes model each one of your underlying tables.
2. Encapsulate your schema: Add methods on those classes (encapsulation 101 applied to your database) -- that compile down to SQL. This gives you the equivalent of computed columns and first-class relations
3. Expose your API: explicitly mark members of your classes to expose
4. Use it: Now - and this is the crazy part - the client (e.g., a web browser) can use your data-model directly to query data with SQL-level power (joins, aggregations, etc -- compiling into a single query) over RPC, securely!Real example visuals are better at describing it:https://typegres.com/Recently added SQLite support and live queries; playground shows the live queries:https://typegres.com/play/

reply

edumucelli
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I am still working on a Linux dockbar for X11 and Wayland, it has all the goods of dockbars I have been using throughout the decades now, 60+ applets baked in, fairly good customization, etc
* 
https://docking.cc/

* 
https://github.com/edumucelli/docking

reply

yashness
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been working on suits of products. But the one I'd standout share is my personal productivity pet peeve. After using pushover & ntfy.sh for agent progress tracking. I felt the need for more.

A notifier which knows what agent is, allows you to approve certain decisions you'd want to be part of, while still running the agents in autopilot mode.It periodically notifies you about agent progress & moreover, sends you proof of work artefacts like screenshots, plan.md etc files so you can review on the go.This is the missing piece of harness, which truly removes baby sitting terminals.It's one click install & installing ios mobile app. Android is coming soon.
curl -fsSLhttps://notifier.aicrew.in/i| shTry it out athttps://notifier.aicrew.inReach me at getnexaitech [at] gmail [dot] com

reply

hknceykbx
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Refreshing my math. With ai being just dev seems to get more boring w time hence will probably have to pivot to data science ml. The goal is to be able to read papers on ml / data science hence probability and statistics, after that / in parallel tensors and all that stuff. I used to somewhat know that so it shouldn’t be too hard

reply

naiquevin
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on my guitar practice app, Captrice[1]. Last week, I added an interactive metronome tutorial[2] in the app to help onboard beginners (quite a challenge). This week I'm planning to implement the long pending "device sync" functionality - currently it's a local-only webapp (it's all static pages; no backend server). So for the past couple of days, I've been learning and evaluating the existing sync solutions.

The app has been my long term side project for more than 2 years now. I've been playing guitar for more than 20 years, mostly as a hobbyist. It started as a personal project and I've got immense value out of it in terms of speed building and consistency of practice. I believe other guitar players can find it useful too.A few months back I got a burst of inspiration to pursue it more seriously. After my last contract ended, I've been primarily working on it. Eventually I may go back to contract work again but for now I'm excited to spend dedicated time on it! Do give it a try, or share it with guitar players in your circle.[1]:https://www.captrice.io/[2]:https://app.captrice.io/metronome-101

reply

tosh
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

smol, a smol agent harness in 9 lines python

https://smolenv.comalso has minimal implementations in clojure, go, php:https://github.com/smol-env/smolcheaper, faster, less peak RAM per task than OpenCode, Hermes, Codex, pi:https://smolenv.com/t/nested-template-includes-60636/https://smolenv.com/t/duckdb-sessionization-23811/exploring what the minimal setup is for an agent to work well

reply

jjcm
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

A fun golfing project, but:

> smol is so smol you can understand it in an afternoon> smol is easy to adaptI would argue that golfed code is not great for these. Asking a LLM to expand out the code and comment it results in very concise, easy to understand code - nice job on that front, it's very simple. The blurb just isn't readable as-is.

reply

tosh
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

ty for the feedback!

i will also provide ungolfed versions

reply

tesnorindian
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

smol code has RCE risk granting model unrestricted access to local environment.

reply

tosh
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

that is by design

intentionally moving the security boundary to where it should be (the environment)

reply

iamflimflam1
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a totally vibe coded clone of Elite - 
https://github.com/atomic14/harmless
 - so far it's pretty playable.

You can try it out here:https://harmless.atomic14.comI'm planning on doing it Open Vibe Code. Add an issue and I'll set Claude on it.PRs will be rejected out of hand. I don't want your code. I want your words.It's just a bit of fun to see what's possible.

reply

relssiegp
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

That seems like a fun idea, but are you going to vibe code this indefinitely? What if Claude fails because of to the increasing complexity of the code, are you gonna abandon the project?

reply

iamflimflam1
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It’s a good question. To be honest, I don’t know yet. In the past couple of days it felt like I might have hit a wall but it turned out a lot of cruft and cargo curled ideas had ended up in Claude.md…

At the moment I’m having more fun adding features than playing it.

reply

socketcluster
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on the backend your AI doesn't have to build 
https://saasufy.com/

For vibe coders.With a focus on:- Security- Analytics- Advanced data sharing scenarios- Realtime updatesClaude can be given full access to your control panel and can impersonate any role to exhaustively test all your data models and views. So even a fool can exhaustively prove the security of their application for all data in their system.

reply

zitterbewegung
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m attending defcon 34 and I vibe coded an image sharing app running on the badge 
https://github.com/zitterbewegung/dc34-baogram
 . When you share a picture you have taken you also digitally sign each picture you share so people know who took the picture . You can also upload arbitrary images using your computer.

reply

runeb
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

In the last few months I have been building an AI assistant that is quite possibly saving my life.

It's an iOS app that uses LLMs to estimate and track nutrients and calories in all the food I eat. It is plugged in to Apple Health so it sees all my activity, sleep, body metrics, etc. I have set some general health goals in the app and it uses this to rate (poor, neutral, good) and advise me on the food I log. A calendar view shows how each day has gone in a traffic light coloring system. I can also log contextual notes to help it make sense of my day, and it has a memory system so each session has continuity.The assistant can save extracted or inferred nutritional data in a library, like when I give it photos of nutritional labels for foods I eat frequently or I log the same thing repeatedly, for easy reuse later. Also useful for home made meals and recipes.I've connected it to my workout tracker app Hevy so it can keep tabs on my exercise and also adjust my programs based on me chatting with it in the app about how a workout went. This is really useful for swapping out exercises I struggle with, for example, or to keep a well-balanced program over time.Recently I added an Apple Watch companion app with a watch face complication so I can keep an easy eye on things like up-to-date calorie deficit.All built in Swift with Opus on the $20 plan. I realize I can probably use existing AI nutrition tracking apps, and probably also connect Claude to Apple Health, but the joy of building and getting this to be completely tailored to me has been so fun and extremely useful. I've shared it with a few friends, but since I am paying for all the API tokens currently I have not yet tried to get more users onboarded.

reply

Havoc
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a web-reader tool of the kinda you might hook into an LLM as a MCP. Wanted to see how far I can get on my own rather than using something commercial.

Surprised how difficult it is to get anything usable. The web really has turned hostile - anything not on a residential IP gets blocked by like 50% of the sites no questions askedI guess they're all responding to mass scraping

reply

CharlieDigital
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm (solo) spinning off the internal agent knowledge and observability layer used at Motion (YC W20, series C, ~40 devs). It was born out of a need to lift all devs using heterogeneous models, harnesses, and prompting styles to a higher level of consistency and quality while surfacing the visibility to see what's working and what's not. The knowledge layer is integrated into the code review layer and all of it tied together with telemetry to the document section level to see how each piece of context is affecting code generation.

Open source repo (.NET 10 + C# + Postgres):https://github.com/zeeq-ai/zeeq-appDocs and more info:https://zeeq.ai

reply

ppnpm
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building Segue: an infinite canvas and keyboard-first mind maps application for windows desktops. I am trying to keep it minimal and only necessary features like text node, sticky note, ink tool and images. Later I shall add more productive feature and less unnecessary tools and features.

It has completely local environment and has no servers. Your files saved as SQLite database files per board. This means you have nothing to set up. No account, no sign-in, no sync settings. Just open it and work. You can use git or Onedrive to sync your SQLite files.The code is open-source on GitHub with MIT license. I am using claude to build it in C#, Skiasharp for canvas and WPF UI.If you are interested to take a look, please check it here :https://github.com/ppnpm/segueThanks,
Ankit

reply

jov3
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Hello-- I've been building Astrotechne, a modern technical astrology workspace.

I wanted to experiment with building my own ephemeris and calculation stack, and refine my agentic development workflow... and honestly make astrology software that doesn’t look like it was made in 2004.I started with asteroid calculation software, because much of it is Windows-only, and really inaccessible. (For the best one you literally need to email a guy to get it)A friend also asked me for a replacement for the old PlanetWatcher.com-- a site where you could use a time scrubber and animate through a chart (it's no longer around)Inevitably, the project has expanded into so much more... It's been a great way to experiment with MCP, different agentic coding processes, and to test some of the custom harnesses and context management tools I've been hacking on.Check it out!https://www.astrotechne.comJove

reply

D13Fd
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I have a keyboard I bought in 2020 called the Makerdiary M60 keyboard. It runs Python, and over the years I've coded in various functions. But it was somewhat buggy, and the upstream firmware was never upgraded.

I love the hardware because it's the only keyboard I've been able to find that keeps a live Bluetooth connection and lets you toggle back and forth between USB and Bluetooth instantly using only a keyboard shortcut. That means you use two computers, and switch back and forth as fast as you can type. Years ago I also added a feature that changes the backlight color based on the active connection, so you can instantly tell which computer your typing will go to. I haven't been able to find any other keyboard that's quite as nice.Lately I've spent weeks using an LLM to update the extremely old keyboard firmware to the latest firmware of its components (e.g., Circuitpython, the BLE firmware, the boot loader) and implementing all of my dream keyboard features that I never had the gumption to spend hours implementing pre-LLM. I finally resolved years-old bugs, and I added things like layer-based backlighting (so that the individual keys with relevant functions are lit), a better battery gauge, better sleep/suspend timing, backlight calibration, better debounce, and so on.I've also upgraded the hardware and added batteries to each of the keyboards (I have three of these, one at home, one in the office, and one for travel).It has been a very satisfying project, finally scratching a years-old itch.

reply

RealityVoid
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Simultaneous connection sounds super cool. I use it in the same way and reconnecting is annoying. I thought of doing something similar with synergy/mouse without borders but not through the internet, through the keyboard/mouse itself, auto toggling on mouse to the edge of screen. Cool project.

reply

needz
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I lead development on Pindigo (
https://pindigo.app
), a social score-tracking and ranking app for pinball players.

Most of my time lately has gone into Flippd, its successor, which we recently soft-launched. We’ve also released a tech demo that uses custom computer-vision models to identify a pinball machine from a photo and extract the player’s score.You can try it here:https://flippd.gg/scan

reply

scoofy
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a program that should help golf courses and golf course architects design better courses. I've been writing about it on my blog. My goal is to start a golf architecture consulting company, and help design/redesign courses that are better.

The general thesis on identifying architecturally interesting areas on the golf course:https://golfcoursewiki.substack.com/p/i-spent-the-last-month...Identifying dynamic golf design so you get more interesting play on the same course:https://golfcoursewiki.substack.com/p/friday-pins-vs-sunday-...Measuring the addition and removal of hazards and how it dynamically affects different skill levels, and how to measure that:https://golfcoursewiki.substack.com/p/measure-2000-times-cut...How I created a golf dispersion pattern generator -- which I made open source -- so that it can be improved, because the golf analytic companies already have the data and almost certainly won't share it:https://golfcoursewiki.substack.com/p/how-to-bake-a-dispersi...

reply

ramon156
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm rebuilding rainbow six siege but cross-compatible (and possibly FOSS?) in Godot.

Ubisoft has decided it will not support Linux because theyneedkernel-level anti-cheat, which is absurd in my opinion.I just want to do a siege with friends

reply

lylo
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on my indie blogging platform, Pagecord (
https://pagecord.com
). It started as a fun side project but is gaining decent traction right now - I’m convinced there’s a blogging renaissance about to happen! :)

I’ve been focused on decentralising it, offering ways for bloggers to write locally (markdown, Obsidian) while hosting remotely on the platform. I think it’s a great way of working. Most people still just use the editor though!I’ve been focused on marketing and distribution, which is mainly about content. Hard in such a crowded space but it seems to be working.It’s been such an interesting journey technically too, from using coding agents to dealing with the crazy deluge of bot traffic.I run it all myself which isn’t so daunting in the AI age.

reply

bob1029
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Browser automation + LLM agents + human curation.

The naive approach has the LLM interacting with the DOM using raw locators and javascript. If a human curates all logical views of the DOM and exposes tools that are only relevant for each, the search space for each agent iteration is reduced by many dimensions. I have achieved deterministic results over hundreds of actions in complex business workflows. Without the human curated layer we barely make it 10-20 actions before things get weird.Most of my thoughts are currently occupied with possibility that this works in the general case. I think an LLM exercising a tool like GitHub via properly curated browser automation might be superior to direct API access in some ways.

reply

yellowapple
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been resuming work on a Zig library for developing N64 homebrew¹. Previous milestone was getting a framebuffer onto the screen, and after achieving that I took an overly-long break.

Current goal, which I've been working on for a bit more than a week now, is to add support for controlling the RDP (the part of the N64's GPU that actually does all the rasterization), such that programs can actually draw triangles. I'd already implemented the control registers, so the current work is defining all the RDP commands, along with documenting what they do and how to use them — which means thatIneed to fully understand what they do and how to use them, and that's been a fun rabbit hole to explore.I'm currently about halfway to two-thirds of the way through defining packed structs for all the RDP commands, then the plan is to build a CommandList struct with methods to build RDP command lists and validate that they make sense (make sure all the triangle/rectangle rendering commands have all their subcommands in the right order, make sure you ain't calling them without there being a framebuffer defined as the rendering target, make sure the needed synchronization commands are in place where needed, etc.). Then that should hopefully be enough for Zig64 to draw its first triangle :)----¹:https://fsl.yellowapple.us/zig64

reply

liamarcx
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Non-tech indie dev , 4 shipped，Lately, I've been working on a project related to Unwordle,a game project.

http://unwordle.online

https://cleanfoto4u.com

https://tinc.cc

https://gta6game.io

reply

Arubis
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Been going a while, working to shift into a verification layer on existing static scanners rather than a standalone product: 
https://rsolv.dev
 takes a highly opinionated TDD approach to _proving_ (or disproving!) scanner-indicated codebase vulnerabilities and writing red tests against the desired secure behavior, so that customers can trust that they're not just making code mutations without cause, and that the shipped fixes actually work, and that there's regression protection in their suite.

Aside from that, I've been getting into building hyper-local services around public data; it feels really rewarding and relatable to invest more locally!Already up and running:https://hailpass.com/?ref=HAILHN9(ref code there knocks $10 off the season price) as a "season pass" for latlong/street address level-targeted hail notifications, built specifically for damaging-size hail (not just _any_ hail) on the Colorado front range. Email is free, texts are on the season pass model.On its way, likely first ship today:https://denverbroomsday.com, same season pass model with same free email/paid-per-season text split on reminders to move your car before street sweeping days in Denver.

reply

dreamiurg
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I've used Claude Science to retrieve and analyze 20 years of meteo data - wind, precipitation, snow cover, temp - for Pacific Northwest, to figure out how can I better plan mountaineering trips: "If Mount Baker is out due to hazardous weather conditions in the middle of September, what would be the plan B summit with the highest probability of having good weather?"

Done a lot of analysis, sliced and diced data different ways, and then realized I need a website.Ended up buildinghttps://climbable.day- hopefully a helpful resource for fellow Mountaineers from Seattle and around. 500 summits, 20 years of weather data, then went all in and added- Wildfire smoke map overlays from official sources
- Road closures from WSDOT
- Information about approaches to most of the summits, sourced from Peak Beggar and Mountaineers
- Database of known incidents from AAC
- Compare your plan A, plan B, plan C, that type of thingSite gained traction in the local community, and I have about a couple hundred users that seem to be using it on a weekly basis. It's free, and I intended to keep it such. It's a personal project, not something I plan to make money on. If you're in PNW and find it helpful, I'd be happy to hear what ideas you have. If you're not in Seattle but would like me to extend it to cover your neck of the woods, let me know.

reply

markdown
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

Nice! BTW is mountaineering a fancy word for hiking, or is there more to it?

reply

dreamiurg
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Let's say mountaineering is an all-encompassing word for all sorts of activities. Hiking is a good entry point, but once you get into it, you will soon find yourself getting into technical gear and skills to to be able to get to the top of places that require some sweat.

For example, here's my recent trip with few friendshttps://www.mountaineers.org/activities/trip-reports/interme...- 2 nights out, roped glacier travel, scrambling, rock climbing, a good mix of planning and stamina was required. And for all I know this is a low end of mountaineering.

reply

markdown
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks.

> here's my recent trip...Incredible! And yes, that's far more advanced than hiking.

reply

burrrno
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I just released HNewsflash [1], an iOS Hacker News reader, which accumulates the top upvoted HN stories over a given timeframe and lets you scroll through its discussions. I developed it for occasional HN users who do not open the frontpage on a daily basis and don't want to miss out on latest posts and news.

The app is build in native SwiftUI. Since the official HN API returns only one item per request, a single thread would mean hundreds of round trips, so there's a small Go + Postgres service in front that archives the top stories, flattens comment trees into one response and caches them.Big shoutout tohttps://hckrnews.com, which gave me the initial idea. I wanted to create something similar for mobile that can also handle comments and discussions.Other features include* bookmarks* code block and markdown rendering* no ads, no tracking[1]https://apps.apple.com/app/id6450697950

reply

idontneedcoffee
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building my "dream tool" too, a cross-device roaming profile-experience context-focused UI. Many, many iterations that go back maybe 15y, even built a custom linux distro (iolinux) back in the day(ro root, containerized user-spac with composer-like app handling). Always worked on side-projects, consulting gigs or one-off implementations, often times across multiple customer-devices. Switching context is damn expensive, hence tried to build a tool to help with that. Always failed on the UI parts - native linux tooling was just awful. What do you specifically mean by "context" you ask? Well, you get a call, switch to work on `work://customer-foo/project-bar/task-baz`, every bound device / tool / application loads data related to that task (your filesystem mount shows relevant files, browser loads relevant tabs, obsidian relevant notes etc). Building my own small db engine to accommodate that use-case, getting more fun working on it every day

reply

dv35z
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Hey - spent a lot of time in this world (solution / sales engineer, technical account manager to many clients), and thinking about this same problem.

Even experimented with per-client Linux users. Per-client calendars & routines. Per client knowledge-base, etcVery curious to see what you come up with.

reply

idontneedcoffee
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I divide my unstructured universe into workspaces, each workspace is a self-contained shareable/moveable soon-to-be-containerized runtime running an in-process LMDB with roaring bitmaps and (for now, S2-like hilbert space projections will replace it soon) lancedb for some basic cossim search. You configure your data sources per Workspace - imap, files, s3, soon slack(bc I use it), on top you create a classically-looking virtual tree. That tree is made of bitmaps - /work/customers/acme org/projects does a logical AND on all bitmaps in the path (work AND customers AND..) - if you zoom out to /work/customers you see all data for all customers, if you'd create /work/projects - you'd see all data tagged with any project. On top of that tree sit contexts - think moveable db views. You create a context "acmeorg" and bind your browsers, cli(for dynamic dotfiles), notes apps etc to it. You can even mount a file representation of all indexed objects via a fuse driver. When you point acmeorg at /work/customers/acme org/projects/foo everything moves with you - your browser stashes current tabs and opens relevant ones, your fs mount shows only relevant content etc - moving to projects/bar does the same, if you do that via commandline ctx set ../projects/foo --update-dotfiles - you get your dotfiles
You can setup actions - if I send a browser tab thats a yt url into home/music download it and place it into my roaming profile workspace Home, if I index a arxiv website, hit the library agent to properly assign it to existing tree paths and write a summary
There is also timeline support - you can have a personal and wikipedia aaand historian foo timeline, wanna know the zeitgeist of when your grandma was born - tick extra timelines and query in layered mode
Ou, and there is real-time streaming support, your db can resurface documents based on GPS or based on your camera feed (or, will implement today - show related documents based on your desktop view) - primitive vector sim search now, will be something much better riding the internal representations of gemma4 (for now) - ok let me stop here, you'll have a pinned task list per workspace on the left and a set of a2ui canvases and old-school boring and rigid apps that will either be directly contextualized or just ride the contextualized filesystem(as obsidian does). Ou, did I mention agent usecase? Agent switches to /work/task1 and his local *.md files are only related to that task, want more zoom, switch to /work. ok, oook, let me really stop here

reply

mapontosevenths
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Reminds me a bit of qubes OS with different motivation.

reply

calvinmorrison
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is awesome. I always have imagined my computer being well, my desk. So far I have to live with a bunch of i3 screens I name after whatever I'm working on. I'd love to be able to page through the bench to flip to a task. Unfortunately with apps going so mono-windowed (slack, etc) it's harder to do. If I could just say have my slack window for this client, with their docs, proposals, database, whatever up, that'd be sick. I love the idea thank you. good luckl

reply

idontneedcoffee
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

replied to another comment - if you are curious go over it, thx!

reply

asim
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Mu - Tools for Agents. An MCP server and web app that provides real time access to news, markets, weather, video, places, search, etc. It's sort of extension of a previous idea I had to put all the key tools and services behind a single api and access token. I don't know that it's quite there yet. The idea might change. Still looking for feedback.

https://micro.muhttps://github.com/micro/muAlso have an agent harness and service framework in Gohttps://github.com/micro/go-micro

reply

danard
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Currently working on (yes, yet another one) Todo app that has a lot of neat keyboard shortcuts and a useful hotkey window on Mac.

I built it because all the Todo apps seem bloated and mainly, when I am working on something, I don't want to ruin my focus, so I wanted some quick way to add/cross tasks off.https://simplythings.app/And also, currently building a "clone" of Apple Music app for macOS because Apple's native App is horribly slow and has many UX shortcomings.

reply

g58892881
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Photo upscaling and inpainting apps, both running in the browser

https://crisp.photos

https://wipe.photos

reply

forsalebypwner
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Sweet, been looking for a better browser-based inpainting tool, will check it out.

reply

jjcm
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Simple and efficient. Nicely done.

reply

g58892881
 
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

kofta999
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Currently building Tensou in my free time

https://github.com/kofta999/tensouI always get frustrated when using local file transfer tools like:Dukto: was my personal favorite, but is tiring to run cross platform, and most importantly does not support transfer resumes (so if copy got cancelled/disconnected at 99% you either have to copy again or search for the diff and copy it manually)LocalSend: pretty good cross platform support, but does not work when connecting 2 devices using a LAN cable, and resume support is poorishSo I'm building Tensou to be an alternative that doesn't compromise all these features.
Supporting resumes, folder syncing similar to rsync, cross platform (well I don't have a Mac to test on but it should work, and mobile support is planned)Performance wise it's on par with Dukto and even slightly better with large files (and I'm still working on optimizations for small files too)Would like to hear HN's feedback or what other features should I add? My goal with Tensou is to be the best, most performant and feature rich local file transfer tool ever.

reply

ymir_e
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A tmux plugin that makes is better to work with many agents:

https://github.com/Ymirke/tmux-agent-switcherYou press ctrl+n and you get a sidebar showing all the tmux tabs you currently have and the statuses of the agents.The sidebar then has a couple different navigation modes based on what floats your boat, toggle by tab:1. Using vim bindings j/k, and supporting number -> j/k to go up or down quickly.2. Using number -> number. Meaning you press the number of session then number of tab.3. Using search, useful if you have a ton of sessions open.I really like what herdr, cmux and others are doing in this space, but I find it hard to get myself away from my core tmux setup, so I made this to not have to change too much of how I work.

reply

gghootch
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

https://nommer.ai
 turns recipes into 2-player mode so you can cook together

People seem to love the concept so far and are starting to sign up, now just need to figure out how to get them to actually use it

reply

simonjgreen
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been hacking on an outdoor sound monitor for 24x7 logging of birds and bats around my house the last couple of weeks with a live indoor monitor: 
https://github.com/simonjgreen/OpenObservatory

And today I knocked out an improved trmnl plugin for Japanese flash cards at my wife’s request as she liked the native one from trmnl but it lacked furiganahttps://github.com/simonjgreen/trmnl-japanese-vocabNote: I let AI do the vast bulk of the work on both counts, and I ideated, architected, and bug fixed. I do love AI coding hobby projects though, when you have an idea for a thing and know exactly how to put it together but don’t have the time to raw dog the whole thing.

reply

jakerubo
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Very interesting!

Do you have a hardware list available? I didn't see it in your repo but adding it would be helpful, thanks!

reply

simonjgreen
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Oh good point, I’ve added a section to the README. Thanks!

(Assuming you are referring the observatory. Trmnl is off the shelf)

reply

phendrenad2
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

"When I asked the computer to identify it, what I got was European Warbler. You see, sir, the SAPS software was originally written to look for birds. And I think when it gets confused, it kind of runs home to mama."

reply

ponyous
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

GrandpaCAD - AI 3D modeling software focused on simplicity. Made it so even my grandpa could model.
He’s been asking me for years when will I teach him how to 3D model. I tried, we failed and then I seen him use ChatGPT so I knew there was a better way than traditional CAD tools.

Recently we also got European funding and the project got some traction. Very exciting times ahead.https://grandpacad.com

reply

chrisandchris
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Looks really nice! Two things:

- Does it support layers / assembling structures? This would allow to combine multiple parts into a product (don't know hoe that is named exactly in english)
- Awesome you support not only subscriptions but also a credit-based approach. I would definetly be a credit-customer, as I may have usage a couple of times a year, bot not continouous!

reply

ponyous
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah you can absolutely do multiple parts, although the mating features are still a bit rough you can do a lot already.

reply

clone1018
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Infrastry, a completely hands-off approach to deploying all kinds of (web) apps. You paste in a repo and Infrastry takes it from there, determining what type of software it is, how it should run, what should be configured, and then provisions to the internet and monitors it over time. It works very well for being so early, which is quite exciting!

The control plane is entirely in Elixir, using Jido & Oban to help power tools it gives an agent to get your app deployed. Uses k8s currently for the infra, but I've made the app => spec => build => deploy layers completely agnostic so we could switch out providers & methodologies in the future.Looking for people who want to throw apps at, it's still early so no guarantees yet. You can find the website athttps://infrastry.ai/(still a brain wreck of ideas, working on it!) and I made a Discord for feedback athttps://discord.gg/sBkS5ZMM3t

reply

pistachiosPower
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a web-based game where players guess a footballer's name based on the list of teams he's played for. The project currently focuses on Italian Serie A

https://athleteguess.pages.dev/demo

reply

krekr
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Helping a friend build a midi controller replica of a legendary vintage synthesizer (Yamaha CS80)

https://www.gijsleijdekkers.nl/gltaudio/

reply

ingvay7
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Very cool

reply

KitN
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/qKitNp/grammar-lol
 Grammarly alternative that uses the AI subscription that you probably already have ChatGPT or Grok and Apple Intelligence for Mac users.

https://tinkerers.spaceCloud platform based on my homelab for agents.

reply

gcanyon
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Not sure if this qualifies, but here goes: I wrote a hard science-fiction novella. It's intended to be scientifically accurate to special and general relativity, with just one tweak that permeates throughout.

https://docs.google.com/document/d/19e3HfnK1lNHHBef-5c-KvNdD...

reply

RobotCaleb
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

Cooool! Do you have an epub?

reply

gcanyon
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

See if this works: 
https://drive.google.com/file/d/1HUQV3IRNtTUt7sorTuJ3Wg6fqwQ...

reply

mgerb
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Spacecap: 
https://github.com/mgerb/spacecap

It's a screen recording tool for Linux. The goal is to make it as fast and efficient as possible, while also being simple to use and install. It's just a hobby project that I am having fun working on. Here are some notable things about it:- Written in Zig- Uses Vulkan Video for encoding- UI built with SDL3 and imgui- Features recording, replay buffer, and screenshots

reply

Evidlo
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Biggest advice for exposure is to try to get it packaged on Debian. Annoying but worth it.

reply

mgerb
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks for the suggestion. I plan to explore things like this as it stabilizes and becomes more feature complete.

reply

moinism
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Been building Chat Octopus (like ChatGPT but for media and content: 
https://chatoctopus.com
) since Feb this year. Now it's available on web, ios, and android but I'm finding it hard to market it and find users.

Which is, i think, a common thing about solo devs.How do you guys deal with that?

reply

faangguyindia
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

MacroCodex app, which results in guaranteed weight loss or weight gain outcomes within 2-5 weeks. It's a completely ad-free, subscription-free product.

Don't believe? Read the reviews.All you need to do is provide it your calorie intake and weight reading each day.How does it work? Explained here:https://macrocodex.app/knowledge/rethink/adaptive-tdee/We already have 16,000+ users.

reply

gppk
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

How do you get your users? This seems like a great little "useful tool" type app, but i always wonder how they get tractions..

reply

soontimes
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a platform that aggregates a business's operational and financial data and builds a causal model on top, deriving target metrics like FCF or EBITDA. With that model we can forecast different scenarios — what happens if we open a new shop, raise prices, take a loan. We also generate reports: weekly overviews, anomaly detection, deviations from targets. All of this is essentially a harness for an AI agent that customizes the platform for a specific business and integrates its data sources. Large companies have dedicated teams and sophisticated tooling for this; my bet is that small and medium businesses would benefit just as much, and with recent progress in AI it's finally possible to deliver it tailored to each case at very low cost.

My primary target right now is e-commerce due to rich data streams, however if you think your business would benefit from this tool, I would be happy to connect and discuss it.

reply

jimnotgym
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Good choice on ecommerce. Other planning scenarios are plauged by missing data, estimates and guesses!

reply

vinhnx
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

This month marks 1 year since I first started self-research and building my own coding agent VT Code [0]. I've been learning and experiment with a lot of things to first adapt myself and to learn about AI native/harness engineering. Thankfully, last month VT Code receives highest amount of contributions from the open-source community.

This month I will be focusing and enhance more long-running horizontal for VT Code such as plan mode, better strengthen tools policy structure and improve its harness as new and existing model grows exponentially. And If you are curious and want to fork it feel free, and welcome, let's build![0]https://github.com/vinhnx/VTCode

reply

pSYoniK
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been working on a static site generator. I've used Hugo and Jekyll before but everytime there is something you have to learn or get used to and they never map 1 to 1 to the flat structure of a simple blog for example.

It's a few classes of C# right now that parses a folder and auto generates the navigation, links, titles and summary off of the folder/file structure for the 1st level and then subsequent depth is mapped to individual items in the list view not on the nav bar (although I did that too, it looked weird with higher depth). So if you have a folder with 3 files and 2 additional folder you get 5 links in the nav bar, 3 content pages and 2 list pages. No other setup is needed. No llm written code, but I used deepseek v4 flash to ask various questions and get samples of some things.I forgot just how much depth there is to exploring a simple problem. Loving it!

reply

SophieBroderick
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

5 Q L 
https://fiveql.com

I've been working on this for a while now. It creates a sort of AGENTS.md or CLAUDE.md table for your database which holds all the joins, definitions, formats, and relationships, as well as what are popular criteria sets and combinations.And it populates it into a bi-directional visual (round-trip) SQL editor. Make changes in the UI or SQL text, it goes both ways.It's a single HTML file.

reply

david927
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Very cool

reply

vanyle
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

vectarine 
https://github.com/vanyle/vectarine

https://vectarineengine.com

It's a game engine with hot-reloading for everything to build and edit games while they are running

reply

oliwary
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

A daily estimation game: 
https://estimatle.com

Every day, players answer 5 questions that require estimating some quantity, such as distance, year, cost etc. Then you can compare against answers of other players and the real answer.Working on finding the right balance of questions that are both fun and also help understand facts about the world.

reply

gmmachine
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

This is a wonderful well thought out game, thanks!

reply

oliwary
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you for trying it! :)

reply

pkhamre
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It was a really great experience. I love the idea and the UX you have provided.

reply

oliwary
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you very much!

reply

storywatch
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Building the GoodReads of fanfiction and web fiction. Currently growing really quickly so dealing with scaling pains :/

https://storywatch.org

reply

ingvay7
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Small observation - some of your published blog posts are all future dated...unless its all fictional :-)

reply

joshdavham
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> dealing with scaling pains

That’s a great problem to have! Keep going!

reply

cmicali
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Vibe, my Winamp-like MacOS music player.

I use it every day, but had stopped dev on it a few years ago. Fable has gotten me excited to take it off the shelf and add a bunch of features I've been wanting for a while. Working on localization now.https://github.com/cmicali/vibehttps://apps.apple.com/us/app/vibe-music-player/id1582482361

reply

hboon
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been bootstrapping my indie SaaS and revitalised old macOS apps.

Along the way, I built AgentControl, so I can work better with coding agents, in ways that suits my style and preferences.The past week, I've started AgentBrowser because I didn't want agent-controlled browsers to steal the focus. I use Safari for day to day browser stuff and Chrome just for dev. This combines them.

reply

xixixao
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Just a little personal tool: Shipment tracking I call Lighthouse:

- All our shipments in one UI (instead of searching trough our mail boxes or going to several merchant apps/sites)- LLM processes update emails, but everything can be manually adjusted (or created from scratch)- We have a bunch of destinations we order to (work, home, different pick-up spots), this lets me see where I have to pick up and with which pick-up code- Real-time sync in case we update something, the other person sees it immediately- PWA, with animations, feels as good as native on mobile- $0 running cost (I only paid for AI sub when vibing this)Desktop:https://imgur.com/a/HD9mCIrMobile:https://imgur.com/a/EAuJiqH

reply

kristjan
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

More things than I meant to, but one's live and three are landing soon. I quit someone else's work a little while back, spent some time building a game that I'll get back too to the extent I can support myself, and then started a things-I-want-and-others-might-want-too studio.

https://sponder.app(Live) - an RSS and podcast mutator. Filter feeds for what you want, merge, time-delay, and drip articles on a cadence (I like to start from feeds' beginnings). For podcasts, detect similar metadata to previous releases so you can skip reruns.https://tellmeapenguin.com(Close! Come help test it) - Endless mad libs about whatever you want, and if it's a good story, you can keep writing more chapters. The kiddos love it, and you can share back and forth with grandparents and whatnot to keep sillily in touch.https://nounogram.com/(Web is live, apps soon) - Hybrid nonogram and crossword puzzles. Shade the grid to find the layout, then add the words where they fit. I built it to make the kiddo practice handwriting, and then it was more fun than I expected.https://getyarnt.com(Free until I ship the Stripe integration) - A task tracker that's actively hostile towards you having tasks. Started as a joke, but I'm using it to track my own stuff and really enjoying it. If you have a manager who likes assigning you work, tell them to get Yarnt!All of it's onhttps://hahamoment.dev/in the likely event you don't need any of this but do want to turn on a light.

reply

absoluteunit1
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a modern typing application.

https://typequicker.comI believe typing is probably one of the most important skills in 21st century for knowledge workers and yet one of the most neglected. Hoping to change that.Anyone can learn to type fast, without having to think about or look down at the keyboard. We are building the best tool to help people get there quickly

reply

vunderba
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Typing applications has been an extremely crowded space since all the way back in the Mavis Beacon days - good luck!

Small bit of feedback that might help it stand out more from the crowd and appeal to HN users: Add in training for Colemak, Dvorak, and maybe regional variants like AZERTY.

reply

absoluteunit1
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you!

I definitely approached it from an engineering perspective - building what I thought was missing in the space that I wanted. In hindsight, it may not be the best business to quit a FAANG job for haha.> Colemak, Dvorak...We have these :). Have QWERTZ and British QWERTY as well. Going to add AZERTY next and a few others.I an also exploring more uniqie/niche ones like Kinesis keyboards, etc.but no plans for this just yet.> good luck!Thank you!

reply

vunderba
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Haha - well hopefully coming from a FAANG you've got some financial runway at least :)

Some more feedbackI'm a fairly fast typist (~120 wpm) so I didn't dig too deep into your tool, but I did see that you seem to have a metric around highlighting for letters where people might be making mistakes.You might already be doing this, but my back-of-the-envelope thought is that you really don’t want to think about typing in terms of individual letters; you want to think in terms of clusters. Ideally, you’d use some kind of frequency corpus or Markov model or something similar to break text into commonly occurring constituent clusters, e.g. the -ing in a gerund.It's essentially the equivalent of "memory chunking" but applied to typing analysis. That’s not to say letter-level analysis is not useful (especially for hunt and peckers learning where the keys are) but as the person progresses, you’d want to introduce this idea of statistical feedback on common sequential clusters.

reply

ingvay7
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Very slick and smooth. The insights pages need a link to go back to the main page. Bookmarking.

reply

chaostheory
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I feel the challenge of typing applications is boredom. It's hard to keep using them. The only ones I kind of keep going back to are games. There serveral modern adventure games and a real time strategy game (I don't remember their names) and then there's Typing of the Dead.

reply

eonmatrix
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a pet project of mine. Linux first translation and transcription studio. 
https://truescribe.app

reply

escot
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

A grid-based flowchart editor designed for speed. It’s optimized for the keyboard with a spreadsheet-like selection and movement mechanism.

I started working on it because I was tired of dragging boxes/arrows around in Miro while making dependency graphs for planning projects.https://knotend.com/A while back I did a Show HN about it, and have since rewrote and changed the concept a bit to be easier to use.

reply

kageneko
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I grew up coding MUDs (in college) and every year I try to recreate that glory, so I start a fresh MUD code base from scratch.

This year, I am creating a nodejs MUD, well closer to a MUSH actually.* Everything is an Entity with Attributes
* A player is an Entity with its client property set
* There's a handful of built-in commands, but the important ones are @eval and @set-attribute
* The soft-code language is ... JavaScript.
* It uses the vm module from nodejs[0] to execute stuff.
* It has separate clients (so far) for Discord, Slack, and local console. It's easy to add more and will be easier after I do this one refactor.Each time an soft-code command or function or what have you executes, it creates a new context to isolate the soft-code from the rest of the application and uses Proxy objects to isolate the database Entity from the soft-code Entity. As an example, this is the look command (placed on the global registry object):if (!me.location) {
 me.send("You are nowhere.");
 } else {
 me.send("**" + me.location.name + "**");
 const contents = me.location.contents;
 if (!contents?.length) {
 me.send("You see nothing here.");
 } else {
 me.emit("You see:\\n" + contents.map(thing => "* " + thing.name).join("\\n"));
 }
 }The Proxy manages access to Entities and Attributes (for example, Attributes can only normally be accessed by their owners).The MUSH outputs markdown for everything, so each client can format it however it likes.I know the security is not nearly close to perfect, but it's mostly a proof of concept that I will make public one day. I did do a few things, like disable eval and Function and Promise but there's probably plenty of ways to get around it.

reply

imtringued
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Have you thought about letting an LLM generate the item and object scripts from a description? The LLM probably shouldn't be involved in regular game play though.

reply

tumidpandora
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on two small products right now.

Bravoboard:https://bravoboard.xyzIt’s a collaborative online card for birthdays, farewells, appreciation, etc. People add messages, photos, GIFs and voice notes, then the recipient gets everything together in one board.The surprisingly interesting part has been figuring out how to make something digital still feel personal, while also making the organizer’s job of chasing 20 people for messages a little less painful :)Presbot:https://presbot.comIt’s a small assistant for businesses and website owners. The idea is pretty simple. Visitors usually have a question they want answered, not necessarily a desire to "chat"It answers what it can and when it can’t or when someone wants to speak with a human it collects a short predefined inquiry insteadI started building an earlier version before ChatGPT existed, and recently rebuilt it while trying to keep the original idea intact - answer the question, then get out of the way.Both are live and very much being worked on, would appreciate any feedback.

reply

RobinL
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

https://rupertlinacre.com/arithmetic_annihilation/

A mental arithmetic tower defence game for kids. Now with head to head/two player. Code:https://github.com/RupertLinacre/arithmetic_annihilation

reply

nghiatran_uit
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I spent few months to buil the alternative to Wireshark. Native macOS app, built with Cocoa (Sorry SwiftUI), on top of libwireshark, so you can see the packet details like Wireshark. Support TCP, UDP, DNS, HTTP2, ...

https://tcpviewer.proxyman.com/

reply

FailMore
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on 
https://smalldocs.org
 for some time. It as if "Claude Code & Microsoft Office had a baby". It's actually very useful if you develop with a terminal based coding agent and sometimes want to get out of the terminal view to dig deep into a topic.

I have had quite a bit of usage:https://smalldocs.org/analytics, which I'm very proud of, with many developers using it week after week.It's free to use by the way.Code is open source at:https://github.com/espressoplease/smalldocs

reply

mgranados
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

this is very cool nice idea!

reply

FailMore
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Tyvm!

reply

aleqs
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a general repository linter. The idea is to declaratively define a set of rules/conventions for your repo, (for things that language-specific linters don't cover), covering things from directory structure, required files, file staleness/freshness, file size, rules for binary files, rules around use of invisible Unicode, etc. - which can be checked deterministically. Many/most large repos have a set of hand-authored scripts for doing these kinds of checks, the tool I'm building basically packages these in a fast, reusable and extensible tool, with some niceties added.

https://alint.org/https://alint.org/blog/why-alint/

reply

philips
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

I like this idea. I feel the hurdle is that many people have come to rely on their language tools for install.

reply

aleqs
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah that's a good point, thank you. I should think about how to distribute/make it available via language-specific packages/tools.

reply

ekrapivin
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I am late for the party, I guess, but I’m still developing an ad-free solitaire/puzzle games collection:

https://inSolitaire.comI’ve just done a major stability & usability release from the comments of a few dozen redditors.Would love to know if one can find any other issues.

reply

ecliptik
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Onigiri [1] - 
https://github.com/ecliptik/onigiri

A calorie tracker for iPhone/Watch/iPad, no subscriptions, no ads, integrates with Apple Health and fully open source. Includes optional AI features, either using on-device Apple Intelligence or BYO with Anthropic, OpenAI and OpenAI compatible services (eg self-hosted).Still tuning it, but over the last month I've used it to lose around 10lbs.I'm planning to put it in Testflight to avoid the 7 day signing expiration and improve iCloud integration, but don't have any plans to put it in the App Store. Developed with Claude Code and Axiom skills [2].1.https://ecliptik.github.io/onigiri/2.https://charleswiltgen.github.io/Axiom/

reply

aslushnikov
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on shard balancing for Playwright Test. The idea is to use the new API released in Playwright v1.62 together with historical test durations to balance tests across shards.

I ended up designing a specialized variant of LPT that works well for Playwright test suites. It's now used in WordPress's Gutenberg project, where it cut test runtime from 35 minutes to 23.The algorithm is called SALT. Here's the detailed write-up if you're interested in job scheduling:https://blog.flakiness.io/posts/2026/salt/

reply

BSTRhino
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://easel.games

A programming language that makes your game multiplayer automatically! It integrates rollback netcode into the programming language itself, guaranteeing that whatever you code is deterministic and can be snapshotted and rolled back. Then it integrates the networking and server automatically so you can just code your game like a singleplayer game and it'll be multiplayer automatically! I've been working on this for four years now.

reply

kderbyma
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a toy game engine for webGL called PixoSpritz (
https://pixospritz.com
) and its been something I have been lazily working on for a number of years, but its a slow crawl. I havent worked as much over the past year and a half mainly due to trying to use LLMs to add some extra features and it ended up making me kind of sick to look at the code, then got depressed with LLMs in general and my coding has taken a hit, but its still something I will continue to work on and one day will make a proper game with it too. (Its 90% useable, but really really rough and messy and LLMs made it slightly more fragile...)

I am also working on a E-zine publishing platform called SVRN for interactive journals, blogs, magazines, books, and self publishing content including ARGs and interactive fiction. It is mainly so I can make my own digital comics and web stories, and episodic zines.Reach out if you want to discuss!

reply

fredwu
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Have been working on three micro-saas, all built in Elixir/Phoenix:

https://feedbun.com- a browser extension that decodes food labels and recipes on any website for healthy eating, with science-backed research summaries and recommendations.https://rizz.farm- a lead gen tool for Reddit that focuses on helping instead of selling, to build long-lasting organic traffic.https://persumi.com- a blogging platform that turns articles into audio, and to showcase your different interests or "personas".Took a long break earlier this year to recharge, but now I'm back at it again, mostly working on Feedbun, about to launch it as an early alpha. :)

reply

erreon
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on 
https://plantkeeper.co/

It started as a tool to help me figure out if I need to protect my plants or water them down here in New Orleans since we don't really have freezing season, but also have super hot days or rain issues.

reply

tesnorindian
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Making legacy 20+ years Java Swing apps run inside a Browser using WASM and JS glue code with CheerpJ/OpenJDK runtime. WASM has a bright future for running native apps. Both WASM and JVM are stack machines. WASM beats on startup speed and memory footprint. But performs bad on compute. Since WASM lacks networking sockets, JDBC is broken.

reply

apignotti
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Always great to see uses of CheerpJ in the wild. Make sure to join our Discord to show the community what you are building.

https://discord.leaningtech.com

reply

xbryanx
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

If you’re in the Minneapolis / Saint Paul metro area and care about trees, you might like my recent project: 
https://msptrees.com

On a walk and wonder what species is shading you? Curious if the city thinks your boulevard tree is as sickly as you think it is? Find your spot on MSP Trees.It's been fun working with some public city data and thinking about how to normalize information across different municipalities. Community doesn't end at city boundaries, but municipal GIS data systems sure do. I'm hoping to build tools like this for some more areas if I can track the data down.

reply

mortenjorck
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

For the past four months, I've been building a window manager for MacOS based on my 2009 concept video 10/GUI.

I've overcome about a dozen "there's simply no way to do this in MacOS and I have to abandon the project" challenges so far. MacOS really does not want to let you manage windows in this novel of a way, and I've had to come up with a handful of tricks to maintain the illusion that the WM is accessing the compositor at a lower level than it actually is. But it works, and I'm dogfooding it as I go!I'm hopefully only a few weeks away now from a full announcement and a beta. If you're curious to try the first beta, feel free to get in touch at clayton at presteign dot com.

reply

bbkane
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Why macOS instead of Linux? For the extra challenge?

reply

mortenjorck
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Mostly just that it's the platform I'm most familiar with and felt reasonably confident in the TAM.

Partly the challenge, too, though! If I were designing within the constraints of a Gnome WM, the result would probably look totally different from where this project is now. It's kind of fun having, on one hand, a lot of OS restrictions to work around, but on the other, native first-party multi-touch, Core Animation, and a rich history of platform conventions to draw from and adapt.

reply

nbbaier
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Sounds cool! Is the video available anywhere?

reply

mortenjorck
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I did post a very brief teaser on the original Vimeo account I used in 2009, but it looks like no one has found it yet: 
https://vimeo.com/1213152954

reply

tyrelb
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

LineLedger - open source (AGPL) accounting. I run a few small companies in BC and got sick of paying for 7 QuickBooks subscriptions, so I built my own.

First thing I've ever open sourced, feedback welcome:https://github.com/lineledger/lineledger

reply

ahmedxuhri
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Thread visualization web tool 
https://sudolaps.top/postroom/
 > Show HN/Reddit/Youtube comments as 2d Auditorium (comments clustered into sections, summarized via ai) -> Free

reply

gremlin0
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building a performance testing tool with a Rust core using Tokio and Reqwest, with a Python interface built around Typer and PyO3. You can use it as a regular CLI, but you can also write performance tests directly in Python. The goal is to keep the developer experience simple and familiar while using Rust for fast, concurrent, high-throughput load generation.

reply

AznHisoka
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building Bloomberry, an alternative to tools like Builtwith for finding companies that use a specific enterprise tech, as soon as we detect them

Most tools just focus on frontend tech like Shopify or Wordpress. Bloomberry shows you who uses backend tools like Hubspot, or Workday, or Gitlab for example.Example:https://bloomberry.com/data/github-enterprise- companies that use Github

reply

the_arun
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

How are you getting data for this? Public data?

reply

jonotime
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on building a generic desktop controller that you can run from any device. 
https://github.com/jonocodes/deckd

Originally inspired by the stream deck, but I wanted a more dynamic interface and less hardware restrictions. For example you can use your phone as the controller.Now it can do a whole lot more. Including mouse, keyboard, media controls. Supports custom buttons types and things like sliders and color pickers. Dynamically switches layout based on foreground app, and can also control which app is in the foreground from the controller itself. Having a lot of fun so there are a bunch more features in the hopper like deeper app integration, and an eink version.Its a web app/PWA, so no app store needed.

reply

ngsevers
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

For the last 6 months I've been working on a local-first replacement for accounting and business management software. I just finished building a modular system that I'm pretty proud of, which lets users develop their own modules and import them into a running instance without having to fork the repo.

https://github.com/celerp/celerp

reply

yboris
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Releasing 3.3.0 version of my 
Video Hub App
 - 
https://github.com/whyboris/Video-Hub-App/
 & 
https://videohubapp.com
 - 8+ years of development!

Working on 1.0.0 ofSimple Image Browser-https://github.com/whyboris/Simple-Image-BrowserReleasing 2.0.0 of mySimplest File Renamer-https://github.com/whyboris/Simplest-File-Renamer- Electron to Tauri 130mb to 3mbReleasing 1.0.0 ofMy Off Remote-https://github.com/whyboris/my-off-remote- turn off your PC from phone / tablet over WiFi

reply

mshekow
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

A CLI and UI tool called "renovate-log-parser" to diagnose issues with Renovate Bot, using its debug log. It's supposed to accelerate this analysis, with several CLI commands (one meant for coding agents to save tokens when they read the log). If you want to try it, it's just one "npx renovate-log-parser" command away.

https://github.com/MShekow/renovate-log-parser

reply

satyamkapoor
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Nice idea

reply

liviux
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Spending time with family, working my Cloud SecOps job and in the little free time that i have, trying to improve LoopTroop ( 
https://github.com/looptroop-ai/LoopTroop
 ) - an open-source GUI to create/update apps using AI.

reply

mkagenius
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a replacement for firecracker.

Thinking ground up what AI agents would need rather than struggling later on with snapshotting live vms, or orchestration overhead etc.rust-vmm proved really great for this.https://github.com/instavm/tarit

reply

meerita
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building a new modern Terminal browser. A text based browser for the terminal. Full privacy, features. Ultra fast. For those who love to work in terminal but somehow are dissapointed with Lynx.

* Native and small.
* Private by default.
* Terminal-safe.
* Agent-ready. A built-in MCP server exposes read-only tools (browser_open, browser_read, browser_list_links).
* Configurable.[0] [code]https://github.com/meerita/puma-browserI am still far away of 1.0, but I've been using it every day since. It's open source, you can compile it and use it as you want.Every week I try to finish more features.

reply

ranger_danger
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

without javascript, doesn't this break a lot of websites, especially ones that lazy-load their content?

reply

meerita
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Full JavaScript websites will not work, but the rest of the web will. I'm trying to build a more solid module to handle URL redirects. I managed to get it working with DuckDuckGo.

Right now, forms don't work yet (still in development), but you can use the `/search` command, and it will perform a search on DuckDuckGo.Addendum: HN breaks a lot, specially since I didn't support nested comments and forms, but it's readeable and you can browse all links, no problem.Give me all the feedback, I really appreciate it.

reply

pugworthy
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Enjoying retirement. Amazed how fast I was able to just stop thinking about software. It's very liberating.

reply

soupspaces
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Why not mentor others with the experience?

reply

ppymou
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been building a PDF reader with dark mode that supports image properly with vimimum navigations. Been using it for the past few months and really happy with the result. Finally got around to publishing it here: 
https://github.com/moomou/xeil

reply

anitil
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on the Jane Street reverse engineering puzzle that was posted here a few days ago[0]. As usual I've not made much progress on the actual challenge because I've fallen down a bunch of rabbit holes.

So far I've built a digital circuit simulator, a parser for my circuit design language, and now a parser for my simulator language (so I can run the sim on known inputs and have the machine enforce asserts for me). All to avoid the painful memories I have of verilog/vhdl.If I don't come to my senses, the next thing is probably going to be a wave form viewer because I've wanted to use Raylib for a real project for a while now.[0] edit: forgot link -https://blog.janestreet.com/can-you-reverse-engineer-an-asic...

reply

niothiel
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

More work on 
https://cardcast.gg
. It's a way for my friends and I to play Magic: The Gathering online using a webcam. For those unfamiliar, you take the webcam sitting on the top of your monitor and point it down at your desk, then play with your friends using paper cards over a video call, but specifically tailored towards Magic + Commander.

Recently I've been focused on marketing and small bug fixes. I think the core feature set is compelling enough, now I want to draw more players and start building a community. Been doing some social media stuff, designing an icon (this is HARD for me, I'm not very creative), and looking to print out a bunch of Cardcast-branded Magic cards that I can hand out at my local TCGs.If you play MTG, I'm looking for more people to come give me feedback and contribute. Feels like something others can benefit from!

reply

threadlting
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Full-time apply for the job/Internships and Part-time Working on a crawling tool for RAG.

reply

vintagevibe
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

https://caffenol.app

It's a darkroom toy/simulator for photogs running in the browser on WebGPU. It's half film sim, half creative chaos and each run is different. Still pretty early.

reply

yboris
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Pretty! Really enjoyed it!

reply

kannanpoem1984
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been working on couple of open source projects related to package intelligence and AI tooling.

https://secchi.devSecchi is Open Source Package Intelligence | python basedhttps://tuffcli.devtuff is Capability lifecycle manager for coding agents | rust basedBoth would be very helpful to be part of developer tooling. I built package intelligence when I need to monitor the downloads of my other personal project packages from package manager.I have learned a lot over in terms of rust language, design patterns in rust, also how the ecosystem of AI capabilities within projects use cases and needsThat sounds interesting, give star to repo :D

reply

alecsm
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a browser IDLE game made with Go. I've never touched Go before. The game core it's 80% done and it was pretty easy to code but I have no idea what I'm doing in with the transport/http layer.

At this rate I'll have it finished by the end of the next decade.

reply

furst-blumier
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

I love idle games. What's it about?

reply

alecsm
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's a MMORPG. Combat, bosses, gathering and crafting professions, etc.

From the moment it launches, there should be enough content for around a year.

reply

RaiausderDose
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Dominus Automa is an idle mmorpg too - 
https://store.steampowered.com/app/3795810/Dominus_Automa/

Same style?

reply

alecsm
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Not at all. It's a different concept.

More likehttps://store.steampowered.com/app/1267910/Melvor_Idle/

reply

furst-blumier
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's awesome! I 100%ed melvor idle and a bunch of the other big ones like antimatter dimensions, cookie clicker etc. Is there some way to get informed when you release it?

reply

alecsm
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I thought no one here would be interested in it but I could post it to /show once it's ready.

reply

thadjones
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm slowly working on a spacecraft design webapp: 
https://vesperastro.com
. Think PCPartPicker for spacecraft.

You can build out and trade hardware in the master equipment list and immediately visualize how any changes impact mass, power, propellant, and link margins, or break power or data interface compatibility. You can also play around with orbit and operating modes to optimize things like orbit average power.I'm hoping it can be useful in rapidly iterating early stage spacecraft designs and weighing system-level trade studies across CONOPS and hardware. Its still very much a work in progress so I'm always open to feedback.

reply

praveer13
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Posted on the other thread too related to this

I’ve been making interactive learning resources for myself - with wasm and browser simulation based labs (browser only interactive courses served from GitHub pages) to teach me topics from beginner to advancedLLMs and systems intersection -https://kernelspace.naigap.comDistributed systems -https://byzantine.play.naigap.com

reply

ryukoposting
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

An analog telephone line simulator built (almost) entirely in CMOS and through-hole parts. It will be the second of its kind designed entirely in the 21st century, and the first of its kind designed in the 21st century with any hope of other people reproducing it. Think of it like a rudimentary PBX you can build at home, 
or
 like a little telephone company that sits on your desk. Either is accurate.

Realized today why my filter circuits weren't working as they should: I screwed up the placement of one capacitor when I moved the design from simulation to schematic. Next post in the series coming soon.https://hardfault.life/t/tinytelco

reply

shaka-bear-tree
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I wanted to know if I could fully describe an online survey using a simple, readable, parseable language.

There are numerous UI form builders. And Xlsform for ODK and KoboToolbox but nothing I could find that is easy for humans and machines to grok. So I wrote a DSL in Ruby to see if it could be done. The language is mostly described athttps://srp.solutionsand some example usage and implementation athttps://srpsurveys.com/

reply

robowo
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

This is a great idea. Is the code open source?

reply

schultetwin1
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://dipstickalerts.com
 - I've been working on this during my kid's naps.

The web app allows car owners in the U.S. to see a list of all the service bulletins the manufacturer has sent out about your car over the years (called Technical Service Bulletins or TSBs). You can subscribe for new bulletins to be sent to your email as well.These service bulletins are not only recalls but also fixes for known issues with the car.I found reading these bulletins super helpful for my own car. There were some symptoms I would have never noticed without reading through these bulletins. For example: the tailgate did not lift up all the way in cold weather. Turns out this was fixed and covered under the extended warranty.The infrastructure is all built on top of Cloudflare workers. I use Gemini Flash Lite to summarize and filter the bulletins.This is my first web app (thank you AI) so any feedback is welcome!

reply

mchaver
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on Cangjie Workbook. I am trying to create the best in class tool for learning Cangjie. It's a Chinese input method based on decomposing characters into sub parts (not necessarily related to how they are written). It has a high learning curve, but it is a lot of fun to type with and helps you remember characters. It is a tool that I use myself. I already have a couple of users that have been giving me feedback. You can use a subset for free and without any login credentials. The complete product is available for a small monthly fee. Any feedback is welcome!

https://www.cangjieworkbook.com/

reply

richstokes
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Had a moment of nostalgia and started building an IRC client for macOS. It’s totally free/open source. And has been fun to customize / add the features I like to see while avoiding the ones I don’t.

https://github.com/richstokes/Netsplit

reply

ryanchants
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Working with agents generates a lot of markdown input and output. So I'm working on viva, a tool to help author and review docs.

You tell it what kind of doc you want, attach any necessary links/files/repo paths/etc, then it asks you clarifying questions until it has the data it needs. Then it authors a doc and give you a review interface. You can approve, request more info, request changes, make direct edits, etc. Then submit and makes edits until and represents until you approve all sections.https://github.com/jacquardlabs/viva

reply

Bootvis
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on my typed, fast data frame language Ibex: 
https://github.com/bobjansen/Ibex

It is usable stand alone but also through an R package:https://bobjansen.net/faster-than-data-table-introducing-ibe...It performs better than data.table in my benchmarking on a wide array of tasks and is competitive with Polars on low core counts.

reply

Wowfunhappy
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm backporting the modern 2026 WebKit framework to work with Safari 7 on OS X Mavericks, from 2013.

With the updated frameworks in place, this ancient browser becomes able to access the modern web again! Even webapps like Figma work!https://github.com/Wowfunhappy/WebKit(As I make clear in the Readme, Claude wrote this code, a project like this would never be feasible otherwise. My main job has been to decide on larger infrastructure questions and find bugs and make them reproducible.)

reply

spicyjpeg
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

An overhaul of my original PlayStation bare-metal programming tutorial repo: 
https://github.com/spicyjpeg/ps1-bare-metal

It was never really meant to be an SDK of sorts that other PS1 homebrew projects would pull as a submodule and depend on, but since it more or less became one I am likely going to split off the examples from the "core" (headers, CMake build scripts and tools). I have also been asked to add more examples, particularly on how to play sounds through the SPU and access the CD-ROM drive, and may cover I/O on some PS1-based arcade systems in the future.

reply

podviaznikov
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Building native WYSIWYG Markdown editor for mac, iPhone and iPad.

I've launched it only three weeks ago but tons of people tried it already, so I'm spending more time to make it better.It's called Wander. And it has history baked in and mostly compatible with Obsidian vaults.https://wander.md

reply

matheusmoreira
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm doing a massive AI code review on my lone lisp project. I finished a complete Fable code review, and the experience pissed me off enough I switched from Anthropic to OpenAI. Decided to run an equivalent code review with Sol and compare it with Fable. I'll publish the results on my website when it's done. Some pretty interesting results already. I think I stressed Anthropic's safety classifiers to the max.

Meanwhile, I decided to revive my Rust liblinux project. Rust has come a long way since 2019, notably the inline assembly macro has been stabilized. Iwilllearn Rust this time!

reply

ihrimech
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on 
https://fittingme.ai
, a product-page widget for fashion e-commerce.

It answers two questions that are usually handled together inside the fitting room: “How might this look on me?” and “Which size should I order?”The virtual try-on renders the garment using a shopper’s photograph. 
The size recommendation component estimates the users measures, use the brand’s size chart estimated measurements and suggests a size plus a fallback.The merchant integrates both through two widgets.

reply

chupchap
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Do you ask for height as a manual input?

reply

ihrimech
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's the one measurement I always need. We support three modes: 
- full manual, where the client enters their own measurements; 
- semi-automatic, where the client fills out a short form and we estimate measurements from anthropometric statistics; 
- full automatic, where the client takes two guided photos in specific poses with their phone, and we derive the measurements using a BMNet-based model

reply

chupchap
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Okay that makes sense

reply

nonethewiser
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A tabletop adventure game generator. Instead of tediously rolling for disconnected content in limited ways (enemy to fight, loot after fight, etc), you generate an adventure and print it out. Random events can be connected, enemies can be elegantly scaled. You discover a rich world rather than tediously generate a low fidelity one.

reply

popupeyecare
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on ProofLeague, an app for keeping workout promises with friends:

https://proofleague.com(iOS, web app and android)You create a private league, set a weekly goal (workout 3x a week), and tap Start when you begin a workout. Friends get notified and then have 30 minutes to ask for a selfie. If nobody asks, the workout counts automatically. There’s no public feed or strangers involved, just a small group keeping each other honest.My friends and I had been doing a version of this via text message for years, but this app has been great. I am in 4 "leagues", all of them get notified at once and then I only share my selfie once and it automatically goes to any group that asks. It's motivating and hilarious to see people working out.It's free and would love for you guys to try it and set up a league with friends or family. Please send me any feedback at amit@proofleague.com

reply

xmstan
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I am working on Bonsai - an open-source conversational framework for brand-safe assistants and agents. It works with text and voice based channels. For example we recently built an email agent that qualifies leads and sends pdf offers back. 2 years ago (before open-sourcing) we built an AI podcaster that conducted interviews in a physical space. 
GH: 
https://github.com/utter-one/bonsai

reply

marginalia_nu
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Marginalia Search as usual.

Recently went on an optimization bender that saw the index now become almost completely bottle-necked by CPU in the ranking calculations step. Pretty neat. Faster ranking means better results as queries run on a timeout.Also working on making the search results more relevant by fixing jank.Also working on some more commercial features, like the ability to monitor queries (e.g. for backlinks or brand mentions) and get an email when there are new results. Unsure if there's much demand for that, but I want the feature, so I'm buying it even if it doesn't make me yacht money.

reply

ignoramous
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

It is both a great (ai tools) & worst (ai slop) time to be building a web search engine!

>working on some more commercial features, like the ability to monitor queries (e.g. for backlinks or brand mentions) and get an email when there are new resultsAs an inspiration (presuming you don't already know), see exa.ai who build generic solutions in similar space:https://exa.ai/docs/reference/monitors-api-guide

reply

buildyard
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on BuildYard (
https://buildyard.ai/
) - where you can build your own portfolio for AI work. Each of us use AI in different ways for different reasons and understanding it would help in spreading it's advantages across the board.

reply

0xnyn
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on an open-source alternative to Loom/Jam/Birdie/Screendesk

It captures the screen recording along with console logs, network requests, and session activity so you can get to the root cause fasterhttps://github.com/0xnyn/userplane

reply

hackitup7
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I was only working on this occasionally, but I built an extension to block sites in a more creative way.

Basically I'm finding myself in a bind where:- I spend too much time doomscrolling (X, reddit, HN etc)
- AI is making me lose touch with a lot of basic skills like coding, and I was already losing touch with doing real mathSo I built an extension that blocks sites and forces you to actually solve a problem before you can get to a distracting site. The idea is to 1) block the reflex of visiting a site and getting a dopamine hit, and 2) at least get some mild cognitive benefit from it. I use it myself.https://sphinx.fyi/

reply

rpjt
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm still tinkering with my iOS/Android app.

It allows you to get a wake up call, like you would at a hotel, but from a real, friendly person somewhere around the world. If nobody is available to make your call, you'll get an automated call with a friendly recording.All calls happen through the app so no phone numbers exchanged.https://apps.apple.com/us/app/wake-up-call-service/id6741027...https://play.google.com/store/apps/details?id=com.socurious....

reply

Eueudhsbsj32
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Looking at the screenshots.. is the "wake up call" concept just a cover to get a phone sex service on an app store?

reply

helloakariq
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Akariq has taken most of my time [0]. I sell travel eSIM plans for 190+ countries, no app or account needed! Since last time, many HN readers have tried it with very positive reviews. I reply to each and every customer who reach out to me and also implemented some feedback they gave.

On July 24 2026, all major eSIM providers including Akariq faced disruptions. However, Akariq was able to serve all customers even during the downtime either by switching to backup resources or issuing replacement eSIMs free of cost. Some customers of major providers like Airalo experienced serious down time. I wrote more about the incident here and what I am striving to be better in terms of automation etc [1].One review from a customer in China [2] made all my effort worth it. They said that they were able to use Akariq to access Gmail, WhatsApp etc around the GFW. It even worked smoothly in areas like Beihai and Weizhou island apart from the cities. Tethering with their laptop was helpful too.[0]https://akariq.com/[1]https://akariq.com/en/blog/akariq-backup-esim-service-interr...[2]https://akariq.com/en/esim/cn/

reply

sethd
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I built a macOS terminal (libghostty wrapper) that runs iOS simulators (and mirrored physical devices) in a Metal-rendered pane inside the terminal.

It works with standard tooling: for example, if anything in one of its tabs runs `xcrun simctl boot`, the simulator just shows up as a pane in that tab. There's a CLI for the things simctl/devicectl don't cover: taps, gestures, rotation, accessibility tree, etc.Check it out:https://deviceterm.comCode:https://github.com/sethdeckard/deviceterm

reply

LouDNL
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Just released USBSID-Pico v1.5 an improved pcb without jumpers. USBSID-Pico is a RaspberryPi Pico/PicoW (RP2040) & Pico2/Pico2W (RP2350) based board for interfacing one or two MOS SID chips and/or hardware SID emulators over (WEB)USB with your computer, phone, ASID supporting player or USB midi controller.

https://github.com/LouDnl/USBSID-Pico

reply

arvida
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://localhero.ai
, automating i18n translations for product teams (runs as a GitHub Action, translates new strings on PRs matching your brand voice and glossary).

Shipped "bring your own translations" feature this month, built together with a customer who wanted Localhero for the workflow and review layer but writes some translations themselves. Otherwise smaller improvements and marketing. Better Lingui support, for example: projects using explicit IDs keep the source text in the source locale's msgstr instead of the msgid, which our CLI got wrong before. Also wrote some blog posts, a comparison of GitHub Actions for i18n and a guide to auto-translating gettext .po files in CI (Django, Phoenix, LinguiJS). Content is slow going but it seems to be how people find us via perplixity/gemini/chatgpt.On the side,https://infrabase.ai(AI infrastructure tools directory) grew ~16% MoM. I leaned further into the agent angle: added a public query API plus llms.txt/agents.md/etc so agents can query the directory directly, and exported the full dataset to a public GitHub repo. Starting to get som traction and people wanting collaborations.

reply

kredd
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

It’s not as cool as most of the other projects, but I have a little app (Ato on AppStore - 
https://apps.apple.com/app/ato/id6757285141
) for basically tracking all walks/bike rides I’ve ever been and visualize it on a single map. I’ve had the app for a couple of years, but redid it with “hexes”, instead of just routes. It has a bit of coop, competition and ranking feeling to it nowadays as well.

I started the original project as an excuse to learn SwiftUI, then been using it as an excuse to test all the frontier models and etc. to see how much better we’re getting at AI-coding. Kinda fun to see a couple dozen weekly users semi-competing with each other. Obviously nothing big, but the feeling you get seeing someone else use your app is very nice.

reply

pcarion
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

Nice concept. The app has to run in the background while you walk/bike/run ? how does the battery drain after a couple of hours?

reply

kredd
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ah sorry, should’ve clarified, it doesn’t have tracking capability (kinda on purpose, semi-because hard to maintain battery/accuracy balance properly, for now). It syncs your old workouts synced into HealthKit, and displays them. I also added options for “manual check in” and “track through photo locations” as they were requested by my friends.

reply

kilroy123
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working to make one of the biggest free and privacy-friendly tool websites. A lot of them are things I want and need all the time.

https://allthedamn.tools

reply

swaroopgrs
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a family organizer app Mana - The AI-Connected Home App for Households & Trusted Circles 
https://share.google/dCKfODeN7c1QhHhft

reply

radius89
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://radius.to/
 - a Meetup.com alternative of sorts - with fairer organiser pricing for smaller groups.

I posted a Show HN [1] here a while back, got tons of great feedback, and have been slowly improving it since, with no real marketing. Another Show HN is probably (definitely) overdue!Current focus is shipping a "Meet people doing X" feature - i.e. "I'm going for a cycle today in Richmond Park - who wants to join" (independent from groups) so I'm excited for that. There are some UI examples of how that will look on the landing page.[1]https://news.ycombinator.com/item?id=40717398

reply

mark_l_watson
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I am retired, so this may not be of general interest: I am working on my fourth AI coding agent, this one written in Racket Scheme: 
https://github.com/mark-watson/racket-coding-agent

I don't necessarily suggest that anyone besides myself use it. I open-sourced it to perhaps give other people ideas, but it is tailored to just my own needs (e.g., hardwired to use deepseek-v4-flash-0731 via FireWorks.ai; supports just the tools I need).

reply

tosh
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

I like the racket+deepseek combo

ty for sharing this + your books

reply

feliixh
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I just hacked together 
https://www.firstbranch.ai
 in a few days, conversational intelligence for congress hearings.

I was talking about healthcare price transparency with a friend. He pointed me to a hearing in congress and I was surprised by how much I learned from one of the witnesses' testimonies so I built a "serendipity engine" for congress hearings.

reply

jordiee
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

An agent harness that is kind of like airflow for agent tasks.

I thought open claw was cool but could never use something so insecure.Each run is in a container. One network bridge out so everything from tool calls to model communication goes over the bridge.Each run has a capability token and the host checks grants for the tools attempting to be called.Core super thin and everything from credentials handling to model communication is a package.Finally got it alpha and have some useful jobs set up like it triggering jobs on an alert channel in slack. Debugging it with tools like GitHub kube and our work mcp and the dropping a comment on every alert with the cause.https://ottoharness.comStill closed source but hoping to change that after some more testing.

reply

alfg
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Launched a suite of media inspection and encoding tools a few months ago, based on FFmpeg. Slowly getting more customers.

https://video-commander.comConstantly iterating through refinement and features. It's built on Rust + Tauri with a React frontend, in case anyone is curious.I've created various open-source and commercial tools in the multimedia space over the last 10+ years and wanted to put it all together into something more premium with an IDE-like experience.Most recently I added a /playground area to experiment with the inspection tools via a WASM build, which I thought was a neat way for users to try the app before downloading the full version.Happy to answer any questions!

reply

NegativeLatency
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

A iTunes inspired music app (uses an extension of DAAP) for classic Macintosh (Mac II and system 6 and newer currently only m68k, ppc coming soon) 
https://github.com/nburns/iRunes

And a extended DAAP compatible server than can convert other local music libraries (files/dlna/etc) for iRuneshttps://github.com/nburns/sharon-jones-and-the-daap-king

reply

yaman071
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I redesigned my portfolio page (
https://yaman.pro
) and my Hacker News Reader hn30 (
https://hn30.eu
) and added a new feature to it since I subscribed to Cursor Pro recently.

I‘m still working on it and adding features to my other side-project which is a local prompt library (https://bearprompt.com).

reply

sunsetSamurai
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I got laid off recently and finally decided to dedicate some time to learn Rust, I started to work on an an idea I've head for a while, to create a game server to play Thai chess inspired by lichess.org, in fact, I plan to use several of their assets.

I'll use Rust for the backend even though it's probably an over kill, but it's the best way to learn for me, doing something with the language. I have some of the front end move logic and board done, I plan to start working on the API soon, after I finish a Rust book I'm reading. Here's some of the code if anybody is interested:https://github.com/thaichess-org.

reply

kartoshka
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building this:

https://safetyevidence.orgIt is the most comprehensive collection of benchmarks of the safety, ethics, and values of LLMs. I also aggregate sparse safety benchmark scores into a global ranking by optimizing the global ranking to maximize correlation with individual benchmarks.

reply

zacharyfmarion
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I left my job a few months ago and have been building 
https://oristudio.pages.dev
. It’s an origami design workspace that runs in the browser. Super niche but I’ve been really loving just working on a passion project I can use for my hobby.

reply

woutr_be
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm still working on 
https://openaltfinder.com
; a directory to help people discover open-source projects. Added quite a bit of new features over the last month, including a new weekly newsletter, and a way for people to find beginner friendly issues: 
https://openaltfinder.com/contribute

It's been tough, for some reason both Google and Bing completely erased my site from their indexes.Another thing I'm working on:https://getpinnd.com- A small social network for map makers.

reply

tajd
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

A few things actually.

I’ve been working up reimplementations of Nikoli puzzles to host on my personal blog, the goal is to work through the maths and then explain how it’s relevant or helps create a fun games. Nikoli is the magazine that helped create sudoku and made it famous - they have a lot of other pen and paper puzzles that are really fun to play.I’ve also got two other open source tools I’ve built to help me work daily:https://tajd.github.io/cofferdam/which is a rust based cli tool I wrote to parse the ast of codebase and enforce architectural preferences - eg don’t reimplement design system for components down to DRYhttps://tajd.github.io/projektor/Is an ai native project management tool where I can plan work on the train and then have my agents pick it up autonomously. Bootstrapped it quickly but then have been incrementally adding more functionality to it. It’s like self hosted jira on cloudflare but much faster and has more agentic development tools. I added tooling around being able to autonomously work through epics, manage quality and fix identified bugs -https://tajd.github.io/projektor/agents/playbooks/epic-goal/. The goal being deliver useful features and then to ultimately surface the number of bugs identified by agents and users so that I can see the health of the project and figure out if I need to write more code myself or improve feature descriptions to reduce discovered bugs. I don’t think this is new at all but it’s reliable and done well, I hope.

reply

tajd
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Also added a load more puzzle types to pokerchallenges.com - a website to train aspects of Texas hold’em - keen for feedback (from humans) so reach out and I’ll give you free access

reply

Kauhentus
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been putting my applied math degree to work!

https://asunder.co/montegrid- Mainly working on a Monte Carlo Excel plugin that can run on Mac. Standard scientific computing shenanigans ... one benefit of everything being Javascript is that one can use Rust -> WASM everywhere :)Also maintaining weaving software (https://asunder.co/bower) which has so many fun puzzles in discrete math and combinatorial optimization to think about.Cool to see everyone else's projects!

reply

mikeklaas
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

A modern game engine that can play the Classic Fallout 1/2 games on modern systems (including mac, linux, iOS, Android). Hoping to bring these games to a wider audience.

https://github.com/fallout2-ce/fallout2-ce/

reply

glitchmodo
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I work full time as a full-stack developer, have a second part-time software development job, and recently started a business named Glitchmodo.

I rebuilt two older projects: AwesomeTools.org, now with more than 200 free browser-based tools, and SuperDadJokes.com, which I originally made for my kids when they were younger. Awesome Tools was recently approved for Google AdSense, so I'm now learning more about SEO, traffic, and monetization.I'm also building a daily word game for iOS and Android, plus a Roblox game. I'm totally new to game development, so that has been fun and challenging. My kids are excited to be testers for the Roblox game, so that one has me the most motivated.https://awesometools.orghttps://superdadjokes.comhttps://glitchmodo.com

reply

wwalker2112
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

A newspaper for kids. Printed on real newspaper and delivered monthly. Full of puzzles, math challenges, nature facts, science experiments, outdoor scavenger hunts, and even custom card/board games for families to play. 
https://thecuriositytimes.com/

Limiting screen time has been a primary goal in my household and has been going well. But I wanted something that would take my kids hours every month that1. isn’t on a screen
2. educational
3. fun

reply

throwaway89201
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

It's a worthy goal, but can you please not push unimaginative AI slop on kids? The frontpage graphic you're showing here already contains numerous slop markers and errors, and you've apparently still chosen to use it.

In modern times, kids mostly get to know the world through images, and they deserve those images to be real or at least realistic. It really matters that the details are either correct or simplified, but not present and wrong.For example, a compass with two norths and a garbled east is not a good start for curious conversation, but I think you should refrain from using generated images even if the details aren't so clearly wrong, as you are not an expert in most subject matters, and can't judge those errors. Instead use either photography or stylized illustrations which leave out details to imagination instead of including them and getting them wrong.

reply

freakynit
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://jerrysniffs.online

Zero-subscriptions google + social media search mcp/api/dashboard/sdk.Every $10 gets you 15K google searches + 3K Twitter search/lookups + 2K Reddit + 15K Url fetches as markdown for feeding to your llm's.Your credits never expire, use them whenever you want to, and you can stack them as many as you want.Already got 40+ paying customers within a month of launch.Now trying to add more social media.

reply

samuelzxu
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A visually grounded AI tutoring application: 
https://knowable.ca

Been working full-time on it for a few months, I'm trying to make the concept of an AI tutor better than just a chatbox.

reply

madprops
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

For the last couple of months I was working daily, and intensely, on Meltdown. The project started in 2024, but I retook it recently and improved/extended it a lot.

https://meltdown.merkoba.comThis is an AI Harness + Platform, made in Python and Tkinter.It has a lot of advanced features, arguments, commands, shortcuts.Lots of widgets and the markdown parser were done from scratch.It has a powerful API to create conversational sessions interactively.You can learn about it on a blog post I made:https://github.com/madprops/blog/blob/main/docs/meltdown/mel...

reply

bahmboo
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Wow! Let me be the first to crangukate you. It has lots of features and commands and arguments. I've been thinking about this for a long time. I've always said that we need commands and arguments. Maybe a cli. Keep it going bro!

reply

madprops
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don't know if you are being funny, but I say stuff like "arguments" because it has 452 of them, because I wanted to make almost everything configurable.

reply

marking-time
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a CLI tool that will build a static web page for a small brick and mortar store. The software is FOSS and could be useful for the small store that has a lot of foot traffic, but is under served by many of the big tech offerings. The idea is that foot traffic can be increased by using a QR code placed on a banner outside the store directing them to the website that can display sales and types of items that the store offers. Pleases check out the build log for details of my progress.

https://codeberg.org/Marking-Time/MicroStore

reply

oneneptune
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been a hobbyist game dev for years; nothing published.

Over the time I've built a massive collection of assets from various stores and stuff I've built.The solutions for managing assets seem to be largely in house tools studio build themselves and don't share.So I'm working on a digital asset management system that plays nicely with the tools I use; unreal engine, unity, and blender.I don't have anything public yet, but hopefully for September or October edition of this post!

reply

jdw64
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

cool!

reply

Oreb
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on The Marvelous Brass Chessplaying Automaton, a chess app for Apple platforms:

https://testflight.apple.com/join/mqfhpmHYThis work is motivated for my lifelong love for chess, my passion for Apple hardware and software (not as much as before, sadly), and my frustration of not having an Apple-native app comparable to ChessBase. My disappointment with the trend of recent macOS apps using Electron or other cross-platform frameworks instead of the native toolkits is also a factor. I miss the days when Apple users demanded more from macOS apps.My aim with MBCA is to create a serious chess app that satisfies the needs of everyone from club players to professionals, with a native Apple look and feel and iCloud sync. Currently the app supports the iPhone, iPad, Mac, and Apple Watch. I hope to make a visionOS port later. There is still a lot of work to do, but I’m having a lot of fun developing it, and I already find the current version very useful for my chess training.The name, in case you wonder, is from a short story by Gene Wolfe, my favorite science fiction author.

reply

jdwyah
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a 5 min multiplayer dungeon 
https://escapethe.app
 which the kids say “is actually fun”.

And taking a second crack at a feature flags withhttps://quonfig.combecause I seem to be unable to put this problem down and finally feel like I have the right git native and agent first approach.

reply

keithasaurus
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Blorp. 
https://blorp-lang.org

It takes inspiration from Python, Rust, Go, and functional programming. It's oriented toward readability, safety, and speed.I'm finishing up the journey of completely self-hosting. Then I'll be tidying it up for an initial release.

reply

saltysalt
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

A human-curated old school web search engine: 
https://greppr.org/

reply

yqiang
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building FitBee, a fast, ad-free, no-nonsense calorie and macro tracker for iPhone, iPad, and Apple Watch.
The app is built with Swift and SwiftUI, with a Python backend.

https://apps.apple.com/us/app/fitbee-calorie-macro-counter/i...

reply

ignatif
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

i'm working on a mobile app which spins up 
https://sprites.dev/
 sandboxes, allows you to log in with your coding agent cli/subscription (claude code and codex currently supported), connect other services (github, vercel) and run+manage your coding agents in a convenient chat interface

it's for people who dont own a home server, don't like to keep their laptops open and working, don't want to trust on magical stuff openclaw does and instead would like to work with the usual harness they are working with day-to-day, don't want to be vendor-locked (crush/opencode/glm-5.2 and other models/providers support to come) but want to have a way to execute ideas while being away from their laptopsthe demo is available on testflight and going to be released to play market soon as wellit's very alpha version but it's functionallmk if anyone would like to test

reply

Bnjoroge
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Looks cool! would be great if the pricing was down to the minute. Often some coding sessions might be quick ones, unless the focus is mostly on background agents that do long-running jobs.

reply

ignatif
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

sprites pricing is exactly down to a minute (or even second)

and sandboxes only operate when the agents is running and sleep when not. wake up time is super quick, under 5 seconds(on my side tho if i make it commercial, im thinking of making it free under 3 sprites/sandboxes and small subscription fee or one time payment for above)

reply

Bnjoroge
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

hmm, the pricing table shows it bills per-CPU hours. why did you specifically chose sprites.dev vs an alternative or making your own?Anything they do particularly better than others?

reply

ignatif
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

im planning to add support for e2b and maybe other sandbox providers (and ability to connect to your home server as well)

why sprites appealed to me is that they are stateful (the disk survives sleep and wake up) and that they are fast to wake up (and it’s not a 24/7 running vm in a traditional sense)making my own infra for that - not sure im in capacity atm

reply

calderarrow
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building Duolingo for blackjack card counting. It's a Progressive Web App so you can install, learn, and practice cross-platform, and it is designed to combine a mastery-styled lesson plan (e.g. you can't move onto until you demonstrate mastery of the current lesson) along with exercises and tools for keeping the skills sharp. A complete novice should be able to pick it up and become a profitable blackjack player.

It also contains tools for scouting casinos, logging sessions, calculating effective profit-per-hour based on table rules, and other things a professional would need.I'm in the process of polishing it up, and am aiming to launch Fall 2026. Current pricing plan is to be ~$10-15 per month for the pro tools, but provide the offline capabilities, lesson plan, and learning tools completely free without ads or weird gimmicks like a limited number of lessons or practice per day.

reply

adakbar
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm remaking an old MMORPG Canaan Online to be fully native web client, learn a lot like reverse engineering the client server protocol, a bit of network programming, and how to render that sweet nostalgic 2D sprite with WebGL. Currently had somewhat playable server and the client going, got lot of help from AI to learn the domain I quite not understand.

reply

gediz
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Today I resumed working on my open source browser extension to export chats from Microsoft Teams web client, after a two week long mandatory break due to busy dayjob activities. Now tackling the issues opened by users. Reached to more than 75000 users in less than a year, which makes me happy that its a useful thing.

Website is:https://teamschatexporter.com/

reply

piker
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Tritium, the legal IDE in pure Rust: 
https://tritium.legal

We're working on our WASM API this month, as AI-native startup law firms are looking to use it on their web platforms:https://tritium.legal/wasm

reply

metanoia_
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Six months ago I began writing and publishing one essay a month. Last month my wife and I hiked Fuego Volcano in Guatamela for our 20th anniversary. Here is my essay on that: A Country Within Myself - 
https://www.metanoia-research.com/dispatch-005-a-country-wit...
 .

reply

aleda145
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

10 years ago I rode my bicycle from Connecticut to Central America. I stayed in Antigua for a few days to just relax and reflect. Thanks for bringing those memories back!

reply

metanoia_
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That is quite the ride! You're welcome, glad to hear it brought back positive memories.

reply

blipvert
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Nice timing!

https://www.bbc.co.uk/news/videos/c9q91dnljpeo

reply

metanoia_
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes! The WSJ had a small article, a picture with a caption, about that. We were there two weeks ago, and our guide mentioned how he had never seen it so active.

reply

pupdogg
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Building FabShack, a white-label instant quoting engine that gives sheet metal fabricators SendCutSend/OshCut-level capabilities without needing an in-house software development team.

https://www.fabshack.io

reply

ig0r0
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on another iOS to help me learn Japanese, this time for explaining grammar. Put in a Japanese sentence, tap Analyze and you get grammar detected, highlighted, explained. There is a public testflight if anyone is interested 
https://setsumeiapp.kulman.sk/

reply

vmg12
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I made a site 
https://snack.game
 where people can upload and share multiplayer games.

It uses webtransport instead of websockets for the networking transport so the games feel a lot better than normal web based multiplayer games. I'm surprised more people aren't using webtransport given it's supported now by all major browsers.

reply

mikeshadpour
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

How has WebTransport treated you in practice? I just shipped a little live map where everyone sees new reports pop in as they happen — I went with Supabase's realtime channels because I didn't trust myself to run my own socket layer, but I keep wondering what I'd gain by going lower level. Did you hit browser-support pain?

reply

vmg12
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No browser support issues, the pain I run into is people running on vpns or their company's internet which block udp and by extension webtransport.

reply

CuriouslyC
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've pivoted to game dev because I'm burned out on AI dev tools. I started working on a hexpunk skirmish roguelite deckbuilder (working name is Hexborne) where you place units and structures on a hex scenario map to build a base and eliminate your opponent. Imagine a combination of X-Com 2 and Starcraft using cards, set in a world reminiscent of Arcane but 10,000 years in their future when humans have ascended to godhood and colonized the multiverse.

It's been a lot of fun, Godot and agents have taken most of the pain I remembered from my childhood attempts at game dev out of the equation so I can focus on game mechanics, art and lore. I'm almost ready to start soliciting external playtesters (which I'll admit is a bit stressful), I just need to clean up the UI/card templating/art/tooltips/etc so the game is accessible out of the gate and I don't churn for reasons other than the gameplay not being tuned yet.

reply

oryx1729
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building cloud managed self improving agents at 
https://sanbox.cloud
.

Each instance gets its own persistent file system, root SSH access and a web terminal. The goal is to let an agent build skills with experience rather than start from scratch on every task.I started with Hermes as the first harness and now exploring Prime Agent. You can use it for a personal assistant, use it to build LLM wiki, connect it as part of an agent team, or run any coding agent on the cloud with dangerously skip permissions.I’m also working towards a more general-purpose agent setup that can connect to channels such as email, WhatsApp, Telegram, Slack, Buzz.

reply

mrieck
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A lot of Claude plugins.

https://github.com/mrieck/demoday-claude-plugin- create demo videos for your projects using Claudehttps://github.com/mrieck/overboard-plugin- CTO assistant, PM helper Claude pluginhttps://plugmyplugin.com- Weekly voting contest and directory for Claude Plugins similar to Devhunt/ProductHunt

reply

epaga
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Nearing the release of my first game ever - Silent Shark, a tactical, map-based WW2 submarine sim releasing this Wednesday on PC, Mac, and Linux! I'm at about 17,000 wishlists on Steam and I'm having such a blast. Very impressed with Steam so far.

I designed Silent Shark to be the sweet spot of minimalism meeting realism of dials and procedures (like a simulated Torpedo Data Computer) that scratches my simmer geek itch without being impossible to write the game myself.https://store.steampowered.com/app/4705650/Silent_Shark/Browser demo:https://silentshark.app/alpha

reply

zahlman
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been hacking away on some scripts to clean up saved ChatGPT transcripts (surprisingly annoying because of how the app's JavaScript works, and I discovered too late that some of them were incomplete; but I have workarounds now) and convert them to a fairly minimal Markdown with some custom restructuring. This is mainly so I can share them on my blog and discuss some experiences of using the LLM; but also I'm extracting some code samples as the basis of some small projects I've had in mind for years but could never motivate myself to start (at least partly from an inability to choose).

In particular: an image viewer with a small suite of extra functionality; and a browser extension for cleaning up URLs and then bookmarking them in a more organized way that I might actually use meaningfully.

reply

foxtrot8672
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://pendragon.foxtrotcommunications.net/

A legit attempt at making an AI financial advisor for everyday Americans. Most Americans can't afford a human CFP which can cost thousands of dollars a year. We offer a great AI driven alternative for less than $300/yr.

reply

pravj
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on two projects.

## Tab Highway: Browser extension focusing on the UX/process of declutteringIt turns tab cleanup into a game.When you pile up too many open tabs or whenever you want, it opens a night drive where each tab is a road sign you drive through or send to the trash.[GitHub](https://github.com/pravj/TAB-HIGHWAY)This is still a work in progress. It works on my machine, but not fully distribution-ready.## A short satirical blog on the overly-expressive/interactive web experiments fueled by coding agents.Ironically, the project listed above falls in the same category.[Woodworking Has Been Achieved Internally](https://hackpravj.com/blog/woodworking-has-been-achieved-int...)

reply

ferCats99
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I got laid off on the recent job cut wave industry wide, so I just started working on cars, it's been really fun to know deeper how something with higher physical consequences work, today I was looking on another old beat up car from marketplace, might work on my father's F150 next week, and got back to the industry this monday with another Tech Consultant job, so, been having a nice time

reply

onion2k
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I wrote a release train modelling app (
https://allaboard.ooer.com/
) and it turned out so horribly complex and hard to use I'm building a general systems modelling app instead so I can rebuild the model in a nice text format.

reply

idorosen
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

My side project this quarter has been building a system that adds steering / planning to LLMs/WAMs/etc. (T, DiT, etc.) in a market/physics/other-ground-truth-constraints aware way. I have a small model outperforming some of the largest frontier models in some games (i.e., adversarial settings) now, but that is not very impressive because "plain old LLMs" are the wrong mathematical object for gameplay, IMO. So far, it's a mix of RL + optimization (e.g., MILP) on the planning side, and not quite realtime enough to play RTSes, but that's only a few weeks away. Have been very impressed at how far the open source ecosystem for this stuff has gotten since the last time I tried something like this.

reply

gottebp
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I resurrected an ancient UIUC x86 ASM game, built with some friends in the summer of 2002 for ECE291. Claude Code drove most of the work.

The first attempt was a full on x86asm->webasm transpiler which ran into some difficult stack issues.The second attempt was successful via conversion from x86asm->c->emscripten->wasm [0]. It plays pretty well on mobile and just about any browser now.Fair warning it is pretty difficult to win, unless you can figure out where the enemy weaknesses are [1].[0] [code]https://github.com/gottebp/alan_parsons_project[1] [play]https://particlefield.com/projects/alan-parsons/game.html

reply

mrnotcrazy
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Ever since I read this 
https://paulbupejr.com/developing-the-optigap-sensor-system/
 I've wanted to build a system that takes in a shape and adds bends and fiber routing so you can dynamically create readable objects. I was initially imagining wanting to add the bending points manually but I'm not so sure that's the best practice and I may want to think of a heuristic for good vs bad bend points before even considering the UI.

I also bought some cheap gloves from harbor freight and used a needle to route fiber through each finger to make a simple power glove like thing which I think I can connect to arm arm to make a cool robot game. I think of the two I am more excited for the first but its much more work than the second and my day job is getting more exciting than I would like so by the end of the month I'll have had to pick one to finish.

reply

arkmm
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a simple sandboxed way to run open weight models over a copy of all my personal data (email, docs, messaging, photos, etc). Think it'd be cool to have a self hosted AI "chief of staff" that has full read access to my personal info.

reply

kirilale
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Few things, trying to take full advantage of AI coding and my domains.

FutureOfGaming.com - In-depth weekly analysis revealing what's actually being developed in gaming, from new player experiences to technical innovation. Over 1,000 gaming patents covered since Nov last year. Every Tuesday for patents and Thursdays for filed.ContentCreators.com - education, free toolkits, tools directory, job board for content creators. Recently also set up creator profiles to build out a creator directory and connect with brands.WebsiteAudit.com - does what it says, run my websites through it to identify gaps - anything from performance, security, SEO and get recommended fixes. Looking to expand to also add brand AI visibility, hoping to launch soon. Still in testing

reply

biotinker
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I was laid off in early June (was a staff software eng at Viam writing motion planning software for robots) and have been fiddling with electronics.

Most recently I made a portable AQI meter, since the air quality here in Central Oregon can quickly get bad.It's a small 3d printed box containing a rpi pico, an 18650 battery, an e-ink display, and a SEN66 sensor.I hit a button, it turns on, runs the sensor for ~40 seconds to get a good reading, displays on the e-ink, and then turns off. So there's zero power draw when it's off, and the battery lasts for ~1500 readings. Accuracy seems fine, the AQI, temp, and CO2 readings all match my permanently placed sensors inside and outdoors.Other projects include using some of the old leftover robot scrap to automate irrigation in my apple orchard.

reply

Kuyawa
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Research on an AI super agent that manages memory, knowledge, skills, tools, other agents, channels, management and orchestration, and auto update its own code at the end of every session if needed

Previous agents developed:Kattohttps://www.npmjs.com/package/@kuyawa/kattoMechahttps://www.npmjs.com/package/mecha-ai

reply

bitexploder
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Work: Security engineering focused on securing authnz at hyperscale in our new agentic reality. What interests me? Agentic engineering, vulnerability discovery at massive scale. Vulnerability remediation at massive scale. Bounding agent non-determinism.

Personal: Local models. Agent harnesses. Track cars, turning wrenches.Had agents build recently:- Photo catalog app with all 100K photos in my library described by a local 9B parameter model (it is absolutely amazing and my favorite personal project in terms of genuien impact)- Generic RAG layer (vector embedding + FTS in SQLite with RRF and document ingestiation layers for 1-2GB knowledge bases to power agent context for stuff I am interested in, neuroscience and philosophy is where I spend time on this right now, and basically every AI research paper publicly available to help agents tinker with local models). This is especially useful for local models, but it even helps frontier models because they can freely churn through without a bunch of web calls and such when you are on a topic thread or research.- Qwen 3.6 35B A3B clean-up proxy, achieving a clean thinking + tool calling A3B that I can leave running for 24+ hours. This particular model gets stuck in long reasoning chains and needs encouragement to get on with it, especially on context tasks. It actually reasons well but then starts second guessing and loops. Built a deterministic framework to inspect its thinking and make it wrap its thinking up if it gets stuck and also to trigger calls to external models and inject solutions to problems when it gets stuck. The agent sees the solution injected from a remote model like it is its own thinking, kind of a subconscious it has no idea about. Metacognition in models, it is wild.DSV4->GLM->Kimi is the "phone a friend" external brain pathing I built. As far as I know no one has shared all of the bugs I have 'fixed' in my project and gotten local Qwen A3B this reliable.

reply

wgx
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building an image sharing site (just for me and a couple of friends) that tries to emulate the old days of Flickr and Instagram. Chronological feed, no recommendation algorithm, no reels, no ads, etc. Knowing that it’ll never be open to registration or “real” users takes all the pressure and expectation away and it’s just been fun to work on.

reply

Igor_Wiwi
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Adding Java class inline editing without decompilation feature to 
https://jar.tools/class-decompiler
 - so you can update some class values (number or strings, or event access modifiers) without needing to recompile the .class file. I called it Tweaks

reply

yassi_dev
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a way to build internal tools inside the Django admin and make them accessible to both humans and agents.

https://github.com/django-control-room

reply

shakermaker83
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been having fun building out a link-in-bio tool / micro-site builder in my spare time. It started out as just something that a solo-dev could build without a lot of experience... but it's turned out to be more complicated and interesting than I thought! Right now I'm working on getting embeds and other 'fancier' types of blocks built out. Also… if any SEO wizards are lurking, I would love tips on getting more Google impressions/CTR, lol.
If you want to check it out (would love some feedback!):

https://soc.bio

reply

petegordon
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Tandem bike physics game with device motion, controller gyro and multiplayer. Open source.

https://tandemonium.jimandi.loveSteam play test:https://store.steampowered.com/app/4482940/Tandemonium/Open source:https://github.com/petegordon/tandemonium

reply

arionhardison
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been working on automating many of the programs that federal prisons run to help newly released inmates with re-entry.

Example:https://atlanta-fci.bop.doj.dev/program/65545-inmate-account...

reply

tisdadd
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been working on the marketing site for an ETL Product that I am ready to launch, and this thread made me realize that I should ask in another thread about recommended MoR/affiliate programs for current day.

This is meant to be something that will help business teams be better able to communicate what they want, while producing ready to deploy tech artifacts that do not rely on AI.More importantly, I have been working on being a Dad - something we were told would be impossible naturally. Way more fun than being in front of the computer - our little one is nearly six months old now, and sleeping through the night until usually at least 8 AM, starting to roll over and enjoy tummy time more, and bringing smiles everywhere she goes.

reply

joddystreet
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

SaaS vendors that manage PII data needs to go through the - security questionnaires, privacy assessments, vendor risk reviews, procurement due diligence, evidence requests - sent by the customer security team.

At digicred, we were managing these in google drive and jira, but with 500+ enterprise customers, and their annual vendor reviews, this practice became unmanagable.CAOS is a dedicated workspace that helps us manage these assessments like projects, additionally, CAOS turns the questionnaires into a system of record. Questionnaires become structured, answerable work. Finished answers and your compliance documents become a searchable, citable corpus. The next questionnaire starts from what you already said, with every claim traceable to the document or prior answer it came from.It is self-hosted. Your policies, your answers, and your customers' questionnaires stay on your infrastructure.Recently open-sourced -https://github.com/DigiCred-OSS/caos-os

reply

joddystreet
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Follow up - What have you been curious about lately?

- Canvas for Agents- LLMs for learning.|Idea: Don't use LLMs for summarisation.
 |Proof of concept-https://www.youtube.com/watch?v=1oF9M5hAazw|Repo-https://github.com/veris-pr/bwaiz

reply

stillpointlab
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a platform for context management that includes apps that operate on structured text formats (e.g. YAML, JSON, XML, MD) and provides editors for structured text formats (code editing using codemirror, markdown editing using prosemirror) and eventually all media assets (images, videos, audio).

The idea is you have a set of sources (e.g. Github, Google Docs, local file system), a bunch of transformations (templates, apps, llms/gen-ai, simulations) and sinks (communicated through changesets). The platform is like a cache layer that connects these together and allows for a graph of operations (source->executor->sink->source->executor->etc.) which allows for tracing the lineage of assets through a system.It's an impossibly large vision made barely possible with agental coding assistance.

reply

samsk
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've finalized and have in beta testing an AI-based natural language search of properties from an MLS feed. On top of that, I'm continually tuning an AI agent that is able to do property research, comparisons, neighborhood and history analysis, etc.

[1]:https://mlsync.ai

reply

Nan0pk
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/Nan0pk/Rush-linux
 A Linux variant one dynamic power and peromance tuning daemon, because Why Not--- 

https://github.com/Nan0pk/local-ai-relay
 A relay to grab Ai web chat and run it as openai compatible provider to run batch jobs 

https://github.com/Nan0pk/Archiv
 An offline Ai first institutional memory harness, ingesting office docs and outputing cited formatted deliverables.

reply

wingtw
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Been building a data ontology project i call Tirith - think palantir's gotham + their different modules on top. Can ingest from different sources (textual, structured or freeform for now, images + video coming maybe later), detect relationships between objects, view graph, geospatial view and rudimentary analysts view. Very raw but with the help of nlp and/or openai compatible cheap model like deepseek its already amazingly capable.

And second thing im building is out of sheer frustration as a father of 5 in the school info management -https://www.classtable.org- aims to be a full school management software which is easy to use for both school staff, students AND (personal itch) for parents to keep an eye on their childrens progress

reply

beeneeb
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I got laid off on Friday so I'm using it as an opportunity to dogfood briansjobsearch.com again. I'm working on a Chrome extension that will help with autofilling job applications. It has dramatically sped up the time it takes to apply to each job even on complicated ATS's.

reply

darkurtpanke
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

A prolog to c compiler

I got depressed from my grievance with my abusive mother and started reading the compiler dragon book along with artificial intelligence by steve.https://github.com/x64x2/proc

reply

Jernesstar
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

A graph-based code editor

https://miralume.dev

reply

davidsojevic
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a web-based image editor with plenty of customisation and support for most Photoshop features.

Built overwhelmingly in vanilla JS with a couple of WASM modules for it.It’s generally very performant across the app so far, but there’s still a handful of features that are functional but subpar in terms of performance that I need to address.

reply

thedreammachine
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Two open-source initiatives:

1.https://preseason.aiBasically a benchmarking platform that measures how the top LLMs recommend devtools when prompted to build different types of web apps.2.https://widen.devA native Mac desktop Postgres GUI with text-to-SQL. You can even use the LLM that already comes installed in your MacOS.

reply

iagooar
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a framework that allows creating very complex SaaS products with AI, that actually work. Very complex = +100k LOC of one-shotted AI-generated code. Codename o2p - outcome-to-proof.

It is a research-first method for designing or reviewing SaaS products. Its central question is:
What customer outcome matters, and what evidence proves that the product delivers it?Idea or existing product
→ Research real customers and current work
→ Identify their Jobs to Be Done
→ Design the minimum safe workflow, define the interface and system behavior (with a sophisticated scoring system)
→ Validate the workflow
→ Implement vertical slices
→ Observe proof of customer progress

reply

rorytbyrne
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on “Supabase for science”: 1-click deploy of scientific databases with validation, transformation, MCP, export-for-ML, and provenance built in.

https://amacrin.com

reply

thimotedupuch
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on Amber.jl an acausal analog electronics simulation tool driven by Julia code. Just like in PyTorch, the neural network 
is
 the code, here the circuit is the code as well.

Because SPICE wasn't built for programmers in mind. The code in 0.1.0 is almost ready and I'll put the github repo public soon.

reply

Arubis
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

I don't know that SPICE was built for _usability_ in mind. I distinctly remember hand-drawing circuits on paper and numbering the nodes as I typed them into PSPICE because there was no schematic visualization functionality at all. I promise you, this was in this millennium, not last.

reply

relssiegp
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

A C++ lib to write SIMD code like you would write GLSL: CPPShader 
https://github.com/gitdepierre/cppshader
. I need to clean up the code a bit right now, and I'll add SSE2 support for older CPUs (currently requiring SSE4, but I want to see it working on C2D and Atom. I just need to replace the blendv functions with something compatible with SSE2). Then I'll focus on adding NEON support.

reply

ChrisMarshallNY
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I am in the final stages of preparing to ship a 2.0 version of a fairly successful app, that has been shipping for a couple of years.

This is a complete, bottom-to-top rewrite (front- and backend). It's ahugeimprovement. I used an LLM, quite a bit. It's been a big help.We're in the last stages of the first-wave testers. This is the one that affects the app UI. After this, we expand the test, and do bug fixes only.Also, we need to start taking screenshots and app previews for the App Store. That requires setting up a test server, with anonymized (fake) users, so we don't compromise actual user anonymity. It's a bit of a pain, but it has to be done.

reply

hugodan
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I am looking into ways to make UIs in the AI age, where text is their natural substract

reply

jwgarber
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Finishing up my GSoC project with MalariaGEN. We're writing a new tool to estimate kinship coefficients between mosquitoes genomes and the project got a lot bigger than I initially planned haha. I'm going to tie up a smaller part for the GSoC submission in August and then keep working on the rest for a paper we're writing up. Also a big shout out to AVX-512 and sleef, for numerical work it is just 
chef's kiss
. For anyone curious you can see the tools used to analyze DNA for disease vector control here, it's pretty interesting :)

https://anopheles-genomic-surveillance.github.io/home.html

reply

gste
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I started making a programming language that is designed to encompass frontend, backend, database, container, and cluster, so that there it is not necessary to stitch together other languages.

It uses functional programming and event sourcing to try and effectively "solve" modern distributed web application development, so that your app code in this language can be extremely simple but not have bad architecture and gaps.I'm probably oversimplifying the complexity, so I don't even know if it's feasible, but it's pretty fun to give Claude my crazy ideas and see what happens.https://github.com/georgestephenson/beck

reply

gpjt
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm adding MoE support to the GPT-2 code from Sebastian Raschka's "Build a Large Language Model (From Scratch)". Just the minimal changes. Planning to do (or at least start!) a from-scratch base model training run on my own hardware before the end of the month.

reply

joch
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I have two personal projects at the moment.

First,https://agency.nu/a personal agent platform for people who aren’t necessarily developers, but still want to connect multiple Gmail, Calendar, and other accounts and automate workflows across them. Spent a lot of time making the interaction easy and natural, so it supports chat, realtime voice and telegram.Second,https://vinarium.one/something I primarily built for myself to keep track of the wines in my wine fridge, when to drink them, and what pairs well with a particular dish.Both are very much scratching my own itch, but I’m curious if either resonates with anyone else here.

reply

timeisapear
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

https://ballcast.app

Hosting an XGBoost-model for MLB totals predictions. It runs every thirty minutes: incorporating weather at the hyperlocal level and joins with player attributes that are provably affected by that weather. It also provides advanced decision-making tools with a Kelly Criterion calculator built in. Model still needs some calibration for bet-sizing but is very close to production-ready.Robust historical evaluations available athttps://ballcast.app/validation

reply

lopatin
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm reviving my multi-player Snake game Snaketron. It's written in Rust and probably the most technically interesting thing about it is that it's built for auto scalable Cloud hosting. The websocket isn't tied to the host actually running the game. And it can scale and rebalance in the middle of the a match without disrupting the game.

https://snaketron.iohttps://github.com/lopatin/Snaketron

reply

qudat
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m iterating on a constellation of git collab services that I’m calling “the disappearing code forge.” All self hostable with a focus on minimalism and Unix philosophy.

I just revamped the collaboration portion which is a patchbin service:https://pr.pico.shAs part of that I work im also iterating on the ci/cd solution we are calling pici:https://ci.pico.shAMA

reply

ra0x3
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've always ran into an issue running arbitrary processes - whether it be for serious production work, or just toy scripts. So many choices with so many dependencies, featuring so many foot-guns. So I decided to take a stab at solving the problem. Would love any feedback or contributors :)

SystemG - An agent-friendly general process composer.-https://sysg.dev/-https://github.com/ra0x3/systemg-https://docs.rs/systemg/latest/systemg/

reply

solomonb
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Waiting for the remaining broadcast equipment for my LPFM (www.kpbj.fm) to arrive! Then we finally get on the broadcast band. We have over 80 shows at this point. We still need fundraising support. If you are in Los Angeles and want to support freeform community please reach out.

reply

jfil
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on writing up pages for projecthammer.org, the new website where I'll host my database of Canadian grocery prices. It's getting interest from more academics and needs a more formal home.

I've been curious about ways in which politicians who are in the minority/out of power can still make progress on issues that matter to them.

reply

zerodollar
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a platform to make hiring simple and easy for recruiters.
Also, increasing candidates/job applicants visibility when applying for a particular job.

reply

kidnoodle
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been playing around with exploiting LLMs having ‘read’ every book ever written to make a chatbot to help people choose library books. You talk to it a bit about things you’ve read, and it uses the llm’s latent knowledge of books to suggest ones you might like.

It’s pretty fun! It might even work on your local library (I got carried away and spent a while making it work on a few thousand round the world - you can see the coverage here:https://leafle.nanosheep.net/coverage).https://leafle.nanosheep.net

reply

kushalpandya
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Petrichor, a music player for macOS: 
https://petrichor.page/

This has been my work outside of work, which I spend most of my weekends on. It has gotten enough downloads (23k+) and traction to motivate me to continue.

reply

david927
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

This is fantastic and exactly what I needed. Thank you!

reply

schipperai
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on “nah” [1] an agent hook guard that blocks catastrophic agent actions like filesystem destruction, secrets exfiltration, and git disasters.

All the agent hook guards I’ve seen can be easily removed by agents (and they often do so they can get going with the task). I made mine harder to remove, and I’m working on making it impossible.I also made “nah” easily extensible. Just point your agent to the docs which ship with the CLI, and ask it to build a custom guard.I’m working on strong Python and Typescript pseudo-interpreters so I can detect disasters in inline code with less false positives. Bash parser is already very strong.This is a side-project that I want to be proud off. I spend a lot of time designing, not just coding.[1] nahguard.ai

reply

nbbaier
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Love the vibe of the website!

reply

cwmoore
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Enjoying an Upper Midwest summer and:

https://www.kakurokokoro.com/sudocubehttps://www.ouruboroi.com/famous

reply

nhatcher
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

As per usual for the last two years I'm working on an open source spreadsheet engine called IronCalc. It is super exciting. We have a proof of concept at

https://app.ironcalc.comIn the last couple of months my partner and myself quit our jobs to work on that. I am pretty sure that in a year from now the world is going to have a fairly competent spreadsheet alternative.My capacity is fairly limited but I am trying to build a community around it. Join us!https://github.com/ironcalc/IronCalc

reply

iot_devs
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

How is ironcalc different from other spreadsheets?

reply

nhatcher
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

From Excel/Google sheets because ot is MIT/Apache 2.

From libre office because it is web first and also an engine firstIt's written in Rust and has bindings to different languages. It's extremely light and fast

reply

conrs
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

The world runs on spreadsheets! How do you plan on sustaining the business?

reply

nhatcher
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I regrettably don't have a good plan for that. We have a grant from the European Union that will pay our salaries for another year or so.

reply

troyvit
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm updating Metabase's Podman documentation to reflect using Quadlet instead of "the old way." It's my first open source contribution in quite awhile and while it's tiny I'm excited for it. It's a chance to get to know pi.dev, not to write, but to behave as a copy editor and fact checker. Since it uses Mistral on the back-end it's a 
slightly insane
 copy editor and fact checker, but that's almost better. It's forcing me to check everything I say.

reply

marko-krkeljas
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a painting of coneflowers and black-eyed susans from near where I live in New York City.

https://imgur.com/a/kP1aKIUOil on canvas, about 28 x 22 in.

reply

mrkpdl
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Gorgeous! Keep going

reply

dgellow
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Looks really neat

reply

johnchinjew
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a simple multiplayer word game: 
http://alphabetsoup.club

It's a bit like NYT Spelling Bee, except it's multiplayer and only your best (longest) word counts toward your score. So, instead of trying to find as many words as possible, the game is more about finding one unusually good word.Funny timing, I just made my first Show HN post for this a few minutes ago:https://news.ycombinator.com/item?id=49235347

reply

nshntarora
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

A free and open source chrome extension to help people review code - 
https://guidedreview.dev

It upgrades your GitHub pull request review experience with a guided walkthrough of the PR optimized for reading.

reply

pandaman28
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a multiplayer stock trading game that was inspired by all my favorite board games. 
https://www.spellfolio.com/

It's a web-based game for 1-8 players, features a tutorial and bots, plays like a board game, and operates with economy, bluffing, forward-planning, risk-taking, course-correcting mechanics.Play as an amateur psychic navigating a fictional stock market. Receive premonitions, call in your wizard friend, navigate dividends & earnings releases, and chase the glamorous annual investor awards.If you try it out, please leave me some feedback :)

reply

dvd42
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

My family has gotten into camping the past couple years. I was navigating around the Texas State Parks' website and got annoyed trying to find the right combination of amenities, trails, etc.

I decided to make my own version of the state parks website which surfaces precisely what you need for all parks in one place and make it filterable. I've been adding states and features to it for the last month or so and I'm up to 20 states and 1252 parks.I try to keep each parks' fire bans, alerts, and events updated on a cadence.https://park-finder.com

reply

dvd42
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

In the interest of sharing more, I was drinking margaritas with a buddy when he said he forgot his log book. I thought, hold on, we can fix this. So I made a web app to record your margaritas(all stored locally on your device).

https://rueda.bar

reply

dvd42
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

One more I've been working on:
My wife and I have been watching Star Trek TNG together(my 4th time or so), her first. I though it would be cool to follow the path that the enterprise took, and couldn't find a good site that did so dynamically.

I've been pulling a bunch of stuff from Memory Alpha, Scripts, and the Star Charts, and have a reasonably interesting visualization of a few series.https://star-trek.pages.dev/A lot of the locations are inferred due to... storytelling.

reply

vunderba
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm still working on Hackerman recorder. As a programmer, I really enjoy having live coding videos playing in the background while I work. But it's surprisingly difficult to find hour+ long videos of coding without commentary on Youtube.

What I really wanted was an infinite coding video, so I built one. Pick your IDE/monitor/ambience of choice, hit the Screensaver button, put it on a second monitor or TV, and enjoy infinite coding ASMR.Recently added a Paper Mode which shows an animated quill that scrawls across a parchment for public domain novels.https://hackerman.specr.net

reply

dummydummy1234
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

So I am working on building a low latency streaming dataflow framework - ala gnuradio but actually usable in production. The idea is to have deterministic latency as a first class objective and let all the other benefits fall out of that.

Additionally:Live graph reconfiguration
Timed events
Easy simd support
Support for non-mmu based architectures
Imperitive configuration management and querying at the single runtime level.
Can be compiled to wasm, and run in the browser (w/ coors headers).
IO/user interface and any GUI is done via typescript.

reply

ramoz
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/backnotprop/plannotator
 is still very useful for annotating html prototypes and markdown plans (as well as terminal agent messages). Was glad to see codex team pick up the feature requests in the Codex App.

About to release a fun paid version. All contributors get lifetime free access.Better running agents run longer, they need better plans. (is my bet)

reply

ramijames
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been slowly building [MiserablyUnemployed.com](
https://miserablyunemployed.com/
) for the last four or five months.

It pulls jobs from tens of thousands of company HR pages, and only keeps them for seven days (unless it sees that the job has been filled). No reposts. Only fresh jobs.Besides that it has a resume builder, matching system, application assistance via an extension, job tracking software, and an interview preparation helper. It turned into some fairly complex software that I ended up learning a lot from!If any of you try it, let me know what you think.

reply

wingtw
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Love the name! :)

reply

ramijames
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks!

reply

wingtw
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Btw, when coming back from buying the credits, return url is invalid (double domain name - 
https://miserablyunemployed.com,https//www.miserablyunemploy...
)

reply

ramijames
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks for letting me know. Will fix!

edit: found it. What a stupid mistake. Fixed.

reply

wingtw
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

What a familiar feeling :D

reply

ramijames
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

:)

reply

reidjs
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Text message reminders and automation.

Send the service number a text message like "call Dave in 2 hours"and then in 2 hours you get a text back that says "call Dave"Open in private beta if you're interested email:textreminders@hazybridge.com

reply

sp1982
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

https://corvi.careers/reports/technology-stack-trends/

It tracks explicit mentions of ~ 181 languages, technologies, vendors, etc as seen in job postings. The motivation was that GitHub activity and developer surveys describe what people use or enjoy, but not necessarily what employers are requesting.

reply

joefreeman
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've continued to work on a modal text editor, which has a server-client architecture that supports multiple clients (terminal, native, web) with consistent UI/bindings. I'm not using an editor as I used to, so this is more oriented around viewing/navigating code. I've recently been working on adding a Markdown viewer. The process of being able to use the editor and then get Claude to quickly make changes has been very satisfying.

I've also revived a project to design/implement a programming language. I'm slowing converging on a (keyword-less) syntax and (Beam-like) architecture that's starting to feel good.

reply

dennisy
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Any link yet?

reply

joefreeman
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Aether (the editor):

-https://github.com/joefreeman/aetherQuiver (the language):-https://github.com/joefreeman/quiver-https://quiver.run(online REPL)

reply

vldszn
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

hi! i'm building 
https://easyinvoicepdf.com
 - a free and open-source invoice generator.

currently building a backend for recurring invoices, a public API, and an MCP server. recently hit 1k stars on GitHub =)https://github.com/VladSez/easy-invoice-pdffeatures:- no sign-up required and no ads- live PDF preview & instant download- save seller & buyer profiles- flexible tax support (VAT, GST, sales tax, etc.)- fully customizable invoice templates- 120+ currencies and 10 languages supported- and much more

reply

emp_
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Just promoting a small utility for others that may need it.

For us MacOS users that use Spaces and want to CMD+Tab only inside that Space, the only alternative was AltTab (that I could find) but it has so many more features and goals, plus I had performance issues with it remotely over HPSS which I use heavily so I've generated the simplest utility that only shrinks the CMD+Tab list per Space and nothing else.https://github.com/emp/SpaceTab

reply

dasyud
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

This is perfect! Thank you!

reply

scottcodie
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

A new transformers architecture based on relational data instead of text. Been exploring search reranking based on graph data and customer prediction.

https://github.com/relativedb/relational-transformershttps://relationaltransformers.com/You can read more about the architecture here:https://relativedb.com/blog/relational-transformer

reply

sentinel1909
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Finally, after at least 5 years of trying, I've figured out a photo storage engine for myself, backed by a SQLite database and Cloudflare R2.

https://metallian-photos.fly.devIt's an Actix Web/Tera/Datastar concoction, hosted on `fly.io`. It provides the backing for galleries for my music site:https://crusty-metallian.netNow, if only I could actually write something for the blog part...

reply

cprecioso
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been gearing up for launching Todone, a CLI / GitHub Action that can scan comments with URLs to GitHub issues, Figma comments, or browser support pages, and more (plugin system available); and open an issue when the issue or comment is resolved, or your target browser has that feature, etc

It’s still in flux and a bit slow as I have to juggle it with my day job, but pretty excited to launch it once it’s good enough for a 1.0!https://github.com/todone-run/todone

reply

bcowde
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

A workflow orchestration engine built for agent harnesses e.g. Hermes:

https://github.com/blairjordan/pygmyhippo

reply

nbbaier
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Reminds me a bit of 
https://github.com/earendil-works/absurd

reply

sqwxl
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a go (the game) server. still unpolished, but it's functional! currently hosted on a raspberry pi in my living room and proxied to the public Web via Tailscale.
Rust backend, SQLite, preact frontend.

https://pi.basilisk-aeolian.ts.net

reply

rbsmith
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working my way through "Improving Heuristics for A* Pathfinding". Thank you so much, HN!

https://news.ycombinator.com/item?id=49079995

reply

plasticsoprano
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Had a problem this week helping a customer troubleshoot some SAML interactions. They couldn't install SAML Tracer in their environment and I got tired of digging through HAR files and manually decoding SAML assertions and the like so I made 
https://hartosaml.com/
.

Just drop in your HAR file and get immediate insights into the SAML related events.

reply

mmsc
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I recently got a Magic Keyboard and Magic Trackpad and have been using them on two different Macbooks (work and non-work).

I couldn't find a good way switch them between different Macs, so I madehttps://github.com/MegaManSec/magic-switch. It's a small application which allows you to basically share the peripherals between Macs, and send them back-and-forth either manually or automatically.

reply

Schiendelman
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Would you consider publishing to the mac app store?

reply

mmsc
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm working on it: 
https://github.com/MegaManSec/magic-switch/issues/67

reply

enduser
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Since January I've been working on a storytelling system that fuses what I think is the best of interactive fiction / MUDs with the strengths of LLMs. The world model is entirely deterministic, but the LLM interprets the player and narrates the game and NPCs.

Also hacking on something similar to YC's QM but designed for small non-profits to ease as much back office work as possible.

reply

mial
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building Prospex (
https://prospex.ch
), a lead-generation tool for B2B salespeople in Switzerland. This is just a side-project as I have a full-time job.

Basically, I'm collecting public data (official registries, job boards, company websites, linkedin etc) to surface sales opportunity signals, like leadership change, new branch/market entry, funding rounds, etc.

reply

thread123
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I had a lot of chats in OpenRouter, google AI Studio and lm studio and no good way to view/search/combine them together. ThreadShelf started as a local archive with semantic search/MCP, and later grew support for continuing conversations through llama.cpp or OpenRouter.

https://github.com/ChrystianSchutz/ThreadShelf

It is my first time creating oss so please be gentle.

reply

eliasson
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I have had fun building a small test-framework in Gleam recently.

https://github.com/eliasson/garanti/Just this friday I wrote an article that took a look under the hood.https://markuseliasson.se/article/under-the-hood-of-a-gleam-...

reply

tornikeo
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

https://peachjam.dev/

A low-cost vibecoding website for non-developers. Still in alpha.

reply

eg312
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

An interactive compound-interest explainer, based on The Compound Effect book 
https://github.com/alexadam/compound-effect

Added more widgets to Printable Mockupshttps://github.com/alexadam/printable-mockups&https://www.printablemockups.com/

reply

matnosner
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

neely (
https://neely.app
) - club & team management for amateur sports clubs in the DACH region, starting with youth handball. I coach youth handball myself. The incumbent here is SpielerPlus - practically every handball team in Germany uses it, and I've yet to meet a coach who's happy with it. That gap is the whole opportunity.

Most inventions are just better versions of things that already exist - I'm building the Google Workspace for clubs.

reply

mlhpdx
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on a sailing watch system for clubs and teams without the resources for existing systems (thousands of dollars per boat).

I’m starting with the Waveshare ESP-32 watch. It has a great price tag and features, and an impossibly small battery for regattas that run for hours over two days. Designing it for super low power like this, no internet (regattas are often rural), and very high expectations (competitive sailors) is challenging and fun.Ultimately custom hardware (probably Nordic based) will be in the cards, but for now I’m engineering a solution from what I have.

reply

ashot
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on codecast. Something that started as a way to index / search and sync agent sessions from their jsonl files has turned into a high level desktop/mobile orchestration and product / steering layer above agent sessions. It's a huge productivity boon for me and for teams that have adopted it.

reply

josters
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on making an old Nokia 3210 use 4G because 2G is being shut down within the next two years in most European countries.

As it currently looks I need to design my own PCB with a modern LTE module and make it connect to all the peripherals. Thought it would be a nice project to get into electronics, soldering etc. Also really enjoying the constraints of an 84x48 LCD screen and how to implement "modern" technology like GPS navigation or design the UI for a music player.

reply

_spl
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on WatchCat — uptime and cron monitoring.

I’ve always enjoyed solving observability and reliability problems, so eventually I decided to build my own take on the boring-but-important "is it actually working?" part of the stack.It does uptime checks, cron/heartbeat monitoring, incidents, status pages and notifications. Nothing revolutionary — the goal is to make the familiar stuff simple, reliable, and pleasant to use.It’s built with Rails and hosted in the EU.https://watchcat.io

reply

emporas
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I am experimenting with using A.I. to see an image, and generate TinyScheme code to draw it on Gimp. As soon as I got the code for a 2D representation, then I bring out the heavy weaponry, Rust and Freecad, and with some more information added I generate the 3D representation of a building.

A.I. generally shines when the steps are small and incremental. I would add that, when A.I. is used properly, generating code and hopping from one code to another, it should be better than any human already.

reply

BubbleRings
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A music recommender website oriented towards albums.

Tell it your 5 favorite albums, get an immediate suggestions list. No sign up, free to use, integrated with Spotify to hear immediate samples (or the whole album).https://SimilaritiesEngine.com

reply

jermaustin1
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

I liked this. I agreed with most of the suggestions (primarily because I knew them already), so I know the "algorithm" is working. There were a couple of groups I had never heard before, so double success!

reply

skor
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Audion, interpreted scripting language that is fun to write and lets you make interactive music, a/v installations using supercollider or any daw and hardware. BPM synchronization between real OS threads and Ableton sync is built in as well. 

https://github.com/audion-lang/audion

hack music

reply

jakegmaths
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a photo book system that respects privacy via no tracking, not sending anything to the server until you go to print (all stored in indexeddb until then) and even then requires as few details as possible (eg email address optional), and no sign up at all. Then everything deleted within a month. It's at 
https://www.rgbloom.com/
 and UK only for now.

reply

gregolo
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Otakit.app - skip App Store review delays!

reply

vlaaad
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I work on 2 things that are the same thing:
1. ghosttyfx — libghostty terminal for JavaFX (
https://github.com/vlaaad/ghosttyfx/
)
2. trying to integrate ghosttyfx into the Defold editor (
https://defold.com/
)

Turns out integrating into a bigger IDE is much harder than just implementing a JavaFX view using libghostty...

reply

adityaathalye
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been following my curiosity to see if I can find "ten (or twenty) year projects", as part of my "second life"; the first was before turning 40-ish, the second is now.

I think I have found three, and they will keep me quite busy for a while.Read/Think:Bioelectric networks as the software plane of morphologycf. Allen Center / Levin labs / TAMEhttps://arxiv.org/abs/2201.10346and other work from that fecund lab is ever-fascinating. I have been following their work for five or six years. Much of that informed a giant essay I wrote prompted by an essay contest on Consciousness:https://www.evalapply.org/posts/consciousness-lives-in-a-ded...Read/Think/Research/Write:How to write a Hard SciFi novel that does not have magic technology genius, and certainly not magic ET showing up to save the day?A spec fic author friend is on my case about it, because he said "why the hell haven't you written your novel yet?" and I foolishly said "yeah why not? okay let me do it", and now I'm stuck in an honour pact. Write or die trying.Side-quest of $DayJob:Um, how does the weather even work (metrology)?Because that's what happens when you're helping an applied sciences team run weather forecasting models, like WRF (pronounced "Worf", which I absolutely love :D). My day-to-day is packer and FreeBSD and shell scripts, but I have to also understand enough about the domain to be somewhat dangerous.And also...whyisn't everybody using FreeBSD + ZFS for all their server workloads?---x-posted from my earlier question [0] that David offered to fold into this regular Ask HN he runs... Thanks again; this is cool :)[0]https://news.ycombinator.com/item?id=49101448#49106213

reply

dbmikus
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://www.amika.dev/
, which lets you put sandboxed agents on cloud VMs and then message them over the internet.

It's for agent + human devboxes, for chatting with coding agents from the web, or automating them with an API. Thing like Claude Code web, but any agent and you directly control the VM, too.We're working to make amika.dev work on any computer, homelab, or K8S cluster. For tech folks, I describe it kinda like if Tailscale and Firecracker had a baby.

reply

ultra_nick
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

https://conceptionary.app/

I've been working on an AI Tutor or Primer that automatically generates Duolingo style curriculums. Planning to apply to YC after the next big feature release.The current website is a rushed out MVP. It takes a significant amount of data science and prompt engineering to generate good courses, so it's taking me a bit longer to build the true vision.

reply

longnguyen
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I have tons of fun building a custom OS for my little ESP32 device: 
https://x.com/daniel_nguyenx/status/2086311226012025006

It now has power management, a launcher, iOS-inspired Control Center, an AI voice assistant (using OpenAI Realtime API), a tamagotchi-style app and I recently built the iBeer app :D

reply

nbbaier
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Which device is this? I'm thinking of hopping on the ESP32 bandwagon!

reply

longnguyen
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's Waveshare ESP32-C6-Touch-AMOLED-2.16 but you should get the ESP32-S3 version. It's better than the C6 (older version).

reply

seanwalker08
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on GameBeacon, a different take on LFG(looking for gamers) app/website where gamers can sign up, light a beacon and invite friends to a game session. You can also add your games to build a game collection, including a neat way to scan photos of your physical games using AI. 
https://www.gamerbeacon.com/
 and download the app in the app stores. Been a blast using it with my buddies on VR games weekly.

reply

SamPatt
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I have a Pebble Time 2, which is an open source watch. I built a voice operated AI assistant for it.

It's hosted on a VPS, connected over Tailscale, and has a realtime TTS server (Piper).The Pebble has built in transcription, so my app takes the transcript, hits the server endpoint with three possible paths:1. Deterministic responseThe server looks for certain triggers from the transcript like "Add task," "Complete task," "Set a timer," etc that will run a simple function on server and write / retrieve to a database, no LLM call needed. It then responds with the TTS output and the watch speaks. This path is nearly instant.2. Fast responseIf no trigger is found, then it hits a gpt5.6 Luna endpoint, which decides if it can answer the query itself, or if it needs to defer to the big brother model. If it can handle a query itself, it usually responds to simple questions in less than 8 seconds. It's also good about properly deferring, very close to 100% after a few weeks.3. Deferred responseThe VPS hosts a Hermes installation, and for more complicated tasks or for ongoing projects the Luna router sends it to the Hermes agent. This is typically quite slow, as you'd expect, but remarkably capable. I built the voice app to cache a few lines like "this will take some time" which will automatically trigger if the router indicates it's deferring, and then will respond with the full response from Hermes once it's finished (sometimes minutes later).Pebble has a quiet mode, and my app will only display the text response if it's on, otherwise all responses are run through the TTS. Piper is so fast that this adds almost no time to the response.In only a few weeks this has become the primary way I set up tasks, review and close them, set timers and reminders, log my weight, check in on the progress of projects I'm running on Hermes, and ask simple day to day AI questions.Since Pebble is open source, AI tools are very good at building it, and it's trivially easy to set it up so that you can just ask the model to deploy it live. It's an awesome experience to tell it to change something, and two minutes later, that change is on your wrist.Very fun project!

reply

namanyayg
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

I had no idea you could do something like this through the Pebble!

I pre-ordered mine last year but it looks like it's not going to come before September :(As soon as it gets here I think this is the first project I'm going to attempt. It'll be helpful you've got any resources or source code for the Pebble STT and TTS parts. (I already have my own hermes that I want to hook it up to)

reply

SamPatt
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The Pebbble transcription is part of their SDK and very easy to use programmatically, also it's quite accurate (not perfect but good enough that I turned confirmation off).

The TTS is Piper installed on the same VPS as Hermes.Happy to answer questions or share code. I might publish the device app eventually. I hope your Pebble arrives soon, it's a great device.

reply

josevalerio
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a cross platform screenshot/screen recording tool with a built in editor:

https://github.com/joswayski/capturesManaged to snag a cool domain for it too!http://captur.es/Would love any feedback from anyone that tries it

reply

ChicagoDave
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Finishing up the IDE (Chord Writer) for my new Interactive Fiction modeling language (Chord) for web+parser based games.

https://sharpee.net/https://sharpee.plover.net/

reply

NiloCK
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://letterspractice.com

This is a high efficiency, narrowly-scoped, low screen-time early literacy app for families with kids aged 2+.

reply

bewal416
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I just released my 2nd app to the App Store: Just Chess Puzzles

It’s as simple as it sounds: 100,000 chess puzzles, all offline, rated (just like chess.com or lichess puzzle modes)A big thing I added that makes mine unique is the play it out” mode that allows you to finish the game with a chess engine of equal difficultyYou get 20 free puzzles per day, or a $5 lifetime purchase for unlimited puzzles and features:https://justchesspuzzles.com

reply

dividedcomet
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

My own IDE!

https://github.com/paradise-runner/toastIt has all the parts I want (lsps, syntax highlighting, a file tree) without the parts I don’t (a bundled terminal, tracking, ai)

reply

iot_devs
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

A writing app.

The overall idea is to work/write at an higher level of abstraction where you work with "ideas" (just small paragraphs).You can move them around and basically restructure many/whole paragraphs by simply changing few words.The final text is generated by an LLM.LLM that has the whole context so you can ask it questions, but more importantly it can provide you feedback

reply

iot_devs
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

I put it online and accessible for people to try! Any feedback is welcome!

https://structo.redbeardlab.com/

reply

fmxexpress
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Orchestrating an AI agent built in native Object Pascal for Free Pascal Compiler and Delphi. Runs in less than 10MB of RAM. Besides being very Windows forward and local first; doing some fun things with it like incorporating WebLLM and running it in the browser inside a WASM Linux.

Https://pasclaw.dev/

reply

conradfr
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Recently completed GearPix 
https://www.gearpix.app/

Which is an app and audio plugin to take and send pictures to a DAW tracks and have them stored in the project file.Not vibecoded but I must say Claude was a big help to finish and debug my C++ code (which I didn't know before this).

reply

nospi
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

This is a great idea, nice one. Does it run as a VST plugin per channel or something?

reply

conradfr
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks. Yes it's a regular plugin that you insert as many times as you want.

reply

pranshuchittora
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on building open-source QA agent for software teams. Consider starring on GitHub - 
https://github.com/vostride/agent-qa
 | Landing 
https://vostride.ai/

reply

wookmaster
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a music sheet app that takes photos and turns it into a local doc you can play midi on, plenty exist but they all want subscriptions to use them. Trying to see if I can do it with pure local phone processing. Still in PoC Phase. The app world is tiring with the lockouts for yearly subscriptions fees of $50+. Apple promotes them too since they get a cut.

reply

MaxLeiter
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I got GIMP running natively on my iPad, and am now working towards VS Code and a few other useful *nix apps

https://files.maxleiter.com/f/gimp-on-ipad-optimized-Dyuygd6...

reply

emn4tor
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm currently working on an open-source End-to-End Encrypted P2P Chat-Platform similar to matrix but with the thinnest backend possible, the backend is a a simple directory server + relay, nothing more you can find more about it in the readme on GitHub :) 

https://github.com/Emn4tor/Seal

reply

edimaudo
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a new tool that can analyze employment contracts and see if there are issues. Also gives the ability to ask labor questions across Canada

reply

shivang2607
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Currently working on Intelligent Codebase Visualizer for reactjs/Nextjs/js and ts Codebases for easy PR review, easy onboarding and easy PR review.

Github:https://github.com/devlensio/devlensOSShttps://devlens.io

reply

achristmascarl
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I recently added autocomplete to rainfrog, the terminal UI database tool I've been working on: 
https://github.com/achristmascarl/rainfrog

I initially made it as a lightweight, keyboard-centric alternative to dbeaver/pgadmin, and it now covers 95%+ of the database-related tasks I need to do at my job.

reply

tmilard
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Been improving the gui of my 3D-web-Player runtime.
- What al I building ?

==> An FPS game editor, using photos as 1st imput.
==> It delivers a realistic FPS game. immersive-visit-game as we like to call it.
==> The FPS-Runtime is the lightest FPS existing today. It works on any web device, even Smartphones.==>https://free-visit.net/

reply

sim04ful
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

https://design.withfudge.com
.

It gives agents the ability to find website design references to improve their design skills via the mcp -https://design.withfudge.com/mcpYou can also critic your existing designs against competition.

reply

jjcm
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Some feedback:

When I enter a url to give me feedback for, it prompts signin, then returns you to the homepage instead of a review for the url you wanted a review for.Conversations on the left should be named. Right now they're just "new conversation". These name themselves after the conversation is complete, but you should be able to fire off a query to a smaller LLM based on the prompt to name them asap.The biggest thing though, the feedback it gave me was incorrect. Not the subjective parts, but the objective bits were incorrect. Here's what it told me:> Change: Make the first viewport a contained product argument:> 1. Navigation and one primary action> 2. Short headline and supporting sentence> 3. A real prompt-to-interface example> 4. One compact proof point or “before / after” comparisonMy landing page (https://diffui.ai) has nav and one primary action. It has a short headline and a supporting sentence. It has a real prompt-to-interface example. It has a before (prompt) and after (multipage web design) in the example.I suspect that it got confused due to this being an interactive example, but a lot of this (the headline/supporting sentence) are present in the screenshot it took.Overall though not a bad start. Good work sourcing references.

reply

sim04ful
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Could you by any chance, share the conversation link here ? there's a share button at the top right

reply

jjcm
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

https://chat.withfudge.com/share/0gqaxigvh1/give_me_feedback...

reply

sim04ful
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Thanks for the feedback, working on it.

reply

emehex
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working a new Fantasy Football league/format that is category-based (like hockey/baseball) in an attempt to make games more "watchable". The problem with traditional Fantasy Football, is that half of the game (defence) is ignored, while not very economically-valuable positions, like RB and TE, are elevated far past their real world relevance. This new system is my attempt at fixing both problems!

reply

bix6
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I just bought a home so doing tons of little projects and a couple big ones, it’s endless!

AI wise I’ve been refining my workout app for a few months and it’s ~90% there - I get good workouts now but I’m constantly tweaking / adding features. My kanban / planning tool has also become very useable with the latest updates. Next up I’m working more on a guitar practice app and a baby life app.

reply

tel
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on an improved Markdown that offers a simplified language, clear hooks for extensibility, and a governance model to let it grow over time.

reply

dataviz1000
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been using coding agents to drive data visualization to help me understand complex concepts. Here is the latest on how reasoning models reason:

A probability grid of chain-of-thought, read through Boyd's OODA loop lens[0][0]https://adamsohn.com/reasoning-grid/

reply

skyfantom
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

One of the projects I’d like to highlight is Cheaspoly.

It’s an attempt to make chess a bit more, you know real:) Like countries buy armies, chess kings can buy figures. Also it’s easy to bring these new rules into offline games.It’s quite early stage yet, but you can give it whirl athttps://chesspoly.com/

reply

robbomacrae
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Benchmarking public agent skills: Oh My ClaudeCode, Superpowers, Git Ship Done, (previously Get Shit Done), and the Karpathy ones against Swebench-Pro and SlopCodeBench. I have a July vs June breakdown. It's been an interesting learning exercise and reveals the cost/performance impact of using these.

https://orcabot.com/benchmarks

reply

oinoom
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Reflect [1], it’s a local-first privacy focused self tracking and data analysis app where you can set goals and run self experiments

[1]https://apps.apple.com/us/app/reflect-track-anything/id64638...

reply

snoke308
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

These are all really good comments and ideas! 
I created a tool to help facilitate, track and recover lost revenue from Stripe subscriptions for SaaS companies. Called RertyForge, www.retryforge.com
It lets a failed payment be seen from a company owner’s perspective. Why things fail, what works best to recover it, what step of the process is most successful, who is most at risk right now. 
It’s bootstrapped and just getting it off the ground. Love any feedback or questions

reply

melenaboija
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

An opensource derivatives pricing engine, distributed and built on QuantLib and gRPC + FlatBuffers.

https://github.com/joseprupi/quantraserverhttps://quantra.io/

reply

jvink
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on the ability to create mixnets with sanctum [0] and its cathedrals.

Sanctum already has very capable traffic analysis protections in place in the form of shroud, but being able to build mixnets will make it even more valuable.But it’s been vacation time so it’s been slow progress as time away from the internet is equally valuable.[0]https://sanctorum.se

reply

red_hare
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm in the process of planning an indoor-outdoor wedding in NYC so I made a little weather history explore tool

https://12seasons.nyc/explore/

reply

robertn702
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building a registry for packages that add WebMCP tools to sites that have not adopted WebMCP yet. Each package describes tools for a specific site as json and those tools are injected and executed using a browser extension.

https://webmcp.today/

reply

jborden13
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working to redefine funeral home operations with 
https://www.everpath.to/

We're competing in October for the NFDA Innovation Award with it and looking for funeral home design partner(s).

reply

4b11b4
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

An experimental merge queue that takes changes amends/inserts into history instead of dumping at the end

reply

4b11b4
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Also a variant of Question-Options-Criteria that rides alongside your git history

reply

the__alchemist
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Bio tools: CLI app, Python or rust lib for installing and running structural bio/drug-design software without the user messing with python envs, conda, system deps etc: 
https://github.com/David-OConnor/bio_tools

reply

pkukkapalli
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been trying to get better at chess recently. But also wanted to explore some AI agent development hands on on the side. So, I built an AI chess coach to analyze my games, learning openings, and drill different endgames and such.

https://thenimzo.com

reply

sarreph
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

https://dozenal.game

A daily puzzle game called Dozenal where you solve each puzzle board by creating chains totalling the number12.My friend and I came up with the idea over a decade a go, and have finally started bringing it to life in the past couple of months.

reply

iamhaseeb
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Personal website engine for developers. Check it out -> 
https://github.com/iam-mhaseeb/koji

reply

majicDave
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I am releasing my music player into open beta this week! I’ve been working on it for a year or so, created my own language, engine, and network protocol to make it all sync wirelessly, and with no AI :) 
https://github.com/mjdave/katipoBrowser

reply

wz3chen
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building a site to help me keep track of the stocks I follow.

* Automatically sets alerts when I favorite a stock* Discuss and analyze stocks with AI* Generate AI research reportsWould love feedback from other investors/builders:https://getmarketalerts.com/

reply

jerpint
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://www.woltspace.com/
 over the last few months. It’s my take at an agent orchestration framework

It builds around the concept of “wolts” running a lodge. A wolt takes the identity of a rodent (racoon, beaver or otter) and can inherit any supported coding harness: claude code, codex, opencode, etc. Each wolt carries a persistent identity and memory, so they always know where you left off.woltspace is designed to help you host your apps directly from woltspace on your machine. If it works on your machine, it works anywhere. This is done through Cloudflare tunnels that you can setup with your own domains (or using ephemeral domains).Under the hood, woltspace is powered by tmux, which means that sessions persist and can easily be resumed and accessed from anywhere. I personally drive woltspace mainly from the telegram integration, which gives me access to my wolts and CLI literally from anywhere. This means I can chat with Claude code CLI from anywhere, spawn new sessions, all running on my own infra. It’s also all in a docker container so you don’t have to worry about approving every single command.95% of woltspace was built from within woltspace, and it’s becoming my prefered way of building.Another feature I really like: the “inter wolt communication layer”, IWCL, allows wolts to chat with each other, making things like having fable orchestrate a gpt 5.6 something that works out the gate.Woltspace is meant to be used by power users (you can bring your own tmux config and use the TUI CLI) or by beginners. The default split pane makes SEEING what you’re working on really intuitive. Each wolt can host its own website where they can render arbitrary html making planning new features much more intuitive.It’s all open source, and I’m constantly adding features to it. Woltspace is mostly self documenting, all of the features are also skills the wolts have access to. I'm also improving the documentation surrounding the project as we speak.Looking for some feedback and users to try it out. You can one line install it withcurl -fsSLhttps://woltspace.com/install.sh| bashProject page: www.woltspace.com GitHub:https://github.com/jerpint/woltspace

reply

mmmnnn
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

iI am working on a synth engine (music synthesizer) in Python and C++
not a developer; music producer, classical pianist, and occasional NI Reaktor programmer.

It creates sound from math expressions which were inspired by the Desmos graphing calculator.The sounds are mainly of the FM/DX7 taste.i can't decide whether to show my progress on video by hiding or showing the expressions LLM(s) and myself "discovered".It sometimes sounds extremely musical and sometimes very dirty and experimental, what's normal for frequency modulation.Please help me decide: show all and open source or continue working on it and pitch it to some big names. ;-) I have the feeling it has strong potential for prototyping, as well as taking the role of a keyboard engine. It is completely viable to manipulation via AI because of its concept.It runs nicely on an M4 Mac mini with 256 voices of polyphony and has a very high level of expressivity mainly via half-pedaling (sustain pedal).Velocity, 8 macro knobs, no filters, no fx, ADSR envelope. A web interface and additionally CLI.

reply

thinkdecidedo
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I am still working on my IndexedDB manager browser extension, Kahuna. The recent release added direct editing of values from the grid view for all 42 data types that can be stored in IndexedDB.

https://github.com/hummingme/kahuna

reply

aamargulies
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Automatic local events aggregator 
https://whatson.town/

reply

nbbaier
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

This is cool, please add Chicago!

Also, what data sources do you aggregate from?

reply

aamargulies
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Chicago is there! Look in the cities dropdown menu.
getting sources is the trick… I’ve made some discoveries about how to ‘reverse-engineer’ a city.

reply

nbbaier
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Oh nice! Silly my, I didn't scroll up!

reply

GonzaloRizzo
 
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

I am also very interested in knowing how you source that information :)

reply

freshteapot
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on an update to my mobile client for Learnalist, specifically bringing upgrade path to gate 200 free flashcard entries before payment.
This now includes, a new add UX, embracing images on the server, not local anymore.

Aside from this:- I asked codex to use my mobile app and web page for the flashcard UX, and make me one using qt + qml so I could run it on the remarkable 2, super happy with the initial results. This will be released as a reference for others, as the eco-system is too clunky today to offer it the non-technical users of remarkable devices.- I learnt about my set-up box, and got assistance in making my first app, so I can post and image from my iphone to it via shortcuts. Currently, it only accepts one photo, but it is cool throwing it up on the tv. This also let me learn a little more about "ios Shortcuts" and cherri, a golang cli, that makes it a little easier to make shortcuts.- Using nurb, to 3d print things, currently working thru printing a stand, so I can mount an iphone and record doing things on the remarkable. Its been really fun testing with little physical prototypes of small parts to then roll into the stand.#Reference-https://nurb.dev/-https://x.com/freshteapot/status/2085692070337888698-https://learnalist.net/features/mobile-learnalist-v1.html

reply

davedx
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a bunch of stuff, but most interesting is maybe 
https://Octoloops.com
 - it's a sort of marketing harness for indie devs/SMBs. Still early days yet, feedback very welcome!

reply

TheSorcerer
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I've built Ziggity an ultra fast, keyboard driven terminal UI for Git, written in Zig 
https://github.com/simoarpe/ziggity

reply

manish_gill
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Published [0] a few days back - learning IO techniques in Linux. Got as far as epoll and will explore io_uring next!

[0]https://parallelthoughts.xyz/2026/08/learning-linux-io-part-...

reply

robstinson
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I love shared daily puzzle games. Wordle, crosswords, that kind of thing.

Swudoku is my take on a daily sudoku puzzle. All the numbers are on the board, you just need to rearrange them to complete the game.Been running it for over a year now with daily plays from friends and family who enjoy it. Recently took a stab at an iPhone app for it as well.https://swudoku.com/

reply

alexpogosyan
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm bilding Jamful - ios audio looper app. I always loved using guitar looper pedals, so i wanted to have something similar on my phone. Currently it's on TestFlight 
https://testflight.apple.com/join/W7nD6v5H

reply

vunderba
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Very cool. I've been using "Loopy" / "Loopy HD" for years as my primary looper on my iPad - makes it really easy to use with AudioBus to route synths over to it as well.

reply

joewhale
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

My wife hates clutter and the junk that we've accumulated the past few years because of our two children receiving junk toys.

I built a simple wish list app that anyone can create a wish list and share without the need to create an account. Great for birthdays, evergreen lists, Christmas, etc.whichwishlist.com/

reply

gboss
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Why don’t you throw out or donate the toys if they’re in acceptable condition? No need to hold on to gifts you don’t like.

reply

mbloom1915
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://memoryindex.io/
 :

A better way to track real-time pricing of DRAM and HBM pricing in the market specific to equipment type, manufacturer, and other metrics. Feedback welcome to improve and see if there is a market for something more in-depth.

reply

jmox
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been working on my master's thesis. I am not really young anymore, so finding the time was tricky.. until I started working with AI agents. Then I started using frontier models and I couldn't sleep anymore, trying to maximize my usage limits.
The project is called Agent Sandboxing Framework. If you are interested in AI agents and security, I’d love to hear what you think.

https://github.com/javimox/asf

reply

willmeyers
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm still working on CT RailTime. It's an app I made to make traveling on CTrail better. CTDOT's app they've outsourced is really bad and broken most of the time. People who use CTrail deserve something that works.

https://ctrailtime.com

reply

opiniateddev
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

A software SDLC harness that can run complex long horizon coding projects.

https://github.com/conductor-oss/conductor-agents/tree/main/...Open for collaboration, still in early dev.

reply

bhouston
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Been working on adding support for Gaussian Splats directly in ThreeJS specifically for WebGPU:

https://ben3d.ca/blog/gaussian-splatting-for-threejsThis PR was merged yesterday morning so the August ThreeJS release will have this new feature.

reply

rmzdotno
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Fast native language (java/rust) regular expression matchers:

* Java:https://github.com/la3lma/rmatch* Rust:https://github.com/la3lma/rustmatch

reply

hamza_q_
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

NVIDIA Parakeet running locally in the browser. Implemented in raw WebGPU compute shaders & SIMD WebAssembly audio frontend:

https://parakeet.narcotic.shThe aim is for it to be a high-performance implementation. Can currently transcribe 1 hour of audio in 20 seconds on an M5 Mac.

reply

dgellow
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I started yesterday working on an airless 3d printed tire/wheel for my electric scooter, and got the first full PLA prototype. Currently waiting for small scale TPU tests to decide which of my designs to go with, and I expect to have a working prototype tomorrow or Tuesday

reply

fasteddie31003
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Two things. 
https://www.draftdownapp.com/
 an open source 3d modeler. 
https://factchronicle.com/
 a fact-based news story aggregator.

reply

pranabsarkar
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on AI memory. Have been working on YantrikDB since January this year. Started as a pet project solving my own problem but now its growing. It's fun and satisfying at the same time

reply

merelysounds
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Larger puzzles in my puzzle game[1].

And some yak shaving in the form of selective zoom, where only the board would zoom in but the clues around the board would still remain visible.[1]:https://lab174.com/nonoverse

reply

alienbaby
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

a toy thing for the game path of exile 2.

Fed up of wading through a metric oodle of waystones and tablets to figure what best, along with a billion stash tabs full of a zillion items.I'm making a tool that scans your inventories and lets you rank and analyse things based on their affixes, so the best ones according to criteria you set pop out at you, minus the hours of staring and thinking.Hobby project, so full on vibe coded zero code review type stuff. If it works, thats good enough. for now, anyway.KimiK3 is the weapon of choice for this one, and its doing pretty damn good!

reply

igor_nast
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on an Agentic IDE (free) - multiple AI agents support + classic IDE experience

https://shikigami.devBETA - means, production ready, but not still extending and experimenting with features - I keep working on it, and collecting feedback.

reply

414techie
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Cool idea. Have you considered making this work on Windows?

reply

igor_nast
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

yes, thank you for adding +1 to this feature request.

If you use windows and would like to test it once released please join the discord server or find me on linkedin. I have one potential tester, and maybe another one (you) if you contact me. :) Thank you for the feedback!

reply

uzidil
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

A roguelike with card battles: 

https://uzudil.itch.io/rquest

Very early. Tech: raylib-zig with Lua, loreline convos, shaders. Graphics in aseprite.

reply

pianopatrick
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I rewrote my AI agent written in POSIX sh to be a single file. So now to use it all you have to do is download the file, mark it executable, and set up environment variables.

https://github.com/patrickjh/ssa

reply

POiNTx
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a puzzle game Quilt. Hope to get the demo out this coming week or next week.

https://store.steampowered.com/app/4760970/Quilt/

reply

duxup
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've slowly been making some tiny apps that just don't collect data in anyway that I want to use myself, pretty basic stuff. I'm sure there are plenty of them but I feel like it says something the world of smartphone apps that they're hard to find.

reply

topper00_raptor
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Atoll, it's part of my Archipel project.

It's just me, building my own tools and self-hosting them. 
Atoll is a project management project. Nothing fancy, not over-engineered: 
- Go
- SQLite
- HTMX (server side rendered, no SPA)Archipel will count different other projects (Atoll, Balise, Passe, Sillage)

reply

nbbaier
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Sounds interesting, where can I find out more?

reply

fy20
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a house. I contracted out the structural shell and exterior, then all the internal work I'm doing myself. Except for plumbing, I don't want to be responsible for creating a swimming pool. In my country there is no such thing as "permits", you can do any work on your own house without certifications. If I had gas I'd contract that out too.

It started when my ex and I were having trouble in our marriage (divorce will be finalised soon), probably after watching too many a YouTube DIY channels, and here I am a year and a half later :DI moved in when it became livable 6 months ago (I had to shower at the gym for a month), and it should be finished sometime next year. I don't work that much on it though, as I am busy with my job and kids. Some rooms are nearly finished, others are barely started. I've got used to the concrete slab as a flooring and no doors.Would I recommend it? Ummmm... probably not. But it's been an interesting experience, and I've learned a lot. I don't want to diminish professional contractors, as some of them are really skilled, but I feel you can get most of the way to "standard home finish" by watching a few YouTube videos on the topic. You will be slower of course and might need to repeat/fix your work, but then to push it to "luxury-ish finish" you mainly just need a good eye for detail.An important lesson I learnt is the phrase "paint covers a multitude of sins" is wrong, as paint does not cover it, your mistakes will still be visible just in a different colour. Joint compound/plaster does though :D

reply

planting
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building Wellsy (
https://wellsy.se/en
), a mobile app (iOS + Android) that turns CBT methods into structured programs for diet, lifestyle and emotional wellbeing.

reply

elpakal
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Sports betting odds over sms (US only). I’ve had to work with carriers to get exemptions as they have rules about providing betting advice or being affiliated with sportsbooks, which has been interesting.

reply

Exorust
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been digging deep into Metal and I recently made this! 

https://github.com/Exorust/metalworking/

Idk who it helps, but it's been a fun journey!!

reply

themousepotato
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Lately been obsessed with learning and doing sales coming from a software engineering background. Working on 
https://getsolenoid.com/
 to help the builders reach out to people with more buying intend.

reply

l5870uoo9y
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Found existing React web frameworks either bloated, buggy or too complex, so I built: 
https://www.rshono.com/

reply

Room10Mind
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

SupportWire → agentic live chat platform for startups: 
https://supportwire.ai

I have fallen in love with the idea the more I spoke to potential customers. The initial feedback has given me confidence to commit to this full-time.

reply

wmedrano
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm creating an Emacs package out of the custom JJ stuff I had. I'll probably publish it to Melpa in a month or so.

https://github.com/wmedrano/consult-jj

reply

ismael_rr
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

for you tennis players out there, I'm working on RallyClip, an app for free tennis match segmentation. It's a free and open source alternative to SwingVision:

github:https://github.com/iroblesrazzaq/RallyClipwebsite: rallyclip.appI'm working on model performance and an iOS app right now; would love feedback on the macOS desktop app.

reply

kuchin
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on a Principal AI Engineer - a harness that learns your code, asks the questions you didn’t think of, shows you exactly what to fix, so your AI project stops breaking in production. Basically, turning what I do for a living into an agent.

reply

code-delta-app
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve developed a code scanner that compares releases and calculates logical statement LLOC churn and detects Ai agents embedded in large codebases. 
https://www.codedelta.app/

reply

pixxxel
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

https://portr.dev
 -> Open source ngrok alternative

https://dbcooper.amal.sh-> Database client

reply

freakynit
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

I loved it.. but, can't use it yet because it's tight bounding with cloudflare managed dns and in-built caddy.

Created this issue:https://github.com/amalshaji/portr/issues/308

reply

anax32
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a simple model inference platform: 
https://marigold.run

Seems everyone is building an inference platform lately, but this one is mine! And I'm enjoying it...!

reply

pryelluw
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

My comedy newsletter featuring short-ish essays about random nonsense: 
https://yelluwcomedy.substack.com/

reply

ghoshbishakh
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on analytics for AI chat and search. Suppose you have a sports shoe brand, then you would like to track what AIs recommend when they are asked "best running shoe".

https://lumirank.ai/

reply

agustinxix
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on [
https://ui.human-kit.com/
](
https://ui.human-kit.com/
) a (still in beta) headless UI library for Svelte. I couldn't find any option that fit my use case, so I decided to build my own and share it to the world.

I've been working on this guy toohttps://github.com/Agustin-Delgado/repath. It's a modern circuit sim with a lot of bugs and things to be tested.

reply

hpen
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

A keyframe animation editor for native app components. Wrap your views in a special type, and load up the editor to drag around keyframes.

https://www.inertiagraphics.com

reply

Aeroi
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Camera Search - visual intelligence app for tradesmen, blue collar workers. www.camerasearch.ai

Surviving Dreams - long horizon code agents that work while you sleep. we're unlocking the next 12 hours of gdp.
www.survivingdreams.com

reply

bobek
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Git back hacking an old flip-dot display. It was sitting on the shelf for years.

https://www.bobek.cz/buse/

reply

WalterGR
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

For further inspiration, also see the previous Ask HN for August: 
https://news.ycombinator.com/item?id=49148884

20 points | 6 days ago | 68 comments

reply

david927
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Just a fun thing I do: editing films to music. 
https://brodlist.com/sfe

P.S. Credit to adityaathalye for the change of phrasing for these posts to add "what are you curious about?"

reply

mcapodici
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

A new tech YouTube channel. It might be all AI or not but we'll see!

https://m.youtube.com/@MartinCapodici

reply

mcjiggerlog
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Waystops (
https://www.waystops.com
), a map-based travel app for working out what destinations exist and which are actually worth visiting.

Google Maps is great for route planning and looking up things you already know about, but it's pretty useless for discovery. Sometimes you just want to know what places are actually worth going to as a tourist or backpacker.It's the kind of information you'd traditionally get from guide books, but in a format that IMO makes a lot more sense - a map. Right now the scores and content are seeded by an AI, but the idea would be for these to eventually be user-derived.It's still pretty early and I have a WIP native app which makes it a lot nicer to interact with on mobile, but it would be awesome to get people trying it out already. It's free to use, with nothing paywalled or anything like that. I'd only think about some kind of monetization if it actually gets some traction. Would love any feedback!

reply

julia-kafarska
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on PaaS called Light Cloud 
https://light-cloud.com
 
Light Cloud is an alternative to Vercel + Render + DB's with projects management.

reply

timmit
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Finance AI Agent

https://tradeinsight.info/ti-agent

reply

kenforthewin
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on my AI-augmented knowledge graph app, Atomic: 
https://github.com/kenforthewin/atomic

reply

goerch
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm slowly finding my way back to testing local LLMs (out of fear of price spikes). Currently positively surprised by OpenVINO. But my private benchmarks indicate not to trust edge models too much.

reply

fenio
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on my own NAS system based on NixOS and bcachefs.

https://github.com/nasty-project/nasty

reply

voodooEntity
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I have started working on a 1 Person RTS project (crazy right? i know :D)

Basically a 2d rts, fully orthogonal view, plays in space with spaceship combat.You start with a deployable base, kinda like the old C&C, which you can place around a minable planet. Than from this you can place further structures arround that planet including the typicals, mining (2 types) of resources, researching stuff, and building ships.The 2 things i focus the most on in this game on are1. Responsiveness. Im a strong fan of starcraft 2 (and brood war) and have spend tons of time playing sc2. I love this super responsive controles and its the only thing i will settle for in terms of controles2. I love the game starsector (yes no rts) for the way its ships are designed. You have a base hull that has some stats like hp / speed / etc - than this thing has basically mountpoints where you can fit weapons into. I always loved this system. So what i build is a game where you can (outside of battle) define your desired ship blueprints combined of a hull, weapons and "inbuilds" (as in upgrades). You can than just build those ships ingame.So ye made quite progress so far , not sure tho what will be the first mode i focus on once i get a playable (as in demo) state.Btw using godot engine as base, but some logic is running as c++ gd extensions (rts is heavy calcs , gdscript is just not fast enaugh (or im just not a gamdev ¯\_(ツ)_/¯)Here a screenshot of the ship blueprint editor for those who are curious
-https://i.postimg.cc/bq5JB9J7/editorexample.jpg

reply

t4nner
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

emira, a tiling-scrolling WM for macOS: 
https://github.com/lightningboltemoji/emira

I know there are lots of options in this space, but I wanted to experiment with a new approach: a compositor overlay. During transitions (like scrolling on focus, moving a window, etc.) an overlay pops up and uses _screenshots_ of windows for animating while the real windows move below. Once in place, the cover dissolves out. It's not perfect, but this makes it _feel_ much closer to native.

reply

dbz
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I just passed the 1M lines of code mark using Claude for this project!

https://www.GetSetReply.comI help small businesses with review management. Getting more reviews, replying to reviews, and some other related features.Right now I'm trying to figure out how to get users and make sales. I'd love advice from someone in the community that is willing to share their experience and wisdom!Similarly, if there are folks here from outside of the US with some ideas/feedback on getting into other markets, I'm interested to hear about that too.The other project I've been working on is:https://ALovelyQuestion.comWe plan proposals within your budget

reply

purple-leafy
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Reflecting on my projects [0]

[0] -https://github.com/con-dogNeural networks | Game engines | Games | LLM Benchmarks | Graphics

reply

davekubehub
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

building kubehub.io , build a private cloud with your own hardware, manage through kubernetes, most important easy to use.

kubernetes on prem setup take a lot of works, even if you setup the cluster there are tons of work wating for you to setup ingress/gateway/DNS/TLS/monitoring.kubehub.io solves all those problems.

reply

marktolson
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

https://runnit.io
 - work / project management and automation for creative teams

reply

memset
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building a tool that lets me organize sheet music, rehearsals, and share with groups I play with.

Also building a Golang middleware to record analytics (saved into a local duckdb)

reply

heresalexandria
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Pawvis, visual hand-tracking mouse & voice control that's open-source and fully local on your Mac (with optional handoff to Codex or Claude Code for complex computer use tasks).

We live in the future, and I wanted to use my computer the way it's been depicted in movies for decades. It turned out more capable than I'd expected and frankly really fun to use.Homepage:https://pawvis.appGitHub:http://github.com/alexandriax/pawvisDemo:https://www.youtube.com/watch?v=1mdwqP0bwUk

reply

elpakal
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

dotIPA, an iOS app build size inspector that runs locally on your macOS [$4.99]
Track app size growth over time, inspect contents, spot duplication and size bloat and more.

https://apps.apple.com/us/app/dotipa/id6742254881

reply

marktolson
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

https://runnit.io
 - creative team work/project management system

reply

usamaasfar
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://sunware.ai/
 to automate software work like GitHub Actions.

reply

raver1975
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Autonomous mathematics research. 
If you like reading articles about mathematics, you might enjoy this:

https://alethean.org

reply

drchiu
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on Broadcast: 
https://sendbroadcast.net

What it is: Self-hosted email marketing softwareBeen doing so since 2024 (pre AI coding era).

reply

greenfish6
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

An agentic marketplace where people can buy business services from inside their claude code: 
https://talkshi.com

reply

pmarreck
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I had issues with reproducing some fuzz testing failures in CI locally; turns out that glibc, musl and macOS actually DO NOT return the same floating point values for certain trig/transcendental functions across all OS'es, so I decided to rectify that by spelunking a deep rabbit hole: 
https://github.com/pmarreck/random

In order to make it work, I had to re-implement some math, so I avoided floating-point altogether (IEEE754 is a personal pet peeve) and went with mantissa and exponent fixed-point decimal. Or should I say binary, because the "decimal place" is the number of bits, not the number of base-10 decimal places.Apparently this is the only deterministic, cross-platform, cryptographically-secure procedural RNG that has many types of distributions (uniform (default), normal (Box-Muller), exponential, Poisson, log-normal, beta... all with configurable inputs AND which will plot the distribution for youin the terminal!) AND is guaranteed to give you the same values... Everywhere. (Because how the fuck has this not existed yet??) Implemented in both LuaJIT and Zig with C FFI. So there you go. MIT license. Enjoy your deterministic but still very random numbers, on every OS, identically.(It sources the best-in-class recommended source per OS if you want true random. It will do that too.)

reply

creature_x
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Building an AI agent that creates promotional content for social media, in a way that deeply resonates with your target audience. I tried using Claude and ChatGPT first, and they could give me a few good posts, but not a reliable stream of them. After 10–15 outputs, the angles converged, the language repeated, and everything became too salesy. I was still providing business context, finding angles, tracking previous posts.

It was clear to me that a marketing harness was needed around the LLMs for this purpose, and so Feral was born.https://feralhq.com

reply

Evidlo
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've rapidly been clearing some of the smaller items off of my ideas list while procrastinating on my PhD:

- nichromecast - TUI/CLI Chromecast sender with for local files and YouTube URLs -https://github.com/evidlo/nichromecast- syncthingtui - TUI for administering Syncthing on headless machines -https://github.com/Evidlo/syncthingtui- Need for Madness Web - WebGL port of an old Java racing/derby game -https://radicalarchive.github.io/nfm/- MdInvetory - Markdown-based personal inventory editor -https://github.com/evidlo/mdinventory

reply

eljonny
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

my own high speed train viewer (trainradar) that i use to further develop my software development skills. so far i'm happy with it and its performance, and it has forced me to learn how to scrape without being detected/banned

i'm using react on the front, pretty interesting how it manages states in the frontend and how to come up with new strategies to not trigger so manny re-renders of the UI, and on the back i use fastapi with postgresql and oauth2

reply

tjhill
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

lazyslurm is a tui for managing slurm jobs on HPC clusters. It's kind of like lazygit or lazydocker. I've been chipping away at it for the last few months. Its built in rust w/ ratatui.

https://github.com/hill/lazyslurm

reply

throwrioawfo
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Nothing. I get no satisfaction out of side projects nowadays

reply

entrep
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building 
https://fridayfika.com/

One week in.

reply

nbbaier
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

This is cool, what's the stack?

reply

rane
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

A new task manager to replace Taskwarrior

https://aven.raine.dev/

reply

g023
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

g023 Code - 
https://github.com/g023/g023code
 a deepseek v4 flash harness built specifically for that model, that uses Ollama for its vision support, and uses the built in web search capability natively. Created only in Python to keep it easy to implement and use. Made to achieve cache efficiency, and keep context tight.

reply

tziki
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

AI sense of humor benchmark: 
http://witbench.com/

reply

richardchilders
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm collecting ideas for my gnomes in Pakistan to work on while pretending to be deeply interested in yuppies' personal lives, lol

reply

lafalce
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on an open source project to make drone delivery accessible across any industry not only the software, but also the drone hardware

reply

selvan
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

An AI agent to convert camera roll shots into cinematic reels with narration + music. Each scene of the generated reel is editable by human.

reply

dainiusse
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on sauna & cold plunge app. 
https://sauna-assistant.com

reply

novren
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on agentic infrastructure for deploying very small production apps en masse.

In particular, I’m exploring what the infrastructure should look like when agents are the primary users: deployment, databases, domains, secrets, observability, and lifecycle management.The goal is that everybody and their pet can deploy an app.These units are called saasies, and the project is Saasie.

reply

zipotm
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Forex analysis software based on waves 
https://dxodus.com

reply

baist0
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm creating a trading bot. Сreating my own agent for a local LLM to help me write code.

reply

kml01
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I created 
https://tuktuk.coach
 to learn Thai for myself

reply

lappet
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Nice. Is it vibe coded? I am looking for a good resource for learning kannada if you know Tamil, but with a focus on spoken language.

reply

donpdonp
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

great looking website - the alphabet portion is fantastic.

I published a project this week to be a thai to english dictionary. Translation is easy to come by but I want a page to paste a paragraph of thai and have it break down every word. That helps me learn. The site uses Wiktionary data.https://thaikam.app/

reply

hatsix
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Some publishing for my kids, turn a pdf into a zine

https://zine-fold.com

reply

reconnecting
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

tirreno - security framework

https://www.tirreno.com

reply

dunster4
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a Web-based guessing game called „Guesstimate“ where the player needs to guess age, capacity and height of things.
Includes friends leaderboard and player‘s statistics:

https://guesstimate.offclock.dev/

reply

mikigraf
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Harness evals on private benchmarks. I haven’t found a good way to evaluate harness releases on realistic private tasks

reply

0gs
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

still trying to figure out how to find users for my offline model agent harness with self-customizability and an offline wikipedia reader/tracker. tell your friends if you can think of a meaningful audience profile. 
http://enough.support
 has details/links

reply

edimaudo
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Keep hearing that management sucks so building a tool that helps new and experienced manager improve and grow.

reply

SamarthaSR
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Got laid off in June. Grinding leetcode.

reply

amdahl
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

a new agent/harness, 
mu
. not ready yet but hope to let people play with it ~soon. its got very few novel ideas, but attempts to do the existing good ideas reasonably well and be as minimalist and composable and pragmatic as possible

https://miu.dev/

reply

phoenix24
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building a cicd + orchestration layer, and on-off hacking a 2d animation engine.

reply

earlyriser
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

https://woomarks.com/

It's a bookmarker tool.

reply

asok_
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I just released a small app called Fogpane:

https://asok.github.io/fog-website/index.html?lang=en

The concept is intentionally simple: you open a photo, it gets covered by a layer of fog, and you use your finger to wipe the fog away and reveal the image underneath – a bit like drawing on a fogged-up window.I’ve always wanted to publish something on the App Store, so I decided to use this as an experiment: how far can I get while letting AI write the entire app?For full transparency, essentially all of the code was written by AI. I guided it, described what I wanted, tested the results, reported bugs, and made product/design decisions, but I didn’t really write the implementation myself.For an app this small, I was surprised by how far this approach got me. It wasn’t completely hands-off – there was plenty of iteration, especially around making the fog and water droplets feel somewhat realistic – but it went from an idea to an actual app in the store.I’m a software developer myself, which made the experiment particularly interesting. In many cases I understood what the AI was doing, but deliberately tried not to take over and write the code myself.I installed Codex around three weeks ago. It’s hard to estimate exactly how much time I’ve spent on the app since then, but it’s probably been a couple dozen hours rather than hundreds.

reply

daviding
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

A few things outside of normal work that are deliberately different to be interesting to me:

- Ongoing work on an airline announcement engine that works with flight simulatorshttps://github.com/fearlessfrog/MSFS_Universal_Announcer- A multiplayer board game for Discourse forum users that is not the popular Risk (tm).https://github.com/fearlessfrog/discourse-not-riskBoth have a fair bit of traction, but is often the case, keen to do something new this month.

reply

theturtletalks
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

An open source, decentralized, interoperable marketplace backed by open-source SaaS for every vertical

reply

bovermyer
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a Python rewrite of Anacreon: Reconstruction 4021.

reply

ryan_lane
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

As a side project, I've been working on a RAG/MCP/agent service with workflows, for security: 
https://mappedsky.com/seizu/

This primarily builds on top of cartography (https://docs.cartography.dev/), which I'm a contributor to, which pulls infrastructure, SaaS, etc info into a Neo4j database, makes edges, and has a standardize ontology, so you can do attack path analysis, vulnerability assessment, inventory, etc.Seizu uses the RAG built by cartography, and adds reporting, graph exploration, automations and more on-top of it. It currently ships with a couple pre-made automations:* Automatic dependency vulnerability fixes, like dependabot, but uses codex/claude/opencode in a sandbox to do so, which ensures it doesn't just bump a version in the file, but actually assesses whether the changes in dependencies need code updates, and gives you a thorough overview on if changes aren't needed, and why changes were needed if so. If tests break, it also watches and fixes them automatically.
* A workflow to run the cartography sync, making it possible to split apart the stages, run portions of the sync on different schedules, in parallel, etc, while also making it possible to properly trigger downstream syncs, or other types of workflows.
* Generic AI agent workflow, which can be staged, run in parallel, or chained together via inputs/outputs, using Seizu's own custom agent (which has good LLM provider support, sandbox support with files, etc)Workflows are built on-top of temporal, allowing it to be quite flexible.

reply

kunaals
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Super cool, and thanks for your contributions to Cartography :)

reply

franze
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

update to my ai first desktop 
https://apps.apple.com/app/aifcc-ai-first-computer/id6782364...

reply

Mathnerd314
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A philosophical task manager, based on notable philosophers such as Baudrillard, Foucault, etc. It's been a fun game of reading these works, trying to distill their essence, and putting them through the LLMs to see what comes out. Currently it's not one task manager but rather many prototypes, and I'm trying to reconcile various design issues. In the same way that Marx's "philosophy" is essentially a "praxis" of political and economic power, which does not presuppose a "truth" but rather creates one, my task manager is a pragmatic tool for establishing the meaning of life.

reply

brynet
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Making rent as an open source developer.

Desperately trying to attract new monthly sponsors and people willing to buy me the occasional pizza with my terrible HTML skills. Is it working?If any individuals, companies (or bitcoin millionaires) would like to help a long-time OpenBSD slacker, unslack, I'd really like to focus more of my time on open source development (and advocacy), rather than making rent. Feel free to contact me.https://brynet.ca/wallofpizza.html(Native SegWit): bc1qwe6zv0ezq4gzlea6tw45qhsn5kckheljn0krvt

reply

ignoramous
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Do see: 
https://oss.fund/
 All the best!

reply

brynet
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks, but unfortunately I found nothing new there that's applicable in my case. Not looking for project grants or rigid commitment/goals based funding at this time.

reply

dchasson
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

My dotfiles.

Specifically, I'm working to stop working on them.

reply

nbbaier
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

Godspeed

reply

martythemaniak
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on an autonomous snow clearing robot: 
https://www.frost-e.com/

The basic idea is that instead of trying to solve the general case in robotics (ie, the humanoid companies - multiple tasks, multiple environments, generalization, etc) which needs billions of capital, can you efficiently deploy current tech to robustly do one task in one environment for cheap.

reply

c_hastings
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Cute idea! It doesn't snow here, so I don't know how the business of snow clearing works, but I would be curious if this could be used by an HOA for residential clearing too.

reply

suryansh1234
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on an AI search engine.

reply

bastawhiz
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

A search engine powered by ai? A search engine for ai? A search engine whose corpus covers data about ai?

reply

reverseblade2
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

3dpack.ing

reply

RAGcontent
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

wellbody.me - a simplified approach to body health. we condense a progression system into 3 daily actions to keep you focused on your goals.

reply

c_hastings
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

I assume you want feedback - onboarding for this was very long (the quiz) and it wasn't clear why I was answering these questions.

Yes, to build a radar graph. But why not be a beginner, working professional, and a parent? How do I pick only one thing that I do after 9 pm?Your onboarding is complicated when your app's premise is just do simple things, but halfway through onboarding, I've lost confidence in the path you are charting.

reply

c_hastings
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm on paternity leave and I've been returning to a host of LLM driven projects;

They are all for me, with a small interest in commercializing some of them as a hustle.Project: a local version of Claude Co-work for document organization, one of my original projects that I wanted from back in 2024, so it could help me find everything on my hard drive and turn it into a knowledge graph/mind map without sending everything over the cloud. Bonus for removing duplicates/disk cleanup.Project: Memoria - an SMS based daily journal - my first platform! security, interoperability, yay! This started out as something for my wife to make notes on the kids milestones with an SMS reminder, but then I have ADHD type memory issues and wanted a voice based journaling system so that I could just narrate about my day and have an AI clean it up. At the end of the week it makes a little email with photos, etc for a week in review. Next step is a big lift if I want to format everything to be put into "baby books" because of the print publishing workflows.Project: Curio - based on the platform above - helping to declutter based on capturing the sentiment of an object. My ADHD means that my memory is trigger based, and if you toss the thing, I lose the memory. I'm trying to find a way to get rid of things without losing my memory that comes from holding it in my hand.Project: Deep Signal - an AI driven daily podcast that gathers AI papers and news based on my interests, then transforms that into a 15 minutes daily news segment. Started out on Google's platform, now just using Kotoro and Gemma 4.Project: Book Explorer - like Sparknotes for non-fiction. Pushes everything into an ontology for non-fiction so that it can summarize it and make it very easy for me to "skim" books that I otherwise don't have time to read. Also helps me to deep dive into particular areas. This is probably one of my most frequently used tools.Project: Meeting Notes - Before Granola existed, this was a local granola clone that used whisper. Only later did I find that the real gap in making this work seamlessly without the janky MIDI Audio Capture was that if it was a "signed" app it got access to much better resources.Project: Hunch - a new type of trivia app that is based on bias and a "sense" of what is true. Made so we could play trivia across multiple education levels and generations with everyone still having fun. Still in development.Project: Drucker MCP - using an MCP to inject prompts from a custom "library" so that I could steer a big model towards as multiple opinionated experts. Meant for business / entrepreneurs - I want to think like Peter Drucker, Alex Osteralder, Rogers, Scott Anthony. This one is the one that I hope can "make a dent in the universe" because I could make it freely available as an MCP and it can help micro-entrepreneurs in the Global South.Project: personal finance app. keeping it local.I suppose to get the triple crown, I need to make a work out app so I have "journaling", "fitness", and "personal finance." Or could be a to-do app. lolHeck, most of these are still in development - but the Audio Capture was abandoned for freeware.

reply

kmstout
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Giving another round of attention to a CLI tool for handling RSS feeds. Over the years I've evolved several automated ingest flows, most of which are fed via RSS. For a long time, I used a setup based on rss2email, but it was baroque. Meanwhile, tools of a more standard design, like elfeed and newsboat, do not cater to my use cases. So, I wrote something that handles only feed management, fetching new items (i.e., <item> or <entry> elements), tagging, and searching the database. Other issues, such as download and storage of content, tagging policy, storage, and indexing are left entirely up to the scripts for which this is a building block.

reply

syndred
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a pet website, but I don't know why I can't comment or submit content here

reply

kimjune01
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

working on building a bench for human ICs for hiring

https://june.kim/human-signal

reply

jjordan
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm just about done with 
https://RSSVault.org
, a curated RSS feed directory.

Password is vaultearly644988 if you want to check it out.The companion app, a widget-first RSS headline viewer called Just The Headlines is just about done too. Site is online if you want to see screenshots:https://justtheheadlines.appI'm in the (required, sigh) closed test phase of Google Play Store approval. Drop me a line on X (https://x.com/JJordan) if you would like to join the test for that.Feedback is more than welcome.

reply

_menelaus
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Using AI to mass scrape the internet for family accounts of Hitler's escape, to prove he made it to Argentina. I started off very skeptical but now I think its 60-70%.

reply

usmanity
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

A slop detecting browser extension for LinkedIn because I have to use it these days to find a job, I was getting tired of seeing all the AI slop content.

reply

ingvay7
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Pls open source!!

reply

Jemm
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

RapidCAM.app is still taking up all my time. It is a 2.5D, parametric CAD/CAM program for CNC and laser with flat or 4th axis. Open source, free, run completely in browser.

This is a passion project that I want for my own use but am happy if other's find it useful and very open to feedback and collaboration.The file system is open and very well defined so that AI can write files. There is an AI Assistant dialog that helps you to write prompts and then takes the AI file and runs the file through a solver and checks.

reply

SMAAART
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on putting together a self-paced "Coding with AI" course for non-SWE(s).

Since I could not find anything out there, I am scratching my own itch.

reply

c_hastings
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

I'd love to see more - I've been thinking about this a lot as a way to go from from vibe to viable - look at NFRs, etc.

Do introductions of key concepts and explain what real scalability ladders look like and how to guide an AI to build it.I'd be interested to be a beta user when you get ready to share.

reply

bikeshaving
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

TermDOM: A terminal renderer which used real DOM nodes, so you can write TUIs like web apps with HTML, CSS, and whatever framework you want. I didn’t really write this, more like spent intense weeks of effort where I product manage (yell at) Claude and did visual testing.

https://github.com/bikeshaving/termdom

reply

zsoltkacsandi
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

A Golang web framework.

https://github.com/gofabrik/fabrikI’ve been waiting for a spine surgery and to do something with my time I started experimenting with an idea I had. It completely pulled me in, and helps me to distract myself.It is work in progress, lacks of documentation, I am not even sure I will release it.

reply

aprentic
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Mostly hardware.

A cheap rowing counter. Competitive rowers use a training device that counts their strokes per minute. I figured out that the major parts are really cheap, even as individual purchases, so I wanted to build a budget version. So far it counts strokes fairly accurately and I've just completed initial tests of the display.Drone experiment. I'm building a image recognition drone from scratch. It's based on a H743 Slim V4, with an RPI5 and a OAK-D Lite. I'm currently trying to figure out why the back left rotor is producing way too little thrust.Like everyone else, I'm also working on an agent harness. tl;dr I don't trust any agent to not be dumb, but the agents seem to have some success recognizing when the work of an other agent is dumb. In early tests, the back and forth seems to provide more stable and better results.

reply

atlasunshrugged
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

What does an image recognition drone mean? Like it recognizes other drones when it sees them?

reply

aprentic
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Sorry. I was trying to keep things brief.

Basically a drone that relies more on the camera and less on the accellerometer and the GPS. Although it still uses both a lot.

reply

atlasunshrugged
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Oh got it, neat!

reply

oulipo
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a repairable e-bike battery at 
https://infinite-battery.com

reply

mohamedkoubaa
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on goldy: 
https://github.com/koubaa/goldy

A new kind of GPU library written in rust with backends for CUDA, DX12, Vulkan, and Metal (tenstorrent and wgpu are planned) and bindings for rust-dynamic, python, c++, c, and dotnet (Java and Fortran are planned).Uses the slang shader language exclusively. All submissions are expressed as graphs (like cuda graphs), are retained automatically (sometimes partially with a graph partition algorithm), and automatic synchronization of GPU resources. No runtime dependencies (slang is vendored) and new calling convention for shaders using a virtual entry point that allows resources to appear as arguments to the shader 'main'. Includes automatic VRAM and resource recycling for device resources.Shader coroutines, rust shader authoring, and automatic kernel fusion are planned.Supports both GPGPU and graphics.Made it because cross backend GPU libraries usually either target lowest common denominator or are specialized for either compute or graphics or ML. In my experience GPU programs and frameworks are written to target a different kind of machine than a tape machine, but nobody outside of tenstorrent have bothered to describe that machine. So I defined a new kind of abstract machine for cooperative resource-oriented computation called a Fondaco machine for which goldy is the reference implementation.

reply

c_hastings
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

But why? (not meant to be rude). why would I want to use this gpu library versus what is out there already? I don't understand the value of it.

reply

bitwize
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

My games, and cleaning up my ext3/4 journalling code for the NetBSD kernel. I've got it opening, reading, and replaying the journal upon mount, now I need to move on to getting it to actually log disk transactions during use.

reply

macinjosh
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I make a podcast client for iOS that detects and skips ads for you using an on device model. This allows me to sell without a subscription. I am working on v2 which will bring support for video podcasts and YouTube podcasts.

reply

jdw64
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a language with AI as a personal project. My hobby is tinkering with my homepage [1], and for paid work, I'm handling a project related to autonomous drones

[1]https://www.makonea.com/en-US

reply

mannanj
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Sun signal. You can time your life events with the sun: think optimize work time, sleep time, rest time by following sunrise, solar noon and sunset.

It was my counter cultural bet to burn out and AI vibe coding all night long. Has worked pretty well.https://sunsignal.app

reply

ksaun
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've continued working on my game project, Vestiges, which is a 2D narrative strategy rogue-like in Godot.

I'd hoped for a more meaningful update from when I first mentioned Vestiges last month (https://news.ycombinator.com/item?id=48884984). But I've often felt discouraged and haven't worked as much as I'd intended.As was recommended by guiambros last month, I started the process of setting up Vestiges on Steam, but that's still in progress (currently, my identity is being verified). I also set-up at micro.blog (https://ksaun.micro.blog/) and (https://mastodon.social/@ksaun), but haven't posted anything yet.I bought a Linux laptop for this project (I was working on a 2020 Surface Book 3). (I had used Unix in the 1990s, but not much since then. The video game industry being so Windows-centric, I'd stuck with that OS throughout my career.) So recently I spent a few days enjoying (not sarcastically!) setting up my new computer and work environment. In doing so, I also took improved some aspects of my development process.Limited meaningful work on the game itself. From a technical perspective, I could release the demo now, but I'm dissatisfied with the content (specifically the writing). Not that it needs to be amazing just yet, but I want it at least less embarrassing. As I've worked with some of the best game writers in the industry (in my opinion; people like Chris Avellone, George Ziets, Neal Hallford, Brian Mitsoda), I'm accustomed to quality that exceeds my personal ability. And this writing work requires greater focus than I can usually muster, so I've been procrastinating, polishing other things that were already sufficient to ship.Since last time, I've finished most work on tutorial features and content as well as the other implementations I wanted for the demo. For the modes that are ready, I added full support for keyboard-only play (which was a more substantial effort than I'd anticipated, taking close to two days (very part-time for me, but Claude was fairly busy)). I also now have an MCP server implemented so that Claude can playtest as a player would, but I've only just started to make use of it. (And some progress on the aforementioned writing, just not much.)

reply

eclipxe
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Software Factory. MIT licensed. runfusion.ai

reply

tjwebbnorfolk
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I put together a nationwide (US) land parcel dataset over the past year and a half, and have been building a bunch of apps on top of this data: 
https://landstats.com

reply

nephihaha
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a guidebook. Not putting it online to get scraped!

reply

QuantumNoodle
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

My health

reply

Goharik
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Avarand, a classic WoW like mmorpg

reply

roschdal
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Northstar web browser :)

https://github.com/nordstjernen-web/northstar-browser

reply

Forgeties79
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

My home media server! I’m so rookie compared to many of you, but proud of what I’ve got. We’ve (family) been on it with no paid streaming for 18mo now but it really became turnkey/low
Maintenance a few months ago.

Still on plex, next step is Jellyfin.

reply

helge9210
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Olympic wrestling education tool.

Indexing multiple captured video streams with awarded action points and adding athlete/referee positions overlay. Stretch goal -- controlling PTZ camera for predictive capture of the high intensity actions.

reply

shevy-java
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I am not really working on anything new as such, but I am mostly
just polishing existing workflows. For instance, the task for
today will be to use mechanize (in ruby) to automatically tap
into a webservice which I use manually right now via a browser
interface. I want to do this all from the commandline next.
(Ideally I'd not want to depend on this and do it locally, but
it does various things with .pdf files which I have not yet
been able to do myself. ghostscript is surprisingly awful, 
and while there may be alternatives, I am not too familiar
with all of what they can do, whereas the webservice really
has all pdf-related tasks already solved, as-is, including
optimising for size. For some reason ghostscript produces
much worse results, from A to Z.)

Nothing too interesting though.I have more interesting projects, but these have to come after
I focus on more pressing reallife requirements; on my next
todo list, though, I want to extend the code I use to compile
from source. I track almost 4000 programs already and can 
compile most of these (for some reason GCC 16.2.0 does not
want to compile today); I want to extend this, finishing 
an automatic build of the linux kernel and full bootstrap
into a new system while also adding more language bindings,
such as lua. And also allow for this to be compilable via
a web-interface.)

reply

moralestapia
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

https://httpstate.com
 // a super easy to use, batteries included, library and server to exchange small bits of data between apps

https://wafertown.com// the first LLMORPG, you write a prompt and your character "lives" through a simulation of life using it as a guide, interacts with others, etc. sends you a summary of what it did and allows you to steer it for next day. think of it as a small tamagotchi but with hundreds (hopefully thousands!) of other players

reply

nbbaier
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

> 
https://httpstate.com
 // a super easy, batteries included, library and server to exchange small bits of data between apps

This is very cool! What's the stack for the actual server?

reply

moralestapia
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks!

Right now it is Node.js and I store data in an in-memory database.(I keep no history, state is volatile, I think that of being a feature :)).There's some work on the roadmap to "standardize" the API spec. and publish servers for most common stacks: Docker (agnostic), Go, node.js and Python.

reply

Beefin
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

rust based agent orchestration tool that works offline

https://github.com/mixpeek/amux

reply

analog8374
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

a lightweight portable foldable seiza bench. yes I know there are such but none are good. mine is good

reply

newbie578
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a discussion board for HN’s Who is hiring.

Too many times I have been burned by applying to scam listings or people who are just to self-promote and use people who want a job as a marketing channel (looking at you BetterStack, fu in particular).I want people to be able to discuss and flag companies which are lying or just a waste of time, yet HN refuses to do anything about it and doesn’t allow threads as discussions and removes comments.Hit me up if you want on the beta testers lists, already got a couple of people.rocket.dev22@gmail.com

reply

Giorgi
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building very high yield ETFs directory, like... Ponzi-scheme-alike levels of dividends, and I am collecting each and single RoC to actually know if they generate any income or do they simply pay your money back, I still have long road to go, but it is coming along.

https://thedividendetf.com/

reply

donpdonp
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

"How much of each payout was your own money handed back." very interesting premise but the site needs more explanation of what that means and how it computes those numbers.

reply

Giorgi
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Agreed. Right now I am writing parsing part though, since how they issue RoC is not standardized (they are required by law but format and how they do it is not a standard).

reply

Razengan
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

About 100 games and still yet to finish 1..

..but I get to take the common stuff from each and put it into an open-source Godot framework so as to not feel totally useless :')https://github.com/InvadingOctopus/comedotand all of this is making me want for a better programming language designed from the ground up for games, with no need to care about hardware, so I've been brainstorming and rubber-duckying about that as well.

reply

mgranados
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

a to-do list app, lol

reply

relug
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

thats super cool! are you using htmx as your web framework? i recently started uSiNgg HtmX

reply

jwarykowski
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Me and you both!

reply

w92178792789
 
16 hours ago
 
 | 
prev
 
[–]

100010101010100010001001010100101010011010100100101010010101001010101001010101001001010011010010101001010010101010100100101010010101001001001010101010101010101001010101010100101010101010101001010101010010101010101001010101010101001010101001001001010010101000101010101010

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