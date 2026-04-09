---
title: Downtown Doug Brown » Finding a 27-year-old easter egg in the Power Mac G3 ROM
url: https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/
site_name: hackernews_api
fetched_at: '2025-06-24T23:06:44.901942'
original_url: https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/
author: zdw
date: '2025-06-24'
description: Finding a 27-year-old easter egg in the Power Mac G3 ROM
tags:
- hackernews
- trending
---

# Downtown Doug Brown

## Thoughts from a combined Apple/Linux/Windows geek.

* Home
* About
* Mac ROM SIMMs
* Software
* Microcontroller lessons
* Contact

Jun

24

## Finding a 27-year-old easter egg in the Power Mac G3 ROM

Doug Brown

Classic Mac
,
Reverse engineering

2025-06-24

I was recently poking around inside the original Power Macintosh G3’s ROM and accidentally discovered an easter egg that nobody has documented until now.

This story starts with me on a lazy Sunday usingHex Fiendin conjunction withEric Harmon’s Mac ROM template (ROM Fiend)to look through the resources stored in the Power Mac G3’s ROM. This ROM was used in the beige desktop, minitower, and all-in-one G3 models from 1997 through 1999.

As I write this post in mid-2025, I’m having a really difficult time accepting the fact that the Power Mac G3 is now over 27 years old. Wow!

While I was browsing through the ROM, two things caught my eye:

First, there was a resource of typeHPOEwhich contained a JPEG image of a bunch of people, presumably people who worked on these Mac models.

This wasn’t anything new;Pierre Dandumont wrote about it back in 2014. However, in his post, he mentioned that he hadn’t figured out how to display this particular hidden image on the actual machine. Several older Macs have secret keypress combinations to show similar pictures, but the mechanism for displaying this one was a complete mystery.

The second thing I found was a big clue: I kept looking for other interesting information in the ROM, and eventually I stumbled uponnittresource ID 43, named “Native 4.3”. Thanks toKeith Kaisershot’s earlier Pippin research, I was quickly able to conclude that this was the PowerPC-native SCSI Manager 4.3 code. The SCSI Manager wasn’t what piqued my interest about this resource though. At the very end of the data, I found some interesting Pascal strings:

These strings were definitely intriguing:

* .Edisk
* secret ROM image
* The Team

The “secret ROM image” text in particular seemed like it could be related to the picture shown above. I decided to dive deeper to see if I could figure out why the SCSI Manager contained these strings, in the hopes that I could solve the mystery. Would this be the clue I needed in order to figure out how to instruct the Power Mac G3 to display this picture?

Some quick Internet searching for the phrase “secret ROM image” revealed thatit had been used for easter eggs with earlier PowerPC Macs. On those machines, you just had to type the text, select it, and drag it to the desktop. Then, the picture would appear. That approach didn’t work on the G3.

I suspected there was some similar way to access this hidden image, but nobody had documented it, at least not as far as I could find. So I had no choice but to disassemble the code and see where this text was used. What is it with me and all these crazy rabbit holes?

I extracted the entirenittresource ID 43 to a file and inspected it:

$ file nitt43
nitt43: header for PowerPC PEF executable

That wasn’t too surprising, considering that the first twelve bytes were “Joy!peffpwpc”. I fed this entire file intoGhidra, which immediately recognized it as a PEF file and had no trouble loading it. Although I’m pretty familiar with reading x86 and ARM assembly, I know essentially nothing about PowerPC assembly code. Thankfully, Ghidra’s decompiler worked very well with this file.

There was one problem, though: it didn’t detect any references to the “secret ROM image” string, other than inside of a huge list of pointers to variables. After scratching my head a little bit, I realized that Ghidra wasn’t doing a great job of finding references to several variables. Luckily, running Auto Analyze a second time after the initial analysis seemed to help it find several more references to things, including all of the strings I was interested in! I didn’t change any options with the analyzer; it just found more stuff on the second run.

The function that used all of these strings was definitely doing something with the .EDisk driver, which I already knew was the RAM disk driver because of past hackery. It seemed to be usingstrncmp()to see if a string was equal to “secret ROM image”, and if so, it would create/open/write a file named “The Team”.

I cleaned up this decompilation quite a bit by giving names to variables and figuring out data types. Fortunately, a lot of the functions likePBGetVInfoSync()had lots of public documentation, so I just had to tell Ghidra about the various Mac Toolbox structs being used.

Okay, that’s a lot easier to understand!

I couldn’t figure out how to format the 32-bit function arguments such as 0x48504f45 into four-letter codes likeHPOE, so that’s what the comments are. Ghidra simply wouldn’t let me display them as ASCII in the decompilation no matter what I did, even though hovering over the constant showed a tooltip with the equivalent text. This is easy to do in IDA, but I couldn’t figure out how to convince Ghidra to do it. I tried Set Equate, but it didn’t change anything. If someone knows how to make it work, I’d love to hear how!

Anyway, the decompiled code shown above makes sense, and here’s a summary of what it does:

* It looks for a driver called .Edisk. (The driver is really named .EDisk, but I guess Mac OS doesn’t care about case sensitivity for this.)
* It finds a disk associated with that driver (the RAM disk).
* It looks for a volume associated with that disk.
* If the volume is named “secret ROM image”:It loadsHPOEresource ID 1, which contains the JPEG image data.It creates a file of creatorttxtand typeJPEGcalled “The Team”.It opens the file, writes the JPEG data to it, and closes it.Then it does something with the driver control entry that I didn’t bother trying to understand further.
* It loadsHPOEresource ID 1, which contains the JPEG image data.
* It creates a file of creatorttxtand typeJPEGcalled “The Team”.
* It opens the file, writes the JPEG data to it, and closes it.
* Then it does something with the driver control entry that I didn’t bother trying to understand further.

Okay, interesting! So this code was clearly looking for the RAM disk to be named “secret ROM image”, but I wasn’t sure exactly how to trigger it. This function was only ever called in one other place: another function, which was checking to see if its first argument was equal to the value 0x3DA (decimal 986).

I didn’t have my beige G3 handy for tinkering, so instead, I mentioned what I had discovered in #mac68k on Libera.^alex came to the rescueafter playing around in Infinite Mac with the hints I had given. They quickly figured out that the trick was to format the RAM disk, and type the special text into the format dialog:

I got out my desktop G3, tested it out on real hardware, and sure enough, it worked! If you want to try it for yourself just like ^alex did, you canrun Infinite Mac in your browser using this link, which sets up an emulated beige G3 running Mac OS 8.1using DingusPPC. There’s a quirk that causes it to fail to resolve an alias at startup. I intentionally disabled it; just click Stop when the error pops up. Here are instructions:

* Enable the RAM Disk in the Memory control panel.
* Choose Restart from the Special menu.
* After the desktop comes back up, select the RAM Disk icon.
* Choose Erase Disk from the Special menu.
* Type thesecret ROM imagetext exactly as depicted above.
* Click Erase.

When you open the newly-formatted RAM disk, you should see a file named “The Team”:

If you double-click the file, SimpleText will open it:

Based on various people’s tests, including my own, it sounds likethis trick works all the way up through Mac OS 9.0.4, but 9.1 may have been the first version where it finally stopped working.

As far as I have been able to determine, this particular secret was undiscovered until now. People definitely knew the image was there in the ROM, but nobody had figured out how to actually activate it. This is probably one of the last easter eggs that existed in the Mac prior toSteve Jobs reportedly banning them in 1997 when he returned to Apple. I wonder if he ever knew about this one?

Special thanks to ^alex for figuring out that the RAM Disk needed to be erased in order to activate the easter egg! I’m not sure I would have thought to try that, and it would have taken a lot more work to trace through the rest of the code to figure it out.

If you are reading this post and you were on “The Team”, I’d love to hear about it! I’m curious if anyone who worked at Apple in the era remembers this little secret.


				Address:
https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/

«
Modifying an HDMI dummy plug’s EDID using a Raspberry Pi

1. Doug Brown Found a Power Mac G3 Rom Easter Egg Nearly 30 Years After Launch - 512 Pixels@2025-06-24 06:35[…] Doug Brown Found a Power Mac G3 Rom Easter Egg Nearly 30 Years After Launch → […]
2. Anon@2025-06-24 07:28What about the “Break at Event Match – Native” part?
3. Ben Shelton@2025-06-24 08:26FYI, the Ghidra bug for not displaying the FourCC strings properly is here:https://github.com/NationalSecurityAgency/ghidra/issues/5209I filed it a couple of years ago and it hasn’t been fixed yet, and I haven’t had the cycles to fix it myself.
4. pete twentythree@2025-06-24 11:16super cool – and thanks for the spur to verify that infinitemac works perfectly on an ipad in the bath:-)
5. ^alex@2025-06-24 12:48@anon “Break at Event Match – Native” doesn’t seem easter-eggy, it’s more likely a debugging feature for the SCSI manager.
6. Doug Brown@2025-06-24 15:23^alex is right, that was a separate string used by a different function, totally unrelated to the easter egg. At first glance in a hex editor, it confused me because I thought it was a big string like “The Team Break at…” but then Ghidra set me straight. Also you can see the 0x1D after The Team.Thank you Ben! It’s good to know I’m not going crazy with Ghidra’s lack of FourCC support.Haha, very cool you got it working on an iPad, pete!

### Add your comment now

Name (required)

Email (Will NOT be published) (required)

URL

Δ

* ## Subscribe
* ## Recent PostsFinding a 27-year-old easter egg in the Power Mac G3 ROMModifying an HDMI dummy plug’s EDID using a Raspberry PiPlease don’t ship heavy, fragile vintage computers. They will be destroyed.How I fixed the infamous Basilisk II Windows “Black Screen” bug in 2013Apple’s long-lost hidden recovery partition from 1994 has been foundThe gooey rubber that’s slowly ruining old hard drivesThe invalid 68030 instruction that accidentally allowed the Mac Classic II to successfully boot upEasy repair of a defective NZXT Signal 4K30 capture card
* Finding a 27-year-old easter egg in the Power Mac G3 ROM
* Modifying an HDMI dummy plug’s EDID using a Raspberry Pi
* Please don’t ship heavy, fragile vintage computers. They will be destroyed.
* How I fixed the infamous Basilisk II Windows “Black Screen” bug in 2013
* Apple’s long-lost hidden recovery partition from 1994 has been found
* The gooey rubber that’s slowly ruining old hard drives
* The invalid 68030 instruction that accidentally allowed the Mac Classic II to successfully boot up
* Easy repair of a defective NZXT Signal 4K30 capture card
* ## CategoriesBug fixes(6)Chumby 8 kernel(13)Classic Mac(14)Computer repair(10)Electronics repair(8)iOS(3)Linux(44)Mac ROM hacking(11)Microcontroller lessons(11)Microcontrollers(4)Product reviews(5)Python(1)Qt(5)Reverse engineering(4)Uncategorized(20)Windows(8)
* Bug fixes(6)
* Chumby 8 kernel(13)
* Classic Mac(14)
* Computer repair(10)
* Electronics repair(8)
* iOS(3)
* Linux(44)
* Mac ROM hacking(11)
* Microcontroller lessons(11)
* Microcontrollers(4)
* Product reviews(5)
* Python(1)
* Qt(5)
* Reverse engineering(4)
* Uncategorized(20)
* Windows(8)
* ## ArchivesJune 2025(2)May 2025(2)March 2025(2)January 2025(2)December 2024(1)November 2024(1)October 2024(2)September 2024(1)August 2024(1)July 2024(3)June 2024(4)May 2024(1)April 2024(2)December 2023(1)November 2023(2)September 2023(3)August 2023(3)June 2023(1)May 2023(1)April 2023(1)March 2023(2)January 2023(1)December 2022(3)August 2022(1)May 2022(2)March 2022(1)December 2021(1)June 2021(1)April 2021(1)January 2021(1)September 2020(1)August 2020(1)July 2020(1)May 2020(1)June 2019(1)April 2019(1)December 2018(1)August 2018(1)May 2018(1)April 2018(3)February 2018(1)October 2017(1)July 2017(1)May 2017(3)March 2017(1)October 2016(1)June 2015(1)March 2015(1)November 2014(1)August 2014(3)July 2014(1)April 2014(1)March 2014(1)February 2014(1)November 2013(1)August 2013(1)June 2013(3)April 2013(1)March 2013(1)January 2013(2)December 2012(2)August 2012(1)July 2012(2)June 2012(1)May 2012(1)February 2012(3)January 2012(1)November 2011(1)October 2011(2)August 2011(3)May 2011(1)April 2011(1)March 2011(2)November 2010(2)October 2010(3)July 2010(5)
* June 2025(2)
* May 2025(2)
* March 2025(2)
* January 2025(2)
* December 2024(1)
* November 2024(1)
* October 2024(2)
* September 2024(1)
* August 2024(1)
* July 2024(3)
* June 2024(4)
* May 2024(1)
* April 2024(2)
* December 2023(1)
* November 2023(2)
* September 2023(3)
* August 2023(3)
* June 2023(1)
* May 2023(1)
* April 2023(1)
* March 2023(2)
* January 2023(1)
* December 2022(3)
* August 2022(1)
* May 2022(2)
* March 2022(1)
* December 2021(1)
* June 2021(1)
* April 2021(1)
* January 2021(1)
* September 2020(1)
* August 2020(1)
* July 2020(1)
* May 2020(1)
* June 2019(1)
* April 2019(1)
* December 2018(1)
* August 2018(1)
* May 2018(1)
* April 2018(3)
* February 2018(1)
* October 2017(1)
* July 2017(1)
* May 2017(3)
* March 2017(1)
* October 2016(1)
* June 2015(1)
* March 2015(1)
* November 2014(1)
* August 2014(3)
* July 2014(1)
* April 2014(1)
* March 2014(1)
* February 2014(1)
* November 2013(1)
* August 2013(1)
* June 2013(3)
* April 2013(1)
* March 2013(1)
* January 2013(2)
* December 2012(2)
* August 2012(1)
* July 2012(2)
* June 2012(1)
* May 2012(1)
* February 2012(3)
* January 2012(1)
* November 2011(1)
* October 2011(2)
* August 2011(3)
* May 2011(1)
* April 2011(1)
* March 2011(2)
* November 2010(2)
* October 2010(3)
* July 2010(5)
* ## Spam Blocked276,259 spamblocked byAkismet

Downtown Doug Brown
 ·
coogee theme
 · 2008 ·
Privacy Policy

RSS Feed
 ·
WordPress
 ·
TOP
