---
title: Quake Shareware, a CD-ROM just a little too full
url: https://fabiensanglard.net/quake_shareware_cd/index.html
site_name: hnrss
content_file: hnrss-quake-shareware-a-cd-rom-just-a-little-too-full
fetched_at: '2026-08-18T12:12:08.459007'
original_url: https://fabiensanglard.net/quake_shareware_cd/index.html
date: '2026-08-17'
description: Quake Shareware, a CD-ROM just a little too full
tags:
- hackernews
- hnrss
---

Fabien Sanglard - WEBSITE

Aug 17, 2026

Quake Shareware, a CD-ROM just a little too full

In the mid-90s the coolest thing to buy for a PC, besides theincredibly expensive Intel Pentium, was aCD-ROM drive. With their capacity of 640 MiB (three times the storage of PC HDD at the time), CDs allowed enthusiasts to step into
a world of multimedia, made of high-resolution 640x480 256 colors palette-indexed photos[1], VOC soundtracks, and play withVideo For Windowsbutter-smooth 12 fps 240x179 videos[2][3]lasting up to several seconds.

For video game developers, the CD-ROM was an odd beast. The capacity far exceeded the quantity of assets they were able to produce. A few titles, like 7th Guest (1993), Wing Commander III: Heart of the Tiger (1994), or Phantasmagoria (1995)
introduced Full Motion Video (in a world where only part of the screen could be animated). Some added high
quality music. My most memorable take on the matter was from id Software's lead developer, John Carmack.

People expect CD games
to have tons of digitized speech and video [...] The joke here is that if we ever do a CD version of DOOM, you are going to get the
game and “The Making of DOOM” a one hour feature film. 

John Carmack (Jan '94) for “ATARI EXPLORER ONLINE”

A good idea on paper but bad on CD

By June 1996, after three years of hard work, id Software had completed their next title, Quake. As for their previous title, they were going to release both a shareware version and a full version of their game. Since it used a mere 22 MiB of storage, people at id Software had the idea of leveraging the remaining capacity of a CD-ROM. Why not include encrypted versions of the full id catalogue of games? Not only this would cut out the middlemen, it would give instant access to gamers with a simple phone call and a credit card.

The concept was implemented. The CD was announced[4]on July 3, 1996 and released on August 30th[5]. The hacker group GNOMON releasedQuakecrk.ziponly 39 days later[6]. The archive containedQCRACK.EXE, a tool allowing to decrypt every single game on the CD-ROM.

 Quake’s shareware retail
experiment had proved disastrous. In theory id was going to cut out retailers
by allowing gamers to buy the shareware and then call an 800 number to
place an order and receive a password that would unlock the rest of the game.

But gamers wasted no time hacking the shareware to unlock the full version
of the game for free. Worse, all the mundane aspects of distribution and order
fulfillment were spinning out of control. In a desperate measure, id tried to
put the brakes on the retail shareware, but it was too late. They were stuck
with almost 150,000 CDs sitting in a warehouse.

David Kushner (
Masters of Doom
)

So what happened? Let's dive in!

Getting Quake retail shareware CD

Thanks to usenet archives ofrec.games.computer.quake.misc, we have detailed discussions[7]of how it worked. A gamer could go to any of the hundreds of CompUSA/Computer City stores and buy the CD for $9.95.

Inside a CompUSA store (1998) (
source
)

Computer City store (1994) (
source
)
 

Quake Shareware CD
 

The packaging was actually pretty high quality for a shareware product. On my copy, a sticker on the front clarifies this is the "Shareware version" with instructions to call 1-800-669-9342 (or 1-800-ID-GAMES) to unlock the full game.

The phone number is still active today. However you don't reach the unlock center since CompUSA went out of business. The Superstore chain closed between 2007 and 2008. Instead of an unlock operator we get an automated message to sell us elderly stuff.

 

 

Upon contacting the operator, users were to also communicate a "SOURCE CODE". It played no part in generating the Unlock code. It may have been a way for the distributors to claim a transaction fee. Browsing eBay, I found many with names indicative of past/present retailers.12-BSTBYBestBuy,24-CCITYComputer City,22-CUSACompUSA, 88, 11-1111,38-EBElectronic Boutique,44-FTRSPFuture Shop (Canada),34-EGGHEgghead Software, and56-MCTRMedia Play/ Musicland.

How it was intended to work

The first contact was sleek. The GUI was well done. Users could jump directly into Quake Shareware but they could also click onQUAKE UNLOCK.

 

 

The CD-ROM also features anID STUFFsection, allowing to browse the catalogue of id games and unlock any of them. Several versions ofDOOMare there, along withHEXEN, andHERETIC.

 

 

Once the unlock process was started, the GUI generated aCODE NUMBER(which I call CHALLENGE) that was to be communicated to a Service Agent over the phone. Upon paying the fees, anUNLOCK CODE NUMBER(which I call SERIAL) would be received. Checksums on both numbers mitigated issues related to this primitive landline mode of communication.

To avoid replay attacks, the CHALLENGE changes every time the program is run and rotates every 5 min while the GUI is active.

 

 

The screen even had the signature provocative tone of the early days of id Software ("those who are too cheap"). Note that there was also a warning that users should back up the game once unlocked. Since theCHALLENGEincluded some randomness, there was no way to reuse aSERIAL.

 

 

At first sight, the process looked solid. Users had to call an unlock service to obtain a password. And only with that password could the final unlock be completed. So what went wrong?

TestDrive, under the hood

The tool powering the lock/unlock was provided by TestDrive Corp's (archivedwww.testdrive.com). The idea was to give players a way to "try-before-you-buy" and allow them to immediately purchase the full version of a program.

Their encrypter was capable of "denaturing" an.EXEexecutable. It replaced the first 32 KiB with acustom header(attempting to run a denatured executable displayed "This application has been disabled"), renamed the file to.MJ3, encrypted the original header as a.ST3, and issued a seed.

Normal EXE

Denatured MJ3

Chunk ST3

Secret seed

Let's peek inside theQuake shareware CDwith afilemapI generated (Split View recommended). In that tree, we can see oneMJ3file for each game available. We can also see all theST3files inside thePAGEMKRarchive. Everything is there to "renature" anMJ3back into anEXEgame installer, except for the secret "seed" that is assurely derived from the SERIAL.

Described as is, there is no flaw in this process. The secret seed comes from the unlock server, tied to a CHALLENGE/SERIAL that could not be reused. But the hacker team GNOMON found a way.

How QCRACK.EXE works

Released on 10/08/96 (gnomon.nfo), only 39 days after Quake retail shareware CD hit the stores,QCRACK.EXEwas a tool able to generate a SERIAL automatically given theCHALLENGE.

What members of GNOMON group figured out was that theSERIAL received over the phone contained no secret at all. It was just aproof of payment.

TheQUAKE unlockprogramFLOW.EXEthat ships on the CD is capable of generating the SERIAL from the CHALLENGE on its own. All it does is check that its own locally-generated SERIAL and the SERIAL entered by the user match! The entire protection mechanism relies onsecurity by obscurity.

The pipeline from CHALLENGE to SERIAL is convoluted but was reversed in 2016 by rmolina[8].

1. The 11-digit CHALLENGE is split into a 4-digit GAME-ID, and a 7-digit number resulting in an OFFSET, and a DEPTH.
2. The GAME-ID indexes an encrypted databaseSKU.17, which gives a codename (e.g.: doom2).
3. The CODENAME allows to retrieve a 512-byte DOC file (e.g.: DOOM2.DOC) inside theFLOWLIB.LIBarchive.
4. Mixed with the CODENAME and the string"Testdrive Corp.", the DOC transforms a 508-byte hard-coded table into a table of 254 16-bit values unique to the title.
5. DEPTH and OFFSET walk that table backwards, XOR-ing DEPTH to generate a single 16-bit value MEM.
6. The SERIAL is thenunlock = ((reverse7(GAME_ID) + MEM + 0x18) & 0x7F)
 + 0x83 * ((MEM ^ 0x1EA3) + 0x1700A1)printed with a leadingB.

The many more flaws

The more I researched the matter, the more it looked like whoever was in charge had no time to polish the result.

 Never attribute to malice what you can attribute to stupidity. And never attribute to stupidity what you can attribute to time pressure.
 
Fab's Razor

Digging insideQuake shareware CDreveals many more issues.

* Some parts of the unlock system look like they were never tested. Final DOOM cannot be unlocked by calling the unlock center because of a bug. The GAME-ID for "Final Doom" is 12. There is a typo in SKU.17 which makes GAME-ID 12 correspond to CODENAME "Final" (with a capital F). This makes the SERIAL generation retrieve the wrong DOC. The correct value was "final". This created an only-too-familiar situation where illegitimate users enjoyed a better experience than paying customers.
* The step-by-step summary mentions an encryptedSKU.17file. There is a plain-text version, completely unencrypted, of the very same file namedSKU.TXTinside theFLOWDIRarchive. There are many more TXT files matching their.17encrypted versions (PRODUCT.TXT, EXE.TXT).
* Several files are temporaries (DM.TMP), editor artifacts (FLOWWORK.BAK), or not used at all (ENCRYPT.EXE).
* The library format is not encrypted or scrambled. Figuring out the.DIRformat offered low resistance and easy access to all DOC files necessary to generate SERIALs.

References

^[1]MediaPack 10-CD Roms^[2]MediaPack Tropical Rainforest^[3]MediaPack Wild Places^[4]Quake' Is Here^[5]When will it be available in stores (rec.games.computer.quake.misc)^[6]gnomon.nfo^[7]Question about Quake Shareware CD (rec.games.computer.quake.misc)^[8]Quake, TestDrive y Qcrack

 

*