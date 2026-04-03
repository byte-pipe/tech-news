---
title: Abusing copyright strings to trick software into thinking it's running on your competitor's PC - The Old New Thing
url: https://devblogs.microsoft.com/oldnewthing/20250624-00/?p=111299
site_name: lobsters
fetched_at: '2025-06-26T23:06:55.621763'
original_url: https://devblogs.microsoft.com/oldnewthing/20250624-00/?p=111299
author: Raymond Chen
date: '2025-06-26'
published_date: '2025-06-24T14:00:00+00:00'
tags: historical, law
---

Raymond Chen

One very complicated part of bringing up Plug and Play was bootstrapping the entire process. After all, the number of computers that supported the Plug and Play specification started at zero, because the specification was still being written. A lot of clever tricks were used to retrofit Plug and Play onto legacy hardware.¹

The Windows 95 team worked to gather a very large range of PC brands and models, and as part of doing “Plug and Play for PCs that predate the Plug and Play specification”, the team gathered information from all of those PCs to look for clues on how they could be identified. This often included searching the BIOS for copyright strings and BIOS firmware dates.

One of the strings they found was “Not Copyright Fabrikam Computer.”

Why would a BIOS deny that it was copyrighted?

We weren’t sure, but we had a theory.

Back in the early 1990’s, it was not uncommon for PCs to come with preinstalled software that was locked to the manufacturer. If you bought (say) a Fabrikam PC, it would come with a copy of “LitWare Word Processor”. This version of LitWare Word Processor was just the trial edition, but the secret was that the trial edition checked if it was running on a PC manufactured by one of its licensees. If so, then it unlocked its features and became the full version.

LitWare detected whether it was running on a PC manufactured by one of its licensees by searching the BIOS for specific copyright strings. For example, since Fabrikam was a licensee, it searched the BIOS for the stringCopyright Fabrikam Computer, and if if found it, it would unlock the features that were normally disabled in the trial edition.

The makers of Contoso PCs wanted to include the free LitWare Word Processor trial edition with their PC, but they also wanted to unlock the features of the full version despite not being a Fabrikam PC.

The solution: In addition to the normal Contoso copyright string, also put the stringNot Copyright Fabrikam Computerin the BIOS!

¹ Some of those retrofitting techniques were really convoluted, because you needed a way to signal information without confusing existing hardware that didn’t understand that signal, and to allow multiple devices to coordinate responses to the same signal. For example, the serial port detection sequence involves writing specific values to the ADDRESS port to enter configuration mode, and then reading values from the READ_DATA port. If the index of the read matches a set bit in the device ID, then the device responds with a value; otherwise, it does an electrical engineering thing that allows the response to default to zero, while still monitoring the actual value read. The result of the read is nonzero if anybody actively responded, and it is zero if nobody responded. If a device wanted to respond zero, but it saw that the actual value was nonzero, then it means that another device with a higher ID number responded to the query, so it backs off for the remainder of the cycle. After the operating system gathers all the bits of the device ID for the highest-numbered ID, it restarts the process, and the device that won the “highest ID” voting backs off to allow the lower-numbered device IDs to respond. This cycle repeats until an ID of zero is read back (meaning that nobody responded to anything), indicating that all the devices have been identified.

Category
Old New Thing
Topics
History

Share



## Author

Raymond Chen

Raymond has been involved in the evolution of Windows for more than 30 years. In 2003, he began a Web site known as The Old New Thing which has grown in popularity far beyond his wildest imagination, a development which still gives him the heebie-jeebies. The Web site spawned a book, coincidentally also titled The Old New Thing (Addison Wesley 2007). He occasionally appears on the Windows Dev Docs Twitter account to tell stories which convey no useful information.





## Read next

June 23, 2025

### The MIDL compiler still has trouble with double greater-than signs, sadly

Raymond Chen

June 17, 2025

### Funding the Egghead store shopping spree took a little extra legwork

Raymond Chen



## Stay informed

Get notified when new posts are published.



Subscribe

By subscribing you agree to our
Terms of Use
 and
Privacy



Follow this blog



Are you sure you wish to delete this
 comment?

OK

Cancel
