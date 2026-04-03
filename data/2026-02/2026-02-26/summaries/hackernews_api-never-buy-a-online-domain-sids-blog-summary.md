---
title: "Never Buy A .online Domain | Sid's Blog"
url: https://www.0xsid.com/blog/online-tld-is-pain
date: 2026-02-26
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-26T06:02:30.429660
---

# Never Buy A .online Domain | Sid's Blog

# Never Buy A .online Domain | Sid's Blog

This blog post details the author's negative experience after purchasing a .online domain for a small project, highlighting the difficulties encountered with Google's Safe Browsing and the registrar, Radix.

## Namecheap's Al alluring Offer

The author took advantage of a Namecheap promotion offering a free .online or .site domain per account for a small, personal project, paying a minimal $0.20 for ICANN fees. The site was set up using ClouDFlare and GitHub.

## The Disappearing Act

Weeks after the purchase, the author noticed no traffic to the site. Attempting to access it resulted in a "This is an unsafe site" warning in both Firefox and Chrome. The site contained a link to the App Store, screenshots, and brief text about the app, with no potentially harmful content. Subsequent attempts to access the site led to a "site not found" error.

## Initial Recon

Initial checks revealed that ClouDFlare was active and pointing to the domain, and the domain status was correct on Namecheap with the proper expiration date and correct nameservers. However, a NS lookup showed no results, and WHOIS information indicated a "serverHold" status.

## Stuck in No-Man’s-Land

Contacting Namecheap revealed the serverHold status. The author then contacted Radix, the registrar, who confirmed the serverHold. The author faced a verification catch-22: Google Search Console verification requires a DNS TXT or CNAME record, which is impossible for a non-resolving domain. Radix wouldn't reactivate the domain without Google removing the flag, and Google wouldn't remove the flag without domain ownership verification.

## A Series of Unfortunate Events

The author reflects on several mistakes made: buying a non-standard TLD (.online), not immediately adding the domain to Google Search Console, and not implementing uptime observability. The author criticizes both Radix and Google for their strict policies and lack of grace periods for resolving issues.

## Notes

The post includes notes defining "serverHold" and "clientHold" statuses and provides a link to a mirror of the site for verification.
