---
title: A Hacker Group Is Poisoning Open Source Code at an Unprecedented Scale | WIRED
url: https://www.wired.com/story/teampcp-software-supply-chain-attack-spree-github/
site_name: newsfeed
content_file: newsfeed-a-hacker-group-is-poisoning-open-source-code-at-an
fetched_at: '2026-05-21T12:05:56.536349'
original_url: https://www.wired.com/story/teampcp-software-supply-chain-attack-spree-github/
author: Andy Greenberg
date: '2026-05-21'
published_date: '2026-05-21T09:00:00.000Z'
description: GitHub is just the latest victim of TeamPCP, a gang that has carried out a spree of software supply chain attacks that has impacted hundreds of organizations.
tags:
- wired
- security
- security / cyberattacks and hacks
- security / security news
---

Save Story
Save this story
Save Story
Save this story

A so-called softwaresupply chain attack, in which hackers corrupt a legitimate piece of software to hide their own malicious code, was once a relatively rare event but one that haunted the cybersecurity world with its insidious threat of turning any innocent application into a dangerous foothold in a victim’s network. Nowone group of cybercriminalshas turned that occasional nightmare into a near-weekly episode, corrupting hundreds of open source tools, extorting victims for profit, and sowing a new level of distrust in an entire ecosystem used to create the world’s software.

On Tuesday night, open source code platform GitHub announced that it had been breached by hackers in one such software supply chain attack: A GitHub developer had installed a “poisoned” extension for VSCode, a plug-in for a commonly used code editor that, like GitHub itself, is owned by Microsoft. As a result, the hackers behind the breach, an increasingly notorious group called TeamPCP, claim to have accessed around 4,000 of GitHub’s code repositories. GitHub’s statement confirmed that it had found at least 3,800 compromised repositories while noting that, based on its findings so far, they all contained GitHub’s own code, not that of customers.

“We are here today to advertise GitHub’s source code and internal orgs for sale,” TeamPCP wrote on BreachForums, a forum and marketplace for cybercriminals. “Everything for the main platform is there and I very am happy to send samples to interested buyers to verify absolute authenticity.”

The GitHub breach is just the latest incident in what has become the longest-running spree of software supply chain attacks ever, with no end in sight. According to cybersecurity firm Socket, which focuses on software supply chains, TeamPCP has, in just the last few months, carried out 20 “waves” of supply chain attacks that have hidden malware in more than 500 distinct pieces of software, or well over a thousand counting all of the various versions of the code that TeamPCP has hijacked.

Those tainted pieces of code have allowed TeamPCP’s hackers to breach hundreds of companies that installed the software, says Ben Read, who leads strategic threat intelligence at the cloud security firm Wiz. GitHub is only the latest on the group’s long list of victims, which has also included AI firm Anthropic and the data contracting firm Mercor. “It may be their biggest one," Read says of the GitHub breach. “But each one of these is a big deal for the company that it happens to. It's not qualitatively different from the 14 breaches that happened last week.”

TeamPCP’s core tactic has become a kind of cyclical exploitation of software developers: The hackers gain access to a network where an open source tool commonly used by coders is being developed—for example, the VSCode extension that led to the GitHub breach or the data visualization software AntV that TeamPCP hijacked earlier this week. The hackers plant malware in the tool that ends up on other software developers’ machines, including some who are writing other tools intended to be used by coders.

The malware allows TeamPCP’s hackers to steal credentials that let them publish malicious versions ofthosesoftware development tools, too. The cycle repeats, and TeamPCP’s collection of breached networks grows. “It’s a flywheel of supply chain compromises,” says Read. “It’s self-perpetuating, and it’s been a hugely successful way to get access to networks and steal stuff.”

Most recently, the group appears to have automated many of its software supply chain attacks with a self-spreading worm that’s come to be known as Mini Shai-Hulud. The name comes from GitHub repositories the worm creates that include encrypted credentials stolen from victims, each of which includes the phrase “A Mini Shai-Hulud Has Appeared” along with a handful of other references to the sci-fi novelDune. That message in turn appears to be a reference not just toDune’s sandworms but to a similarsupply chain compromise worm known as Shai-Hulud that appeared in September, though there’s no evidence TeamPCP was behind that earlier self-spreading malware.

“They’re definitely going for big exposure. They really care about getting big attention,” says Philipp Burckhardt, who leads research at Socket and has tracked TeamPCP for months. “They like to toot their own horn.” A dark-web site for the group, which links to “business contacts” likely used to carry out ransom negotiations, featuresMatrix-style cascading ones and zeros, a reggae fusion soundtrack, and the words “TEAMPCP: The Cats Hijacking Your Supply Chains.”

Before landing on its current strategy for supply chain attacks, TeamPCP emerged in late 2025 exploiting cloud misconfigurations and a vulnerability in the web app development tool Next.js to deploy a botnet for attacks like credential theft and cryptocurrency mining. The group’s reliance on worms emerged during this time with increasing success grabbing static credentials and authentication tokens to bore deeper into victims’ systems.

“It’s been like wildfire; it’s gone very fast,” says Nathaniel Quist, manager of the Cortex Cloud intelligence team at Palo Alto Networks. “They find credentials, personal access tokens, and then it’s just how far can one credential go. I think we will continue to see these techniques. Threat actors know they work, and they’re running with it.”

TeamPCP appears to be financially motivated and often deploys ransomware or data extortion campaigns against its targets, though it also appears willing to sell victims’ data to any buyer. In the most recent case of GitHub, for instance, it wrote on its BreachForums site that “this is not a ransom. We do not care about extorting GitHub, 1 buyer and we shred the data on our end.”

It added what appeared to be a veiled threat to GitHub, perhaps intended to coerce the company to pay: “It looks like our retirement is soon so if no buyer is found we will leak it free.”

The picture has become increasingly complex, Quist says, since TeamPCP began moving to a ransomware-as-a-service model in April by establishing partnerships with the cybercriminal platforms BreachForums and DragonForce. The group has also, at times, seemed to wade into geopolitics, deploying a geographically targeted wiper (dubbed CanisterWormby researchers) that targeted any Kubernetes cloud infrastructure with malware but only deployed a destructive wiper against Iranian targets. This week, an entity claiming to be TeamPCP also leaked the original Shai Hulud worm source code along with detailed documentation, though its motivations for that leak aren’t clear.

The scale of TeamPCP’s targeting expanded dramatically in March as it hacked more software utilities, leading to its more recent cascading effect of supply chain attacks. The group embedded an infostealer in the open source security scanner Trivy and then used stolen credentials from this attack tocompromise certain versionsof the AI application programming interface tool LiteLLM hosted on the popular Python software repository PyPI. The group alsotaintedinfrastructure from the web application security firm Checkmarx, hit the development server pgserve, and compromised the web app library TanStack as well as the enterprise AI platform Mistral AI.

The fallout has been severe. In addition to GitHub, TeamPCP attacks on software service providers have led to breaches of theEuropean Commission’s public website, source code of Anthropic’s Claude, two employees’ devices atOpenAI, compromise of the data contracting firm Mercor, and many others. But Palo Alto’s Quist emphasizes that organizations can protect themselves to a degree through security "hygiene" practices that carefully manage authentication tokens and impose access restrictions wherever possible.

“The biggest opportunistic thing that’s making this operation successful is long-lived credentials in these environments,” he says. “It’s vitally important to change your tokens even if you’re not using LiteLLM or any of these packages that have been compromised. If you have Gitlab and GitHub personal access tokens, rotate them. And AWS, Azure, GCP, Alibab, Oracle all of these credentials are being taken.”

TeamPCP’s tidal waves of tainted code also raise hard questions about how to safely use open source software in an era of mounting supply chain attacks. Wiz’s Read recommends safeguards such as “age-gating” updates to open source tools—vetting and installing security updates but otherwise holding off on immediate updates to code that’s been newly published and may be malicious.

In the case of one recent malicious TeamPCP update, Read says Wiz detected the supply chain compromise and warned customers within minutes, but many of the software’s users had auto-updates enabled and had already downloaded it. “You don't want to just install the freshest version all the time,” Read says.

Amid an epidemic of supply chain attacks like the ones TeamPCP has unleashed, Socket’s Burckhardt says open-source users will need to take trust-but-verify measures, like analyzing updates for malware before rolling them out across a network, as well as the kind of “cool-down” period that Read recommends before downloading and running code.

“At the point it hits your machine,” Burckhardt says, “it’s already too late.”

## Comments

Back to top
Triangle

## You Might Also Like

* How to find us:Add WIRED.com to your preferred sourcesin Google
* These women are trying tooptimize their vaginas
* Big Story:AI gig work is the new waiting tables—and it's soul-crushing
* This summer,the American water crisisbecomes real
* Event:How to adapt, compete, andwin in the next era of business
Andy Greenberg
 is a senior writer for WIRED covering hacking, cybersecurity, and surveillance. He’s the author of the books 
Tracers in the Dark: The Global Hunt for the Crime Lords of Cryptocurrency
 and 
Sandworm: A New Era of Cyberwar and the Hunt for the Kremlin's Most Dangerous Hackers
. His books ... 
Read More
Senior Writer
* X
Lily Hay Newman
 is a senior writer at WIRED focused on information security, digital privacy, and hacking. She previously worked as a technology reporter at Slate, and was the staff writer for Future Tense, a publication and partnership between Slate, the New America Foundation, and Arizona State University. Her work ... 
Read More
Senior Writer
* X
Topics
hacks
github
Microsoft
Crime
cyberattacks
cybercrime
hackers
data breach
software
AI Tools Are Helping Mediocre North Korean Hackers Steal Millions
One group of hackers used AI for everything from vibe coding their malware to creating fake company websites—and stole as much as $12 million in three months.
Matt Burgess
Cybercriminal Twins Caught After They Forgot to Turn Off Microsoft Teams Recording
Plus: Instructure’s Canvas ransomware debacle comes to a close, an alleged dark net market kingpin gets arrested, OpenAI workers fall victim to a supply chain attack, and more.
Andy Greenberg
Newly Deciphered Sabotage Malware May Have Targeted Iran’s Nuclear Program—and Predates Stuxnet
Researchers have finally cracked Fast16, mysterious code capable of silently tampering with calculation and simulation software. It was created in 2005—and likely deployed by the US or an ally.
Andy Greenberg
Dangerous New Linux Exploit Gives Attackers Root Access to Countless Computers
The exploit, dubbed CopyFail and tracked as CVE-2026-31431, allows hackers to take over PCs and data center servers. The Linux vulnerabilities have been patched—but many machines remain at risk.
Dan Goodin, Ars Technica
Thousands of Vibe-Coded Apps Expose Corporate and Personal Data on the Open Web
Companies like Lovable, Base44, Replit, and Netlify use AI to let anyone build a web app in seconds—and in thousands of cases, spill highly sensitive data onto the public internet.
Andy Greenberg
Foxconn Ransomware Attack Shows Nothing Is Safe Forever
Famous for helping build Apple’s iPhones, Foxconn just suffered another cyberattack, highlighting the perils of warehousing some of the world’s most valuable data.
Lily Hay Newman
Hackable Robot Lawn Mower Unlocks a New Nightmare
Plus: Meta officially kills encrypted Instagram DMs, the Trump administration targets “violent left wing extremists,” leaked documents reveal Russia's school for elite hackers, and more.
Matt Burgess
5 AI Models Tried to Scam Me. Some of Them Were Scary Good
The cyber capabilities of AI models have experts rattled. AI’s social skills may be just as dangerous.
Will Knight
Your iPhone Gets Stolen. Then the Hacking Begins
A bustling underground ecosystem is providing criminals with the tools to unlock iPhones—and wage phishing attacks against their contacts to access bank accounts and more.
Matt Burgess
Mozilla Used Anthropic’s Mythos to Find and Fix 271 Bugs in Firefox
The Firefox team doesn’t think emerging AI capabilities will upend cybersecurity long term, but they warn that software developers are likely in for a rocky transition.
Lily Hay Newman
OpenAI Rolls Out ‘Advanced’ Security Mode for At-Risk Accounts
OpenAI is rolling out Advanced Account Security for people concerned that their ChatGPT or Codex accounts could be potential targets of phishing attacks.
Lily Hay Newman
Hackers Hate AI Slop Even More Than You Do
It's not just you. Scammers, hackers, and other cybercriminals are complaining about “AI shit” flooding platforms where they discuss cyberattacks and other illegal activity.
Matt Burgess