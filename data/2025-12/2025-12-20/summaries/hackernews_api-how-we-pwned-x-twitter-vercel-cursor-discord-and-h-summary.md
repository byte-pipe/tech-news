---
title: How we pwned X (Twitter), Vercel, Cursor, Discord, and hundreds of companies through a supply-chain attack · GitHub
url: https://gist.github.com/hackermondev/5e2cdc32849405fff6b46957747a2d28
date: 2025-12-18
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-20T11:12:50.871096
screenshot: hackernews_api-how-we-pwned-x-twitter-vercel-cursor-discord-and-h.png
---

# How we pwned X (Twitter), Vercel, Cursor, Discord, and hundreds of companies through a supply-chain attack · GitHub

## How We Pwned X: A Supply Chain Attack on Multiple Companies

### Introduction

In this article, we will reveal a supply chain attack that allowed us to compromise the integrity of multiple high-profile companies through a cross-site scripting vulnerability.

### Vulnerabilities Exploited

*   **Mintlify:** Found critical cross-site scripting vulnerabilities in its AI-powered documentation platform used by top companies like Twitter and Vercel.
*   **Discord:** Discovered a new update that switched to an AI-powered documentation platform, but did not provide adequate security measures.

### Our Story

Our story begins with the discovery of a critically vulnerable custom-built documentation platform being switched out for an AI-powered framework. As a seasoned hacker and advocate for bug bounty programs, I took it upon myself to review the update from top to bottom to identify potential issues.

On Friday, November 7, 2025, Discord announced a new update to their developer documentation platform. We immediately began poking around and identified a critical cross-site scripting vulnerability in the process. As someone familiar with Discord's API and platform, we were excited to test our skills

### The Attack

Our attack exploited several vulnerabilities to compromise multiple companies' integrity:

*   **Mintlify:**

    *   Found a critical cross-site scripting vulnerability that, if abused, would allow an attacker to inject malicious scripts into the documentation of numerous companies.
*   **Discord:**

    *   Discovered a new update that switched to an AI-powered framework but did not provide adequate security measures.

### Conclusion

Our exploit allows us to compromise multiple high-profile companies by compromising the integrity of their AI-powered documentation platforms. This is just another example of how hackers use supply chain attacks to undermine organizations' security posture.
