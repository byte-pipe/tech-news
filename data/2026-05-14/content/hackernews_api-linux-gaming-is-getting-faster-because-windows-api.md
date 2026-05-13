---
title: Linux gaming is getting faster because Windows APIs are becoming Linux kernel features
url: https://www.xda-developers.com/linux-gaming-is-getting-faster-because-windows-apis-are-becoming-linux-kernel-features/
site_name: hackernews_api
content_file: hackernews_api-linux-gaming-is-getting-faster-because-windows-api
fetched_at: '2026-05-14T06:00:51.872730'
original_url: https://www.xda-developers.com/linux-gaming-is-getting-faster-because-windows-apis-are-becoming-linux-kernel-features/
author: haunter
date: '2026-05-11'
published_date: '2026-05-10T16:30:21Z'
description: As time goes on, fewer games than ever are unplayable on Linux
tags:
- hackernews
- trending
---

By 

Ty Sherback

Published
 May 10, 2026, 12:30 PM EDT

His love of PCs and their components was born out of trying to squeeze every ounce of performance out of the family computer. Tinkering with his own build at age 10 turned into building PCs for friends and family, fostering a passion that would ultimately take shape as a career path. 

Besides being the first call for tech support for those close to him, Ty is a computer science student, with his focus being cloud computing and networking. He also competed in semi-pro 
Counter-Strike
 for 8 years, making him intimately familiar with everything to do with peripherals. 

Sign in to your 
XDA
 account

In March 2026, Linux crossed five percent of Steam's user base for the first time, an all-time high for an operating system that spent two decades as a novelty when it came to any kind of gaming. Microsoft's end-of-support deadline for Windows 10 last October pushed many users to look at alternatives, and the Steam Deck has quietly turned millions of people into Linux gamers without them really thinking about it, leading to more widespread adoption on desktop machines.

 

Most of that progress used to happen inside a piece of software called Wine, the translation layer that convinces Windows games they're running on Windows. Valve's tuned version ofWine, called Proton, is what makes Steam Play and the Steam Deck work. For years, every meaningful improvement to Linux gaming came from changes to Wine and Proton themselves. That's still true, but increasingly the most important changes are happening one layer deeper, inside the Linux kernel. The latest example of that is something calledNTSYNC, a kernel-level driver that has offered great performance gains over previous versions of Wine, and is loaded by default on every Steam Deck that's up-to-date.

Related

##### Wine 11 rewrites how Linux runs Windows games at the kernel level, and the speed gains are massive

Wine 11 is the biggest jump for Linux gaming in years.

By 

Adam Conway

## What NTSYNC actually is

### An additional piece of the performance puzzle

NTSYNC is a small piece of driver added directly to the Linux kernel that gives it a native implementation of a set of Windows-specific tools that games depend on to coordinate themselves.

 

Modern games juggle dozens of things at once. While you're playing, your CPU manages the rendering pipeline, loading assets, running physics, processing audio, handling AI NPC routines, and tracking inputs, all in parallel across multiple cores. All those jobs constantly have to coordinate so they don't trip over each other.

 

Quiz
8 Questions · Test Your Knowledge

## The history of LinuxTrivia challenge

From a Finnish student's side project to powering the world — how well do you know the story of Linux?

Origins
Kernel
Distros
Pioneers
Milestones
Begin
01 / 8
Origins

In what year did Linus Torvalds first announce the Linux kernel to the world?

A
1989
B
1991
C
1993
D
1995
Correct! Linus Torvalds posted his now-famous message to the comp.os.minix newsgroup on August 25, 1991, describing Linux as 'just a hobby' project. Few could have predicted it would one day run the majority of the world's servers and smartphones.
Not quite — Torvalds made his announcement in 1991. He was a 21-year-old computer science student at the University of Helsinki at the time, and his modest post described the project as something that 'won't be big and professional' like GNU.
Continue
02 / 8
Pioneers

Which university was Linus Torvalds attending when he created the first version of the Linux kernel?

A
Stockholm University
B
Aalto University
C
University of Helsinki
D
MIT
Correct! Torvalds was studying at the University of Helsinki in Finland when he began working on Linux as a personal project, initially inspired by MINIX, a small Unix-like system used for educational purposes.
Not quite — Torvalds was a student at the University of Helsinki in Finland. He started Linux partly out of frustration with the limitations of MINIX, which his professor Andrew Tanenbaum had designed deliberately to be simple for teaching.
Continue
03 / 8
Kernel

What operating system primarily inspired Linus Torvalds to create the Linux kernel?

A
MS-DOS
B
MINIX
C
BSD Unix
D
Solaris
Correct! MINIX, created by professor Andrew Tanenbaum, was the direct inspiration for Linux. Torvalds used MINIX on his new Intel 386 PC but found it too restricted for his needs, which pushed him to write his own kernel.
Not quite — the answer is MINIX. Torvalds was using MINIX when he started Linux, and even held a famous online debate with its creator Andrew Tanenbaum about kernel design philosophy, specifically monolithic versus microkernel architectures.
Continue
04 / 8
Milestones

What was the version number of the first publicly released Linux kernel in 1991?

A
0.01
B
0.1
C
1.0
D
0.99
Correct! Linux version 0.01 was the first kernel Torvalds released publicly in September 1991. It was a rough, early build that could only run on Intel 386 hardware and had very limited functionality, but it marked the true beginning of the Linux project.
Not quite — the first public release was version 0.01 in September 1991. The kernel didn't reach version 1.0 until March 1994, by which point it had grown significantly in capability and had attracted contributions from developers around the world.
Continue
05 / 8
Distros

Which Linux distribution, first released in 1993, is one of the oldest still actively maintained today?

A
Ubuntu
B
Fedora
C
Slackware
D
Debian
Correct! Slackware, created by Patrick Volkerding, was first released in July 1993, making it one of the oldest surviving Linux distributions. It is known for its simplicity and Unix-like philosophy, and it continues to be maintained to this day.
Not quite — the answer is Slackware, released in 1993 by Patrick Volkerding. While Debian was also founded in 1993, Slackware narrowly edges it out as the older release. Ubuntu didn't arrive until 2004, and Fedora launched in 2003.
Continue
06 / 8
Origins

The GNU Project, which provided many tools that paired with the Linux kernel, was founded by which developer?

A
Eric Raymond
B
Richard Stallman
C
Bruce Perens
D
Ian Murdock
Correct! Richard Stallman founded the GNU Project in 1983 with the goal of creating a completely free Unix-like operating system. When the Linux kernel appeared in 1991, it filled the missing piece GNU needed, and the combination became what many call GNU/Linux.
Not quite — it was Richard Stallman who founded the GNU Project in 1983. Stallman is also known for creating the GPL (GNU General Public License) and founding the Free Software Foundation, two pillars that shaped the legal and philosophical foundation of free software.
Continue
07 / 8
Milestones

Which company released a landmark commercial Linux distribution in 1994, helping bring Linux into the enterprise world?

A
Canonical
B
SUSE
C
Red Hat
D
Mandriva
Correct! Red Hat released its first Linux distribution in 1994 and became one of the most influential commercial Linux companies in history. It pioneered the enterprise Linux market and was eventually acquired by IBM in 2019 for approximately $34 billion.
Not quite — Red Hat is the answer. Founded by Marc Ewing and Bob Young, Red Hat helped prove that companies could build sustainable businesses around open-source software. SUSE Linux also launched in 1994, making it a close rival, but Red Hat became the more globally dominant enterprise force.
Continue
08 / 8
Distros

Ubuntu Linux, one of the most popular desktop distributions, is based on which other Linux distribution?

A
Arch Linux
B
Fedora
C
Debian
D
Gentoo
Correct! Ubuntu is based on Debian and was first released in October 2004 by Mark Shuttleworth's company Canonical. It was designed to make Linux more accessible to everyday users, and its six-month release cycle and long-term support versions made it a favorite for both desktops and servers.
Not quite — Ubuntu is built on top of Debian. Debian itself was founded in 1993 by Ian Murdock and is known for its strict commitment to free software and stability. Ubuntu inherits Debian's package management system (APT and .deb packages) but adds its own user-friendly layer on top.
See My Score
Challenge Complete

## Your Score

/ 8

Thanks for playing!

Try Again

Windows handles this coordination by using a specific set of mechanisms, and before NTSYNC, Wine had to mimic these mechanisms using things like esync and fsync, which both worked, but didn't always match Windows exactly. NTSYNC builds these mechanisms straight into the Linux kernel for the first time, and it means Wine doesn't have to emulate anything anymore. The developer-facing API calls don't actually change, Linux just knows how to answer them natively.

Related

##### Wine has been translating Windows games to Linux since 1993, but Proton is what made it effortless

Wine is the foundation that makes gaming on Linux possible.

By 

Adam Conway

## NTSYNC is part of a growing pattern

### Not the first time Linux has inherited features because of Windows

NTSYNC isn't the first time Linux has gained a new feature specifically because Windows games needed it. A few years back, Linux added a way for software to wait on several events at once, which is something Windows had built in for decades, but Linux didn't. Wine had been working around the gap with awkward tricks until the kernel finally got native support.

 

This work is driven by Valve, by CodeWeavers (the company that employs many of the core Wine developers, including NTSYNC's author Elizabeth Figura), and by a steady stream of contributors who want Linux to be a real gaming platform without depending on out-of-ecosystem patches forever.

Related

##### Valve isn't ditching Windows or x86, but it's quietly making both optional

Valve wants to make it possible for gamers to play anywhere.

By 

Adam Conway

## These aren't magical performance gains

### fsync was already pretty good

The headline performance gains look great, but they need some context. The eye-catching 40 to 200 percent FPS gains cited inNTSYNC's original benchmarkswere measured against unmodified upstream Wine, which almost nobody uses to play games on Linux anymore. Most Linux gamers, including every Steam Deck owner, use Proton, which already has fsync. Compared to fsync, NTSYNC's performance gains are far more modest. The games that benefit most from the change to NTSYNC are games that were really struggling before. Anything that was running at decent framerates beforehand is still going to run fine.

Related

##### These 7 Linux myths you still believe simply aren't true

Linux is a completely different beast than it was a decade ago.

By 

Rich Edmonds

## Valve adopted it anyway

### It's a great sign

Pierre-Loup Griffais, an engineer at Valve, hasgone on the record to say that fsync was already fast enough, and despite that, Valve still shipped NTSYNC in stable SteamOS in March anyway, which speaks to the fact that fsync is still a workaround at its core, and can be the cause of issues outside of poor raw FPS.

These old workarounds got subtle edge cases wrong in ways that produced occasional hitches, deadlocks, or weird behavior in specific games, which are bugs that don't show up on benchmark charts but can absolutely ruin individual experiences. NTSYNC fixes those at the source by matching Windows behavior exactly, and that means as soon as your favorite distro moves to the new kernel version, whether it be Bazzite, CachyOS, Fedora, or a flavor of Ubuntu, they all get this much-needed fix.

Related

##### 4 reasons Valve's full SteamOS release will change PC gaming again

Valve's full SteamOS release will change PC gaming again, and here are some of the most important ways.

By 

Adam Conway

### Gaming on Linux continues to improve by the month

Linux has grown so much in the gaming department. Where there once was nothing but cleverWine patches and community workaroundsnow lies support from gaming behemoths like Valve, driving changes to the Linux kernel itself. NTSYNC won't be the last time a piece ofWindowsgets rebuilt inside Linux because gamers needed it, and with more than five percent of Steam's user base now running Linux, the incentive to keep doing it has never been stronger.

 

Close