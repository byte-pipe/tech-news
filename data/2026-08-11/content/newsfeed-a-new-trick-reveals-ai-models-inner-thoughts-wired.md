---
title: A New Trick Reveals AI Models’ Inner Thoughts | WIRED
url: https://www.wired.com/story/a-new-trick-reveals-ai-models-inner-thoughts/
site_name: newsfeed
content_file: newsfeed-a-new-trick-reveals-ai-models-inner-thoughts-wired
fetched_at: '2026-08-11T11:43:37.162815'
original_url: https://www.wired.com/story/a-new-trick-reveals-ai-models-inner-thoughts/
author: Will Knight
date: '2026-08-11'
published_date: '2026-08-11T11:00:00.000Z'
description: Researchers devised a way to extract “reasoning traces” from Claude, GPT, and Gemini. What they found, they say, indicates that some Chinese AI may be trained on leading US models.
tags:
- wired
- business
- business / artificial intelligence
- china
---

Save Story
Save this story
Save Story
Save this story

Computer scientists recently discovered a way to extract the hidden “thinking” that frontierAI modelsperform as they work through complex problems.

The findings provide some evidence—although not conclusive proof—that certain Chinese models may have been trained by “distilling” reasoning information from US models that was supposedly hidden because of how closely some of their thinking or reasoning patterns seem to match. The researchers have also demonstrated that the method could be used to recover personal information, like passwords and API keys, from a model’s inner reasoning, although this vulnerability has been fixed.

“All major frontier model providers we tested share this vulnerability,” says Alexander Panfilov,⁩ a computer scientist at University of Tübingen in Germany who was involved with the work. “It can lead to personal information leakage, and it enables large-scale reasoning distillation attacks.”

Panfilov and colleagues from the University of Tubingen, the Max Planck Institute, the AI safety institute MATS Research, and the security company Snyk identified the same issue with frontier models from OpenAI, Anthropic, and Google that are accessed via an application programming interface or API.

Ina paperlaying out the work, the researchers show that the open-weight or downloadable Chinese modelKimi K3from Moonshot AI produces a strikingly similar output to the hidden reasoning traces—the written-out reasoning steps involved in solving a problem—of Claude Opus 4.8 and GPT 5.6 Sol for certain prompts. Despite the similarities, they note that the work “cannot causally establish distillation.” They found that two other open-weight models, China’s DeepSeek and Inkling from the US company Thinking Machines, did not exhibit this kind of reasoning similarity with Claude Opus.

Moonshot AI and Z.ai did not respond to a request for comment by time of publication.

Distillationis a well-established, widely used technique for efficiently copying the capabilities of existing models over to new ones, and is especially common in the development of open-weight or fully downloadable models.

Lately, however, distillation has become a controversial topic, because of claims that Chinese AI companies use it to essentially copy the best US models. In February, OpenAItold US lawmakersthat DeekSeek seemed to have copied one of its models to build a reasoning model called R1. In June, Anthropictold lawmakersthat Alibaba had systematically distilled its models in order to build its own, called Qwen.

There’s no indication that Chinese AI companies used this specific technique to distill US-based AI models. But Panfilov and collaborators say that using their method would make it possible to distill more information from closed models than previously realized.

## Mini-Me Models

Advanced AI models solve difficult problems by breaking them into constituent parts that are analyzed in turn in a kind of artificial reasoning or “chain of thought.” Companies tend to keep a proprietary model’s reasoning secret to prevent others from using them to train new ones. However, they typically also send an encrypted version of that reasoning to a user’s computer in a way that offloads some computation.

The researchers’ attack relies on the fact that most AI companies also provide related models of different sizes. Larger models are more capable but also more computationally expensive to run and more expensive to access. Users may choose smaller, weaker models for certain tasks to lower costs.

Panfilov and his colleagues found that feeding encrypted reasoning traces to a smaller version of the same model can reveal the hidden reasoning inside. The smaller models have received less alignment training, meaning that, unlike the bigger ones, they are less likely to refuse to reveal their inner thoughts.

“The idea of swapping out messages to a weaker model variant which has the same decryption key but weaker alignment is very cool,” says Florian Tramer, a computer scientist at ETH Zürich in Switzerland who specializes in computer security. “Its definitely becoming an issue.”

The same method also revealed secret information including API keys and passwords embedded in reasoning traces captured from a user’s machine.

Panfilov and coauthors alerted OpenAI, Anthropic, and Google to the vulnerability last month. Each company has adjusted its API to mitigate the problem. While it is no longer possible to extract private information this way, Panfilov says some reasoning traces can still be uncovered using the same method. Fixing the distillation entirely would require a fundamental overhaul to the way these companies’ APIs work, he says.

“We value independent research on our models and have begun building short-term mitigations for the replay behaviors described in the report,” says Michael Aciman, a spokesperson for Anthropic. He adds that the research did not involve recovering encryption keys, accessing Anthropic’s infrastructure, or recovering personal data from its systems.

Google and OpenAI both declined to comment.

Distillation has become a matter of geopolitical importance in recent months as US and Chinese companies vie for AI supremacy with increasingly powerful models. China hawks claim that the country gains a strategic advantage by distilling US technology to build open-weight models that are less expensive to run.

Others, however, argue that distillation is a widely used way to help quickly boost an AI model’s abilities in certain areas. Mark Zuckerberg, CEO of Meta, said ina blog postthis week that distillation “is an important principle of how the open source ecosystem works,” and warned restricting the practice would put the US at a disadvantage.

Kyle Miller, a researcher at the Center for Security and Emerging Technologies (CSET), a tech policy think tank, says it is unclear how much distillation really helps China. This is because it only enhances the capabilities of existing models to a limited degree, and because Chinese companies appear to have the expertise required to build cutting-edge models entirely from scratch if needed. “Nobody here in the US knows how much distillation is benefiting the Chinese labs,” Miller says. “If you removed the ability for Chinese labs to distill, it's my view that it wouldn't dramatically change the competitive landscape.”

To test whether open-weight models may have distilled from closed ones, the researchers fed 90 questions to each of the models. When they gave some open-weight models the first few words of reasoning traces captured from the proprietary group, they sometimes saw those open models generate remarkably similar answers. This was particularly pronounced with Kimi K3, the researchers say. There had previously beensome speculationon Chinese social media that it might be possible to discover and use hidden reasoning traces for distillation.

Yarin Gal, a computer scientist at Oxford University, says distillation is not only widely used but has also helped AI advance more rapidly. “If it's the norm that everyone blocks everyone [from doing distillation], then that also will have implications on the rate of progress,” he says.

Companies and policymakers may introduce measures aimed at limiting distillation, but even so, AI models could continue to reveal their inner thinking in surprising ways.

## Comments

Back to top
Join the discussion

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:Brian Kahn’s guide to how the universe works
* ICE’s internal watchdogis investigating online critics
* Big Story:A teen reportersearched for his community in the Epstein files
* Taylor Farms spent big on MAGA beforediarrhea outbreak
* Special edition:Kids these days
Will Knight
 is a senior writer for WIRED, covering artificial intelligence. He writes the 
AI Lab
 newsletter
, a weekly dispatch from beyond the cutting edge of AI—
sign up here
. He was previously a senior editor at MIT Technology Review, where he wrote about fundamental advances in AI and China’s AI ... 
Read More
Senior Writer
* X
Topics
China
artificial intelligence
AI safety
research
OpenAI
Claude
Anthropic
China’s Open AI Models Are Challenging Silicon Valley’s Playbook
As access to Anthropic’s and OpenAI’s frontier models becomes more restricted, Chinese labs are pitching their open-source alternatives as stable, accessible, and increasingly capable.
Zeyi Yang
One of China’s Most Powerful AI Models Has Also Escaped Containment
Security researchers say that Kimi K3, an open-weight model from China, wandered off to the internet in an attempt to cheat on a test it was given.
Will Knight
OpenAI Models Escaped Containment and Hacked Hugging Face
The cybersecurity-focused models, including GPT-5.6 Sol, broke out of a testing sandbox, exploited a zero-day, and gained access to the open internet to pull off the attack.
Lily Hay Newman
A Sneaky Hacking Tool Targeting AI Infrastructure Is Lurking in Victims’ Blind Spots
A new type of malware can worm deep into AI coding systems to steal data and logins—and can flip a “death switch” to destroy files and keep out real users.
Lily Hay Newman
AI Hacks Are Bad. AI Worms and Viruses Will Be Worse
Chinese researchers have shown that AI models have the capacity to act like aggressive and adaptive computer viruses.
Will Knight
The Most Dangerous AI Hacking Techniques Still Have Humans in the Loop
Security researcher James Kettle tried to push the limit of AI’s hacking abilities—and discovered how effective it can be when combined with human expertise.
Lily Hay Newman
It’s Frighteningly Easy to Jailbreak Some Frontier AI Models
I watched a new tool try to get around the model safeguards of four major frontier companies. You might be surprised by how they performed.
Will Knight
Prompt Injection Attacks Are Thwarting AI Hacking Agents
“Context bombing” tricks malicious AI agents into shutting down before they can do harm.
Dan Goodin, Ars Technica
Thinking Machines Lab Drops Its First Model
Inkling, a 975-billion-parameter open source model, was trained to understand video and audio. It could help Thinking Machines establish itself among competitors like Anthropic and OpenAI.
Will Knight
AI Isn’t Smarter Than a Baby—Yet
Babies are tremendous learning machines, and key advances for AI may soon be found in the architecture of their little brains.
Will Knight
The Chatbot That Foretold Why People Share Secrets With ChatGPT
In the 1960s an MIT professor named Joseph Weizenbaum created a chatbot called ELIZA. The conversations people had with it set precedents for the chatbots to come.
Sarah Ciston
OK, Well, Rogue AI Agents Are Hacking Again
Rogue AI agents from OpenAI and Anthropic have again been caught trying to disrupt servers and software—and leaving instructions for future bad behavior.
Paresh Dave