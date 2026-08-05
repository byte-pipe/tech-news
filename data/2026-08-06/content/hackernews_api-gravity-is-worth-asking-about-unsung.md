---
title: “Gravity is worth asking about.” – Unsung
url: https://unsung.aresluna.org/gravity-is-worth-asking-about/
site_name: hackernews_api
content_file: hackernews_api-gravity-is-worth-asking-about-unsung
fetched_at: '2026-08-06T07:11:15.035552'
original_url: https://unsung.aresluna.org/gravity-is-worth-asking-about/
author: Marcin Wichary
date: '2026-07-30'
description: A blog about software craft and quality
tags:
- hackernews
- trending
---

I’ve enjoyed John Gruber’s posts about ads appearing on an increasing number of Apple surfaces: the App Store, Apple News, and – soon, perhaps – Apple Maps. (Just for reference, here’s an example of such an ad.)

Ina post earlier this week, Gruber likened ads to stickers on laptops, and shared a fun Steve Jobs story:

That’s what those stickers on PCs are: they’re ads. Intel pays for the “Intel Inside” stickers that booger up PC laptop palm rests. Longtime readers will recall thatback in August 2007, Apple held a Town Hall event to introduce new iMacs and some iLife and iWork software updates. In a post-event Q&A (imagine that),Bob Keefe of Cox Newspapers asked“Can you say why you all are not participating in the Intel Inside program, putting the stickers on your new or previous Macs?” This question was so absurdfrom the perspective of those who covered Apple closelythat it prompted outright laughter. […]

The 2007 exchange went as follows:

Keefe: Why are you not participating in Intel Inside program and not putting stickers on your Macs?Jobs: Uh… what can I say? We like our own stickers better.

(In case it’s not clear, this was a joke; Apple didn’t and doesn’t put any such stickers on their products. They instead used to includeApple logo stickersin boxes.)

In May,Gruber posted about Apple’s ads, too, and brought upthe zero-one-infinity rule:

I feel like a variation of Zero-One-Infinity is a good rule of thumb for ads, too. From the perspective of users — and probably developers — zero was the best number of ads for Apple to show in App Store search results. One was worse but acceptable. But now that they’re showing more than one, they’re on their way to infinity. They’ve started down the slippery slope. Remember when Google only showed one ad in search results?

“Slippery slope” is a perfect term. But I wanted to add something here. In my experience, in the realm of UI, there is no middle notch. I’ve seen it time and time again… the moment you open the door to One, Infinity starts exerting its pull:

* adding just one setting will send a message that We Do Settings Now and more settings will follow,
* one uncomfortable exception followed by weeks of deliberations will inevitablyopen the doorto subsequent mindless exceptions,
* onecheaporlazyapproach can spread through the interface like rust, subconsciously telling people “cheap and lazy solutions are okay here.”

Here are two examples I’ve been thinking about recently:

* This right click menu in Chrome started with just one fork (new window or new tab) – now there are three alts that I have to choose between, every single time, even if I only ever use one option:

* This – screenshotting in iOS – was originally just one fork: Save or Delete. Now it’s a staggeringfiveoptions I have to choose from, every time, even if I never touch four of them:

Once you wedge one thing in the door, it’s really hard to stop. My theory is that this is because digital interfaces are pretty much all infinitely extensible. There willalwaysbe a way to add one more button, one more link, one more setting, one more ad. If something doesn’t fit, you make it smaller. If making it smaller looks bad, you add a scrollbar. If a scrollbar doesn’t feel right, there’s always overflow.

Not only is it very hard to create interfaces that have limitations, but a bad decision is not just precedent – it’s code that can be copied and reused. Existing code always had tons of… well, gravity, even before LLMs.

And so, products grow complex without anyone intending them to; a new team adds just one more thing, which in isolation always feels like nothing to worry about. TheHick’s Law, theextra mental load, theweirdnessall grow in between those moments, in a no-man’s land no team typically feels responsible for. The logic is always circular: Why would the team adding a third option have to do something a team adding a second option didn’t have to do? Why would the team adding the second option worry in advance about option number 5?

This is why it’s important to hire and recognize people who will understand that those limitations have to be imposed arbitrarily, and empower them to be able to say, “Let‘s not add this. We like our own stickers better.”

My MacBook does have a sticker, which Iboughtand put on it since for some reason I find it really funny.

Jul 29, 2026
* complexity21systemdesign4
* systemdesign4