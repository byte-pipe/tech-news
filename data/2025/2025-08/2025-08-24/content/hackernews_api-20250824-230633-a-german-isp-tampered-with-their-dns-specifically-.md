---
title: A German ISP tampered with their DNS - specifically to sabotage my website - lina's blog
url: https://lina.sh/blog/telefonica-sabotages-me
site_name: hackernews_api
fetched_at: '2025-08-24T23:06:33.861991'
original_url: https://lina.sh/blog/telefonica-sabotages-me
author: lina
date: '2025-08-24'
description: One of Germany's biggest ISPs changed how their DNS works, right after I exposed an organization that they’re part of.
tags:
- hackernews
- trending
---

## My website: Publishing Germany's secret internet blocklist

In Germany, we have theClearingstelle Urheberrecht im Internet(CUII) - literally 'Copyright Clearinghouse for the Internet',
a private organization that decides what websites to block, corporate interests rewriting our free internet.
No judges, no transparency, just a bunch of ISPs and major copyright holders deciding what your eyes can see.I decided to create a website,cuiiliste.de, to find blocked domains, as the CUII refuses to publish such a list.
To read more about the CUII, check outone of my previous blog posts. Germany's four biggest ISPs
(Telekom, Vodafone, 1&1 and Telefonica (o2)) are all part of the CUII.

## Yet another slip-up by the CUII

This week, Netzpolitik.org published an article about the CUII's latest blunder1, based on information I gathered.
They managed to block domains that no longer even existed: websites that had already been seized and taken offline when they were blocked.
It's not the first time the CUII has tripped over its own feet, and this mistake likely didn’t sit well with them.
In the past, it wasreallyeasy to find out if a domain was blocked by the CUII.
If you asked an ISP's DNS server (basically the internet's phone book) for a site and got a CNAME tonotice.cuii.info, you knew it was blocked.What this basically means in case you're not a tech nerd:You can check the phone book of an ISP (the "DNS server") where to find a website, and you'd receive a note saying "This site is blocked by the CUII" if the page is blocked.
Automating this was simple, I could basically just ask "Hey, where can I find this site?" and immediately knew if it was blocked.
The CUII apparently didnotlike the fact that it was so easy for me to check if a domain was blocked. They want to keep their list secret.ISPs like Telekom, 1&1 and Vodafone actually all stopped using this response a few months ago,
after older articles about the CUII's past failures were published. Instead, they started pretending that blocked sites didn't exist at all.
Straight up erasing entries from the phone book. You could not tell if a site was blocked or just didn't exist.
Telefonica (the parent company of for example o2, Germany'sfourth-biggest ISP2), apparently didn't get this memo, and they still usednotice.cuii.infoin their DNS responses.

On cuiiliste.de, anyone can enter a domain, and see if it is blocked by the CUII, and which ISPs block it specifically.

### I get a new visitor

Telefonica modified their DNS servers, specifically saying thatblau-sicherheit.infowas blocked by the CUII.
At 11:06 AM last Friday, someone from Telefonica's network checked ifblau-sicherheit.infowas blocked on my site.
The twist? Telefonica seems to own this domain. Blau is one of their brands3, andblau-sicherheit.infowasn’t some piracy hub -
it appears to be a test domain of theirs.
My tool flagged it as blocked because Telefonica's DNS servers said so.
Why would they block their own domain?

To recap:

* Telefonica blocks their own domain
* Someone from Telefonica visits my website to check if I detect this
* Idoin fact detect this

### Telefonica modifies how their blocking works... to mess specifically with my website

Two hours after this suspicious query, I was bombarded with Notifications.
My program thought that the CUII had suddenly unblocked hundreds of domains.The reason: Telefonica had altered their DNS servers to stop redirecting blocked domains tonotice.cuii.info.
Now they pretend that the domain doesn't exist at all, after theyspecificallyblocked their own domain, likely to find out how my website works.I had to spend my entire Friday afternoon fixing this mess, and now everything is fully operational again.The fix worked, but there’s a catch: without thenotice.cuii.inforedirect, it's harder to confirm if a block is actually the CUII's doing.
Sometimes ISPs block sites for other reasons, like terrorism content (I wrote about that too).
I try to compensate this by cross-checking domains against a list of known non-CUII-blocks.

### Why sabotage my website?

The timing is more than suspicious.
Right after Netzpolitik’s article exposed the CUII for blocking non-existent domains, they make it harder to track their mistakes.
Coincidence? Or a move to bury future slip-ups?
We can only speculate.
Regardless of intent, the result is the same: less transparency and harder oversight. And that benefits the CUII, not the public.

In this context, Netzpolitik.org released another article (German):Netzpolitik.org: Provider verstecken, welche Domains sie sperren

### Sources

1. Netzpolitik: 17-Jähriger treibt die CUII vor sich her (German)↩
2. DSLWEB, Übersicht: Aktuelle Marktanteile Breitband↩
3. Telefonica: Blau (German)↩
