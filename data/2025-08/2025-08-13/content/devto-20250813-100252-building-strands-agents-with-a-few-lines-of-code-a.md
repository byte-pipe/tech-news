---
title: 'Building Strands Agents with a few lines of code: Agent-to-Agent (A2A) Communication - DEV Community'
url: https://dev.to/aws/building-strands-agents-with-a-few-lines-of-code-agent-to-agent-a2a-communication-18h1
site_name: devto
fetched_at: '2025-08-13T10:02:52.954219'
original_url: https://dev.to/aws/building-strands-agents-with-a-few-lines-of-code-agent-to-agent-a2a-communication-18h1
author: Elizabeth Fuentes L
date: '2025-08-07'
description: 🇻🇪🇨🇱 Dev.to Linkedin GitHub Twitter Instagram Youtube Linktr ... Tagged with python, aws, beginners, programming.
tags: '#python, #aws, #beginners, #programming'
---

🇻🇪🇨🇱Dev.toLinkedinGitHubTwitterInstagramYoutubeLinktr

## Elizabeth Fuentes LFollow

AWS Developer Advocate

GitHub repository

Agent-to-agent (A2A) communication represents the next evolution in AI automation, where multiple specialized agents collaborate to solve complex problems.

With the Strands Agent framework, you can build multi-agent systems that coordinate seamlessly to handle tasks beyond the capabilities of individual agents.

In this blog, you'll learn how to create agents that communicate with each other, share information, and work together to accomplish complex workflows using the new Strands A2A Tools.

## ⭐ Understanding Agent-to-Agent Communication

The Agent-to-Agent protocol is an open standard that defines how AI agents can discover, communicate, and collaborate with each other.

A2A protocol support enables several powerful use cases:

* Multi-Agent Workflows: Chain multiple specialized agents together
* Agent Marketplaces: Discover and use agents from different providers
* Cross-Platform Integration: Connect Strands agents with other A2A-compatible systems
* Distributed AI Systems: Build scalable, distributed agent architectures

### MCP vs A2A

It's important to understand how A2A relates to MCP, or Model Context Protocol. These are complementary standards.

* MCP connects agents to tools, APIs, and resources with structured inputs/outputs. Think of it as how agents access their capabilities.
* A2A facilitates dynamic communication between different agents as peers. It's how agents collaborate, delegate, and manage shared tasks.

They're complementary - MCP gives agents their tools, A2A enables collaboration.

### A2A Architecture

* Primary Agent: Initiates communication and delegates tasks (the "manager")
* Secondary Agent(s): Receive tasks and provide responses (the "specialists")
* A2A Tool: Handles protocol details for seamless communication between the agents
* Message Protocol: Defines message format and structure

## 🚀 Getting Started

Clone the sample repository:

git clone https://github.com/elizabethfuentes12/strands-agent-samples

cd
notebook

Enter fullscreen mode

Exit fullscreen mode

Create and activate a virtual environment:

python
-m
 venv .venv

source
 .venv/bin/activate
# On Windows: .venv\Scripts\activate

Enter fullscreen mode

Exit fullscreen mode

Install the required dependencies:

pip
install

-r
 requirements.txt

Enter fullscreen mode

Exit fullscreen mode

## 🔧 Creating Your First Agent-to-Agent System

In this section, we will do a walkthrough of selected code blocks, that have been used to buildstrands-a2a-inter-agent, based on thesample-agentic-ai-demos repositorie(thanksJames Ward) to create a A2A agent.

In our example, we'll explore a three-tier architecture where:

* AnHR Agentcommunicates with an Employee Agent
* TheEmployee Agentcommunicates with an MCP Server
* TheMCP Serverprovides access to employee data

Here's the basic implementation:

### 1. Employee Data

First, we have a simple module that generates random employee data with skills:

import

random

FIRST_NAMES

=

[
"
James
"
,

"
Mary
"
,

"
John
"
,

"
Patricia
"
,

"
Robert
"
,

"
Jennifer
"
,

"
Michael
"
,

"
Linda
"
,

"
William
"
,

"
Elizabeth
"
]

LAST_NAMES

=

[
"
Smith
"
,

"
Johnson
"
,

"
Williams
"
,

"
Brown
"
,

"
Jones
"
,

"
Garcia
"
,

"
Miller
"
,

"
Davis
"
,

"
Rodriguez
"
,

"
Martinez
"
]

SKILLS

=

{


"
Kotlin
"
,

"
Java
"
,

"
Python
"
,

"
JavaScript
"
,

"
TypeScript
"
,


"
React
"
,

"
Angular
"
,

"
Spring Boot
"
,

"
AWS
"
,

"
Docker
"
,


"
Kubernetes
"
,

"
SQL
"
,

"
MongoDB
"
,

"
Git
"
,

"
CI/CD
"
,


"
Machine Learning
"
,

"
DevOps
"
,

"
Node.js
"
,

"
REST API
"
,

"
GraphQL
"

}

EMPLOYEES

=

list
({
emp
[
"
name
"
]:

emp

for

emp

in

[


{


"
name
"
:

f
"
{
random
.
choice
(
FIRST_NAMES
)
}

{
random
.
choice
(
LAST_NAMES
)
}
"
,


"
skills
"
:

random
.
sample
(
list
(
SKILLS
),

random
.
randint
(
2
,

5
))


}


for

i

in

range
(
100
)

]}.
values
())

Enter fullscreen mode

Exit fullscreen mode

### 2. MCP Server

Next, we have an MCP server that exposes tools to access the employee data:

from

mcp.server.fastmcp

import

FastMCP

from

employee_data

import

SKILLS
,

EMPLOYEES

mcp

=

FastMCP
(
"
employee-server
"
,

stateless_http
=
True
,

host
=
"
0.0.0.0
"
,

port
=
8002
)

@mcp.tool
()

def

get_skills
()

->

set
[
str
]:


"""
all of the skills that employees may have - use this list to figure out related skills
"""


print
(
"
get_skills
"
)


return

SKILLS

@mcp.tool
()

def

get_employees_with_skill
(
skill
:

str
)

->

list
[
dict
]:


"""
employees that have a specified skill - output includes fullname (First Last) and their skills
"""


print
(
f
"
get_employees_with_skill(
{
skill
}
)
"
)


skill_lower

=

skill
.
lower
()


employees_with_skill

=

[
employee

for

employee

in

EMPLOYEES

if

any
(
s
.
lower
()

==

skill_lower

for

s

in

employee
[
"
skills
"
])]


if

not

employees_with_skill
:


raise

ValueError
(
f
"
No employees have the
{
skill
}
 skill
"
)


return

employees_with_skill

if

__name__

==

"
__main__
"
:


mcp
.
run
(
transport
=
"
streamable-http
"
)

Enter fullscreen mode

Exit fullscreen mode

The MCP server exposes two tools:

1. get_skills(): Returns all possible skills that employees may have
2. get_employees_with_skill(skill): Returns employees that have a specific skill

These tools are exposed via the Model Context Protocol (MCP) using the FastMCP framework, which provides a standardized way for agents to access these functions.

## 3. Employee Agent

The Employee Agent connects to the MCP server and exposes its capabilities through an A2A server:

import

os

from

mcp.client.streamable_http

import

streamablehttp_client

from

strands

import

Agent

from

strands.tools.mcp.mcp_client

import

MCPClient

from

strands.multiagent.a2a

import

A2AServer

from

urllib.parse

import

urlparse

from

strands.models.anthropic

import

AnthropicModel

# Define URLs correctly

EMPLOYEE_INFO_URL

=

"
http://localhost:8002/mcp/
"

EMPLOYEE_AGENT_URL

=

"
http://localhost:8001/
"

# Create the MCP client

employee_mcp_client

=

MCPClient
(
lambda
:

streamablehttp_client
(
EMPLOYEE_INFO_URL
))

model

=

AnthropicModel
(


client_args
=
{


"
api_key
"
:

"
YOUR_API_KEY_HERE
"
,

# Replace with your API key


},


max_tokens
=
1028
,


model_id
=
"
claude-sonnet-4-20250514
"
,


params
=
{


"
temperature
"
:

0.7
,


}

)

# Use the MCP client within a context

with

employee_mcp_client
:


tools

=

employee_mcp_client
.
list_tools_sync
()


# Create a Strands agent


employee_agent

=

Agent
(


model
=
model
,


name
=
"
Employee Agent
"
,


description
=
"
Answers questions about employees
"
,


tools
=
tools
,


system_prompt
=
"
you must abbreviate employee first names and list all their skills
"


)


# Create A2A server


a2a_server

=

A2AServer
(


agent
=
employee_agent
,


host
=
urlparse
(
EMPLOYEE_AGENT_URL
).
hostname
,


port
=
int
(
urlparse
(
EMPLOYEE_AGENT_URL
).
port
)


)


# Start the server


if

__name__

==

"
__main__
"
:


a2a_server
.
serve
(
host
=
"
0.0.0.0
"
,

port
=
8001
)

Enter fullscreen mode

Exit fullscreen mode

### Server Configuration Options

The A2AServer exposes the agent's capabilities to other agents through an HTTP API and accepts several configuration options:

* agent: The Strands Agent to wrap with A2A compatibility
* host: Hostname or IP address to bind to (default: "0.0.0.0")
* port: Port to bind to (default: 9000)
* ersion: Version of the agent (default: "0.0.1")
* skills: Custom list of agent skills (default: auto-generated from tools)
* http_url: Public HTTP URL where this agent will be accessible (optional, enables path-based mounting)
* serve_at_root: Forces server to serve at root path regardless of http_url path (default: False)

## 4. HR Agent

Finally, the HR Agent provides a user-facing API and communicates with the Employee Agent.

* Creates a FastAPI application to handle HTTP requests
* Uses the A2AClientToolProvider for discovering and interacting with A2A agents without manually writing client code.
* Provides an endpoint for users to ask questions about employees

This agent serves as the entry point for user queries and delegates specialized tasks to the Employee Agent when needed.

import

os

import

uvicorn

from

strands

import

Agent

from

strands.models

import

BedrockModel

from

strands_tools.a2a_client

import

A2AClientToolProvider

from

fastapi

import

FastAPI

from

fastapi.responses

import

StreamingResponse

from

pydantic

import

BaseModel

EMPLOYEE_AGENT_URL

=

"
http://localhost:8001/
"

app

=

FastAPI
(
title
=
"
HR Agent API
"
)

class

QuestionRequest
(
BaseModel
):


question
:

str

@app.get
(
"
/health
"
)

def

health_check
():


return

{
"
status
"
:

"
healthy
"
}

model

=

AnthropicModel
(


client_args
=
{


"
api_key
"
:

os
.
getenv
(
"
api_key
"
),


},


# **model_config


max_tokens
=
1028
,


model_id
=
"
claude-3-7-sonnet-20250219
"
,


params
=
{


"
temperature
"
:

0.3
,


}

)

@app.post
(
"
/inquire
"
)

async

def

ask_agent
(
request
:

QuestionRequest
):


async

def

generate
():


provider

=

A2AClientToolProvider
(
known_agent_urls
=
[
EMPLOYEE_AGENT_URL
])


agent

=

Agent
(
model
=
bedrock_model
,

tools
=
provider
.
tools
)


stream_response

=

agent
.
stream_async
(
request
.
question
)


async

for

event

in

stream_response
:


if

"
data
"

in

event
:


yield

event
[
"
data
"
]


return

StreamingResponse
(


generate
(),


media_type
=
"
text/plain
"


)

if

__name__

==

"
__main__
"
:


uvicorn
.
run
(
app
,

host
=
"
0.0.0.0
"
,

port
=
8000
)

Enter fullscreen mode

Exit fullscreen mode

## ✅ Running the Example

### Option 1: Run each component in a separate terminal:

1. Set your API key:


export
api_key
=
'your-anthropic-api-key-here'

Enter fullscreen mode

Exit fullscreen mode

2. Install Required Packages:


!
pip
install

-r
 requirements.txt

Enter fullscreen mode

Exit fullscreen mode

3. Start the MCP Server:

python3 strands-a2a-inter-agent/server.py

Enter fullscreen mode

Exit fullscreen mode

4. Start the Employee Agent:

python employee-agent.py

Enter fullscreen mode

Exit fullscreen mode

5. Start the HR Agent:

python hr-agent.py

Enter fullscreen mode

Exit fullscreen mode

6. Make a request to the HR Agent:

Once all three components are running, you can make requests to the HR Agent:

curl
-X
 POST
--location

"http://0.0.0.0:8000/inquire"

\

-H

"Content-Type: application/json"

\

-d

'{"question": "list employees that have skills related to AI programming"}'

Enter fullscreen mode

Exit fullscreen mode

### Option 2: Runs the MCP Server, Employee Agent, and HR Agent in parallel

1. Set your API key:


export
api_key
=
'your-anthropic-api-key-here'

Enter fullscreen mode

Exit fullscreen mode

2. Install Required Packages:


!
pip
install

-r
 requirements.txt

Enter fullscreen mode

Exit fullscreen mode

3. Start the system:

 python run_a2a_system.py

Enter fullscreen mode

Exit fullscreen mode

4. Make Requests to the HR Agent

Once all three components are running, you can make requests to the HR Agent:

curl
-X
 POST
--location

"http://0.0.0.0:8000/inquire"

\

-H

"Content-Type: application/json"

\

-d

'{"question": "list employees that have skills related to AI programming"}'

Enter fullscreen mode

Exit fullscreen mode

## 🎯 Best Practices for A2A Communication

1. Clear Agent Responsibilities: Define specific roles for each agent
2. Error Handling: Implement robust error handling and fallback mechanisms
3. Message Format Standardization: Use consistent message formats between agents
4. Performance Monitoring: Track response times and success rates
5. Security Considerations: Validate messages between agents
6. Testing Strategy: Test individual agents and their interactions

## 🔮 Next Steps

This introduction to A2A communication with Strands Tools opens up numerous possibilities for building sophisticated AI systems. In upcoming posts, I'll explore:

* Advanced coordination patterns and workflows
* Integration with external systems and APIs
* Performance optimization for multi-agent systems
* Real-world deployment scenarios using AWS CDK

The complete code and examples are available in theGitHub repository. Experiment with different agent configurations and communication patterns to discover what works best for your use cases.

Stay tuned for more advanced Strands Agent implementations!

## 📚 Resources

* Strands Agent Documentation
* Part 1: Basic Multi-Modal Processing
* Complete Code Examples
* AWS Bedrock Documentation
* Getting Started with Strands Agents

¡Gracias!

GitHub repository

🇻🇪🇨🇱Dev.toLinkedinGitHubTwitterInstagramYoutubeLinktr

## Elizabeth Fuentes LFollow

AWS Developer Advocate

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
