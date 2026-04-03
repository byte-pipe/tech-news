---
title: A Botnet Accidentally Destroyed I2P (The Full Story)
url: https://www.sambent.com/a-botnet-accidentally-destroyed-i2p-the-full-story/
site_name: hnrss
content_file: hnrss-a-botnet-accidentally-destroyed-i2p-the-full-story
fetched_at: '2026-02-22T19:11:31.996981'
original_url: https://www.sambent.com/a-botnet-accidentally-destroyed-i2p-the-full-story/
date: '2026-02-22'
published_date: '2026-02-21T21:12:44.000Z'
description: A Botnet Accidentally Destroyed I2P
tags:
- hackernews
- hnrss
---

On February 3, 2026, the I2P anonymity network was flooded with 700,000 hostile nodes in what became one of the most devastating Sybil attacks an anonymity network has ever experienced. The network normally operates with 15,000 to 20,000 active devices. The attackers overwhelmed it by a factor of 39 to 1.For three consecutive years, I2P has been hit with Sybil attacks every February. The 2023 and 2024 attacks used malicious floodfill routers and remain unattributed. When the 2026 attack began, most assumed it was the same state-sponsored operation continuing its annual disruption campaign. The assumption was wrong.The attacker was identified as the Kimwolf botnet, an IoT botnet that infected millions of devices including streaming boxes and consumer routers throughout late 2025. Kimwolf is the same operation behind the record-setting 31.4 terabit per second DDoS attack in December 2025. The operators admitted on Discord they accidentally disrupted I2P while attempting to use the network as backup command-and-control infrastructure after security researchers destroyed over 550 of their primary C2 servers.The I2P development team responded by shipping version 2.11.0 just six days after the attack began. The release includes hybrid ML-KEM plus X25519 post-quantum encryption enabled by default, making I2P one of the first production anonymity networks to ship post-quantum cryptography to all users. Additional Sybil mitigations, SAMv3 API upgrades, and infrastructure improvements were included.
