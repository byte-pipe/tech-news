---
title: "It's always TCP_NODELAY. Every damn time. - Marc's Blog"
url: https://brooker.co.za/blog/2024/05/09/nagle.html
date: 2025-12-23
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-23T11:17:45.605825
screenshot: hackernews-it-s-always-tcp-nodelay-every-damn-time-marc-s-blo.png
---

# It's always TCP_NODELAY. Every damn time. - Marc's Blog

## It's Always TCP_NODELAY. Every Damn Time.

### Understanding the Problem

The article discusses the issue of latency in distributed systems and how setting TCP_NODELAY enables a significant reduction in latency. However, the author questions whether this behavior is necessary given the advancements in networking technology.

### Key Points

* Distributed system builders often struggle with debugging latency issues using TCP_NODELAY.
* The default behavior of TCP_NODELAY has changed over time.
* There's no straightforward explanation for why TCP_NODELAY causes latency increases to 4000%.

### Main Ideas and Solutions

#### What is TCP_NODELAY?

TCP_NODELAY is a socket option that enables the sending of a "noDelay" message instead of waiting for an ACK before sending data. This can significantly reduce latency in distributed systems.

#### Why TCP_NODELAY Causes Latency

The article suggests that TCP_NODELAY causes significant latency increases because it allows new outgoing data to be sent without waiting for acknowledgement from the receiving end, leading to unnecessary network activity and increased latency.

## It's Always TCP_NODELAY. Every Damn Time.

### Analysis ofTCP_NODELAY

In conclusion, the issue of latency in distributed systems is complex, but setting TCP_NODELAY can significantly reduce it. However, this behavior has changed over time, and its necessity depends on various factors such as network architecture and application requirements.

### Next Steps

Further investigation into the causes and implications of TCP_NODELAY reveals a more intricate picture than initially thought. The author recommends exploring alternative solutions to mitigate latency in distributed systems while considering the potential drawbacks of enabling TCP_NODELAY as a default behavior.
