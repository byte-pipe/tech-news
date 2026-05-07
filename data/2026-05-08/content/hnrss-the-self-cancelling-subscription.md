---
title: The Self-Cancelling Subscription
url: https://predr.ag/blog/the-self-cancelling-subscription/
site_name: hnrss
content_file: hnrss-the-self-cancelling-subscription
fetched_at: '2026-05-08T08:12:55.448171'
original_url: https://predr.ag/blog/the-self-cancelling-subscription/
date: '2026-05-07'
description: When family TV show night became systems debugging night.
tags:
- hackernews
- hnrss
---

# The Self-Cancelling Subscription

 April 01, 2026
 
 

april cools

debugging

personal

Happy April 1st! This post is part ofApril Cools Club: an April 1st effort to publish genuine essays on unexpected topics. Please enjoy this true story, and rest assured that the tech content will be back soon!

One Friday night a few months ago, my family and I sat down to relax and enjoy a TV show on our streaming platform of choice. The subscription was a perk of one of our credit cards, and we had been satisfied customers for several months.

This time was different. Instead of a "Continue watching" button, we saw "Start your free trial."

Our streaming subscription had been deactivated.[Sidenote:I'm intentionally not naming companies here. Systems are hard, and systems across organizational boundaries are even harder. This essay will do more good in the world in an educational capacity than in a "name names thereby throwing engineers under a bus" capacity.]

* Easy to fix, surely?
* "No issues on our end"
* Support ping-pong, and debugging steps for someone else
* Black-box debugging to fall asleep
* What (probably) happenedA sync-vs-async race conditionHow waiting fixed the problemWhy did the account get deactivatedoriginally?
* A sync-vs-async race condition
* How waiting fixed the problem
* Why did the account get deactivatedoriginally?
* Systems are hard

## Easy to fix, surely?

Not a big deal, I thought. The credit card info must have gotten desynchronized.

The streaming service requires a credit card on file. Our card there had recently expired and been replaced. Sometimes vendors are either lenient toward this, or areable to update the card automatically— but perhaps not this time?

I used another device to log in and updated the credit card on file. Then I was surprised by service asking to charge my card for the subscription instead of applying the credit card perk.[Sidenote:The perk was from one credit card, while the card on file was a different card. Did this play a part in the confusion? Who knows!]

Time for the good old "turn it off then turn it back on again" method! I logged into the bank's website and toggled the streaming subscription perk back and forth.[Sidenote:Separately, I also updated the card on file with the streaming provider to the new, valid card.]Easy enough!

Everything worked ... for about 5 minutes 🤨

We barely got past the "in the last episode" recap, when the playback got paused and the dreaded "Start your free trial." message re-appeared.

I barely got out a "What the..." when my phone flashed a notification: a new email with the subject line"Your Subscription Expired."

Huh.Weird.

Surely a glitch, right? I hadjustset up the subscription, how could it possibly have expired?

When in doubt, turn it off and turn it back on yet again.

Another 5 minutes of streaming TV later — same thing! The show stopped cold, and I hadyet anotheremail claiming my subscription expired.

## "No issues on our end"

With our thrilling TV show replaced by a thrilling debugging session, I was becoming profoundly grumpy.

I don't particularly enjoy talking on the phone. I enjoy calling support even less. But my grumpiness gave me energy to pick up the phone and call the credit card support line.

"No issues on our end," they said! Everything looked in order. There was a valid activation of the streaming perk, and a confirmation from the provider. "Must be on the other end, please give them a call" they said.

You'll never guess what the other side's support team said. Jinx! "No issues on our end!" The subscription had been activated, then cancelled in an orderly fashion about 5 minutes later.

What the...

## Support ping-pong and debugging steps for someone else

I got ping-ponged between the credit card's and the streaming provider's support lines.

They escalated me to higher tiers of support staff. I patiently waited on hold, then dutifully repeated the whole story to each new support agent.

Each party claimed, insisted, swore up and down that the problem isn't on their end. Everything was in order! Surely the issue was on the other side?

Or just maybe, had I shared my credentials with someone else who might have unsubscribed? Maybe if I tried on a different device? Or updated the streaming app? Cleared the cache?

Those are valid debugging steps. There's a good reason they are in the support script! I'm sure they are the answer tomany people'ssituation. But not here!

It was a Friday night, and I was spending a large chunk of it on the phone with support.

I just wanted to watch a TV show with my family.

## Black-box debugging to fall asleep

By this point, it had gotten pretty late in the evening — too late to start watching the show, even if somehow everything magically started to work.

But you know that nagging feeling when a problem bothers you enough that you can't fall asleep?

Yeah. I couldn't sleep. My mind was churning away!

Then it hit me ⚡

I logged into the bank website, unlinked it from the streaming account, and called it a night. I slept like a baby![Sidenote:I'm pretty sure whoever came up with this phrase never had kids of their own... Anyway, you know what I mean.]

The next morning, I re-linked the accounts to set up the streaming subscription again.

I held my metaphorical breath for 5 minutes ... 10 minutes ... 15 minutes. No cancellation email!

Success 🎉

## What (probably) happened

Obviously, I can'tprovewhat really happened.

But I have some prior experience with cursed systems problems. Regular readers may remember I previously solvedthe case of the Wi-Fi that only worked while it was raining. I also figured outwhy Safari was blocking some pages only from thesecondtime you visited.

I solved this problemby thinking about it, making a prediction, and testing it. It worked out, so I feel pretty good about my theory!

Brief recap of the facts before we dive in:

* Re-linking the subscription always worked immediately.
* The failure mode was delayed and repeatable: about 5 minutes after activation, playback stopped and an expiration email arrived.
* Support on both sides saw an orderly activation followed by an orderly cancellation, with no errors.
* When I unlinked the accounts, waited overnight, and only then re-linked them, the cancellation never came back.

Does anything jump out at you? It sure feels like "set up the subscription" and "tear down the subscription" were not happening with the same timing guarantees, doesn't it?

As a one-liner:"creation was synchronous, unlinking was async."A race condition!

### A sync-vs-async race condition

From my perspective, I unlinked the accounts first and re-linked them second. Thebank systemsobserved the same! But the streaming provider observed themin the opposite order: as if linking the accounts happened first, followed by unlinking a few minutes later.

Linking the accounts between the bank and the streaming provider is a synchronous process,[Sidenote:At least mostly — the user-observable part is sync, but there's likely additional async work behind the scenes.]for both technical and user experience reasons. For example, it makes sense to get the user access as quickly as possible! "Click here and you're done" feels good, "click here and we'll send you an email in a few minutes" does not. To make that happen:

* The bank website produces a special link to the streaming provider's site. The link is tagged with a unique code corresponding to the user's complementary subscription.
* The streaming provider applies that special subscription to the logged-in account, offering the user to log in if they haven't already.
* The link is established and the user can start watching things!
* Meanwhile, any remaining work can be done asynchronously, such as the streaming site reporting to the bank that the subscription has been activated etc. The user doesn't need to observe this — they are happily watching something instead!

De-linking accounts is async, again for both technical and user experience reasons. A partially-sync, partially-async workflow is harder to build than one firmly on one side or the other. Here, purely-async makes more sense than purely-sync:

* From a user experience perspective, the user has no need to wait around until the link is severed. They expressedthe intentto sever the link, and were told this would be accomplished. Generally, that's sufficient.
* From a technical perspective, async workflows can recover more gracefully in case a component of the system is currently experiencing an outage — especially if the component is across an API boundary or owned by another company. Instead of a user being frustrated by an error message, the system can simply buffer the user's command then execute it after the outage is resolved.

### How waiting fixed the problem

Async workflows usually have higher latency than sync ones. The resilience of async workloads usually requires more heavyweight steps, like durably persisting data on disks.

In the case of unlinking accounts, there's also no business-imposed pressure to optimize the latency. As long as it works, it's fine — 5 minutes and 5 seconds are qualitatively the same here.Usually, at least!

Putting it all together, then:

1. I unlinked the accounts on the bank website.* This immediately flipped a flag in my profile, updating the UI to let me re-link if I wanted to.
* It also kicked off an async workflow to notify the streaming service that the subscription is discontinued.
2. I then linked the accounts again.* This synchronously took me to the streaming provider, where I completed the subscription setup.
* I then was able to start playing my TV show. Meanwhile...
3. The bank and streaming site were still asynchronously processing the unlinking event.* A few minutes later, that process was complete — deactivating my account and sending me an email confirmation of the requested cancellation. The cancellation email was due tomy act of unlinking the accounts, even though it happened in the wrong order and despite me having re-linked the accounts.

Which leaves one more mystery...

### Why did the account get deactivatedoriginally?

The streaming provider has a policy of requiring a valid credit card, even for complementary memberships via a credit card perk.

Recall that my family and I had already been watching shows there for a few months. All this trouble started right around when the credit card we had on file expired!

The most likely sequence of events[Sidenote:In which I have substantially less confidence than the other part...]rhymes with the following.

Our TV app noticed that our account was no longer in good standing — it had an expired card on file. This is against policy, so it needed to be rectified before proceeding.

Typing in a new credit card into a TV using an on-screen keyboard isnota choice most security team would endorse. Instead, the app logged us out as a means to encourage logging in on another device. A login on another device would show a prompt to update the credit card on file, and the common flow for TV app logins is to log into another device first, then enter a code or scan a QR code to cross-authenticate. Either way, the credit card gets updated.

However, the act of entering a new credit card appears to have erroneously triggered the "make a payment" flow, instead of applying the subscription perk. The perk info may have been unlinked as a result of entering the card. The fact that the card on file was not the same card providing the subscription perk may have been a contributing factor.

## Systems are hard

The real world is complex, so good systems are difficult to build!

I tell this story not to throw builders under the metaphorical bus, but with a profound sense of child-like amazement at the fact that cases like this are the exception, not the rule.

If I flick on a light switch, the lights turn on — yet I don't need to know where those electrons came from nor how they got here. Amazing!!

Only when thingsdon'twork do we usually notice the systems at hand. Complaining about an outage means thedefault caseis that things just work!

"Working" is not the natural state in a complex world! It's a testament to the combined energy and skill of many people that systems are built and kept working well enough for long enough so as to become invisible.

A system quietly becoming invisible should be celebrated. That's why this essay exists.

To the builders 💖

If you liked this essay, considersubscribing to my blogor following me onMastodon,Bluesky, orTwitter/X.

Discuss onlobste.rs.

Machine-friendly markdown version with the same content:https://predr.ag/blog/the-self-cancelling-subscription.md