---
title: Microsoft’s ‘unhackable’ Xbox One has been hacked by 'Bliss' — the 2013 console finally fell to voltage glitching, allowing the loading of unsigned code at every level | Tom's Hardware
url: https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level
site_name: hackernews_api
content_file: hackernews_api-microsofts-unhackable-xbox-one-has-been-hacked-by
fetched_at: '2026-03-18T11:20:44.864338'
original_url: https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level
author: crtasm
date: '2026-03-17'
published_date: '2026-03-15T15:17:30Z'
description: This console had remained a fortress since its launch over a decade ago.
tags:
- hackernews
- trending
---

(Image credit: Markus ‘Doom’ Gaasedelen
video presentation
)

* Copy link
* Facebook
* X
* Whatsapp
* Reddit
* Pinterest
* Flipboard
* Email

Share this article

12

Join the conversation

Follow us

Add us as a preferred source on Google

Newsletter

Get the Tom's Hardware Newsletter

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Contact me with news and offers from other Future brands

Receive email from us on behalf of our trusted partners or sponsors

By submitting your information you agree to the
Terms & Conditions
 and
Privacy Policy
 and are aged 16 or over.

You are now subscribed

Your newsletter sign-up was successful

 An account already exists for this email address, please log in.

Subscribe to our newsletter

A groundbreaking hack forMicrosoft’s ‘unhackable’Xbox Onewas revealed at the recent RE//verse 2026 conference. This console has remained a fortress since its launch in 2013, but now Markus ‘Doom’ Gaasedelen has showcased the ‘Bliss’ double glitch. Just as theXbox 360famously fell to the Reset Glitch Hack (RGH), the Xbox One has now fallen to Voltage Glitch Hacking (VGH).

RE//verse 2026: Hacking the Xbox One - YouTube

Watch On

Go deeper with TH Premium: CPU


(Image credit: Tom's Hardware)
* CPU scaling with DLSS
* Ryzen to the top: How AMD innovated in the gaming CPU market
* How ARM is working its way into PCs
* AMD CES 2026 gaming trends press Q&A roundtable transcript

“In 2013 some kind of iron curtain came down onsecurity, of the Xbox ecosystem, and the Xbox One never got hacked,” noted Gaasedelen in his introduction. The same is true of the Xbox One’s successors, and Microsoft was rightly proud. Seven years after its launch, Microsoft engineers would still assert that the Xbox One was “the most secure product Microsoft has ever produced.”



(Image credit: Markus ‘Doom’ Gaasedelen
video presentation
)

What made the Xbox One so secure, so special? Gaasedelen referenced prior work and presentations to convey this information. I’ve shared a summary slide about this, too, but let’s fast forward to the demo of the new Bliss hack, which takes place from about 46 minutes into the presentation.

Article continues below

Since reset glitching wasn’t possible, Gaasedelen thought somevoltage glitchingcould do the trick. So, instead of tinkering with the system rest pin(s) the hacker targeted the momentary collapse of the CPU voltage rail. This was quite a feat, as Gaasedelen couldn’t ‘see’ into the Xbox One, so had to develop new hardware introspection tools.

Eventually, the Bliss exploit was formulated, where two precise voltage glitches were made to land in succession. One skipped the loop where theARM Cortexmemory protection was setup. Then the Memcpy operation was targeted during the header read, allowing him to jump to the attacker-controlled data.

Image
1
 of
3
(Image credit: Markus ‘Doom’ Gaasedelen
video presentation
)
(Image credit: Markus ‘Doom’ Gaasedelen
video presentation
)
(Image credit: Markus ‘Doom’ Gaasedelen
video presentation
)

As a hardware attack against the boot ROM in silicon, Gaasedelen says the attack in unpatchable. Thus it is a complete compromise of the console allowing for loading unsigned code at every level, including the Hypervisor and OS. Moreover, Bliss allows access to thesecurity processorso games, firmware, and so on can be decrypted.

What happens next with this technique remains to be seen.Digital archivistsshould enjoy new levels of access to Xbox One firmware, OS, games. There could be subsequent emulation breakthroughs thanks to this effort. We also now have a route to making a Bliss-a-like mod chip to automate the precise electrical glitching required.

Stay On the Cutting Edge: Get the Tom's Hardware Newsletter

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Contact me with news and offers from other Future brands
Receive email from us on behalf of our trusted partners or sponsors

Whether PC users, our core readership, will be interested in actually emulating Xbox One, looks unlikely. The 2013 system’s game library is largely overlapped in better quality on the PC platform.



FollowTom's Hardware on Google News, oradd us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

TOPICS

Mark Tyson
News Editor

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.
