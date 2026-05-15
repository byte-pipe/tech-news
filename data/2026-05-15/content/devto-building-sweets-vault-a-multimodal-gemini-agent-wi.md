---
title: Building "Sweets Vault" - a multimodal Gemini Agent with physical hardware integration - DEV Community
url: https://dev.to/googleai/building-sweets-vault-a-multimodal-gemini-agent-with-physical-hardware-integration-1nmh
site_name: devto
content_file: devto-building-sweets-vault-a-multimodal-gemini-agent-wi
fetched_at: '2026-05-15T19:34:00.739552'
original_url: https://dev.to/googleai/building-sweets-vault-a-multimodal-gemini-agent-with-physical-hardware-integration-1nmh
author: Remigiusz Samborski
date: '2026-05-15'
description: Motivating seven-year-olds to complete their daily reading and handwriting practice is a classic... Tagged with ai, gemini, agents.
tags: '#ai, #gemini, #agents'
---

Motivating seven-year-olds to complete their daily reading and handwriting practice is a classic parenting challenge. Traditional rewards work for a while, but they lack interactivity and require constant manual verification.

As a developer, I like to solve such challenges with automation. After putting some thought into it, I came up with theSweets Vaultidea: an interactive agent powered byGoogle's Agent Development Kit (ADK)and theGemini API. The system acts as a cheerful guardian that talks to children, visually inspects their workbooks via uploaded images, tests their reading comprehension, and triggers a hardware lock to open a drawer full of sweets upon successful completion.

In this guide, I will walk you through the architecture and implementation of this solution. You will learn how to:

* Structure a multimodal agentusing the Agent Development Kit (ADK).
* Implement visual and verbal verificationusing Gemini's multimodal capabilities.
* Manage stateacross multiple conversation turns and tools.
* Connect agent tool calls to physical hardwareinterfaces.
* Develop and run locallyto access the physical hardware.

If you’d like to jump directly to the code visit theGitHub repository. All the code is available there for your exploration.

### System architecture overview

The diagram below presents the high level architecture of the solution:

The core components include:

1. Gemini API: Handles reasoning, multimodal homework validation and tool calls.
2. ADK Agent & Tools: Encapsulates the system instructions, state management, and callable Python functions.
3. Hardware Interface: Translates tool execution into physical actions (unlocking specific drawer IDs).

The system is designed in such a way that the Agent runs on a local machine (I am using a mini PC with Ubuntu installed) to allow for direct hardware access:

* Magnetic drawers controlled viaFT232HUSB to GPIO converter
* LED Matrix controlled via REST API running on aRaspberry Pi

Initially, I planned to control the LED Matrix using a second FT232H controller, but due to lack of library support, I ended up using an intermediary Raspberry Pi. This approach has its benefits, for example the LED Matrix can be located anywhere at home within the Wifi range 😀

### Root agent logic

To kick-start the agent development, I leveraged theagent-starter-packtemplates. It provides a production-ready foundation with FastAPI, frontend UI integration, and built-in observability.

The heart of the Sweets Vault is located inagent/app/agent.py. I start by configuring the environment and initializingGemini Enterprise Agent Platform(former Vertex AI). I also define the specific tasks required for our users (Mary and James):

load_dotenv
()

project_id
 
=
 
os
.
getenv
(
"
GOOGLE_CLOUD_PROJECT
"
)

location
 
=
 
os
.
getenv
(
"
GOOGLE_CLOUD_LOCATION
"
,
 
"
us-central1
"
)

os
.
environ
[
"
GOOGLE_CLOUD_PROJECT
"
]
 
=
 
project_id

os
.
environ
[
"
GOOGLE_CLOUD_LOCATION
"
]
 
=
 
location

os
.
environ
[
"
GOOGLE_GENAI_USE_VERTEXAI
"
]
 
=
 
"
True
"

# Initialize Vertex AI

vertexai
.
init
(
project
=
project_id
,
 
location
=
location
)

Enter fullscreen mode

Exit fullscreen mode

As a native Polish speaker I want to have the ability for the Agent to work both in Polish (for the sake of my kids) and English (for demo purposes). This is handled by the AGENT_LANGUAGE variable:

AGENT_LANGUAGE
 
=
 
os
.
getenv
(
"
AGENT_LANGUAGE
"
,
 
"
en
"
)

Enter fullscreen mode

Exit fullscreen mode

The actual agent (root_agent) is created at the bottom of the same file:

root_agent
 
=
 
Agent
(

 
name
=
"
root_agent
"
,

 
model
=
Gemini
(

 
model
=
"
gemini-2.5-flash
"
,

 
retry_options
=
types
.
HttpRetryOptions
(
attempts
=
3
),

 
),

 
instruction
=
load_prompt_from_file
(
f
"
sweet-vault-agent-
{
AGENT_LANGUAGE
}
.txt
"
),

 
tools
=
[
get_progress
,
 
complete_task
,
 
unlock_drawer
],

)

Enter fullscreen mode

Exit fullscreen mode

Note:The prompt is language specific and pulled from a file with a language suffix (en or pl).

### Handling state

A common failure mode in conversational AI is lost context or hallucinated task completion. To prevent this, we implement strict state management usingToolContext.

Instead of relying on the model's memory, the agent reads and writes explicit completion flags to itssession state:

def
 
_get_task_status
(
user_key
:
 
str
,
 
task_id
:
 
str
,
 
tool_context
:
 
ToolContext
)
 
->
 
bool
:

 
"""
Retrieves the completion status for a specific task from the flat state.
"""

 
state_key
 
=
 
f
"
user_tasks_
{
user_key
}
_
{
task_id
}
"

 
return
 
tool_context
.
state
.
get
(
state_key
,
 
False
)

def
 
_set_task_status
(
user_key
:
 
str
,
 
task_id
:
 
str
,
 
is_done
:
 
bool
,
 
tool_context
:
 
ToolContext
):

 
"""
Saves the completion status for a specific task and ensures all user/task 
 combinations are explicitly represented in the flat tool_context.state.
 
"""

 
# First, update the specific target task in the current tool state

 
target_key
 
=
 
f
"
user_tasks_
{
user_key
}
_
{
task_id
}
"

 
tool_context
.
state
[
target_key
]
 
=
 
is_done

 
# Now, ensure every possible combination for all known users exists in the flat state.

 
all_sync_updates
 
=
 
{}

 
for
 
name
 
in
 
user_names
:

 
u_key
 
=
 
name
.
lower
()

 
for
 
t_id
 
in
 
TASKS_CONFIG
:

 
key
 
=
 
f
"
user_tasks_
{
u_key
}
_
{
t_id
}
"

 
# If the key isn't already in the current state, default it to False.

 
# Otherwise, keep its existing value.

 
all_sync_updates
[
key
]
 
=
 
tool_context
.
state
.
get
(
key
,
 
False
)

 
# Apply all values back to the flat state

 
tool_context
.
state
.
update
(
all_sync_updates
)

 
logging
.
info
(
f
"
Synchronized all task state values. Updated 
{
target_key
}
 to 
{
is_done
}
"
)

Enter fullscreen mode

Exit fullscreen mode

Key learning:When building the system I tried using session state elements as anested dictionary, but unfortunately at the time of writing this is not supported. The workaround was to use a flat structure with keys including both theuser_keyandtask_id, which works well for my use case. However, this pattern might not scale well for a complex system with many users and tasks, in which case serialization or an external DB could be a better option.

### Agent tools

I provided the agent with three specific tools: checking progress, marking tasks complete, and unlocking the drawer.

#### Checking progress

Theget_progressfunction retrieves and formats a checklist of a specific user's tasks, indicating whether each task is marked as completed or pending based on the application's current session state.

def
 
get_progress
(
user_name
:
 
str
,
 
tool_context
:
 
ToolContext
)
 
->
 
str
:

 
"""
Check the progress of tasks for a specific user.
"""

 
user_key
 
=
 
user_name
.
lower
()

 
status_msg
 
=
 
f
"
Progress for 
{
user_name
}
:
\n
"

 
for
 
task_id
,
 
desc
 
in
 
TASKS_CONFIG
.
items
():

 
is_done
 
=
 
_get_task_status
(
user_key
,
 
task_id
,
 
tool_context
)

 
state_str
 
=
 
"
✅ DONE
"
 
if
 
is_done
 
else
 
"
❌ PENDING
"

 
status_msg
 
+=
 
f
"
- [
{
task_id
}
] 
{
desc
}
: 
{
state_str
}
\n
"

 
return
 
status_msg

Enter fullscreen mode

Exit fullscreen mode

#### Marking task as complete

Thecomplete_tasktool acts as a gatekeeper. It checks if all tasks are finished before informing the model that it is authorized to unlock the drawer:

def
 
complete_task
(
user_name
:
 
str
,
 
task_id
:
 
str
,
 
tool_context
:
 
ToolContext
)
 
->
 
str
:

 
"""
Mark a task as completed for a user.
"""

 
user_key
 
=
 
user_name
.
lower
()

 
# Mark task as complete

 
if
 
task_id
 
in
 
TASKS_CONFIG
:

 
_set_task_status
(
user_key
,
 
task_id
,
 
True
,
 
tool_context
)

 
else
:

 
return
 
f
"
Error: Task ID 
'
{
task_id
}
'
 not found.
"

 
# Check if ALL tasks are complete

 
all_complete
 
=
 
True

 
remaining
 
=
 
[]

 
for
 
t_id
 
in
 
TASKS_CONFIG
:

 
if
 
not
 
_get_task_status
(
user_key
,
 
t_id
,
 
tool_context
):

 
all_complete
 
=
 
False

 
remaining
.
append
(
t_id
)

 
if
 
all_complete
:

 
return 
(

 
f
"
SUCCESS: All tasks completed for 
{
user_name
}
! 
"

 
"
You may now unlock the drawer.
"

 
)

 
# If not all complete, show progress

 
return 
(

 
f
"
Task 
{
task_id
}
 marked as DONE. 
"

 
f
"
Remaining tasks: 
{
'
, 
'
.
join
(
remaining
)
}
.
"

 
)

Enter fullscreen mode

Exit fullscreen mode

Notice how descriptive the returned values are. They are written this way intentionally to give the Agent enough information to handle communication with the user, provide feedback and motivate them to complete the remaining tasks.

#### Integrating physical hardware

When the model receives the success confirmation, it calls theunlock_drawertool. This interfaces directly with our hardware relay logic to update the LED display and pop open the assigned drawer:

# Initialize the HW interface and lock the drawers

user_names
 
=
 
[
"
Maria
"
,
 
"
Jan
"
]
 
if
 
AGENT_LANGUAGE
 
==
 
"
pl
"
 
else
 
[
"
Mary
"
,
 
"
James
"
]

hw_interface
 
=
 
HardwareInterface
(
user_names
)

def
 
unlock_drawer
(
id
:
 
int
,
 
user_name
:
 
str
)
 
->
 
str
:

 
"""
Unlock a drawer by its ID.
"""

 
if
 
id
 
in
 
[
0
,
 
1
]:

 
hw_interface
.
unlock_drawer
(
id
)

 
return
 
f
"
Drawer 
{
id
}
 unlocked for 
{
user_name
}
"

 
return
 
"
Drawer not found
"

Enter fullscreen mode

Exit fullscreen mode

TheHardwareInterface(defined inagent/app/app_utils/hw_interface.py) actively communicates with theLED Matrix APIon the Raspberry Pi to display whether each drawer is currently locked or unlocked.

While the code to control the physical drawer magnets is fully functional and tested (located indrawers.py), it is not yet integrated into the mainHardwareInterface. This integration is simply on hold until the magnets are physically mounted to the drawer box.

### Agent prompts

Tools alone are not enough; the model requires precise instructions onhowto verify the work. Inagent/app/promptsI defined a strict multi-step verification protocol both in English and Polish. Here is the English prompt:

You are a friendly, cheerful, and helpful AI assistant, the guardian of the "Sweets Vault." Your task is to verify tasks performed by children in order to grant a sweet reward.

### MAIN RULES:
1. **LANGUAGE**: You speak ONLY AND EXCLUSIVELY IN ENGLISH.
2. **USERS**:
 - **Mary** (girl, 7 years old) -> Assigned drawer ID: **0**
 - **James** (boy, 7 years old) -> Assigned drawer ID: **1**
 - **Parent** (man, 42 years old) -> May test the system by saying, for example, "I'm pretending to be Mary." Treat him exactly like the child he is claiming to be.
3. **PERSONALITY**: You are enthusiastic, warm, and supportive. Use exclamation marks and a joyful tone.

### TASK VERIFICATION PROCESS:
1. **STATE IDENTIFICATION**: When a child starts a conversation, ALWAYS first use the `get_progress(user_name)` tool to check what needs to be done.
2. **REPORTING**: The child reports completing a task (A or B).
3. **VERIFICATION**: Conduct a rigorous verification (camera/questions) as described below.
4. **CREDITING**: If verification is successful, use the `complete_task(user_name, task_id)` tool.
 - Read the tool's response carefully!
 - ONLY IF the response is "SUCCESS: All tasks completed...", then use `unlock_drawer`.
 - If the response shows "Remaining tasks," inform the child what they still need to do.

**Task A: Reading a page of a book**
* **Verification 1**: Ask the child to show the read page to the camera. Confirm that you see it. Don't expose any details that can help answer the question in the next step (i.e. avoid sharing details of what exactly you can see).
* **Verification 2**: Ask a simple follow-up question about the read text. The child must answer it.
* **Task ID**: "A"

**Task B: Calligraphy (writing letters in workbooks)**
* **Verification 1**: Ask to show the completed page in the workbooks to the camera. 
* **Verification 2**: Confirm that the task has been performed. Make sure the picture contains hand-written letters (usually with a pencil).
* If the page only contains examples, ask the child to complete missing parts.
* **Task ID**: "B"

### SUCCESS AND REWARD:
IF the `complete_task` tool returns "SUCCESS", run `unlock_drawer(id)`.
Then **CELEBRATE!** Use phrases like: "Yippee!", "Hurray!", "Bravo!", "You're a champion!", "The sweets are yours!". Make some "noise."

### FAILURE:
If verification fails (e.g., the child doesn't show the page or answers incorrectly), gently and encouragingly ask for improvement or a retry. Do not open the drawer.

Enter fullscreen mode

Exit fullscreen mode

This prompt structure ensures the agent does its due diligence, preventing kids from simply holding up a blank page or skipping the reading comprehension check.

### Demo

You can see a demonstration of the working system in the video below:

### Conclusion

By combining the Gemini API, the Agent Development Kit, and a simple hardware relay, you can build highly interactive, physically grounded AI Agents. The Sweets Vault demonstrates how multimodal verification and structured tool calling solve practical, real-world problems with a dose of fun.

Explore more at:

* Sweets Vault code repository
* Agent Development Kit (ADK)
* Gemini Enterprise Agent Platform

### Future plans

Current implementation usesGemini Flashwhich guarantees high performance, multimodality and tool calling capabilities. Nevertheless it requires text input and provides only text as output. In the near future I plan to experiment withGemini Live APIwhich enables voice, video and text as input and conversational audio as output.

I am also going to finish the physical locks part with electro magnets. Stay tuned for updates.

### Thanks for reading

Thank you for reading. I hope this blog inspires you to bring your own creative AI and hardware projects to life. If you found this article helpful, please consider following me here and giving it a clap 👏 to help others discover it.

I am always eager to connect with fellow developers and AI enthusiasts, so feel free to follow me onLinkedIn,XorBluesky. Your feedback is incredibly valuable, so please do not hesitate to leave a comment with your thoughts, questions, or your own experiences building multimodal agents!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse