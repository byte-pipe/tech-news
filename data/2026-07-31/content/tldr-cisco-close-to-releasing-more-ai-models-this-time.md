---
title: Cisco close to releasing more AI models, this time for deep networking ops
url: https://www.theregister.com/networks/2026/07/28/cisco-close-to-releasing-more-ai-models-this-time-for-deep-networking-ops/5279350
site_name: tldr
content_file: tldr-cisco-close-to-releasing-more-ai-models-this-time
fetched_at: '2026-07-31T06:01:04.308748'
original_url: https://www.theregister.com/networks/2026/07/28/cisco-close-to-releasing-more-ai-models-this-time-for-deep-networking-ops/5279350
date: '2026-07-31'
published_date: '2026-07-28T06:50:40.000Z'
description: Token costs not quite sorted, but on-prem will be an option
tags:
- tldr
---

NETWORKS

 

# Cisco close to releasing more AI models, this time for deep networking ops

Token costs not quite sorted, but on-prem will be an option

Simon Sharwood

Simon

Sharwood

APAC Editor

APAC Editor

Published

tue 28 Jul 2026 // 07:50 UTC

Cisco has developed AI models that can solve networking problems and is close to releasing the tools, plus the Cloud Control agentic ops tool that puts its models to work.

Cloud Control is Cisco’s attempt to tame console sprawl, but creating a new interface to its product portfolio driven by agentic AI.

The networking giant says Cloud Control will allow users to query their infrastructure to do things like find the source of a single glitchy connection. Today, figuring that out could see NetAdmins look for info across several product consoles. Cisco reckons Cloud Control will diagnose issues more quickly, by using agents that source and analyze data from whichever parts of its product portfolio you’ve deployed.

REG AD

DJ Sampath, senior veep and general manager of Cisco’s AI Software and Platform biz, suggested agents running under Cloud Control could diagnose a single device’s inability to connect to a Wi-Fi network on one floor of a building by referencing security policies that might prohibit the connection and the channels an access point offers. If the agents find a fault that requires a reboot, Sampath said Cisco’s new toy can explain the blast radius of that effort so NetAdmins can understand when to press Off and On again.

REG AD

Cisco developed its own deep networking AI model to make that sort of thing possible and Sampath toldThe Registerthe model will “shortly” appear on Hugging Face, alongside theAntaressecurity models the company recently published.

Sampath said the model "understands routing and switching configs" and therefore “solves network problems better than a frontier model.”

He also revealed that Cloud Control, which Cisco hastouted for several months, will become available to US-based customers by the end of August. The service will be included with Cisco’s other products, but the company is yet to finalise pricing plans.

## MORE CONTEXT

* ### Cisco making SONiC available to all customers – not just hyperscalers
* ### Cisco sings Mythos' praises - but doesn't say how many bugs the model uncovered
* ### Cisco used AI to write security incident reports, with mixed results
* ### Cisco serves up yet another perfect 10 bug with Secure Workload admin flaw

Like other AI services, Cloud Control chews through tokens. Cisco plans to include a certain quantity of tokens with its existing subscriptions and will figure out how to charge for extra tokens.

The company will also make its networking models available for on-prem use – including on collections of its own UCS servers – for those who don’t want to surf the chaotic terrain that istokenomics.

Cloud Control will come to Europe and the Asia-Pacific in coming months. Sampath said the work needed to build the infrastructure Cisco needs to run it is one reason for the delay. Another is regulatory issues, because the service needs access to customers’ systems and that requirement means sensitive data comes into play – as do local laws about how to make that happen with appropriate security and governance.

Sampath doesn’t see Cloud Control replacing Cisco’s product-specific consoles anytime soon, because he thinks customers have built processes around them and trained workers to use the tools. That position perhaps validates analyst firm Gartner’spredictionthat the advent of AI management tools will initially mean some bloat in organizations’ fleet of management tools. ®

cisco

ai and ml

aiops

networks

REG AD

AI AND ML

## Oracle adds Google Gemini to the agent menu

Chocolate Factory LLMs join Big Red's Fusion automation party

STORAGE

## GPUs could explode to multiple TB with new storage-inspired memory tech

High-bandwidth flash promises SSD-like capacities with HBM-like speeds, but it's not all unicorns and rainbows

## From individual achievement to partner impact

PARTNER CONTENT: Databricks survey data suggests certified professionals lift partner delivery capacity, customer credibility, and AI readiness well beyond the individuals who earn the credential

AI and ML

## Open source project fools AI scrapers with poisoned font

ShieldFont is available today if you've got copy that needs protecting, we mean

columnists

## Digital sovereignty is real in Europe. The UK? Not so much

Trump's unpredictability is pushing governments and businesses toward open source while Britain remains glued to US tech

Security

## Jailed Flock vandal wipes out three cameras, racks up thousands in damages

A lesson for aspiring vandals: Take out all the cameras, not just the ones that flout your ideals

### MOST POPULAR

* security#### DEF CON bans Meta-style 'pervert glasses'
* DATABASES#### After rewriting SQLite in Rust, Turso turns its sights on Postgres
* security#### Word worm crawls into Copilot, spreads chaos
* virtualization#### Foxconn drops VMware, adopts hyperconverged upstart Arcfra for workloads including AI
* SOFTWARE#### Microsoft seeks Supreme Court lifeline in pre-owned license battle

### AI

* STORAGE#### GPUs could explode to multiple TB with new storage-inspired memory techHigh-bandwidth flash promises SSD-like capacities with HBM-like speeds, but it's not all unicorns and rainbows
* AI and ML#### Open source project fools AI scrapers with poisoned fontShieldFont is available today if you've got copy that needs protecting, we mean
* OFF-PREM#### The majority of corporate IT is now off premises for the first timeSurvey finds more workloads run off-site than at in-house corporate facilities for the first time
* AI and ML#### Closed models refuse to help researcher swat Linux bug"I'm sorry, Dave. I'm afraid I can't do that" is an effective sales pitch for open source
* Storage#### A requiem for Optane, Intel's KV cache killer that could have eased the RAM price crunchWith microscopic latencies and otherworldly write endurance, it was perfect for today's AI workloads – but gone before they arrived

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### FOSS smashed one Microsoft monopoly. After 20 years of failure, it's time to smash anotherWord up
* #### GNOME can look like Windows – and Flashback can do it without extensionsNew 'Simple-taskbar' is an option, but there's a simpler, stabler way
* #### A moment of silence, please, for the final release of Debian on x86-32New Debian versions hit FOSSland in the form of 13.6 and 12.15
* #### Baddies caught exploiting extensions bugs with perfect 10 scores on vulnerable Joomla websitesFlaws in iCagenda, Balbooa Forms extensions can impact open source CMS that powers a million sites worldwide
* #### Frame: A new X11 server – implemented directly in assemblyJoins yserver, Phoenix, and of course XLibre – and outlier Arcan
* #### Cinnamon 6.8 will support Wayland – if you want itNext version of Linux Mint’s desktop has both kinds of display server