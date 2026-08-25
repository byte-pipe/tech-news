---
title: AI won’t replace radiologists, but it will dramatically change their jobs
url: https://arstechnica.com/health/2026/08/ai-wont-replace-radiologists-but-it-will-dramatically-change-their-jobs/
site_name: newsfeed
content_file: newsfeed-ai-wont-replace-radiologists-but-it-will-dramatica
fetched_at: '2026-08-25T19:29:45.014508'
original_url: https://arstechnica.com/health/2026/08/ai-wont-replace-radiologists-but-it-will-dramatically-change-their-jobs/
date: '2026-08-25'
published_date: '2026-08-25T15:10:03+00:00'
description: A pioneering AI scientist once predicted computers would replace human radiologists. They haven't.
tags:
- ars-technica
- ai
- health
- radiology
---

Text
 settings

In 2016 Geoffrey Hinton, the Nobel-winning “godfather of AI,” predicted that radiologists—the physicians who read X-rays, ultrasounds, and other images to help make medical diagnoses—would find themselves replaced by computers within five years. Today the field can retort by quoting Mark Twain’s famous quip:The report of my death was an exaggeration.

Radiology’s ranks are in fact growing steadily, with the number of practitioners expected toexpand by 26 percent or more over the next three decades. But what Hinton may have missed about the dynamics of the job market should not obscure his prescience: He was correct that human physicians now have a silicon-based colleague in the room that matches or exceeds their performance. In fact, radiology is far and away medicine’s hot spot for AI, making it a bellwether for the adoption of expert decision-making systems across healthcare and perhaps in other fields.

As of early 2026, about three-quarters of the 1,400 AI-enabled medical devices cleared by theFood and Drug Administrationwere for radiology. Some make physicians more efficient by drafting reports or alerting them to the images that urgently need attention. But other AI tools have the potential to improve on human performance by identifying abnormalities that may not be visible to the human eye, or interpreting images as well as—and sometimes better than—trained radiologists. For example, ananalysis of 43 clinical trialsconcluded that AI-assisted colonoscopies reveal more polyps than conventional ones.

Improving accuracy is important, because the average human error rates involving diagnostic images are estimated to range from 3 to 5 percent, which translates to about40 million errors worldwide each year. Yet the solution is not as simple asreplacing humans with machines. Ten years after Hinton’s sensational prediction, the big question is not whether humans or AI do statistically better at a given task, but how the technical precision of AI can be combined with the experience and flexibility of humans to improve accuracy for the benefit of patients.

## Working together

Finding the best way todesign such a collaborative systemis not straightforward. Even if AI is more reliable on average than a skilled radiologist at interpreting certain images, it is still going to make some mistakes that humans would not, says radiologist Curtis Langlotz, director of the Center for Artificial Intelligence in Medicine and Imaging at Stanford University. That puts radiologists in the role of evaluating each AI decision—the vast majority of which will be correct—and identifying the rare instances when the algorithm got it wrong.

“This requires a whole mental rewiring,” says radiologist Paul Yi, section chief of intelligent imaging informatics at St. Jude Children’s Research Hospital in Memphis, Tennessee.

Physicians have grown used to overruling computers, but this moment is different. Electronic medical record alerts triggered by rule-based algorithms have been warning physicians for decades about things like potentially dangerous drug interactions. Physicians typically override those warnings about half the time, Langlotz says. “I’m going to get some advice from the computer and I’m going to have to evaluate that in the context of all the other information I have about that patient and just make the best decision,” he says.

In contrast, AI image analysis systems in radiology are usually based on neural networks that can identify tumor subtypes, outline the boundaries of lesions, and perform other diagnostic tasks with high accuracy. Unlike rules-based algorithms, which give answers or prompts that doctors can quickly interpret based on their own medical knowledge, neural networks are referred to as“black box” systems. These AI models typically do not reveal how they reached a decision, which makes a radiologist’s job of deciding whether to veto it much more opaque.

“Is that really an abnormality, or am I missing something that AI with its subtle mind or whatever is identifying?” says Charles Kahn, editor ofRadiology: Artificial Intelligence, a publication of the Radiological Society of North America. “And that is really challenging for us.”

## Veto power

Langlotz gives the example of a theoretical AI tool that can detect 95 percent of the lung nodules on a chest CT, while radiologists are known to detect 90 percent. “Some would say, ‘Oh, the AI is better than the radiologists, therefore we should replace all the radiologists with AI,’” he says. “But I will tell you that the radiologist is going to detect some of that 5 percent that were missed by the machine. And that’s because machine intelligence and human intelligence are different kinds of intelligence.”

AI can examine every pixel on an image without getting tired or distracted and compare it to every other image it has ever encountered. In contrast, radiologists’ understanding of disease allows them to interpret images in ways that AI cannot.

“How do you make sure that when the AI and the radiologists are naturally thinking something different, that the radiologist accepts every time the AI is right and dismisses every time it’s wrong?” says Nina Kottler, chief medical AI officer of Mosaic Clinical Technologies. “It’s not necessarily easy, but there are ways to do it.”

With the goal of creating an ideal AI/human team, radiologists around the world are working to learn how to collaborate with AI so they and their patients can reap its benefits. That collaboration requires dealing withunconscious biasesthat make a physician eitherrely on AI too muchor dismiss its responses inappropriately. So to work with these systems optimally, radiologists need to appreciate the overall reliability of AI while still being able to spot its mistakes.

“It does help to know a little bit about how these systems work so that you can understand better when an algorithm might be leading you astray,” Langlotz says.

Whenever a human or machine makes a yes/no error in the interpretation of a medical image, there are two possible ways to go wrong: A false negative misses the presence of disease, whereas a false positive sees one when it isn’t actually there.

For uncommon diseases—and most diseases are relatively uncommon—any diagnostic will tend to produce a lot of false positives simply because it encounters large numbers of people without the disease, giving it more opportunities to issue false alarms. A physician needs to be able to recognize and overrule these false positives while still correctly identifying the machine’s relatively rare correct diagnosis. Believing too much in the machine’s results—positive or negative—is called automation bias.

But it’s important to avoid accepting false negatives, too. For example, an AI system might miss the presence of blood in the brain on a CT or MRI scan when it’s actually there. Trusting in such oversights is called automation complacency.

“These are both issues of letting the AI change the radiologist’s level of suspicion without realizing it,” Kottler says. Over time, people may start to believe AI’s answers too much. One study found that even experienced radiologists saw bigdrops in the accuracy of their mammographyinterpretation when their decisions were made under the influence of incorrect AI predictions.

On the other hand, the issue of AI distrust is a bit more intuitive. Many people will naturally be suspicious of a new technology—especially one that has been accused of potentially taking their jobs—until it proves its worth. And it doesn’t help that otherwise reliable AI systems make obvious mistakes that are different from human errors. “So you see a silly mistake, a silly false positive, and you’re like, ‘Well, of course the AI is not smart,’ and you could then dismiss it,” Kottler says.

She suggests addressing these biases by monitoring over time how much radiologists agree or disagree with their AI colleagues and intervening if they appear to go too far one way or the other. “If radiologists are accepting the AI result 99 out of a hundred times and we know it’s only 95 percent accurate, we go talk to that rad,” Kottler says.

But simply telling radiologists that an AI tool is accurate 95 percent of the time is not enough, Kottler says. Training is essential so that physicians know what to look for and when. They need to know, for example, that a certain AI tool is going to be wrong on 30 percent of scans if the patient moved in the scanner. Yet more than a quarter of physicians responding to a 2026 American Medical Association survey said they had receivedno training about AI, and only 11 percent said they had received a lot of training.

Kottler also advocates for AI tools to report a confidence estimate for each evaluation instead of a simple yes/no response, because no radiologist can be expected to know the intricacies of multiple AI systems. And those systems are only going to proliferate in number and complexity.

“We are just at the very beginning of understanding how to optimize the human/machine system,” Langlotz says. The important thing for radiologists to appreciate today, he adds, is the same thing he said nearly a decade ago in rebutting the godfather of AI’s prediction: It’s not that AI will replace radiologists.Radiologists who use AI will replace radiologists who don’t.

This story originally appeared in Knowable Magazine. Read the original articlehere.

 Knowable Magazine
 

 Knowable Magazine
 

 Knowable Magazine explores the real-world significance of scholarly work through a journalistic lens.
 

1. 1.Inaudible sounds used to fingerprint browsers catch AliExpress red-handed
2. 2.Ads and tracking infiltrated TVs. Now they're coming for monitors.
3. 3.AI is hitting entry-level jobs hardest, Stanford study finds
4. 4.Data centers become "killer application" for new power transformer tech
5. 5.GM vehicles under federal scrutiny after hundreds of reports

Customize