---
title: '"Notepad++ for Mac" release is disavowed by the creator of the original - Ars Technica'
url: https://arstechnica.com/gadgets/2026/05/unofficial-vibe-coded-notepad-for-mac-draws-objections-from-original-author/
site_name: newsfeed
content_file: newsfeed-notepad-for-mac-release-is-disavowed-by-the-creato
fetched_at: '2026-05-05T11:59:55.286758'
original_url: https://arstechnica.com/gadgets/2026/05/unofficial-vibe-coded-notepad-for-mac-draws-objections-from-original-author/
date: '2026-05-04'
published_date: '2026-05-04T21:38:37+00:00'
description: 'To be clear: Notepad++ has never released a macOS version."'
tags:
- ars-technica
- ai
- tech
- anthropic claude
---

Text
 settings

As its name implies, the venerableNotepad++ text editorbegan as a more capable version of the classic Windows Notepad, with features such as line numbering and syntax highlighting. It was created in 2003 by Don Ho, who continues to be its primary author and maintainer, and it has beena Windows-exclusive appthroughout its existence (older Notepad++ versions support OSes as old as Windows 95; the current version officially supports everything going back to Windows 7).

I’m not a devoted user of the app, but I was aware of its history, which is why I was surprised to see news of a “Notepad++ for Mac” portmaking the rounds last week, as though it were a port of the original available from the Notepad++ website.

Apparently, this news surprised Ho as well, whoclaimsthat the Mac version and its author,Andrey Letov, are “usingthe Notepad++ trademark(the name) without permission.”

“This is misleading, inappropriate, and frankly disrespectful to both the project and its users,” Ho wrote. “It has already fooled people—including tech media—into believing this is an official release. To be crystal clear: Notepad++ has never released a macOS version. Anyone claiming otherwise is simply riding on the Notepad++ name.”

## An escalating back-and-forth

Further communication between Ho and Letov can be found in a Notepad++ GitHub thread, where Hosaidhe had been contacted by Letov before the Notepad++ for Mac app had launched, but that he hadn’t had time to reply.

“The problem is that using the official name Notepad++ and its logo gives the impression that your project is an official macOS version maintained or endorsed by the Notepad++ team, which is not the case,” wrote Ho in an email to Letov that he reposted to GitHub. “This create [sic] confusion for users and exposes both you and the project to trademark issues.”

Letovrespondedtwo days later, saying he hadn’t meant to insinuate that Ho was involved with the Notepad++ for Mac project. But he did insist that his port “actually expands notepad++ brand to mac” and expressed hope that Ho would allow him to continue to use the name. Horesponded, again asking Letov to stop using the Notepad++ name and logo and to change the project’s URL so that users would not mistake the project for an official Notepad++ port and contact Ho looking for support.

“I will prep for the site and some naming changes,”wroteLetov. “Give me a couple of weeks. My intention was to expand your brand. I really hope that at some point in the future you change your mind and see this as a positive growth for your brand.”

At this point, Ho seemed to lose patience with Letov’s responses, particularly with being asked to allow Letov to continue using the Notepad++ name for “a couple of weeks.” Ho reported the use of the Notepad++ trademark to Cloudflare, the CDN of the Notepad++ for Mac site, and asked Letov to take it down.

“Every day that website remains active, you are in further violation of the law,” Howroteearlier today. “I cannot authorize a ‘week or two’ of continued trademark infringement.”

Letov began changing the websitetwo days ago, though at first he claimed to be making these changes “in coordination with Don Ho.” This drewfurther accusationsfrom other GitHub users that he was trying to misrepresent the port’s relationship to the original project.

Those changes continue and have ramped up over the last few hours; the app will now be called “NextPad++,” an homage toNeXT Computer, and uses a frog icon rather than the Notepad++ lizard. The original version, along withthe authors pagethat lists Ho beneath Letove, is available via Internet Archive snapshots.

Letov claims that the app’s name will change in version 1.0.6. Version 1.0.5, with the Notepad++ logo and branding intact, is available for download. The project’s URL also hasn’t changed.

## A seemingly thoughtful but low-effort port

 The “Notepad++ for Mac” app looks right, but there are reasons to prefer an “official” port when you can get one.
 

 Credit:
 NextPad++
 

 The “Notepad++ for Mac” app looks right, but there are reasons to prefer an “official” port when you can get one.

 

 Credit:

 
 NextPad++

 

I had considered writing about Notepad++ for Mac last week, but lost a bit of interest after discovering it was “an independent community port” rather than an official release—independent ports and forks are all well and good, but an official release implies ongoing updates and support, where an “independent community port” might fade away or vanish entirely as soon as its creator gets bored and/or moves on.

But I continued to dig because, at a glance, it seemed like an exceptionally thoughtful community port. It supported macOS versions dating back to 11.0 Big Sur on both Intel and Apple Silicon processors. It was a native macOS app with aCocoauser interface that replaces the original Win32 interface rather than translating it orusing a wrapper. The app seemed to be lightweight and clean, as promised. And it was properlynotarizedso that users could download and launch it relatively easily—not a given, for many independent and/or open source Mac software projects.

But I paused when I hitLetov’s About page, which mentioned being “deep in multi-agent AI” and showed a flurry of GitHub commits that happened exclusively in March and April 2026. The Notepad++ for Mac page made no mention of the project being AI-coded, but when contacted for comment, Letov confirmed that both the Notepad++ for Mac app and the website were created at least partially using Anthropic’s Claude CLI.

“I primarily use Claude CLI with some customizations to run multiple agents and also Codex plugin for VSS. I also use Beads,” Letov told Ars. “Website is also partly managed using Claude CLI plus some manual work on graphics.”

“I run some agents that scan for Issues and general issues reported, list/create options to implement features and fixes. I usually review most and decide on the path,” Letov continued when asked how much human oversight the project had. “Also UIs are not as easily tested by AI as backend code and some things have to be thought through and build iteratively.”

It’s not that I think the use of AI coding tools should be disqualifying in and of itself. AI coding toolsdo have real utility, and many companies and projects aremaking at least some use of them; you likely are running or will eventually run an app containing AI-generated code whether you want to or not. But the port being both “independent” and AI-generated heightens my existing concerns about ongoing support and the developer’s capability to address bug reports and merge upstream code.

And, as Ho and other users warned in the GitHub thread, downloading an unvetted unofficial port of a project can increase your risk of downloading malware.

“I apologize for sounding paranoid, but I have not verified your code & binaries, and I have no time to do so,” wrote Ho, whocomes by his concern about hidden malware in Notepad++ honestly.

 Andrew Cunningham
 

Senior Technology Reporter

 Andrew Cunningham
 

Senior Technology Reporter

 Andrew is a Senior Technology Reporter at Ars Technica, with a focus on consumer tech including computer hardware and in-depth reviews of operating systems like Windows and macOS. Andrew lives in Philadelphia and co-hosts a weekly book podcast called 
Overdue
.
 

1. 1.Zack Cregger has his own vision for Resident Evil reboot
2. 2.Toyota built a $10 billion private utopia—what’s going on in there?
3. 3.Amazon stuck with months of repairs after drone strikes on data centers
4. 4.Musk’s “World War III” threat in Twitter lawsuit haunts him at OpenAI trial
5. 5.Canadian election databases use "canary traps"—and they work

Customize