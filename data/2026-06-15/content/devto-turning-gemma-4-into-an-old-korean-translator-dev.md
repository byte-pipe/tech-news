---
title: Turning Gemma 4 into an Old Korean Translator - DEV Community
url: https://dev.to/googleai/turning-gemma-4-into-an-old-korean-translator-hop
site_name: devto
content_file: devto-turning-gemma-4-into-an-old-korean-translator-dev
fetched_at: '2026-06-15T20:10:49.740537'
original_url: https://dev.to/googleai/turning-gemma-4-into-an-old-korean-translator-hop
author: bebechien
date: '2026-06-15'
description: There’s something uniquely beautiful about old books. The smell of weathered paper, the texture of... Tagged with finetuning, gemma, ai.
tags: '#finetuning, #gemma, #ai'
---

There’s something uniquely beautiful about old books. The smell of weathered paper, the texture of the pages, and the stories that have survived generations. But if you’ve ever tried opening a piece of Classical Korean literature—like the Joseon Dynasty novelHongGildongJeon (홍길동전)—you’ll quickly realize that time leaves its own mark on language.

Between the lack of word spacing and obsolete letters like the dot vowelArae-a (ㆍ)or the softYeorin-hieut (ㆆ), reading it feels less like browsing a novel and more like solving a beautiful, ancient puzzle. Even for native speakers, the linguistic gap is massive.

So, that's why I decided to creatthis tutorial, a digital bridge between the past and the present. UsingGemma 4 E2B (IT), I set out to create a humble translator that turns Classical Korean into smooth, modern Korean.

# The Recipe for Training

To keep things manageable, I ran this on a single NVIDIA T4 GPU (16GB) using Google Colab.

## 1. Setting Up the Kitchen

First, we pull in our favorite open-source tools: Hugging Face’stransformers,trlfor the training loop, andpeftso we can use LoRA (Low-Rank Adaptation) to fine-tune our model without needing a massive server cluster.

## 2. Gathering the Ingredients

For our data, I used a public domain version ofHongGildongJeon, paired with a beautifulmodern translationby직지프로(licensed under Creative Commons).

To make Gemma feel at home, I structured the data into a conversation, guiding the model with a clearsystemprompt:

[

 
{
"role"
:
 
"system"
,
 
"content"
:
 
"Translate Classical Korean into Modern Korean."
},

 
{
"role"
:
 
"user"
,
 
"content"
:
 
"됴션국셰둉ᄃᆡ왕즉위십오연의홍희문밧긔ᄒᆞᆫᄌᆡ상이잇스되"
},

 
{
"role"
:
 
"assistant"
,
 
"content"
:
 
"조선국 세종대왕 즉위 십오년에 홍회문 밖에 한 재상이 있으되,"
}

]

Enter fullscreen mode

Exit fullscreen mode

(Translation note: This line introduces us to a prime minister living just outside the Honghoemun Gate during the 15th year of King Sejong's reign!)

# The "Before" Picture

Before giving Gemma any specific training, I ran a quick baseline test. Base models are smart, but archaic grammar is a highly specific domain. Without tuning, Gemma tried its best but ended up giving long, overly literal explanations:

* Original Classical Text:ᄇᆡᆨ씨듯고ᄂᆡ심의탄복왈그근본을ᄀᆞᆷ초지아니ᄒᆞ니장부로다ᄒᆞ고ᄌᆡ삼위로ᄒᆞ더라
* Human Translation:백씨 듣고 내심에 탄복 왈, "그 근본을 감추지 아니하니 장부로다!" 하고, 재삼 위로하더라.
* Gemma's Initial Guess:"Like the color, the heart's praise said, 'The foundation cannot be deeply felt...'"
* Initial Similarity Score:4.85%💔

(Translation note: This line actually means - Upon hearing this, Mr. Baek was deeply impressed and said, "He does not hide his true nature; he is a true man!" and comforted him again and again.)

The base model was clearly lost in time. It needed a map.

# Teaching Gemma with Care

To train the model efficiently, I used a Parameter-Efficient Fine-Tuning (PEFT) setup with LoRA.

from
 
peft
 
import
 
LoraConfig

peft_config
 
=
 
LoraConfig
(

 
lora_alpha
=
16
,

 
lora_dropout
=
0.05
,

 
r
=
16
,

 
bias
=
"
none
"
,

 
target_modules
=
"
all-linear
"
,

 
task_type
=
"
CAUSAL_LM
"
,

)

Enter fullscreen mode

Exit fullscreen mode

The Secret Sauce:collate_fn

When fine-tuning a chat model to behave like a specific tool, you don't want it to waste energy learning how to re-write your prompt. By using a custom data collator, I masked thesystemanduserinputs (setting their labels to-100), forcing Gemma's loss calculation to focusstrictlyon generating the correct modern assistant response.

After setting our hyper-parameters to gently cruise through 5 epochs with a learning rate of2e-5, I hit train.

# The Warm "After" Glow

After a bit of patience and letting the trainer do its magic, the results were incredibly rewarding. The character-by-character similarity score jumped all the way up to a brilliant79.93%!

Look at how it handles the text now:

* Original Classical Text:ᄇᆡᆨ씨듯고ᄂᆡ심의탄복왈그근본을ᄀᆞᆷ초지아니ᄒᆞ니장부로다ᄒᆞ고ᄌᆡ삼위로ᄒᆞ더라
* Human Translation:백씨 듣고 내심에 탄복 왈, "그 근본을 감추지 아니하니 장부로다!" 하고, 재삼 위로하더라.
* Gemma's Fine-Tuned Translation:백씨듯 고내심에 탄복 왈, "그 근본을 감초지 아니하니 장부로다." 하고 제삼 위로 하더라.
* New Similarity Score:85.71%✨

# Closing Thoughts

Technology often pushes us relentlessly into the future, but my favorite tech projects are the ones that allow us to look backward with greater clarity. By spending a little time fine-tuning a lightweight model like Gemma 4, we can build tools that preserve cultural history, making ancient wisdom and classic stories accessible to anyone with a laptop.

Next time you find a piece of history that feels just a bit too out of reach, remember that a small dataset and a fine-tuning session might be all you need to bring it into the light.

Here's the structured workflow when you do a fine-tuning for your own domain:

1. Define a clear goal
2. Prepare a high-quality dataset and evaluation plan
3. Verify the model is learning
4. Evaluate with metrics and human judgment
5. Deploy and iterate

👉Check out this tutorial in Gemma Cookbook👉Star the repository to support us

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse