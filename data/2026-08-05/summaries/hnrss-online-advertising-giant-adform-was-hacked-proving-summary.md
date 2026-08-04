---
title: Online advertising giant Adform was hacked, proving once again why ad blockers are necessary
url: https://this.weekinsecurity.com/online-advertising-giant-adform-was-hacked-proving-once-again-why-ad-blockers-are-necessary/
date: 2026-08-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-05T06:02:37.291263
---

# Online advertising giant Adform was hacked, proving once again why ad blockers are necessary

# Online advertising giant Adform was hacked, proving once again why ad blockers are necessary

## Incident overview
- On July 27 2024 Adform began serving ads that contained malicious code.  
- Security researcher Kevin Beaumont first disclosed the breach.  
- Adform’s annual report notes it serves about 1.5 billion ads daily.

## Malicious code mechanics
- The code injected into Adform’s ad‑loading script was altered to run in visitors’ browsers.  
- Every three seconds it overwrote any crypto‑wallet address in the user’s clipboard with an address controlled by the attacker.  
- This forces victims who paste the clipboard contents to send crypto to the hacker’s wallet.

## Impact on users and downstream sites
- Any website that uses Adform (e.g., `example.com`) can inadvertently deliver the crypto‑stealing payload to its visitors.  
- The attack compromises “end‑user devices of downstream websites,” effectively turning ordinary sites into infection vectors.

## Ad‑blocker benefits
- Blocking ads prevents the malicious script from loading, protecting against tracking, surveillance, and malware.  
- The author’s own ad blocker (uBlock Origin on desktop, Filtr/Wipron on iPhone) blocked the entire Adform domain, illustrating practical protection.

## Adform’s response
- Adform confirmed the breach but did not disclose how the initial compromise occurred or the number of affected users.  
- The company is still investigating whether hackers also harvested data about which sites individuals visited.

## Author’s observations
- The author attempted to view Adform’s public statement but was initially blocked by his ad blocker, underscoring the tool’s effectiveness.  
- He urges readers to practice safe browsing and use an ad blocker.

## Newsletter call‑to‑action
- The article is part of the “this week in security” newsletter by Zack Whittaker.  
- Readers are invited to support the newsletter via paid subscriptions (starting at $10/month) or one‑time tips.  
- Links to recent blog posts and subscription information are provided.