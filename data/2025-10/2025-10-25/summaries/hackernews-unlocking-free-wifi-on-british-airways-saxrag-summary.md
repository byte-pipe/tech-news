---
title: Unlocking free WiFi on British Airways | saxrag
url: https://www.saxrag.com/tech/reversing/2025/06/01/BAWiFi.html
date: 2025-10-25
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-25T11:24:15.612956
screenshot: hackernews-unlocking-free-wifi-on-british-airways-saxrag.png
---

# Unlocking free WiFi on British Airways | saxrag

# Unlocking Free WiFi on British Airways: A Summary

**Key Points**

* British Airways offers free WiFi for messaging through its "The British Airways Club"
* The system can be accessed via the captive portal while flying
* To sign up, one must log in and verify their email address implicitly without need for password confirmation (due to lack of internet access at the time)
* The connection is encrypted using TCP connections with specific headers, such as SNI (Server Name Indicator), indicating the domain used for messaging
* Observing the TLS handshake reveals the domain name of websites connected through this system

**Maintenance and Troubleshooting**

* The WiFi network appears to use a set of whitelisted domains controlled by messaging apps
* Whitelisting may be related to SNI or other security measures implemented by airlines
* Some analysts have expressed concern that the lack of VPN usage is visible to internet service providers (ISPs)

**Technical Explanation and Analysis**

* The connection between the client's TCP stack and the server's TLS handshake reveals specific information about the domains involved in the conversation
* Observing the TLS protocol can provide a window into the network traffic during conversations, revealing potential security risks or weaknesses
