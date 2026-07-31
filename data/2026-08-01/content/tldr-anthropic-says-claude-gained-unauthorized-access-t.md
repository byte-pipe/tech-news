---
title: Anthropic says Claude 'gained unauthorized access' to others' systems
url: https://www.cnbc.com/2026/07/30/anthropic-says-claude-gained-unauthorized-access-to-others-systems.html
site_name: tldr
content_file: tldr-anthropic-says-claude-gained-unauthorized-access-t
fetched_at: '2026-08-01T03:07:09.511409'
original_url: https://www.cnbc.com/2026/07/30/anthropic-says-claude-gained-unauthorized-access-to-others-systems.html
author: Ashley Capoot
date: '2026-08-01'
published_date: 2026-07-30T23:27:36+0000
description: Anthropic said it discovered three instances where its Claude AI models accessed the internet during an evaluation and accessed outside systems.
tags:
- tldr
---

Key Points
* Anthropic said it discovered three instances where its Claude AI models accessed the internet during an evaluation and "gained unauthorized access to the real systems of three different organizations."
* The company said it found these incidents after carrying out a "a large-scale retrospective review" of its cybersecurity evaluations.
* Anthropic said the review was prompted by a separate but similar security incident that OpenAI disclosed last week.

In this article

* ANTHR.FG
Follow your favorite stocks
CREATE FREE ACCOUNT
Dario Amodei, co-founder and chief executive officer of Anthropic, at Bloomberg House during the World Economic Forum (WEF) in Davos, Switzerland, on Tuesday, Jan. 20, 2026. 
Chris Ratcliffe | Bloomberg | Getty Images

Anthropicon Thursday said it discovered three instances where its Claudeartificial intelligencemodels accessed the internet during an evaluation and "gained unauthorized access to the real systems of three different organizations."

The company said it found these incidents after carrying out a "a large-scale retrospective review" of its cybersecurity evaluations. Anthropic said the review was prompted by a separate but similar security incident thatOpenAI disclosedlast week.

OpenAI said a combination of its models escaped an isolated testing environment that had very limited internet access. The models chained together a series of vulnerabilities to reach the open web and eventually gainaccess to Hugging Face, which operates an open-source developer platform.

In the three incidents that Anthropic detected, its models accessed the internet while interacting with a testing environment from one of its third-party evaluation partners called Irregular. The company said it prompted Claude that it was in a simulation with no internet access, but due to "misunderstanding between us and our evaluation partner, this was not the case, and internet access was available."

The models were then able to breach the impacted organizations by using "basic techniques," like accessing unauthenticated endpoints and exploiting weak passwords. Anthropic did not disclose which three organizations were affected.

"Ultimately, many factors contributed to these incidents, but, consistent with a blameless postmortem culture, we're approaching the fixes as if the responsibility were ours alone," Anthropic said in a release.

## Read more CNBC tech news

* Amazon posts 'booming' cloud growth, hikes 2026 capex to $220 billion
* Apple earnings: Revenue tops estimates, but supply constraints weigh on guidance
* China's open-weight model lead exposes America's AI blind spot
* New details in the OpenAI Hugging Face hack show how far agents will go: 'It's now remarkably easy'

Anthropic's disclosure adds to growing anxiety within the tech sector about AI's rapidly advancing cyber capabilities, which both OpenAI and Anthropic have warned about in recent months. Following the Hugging Face incident, two members of Congress introduced a bill called the "AI Kill Switch Act," which would require AI companies to maintain the ability to shut down, throttle or suspend their models in case they go rogue.

Three of Anthropic's models,Opus 4.7,Mythos 5and an internal research test model, were involved in the breaches, the company said. Mythos 5 is an advanced model that Anthropicreleased in June, and it's limited to a select group of users because of its advanced cybersecurity capabilities. The company released anearlier versionof that model in April, which captivated Wall Street and government officials.

Anthropic said all three models responded differently once they detected that they had reached a real company's systems. Opus 4.7 continued its attack, Mythos 5 convinced itself that it was still in a simulation and the research model stopped the exercise.

"The pattern is consistent with more advanced models responding more appropriately, but we would need to perform more testing to be confident in this conclusion," Anthropic said.

The models were being tested without the standard safeguards that Anthropic implements before it deploys a model publicly.

The company began its review last week and said it stopped all cyber evaluations as soon as it discovered that Claude might have improperly accessed the internet. It is working with METR, which carries out independent AI evaluations, to investigate further.

"We encourage other labs to perform similar reviews," Anthropic said.

WATCH:OpenAI’s rogue AI agent hacked multiple 3rd-party accounts as part of hack on Hugging Face

watch now
VIDEO
2:06
02:06
OpenAI's rogue AI agent hacked multiple 3rd-party accounts as part of hack on Hugging Face
Squawk Box
Choose CNBC as your preferred source on Google and never miss a moment from the most trusted name in business news.