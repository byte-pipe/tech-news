---
title: A bug which only affected left-handed users – Terence Eden’s Blog
url: https://shkspr.mobi/blog/2026/07/a-bug-which-only-affected-left-handed-users/
site_name: tldr
content_file: tldr-a-bug-which-only-affected-left-handed-users-terenc
fetched_at: '2026-07-09T19:36:46.889411'
original_url: https://shkspr.mobi/blog/2026/07/a-bug-which-only-affected-left-handed-users/
author: Terence Eden
date: '2026-07-09'
published_date: '2026-07-08T12:34:43+01:00'
description: Verily, some of our brethren (and sistren) be afflicted with a sinister disposition. While the righteous scroll using the thumb of their right hand - as is good and proper - an accurs'd minority swing the other way. Look, you try writing an interesting bug report without sounding like a clanker, OK! I try to optimise my blog as much as possible. It may not look like much, but it has got it…
tags:
- tldr
---

Verily, some of our brethren (and sistren) be afflicted with a sinister disposition. While the righteous scroll using the thumb of their right hand - as is good and proper - an accurs'd minority swing the other way.

Look, you try writing an interesting bug report without sounding like a clanker, OK!

I try to optimise my blog as much as possible. It may not look like much, but it has got it where it counts. I've made a lot of special modifications myself to the base WordPress install.

One of those modifications is reducing the amount of JavaScript in use to the bare minimum. Everything functions without it, but there are a few places where it helps - the most notable being comments.

That's why I was distressed when a loyal reader wrote in saying there was a bug on my site. When they were scrolling the page a comment box would suddenly appear and interrupt their browsing.

I scroll my own site a lot (probably more than is healthy) so why hadn't I noticed this bug?

Because I scroll on my phone's touchscreen with my right thumb and the bug reporter uses their left. The "reply" link which was being triggered is on the left side of the page. A bug which won't be triggered by righteous people but infuriating to those who will surely be left behind after The Rapture™.

To be fair,this bug was reported seven years ago- but I guess the WordPress team have been too busy cleaning up after their mad God-Emperor to take a look at it.

Back in 2017, a developeradded atouchstartlistener to link clicks. I don't really understand why. At one point in history, browsers couldn't be sure if a touch event was the start of aclickor a double-tap to zoom. So firing an event when a touch occurred on a link sort of made sense to avoid a 300ms delay.

But that hadn't been the case for several years -as this 2013 blog post makes clear. Even in 2015it was no longer an issue.

So why was this lefty-baiting code added? Not a clue.

Anyway,seven yearsafter the bug was reportedI committed a fix. It isn't the most sophisticated change to WordPress - merely deleting a couple of lines. But hopefully it will stop those strange and unusual mutants from complaining that their unnatural thumb-usage is accidentally triggering unwanted events on my website.

Sadly, there is as yet no way to prevent the corrupt from using our blessed sites. The WHAT-WG haven't seen fit to take on board my suggestion of<meta handed="right">to keep out the unwanted and polluted. So, hopefully, this change will at least prevent them complaining.

Why, yes officer, I have had a glass or two of tonic wine. Why do you ask?

## Share this post on…

## 8 thoughts on “A bug which only affected left-handed users”

1. ### Cassidy Leftthebuilding“By faith did Abraham thumb left handed and it was accorded to him righteousness.”
Left handed but tend to scroll left handed only on my phone but right handed on a tablet. English makes a lot of historically bigoted assumptions: right handedness, gender binaries, color and handedness based correctness and morality, and others. Most of these are still taken for granted, even fought over, in a time when reason should have long since supplanted superstition. Walking a mile in another’s shoes is just as valid today for empathy as it was 2000 years ago. I’m left handed, queer, ethnically a mutt, with mild visual impairment and bipolar. I continually struggle with American exclusionary assumptions in life most of us never question and often react poorly when they are. Thank you for making the effort and for the humor. I loved it.Reply2026-07-08 15:55
2. ### Steph Driverthis got me thinking - as a right-handed person, I hold my phone in my left hand, scroll with their left thumb, so that the right hand is free to type.And why wouldn’t you hold your phone in your less-dextrous hand?Reply|Reply to original comment on bsky.app2026-07-08 17:17### Job van der ZwanAs a lefty who once upon a time looked into the design of bimanual interfaces for his master thesis, all I can say is: Yves Guiard would be proudhttps://www.lri.fr/~mbl/ENS/FONDIHM/2013/papers/Guiard-JMB87.pdfReply2026-07-08 20:44### Dajve BlokeAs a lefty, i tend to use my right hand to work mouse or phone, for a similar reason to you - it allows me to use my dominant hand to jot notes down when this becomes necessary.Reply2026-07-08 21:16
3. ### Job van der ZwanAs a lefty who once upon a time looked into the design of bimanual interfaces for his master thesis, all I can say is: Yves Guiard would be proudhttps://www.lri.fr/~mbl/ENS/FONDIHM/2013/papers/Guiard-JMB87.pdfReply2026-07-08 20:44
4. ### Dajve BlokeAs a lefty, i tend to use my right hand to work mouse or phone, for a similar reason to you - it allows me to use my dominant hand to jot notes down when this becomes necessary.Reply2026-07-08 21:16
5. ### DenilsonTruth to be told, I have faced this bug myself; and I'm right-handed. I just never bothered to report it. Mostly because reporting it requires more energy and time than I have available whenever I'm reading on the phone.Reply2026-07-08 18:47
6. ### news.ycombinator.comA bug which affected only left handed users | Hacker NewsReply|Reply to original comment2026-07-08 19:20
7. ### TRXIt happens in Fennec (Firefox) on Android on my Samsung tablet. Scrolling works fine, until it suddenly either zooms or shrinks the font, even though my right thumb is swiping the exact same spot it always does.Reply2026-07-08 22:53
8. ### nopeI too use my phone in my left hand frequently, even though I'm right handed. I thought this was something most people do, but since that wordpress bug went unfixed for so long, maybe it actually isn't?Funny how easy it is to make an assumption and never really notice you're making it, until suddenly something calls it into question.Reply2026-07-09 19:50
9. ### More comments on Mastodon.

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