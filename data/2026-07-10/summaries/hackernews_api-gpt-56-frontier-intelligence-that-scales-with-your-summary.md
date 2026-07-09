---
title: GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI
url: https://openai.com/index/gpt-5-6/
date: 2026-07-10
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-10T09:10:01.209288
---

# GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI

# GPT‑5.6: Frontier intelligence that scales with your ambition

## Launch overview
- OpenAI releases the GPT‑5.6 family for general availability after a limited preview.  
- Three models are offered:
  - **Sol** – flagship model with highest capability and efficiency.  
  - **Terra** – balanced model for everyday work.  
  - **Luna** – most cost‑efficient model.  

## Performance and efficiency
- Sol achieves state‑of‑the‑art results in coding, knowledge work, cybersecurity, and science while using fewer tokens and lower estimated cost than prior and competing models.  
- On the “Agents’ Last Exam” benchmark (55 professional fields), Sol scores 53.6, surpassing Claude Fable 5 by 13.1 points and beating it at roughly one‑quarter the cost.  
- Terra and Luna outperform Fable 5 at about one‑sixteenth the cost.  
- On the Artificial Analysis Intelligence Index, Sol with max reasoning is within one point of Fable 5, completes tasks 61 % faster, and costs about half as much.  

## Ultra mode and multi‑agent coordination
- **Ultra** is the highest‑capability setting that runs multiple agents in parallel to accelerate complex tasks.  
- Ultra’s default four‑agent configuration improves score‑latency trade‑offs on benchmarks such as BrowseComp, SEC‑Bench Pro, and Terminal‑Bench 2.1.  
- A 16‑agent configuration further pushes results upward and leftward on the frontier.  
- Developers can access ultra‑like behavior via the multi‑agent beta in the Responses API.  

## Safety and evaluation
- GPT‑5.6 incorporates OpenAI’s most robust safeguards to date, aiming to resist determined misuse while preserving legitimate use.  
- The models underwent extensive human red‑team testing and large‑scale automated evaluation, with input from expert organizations and trusted partners.  
- Protection layers include model‑embedded safeguards, real‑time checks, monitoring, and access controls calibrated to trust and risk.  

## Benchmark highlights
- **Coding**: Sol with max reasoning reaches 80 on the Artificial Analysis Coding Agent Index, 2.8 points above Fable 5, using less than half the output tokens, less than half the time, and about one‑third the cost.  
- Terra scores just above Fable 5; Luna outperforms Opus 4.8, each with roughly one‑third the latency, half the output tokens, and about one‑quarter the estimated cost.  
- New state‑of‑the‑art results on Terminal‑Bench 2.1 and DeepSWE, measuring complex command‑line workflows and long‑horizon engineering.  
- Programmatic Tool Calling in the Responses API enables lightweight programs to coordinate tools, filter intermediate data, and adapt workflows with fewer token round‑trips.  

## Partner feedback
- **Cursor** (Oskar Schulz): “GPT‑5.6 is one of the strongest models we’ve tested on CursorBench, delivering solid results in early evals.”  
- **Qodo** (Itamar Friedman): “Strongest model on our agentic code‑review tests, beating GPT‑5.5 on F1 while using ~3× fewer tokens per PR.”  
- **Notion** (Simon Last): “Sol is the most tenacious problem‑solver we’ve seen; Terra and Luna punch well above their price.”  
- **Cognition** (Scott Wu): “Top‑tier coding‑agent performance with very strong cost efficiency.”  
- **Rogo** (Alex Wang): “Improved rubric quality by 6.2 points and answer accuracy by 3.6 points versus GPT‑5.5; 24 % fewer output tokens and 28 % faster with Programmatic Tool Calling.”  
- **Ramp** (Ian Tracey): “Feels less like a chat assistant and more like an end‑to‑end technical operator.”  
- **Shopify** (Shane Moran): “Followed multi‑stage workflow intent better than GPT‑5.5, consistently produced accurate GitHub references.”  
- **Cisco** (Arjun Sambamoorthy): “Stays focused through long‑running tasks, produces clear reports and intuitive diagrams that accelerate research and design.”  

## Summary
GPT‑5.6 introduces a tiered family of models that deliver higher intelligence per token, stronger performance‑per‑dollar, and on‑demand capability through ultra multi‑agent coordination. The launch is backed by extensive safety testing and validated by a range of industry partners across coding, finance, legal, and infrastructure domains.