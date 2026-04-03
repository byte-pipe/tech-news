---
title: Is End-to-End Encryption Optional For Large Groups? - Dhole Moments
url: https://soatok.blog/2026/02/14/is-end-to-end-encryption-optional-for-large-groups/
site_name: lobsters
content_file: lobsters-is-end-to-end-encryption-optional-for-large-groups
fetched_at: '2026-02-17T06:00:38.738428'
original_url: https://soatok.blog/2026/02/14/is-end-to-end-encryption-optional-for-large-groups/
date: '2026-02-17'
published_date: '2026-02-14T16:54:26+00:00'
description: 'One of the recent topics in Messaging App Discourse is whether it makes sense to prioritize End-to-End Encryption (E2EE) when searching for an alternative to Discord. Who''s Saying "No"? I''m going to quote 0xabad1dea here, because she is awesome and explains my "opposition" position better than anyone else: So You Want To Write An Open…'
tags: cryptography, security
---

One of the recent topics in Messaging App Discourse is whether it makes sense to prioritize End-to-End Encryption (E2EE) whensearching for an alternative to Discord.

## Who’s Saying “No”?

I’m going to quote 0xabad1dea here, because she is awesome and explains my “opposition” position better than anyone else:

So You Want To Write An Open Source Discord Replacement

Things you don’t need:– federation/distributed systems– multiparty end-to-end encryption(…)

0xabad1dea
 (link to the full post)

She then followed this up witha second post, pointing tothis news story, highlighting the dangers of overconfidence in your encrypted messaging software with large numbers of hard-to-vet participants.

Her overall argument is a simple one to understand, and is congruent to the one I made in my previous post: You cannot hope to replace Discord for the overwhelming majority of its users if you don’teven know what Discord is for them. The user experience is more important to adoption than federation or even encryption. You don’t need to build infrastructure for “planning the revolution” to replace Discord.

While everything 0xabad1dea said is true, we need to stop and ask, “Why is Discord even pushing for age verification to begin with?”

## Why E2EE Still Matters

You could point tothe anti-porn lobby’s strategiesthat have been at play for years, to start with: Target infrastructure to repress everyone.

Discord isn’t pushing for this because they want to, they’re pushing for this because they’re a centralized platform used by millions of people. Not only do Christian extremist groups look for these single points of failure in their lobbying efforts, many countries and states have pushed for laws requiring platforms verify the age of the users.

Cryptographers know how to satisfy these requirementswithout sacrificing user privacy, but, often, these laws do not allow such measures.

### Age verification requirements and centralization go hand-in-hand.

Federated platforms have two advantages, and one massive crippling disadvantage.

Federated systems do not create a giant central hub that lobbyists and right-wing politicians can target. Additionally, users can choose instances that do not exist under the jurisdiction of oppressive laws.

However, if a viable federated alternative springs up, the Christofascists will simply change their tactics: Have law enforcement investigate large instances and harass the people that operate them.

The downside of federation is that most instance operators do not have the war chest or legal resources to fight overreaching government demands (nor extralegal measures taken against payment processors). They’re lucky if their operational budget is solvent to begin with.

And that is the reason end-to-end encryption matters for federated systems: If law enforcement shows up demanding all of your user data, if it’s all encryptedso even you can’t decrypt it, you can only surrender ciphertext to the authorities.

In short, the reason multiparty end-to-end encryption is still important for any Discord alternative is as follows:

1. Any centralized system will inevitably need to comply with stupid age verification laws.Without federation, your alternative will follow suit.
2. Any federated system that has access to user messages will be a juicy target.Without E2EE, your instance operators are at high risk.

End-to-end encryption doesn’t just protect the users, it protects the people operating the infrastructure. And that’s why it still matters.

Art: CMYKat

## E2EE Should Be Ubiquitous

Secure end-to-end encryption needs to become table stakes for communication software.

In an age where user data is sold to the advertising industry and large language models are trained on users’ posts, the less data that service operators can slurp up, the better.

But additionally, we need to make its existence somundanethat no one becomes overconfident about their use of encryption.

“Don’t plan your crimes in a chatroom full of 300 people” should be common sense, whether or not that chatroom uses encryption properly.

### E2EE Should Be Better Than Today

If your understanding of E2EE is informed by using Matrix or XMPP+OMEMO, you might think this is bonkers. That is because you are coming from a bonkers user experience.

For example, Matrix’s encryption library only allows you to buffer40 ratchetsbefore encryption becomes unusable.

In order to make E2EE ubiquitous, the developers need to step up their game to make E2EE better.

### Can E2EE Scale to Thousands of Users?

Yes. I explored this inmy proposal for encrypted messaging for BlueSky.

TreeKEM from RFC 9420 (Messaging Layer Security) scaleslogarithmicallyto the number of participants.

A server with a million users would only require about 21 key encapsulations per group operation. The bandwidth of that is digestible for most folks. And then, for the epoch following each key agreement change, you only need symmetric-key ratcheting.

CMYKat

### What About Message History?

What about it?

There’s no law of mathematics saying you can’t create an encrypted backup feature that lets you persist history across devices, or across identities, if you really want to. Go nuts.

## Closing Thoughts

I was originally going to write this as an addendum to my Discord post, but ultimately felt it was nuanced enough to warrant a separate, focused discussion.

Header art:Harubaki,CMYKat,Johanna Tarkela

* TagsDiscord,E2EE,Online Privacy,Politics



## By Soatok

Security engineer with a fursona. Ask me about dholes or Diffie-Hellman!

			View Archive
→
