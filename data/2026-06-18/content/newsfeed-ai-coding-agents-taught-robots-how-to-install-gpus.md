---
title: AI coding agents taught robots how to install GPUs and cut zip ties - Ars Technica
url: https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/
site_name: newsfeed
content_file: newsfeed-ai-coding-agents-taught-robots-how-to-install-gpus
fetched_at: '2026-06-18T12:19:41.003751'
original_url: https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/
date: '2026-06-17'
published_date: '2026-06-17T19:25:19+00:00'
description: Nvidia's self-improvement program for robots enlists teams of AI coding agents.
tags:
- ars-technica
- ai
- ai agents
- artificial intelligence
---

Text
 settings

What happens when you give AI coding agents a lab full of robotic arms, some compute resources, and a “generous token budget” for teaching the robots various tasks? The agents can apparently figure out a training regimen that teaches the robots to successfully cut zip ties and even insert GPUs into thin sockets on motherboards.

That glimpse into how AI can act in a fully autonomous way to automate robot training was made possible by a new agent harness framework—software that wraps around AI models to enable their use of various tools while also providing capabilities such as memory, context, constraint, and feedback loops. That agentic harness,called ENPIRE, was developed by robotics researchers at the Nvidia GEAR (Generalist Embodied Agent Research) lab alongside collaborators from Carnegie Mellon University in Pittsburgh and the University of California, Berkeley.

“A part of our NVIDIA GEAR lab now self-improves tirelessly overnight,” wrote Jim Fan, director of AI at NVIDIA, in aLinkedIn post. “We just read the reports in the morning.”

Fan also jokingly described the goal of such AI-directed robot training, saying, “We all take a holiday and Jensen wouldn’t even notice,” in reference to Nvidia founder and CEO Jensen Huang. But it’s not only Nvidia robotics researchers who could benefit—Fan said the team would be open-sourcing everything so anyone can host their own “self-running robot lab at home.”

The ENPIRE harness has four modules that enable AI coding agents to perform automatic reset and verification on tasks, refine policies that guide robotic behavior, evaluate such policies across multiple physical robots working in parallel, and address failures by analyzing logs, ingesting research papers, and improving training infrastructure and algorithm code. More technical details are available in theresearch paperuploaded on June 16, 2026.

The harness was tested with three different AI coding agents, including OpenAI’s Codex with GPT-5.5, Anthropic’s Claude Code with Opus 4.7, and Moonshot AI’s Kimi Code with Kimi K2.6. Teams of the coding agents independently developed different algorithmic approaches to robot training, tested them in real-world experiments, and then retained whatever changes helped raise the overall success rate over repeated cycles of self-directed testing.

## The success and limits of AI-directed robot training

Equipped with ENPIRE, the AI coding agents developed strategies for robotic self-improvement that achieved a 99 percent success rate across several manipulation tasks, including the standard “Push-T” task that challenges robots to move a T-shaped block to fit a target position on top of a table. Other tasks included organizing pins in a pin box, tying and cutting zip ties, and placing a GPU into a motherboard before unplugging the graphics card again to reset for the next trial.

The most promising result may have come from the pin insertion and organization task. In that robot-training scenario, AI coding agents achieved nearly 100 percent success faster than a “frontier human-in-the-loop method”developed by many of the same human researchers.

Such experiments also showed how larger teams of up to eight AI coding agents could achieve high success rates in robot training more quickly than smaller four-agent teams or single agents working alone. For example, the eight-agent team achieved 99 percent success on the Push-T task in two hours of research time, compared to the four-agent team requiring three hours and the single-agent team requiring nearly five hours.

But the human researchers also discovered some crucial limitations when unleashing AI coding agents as autonomous robot trainers. The robots often sat idle and unused while the coding agents were busy “reading logs, writing code, debugging, or waiting for the language-model backbone.” Larger teams of coding agents also spent more time summarizing each other’s ideas and less time actually using the robots, and the coding agents sometimes failed to make full use of available compute resources when launching parallel training sessions.

The faster success rates enabled through more agents and robots working together also came at the cost of higher token consumption—a noteworthy consideration at a time when AI developers such as Anthropic areweighing pricing changesthat would significantly increase the token-related costs of using AI services.

Flush with cash from the AI boom, Nvidia has been busily pushing its vision for physical AI through multiple robotics initiatives. On May 31, the companyannounced a partnershipwith the prominent Chinese robotics company Unitree to provide a “Reference Humanoid Robot” for research labs developing general-purpose AI-powered robots.

During awhirlwind tour of South Koreain early June, Nvidia founder and CEO Jensen Huang also met with Hyundai Motor Executive Chair Chung Euisun to discuss scaling up themass manufacturing of AI-powered robots. Hyundai Motor Group owns the US robotics company Boston Dynamics, which is already well-known for itsfour-legged “robot dog” Spotand has been working to commercialize its Atlas humanoid robot.

 Jeremy Hsu
 

Tech Reporter

 Jeremy Hsu
 

Tech Reporter

 Jeremy Hsu is a reporter exploring a wide range of topics across deep tech and AI. He has previously written for New Scientist, Scientific American, IEEE Spectrum, Wired, Undark Magazine and MIT Tech Review, among many other publications, about topics such as deepfakes, data centers, drones, battery tech, robotics, and GPS jamming. He also has a Master of Arts in Journalism from NYU, and a bachelor's degree from University of Pennsylvania in History and Sociology of Science, with a minor in English.

 

1. 1.Windows and Linux users: The deadline to update Secure Boot keys is near
2. 2.Massive breach spills credentials for thousands of sensitive networks
3. 3.Tesco moving 40,000 server workloads off VMware amid Broadcom's “abusive conduct”
4. 4.Anthropic "pauses" token-based billing for its Claude Agent SDK
5. 5.The Slate Truck's price may have leaked, starts at $24,950

Customize