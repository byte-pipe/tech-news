---
title: Build a voice-enabled Telegram Bot with the Gemini Interactions API - DEV Community
url: https://dev.to/googleai/build-a-voice-enabled-telegram-bot-with-the-gemini-interactions-api-nm5
date: 2026-04-16
site: devto
model: llama3.2:1b
summarized_at: 2026-04-17T06:14:26.468815
---

# Build a voice-enabled Telegram Bot with the Gemini Interactions API - DEV Community

**Building a Voice-Enabled Telegram Bot with Gemini Interactions API**

This guide will walk you through the process of creating a voice-enabled Telegram bot that utilizes Google's Gemini Interaction API to handle both text and voice messages.

### Key Points:

* Use a combination of Python, Flask API, pydub, and ffmpeg for audio processing and conversion
* Create a new directory and set up project basics using `python-telegram-bot`, `google-genai`, and `pydub`
* Configure environment variables and add credentials to the `.env` file
* Utilize Gemini models: `gemini-3.1-flash-lite-preview` for reasoning and `gemini-3.1-flash-tts-preview` for text-to-speech rendering

### Prerequisites:

* Python 3.11+
* Telegram Bot Token (create a bot via @botfather)
* Google AI API Key
* ffmpeg installed on macOS or Linux

### Project Setup:

Create a new directory and set up the basics:
```markdown
mkdir telegram-gemini-voice-bot
cd telegram-gemini-voice-bot

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install python-telegram-bot[webhooks]~=21.11
google-genai>=1.55.0
pydub~=0.25

# Create .env file with credentials
echo "TELEGRAM_BOT_TOKEN=your-telegram-bot-token" > .env
echo "GOOGLE_API_KEY=your-google-api-key" >> .env
echo "TELEGRAPH_SECRET_TOKEN=axpgenerated-string-here" >> .env
echo "VOICE_ENABLED=true" >> .env

# Enter fullscreen mode
fullscreen_mode

# Exit fullscreen mode
exit fullscreen_mode
```
### Step 1: The Skeleton

Create a new file called `bot.py` and import required libraries:
```python
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import base64
import io
import logging
import os
import wave
from google.genai import Client

# Config
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
GOOGLE_API_KEY = "your-google-api-key"
WEBHOOK_URL = "wheepeevoBot:12345678"  # Replace with your webhook URL

PORT = int(os.environ['PORT'])

REASONING_MODEL = "github/gemini-3.1-flash-lite-preview"
TTS_MODEL = "github/gemini-3.1-flash-tts-preview"
TTSVoice = "Kore"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

class Bot:
    def __init__(self, client):
        self.client = client

def main():
    bot = Bot(Client(api_key=GOOGLE_API_KEY))
    app = ApplicationBuilder().token(WEBHOOK_URL).build()
    app.add_handler(CommandHandler("start", lambda ctx: print(f"Starting service with token {BOT_TOKEN}")))
    app.add_handler(MessageHandler filters.text_commands())
    app.listen(PORT)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(str(e))

```
### Step 2: Reasoning and Text-to-Speech Processing

In this step, we will utilize two Gemini models: `gemini-3.1-flash-lite-preview` for reasoning and `gemini-3.1-flash-tts-preview` for text-to-speech rendering.
```python
@app.on_message()
async def handle_text_message(ctx):
    # Use pydub to convert PCM audio to Opus format
    opus_file = base64.b64encode(io.BytesIO(open(f"PianoMelody.wav", 'rb').read()).getvalue())
    logger.info(opus_file.decode('utf-8'))

    # ConvertOpus file to WAV file
    wav_file = f"WAV_{opus_file[:16]}{opus_file[16:]}"

    # Create voice message using TTS model for text-to-speech rendering
    audio_features = {
        "opus": opus_file,
        "wav": open(wav_file, 'rb').read(),
    }
    logger.info(audio_features)

    # Reasoning step (replace with your logic)
    reasoning_response = ...
    logger.info(reasoning_response)

    return True

class SendVoiceMessageHandler(ContextTypes.DEFAULT):
    def __init__(self, sender, bot):
        self.sender = sender
        self.bot = bot

    @staticmethod
    async def main(ctx):
        # Speak the reply back as a voice message using TTS model
        audio_features = SendVoiceMessgeHandler.get_audio_features()
        response = f"I said {username} that"
        if 're': response += "re"
        logger.info(response)
        await ctx.sendaudio(audio_features['wav'])

def generate.voice_message():
    # Replace with your logic for generating voice messages
    return ...
```
### Step 3: Integrate the Logic

Integrate the logic for reasoning and text-to-speech rendering into the `main` function.
```python
@app.on_message()
async def handle_text_message(ctx):
    ...

    response = await SendVoiceMessageHandler.main(ctx)
    logging.info(response)

if __name__ == "__main__":
    try:
        bot = Bot(Client(api_key=GOOGLE_API_KEY))
        app.run()
    except Exception as e:
        logger.error(str(e))

```

This is a basic example to get you started. You'll need to customize and expand this code to fit your specific requirements.