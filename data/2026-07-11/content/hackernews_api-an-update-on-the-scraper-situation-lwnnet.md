---
title: An update on the scraper situation [LWN.net]
url: https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/
site_name: hackernews_api
content_file: hackernews_api-an-update-on-the-scraper-situation-lwnnet
fetched_at: '2026-07-11T19:27:25.791522'
original_url: https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/
author: chmaynard
date: '2026-07-10'
description: An update on residential proxies and the scraper situation
tags:
- hackernews
- trending
---

### Welcome to LWN.netThe following subscription-only content has been made available to you 
by an LWN subscriber. Thousands of subscribers depend on LWN for the 
best news from the Linux and free software communities. If you enjoy this 
article, please considersubscribing to LWN. Thank you
for visiting LWN.net!ByJonathan CorbetJuly 10, 2026Our article "Fighting the AI scraper bot
scourge", published in early 2025, discussed the problem of widespread
scraping of web sites in search of training data for large language models
and related projects. This activity overwhelms sites with traffic. Over a
year after that article is published, the problem is still growing. The
hammering of sites by shadowy actors has reached new heights, and the open
web is becoming increasingly difficult to maintain. Where is this traffic
coming from, and what can be done about it?#### Residential proxiesAs was described last year, scraper attacks come from a huge number of
sources across the net. It is not unusual to see coordinated requests from
millions of unique IP addresses over the course of a few hours, each of
which hits the site at most two or three times. Attacker-controlled data,
such as the user-agent field, is entirely fictional; each hit is meant to
look like just another human with a web browser. There are ways to tell
the difference — the bots usually do not fetch images or CSS, for example —
but, by the time that determination is made, the address in question will
not be used again. Blocking the address at that point is just a waste of
time.This traffic comes predominantly from residential and mobile networks,
directed by central command-and-control nodes. Software is installed on
ordinary systems that takes orders from a control node, fetches web pages
on demand, and forwards the resulting data back to the controller. Much of
the time, this activity occurs without the knowledge or consent of the
owner of the device in question. The term "residential proxies" is used to
describe systems that are used in this way.There are a few different (on the surface, at least) types of operator
running residential-proxy networks to attack web sites. One type is purely
criminal, running scrapers on systems that have been compromised with some
sort of malware. At the beginning of the year, Googleacted
to take down a bot network called IPIDEAand provided a lot of
information about how these operations work. The shutdown of IPIDEA
correlated with a significant reduction in scraper traffic here at LWN;
things were relatively peaceful for a few months. That period of peace has
since come to an end, though.More recently, media-streaming devices have beenidentifiedas a major carrier of malicious scraping software. Sometimes the devices
are compromised at the source; other times, they are just poorly secured
and easily compromised after the fact.The second sort of operator works more overtly, pretending to a degree of
legitimacy and offering "ethically sourced" IP addresses. A company called
Bright Data is one of the most prominent of these; it happily advertises
its prowess at getting around web-site access controls and traffic limits.
Bright Data offers a "free" VPN service; all that is needed is for the user
to give Bright Data the ability to route traffic through the user's device
— to become a part of the company's residential-proxy network, in other
words. Every phone or other device that makes use of this VPN becomes yet
another endpoint that will be used to attack web sites.There are many other examples of this type of operator out there; often
they offer a library that app developers can link into their offerings and
be paid for hijacking their users' network connections. One of them even
sent us a query about running an ad for its SDK on LWN; that was, it
suffices to say, a short conversation. In general, these companies range
from those that aspire toward some appearance of legitimacy, advertising
"GDPR compliance" for example, to others that are just overtly sleazy.While these residential-proxy networks are used for web-site scraping, it
is worth emphasizing that these operators have the ability to run code that
accesses resources on whatever networks millions of devices happen to be
connected to. To assume that this type of access would only be used for
scraping would be naive at best.Then, of course, there are the high-profile companies developing models as
their core business. These companies do their own scraping; the traffic
that can be easily attributed to them is clearly identified in the
user-agent field and, as a general rule, observes measures likerobots.txt. They, too, will scrape an entire site, repeatedly,
seemingly on the theory that articles written in 2003 might somehow have
changed in the last day, but they do not generate overwhelming amounts of
traffic from millions of systems and are not the biggest problem.What isn't clear is who is using the residential proxies;somebodyis paying them to run these attacks on web sites. There is no
evidence (that I am aware of) that the frontier-model companies are using
those networks. If it were to turn out that theyaredoing so, though,
the increase in global astonishment would barely register. Those companies
are feeding their models somehow, they are not forthcoming about how they
get their training data, and they have not distinguished themselves with
their level of respect toward content creators — or toward anybody who
might have concerns about their operations.For every public model, though, there must be a vast number of undercover
models. Many companies are surely trying to build their own; after all, we
are reliably informed that AI is going to take over the world and the
companies that come out on top of that race will be worth untold amounts of
money. There must be shadowy government agencies in many countries working
on their own models and groping for training data wherever they can find
it. Large-scale criminal organizations (to the extent that they are
distinct from governments) probably also want to have their own models.
These tools are seen as weapons, and there is an arms race underway. The
Internet as a whole is caught in the crossfire.#### Defending the open InternetIn response to all of this, web-site operators have been scrambling to
defend their sites while minimizing the effect on their actual users.Anubis, which attempts to fend off scrapers by
requiring a proof of work, is now widespread. Other sites use commercial
services, which sometimes make themselves known with a "prove you are
human" button. Or sites force users to pick out squares containing
streetlights (but only those with LED bulbs), place puzzle pieces, or hum a
song while holding down the space bar. Many site features have been placed
behind login gates or paywalls. Some sites attempt to actively poison the
data sent to scrapers with tools likeiocaine.Both the need to set up and maintain these mechanisms, and the requirement
that users cope with them to access a web site, constitute a heavy tax
placed on the world as a whole by scrapers and those who pay them.Recently, LWN was subjected what was, by far, the heaviest scraper attack
yet. Thanks to the defenses that have been implemented, the site bore the
traffic well enough that most actual readers probably did not even notice.
There have been requests to describe the measures we have taken to defend
the site; for obvious reasons we do not wish to discuss them in any detail.
It is an arms race at this level too.What wecansay is that we have tried to minimize the impact on real
readers as much as possible. We have not gone with tools like Anubis,
partly because it causes annoying delays for those trying to get to the
site, but also partly because it seems inevitable that the scrapers will
eventually find their way around it. Indeed, there are some indications
that is already happening. A proof-of-work requirement is not a huge
obstacle when you have millions of other people's machines to do the work
on.There is also a desire to not impede the operation of legitimate search
engines, the Internet Archive, and other such groups. Some sites may add
explicit allowlists to, for example, give the dominant search engine access
to the site. Such measures have the effect of further entrenching a
monopoly that already serves us poorly and should be avoided. We have,
thus far, succeeded in that.Wehaveaggressively optimized parts of the site, and found ways to
minimize expensive operations during times when the site is under attack.
Anonymous readers may occasionally encounter one of those measures;
logged-in users will not. Amusingly, the response time when the site is
under attack is often better than during the calm times, when the defensive
measures are dormant. We have learned better than to think that the
problem is solved, though; consideration must be given to our next steps
once the current measures are no longer effective.On July 2, Googleannouncedthat it had, in coordination with the US Federal Bureau of Investigation
and others, taken down a residential-proxy network called "NetNut". For
the time being, that action would, indeed, seem to have succeeded in
reducing the level of scraper attacks somewhat. Experience shows, though,
that this welcome peace will only last so long. Google takes pains to
point out that its Play Store will now check for NetNut-infected apps, but
all of the major vendors are silent on the topic of why it is so easy to
put apps with residential-proxy functionality into their app stores.It would be good to find a more lasting solution before the entire Internet
is driven behind defensive walls, and the open network that inspired so
much creativity is lost. The industry that is driving these attacks seems
entirely at ease with turning independent web sites into smoking craters
after having pillaged their contents — an attitude that extends to the
planet and its economies as well. Some of us, though, object to that idea
and will fight against it. Someday, with luck, the world as a whole will
decide to hold the companies behind large language models and related
technologies to a minimal ethical standard. Until then, though, this
behavior will continue, and we will have no choice but to defend ourselves
against it.to post comments### How to avoid running a residential proxy (especially on Android phones)?Posted Jul 10, 2026 15:59 UTC (Fri)
 byKJ7RRV(subscriber, #153595)
 [Link] (6 responses)How can one avoid unintentionally running one of these proxies? It's easy enough on a desktop/laptop to just check for unexpected network usage (and I doubt Linux machines are a common target of these Trojans, not to mention the fact that most Linux users get software mostly or entirely from distro repos), but for those who use proprietary apps on smartphones (Android, in my case), where it's not always as easy to monitor network usage, is there a way to scan installed apps for these malicious SDKs?### How to avoid running a residential proxy (especially on Android phones)?Posted Jul 10, 2026 16:25 UTC (Fri)
 byfarnz(subscriber, #17727)
 [Link]If you're using Google Play Services, turn on Play Protect and have that scan every so often - this will catch any apps that Google has found contain one of these proxies.Other than that, you can ask Android to tell you how much mobile data an app used; go to "Settings", then "Apps", and it's in the "App Info" screen for individual apps. You can also disable "Background data" if you're suspicious of an app - that stops it using data when you don't have it open and are on mobile; IIRC, this also covers WiFi networks set as "metered", but ICBW on that one.### How to avoid running a residential proxy (especially on Android phones)?Posted Jul 10, 2026 20:26 UTC (Fri)
 bymirabilos(subscriber, #84359)
 [Link]TEMU is rumoured to contain one. AFAIHH it just runs in the foreground while the device users browse its marketplace.Note this is hearsay. I have not installed that äpp nor sniffed its traffic myself. But it was the first one where I heard about what is now called residential proxies, via “trojaned” äpps, and from multiple sources.I’m sure the “link fetchers” from GAFAM äpps can also occasionally do that…### How to avoid running a residential proxy (especially on Android phones)?Posted Jul 10, 2026 21:42 UTC (Fri)
 byrgmoore(✭ supporter ✭, #75)
 [Link] (1 responses)How can one avoid unintentionally running one of these proxies?Some of the other posters have commented on how to avoid these kinds of proxies on your own system, but I want to point out that individual action won't be enough to solve the broader problem. I don't want to discourage anyone from trying to keep their own system clean, but we will never get rid of these kinds of proxies by encouraging each person with a mobile device to avoid them. You need to block access to a large majority of the available devices to make any real progress, and voluntary programs that involve real effort are never going to get that level of participation. This stuff needs to be taken care of at the system level- getting the apps out of app stores, making this kind of thing clearly illegal and prosecuting the offenders, etc.- not the individual user level.### How to avoid running a residential proxy (especially on Android phones)?Posted Jul 10, 2026 23:40 UTC (Fri)
 byKJ7RRV(subscriber, #153595)
 [Link]Thank you for the reminder! I completely understand that, and apologize for any impression my comment may have given that this is primarily a problem to be solved by individual users; that was certainly not my intention. I just want to make sure I am not personally contributing to the problem, however small any one user's part may be; I'm not asking everyone with a smartphone to research every app they use.### How to avoid running a residential proxy (especially on Android phones)?Posted Jul 11, 2026 3:04 UTC (Sat)
 byduelafn(subscriber, #52974)
 [Link]I can't answer the monitoring issue, but NetGuard (on f-droid or play store) can block network access per-app. I fully deny network access to about a third of my apps that want network, about another third get access only when the screen is on. Not a perfect fix, but a nice layer of protection.### How to avoid running a residential proxy (especially on Android phones)?Posted Jul 11, 2026 3:15 UTC (Sat)
 bymarcH(subscriber, #57642)
 [Link]For apps you use very rarely but don't want to keep uninstalling and re-installing (the latest, different version), there is a "pause app" button available when you long-press the app. Except... it inexplicably pauses the app only for 1 day :-(But there is another, permanent option. Long press -> App Info -> Screen Time! You can set it to zero and it stays at zero. It's called "Screen Time" but it seems to block background usage too, hopefully some Android developer can confirm.(and yes of course this sort of advice is only useful for techies and will do nothing to save the open web)### Thanks for your efforts and keep up the good work!Posted Jul 10, 2026 16:08 UTC (Fri)
 bywtarreau(subscriber, #51152)
 [Link] (2 responses)Hi Jon,I think that many of us here are totally aware of the problem these bots and proxies are causing to web sites like this one, and the difficulties in fighting them. At least I can say that I haven't noticed anything abnormal on the site here, so your actions were fine from the user experience perspective. Thanks for this!You're right, it's important never to publicly explain the counter-measures that you apply. Very often some are extremely simple and effective (some easy tricks I've deployed 9 months ago that I imagined would only last one week are still working fine). Also they're often very specific to the site and would hardly adapt to other ones (except for the main principle), so there's little to share by explaining everyone how your specific site is fighting these.I noticed a 30% drop of traffic on July 2nd, after a 50% one on June 25th that I couldn't explain (mostly attributed to user-agent "sleepbot"). So yes, it seems that such networks are progressively getting dismantled, probably to re-appear somewhere else soon, given that infected browsers (and their unsuspecting users) are just waiting for another C&C to take care of them :-/I must confess I'm a bit worried about the risk of losing a lot of legit content indexing on the net in the coming years due to installed counter-measures against non-humans. If sites cannot be found via search engines it will become a problem. All this due to AI startups racing in training their own models (or variants).Maybe it would work better to set up a static central registry of the whole internet's contents that could be scraped by such companies as much as they want without killing small web sites. It could still take a lot of time before we start to see something like this happen though.### Thanks for your efforts and keep up the good work!Posted Jul 10, 2026 17:15 UTC (Fri)
 bydaroc(editor, #160859)
 [Link] (1 responses)The central registry you propose sort of exists in the form of Common Crawl:https://commoncrawl.org/The idea is that you contribute resources to their project, they have _one_ scraper that downloads web content in a polite way (respecting rate limits and robots.txt), and then anyone who wants to can make use of the scraped content without having to re-scrape it.There are some problems with the approach, but I'm generally pretty happy when I see Common Crawl go by in the server logs because I know that's a bunch of unrelated projects that don't need to send us multiple requests.### Thanks for your efforts and keep up the good work!Posted Jul 10, 2026 17:46 UTC (Fri)
 bywtarreau(subscriber, #51152)
 [Link]> The central registry you propose sort of exists in the form of Common Crawl:https://commoncrawl.org/Oh, thanks for the link, I wasn't aware. I'll try to make sure not to block that one!### Preventing this at the app store level is hardPosted Jul 10, 2026 20:42 UTC (Fri)
 byroc(subscriber, #30627)
 [Link] (4 responses)> all of the major vendors are silent on the topic of why it is so easy to put apps with residential-proxy functionality into their app stores.Google's rules already forbid non-user-authorized "residential proxies":https://support.google.com/googleplay/android-developer/a...But if the user gives genuine consent to it, should they still be banned? That's a tough call.Of course developers can and do violate those rules. Then the problem is that it's not really possible in general to detect that code is going to break those rules just by inspecting it. So how do you detect violations other than by people reporting them and then shutting them down after the fact? That's roughly what happens now and it's better than nothing, but still whack-a-mole.### Preventing this at the app store level is hardPosted Jul 10, 2026 22:29 UTC (Fri)
 byrgmoore(✭ supporter ✭, #75)
 [Link] (3 responses)Google's rules already forbid non-user-authorized "residential proxies" But if the user gives genuine consent to it, should they still be banned? That's a tough call.No, they shouldn't be allowed. Banning them is at least as much about protecting the whole internet from their pernicious effects as it is about protecting the individual user, so it shouldn't be up to the individual user any more than emissions controls should be up to the individual driver.I would also argue that for any user to give "genuine consent", they would need to be given the option to have the same app without the proxy. If you let the author condition use of their app on accepting the proxy, consent is at least somewhat coerced.### Preventing this at the app store level is hardPosted Jul 10, 2026 23:11 UTC (Fri)
 byWol(subscriber, #4433)
 [Link]> I would also argue that for any user to give "genuine consent", they would need to be given the option to have the same app without the proxy. If you let the author condition use of their app on accepting the proxy, consent is at least somewhat coerced.And do they ask the VICTIM for consent? Of course not, they know consent would be refused.Let's say I run a web server. The whole point of this scheme is bypass/dodge my attempts to prevent my site being DoS'd by scrapers. Whether it's criminal or not (in Europe it probably is), the whole point of this is to attack my server in a manner to which "you knew or should have known" I would have refused to consent to.I find it hard to think of any use to which such a network would be put, that is not in violation of England's Computer Fraud And Abuse Act. Whether said act could be enforced is another matter :-( , but consenting to your computer being used for such things could also be criminal under the "going equipped to ..." rules ...Cheers,Wol### Preventing this at the app store level is hardPosted Jul 11, 2026 5:28 UTC (Sat)
 byroc(subscriber, #30627)
 [Link]The "I should be able to run whatever code I want on my device" people would surely object.### Preventing this at the app store level is hardPosted Jul 11, 2026 14:49 UTC (Sat)
 byibukanov(subscriber, #3942)
 [Link]What about offering a cheaper version in return for the user consent to allow to use their network?I also wonder why does not BrightData not offer users just to run their software for money on devices? Maybe it will be the next step.### IP blocks should be neither authentication nor authorizationPosted Jul 10, 2026 20:59 UTC (Fri)
 byquotemstr(subscriber, #45331)
 [Link] (4 responses)> more lasting solution before the entire Internet is driven behind defensive wallsIt already is in large part. Have you tried browsing the internet from outside a well-known residential or end-user-VPN IP block? Tons of sites block access out of the gate or put up so many "click the traffic lights" gates that they might as well have blocked you.Residential VPNs are, yes, often scummy, but also an understandable reaction to much of the internet using routing tables as a proxy for proof of humanity. You can't stamp them out, either: there will always be people willing to trade their home bandwidth for trinkets. You can't stop them without stamping out general-purpose computing altogether, and I don't think anyone wants that.What we need instead is an open protocol through which network clients can provide proof of interactive humanity under zero knowledge in such a way as to resist cloning and Sybil attacks. I believe recent advances in zkVMs and remote attestation make such a protocol possible. If we had it,1. residential VPNs would cease to be special and incentives for scummy tricks would disappear,2. assurance of humanity could shift from annoying interstitials to automatic protocol exchange (because we could prove recent human interaction end-to-end authenticated from hardware without sacrificing privacy), and3. site operators could, in principle, create a market for non-interactive access permits (e.g. under an anonymous cap-and-trade scheme), naturally rate-limiting accesses while avoiding the monopoly-reinforcing effects of just whitelisting IP blocks owned by this or that archive or search engine.Interactive users couldn't sell their interactivity for trinkets without setting up robots to manipulate their input devices or doing tedious link-clicking themselves. Channel- and hardware-binding would mitigate proxy attacks, again anonymously. Remote attestation doesn't have to be a privacy nightmare. It can *enable* privacy!Such a scheme would be compatible with free software operating systems too, since input attestation would be pass-through. You'd just prove, remotely, that the same TPM generated both the input attestation and your TLS session key. Linux can drive this hardware just fine.Privacy-preserving protocols like this have become practical just recently, over the past few years. It's a shame we haven't yet begun to explore their potential. The alternative is something like the Cloudflare Monetization Gateway [1], which accomplishes similar goals, but without the privacy or the democracy. A world where Cloudflare becomes de-facto internet gatekeeper is a worse world than one with an open attestation ecostystem.[1]https://blog.cloudflare.com/monetization-gateway/### UI automation is necessary for accessibilityPosted Jul 11, 2026 4:11 UTC (Sat)
 byDemiMarie(subscriber, #164188)
 [Link] (1 responses)Accessibility tools work by automating user interactions. In fact, one of Windows’s accessibility frameworks is called “Microsoft UI Automation”.Unless one imposes an allowlist of accessibility tools, one won’t be able to use hardware attestation to prevent automating a user’s actions. What one can do is tie them to a user identity, and therefore rate-limit or ban abusive users.### UI automation is necessary for accessibilityPosted Jul 11, 2026 6:08 UTC (Sat)
 byquotemstr(subscriber, #45331)
 [Link]> Unless one imposes an allowlist of accessibility toolsAccessibility tools translate one form of user input into another. They don't generate interactions out of thin air. They can carry through attestations made against their original inputs. Besides: what you really want to do is attest physical human presence, and there are multiple ways to do that, of which using attested input stamps is just one.> What one can do is tie them to a user identityRequiring identity linkability for everyone is far worse than complicating accessibility tools for a few.### IP blocks should be neither authentication nor authorizationPosted Jul 11, 2026 11:02 UTC (Sat)
 bymuase(subscriber, #178466)
 [Link]> Privacy-preserving protocols like this have become practical just recently, over the past few years. It's a shame we haven't yet begun to explore their potential. The alternative is something like the Cloudflare Monetization GatewayI think a maybe better interesting alternative – funnily enough also from Cloudflare – is CAP:https://developers.cloudflare.com/fundamentals/reference/...CAP uses WebAuthn to basically do two things: see if your device has an attested WebAuthn hardware authenticator it can trust, and then it ask the trusted hardware to perform biometric user authentication.And this is kinda clever, because this means it simply uses WebAuthn as an open standard, and everyone can implement it independently of Cloudflare. The only downside is that with this approach the same user can be re-identified; I think an extension to WebAuthn could help with that.### IP blocks should be neither authentication nor authorizationPosted Jul 11, 2026 14:15 UTC (Sat)
 byfraetor(subscriber, #161147)
 [Link]Mozilla has been exploring this recently with anonymous credentials to allow different services to assert identity via zero-knowledge proofs.It essentially acts as a web-wide rate limit, under the theory that bot traffic is problematic not because it is automated, but rather because a single bot operator can produce way more traffic than an individual person would.High level post on the goals:https://blog.mozilla.org/en/firefox/privacy-security/keep...And the Hacks post that goes into the technical details:https://hacks.mozilla.org/2026/06/pact-anonymous-credenti...### Anubis doesn't seem to be working anymore herePosted Jul 10, 2026 22:34 UTC (Fri)
 bykoverstreet(subscriber, #4296)
 [Link] (6 responses)I started seeing a ton of AI crawlers hammer all my git endpoints, and they're going right past the anubis checks; it seems a least some crawlers are using full web browsers that can do the proof of work.Ouch.So I'm back to a script that I run regularly that just scrapes the hammering IPs from the nginx log and iptables blocks them...### Anubis doesn't seem to be working anymore herePosted Jul 11, 2026 0:21 UTC (Sat)
 byjoey(guest, #328)
 [Link] (5 responses)I'm coming to the conclusion that it doesn't make sense to have a whole public gitweb or cgit or similar on the web anymore. There are a few pages of that are valuable to provide to my users, like the most recent commit log and the current file tree, and a things like commits that I link to specifically from blog posts. But the ability to explore deeply through the whole git history is a marginal value, and the value proposition for that has overall gone negative. The interested user can make their own clone and use their own tools on it.LWN's mailing list archives may have a similar value distribution.### Anubis doesn't seem to be working anymore herePosted Jul 11, 2026 0:58 UTC (Sat)
 bykoverstreet(subscriber, #4296)
 [Link] (3 responses)I use cgit pretty frequently, and my users are perusing it regularly too, so it's pretty painful here.Realistically, the solution needs to be some kind of throttling baking into the webserver, and a more efficient cgit implementation with some caching would help a lot. I've hit quite a few perf issues with git, I'm hoping now that they're starting to use Rust in the core codebase that'll make performance work easier.Definitely not excited by the prospect of yet more sysadmin work, though.And. If web access to too many git repos gets shut down I have to imagine the AI companies would switch to just chain cloning repos with no caching. Everything they're doing is just really anti social.### Anubis doesn't seem to be working anymore herePosted Jul 11, 2026 3:32 UTC (Sat)
 bydanielbaumann(subscriber, #38804)
 [Link] (2 responses)I started to use basic auth with a "dummy" user and password that is written on the webpage. It's unexpected/inconvenient for non-regular/first-time/one-time-only human visitors, but it works for now.### Anubis doesn't seem to be working anymore herePosted Jul 11, 2026 5:27 UTC (Sat)
 bykoverstreet(subscriber, #4296)
 [Link]Heh, the cat and mouse games are getting out of hand...### Anubis doesn't seem to be working anymore herePosted Jul 11, 2026 14:02 UTC (Sat)
 bydskoll(subscriber, #1630)
 [Link]Yes, I do the same Basic Auth trick with the username and password disclosed on the front page and it seems to be working very well for now. I check the user agent and if it's git, I don't require the authentication, so agit cloneworks without authentication. At some point, I suspect the scrapers will catch on and we'll be one step further along the arms race. 🙁### Dumb transport is very efficientPosted Jul 11, 2026 4:04 UTC (Sat)
 byDemiMarie(subscriber, #164188)
 [Link]The dumb transport just requires a static file server, which means it is vastly more efficient on the server side unless it (for some reason) requires far more bandwidth.### Have your cake and eat it tooPosted Jul 11, 2026 3:31 UTC (Sat)
 bymarcH(subscriber, #57642)
 [Link] (2 responses)> Google takes pains to point out that its Play Store will now check for NetNut-infected apps, but all of the major vendors are silent on the topic of why it is so easy to put apps with residential-proxy functionality into their app stores.Amusingly, the interwebs were up in arms about the recent "Android Developer Verification" changes. In summary:- it's too easy to publish random stuff on the app stores. Yet:- it's increasingly difficult to publish random stuff on the app stores!How about: security is extremely hard? Security as in: blocking and catching bad people while not bothering honest people (low security "friction").Even harder on the wild, borderless internet. Amazing all this has been working at all. With hindsight, maybe this was all some kind of short-lived miracle... Lucky us who lived at that time and could experience it!### Have your cake and eat it tooPosted Jul 11, 2026 9:23 UTC (Sat)
 byshalem(subscriber, #4062)
 [Link]The problem with "Android Developer Verification" is not Google enforcing this for the official Android Playstore, that is fine. The problem is Google abusing their Android monopoly to force "Android Developer Verification" to also apply to apps loaded through third party stores like fdroid.Although this is a slippery slope I could live with Google using their gatekeeper capabilities to only allow third party app stores which have gone through some sort of registration process with Google to avoid creating a third party app store malware loophole.Google should have no say over what goes into third part app stores, that should be up to the third party app-stores. This will likely require an unfortunately unavoidable added process for Google to revoke the "app store" capability from badly behaving add stores.### Have your cake and eat it tooPosted Jul 11, 2026 14:07 UTC (Sat)
 byZentaya(guest, #185040)
 [Link]Unfortunately android developer verification is not going to help with netnut infested apps.Malware infected apps are rampant in the play store even now. ADV will not help with that.What it will do is prevent apps installed from f-droid and other sources, that are much less likely to contain malware anyway.