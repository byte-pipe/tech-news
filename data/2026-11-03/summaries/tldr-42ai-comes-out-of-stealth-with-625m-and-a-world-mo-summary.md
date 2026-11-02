---
title: "42AI comes out of stealth with $62.5M and a world model that can 'predict human behavior' | TechCrunch"
url: https://techcrunch.com/2026/11/02/42ai-comes-out-of-stealth-with-62-5m-and-a-world-model-that-can-predict-human-behavior
date: 2026-11-03
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-03T06:08:01.301674
---

# 42AI comes out of stealth with $62.5M and a world model that can 'predict human behavior' | TechCrunch

# 42AI emerges from stealth with $62.5M seed and a “behavioral world model”

## Core technology
- Develops a “behavioral world model” that predicts the probability of an individual’s decision by modeling underlying psychological tendencies rather than just past actions.  
- Uses a transformer‑based world model to generate probability distributions and a separate language model to produce explanations.  
- Feeds diverse data points into the model: sentiment, voice tone, support‑call frequency, KYC/onboarding steps, transaction history, market conditions, etc.  
- Converts observations into mathematical trait representations; training rewards preserve a person’s consistent tendencies (e.g., risk‑aversion).

## Development and data foundation
- Three‑year R&D effort combining psychology, neuroscience, genetics, and advice from experts including Nobel laureate Dan Shechtman.  
- Conducted psych assessments on thousands of people, then added government and biobank datasets covering >2 million individuals; customer datasets now approach 30 million profiles.  
- Model operates without personally identifiable information, creating behavioral profiles from linked activity while never “knowing” the individual’s identity.

## Performance and live deployments
- Deployed with roughly ten large financial brokerages to manage liquidity, margin requirements, and dynamic hedging exposure.  
- Claims 98 % accuracy in predicting whether trading flows fall within a forecasted range; F1 score of 0.8‑0.85 for predicting trade direction and volume.  
- Generates “seven‑figure” revenue; one brokerage reports about $30 million of additional value from the platform’s hedging recommendations.

## Funding details
- Raised $62.5 million in seed funding from the founders and Infinity Group (chaired by co‑founder Amit Gal‑Or’s father, Amir Gal‑Or).  
- Funding was spread over three years and not solely from external investors; the company plans to raise additional capital.

## Planned expansion and use cases
- Exploring applications beyond finance: gaming, fraud prevention, cybersecurity, and eventually enabling robots and AI agents to understand human behavior.  
- Acknowledges that each new domain requires training on specific rules and contextual data.

## Ethical and regulatory concerns
- Recognizes the risk that brokerages could exploit predictive insights for unfair advantage over their customers.  
- Points to existing regulations, internal monitoring, and an ethics committee as safeguards, though concrete enforcement mechanisms are not detailed.  
- Founders assert that the technology itself is part of the solution to mitigate such risks.