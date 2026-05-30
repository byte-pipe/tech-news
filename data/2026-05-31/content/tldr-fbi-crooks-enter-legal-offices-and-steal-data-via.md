---
title: 'FBI: Crooks enter legal offices and steal data via USB drive'
url: https://www.theregister.com/security/2026/05/27/fbi-crooks-enter-legal-offices-and-steal-data-via-usb-drive/5247212/
site_name: tldr
content_file: tldr-fbi-crooks-enter-legal-offices-and-steal-data-via
fetched_at: '2026-05-31T06:00:36.013865'
original_url: https://www.theregister.com/security/2026/05/27/fbi-crooks-enter-legal-offices-and-steal-data-via-usb-drive/5247212/
date: '2026-05-31'
published_date: '2026-05-27T16:15:52.000Z'
description: Cybercriminals still allowed to walk into office blocks and convince staff to let them plug in their own thumb drives
tags:
- tldr
---

Security

# Extortion crews are visiting law firms pretending to be tech support, FBI warns

Cybercriminals still allowed to walk into office blocks and convince staff to let them plug in their own thumb drives

Connor Jones

Connor

Jones

Cybersecurity reporter

Published

wed 27 May 2026 // 17:15 UTC

The FBI is warning unsuspecting lawyers that their firms  continue to be an active target for members of a longstanding extortion crew.

Silent Ransom Group has been operating since 2022, by the FBI’s reckoning, and itslatest message [PDF] about the gang comes almost exactly a year after its last. The group is still targeting US law firms and their staff, and the criminals are pretending to be company IT staff.

It also warned last year that the callback phishing specialists had started physically walking into the law firms’ offices when remote social engineering attempts go south. The FBI’s latest advisory reaffirms these findings, with fresh attacks reported in Spring 2026.

REG AD

Law firms should be locking up their USB ports because the extortion crew is still sending members to plug in their thumb drives into the computers, for when they can’t convince employees to surrender remote access.

REG AD

In these scenarios, they rock up to the victim they’ve tried to phish and socially engineer from behind a phone or computer screen, continue the facade of being a company IT rep, and then claim they need to image the person's device or create a backup file to assess the damage of their ownphishingemail.

What they’re actually doing is copying important files onto said thumb drive, which SRG will later use to extort the law firm.

The FBI didn’t say exactly how many of these in-person callouts SRG has made, but it was evidently enough to include in a fresh advisory on the group’s methods and tactics.

According to the advisory, these attacks were first reported in Spring 2026.

## SRG in brief

SRG’s target industries used to be broader than just legal. The hack-and-leak group has been known to target organizations operating in various industries, but the legal sector has remained a common theme since 2023.

The FBI said in its advisory on the grouplast yearthat it believes SRG consistently targets US law firms “likely due to the highly sensitive nature of legal industry data.”

## MORE CONTEXT

* ### Crime crew impersonates help desk, abuses Microsoft Teams to steal your data
* ### 'Several dozen' high-value corporations hit by new extortion crew in helpdesk phishing spree
* ### Formal ban on ransomware payments? Asking orgs nicely to not cough up ain't working
* ### Pass the key, passwords have passed their sell-by date

When they’re not sending crooks into office blocks, SRG’s primary goal is to achieve their aims through callback phishing.

REG AD

Using SMS messages or emails, group members would single out employees at target companies, asking them to call a number whileimpersonating real IT staff.

If the staffer fell for the scheme, they’d call up, and the SRG IT imposter would attempt to convince them to grant access to a remote desktop session, during which they would elevate their privileges and set about stealing data to use as extortion leverage.

In some cases, SRG will run WinSCP or a disguised version of Rclone to scoop up files of interest. In others, they are known to share those documents using internal file-sharing platforms such as Google Drive or Microsoft OneDrive.

Before the callback phishing methodology, the group would send emails claiming that a fake subscription had been authorized that would charge small sums to the target’s account each month. The email included a phone number to call in order to cancel the subscription, and once on the call, the crooks would convince the target to install remote access software, and rinse-repeat the data theft playbook.

SRG isnot known for using ransomware, but it operates a data leak site (DLS) just like any other extortion crew and charges victims to return the data they stole, threatening to leak it online if they refuse to pay.

Recent alleged victims of the group have included law giant Jones Day, the legal eagles favored by US president Donald Trump during both his election campaigns. SRG listed Jones Day on its DLS, and the law firmconfirmeda “cyber phishing incident” in April, but did not name SRG as the culprits.

## Your country needs you

The FBI pleaded with the public to send it any evidence of SRG in action to aid future investigations. Of particular use would be phone numbers used to contact the crooks, copies of the phone call transcripts and phishing emails, cryptocurrency wallet information, and identifying information of the individuals who step foot in office buildings.

REG AD

As for how to prevent attacks from SRG or others adopting similar methods, the FBI recommended that organizations disallow connecting external drives to company-issued devices, especially those that store confidential or otherwise sensitive information.

Verifying the credentials of each person walking into the building wouldn’t hurt, either.

The usual advice applies for the group’s remote attacks: limiting access to sensitive data from less-secure networks and requiringphishing-resistant MFAfor as many services as possible.

The FBI also recommends blocking port 22 access, which would prevent encrypted remote access, and investing in robust staff training programs so they know not to let outsiders plug hardware into their machines. ®

security

REG AD

Software

## Wikipedia editors plot strike and banner sabotage after Wikimedia layoffs

Foundation sparks revolt after disbanding team responsible for many community-requested fixes and moderation tools

Offbeat

## Rocket exhibit at National Space Centre pulls off unintentional NASA SLS impression

5, 4, 3, 2, 1... pfft

PARTNER CONTENT

## AI and data sovereignty in Postgres: An answer to the datacenter energy crisis

A billion AI agents walk into a power grid

AI + ML

## AWS reportedly to tuck Elon Musk's Grok into Bedrock, despite zero enterprise demand

The energy drink of frontier models

Systems

## EU's digital sovereignty boo-boo may be the best thing to ever happen to the project

DIY or die. Just don't let the CIA buy it

Security

## Lone attacker published 14 malicious npm packages mimicking popular OpenSearch, Elasticsearch libraries

And then Microsoft busted them all

### MOST POPULAR

* AI + ML#### Google has seriously leaned into AI enshittification lately
* Security#### Anthropic to release Mythos-class models to the public
* Security#### Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops
* Operating Systems#### Linus Torvalds to ‘start being more hardnosed’ about ‘pointless pull requests’ – some of which come from AIs
* Security#### Troops’ phones gave away location data to foreign adversaries

## EVENTS

* ### Overcoming the trade-offs in data sovereigntyWhat does data sovereignty actually mean for your network, which trade-offs are unavoidable? Learn more.
* ### From Prompt to Exploit: How LLMs Are Changing API AttacksModern applications are API-driven, interconnected, and often over-permissioned, making them an ideal target for AI-assisted attacks.
* ### Architecting the Future: Unlocking Enterprise Data Services for KubernetesJoin us to discover how to eliminate infrastructure silos and establish a standardized, enterprise-grade cloud-native platform.
* ### Catch the Advanced Attacks Microsoft 365 Misses with Behavioral AI SecurityMicrosoft 365 is the backbone of enterprise communication, and its native security filters out the known and the noisy.
* ### Virtual Cyber Recovery SimStep into the chaos of a live ransomware breach, test your response skills, and team up with other IT and security pros to outsmart cybercriminals
* ### Virtual Cyber Recovery SimulationRansomware attacks aren’t slowing down, and neither are we. Druva’s hit event, Escape Ransomware, is now fully virtual.
* ### Agentic AI at Scale: From Pilot to ProductionJoin us to learn how to unlock real ROI by driving adoption of AI at scale.

 EXPLORE ALL OF OUR EVENTS
 

### AI

* Software#### Wikipedia editors plot strike and banner sabotage after Wikimedia layoffsFoundation sparks revolt after disbanding team responsible for many community-requested fixes and moderation tools
* Offbeat#### Rocket exhibit at National Space Centre pulls off unintentional NASA SLS impression5, 4, 3, 2, 1... pfft
* AI + ML#### AWS reportedly to tuck Elon Musk's Grok into Bedrock, despite zero enterprise demandThe energy drink of frontier models
* Security#### Lone attacker published 14 malicious npm packages mimicking popular OpenSearch, Elasticsearch librariesAnd then Microsoft busted them all
* ai + ml#### Okta writes its own license to kill rogue AI agentsCEO Todd McKinnon says customers including ServiceNow want an off switch

### Infosec

* Software#### Wikipedia editors plot strike and banner sabotage after Wikimedia layoffsFoundation sparks revolt after disbanding team responsible for many community-requested fixes and moderation tools
* Offbeat#### Rocket exhibit at National Space Centre pulls off unintentional NASA SLS impression5, 4, 3, 2, 1... pfft
* AI + ML#### AWS reportedly to tuck Elon Musk's Grok into Bedrock, despite zero enterprise demandThe energy drink of frontier models
* Security#### Lone attacker published 14 malicious npm packages mimicking popular OpenSearch, Elasticsearch librariesAnd then Microsoft busted them all
* ai + ml#### Okta writes its own license to kill rogue AI agentsCEO Todd McKinnon says customers including ServiceNow want an off switch

### FOSS

* #### Wikipedia editors plot strike and banner sabotage after Wikimedia layoffsFoundation sparks revolt after disbanding team responsible for many community-requested fixes and moderation tools
* #### Rocket exhibit at National Space Centre pulls off unintentional NASA SLS impression5, 4, 3, 2, 1... pfft
* #### AWS reportedly to tuck Elon Musk's Grok into Bedrock, despite zero enterprise demandThe energy drink of frontier models
* #### Lone attacker published 14 malicious npm packages mimicking popular OpenSearch, Elasticsearch librariesAnd then Microsoft busted them all
* #### Okta writes its own license to kill rogue AI agentsCEO Todd McKinnon says customers including ServiceNow want an off switch
* #### ICE to keep an eye on your eyes under $25M biometric scanner dealAnd you thought a face recognition app was intrusive?

## FEATURES

* ### Europe built sovereign clouds to escape US control. Then forgot about the processors
* ### Nobody believes the 'criminals and scumbags' who hacked Canvas really deleted stolen student data
* ### Europe wants out from under US tech – but first it has to find the exits
* ### GNOME may rule Ubuntu Resolute Raccoon, but X.org isn't roadkill yet
* ### OpenClaw, but in containers: Meet NanoClaw
* ### Open source registries don't have enough money to implement basic security
* ### Contain your Windows apps inside Linux Windows
* ### The Linux mid-life crisis that's an opportunity for Tux-led transformation
* ### Too much AI for some, too little for others: Why AMD can't win with investors
* ### How agentic AI can strain modern memory hierarchies