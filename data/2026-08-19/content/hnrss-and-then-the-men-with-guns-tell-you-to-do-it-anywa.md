---
title: And then the men with guns tell you to do it anyway – Terence Eden’s Blog
url: https://shkspr.mobi/blog/2026/08/and-then-the-men-with-guns-tell-you-to-do-it-anyway/
site_name: hnrss
content_file: hnrss-and-then-the-men-with-guns-tell-you-to-do-it-anywa
fetched_at: '2026-08-19T11:23:14.041941'
original_url: https://shkspr.mobi/blog/2026/08/and-then-the-men-with-guns-tell-you-to-do-it-anyway/
author: Terence Eden
date: '2026-08-18'
published_date: '2026-08-17T12:34:24+01:00'
description: In early February 2011 Egypt was in the middle of a political revolution. One morning, everyone's phones suddenly pinged with an alert. The Armed Forces asks Egypt's honest and loyal men to confront the traitors and criminals and protect our people and honour and our precious Egypt. A series of messages arrived all ostensibly from the network provider Vodafone. All pro-regime and all with the…
tags:
- hackernews
- hnrss
---

In early February 2011Egypt was in the middle of a political revolution. One morning, everyone's phones suddenly pinged with an alert.

The Armed Forces asks Egypt's honest and loyal men to confront the traitors and criminals and protect our people and honour and our precious Egypt.

Aseries of messages arrivedall ostensibly from the network provider Vodafone. All pro-regime and all with the undercurrent of violence.

Why did Vodafone send these messages? Earlier in the week,all Internet access was cut offnow phones were blasting propaganda to the masses.

After the network went down, Vodafone issued a statement saying:

It has been clear to us that there were no legal or practical options open to Vodafone, or any of the mobile operators in Egypt, but to comply with the demands of the authorities.

Do you have to follow orders? Do you have to obey the law even when it is unjust? Should multinational corporations instruct local executives to be loyal to their parent company or the rulers of the country they live in?

After the messages came in - including promises that "The Armed Forces cares for your safety and well being and will not resort to using force against this great nation" - Vodafone Global, safely ensconced in the UK, put out another statement:

Under the emergency powers provisions of the Telecoms Act, the Egyptian authorities can instruct the mobile networks of Mobinil, Etisalat and Vodafone to send messages to the people of Egypt. They have used this since the start of the protests. These messages are not scripted by any of the mobile network operators and we do not have the ability to respond to the authorities on their content.

Vodafone Group has protested to the authorities that the current situation regarding these messages is unacceptable. We have made clear that all messages should be transparent and clearly attributable to the originator.

Statements - Vodafone Egypt

A few years later I was at a networking event chatting to a guy. We'd both previously worked for Vodafone. Me in the UK, he in Egypt. I asked him about the incident - he talked about how they built the SMS infrastructure, what they did to secure it, how they prevented spam, and how one day armed men arrived.

I suspect most of us have seen a movie where some flunky in an office refuses the baddies demands to open the safe, and then gets shot in the head. Perhaps you think that's a noble death? He lived with honour and refused to yield! But, in every movie I've seen, the guy's subordinate opens the safe anyway and gets to live.

But we're technologists, right? We can build fail safes and cryptographic proofs andsimply build infrastructure that can't be abused.

And then the men with guns come and tell you what to do.

I've written before aboutCivic Hygiene- it's the idea that we should be mindful of the ways that our technologies could be misused. The term was coined back in 2010 by the technologist Bruice Schneier

It's bad civic hygiene to build technologies that could someday be used to facilitate a police state.

But what do we mean by that?

We don't want backdoors in security products - lest hackers break in or evil governments get elected. But we want a way to access our beloved ones' data after they die. It's important that we know that photos haven't been manipulated by propagandists and saboteurs. But we want to send funny memes about that politician we don't like. We don't want police stalking ex girlfriends' cars - but we want dangerous drivers prosecuted.

We want to be alerted about imminent threats, but don't want Governments to use that power for ill.

Way back in the early 2020s, I had a minor role in the UK Government's adoption ofCommon Alerting Protocolthe technology which powers cell-broadcast emergency alerts.

Even back then, one of the discussions was around whether the utility of being able to send an unavoidable push notification was worth the risk that someone would send an inappropriate message. Fresh in everyone's minds was thefalse alarm saying missiles were heading to Hawaii.

Too many safeguards means that a genuine alert doesn't get sent in time. Too few safeguards and you can blame "Human Error" for any mistakes.

I don't know which safeguards are in place for the UK's system -and most details are exempt from Freedom of Information requests. But it is both easy and fun to speculate on how such a system might be designed.

The Government generates an alert. It specifies where and when the alert should be sent. It sends that message to the network operators via a secure and private channel. Perhaps they also do some out-of-band verification like having the network operator call a pre-determined phone number to check the message's validity.

At which point, the operator can choose to send the message or not.

Or can they?

In August 2026, the UK government instructed network operators to send this message:

Did the networkshaveto send that message? If they thought it wasn't serious enough, could they have refused? As far as I can tell, the law only talks about the fact that operators can disregard "spam" laws in order to send a mass message:

A relevant public communications provider (P) may, for the purpose of providing an emergency alert service, disregard the restrictions on the processing of data relating to users or subscribers set out in paragraph (2) if the conditions set out in paragraph (3) are met.

[…]

(3) The conditions are—

(a)P is notified by a relevant public authority that—

(i)an emergency within the meaning of section 1(1) of the Civil Contingencies Act 2004 has occurred, is occurring or is about to occur;

Statutory Instrument 2015 No. 355

I'm no expert, but I can't see anything inthe spectrum licencenor in theWireless Telegraphy Actwhichcompelsoperators to process these messages.

The usual British way is to ask people to play nicely and threaten them with regulation if they don't.

Could the networks have refused to send the message about wildfires - or indeed any other message? If your least favourite politician gets their hands on the emergency alert system and tries to abuse it, would you want the networks to stand up to them?

What if the network refuses to send the message because they're worried alerting people about a hurricane will lower the company's profits?

What if armed thugs are sent in and the choice is send the message or die?

I don't know what the answer is here. I think most people agree that it is broadly sensible to have a way to alert the population of emergencies. There's no mass media any more, we're not all listening to a single radio channel, or reading newspapers, or even on the same social media platforms. Sometimes there are emergencies and the Government has a duty to alert people to them.

How would you design a system that simultaneously achieved all these goals:

* Rapid sending of messages
* Careful checking of the content of messages
* Ability to quickly target a specific geographic area
* Inability to mistakenly send a test message
* Requiring strong proof that the message is authentic before sending
* Resilient enough to work after significant damage to infrastructure
* That networks have the ability to vet and ignore
* That networks are compelled to send
* Which can only be used for good
* And cannot be used for evil.

In truth,having experienced fire-starters, I'm not bothered about the contents of this latest message from the UK Government. Given the overstretched fire service and the imminent threat across most of the country, my personal opinion is that it is proportionate.

But it is easy to see why some people feel this might open the gateway to messages which, at best, are irrelevant and, at worst, are similar to the insidious propaganda which appeared on the phones of Egyptians:

To every mother-father-sister-brother, to every honest citizen. Preserve this country as the nation is forever.

Perhaps you can think of a way to design an alerting system which cannot be abused - but I can't.

## Share this post on…

## 9 thoughts on “And then the men with guns tell you to do it anyway”

1. ### Kian RyanOn previous test messages, a warning period was given before the message was sent. This allowed people with hidden phones to make plans in advance. While the nature of the emergency was serious, there was no imminent threat to life, and as such, at a minimum, a warning period could have been issued before sending the message.The range of responses from people alarmed when the message was received indicates that this was not a proportionate action to the risk and alarm generated to people at risk, operators, drivers, etc.I'm quite glad I was only holding a soldering iron.Reply2026-08-17 12:47
2. ### Simon Brooke@blogit would be technically possible to have an agreed list of specific message texts:1. Nuclear missiles incoming, bad luck.2. Expanding fire near <location>, evacuate immediately if within <distance>.3. Toxic gas release near <location>, stay indoors, close all doors and windows.And so on. This has the benefit that the actual texts boilerplate text can already be present on people's devices in their preferred language, and only a code and parameters need be sent; and, harder to abuse.Reply|Reply to original comment on mastodon.scot2026-08-17 13:04### m_eiman@simon_brooke@blogNot a bad idea, but I'd guess that something along these lines will happen: you're pretty much guaranteeed to forget some important template, and if there wasn't one already we'll soon add a "<any text here>" template, and we're back to square one (with a bunch of unused templates everywhere)…Reply|Reply to original comment on mastodon.sdf.org2026-08-17 13:16### Simon Brooke@mikaeleiman@blogyou'd obviously have to have a protocol to update the list of approved messages. But the principle that parameters could only be numeric or locations would be very easy both to police and to defend.And by 'location' I mean something like latitude/longitude, ordnance survey grid ref, or similar. I don't think the protocol should allow any free text fields, specifically because any free text can be abused.Reply|Reply to original comment on mastodon.scot2026-08-17 13:29### m_eiman@simon_brooke@blogYeah, as long as free text can be kept out it could work. I'm just pessimistic about the likelihood of keeping it outReply|Reply to original comment on mastodon.sdf.org2026-08-17 13:47
3. ### m_eiman@simon_brooke@blogNot a bad idea, but I'd guess that something along these lines will happen: you're pretty much guaranteeed to forget some important template, and if there wasn't one already we'll soon add a "<any text here>" template, and we're back to square one (with a bunch of unused templates everywhere)…Reply|Reply to original comment on mastodon.sdf.org2026-08-17 13:16### Simon Brooke@mikaeleiman@blogyou'd obviously have to have a protocol to update the list of approved messages. But the principle that parameters could only be numeric or locations would be very easy both to police and to defend.And by 'location' I mean something like latitude/longitude, ordnance survey grid ref, or similar. I don't think the protocol should allow any free text fields, specifically because any free text can be abused.Reply|Reply to original comment on mastodon.scot2026-08-17 13:29### m_eiman@simon_brooke@blogYeah, as long as free text can be kept out it could work. I'm just pessimistic about the likelihood of keeping it outReply|Reply to original comment on mastodon.sdf.org2026-08-17 13:47
4. ### Simon Brooke@mikaeleiman@blogyou'd obviously have to have a protocol to update the list of approved messages. But the principle that parameters could only be numeric or locations would be very easy both to police and to defend.And by 'location' I mean something like latitude/longitude, ordnance survey grid ref, or similar. I don't think the protocol should allow any free text fields, specifically because any free text can be abused.Reply|Reply to original comment on mastodon.scot2026-08-17 13:29### m_eiman@simon_brooke@blogYeah, as long as free text can be kept out it could work. I'm just pessimistic about the likelihood of keeping it outReply|Reply to original comment on mastodon.sdf.org2026-08-17 13:47
5. ### m_eiman@simon_brooke@blogYeah, as long as free text can be kept out it could work. I'm just pessimistic about the likelihood of keeping it outReply|Reply to original comment on mastodon.sdf.org2026-08-17 13:47
6. ### Sinjo@EdentWhile I disagree with that specific alert being sent out, I agree that it’s not reasonable or even possible for network operators to act as a filter on the government where they operate.It’s a small sample, but I now have a bunch of friends who’ve turned those alerts off entirely. I think the mechanism will lose its effectiveness through overuse.Reply|Reply to original comment on tech.lgbt2026-08-17 14:11
7. ### Steven D. Brewer 🏳️‍⚧️@EdentThis reminds me of the xkcd about security:https://xkcd.com/538/SecurityReply|Reply to original comment on wandering.shop2026-08-17 15:15
8. ### JulianI wonder how damaging this would actually be:The banks are under cyber-attack, you must withdraw cash immediately.Reply2026-08-17 16:15
9. ### news.ycombinator.comAnd then the men with guns tell you to do it anyway | Hacker NewsReply|Reply to original comment2026-08-18 19:31
10. ### More comments on Mastodon.

### Trackbacks, Pingbacks, and Boosts

1. ### David C. Norris 🇺🇦 🗽TIL: "Civic Hygiene"#CivicHygiene2026-08-17 12:45

### What are your reckons?Cancel reply

All comments are moderated and may not be published immediately. Your email address willnotbe published.

Comment:

See allowed HTML elements:

<a href="" title="">
								
<abbr title="">
								
<acronym title="">
								
<b>
								
<blockquote cite="">
								
<br>
								
<cite>
								
<code>
								
<del datetime="">
								
<em>
								
<i>
								
<img src="" alt="" title="" srcset="">
								
<p>
								
<pre>
								
<q cite="">
								
<s>
								
<strike>
								
<strong> 
							

Your Name (required):

Your Email (required):

Your Website (optional):

 

To respond on your own website, write a post which contains a link to this post - then enter the URl of your page here.Learn more about WebMentions.

URL/Permalink of your article