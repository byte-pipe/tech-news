---
title: I paid people to try and follow my README – Terence Eden’s Blog
url: https://shkspr.mobi/blog/2026/10/i-paid-people-to-try-and-follow-my-readme/
site_name: hnrss
content_file: hnrss-i-paid-people-to-try-and-follow-my-readme-terence
fetched_at: '2026-10-11T16:33:05.504621'
original_url: https://shkspr.mobi/blog/2026/10/i-paid-people-to-try-and-follow-my-readme/
author: Terence Eden
date: '2026-10-11'
published_date: '2026-10-11T12:34:39+01:00'
description: Developers suck at writing documentation. We like to say RTFM but often there ain't no FM to R. At best we have a half-arsed collection of notes, some obsolete tips, and a link to a desolate forum full of people asking the same questions again and again. That's no way to treat our users. I naïvely believe there's a better way. As I've written before, you should sit down and actually test your …
tags:
- hackernews
- hnrss
---

Developers suck at writing documentation. We like to say RTFM but often there ain't no FM to R. At best we have a half-arsed collection of notes, some obsolete tips, and a link to a desolate forum full of people asking the same questions again and again. That's no way to treat our users.

I naïvely believe there's a better way. As I've written before, you should sit down andactuallytest your readme. Spin up a fresh Virtual Machine, go through what you've written, and see if it makes sense.

But it isreallyhard to ignore your own biases. Of course you know that certain commands requiresudoand obviously when you wrote-fooyou meant--fooand everyone knows that you have to reboot afterwards.

How do you get rid of those biases? I paid people!

As part of myNLnet grant application for ActivityBot, I said I wanted to test the install experience with real users and I was prepared to pay them €25 for an hour of their time. I stuck out the call on Mastodon, gathered a few people, and had a video call with them.

The format was simple. I explained that I was looking for feedback on the first-run experience. I knew that it wasn't perfect and actively wanted constructive criticism. I asked the volunteer to share their screen and, crucially, to speak aloud. Tell me what they were doing. What they didn't understand, what confused them, what delighted them, what frustrated them, etc.

I took notes by hand (fuck feeding the machine) and spent several hours being told what incorrect assumptions I'd made.

Amongst the highlights I discovered were:

* The link to the demo tool was wrong.
* Some people read a README in the terminal.
* What does it actually mean to rename a file?
* How do you rename a hidden file?
* Should a demo tool be available on the web or just the user's local machine?
* Why does some text explicitly need to be quoted and some not?
* My jokes aren't funny and are actively confusing.
* Some of the technical terminology needed explaining.
* The ordering of the different sections was confusing.
* I hadn't actually explained what the software would do.
* A whole section which was technically interesting to me was utterly confusing to everyone else.
* Not all web servers use permissions in the same way.

And on it went!

After each session I updated the README based on what people found difficult, then I re-tested it with the next person.

In total, I paid out around €150 to have a bunch of people criticise me to my face. Hey, cheaper than therapy, right?

I know someone is going to say "why not just ask an LLM to simulate a range of users?" The answer is very simple - I want to speak to real people. People are brilliant! They can make you laugh, you can see their cat when it wanders on to the call, they bring a unique perspective to the problem, and they're really happy when you give them a €25 voucher. Some will gladly do it for free and makeyouhappy!

When I was doing technical writing for GOV.UK, all my beautiful prose was given a second-eye by another human. They eviscerated all my flowery phrases and turned the document into something more readable. They were the ones who caught the mistakes that no spell chequer could. They were able to have a proper conversation with me. More importantly, I couldhearthe frustration in their voice - that's the thing which lets you know a mistake needs to be corrected.

I don't claim thatActivityBot's READMEis now perfect - far from it - but it is now demonstrably easier to follow. Developers need to talk torealpeople. You don't have to pay them if you can't afford it - but find a few people who will talk aloud while they try to follow your instructions. I guarantee you that your README will become much better for it.

## Share this post on…

## 2 thoughts on “I paid people to try and follow my README”

1. ### news.ycombinator.comI paid people to try and follow my README | Hacker NewsReply|Reply to original comment2026-10-11 12:01
2. ### James AylettOh, this is great. In an ideal world we'd see specific grants available to support this kind of thing (and documentation writing in general, although ISTR that some of the OSS grant giving has documentation as a category).Reply|Reply to original comment on bsky.app2026-10-11 13:44
3. ### More comments on Mastodon.

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
								
<img src="" alt="" title="" srcset="" width="" height="">
								
<p>
								
<pre>
								
<q cite="">
								
<s>
								
<strike>
								
<strong> 
							

Your Name (required):

Your Email (required):

Your Website (optional):

 

Posted a response on your own website? Share the link here:Your post must include a link to this post.

Send Webmention

How does this work?

To respond on your own website, write a post which contains a link to this post - then enter the URl of your page here.
								
Learn more about WebMentions
.