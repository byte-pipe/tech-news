---
title: My Take On AI and Technology (Besides the Pure Developer PoV) - DEV Community
url: https://dev.to/luftietheanonymous/my-take-on-ai-and-technology-besides-the-pure-developer-pov-cce
site_name: devto
content_file: devto-my-take-on-ai-and-technology-besides-the-pure-deve
fetched_at: '2026-02-27T19:17:28.840223'
original_url: https://dev.to/luftietheanonymous/my-take-on-ai-and-technology-besides-the-pure-developer-pov-cce
author: Luftie The Anonymous
date: '2026-02-27'
description: Hello Dev.to community ! I hope you're all doing well, today I decided for a little bit more... Tagged with ai, future, machinelearning, discuss.
tags: '#discuss, #ai, #future, #machinelearning'
---

Hello Dev.to community !

I hope you're all doing well, today I decided for a little bit more controversial topic this time and namely to present my point of view on AI besides just a tool for code-analysis, vibe-coding, generating images or other cuty activity people use AI for. Are you're interested ?

Buckle up and let's go !

WARNING ⚠️:This article contains personal views on the modern technology of Artificial Intelligence and current world's geopolitical situation and actions of certain governments. This article has in no condition been written with intent to trigger fear or be taken as an oracle.

But before I start, some entry information for a reader, so that they would know who is writing that to make the things clear.

### Introduction Information

* I define my views in case of world-views as an crypto-anarchist. I do not support any political side, I think out of the box.
* I do not belong to any associatations (like idk what you guys would think of me, that I'm foil-cap gang member or whatever, lol), every statement I make is my personal view.
* I'm an Web3 Developer with 3 years of experience in full-stack web-dev, with many interests on IT, so I also grasped some take on how AI neuro-networks are actually working. My knowledge on AI bases on youtube videos from experts on it, Brilliant lessons (on AI)
* My opinions are based on previous historic events and history of human species evolution.

### General take on AI

First of all, to make clear I treat AI as an statistical/probabilistic model that predicts the next word sequence, based on the appearance-ratios to certain word given. Which means every time it generates an output, I know that it's just pure statistics and probability based on the data that it posesses. And I state that we should not let AI just automate everything, without human-intervention on the entire workflow.

Whenever it generates an output for generating a list of elements in React:

import

React
,

{
useEffect
,

useState
}

from

"
react
"
;

import

{
getData
}

from

"
../some/directory/utils.ts
"

function

DataList
<
T
>
(
databaseTable
:
string
){

const

[
data
,

setData
]

=

useState
<
T
[]
>
();

async

function

fetchData
()

{


setBio
(
null
);


const

result

=

await

getData
(
databaseTable
);

if
(
results
.
length

>

0
){

setData
(
result
);

}


}

useEffect
(()
=>
{

fetchData
();

},[]);

return
(
<
div

className
=
"
some-style
"
>

{
data
.
map
((
element
)
=>
(
<
Element

data
=
{
element
}
/>
))
}

<
/div>
)

}

export

default

DataList
;

Enter fullscreen mode

Exit fullscreen mode

I can infer 2 things:

* The model I'm working on has been trained only on junior code
* My prompt was not specific enough

For those who do not know what the heck am I talking about is that, this component presents very pure understanding ofuseEffecthook in React, because it will get executed only once and the array content will not be trigged on any changes to parameter databaseTable.

But AI-code generation known also as vibe-coding and generally these all accessible AI-models, is just a top of the iceberg. As you could see on the thumbnail, I linked a video which informs that Antrophic has announced due to the US Department of War,...sorry ("Defense") the change of the guardrails, having as the author of the video said:

Abandoned the company's ethics rules for their AI-models

Well, for someone that is not really into history or just operates in a deep in a bubble and is absorbed by their environment (which is understandable), it might sound just as another boring company statement, updating some policies etc.

In fact however, it is for me a sign like:Ok in 1940s there's been the necluar bomb created...BY SCIENTISTSfor government. This timeperhapsAI-companies will be used as those who will create an Skynet-like weapon.

AI-companies are already involved in various dubious actions like transactions with NVIDIA --> OpenAI cycles etc. (sorry for that generalization) and OpenAI turning from non-profit to for-profit. Besides Scam Altman to state differently. Well as someone said:

Everything is temporary

## AI Madness Time

Social media and also media per se are flooded with articles on the AI spreading fear and announcing another AGIs, paralyzing newbies and repeatedly speaking of replacement by AI.

I will mention only that for me it's absolutely not apprehensive, how and why someone would allow tools made by some company or by some dude, that came back with a milk after years like OpenClaw/Moltbot whatever to manageTHEIRprivate data and information.

Here the podcast episode with the main-character from OpenClaw

I'm wondered because OpenClaw and AI automation is not flawless and it performs bugs as well, here an example.Openclaw deletes entire inbox

### My AI-usage

My personal AI-stack is actually quite peculiar, because I use actually only duck.ai wrapper for my daily usage (Privacy first).I contemplated about purchasing an subscription for github co-pilot, but for now I don't think it's necessary.

I use AI quite often to handle errors if I can't find the bug on my own for a bit longer, but not like:"Hey Bobert, fix the code for me,no mistakes!"-guy, but rather in a way."I'm running into an issue: [The error message]. I tried [list down the steps] and I still could not resolve that error. Find the issue inside my code and provide the potential solution approach."

Basically I let it check whether it spots some logic failure of mine whenever I get an error faster than I do and then learn from it.

### Why I write about it ?

I write this article in order to showcase the deceitful narrative served by social-media about AI, that should "make people more creative" etc. I want to showcase that conversely it turned out that creativity is almost gone and noone cares:

* Almost every website is currently looking the same (they use shadcnx + next.js + tailwind) with basic template and design not so much customized, if that's called creativity, thus I'm done also with web-dev as it's so red ocean area, that it's not engaging to enter anymore.
* The amount of shitty code increased.
* The IQ level of an average person decreases instead of increasing
* Scammers got a perfect tool to make their scams even more benefitial. I recently helped some person of my narrow-circle of contacts to investigate why there's been some amount of money taken from their bank-account. It turned out that they have used for some period of time a tool in free trial, but there was no mention about it's expiration or when they will get charged. Additionally the tool they used was so shit that OSINT tools likehttps://haveibeenpwned.com/or such websites would give more comprehensive data than that tool.
* People are getting paralyzed
* Social connections for people are tough to be bound

And there are other much bigger social, financial and technological issues coming from AI.

I do not state that we should stop using AI etc.I just assert the facts of different point of view on AI and it's impact.

And if you're fed up stop reading, please read next few lines about primary purpose of Internet and you can go.

### Primary Purpose of the Internet

For a context of my conjecture on possible miss-use of AI companies by government. Let's head back to the ground-level of digital world, the Internet. If you have ever wondered why the internet has been created, who created it and why isn't the creator of internet a rich well known guy. The answer is quite simple. One of the leading scientists in building the internet were Vint Cerf and Paul Baran, who was building the internet for the Government's Commission to build a communication system that surrvives nucluar attack.

No social-connection and building better world focused, not enhancement for good. It's been built for again:

Government to build a communication system that survives neclear attack

Here is the link to the confirmation of what I say

And this has been with any other invention or any other science-field. Cryptography (my main focus in my career) has not been invented to enable regular people securely communicate, it's been for the military purposes. Is that a reason why I should throw away cryptography otherwise should be named a spy ?

Well for some people perhaps yes, but I comprehend their statement. I was and still am oppose to the governments and any globalists ideas, I think not using the ready to use tools and building something from scratch is pointless and irrational.

### Additionally one simple but broad fact, inferred by me from the human species history study

1. Environment changes, possibilities changes, patterns stay the same: Throughout many years the technology has evolved, live conditions enhanced, but patterns remained. What do I mean ?

* Surveilance and Control was always the purpose on the first place. Because I studied for some time history of Britain, creation in 1086 of the Domesday Book is one of the example of rising surrveilance.
* Media are basically the subordinaries of the government or the opposition, depending on who will be paid.

1. Human have actual not evolved much from monkey: controversial, but unfortunately the truth is that any action in our life can be narrowed down to the monkey world. Which for me personally is sad, because the development of the new technologies is interesting and flabbergasting, but often flawed by monkey incentive, carved inside human brain.
2. Entities who pursued good for humanity were always mocked, taunted or were introverted: People like Nikola Tesla, whose biography I also studied was an phenomenal inventor, but he was not an entrepreneur like Edison, whom I actually condemn for the Propaganda against AC (Alternative Current) using it on animals. But as I said:Greedy Monkey will do everything for more bananas.

And thus Tesla died feeding pigeons in a hotel room paid by the company as honorary for his work.

### Conclusion

My take away from all of this would be quite simple. As a species we're likely on the verge on existence, meaning it will be a miracle if human species survives until 2100. So:

* Switch off the media, focus only on what you are passionate about.
* Don't let yourself absorb with stress and find your tribe (again monkey analogy XD) and contact with them.
* Don't trust politicians and big companies in their incentives.
* Don't stress about being replaced by AI, today world is so screwed that entrepreneurs are people like Amodei from Antrophic who can't fit a single deadline of replacing human by AI.

Happy Weekend and and stay tuned for first report of progression on sunday ! I decided I will post the reports of my efforts in cryptography and blockchain architecture weekly on sunday.

Stay safe, stay alert, stay curious ;D

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
