---
title: 'GitHub - chiphuyen/aie-book: [WIP] Resources for AI engineers. Also contains supporting materials for the book AI Engineering (Chip Huyen, 2025) · GitHub'
url: https://github.com/chiphuyen/aie-book
site_name: github
content_file: github-github-chiphuyenaie-book-wip-resources-for-ai-engi
fetched_at: '2026-04-23T20:05:50.332526'
original_url: https://github.com/chiphuyen/aie-book
author: chiphuyen
description: '[WIP] Resources for AI engineers. Also contains supporting materials for the book AI Engineering (Chip Huyen, 2025) - chiphuyen/aie-book'
---

chiphuyen

 

/

aie-book

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.2k
* Star15.1k

 
 
 
 
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

28 Commits
28 Commits
assets
assets
 
 
scripts
scripts
 
 
.DS_Store
.DS_Store
 
 
.gitignore
.gitignore
 
 
README.md
README.md
 
 
ToC.md
ToC.md
 
 
ToC.pdf
ToC.pdf
 
 
appendix.md
appendix.md
 
 
case-studies.md
case-studies.md
 
 
chapter-summaries.md
chapter-summaries.md
 
 
misalignment.md
misalignment.md
 
 
prompt-examples.md
prompt-examples.md
 
 
resources.md
resources.md
 
 
study-notes.md
study-notes.md
 
 
View all files

## Repository files navigation

# AI Engineering book and other resources

This repo will be updated with more resources in the next few weeks.

* About the book AI EngineeringTable of contentsChapter summariesStudy notes
* Table of contents
* Chapter summaries
* Study notes
* AI engineering resources
* Prompt examples
* Case studies
* Misalignment AI
* Appendix
* Fun tools:ChatGPT and Claude conversation heatmap generator
* ChatGPT and Claude conversation heatmap generator
* And more ...

## About the book

The availability of foundation models has transformed AI from a specialized discipline into a powerful development tool everyone can use. This book covers the end-to-end process of adapting foundation models to solve real-world problems, encompassing tried-and-true techniques from other engineering fields and techniques emerging with foundation models.

The book is available on:

* Amazon
* O'Reilly
* Kindle

and most places where technical books are sold.

This is NOT a tutorial book, so it doesn't have a lot of code snippets.

## What this book is about

This book provides a framework for adapting foundation models, which include both large language models (LLMs) and large multimodal models (LMMs), to specific applications. It not only outlines various solutions for building an AI application but also raises questions you can ask to evaluate the best solution for your needs. Here are just some of the many questions that this book can help you answer:

1. Should I build this AI application?
2. How do I evaluate my application? Can I use AI to evaluate AI outputs?
3. What causes hallucinations? How do I detect and mitigate hallucinations?
4. What are the best practices for prompt engineering?
5. Why does RAG work? What are the strategies for doing RAG?
6. What’s an agent? How do I build and evaluate an agent?
7. When to finetune a model? When not to finetune a model?
8. How much data do I need? How do I validate the quality of my data?
9. How do I make my model faster, cheaper, and secure?
10. How do I create a feedback loop to improve my application continually?

The book will also help you navigate the overwhelming AI landscape: types of models, evaluation benchmarks, and a seemingly infinite number of use cases and application patterns.

The content in this book is illustrated using actual case studies, many of which I’ve worked on, backed by ample references and extensively reviewed by experts from a wide range of backgrounds. Even though the book took two years to write, it draws from my experience working with language models and ML systems from the last decade.

Like my previous book,Designing Machine Learning Systems (DMLS), this book focuses on the fundamentals of AI engineering instead of any specific tool or API. Tools become outdated quickly, but fundamentals should last longer.

### ReadingAI Engineering(AIE) withDesigning Machine Learning Systems(DMLS)

AIE can be a companion to DMLS. DMLS focuses on building applications on top of traditional ML models, which involves more tabular data annotations, feature engineering, and model training. AIE focuses on building applications on top of foundation models, which involves more prompt engineering, context construction, and parameter-efficient finetuning. Both books are self-contained and modular, so you can read either book independently.

Since foundation models are ML models, some concepts are relevant to working with both. If a topic is relevant to AIE but has been discussed extensively in DMLS, it’ll still be covered in this book, but to a lesser extent, with pointers to relevant resources.

Note that many topics are covered in DMLS but not in AIE, and vice versa. The first chapter of this book also covers the differences between traditional ML engineering and AI engineering.

A real-world system often involves both traditional ML models and foundation models, so knowledge about working with both is often necessary.

## Who this book is for

This book is for anyone who wants to leverage foundation models to solve real-world problems. This is a technical book, so the language of this book is geared towards technical roles, including AI engineers, ML engineers, data scientists, engineering managers, and technical product managers. This book is for you if you can relate to one of the following scenarios:

* You’re building or optimizing an AI application, whether you’re starting from scratch or looking to move beyond the demo phase into a production-ready stage. You may also be facing issues like hallucinations, security, latency, or costs, and need targeted solutions.
* You want to streamline your team’s AI development process, making it more systematic, faster, and reliable.
* You want to understand how your organization can leverage foundation models to improve the business’s bottom line and how to build a team to do so.

You can also benefit from the book if you belong to one of the following groups:

* Tool developers who want to identify underserved areas in AI engineering to position your products in the ecosystem.
* Researchers who want to understand better AI use cases.
* Job candidates seeking clarity on the skills needed to pursue a career as an AI engineer.
* Anyone wanting to better understand AI's capabilities and limitations, and how it might affect different roles.

I love getting to the bottom of things, so some sections dive a bit deeper into the technical side. While many early readers like the detail, I know it might not be for everyone. I’ll give you a heads-up before things get too technical. Feel free to skip ahead if it feels a little too in the weeds!

## Reviews

* "This book offers a comprehensive, well-structured guide to the essential aspects of building generative AI systems. A must-read for any professional looking to scale AI across the enterprise."- Vittorio Cretella, former global CIO at P&G and Mars
* "Chip Huyen gets generative AI. She is a remarkable teacher and writer whose work has been instrumental in helping teams bring AI into production. Drawing on her deep expertise, AI Engineering is a comprehensive and holistic guide to building generative AI applications in production."- Luke Metz, co-creator of ChatGPT, ex-research manager @ OpenAI
* "Every AI engineer building real-world applications should read this book. It’s a vital guide to end-to-end AI system design, from model development and evaluation to large-scale deployment and operation."- Andrei Lopatenko, Director Search and AI, Neuron7
* "This book serves as an essential guide for building AI products that can scale. Unlike other books that focus on tools or current trends that are constantly changing, Chip delivers timeless foundational knowledge. Whether you're a product manager or an engineer, this book effectively bridges the collaboration gap between cross-functional teams, making it a must-read for anyone involved in AI development."- Aileen Bui, AI Product Operations Manager, Google
* "This is the definitive segue into AI Engineering from one of the greats of ML Engineering! Chip has seen through successful projects and careers at every stage of a company and for the first time ever condensed her expertise for new AI Engineers entering the field."- swyx, Curator, AI.Engineer
* "AI Engineering is a practical guide that provides the most up-to-date information on AI development, making it approachable for novice and expert leaders alike. This book is an essential resource for anyone looking to build robust and scalable AI systems."- Vicki Reyzelman, Chief AI Solutions Architect, Mave Sparks
* "AI Engineering is a comprehensive guide that serves as an essential reference for both understanding and implementing AI systems in practice."- Han Lee, Director - Data Science, Moody's.
* "AI Engineering is an essential guide for anyone building software with Generative AI! It demystifies the technology, highlights the importance of evaluation, and shares what should be done to achieve quality before starting with costly fine-tuning."- Rafal Kawala, Senior AI Engineering Director, 16 years of experience working in a Fortune 500 company

See what people are talking about the book on Twitter@aisysbooks!

## Acknowledgments

This book would've taken a lot longer to write and missed many important topics if it wasn't for so many wonderful people who helped me through the process.

Because the timeline for the project was tight—two years for a 150,000-word book that covers so much ground—I'm grateful to the technical reviewers who put aside their precious time to review this book so quickly.

Luke Metzis an amazing soundboard who checked my assumptions and prevented me from going down the wrong path.Han-chung Lee, always up to date with the latest AI news and community development, pointed me toward resources that I missed. Luke and Han were the first to review my drafts before I sent them to the next round of technical reviewers, and I'm forever indebted to them for tolerating my follies and mistakes.

Having led AI innovation at Fortune 500 companies,Vittorio CretellaandAndrei Lopatenkoprovided invaluable feedback that combined deep technical expertise with executive insights.Vicki Reyzelmanhelped me ground my content and keep it relevant for readers with a software engineering background.

Eugene Yan, a dear friend and amazing applied scientist, provided me with technical and emotional support. Shawn Wang (swyx), provided an important vibe check that helped me feel more confident about the book.Sanyam Bhutaniis one of the best learners and most humble souls I know, who not only gave thoughtful written feedback but also recorded videos to explain his feedback.

Kyle Krannen is a star deep learning lead who interviewed his colleagues and shared with me an amazing writeup about their finetuning process, which guided the finetuning chapter.Mark Saroufim, an inquisitive mind who always has his pulse on the most interesting problems, introduced me to great resources on efficiency. Both Kyle and Mark's feedback was critical in writing Chapters 7 and 9.

Kittipat "Bot" Kampa, on top of answering my many questions, shared with me a detailed visualization of how he thinks about AI platform. I appreciateDenys Linkov's systematic approach to evaluation and platform development.Chetan Tekurgave great examples that helped me structure AI application patterns. I'd also like to thankAlex (Shengzhi Li) LiandHien Luufor their thoughtful feedback on my draft on AI architecture.

Aileen Buiis a treasure who shared unique feedback and examples from a product manager's perspective. ThanksTodor Markovfor the actionable advice on the RAG and Agents chapter. ThanksTal Kachmanfor jumping in at the last minute to push the finetuning chapter over the finish line.

There are so many wonderful people whose company and conversations gave me ideas that guide the content of this book. I tried my best to include the names of everyone who has helped me here, but due to the inherent faultiness of human memory, I undoubtedly neglected to mention many. If I forgot to include your name, please know that it wasn't because I don't appreciate your contribution, and please kindly remind me so that I can rectify as soon as possible!

Andrew Francis, Anish Nag,Anthony Galczak,Anton Bacaj, Balázs Galambosi, Charles Frye, Charles Packer, Chris Brousseau, Eric Hartford, Goku Mohandas, Hamel Husain, Harpreet Sahota, Hassan El Mghari, Huu Nguyen, Jeremy Howard, Jesse Silver, John Cook,Juan Pablo Bottaro, Kyle Gallatin, Lance Martin, Lucio Dery, Matt Ross, Maxime Labonne, Miles Brundage, Nathan Lambert, Omar Khattab,Phong Nguyen, Purnendu Mukherjee, Sam Reiswig, Sebastian Raschka, Shahul ES, Sharif Shameem, Soumith Chintala, Teknium, Tim Dettmers, Undi5, Val Andrei Fajardo, Vern Liang, Victor Sanh, Wing Lian, Xiquan Cui, Ying Sheng, and Kristofer.

I'd like to thank all early readers who have also reached out with feedback. Douglas Bailley is a super reader who shared so much thoughtful feedback. Nutan Sahoo for suggesting an elegant way to explain perplexity.

I learned so much from the online discussions with so many. Thanks to everyone who's ever answered my questions, commented on my posts, or sent me an email with your thoughts.

Of course, the book wouldn't have been possible without the team at O'Reilly, especially my development editors (Melissa Potter, Corbin Collins, Jill Leonard) and my production editors (Kristen Brown and Elizabeth Kelly). Liz Wheeler is the most discerning editor I've ever worked with. Nicole Butterfield is a force who oversaw this book from an idea to a final product.

This book, after all, is an accumulation of invaluable lessons I learned throughout my career. I owe these lessons to my extremely competent and patient coworkers and former coworkers. Every person I've worked with has taught me something new about bringing ML into the world.

Chip Huyen,AI Engineering. O'Reilly Media, 2025.

@book{aiebook2025, 
 address = {USA}, 
 author = {Chip Huyen}, 
 isbn = {978-1801819312}, 
 publisher = {O'Reilly Media}, 
 title = {{AI Engineering}}, 
 year = {2025} 
}

## About

[WIP] Resources for AI engineers. Also contains supporting materials for the book AI Engineering (Chip Huyen, 2025)

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

15.1k

 stars
 

### Watchers

237

 watching
 

### Forks

2.2k

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors5

## Languages

* Jupyter Notebook100.0%