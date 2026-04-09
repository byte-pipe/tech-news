---
title: New Linux udisks flaw lets attackers get root on major Linux distros
url: https://www.bleepingcomputer.com/news/linux/new-linux-udisks-flaw-lets-attackers-get-root-on-major-linux-distros/
site_name: hackernews_api
fetched_at: '2025-06-24T19:06:28.754989'
original_url: https://www.bleepingcomputer.com/news/linux/new-linux-udisks-flaw-lets-attackers-get-root-on-major-linux-distros/
author: smig0
date: '2025-06-20'
description: Attackers can exploit two newly discovered local privilege escalation (LPE) vulnerabilities to gain root privileges on systems running major Linux distributions.
tags:
- hackernews
- trending
---

# New Linux udisks flaw lets attackers get root on major Linux distros

 By

###### Sergiu Gatlan

* June 18, 2025
* 04:45 AM
* 0

Attackers can exploit two newly discovered local privilege escalation (LPE) vulnerabilities to gain root privileges on systems running major Linux distributions.

The first flaw (tracked asCVE-2025-6018) was found in the configuration of the Pluggable Authentication Modules (PAM) framework on openSUSE Leap 15 and SUSE Linux Enterprise 15, allowing local attackers to gain the privileges of the "allow_active" user.

The other security bug (CVE-2025-6019) was discovered in libblockdev, and it enables an "allow_active" user to gain root permissions via the udisks daemon (a storage management service that runs by default on most Linux distributions).

While successfully abusing the two flaws as part of a "local-to-root" chain exploit can let attackers quickly gain root and completely take over a SUSE system, the libblockdev/udisks flaw is also extremely dangerous on its own.

"Although it nominally requires 'allow_active' privileges, udisks ships by default on almost all Linux distributions, so nearly any system is vulnerable,"saidQualys TRU senior manager Saeed Abbasi.

"Techniques to gain 'allow_active,' including the PAM issue disclosed here, further negate that barrier. An attacker can chain these vulnerabilities for immediate root compromise with minimal effort."

The Qualys Threat Research Unit (TRU), which discovered and reported both flaws, has also developedproof-of-concept exploitsand successfully targeted CVE-2025-6019 to get root privileges on Ubuntu, Debian, Fedora, and openSUSE Leap 15 systems.

## Admins urged to patch immediately

The Qualys Security Advisory team has shared more technical details regarding these two vulnerabilitieshereand linked to security patches in thisOpenwall post.

"Root access enables agent tampering, persistence, and lateral movement, so one unpatched server endangers the whole fleet. Patch both PAM and libblockdev/udisks everywhere to eliminate this path," Abbasi added.

"Given the ubiquity of udisks and the simplicity of the exploit, organizations must treat this as acritical, universal risk and deploy patches without delay."

In recent years, Qualys researchers have discovered several other Linux security vulnerabilities that let attackers hijack unpatched Linux systems, even in default configurations.

Security flaws they discovered include a flaw in Polkit's pkexec component (dubbed PwnKit), one in glibc's ld.so dynamic loader (Looney Tunables), another in the Kernel's filesystem layer (dubbed Sequoia), and one in the Sudo Unix program (akaBaron Samedit).

Shortly after the Looney Tunables flaw was disclosed, proof-of-concept (PoC) exploits werereleased online. One month later, attackersbegan exploiting itto steal cloud service provider (CSP) credentials using Kinsing malware.

Qualys also recentlyfound five LPE vulnerabilitiesintroduced over 10 years ago in the needrestart utility used by default in Ubuntu Linux 21.04 and later.

## Why IT teams are ditching manual patch management

Patching used to mean complex scripts, long hours, and endless fire drills. Not anymore.

In this new guide, Tines breaks down how modern IT orgs are leveling up with automation. Patch faster, reduce overhead, and focus on strategic work -- no complex scripts required.

Get the free guide

### Related Articles:

CISA warns of attackers exploiting Linux flaw with PoC exploit

ASUS Armoury Crate bug lets attackers get Windows admin privileges

Microsoft shares script to restore inetpub folder you shouldn’t delete

Google fixes Android zero-day exploited by Serbian authorities

Microsoft: Windows 'inetpub' folder created by security fix, don’t delete
