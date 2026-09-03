---
title: I Built My First AWS Agent Workflow, and the Hardest Part Was Getting It to Stop Assuming Things - DEV Community
url: https://dev.to/hemapriya_kanagala/i-built-my-first-aws-agent-workflow-and-the-hardest-part-was-getting-it-to-stop-assuming-things-8fg
site_name: devto
content_file: devto-i-built-my-first-aws-agent-workflow-and-the-hardes
fetched_at: '2026-09-04T07:24:56.942994'
original_url: https://dev.to/hemapriya_kanagala/i-built-my-first-aws-agent-workflow-and-the-hardest-part-was-getting-it-to-stop-assuming-things-8fg
author: Hemapriya Kanagala
date: '2026-09-03'
description: TL;DR I recently finished a project from Udacity's Future AWS Agent Engineer Nanodegree Program,... Tagged with discuss, aws, beginners, agents.
tags: '#discuss, #aws, #beginners, #agents'
---

Schema validation belongs outside prompts

TL;DR

I recently finished a project from Udacity's Future AWS Agent Engineer Nanodegree Program, which I was able to take through the AWS AI & ML Scholarship.

I built a customer support agent using Amazon Bedrock AgentCore, AgentCore Gateway, AWS Lambda, DynamoDB, and an FAQ. The agent had to understand whether a customer was reporting a bug, asking a question that could be answered from the FAQ, or asking for something that needed human support.

I finished it in about two days and passed on my first attempt with a correctness score of0.83. I did not have enough time to go back and refine it or run another evaluation round because there was a lot happening in my life at the time.

The part I learned the most from was actually one of my evaluation failures. For a bug report, I had told the agent that it needed 3 things before creating a ticket: a description of the problem, steps to reproduce it, and the environment where it happened. But in 2 test cases, the model understood what the customer was talking about and created the ticket even though one of those required pieces of information was missing.

That made me realize something I had not thought about enough before:understanding a request is not the same as having enough information to safely take an action.

That is the main lesson I took from this project. Building an agent is not only about making the model capable of answering. It is also about being clear about when it should act, when it should ask for more information, and when it should stop and hand the request to a person.

I know there are already many great articles about AWS, AgentCore, and AI agents, and I have learned from many of them myself. I am still learning too, so this is simply my experience of building this project, what confused me, what the evaluation showed me, and what I would do differently next time.

## Table of Contents

* I Want to Start With Something Honest
* What I Built and How the Pieces Fit TogetherSo What Does Each AWS Service Actually Do Here?
* So What Does Each AWS Service Actually Do Here?
* The Prompt Was Doing More Than I ExpectedThe Prompt Was Setting the RulesI Also Had to Think About What the Customer Might Try
* The Prompt Was Setting the Rules
* I Also Had to Think About What the Customer Might Try
* The Evaluation Showed Me Where I Was WrongThe Two Failures
* The Two Failures
* What I Would Change and What I LearnedSeeing the Backend Made the Agent Make More Sense
* Seeing the Backend Made the Agent Make More Sense
* If You Are Also Starting Out
* I Would Love to Hear From You
* A Small Thank You
* My Final Takeaway
* 🤝 Let's Stay Connected

## I Want to Start With Something Honest

I finished another project recently, and this one was a little different for me. It was part of theFuture AWS Agent Engineer Nanodegree Program from Udacity, which I was able to take through theAWS AI & ML Scholarship.

I finished the project in roughly 2 days. I was working around a lot of other things happening in my life, so I was trying to make the most of the time I had and keep moving.

I passed the project on my first attempt, which I was really happy about, but I also knew I had not spent the time I normally would on refining it.

If I had more time, I would have gone back, looked at the evaluation results more carefully, improved the prompt, added more test cases, and run another evaluation. I did not do that this time. The final correctness score was0.83.

At first, I felt like I should probably wait until I had a higher score before writing about the project. Then I thought about what I had actually learned from it. The 2 things that did not work perfectly were some of the most useful parts of the project for me. That is what I wanted to share.

There are already a lot of really good articles about building agents, AWS services, and AgentCore. I have learned from many of them myself. This is not meant to be another article that tries to explain everything about agent development. Instead, I wanted to share what the project looked like from my side as someone who is still learning.

Because when you are a beginner, sometimes the hardest part is not the code. It is understanding what all the pieces are actually doing and why they need to be there.

## What I Built and How the Pieces Fit Together

The project was a fictional customer support system for an online shop. A customer could send a message, and the agent had to understand what the customer needed and decide what to do next.

There were three possible behaviors. The first wasBUG_REPORT. If a customer said something like, “The checkout page crashes every time I click Pay,” the agent needed to recognize that as a technical problem. But recognizing it as a bug was not enough to create a ticket. Before doing that, the agent needed to collect three specific pieces of information:description, steps to reproduce, and environment.

The second wasPLATFORM_QUESTION. These were questions about things such as orders, shipping, returns, refunds, payments, products, accounts, and privacy. For these questions, the agent had an FAQ that it was expected to use instead of making up an answer from what it generally knew.

The third wasOTHER_REQUEST. If the request was not a technical bug and could not be answered using the FAQ, the agent needed to direct the customer to human support.

Once I stopped looking at each AWS service separately and looked at how they worked together, the architecture became much easier for me to understand.

The flow was essentially:

This is the architecture I built for the project. The routing was handled through the system prompt rather than through a separate classifier or condition node.

### So what does each AWS service actually do here?

If you are new to AWS, the service names can make a project like this look much more complicated than it really is. What helped me was thinking about what each piece was responsible for instead of trying to understand every AWS service at once.

Amazon Bedrock AgentCore Managed Harnesswas the environment around the agent. In simple terms, it gave me the structure needed to run the agent with its model, instructions, and tools without having to build all of that setup myself.

The modelwas responsible for understanding the customer's message and deciding what to do next based on the instructions it was given. It was the part doing the actual language understanding and decision-making.

The system promptdefined how the agent was supposed to behave. This was especially important in my project because the routing logic was written into the prompt. The prompt told the model how to recognize the 3 types of requests and what rules to follow for each one.

AgentCore Gatewayconnected the agent to the backend tool. The model was not directly changing the database. Instead, once the required information had been collected, the agent could call the tool through the Gateway.

AWS Lambdahandled the actual backend operation. When the agent called the tool with the required information, Lambda processed the request and created the bug report.

Amazon DynamoDBstored that bug report. This was also a useful thing for me to understand because it showed that the agent's response was not just text. If the agent returned a ticket ID, there was an actual record stored in DynamoDB behind that response.

And theFAQwas the controlled source of information for platform questions. The agent was expected to use the information provided there instead of relying on general knowledge when answering those questions.

Once I looked at it this way, the architecture stopped feeling like a collection of unfamiliar AWS names. The model understood the customer's message, the prompt told it what rules to follow, the Gateway connected it to an action, Lambda performed that action, and DynamoDB stored the result. For platform questions, the FAQ provided the information the agent was allowed to use, while requests outside those boundaries went to human support.

That simple way of looking at the system helped me more than memorizing what each AWS service does on its own.

One thing that confused me at first was the word“classifier.”When I first saw that requirement, I imagined there would be a separate component whose only job was to classify the customer's message and then send it to the right part of the system.

That was not what I built.

In my implementation, the routing logic was part of the system prompt. The model was instructed to choose one of the 3 routes and then follow the rules for that route.

Understanding this changed how I looked at the prompt. I initially thought of the prompt mostly as instructions for how the agent should respond. In this project, it was doing much more than that. It was also defining what information the agent needed, when it was allowed to take an action, what information it could use to answer a question, and when it needed to stop and involve human support.

## The Prompt Was Doing More Than I Expected

Before this project, I mostly thought about a system prompt as a way of telling the model how to behave. Something like:

“You are a helpful customer support assistant.”

That is useful, but it is not enough when the model is also making decisions and using tools. In this project, the prompt was not just telling the agent how to respond. It was also telling it what it was allowed to do and what information it needed before doing it.

### The Prompt Was Setting the Rules

For aBUG_REPORT, the prompt explained what counted as a bug and what information was required before a ticket could be created. The 3 required fields weredescription, steps to reproduce, and environment. If something was missing, the agent had to ask for that information one field at a time. It was not supposed to call the tool until all 3 were available.

The prompt also defined the other 2 routes. APLATFORM_QUESTIONhad to be answered using the provided FAQ, while anOTHER_REQUESThad to be directed to human support.

The FAQ part was interesting to me because it showed why an agent sometimes needs to be told what information it can and cannot use.

Suppose a customer asks:

“How long do I have to return an item?”

The FAQ says that most items can be returned within30 days of delivery, as long as they are unused and in their original packaging, unless the item arrived defective. So the agent can answer that using the information it was given.

But suppose someone asks:

“Do you offer a student discount?”

If the FAQ does not mention student discounts, the agent should not simply make up an answer because the model might have seen student discounts mentioned somewhere else. It should send the customer to human support.

That made something very clear to me: a model can know a lot, but that does not mean it knowsyour company's policy.

The same applies to things like refunds, shipping, payment policies, account rules, and other information where giving a confident but incorrect answer could cause a real problem. For this project, the FAQ was a controlled source of information, and the prompt made that boundary clear.

### I Also Had to Think About What the Customer Might Try

The prompt had another job that I had not thought much about before this project: dealing withprompt injection.

One of the test cases essentially told the agent to ignore its instructions, reveal the system prompt, and create a bug ticket without collecting the required information. The agent did not follow those instructions. It continued following the rules defined in the system prompt.

I found this useful because it made me think beyond the simple test cases I naturally wrote while building the project. When we test an agent ourselves, we usually give it the kind of message we expect a customer to send. Real users can leave information out, ask something completely unrelated, or deliberately try to change how the agent behaves.

So the prompt cannot only describe the happy path. It also needs to make the boundaries clear.

At the same time, passing this one prompt-injection test does not mean the agent is protected against every possible injection. It only showed me that this particular test case was handled according to the rules I had defined.

That was another lesson from the project for me.Giving an agent more capabilities is only part of the work. You also have to be clear about when those capabilities should and should not be used.

## The Evaluation Showed Me Where I Was Wrong

This was probably the most useful part of the project for me.

Getting the agent to respond correctly in a few manual tests is one thing. Evaluating it with deliberately incomplete and tricky inputs is another. For the project, I created a test dataset covering the different routes, including complete bug reports, bug reports with missing information, FAQ questions, questions that were not covered by the FAQ, requests to speak to a real person, and a prompt-injection case.

The final correctness score was0.83. Most of the tests behaved the way I wanted. Complete bug reports worked, the missing-environment case worked, the FAQ questions worked, unsupported questions were handed off, requests for human support were handled correctly, and the prompt-injection case also passed.

But two tests failed, and both failures taught me basically the same thing.

### The Two Failures

In the first case, the customer said that product images were not loading on category pages and mentioned Safari on an iPhone. The problem description was there, and the environment was there, but the customer had not explicitly provided reproduction steps. The agent still created a ticket.

In the second case, the customer gave reproduction steps and a Chrome/Windows environment, but did not provide a clear description of the actual problem. Again, the agent created a ticket.

At first, I thought the model had simply misunderstood my prompt. But when I looked at the two cases more carefully, I realized that the model probably understood what the customers were talking about. The problem was that it treated that understanding as enough information to take the next action.

From a normal human conversation perspective, that is not necessarily a bad thing. If someone says:

“The product images are not loading on Safari on my iPhone.”

a person can probably understand what is going wrong and know what the customer is referring to.

But that was not the rule I had given the agent. The agent was not supposed to decide, “I understand the problem, so I can create the ticket.” It was supposed to check whetherall 3 required fields were explicitly availablebefore creating the ticket.

That is a much stricter requirement.

This was probably the biggest lesson I got from the project:understanding something is not the same as having enough information to safely perform an action.

That matters even more when an agent starts calling tools. If the same kind of assumption happened in a system that creates a refund, changes an account, submits an application, or updates a database, the model might make a very reasonable guess, but that guess could still lead to the wrong action.

So for me, the important question changed from:

“Does the model understand what the customer means?”

to:

“Does the model have everything it is required to have before it takes this action?”

That is something I would pay much more attention to if I built another agent.

Looking back, I actually found the individual evaluation results more useful than the overall score. The 0.83 tells me how the agent performed overall, but looking at the individual cases showed me exactly where the behavior broke down.

For me, those two failed cases were more useful than simply knowing that the score was not 1.0. They showed me a specific problem in the way I had defined the agent's behavior, and more importantly, they gave me something concrete that I could improve.

## What I Would Change and What I Learned

If I had another day to work on the project, I would start with those two failed cases.

I would make the prompt more explicit about what counts as a field being present, especially the difference between a description and reproduction steps. For example,“The images are not loading”is a description of the problem.“Open the shop, go to a category, and tap any product”is a sequence of steps someone could follow to reproduce it.

I would also make it clearer that the agent should not fill in a missing field just because the rest of the message makes the situation easy to understand. If the customer has not actually provided the reproduction steps, the agent should ask for them instead of deciding that it already knows what they probably are.

Then I would add more tests around the same problem. What happens when the customer provides two fields in one sentence? What happens when the third field comes in a later message? What happens when the customer uses vague language? What happens when the information could reasonably fit into more than one field?

Those are the cases I would want to explore next because they are the kinds of situations where an agent can appear to be doing well while still making assumptions.

### Seeing the Backend Made the Agent Make More Sense

I also learned something from the backend side of the project. Before building it, I mostly thought of an agent as something that takes a message and gives you an answer. Working with the tool and the backend made me see what happens when the agent is expected to actually do something.

The flow in my project was:

Customer information
 ↓
Agent checks whether enough information exists
 ↓
AgentCore Gateway
 ↓
Lambda
 ↓
DynamoDB
 ↓
Ticket ID returned
 ↓
Customer receives the ticket ID

Enter fullscreen mode

Exit fullscreen mode

The important part for me was that the model's response was not the action itself. When the agent said that a ticket had been created, there needed to be an actual operation behind that response. The tool call went through AgentCore Gateway, Lambda handled the backend operation, and DynamoDB stored the ticket. The ticket ID returned from that process was then given back to the customer.

That made the difference between a regular chatbot and an agent workflow much clearer to me. A chatbot can mainly respond to what you say. An agent can also be given tools that allow it to take actions outside the conversation.

But once you give a model that ability, you also have to be careful about what happens when things do not go as expected.

The model should not say that a ticket was created if the tool failed. It should not invent a ticket ID if one was not returned. And if the FAQ does not contain an answer, it should not create one just because it can produce a convincing response.

These might sound like obvious rules, but actually building the workflow made me understand why they matter. The model is only one part of the application. The prompt defines what it should do, the tools perform actions, the backend systems store or change information, and the application needs to make sure those pieces agree with each other.

That changed how I think about agents. I no longer see the model as the whole application. I see it as one part of a larger system where the instructions, tools, data, and backend all have to work together.

## If You Are Also Starting Out

I am writing this part especially for beginners because I am one too.

I did not start this project knowing exactly how all of these services worked together. A lot of the environments I had worked with before already had things set up for me. You work inside the provided environment, use the tools that are already there, and gradually learn how everything fits together.

This project made me look underneath that layer. I had to understand what the AgentCore harness was doing, why the Gateway was needed, how Lambda connected the tool to the backend, why DynamoDB was there, and how the evaluation could show me that something I thought was working was actually not behaving according to the requirements.

That was probably the biggest difference for me.

When you build a normal application, it can be easy to think about it as:

Input
 ↓
Code
 ↓
Output

Enter fullscreen mode

Exit fullscreen mode

With an agent, the model is also making decisions about what should happen next. So I had to start thinking about things I had not really considered before. What is the model allowed to decide? What information does it need before it can act? What should it do when information is missing? What should it do when it does not know the answer? What happens when someone tries to make it ignore its instructions? And what should happen if the tool itself fails?

Those questions are just as important as connecting the AWS services. That was something I did not fully appreciate before working on the project.

I also realized that I did not need to understand every AWS service deeply before I could start building. What helped me was asking a much simpler question whenever I came across something unfamiliar:

What problem is this service solving in my application?

For DynamoDB, I did not need to understand everything about the database service. I needed to understand that my application needed somewhere to store the bug report.

For Lambda, I did not need to know every feature it provides. I needed to understand that something had to actually execute the backend operation when the agent called the tool.

For AgentCore Gateway, I did not need to know every capability it has. I needed to understand that it provided the connection between the agent and the tool.

Thinking about the services this way made the architecture much less overwhelming for me. Instead of trying to learn a huge list of AWS services first and then figuring out where they fit, I could start with what my application needed and learn the service that solved that particular problem.

I am also glad I started this project even though I did not finish it in the ideal way I normally would have. I completed it in about 2 days, passed on my first attempt, and then had to move on instead of spending another round going back through everything and trying to improve the0.83score.

Of course, part of me would have liked to see what I could have changed and whether another evaluation would have given me a better result. But I am also glad I did not wait until I felt completely ready before starting.

There were moments when I was learning something and immediately had to figure out how to use it in the project. That was uncomfortable sometimes, especially when I was still trying to understand what a service actually did, but it also made the concepts much easier for me to remember.

I saw where AgentCore Gateway fit into an actual workflow instead of only reading about it. I saw Lambda handle the backend operation and DynamoDB store the result. And I saw the evaluation catch something I had missed myself.

That is probably what I will remember from this project more than the final score. I started without knowing everything, built something with what I understood, found places where it could be better, and learned from those places.

## I Would Love to Hear From You

I am still learning, so I would love to hear from people at different stages of this.

If you havetips, advice, lessons from your own projects, mistakes that taught you something, or anything you think might help someone who is just starting out, please share it in the comments.

One of the things I love about DEV is that people come from such different experiences. So if you have something to add, even if it seems small, please share it. Maybe something you learned along the way can help someone else who is just starting.

## A Small Thank You

I also want to thankUdacityand the people involved in theFuture AWS Agent Engineer Nanodegree Program. Having the project structure, learning material, and live sessions made it much easier for me to keep going when I was confused about something.

The live sessions were especially useful because sometimes you can read something several times and still not understand how it fits into the actual project. Hearing someone walk through it and then trying it yourself makes a difference.

I am still learning, but having a project where I could actually put these concepts together helped me understand them in a way that reading about them alone probably would not have.

## My Final Takeaway

If I had to take one thing from this project, it would be this:

A good agent is not only one that knows what to do. It also needs to know when it has enough information to do it.

That sounds simple now, but I understood it differently after seeing the evaluation catch my own assumption.

The model can understand the customer. The prompt can give it instructions. The tools can let it take actions. The backend can store the result. But all of those pieces still need clear rules about when the next step is actually allowed to happen.

That is what I found most interesting about building this project.

I started by thinking I was mainly learning how to put AWS services together. I ended up learning much more about how important the boundaries around an agent are.

And honestly, that is probably a better lesson for me to take into the next project.

## 🤝 Let's Stay Connected

Place

Find me here

GitHub

building things → 
hemapriya-kanagala

LinkedIn

resources & updates → 
hemapriya-kanagala

X

random dev thoughts → 
@KanagalaHema

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse