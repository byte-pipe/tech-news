---
title: AI-detection tools have made huge leaps forward — how good are they? | Nature
url: https://www.nature.com/articles/d41586-026-02569-3
site_name: newsfeed
content_file: newsfeed-ai-detection-tools-have-made-huge-leaps-forward-ho
fetched_at: '2026-08-26T12:52:37.664903'
original_url: https://www.nature.com/articles/d41586-026-02569-3
date: '2026-08-25'
description: Scientists and publishers are testing a new breed of software that promises impressive accuracy at spotting AI-written text.
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

Illustration by Karol Banach

 

When Daniel Evanko asked a scientist whether they had used artificial intelligence to write their peer-review report, he didn’t expect a confession. Most researchers don’t reveal AI help, says Evanko, who is the director of journal operations at the American Association for Cancer Research (AACR).

How to manage AI risks while reaping the benefits

But this time was different. “Wow, you guys are good!” the reviewer wrote back, admitting that he had used a large language model (LLM) after running out of time.

Evanko had a secret weapon. He and the AACR deploy a commercialAI-detection tool called Pangram, because of concerns over the number of peer-review reports submitted to their journals that seem to use AI without disclosing it, contrary to the publisher’s policy.

After years of disappointing results, multiple firms now claim that software can reliably distinguish between AI-written and human-written text. One is Pangram Labs, the New York City-based start-up that makes Pangram. “Detect AI-generated content with 99.98% accuracy,” the firm sayson its website.

Scientists and research organizations are among those using the tool to spot AI’s traces. One in eight biomedical articles last year contained some AI-generated text according to Pangram, a study reported in January1. In June, the premier computer-science conference NeurIPSannounced that it rejected 18% of submissions after screening them with Pangram. Users of the preprint server arXiv can now check Pangram’s verdict on any article there, by visiting a mirror site calledalphaXivthat has installed the tool. And the University of Chicago in Illinois says that it has started using it to vet students’ coursework.

Pangram’s co-founder, Max Spero, says he wants to help everyone spot when text is AI-written. “If it’s taboo to call out that somebody’s using AI to write, then I think we’re going to see a lot more people shirking their jobs and letting AI replace themselves. We’re in a really critical time of setting norms,” he says. Spero has personally called out journalists whom Pangram suggests are using AI and, on one occasion, even flagged the Pope’s social-media posts as AI-written. This July, Pangram was integrated across the popular blogging platform Substack, allowing readers to see whether it deems posts to be AI-written.

Universities are relying on AI-detection software to catch cheating. How well do the programs work?

Pangram isn’t the only firm reporting remarkable results.GPTZero, a competitor also in New York City, says that it has 99% accuracy and provides “the most precise, reliable AI detection results on the market”. Five computer-science conferences and three universities have signed up to use it so far, says the firm’s chief technical officer, Alex Cui, and others are piloting it.

These AI detectors do work in the sense that they correctly flag solely human-written content as human almost all the time, independent analysts say, although no tool can be perfect. And they are “good for screening out places that are pumping out slop”, says Tim Requarth, who studies science communication at New York University’s Langone Health centre in New York City.

But they still sometimes make mistakes, so the tools can be used only as starting points for investigation — and their results are less illuminating for AI-edited writing, in which human and AI text intertwines and there is no clear boundary for problematic use.Naturehas tested the tools and interviewed experts to assess how well they do in various situations: where they work, and where they fall short.

## How to tell AI writing apart

Until Pangram and others came along, AI-detection software was notoriously unreliable, says Marzena Karpinska, a computer scientist at Simon Fraser University in Burnaby, Canada, who has conducted independent analyses of the tools. Most software analysed statistical characteristics of a text: AI writing tended to display more ‘perplexity’, an estimate of how predictable each word in a sequence is, and less ‘burstiness’, which measures changes in sentence lengths and structures across a text. Some tools would pick up on stylistic quirks in AI writing, such as over-use of the ‘It’s not X, it’s Y’ construction.

But these approaches would too often falsely flag human-authored text as AI-generated. “We didn’t have much faith in the detection,” says Karpinska. Some universities became so fed up with capricious AI detectors that they ended up banning or discouraging staff from using the software.

Then, in early 2024, Spero and Bradley Emi — both computer scientists who had worked at various technology firms since studying together at Stanford University in California — reported a different approach.

They gathered millions of human-written texts and asked LLMs to create ‘mirrors’ of the texts: requesting, for instance, an essay of the same title, length and tone as a human example. Then, they trained machine-learning models to distinguish between the human-written content and the AI mirror, refining the model’s performance by feeding the most challenging cases back in again. Like many such models, the resulting software is a black box. It learns to pick up subtle features of AI writing, often particular to specific LLMs. But these features cannot always be easily described in human terms.

How much of the scientific literature is generated by AI?

In their 2024 study (which has not been peer reviewed)2, Spero and Emi reported a 0.02% false-positive rate: that is, the model rarely labelled human writing as AI. Karpinska and other independent researchers tested the models3. “We were actually quite surprised that it was working really well. Whatever we threw at it, it was really, really good at detection,” she says.

This July, Epoch AI, a research firm in San Francisco, California,reported that Pangram had zero false positiveson 495 human-written texts. Pangram’s own latest technical paper reports a 0.0041% false-positive rate on English texts, with similarly low rates in more than 100 languages4. Tests in the study also show that Pangram doesn’t discriminate against writers who are not fluent English-speakers, a problem flagged with earlier software.

By the time Pangram’s early work became public, GPTZero had also switched from measuring perplexity and burstiness to deploying a similar form of machine learning. It, too, performed well in Karpinska’s study and scored zero false positives on Epoch AI’s test. In February, GPTZero marketed a 0.08% false-positive rate in internal tests, although its technical paper5more cautiously states this as “sub 1%” across all domains of writing.

## AI arms race

The tools’ impressive ability to spot solely human-authored work comes with a trade-off. To avoid flagging human text as AI, both firms accept a higher proportion of false negatives — that is, erroneously clearing some AI-generated text as human. Epoch AI found that Pangram and GPTZero flagged nearly all AI-generated passages made using basic prompts. But when AI was asked to mimic a particular author, some 8% of the resulting passages passed as human.

Karpinska’s study examined a ‘humanizer’ tool — one that rewrites AI-generated text to remove some signs of AI. She found that when detectors were asked to classify human texts versus humanized AI-written text, their false-negative and false-positive rates rose.

But the firms say these tests are already out of date. For instance, Karpinska’s study found that the just-released o1 LLM from OpenAI tripped up an old version of Pangram. Both these tools have now been superseded, and AI-detection firms continually update their models as new versions of LLMs are released.

In the past year, for instance, GPTZero has released 23 updates to its models. Meanwhile, Pangram Labs released its next-generation model, Pangram 4, in July, promising huge advances over its predecessor, including improvements in spotting AI-humanizer signatures. It says its false-negative rate is now only 0.34%, and when AI is asked to imitate styles (as in Epoch’s test), the false-negative rate falls to 2.9%. As with all models, however, performance drops with very short AI passages (of under 50 words).

The upshot is that only the accuracy rates announced by the firms from internal testing can be truly current — but these are not externally verified. “Third-party evaluations will always lag behind the latest detectors,” Requarth says.

## The mixed-AI challenge

Both Pangram and GPTZero make money by selling subscriptions for regular or heavy use, but allow some limited free checks. Both have also launched browser tools that check for AI-written text on social media, other web pages and Google docs.

As more writers have experienced being flagged by the software, it’s become clear that the biggest challenge lies in how to approach cases of AI-assisted writing, which is becoming increasingly common. Writers who use AI toldNaturethat it would be useful to draw a line between using AI to polish or edit human-authored drafts, which they saw as mostly acceptable, and generating a draft with AI from scratch then editing or humanizing it.

Both Pangram and GPTZero break down texts into parts and try to show the degree to which a document is lightly polished with AI, heavily AI-assisted or entirely AI-generated (see ‘How two AI-detectors present their scores’). But in practice, the tools don’t always satisfyingly distinguish between these cases.

Source: top, Pangram; bottom, GPTZero

For instance, in June, Elena Vicario, director of research integrity at the publisher Frontiers, headquartered in Lausanne, Switzerland, wrotea post for The Scholarly Kitchen, a website that posts views on scientific publishing, arguing that AI can be used to support peer review. WhenNatureran this article through Pangram in early July, it came up as 100% AI; after Pangram 4 was released, this changed to 96% AI.

But Vicario says her first draft and the ideas that went into it were “entirely human-created” and that she used AI as a tool to polish the text “which is simply best practice”. Editors at The Scholarly Kitchen add that the article was further edited there, so it couldn’t be wholly AI.

If Pangram labels a work as 100% AI, this doesn’t actually mean every word was AI-generated, Spero says. The tool divides a text into segments and judges whether each segment is probably AI-generated, human-written or ‘mixed’. Then, Pangram assigns an overall score on the basis of the proportion of segments flagged. 100% AI means only that each segment was judged as probably AI, even if the segment has some human-written content.

This chunking process means that a paragraph judged ‘human’ in isolation could switch to AI when combined with other text in a segment, Spero adds — explaining why some writers find that sentences extracted from an article can score differently than when judged in the article as a whole.

“If an editor or author used an AI program to smooth out a sentence or clarify the argument during the editing process, we do not view this as a problem,” Vicario says.

Pangram 4, the software launched this July, has changed evaluations in part because it divides text into more fine-grained sections. Whereas the older version analysed segments of some 200–300 words — meaning that a 1,000-word post might end up being divided into only three sections — the new version can analyse chunks as small as 30–40 words.

Spero says that Pangram 4 better distinguishes between a light AI polish — which usually retains a human-authored label — and heavy AI edits. “It takes major AI input like fully-generated sentences or major rewrites to trigger Pangram 4,” he says.

GPTZero analyses texts slightly differently. Like Pangram, it divides them into segments, but at the end, it gives a score that represents its confidence about the whole text, rather than a breakdown of the results of each segment5. Paid users can see which sentences contributed most to GPTZero’s assessment of a work as probably human, AI or mixed. The tool produces 100% confidence that Vicario’s post was AI, described as meaning the software is “highly confident this text is AI-generated”.

Can Anthropic’s invisible watermarks curb ‘AI slop’? Researchers remain sceptical

AfterNaturelooked into the case, editors at The Scholarly Kitchen noted on the post that AI had been used “as an editing tool”.

Further questions about Pangram’s evaluations arose when, during the reporting of this article, Spero sent over an examination of articles onNature’s website. Some articles in a sample from the websites ofNature IndiaandNature Africacame up as mixed AI–human, and in some cases, 100% AI, he noted, using Pangram 3.3’s assessment.

An examination by the sites’ editorial teams showed that some of the articles flagged were AI-assisted translations of another article or short research highlights that were explicitly written with the aid of AI and had been human-edited. But some were articles written by contributors. They said that they had used AI only to help transcribe or translate interviews, organize notes and edit their drafts. All of these articles went through further rounds of human editing.

In many cases, Pangram 4 judged these articles as merely mixed human–AI, whereas the older version had called them wholly AI. But the newer software still labelled twonewsreportsas 100% AI that contained information derived from original reporting, including interviews. Both sites permit AI use with human oversight, in line withguidance for publications in the Nature Portfoliothat says AI should be declared if used for extensive copy-editing or writing, but doesn’t need to be declared for polishing or refining language, although transparency is encouraged. After examining the Pangram results, site editors added notes to some articles to flag the AI assistance.

Overall, as with The Scholarly Kitchen case, the software correctly spotted AI involvement. But Pangram and GPTZero sometimes disagreed on how they rated the articles and on which segments had the strongest indications of being human or AI. And the examples suggest that articles flagged as 100% AI or near 100% can include text written and edited by humans.

Spero says that although Pangram is good at spotting cases in which wholly AI-written paragraphs are inserted between stretches of human-authored text, “there’s a lot of room for improvement” in judging real-world cases in which AI and human writing mingles in a more homogeneous way. For instance, he says, small edits to such documents can sometimes shift Pangram’s score by a large amount — a problem known as ‘jitter’. Pangram’s technical study also notes that when the firm tested using consumer AI to “substantially modify” human-written student essays, the model still labelled the results fully human 41% of the time.

Requarth says that he doesn’t put a lot of faith in exact percentages given by detectors for cases in which AI assistance or editing is involved, and particularly not down to the level of arguing that individual sentences or short chunks of text were AI-written.

The priority for AI detectors should be determining whether a text is fully generated by AI, because “that’s what people are looking for”, says Cui. Determining the extent of AI assistance in a text “is a harder problem”, he says.

## Enjoying our latest content?Log in or create an account to continue

* Access the most recent journalism from Nature's award-winning team
* Explore the latest features & opinion covering groundbreaking research

Access through your institution

or

Sign in or create an account

Continue with Google

Continue with ORCiD

Nature656, 808-811 (2026)

doi: https://doi.org/10.1038/d41586-026-02569-3

## References

1. She, R. Preprint at bioRxivhttps://doi.org/10.64898/2026.01.01.697311(2026).
2. Emi, B. & Spero, M. Preprint at arXivhttps://doi.org/10.48550/arXiv.2402.14873(2024).
3. Russel, J., Karpinska, M. & Iyyer, M. InProc. 63rd Annu. Meet. Assoc. Comput. Linguist.(Vol. 1: Long Papers), 5342–5373 (Association for Computational Linguistics, 2025).
4. Glickenhaus, B.et al.Preprint at arXivhttps://doi.org/10.48550/arXiv.2607.27183(2026).
5. Alexandru Adam, G.et al.Preprint at arXivhttps://doi.org/10.48550/arXiv.2602.13042(2026).

Download references

Reprints and permissions

## Related Articles

* How to manage AI risks while reaping the benefits
* Can Anthropic’s invisible watermarks curb ‘AI slop’? Researchers remain sceptical
* Universities are relying on AI-detection software to catch cheating. How well do the programs work?
* How much of the scientific literature is generated by AI?
* Major AI conference flooded with peer reviews written fully by AI
* LINK AI tool detects LLM-generated text in research papers and peer reviews

## Subjects

* Machine learning
* Computer science
* Publishing
* Peer review

## Latest on:

* Machine learning
* Computer science
* Publishing

* Amend copyright licences to halt AI misuse and reassert human controlCorrespondence25 AUG 26
* The future of peer review requires AI support, not AI bansCorrespondence25 AUG 26
* Assessing students in the AI eraCorrespondence25 AUG 26

* How to manage AI risks while reaping the benefitsEditorial25 AUG 26
* Staggering 90% of biomedical papers now show signs of AI helpNews20 AUG 26
* AI tool lets researchers ‘vibe code’ in the quantum realmNews19 AUG 26

* Amend copyright licences to halt AI misuse and reassert human controlCorrespondence25 AUG 26
* The future of peer review requires AI support, not AI bansCorrespondence25 AUG 26
* Sleuth identifies dozens of studies that used the wrong antibodyNews21 AUG 26

### Jobs

* #### 2027 Overseas Outstanding Young Scholars: NKU Invites Talents From Around the WorldNankai University sincerely invite outstanding talents at home and abroad to apply for the 2027 Overseas Outstanding Young Scholars Fund.Tianjin, CNNankai University
* #### Physician-Scientist Positions in Research Hospital, ShanghaiTech UniversityInvites visionary Physician-Scientists and Clinicians across all disciplines and career stages to join our foundational team.Shanghai (CN)ShanghaiTech University
* #### Faculty Positions (School of Biomedical Engineering (BME))School of Biomedical Engineering invites highly qualified candidates to apply for multiple tenure-track/tenured faculty positions.Shanghai (CN)ShanghaiTech University
* #### Faculty Positions (School of Creativity and Art (SCA))School of Creativity and Art (SCA) calls for candidates with exceptional academic records or demonstrated potential.Shanghai (CN)ShanghaiTech University
* #### Faculty Positions (Information & Mathematical Science)School of Information Science and Technology invites highly qualified candidates to fill multiple tenure-track/tenured faculty positions.Shanghai (CN)ShanghaiTech University