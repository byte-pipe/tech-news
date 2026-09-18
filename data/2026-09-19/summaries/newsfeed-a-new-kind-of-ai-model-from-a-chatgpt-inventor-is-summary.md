---
title: A new kind of AI model from a ChatGPT inventor is thrilling developers | TechCrunch
url: https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/
date: 2026-09-18
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-09-19T06:01:12.935369
---

# A new kind of AI model from a ChatGPT inventor is thrilling developers | TechCrunch

# A new kind of AI model from a ChatGPT inventor is thrilling developers | TechCrunch

## Overview
- Diogo Almeida, former OpenAI researcher and RLHF inventor, left OpenAI to address the mismatch between human‑language‑optimized models and automation needs.  
- His startup, TypeSafe AI, released **Jev**, a transformer‑based model that does not generate text but outputs calibrated probability decisions.  
- By avoiding language generation, Jev is cheap, fast, and eliminates hallucinations, making it attractive for software automation.

## Key Features of Jev
- Produces probability scores (“calibrated decisions”) instead of text tokens.  
- Input tokens are billed per billion, while output tokens are free.  
- Low latency and low cost enable high‑throughput usage.  
- Cannot hallucinate because outputs are predefined by the user.  
- Trained exclusively on synthetic data using “reinforcement learning from calibrated decisions,” a technique Almeida claims surpasses RLHF.

## Developer Adoption
- High demand caused a temporary API outage due to overwhelming traffic.  
- Vercel replaced OpenAI’s Luna classifier with Jev, achieving 5‑18× faster results and higher accuracy.  
- Bryo AI CTO Nikhil Mudholkar found Jev slightly less accurate than Gemini for email classification but 10‑20× cheaper, praising its confidence scores for workflow automation.  

## Use Cases
- **Software automation**: Replace LLM classifiers with a cheaper, more reliable decision engine.  
- **Safety monitoring**: Act as a lightweight guard for LLM agents, detecting jailbreak attempts without the expense of running another LLM.  
- **Model routing**: Quickly decide which workload should be sent to a larger model, reducing overall compute costs.  
- **Future modalities**: TypeSafe plans to expand Jev into other data types beyond text.

## Future Outlook
- Almeida named the model after economist William Stanley Jevons, emphasizing that cheaper intelligence should lead to widespread, emergent deployment similar to the early internet.  
- He keeps the architecture details private, though observers suspect it builds on an open‑weight LLM.  
- Competitors are expected to create similar “System One” models once Jev’s utility is proven.  
- TypeSafe positions itself as a “Frontier Lab” focused on delivering practical intelligence rather than speculative hype.