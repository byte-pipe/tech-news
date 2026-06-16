---
title: A backdoor in a LinkedIn job offer - Roman Imankulov
url: https://roman.pt/posts/linkedin-backdoor/
date: 2026-06-15
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-06-16T12:47:52.844398
---

# A backdoor in a LinkedIn job offer - Roman Imankulov

# A Backdoor in a LinkedIn Job Offer: A Story of Identity Theft and Exploitation

## Introduction

An author obtained an email from a recruiter at a small crypto startup, requesting a review of the codebase publicly available on GitHub. Instead of cloning and installing dependencies to create a test environment, the author spun up a throwaway VPS on Hetzner, cloned the repository, and pointed it in read-only mode. The agent was tasked with reviewing the codebase, but the author spotted suspicious hints that indicated a potential backdoor.

## The Backdoor

The reprompted repo appeared to be a React frontend with a Node backend. However, key details stood out:

*   A malicious URL assembled from fragments:
    *   Protocol: "https"
    *   Domain: "store"
    *   Separator: "//"
    *   Path: "/"
    *   Token: "77"
    *   Subdomain: "rest-icon-handler"
    *   Browser token: "logo"

*   The payload executed on app/index.js, which received server-generated data.

The issue was that a commented-out test ran code with an incoming URL.

## Identity Theft and Exploitation

*   The author suspected the backdoor could be used as a malicious injection vector in future reviews or projects.
*   The fact that multiple developers contributed to this commit history raises concerns about attribution and ownership.
*   An investigation into the incident revealed several red flags:
    *   A fake GitHub repository with 39 commits attributed to "a real developer."
    *   Numerous suspicious URLs, including HTTPS://rest-icon-handler.store/icons/77.

The discovery of a backdoor in a LinkedIn job offer highlights the importance of verifying identities and ensuring that contributors are legitimate. It also underscores the need for additional security measures when interacting with public codebases.