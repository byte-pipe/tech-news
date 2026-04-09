---
title: How I Reverse Engineered a Billion-Dollar Legal AI Tool and Found 100k+ Confidential Files | Alex Schapiro
url: https://alexschapiro.com/security/vulnerability/2025/12/02/filevine-api-100k
date: 2025-12-04
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-04T11:18:00.477709
screenshot: hackernews-how-i-reverse-engineered-a-billion-dollar-legal-ai.png
---

# How I Reverse Engineered a Billion-Dollar Legal AI Tool and Found 100k+ Confidential Files | Alex Schapiro

# Summary of Hacker News Post: Reverse Engineering a Billion-Dollar Legal AI Tool

## Timeline and Responsible Disclosure

*   Initial Contact: Discovers vulnerability in Filevine's security team via email on October 27, 2025.
*   Security Team Thanked and Reviewed Vulnerability
*   Verified Fix via Follow-up Email from November 20, 2025
*   Published Technical Blog Post on December 3, 2025

## Key Points

*   The author uses subdomain enumeration to test Filevine's demo environment without logging in.
*   Finds a custom endpoint "/dxxxxxx9.execute-api.us-west-2.amazonaws.com/prod/recommend" that can be tested with a constructed payload.

## Implications and Analysis

*   Potential security risks if not handled properly: unauthorized access to confidential information if the vulnerability is exploited.
*   The author's ability to reverse-engineer the API suggests a strong security posture, but improper disclosure could have consequences.

## Conclusion

The post provides insight into how Filevine's demo environment can be accessed directly, highlighting the importance of responsible disclosure in software development and the need for robust testing and security measures in place for high-security applications like AI tools.
