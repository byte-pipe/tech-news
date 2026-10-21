---
title: France's Supermarket Fridges Were Vulnerable Online for Months | IPinfo.io
url: https://ipinfo.io/blog/france-fridges-hack
site_name: hackernews_api
content_file: hackernews_api-frances-supermarket-fridges-were-vulnerable-online
fetched_at: '2026-10-21T11:11:09.629344'
original_url: https://ipinfo.io/blog/france-fridges-hack
author: emot
date: '2026-10-20'
description: IPinfo scans reveal that 85% of exposed French refrigeration controllers had known security flaws before the October 2026 cyberattack.
tags:
- hackernews
- trending
---

Skip to main content
* IP Data Fundamentals
* IP Data Accuracy
* Solving Business Challenges
* Getting Started
* Optimizing and Scaling
* Community and Thought Leadership
* Company News and Updates
a day ago
 
by
 
João Tomé
 
— 
9
 min read

# France's Supermarket Fridges Were Vulnerable Online for Months

### Get Unlimited Access to IPinfo Lite

Start using accurate IP data for cybersecurity, compliance, and personalization—no limits, no cost.

Sign up for free

On the night of October 11 to 12, 2026, fridges and freezers in hundreds of French supermarkets started to warm up. Cyber attackers had pushed the refrigeration systems into defrost mode, which heats the cooling parts to melt ice. Some unitsreached 50°C(122°F), some equipment started to catch fire,according to the Paris prosecutor, and storesthrew away their fresh and frozen food. The reports pointed to one maker of refrigeration controllers, Danfoss (a Danish industrial company).

We went through IPinfo's weekly Internet scans to examine these systems before the attack. In this blog post we’ll explore some of the findings. Here’s the TL;DR:

* France had more exposed fridge dashboards than the rest of the world combined:1,331, against 1,197 in the other 72 countries and territories put together.
* 85% ran software with known security flaws.That includes 527 older controllers Danfoss no longer supports. Only 195 had every known fix.
* Most had been exposed for at least six months.1,019 of the French dashboards were at the same address on March 30, and the share fully updated rose only from 14% to 24% in that time period.
* France didn't patch worse than other countries.The flawed share elsewhere was almost the same (84%). France just had far more of these systems online.
* Most went offline after the attack.316 of the 1,331 were still online on October 14.

## What Happened

The numbers from the chains keep growing.More than 400 storeswere hit in total according to Futura-Sciences, andlosses could reach several million euros. Carrefour said 80 of its stores were hit, while Intermarché and Netto, both part of Les Mousquetaires (a French retail group), hadmore than 300 hit. Monoprix reported thatabout 5% of its storeswere affected.

Leclerc and Coopérative U, two other French supermarket chains,also confirmed attacks. Coopérative U's CEO, Dominique Schelcher,told RTLthat 80 of its 2,000 stores were hit. He added that the stores don't buy from Danfoss directly but use a Danfoss system supplied by their refrigeration contractors.

Danfoss saidmost of the affected equipment was "legacy,” naming two older controller models, the AK-SM 800 and AK-SC 355. CERT-FR (France's cybersecurity agency)said it knew of numerous compromisesof AK-SM and AK-SC controllers. It told operators to disconnect them or restrict who can reach them, andupdated its alert on October 13to add XWEB supervisors (systems that monitor a store's fridges and freezers) from Copeland, a US maker of cooling equipment, and Dixell, its Italian brand. Its alert says attack campaigns are probably still ongoing. Nobody has said who did it or how they got in, and the Paris prosecutor's office has opened aninvestigation.

## France Stood Out, by Far

We scanthe IPv4 Internet(the most common type of Internet address) every week, connecting to the usual ports that websites use (the numbered doors a computer answers on) and recording what answers. In the sweep that ran on October 6 and 7, five days before the attack, 2,528 addresses showed a Danfoss StoreView dashboard. That is the web page that stores and technicians use to watch and manage these controllers, the equivalent of the control panel in the back room, except that anyone who typed in the address could open it.

According to our data, France had 1,331 of them (53%). That is more than the other 72 countries and territories combined (1,197). Poland came next with 179, then the United States (101), Portugal (92), and Belgium (85).

Danfoss dashboards open to the Internet, by country, October 6–7, 2026.

Why France? Our data can't say, but it rules a few things out. French dashboards ran the same mix of software versions as everywhere else, so they weren't patched worse. They also weren't unusual in how they connect. In France, about two-thirds connect through one national provider, much like the main telecom in Portugal, Germany, or Romania. Almost all (98%) are on telecom providers' networks rather than in data centers or clouds, which fits a controller plugged into the store's own Internet connection, with access opened for a technician or head office.

CERT-FR's advicehints at why stores keep them online: it tells them to check their insurance terms before cutting the data their controllers send to refrigeration contractors.

## Most Fridge Software Was Out of Date

The dashboards also give away how old the software behind them is. They come in two generations. The older one is a page built with Flash (an old browser plug-in, retired in 2020) and served by the AK-SM 800. Danfossdeclared these controllers end of life in 2023. That same year, the security firm Synacktivpublished a login bypass(a way in without the password) for them, and Danfoss's advice was to restrict network access. This is the "legacy" equipment Danfoss named.

The newer one runs on the AK-SM 800A, Danfoss's current model. Its dashboard shows when its software was built, a bit like the production date stamped on a carton, which tells us roughly which version it runs: 242 of them say May 19, 2023, the build date of firmware 3.3 (firmware is the software built into the controller). Controllers older than 3.3 missthree 2023 fixes, including one fora flaw rated critical. Those older than 4.2 also miss a fix fora 2025 login bypass, and those older than 4.3.1 misstwo more 2025 fixes.

Put together, 85% of the French dashboards (1,136 of 1,331) ran software with known security flaws, almost the same as the 84% elsewhere. That is 527 older controllers Danfoss no longer supports, 280 missing the 2023 fixes, and 329 missing the 2025 fixes. Only 195 had every known fix.

How up to date the Danfoss dashboards were, France and the rest of the world.

## The Exposure Has Existed for Months

Every scan from late March 2026 until the attack found about the same number: between 2,464 and 2,622 Danfoss dashboards open to the Internet, roughly half of them in France.

They were mostly the same devices. Of the 1,331 French dashboards found on October 6, 1,019 were open at the very same address on March 30, six months earlier. Over those months, the number of older controllers Danfoss no longer supports didn't go down in France (519 at the end of March, 527 in October). Updates came slowly. The share of newer French controllers with every known fix went from 14% to 24%, under two points a month.

Danfoss dashboards found in each weekly scan, March 30 to October 6, 2026.

## Did Stores Disconnect After the Attack?

Most stores did disconnect after the attack. Our next weekly scan ran on October 14, two days after the attack. Of the 1,331 French dashboards from October 6–7, only 316 were still online at the same address, a 76% drop. In the weekly scans from August to early October, only 3% to 7% disappeared from one week to the next. The older controllers Danfoss no longer supports fell the most, from 527 to 64. Fully updated ones fell too, from 195 to 54, which points to stores disconnecting them rather than updating them.

Outside France, 25% disappeared, more than the usual 9% to 12%.Censys, another Internet scanning company that counts every day, saw a similar 71% drop in France between October 11 and 14. On October 14, the technical director of Claroty, the security company that found the 2025 flaws,told Tom's Guidethat exposed AK-SM 800 controllers were still online. Our October 14 scan still found 64 of them.

Danfoss dashboards in France before and after the attack, by software.

## Where Else These Controllers Are Open

France wasn't the only country with these systems online. Danfoss dashboards with known flaws were open in 69 other countries and territories, led by Poland (157), the United States (85), and Portugal (77). In some countries most were the older controllers Danfoss no longer supports: 80% in Iceland, 75% in Australia, and 72% in Germany.

Danfoss dashboards with known security flaws, by country.

Some reports suggest other European countries may have been hit. One analyst quoted by Australia'sABCsaid Spain, Portugal, Poland, Germany, and Belgium had also been affected. Our data can't say whether they were, but it does show that all five had out-of-date Danfoss dashboards open to the Internet five days before the attack.

## What About Dixell?

CERT-FR's updated alert also names XWEB supervisors from Dixell, Copeland's Italian brand of refrigeration controllers, so we counted those too. The same scan found 1,611 XWEB dashboards in 66 countries, but only 70 in France; Italy, where Dixell is based, had 467. Judging by when their software was built, only 180 of the 752 newer XWEB PRO units hadthe February 2026 fixes. The other 859 were older models thathaven't had a software updatefrom Copeland since 2018. After the attack, French operators unplugged their XWEB dashboards too: our October 14 scan found only 20 of the 70 still online, a 71% drop, when a normal week loses 2% to 9%. Elsewhere, including Italy, the number fell only at the usual weekly rate.

## How We Counted

The dashboards were identified with two fingerprints (patterns that identify a device) built by our data team. The newer interface is matched by its page title. The older one is matched by its web server plus the Flash loader page, which identifies the AK-SM 800. AK-SC 355 controllers, which Danfoss also named, may not be in our count. Sixteen devices that share the older web server but aren't Danfoss (network cards in backup power units, building controllers, thermostats) were removed, along with two addresses that answer on almost every port, a sign of a honeypot (a decoy set up to attract attackers).

An independent count by the security researcher Baptiste Robert,posted on X, found 2,752 Danfoss systems online, 1,590 of them in France, a little above ours. Censys, which scans differently, found more: 1,825 of the newer dashboards in France on October 11, 61% of its worldwide total.

The numbers are a minimum. They cover IPv4 only and the ports we scan, and an address is not always one store. We aren't publishing any of the addresses. CERT-FR told us it had already identified the affected systems, and we're in contact with CERT-EU (the EU's cybersecurity team for its institutions) to help other European cybersecurity teams in any way we can.

## What Operators Can Do

CERT-FR's adviceis to take these controllers off the public Internet and, if a contractor needs remote access, to give it through a secure VPN (a private, encrypted connection). Letting in only the contractor's addresses is a stopgap, not a fix. A factory reset alone isn't enough either: an exposed controller that no longer gets updates will likely be compromised again. For Danfoss systems, CERT-FR also says to update the firmware, set the security level to Strict, and change the default passwords.

## What the Data Can't Say

We can't tell from the scans how the attackers got in or who they were, and we don't know which chains or stores were hit. Being able to open a dashboard from the Internet doesn't mean anyone can break in through it, and nobody has said whether any of the flaws above were used.

The data does show what things looked like before and after the attack. Five days before the attack, France had more of these dashboards open to anyone than the rest of the world combined, and most were behind on updates. After the attack, most of them went offline within days, and we'll keep checking the 316 that were still online on October 14.

This is one of IPinfo's data stories, where we use our own measurements to look at what happens on the Internet. If you spot something we got wrong, have data that adds to this, or have a story you'd like us to look into, write to us at emot@ipinfo.io.

Data: IPinfo’s Internet scans of IPv4 addresses: 18 scans from March 30 to October 6–7, 2026, about one a week, and one on October 14, after the attack. Counts are addresses and a minimum.

#### Share this article

#### About the author

João Tomé

João Tomé is an Internet Data Research Editor at IPinfo, finding trends and stories about how the Internet works and changes. He has a background in journalism, data storytelling, and podcasting, including five years at Cloudflare.

joaotome.com

### Get Unlimited Access to IPinfo Lite

Start using accurate IP data for cybersecurity, compliance, and personalization—no limits, no cost.

Sign up for free

#### Recent articles

* RPKI Now Protects 70% of Internet Routes, Up From 54% a Year Ago
* Money20/20 2026: When Fraud Looks Like a Real Customer
* New White Paper: The State of AdTech 2026
* How We Made Our MMDB Files a Third Smaller Without Changing a Byte of Data
* Bad Traffic Brought Visitors to Our DMEXCO Booth, but Good Traffic Kept Them There

#### Share this article