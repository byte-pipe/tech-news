---
title: 'Abusing .arpa: The TLD That Isn’t Supposed to Host Anything'
url: https://www.infoblox.com/blog/threat-intelligence/abusing-arpa-the-tld-that-isnt-supposed-to-host-anything/
site_name: tldr
content_file: tldr-abusing-arpa-the-tld-that-isnt-supposed-to-host-an
fetched_at: '2026-03-05T06:00:33.198966'
original_url: https://www.infoblox.com/blog/threat-intelligence/abusing-arpa-the-tld-that-isnt-supposed-to-host-anything/
author: Infoblox Threat Intel
date: '2026-03-05'
published_date: '2026-02-26T15:55:47+00:00'
description: The .arpa domain is being abused to host phishing content on domains that should not resolve to an IP address, but do.
tags:
- tldr
---

Phishing email campaigns are so common that it takes something fundamentally different to stand out. We recently found campaigns using a novel, previously unreported method to get around security controls. Actors are abusing the .arpa top-level domain (TLD), in conjunction with IPv6 tunnels, to host phishing content on domains that should not resolve to an IP address. Unlike familiar TLDs like .com and .net, that are used for domains that host web content, the .arpa TLD has aspecial rolein the domain name system (DNS): it’s primarily used to map IP addresses to domains, providing reverse records. Threat actors have discovered a feature in the DNS record management control of certain providers, which allows them to add IP address records for .arpa domains. From there, they can do whatever they like at the hosting provider. It’s a pretty clever trick.

The spam emails in the phishing campaigns we analyzed impersonate major brands and promise a free prize. The messages only display an image, which hides an embedded hyperlink that will take the victim to a malicious website, often through a series of redirects via atraffic distribution system(TDS). The novel feature of this attack is that these image links use a reverse DNS string (used to reverse-map an IP address to a domain name via a PTR record) rather than a standard domain name. For example:

d.d.e.0.6.3.0.0.0.7.4.0.1.0.0.2.ip6.arpa

If the user realized they were being sent to a long domain like this, they would probably be alarmed but in these campaigns the domain is hidden. When the user clicks on the image, the device will resolve the .arpa domain. Because .arpa is a critical TLD for the operation of the internet, these domain names are unlikely to be blocked. From the initial link, the user is typically fingerprinted and redirected tofraudulent content. Figure 1 shows an example of the spam HTML.

Figure 1. An example of the HTML of a phishing email using a reverse DNS string, rather than a standard domain name

To make this attack work, the threat actor acquires some IPv6 address space, for which they are delegated control of the corresponding .arpa subdomain. Then, instead of adding the expected PTR records, they create A records for the reverse DNS names. We have seen threat actors abuse Hurricane Electric and Cloudflare to create these records—both of which have good reputations that actors leverage—and we confirmed that some other DNS providers also allow these configurations. Our tests were not exhaustive, but we notified the providers where we discovered a gap. Figure 2 depicts the process the threat actor used to create the domain used in the phishing emails.

Figure 2. An overview of the process used to abuse the .arpa TLD in phishing emails

The same toolkit used in the .arpa abuse phishing campaign appears to be used by multiple actors since at least 2017. In addition to the .arpa tactic, we have also observed these phishing campaigns using several other methods to bypass security controls, includinghijacking dangling CNAMEsandsubdomain shadowing. Dangling CNAME hijacks are typically DNS records forexpired domainsorabandoned cloud servicesand take advantage of highly reputable organizations. While this blog is focused on introducing the IPv6 / arpa trick, dangling CNAMEs remain a major threat to organizations of all shapes and sizes. For this reason, we’ve included a short section on this topic.

### How .arpa Can Be Abused

The most well-known type of DNS query is the one used to identify the IP address or addresses for a given domain name: the type A query. Conversely, a reverse DNS lookup is performed to identify the domain name or names associated with a given IP address. A reverse DNS domain is built from the IP address. This process involves reversing the bytes of the IPv4 address or nibbles of an IPv6 address and appending a special domain within the .arpa TLD (in-addr.arpa for IPv4 addresses and ip6.arpa for IPv6 addresses).

Figure 3 shows the process the actors used to turn their IPv6 IP address range into a domain they could use in phishing emails. For a normal reverse DNS lookup, the entire IP address is needed to calculate the reverse DNS string. However, since the threat actor operates a /64 range, the last 64 bits of the address can be ignored. To make their reverse DNS domains harder to detect and block, they prepend the domain with a randomly generated subdomain to make each FQDN unique.

Figure 3. The process to create a reverse DNS lookup string of an IPv6 address range and then create a unique FQDN using the string. Green additions are part of the normal process of building an IPv6 reverse DNS domain from an address range and the red addition is made by the actor.

Reverse DNS domains are only intended for internet infrastructure purposes, but DNS can be challenging to implement correctly and there are sometimes unintended behaviors. Figure 4 shows what happened when we performed a type A query on one of the reverse DNS domains in the phishing emails. DNS servers were queried until the authoritative server for the domain was found. In this case, the authoritative name servers were operated by Cloudflare. Using these name servers, the reverse DNS FQDN resolved to two IP addresses. Both IP addresses belonged to Cloudflare’s edge network, which hides the actual host of—in this case—the malicious content. Although reverse DNS domains aren’t supposed to work like this, the threat actors found a way to make it happen.

Figure 4. The series of DNS queries used to resolve an IPv6 reverse DNS domain to an A record of a phishing actor

While the idea of reverse FQDNs may seem straightforward, there are several potential gotchas that need to be addressed for this attack to work properly. It relies on the coordinated abuse of two different services: getting a free IPv6 tunnel and getting name servers that resolve the reverse DNS domain to the owner’s content. The IPv6 tunnel encapsulates IPv6 traffic and sends it over IPv4, but the actor doesn’t need or use the tunnel. It’s simply an easy way to get administrative access to a free IPv6 range. The tunnel isn’t surprising, but the ability to claim ownership of a .arpa domain with a DNS provider is. Given the reserved nature of the .arpa TLD, we wouldn’t expect it to be as easy as entering the domain in a web form. When we evaluated a few DNS providers to check if they were vulnerable, this was the point in the process that was ultimately the determining factor. If the provider prevented us from claiming ownership of a .arpa domain, either by explicitly denying the request or by the request failing, we considered the DNS provider not vulnerable.

### There’s More to the Story

Another notable tactic we have observed in the phishing email hyperlinks is the abuse of subdomains of high-profile, legitimate domains. We found over 100 instances where the threat actor used hijacked CNAMEs of well-known government agencies, universities, telecommunication companies, media organizations, and retailers. Five of the hijacked CNAMEs we observed werepreviously reported in August 2024as being used in phishing attacks. The others appear not to be publicly known. We also saw a few cases of domain shadowing, in which an actor-controlled subdomain is created, typically through credential theft. The lure images are unrelated to the hijacked domains. As with the IPv6 reverse domains, victims are unlikely to ever notice them.

We have observed the same hijacked CNAMEs in phishing emails consistently since September 2025. Some were used in over 100 different emails in a single day. Some (including shadow subdomains) appear to have been abused for years; one shadow subdomain has operated since 2020, seemingly without detection.

Many of the CNAMEs appear to have been hijacked one at a time. There are a few instances, though, where a single domain expiring creates many dangling CNAMEs. Some examples:

* At one point, the domain publicnoticessites[.]com provided public notice content for over 120 different local newspaper websites. When it expired, the threat actor purchased the domain and gained access to all the CNAMEs that referenced the domain, eight of which we observed in phishing emails.
* A similar situation occurred when hobsonsms[.]com expired. The domain provided account services for at least three different universities through the same subdomain account[.]hobsonsms[.]com. Setting up that one subdomain allowed the threat actor to hijack all three.

It isn’t just smaller organizations that have this problem. The domain hyfnrsx1[.]com had subdomains that served as CNAMEs for global food and beverage companies and just recently expired. Hijacked CNAMEs for both companies were observed in phishing emails starting January 2026.

### The Phish Itself

The phishing emails in these campaigns are simple, usually consisting of a hyperlinked lure image. The lure itself frequently promises a “free gift” for completing a survey. Of course they need the victim’s credit card to pay for shipping, but that shouldn’t be much, right? Other lures include claims that an online subscription or service has been interrupted or that the user has exceeded their cloud storage quota. We’ve provided examples of some of the lures in Figure 5.

Figure 5. The phishing emails use a variety of lures to entice users into clicking on the hyperlinked image. The embedded malicious domain is not related to the impersonated brand in the image.

Once victims click on the lure image, they are redirected to one of several TDSs, the exact one depends on the campaign. It initially takes them to a page that analyzes their traffic. If it meets specific criteria, the victim is redirected through a series of domains until they ultimately land on the malicious phishing page. Each domain in the redirection chain performs its own checks and if the victim doesn’t meet the criteria, they will get an HTTP error such asthis, or be redirected to a benign page such as TikTok, as shownhere. We don’t have access to the specific criteria in the various stages of the redirection chain, but we were able to determine that a combination of being on a mobile device and using a residential IP address increased our chances of getting redirected to the malicious landing page.

A final feature of these campaigns was that the hyperlinks in the phishing emails were only active for a short time, usually a few days. After that, any request for the link either displays a generic unsubscribe page such asthis, or generates an error, regardless of traffic type. This limited lifetime makes attempts to replicate the phish during an investigation challenging.

### Why All This Matters

Threat actors are constantly looking for new ways to evade detection, and most techniques are variations on familiar themes. The abuse of the .arpa TLD is novel in that it weaponizes infrastructure that is implicitly trusted and essential for network operations. By using IPv6 reverse DNS domains as malicious links, the threat actor has discovered a delivery mechanism that bypasses security tools. The impact is immediate and cannot be overstated: security that depends on detecting suspicious domains using things like reputation, registration information, and policy blocklists is ineffective for these domains. These domains have an implicitly clean reputation, no registration information, and aren’t usually blocked by policy.

To date we have not observed any queries to these kinds of domains in customer traffic. However, we have observed queries to numerous IPv6 and IPv4 reverse DNS domains, including the ones observed in phishing emails, in our global passive DNS.

The table below provides a selection of the indicators of activity observed in these phishing campaigns. Note, indicators are associated legitimate services and namespaces that have been abused. In all cases, careful consideration should be made before blocking.

For more indicators, visit the Infoblox Threat Intel Github repo:https://github.com/infobloxopen/threat-intelligence.

Indicators

Description

<10 random letters>.5.2.1.6.3.0.0.0.7.4.0.1.0.0.2[.]ip6[.]arpa

IPv6 reverse DNS domain with DGA subdomain

<10 random letters>.1.9.5.0.9.1.0.0.0.7.4.0.1.0.0.2[.]ip6[.]arpa

IPv6 reverse DNS domain with DGA subdomain

<10 random letters>.8.1.9.5.0.9.1.0.0.0.7.4.0.1.0.0.2[.]ip6[.]arpa

IPv6 reverse DNS domain with DGA subdomain

<10 random letters>.9.a.d.0.6.3.0.0.0.7.4.0.1.0.0.2[.]ip6[.]arpa

IPv6 reverse DNS domain with DGA subdomain

<10 random letters>.d.d.e.0.6.3.0.0.0.7.4.0.1.0.0.2[.]ip6[.]arpa

IPv6 reverse DNS domain with DGA subdomain

actinismoleil[.]sbs

Malicious phishing domain

cablecomparison[.]shop

Malicious phishing domain

cheapperfume[.]shop

Malicious phishing domain

drumsticks[.]store

Malicious phishing domain

fightingckmelic[.]makeup

Malicious phishing domain

dulcetoj[.]com

TDS domain

golandof[.]com

TDS domain

politeche[.]com

TDS domain

taktwo[.]com

TDS domain

toindom[.]com

TDS domain

publicnoticessites[.]com

Domain with a subdomain acting as a hijacked CNAME

hobsonsms[.]com

Domain with a subdomain serving as a hijacked CNAME

hyfnrsx1[.]com

Domain with a subdomain acting as a hijacked CNAME



February 26, 2026

Labels:
* Phishing
* reverse DNS
* hijacked CNAME
* scam
* Threat Intelligence
* Cybercrime
* TDS
* threat research
* Threat hunting

#### Infoblox Threat Intel

Infoblox Threat Intel is the leading creator of original DNS threat intelligence, distinguishing itself in a sea of aggregators. What sets us apart? Two things: mad DNS skills and unparalleled visibility. DNS is notoriously tricky to interpret and hunt from, but our deep understanding and unique access to the internet's inner workings allow us to track down threat actors that others can't see. We're proactive, not just defensive, using our insights to disrupt cybercrime where it begins. We also believe in sharing knowledge to support the broader security community by publishing detailed research and releasing indicators on GitHub. In addition, our intel is seamlessly integrated into our Infoblox Protective DNS solutions, so customers automatically get its benefits, along with ridiculously low false positive rates.

View All Posts
