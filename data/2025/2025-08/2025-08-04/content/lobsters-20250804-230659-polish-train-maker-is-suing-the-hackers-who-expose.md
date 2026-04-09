---
title: Polish Train Maker Is Suing the Hackers Who Exposed Its Anti-Repair Tricks - iFixit
url: https://www.ifixit.com/News/112008/polish-train-maker-is-suing-the-hackers-who-exposed-its-anti-repair-tricks
site_name: lobsters
fetched_at: '2025-08-04T23:06:59.508275'
original_url: https://www.ifixit.com/News/112008/polish-train-maker-is-suing-the-hackers-who-exposed-its-anti-repair-tricks
date: '2025-08-04'
description: Newag, maker of Polish trains, is suing ethical hackers who exposed its anti-repair software, threatening independent repair and consumer rights.
tags: law, reversing
---

Rememberback in 2023 when hackers exposed(and fixed) malicious anti-repair software in Polish trains? Well, it turns out that the manufacturer, Newag, is at it again.

Just last month, three new trains got locked up in Poland. Newag initially refused to unlock them but relented in the end. But it gets worse. Much worse. Newag has now sued both the Polish repair service SPS that fixed those original trains, and has also gone after the individual members of ethical hacking groupDragon Sector, who studied the trains’ software and discovered Newag’s anti-repair measures. In total, the two lawsuits seek the equivalent of over $3 million USD.

But first, let’s see how we got here.

## Attempt Third Party Repair? Here’s a Lockout For You

Back in 2022, members ofDragon Sectorwere called in by a train repair shop Serwis Pojazdów Szynowych (SPS) to work out why its trains were refusing to run. Digging into the code revealed a software trap that would disable trains if they were anywhere near a repair facility that wasn’t run by the manufacturer, Newag. But Newag used a pretty inaccurate way to determine when the trains were in a rival repair shop, which led to some unexpected consequences.

The original version of the locking mechanism seems to have counted how many days a train sat out of use. If it exceeded a time limit (originally ten days), it locked up the train.

This lock got triggered in the first few trains serviced by SPS (which had no idea what was really happening), and Newag claimed that the trains had locked up because the repair techs had broken something.

A few weeks later, two more trains were waiting to be sent to SPS (because the SPS storage facilities were full of locked-up trains). After SPS freed up some space, train owner Koleje Dolnośląskie found that they didn’t start anymore either, showing exactly the same symptoms as those that locked up at SPS. At this point, Michał Kowalczyk of Dragon Sector tells us, Newag’s version of events started to look suspicious. They said that the trains at SPS broke down because of faulty servicing. But these newly locked trains never even got near SPS, and they’d locked up in exactly the same way.

These two trains were subsequently repaired by Newag, but without revealing what they had actually fixed. When the Dragon Sector team analyzed them afterwards, they discovered that the locking system had been updated to wait for 21 days instead of ten.

And it gets better. Newag also added a new GPS component. This would check whether trains were near known workshop locations before disabling the trains. And of course, this trick also backfired. Newag ships slightly different software for each manufactured “batch”, so effectively each owner gets slightly different trains. And one batch of the 45WE EMU (electric multiple unit, the kind of train that doesn’t have a separate engine up front to pull the passenger cars), would switch off automatically when passing through the Mińsk Mazowiecki railway station. Trains full of passengers were left stranded.

You can probably guess what happened next. Newag not only denied that it had added such software, but claimed that it had been added by hackers, hinting that those hackers had done it on behalf of a rival company.

It seems like a lot of hassle on the part of Newag, but the rewards are huge. For example, Michał Kowalczyk told me that Newag was “taking around 25k EUR per unlock” in the past. That’s a chunk of money for sure, but Newag may also have been angling to monopolize the Impuls train service market, which is worth around $40 million USD annually. Think of it more as having to pay to get your cell phone unlocked from the carrier.

A Newag “Impuls” train passes the National Stadium Warsaw. Photo via
Schnitzel_bank on Flickr
.

## Are Software Lockouts Legal?

In the US, companies like tractor maker John Deere have used the Digital Millennium Copyright Act (DMCA) tothreaten independent repair shops. Manufacturers put protections into their software, and sue under the DCMA, which makes breaking such protections illegal. The DMCA was meant to stop people from copying movies and music, but has since gone far beyond.

Criminal punishments under the DCMA include fines up to $500,000, up to five years in jail, or both. You can see why it’s such a powerful tool for suppressing both big and small repair outfits.

But we’ve been fighting for the last decade to make repair activities exempt, and we’ve had a lot of success. With our friends at Public Knowledge, we’ve won DMCA exemptions for everything fromcell phonestoMcFlurry machines. Still, as we know from the continued existence ofillegal“warranty void if removed” stickers, manufacturers don’t always seem to care about the law when it comes to abusing our rights to repair the products we bought and own.

Fortunately, the law in the EU generally seems to favor this sort of reverse engineering. Several judgements from the European Court of Justice (CJEU) have ruled in favor of reverse engineering vs copyright. One of thesespecifically rules that decompiling softwarein order to find and fix bugs does not infringe copyright. Another judgement, against Sony,allowed for people who made PlayStation Portable third-party add-ons to interfere with game codeas it runs, without violating copyright.

If you read some of the CJEU judgements above, you’ll see that they are less clear on whether or notalteringsoftware is explicitly allowed. In another case, a different train company (Koleje Mazowieckie) neatly skirted this by just disconnecting the GPS receiver. If nothing else, this proves that even the fanciest digital lockouts can still be beaten through a good old-fashioned analog hole.

Which brings us back to the present day. Newag has sued SPS, along with Michał, Sergiusz, and Jakub, the Dragon Sector team members who unearthed the anti-repair measures.

More Newag “Impuls” trains in Wroclaw, via
M.M. Czarnecki on Flickr
.

## The Train Company’s Suing. Do They Have a Case?

Newag is suing in the Warsaw courtfor 6,453,000 PLN (US$1.7 million) for copyright violation and unlawful competition. It isalso suing in the Gdańsk court, demanding 5,100,000 PLN (US$1.36 million) for unlawful competition, and infringement of personal rights.

Do they have a case? A lay reading of the EU laws above sure makes it seem like ​​you can explore software for diagnostic purposes.

And the cases seem a little muddled, too. Newag claims that the Dragon Sector team endangered passengers’ safety by modifying the software without proper experience. But Newag then turns right around and claims that Dragon Sector did not modify the software at all. They point out that EU law only allows reverse engineering of software in order to fix bugs. And if Dragon Sector did not actually modify the software, it cannot have fixed any bugs, in which case their reverse-engineering must be illegal.

I’m no lawyer, nor do I impersonate one on the internet, but that seems like self-contradictory nonsense to me. Digging into the case filings, it really does seem like Newag is trying to scare everybody off. Otherwise, what other reason is there to go after the individuals who did the digital exploration?

This continuing saga shows how important regulation and legislation are to protect consumers, whether it’s individuals like us, or companies that are being bullied into complying with some pretty odious demands. In fact, it’s the companies that are most important here. If you hack your car so that you can repair it yourself, then nobody will even notice. But if your local repair shop tries to do the same, perhaps to use third-party spares, then this kind of bullying can shut them down.

Europe is far from perfect in this regard. It too has insane copyright laws on the books, but in general the EU is a lot more pro-consumer-rights than the US. In the meantime, iFixit continues to fight for the right to repair, which isslowly sweeping the world, being written into law, state by state, country by country. Without better laws, Big Corporate will continue to use current laws to extract as much money as possible from anyone who looks like a weak mark.
