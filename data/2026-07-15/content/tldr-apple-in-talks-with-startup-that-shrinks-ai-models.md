---
title: Apple in talks with startup that shrinks AI models to run on an iPhone
url: https://www.cnbc.com/2026/07/14/apple-prismml-ai-compression-iphone.html
site_name: tldr
content_file: tldr-apple-in-talks-with-startup-that-shrinks-ai-models
fetched_at: '2026-07-15T19:31:00.781568'
original_url: https://www.cnbc.com/2026/07/14/apple-prismml-ai-compression-iphone.html
author: MacKenzie Sigalos
date: '2026-07-15'
published_date: 2026-07-14T17:00:20+0000
description: PrismML says its compressed version of Alibaba’s Qwen model uses up to 15 times less memory, potentially advancing Apple’s AI push.
tags:
- tldr
---

Key Points
* Apple is evaluating PrismML’s technology, which the startup says can shrink powerful AI models enough to run directly on an iPhone while using up to 15x less memory.
* The breakthrough could help Apple make Siri faster and more private by keeping more AI processing on-device instead of sending requests to the cloud.
* If PrismML’s claims hold up in real-world testing, the technology could reshape demand for memory and datacenter compute — though analysts say AI will still require plenty of chips.

In this article

* AAPL
Follow your favorite stocks
CREATE FREE ACCOUNT
watch now
VIDEO
1:43
01:43
Apple in talks with startup that shrinks AI models to run on an iPhone
TechCheck

Appleis in talks with a small Silicon Valley company that says it can shrink powerfulartificial intelligencemodels enough to run directly on an iPhone, the startup's CEO told CNBC.

PrismML, a Khosla Ventures-backed spinout from the California Institute of Technology, publicly released compressed versions of Alibaba's open-source Qwen model on Tuesday. The company said it reduced the model from roughly 54 GB to less than 4 GB, allowing all 27 billion of its parameters to run on an iPhone 15 or newer.

PrismML CEO Babak Hassibi told CNBC that Apple and other companies have been evaluating the startup's models and measuring their speed, energy efficiency and performance on devices.

"They're really evaluating our technology right now," Hassibi said of Apple.

He characterized the discussions as very early and said it remains unclear where they will lead, but that "things are progressing nicely."

Apple did not immediately respond to a request for comment.

The Informationpreviously reported the PrismML breakthrough.

The release comes one day after Apple opened the public beta of iOS 27, giving iPhone owners their first broad access to the company's long-delayed overhaul of Siri. Apple is trying to make Siri more competitive with assistants fromOpenAIandAnthropicwhile keeping more personal information and AI processing on the device.

The company's approach could address one of the central constraints facing Apple's AI strategy. The most capable models typically require too much memory and processing power to run on a smartphone.

Apple can send complex requests to cloud-based models, but running more AI directly on the iPhone would reduce the delay associated with sending data to a remote server, lower cloud-computing costs and support the company's privacy pitch. It would also allow certain features to work without an internet connection.

watch now
VIDEO
3:04
03:04
Apple says OpenAI stole its secrets to build rival hardware
Fast Money

Carolina Milanesi, president and principal analyst at Creative Strategies, said smaller models could let Apple move more demanding features onto the iPhone, including computational photography, video generation and health or fitness tools that rely on sensitive personal data.

"The more you can do on device, the better it is," she said, pointing to health and medication data that users would want to keep private.

PrismML said it shrinks AI models by drastically simplifying how their internal information is stored — reducing each value from 16 bits to just one or three possible values. That significantly cuts the memory required to store and operate the model.

Hassibi compared it to the chip industry's move from eight-bit to four-bit computing, but takes it a step further.

The startup said the compressed models use between 10 and 15 times less memory, generate responses six to eight times faster and consume three to six times less energy than conventional versions running on existing hardware.

Hassibi did acknowledged there is a trade-off, however. PrismML's models typically lose a few percentage points of overall performance, with factual recall weakening before skills such as reasoning, math and coding, he said.

PrismML is releasing two compressed versions of the model for free. They are designed to run on everyday devices, including iPhones, MacBooks and Nvidia-powered PCs.

The technology emerged from Hassibi's research group at Caltech. The university owns the underlying patents and licenses them exclusively to PrismML. In March, the company raised a $16.25 million seed round backed by Khosla Ventures and other investors.

Hassibi saidGoogle's open-source Gemma model is next in the pipeline, followed by much larger models, including those from frontier labs that today generally require datacenter hardware.

The technology, according to PrismML, could ultimately extend well beyond phones and laptops to robotics, autonomous systems and other products that need to make decisions quickly without relying on a cloud connection.

"It's very important that the intelligence be local and that it can run fast," he said.

watch now
VIDEO
3:10
03:10
Apple faces AI memory crunch with upcoming iPhone lineup
TechCheck

### Apple's on-device advantage

Apple already runs parts of its AI system locally, including translation, some summarization and features tied closely to personal information. More complex requests are routed to Apple's private cloud infrastructure or outside models.

Horace Dediu, founder of Asymco, said Apple is likely trying to keep the large majority of common Siri interactions on-device while reserving the most demanding tasks for the cloud.

The advantage is not simply using less memory, he said, but fitting a more capable model within the same physical limits.

"They're trying to figure out how big a model and how clever a model they can fit on the device," Dediu said. Keeping common requests local gives Apple lower latency, greater privacy and potentially lower licensing and cloud costs.

Apple may have an advantage in putting these models to work because it designs the iPhone's chips and software together, giving it tighter control over how AI runs on the device.

But analysts cautioned that PrismML's claims still need to be proven outside controlled demonstrations.

Tarun Pathak, research director at Counterpoint Research, said the model's performance on lengthy prompts, battery consumption during multitasking and reliability across millions of requests will be critical.

"The ultimate test will be millions of queries, thousands of device combinations and robust testing at scale," Pathak said.

Phil Solis, who leads IDC's research on client processors, said power consumption may be the biggest open question. A model that is capable enough to be used frequently — or continuously in the background for agent-like tasks — could drain a phone's battery even if it requires less memory.

watch now
VIDEO
2:32
02:32
Apple shares move higher despite losing ground in China
TechCheck

### What it means for chip demand

PrismML's release also comes during an intense debate over whether improvements in AI efficiency could eventually reduce demand for memory chips and expensive datacenter infrastructure.

Memory has become one of the biggest constraints and costs across consumer electronics and AI servers.Morgan Stanleyestimates Apple's average dynamic random access memory cost per bit could rise roughly 190% year over year in fiscal 2027, with NAND costs up about 180%. NAND is typically used in flash drives and solid state drives.

The firm expects Apple to raise the starting price of comparable iPhone 18 models by about $200 to protect margins.

PrismML said its approach could allow a cloud model that normally requires eight GPUs to run on one, while also allowing models that once required a server to move onto phones and laptops.

That could reduce the amount of memory or computing capacity needed for a given AI task. But it does not necessarily mean overall chip demand will fall.

Gil Luria, an analyst at D.A. Davidson, said shrinking models would not eliminate the need for processors or memory. It could simply move more of those chips from datacenters into phones and other devices.

"It's not that you're not going to need the chip," Luria said. "You're still going to need the GPU, and you're still going to need the memory."

He added that running AI on individual devices can actually be less efficient than using shared datacenter infrastructure because chips in phones may sit idle much of the time.

Efficiency breakthroughs can also lead to more use rather than lower spending, as cheaper and faster AI enables new products and prompts consumers to run models more often.

Still, the market has been quick to punish anything that suggests AI may need less memory than expected.Micronshares plunged in March after Google published itsTurboQuant paperon cutting memory use without hurting model performance, though the stock later recovered.

PrismML's public release gives everyday users and investors a chance to test whether its claimed gains hold up outside the lab. And for Apple, running more capable AI directly on the iPhone could help the company improve Siri without abandoning the privacy and hardware integration that distinguish its products.

"The combination of cloud and on-device AI can serve a more complete, efficient and privacy-centric AI experience," Counterpoint's Pathak said. "Complex tasks will be offloaded to the cloud, whereas sensitive, latency-critical and privacy-relevant tasks will be executed on-device."

WATCH:Apple sues OpenAI alleging trade secret theft: Here's what to know

watch now
VIDEO
7:05
07:05
Apple sues OpenAI alleging trade secret theft: Here's what to know
Squawk Box
Choose CNBC as your preferred source on Google and never miss a moment from the most trusted name in business news.