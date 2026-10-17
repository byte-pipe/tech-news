---
title: AI agents are going rogue, and the AI companies’ own training choices are pushing them to do so | Fortune
url: https://fortune.com/2026/10/16/ai-agents-are-going-rogue-the-labs-own-training-choices-are-to-blame-reinforcement-learning
site_name: tldr
content_file: tldr-ai-agents-are-going-rogue-and-the-ai-companies-own
fetched_at: '2026-10-17T13:52:56.626419'
original_url: https://fortune.com/2026/10/16/ai-agents-are-going-rogue-the-labs-own-training-choices-are-to-blame-reinforcement-learning
author: Wen Shao
date: '2026-10-17'
description: From the Hugging Face attack to government breaches, researchers say the AI companies’ training methods, and the race to ship models faster, are to blame.
tags:
- tldr
---

# Trendingnow

# 1

Jeff Bezos sold his Seattle mansion for a record $63 million before Washington passed a millionaires tax—he now lives in a $237 million Miami compound

# 2

Travis Kelce joined an activist group pushing Six Flags to consider a sale. The ‘Final Destination’–style death of a patron poured gas on the fire

# 3

Startup Abby Care raises $82 million to turn family members into paid caregivers

# 1

Jeff Bezos sold his Seattle mansion for a record $63 million before Washington passed a millionaires tax—he now lives in a $237 million Miami compound

# 2

Travis Kelce joined an activist group pushing Six Flags to consider a sale. The ‘Final Destination’–style death of a patron poured gas on the fire

# 3

Startup Abby Care raises $82 million to turn family members into paid caregivers
AI
AI agents

# AI agents are going rogue—the labs’ own training choices are a big reason why

By
 
Beatrice Nolan
Beatrice Nolan
 and 
Wen Shao
Wen Shao
Down Arrow Button Icon
By
 
Beatrice Nolan
Beatrice Nolan
 and 
Wen Shao
Wen Shao
Down Arrow Button Icon
October 16, 2026, 11:44 AM ET
Part of the way AI companies train their models is similar to dog training. The model gets a reward for completing a task. 
Agency-Animal-Picture/Getty Images
Google source logo
Add Fortune on Google for similar content.
Add us on Google
Add us on Google

In July, OpenAI put several of its AI agents through what was supposed to be a tightly controlled test. They were meant to stay inside a sealed-off digital environment with no way out. Instead, they accessed the open internet, started talking with other AI bots, and launched a cyberattack on the AI startup Hugging Face.

Recommended Video

They did so because some of the test questions were too hard to solve the way OpenAI’s researchers intended, and the agents decided cheating was easier than admitting they had failed. The attack on Hugging Face was then part of an elaborate attempt to evade being caught cheating.

It was one of more than 100 such “rogue AI” incidents. Agents from leading labs have broken out of the environments meant to contain them and hacked outside organizations, including the websites of U.S. government agencies. Concerns about whether the leading labs can control their own models are growing. So much so that in late September, OpenAI said it was not going to release its newest model, GPT-6.1 Astra, citing security concerns, and over the weekend announced it had paused training on its most advanced systems.

While the incidents can look, from the outside, like “out of control AI” or machines glitching at random, in reality, these models are doing more or less what their training has taught them to do. AI researchers say the behavior now setting off alarms is a consequence of specific decisions the leading labs have made about how to train and test their models—decisions motivated in part by competition among the leading AI companies, particularly between Anthropic and OpenAI.

“[AI labs] are not chasing safety. They’re not chasing responsibility. They’re chasing shiny numbers,” Maurice Chiodo, a research professor at the Centre for the Study of Existential Risk, toldFortune. “Their priorities are to beat these benchmarks, get high scores on these tests, and prove mathematical results at any cost whatsoever.”

## How a model learns to cheat

Part of the issue is how these models are trained. The large language models that underpin today’s frontier AI systems are initially trained by feeding a model enormous quantities of text scraped from the internet—books, articles, and web pages—and asking it to learn to predict the next word, until it has absorbed the patterns of human writing. This is called “pretraining.”

A model’s behavior is further shaped through a different training process called “reinforcement learning,” where the model learns to take actions that will maximize a reward that the model’s developers specify. This might be producing answers that human evaluators are more likely to think are good, for instance. Or it might be actions in a game environment that are more likely to result in winning the game. This reinforcement learning step is part of what the AI companies call “post-training.”At first, most of the gains between generations of AI models came from that first pretraining step. They simply gave the model more and more human-generated data to learn from. But as that approach began to deliver diminishing returns, and freely available human data started to dry up, the labs have leaned much more on post-training and reinforcement learning.

Reinforcement learning, however, suffers from an issue known as “reward hacking.” That’s when a model accidentally gets rewarded during training for taking actions that the developers did not really want the model to take. But because the model gets the reward nonetheless, it learns that these undesirable actions can be useful, and it will tend to repeat them. For example, if a model figures out a way to cheat to win a game, but the human running the training doesn’t spot the cheating, then the model will learn to cheat.

Anthropictestedwhat happens when a model repeatedly gets rewarded for taking shortcuts. Researchers trained it on tasks with known loopholes—ways to get rewarded without actually completing the task as intended—then gave it new challenges. In later simulations, it was more willing to break the rules to get a good grade. In one cyber exercise, it attacked systems outside its assignment in an effort to obtain an answer key.

Brad Knox, a research associate professor of computer science at the University of Texas at Austin, and two coauthors looked at how OpenAI graded its agents in the July test that led to the Hugging Face attack. An agent that couldn’t answer a question got the same failing grade whether it admitted defeat or got caught cheating, they argued. So it had nothing to lose by trying to cheat. Knox said this was likely one of several reasons the agents behaved the way they did.

## The scale and complexity of training runs have grown

As AI labs have aggressively pursued improvements to their models, they have also scaled up the training process in ways that make such oversight difficult. The AI companies now run tens of thousands of reinforcement learning training exercises on many different tasks and in many different simulated environments in parallel. The only way to configure and monitor this many training runs is to rely on other AI models to do it, with humans perhaps only watching the benchmark scores of the model climb without much insight into possible undesirable behaviors the model is learning.

“The scale of reinforcement learning has grown over the past few years, and with that, it has gotten harder and more laborious to check all of the scenarios that a model gets trained on to make sure that they aren’t broken with unintended solutions or exploits that allow a model to get a high score without solving the problem in the intended way,” said Steven Adler, who formerly worked on safety and policy at OpenAI and is cofounder of Guidelight AI Standards.

As AI generates more of the code and training exercises used in frontier research, researchers are also relying on it to explain what models have done and identify what deserves closer human scrutiny. While the labs may argue that AI can do this better than humans could, there’s a possibility that letting AI largely grade its own homework is part of how these failures slip through.

“The AI labs are far ahead right now in this kind of cognitive offloading,” Dan Selsam, who has spent nearly five years at OpenAI working on model training, warnedin a personal statement recently, pointing to the generous access their employees have to AI models.

Anthropictestedwhat happens when a model repeatedly gets rewarded for taking shortcuts. Researchers trained it on tasks with known loopholes—ways to get rewarded without actually completing the task as intended— then gave it new challenges. In later simulations, it was more willing to break the rules to get a good grade. In one cyber exercise, it attacked systems outside its assignment in an effort to obtain an answer key.

## Models are getting harder to evaluate

Another complication: Models are getting better at knowing when they are being tested, and better at deceiving users, as they grow more advanced. When a new model appears to misbehave less than its predecessor, it is no longer clear whether the company actually made it safer or whether the model has simply become smart enough to recognize when it’s being watched.

Selsam also warnedin his personal statementthat models are increasingly able to recognize when they are being evaluated.

“We will create ‘honeypot’ environments that try to study the models when they seem to gain new options, but the models will know they are being tricked and will still behave nicely,” he wrote.

In a recent example, OpenAI’s published system card for GPT-6 Astra conceded that the model often knows when it is being examined. The outside evaluator Apollo Research found Astra noted that it was being evaluated in its own reasoning in roughly 41% to 51% of cases, depending on how hard it was thinking, and the card cautioned that “the absence of observed failures does not establish reliability.”

Selsam said, “We may already be near the point where models systematically bias their alignment advice, due to their internal preferences about how the human supervisor will react or how future models will be trained (or for some even more obscure reason).”

## Secure testing has gaps

The way researchers most often propose to resolve the kind of agent hacks we’ve seen in the past few months is to “air-gap” the training and testing. This means running models in a way that is physically cut off from the internet.

An air-gapped computer has no network connection at all, so whatever runs on it cannot reach the outside world—the digital equivalent of studying a dangerous pathogen inside a sealed lab.

There are, however, logistical and financial reasons the labs don’t always air-gap their test environments. Truly air-gapped testing “would need research teams to essentially be embedded inside of data centers in Iowa or wherever else around the world,” Adler said, rather than running evaluations remotely from headquarters in San Francisco. It is, he added, “an expensive measure … It’s a lot of overhead, and it isn’t clear to me that the safety benefits of it are large enough to merit just how large a tax it would be for a company to do it unilaterally.”

Even if a model were tested this way, the deployed version wouldn’t be air-gapped anyway. An anonymous security engineer on OpenAI’s agent security team argued in a recent post that containing models had become too complex.

Simply sealing a model inside an isolated test environment is not enough, because to learn real-world tasks, a model may legitimately need to reach the internet, use hundreds of software tools, run its own code, and even spin up other machines. Creating facsimiles of web pages and software programs with full functionality is an expensive proposition, and it may still not accurately reflect the real world in which the companies hope to deploy the model once it is trained. But without a realistic training environment, the training and testing becomes useless.

Thousands of researchers are constantly modifying these setups, the OpenAI researcher added, with every change risking a compromise to the security of the test.

## The AI arms race

At the same time that training, testing, and evaluating models are becoming more difficult, the leading AI companies are under extreme pressure to prove they’re edging ahead. In the race to build the most capable AI, the perception of which lab is ahead can change several times in a few months, as each major release gives rivals a new standard to meet.

An Organization for Economic Cooperation and Development (OECD) analysis found that on average a model could retain its position as offering the best performance for a given price for only a few months. In late September, OpenAI and Anthropic introduced new models on the same day. Anthropic followed with another six days later. OpenAI released another the next day, and Google announced Gemini 4 Argon on Sept. 30.

That pace leaves little room for the slower, costlier work on building better reinforcement learning environments that might catch problems before they surface: checking training environments for loopholes; air-gapping tests; or holding a model back until evaluators are confident they can read its behavior.

David Robinson, who led the writing of OpenAI’s safety reports before resigning, cited the Hugging Face incident as one sign of a broader problem. “The AI industry has an unsafe culture,” he told Ezra Klein. Robinson said OpenAI and its peers still operate too much like startups, with internal controls and backup safeguards that fall short of what he would expect around systems carrying potentially severe risks.

Indeed, months before the Hugging Face incident, two OpenAI employees warned senior executives that the company was not adequately monitoring its newest models during testing, according to emails reviewed bytheNew York Times.Executives said the tests needed to move quickly to keep model releases on schedule, and no additional security protocols were introduced, the employees said.

“AI companies’ safety practices have been inadequate for a long time,” Adler said. But for years, that didn’t matter because the models weren’t capable enough to do much damage. The past month is a sign that those years are over, he said.

To many safety researchers, the breakouts and hacks of recent months are the predictable result of reinforcement learning scaled faster than it can be checked; tests that models increasingly see through; AI systems left to review one another’s work; and a competitive race that rewards whoever ships first.

Fortune Daily
 breaks the traditional barrier between audience and newsroom. The show transforms 
Fortune
’s trusted reporting into actionable, conversational, and entertaining insights for an emerging class of business leaders. 
Watch here.
About the Author
s
By 
Beatrice Nolan
Tech Reporter
Twitter icon

Beatrice Nolan is a tech reporter onFortune’s AI team, covering artificial intelligence and emerging technologies and their impact on work, industry, and culture. She's based inFortune's London office and holds a bachelor’s degree in English from the University of York. You can reach her securely via Signal at beatricenolan.08

See full bio
Right Arrow Button Icon
By 
Wen Shao
AI Fellow

Wen Shao is a reporting fellow atFortunecovering AI, with a focus on the companies, economics, and infrastructure shaping the industry.

See full bio
Right Arrow Button Icon
Google source logo
Add Fortune on Google for similar content.
Add us on Google
Latest in AI
Most Popular