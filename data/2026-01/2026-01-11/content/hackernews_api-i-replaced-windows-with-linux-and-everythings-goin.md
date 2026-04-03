---
title: I replaced Windows with Linux and everything’s going great | The Verge
url: https://www.theverge.com/tech/858910/linux-diary-gaming-desktop
site_name: hackernews_api
fetched_at: '2026-01-11T11:06:43.774138'
original_url: https://www.theverge.com/tech/858910/linux-diary-gaming-desktop
author: Nathan Edwards
date: '2026-01-10'
published_date: '2026-01-10T15:00:00+00:00'
description: I’ve spent half a week with CachyOS and I’m unstoppable.
tags:
- hackernews
- trending
---

* Tech
* Gaming
* Desktops

# I replaced Windows with Linux and everything’s going great

Linux diary, chapter one: winging it.

Linux diary, chapter one: winging it.

by


Nathan Edwards
Jan 10, 2026, 3:00 PM UTC
* Link
* Share
Is this… bliss?

Screenshot: Nathan Edwards / The Verge
Nathan Edwards

is a senior reviews editor who’s been testing tech since 2007. Previously at
Wirecutter
 and
Maximum PC
. Current fixations: keyboards, DIY tech, and the smart home.

Greetings from the year of Linux on my desktop.

In November, I got fed up and saidscrew it, I’m installing Linux. Since that article was published, I have dealt with one minor catastrophe after another. None of that has anything to do with Linux, mind you. It just meant I didn’t install it on my desktop until Sunday evening.

My goal here is to see how far I can get using Linux as my main OSwithoutspending a ton of time futzing with it — or even much time researching beforehand. I am not looking for more high-maintenance hobbies at this stage. I want to see if Linux is a wingable alternative to Microsoft’sincreasingly annoying OS.

### Related

* Microsoft is turning Windows into an ‘agentic OS,’ starting with the taskbar
* Screw it, I’m installing Linux

Honestly? So far it’s been fine. Many things I expected to be difficult — like getting my Nvidia graphics card working properly — were perfectly straightforward. A few things I thought would be simple weren’t. And I’ve run into one very funny issue with a gaming mouse thatonlyworks in games. But I’ve been able to use my Linux setup for work this week, I played exactly one video game, and I even printed something from my accursed printer.

## Day one

Spoiler alert: it worked
.

Screenshot: Nathan Edwards/The Verge

I pickedCachyOSrather than a better-known distro like Ubuntu because it’s optimized for modern hardware, and I had heard that it’s easy to install and set up for gaming, which is one of the reasons I’d stuck with Windows for this long. After backing up my Windows image sometime in December (close enough), I follow theinstallation instructions in the Cachy wikiand download theCachyOSlive image to aVentoyUSB drive, plug it into my PC, reboot into the BIOS to disable Secure Boot, reboot again into the Ventoy bootloader, and launch the CachyOS disk image.

First challenge: My mouse buttons don’t work. I can move the cursor, but can’t click on anything. I try plugging in a mouse (without unplugging the first one), same deal. Not a major issue; I can get around fine with just the keyboard. Maybe this is just an issue with the live image.

I launch the installer and am thrust into analysis paralysis. An operating system needs lots of little pieces to work — stuff you don’t even think of as individual components if you use Mac or Windows. How do you boot into the OS? What runs the desktop environment? How are windows drawn? What’s the file system? Where do you get software updates? In Mac and Windows, all those decisions are made for you. But Linux is fundamentally different: The core of the OS is the kernel, and everything else is kind of up to you. A distro is just somebody’s idea of what pieces to use. Some, likePop_OS!andMint, aim for simplicity and make all those choices for you (though you can still change them if you want). But Cachy is based onArch, a notoriously DIY distro, and before I do anything else, I have to pick one of four bootloaders. I pick Limine, for reasons I can’t recall.

Next, I need to figure out where to install it. On the recommendation of Will Smith from theDual Boot Diariespodcast— from whom the “an operating system is a bunch of pieces” thing above is largely cribbed — I install Cachy on a different physical drive from Windows, since Windows updates tend not to care if they overwrite other bootloaders.

Why did I leave all that blank space on the drive? Couldn’t tell you. I had to go fix it later.

Image: Nathan Edwards / The Verge

I have a 4TB storage drive with just over a terabyte of data on it, so I shrink that partition down to 2TB using the installer’s manual partitioning interface, then (following the guide) make a 2GB boot partition and a root partition using the btrfs file system. The guide says it needs at least 20GB, so I go big and make it 100GB. This will cause a minor problem later.

Next, I have to pickone ofthirteendifferent desktop environments. This is too many options. KDE and Gnome seem to be the best-supported for gaming, so I pick KDE. I could rabbit-hole on this, but I don’t.

And then I just have to pick a username and password and name the computer. After some thought, I go with Maggie, after my in-laws’ cat, who half the family calls Linux. She doesn’t answer to either name.

Tried getting Linux on my laptop over Christmas. Didn’t work.

Photo: Nathan Edwards / The Verge

Installation takes six minutes. I reboot the computer, and it loads into the Limine bootloader, which has also found my Windows install, so I can choose between Cachy and Windows.

Then I’m on the Cachy desktop, and my mouse buttonsstillaren’t working. Swapping USB ports doesn’t do anything. Plugging in my trackball doesn’t fix it either. I finally tryunpluggingthe mouse, which makes the trackball work normally. My gaming mouse isan ancient Mad Catz Cyborg RAT 7; it turns out this is aknown issue. I defer editing configuration files for now and just keep the mouse unplugged.

## Stuff that works

The Cachy welcome screen gives you a little selection of popular Linux apps to install.

Screenshot: Nathan Edwards / The Verge

That weird mouse aside, all of the hardware I’ve tried so far has just worked. Cachy automatically installed the correct GPU drivers; my monitor, speakers, and Logitech webcam work fine with no effort. Even my printer prints, with only a tweak to my firewall settings.

There are lots of ways to install apps on Linux. Sometimes you can just download them from a company’s website, or you get them from your distro’s official repositories, or GitHub, or wherever. There’s no official app store for Linux, but there are at least three projects aiming to provide universal Linux apps: Flatpak, AppImage, and Snap. Neat! Commence hodgepodging.

I grab Chromium, Discord, Slack, and Audacity using the “Install Apps” button on Cachy’s welcome screen. Slack I get from the Arch User Repository. Twenty minutes later, I try to install 1Password from the same location, but the repository is down. I pick up my kid from a playdate and try again. It works.

## What’s missing

I prefer the Arc browser, which doesn’t have a Linux build, but there are plenty of browsers. Firefox and Chromium will do. I can’t find official apps for Airtable (which I use for work), Spotify, or Apple Music, but they all work fine in the browser in the short term, and I’ll revisit this later.

## Shall we play a game?

Heroic Games Launcher lets you download and play games from your Epic, GOG, and Amazon libraries.

Screenshot: Nathan Edwards / The Verge

Cachy has a one-click gaming package install that includes the Proton compatibility layer, Steam, andHeroic(a launcher for Epic, GOG, and Amazon). I figure I ought to tryonegame. Then I remember that my root partition is only 100GB. I reboot back into the Cachy live image and use the Parted utility to increase it to 1TB, then make a second btrfs partition in the remaining space. I reboot, log into Epic and GOG, and start downloadingThe Outer Worlds, a game from 2019 I’ve been playing a bit lately. It runs fine with Proton, and I can even sync my saves from the cloud. I play it for a few minutes with my trackball, remember I hate gaming on a trackball, and plug my gaming mouse back in. It works fine as long as I’m in the game, but outside the game, mouse clicks stop working again. It makes sense — the bug is on the desktop, not in games — but it’s very funny to have a gaming mouse thatonlyworks for gaming.

## The children yearn for the mines

So close…

Screenshot by Nathan Edwards / The Verge
…and yet so crash.

Screenshot by Nathan Edwards / The Verge

The biggest issue I’ve had so far isMinecraft: Bedrock Edition. For some reason, Microsoft hasn’t prioritized making a Linux version of Bedrock. Java Edition works fine in Linux, but I playMinecraftwith my kids, and they’re on Bedrock Edition on their iPads. There’s supposed to be a way to run the Android app withMCPE Launcher, but I couldn’t get it to work. There’s also a project to get the Windows version running on Proton, which will be my next step.

## Stuff I haven’t tried yet

I hear good things abouthowdy, a Linux equivalent to Windows Hello face authentication, but I haven’t installed it yet. I hear theZenbrowser is a good Arc alternative. I also haven’t gotten my cloud storage synced, configured git so I can compile programs from scratch, figured out a backup strategy, or tried much other hardware beyond what’s currently plugged into my computer. There’s a command-line Spotify player I want to try. I’ve only scratched the surface.

I did take the time to install a KDE Plasmatheme that makes it look like Windows XP,though. Just because.

## Regret level: none

I’m well aware this is the honeymoon phase. And using Linux for less than a week isn’t exactly a flex. Many people use Linux. And I haven’t even tried doing anything particularly difficult, or playing a game that came out this decade. But so far it’s been a much easier transition than expected, and a quieter experience overall. My OS isn’t trying to change my browser or search engine to make some shareholder happy somewhere. It’s not nudging me to try some bullshit AI feature.

Will I go crawling back to macOS or Windows the first time I have to edit a batch of photos? Possibly! I’ll definitely boot back into Windows — or pull out a Chromebook — to playMinecraftwith my kids, if I can’t get it running on Linux. And I don’t think I’ll ever be able to use Linux exclusively; my job as a reviews editor means I have to stay familiar with as many operating systems as possible. (This is a good way to drive yourself nuts.)

I’m sure I’ll run into plenty of fun problems soon enough. But the first few days have been great.

Follow topics and authors
 from this story to see more like this in your personalized homepage feed and to receive email updates.
* Nathan Edwards
* Desktops
* Gaming
* Linux
* Microsoft
* PC Gaming
* Tech
* Windows

## Most Popular

Most Popular
1. I replaced Windows with Linux and everything’s going great
2. Tim Cook and Sundar Pichai are cowards
3. The CES 2026 stuff I might actually buy
4. The Verge Awards at CES 2026
5. These are the smart home gadgets that impressed me at CES 2026

## The Verge Daily

A free daily digest of the news that matters most.

Email (required)
Sign Up
By submitting your email, you agree to our

Terms
 and
Privacy Notice
.
This site is protected by reCAPTCHA and the Google

Privacy Policy

and

Terms of Service

apply.
Advertiser Content From

This is the title for the native ad

## More inTech

Amazfit’s Active 2 tracker and Blu-rays are this week’s best deals
I’ve never used a trackball, but Keychron’s Nape Pro looks like the perfect one
Play
We tried to get humanoid robots to do the laundry
What’s on your desk, Stevie Bonifield?
The CES 2026 stuff I might actually buy
Betterment’s financial app sends customers a $10,000 crypto scam message
Amazfit’s Active 2 tracker and Blu-rays are this week’s best deals
Sheena Vasani
Jan 10
I’ve never used a trackball, but Keychron’s Nape Pro looks like the perfect one
Antonio G. Di Benedetto
Jan 10
Play
We tried to get humanoid robots to do the laundry
Verge Staff
Jan 10
What’s on your desk, Stevie Bonifield?
Stevie Bonifield
 and
Barbara Krasnoff
Jan 10
The CES 2026 stuff I might actually buy
David Pierce
Jan 10
Betterment’s financial app sends customers a $10,000 crypto scam message
Jay Peters
Jan 10
Advertiser Content From

This is the title for the native ad

## Top Stories

Jan 10
We tried to get humanoid robots to do the laundry
﻿
Video
Jan 10
CES 2026 was packed with smart home gadgets that matter
Jan 9
People are fighting for the truth in Minneapolis
Jan 9
Tim Cook and Sundar Pichai are cowards
Jan 10
The CES 2026 stuff I might actually buy
5:01 AM UTC
Easiest CPU liquid cooling install ever?
