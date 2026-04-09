---
title: Maintainers of Last Resort
url: https://words.filippo.io/last-resort/
site_name: lobsters
fetched_at: '2025-08-17T23:07:10.730378'
original_url: https://words.filippo.io/last-resort/
date: '2025-08-17'
published_date: '2025-08-14T14:23:59.840150Z'
description: Geomys sometimes acts as a maintainer of last resort for critical Go projects. Recently, we took over the bluemonday HTML sanitizer, and built upgrade paths for the gorilla/csrf library.
tags: practices, security
---

14 Aug 2025

# Maintainers of Last Resort

Geomysis an organization of professional open source maintainers, focused on a portfolio of critical Go projects. For example, we are two thirds of the Go standard library cryptography maintainers, we provide theFIPS 140-3 validationof the upstream Go Cryptographic Module, and we fund the maintenance of x/crypto/ssh and staticcheck amongst others.

Our retainer clientsengage usboth to get access to our expertise, and so that the critical dependencies they rely on are professionally maintained. Beyond our portfolio, we sometimes act asmaintainers of last resortwhen critical, security-relevant Go projects go unmaintained.

Recently, there were two occasions in which we stepped into this informal role:

* we took over maintenance of the popularbluemondayHTML sanitizer when the maintainer chose to move on; and
* we built alternative upgrade paths for the seemingly unmaintainedgorilla/csrflibrary, by introducing a newcarefully researched implementationinto the standard library and creating adrop-in package replacement, after we discovered a security vulnerability in the original.

We can professionally serve in this role, including contracting external help, thanks to the sustainable funding of our retainer agreements. Our clients benefit from our maintenance efforts, and have a direct line to highlight projects in need.

## bluemonday

bluemondayis the most popular HTML sanitizer in the Go ecosystem, used by thousands of applications and libraries to clean up user-generated markup before including it in web pages. Needless to say, it’s a security-critical, load-bearing component.

In late 2023, the sole previous maintainer announced that their new professional circumstances were not compatible with volunteer OSS work, and that they were looking for responsible ways to wind it down. Geomys offered to take over maintenance instead.

Over 2024, Geomys worked with the maintainer to take over the project at its original location, avoiding the disruption of a deprecation, and guaranteeing a natural path for future security updates.

Since we work on Go and open source on a daily basis, the marginal load for Geomys is tiny, but there is outsized value to the community in knowing that security reports would be handled by dedicated professionals that can prioritize them appropriately.

Beyond handling security and critical issues, we are also discussing bringing on a domain subject expert on a contract basis to improve safety in edge cases and to future-proof the library further. Again, we can do that because we are sustainably funded through our retainer agreements.

Thiswas welcomed as a great outcome by the original maintainer. The existence of a maintainer of last resort is not only beneficial to the consumers of the ecosystem, but also releases a lot of pressure from volunteer maintainers who would otherwise sometimes carry unsustainable loads out of a sense of duty.

## gorilla/csrf

gorilla/csrfis an extremely popularCross-Site Request Forgeryprotection middleware.

In December 2024, Patrick O’Doherty discovered thatthe library was unintentionally vulnerable toschemelesslysame-site cross-origin request forgeries. This meanshttps://admin.example.comcould be attacked byhttps://blog.example.comor, even worse,http://foo.example.com. UnlessHTTP Strict-Transport-SecuritywithincludeSubDomainsis used, any network attacker can control the latter and mount the attack. This wasfixed publicly in January, but a new release (v1.7.3) and an advisory (CVE-2025-24358) weren’t published until April.

Alerted by Patrick’s finding, we looked into the library, and found a further issue that again allowed network attackers to mount CSRF attacks if the application used theTrustedOriginsoption. We reported this to the project on April 18th, 2025; however, it hasn’t been acknowledged and the project appears unmaintained. (We arepublicly disclosing itas the customary 90-day deadline has lapsed, and all the upgrade paths listed below are available as of yesterday, with the release of Go 1.25.)

We tried reaching out to past maintainers via email and Slack to offer to take over the project, but unfortunately never heard back. Therefore, we set out to find other solutions to fill this critical CSRF-shaped hole in the ecosystem.

1. First, we researched the landscape of CSRF countermeasures, and consulted with subject experts, including some of the authors of relevant Web specifications. We found that modern browsers providesecurity metadata in request headersthat makes it possible to reject cross-origin requests without any tokens or keys, leading to a drastically better developer experience, better security, and fewer false positives!The results of that investigationare public for other projects that may benefit from it.
2. Second, weproposed and introduceda newCrossOriginProtectionmiddleware in thenet/httpstandard library package. It is part of Go 1.25,released yesterday, and we recommend all gorilla/csrf users consider switching to it. We trust that a standard library solution will safely serve the ecosystem going forward.
3. For applications that are not ready to update to Go 1.25, we made a nearly-identical middleware available as a Go module, atfilippo.io/csrf.
4. Finally, we made a drop-in replacement package for the whole gorilla/csrf API that uses the new countermeasures instead:filippo.io/csrf/gorilla. We tried to minimize any side-effects of the substitution, for example by returning random values in place of the now disused tokens, but we invite you to read the package docs.

Again, all of this is enabled by and part of the Geomys retainer contracts. If you work at a company with a critical dependency on the Go ecosystem, consider reaching out at hi@geomys.org. Regardless, you might also want to follow me on Bluesky at@filippo.abyssdomain.expertor on Mastodon at@filippo@abyssdomain.expert.

## The picture

Since we’re talking about Geomys, here’s a throwback to… last year? Was it just last year?? Anyway, we sponsored GopherCon US and set up a booth mostly to cover it with my collection of gophers and pins.

Geomys is funded bySmallstep,Ava Labs,Teleport,Tailscale, andSentry. Here are a few words from some of them!

Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social engineering, credential theft, or phishing.Teleport Identityis designed to eliminate weak access patterns through access monitoring, minimize attack surface with access requests, and purge unused permissions via mandatory access reviews.

Ava Labs — We atAva Labs, maintainer ofAvalancheGo(the most widely used client for interacting with theAvalanche Network), believe the sustainable maintenance and development of open source cryptographic protocols is critical to the broad adoption of blockchain technology. We are proud to support this necessary and impactful work through our ongoing sponsorship of Filippo and his team.
