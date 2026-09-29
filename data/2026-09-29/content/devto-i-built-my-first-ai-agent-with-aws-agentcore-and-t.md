---
title: I Built My First AI Agent With AWS AgentCore, and the Hardest Part Wasn't the AI - DEV Community
url: https://dev.to/hemapriya_kanagala/i-built-my-first-ai-agent-with-aws-agentcore-and-the-hardest-part-wasnt-the-ai-54lf
site_name: devto
content_file: devto-i-built-my-first-ai-agent-with-aws-agentcore-and-t
fetched_at: '2026-09-29T22:52:24.113786'
original_url: https://dev.to/hemapriya_kanagala/i-built-my-first-ai-agent-with-aws-agentcore-and-the-hardest-part-wasnt-the-ai-54lf
author: Hemapriya Kanagala
date: '2026-09-29'
description: TL;DR I recently completed another project from Udacity's Future AWS Agent Engineer Nanodegree... Tagged with discuss, aws, beginners, agents.
tags: '#discuss, #aws, #beginners, #agents'
---

Infrastructure complexity outweighs AI setup

TL;DR

I recently completed another project from Udacity's Future AWS Agent Engineer Nanodegree Program, which I was able to take through the AWS AI & ML Scholarship.

This was my second project working with AI agent systems, but it was my first time building one withAmazon Bedrock AgentCore and the Strands SDK. The goal was to build a customer support AI agent that could track orders, process refunds, answer product and policy questions using a Knowledge Base, remember customer information across sessions, calculate loyalty discounts using code, and browse live websites.

On paper, that sounds like six features.

In reality, it meant connectingAgentCore Runtime, AgentCore Gateway, Lambda, API Gateway, Knowledge Base, Memory, Code Interpreter, Browser Tool, IAM, deployment, and CloudWatchinto one working system.

When I first saw all of that, it felt like a lot. I knew what I was supposed to build, but I didn't yet understand how all the pieces were supposed to fit together.

This time, I had enough time to work through the project properly instead of rushing through it. And that gave me room to notice something I probably wouldn't have noticed otherwise:I was making the project harder by trying to understand everything at once.

Once I stopped doing that and started asking,“What is the next thing I need to understand?”, the project became much easier to work through.

This isn't a step-by-step guide. There are already many great guides for AWS and AgentCore. This is my experience of building the project, what confused me, what went wrong along the way, how the architecture eventually started making sense, and what I learned from putting all those pieces together.

And somewhere along the way, the word“agent”stopped feeling like just another AI buzzword to me. I could actually see what it meant in a working system.

## Table of Contents

* I Knew What I Had to Build. I Just Didn't Know How Big It Would Feel
* So What Was This Agent Actually Supposed to Do?
* The Architecture Finally Made Sense When I Stopped Thinking in AWS Names
* I Drew the Architecture Because I Needed to See It
* The Six Capabilities Were Really Six Different Problems1. Order Tracking: Getting Real Data Back to the Customer2. Refunds: When the Agent Needs to Take an Action3. Knowledge Base: The Model Knowing Isn't the Same as the Application Knowing4. Memory: When a New Conversation Isn't Really Starting From Zero5. Code Interpreter: Let the Model Decide, Let Code Calculate6. Browser Tool: When the Information Isn't Inside Your Application
* 1. Order Tracking: Getting Real Data Back to the Customer
* 2. Refunds: When the Agent Needs to Take an Action
* 3. Knowledge Base: The Model Knowing Isn't the Same as the Application Knowing
* 4. Memory: When a New Conversation Isn't Really Starting From Zero
* 5. Code Interpreter: Let the Model Decide, Let Code Calculate
* 6. Browser Tool: When the Information Isn't Inside Your Application
* Having the Right Code Doesn't Mean Having Access to It
* Deployment Wasn't the Finish Line
* Six Tests Were Easier Than One Giant “Does It Work?”
* The Part That Became Clear Only After Everything Worked
* There Was Another Layer I Hadn't Thought About Enough: Operating the System
* I Also Had to Learn When the Project Was Actually Finished
* What This Project Actually Taught Me
* A Small Thank You
* I Would Love to Hear From You
* 🤝 Let's Stay Connected

## I Knew What I Had to Build. I Just Didn't Know How Big It Would Feel

I want to start here because the finished project looks much simpler than the experience of building it. Once everything was working, I could look at the architecture and understand what each part was doing.

But at the beginning, I saw a long list of unfamiliar names:Amazon Bedrock AgentCore, Strands SDK, Lambda, API Gateway, AgentCore Gateway, Knowledge Base, Memory, Code Interpreter, Browser Tool, IAM, and CloudWatch.And then there was deployment, testing, and permissions.

Individually, none of those things sounded impossible. Together, they felt like a lot.

I think that is one of the hardest parts of learning cloud and AI systems. You can understand each word separately and still have no idea how the words are supposed to connect.

I initially wanted to understand the entire architecture before I started building. That didn't work very well. The more I tried to understand everything at once, the more overwhelming it became.

So I changed the question I was asking myself.

Instead of:

“How am I supposed to understand this entire project?”

I started asking:

“What is the next thing I need to understand?”

That became a much more manageable way to work.

And eventually, the pieces started connecting.

## So What Was This Agent Actually Supposed to Do?

The project was a fictional customer support system. A customer could ask something, and the AI agent needed to understand the request and use the appropriate capability.

The six capabilities were:

1. Order tracking
2. Refund processing
3. Product and policy questions
4. Customer memory across sessions
5. Loyalty discount calculation
6. Live website browsing

That meant this wasn't just a chatbot that generated a response. The agent could actually interact with other parts of a system, depending on what the customer needed.

A simplified view of the flow was:

Customer
 ↓
AI Agent
 ↓
What does the customer need?
 ↓
Use the appropriate capability
 ↓
Get the result
 ↓
AI Agent
 ↓
Final response
 ↓
Customer

Enter fullscreen mode

Exit fullscreen mode

At first, that flow looks straightforward. But every capability underneath it needed different infrastructure, and that is where the project became interesting.

## The Architecture Finally Made Sense When I Stopped Thinking in AWS Names

The biggest change in my thinking came when I stopped looking at the project as a list of AWS services. Instead, I started looking atwhat job each piece had.

TheAI modelwas responsible for understanding the customer's request and deciding what to do based on the instructions and available tools. For the project, I usedAmazon Nova 2 Litethrough Amazon Bedrock.

TheStrands SDKgave me the framework for building the agent and connecting its behavior with the tools and capabilities it needed.

Then there was the infrastructure that helped the agent actually do things.AgentCore Runtimewas where the deployed agent ran, whileAgentCore Gatewayprovided the connection between the agent and backend tools.API Gatewayexposed the order-related backend operations through APIs, andAWS Lambdaperformed those backend operations.

The other capabilities had their own pieces as well. TheKnowledge Baseprovided product and policy information that the agent could retrieve, whileAgentCore Memoryallowed useful customer information to be retrieved across sessions.Code Interpreterhandled calculations using actual code, and theBrowser Toolallowed the agent to interact with live webpages. Finally,CloudWatchhelped me monitor the deployed runtime.

Once I looked at those services by their jobs, rather than their names, the architecture became much less intimidating.

I wasn't trying to memorize AWS. I was trying to answer:

“What does my application need to do, and what piece is responsible for doing that?”

That question helped me much more.

## I Drew the Architecture Because I Needed to See It

I eventually made an architecture diagram in Excalidraw. I wanted it to show thestory of a request, rather than just put every AWS service on a page.

The idea was simple: the customer asks something, the agent figures out what the customer needs, the appropriate capability is used, and the result comes back to the agent. The agent then uses that result to respond to the customer. The supporting AWS services sit underneath the capabilities that need them.

This is the architecture I built for the project. Drawing it this way helped me understand the system as a flow instead of a collection of services.

Looking at the finished diagram now, it feels obvious to me. But I think that is because I built the pieces underneath it. The diagram became easier to understandafterI understood what each box was solving.

## The Six Capabilities Were Really Six Different Problems

Once the overall architecture made sense, I could look at each capability separately. That made the project feel much more manageable because I was no longer trying to understand six different things at the same time.

### 1. Order Tracking: Getting Real Data Back to the Customer

If a customer asked:

“Where is my order?”

the agent needed more than a generated sentence. It needed actual order information.

I created an order-tracking Lambda and exposed the required operations through API Gateway. AgentCore Gateway then provided the connection between the agent and those backend operations.

So the flow was roughly:

Customer
 ↓
Agent
 ↓
AgentCore Gateway
 ↓
API Gateway
 ↓
Lambda
 ↓
Order information
 ↓
Agent
 ↓
Customer

Enter fullscreen mode

Exit fullscreen mode

That was one of the first times the difference between a chatbot and an agent workflow became clearer to me. The model wasn't inventing the order status. It was asking another part of the system for the information.

### 2. Refunds: When the Agent Needs to Take an Action

Refund processing was similar, but the idea was slightly different. The agent wasn't just retrieving information. It needed to trigger an operation.

I connected the refund functionality through AgentCore Gateway to a Lambda function. This made something important click for me:a model saying that something happened and a system actually performing that action are two different things.

If an agent tells a customer:

“Your refund has been processed.”

there should be an actual operation behind that statement. That operation needs to succeed, the result needs to come back, and the agent should respond based on that result rather than simply assuming the action worked.

That is a very different way of thinking about AI applications compared with a simple question-and-answer chatbot.

### 3. Knowledge Base: The Model Knowing Isn't the Same as the Application Knowing

For product and policy questions, I used an Amazon Bedrock Knowledge Base. This was where I got a much more practical understanding of RAG.

Imagine a customer asks:

“What is the return policy?”

I don't want the model to generate something thatsoundslike a return policy. I want it to retrieve the information that belongs to the application.

The basic flow becomes:

Customer question
 ↓
Retrieve relevant information
 ↓
Give the information to the agent
 ↓
Generate the response

Enter fullscreen mode

Exit fullscreen mode

That made me realize something important: a model can know many things while still not knowmy application's information.

The Knowledge Base gives the agent a source of information it can retrieve from. That is much more useful than simply hoping the model happens to know the right answer.

### 4. Memory: When a New Conversation Isn't Really Starting From Zero

I also added AgentCore Memory. The goal was to allow the agent to remember useful customer information across sessions.

I tested this with a simple example. In one session, I told the agent a customer's name and response preference. Then I started a separate session and asked it to retrieve that information from the previous conversation.

It was able to do that.

This was interesting because the second session wasn't simply continuing the first conversation. The system had to retrieve the stored customer context.

That helped me understand the difference between:

“The model can see the previous messages.”

and:

“The application has a mechanism for retrieving relevant customer context.”

It also made me think about the responsibility that comes with memory. In a real customer support application, you would need to think carefully about what information is stored, how long it is retained, who can access it, and how customer information is protected.

Getting memory to work is only one part of the problem.

### 5. Code Interpreter: Let the Model Decide, Let Code Calculate

The loyalty discount was one of the more interesting pieces because I actually made a mistake here.

The agent needed to calculate a customer's discount using their loyalty tier, available points, and order total. My first calculation logic was incorrect because I was treating loyalty points and dollar values incorrectly.

The model wasn't the problem.My calculation logic was.

I fixed the calculation and redeployed the agent.

That taught me something I think is easy to forget when working with AI:an AI application still contains normal software engineering problems.

You can still have incorrect formulas, incorrect assumptions, edge cases, configuration problems, and bugs. The fact that a model is involved doesn't remove any of those.

It also helped me understand why Code Interpreter was useful. The model could understand that a calculation was needed, while code could perform the actual calculation. For precise arithmetic, that separation made much more sense to me than asking the model to do everything itself.

### 6. Browser Tool: When the Information Isn't Inside Your Application

The final capability was live web browsing. I used the AgentCore Browser Tool and tested it by asking the agent to visit the Udacity website and return the page title.

This was different from the Knowledge Base because the information wasn't sitting inside my application. The agent had to interact with a live webpage.

That helped me see another side of tools:a tool isn't necessarily just a function that returns data.It can give the agent a way to interact with something outside the model's immediate context.

## Having the Right Code Doesn't Mean Having Access to It

This was probably one of the most practical lessons of the project. There were times when the architecture made sense and the code was there, but something still didn't work. The reason was permissions.

The AgentCore runtime needed the right permissions to access resources such as Memory and the Knowledge Base. The Browser Tool also needed the appropriate permissions before it could start a browser session.

This changed the way I approached debugging. Before this project, I might have immediately looked for a code problem. During this project, I started asking a different set of questions:Does the resource exist? Is it in the correct region? Does the runtime have permission to access it? Is the IAM role correct? Is the specific action allowed? Is the tool configured correctly?

That was a much better debugging mindset because sometimes the problem isn't:

“My code doesn't work.”

It is:

“My code is trying to use something it isn't allowed to use.”

The Browser Tool gave me a good example of this. I had the browser capability configured, but the runtime couldn't start the browser session. It would have been easy to assume that the Browser Tool itself was broken.

The actual issue was that the runtime was missing the required permission. I added the permission and tested it again, and this time, it worked.

It was a small fix, but it taught me something important about cloud applications:there is a lot around the code.The application has identities, permissions, resources, configurations, and service connections. All of those pieces have to agree before a feature can actually work.

## Deployment Wasn't the Finish Line

Once the pieces were working, I deployed the agent using the AgentCore deployment workflow. This was another point where I changed how I think about deployment.

A successful deployment doesn't automatically mean a successful application. The runtime can deploy successfully while one of the tools still has a configuration or permission problem.

So I treated deployment as the beginning of testing rather than the end of development. I tested the deployed agent capability by capability, which gave me much more confidence than simply seeing a successful deployment message.

## Six Tests Were Easier Than One Giant “Does It Work?”

Instead of asking myself,“Does my AI agent work?”, I broke that question into smaller ones.

Can it track an order? Can it process a refund? Can it answer from the Knowledge Base? Can it remember information across sessions? Can it calculate the loyalty discount correctly? Can it browse a live website?

Each one became its own test.

I captured evidence for each of these tests, which gave me six concrete things to verify instead of one enormous pass/fail question.

And eventually, all six worked.

That was a much less intimidating way to test the project.

## The Part That Became Clear Only After Everything Worked

Looking back, I think the biggest shift happened after I had all six capabilities working. Before that, I was thinking about individual services. After that, I could finally see the pattern.

The model understands the request, the agent determines what it needs, and a tool provides the appropriate capability. Another service performs the work, the result comes back, and the agent uses that result to respond. That pattern repeats across the six capabilities.

The actual tools are different, but the underlying idea is similar:

Order tracking
→ retrieve backend information

Refund
→ perform a backend action

Knowledge Base
→ retrieve application information

Memory
→ retrieve customer context

Code Interpreter
→ perform computation

Browser
→ interact with live information

Enter fullscreen mode

Exit fullscreen mode

That was when the wordagentfinally started making sense to me.

It wasn't simply:

“An AI model that talks to you.”

It was:

“A model that can understand what needs to happen and use capabilities to actually do something about it.”

## There Was Another Layer I Hadn't Thought About Enough: Operating the System

Once the agent was working, I started thinking about what would happen if this were a real customer support application. A customer doesn't care which service failed. They just know their request didn't work.

For example, an order request could travel through:

Customer
 ↓
AgentCore Runtime
 ↓
Agent
 ↓
AgentCore Gateway
 ↓
API Gateway
 ↓
Lambda
 ↓
Response

Enter fullscreen mode

Exit fullscreen mode

If something fails somewhere in that chain, the engineering team needs to know where. That's where monitoring becomes important.

For this project, I used CloudWatch to monitor the AgentCore runtime and created a CPU usage alarm. If I were taking this system further for real production usage, I would want to monitor things such asfailed requests, error rates, response times, tool failures, resource usage, service health, and costs.

Cost would also matter because this agent uses multiple managed services. A project that works perfectly with a small number of requests could have a very different cost profile at much larger scale.

That made me realize something:

Building something that works and operating something reliably are different problems.

## I Also Had to Learn When the Project Was Actually Finished

After the agent was working and the project was submitted, I went back through the AWS resources I had created and cleaned up the project-specific resources.

This wasn't the exciting part of the project, but I think it is an important part of cloud work. Getting the application to work isn't necessarily the same as being finished with the cloud environment around it.

When you create cloud resources, you should know what you created, what is still running, and what happens when you are done with it. Leaving resources active after a project is over can lead to unnecessary usage and costs, especially when multiple managed services are involved.

For someone learning with a limited cloud budget, that matters even more. I wanted to finish the project knowing that I had cleaned up what I no longer needed.

For me, cleanup became part of whatactually finishing the projectmeant, not something separate from it.

## What This Project Actually Taught Me

If I could go back to the beginning, I wouldn't tell myself,“Learn everything first.”I would tell myself:

“You don't need to understand the whole architecture before you start.”

When I first saw the project, I wanted to understand AgentCore, Lambda, API Gateway, IAM, RAG, Memory, Browser Tool, Code Interpreter, deployment, and monitoring all together. That was too much. I could understand what each service was called, but that didn't mean I understood how all of them were supposed to work together.

What helped was breaking the project down into smaller questions:What does this resource do? Why does the agent need it? What does it connect to? What should happen when I test it? What happens if it fails?

Those questions were much easier to answer, and each answer made the next one easier.

I think this is especially useful when you're starting something that looks too big. It is easy to look at a cloud architecture full of services and think:

“I don't know any of this.”

But you don't need to know all of it at once. Start with the application and ask what the user needs to happen. Then ask what the system needs in order to make that happen, and learn the service that solves that particular problem.

If you need to store data, learn the database piece. If you need to execute backend logic, learn the compute piece. If the agent needs to retrieve information, learn the retrieval piece. If it needs to remember customer context, learn the memory piece. If it needs to interact with an external capability, learn the tool or gateway piece.

You also don't have to assume that every problem is an AI problem. A missing permission can look like a broken feature. A configuration problem can look like broken code. A calculation bug can look like a model problem. A deployment can succeed while one capability is still misconfigured.

That was another important lesson for me. Before this project, I might have immediately looked for a code problem. During this project, I became more comfortable asking whether the resource existed, whether it was in the right region, whether the runtime had permission to access it, whether the IAM role was correct, and whether the specific action was allowed.

I started this project thinking I was mainly going to learnAmazon Bedrock AgentCore. I did, but I ended up learning several things around it too. I learned how an AI agent can use tools to interact with backend systems, how a Knowledge Base can give an agent access to application-specific information, how Memory changes what a conversation can mean across sessions, and why precise calculations sometimes belong in code rather than in the model's reasoning.

I also learned that IAM isn't something you set up once and forget about, that a successful deployment doesn't prove every capability works, that monitoring matters even for a relatively small project, and that cloud development includes knowing how to clean up what you create.

I don't think the biggest lesson I am taking into my next project is one specific AWS service. It is a way of approaching projects that initially look too big.

When I see a complicated architecture now, I don't immediately think:

“I need to understand everything.”

I think:

“What is the first piece?”

Then I work from there.

That doesn't mean the project suddenly becomes easy. There are still confusing moments, permissions to figure out, code to debug, and configuration to understand. Sometimes you understand a service after reading about it. Sometimes you understand it after using it. And sometimes you understand it only after something breaks and you have to figure out why.

All three are learning.

So if you're somewhere at the beginning of your own AI or cloud journey and you're looking at a project that feels like too much, start with one thing. Understand what it is supposed to do. Make that part work. Then move to the next.

You don't have to build the entire system in your head before you build it in reality.

And that is probably the thing I value most from this project.

I learned how to make a complicated project feel manageable.

Not by making the project smaller.

By making thenext problemsmaller.

## A Small Thank You

I want to thankUdacityand everyone involved in theFuture AWS Agent Engineer Nanodegree Programfor giving me the opportunity to work through a project like this. And I'm especially grateful for theAWS AI & ML Scholarshipthat made the program possible for me.

This project gave me something I don't think I would have understood as clearly by only reading about AgentCore. I had to actually connect the pieces, troubleshoot them, and test them. Eventually, I could look back at the architecture and realize that I understood what I was looking at.

That was probably the most valuable part for me.

## I Would Love to Hear From You

If you've built an AI agent, worked with AWS, or are currently learning cloud engineering, I'd genuinely love to hear from you.

What was the first cloud or AI concept that felt completely confusing at first, but eventually started making sense to you?Or, if you're currently building something difficult, what part are you working through right now?

Share it in the comments.

Sometimes the thing that feels obvious to you now is exactly the thing someone else is struggling to understand.

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

 View full discussion (17 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse