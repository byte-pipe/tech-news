---
title: Master Local Fine-Tuning with "gemma-trainer" - DEV Community
url: https://dev.to/googleai/master-local-fine-tuning-with-gemma-trainer-3ipp
site_name: devto
content_file: devto-master-local-fine-tuning-with-gemma-trainer-dev-co
fetched_at: '2026-07-08T01:53:50.766926'
original_url: https://dev.to/googleai/master-local-fine-tuning-with-gemma-trainer-3ipp
author: bebechien
date: '2026-07-07'
description: Take control of your AI models with our newest skill, designed to make local fine-tuning efficient. Tagged with gemma, finetuning, ai, agents.
tags: '#gemma, #finetuning, #ai, #agents'
---

Remember back in May when I introduced thegemma-skillsrepository? It's been rewarding to see how many of you have usedmy previous postto streamline your workflows. (And hey, even if we aren't swimming in GitHub stars yet, I think we're off to a great start!😉)

But as I built more custom applications, I kept hitting the same roadblock:how to take a great base model and adapt it to my specific needs.

Fine-tuning a model usually requires wading through complex setups and confusing guides. To make this process straightforward and quick, we created our newest skill:gemma-trainer

# What isgemma-trainer?

gemma-traineris your blueprint for training and adapting Gemma models on your local hardware. It handles the "how-to" so you can focus on your specific project goals, whether you are teaching a model a new domain or aligning its behavior to your preferences.

# Why You'll Use It

* Faster, Lighter Training: We recommend usingUnslothfor single-GPU training, making it fast and using less memory so it runs easily on personal hardware.
* Three Key Methods: It guides you through Supervised Fine-Tuning (SFT) to teach new info, Direct Preference Optimization (DPO) to align with preferences, and Reward Modeling (RM) to rate responses.
* Teach Models to See and Hear: It includes clear instructions for training models with images and audio (multimodal learning) alongside text.
* Run Anywhere: Quickly convert your models to lightweight formats (like GGUF) and run them on mobile or smart devices (IoT) usingLiteRT-LM.
* Up-to-Date Best Practices: The skill is continuously updated with the latest optimized settings and training techniques, ensuring you're always using the best methods.

# Practical Use Case

To see this in action, recall how we turned Gemma 4 into an expert translator for Classical Korean literature inmy previous post. Withgemma-trainer, you don't need to manually piece together a pipeline. You can simply ask your agent:

"Fine-tune Gemma 4 E2B on the dataset bebechien/HongGildongJeon."

With thegemma-trainerskill, your agent will partner with you to:

1. Verify your data: Use the validation script to ensure your training data matches template requirements.
2. Set up parameters: Select the best LoRA settings to teach the model linguistic nuances without running out of video memory (VRAM).
3. Run the training: Launch the training session using optimized, resource-efficient defaults.
4. Evaluate and iterate: Review the model's performance and adjust settings to get the exact results you need.

Here is an example showing the agent starting a fine-tuning run on a Gemma 4 12B model for audio tasks:

Once configured, the agent kicks off the training process using your designated dataset:

Even if you make a mistake, the agent has your back. For instance, when I accidentally requested training a Gemma 4 31B model (which is a text-and-vision model and has no audio capability), it suggested using Gemma 4 E2B or 12B for audio tuning instead:

Once training is complete, the agent presents the results and outlines the next steps:

You can also ask your agent to write a custom evaluation script based on your specific requirements. In this case, I asked the agent to create a script that checks transcription similarity:

Finally, you will receive a comprehensive report summarizing the training performance, making it clear where you can make improvements in the next run:

# Let's try!

gemma-traineris a living, structured document. Drop it into your agent's skills directory, and your AI assistant will immediately know how to guide you through the process.

Check out therepository, add the skill to your toolbox, and let's build something amazing!

Thanks for reading and happy training!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse