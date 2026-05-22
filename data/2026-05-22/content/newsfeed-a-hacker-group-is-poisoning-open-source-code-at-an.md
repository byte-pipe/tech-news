---
title: A hacker group is poisoning open source code at an unprecedented scale
url: https://arstechnica.com/information-technology/2026/05/a-hacker-group-is-poisoning-open-source-code-at-an-unprecedented-scale/
site_name: newsfeed
content_file: newsfeed-a-hacker-group-is-poisoning-open-source-code-at-an
fetched_at: '2026-05-22T11:58:21.372050'
original_url: https://arstechnica.com/information-technology/2026/05/a-hacker-group-is-poisoning-open-source-code-at-an-unprecedented-scale/
date: '2026-05-22'
published_date: '2026-05-22T10:30:14+00:00'
description: GitHub is just the latest victim of TeamPCP, a gang that has carried out a spree of software supply chain attacks.
tags:
- ars-technica
- biz & it
- security
- github
---

Text
 settings

A so-called softwaresupply chain attack, in which hackers corrupt a legitimate piece of software to hide their own malicious code, was once a relatively rare event but one that haunted the cybersecurity world with its insidious threat of turning any innocent application into a dangerous foothold in a victim’s network. Nowone group of cybercriminalshas turned that occasional nightmare into a near-weekly episode, corrupting hundreds of open source tools, extorting victims for profit, and sowing a new level of distrust in an entire ecosystem used to create the world’s software.

On Tuesday night, open source code platform GitHub announced that it had been breached by hackers in one such software supply chain attack: A GitHub developer had installed a “poisoned” extension for VSCode, a plug-in for a commonly used code editor that, like GitHub itself, is owned by Microsoft. As a result, the hackers behind the breach, an increasingly notorious group called TeamPCP, claim to have accessed around 4,000 of GitHub’s code repositories. GitHub’s statement confirmed that it had found at least 3,800 compromised repositories while noting that, based on its findings so far, they all contained GitHub’s own code, not that of customers.

“We are here today to advertise GitHub’s source code and internal orgs for sale,” TeamPCP wrote on BreachForums, a forum and marketplace for cybercriminals. “Everything for the main platform is there and I very am happy to send samples to interested buyers to verify absolute authenticity.”

The GitHub breach is just the latest incident in what has become the longest-running spree of software supply chain attacks ever, with no end in sight. According to cybersecurity firm Socket, which focuses on software supply chains, TeamPCP has, in just the last few months, carried out 20 “waves” of supply chain attacks that have hidden malware in more than 500 distinct pieces of software, or well over a thousand counting all of the various versions of the code that TeamPCP has hijacked.

Those tainted pieces of code have allowed TeamPCP’s hackers to breach hundreds of companies that installed the software, says Ben Read, who leads strategic threat intelligence at the cloud security firm Wiz. GitHub is only the latest on the group’s long list of victims, which has also included AI firm OpenAI and the data contracting firm Mercor. “It may be their biggest one,” Read says of the GitHub breach. “But each one of these is a big deal for the company that it happens to. It’s not qualitatively different from the 14 breaches that happened last week.”

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

The fallout has been severe. In addition to GitHub, TeamPCP attacks on software service providers have led to breaches of theEuropean Commission’s public website and the data contracting firm Mercor, compromise of two employees’ devices atOpenAIand many other incidents. But Palo Alto’s Quist emphasizes that organizations can protect themselves to a degree through security “hygiene” practices that carefully manage authentication tokens and impose access restrictions wherever possible.

“The biggest opportunistic thing that’s making this operation successful is long-lived credentials in these environments,” he says. “It’s vitally important to change your tokens even if you’re not using LiteLLM or any of these packages that have been compromised. If you have Gitlab and GitHub personal access tokens, rotate them. And AWS, Azure, GCP, Alibab, Oracle all of these credentials are being taken.”

TeamPCP’s tidal waves of tainted code also raise hard questions about how to safely use open source software in an era of mounting supply chain attacks. Wiz’s Read recommends safeguards such as “age-gating” updates to open source tools—vetting and installing security updates but otherwise holding off on immediate updates to code that’s been newly published and may be malicious.

In the case of one recent malicious TeamPCP update, Read says Wiz detected the supply chain compromise and warned customers within minutes, but many of the software’s users had auto-updates enabled and had already downloaded it. “You don’t want to just install the freshest version all the time,” Read says.

Amid an epidemic of supply chain attacks like the ones TeamPCP has unleashed, Socket’s Burckhardt says open-source users will need to take trust-but-verify measures, like analyzing updates for malware before rolling them out across a network, as well as the kind of “cool-down” period that Read recommends before downloading and running code.

“At the point it hits your machine,” Burckhardt says, “it’s already too late.”

This story originally appeared atWIRED.com.

 WIRED
 

 WIRED
 

 Wired.com is your essential daily guide to what's next, delivering the most original and complete take you'll find anywhere on innovation's impact on technology, science, business and culture.
 

1. 1.Zillow loses thousands of listings in fight over “hidden” homes
2. 2.Uh-oh, the International Space Station is leaking again
3. 3.The Internet can't stop watching Figure AI's humanoid robots handling packages
4. 4.These clever active beam headlights are finally coming to America
5. 5.Famously secret about its finances, SpaceX opens its books for the first time

Customize