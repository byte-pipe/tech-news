---
title: 333 Tor exit nodes hijacked to intercept SSH traffic and retrieve plaintext email - Ars Technica
url: https://arstechnica.com/information-technology/2026/10/300-tor-exit-nodes-hijacked-to-intercept-ssh-traffic-and-retrieve-plaintext-email/
date: 2026-10-22
site: newsfeed
model: llama3.2:1b
summarized_at: 2026-10-22T16:07:14.653805
---

# 333 Tor exit nodes hijacked to intercept SSH traffic and retrieve plaintext email - Ars Technica

**Tor Exit Node Hijacking and SSH Interception**

* Hackers compromised over 300 Tor exit nodes, reconfiguring them to intercept SSH traffic and redirect unencrypted email connections.
* The hijacking began in late August and continued until mid-October, with 333 exit nodes involved.
* The attackers used a valid password stored in a Tor management server to gain access and reconfigure settings.
* They installed the backdoor Ebury, written for Linux, on several servers, including Switzerland2, a Tor server controlled by the attackers.
* The attackers redirected SSH traffic from Switzerland2 to an interceptor server, and also blocked ports for encrypted email connections.

**Key Details and Investigations**

* Investigators found that the attackers changed the SSH host key without identifying any reasons behind their decision.
* The attackers used Tor volunteers' warnings that the SSH host key had changed to their advantage, directing users with the new key to an interceptor server.
* The hijacking is still not fully understood, with some questions remaining about the attackers' identity and motivations.

**Technical Aspects**

* The attackers used a combination of Ebury and a modified RSA key to intercept and redirect traffic.
* The use of a valid password stored in the Tor management server facilitated the attackers' initial access.
* The attackers' installation of Ebury on several servers, including Switzerland2, allowed them to expand their control over the Tor network.