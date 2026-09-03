---
title: Designing a Webhook Delivery System for 10 Million Events a Day - DEV Community
url: https://dev.to/lovestaco/designing-a-webhook-delivery-system-for-10-million-events-a-day-2p5d
site_name: devto
content_file: devto-designing-a-webhook-delivery-system-for-10-million
fetched_at: '2026-09-03T14:53:14.215925'
original_url: https://dev.to/lovestaco/designing-a-webhook-delivery-system-for-10-million-events-a-day-2p5d
author: Athreya aka Maneshwar
date: '2026-09-02'
description: Hello, I'm Maneshwar, and I'm building LiveReview — a blast-radius aware AI code review built for... Tagged with systemdesign, webhooks, backend, architecture.
tags: '#systemdesign, #webhooks, #backend, #architecture'
---

Hello, I'm Maneshwar, and I'm building LiveReview — a blast-radius aware AI code review built for your business-critical systems.Star usto help devs discover the project, give it a try, and share your feedback to help improve the product.

Somebody on your team is going to say it, probably in a planning meeting, probably while looking at a Jira ticket that has three words in it.

"Webhooks? That's just a POST request. Half a day."

And they are not wrong about the POST request part.

That is genuinely all a webhook is.

Something happened on your side, your customer wants to know, you send them an HTTP request. Done.

Then you ship it, and six weeks later you are on a call explaining to a customer why they missed 4,000 payment events during a window whentheir own serverwas down.

So let's actually build this thing.

Ten million events a day, which is roughly 115 a second on average and a lot more than that at peak.

I'm going to build the naive version first and then break it, on purpose, over and over, until we end up somewhere that survives contact with real customers.

## Version 1: just POST it

The obvious one. Event happens in your request handler, you post it to the customer's URL, you wait for a200 OK.

def
 
on_payment_succeeded
(
payment
):

 
db
.
save
(
payment
)

 
requests
.
post
(
customer
.
webhook_url
,
 
json
=
payment
.
to_dict
())
 
# 🙃

 
return
 
{
"
ok
"
:
 
True
}

Enter fullscreen mode

Exit fullscreen mode

This works beautifully in staging, where the "customer" is a webhook.site tab you have open in another window.

Here is what it looks like in production.

Your customer's endpoint is a Rails app on a small box that also runs their cron jobs.

At 3pm their cron kicks off, their server starts taking eight seconds to respond, and nowyourrequest handler is sitting there holding a thread hostage waiting on somebody else's infrastructure.

Your latency graph spikes. Your connection pool drains.

Your own users, who have nothing to do with this, start seeing timeouts.

And then the worst part: your request times out, the process moves on, and the event is gone.

You never wrote it down anywhere. It existed only as a variable in a function that has now returned.

The bug here is not "it was slow." The bug is that you made your availability a function of your customer's availability, and you did it in the hot path.

## Version 2: write it down first

Rule one of distributed systems, and honestly rule one of life: write it down before you try to do it.

So the handler stops posting. It writes the event to a table, in the same transaction as the business change that caused it, and returns.

That is thetransactional outbox pattern, and it is doing something subtle that is worth saying out loud.

If you save the payment and then push to a queue, those are two systems and there is a gap between them.

Crash in the gap, and you have a payment with no event.

By putting the event row in thesamedatabase transaction as the payment, the two either both happen or both don't. No gap.

BEGIN
;

 
INSERT
 
INTO
 
payments
 
(
id
,
 
amount
,
 
status
)
 
VALUES
 
(...);

 
INSERT
 
INTO
 
webhook_outbox
 
(
customer_id
,
 
event_type
,
 
payload
,
 
status
)

 
VALUES
 
(...,
 
'payment.succeeded'
,
 
...,
 
'pending'
);

COMMIT
;

Enter fullscreen mode

Exit fullscreen mode

Then a separate worker polls forpendingrows and does the actual posting.

Your handler is fast again. Your event is durable.

If the delivery fails, it fails somewhere you can see and retry, instead of in a dead stack frame.

But you have traded one problem for a sneakier one.

You have one worker, or one pool of workers, pulling from one queue in order.

Customer A's endpoint takes 10 seconds to time out.

Every worker that picks up a Customer A job is parked for 10 seconds.

Meanwhile Customers B through Z have events sitting behind them in the queue, perfectly deliverable, going nowhere.

This is head-of-line blocking, and it is the noisy neighbour problem wearing a queue costume.

One customer with a bad endpoint degrades everyone. Your worst customer sets the pace for all of them.

## Version 3: everyone gets their own lane

The fix is fairness, and fairness needs somebody to enforce it.

Put a dispatcher in front of the worker pool.

Its whole job is to decidewhich event goes next, and it is not allowed to just take the oldest one.

The dispatcher keeps a count of how many workers are currently busy with each customer.

Customer A already has 3 in flight and their cap is 3? Skip them. Take the next customer's event instead. Come back to A later.

This is per-tenant concurrency limiting, and it is the single highest-leverage thing in the whole design.

Concurrency limits are also whatStripe usesas a first-class rate limiting primitive, for exactly this reason: they bound damage rather than just counting requests.

The effect is that Customer A's disaster is now capped. Three workers are stuck on them.

Every other worker in the pool is happily serving everyone else.

A slow customer now only degrades themselves, which is the correct place for the pain to land.

If you want to go further, the dispatcher is also where you put weighted fairness, so your enterprise tier doesn't get starved by a free-tier customer emitting a million events an hour.

Here is the routing logic, which is really the heart of the system:

flowchart TD
 A[Pull next pending event] --> B{Customer at<br/>concurrency cap?}
 B -->|Yes| C[Skip, try next customer]
 B -->|No| D{Endpoint circuit<br/>open?}
 D -->|Yes| E[Park until cooldown ends]
 D -->|No| F[Hand to a free worker]
 C --> A
 E --> A
 F --> G[POST signed payload]

 classDef decision fill:#f4d35e,stroke:#b8991f,color:#1a1a1a
 classDef start fill:#e9ecef,stroke:#6c757d,color:#1a1a1a
 classDef action fill:#5ee6c8,stroke:#1f9c86,color:#1a1a1a
 classDef wait fill:#ff9a5c,stroke:#c26a33,color:#1a1a1a

 class B,D decision
 class A start
 class F,G action
 class C,E wait

That circuit breaker branch is worth adding once you have the concurrency cap working.

If a customer's endpoint has failed the last 20 attempts in a row, you already know the next one fails too.

Stop spending workers to find out.

## Version 4: sending one webhook, properly

Zoom all the way in now. A worker has picked up one job. What happens?

Short timeout. Ten seconds, not sixty. A slow endpoint is a broken endpoint and you should not let it hold a worker hostage while you find out.

Then you look at what comes back, and the important move is thatnot all failures are the same failure.

* 200,201,204: delivered. Mark it, move on.
* Connection refused, timeout,502,503,429: temporary. Their server is having a moment. Retry with exponential backoff, with jitter, so that when their box comes back up you don't hit it with your entire retry backlog in the same millisecond. AWS wrotethe canonical piece on jitterand it is worth ten minutes of your time.
* 404,410, DNS does not resolve, TLS handshake fails: permanent. The URL is wrong, or the endpoint is gone. Retrying this 12 times over 24 hours is not resilience, it is just you generating traffic to nowhere and delaying the moment the customer finds out their config is broken.Fail it fast and loudly.

That third bucket is the one teams skip, and it is the one that turns your retry queue into a landfill.

While we are here, two things that are not optional.

Sign the payload.Every event goes out with an HMAC of the body plus a timestamp, in a header.Your customer recomputes it with their shared secret and confirms the event actually came from you.Without this, your webhook endpoint is a URL that anybody who guesses it can post fake "payment succeeded" events to.Include the timestampinsidethe signed content so a captured request can't be replayed at them next week.

Assume they will process it twice.Retries mean at-least-once delivery.That is not a flaw you can engineer away, it is the shape of the problem: if your request times out you genuinely cannot tell whether they processed it or not.So give every event a stableid, tell your customers to key on it, and document it clearly.Exactly-once delivery is marketing. At-least-once plus idempotency is engineering.

## Version 5: the dead letter queue is a product feature

Retries run out. It happens. Their endpoint was down for the whole eight hour retry window and there is nothing more to try.

The event does not get deleted. It goes to a dead letter queue.

And here is the part I really want to land, because it is where most implementations stop one step too early:a dead letter queue nobody can see is just a slower way of losing data.

Put a UI on it. A dashboard, in your product, where the customer can see their own failed deliveries.

Event type, timestamp, attempt count, the actual response body you got back from their server.

That last one saves so many support tickets, because "we got502 Bad Gatewayfrom your server at 3:04pm" ends an argument that "webhooks are broken" would otherwise stretch across four days.

Then give them a Replay button.

They fixed their deploy, they click replay, the events go back into the outbox as pending and flow through the exact same pipeline.

Bulk replay for a time range, so they can recover a whole outage window in one click.

You have just converted your worst support conversation into a self-serve action. That is a genuinely good trade.

## The whole thing, end to end

flowchart LR
 APP[App writes event<br/>+ business change<br/>in one transaction] --> OUT[(Outbox)]
 OUT --> DISP[Dispatcher<br/>per-customer caps]
 DISP --> W[Worker pool]
 W -->|HMAC signed POST| CUST[Customer endpoint]
 CUST -->|2xx| DONE[Delivered]
 CUST -->|5xx / timeout| RETRY[Backoff + jitter]
 CUST -->|4xx permanent| DLQ[(Dead letter queue)]
 RETRY --> W
 RETRY -->|attempts exhausted| DLQ
 DLQ --> UI[Replay UI]
 UI -->|customer clicks replay| OUT

 classDef store fill:#9d8cff,stroke:#5b4bcc,color:#1a1a1a
 classDef proc fill:#5ee6c8,stroke:#1f9c86,color:#1a1a1a
 classDef ext fill:#6ea8ff,stroke:#3565bd,color:#1a1a1a
 classDef bad fill:#ff9a5c,stroke:#c26a33,color:#1a1a1a

 class OUT,DLQ store
 class APP,DISP,W,UI,DONE proc
 class CUST ext
 class RETRY bad

Read it as one sentence: write it down before you send it, be fair about who you send next, send it signed with a short timeout, retry the failures that deserve retrying, and make the ones that don't visible to the human who can actually fix them.

## The bits that bite you later

A few things that don't fit neatly into the versions but will absolutely find you.

Ordering.Somebody will ask for it. Ordered delivery per customer means concurrency 1 for that customer, which means one slow response stalls their entire stream. It is a real trade, not a free feature. Usually the better answer is to send a sequence number and let them sort, or send a "something changed, come fetch it" ping instead of the state itself.

Payload size.Do not put a 4MB object in a webhook. Send the id and the event type, let them call your API for the rest. Thin payloads are cheaper to store in the outbox, cheaper to retry, and they sidestep the awkward question of what happens when the state changed between the event firing and them reading it.

SSRF.Customers hand you a URL and you make your servers fetch it. That is textbook server-side request forgery. Resolve the hostname, reject private ranges and link-local addresses, and re-check on redirects, becausehttp://customer.com/hookredirecting to169.254.169.254is somebody trying to read your cloud metadata credentials.OWASP has the full list.

Poison events.One event that crashes your worker on deserialize will be retried forever and take a worker down with it every single time. Cap attempts on yourownfailures too, not just theirs.

Meme idea 3— Template:They Don't Know(the guy alone in the corner at a party, thought bubble)

* Thought bubble: "they don't know my webhook endpoint is a Google Sheet"

## So, half a day?

The POST request is half a day. Genuinely.

The other 95% is the outbox that keeps the event alive, the dispatcher that stops one customer from ruining everyone's afternoon, the retry classifier that knows the difference between "try again" and "this will never work", and the replay UI that turns a data loss incident into a button.

None of that is exotic. It is one table, one dispatcher loop, and a bit of discipline about failure modes.

But it is the difference between a webhook system your customers trust and one they write defensive polling code around, which is what they will do the second they miss an event and you cannot tell them where it went.

Write it down first. Everything else follows from that.

If you have been building on top of a webhook pipeline like this, I'd genuinely like to hear which version you're currently stuck on.

My guess is version two, and the customer causing the jam is one you can name from memory.

Your team's attention is limited, and the deluge of AI-generated code is making it harder to keep production code safe without slowing you down.

I'm buildingLiveReview, a blast-radius aware AI code review built for your business-critical systems.

Instead of presenting every diff with equal emphasis,LiveReview scores each change by blast radius — how far its impact reaches through your call graph — so you can focus attention where it actually matters.

Spend code review effort where business risk is highest — not spread evenly across every diff.

Try LiveReview on your codebase:

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse