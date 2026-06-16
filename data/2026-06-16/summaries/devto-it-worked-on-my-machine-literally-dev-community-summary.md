---
title: It Worked on My Machine (Literally) - DEV Community
url: https://dev.to/cseeman/it-worked-on-my-machine-literally-4ekn
date: 2026-06-09
site: devto
model: llama3.2:1b
summarized_at: 2026-06-16T12:41:36.824675
---

# It Worked on My Machine (Literally) - DEV Community

**Bot Detection and TLS Handshake Fingerprints on TRMNL Plugin**

* **TRMLN's Current Status and Features**: Displays current read item, book title, and next two books in the to-read pile as the developer.
	+ Main ideas: The development of a small TRMNL plugin, utilizing polling for data retrieval and StoryGraph's lack of public API.
* **Scrying into TRMNL's Security**: Identifies potential security concerns related to fetching read items using poll-based data transmission.
	+ Key points:
		- Polling is selected as the method for transmitting data.
		- The issue lies in accessing StoryGraph's profile pages without a user-provided API key or credentials.
* **Trusting a Non-Destructive Test**: Validates the feasibility of fetching read items using poll-based transmission methods, despite potential security risks.
	+ Main facts: 
		- A full HTTP probe was sent to retrieve a display item on the StoryGraph profile page.
		- The server responded with unexpected headers and content.
* **The Cloudflare Conundrum**: Unravels how the TLS handshake fingerprints were handled by Cloudflare's managed security feature.
	+ Main facts: 
		- The challenge related to secure communication between clients (e.g., web browsers) and servers.
		- A clever workaround was found by spoofing the TLS handshake instead of providing headers or credentials.