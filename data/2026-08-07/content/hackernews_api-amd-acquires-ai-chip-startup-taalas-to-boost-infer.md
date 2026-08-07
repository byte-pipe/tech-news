---
title: AMD acquires AI chip startup Taalas to boost inference performance by etching models into silicon
url: https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344
site_name: hackernews_api
content_file: hackernews_api-amd-acquires-ai-chip-startup-taalas-to-boost-infer
fetched_at: '2026-08-07T00:41:30.850822'
original_url: https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344
author: itvision
date: '2026-08-06'
published_date: '2026-08-06T20:05:00.000Z'
description: Early tech demos show model-specific integrated circuits churning out up to 17,000 tokens a second
tags:
- hackernews
- trending
---

AI and ML

 

# AMD acquires AI chip startup Taalas to boost inference performance by etching models into silicon

Early tech demos show model-specific integrated circuits churning out up to 17,000 tokens a second

Tobias Mann

Tobias

Mann

SYSTEMS EDITOR

Published

thu 6 Aug 2026 // 21:05 UTC

In AMD’s latest bid to upset Nvidia's dominance in AI hardware, the House of Zen has acquired AI chip company Taalas, which bakes model weights directly into silicon in a process that promises to boost inference performance by an order of magnitude or more.

The deal, announced at market close on Thursday, appears to be framed in much the same context as Nvidia’s $20 billionlicensing dealwith Groq last December: make high-performance “premium” inference services prized for AI agents, like code assistants, faster and cheaper to run. AMD didn’t disclose the terms of the deal, but from what we understand, this is an actual acquisition rather than an acquihire.

Founded in 2023 and based in Toronto, Taalas’ approach to inference is radically different from conventional GPUs or the dataflow architectures that underpin Groq LPUs or Cerebras' waferscale accelerators.

REG AD

### A model-specific integrated circuit

REG AD

The startup’s chips don’t rely on HBM to store the model weights but rather etch them directly into the silicon. In a sense, Taalas’ chips are really model-specific integrated circuits or MSICs.

Perhaps more importantly, Taalas’ tech isn’t just conceptual. In February, the startuprevealedits first test chip fabbed on TSMC’s 6nm process tech, which it called the HC1. Initial benchmarks saw the chip serve Meta’s Llama 3.1 8B at a blistering 16,960 tokens a second — when announced last February, that was 48x faster than Nvidia's GPUs and 8.5x faster than Cerebras' accelerators.

While Llama 3.1 is ancient by today’s standards, having made its debut all the way back in mid 2024, the reticle-sized chip was really intended to prove the concept.

Taalas has been incredibly secretive about how its chips actually work, but we know its processors are comprised of two main regions: the mask-ROM recall fabric where model weights are etched, and the SRAM recall fabric where KV caches and fine-tuning adapters are stored.

For its second-gen HC2 chip due out this summer, Taalas aims to boost parameter count to 20 billion parameters. That might not sound like much, but just like with GPUs for larger models, weights are simply distributed across multiple accelerators using pipeline parallelism.

At 20 billion parameters per chip, you’d need just 50 accelerators to support a trillion-parameter model, and AMD just so happens to have a rack-scale compute platform and in-house system design team that can comfortably accommodate that.

That’s quite a bit more space and power efficient than Nvidia’s recently unveiled LPX systems, which would need a few dozen GPUs and at least2,000 Groq LPUsto serve the same model.

From what we understand, AMD intends to pair its Instinct-basedHelios rackswith chips based on Taalas’ tech, which implies a disaggregated architecture where compute-heavy prompt processing is done on GPUs while token generation is offloaded to Taalas-based accelerators.

REG AD

It’s also possible that AMD could adopt a sort of tick-tock cadence in which customers initially deploy and validate models on Instinct accelerators and, once they’re satisfied with them, transition to Taalas accelerators. We can only speculate at this point, but here’s what AMD’s SVP of AI, Vamsi Boppana, had to say about it in a canned statement:

“AMD is building a full-stack AI platform that gives customers the flexibility to deploy the right compute solutions for every AI workload."

### You better really love that model

While the tech is blazing fast, if you hadn’t already figured it out, it comes with a pretty substantial downside. Once the chips are deployed you’re stuck with that model. Any change bigger than something like a LoRA adapter is going to require a re-spin of the chips, which is not only expensive but time-consuming.

Nearly four years into the AI boom, new models are rolling out on a nearly monthly basis. In order to benefit from Taalas’ tech, AMD’s customers are going to have to be really sure about their choice of models, which will be easier for some than others.

However, if the startup is to be believed, the situation isn’t quite as bad as it sounds. While new models will require a re-spin, it doesn’t require starting over from scratch. Instead, just two layers of metal need to be changed, which is a lot cheaper and less time-consuming.

## MORE CONTEXT

* ### Elon pledges to give Nvidia a virtual monopoly over the stars
* ### AMD's AI eggs are in too few baskets, Wall Street worries
* ### China turns up the heat with open model blitz as US model makers panic
* ### A deep dive into Nvidia's Vera CPU and the Olympus cores that power it

With that said, we strongly suspect this tech will largely be deployed by AI model devs, their infrastructure providers, and a handful of inference providers. In an interview with our sibling siteThe Next Platformin February, the company suggested that etching a model's weights into silicon is 100x less expensive than training a frontier model.

AMD is certainly in a position to negotiate those deals. OpenAI, Anthropic, and Meta are all major Instinct customers. Given the close working relationship between the model houses and the chip designer, it wouldn't be surprising to see a GPT or Claude deployed on a combination of Taalas and instinct accelerators.

REG AD

The tech also has implications for model development. One of the ways developers have cut down on hallucinations is by trading time for accuracy. The technique, called test-time scaling, is quite simple in practice, and involves allowing a model to “think” for longer before responding.

One drawback of test-time scaling is that it consumes substantially more tokens, which makes it expensive, and means users have to wait longer for the chatbot, code assistant, or agent to respond. If AMD’s Taalas buy can drive down the cost per token and boost output speeds by 10x or 20x, model devs may opt to extend the reasoning time even further.

In any case, we may not have to wait long to see just how Taalas fits into AMD’s broader vision. Subject to regulatory approval, the deal is expected to close in the fourth quarter. ®

gpu

nvidia

amd

ai

semiconductor

systems

cloud infrastructure month 2026

REG AD

AI and ML

## How the famed USENIX Security conf is managing a flood of papers in the AI era

AI usage is evident but isn't yet a serious problem

AI and ML

## AMD acquires AI chip startup Taalas to boost inference performance by etching models into silicon

Early tech demos show model-specific integrated circuits churning out up to 17,000 tokens a second

devops

## Platform Engineering 2.0: your platform was built for a different era. AI just exposed it

PARTNER CONTENT: Platform engineering won the argument. Now it has to grow up fast and evolve for the AI era.

AI and ML

## AI struggles to patch vulns without adult supervision

Left alone, autonomous fixes often fail to fully remediate flaws

COLUMNISTS

## Adding an API to networking hardware doesn’t solve management challenges

This is why cloud-inspired networks win: virtual switches are all consistent

devops

## Latest GitHub outage squeezes Actions, Pages to death

Look over there, Copilot - it's a beautiful AI farm where you can tend some digital rabbits

### MOST POPULAR

* Security#### London cops handed victim's new address and number to her stalker, watchdog says
* saas#### Double trouble for Microsoft as pre-owned software license claims converge
* offbeat#### New Boeing finally gets going, 15 years after debut
* SECURITY#### IT department put sticky notes on the laptops to help employees log in
* AI AND ML#### Microsoft tells engineers to curb their token-burning enthusiasm

### AI

* AI and ML#### How the famed USENIX Security conf is managing a flood of papers in the AI eraAI usage is evident but isn't yet a serious problem
* AI and ML#### AMD acquires AI chip startup Taalas to boost inference performance by etching models into siliconEarly tech demos show model-specific integrated circuits churning out up to 17,000 tokens a second
* AI and ML#### AI struggles to patch vulns without adult supervisionLeft alone, autonomous fixes often fail to fully remediate flaws
* AI AND ML#### An off-grid AI sounds like a great survival assistant, but is better left to roleplaying the zombie apocalypseWould you rather play Russian roulette with an LLM or put your health and safety in the hands of a professional
* SYSTEMS#### Elon pledges to give Nvidia a virtual monopoly over the starsIn space, no one can hear you scream when the LLMs hallucinate

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### FOSS smashed one Microsoft monopoly. After 20 years of failure, it's time to smash anotherWord up
* #### GNOME can look like Windows – and Flashback can do it without extensionsNew 'Simple-taskbar' is an option, but there's a simpler, stabler way
* #### A moment of silence, please, for the final release of Debian on x86-32New Debian versions hit FOSSland in the form of 13.6 and 12.15
* #### Baddies caught exploiting extensions bugs with perfect 10 scores on vulnerable Joomla websitesFlaws in iCagenda, Balbooa Forms extensions can impact open source CMS that powers a million sites worldwide
* #### Frame: A new X11 server – implemented directly in assemblyJoins yserver, Phoenix, and of course XLibre – and outlier Arcan
* #### Cinnamon 6.8 will support Wayland – if you want itNext version of Linux Mint’s desktop has both kinds of display server