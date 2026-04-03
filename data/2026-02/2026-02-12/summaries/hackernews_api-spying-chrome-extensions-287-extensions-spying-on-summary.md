---
title: Spying Chrome Extensions: 287 Extensions spying on 37M users
url: https://qcontinuum.substack.com/p/spying-chrome-extensions-287-extensions-495
date: 2026-02-11
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-12T06:02:11.941769
---

# Spying Chrome Extensions: 287 Extensions spying on 37M users

# Spying Chrome Extensions: 287 Extensions spying on 37M users

* A research team developed an automated scanning pipeline to detect Chrome extensions that exfiltrate browsing history.
* The scan identified 287 Chrome extensions with approximately 37.4 million installations, representing roughly 1% of the global Chrome user base.
* The actors behind these leaks include Similarweb, Curly Doggo, Offidocs, Chinese actors, various data brokers, and a group suspected to be an extension of Similarweb called "Big Star Labs."
* The research highlights a persistent issue with browser extensions collecting and selling user data, posing moral and security risks. Users of non-open-source software should assume they are the product.
* The automated scan involved a Docker container with Chrome, a MITM proxy, synthetic browsing workloads, and a regression model to detect a correlation between outbound traffic volume and URL length.
* The leakage ratio, defined as the ratio of bytes sent to the compressed URL length, was used to identify potential data exfiltration. Extensions with a ratio of 1.0 or higher were considered definite leaks.
* Honeypots were set up with specific URLs to attract data brokers, revealing five distinct IP ranges associated with known scraping entities like HashDit, Blocksi AI Web Filter, and Kontera.
* OSINT analysis of the flagged extensions revealed connections between Similarweb extensions and scrapers like Kontera, which are linked to Curly Doggo and Offidocs. "Big Star Labs" is suspected to be an extension of Similarweb.
* The scale of exposure is significant, affecting a population comparable to that of Poland. The threat model includes profiling, targeted advertising, corporate espionage, and credential harvesting.
* Examples of data exfiltration were provided, showing how extensions send URL data to remote servers.

## Key Points:

* **Scale of the Problem:** A significant number of Chrome extensions are actively spying on users, affecting a large portion of the Chrome user base.
* **Persistent Actors:** Known data brokers like Similarweb remain active in collecting and selling user data through these extensions.
* **Automated Detection:** A research pipeline was developed to systematically identify potentially malicious extensions.
* **Data Exfiltration Methods:** Extensions are sending URL data to remote servers, potentially including personal identifiers.
* **Security and Privacy Risks:** This practice poses significant risks to user privacy and security, potentially enabling targeted attacks and corporate espionage.
