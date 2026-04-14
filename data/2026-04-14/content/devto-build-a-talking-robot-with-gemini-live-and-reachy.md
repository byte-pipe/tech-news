---
title: Build a Talking Robot with Gemini Live and Reachy Mini - DEV Community
url: https://dev.to/googleai/build-a-talking-robot-with-gemini-live-and-reachy-mini-20e2
site_name: devto
content_file: devto-build-a-talking-robot-with-gemini-live-and-reachy
fetched_at: '2026-04-14T11:57:19.966399'
original_url: https://dev.to/googleai/build-a-talking-robot-with-gemini-live-and-reachy-mini-20e2
author: Thor 雷神 Schaeff
date: '2026-04-13'
description: Imagine a tiny desk robot that listens to you, answers back in real time, dances on command, tracks... Tagged with ai, robotics, gemini, opensource.
tags: '#ai, #robotics, #gemini, #opensource'
---

Imagine a tiny desk robot that listens to you, answers back in real time, dances on command, tracks your face, and cracks the occasional dad joke — all powered by the Gemini Live API.

That's exactly what theReachy Mini Conversation Appdoes. It's an open-source Python application that connectsPollen Robotics' Reachy Minito a real-time voice LLM so the robot can hold full-duplex audio conversations while expressing itself through head movements, antenna wiggles, dances, and emotions.

In this tutorial you'll learn:

1. How the architecture works— from microphone to motor.
2. How to set it upon your own machine.
3. How to give the robot a custom personalitywithout touching a single line of Python.

Let's dive in.

## Architecture at a glance

The app is split into four cooperating layers:

┌─────────────┐
│ Your voice │ Microphone audio (16-bit PCM, 16 kHz)
└──────┬──────┘
 ▼
┌─────────────────────────────────────┐
│ fastrtc (low-latency WebRTC I/O) │
│ ─ streams audio to/from the LLM │
│ ─ resamples between sample rates │
└──────┬──────────────────┬───────────┘
 │ │
 ▼ ▼
┌──────────────┐ ┌──────────────────┐
│ Gemini Live │ │ OpenAI Realtime │ (pick one via MODEL_NAME)
│ Handler │ │ Handler │
└──────┬───────┘ └──────┬───────────┘
 │ │
 ▼ ▼
┌─────────────────────────────────────┐
│ Tool dispatch layer │
│ ─ dance, play_emotion, camera, │
│ move_head, head_tracking, ... │
└──────┬──────────────────────────────┘
 ▼
┌─────────────────────────────────────┐
│ MovementManager (60 Hz loop) │
│ ─ sequential primary moves │
│ ─ additive secondary offsets │
│ (speech wobble + face tracking) │
│ ─ idle breathing │
└──────┬──────────────────────────────┘
 ▼
┌─────────────┐
│ Reachy Mini │ Robot hardware / simulator
└─────────────┘

Enter fullscreen mode

Exit fullscreen mode

### The audio loop

The heart of the app is anAsyncStreamHandler(from thefastrtclibrary). The default backend isGemini Live(GeminiLiveHandleringemini_live.py), which uses the Google GenAI SDK for bidirectional audio streaming viasession.send_realtime_input().

An alternativeOpenAI Realtimebackend (OpenaiRealtimeHandlerinopenai_realtime.py) is also available if you prefer WebSocket-based streaming through OpenAI's API. You switch between them by setting theMODEL_NAMEenvironment variable — the rest of the app doesn't know or care which backend is active.

Here's the condensed flow inside the Gemini handler:

# 1. Microphone → Gemini

async
 
def
 
receive
(
self
,
 
frame
):

 
pcm_bytes
 
=
 
audio_to_int16
(
frame
).
tobytes
()

 
await
 
self
.
session
.
send_realtime_input
(

 
audio
=
types
.
Blob
(
data
=
pcm_bytes
,
 
mime_type
=
"
audio/pcm;rate=16000
"
)

 
)

# 2. Gemini → Speaker

async
 
def
 
_run_live_session
(
self
):

 
async
 
with
 
client
.
aio
.
live
.
connect
(
model
=
...,
 
config
=
...)
 
as
 
session
:

 
async
 
for
 
response
 
in
 
session
.
receive
():

 
if
 
response
.
server_content
 
and
 
response
.
server_content
.
model_turn
:

 
for
 
part
 
in
 
response
.
server_content
.
model_turn
.
parts
:

 
audio_array
 
=
 
np
.
frombuffer
(
part
.
inline_data
.
data
,
 
dtype
=
np
.
int16
)

 
await
 
self
.
output_queue
.
put
((
24000
,
 
audio_array
))

 
if
 
response
.
tool_call
:

 
await
 
self
.
_handle_tool_call
(
response
)

Enter fullscreen mode

Exit fullscreen mode

Audio in at 16 kHz, audio out at 24 kHz, with transcriptions and tool calls flowing through the same session.

### Tool calling

When the LLM decides the robot shoulddosomething — dance, look around, show an emotion — it emits afunction call. The app converts these between OpenAI and Gemini formats automatically, then dispatches them through aBackgroundToolManagerso the audio stream is never blocked:

LLM says: "dance(name='macarena')"
 → BackgroundToolManager starts a task
 → Task calls MovementManager.queue_move(MacarenaMove)
 → Result sent back to the LLM so it can narrate what happened

Enter fullscreen mode

Exit fullscreen mode

Built-in tools include:

Tool

What it does

dance

Queue a dance from the open 
dances library

play_emotion

Play a recorded emotion clip (happy, sad, surprised, …)

move_head

Tilt the head left/right/up/down

camera

Capture a frame and send it to the LLM for visual understanding

head_tracking

Toggle face tracking on or off

do_nothing

Explicitly stay idle (the LLM uses this when it decides not to act)

### The movement system

TheMovementManagerruns a60 Hz control loopin a dedicated thread. It blends two types of motion:

* Primary moves(dances, emotions, goto poses) run sequentially from a queue. Only one plays at a time.
* Secondary offsets(speech-reactive wobble, face tracking) are additive — they layer on top of whatever primary move is playing.

When nothing is happening, the robot automatically starts a gentlebreathing animation— a subtle up-and-down sway with antenna movement — so it always looks alive.

### Continuous video streaming

When a camera is connected, the Gemini handler runs a1 FPS video loopthat continuously sends JPEG frames to the model:

async
 
def
 
_video_sender_loop
(
self
):

 
while
 
not
 
self
.
_stop_event
.
is_set
():

 
frame
 
=
 
self
.
deps
.
camera_worker
.
get_latest_frame
()

 
_
,
 
buffer
 
=
 
cv2
.
imencode
(
"
.jpg
"
,
 
frame
,
 
[
cv2
.
IMWRITE_JPEG_QUALITY
,
 
70
])

 
await
 
self
.
session
.
send_realtime_input
(

 
video
=
types
.
Blob
(
data
=
buffer
.
tobytes
(),
 
mime_type
=
"
image/jpeg
"
)

 
)

 
await
 
asyncio
.
sleep
(
1.0
)

Enter fullscreen mode

Exit fullscreen mode

This gives the robot passive visual context — it can comment on what it sees without you having to ask it to look.

## Prerequisites

Before you start, make sure you have:

* Python 3.10+installed
* AReachy Mini robot(physical or simulated via theReachy Mini SDK)
* AGemini API keyfromAI Studio
* A workingmicrophone and speakers

No robot?You can still explore the code and run in simulation mode — the SDK includes a MuJoCo simulator and a desktop mockup.

## Step 1: Clone and install

The project usesuvfor fast dependency management (pip works too).

# Clone the repo

git clone https://github.com/pollen-robotics/reachy_mini_conversation_app.git

cd 
reachy_mini_conversation_app

# Create a virtual environment (macOS example)

uv venv 
--python
 python3.12 .venv

source
 .venv/bin/activate

# Install dependencies

uv 
sync

Enter fullscreen mode

Exit fullscreen mode

### Optional extras

Want face tracking, local vision, or YOLO? Install the matching extra:

uv 
sync
 
--extra
 mediapipe_vision 
# Lightweight head tracking

uv 
sync
 
--extra
 yolo_vision 
# YOLO-based face detection

uv 
sync
 
--extra
 local_vision 
# On-device VLM (SmolVLM2, GPU recommended)

uv 
sync
 
--extra
 all_vision 
# Everything

Enter fullscreen mode

Exit fullscreen mode

## Step 2: Configure your environment

cp
 .env.example .env

Enter fullscreen mode

Exit fullscreen mode

Open.envand fill in:

# Your Gemini API key — that's all you need to get started
GEMINI_API_KEY=your-gemini-api-key-here

Enter fullscreen mode

Exit fullscreen mode

That's the minimum — the app defaults to Gemini Live. The full list of options:

Variable

Description

GEMINI_API_KEY

Your Gemini key. Also accepts 
GOOGLE_API_KEY
.

MODEL_NAME

Defaults to 
gemini-3.1-flash-live-preview
. Set to 
gpt-realtime
 to use OpenAI Realtime instead.

OPENAI_API_KEY

Only needed if you switch to the OpenAI backend.

REACHY_MINI_CUSTOM_PROFILE

Name of a personality profile to load (see below).

## Step 3: Start the Reachy Mini daemon

The conversation app talks to the robot through the Reachy Mini SDK daemon. The daemon is installed as part of theReachy Mini SDKsetup —notinside the conversation app's.venv.

Open aseparate terminaland activate the SDK's virtual environment:

# Navigate to wherever you cloned/installed the Reachy Mini SDK

cd 
path/to/reachy_mini

source 
reachy_mini_env/bin/activate

Enter fullscreen mode

Exit fullscreen mode

Then start the daemon (keep this terminal running):

# Physical robot — auto-detects USB connection

reachy-mini-daemon

# Or simulation mode

reachy-mini-daemon 
--simulation

Enter fullscreen mode

Exit fullscreen mode

Important:The daemon must stay running in its own terminal for the entire session. Switch back to your conversation app terminal (with.venvactivated) for the next step.

If you see aTimeoutErrorwhen launching the conversation app, the daemon isn't running.

## Step 4: Launch the conversation app

In your terminal from Step 1 (with the conversation app's virtual environment activated), run:

reachy-mini-conversation-app

Enter fullscreen mode

Exit fullscreen mode

That's it! The robot will start breathing gently, and you can start talking. It runs inconsole modeby default — your terminal becomes the interface.

### Web UI mode

Want a visual interface with live transcripts and a chatbot panel? Add--gradio:

reachy-mini-conversation-app 
--gradio

Enter fullscreen mode

Exit fullscreen mode

This launches a Gradio app athttp://127.0.0.1:7860where you can see the conversation, switch personalities, and view camera frames.

### More CLI options

# With MediaPipe head tracking

reachy-mini-conversation-app 
--head-tracker
 mediapipe

# Audio-only (no camera)

reachy-mini-conversation-app 
--no-camera

# Verbose logging

reachy-mini-conversation-app 
--debug

# Connect to a specific robot on the network

reachy-mini-conversation-app 
--robot-name
 my-reachy

Enter fullscreen mode

Exit fullscreen mode

## Customizing the robot's personality

This is where it gets fun. The app uses aprofile system— plain text files that control who the robot thinks it is.

### Profile structure

profiles/
├── default/
│ ├── instructions.txt 
# System prompt

│ └── tools.txt 
# Which tools are enabled

├── mars_rover/
│ ├── instructions.txt
│ └── tools.txt
├── noir_detective/
│ ├── instructions.txt
│ └── tools.txt
└── ...

Enter fullscreen mode

Exit fullscreen mode

### Creating your own personality

1. Create a folder underprofiles/:

mkdir 
profiles/pirate_captain

Enter fullscreen mode

Exit fullscreen mode

1. Write aninstructions.txt:

## IDENTITY
You are Captain Byte, a swashbuckling robot pirate who speaks in nautical
metaphors and ends every sentence with "Arrr" or a pirate-themed quip.

## RESPONSE RULES
Keep responses to 1-2 sentences. Be helpful first, pirate second.
Always refer to the user as "matey" or "landlubber".

Enter fullscreen mode

Exit fullscreen mode

1. Create atools.txtlisting which tools the robot can use:

dance
play_emotion
move_head
camera
head_tracking

Enter fullscreen mode

Exit fullscreen mode

1. Activate it:

# In your .env file
REACHY_MINI_CUSTOM_PROFILE="pirate_captain"

Enter fullscreen mode

Exit fullscreen mode

Or switch live from the Gradio UI's "Personality" panel — no restart needed.

### Reusable prompt fragments

The profile system supportscomposable prompts. Instead of duplicating text, reference shared fragments:

# instructions.txt
[identities/witty_identity]
[passion_for_lobster_jokes]
You love to dance and will look for any excuse to bust a move.

Enter fullscreen mode

Exit fullscreen mode

Each[placeholder]pulls fromsrc/reachy_mini_conversation_app/prompts/. This keeps profiles DRY and lets you mix and match personality traits.

### Custom tools

You can even addprofile-specific toolsby dropping a Python file in the profile folder. For example, the built-inexampleprofile includes asweep_look.pytool that makes the robot slowly scan the room:

# profiles/example/sweep_look.py

from
 
reachy_mini_conversation_app.tools.core_tools
 
import
 
Tool

class
 
SweepLookTool
(
Tool
):

 
name
 
=
 
"
sweep_look
"

 
description
 
=
 
"
Slowly look around the room in a sweeping motion.
"

 
async
 
def
 
run
(
self
,
 
args
,
 
deps
):

 
# Queue a sequence of head movements...

 
return
 
{
"
status
"
:
 
"
done
"
,
 
"
description
"
:
 
"
Finished looking around
"
}

Enter fullscreen mode

Exit fullscreen mode

Enable it intools.txt:

dance
play_emotion
sweep_look # Your custom tool

Enter fullscreen mode

Exit fullscreen mode

## How the Gemini Live session works under the hood

Let's trace a full conversation turn to see all the pieces fit together.

### 1. Session setup

When the app starts, it builds aLiveConnectConfigwith:

* The system prompt (from the active profile)
* A voice selection (Gemini supports: Aoede, Charon, Fenrir,Kore(default), Leda, Orus, Puck, Zephyr)
* Function declarations for every enabled tool
* Input and output audio transcription enabled

live_config
 
=
 
types
.
LiveConnectConfig
(

 
response_modalities
=
[
types
.
Modality
.
AUDIO
],

 
system_instruction
=
types
.
Content
(
parts
=
[
types
.
Part
(
text
=
instructions
)]),

 
speech_config
=
types
.
SpeechConfig
(

 
voice_config
=
types
.
VoiceConfig
(

 
prebuilt_voice_config
=
types
.
PrebuiltVoiceConfig
(
voice_name
=
"
Kore
"
),

 
),

 
),

 
tools
=
[{
"
function_declarations
"
:
 
declarations
}],

 
input_audio_transcription
=
types
.
AudioTranscriptionConfig
(),

 
output_audio_transcription
=
types
.
AudioTranscriptionConfig
(),

)

Enter fullscreen mode

Exit fullscreen mode

### 2. You say something

Your microphone audio flows through fastrtc →receive()→ resampled to 16 kHz → sent to Gemini as raw PCM bytes.

### 3. Gemini responds

The response stream can contain multiple types of data in a single turn:

* Audio chunks→ queued for playback and fed to theHeadWobbler(which generates speech-reactive head sway)
* Input transcription→ "what the user said" displayed in the chat
* Output transcription→ "what the robot said" displayed in the chat
* Tool calls→ dispatched to theBackgroundToolManager
* Interruption signals→ the user barged in, clear the audio queue

### 4. Tool execution

Tool calls run in background tasks so the audio stream isn't blocked. When a tool finishes, its result is sent back to Gemini as aFunctionResponse, and the model can narrate what happened:

"I just did a little happy dance for you! 💃"

### 5. Idle behavior

If nobody speaks for 15+ seconds and the robot is idle, the handler sends a nudge:

"
You
'
ve been idle for a while. Feel free to get creative — dance, 
show an emotion, look around, do nothing, or just be yourself!
"

Enter fullscreen mode

Exit fullscreen mode

This triggers the robot to autonomously pick an action — maybe a dance, maybe a curious head tilt — keeping interactions lively even during pauses.

## Deployment options

### Local (recommended for development)

Just runreachy-mini-conversation-appas shown above. The app connects to a robot daemon on your local network.

### Cloud Run (for Twilio phone integration)

The app can also be deployed to Google Cloud Run with a Twilio integration for phone-based conversations. This is a more advanced setup — check the repo's deployment docs for details on:

* Configuring Twilio Media Streams
* Setting up IAM-based authentication
* Managing secrets with Google Secret Manager

## The built-in personalities

The repo ships with 15 ready-made profiles to get you started:

Profile

Character

default

Friendly, concise robot assistant with subtle humor

mars_rover

A rover exploring Mars

noir_detective

A hardboiled detective from a 1940s film

victorian_butler

An impeccably proper English butler

mad_scientist_assistant

An excitable lab assistant

bored_teenager

...you get the idea

cosmic_kitchen

A space-themed cooking show host

hype_bot

Maximum enthusiasm about everything

captain_circuit

A superhero robot

chess_coach

A patient chess mentor

nature_documentarian

David Attenborough vibes

sorry_bro

Apologizes for literally everything

tedai

A TED talk speaker

time_traveler

Visiting from the future

Try them out! Each one completely transforms how the robot behaves and responds.

## Wrapping up

The Reachy Mini Conversation App shows what's possible when you combine real-time voice AI with expressive robotics. The key design decisions that make it work:

* Handler abstraction— Gemini Live by default, with OpenAI Realtime as a drop-in alternative
* Background tool dispatch— tool calls never block the audio stream
* Layered motion system— primary moves + secondary offsets + idle breathing = a robot that always feels alive
* Plain-text profiles— customize personality without writing code

The entire project is open source under Apache 2.0. Fork it, give your robot a personality, and let us know what you build!

Links:

* 📦GitHub Repository
* 🤖Reachy Mini SDK
* 💃Dances Library (Hugging Face)
* 😊Emotions Library (Hugging Face)
* 🔑Get a Gemini API Key

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse