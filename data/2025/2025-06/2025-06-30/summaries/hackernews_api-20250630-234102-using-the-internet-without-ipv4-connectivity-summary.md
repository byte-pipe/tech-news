---
title: Using the Internet without IPv4 connectivity
url: https://jamesmcm.github.io/blog/no-ipv4/
date: 2025-06-29
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-06-30T23:41:02.269892
---

# Using the Internet without IPv4 connectivity

**Analysis: Using the Internet without IPv4 Connectivity**

As a solo developer, this article highlights a common issue faced by individuals who rely on IPv6 connectivity but have limited access to IPv4 systems. The author's home ISP struggled with NAT (Network Address Translation), causing only a small fraction of websites to become inaccessible.

For those unaware, Network Address Translation (NAT) is a technology that allows multiple devices on the same network to share one public IP address. This can alleviate the issue of device sharing and reduce the need for private addresses, making it possible to use IPv6.

**Market Indicators:**

* A few days ago, the author's ISP broke IPv4 connectivity, resulting in limited access to online services.
* Despite the availability of Hetzner VPS servers with multiple IPv4 and IPv6 addresses, they became inaccessible due to NAT issues.

**Technical Feasibility for a Solo Developer:**

* Linux is an open-source operating system that can be easily modified to support IPv6.
* WireGuard is a modern internet protocol called "Guard" which has excellent support for IPv6.
* Hetzner offers VPS hosting, allowing solo developers to have multiple addresses (IPv4 and/or IPv6) at their disposal.

**Business Viability Signals:**

* With several major ISPs having NAT issues, businesses that rely on these systems may be impacted.
* The article mentions the ISP's estimated delay of two days before sending a technician, which might indicate slower processing times for resolving the problem.
* The author mentions being willing to pay for IPv6 connectivity as they have multiple devices and need reliable access to online content.

**Actionable Insights:**

1. **Prioritize**: Focus on IPv4 availability first, then consider IPv6 in your development workflow or hosting infrastructure if it's necessary.
2. **Plan ahead**: If possible, set aside time for IPv6 setup or migrations before a NAT issue arises.
3. **Communicate with your network**: Inform clients about the potential inconvenience and explore alternative solutions like Cloud hosting to mitigate risks associated with NAT issues.

**Actionable Numbers (as per the text):**

* Only a small fraction of websites (5%) became inaccessible due to IPv4 issues
* 1 ISP mentioned that their technicians would take several days to arrive, potentially delaying online access

By understanding the nuances of NAT and its implications for solo developers, businesses can take proactive steps to mitigate risks associated with limited IPv6 availability.
