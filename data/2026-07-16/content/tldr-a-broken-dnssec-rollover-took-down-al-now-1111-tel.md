---
title: A broken DNSSEC rollover took down .AL. Now 1.1.1.1 tells you when validation is bypassed | The Cloudflare Blog
url: https://blog.cloudflare.com/dnssec-nta-ede-33/
site_name: tldr
content_file: tldr-a-broken-dnssec-rollover-took-down-al-now-1111-tel
fetched_at: '2026-07-16T03:37:07.178945'
original_url: https://blog.cloudflare.com/dnssec-nta-ede-33/
date: '2026-07-16'
published_date: '2026-07-14T13:00:00.000Z'
description: 'When a failed DNSSEC key rollover took down the .AL TLD, we deployed a Negative Trust Anchor to restore resolution. This time, though, clients didn''t have to take our word for it: 1.1.1.1 returned EDE 33, a new DNS error code that signals directly in the response that DNSSEC validation was bypassed.'
tags:
- tldr
---

On July 3, 2026, the Albanian communications authority (AKEP), the operator of the.alcountry-code top-level domain (TLD) of Albania, attempted a DNSSEC key rollover. Something went wrong, resulting in DNSSEC validation failures. Any validating DNS resolver receiving these signatures was required by the DNSSEC specification to reject them and return errors to clients. That includes1.1.1.1, the public DNS resolver operated by Cloudflare.

The.alTLD is the online home of Albanian government services, banks, and media; it ranks#191 on Cloudflare Radar's TLD ranking. Anyone trying to visit those sites, using a validating resolver, found them unreachable during the incident. The failure had the potential to affect every.aldomain, regardless of where it was hosted or which authoritative nameservers served it.

Just two months earlier, a similar incident struck.de, the TLD of Germany. As we described inour blog post on the incident, our response was to install a Negative Trust Anchor (NTA) for.de, temporarily suspending DNSSEC validation in 1.1.1.1 to keep domains reachable while the registry resolved the issue. We did the same for .al.

NTAs restore resolution, but silently. A client receiving a response served under an NTA has no way to tell, from the response alone, that DNSSEC validation was bypassed, leaving it unable to distinguish a legitimate answer from a spoofed one. For the.alincident, 1.1.1.1 addressed that gap for the first time, returning a new Extended DNS Error (EDE) code alongside every affected response to signal that the answer was not DNSSEC-validated due to the presence of an NTA.

The graph below shows the SERVFAIL and NOERROR rates for.alqueries on 1.1.1.1 throughout July 3. The SERVFAIL rate climbs as cached records expire and resolvers are forced to revalidate. It drops sharply when the NTA is applied at 17:15 UTC, restoring resolution.

### What happened to.al

We discussed how DNSSEC works in more detail inour prior blog post. A brief recap:

DNSSEC builds a chain of trust from the root zone down to individual domain names. The root zone holds a Delegation Signer (DS) record for each signed TLD, a fingerprint of that TLD's DNSKEY. A resolver verifying.alchecks that the DNSKEY served by.al's nameservers matches the DS record in the root. If it does, the resolver trusts that DNS responses from.al's nameservers are authentic. The same pattern repeats one level down:.alholds DS records for its signed child zones, each with a matching DNSKEY. A break anywhere in that chain, such as a DS record pointing to a key that no longer exists, causes validation to fail for everything below it.

Before the incident, the root zone held a DS record matching the DNSKEY served by the.alnameservers, as illustrated below.

At around 14:15 UTC, the.aloperator published a new DNSKEY and stopped serving the old one. The DS record in the root zone still pointed to the old DNSKEY (id=26319), so any resolver attempting to validate.alresponses found no matching key and failed.

At roughly 17:00 UTC, the.aloperator removed the new DNSKEY without restoring the old one. The zone now had no DNSKEY records at all, while the DS record in the root still pointed to id=26319, and resolution continued to fail.

At roughly 19:15 UTC, the.aloperator removed the DS record from the root zone. Without a DS record, resolvers no longer expected DNSSEC validation for.al, and resolution was restored, though the entire TLD was now unsigned.

As of publishing,.alremains unsigned. The DS record has not been restored to the root zone by the.aloperators. Without a DS record, every.aldomain is unable to use DNSSEC protections.

### Why Negative Trust Anchors are used

Having a broken DNSSEC configuration can be painful, especially when it impacts an entire TLD at once. As we covered in our.deincident blog, recursive DNS operators can install a Negative Trust Anchor (NTA) as defined inRFC 7646, which tells a resolver to treat a zone as unsigned and bypass validation. Before installing the NTA, we attempted to reach the.aloperator directly and posted on theDNS-OARC Mattermostto alert the community. We received no response, in part because the operator's contact addresses were themselves under.al, making them unreachable during the outage.

We applied the NTA for.aland rolled it out to all 1.1.1.1 users by 17:15 UTC, roughly three hours after the chain broke.

The tradeoff is the same as it was for.de: a Negative Trust Anchor suspends DNSSEC validation, which means.aldomains were no longer protected against DNS spoofing for the duration. We judged this acceptable for the same reason: the failure was public, confirmed, and affecting every validating resolver equally.

The Negative Trust Anchor was removed the following day, once the.aloperator had removed the DS record from the root zone. With no DS record present, resolvers no longer expected DNSSEC for.aland the NTA was no longer needed.

### The problem with Negative Trust Anchors

Installing a Negative Trust Anchor is an aggressive measure. We suspend DNSSEC validation to keep domains reachable, accepting that responses are no longer cryptographically verified for the duration. Users get answers instead of SERVFAIL, but those answers carry no DNSSEC guarantee.

What makes this harder is that, up until now, nothing in the DNS response signalled this to the client; a response served under an NTA looked identical to a fully validated one. RFC 7646 acknowledges this gap and recommends that operators publicly disclose which NTAs they have in place, but that disclosure is out-of-band. For both the.deand.alincidents we published status pages, but a status page requires the user to go looking. An application, a monitoring tool, or a user querying 1.1.1.1 had no way to tell, from the response alone, that DNSSEC validation was bypassed.

### Bringing transparency to Negative Trust Anchors

Extended DNS Error (EDE) codes, defined inRFC 8914, allow resolvers to include additional context alongside any DNS response, whether that is an error or a successful answer. Babak Farrokhi at Quad9 proposed an Internet-Draft to signal the presence of a Negative Trust Anchor directly in the DNS response, using a new EDE code:Disclosure of Negative Trust Anchors in DNS Responses. We joined as co-authors, and 1.1.1.1 now implements it.

During the.alincident, any query for a.alname returned both the answer and the new EDE code while the Negative Trust Anchor was installed. Here is what that looked like:

$ kdig @1.1.1.1 google.al

;; ->>HEADER<<- opcode: QUERY; status: NOERROR; id: 32848

;; Flags: qr rd ra; QUERY: 1; ANSWER: 1; AUTHORITY: 0; ADDITIONAL: 1

;; EDNS PSEUDOSECTION:

;; Version: 0; flags: ; UDP size: 1232 B; ext-rcode: NOERROR

;; EDE: 9 (DNSKEY Missing): 'no SEP matching the DS found for al.'

;; EDE: 33 (Negative Trust Anchor): 'a Negative Trust Anchor has been applied for this query (see RFC 7646)'

;; ANSWER SECTION:

google.al. 300 IN A 142.251.142.196

The response is a NOERROR with a valid answer:google.alresolves, but two EDE codes accompany it.EDE 9 (DNSKEY Missing)surfaces the underlying DNSSEC failure: the chain of trust was broken and validation failed.EDE 33 (Negative Trust Anchor)signals that 1.1.1.1 applied a Negative Trust Anchor and served the response anyway. Together they give clients and operators full visibility into what happened: the answer is real, but it was not DNSSEC-validated.

1.1.1.1 returns EDE 33 on any response generated while an NTA is active, regardless of whether the query itself would have failed DNSSEC validation. A query for a domain that does not use DNSSEC at all will still carry EDE 33 if it falls under an active NTA. This is intentional: the NTA covers the entire zone, and transparency applies equally to every response served under it. This also resolves an issue we flagged in our.deblog, where 1.1.1.1 incorrectly returnedEDE 22 (No Reachable Authority)instead of surfacing the underlying DNSSEC error. During the.alincident, 1.1.1.1 correctly returnedEDE 9 (DNSKEY Missing)alongside EDE 33.

The Internet-Draft is an individual submission and EDE 33 has beenassigned by the Internet Assigned Numbers Authority (IANA). Thanks to our co-author, Babak Farrokhi at Quad9, thekdigtool from the Knot projectnow recognizes EDE 33 by name, anda pull request for Unboundis under review. We hope other resolver implementations will follow. The Internet-Draft has been submitted to theInternet Engineering Task Force (IETF) DNSOP Working Group, and will be discussed in the DNSOP Working Group at the IETF meeting, taking place in Vienna from July 18 to July 24.

### Closing the gap

TLD-level DNSSEC failures are rare, but when they happen they affect every domain underneath the affected TLD simultaneously, and every validating resolver equally. The.alincident, following closely behind.de, shows that Negative Trust Anchors are a necessary operational tool, but one that has, until now, been invisible to the users they affect.

EDE 33 closes a gap that RFC 7646 left open. A response served under a Negative Trust Anchor now says so directly, giving operators, monitoring tools, and users the information they need to understand what the resolver did and why.

The Internet-Draft is available at theIETF datatracker. If you have thoughts on it, theIETF DNSOP mailing listis the right place to share them.

If you want to learn more about how DNSSEC works, visit our pageHow does DNSSEC work?And you can always follow real-time DNS trends and TLD data onCloudflare Radar.

## Related tags

1.1.1.1
DNS
DNSSEC
Incident Report
Reliability
Standards

Follow on Social Media

* Cloudflare

## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.