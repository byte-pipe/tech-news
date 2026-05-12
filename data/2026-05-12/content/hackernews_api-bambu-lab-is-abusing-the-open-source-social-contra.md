---
title: Bambu Lab is abusing the open source social contract - Jeff Geerling
url: https://www.jeffgeerling.com/blog/2026/bambu-lab-abusing-open-source-social-contract/
site_name: hackernews_api
content_file: hackernews_api-bambu-lab-is-abusing-the-open-source-social-contra
fetched_at: '2026-05-12T19:39:10.813131'
original_url: https://www.jeffgeerling.com/blog/2026/bambu-lab-abusing-open-source-social-contract/
author: rubenbe
date: '2026-05-12'
published_date: '2026-05-12T09:00:00-05:00'
description: 'Last year I said I''d probably never recommend another Bambu Lab printer again. I still use my P1S, but after Bambu Lab started pushing their always-connected cloud solution as the new default: I blocked the printer from the Internet via my OPNsense Firewall I stopped updating the firmware I locked the printer into Developer mode I deleted Bambu Studio and started using OrcaSlicer I had to do that to keep it under my control, instead of Bambu''s.'
tags:
- hackernews
- trending
---

# Bambu Lab is abusing the open source social contract

May 12, 2026

Last yearI said I'd probably never recommend another Bambu Lab printer again.

I still use my P1S, but after Bambu Lab started pushing their always-connected cloud solution as the new default:

* I blocked the printer from the Internet via my OPNsense Firewall
* I stopped updating the firmware
* I locked the printer into Developer mode
* I deleted Bambu Studio and started usingOrcaSlicer

I had to do that to keep it undermycontrol, instead of Bambu's.

But I'm weird—I acknowledge that. I'm one of those crazy ones who likes toown something they purchased, and not have the company watch everything I do with hardware I paid for.

Bambu Lab could've left the status quo at that, and I wouldn't be writing this blog post.

But they didn't.

## What happenedthistime?

For context:OrcaSliceris a fork of the open source projectBambu Studio, which is a fork ofPrusa Slicer, which is a fork ofslic3r. (They are all licensed under theAGPLv3 open source license).

OrcaSlicer already has to dance around Bambu's weird default setup whereevery file you print goes through Bambu's servers, meaning they can see everything you ever print on your printer.

That is, unless you're like me and you run it inDeveloper mode, and completely block it from the Internet on old firmware.

Some peopleareokay with using OrcaSlicer and printing through Bambu's cloud. It's convenient if you're on the road and want to start a print on your printer at home, without managing your own VPN.

I run my own WireGuard VPN, so I don't need that, but I understand not everyone has the resources to manage their own remote access.

Bambu saw a fork of OrcaSlicer that allowed you to use all your printer's features without having to route prints through Bambu's cloud calledOrcaSlicer-bambulaband was like, "You know what? No. For the 0.1% of power users who want to run OrcaSlicer without the cloud delivery mechanism like we have in our AGPL-licensed Linux Bambu Studio code... no. Youhaveto use our app, andonlyour app."

So they threatened that OrcaSlicer fork's developer with legal action for things that developerdidn'tdo. For example, they indicated the fork used an impersonation attack, despite the fork using Bambu Studio's upstream codeverbatim.

These are very serious public accusations.

Bambu Lab did not write to me with these specific public claims first. They also refused my request to publish the full correspondence. Instead, they published a one-sided public statement where I cannot reply directly.

In practice, this presents me to the public as someone bypassing security, impersonating their client, and creating a risk to their infrastructure. I reject that characterization.

—OrcaSlicer-bambulabs developer's response

Bambu is abusing the open source social contract, and using their legal might, to suppress a tiny number of their users1, for who knows what reason.

It seems dumb to me, because it would've been easier (and more profitable) to do nothing at all2. Instead, theywrote a blog post blaming an individual open source developerfor their own infrastructure and security problems.

This is where the actual issue arises: the modification in question worked by injecting falsified identity metadata into network communication.

In simple terms: it pretended to be the official Bambu Studio client when communicating with our servers.

—Bambu Lab blog post

I don't think they understand open source culture. Security either, if a public user agent string is their only protection against DDoS attacks...

Instead of finding solutions to ecosystem problems and building a more secure platform, Bambu is putting devoted power users like the fork's developer on blast3.

When tensions flared last year, they wrote asimilar blog postblaming community backlash on 'unfortunate misinformation'. I imagine they meant speculation from community members (like myself) frustrated the whole software ecosystem and ownership model was turned upside down post-purchase.

This year they're blaming one developer of a tiny slicer fork for thepotentialimpact he could have on their entire cloud infrastructure.

It creates structural vulnerability. If this method were widely adopted or incorrectly configured, thousands of clients could simultaneously hit our servers while impersonating the official client. Our systems would have no way to distinguish traffic, because the requests would look identical.

—Bambu Lab blog post

I love how they frame this as a developer trying to impersonate their app, when he's literally usingthe same AGPL-licensed code their Linux app uses.

I find itdoubly ironicsince their own forkcaused Bambu users' telemetry to hitPrusa'sservers back in 2022, and (to my knowledge) Prusa didn't snap back with a C&D.

They spent the rest of their blog post talking about vulnerabilities, bugs, and instabilities—as if that has anything to do with a developer using upstream code verbatim in his fork.

Maybe they could take a new approach and just not lock down their whole ecosystem in the first place.

But who am I kidding? Nothing I say, and no amount of complaining in the comments below, seems to help Bambu see the fault in their ways.

Spending a little more for a printer from another company just might do it, though.

Louis Rossmann posted a video sayinghe'd pledge $10,000to help the open source dev fight Bambu's legal threats. And I'd happily chip in too, but that's only usefulif the dev wants to put himself back in Bambu's crosshairs.

The better play might just be to skip Bambu altogether.

1. The OrcaSlicer fork in question didn't seem to have much uptake outside of a very small subset of users prior to Bambu Lab's cease and desist order.↩︎
2. Maybe ask for the fork to not include "bambulabs" in the name, since that could be a reasonable trademark-related demand.↩︎
3. The fork's developer mentioned "I previously helped Bambu Studio users with Linux and Wayland issues, including on Bambu Lab's own GitHub. That makes it especially absurd to me that I am now being publicly presented as someone dangerous to their infrastructure."↩︎