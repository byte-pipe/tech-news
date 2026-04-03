---
title: Evolving Git for the next decade [LWN.net]
url: https://lwn.net/SubscriberLink/1057561/bddc1e61152fadf6/
date: 2026-02-15
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-15T06:03:23.531645
---

# Evolving Git for the next decade [LWN.net]

# Evolving Git for the next decade

## Summary of Key Points

* **Git's Ubiquity and Evolution Needs:** Git has become the dominant version control system, but its design from 2005 is no longer fully adequate for the modern software development landscape. It requires evolution rather than a revolution due to its widespread adoption.
* **SHA-256 Transition:** The most visible change is the transition from the insecure SHA-1 hash algorithm to SHA-256. While Git has supported SHA-256 since 2020, ecosystem support from major Git hosting platforms like GitHub is lacking, creating a chicken-and-egg problem. Git will make SHA-256 the default for new repositories in version 3.0 to encourage adoption.
* **Reflog and Packed References:** Git currently stores references as individual files, which becomes inefficient with a large number of references. The upcoming packed-refs feature will address this by storing references in a more compact format. However, this introduces complexities related to file system limitations, such as case-insensitive filenames, and potential computational costs.
* **Call to Action:** The author encourages users to advocate for SHA-256 support in their preferred code forges and to contribute to testing and implementing SHA-256 support in third-party tools.

## Detailed Breakdown

* **Introduction:** Git's dominance in version control is undeniable, but its original design is outdated given the current environment (e.g., increased repository size, CI pipelines).
* **SHA-256:** The SHA-1 hash algorithm is vulnerable to attacks, and the transition to SHA-256 is crucial for security. While Git has the underlying support, widespread adoption is hindered by a lack of support in major Git hosting platforms.
* **Reflog:** The current storage of references as individual files is inefficient for projects with many references. Packed references will improve storage efficiency but introduce challenges related to file system behavior.
* **Future Outlook:** Git 3.0 will default to SHA-256 for new repositories, aiming to drive ecosystem-wide adoption. This transition may involve some difficulties.
* **Community Involvement:** Users are encouraged to actively participate in the transition by advocating for SHA-256 support and contributing to related tools.
