---
title: Building Production-Ready AI Agents with LlamaIndex and Amazon Bedrock AgentCore - DEV Community
url: https://dev.to/aws/building-production-ready-ai-agents-with-llamaindex-and-amazon-bedrock-agentcore-1fm3
site_name: devto
fetched_at: '2025-09-15T19:06:13.947236'
original_url: https://dev.to/aws/building-production-ready-ai-agents-with-llamaindex-and-amazon-bedrock-agentcore-1fm3
author: Danilo Poccia
date: '2025-09-15'
description: In this fourth deep dive of our multi-framework series, I'll show you how to build a production-ready... Tagged with ai, aws, bedrock, agentcore.
tags: '#ai, #aws, #bedrock, #agentcore'
---

In this fourth deep dive of ourmulti-framework series, I'll show you how to build a production-ready AI agent usingLlamaIndexand deploy it usingAmazon Bedrock AgentCore. The complete code for this implementation, along with examples for other frameworks, is available on GitHub atagentcore-multi-framework-examples.

LlamaIndex takes a data-centric approach to agent development. While other frameworks focus primarily on orchestration and tool calling, LlamaIndex specializes in connecting agents with diverse data sources and building RAG (Retrieval-Augmented Generation) pipelines. This is useful when your agent needs to reason over documents, databases, or APIs while maintaining production-grade memory persistence through AgentCore.

LlamaIndex provides specialized components for every aspect of data processing—from ingestion and chunking to embedding and retrieval. This modular design works well with AgentCore's memory system, allowing me to build agents that process external data while maintaining searchable conversation histories.

## Setting Up the Development Environment

I'll start by navigating to the LlamaIndex project within our multi-framework repository:

cd
agentcore-multi-framework-examples/agentcore-llama-index
uv
sync
source
 .venv/bin/activate

Enter fullscreen mode

Exit fullscreen mode

The project uses several LlamaIndex packages for different capabilities:

llama
-
index
-
core

# Core agent and data framework

llama
-
index
-
llms
-
bedrock
-
converse

# Amazon Bedrock LLM integration

llama
-
index
-
embeddings
-
bedrock

# Bedrock embeddings for semantic search

llama
-
index
-
tools
-
wikipedia

# Wikipedia data source

llama
-
index
-
tools
-
requests

# Web request capabilities

bedrock
-
agentcore

# AgentCore SDK

bedrock
-
agentcore
-
starter
-
toolkit

# Deployment tools

Enter fullscreen mode

Exit fullscreen mode

## Understanding the LlamaIndex Agent Architecture

LlamaIndex recently introduced theFunctionAgent, a streamlined agent implementation that focuses on tool use and conversation flow. Unlike the earlier ReActAgent, FunctionAgent leverages the native function-calling capabilities of modern LLMs, resulting in more reliable and efficient agent behavior.

The architecture I've built combines three key LlamaIndex concepts:

### Global Settings Configuration

LlamaIndex uses aSettingsobject to configure global defaults for LLMs, embeddings, and processing parameters. This centralized configuration provides consistency across all components:

def

initialize_llamaindex_settings
():


"""
Initialize LlamaIndex global settings.
"""


# Configure LLM


llm

=

BedrockConverse
(


model
=
"
us.amazon.nova-pro-v1:0
"
,


)


# Configure embeddings


embed_model

=

BedrockEmbedding
(


model_name
=
"
amazon.titan-embed-text-v2:0
"
,


region_name
=
"
us-east-1
"


)


# Set global settings


Settings
.
llm

=

llm


Settings
.
embed_model

=

embed_model


Settings
.
chunk_size

=

512


Settings
.
chunk_overlap

=

50

Enter fullscreen mode

Exit fullscreen mode

TheBedrockConverseintegration uses the Amazon Bedrock Converse API, which provides a unified interface across different foundation models. This means I can easily switch between Claude, Llama, or Amazon Nova models without changing my agent code.

### Tool Integration

LlamaIndex tools follow a consistent interface through theFunctionToolabstraction. I've created a comprehensive tool suite that combines custom tools with pre-built integrations:

def

create_llamaindex_tools
(
memory_manager
=
None
)

->

List
[
FunctionTool
]:


"""
Create a list of tools for the LlamaIndex agent.
"""


tools

=

[]


# Basic function tools


tools
.
extend
([


FunctionTool
.
from_defaults
(


fn
=
calculator
,


name
=
"
calculator
"
,


description
=
"
Perform basic mathematical calculations
"


),


FunctionTool
.
from_defaults
(


fn
=
text_analyzer
,


name
=
"
text_analyzer
"
,


description
=
"
Analyze text and provide statistics
"


)


])


# Add external tools


wikipedia_spec

=

WikipediaToolSpec
()


wikipedia_tools

=

wikipedia_spec
.
to_tool_list
()


tools
.
extend
(
wikipedia_tools
)

Enter fullscreen mode

Exit fullscreen mode

TheToolSpecpattern allows entire tool suites to be packaged and shared. The Wikipedia and Requests tools come from LlamaHub, the LlamaIndex community tool repository, demonstrating how easy it is to extend agent capabilities.

### Memory-Enhanced Context

Integrating AgentCore Memory with LlamaIndex requires dynamically updating the agent's system prompt based on retrieved memories, rather than just appending memories to prompts:

# Enhance the user input with memory context if available

if

memory_manager
:


memory_context

=

memory_manager
.
get_memory_context
(


user_input
=
user_input
,


actor_id
=
actor_id
,


session_id
=
session_id


)


# Update agent's system prompt if enhanced


if

memory_context
:


enhanced_prompt

=

f
"
{
get_system_prompt
()
}
\n\n
Relevant context from previous interactions:
\n
{
memory_context
}
"


agent_instance
.
update_prompts
({
"
system_prompt
"
:

enhanced_prompt
})

Enter fullscreen mode

Exit fullscreen mode

## AgentCore Runtime Integration

The integration withAgentCore Runtimestarts with the entrypoint function that receives requests and returns responses. Let me explain how each component works:

### The Entrypoint Function

from

bedrock_agentcore

import

BedrockAgentCoreApp

from

bedrock_agentcore.runtime.context

import

RequestContext

app

=

BedrockAgentCoreApp
()

@app.entrypoint

async

def

invoke
(
payload
:

Dict
[
str
,

Any
],

context
:

Optional
[
RequestContext
]

=

None
)

->

str
:


"""
AgentCore entrypoint for LlamaIndex agent invocation.
"""

Enter fullscreen mode

Exit fullscreen mode

The@entrypoint decoratormarks this function as the handler that AgentCore Runtime invokes when your agent receives a request. The function receives two parameters:

* payload: A dictionary containing the request data, including the user's prompt
* context: ARequestContextobject that provides session information managed by AgentCore

### Processing Requests

# Extract parameters from the request

user_input

=

payload
.
get
(
"
prompt
"
,

"
Hello! What can you help me with?
"
)

actor_id

=

payload
.
get
(
"
actor_id
"
,

DEFAULT_ACTOR_ID
)

session_id

=

context
.
session_id

if

context

and

context
.
session_id

else

payload
.
get
(
"
session_id
"
,

DEFAULT_SESSION_ID
)

logger
.
info
(
f
"
Processing request for actor_id:
{
actor_id
}
, session_id:
{
session_id
}
"
)

Enter fullscreen mode

Exit fullscreen mode

The session_id from the RequestContext is particularly important—AgentCore Runtime automatically manages session isolation at iuinfrastructure level, giving each user their own isolated conversation space that persists across invocations.

### Memory Enhancement Before Processing

Before the agent processes the request, I retrieve relevant memories and add them to the prompt:

# Enhance prompt with AgentCore memory context

memory_context

=

memory_manager
.
get_memory_context
(


user_input
=
user_input
,


actor_id
=
actor_id
,


session_id
=
session_id

)

# Update agent's system prompt if enhanced

if

memory_context
:


enhanced_prompt

=

f
"
{
get_system_prompt
()
}
\n\n
Relevant context from previous interactions:
\n
{
memory_context
}
"


agent_instance
.
update_prompts
({
"
system_prompt
"
:

enhanced_prompt
})

Enter fullscreen mode

Exit fullscreen mode

Theget_memory_context()method performs two operations:

1. Retrieves conversation history using theget_last_k_turnsAPI
2. Searches for relevant memories using theRetrieveMemoriesoperation

This enriched context becomes part of the agent's system prompt, providing historical context for the response generation.

### Executing the Agent and Returning the Response

# Run the agent asynchronously

response

=

await

agent_instance
.
run
(
user_input
)

response_text

=

str
(
response
)

# Store conversation after generating response

if

memory_manager
:


memory_manager
.
store_conversation
(


user_input
=
user_input
,


response
=
response_text
,


actor_id
=
actor_id
,


session_id
=
session_id


)

# Return the text response

return

response_text

Enter fullscreen mode

Exit fullscreen mode

The function returns a string containing the agent's response. AgentCore Runtime takes this string and automatically:

* Wraps it in the appropriate HTTP response structure
* Handles response formatting for API Gateway
* Manages error responses if exceptions occur

Notice theasynckeyword—the FunctionAgent in LlamaIndex supports asynchronous execution natively. This allows the agent to make multiple tool calls or process large documents without blocking other requests. TheBedrockAgentCoreApphandles async functions transparently, whether running locally or deployed.

## AgentCore Memory Integration

The memory system in this implementation usesAgentCore Memoryto provide persistent context across sessions. Here's how it works:

### Memory Retrieval and Prompt Enrichment

The memory integration happens in two phases. First, when the agent starts processing a request, it retrieves relevant memories to enrich the input:

# Get memory context using the shared memory manager

memory_context

=

memory_manager
.
get_memory_context
(


user_input
=
user_input
,


actor_id
=
actor_id
,


session_id
=
session_id

)

Enter fullscreen mode

Exit fullscreen mode

Theget_memory_context()method performs these operations:

1. Load Conversation History: On the first invocation of a session, it calls theget_last_k_turnsAPI to retrieve up to 100 previous conversation turns:

conversations

=

self
.
memory_client
.
get_last_k_turns
(


memory_id
=
self
.
memory_config
.
memory_id
,


actor_id
=
actor_id
,


session_id
=
session_id
,


k
=
100

# Maximum conversation turns to retrieve

)

Enter fullscreen mode

Exit fullscreen mode

1. Retrieve Relevant Memories: It performs semantic search using theRetrieveMemoriesoperation to find relevant facts, preferences, and summaries:

memories

=

retrieve_memories_for_actor
(


memory_id
=
memory_manager
.
memory_config
.
memory_id
,


actor_id
=
actor_id
,


search_query
=
user_input
,


memory_client
=
memory_manager
.
memory_client

)

Enter fullscreen mode

Exit fullscreen mode

The namespace structure/actor/{actor_id}/provides complete isolation between users—each actor has their own memory space that other users cannot access.

### Storing Conversations After Response

After the agent generates a response, the conversation is stored in AgentCore Memory:

# Store conversation in AgentCore Memory

memory_manager
.
store_conversation
(


user_input
=
user_input
,


response
=
response_text
,


actor_id
=
actor_id
,


session_id
=
session_id

)

Enter fullscreen mode

Exit fullscreen mode

Thestore_conversation()method calls thecreate_eventAPI:

messages_to_store

=

[


(
user_input
,

'
USER
'
),


(
response_text
,

'
ASSISTANT
'
)

]

self
.
memory_client
.
create_event
(


memory_id
=
self
.
memory_config
.
memory_id
,


actor_id
=
actor_id
,


session_id
=
session_id
,


messages
=
messages_to_store

)

Enter fullscreen mode

Exit fullscreen mode

Whencreate_eventis called, AgentCore Memory automatically:

* Stores the raw conversation
* Extracts user preferences using the UserPreferences strategy
* Identifies semantic facts using the SemanticFacts strategy
* Generates session summaries using the SessionSummaries strategy

These extracted insights become available for future retrievals, building the agent's long-term knowledge.

### Memory as an Agentic Tool

I've also exposed memory retrieval as a tool that the agent can use strategically:

def

retrieve_memories
(
query
:

str
,

max_results
:

int

=

5
)

->

str
:


"""
Retrieve relevant memories based on a query.
"""


try
:


memories

=

retrieve_memories_for_actor
(


memory_id
=
memory_manager
.
memory_config
.
memory_id
,


actor_id
=
memory_manager
.
default_actor_id
,


search_query
=
query
,


memory_client
=
memory_manager
.
memory_client


)


if

not

memories
:


return

f
"
No relevant memories found for query:
'
{
query
}
'"


result

=

f
"
Retrieved
{
len
(
memories
)
}
 memories for
'
{
query
}
'
:
\n\n
"


for

i
,

memory

in

enumerate
(
memories
,

1
):


content

=

memory
.
get
(
'
content
'
,

'
No content
'
)


score

=

memory
.
get
(
'
score
'
,

'
N/A
'
)


result

+=

f
"
{
i
}
. (Score:
{
score
}
)
{
content
}
\n
"


return

result

Enter fullscreen mode

Exit fullscreen mode

Exposing memory retrieval as a tool gives the agent agency over its memory. Rather than automatically retrieving memories for every query, the agent can decide when memory context would be helpful. For instance, when asked about preferences, the agent might search for "user preferences" explicitly, or when solving a problem, it might search for similar problems from past conversations.

### Context Window Management

LlamaIndex's context management is important when dealing with large documents or extensive conversation histories. The memory manager handles this by implementing a sliding window approach:

conversations

=

self
.
memory_client
.
get_last_k_turns
(


memory_id
=
self
.
memory_config
.
memory_id
,


actor_id
=
actor_id
,


session_id
=
session_id
,


k
=
100

# Retrieve up to 100 previous conversation turns

)

Enter fullscreen mode

Exit fullscreen mode

Theget_last_k_turnsAPI efficiently retrieves recent conversation history without overwhelming the context window. This matters when using LlamaIndex with document-heavy workflows where context space is at a premium.

## Deploying the Agent

The deployment process leverages the AgentCore Starter Toolkit's streamlined workflow. First, I configure the agent:

agentcore configure
-n
 llamaindexagent
-e
 main.py

Enter fullscreen mode

Exit fullscreen mode

When prompted, I accept the default values. This creates the necessary AWS infrastructure including IAM roles, ECR repositories, and Lambda function configurations.

### Local Testing

Before deploying to the cloud, I always test locally to verify everything works correctly:

agentcore launch
--local

Enter fullscreen mode

Exit fullscreen mode

This starts a containerized version of the agent running on my local machine. The local environment exactly mirrors the production environment—same container, same runtime, same memory access.

Testing the local deployment:

agentcore invoke
--local

'{"prompt": "What did I say about fruit?"}'

Enter fullscreen mode

Exit fullscreen mode

The agent retrieves the sample memory we added during setup and responds appropriately. I can then test more complex scenarios:

agentcore invoke
--local

'{"prompt": "Search Wikipedia for information about apples and tell me if I would enjoy apple-based dishes"}'

Enter fullscreen mode

Exit fullscreen mode

This tests both the Wikipedia tool integration and memory retrieval, demonstrating how LlamaIndex agents can combine external data sources with personal context.

### Production Deployment

Once satisfied with local testing, deploying to AWS is straightforward:

agentcore launch

Enter fullscreen mode

Exit fullscreen mode

AgentCore handles all the complex deployment tasks automatically. It builds the container image, pushes it to Amazon ECR, creates the Lambda function with proper networking configuration, sets up API Gateway endpoints, configures IAM permissions with least privilege access, and enables comprehensive CloudWatch logging.

After deployment completes, I check the status:

agentcore status

Enter fullscreen mode

Exit fullscreen mode

This provides the endpoint ARN, CloudWatch log group, and other deployment details I need for monitoring and debugging.

## What's Next

This LlamaIndex implementation demonstrates how to build data-centric agents with RAG capabilities while maintaining production-grade memory persistence. The framework's modular architecture and extensive tool ecosystem make it ideal for agents that need to process diverse data sources while maintaining conversational context.

In the next article, I'll explore LangGraph, showing how to build stateful, graph-based agent workflows using the same AgentCore infrastructure. You'll see how LangGraph's unique approach to agent orchestration enables complex, multi-step reasoning while leveraging our shared memory architecture.

The complete code is available onGitHub. I encourage you to experiment with the implementation and explore how LlamaIndex's document processing capabilities can enhance your agent's knowledge base beyond just conversation memory.

Ready to build your own data-powered AI agent? Clone the repository and start exploring the possibilities!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
