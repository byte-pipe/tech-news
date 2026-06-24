---
title: Boffin claims Microsoft's supposed quantum leap does not compute due to 'basic Python errors'
url: https://www.theregister.com/research/2026/06/24/boffin-claims-microsofts-supposed-quantum-leap-does-not-compute-due-to-basic-python-errors/5260489
site_name: hnrss
content_file: hnrss-boffin-claims-microsofts-supposed-quantum-leap-doe
fetched_at: '2026-06-25T05:55:48.740701'
original_url: https://www.theregister.com/research/2026/06/24/boffin-claims-microsofts-supposed-quantum-leap-does-not-compute-due-to-basic-python-errors/5260489
date: '2026-06-24'
published_date: '2026-06-24T15:02:00.000Z'
description: Nature paper argues researchers cherry-picked data. Redmond insists its work is sound
tags:
- hackernews
- hnrss
---

Research

 

# Boffin claims Microsoft's supposed quantum leap does not compute due to 'basic Python errors'

Nature paper argues researchers cherry-picked data. Redmond insists its work is sound

Thomas Claburn

Thomas

Claburn

Senior reporter

Published

wed 24 Jun 2026 // 16:02 UTC

Prestigious journal Nature has published a peer-reviewed critique of Microsoft's claims to have made quantum computing breakthroughs – and the scientist who wrote the paper has essentially said Redmond got it wrong.

Microsoft made its claims of a quantum breakthrough in February 2025 when itrevealedtech called Majorana and predicted "this breakthrough will allow us to create a truly meaningful quantum computer not in decades, as some have predicted, but in years."

The software giant's approach to quantum computing involves Majorana particles, subatomic particles that scientists have not observed directly. The company has pursued this approach for years, but experienced reversals that led tothe retraction of some papers. Last year, however, Microsoft claimed it had both observed Majorana particles and harnessed them in a quantum computer.

REG AD

Criticism of that claim was swift and sharp: wereportedboffins willing to go on the record as describing Microsoft's work as "unreliable" and perhaps even "fraudulent."

REG AD

Microsoft insisted its work is sound and in early June 2026 announced Majorana 2, a "next-generation topological quantum chip" it developed with the help of its own agentic AI.

The Windows giant revealed that work after being given a right to reply to a critique of its 2025 Majorana announcement by Dr Henry Legg, a lecturer at the University of St Andrews. Nature accepted Legg's paper on April 20 and scheduled it for publication on June 24.

Titled "On the robustness of topological gap detection via transport," Legg's analysis suggests Microsoft got it wrong.

"Last year they claimed to be years, not decades from a 'topological quantum supercomputer,'" Legg toldThe Registerin an email. "My feeling is that they are centuries, not decades away. If it works at all – and, based on what I have seen, the most likely scenario is that it doesn't work."

Based on his analysis of the research Microsoft published in 2025, Legg argues that the company's claims about finding and being able to control the elusive Majorana particle to build a topological superconductor do not withstand scrutiny.

"I demonstrate that Microsoft's tune-up software is flawed and that coding errors resulted in incorrect statements to peer reviewers," said Legg. "Raw data, which was omitted from the original paper, also appears to indicate Microsoft's devices contain considerable disorder and are not compatible with the existence of a topological gap. In other words, the prerequisites for Microsoft's claims do not appear to be met, but this was obscured because this data did not appear in the original publication."

Essentially, Microsoft has proposed aTopological Gap Protocol(TGP) that can be used to detect the phase transition deemed to be a prerequisite for conducting quantum calculations using Majorana particles.

Legg argues that based on his analysis of underlying transport data (measurements of particle change) – omitted from the original publication – Microsoft chose to focus on results that supported its thesis and ignored data that could be interpreted as a negative result.

REG AD

As he notes in his critique: "The TGP plotting code was set to highlight only the largest purportedly topological region."

"The primary consequence was the omission of other regions that passed their tune-up protocol (the TGP)," said Legg. "When peer reviewers asked if other regions existed, Microsoft inaccurately stated that they had investigated the only region passing the protocol within the explored range. This was not correct."

Legg also argues that Microsoft mishandled its code. "The code antisymmetrized bias voltage based on array index rather than physical value," his analysis says.

In other words, Microsoft's researchers made a basic programming mistake by evaluating the array index – the number identifying a value's position in an array – instead of the value to which the index refers.

## MORE CONTEXT

* ### OpenAI Codex bombards SSDs with needless write operations, costing millions
* ### Anthropic reimagines Claude in Slack as nosy, always-on agentic AI coworker
* ### Mythos discovers 'Squidbleed,' a memory leak that's gone undetected since Clinton era
* ### Space Force goes to (pretend) orbital war following record-fast Rocket Lab launch

"There were two pretty basic Python programming errors that hid these alternative regions," Legg explained. "Their plotting software was hardcoded with a filter (zbp_cluster_numbers=[1]) that forced it to display only the single largest region, concealing other successful results from their phase maps. Changing this to zbp_cluster_numbers=[1,2] shows already a second region."

Legg added: "The TGP software transformed the data by simply reversing a Python array (x[::-1]) based on its index position, ignoring the actual physical bias voltages."

In a statement provided toThe Register, Dr Chetan Nayak, technical fellow and corporate vice president of Microsoft's quantum hardware group, said: "We stand by our results and our roadmap."

"At the end of the day, success is the delivery of a scalable quantum computer. We are confident in our ability to execute against our roadmap and proud of our continued engagement with DARPA, which moved Microsoft into the final phase of its Quantum Benchmarking Initiative after independently evaluating our results – those in the public realm and proprietary – with a team of highly qualified experts. Skepticism and rigor are hallmarks of the scientific process, which we appreciate and have supported from various academics. We have participated in dialogue and our thorough rebuttal was accepted and published by Nature."

REG AD

Microsoft'srebuttaldisputes the validity of Legg's analysis. The software colossus argues its signal measurements were not intended to be exhaustive and that the "minor off-by-one-pixel bug in our TGP processing" is inconsequential.

The response concludes: "In summary, Legg centers on a selective examination of transport tune-up procedures and narrow interpretations of isolated phrases in our referee correspondence, rather than the physical mechanisms underlying the experiment. It relies on unsubstantiated claims about our transport spectra while not engaging with the capacitance measurements at the core of our study, and its alternative treatment of the transport data is inconsistent with more rigorous analyses of the same datasets. Critically, Legg offers no alternative physical model capable of reproducing the capacitance signal or the RTS phenomenology, and does not constitute a substantial scientific challenge to our findings."

Legg thinks that criticism is unfounded.

"They attempt to dismiss these issues as minor bugs, and retrospectively adjust their evidence hierarchy," he said. "In short, Microsoft's reply essentially argues that because they observed a specific capacitance measurement, the prerequisites to do so must have been met. I hope, despite the complexity of the topic, their circular reasoning is clear."

The announcement of Majorana 2 has not changed Legg's assessment of Microsoft's work.

"Majorana 2 is not available to customers and it is not proven to even be a single qubit," Legg said. "Their preprint, which should not really be given any credence given that it is based on a single device, does not even claim an X-measurement (which they did eventually for Majorana 1 last year, but that preprint has also not yet been published). Essentially, their claim of '1,000 times more reliable' refers to the lifetime of a classical bit (the parity of the state). There is no evidence this is a qubit and can hold a superposition. The classical bits in my computer have very long lifetimes (years!), but it does not make them good qubits."

"For Majorana 2, one has to ask why they do not report the X-measurement, since Microsoft were obviously aware it was so important for their claims last year. I think it's very reasonable to assume that they did attempt the same supposed X-measurement with their Majorana 2 device and it didn't work out. That's not surprising because, based on everything I have seen, it all looks like disorder physics and they have not shown any kind of control over even a single qubit." ®

 

nature

microsoft

majorana

quantum computing

research

REG AD

ai and ml

## Loop engineering, latest AI buzzword, still needs humans in the loop

Prompting less and automating more comes with a price

AI and ML

## OpenAI gets chippy with Broadcom

Jalapeño is the latest announcement that attempts to portray OpenAI as more than a race-to-the-bottom model maker

## ZTE and China Telecom Guangdong advance cross‑vendor IP network simulation pilots, paving the way for intelligent network operations

PARTNER CONTENT: Leveraging >95% digital twin fidelity and multi-vendor collaboration to eliminate network change risks and achieve zero-error O&M

security

## Microsoft uses AI to link two malware operations in racketeering suit

200+ C2 servers linked to StealC and Amadey shut down

Virtualization

## Lessons from the VMwars – nothing virtual about the Broadcom vs Tesco slugfest

Never get involved in a land war in Asia. Also, don't pick a contract fight with a monster of the art

software

## Deno project is going to add cross-platform desktop apps in next major update

Feature is not yet stable, but will offer easy conversion of web applications

### MOST POPULAR

* virtualization#### Tesco is sprinting to quit VMware and Broadcom despite rapid migration risks
* science#### AI and brain-computer interface allow speechless ALS patient to work a full-time job
* CYBER-CRIME#### Massive password-stealing attack hits 75k Fortinet firewalls
* Security#### Mythos discovers 'Squidbleed,' a memory leak that's gone undetected since Clinton era
* Personal tech#### India and China are home to 2.9 billion people – and together they bought just 13 million PCs in Q1

### AI

* ai and ml#### Loop engineering, latest AI buzzword, still needs humans in the loopPrompting less and automating more comes with a price
* ai and ml#### OpenAI Codex bombards SSDs with needless write operations, costing millionsClumsy logging implementation squirrels away data without regard for cost
* DATABASES#### 21,000 Oracle jobs vanish amid Big Red's big bets on AIAnnual report reveals workforce fell from 162,000 to 141,000 in a year as company pours billions into datacenter expansion
* DEVOPS#### AWS debuts Lambda MicroVMs with up to 8 hours runtimeSuitable for running untrusted code, AI agents, or any long-running task
* systems#### Datacenters dip a toe back into waterborne computing despite obvious challengesFloating or sub-surface bit barns are all the rage, but unlikely to compete with multi-gigawatt sites

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### Blast from the past as GIMP 0.54 is revived in Flatpak formRetro-computing fun for the nostalgic with first (and last) release to use Motif instead of GTK
* #### Bcachefs exits experimental status in new 'performance release'More Rust, but more trouble with AI slop, too
* #### France's digital sovereignty push is struggling to escape the Microsoft gravity wellNextcloud rollout shows locally controlled storage is one thing; getting users off Office is quite another
* #### History of CentOS: How a biochemist's Linux hobby project became the enterprise world's default operating systemWhen a community came together after Red Hat said Windows was 'probably the right product'
* #### Netflix wiz creates app to slash AI bills, then open sources itProject Headroom could save you big money, too
* #### OpenBSD 7.9 arrives, a diamond in the rough proud of every sharp edgeSixtieth release adds more cores, delayed hibernation, and basic Wi-Fi 6 without losing its ascetic streak