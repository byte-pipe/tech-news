---
title: AI co-scientists are revolutionizing how research is done | Nature
url: https://www.nature.com/articles/d41586-026-02931-5
site_name: newsfeed
content_file: newsfeed-ai-co-scientists-are-revolutionizing-how-research
fetched_at: '2026-09-21T16:50:38.404404'
original_url: https://www.nature.com/articles/d41586-026-02931-5
date: '2026-09-21'
description: Artificial-intelligence systems can generate hypotheses, design experiments and analyse data — but humans still need to decide what makes sense.
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

Illustration: The Project Twins

 

Biochemist Anna Pertl typed in her question, pressed Enter and left for the night.

The artificial-intelligence system that she had prompted is designed to produce innovative scientific hypotheses. But, unlike a typical chatbot, this AI tool — called Co-Scientist — doesn’t simply generate an answer in a single pass. It launches several autonomous AI systems, known as agents, to search for and synthesize information from papers, evaluate competing explanations, refine and critique hypotheses and iteratively test ideas against published evidence.

Why AI cannot do good science without humans

The process can involve vast quantities of computational power because agents pursue distinct lines of reasoning before converging on workable solutions. And that takes time. Long enough, Pertl jokes, for her to complete a long-distance triathlon, which she has done eight times since she started her PhD at the Whitehead Institute for Biomedical Research in Cambridge, Massachusetts.

On a rainy Tuesday in July, Pertl put the AI system to work on one of cancer’s most complicated problems. She asked Co-Scientist for non-obvious but practical ways of harnessingthe biology of molecular droplets known as condensatesto shut down MYC, a protein that runs amok in most cancers and haslong defied attack attempts.

The request built on years of research by Pertl’s supervisor, Whitehead biologist Richard Young. In 2018, Young and his colleagues found that cells switch on crucial genes by gathering regulatory proteins into condensates that cluster at important genome-control regions called super-enhancers1. They also worked out how cancer cells hijack these super-enhancers to send the gene encoding MYC into overdrive, a strong hint that condensates help to fuel the high expression rate of the protein2.

To Young, the obvious next step is to target the tumour cells’ condensates directly. Dewpoint Therapeutics in Boston, Massachusetts, a company that he co-founded, is now exploring that option. However, because previous attempts to subdue MYC failed, Pertl wanted to see whether AI could come up with a fresh line of attack.

Getting to an idea worth pursuing took some work. Pertl and Whitehead bioengineer Kalon Overholt spent close to an hour going back and forth with Co-Scientist before it understood the question. At first, the AI model assumed that the protein clusters at the centre of the research were meant to be the drug rather than the target. The tool also assumed that the clusters always activated gene expression, when in fact some do the opposite.

Once Pertl and Overholt had corrected these misconceptions, they set the system loose. By the next day, Co-Scientist had combed through more than 700 scientific papers and generated 108 possible strategies. It rejected all but one of the approaches as unworkable. The last strategy turned the laboratory’s thinking on its head.

Rather than dissolving the clusters — the method that Dewpoint is pursuing — the AI tool proposed gluing them together. Using a molecular linking technology calledclick chemistry, the approach smushes proteins that either activate or repress theMYCgene into one gooey mass, setting off a chain reaction untilMYC’s DNA can no longer be read.

Scientists already knew that DNA and the proteins surrounding it could turn from a loose liquid into something firmer, stiffening like gelatin in a refrigerator. But exploiting that transition to shut down a cancer gene was uncharted territory. “It’s extremely conceptually compelling,” says Overholt. “We had certainly never thought about anything like this.”

## Trust, but verify

This kind of AI-assisted brainstorming is becoming increasingly common. Researchers have already used Co-Scientist, developed by Google in Mountain View, California, to find a drug combination that kills leukaemia cells in a dish3and identify a treatment that, in the lab, regenerates liver tissue damaged by disease4.

And Co-Scientist isn’t theonly game in town. Frontier AI labs, including Anthropic and OpenAI, and start-ups such as FutureHouse5and Phylo6(all four based in or around San Francisco, California) are rolling out systems that can tackle tasks once reserved for human scientists, freeing researchers to focus on the most consequential questions and decisions. “We imagine it to be like a collaborator — a partner with you,” says Vivek Natarajan, an AI researcher at Google, who helped to develop Co-Scientist.

Teams of AI agents boost speed of research

That could change not just how scientists work, but also how they are valued. For generations, scientific progress has depended on researchers who could pose difficult questions, devise ways to answer them and make sense of the results. As machines take over more of that work, the scarce resource could end up being human scientific judgement: knowing which questions are worth asking and which lines of enquiry worth pursuing. “The most valuable part now is actually asking the question,” says Ajay Agrawal, an economist at the University of Toronto Rotman School of Management in Canada, who studies AI’s effects on innovation and entrepreneurship.

The goal, says Le Cong, a molecular geneticist at Stanford University in California and scientific co-founder of Phylo, is not to replace researchers but to free them from the routine aspects of discovery. “We’re trying to move humans up the value chain,” he says.

But the adoption of these AI tools also creates a troubling paradox. Researchers might need deeper knowledge than ever to judge whether an AI-generated idea is sound, even as students get fewer opportunities to build that expertise by doing the work themselves. The tools that promise to accelerate discovery could therefore make it harder to train the scientists needed to oversee them.

“Investigators with human skills that understand the full picture are going to be more valuable than ever,” concludes Hector Zenil, a biomedical computing researcher at King’s College London.

For Fyodor Urnov, who studies genome editing at the University of California, Berkeley, and was an early adopter of FutureHouse’s Kosmos platform, the promise of AI research assistants comes with a simple rule: don’t take their pronouncements on faith.

Urnov grew up in Moscow and remembers well a phrase popularized during the 1980s nuclear-arms-control negotiations between the United States and the Soviet Union. “My relationship with [Kosmos] is very much based on that Reagan–Gorbachev proverb,” he says: “Trust, but verify.”

Anna Pertl used Co-Scientist to look for ways to target the cancer-associated protein MYC.Credit: Anna Pertl

A verification step was built into a test of Google’s Co-Scientist by researchers at Imperial College London, who used the platform in 2025 while investigating how bacteria swap snippets of DNA across species7. They had already collected experimental data and formed a theory, but rather than feeding those into the system, they held the unpublished results back and asked the AI tool to work from the publicly available literature and data sets alone. Only after it had produced its theory did they reveal the experimental findings and compare the platform’s work with their own.

Co-Scientist’s theory of what was happening closely matched what the researchers, microbiologists José Penadés and Tiago Costa, had spent years working out: bacterial DNA elements can borrow parts of viruses to spread between distantly related hosts. Thanks to its ability to reason across and connect information from many sources, Co-Scientist reached essentially the same conclusion in about two days7. Had the Imperial researchers used the tool from the start, Costa says, it could have saved them the years of exploratory experiments that they conducted before they hit on the right mechanism.

“If you think about scientific discovery as a 100-metre race,” he says, with an AI assistant “you start this race at, say, metre 30 instead of metre 0”.

AI assistants generally use several agents to attack the same question from different angles. They can break scientific questions into smaller tasks, with agents tackling different pieces in parallel. The Google system — and competing platforms by FutureHouse, Huawei Technologies in Shenzhen, China8, and Sakana AI in Tokyo9— can explore several possible paths at once, allowing useful connections to emerge from the interplay between agents rather than from a single chain of reasoning.

“You have all these AI agents with different backgrounds to give different perspectives,” says Kyle Swanson, a computer scientist at Stanford who helped to developVirtual Lab, an early academic AI research-assistant platform10. “It gives you instant access to interdisciplinary experts.”

## Importance of good questions

But even a team of AI specialists requires someone to point the tool towards a worthwhile problem and to frame the challenge in such a way that the system can tackle it productively.

For a narrowly defined problem,the goal might be obvious. Perhaps this is why decades-old problems posed by the late Hungarian mathematicianPaul Erdősand solved by an AI tool in May provedfertile ground for machine logic. However, in open-ended science, deciding what to ask, and what would count as a meaningful answer, remains a fundamentally human task.

Human scientists trounce the best AI agents on complex tasks

“You have to ask really good questions,” Swanson points out. “If you ask very generic questions, then you’ll probably get very generic answers.”

Not that good questions necessarily require a tightly framed scope. For example, Philine Guckelberger, a molecular geneticist at FutureHouse and Stanford, fed Kosmos a large data set of molecular contacts that help to control which genes are switched on. She then asked the tool to hunt for patterns that a human researcher might overlook.

Kosmos initially stumbled over how the data were labelled, failing to make distinctions that seemed obvious to Guckelberger but had tripped up the tool. In one 30-million-row data set, for instance, it ignored a column in which two types of DNA region were distinguished. After Guckelberger corrected it, the system uncovered an unexpected pattern in cancer cells that she was able to confirm in independent data sets.

“It accelerated this like crazy,” she says.

## From start to finish

Another appeal of AI co-scientist platforms is that they can compress the most tedious parts of the research process and take on complex, multistep workflows a scientist would otherwise have to work out by hand.

## Enjoying our latest content?Log in or create an account to continue

* Access the most recent journalism from Nature's award-winning team
* Explore the latest features & opinion covering groundbreaking research

Access through your institution

or

Sign in or create an account

Continue with Google

Continue with ORCiD

Nature657, 1108-1110 (2026)

doi: https://doi.org/10.1038/d41586-026-02931-5

## References

1. Sabari, B. R.et al.Science361, eaar3958 (2018).ArticlePubMedGoogle Scholar
2. Schuijers, J.et al.Cell Rep.23, 349–360 (2018).ArticlePubMedGoogle Scholar
3. Gottweis, J.et al.Nature655, 487–496 (2026).ArticlePubMedGoogle Scholar
4. Guan, Y.et al.Adv. Sci.12, e08751 (2025).ArticleGoogle Scholar
5. Ghareeb, A. E.et al.Nature655, 497–505 (2026).ArticlePubMedGoogle Scholar
6. Huang, K.et al.Science393, eadz4351 (2026).ArticlePubMedGoogle Scholar
7. Penadés, J. R.et al.Cell188, 6654–6665 (2025).ArticlePubMedGoogle Scholar
8. Lyu, Y.et al.Preprint at arXivhttps://doi.org/10.48550/arXiv.2603.08127(2026).
9. Lu, C.et al.Nature651, 914–919 (2026).ArticlePubMedGoogle Scholar
10. Swanson, K., Wu, W., Bulaong, N. L., Pak, J. E. & Zou, J.Nature646, 716–723 (2025).ArticlePubMedGoogle Scholar
11. Cong, L.et al.Preprint at bioRxivhttps://doi.org/10.1101/2025.10.16.679418(2025).

Download references

## Related Articles

* Why AI cannot do good science without humans
* Teams of AI agents boost speed of research
* Human scientists trounce the best AI agents on complex tasks
* AI ‘scientists’ joined these research teams: here’s what happened
* AI for research: the ultimate guide to choosing the right tool
* NatureTech

## Subjects

* Technology
* Machine learning
* Drug discovery

## Latest on:

* Technology
* Machine learning
* Drug discovery

* Chinese companies doubled down on science after US tech restrictionsNews18 SEP 26
* Who gets credit in the AI era? OpenAI maths bombshell sparks debateNews17 SEP 26
* Is it safe to use consumer wearable devices for research?Spotlight16 SEP 26

* AI cracked the Navier–Stokes challenge. What does that mean for physics?News18 SEP 26
* How fast are you ageing? Ask AINews17 SEP 26
* How a team of AIs discovered a promising lung-cancer drugNews17 SEP 26

* Development of a random background to understand ligand optimizationArticle16 SEP 26
* Drug firms’ secret data supercharge AI protein modelsNews14 SEP 26
* TRI-611, a selective, brain-penetrant molecular glue degrader of ALKArticle09 SEP 26

### Jobs

* #### Assistant Professor of Physiology (in the Institute of Human Nutrition) - Tenure TrackThe Institute of Human Nutrition (IHN) at Columbia University seeks candidates for Assistant Professor in the tenure track.New York City, New York (US)Columbia University Irving Medical Center / Vagelos College of Physicians and Surgeons
* #### Cancer and Blood Diseases Institute - Brain Tumor Research - Faculty - JR225336The Cancer & Blood Diseases Institute, Cincinnati Children’s, invites applications for a faculty position in Brain Tumor research or CNS malignancies.Cincinnati, OhioCincinnati Children's
* #### Talent Recruitment Announcement at the College of Plant Science & TechnologyGather Global Talents, Forge Great AchievementsWuhan, Hubei (CN)Huazhong Agricultural University (HZAU)
* #### Recruitment Announcement for High-Level Talent at the Center for Agricultural MicrobiologyJoin HZAU's global faculty team to advance research with competitive benefits.Wuhan, Hubei (CN)Huazhong Agricultural University (HZAU)
* #### Faculty Search, Vanderbilt UniversityNashville, TennesseeVanderbilt University School of Medicine