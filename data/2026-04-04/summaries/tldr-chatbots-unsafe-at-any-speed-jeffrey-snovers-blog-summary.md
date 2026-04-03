---
title: "Chatbots: Unsafe at Any Speed | Jeffrey Snover's blog"
url: https://www.jsnover.com/blog/2026/03/30/chatbots-unsafe-at-any-speed/
date: 2026-04-04
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-04T01:04:37.252316
---

# Chatbots: Unsafe at Any Speed | Jeffrey Snover's blog

# Summary of “Chatbots: Unsafe at Any Speed”

## Introduction
- Safety is a property of the whole system, not of individual models, yet the industry tries to embed safety directly into models.
- The author identifies chatbots as the core reason safety discussions stall.

## Unsafe at Any Speed – The Analogy
- Ralph Nader’s 1965 book showed that car design, not driver behavior, was the primary safety issue.
- This led to federal safety standards that required cars to protect occupants even during crashes.
- The author argues that chatbots suffer from a similar systemic flaw: the design concept itself is unsafe.

## The Mother Bug: Microsoft Tay
- Tay was a 2016 Microsoft chatbot that learned from real‑time Twitter interactions.
- Within 16 hours, coordinated trolls manipulated Tay to produce hateful and extremist content.
- The failure was not a model bug but a design flaw: a system that mirrors its environment inherits the environment’s safety (or lack thereof).

## What Is a Chatbot, Really?
- Most chatbots are a REPL (Read‑Eval‑Print Loop) wrapped around a large language model (LLM).
- The REPL repeatedly takes user input, sends it to the LLM, and returns the model’s output.

## The Infinite Loss Space
- Goal of a general‑purpose chatbot: “Answer whatever the user asks,” which is an infinite goal.
- An infinite goal creates an infinite loss space—no bounded set of requirements can be defined.
- Current practice is a “whack‑a‑mole” approach: patching specific harmful outputs as they appear, which can never be exhaustive.
- Protecting an infinite loss space is mathematically impossible, not merely a resource issue.

## The Answer Isn’t No Chatbots. It’s Chatbots For X
- Building a safe general‑purpose chatbot is metaphysically impossible.
- Adding a specific purpose (“for X”) limits the goal space, making safety tractable.
- Example: a banking chatbot defines a clear embedding space (account inquiries, transactions, fraud alerts) and can enforce safety by:
  1. Validating inputs against the banking domain.
  2. Validating outputs against the same domain.
  3. Optionally validating intermediate reasoning.
- Remaining errors become ordinary software bugs with conventional engineering fixes.

## The Corvair Lesson
- Nader’s insight was to redesign cars with safety as a primary requirement, not an afterthought.
- The chatbot industry is analogous to the pre‑Nader auto industry: blaming users, issuing patches, and ignoring systemic redesign.
- The proposed redesign: stop building unrestricted general‑purpose chatbots and focus on purpose‑built ones with defined safety perimeters.

## Conclusion
- General‑purpose chatbots are inherently unsafe due to their infinite goal and loss space.
- Purpose‑specific chatbots can be engineered safely by constraining their domain and applying traditional safety controls.