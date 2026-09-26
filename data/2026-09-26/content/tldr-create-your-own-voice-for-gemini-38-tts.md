---
title: Create your own voice for Gemini 3.8 TTS
url: https://www.philschmid.de/gemini-3-8-tts
site_name: tldr
content_file: tldr-create-your-own-voice-for-gemini-38-tts
fetched_at: '2026-09-26T14:54:16.603036'
original_url: https://www.philschmid.de/gemini-3-8-tts
author: Philipp Schmid
date: '2026-09-26'
published_date: '2026-09-24'
description: Gemini 3.8 Flash TTS lets you replicate your own voice or design one from a sentence, then direct delivery line by line.
tags:
- tldr
---

# Create your own voice for Gemini 3.8 TTS

 
September 24, 2026
4
 minute read

Gemini 3.8 Flash TTS and Flash-Lite TTSare now available, in the Gemini API andAI Studio. Ranking #1 on Hume's Voice Design Benchmark, and on top ofVoice Arenain 6 languages.

Biggest new features is that you can now replicate your own voice or create a new one from a sentence. The guide below shows how to do both.

### 1. Record 2 clips

Same mic, same room, 24kHz mono. The API compares the two recordings, so don't switch from a headset to the laptop mic between them.

Bash
# macOS. ":0" is audio device 0. To find your mic:

# ffmpeg -f avfoundation -list_devices true -i ""

 

# me.wav: 15-20s of you talking like you normally do. Explain what

# you're building this week. Don't read, just talk.

ffmpeg
 -f
 avfoundation
 -i
 ":0"
 -ac
 1
 -ar
 24000
 -t
 20
 me.wav

 

# consent.wav: read this word for word:

# "I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model."

ffmpeg
 -f
 avfoundation
 -i
 ":0"
 -ac
 1
 -ar
 24000
 -t
 8
 consent.wav

Linux:-f alsa -i default. On macOS, the first run may only open the microphone permission dialog. Allow it, then run the command again.

The consent sentence must be one of the25 supported versions, read exactly. German, for example:"Ich bin der Eigentümer dieser Stimme und bin damit einverstanden, dass Google diese Stimme zur Erstellung eines synthetischen Stimmmodells verwendet."The reference clip can be in any language. Use the language you want the voice to speak later.

### 2. Create the voice, then speak

Python
import
 base64

from
 google 
import
 genai

 

client = genai.
Client
()

 

def
 b64
(
path
):

 return
 base64.
b64encode
(open(path, 
"rb"
).
read
()).
decode
()

 

voice = client.voices.
create
(

 store
=
True
, 
# kept in your project for 1 year, returns voice_...

 voice
={

 "model"
: 
"gemini-3.8-flash-tts"
,

 "type"
: 
"replicated"
,

 "display_name"
: 
"Me"
,

 "replicated"
: {

 "source_audio"
: {
"mime_type"
: 
"audio/wav"
, 
"data"
: 
b64
(
"me.wav"
)},

 "consent_audio"
: {
"mime_type"
: 
"audio/wav"
, 
"data"
: 
b64
(
"consent.wav"
)},

 },

 },

)

print(voice.id)

 

interaction = client.interactions.
create
(

 model
=
"gemini-3.8-flash-tts"
,

 input
=[{

 "type"
: 
"user_input"
,

 "content"
: [{

 "type"
: 
"text"
,

 "text"
: 
"Okay so... <short pause> I did not record this. <laugh> "

 "Twenty seconds of audio and one consent sentence. That's it."
,

 "annotations"
: [{
"type"
: 
"speech_metadata"
, 
"style"
: 
"casual, a bit amused"
}],

 }],

 }],

 response_format
={
"type"
: 
"audio"
},

 generation_config
={
"speech_config"
: [{
"voice"
: voice.id}]},

)

 

# 3.8 returns a real WAV with a RIFF header. No wave-module wrapping.

open(
"me_synth.wav"
, 
"wb"
).
write
(base64.
b64decode
(interaction.output_audio.data))

Two things to notice. The text is spoken word for word. The delivery ("casual, a bit amused") goes inspeech_metadata.style, and the short sounds go inline as<short pause>and<laugh>. The voice ID is reusable: pass it in any later request, or find it again withclient.voices.list(type_=["replicated"]).

If you don't want anything stored server-side,store=Falsereturns an encryptedvoicekey_...that you keep yourself. It works in the samespeech_configfield and expires after 7 days.

## Or design one from a sentence

No recordings needed. Same call, differentvoicedict. You also get asample_audiopreview, so you can listen to the voice before you synthesize anything:

Python
voice = client.voices.
create
(

 store
=
True
,

 voice
={

 "model"
: 
"gemini-3.8-flash-tts"
,

 "type"
: 
"prompted"
,

 "display_name"
: 
"Deadpan host"
,

 "gender"
: 
"male"
,

 "language_code"
: 
"en-US"
,

 "prompted"
: {
"input"
: 
"A dry, deadpan podcast host in his 30s, low pitch, slight German accent."
},

 },

)

open(
"preview.wav"
, 
"wb"
).
write
(base64.
b64decode
(voice.sample_audio.data))

Then usevoice.idexactly as above.

## What changed in prompting

If you're coming fromgemini-3.1-flash-tts-preview, this will break your prompts, so read theprompting guideand themigration notes. The short version:

* Input text is spoken word for word. Instructions written inside the text get spoken out loud too.
* Delivery that lasts the whole line ("whispering", "out of breath") goes inspeech_metadata.style. Short sounds go inline in angle brackets.
* Multi-speaker turns need an explicitspeakeron every turn.
* Long "Audio Profile" prompts now cause voice drift. Design the persona once with the Voices API, then send short or emptystylestrings.
* Non-streaming (unary) responses are real WAV (audio/wav), so remove any code that adds a WAV header. Setresponse_formattoaudio/l16if you still want raw PCM.