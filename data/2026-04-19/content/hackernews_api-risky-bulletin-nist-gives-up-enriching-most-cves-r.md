---
title: 'Risky Bulletin: NIST gives up enriching most CVEs - Risky Business Media'
url: https://risky.biz/risky-bulletin-nist-gives-up-enriching-most-cves/
site_name: hackernews_api
content_file: hackernews_api-risky-bulletin-nist-gives-up-enriching-most-cves-r
fetched_at: '2026-04-19T06:00:15.957625'
original_url: https://risky.biz/risky-bulletin-nist-gives-up-enriching-most-cves/
author: Catalin Cimpanu
date: '2026-04-18'
description: The US National Institute of Standards and Technology announced on Wednesday a new policy regarding the US National Vulnerability Database [Read More]
tags:
- hackernews
- trending
---

### Risky Bulletin Newsletter

### April 17, 2026

## Risky Bulletin: NIST gives up enriching most CVEs

Written by

Catalin Cimpanu

News Editor

This newsletter is brought to you byCorelight. You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business" in your podcatcher or subscribing viathis RSS feed. You can also add the Risky Business newsletter as a Preferred Source to your Google search results by goinghere.

The US National Institute of Standards and Technology announced on Wednesday a new policy regarding the US National Vulnerability Database, which the agency has been struggling to keep updated with details for every new vulnerability added to the system.

Going forward,NIST saysits staff will only add data—in a process calledenrichment—only for important vulnerabilities.

This will include three types of security flaws, which the agency says are critical to the safe operation of US government networks and its private sector.

* CVE entries for vulnerabilities listed inCISA KEV, a database of actively exploited bugs;
* CVEs in software known to be used byUS federal agencies;
* and CVEs in what the agency classifies as "critical software."

This latter category sounds restrictive, but is in fact quite broad and includes all the major software you'd expect and want to have properly enriched CVEs for. Stuff like operating systems, web browsers, security software, firewalls, backup software, and VPNs; they are all on the list [PDF], which you can also see below this post.

NIST has been struggling to enrich CVEs for more than two years due to an explosion in bug discoveries and mounting costs, also made worse by the Trump administration's recent cuts to various DHS and CISA budgets.

Its problems startedin early 2024, when a handful of 2,100+ CVE entries that were left without enriched metadata turned into almost 30,000 by the end of the year. Despite efforts to catch up and add details to all CVEs published in the NVD, the agency is still tens of thousands of bugs behind.

The NIST announcement is a capitulation, with the agency admitting it won't ever catch up due to its current budgetary circumstances.

It is a smart decision. Even though this sounds as a blasphemy for the infosec people in the vulnerability management space, the only way forward for NIST was to focus on the important bugs only and giving up on all the CVE chaff.

Each year, there are tens of thousands of vulnerabilities being reported in all kinds of no-name software you have never heard of, in all the tiny libraries that barely have 100 stars on GitHub, and all the IoT gear and their firmware components.

The announcement is not what the vulnerability management companies wanted, since many of them relied on packaging the NVD output into their own vulnerability scanners, dashboards, and reporting tools.

With some of that output set to disappear for good, they will have to find other places to get the data, or enrich it themselves. Aikido Security's Sooraj Shah has anexcellent takeon what this means for the industry

"The TL;DR is that there is no single source of truth anymore (if there ever really was). NVD is deprioritizing, EUVD is nascent but may go the same way, and other CVE programs, such as MITRE, have had funding scares. Being reliant on one database as a team or for a security tool means you have less coverage and visibility. That era is officially over."

The cybersecurity industry was expecting this to happen. At a January quarterly meeting, NIST officials talked about "rethinking" the agency's role in analyzing software vulnerabilities, and hinted at a plan to only triage the important bugs.

NIST says that besides focusing on enriching only the big bugs, it will alsostop providingits own CVSS severity scores for NVD entries, and will now show the severity score initially assigned by the organization that issued the CVE.

This opens the door for a lot of infosec drama. Some of the organizations that issue CVE numbers are also the makers of the "reported" software, and these companies are extremely likely to issue low severity scores and downplay their own bugs.

This has been happening for decades, and if you read enough vulnerability write-ups, you'll often find security researchers accusing companies of blatantly downgrading CVSS scores and mischaracterizing their own bugs to downplay the bug's impact, over and over again.

More than48,000 vulnerabilitiesreceived a CVE number last year and NIST is giving up right before experts anticipate this number will explode with the broad adoption of AI cybersecurity agents designed to help improve vulnerability discovery.

The integration of AI vulnerability scanners is likely to yield a few major bugs, but they're also expected to produce mountains of CVE chaff that no human team at NIST would have been able to keep up with anyway.

NIST's new enrichment policy entered into effect this week, on Wednesday, April 15.

### Risky Business Podcasts

The mainRisky Businesspodcast is now on YouTube with video versions of our recent episodes. Below is our latest weekly show with Pat and Adam at the helm!

### Breaches, hacks, and security incidents

Russian hackers targeted a Swedish thermal plant:A pro-Russian hacktivist group tried to disrupt a Swedish thermal power ​plant last year. The attack targeted a power plant in western ​Sweden last spring. The intrusion was caught by the plant's built-in safeguards. Swedish officials linked the group to Russia's security services. [EnergyWatch//SVT]

Russia hacked Ukrainian prosecutors:Russian hackers have broken into the emails of more than 170 Ukrainian prosecutors. The campaign sought to gain access to investigative information. The attacks were linked to APT28, a cyber unit inside Russia's military intelligence agency, the GRU. The same campaign also breached militaries in Greece, Romania, and Serbia. The hacks are part of a campaign spotted last month byCtrl-Alt-Intel. [Reuters]

Grinex shuts down after hack:Russian cryptocurrency exchange Grinex has shuttered operations following a theft this week. The company claims "Western intelligence agencies" broke into its wallets and stole $13 million (1 billion rubles) worth of assets. The exchange wassanctionedby US authorities last August for helping Russia evade sanctions and laundering ransomware payments. ATRM Labs reportfound that Grinex was a rebrand of an older Russian crypto exchange Garantex, also sanctioned for the same things. [Wayback Machine]

Zerion blames North Korea for crypto-heist:Crypto-wallet provider Zerion hasblameda recent heist of $100,000 on North Korean hackers.

Autovista ransomware attack:A ransomware group has hit automotive data analytics companyAutovista, with the attack impacting systems in Europe and Australia.

McGraw Hill breach:Hackers have leaked the personal details of13.5 million usersof educational platform McGraw Hill. The data was taken from the company's SalesForce accounts. It was leaked after a failed extortion attempt by the ShinyHunters group. It includes details such as real names, home addresses, emails, and phone numbers.

Standard Bank breach:South Africa's largest bank has disclosed a security breach. The Standard Bank says hackers breached last week an internal network storing customer data. The incident is the third hack of a South African bank this year. [IOL]

BlueLeaks 2.0 data is now up for sale:A hacker is selling 8.3 million confidential crime tips for $10,000 in cryptocurrency. The data was stolen earlier this year from P3 Global Intel, a software provider for US law enforcement agencies. The hacker, who goes by the nameInternet Yiff Machine, initially provided the data for free to select journalists and the DDoSecrets project. The hacker says they're selling the data because "principles are for the well-fed, and I’m unfortunately not in a great place." [Straight Arrow News//DataBreaches.net]

Krybit hacks 0APT:The Krybit ransomware group has hacked the website of rival ransom group 0APT. The incident occurred after the 0APT groupthreatenedto dox Krybit's members last week. According to security firmBarricade, 0APT leaked plaintext credentials for Krybit's ransomware backend panel, along with Bitcoin addresses and victim names. Krybit returned the favor by leaking 0APT's entire server contents.

### General tech and privacy

OpenAI announces its own private cyber model:OpenAI has released an LLM model for cybersecurity work into private testing. Thousands of verified professionals and hundreds of teams responsible for defending critical software have been invited to test theGPT‑5.4‑Cybermodel. The new model has loose permissions for cybersecurity research, such as reverse-engineering and vulnerability discovery. The new limited access model is OpenAI's response to Anthropic's Project Glasswing and the Mythos model.

Anthropic rolls out KYC for Claude:Anthropic will ask certain Claude users to verify their identity by providing a selfie and a government ID. Thecompany saysthe new identity verification check will only roll out in a "few use cases." The checks are meant to prevent abuse and comply with legal obligations. The ID checks will be handled by Persona, the same company Discord had to cut ties because of community backlash.

BlueSky's mega outage:Social media network BlueSky had a prolonged outage on Thursday that was so bad, even its server status page was down—probably because they hosted it on the same infrastructure. You live and learn, I guess. [News.az]

Grok is still nudifying:xAI's Grok is still generating nude images at users' requests, despite a huge backlash from authorities all over the world. Just take Grok behind the shed, Elon! It's time. [NBC News]

Nudify apps are still everywhere:Both Apple and Google are still hosting nudify apps on their stores, and their ad systems are often used to lure users to the very same apps they're supposed to have banned. [Tech Transparency Project]

News sites block the Internet Archive:Twenty-three major news outlets are now blocking the Internet Archive's Wayback Machine from creating copies of their content. Most cited fear the backed up pages could be used as a proxy to train AI on their content. [Tom's Hardware]

IPv6 milestone:Global IPv6 traffic hascrossed 50%for the first time at the end of last month.

IPv8 protocol proposal:A new version of the IP addressing protocol has been proposed with the Internet Engineering Task Force. The new protocol is being calledIPv8and is meant to be compatible with old IPv4 addresses. IPv8 addresses will include a prefix and an old IPv4 address. The prefix will be specific to each ASN (network operator). For old IPv4 addresses, this prefix will be 0.0.0.0. This will allow devices and networks with old IPv4 addresses to connect to IPv8 systems without any software updates required.

Chrome does nothing to stop browser fingerprinting:Web privacy expertAlexander Hanfflooks at the various browser fingerprinting techniques used by online trackers and how Chrome doesn't do anything to block them.

Android gets new one-time data pickers:The next Android OS version will includetwo new systemsto let users pick contacts or share their precise location for one time without an app needing persistent access to the read contacts and precise geolocation permissions.

Raspberry Pi disables passwordless sudo:The Raspberry Pi project hasdisabledpasswordless access to the sudo utility in its OS.

Some ESUs extended:Microsoft hasextendedthe Exchange 2016/2019 Extended Security Updates (ESU) program until October this year. The ESU ended this month.Same goesfor the Skype for Business ESU.

Windows adds RDP warning popups:Windows will now show asecurity warning popupwhenever users open RDP configuration files. The popups will alert users that they are about to make dangerous changes that may allow remote attackers to connect to their PCs and steal data. Several threat actors have used malicious RDP config files in phishing operations as a way to gain a foothold inside targeted networks. Russian group ATP29 is known for using this technique in espionage operations.

### Government, politics, and policy

FCC exempts Netgear from foreign router ban:The US Federal Communications Commission has excluded Netgear from the Trump administration ban on foreign-made routers. The agency granted theexemptionat the request of the US Department of War. Netgear is an American company but most of its routers are made in Southeast Asia.

More cyber EOs are coming:National Cyber Director Sean Cairncross says the Trump administration will soon sign and issue more cyber-related executive orders to help push forward the implementation of the White House's new cybersecurity strategy. [CyberScoop]

US Tech Force is hiring cyber staff:The Trump administration isrecruitingcybersecurity specialists for its new and upcoming US Tech Force agency. The Tech Force was announced at the end of last year. The plan is to recruit around 1,000 tech workers from large US corps to "modernize" the US government's networks. The new hiring process comes after the Trump administration fired a third of CISA's staff and plans hundreds more next year. CISA alsorecently canceledsummer internships for cyber scholarship students amid DHS funding lapse.

Foreign internet traffic in Russia is becoming very expensive:Russian telcos will increase the price for internet traffic received from outside the country's borders as part of measures to crack down on VPN use. [RBC]

EU launches age verification app:The EU haslaunchedits own internally-developed age verification app.The appuses cryptographic proofs to verify a user's age without sharing their personal data. EU officials have urged online platforms to integrate the app with their processes. Age verification is mandatory under the EU's new Digital Services Act. The app is available for Android and iOS, and future desktop and web versions are planned. The source code is also availableon GitHub.

### Sponsor section

In thisRisky Business sponsor interview, Corelight’s Senior Director of Product Management, Dave Getman, tells James Wilson how Corelight Agentic Triage helps defenders stay ahead of AI-powered attacks.

### Arrests, cybercrime, and threat intel

DPRK laptop farmers sentenced:The US hassentencedtwo individuals to prison for running a laptop farm for North Korean remote IT workers. Kejia Wang and Zhenxing Wang were sentenced to 108 and 92 months in prison, respectively. Both hosted laptops at their homes in New Jersey that ran from US IPs to allow North Koreans to pose as American citizens. Authorities also indicted nine North Koreans remote workers who participated in the scheme.

16yo arrested for school cyberattack:Northern Ireland authorities havearresteda 16-year-old for a cyberattack that disrupted the country's national school IT network. The C2K platform was down at the start of the month after a cyberattack that targeted a small number of schools. More than 300,000 pupils and 20,000 teachers couldn't access exam data, home assignments, and teaching materials for days following the incidents, as officials shut down the platform to investigate. [BelfastLive]

53 DDoS-for-hire domains seized:Europol and other law enforcement agencies haveseized 53 domainsthat hosted DDoS-for-hire services. Four suspects were also detained following 25 house searches. Authorities have also sent letters and emails to more than 75,000 users who had signed up for the services. They also worked with Google to remove ads promoting DDoS services.

UNC2465 shifts to Europe:Orange's security team reports that a known ransomware affiliate tracked asUNC2465has shifted its attacks to Europe. The group is currently using the SmokedHam backdoor as an initial entry point for Qilin ransomware attacks.

Black Basta offshoots target execs:A group of former Black Basta affiliates are using automated email bombing and Teams-based social engineering to target executives and senior-level employees for initial access into corporate networks. [ReliaQuest]

Hazy Hawk hijacks university subdomains:A cybercrime group has hijacked subdomains at 34 US universities and educational organizations to show pornographic spam. MIT, Harvard, Stanford, Johns Hopkins, and other large universities have had subdomains hacked. The spam campaign has been linked to Hazy Hawk, a group that hijacked CDC subdomains last year. [SH Consulting]

QEMU abused in the wild:Sophos saysat least two cybercrime groups are deploying the QEMU virtualization environment on compromised networks to hide malicious activity and later deploy ransomware.

WP scanning:F5 says a badness cluster it's been keeping an eye on has recently startedmass-scansfor sites running vulnerable WordPress plugins.

FTP exposure is still huge:According toCensys, there are still 6 million endpoints exposing an FTP port over the internet, almost 55 years after the protocol was created.

C2 servers in Russia:A large-scale study of the Russian web hosting space has found more than 1,200 malicious command and control servers hosted inside Russia this year. Most of the servers are for IoT malware botnets, such as Keitaro, Hajime, Mozi, and Mirai. [Hunt Intelligence]

### Malware technical reports

Rhadamanthys's secret bug:The Rhadamanthys infostealer left its command and control server APIs exposed online without authentication, allowing security researchers to track its activity for months before the Europol takedown last year. [Censys]

Direct-Sys Loader:The Cyderes team has discovered a new malware loader namedDirect-Sys Loaderbeing delivered in the wild.

PowMix botnet:Cisco Talos has spotted a new Windows botnet malware strain namedPowMix, currently going on a test run in the Czech Republic.

AngrySpark:Gen Digital has spotted a new Windows rootkit namedAngrySpark, already used in the wild on a UK victim's system.

W3LL PhaaS:Group-IB published a report onW3LL, the phishing platformseizedby authorities earlier this month.

ATHR platform:A cybercrime group has developed and is renting access to a platform that automates voice phishing attacks. The ATHR platform uses AI agents to call targets using preconfigured and multi-step scripts. ATHR access is being sold for $4,000 and 10% of a campaign's profits. According toAbnormalAI, the platform is primarily being used to trick victims into revealing credentials for their online accounts.

### Sponsor section

James Pope, Corelight's Director of Technical Marketing Engineering, demonstrates the company's Open NDR Platform and how it combines network detections with a whole host of other data sources.

### APTs, cyber-espionage, and info-ops

UAC-0247 and AGINGFLY:CERT-UA reported a new wave of attacks against its government agencies, hospitals, and emergency services. This activity was linked to a cluster tracked as UAC-0247. The final payload was a new infostealer namedAGINGFLY.

Sapphire Sleet targets macOS:DPRK APT group Sapphire Sleet has adapted its "install this Zoom update to hear me" malware delivery technique for macOS, per a newMicrosoft report.

### Vulnerabilities, security research, and bug bounty

Security updates:Apache Tomcat,Cisco,Composer,Dolibarr,Kubernetes,NGINX,Thymeleaf.

PyPI security audit:Python's PyPI has completed itssecond security audit.

Zero Day Quest 2026:Microsoft awarded$2.3 millionin bug bounty rewards at this year's edition of Zero Day Quest, its cloud and AI hacking contest.

Mythos guidance:Cisco [PDF]and theCloud Security Alliancehave issued guides on how to protect and defend networks in the face of rising powerful AI vulnerability discovery agents like Anthropic's Mythos.

Mythos/Glasswing vulnerabilities:VulnCheck has sifted through its huge CVE database and believes it hastracked downsome of the bugs discovered using Anthropic's Mythos agent as part of Project Glasswing. There are 75 CVEs that mention Anthropic, 40 credited to Anthropic, but only one specifically mentions Glasswing. So far, it's unclear if any of the Mythos-found bugs even received proper CVEs.

You can trick Claude by being an industry legend:Manifold Securitytricked Claude' GitHub bot to merge malicious code to repositories by spoofing their requests under the names of famous developers.

Researcher drops another Windows zero-day:A disgruntled security researcher haspublishedproof-of-concept code for a new Windows zero-day. TheRedSunzero-day can be used to elevate privileges on Windows to SYSTEM level access. The researcher released the public exploit after a disagreement with the Microsoft team that handles its bug bounty program. The same researcher also released another Windows zero-day named BlueHammer earlier this month.

NGINX UI bug exploited in the wild:Hackers are exploiting a bug in a popular dashboard for managing NGINX web servers. Attacks beganlast monthand are targeting the dashboard's MCP endpoints. Tracked asCVE-2026-33032, the bug allows attackers to access the MCP endpoint without authentication and then modify the server's config files. More than 2,600 of NGINX UI dashboards are currently exposed on the internet. [Pluto Security]

RAGFlow patches bug after public disclosure:The RAGFlow AI toolkit haspatcheda remote code execution bug in its software almost a week after the bug waspublicly disclosedby security researchers. The project initially ignored the report and only patched the issue after the researchers themselves submitted the patch code.

Dolibarr RCE:The Dolibarr CRM and ERP haspatchedan eval-based remote code execution bug (CVE-2026-22666). A write-up and POC are available viaJiva Security.

Thymeleaf RCE:A critical vulnerability has been patched in the Java template engine Thymeleaf. Tracked asCVE-2026-40478, the bug allows attackers to bypass security checks and inject malicious content in server page templates. The bug impacts all Thymeleaf versions ever released and has a wide impact since Thymeleaf is also the default template engine in the Spring Boot Java framework. [Endor Labs]

Codex hacks a smart TV:Security firm Calif has used OpenAI's Codex agent to hack andgain root accesson a Samsung smart TV.

Fabricked attack:A team of academics has developed a new attack that breaks the confidentiality of AMD's secure enclave technology. TheFabricked attackredirects memory transactions to trick AMD's secure co-processor into improperly initializing SEV-SNP enclaves. The novel technique allows attackers to control confidential virtual machines where each individual customer's data is typically processed in cloud environments. AMDreleased patchesthis week as part of its Patch Tuesday. Frabricked is one of multiple AMD SEV-SNP attacks disclosed over the past two years. Others include RMPocalypse, BadRAM, Ahoi, Heracles, WireTap, BatteringRAM, and TEE.Fail.

 
 
 
Post by @stevel@hachyderm.io
 
View on Mastodon
 
 
 

### Infosec industry

Threat/trend reports:Check Point,CyberHUB-AM,Google Mandiant,GuidePoint Security,Kaspersky, andSysdighave recently published reports and summaries covering various threats and infosec industry trends.

New tool—Jaspr:Googlehas open-sourcedJaspr, a new web development framework written in Dart.

New tool—Malfixer:Mobile security firmCleafyhas open-sourcedMalfixer, a toolkit for inspecting and recovering malformed Android APK files.

New tool—RePythonNET-MCP:Security firmSekoiahas open-sourcedRePythonNET-MCP, an MCP server for .NET reverse engineering automation.

New tool—PMG:DevSecOps firmSafeDephas releasedPMG, a tool that delays npm and Python package installs until the libraries are checked against its threat intel database.

New tool—HoneyWire:Andrea Termine has publishedHoneyWire, a lightweight distributed deception engine designed for internal networks.

New tool—NetWatch:Westpac's chief engineer Matt Hartley has releasedNetWatch, a real-time network diagnostics tool for terminals.

### Risky Business podcasts

In this edition ofSeriously Risky Business, Tom Uren and Amberleigh Jack talk about a new Citizen Lab report into Webloc, a tool to identify and track mobile devices. It demonstrates how the collection and sale of mobile phone geolocation data presents privacy and national security risks.

In this episode ofRisky Business Features, James Wilson chats to professional hacker Jamieson O’Reilly about Anthropic’s Mythos and the impact it could have on offensive security. Jamieson is CEO of DVULN and co-founder of Aether AI.