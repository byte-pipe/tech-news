---
title: 'GitHub - microsoft/AI-For-Beginners: 12 Weeks, 24 Lessons, AI for All! · GitHub'
url: https://github.com/microsoft/AI-For-Beginners
site_name: github
content_file: github-github-microsoftai-for-beginners-12-weeks-24-lesso
fetched_at: '2026-06-30T11:55:35.497403'
original_url: https://github.com/microsoft/AI-For-Beginners
author: microsoft
description: 12 Weeks, 24 Lessons, AI for All! Contribute to microsoft/AI-For-Beginners development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 microsoft

 

/

AI-For-Beginners

Public

* NotificationsYou must be signed in to change notification settings
* Fork10.1k
* Star48.9k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

1,171 Commits
1,171 Commits
.devcontainer
.devcontainer
 
 
.github/
workflows
.github/
workflows
 
 
binder
binder
 
 
data
data
 
 
etc
etc
 
 
examples
examples
 
 
images
images
 
 
lessons
lessons
 
 
translated_images
translated_images
 
 
translations
translations
 
 
.gitignore
.gitignore
 
 
.nojekyll
.nojekyll
 
 
AGENTS.md
AGENTS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
environment.yml
environment.yml
 
 
index.html
index.html
 
 
requirements.txt
requirements.txt
 
 
troubleshoot.md
troubleshoot.md
 
 
View all files

## Repository files navigation

# Artificial Intelligence for Beginners - A Curriculum

AI For Beginners - 
Sketchnote by 
@girlie_mac

Explore the world ofArtificial Intelligence(AI) with our 12-week, 24-lesson curriculum! It includes practical lessons, quizzes, and labs. The curriculum is beginner-friendly and covers tools like TensorFlow and PyTorch, as well as ethics in AI

### 🌐 Multi-Language Support

#### Supported via GitHub Action (Automated & Always Up-to-Date)

Arabic|Bengali|Bulgarian|Burmese (Myanmar)|Chinese (Simplified)|Chinese (Traditional, Hong Kong)|Chinese (Traditional, Macau)|Chinese (Traditional, Taiwan)|Croatian|Czech|Danish|Dutch|Estonian|Finnish|French|German|Greek|Hebrew|Hindi|Hungarian|Indonesian|Italian|Japanese|Kannada|Khmer|Korean|Lithuanian|Malay|Malayalam|Marathi|Nepali|Nigerian Pidgin|Norwegian|Persian (Farsi)|Polish|Portuguese (Brazil)|Portuguese (Portugal)|Punjabi (Gurmukhi)|Romanian|Russian|Serbian (Cyrillic)|Slovak|Slovenian|Spanish|Swahili|Swedish|Tagalog (Filipino)|Tamil|Telugu|Thai|Turkish|Ukrainian|Urdu|Vietnamese

Prefer to Clone Locally?

This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:

Bash / macOS / Linux:

git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git

cd
 AI-For-Beginners
git sparse-checkout 
set
 --no-cone 
'
/*
'
 
'
!translations
'
 
'
!translated_images
'

CMD (Windows):

git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git

cd
 AI-For-Beginners
git sparse-checkout 
set
 --no-cone 
"
/*
"
 
"
!translations" "!
translated_images
"

This gives you everything you need to complete the course with a much faster download.

If you wish to have additional translations languages supported are listedhere

## Join the Community

## What you will learn

Mindmap of the Course

In this curriculum, you will learn:

* Different approaches to Artificial Intelligence, including the "good old" symbolic approach withKnowledge Representationand reasoning (GOFAI).
* Neural NetworksandDeep Learning, which are at the core of modern AI. We will illustrate the concepts behind these important topics using code in two of the most popular frameworks -TensorFlowandPyTorch.
* Neural Architecturesfor working with images and text. We will cover recent models but may be a bit lacking in the state-of-the-art.
* Less popular AI approaches, such asGenetic AlgorithmsandMulti-Agent Systems.

What we will not cover in this curriculum:

Find all additional resources for this course in our Microsoft Learn collection

* Business cases of usingAI in Business. Consider takingIntroduction to AI for business userslearning path on Microsoft Learn, orAI Business School, developed in cooperation withINSEAD.
* Classic Machine Learning, which is well described in ourMachine Learning for Beginners Curriculum.
* Practical AI applications built usingCognitive Services. For this, we recommend that you start with modules Microsoft Learn forvision,natural language processing,Generative AI with Azure OpenAI Serviceand others.
* Specific MLCloud Frameworks, such asAzure Machine Learning,Microsoft Fabric, orAzure Databricks. Consider usingBuild and operate machine learning solutions with Azure Machine LearningandBuild and Operate Machine Learning Solutions with Azure Databrickslearning paths.
* Conversational AIandChat Bots. There is a separateCreate conversational AI solutionslearning path, and you can also refer tothis blog postfor more detail.
* Deep Mathematicsbehind deep learning. For this, we would recommendDeep Learningby Ian Goodfellow, Yoshua Bengio and Aaron Courville, which is also available online athttps://www.deeplearningbook.org/.

For a gentle introduction toAI in the Cloudtopics you may consider taking theGet started with artificial intelligence on AzureLearning Path.

# Content

Lesson Link

PyTorch/Keras/TensorFlow

Lab

0

Course Setup

Setup Your Development Environment

I

Introduction to AI

01

Introduction and History of AI

-

-

II

Symbolic AI

02

Knowledge Representation and Expert Systems

Expert Systems
 / 
Ontology
 /
Concept Graph

III

Introduction to Neural Networks

03

Perceptron

Notebook

Lab

04

Multi-Layered Perceptron and Creating our own Framework

Notebook

Lab

05

Intro to Frameworks (PyTorch/TensorFlow) and Overfitting

PyTorch
 / 
Keras
 / 
TensorFlow

Lab

IV

Computer Vision

PyTorch
 / 
TensorFlow

Explore Computer Vision on Microsoft Azure

06

Intro to Computer Vision. OpenCV

Notebook

Lab

07

Convolutional Neural Networks
 & 
CNN Architectures

PyTorch
 /
TensorFlow

Lab

08

Pre-trained Networks and Transfer Learning
 and 
Training Tricks

PyTorch
 / 
TensorFlow

Lab

09

Autoencoders and VAEs

PyTorch
 / 
TensorFlow

10

Generative Adversarial Networks & Artistic Style Transfer

PyTorch
 / 
TensorFlow

11

Object Detection

TensorFlow

Lab

12

Semantic Segmentation. U-Net

PyTorch
 / 
TensorFlow

V

Natural Language Processing

PyTorch
 /
TensorFlow

Explore Natural Language Processing on Microsoft Azure

13

Text Representation. Bow/TF-IDF

PyTorch
 / 
TensorFlow

14

Semantic word embeddings. Word2Vec and GloVe

PyTorch
 / 
TensorFlow

15

Language Modeling. Training your own embeddings

PyTorch
 / 
TensorFlow

Lab

16

Recurrent Neural Networks

PyTorch
 / 
TensorFlow

17

Generative Recurrent Networks

PyTorch
 / 
TensorFlow

Lab

18

Transformers. BERT.

PyTorch
 /
TensorFlow

19

Named Entity Recognition

TensorFlow

Lab

20

Large Language Models, Prompt Programming and Few-Shot Tasks

PyTorch

VI

Other AI Techniques

21

Genetic Algorithms

Notebook

22

Deep Reinforcement Learning

PyTorch
 /
TensorFlow

Lab

23

Multi-Agent Systems

VII

AI Ethics

24

AI Ethics and Responsible AI

Microsoft Learn: Responsible AI Principles

IX

Extras

25

Multi-Modal Networks, CLIP and VQGAN

Notebook

## Each lesson contains

* Pre-reading material
* Executable Jupyter Notebooks, which are often specific to the framework (PyTorchorTensorFlow). The executable notebook also contains a lot of theoretical material, so to understand the topic you need to go through at least one version of the notebook (either PyTorch or TensorFlow).
* Labsavailable for some topics, which give you an opportunity to try applying the material you have learned to a specific problem.
* Some sections contain links toMS Learnmodules that cover related topics.

## Getting Started

### 🎯 New to AI? Start Here!

If you're completely new to AI and want quick, hands-on examples, check out ourBeginner-Friendly Examples! These include:

* 🌟Hello AI World- Your first AI program (pattern recognition)
* 🧠Simple Neural Network- Build a neural network from scratch
* 🖼️Image Classifier- Classify images with detailed comments
* 💬Text Sentiment- Analyze positive/negative text

These examples are designed to help you understand AI concepts before diving into the full curriculum.

### 📚 Full Curriculum Setup

* We have created asetup lessonto help you with setting up your development environment. - For Educators, we have created acurricula setup lessonfor you too!
* How toRun the code in a VSCode or a Codespace

Follow these steps:

Fork the Repository: Click on the "Fork" button at the top-right corner of this page.

Clone the Repository:git clone https://github.com/microsoft/AI-For-Beginners.git

Don't forget to star (🌟) this repo to find it easier later.

## Meet other Learners

Join ourofficial AI Discord serverto meet and network with other learners taking this course and get support.

If you have product feedback or questions whilst building visit ourAzure AI Foundry Developer Forum

## Quizzes

A note about quizzes: All quizzes are contained in the Quiz-app folder in etc\quiz-app, orOnline HereThey are linked from within the lessons the quiz app can be run locally or deployed to Azure; follow the instruction in thequiz-appfolder. They are gradually being localized.

## Help Wanted

Do you have suggestions or found spelling or code errors? Raise an issue or create a pull request.

## Special Thanks

* ✍️ Primary Author:Dmitry Soshnikov, PhD
* 🔥 Editor:Jen Looper, PhD
* 🎨 Sketchnote illustrator:Tomomi Imura
* ✅ Quiz Creator:Lateefah Bello,MLSA
* 🙏 Core Contributors:Evgenii Pishchik

## Other Curricula

Our team produces other curricula! Check out:

### LangChain

### Azure / Edge / MCP / Agents

### Generative AI Series

### Core Learning

### Copilot Series

## Getting Help

If you get stuck or have any questions about building AI apps. Join fellow learners and experienced developers in discussions about MCP. It's a supportive community where questions are welcome and knowledge is shared freely.

If you have product feedback or errors while building visit:

## About

12 Weeks, 24 Lessons, AI for All!

### Topics

 nlp

 machine-learning

 ai

 computer-vision

 deep-learning

 cnn

 artificial-intelligence

 gan

 rnn

 microsoft-for-beginners

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

48.9k

 stars
 

### Watchers

523

 watching
 

### Forks

10.1k

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Jupyter Notebook100.0%
* Python0.0%
* HTML0.0%
* Vue0.0%
* JavaScript0.0%
* Dockerfile0.0%