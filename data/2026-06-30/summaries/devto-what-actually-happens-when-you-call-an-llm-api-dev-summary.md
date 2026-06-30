---
title: What Actually Happens When You Call an LLM API - DEV Community
url: https://dev.to/dannwaneri/what-actually-happens-when-you-call-an-llm-api-28l6
date: 2026-06-29
site: devto
model: llama3.2:1b
summarized_at: 2026-06-30T12:03:18.628256
---

# What Actually Happens When You Call an LLM API - DEV Community

# The Journey of an API Call: From Prompt to Response

## Understand the Basics

* Every second, a prompt is typed and sent via wifi.
* The response times vary from seconds to milliseconds due to factors like latency and server processing power.

## Breaking Down the Process

1. **Prompt Generation**:
	* Your device sends a prompt through its internet connection to a nearbyISP.
2. **Fibre Cable Connection**:
	* The prompt travels to a submarine fibre cable, which is used for data transmission across long distances.
3. **Ocean Crossing and Data Centre**:
	* The data centre facility receives the message and routes it to a specific server through multiple fibre cables.

## The Complexity of Servers in Africa

* Thousands to millions of servers are present in building data centres around the world, including those in Nigeria.
* Each server generates heat at high densities due to the large number of operations it performs daily.

## **Latency: A Physics Problem**

* Data is transmitted through fibre optic cable at approximately 2/3 of the speed of light.
* The time distance traveled alone is roughly equivalent to a minimum round-trip time of 50ms between two points.
* Factors like routing, congestion, and processing delay add significant variability to this time.

## **The Role of Machine Learning**

* Limited developers in Nigeria build and deploy machine learning models on these servers, using data from users worldwide for training and testing purposes.