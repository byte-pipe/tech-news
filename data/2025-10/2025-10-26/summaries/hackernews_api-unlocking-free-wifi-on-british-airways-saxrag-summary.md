---
title: Unlocking free WiFi on British Airways | saxrag
url: https://www.saxrag.com/tech/reversing/2025/06/01/BAWiFi.html
date: 2025-10-24
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-26T11:24:18.463435
screenshot: hackernews_api-unlocking-free-wifi-on-british-airways-saxrag.png
---

# Unlocking free WiFi on British Airways | saxrag

**Unlocking Free WiFi on British Airways: Key Discoveries and Insights**

### Main Point 1:

British Airways offers free WiFi to members of their frequent flyer program, **The British Airways Club**, as a promotional offer. However, this may come with some surprises when accessing popular messaging apps.

### Key Points:

- The WiFi provides basic internet access during flights, including texting.
- The captive portal prompts the user to "Start session" and invites conversations via WhatsApp, Signal, Wechat, or Discord.
- The provider uses TCP bandwidth/capacity, which may differ depending on app usage, as suggested by testing with example.com and wireshark.
- Notably, **SNI (Sender Name Index)** reveals a domain name, allowing any entity to access the internet regardless of their intentions.

### Interesting Findings:

* The SNI feature allows for exposure of connected websites before the TLS handshake is established.
* The WiFi provider likely uses whitelisted domains or default settings when connecting users to messaging apps in **The British Airways Club**.
* The user's experience highlights the importance of internet security and awareness, especially during airline flights.

### Takeaways:

- Be cautious when accessing untrusted networks and services in public.
- Recognize that even seemingly innocuous internet connections can compromise your online safety.
- The **British Airways WiFi offering may be an attractive option for frequent flyers; however, understanding its implications is essential.
