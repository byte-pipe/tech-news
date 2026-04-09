---
title: "\"Super secure\" MAGA-themed messaging app leaks everyone's phone number :: Eric Daigle"
url: https://ericdaigle.ca/posts/super-secure-maga-messaging-app-leaks-everyones-phone-number/
date: 2025-12-15
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-16T11:12:08.558715
screenshot: hackernews_api-super-secure-maga-themed-messaging-app-leaks-every.png
---

# "Super secure" MAGA-themed messaging app leaks everyone's phone number :: Eric Daigle

# “Super secure” MAGA-themed messaging app leaks everyone's phone number

**Background**

In 2023, a new messaging app called Converso was launched claiming to implement state-of-the-art end-to-end encryption and collect no metadata. However, security researcher crnković discovered that these claims were false.

**Key Findings**

* The app collects a vast amount of metadata on every message
* Uses third-party E2EE provider for server storage
* Implements flawed Seald E2EE service
* Uploads encrypted messages to an open Firebase bucket

**Consequences and Response**

The discovery led to the app's initial release, then withdrawal from App Store and Google Play, claiming to address issues. However:

* CEO Tanner Haas took a break, seemingly responding poorly to crnković's responsible disclosure
* Responded with vague legal threats and accusations of being a Signal shill

**Update on Converso's Status**

Despite the initial setback, Converso rebranded its blog post, emphasizing valuable lessons learned, such as "accept criticism" and "ensure product is thoroughly tested."
