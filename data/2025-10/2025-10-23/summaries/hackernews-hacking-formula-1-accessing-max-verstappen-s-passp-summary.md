---
title: "Hacking Formula 1: Accessing Max Verstappen's passport and PII through FIA bugs"
url: https://ian.sh/fia
date: 2025-10-23
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-23T11:22:44.447746
screenshot: hackernews-hacking-formula-1-accessing-max-verstappen-s-passp.png
---

# Hacking Formula 1: Accessing Max Verstappen's passport and PII through FIA bugs

Here is a concise and informative summary of the article:

## Hacking Formula 1: Accessing Driver Sensitive Information

**Introduction**

* The FIA Super Licence, issued to drivers competing in Formula 1, requires annual renewal through a driver's national motorsport authority (ASN).
* To access driver sensitive information, it is necessary to use public HTTP requests.

**Finding Driver Licenses and Categorization**

* Drivers can apply for a new driver license or categorization on the FIA portal.
* A simple HTTP PUT request can be used to update an existing user profile.
* The response contains additional attributes with extra values, making analysis difficult.

## Key Points

* To access a driver's passport information, including their nationality and filters, requires public exposure of sensitive server resources.
* Accessing driver personal data through the FIA portal may compromise security features implemented for driver protection.
* The system is only accessible through specific API endpoints and uses standard HTTP requests.
