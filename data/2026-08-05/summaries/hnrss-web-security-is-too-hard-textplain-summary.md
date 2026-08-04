---
title: Web Security is Too Hard – text/plain
url: https://textslashplain.com/2026/08/04/security-is-hard-yall/
date: 2026-08-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-05T06:03:04.963604
---

# Web Security is Too Hard – text/plain

# Web Security is Too Hard – text/plain

## Story Overview
- I saw a tweet about a new Cloudflare product and clicked the link.
- The page asked me to claim a handle and sign in with my existing Cloudflare account.
- After signing in, I was prompted to authorize a new feature on a `cloudflare.pay` domain.
- The request looked like a consent‑phishing attack, especially because the domain was outside the trusted `cloudflare.com` space and the green check‑mark seemed suspicious.

## Issues Encountered
- The permission page did not follow best practices (no “Report suspicious request” link).
- The AI chat assistant on Cloudflare’s site asked for full account access before answering my question, violating the principle of least privilege.
- After reporting the suspected phish, I received no response and the experience felt like a dead‑end.
- Eventually I discovered the page was a legitimate new Cloudflare feature, but its design made it look malicious.
- The green check‑mark was actually a hover‑over security UI element, poorly placed.
- Reporting the issue via HackerOne was hindered by a broken CAPTCHA.

## Lessons
- **For developers**  
  - Host applications and content under a trusted domain (e.g., `cloudflare.com/pay` or `pay.cloudflare.com`).  
  - If a new domain is needed, link to it from a page on the trusted domain.  
  - Display security information clearly where users make security decisions.  
  - Provide an obvious, in‑context way to report scams or suspicious requests.  
  - Test security‑reporting flows to ensure they are monitored and functional.  

- **For users**  
  - Think before clicking links, especially when urgency is implied.  
  - If unsure, pause and verify the URL and site authenticity.  

- **For security professionals**  
  - Avoid blaming victims; recognize the difficulty of distinguishing legitimate from malicious sites.

## Author Information
- Eric (username @ericlaw) – impatient optimist, dad, author/speaker.  
- Created Fiddler & SlickRun.  
- Former PM at Microsoft (2001‑2012, 2018‑present) working on Office, IE, Edge, now Microsoft Defender.  
- Opinions are personal and not representative of any organization.