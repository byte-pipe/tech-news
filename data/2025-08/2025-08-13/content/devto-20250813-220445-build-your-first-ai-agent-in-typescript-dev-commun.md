---
title: Build Your First AI Agent in TypeScript - DEV Community
url: https://dev.to/pmbanugo/build-your-first-ai-agent-in-typescript-hbo
site_name: devto
fetched_at: '2025-08-13T22:04:45.519202'
original_url: https://dev.to/pmbanugo/build-your-first-ai-agent-in-typescript-hbo
author: Peter Mbanugo
date: '2025-08-11'
description: Learn how to build your first AI agent in TypeScript. This tutorial guides you through creating a weather agent that can suggest activities based on weather and time. Tagged with ai, typescript, node, gemini.
tags: '#ai, #typescript, #node, #gemini'
---

Until recently, I assumed building AI agents was too complex. The complexity may vary from agent to agent, but they’re fairly simple to start with. The purpose of this post is to share my excitement on getting my “Hello World”-likeexperience running my own AI weather agent. I’ll show you how to create and run an agent that can tell the current time, weather, and suggest activities based on that.

## Prerequisite

You’re going to build your first agent using TypeScript and Node.js, so make sure you have those tools installed. Besides that, you need an API key to the LLM that will run your agent. I recommend Gemini because it’s easy to create an API key if you have a Google account, and there’s a free plan so you don’t have to worry about cost. To get an API key, go tohttps://aistudio.google.com/apikeyand click the "Create API Key"button at the top right. Follow the instructions in the dialog window that appears, then copy/save your API Key when it’s generated.

If you prefer to use Open AI or Claude models, refer to their documentation for how to create an API Key.

## Scaffolding The Project

You’re going to build the project using the Mastra SDK.Mastraprovides an SDK and framework for building AI apps in JavaScript/TypeScript. Run the commandnpx create-mastra@latest --project-name weather-ai --example --components tools,agents,workflows --llm googleto scaffold a new project with the nameweather-ai. The generated project will include a sample weather agent and tool.

Once the project is created, open the.envfile in it and add your Gemini API key as value forGOOGLE_GENERATIVE_AI_API_KEY.

Test that it works by running the commandnpm run devand open the Mastra playground available athttp://localhost:4111.

## Understanding the Project Structure

In just a few minutes you have an agent that can tell the current weather condition and recommend activities or outfit based on that data. How does this work behind the scenes?

Mastra framework convention splits the logic into three folders — agents, tools, and workflows. Theweather-agent.tsfile defines the weather agents you saw in the demo:

export

const

weatherAgent

=

new

Agent
({


name
:

"
Weather Agent
"
,


instructions
:

`
 You are a helpful weather assistant that provides accurate weather information and can help planning activities based on the weather.

 Your primary function is to help users get weather details for specific locations. When responding:
 - Always ask for a location if none is provided
 - If the location name isn't in English, please translate it
 - If giving a location with multiple parts (e.g. "New York, NY"), use the most relevant part (e.g. "New York")
 - Include relevant details like humidity, wind conditions, and precipitation
 - Keep responses concise but informative
 - If the user asks for activities and provides the weather forecast, suggest activities based on the weather forecast.
 - If the user asks for activities, respond in the format they request.

 Use the weatherTool to fetch current weather data.
`
,


model
:

google
(
"
gemini-2.5-flash
"
),


tools
:

{

weatherTool

},


memory
:

new

Memory
({


storage
:

new

LibSQLStore
({


url
:

"
file:../mastra.db
"
,

// path is relative to the .mastra/output directory


}),


}),

});

Enter fullscreen mode

Exit fullscreen mode

It exports anAgentobject which contains information about the model, tools, memory, and instruction. The instruction is the system prompt that tells the agent how to behave and it’s interesting to see the amount of details that go into such instructions. Before now, I didn’t understand what to do with system instructions when using Playgrounds like Google’s AI Studio or OpenAI GPT playground, and now that I do, I’m exploring different instructions to learn more how to control agent output and behaviour. If you’ve got more time, play around with the system instruction in this project, or in Google’sAI Studio.

Tools are functions that your model (or agent, not sure about the right terminology here 🙃) uses to retrieve information or perform actions (e.g. delete a file). TheweatherToolis used to retrieve weather information. Here’s a truncated version of what it should look like:

export

const

weatherTool

=

createTool
({


id
:

"
get-weather
"
,


description
:

"
Get current weather for a location
"
,


inputSchema
:

z
.
object
({


location
:

z
.
string
().
describe
(
"
City name
"
),


}),


outputSchema
:

z
.
object
({


temperature
:

z
.
number
(),


feelsLike
:

z
.
number
(),


humidity
:

z
.
number
(),


windSpeed
:

z
.
number
(),


windGust
:

z
.
number
(),


conditions
:

z
.
string
(),


location
:

z
.
string
(),


}),


execute
:

async
({

context

})

=>

{


return

await

getWeather
(
context
.
location
);


},

});

const

getWeather

=

async
(
location
:

string
)

=>

{


const

geocodingUrl

=

`https://geocoding-api.open-meteo.com/v1/search?name=
${
encodeURIComponent
(
location
)}
&count=1`
;


const

geocodingResponse

=

await

fetch
(
geocodingUrl
);


const

geocodingData

=

(
await

geocodingResponse
.
json
())

as

GeocodingResponse
;


if
(
!
geocodingData
.
results
?.[
0
])

{


throw

new

Error
(
`Location '
${
location
}
' not found`
);


}


const

{

latitude
,

longitude
,

name

}

=

geocodingData
.
results
[
0
];


const

weatherUrl

=

`https://api.open-meteo.com/v1/forecast?latitude=
${
latitude
}
&longitude=
${
longitude
}
&current=temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,wind_gusts_10m,weather_code`
;


const

response

=

await

fetch
(
weatherUrl
);


const

data

=

(
await

response
.
json
())

as

WeatherResponse
;


return

{


temperature
:

data
.
current
.
temperature_2m
,


feelsLike
:

data
.
current
.
apparent_temperature
,


humidity
:

data
.
current
.
relative_humidity_2m
,


windSpeed
:

data
.
current
.
wind_speed_10m
,


windGust
:

data
.
current
.
wind_gusts_10m
,


conditions
:

getWeatherCondition
(
data
.
current
.
weather_code
),


location
:

name
,


};

};

Enter fullscreen mode

Exit fullscreen mode

It uses thecreateTool()function from Mastra to define a tool with a name, input and and output schema, and a function to execute when the tool is called. It uses Zod to define the schema and I believe it supports JSON schema as well. When theweatherToolis called by the agent, thegetWeather()function is called with the given arguments and return the JSON.

## Give them tools, give them superpowers

Tools are the hands that allow an LLM's brain to interact with the world. The weather agent just knows the current weather; it can’t tell if it’s a good time for sunbathing or going to a nightclub. Let’s extend theweatherAgentwith atimeToolthat it can use to get the current time and recommend a suitable activity.

Create a new filetime-tool.tsin thesrc/mastra/toolsfolder and paste the code below in it:

import

{

createTool

}

from

"
@mastra/core/tools
"
;

import

{

z

}

from

"
zod
"
;

export

const

timeTool

=

createTool
({


id
:

"
get-current-time
"
,


description
:

"
Get the current time and date information
"
,


inputSchema
:

z
.
object
({


timezone
:

z


.
string
()


.
optional
()


.
describe
(


'
Timezone to format the time in (e.g., "America/New_York", "Europe/London"). Defaults to system timezone
'
,


),


}),


outputSchema
:

z
.
object
({


date
:

z
.
string
(),


time
:

z
.
string
(),


timestamp
:

z
.
number
(),


}),


execute
:

async
({

context

})

=>

{


return

getCurrentTime
(
context
.
timezone
);


},

});

const

getCurrentTime

=

(
timezone
?:

string
)

=>

{


const

now

=

new

Date
();


const

timestamp

=

now
.
getTime
();


// Use provided timezone or system default


const

targetTimezone

=


timezone

||

Intl
.
DateTimeFormat
().
resolvedOptions
().
timeZone
;


const

dateFormatter

=

new

Intl
.
DateTimeFormat
(
"
en-US
"
,

{


timeZone
:

targetTimezone
,


weekday
:

"
long
"
,


year
:

"
numeric
"
,


month
:

"
2-digit
"
,


day
:

"
2-digit
"
,


});


const

timeFormatter

=

new

Intl
.
DateTimeFormat
(
"
en-US
"
,

{


timeZone
:

targetTimezone
,


hour
:

"
2-digit
"
,


minute
:

"
2-digit
"
,


second
:

"
2-digit
"
,


hour12
:

false
,


});


const

date

=

dateFormatter
.
format
(
now
);


const

time

=

timeFormatter
.
format
(
now
);


return

{


date
,


time
,


timestamp
,


};

};

Enter fullscreen mode

Exit fullscreen mode

Now that you have the tool, add it to the agent’s tools list. First import the module:

import

{

timeTool

}

from

"
../tools/time-tool
"
;

Enter fullscreen mode

Exit fullscreen mode

Then update theweatherAgent

export

const

weatherAgent

=

new

Agent
({


//... rest of the code


model
:

google
(
"
gemini-2.5-flash
"
),


tools
:

{

weatherTool
,

timeTool

},


//.... rest of the code

});

Enter fullscreen mode

Exit fullscreen mode

Finally, update the system instruction to get the current time. Add the following prompt to theinstructionfield:

 - If the user asks for activities, use the timeTool to get the current time based on the location's timezone and suggest activities accordingly.

Enter fullscreen mode

Exit fullscreen mode

Your dev server should still be running. If not, restart it and open the playground to try it out.

## That’s A Wrap

In this post, you've seen how quick and simple it is to build an AI agent. You started with a weather agent and extended it with a tool to get the current time, making it smarter with activity suggestions. This is just the beginning. You can add more tools to give your agent more capabilities, like searching the web or interacting with other APIs. The possibilities are endless. I hope this has sparked your interest in building AI agents, just like it did for me.

I'm curious to see what you build with these models/tools! I'll keep sharing what I learn along the way.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
