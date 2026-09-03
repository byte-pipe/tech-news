---
title: AliExpress accused of fingerprinting shoppers with silent audio trick that also muted a dev's headphones
url: https://www.theregister.com/security/2026/08/24/aliexpress-accused-of-fingerprinting-shoppers-with-silent-audio-trick-that-also-muted-a-devs-headphones/5291662
site_name: tldr
content_file: tldr-aliexpress-accused-of-fingerprinting-shoppers-with
fetched_at: '2026-09-03T14:53:19.754968'
original_url: https://www.theregister.com/security/2026/08/24/aliexpress-accused-of-fingerprinting-shoppers-with-silent-audio-trick-that-also-muted-a-devs-headphones/5291662
date: '2026-09-03'
published_date: '2026-08-24T12:32:00.000Z'
description: Sawtooth waves you can't hear still mess with your Bluetooth. Firefox and Brave say they've got you covered
tags:
- tldr
---

Security

 

# AliExpress accused of fingerprinting shoppers with silent audio trick that also muted a dev's headphones

Sawtooth waves you can't hear still mess with your Bluetooth. Firefox and Brave say they've got you covered

Connor Jones

Connor

Jones

Cybersecurity reporter

Published

mon 24 Aug 2026 // 13:32 UTC

Developer Matt Callaghan claims he caught Alibaba's B2C website, AliExpress,  trying to track web users by playing sounds through browsers vulnerable to audio fingerprinting.

The software engineer drew attention to the issue late last week after investigating why his Bluetooth headphones stopped playing music whenever he visited the AliExpress website.

“Recently I ran into a strange problem with my Bluetooth headphones,” Callaghanwrote. “They support multipoint Bluetooth audio, so they can be connected to my PC and phone at the same time. Normally, the PC takes priority playing audio, with my phone being able to play audio when nothing is playing on the PC.

REG AD

“Usually I listen to music on my phone but with notifications or YouTube playing through the PC, this works reliably until I open an AliExpress page in Firefox or Chrome.

REG AD

“Shortly after loading the AliExpress homepage, audio from my phone would stop playing. Closing the AliExpress tab fixes it immediately. Muting the tab/Firefox/Windows does not help, and there is no visible video, music, or other media playing on the page.”

Callaghan tried to find any hidden conventional media elements but found nothing. Further digging revealed two audio scripts that he said were “extremely obfuscated” within AliExpress's browser security and anti-abuse tooling.

He said the scripts built a WebAudio graph that introduced a sawtooth oscillator to generate a waveform, an analyzer to measure the result after the waveform passes through a browser’s audio implementation, and a script to read the associated frequency data.

The scripts set the audio’s gain to zero, meaning the end user won’t hear anything, but the WebAudio graph will still be processed by the browser.

“This is very different from an autoplaying video,” said Callaghan. “There is no media element for the browser's normal tab mute control to stop. As far as the page is concerned, it is performing live audio processing.

“In my case, that appears to have been enough for Firefox or Windows to keep the Bluetooth audio path active, preventing my multipoint headphones from switching cleanly back to the phone.”

Callaghan found further evidence in the code looking for data related to screen dimensions, device memory, browser plugins, WebGL rendering, mouse events, and more.

As well as signs that AliExpress is encrypting data and sending it to its telemetry services, the developer said all of it amounts to “a fairly comprehensive browser and device fingerprint.”

REG AD

The Registerhas asked Alibaba to comment.

Despite Callaghan saying he could reliably reproduce this issue on both Firefox and Chrome,Firefoxissued aXtatementsaying its anti-fingerprinting technology thwarts AliExpress’ tracking tricks.

## MORE CONTEXT

* ### Google Chrome lacks protection against one of the most basic and common ways to track users online
* ### Your browser has ad tech's fingerprints all over it, but there's a clean-up squad in town
* ### UK ICO not happy with Google's plans to allow device fingerprinting
* ### Meta, Spotify break Apple's device fingerprinting rules – new claim

It pointed to ablog postfrom Tom Ritter, a security engineer on the Firefox team, who explained that as of version 118 (September 2023), the protections it introduced eliminated the efficacy of WebAudio-based fingerprinting.

These protections are not designed to stifle fingerprinting efforts at the source. Instead, they work to group all users together, making it look like all fingerprinted users are the same, effectively nullifying the tracking attempts.

For 99.24 percent of users, they fall into one of three “buckets” – user categories delineated by types of hardware. The vast majority fall into buckets one and two:

* Bucket one: x86/x64 CPUs lacking FMA (Fused Multiply-Add) instructions
* Bucket 2: x64 CPUs with FMA instructions

And for the remaining 0.76 percent, the fingerprinting script failed entirely, according to Firefox’s data.

However, Ritter said there are 48 users worldwide who do not fall into the three buckets, or the 0.76 percent whose machines did not allow the scripts to run. These 48 users fell into 23 other minuscule buckets, which means they are not grouped into the masses like the rest, and so fingerprinting is more effective on this vast minority of users.

REG AD

“This is very unfortunate, as it makes these users completely unique, but it is also not terribly unusual - computers are weird and these results could have been caused by badRAM, a CPU bug, or possibly some crazy architecture (LoongArch??),” said Ritter.

“But at the end of the day, WebAudio fingerprinting is nearly useless. I don't expect browser fingerprinting to disappear from websites entirely (unless some regulatory action occurs, fingers crossed) - it's still going to be effective against a majority of users on the web, but at least for privacy-focused browsers, it should be wildly less effective.”

Brave, maker of the eponymous privacy-centric browser, alsoXeeteda response to Calalghan’s findings, saying it has protected users from fingerprinting for six years. “Brave injects random data into the browser's output so you show a different fingerprint to different sites. This fingerprint also resets across sessions.

“For added protection, we also block the specific scripts used by AliExpress for the tracking method mentioned above. Again, this is done by default for all Brave users. You don't have to change any settings to be shielded from this audio fingerprinting.”

Ritter said Chrome and Safari “probably have defenses against this [brand of fingerprinting].”

Safari deploys Advanced Tracking and Fingerprinting Protection to prevent WebAudio-based tracking and other methods of fingerprinting. It works differently to Firefox, though, injecting audio errors into an audio buffer, instead of trying to lump all users into an identical bucket.

Chrome, on the other hand, does not aggressively protect users from fingerprinting, as privacy consultant Alexander Hanffsaid earlier in the year.

"There are at least thirty distinct fingerprinting techniques that work in Chrome right now, today, as you read this," he wrote.

"Not theoretical attacks from academic papers that might work under laboratory conditions – real, production techniques deployed on millions of websites to identify and track you without your knowledge or consent." ®

Updated 08/25 at 1805 GMTto clarify the behavior was observed on AliExpress, which is Alibaba's B2C web site for small-scale purchases.

google

firefox

chrome

alibaba

security

web browser

safari

REG AD

AI AND ML

## Salesforce blames its Claude addiction for denting profit margin guidance

But investors hear CRM giant is now in 'refinement mode,' picking models more carefully

AI AND ML

## Nvidia buys Hugging Face for $12.9B, promises not to squeeze too hard

GPU giant pledges to keep the model hub open to the entire AI ecosystem

devops

## Platform Engineering 2.0: your platform was built for a different era. AI just exposed it

PARTNER CONTENT: Platform engineering won the argument. Now it has to grow up fast and evolve for the AI era.

cyber-crime

## Cybercrooks trawl Fishbrain to net password hashes

Armed with password hashes and salts, attackers could already be kraken those creds

COLUMNISTS

## The teen Bill Gates has answers to the AI-pocalypse the 70-year-old Gates has forgotten

Hacking education to thrive in the AI world is the first and best step in keeping control

OFFBEAT

## 'Uber rapture' leaves passengers and drivers behind in Nigeria and Uganda

No time for a fare-thee-well as app hails a ride out of two more markets

### TOP STORIES

* security#### Researcher shows how Claude Code can be tricked simply by asking it to summarize a website
* virtualization#### Broadcom pledges to lock down open source Python, Java libraries
* science#### German-Japanese researchers invent electricity-free tech that could cool datacenters
* Legal#### Nuisance-call blocker fined £190k for being a nuisance caller
* security#### Security vets rally around $4 paper password books for sale in Australia
* NETWORKS#### A lot of datacenter networks are run by absolute clowns. Not Amazon's

### AI

* ai and ml#### Zuck's Muse to Spark joy with open weights release 'soon'While you wait, Meta says it’s taught the model to stop wasting tokens and ask for help a bit more often
* ai and ml#### With Gemini 3.8 Flash, Google reminds everyone it's still in the raceAI model scores well, runs fast, and doesn't cost too much (yet)
* security#### AI agents carried out every step of this ransomware attack – then left the victim an 80-page security auditAdding insult to injury
* ai and ml#### Anthropic promises zero data retention – but customers must check it workedMore compliance-friendly stance could boost appeal of Fable
* Security#### Attacker stole a METR API key, used $600K worth of credits, and no one noticed for weeksThe model provider gave METR the credits for free. An actual customer would not have been so lucky

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### Haiku OS rises / Beta 6 sails open web / Virtual winds fly fastA real alternative to running some kind of FOSS Unix clone
* #### Offshoots of cancelled TrueNAS Core upgrade to FreeBSD 15Exeunt zVault stage right; enter FreeCORE and BSDnas
* #### Debian votes to let contributors code with AIDisclosure optional, quality mandatory
* #### LibreOffice 26.8 is out – local first, and with no AIIt looks a bit clunky, but it does the job – and on your own computer
* #### Keepers of Noble Numbats to be offered a Resolute Racoon: Ubuntu 26.04.1 is comingGRUB's up for furry new update
* #### AROS, the FOSS recreation of AmigaOS, comes to Raspberry PiPlus: new official Amiga-branded hardware is coming