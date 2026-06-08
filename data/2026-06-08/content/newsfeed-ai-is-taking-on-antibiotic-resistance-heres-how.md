---
title: AI is taking on antibiotic resistance — here’s how
url: https://www.nature.com/articles/d41586-026-01818-9
site_name: newsfeed
content_file: newsfeed-ai-is-taking-on-antibiotic-resistance-heres-how
fetched_at: '2026-06-08T12:34:01.836259'
original_url: https://www.nature.com/articles/d41586-026-01818-9
date: '2026-06-08'
description: A suite of artificial-intelligence tools is helping to speed up the process of discovering new antibiotics. A suite of artificial-intelligence tools is helping to speed up the process of discovering new antibiotics.
tags:
- nature
---

AI is taking on antibiotic resistance — here’s how
 

Download PDF

Download PDF

* Email
* Bluesky
* Facebook
* LinkedIn
* Reddit
* Whatsapp
* X

 

Some bacteria are becoming resistant to the antibiotics commonly used to control them.Credit: NIAID/NIH/Science Photo Library

When it comes to bacterial infections in the gut, antibiotics are effective yet broad-acting: although they might kill disease-causing species effectively, beneficial microflora can get caught in the crossfire. This indiscriminate effect can be harmful, particularly for people with Crohn’s disease or other chronic gastrointestinal conditions. It also increases the likelihood that antibiotic-resistant strains of bacteria will evolve.

In 2023, microbiologist Jonathan Stokes at McMaster University in Hamilton, Canada, began looking for options that could target pathogens with greater precision. He and his colleagues screened some 10,000 bioactive compounds for antibacterial activity against a strain ofEscherichia colithat can cause severe gut infections. They filtered the results on the basis of various criteria, including toxicity to bacteria and structural novelty compared with existing antibiotics. “We got super lucky in that we only ended up with one molecule,” says Denise Catacutan, the doctoral student in Stokes’s laboratory who led the work1.

But the team needed to confirm that the promising molecule, named enterololin, was specific to its target pathogen, rather than acting as another broad-spectrum antibiotic. Typically, researchers rely on extensive biochemical screens, RNA sequencing or proteomics to elucidate how molecules such as enterololin disrupt bacterial pathways. This time, the team turned to artificial intelligence.

How we’re using AI tools to improve psychedelic-drug research

AI tools can accelerate the process of developing pharmaceuticals and are fast becoming a crucial component of drug discovery. But using AI to identify an antibiotic’s mechanism of action is still uncommon, says Regina Barzilay, a computer scientist at the Massachusetts Institute of Technology (MIT) in Cambridge.

Barzilay’s lab developed a tool to fill that gap.DiffDockuses AI to predict how small molecules bind to proteins. It can thereby identify possible protein targets — and potential mechanisms of action for the small molecules. By applying this tool to enterololin, Stokes and his research group “could kind of narrow down our experimental pipeline”, Catacutan says. The team developed bacterial strains with mutations in the genes encoding predicted target proteins, and quickly confirmed DiffDock’s predictions.

Barzilay’s interest in antibiotics is personal. Her father contracted a bacterial infection of the spine that required complex surgery, and another family member survived an infection that didn’t respond to any antibiotics. “We are so used to the idea that antibiotics are there to protect us,” she says. But that protection is precarious. Antibiotic resistance is a pervasive, growing global crisis; estimates suggest that drug-resistant infections could kill at least 39 million people by 2050.

Yet antibiotic development and manufacturing are expensive and rarely profitable, so drug companies are reluctant to invest. Discovering antimicrobials that can be synthesized easily — and cheaply — could help. An increasing number of researchers are turning to AI to address this need. Using machine-learning tools to tackle tasksin silico, from identifying new antibiotic candidates to predicting potential mechanisms of action, enables researchers to work faster — and on tighter budgets.

## Strong foundation

Barzilay’s interest in antibiotic development began in 2018, when she met MIT biomedical engineer James Collins at an institution-wide symposium on the use of AI tools. Barzilay and Collins teamed up to apply these techniques to antibiotic discovery. Stokes, who was a postdoctoral researcher in Collins’s lab with expertise in high-throughput screening of small molecules, joined the effort.

The team developed a model based on neural networks (machine-learning architectures inspired by the human brain) that correlated molecular features — for example, bond types, atomic number and electronic charge — with properties such as solubility and microbial growth inhibition.

The researchers trained their model — calledChemprop— on data from 2,300 or so molecules that had been tested for their ability to inhibit the growth ofE. coli. They then used the model to screen millions of molecules for potential drug candidates, eventually homing in on a kinase inhibitor that the group named halicin. This proved to have a potent effect on several pathogenic species, includingMycobacterium tuberculosis(the causative agent of tuberculosis); drug-resistantE. coli; andAcinetobacter baumannii(an opportunistic pathogen that can cause infections in hospitalized individuals)2. “We were able to create a model that can generalize to totally unseen classes of chemistry,” Barzilay says.

But having training data is only a first step — how it’s labelled and classified is equally important, says Molly Bartlett, a chemical informatician at Imperial College London. Bartlett works with the Fleming Initiative, a multi-institutional collaboration headed by Imperial College London and Imperial College Healthcare NHS Trust that aims to combat antimicrobial resistance globally.

When compiling the initiative’s data, Bartlett searched the published literature for examples of high-throughput screening for molecules that can breach the outer cell membrane of pathogenic bacteria and accumulate inside the cells. Bartlett uses RDKit and xTB, computational tools that simulate and analyse molecular structures, to mimic how these molecules might behave when dissolved in water or in a cell’s lipid membrane. She also categorizes the chemical features that are responsible for various properties of the molecules, such as their solubility and ability to enter the bacterial cell. “If the input is not able to represent what makes the property happen, you’re not going to be able to get a good prediction,” she explains.

Computer scientist Regina Barzilay is trying to use AI to decipher drugs’ mechanisms.Credit: Sophie Park for The Washington Post via Getty

In Stokes’s experience, a strong training data set should include at least a subset of available clinical drugs, as well as potential antibiotics that are not currently used in the clinic. Training data should also be physically, chemically and structurally diverse — and should represent powerful antimicrobials, as well as ineffective ones, so that AI models can also learn what not to do. For those interested in building AI tools to find new antibiotics, “80% of your time has to be spent on data acquisition, data processing and data representation,” Stokes advises.

Bartlett, for instance, says that at least 10% of the molecules in her training data need to penetrate the bacterial envelope, so that the model can learn the characteristics that predict accumulation. Some databases she works with contain upwards of 100,000 molecules, but often only 3% of those molecules can enter the type of bacteria that interests her. She also tries to maximize the diversity of chemical structures represented in the training data. Without this breadth, she says, “you’re not going to be able to have a predictive model”.

Generative AI tools have made her work easier. Bartlett and Catacutan struggled at first with writing the code necessary to run models, but now use AI tools such as Google’s Gemini and OpenAI’s ChatGPT to help with troubleshooting. Bartlett will occasionally provide Gemini with a toolkit’s explanatory text file, often called a README file, then give the chatbot detailed instructions on what errors to look for in her code. “You still have to know what to ask for, but you don’t have to be an expert in the architecture itself of the code,” she says. “It makes it really accessible.”

## Peptide power-up

Also on a quest for chemical diversity is César de la Fuente, a synthetic biologist at the University of Pennsylvania in Philadelphia. De la Fuente’s work focuses on antimicrobial peptides: naturally occurring short chains of amino acids that could prove to be potent antibiotics. His lab has also pioneered a technique called molecular de-extinction, which aims to ‘resurrect’ molecules that might have useful biological characteristics from extinct organisms.

Six key developments in the fight against antimicrobial resistance

De la Fuente and his team used a combination of neural networks to create a tool calledAPEX(antibiotic peptide de-extinction). They used this to screen a database of more than ten million peptides, and identified more than 37,000 that were predicted to have broad-spectrum antimicrobial activity3. About 11,000 of these were derived from the ‘extinctome’ — proteomes from extinct creatures, including, in this case, an ancient magnolia, a giant sloth and a Grant’s zebra.

The researchers synthesized and tested 69 of these candidate molecules against bacterial pathogens and found that many of them had an unusual mechanism of action. Rather than targeting a pathogen’s outer, rigid cell wall, these compounds acted on the inner cytoplasmic membrane — a strategy that might make them more robust as antibiotics, because bacteria are less likely to have evolved resistance to molecules they have never encountered. “Evolution is this beautiful planetary-scale optimization process,” de la Fuente says. It’s “the biggest optimization experiment that we have ever seen”.

## Making molecules

Having learnt from extinct molecules, de la Fuente’s team took the next step: they developed a generative AI model that can design synthetic molecules that don’t — yet — exist in nature4. “Generative AI gives you this opportunity now to go beyond the sequence space that evolution has explored, to come up with things that may have properties and functions that are more optimized in certain ways,” de la Fuente says.

The team provides its model — called ApexGO — with a peptide template, and specifies design goals, constraints and rules, such as how closely the designs must adhere to the starting peptide. People in the lab then step in to assess which designs could be viable. They might, for instance, exclude peptides that have too many hydrophobic residues, which would cause clumping in solution, de la Fuente says. The researchers then synthesize promising molecules, which they study in cultured cells and in animal models of infection. The team has so far synthesized and tested around 100 peptides, de la Fuente says. About 86% showed antimicrobial activity against at least one pathogen.

The hunt for the next antibiotics

But most antibiotics are small molecules, not peptides. And small molecules designed by generative AI tools can often be challenging to make, Collins says, because they are too unstable, too expensive or simply chemically impossible. AI tools frequently design molecules that cannot actually be made, because the synthetic steps required don’t follow real-world rules.

## Enjoying our latest content?Log in or create an account to continue

* Access the most recent journalism from Nature's award-winning team
* Explore the latest features & opinion covering groundbreaking research

Access through your institution

or

Sign in or create an account

Continue with Google

Continue with ORCiD

Nature654, 560-562 (2026)

doi: https://doi.org/10.1038/d41586-026-01818-9

## References

1. Catacutan, D. B.et al.Nature Microbiol.10, 2808–2822 (2025).ArticlePubMedGoogle Scholar
2. Stokes, J. M.et al.Cell180, 688–702 (2020).ArticlePubMedGoogle Scholar
3. Wan, F., Torres, M. D. T., Peng, J. & de la Fuente-Nunez, C.Nature Biomed. Eng.8, 854–871 (2024).ArticlePubMedGoogle Scholar
4. Torres, M. D. T.et al.Nature Mach. Intell.8, 841–856 (2026).ArticlePubMedGoogle Scholar
5. Krishnan, A.et al.Cell188, 5962–5979 (2025).ArticlePubMedGoogle Scholar
6. Swanson, K.et al.Mol. Syst. Biol. https://doi.org/10.1038/s44320-026-00206-9 (2026).ArticleGoogle Scholar

Download references

## Related Articles

* How we’re using AI tools to improve psychedelic-drug research
* Six key developments in the fight against antimicrobial resistance
* The hunt for the next antibiotics
* Nature Outlook: Antimicrobial resistance
* NatureTech hub

## Subjects

* Antibiotics
* Microbiology
* Chemistry
* Machine learning

## Latest on:

* Antibiotics
* Microbiology
* Chemistry

* A natural depsipeptide antibiotic binds the E-site of the bacterial ribosomeArticle03 JUN 26
* The hunt for the next antibioticsOutlook13 MAY 26
* Street sellers and private physicians fuel antibiotic overuseOutlook13 MAY 26

* A natural depsipeptide antibiotic binds the E-site of the bacterial ribosomeArticle03 JUN 26
* Commensal-derived acetylcholine enhances mucosal immune educationArticle03 JUN 26
* Better diagnostics could have limited this Ebola outbreakWorld View02 JUN 26

* Nuclear-fusion firm says plant will deliver electricity to grid – but big questions remainNews08 JUN 26
* Electric vehicles cut pollution in China – and prevent 260,000 premature deathsNews05 JUN 26
* Mechanophore cross-linking enhances ballistic energy dissipation of polymersArticle03 JUN 26

### Jobs

* #### Associate or Senior Editor, Nature CatalysisTitle: Associate or Senior Editor, Nature Catalysis Locations: Shanghai, Beijing, Milan and Pune – hybrid working model Application Deadline: July ...Shanghai, Beijing, Milan and Pune – hybrid working modelSpringer Nature Ltd
* #### Postdoctral ResearcherThis postdoctoral researcher position focuses on research on the development of polymer biomaterials for medical applications. Specifi...Tsukuba, Ibaraki (JP)National Institute for Materials Science (NIMS)
* #### Seeking Global Talents at All Levels - SIATWe find Distinguished PIs, Senior PIs, Junior PIs, Senior Engineer, Junior Engineer, Post-doctoral fellow, Assistant research fellow.1068 Xueyuan Avenue, Shenzhen 518055 P. R. ChinaShenzhen Institutes of Advanced Technology (SIAT), Chinese Academy of Sciences（CAS)
* #### Global Recruitment of Outstanding Young TalentsWe are seeking exceptional candidates who qualify for the National Science Fund for Excellent Young Scholars (Overseas)1068 Xueyuan Avenue, Shenzhen 518055 P. R. ChinaShenzhen Institutes of Advanced Technology (SIAT), Chinese Academy of Sciences（CAS)
* #### Global Recruitment for Faculty, Postdocs, and Specialists at Hangzhou Institute of Medicine, CASSeeking exceptional Senior/Junior PIs, Postdocs, and Core Specialists globally year-roundHangzhou, ChinaHangzhou Institute of Medicine Chinese Academy of Sciences (HIMCAS)

Close banner

Close

Sign up for theNature Briefingnewsletter — what matters in science, free to your inbox daily.

Email address

Sign up

I agree my information will be processed in accordance with the 
Nature
 and Springer Nature Limited 
Privacy Policy
.

Close banner

Close

Get the most important science stories of the day, free in your inbox.

Sign up for Nature Briefing