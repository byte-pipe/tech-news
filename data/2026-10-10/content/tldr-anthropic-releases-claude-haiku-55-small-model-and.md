---
title: Anthropic releases Claude Haiku 5.5 small model and halves Sonnet 5.5 cache read prices - SiliconANGLE
url: https://siliconangle.com/2026/10/07/anthropic-releases-claude-haiku-5-5-small-model-and-halves-sonnet-5-5-cache-read-prices
site_name: tldr
content_file: tldr-anthropic-releases-claude-haiku-55-small-model-and
fetched_at: '2026-10-10T22:14:21.091046'
original_url: https://siliconangle.com/2026/10/07/anthropic-releases-claude-haiku-5-5-small-model-and-halves-sonnet-5-5-cache-read-prices
author: Duncan Riley
date: '2026-10-10'
published_date: '2026-10-07T22:28:07+00:00'
description: Anthropic releases Claude Haiku 5.5 small model and halves Sonnet 5.5 cache read prices - SiliconANGLE
tags:
- tldr
---

UPDATED 18:28 EDT / OCTOBER 07 2026

 
AI

### Anthropic releases Claude Haiku 5.5 small model and halves Sonnet 5.5 cache read prices

byDuncan Riley

Anthropic PBC today releasedClaude Haiku 5.5, pricing its newest small model at roughly a quarter of what Haiku 4.5 costs to run.

Claude Sonnet 5.5 is getting cheaper as well, since the company is halving what it charges for cache reads on that model.

Two weeks after Opus 5.5launched Sept. 22, Haiku 5.5 makes three models in the 5.5 generation. Anthropic is aiming it at repetitive work. High-volume summaries and classification are the main target, and coding teams can also use the model as a subagent that Opus 5.5 or Sonnet 5.5 hands smaller tasks to. Because no Anthropic model runs faster at standard speed, the company suggests it for live customer support and browser automation.

Anthropic’s running-cost figure rests on a steep cut to list prices. Haiku 4.5, releasedlast October, costs $1 per million input tokens and $5 per million output. For prompts of up to 100,000 tokens, which Anthropic said covered about 90% of the older model’s requests, Haiku 5.5 is 90% cheaper on input and output alike, at 10 cents and 50 cents per million tokens. Longer prompts get a 50% discount. The 75% average saving the company quotes takes in a new tokenizer that uses slightly more tokens per task. Cost can be tuned further, since Haiku 5.5 is the first Haiku model with an adjustable effort setting.

The 10-cent and 50-cent rates match what OpenAI Group PBC charges for GPT-6 Luna, the low-cost model it launchedlast month. Anthropic’s published benchmarks have Haiku 5.5 ahead of Luna on all six tests where both have a score. On OSWorld 2.1, a test of agents operating a real computer through long multistep tasks, the new model scored 72.4% on the offline subset against 48.9% for Luna. Luna scored 16.4% on the Terminal-Bench 4.0 agentic coding test, less than half the new model’s 39.2%. For complex agentic coding, Anthropic still points customers to Sonnet 5.5 and Opus 5.5.

Asana Inc. was among the customers that tested Haiku 5.5 before release, running it through the evaluation suite for its AI Teammates agent. Task completion latency came in more than 30% lower than with the model Asana uses today, and inference on each agent turn ran up to 2.5 times faster. “It’s a noticeably snappier experience,” said Aaron Vinh, a staff software engineer at the company.

On safety, Anthropic said alignment testing turned up far fewer instances of misaligned behavior than Haiku 4.5 showed. Cybersecurity safeguards on the model allow more defensive work than Sonnet 5.5 permits. Penetration testing is still blocked, as are other techniques attackers are more likely to use, and organizations that need wider access can apply to the Cyber Verification Program Anthropic expandedon Tuesday.

The Haiku launch also came with a price cut for Anthropic’s midsize model. Cache reads on Sonnet 5.5, whichlaunched Sept. 28, drop from 20 cents per million tokens to 10 cents. Because cached tokens account for a large share of what models consume, Anthropic expects the cut to take about 20% off the cost of most agentic work on the model.

Claude Max and Team subscribers will also start receiving monthly application programming interface credits for the Claude Platform this week. A Max 5x subscription comes with $100 a month, double that on Max 20x. Team accounts get up to $500 shared across their users, and the credits can go toward any Claude model.

Haiku 5.5 is available now on the Claude Platform as claude-haiku-5-5 and through Amazon Web Services Inc., Google Cloud and Microsoft Azure.

##### Image: SiliconANGLE/GPT Image 2.5

# A message from John Furrier, co-founder of SiliconANGLE:

Support our mission to keep content open and free by engaging with theCUBE community.Join theCUBE’s Alumni Trust Network, where technology leaders connect, share intelligence and create opportunities.

* 15M+ viewers of theCUBE videos, powering conversations across AI, cloud, cybersecurity and more
* 11.4k+ theCUBE alumni— Connect with more than 11,400 tech and business leaders shaping the future through a unique trusted-based network

### Are you an AWS customer?Support SiliconANGLE financially by buying your AWS services from ourMarketplace portal page and links:https://siliconangle.com/aws-marketplace/

 

##### About SiliconANGLE Media

SiliconANGLE Media is a recognized leader in digital media innovation, uniting breakthrough technology, strategic insights and real-time audience engagement. As the parent company of 
SiliconANGLE
, 
theCUBE Network
, 
theCUBE Research
, 
CUBE365
, 
theCUBE AI
 and theCUBE SuperStudios — with flagship locations in Silicon Valley and the New York Stock Exchange — SiliconANGLE Media operates at the intersection of media, technology and AI.

Founded by tech visionaries John Furrier and Dave Vellante, SiliconANGLE Media has built a dynamic ecosystem of industry-leading digital media brands that reach 15+ million elite tech professionals. Our new proprietary theCUBE AI Video Cloud is breaking ground in audience interaction, leveraging theCUBEai.com neural network to help technology companies make data-driven decisions and stay at the forefront of industry conversations.

##### LATEST STORIES

* AI reshapes professional services around trust and business outcomes
* What to expect during LogicMonitor’s Elevate event: Join theCUBE Oct. 14
* The AI control gap: Who gets to say ‘It’s safe'?
* Oxide Computer raises $445M to step up data center rack production
* Warehouse robot maker Ultra Robotics bags $62M
* IBM connects enterprise AI orchestration to production readiness ahead of TechXchange

##### LATEST STORIES

* AI reshapes professional services around trust and business outcomesAI- BYCHERYL KNIGHT.2 HOURS AGO
* What to expect during LogicMonitor’s Elevate event: Join theCUBE Oct. 14CLOUD- BYCHERYL KNIGHT.2 HOURS AGO
* The AI control gap: Who gets to say ‘It’s safe'?AI- BYDAVE VELLANTE.5 HOURS AGO
* Oxide Computer raises $445M to step up data center rack productionINFRA- BYMARIA DEUTSCHER.21 HOURS AGO
* Warehouse robot maker Ultra Robotics bags $62MIOT- BYMARIA DEUTSCHER.23 HOURS AGO
* IBM connects enterprise AI orchestration to production readiness ahead of TechXchangeAI- BYVICTORIA GAYTON.23 HOURS AGO