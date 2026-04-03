---
title: 'GitHub - QwenLM/Qwen-Agent: Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc. · GitHub'
url: https://github.com/QwenLM/Qwen-Agent
site_name: github
content_file: github-github-qwenlmqwen-agent-agent-framework-and-applic
fetched_at: '2026-03-06T11:12:23.287449'
original_url: https://github.com/QwenLM/Qwen-Agent
author: QwenLM
description: Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc. - QwenLM/Qwen-Agent
---

QwenLM

 

/

Qwen-Agent

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star14.3k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

304 Commits
304 Commits
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
benchmark
benchmark
 
 
browser_qwen
browser_qwen
 
 
examples
examples
 
 
qwen-agent-docs/
website
qwen-agent-docs/
website
 
 
qwen_agent
qwen_agent
 
 
qwen_server
qwen_server
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
README_CN.md
README_CN.md
 
 
browser_qwen.md
browser_qwen.md
 
 
browser_qwen_cn.md
browser_qwen_cn.md
 
 
run_server.py
run_server.py
 
 
setup.py
setup.py
 
 
View all files

## Repository files navigation

中文｜ English

💜Qwen Chat|   🤗Hugging Face|   🤖ModelScope|    📑Blog｜   📖Documentation📊Benchmark|   💬WeChat (微信)|   🫨Discord

Qwen-Agent is a framework for developing LLM applications based on the instruction following, tool usage, planning, and
memory capabilities of Qwen.
It also comes with example applications such as Browser Assistant, Code Interpreter, and Custom Assistant.
Now Qwen-Agent plays as the backend ofQwen Chat.

# News

* 🔥🔥🔥Feb 16, 2026: Open-sourced Qwen3.5. For usage examples, refer toQwen3.5 Agent Demo.
* Jan 27, 2026: Open-sourced agent evaluation benchmarkDeepPlanningand added Qwen-Agentdocumentation.
* Sep 23, 2025: AddedQwen3-VL Tool-call Demo, supporting tools such as zoom in, image search, and web search.
* Jul 23, 2025: AddQwen3-Coder Tool-call Demo; Added native API tool call interface support, such as using vLLM's built-in tool call parsing.
* May 1, 2025: AddQwen3 Tool-call Demo, and addMCP Cookbooks.
* Mar 18, 2025: Support for thereasoning_contentfield; adjust the defaultFunction Call template, which is applicable to the Qwen2.5 series general models and QwQ-32B. If you need to use the old version of the template, please refer to theexamplefor passing parameters.
* Mar 7, 2025: AddedQwQ-32B Tool-call Demo. It supports parallel, multi-step, and multi-turn tool calls.
* Dec 3, 2024: Upgrade GUI to Gradio 5 based. Note: GUI requires Python 3.10 or higher.
* Sep 18, 2024: AddedQwen2.5-Math Demoto showcase the Tool-Integrated Reasoning capabilities of Qwen2.5-Math. Note: The python executor is not sandboxed and is intended for local testing only, not for production use.

# Getting Started

## Installation

* Install the stable version from PyPI:

pip install -U 
"
qwen-agent[gui,rag,code_interpreter,mcp]
"

#
 Or use `pip install -U qwen-agent` for the minimal requirements.

#
 The optional requirements, specified in double brackets, are:

#
 [gui] for Gradio-based GUI support;

#
 [rag] for RAG support;

#
 [code_interpreter] for Code Interpreter support;

#
 [mcp] for MCP support.

* Alternatively, you can install the latest development version from the source:

git clone https://github.com/QwenLM/Qwen-Agent.git

cd
 Qwen-Agent
pip install -e ./
"
[gui,rag,code_interpreter,mcp]
"

#
 Or `pip install -e ./` for minimal requirements.

## Preparation: Model Service

You can either use the model service provided by Alibaba
Cloud'sDashScope, or deploy and use your own
model service using the open-source Qwen models.

* If you choose to use the model service offered by DashScope, please ensure that you set the environment
variableDASHSCOPE_API_KEYto your unique DashScope API key.
* Alternatively, if you prefer to deploy and use your own model service, please follow the instructions provided in the README of Qwen2 for deploying an OpenAI-compatible API service.
Specifically, consult thevLLMsection for high-throughput GPU deployment or theOllamasection for local CPU (+GPU) deployment.
For the QwQ and Qwen3 model, it is recommended todo notadd the--enable-auto-tool-choiceand--tool-call-parser hermesparameters, as Qwen-Agent will parse the tool outputs from vLLM on its own.
For Qwen3-Coder, it is recommended to enable both of the above parameters, use vLLM's built-in tool parsing, and combine with theuse_raw_apiparameterusage.

## Developing Your Own Agent

Qwen-Agent offers atomic components, such as LLMs (which inherit fromclass BaseChatModeland come withfunction calling) and Tools (which inherit
fromclass BaseTool), along with high-level components like Agents (derived fromclass Agent).

The following example illustrates the process of creating an agent capable of reading PDF files and utilizing tools, as
well as incorporating a custom tool:

import
 
pprint

import
 
urllib
.
parse

import
 
json5

from
 
qwen_agent
.
agents
 
import
 
Assistant

from
 
qwen_agent
.
tools
.
base
 
import
 
BaseTool
, 
register_tool

from
 
qwen_agent
.
utils
.
output_beautify
 
import
 
typewriter_print

# Step 1 (Optional): Add a custom tool named `my_image_gen`.

@
register_tool
(
'my_image_gen'
)

class
 
MyImageGen
(
BaseTool
):
 
# The `description` tells the agent the functionality of this tool.

 
description
 
=
 
'AI painting (image generation) service, input text description, and return the image URL drawn based on text information.'

 
# The `parameters` tell the agent what input parameters the tool has.

 
parameters
 
=
 [{
 
'name'
: 
'prompt'
,
 
'type'
: 
'string'
,
 
'description'
: 
'Detailed description of the desired image content, in English'
,
 
'required'
: 
True

 }]

 
def
 
call
(
self
, 
params
: 
str
, 
**
kwargs
) 
->
 
str
:
 
# `params` are the arguments generated by the LLM agent.

 
prompt
 
=
 
json5
.
loads
(
params
)[
'prompt'
]
 
prompt
 
=
 
urllib
.
parse
.
quote
(
prompt
)
 
return
 
json5
.
dumps
(
 {
'image_url'
: 
f'https://image.pollinations.ai/prompt/
{
prompt
}
'
},
 
ensure_ascii
=
False
)

# Step 2: Configure the LLM you are using.

llm_cfg
 
=
 {
 
# Use the model service provided by DashScope:

 
'model'
: 
'qwen-max-latest'
,
 
'model_type'
: 
'qwen_dashscope'
,
 
# 'api_key': 'YOUR_DASHSCOPE_API_KEY',

 
# It will use the `DASHSCOPE_API_KEY' environment variable if 'api_key' is not set here.

 
# Use a model service compatible with the OpenAI API, such as vLLM or Ollama:

 
# 'model': 'Qwen2.5-7B-Instruct',

 
# 'model_server': 'http://localhost:8000/v1', # base_url, also known as api_base

 
# 'api_key': 'EMPTY',

 
# (Optional) LLM hyperparameters for generation:

 
'generate_cfg'
: {
 
'top_p'
: 
0.8

 }
}

# Step 3: Create an agent. Here we use the `Assistant` agent as an example, which is capable of using tools and reading files.

system_instruction
 
=
 
'''After receiving the user's request, you should:

- first draw an image and obtain the image url,

- then run code `request.get(image_url)` to download the image,

- and finally select an image operation from the given document to process the image.

Please show the image using `plt.show()`.'''

tools
 
=
 [
'my_image_gen'
, 
'code_interpreter'
] 
# `code_interpreter` is a built-in tool for executing code. For configuration details, please refer to the FAQ.

files
 
=
 [
'./examples/resource/doc.pdf'
] 
# Give the bot a PDF file to read.

bot
 
=
 
Assistant
(
llm
=
llm_cfg
,
 
system_message
=
system_instruction
,
 
function_list
=
tools
,
 
files
=
files
)

# Step 4: Run the agent as a chatbot.

messages
 
=
 [] 
# This stores the chat history.

while
 
True
:
 
# For example, enter the query "draw a dog and rotate it 90 degrees".

 
query
 
=
 
input
(
'
\n
user query: '
)
 
# Append the user query to the chat history.

 
messages
.
append
({
'role'
: 
'user'
, 
'content'
: 
query
})
 
response
 
=
 []
 
response_plain_text
 
=
 
''

 
print
(
'bot response:'
)
 
for
 
response
 
in
 
bot
.
run
(
messages
=
messages
):
 
# Streaming output.

 
response_plain_text
 
=
 
typewriter_print
(
response
, 
response_plain_text
)
 
# Append the bot responses to the chat history.

 
messages
.
extend
(
response
)

In addition to using built-in agent implementations such asclass Assistant, you can also develop your own agent implemetation by inheriting fromclass Agent.

The framework also provides a convenient GUI interface, supporting the rapid deployment of Gradio Demos for Agents.
For example, in the case above, you can quickly launch a Gradio Demo using the following code:

from
 
qwen_agent
.
gui
 
import
 
WebUI

WebUI
(
bot
).
run
() 
# bot is the agent defined in the above code, we do not repeat the definition here for saving space.

Now you can chat with the Agent in the web UI. Please refer to theexamplesdirectory for more usage examples.

# FAQ

## How to Use the Code Interpreter Tool?

We implement a code interpreter tool based on local Docker containers. You can enable the built-incode interpretertool for your agent, allowing it to autonomously write code according to specific scenarios, execute it securely within an isolated sandbox environment, and return the execution results.

⚠️Note: Before using this tool, please ensure that Docker is installed and running on your local operating system. The time required to build the container image for the first time depends on your network conditions. For Docker installation and setup instructions, please refer to theofficial documentation.

## How to Use MCP?

You can select the required tools on the open-sourceMCP server websiteand configure the relevant environment.

Example of MCP invocation format:

{
 "mcpServers": {
 "memory": {
 "command": "npx",
 "args": ["-y", "@modelcontextprotocol/server-memory"]
 },
 "filesystem": {
 "command": "npx",
 "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
 },
 "sqlite" : {
 "command": "uvx",
 "args": [
 "mcp-server-sqlite",
 "--db-path",
 "test.db"
 ]
 }
 }
}

For more details, you can refer to theMCP usage example

The dependencies required to run this example are as follows:

# Node.js (Download and install the latest version from the Node.js official website)
# uv 0.4.18 or higher (Check with uv --version)
# Git (Check with git --version)
# SQLite (Check with sqlite3 --version)

# For macOS users, you can install these components using Homebrew:
brew install uv git sqlite3

# For Windows users, you can install these components using winget:
winget install --id=astral-sh.uv -e
winget install git.git sqlite.sqlite

## Do you have function calling (aka tool calling)?

Yes. The LLM classes providefunction calling. Additionally, some Agent classes also are built upon the function calling capability, e.g., FnCallAgent and ReActChat.

The current default tool calling template natively supportsParallel Function Calls.

## How to pass LLM parameters to the Agent?

llm_cfg
 
=
 {
 
# The model name being used:

 
'model'
: 
'qwen3-32b'
,
 
# The model service being used:

 
'model_type'
: 
'qwen_dashscope'
,
 
# If 'api_key' is not set here, it will default to reading the `DASHSCOPE_API_KEY` environment variable:

 
'api_key'
: 
'YOUR_DASHSCOPE_API_KEY'
,

 
# Using an OpenAI API compatible model service, such as vLLM or Ollama:

 
# 'model': 'qwen3-32b',

 
# 'model_server': 'http://localhost:8000/v1', # base_url, also known as api_base

 
# 'api_key': 'EMPTY',

 
# (Optional) LLM hyperparameters:

 
'generate_cfg'
: {
 
# This parameter will affect the tool-call parsing logic. Default is False:

 
# Set to True: when content is `<think>this is the thought</think>this is the answer`

 
# Set to False: when response consists of reasoning_content and content

 
# 'thought_in_content': True,

 
# tool-call template: default is nous (recommended for qwen3):

 
# 'fncall_prompt_type': 'nous'

 
# Maximum input length, messages will be truncated if they exceed this length, please adjust according to model API:

 
# 'max_input_tokens': 58000

 
# Parameters that will be passed directly to the model API, such as top_p, enable_thinking, etc., according to the API specifications:

 
# 'top_p': 0.8

 
# Using the API's native tool call interface

 
# 'use_raw_api': True,

 }
}

## How to do question-answering over super-long documents involving 1M tokens?

We have releaseda fast RAG solution, as well asan expensive but competitive agent, for doing question-answering over super-long documents. They have managed to outperform native long-context models on two challenging benchmarks while being more efficient, and perform perfectly in the single-needle "needle-in-the-haystack" pressure test involving 1M-token contexts. See theblogfor technical details.

# Application: BrowserQwen

BrowserQwen is a browser assistant built upon Qwen-Agent. Please refer to itsdocumentationfor details.

# Disclaimer

The Docker container-based code interpreter mounts only the specified working directory and implements basic sandbox isolation, but it should still be used with caution in production environments.

## About

Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

pypi.org/project/qwen-agent/

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

14.3k

 stars
 

### Watchers

95

 watching
 

### Forks

1.4k

 forks
 

 Report repository

 

## Releases25

v0.0.26

 Latest

 

May 29, 2025

 

+ 24 releases

## Used by141

 + 133
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python91.4%
* TypeScript3.1%
* Shell2.4%
* CSS1.1%
* JavaScript1.1%
* MDX0.7%
* Other0.2%