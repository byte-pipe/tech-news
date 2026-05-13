---
title: Hacking perfectly square AI videos with Veo 3.1 and NanoBanana 2 - DEV Community
url: https://dev.to/googleai/hacking-perfectly-square-ai-videos-with-veo-31-and-nanobanana-2-5cpn
site_name: devto
content_file: devto-hacking-perfectly-square-ai-videos-with-veo-31-and
fetched_at: '2026-05-13T19:36:40.634304'
original_url: https://dev.to/googleai/hacking-perfectly-square-ai-videos-with-veo-31-and-nanobanana-2-5cpn
author: Paige Bailey
date: '2026-05-12'
description: 'If you’ve been playing around with AI video generation lately, you already know the struggle: the... Tagged with python, ai, videogen, webdev.'
tags: '#python, #ai, #videogen, #webdev'
---

If you’ve been playing around with AI video generation lately, you already know the struggle: the tech is insanely cool, but sometimes getting it to outputexactlythe format you want feels like trying to center a<div>in 2014.

Recently, I needed to generate a perfectly looping, high-qualitysquare (1:1) videowith audio using Google's new video models. The problem? Native aspect ratio support can sometimes be finicky depending on the model tier, and cropping a generated 16:9 or 9:16 video often ruins the framing or hallucinates weird artifacts at the edges.

So, I had to let it cook. I came up with a slightly hacky but reliable workaround usingNanoBanana 2,Veo 3.1 Lite, and our old reliable friend,FFmpeg.

Here is the ultimate pipeline to get flawless square AI videos:

### TL;DR

1. Start with a square image concept.
2. Ask NanoBanana 2 to convert it to a 9:16 aspect ratio by literally just padding the top and bottom with black bars.
3. Feed that phone-format 9:16 image into Veo 3.1 Lite as your start and end frames to force a loop.
4. Run a quick Python script usingffmpegto slice off the black bars.

Boom. Perfect square video. Perfect audio sync. And no weird edge hallucinations. Here’s how to automate this flow using Python. 🐍

### Step 1: Generating the "phone format" 9:16 frames with NanoBanana 2

First, we need to generate our 9:16 image with the black bars baked in. Using the newGemini API SDK, we can prompt NanoBanana 2 to do the heavy lifting for us.

from
 
google
 
import
 
genai

from
 
google.genai
 
import
 
types

# Initialize your client

client
 
=
 
genai
.
Client
(
api_key
=
"
YOUR_API_KEY
"
)

def
 
generate_padded_frame
(
prompt
,
 
output_filename
):

 
print
(
"
🎨 Generating padded 9:16 image with NanoBanana 2...
"
)

 
# We explicitly tell NanoBanana 2 to give us a 9:16 image 

 
# where the subject is a square in the middle, padded by black bars.

 
hacked_prompt
 
=
 
f
"
{
prompt
}
. Keep the main subject perfectly square in the center, and pad the top and bottom with solid black bars to make the overall aspect ratio 9:16.
"

 
result
 
=
 
client
.
models
.
generate_images
(

 
model
=
'
nanobanana-2
'
,
 
# Our trusty image model

 
prompt
=
hacked_prompt
,

 
config
=
types
.
GenerateImagesConfig
(

 
number_of_images
=
1
,

 
aspect_ratio
=
"
9:16
"
,

 
output_mime_type
=
"
image/jpeg
"

 
)

 
)

 
# Save the output

 
for
 
generated_image
 
in
 
result
.
generated_images
:

 
image
 
=
 
generated_image
.
image

 
image
.
save
(
output_filename
)

 
print
(
f
"
✅ Saved to 
{
output_filename
}
"
)

# Generate our start/end frame

generate_padded_frame
(
"
A majestic pink flamingo standing in a serene pond
"
,
 
"
flamingo_padded.jpg
"
)

Enter fullscreen mode

Exit fullscreen mode

### Step 2: Generating the video with Veo 3.1 Lite

Now that we have our 9:16 image with black bars (flamingo_padded.jpg), we pass it to Veo 3.1 Lite. By using the same image as the visual prompt, we ensure the video maintains those exact black bars throughout the generation process.

(Note: In the Veo web UI, you can set this as the start and end frame for a perfect loop. Here is the API equivalent for generating the video from your image).

import
 
time

def
 
generate_video
(
image_path
,
 
video_prompt
,
 
output_filename
):

 
print
(
"
🎬 Uploading frame and prompting Veo 3.1 Lite...
"
)

 
# Upload the padded image to the Gemini API

 
initial_frame
 
=
 
client
.
files
.
upload
(
file
=
image_path
)

 
# Wait for the file to be processed

 
while
 
initial_frame
.
state
.
name
 
==
 
"
PROCESSING
"
:

 
print
(
"
.
"
,
 
end
=
""
,
 
flush
=
True
)

 
time
.
sleep
(
2
)

 
initial_frame
 
=
 
client
.
files
.
get
(
name
=
initial_frame
.
name
)

 
# Call Veo 3.1 Lite

 
# We ask it to animate the subject but keep the black bars untouched

 
response
 
=
 
client
.
models
.
generate_content
(

 
model
=
'
veo-3.1-lite
'
,

 
contents
=
[

 
initial_frame
,
 
 
f
"
{
video_prompt
}
. The flamingo moves slightly, but the black bars at the top and bottom must remain exactly the same.
"

 
]

 
)

 
# Save the generated video bytes

 
with
 
open
(
output_filename
,
 
"
wb
"
)
 
as
 
f
:

 
f
.
write
(
response
.
text
.
encode
(
'
utf-8
'
))
 
# Handling depends on raw bytes returned

 
print
(
f
"
\n
✅ Video generated and saved as 
{
output_filename
}
"
)

generate_video
(
"
flamingo_padded.jpg
"
,
 
"
Cinematic shot of a flamingo looking around
"
,
 
"
raw_veo_output.mp4
"
)

Enter fullscreen mode

Exit fullscreen mode

### Step 3: Theffmpegpost-processing

Now we have a beautiful video of a flamingo, but it's a 9:16 file with annoying black bars at the top and bottom.

Wecouldcrop this frame-by-frame using Python libraries like MoviePy, but honestly?ffmpegvia thesubprocessmodule is infinitely faster, uses way less memory, and most importantly:it perfectly preserves the audio streamwithout degrading it through re-encoding.

Since the video is 9:16, trimming it toiw:iw(input width : input width) creates a perfect 1:1 square. FFmpeg is smart enough to center the crop automatically, perfectly slicing off the top and bottom black bars.

import
 
subprocess

def
 
crop_to_square
(
input_video
,
 
output_video
):

 
print
(
"
✂️ Cropping out the black bars with FFmpeg...
"
)

 
command
 
=
[

 
'
ffmpeg
'
,

 
'
-y
'
,
 
# Overwrite output if it exists

 
'
-i
'
,
 
input_video
,
 
# Input file

 
'
-vf
'
,
 
'
crop=iw:iw
'
,
 
# Video Filter: Crop to width x width (automatically centered!)

 
'
-c:a
'
,
 
'
copy
'
,
 
# Copy the audio as-is (chef's kiss for performance)

 
output_video

 
]

 
try
:

 
subprocess
.
run
(
command
,
 
check
=
True
,
 
stdout
=
subprocess
.
DEVNULL
,
 
stderr
=
subprocess
.
DEVNULL
)

 
print
(
f
"
🔥 Success! Perfectly square video saved to 
{
output_video
}
"
)

 
except
 
subprocess
.
CalledProcessError
 
as
 
e
:

 
print
(
f
"
💀 FFmpeg failed: 
{
e
}
"
)

# Run the final crop

crop_to_square
(
"
raw_veo_output.mp4
"
,
 
"
final_square_flamingo.mp4
"
)

Enter fullscreen mode

Exit fullscreen mode

### Why this workaround actually... works

1. Framing control:When you force the AI to outpaint black bars first,youcontrol the framing of the main subject. You aren't relying on the video model to guess what to keep in the center.
2. Audio preservation:The'-c:a', 'copy'flag in FFmpeg ensures you don't lose any audio fidelity when manipulating the video file.
3. Zero hallucinations:Because the video model is explicitly told to keep the black bars, it doesn't waste compute trying to generate weird background details at the extreme top and bottom edges.

Sometimes the best engineering solutions are just stacking simple tools together in a trench coat. 🧥

Have you guys found any other weird/genius hacks for wrangling AI video generation APIs? Drop them in the comments, I’d love to test them out!

(P.S. Make sure you haveffmpegalready installed on your machine before running the Python script, or it will yell at you).

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse