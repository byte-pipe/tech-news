---
title: 'Behind the complaints: Our investigation into the suspicious pressure on Archive.today'
url: https://adguard-dns.io/en/blog/archive-today-adguard-dns-block-demand.html
site_name: hackernews_api
fetched_at: '2025-11-15T19:06:19.700130'
original_url: https://adguard-dns.io/en/blog/archive-today-adguard-dns-block-demand.html
author: immibis
date: '2025-11-15'
description: Some time ago, we were contacted by a group fighting against online CSAM, demanding that AdGuard DNS blocks the Archive.today website. This was only the beginning of a much larger story…
tags:
- hackernews
- trending
---

# Behind the complaints: Our investigation into the suspicious pressure on Archive.today

 November 13, 2025


 5 min read


14 Nov 2025 UPD: We have updated the article with more information on the bailiff reports sent to us and the person who ordered them.

The FBI has been investigating Archive.is (also known as Archive.today),as was recently revealed. The agency issued a subpoena to the site’s domain registrar, asking for information about the person behind it, citing a “federal criminal investigation.”

Archive.is was launched in 2012 by someone using the nameDenis Petrov— though whether that’s their real identity remains unclear. The site lets users save “snapshots” of web pages by submitting URLs, which makes it a valuable tool for preserving content that might otherwise disappear. But because it can also be used to bypass paywalls, it’s long been a thorn in the side of many media organizations.

While the exact nature of the FBI investigation hasn’t been confirmed, it is speculated it can be related to copyright or CSAM (child sexual abuse material) dissemination issues. Altogether, the situation suggests growing pressure on whoever runs Archive.is, and on intermediaries that help make its service accessible. AdGuard DNS, as it turns out, may have just become one such pressure point.

## How we got entangled

A few weeks ago, we were contacted by a representative of an organization called theWeb Abuse Association Defense, a French group claiming to fight against child pornography. Their website iswebabusedefense.com, and here is thearchived versionas of November 7.

They demanded that we block the domainarchive.today(and its mirrors) in AdGuard DNS, alleging that the site’s admin had refused to remove illegal content since 2023. To be clear, Archive.today allows users to take “snapshots” of any webpages, including potentially illegal material. In such cases, it’s the site admin’s job to respond to complaints and promptly remove that content.

This struck us as strange — we’re not a hosting provider, and it seemed unusual for an infrastructure-level service like ours to be asked to take action like this.

Soon after, the situation escalated into what we could only describe as direct threats:

We won’t share all the screenshots here, but there were several similar messages.

We sought legal advice, and unfortunately discovered that French law, specifically Article 6-I-7 of theLoi pour la Confiance dans l'Économie Numérique(LCEN), might actually require us to respond and apply blocking measures, at least for French users.

That said, this whole situation shows just how inadequate this regulation is. Such decisions should be made by a court — a private company shouldn’t have to decide what counts as “illegal” content under threat of legal action.

Even so, the story didn’t quite add up. Since someone was trying to pressure us into taking action, we decided to contact the other side, Archive.today, directly.

We sent an email to Archive.today’s contact address and asked two simple questions:

1. Can they remove the illegal content from the URLs we were informed about?
2. Is it true that they refused to remove such content in the past, and had they been notified about it before?

They replied within a few hours. The response was straightforward: the illegal content would be removed (and we verified that it was), and they hadneverreceived any previous notifications about those URLs.

Moreover, they hinted that Archive.today had been targeted by a campaign of “serial” complaints, supposedly from French organizations, sent to various companies and institutions that could potentially harm the site. They even shareda linkdemonstrating a complaint similar to the one we had received.

At that point, things were looking increasingly odd, so we decided to dig deeper into the “complainant.”

The Web Abuse Association Defensewebsite references several well-known organizations — Europol, OFAC, NCA — yet provides no details or evidence of any cooperation with them.

The association itself was registered in February–March 2025, around the same time its website appeared. There is very little public information about it. Interestingly, registering an association in France can apparently be doneentirely onlineand does not require proof of identity.

The association is registered at an address used formass company registration, which isn’t inherently problematic but it does indicate that the entire registration process could have been carried out online by a single person.

ItsTwitter/X accountappeared only recently — in August 2025. It has just four followers, and its feed consists of just a few reposts.

None of this proves anything by itself, but something still doesn’t add up. In their first email, the “head” of the association claimed that their correspondence with Archive.today started with a bailiff report from 2023. That timeline simply doesn’t fit.

We examined the so-called “bailiff reports” they had sent us as evidence. It’s important to note that these aren’t bailiff reports in the English sense — they’re“constat d’huissier sur Internet,”official records of online content such as webpages, posts, or videos.These particular reports were ordered online via the service called Qualijuris, and, based on the timestamps, most of them were also created in August 2025 — not 2023.

Only two of these bailiff reports were ordered in 2023 from a similar service. What’s interesting is that they weren’t ordered by WAAD. The name of the person who ordered these bailiff reports matches the name that appears inthe correspondenceshared with us by the Archive.today administrator — the same one he wrote abouton X in 2024. In that case, the complaint appeared to come from a real lawyer — but someone had registered a domain with the lawyer’s surname, containing nothing but a redirect to the lawyer’s actual website, and did it on the same day the complaint was sent. The domain was used solely to send the emails and it is not active anymore. Interestingly, that email also invoked the LCEN law.

So what is the link between WAAD and that lawyer from before? Are these bailiff reports real and could it be that this is a case of impersonation of a real person? We don’t know yet, but we hope to discover the truth soon enough.

Unfortunately, we couldn’t dig any deeper about who exactly is behind WAAD. The domainwebabusedefense.comis registered withname.com, but ownership information (including historical records) is hidden. They use ProtonMail for email, so that’s another dead end. The site itself is behind Cloudflare, making further tracing impossible.

## What we have in the end

With everything said and done, here’s where things stand now:

1. The illegal content was promptly removed from Archive.today after we notified them.
2. The complaints against the site look extremely suspicious. In our case, they came from an organization that was only recently registered that seems deliberately set up to hide the identities of those behind it.
3. The sample complaint shared by Archive.today’s admin shows signs of impersonating a real person. We have contacted the person in question and are currently waiting for a reply.
4. In both our case and that other example, the recipients were pressured to act under the French LCEN law. However, that same law also provides penalties for false reports:Art. 6-I-4 LCEN:4. Any person who presents content or activity to the persons referred to in paragraph 2 as being illegal with the aim of having it removed or its dissemination stopped, when they know this information to be inaccurate, shall be punished by one year’s imprisonment and a fine of €15,000.
5. We believe there are indications of criminal behavior here that should be investigated by law enforcement. Therefore, we will file an official complaint with the French police, including all relevant details.
6. All this is unfolding amid reports of anFBI investigationinto the owner of Archive.today. It seems that this investigation may be related to CSAM hosting. While we can’t confirm any connection between that case and ours, the timing is certainly suspicious.
