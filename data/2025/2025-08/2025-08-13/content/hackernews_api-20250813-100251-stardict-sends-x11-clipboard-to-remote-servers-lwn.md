---
title: StarDict sends X11 clipboard to remote servers [LWN.net]
url: https://lwn.net/SubscriberLink/1032732/3334850da49689e1/
site_name: hackernews_api
fetched_at: '2025-08-13T10:02:51.178471'
original_url: https://lwn.net/SubscriberLink/1032732/3334850da49689e1/
author: pabs3
date: '2025-08-12'
description: StarDict sends X11 clipboard to remote servers
tags:
- hackernews
- trending
---

LWN
.net

News from the source






User:


Password:



 |


 |


Subscribe
 /

Log in
 /

New account

# StarDict sends X11 clipboard to remote servers

## [LWN subscriber-only content]

### Welcome to LWN.netThe following subscription-only content has been made available to you
by an LWN subscriber. Thousands of subscribers depend on LWN for the
best news from the Linux and free software communities. If you enjoy this
article, please considersubscribing to LWN. Thank you
for visiting LWN.net!ByDaroc AldenAugust 11, 2025StarDictis a
GPLv3-licensed cross-platform dictionary application. It includes dictionaries
for a number of languages, and has a rich plugin ecosystem. It also has a
glaring security problem: while running on X11, using Debian's default configuration,
it will send a user's text selections over unencrypted HTTP to two remote servers.On August 4, Vincent Lefevrereportedthe problem to the oss-security mailing list and toDebian's bug tracker.
He identified it while testing his setup before the
upcoming Debian 13 ("trixie") release.
Installing StarDict will also
install thestardict-pluginpackage by default, because the former
recommends the latter. The plugins package contains a set of commonly used
StarDict plugins, including a plugin forYouDao, a Chinese search engine that supplies Chinese-to-English
translations. The plugin also contacts a second online Chinese dictionary,dict.cn.This would normally not be much cause for concern; of course a dictionary
program will include code to talk to dictionary-providing web sites. But one of
StarDict's features, which is also enabled by default, is its "scan"
functionality: it will watch the user's text selections (i.e. text highlighted
with the mouse), and automatically
provide translations as a pop-up. Taken together, the two features result in any
selected text being sent to both servers. This only occurs while StarDict is
open, but the application is designed to be left open in the background in case
the user needs a quick reference while reading.StarDict on Wayland doesn't have this problem, because Wayland
prevents applications from being
able to capture text from other applications by default. That does mean that it
breaks StarDict's scan feature, though.Xiao Sheng Wen, the Debian package maintainer for StarDict,didn't see a problemwith the behavior, noting that if a user doesn't want
to use the scan functionality or the YouDao plugin, both can be disabled.
Lefevrewasn't satisfiedwith that, saying:But this is not the whole point. Features with privacy concerns
should never be enabled by default (unless the feature is the
only purpose of the package, and such a package would never be
installed automatically — and even in such a case, there should
be a big warning first).In response, Xiaopointed outthatthe package descriptioncan be read by any
user who chooses to install the software, and it does mention the scan feature.
That said, I noted during my investigation that thedescriptionofstardict-plugindid
not mention that the YouDao plugin uses an online service instead of an offline
dictionary. Xiao suggested splitting the networked dictionary plugins into a
separate package, but was "not sure whether it's very necessary to do so".It is worth noting that the scan feature, while obviously a problem in this
context, is one of the reasons that a user might choose to use StarDict over an
alternative. Reading foreign-language media is often easier when words can be
sought in a dictionary with as little fuss as possible. From that perspective,
it makes sense that Xiao might not view the feature as problematic.Any user who did read the description of the package, and who knew what the
YouDao plugin would do, might nevertheless expect the resulting communication to
at least be encrypted. But the plugin actually reaches out to its backend
servers — dict.youdao.com and dict.cn — over unsecured HTTP. So, not only are
these servers sent any text the user selects, but anyone who can view traffic
anywhere along its path can see the same thing.This is not even the first time that StarDict has sent user selections to the
internet; the
same kind of problemwas
reportedby Pavel Machek in 2009 andagainby "niekt0" in 2015. The 2009 bug was solved by patching
the application's default configuration to disable networked dictionaries. That
appears to have worked for a time, but the YouDao plugin, which was added in
2016, does not respect the
configuration option. The 2015 problem was not fixeduntil
August 6 of this year(although the package was removed from Debian for
unrelated reasons for a few months from 2020 to 2021). That fix just removed thestardict_dictdotcn.soplugin, which also sent translation requests to
dict.cn and was later subsumed by the YouDao plugin,
from the package. In fairness to Xiao, he
was not the
StarDict maintainer in 2015 —that wasAndrew Lee — but Xiaoknewabout the 2015 bug since at least 2021, even if he didn't consider it a priority.According to Debian'spackage popularity
contest statistics,
only 178 people have
StarDict installed, down from around a thousand between 2009 and 2015.
That obviously doesn't capture people who have configured
their Debian system not to participate in the statistics collection, but it does
suggest there were a number of people who might have been broadcasting their text
selections to the internet for several years. Given that people copy and
paste passwords from their password managers, or select the text of sensitive
emails and documents during the course of editing, that should be a significant cause
for concern.Debian is a large distribution, containing tens of thousands of packages.
Moreover, because of its commitment to stability, a decent fraction of these
are older software with delayed or sporadic updates. The reality is that Linus's
law ("given enough eyeballs, all bugs are shallow") only holds up if
people are looking — and if, once they have looked, and have reported things,
the people who have taken up maintenance of the software actually agree that
there is a problem.Part of the justification for moving to Wayland over X11 is to make security
vulnerabilities relating to one application spying on another more difficult to
introduce. That obviously has to be balanced against the
cost of adapting to a new way of doing things, but it's not hard to see why so
many people are eager to make Wayland work. Maybe, in the future, StarDict's
default behavior would
have had little to no impact. Or maybe StarDict would have started asking for
special permissions to let it work on Wayland, and users would have accepted
those defaults the same way they currently do.Either way, the existence of serious security problems that can be
found, diagnosed, reported, and still remain unfixed is cause for concern. Linux
has long enjoyed a reputation for security; maintaining that reputation depends
on the developers, maintainers, and users of open-source software caring enough
to fix security problems when they arise.to post comments



### Beauty is all aroundPosted Aug 11, 2025 17:28 UTC (Mon)
 byjadedctrl(subscriber, #178426)
 [Link]I laughed out loud — I love this so much, it is truly insane this was default behavior. Not even HTTPS! This world really is beautiful.### memoryPosted Aug 11, 2025 17:37 UTC (Mon)
 byshironeko(subscriber, #159952)
 [Link] (1 responses)I remember using something like this back in the day on my XP machine. Nowadays it is truly wild to think that something like this would be a thing, at least make a tooltip and let the user confirm before sending stuff to the internet.### memoryPosted Aug 12, 2025 10:29 UTC (Tue)
 byaragilar(subscriber, #122569)
 [Link]Was it wordnet? I recall something like that existing, not sure if it had a similar issue to StarDict.### Seriously?Posted Aug 11, 2025 18:05 UTC (Mon)
 bywtarreau(subscriber, #51152)
 [Link] (6 responses)IMHO the problem is not even that it talks over clear HTTP, it's that it's sending those data in the first place! Who can imagine that your selected text which can include parts of e-mails, server configs, passwords etc would be sent to a cryptic remote site ? I'd say it's a great thing this was done in clear, as it allowed to instantly notice what was happening. CnC servers usually to that over encrypted channels precisely so that you don't know ;-)### Seriously?Posted Aug 11, 2025 18:31 UTC (Mon)
 byWol(subscriber, #4433)
 [Link] (4 responses)Exactly. What if you're at work dealing with "top secret IP". Call me cynical about that claptrap, but if it's sending chunks of confidential documents "in the clear" to chinese servers, that's a classic case of industrial espionage!Cheers,Wol### Seriously?Posted Aug 12, 2025 7:33 UTC (Tue)
 bychris_se(subscriber, #99706)
 [Link] (3 responses)> that's a classic case of industrial espionage!Nah, without any corroborating evidence, Hanlon's Razor applies. The feature itself will be considered useful by some people and my guess is that the authors don't care that much about privacy to begin with, but not because of malice, but more because of a different perspective.Doesn't make the impact of this issue any better, but I also don't think this kind of rhetoric is helpful at all.### Seriously?Posted Aug 12, 2025 8:37 UTC (Tue)
 byWol(subscriber, #4433)
 [Link] (2 responses)> Doesn't make the impact of this issue any better, but I also don't think this kind of rhetoric is helpful at all.Considering that the impact COULD be severe economic damage (remember, the US is unusual, in the rest of the world mere disclosure of economic secrets destroys any value), I don't think I'm being over the top.If I (as an outsider) notice that document, I can use it to block any patent application, for example. Okay, espionage implies intent, but the end result is near as dammit identical.Cheers,Wol### Seriously?Posted Aug 12, 2025 11:26 UTC (Tue)
 bymathstuf(subscriber, #69389)
 [Link] (1 responses)> (remember, the US is unusual, in the rest of the world mere disclosure of economic secrets destroys any value)If you're referring to the "first to file" policy used in the rest of the world…the US joined that party in 2013[1].[1]https://en.wikipedia.org/wiki/First_to_file_and_first_to_...### Seriously?Posted Aug 12, 2025 14:40 UTC (Tue)
 byWol(subscriber, #4433)
 [Link]No the rest of the world does NOT (and mostly never has, to the best of my knowledge) use "first to file".The rest of the world has used "filing must be the first publication" - if you accidentally let slip your filing documents today, and file tomorrow, that slip counts as prior art and will invalidate your application. It's happened! ("Publication" meaning "making available to the public", not necessarily our normal meaning of the word of "printing copies and selling them". Which includes accidentally losing a copy on the bus ...)As far as RoW is concerned, "first to file" is just an accidental byproduct of the first publication rule - if my application pre-dates yours, any conflict is resolved in my favour not because I filed before you, but because I published before you. That's why there's discussion every now and then about a "journal of inventions" - the whole point of which is to prevent any future patent applications on those ideas because of "first to publish".The problem is that if patent examiners mostly read only patent applications, they may well grant invalid patents because they are unaware of prior publications.Cheers,Wol### Seriously?Posted Aug 12, 2025 7:02 UTC (Tue)
 bydanieldk(subscriber, #27876)
 [Link]I was most surprised by the laissez-faire attitude of the Debian maintainer. As the article states (for worse or better) Linux is known for a security and privacy stance. Most Debian users I know highly value privacy and then the maintainer of this package goes "sends all clipboard data unencrypted to some server without really telling the user? <shrug>".I am glad that this was discovered (again).### Upstream is pretty surreal.Posted Aug 11, 2025 20:26 UTC (Mon)
 byHobart(subscriber, #59974)
 [Link] (2 responses)From the StarDict page, I followed a link (via Wayback Machine) to the no longer active homepage of the author.It's... unusual.https://web.archive.org/web/20230704145152/http://www.huz...### Upstream is pretty surreal.Posted Aug 12, 2025 0:43 UTC (Tue)
 byshironeko(subscriber, #159952)
 [Link] (1 responses)Did some digging, the author started behaving quite weird around 2008, converted to Buddhism, and went missing in 2011 and was later found. After that his condition got worse and worse, and around 2013-14 his communications online is pretty much fully schizophrenic. Not sure what happened to the site, from archive.org he's still active in 2023.### Upstream is pretty surreal.Posted Aug 12, 2025 0:54 UTC (Tue)
 byshironeko(subscriber, #159952)
 [Link]Just noticed today is the day Terry died, RIP.### Privacy issues in Linux distrosPosted Aug 12, 2025 4:14 UTC (Tue)
 bypabs(subscriber, #43278)
 [Link]There are numerous privacy issues in distros, some known, most probably unknown, some examples from Debian:https://wiki.debian.org/PrivacyIssuesAs an example, Evolution/Balsa/Geary have privacy issues with HTML email:https://www.emailprivacytester.com/badClientsLuckily there are things like opensnitch that can block some of these issues:https://github.com/evilsocket/opensnitch### Distro privacy policies?Posted Aug 12, 2025 4:18 UTC (Tue)
 bypabs(subscriber, #43278)
 [Link]I wonder how many distros have privacy policies for the packages they distribute, and privacy support for fixing those issues like they would fix security issues.### Security policy and secure-by-defaultPosted Aug 12, 2025 5:07 UTC (Tue)
 bygdt(subscriber, #6284)
 [Link]The article's linked Debian BTS is worth a read to see very differing viewpoints of security, and particularly around the security policy of secure-by-default (which has been a typical policy in Unix-like operating systems since the events of 1988. I can't see a mention of in the Debian Policy Manual, the main guidance for packagers; easily could have missed it though).### I wrote my own stardict comatible library and appPosted Aug 12, 2025 8:17 UTC (Tue)
 bymetan(subscriber, #74107)
 [Link]I never liked the stardict apps so I wrote a simple library[1] to do lookups on the stardict formatted dictionaries that includes simple command line tool for looking up translations. And there is also very simple graphical app build on the top of the library [2]. If anyone is interested packages could be grabbed from OBS [3].[1]https://github.com/gfxprim/libstardict[2]https://github.com/gfxprim/gpdict[3]http://gfxprim.ucw.cz/packages.html### GDPR violationPosted Aug 12, 2025 10:54 UTC (Tue)
 byhelge.bahmann(subscriber, #56804)
 [Link] (1 responses)Considering that the sensitivity of clipboard data is rather non-specific (FWIW it might contain medical data), the feature would have likely required _explicit_ informed consent (even if maintainer considers installing the package as "consent", that would merely be implicit). Such things can therefore likely not legally be distributed at all in EU without somehow showing a consent screen.I presume it is an honest error by the maintainer, but when trying to justify external data processing it is important to also look at it from this POV in addition to moral obligations.### GDPR violationPosted Aug 12, 2025 14:28 UTC (Tue)
 byWol(subscriber, #4433)
 [Link]> (even if maintainer considers installing the package as "consent", that would merely be implicit)And such consent must be given by the data SUBJECT, not the data PROCESSOR, so in this particular example, consent is probably not even possible ...Cheers,Wol





Copyright © 2025, Eklektix, Inc.Comments and public postings are copyrighted by their creators.Linux is a registered trademark of Linus Torvalds
