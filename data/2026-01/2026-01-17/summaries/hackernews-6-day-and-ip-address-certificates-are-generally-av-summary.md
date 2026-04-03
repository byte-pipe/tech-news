---
title: "6-day and IP Address Certificates are Generally Available - Let's Encrypt"
url: https://letsencrypt.org/2026/01/15/6day-and-ip-general-availability
date: 2026-01-17
site: hackernews
model: llama3.2:1b
summarized_at: 2026-01-17T11:20:19.310771
screenshot: hackernews-6-day-and-ip-address-certificates-are-generally-av.png
---

# 6-day and IP Address Certificates are Generally Available - Let's Encrypt

**6-day and IP Address Certificates are Generally Available**

Let's Encrypt has announced that short-lived IP address certificates are now generally available. These certificates have a limited validity period (over six days) versus 90 days for traditional domain-registered certificates.

*   **Security**: Short-lived certificates improve security by requiring more frequent validation, reducing the use of unreliable revocation mechanisms.
*   **Advantages**:
    *   Improved reliability during certificate issuance and renewal
    *   Reduced vulnerability to private key exposure or compromise
    *   Easier transition for organizations with automated renewal processes
*   **Limitations**: Short-lived certificates are opt-in, and the default lifespan will be reduced over time. However, not everyone can adopt this approach, as they may prefer fully automated solutions.

**Key Benefits**

By offering short-lived IP address certificates, Let's Encrypt aims to improve security and reliability in TLS connections. This move also demonstrates a commitment to providing more robust certificate issuance processes, aligning with the evolving digital economy needs.
