---
title: How we pwned X (Twitter), Vercel, Cursor, Discord, and hundreds of companies through a supply-chain attack · GitHub
url: https://gist.github.com/hackermondev/5e2cdc32849405fff6b46957747a2d28
date: 2025-12-18
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-19T11:11:23.434240
screenshot: hackernews_api-how-we-pwned-x-twitter-vercel-cursor-discord-and-h.png
---

# How we pwned X (Twitter), Vercel, Cursor, Discord, and hundreds of companies through a supply-chain attack · GitHub

**Discovering Critical Vulnerabilities: A Supply Chain Attack**
===========================================================

### Introduction

As a high school senior pursuing tech, I recently found myself involved in the supply chain of vulnerabilities on several major companies' platforms. In this writeup, I will share my experiences and provide an overview of the critical vulnerabilities we discovered.

**The Vulnerability**

We found two significant issues with Mintlify's new documentation platform. The first issue was a critical cross-site scripting (XSS) vulnerability that exploited an input validation flaw in their "write" feature. This allowed an attacker to inject malicious JavaScript code into users' accounts, potentially leading to authentication breaches.

*   **Story:**

    My friends and I discovered this vulnerability when we reviewed the updated documentation platform for our AI-powered documentation tool, Mintlify. We were familiar with the API and platform to identify potential vulnerabilities.
*   **Exploitation:**
    An attacker would be able to manipulate user inputs (e.g., login credentials) and inject malicious code into Mintlify's document templates.

**The Vulnerability on Discord**

We also discovered a critical vulnerability on Discord, their developer documentation platform. We found that they used a custom-built documentation framework, which we were not aware of at the time.

*   **Vulnerable Code:**
    Our research revealed a significant flaw in Discord's codebase, specifically in their `discord.py` library, which is used by developers to build chat applications.
*   **Fixes:**
    We identified multiple critical vulnerabilities that could be exploited by attackers. These fixes led to improved security measures and increased transparency around the vulnerability.

**The Vulnerability on Vercel**

Our experience with Mintlify's new documentation platform also prompted us to review Vercel, a popular hosting service for web applications. We discovered an XSS vulnerability in their `render` function, which allowed attackers to inject malicious scripts into user accounts.

*   **Vulnerable Code:**
    Our analysis showed that Vercel's code was lacking sufficient input validation, making it vulnerable to XSS attacks.
*   **Fixes:**
    We worked with the Vercel team to implement secure coding practices and fix these vulnerabilities.

**Conclusion**

Discovering these critical vulnerabilities has significantly improved the security of several companies' platforms. It highlights the importance of keeping up-to-date with the latest development frameworks, APIs, and testing efforts.

### Key Takeaways

*   **Keep an eye on vulnerable codebase**: Regularly review your own codebases to identify potential weaknesses.
*   **Stay informed about new vulnerabilities**: Follow reputable sources to stay ahead of the curve regarding known security issues.
*   **Team up with others**: Share knowledge and expertise when tackling complex vulnerability hunting problems.
