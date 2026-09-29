---
title: An AI broke five of China's new crypto candidates in a day · freenode
url: https://freenode.net/article/an-ai-broke-five-of-chinas-new-crypto-candidates-in-a-day
site_name: tldr
content_file: tldr-an-ai-broke-five-of-chinas-new-crypto-candidates-i
fetched_at: '2026-09-29T16:48:45.461638'
original_url: https://freenode.net/article/an-ai-broke-five-of-chinas-new-crypto-candidates-in-a-day
date: '2026-09-29'
published_date: '2026-09-29T15:22:35.903890+00:00'
description: NGCC's first round of post-quantum submissions is collapsing under human and machine cryptanalysis, and the fastest breaks came from an AI running on its own.
tags:
- tldr
---

Analysis
Security & Cryptography
By staff
September 29, 2026

# An AI broke five of China's new crypto candidates in a day

NGCC's first round of post-quantum submissions is collapsing under human and machine cryptanalysis, and the fastest breaks came from an AI running on its own.

L

## A first round that did not survive the week

On 21 September, Ericsson's John Preuss Mattsson told the NIST pqc-forum that China's Next-Generation Commercial Cryptography program, NGCC, had published its first-round candidates: 84 public-key algorithms and 35 hash algorithms, with dedicated mailing lists for each competition. "Will be interesting to follow," he wrote. It was. Within days the forum filled with breaks, and the fastest of them were not found by people.

By the same afternoon Markku-Juhani O. Saarinen was maintaining a live tracker of NGCC failures at ngcc.dev, and the early entries alone read like a post-mortem: trivial hash collisions in every implementation of the Eijen and MasterCube candidates, an ineffective implicit rejection that breaks IND-CCA security in Aigis-Enc+, rejection-mask leaks that expose the shared secret in CheetahKEM and LoongKEM, publicly reproducible secret keys in the code-based HEP-QC, and a lattice KEM, Polar-KEM, whose submission "ships a complete public-key-only break." Most of these, Saarinen noted, "are pretty easy to verify."

## The machine did the cryptanalysis

The entries that drew the most attention arrived on 25 September, when Martin Feussner posted five separate attacks against five different NGCC signature candidates in the space of a few hours. Each carried the same disclosure: the attack "was independently found by an AI system, OpenAI Codex using Daybreak Blue at maximum reasoning effort, without a human first proposing this specific attack," and "the attached manuscript describing the attack was also produced by the AI."

The results were concrete. Against VDOO-128, the AI produced a public-key-only forgery accepted by the verifier in about 12 minutes. Against Sigurd, it recovered signing witnesses from 4 to 8 ordinary signatures and forged fresh messages for all 35 tested keys across three parameter sets, the slowest run finishing in under 17 seconds. Against Chinith it demonstrated a universal forgery on all 14 parameter sets, each forgery taking between 0.011 and 2.66 seconds. Against BiT-128 it recovered an equivalent signing key from 200,000 signatures in about 139 seconds. Against Shuttle it recovered equivalent keys for all three parameter sets, the largest run against Shuttle-512 taking roughly 37 minutes.

Feussner was careful about scope. Several of these, he stressed, target the submitted reference code rather than the scheme as designed: the VDOO forgery "exploits the central-map construction used in the implementation and is not an attack on VDOO as defined in the specification," and the Chinith break exists because both submitted implementation trees omit a value, the reconstructed QuickSilver constant term, that the specification says must be bound into the final Fiat-Shamir challenge. He also flagged that the attacks "have not yet undergone thorough independent human verification."

That verification came quickly anyway. Saarinen reproduced most of the findings the same day and assigned them tracker designations. When Jacob Alperin-Sheriff asked, "Wow how many more of these are you dropping today?", Feussner answered: "As many at the audit finds. It's still running. Crazy times."

## Not the only model

Feussner's Codex runs were not the week's only machine-found break. Three days earlier, Ward Beullens and Basil Hess reported a key-recovery attack on the round-3 additional-signature candidate SNOVA over fields of odd characteristic, recovering secret keys for two security levels in as little as 22 seconds. Their disclosure carried its own note: "The first version of this attack was found independently by an AI system (gpt-5.6-sol). We only verified the correctness, made small improvements, and wrote up the attack."

The SNOVA case is also a useful corrective against overreading. Beullens and Hess clarified a day later that the affected parameter sets are alternative sets, not the main proposal, and the SNOVA team confirmed it: the recommended round-3 parameters are defined over fields of characteristic 2 and are unaffected, the specification issue has been corrected in version 3.1, and the vulnerable alternative sets had been included "to encourage further cryptanalytic investigation." Alperin-Sheriff's read on the AI's role was similarly measured: "I am certain you'd have found it in a few weeks even in the dinosaur pre-AI age." The machine compressed the timeline. It did not invent the result.

## The humans kept pace

People were breaking things too, and the sharpest single result of the week was human. Jintai Ding's lab announced what it called a total break of Origami, an NGCC round-1 signature candidate: a universal forgery in which, "given only a public key, an attacker can sign any message of their choice, with no signing queries," in about 0.01 seconds for Origami-128. Crucially, Ding wrote, the forgery "follows from the specification, not from an implementation error, and it contradicts the security proof of the submission," making it, to his knowledge, the first NGCC round-1 candidate "totally broken for all security levels." Pierre Pebereau reported a near-identical attack he had disclosed to the authors days earlier: Origami reveals the change of variables from its private map to its public one, and inverting it "yields a system that is easy to solve." Matt Henricksen offered the epitaph: "It folded so easily." Separately, Hao Guo and colleagues estimated that VDOO's level-5 parameters, advertised at 512-bit security, actually reach about 379.

## What this changes

Two things are worth keeping straight. First, not every result is equal. A spec-level break like Origami's says the design is dead; an implementation-specific forgery like Chinith's or Shuttle's says the reference code is dead, which is embarrassing and dangerous but repairable. Feussner's own hedging ("potential," "not yet verified") deserves to survive into any headline, even if Saarinen's independent reproduction removes most of the doubt. Second, and less comfortably, a national standardization program's first round should not fall apart in a week, and this one did, across hash functions, KEMs, key exchange, and signatures alike.

The question Alperin-Sheriff put to the forum is the one that lingers. Did reasoning models take another jump in strength this week, or did submitters simply skip an audit that any of these tools could have run first? Neither answer flatters the process. If a laptop core and an off-the-shelf model can universally forge a candidate in twelve minutes, the submitters could have done the same before submitting. If they could not, the economics of cryptanalysis just changed under everyone's feet. There is even an access wrinkle: pqc-forum is hosted by Google, which is blocked in China, so the designers may not be reading the posts that dismantle their work at all, as Saarinen pointed out while directing people to the actual NGCC lists.

This lands in the middle of a run of stories, covered here recently, about models turning up as contributors and as the machine in the middle of review. NGCC is the sharper version of the same shift. The old signal, that an algorithm reached a national competition, is worth less than it used to be, at least until the machines have had their pass. The reassurance is that the same tools breaking these candidates in an afternoon can be pointed at ours, cheaply, before standardization rather than after. The warning is that from now on, if you did not run them first, someone else will, and they will post the results before you finish reading your own spec.

#post-quantum
#cryptanalysis
#ngcc
#ai
#pqc