---
title: 'A Vibe Is Not a Verdict: I Built a Tool That''s Allowed to Say ''I Don''t Know'' - DEV Community'
url: https://dev.to/copyleftdev/a-vibe-is-not-a-verdict-i-built-a-tool-thats-allowed-to-say-i-dont-know-4foe
site_name: devto
content_file: devto-a-vibe-is-not-a-verdict-i-built-a-tool-thats-allow
fetched_at: '2026-07-17T11:31:52.098362'
original_url: https://dev.to/copyleftdev/a-vibe-is-not-a-verdict-i-built-a-tool-thats-allowed-to-say-i-dont-know-4foe
author: Don Johnson
date: '2026-07-13'
description: My gut screamed scam. My tool said 'I don't know' — and that refusal is what actually cracked the case. An experiment in why honest CLIs beat confident ones. Tagged with ai, rust, cli, security.
tags: '#ai, #rust, #cli, #security'
---

Rust CLI for vetting suspicious links

A tool should do one thing, do it well, and — this is the part everyone forgets — know exactly where its knowledge ends.

I builtkilofor a morning like this one. I just didn't know the morning would come this soon.

## The message that was waiting for me

I woke up, poured the coffee, and did the thing you're not supposed to do before you're fully awake: I opened my messages. And there it was, sitting at the top of the inbox like it had been placed there on purpose — a cold recruiter pitch.

An "exciting opportunity" for a Quality Engineer role at an aerospace firm. Warm, professional, faintly urgent.Please click the link below to view the job description and apply.The link was a long tracking URL, the kind with an opaque token andsourceandmethodparameters stapled to the end.

And then the signature. One "recruiter" who claimed, in a single line, to be a physical therapist, a call-centre manager, an e-commerce power seller, a freight dispatcher — half a dozen unrelated trades piled into one job title, now, apparently, placing quality engineers at an aerospace company. That's not a résumé. That's a slot machine.

There it was: the exact situation I wrote the tool for, delivered to my inbox before I'd finished the coffee.

Because here's what would normally happen next. My gut saysscam. My gut is usually right. But "usually right" is how you eventually click the one link that isn't. A gut feeling is a vibe, and a vibe is not a verdict. That frustration is precisely why, months ago, I sat down and wrotekilo— a way to stop feeling about an address and start knowing about it. So this morning wasn't an annoyance. It was the experiment finally running itself.

I put the coffee down and opened a terminal.

## What I actually built, and why

Let me back up and tell you whatkilois, because the design is the whole argument.

KiloCheckis an offline IP-reputation engine. One binary. ~12MB. Written in Rust. Its entire worldview is a four-stage pipeline:ingesta signed, versioned threat release →normalizetyped observations →compilean immutable local index →checkIPs against it. Cryptographically verified going in. Zero network calls coming out.

I made it offline on purpose. An ordinary check never reaches an intelligence API. When I'm triaging something sketchy, I don't want my queries leaking, I don't want to tip anyone off, and I want the same answer at 3AM on a plane as I get at my desk. The threat knowledge is baked into a signed local snapshot. The check is just a lookup against evidence I already trust.

Install is a checksum and a copy — the way a tool should be:

curl 
-fsSL
 https://raw.githubusercontent.com/copyleftdev/kilocheck/v0.2.0/scripts/install.sh | sh
kilo update 
# pulls the signed data release → prints "Claims 3160"

kilo status 
--json

# → "integrity": "verified", "freshness": "fresh"

Enter fullscreen mode

Exit fullscreen mode

That was the tool. This was the morning. Time to point one at the other.

## The experiment, step one: turn the lure into a number

kiloanswers exactly one question —is this IP a known bad actor?— so first I had to turn that tracking link into an address. That'sdig's whole job: resolve the hostname behind the URL down to the IP actually serving it.

$ 
dig +short <the-redirect-host>
203.0.113.90

Enter fullscreen mode

Exit fullscreen mode

Then I asked my tool the question I built it to answer. This is the moment the experiment either validates the design or embarrasses me:

$ 
kilo check 203.0.113.90 
--json
 | jq 
'.data[0].verdict'

Enter fullscreen mode

Exit fullscreen mode

{

 
"disposition"
:
 
"unknown"
,

 
"confidence"
:
 
0.0
,

 
"recommended_action"
:
 
"monitor"
,

 
"reason_codes"
:
 
[
"NOT_OBSERVED"
]

}

Enter fullscreen mode

Exit fullscreen mode

NOT_OBSERVED. Confidence0.0.

And I grinned, because this is exactly the behavior I designed for — and the exact behavior a worse tool would have gotten wrong.

Think about the pressure in that moment. I clearly think it's a scam. The vibe is overwhelming. A tool built to please its operator would have felt that pressure and handed me a scary red verdict to confirm what I already believed.kilorefuses. It says:I have no evidence about this address, and I am not going to invent some to make you feel clever.

That refusal is the single most important thing I built into it.A tool has to know the difference between "safe," "bad," and "I don't know" — and it has to refuse to smear them together.Missing, unknown, stale, incomplete, unsafe: five distinct states in my model, not three shades of the same shrug. This morning it chose the honest one under maximum temptation to lie.

## Step two: prove it can still bite

An honest "I don't know" is only worth something if the same tool can say a hard "yes." Ifkiloreturnedunknownfor everything, it wouldn't be humble — it'd be broken. So I ran the control, right there in my pajamas: the suspicious host, a known command-and-control node, and a boring public DNS resolver, all in one shot. Distilled from the JSON:

203.0.113.90 → unknown monitor NOT_OBSERVED (0 sources)
162.243.103.246 → CRITICAL block COMMAND_AND_CONTROL (1 source, conf 0.99)
8.8.8.8 → unknown monitor NOT_OBSERVED (0 sources)

Enter fullscreen mode

Exit fullscreen mode

There. A known C2 node getscritical / block / 0.99with provenance attached. The public resolver and the suspicious host both get a calmNOT_OBSERVED. No false alarms on clean infrastructure, no missed alarm on a real one. The experiment held:the tool's silence means something precisely because its alarm means something.

## Step three: the twist my own tool pointed me toward

So the infra came back clean. Was my gut wrong? No — it was pointed at the wrong target. And that's the part I didn't see coming.

kilo's honest negative didn't close the case. Itmovedit. "The danger is not in this infrastructure" is a coordinate — it told me to go look somewhere else. So I followed the rest of the trail with the neighbors on my toolbelt.

curlfollowed the redirect — headers only, I never touched the body:

HTTP
/
2
 
302
 
→ /<captcha-gate>?...&source=...&method=...

Enter fullscreen mode

Exit fullscreen mode

opensslread the cert straight off the wire: a real, correctly issued certificate for a legitimate, well-known job-traffic aggregator. And a quick lookup closed the loop: the aerospace company in the pitch is real, with genuine engineering openings, and the tracking link was an affiliateclick-trackerredirecting through the aggregator's own anti-click-fraud gate. No payload. No credential harvest. No bad IP anywhere in the chain.

So what was the actual threat? It was never in the packets. It was the sender — a freelance lead-gen spammer blasting affiliate commission links across social platforms, wearing a recruiter costume stitched together from half a dozen unrelated careers.

And here's why I'm writing this at all:my own tool solved the case by refusing to pretend.Its0.0sent me away from a malware rabbit hole and toward the social-engineering signal where the truth actually lived. Ifkilohad cried wolf on clean infrastructure to match my mood, I'd have wasted the morning dissecting a job board. Because it stayed honest, it handed me the thread on the first pull.

That is the exact experiment I wrote the tool to run. And it passed.

## What the morning actually taught me

The recruiter was never the point. The shape of the morning was.

I didn't solve this with one brilliant tool. I solved it with a chain of small, honest ones:digturned a name into an address sokilohad something to check;kilo's honest negative reframed the question socurlandopensslknew where to look. And every one of them spokestable JSON— so I was consumingcontracts, not parsing prose. Exit codes matter. Schemas matter. Failure stays legible.

That's the manifesto I keep coming back to as I build these things:contracts, not vibes.When I pipekilo check --jsonintojq, I'm having a typed conversation with reality. I can't hallucinate a verdict, because the verdict arrives as a signed struct with its provenance stapled on.

It's the difference between a tool that sounds right and one that is right:

A gut feeling is an opinion. A sharp, composable, honest toolbelt is a witness.

And witnesses — unlike hunches — can say the three most valuable words in this whole trade:"I don't know."Then go find out.

Steal the pattern if it's useful:

1. Small, single-purpose tools that speak stable JSONcompose into something no chatty do-everything API can match.
2. Honesty beats confidence.A tool that returnsunknownunder pressure is worth ten that guess to please you.
3. Let the negatives navigate.The most useful result of the entire morning was a0.0.

So the next time a link makes your gut twitch, don't argue with the vibe. Resolve it, and ask a tool that's allowed to say nothing.

kilodidn't catch a scam — there wasn't one, just spam in a lab coat. It did something I value more: it told me the truth about what it knew, drew a hard line around what it didn't, and pointed me at where the real answer was hiding.

I built a 12MB binary to say"not observed"without flinching, on the exact morning I most wanted it to lie. It didn't. That's the whole experiment. That's why I built it.

kilo check <your-suspicions-here> 
--json

Enter fullscreen mode

Exit fullscreen mode

Tooling in this piece:KiloCheck· the eternaldig/openssl/curl. The story is real; the identifying details have been filed off.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse