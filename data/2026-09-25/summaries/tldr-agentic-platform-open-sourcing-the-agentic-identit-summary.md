---
title: Agentic Platform: Open-Sourcing the Agentic Identity Broker
url: https://engineering.zalando.com/posts/2026/09/agentic-platform-open-sourcing-agentic-identity-broker.html
date: 2026-09-25
site: tldr
model: llama3.2:1b
summarized_at: 2026-09-25T15:49:57.375365
---

# Agentic Platform: Open-Sourcing the Agentic Identity Broker

## Agentic Identity Broker: A Core Component of Agentic Platform

The Agentic Platform, developed by Zalando, aims to provide an agentic identity broker that enables AI agents to act on behalf of users across third-party systems without holding the users' provider tokens. This component was built by the Agentic Engineering team, consisting of the same individuals who worked on the Agentic Platform, to address two key questions: how to handle agentic identity and give agents reasonable access to multiple systems.

## Handling Agentic Identity

The challenges of agentic identity are twofold: (1) identifying agents through their own machine identity, (2) giving agents access to multiple third-party systems that issue their own access tokens. Unlike traditional microservices, these issues of identity are not new, but as an industry, they have been partly ignored.

A solution to these problems exists: the shared pressure to make access decisions based on user and agent permissions. The identity assertion JWT authorization grant, known as Cross-App Access (XAA), is an example of how this is being standardized. To unify access across third-party systems, the Agentic Platform's identity broker captures delegation chains, which enables access to services.

## On-Behalf-Of Flows

The Agentic Platform also focuses on on-behalf-of flows, where users interact directly with agents or trigger them indirectly. This class of agents benefits from existing enterprise access management and user permissions. By assigning permissions to the agent's own identity, effective permissions are achieved as the intersection of both user and agent permissions.

## Benefits and Future Directions

The Agentic Platform's identity broker has several benefits: (1) enables independent AI agents to interact with users without relying on provider tokens (2) unifies access across multiple third-party systems (3) addresses the shared problem of identity and access control (4) introduces the first core piece of the Agentic Platform: the identity broker.

The future direction of the Agentic Platform involves further standardization and integration of identity and access control mechanisms across various systems and services.