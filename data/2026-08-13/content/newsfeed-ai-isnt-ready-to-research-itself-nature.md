---
title: AI isn’t ready to research itself | Nature
url: https://www.nature.com/articles/d41586-026-02494-5
site_name: newsfeed
content_file: newsfeed-ai-isnt-ready-to-research-itself-nature
fetched_at: '2026-08-13T19:56:44.291725'
original_url: https://www.nature.com/articles/d41586-026-02494-5
date: '2026-08-13'
description: An agentic system successfully developed concepts from two computer-science papers — but the original authors were not impressed.
tags:
- nature
---

* Email
* Bluesky
* Facebook
* LinkedIn
* Reddit
* Whatsapp
* X

Save article

View saved research

 

One of the earliest applications of ‘AI scientists’ was to research AI itself.Credit: La Pico de Gallo/Getty

Artificial intelligence has made leaps in AI research itself, finding ways to make existing algorithms smarter — or writing new ones. But computers are not yet ready to replace their makers, according to a study posted on the preprint server arXiv1in late July.

“I don’t think full automation of open-ended research is on the horizon right now,” says Sayash Kapoor, a computer scientist at Princeton University in New Jersey and a co-author of the preprint.

The effort to fully automate the scientific process, from idea generation to the writing and self-evaluation of a paper, was pioneered by a team mostly from the firm Sakana AI in Tokyo. The teamunveiled their system, called The AI Scientist, in 2024, and laterpublished resultsfrom an improved version in March inNature2.

The AI Scientist was tasked with studying pitfalls in machine learning. Three of the papers it produced were submitted for peer review at a conference workshop, and one achieved a score high enough for acceptance. But, according to Kapoor, peer review is an unreliable way of assessing the quality of a paper, especially in AI research.

More generally, some researchers have questioned whether automating AI research from idea creation to publication can produce true breakthroughs yet, suggesting it is better at optimizing existing techniques.

To hold AI to a higher standard than peer review, Kapoor and his colleagues created a new challenge, called shadow evaluation. First, they picked two papers that had been submitted to this year’s Neural Information Processing Systems conference. Then they asked an AI tool to do research and write papers based on a research question from each paper, and asked the original authors to scrutinize its output. The idea was that these authors would have more of the expertise and dedication to dig into the output than a harried peer reviewer would.

The team built its AI system by ‘harnessing’ the large language model Claude Opus 4.8 in a modified version of the agentic system OpenClaw, and then wrapped that in a broader ‘scaffold’ that contained general instructions and ways to check progress. The harness gave the model an array of tools, including the ability to create sub-agents and to access the Internet, software libraries, computer processors for running experiments and software that simulates peer review. For each paper, the AI system had six days and US$3,000 in computing credits. Following the general research direction of the first paper, Kapoor’s team asked the system to design a method for the precise control of chatbot personality. Mirroring the second paper, it had to design a failure detector for a certain kind of neural network.

The authors were surprised by the system’s success at the engineering work of its research. It could run hundreds of experiments over several days, without getting stuck in a loop of unresolvable errors. And it performed solid literature reviews and made some minor findings. It also caught its own false claims (sometimes called hallucinations) and did not try to cut corners (or ‘reward hack’), despite the authors’ predictions.

## Poor marks

But the AI system mostly failed at its two assigned tasks, earning overall scores of 2/6 and 1/6 from the original papers’ authors. A typical way in which it would fail was to select a few hypotheses to explore, but settle too early on one and not backtrack sufficiently when its approach wasn’t working. Subsequent self-review wasn’t sufficiently negative, so the system persisted on its initial choices, whittling down its claims until it said little of interest.

## Enjoying our latest content?Log in or create an account to continue

* Access the most recent journalism from Nature's award-winning team
* Explore the latest features & opinion covering groundbreaking research

Access through your institution

or

Sign in or create an account

Continue with Google

Continue with ORCiD

doi: https://doi.org/10.1038/d41586-026-02494-5

## References

1. Kirgis, P.et al.Preprint at arXivhttps://doi.org/10.48550/arXiv.2607.27191(2026).
2. Lu, C.et al.Nature651, 914–919 (2026).ArticlePubMedGoogle Scholar

Download references

Reprints and permissions

## Related Articles

* Teams of AI agents boost speed of research
* AI ‘scientists’ joined these research teams: here’s what happened
* How to build an AI scientist: first peer-reviewed paper spills the secrets
* Which ‘AI scientist’ suits your lab? A guide for the perplexed

## Subjects

* Machine learning
* Computer science

## Latest on:

* Machine learning
* Computer science

* Can Anthropic’s invisible watermarks curb ‘AI slop’? Researchers remain scepticalNews13 AUG 26
* AI tools speed up analysis, but scientific truths must be grounded in realityCorrespondence11 AUG 26
* Learning millisecond protein dynamics from what is missing in NMR spectraArticle10 AUG 26

* Can Anthropic’s invisible watermarks curb ‘AI slop’? Researchers remain scepticalNews13 AUG 26
* Scientists using LLMs will ‘do more, less well’, modelling study predictsNews31 JUL 26
* Underdog ‘spin qubits’ leap forward in race to a useful quantum computerNews29 JUL 26

### Jobs

* #### Open Rank Faculty Positions (Assistant, Associate, Full Professor) in Emerging Pathogen ResearchCleveland, Ohio (US)Cleveland Clinic
* #### Open Rank Faculty Positions (Assistant, Associate, Full Professor) in Antimicrobial ResistanceCleveland, Ohio (US)Cleveland Clinic
* #### Multiple Faculty and Postdoctoral Positions in Ultrasound Medicine and EngineeringSeeking global talents at all levels (Distinguished, Leading, Young Scholars, Postdocs).Chongqing (CN)State Key Laboratory of Ultrasound in Medicine and Engineering, Chongqing Medical University.
* #### Postdoctoral ResearcherPostdoctoral Researcher to investigate the neural circuit mechanisms underlying individual differences in stress vulnerability and resilience.New York City, New York (US)Anacker Lab
* #### UTSW OBI Scholars – Assistant Professor or Associate ProfessorOBI Scholars seeks exceptional early-career scientists studying mechanisms of nervous system disease for faculty positions with ~$3M in support.Dallas, Texas (US)UT Southwestern Medical Center