---
title: 'Interview: How ReXGlue is bringing the Xbox 360 into the static recompilation era'
url: https://readonlymemo.com/rexglue-xbox-360-recompilation-interview/
site_name: hnrss
content_file: hnrss-interview-how-rexglue-is-bringing-the-xbox-360-int
fetched_at: '2026-04-04T01:03:00.429011'
original_url: https://readonlymemo.com/rexglue-xbox-360-recompilation-interview/
date: '2026-03-29'
published_date: '2026-03-29T11:00:03.000Z'
description: 'Plus: A launcher for recompilations and a new PS1 fan translation.'
tags:
- hackernews
- hnrss
---

# Interview: How ReXGlue is bringing the Xbox 360 into the static recompilation era

Plus: A launcher for recompilations and a new PS1 fan translation.

				by
				
Wes Fenlon

March 29, 2026 — 15 min read

 

Hello hello hello! In this week-late-but-worth-the-wait edition ofROM, I'm back to my old hijinks with a meaty interview for one of the most exciting open source projects on the scene right now: ReXGlue, the Xbox 360 recompilation tool.

You may have seen some videos of early days PC ports for 360 games floating around in the last couple months. Those are indeed thanks to ReXGlue, and I've got a whole buncha words from the toolkit's creator to get you up to speed on how it works and what it's currently capable of. No, you can't properly play Lost Oddysey on your PC just yet, but are you going to be able to at some point?Hell yeah.

One point of confusion about ReXGlue I've seen floating around is whether it's essentially "just" emulation because a good chunk of its codebase is based on the Xbox 360 emulator Xenia. I bet you'd be able to guess that the real answer is a whole lot more complex than that assumption.

Over in the world of hardware emulation, I've had just a little bit of free time in the last week to dedicate to the beta of Taki Udon's "Console Mode" UI for the MiSTer, testing it out on theSuperStation One. The software isn't available for everyone to use yet, and there are still some rough edges as you'd anticipate from a beta. But expect me to be writing impressions of it as soon as it's kosher to do so.

That's going to do it for a speedy intro this week, as I've got a date with the excellentShadow of the Ninja - Rebornto get to. If you see me wincing next time I sit down in public, assume it's because my ass is still sore from this game mercilessly kicking it.

💸
If you enjoy 
ROM
, I'd love it if you'd consider 
a small tip
 to help me cover my monthly costs. (Follow the link and click 'change amount' to whatever you want).

## The Big Two

### 1. Getting into the sticky details with ReXGlue creator Tom

Last year, something caught the eye of programmer Tom, a longtime Xbox 360 fan:Sonic Unleashed Recompiled. The blue hedgehog going faster on PC than he ever had in the game's original console version sparked his interest in static recompilation, a promising technique also being used withN64 Recompiledto translate game code from its original platform to run natively on the PC. As impressive as the Unleashed project was, he could tell that much of the work that went into it was tailored to that specific game. What if he could go bigger?

"Around that time, someone reached out to me about a community working on the Fable 2 Recomp," says Tom. "That's where I came into contact with a great group of people who shared similar goals and aspirations. Loreaxe (Ryan Fisher) was the owner of that Discord server and became my biggest supporter during the early days of getting the project off the ground.

"I was experimenting with how we could build something that provides the foundational pieces for an emulated backend while also giving developers the ability to implement native rendering, audio, and other subsystems. That is really where static recompilation shines."

That's howReXGluewas born. In the few months since its reveal, a host of recompilation ports have popped up in early development using the tools that Tom and other contributors have been working on. It's a list that, unsurprisingly, contains quite a few games that never made it off the Xbox 360 as well as some other favorites:

* Blue Dragon
* Lost Odyssey
* Banjo Kazooie: Nuts & Bolts
* Ninja Gaiden 2
* Halo 3's beta
* Crackdown 2
* Viva Pinata

While Tom keeps a fairly low profile, he says he's been dipping into the Xbox 360 emulation and modding scene for essentially as long as it's been around. He did some modding for Source Engine games back in the day, but his professional background in systems & platform engineering gave him the right experience to build a bigger project like ReXGlue. As the Github page cautions, the proejct remains "in early development" and it's not yet time to get psyched about playing pristine, perfect PC ports of the games above. But what ReXGlue's current statedoesgive us is a great opportunity for insight into how recompilation works for a platform as complex as the Xbox 360.

Tom makes no secret that ReXGlue is heavily based on the work of the Xbox 360 emulator Xenia, Unleashed Recompiled, as well asXenonRecomp, a tool for converting the 360 game code to native C++. But getting a game running on PC is hardly as simple as slapping those three things together and calling it a day.

"As the project matured, we made the decision to adopt Xenia's codebase wholesale and replace its JIT backend with AOT (ahead-of-time) mechanics, similar in concept to what parts of the Unleashed Recomp did, but packaged as a consumable and extensible SDK," he says. "That distinction matters: ReXGlue is not meant solely as an emulator. It's a platform. Static recompilation opens the door for things that are extremely difficult or outright impossible to achieve in the realm of JIT emulation. Things like deep modding support, native subsystem replacements, and platform-specific optimizations that just aren't feasible when you're translating instructions on the fly."

I asked Tom for a breakdown of how ReXGlue's approach differs from N64 Recompiled, given the dramatically more complex console hardware.

"The hardware is very different, but the core concept of static recompilation remains the same and that's really the beauty of it," he says. "Static recompilation is universally applicable because the fundamental idea maps directly to how any CPU processes instructions: you're taking the original machine code, analyzing it, and producing equivalent code for a different target architecture. The specifics of the instruction set change, but the methodology doesn't.

"Where it really shines is in what comes after the translation. Once you have native code for the host platform, you get all the benefits of modern compiler optimizations that the original hardware never had access to. The result is code that can run not just correctly, but often more efficiently than the original."

Indeed, you can see that even in the very early versions of ReBlue, the Blue Dragon recompilation Tom is working on himself. He calls it "the pilot title for most of my mad scientist experiments," like getting multi-disc games to work seamlessly. Even in nascent form the framerate is already much better than it is on console, echoing the performance advantage inherent to running code for these decades-old games natively on PC.

The fact that ReXGlue uses pieces of the Xenia emulator, though, can be hard to understand for those of us who aren't wizened programmers. Is this recompilation or emulation? What's the point of all this work if an emulator already exists? Those questions are the crux of what makes ReXGlue special, and the nuance is in what it can doright nowvs. what it will eventually be capable of.

Tom explains in detail:

"That's a question I see come up a lot, and I'll be honest, it's a frustrating one because it usually comes from people who haven't looked at what we've actually built. The short answer is: yes, it is absolutely a recompilation. The game's CPU code, every PowerPC instruction in the original binary, is converted to native C++ ahead of time through our codegen pipeline and compiled with Clang. There is no JIT. There is no instruction interpretation at runtime. When the game runs, it is executing native host code that was produced offline by the recompiler. That is static recompilation by definition.
The confusion comes from the GPU side, and I understand why. Right now, we use Xenia's Xenos GPU backend for graphics. But the GPU is not the game. The game logic, the physics, the AI, the scripting, the kernel interactions, all of that is statically recompiled native code. The GPU backend is a rendering service that the recompiled code talks to, the same way a PC game talks to DirectX or Vulkan. Nobody would say a PC port "isn't real" because it uses a graphics API. The GPU backend is a subsystem, and it's one we fully intend to replace with native rendering over time. In fact, the entire graphics system is an abstract interface in the SDK. It's injected at build time, not baked into the recompiled output. That's by design.
What people also tend to miss is that emulation and recompilation are not opposite ends of a spectrum with a clean line between them. With hardware as complex as the Xbox 360, you need to provide a compatible environment for the recompiled code to run in. That means memory layout, kernel objects, threading, filesystem access. Those are real systems that need to exist regardless of whether the CPU code is JIT-compiled or statically recompiled. We inherited Xenia's kernel layer and have heavily modified it to work with our execution model, but the fact that some of that infrastructure has roots in an emulator doesn't make the recompilation any less real. It means we were smart about what we built from scratch and what we adapted.
The difference in execution model is significant and measurable. In Xenia, when a thread executes, the JIT translates PPC instructions on the fly, manages a code cache, and makes runtime optimization decisions. In ReXGlue, the function dispatch table is populated once at startup with native function pointers. When a thread needs to execute a guest function, it looks up the address, gets a C++ function pointer, and calls it directly. No translation, no cache, no interpretation. The recompiled code can be stepped through in a standard debugger, profiled with standard tools, and optimized by the full Clang optimization pipeline. That is a fundamentally different execution model from JIT emulation, and the results speak for themselves."

As ReXGlue processes, it'll eventually come to include native rendering, audio, and input support. Once it's replaced the GPU emulation from Xenia, games will be able to run even faster on PC — but that's a big job still to come. The Xbox 360's hundreds of games used its GPU in different ways, which means that for the forseeable future each individual port project will be figuring out howthatgame did things and feed that understanding back into the ReXGlue SDK.

Tom has already been doing that with his work on Blue Dragon. "Everyone tries things out and reports back with improvements or things that need to be fixed," he says. "In my experience, that feedback loop is the best way to keep experimental research projects like this alive and moving forward. Experimentation drives innovation."

ReXGlue is open to anyone interested in getting involved, with its ownDiscord serverfor organizing. Like N64 Recompiled, ReXGlue doesn't exist just to make it possible to develop PC ports of these games, but to make them better; to make them accessible playgrounds in ways they weren't before, even ifreallydedicated modders were able to hack their consoles and mess around with games 15 years ago. "The goal has always been to make this a platform that others can build on, not just a black box that runs a game," Tom says.

Halo 3 via Twister on ReXGlue Discord

So, the big question: When will we be able to play Blue Dragon, or Nuts & Bolts, or any of these other recomps? Tom knows better than to guess at a date.

"I honestly don't have a timeline. For Blue Dragon specifically, it needs to be at a place where I can say it is genuinely worthy of being put in front of people. That's a high bar, and I know it's a subjective one. I hold my own work to a strict standard. Getting a title to boot is a real accomplishment, and the effort involved should not be understated, especially for people who have limited exposure to systems-level programming. But booting is a starting point, not a finished project. There is a long distance between 'it runs' and 'this is something people should play.' I want the projects that come out of ReXGlue to represent what the SDK is actually capable of, not just that it technically works. When something is ready to be released, it should demonstrate real quality: clean implementations, thoughtful use of the SDK, and genuine progress beyond initial boot. That is the standard I hold Blue Dragon to, and it is the standard I encourage everyone in the community to hold their own projects to as well." 💽

### 2. N64 Recomps get an all-in-one launcher

Fortuitous timing, giving we're talking all about recompilations this issue! As more and more of these projects arrive, keeping tabs on each one will either mean a cluttered desktop of icons, manually adding each to your Steam library, or... using a dedicated launcher!

N64RecompLauncher, currently v1.56, has actually been around since last August, but a bevy of updates since then have seemingly gotten it into pretty good shape. It currently runs on Windows and Linux, and I got it installed and cruising in just a couple minutes. It's got a built-in updater and a bunch of UI options, so you can choose a layout more suited to a big library, a desktop monitor, or a more cramped Steam Deck screen.

Installing each recomp takes only a second or two, because this is really just an organizer for those projects which each have their own launcher and require providing your own copy of the game ROM before they can be played. But it's definitely convenient. My favorite option in the settings menu is "Show Experimental Games," which is off by default; this prevents a load of early, incomplete recomps from cluttering up the interface if you just want to play the ports that have stable releases or are actually finished.

But tick that box and you can see a bunch of in-the-works projects like Mega Man 64 and Chameleon Twist, playable (at least somewhat) on your computer! There's also another switch for "custom games" which are not specifically recompilations, but other ports of console games based on decompilations, like the ones I've been keeping track of on myDecompilation projects and N64 Recompiled PC portslist. RexGlue's Banjo Kazooie: Nuts & Bolts, Legend of Dragoon: Severed Chains, Perfect Dark, Link's Awakening DX HD, and more can be found within.

Some of the classifications might be a bit wonky — Nuts & Bolts is listed as stable, for example, but that's only because the Github project'slauncheris billed as 1.0, while the underlying recompilation tools for the Xbox 360 are still very much in development as the interview above covers. That's not going to be anywhere close to a pristine experience.

But the option to have all of these ports organized in one place with easy updating is a big win, particularly if, like me, you want to eventually try them all. For native PC games we used to groan every time Steam had to launch another launcher, but in this case I think it's a welcome convenience.

Subscribe to ROM!

## Patching In

Azahar 2125 brings the noise, and an offical Libretro core– For Retroarch folks, the premiere 3DS emulator is now available as a core across Windows, Linux, Mac, Android and iOS, but that's just the tippy top of the iceberg for this update. It also includes a disk shader cache for Vulkan to avoid shader recompilation; CPU usage improvements when using the Artic Base streaming app; restored texture filtering support; new video scaling options; and loads of platform-specific fixes and additions. Android users can now automap controls as on desktop, for example, while on desktop controllers with touchpads like the DualSense can be used to control the emulated 3DS touchscreen. Neat!

ShadPS4 v0.15 does stuff, sets the stage for Bloodborne netplay– The Bloodboo—er, PS4 emulator hit a new major version number, though none of its listed improvements like "Prevent protects during unmaps" or "Threads: initialize TLS on thread creation" immediately mean much to me. The release notes also mention bigger improvements to come in the next release, and over on YouTube developer George Moralis posted a taste: online play working in Bloodborne. I'm guessing there will be some problems or limitations for quite some time to come, but it's tantalizing nonetheless.

PPSSPP continues to polish, including savestate-undoing– The PSP emulator's big recent release is up to .3 in bugfix and polish patches, including one that fixes a missing prompt to undo a savestate you've just made, if it was a terrible mistake. A handy feature! You can also now apply game-specific settings to homebrew, and DualSense Edge controllers work.

RPCS3 lets you add games to Steam from within the emulator– Quite a cool quality-of-life feature here, the PS3 emulator now includes a right-click menu entry to add a shortcut for any game to your Steam library, so you can boot 'em right up like any other PC games. Seems quite nice if you're a Big Picture Mode user especially, and to that end RPCS3 also just rolled outa new in-game menu UIthat seems a bit more organized. Dang... it's almost like they planned it.

You can now add games to Steam directly from RPCS3!Games can be launched directly from Steam, without going through the main RPCS3 UI.pic.twitter.com/3QUAEuGZPR

— RPCS3 (@rpcs3) 
March 16, 2026

## Core Report

A hearty helping of MiSTer tweaks– An unusually big roundup from Sorgelig this week with updates for a number of systems. The SNES core gets both rumble and save state support, my nemesis the CD-i gets some fixes, and the MiSTer as a whole get a nice QoL feature: "video_off_hdmi option to power down HDMI on idle timeout."

Taito System SJ heads to the front line– Developer Anton Gale reported this past week that an update to the System SJ core for the MiSTer now includes Front Line and The Tin Star, following Sea Fighter Poseidon in February. Get yer '80s action on.

## Translation Station

Blaze & Blade Busters bursts into English– I have to say, this is an endearingly uggo PS1 action RPG. Is it a better game than its apparently dogwater predecessor, Blaze & Blade: Eternal Quest? That I cannot tell you! But where that game got a PAL release this one never did, until now, thanks to fan translator Ben128. The multiplayer (with 4-player multitap support!) seems like fairly uncommon for an RPG of the time, and at least according to whoever submitted it to the GOG Dreamlist, it's seen at least some improvements: "

Sherlock Holmes for the SG-1000 paints an English portrait of Loretta– Given the number of Sherlock adaptations out there, I would not be surprised if you told me there were literally dozens of games outside the modern Frogwares series that I've never heard of. There's certainly at least one! Sherlock Holmes: Loretta's Portrait was released on Sega's first console (predating the Master System) in 1987, and now it's been translated thanks to Jamiras.

"What stuck out to me about Loretta's Portrait was how ambitious it was for an SG-1000 game," writes YouTuber NintendoComplete. "The machine wasn't designed to handle much beyond simple early 80s arcade-style shooters and platformers, and yet here we see a fully explorable city, full-screen background images, window overlays, boatloads of text, and a save system. As crude as the graphics and sound are, I can't help but be impressed by what Sega achieved with this cart." Honestly, rudimentary as it is, there's some pretty nice art in here.

## Good pixels

Closing out with a dip into the always delightful #scanlinesunday. Stay sharp!

Did you ever wish your favorite light novel characters could battle it out? This #ScanlineSunday you can in Dengeki Bunko: Fighting Climax for Playstation 3 🥖

in this 1v1 fighter from French Bread, select one of 12 characters and an assist from 22 titles, with some new and others you know!

— 
Sick Combos (@sickcombos.bsky.social)
 
2026-03-23T04:15:28.899Z

With Bio Hazard/RE's 30th Birthday in its twilight, I thought I'd revisit the original Capcom haunted mansion for this week's #ScanlineSunday. 

A not-so-Sweet Home in its own Forest Zone and with creepily opening doors…

📺: Toshiba VTW-2187, composite, snapped with an Olympus Camedia C-765

— 
Sasha's Retrobytes 🏳️‍⚧️ (@sharkabytes.bsky.social)
 
2026-03-22T21:17:40.821Z

SCR$: International Karate+ / ZX Spectrum via MiSTer 
RGB / Sony WEGA 21" CRT TV
#CRT #photography #retrogames #scanlineSunday

— 
CRT ART Books (@crtartbooks.bsky.social)
 
2026-03-08T13:40:41.102Z

Bought a Gameboy player recently, and i've been having SO MUCH fun seeing what all these games look like on a crt! #ScanlineSunday

— 
Neimi (@aquaticscent.digital)
 
2026-03-08T19:03:34.539Z

## Sign up for Read Only Memo

Videogame emulation news and exclusive interviews, from the aesthetics of razor sharp scanlines to the wild technical challenges of making yesterday's games run on tomorrow's hardware.

Heck, it's free

 Email sent! Check your inbox to complete your signup.
 

No spam. Unsubscribe anytime.

Share this post

The link has been copied!

 

### You might also like

## DREAMM explores a galaxy of fun as it rescues more LucasArts games from obscurity

		by
		
Wes Fenlon

 

## After 17 years, Dolphin can finally emulate the Triforce arcade — except this one obscure, ambitious card game

		by
		
Wes Fenlon

 

## The follow-up: Taki Udon on the SuperStation Dock, and more Quest 64 Recomp

		by
		
Wes Fenlon

 

## "Failure can't be an option:" Taki Udon breaks down the last year of 12 hour days, 6 days a week he poured into the SuperStation, his dream MiSTer FPGA console

		by
		
Wes Fenlon

 

## Quest 64 Recompiled: The "classic" RPG like you've never seen it before

		by
		
Wes Fenlon