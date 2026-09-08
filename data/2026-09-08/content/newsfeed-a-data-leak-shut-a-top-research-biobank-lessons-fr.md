---
title: 'A data leak shut a top research biobank: lessons from the recovery | Nature'
url: https://www.nature.com/articles/d41586-026-02803-y
site_name: newsfeed
content_file: newsfeed-a-data-leak-shut-a-top-research-biobank-lessons-fr
fetched_at: '2026-09-08T14:54:05.151437'
original_url: https://www.nature.com/articles/d41586-026-02803-y
date: '2026-09-08'
description: The UK Biobank is imposing new safety measures after a security incident, but safeguarding biomedical data while enabling researcher access remains a challenge.
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

Illustration: Adrià Voltà

 

On a Tuesday in mid-April, the UK Biobank — one of the largest and most comprehensive health-tracking studies in the world — received a troubling e-mail from an anonymous researcher. The sender had discovered what appeared to be sensitive information from hundreds of thousands of the study’s participants for sale on Xianyu, an e-commerce website owned by the Chinese technology company Alibaba.

With the help of Alibaba and the governments of the United Kingdom and China, the UK Biobank managed to get the listing removed. Still, the incident raised concerns about data security, spurred an internal investigation and led the biobank to cut off access for researchers while it built new infrastructure to secure its data. After nearly five months offline, the biobank has said it will begin to re-open to researchers this month.

Using biobanks to boost research: a how-to guide

The UK Biobankcontains genetic information and troves of other biomedical data, including medical-imaging files, health history and lifestyle information, from 500,000 people who agreed to take part in the decades-long study. It’s one of several biobanks available to researchers globally. But researchers say that theUK Biobank is particularly valuable. “We’ve learned more about human biology from the work from UK Biobank than I think we have from any other single resource,” says Daniel MacArthur, a geneticist at the Garvan Institute of Medical Research in Sydney, Australia. Reasons for this include the large number of participants and the volume and diversity of the data collected, MacArthur adds. “But fundamentally, it’s also because they made it highly accessible, and that meant researchers all around the world were able to use that resource.”

The incident suggests that this openness might have its downsides — at least without stringent security measures. According to theresults of the UK Biobank’s internal investigation, published on 4 June, there have been three instances, all linked to institutions in China, in which participant data were offered for sale online. All the listings have been taken down and the UK Biobank has banned these institutions from further access. And Alibaba has implemented automated searches to remove listings that reference the biobank.

This isn’t the first time that research data sets have dealt with a data-security issue. In March, shortly before the latest security incident, UK newspaperThe Guardianreported that, on dozens of occasions, data from the UK Biobank hadaccidentally been uploaded by researchers onto the public code repository GitHub, and showed how the data could potentially be linked back to an individual study participant. And in 2023, hackers accessed sensitive data, such as names, addresses and ancestry information, from millions of users of the consumer genetic-testing company 23andMe.

The UK Biobank and 23andMe have since reassessed their security protocols and made updates to their platforms to put stricter controls on access. (23andMe was sued by affected users and agreed to pay more than US$40 million in compensation earlier this year.) These changes are happening amid abroader trend of biorepositories increasing restrictionson who can access their data and how. Many researchers say that the benefits of these changes to data security outweigh the drawbacks, but some worry that these restrictions might prevent legitimate users from using the data to their full potential.

Getting the right balance between data accessibility and security is crucial, says Joe Watts, director of data policy at the UK Biobank, who is based in Cambridge, UK. “We take the protection of our participants’ data extremely seriously and use great care to remove identifiable information and vet researchers and institutions,” he says. “We recognize that we can do more, and we are adding extra security measures.”

## Controlled access

When the UK Biobank was first opened to the scientific community in 2012, it operated on what some describe as a ‘lending library’ system, in which researchers who obtained approval were able to download raw data to analyse on their own devices.

To protect participant privacy, the UK Biobank and some other repositories keep personally identifiable information, such as names, addresses and dates of birth, hidden through a process known as pseudonymization. This keeps sensitive details, such as information around drug and alcohol use, physical and sexual abuse and diagnoses, from being linked to individual people. But concerns have been raised about the extent to which personal information can be linked to specific people — a process known as re-identification — if a pseudonymized data set leaks online, even with such measures in place.

Screening babies’ genomes could save lives. Here’s how it would work

In its March report,The Guardianrevealed that it had managed to link health records that had inadvertently been posted online back to a UK Biobank participant, using the month and year of her birth and the date of a surgical procedure, which she had provided to the paper. (In theUK Biobank’s report on the security incidentin April, it stated that, although re-identification is not impossible, the organization is unaware of any cases in which it has occurred without a participant’s help.)

Other concerns about data security preceded the latest incident. The same investigation byTheGuardianrevealed that, between July and December last year, the UK Biobank had issued several take-down notices to GitHub, asking the repository to remove biobank data that researchers had accidentally posted. Of the roughly 1,500 research institutions that have downloaded the UK Biobank data set, about 700 failed to confirm that they had deleted the data after an authorized period of use was up. The UK Biobank has said that if researchers fail to delete these data, everyone at their respective institutions will be barred from accessing the biobank when it reopens.

Other security measures have also been put in place. To help keep data secure, biobanks have increasingly adopted ‘reading library’ approaches. Researchers are not allowed to download the data; instead, they must run experiments on a secure platform and can only download results. For example,All of Us— an initiative run by the US National Institutes of Health (NIH) aimed at creating a repository of genetic and other biomedical data from one million people in the United States — makes data corresponding to individual participants (also known as participant-level data) accessible only through a cloud-based platform.

The UK Biobank collected DNA data from 500,000 people across the United Kingdom.Credit: Sean Wilton/Bloomberg via Getty

The UK Biobank itself started transitioning to this type of system in 2021, and made it broadly accessible to researchers in 2024. However, it remained possible to download participant-level data by designating them as a result. Although the UK Biobank’s policy explicitly stated that this was not allowed, the organization did not have a system in place to automatically monitor exactly what was exported from its platform. Many biobanks have implemented security systems, sometimes referred to as ‘airlocks’, that screen exported data to prevent participant-level information from being downloaded. The UK Biobank has been working on setting up an airlock, which will start being rolled out when the research platform reopens.

Even with airlock-type systems in place, there remain ways for bad actors to get around them — for example, by taking screenshots of data while they are on the secure platform. Protecting participant data is a “continuous process” for biobanks, says Josh Denny, the chief executive of All of Us. This involves regularly scouring the Internet to ensure that data haven’t leaked, as well as communicating potential risks to other biobanks. For example, the UK Biobank discovered that Xianyu also had listings referencing other biobanks, including All of Us, and immediately informed them of the risk, enabling them to check the postings and confirm that no participant-level data were being put up for sale, Denny says.

“There is no single magic silver bullet when it comes to data security,” says Ewan Birney, director of the European Molecular Biology Laboratory’s European Bioinformatics Institute in Hinxton, UK. But having several layers of security makes it harder for researchers to make careless mistakes, and for bad actors to misuse the data, Birney adds.

Luc Rocher, a data-privacy researcher at the Oxford Internet Institute, UK, says that, although implementing airlock-type checks on reading-library-style platforms might help to mitigate data leaks, biorepositories could go further when it comes to data security. According to Rocher, researchers could switch to a system in which they send code to a platform that allows them to analyse participant data without having direct access to the information. One such system is OpenSAFELY, run by the University of Oxford, UK.

## Research silos

Although the reading-library approach provides more security than the lending-library model, it also poses challenges for research. Currently, researchers who want to integrate data from several biobanks typically need to log into each one’s research environment, perform the same analysis, export results and then conduct a meta-analysis using those findings.

Nowadays, MacArthur says, each new national biobank is installed inside a custom environment. This makes it essentially impossible to bring all of the raw data together. And each system has idiosyncrasies — a piece of code that works in one might not run in another, for example — meaning that researchers need to understand the complexities of every system that they work with.

Open data is key to genomics research — if the information can be kept safe

There are several efforts to combine summary statistics, such as the frequency of particular gene variants or the results from genome-wide association studies (GWAS) across databases, to reduce the need for this type of cross-analysis. (Biobanks often make summary statistics publicly available, because they are considered low risk when it comes to participant privacy.) The Global Alliance for Genomics & Health is working on developing ways to unify analyses, and the Genome Aggregation Database (gnomAD) aims to combine summary statistics from biobanks around the world. Researchers in the Global Biobank Meta-Analysis Initiative have brought together more than 30 biobanks to enable scientists to conduct joint assessments of GWAS results.

## Enjoying our latest content?Log in or create an account to continue

* Access the most recent journalism from Nature's award-winning team
* Explore the latest features & opinion covering groundbreaking research

Access through your institution

or

Sign in or create an account

Continue with Google

Continue with ORCiD

Nature657, 334-336 (2026)

doi: https://doi.org/10.1038/d41586-026-02803-y

Reprints and permissions

## Related Articles

* Using biobanks to boost research: a how-to guide
* Screening babies’ genomes could save lives. Here’s how it would work
* Open data is key to genomics research — if the information can be kept safe
* What went wrong at 23andMe? Why the genetic-data giant risks collapse
* Ambitious survey of human diversity yields millions of undiscovered genetic variants

## Subjects

* Genetics
* Genomics
* Public health

## Latest on:

* Genetics
* Genomics
* Public health

* DeepMind’s new genome ‘atlas’ charts effects of all 9 billion human gene mutationsNews08 SEP 26
* Two children died from gene therapies in China: where the field goes nextNews08 SEP 26
* Robust inference and correlates from genetic associations with personalityArticle02 SEP 26

* DeepMind’s new genome ‘atlas’ charts effects of all 9 billion human gene mutationsNews08 SEP 26
* Anxious or outgoing? Huge study links ‘Big Five’ personality traits to genetic variantsNews02 SEP 26
* Mutating every DNA letter of a genome shows surprising effects — and the limits of AINews01 SEP 26

* Scale of snakebites estimated globallyNews & Views31 AUG 26
* AI models are being used to track zoonotic diseases. Will they prevent the next pandemic?Technology Feature30 AUG 26
* The Moderna cancer vaccine offers hope — now we must speed up personalized therapiesWorld View28 AUG 26

### Jobs

* #### Professor in Medical BacteriologyJoin Uppsala University as Professor of Medical Bacteriology. Lead research, teaching and doctoral education. Apply no later than 31 October 2026 now.Uppsala (Stad) (SE)Uppsala University
* #### 2027 Overseas Outstanding Young Scholars: DUT Invites Talents From Around the WorldSuccessful candidates receive professorships, competitive pay, research funding, relocation support, PhD quotas, and family benefits.Dalian, Liaoning (CN)Dalian University of Technology
* #### Chief Strategy OfficerThis role leads the Strategy Group which sits at the centre of the organisation’s coordination architecture.Canary Wharf, London E14 4PUMHRA - Medicines and Healthcare products Regulatory Agency (MHRA)
* #### Professorship Position in Materials PhysicsAt Montanuniversität Leoben (MUL), AustriaAustria (AT)Technical University of Leoben
* #### Faculty Positions at the Center for Machine Learning Research (CMLR), Peking UniversityCMLR's goal is to advance machine learning-related research across a wide range of disciplines.Beijing (CN)Center for Machine Learning Research (CMLR), Peking University