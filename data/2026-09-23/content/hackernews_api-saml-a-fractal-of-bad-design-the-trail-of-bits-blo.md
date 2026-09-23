---
title: 'SAML: A fractal of bad design - The Trail of Bits Blog'
url: https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/
site_name: hackernews_api
content_file: hackernews_api-saml-a-fractal-of-bad-design-the-trail-of-bits-blo
fetched_at: '2026-09-23T15:19:23.471491'
original_url: https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/
author: aray07
date: '2026-09-22'
published_date: '2026-09-21T07:00:00-04:00'
description: SAML, the XML-based authentication protocol that birthed the SSO industry, is fundamentally flawed due to XML complexity, canonicalization issues, enveloped signatures, and design ossification, making it vulnerable to signature wrapping attacks and parser differentials that persist despite decades of awareness. Organizations should migrate to OpenID Connect (OIDC), which avoids these pitfalls through simpler JSON-based design, detached signatures, and agile evolution.
tags:
- hackernews
- trending
---

Page content

Born out of academia and raised in corporate IT departments, the Security Assertion Markup Language (SAML) authentication protocol continues to be a staple in these organizations. However, it’s time for it to retire. With the rise of software-as-a-service (SaaS) companies in the late aughts, IT departments needed a way for users to authenticate to many new web services. SAML and the burgeoning single sign-on (SSO) industry fulfilled this need. However, SAML is being crushed under the weight of its own complexity. It’s time to deprecate it and move on to modern alternatives like OpenID Connect (OIDC). In this post, I will explore the design-by-committee origin of SAML, its progression through the ranks in academic and corporate environments, its slow disintegration at the hands of the security research community, and its (hopeful) deprecation in favor of newer protocols.

SAML 101

What’s insidious about SAML is that it really is mostly straightforward to understand, but it’s built on a foundation of sand, bone dust, and ash; it works … if you assume XML signature validation is reliable. But XML signature validation is deeply cursed, and is so complicated that most fielded SAML implementations are wrapping libxmlsec, a gnarly C codebase nobody reads.—Thomas Ptacek, 2023

## SAML and the birth of the SSO industry

Wikipedia tells methat “SAML is an XML-based markup language for security assertions.” It was created in 2002 by the Organization for the Advancement of Structured Information Standards (OASIS) Security Services Technical Committee (SSTC). Okay, we’re not off to a great start by modern standards. XML, despite having some redeeming qualities, is quite complex compared to newer alternatives like JSON, but we’ll get more into that later. Further, a committee of subcommittees having meetings is a recipe for “kitchen-sink” protocol design (e.g.,waterfall methodology,big design up front, etc.). And sure enough, we’ve now jammed four (!) XML-based security protocols into one:

… the following intellectual property was contributed to the SSTC:

* Security Services Markup Language (S2ML) from Netegrity
* AuthXML from Securant
* XML Trust Assertion Service Specification (X-TASS) from VeriSign
* Information Technology Markup Language (ITML) from Jamcracker

—SAML: History

However, the desire for such a protocol was undeniable. As the internet shifted from Web 1.0 in the 90s to Web 2.0 in the early aughts, users and organizations needed an easy way to authenticate to many new web services. Academia was the biggest driver of this movement, although not the only one: Central Authentication Service (CAS) in 2002 at Yale, Shibboleth IdP in 2003 by Internet2, a consortium of research universities (including my alma mater), ADFS in 2003 by Microsoft, and simpleSAMLphparound 2007by Uninett, a state-owned Norwegian company with close ties to academia. All these authentication projects eventually supported SAML in one way or another. Like ARPANET before it, universities were at the forefront of internet development and were the earliest consumers of web services. Once this base layer of protocol availability and nascent academic proving ground was established, the commercial industry took it and ran toward a multibillion dollar industry.

The SSO, identity, and authentication provider industry was also starting up in the early aughts, but really came to fruition a few years later: Ping Identity (2002), OneLogin (2009), Okta (2009), and Duo Security (2010). These companies were essentially built on the SAML protocol with the exception of Duo, who would introduce their first SSO product in 2015, which is where I come into the story. I worked on Duo’s firston-premises Access Gateway product(DAG), which was built on simpleSAMLphp and, obviously, the SAML protocol. It’s where I became intimately familiar with the SAML protocol and spent many years of my life digesting its lengthy specifications. I was there whenKelby Ludwigfound theXML comment bypass, but we will get into various attacks and SAML deficiencies later. Suffice it to say, the SSO and authentication provider industry was booming, and much of it was built on the SAML protocol.

## A crack in the armor

XML signature wrapping (XSW) attacks are the proverbial arrow to SAML’s heel. While there was earlier security research into both signature wrapping (2005,2008, and2009) and SAML (2008), I consider the godfather of it all to be “On Breaking SAML: Be Whoever You Want to Be” (2012). It tested theory against practice and resulted inan automated wayto check for XSW attacks. This was our north star when implementing the DAG. It was the reason we chose simpleSAMLphp as our building block. PHP,especially at the time, was not exactly known for its security track record, but simpleSAMLphp’s spoke for itself. simpleSAMLphp was resilient to XSW at a time when nobody really knew what that was:

simpleSAMLphp’s security track record (credit: On Breaking SAML)

Despite being front and center in this 2012 paper, XSW isstill present today. If we know the bug class, then why can’t we fix it? But before we get into SAML’s flaws we first have to consider the shaky ground it was built upon: XML.

XML is no slouch when it comes to a (lack of) security track record.These bug classeswould have been more familiar to a developer in the 90s, but nonetheless are still present in XML today: XXE, entity expansion (“billion laughs”), DTD retrieval (SSRF), XPath/XQuery/XInclude/XSLT/CDATA injection, and more. A SAML library needs to handle all these bug classes before even getting to the actual SAML functionality.

In addition to security bug classes, there’s also the sheer complexity of XML when compared against something like JSON. In XML you have tags, elements, attributes, comments, namespaces, markup versus content, schemas, CDATA, DOCTYPEs, and more. In JSON, you essentially have keys, values, objects, and lists. Complexity is generally at odds with security, and this is one reason I consider SAML to be a fractal of bad design.

## A fractal of bad design

SAML provides ample opportunity to learn about protocol design. In this section, I will cover five flaws that I consider to be fatal to the long-term viability of SAML as an authentication protocol. These flaws can also be used when designing new authentication protocols. That is, you can either sidestep the flaw, or take its inverse and attempt to bake that into the protocol.

### Built on XML

As mentioned above, SAML is built on XML, and XML is complex, butit’s not the committee’s fault. XML is what they had at the time, and it’s what people used. JSON was“discovered”in 2001, but this was right around the time the SAML committee was meeting, and they’d be unlikely to design an authentication protocol around an experimental new format. Especially when it caters to JavaScript and you write a lot of Java.

One could design a quantitative complexity measurement for XML versus JSON or SAML versus JWT/OIDC (e.g., spec/RFC word count, spec/RFCnormativeword count, etc.), but that would require a blog post or paper all to itself. In the interest of staying on topic, I will refrain from doing that here, and suffice to say that XML is significantly more complex than something like JSON.

### Canonicalization

Canonicalization(C14N) is what you do when you want to take the wild mess that is XML, compute a hash of it, and get consistent results. In other words, if the SP and IdP cannot agree on a consistent representation of the XML data, then the bytes won’t line up, the signatures won’t match, and your authentication fails. However, this is easier said than done.

Canonicalization bugs enabled Kelby’s XML comment bypass in 2018:

XML canonicalization (credit: Identity Theft)

Canonicalization is often a precursor to parser differential and/or “round-trip” bugs, which are what most modern SAML attacks use:

* Coordinated disclosure of XML round-trip vulnerabilities in Go’s standard library(2020)
* Securing XML implementations across the web(2021)
* Abusing libxml2 quirks to bypass SAML authentication on GitHub Enterprise(2025)
* Sign in as anyone: Bypassing SAML SSO authentication with parser differentials(2025)
* SAML roulette: the hacker always wins(2025)
* The Fragile Lock: Novel Bypasses For SAML Authentication(2025)

### Enveloped signatures

Enveloped signatureconcerns are a not-too-distant cousin of canonicalization. In short, if you’re trying to insert the signature into the data payload that you’re signing, you’re going to have a bad time. Let’s compare and contrast JWT and SAML in this way:

JWT versus SAML signatures (credit: jwt.io and samltool.io)

In the JWT example above, the blue signature isdetachedfrom the JSON payload and delimited in the JWT with a period (“.”). In the SAML example, theSignatureelement is inserted (“enveloped”) in theAssertionelement. The problem here is that it is very difficult to get a byte-for-byte, canonically equivalent representation of the data whenyou’re also modifying it!Even more so when you have a complex format like XML and complex canonicalization rules.

### “Kitchen-sink” design

This design deficiency essentially transposes toyou aren’t gonna need it(YAGNI). It’s not an entirely fair characterization because the portions of the SAML specification that are used in the real-world have changed over the past 20 years (sorry,SOAP and artifact binding). However, the fact of the matter is that 99% of modern SAML implementations use a very similar data shape and subset of the specification. Any given SAML authentication you would encounter in the wild today probably avoids 90% of the specification. This adds significant complexity for largely unused features.

If I was adding SAML support to something new, I’d consider beyond all the standard SAML checks also rejecting any message that doesn’t have the same shape as what Okta, Onelogin, Google, or Shib generates.—Thomas Ptacek, 2021

### Ossification

SAML was designed in a different era for a different time and has not received necessary updates. These concerns will generally be of practical implication rather than theoretical. What I mean by ossification can roughly be enumerated as the following:

1. OIDCassumes HTTP, whereas SAML is transport independent.Sure, SAML HTTP bindings exist and are most commonly used, but they are not required. This affords SAML a certain degree of flexibility, but also means that flexibility must be well defined, must be implemented somewhere, and can contain bugs. SAML came about at a time when HTTP + TLS was not yet the dominant backbone of web service communication, and it has never reconciled with this modern landscape. HTTPS allows OIDC to punt encrypted, trusted communication to the transport layer.
2. OIDC generally assumes a connected network topology, whereas SAML does not.The most common OIDC flow (authorization code) assumes the OpenID Provider (OP) and Relying Party (RP) can communicate directly (OIDC OP/RP == SAML IdP/SP). Sure, OIDCimplicit flow with form postexists, but it is very uncommon to see today. Further, SAML has artifact binding for direct communication, but it is also very uncommon. The point is that if the OP and RP can communicate directly then that relieves pressure off of the authentication response payload to contain all the information necessary to make an authentication and authorization decision. This reduces payload size and complexity. The OIDC OP and RP can instead exchange information in a backchannel.
3. OIDC grew organically over the years, whereas SAML was largely designed up front.OIDC encompasses dozens of specifications and RFCs that grew organically over many years. These documents were generally created to solve a specific need rather than trying to anticipate all future needs and building that up front. This is akin to agile methodology versus waterfall, as described in the first section. Consider the following non-exhaustive timeline:OpenID Connect 1.0 specification published (2014)JOSE stack finalized for JW{S,E,K,A,T} via RFC 7515-7519 (2015)PKCE published via RFC 7636 (2015)PKCE for mobile/native apps published via RFC 8252 (2017)Device authorization grant for IoT devices published via RFC 8628 (2019)Demonstrating proof of possession (DPoP) for MFA workflows published via RFC 9449 (2023)PKCE for SPAs published via RFC 10017 (2026)
4. OpenID Connect 1.0 specification published (2014)
5. JOSE stack finalized for JW{S,E,K,A,T} via RFC 7515-7519 (2015)
6. PKCE published via RFC 7636 (2015)
7. PKCE for mobile/native apps published via RFC 8252 (2017)
8. Device authorization grant for IoT devices published via RFC 8628 (2019)
9. Demonstrating proof of possession (DPoP) for MFA workflows published via RFC 9449 (2023)
10. PKCE for SPAs published via RFC 10017 (2026)

I find the historical circumstances interesting too. For example, SAML came of age in an era of VPNs and network segmentation, hence point (2) above. If the IdP or SP was behind a corporate firewall, and it couldn’t speak directly to the other end, then the whole rollout came to a halt and that vendor lost the sales deal. SAML needed to seamlessly account for this situation. Google’sBeyondCorp modeland zero-trust architecture flipped this notion on its head in 2014. Additionally, SAML failed to anticipate the mobile, SPA, and IoT revolutions, and had no answers when these technologies arrived on the scene in the late aughts. Even though SAML is still widely adopted in corporate environments, these macroscopic events helped start the long, slow decline of the protocol. Agility and loose coupling enable rapid adaptation in ever-changing IT environments.

## All roads lead to OIDC

No protocol is perfect, but in terms of a solution all roads lead to OIDC. As far as I can tell, the only deployment scenario where SAML had an advantage was networks where the SP and IdP cannot communicate directly. OIDC’s implicit flow with form post provides all the same ingredients. This is actually one of the cleanest migration plans I’ve seen available in the industry.

So what can I do if I’m aservice provider(i.e., SP) and I’d like to integrate into the SSO ecosystem without SAML? Just support OIDC. Abandon SAML. Apparently Fly.io and Tailscale are already doing it:

We’ve managed to hold the line on OIDC so far. So has Tailscale. If Tailscale can hold the line, given who they’re selling to, I think most orgs can. Really, try to avoid doing SAML. Remember, as a vendor, you’re often competing with companies that don’t do real SSO integration at all.—Thomas Ptacek, 2024

So what can I do if I’m anidentity or authentication provider(i.e., IdP) and I’d like to move off of SAML? Well, depending on your customer count, this may be a long road indeed. But you know how you eat an elephant? One bite at a time. This is a well-worn path in the industry: develop a deprecation plan, communicate it to customers, stop onboarding new customers to SAML integrations, provide existing SAML customers with equivalent OIDC configurations, set a sunset date, and get to work.

SAML had a good 25 year run. It birthed the SSO industry, helped secure untold numbers of authentications, improved the UX of authenticating to dozens of web services, and created billions of dollars of economic impact. We should be thankful to the creators of the SAML protocol. It has provided us with a great case study in protocol design and evolution over a very dynamic period in the tech industry.

If you’d like to read more about historical analyses of security topics, then check out “Marshal madness: A brief history of Ruby deserialization exploits.”

Contact usif you’re interested in a protocol design audit or would like a review of your authentication system.