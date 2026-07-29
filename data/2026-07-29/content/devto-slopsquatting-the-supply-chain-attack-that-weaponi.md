---
title: 'Slopsquatting: The Supply Chain Attack That Weaponizes AI Hallucinations - DEV Community'
url: https://dev.to/nazar-boyko/slopsquatting-the-supply-chain-attack-that-weaponizes-ai-hallucinations-2m2
site_name: devto
content_file: devto-slopsquatting-the-supply-chain-attack-that-weaponi
fetched_at: '2026-07-29T12:28:30.309456'
original_url: https://dev.to/nazar-boyko/slopsquatting-the-supply-chain-attack-that-weaponizes-ai-hallucinations-2m2
author: Nazar Boyko
date: '2026-07-28'
description: Typosquatting bets on your typo. Slopsquatting bets on your AI assistant. When a model invents a... Tagged with security, ai, webdev, programming.
tags: '#security, #ai, #webdev, #programming'
---

Coined by Python's Seth Larson in 2025

Typosquatting bets on your typo. Slopsquatting bets on your AI assistant. When a model invents a package that doesn't exist, an attacker registers the name and waits for install to run. Here's the kill chain, why your usual defenses miss it, and what actually stops it across npm, Composer, and pip.

Imagine a coding assistant just told you to run this:

pip 
install 
requests-oauth2-helper

Enter fullscreen mode

Exit fullscreen mode

It looks right. You asked for a clean way to attach OAuth2 tokens to yourrequestscalls, and the name reads exactly like a package that would do that. The casing is idiomatic, the hyphenation matches the ecosystem, it sounds like fifty other real PyPI helpers. So you run it. Tests pass. You move on.

The problem is thatrequests-oauth2-helpernever existed when the model learned to suggest it. The model made it up. And if an attacker was paying attention, that name isn't empty anymore.

That'sslopsquatting: a supply chain attack that swaps the human typo at the heart of typosquatting for a machine hallucination. The term was coined bySeth Larson, Developer-in-Residence at the Python Software Foundation, and popularized by Andrew Nesbitt of Ecosyste.ms in 2025. It's a small idea with a nasty consequence: you don't have to fat-fingerreqeustsanymore. Your AI will confidently hand you a fake package with a straight face, and you'll trust it more than your own typo.

## Typosquatting needed your mistake. This one doesn't.

Typosquatting is old. You registerexpresnext toexpress,python-dateutlnext topython-dateutil, and you wait for someone's fingers to slip. It works, but it's a numbers game with thin odds. Most people spellexpresscorrectly. The attacker is fishing for the fraction of a percent who don't.

Slopsquatting removes that dependency on human error entirely. The developer types the name correctly, character for character, because they're copying it from a source they trust more than themselves right now: the assistant that just wrote the surrounding code. The mistake was already made upstream, by the model, and the human is faithfully reproducing it.

Here's the shift that matters. In typosquatting, the attacker guesses at what your fingers might slip into. In slopsquatting, the attacker doesn't guess at all. They read what the model actually outputs, at scale, and register the names that come up. The model is doing the target selection for them.

## Why this works: hallucinations are frequent, and worse, they repeat

If model hallucinations were rare and random, slopsquatting would be a footnote. Register a fake name, wait forever, catch nobody. The reason this is a real threat is that neither of those things is true.

The scale first. A USENIX Security 2025 study,We Have a Package for You!, generated 576,000 code samples across 16 LLMs in Python and JavaScript and checked every package the models recommended.19.7% of recommended packages didn't exist.That's not a rounding error at the edge of a benchmark. That's one in five. The study logged 205,474 distinct hallucinated package names. Commercial models were better behaved (at least 5.2% on average) and open-source models worse (at least 21.7%), but nobody was clean.

The scale would still be manageable if every hallucination were a unique snowflake, because an attacker can't register two hundred thousand names and would have no idea which ones anyone will ever see again. The killer finding is that hallucinations arereproducible. The researchers took 500 prompts that had produced a fake package and ran each one ten more times. 43% of the hallucinated packages came backevery single time. 58% showed up in more than one run. Only 39% never reappeared.

Sit with that. Nearly half of these fabrications are stable model behavior, not noise. That flips the economics completely. An attacker doesn't need to register everything. They mine model output, keep the names that recur, and register the sticky ones. The reproducibility is the reconnaissance. The model tells them, over and over, exactly which fake name a future developer is most likely to be handed.

WarningThe names don't even have to look like real packages. Using Levenshtein distance, the same study found only 13% of hallucinated names were simple typos of real ones. About 38% had moderate similarity, and nearly half were highly dissimilar: fully fabricated, but still believable in the context of the code around them. That last bucket is the one that walks straight past typosquat detection, and we'll come back to why.

## The kill chain, one step at a time

None of this is theoretical. It's a clean, repeatable sequence, and every link is something you've watched happen in a normal workday.

1. The model suggests an import.You ask for a feature. The assistant writes the code and reaches for a dependency that fits the shape of the problem. It emits a name. The name is invented, but it's grammatical: right ecosystem conventions, right casing, right "sounds like a thing that exists" energy.

2. You trust it because the name fits.This is the load-bearing step, and it's psychological, not technical. Confident AI output slides past your guard the same way a confident senior engineer's PR does. The name is idiomatic. Nothing about it pattern-matches to "danger." You're reviewing the logic, not auditing whether a four-word package name is real, because who does that?

3. The install runs code.On npm and pip, installing a package can execute a script automatically: apostinstallhook, asetup.pybuild step. The attacker's payload doesn't need you to import anything or call a function.installfinished, so the code already ran.

4. Credentials leave the building.The payload reads what a build agent always has lying around: environment variables,~/.aws/credentials,~/.npmrctokens, aGITHUB_TOKEN,.envfiles. It POSTs them to an attacker-controlled endpoint. From the outside it looks like a package fetching metadata during install. From the inside, your CI just handed a stranger the keys.

The whole thing is unnervingly quiet. There's no exploit, no CVE, no clever memory corruption. A developer trusted a name and ran the standard install command they run fifty times a day. That's the entire attack.

And it's not hypothetical that people fall for the trust step. Security researcher Bar Lanyado at Lasso Security noticed models repeatedly hallucinating a Python package calledhuggingface-cli. He registeredan empty package under that exact name on PyPIas an experiment. Over the next three months it pulled more than 15,000 real downloads, and Alibaba's GraphTranslator project ended up recommendingpip install huggingface-cliin its README, when the real tool installs withpip install -U "huggingface_hub[cli]". Lanyado's package was harmless on purpose. A slopsquatter's wouldn't be.

## Same idea, four ecosystems, four different blast radii

The brief version is "it hits JavaScript, PHP, and Go alike." The accurate version is that each ecosystem hands the attacker a different amount of rope, and knowing the difference tells you where to spend your defense budget.

npm gives an attacker the most.Lifecycle scripts (preinstall,install,postinstall) run automatically onnpm install. That's the classic vector, and it's exactly why the ecosystem is finally moving. pnpm v10disabled dependency lifecycle scripts by defaultin early 2025, and npm followed:npm v12 turns off automatic script execution by default, announced in June 2026. Until you're on those versions,postinstallis a loaded gun pointed at your CI.

package.json (the malicious dependency)

{

 
"name"
:
 
"requests-oauth2-helper"
,

 
"version"
:
 
"1.0.3"
,

 
"scripts"
:
 
{

 
"postinstall"
:
 
"node ./collect.js"

 
}

}

Enter fullscreen mode

Exit fullscreen mode

pip is close behind.A source distribution runssetup.pyat install time to compute metadata and build, which means arbitrary code onpip install. A wheel (.whl) doesn't run install-time code the same way, which is why--only-binaryis a real hardening lever, not a nicety.

# Refuse source builds; only accept prebuilt wheels

pip 
install
 
--only-binary
 :all: requests-oauth2-helper

Enter fullscreen mode

Exit fullscreen mode

Composer is quietly the safest of the three, by design.Composer only executes scripts defined in therootpackage'scomposer.json. A dependency's ownscriptsblock is ignored. So a slopsquatted Composer package can't hand you an automaticpost-install-cmd, the way an npm package hands you apostinstall. The one caveat is plugins: a malicious Composerplugincan hook install events, which is whycomposer install --no-plugins --no-scriptsexists for untrusted trees. The payload has to wait until your code actually calls into it, which is a meaningfully higher bar than "runs on install."

Go doesn't have install scripts at all, so the kill chain shifts.go getandgo builddon't run a package's arbitrary setup code the moment you add it. The malicious code in a slopsquatted Go module runs the first time your program executes it, via a packageinit()function on import, or duringgo test. Later, but not never.

Go adds its own twist through the module proxy. Socket found abackdoored typosquat of BoltDB,github.com/boltdb-go/bolt, that was uploaded in November 2021, cached by the Go module mirror, and then had its Git tag rewritten to clean code. The proxy kept serving the cached malicious version anyway. It went undetected for over three years. Caching that's meant to make builds reproducible also makes a poisoned version durable.

So the mental model isn't "one attack, three languages." It's: npm and pip fire on install, Composer waits for a plugin or a call, Go waits for execution and then remembers the bad version forever. A slopsquatter picks the ecosystem that gives them the earliest, quietest trigger.

## Why your usual supply chain defenses don't catch this

Here's the uncomfortable part. Most of the controls you already run were built for a different threat model, and slopsquatting slips through the seams between them.

Lockfiles only help after the first install.Apackage-lock.jsonorcomposer.lockpins exact versions and hashes so a dependency can't silently change under you. That's great for a package you already vet and lock. But slopsquatting attacks thefirstinstall of a brand-new name. There's nothing in the lockfile yet, because you've never installed this thing. The AI just suggested it thirty seconds ago. The lockfile faithfully records whatever malicious version you first pulled, and now it's pinned. Lockfiles protect continuity, not first contact.

Scanners look for known-bad, and this is never-seen.A vulnerability scanner or a malware feed matches against packages someone has already flagged. A slopsquatted package registered yesterday, targeting a hallucination that only started recurring this quarter, has no CVE, no advisory, no reputation, no history. It's clean by absence. The scanner isn't broken; it's answering a different question. "Is this a known threat?" is not "is this a real package a human chose."

Typosquat detection keys on edit distance, and half these names don't resemble anything.The standard defense against typosquatting measures string similarity: how many edits to turnexpresintoexpress? Flag the near-misses. But remember the Levenshtein finding, nearly half of hallucinated names werehighly dissimilarto any real package.requests-oauth2-helperisn't one edit away from a real thing. It's not a corruption of an existing name at all. It's a fresh invention that happens to sound plausible. There's no real neighbor to measure distance from, so the detector has nothing to trip on.

Put those three together and you see the shape of the gap. Every one of these defenses assumes the bad package either changed (lockfiles), was previously flagged (scanners), or mimics something real (typosquat detection). Slopsquatting is none of those. It's a genuinely new name, never seen, that doesn't resemble anything, chosen by a machine that sounds confident. The defenses aren't weak. They're aimed somewhere else.

## What actually works: don't let a name into the repo on faith

The good news is that the fix isn't exotic. It's the same instinct that should govern any dependency, applied to a source you've started over-trusting. You don't need a new product category. You need to stop treating an AI's package suggestion as a citation.

Verify the package exists and is maintained before it touches your machine.Before you install anything a model handed you, look it up. Does it exist on the registry? How many downloads, how many versions, when was the last release, who publishes it, is there a repo behind it that a human clearly maintains? A slopsquatted package is usually days old with a suspiciously round download count and no history. Thirty seconds of looking kills most of these.

# npm: does it exist, who owns it, how old is it?

npm view requests-oauth2-helper

# PyPI: check the project page, release history, and maintainers

pip index versions requests-oauth2-helper

Enter fullscreen mode

Exit fullscreen mode

If the first command 404s, the model didn't find you a hidden gem. It made one up.

Disable install scripts by default.This single control neuters the loudest version of the kill chain. Turn automatic execution off and let real build steps be an explicit exception, not the default:

:::tabsnpm

# Kill lifecycle scripts globally; allow-list the rare package that needs one

npm config 
set 
ignore-scripts 
true

Enter fullscreen mode

Exit fullscreen mode

pnpm

# pnpm v10+ blocks dependency scripts by default.

# Approve only the ones you actually trust:

pnpm approve-builds

Enter fullscreen mode

Exit fullscreen mode

pip

# Prefer prebuilt wheels so setup.py never runs at install time

pip 
install
 
--only-binary
 :all: <package>

Enter fullscreen mode

Exit fullscreen mode

composer

# Untrusted tree? No plugins, no scripts.

composer 
install
 
--no-plugins
 
--no-scripts

Enter fullscreen mode

Exit fullscreen mode

:::

Only about 2% of npm packages legitimately use install scripts, which is exactly why the ecosystem decided the sane default is off. You lose almost nothing and you close the door the payload was counting on.

Proxy everything through a private registry with an allowlist.A build agent should not be able to reach out to the public registry and pull whatever a model named. Put a proxy in front (Artifactory, Verdaccio, a private PyPI, Composer's Satis) and allow only packages that have been reviewed in. Now a hallucinated name doesn't failafterinstall, it failsbefore, because it was never approved. This is the control that scales, because it moves the decision from "did the developer notice" to "is this on the list."

Add a maturity delay for new versions.pnpm v11 shippedminimumReleaseAge, defaulting to 1440 minutes (24 hours), which refuses to install a package version until it's been public long enough for the community to catch obvious malware. A slopsquatted package racing to catch a fresh hallucination is exactly the thing a cooling-off window is good at stopping.

And the one rule under all the others: never let a dependency into the repo just because the AI suggested it.An AI package suggestion is a hypothesis, not a source. Treat it the way you'd treat a Stack Overflow answer from an account you've never seen: possibly right, worth checking, never trusted on sight. The whole attack hinges on that one moment of misplaced trust in step two. Verify the name and the attack has nowhere to stand.

The uncomfortable truth is that the model isn't going to stop doing this soon. Hallucination is a property of how these systems generate text, and a fake package name reads exactly like a real one from the inside. So the burden sits with you: the human who runsinstall. The name your assistant just gave you might be a real library, or it might be an attacker's package wearing a real library's name. The only way to tell them apart is to look before you install, and the whole point of slopsquatting is that you won't.

P.S. Thanks for taking the time to read this article! The ideas and opinions expressed here are my own. English is not my first language, so I use AI to help correct grammar and make my writing clearer and easier to read. If anything still sounds a little awkward, I appreciate your understanding!

Originally published atnazarboyko.com.

Enjoyed this one? Let's stay in touch - I'm onLinkedIn, always happy to chat, swap ideas, or just say hi. 👋

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (20 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse