---
title: Microsoft patches Windows and Excel – breaks audio, remote access, and paste
url: https://www.theregister.com/os-platforms/2026/09/14/microsoft-patches-windows-and-excel-breaks-audio-remote-access-and-paste/5296085
site_name: hnrss
content_file: hnrss-microsoft-patches-windows-and-excel-breaks-audio-r
fetched_at: '2026-09-15T07:38:35.552968'
original_url: https://www.theregister.com/os-platforms/2026/09/14/microsoft-patches-windows-and-excel-breaks-audio-remote-access-and-paste/5296085
date: '2026-09-14'
published_date: '2026-09-14T13:00:00.000Z'
description: Redmond's quality drive takes another detour through the known issues list
tags:
- hackernews
- hnrss
---

OS Platforms

 

# Microsoft patches Windows and Excel – breaks audio, remote access, and paste

Redmond's quality drive takes another detour through the known issues list

Richard Speed

Richard

Speed

MICROSOFT ECOSYSTEM REPORTER

Published

mon 14 Sep 2026 // 14:00 UTC

### READ MORE

* #### Microsoft anoints Rust as a 'Tier 1' internal language3 days ago
* #### Azure SQL Data Sync stops taking newcomers before 2027 execution4 days ago
* #### AI uprising postponed after Copilot falls off the web4 days ago
* #### Microsoft goes after Salesforce and ERP users with AI-powered converter4 days ago
* #### Novel Blue Moon kit targeting Chrome and Windows reflects new reality of AI-driven exploits4 days ago

Microsoft has confirmed that its latest security updates can disrupt Remote Desktop Services, silence some USB audio devices, and break pasting in Excel.

September's Windows patches hardly support Microsoft's insistence thatit is sorting out quality. The known issues list suggests there's still work to do.

Reports of problems with Remote Desktop Services (RDS) began circulating on social media shortly after the update, and Microsoft has nowacknowledgedthat, for some users, RDS has indeed been broken across multiple Windows versions, including Windows 11 26H1 and Windows Server 2012.

REG AD

The latter is due todrop out of the Extended Security Updates (ESU)program on October 13, 2026, so perhaps administrators might consider this a going-away present from Microsoft?

REG AD

Connections might fail after a few minutes, servers might hang at "Please wait for the Remote Desktop Configuration," and so on.

"Related tools, including Microsoft Management Console (MMC), RDS Licensing Diagnoser, and File Explorer might also become unresponsive," Microsoft admitted.

"Additionally, the Windows Update page might stop responding and continuously display a loading indicator."

If a virtual machine becomes inaccessible through RDP, stopping (deallocating) and restarting it might temporarily restore connectivity. Microsoft is working on a fix.

Microsoft alsoconfirmedissues with support for some USB Audio Class 1.0 devices on Windows 11 26H1, 25H2, and 24H2. The standard dates back to the previous century, but affected users might find themselves with no audio, broken sound settings and volume controls, or problems with multichannel audio.

Some customers have restored audio by switching to two-channel mode, Microsoft says. The company is working on a fix but has not provided a timeline.

Users of Microsoft's productivity applications were not left out. either A fix for Excel remote code execution and information disclosure vulnerabilities has broken a basic spreadsheet function.

"The paste operation might fail silently,"accordingto Microsoft.

REG AD

Excel 2016, 2019, 2021, and 2024 are affected. Microsoft said: "Although users try to paste content, the source remains selected and the destination is unmodified. When this issue occurs, users receive no indication of the failure, such as a beep or error message."

The bad news for users with automatic updating turned on is that this update could have already been downloaded and installed automatically. Microsoft has not published a workaround, and one forum user reported resolving the issue by uninstalling and reinstalling Office, while othersreported successusing commands to uninstall the security update. Removing the update also removes its security fixes. ®

excel

windows

os platforms

microsoft

REG AD

databases

## Oracle celebrates banner quarter with another round of layoffs

Congratulations on helping Larry Ellison's AI cloud boom. Now please pack your bags and go

SECURITY

## New hardware device can RAM into encrypted memory, expose your data

Attackers would need physical access to the server to pull off the DDR5 trick

## HPE makes its “unified storage” claim real as B10000 R6 hits GA

PARTNER CONTENT: Pairs block and adjacent file workloads with independent scaling of performance and capacity

Security

## OpenAI's malicious bot swarm attacked RubyGems

Ruby are you ok? Ruby are you ok? Are you ok Ruby?

COLUMNISTS

## Europe's right-to-repair rules are broken, not beaten

Patchy compliance is an argument for stronger enforcement, not abandoning the project

on-prem

## Datacenter developers want your backyard. FAS says negotiate harder

Tax breaks, water, noise, decommissioning - report tells local officials what to nail down before signing

### TOP STORIES

* PERSONAL TECH#### Smartphone makers don't bother to comply with EU repairability requirements
* NETWORKS#### Virgin Media offloads email services to third-party provider
* offbeat#### Retired man turns spare room into Soviet-era supercomputer
* CYBER-CRIME#### Ukrainian lawyer's second career as a Conti coder earns him 4 years behind bars
* software#### Another Microsoft team admits it’s struggling to handle flood of AI-generated code
* virtualization#### VMware defends ending downloads of SDK that helps VM backups – or migrations to rivals

### AI

* on-prem#### Datacenter developers want your backyard. FAS says negotiate harderTax breaks, water, noise, decommissioning - report tells local officials what to nail down before signing
* LEGAL#### Nvidia's Groq acquihire is on the DOJ's radar, but it's already too lateEven if regulators did somehow unwind the $20B deal, there's a growing list of alternatives ready to take Groq's place, no merger required
* SECURITY#### Watch out: Apple timepiece can grab snippets of conversation without both speakers' consentWar is peace. Freedom is slavery. Privacy is surveillance
* SYSTEMS#### d-Matrix drinks the Nvidia Kool-Aid with NVLink Fusion and MGX rack designsAI infrastructure startup joins Qualcomm, Arm, Marvell, Amazon, Fujitsu, and MediaTek as NVLink true believers
* ai and ml#### Anthropic reveals fourth likely crime committed by its AIClaude's Felony Bench rap sheet is now as long as OpenAI's

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### Shopify extends lifeline to Tailwind as vibe coding erodes web dev platform's bottom lineAcquisition gives open source CSS framework 'a stable long-term home'
* #### Switzerland tests a FOSS escape route from Microsoft 365Swiss Army sticks a knife in American cloud apps with its own FOSS push
* #### Feel peak Windows was 7? You might like Kumander LinuxDebian and Xfce – solid, sensible choices – with a pretty skin
* #### Canonical shuttering some of its legacy chat channelsThe Ubuntu Pastebin went in June, IRC gets demoted next
* #### Audacity audio-editing app no longer looks like it's from the early 2000sThe FOSS tool for audio editing has a fresh coat of paint, and new features to boot
* #### Haiku OS rises / Beta 6 sails open web / Virtual winds fly fastA real alternative to running some kind of FOSS Unix clone