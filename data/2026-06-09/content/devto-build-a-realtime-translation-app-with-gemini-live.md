---
title: Build a Realtime Translation App with Gemini Live API, LiveKit, & Google Cloud Run - DEV Community
url: https://dev.to/googleai/build-a-realtime-translation-app-with-gemini-live-api-livekit-google-cloud-run-5474
site_name: devto
content_file: devto-build-a-realtime-translation-app-with-gemini-live
fetched_at: '2026-06-09T19:43:49.319114'
original_url: https://dev.to/googleai/build-a-realtime-translation-app-with-gemini-live-api-livekit-google-cloud-run-5474
author: Thor 雷神 Schaeff
date: '2026-06-09'
description: Imagine speaking in English, and having listeners from all over the world hear you translated into... Tagged with ai, gemini, nextjs, tutorial.
tags: '#ai, #gemini, #nextjs, #tutorial'
---

Imagine speaking in English, and having listeners from all over the world hear you translated into Spanish, Japanese, or French — in real-time, with low latency, and natural vocal delivery.

In this guide, we’ll build and deploy aReal-Time Multilingual Translation Broadcastweb application. We'll leverageNext.jsfor the frontend,LiveKit Cloudfor ultra-low latency WebRTC audio delivery, and theGemini Live APIto translate audio streams on the fly.

Finally, we’ll containerize the entire application and deploy it as a production-ready, auto-scaling service onGoogle Cloud Run.

## Architecture

Our application runs entirely within a single LiveKit Room to keep signaling fast and simple:

Organizer (Speaking)
 │ (Vocal audio via WebRTC)
 ▼
LiveKit Room
 ├── TranslationBridge Bot ES (Gemini) ──► Spanish Audio Published
 ├── TranslationBridge Bot JA (Gemini) ──► Japanese Audio Published
 └── TranslationBridge Bot FR (Gemini) ──► French Audio Published
 │
 ▼ (Selected translation stream)
Attendees (Watch Page)

Enter fullscreen mode

Exit fullscreen mode

1. The Ingest: The host starts a broadcast. Their vocal audio is streamed to a LiveKit Room.
2. On-Demand Spin-up: When a listener joins and selects a language (e.g., Spanish), the Next.js backend spins up a dedicated background worker thread called theTranslation Bridge.
3. The WebRTC to WebSocket Pipe: The worker connects to the LiveKit Room as a bot, subscribes to the host's audio track, and forwards the raw PCM audio frames over a WebSocket connection to theGemini Live API.
4. Vocal Translation: Gemini processes the vocal stream and responds with real-time translated audio.
5. Playback: The bot publishes the translated audio track back to the LiveKit Room, and the listener renders that specific bot track.

## 🛠️ Prerequisites

Before we start, make sure you have:

* Node.js 18+installed locally.
* ALiveKit Cloud Account(the free tier is perfect).
* A Google Cloud Project with thegcloud CLIinstalled and authenticated.
* AGemini API Keywith access to the Live API models.

## 💻 Step-by-Step Setup Guide

### Step 1: Install Dependencies

Navigate to the root of the project and install the NPM packages:

npm 
install

Enter fullscreen mode

Exit fullscreen mode

### Step 2: Start a Local LiveKit Server

If you want to test the setup locally, you can easily spin up a local LiveKit development server using Docker:

docker run 
--rm
 
-p
 7880:7880 
-p
 7881:7881 
-p
 7882:7882/udp 
\

 
-e
 
LIVEKIT_KEYS
=
"devkey: secret"
 
\

 livekit/livekit:latest 
\

 
--dev

Enter fullscreen mode

Exit fullscreen mode

### Step 3: Configure Environment Variables

Create a.env.localfile in the root of the project. This will be used for your local environment:

LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
NEXT_PUBLIC_LIVEKIT_URL=ws://localhost:7880
LIVEKIT_URL=ws://localhost:7880
GEMINI_API_KEY=your-gemini-api-key-here

Enter fullscreen mode

Exit fullscreen mode

### Step 4: Run the Application Locally

Launch the Next.js development server:

npm run dev

Enter fullscreen mode

Exit fullscreen mode

Openhttp://localhost:3000to view the application. Open one tab as theBroadcast(host) and another tab toWatch(attendee) to test translation.

## ⚡ Latency & Performance Optimization: 100ms Chunks

When dealing with real-time WebRTC streams, standard packet delivery operates on a20msinterval. Delivering audio chunks to the Gemini Live API at 50 Hz (50 times per second) results in high network overhead and CPU cycles.

To optimize performance, we configure LiveKit's native FFI audio stream to capture100ms chunksinstead.

Intranslation-bridge.ts, we initialize theAudioStreamwith anAudioStreamOptionsobject:

const
 
audioStream
 
=
 
new
 
AudioStream
(
track
,
 
{

 
sampleRate
:
 
this
.
inputSampleRate
,

 
numChannels
:
 
this
.
channels
,

 
frameSizeMs
:
 
100
,
 
// Deliver 100ms frames to optimize transmission frequency

});

Enter fullscreen mode

Exit fullscreen mode

### Why do this?

* Frequency Drop:This drops the transmission frequency to Gemini from50 Hz to 10 Hz(10 times per second).
* The Trade-Off:This dramatically reduces network/CPU serialization overhead on the server, with only a minor latency increase (~80ms).

## 🐳 Step 5: Containerizing with Docker

Next.js's standalone output builds yield highly optimized production bundles containing only the exact files needed for deployment.

The@livekit/rtc-nodeSDK uses a native compiled WebRTC core. During initialization, this core makes HTTPS requests to verify Cloud settings. Bare-minimum Linux images likenode:slimdo not ship with SSL certificates, which can cause the secure connection to fail silently. We explicitly installca-certificatesin our multi-stageDockerfile:

# --- Build stage ---

FROM
 
node:22-slim
 
AS
 
builder

WORKDIR
 /app

COPY
 package.json package-lock.json ./

RUN 
npm ci

COPY
 . .

RUN 
npm run build

# --- Production stage ---

FROM
 
node:22-slim
 
AS
 
runner

RUN 
apt-get update 
&&
 apt-get 
install
 
-y
 ca-certificates 
&&
 
rm
 
-rf
 /var/lib/apt/lists/
*

WORKDIR
 /app

ENV
 NODE_ENV=production

ENV
 PORT=8080

COPY
 --from=builder /app/.next/standalone ./

COPY
 --from=builder /app/.next/static ./.next/static

COPY
 --from=builder /app/public ./public

EXPOSE
 8080

CMD
 ["node", "server.js"]

Enter fullscreen mode

Exit fullscreen mode

## 🚀 Step 6: Deploying to Google Cloud Run

We recommend deploying to Google Cloud Run since the translation bridges are long-running processes (WebSocket connections to Gemini and LiveKit) that require persistent containers and support for long-running requests.

### 1. Store Secrets in Google Secret Manager

Instead of exposing credentials in env vars, store them in Google Secret Manager:

source
 <
(
grep
 
-v
 
'^#'
 .env.local | 
sed
 
's/^/export /'
)

echo
 
-n
 
"
$GEMINI_API_KEY
"
 | gcloud secrets create gemini-api-key 
--data-file
=
-

echo
 
-n
 
"
$LIVEKIT_API_KEY
"
 | gcloud secrets create livekit-api-key 
--data-file
=
-

echo
 
-n
 
"
$LIVEKIT_API_SECRET
"
 | gcloud secrets create livekit-api-secret 
--data-file
=
-

Enter fullscreen mode

Exit fullscreen mode

### 2. Grant Secret Access Permissions to Cloud Run

Grant the Default Compute Engine Service Account access to read these secrets:

PROJECT_NUMBER
=
$(
gcloud projects describe 
$(
gcloud config get-value project
)
 
--format
=
"value(projectNumber)"
)

gcloud secrets add-iam-policy-binding gemini-api-key 
\

 
--member
=
"serviceAccount:
${
PROJECT_NUMBER
}
-compute@developer.gserviceaccount.com"
 
\

 
--role
=
"roles/secretmanager.secretAccessor"

gcloud secrets add-iam-policy-binding livekit-api-key 
\

 
--member
=
"serviceAccount:
${
PROJECT_NUMBER
}
-compute@developer.gserviceaccount.com"
 
\

 
--role
=
"roles/secretmanager.secretAccessor"

gcloud secrets add-iam-policy-binding livekit-api-secret 
\

 
--member
=
"serviceAccount:
${
PROJECT_NUMBER
}
-compute@developer.gserviceaccount.com"
 
\

 
--role
=
"roles/secretmanager.secretAccessor"

Enter fullscreen mode

Exit fullscreen mode

### 3. Deploy the Service

Run the deployment command. Note the specific Cloud Run production scaling configurations required:

* --min-instances 1: Keeps the container warm so active sessions aren't killed.
* --max-instances 1: TheTranslationSessionManagersingleton requires a single instance.
* --timeout 3600: Allows translation sessions up to 1 hour.
* --no-cpu-throttling: Keeps CPU allocated between requests to ensure zero audio processing lag.

gcloud run deploy live-translate 
\

 
--source
 
.
 
\

 
--region
 us-central1 
\

 
--allow-unauthenticated
 
\

 
--min-instances
 1 
\

 
--max-instances
 1 
\

 
--timeout
 3600 
\

 
--no-cpu-throttling
 
\

 
--set-secrets
 
"
\

GEMINI_API_KEY=gemini-api-key:latest,
\

LIVEKIT_API_KEY=livekit-api-key:latest,
\

LIVEKIT_API_SECRET=livekit-api-secret:latest"
 
\

 
--set-env-vars
 
"
\

LIVEKIT_URL=wss://your-project.livekit.cloud"

Enter fullscreen mode

Exit fullscreen mode

### 4. Deploying Future Code Updates (Without Changing Env Vars)

Once your service configuration and secrets are set, you can deploy code updates without repeating or redefining the environment variables:

gcloud run deploy live-translate 
--source
 
.
 
--region
 us-central1

Enter fullscreen mode

Exit fullscreen mode

Google Cloud Run automatically preserves all environment variables, secrets, scaling limits, and CPU allocations from the previous revision.

## 🎉 Conclusion

You now have a fully functional, production-ready Real-Time Multilingual Translation Broadcast app deployed on Google Cloud Run!

### What we learned:

* How to bridgeLiveKit WebRTC audiowith theGemini Live APIto translate spoken streams in real-time.
* How to tweak native FFI stream options (frameSizeMs: 100) to optimize network packet overhead.
* How to set up Google Secret Manager and deploy robust multi-stage docker setups to Google Cloud Run.

Happy broadcasting! 🌐🎙️

## What's next

* Read thedocs
* Run theGoogle Colab
* Check out the GeminiLive API examples on GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse