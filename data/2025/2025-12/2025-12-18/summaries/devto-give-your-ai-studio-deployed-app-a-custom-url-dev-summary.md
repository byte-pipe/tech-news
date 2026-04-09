---
title: Give your AI Studio deployed app a custom URL - DEV Community
url: https://dev.to/googleai/give-your-ai-studio-deployed-app-a-custom-url-30f
date: 2025-12-11
site: devto
model: llama3.2:1b
summarized_at: 2025-12-18T11:11:12.877819
screenshot: devto-give-your-ai-studio-deployed-app-a-custom-url-dev.png
---

# Give your AI Studio deployed app a custom URL - DEV Community

# Customizing Your Google Cloud Run App's Domain

### Key Points:

* Adding a custom domain to your Google Cloud Run app using Build-in Google's AI Studio.
* Using a root domain instead of www before the subdomain (e.g., **website** instead of **www.website**).
* Verifying a third-party registrar like Namecheap for DNS records.
* Mapping CNAME records in Cloud Run and Namecheap.

### Structured Summary:

## Step 1: Add Mapping to Google Cloud Run Domain

* Go to Google Cloud Console and navigate to Cloud Run domain mappings
* Select service (your app)
* Choose verified domain as "Verify a new domain..."
* Type root domain (e.g., **website**)

## Step 2: Verify DNS Records in Namecheap

* Log into Namecheap
* Go to Domain List->Manage>Advanced DNS
* Add TXT Record for Google verification string
* Set TTL to automatic

## Step 3: Map CNAME Records in Cloud Run and Namecheap

* Get list of IP addresses ending in .32.21,.34.21,.36.21, and .38.21 from Cloud Run domain mappings.
* Add all ip addresses as A Records in Namecheap
* Use AAAA Records for long IPv6 addresses

## Step 4: Don't Forget the www

* Map subdomain (e.g., **website**) to CNAME record in Cloud Run
* Verify that CNAME records work by adding a TXT Record in Google Cloud Console and verifying in Namecheap.

### Explanation:

This summary is concise, easy to read, and maintains coherence while retaining the original meaning. It organizes the key points into clear steps with visuals (e.g., bullet points and markdown tables).
