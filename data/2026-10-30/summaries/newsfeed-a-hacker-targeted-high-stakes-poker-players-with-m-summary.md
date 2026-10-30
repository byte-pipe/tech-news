---
title: A Hacker Targeted High-Stakes Poker Players With Malware That Exposed Their Cards | WIRED
url: https://www.wired.com/story/a-hacker-targeted-high-stakes-poker-players-with-malware-that-exposed-their-cards/
date: 2026-10-29
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-10-30T12:47:42.029891
---

# A Hacker Targeted High-Stakes Poker Players With Malware That Exposed Their Cards | WIRED

# Summary of “A Hacker Targeted High‑Stakes Poker Players With Malware That Exposed Their Cards”

## Overview
- In September 2026 professional poker player “Alex” discovered a hidden program called **MeshAgent** on his computer via his Claude AI assistant.  
- MeshAgent could capture Alex’s screen and control his machine, exposing his cards during online sessions on Americas Cardroom (ACR).  
- The same opponent, “OxOO,” appeared in 10 of the 11 compromised sessions, prompting suspicion of cheating.

## Scope of the Campaign
- Alex’s investigation revealed **hundreds of high‑stakes players** had been infected with the same malware over several years.  
- Reported financial losses total **millions of dollars** across major online poker platforms.  
- Alex’s personal loss was about **$30,000**, but many peers suffered larger losses.

## Historical Context
- Super‑user cheating scandals have plagued online poker before (Absolute Poker, Ultimate Bet, 2013 Finnish laptop case, Mike Postle 2018‑19).  
- After a brief 2023 incident, the industry had not seen a confirmed super‑user breach until this campaign.

## Attack Methodology
- **Initial Access:** Hacker compromised third‑party multi‑table software—**Intuitive Tables** and **Jurojin**—which high‑stakes players use to manage many tables simultaneously.  
- **Supply‑Chain Compromise:**  
  - For Jurojin, the attacker breached the developer’s update server and inserted MeshAgent into automatic updates.  
  - For Intuitive Tables, the attacker infected the developer’s test machine (running Jurojin), added malicious code before the app was signed and released.  
- **Target Selection:** The malicious app checked the user’s poker username against a hard‑coded list stored on the attacker’s server. Only listed high‑stakes players received the full backdoor; others ran a benign version.  
- **Reconnaissance Phase:** From 2022 onward the hacker performed low‑profile data collection, waiting for an optimal moment to exploit the gathered information.

## Impact on Players
- MeshAgent recorded screen data, allowing the attacker (or collaborators) to see opponents’ cards in real time.  
- The compromised player “OxOO” consistently won against victims, suggesting use of the stolen information.  
- The scheme remained undetected for years because the malicious code was delivered through legitimate software updates, evading antivirus detection.

## Response and Investigation
- Cybersecurity expert **WolfSec** first publicized the MeshAgent scam on September 29, 2026 via X (Twitter).  
- WolfSec notes the attacker’s patience and sophisticated supply‑chain approach differ from typical “hit‑and‑run” financially motivated attacks.  
- The poker community is now questioning the security practices of major sites and the integrity of online poker after the breach.

## Current Status (as of article)
- Early 2025 saw new high‑stakes entrants (e.g., “JackKlompus” on ACR, a player on CoinPoker) potentially exposed to the same threat.  
- Ongoing investigations aim to identify the threat actor, assess the full financial damage, and implement stronger defenses against future supply‑chain compromises.