---
title: I Built My First AWS Agent Workflow, and the Hardest Part Was Getting It to Stop Assuming Things - DEV Community
url: https://dev.to/hemapriya_kanagala/i-built-my-first-aws-agent-workflow-and-the-hardest-part-was-getting-it-to-stop-assuming-things-8fg
date: 2026-09-03
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-09-04T07:26:14.020930
---

# I Built My First AWS Agent Workflow, and the Hardest Part Was Getting It to Stop Assuming Things - DEV Community

# Summary of “I Built My First AWS Agent Workflow, and the Hardest Part Was Getting It to Stop Assuming Things”

## I Want to Start With Something Honest
- Completed the Udacity Future AWS Agent Engineer Nanodegree project in ~2 days while juggling other life events.  
- Passed on the first try with a correctness score of 0.83 but did not have time to refine prompts or rerun evaluations.  
- The most valuable insights came from the two evaluation failures rather than the parts that worked.

## What I Built and How the Pieces Fit Together
- Created a fictional customer‑support agent for an online shop using:
  - **Amazon Bedrock AgentCore Managed Harness** – hosts the model, instructions, and tools.  
  - **System prompt** – encodes routing logic and rules for three request types.  
  - **AgentCore Gateway** – connects the model to backend tools.  
  - **AWS Lambda** – executes actions (e.g., creates a bug‑report ticket).  
  - **Amazon DynamoDB** – stores created tickets.  
  - **FAQ data source** – supplies authoritative answers for platform questions.  
- Request types and required behaviors:
  - **BUG_REPORT** – must collect *description*, *steps to reproduce*, and *environment* before creating a ticket.  
  - **PLATFORM_QUESTION** – answer using the provided FAQ, not the model’s general knowledge.  
  - **OTHER_REQUEST** – hand off to human support.

## The Prompt Was Doing More Than I Expected
- The routing logic was embedded directly in the system prompt rather than a separate classifier.  
- The prompt also defined validation rules (e.g., “do not create a ticket unless all three pieces of information are present”).  
- Assumed that the model would automatically enforce those rules, which proved false.

## The Evaluation Showed Me Where I Was Wrong
- **Failure 1:** For a bug report missing one required field, the model still created a ticket.  
- **Failure 2:** Similar scenario where the model proceeded despite incomplete information.  
- These failures highlighted that *understanding* a request ≠ having *sufficient* information to act safely.

## What I Would Change and What I Learned
- Move schema validation (checking that all required fields are present) out of the prompt and into a separate step or backend check.  
- Treat the prompt as a guide for intent classification, not as a strict gatekeeper for actions.  
- Add explicit post‑processing logic that verifies completeness before invoking Lambda.  
- Include more diverse test cases and iterate on evaluation results.

## Advice for Beginners
- Focus first on the overall data flow rather than memorizing each AWS service name.  
- Understand the role of each component: model → prompt (rules) → gateway → Lambda → DynamoDB.  
- Separate concerns: let the model decide intent, let the backend enforce business rules.  
- Use evaluation feedback to identify hidden assumptions in prompts.

## Final Takeaway
- Building an AI agent is as much about *when* to act as about *how* to answer.  
- Relying solely on prompts for validation leads to “assuming” behavior; explicit schema checks outside the prompt are essential for safe, reliable actions.