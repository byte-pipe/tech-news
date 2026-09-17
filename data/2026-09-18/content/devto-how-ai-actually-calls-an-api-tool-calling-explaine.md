---
title: How AI Actually Calls an API? Tool Calling Explained from Scratch - DEV Community
url: https://dev.to/aws/how-ai-actually-calls-an-api-tool-calling-explained-from-scratch-4lf8
site_name: devto
content_file: devto-how-ai-actually-calls-an-api-tool-calling-explaine
fetched_at: '2026-09-18T05:27:50.283577'
original_url: https://dev.to/aws/how-ai-actually-calls-an-api-tool-calling-explained-from-scratch-4lf8
author: Rohini Gaonkar
date: '2026-09-16'
description: In the previous post, we taught a model to read our documents. It could search a pile of files and... Tagged with ai, mcp, aws, tutorial.
tags: '#ai, #mcp, #aws, #tutorial'
---

Clarifies models only request tools not run them

In theprevious post, we taught a model to read our documents. It could search a pile of files and answer from them, which was very useful.

But I still couldn't ask it if it was going to rain, check a live price or even what today's date is.

Because as we discussed this earlier, a foundation model on its own is frozen in time. Its knowledge stops at its training cutoff and it's locked in a box. No window to the outside world.

This post is about that window, tool calling. We give the model one tool and watch it reach out for live data, add a second tool, then get into the two very different ways an app can hand a model a fact it doesn't have. One of those two is the reason one of the AI assistant you've used can tell you today's date.

All the code is inmy GitHub repo, in theep07-tool-callingfolder. Three tiny scripts, one idea each: one tool, two tools, and the injection trick.

## Model runs a tool?

When I first heard "the model calls a tool," I pictured the model reaching out and running code by itself.

That is not what happens.

The model does not run anything because it really can't. It is still just reading a prompt and producing text.

What it produces is a structured request that says "I'd like to call this tool, with these inputs."

It just hands you a note, that your code reads and then runs the actual tool. It then hands the result back to the model for further actions, either to tell you the answer or call another tool.

The model is the decision-maker. Your code is the hands.

## The four-step loop

This is run every single time:

1. You send the model your question, plus a description of the tools it's allowed to use.
2. The model decides: can I answer this myself, or do I need a tool? If it needs one, it replies with a structured request. A little package that sayscall get_weather, city is Toronto.
3. Your code sees that request and runs the real function, the one that actually hits the weather API.
4. You send the result back to the model. Now it writes the final answer, grounded in real data it could never have known on its own.

## Setup: describing a tool

I'm usingAmazon Bedrockagain, same as the whole series, calling a Claude Model through the Converse API. Converse has a spot built in for tools, calledtoolConfig.

response
 
=
 
bedrock
.
converse
(

 
modelId
=
MODEL
,

 
messages
=
messages
,

 
toolConfig
=
{
"
tools
"
:
 
[
WEATHER_TOOL
]},

 
inferenceConfig
=
{
"
maxTokens
"
:
 
2048
},

 
additionalModelRequestFields
=
THINKING
,

)

Enter fullscreen mode

Exit fullscreen mode

Let's take the simplest tool to start: get the weather.

Describing a tool to the model is three parts: a name, a plain-English description, and an input schema for the arguments.

WEATHER_TOOL
 
=
 
{

 
"
toolSpec
"
:
 
{

 
"
name
"
:
 
"
get_weather
"
,

 
"
description
"
:
 
"
Get the current weather for a single city.
"
,

 
"
inputSchema
"
:
 
{

 
"
json
"
:
 
{

 
"
type
"
:
 
"
object
"
,

 
"
properties
"
:
 
{

 
"
city
"
:
 
{

 
"
type
"
:
 
"
string
"
,

 
"
description
"
:
 
"
A plain city name, e.g. Toronto or Paris.
"
,

 
}

 
},

 
"
required
"
:
 
[
"
city
"
],

 
}

 
},

 
}

}

Enter fullscreen mode

Exit fullscreen mode

This description and schema are the only things the model reads to decide when and how to use this tool.

Your tool description is a prompt, so treat it like one.

And separately, the real function that does the work:

import
 
requests

# Open-Meteo returns a numeric weather_code; map the ones we need to plain words.

WEATHER_CODES
 
=
 
{
0
:
 
"
clear sky
"
,
 
2
:
 
"
partly cloudy
"
,
 
3
:
 
"
overcast
"
,
 
61
:
 
"
light rain
"
,
 
63
:
 
"
moderate rain
"
}

def
 
get_weather
(
city
:
 
str
)
 
->
 
dict
:

 
geo
 
=
 
requests
.
get
(

 
"
https://geocoding-api.open-meteo.com/v1/search
"
,

 
params
=
{
"
name
"
:
 
city
,
 
"
count
"
:
 
1
},

 
).
json
()[
"
results
"
][
0
]

 
now
 
=
 
requests
.
get
(

 
"
https://api.open-meteo.com/v1/forecast
"
,

 
params
=
{

 
"
latitude
"
:
 
geo
[
"
latitude
"
],

 
"
longitude
"
:
 
geo
[
"
longitude
"
],

 
"
current
"
:
 
"
temperature_2m,weather_code,wind_speed_10m
"
,

 
},

 
).
json
()[
"
current
"
]

 
return
 
{

 
"
city
"
:
 
geo
[
"
name
"
],

 
"
country
"
:
 
geo
[
"
country
"
],

 
"
temperature_c
"
:
 
now
[
"
temperature_2m
"
],

 
"
conditions
"
:
 
WEATHER_CODES
.
get
(
now
[
"
weather_code
"
],
 
"
unknown
"
),

 
"
wind_kph
"
:
 
now
[
"
wind_speed_10m
"
],

 
}

Enter fullscreen mode

Exit fullscreen mode

This is normal code. No AI in it. It hitsOpen-Meteo, a free weather API with no key required.

## Demo: the model calls the tool

Question:"Do I need an umbrella in Toronto today?"

I send that to the model along with theget_weatherdefinition.

The model stops with astopReasonoftool_useand hands back a request:

{

 
"toolUse"
:
 
{

 
"toolUseId"
:
 
"tooluse_abc123"
,

 
"name"
:
 
"get_weather"
,

 
"input"
:
 
{
 
"city"
:
 
"Toronto"
 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

I never told it which tool to use, and I never told it the argument. It read one question and worked out both. But nothing has run yet.

So my code runsget_weather("Toronto"), hits the API, and gets back the real conditions. Then I package that up and send it back to the model as atoolResult:

messages
.
append
({

 
"
role
"
:
 
"
user
"
,

 
"
content
"
:
 
[{

 
"
toolResult
"
:
 
{

 
"
toolUseId
"
:
 
"
tooluse_abc123
"
,

 
"
content
"
:
 
[{
"
json
"
:
 
{

 
"
city
"
:
 
"
Toronto
"
,

 
"
country
"
:
 
"
Canada
"
,

 
"
temperature_c
"
:
 
23.8
,

 
"
conditions
"
:
 
"
overcast
"
,

 
"
wind_kph
"
:
 
3.9
,

 
}}],

 
}

 
}],

})

Enter fullscreen mode

Exit fullscreen mode

With a single tool, the whole thing is a straight line. Send, get the request, run it, send the result back, get the answer. Top to bottom, no loop:

messages
 
=
 
[{
"
role
"
:
 
"
user
"
,
 
"
content
"
:
 
[{
"
text
"
:
 
QUESTION
}]}]

# 1. Send the question + the tool.

response
 
=
 
bedrock
.
converse
(

 
modelId
=
MODEL
,

 
messages
=
messages
,

 
toolConfig
=
{
"
tools
"
:
 
[
WEATHER_TOOL
]},

)

messages
.
append
(
response
[
"
output
"
][
"
message
"
])

# 2. The model asks for the tool. 3. Run it. 4. Send the result back.

tool_request
 
=
 
next
(

 
b
[
"
toolUse
"
]
 
for
 
b
 
in
 
response
[
"
output
"
][
"
message
"
][
"
content
"
]
 
if
 
"
toolUse
"
 
in
 
b

)

result
 
=
 
get_weather
(
tool_request
[
"
input
"
][
"
city
"
])

messages
.
append
({

 
"
role
"
:
 
"
user
"
,

 
"
content
"
:
 
[{

 
"
toolResult
"
:
 
{

 
"
toolUseId
"
:
 
tool_request
[
"
toolUseId
"
],

 
"
content
"
:
 
[{
"
json
"
:
 
result
}],

 
}

 
}],

})

# The model writes the final answer, grounded in the real data.

final
 
=
 
bedrock
.
converse
(
modelId
=
MODEL
,
 
messages
=
messages
,
 
toolConfig
=
{
"
tools
"
:
 
[
WEATHER_TOOL
]})

Enter fullscreen mode

Exit fullscreen mode

One tool, one round trip. I know exactly what's going to happen, so I can just write it out.

With real data in hand, the model writes the answer:"Based on the current weather in Toronto, **you probably don't need an umbrella right now."

That answer did not exist anywhere in the model. It went from frozen to current in one tool call.

## Give it a second tool

Now something that feels like it should be trivial.

Question:"What's today's date?"

No tool call comes back. The model just says, plainly, that it doesn't have access to the current date.

The only tool it has access to is weather, so nothing here can reach a date. It can't answer, and this is the part I love, it doesn't pretend to. It just tells me it doesn't know, which is a real shift fromthe hallucinations post.

If the problem is "there's no tool for the date," the fix is obvious, lets give it one.

DATETIME_TOOL
 
=
 
{

 
"
toolSpec
"
:
 
{

 
"
name
"
:
 
"
get_current_datetime
"
,

 
"
description
"
:
 
"
Get the current date and time.
"
,

 
"
inputSchema
"
:
 
{
"
json
"
:
 
{
"
type
"
:
 
"
object
"
,
 
"
properties
"
:
 
{}}},

 
}

}

def
 
get_current_datetime
()
 
->
 
dict
:

 
from
 
datetime
 
import
 
datetime

 
now
 
=
 
datetime
.
now
()

 
return
 
{

 
"
date
"
:
 
now
.
strftime
(
"
%Y-%m-%d
"
),

 
"
day_of_week
"
:
 
now
.
strftime
(
"
%A
"
),

 
"
time
"
:
 
now
.
strftime
(
"
%H:%M
"
),

 
}

Enter fullscreen mode

Exit fullscreen mode

No arguments, no AI, it just returns today's date and time. I add it to the list of tools the model is allowed to use. Now the model has two tools - weather and date.

Question:"Do I need an umbrella in Toronto? And what is today's date?"

Two requests come back, for two tools.get_weatherwith{"city": "Toronto"}, thenget_current_datetimewith{}. My code runs each one, hands both results back, and the model writes one answer using both.

One sentence, two different needs, right tool for each. It just routed it.

## What changed? We now need a LOOP

But notice the problem with my nice straight line from before. With one tool, I knew there'd be exactly one round trip. With two, I don't know which the model will pick, or how many, or whether it'll come back for more after seeing the first result. So the four steps go inside a loop. Keep going while the model keeps asking for tools, and stop when it writes the answer instead:

# name → the real function to run when the model asks for it.

TOOLS
 
=
 
{

 
"
get_weather
"
:
 
get_weather
,

 
"
get_current_datetime
"
:
 
get_current_datetime
,

}

messages
 
=
 
[{
"
role
"
:
 
"
user
"
,
 
"
content
"
:
 
[{
"
text
"
:
 
QUESTION
}]}]

while
 
True
:

 
response
 
=
 
bedrock
.
converse
(

 
modelId
=
MODEL
,

 
messages
=
messages
,

 
toolConfig
=
{
"
tools
"
:
 
[
WEATHER_TOOL
,
 
DATETIME_TOOL
]},

 
)

 
assistant_message
 
=
 
response
[
"
output
"
][
"
message
"
]

 
messages
.
append
(
assistant_message
)

 
# Done? The model stopped asking for tools and wrote its answer.

 
if
 
response
[
"
stopReason
"
]
 
!=
 
"
tool_use
"
:

 
answer
 
=
 
""
.
join
(
b
[
"
text
"
]
 
for
 
b
 
in
 
assistant_message
[
"
content
"
]
 
if
 
"
text
"
 
in
 
b
)

 
break

 
# Otherwise: run every tool the model requested, send the results back.

 
tool_results
 
=
 
[]

 
for
 
block
 
in
 
assistant_message
[
"
content
"
]:

 
if
 
"
toolUse
"
 
not
 
in
 
block
:

 
continue

 
request
 
=
 
block
[
"
toolUse
"
]

 
result
 
=
 
TOOLS
[
request
[
"
name
"
]](
**
request
[
"
input
"
])

 
tool_results
.
append
({

 
"
toolResult
"
:
 
{

 
"
toolUseId
"
:
 
request
[
"
toolUseId
"
],

 
"
content
"
:
 
[{
"
json
"
:
 
result
}],

 
}

 
})

 
messages
.
append
({
"
role
"
:
 
"
user
"
,
 
"
content
"
:
 
tool_results
})

Enter fullscreen mode

Exit fullscreen mode

Thatwhileloop is the whole difference. One tool was a straight line I could hardcode. More than one, and I hand the control to the model and let it drive until it's done.

This is so so so important to understand, because this is a seed of an agent!

## So how does AI Assistants know the date?

This is the part that bugged me while I was learning. If a raw model doesn't know today's date, how does ChatGPT or Claude or any AI assistant know it? You ask what day it is and they answer instantly. Are they calling a date tool every time? Short answer, no.

Anthropic actually publishes the system prompt they use for Claude, in theirrelease notes. They say Claude's web interface and mobile apps use asystem promptto provide up-to-date information, such as the current date, at thestart of every conversation.

That's it. No tool runs. It's just text thats slipped into the instructions before your message ever gets there. The model was handed the date as context.

You can do the exact same thing in a script. Take away the date tool and paste today's date into the system prompt as plain text:

system_prompt
 
=
 
[{

 
"
text
"
:
 
f
"
Today
'
s date is 
{
datetime
.
now
()
:
%
A
,
 
%
d
 
%
B
 
%
Y
}
.
"

}]

Enter fullscreen mode

Exit fullscreen mode

Ask "what's today's date?" and it answers, correctly, with no tool call at all. Because you handed it the date.

### Tool or inject? The clean rule

So there are two ways to give a model a fact it doesn't have. A tool it calls and you run, or context you inject straight into the prompt. When do you use which?

* Cheap and static, like today's date? Inject it.One line. No tool needed.
* Live and always changing, like the weather? Use a tool.You can't inject weather, you'd have to know it in advance, which defeats the point. A tool goes and fetches it, fresh, when the model asks.

And remember that schema,cityand nothing else? That's why I can't ask this thing about next week. There's no date to pass in. If I wanted a forecast, that's a different tool.

## The hardcoding problem, and MCP

So we've got two tools working. Weather and date. Great. But real systems don't have just two tools. They have dozens - check the calendar, search the CRM, query the database, send the email and/or read the file.

And with what we just built, every one of those is something I hand-wire myself - write the schema, write the function, register it, keep the description in sync when the tool changes.

For two tools, that's fine. Fifty tools, across five apps, all changing over time? That's a maintenance nightmare. And everyone building AI apps was writing the same glue code, over and over, for the same tools.

This is the problem MCP solves. MCP stands forModel Context Protocol. It's an open standard, started by Anthropic and now used across the industry, for how AI apps and tools talk to each other.

The clean way to think about it: MCP is like USB-C for AI tools. Before USB-C, every device had its own cable and connector. It was a chaos of cables. USB-C is one standard plug. MCP is that, but for connecting models to tools and data.

The tool lives behind an MCP server, and that server describes itself: here are the tools I offer, here's what each does, here are the inputs I need. Your app is the MCP client. It just asks "what have you got?" and the server tells it. The tools get discovered at runtime.

So if someone builds an MCP server for GitHub, or your database, or Slack, you don't write the integration. You point your app at the server and the tools show up.

We're not building one today, that's a whole topic on its own. The mental model is enough for now: tool calling is how one model uses a tool, and MCP is how any model discovers and uses tools.

## Key takeaways

If you're just getting started:Tool calling is how AI stops being a closed box. Give it tools and it can pull live information and take action instead of just talking. The one thing to hold onto: the model is the brain, your code is the hands.

If you're more on the builder side:The model picks the tool and fills in the arguments, and the only thing it reads to make that call is your description and schema. So write them like prompts, and be specific about what the tool does and doesn't do. Then: static facts get injected, live facts get a tool. And once you're past a couple of tools, stop hardcoding and look at MCP.

## What's next

Today the model called one tool, or two, once each, then answered. But what happens when a question needs several tools, in the right order? Check my calendar, then check the weather for that day, then draft the email. The model has to plan, act, look at the result, and decide the next step. Over and over in a loop, until it's done.

Well, that loop is actually called an agent. And next post, we build one withStrands Agents SDK.

Ride along.

This post is part of the "Learning AI Out Loud" series, a cloud architect learning AI from first principles.

Follow along with the series

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse