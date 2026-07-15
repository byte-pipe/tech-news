---
title: A broken DNSSEC rollover took down .AL. Now 1.1.1.1 tells you when validation is bypassed | The Cloudflare Blog
url: https://blog.cloudflare.com/dnssec-nta-ede-33/
date: 2026-07-16
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-16T03:40:18.361943
---

# A broken DNSSEC rollover took down .AL. Now 1.1.1.1 tells you when validation is bypassed | The Cloudflare Blog

# A broken DNSSEC rollover took down .AL. Now 1.1.1.1 tells you when validation is bypassed

## Incident overview
- On 3 July 2026 the Albanian registry (AKEP) attempted a DNSSEC key rollover for the `.al` TLD.
- The new DNSKEY was published without updating the root’s DS record, causing validation failures for all validating resolvers, including Cloudflare’s 1.1.1.1.
- Every `.al` domain (government, banks, media) became unreachable for users relying on DNSSEC‑validating resolvers.

## Timeline of the breakage
- **14:15 UTC** – New DNSKEY published, old key removed; root DS still points to the old key → validation fails.
- **≈17:00 UTC** – New DNSKEY removed, leaving the zone without any DNSKEY; DS still points to the removed key → continued failures.
- **≈19:15 UTC** – Registry removed the DS record from the root; resolvers stop expecting DNSSEC for `.al`, making the zone unsigned and restoring resolution.
- As of the post‑mortem, `.al` remains unsigned because the DS record has not been re‑added.

## Use of Negative Trust Anchors (NTAs)
- Cloudflare applied an NTA for `.al` at 17:15 UTC, treating the zone as unsigned to avoid SERVFAIL responses.
- The NTA was rolled out to all 1.1.1.1 users, restoring connectivity while DNSSEC validation was bypassed.
- The NTA was removed the following day after the DS record deletion made the zone effectively unsigned.

## Limitations of NTAs
- NTAs silently suspend DNSSEC validation; clients cannot tell from the DNS response whether the answer is cryptographically verified.
- RFC 7646 recommends out‑of‑band disclosure, which requires users to check status pages or other sources.

## Adding transparency with Extended DNS Error (EDE) codes
- RFC 8914 defines EDE codes that can accompany any DNS response.
- Cloudflare co‑authored an Internet‑Draft to introduce a new EDE code (33) that signals the presence of an NTA.
- During the `.al` incident, 1.1.1.1 returned both:
  - **EDE 9 (DNSKEY Missing)** – explains the underlying DNSSEC failure.
  - **EDE 33 (Negative Trust Anchor)** – indicates that the response was served under an NTA.

## Example response
```
$ kdig @1.1.1.1 google.al
;; ->>HEADER<<- opcode: QUERY; status: NOERROR; id: 32848
;; Flags: qr rd ra; QUERY: 1; ANSWER: 1; AUTHORITY: 0; ADDITIONAL: 1
;; EDNS PSEUDOSECTION:
;; Version: 0; flags: ; UDP size: 1232 B; ext-rcode: NOERROR
;; EDE: 9 (DNSKEY Missing): 'no SEP matching the DS found for al.'
;; EDE: 33 (Negative Trust Anchor): 'a Negative Trust Anchor has been applied for this query (see RFC 7646)'
;; ANSWER SECTION:
google.al. 300 IN A 142.251.142.196
```
- The answer is valid, but the two EDE codes make clear that DNSSEC validation was not performed.

## Impact and takeaways
- NTAs provide a pragmatic way to keep domains reachable during DNSSEC outages, at the cost of losing cryptographic guarantees.
- By attaching EDE 33, 1.1.1.1 gives clients immediate visibility that DNSSEC validation was bypassed, eliminating the need for out‑of‑band status checks.
- The approach improves transparency for both end‑users and operators when DNSSEC failures affect entire TLDs.