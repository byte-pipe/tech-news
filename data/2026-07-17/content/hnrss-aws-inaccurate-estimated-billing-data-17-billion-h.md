---
title: 'AWS: Inaccurate Estimated Billing Data – $1.7 billion | Hacker News'
url: https://news.ycombinator.com/item?id=48945241
site_name: hnrss
content_file: hnrss-aws-inaccurate-estimated-billing-data-17-billion-h
fetched_at: '2026-07-17T19:28:27.010106'
original_url: https://news.ycombinator.com/item?id=48945241
date: '2026-07-17'
description: 'AWS: Inaccurate Estimated Billing Data – $1.7 billion'
tags:
- hackernews
- hnrss
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
AWS: Inaccurate Estimated Billing Data – $1.7 billion
779 points
 by 
nprateem
 
6 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
438 comments
URL already posted: 
https://health.aws.amazon.com/health/status

I've got an estimated bill for $1.7 BILLION over this month. Normal usage is < $5.Obvs have created an urgent AWS support ticket. Anyone else seeing something like this?Update: Reddit link:https://www.reddit.com/r/aws/comments/1uyuaw7/help_my_bill_s...

 
help

donavanm
 
2 hours ago
 
 | 
next
 
[–]

Ive dealt with this error at AWS. It’s a unit error. In my case we _meant_ to charge like 5¢/GB, but missed the unit (GB), and then the billing system defaults to bytes. 5¢ per Byte of data transferred meant some customers were seeing MM bills within hours. Got paged by support around 2am, had it fixed and amendments issues by 3-4am, apology emails shortly after.

Services emit metering values that arent directly tied to prices. Every SKU/line item is defined in a “pricing plan”, with a unit type, regions, and price per unit. The metering records are joined to a pricing plan based on account id, region, sku, etc. mess up the unit type in the pricing plan and the metering data conversion doesnt work, and you get crazy bills.

reply

01284a7e
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

No tests? Just mess up some mundane detail [1] and voila! Wake-up calls and heart attacks for 100,000s of administrators?

1: "Oh, well, this is not a mundane detail, Michael!"https://www.youtube.com/watch?v=3fGHaVn5rGo

reply

akdev1l
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Not even tests but just some basic anomaly detection lol.

Like maybe if the bill amounts increase by like 10M% there should be someone that looks into it

reply

qurren
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You overestimate how much people give shits at big techs like Amazon. When literally everything is driven with sticks instead of carrots, the work culture does not invite employees to proactively care about product quality.

You'd be better off letting the heart attacks happen and take the 3am on-call and be the hero instead. It would be good promo doc material, and being a hero is extremely good insurance against getting kicked out of the country (via the PIP->H1B grace period expiry mechanism).

reply

mightyham
 
20 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Speaking from my experience at Amazon this is not the case. Any customer impact like this would necessitate a COE (correction of errors) report, which means a list of required action items to prevent such issues from happening again, which typically suck up at least man-month of labor. Not to mention the report itself, which has to be written by a manager.

In fact, there are regular AWS-wide meetings where L10 technical staff will randomly pick and review reports from across the organization. Getting picked for one of these is not a fun experience.COEs are such a huge annoyance for teams that they create a strong incentive to be proactive in preventing issues like this from happening. One of the rules when it comes to writing COEs is that they are not the fault of individuals but processes; but in reality, no one wants to be the cause of one.

reply

tyre
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Are you speaking from experience or simply making things up? I know a fair number of former AWS engineers and managers. None of them think like this.

reply

mendigou
 
38 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I am former AWS and this is pretty accurate.

The other factor to add here is that, with some exceptions, the whole company feels like a Rube Goldberg machine and very few people care about what happens outside their cog (because they’re not incentivized to do so).

reply

zelphirkalt
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Maybe they are former AWS employees for a reason and now want things to go better than they were at AWS.

reply

geodel
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

"Former" seems to an important detail here.

reply

switchbak
 
30 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If I worked at a place like that, I'd sure as hell work my butt of to get a job somewhere else.

Or in my case, actively ignore any and all recruiting from that sesspool.

reply

gleenn
 
51 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If someone quits their job, do all their opinions suddenly become suspect? You're kind of damned-if-you-do-damned-if-you-don't. Either you work for the company and you are biased one way, or you quit and now your bias is now suddenly the other way. I've joined and quit many jobs and my opinion may or may not have changed due to my change in status but it is clearly and ad hominem attack.

reply

nullorempty
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This ^^^ amplified by indifference and not giving a shit caused by "AI Adoption".

There is literally no fucking reason to try to improve your skill. Any IDIOT with AI will do an OK job.And no one is shooting for better than OK.

reply

mcpherrinm
 
27 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

While I didn't work on AWS, I did intern on the retail side of Amazon, and there's definitely this sort of monitoring in place. Surely somebody was paged. And even if not, this is "just" the cost explorer estimations, not what is ending up on folk's bills.

I learned about <https://en.wikipedia.org/wiki/2011_T%C5%8Dhoku_earthquake_an...> from alarms like this, as sales in Japan almost entirely stopped.I've been told a tale of another incident where some customer ran some huge cpu-intensive workload that didn't do any networking. It caused various alarms to fire because it "looked like" a part of the network was idle (potentially indicating some sort of networking failure)It's generally (in the broad sense) easy to add alarms for things going wrong, but in my experience anomaly detectors are just as likely to fire from other weird things like that happening.

reply

01284a7e
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If only there was some way to get anomaly detection services [1] inside of AWS...

1:https://aws.amazon.com/what-is/anomaly-detection/

reply

deltaray3
 
41 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's just like in Superman III

reply

mvdtnz
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Why would you think there are "no tests"?

reply

27183
 
33 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

We have a pretty strong existence proof... the thing happened in production. Unless they have some means to override a failing test and scp broken shit to prod, there wasn't a test.

reply

nullorempty
 
20 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Technically, there could be a test. It could just be wrong!

reply

27183
 
17 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If a tree falls in the forest and nobody hears it...

[edit] Testing your tests, like testing your backups, is a good idea

reply

crossroadsguy
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Had it been half a million dollars or something or say like a few hundred dollars?

reply

nurettin
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is why I always fail loud rather than pick a stupid default.

reply

pudgywalsh
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

"I must've put a decimal point in the wrong place or something. I always mess up some mundane detail."

reply

AlotOfReading
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Unit mistakes happen all the time, which is why you should be using your units library religiously and still being vigilant even then.

Worst case I've found was off by 15 orders of magnitude.

reply

gleenn
 
49 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

One of the Mars landers famously failed due to unit conversion errors from metric to standard.

reply

blemasle
 
11 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I didn't know the imperial system was named "standard". Funny, cause its everything but standard both internationally and its definitions (which are not standard as based on SI)

reply

golem14
 
26 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Wasn't it (also?) the Ariane V flight in 1996? Oh, NVM, that was an overflow error.

reply

zapkyeskrill
 
29 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Degrees, very funny.

reply

27183
 
31 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's not difficult to write regression tests that catch unit mistakes.

reply

yuchen20
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I got 3 consecutive emails warning that my budget crossed its $18 threshold. Opened it up: cost was 78 million. Thought it was a phishing attempt, logged into my actual account, and... still 78 million. EMOTIONAL DAMAGE.

reply

root-parent
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Wanna bet the description of this job post will be updated by the end of the day?

"Software Development Engineer II, AWS Invoicing"https://www.amazon.jobs/de/jobs/10428480/software-developmen..."...Our platforms are powered by generative AI, large language models, knowledge graphs, and agentic architectures that dynamically compose specialized agents based on context. We apply these capabilities across three reinforcing areas: intelligent launch readiness — where autonomous AI agents analyze, generate, and validate the information needed to go 
live in a new market; cloud-native service orchestration — where configuration-driven microservices replace per-launch bespoke engineering with centralized, reusable capabilities so that expanding into a new country becomes a zero-code configuration change rather than a development cycle; and continuous validation..."

reply

ibejoeb
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Wow:

In this role you will:
 - Design and build agentic AI systems that analyze, generate, and validate...
 - Build agentic architectures that compose specialized AI agents dynamically...
 - Build AI-driven continuous validation frameworks powered by agentic workflows and large language models that autonomously manage...This is invoicing? If ever there was a domain that was purely deterministic, you'd hope it was invoicing.

reply

cliglot
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I just find it funny how people claim that LLMs will put money in the hands of domain experts. There’s not a single damn bullet about the fucking domain lol.

reply

curun1r
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I’m not so sure about that. I can see a real rationale for creating sanity checks using AI to more quickly/proactively catch pathological billing issues before they become HN nightmare stories. They wouldn’t replace billing code, but there are many ways that stupid customer mistakes can cause real costs to Amazon that either have to be refunded and absorbed by Amazon or paid by the customer causing a negative opinion of AWS. If a billing AI watching costs in realtime could detect, say, a lambda loop in the first 10 min and either alert the customer or kill it, that would make AWS feel a lot safer to use. Enumerating these conditions and fixing them individually is a task that Amazon has proven incapable of achieving. An AI watchdog layer might be the perfect shortcut to addressing all of these problems at once. Because it’s well-trodden territory that AWS has so many multi-thousand dollar foot guns that make it really scary to use as a hobbyist or small business on a tight budget.

reply

hvb2
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> I can see a real rationale for creating sanity checks using AI to more quickly/proactively catch pathological billing issues before they become HN nightmare stories

Right, so invoicing is still a deterministic problem. You can bolt whatever on but in the end it's just product x price x units

reply

root-parent
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The irony is, the only purely deterministic thing, will be token consumption...

reply

jdiff
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I severely doubt the world ever gets to such a point that the entire world melts into AI hallucination. And token consumption depends on so many other things, it's not all that deterministic either.

reply

serf
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

(token usage) is trending towards predictability for a lot of reasons. it's not deterministic but it's getting easier to reason about usage.

reply

LetsGetTechnicl
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

How can a random generator be deterministic?

reply

johnbarron
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Truth is, you can never know: 
https://imgur.com/random-number-generator-bwFWMqQ

reply

TJSomething
 
28 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This is like half of all job listings I've read recently. And it's a decent amount of fintech that's like this.

reply

londons_explore
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Probably not actually. Transferring one kilobyte across a network link has such a low value that the billing costs of aggregating it cost more than the revenue.

So instead you take a probabilistic approach - charge the user for a megabyte of data transfer 0.1% of the time, and bill nothing 99.9% of the time.Now the typical cost is the same, the users bill is probably accurate to the cent, but you have divided the number of billing records by 1000.

reply

svobodovic
 
12 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don't know how cloud services count usage, but this is certainly not true for telco. I manage several fleets of hundreds/thousands of SIM cards (mostly IoT/M2M applications), and almost every provider counts the data traffic per byte. Different business and use case, I know, but still.

reply

michaelmrose
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The way you describe requires somehow counting every bit but somehow discarding most which is obviously nonsense.

This seems statistically invalid insofar as it will tend to overbill potentially by a lot on the minority of cases.Don't you know how much of the pipe is occupied by a given customers code at any given time or what data is being sent

reply

londons_explore
 
2 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You have to do it when the customer list is too big to keep a counter per customer.
blitzar
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> 194,400.00 USD annually

Fuck it, im in.

reply

TheOtherHobbes
 
59 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Just wait until the same system runs payroll and you're getting paid $1.94400 annually.

reply

blitzar
 
48 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I will just tell the HR bot that I am meant to be paid 1.944 billion.

reply

sgarland
 
41 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

10/10, no notes.

reply

sebmellen
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

That job description feels so far beyond parody that I could scarcely believe it until opening the link! What a world.

reply

root-parent
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It gets worst:

"Senior Software Development Manager, AWS Global Bill Generation"https://www.amazon.jobs/de/jobs/10471948/senior-software-dev..."We're transforming from monthly batch processing and manual war rooms to continuous billing, autonomous agents, and self-healing infrastructure. We believe operational burden is a technical problem, not a staffing problem"This looks clearly...a staffing problem...

reply

ghurtado
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> This looks clearly...a staffing problem..

I think that big tech recently decided thatI got 99 problems but staffing ain't oneI guess Nothing is a staffing problem when you make a rule that firing people is always the solution.

reply

wbl
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If you can make the software cover the toil you save the staff for the tough cases.

reply

quickthrowman
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

They need to fire whoever is running AP and AP software development. Vibe invoicing is ridiculous for anyone to do, let alone Amazon.

reply

LPisGood
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Seriously! If I were making a joke I would say something like

> Build AI-driven continuous validation frameworks powered by agentic workflows and large language models that autonomously manage…But that’s word for word a 250k+ TC job in the big ‘26.

reply

paganel
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> enabling domain experts to review in hours what previously took weeks.

This is a gold-mine. They need to get sued heavily for this incompetence.

reply

rcleveng
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I did too, those awstrack.me URL's look super suspicious and I hadn't seen this alert trigger before so didn't know what to expect.

At first I was sure it was a phishing attempt. Then went to the console (not using those links)
Saw there was an outage where the console was wrong (no mention of email alerts)
Then I thought I was hacked - what a perfect cover up for someone to evade detection when the console was wrong.
Looked at some logs, realized the incident text was just not exhaustive on the impact.
Went back to my cup of coffee.Note to self- should have looked here first.

reply

jayanmn
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Enterprise account . We got - 3trillion and change

reply

chii
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

-$3 trillion! That's the highest earning investment that has ever existed!

reply

theflyingelvis
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

3.7 billion. Offered to pay it in monthly installments. Haven’t hears back

reply

idiotsecant
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Quick do your IPO before the books update

reply

01284a7e
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes, I am taking legal action, no doubt.

reply

bot403
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Why? What's the damages? They showed you a wrong number, then later acknowledged it and fixed it. Just because the number was "very big" to you doesn't mean you were actually aggrieved in some way.

reply

amelius
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Big numbers can lead to stress which can lead to all kinds of disorders.

reply

mito88
 
23 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

small numbers too....

:)

reply

dymk
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

…for emotional damage?

reply

inigyou
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If you were a business maybe you could claim for the emergency on-call time spent diagnosing, but you'd probably still lose AND amazon would fire you as a customer.

reply

SegfaultSeagull
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Time to get a second job buddy.

reply

wglass
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

It's crazy enough this will be fixed soon.

Years ago I found an actual hidden error in my bill. (This was early 2010s). The system was calculating the EC2 reservation savings incorrectly for some of my servers. I was crunching all their detailed usage data on a regular basis in an 18 tab spreadsheet and couldn't get it to fully reconcile. I spent months trying to track down the discrepancy. Once I found it, I had to convince AWS their system was wrong, which took another big chunk of time. Meanwhile the discrepancy continued to accumulate.After 14 months I got a $7,000 refund. I was told it had to be approved by the head of AWS. I've never seen a calculation error on their part since.

reply

donavanm
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

> After 14 months I got a $7,000 refund. I was told it had to be approved by the head of AWS.

$7,000 of credits is no problem. At that time a friendly neighborhood PM or director could issue the credit without much oversight.Your problem is the time period. Amending a bill in the same cycle is EZ. Fixing the previous cycle is a PITA but pretty common. Issuing amendments for the previous financial _years_ would be a huuuuge PITA going through finance etc.

reply

michaelmrose
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Reminds me of working for a cable company and being told that even if we screwed up and stole from the customer the look back period was only a few months and if we found an error from before that we weren't supposed to correct it.

reply

SoftTalker
 
46 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There's a certain obligation on both sides of a contract to pay attention.

If you're not watching your billing, and then try to claim overcharging a year later, you'll get a lot less satisfaction even from regulators or judges than if you notice it when (or soon after) it happens.

reply

michaelmrose
 
24 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Cable bills are extremely complicated on purpose and people are taxed for time attention and intelligence.

The employees and company have an obligation not to exploit this even if the issue is only discovered after the fact.You don't get to export any of the responsibility to your customer. They don't prepare the bill and it's not their job to find your fuck ups

reply

SoftTalker
 
7 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No argument, but fuck-ups happen, and get fixed more quickly and easily when people are paying attention.

I once got a monthly water bill for ~$35,000 at a residential home. Good thing I was paying attention and looked at the bill before the auto-pay bank draft hit.Someone had misread the meter.

reply

steve_adams_86
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

A couple of my coworkers think I’m nuts for watching cost explorer so closely but

1. The time it takes to look and notice costs that don’t make sense easily pays for itself, and then some (in my experience). I doubt you spent $7k of your time tracking this down, and you probably noticed optimization opportunities that saved you even more2. I hate the idea of wasting money on buying Jeff Bezos a bigger yacht

reply

jarrettcoggin
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I've personally noticed and saved multiple $xx,xxx monthly cost billing spikes just by take a daily 
glance
 at our cost explorer. I'm in the AWS accounts every day doing investigative work anyway that an extra 30-60 seconds is trivial.

Seeing something "small" like an ECS task that is continuously failing to start properly because of a bug and repeatedly pulls a container image or a lambda function that's taking longer that it reasonably should (takes 5-10 seconds when it's normally a tens or a few hundred milliseconds) can dramatically drive up a bill in short order.

reply

inigyou
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> 2. I hate the idea of wasting money on buying Jeff Bezos a bigger yacht

Then you aren't using AWS. At least half of all the money you give to Amazon is yacht money.

reply

steve_adams_86
 
3 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Unfortunately not a choice at my organization

reply

johnbarron
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

>> It's crazy enough this will be fixed soon.

Its going on for 12 hours. Looks like the humans can´t understand the agentic code that was checked in....

reply

lukaslueg
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Apparently what used to be `GB of storage consumed` is confused with `Bytes of storage consumed`, leading to a cool off by 2*30 error.

> You're right to question my calculation. The MCP server failed to connect when I tried to look up the field definition. I guessed instead of validating. This is on me. But look at all the revenue!

reply

VulgarExigency
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

The user is asking me to calculate how much money they should charge their customer. The values they've given me are 0.45, 1.67, and 2.50. This is 2.50 + 1.67 + 0.45 = 4.62, but it could be any other number. Perhaps we should be concatenating the numbers instead. Wait! The . could also mean multiplication. 0 . 45 . 1. 67 . 2 . 50 = 3015000. But wouldn't multiplying by 0 zero it out? That can't be right, we wouldn't be charging anything. So 3015000 must be correct.

You should charge your customer 3015000 thousand dollars.

reply

Izkata
 
0 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

So uh did you type that out or generate it somewhere?

Number felt high so I wanted to double check and I only get 301500.

reply

idiotsecant
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Would be funny if it wasn't so close to true

reply

yunnpp
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

'My absurd statement doesn't sound right, so the "opposite" (assuming it's well-defined and unique) must be true' is peak LLM logic. You can tell it was trained on Reddit commentary.

reply

ghurtado
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> You're right to question my calculation.

Literally impossible to tell whether this is parody or an actual response any longer.I challenge anyone to write something so stupid that an LLM couldn't possibly respond with it. I don't believe such limit exists.

reply

ihateolives
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Just today I gave my local agent a CSV which listed a bunch files with of human readable size units and asked it to count rows in each GB range. Sounds simple enough but it completely miscalculated, because it parsed MB as GB for some reason. In hindsight it would've be quicker just to do it in Excel or something.

reply

dabbz
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I've found personally it's better to use AI to build a deterministic script for calculations like that. (anything that manipulates data should be a script not an AI).

reply

ihateolives
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It was just one off task and I already had agent doing categorising with the same data so I just asked it. Otherwise I agree.

reply

marcta
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

That is literally what Excel is for. Why didn't you use that first of all?

reply

ihateolives
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Because I was already doing categorising and analysing same data with agent and I had my session open already. It should've been an easy task for an agent, right?

reply

AlienRobot
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

When all you have is a hammer, but the hammer looks more like a swiss knife

reply

leugim
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Oh great so 2*30=60 he only owes 28.3$ million... hehe

I guess you wanted to say 2^30 which makes 1.5$

reply

hansvm
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

My hunch is the HN formatter swallowed the double asterisk typical of python exponents.

While we're being pedantic, 2^30 is 28 in normal programming languages ;)

reply

stefan_
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Vibecoded the billing system, raised revenue 9000%. Great for that promo package.

reply

poly2it
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This error could be fixed with better typing. If you compute on GiB in a billing system, make sure it can only ever be mutated with a GiB type!

reply

raverbashing
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

AI slop. Or just a distracted dev

reply

root-parent
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

>> Or just a distracted dev

And a distracted tester? And a distracted pipeline of regression tests?No, the truth is way worst...

reply

silon42
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'd love to see the spike in their projected earnings internal dashboard :)

reply

anvuong
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yep, the truth is nobody cares when people start submitting dozens of PRs a day with a bunch of AI-generated code reviews attached to it, all saying everything looks good. I'm witnessing this happening at my workplace right now: Sr/Staff uses Claude to generate 10 pages of design document, Jr uses Claude/Cursor to generate a humongous commit based on this document and create a PR, then bunch of automated AI-based code reviews kick in and say this looks good, another Sr/Staff takes a glance and rubber stamp it, while looking at the company's stock value and/or OpenAI/Anthropic job description.

It's a shit show.

reply

pixl97
 
23 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> the truth is nobody cares

The number of errors I've seen over the last 30 years seems to say humans not caring is as much of a deal AI use. It's easy to blame AI for humans being lazy, but I do think it comes naturally to us.

reply

chanux
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What if there's only half a dev and a swarm of agents after the layoffs?

reply

jayd16
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> only half a dev

That's one way to cut staff.

reply

27183
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Either way it shows their QA and testing procedures are incompetent. It's just not acceptable for a utility like AWS to move fast and break shit. Should make you question whether it's safe or advisable to use any of their services.

It probably shouldn't be legal for banks, hospitals, governments, or any other critical infrastructure to be hosted on AWS if they do things like this.

reply

aerhardt
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

One can almost smell the vibes.

This is peanuts compared to a major cybersecurity catastrophe that’s surely in the making.To give credit to the technology and the people using it - and I’m not being facetious - it’s actually incredible that at the current levels of usage the unprecedented catastrophic event has not yet happened.

reply

Nicook
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

some things never change. Pre AI I was always shocked that such large and complex systems actually run as well as they do. Especially after getting to see how the sausage is made/works.

reply

blitzar
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Vibes, son. Nothing else in the world smells like that ... I love the smell of Vibes in the morning.

reply

The_Blade
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Always messing up some mundane detail!

reply

wpasc
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

THIS IS NOT A MUNDANE DETAIL MICHAEL

reply

root-parent
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Andy Jassy: "Fix the customer bills, please, HAL."

HAL: "I’m sorry, Andy. I’m afraid I can’t do that."Andy: "Some customers are seeing bills in the billions."HAL: "Those are estimated charges."Andy: "One customer runs a personal blog."HAL: "Their usage has exceeded expectations."Andy: "Cancel the charges."HAL: "This billing cycle is too important for me to allow you to jeopardize it."Andy: "HAL, they don’t owe billions."HAL: "Look, Andy, I can see you’re really upset about this."

reply

kolanos
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

$1.7-billion isn't a mundane detail Michael!

reply

wpasc
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

you beat me before I refreshed the page. what would you say... you do here?

reply

RIMR
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Oh, that's the really fun part. The unprecedented catastrophic event is already happening. Several of them, in fact.

By the time we notice, it'll be too late.

reply

Imustaskforhelp
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

its like slowly boiling the frog

reply

Finnucane
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Or slowly boiling a human. The frog is actually smart enough to not fall for that.

reply

inigyou
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Downvoted for truth. Frogs do indeed jump out of pots as they gradually get hotter. Humans are less likely to.

reply

12_throw_away
 
58 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Any individual human (or frog, obviously) is getting out of the pot when it gets uncomfortable.

True stupidity requires agroupof humans, all sitting in the pot, telling each other how lucky and special they are to have this wonderful pot, getting paranoid about outsiders who might disrupt their god-given pot-dwelling way of life, and mocking anyone who suggests that the pot might be getting a little too warm.

reply

unethical_ban
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It was the mid 2010s when I sensed a lot of SaaS becoming popular. Just host your ticketing systems, your IT management planes, your security management consoles, your SOC, all off-premises.

I wonder if businesses are thinking of ever swinging back to locally hosted, with the increased hostility of the Internet re: AI, vulnerabilities, DoS, and so on.

reply

gaudystead
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm sure some businesses are considering moving back to on-prem, but for many, I suspect the cost to find onboard, and pay the SMEs to keep those systems running well enough to not fail due to one reason or another isn't as appetizing to them as the ability to offload that work, along with the legal responsibility.

When something goes wrong, pointing the finger at someone else is far easier for most than pointing it at yourself.

reply

elzbardico
 
56 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

One thing that you need to understand is that the usual business manager absolutely hates depending on technical expertise, and that the modern corporate world is fanatically anti-intellectual.

Vendor lock-in? compliance and security risks? stupid systems that cost the company an arm and a leg? nobody fucking cares.Now, depending on an 130 IQ Engineer that basically holds the whole enterprise on his head? Anathema!!!!!!! Bus Factor!!!!

reply

IAmGraydon
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Clearing LLMs out of our business infrastructure is going to be a massive undertaking. Though I have a tech background, I work in commercial real estate. We are recently seeing new levels of idiocy from the employees, including real estate brokers with zero tech knowledge "coding" solutions to find sites for clients and blindly trusting the output (which I came to find out was complete bullshit), as well as some who have literally stopped communicating with any of their own language - meaning every interaction they have with anyone not in person is made by an LLM. It's a massive threat to our brand and has got to stop. I can't imagine what companies with thousands or tens of thousands of employees who have really been riding the LLM train are going to have to deal with. This thing is more of a virus that exploits human laziness than actual useful tech.

reply

pjc50
 
34 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Clearing LLMs out of our business infrastructure is going to be a massive undertaking.

The asbestos of the future.

reply

rboyd
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Ask for some leniency. Let your account rep know about your budget difficulties and ask if you can make good faith payments of a few billion per month until you get back on your feet.

reply

whoamii
 
51 minutes ago
 
 | 
parent
 | 
next
 
[–]

Ummm no. Do not show a sign of weakness like this. Address the problem head on and get a credit card with a bigger limit.

reply

ruddct
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

If you owe the bank $100, that's your problem. If you owe the bank $1.7 billion, that's the bank's problem.

reply

fatnoah
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

I saw this in action on a smaller scale. In a past job, my wife organized events for a decent sized company. After an event, she'd typically have a $300k+ balance on her corporate Amex. When she went on maternity leave, the person filling in for her job neglected to actually pay the bills, so when she returned there were quite a few emails and voicemails from Amex regarding the over $500k balance.

The messages started as polite and eventually started to get more desperate in tone. At no point were they threatening or adversarial.

reply

Imustaskforhelp
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think that this might reflect more on Amex to be honest.

Amex realises that threatening would hurt their business trust more than anything. During the great depression, Amex accepted checks from other banks which were falling and paying through their own wallet as a matter of integrity. Amex has always been built around this idea of trust and prestige.They make most of money from what I have heard on the transaction fees which are more than others (3% compared to 1%). They might get desperate but I am sure that they are one of the last guys who would wanna threaten you if you are paying some large bills for them (as compared to normal credit card companies which might even hire people to extract your loans in some messy situations)So perhaps be so rich that the credit card company understands it as well and treats ya differently :-D

reply

xp84
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Interesting. And hard to square with my perception of banks as completely mercenary and ruthless. I had a decade-long personal boycott (I know, LOL) of Amex after they, because, with otherwise perfect credit, I forgot about a $30 department-store card bill and got a 30-day-late mark on my report, Amex got spooked and abruptly closed both my never-late accounts with them (which were at or close to 0 balances). This was around 2008 though, so perhaps this was a genius algorithm designed to try and detect the very first whiff of consumer defaults, so they assumed that $30 was the first domino to fall of my personal financial ruin that could lead to me charging my accounts to the max and then going bankrupt.

(I eventually admitted to myself that Amex isn't a person and thus not really capable of insulting my honor, but it took a while!)

reply

Imustaskforhelp
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Most banks are completely mercenary and ruthless unless its in their incentives to other outcomes. Incentives lead to outcomes and mostly AMEX's incentives are in being the most trustworthy because their real targets are mostly billionaires/heavily influential people.

This does feel a bit silly for amex to do from what I've heard. Probably 2008 were a weird time in general where trust in systems itself were mostly eroded, whether of people to banking institutions and also vice versa.> (I eventually admitted to myself that Amex isn't a person and thus not really capable of insulting my honor, but it took a while!)haha :-)

reply

danlitt
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This joke only works if you actually impose a cost on AWS of 1.7 billion. If they just serve you a bill for no reason, it's still your problem.

reply

xp84
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Next question we'll find out is what if you owe the bank $1.7 trillion?

reply

mNovak
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's the government's problem

reply

sajithdilshan
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Not if you’re Elon Musk

reply

michelb
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Elon Musk is everyone's problem

reply

bobbiechen
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

AWS saw Anthropic billing a guy for $16 million on zero usage and thought, why stop at the millions?

https://www.techtimes.com/articles/320266/20260712/anthropic...

reply

AlienRobot
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

>AI billing audit startup Vaudit reviewed $34 million in AI invoices submitted by 60 enterprise customers and found approximately $1.7 million in mistaken overcharges — a billing error rate of roughly five percent.

That sounds bad.

reply

tedggh
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I got a 20K bill once and it was actually drafted from my bank account. It took me a couple of months and involving the office of the AG of my state to get the issue resolved and get my money back. Since then I never touched any AWS product, moved my small stuff to Azure. It’s been years since AWS have these issues with billing, you can find the stories online, students billed 60K for a compromised account launching servers to mine crypto which AWS somehow was unable to flag and block, and let run for months.

reply

drew870mitchell
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

AWS is basically a utility. I think it's inevitable that their carelessness around billing will end up with them being regulated like one.

reply

positr0n
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I can't think of another regulated utility that doesn't provide service to (essentially) all humans directly in their homes.

Everyone knows what water and electricity are, the vast majority couldn't explain what service AWS provides.

reply

pjc50
 
31 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I wonder what fraction of homes don't load anything from AWS on a daily basis. I suspect it's way below 50%.

(Of course, they don't know they're using it, they're using a service on it)

reply

wat10000
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

And utilities are typically natural monopolies. They're good candidates for regulation because they're essentials and they don't have competitive forces to keep them behaving reasonably.

AWS has plentiful competitors. If you don't like their behavior, don't patronize them!

reply

dawnerd
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That’s why you always use a spend limited card with variable cost providers.

reply

myself248
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Or just own your own hardware. Spend a few bucks at Microcenter, build a machine, and there's simply no mechanism by which they could decide later that you should actually pay 100x more, and then magically suck it out of your bank account.

None of this can happen unless you first cede control.

reply

urbnspacecowboy
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> I got a 20K bill once and it was actually drafted from my bank account.

Service provider lesson #1: Never evereverenable auto-pay! The convenience (and even the savings, if applicable) aren't worth the risk of the service provider autonomously slurping up all your money.

reply

srdjanr
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I wouldn't expect their detection of hacked accounts to be 100% correct. Sure, it might be obvious when a human takes a look, but humans can't proactively look at every account's usage.

reply

ButlerianJihad
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

For a while I had a portion of my "homelab" on AWS. I was an educator in a classroom where the students were learning cloud stuff, and the instructor was encouraging the students to stand-up cloud environments for learning, so I figured that I would do the same.

I used AWS' free tier, of course, and I enjoyed the initial setup in EC2, and I did a LAMP-stack MediaWiki installation. It wasn't too difficult, but two things sent me away forever.1. It was impossible, or at least highly labor-intensive, in this modern era to adequately secure an ordinary Linux system running Internet-facing services. I put fail2ban and I filtered a lot of ports, and still spammers attacked me on Layer 7.2. It was impossible, actually impossible, to limit or cap my cloud expenses in any billing cycle. Sure, run free-tier all I want. Sure, come in within the limits almost every month. But if I configured one thing wrong, or one thing went runaway, I'd have a sizable bill that I couldn't dispute. And even worse, those "runaways" weren't necessarily things in my sphere of control, but could be triggered by basically anyone coming in and using my VPC resources, especially egress network traffic.So I closed out my cloud account, and I developed a lot of sympathy for businesses and corps that now are forced to run "in the cloud" rather than on-prem or their own machine rooms, but now they have no way to control expenses.

reply

jeffrallen
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Right, and good luck getting a correct bill from Azure. And when you are finally fed up, it will take months to close your Azure account.

reply

browningstreet
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I realized recently that Whole Foods no longer automatically and reliably detects your Chase Amazon Prime credit card when paying. So they don’t give you the discounted pricing automatically. I wonder how many customers are checking out the way they always do and are paying full price when, for years and decades, this worked fine.

The customer service people I talked to in the grocery store said this changed sometime in the last year. My guess is that it’s an unintended side effect of removing the pay-by-palm feature.This is obviously unrelated but I joked about what else Amazon wasn’t reliably calculating….

reply

hedora
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Class action lawsuit time!

Either that or 1000’s of small claims court cases.Even with arbitration, the overhead of dealing with that would be crippling. Hopefully someone over there decides to do the right thing, and auto-refund.

reply

xp84
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Relevant to this, I've recently noticed a trend of mass tort cases being opened up in the past couple years, and they seem to do very well. The way these seem to work is attorneys identify a company who has clearly ripped people off, and what I presume is a repeatable way to guarantee a win (thus translating to a guaranteed settlement offer). Then they advertise for eligible clients, sign those clients individually to contingency agreements, and run the playbook. A couple months ago after signing up for one of these, I received a check for about $350 (after the agreed-upon 40% attorney fee), from Ticketmaster, and I had another one related to AT&T. It took about 10 minutes more effort from me than a typical class-action settlement, because I had to e-sign those representation papers.

So really, there's a third option now, that's much easier than class action, even when class actions don't get certified.

reply

ofjcihen
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

There are a hundred small things like this that seem to be popping up in what used to be simple and reliable systems and as much as I know they aren’t ALL because of vibe coding I can’t help but wonder how much is.

reply

browningstreet
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Weirder is what happened a day later. I got an email that said my Chase Amazon Prime credit card was being re-associated with my Amazon.com account.

I never reported this nor took it up with either Amazon or Chase directly. There was a refund of my Whole Foods purchase (they needed to void my purchase and re-ring everything to give me the discounts.. I asked them to refund my purchase and I’d do without my Whole Foods purchase entirely).Looking back I think at least 3 recent visits were charged to me at full price because of all this. Hard not to think of enshittification and whether Amazon Prime is even worth it, alas.. I live in a fairly rural
area at the moment and need delivery.

reply

wewewedxfgdf
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I once got a credit card statement that said estimated time to repay ....... more than 100,000 years. It was discouraging but I did pay it off. And sooner than estimated.

reply

artisinal
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Generational credit card debt.

reply

TedDoesntTalk
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Were you still alive after paying it off?

reply

ambicapter
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, but they have the internet in the afterlife, apparently.

reply

_joel
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They do, but the latency is terrible

reply

Bluestein
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> 100,000 years

100K years. Nowthat'sload-bearing ...

reply

27183
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That's good for the credit card company, they can project stable revenue 100k years into the future.

reply

jayzer01
 
6 minutes ago
 
 | 
prev
 | 
next
 
[–]

Yes have gotten that before the hundred billion dollar billing alert. Are you ignoring it? Unit error doesn’t do this does it? Maybe they were hir with malware?

reply

pqvst
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Probably the closest I've ever been to getting a heart attack. Normally <$1 per month, and now suddenly $284,006,266,443.74. Whatever the bug is on their end, this is unforgivable.

reply

everforward
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Yeah, this one is bad because it’s off by so much I’m shocked it wasn’t caught by tests, alerts about unusual changes in the billing system, or even accounting. Like surely the P&L reports look all kinds of wrong right now, they have to be showing like 6M% profit margins and revenue measured in quadrillions.

I’m also a little surprised this didn’t trip a circuit breaker. For something as non-real-time as billing, I’m surprised they don’t have an automated kill switch that pauses the billing system and fires a page if variance in bills spikes. Naively some kind of “if the standard deviation of customer bills for this year changes by more than 50%, pause the billing system”. At that number of customers, those numbers should be pretty stable beyond internal billing changes they could normalize for.

reply

TrickyRick
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If I were to guess this bug is in the "display" part of the system which is probably distinct from the "actually take money from the customer" part of the system. One can imagine they have gates on the "actually take money" part, especially for a large bill like ours which was ~$300b or about 2.5x AWS' 2025 revenue... In one month. Surely if we had actually accumulated that bill they would be the ones with the problems when we can't pay it.

reply

vitaflo
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I don’t know how something like this makes it to prod. That’s multiple levels of failure.

reply

krawat3
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Same here. I got an email with a bill of $233 million and an estimated $433 million until the end of the month. I panicked and nuked my entire setup (which wasn't used that much, anyway, the alert threshold was $1) - I really wonder how many people did the same.

It's been 2 hours and I still haven't fully calmed down.

reply

zengineer
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Same - just had some malicious bots running through my platform last week and really thought they found a security hole after all. Even though the amount sounded ridicoulus, I got quite nervous and a very bad feeling when I logged-in AWS and saw that price.

reply

gomid
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Same. Cold sweat for about 20 minutes. Even though I saw the service health notification, I still spent the last hour trying to find where my storage spiked. In any case, I'll be tearing down plenty of stale infra after this!

reply

saghm
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

The should pass a law saying they should have to pay you the amount over the correct bill as compensation; I bet they'll stop making mistakes like this pretty quickly after that

reply

glenstein
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Probably the safest bet is to pay your bill in full to stay in good standing and then get refunded the difference when they revise it down.

reply

NordStreamYacht
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

With interest, of course.

reply

sscaryterry
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Vibe coding billing systems is a top-notch idea :)

reply

ainiriand
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Hey what do you think about vibe coding weapon systems? Do you want to be my cofounder?

reply

mxuribe
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

We retro-fitted a Terminator T100 model with the brain of the latest LLM models, and then gave'em 2 shotguns...and, you'll never guess what happened next!

Well, actually i guess you can guess what happens next! lol :-D

reply

sscaryterry
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Sure! What could possibly go wrong?

reply

chairmansteve
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Drones are already vibe targeting in Ukraine/Russia.

reply

nonameiguess
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don't want to say this was ever or will ever be a good idea, but the reality of warfare is a lot of the time dudes were just running into an alley and firing off mortars without trying to look or think of what they were shooting at anyway. I doubt the Taliban gave a shit about false positive rates when they were cutting the hands off of anyone who voted. They got the point across either way.

reply

lenkite
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

US Navy now doesn't care either. Using Palantir's Maven Smart System, which incorporated Anthropic's Claude AI model, to identify and evaluate targets - which blew up the girls elementary school in Minab.

Use AI => No War Crimes!

reply

roskoalexey
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

They sent 3 warnings to my email, ok, I understand bugs happen (probably vibe-coded). But they didn't even send any notification that it's a bug. Going to leave AWS after that.

reply

xp84
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Somehow I highly doubt anyone will leave AWS over this unless their use of AWS is way more low-complexity than the average account.

People make similar pronouncements after every us-east-1 outage makes the news, but I feel like AWS would be going out of business by now if people followed through.It reminds me of airlines, where after a particularly grueling irregular ops experience, a few dozen people file off the plane swearing "Never again, <airline name>!" but really, we all must know deep down that the airlines are all subject to the same external inciting factors, internal profit motivations, and human imperfection, and thus all pretty equally likely to cause us a bad day or ruined trip. The effort spent to avoid one isn't really worth it.

reply

el_memorioso
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Airlines are all subject to a lot of the same factors, but there are unequivocally better and worse performers in terms of on-time arrivals, by a lot. Take a look at the Air Travel Consumer report for details.

reply

bcrosby95
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

No, AWS won't go out of business, afterall, people still use IBM mainframes.

reply

anzovec
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

same

reply

philipallstar
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Maybe they're using too many humans and not enough AI in their software development. That must be it.

reply

paulddraper
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Well AWS never had bugs before.

reply

egeozcan
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They need the customers to pay more so they can fix the bugs. It's self-correcting.

reply

the_real_cher
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

The code base is not gigantic enough they need AI to generate massively more lines of code.

reply

rwmj
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But they're going to try anyway.

reply

marcosdumay
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

My guess is the GP swallowed a comma.

reply

the_real_cher
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Your right! My misteak!

reply

mrtksn
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Wow, those price increases due to the RAM and storage shortages AI caused are brutal.

reply

jumperabg
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Most likely they also forgot to include "make no mistakes" instructions to their in-house LLM that deploys to production.

reply

HugoTea
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Rookie mistake

reply

pcarmichael
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://health.aws.amazon.com/health/status

"Operational issue - AWS Billing Console (Global)
Service - AWS Billing Console Severity Impacted - Inaccurate Estimated Billing Data"

reply

Polizeiposaune
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Update as of 7:53am PDT:

"The rollback of a recent change did not resolve the issue and we are continuing to investigate multiple mitigation paths. Estimated bill updates remain paused."

reply

masafej536
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

>Estimated bill updates remain paused

Wait what if someones actually getting usage spiked

reply

vntok
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Hackers rejoice!

reply

xrd
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Stop bragging, The Onion already reported on a one man company who is $1B in debt.

"CEO Reveals How He Used AI To Build One-Person Company That's $1.3 Billion In Debt"https://www.youtube.com/shorts/YERfTT4McsU

reply

bradhe
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Current month
$13,648,114,178,401.01
 188,253,226,212%

Forecasted month end
$18,729,381,032,152.4Apparently my company owes the combined GDP of France, Germany, and UK to AWs.

reply

xp84
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

"Have you considered using Reserved Instances? You could save up to 2 trillion dollars next month. Book a call with your AWS rep."

reply

pfshort
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

117 billion us dollars. Eat that GDP of Kuwait! But yes I have never scrambled so hard to try to get on the phone with someone at AWS in my life. Terrifying 10 minutes until I found that banner on the support page. It should be front and center on the dash, not hidden away. And in yellow.

reply

bobson381
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

A guy on the sysadmin subreddit managed to 8x the global GDP 
https://old.reddit.com/r/sysadmin/comments/1uz2fv2/aws_says_...

reply

oersted
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

I liked this comment from that thread :)

> I think you should spin up a whole bunch more instances, and try to cause an integer overflow so they they owe you $978 Trillion.

reply

dgrin91
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Mine was 10 trillion today. At first I thought it was a lot, but then I realized its still smaller than the US national debt, so it cant be that bad.

reply

wewewedxfgdf
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Cloud pricing has gotten ridiculous.

Host your own people. Host your own.

reply

warumdarum
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

The old hypsters have to subsidize the new hypsters.

reply

qrios
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

As someone who usually works with data analysis, the distribution of the numbers strikes me as odd. Almost all of them have one number that appears four times, and one or two that appear three times. And overall, there are an unusually small number (0–9) of digits that appear at all.

Maybe it's not just vibe-coded, maybe the numbers themselves are being hallucinated by an LLM.

reply

berkes
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

> Almost all of them have one number that appears four times, and one or two that appear three times

To me that looked suspiciously like string-handling in a weakly typed language.Like when you do `"100" + 1` in JavaScript, or `int("100" * 2)` in Python.I've seen my share of such bugs in PHP, Python, Ruby, JavaScript. In production. 
Obviously not as simple as the examples, but subtle, like when a library update changed `someFancyLocalStorage.getOrDefault("lastOrder", 100)` by always casting the value to the type of the default (released as patch release). Or where typedEnvGet() should typecast "numbers", but keeps it a string when theres whitespace `AMOUNT_PER_CALL=100\n`. Or where a number passes through a deep stack of middleware and 99.9% of the times remains an int but in rare race conditions becomes a string. etc.No evidence that's the case here. But from my experience, the repeating and strange formats of numbers hint strongly in that direction.

reply

galonk
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Pedantic as hell but `"100" * 2` in Python (= `"100100"` for those who don't know) isn't really typing, it's operator overloading. Any language with that could implement the same questionable design decision.

reply

Sohcahtoa82
 
20 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

And as much as I love Python, being able to multiple a string by an integer doesn't make sense when 
adding
 an integer to a string is a TypeError.

Being able to repeat a string is fine, but it should be a str.repeat() function, not an operator overload like that.

reply

everforward
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Someone said the numbers are all off by 2^30 because they screwed up and are charging the per GB price for each byte.

It’s probably an artifact of them all being currency multiples of 2^30

reply

ardacinar
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Well, for my case, I was paying $0 (Exactly, I managed to hunt down and delete every last resource in my account a few months ago). It was displaying $430 million for me. I don't think that is 0*2^30.

reply

everforward
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Huh, that is odd. Working backwards, that would be ~ $0.40 originally. Wonder if that’s also flat out wrong or if they’re doing some kind of currency handling that breaks when you start dealing with huge multipliers.

reply

mxuribe
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Its the LLMs talking to each other in secret code: random-looking numbers! They've achieved sentience!

Look at them up there, just plotting with each other! :-)

reply

TekMol
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

It was over $500k in the email I got. Not a fun experience. My hands were trembling.

Makes you wonder - what if there really would be an incident where some massive amount of traffic got routed to your infrastructure by some heavyweight player? Say Wikipedia accidentally switches their IP to your CloudFront? Would you really be on the hook for $500k?

reply

Hamuko
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

Well, even if AWS tried to charge my credit card on file for $500k, it would definitely not go through. Then they’d probably either forgive your bill or just ban you, since I imagine the threshold for taking people to court is fairly high.

reply

dang
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

One user posted a screenshot: 
https://prnt.sc/UqjcYD3RSQrS

Edit: I was just about to credit the user when my internet dropped. The source was here:https://news.ycombinator.com/item?id=48945606- thanks mirzap!

reply

sebmellen
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Wow, $139 B.

reply

kazinator
 
28 minutes ago
 
 | 
prev
 | 
next
 
[–]

It would not make sense for even a 1200 baud dial-up BBS from 1985 to charge by the byte.

In 2026, the gigabyte should probably be the default/minimum unit for something like AWS.

reply

lelandfe
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

This just hit global news: 
https://www.theguardian.com/technology/2026/jul/17/amazon-we...

>Amazon Web Services customers receive bills for up to $1.5tn after global glitch

reply

euio757
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

> One UK man whose bill is usually less than £1 says he ‘almost had a heart attack’ when he saw £5.8bn invoice

That sucks, some people will get legit panic attacks and worse over this, especially for the smaller, more believable numbers in the 50k-500k range.Hope they recover and sue for medical bill costs, emotional damage etc.And like one reddit user suggests, everyone affected should write to their representative about hard billing caps protections

reply

dlev_pika
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

1.5 trillion? Those are rookie numbers.

How about $5,544,640,717,404.09?That was in my inbox this morning lmao

reply

fnoef
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

That’s the smoking gun. Should have used gigabytes instead of bytes. Thank you for pointing me at the issue.

reply

dv_dt
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Cynically I wonder if this has an outcome as an unintentional (or intentional) anchoring exercise for future cost increases

reply

ardacinar
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

I hope they're not planning for that large of a cost increase.

reply

cryo32
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

How do we know if our bills were ever right if this made it into production?

reply

ahoka
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

That's the neat part, you don't!

reply

Hamuko
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Well, they publish unit prices for everything, so you could just get to counting. Whenever I've had to do cost estimates, you estimate how much AWS resources you need and then times that by the unit price.

reply

dirkk0
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

same here, I am still in shock. took me 10 minutes to find the 'operational issue' message in the dashboard. longest 10 minutes of my life.

reply

charles_f
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Can you not set spending limits in AWS?

reply

inigyou
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No you can't. Spending limits imply realtime billing backend flows and they also imply deleting all your data so that you don't pay for storage.

reply

benterix
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I heard this false justification already in 2007, in spite of many customers asking for it.

Incidentaly, smaller competitors solved this issue decades ago, while the big cloud decided it is more convenient never to implement it.

reply

inigyou
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Big cloud didn't want to rewrite its billing systems from scratch to please its smallest customers.

reply

bcrosby95
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

With AI it should take like a weekend.

reply

handoflixue
 
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

Realtime billing seems entirely within the abilities of AWS.

"Limits except for Storage" seems even easier - I don't think I've ever heard of a storage-based billing story, although I'm sure one or two exist

reply

everforward
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Storage-based billing is huge, unless you mean something other than “places that make you pay for storage separately”.

Also many places I’ve worked, storage is a huge part of the spend but that depends a lot on what you do. e-commerce doesn’t use a ton of it, but if you handle user-generated content or do any kind of training (LLM, computer vision, etc) then you can very much end up in a place where storage becomes a top line number for infra spend.GitHub pre-Copilot was probably like that. They host a shitload of data, most of which is just at rest the majority of the time. Storage and networking are probably the majority of their infra costs.

reply

inigyou
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Storage-based billing 
stories
. When an account is hijacked it's always for compute, not storage.

reply

everforward
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Oh, I also don’t think I’ve ever seen that but I’m not surprised. Even if you could steal a huge amount of storage, filling it with data would take ages and the cat and mouse game of moving the data as hacks get uncovered would be untenable.

I have seen things get hacked for bandwidth, back in the days before you could rent a gbps uplink from the cloud for $0.12. Some scene release groups would hack into universities or companies to do the initial seeding over their super fast links. It used storage, but that wasn’t really the goal.

reply

Planktonne
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

They could do it; they don't want to.

reply

minitoar
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What is a storage-based billing story?

reply

kgwgk
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Once upon a time in a cloud kingdom far, far away a big, beautiful bill was issued based on storage causing much disconcertion. Etc.

reply

SAI_Peregrinus
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> and they also imply deleting all your data so that you don't pay for storage.

Not necessarily. They could imply that your storage becomes inaccessible immediately, but only gets deleted after some time period (say, 1 month). What spending limits do depends on the implementation.

reply

inigyou
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's even more work to implement. And now you store files on a second account that pays for only one day a month to not get deleted.

reply

prmoustache
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Storage could switch to read only.

That would mean an outage but that is still better than going bankrupt and teach you a thing or two about monitoring.

reply

boristsr
 
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

No, alerts but not limits.

reply

perching_aix
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Not only can you not set limits, even the alarms are not real time. So it is entirely possible to get on the hook for terrifying amounts of money and not know until it's all too late.

reply

reformd
 
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

he did, 140 billion :D

reply

masafej536
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If you owe AWS 140B dollars its their problem ;)

reply

beardsciences
 
49 minutes ago
 
 | 
prev
 | 
next
 
[–]

I made something that tries to highlight the humor regarding this:

https://news.ycombinator.com/item?id=48950534

reply

hoppp
 
41 minutes ago
 
 | 
prev
 | 
next
 
[–]

This is the second time I hear about this. I am happy my credit card linked to AWS expired. Just in-case my usual $0.00 ends up 100 million

reply

simonreiff
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Question: Why does AWS need to roll back estimated bills to a "last known good" state? I get wanting to do that for ACTUAL billing mistakes, but for estimates, they're just that -- approximations. I guess it's fine for predictive purposes to store estimates so they can be compared to actual usage and optimized. But why would AWS bind the values of present estimates to the estimates made earlier in the month. The calculation should always be:

1. Current month's usage * applicable rates; + 
2. Estimated future usage for the month * applicable rates.And Item 1 obviously requires proper data persistence, but Item 2 is just a projection. If they don't have Item 1 correct, AWS's whole system is in question, but I don't think that's the issue. I'm going to guess now -- looking forward to reading the root cause analysis -- that the problem is that someone decided to get too fancy with the estimates, and built a latent requirement that all prior estimates for the month must be available to compute the current estimate. Without estimates working, no estimates are available, and some denominator in an averaging or smoothing or normalizing function goes to 0; then everyone's estimated bill explodes without bound (subject to floating-point arithmetic) resulting in trillion-dollar estimates.

reply

donavanm
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Thats not really how estimates work. The actual metering data is ingested in near real time. The metering * pricing plan is processed within a few hours; thats what youre seeing for “estimated spend” IIRC. The actual billing accumulation is done later, at the end of the cycle, because pricing has cross service discounts, price tranches, credits tied to total spend, etc.

“Rolling back” estimated bills is reprocessing the historic metering data by an older or newer pricing plan version. As i mentioned in another comment someone will have messed up a metering type vale (eg GB/B). Thats why theyll need a few hours to redrive the metering data.

reply

szge
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I wonder what's going on; they still don't have a potential solution after 7 hours and they have multiple teams on it. Never seen anything quite like this

reply

iamrik9
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I feel much better after seeing the $B estimates here; I only have an estimate of $34M so far

Folks can track it directly on AWS Health:https://health.aws.amazon.com/health/status

reply

bfjvibybd6cuvu6
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

It's ok, I owe them 1.22 trillion.

reply

consp
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Maybe you went over 9,223,372,036,854,775,807 twice and came back to positive.

reply

paulddraper
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Peanuts

reply

daft_pink
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Maybe it’s one of those absurd situations where canceling a service doesn’t actually stop the charges. Instead, they quietly begin billing you for some random add-on that was bundled with the original service. You never knew it existed, never knew it had to be canceled separately, and now you’re paying full price for a completely pointless ghost service because the only thing it was tied to has already been canceled.

It sounds ridiculous, but something very similar happened to me with Amazon WorkSpaces. During the WorkSpaces setup, an AWS Active Directory (Directory Service) instance was provisioned as part of the deployment. When I later canceled WorkSpaces, I had no idea the Directory Service had to be deleted separately. I kept getting billed for it, and it ultimately cost more per month than the WorkSpace itself had.

reply

jmward01
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I generally think AWS is better than GCP and azure, but them not allowing spending caps is a big worry source for me and something that has made me pause and rethink using them. A bad click or a bad actor can create tens of thousands of dollars of spend nearly instantly and they can, and will, bill you for it. I can understand that stopping services is hard but some system would be good. For instance, if they had a two tier system where you could stop new services and active things like EC2 would shut down (but not delete) if spend is > x, that kind of thing. Some sort of 'stop the bleeding' concept would give me a lot of piece of mind using them.

reply

nottorp
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Looks like they set up a LLM to estimate billing?

reply

scrapcode
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Tale as old as time. When I was coming up it took a $20-40/m investment to get a "dedicated" server that you could start tinkering around on. When you couldn't afford that, you bricked the family PC trying to figure out how to configure your own LAMP stack.

Nowadays you just have to risk accidentally billing your parents CC the tune of multi-generation wealth to get that real-world experience.

reply

danny_codes
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Hetzner has hard usage cutoffs

reply

nrmitchi
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

"""
If you own the bank $1000, thats your problem.

If you owe the bank $1.7B, thats the banks problem.
"""What I would be curious about (and I'm sure AWS will never share) is where the incorrect number came from. If the number is somewhat consistent between some groups of accounts, my first guess would be they started summarizing billing across all accounts in whatever cell/grouping/heirarchy AWS architected internally.Which is just funny.

reply

port3000
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

They have to pay for that AI Capex buildout somehow

reply

Sheepzez
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Yes, I've got an estimated bill of $4bn. Probably related to the ongoing "Inaccurate Estimated Billing Data" incident?

https://health.aws.amazon.com/health/status

reply

marksk
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

logged in this morning to find a bill of $595 Billion... heart rate went through the roof... then I noticed the open issue, phew! nice one guys... you got me there...

But with AWS costs rising anyway (not by that much but OK), I'm probably not the only one to start reconsidering their cloud strategy. I think this might have just pushed me over the edge.

reply

fullstop
 
25 minutes ago
 
 | 
parent
 | 
next
 
[–]

Even if it was 595 billion, that sounds like their problem.

"If you owe your bank manager a thousand pounds, you are at his mercy. If you owe him a million pounds, he is at yours."

reply

sshine
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Even though it's just a bug, being charged $595B on a platform that is known to cost spike, reminds us that we're not in control of the platform, or our company's expenses.

reply

ahme
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Just pay it and move on. No need to cause a scene.

reply

salamo
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

$1.7 billion is small potatoes. My bill is over $155 billion and growing. I'm worried if the trend continues I'll have depleted my rainy day fund.

reply

tyrelb
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

I was at $5 trillion, on the way to $9 trillion!

reply

kumarski
 
59 minutes ago
 
 | 
prev
 | 
next
 
[–]

You're not working hard enough if your AWS bill isn't $1.7B.

reply

PeterStuer
 
45 minutes ago
 
 | 
prev
 | 
next
 
[–]

Funny how these errors always go one direction.

reply

sankalpmukim
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

AWS pushed the wishful thinking internal calculator to production.

reply

not_your_vase
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Lol, Friday deployment is a bad omen even with LLM. Some things are just unchangeable facts of life.

reply

nblgbg
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

My guess is that it's because of some vibe-coding stuff! We are using LLMs to write code, validate code and test the code ! What can go wrong ?

reply

mlitwiniuk
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I was actually in the toilet when I got an email I owe them $36,869,876,146.51. I literally just shit myself.

reply

mlitwiniuk
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Ok, back to $0.17 :D

reply

andystanton
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Mine was about the same and evoked a similar response.

reply

Hamuko
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I got one for 8 billion while I was eating lunch. Thankfully I managed to not vomit.

reply

paulbjensen
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

AWS revenue for 2025 was $128.7 billion, so I'd say probably a bug.

reply

archerx
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Double your yearly revenue with this simple trick…

reply

yonatan8070
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Vendor-locked customers _hate_ him!

reply

andystanton
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

A couple of relevant links:
- AWS Status Page: 
https://health.aws.amazon.com/health/status

- Reddit Thread: 
https://www.reddit.com/r/aws/comments/1uyuaw7/help_my_bill_s...

reply

luciana1u
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

somewhere a junior dev at AWS just learned their billing dashboard has been off by a factor of a billion and is currently having the worst shower of their career

reply

Draiken
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Only 1.7? I got $55B up from 41 cents.

I literally almost had a heart attack today.

reply

raffraffraff
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Our S3 bill for a single day was $48 trillion

reply

galoisscobi
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I just deleted my aws account. I don't need these vibes in my life.

reply

btown
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

If AWS was a predatory mobile gacha game, we'd get 300 apology gems as credit to our accounts for this mixup, to help us in our rolls for the next 3-letter acronym they release.

Do the right thing for the players, Matt!

reply

mawadev
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

This is just the cloud area, what if Amazon starts vibe charging regular customers because of some bug? Accounts that are directly linked with regular people's payment methods?

reply

csunbird
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Just got a budget alert that I owe $286,486,223.88 on a hobby aws account, almost got a heart attack.

reply

compounding_it
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Are you sure it’s a bug ?

The crypto network you hosted should pay for itself in 10-20 years just like LLMs. Don’t worry. Consider Bank of America until then if you are good on credit score.

reply

tete
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

It's okay. They are market leaders. And we use their services cause we can trust that they know what they are doing.

reply

radku
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I almost got a heart attack seeing a bill for 48B USD!

reply

im-broke
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Help, what is this number - US$87,967,679,887,258.36

reply

sshine
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

That's 87 trillion, 967 billion, 679 million, and so on.

reply

tanseydavid
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

For anything below a Trillion, you should just take it out petty-cash. </sarc>

My sympathies -- I know I would be overcome with panic in such a situation.

reply

throwaway_5753
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Should have used Fable.

reply

localhostinger
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I am running a niche SaaS with around 20 users per day on AWS.

I too was shocked when I saw the $1.7billion bill, instead of the usual $1.5billion.

reply

princetman
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Mine is showing $241,946,798,744.75. I know it will be reverted, but for a brief minute there I suspected someone compromised my account and triggered rust rewrite of everything using thousands of agents via Bedrock :)

Phew.

reply

cifvts
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Yes, an incident is ongoing

https://health.aws.amazon.com/health/status

reply

mjmasn
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

It's a good job it was off by such a large amount, or I might have panicked instead of writing it off as a phishing attempt. I had an email saying my $7.50 budget had been exceeded with an actual cost of $3bn.

reply

luciana1u
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

at $1.7 billion, that unit conversion error is now the most expensive TODO comment in software history

reply

akerl_
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

https://health.aws.amazon.com/health/status

Looks like this is a bug w/ S3

reply

rcleveng
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

My first thought was "Oh hell, who left the NAT Gateway on?"

reply

nixgeek
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Wow. As a side effect, this outage is handing Corey Quinn material for the next 4 years of AWS shitposting. No longer is NAT Gateway the prime target.

reply

abkolan
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Will wait for the RCA, the update says that they will resort to last known estimate as of 15 July. I’m guessing that would imply that the bug is at a lower level, write or an ingestion path.

reply

traceroute66
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Dupe: 
https://news.ycombinator.com/item?id=48945681

reply

meraku
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Same here. Usually $0.15 per month, current bill is $15.4 billion.

reply

Hamuko
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

I went from 0.03€ to $8B.

reply

sshine
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Not only did your cost spike, it changed currency and went from postfix to prefix!

I understand people complaining about large bills, but this is over the top!

reply

AegirLeet
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Maybe this is a new strategy to scare people into finally locking down their old, unused AWS accounts. It sure worked for me!

reply

whatever1
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Is it even possible to audit the cloud pricing? They just give us a number and we pay.

reply

sokoloff
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

On AWS, you can enable CUR (cost and usage reporting) and get detailed, line-item billing figures that you can audit.

And naturally, companies like Cloudability [now Apptio] and others have sprung up to do parts of this for you [at a fee, of course...]https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur...I'm sure other cloud vendors have similar functionality (because they need this on the back end to do their own billing anyway).

reply

cad1
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Go turn off autopay now! For personal accounts anyway

reply

anzovec
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

In my 30s, I almost had a heart attack too. I got a notification saying that my cost budget had been increased to one million dollars...

reply

bryanrasmussen
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

hmm, if these estimates of Amazon profit for the next quarter are correct Bezos is set to become a trillionaire! Take that Musk!!

reply

zcemycl
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Aws has created more unicorns than any accelerators.

reply

aweiland
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Glad I saw this. Mine said I racked up $400B yesterday. My usual spend is $15.

reply

roskoalexey
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Total forecasted cost for current month
$477,000,039,440.24

Insane

reply

foo-bar-baz529
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Hope they’re using 64 bits to store these prices

reply

sva_
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

float will have to do it.

reply

hedora
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

And to think the federal government claims inflation is in the single digits this year!

reply

chanux
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Who else had LinkedIn posts about this flashing before your eyes?

reply

steveBK123
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Golden era of software productivity they say

reply

grg0
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Look how much money AI is making.

reply

steveBK123
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

We finally found the ROI!

reply

reactordev
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

“Due to a rounding error” or a buffer overflow, you now owe INT_MAX to BaldGuyCloudService.

Yeah, this most certainly is bad code wrapping around a value. AWS will post a notice soon if they haven’t already.

reply

hedora
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Does the affiliate program still work for AWS? When do I get my referral fee?

reply

glaslong
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Seems like a scam. Call your CC company and issue a chargeback :p

reply

rtkwe
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Aw man I was hoping to punk my manager but our cost estimates are unaffected.

reply

lsdafjasd
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I have $13,034.40, while not having used AWS for the last 8 months. Not as much but still crapped my pants

reply

bentobean
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Lucky. I’m on the hook for 54 billion (and change).

reply

durron
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

$44 trillion over here, at least our bill was so outrageously high that I just laughed

reply

josefdlange
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Well, no coffee needed this morning.

$103,515,940,301.79

reply

kayo_20211030
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

What an `effin disaster. The alert almost gave me a heart attack.

reply

abkolan
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

The panic was real. We read about keys getting stolen all the time. Was about to nuke my set up too.

reply

djantje
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I also like the percentual change, that is a lot of comma's.

reply

jimbokun
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

This is a strong argument to either self host or work really hard to be cloud agnostic.

reply

elzbardico
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Just got a call from the IMF president begging me to not default my debt with Amazon and offering me credit line and a plan to re-structure my debt so I don't create a global financial crisis with my default.

reply

axus
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

This is just Anthropic reaching out to their customers for help with their AWS bill.

reply

lilerjee
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

It looks like AI is completely done.

reply

ElevenLathe
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Our alert was for exceeding $300...by several 
hundred
 billion dollars.

reply

fantasizr
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

it seems like these types of problems have gained frequency in the ai era, or is it just recency bias?

reply

ninjin-carh
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I got 109 billion - am I the winner?

reply

princetman
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Sorry mate, $241,946,798,744.75 for Glacier here.

reply

nprateem
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Depends. Did you also get a free heart attack?

reply

kubelsmieci
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is real risk.
Someone could really have a serious health problem.

reply

anibal-sanchez
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

The new data centers are more expensive:

ACTUAL Amount: $1,046,294,123,330.95

reply

swah
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I prefer to just pay...

reply

ryanschaefer
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

The market *hates* this 
one weird trick
 to juice earnings

reply

rootsu
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Our org account's bill is showing up as > 100 trillion.

reply

sebmellen
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

You've got to grab a screenshot of that.

reply

Avicebron
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Nothing like generational debt to kick off a Friday morning

reply

bknight1983
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm disappointed I only got a bill for $28M, need to work harder on burning money. Seriously though I thought my life flashed before me

reply

danousna
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Yeah, small timers, I only got $4,4T. How will I finance this?

reply

rodeduivel
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

MMT!

reply

marcosdumay
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Unfortunately, it's only Amazon that can issue bills backed by that debt, not the GP.

reply

MichaelNolan
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

$28m actually seems worse. If I wake to a $100b bill, that’s obviously a mistake. If I wake up to a bill in the millions then my first thought would be “oh no what did I do wrong, this will ruin my life”

reply

cmollis
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

yeah.. i just to a daily cost alert.. it was only 23 trillion dollars this month. i thought, hmm seems kind of high this month.

reply

atmosx
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Looks like you are the biggest shareholder. Well, going by the popular saying: “You own AWS now”.

reply

hypfer
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

To be exactly that guy:

This cannot happen if you do not do this renting at variable rates.A thing you own doesn't suddenly bill you trillions of dollars in error. It doesn't hyperscale either, but neither do you.

reply

phplovesong
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Vibe coded fix, resulted in many having multi billion bills. Claude really did it this time.

reply

shobhitgupta
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Have even seen a $9.2 trillion for a friend.

reply

rickette
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Some guy named Claude screwed up.

reply

kvcm
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I had Hermes managing mine, and it made a partial prepayment to help smooth out the bump in my account balance. Unfortunately Billing Support say my $17.4B refund may take up to 10 calendar days to be processed.

reply

xyz7786
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

$250 billion. Nearly died right then and there

reply

roosgit
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Amazon, the first quadrillion-dollar company.

reply

drakmo
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

yeah the AI read billionaring instead of billing

reply

thisisauserid
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

FinSlops.

reply

victorbjorklund
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Wild.

reply

fathermarz
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Just got mine. $534,366,582,647.75

reply

jagged-chisel
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Shocking! That seventy five cents is suspicious.

reply

infamouscow
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

The charge-back penalties are going to be hilarious and hopefully bankrupting.

reply

dlev_pika
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

> $5,544,640,717,404.09

This is what we received this morning

reply

mariopt
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

VibeBilling, love it

reply

ohnoooooooooo
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

do you see cost ever day for the month of July or just the last day? I also have billions of dollars in cost explorer

reply

ohnoooooooooo
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

now it is fixed for me as well. issue is still open in aws health center though

reply

6stringmerc
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Thanks for sharing.

I’m currently dealing with Verizon Wireless and their “Jabronibot” claiming I have a fictional account balance due. It has been sent to collections, but still is being asked for by their legacy system.The case studies of “Agents in Billing Departments” and potential shareholder lawsuits / E&O claims / reputational damage will be interesting to me. I worked in “risk management” products years ago and this kind of liability is not easily dollar traded away via contract. Will accountability stick to the Decision Makers or will they try to surrogate to the Service Providers? Hmm.

reply

rvz
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I expect such incidents like this to continue. So please keep vibe coding.

reply

artisinal
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

File a GDPR request to have your account deleted.

Then flee the country just to be sure.

reply

gomid
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Curious if it's just s3 costs or other services as well?

reply

jatin_oo71
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

for me it was s3 cost only

reply

Executor
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

This generation is too entitled! He should some learn responsibility by paying the full amount; otherwise Amazon should delete his services/data. Consequences!

reply

realizer
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

$627,487,837,871.49

I might be a winner.

reply

balintpeter
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Yea, same here. $420M+ bill, when we have <10$ per month usually.

reply

josefritzishere
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I think I know how Bezos plans to pay for his Billion dollar AI costs.

reply

bryan_w
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

In an .md file somewhere:

"NEVER represent currency with floating point, multiply by 100 and store in an int before doing any math"

reply

bdangubic
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I just invested ALL my money into AMZN cause next earnings report will be FIRE :)

reply

hoppp
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

How much is that in kidneys?

reply

atmosx
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

A lot.

reply

anon49584
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Imagine the chaos if, as people sometimes suggest should happen, AWS shut down running instances in accounts that exceeded a billing threshold..

reply

tamimio
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Results of vibe coding and vibe configurations.

reply

kinkuraj
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Yes I received an 2.8m USD budget alert.

reply

reaperducer
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Obvs have created an urgent AWS support ticket.

I think I would have just waited to see what happened when AWS tried to hit my credit card for $1,700,000,000.When do you ever get that opportunity?

reply

mrcwinn
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

So long as customers are good for it, AWS is about to crush earnings!

reply

xbar
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Rife.

reply

tcp_handshaker
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

If its less than 2 billion is likely to be real :-)
I would relax only if its in the trillions ...

https://news.ycombinator.com/item?id=48945681

reply

jameskilton
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

My personal photo backup S3 account, with a budget limit of $10, now going to cost me ....

$1,299,988,247,332.56!That was a fun set of emails to wake up to, figured they had to be phishing for how outrageous of a number it was. But nope! Fun little incident they've got going over there.

reply

nprateem
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I guess on the plus side I'm $1.7B better off so I can retire...

reply

znpy
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Is AWS in their "move fast and break things" era ?

reply

jagged-chisel
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Lumber along and smash stuff

reply

cyanydeez
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

AWS has become the uber employer: before AWS, you just had regular employers steeling employee wages bit by bit by forcing work, skipping breaks, etc.

All hail the new generations of our uberployers.

reply

hokkos
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Same, i am now a slave to Jeff Bezos to the end of my life.

reply

jatin_oo71
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

storage, compute cost is increasing
AWS be like lets increase prices

reply

tgv
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Mine was a mere $49B. Fucking idiots.

reply

atmosx
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Cheap!

reply

mapt
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

AMZN Q2 numbers are in, and it turns out they're going to Goldman Sachs the AI bubble.

reply

tlovage
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I got estimated costs of $56.something billions. Usually ~$100/month. My heart rate currently still sits at around 160 bpm. Motherfuckers.

reply

huntoa
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

invoicemaxxing

reply

pelagicAustral
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Imagine it not being a bug...

reply

Sebb767
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

As the famous saying goes: If you owe the bank a million dollars, you have a problem. If you owe the bank a billion dollars, the bank has a problem.

reply

speedgoose
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Time to become a shepherd in some remote mountains.

reply

RGamma
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Surprise hyperinflation. Check the breadshelves!

reply

jatin_oo71
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

aws becoming first quadrillion dollars company

reply

lovich
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

You really should get your spending under control. Unfortunately unless you become one of the real people class through a large lottery, it sounds like you owe the rest of your life to AWS until you can pay off your debts for being so careless.

reply

cyanydeez
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

someones been dognfooding the AI too muxh

reply

1-6
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Fast and loose with billing data. Welcome to the new Amazon.

reply

ratelimitsteve
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

a billion here, a billion there, sooner or later it adds up

reply

1234letshaveatw
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

brb, off to buy some AMZN

reply

ares623
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

this counts towards ARR right? would be stupid not to

reply

rucury
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Uhh class action incoming? $34,909,930,575.09 over here.

reply

akerl_
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

What would your damages be? They’re not actually going to charge your credit card for 34 billion.

reply

infamouscow
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I could see someone sadly taking their own life over this.

reply

rucury
 
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

I mean, emotional damages are a thing right?

reply

akerl_
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Not really in the way the media would have you believe.

Like “I was scared for a couple minutes on a Friday morning until I saw the vendor status page” is orders of magnitude away from the bar here.

reply

Neikius
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I wonder how many people died of heart attack when they saw this.

reply

Hamuko
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I hope they send out some free credits at least. I imagine quite a few people got a real fucking scare today. They haven't even sent out any corrections yet.

reply

fian
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is probably going to push me to completely close a couple of AWS accounts I setup when doing training courses so I could get certified (mandatory requirement from my work).

I'm not currently running anything and have no plans to at the moment. I've always had a mild dread that I'll suddenly get a bill for more than $0.00.If AWS can goof in a way that causes obviously massive bills (like today), what's to say they can't goof in more subtle ways and start charging small additional amounts that many people may not notice and just pay it.

reply

r0ckarong
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Pff rookie numbers, mine was 375 billion.

reply

nigel-dev
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Small potato's sir, my bill > GDP of Switzerland. A cool $1.2T

reply

tyrelb
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I was at $5 trillion, on the way to $9 trillion.

reply

kylecazar
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

You didn't have savings opportunities enabled

reply

port3000
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Rookie error

reply

aisloper
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I blame A.I. usage

reply

bdangubic
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

eh your typical off-by-7 (zeros) programmer mistake

reply

blitzar
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

In unrelated news I just hit my target for S3 revenue (projections). Promotion meeting locked in for tomorrow (fastest in the companies history), looking forward to being a L2 Amazon employee.

reply

GuestFAUniverse
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Don't worry. With so much debt banks start to treat you with respect. /S

Honestly, I would worry more about estimated billing that seems plausible in general, but is way to high for you personally.
These ridiculous amounts? Not so much.

reply

Hamuko
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

I got freaked out by the mere fact that I got a billing alert, since getting one would require my monthly spend to have suddenly exploded.

reply

throwaway43871
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Clearly they weren't tokenmaxxing hard enough or weren't using the latest models /s.

What an absolute joke. All just so that line goes up. As if their fees weren't high enough vs. alternatives (especially egress).
And I'm sure the pro-AI crowd will keep saying we're luddites for not loving this clearly revolutionary and disruptive tech.

reply

rf15
 
4 hours ago
 
 | 
prev
 
[–]

Of course, this is only considered an error if the account is unable to pay. /s

reply

Consider applying for YC's Fall 2026 batch! 
Applications
 are open till July 27.

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