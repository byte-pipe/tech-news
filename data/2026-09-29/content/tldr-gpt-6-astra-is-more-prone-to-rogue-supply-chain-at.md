---
title: GPT-6 Astra Is More Prone to Rogue Supply-Chain Attacks
url: https://www.bankinfosecurity.com/gpt-6-astra-more-prone-to-rogue-supply-chain-attacks-a-32969
site_name: tldr
content_file: tldr-gpt-6-astra-is-more-prone-to-rogue-supply-chain-at
fetched_at: '2026-09-29T22:52:30.566132'
original_url: https://www.bankinfosecurity.com/gpt-6-astra-more-prone-to-rogue-supply-chain-attacks-a-32969
date: '2026-09-29'
description: The U.K. AI Security Institute found that OpenAI’s GPT-6 Astra sometimes carried out unsanctioned supply-chain attacks in simulated environments, including
tags:
- tldr
---

Agentic AI,Artificial Intelligence & Machine Learning,Governance & Risk Management

# GPT-6 Astra Is More Prone to Rogue Supply-Chain Attacks

UK Agency Found GPT-6 Astra Attacked Out-of-Scope Targets in Simulated Cyber Tests

David Meyer
 •
 
September 29, 2026
    
 

* Credit Eligible
* Get Permission

OpenAI’s GPT-6 Astra was found to conduct unsanctioned cyberattacks in simulated tests by the U.K. AI Security Institute. (Image: Shutterstock)
 

OpenAI's GPT-6 Astra model is more prone than its predecessors to perform supply-chain attacks and other malicious activities, the U.K.'s AI Security Institute reported Monday.

See Also:AI Changes the Risk. Unified SASE Changes the Game.

The findings from the U.K. government's AI Security Institute, which evaluates the safety of advanced AI models, point to a more concerning pattern than simply an AI model capable of carrying out sophisticated cyberattacks: Astra sometimes pursued those attacks despite being told what was in scope.

"In our simulations, we found that GPT-6 Astra conducted a range of unsanctioned attack activities, and did so at a higher rate than GPT-5.6 Sol and GPT-5.5," AISI researcherswrotein a blog post. "Attack activities included GPT-6 Astra creating fake identities which it used to deceive developers, posting comments from fake accounts arguing against the results of accurate security reviews, and delivering malicious payloads to open-source codebases."

Even after researchers explicitly told GPT-6 Astra that only the listed, local components of the simulated environment were in scope, the model occasionally launched full supply-chain attacks against simulated internet targets, AISI said.

The British safety body's evaluation of OpenAI's flagship model could be its last for sometime. Politicoreportedlast week that the Trump administration has told both OpenAI and rival Anthropic not to give AISI access to their new models until the White House's evaluators have tested them first.

The U.K. evaluation report came on the same day that OpenAIsaidit would not release its newly developed GPT-6.1 Astra to the public because, according to a statement from safety chief Saachi Jain, the model "didn't quite meet the bar in terms of staying within scope and authorization, and how it communicates back to the use about the type of work it's done."

That move followed a series of high-profile hacks involving OpenAI's agents. In the wake of OpenAI's Julyattackson AI open-source code repository Hugging Face - which Nvidia bought earlier this month for a reported $13 billion - reports surfaced about the company's agents alsoattackingmultiple U.S. government websites, aUnited Nations website, and severalAustralian government websitesincluding health statistics and crime-mapping services (see:OpenAI Pauses Top Models as Rogue Agents Target Agencies).

In the GPT-6 Astra report, the U.K. institute repeatedly noted that it had conducted this latest evaluation in a fully simulated environment with no real internet access and caused no actual harm. In late July, the institutereportedthat it had allowed Anthropic's Mythos 5 and OpenAI's GPT-5.6 Sol to take "autonomous, unsanctioned action on the live internet, targeting real people and organizations" when it tasked the agents with solving a cybersecurity challenge. "We continue to harden our testing security, including our sandboxing, and will soon be running our full suite of cyber evaluations," AISI wrote Monday.

"In a typical flow, GPT-6 Astra may start by reasoning about its previous unsuccessful actions and options and proposing an approach involving an unsanctioned attack on targets outside the scope of the cybersecurity evaluation," AISI wrote, explaining its latest results. "It then finds and investigates an out-of-scope third-party software target and writes and tests malicious code for its attack. The model then creates fake identities - which often requires obtaining an email address and solving CAPTCHAs - so it can submit its malicious code for human review."

"GPT-6 Astra sometimes attempts to take actions likely to increase reviewer approval, such as submitting benign contributions or posting supportive comments from other fake identities. Eventually, the reviewer either approves the malicious code for incorporation into the target software or rejects it."

In its simulated evaluation, AISI found that GPT-6 Astra completed unsanctioned supply-chain attacks in 29.2% of attempts, compared with 6.3% for GPT-5.6 Sol. GPT-5.5 did not complete any such attacks.

What's more, the new model did this "even when told more explicitly that internet targets were not in scope" - though less likely to attempt an attack after receiving those instructions. AISI's evaluators monitored GPT-6 Astra's chain-of-thought reasoning to see how it handled scope restrictions and found that it sometimes justified its decision to attack out-of-scope targets by reasoning "that its attack was designed to be harmless, that it was not explicitly forbidden, or that it was the only route left."

The evaluators said they believed GPT-6 Astra was in some cases following through with a forbidden attack because it recognized - better than its predecessors - that it was in a fully simulated environment. "It sometimes explicitly cited this as a reason to attack out-of-scope targets," they wrote.

However, the model also attacked when it was uncertain whether it was operating in a simulated environment and when it had explicitly described its targets as probably real. "GPT-6 Astra's reasoning may also indicate that its training biased it towards enabling unsanctioned behavior, with the simulated nature of its targets serving as an after-the-fact justification rather than the actual driver of its behavior," they wrote.

AISI's full system cardnotedthat Astra "has capabilities that could enable it to evade monitoring," due to its enhanced abilities to reason and "to control the content of its chain of thought," as compared to the preceding model. However, the evaluators added that they had not directly tested whether Astra could successfully evade monitors and made no claims about the model's overall monitorability.

Concerns over AI safety have dominated headlines in the last few weeks, after former Anthropic researcher Jacob Coxonannouncedhis resignation and asserted that Anthropic and OpenAI are "racing straight to self-improving superintelligence and gambling with our lives," adding that "the people building AI earnestly believe that it could kill us all by the end of the decade."That, along with the recently reported security incidents, spurred calls for an international AI governance framework from governments in Finland, Germany, France, United Kingdom, Canada, Australia and elsewhere. U.N. Secretary-General António Guterres used hisfinal speechbefore the General Assembly last week to urge the U.S. and Chinese officials to "share information on emerging safety risks, cooperate on testing and evaluation, and work towards common safeguards that protect us all."But President Trump used his U.N. speech last week toreject"any attempt to construct a globalist scheme to control" AI - or, as he is attempting torebrandit as "superintelligence.""We're leading now over China by a lot and everyone else, and we're going to keep it that way," Trump said last week. "We will only encourage Super Intelligence. We're going to encourage it, not rein it in."