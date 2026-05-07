---
title: The Self-Cancelling Subscription
url: https://predr.ag/blog/the-self-cancelling-subscription/
date: 2026-05-07
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-08T08:14:44.068879
---

# The Self-Cancelling Subscription

# The Self‑Cancelling Subscription

## Situation
- Family was watching a streaming service that was a perk of a credit‑card.
- Suddenly the UI showed “Start your free trial” and the subscription was deactivated.
- The author suspected a desynchronised credit‑card record after the card had expired and been replaced.

## Initial Fix Attempts
- Updated the card information on the streaming service and on the bank’s website.
- Toggled the perk on and off, which restored service for about five minutes before it cancelled again.
- Received repeated “Your Subscription Expired” emails each time the service stopped.

## Support Interaction
- Contacted both the credit‑card issuer and the streaming provider; each claimed “no issues on our end.”
- Was bounced between support teams, each confirming an activation followed by an orderly cancellation five minutes later.
- Tried typical debugging steps (different device, clearing cache) without success.

## Personal Debugging
- Unlinked the bank account from the streaming service before going to sleep.
- Next morning re‑linked the accounts and waited; the subscription remained active with no cancellation emails.

## Theory of What Happened
- The problem behaved like a race condition between synchronous linking and asynchronous unlinking.
- Linking is presented to the user as synchronous, but background work (e.g., notifying the bank) occurs asynchronously.
- Unlinking is performed asynchronously on the streaming side.
- When linking and unlinking happen close together, the asynchronous unlink may be processed after the synchronous link, causing the system to think the subscription should be cancelled a few minutes later.

## Key Takeaways
- Systems that span organizational boundaries can have mismatched timing guarantees.
- Even “easy” fixes like updating a card can trigger hidden race conditions.
- Observing the order and timing of side‑effects (link vs. unlink) can reveal the root cause.