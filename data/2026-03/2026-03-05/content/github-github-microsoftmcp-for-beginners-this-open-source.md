---
title: 'GitHub - microsoft/mcp-for-beginners: This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration. · GitHub'
url: https://github.com/microsoft/mcp-for-beginners
site_name: github
content_file: github-github-microsoftmcp-for-beginners-this-open-source
fetched_at: '2026-03-05T11:15:59.583814'
original_url: https://github.com/microsoft/mcp-for-beginners
author: microsoft
description: This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration. - microsoft/mcp-for-beginners
---

microsoft



/

mcp-for-beginners

Public

* NotificationsYou must be signed in to change notification settings
* Fork4.8k
* Star14.7k




 
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

1,831 Commits
1,831 Commits
.devcontainer
.devcontainer
 
 
.github/
ISSUE_TEMPLATE
.github/
ISSUE_TEMPLATE
 
 
00-Introduction
00-Introduction
 
 
01-CoreConcepts
01-CoreConcepts
 
 
02-Security
02-Security
 
 
03-GettingStarted
03-GettingStarted
 
 
04-PracticalImplementation
04-PracticalImplementation
 
 
05-AdvancedTopics
05-AdvancedTopics
 
 
06-CommunityContributions
06-CommunityContributions
 
 
07-LessonsfromEarlyAdoption
07-LessonsfromEarlyAdoption
 
 
08-BestPractices
08-BestPractices
 
 
09-CaseStudy
09-CaseStudy
 
 
10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit
10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit
 
 
11-MCPServerHandsOnLabs
11-MCPServerHandsOnLabs
 
 
images
images
 
 
translated_images
translated_images
 
 
translations
translations
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
changelog.md
changelog.md
 
 
study_guide.md
study_guide.md
 
 
View all files

## Repository files navigation

Follow these steps to get started using these resources:

1. Fork the Repository: Click
2. Clone the Repository:git clone https://github.com/microsoft/mcp-for-beginners.git
3. Join The

### 🌐 Multi-Language Support

#### Supported via GitHub Action (Automated & Always Up-to-Date)

Arabic|Bengali|Bulgarian|Burmese (Myanmar)|Chinese (Simplified)|Chinese (Traditional, Hong Kong)|Chinese (Traditional, Macau)|Chinese (Traditional, Taiwan)|Croatian|Czech|Danish|Dutch|Estonian|Finnish|French|German|Greek|Hebrew|Hindi|Hungarian|Indonesian|Italian|Japanese|Kannada|Korean|Lithuanian|Malay|Malayalam|Marathi|Nepali|Nigerian Pidgin|Norwegian|Persian (Farsi)|Polish|Portuguese (Brazil)|Portuguese (Portugal)|Punjabi (Gurmukhi)|Romanian|Russian|Serbian (Cyrillic)|Slovak|Slovenian|Spanish|Swahili|Swedish|Tagalog (Filipino)|Tamil|Telugu|Thai|Turkish|Ukrainian|Urdu|Vietnamese

Prefer to Clone Locally?

This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:

Bash / macOS / Linux:

git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git

cd
 mcp-for-beginners
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

git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git

cd
 mcp-for-beginners
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

# 🚀 Model Context Protocol (MCP) Curriculum for Beginners

## Learn MCP with Hands-on Code Examples in C#, Java, JavaScript, Rust, Python, and TypeScript

## 🧠 Overview of the Model Context Protocol Curriculum

Welcome to your journey into the Model Context Protocol! If you've ever wondered how AI applications communicate with different tools and services, you're about to discover the elegant solution that's transforming how developers build intelligent systems.

Think of MCP as a universal translator for AI applications - just like how USB ports let you connect any device to your computer, MCP lets AI models connect to any tool or service in a standardized way. Whether you're building your first chatbot or working on complex AI workflows, understanding MCP will give you the power to create more capable and flexible applications.

This curriculum is designed with patience and care for your learning journey. We'll start with simple concepts you already understand and gradually build your expertise through hands-on practice in your favorite programming language. Every step includes clear explanations, practical examples, and plenty of encouragement along the way.

By the time you complete this journey, you'll have the confidence to build your own MCP servers, integrate them with popular AI platforms, and understand how this technology is reshaping the future of AI development. Let's begin this exciting adventure together!

### Official Documentation and Specifications

This curriculum is aligned withMCP Specification 2025-11-25(the latest stable release). The MCP specification uses date-based versioning (YYYY-MM-DD format) to ensure clear protocol version tracking.

These resources become more valuable as your understanding grows, but don't feel pressured to read everything immediately. Start with the areas that interest you most!

* 📘MCP Documentation– This is your go-to resource for step-by-step tutorials and user guides. The documentation is written with beginners in mind, providing clear examples you can follow along with at your own pace.
* 📜MCP Specification– Think of this as your comprehensive reference manual. As you work through the curriculum, you'll find yourself returning here to look up specific details and explore advanced features.
* 📜MCP Specification Versioning– This contains information about protocol version history and how MCP uses date-based versioning (YYYY-MM-DD format).
* 🧑‍💻MCP GitHub Repository– Here you'll find SDKs, tools, and code samples in multiple programming languages. It's like a treasure trove of practical examples and ready-to-use components.
* 🌐MCP Community– Join fellow learners and experienced developers in discussions about MCP. It's a supportive community where questions are welcome and knowledge is shared freely.

## Learning Objectives

By the end of this curriculum, you'll feel confident and excited about your new abilities. Here's what you'll achieve:

•Understand MCP fundamentals: You'll grasp what the Model Context Protocol is and why it's revolutionizing how AI applications work together, using analogies and examples that make sense.

•Build your first MCP server: You'll create a working MCP server in your preferred programming language, starting with simple examples and growing your skills step by step.

•Connect AI models to real tools: You'll learn how to bridge the gap between AI models and actual services, giving your applications powerful new capabilities.

•Implement security best practices: You'll understand how to keep your MCP implementations safe and secure, protecting both your applications and your users.

•Deploy with confidence: You'll know how to take your MCP projects from development to production, with practical deployment strategies that work in the real world.

•Join the MCP community: You'll become part of a growing community of developers who are shaping the future of AI application development.

## Essential Background

Before we dive into MCP specifics, let's make sure you feel comfortable with some foundational concepts. Don't worry if you're not an expert in these areas - we'll explain everything you need to know as we go!

### Understanding Protocols (The Foundation)

Think of a protocol like the rules for a conversation. When you call a friend, you both know to say "hello" when you answer, take turns speaking, and say "goodbye" when you're done. Computer programs need similar rules to communicate effectively.

MCP is a protocol - a set of agreed-upon rules that help AI models and applications have productive "conversations" with tools and services. Just like how having conversation rules makes human communication smoother, having MCP makes AI application communication much more reliable and powerful.

### Client-Server Relationships (How Programs Work Together)

You already use client-server relationships every day! When you use a web browser (the client) to visit a website, you're connecting to a web server that sends you the page content. The browser knows how to ask for information, and the server knows how to respond.

In MCP, we have a similar relationship: AI models act as clients that request information or actions, while MCP servers provide those capabilities. It's like having a helpful assistant (the server) that the AI can ask to perform specific tasks.

### Why Standardization Matters (Making Things Work Together)

Imagine if every car manufacturer used different shaped gas pumps - you'd need a different adapter for each car! Standardization means agreeing on common approaches so things work together seamlessly.

MCP provides this standardization for AI applications. Instead of every AI model needing custom code to work with every tool, MCP creates a universal way for them to communicate. This means developers can build tools once and have them work with many different AI systems.

## 🧭 Your Learning Path Overview

Your MCP journey is carefully structured to build your confidence and skills progressively. Each phase introduces new concepts while reinforcing what you've already learned.

### 🌱 Foundation Phase: Understanding the Basics (Modules 0-2)

This is where your adventure begins! We'll introduce you to MCP concepts using familiar analogies and simple examples. You'll understand what MCP is, why it exists, and how it fits into the larger world of AI development.

•Module 0 - Introduction to MCP: We'll start by exploring what MCP is and why it's so important for modern AI applications. You'll see real-world examples of MCP in action and understand how it solves common problems developers face.

•Module 1 - Core Concepts Explained: Here you'll learn the essential building blocks of MCP. We'll use plenty of analogies and visual examples to make sure these concepts feel natural and understandable.

•Module 2 - Security in MCP: Security might sound intimidating, but we'll show you how MCP includes built-in safety features and teach you best practices that protect your applications from the start.

### 🔨 Building Phase: Creating Your First Implementations (Module 3)

Now the real fun begins! You'll get hands-on experience building actual MCP servers and clients. Don't worry - we'll start simple and guide you through every step.

This module includes multiple hands-on guides that let you practice in your preferred programming language. You'll create your first server, build a client to connect to it, and even integrate with popular development tools like VS Code.

Each guide includes complete code examples, troubleshooting tips, and explanations of why we make specific design choices. By the end of this phase, you'll have working MCP implementations you can be proud of!

### 🚀 Growing Phase: Advanced Concepts and Real-World Application (Modules 4-5)

With the basics mastered, you're ready to explore more sophisticated MCP features. We'll cover practical implementation strategies, debugging techniques, and advanced topics like multi-modal AI integration.

You'll also learn how to scale your MCP implementations for production use and integrate with cloud platforms like Azure. These modules prepare you to build MCP solutions that can handle real-world demands.

### 🌟 Mastery Phase: Community and Specialization (Modules 6-11)

The final phase focuses on joining the MCP community and specializing in areas that interest you most. You'll learn how to contribute to open-source MCP projects, implement advanced authentication patterns, and build comprehensive database-integrated solutions.

Module 11 deserves special mention - it's a complete 13-lab hands-on learning path that teaches you to build production-ready MCP servers with PostgreSQL integration. It's like a capstone project that brings together everything you've learned!

### 📚 Complete Curriculum Structure

Module

Topic

Description

Link

Module 0-3: Fundamentals

00

Introduction to MCP

Overview of the Model Context Protocol and its significance in AI pipelines

Read more

01

Core Concepts Explained

In-depth exploration of core MCP concepts

Read more

02

Security in MCP

Security threats and best practices

Read more

03

Getting Started with MCP

Environment setup, basic servers/clients, integration

Read more

Module 3: Building Your First Server & Client

3.1

First Server

Create your first MCP server

Guide

3.2

First Client

Develop a basic MCP client

Guide

3.3

Client with LLM

Integrate large language models

Guide

3.4

VS Code Integration

Consume MCP servers in VS Code

Guide

3.5

stdio Server

Create servers using stdio transport

Guide

3.6

HTTP Streaming

Implement HTTP streaming in MCP

Guide

3.7

AI Toolkit

Use AI Toolkit with MCP

Guide

3.8

Testing

Test your MCP server implementation

Guide

3.9

Deployment

Deploy MCP servers to production

Guide

3.10

Advanced server usage

Use advanced servers for advanced feature usage and improved architecture

Guide

3.11

Simple auth

A chapter showing you auth from the beginning and RBAC

Guide

3.12

MCP Hosts

Configure Claude Desktop, Cursor, Cline, and other MCP hosts

Guide

3.13

MCP Inspector

Debug and test MCP servers with the Inspector tool

Guide

3.14

Sampling

Use sampling to collaborate with the client

Guide

3.15

MCP Apps

Build MCP Apps

Guide

Module 4-5: Practical & Advanced

04

Practical Implementation

SDKs, debugging, testing, reusable prompt templates

Read more

4.1

Pagination

Handle large result sets with cursor-based pagination

Guide

05

Advanced Topics in MCP

Multi-modal AI, scaling, enterprise use

Read more

5.1

Azure Integration

MCP Integration with Azure

Guide

5.2

Multi-modality

Working with multiple modalities

Guide

5.3

OAuth2 Demo

Implement OAuth2 authentication

Guide

5.4

Root Contexts

Understand and implement root contexts

Guide

5.5

Routing

MCP routing strategies

Guide

5.6

Sampling

Sampling techniques in MCP

Guide

5.7

Scaling

Scale MCP implementations

Guide

5.8

Security

Advanced security considerations

Guide

5.9

Web Search

Implement web search capabilities

Guide

5.10

Realtime Streaming

Build realtime streaming functionality

Guide

5.11

Realtime Search

Implement realtime search

Guide

5.12

Entra ID Auth

Authentication with Microsoft Entra ID

Guide

5.13

Foundry Integration

Integrate with Azure AI Foundry

Guide

5.14

Context Engineering

Techniques for effective context engineering

Guide

5.15

MCP Custom Transport

Custom Transport implementations

Guide

5.16

Protocol Features

Progress notifications, cancellation, resource templates

Guide

Module 6-10: Community & Best Practices

06

Community Contributions

How to contribute to the MCP ecosystem

Guide

07

Insights from Early Adoption

Real-world implementation stories

Guide

08

Best Practices for MCP

Performance, fault-tolerance, resilience

Guide

09

MCP Case Studies

Practical implementation examples

Guide

10

Hands-on Workshop

Building an MCP Server with AI Toolkit

Lab

Module 11: MCP Server Hands On Lab

11

MCP Server Database Integration

Comprehensive 13-lab hands-on learning path for PostgreSQL integration

Labs

11.1

Introduction

Overview of MCP with database integration and retail analytics use case

Lab 00

11.2

Core Architecture

Understanding MCP server architecture, database layers, and security patterns

Lab 01

11.3

Security & Multi-Tenancy

Row Level Security, authentication, and multi-tenant data access

Lab 02

11.4

Environment Setup

Setting up development environment, Docker, Azure resources

Lab 03

11.5

Database Design

PostgreSQL setup, retail schema design, and sample data

Lab 04

11.6

MCP Server Implementation

Building the FastMCP server with database integration

Lab 05

11.7

Tool Development

Creating database query tools and schema introspection

Lab 06

11.8

Semantic Search

Implementing vector embeddings with Azure OpenAI and pgvector

Lab 07

11.9

Testing & Debugging

Testing strategies, debugging tools, and validation approaches

Lab 08

11.10

VS Code Integration

Configuring VS Code MCP integration and AI Chat usage

Lab 09

11.11

Deployment Strategies

Docker deployment, Azure Container Apps, and scaling considerations

Lab 10

11.12

Monitoring

Application Insights, logging, performance monitoring

Lab 11

11.13

Best Practices

Performance optimization, security hardening, and production tips

Lab 12

### 💻 Sample Code Projects

One of the most exciting parts of learning MCP is seeing your code skills develop progressively. We've designed our code examples to start simple and grow more sophisticated as your understanding deepens. Here's how we introduce concepts - with code that's easy to understand but demonstrates real MCP principles, you'll understand not just what this code does, but why it's structured this way and how it fits into larger MCP applications.

#### Basic MCP Calculator Samples

Language

Description

Link

C#

MCP Server Example

View Code

Java

MCP Calculator

View Code

JavaScript

MCP Demo

View Code

Python

MCP Server

View Code

TypeScript

MCP Example

View Code

Rust

MCP Example

View Code

#### Advanced MCP Implementations

Language

Description

Link

C#

Advanced Sample

View Code

Java with Spring

Container App Example

View Code

JavaScript

Advanced Sample

View Code

Python

Complex Implementation

View Code

TypeScript

Container Sample

View Code

## 🎯 Prerequisites for Learning MCP

To get the most out of this curriculum, you should have:

* Basic knowledge of programming in at least one of the following languages: C#, Java, JavaScript, Python, or TypeScript
* Understanding of client-server model and APIs
* Familiarity with REST and HTTP concepts
* (Optional) Background in AI/ML concepts
* Joining our community discussions for support

## 📚 Study Guide & Resources

This repository includes several resources to help you navigate and learn effectively:

### Study Guide

A comprehensiveStudy Guideis available to help you navigate this repository effectively. This visual curriculum map shows how all the topics connect and provides guidance on how to use the sample projects effectively. It's especially helpful if you're a visual learner who likes to see the big picture.

The guide includes:

* A visual curriculum map showing all topics covered
* Detailed breakdown of each repository section
* Guidance on how to use sample projects
* Recommended learning paths for different skill levels
* Additional resources to complement your learning journey

### Changelog

We maintain a detailedChangelogthat tracks all significant updates to the curriculum materials, so you can stay current with the latest improvements and additions.

* New content additions
* Structural changes
* Feature improvements
* Documentation updates

## 🛠️ How to Use This Curriculum Effectively

Each lesson in this guide includes:

1. Clear explanations of MCP concepts
2. Live code examples in multiple languages
3. Exercises to build real MCP applications
4. Extra resources for advanced learners

### Let's Learn MCP with C# - Tutorial Series

Let's learn about the Model Context Protocol (MCP), a cutting-edge framework designed to standardize interactions between AI models and client applications. Through this beginner-friendly session, we'll introduce you to MCP and guide you through creating your first MCP server.

#### C#:https://aka.ms/letslearnmcp-csharp

#### Java:https://aka.ms/letslearnmcp-java

#### JavaScript:https://aka.ms/letslearnmcp-javascript

#### Python:https://aka.ms/letslearnmcp-python

## 🎓 Your MCP Journey Begins

Congratulations! You've just taken the first step in an exciting journey that will expand your programming capabilities and connect you to the cutting edge of AI development.

### What You've Already Accomplished

By reading through this introduction, you've already begun building your MCP knowledge foundation. You understand what MCP is, why it matters, and how this curriculum will support your learning journey. That's a significant achievement and the beginning of your expertise in this important technology.

### The Adventure Ahead

As you progress through the modules, remember that every expert was once a beginner. The concepts that might seem complex now will become second nature as you practice and apply them. Each small step builds toward powerful capabilities that will serve you throughout your development career.

### Your Support Network

You're joining a community of learners and experts who are passionate about MCP and eager to help others succeed. Whether you're stuck on a coding challenge or excited to share a breakthrough, the community is here to support your journey.

If you get stuck or have any questions about building AI apps. Join fellow learners and experienced developers in discussions about MCP. It's a supportive community where questions are welcome and knowledge is shared freely.

If you have product feedback or errors while building visit:

### Ready to Begin?

Your MCP adventure starts now! Begin with Module 0 to dive into your first hands-on MCP experiences, or explore the sample projects to see what you'll be building. Remember - every expert started exactly where you are now, and with patience and practice, you'll be amazed at what you can achieve.

Welcome to the world of Model Context Protocol development. Let's build something amazing together!

## 🤝 Contributing to the Learning Community

This curriculum grows stronger with contributions from learners like you! Whether you're fixing a typo, suggesting a clearer explanation, or adding a new example, your contributions help other beginners succeed.

Thanks to Microsoft Valued ProfessionalShivam Goyalfor contributing code samples.

The contribution process is designed to be welcoming and supportive. Most contributions require a Contributor License Agreement (CLA), but the automated tools will guide you through the process smoothly.

## 📜 Open Source Learning

This entire curriculum is available under the MITLICENSE, meaning you can use, modify, and share it freely. This supports our mission of making MCP knowledge accessible to developers everywhere.

## 🤝 Contribution Guidelines

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visithttps://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted theMicrosoft Open Source Code of Conduct.
For more information see theCode of Conduct FAQor
contactopencode@microsoft.comwith any additional questions or comments.

Ready to start your MCP journey? Begin withModule 00 - Introduction to MCPand take your first steps into the world of Model Context Protocol development!

## 🎒 Other Courses

Our team produces other courses! Check out:

### LangChain

### Azure / Edge / MCP / Agents

### Generative AI Series

### Core Learning

### Copilot Series

## About

This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

### Topics

 javascript

 python

 java

 rust

 typescript

 csharp

 model

 mcp

 javascript-applications

 model-context-protocol

 mcp-server

 modelcontextprotocol

 mcp-client

 mcp-security

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

14.7k

 stars


### Watchers

130

 watching


### Forks

4.8k

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

* Jupyter Notebook85.2%
* TypeScript4.6%
* Python4.4%
* Java2.7%
* C#1.0%
* Rust0.8%
* Other1.3%
