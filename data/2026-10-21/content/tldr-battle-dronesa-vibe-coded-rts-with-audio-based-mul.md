---
title: Battle Drones—a vibe coded RTS with audio-based multiplayer
url: https://simonwillison.net/2026/Oct/20/battledrones
site_name: tldr
content_file: tldr-battle-dronesa-vibe-coded-rts-with-audio-based-mul
fetched_at: '2026-10-21T11:11:18.580586'
original_url: https://simonwillison.net/2026/Oct/20/battledrones
author: Simon Willison
date: '2026-10-21'
description: Battle Drones - a vibe coded RTS with audio-based multiplayer
tags:
- tldr
---

# Simon Willison’s Weblog

Newsletter

Sponsored by:
 
Teleport
 — AI agents (and sub-agents they spawn) are given the same access as humans, but they never sleep. Learn how to monitor and constrain their behavior with isolated ephemeral trusted runtimes.
 

## Battle Drones—a vibe coded RTS with audio-based multiplayer

20th October 2026

My latest vibe coded game experiment is a Command & Conquer style RTS (Real Time Strategy) game calledBattle Drones(play it here). Unlikemy previous experiments, this one isactually fun to play. I’m somewhat embarrassed to admit that I got there by telling Claude to “Make it a LOT more fun”. It also supports multiplayer between nearby devices using audio to synchronize game state! Here’s what I’ve built so far, and some of the things I learned along the way.

* Battle Drones
* How I built this
* v1: the initial prototype
* v2: full sprites
* v3: varied terrain
* v4: the fun update
* v5: Battle Drones goes 3D
* v8: Archipelago
* v10: Goliath, and agent battles
* Agent battles
* v11: Random Maps
* v12: Multiplayer via sound
* Some thoughts
* Update: Online multiplayer support

#### Battle Drones

My initial goal was to build an RTS game I could play on my phone, in the style ofCommand & Conquer. I have fond memories of the 1995 original (I liked Red Alert too) and wanted to recapture a little bit of the magic.

After 12 major iterations (and321 commitsby coding agents, mainly Claude Code) I now have a browser-based game that works on mobile and desktop, has multiple play modes, several maps (including a random map generator) and even supports multiplayer for two devices within microphone range of each other.

Here’s a video demo of Battle Drones running in a desktop browser:

 

Features so far include:

* 9 buildings, 7 ground vehicles, 6 aerial vehicles, 3 infantry units—all 3D models, which you canbrowse here
* Fog of war
* Different weapons are needed to target aerial or ground vehicles
* Six maps, across five biomes—temperate, desert, arctic, volcanic, tropical
* A random map generator
* Skirmish mode—red vs. blue on a rotationally symmetrical map
* Last Stand mode—one player holds out against as many waves of enemies as possible
* Area effect weapons: Barrage, EMP, Drop Pod, Sky Hammer
* Crate dropswith bonus resources
* In-game music that responds to events—it gets more intense as fighting breaks out
* Different in-gameAI personalities(Balanced, Rush, Air Swarm, Boom, Skyforce, Ironclad)
* AI vs. AImode, to watch those personalities play each other
* TheGoliath—a giant stomping mech with laser eyes and arm cannons and the ability to establish a new base
* Mutatorsthat add extra rules or twists
* A “Daily Op” challenge
* Ranks and achievements (Medals)
* Agent vs. Agentmode where two LLMs can play Battle Drones against each other
* Amultiplayer modebased on two nearby phones communicating via audio messages, an extension of my earlier experiment withChirp Pong

#### How I built this

Battle Drones is heavily vibe coded—I’ve reviewed almost none of the code, and it’s built in a language (TypeScript) that I’ve hardly used myself. I’ve playtested it quite a bit though, and it’s been through a large number of iterations since I started the project.

Here’s a rough history of the project so far, including key prompts and links to transcripts.

#### v1: the initial prototype

I started out with Claude Fable 5 back in July:

We are going to build a mobile friendly RTS game - command and conquer style - called Battle Drones, in which two armies of drones (both flying and ground-based) battle for territory and resources

Let's start with a MVP design, ask me some questions

Here’s ashared transcript. I’d given Claude Code for Web an environment variable with an OpenAI API key and told it to use the OpenAIImage Generation APIfor assets, which got me some basic sprites.

You cantry v1 here—it looked like this:

It’s recognizable as an RTS, has building mechanics and the ability to select and direct units, and a basic AI to play against.

This first version was barely a proof of concept, and it wasn’t any fun to play.

Claude used thePhaser2D game framework for these early versions. I didn’t even realize this until several iterations later!

#### v2: full sprites

The second version (try v2 here) added sprites for all of the vehicles and the “AI vs. AI” mode, so I could watch the game playing without having to directly control it myself.

Claude proved reasonably competent at prompting OpenAI’s image models to generate sprites. You can browse the v2 sprites in thepublic/assets/spritesfolder.

#### v3: varied terrain

It still wasn’t much fun, and the graphics were boring. It was now October, and I had upgraded to Claude Opus 5.5. I told it:

Massively improve this game. Make the graphics and gameplay better (keep it mobile friendly). Render new graphics using the latest OpenAI GPT image API (lookup details) with the API key in the environment variable. Add new unit types and balance the gameplay better. Also add new buildings and better, more varied terrain.

This resulted in five new maps with generated background tiles in a variety of styles,visible here. Opus also regenerated the sprites, making them much more visually appealing. You cantry v3 here—it looks like this:

This is starting to feel like a real game! It still wasn’t very fun to play though—I found myself getting bored pretty quickly.

#### v4: the fun update

So far my Battle Drones experiment was confirming myprevious beliefthat coding agents can build a thing that looks like a game but can’t actually make something that’s genuinely compelling to play.

I shared this theory with someone over dinner, and then thought to myself that I should give the models a proper chance to prove me wrong. I prompted Opus 5.5 on my phone:

This game isn't fun enough yet. Make it a LOT more fun.

This time I was running inUltracode mode, where Claude Code (in this case Claude Code for Web) runs “dynamic workflows”, described in their docs as:

A dynamic workflow is a JavaScript script that orchestrates manysubagentsat once.

This kicked offmany hoursof work. I started it in the evening and didn’t get a playable result back until late into the next morning. But the results were spectacular.

You cantry v4 here—it looks like this:

I had Claudewrite its own release notes—here are the highlights:

Every skirmish and Daily Op now opens with a choice, gives the side that’s losing a way back, and pulls the armies into the middle of the map. There are also two new ways to play.

* Openers: pick Blitz, Industry or Air Wing before the clock starts.
* Call-down powers: Barrage, EMP, Drop Pod and the Sky Hammer orbital strike.
* Objectives and salvage: Uplink relays, supply drops and wrecks worth scrap.
* Feel: combat juice, adaptive music, unit voices and an announcer.
* Command: battle alerts, game speed, saved squads and touch placement.
* New modes: Last Stand survival waves and an 8-mission Ops campaign.
* Progression: heroes, an after-action report with awards, a career, 7 mutators and a Daily Op.

Fights run longer and swing more. In 1,200 AI-vs-AI test matches on Normal, games still undecided after 25 minutes fell from 14% to 0.9%. The share of wins by a side that had been 800+ scrap behind rose from 24% to 46%.

Part of the reason Claude took so long was that it ran over a thousand simulated playtest sessions, and used the results to rebalance the existing units, add new ones, and introduce new features.

#### v5: Battle Drones goes 3D

After the success of Ultracode at “Make it a LOT more fun”, I decided to be more ambitious:

Port this game to three.js with 3D models for all of the buildings and vehicles and landscapes

That was another overnight run. I woke up tothis v5 version:

The new 3D models were entirely constructed by Claude in TypeScript code.

v6 (play v6 here) added some more visual polish. v7 (play v7) added robot infantry (troopers, rocket squads, snipers) and a “Condor” troop carrying aircraft.

#### v8: Archipelago

I was beginning to feel guilty at how little actual design input I had into the game—it really had been a case of me saying “make it more fun” and “add visual polish” for the past few releases.

I’d noticed that the AI didn’t use the new infantry and troop carrying aircraft from v7 very often—there wasn’t a great strategic reason to use them.

It would be neat if we had a new map with a new game mechanic that actively encouraged players to load up Condors with infantry robots and send them out into the map.

This resulted in my longest prompt yet:

Design a new map. Goal is to make different strategic incentives that encourage use of Infantry and Condors and aerial vehicles.

To do this the map will have limited harvester resources but several more uplinks - but uplinks will be on islands that are inaccessible by land vehicles or infantry. These uplinks can also not be claimed using air vehicles. The ONLY way to get them is to fly infantry there in a Condor.

Armies always start with a Condor and a single squad. If an army has no Condor a new one will be provided for free, flying in from the edge closest to their HQ and landing there. That free condor will come with a single free squad on board.

The two HQs should be entirely separated by water, but still accessible by vehicles thanks to two bridges across the map in different places

I want to encourage a battle over uplinks.

The map should be the times the size of other maps - still square

First research and then critique this design. Only build after we have agreed on any modifications

You get to design a new biome for this

The result was the tropicalArchipelagomap, with seven island uplinks that players can only capture by flying out infantry in a Condor. It’s definitely the most fun map to play, once you’ve got the hang of the basic game mechanics from the simpler maps. Thev9 editionmade that map a little more interesting—it now looks like this:

#### v10: Goliath, and agent battles

I decided to add giant robot mechs to the game—think Jaegers fromPacific Rim, or Titans from Warhammer 40,000.

Here are some of the prompts I used to brainstorm with Claude:

Help me brainstorm ideas for adding giant robots to this game - think dreadnoughts or titans from W20K - how could we do this in a way that enhanced gameplay, kept things balanced, added unique twist? Don't overthink this yet

Let's keep brainstorming. I like the idea that it's a mobile base - that can accept harvested scrap and can have buildings built near it (even if it later moves on) and can produce infantry units too. An interaction with condor would be neat but I don't know what that could be.

Idea: as it gets damage it loses the ability to fire some weapons - by default it has eye laser (like lancers) and arm canons (like titan) and two shoulder mounted mortars, plus machine guns similar to a squad of troops

Damage knocks out mortars and then laser - it always has guns. You can't build next to a building that was only put there because of the mech, you need the mech there for off-base building and only within three squares of it

[...] Lets do two condors can carry the mech

The end result isreally cool.

 Your browser does not support HTML video.

Goliaths can be constructed using a Gantry—a building that can only be created after first building a Fab, Bay, Airpad, and Tech Lab. You can see the Goliath under construction, and it then walks out from the Gantry and can march around the map.

Goliaths can “anchor”, which digs them into the ground. In their anchored state they can act as a new HQ, constructing infantry units and additional buildings in a new area.

Two Condor aircraft can hook onto a Goliath, at which point it can be flown around the map!

The game now ends when you destroy the enemy’s HQ buildingandany Goliaths they might have built.

There are also a couple of mutators relating to Goliaths:

* Goliath Armadastarts each side with four airborne Goliaths (each with a pair of Condors) and no other units.
* Robot Loveadds a special rule: if enemy Goliaths get close to each other on the battlefield they fall in love and the game ends in a draw. (Thank Natalie for that one).

#### Agent battles

The other v10 feature isagent battles. In musing about how multiplayer could work I had an idea: what if different LLMs could fight it out in the game?

Fun extra challenge: think about how we might make multiplayer available to coding agents. It would be neat if we could set up a battle between eg GPT-6 Sol and Claude Opus 5.5 where each model has access to a tool which gives them information about the game (presumably non-visual, but only the information they could see through fog of war etc) and lets them control their units etc [...]

Consult ~/dev/llm/docs and include notes in that file about how LLM could be used here via a new tools plugin

Opus 5.5 went to work on this, producingthis AGENT-BATTLES.md proposaland then implementing and testing it. The feature also includes the ability to record and replay these battles—here’sa replay of Claude Haiku 5.5 vs. GPT-6 Luna, and here’s that same battlein a separate debug toolthat shows the underlying prompt responses.

The prompt that drives agent battlescan be seen here.

There are a few more replays like thislinked in the README. I hope to turn this into a full league table at some point in the future.

#### v11: Random Maps

This version exists purely because I glanced at myClaude Usagepage one day and saw that I’d only used 75% of my weekly allowance and it was resetting in 45 minutes. I decided to see if I could get an extra Battle Drones feature from my remaining tokens, and picked “random map” as the target:

Design and implement a mechanism for generating a random map using any of the available biomes - it should be the size of the largest map and rivers and bridges and rocks and forest and scrap and crystals are all in play. Make them rotationally symmetric and use a seed to allow them to be selected or reused later. You have 45 minutes to build this! Be creative.

Here’sthe transcript, and an image Claude generated to show me its work:

#### v12: Multiplayer via sound

I onlyjustgot this working, so I’ve not had much time to actively test it yet. The latest Battle Drones now supports multiplayer via two devices sat within microphone distance of each other!

This feature started out as myChirp Pongexperiment from last week. I pointed Claude Code at that working proof of concept:

Clone Simonw/tools from GitHub and look at recent branches for the example pong game that uses web microphone to implement multiplayer between two phones via audio signals

Build a version of that for battledrones

Opus builtthis Radio Probe toolto measure how much bandwidth we could get between two devices and, based on positive results from that, implemented a full audio modem system. I’ve tried it between laptops, iPhones and iPads so far and it seems to work really well!

Why use sound for this? Because Ilove static HTMLthat costs nothing to run, and I don’t want to spin up a server somewhere and then stay responsible for keeping it operating for as long as anyone might want to play the game.

#### Some thoughts

I know almostnothingabout game development. This makes it a great opportunity to try out coding agents in a field where my existing software engineering experience has less impact on the results.

Games are also super low stakes. The worst that can happen is one of my silly game experiments suffers a bug.

This morning (via Hacker News) I foundSteam Fans Are Begging for a No-AI Filter as Steam Next Fest Is Filled With Slop. I wouldn’t personally dream of submitting Battle Drones to an event like this—it’s still way too low effort to warrant consideration as a legitimate indie gaming project.

... but I can now see a path to vibe coded games like this being taken seriously. Battle Drones is fun, it looks good, it has innovative features (the multiplayer-over-audio thing is a first for an RTS as far as I can tell).

I’d love to see what someone with better taste than me and a driving passion to produce something truly exceptional could build!

A few other observations from this project:

* Static HTML and JavaScript is a fantastic medium for games development. WebGL works great, andThree.js(andPhaserbefore it) are excellent platforms to build on that the current models know inside out.
* This also lets them run asProgressive Web Apps—I didn’t ask for it, but Battle Drones works offline. I was able to play it on a plane despite never having directly installed it—my phone had it cached.
* Giving Claude an OpenAI API key and telling it to generate images using OpenAI’s models works really well. It can view the images it has generated and iterate on the prompts.
* Opus 5.5 is spectacular at 3D modeling using Three.js (and Blender, and no doubt other 3D applications as well). Thesame is trueof GPT-6 Astra. They are absolutely capable of building models for 3D game projects.
* For features like replay and multiplayer it’s useful to have a deterministic simulation engine. At one point Claude had to replace calls toMath.sin()andMath.cos()and friends withcustom versionsbecause different browsers (Chrome vs. Safari, for example) returned very slightly different numbers, desynchronizing the replay.
* Opus 5.5 can write music! There are no audio files in this project—the soundtrack is entirely generated through code, varies across different maps, and even gets more intense as the battle heats up. SeeScrimshaw Jukeboxfor a previous experiment with Claude for music composition.
* I still can’t get over how well the prompt “Make it a LOT more fun” worked.
* Tools are effectively free. I prompted up theRadio Probe, theModel browser, theAgent vs. Agent debug tool, and Claude Codebuilt a bunch of toolsfor itself that I haven’t even explored myself.
* Audio-based multiplayer between static HTML games works! I hope to see a whole lot more games use this same pattern—in digging around today I’ve not found much prior art beyondSinerby Alon Horesh andggwaveby Georgi Gerganov (also ofllama.cppfame).
* Claude Code “Ultracode” burns tokens like there’s no tomorrow, but it can also solve complex problems (like adding audio-based multiplayer) from a single prompt.
* I’m still not quite over theguiltof building software in this way. I don’t feel like I’ve earned the right to create something this good, in a field in which I have so little prior experience! At this point I’ve shown it to enough people in private that it felt wrong not to publish it for everyone else to see and learn from.

#### Update: Online multiplayer support

Earlier in this article I said:

Games are also super low stakes. The worst that can happen is one of my silly game experiments suffers a bug.

Then I tried playing the multiplayer version with Natalie... and the high pitched modem sounds gave her a nasty headache!

That’s a pretty bad bug. Iadded a warningand was then inspired to build proper network multiplayer. I triedgetting WebRTC to workbut couldn’t get a connection going between two of my own devices even on my own WiFi network, soI had Claude builda simple, stateless WebSockets relay server instead:

If I wanted to support multiplayer between two devices at a very low cost without storing any state on the server could I do that with a tiny asyncio web server running on the cheapest Fly instance?

Build the server and the fly.toml for deploying it, use Fly application name battledrones-relay - put that in a folder in the repo, include deploy instructions in the README in that folder

Here’sthe resulting server. Since this scales to zero and runs on a singleFly.ioshared-cpu-1xinstance it should cost me no more than $2.19/month—and that’s if it stays hot and serving connections the whole time.

Battle Drones now supports online multiplayer. Click “Duel a friend online”, then either share the resulting room URL via your messaging app of choice or have them snap a picture of the displayed QR Code.

I also added a feature where you can copy JSON of the match once it has ended and then feed that into the replay feature to rewatch your game.

I didn’t expect to introduce online multiplayer this soon, but the headache bug felt like it warranted an urgent alternative.

Posted 
20th October 2026
 at 7:34 pm · Follow me on 
Mastodon
, 
Bluesky
, 
Twitter
 or 
subscribe to my newsletter

## More recent articles

* Hello Python 3.15, goodbye 3.10, and now I can use 3.11- 12th October 2026
* A new feature for my blog, built using my voice- 9th October 2026
* Claude Haiku 5.5- 7th October 2026
* We're going to need default hard budget caps on pretty much everything- 3rd October 2026

 

This isBattle Drones—a vibe coded RTS with audio-based multiplayerby Simon Willison, posted on20th October 2026.

Part of seriesHow I use LLMs and ChatGPT

1. Vibe coding SwiftUI apps is a lot of fun- March 27, 2026, 8:59 p.m.
2. Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code- June 22, 2026, 11:43 p.m.
3. A new feature for my blog, built using my voice- Oct. 9, 2026, 12:54 p.m.
4. Battle Drones - a vibe coded RTS with audio-based multiplayer- Oct. 20, 2026, 7:34 p.m.

 game-design
 
26

 projects
 
560

 ai
 
2,287

 generative-ai
 
2,029

 llms
 
1,995

 claude
 
320

 vibe-coding
 
102

 coding-agents
 
261

 claude-code
 
132

Previous:Hello Python 3.15, goodbye 3.10, and now I can use 3.11

### Monthly briefing

Sponsor me for$10/monthand get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

 Sponsor & subscribe
 

 

 

* Disclosures
* Colophon
* ©
* 2002
* 2003
* 2004
* 2005
* 2006
* 2007
* 2008
* 2009
* 2010
* 2011
* 2012
* 2013
* 2014
* 2015
* 2016
* 2017
* 2018
* 2019
* 2020
* 2021
* 2022
* 2023
* 2024
* 2025
* 2026