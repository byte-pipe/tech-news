---
title: Reverse-engineering the 1998 Ultima Online demo server - Draxinar
url: https://draxinar.github.io/articles/2026-05-01-uodemo-reverse-engineering.html
site_name: hnrss
content_file: hnrss-reverse-engineering-the-1998-ultima-online-demo-se
fetched_at: '2026-05-06T20:20:59.335550'
original_url: https://draxinar.github.io/articles/2026-05-01-uodemo-reverse-engineering.html
date: '2026-05-06'
description: Reverse-engineering the 1998 Ultima Online demo server
tags:
- hackernews
- hnrss
---

# Reverse-engineering the 1998 Ultima Online demo server

May 1, 2026

After 10 years of on-and-off work, I’m releasing a full reverse-engineering of the 1998 Ultima Online demo server:https://github.com/draxinar/ouo. About 5,000 functions disassembled from MSVC x86 and translated into portable C99, with each function compared instruction-by-instruction against the binary.

## UoDemo.exe

For those who don’t know, Ultima Online is a 1997 MMORPG developed by Origin Systems Inc. It was one of the first commercially successful MMORPGs. The client ran on Windows and each server (so called “shards”) ran on multiple Solaris machines (the map was split by regions).

The first release of “Ultima Online: The Second Age” expansion (October 1998) shipped with a standalone Ultima Online demo (UoDemo.exeandUoDemo.dat), which bundled a client and a Windows port of the full server code and data.UoDemo.exeis dated 1998-09-02, and the server data were extracted from the production server on June 2nd, 1998. A handful of features were stubbed for the demo and the playable map was reduced to the island of Ocllo (a small NPC town off the southern coast of Britannia), but the rest is the actual production server code that was running on live UO in mid-1998. The demo featured a simple quest to kill a dragon on the island of Ocllo, with an overview of the basic game mechanisms (speech, trading, combat, etc.). Many UO server emulators reused parts of it, but so far none have ever fully reverse-engineered it.

UoDemo.exewas compiled with Microsoft Visual C++ 5.0 (Visual Studio 97), targeting a pre-C++98 dialect of C++.

I worked on this project intermittently for 10 years, until recent developments in LLMs finally made it possible to complete this seemingly never-ending task.

## Methodology

* Disassembly withradare2.
* Symbol names deduced from an experimental Linux port of UO client 1.25.37, which was shipped with C++ symbols.
* Each function is translated by hand into C99, keeping the same control flow, struct layout and branches as the binary. When something differs, it’s either a fix for a real bug in the demo or a platform adaptation, and it’s flagged in the source.
* To verify, I re-disassemble the C build under r2 and compare it against the original. A function is only marked done once the two match.
* Helper functions are used only for repeated inline patterns, and only when the helper expands back to the same code as the inline version.

The class hierarchy was the most important thing to get right early on:CEntity (0x10) -> CResourceEntity (0x1C) -> CItem (0x50) -> CContainer (0x5C) -> CMobile (0x37C) -> CPlayer (0x458), with virtual dispatch through vtable slots (vtable[0x18]isIsPlayer,[0xD0]isIsMobile,[0xE4]isIsNPC, etc.). Once those layouts were nailed down, most of the binary was straightforward to translate.

The result is an almost perfect replica of a 1998 Ultima Online server, though there are some differences.

## Findings

Compared to the original code, I’ve fixed stability issues (crashes, overflows, uninitialized variables, etc.) and gameplay issues (skill gain, fame/notoriety direction, spawn density, etc.). Each fix is tagged in the source, so anyone diffing againstUoDemo.execan see precisely what changed and why.

Some features were broken, like the spawn system and the decay system, probably because they were partially disabled or stubbed out specifically for the demo release: the code is intact but no live call site reaches it. Decompiling them in isolation and re-wiring the dispatch is enough to make them work again. Some data was missing too: for example, the game map only covered the island of Ocllo. I’ve written a full tooling suite to manipulate the server data formats, and fully reconstructed doors, signs, decorations, teleporters, traps, chests and spawn locations for the rest of the world.

More surprisingly, the famous retiredecology systemwas still present in the code, even though the functions were no longer called. I’ve re-wired the predator/prey/scavenger system, which is very cool: you can now see wolves chasing rabbits or crows eating items. However, this doesn’t implement the full resource/production system, because of the lack of precise data. See blog posts from Raph Koster about UOecology systemand UO resource system:1,2and3.

I’ve also added a few straightforward new features, like the Meditation, Stealth and Remove Trap skills, which were added by OSI in February 1999, though some early traces were already present in the code. Most of the new features can be enabled or disabled at startup using the-featuresparameter.

Since the account system was completely absent from the demo server, I’ve re-implemented it by guessing how the original developers would have done it, though slightly modernized.

While the demo server only supported client 1.25.33, I’ve added support for allclientsfrom 1.25.30 up to 5.0.9.1 (2007-03-27), with and without encryption. Since there were five completely different encryption mechanisms over the years, I had to reverse-engineer each of them in the client binaries.

The original binary is 32-bit, but the default build now targets 64-bit. The class hierarchy uses C struct embedding to reproduce the original C++ inheritance, so aCMobile*can still be passed where aCContainer*is expected. Pointer widening on 64-bit would otherwise shift the inherited fields out of place, so some structs are deliberately padded to keep the inheritance and vtable layout matching the binary in both modes.

## Links

* Code:https://github.com/draxinar/ouo
* Data, based onUoDemo.datalong with fixes, completed data and new features:https://github.com/draxinar/rundir
* Test Center:https://uo.serpent-isle.com/. This is not a real shard, but a testing environment. You are very welcome to join and try out a very faithful reproduction of a 1998 Ultima Online server.
* Inspiration:UO:98by Batlin and Derrick, the project that started me down this path in 2016.

I’d strongly encourage you to read the code and data, because there are innumerable little details about the internals of Ultima Online that are little known and explain a lot about its history and design.

OUO is still in early stages and many issues could be still present. Please report anyissueyou encounter. Contributions are highly appreciated.

Enjoy.

## A request to the Ultima Online community

If anyone out there has thedynamic0.mulordynamic0.bkp(server savegames) orregions.txt(spawn definitions) orresbank.mul(resources definitions) files from the original Ultima Online servers, circa 1997-2003, I’d be very grateful if you could send them to me. It seems very unlikely that the originaldynamic0.mulordynamic0.bkpfiles are truly lost, since they were surely backed up in multiple safe places.

I have all the tooling needed to strip out player data from thedynamic0.mulfiles to preserve privacy before distributing them.

These files would be extremely valuable to produce a highly accurate reproduction of the Ultima Online world content.