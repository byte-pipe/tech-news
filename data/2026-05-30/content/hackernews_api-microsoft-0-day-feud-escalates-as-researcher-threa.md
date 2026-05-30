---
title: Microsoft 0-day feud escalates as researcher threatens another Windows exploit dump
url: https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085
site_name: hackernews_api
content_file: hackernews_api-microsoft-0-day-feud-escalates-as-researcher-threa
fetched_at: '2026-05-30T11:32:28.357571'
original_url: https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085
author: Cider9986
date: '2026-05-29'
published_date: '2026-05-28T20:19:09.000Z'
description: Six 0-days, three under active exploitation, more to come on July 14?
tags:
- hackernews
- trending
---

Security

# Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops

Six 0-days, three under active exploitation, more to come on July 14?

Jessica Lyons

Jessica

Lyons

Published

thu 28 May 2026 // 21:19 UTC

The ongoing saga of Microsoft versus Nightmare Eclipse (aka Chaotic Eclipse), the disgruntled bug hunter with a deep understanding of Windows and an even deeper grudge against Microsoft, reached a fever pitch, with the researcher, who has thus far released six Windows zero-days, promising a “bone shattering” drop on July 14.

Microsoft, for its part,finally respondedto the security researcher and their weaponized Windows flaws with a blog post on (un)coordinated vulnerability disclosure about the now-public bugs:RedSun,UnDefend,BlueHammer,YellowKey, GreenPlasma, and MiniPlasma. Redmond says that none of these were reported via its official channels prior to being made public.

Attackers began hammering three of the six -BlueHammer, RedSun, and UnDefend- soon after Nightmare published workingproof-of-concept exploit codefor each onnow-bannedGitHub (owned by Microsoft) and GitLab accounts.

REG AD

## MORE CONTEXT

* ### Mystery Microsoft bug leaker keeps the zero-days coming
* ### Microsoft's massive Patch Tuesday: It's raining bugs
* ### Welcome to the vulnpocalypse, as vendors use AI to find bugs and patches multiply like rabbits
* ### Microsoft promises more bug payouts, with or without a bounty program

YellowKey, GreenPlasma, and MiniPlasma still don’t have fixes, and Microsoft has deemed “exploitation more likely” for YellowKey, aka CVE-2026-45585, citing a working POC.

REG AD

“We remain firmly opposed to these actions, and any disclosure outside proper coordination that could harm our customers and the digital ecosystem,” Microsoftwrotein a Wednesday blog, and then seemingly threatened legal action against Nightmare:

“Uncoordinated disclosures that put proof-of-concept code for unpatched vulnerabilities into the hands of bad actors are never justifiable and have real-world consequences. Our security teams across the company work tirelessly tracking threat actors who look for weaknesses just like these to attack Microsoft and our customers. Our Digital Crimes Unit will continue bringing cases against these actors and those that enable their criminal activity – coordinating as needed with law enforcement around the world.”

Microsoft did not respond toThe Register’s questions, including whether its legal team planned to sue Nightmare, whether the zero-day researcher is a current or former employee, and whether Microsoft axed Nightmare’s MSRC account, meaning that the bug hunter can’t disclose vulnerabilities to the Windows giant.

Nightmare, in their latest anti-Microsoft missive, claims Microsoft did just that.

“When I actively asked you to communicate with me, you refused, humiliated me and made sure to insult me in front of people,” theywroteon Saturday. “You defame me in public with your CVE-2026-45585 advisory even though you literally deleted the Microsoft account I used to report bugs to you with and I got zero pennies from doing so and I still happily did like an idiot.”

### Mark this date July 14th, I will make sure your bones are shattered that day

Nightmare also noted that “Microsoft still has chains in my hands,” preventing them from releasing “documents” yet, or anytime in June, and then warned: “Mark this date July 14th, I will make sure your bones are shattered that day.”

Regardless of what does or does not happen on July 14, Nightmare has already caused chaos - and real enterprise-level damage, as systems engineer Muhammad Qasim Shahzadsaidon LinkedIn.

“One person caused more enterprise-level damage in six weeks than most APT groups cause in a year,” Shahzad wrote. “The gap between disclosure and weaponization is now measured in hours, not days. Your patching window is shrinking fast.”

REG AD

Zero Day Initiative’s bug hunter-in-chief Dustin Childs, who previously spent about seven years working for Microsoft security and has decades of experience onboth sidesof thecoordinated vulnerability disclosure(CVD) process, toldThe Registerthat Microsoft could have handled this better. And he wondered what happened between the two parties to get to this point.

“CVD is a two-way street,” he said. “The vendor has some responsibility as well, so to go out publicly stating this person violated CVD without showing any of the correspondence seems bold.”

Microsoft could also improve its communications to customers on “what the real risks from these bugs are and how they can defend themselves,” Childs added. “That clear direction seems to be missing.”

### Microsoft's 'dumpster fire'

Luta Security founder and CEOKatie Moussouris, whopioneered Microsoft’s bug bounty programdespite execs vowingnever to payresearchers for bugs, said Redmond’s response to Nightmare sends “mixed messages.”

“It confusingly claims their program ‘ensures researchers are compensated and publicly acknowledged’ in a statement answering a researcher who says he got neither,” Moussouris toldThe Register. “The language choices are also not deescalating. Microsoft invoked the outdated term ‘responsible disclosure,’ whichI retired years ago at Microsoftbecause it was subjective and judgy.”

This phrase, Moussouris added, “got in the way of coordination” when the two sides disagreed about how to best protect end users.

“The mention of the Digital Crimes Unit in a post discussing vulnerability disclosure makes the post vaguely threatening, which seems intentional, but then they wrap up the post saying they welcome reports regardless of disclosure history,” she said. “No one except the parties involved can know for sure what happened between this researcher and Microsoft. Whatever the facts, it's hard to imagine why Microsoft would not try to deescalate, if for no other reason than avoiding the chilling effect on other researchers.”

REG AD

Security sleuth Kevin Beaumont, in his blog on the ongoing Microsoft-Nightmare Eclipse saga, called it a "dumpster fireof [Microsoft’s] own making.”

Beaumont also used to work at Microsoft, and he noted that the Windows company previouslyhired a hacker called SandboxEscaperafter she published zero-day POC exploits for Microsoft products - something that Redmond’s blog now describes as criminal.

“If Microsoft’s tactic is to try to criminalise not following often arbitrary ‘responsible disclosure’ frameworks, good luck defending that in court - because there’s a whole clown car of prior decision making within Microsoft and facts which would emerge in that process,” Beaumont said.

To be clear: neither Beaumont nor the researchers thatThe Regspoke to support Nightmare’s zero-day antics. Childs called the “July 14” post “troubling” and Moussouris said the date plus “incendiary language … doesn't help organizations trying to make sense of the technical risk.”

### 'David and Goliath dynamic'

Moussouris did add that this latest missive, taken in context with the earlier blog posts, “paint[s] a picture of someone who believes they have been pushed to this extreme. It is the sound of someone who believes every legitimate channel was closed to them: GitHub account deleted, payments withheld, credit stripped, then publicly accused of violating CVD after Microsoft cut off their ability to coordinate. The researcher's grievances are serious and specific.”

Ultimately, “the bugs are Microsoft's,” Moussouris said. “They wrote the code and they own the risk to customers. Often researchers who previously work with a vendor respond in the extreme only when they feel there is no other choice. The power they hold is not at all proportionate to the vendor. This is a David and Goliath dynamic we don't like to see play out, especially since it’s users who lose when coordination negotiations fail."

While it’s a very extreme - perhaps the most extreme - example of coordinated disclosure gone wrong, it’s not an isolated problem. Researchers have beencomplaining about CVD, and specificallyRedmond’s bug disclosure habits, for years.

“While some companies have improved, Microsoft has not,” Childs said. “If anything, they are seen as difficult to work with, especially if your bug is Moderate instead of Critical. I’ve had researchers tell me that they stopped looking at Microsoft altogether because they were too difficult to work with.”

Plus, these types ofdisagreements between researchers and bug bounty programswill likely increase, asAI-assisted bug reportsbecomethe normand vulnerabilities skyrocket.

“We as an industry need to take a breath, remember there are real people involved, and that poor interactions could lead to real customer risk,” Childs said. “Real-world impact is lost far too often when disclosure goes wrong.” ®

microsoft

coordinated vulnerability disclosure

zero-day

windows

security

REG AD

Offbeat

## Rocket exhibit at National Space Centre pulls off unintentional NASA SLS impression

5, 4, 3, 2, 1... pfft

AI + ML

## AWS reportedly to tuck Elon Musk's Grok into Bedrock, despite zero enterprise demand

The energy drink of frontier models

PARTNER CONTENT

## AI and data sovereignty in Postgres: An answer to the datacenter energy crisis

A billion AI agents walk into a power grid

Security

## Lone attacker published 14 malicious npm packages mimicking popular OpenSearch, Elasticsearch libraries

And then Microsoft busted them all

Systems

## EU's digital sovereignty boo-boo may be the best thing to ever happen to the project

DIY or die. Just don't let the CIA buy it

public sector

## ICE to keep an eye on your eyes under $25M biometric scanner deal

And you thought a face recognition app was intrusive?

### MOST POPULAR

* AI + ML#### Google has seriously leaned into AI enshittification lately
* Security#### Anthropic to release Mythos-class models to the public
* Security#### Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops
* Operating Systems#### Linus Torvalds to ‘start being more hardnosed’ about ‘pointless pull requests’ – some of which come from AIs
* OSes#### Microsoft tests the 15-character limit of Windows Server admins' patience

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

* Offbeat#### Rocket exhibit at National Space Centre pulls off unintentional NASA SLS impression5, 4, 3, 2, 1... pfft
* AI + ML#### AWS reportedly to tuck Elon Musk's Grok into Bedrock, despite zero enterprise demandThe energy drink of frontier models
* Security#### Lone attacker published 14 malicious npm packages mimicking popular OpenSearch, Elasticsearch librariesAnd then Microsoft busted them all
* ai + ml#### Okta writes its own license to kill rogue AI agentsCEO Todd McKinnon says customers including ServiceNow want an off switch
* public sector#### ICE to keep an eye on your eyes under $25M biometric scanner dealAnd you thought a face recognition app was intrusive?

### FOSS

* #### Rocket exhibit at National Space Centre pulls off unintentional NASA SLS impression5, 4, 3, 2, 1... pfft
* #### AWS reportedly to tuck Elon Musk's Grok into Bedrock, despite zero enterprise demandThe energy drink of frontier models
* #### Lone attacker published 14 malicious npm packages mimicking popular OpenSearch, Elasticsearch librariesAnd then Microsoft busted them all
* #### Okta writes its own license to kill rogue AI agentsCEO Todd McKinnon says customers including ServiceNow want an off switch
* #### ICE to keep an eye on your eyes under $25M biometric scanner dealAnd you thought a face recognition app was intrusive?
* #### No fix yet for critical RCE bug in open-source Git service Gogs - exploit module is outResearcher reported the vuln in March. Maintainers haven't responded to his messages since

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