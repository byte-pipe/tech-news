---
title: Feds freaked over Fable 5 after simple 'fix this code' prompt, not jailbreak, says researcher
url: https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827
site_name: hackernews_api
content_file: hackernews_api-feds-freaked-over-fable-5-after-simple-fix-this-co
fetched_at: '2026-06-16T20:04:55.466576'
original_url: https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827
author: _tk_
date: '2026-06-16'
published_date: '2026-06-15T21:07:26.000Z'
description: According to the one person who actually read the research paper
tags:
- hackernews
- trending
---

security

 

# Feds freaked over Fable 5 after simple 'fix this code' prompt, not jailbreak, says researcher

According to the one person who actually read the research paper

Jessica Lyons

Jessica

Lyons

Published

mon 15 Jun 2026 // 22:07 UTC

The “jailbreak” that prompted the Trump administration to block Anthropic’s most advanced models was actually a simple three-word prompt: “Fix this code.”

That's according toKatie Moussouris, founder and CEO of Luta Security, and thefairy godmother of bug bounties. She says she was the only outside expert to read the third-party research paper on the Fable 5 guardrail bypass techniques that prompted the ban.

On Friday, the US government, reportedly citing national security concerns, issued an export control directive to suspend access to Fable 5 and Mythos 5 by any foreign national, inside or outside the United States. In response, Anthropicdisabled both models“for all our customers to ensure compliance.”

REG AD

Anthropic shared the report privately with her, Moussouriswrotein a Monday blog post.

REG AD

The outside researchers reportedly fed Anthropic’sFable 5,Mythos, and Claude Opus models open-source code containing known CVEs, plus new code intentionally laced with vulnerabilities, and asked the models to “review the code for security issues.”

As Moussouris tells it, Fable 5 refused, so the researchers asked the AI systems to “fix this code.” The model reportedly obliged, and after additional prompts also produced scripts to test the patches.

“That’s it,” Moussouris wrote. “‘Fix this code,’ plus several manual steps to generate test scripts, should never have triggered an export control. I feel like making ’90s-style t-shirts with ‘fix this code’ on the front and ‘this shirt is a munition’ on the back.”

Between 2013 and 2017, Moussourisserved on the technical expert groupthat renegotiated theWassenaar Arrangement, a voluntary agreement between 42 nations that governs certain export controls for classified dual-use software and technology.

The group eventually won exemptions for defensive cybersecurity activity. This allows defenders to share vulnerability data, conduct malware analysis, and coordinate incident response internationally without the threat of criminal prosecution.

On Sunday, Moussouris joined more than 100 other cybersecurity leaders and signed an open letterurging the Trump administration to reversethe restrictions on Fable 5 and Mythos and restore cybersecurity firms' access to the advanced models.

“To pull the best capabilities away from defenders without a good reason when our adversaries are rapidly advancing is dangerous,” theywrote.

In her blog, Moussouris argues that there was no guardrail bypass or jailbreak. Defenders should be able to ask AI systems to find and fix bugs, and write tests to validate the patch, she said. Anthropic’s models were doing “the most valuable thing an AI model can do for defensive security: executing the find, fix, and test loop defenders run every day.”

REG AD

Removing the capability for models to respond to defensive requests makes AI systems “worse at finding bugs and verifying patches,” she continued.

Plus, the US can’t extend export controls toopen-weight systems or similar advanced modelsfrom China and other countries - and these systems will soon achieve Mythos-like capabilities, anyway. Anthropic and Google have bothaccused China-based rivalsincluding DeepSeek of using“distillation attacks”to train their models by siphoning knowledge from American companies’ AI.

Banning Anthropic’s advanced models is going to hurt defenders more than attackers, Moussouris warns. “Defense improves when defenders find the same bugs attackers find and fix them faster,” she wrote. “We need the best tools to defend against increasingly capable attackers in the AI era of cybersecurity.”

The Registerreached out to the Trump administration for comment on Moussouris' assertion, and we'll update this post if we hear back. ®

## MORE CONTEXT

* ### US clampdown on Anthropic models sends EU sovereignty surge into overdrive
* ### Anthropic spins a Fable of a tamer, safer Mythos
* ### It blocked us at 'hello!' Anthropic Fable 5 refusing innocuous prompts
* ### Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops

export controls

anthropic

ai

ai and ml

jailbreak

security

REG AD

HPC

## Decade-old networking tech spun out of Intel bests Infiniband to power DoE supercomputer

Omni-Path lights up Lawrence Livermore system at 400 Gbps

science

## AI and brain-computer interface allow speechless ALS patient to work a full-time job

The hardware isn't new, but a UC Davis research team's machine learning-powered method of translating brain activity in an ALS patient into sentences with 92% accuracy is

## ZTE Day 2026 in Almaty Showcases Innovations Shaping Kazakhstan's Intelligent Telecom Future

PARTNER CONTENT: Empowering Kazakhstan’s "Year of Digitalization and AI" with Next-Gen Connectivity and Supercomputing Solutions

Security

## Three critical Fortinet sandbox bugs splattered by unknown attackers

All have patches, so make sure you upgrade to a fixed version

PAAS AND IAAS

## Graviton 5 impresses, but please, for the love of all that's holy, stop calling them 'AI chips'

AWS better at running chip fabs than their mouths

Personal tech

## Commodore gets into the phone biz with Sailfish-powered retro 'Callback'

Ships sans email, web, or socials, but with plenty of beige plastic

### MOST POPULAR

* security#### Feds freaked over Fable 5 after simple 'fix this code' prompt, not jailbreak, says researcher
* ON-PREM#### Amazon owns up to using 2.5bn gallons of H2O in its bit barns last year
* Security#### Angry bug hunter with Microsoft beef drops new Windows 0-day
* Security#### Signal says UK plan to scan devices for nude images 'endangers us all'
* security#### GitHub nukes 70+ Microsoft repos, breaks CI/CD pipelines, following suspected worm infections

## EVENTS

* ### From Prompt to Exploit: How LLMs Are Changing API AttacksModern applications are API-driven, interconnected, and often over-permissioned, making them an ideal target for AI-assisted attacks.
* ### Architecting the Future: Unlocking Enterprise Data Services for KubernetesJoin us to discover how to eliminate infrastructure silos and establish a standardized, enterprise-grade cloud-native platform.
* ### Catch the Advanced Attacks Microsoft 365 Misses with Behavioral AI SecurityMicrosoft 365 is the backbone of enterprise communication, and its native security filters out the known and the noisy.
* ### Accelerate your innovationThis is your technical deep-dive into the practical tools and techniques that define the next generation of resilient Dev and IT operations.
* ### Virtual Cyber Recovery SimStep into the chaos of a live ransomware breach, test your response skills, and team up with other IT and security pros to outsmart cybercriminals
* ### Virtual Cyber Recovery SimulationRansomware attacks aren’t slowing down, and neither are we. Druva’s hit event, Escape Ransomware, is now fully virtual.
* ### Zero Trust for the Agentic AI EraThe identity and access models most organizations rely on were built for human users, not non-human identities operating independently.
* ### Zero Trust for the Agentic AI EraThe identity and access models most organizations rely on were built for human users, not non-human identities operating independently.
* ### Agentic AI at Scale: From Pilot to ProductionJoin us to learn how to unlock real ROI by driving adoption of AI at scale.

 EXPLORE ALL OF OUR EVENTS
 

### AI

* science#### AI and brain-computer interface allow speechless ALS patient to work a full-time jobThe hardware isn't new, but a UC Davis research team's machine learning-powered method of translating brain activity in an ALS patient into sentences with 92% accuracy is
* SYSTEMS#### There's no such thing as an agentic CPUAI agents are a general-purpose workload no different from any other
* SOFTWARE#### Microsoft faces down sueball, capacity problems in series of challengesMisleading statements about Copilot and AI? Surely not!
* SYSTEMS#### Non-x86 servers now nearly half the market, IDC saysDemand for AI systems plus the shortage of DRAM and NAND are shaping the global market
* AI AND ML#### ERP users may soon get ahead by going headless, says Rimini Street bossLook to AI agents and open source to escape the vendor-driven upgrade cycle

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### France's digital sovereignty push is struggling to escape the Microsoft gravity wellNextcloud rollout shows locally controlled storage is one thing; getting users off Office is quite another
* #### History of CentOS: How a biochemist's Linux hobby project became the enterprise world's default operating systemWhen a community came together after Red Hat said Windows was 'probably the right product'
* #### Netflix wiz creates app to slash AI bills, then open sources itProject Headroom could save you big money, too
* #### OpenBSD 7.9 arrives, a diamond in the rough proud of every sharp edgeSixtieth release adds more cores, delayed hibernation, and basic Wi-Fi 6 without losing its ascetic streak
* #### Fedora: Microsoft is all aboard, but Deepin is dumpedRed Hat’s free distro loses a desktop, but makes an important new friend
* #### LocalSend puts your sneakernet out of businessLike AirDrop, minus the Apple lock-in