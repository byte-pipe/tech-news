---
title: Apple’s Browser Engine Ban Persists, Even Under the DMA - Open Web Advocacy
url: https://open-web-advocacy.org/blog/apples-browser-engine-ban-persists-even-under-the-dma/
site_name: hackernews_api
fetched_at: '2025-07-14T23:06:52.412113'
original_url: https://open-web-advocacy.org/blog/apples-browser-engine-ban-persists-even-under-the-dma/
author: yashghelani
date: '2025-07-14'
description: Apple's Browser Engine Ban Persists, Even Under the DMA
tags:
- hackernews
- trending
---

# Apple’s Browser Engine Ban Persists, Even Under the DMA

14th of July 2025

Written by OWA

* #Policy
* #Apple
* #Eu
* #Dma
* #Browserengine

TL;DR: Apple’s rules and technical restrictions are blocking other browser vendors from successfully offering their own engines to users in the EU.At the recent Digital Markets Act (DMA) workshop, Apple claimed it didn’t know why no browser vendor has ported their engine to iOS over the past 15 months. But the reality is Apple knows exactly what the barriers are, and has chosen not to remove them.

Safari isthe highest margin productApple has ever made, accounts for 14-16% of Apple’s annual operating profit and brings in $20 billion per year insearch engine revenuefrom Google. Foreach 1% browser market sharethat Apple loses for Safari,Apple is set to lose $200 million in revenue per year.

Ensuring other browsers are not able to compete fairly is critical to Apple’s best and easiest revenue stream, and allows Apple to retain full control over the maximum capabilities of web apps, limiting their performance and utility to prevent them from meaningfully competing with native apps distributed through their app store. Consumers and developers (native or web) then suffer due to a lack of competition.

This browser engine ban is unique to Apple and no other gatekeeper imposes such a restriction. Until Apple lifts these barriers they are not in effective compliance with the DMA.

We had the opportunity to question Apple directly on this at the 2025 DMA workshop. Here's how they responded:

Share and join the conversation:X/Twitter,Mastodon,LinkedIn,Bluesky.

## #Quick Background

As a quick background to new readers, we (Open Web Advocacy) are a non-profit dedicated to improving browser and web app competition on all operating systems. We receive no funding from any gatekeeper, nor any of the browser vendors. We have engaged with multiple regulators including in theEU,UK,Japan,Australiaand theUnited States.

Our primary concern isApple’s rule banning third-party browser engines from iOSand thus setting a ceiling on browser and web app competition.

We engaged extensively with the UK’s CMA and the EU on this topic and to our delight specific text was added to the EU’s Digital Markets Actexplicitly prohibiting the banning of third-party browser engines,and stating that the purpose was to prevent gatekeepers from determining the performance, stability and functionality of third party browsers and the web apps they power.

The first batch of designated gatekeepers Apple, Google, Meta, Amazon, Bytedance, Microsoftwere required to be in compliance with the DMA by March 7th, 2024.

Apple’s compliance did not start well. Faced with the genuine possibility of third-party browsers effectively powering web apps,Apple's first instinct was to remove web app support entirely from iOSwith no notice to either businesses or consumers. Under significant pressure from us and the Commission,Apple canceled their plan to sabotage web apps in the EU.

Both Google and Mozillabegan porting their browser engines Blink and Gecko respectively to iOS. Other browser vendors are dependent on these ports to bring their own engines to their browsers iOS, as their products are typically soft forks (copies with modifications) of Blink or Gecko.

However there were significant issues with Apple’s contract and technical restrictions that made porting browser engines to iOS “as painful as possible” for browser vendors.

Apple’s proposals fail to give consumers viable choices by making it as painful as possible for others to provide competitive alternatives to Safari [...] This is another example of Apple creating barriers to prevent true browser competition on iOS.Damiano DeMonte - Mozilla

Many of Apple’s barriers rely on vague security and privacy grounds for which Apple has published no detailed technical justification for both their necessity and proportionality. As the US’s Department of Justice wrote in their complaint:

In the end, Apple deploys privacy and security justifications as an elastic shield that can stretch or contract to serve Apple’s financial and business interests.DOJ Complaint against Apple

In June, 2024we published a paper outlining these barriers.

## #Key Barriers Apple has put in Place

We recognize under the DMA that we've been forced to change. And we have created a program that keeps security and privacy in mind, that keeps the integrity of the operating system in mind, andallows third parties to bring their browser engine, Google, Mozilla, to the platform. And for whatever reason, they have chosen not to do so.Kyle Andeer - Apple - Vice President Apple Legal(emphasis added)

At the DMA workshop last week, we directly raised with Apple the primary blocker preventing third-party browser engines from shipping on iOS. Apple claimed that vendors like Google and Mozilla have“everything they need”to ship a browser engine in the EU and simply"have chosen not to do so”.

Apple has been fully aware of these barriers since at least June 2024,when we covered them in exhaustive detail. Multiple browser vendors have also discussed these same issues with Apple directly. The suggestion that Apple is unaware of the problems is not just ridiculous, it’s demonstrably false.Apple knows exactly what the issues are. It is simply refusing to address them.

The most critical barriers that continue to block third-party engines on iOS include:

* Loss of existing EU users: Apple forces browser vendors to create entirely new apps to use their own engine, meaning they must abandon all current EU users and start from scratch.
* Web developer testing: Apple allows native app developers outside the EU to test EU-specific functionality, but offers no equivalent for web developers to test their software using third-party browser engines on iOS. Apple stated during the conference to expect updates here but provided no details.
* No updates on long trips outside EU: Apple has not confirmed they will not disable browser updates (including security patches) if an EU user travels outside the EU for more than 30 days. This, far from being a security measure, actively lowers users' security by depriving them of security updates.
* Hostile legal terms: The contractual conditions Apple imposes are harsh, one-sided, and incompatible with the DMA’s requirement that rules for API access can only be strictly necessary, proportionate security measures.

Apple has addressed two of the issues we raisedin our original paper:

* Dual engine support: Apple now allows browsers to include both WebKit and their own engine in the same app. This is essential for introducing a new engine to the platform while maintaining fallback compatibility.
* Allow browser vendors to test their own browsers: Apple now permits browser vendors to test their own engines outside the EU. Yes, you read that correctly,Apple initially attempted to block Google, Mozilla, and Microsoft from testing their own browsers.

However, the most critical barrier remains firmly in place: Apple still forces browser vendors to abandon all their existing EU users if they want to ship a non-WebKit engine.This single requirement destroys the business case for porting an engine to iOS.Building and maintaining a full browser engine is a major undertaking. Requiring vendors to start from scratch in one region (even a region as large as the EU), with zero users, makes the investment commercially nonviable.

Instead, transaction and overhead costs for developers will be higher, rather than lower, since they must develop a version of their apps for the EU and another for the rest of the world. On top of that, if and when they exercise the possibility to, for instance, incorporate their own browser engines into their browsers (they formerly worked on Apple's proprietary WebKit), they must submit a separate binary to Apple for its approval. What does that mean exactly?That developers must ship a new version of their app to its customers, and 'reacquire' them from zero.Alba Ribera Martínez - Lecturer in Competition Law and Digital Markets(emphasis added)

Those are the major blockers to browser vendors porting their own engines to iOS. The list of changes that we believe Apple needs to make to be compliant with the DMA with respect to browsers and web apps on iOS is far larger, and we outline them in detail at the end of the article.

Perhaps the most important of these isthe ability for browsers to install and manage web apps with their own engines. Something that has been directly recommended by both theUK’s MIR investigationand theUK’s SMS investigations.

## #Why Does this Matter?

Gatekeepers can hamper the ability of end users to access online content and services,including software applications. Therefore, rules should be established toensure that the rights of end users to access anopen internetare not compromised by the conduct of gatekeepers.Recital 54 - Digital Markets Act(emphasis added)

What sets the web apart is that it was never designed to confine users within closed ecosystems. It is the world’s only truly open and interoperable platform, requiring no contracts with OS gatekeepers, no revenue sharing with intermediaries, and no approval from dominant platform owners. Anyone can publish a website or build a web app without permission. There are no built-in lock-in mechanisms keeping users tied to a single company’s hardware or services. Users can switch browsers, move between devices, and across ecosystems, all without losing access to their data, tools, or digital lives.

This kind of freedom simply doesn’t exist in app store-controlled environments, where every app update, transaction, and user interaction is subject to centralized control, censorship, or a mandatory financial cut. The web’s architecture prioritizes user autonomy, developer freedom, and cross-platform compatibility.

Apple’s justification for its gatekeeping is security. Its position is that only Apple can be trusted to decide what software users are allowed to install. Every third party must submit to its review and approval process, no exceptions.

But the secure, interoperable, and capable alternative already exists, and it's thriving. That solution is the Web, and more specifically, web apps. On open platforms like desktop, web technologies already account for over 70% of user activity, and that figure is only growing.

Web apps offer the key properties needed to solve the cross-platform problem. They run inside the browser sandbox, which evenApple admitsis“orders of magnitude more stringent than the sandbox for native iOS apps”. They are fully interoperable across operating systems. They don’t require contracts with OS vendors. And they’re highly capable: if there was effective competition, around 90% of the apps on your phone could be delivered as web apps.

However, this promise only holds if browser vendors are allowed to compete, using their own engines, on every platform. Without that, Apple can unilaterally limit what the web is capable of, not just on iOS, but everywhere. If a feature can’t be used on a platform as critical as iOS, then for many developers, it may as well not exist.

That’s why enforcement of the Digital Markets Act on this issue is so vital, not just for the EU, but for the world.

The web is the world's only truly interoperable check against operating system platform monopolies. Itmustbe allowed to compete fairly.

## #Is Apple Obligated to Fix This Under the DMA?

A key question is whether Apple is required to fix this under the Digital Markets Act. Apple’s representatives argue that browser vendors can port their own engines to iOS in the EU and at a highly superficial and technical level this is true. However, what Apple does not acknowledge is that the conditions it imposes make doing sofinancially unviable in practice. Does this really count as compliance?

To answer that, we need to examine the DMA itself.

### #The Core Obligation: Article 5(7)

The primary relevant article in the Digital Markets Act is Article 5(7):

The gatekeeper shall not require end users to use, or business users to use, to offer, or to interoperate with, an identification service,a web browser engineor a payment service, or technical services that support the provision of payment services, such as payment systems for in-app purchases,of that gatekeeper in the context of services provided by the business users using that gatekeeper’s core platform services.Article 5(7) - Digital Markets Act(emphasis added)

At face value, Apple appears to have complied with the letter of Article 5(7). It technically allows third-party engines, but only under technical platform constraints and contractual conditions that render porting non-viable.

### #But the DMA Demands More Than Surface-Level Compliance

The gatekeeper shall ensure and demonstrate compliance with the obligations laid down in Articles 5, 6 and 7 of this Regulation.The measures implemented by the gatekeeper to ensure compliance with those Articles shall beeffectivein achieving the objectives of this Regulationand of the relevant obligation.Article 8(1) - Digital Markets Act(emphasis added)

The gatekeeper shall not engage in any behaviour thatundermines effective compliancewith the obligations of Articles 5, 6 and 7regardless of whether that behaviour is of acontractual, commercial ortechnical nature, or of any other nature, or consists in the use of behavioural techniques or interface design.Article 13(4) - Digital Markets Act(emphasis added)

These two articles clarify that it is not enough for Apple to simplyallowalternative engines in theory. The measures must beeffectivein achieving the article’s objectives, and Apple must not undermine those objectives by technical or contractual means.

### #The Intent Behind Article 5(7)

The intent of this provision is laid out clearly in the recitals of the DMA:

In particular, each browser is built on a web browser engine, which is responsible for key browser functionality such as speed, reliability and web compatibility.When gatekeepers operate andimpose web browser engines, they are in a position todetermine the functionality and standardsthat will apply not only to their own web browsers, but alsoto competing web browsersand, in turn, toweb software applications.Gatekeepers should therefore not use their position to require their dependent business users to use any of the services provided together with, or in support of, core platform services by the gatekeeper itself as part of the provision of services or products by those business users.Recital 43 - Digital Markets Act(emphasis added)

In other words, Apple should not be in a position to dictate what features, performance, or standards in competing browsersand the web apps they power. That is, the intent is to guarantee that browser vendors have the freedom to implement their own engines, thereby removing Apple’s ability to control the performance, features, and standards of competing browsers and the web apps built on them.

### #Is Apple Complying in Practice?

Fifteen months since the DMA came into force,no browser vendor has successfully ported a competing engine to iOS. The financial, technical, and contractual barriers Apple has put in place remain insurmountable. These restrictions are not grounded in strictly necessary or proportionate security justifications.

This is not what effective compliance looks like. Article 5(7)’s goals, enabling engine-level competition and freeing web apps from Apple’s ceiling on functionality and stability, have not been met. Under Article 8(1) and Article 13(4), that makes Apple non-compliant.

Apple has a clear legal obligation to fix this. But will it act without pressure?

## #Why Apple is right to fear a successful DMA solution

Any successful solution to allow browsers to use their own engines in the EU is highly likely to become global. Multiple regulators and government organizations have recommended ending Apple’s ban on third-party browsers including in the UK, Japan, USA and Australia. Further multiple new laws have already been passed, including theUK’s Digital Markets, Competition and Consumers Act(DMCC), andJapan’s Smartphone Actwhich directly prohibits it.Australiaand theUnited States are also considering similar legislation. Finally theU.S. Department of Justice is pursuing an antitrust case against Appleandtheir complaintdirectly cites the issue.

With growing international momentum, and continued advocacy pushing for aligned global enforcement, Apple’s browser engine ban is facing sustained and mounting pressure. If the EU succeeds in forcing meaningful compliance under the DMA, it will set a global precedent. What regulator or government would tolerate such an obvious restriction on competition in their own market once the EU has shown it can be dismantled?

So why is Apple resisting this change so hard?They've already fought, and lost, a high court battle over it. Is this just a matter of being litigious? Hardly. Apple is acting rationally, if unethically.At the end of the day, it’s all about protecting revenue.

The UK regulator cites two incentives: protecting their app store revenue from competition from web apps, and protecting their Google search deal from competition from third-party browsers.

Apple receives significant revenue from Google by setting Google Search as the default search engine on Safari, and therefore benefits financially from high usage of Safari. [...]The WebKit restriction may help to entrench this positionby limiting the scope for other browsers on iOS to differentiate themselves from Safari [...] As a result, it is less likely that users will choose other browsers over Safari, which in turnsecures Apple’s revenues from Google. [...] Apple generates revenue through its App Store, both by charging developers for access to the App Store and by taking a commission for payments made via Apple IAP. Apple therefore benefits from higher usage of native apps on iOS. By requiring all browsers on iOS to use the WebKit browser engine,Apple is able to exert control over the maximum functionality of all browsers on iOSand, as a consequence, hold up the development and use of web apps. Thislimits the competitive constraint that web apps pose on native apps, which in turn protects and benefits Apple’s App Store revenues.UK CMA - Interim Report into Mobile Ecosystems(emphasis added)

A third and interesting incentive which the US's Department of Justice cites, is that this behavior greatly weakens the interoperability of Apple's devices, making it harder for consumers to switch or multi-home. It also greatly raises the barriers of entry for new mobile operating system entrants by depriving them of a library of interoperable apps.

Apple has long understood how middleware can help promote competitionand its myriad benefits, including increased innovation and output,by increasing scale and interoperability. [...] In the context of smartphones, examples ofmiddleware include internet browsers, internet or cloud-based apps, super apps, and smartwatches, among other products and services. [...]Apple has limited the capabilities of third-party iOS web browsers, including by requiring that they use Apple’s browser engine, WebKit. [...] Apple has sole discretion to review and approve all apps and app updates.Apple selectively exercises that discretion to its own benefit, deviating from or changing its guidelines when it suits Apple’s interests and allowing Apple executives to control app reviews and decide whether to approve individual apps or updates. Apple often enforces its App Store rules arbitrarily.And it frequently uses App Store rules and restrictions to penalize and restrict developers that take advantage of technologies that threaten to disrupt, disintermediate, compete with, or erode Apple’s monopoly power.DOJ Complaint against Apple(emphasis added)

Interoperability via middleware would reduce lock-in for Apple’s devices. Lock-in is a clear reason for Apple to block interoperability, as can be seen in this email exchange where Apple executives dismiss the idea of bringing iMessage to Android.

The #1 most difficult [reason] to leave the Apple universe app is iMessage ... iMessage amounts to serious lock-inUnnamed Apple Employee

iMessage on Android would simply serve to remove [an] obstacle to iPhone families giving their kids Android phones ... moving iMessage to Android will hurt us more than help us, this email illustrates why.Craig Federighi - Apple's Senior Vice President of Software Engineering

Apple has also long been concerned that the web could be a threat to its app store. In 2011, Philip Schiller internally sent an email to Eddie Cue to discuss the threat of HTML5 to the Apple App Store titled“HTML5 poses a threat to both Flash and the App Store”.

Food for thought: Do we think our 30/70% split will last forever? While I am a staunch supporter of the 30/70% split and keeping it simple and consistent across our stores, I don’t think 30/70 will last unchanged forever. I think someday we will see a challenge from another platform or a web based solution to want to adjust our modelInternal Apple Emails(emphasis added)

It is crucial that readers and regulators understand that this is not some trivial matter for Apple. Allowing both browsers and the web to compete fairly on iOS will seriously harm Apple’s margins and revenue.

Apple getsan astonishing $20 billion a yearfrom Googleto set its search engine as the default in Safari,accounting for 14-16 percent of Apple's annual operating profits.Safari’s budget is a mere fraction of this, likely in the order of$300-400 million per year.This means thatSafari is one of Apple’s most financially successful products and the highest margin product Apple has ever made.Foreach 1% browser market sharethat Apple loses for Safari,Apple is set to lose $200 million in revenue per year.

In 2024,Apple is estimated to have collected $27.4 billionfrom $91.3 billion in sales on its app store, underscoring its role as a critical and expanding source of profit. By contrast, the macOS App Store, where Apple does not exercise the same gatekeeping power over browsers or app distribution, remains a much smaller operation, with revenue that Apple chooses not to report.

Web apps, which already have a dominant 70% share on desktop, can replace most of the apps on your phone. Even a far more modest 20% shift towards web appswould represent a $5.5 billion annual loss in revenue.

This is important because it explains why Apple will not voluntarily make these changes.No rational actor with such a tight monopolistic grip on a market (the market for browsers and the market for apps on iOS) would give that up if they could plausibly hang onto it by subtly or explicitly undermining attempts to open it up. Apple’s statements about engaging or making changes are meaningless,it is only the concrete actions that they have taken to date that must be measured.

These changes, and the competition and interoperability they bring, will literally cost Apple billions if not tens of billions per year. On the flip side these are savings that developers and consumers are missing out on, both in terms of quality of apps and services, and direct costs. This is money that Apple is extracting out the market via their control of iOS on high-cost and high-margin devices sold to consumers at full price.

With a market value of $3 trillion, Apple has a legal budget of over $1 billion a year, giving it legal power that outstrips that of small nations. It is also not afraid to step as close to the line of non-compliance as possible, as Apple’s former general counsel explains:

work out how to get closer to a particular risk but be prepared to manage it if it does go nuclear, …steer the ship as close as you can to that linebecause that's where the competitive advantage occurs. … Apple had to pay a large fine, Tim [Cook]'s reaction was that's the right choice, don't let that scare you, I don't want you to stop pushing the envelope.Bruce Sewell, Apple’s former General Counsel(emphasis added)

This, unfortunately, means that regulation is the only answer. Even Open Web Advocacy was only formed after we had exhausted every possible avenue at trying to convince Apple to develop critical web functionality.

Many other parties have attempted to negotiate with Apple on these topics over the last 15 years and all have come to naught,the power imbalance and the incentives for Apple not to do this is simply too strong.

## #Apple vs the World

Some have tried to frame the DMAas a clash between the EU and the US, with the DMA unfairly targeting American tech giants, but that is not the case.

For US negotiators to carve out exemptions for American companies now would defang the DMA and stall its pro-competition benefits just as they begin to be felt. [...] The victims of a DMA pause would be America’s most innovative upstarts — especially AI start-ups.The DMA’s interoperability and fairness rules were designed to pry open closed platforms and give smaller companies a fighting chance.[...] Big Tech lobbyists portray the DMA as anti-American. In reality, the DMA’s goals align with American ideals of fair competition.This isn’t Europe versus America; it’s open markets versus closed ones.Luther Lowe - Y Combinator - Head of Public Policy(emphasis added)

The reality is this: Apple stands alone in enforcing a ban on competing browser engines and suppressing web app competition on iOS. No other gatekeeper imposes such a restriction.

In fact, the three major organizations working to port alternative browser engines to iOS, Google, Mozilla, and Microsoft are themselves American. Smaller browser vendors, many of whom are also based in the US, are depending on these efforts. Apple’s restrictions don’t serve consumers, startups, web developers, native app creators, or even other American tech companies.They serve only Apple, who makes billions per year from undermining both browser and web app competition on iOS.

Through front groups like ACT, which Apple primarily funds, the company may attempt to reframe this issue as the EU targeting successful US firms. But that’s a distraction. This isn’t Europe versus America,it’s Apple versus the World.

## #Apple DMA Workshop

At the DMA workshop last Monday, we had a chance to ask some of these questions, and to chat with Apple’s ever-charming Gary Davis (Senior Director, Apple Legal) on the sidelines. While we are strongly opposed to Apple’s ongoing anti-competitive conduct, we do deeply appreciate that Gary and Kyle were willing to come over and participate in person.

### #No Browser Vendor has been able to bring their own engine to iOS

To kick off the first of OWA’s questions on browser engines, Roderick Gadellaa asked the key question:Why has no browser vendor been able to bring their own engine to iOS, even after 15 months of the DMA being in force?

The DMA has been in force now for 15 months.Despite this, not a single browser vendor has been able to port their browser using its own engine to iOS.It's not because they're incapable or they don't want to,it's because Apple's strange policies are making this nearly impossible.One of the key issues slowing progress is that Apple is not allowing browser vendors to update their existing browser app to use their own engine in the EU, and Apple's WebKit engine elsewhere. This means thatbrowser vendors have to ship a whole new app just for the EUand tell their existing EU customers to download their new app andstart building the user base from scratch.Now, we would love for Apple to allow competing browsers to ship their own engines globally. But if they insist on allowing this only in the EU, Apple can easily resolve this problem. Here's how:They can allow browsers to ship two separate versions of their existing browser to the App Store, one version for the EU and one for the rest of the world. Something which is currently possible in other App Stores.This would allow existing European users to get the European version of the app without having to download a separate app simply by receiving a software update.But it seems Apple doesn't want that, and they make this very clear in their browser engine entitlement contract.Given that, Apple can easily resolve this problem simply by allowing browsers to ship a separate version of the app to the EU under the same bundle ID.Why is Apple still insisting that browser vendors lose all their existing EU customers in order to take advantage of the rights granted under the DMA?Thank you.Roderick Gadellaa - Open Web Advocacy(emphasis added)

Coalition for Open Digital Ecosystems(an European advocacy group with members including Google, Meta, Qualcomm and Opera) also asked about the difficulty in porting browser engines:

Apple has made some changes to its rule governing third-party browsers and the ability to use other browsers engines in the EU. However, as was already mentioned, they have various restrictions, includinghaving two different versions of the app,limitations on testing,cumbersome contract requirements, still making it onerous to meaningfully take advantage of the browser engine interoperability. Which is why no one has really successfully launched on iOS using an alternative browser engine.What is Apple going to do to enable the third parties to launch a browser on iOS via an alternative engine?Emre Kursat Kaya - Coalition for Open Digital Ecosystems(emphasis added)

Gary Davis (Senior Director Apple Legal) and Kyle Andeer (Vice President Apple Legal) were there to answer the questions:

Let me take the browser engine first. I know this isall just conversation is supposed to be about browser choice screens and defaults, but I know some of you, many of you with the same group, have traveled very far to have this conversation. And so I'll take a question on that, which is, listen: as everyone knows, when we designed and released iOS and iPadOS over 15 years, we were hyper focused on how do we create the most secure computing platform in the world. We built it from the ground up with security and privacy in mind.The browser engine was a critical aspect of that design.Webkit was that aspect of the design. And that has worked for 18 years.We recognize under the DMA that we've been forced to changeAnd we have created a program that keeps security and privacy in mind, that keeps the integrity of the operating system in mind, and allows third parties to bring their browser engine, Google, Mozilla, to the platform.And for whatever reason, they've chosen not to do so.And so we remain open. We remain open to engagement. We have had conversations, constructive conversations with Mozilla, less constructive engagement from the other party, but we are working to resolve that, those differences, and bring them to iOS in a way that we feel comfortable with in terms of security, privacy, and integrity perspective.Kyle Andeer - Apple - Vice President Apple Legal(emphasis added)

Kyle began by incorrectly asserting that the session was focused solely on browser choice screens and defaults,despite the session being explicitly titled “Browsers”. This appeared to suggest that our question on browser engines was somehow out of scope.

DMA Apple Workshop Agenda 2025

He acknowledged that under the DMA, Apple is now required to allow third-party browser engines on iOS. He then reiterated Apple’s long standing talking points: that iOS was built from the ground up with security and privacy in mind, that WebKit is a core part of that design, and that any changes must preserve what Apple deems the "integrity" of the platform.

However, the fact that Safari heavily reuses iOS code and components is unlikely to be a genuine security feature and is almost certainly a cost-saving measure. By reusing code and libraries between iOS components, Apple can save significant amounts on staffing. This comes with two significant downsides: First it worsens security by locking Safari updates to iOS updates, increasing the time it takes security patches to reach users. Second, this tight coupling harms Safari itself by making it difficult for Apple to port its browser to other operating systems, ultimately weakening its competitiveness and reach. It also means that Apple can’t offer beta versions of Safari to iOS users without them installing an entire beta version of the operating system, a limitation that other browsers do not have.

According to Kyle, Apple has created a program that allows third-party engines“in a way we feel comfortable with in terms of security, privacy, and integrity”but offered no specifics. He then shifted blame onto browser vendors, stating that Mozilla and Google have simply“chosen not to”bring their engines to iOS, omitting the fact that Apple’s technical and contractual constraints make doing so unviable.

There's a lot of OWA people here in the rooms so well done on that.I also half the questions at least were about browser engines, which is obviously an Article 5(7) as opposed to a 6(3) issue. More than happy as Kyle already did to address the question,but I think it would be a shame that a session that is about choice screens and uninstallation and the defaults become a browser engine discussion.I was pleased that Kush was nodding when Kyle was pointing out the ongoing engagements with Google and Mozilla, which are continuing right up even to last week, and I think just some more this week.There was a bottom line issue, however, which is that both Google and Mozilla have everything they need to build their engines and ship them on iOS today.We heard some other issues mentioned. We are happy to engage on those issues. We are engaging on those issues, but everything is in place to ship here in the EU today. I think that's an extremely important point to take away from this.Gary Davis - Apple - Senior Director Apple Legal(emphasis added)

Gary reiterated Kyle’s suggestion that the questions on browser engines were out of scope and that browser vendors have everything they need to ship a browser engine on iOS today.

I think one other point I wanna make sure I address as I reflected upon the end, there was a question about why we don't do this on a global basis. And I thinkwe've always approached the DMA as to the European law that relates to Europe. And we are not going to export European law to the United States, andwe're not going to export European law to other jurisdictions. Each jurisdiction should have the freedom and decision making to make its own decisions. And so we're going to abide by that.Kyle Andeer - Apple - Vice President Apple Legal(emphasis added)

Kyle concluded by asserting that Apple would comply with the DMA only within the EU, stating that it would not "export a European law to the United States". This ignores the reality that Apple has, in fact, already extended several EU-driven changes globally, includingUSB-C charging for iPhones,support for game emulators,NFC access for third-party payments,the new default apps pageandno longer hiding the option to change default browser if Safari was the default.

While we would prefer that Apple enable browser competition globally on iOS, we recognize that the DMA does not require it to do so. We highlight these globally adopted changes simply to point out that Apple could choose to take the same pro-competative approach here. This restriction not only undermines global interoperability, but also weakens the effectiveness of the solution for EU users themselves.

[...] it's OK to ask questions which are other questions related to browsers. So I think that's totally OK given the name of the session.Lucia Bonova - European Commission - Head of Unit - Digital Platforms

Finally, Lucia, on behalf of the Commission, clarified that all questions on browsers related to the DMA were in scope.

### #Spotify & Web Developer Testing

Earlier in the day, in a response to a question on reporting malicious apps, Kyle had finished with a quip suggesting that OWA gets its talking points from Spotify.

So I guess I get to.. I suppose OWA get to talk to SpotifyKyle Andeer - Apple - Vice President Apple Legal(emphasis added)

This may have been a reference to an earlier question where we usedApple blocking Spotify from updating its appfor 5 months,despite having been fined 1.8 billion euros,as an example of Apple abusing app review for non-security purposes. For the record, OWA's information came from publicly available and widely reported news articles, nor had we talked to Spotify.

In response, OWA volunteer James Heppell addressed the insinuation directly before asking a question about web developer testing and third-party engines:

So I'd like to return to a browser engine for a second. But if it's OK, I'd like to quickly clear up my kind of connections to this. Because I think, Kyle, you were suggesting that I'm a front for Spotify and that OWA is. That's what I heard.I'm just a student. I volunteer becauseI truly believe in the open web. I don't get paid. I don't receive any compensation. I paid for myself to be here because I want to be.And the organization does not receive any money either. It's just donations. So if that's OK, and all clear. I'd like to carry on to the question.When Apple does, eventually, hopefully, allow other browser engines on iOS, it will be adding a new phase of competition.These engines will be unique on iOS, acting as an intermediary platform between the OS and the web. But having been blocked from iOS for over 15 years, when they arrive, there will inevitably be any unique bugs which need to be identified and resolved. And I think if I remember correctly, you said earlier that the new EU iOS will experience, I quote, "vulnerabilities and problems that will be unique here".However, these restrictions, which are unique to Apple, creates a new problem. Most web developers like us, but not like us, are all around the world: in the US, where you're from, in Asia, in Africa, and the rest of the Americas,all over, and they still will serve EU users, but they're going to be unable to install or test these new browsers with their third-party engines on their devices. This means that these developers will be able to test Safari, but not Firefox's Gecko or Chromium, putting these competing browsers, web developers, businesses, and users at a significant disadvantage.Apple faced the same issue with native app developers earlier, and ultimately resolved it by allowing testing versions of EU-only apps to be downloaded outside of the EU for developmental purposes.The same principle should apply here. Web developers globally must be able to test their sites in the new competing browsers on iOS regardless of where they're located. We understand that Apple may not wish to allow these browsers to ship to consumers, that's their choice, I suppose, but that is a completely separate issue to allowing developers to test it.So my question is,what solution does Apple propose to ensure that web developers outside of the EU can install and test these browsers and maintain compatibility and interoperability for users in the EU?James Heppell - Open Web Advocacy(emphasis added)

Kyle Andeer responded:

We're in a period of transition where we built an operating system, a set of operating systems that was designed to be the most secure in the world, and that is what we have built. A critical aspect of that was our integration of WebKit into our operating systems. And we've continued to maintain that as the most secure way to ensure that we have the very best operating system possible. We've also introduced flexibility and APIs for third-party browser engines to take advantage of these new opportunities under the DMA. We're also engaged in ongoing conversations with Mozilla and with the other company in terms of bringing them to iOS.In terms of earlier, I don't think I referenced that you were getting funding from Spotify. I don't know where you're getting funding from. My reference is more to the code representative who does get a lot of funding from Google and Meta and Qualcomm and Spotify and others, but not yourself.I understand that, and I actually really […] respect the way that your team has approached this.I don't question your motives. I don't question your funding.We disagree, right? I think that's clear. In forums like this, our place is to disagree. We think we have developed a compliant solution. I appreciate hearing your feedback, and your feedback, and your colleagues' feedback. We'll take that into account.We've read your papers. We've read your advocacy.There are points where we disagree and we'll probably continue to disagree going forward. But I am not in any way disparaging where you're coming from.I understand you're a well-meaning person who believes that he understands how to best design our operating system.I get that.Kyle Andeer - Apple - Vice President Apple Legal(emphasis added)

We appreciate Kyle’s acknowledgment that we are sincere and not a front for any tech giant. We are also glad that Apple is reading and considering our papers and advocacy.

That said, Kyle slightly undercuts his otherwise polite tone by remarking,"I understand you're a well-meaning person who believes that he understands how to best design our operating system". While we welcome the recognition of good intentions, it’s important to clarify that OWA's volunteer base includes experts in web development, browser engine design, security, and even operating system design.

While Apple likely knows best how to technically design their own products,Apple has repeatedly demonstrated that it prioritizes its business interests over the needs of developers and the broader public.It is precisely because Apple refuses to design an OS that allows fair browser competition or complies with laws like the DMA that OWA has stepped in, on a volunteer basis and with limited funding, to do work Apple should have done itself.

Several design ideas and proposals submitted by OWA have already found their way onto Apple devices both in the EU and in some cases globally. These includepush notifications in Safari,the unified defaults settings screen,placing the new default browser on the home screen hotseat,making Safari soft-uninstallable (with the a default browser warning),expanding the information shown in the browser choice screen, anddownloading the chosen choice screen browser in the background.

When it comes to designing an operating system that enables fair competition and complies with the DMA, we would genuinely prefer that Apple take the lead. OWA’s contributions are only necessary because Apple has chosen not to.

James, maybe I'll just take yours first in terms of what we'd call the testing entitlement. I think as we've been going along, we have learnt a lot as to how to facilitate that kind of testing outside of the EU, even in relation to browser engines. I think that's a subjective, active discussion.I think we've been discussing it with Mozilla and Google also. And the commission, I would expect to see some updates there.Gary Davis - Apple - Senior Director Apple Legal(emphasis added)

As far as we’re aware, none of the browser vendors have been informed about this. That said, if Apple is actively working on a solution, that’s great. However, without published details, it’s difficult to properly evaluate. Note,Apple has been aware of this issue since June 2024, over a year ago.

Our proposed solution is straightforward: web developers outside the EU should be able to download and install test versions of third-party browsers on iOS, using their own engines, directly onto their devices for the purpose of testing web apps and websites for EU users. This is strengthened by the fact that Apple has already implemented an equivalent solution for native app developers outside to test EU only features for their EU users.

### #Mozilla on the Separate App Requirement

Yeah, just to your last point, Gary, my first question about user testing would be great to get a response to that. And then just to Kyle's point about two separate binaries and security being the reason for the BrowserEngineKit restrictions, we'd love to understand how you see those things connected and why security is the reason for that restriction.Kush Amlani - Mozilla - Director, Global Competition & Regulation

Kush’s question is crucial because it challenges Apple to prove that its separate binary rule is truly connected to security, privacy, or platform integrity. Apple has provided no technical analysis showing that a single binary approach,or any alternative, pose a genuine security risk. Under the DMA Apple carries the full burden of demonstrating that such a restriction is both necessary and proportionate. So far Apple has neither satisfied that burden nor even attempted to meet it.

I think you raise an issue in relation to security. The reality is, and everybody knows this, and this is why it's taken a while to work through the issues, that browser engines are a security vector. I know it’s not agreed by everybody that they have a similar security profile, but they do. I could sit here now and read a list of, I don't know, 100 actual vulnerabilities associated with browser engines. They are a known vulnerability. So therefore, we want to move forward in a way that takes account of those vulnerabilities and does not put our users at risk on the platform. And I think that is something which everybody should want as an outcome here.Gary Davis - Apple - Senior Director Apple Legal

We have been consistent inour viewpoint that browsers are complex applications that require significant security investment, we have never claimed that browsers are not a known vector for security vulnerabilities. Rather, our position is thatApple is undermining user securityby preventing arguably more capable browser vendors from competing with Safari on iOS.

Apple has previously asserted to the UK regulator that its WebKit engine was more secure than Blink and Gecko. However, when asked to substantiate this claim, Apple failed to provide compelling evidence. The UK Competition and Markets Authority (CMA) concluded:

... in Apple's opinion, WebKit offers a better level of security protection than Blink and Gecko.... the evidence that we have seen to datedoes not suggestthatthere are material differences in the security performance of WebKit and alternative browser engines.Overall, the evidence we have received to datedoes not suggest that Apple's WebKit restriction allows for quicker and more effective response to security threats for dedicated browser apps on iOSUK CMA - Interim Report into Mobile Ecosystems(emphasis added)

Another key issue is that, due to how performance and sandboxing are implemented in browser engines, Apple will inevitably need to entrust significant responsibility for user security to the browser vendors themselves. Given thatthese browser vendors have security track records that are arguably superior to Apple’s,this will, in fact, improve security on iOS. Apple is well within its rights under the DMA to impose reasonable baseline requirements such as regular security updates to all browsers on iOS, including Safari, and few would object to that. What needs to be avoided though is security rules that restrict utility to Apple’s native app ecosystem or that undermine competition.

### #Web Apps powered by other Engines

So last year, after we made a lot of noise to get Apple to reinstate homescreen web apps in the EU. Apple announced that homescreen web apps continue to be built directly on WebKit and its security architecture. However, under Article 5(7) of the DMA, Apple is not allowed to impose a browser engine on either users or third-party browsers. Can Apple update us on the progress made for allowing third-party browser engines to install and manage homescreen web apps on iOS once third-party browser engines arrive on iOS? Thank you.John Ozbay - Open Web Advocacy

This is an important question as Apple has given no indication that it intends to share the ability to install and manage web apps with third-party browser engines. In fact, their actions suggest the opposite:they initially removed this functionality entirely rather than make it available to others,have stated it will remain exclusive to WebKit, and have offered no timeline or commitment to open it up.

Under Article 6(7), Apple is prohibited from reserving such functionality for its own use, and Recital 43 makes clear that this is precisely the type of self-preferencing that the DMA's browser engine provision in Article 5(7) is meant to prevent. It is therefore unclear how Apple can lawfully justify denying third-party browsers the ability to install and manage web apps, particularly in browser vendor development environments where no user-facing concerns could be invoked during this development phase.

Finally, Apple has not published any detailed technical justification for why reserving these functionalities exclusively for itself is the only proportionate and strictly necessary security measure. In our view, no credible case can be made for such a blanket restriction,but tellingly, Apple has not even attempted to present one.

I think on homescreen web apps, obviously these are available today here and around the world.We have nothing to announce in terms of what we will doifand when athird-party browser engine comes to iOS. Certainly I can say from a high level perspective, our focus will continue to be, as I've said several times, on ensuring that anything that's operating on our platform is as secure and as private as possible, and it does not damage the operating system.Browsers and home screen web apps are different than other things. They have other access to the operating system that we will have to manage and control.And so we have not settled out on any of those issues. As I've said again, we've engaged with Mozilla, we've engaged with Google. We're figuring out the solution that works best for all parties.Kyle Andeer - Apple - Vice President Apple Legal(emphasis added)

First, it is concerning that even Kyle, Apple’s lead executive responsible for DMA compliance, expressed uncertainty about whether browser vendors will port their engines to iOS under Apple’s current technical and contractual terms, despite vendors doing so on every other major platform.This signals low confidence from Apple that their compliance measures will be successful in achieving the aims of Article 5(7).

Kyle’s statements in relation to security are also misleading. While he is correct in that, as covered in the previous section, Apple will need to give significantly greater access and delegate more security to browsers than a typical native app, the same is not true for web apps.

Web apps are extremely tightly sandboxed, according to Apple this sandboxing is “orders of magnitude” stronger:

WebKit’s sandbox profile on iOS isorders of magnitudemore stringent than the sandbox for native iOS apps.Apple’s Response to the CMA’s Mobile Ecosystems Market Study Interim Report(emphasis added)

Orders of magnitude, while correct, is also a striking phrase. That is, not slightly better but hundreds to thousands of times stronger. Allowing other browsers to improve the functionality, discoverability, performance and stability of web apps, will allow more end users to take advantage of the greater security and privacy of web apps.Native apps on iOS have far greater automatic access to personal data, andare not afraid to abuse that access due to Apple’s frustratingly toothless app store privacy enforcement.

Apple’s statement suggests that browser vendors aren’t ready to support this functionality, but in reality, vendors have already taken steps to gain access to the ability to install and manage web apps, including at least one formal request under Article 6(7) made over a year ago which was flatly rejected outright by Apple’s legal team.

Rejecting requests to share the ability to install and manage web apps, without offering any detailed technical justification, is not meaningful engagement. Apple has not, to our knowledge, acknowledged that they have this obligation, nor have they begun detailed technical discussions on how to effectively comply.

Again, and this is critical, while it is encouraging that Apple has not explicitly denied its obligation to make this functionality available,compliance must be measured by actions, not words.

## #What needs to be fixed on iOS?

To comply with the aims of Article 5(7) of the DMA, and as outlined by Recital 43, Apple must stop imposing the use of its own browser engine on users, developers, and browser vendors within the EU. It must also no longer use such restrictions to control the functionality, performance, or stability of web applications installed and managed by third-party browsers.

Under Article 8(1), Apple is required to make changes that ensure this obligation iseffective in achieving its objectives. Furthermore, under Article 13(4) Apple may not undermine compliance through contractual, commercial, or technical means.

So what must Apple change to meet these requirements?

Below is a brief summary of the most critical outstanding issues. You can follow the links to find out more detail about each individual fix. The vast majority of these remain unchanged from ourJune 2024 Apple DMA Reviewpaper.

### #Browser Engines and Interoperability

* No Separate App Requirement (Single Bundle ID)Allow browser vendors to keep their existing users by letting vendors update their existing apps to use their own browser engine.
* Web Developer TestingAllow non-EU web developers to be able to test web software for the purpose of supporting their EU users.
* SFSafariViewControllerUpdate SFSafariViewController to respect the users choice of default browser and to provide meaningful benefit from the browser choice screen. The solution already works for Android via Android Custom Tabs.
* Interoperability and Hardware AccessEnsure browser vendors have access to all relevant hardware related functionality like on other operating systems for the purposes of developing web APIs such as WebUSB, WebBluetooth, WebNFC and ensure functionality extends to web apps installed by these browsers.
* BrowserEngineKitImprove the stability and functionality of BrowserEngineKit. Ensure Apple has a transition strategyto migrate Safari to use their own framework.
* Grant Equivalent Access to Content Filtering APIsCurrently, iOS content filtering settings, used by parents to restrict access to harmful or adult material, only apply to Safari and apps using WKWebView. Third-party browsers with their own engines cannot integrate with these system-level protections, meaning they can not respect parental controls configured by users.Apple has stated that adding support is a"mild engineering effort"and has promised a beta release in March 2026.Likely, no browser vendor will be willing to ship a consumer product without this API given its importance to online safety and parental controls.
* Fair Browser Engine Entitlement Contract TermsRemove all unfair and non-security related terms from theBrowser Engine Entitlement Contract. Any security terms must be proportionate and iOS Safari must be proven to be meeting them.
* Apple Should Not Break Updates for EU Residents Traveling Outside The EUApple has stated that it will prevent all updates for apps downloaded from third-party app stores that are outside the EU for more than 30 days.Apple has not released any explicit statement on what will happen to browsers using their own engine downloaded from Apple’s app store if the user (an EU resident) leaves the EU for greater than 30 days.Given Apple attempted to block even browser vendors from testing on their own test devices outside the EU, it seems likely they will attempt to extend a similar policy to third party browsers which use their own engine even if they are downloaded from Apple’s app store.We would like a statement from Apple clarifying that this does not apply to browsers with the browser engine entitlement.
* Allow Own Browser ExtensionsAllow third-party browsers to ship their own extensions on iOS (something that Apple currently only allows Safari to do), including separately from Apple’s app store if desired. Browser Extensions are a critical part of browser competition.

### #Web Apps

* Web Apps run by Third-Party EnginesAllow browsers to install and manage Web Apps which then run in the third-party browser’s engine. Third-party browsers should be able to manage the web app install process and customize the web apps settings page to support desired features. Browsers should also be able to operate “web app stores”.
* Web App Install DiscoverabilityAllow installation of Web Apps in Safari to be asdiscoverable asnative apps. Currentlythe option to install a web app is hiddenand has been made worse in the upcoming iOS 26.

### #Distribution

* Direct Browser InstallationAllow direct browser installation independently from Apple’s app store without scare screens.
* Automatic NotarizationMake notarization for browsers with the browser engine entitlement automatic. Browser vendors with thebrowser engine entitlementhave agreed to security conditions such as regular patching and some havearguably better securitythan Apple. The app review team does not contain browser engineers and certainly not on the scale to meaningfully contribute. This means thehuman review element adds nothingbut it does grant Apple the ability to suppress competition and delay compliancevia app reviewas withSpotifyand Epic.
* Alpha and Beta Versions of BrowsersAllow Alpha and Beta versions of Browsers in the App Store, currently blocked by App Store rules. Currently Safari can not offer this feature due to being tightly tied to the operating system but that should not stop third-party browser vendors from contesting Safari by doing so. The scale that browsers operate on makes this necessary and other beta testing methods insufficient. Several browser engineers we have spoken to have said that testflights 10k user limit makes it next to useless for applications of this scale.

### #Choice & Contestability

* Age-Restriction ParityEnsure equal treatment between Safari and third party browsers in relation to Age‑Restrictions including accounting for Safari being preinstalled.
* System Change Default Browser PromptMake setting the default browser easier, by adding a system prompt to switch default browser. Other operating systems such as Android have such a prompt. Apple may subject this prompt to the usual anti-spamming rules it uses for iOS app permissions such as push notifications.
* Hotseat on Setting Default BrowserWhen a user manually downloads a browser and sets it as their default the operating system should prompt the user as to whether to place this browser in the hotseat replacing Safari.
* Safari Should Not Be Locked to Apple PayUpdate Safari to allow Apple Pay competitors. Apple is directly obligated to do this under Article 5(7) which stipulates they can not impose a payment provider via a core platform service. Safari is a core platform service.
* Default Browser DetectionInitially, third-party browsers on iOS were unable to detect whether they were set as the default. Apple now permits this check, but only four times per year. This arbitrary limitation prevents browser vendors from creating user experiences similar to Apple’s own flow for Safari on macOS, where the browser’s internal settings page indicates whether the browser is currently the default. By contrast, Apple imposes no such restrictions on more potentially intrusive APIs, such as push notifications, which can be queried without limit. Apple should apply consistent and non-discriminatory logic, and allow third-party browsers the same flexibility in determining their default status.
* Direct Install Browsers Should Be Included In Choice ScreensUpgrade the browser choice screen to install the direct install version of the browser if the browser vendor so chooses.

## #What Now?

Apple is not in compliance with the Digital Markets Act (DMA) regarding browsers and web apps.

While we understand the Commission’s measured approach and its willingness to give Apple the opportunity to comply voluntarily, it is now clear that, without firm intervention, Apple will continue to avoid resolving this issue indefinitely.

Due to Apple’s current technical limitations and contractual conditions, browser vendors lack a financially viable path to port their own engines to iOS, despite doing so on nearly every other operating system. Unless meaningful changes are enforced, Apple will have effectively circumvented its obligation under Article 5(7), rendering compliance hollow and defeating the purpose laid out in Recital 43.

The result: Safari remains shielded from effective competition on iOS, and Apple’s restrictions will continue to prevent the Web from serving as a viable, interoperable alternative to Apple’s App Store.

Apple will continue to reap billions per year as a reward for its defiance of the DMA, revenues that are extracted from consumers and businesses via denying them meaningful choice and locking them into Apple’s services on Apple’s terms.

We call on the Commission to investigate Apple's compliance and to compel Apple to make the necessary changes that would allow browser vendors to port their engines to iOS and, for the first time in 15 years, compete on fair terms.

Such enforcement will benefit EU consumers, EU businessesand ultimately the entire world.
