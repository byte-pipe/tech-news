---
title: Email could have been X.400 times better
url: https://buttondown.com/blog/x400-vs-smtp-email
site_name: hnrss
content_file: hnrss-email-could-have-been-x400-times-better
fetched_at: '2026-04-25T11:37:36.208071'
original_url: https://buttondown.com/blog/x400-vs-smtp-email
author: Matthew Guay
date: '2026-04-23'
description: X.400 said what must be possible. SMTP said what must be done.
tags:
- hackernews
- hnrss
---

If the history of email had gone somewhat differently, the last email you sent could have been rescinded or superseded by a newer version when you accidentally wrote the wrong thing. It could have been scheduled to arrive an hour from now. It could have auto-destructed if not read by midnight.

You would never have needed to type “as per my previous message.” Instead, you could have linked emails together into a personal Wikipedia of correspondence. You could have messaged an entire organization or department, with your email app ensuring the message was deliverable before it left your outbox.

And you could have attached files and written a multilingual message with letters beyond ASCII’s 128 characters, eight years before those features came to internet email. You could have been notified when the message was read a full 15 years before email had something similar tacked on. Encryption would have been baked in from the start, rather than waiting for PGP, S/MIME, and TLS to add them later.

All that, and more, was standardized in the 1984 spec for X.400 asInterpersonal Messaging. It was everything we callemailtoday, and then some.

“We had a better system back in the day: X.400,” as one commentatorreminisced. SMTP, theSimple Mail Transfer Protocolthat became the standard behind how modern email is sent, “didn’t win because it was ‘better,’” he argued, but “just because it was easier to implement. Like a car with no brakes or seatbelts.”

“Of all the things OSI has produced, one could point to X.400 as being the most successful,”agreed Marshall T. Rose, a developer who helped bridge the differences between X.400 and SMTP email. Differences like X.400 email addresses withbang path-esqueaddresses likeC=no; ADMD=; PRMD=uninett; O=uninett; S=alvestrand; G=haraldwhile SMTP email addresses looked likeHarald.Alvestrand@uninett.no.

“On the other hand,” he concluded, “that’s kind of like saying that World War II was the successful conclusion of the Great Depression.”

## Come, let us build a standard

Exchange Server was, in part, built on X.400 standards, and connected to X.400 for years after the standard had faded from popularity

Six months before Neil Armstrong stepped on the moon, the United States Department of Defense started building ARPANET, a network to link computers around the country, budgeted from money redirected from missile defense.

It was on that network that email as we know it was invented. Ray Tomlinson pulled file transfer software, the ARPANET network, and the@symbol together, and in 1971 email was born. Soon enough it wastaking up more than 3/4th of all ARPANET traffic. “Here was this fantastic infrastructure built at government expense for serious purposes — and these geeks were using it for sending messages to one another,” as John Naughton put it in hisBrief History of the Future.

Email—or at least the idea of email—took the world by storm. CompuServe offered electronic mail to businesses in 1978 and to consumers a year later, with numeric IDs to message anyone else on their network. Or you could subscribe to The Source (launched in ’78) or MCI Mail (as of ’83) or AppleLink (fashionably late in ’86, then to powerthe first email to spacein ’91).

Telecoms and governments joined the rush. By 1982, British Telecom launched their Telecom Gold email solution, and USPS, in a $40 million misstep, tried to monopolize email on paper withE-COM. “Two-thirds or more of the mailstream could be handled electronically,” assumed Congress a mere eleven years after Tomlinson sent the first email.

Yet the majority of those emails were messages inside walled gardens. You could email anyone you wanted, as long as they, too, used the same service. Even email’s original home was a mess. “By 1977, the Arpanet employed several informal standards for the text messages (mail) sent among its host computers,”stated RFC 822, an attempt in 1982 to standardize email. Someone had to make electronic messages speak the same language.

In stepped the United Nations. “The establishment in various countries of telematic services and computer-based store-and forward message services in association with public data networks creates a need to produce standards to facilitate international message exchange between subscribers to such services,” opened the document that aimed to standardize email, three layers of bureaucracy removed from the Secretary-General, and for a moment email could have been an international standard.

## I'm from the government and I'm here to help

One of the simpler diagrams from the X.400 standard

Email should be clear and concise, says the United Nations today, decades removed from the medium’s chaotic early years. Focused on a single topic, with short, meaningful sentences free from jargon. It should be positive, civil, and formal when appropriate,advisesthe self-described universal global organization.

Under its auspices—via the International Telecommunication Union’s Consultative Committee for International Telephony and Telegraphy committee and the UNESCO-linked International Federation for Information Processing—email was almost standardized in October, 1984 under the X.400 spec that was anything other than concise and jargon-free.

“This Recommendation is one of a series of Recommendations and describes the system model and service elements of the message handling system (MHS),” started the‌Data Communication Networks Message Handling Systemsdocument that spelled out the X.400 spec, drafted by a committee chaired by Canadian Department of Communications senior advisor V. C. MacDonald and filled with national telecom representatives. “The MHS model uses the techniques of the OSI Reference Model to formally define the layered communication structure used between the model’s functional components.” And so on and so forth, for 266 pages. It took six pages to describe how to address messages without once showing a complete email address (and perhaps that was for the best, since X.400 addresses were varied enough thatRFC 1506identified six common ways to format them).

It was convoluted, over-described, and under-specified, right when email most needed simplification. And it was late.

Two years earlier, the Simple Mail Transfer Protocol had been spelled out in 68 short pages. “The objective of Simple Mail Transfer Protocol (SMTP) is to transfer mail reliably and efficiently,” wrote University of Southern California research scientist Jon Postel inRFC 821about the system that built on the ARPANET’s original email protocols and the earlier Mail Transfer Protocol. “The SMTP design is based on the following model of communication: as the result of a user mail request, the sender-SMTP establishes a two-way transmission channel to a receiver-SMTP.” Its email addresses used a refreshingly simple user@domain format. Its syntax spelled out exactly how a simple email should work, and little more.

Very quickly, the community effort won out over the committee.

## Prescribe versus describe

“Using the X.400 recommendations themselves is practically impossible in most cases, since just learning to read them takes a fair effort which can be expended only by specialists,” opened Cemil Betanov’sIntroduction to X.400book, published in 1993. “X.400 was conceived as a tool, rather than a product.”

X.400’s spec prescribed outcomes, that software shall do this and this shall happen as a result. SMTP typically instead described exactly how things should work.

Sending a message, for instance, is described in X.400 as follows, with a description of the desired outcome (envelopes, in X.400, generally stood for what today we’d think of as an email message with headers):

The submission interaction is the means by which an originating UA transfers to an MTA the content of a message plus the submission envelope. The submission envelope contains the information the MTS requires to provide the requested service elements.

SMTP, on the other hand, describes sending an email with specific command names and interaction steps:

There are three steps to SMTP mail transactions. The transaction is started with a MAIL command which gives the sender identification. A series of one or more RCPT commands follows giving the receiver information. Then a DATA command gives the mail data. And finally, the end of mail data indicator confirms the transaction.

There were reasons for the complex verbiage. X.400 was imagined as an ideological framework that telecoms and software vendors could each implement in their own way. The ugly addressing? It “provides solutions to certain problems and is ugly for good reason,” Betanov explains. “Make it less ugly, and it immediately loses functionality. Thus, the solution is not to make addressing nicer, but to hide it from the user,” something both internet email and X.400-powered software could easily do with headers, not so much with addresses.

Users liked the ideas in X.400, liked the potential of interoperability and richer email. Businesses and governments alike found its security features alluring, with authenticated message origins, body part encryption to keep privileged data from prying eyes, and classification labels. User demand led businesses to deploy it. By 1989,X.400 was supported by“22 E-Mail software vendors,” including software names like CC Mail and Lotus, computer makers like DEC, and telecoms like AT&T. “X.400 had interconnected one million mailboxes on many networks by 1994,”wrote Dorian Rutterin a thesis on British networks (paling beside the estimated 25 million internet users that same year).

But they were equally taken aback by the difficulty of using it, and by implementations that fell short.

X.400 was “top-down,” MIME authorNathaniel Borensteinrelayed on a call. “That's the way the telecoms did things. They would set out requirements, and their teams of people who wrote the specifications would fulfil those requirements.”

It was easy enough, in theory, for AT&T or British Telecom to implement the standard they helped create. “Because they had total control over the architecture, they could do that a lot more than you can in today's world.” So it was possible, say, for one implementation of X.400 to offer X.400 features like recalling a message, in theory at least, when such guarantees would fail as soon as messages left their walled garden. But “they couldn't buck the rules of physics,” Borenstein concluded. Once a message reached another server, the X.400 implementations couldsaythat an email was recalled or permanently deleted, but there was no way to prove that it hadn’t been backed up surreptitiously.

And thus X.400’s original mission of interoperability was doomed to failure, regardless of how far original X.400 implementations spread.

Despite the standard, Rutter’s thesis found, “most e-mail users remained isolated from each other. X.400 had therefore failed to fulfil the promise set for it by its proponents.” Another case study into why X.400 failed reached a similar conclusion: “Even early implementations of the incomplete initial X.400 version were frequently incompatible,” wrote Kai Jakobs. “It was next to impossible to exchange messages between systems from different vendors.”

Inside the X.400 ecosystem itself, the complexities added up to an unworkable system. AsTom Fitzgerald parodied it: “X.400: So secure that an X.400 mailer won't even talk to another X.400 mailer from a different vendor.” “I have several accounts that could be reached by X.400, each of which could be used in a different way, depending on what system you come from,”recounted Jim Carroll, co-author of theCanadian Internet Handbook. “You might reach me asc:us,a:mcimail;f:jim;s:carroll;on one system, or you might reach me using the methodmhs!c=us/ad=mcimail/pn=jim_carroll, while on yet a third system you might send to me using the form[jim_carroll/jacarrollconsulting] mcimail/usa.”

“People pay me to help them figure out how to use X.400. They pay me!,” Carroll marveled. “Isn't there something wrong with this picture—an addressing standard that is so complicated that you have to hire a consultant to figure it out?”

Telecoms standardized X.400. Governments, from the US’s GOSIP to the EU’s procurement rules, mandated it. Developers either rued its complexity or raved over its potential.

Meanwhile the simple mail transfer protocol spread like wildfire, and by 1993 even the United Nations acquiesced to sending email over both X.400 and the internet.

“I worked for a company that ran X.400 commercially, before the Internet really got going,”shared Chris Marshall, a former Dialcom employee. “It did, indeed, have many things that we wish email had, these days, like true read receipt and routing management. But it was a complex beast, and that is why it lost out to simple SMTP and POP.”

“X.400 is dead,” Carroll surmised, “because it isn't as simple as the telephone, fax, and Internet e-mail.”

## What is dead may never die

Aeronautical software Lunar AMHS, with X.400-style addresses while submitting a flight plan

You don’t email with X.400 today. That is, unless you work in aviation, where AMHS communications for sharing flight plans and more are still based on X.400 standards (which enables, among other things, prioritizing messages and sending them to the tower at an airport instead of a specific individual). It’s used, sparingly today, in militaries, governments, and banking—and previously powered parts of the SWIFT standard for transferring money.

And if you use Microsoft Outlook with a Microsoft Exchange Server, you might recognize some similarities with X.400 (and its related X.500 standard for directories, “the one part of OSI that actually won,” as Borenstein put it). Exchange included built-in authentication, long before SPF, DKIM, and DMARC were possible, and its delivery reports are still more detailed than their SMTP counterparts. “The entire data model of MAPI is based on [X.400],” said @p_l in aHacker News comment, “shared between Outlook and Exchange, with somewhat lossy translation when it has to go outside of X.400-over-RPC that MAPI provides.”

Internet email—the SMTP stack we’d come to just call email—gained enough features over the years to nearly reach parity with X.400. It moved fast, far faster than X.400. The original idea that turned into X.400 started with a working group convened in 1978; it took 6 years to get the first standard, and 4 more years to update it. In that same timeframe, 339 RFCs were published, including the nine core email-focused RFCs. And email’s changes were implemented in a way that let every email system do its own thing, maintaining uniqueness and compatibility at the same time.

MIME, the standard that among other thingsadded multi-language support and attachments to SMTP email, started around existing email systems. “Let us assume that we have an existing electronic mail infrastructure. And now we are going to figure out the minimalist set of changes which we can add on top of that,” Marshall Rose described MIME’s approach. X.400, by contrast, had “this kind of blanket assumption that someday everything will be X.400 and we won’t have to worry about existing mail systems.”

Email’s a messy, living standard, one that’ssurvived this longin part thanks to the simplicity embodied in SMTP’s name. It looked too simple at first, almost emblematic of venture capitalistChris Dixon’s postulationthat “The next big thing will start out looking like a toy.”

A simple mail transfer protocol it was, but it did just enough to get email systems talking to each other. It specified just enough to make diverse implementations compatible. And it was rapidly iterated on enough that by the time X.400 systems were ready for use, people were using SMTP-powered email to talk about it.

And that was enough to relegate X.400 to the inspiration pile, and for SMTP to outlive X.400 as what we’d know today as email.

Image credits

Image
Credit
Header photo from the ITU
International Telecommunication Union
X.400 in Exchange Server
Network Encyclopedia
Lunar AMHS Terminal
Galadrium