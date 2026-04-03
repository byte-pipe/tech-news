---
title: System 7 natively boots on the Mac mini G4!
url: https://macos9lives.com/smforum/index.php?topic=7711.0
site_name: hackernews
fetched_at: '2025-11-29T19:06:55.525658'
original_url: https://macos9lives.com/smforum/index.php?topic=7711.0
author: ibobev
date: '2025-11-29'
description: System 7 natively boots on the Mac mini G4!
---

* November 29, 2025, 11:06:55 AM
* Welcome,Guest

					Please
login
 or
register
.

1 Hour

1 Day

1 Week

1 Month

Forever

					Login with username, password and session length


 


### News:

* Mac OS 9 Lives>
* Mac OS 9 Discussion>
* Mac OS 9, Hacks & Upgrades>
* Mac OS 9 on Unsupported Hardware(Moderator:ssp3) >
* System 7 natively boots on the Mac mini G4!

Pages: [
1
]   
Go Down

* Print

### AuthorTopic: System 7 natively boots on the Mac mini G4!  (Read 48290 times)

#### Jubadub

* 512 MB
* Posts: 525
* There is no Mac in OS X

##### System 7 natively boots on the Mac mini G4!

«
 on:
 November 27, 2025, 10:13:03 AM »

(And Mac OS 8!)
Hey, guys!
Surely y'all know and have enjoyed Mac OS 9.2.2 booting and beautifully-running on all four Mac mini G4 models for close to 8 years now. (Wow!)
Well, that was one massive revolution...
... But most of us did not think we would live to see the day New World ROM machines, even more so the likes of the Mac mini G4, to NATIVELY boot System 7:
(Gotta love it trying to display 1 GB RAM capacity.)
Before your eyeballs leave your eyesockets completely, I ought to warn that there's still much to be sorted out in this, especially sound, video and networking (the usual suspects). In other words, your mileage may vary, so keep expectations in check!
========================================================
OK, so HOW in the WORLD is any of this possible?
========================================================
It turned out "New World ROM" Macs had a cousin born out of the clone program (until the usual villain, Steve Jobs, came and killed it), which was an architecture called "
CHRP
" (pronounced "chirp"). It was the successor to
PReP
, but, unlike PReP, Mac OS was also going to be officially-bootable on it. Close to no CHRP machines ever saw the light of the day, thanks to Jobs' return. Nonetheless, Apple internally developed Mac OS 7.6 ~ 8.0 for CHRP systems before it got axed. It's just that they never released it, but the development was done regardless. On October 2025, it turned out someone preserved some of these Mac versions, which were then acquired and preserved and shared with the world. (
Macintosh Garden link
,
archive.org link
.)
Although CHRP was left to die, the so-called "New World ROM" Macs inherited much of its architecture and design. As you probably know, these Macs rely on an extra system file called "Mac OS ROM", whereas "Old World ROM" Macs do not need it, and can use their own actual ROM to get Mac OS going. This meant any Mac OS version unaware of the concept of a Mac OS ROM file could not just simply boot in a New World ROM Mac normally. People were able to boot Mac OS versions as low as 8.1, but not any lower, and that too only for the very first few New World ROM Macs, but none of the later ones, which increasingly had a higher and higher minimum OS version.
But not anymore, as the following major events happened:
- The recent Mac OS 8.0 CHRP leaks provided an earlier ROM file that, it turns out, allows regular Mac OS 8.0 to boot, as well. Or, alternatively, the Mac OS ROM file that always worked with Mac OS 8.1 also worked on these Mac OS 8.0 CHRP releases. (Exact details are fuzzy in my memory by now, so someone else might want to correct me if I got something wrong.)
- The recent Mac OS 7.6 CHRP leak provided an additional System Enabler file, which could be exploited for loading Mac OS ROM files. I forget if that's how it worked out-of-the-box, or if a bit of hacking to the System Enabler was required for that, however what I do remember clearly is that, while the System Enabler was hardcoded so that artifically no OS earlier than 7.6 could use it, the OS version check could be patched out of it, so that System 7.5.x (and potentially earlier) can also use it.
In other words,
this file is the reason that earlier Mac OS versions can make use of the Mac OS ROM file
, thus bringing Mac OS 7.6.1 and earlier potentially to ALL New World ROM Macs!
(Trivia tidbit: Apparently this enabler was also present in certain archives of the Mac OS 8.0 betas from when it was still known as "Mac OS 7.7". Oops! This thing was right under our nose all this while!)
- Of course, as hinted at previously, a System Enabler _alone_ is NOT enough to boot System 7 and the like when even much newer systems that were already aware of the Mac OS ROM file could not boot. The newer the model of the New World ROM Mac, the less you could actually "go back". The reason is simple: Mac OS ROM files, over time through its various versions, would get new features added, BUT also would remove older ones which were required by older OS versions. The solution? Using
ELN's great Mac OS ROM patching tools
 (plus other tools of his own), "Rairii" AKA "Wack0", known for his amazing PPC Windows NT 3.51 / NT 4.0 project on
PowerMacs
 and the
Nintendo GC / Wii / Wii U
, analyzed many of these Mac OS ROM files, and fixed + patched + stitched together new Mac OS ROM files that attempt to keep ALL the old features that were removed AND all the new features that were added. In other words, the ultimate Mac OS ROM file that boots everything and runs everything (roughly-speaking). He also is the one who figured out and hacked the System Enabler to also accept OSes earlier than Mac OS 7.6.
Keep in mind, however, that this effort essentially allows Macs that are already able to boot SOME version of Mac OS to ALSO boot older versions. But if a given machine cannot boot ANY Mac OS version, such as the two DLSD PowerBook G4s (
15"
,
17"
), these patches cannot do anything about that: Their incompatibilities need to be addressed first and separately.
One more interesting thing to note about the similarity between CHRP systems and New World ROM Macs: If you check ANY "Mac OS ROM" file to see its TYPE and CREATOR codes, you will see they are "tbxi" and, you guessed it, "
chrp
", respectively. I couldn't believe "chrp" was in ALL the Mac OS ROM files all these years!
========================================================
Where can I get ahold of this EPIC stuff ? ? ? ? ?
========================================================
Rairii's "super" ROMs are available on
this GitHub repository
, under
releases
. You may also fetch the patched System Enabler for Mac OS 7.6.1 and earlier from there, and place it in the System Folder. Make sure to download the files from the latest release there.
Note that he applied his patches to 3 different versions of the (US) ROMs:
- 10.2.1 with CPU Software 5.9: The "latest and greatest" Mac OS ROM file of all Mac OS. For reference, this is also the ROM version that the
1.628 GB max RAM Mac OS ROM we have was based on (thus going beyond the 1.5 GB limit)
, although do note that the RAM limit break patches are NOT included in this, at least not yet as of the time of writing.
- 2.5.1: A much earlier version of the ROM, but still new enough to support USB. See the GitHub page for details.
- 1.7.1: A very early ROM, which can be well-leveraged by very early New World ROM Macs. See the GitHub page for details.
Note you need ROM version 9.1 or higher to use ATA-6 AKA Ultra ATA/100 AKA Kauai drivers, which are essential on the likes of the Mac mini G4 and the MDD. Special notes for the Mac mini G4 are further down.
========================================================
What is the COMPLETE list of Mac OS versions that now boot?
========================================================
To be exact, this is the complete list of OSes I have attempted, all on the Mac mini G4 1.5GHz model, with the following results:
- System 6.0.8:
No boot
. You get a Happy Mac, followed by a blinking question mark in a floppy icon. (Note: Although this very attempt is UTTERLY insane for multiple technical reasons, it might be not AS seemingly-impossible as one may think, as the 68k emulator resides within the Mac OS ROM file.)
- System 7.0:
No boot
. You get a Happy Mac, but then a warning window pops up saying System 7.0 cannot boot on this computer.
- System 7.1.2:
No boot
. You get a Happy Mac, but then a warning window pops up saying System 7.1 cannot boot on this computer.
- System 7.5:
BOOTS AND IS STABLE
. It requires you to hold shift to turn Extensions (and Control Panels / INITs) off, though, or to get rid of the "Mouse" Control Panel (and possibly more). The system is surprisingly stable! I tested the British version of this one, as Apple's Mac OS Anthology discs did not include the US installers, for some very slacker-y reason.
- System 7.5.2:
Boots, but very broken, close to nothing works
. It could be because System 7.5.2 was always VERY machine-specific, and is apparently one of the most broken versions of Mac OS of ALL time, regardless. The machine-specific enablers, and other things, might be what is making it so unstable.
- System 7.5.3:
BOOTS AND IS STABLE
. It requires you to hold shift to turn Extensions (and Control Panels / INITs) off, though, or to get rid of the "Mouse" Control Panel (and possibly more). The system is surprisingly stable!
- Mac OS 7.6:
BOOTS AND IS STABLE
. Holding shift is not required here. What else can I say? It "works".
- Mac OS 8.1:
BOOTS AND IS STABLE
. Holding shift is not required here, either. Behaves much the same as the others, except we now have HFS+ by default. Still, it did NOT like me having a 940 GB HFS+ partition, and prompted me to either eject it or format it. (To be fair, older OSes tried to do that, too, but Mac OS 8.1 was THE OS to _officially_ be able to handle HFS+ properly, so there are no excuses for it to fail here. Mac OS 9.2 ~ 9.2.2 all work perfectly with it.)
- Mac OS 8.5: No boot. Rather, it seems like it WOULD boot, but starting with Mac OS 8.5, Mac OS now always checks to see if the machine you are booting from is within a list of Apple-endorsed machine IDs for the given Mac OS version. In other words, Mac OS 8.5 does not know what the Mac mini G4 is, nor what a G4 Cube is (our Mac mini G4 ROM file makes the mini pretend to be the latter). It seems it should be possible to patch out the machine check. According to Rairii, this should be able to be patched out by disabling such a check on the "boot" resource in the Resource Fork of the System file, in ID 3 (also known as "boot3"). For Mac OS 8.6, it seems like this check happens at the end of boot3, wherever a check for machine ID 406 is located, in which after it's detected, the code checks to see if the exact Mac model is whitelisted or not.
- Mac OS 8.5.1:
No boot
. All that applies to Mac OS 8.5 also applies to Mac OS 8.5.1.
- Mac OS 8.6:
No boot
. It crashes during the start screen, when the loading bar appears, but before the first extension gets to load. See the top-left corner of the picture for a glitchy visual artifact. Same happens if you try to boot with Extensions off.
- Mac OS 9.0.4: No boot. It crashes during the start screen, when the loading bar appears, but before the first extension gets to load. Same happens if you try to boot with Extensions off. Exact same symptoms as when trying to boot Mac OS 8.6 at least on this mini model, including the visual artifact on the top-left corner.
- Mac OS 9.1:
No boot
. It crashes during the start screen, when the loading bar appears, but before the first extension gets to load. Same happens if you try to boot with Extensions off. Exact same symptoms as when trying to boot Mac OS 8.6 and Mac OS 9.0.4 at least on this mini model, including the visual artifact on the top-left corner.
- Mac OS 9.2 ~ 9.2.2: BEST OS EVER, BOOTS AND RUNS BEAUTIFULLY. 'Nuff said.
Note that, although I describe many of these as "stable", I mean you can use much of it normally (sound/video/networking aside) without it crashing or misbehaving, at least not too hard, but that is not to say everything works, because that is just not the case. For example, when present, avoid opening the Apple System Profiler, unless you want a massive crash as it struggles trying to profile and gather all the information about your system. Some other apps or Control Panels might either not work, or work up to a certain point, after which they might freeze, requiring you to Force Quit the Finder to keep on going. And so on.
As you can see, I did not yet try System 7.5.5, Mac OS 7.6.1 and Mac OS 8.0. That's because they all are most likely working exactly as their neighbouring versions. But feel free to confirm.
Most non-mini systems should be able to boot Mac OS 8.6 ~ Mac OS 9.1 just fine. A "Mac OS 8.6 Enabler", so to speak, by LightBulbFun, can be renamed as e.g. "Sawteeth" and put inside the System Folder for some machines that cannot boot Mac OS 8.6 normally, so that they can, then, boot it. It is actually a Mac OS ROM file, but can function as a complementary, helper file to aid the actual Mac OS ROM file in this case. If you'd like, check
here
 for more info. I have attached "Sawteeth.bin" to this post for convenience. LightBulbFun first shared it on
this post
, specifically through this
MEGA link
.
Most non-mini systems should also be able to boot Mac OS 8.5 and 8.5.1, especially on G3s and earlier. Some G4 Macs might need to spoof the Mac model in Open Firmware (or some other Forth script added to ROM) to boot, though, or patch the check out like I mentioned for the mini earlier. The reason the mini doesn't have the spoofing as an option is that any spoofing in OF would be overwritten by its own specialized Mac OS ROM, which spoofs a G4 Cube, which is clearly not in the whitelist of supported machines for Mac OS 8.5 and 8.5.1.
Also note that the mini behaves as reported above with Mac OS 8.6 with or without this "8.6 enabler" file (and with or without the System Enabler for Mac OS 7.6.1 and earlier, both of which don't seem to get in the way of later, nor earlier, OSes).
Most importantly, I did
not
 yet attempt to identify which are the latest versions of each Control Panel and Extension for each of these OSes. If I did, I'm sure it would help a lot, and perhaps address quite a number of these problems. The more people chime in on this effort, the better! Imagine if we had a proper "Mac mini G4 System 7.5.5" CD, then an "MDD Mac OS 8.5.1" CD, then an "iBook G3 Mac OS 7.6.1" CD, and so on. Everyone with a G3 or G4 Mac can help by trying things out!
Namely, something akin to MacTron's efforts highlighting the latest Extensions for Mac OS 9.2.2 and Mac OS 8.6 like this, but also for every other Mac OS version:
========================================================
But how did you get the mini to boot? It requires its own special ROM!
========================================================
Indeed it does! All credit goes to ELN and all of those who helped him on Mac OS 9 Lives!: you can simply use his tooling (which was also very useful for Rairii) to re-apply the Mac-mini-G4-specific ROM patches to Rairii's latest 10.2.1 ROM, and voila! It works as well as you would hope it to!
You can even use the resulting ROM for Mac OS 9.2.2, as well, even though you don't have to: Originally, the Mac mini G4 ROM as we see them in RossDarker's Mac mini G4 CDs version 8 and 9 (AKA v8 and v9), as well as in all the previous versions, were based on the US ROM v9.6.1. I could not find an explanation as to why ROM v10.2.1 wasn't used in the end, even when digging the old Mac mini G4 thread again that started it all. Perhaps because we already had a working ROM with v9.6.1 and did not want to risk breaking anything, or who knows. However, I have thoroughly tested Mac OS 9.2.2 with this new ROM combination (latest Rairii 10.2.1 + latest Mac mini G4 patches AKA v9 patches), and from what I could tell, everything behaves
exactly
 the same as with the previous ROM we always used. Except now we have the ability to use the same ROM to also boot System 7.5 (I still can't believe this, even though it is true).
(For the record, while the 9.6.1 ROM was also modified to spoof the Mac mini G4 model identifier as a G4 Cube, we also tried to spoof it as a QuickSilver 2002 at one point, but someone reported sound issues with that, and so it was quickly changed back to a G4 Cube and such a change never made it into one of RossDarker's CDs. So just about everyone using Mac OS on the mini for all these years has had a ROM reporting to the OS as a G4 Cube, exclusively.)
To apply the Mac mini G4 patches, I used ELN's
tbxi
 and
tbxi-patches
 to apply his "macmini.py" script. You can follow the instructions as per the tbxi-patches page, which you should not let intimidate you even if you are not used to this kind of thing. It's quick and easy, and the scripts are also fully-commentated very nicely by ELN if you are curious about what it is doing and why.
In my case, first I tried using the latest Python 3.13.9 both from Windows 7 (bad idea due to resource fork loss) and macOS 10.14.6 Mojave, but neither worked: it seems like that version of Python was just too new. I then retried with
Python 3.8.10
 instead (which I chose thinking it might be more period-appropriate for the script's age) on Mojave, which worked
flawlessly
. I didn't try it, but perhaps an older Python version might work on PowerPC OS X, as well.
I used the Python installer
from the official website
, and I also used an "official" Git installer from
here
 (thus avoiding any package manager headache... man, how I hate non-Mac-OS systems, including OS X, and package managers in general...)
If somehow someone with plenty of Python knowledge and the willingness to put enough time into it wished to, both tbxi and tbxi-tools could, perhaps, be ported to
MacPython 2.3.5
, so that we could do all this patching from Mac OS 9.2.2 directly and natively without leaving our main OS. That would also be awesome! (Of course, it helps that this is also available on more recent systems nonetheless, because then everyone gets to join in on the fun with all kinds of different backgrounds and setups.)
For convenience, I attached the final patched ROM to this post, so that anyone can go wild on their minis right away!
========================================================
Why should I care when Mac OS 9.2.2 already boots, and runs better?
========================================================
It is also my opinion Mac OS 9.2.2 is the greatest OS, and Mac OS, ever, but not everything that is possible in earlier Mac OS versions is possible in Mac OS 9.2.2. For example, some software requires Mac OS 9.0.4 or earlier to work. A lot of software is System-7-exclusive.
Some people also just prefer the likes of System 7 for its even-lighter memory footprint, lack of mandated Appearance Manager and the like. Mac OS 9.2.2 is already overkill-fast on the mini, and on most New World ROM Macs, but the likes of System 7.5 are just RIDICULOUSLY fast. Even more ridiculously. I still am trying to come into terms with how indescribably fast using it on the mini was. It got even faster when I thought there was no way to get "faster than instantaneous", as Mac OS 9.2.2 always felt instantaneous like no other system already!
People might also have some other kind of reason and/or special attachment to an earlier OS version. Or maybe people want to explore older OS APIs and behaviors, perhaps even make a new application they want to know how it will behave on bare-metal not just on Mac OS 9, but also System 7 etc..
The value is in opening up the doors that give us, the users, more options that help us all out.
========================================================
Final remarks
========================================================
Above all, thank you to everyone that made this possible. But I wanted to emphasize and give special thanks to Rairii for engineering all these ROMs, Mac84 for archiving and sharing all the CHRP discs, ELN for engineering all the Mac mini G4 ROM compatibility scripts and creating all the ROM and other Mac OS tooling, and to the Mac community at large everywhere that assisted in all of this into becoming reality. There's honestly many, many people to thank we owe over this one way or another, both in small and big ways.
I can't wait to see what people will do with all these new Mac OS versions on their New World ROM systems over the course of time!

						«
Last Edit: November 27, 2025, 11:24:38 AM by Jubadub
 »


						Logged


#### Jubadub

* 512 MB
* Posts: 525
* There is no Mac in OS X

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #1 on:
 November 27, 2025, 10:28:21 AM »

For the record, I posted this on all these 3 places for greater reach:
-
Here
 (where the Mac mini G4 ROM is);
-
Macintosh Garden
;
-
System 7 Today
.
These posts were also linked to from the following places, with discussions of their own:
-
MacRumors PPC
;
-
68kMLA
.
I'm mentioning this here in case anyone wants to quickly jump to discussions happening on either side of the isle.
EDIT: For some reason I seem unable to make posts with attachments (they just erase my message and prompt me to start a new topic), so I'm trying to see what file upload service I should use for the Mac mini G4 ROM that boots System 7 (and the "Sawtooth.bin" file).
I'd rather not create a Garden page just for this just yet as this project is still in its infancy, so any Mac-friendly file upload service recommendations would be appreciated.
EDIT 2: Ah, I got it figured out: Attachments cannot be ".bin" nor ".hqx"... This should change... I repackaged the contents as ".sit" for now and put them up in the first post, as intended.

						«
Last Edit:
Today
 at 02:14:33 AM by Jubadub
 »


						Logged


#### n8blz

* 8 MB
* Posts: 13
* New Member

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #2 on:
 November 27, 2025, 03:28:43 PM »

Quote from: Jubadub on November 27, 2025, 10:13:03 AM
I have thoroughly tested Mac OS 9.2.2 with this new ROM combination (latest Rairii 10.2.1 + latest Mac mini G4 patches AKA v9 patches), and from what I could tell, everything behaves
exactly
 the same as with the previous ROM we always used.
Long shot, but, is the mouse-freezing bug still present?

						Logged


#### Jubadub

* 512 MB
* Posts: 525
* There is no Mac in OS X

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #3 on:
 November 27, 2025, 10:46:15 PM »

Quote from: n8blz on November 27, 2025, 03:28:43 PM
Quote from: Jubadub on November 27, 2025, 10:13:03 AM
I have thoroughly tested Mac OS 9.2.2 with this new ROM combination (latest Rairii 10.2.1 + latest Mac mini G4 patches AKA v9 patches), and from what I could tell, everything behaves
exactly
 the same as with the previous ROM we always used.
Long shot, but, is the mouse-freezing bug still present?
You know... Now that you mention it, I don't think I encountered it. But maybe I was just "lucky": even with the previous ROM, it was not THAT common for me to encounter it (but at the same time, it wasn't exactly very rare).
If you have a mini, are you able to check it on your end, as well? The more people we have trying this out, the more likely we are to truly find out.
I suspect the mouse glitch probably remains, since as far as we know it's a shortcoming to be addressed in our patches for the mini rather than Apple's own code, but... who knows?

						«
Last Edit: November 27, 2025, 11:07:05 PM by Jubadub
 »


						Logged


#### ssp3

* Moderator
* 512 MB
* Posts: 1019

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #4 on:

Yesterday
 at 04:38:32 AM »

@Jubadub, thank you for writing all this! I will need to re-read it several times to fully grasp what's going on there.
This is EPIC!

						Logged


If you're not part of the solution, you're part of the problem.

#### Protools5LEGuy

* Staff Member
* 2048 MB
* Posts: 2842

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #5 on:

Yesterday
 at 09:23:44 AM »

Great Post!
Quote
This is EPIC!
Agree!

						Logged


Looking for MacOS 9.2.4

#### aBc

* Staff Member
* 256 MB
* Posts: 414
* FdB•FBz•aBc

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #6 on:

Yesterday
 at 12:57:18 PM »

BRAVO Jubadub!
Had been wondering about your absence ‘round here lately.
Now that’s evident, considering what you’ve been working on.
Extremely well done and VERY highly commendable.
Not everyone is capable of pulling all of that information together
and then presenting it in such a concise, yet clearly written manner.
Kudos!

						Logged


TRY the Original MacOS9Lives theme “Blu” / via your Profile --> Look and Layout settings.

#### DieHard

* Staff Member
* 2048 MB
* Posts: 2458

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #7 on:

Yesterday
 at 03:26:59 PM »

In the words of the late great Ozzy "Never say Die..."

						Logged


#### Jubadub

* 512 MB
* Posts: 525
* There is no Mac in OS X

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #8 on:

Today
 at 01:57:57 AM »

Quote from: aBc on
Yesterday
 at 12:57:18 PM
BRAVO Jubadub!
Had been wondering about your absence ‘round here lately.
Now that’s evident, considering what you’ve been working on.
Extremely well done and VERY highly commendable.
Not everyone is capable of pulling all of that information together
and then presenting it in such a concise, yet clearly written manner.
Kudos!
I'm glad you like the post! Indeed, gathering all the information so that everyone's on the same page was one of my main goals with all this.
But, just to be sure there's no risk of any misunderstanding, I'm just the messenger in all this: we all owe it to Rairii, who is the sole owner of this project that made all this possible. All I did was to combine it with @ELN's mac mini scripts and tools, then share the result of
that
 with everyone along with the story and all the information.
My overall "Mac absence" for the year was mostly due to having to take care of personal matters to get things in due order. But after I saw these crazy new developments brewing, I sure took the time to take a dive and share whatever I could!

						Logged


#### ELN

* 256 MB
* Posts: 297
* new to the forums

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #9 on:

Today
 at 03:23:29 AM »

Excellent work!
I switched from Python to Go in large part for the compatibility guarantee.
https://go.dev/doc/go1compat

						Logged


#### Jubadub

* 512 MB
* Posts: 525
* There is no Mac in OS X

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #10 on:

Today
 at 05:13:52 AM »

Hey, it's great to see you return here, @ELN! Your scripts and tools really saved the Mac-day here!
I wasn't sure about Go, but yeah, Python doesn't usually leave me with the best impression with lack of forward compatibility among even minor versions... I thought the infamous Python 2 to 3 migration was going to be the last time it would have issues like this, but I guess not. However, I'm just glad your tools work with most Python 3.x versions still! They made all the difference, and they were very easy to use thanks to the lengths you went through to keep it as heavily-commentated and easy-to-use as possible for a CLI app. I see why you would favor Go nowadays, though, as they reassure to do better to devs. (What about good ol' Perl?)
By the way, in case it might interest you, you can interact with Rairii directly through
this Discord server of his
 (listed in his
Nintendo PPC NT GitHub page
, which currently accomodates PowerPC/MIPS WinNT + Mac discussions/developments in particular).

						Logged


#### davecom

* Project Patron
* 32 MB
* Posts: 39
* Mac mini G4 Guy

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #11 on:

Today
 at 09:06:52 AM »

Congratulations all involved! That's quite the hack and definitely something that brings excitement to the whole space. Great write up and it was cool to see how the efforts of multiple individuals came together.

						Logged


Purchase a refurbished Mac mini G4 with an SSD and Mac OS 9 pre-installed from me at
https://os9.shop

#### RonsCompVids

* 1 MB
* Posts: 1

##### Re: System 7 natively boots on the Mac mini G4!

«
Reply #12 on:

Today
 at 09:53:19 AM »

It was Mac84, not "someone"... just give credit where credit is do:
https://www.youtube.com/watch?v=qbIoaulKYJY&pp=ygUFbWFjODQ%3D

						Logged


* Print

Pages: [
1
]   
Go Up

* Mac OS 9 Lives>
* Mac OS 9 Discussion>
* Mac OS 9, Hacks & Upgrades>
* Mac OS 9 on Unsupported Hardware(Moderator:ssp3) >
* System 7 natively boots on the Mac mini G4!

### Recent Topics

					[
Mac OS 9 on Unsupported Hardware
]


System 7 natively boots on the Mac mini G4!

					by
RonsCompVids

Today
 at 09:53:19 AM


					[
Mac OS 9 on Unsupported Hardware
]


Mac OS 9 booting on: Mac mini G4 (Detailed Posts)

					by
aBc

					November 27, 2025, 11:50:51 PM


					[
Mac OS 9, Hacks & Upgrades
]


I am in search of the perfect launcher

					by
n8blz

					November 27, 2025, 03:37:53 PM


					[
Storage
]


List of SSDs that works with Mac Os 9

					by
IIO

					November 27, 2025, 12:39:04 PM


					[
Mac OS 9, Hacks & Upgrades
]


Mac OS 9.2.2 Memory Limit of 1.5 GB... Some Answers

					by
Daniel

					November 27, 2025, 08:03:03 AM


					[
Software
]


My writing woes

					by
aBc

					November 26, 2025, 10:08:47 AM


					[
Community Marketplace
]


WTB: PowerMac G4 / 23" Apple Cinema Display (M8536)

					by
smilesdavis

					November 26, 2025, 09:19:36 AM


					[
News, Information & Feedback
]


“The startup disk no longer has a valid system folder” after using bless (osX)

					by
overshoot

					November 25, 2025, 03:22:11 AM


* XHTML
* RSS
* WAP2
