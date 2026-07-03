---
title: Azure CLI Password Spray Hits at Least 78 Microsoft Accounts in 81M+ Attempts
url: https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html
date: 2026-07-03
site: tldr
model: llama3.2:1b
summarized_at: 2026-07-03T11:58:40.331152
---

# Azure CLI Password Spray Hits at Least 78 Microsoft Accounts in 81M+ Attempts

## Azure CLI Password Spray Hits at Least 78 Microsoft Accounts in 81M+ Attempts

### Overview
Cybersecurity researchers have identified a massive "password spray attack" targeting Microsoft's Azure command-line interface (CLI), compromising dozens of accounts across multiple organizations.

### Key Points

* The attack has made over 81 million login attempts using an IPv6 address range controlled by internet infrastructure provider LSHIY LLC(AS32167) between June 12 and 26.
* At least 78 Microsoft accounts have been compromised, with the majority located in 64 organizations.
* Researchers warn of weaknesses in Conditional Access policies, which have enabled the breach without CAP protections.
* Many impacted organizations had their Conditional Access policies enabled, allowing the attackers to bypass CAP protections.

### Interesting Aspects

* The attack leverages a deprecated OAuth flow called Resource Owner Password Credentials (ROPC) to bypass CAP policies.
* This vulnerability allows attackers to gain unauthorized access to credentials through this flawed authentication mechanism.
* Research firms recommend alternative, more secure methods for handling passwords and authentication.
* The attacks resulted in a high volume of successful logins per day, with some businesses experiencing up to 12 user account compromises.

### Implications

* The ongoing nature of the attack suggests it will continue throughout the year unless mitigated.
* Organizations should take immediate action to address any weaknesses in Conditional Access policies and implement measures to prevent similar attacks in the future.