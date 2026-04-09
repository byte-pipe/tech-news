---
title: 'Agent Development Kit: Making it easy to build multi-agent applications - DEV Community'
url: https://dev.to/googleai/agent-development-kit-making-it-easy-to-build-multi-agent-applications-4594
site_name: devto
fetched_at: '2025-08-06T01:07:05.131784'
original_url: https://dev.to/googleai/agent-development-kit-making-it-easy-to-build-multi-agent-applications-4594
author: Erwin Huizenga
date: '2025-07-29'
description: The world of AI is rapidly moving beyond single-purpose models towards intelligent, autonomous... Tagged with googlecloud, machinelearning, ai, webdev.
tags: '#googlecloud, #machinelearning, #ai, #webdev'
---

The world of AI is rapidly moving beyond single-purpose models towards intelligent, autonomous multi-agent systems. Building these multi-agent systems, however, presents new challenges. That is why we haveintroduced Agent Development Kit(ADK) atGoogle Cloud NEXT 2025, a new open-source framework from Google designed to simplify the full stack end-to-end development of agents and multi-agent systems. ADK empowers developers like you to build production-ready agentic applications with greater flexibility and precise control.

ADK is the same framework powering agents within Google products like Agentspace and the Google Customer Engagement Suite (CES). By open-sourcing ADK, we aim to provide developers with powerful, flexible tools to build in the rapidly evolving agent landscape. The ADK is designed to be flexible, use different models and build production ready agents for different deployment environments.

## Core Pillars of ADK: Build, Interact, Evaluate, Deploy

ADK provides capabilities across the entire agent development lifecycle:

* Multi-Agent by Design:Build modular and scalable applications by composing multiple specialized agents in a hierarchy. Enable complex coordination and delegation.
* Rich Model Ecosystem:Choose the model that works best for your needs. ADK works with your model of choice – whether it is Gemini or your any model accessible via Vertex AI Model Garden. The framework also offers LiteLLM integration letting you choose from a wide selection of models from providers like Anthropic, Meta, Mistral AI, AI21 Labs, and many more!
* Rich Tool Ecosystem:Equip agents with diverse capabilities: use pre-built tools (Search, Code Exec), Model Context Protocol (MCP) tools, integrate 3rd-party libraries (LangChain, LlamaIndex), or even use other agents as tools (LangGraph, CrewAI, etc).
* Built-in streaming:Interact with your agents in human-like conversations with ADK's unique bidirectional audio and video streaming capabilities. With just a few lines of code, you can create natural interactions that change how you work with agents – moving beyond text into rich, multimodal dialogue.
* Flexible Orchestration:Define workflows using workflow agents (Sequential,Parallel,Loop) for predictable pipelines, or leverage LLM-driven dynamic routing (LlmAgenttransfer) for adaptive behavior.
* Integrated Developer Experience: Develop, test, and debug locally with a powerful CLI and a visual Web UI. Inspect events, state, and agent execution step-by-step.
* Built-in Evaluation: Systematically assess agent performance by evaluating both the final response quality and the step-by-step execution trajectory against predefined test cases.
* Easy Deployment: Containerize and deploy your agents anywhere.

## Getting started with your first agent

While we encourage you to explore the examples in thedocs, the core idea is Pythonic simplicity. You define your agent's logic, the tools it can use, and how it should process information. ADK provides the structure to manage state, orchestrate tool calls, and interact with the underlying LLMs. Here is an illustrative example of a basic agent.

The code can be found in thequickstart guide.

from

google.adk.agents

import

LlmAgent

from

google.adk.tools

import

google_Search

dice_agent

=

LlmAgent
(


model
=
"
gemini-2.0-flash-exp
"
,

# Required: Specify the LLM


name
=
"
question_answer_agent
"
,

# Required: Unique agent name


description
=
"
A helpful assistant agent that can answer questions.
"
,


instruction
=
"""
Respond to the query using google search
"""
,


tools
=
[
google_search
],

# Provide an instance of the tool

)

# you can run this by using adk web

Enter fullscreen mode

Exit fullscreen mode

This simple example shows the basic structure. ADK truly shines when building more complex applications involving multiple agents, sophisticated tool use, and dynamic orchestration, all while maintaining control.

ADK offers flexibility in the way you interact with your agents: CLI, Web UI, API Server and API (Python). The way you define your agent (the core logic withinagent.py) is the same regardless of how you choose to interact with it. The difference lies in how you initiate and manage the interaction. For all you find examples in theADK documentation.

## Building Multi-Agent Applications with ADK

ADK truly shines when you move beyond single agents to build collaborative multi-agent systems that leverage tools. Imagine creating a team of specialized agents where a primary agent can delegate tasks based on the conversation. ADK makes this easy through hierarchical structures and intelligent routing.

Let's walk through an illustrative example – aWeatherAgentthat handles weather queries but delegates greetings to a specialized GreetingAgent.

1. Define a Tool:Agents use tools to perform actions. Here, ourWeatherAgentneeds a tool to fetch weather data. We define a Python function; ADK uses itsdocstringto understand when and how to use it.

def

get_weather
(
city
:

str
)

->

Dict
:


# Best Practice: Log tool execution for easier debugging


print
(
f
"
--- Tool: get_weather called for city:
{
city
}
 ---
"
)


city_normalized

=

city
.
lower
().
replace
(
"

"
,

""
)

# Basic input normalization


# Mock weather data for simplicity (matching Step 1 structure)


mock_weather_db

=

{


"
newyork
"
:

{
"
status
"
:

"
success
"
,

"
report
"
:

"
The weather in New York is sunny with a temperature of 25°C.
"
},


"
london
"
:

{
"
status
"
:

"
success
"
,

"
report
"
:

"
It
'
s cloudy in London with a temperature of 15°C.
"
},


"
tokyo
"
:

{
"
status
"
:

"
success
"
,

"
report
"
:

"
Tokyo is experiencing light rain and a temperature of 18°C.
"
},


"
chicago
"
:

{
"
status
"
:

"
success
"
,

"
report
"
:

"
The weather in Chicago is sunny with a temperature of 25°C.
"
},


"
toronto
"
:

{
"
status
"
:

"
success
"
,

"
report
"
:

"
It
'
s partly cloudy in Toronto with a temperature of 30°C.
"
},


"
chennai
"
:

{
"
status
"
:

"
success
"
,

"
report
"
:

"
It
'
s rainy in Chennai with a temperature of 15°C.
"
},


}


# Best Practice: Handle potential errors gracefully within the tool


if

city_normalized

in

mock_weather_db
:


return

mock_weather_db
[
city_normalized
]


else
:


return

{
"
status
"
:

"
error
"
,

"
error_message
"
:

f
"
Sorry, I don
'
t have weather information for
'
{
city
}
'
.
"
}

Enter fullscreen mode

Exit fullscreen mode

2. Define the Agents and Their Relationship:We useLlmAgentto create our agents. Pay close attention to the instruction and description fields – the LLM relies heavily on these for understanding roles and making delegation decisions using auto delegations for sub agents.

greeting_agent

=

Agent
(


model
=
LiteLlm
(
model
=
"
anthropic/claude-3-sonnet-20240229
"
),


name
=
"
greeting_agent
"
,


instruction
=
"
You are the Greeting Agent. Your ONLY task is to provide a friendly greeting to the user.
"

"
Do not engage in any other conversation or tasks.
"
,


# Crucial for delegation: Clear description of capability


description
=
"
Handles simple greetings and hellos
"
,


)

farewell_agent

=

Agent
(


model
=
LiteLlm
(
model
=
"
anthropic/claude-3-sonnet-20240229
"
),


name
=
"
farewell_agent
"
,


instruction
=
"
You are the Farewell Agent. Your ONLY task is to provide a polite goodbye message.
"


"
Do not perform any other actions.
"
,


# Crucial for delegation: Clear description of capability


description
=
"
Handles simple farewells and goodbyes
"
,


)

root_agent

=

Agent
(


name
=
"
weather_agent_v2
"
,


model
=
"
gemini-2.0-flash-exp
"
,


description
=
"
You are the main Weather Agent, coordinating a team. - Your main task: Provide weather using the `get_weather` tool. Handle its
'
status
'
 response (
'
report
'
 or
'
error_message
'
). - Delegation Rules: - If the user gives a simple greeting (like
'
Hi
'
,
'
Hello
'
), delegate to `greeting_agent`. - If the user gives a simple farewell (like
'
Bye
'
,
'
See you
'
), delegate to `farewell_agent`. - Handle weather requests yourself using `get_weather`. - For other queries, state clearly if you cannot handle them.
"
,


tools
=
[
get_weather
],

# Root agent still needs the weather tool


sub_agents
=
[
greeting_agent
,

farewell_agent
]

)

Enter fullscreen mode

Exit fullscreen mode

### How Delegation Works:

* The default agent behavior is to allow delegation.
* When processing a user message, the LLM considers the query, the current agent'sdescription, and thedescriptionfields of related agents (parent / sub agents defined in the hierarchy).
* If the LLM determines another agent is a better fit based on its description (e.g., user says "Hi", matching theGreetingAgentdescription, it initiates a transfer.
* Clear, distinct descriptions are vital! The LLM uses them to route tasks effectively.

In this setup, if a user starts with "Hi", theWeatherAgent(if it's the root agent processing the input) can recognize it's not a weather query, see theGreetingAgentis suitable via its description, and automatically transfer control. If the user asks "What's the weather in Chicago?", theWeatherAgenthandles it directly using itsget_weathertool.

This example demonstrates how ADK's hierarchical structure and description-driven delegation allow you to build organized, maintainable, and sophisticated multi-agent applications.

## Completing the Lifecycle: Evaluation and Deployment

Building intelligent agents like our weather agent is foundational, but bringing them reliably to users involves crucial next steps: rigorous evaluation and seamless deployment. Before going live, ensuring your agent behaves predictably and correctly is paramount. ADK's integrated evaluation tools are designed precisely for this, letting you systematically test execution paths and response quality against predefined datasets, likeevaluation.test.jsonortest.json. You can run these checks programmatically within your test suites usingAgentEvaluator.evaluate(). You can also use evaluation directly via the ADK eval command-line tool or via the web UI.

Once you're satisfied with performance, ADK offers a clear and streamlined path to production through the option to deploy to any container runtime or using its integration with Vertex AI Agent Engine. This allows you to leverage a fully managed, scalable, and enterprise-grade runtime, completing the development lifecycle and empowering you to move from sophisticated prototypes to robust, production-ready agentic applications.

## Choosing the framework for you: ADK or Genkit?

As you explore the possibilities of building multi-agent systems with ADK, you might be wondering how it fits into the broader landscape of GenAI development tools from Google. While a variety of SDKs and frameworks are available, such as theGenkit framework, it's helpful to understand ADK's relative focus. Here's a quick comparison:

### Agent Development Kit:

* Optimized for complex agents and multi-agent systems, it provides higher-level abstractions for agent development with built-in integration for LiteLLM and Vertex AI Model Garden supporting a variety of models.
* Focuses on defining agent behaviors and interactions.
* Supports bidirectional streaming.

### Genkit:

* Provides fundamental building blocks for building a large variety of AI powered experiences.
* Includes developer tooling for iterating, testing and debugging your AI related interactions.
* Support a wide variety of large language models from Google AI, Vertex AI, and from 3rd parties through community plugins.

### Choosing the Right Tool

Ultimately, the best choice depends on your project's specific goals. If you are building intricate, collaborative agent systems within a well-defined framework, ADK offers a powerful solution. For many other GenAI projects requiring flexibility and broad model support, Genkit is an excellent choice.

## ADK works anywhere, but optimized for Google Cloud

While the Agent Development Kit (ADK) offers flexibility to work with various tools, it is optimized for seamless integration within the Google Cloud ecosystem, specifically with Gemini models and Vertex AI. This tailored design allows developers to fully leverage the advanced capabilities of Gemini, such as the enhanced reasoning and tool use found in Gemini 2.5 Pro Experimental, and provides a direct, native pathway to deploy these agents onto Vertex AI's fully-managed, enterprise-grade runtime for scalability.

Crucially, this deep integration extends to your broader enterprise landscape; ADK enables agents to connect directly to systems and data through over 100 pre-built connectors, utilize workflows built with Application Integration, and access data stored in systems like AlloyDB, BigQuery, and NetApp without requiring data duplication.

Additionally, agents built with ADK can securely tap into your organization's existing API investments managed through Apigee, further enhancing their capabilities by leveraging established interfaces.

This comprehensive connectivity across advanced AI models, scalable deployment, diverse data sources, and existing APIs makes ADK exceptionally powerful when used within the Google Cloud environment.

## Build the next generation of Agents with ADK

The Agent Development Kit (ADK) provides a powerful, flexible, and open-source foundation for building the next generation of AI applications. It tackles the core challenges of multi-agent development by offering:

* Precise controlover agent behavior and orchestration.
* Arich ecosystemfor tools and integrations.
* Anintegrated developer experience for building and debugging.
* Arobust evaluation frameworkessential for reliable agents.
* Aclear path to deployment, including managed options.
We're incredibly excited to see what you build with ADK!

Explore the Code:Official ADK Documentation.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
