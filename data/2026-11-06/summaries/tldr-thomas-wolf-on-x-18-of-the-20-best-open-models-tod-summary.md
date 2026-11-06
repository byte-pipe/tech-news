---
title: "Thomas Wolf on X: \"18 of the 20 best open models today are Mixture-of-Experts. Dense is basically over. And yet the know-how to train a good MoE still..."
url: https://x.com/thom_wolf/status/2118432475730882627
date: 2026-11-06
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-06T12:30:01.476286
---

# Thomas Wolf on X: "18 of the 20 best open models today are Mixture-of-Experts. Dense is basically over. And yet the know-how to train a good MoE still...

# Summary of Thomas Wolf’s X Post on “The Ultimate MoE Training Handbook”

## Overview
- Thomas Wolf states that 18 of the 20 best open‑source models today are Mixture‑of‑Experts (MoE) and that dense models are essentially obsolete.  
- He notes that practical expertise for training high‑quality MoE models is still confined to a few teams.  

## Effort Behind the Handbook
- The Hugging Face team invested **800 k GPU hours** to run extensive experiments.  
- All findings have been compiled into a **free, open‑access handbook** titled *“The Ultimate MoE Training Handbook.”*  

## Contents and Focus Areas
The handbook is organized around the most common questions training teams encounter, including:  
- Choosing the number of experts, their size, and whether to share parameters.  
- Understanding and reducing the time spent in all‑to‑all communication.  
- Diagnosing why a run may be 25× slower despite clean logs.  
- Selecting the router activation (softmax, sigmoid, or √softplus) and the rationale for keeping it in fp32.  
- Deciding between auxiliary loss and DeepSeek’s loss‑free bias.  
- Strategies for upcycling a dense checkpoint versus training from scratch.  
- Possibilities for serving with fewer experts per token than used during training.  

## Format and Availability
- Length: roughly **70 k words** (requires a few days to read).  
- Includes **55 interactive figures**, runnable code snippets, and performance numbers from the authors’ own experiments.  
- The handbook can be accessed here: https://huggingface.co/spaces/hugging…  

## Additional Context
- The post was shared on X (formerly Twitter) on Nov 5 2026, receiving over 56 k views and notable engagement.