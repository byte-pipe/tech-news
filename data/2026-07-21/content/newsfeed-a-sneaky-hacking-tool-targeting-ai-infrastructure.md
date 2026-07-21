---
title: A Sneaky Hacking Tool Targeting AI Infrastructure Is Lurking in Victims’ Blind Spots | WIRED
url: https://www.wired.com/story/a-sneaky-hacking-tool-targeting-ai-infrastructure-is-lurking-in-victims-blind-spots/
site_name: newsfeed
content_file: newsfeed-a-sneaky-hacking-tool-targeting-ai-infrastructure
fetched_at: '2026-07-21T19:33:34.641194'
original_url: https://www.wired.com/story/a-sneaky-hacking-tool-targeting-ai-infrastructure-is-lurking-in-victims-blind-spots/
author: Lily Hay Newman
date: '2026-07-21'
published_date: '2026-07-21T16:08:44.724Z'
description: A new type of malware can worm deep into AI coding systems to steal data and logins—and can flip a “death switch” to destroy files and keep out real users.
tags:
- wired
- security
- security / cyberattacks and hacks
- cybersecurity
---

Save Story
Save this story
Save Story
Save this story

As AI tools proliferate and becomedeeply ingrainedin software development around the world,new researchfrom the cybersecurity firm Crowdstrike shows how attackers are actively targeting the AI toolchain to steal access credentials, gain deeper access to a target environment, exfiltrate sensitive data, and even destroy target files and systems—all while finding new ways to cover their tracks.

Researchers discovered a worm in the wild while investigating AI software supply chain attacks. Adam Meyers, CrowdStrike's senior vice president of counter adversary work, says that the company has not yet attributed the activity to a specific actor, but that it fits into larger evolutions in how attackers likeTeamPCP(which Crowdstrike tracks as “Altered Spider”) andNorth Korean groupsare targeting the AI software supply chain.

“This is one of the campaigns that we’ve seen showing that this is an emerging attack class,” Meyers tells WIRED. “As AI coding agents become the development standard, supply chain threats are evolving to exploit those trust relationships. For the first time we’re experiencing how much AI and the AI toolchain has played into the broader tech ecosystem.”

The worm CrowdStrike identified works in phases. First it does reconnaissance to assess the target environment. Then it looks for access tokens and other sensitive data, like cryptographic keys and server access credentials that it can deliver to attackers. As the malware gains privileges, it further unpacks itself and continues to grab credentials, particularly “npm" tokens that give access to key software package management servers and other development capabilities like pull requests.

The deeper the malware bores into the system, the more sensitive data it can grab. At this point, the malware can also deploy its destructive capability, or what Meyers calls a “death switch,” to destroy files or block legitimate access to the compromised infrastructure.

The key finding, though, is that much of the worm's malicious activity takes place in what are essentially blind spots, because so much of its behavior mimics legitimate actions. “It's like a needle in a haystack, except this is a needle in a needle stack,” Meyers says. “This looks very much like a lot of the automation organizations are using to build code, so it’s very difficult to detect.”

Meyers adds, too, that in these AI software development pipelines, it is harder to gather the data points that security scanners and analysis tools traditionally use to detect potentially suspicious activity.

“There’s a lot of telemetry overlap because legitimate AI coding systems are operating the same way as this worm, so it becomes very difficult to discern from the telemetry you have available to you what is legitimate and what is illegitimate,” Meyers says.

To hide in plain sight even more insidiously, the authors of the worm included time delays where various capabilities will execute hours or even days after the groundwork is laid, making it even harder for defenders to establish a cause and effect of certain events leading to certain outcomes.

Meyers says that Crowdstrike has been working on strategies to connect more of the dots, but he emphasizes that as AI software development explodes, there is a pressing need for all players to collaborate on structural solutions.

“It’s a limited detection surface because only so much of this activity is actually going to produce any sort of telemetry signal for us to look at,” Meyers says, “so it becomes extremely onerous to determine what is legitimate and what is illegitimate behavior.”

## Comments

Back to top
Join the discussion

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:Inside WIRED’s newsroom with Katie Drummond
* Trumpmocked Zuckerberg and Bezosby showing off fawning texts
* Big Story:I found Jesusat a drone show
* Apple is making your olderiPhone run faster and stay alive longer
* WIRED event:PepsiCo’s once-in-a-generation transformation
Lily Hay Newman
 is a senior writer at WIRED focused on information security, digital privacy, and hacking. She previously worked as a technology reporter at Slate, and was the staff writer for Future Tense, a publication and partnership between Slate, the New America Foundation, and Arizona State University. Her work ... 
Read More
Senior Writer
* X
Topics
cybersecurity
hacking
security
vulnerabilities
malware
artificial intelligence
You Can Now Sound the Alarm on AI Behaving Badly
Are you worried your AI chatbot is trying to build a bomb or leak personal information about you? There’s a website for that.
Will Knight
China Defies US Restrictions and Builds the World’s Fastest Supercomputer
The Chinese supercomputer LineShine was ranked as the fastest in the world, despite not using any GPUs.
Fernanda González
LastPass Users Had Their Data Stolen—Again
Plus: Former national security advisor John Bolton pleads guilty in classified-materials case, Microsoft helps take down major infostealer infrastructure, and more.
Lily Hay Newman
How People in China Keep Outsmarting Anthropic’s Geolocation Restrictions
As Anthropic tightens restrictions on access to Claude in China, users keep finding new workarounds, from proxy services to fake identities sourced on Telegram.
Zeyi Yang
What Happens if China Hacks the US Water Supply? I Went to a Secret War Game to Find Out
Burst water mains. Evacuated hospitals. In a closed-door simulation, insurers played out their response to a mass disruption by China’s Volt Typhoon hackers—and found a nightmare scenario.
Andy Greenberg
A Device Hidden in Cars Across the US Leaves Them Vulnerable to Hacking and Paralysis. Patch It Now
Dealerships installed alarms in millions of vehicles—and left them in even if the buyer didn’t want them. Now researchers warn they can be hacked to unlock, track, and disable cars.
Andy Greenberg
OpenAI Launches Full-Scale Effort to Patch Open-Source Bugs as It Takes on Anthropic’s Mythos
Amid concerns about AI models’ cybersecurity capabilities, OpenAI revealed an improved version of GPT-5.5-Cyber and its “Patch the Planet” initiative to fix open-source software bugs.
Lily Hay Newman
I Met With China’s Top AI Experts. They’re Freaking Out, Too
The AI arms race between China and the US has researchers on both sides worried about a “Chernobyl moment.”
Will Knight
The ‘Parasite of Parasites’ Has Been Discovered in the Tropical Forests of Borneo
A newly identified species of fungus attacks the famous “zombie mushrooms” that control ants.
Marta Musso
World Cup Scams Are Getting Harder to Spot
From fake tickets to cloned websites, AI is magnifying World Cup scams. Can fans distinguish between what’s real and what’s not?
Jumana Naim
I Built a Self-Improving AI, and So Can You
Experiments in using AI to build AI show that the future doesn’t just belong to the frontier labs.
Will Knight
Shut Those Laptops! Anthropic Puts Its Claude Cowork Agent on Your Phone
Claude Cowork now keeps working on tasks even after you close your laptop. It’s part of a larger push toward smartphone-controlled agents.
Reece Rogers