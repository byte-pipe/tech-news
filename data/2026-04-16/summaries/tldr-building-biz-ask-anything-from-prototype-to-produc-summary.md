---
title: Building Biz Ask Anything: From Prototype to Product
url: https://engineeringblog.yelp.com/2026/03/building-baa-from-prototype-to-product.html
date: 2026-04-16
site: tldr
model: llama3.2:1b
summarized_at: 2026-04-16T06:13:11.529681
---

# Building Biz Ask Anything: From Prototype to Product

# Building Biz Ask Anything: From Prototype to Product

**Introduction**

Yelp has long struggled to connect users with the information they need quickly and accurately on its business pages. The absence of a simple answer option led to frustration for users who wanted to know more about a specific business before deciding whether or not to visit.

* **Maria Christoforaki, Group Tech Lead; Shree Shalini Pusapati, Software Engineer**
Mar 27, 2026

## Understanding the Problem

The existing search functionality on Yelp business pages failed to capture users' expectations for immediate and direct answers. The system relied heavily on manual curation of content, which was time-consuming and not efficient.

* **Users**: Now expect instant information
* **Expectations**: People seek straightforward facts without excessive searching

## Proposed Solution

To address these challenges, the team developed a new AI-powered chatbot called Yelp Assistant. This solution aims to provide users with accurate, evidence-backed answers that preserve the value of in-depth reviews.

**Key Features**

1.  **Business Question Answering**: Yelp Assistant can identify and answer questions on business pages about any topic.
2.  **Data Abundance Challenge**: The tool simplifies the information retrieval process by using Large Language Models (LLMs).
3.  **Answer Preservation**: AI ensures that users receive a direct answer while respecting in-depth reviews.

## Case Studies

### Figure 1: Example Question and Answer
*   A user wants to know about a new restaurant.
*   Yelp Assistant analyzes the question and retrieves relevant information from its vast knowledge base, such as menu items, opening hours, and customer reviews.

### Section Discussion

A. **Answering the "Tell me 5 things I should know..." Question**
The approach employs AI-driven content retrieval to address questions of general interest about specific businesses. This strategy leverages large language models to infer relevant information directly from user queries.

B. **Explaining Why the Business is "Good for Kids?"**
This example showcases how Yelp Assistant uses structured data, combined with natural language processing, to provide users with accurate and informative responses based on context.

C. **Recommending a Dinner Plan**
In this scenario, AI-driven system takes into account various dietary restrictions ( vegetarian), ingredient limitations, etc., while generating a 3-course reservation in the user's preferred setting.

For more information or resources related to Yelp Assistant, please refer to the following link: https://yelp-assistant.com