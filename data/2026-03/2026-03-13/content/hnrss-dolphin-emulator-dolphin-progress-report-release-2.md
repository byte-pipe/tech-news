---
title: 'Dolphin Emulator - Dolphin Progress Report: Release 2603'
url: https://dolphin-emu.org/blog/2026/03/12/dolphin-progress-report-release-2603/
site_name: hnrss
content_file: hnrss-dolphin-emulator-dolphin-progress-report-release-2
fetched_at: '2026-03-13T03:13:08.271166'
original_url: https://dolphin-emu.org/blog/2026/03/12/dolphin-progress-report-release-2603/
date: '2026-03-12'
description: 'Dolphin started out as a GameCube emulator in 2003. In 2008, experimental Wii support was added. And now, in 2026, Dolphin enters the realm of arcade emulation with support for the Sega, Namco, and Nintendo arcade effort, the Triforce, finally arriving. Want to learn more about the Triforce? Check out our deep dive into the Triforce and how it ended up back in Dolphin! Emulating a new system and library of games for the first time in 18 years is big news, and we''ll dive into some details and updates on that later in the report. However, there are two other major additions that would have been flagship changes on their own in any other report. Optimizations to Dolphin''s MMU emulation have brought major performance uplifts to games that rely on custom page table mappings. In fact, on powerful hardware, all Full MMU games can run full speed, including the legendary Rogue Squadron III: Rebel Strike. On the other side of things is a targeted fix that took an inordinate amount
  of effort. An epic tale that spanned years of frustration. In the end, the incredible efforts of the Mario Strikers Charged community combined with several CPU emulation experts finally cracked the case of a minor physics bug that would normally be impossible to see or test. All that and more awaits in this release''s jam-packed notable changes!'
tags:
- hackernews
- hnrss
---

Dolphin started out as a GameCube emulator in 2003. In 2008, experimental Wii support was added. And now in 2026, Dolphin enters the realm of arcade emulation with support for the Triforce, a joint Sega, Namco, and Nintendo arcade effort. Want to learn more about the Triforce? Check out our deep dive into the Triforce and how support for it ended up back in Dolphin!

Click or tap the image above to read our deep dive into the Triforce!

Emulating a new system and library of games for the first time in 18 years is big news, and we'll dive into some details and updates on that later in the report. However, there are two other major additions that would have been flagship changes on their own in any other report. Optimizations to Dolphin's MMU emulation have brought major performance uplifts to games that rely on custom page table mappings. In fact, on powerful hardware, all Full MMU games can run full speed,including the legendaryRogue Squadron III: Rebel Strike.

On the other side of things is a targeted fix that was an epic tale spanning years of frustration. In the end, the incredible efforts of theMario Strikers Chargedcommunity combined with several CPU emulation experts finally cracked the case of a minor physics bug that would normally be impossible to see or test.

All that and more awaits in this release's jam-packed notable changes!

### Notable Changes¶

All changes below are available in Release 2603.

#### 2512-285 - Core: Create Fastmem Mappings for Page Table AddressesbyJosJuice¶

"Fastmem" is one of Dolphin's biggest performance tricks. The GameCube and Wii's MMIO (Memory-Mapped Input and Output) memory mappings do not directly translate to the host system, and without a way to sort ordinary RAM accesses from MMIO accesses, Dolphin would need to manually translateeverymemory access at tremendous cost. Enter fastmem, where Dolphin exploits the host CPU's exception handler to sort accesses for us. If we map the entire GC/Wii address space to host memory, mappings for main memory will just work, no intervention needed. But attempting to access an address assigned to MMIO will trigger a CPU fault. When that happens, Dolphin can catch this fault and immediately backpatch the affected JIT code to manually translate the address instead. Just like that, Dolphin will only spend the effort translating memory accesses that it actually needs to translate, and the rest will be performed natively by the host CPU at incredible speeds.

However, fastmem didn't cover everything - it only supported memory mapped withBlock Address Translation (BAT). Any time a game accessed memory mapped with apage table, the other way to map memory on the GameCube, Dolphin wouldalwayshave to manually translate it.

This may sound problematic, but thanks to tricks like theMMU Speedhack, the vast majority of games see no performance penalty from page table accesses. In order for this lack of support to actually impact performance, a game would have to have a custom memory handler that resists our hacksandheavily relies on the page table. But what developer would be crazy enough to do all of that?

...Right.
You.

Factor 5 is arecurringvillainfrenemy here on the Dolphin blog for a reason. If there's a trick to squeeze more power out of a GameCube, Factor 5probably invented it. In this case, they went through all that trouble to getextra RAM.

The GameCube is amemory starvedmachine - its paltry 24MiB of RAM istinycompared to its capabilities and storage media, which limited what developers could do with the machine. However, there is an additional 16MiB of RAM connected to the DSP, known as Audio RAM (ARAM). On a memory starved machine, an extra66%of memory is extremely tempting.

There's a problem, though - the GameCube's CPU does not have direct access to ARAM. All the GameCube's CPU can do with ARAM is tell the DSP to useDirect Memory Access (DMA)to copy data from a range of main memory to ARAM, or vice versa. This is normally used for various DSP functions, such as loading audio samples.

For a game to use Audio RAM asgeneral purposeRAM, some setup is required. If a game configures a range in thepage tableto point to invalid memory addresses, when it tries to access this memory, the invalid memory access triggers a CPU fault. That invokes the game'spage fault handler, which uses DMA transfers to swap data between main memory and ARAM as needed. When the game resumes, the memory access will return data as if it were stored in valid memory all along. Through this process, data can be copied to/from ARAM in an automated fashion outside of the primary game logic, allowing games to more or less treat a range of invalid memory as if it were extra RAM. Audio RAM used this way is significantly slower than main memory due to its reliance on DMA transfers, but it'sorders of magnitudefaster than waiting for data from a spinning optical disc, so it's still a huge win.

Notably, the GameCube can only perform the above setup with the page table, as the hardware has too fewBATsand their granularity is too large for this technique.

Halfway into the GameCube's life, Nintendo standardized this ARAM access process with a library provided in the GameCube developer support tools, so that developers didn't need to waste time creating their own solution. All games that utilize this library configure the page table in the exact same predictable way. Since we know exactly what they are going to do and we aren't bound to a GameCube's hardware limitations, Dolphin can just cheat for these games and set up a BAT pointing to extra memory that the GameCube doesn't have, bypassing all of that trouble while still getting the full benefits of fastmem. This trick is the aforementionedMMU Speedhack, and it has been enabled by defaultsince 2014.

But years before Nintendo standardized this process, Factor 5did it all themselveswith their own custom memory handler inRogue Squadron II. And, even though Nintendo's library existed by the timeRogue Squadron IIIcame out, Factor 5 went above and beyond in that game with aneven more optimizedcustom memory handler to squeeze as much as they possibly could out of ARAM. Tricks like this are what allowed Factor 5 to push the GameCube to such ridiculous levels.

Is that...
texture streaming
?!
Click or tap the clip for a larger version.

Factor 5 may have gone to the extreme, but they weren't alone.Star Wars: The Clone Wars,Spider-Man 2, andUltimate Spider-Manalso use custom memory handlers.

On the Wii, none of this is necessary as ARAM is directly accessible to the Wii's CPU as "MEM2". But that didn't stop some games from being weird. As werecently covered, the Disney Trio of Destruction™ use the typical memory addresses that any other Wii game would use, but theyremove the default BATsand recreate them with the page table. Dolphin now patches out that behavior by default, but we know that they also use the page table for... (checks notes)memory defragmentation?

Since these games use custom memory handlers, their usage of memory on the system is entirely unique. We can't predict what they are doing and we need to properly emulate their page table mappings. And since page table mappings weren't implemented in fastmem,everyaccess to memory handled by the page table had to be manually translated, with a varying performance impact depending on whatever the game was doing.

Admittedly, this didn't affect a lot of games. But one of those titles isRogue Squadron III: Rebel Strike, a game that has effectivelynever been playable at full speed in Dolphin. We knew that implementing page table mappings in fastmem would be the key to making these games go faster, and we were more than willing to put in the effort to do it. Unfortunately,we just didn't know how.We've even attempted it a few times over the years, but we never created a successful, let alone fast, implementation.

We were missing something.

While we were trying to defang the Disney Trio of Destruction™,JosJuicenoticed that every timeCars 2manipulated the page table, it executed the instructiontlbie. According to the publicly available PowerPC 750 user manual, after any page table modificationtlbiemust be used to clear the relevant part of the TLB (the page table cache). If Dolphin paid attention to when this instruction was executed, it would have a way to keep track of every page table modification.Dolphin could use this information to map the page table in fastmem!

Upon this realization,JosJuiceimmediately began implementing page table mappings in fastmem. However, knowing how to do something and actually doing it are two different things. Even with a plan, this required loads of tricky, low-level work with tons of trial and error. And it wasn't immediately successful! An early implementation was actuallyslowerthan manually translating everything! But after a lot of thinking and experimentation,JosJuiceimplemented incremental updates to page table mappings in fastmem, where we compare the new mappings with the old ones in 64-byte chunks, and then do a bunch of logic to figure out which mappings need to be removed or added.

This secret sauce is still heavy, but it's faster than manually translating every page table access! At least,usually. It depends on the game and how often it usestlbie.Rogue Squadron IIandespeciallyIIIhit ARAM so hard that they will always see a performance boost from page table fastmem. Meanwhile, some games with custom memory handlers, likeSpider-Man 2, actuallylosea little bit of performance due to the overhead of tracking page table updates. On the flipside, when those games do load from ARAM, the hitches that once plagued them are greatly reduced or completely removed in many cases, so their overall playability is better than before.

When Spider-Man 2 loads data from ARAM, Dolphin would sometimes drop several frames.

While overall performance is slightly lower, traversing the city is a smoother experience overall with smaller and rarer hitches.

Now, this is the part where we show you some fancy performance graphs. However,JosJuicewasn't quite done yet. After implementing Page Table Fastmem Mappings, they unleashed a flurry of optimizations targeting the Rogue Squadron games specifically. So, we've opted to bundle all of the Rogue Squadron results into the next section. For now though, here's ourSpider-Man 2andCars 2performance test results.

Before
Spider-Man 2: 56 FPS
Cars 2: 37 FPS

After
Spider-Man 2: 52 FPS
Cars 2: 57 FPS

Before
Spider-Man 2: 133 FPS
Cars 2 - 278 FPS

After
Spider-Man 2: 126 FPS
Cars 2 - 397 FPS

As mentioned earlier,Spider-Man 2is slightly slower with this change, but it has fewer traversal stutters so it feels more fluid in motion. Given that performance is not really an issue with this game - our eight year old low end laptop can run it easily - the trade is more than worth it. As forCars 2, while we patch out theover 10,000 page table mapped entriesthat the Trio performs when it remaps the standard BATs with the page table, it turns out that they still have 400-800 page table mapping entries remaining. Now that these mappings can go through fastmem,Cars 2has become a fairly accessible game. The old low end laptop in the test above is almost able to play it at full speed now. Compared to a year ago whenCars 2's performance was barely in the double digits on that hardware, this is an amazing turnaround!

Now, back to Rogue Squadron!

#### EvenMoreRogue Squadron II & IIIOptimizationsbyJosJuice¶

Even with page table fastmem mappings,Rogue Squadron IIandIIIare still among the most demanding games in the entire GameCube and Wii library. Fortunately, by removing that primary performance bottleneck, a lot of optimization opportunities revealed themselves.

One major complaint inRogue Squadron II: Rogue Leaderspecifically is that swapping between cockpit view and chase view results in a serious stutter. For some reason (we haven't fully investigated it, but it's likely related to ARAM swapping), the game forces Dolphin to both invalidate and JIT an enormous amount of code all at once. The sheer volume of what it's doing in a short time bottlenecks CPU emulation and causes a hard stutter.

This stutter was over 300 milliseconds long!

JosJuicetook multiple measures to speed up this particular case. First, they disabled a feature known asBranch Followingfor this game. This feature makes the JIT follow branch instructions to create larger blocks of code to process all at once, making it possible for the JIT to output more optimized code. Especially in games with tricky to detect idle loops, such asXenoblade Chronicles, the larger blocksvastly improve performance. But it also causes the JIT to outputmorecode, making both JIT-ing and invalidating slower, which is very bad inRogue Squadron II's case! This feature is why the view change stuttering suddenly got worse soon after 5.0, and disabling Branch Following in the Rogue Squadron games resolves this regression.

Second,JosJuicefound ways to optimize invalidating code! By using a more efficient data structure to keep track of JIT blocks, this part of CPU emulation becomes faster and Dolphin has more time to JIT the new code. All combined, the stutter is substantially improved.

There is still a stutter of around 60 milliseconds. But console also stutters about this much on every view change! This isn't accurate emulation by any means, but it feels similar during play.

The next improvement centers around the other demanding part of emulating these games - their graphics. Rogue Squadron renders stages in a rather unorthodox way. The terrain is divided into squares, and the game draws one square at a time, changing out the active texture for each square. Dolphin has to process hundreds of these squares per frame, with each one triggering Dolphin's texture lookup code. But it's not like the terrain is the only thing in the game - ships, ground troops, and lots of other things are being drawn too. Combined, this creates a huge number of draw calls and texture lookups.

That's a lot of polygons for the 'cube to push out.

JosJuicefound a regression where Dolphin was creating extra objects in memory whenever the game used textures. In most games, this regression was essentially invisible. But in the land stages inRogue Squadron IIandIII, the affected texture code can run over 300,000 times per second! Even a tiny optimization makes a sizeable difference when the affected code path runs that many times!

Next, these two games saw several changes in Dolphin's GameSettings database. We already mentioned disabling Branch Following, but several more settings have been changed to improve performance in these games.CPU Vertex Cullingis now enabled, letting Dolphin skip rendering 3D objects that wouldn't be visible anyway, which among other things cuts down on how many of those terrain squares Dolphin has to process.

And finally, Store EFB Copies to Texture Only is no longer being forced off for this game. Why was it forced off, you ask? Back whenRogue Squadron IIandIIIfirst became playable, turning this off was necessary to getpaletted EFB copies working, which are used by the targeting computer. But paletted EFB copies started working with the setting turned onjust a month later! Aside from that, the only other effects we're aware of that needs the setting off are some of the menu fadeouts inRogue Squadron II. These fadeouts are a relatively minor thing, so we've decided to not force a value for the setting. Instead, each user can choose whether they prefer higher performance or nice menu fadeouts.

And now for the big question: with page table mappings in fastmem and all these optimizations summed up, how much faster doRogue Squadron IIandIIIrun?

Benchmark 1:
 RS2 Ison Corridor: 83 FPS
 RS2 Hoth: 35 FPS
 RS3 Revenge of the Empire: 13 FPSBenchmark 2:
 RS2 Ison Corridor: 93 FPS
 RS2 Hoth: 42 FPS
 RS3 Revenge of the Empire: 28 FPS
Benchmark 3:
 RS2 Ison Corridor: 107 FPS
 RS2 Hoth: 55 FPS
 RS3 Revenge of the Empire: 34 FPS

Benchmark 1:
 RS2-Ison: 303 FPS
 RS2-Hoth: 106 FPS
 RS3-Rev: 46 FPSBenchmark 2:
 RS2-Ison: 350 FPS
 RS2-Hoth: 140 FPS
 RS3-Rev: 52 FPS
Benchmark 3:
 RS2-Ison: 443 FPS
 RS2-Hoth: 172 FPS
 RS3-Rev: 90 FPS

The performance benefits areabsolutely massive. Of particular note isRogue Squadron III, whichdoubledin performance! On our top-of-the-line desktop, it can even be played at full speed for the very first time! And it's not just raw performance that improved - these changes help minimize hitching when the games are loading from ARAM. Even on the most powerful hardware, it's still not uncommon to drop a frame or two on loading screens and transitions. But compared to before, it's a night and day difference.

The caveat is thatRogue Squadron IIandIIIstill require extremely powerful hardware to get consistently playable speeds. Furthermore, the new default settings sacrifice graphical accuracy for performance, and disablingStore EFB/XFB Copies to Texture OnlyandSkip EFB Access from CPUlowers performance by roughly 12% to 15% in a demanding scene. That'sstillfull speed on strong enough hardware, but it does raise the barrier of entry that much more for players that want everything to look just right.

With strategic victories on all fronts, we fly home, having destroyed the once impenetrable Death Star of performance problems. Yet, it is unlikely we'll have ever truly won. Not only do these games still have some minor problems, but we know that something much more fearsome was in the works. Isolated from the rest of the galaxy, Factor 5 scientists built aRogue Squadron game for the Wiithat was never released. We know it exists, lurking in themawof someone's hard drive. If it ever comes online, Dolphin may becrushedby a threat moredevastatingthan any before...

#### 2512-395 - Core: Add Triforce Supportbycrediar¶

SinceTriforce support was added to Dolphin a few weeks ago, the community has been tremendously helpful, with multiple users who own fully operational Triforce cabinets coming forward to give us more information on how they work or to help us run hardware tests. It's only been a few weeks, so the feature article is stillmostlyup to date with our current Triforce efforts, but there have been a few changes already merged with more on the horizon:

* Dolphin now automatically inserts Magnetic Cards for cleaning checks. This change is available in 2603.
* Regions are currently hardcoded for games. A setting that allows the user to change regions will be added to the GUI soon.
* Several bugs in Dolphin's multicabinet emulation have been identified and are being worked on. These fixes will make multicabinet emulation work on a much wider range of hardware.
* F-Zero AXGameCube Memory Cardsupport has been solved and will be coming soon.
* Work on integrated namcam2 support forMario Kart Arcade GPandGP 2has been started, which will allow the games to work without the need of a separate program to emulate the camera.
* The touchscreen protocol used byThe Key of Avalonhas been identified and solved.
* Users with multiple originalF-Zero AXcabinets have submitted packet dumps to assist with implementing network emulation. We've already made some basic progress, though multiple instances still cannot join each other.

Soon. Hopefully. If the game is cooperative.

A lot of our effort after merging Triforce support has gone toward solvingThe Key of Avalon. Despite our best efforts, finding hardware for this game has proven impossible, so we've had to reverse engineer the game to determine what the hardware does. Thanks to tools likeGhidra, this is actually doable, though it is very time consuming and monotonous.

This approach isn't ideal, but we've made a lot of progress and had a few breakthroughs. Notably, we've identified the touchscreen protocol as being similar toElo's SmartSet Data Protocol. By hacking in the appropriate responses, we managed to start a new game! ...Only for it to immediately hang on the next screen.

We assumed that the problem was networking related, as the host and client didn't appear to be synced up, but that was a red herring. It turned out that the game only syncs up the attract modeoccasionallybetween the clients and the host, and the behavior we were seeing was normal. With no leads, we were essentially stuck once again. That was going to be the end of this entry, but serendipitously,Billiardstumbled across a disabled debug logging function built into the game! We patched the game to re-enable it, and the game started spitting out information onexactlywhat was going wrong.The gametold us directly that the culprit was IC Card initialization.

Over the following days, we identifiedmanyproblems with Dolphin's IC Card emulation code. So much so that we couldn't quite get everything done in time for the 2603 release. For now, here's a teaser of what's to come.

On each pedestal, players have secret information, such as their current cards.

The main screen shows an overview of player movement on the board or monster battles when they occur.

We also plan to bring multiple IC Card fixes toVirtua Striker 4,Virtua Striker 4 ver. 2006, andGekitou Pro Yakyuu, which will restore card functionality to them. In the Triforce article, we mentioned there were some modes that we couldn't find inGekitou Pro Yakyuu. Well, we found them. They're locked behind IC Cards! There's a whole team building mode, complete with a character creator, RPG elements where you level up your player, and the aforementioned homerun contest. The points that are used for high scores are saved to your card and can be used to upgrade your created player.

There will likely bea lotof updates to Triforce emulation in the next Progress Report, but until then, we'll leave our readers with another question that has us stumped.The Key of Avalonhas code to detect specialOWABIcards, and through hackery, we can get the game to acknowledge a card as an OWABI card. Unfortunately, we don't actually know what these cards are for, and the game hangs shortly afterward. If anyone has used an OWABI card or knows how they work, please let us know.

#### 2506-372and2512-211- The Mario Strikers Charged SagabyGeotaleandJosJuice¶

Sometimes a lot of big changes hit all at once. Triforce compatibility is huge. Nearly doubling the performance of the Rogue Squadron games is massive. But, this change here? It was a five year project with tons of twists and turns. Our reaction to seeingthisin the changelog can be summed up by this comment from someone on the blog staff:

AHHH THIS COULD HAVE BEEN A WHOLE ARTICLE ON ITS OWN I'M SO SCREWED.

Oh boy.

Back in theAugust 2021 Progress Report, we talked about a bug fix forInazuma Eleven GO: Strikers 2013. In this soccer game, if you used a Nintendo Wi-Fi Connection replacement service like Wiimmfi to play an online match between Dolphin and a real Wii, the two players would desync when performing certain actions. Thisslightlyhindered the online experience!

Thanks to the game's desync mitigation, Dolphin didn't disconnect, but the issues still made the game unplayable online.
Click/Tap to play. Click
HERE
 for a higher quality version.

The investigation was rather difficult because we couldn't debug it offline. Since Dolphin had to be connected over the internet with a real Wii, we couldn't just pause the emulator and use our usual debugging tools. Thankfully, the game's community narrowed down the issue and eventually found that thefnmsubsCPU instruction was implemented incorrectly in Dolphin's JIT but worked correctly in our interpreter.

Armed with that information,JosJuicejust had to make the JIT implementation match the interpreter implementation, rather than having to debug an online game. Once the differences were fixed, online play worked fine even when using the JIT.

So, why are we bringing up a problem that was fixed five years ago? It turns out thatInazuma Eleven GO: Strikers 2013wasn't the only Wi-Fi enabled Wii soccer game that desynced when playing between Dolphin and real hardware.Mario Strikers Chargedsuffered from a very similar problem and their community reached out to us following that Progress Report.

Unfortunately, it wasn't good news.Mario Strikers Chargedstill desynced shortly after the match started. And unlikeInazuma Eleven, there is no desync mitigation - if a desync happens, it's game over.

Seconds into a match between Dolphin and real hardware, this would inevitably happen.

There was a small upside: thefnmsubsfix did allow the game to stay synced forslightly longer. But since desyncs continued to occur after the fix, something was still horribly broken.

JosJuiceandJMC47both already had the game and quickly launched an investigation thinking it wouldn't be very hard to narrow down the issue. With JosJuice on a Wii U and JMC on Dolphin, they set up a transatlantic Wiimmfi session and tried to play a few matches. Everything worked fine for a while! ...Until two players touched one another. And even if that didn't happen, eventually the game would desync anyway.

To debug the problem, different JIT instructions on the Dolphin side were disabled so that they would fallback to interpreter.

What exactly are fallbacks? Dolphin is able to emulate the PowerPC CPU in two ways: using a Just-In-Time (JIT) recompiler, or using the interpreter. JIT recompilers area lotfaster than the interpreter, but it is much easier to program an interpreter and understand how it works. As such, the interpreter also contains some extra accuracy improvements that we haven't wanted to put in the JIT, either because it would hurt performance or because it would be too complicated.

It can be convenient to use the interpreter when investigating CPU emulation issues, but completely forgoing the JIT is very slow! To deal with this, the JIT has a feature called interpreter fallbacks, where one or more CPU instructions can be set to run using the interpreter, while all other CPU instructions run using the JIT as normal. This reduces performance anywhere from 0% to over 50% depending on what instructions are handled by the interpreter and how the game uses them, but even a 50% slowdown is a lot faster than not using the JIT at all.

After trying interpreter fallbacks foreverycategory of instructions, we still had no answer. But if no single category fixed it, there was always the chance that the issue spanned multiple categories. We first tried combinations of floating point instruction fallbacks, to no avail. Then, we outright disabledeverythingand used theCached Interpreterinstead. This made Dolphin run so slowly that we expected the Wii to kick Dolphin out of the match. But surprisingly, the game was able to cope with the horrible lag! Or at least it did, until it popped up a network synchronization error like in every previous attempt.

This is why theStrikersissue couldn't be easily fixed. Dolphin hadno correct implementation to reference. And with the test case requiring Wiimmfi, a real Wii/Wii U, and a network connection from Dolphin, the issue was essentially impossible to debug.

And soStrikerscontinued to haunt us. Different developers took stabs at trying to fix it over the years, but again and again we would hit a wall. We were at a loss. But as we despaired, theMario Strikers Chargedcommunity did not give up. If we needed a testable case, they wouldmake us one.

TheMario Strikers Chargedlabbers are insane. They know more about how the game works than we will ever understand. They've mapped out parts of the physics, character stats, and modded in their own features to balance the game to their liking. In order to try to solve this issue, theyimplemented a new mode into the game: AI vs AI spectator mode! This way, we could watch a match with zero player input. Combined with a patch to freeze RNG, we finally had our test case that we could use to analyze the problem!

This is the AI vs AI match they set up for us so we could compare with console. The score counters have been replaced with the coordinates of the ball!

By recording a match on console and comparing it to Dolphin, we could see where the game desynced. They even changed the scoreboard functions to print out debug information, so that we would knowexactlywhen things went wrong. The final push was a major collaboration betweenGeotale,flacs, and most importantly ace Strikers reverse engineerFeder. Together, they managed to narrow the problem down to an extremely small set of instructions that allowed for the creation of a hardware test.

The culprit?fmadds.Again.

fmaddsis closely related to thefnmsubsinstruction thatInazuma Eleven GO: Strikers 2013had problems with, since they're both Fused Multiply-Add (FMA) instructions. Like all respectably powerful CPUs, the PowerPC CPU in the GameCube and Wii has normal addition and multiplication instructions for both integers and floating point numbers. But with FMA, it also had a type of instruction that x86 CPUs didn't get until the 2010s: multiplying two floating point numbers and adding or subtracting a third floating point number, all in one go. Doing this in a single instruction not only improves performance, but also boosts accuracy.

When a CPU performs a floating point calculation, the result might end up having more decimals than the CPU can store in its registers, which forces the CPU to round the result. If a calculation is done using a multiplication instruction followed by an addition instruction, this results indouble rounding. But if the calculation is done using a Fused Multiply-Add instruction, the result only has to be rounded once, reducing the rounding error. This difference in rounding error has the potential to cause desyncs!

But by the time this issue was investigated, pretty much every CPU running Dolphin was already emulating FMA instructions using FMA instructions. The problem had to be something else. And it couldn't be the same problem asInazuma Eleven GO: Strikers 2013used to have, because that problem only happens as a result of negation, and the mnemonicfmaddsconspicuously doesn't containn(for "negate") orsub. Yes, the letter soup in instruction mnemonics actually means something!

To explain the problem, we have to go further back than a Progress Report from 2021. We have to go all the way back to the year the Progress Reports began and revisit theAugust 2014 Progress Report.

These replays proved invaluable to testing Dolphin's CPU emulation accuracy back in the day.

This ancient tome describes the valiant efforts of two legends from Dolphin's olden days,magumaguandFioraAeterna. Through their work, Dolphin's emulation of multiplication instructions likefmulsandfmaddsbecame more accurate, fixing replay desyncs inMario Kart Wii,F-Zero GX, and many other games. Unfortunately, the tome is rather light on details about the specific inaccuracy they fixed, but through an archeological technique known as "reading the commit history", we were able to fill in the blanks.

On PowerPC, floating point instructions come in two variants: 32-bit and 64-bit. (The instructions we've been talking about so far are all 32-bit, as indicated by their mnemonics ending insfor "single precision".) 32-bit instructions take 32-bit inputs and produce a 32-bit output, and 64-bit instructions take 64-bit inputs and produce a 64-bit output.

But what would happen if you tried to give a 64-bit input to a 32-bit instruction? IBM's manuals say that you shouldn't do this, but GameCube and Wii games do it all the time, likely due to compiler quirks. And it does work, kind of! Many other CPU architectures would have read half of the 64 bits of the inputs, resulting in a nonsensical number, but PowerPCalmostdoes the desired behavior. The least significant 28 bits of the right-hand side operand are truncated, but other than that, you get the result you would expect!Fiora's change implemented this truncation, making Dolphin more accurate to a real console.

But hold on. This is an operation that takes in 64-bit inputs but results in a 32-bit output. There aren't any x86-64 or AArch64 instructions that do that! Instead, Dolphin emulates the operation using a 64-bit instruction, and rounds to 32-bit afterwards. This results indouble rounding! Fortunately, it has beenmathematically proventhat double rounding is safe when feeding 32-bit inputs into a 64-bit addition, subtraction, multiplication, or division instruction, as it doesn't change the result at all. There may be rounding errors when using 64-bit inputs, but Dolphin's approach is still more accurate than the alternative of using a 32-bit instruction.

But hold on once again. What about feeding 32-bit inputs into a 64-bitFused Multiply-Addinstruction?

This is where we return toFeder's investigation. They had discovered a specific set of 32-bit inputs tofmaddsthat resulted in-0.83494705(hexadecimal0xbf55bf17) on console but-0.83494711(hexadecimal0xbf55bf18) on Dolphin. That's a difference of just one in the hexadecimal representation, which is indicative of a rounding error!Geotaleimmediately knew what was going on, thanks to her experience of investigating how math works both in Dolphin and on original hardware. The type of double rounding that Dolphin does is in factunsafefor Fused Multiply-Add.

Pictured: Dolphin developers getting more and more angry at how
Mario Strikers Charged
 calculates how the ball spins.

Geotalequickly implemented a solution in Dolphin's interpreter: if none of the inputs lose precision if converted to 32-bit, the interpreter converts them to 32-bit and uses a 32-bit FMA instruction. Otherwise, it uses a 64-bit FMA instruction like before. Not long after, theMario Strikers Chargedcommunity were able to confirm that this change solved their desync issue. But the change also had the potential to negatively impact performance. To make Dolphin run different code depending on whether all inputs are safe to convert to 32-bit, a conditional branch instruction is needed. If the result of the condition is the same almost every time, the CPU's branch predictor can do a very good job, which minimizes the performance impact of the conditional branch. But an incorrect guess from the branch predictor costs tens of cycles of execution time, which adds up quickly with how often games use FMA instructions.

JosJuicetherefore came up with another idea: Dolphin could perform the calculation using a 64-bit FMA instruction as before, and then use the2Sumalgorithm to calculate the difference between the mathematically correct result and the 64-bit rounded result. Using a conditional branch, the result would then be nudged by a tiny bit if there was a difference, to make sure the result is rounded in the correct direction. Finally, Dolphin would convert the 64-bit result to 32-bit.Geotaleimproved on this idea by making the branch conditional not only on whether there was a difference, but also on whether the 64-bit result is exactly halfway between two numbers that can be represented as 32-bit - the exact case that's troublesome for double rounding. It's very unlikely for both of these two be true at once, which makes the branch predictor happy. On top of that, this method also increases accuracy for 64-bit inputs! There are still some 64-bit inputs that aren't handled correctly, mostly involving denormals and numbers so large they can get rounded into infinity, but games shouldn't trigger these cases unless they're intentionally trying to be mean to us. We hope.

Unfortunately, the code for this solution is a bunch of math soup that confuses everyone not willing to spend hours trying to understand what's going on. ButGeotaleandJosJuicepersevered. Thanks to their work, and the multi-year effort of everyone investigating the issue, floating point numbers are now rounded a tiny bit differently for certain instructions. All of this just to let Dolphin play online with real Wii consoles in a game whose official servers are since long dead and whose replacement servers have a peak of only15concurrent online players.

But did you know that there's still a desync if you connect Dolphin and a GameCube through LAN and play1080° Avalanchetogether? This is now thelastknown physics desync in a multiplayer game between Dolphin and console! Keep an eye out for it in a future Dolphin Progress Report!

#### 2512-59 - Wii Menu Data Management TimingsbyBilliard¶

The Wii Menu is one of the hardest to run pieces of Wii software on Dolphin for one simple reason - Dolphin is too fast. A lot of the memory operations that the Wii does, specifically with NAND management, don't have proper timings in Dolphin. On console, a lot of these operations are pretty slow, but Dolphin will attempt to complete them as fast as possible and thenlagwhen host hardware can't keep up even though it's going many times faster than a real Wii!

Trying to load all of the saves on a NAND at once caused Dolphin to chug when opening this screen.

In order to make things a little more palatable,Billiardadded some very rough timings to ease the difficulty of emulating this menu. Dolphin is still faster than a real Wii, but it's now slow enough that it shouldn't bring even the most powerful hardware to its knees anymore. For a full fix, hardware testing and real timing data needs to be used to make the Wii Menu do these operations at a reasonable speed.

#### 2512-19 - Core: Ability to Load Games into MemorybyBilliard¶

Many times over the years, users have asked us to implement a way to load games into RAM. Drives are slow, RAM is fast, it seems like a no brainer. However, every time we would respond by telling them that there would be no difference.

For compatibility reasons, Dolphin emulates the disc read rates of GameCube and Wii optical drives, even down to theConstant Angular Velocity. And those drives aretremendously slowby modern standards. The Wii's DVD drive was capable of an up to ~8.5MiB per second transfer rate. An ATA133 hard drive, which uses astandardthat was superseded years before the Wii released, is over ten times faster!

This puppy can get transfers up to 167MiB per second!

Whether anUltra ATA hard drive, a default-speed SD Card, or aMemory Stick, it doesn't matter - they are all faster than a Wii's optical disc drive. Even seek times (the bane of spinning rust) didn't affect Dolphin much, as the seek times of a Wii drive are even worse! Dolphin's game loading haseffectivelynever been bottlenecked by current storage devices, so there was no reason to implement a way to load games into RAM. There was simply no benefit.

Except, for one specific scenario that is becoming increasingly common these days - playing from a hard drive over a network. As people adopt more and more devices, home intranets have become increasingly complex. At the heart of these intranets is often aNetwork Attached Storage (NAS) device. These dedicated storage appliances allow their files to be accessed by any device on the network, and feature large storage capacity, redundancy, and integrity verification - everything needed to be very good at long term digital storage. NASes are perfect for storing things like game disc backups.

Butplaying gamesfrom a NAS in Dolphin has often been an annoying experience. The NAS isn't aware of what some device far away on the network is doing, and since GameCube and Wii games needso little data so infrequently, it may decide to put a hard drive to sleep while someone is actively playing a game that's on it. This results in ahard stutterthe next time the game asks to read the disc, as now Dolphin has to wait for the NAS to wake up the drive. There are ways for NASes to work around issues like this, such as SSD storage pools and RAM caches, but the most common NASes are simple hard drive boxes with little if any caching.

Fortunately, we already knew of a solution that could solve this. All we had to do was provide a way to load the game disc into the host's system memory. When enabled, Dolphin will continuously copy the disc in the background until the entire game is cached in RAM, and then the NAS can turn off the drive whenever it wants and the player will be none the wiser.

We never thought we'd ever actually implement this feature, but sometimes new problems can be solved by old solutions.

You can find this feature in our Qt GUI under Config > General as "Load Whole Game into Memory".

This feature is currently only available in our desktop builds.

#### 2512-403 - Core: Add SDL Hints SettingsbyTixoRebel¶

SDL hints are a useful mechanism that allows Dolphin to tell SDL how to handle certain controllers. Recently, we've been having trouble with some controllers and have been using SDL hints in an attempt to work around them. For example, having an8BitDo Ultimate 2controller plugged in causes Dolphin to hang on shutdown in some cases. To fix this, we disabled SDL's DirectInput support as a temporary remediation. Unfortunately, that also broke hotplug support for DualSense and DualShock 4 controllers. Given that other programs don't seem to be having this issue, it's fairly apparent that Dolphin is doingsomethingwrong, we just don't know what.

Users could modify Dolphin's SDL hints through setting anenvironment variable, but that's not really something the average user knows how to do. SoTixoRebeladded a GUI for enabling certain SDL hints. However, their intended use case wasn't for fixing either of those bugs! They wanted to use SDL hints to change how Nintendo Switch Joy-Cons are handled. By default, SDL will combine a left Joy-Con and a right Joy-Con into one controller. If you want to separate left and right Joy-Cons into two different controllers to emulate the Wii and Nunchuk, you need to use an SDL hint.

Realizing the opportunity to kill two birds with one stone, we hadTixoRebelimplement a way to addanySDL hint directly in the Controller Settings GUI. That way, it could be used for Joy-Con handling, working around the 8BitDo/DS4/DS5 bugs, or anything else the user wants!

At the bottom of the Controllers settings pane of our Qt GUI, there's a new button!

Click it to reveal a number of options for SDL hints.

There's one caveat we should note: changes to SDL hints will only apply after restarting Dolphin. Please keep that in mind when modifying these settings.

#### More Performance PatchesbyBilliard¶

More games have been identified with behaviors that are problematic for Dolphin. For more information on how these patches are made and what they do, please refer to theprevious Progress Report. All of the following games are of the variety that run uncapped internally, and each of them have been patched to force the games to synchronize to theVertical Blanking Interrupt (VBI).

* Need For Speed: Hot Pursuit 2
* Monster 4x4 Stunt Racer
* 4x4 Evo 2
* Rabbids Go Home- Only the NTSC, PAL 1.0 and 1.1 versions are patched. The Japanese and UK specific versions are still unpatched.
* Rabbids Lab
* 007: Quantum of Solace- This particular game suffers even more than others due to the lightweight menus sometimes pushing out thousands of frames per second with Dolphin's improper GPU timings. The problem would subside in busier scenes, but the game was still rendered all but unplayable. It now runs normally.

### This Release's Contributors...¶

Special thanks toall of the contributorsthat incremented Dolphin by 465 commits after Release 2512!
