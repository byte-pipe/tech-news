---
title: Building a Hands-Free AI Fitness Applet with Gemini Live API - DEV Community
url: https://dev.to/prema_ananda/building-a-hands-free-ai-fitness-applet-with-gemini-live-api-3fg1
site_name: devto
fetched_at: '2025-09-21T11:05:35.238793'
original_url: https://dev.to/prema_ananda/building-a-hands-free-ai-fitness-applet-with-gemini-live-api-3fg1
author: Prema Ananda
date: '2025-09-14'
description: This is a submission for the Google AI Studio Multimodal Challenge What I Built AI... Tagged with devchallenge, googleaichallenge, ai, gemini.
tags: '#devchallenge, #googleaichallenge, #ai, #gemini'
---

Google AI Challenge Submission

This is a submission for theGoogle AI Studio Multimodal Challenge

## What I Built

AI Personal Trainer is an experimental fitness app with a "voice-first" approach that turns your smartphone into an interactive workout partner. The app is primarily controlled by voice commands, allowing you to focus on exercises rather than the screen.

The problem I'm exploring:

* Distractions during workouts:The need to constantly interact with the phone screen
* Lack of personalization:Most apps offer one-size-fits-all solutions
* Passive interaction:Apps work as trackers rather than assistants

Implemented features:

* 🎤Voice program creation:Dialog with AI to create personalized workout programs
* 🧠Real-time audio interaction:Two-way voice communication during workouts
* 📊Comprehensive database system:System for storing programs, sessions, and progress
* 📈Analytics dashboard:Visual progress tracking and performance insights
* 📅Google Calendar integration:Automatic addition of workouts to calendar
* 🎯Hybrid architecture:Combining dialog speed with analysis accuracy

## Demo

⚡Live Applet

📱View in AI Studio

💻GitHub Repository:ai-personal-trainer

Thanks@aquascript-teamfor help with the video!

## How I Used Google AI Studio

Development started directly inGoogle AI Studio, where I experimented with different approaches to multimodal interaction.

### Development process:

1. Prototyping in Google AI Studio:Creating user interface and initial system setup
2. Export and development:Downloaded the project for local development
3. Extended development:UsedGemini CLIto integrate complex functions
4. Final deployment:Uploaded the finished project and usedDeploy App

### Two-model architecture:

#### Main model: Real-time dialog

// Connection to live audio dialog

sessionRef
.
current

=

await

clientRef
.
current
.
live
.
connect
({


model
:

'
gemini-2.5-flash-preview-native-audio-dialog
'
,


callbacks
:

{


onopen
:

()

=>

setConnectionStatus
(
'
connected
'
),


onmessage
:

async
(
message
)

=>

{


// Processing user speech


if
(
message
.
serverContent
?.
inputTranscription
)

{


const

userText

=

message
.
serverContent
.
inputTranscription
.
text
;


onTranscript
(
userText
);


}


// Playing AI response


const

audio

=

message
.
serverContent
?.
modelTurn
?.
parts
[
0
]?.
inlineData
;


if
(
audio

&&

outputAudioContextRef
.
current
)

{


await

playAudioResponse
(
audio
);


}


}


},


config
:

{


systemInstruction
:

createDynamicPrompt
(),


responseModalities
:

[
Modality
.
AUDIO
],


outputAudioTranscription
:

{},

// <--- Enable LLM transcription


inputAudioTranscription
:

{},

// <--- Enable user transcription


speechConfig
:

{


voiceConfig
:

{

prebuiltVoiceConfig
:

{

voiceName
:

'
Orus
'

}

}


}


}

});

Enter fullscreen mode

Exit fullscreen mode

#### Analytics model: Data extraction

// Precise interpretation of user commands

export

const

interpretWorkoutCommand

=

async
(
transcript
:

string
):

Promise
<
{

command
:

'
log_set
'

|

'
get_form_tip
'

|

'
chat_message
'
,

data
:

{

reps
?:

number
,

weight
?:

number
,

text
?:

string

}

|

null

}
>

=>

{


const

prompt

=

`You are an AI assistant interpreting voice commands from a user during a workout. The user's voice transcript is: "
${
transcript
}
".

 Your task is to analyze the transcript and classify it into one of the following commands, extracting relevant data.

 POSSIBLE COMMANDS:
 1. 'log_set': The user is reporting the completion of a set. They might mention repetitions (reps) and/or weight.
 - Keywords: "done", "finished", "log it", "reps", "weight", "kilos", numbers.
 - Example Transcripts: "Okay, 12 reps at 50 kilos", "I'm done", "8 reps", "log 90 pounds".
 2. 'get_form_tip': The user is asking for advice on their exercise form.
 - Keywords: "form", "technique", "how do I do this", "am I doing it right".
 - Example Transcripts: "check my form", "what's the technique for this".
 3. 'chat_message': The user is saying something else, likely a question or comment for the AI coach. This is the default if no other command fits.
 - Example Transcripts: "how many sets left", "I'm feeling tired", "what's the next exercise".

 Respond in JSON format with "command" and optional "data".
 - For 'log_set', 'data' should be an object with optional 'reps' and 'weight' numbers.
 - For 'get_form_tip', 'data' should be null.
 - For 'chat_message', 'data' should be an object with the original transcript as 'text'.

 Return ONLY the JSON object.

 Example Responses:
 - Transcript: "10 reps at 80 kg" -> { "command": "log_set", "data": { "reps": 10, "weight": 80 } }
 - Transcript: "how do I do this right?" -> { "command": "get_form_tip", "data": null }
 - Transcript: "what's the next exercise?" -> { "command": "chat_message", "data": { "text": "what's the next exercise?" } }
 `
;


try

{


const

result

=

await

ai
.
models
.
generateContent
({


model
:

"
gemini-2.5-flash
"
,


contents
:

prompt
,

...

Enter fullscreen mode

Exit fullscreen mode

## Multimodal Capabilities

### 1.Seamless audio interaction

Implemented:using client.live.connect fromGemini Live API SDKconnection with continuous bidirectional streamingUniqueness:Works like a phone conversation — you can interrupt and get instant responses

### 2.Hybrid command processing

Architecture:

* Dialog Model: Maintains natural conversation
* Analysis Model: Extracts precise data from speech

Processing example:

User: "Did eight reps with sixty kilos, felt pretty easy"

Dialog Model → "Great! Logged 8 reps with 60 kg. Should we increase the weight?"
Analysis Model →
 {
 "command": "log_set",
 "data": {
 "reps": 8,
 "weight": 60
 }
 }

Enter fullscreen mode

Exit fullscreen mode

### 3.Full-featured data system

Implemented architecture:

Workout programs(/programs/{programId}):

{


"name"
:

"Strength program, 12 weeks"
,


"createdBy"
:

"userId"
,


"workouts"
:

{


"day1"
:

{


"dayName"
:

"Chest and triceps"
,


"exercises"
:

[


{


"exerciseId"
:

"bench_press"
,


"name"
:

"Barbell bench press"
,


"sets"
:

[{
"reps"
:

8
,

"weight"
:

60
}],


"rest"
:

120


}


]


}


}

}

Enter fullscreen mode

Exit fullscreen mode

Detailed training sessions(/sessions/{sessionId}):

{


"userId"
:

"user123"
,


"date"
:

"2024-01-15T10:00:00Z"
,


"programId"
:

"strength_program_001"
,


"workoutId"
:

"day1_chest"
,


"duration"
:

5400
,

//

seconds


"voiceTranscript"
:

"Complete log of conversation with AI..."
,


"performedSets"
:

{


"set001"
:

{


"exerciseId"
:

"bench_press"
,


"setNumber"
:

1
,


"reps"
:

8
,


"weight"
:

62.5
,


"timestamp"
:

"2024-01-15T10:15:30Z"


}


}

}

Enter fullscreen mode

Exit fullscreen mode

### 4.Automatic calendar integration

Implemented:Direct integration with Google Calendar API

export

const

scheduleWorkouts

=

async
(
workouts
:

Workout
[],

accessToken
:

string
):

Promise
<
void
>

=>

{


if
(
!
workouts

||

workouts
.
length

===

0
)

{


throw

new

Error
(
"
No workouts to schedule.
"
);


}


const

schedulePromises

=

workouts
.
map
(
workout

=>

{


const

startTime

=

getNextWorkoutDate
(
workout
.
dayOfWeek
);


const

endTime

=

new

Date
(
startTime
.
getTime
()

+

60

*

60

*

1000
);

// Assume 1-hour duration


const

event

=

{


'
summary
'
:

`Workout:
${
workout
.
dayName
}
`
,


'
description
'
:

`Your scheduled workout session.\n\nExercises:\n-
${
workout
.
exercises
.
map
(
e

=>

e
.
name
).
join
(
'
\n
-
'
)}
`
,


'
start
'
:

{


'
dateTime
'
:

startTime
.
toISOString
(),


'
timeZone
'
:

Intl
.
DateTimeFormat
().
resolvedOptions
().
timeZone
,


},


'
end
'
:

{


'
dateTime
'
:

endTime
.
toISOString
(),


'
timeZone
'
:

Intl
.
DateTimeFormat
().
resolvedOptions
().
timeZone
,


},


};


return

fetch
(
'
https://www.googleapis.com/calendar/v3/calendars/primary/events
'
,

{


method
:

'
POST
'
,


headers
:

{


'
Authorization
'
:

`Bearer
${
accessToken
}
`
,


'
Content-Type
'
:

'
application/json
'
,


},


body
:

JSON
.
stringify
(
event
),


});


});


await

Promise
.
all
(
schedulePromises
);

};

Enter fullscreen mode

Exit fullscreen mode

### 5.Contextual understanding of fitness terminology

AI understands specific vocabulary:

* Recognition of data for set logging (log_set): AI searches user speech for numbers and keywords (such as "reps", "times", "weight", "pounds") to automatically fill in data about completed sets.
* Processing requests and comments (get_form_tip,chat_message): Phrases that don't contain direct data for logging are processed as trainer requests or simple comments.

### 6.Comprehensive Analytics Dashboard

Implemented:A dedicated analytics section that provides detailed insights into workout performance and progress tracking.

Features include:

* Visual progress charts and graphs
* Historical workout data visualization
* Performance metrics and trends analysis

## Current MVP Limitations

### Main challenges:

1. Speech recognition accuracy:AI doesn't always correctly interpret commands in live dialog, especially with background noise
2. Command execution:The model sometimes "forgets" to execute specific actions in the app after responding

## Why Multimodality Matters for Fitness

Traditional fitness apps force you to choose: EITHER data tracking OR workout focus. The multimodal approach solves this dilemma:

* Voice interfaceallows you to stay focused on exercises
* Intelligent speech analysisstructures data automatically
* Real-time feedbackcreates the feeling of a personal trainer
* Automatic workout schedulingintegrates fitness into daily life

The result is a fitness companion that understands natural speech and adapts to each user's unique style.

Note:Despite my AI trainer being quite smart and motivating, we strongly recommend maintaining common sense, especially when it comes to health matters. 💪

## Acknowledgments

I express deep gratitude to the organizers of theGoogle AI Studio Multimodal Challengefor the unique opportunity to experiment with cutting-edge artificial intelligence technologies.

Special thanks to:

* The Google AI Studio teamfor the intuitive platform that makes complex technologies accessible
* Gemini Live Audio API developersfor the revolutionary real-time voice interaction technology
* The Dev.to communityfor providing an inspiring platform for innovative projects

This project was made possible by an ecosystem of cutting-edge tools and the supportive developer community that Google AI creates.

MVP developed with React, TypeScript, Firebase, Google Calendar API and Google Gemini multimodal capabilities

Built with ❤️ by Premananda

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (33 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.
 Some comments have been hidden by the post's author -find out more

For further actions, you may consider blocking this person and/orreporting abuse
