---
title: 'Two Devs and a Copilot Created ClassifierAI: A Prototype Chrome Extension that Automatically Detects AI-Generated Content on DEV! - DEV Community'
url: https://dev.to/devengers/two-devs-and-a-copilot-created-classifierai-a-prototype-chrome-extension-that-automatically-4fge
site_name: devto
content_file: devto-two-devs-and-a-copilot-created-classifierai-a-prot
fetched_at: '2026-06-09T12:03:13.166174'
original_url: https://dev.to/devengers/two-devs-and-a-copilot-created-classifierai-a-prototype-chrome-extension-that-automatically-4fge
author: FrancisTRᴅᴇᴠ (っ◔◡◔)っ
date: '2026-06-06'
description: 'This is a submission for the GitHub Finish-Up-A-Thon Challenge Note: AI is currently a Hot Topic in... Tagged with devchallenge, githubchallenge, discuss, showdev.'
tags: '#discuss, #devchallenge, #githubchallenge, #showdev'
---

GitHub “Finish-Up-A-Thon” Challenge Submission

This is a submission for theGitHub Finish-Up-A-Thon Challenge

Note:AI is currently a Hot Topic in the developer space.I recommend reading this post in full before commenting.The dataset being used does not come from dev.to, so expect the AI model to be inaccurate. This is to showcase a tool that can be helpful for others in the future and eventually tune it to be more accurate on the DEV platform.I will talk more about it further in the post. If you have any questions or concerns, I would love to hear from you!

 

# Authors

Main Author:Francis Tran@francistrdevCo-Author:Elmar Chavez@codingwithjiro

This is a Team Submission featuring Francis and Elmar!

# Table of Contents

* Introduction
* What We BuiltWhy does this Project Exist?
* Why does this Project Exist?
* DemoInstallationUsing the Chrome Extension
* Installation
* Using the Chrome Extension
* The Comeback StoryThe Old EraThe New Era
* The Old Era
* The New Era
* My Experience with GitHub Copilot
* SummaryCurrent Challenges in our Chrome Extension
* Current Challenges in our Chrome Extension
* Thank You!

# Introduction

AI has shaped everything on the internet. This ranges from easier access to information faster than before to having AI in our development workflows.

With the good side of the use of AI, there is also the bad side of using AI. Currently, there is a lot of purely AI-generated content being produced on the internet in order for sites to boost themselves to relevance on Google, which creates unnecessary competition. Additionally, with the advance of AI, it has continuously become more difficult to distinguish content that is AI-generated versus content made by a Human. "AI" as a name on its own has a bad reputation due to how people are using AI regardless of if you are using it as a tool.

Even though AI is everywhere, many people are combating it. Sometimes it is handled in a professional setting while others handle on a vigilante level (not recommended at all).As a DEV user, the goal is to try to minimize AI-generated articles on dev.to in order to enhance the user experience and diversifying content where others can learn and grow as a developer.

With that said, along with Elmar's collaboration, we built ClassifierAI!

Disclaimer:Before commenting, this project is a prototype! This is meant to showcase what the Chrome Extension can do based on existing data used, which the model is not accurate due to data not coming from dev.to directly.This Chrome Extension is not meant to be used as a perfect solution to filter out AI-Generated contentas a result of data outside of dev.to.I will talk more about this later in the post.

 

 

# What We Built

We builtClassifierAI, which is aprototypeChrome Extension that allows you to detect AI-generated content on DEV in an instant. This is built usingTensorflow.jsto perform:

* Image Classificationto determine if the cover image of the article is AI-generated usingTeachable Machineby Google.The dataset used to train the model:https://huggingface.co/datasets/Hemg/AI-Generated-vs-Real-Images-DatasetsThe settings to train the model based on866 images in total(433 images per class where we have two classes that is labeled "AI" and "NotAI"):
* The dataset used to train the model:https://huggingface.co/datasets/Hemg/AI-Generated-vs-Real-Images-Datasets
* The settings to train the model based on866 images in total(433 images per class where we have two classes that is labeled "AI" and "NotAI"):

866 Images Total
2 Classes Total
 - "AI" Class
 - "NotAI" Class

Epochs: 30
Batch Size: 16
Learning Rate: 0.0001

Enter fullscreen mode

Exit fullscreen mode

* Text Classificationto determine if the article itself is AI-generated.The dataset used:https://huggingface.co/datasets/gouwsxander/wikipedia-human-ai
* The dataset used:https://huggingface.co/datasets/gouwsxander/wikipedia-human-ai

 

Initially,it started off as a Chrome Extension that scans 100 images on Google Images to detect if the image is AI-generated and label them accordingly.

For this case, we updated the Chrome Extension where it only works on dev.to, and is able to classify the entire article, including the cover image, and showing the result to the user whether the content is AI-generated. This Chrome Extension works every time the user clicks on an article on DEV.

## Why does this Project Exist?

Generative AI is currently a hot topic in my experience. Many friends and colleagues I have despise Generative AI because they have the notion that"it will replace your job".

 

Sounds familiar? We all heard that phrase at least once...

 

Although there are tools to combat this likeGPTZero, it is still an issue because:

* It is alot of manual workjust to copy/paste to see if it is AI-generated.
* There are tools that bypass GPTZero in order to get the "Human" result.Every style of writing is different across communities, so it can be difficult to identify AI-generated content overtime.

 

With these problems in mind and the state of DEV, I want to create a useful tool thatidentifies AI-generated content automatically without having to open GPTZero and copy and pasting just to know the result of the content.

Additionally,this Chrome Extension is personalized for DEV since I believe the dataset collected in the future will be more focused and accurate(I believe all blogging platforms have different writing styles regardless of content being AI-Generated. Hence, making it more personalized and focus on the DEV space).

Overall,this Chrome Extension solves the issue when it comes to less manual work and more personalized for DEV since I believe it reduces the chance of having tools that bypass the AI scanner since it is more focused than broad.

With community support, I hope that the model will be more tuned and accurate as DEV continues forward! Which is why we made it Open Sourced as an Unofficial DEV Chrome Extension. More details later in the post.

With that said, we will now show our prototype Chrome Extension in action!

 

 

# Demo

In this demo, we will show you the installation process in order to get the Chrome Extension running in your browser and showcasing how the Chrome Extension works.

## Installation

To get started, create an empty folder on your computer and open it usingVScode or any IDE.

 

1) In the Terminal, clone the repository:

git clone https://github.com/FrancisTR/ClassifierAI.git

 

2) Ensure you are in the directory by doing:

cd ClassifierAI

 

3) Then install packages and run the build:

npm installnpm run build

 

4) On your browser, head over to the extension page and ensure you enabled Developer Mode.

 

5) Finally, drag the "dist" folder onto the extension page and you are ready to go!

 

Now we will talk about how to use the Chrome Extension on dev.to!

## Using the Chrome Extension

To use the Chrome Extension, open the popup located on the top right of the browser and enable the switch.

Then, click on any article you see on dev.to and it will do its thing: Scanning the Cover image and the article to determine if either of them are AI-generated.

 

For the Cover Image,the AI will perform Image Classification to determine if the image is AI-generated. Once the scan is complete, the AI will embed an icon, located on the bottom right of the image. In this case, it is not AI-generated.

 

There are three icons to expect:

 

* Like we saw, this icon indicates that the image is not AI-generated.

 

* This icon indicates that it may or may not be AI-Generated.

 

* This icon indicates that it is AI-generated.

 

For the article itself,the way you can see if the article is written by AI or not is located in the popup menu in the Chrome Extension on the top right as shown below:

Note:There is currently no breakdown feature on which part of the article is AI-generated or not.

 

 

# The Comeback Story

Initially, the project was considered"complete"in my view a couple years ago. However, I wasn't proud of the outcome due to the fact that there were bugs that were hard to detect and how"messy" it felt.I haven't touched the project in years due to other things that needed my attention during that span.

When I heard about this challenge, I though it would be agreat opportunity to not only finish the project, but also to work with Elmar directly and explain the code-base to someone.

This gave me the opportunity to practice my skills in communication and to be able to explain what I have built. It was also a good opportunity for Elmar as well since this is his first time working on an existing code-base and contributing to it!

 

Not only did we finish the prototype, but we also learned from each other when it comes to:

* Explaining the code-base to a new developer.
* Organization and Communication skills when working in different time zones.
* Learning the responsibility of a Maintainer for a project.

 

With that said,I will be explaining what the project was meant to be and how we got to the finish line!

## The Old Era

The old ClassifierAI's purpose was to scan 100 Images sequentially based on what is currently being loaded on the page and to label each image accordingly if it is made by a Human or not via icons shown here.

 

For the main functionality, all you have to do is enable the scan in the popup.

 

You then scroll the Google Image page and let it do its thing.

That's it.

 

Additionally, the repository is incomplete since the "demo" section in the README.md is empty during that time. The overall project back then didn't feel "impactful" since its only purpose was to scan images and the model I currently haveisn't accurate due to an unbalanced data sample in the dataset overall.

If you would like to see what it looked like initially, feel free to visit the branch I linked below:https://github.com/FrancisTRAlt/ClassifierAI/tree/OldProject

 

Now, we then transfer to the new Era and how we complete the project(as a prototype)!

## The New Era

When the Challenge was announced, I asked Elmar if he would like to contribute to my half-baked project, which he said "Yes"!

The first thing we did was to migrate to Vite.The reason is that in the old project, the packages were installed locally instead of vianpm. The reason is how Chrome Extension works is that it restricts developers from calling "CDN" links and external packages. The only way to do this in Vanilla was to install the files locally.

Is this ideal? Definitely not. Back then, with the knowledge I had, it was the only solution.

Fortunately, with the help of AI, we were able to Migrate to Vite. Migrating to Vite allows us to install packages vianpm. It is much more clean and saves a lot of space.

 

Speaking of installing packages, Elmar noted that theml5.js, a library that is used for Teachable Machines, is a deprecated package and other issues he came across:

 

The bright side is that the issues were fixed, though it gave us this when wenpm install:

 

You could say that we can donpm audit fix --force, but that lead to more issues than before. Even then when doingnpm audit fixdoesn't change anything.For right now, these vulnerabilities exist in the current state...

With the migration to Vite,we then moved on to the bigger tasks, which is training the AI Model!

 

Initially, the goal was using Gemma 4 instead of using the custom model I have trained using Teachable Machines for scanning cover images. However, like any local model, the problem was performance since it takes awhile to produce an output.

For some reason, it got to the point where the Chrome Extension nuked the whole browser, making it unusable(Don't ask how that happened or even how it is possible to begin with).

Instead of using an existing LLM,I thought about using an existing dataset that already has images for me to train as an improvement to the current model I have for Image Classification.

Although this is an improvement, the model is still not perfectsince the images in the dataset is WAY different from images being used on DEV, but it is at least diversified compared to the previous dataset I had. Additionally, instead of scanning 100 images, it only scans one (which is the Cover Image).

 

The new feature we implemented in our Chrome Extension is classifying articles and determining if the article is AI-generated. I looked on YouTube for an approach and I found this video explaining on classifying text:

The way text-classification works on this current Chrome Extension is that it grabs the entire text from the article to feed into the model.

function
 
getCleanArticleText
()
 
{

 
const
 
root
 
=

 
document
.
querySelector
(
"
.crayons-article__body
"
)
 
||

 
document
.
querySelector
(
"
article
"
);

 
return
 
root
 
?
 
normalizeWhitespace
(
root
.
innerText
)
 
:
 
""
;

}

Enter fullscreen mode

Exit fullscreen mode

 

Then, it takes in the article and performs classification based on the dataset used from Wikipedia(which is the reason why it is not accurate when using this extension on dev.to due to the style of the content).

It then gives a score to the user a percentage on how much it is Human generated versus AI-generated.

function
 
detectGPTStyle
(
text
)
 
{

 
if 
(
!
wikipediaDataset
 
||
 
wikipediaDataset
.
length
 
<
 
10
)
 
{

 
return
 
baseUnknownResult
();

 
}

 
const
 
datasetScore
 
=
 
compareDataset
(
text
);
 
// AI %

 
const
 
devHuman
 
=
 
computeDevHumanScore
(
text
);
 
// Human %

 
const
 
generalHuman
 
=
 
computeGeneralScore
(
text
);
 
// Human %

 
const
 
aiPenalty
 
=
 
detectAIPatterns
(
text
);
 
// AI %

 
// Adjust weights here

 
let
 
humanScore
 
=

 
devHuman
 
*
 
0.40
 
+

 
(
100
 
-
 
datasetScore
)
 
*
 
0.35
 
+

 
generalHuman
 
*
 
0.25
 
-

 
aiPenalty
 
*
 
0.25
;

 
// Modify squash sensitivity

 
humanScore
 
=
 
squashScore
(
humanScore
);

 
// Adjust classification thresholds

 
let
 
label
 
=

 
humanScore
 
<=
 
33.33

 
?
 
"
AI-generated
"

 
:
 
humanScore
 
>=
 
66.66

 
?
 
"
Human-written
"

 
:
 
"
Mixed
"
;

 
const
 
finalScore
 
=
 
Number
(
humanScore
.
toFixed
(
2
));

 
return
 
{

 
label
,

 
averageAIScore
:
 
finalScore
,

 
humanPercent
:
 
finalScore
,

 
aiPercent
:
 
Number
((
100
 
-
 
humanScore
).
toFixed
(
2
)),

 
mixedPercent
:

 
finalScore
 
>
 
33.33
 
&&
 
finalScore
 
<
 
66.66
 
?
 
100
 
:
 
0
,

 
};

}

Enter fullscreen mode

Exit fullscreen mode

 

Other small things we added was UI enhancements where we usedchart.jsto display information in a more clean way.

 

That's it! The project is complete! Is it perfect?

I say this because there is always room for improvements, especially with the dataset we currently have. The dataset for the image classification and text classification is there as a placeholder just to showcase the main functionality.In the future, we hope to use the dataset coming from dev.to specifically in order for the model to be more accurate.

 

 

# My Experience with GitHub Copilot

Disclaimer:This section accounts for my experience using GitHub Copilot. Elmar uses ChatGPT for his development workflow and has been using it as a mentor to navigate the code-base and fix bugs as shown earlier.

 

I have used GitHub Copilot before in past challenges on DEV and I talked about my experience using GitHub Copilot. For this project, nothing really changed much. The main thing GitHub Copilot has been really useful for is in themigration processsuch as

* TranslatingBootstrap to Tailwind CSS.
* Moving away fromml5.js to Tensorflow.js.
* Ensuring the project follows the Chrome Extension Manifest V3.

 

One example I will showcase is telling GitHub Copilot to translate the currentml5.js code to Tensorflow.js.

Essentially, I asked GitHub Copilot"Migrate from ml5.js to tensorflow.js"and it did the work!

It was quite a smooth process when migrating. Sometimes there were errors during the migration such as:

Uncaught (in promise) TypeError: Cannot read properties of undefined (reading 'NotAI')

Even with that, it was able to fix the issue relatively fast without the need for me to undo everything and re-prompt it(which is the biggest issue when working with AI).

 

Overall, it was nice to see GitHub Copilot being able to migrate, fix errors, and ensure the code-base cleanly migrates without any issues.

However,token usage has been burning faster than before when I used it in a previous DEV challenge where we used GitHub Copilot.I am not sure if there is a change in policy of how many tokens are being burnt, but it is one thing I noticed. Other than that, it was a good experience!

 

 

# Summary

In conclusion, this is the project we built with the intention of reducing the number of AI-generated content on DEV. Additionally, we intended for this project to diversify content and enhance the user's experience when it comes to connecting and growing as a developer.

Not only did we create this project with the intention of helping the community, but we also learned new things when working on the project.

For me,I learned about the responsibility as a project maintainer and being able to communicate with my partner on the tasks that needed to be completed as well as considering the time zone we live in(I am based in the US while Elmar is based in the Philippines). Additionally, as this is Elmar's first time seeing my existing code,I learned not to over explain my code and to be as simple and straightforward as possible when it comes to delivering tasks to Elmar and reviewing his Pull Requests.

 

For Elmar, this is his statement about this project overall:

### Navigating My First Open Source Chrome Extension Codebase

Working on someone else's codebase was a completely different challenge.

At times, it felt like I was walking on glass, afraid to mess something up.

It forced me to slow down and read the codebase first. While ChatGPT helped me understand concepts and unfamiliar parts of the code.

I've had experience reviewing other people's code through Frontend Mentor, but this felt very different. When contributing to a real project, every change has consequences. I found myself asking more questions than usual and learning the answers along the way.

One thing I learned even more than the codebase itself was the importance of communication. I spent a lot of time discussing ideas, asking questions, and seeking clarification from the maintainer.

Looking back, I think the cycle of asking, learning, understanding, and validating took far more time than writing the code itself.

I also learned the importance of being adaptable. The project evolved during my contribution journey, which meant my assumptions and plans had to evolve as well. On top of that, I encountered my first real merge conflicts but I managed to pull through in the end.

Overall, contributing to ClassifierAI gave me a much better understanding of how real-world software development differs from building projects alone.

Beyond the technical skills, I learned how to collaborate with maintainers and communicate changes through pull requests.

This experience yet again proved what I read early on in my career:

"The ability to read and understand code is often more valuable than the ability to write it."

Although we have learn a lot, there are still current issues that I believe it is important to address when using this Chrome Extension.

## Current Challenges in our Chrome Extension

As mentioned many times before, this project is a prototype for many reasons. Right now:

* The model and the dataset is not aligned to what we have on dev.to.In detail, the dataset comes from the Wikipedia while the dataset for images comes from HuggingFace. Both of these dataset are not accurate to the dev.to platform. We hope, with more collaboration, to get data from dev.to and retrain the model that is more accurate than before and align to value of the DEV community.
* Limited features to the users such as which area in the article is AI-generated and which is not.Also, not accounting for when it is appropriate to use AI such as using AI as a translation, grammatical checks, etc.

With that said, we hope you see the value in our work and contributing to this project further!

 

 

# Thank You!

Thank you for reading our poston our Chrome Extension Project! It was fun to work with Elmar and getting to know him more and his current knowledge as a developer!

If you would love to contribute to our Chrome Extension, feel free to visit the repository below. Your contribution matters to dev.to! Feel free to provide any feature requests and issues you may notice!

## FrancisTR/ClassifierAI

### A Chrome Extension that detects AI-generated images using Machine Learning.

# Welcome to the ClassifierAI Repository!

## Description

A Google Chrome Extension that integrates Machine Learning to determine if the image and the dev.to article, that the user is viewing, is AI-Generated. This uses Tensorflow.js to perform Image Classification and Text Classification.

The model is trained usingTeachable Machineby Google where it is train from 866 images, that consists of AI and Non-AI images, using the following settings:

* Epochs: 30
* Batch Size: 16
* Learning Rate: 0.0001

## Technologies Used

Core Tech:

Content Analysis:

Extension Tooling:

## How to Run

1. Clone or download the repository and navigate to the project directory.
2. Install the project dependencies:npm installEnter fullscreen modeExit fullscreen mode
3. Build the extension:npm run buildEnter fullscreen modeExit fullscreen mode
4. Open Google Chrome and navigate to:chrome://extensions
5. EnableDeveloper Modein the top-right corner.
6. ClickLoad unpackedand select the generateddist/folder.
7. The extension is now installed and ready to use.

## Demo

### Installation

### Usage

## Contributing

ClassifierAI is an open-source project…

View on GitHub

 

I hope this project will be useful for you and inspire you to build something that will make an impact! Thanks for stopping by!

 

Follow The DEVengers Organization!

## The DEVengersFollow

 This is an organization where we assemble the greatest minds the community has ever known! The question isn't "How fast can I code?". The question is "What will I learn from the farthest below?".
 

Check out Elmar Chavez!

## Elmar ChavezFollow

Licensed civil engineer turned full stack developer building accessible, responsive web applications. I also review code in Frontend Mentor and participate in collaborative projects.

 

 

Any questions/comments? I would love to hear from you!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (28 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse