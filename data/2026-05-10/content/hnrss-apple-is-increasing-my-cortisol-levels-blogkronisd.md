---
title: Apple is increasing my cortisol levels | blog.kronis.dev
url: https://blog.kronis.dev/blog/apple-is-increasing-my-cortisol-levels
site_name: hnrss
content_file: hnrss-apple-is-increasing-my-cortisol-levels-blogkronisd
fetched_at: '2026-05-10T07:46:01.826837'
original_url: https://blog.kronis.dev/blog/apple-is-increasing-my-cortisol-levels
date: '2026-05-09'
description: My blog, where I attempt to collect my thoughts and share the occasional interesting topic with others
tags:
- hackernews
- hnrss
---

## Apple is increasing my cortisol levels

Date:2026-05-09

I'm creating a simple developer utility to make managing Claude Code profiles (e.g. running it with DeepSeek, or some OpenRouter models) a little bit easier. The utility itself is written in theGo language, and the tooling there makes it really easy to compile for various platforms - I get a static executable I can put anywhere I want. I intend to release it soon, but for now wanted to check how easily I can get it running everywhere.

It works just fine for distributing Windows software (I get an .exe).

It works just fine for distributing Linux software (same deal, afterchmod +x).

### Distributing Mac software

It does not just work for macOS and my MacBook instead shows me this:

What you see is theirquarantine kicking infor downloaded software, even if I share it with myself over Nextcloud.

Technically, you can ask your users to override it manually, in the terminal:

Most developers might be willing to do that. It is not, however, good user experience and might raise some eyebrows.

Doesn't seem like such a big deal, right? I'll just enroll in theirApple Developer Program, sign the executable and be on my way, right?

### Giving Apple money, and failing

Wait, they want how much money for the account?

And it's a yearly subscription? My brother in Christ, I intend to release a utility maybe a dozen or two dozen people are going to download, tops, for like 7 USD onItch.iowith apay-what-you-want model, meaning that most of those people will probably choose the price of 0 USD instead (since I don't intend to be like Apple, people have various circumstances).

That means that even if it works out that much, there's going to be VAT and Itch.io will also take a cut so out of those maybe 50 USD I'll get about 25 USD, which funds me about 3 months of that Apple Developer Program price. I guess the reason for it being priced like that lies somewhere between greed and wanting to gatekeep hobbyists out and only support Serious Users™, but it seems a bit stupid. Oh well, I already had to get the overpriced MacBook for another freelance thing, because they also won't let me compile macOS/iOS apps on Windows or Linux, so I guess this is just them spitting on me after slapping me in the face.

What I get from that is that articles likeAn app can be a home-cooked mealare cool but don't take the economics of wanting to release something publicly into account - unless you're developing something that you'll add a bunch of monetization to, you'll be losing money. For desktop software there isHomebrewbut that also means that you couldn't charge a few bucks for it even if you wanted to (or that you'd need to addmac-homebrew-install-instructions.txtto the Itch.io downloads page when doing the pay-what-you-want approach, which would feel awkward).

I don't like that the economics are pushing software and app development in a direction where releasing a package (that might be non-open-source or just source-available, but you want to release binaries) costs money, though I also acknowledge that there would be other issues, like insane amounts of spam, with not doing that.

Then, we get to the actual verification process - it's understandable that they'd want to verify my ID. The problem is that on the MacBook they also expect me to use its webcam to take a picture. I will admit that my M1 MacBook Air is getting dated at this point, but regardless of what lighting I tried, I could just not get a good picture of the document. It's not like they were like "Oh hey, we've detected that your own iPhone is connected to the same local network as this MacBook, would you like to use it as a camera?", so for about 10 attempts, this is what I saw:

Eventually, I moved over to trying to use my main webcam for that, since their built in one just doesn't work:

Why they can't just let me upload a scan of the document eludes me. I mean, I guess I can imagine a few reasons why, but it'd probably be easier to forge my own ID so it's not as glossy rather than having to turn my small kitchen table into this. Pictured for maximum frustration, a dongle that I needed:

Even that wasn't good enough, because understandably it doesn't have autofocus for something that you hold close. Not only that, but every 2nd failure seemed to just give me a generic error and I'd have to start the whole enrollment process from the beginning again:

Luckily I realized that I can install the app on my iPhone directly. There, it worked on the first try. I guess it must really suck if you don't have an iPhone or a fancy webcam, better spend some more money so you can give them money! The payment went through okay, soon after I had an activated developer account.

Except of course I didn't, look, the app tells me to await an e-mail (which I seemingly already received?):

And the desktop app doesn't care at all either, it doesn't even know that I've tried the enrollment, and offers me to start the whole thing over again, despite me being signed into the exact same account:

It's probably a case of eventual consistency and some background processes or whatever, but it's also quite frustrating and, in a word, stupid.

### Apple is kind of frustrating

Apple, I think you make hardware with pretty good build quality and the M-series chips made for pretty much the perfect notebook for me - and I'm sure they're great main dev machines for those that can afford the higher spec versions.

I think that's nice and I genuinely enjoy having the iPhone SE 2022, at least before learning that youkilled off the budget series altogether(your new e-series are more expensive) andremoved the nice silent mode toggle on the sideandremoved TouchID. That's before we even start talking about the 3.5mm jack and frankly all of that makes me question whether my next phone shouldn't just be an Android again.

I can deal with needing software likeAutoRaiseandRectangleandDiscreteScrollalongside others to customize your OS to my liking because you won't let me do that myself like most Linux distros do. I can even deal with your window focus needing an extra click across multiple monitors and AutoRaise being nice but perhaps too aggressive, since the developers are at least trying to make the experience nicer!

I can deal with your keyboard shortcuts being odd and not even having a "Cut" option in your Finder program.

I can deal with your weird Control/Command button setup which even breaks remote desktop software.

I can deal with your weird "programs you close aren't actually closed" approach even though you sold me a MacBook with 8 GB of RAM just so I could develop software in your walled garden ecosystem.

But to first vendor lock me to your ecosystem for developing apps, then demanding a whole bunch of money so I can sign my software and it not get quarantined all while I'm not too well off financially, then refuse to let me submit my documents to you because your hardware produces pictures that are not good enough and make me have to install the app on a phone that's also expensive and that not even everyone has, then to still make me wait and have your apps not even show that I've submitted my application?

You know what? Apple, fuck you and your forsaken ecosystem. This sucks.

### A more sane world

I can useSmartIDto verify my ID (and age) in about 20 seconds when buying an energy drink at the local grocery store.

I can useeParakststo digitally sign documents in about a minute, from either my PC with a card reader (using my government issued ID card), or my phone with their app, ending up with a proper cryptographic signature either attached to theEDOC container (ASIC-E)or a PDF file directly.

I'm sure that other countries also have plenty of similar services for ID and age verification, signing documents, and other digital services. I acknowledge that that's not all of them, and that things are all over the place in this regard (alongside the credit card mafia holding a lot of the world's payment infrastructure hostage), but come on, surely it's possible to create something that works better than my experience did.

Having a bunch of scrappy Baltic software packages working better than those by a multi-billion dollar company feels silly.

### Update

You know what, Apple isn't the only company where things are somewhat messed up.

If you want to sign some code for Windows, you can findCertum offering code signing, but that also costs around 209 EUR per year, all while they're supposed to be one of the affordable options out there! I'm not singling them out as much as acknowledging that they're one of the cheaper options and that many others out there are worse. What the fuck?

And then you look atAzure Artifact Signingnoticing that theirbasic tier only costs 8.54 EUR per monthand for a bit feel happy that someone has at least tried to disrupt the extortionate prices - until you set up your Azure account and notice that you cannot sign certificates as anindividualif you're outside of US & Canada, in the EU only organizations can sign code through them.

This feels about as bad as getting TLS certs was beforeLet's Encryptdisplaced most of that rent seeking behavior - the problem being that there aren't many alternatives or competitors to them, which on one hand means that we're moving towards a massive point of failure, and on the other hand means that if they ever decide to demand money, then a large part of the Internet will be straight up fucked.

I thought that maybe I'm overreacting a bit - since my previous issues were mostly about the Apple signup process being annoying and the way they've treated their users being worse than it could be, but no, I should be more angry - the whole code signing space is stupidly expensive for what it is. You have arguments in the opposite direction? Just know that they said the exact same kind of stuff about TLS before Let's Encrypt and how you have to pay 100 EUR a year for a cert that's not even a wildcard because of reasons™.

Just let me sign my code with my governmental ID card and be done with it, jeez.

Other posts:Previous »