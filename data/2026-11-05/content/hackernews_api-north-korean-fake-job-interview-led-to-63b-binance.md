---
title: North Korean fake job interview led to $6.3B Binance heist
url: https://www.theregister.com/security/2026/11/03/north-korean-fake-job-interview-led-to-63b-binance-heist/5307398
site_name: hackernews_api
content_file: hackernews_api-north-korean-fake-job-interview-led-to-63b-binance
fetched_at: '2026-11-05T15:23:43.444500'
original_url: https://www.theregister.com/security/2026/11/03/north-korean-fake-job-interview-led-to-63b-binance-heist/5307398
author: smalltech
date: '2026-11-05'
published_date: '2026-11-03T22:04:45.000Z'
description: '''It was not a single isolated breach or a simple phishing incident,'' exchange says'
tags:
- hackernews
- trending
---

security

 

# North Korean fake job interview led to $6.3B Binance heist

'It was not a single isolated breach or a simple phishing incident,' exchange says

Jessica Lyons

Jessica

Lyons

Cybersecurity Editor

Published

tue 3 Nov 2026 // 22:04 UTC

Make us preferred on Google

### READ MORE

* #### FBI pins $6.3B Binance crypto heist on North Korean hackers2 days ago
* #### Google says Asian advertisers spending less due to Europe's customs changes3 days ago
* #### In the year AI re-wrote the infosec rulebook, it’s comforting to know crypto exchanges still have bad security5 days ago
* #### Attackers turn GitHub issues into supply chain campaign against 61 public repos in less than an hour6 days ago
* #### China's spaceplane bears striking resemblance to America's X-37B7 days ago

North Korean cryptocurrency thieves tricked a Binance software engineer into downloading malware onto their work-issued computer during a fake job interview process before last week'srecord-breaking $6.3 billion heist.

In an incident report published on Tuesday, the cryptocurrency exchange said several techniques - including social engineering via fake job interviews, malware downloads, compromised internal AI tooling, endpoint takeover, and an “advanced transaction-authorization method” - led to the October 29 security breach.

“Our current investigation indicates that this was a sophisticated, multi-stage campaign,” theincident reportsaid. “It was not a single isolated breach or a simple phishing incident.”

REG AD

Over the weekend, theFBI attributed the theftto TraderTraitor, a North Korean hacking operation linked toLazarus Group, known for combining espionage withmassive cryptocurrency heists. The Pyongyang-backed crew is also highly adept atjob market scams- bothposing as IT workers, who are thenhired by Western companies, and aspotential employersto lure software engineers intodownloading malwareandinfecting corporate devices.

REG AD

With the recent Binance attack, the Norks used the latter.

The attack prep began back in June with a supply chain attack when one of its engineers downloaded amalicious Homebrew installation. While the malware was detected by the security team, the device was replaced, and all affected credentials rotated, “Engineer A’s role and his related colleagues on our wallet infrastructure team was exposed to the hacker,” the report says.

Three months later, the social engineering part of the attack happened.

In September, another software engineer was contacted via a “legitimate job-hunting platform” by someone purporting to be a project director who arranged a series of job interviews for the Binance engineer with the fake company. During the first round - a live video interview with the engineer and a fake HR rep - the interviewer “shared a social media account with him, including personal photos and videos posted on the platform, in order to build trust,” according to the report. “This was more advanced and deceptive than previously seen social engineering approaches.”

The second interview with someone purporting to be the CEO of the phony company was conducted on a “popular social chat app,” and toward the end, the CEO instructed the engineer to download an “assignment” containing a malware-laced code repository. The code executed on his work computer during the setup process, which kicked off a series of unauthorized activities.

According to Binance, the malware replaced a legitimate development tool component with a malicious version, which executed commands and established communication with an attacker-controlled external server. The attackers also took steps to hide the malicious script and evade detection, and it worked. Binance’s endpoint security tools did not immediately detect the malware.

Here’s the script:

CREATE  /opt/homebrew/Cellar/pyenv/2.8.0/libexec/pyenv_

REG AD

MODIFY  pyenv_ → 3,414 B

DELETE  .../libexec/pyenv  (3,344 B)      ← remove the valid pyenv

RENAME  pyenv_ → pyenv  (3,414 B)  ← replace it with a malicious version

DELETE  /opt/homebrew/bin/pyenv  (3,414 B)

ln  (create a new symlink)  +  spawn zsh

Then, on October 20, the miscreants used the compromised computer and an internal AI tool to gain access to the computers of wallet DevOps engineer A and another wallet software developer, Engineer C.

Engineer A had a container deployment permission token on his computer, which the Norks soon discovered. On October 29, the attacker accessed Engineer C's computer, used the stolen credentials from Engineer A to deploy a container, and triggered a script to launch the cryptocurrency-stealing attack.

As of Tuesday, Binance said it has rebuilt the compromised wallet system and internal AI tool, and replaced all of the affected devices. It also decommissioned all credentials and tokens assigned to the compromised engineers, and is working with law enforcement, blockchain intel firms, and security researchers to trace and freeze the assets.

REG AD

The crypto exchange has also hired independent cybersecurity experts to conduct a cybersecurity review of the incident, and recommend additional protective measures. Binance said it’s also working to establish a security research fund and initiatives with AI companies and security shops to focus on AI security in blockchain environments.®

supply chain attack

north korea

binance

security

cryptocurrency

Make us preferred on Google

REG AD

## Microsoft admits certifications can be a drag, launches creds that recognize skills

‘Pro Badges’ don’t require a test, Microsoft awards them by watching you use GitHub

## Uber says it alone can make robotaxis pay, hours after Waymo quit its app

Oh, the irony, as platform players fight

## From expertise to intelligence: NISCO deploys world's first swarm-intelligence steel model at scale

PARTNER CONTENT: 300+ AI applications delivering surges in core metrics and annual cost reduction of over CNY100m

## Meta brings Conductor on board its model train

Agent orchestration startup gets its exit

OPINION

## Microsoft's moolah mountain is more massive than ever. It just doesn't want the people who built it

Flash the cash, flush the cache

## Building AI factories at enterprise scale

SPONSORED FEATURE: ASUS wants to scale AI everywhere in the enterprise

### TOP STORIES

* #### Landline phones will switch off across Britland in 100 days, no extensions – Openreach
* #### Cops bust botnet of 1.3M infected Android TV boxes
* #### British fintech Revolut slashes AI coding costs 10x by cutting out Claude and going self-hosted
* #### Linus Torvalds says Linux kernel is out of 'stabilization phase' and using 'much healthier model' for AI contributions
* #### North Korean fake job interview led to $6.3B Binance heist
* #### Google struggling to make AI Mode searches pay

### AI

* #### Meta brings Conductor on board its model trainAgent orchestration startup gets its exit
* #### Bare metal boom: On-prem server sales for HPC and AI up 20% this yearFirms still want kit on-premises, but spike in revenue is as much about increased costs as higher sales
* #### Windows pushed AI PCs, but now it's hit a wall of RAM pricesCustomers sweating assets amid tight budgets, as Microsoft execs get creative with sales pitches
* #### Drax wants to feed Britain's AI habit with £20B datacenter at biomass power stationBut first it needs planning permission, government approval and, rather importantly, a customer
* #### Anthropic's compute tab could top $1T as Q3 revenue nears $17BRevised IPO filing warns 12x revenue growth is unlikely to continue

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### Achieving nirvana: Enlightenment 0.28 hits the desktopVery nearly 30something environment gets spruced up… and there's a new Trinity, too
* #### Architect creates open source replacement for VM migration tool VMware has hiddenOpenVDDK is reportedly already being used in production, at scale
* #### AlpineBSD announced – an AI-free FOSS OSCombining the NetBSD kernel with the Alpine Linux userland
* #### Ubuntu 27.04 may bring a preview of the long-awaited Core DesktopCanonical has a long way to catch up, but it knows who it's chasing
* #### Systemd adds support for RustWhat's even better than Rust in the Linux kernel? Rust in systemd!
* #### FreeBSD founder ports Omarchy to FreeBSD in ten days, ten releasesDaemonarchy is unaffiliated with the Linux original, built with AI help, and could complicate FreeBSD's debate over AI contributions