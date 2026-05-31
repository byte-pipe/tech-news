---
title: Glassworm botnet disrupted after resilient C2 infrastructure takedown
url: https://www.bleepingcomputer.com/news/security/glassworm-botnet-disrupted-after-resilient-c2-infrastructure-takedown/
site_name: tldr
content_file: tldr-glassworm-botnet-disrupted-after-resilient-c2-infr
fetched_at: '2026-05-31T11:34:55.829764'
original_url: https://www.bleepingcomputer.com/news/security/glassworm-botnet-disrupted-after-resilient-c2-infrastructure-takedown/
date: '2026-05-31'
description: The Glassworm botnet targeting developers in software supply-chain attacks has been disrupted after researchers took down its resilient command-and-control infrastructure relying on Solana blockchain transactions and the BitTorrent DHT network.
tags:
- tldr
---

# Glassworm botnet disrupted after resilient C2 infrastructure takedown

 By 

###### Ionut Ilascu

* May 27, 2026
* 09:28 AM
* 0

The Glassworm botnet targeting developers in software supply-chain attacks has been disrupted after researchers took down its resilient command-and-control infrastructure relying on Solana blockchain transactions and the BitTorrent DHT network.

​In a coordinated operation conducted  yesterday, CrowdStrike, Google, and The Shadowserver Foundation cut off the botnet operators’ access to four distinct command-and-control (C2) channels designed to resist conventional disruption efforts.

Glassworm campaigns have beenongoing since October 2025and initially targeted developers with malicious OpenVSX and Microsoft VS Code extensions that stole cryptocurrency wallets and developer credentials.

Later attack waves extended to GitHub repositories and npm packages, with one campaign in Marchimpacting more than 400 software artifacts.

In a more recent attack, Glassworm operators planteddozens of dormant extensions on OpenVSXthat would activate the malicious component after an update.

One reason the Glassworm threat has survived this long is its C2 infrastructure, which relies on non-traditional communication channels that are difficult to take down.

“The combination of blockchain, peer-to-peer, and legitimate web services as resolution layers was designed to be resilient against takedowns — a dynamic front protecting the actual C2 servers behind multiple layers of indirection,”CrowdStrike notes.

The researchers say that “Glassworm's operators built their infrastructure for resilience,” and taking down the botnet required hitting the four C2 channels simultaneously:

1. Solana blockchain: C2 server addresses are encoded in the memo fields of blockchain transactions, creating an immutable, publicly accessible dead drop that cannot be taken offline by conventional means.
2. BitTorrent Distributed Hash Table (DHT): The GlasswormRAT queries the BitTorrent peer-to-peer network for configuration data stored against hardcoded public keys, leveraging a global decentralized network with no single point of failure.
3. Public calendar service: Glassworm uses Google Calendar event titles as dead-drop locations for Base64-encoded C2 paths.
4. Direct server connections: Traditional C2 infrastructure hosted on commercial VPS providers served as the final payload delivery mechanism.

Glassworm command-and-control architecture
source: CrowdStrike

​Because of this architecture, disrupting a single channel would have little impact on the Glassworm operation, as communications could shift to another channel, allowing the threat actor to maintain control.

“All four channels had to be disrupted simultaneously in a coordinated effort. As a result, infected machines can no longer receive new instructions or payloads,” CrowdStrike says.

Following the disruption, all machines compromised in a Glassworm attack are beaconing to the IP address 164.92.88[.]210 operated by CrowdStrike.

Organizations are advised to look for this network indicator and take immediate remediation action. Additionally, the researchers have published YARA rules to confirm infections on suspected hosts.

## The Validation Gap: Automated Pentesting Answers One Question. You Need Six.

Automated pentesting tools deliver real value, but they were built to answer one question: can an attacker move through the network? They were not built to test whether your controls block threats, your detection rules fire, or your cloud configs hold.

This guide covers the 6 surfaces you actually need to validate.

Download Now

### Related Articles:

Charter Communications data breach affects 4.9 million accounts

FBI warns of in-person data theft attacks from extortion gang

7-Eleven confirms data breach claimed by the ShinyHunters gang

GitHub confirms breach of 3,800 repos via malicious VSCode extension

Inside a Crypto Drainer: How to Spot it Before it Empties Your Wallet