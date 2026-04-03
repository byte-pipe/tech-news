---
title: 'Tell HN: HN was down | Hacker News'
url: https://news.ycombinator.com/item?id=46301921
site_name: hackernews
fetched_at: '2025-12-18T11:07:29.634992'
original_url: https://news.ycombinator.com/item?id=46301921
author: uyzstvqs
date: '2025-12-18'
---

Hacker News
new
 |
past
 |
comments
 |
ask
 |
show
 |
jobs
 |
submit
login
Tell HN: HN was down
567 points
 by
uyzstvqs

18 hours ago

 |
hide
 |
past
 |
favorite
 |
307 comments
- HN errored on all authenticated requests with 502 Bad Gateway. It did still respond to a limited amount of unauthenticated requests with presumably cached pages, which did not get updated. The last post on /newest claimed "0 minutes ago", but was actually much older (1:32:57 PM GMT) and not the newest post.

- This status page actually identified the outage:https://hackernews.onlineornot.com/- Pages by Hund and Statuspal did not show the outage.- The last post before the outage washttps://news.ycombinator.com/item?id=46301823(1:39:59 PM GMT). The last comment washttps://news.ycombinator.com/item?id=46301848(1:41:54 PM GMT).- There was an average of ~4 seconds per comment just prior to the outage. Based on this, HN likely went down at 1:41:58 PM GMT.

dang

16 hours ago

 |
next

[–]

Yes, sorry! We're investigating, but my current theory is we got overloaded because I relaxed some of our anti-crawler protections a few days ago.

(The reason I did that is that the anti-crawler protections also unfortunately hit some legit users, and we don't want to block legit users. However, it seems that I turned the knobs down too far.)In this case, though, we had a secondary failure: PagerDuty woke me up at 5:24am, I checked HN and it seemed fine, so I told PagerDuty the problem was resolved. But the problem wasn't resolved - at that point I was just sleeping through it.I'll add more as we find out more, but it probably won't be till later this afternoon PST.

reply

shlomo_z

16 hours ago

 |
parent
 |
next

[–]

Crazy that Dang literally manages HN in his sleep!

We all knew that but I haven't seen any confirmation before this.

reply

easterncalculus

10 hours ago

 |
root
 |
parent
 |
next

[–]

I like hacker news but I don't think this site is worth getting paged over lol

reply

archon810

5 hours ago

 |
root
 |
parent
 |
next

[–]

You might be underestimating HN's popularity.

reply

locknitpicker

4 hours ago

 |
root
 |
parent
 |
next

[–]

> You might be underestimating HN's popularity.

I think you're confusing popularity with criticality. I'm sure everyone in here can withstand a few hours without browsing the page.

reply

bayindirh

2 hours ago

 |
root
 |
parent
 |
next

[–]

If you like the thing you're managing, then its health is critical for
you
, not your users.

It's dang's baby at this point, and this is a good thing, as long as HN doesn't affect his life in ways he doesn't want.

reply

locknitpicker

2 hours ago

 |
root
 |
parent
 |
next

[–]

> If you like the thing you're managing, then its health is critical for you, not your users.

Get a grip and go touch some grass. Even FANGs understand the concept of business hours SEV.

reply

bayindirh

33 minutes ago

 |
root
 |
parent
 |
next

[–]

I have a pretty firm grip on life and touch plenty of grass both literally and figuratively.

However, when something I care about crashes and burns once in a blue moon, I make sure to put the fire out, at least to make it survive till regular hours. Things I care about can be both business and personal, and nobody bugs me for them.Maybe we shouldn't make any assumptions about people we don't personally know, while we are at it.

reply

dang

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

failing to manage HN in my sleep is more like it

reply

jonny_eh

15 hours ago

 |
root
 |
parent
 |
next

[–]

Your sleep is more important than our work distraction.

reply

seemaze

10 hours ago

 |
root
 |
parent
 |
next

[–]

I was curiously productive this morning..

reply

koakuma-chan

9 hours ago

 |
root
 |
parent
 |
next

[–]

I took a shower for the first time in one week

reply

bigbuppo

3 hours ago

 |
root
 |
parent
 |
next

[–]

Bet that felt great.

reply

fouc

6 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

looks like a redditor snuck into HN

reply

arnavpraneet

5 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

came back just in time for me to spend the first hour of my work

reply

zenoprax

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Which is fine! I don't mind if it's down for a few hours. It reminds me that it's just a place to stop by for a bit before moving on. Like a digital coffee shop that sometimes has a leaky pipe and isn't open right at 7am.

I hope it doesn't change (much).

reply

wkat4242

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You're still a miracle worker. Single-handedly managing a well-known fully user-contributed site not just technically but moderation in contentious times like these and still keeping it working well and encouraging a positive user community can't be an easy task.

reply

dang

5 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks, I'll take it! except for the single-handedly part - gotta share the love with
https://news.ycombinator.com/posts?id=tomhow
.

reply

franciscop

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

No worries, please take care of your sleep and thanks for all your hard work

reply

dijit

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

We all have our moments, and I personally consider HN to be “best effort”, almost like a volunteer project. I’m not certain I’m correct: but thats the optics I have so my expectations are adjusted to that.

So don’t beat yourself up please.When I worked for “SaaS unicorn” we typically had multiple levels of escalation, and acknowledging would have done nothing because the alarm would continue firing until fixed. Not sure what’s changed in 15 years of ops, I had assumed it would be better now- I can’t imagine silencing an alert totally by acknowledging it- if its still occurring.I’m totally fine with how you handled it, if anything I am thankful. But that seems to be a system I would improve if I had the time.“mute” is different than “resolve” to me, and both should exist. (Where mute is an acknowledgement of an issue as ongoing.)

reply

giancarlostoro

15 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah we don't exactly pay to be on HN, not much to complain about. I appreciate everyone who works on HN.

reply

jacquesm

9 hours ago

 |
root
 |
parent
 |
next

[–]

We pay with content and with the fact that we attract the talent that eventually ends up powering ycombinator investment rounds.

reply

phantasmish

9 hours ago

 |
root
 |
parent
 |
next

[–]

It’s ad-supported. Any post with comments disabled is definitely an ad. Probably a lot of the others are, too.

reply

abustamam

5 hours ago

 |
root
 |
parent
 |
next

[–]

Your comment makes me realize that I consume HN differently than many others, because I've never seen a post with comments disabled and I've been around here for at least ten years. It's not that I don't think they don't exist — they obviously do because you're mentioning them. I've just never encountered one, primarily because I don't casually browse HN, ever. I subscribe to a pushbullet channel that notifies me when a post hits 500 up votes. That's it. The list of submissions on the home page (even on reddit) is just overwhelming to me so I use the pushbullet channel as a sort of community curated "best of" or "trending" signal.

Not to say that I don't procrastinate or waste time doing other nonsense. I can definitely spend a lot of time reading HN comments, as I'm doing right now.Anyway,anyone who finds themselves with a problem with HN should try that out :)

reply

mysterydip

7 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I assumed the main purpose was to show off the ycombinator batches when they launch.

reply

scottlamb

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

This. If it were a business-critical money fountain, I'd expect follow-the-sun SRE coverage. I don't think it is, so I can probably accept drinking my morning coffee without scrolling HN once in a while. There's only so much one can beat oneself up about a slow/incorrect response when the on-call is handled by what, just one person? maybe two people in the same time zone?

(Might be wise though to have PagerDuty configured to re-alert if the outage persists.)

reply

notachatbot123

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

And that is a good thing. Sleep tight!

reply

sizzle

7 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Time to train an AI agent on your moderation activity and get some well deserved sleep!

reply

dang

5 hours ago

 |
root
 |
parent
 |
next

[–]

We're working on it! well, some of it.

I'm pretty happy with how it's developing—the trendline is promising—but not ready to rely on it in prod yet.

reply

nubinetwork

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I was starting to think you never slept, I remember that one time I emailed you at 1am. :)

reply

commandersaki

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Do you have nightmares of failing to manage HN when you sleep too?

reply

djmips

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I appreciate what you do. Hope you got some rest when it was all over.

reply

feczeri_c

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You deserve a lot of rest!

reply

sailfast

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Yeah, I mean how dare you?! I pay good money for high uptime SLAs! :)

reply

qingcharles

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I was today years old when I found out Dan sleeps.

reply

gaudystead

13 hours ago

 |
root
 |
parent
 |
next

[–]

I was today years old when I found out that dang's first name is Dan

reply

anonymous908213

12 hours ago

 |
root
 |
parent
 |
next

[–]

You'll never guess what letter dang's last name starts with.

reply

smolder

12 hours ago

 |
root
 |
parent
 |
next

[–]

A as in Ang, clearly.

reply

qingcharles

12 hours ago

 |
root
 |
parent
 |
next

[–]

No, he's Asian. The
n
 is doing double-duty. His last name is Ng :p

reply

fragmede

8 hours ago

 |
root
 |
parent
 |
next

[–]

That's exactly what a French person with the last name of Les would say!

reply

sizzle

7 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

What if Dang made an AI agent of himself for when he sleeps?

reply

utopcell

8 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

By demonstration he didn't.

reply

xandrius

13 hours ago

 |
parent
 |
prev
 |
next

[–]

Hey dang, don't worry. It's just a site for reading articles and reacting to them.

Enjoy your deserved sleep and if for a couple of hours it's down, so be it.Thanks for your continued service!

reply

powvans

13 hours ago

 |
root
 |
parent
 |
next

[–]

100%

Though I will say, HN is a pretty great source of information about major outages like the recent AWS and Cloudflare issues. I had a moment this morning where I thought, oh, is there a larger issue and then, oh, HN is down, huh, the next option is so far down my list that it's going to take me a moment to think of it.I hope that serves as a testament to how great this site and the community is. Thanks for all your hard work keeping it that way!

reply

derrida

11 hours ago

 |
root
 |
parent
 |
next

[–]

> huh, the next option is so far down my list that it's going to take me a moment to think of it.

Option 4: take your grab bag with the tcp over IP shortwave radio, sextant and head for pre-cached month supply of food in the hills.

reply

rldjbpin

58 minutes ago

 |
parent
 |
prev
 |
next

[–]

> The reason I did that is that the anti-crawler protections also unfortunately hit some legit users, and we don't want to block legit users.

it is a shame that it needs to be this way. as a lurker who doesn't stay logged in nor use incognito mode, i have seen "Sorry" page way too often, even when opening the "past" page from the homepage.truly hope you find a solution that reduces friction for all. personally, it is back to "Sorry" situation for now.PS: for others facing a similar situation, it all disappears after logging in, which has been the most reliable solution thus far.

reply

Imustaskforhelp

14 hours ago

 |
parent
 |
prev
 |
next

[–]

I was personally worried if there was some major outage of the whole world or something the first time hackernews didnt work because I didnt expect hackernews to go down but rather, something even more catastrophic than aws going down must happen (because we see major cloud outage posts)

https://downforeveryoneorjustme.com/hacker-newsThis website had many instances of reports, the last I saw were 52 reports in only a short frame of time, the maximum reports on this are 118 it seems.> In this case, though, we had a secondary failure: PagerDuty woke me up at 5:24am, I checked HN and it seemed fine, so I told PagerDuty the problem was resolved. But the problem wasn't resolved - at that point I was just sleeping through it.Its okay I suppose, have you figured out who is crawling hackernews so much tho, was it a ddos attack or an AI company trying to get data, doesn't hackernews support an api and I am sure that there are datasets for it too so Its interesting why they might crawl but we all know the reasons why as they have been discussed here.

reply

neilv

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Maybe it would be fine if ops alerts were silenced during normal US sleeping hours?

HN is important, but unlikely much harm could be done before morning.(Source: Lost a lot of sleep at one place, enough to realize that sleep interruption and deficit has significant costs.)

reply

Rooster61

16 hours ago

 |
parent
 |
prev
 |
next

[–]

No apology needed. We all needed to stop procrastinating anyways :)

reply

tsoukase

15 hours ago

 |
parent
 |
prev
 |
next

[–]

During the last week my IP was banned for unknown reason. Glad to hear it might not be a problem from my side.

reply

dang

12 hours ago

 |
root
 |
parent
 |
next

[–]

Yes, sorry! This is the problem - we don't want to block legit users, but if we loosen the bolts, we get flooded.

If you browse HN while logged in, that should immunize you against this happening. Also, if it does happen again, you can unban your IP as described athttps://news.ycombinator.com/newsfaq.html. But you have to do that from a different IP address, of course.If those things don't work, email hn@ycombinator.com and we'll get it sorted.

reply

tsoukase

2 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks. It is so easy to change the IP using mobile that the unbanning is little hassle.

reply

_shadi

56 minutes ago

 |
parent
 |
prev
 |
next

[–]

> anti-crawler protections

what type of protections are used on HN? rate-limiting? ip range blacklist?

reply

andy_ppp

15 hours ago

 |
parent
 |
prev
 |
next

[–]

I’d love to know more about what running a site like HN involves, would be great to get a write up of what it’s like running something like this at this scale (and what kind of traffic you guys get)!

reply

alwa

15 hours ago

 |
root
 |
parent
 |
next

[–]

I can’t put my finger on anything within the last decade, but I seem to recall it running in something close to its current form on a single core on a single server for a long time:

https://news.ycombinator.com/item?id=5229522Re: traffic, dang said (2022):https://news.ycombinator.com/item?id=33454140I took it as a good reminder that the hard part is the human part: that high-overhead features and UI fripperies are nice but not necessary (or sufficient) to keep a community healthy and vibrant over the decades.(And on the subject of the human side, if you didn’t catch Anna Wiener’s 2019 profile, it’s here:https://www.newyorker.com/news/letter-from-silicon-valley/th...)

reply

ilamont

14 hours ago

 |
root
 |
parent
 |
next

[–]

From dang's 2022 comment about traffic:

The most interesting number is the 1300 submissions because that hasn't grown since 2011 - it just fluctuates. Everything else has been growing more or less linearly for a long time, which is how we like it.I find that surprising, as 2011-2022 covers an exponential rise in SEO spam and "growth hackers" attempting to drive traffic and links.Or was 1,300 the number of non-flagged submissions?

reply

tempest_

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

The other reality is that as much as this industry is up its ass about scalability you can run a very very busy site on a single machine now a days.

A lot of people out here designing their blogs like its 1989.

reply

giancarlostoro

15 hours ago

 |
parent
 |
prev
 |
next

[–]

The transparency is deeply appreciated by me and others. We don't pay to keep HN on, so we cannot complain. Thank you and the rest of the team for all you do to give us a corner of the internet that is quite 'different' from the rest of the wild west that is the web.

reply

maxloh

14 hours ago

 |
parent
 |
prev
 |
next

[–]

Frankly, I don't understand why someone would even try to crawl Hacker News.

There is an official dump which doesn't even require parsing HTML at all:https://console.cloud.google.com/marketplace/details/y-combi...

reply

dang

12 hours ago

 |
root
 |
parent
 |
next

[–]

These are not, er,
experienced
 crawlers.

https://www.youtube.com/watch?v=Sbpl3ywNlpA#t=56s

reply

mmooss

14 hours ago

 |
parent
 |
prev
 |
next

[–]

In a situation like this one, good crisis leadership is essential. dang, HN will help you with tips from vast collected experience (please chip in):

1. Blame: The first thing to do is to point the finger. That doesn't mean analysing the technical issue, which can delay this step and limit your options, but figuring out who is politically easiest to blame. Often, that's the new guy, but outside contractors and vendors without good connections are also a common solution. Even if you are technically responsible for hiring them, you can always push them under the bus with a little skill. This small sacrifice helps unify, focus, and motivate the rest of the team.2. Emotion: Inject your emotion into the situation and make that the implicit, but indisputable priority. Particularly, outrage and anger -This is completely _____. These people are utterly _____(I'd use all caps, but that's not allowed on HN). Make sure everyone's attention is over their shoulder, on your emotion, and infect the team with it. Threats are an effective tool here - this is a crisis, and anyone who is calm is not emotionally engaged. Otherwise, they won't care enough about this problem - without you driving them, they probably wouldn't care much at all. Anyway, you don't have time for niceties like empathy or even basic respect.3. Speed: Respnsiveness to stakeholders is very important. People need answersnow. Give them answers they want to hear, outcomes they will be comfortable with. Don't worry if different groups hear different things. Your team will find a way to make it all work - that's their job.4. Communication: Good communication is essential. Make sure you clearly tell your team what they should be doing; repeat it several times to prevent misunderstanding. Especially people with experience can have minds of their own; keep them on track. The situation is a crisis so you can't take any risks; stay on top of them and everything they do, and give input if you're not certain they are doing exactly what you would be doing.5. Victimhood: Find a way to turn the tables: Make it about you, and how you're the victim here, and feed the fire with more outrage. With this and outrage, nobody will undermine the team by challenging your ideas or authority, which is the most essential component of a successful outcome. Remember, without you this all falls apart.Have I missed anything?

reply

yearolinuxdsktp

9 hours ago

 |
root
 |
parent
 |
next

[–]

Engagement: make sure that every member of the team is either on the incident bridge or has dropped what they are doing to watch you diagnose the problem. The more eyes on the problem, the more awareness of the pain will be absorbed by all. If members need to leave to get food or put children to bed, tell them to order delivery and to ask their spouse to do their job. Demonstrate human touch by allowing them to turn off camera while they are eating.

Comprehensiveness: propose extreme, sweeping solutions, such as a lights-out restart of all services, shutting down all incoming requests, and restoring everything to yesterday's backup. This demonstrates that you are ready to address the problem in a maximally comprehensive way. If someone suggests a config change rollback, or a roll-forward patch, ask them why are gambling company time with localized changes, and ask them why are they willing to gamble company time on technical analysis?Root Cause Analysis Meeting: spend the entire meeting time rehashing the events, pointing fingers and assigning blame. Be sure to mention how the incident could've been over sooner if you just restarted and rolled back every single thing. Be sure to demonstrate out-of-the-box thinking by discussing unrealistic grandiose solutions. When the time is up, run the meeting over by 30 minutes and force all to stay while realistic solution ideas are finally discussed in overtime. This makes it clear to the team that nothing is more important than this incident's RCA--their time surely is not. If someone asks to tap out to pick their kids up after school, remind them that they are making enough money to call them an Uber.Alerting: be sure to identify anything remotely resembling leading indicators, and add Critical-level wake-you-up alerts with sensitive thresholds for those indicator. Database exceeding 50% CPU? Critical! Filesystem queue length exceeding 5? Critical! Heap usage over 50%? Critical! 100 errors in one minute on a 100000 requests per minute service? Critical! Single log line indicating DNS resolution failure anywhere in the system? Critical! (What if AWS's DNS is down again?) Service requests rate 10% higher than typical peak? Critical! If anyone objects to such critical alerts, ask them why do they want to be responsible for not preventing the next incident?

reply

showcaseearth

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Short lived and driven by good intentions– all's good. Thanks again for keeping this thing going!

reply

bicepjai

16 hours ago

 |
parent
 |
prev
 |
next

[–]

Even after providing firebase endpoint, crawlers come to the site ?

reply

Bender

15 hours ago

 |
root
 |
parent
 |
next

[–]

Most crawlers have no concept of what that is. They will follow links to this site and then follow links out of this site even after being told not to [1]. The majority of crawlers follow zero rules, RFC's, etc... The few platforms that do follow standards and rules are akin to a law abiding citizen in Mos Eisley.

[1] - rel="nofollow"

reply

dang

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Oh my god. It's the crawlpocalypse.

reply

busymom0

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Unfortunately, the firebase API is very bad as they even acknowledge that in their github page.

reply

8cvor6j844qw_d6

13 hours ago

 |
parent
 |
prev
 |
next

[–]

> anti-crawler protections

Sometimes I could not open the comment section, receiving a blank page with "... We're sorry" or something along these lines when opening from new private window. It works when opening normally.Logging in on the private window seems to resolve the issue. Can you take a look on this if possible?

reply

dang

12 hours ago

 |
root
 |
parent
 |
next

[–]

Best to email your IP address to hn@ycombinator.com so we can see if it's blocked.

reply

nottorp

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Can't speak for others, but I'm sure i'll be pretty fine if no one gets woken up if HN is down...

Of course, they'd better restore service after they wake up naturally, because I need my HN dose. But it's not worth losing sleep over it.

reply

QuantumNomad_

10 hours ago

 |
parent
 |
prev
 |
next

[–]

> the anti-crawler protections also unfortunately hit some legit users, and we don't want to block legit users

Was the blocking returning “Sorry.” instead of any page content? A couple of days ago there was a few hours where when I’d go to HN I could load the main page as a non-logged in user. But if I tried to log in I would get “Sorry.” instead. I also got the sorry message if I tried to click on user profiles of other people and a few other pages.I am assuming that the reason I could see the front page itself and discussions on posts on the front page is that they were in a shared cache for non-logged in users, but that when I clicked on some pages like some random user pages those were not in cache and hit the origin server and it blocked those with “Sorry.” like it did for log-in attempts.I also tried to go to the unblock IP page, but that one also returned “Sorry.”For a while I was scratching my head wondering if I had gotten some malware on one of my computers that was aggressively making requests to HN, and that I had become IP banned because of that. Since I think my actual request rate from browsing and commenting should be pretty average. I read HN a lot, but notthatmuch :pLater in the day, or the next day, things were back to normal and I could log in again. Presumably after those anti-crawler protections had been relaxed again.

reply

irishcoffee

15 hours ago

 |
parent
 |
prev
 |
next

[–]

> The reason I did that is that the anti-crawler protections also unfortunately hit some legit users

How does this happen?

reply

Bender

15 hours ago

 |
root
 |
parent
 |
next

[–]

How does this happen?

Not the person you are asking. Bot operators have an incentive to make crawlers look as much like a human as possible so they do not get blocked. Some of them fail miserably and some nearly succeed. That makes it trivial to accidentally block a real person. I am personally fine with that given I do not pay for this site and have no SLA or contract with it.

reply

arccy

14 hours ago

 |
root
 |
parent
 |
next

[–]

some humans also try their best to make themselves look like bots...

reply

slater

14 hours ago

 |
root
 |
parent
 |
next

[–]

You're absolutely right!

reply

Imustaskforhelp

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

beep boop.

reply

ZuoCen_Liu

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

lol

reply

pjc50

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Every filter process has false positives and false negatives, especially when crawlers are trying to fake their status.

reply

ohhnoodont

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Last week if you are using a VPN + a browser that limits fingerprinting, you were likely to see error messages accessing HN.

reply

shmeeed

16 hours ago

 |
parent
 |
prev
 |
next

[–]

Looking forward to the post mortem. :)

reply

michelsedgh

16 hours ago

 |
root
 |
parent
 |
next

[–]

dang

reply

shmeeed

14 hours ago

 |
root
 |
parent
 |
next

[–]

In my defense, I was commenting at 0 min, since then he made several updates explaining the situation.

reply

dang

12 hours ago

 |
root
 |
parent
 |
next

[–]

Yes sorry! Normally I put in "[editing - bear with me...]" or some such.

reply

michelsedgh

10 hours ago

 |
root
 |
parent
 |
next

[–]

I was just trolling, thanks for ur work

reply

stmw

11 hours ago

 |
parent
 |
prev
 |
next

[–]

dang - just to say, we've all done it...

reply

walrus01

12 hours ago

 |
parent
 |
prev
 |
next

[–]

Just out of curiosity, if HN is still running on one physical system, what does a daily or weekly traffic chart look like for the switch port facing it?

reply

echelon

16 hours ago

 |
parent
 |
prev
 |
next

[–]

I didn't realize you were carrying the pager too! Kudos!

reply

malwrar

16 hours ago

 |
root
 |
parent
 |
next

[–]

I feel such a sense of kinship for anyone who carries a pager, almost 7 years at my current role doing it. Super cool that dang is among our number :)

reply

geocrasher

15 hours ago

 |
root
 |
parent
 |
next

[–]

Yep, have been on constant "pager duty" for 2+ years, although I have more help now and I get paged 1-3 times a week instead of per night. Still, carry my lappy everywhere I go. Bought an ARM Windows laptop to get that 20hr battery life so I could worry less during my travels. You know, fancy things like going get food or going grocery shopping.

reply

malwrar

13 hours ago

 |
root
 |
parent
 |
next

[–]

Rough shift, my worst was every other week and my boss prior to hiring me was 24/7 just like you. I just carry a backpack with a few batteries + my work laptop, fortunately only a few really bad stories but hooooo boy me and that backpack have seen some fun times.

reply

wkat4242

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I wish I could still buy a pager where I live :'(

reply

idontwantthis

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Do you carry a literal pager? We use the PagerDuty app.

reply

geocrasher

14 hours ago

 |
root
 |
parent
 |
next

[–]

My organization is, for now, using OpsGenie.

My pager noise:https://www.soundjay.com/transportation/sounds/train-crossin...That will not only wake the dead, it'll wakemeno matter how asleep I am.

reply

malwrar

13 hours ago

 |
root
 |
parent
 |
next

[–]

Haha I made the mistake of using the default iPhone ringtone, now when strangers get called in public my heart rate spikes. Too scared to change it.

reply

darkwater

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

The "for now" is very important because it will be sunset in 1 year and something. I can recommend you Incident.io or Rootly as alternatives.

reply

kunwon1

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It may interest you to know that pagers are still a thing, Motorola still makes them, and I know that one major use case is volunteer fire departments

I used to work on Motorola Minitor 5 pagers. Looks like they recently released their newest model, the Minitor 7I wonder if pagers are still used in hospitals? I imagine so

reply

sgerenser

14 hours ago

 |
root
 |
parent
 |
next

[–]

Doctors on call at hospitals also routinely still use pagers. There was a planet money episode on it a couple years ago:
https://www.npr.org/2023/12/08/1197955913/doctors-pagers-bee...

reply

xeonmc

12 hours ago

 |
root
 |
parent
 |
next

[–]

Do doctors in the Middle East also carry pagers?

reply

sharpshadow

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

The AUBMC hospital is definitely using them as well as the paramilitary in that country, at least until recently.

reply

ZuoCen_Liu

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Now, whenever I see a pager, I think of explosions. Haha.

reply

ErroneousBosh

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

There's a company in England called "Cascode" who make firefighter alerters. These are really basic "beeper" pagers, which you can program to have a bunch of different tones and LED patterns based on the RIC and Subcode.

I look after several thousand of these across several hundred paging sites.They're relatively inexpensive (70 quid or so in quantity) and they last about six weeks on a commonly-available AA battery. The batteries go flat enough to trigger the "low battery" beep at about 3am, for some reason. I don't know why.There's no messaging involved, although the encoders are capable of sending a text string. The message is "get up and get down to the fire station right now", which generally needs no further explanation. POCSAG is unencrypted, so there would be privacy concerns with sending actual incident information in the clear with it.While we're on the subject of old tech, until BT finally cut the last of them off, we use dialup modems to control the encoders (not dialup internet, just a hundreds-of-miles serial cable) as a backup, and dot-matrix printers to print out a hardcopy message for the crews to pick up.All very low-tech. All very fixable. All stays working if you don't mess with it.https://cascode.co.uk/products/2ar2-and-2ar3/

reply

wkat4242

10 hours ago

 |
root
 |
parent
 |
next

[–]

Encryption is easily doable even with one way pagers. With one way you will lose the perfect forward secrecy option but that's usually ok.

reply

ErroneousBosh

1 hour ago

 |
root
 |
parent
 |
next

[–]

It's doable but it would be custom firmware and it's not really necessary. Two way paging isn't really worth doing because then you need a massive device with a massive battery, or something that uses uncontrolled mobile phone networks (and generally still has a massive battery, that lasts about a day).

You wouldn't even need particularly good encryption, you'd just need something adequate to stop casual eavesdropping really - "keep them busy for half an hour" would stop people from sniffing the POCSAG traffic and tweeting it, so that people show up at incidents and hang around filming it on their phones.This incidentally is what a guy in England got arrested for a few years ago, exactly that. It's perfectly legal to listen to and decode pager messages (or any other radio messages), you're just not allowed to pass them on to people or act upon them, and posting them on twitter and then going round to rubberneck at the ongoing incident very much ticks those boxes. As with so many things in the UK, to paraphrase Aleister Crowley, "Don't Be A Dick shall be the whole of the law".

reply

malwrar

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Oh no, I just always hear it termed that way and it captures the “feeling” for me since it feels like a dedicated device. I just just carry a work phone w/ PagerDuty during my shift.

reply

altairprime

16 hours ago

 |
parent
 |
prev
 |
next

[–]

Decades ago I had to write a Perl script to auth to the site for proper downtime checking. Some things never change :) Good luck with the triage.

reply

racl101

15 hours ago

 |
parent
 |
prev
 |
next

[–]

dang!

reply

Elfener

17 hours ago

 |
prev
 |
next

[–]

I got stuck in an infinite loop.

Try opening HN -> it's down, better check HN to see everyone talking about a major website being down -> Try opening HN -> loop

reply

neom

17 hours ago

 |
parent
 |
next

[–]

Yeah me too. Wake up -> HN down -> That's weird, oh well it's usually only down for a few minutes -> I should check if HN is still down -> That's weird, oh well it's usually only down for a few minutes -> I should check if HN is still down -> loop.

That was a few hours ago. I'm glad this loop is broken.

reply

squeefers

17 hours ago

 |
root
 |
parent
 |
next

[–]

sounds very much like an evil social media dopamine feedback loop. ironic given everyone on HN is so anti social media.... its clearly only bad for kids though i should add, silly of me to exclude such a detail

reply

bee_rider

16 hours ago

 |
root
 |
parent
 |
next

[–]

HN is obviously social media and it is silly to say otherwise. It is just social media that occasionally has interesting stuff. The SNR is just slightly higher.

reply

ptsd_dalmatian

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I guese developed this addiction on Facebook and now that I don’t use it, I come for methadon shot to HN

reply

neom

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I've been on this internet hit shit since the 90s lil bro, s' all good.

reply

strbean

16 hours ago

 |
root
 |
parent
 |
next

[–]

I can stop any time I want, I just don't want!

reply

HPsquared

16 hours ago

 |
parent
 |
prev
 |
next

[–]

Sometimes I'll catch myself absentmindedly reopening the browser and checking two or three front pages, seconds after having just checked them and closed the browser.

reply

notachatbot123

16 hours ago

 |
root
 |
parent
 |
next

[–]

That's a sign of addiction and I highly recommend changing your behaviour towards those pages!

reply

cheschire

14 hours ago

 |
root
 |
parent
 |
next

[–]

I feel like I need to avoid channelling Bob Saget from Half Baked when I say that is not addiction. That's a habit.

reply

cbracketdash

13 hours ago

 |
root
 |
parent
 |
next

[–]

There is a noprocrast feature in your settings to specify how long you can stay on for a single session and the frequency at which you can view HN. Super helpful!

reply

Rendello

12 hours ago

 |
parent
 |
prev
 |
next

[–]

Funny, I don't seem to need an outage to get stuck in a HN loop...

reply

mustak_im

16 hours ago

 |
parent
 |
prev
 |
next

[–]

I woke up and was wondering if I’ve just woken up in hell!

reply

Imustaskforhelp

14 hours ago

 |
parent
 |
prev
 |
next

[–]

Yeah, I had assumed something very major must have happened for HN to go down, lmao and I even asked in some linux discord server regarding it asking if there is a major outage as hackernews is down

reply

ErroneousBosh

12 hours ago

 |
parent
 |
prev
 |
next

[–]

Not just me then?

"Shit, HN is down! Hm, I wonder if there's anything about it on HN?"until stack overflow occurs.

reply

RJIb8RBYxzAMX9u

15 hours ago

 |
parent
 |
prev
 |
next

[–]

HN is how I discover whether other sites are down or not, so it serves a critical function, so of course I check it frequently.

/s

reply

manbitesdog

18 hours ago

 |
prev
 |
next

[–]

TIL I have a "open Hacker News" hand reflex

reply

ectospheno

17 hours ago

 |
parent
 |
next

[–]

I learn more reading the comments here than anywhere else. Thanks everyone for my addiction.

reply

directmusic

16 hours ago

 |
parent
 |
prev
 |
next

[–]

I'm glad I'm not the only one. If I type 'n' into any browser it autocompletes to HN.

reply

embedding-shape

16 hours ago

 |
root
 |
parent
 |
next

[–]

Save typing hundreds of letters per day, and replace about:newtab with news.ycombinator.com, now you can just do CTRL+T :)

reply

tom1337

15 hours ago

 |
root
 |
parent
 |
next

[–]

at that moment my productivity would drop to zero

reply

Imustaskforhelp

14 hours ago

 |
root
 |
parent
 |
next

[–]

mine already has and I dont even have hackernews as my new tab :)

On all fairness though, mine is same for the original comment where just pressing n autocompletes it tohttps://news.ycombinator.com/

reply

geocrasher

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I had the same thing for Slashdot.org for many, many years. Both the reflex and the browser autocomplete. I still miss the old /. It was like HN + Hackaday + Usenet.

reply

neom

10 hours ago

 |
root
 |
parent
 |
next

[–]

digg too, till they ruined it...still can't believe they ruined digg.

reply

1shooner

17 hours ago

 |
parent
 |
prev
 |
next

[–]

If you're looking to put the brakes on that, I've used LeechBlock to add a 5-second timer to opening a new HN window (along with other block schedules). The timer even fails if it loses focus, so it really helps slow you down.

https://www.proginosko.com/leechblock/

reply

embedding-shape

16 hours ago

 |
root
 |
parent
 |
next

[–]

echo '127.0.0.1 news.ycombinator.com' | sudo tee -a /etc/hostsDoes the trick as well :) For bonus points (and so you can't workaround it with your phone), do it on your router/switch instead.You'll still open new tabs and go to HN, but you'll be reminded quickly, and every day can be downtime day \o/ (for you, personally)

reply

squeefers

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

so youve got the willpower to do something about it but not enough to just stop doing it?

reply

MikeTheGreat

16 hours ago

 |
root
 |
parent
 |
next

[–]

To be fair, making a change (particularly changing a habit) takes time. Having something there to remind and nudge you helps make this easier, especially when you're tired, stressed, 'just looking for a short break', etc, etc.

It's like they say: "Your demons will comfort you when no one else will. That's why it's so hard to get rid of them"

reply

1shooner

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Yes.

reply

dwedge

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Have you never suffered from habitual reflexes? I blocked twitter for a while in my hosts file and a dozen times over those first few days I instinctively opened a new tab and typed twitter in

reply

sunrunner

16 hours ago

 |
root
 |
parent
 |
next

[–]

I deleted the YouTube mobile app a few months ago and I still reflexively reach for the app icon every now and then. Thanks YouTube Shorts.

reply

squeefers

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> I blocked twitter for a while in my hosts file and a dozen times over those first few days I instinctively opened a new tab and typed twitter in?

youd go through that effort when you could have just stopped though.

reply

frikk

16 hours ago

 |
root
 |
parent
 |
next

[–]

We all admire your absolute mastery of your own habitual reflexes and mind. For the rest of us, there is a daily battle of wits, desires, weakness, and habit.

If I could snap my fingers and break toxic habits and patterns, I would have done so decades ago :)

reply

jstummbillig

17 hours ago

 |
parent
 |
prev
 |
next

[–]

I say. Vibe coded 4 apps once I got past that, on my way to half a billion in ARR already.

reply

wincy

17 hours ago

 |
parent
 |
prev
 |
next

[–]

I’ve turned on no procrast mode and set it to ten minutes per hour. Helped me a lot!

reply

HanClinto

17 hours ago

 |
root
 |
parent
 |
next

[–]

What are you using to control this?

reply

bee_rider

16 hours ago

 |
root
 |
parent
 |
next

[–]

It is on your profile, the “noprocrast” dropdown.

reply

randallsquared

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It's a setting available on the page you get from clicking on your own username.

reply

HanClinto

16 hours ago

 |
root
 |
parent
 |
next

[–]

Whoa. A website that cares about its users enough to _easily support limiting access to itself_?

That's so refreshing in terms of being a user-focused feature, and yet it stands in sharp contrast against today's engagement-hyperfocused climate. I never would have thought to look on a website's own settings page to limit my access to that same website.I love it, thank you for pointing me to this!

reply

thesurlydev

18 hours ago

 |
parent
 |
prev
 |
next

[–]

Same! Right there with "every day must begin with coffee"

reply

locknitpicker

3 hours ago

 |
parent
 |
prev
 |
next

[–]

> TIL I have a "open Hacker News" hand reflex

You mean it's not your homepage?

reply

AndrewKemendo

18 hours ago

 |
parent
 |
prev
 |
next

[–]

It just reinforces for me that addiction is a human problem not a problem with technology

I know dang basically works
tirelessly to not change the format in order to not induce those addictive patternsbut yet here we all are

reply

chistev

18 hours ago

 |
root
 |
parent
 |
next

[–]

It's a website with the smartest people in the world. The level of conversations here are unrivaled in internet communities.

It's understandable to be addicted. Lol.I visit this place multiple times a day.

reply

phantasmish

17 hours ago

 |
root
 |
parent
 |
next

[–]

99% of social science or political topics and 50% of technical topics here do not… read as smart, and you’d be much better off spending the same time reading the first chapter of a relevant 101-level college textbook.

reply

seizethecheese

17 hours ago

 |
root
 |
parent
 |
next

[–]

It's entirely possible that this is the smartest place on the internet, but also often dumb. In fact, it seems likely. More of an indictment of the rest of the places on the internet.

reply

squeefers

17 hours ago

 |
root
 |
parent
 |
next

[–]

> It's entirely possible that this is the smartest place on the internet,

i cant find the link, but there was a post about how to "be nice" and it was a revelation to a worrying amount of "geniuses" on here. bare in mind the sum total of the advice was "be nice, dont be rude"

reply

seizethecheese

13 hours ago

 |
root
 |
parent
 |
next

[–]

1. niceness and genius are orthogonal

2. your characterization of the article sounds uncharitable3. my point isn't exactly that thisis necessarily the smartest place

reply

squeefers

23 minutes ago

 |
root
 |
parent
 |
next

[–]

1. but social skills and genius are
2. im still staggered at how elementary it was
3. ok?

reply

ssdspoimdsjvv

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Intelligence has many dimensions.

reply

the_af

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

>
It's entirely possible that this is the smartest place on the internet, but also often dumb. In fact, it seems likely. More of an indictment of the rest of the places on the internet.

Almost every (non-troll) online community that is relatively peaceful and has some semblance of moderation to remove flamewars thinks of itself as "the best community". Usually as compared to reddit, though if it's on reddit they will compare themselves to some other (hated) sub.It's a fact of the internet. Every online community thinks of itself as the smartest, more thoughtful, more civilized. HN is no exception.It goes without saying HNis notthe smartest or more thoughtful online community. It's just... ok. Not the worst, not the best. Certainly NOT the place with the smartest people, though some smart people frequent it. As a regular, you can soon figure out HN's unspoken rules, blindspots, and areas where the group opinion is more likely to be accurate.

reply

jrowen

14 hours ago

 |
root
 |
parent
 |
next

[–]

> It goes without saying HN is not the smartest or more thoughtful online community.

How does that go without saying? Name some others then, compare and contrast. As-is your argument is just posturing.

reply

the_af

13 hours ago

 |
root
 |
parent
 |
next

[–]

>
Name some others then, compare and contrast.

No need, because whether an online community is more thoughtful or smarter than another is very subjective. Almost by definition, HN is not it. Extraordinary claims require extraordinary evidence, and all that. Of course, by internet law, HN (or a subset of its members) considers itself to be the smartest, more thoughtful online community.There are communities I like better, which are smarter and more thoughtful, but I've no desire to argue with you.>As-is your argument is just posturingNah. Hard pass. Nice try though!

reply

jrowen

3 hours ago

 |
root
 |
parent
 |
next

[–]

I see you're downvoted, it wasn't me. I wasn't making any claim, you're making claims and disparaging remarks that you won't substantiate.

reply

steve_adams_86

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> the smartest people in the world

But also, people like me. Be careful what you choose to believe on this website

reply

fwip

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It's really not 'the smartest people.' It's people interested in tech, and often in making-a-lot-of-money-in-tech. It does have a lot of people with significant industry experience, which is cool.

reply

worksonmine

17 hours ago

 |
root
 |
parent
 |
next

[–]

> It's really not 'the smartest people.'

This was especially obvious during Covid, I even stopped visiting because the comment section was so crazy.

reply

the_af

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

>
It's a website with the smartest people in the world.

Nice joke!At least, I hope it was a joke...

reply

linhns

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Also the level of flak is unrivaled.

reply

krapp

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Any professional forum or technical subreddit with good moderation and gatekeeping blows Hacker News out of the water any day of the week.

reply

andrepd

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Poe's Law for a parody of the self-important sv techbro

reply

the_af

15 hours ago

 |
root
 |
parent
 |
next

[–]

It's a testament to Poe's Law that I genuinely cannot tell if the OP was being funny or not.

reply

mrguyorama

13 hours ago

 |
root
 |
parent
 |
next

[–]

There's a reason why HN of all places has such a terrible record of handling actual sarcasm and telling it apart from genuine belief and that reason is NOT that "HN is really smart" lol

reply

the_af

13 hours ago

 |
root
 |
parent
 |
next

[–]

Agreed! I think HN is average, and its userbase think themselves smarter than they really are.

... but I still cannot tell if the original commenter was sarcastic or not! ;)

reply

dzink

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

This one is at least healthy-ish for the mind. I’d much rather hacker news than any other news. Social Media is an emotional rage-bait cesspool these days. If it’s not for Hacker News those of us who abstain from the rest would be living in the dark.

reply

PurpleRamen

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

But, would the addiction become worse if HN changed, or would there be a point where they could cure it?

reply

ZuoCen_Liu

11 hours ago

 |
root
 |
parent
 |
next

[–]

Perhaps this is the role of HN - at least it still allows us to reflect.

reply

yigithan

6 hours ago

 |
parent
 |
prev
 |
next

[–]

I stopped using google.com for Internet access check, I now use HN.

reply

cbracketdash

13 hours ago

 |
parent
 |
prev
 |
next

[–]

There is a noprocrast feature in your settings to specify how long you can stay on for a single session and the frequency at which you can view HN. Super helpful!

reply

lysace

16 hours ago

 |
parent
 |
prev
 |
next

[–]

⌘-T, N, <RET>

Did it like 5 times during that 1h-ish outage. :(

reply

ChrisMarshallNY

17 hours ago

 |
parent
 |
prev
 |
next

[–]

So do I, but it was such a shock that I just passed out, and when I woke up, it was back up.

reply

ZuoCen_Liu

11 hours ago

 |
root
 |
parent
 |
next

[–]

Admirable~

reply

ErroneousBosh

12 hours ago

 |
parent
 |
prev
 |
next

[–]

Do you log into things and reflexively type "ls", too?

reply

kevin061

18 hours ago

 |
parent
 |
prev
 |
next

[–]

I did not know how addicted I was to HN until today lol

reply

nottorp

15 hours ago

 |
parent
 |
prev
 |
next

[–]

What? You mean you ... close the HN tab?

reply

selectnull

17 hours ago

 |
parent
 |
prev
 |
next

[–]

I already knew that. :)

reply

numpad0

17 hours ago

 |
parent
 |
prev
 |
next

[–]

obligatory:
https://xkcd.com/477/

reply

sosodev

18 hours ago

 |
prev
 |
next

[–]

Yes, and I'm a little ashamed to admit my morning routine wasn't the same without it.

reply

fedreg

18 hours ago

 |
parent
 |
next

[–]

This was more impactful to my day than the last AWS and CloudFlare outages...

reply

messe

18 hours ago

 |
root
 |
parent
 |
next

[–]

At least during those outages I could procrastinate on HN.

reply

the_arun

17 hours ago

 |
root
 |
parent
 |
next

[–]

I felt like changing HN down page to show top 30 posts from this week before or after the generic message.

reply

al_borland

18 hours ago

 |
prev
 |
next

[–]

Is this still a valid account for HN status? It says it’s the official one, but with the changes at Twitter to no longer show chronological feeds (at least for users that aren’t logged in), it’s rather useless. The top 5 listed post (for me) are seemingly random from 2014 - 2022.

https://x.com/HNStatusIs there a better place to check, beyond a basic down detector that may provide more insight or signal that the outage is acknowledged?

reply

dang

13 hours ago

 |
parent
 |
next

[–]

We post there when we know we're down and it may take more than a few minutes. But in this case we didn't know!
https://news.ycombinator.com/item?id=46303196

reply

alexfoo

14 hours ago

 |
parent
 |
prev
 |
next

[–]

https://xcancel.com/HNStatus
 only uses chronological ordering (after any pinned tweets) and that has the last message 12 Dec 2023.

(Basically whenever you see an x.com link just change it to xcancel.com and avoid the nonsense.)

reply

FuriouslyAdrift

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Only way I have figured out how to to change the "Following" sort order back to chronological is from the mobile app: click the down arrow on the "Following" tab. Change the sort from "popular" to "most recent."

Seems to reset it on the web view, too.

reply

al_borland

16 hours ago

 |
root
 |
parent
 |
next

[–]

It sounds like this would only work for logged in users.

reply

zipy124

18 hours ago

 |
parent
 |
prev
 |
next

[–]

https://hn.hund.io/
 Is a status page, no idea if official or not, but it didn't register here for some reason.

I didn't read the post text, it's identified there haha, my bad! I wish the text post text wasn't grey, I gloss over it too easily.

reply

laCour

17 hours ago

 |
root
 |
parent
 |
next

[–]

This was monitoring the unauthenticated news page, which is why it didn't catch it. It now monitors authentication as well. It is not official, and was made by a co-founder years ago.

reply

eddyg

16 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks! I checked that page and wondered why it stayed green. I resorted to checking
https://downforeveryoneorjustme.com/hacker-news

reply

lagniappe

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

This site said HN was fine and green the entire time it was down.

reply

liampulles

17 hours ago

 |
prev
 |
next

[–]

Smart. Have to use that error budget before year end...

reply

dylan604

17 hours ago

 |
parent
 |
next

[–]

I always hated the late use-it-or-loose-it at the end of the year where you end up buying the things that were denied requests from earlier in the year. You just cost me half a year of using the damn thing.

reply

ortusdux

18 hours ago

 |
prev
 |
next

[–]

Looks like 3 hrs

https://hackernews.onlineornot.com/incidents/yaz-eOJeARBLhttps://downforeveryoneorjustme.com/hacker-newsStrangely, nothing from the statuspal, which is the first google resulthttps://hacker-news.statuspal.io/

reply

rozenmd

18 hours ago

 |
parent
 |
next

[–]

Interestingly it stayed up if you weren't logged in.

reply

Izkata

17 hours ago

 |
root
 |
parent
 |
next

[–]

Not completely, I'm not logged in on my work laptop and it was only working some of the time (and not like some pages were cached and some weren't, I was refreshing the same page and sometimes it worked and sometimes not).

reply

cess11

17 hours ago

 |
root
 |
parent
 |
next

[–]

That's how I concluded that it wasn't a ban on my account but rather more serious.

reply

jedberg

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

If you aren't logged in you get a cached version from the CDN/cache. Reddit works the same way.

reply

bryanrasmussen

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

also went down if you went to login, and people's individual pages were also down. So as far as I saw the front page was up as long as you were not logged in, however I'm not sure if that wasn't just luck of the draw, I had one experience where it looked like maybe the front page was sometimes down for not logged in users as well.

on edit: ok others pointed out it was cached pages I saw. explains it.

reply

smallerize

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

That only worked for a while, eventually I couldn't load comment pages even logged out.

reply

davnicwil

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

that'll be because it's served from cache when you're not logged in

reply

ramonga

1 hour ago

 |
prev
 |
next

[–]

when I realised the api still worked I put this together
https://hackernewsx.com
 just to realise it will just work if I cleared my site data.

reply

wavemode

18 hours ago

 |
prev
 |
next

[–]

When it was down my thought was "damnit, I'll actually have a productive workday now."

reply

tzs

18 hours ago

 |
parent
 |
next

[–]

Next time you can avoid that fate by opening HN in a private browsing (or whatever your browser calls its equivalent) window. This outage, like the vast majority of HN outages, only affected logged in requests.

I suppose you could also just clear your HN cookies in regular browsing window, but then when they fix it you'd have to log in again.

reply

dpoloncsak

16 hours ago

 |
root
 |
parent
 |
next

[–]

Huh. Dunno why, but when it failed on Firefox I tried Chrome, and it worked. I wrote it off as a Mozilla issue, but this would better explain that I think

reply

neom

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Is it my imagination or did they used to automatically serve you a logged out page when it was down?

reply

ycombinator_acc

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I couldn't access it in private or regular.

reply

dwa3592

18 hours ago

 |
parent
 |
prev
 |
next

[–]

hahaha

reply

steve_adams_86

16 hours ago

 |
prev
 |
next

[–]

I was fortunate enough to get to watch a bunch of kids racing and bouncing in bouncy castles in our school gym during HN's downtime.

It's not that much different from HN, come to think of it.(ha, ha)

reply

esafak

18 hours ago

 |
prev
 |
next

[–]

A lot of the outage indicators failed. Someone needs to create an outage indicator reliability dashboard.

reply

Nextgrid

18 hours ago

 |
parent
 |
next

[–]

A lot of them got fooled by the caching; pages for signed-out users are cached heavily and those kept returning successful responses even if the actual backend server was down.

reply

dizhn

17 hours ago

 |
root
 |
parent
 |
next

[–]

This site also got it right:
https://downforeveryoneorjustme.com/hacker-news

I believe it's because they accept user reports.

reply

esafak

17 hours ago

 |
root
 |
parent
 |
next

[–]

Yes! Now we see what a difference it makes.

reply

chistev

18 hours ago

 |
parent
 |
prev
 |
next

[–]

And an outage reliability indicator for that outage reliability indicator.

reply

willis936

17 hours ago

 |
root
 |
parent
 |
next

[–]

We apologize again for the fault in the fault indicator. Those responsible for sacking the people who have just been sacked have been sacked.

reply

arionmiles

17 hours ago

 |
parent
 |
prev
 |
next

[–]

So a downdetectorsdowndetector.com but for Hacker News?

reply

sltr

18 hours ago

 |
prev
 |
next

[–]

Yeah I couldn't log in for a bit this morning. It's concerning how often and how many times I tried. Glad it's resolved.

reply

imiric

18 hours ago

 |
parent
 |
next

[–]

Next time try not to beat a dead horse expecting it to resurrect. :)

reply

mlhpdx

17 hours ago

 |
root
 |
parent
 |
next

[–]

So now we call the refresh button CPR?

reply

rob

18 hours ago

 |
prev
 |
next

[–]

Maybe PG is more involved now and hired the "10,000 lines of AI code a day" person who made a deployment mistake?

https://x.com/paulg/status/1953289830982664236?s=46

reply

dhruv3006

18 hours ago

 |
prev
 |
next

[–]

I was quiet surprised really. HN almost never goes down.

reply

Aachen

17 hours ago

 |
parent
 |
next

[–]

You don't visit enough my friend :)

It's down about 8.4 minutes per week. On 26% of days it doesn't work at least once, and on 12% of days it has more than one consecutive failed check. The longest uptime streak was 24 daysI've been keeping track since exactly 2 years (to the day!) because I was surprised that it seemed briefly down for me on a daily basis. Was I getting unlucky and hitting it every time, or was it just down very often? Nobody posted anything so I started answering the question for myself :pI've been meaning to post the tracker to HN but there's a pesky bug I want to fix: the "is it currently down" stat. I don't know how this is beyond me but something in the code bugs out. So this is my first time posting about it

reply

ayewo

15 hours ago

 |
root
 |
parent
 |
next

[–]

Would love to see it when you do get round to posting it :)

reply

dustfinger

15 hours ago

 |
prev
 |
next

[–]

It would be a nice feature if hackernews had a simple news.ycombinator.com/status page that I could trust. I don't like loading those some-sketchy-domain/status-right-now sites.

reply

mmooss

14 hours ago

 |
parent
 |
next

[–]

> news.ycombinator.com/status page

That's not so useful when news.ycombinator.com is having problems.

reply

dustfinger

14 hours ago

 |
root
 |
parent
 |
next

[–]

True. how about
https://ycombinator-status.com
 or
https://status.ycombinator.com
. They can drop that link on their official ycombinator.com site just so it is easy to tell that it is legit when they are not down. They can maintain the status for all of their official sites there. Well, with the exception of ycombinator-status.com of course. I guess they can post that status on some-sketchy-domain/status-right-now - LOL!

Maybe ycombinator does have an official status page somewhere, but it is not easy to find if that is the case.

reply

danielfalbo

17 hours ago

 |
prev
 |
next

[–]

As soon as I noticed it was down I came to hacker news to post about it, but...

reply

Aperocky

10 hours ago

 |
prev
 |
next

[–]

During that time I couldn't load HN web page, but my HN CLI tool could connect to HN:
https://github.com/Aperocky/hnterminal
, but only read.

reply

xxs

17 hours ago

 |
prev
 |
next

[–]

PSA - if you delete your cookies, HN gets it easier. Or just test it in a private window.

It did work without being logged on. The auth service appeared to be down as the log in attempt (just showing the page) failed.

reply

scottydelta

16 hours ago

 |
parent
 |
next

[–]

Now it makes sense. I was puzzled about why it was working on the phone browser and not on my system. I'm logged into HN on my system.

reply

codyklimdev

14 hours ago

 |
prev
 |
next

[–]

I thought HN traffic got blocked on my work's network for a second, phew! My lunch breaks would've gotten a lot more dull.

reply

ashf023

18 hours ago

 |
prev
 |
next

[–]

Yes, and on one request I saw a message like "Restarting server - this won't take long", and soon after it's back up.

reply

zzixp

18 hours ago

 |
prev
 |
next

[–]

First AWS/Azure/Cloudflare and now HN?!?

reply

philipwhiuk

18 hours ago

 |
parent
 |
next

[–]

Time to update the meme:
https://preview.redd.it/cloudflare-had-a-rough-day-today-and...

reply

imiric

18 hours ago

 |
parent
 |
prev
 |
next

[–]

We can live without the former, but not HN!

reply

gjsman-1000

18 hours ago

 |
root
 |
parent
 |
next

[–]

You won't be employed without the former.

reply

ajdude

17 hours ago

 |
prev
 |
next

[–]

I was able to view the site without being signed in (i.e. private window) but any browser I was logged into wouldn't load.

I'm sure it's a coincidence but it started working again shortly after emailing hn@ycombinator.com

reply

whynotmaybe

16 hours ago

 |
prev
 |
next

[–]

I Still found it funny that we have downdetector, downdetectordowndetector, downdetectordowndetectordowndetector,... (I lost count) but downdetector doesn't detect HN's status.

reply

chistev

18 hours ago

 |
prev
 |
next

[–]

It was the first time since I started using this website (August last year) that it was down.

I'm still impressed nonetheless.I'd like to know what caused the outage and how it could have been prevented, for learning purposes.

reply

stevenjgarner

18 hours ago

 |
prev
 |
next

[–]

https://www.stevenjgarner.com/HN-Down-2025-12-17-07-48-UTC-0...

reply

fatty_patty89

18 hours ago

 |
prev
 |
next

[–]

I got irrationally angry when it refused to load the website

reply

imvetri

18 hours ago

 |
parent
 |
next

[–]

you could refuse to be angry to mock it

reply

DonHopkins

18 hours ago

 |
parent
 |
prev
 |
next

[–]

You handle your irrational anger much better than whatevermrfukz who keeps pooping his pants.

reply

fatty_patty89

18 hours ago

 |
root
 |
parent
 |
next

[–]

Interesting that you mention that, how do you keep track of his comments? Some sort of plugin/scraper?

reply

Jtsummers

17 hours ago

 |
root
 |
parent
 |
next

[–]

> how do you keep track of his comments?

You can just look at them, turn on showdead in your profile and you'll see a bunch of flag-killed comments in this discussion by whatevermrfukz. No need for a plugin or scraper.

reply

fatty_patty89

17 hours ago

 |
root
 |
parent
 |
next

[–]

thank you

reply

zelphirkalt

18 hours ago

 |
prev
 |
next

[–]

Yep "having trouble serving my request" or so.

reply

PurpleRamen

17 hours ago

 |
prev
 |
next

[–]

In other words, productivity in tech skyrocketed for hours..though it seems some work was flavoured with irrational anger.

reply

khobragade

16 hours ago

 |
prev
 |
next

[–]

Man if I had a coin every time I email the mods and this thing goes down, I'd strangely have two coins.

reply

Kim_Bruning

17 hours ago

 |
prev
 |
next

[–]

In with the rest, yes, and my first thought is always "I have an internet outage" when HN is down. :-P

reply

numpad0

18 hours ago

 |
prev
 |
next

[–]

Could have been accidental flagging of sorts. Didn't work on PC for few minutes while showing fine on phone.

reply

sangeeth96

17 hours ago

 |
prev
 |
next

[–]

Thought it had something to do with some model updates, like Gemini Flash 3 for a moment.

reply

arm32

17 hours ago

 |
prev
 |
next

[–]

The "site status" apps are all smoke and mirrors, how unreliable.

reply

oidar

17 hours ago

 |
prev
 |
next

[–]

What was the longest that HN has been down? I feel like this is up there.

reply

pedro380085

18 hours ago

 |
prev
 |
next

[–]

Yes, I got an error message, but I cleared my cookies and was able to access.

reply

dvaun

17 hours ago

 |
prev
 |
next

[–]

Will we get a post mortem?

reply

voxleone

18 hours ago

 |
prev
 |
next

[–]

Yes, it' been out for me too, southern hemisphere, GMT -03

reply

neurolesudiste

17 hours ago

 |
prev
 |
next

[–]

Hi,
Got an error an hour ago on phone, not loged.

Anyway, glad to see you back.Paris 1812.Cheers from France.

reply

rustaceanU32

17 hours ago

 |
prev
 |
next

[–]

I'll admit this ruined my morning

reply

arbirk

17 hours ago

 |
prev
 |
next

[–]

We need a serious post mortem for this

reply

neurolesudiste

17 hours ago

 |
prev
 |
next

[–]

Yup, France here , Paris 1809.

HN was down about an hour ago.Glad to see it back !Cheers.

reply

silverpiranha

18 hours ago

 |
prev
 |
next

[–]

Yes, was down for me too this morning

reply

markus_zhang

18 hours ago

 |
prev
 |
next

[–]

Yes was down for me. Ontario, Canada.

reply

gepiti

17 hours ago

 |
prev
 |
next

[–]

Athens, Greece yes it was down.

reply

wek

18 hours ago

 |
prev
 |
next

[–]

Yes, it was down for a few hours

reply

gaigalas

17 hours ago

 |
prev
 |
next

[–]

I got confused by the "minutes ago" thing.

Working with full dates in the HTML and doing a tiny JavaScript that calculates the "minutes ago" would actually be a neat improvement.

reply

thatgerhard

17 hours ago

 |
prev
 |
next

[–]

Thought for a second I got banned for something lol

reply

elxr

17 hours ago

 |
parent
 |
next

[–]

I thought I was being rate-limited for opening posts too fast, which has happened before.

After more than an hour I thought, "wow this is pretty harsh" and "so much of my exposure to learning things is directly tied to HN posts". I was lost lol.

reply

verzali

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Me too and I was wondering what I did!

reply

Aachen

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Your comment history doesn't sound IP-ban-worthy. Is there an alt that has you worried? :P

reply

agumonkey

17 hours ago

 |
prev
 |
next

[–]

hn applied ycombinator too strictly

reply

bossyTeacher

16 hours ago

 |
prev
 |
next

[–]

I have never before seen this website down.

reply

SilverElfin

17 hours ago

 |
prev
 |
next

[–]

I tried to refresh an embarrassing amount of times

reply

russellbeattie

17 hours ago

 |
prev
 |
next

[–]

HN being down makes you start wondering about the differences between routine, addiction, compulsion, and habit.

reply

khaledh

17 hours ago

 |
prev
 |
next

[–]

It was down if you tried to access it while authenticated (i.e. you have a cookie). It was loading fine for unauthenticated sessions (e.g. incognito).

reply

rzerowan

18 hours ago

 |
prev
 |
next

[–]

Yes

reply

busymom0

18 hours ago

 |
prev
 |
next

[–]

I run the app called HACK and received user emails that the HN website was down.

reply

maverwa

18 hours ago

 |
parent
 |
next

[–]

Thank you for HACK. I love it!

reply

spooneybarger

18 hours ago

 |
prev
 |
next

[–]

Yes

reply

ProofHouse

18 hours ago

 |
prev
 |
next

[–]

I wake up, and look at HackerNews lol. This morning sucked hahaha

reply

bennydog224

18 hours ago

 |
prev
 |
next

[–]

Yes, I had to touch grass this morning.

reply

complianceowl

14 hours ago

 |
prev
 |
next

[–]

I was convinced that I got banned lol.

reply

FergusArgyll

18 hours ago

 |
prev
 |
next

[–]

Yeah & chatgpt was trying to gaslight me - claiming it was my fault. Happy to put that bum in its place...

reply

chistev

17 hours ago

 |
parent
 |
next

[–]

You use ChatGPT to know if a site is down?

reply

laCour

17 hours ago

 |
prev
 |
next

[–]

I'm with Hund. Our hn.hund.io page did not catch this because it was requesting the cached, unauthenticated page. It now monitors authentication as well.

reply

joncrane

17 hours ago

 |
parent
 |
next

[–]

Thank you. I was thinking myself or my corporate IP was shadowbanned

reply

sammy2255

14 hours ago

 |
parent
 |
prev
 |
next

[–]

You should add a graph of visitors per-minute for the status page for the past 24 hours or so. Would really help for situations like this

reply

jonahx

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Is this a mistake by hund, or the configuration of hund by HN?

reply

laCour

17 hours ago

 |
root
 |
parent
 |
next

[–]

Mistake on our part (Hund) for not monitoring authentication. This page is unofficial and was made by a co-founder several years ago.

reply

Cheer2171

16 hours ago

 |
parent
 |
prev
 |
next

[4 more]

[flagged]
dang

13 hours ago

 |
root
 |
parent
 |
next

[–]

Yikes, you can't do this here.

We've banned this account for repeatedly breaking the site guidelines and ignoring our requests to stop.If you don't want to be banned, you're welcome to email hn@ycombinator.com and give us reason to believe that you'll follow the rules in the future. They're here:https://news.ycombinator.com/newsguidelines.html.

reply

sentrysapper

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

What a rude thing to post. Hund, don't listen to this entitled nonsense. There is a reason it's called human error. Companies 100x your size and 10000x your revenue like AWS, Microsoft, CloudFlare, CrowdStrike can't figure out how to accurately provide status dashboards. At least you took the time to explain your mistakes. If anything you got another supporter for your honesty.

reply

seanw444

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

This just in: people make mistakes on occasion.

reply

gjsman-1000

18 hours ago

 |
prev
 |
next

[9 more]

[flagged]
Aachen

17 hours ago

 |
parent
 |
next

[–]

Keep in mind that votes aren't supposed to be about whether you agree or disagree, but whether a comment adds substance to the thread. A good question that makes a wrong assumption can be worth upvoting; a correct but fairly irrelevant statement about politics not (to give a relatively obvious example)

Being "voted to -2" doesn't necessarily mean you were wrong (it often correlates though). People might just think it wasn't relevant in whatever context you posted it inI often find it hard to tell what makes people think something I write is not helpful (or sometimes also a comment someone else made) and thus appreciate comments that clarify constructively. It can also help to ask for clarification if you're particularly surprised about the votes on a given post

reply

Eikon

15 hours ago

 |
root
 |
parent
 |
next

[–]

> Keep in mind that votes aren't supposed to be about whether you agree or disagree

That’s not what happens in practice.

reply

abujazar

18 hours ago

 |
parent
 |
prev
 |
next

[–]

Unless the downtime was caused by something Cloudflare would've prevented, this downtime would've happened regardless of being behind Cloudflare. Cloudflare adds another single point of failure.

reply

null_deref

18 hours ago

 |
parent
 |
prev
 |
next

[–]

Could this be a self-inflicted bug? In that case, the broader point still stands: cloud providers can cause outages that are outside your direct realm of responsibility.

reply

gjsman-1000

18 hours ago

 |
root
 |
parent
 |
next

[–]

Your VPS server and your data center and the ISP your data center uses and the AS system your ISP uses all can cause outages outside your direct realm of responsibility.

reply

Jtsummers

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Complaining about downvotes usually gets you more downvotes, so the response here isn't really that surprising.

reply

Jeremy1026

16 hours ago

 |
parent
 |
prev
 |
next

[–]

You're probably being downvoted today for your "I was smarter than you" tone.

reply

DonHopkins

18 hours ago

 |
parent
 |
prev
 |
next

[–]

It's absolutely irresistible downvoting people who preemptively complain about being downvoted like you do. It really made my day. Post another complaint so I can do it again please! It's not knee jerk when you explicitly ask for it, by leading with a complaint about downvoting, instead of just making your point and letting it fall or rise on its own merits. You're the one who put the idea of downvoting you into my head in the first place.

reply

whatevermrfukz

18 hours ago

 |
prev

[4 more]

[flagged]
DonHopkins

18 hours ago

 |
parent

[–]

I remember my first beer.

reply

null_deref

18 hours ago

 |
root
 |
parent

[–]

That Markov chain spiraled out of control

reply

rolandog

17 hours ago

 |
root
 |
parent

[–]

Perhaps Grok was not trained to go so much time with 0 responses due to the downtime?

reply

Guidelines
 |
FAQ
 |
Lists
 |
API
 |
Security
 |
Legal
 |
Apply to YC
 |
Contact

Search:
