---
title: '''This is absolutely not being overhyped'': Sherrod DeGrippo on the PHP flaws and AI''s cybersecurity reckoning'
url: https://www.groundlevel-ai.com/p/php-vulnerabilities-ai-cybersecurity-sherrod-degrippo
site_name: tldr
content_file: tldr-this-is-absolutely-not-being-overhyped-sherrod-deg
fetched_at: '2026-10-22T22:04:34.465028'
original_url: https://www.groundlevel-ai.com/p/php-vulnerabilities-ai-cybersecurity-sherrod-degrippo
author: Sharon Goldman
date: '2026-10-22'
description: Palo Alto Networks’ Unit 42 threat intelligence chief says AI-driven vulnerability discovery is “the new normal” — and explains why she’s surprisingly optimistic.
tags:
- tldr
---

# 'This is absolutely not being overhyped': Sherrod DeGrippo on the PHP flaws and AI's cybersecurity reckoning

### Palo Alto Networks’ Unit 42 threat intelligence chief says AI-driven vulnerability discovery is “the new normal” — and explains why she’s surprisingly optimistic.

Sharon Goldman
Oct 22, 2026
10
2
Share

Governments and businesses around the world were sent scrambling to prevent hacker exploits yesterday aftertwo vulnerabilities were disclosed in PHP, a popular programming language that powers an estimated 60-70% of the world’s websites. The bugs allow hackers to execute remote code and take control of vulnerable websites.

The flaws, which had been lurking in PHP’s code for more than a decade, were disclosed, along with a patch, in a coordinated effort involving OpenAI, Wiz, PHP’s maintainers and other security firms. Researchers found them with the help of AI. The incident is raising yet more concerns about what happens when AI makes it dramatically faster and cheaper to find serious security vulnerabilities in the software underlying the internet.

I spoke this morning with Sherrod DeGrippo, VP of threat intelligence at Palo Alto Networks’ Unit 42, who called the PHP flaws a “watershed moment” in her long-running worries about the software supply chain, and said the alarm is “absolutely not being overhyped.”

This interview has been condensed and edited for clarity.

I’m making this interview free because the PHP vulnerabilities affect a huge share of the internet and the information matters now. Ground Level AI is independent and reader-supported. If you value reporting like this, please consider a paid subscription.

Subscribe

Ground Level AI: Is this a real turning point in cybersecurity? Are people right to be freaking out, or are we overhyping what AI has changed?

Sherrod DeGrippo:This is absolutely not being overhyped. This is huge.

Palo Alto Networks alone has found22 million exposed instances. PHP is a programming language that essentially makes websites. It has been around a very long time. It’s older; it’s not on trend or in fashion.

But what’s interesting is that the things that are old and not in fashion are mostly the ones that create the infrastructure and bottom line of the internet. These are the things that the internet runs on.

We were fortunate enough to have some heads-up on this vulnerability. The PHP Foundation let certain providers know this was coming out ahead of time so we could prepare and put mitigations in place.

It’s the new normal, unfortunately. We’re going to be in this scramble, this vulnerability velocity, for some time to come. AI is really good at finding vulnerabilities. It finds them very quickly, and it finds high-severity and critical vulnerabilities very quickly.

Our hope is that AI finds these vulnerabilities, and then we quickly use AI to mitigate them, either by patching the code itself or creating some kind of compensating control. If you can’t patch right now, you can use a firewall to block the traffic from coming in at all.

But in this particular instance, traditional wisdom doesn’t fit as well because these are all web-facing systems. Many of them are not protected well. Many of them are very old. Some organizations don’t even know that they have PHP or how much they have.

So this one was really concerning. It’s a 9.2 out of 10 on the severity scale. It’s a critical vulnerability. At this point, we have not seen in-the-wild exploitation. We have seen proof-of-concept code. We’ve found over 200 examples of proof-of-concept exploit code, and we’re testing those.

Security is a process, not a product. It’s not like there’s an end where we’re just like, okay, we’re secure, it’s done. That’s not how it works.

Does the fact that you haven’t seen exploitation yet make you any less worried?

No, because it is imminent if it hasn’t happened already. There may be successful exploitation in the wild that we just haven’t seen.

It’s either here or coming. That’s guaranteed, because PHP is such a massively globally deployed technology that threat actors know there are millions of available instances of vulnerable PHP out in the world.

Every threat actor in the world right now is working on this — both military espionage, nation-sponsored and financially motivated crime.

As a layperson, I keep thinking of the internet as an old New York City subway system that needs repairs. These vulnerabilities have been there all along, but AI is suddenly exposing them. Is that how you see it?

I think that’s apt. It’s always been this way. I want to be clear about that. These vulnerabilities have always been there, but now we have this really powerful flashlight, and we’re crawling around under the track like, wow, there’s a hole in the floor, and that wheel is rusting off.

And those of us who’ve been doing subway maintenance for a long time are like, yeah, we’ve been fixing it day in and day out. But now it’s like, oh my gosh, I can see so much more. Not all, but so much more. AI is that flashlight under the subway car, showing us the little flaky, rusted pieces and the broken axle. And we’re like, I’m not comfortable having passengers on this car.

The NSA recommended that anything that couldn’t be patched immediately that was internet-facing should be turned off from the internet. I agree. If you don’t have other controls in place and you’re not able to patch, you have to take your presence offline, or you have an incredibly high risk of being breached.

It seems like AI is changing the economics of vulnerability discovery. Finding serious flaws is becoming cheaper and faster, but defenders still have to deal with every one of them. How does that change things?

We’ve always had vulnerabilities coming in. Patches need to be applied. If you can’t apply the patch, then you have to have mitigating controls. That’s been our lives for a long time.

But AI has increased the velocity. It’s so accelerated now that it feels much more urgent, and it is. Where there might have been one or two massive vulnerabilities in a month, we’re starting to see bigger, more severe vulnerabilities than we have before.

It’s almost like climate change in some ways. We used to get one big storm a year, but now we’re getting a couple of hurricanes during hurricane season, and they’re bigger than they’ve ever been.

Every month is a bigger patch experience than the month before. And that’s the path we’re on probably for the next year or two.

Does this mean the policies and processes around vulnerability disclosure have to change? Traditionally, companies have had weeks or months to coordinate fixes before making vulnerabilities public. Can that approach survive this acceleration?

I would not recommend significant changes to vulnerability disclosure programs and processes. I think bug bounty programs and disclosure programs over the past couple of years have gotten to the point where they work.

I come from the olden times of what was called Bugtraq and Full Disclosure. If you had a vulnerability, you just posted it on a mailing list. Devil may care what’s going to happen. Just post it out there and watch the chaos unfold.

We’ve worked over years to change things from Wild West chaos to what we have now, which are coordinated vulnerability disclosure processes.

I’m very impressed and fortunate to be part of these programs. We’ve matured as an industry to get where we are.

What I don’t want to see are organizations included in these early warning disclosures leaking them for their own purposes. That’s something we have to maintain our integrity as security professionals and not do.

Are we headed toward a world where companies simply can’t patch fast enough? What’s a security team supposed to do?

We’ve always been in a world where security teams can’t patch fast enough. Organizations have to get used to the pace a little bit. They’re going to have to think about things beyond just vulnerability management. That’s not going to be enough anymore.

They’re going to have to change the way they think about prioritization and protection, understand what their exposure actually is before these brutal vulnerabilities come out, know what could happen and understand what that would look like.

And something that’s really important to me is having a plan for resilience. We can’t live with this idea that if we do enough security, we’ll never get breached.

We need security policies and programs in place, and our security posture needs to continue improving. But we also need a resilience plan for when something does happen.

For example, if an organization has PHP and couldn’t patch, they should know that they have backups of the data, segmented networks and a plan for what actions to take if something happens. Resilience is required now. It’s not a nice-to-have.

What scenario worries you most over the next few months?

I think this PHP event is a watershed moment in a lot of ways for me, because the thing I’ve always been concerned about is the software supply chain.

PHP is both part of and a consumer of the software supply chain. And it’s open source, which just goes to show that having access to the code doesn’t mean it’s vulnerability-free.

The software supply chain is very delicate. It’s this foundation that the internet is coded upon everywhere. So resiliency to the software supply chain is really important.

Separately, I have a lot of concerns around non-human identities — machines logging into other machines, persistence, service principals, certificates, cookies, all these different access and authorization mechanisms that we use to allow computers to talk to other computers.

You can’t use multifactor authentication for those kinds of identities. A lot of organizations have many of them and don’t have an inventory of what they are or how they’re permissioned.

After everything you’ve described, is there anything that makes you optimistic?

I actually am extremely optimistic. I talk with my industry peers all day, and we’re really optimistic because, frankly, we knew the subway car needed maintenance. And now we’ve handed everyone flashlights.

Let’s take advantage of the spotlight. Let’s take advantage of the focus on some of these repairs that need to be done. Yes, this is dire. Yes, this is urgent. Yes, I am very stressed out about these two PHP vulnerabilities. But it’s time. Let’s do it.

Many of us are veryAvengers assembleabout it right now. We’re all in these chats together, going, do you have that one? Do you have this? Are you coordinated? Do you have indicators of compromise? Do you have protection signatures?

Everyone’s working together as fast as we can. And we’ve always wanted that. We’ve always wanted everyone to take this seriously and put effort into it.

I’m optimistic that we’re getting the work done because this needed to be done either way. The vulnerability existed either way. Now we have the opportunity to gather our resources, get in the driver’s seat and take care of it.

We’re gonna patch all the PHP in the world. That’s pretty cool.

10
2
Share
Previous