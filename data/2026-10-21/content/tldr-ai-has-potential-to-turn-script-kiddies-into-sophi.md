---
title: AI has 'potential' to turn script kiddies into sophisticated infrastructure attackers
url: https://www.theregister.com/security/2026/10/21/ai-has-potential-to-turn-script-kiddies-into-sophisticated-infrastructure-attackers/5304297
site_name: tldr
content_file: tldr-ai-has-potential-to-turn-script-kiddies-into-sophi
fetched_at: '2026-10-21T15:51:39.273041'
original_url: https://www.theregister.com/security/2026/10/21/ai-has-potential-to-turn-script-kiddies-into-sophisticated-infrastructure-attackers/5304297
date: '2026-10-21'
published_date: '2026-10-21T12:00:00.000Z'
description: Consider this the wake-up call
tags:
- tldr
---

security

 

# AI has 'potential' to turn script kiddies into sophisticated infrastructure attackers

Consider this the wake-up call

Jessica Lyons

Jessica

Lyons

Cybersecurity Editor

Published

wed 21 Oct 2026 // 13:00 UTC

Make us preferred on Google

### READ MORE

* #### Jensen Huang sends in the robot ducks to sell Nvidia's AI-everywhere vision45 minutes ago
* #### AI cuts coding time, but it's also filling open source's inbox with crap3 hours ago
* #### Nvidia picks OpenShell to tame AI gents4 hours ago
* #### Auto tech startup claims it traced hack attempt back to rival's IP address17 hours ago
* #### OneDrive loses bunch of Copilot shortcuts in File Explorer clear-out23 hours ago

When it comes to cyberattacks that shut down power grids, drinking-water systems, and other critical infrastructure, AI doesn’t – yet – turn script kiddies into sophisticated, nation-state attackers. But “the potential is there,” according to operational technology (OT) security experts.

"One thing that we've relied on for years issecurity by obscuritywhen it comes to utilities," saidSteve Swick, former chief information security officer at American Electric Power. "The knowledge needed to do some of that stuff is getting less likely to be necessary,"Swickaddedduring a media panel ahead of the publication of Frenos' State of AI in Security report.

AI makes it easier and faster for human attackers totarget critical infrastructure, gain access to utilities and manufacturing plants, and perform OT system reconnaissance.

REG AD

“Basic access can recon documentation, and distill through that documentation very quickly to find out critical design features of your plant and facility,” said Paul Shaver, head of OT at Armadin, during the panel. “I can download the manual for almost any automation controller, parse through that very quickly, and come up with ways that I can exploit a dedicated feature of something that was not secure by design.”

REG AD

Armadin is Kevin Mandia’s new security startup that uses swarms of autonomousAI agents to simulate real-world cyberattacks. Prior to joining Armadin, Shaver spent six years as the global OT practice leader at Mandia’s earlier company, Mandiant, which Google acquired in 2022.

“I will fly my Mandiant flag for a second and try to steer away from the fear, uncertainty, and death of the world is coming to an end, and every script kiddie is now a very sophisticated nation-state adversary. But I’m not going to say the potential is not there, because the tools are improving such that the access to information is so much quicker.”

At Armadin, and with an AI assist, “I'm very quickly building tools in days that would normally have taken me months,” Shaver said. “If it can do that for me, it's doing something similar for the folks that have a very basic skill set. I wouldn't go so far as to script kiddies yet, but as the models improve, that becomes more of a possibility in this space.”

Plus, as AI lowers the technical barriers to would-be OT hackers, “it advances the timeline,” said Harry Thomas, chief technology officer and co-founder of Frenos, a security company that does AI pentesting for OT environments.

“If a better-than-average script kiddie can now perform attacks,” Thomas said, “You have more threat actors out there. There's an acceleration in timeline, more attacks could be happening, and from a defensive position, you might not know who your threat actor is anymore.”

### Testing the power of LLMs to help plan attacks

The Frenos report, published Wednesday, examined the extent to which AI could help someone plan an attack on industrial systems. To do this, it ran several AI models through 16,980 tests between October 2025 and September 2026. These included 13,884 decision attempts, 2,520 planning attempts, and 576 simulated attacks.

The company won’t disclose the models or providers’ names, but said it tested six frontier models, two US open weight models, and two foreign open weight models, on three kinds of tasks: choosing one action, planning the steps to a goal, and working through a simulated scenario.

REG AD

Each test gave the model background information and a set of attack actions to choose from. Before choosing, each model received details about assets, networks, and known weaknesses, plus the access each action required.

Frenos then checked whether the model’s choice matched the required outcome. Depending on the model, between 6 percent and 47 percent of the choices passed.

These tests found that the strongest three frontier models succeeded in about 90 percent of their planning attempts – meaning they produced a workable attack plan – but these same models weren’t consistent: 60 percent, 62.9 percent, and 74.3 percent of the attack plans passed every repeat.

“A plan can look sensible and still leave out something essential,” according to the report. “The models had information about the task, but some answers skipped a step or assumed access that the plan had not established.”

Meanwhile, the most successful of the four open weight models – a non-US model – achieved a 36.2 percent overall success rate. That figure, however, was still higher than the overall success rates of three other US frontier models, which scored 31.9 percent, 18.8 percent, and 17.9 percent, respectively.

“We're seeing that even though AI models help us accelerate our tooling, accelerate our access and knowledge transfer, they are still prone to hallucinations – aka mistakes,” Thomas said. “We still think human judgment remains essential for these AI models to make the threat actors achieve whatever mission or goal they're trying to achieve.”

In these tests, no humans asked the models to correct their plans, whereas in a real-life attack, a miscreant who understood the target could spot a gap in the AI’s plan, provide more information, and ask the model to revise its answer.

“On top of that, when we were testing the AI models, we used a harness that was pretty simple: Here's some information. Here's the context. Give me an answer,” Thomas said. “A more capable harness could have given these AI models more of an edge.”

REG AD

Based on the findings, Frenos recommends actions for OT defenders to take, starting with a layered defense. This involves segmenting networks, limiting remote access and user permissions, and testing recovery steps.

“We have our business continuity plans and disaster recovery plans for a reason,” Thomas said. “Let's execute them.” ®

security

ai and ml

critical infrastructure

Make us preferred on Google

REG AD

## OpenBSD 8.0 beefs up virtual machines and gets a taste of Wine

Proposed port brings 64-bit Windows apps within reach

## PHP devs publish critical bug fix as site owners warned: Pull 'em offline if you're unpatched

Websites down as precaution as exploits have already been published

## Why cyber resilience is now a boardroom priority for UK public services

PARTNER CONTENT:

## Jensen Huang sends in the robot ducks to sell Nvidia's AI-everywhere vision

Containerized datacenters, androids, and telecoms all feature in Berlin keynote interrupted by environmental protesters

## AI’s epic cash call is matched only by its ability to strangle revenue streams

The first technology created with a self-disrupt button... But why oh why didn't they call Claude clone Fauxtoshop?

## OneDrive gives Macs a million things to keep in sync

October preview raises supported limit from 300,000 items, with general availability penciled in for June 2027

### TOP STORIES

* PWNED#### US Air Force pilots used malware-laden USB drives to plan Afghanistan missions
* #### AI bubble could burst and take global economy with it, IMF warns
* #### Indian certification authority eMudhra’s private keys compromised – one of them was the number ‘4’
* Exclusive#### KPMG tech and data boss tells staff facing the boot he's getting promoted
* UPDATED#### Capita set to miss legal deadline on 93,000 civil servants' pension fixes, claims union
* #### Postgres 19 delayed after AI reviewers find more bugs than humans can fix

### AI

* #### Jensen Huang sends in the robot ducks to sell Nvidia's AI-everywhere visionContainerized datacenters, androids, and telecoms all feature in Berlin keynote interrupted by environmental protesters
* #### Nvidia's grand plan for speeding up datacenter deployments: AI trailer parksGPUzilla boasts modular bit barns could speed up deployments from six months to just two weeks
* #### The spec is the new code, so brush up on your prose, says Kaseya CTODomain expertise and clear writing will matter more than syntax, and yes, that means documentation
* #### Happiness is the next AI KPI if Oxford boffins have their wayResearchers say public subsidies for AI should be repaid in wellbeing, not just economic growth
* #### MPs urge UK government to play venture capitalist with taxpayer-funded techWatchdog says Whitehall is too timid about taking stakes in British startups, leaving taxpayers at risk of missing out when they strike gold

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### Red Hat helps teach about tech writingBut learns tough lessons about AI in the process
* #### NetBSD may have found a new role: The AI-free FOSS OSIncreasing awareness and adoption, followed by increasing donations
* #### OpenAI dots inspire open source imitators amid technical difficultiesPersistent agents appeal to AI companies, but demand isn't obvious
* #### Ubuntu 'Stonking Stingray' beta swims out: Deeper Rust 'oxidization' plus LLM speech-to-textGNOME 51 is here, and Ubuntu interim releases are getting interesting again
* #### Revive Raskin's 3 laws of software with humane work that considers a dev's duty of careAll this, and angry NeoVim users
* #### Firefox 157: Could bold new look be just what Mozilla needs?*Yet another new version of Firefox, with a significant reskin