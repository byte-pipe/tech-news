---
title: After three months on Linux, I don’t miss Windows at all | The Verge
url: https://www.theverge.com/tech/918797/switched-to-linux-dont-miss-windows
site_name: newsfeed
content_file: newsfeed-after-three-months-on-linux-i-dont-miss-windows-at
fetched_at: '2026-04-26T19:44:59.338908'
original_url: https://www.theverge.com/tech/918797/switched-to-linux-dont-miss-windows
author: Nathan Edwards
date: '2026-04-26'
published_date: '2026-04-26T13:00:00+00:00'
description: "\uFEFFI regret nothing"
tags:
- the-verge
- linux
- microsoft
- tech
---

* Tech
* Linux
* Microsoft

# After three months on Linux, I don’t miss Windows at all

﻿I regret nothing

﻿I regret nothing

by
 
 
Nathan Edwards
Apr 26, 2026, 1:00 PM UTC
* Link
* Share
* Gift

If you buy something from a Verge link, Vox Media may earn a commission.See our ethics statement.

Some relevant reading.
Nathan Edwards
 
is a senior reviews editor who’s been testing tech since 2007. Previously at 
Wirecutter
 and 
Maximum PC
. Current fixations: keyboards, DIY tech, and the smart home.

In January Ifinally made goodon mythreat/promise to install Linux on my desktop. I wanted to see how far I could get using a Linux PC as my main computer without doing a bunch of research beforehand or troubleshooting afterwards. Since then I have booted into Windows exactly twice: once to scan a multipage document that wasn’t scanning right in Linux, and once to print a photo for my kids’ school on extremely short notice. There’s a reason it’s taken me three months to write the next installment in my Linux diary: nothing has gone horribly wrong.

It didn’t take long for my Linux install to stop feeling new and exciting and start feeling like, well, my computer. It’s notexactlylike a less annoying version of Windows, though it is less annoying than Windows, but it’s been a much easier transition than I thought it would be. There are a few extra steps sometimes in finding and installing apps — usually it’s easier than in Windows, and occasionally it’s harder. And there are a few apps I still haven’t been able to replicate in Linux. I’ve also had a smattering of fun bugs, and a few genuinely frustrating moments, but the overall experience is a lot calmer and more robust than I expected. Even troubleshooting is (mostly) satisfying in a weird way.

### Related

* I replaced Windows with Linux and everything’s going great
* I saved a doomed Windows laptop by embracing Linux
* I went back to Linux and it was a mistake

## Getting fiddly

Fortunately, everything that’s gone wrong so far has only goneslightlywrong, like a gaming mouse that only works in games, and most of it has been pretty funny, like a gaming mouse that only works in games. Some of it has to do with specific hardware I’m using, or specific choicesImade. (Keepingmy nemesis, the HP OfficeJet 8720 printer, for one.) Some of it has to do with the fact that I deliberately chose a relatively newrolling distributionbased on Arch Linux rather than a more mainstream distribution with a predictable release cycle, like Ubuntu.

Here’s my favorite fix so far. CachyOS comes withSnapper, a built-in imaging service that stores snapshots of the OS before you install or update a program, so you can roll back if something goes wrong. It defaults to saving 50 snapshots, which are stored in the boot partition. When I installed CachyOS, I went with the recommended size for that partition, which was 2GB. That filled up pretty quickly, and after a few weeks Snapper started warning me that it had run out of space and wouldn’t be taking any more snapshots (It defaults to 50, but didn’t have room to store 50 snapshots). CachyOS has since changed its installer to default to a 4GB partition, but it was too late to help me. There was only one thing to do: boot back into the live image, shrink my rightmost partition by 2GB, and slideevery volume on the diskto the right of the boot partition over by 2GB, one at a time, to make room to expand the boot partition. It’s silly that I had to do that but it was easy enough, and kinda satisfying in a tactile way.

When I say “slide every volume on the drive to the right” I’m not kidding.

In January, I noticed I couldn’t get an IP address from my router on my ethernet connection after waking from sleep unless I first connected to Wi-Fi. This drove me up the goddamnwall. Fortunately, I could keep using the computer while troubleshooting because I do have both Wi-Fi and ethernet, but I prefer ethernet, so I had to fix it. I learned the default driver that the Linux kernel uses for my particular ethernet card doesn’t always work well, so I installed a new driver. I turned off ipv6, then turned it back on again. I made sure my wired and wireless connections identified themselves as different devices to the router, though that didn’t help. I set a static IP on both the router and computer side. I extended my DHCP lease timeout. Finally I found the actual culprit.

Several years ago, in an effort to get my multigenerational Sonos speakers to play nicely with my Unifi router (it’s a whole thing), I followed some advice on a forum and enabled STP — an older port-scanning protocol — on my networking switch. This was fine for my Windows PC, but in Linux it made getting an IP address from the router take so long every time that the ethernet card gave up. Disabling it fixed the problem with my desktopandfinally got the Era 100 in my kitchen showing up consistently in the Sonos app. Figuring out how to solve a problem on an OS I’d used for a few weeks fortuitously solved a problem I’d created trying to solve adifferentproblem on a different OS a few years ago. We learn by doing!

My current gremlin is that the mic on my Logitech Brio webcam doesn’t always transmit sound. Sometimes nobody can hear me from the get-go; other times it stops working in between one meeting and the next, and lately it’s been cutting out mid-sentence. This is probably because I installedEasyEffects, but I’m not sure yet. I have another microphone — and also other computers, if really necessary. If I didn’t, I would probably be more annoyed. Maybe annoyed enough to fix it.

On the other hand, sometimes problems solve themselves if you wait. I wanted to find a way to add text extraction to the screenshot utility in KDE Plasma — a feature I missed from other operating systems. The solution was to wait a week until Cachy updated to Plasma 6.6, which added that feature. Score another point for laziness.

## Where we left it

When I last wrote about my experience with CachyOS, I bemoaned the absence of the Arc browser. Several readers pointed me toZen, which is basically Arc but open-source and built on Firefox, and it is indeed good enough. Thank you, readers. I also grabbed aSpotify clientfrom the Arch User Repository. I set up git and finally recompiled theZMK firmwarefor my number pad. I even gotZMK Studio— a GUI keymap editor — working. In lieu of Photoshop, I’ve been using thePhotopeaweb app. It’s probably not load-bearing if I have to edit a bunch of photos, but so far I haven’t had to.

I didn’t end up installinghowdyfor webcam facial-recognition unlocking because it doesn’t seem to be as secure as Windows Hello. Windows Hello uses infrared 3D face mapping; by the developer’s own admission, howdy can apparentlybe fooled by a photo. I’m not worried about my kids printing photos of me so they can run sudo commands on my computer, but for now I’m typing my password every time. Microsoft and Apple have put a lot of money into nailing biometric authentication, and the Linux approach of “hoping someone volunteers to make this” really does put the ecosystem at a disadvantage. Fingerprint authentication seems to work fine, but my desktop doesn’t have a fingerprint reader.

## Gaming part deux

Cachy is working fine for gaming, with the caveat that I am still not playing competitive multiplayer games or anything requiring anti-cheat — or anything that’s really pushing my RTX 4070 Super, for that matter. I gotMinecraft: Bedrock Editionworking withMCPE Launcher; all I had to do was enable remote login and disable vibrant visuals. My kids kind of fell off ofMinecraftbut we had a few good weeks there. I’ve also played a bit ofHardspace: Shipbreaker,Esoteric Ebb(greatgame),Caves of Qud(live and drink), andBaldur’s Gate 3(just a little). They’ve all run fine. I playedHardspacethrough the Heroic Games Launcher, and the rest through Steam.

Behold my kingdom.

Last time, I mentioned a weird bug where my ancient gaming mouse only workedingames, and not outside of them. It isapparently fixable, but I replaced it anyway with aKeychron M5vertical mouse, which has been great both in and out of game and has largely replaced my trackball, to my surprise.

## Current regret level: still zero

You might ask: why would I put up with a computer that I had to cajole into getting itswiredethernet working, that sometimes completely forgets about the mic on my webcam, that refuses to sleep for unknown reasons at unpredictable intervals? It’s because those are outliers. It mostly just works, and figuring out how to fix the things that don’t is fun.

I was happy on Windows until I wasn’t. I liked Windows! I have been using it since I was a kid, and I’ve been building my own desktops for close to 20 years. I wasn’t the one who decided to ruin the Start menu by making it search Bing instead of my files; I didn’t break indexing; I didn’t rename the app that launches Office documents so many times the computer forgot how to open Word documents. I didn’t opt in to any of that.Mychoices didn’t make Windows worse. It’s not fun to fix Windows when it breaks because Microsoft is shipping its org chart.

But if my browser in Linux can’t find my webcam mic because I installedEasyEffectswithout bothering to read the docs, brother, that’s on me. Similarly, if half my operating system is in French all of a sudden, c’est parce que j’ai l’ajouté. I opted in to this situation; it wasn’t foisted on me. It’s the difference between running because you want to go for a run and running because you’re late for the train.

Why did this switch to French halfway through? Je ne sais pas.

Linux is built on theUnix philosophy: it’s made up of lots of little pieces of modular software that each do one thing well, rather than huge monolithic programs that try to do everything for everyone. It’s like a box of Lego, rather than an action figure. I’m having a great time with metaphors today. The skills I build by figuring out how to install a spellchecker, or change drivers, or add a software repository, or configure git, are transferable to the rest of the OS and a lot of the software as well. I think that’s neat.

I have not totally gone away from Windows. My laptop still runs on Windows for now, and I do have to hand it to Microsoft: the Surface Pro is a great tablet computer. Of course, it would be even better if Windows were less annoying, butMicrosoft is aware. And I need to be current with Windows for my job. But it turns out I don’t need to run Windows on my desktop, and I’m having more fun with Linux, so I’m gonna keep at it.

Follow topics and authors
 from this story to see more like this in your personalized homepage feed and to receive email updates.
* Nathan Edwards
* Linux
* Microsoft
* Tech
* Windows

## Most Popular

Most Popular
1. Trump fires the entire National Science Board
2. The US gets the worst phones
3. Alex Jones has uncovered another massive conspiracy
4. 360-degree cameras have a new superpower
5. We translated the Palantir manifesto for actual human beings

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

An influx of used EVs could drive down prices
Researchers say we’re talking less than ever
The Govee smart lamp brightened up my room, and then my life
The most exciting laptop I’ve seen in forever
The US gets the worst phones
Microsoft will let you pause Windows Updates indefinitely, 35 days at a time
An influx of used EVs could drive down prices
Terrence O'Brien
Apr 25
Researchers say we’re talking less than ever
Terrence O'Brien
Apr 25
The Govee smart lamp brightened up my room, and then my life
Sheena Vasani
Apr 25
The most exciting laptop I’ve seen in forever
David Pierce
Apr 25
The US gets the worst phones
Dominic Preston
Apr 25
Microsoft will let you pause Windows Updates indefinitely, 35 days at a time
Stevie Bonifield
Apr 24
Advertiser Content From

This is the title for the native ad

## Top Stories

4:18 PM UTC
Trump turns the WHCD shooting into a pitch for the White House ballroom
12:00 PM UTC
The plan to quietly kill Coyote v. Acme blew up in David Zaslav’s face
4:00 PM UTC
Tomora’s Come Closer is an ecstatic love letter to 90s dance music
Apr 25
The US gets the worst phones
An hour ago
Google’s new gradient icon design is coming to more apps
3:42 PM UTC
The villain-loaded Spider-Noir trailer comes in two flavors.