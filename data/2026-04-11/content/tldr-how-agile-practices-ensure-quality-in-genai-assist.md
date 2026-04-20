---
title: How Agile practices ensure quality in GenAI-assisted development | InfoWorld
url: https://www.infoworld.com/article/4155901/how-agile-practices-ensure-quality-in-genai-assisted-development.html
site_name: tldr
content_file: tldr-how-agile-practices-ensure-quality-in-genai-assist
fetched_at: '2026-04-11T06:00:30.237329'
original_url: https://www.infoworld.com/article/4155901/how-agile-practices-ensure-quality-in-genai-assisted-development.html
date: '2026-04-11'
description: AI lets you code at warp speed, but without Agile "safety nets" like pair programming and automated tests, you're just creating technical debt even faster.
tags:
- tldr
---

by
Likhesh Bramhanwade

Contributor

# How Agile practices ensure quality in GenAI-assisted development

opinion

Apr 9, 2026
15 mins


## AI lets you code at warp speed, but without Agile "safety nets" like pair programming and automated tests, you're just creating technical debt even faster.



							Credit: 															Cherdchai101 / Shutterstock

Generative AI has revolutionized the space of software development in such a way that developers can now write code at an unprecedented speed. Various tools such as GitHub Copilot, Amazon CodeWhisperer and ChatGPT have become a normal part of how engineers carry out their work nowadays. I have experienced this firsthand, in my roles from leading engineering teams at Amazon to working on large-scale platforms for invoicing and compliance, both the huge boosts in productivity and the equally great risks that come with GenAI-assisted development.

With GenAI, the promise of productivity is very compelling. Developers who use AI coding assistants talk about their productivity going up by 15% to 55%. But most of the time, this speed comes with hidden dangers. To name a few, AI-generated software without good guardrails could open up security issues, lead to technical debt and introduce bugs that are difficult to detect through traditional code reviews. According to McKinsey research, while GenAI tools allow developers to be more productive at a higher level but also require rethinking of software development practices to maintain code quality and security.

The answer is not to abandon these awesome tools altogether. In fact, it is about combining them with reliable engineering practices that the teams already know and trust. In fact, the proper application of traditional Agile methodologies generates the precise guidelines that allow you to benefit from GenAI while also controlling its hazards. In this article, I consider the five basicAgile methodologies: Test-driven development (TDD), behavior-driven development (BDD), acceptance test-driven development (ATDD), pair programming and continuous integration together provide the guardrails to GenAI development, not just to make it quicker, but also of higher quality.

## The GenAI code quality crisis: Real-world issues

Before we jump into solutions, it is worth naming the problem. The issues with AI-generated code aren’t theoretical. They’re appearing in production systems across the industry:

* Security vulnerabilities:In 2023, researchers atStanfordfound that developers using AI assistants were more likely to introduce security vulnerabilities into their code, particularly injection flaws and insecure authentication mechanisms. A study published inIEEE Security & Privacydemonstrated that GitHub Copilot suggested vulnerable code approximately 40% of the time across common security-critical scenarios. At one major financial institution, an AI-generated SQL query bypassed parameterization, creating a critical injection vulnerability that wasn’t caught until penetration testing.
* Hallucinated dependencies:AI models sometimes generate suggestions for libraries, functions or APIs that don’t exist. A group from a healthcare company invested three days in finding the bug in their microservice compiling issue, only to learn that the AI had suggested a nonexistent AWS SDK method. The code seemed legitimate, went through the first review, but the method signature was completely made up.
* Subtly incorrect business logic:Most misleading of all are mistakes in the business logic that look good on the surface but have subtle defects in them. For example, we came across a line, item tax calculation on an invoice that was AI-generated, which looked perfect, but upon close inspection, it was discovered that rounding was applied at the level of each item rather than at the level of the subtotal. While a brief inspection of the logic indicated that it was correct, the difference in the sequence of rounding would have resulted in the final invoice totals being different from the legal requirements for tax reporting, thus leading to compliance risks and reconciliation errors from millions of transactions.
* Technical debt accumulation:AI tools focus on producing working code rather than maintainable code. They frequently recommend very nested conditional logic, duplicated code patterns and excessively complex solutions when simpler alternatives are available.Gartner researchwarned that without strong governance, early GenAI adopters can accumulate cost, complexity and technical debt.
* Compliance and licensing issues:AI models trained from public code repositories can, at times, generate code that is basically a copy of the code with certain licenses that are incompatible. For industries that are heavily regulated, such as healthcare and finance, this kind of situation poses very serious risks of noncompliance. A pharmaceutical company, as an example, came across AI-generated codes that were very similar to the GPL-licensed open-source software and if the company relies on such a platform, it would be legally exposed.

## The root cause: Speed without clear specification

These problems arise from the same root, which is AI producing code based on patterns it has seen, without real understanding of requirements, context or whether the code is correct. It works on probability, for example, “what code pattern from the prompt is most likely” rather than correctness or suitability for the particular case.

Traditional code review, although essential, is not enough to protect against errors from AI-generated code. Most people find it difficult to spot subtle errors in code that looks legitimate and the volume of AI-generated code can easily overwhelm the review capacity. We must have automated, systematic methods that check correctness and not just quick visual inspection.

## Agile practices as GenAI guardrails

One can find the answer in the methods that have been around for a long time, even before GenAI, and yet they are great at fixing its flaws. Every one of these methods provides a different type of safety net:

### 1. Test-driven development (TDD): The correctness validator

The TDD cycle,Red, Green, Refactorprovides the most direct protection against incorrect AI-generated code. By writing tests first, you create an executable specification of correctness before the AI generates any implementation.

How it works with GenAI:

* Red:Write a failing test that specifies the exact behavior you need. This test becomes your requirement specification in executable form.
* Green:Ask the AI to generate code that makes the test pass. The AI now has a clear, unambiguous target.
* Refactor:Use AI to suggest improvements to the working code while ensuring tests still pass.

Real-world impact:We applied very strict TDD alongside GenAI-assisted development. Before developers accept any AI suggestions, they should write extensive unit tests that detail all the aspects. This caught a critical line-item tax calculation error, while the AI suggested a simple multiplication that “looked” correct, the test specifically checked for legal rounding requirements (rounding at the subtotal level rather than the line level). Because the test specified these precision requirements, the AI’s initial code failed immediately. Without TDD, this discrepancy would have reached production, resulting in significant compliance risks and revenue reconciliation failures.

Moreover, TDD solves the problem of hallucination of dependencies. For example, if AI offers a method or a library that does not exist, the test will not be able to compile or run, thus providing immediate feedback instead of finding out the issue after several days.

### 2. Behavior-driven development (BDD): The business logic guardian

BDD extends TDD by focusing on system behavior from the user’s perspective using Given-When-Then scenarios. This is particularly powerful for GenAI-assisted development because it creates human-readable specifications that bridge the gap between business requirements and code.

BDD scenarios serve two critical functions with AI-generated code:

First, they provide context-rich prompts for the AI. Instead of asking “write a function to calculate tax,” you provide a complete scenario: “Given a customer in California, when they purchase a $100 item, then the tax should be $9.25.” The AI has more context to generate correct code.

Second, they create executable business logic tests that catch subtle errors humans might miss. The scenarios are written in plain language by product owners and domain experts, then automated using frameworks likeCucumberorCypress.

Real-world impact:Compliance platform processes invoices across multiple tax jurisdictions. When we started using AI assistance, we first created comprehensive BDD scenarios covering all tax rules, edge cases and regulatory requirements. These scenarios, written by our tax compliance specialists, became the specification for AI code generation. The AI-generated code that passed all BDD scenarios was correct 95% of the time, far higher than code generated from vague prompts.

### 3. Acceptance test-driven development (ATDD): The stakeholder alignment tool

ATDD involves customers and stakeholders early in defining automated acceptance tests before development begins. This practice is crucial when using GenAI because it ensures the AI is solving the right problem, not just generating plausible-looking code.

The ATDD workflow with GenAI:

* Specification Workshop:Product owners, developers and testers collaborate to define acceptance criteria in a testable format. This creates a shared understanding of “done.”
* Test Automation:Convert acceptance criteria into automated tests before writing implementation code. These tests represent the customer’s definition of success.
* AI Assisted Implementation:Use GenAI to implement features that satisfy the acceptance tests. The tests prevent the AI from drifting away from actual requirements.

Real-world impact:For a volume-based discount feature, we held ATDD workshops to define a specific requirement: “Buy 10, Get 10% Off” must apply only to the qualifying line items, not the entire invoice total. These became our automated acceptance tests. When developers used GenAI to implement the logic, the AI suggested a simple, global discount function that subtracted 10% from the final balance, a common coding pattern for retail, but incorrect for our B2B contractual rules. Because theATDD testvalidated the discount at the line-item level, the AI’s “perfect-looking” code failed immediately. This prevented a logic error that would have resulted in significant over-discounting and lost revenue across thousands of bulk orders.

### 4. Pair programming: The human-AI collaboration model

Traditional pair programming involves two developers working together, often one writing tests and the other writing implementation. With GenAI, this model evolves into a powerful three-way collaboration: Developer A writes tests, Developer B reviews AI-generated code and the AI serves as a rapid implementation assistant.

The enhanced pair programming workflow:

* Navigator Role:One developer focuses on writing comprehensive tests and thinking about edge cases, security implications and architectural fit. They are not distracted by implementation details.
* Driver Role:The other developer works with the AI to generate implementation code, critically evaluating each suggestion. They serve as the quality filter for AI output.
* AI Assistant:Generates implementation suggestions based on tests and context, accelerating the coding process while the human pair ensures quality.

Real-world impact:A recent study byGitClearfound that code quality metrics declined when developers used AI tools in isolation but improved when used in pair programming contexts. We recommend pair programming for any AI-assisted development of critical systems. The navigator catches security issues and architectural mismatches that the driver, focused on AI output, might miss. We have seen a 60% reduction in post-deployment bugs compared to solo AI-assisted development.

### 5. Continuous integration (CI): The automated safety net

Continuous integration runs automated test suites every time code is merged. It becomes even more critical with GenAI-assisted development. CI provides the final safety net that catches issues before they reach production.

Enhanced CI pipeline for GenAI code:

* Comprehensive test execution:Run all unit tests, integration tests, BDD scenarios and acceptance tests on every commit. AI-generated code must pass the entire suite.
* Static analysis:Include additional static analysis tools that check for common AI-generated code issues like security vulnerabilities, code complexity metrics and licensing compliance.
* Performance benchmarks: Automated performance tests catch AI-generatedcode that works correctly but performs poorly at scale.

Real-world impact:Our CI pipeline is configured with specialized checks designed to catch the unique risks of AI-assisted coding. For the invoicing platform, we integrated automated business-rule validators that specifically verify logic like tax rounding and discount applications.

## The synergistic effect: Practices working together

The real power emerges when these practices work together. Each creates a different layer of protection:

* TDDensures the code works correctly for specified inputs.
* BDDensures it implements the right business behavior.
* ATDDensures it meets stakeholder expectations.
* Pair programmingensures human oversight and critical thinking.
* CIensures all these checks run automatically and consistently.

Consider a typical user story for an e-commerce platform: “As a customer, I want to apply discount codes so that I can save money on purchases.”

Without Agile practices, a developer might prompt an AI: “Write a function to apply discount codes to shopping carts.” The AI generates plausible-looking code, the developer briefly reviews it and it ships. Hidden issues might include: discount stacking vulnerabilities, floating-point rounding errors, failure to validate expiration dates or SQL injection in the discount code lookup.

With Agile practices:

* ATDD:Product owner, developer and tester define acceptance criteria: “Given a valid 10% discount code, When applied to a $100 cart, Then the total should be $90.”
* BDD:Business analyst writes scenarios covering edge cases: expired codes, invalid codes, maximum discount limits, combination rules.
* TDD:Developer pair writes unit tests first, including security tests for injection attacks, tests for decimal precision and tests for all edge cases.
* Pair programming:One developer writes tests, the other works with AI to implement, both review the generated code critically.
* CI:All tests run automatically on commit, plus static analysis for security issues, performance benchmarks and compliance checks.

This multi-layered approach catches issues at different stages: tests catch functional errors, pair programming catches architectural mismatches, CI catches regressions and security issues.

## Implementation recommendations

Based on our experience implementing these practices across multiple teams, here are practical recommendations for organizations adopting GenAI development tools:

* Start with TDD as the foundation:Make test-first development non-negotiable when using AI assistance. This single practice prevents the majority of AI-generated code issues. Invest in training developers on TDD if they’re not already proficient.
* Enhance code review processes:Traditional code review checklists need updating for AI-generated code. Add specific review criteria: Does the code handle edge cases? Are there obvious security vulnerabilities? Does it match our architectural patterns? Is the complexity appropriate for the problem?
* Invest in test infrastructure:Strong CI pipelines become even more important. Ensure your pipeline can run comprehensive test suites quickly. Slow test execution discourages frequent commits and reduces the effectiveness of CI as a safety net.
* Create AI usage guidelines:Document when and how to use AI assistance. Some scenarios might be high risk (security-critical code, financial calculations) and require extra scrutiny. Others might be low-risk (boilerplate code, standard CRUD operations) and benefit most from AI acceleration.
* Measure and monitor:Track metrics specific to AI-assisted development, such as defect rates in AI-generated vs. human-written code, test coverage trends, time-to-production and post-deployment issues. Use data to refine your practices.

 

## Conclusion: Speed with safety

Generative AI is a fundamental change in how we write software that can be compared to the introduction of high-level programming languages or integrated development environments. It brings real and huge productivity gains. But speed without quality is not progress; it is technical debt accumulation at an accelerated rate.

The great thing is that we don’t have to come up with new methods to make use of GenAI safely. The Agile methods that have been used for decades, such as TDD, BDD, ATDD, Pair Programming and CI, are exactly the safety measures we need. These methods have quality at their core through automation, collaboration and continuous verification. They are even more impressive with AI help because they provide objective, automated checks that don’t have the same pattern-matching biases as humans, who are poor at reviewing AI-generated code, have.

Companies that use GenAI tools but keep up with strict software development practices will get the best results. For example, faster development without sacrificing quality, reduced defect rates despite increased velocity and sustainable productivity gains that don’t create future maintenance issues.

Software development in the future is not about just humans or AI. It is humans and AI cooperating within established quality assurance that is protected by proven frameworks. The combination of AI’s speed and the safety of Agile methods allows us to do software development that is both really efficient and of high quality on a large scale.

This article is published as part of the Foundry Expert Contributor Network.Want to join?

Agile Development
Artificial Intelligence
Development Approaches
Generative AI
Software Development




														by

																Likhesh Bramhanwade

Contributor

1. Follow Likhesh Bramhanwade on LinkedIn

Likhesh Bramhanwadeis a software development manager at Amazon, where he leads teams building large-scale platforms for invoicing, compliance, cloud-based voice assistants, personalization and AI-driven customer experiences. He has more than 21 years of experience at Amazon, Microsoft, Nordstrom and NTT DATA, specializing in cloud-native architectures, low-latency services, advertising systems and B2B integrations. Likhesh is a Fellow of IETE, a senior member of IEEE and an active contributor to technical communities as a reviewer, speaker and mentor.Disclaimer: The views expressed here are personal and do not represent those of Amazon.

## Show me more

Popular
Articles
Videos

news



### AWS targets AI agent sprawl with new Bedrock Agent Registry


By Anirban Ghoshal
Apr 10, 2026
4 mins

Amazon Web Services
Artificial Intelligence
IaaS

opinion



### AI agents aren't failing. The coordination layer is failing


By Sreenivasa Reddy Hulebeedu Reddy
Apr 10, 2026
8 mins

Cloud-Native
Development Approaches
Microservices

opinion



### Cloud degrees are moving online


By David Linthicum
Apr 10, 2026
6 mins

Careers
Cloud Computing
Technology Industry

video



### Python's new frozendict type


Apr 2, 2026
4 mins

Python

video



### How to boost app performance with Python 3.15's lazy import


Mar 31, 2026
6 mins

Python

video



### How to run your own little local Claude Code (sort of!)


Mar 26, 2026
7 mins

Python
