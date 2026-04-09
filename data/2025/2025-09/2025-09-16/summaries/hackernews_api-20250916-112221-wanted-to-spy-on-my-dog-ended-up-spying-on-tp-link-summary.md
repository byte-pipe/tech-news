---
title: "Wanted to spy on my dog, ended up spying on TP-Link – Kennedn's Blog"
url: https://kennedn.com/blog/posts/tapo/
date: 2025-09-15
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-09-16T11:22:21.967666
---

# Wanted to spy on my dog, ended up spying on TP-Link – Kennedn's Blog

**Analysis from a Solo Developer Business Perspective**

The author of the article found an opportunity in "reverse-engineering" onboarding flows for their cheap Tapo indoor camera. They discovered that the device's API would accept credentials after onboarding, but only if they were admin levels. However, this led them to consider a cloudless onboarding solution.

**Market Indicators:**

* The problem of poor documentation and lack of support from TP-Link (an established and trustworthy brand in the security camera industry) is not unique.
* The need for a more secure and reliable way to onboard cameras on-boarded by TP-Link is common among businesses that struggle with securing their devices.

**Technical Feasibility:**

* MitM (Man-in-the-Middle) attacks can be effective, but dynamic instrumentation via tools like frida provides an easier and more robust way to achieve this.
* The use of MITMting TLS sessions requires a solid understanding of cryptographic concepts and is relatively complex.

**Business Viability Signals:**

* There are potentially significant revenue opportunities in creating and selling solutions for secure camera onboarding.
* A cloudless onboarding solution could provide a competitive edge over existing solutions.

However, the author notes that "establishing a man-in-the-middle" can be challenging due to the tools used by phone apps (frida) and certificate pinning, which can render such approaches ineffective. The use of mitmproxy for dynamic instrumentation is also mentioned as an alternative method.

**Actionable Insights:**

* Before investing time in building a solution from scratch, consider acquiring the knowledge and experience necessary to tackle similar challenges.
* Building a cloudless onboarding system requires substantial resources (development team, infrastructure, etc.) but can be profitable if done correctly.
* Establishing trust with potential customers is crucial when offering non-cloud-based solutions; providing documentation, support, or proof of concept may help in mitigating the risk.

To extract meaningful information from the article regarding pricing and revenue:

* There's no mention of specific pricing for a cloudless onboarding solution that provides security features for TP-Link cameras.
* However, some details about additional services (e.g., onboarding, support) might be inferred, but this would require further investigation.
* Business model potential:
   - Charge customers directly for onboarding solutions or add revenue streams through consulting
   - Offer subscription-based services that include cloudless onboarding plus other security features

In the context of a solo developer business, consider the following:

* Acquire expertise in camera security and security camera devices to tackle similar challenges.
* Consider acquiring existing tools (like frida) which can save time for integration development.
* Market value for your solution may differ as it's based on TP-Link cameras; be prepared to adapt strategy or market position accordingly.

Example script snippets and relevant technical terms used in the article are included.

```
import logging

def configure_proxy(them, proxies, headers):
    # Update proxy configuration
    logging.info("Configuring proxy for them: {}".format(them))
    logging.info(" proxies added:", proxies)
    logging.info("headers configured:", headers)

# Generate debug console output using mitmproxy
mitmproxy = frida.from_command_line_args(["start"])

def sniff_and_inject(proxy, method):
    # Create HTTP requests with injected data
    data = {"username": "admin", "password": "some secret value"}
    request = proxy.request(method, 'https://example.com', headers={"Content-Type": "application/json"}, body=data)
```

**Best Practices:**
-
This is a significant challenge of developing the solution. However, with more technical resources (development team, infrastructure), it can be accomplished. For a solo developer, acquiring knowledge relevant to this challenge may help improve project development time or save time by leveraging pre-existing solutions.

The next step for the author would likely involve:

- Documenting their process in detail
- Reaching out to TP-Link and potential customers (industrial security audience) to discuss business plans
  * Building a reputation with them through marketing efforts, support services or consulting projects.
