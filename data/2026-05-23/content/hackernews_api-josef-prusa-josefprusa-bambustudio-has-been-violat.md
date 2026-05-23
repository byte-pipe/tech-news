---
title: 'Josef Prusa (@josefprusa): "BambuStudio has been violating PrusaSlicer AGPL license since their fork, with the same networking binary black box in question today. Why are they willing to burn the goodwill over it? There''s something most have sensed but never seen it all in one place, the five-law framework China built between 2017 and 2023 ⤵️ So maybe their hand is forced as their "network" is too valuable already? Each law on its own, interesting, okay... Read them together, and add any Chinese company with big reach to the mix you get the complete picture. 1) National Intelligence Law (2017) All organizations and citizens must "support, assist, and cooperate" with intelligence work. The same law makes it illegal to disclose that cooperation happened. Cooperation is mandatory, and silence about it is mandatory too. 2) Cryptography Law (2020) Commercial encryption must be state-approved and state-reviewed. When authorities request it, companies must provide decryption keys or plaintext.
  The state on both sides of that equation is the same one. 3) Data Security Law (2021) Article 2 gives the state extraterritorial reach over data that touches Chinese national security or public interests. So EU/US data hosting does nothing to make it safe, because jurisdiction follows the company, not the server location. 4) Counter-Espionage Law revision (2023) The general definition of espionage was expanded to cover "documents, data, materials, or items related to national security and interests." Industrial data is one of the intended targets since the revision. 5) Network Product Security Vulnerability regulation (2021) Any company or researcher that discovers a software vulnerability must report it to MIIT within 48 hours. From there it flows to CNNVD (China National Vulnerability Database of Information Security), operated by the 13th Bureau of the Ministry of State Security. Microsoft''s threat intelligence team documented Chinese state-hacker zero-day usage rising after this took
  effect. Shows the willingness to use the “tools” China built. Together they describe a system with no neutral exits. Cooperation is required, encryption is real but the spare keys live at the ministry, jurisdiction follows the company across borders, industrial data is in scope, and discovered vulnerabilities flow to an intelligence agency 😬 3D printing became strategic for China in 2020 and joined the “Made in China 2025” plan soon after. Why does 3D printing matter so much? 1/x" | XCancel'
url: https://xcancel.com/josefprusa/status/2054602354851254330
site_name: hackernews_api
content_file: hackernews_api-josef-prusa-josefprusa-bambustudio-has-been-violat
fetched_at: '2026-05-23T19:29:56.682326'
original_url: https://xcancel.com/josefprusa/status/2054602354851254330
author: Tomte
date: '2026-05-23'
description: BambuStudio has been violating PrusaSlicer AGPL license since their fork
tags:
- hackernews
- trending
---

Josef Prusa

@josefprusa

May 13

BambuStudio has been violating PrusaSlicer AGPL license since their fork, with the same networking binary black box in question today. Why are they willing to burn the goodwill over it?
There's something most have sensed but never seen it all in one place, the five-law framework China built between 2017 and 2023 ⤵️

So maybe their hand is forced as their "network" is too valuable already? Each law on its own, interesting, okay... Read them together, and add any Chinese company with big reach to the mix you get the complete picture.

1) National Intelligence Law (2017)
All organizations and citizens must "support, assist, and cooperate" with intelligence work. The same law makes it illegal to disclose that cooperation happened. Cooperation is mandatory, and silence about it is mandatory too.

2) Cryptography Law (2020)
Commercial encryption must be state-approved and state-reviewed. When authorities request it, companies must provide decryption keys or plaintext. The state on both sides of that equation is the same one.

3) Data Security Law (2021)
Article 2 gives the state extraterritorial reach over data that touches Chinese national security or public interests. So EU/US data hosting does nothing to make it safe, because jurisdiction follows the company, not the server location.

4) Counter-Espionage Law revision (2023)
The general definition of espionage was expanded to cover "documents, data, materials, or items related to national security and interests." Industrial data is one of the intended targets since the revision.

5) Network Product Security Vulnerability regulation (2021)
Any company or researcher that discovers a software vulnerability must report it to MIIT within 48 hours. From there it flows to CNNVD (China National Vulnerability Database of Information Security), operated by the 13th Bureau of the Ministry of State Security. Microsoft's threat intelligence team documented Chinese state-hacker zero-day usage rising after this took effect. Shows the willingness to use the “tools” China built.

Together they describe a system with no neutral exits. Cooperation is required, encryption is real but the spare keys live at the ministry, jurisdiction follows the company across borders, industrial data is in scope, and discovered vulnerabilities flow to an intelligence agency 😬

3D printing became strategic for China in 2020 and joined the “Made in China 2025” plan soon after. Why does 3D printing matter so much? 1/x

Jeff Geerling

@geerlingguy

May 12

Bambu Lab 3D printers: never again.

They're breaking the open source social contract (for the nth time...), and I'm past hoping they'll amend their ways.

youtu.be/watch?v=eb48MdtN…

May 13, 2026 · 4:39 PM UTC

 61

 371

 2,270

 188,313

Josef Prusa

@josefprusa

May 13

Two reasons this is especially dangerous in 3D printing:

First, Made in China 2025 designates essentially every advanced technology as strategic, so industrial data broadly fits the "national security and interests" definition.

Second, 3D printers concentrate at the places where new IP is created. R&D departments, prototype shops, defense suppliers, university labs, hardware startups. The machine sits next to the thing being invented. And the slicer sits on your computer with the same data and access you have.

I'm not claiming I know what's happening inside Bambu. This is relevant to every Chinese manufacturer, not just 3D printing. It's cameras, it's cars, it's the free AI models in your coding tools collecting your data.
Six years after China's wildly successful subsidies for 3D printing began, we are the only desktop Western manufacturer remaining. Let that sink in.

My personal guess is that the subsidies are not designed for the benefit of Western consumers. What do you think? 2/x

 5

 21

 553

 20,645

Josef Prusa

@josefprusa

May 13

What does the PrusaSlicer AGPL violation actually look like?

PS is licensed under AGPL-3.0. That's the strongest copyleft license there is. It's simple: you can fork it, you can build a business on it, you can ship it commercially. But any derivative work has to stay open source too. You take from the community, you give back to the community. That's the social contract. PS is a fork of Slic3r and even though 90+% of the codebase is now written by us, we are proud about the heritage.

BambuStudio (BS) is a fork of PrusaSlicer (PS). They published the slicer parts, that's fine. The networking plugin, the part that actually talks to their cloud, is closed-source. Just a binary black-box.

The standard defense for something like this is "the plugin is a separate work, so it's not subject to copyleft." That argument falls apart on contact with the actual software. BS cannot do its primary job without the plugin. The plugin cannot do anything without BS. They are not two products that happen to talk to each other, they are one product split across two files for PR license-laundering convenience 😒

Under AGPL, that's still a violation. You don't get to keep the copyleft piece closed by moving it across a function call boundary and calling it a separate work. The license they inherited from us doesn't allow that. The OrcaSlicer inherited the same license by forking BS and follows the rules.

Most people miss that the networking blob isn't even bundled inside BS. It downloads itself at runtime.

So you can audit BambuStudio's open source code all you want. You cannot meaningfully audit the part that actually talks to the cloud. It lives outside the published software supply chain, arrives from a CDN you don't control, and can be replaced from one launch to the next without anyone outside Bambu having a chance to look at it first 😬

I flagged this exact architecture publicly in March 2023. The same architecture is in place today.

xcancel.com/josefprusa/status/1634…
 

Back then we considered legal action. We seriously did. But the practical reality: PrusaSlicer is software, not hardware. There's no boxed product crossing customs to stop - only real possibility which would make them comply. And jurisdiction for the licensee lands in China, which means the case lands in a Chinese court applying Chinese law to a Chinese company.

The AGPL is a license. A license without a viable enforcement path is, in practice, a suggestion.
So Bambu got away with it. The networking blob kept doing whatever it does. And many “we are sorry”s later we land here today - legal threats to a small developer opening their tiny black box 🤦‍♂️ 3/x

 10

 40

 637

 27,792

Josef Prusa

@josefprusa

May 13

A funny story from the very beginning, because I want to be clear how long this has been on our radar.

PrusaSlicer 2.4 introduced opt-in anonymous telemetry. Shortly after release, we started seeing entries in our database labeled "BambuSlicer." We hadn't heard of BambuStudio yet. Their internal builds were accidentally configured to send telemetry to our servers instead of theirs 🤭

That's how we found out a fork existed, before they publicly launched. And after launch the community had to call out BambuLab to release the BambuStudio source code in accordance with the AGPL license 
xcancel.com/Bryan_Vines/status/154…

We've known what this software is and where it came from since day one.

xcancel.com/josefprusa/status/1542…
 4/4

 9

 26

 554

 22,633

DavidHasbun

@TheDavidHasbun

May 17

Replying to 
@josefprusa

Bambu is getting downright offensive about this.

They will brick your printer if you don't let them spy on you.

DavidHasbun

@TheDavidHasbun

May 15

Bambu Labs has just effectively bricked every printer that does not send their prints through Bambu Labs servers for them to spy on you.

These are expensive, top of the line printers that many people including myself rely on as a source of income.

I now have about $1,000 dollars of hardware sitting at my home that is useless unless I allow a Chinese company to spy on me and steal my designs.

@BambulabGlobal
 would you like to explain this crap?

@BambuLabSupport
 any comment?

@FTC
 this HAS to be illegal especially for a foreign company to do to American consumers. Is it possible to ban them from selling printers in the US entirely if they insist on using them to spy on US citizens and steal our work?

@bbb_us
 this is a horrific business that preys on its customers. If you look through my profile I have tagged them in many concerns which they have ignored. How do I go about filing a formal complaint against them?

 2

 2

 16

 1,653

Josef Prusa

@josefprusa

May 17

😬

 1

 9

 1,011

more replies

International Cyber Digest

@IntCyberDigest

May 14

Replying to 
@josefprusa

To be honest, Josef, I really wanted to buy a Prusa printer. But the value proposition isn't there compared to Bambulab. Perhaps you could focus on that.

Until then, the Bambulab printers I have are in LAN mode and blocked from initiating outbound traffic.

 4

 34

 4,026

Barnacules Nerdgasm

@Barnacules

May 14

Replying to 
@josefprusa

I've been calling this out for years 
@josefprusa
. It's not just PrusaSlicer either, they have "allegedly" stolen from more open-source projects than I can count! They have refused to allow any 3rd party code reviews ever since they got caught lying about PrusaSlicer.

 2,015

Hamilton PrintWorks

@HPW3D

May 13

Replying to 
@josefprusa
 
@YukonK9

Unfortunately many in the 3D printing space are naive when it comes to security and sovereignty concerns like this. To many, it’s “cheap = good for the consumer” and that’s it.

Western governments share blame though, they have been shockingly complacent about how China competes in this industry. We’ve got to start subsidizing local homegrown manufacturing while tariffing foreign competitors.

 4

 1

 51

 5,184

This is Greg

@Greg_TheBuilder

May 13

Replying to 
@josefprusa

Whenever anyone asks for a 3d printer rec, I dont flinch and suggest Prusa over Bambu everytime

 4,153

Garrett Kinsman

@GeKinsman

May 13

Replying to 
@josefprusa

I had my agent dig through their network tool and it found that it’s sending everything home even in LAN mode

 7

 1

 47

 6,014

Aidas Lemon

@Lomanonis

May 13

Replying to 
@josefprusa

This is all rather unsettling, but you still dont have anything to offer against H2D that was released more than a year ago, and even the AMS of 2022. Regarding specs on paper you have something that is close, but in reality your products are not state of the art anymore unfortunately. And yet, you decide to waste your focus on useless styling of oak edition. Did LVMH aquire you or smth? 
As it stands, its not even about the price. Customers are forced to choose between security risk and inferior technology, and well, as we can see, most decide to take the risk.

 12

 35

 6,168

EG33

@084bodicantbias

May 13

Replying to 
@josefprusa

lol they are like huawei for 3d printers, not surprising at all.

 22

 2,917

Mitch
@LilApe1990

May 13

Replying to 
@josefprusa

Bambu lab wants to force everyone to use their slicer and cloud so they can spy on you and monitor your prints. Its as simple at that. Nobody else in this industry tries to force you to use their slicer quite like bambu lab does.

 3

 18

 2,557

2disbetter

@2disbetter

May 13

Replying to 
@josefprusa

I don't have anything to offer with how to handle this, but I just wanted you to know that I am a loyal Prusa customer who has used your printers awesome things (at least to me). As of now, Prusa is the only printer I would buy.

 13

 2,513

Reza
@goofieguru

May 13

Replying to 
@josefprusa

Maybe, but it looks more like standard predatory capitalism. Elegoo is there, also chinese, much better with open source and costs a fraction of the X1

 2,288

Azzys Design Works

@AzzyDesignWorks

May 13

Replying to 
@josefprusa

Jo, 

I understand the playbook. I understand how they use the world's law to profit and dominate. 

What's the West to do, to combat it realistically?

 1,578

Clay White
@ClayinVA

May 13

Replying to 
@josefprusa

Or we could ban their IP under DOD regulations and mark their patents as open source if they want to play China games. Nothing says we have to allow them use of the DCMA.

 1,101

NVRMOR
@NVRMOR23

May 13

Replying to 
@josefprusa

Im good paying 50% less than your stuff for better qualitiy and filling up China's datacenters with my plastic tchotchkes.

 886

Keith
@petllama

May 14

Replying to 
@josefprusa

Then fix your pricing.

I can get an A1 with AMS that prints flawlessly for about $400

Or I can (and have) pay $1100 for a single color prusa that provides the same print quality.

 1

 4

 615

Adam
@fknrdcls

May 14

Replying to 
@josefprusa

Yes, please stop sending your innovations directly to the CCP.

 875

xRadiant
@x7radiant

May 14

Replying to 
@josefprusa

bambu really seems to be trying hard to push customers away lately 😕

 1,548

Chris Fraser

@defrisselle

May 13

Replying to 
@josefprusa

All talk till lawyers start filing court actions
I'm not seeing much of a way Bambu Lab can stop Oracslicer from downloading their binary network module blob, since it's in their AGPL'd code They would have to figure out an outside download authorization method

 1,314

The Lizard King
@HappyLizard69

May 16

Replying to 
@josefprusa

I haven’t trusted Prusa since I saw this man put his own face on a sticker 

Bambu for the win

 3

 346

Niklas Förstberg
@nforstberg

May 17

Replying to 
@josefprusa

IT seems China is waging a silent war against the west, and we just happily go along.

 392

Dennis Moule
@Rum_Race

May 13

Replying to 
@josefprusa
 
@stlDenise3D

Awesome post. I refuse to pay musk for my long winded ramblings. It cracks me up when one Canadian politician demands another fix Chinas ethics & humanity. Easy stop enabling from US multinationals & CCP financed. That’s what the 25% tariff is about stopping enabling

 1,623

T Ξ S L Λ Algo

@TeslaAlgo

May 18

Replying to 
@josefprusa

Same thing with Home Security Cameras Made in China.. Cheap, very Cheap, but most likely the CCCP has access to your WiFi network and beyond..

 1

 130

cb

@rbe_01

2h

Thank you 
@josefprusa
 for posting this. Putting these 5 laws together show, in my mind, that Chinese products can't be trusted. At all. CCTV cameras, routers are what a lot of use and are some of the most insidious. I've been considering a 3D printer and I think I'll opt for a home brew. These 5 laws should be shared far and wide if for no other reason than simple awareness of what we're up against.

 8

Gary
@BWGaryP

May 17

Replying to 
@josefprusa

There is zero reason for the network plug-in to not be open source. Any claim it's about security is absolute rubbish. You do not attempt to protect a remote device or server by needing the client side (i.e network plug-in) to remain secret.

 529

Oliver Draxler
@FadiA85308728

May 20

Replying to 
@josefprusa

Stop crying and weining and go for one focus on updating your shitty printers. Your brand is dead, outdated, bad designs. Again outdated...rather then crying spend your time to make better printers....start by copying Bambu....
Loser.

 50

TechThatOut

@domo326

May 15

Replying to 
@josefprusa

Noooo I have so many Bambu printers. Time to switch teams from Green to Orange.

 488

Backyhouse

@backyhouse

May 16

Replying to 
@josefprusa

@grok
 given this legislation and law Is it likely that sensitive designs printed on bambulab printers are accessible under these laws?

 1

 600

5465 ¹
@mrdaiber

May 15

Replying to 
@josefprusa

i just have 3k of 
@BambulabGlobal
 printers in my shopping cart. Will not pull the trigger now, considering that I'm being locked in.

 1

 638

Cooper

@CooperZurad

May 13

Replying to 
@josefprusa

yeah this is absolutely insane.

 1,155

@_@

@dysinger

May 17

Replying to 
@josefprusa

I wanted to buy a 
@BambulabGlobal
 printr but their behavior made me decide otherwise. Too bad. Seems like a good printer. I can't stomach license violators and bad actors/bullies though. F that.

 149

krrawn

@krrawn

May 13

Replying to 
@josefprusa

Oh, are we still pretending international law exists?

 1,103

Load more