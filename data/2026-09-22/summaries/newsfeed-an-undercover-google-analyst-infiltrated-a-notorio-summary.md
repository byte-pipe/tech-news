---
title: An undercover Google analyst infiltrated a notorious supply-chain hacking gang
url: https://arstechnica.com/security/2026/09/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/
date: 2026-09-20
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-09-22T08:46:59.647156
---

# An undercover Google analyst infiltrated a notorious supply-chain hacking gang

# Summary of “An undercover Google analyst infiltrated a notorious supply-chain hacking gang”

## Background on TeamPCP  
- TeamPCP emerged online in late 2025 and launched a massive supply‑chain hacking campaign that compromised hundreds of open‑source projects.  
- The group stole developer credentials, injected malware into widely used tools, and used a Dune‑themed self‑spreading worm (Mini Shai‑Hulud) to automate attacks.  
- Victims included the open‑source scanner Trivy, AI API tool LiteLLM, Checkmarx, TanStack, Mistral AI, GitHub, Mercor, OpenAI, the European Commission and many others.  
- Despite stealing over half a million credentials, the gang generated only tens of thousands of dollars in extortion revenue.

## Google’s undercover operation  
- Mandiant, Google’s security subsidiary, placed an undercover analyst inside TeamPCP’s core chat channel “CanisterWorm” almost from the start of the public campaign.  
- The analyst was granted access to a server storing the gang’s trove of stolen usernames, passwords and access tokens.  
- Google used this position to monitor internal communications, track operational‑security mistakes, and collect intelligence on the group’s activities.

## Disruption and victim protection  
- Rather than notifying each compromised organization individually, Google first contacted cloud providers (e.g., AWS, Microsoft) to revoke the stolen credentials, preventing further exploitation.  
- Hundreds of notification emails were sent to providers and affected victims, prompting rapid responses.  
- Through the internal chat, Google learned that a group member was using an AI tool to develop a zero‑day exploit against a popular login platform’s two‑factor authentication. Google obtained the exploit code, verified its functionality, and alerted the software vendor, leading to a patch.  

## Internal betrayals and sloppy operational security  
- TeamPCP’s poor opsec allowed Google to trace the gang to two Australian members, Ruben Ian Thomson and Louis Michael Gaebler, who were arrested in a joint AFP‑FBI operation.  
- To monetize its credential stash, TeamPCP partnered with other cybercriminal groups, notably ShinyHunters, offering a share of extortion proceeds in exchange for using the data.  
- ShinyHunters later turned rogue, extorting victims with TeamPCP’s credentials while withholding the agreed‑upon cut, and voluntarily shared a full log of its activities with Google’s researcher.  

## Outcomes and significance  
- Google’s early infiltration gave it a unique view of the largest recorded supply‑chain attack campaign, enabling real‑time disruption and the prevention of further compromises.  
- The operation highlighted the potential of undercover cyber‑intelligence work and the risks posed by insecure supply‑chain practices in open‑source ecosystems.  
- The arrests of the two Australian suspects marked a rare successful law‑enforcement response to a sophisticated, multi‑stage supply‑chain hacking operation.