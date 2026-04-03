---
title: Video Understanding with Gemini 3.0 Flash for Robotics - DEV Community
url: https://dev.to/googleai/video-understanding-with-gemini-30-flash-for-robotics-5896
site_name: devto
content_file: devto-video-understanding-with-gemini-30-flash-for-robot
fetched_at: '2026-02-08T11:09:39.569649'
original_url: https://dev.to/googleai/video-understanding-with-gemini-30-flash-for-robotics-5896
author: Paul Ruiz
date: '2026-02-05'
description: In the robotics field, as with nearly every other corner of tech, the landscape is shifting rapidly... Tagged with ai, robotics, gemini, developers.
tags: '#ai, #robotics, #gemini, #developers'
---

In the robotics field, as with nearly every other corner of tech, the landscape is shifting rapidly as we integrate AI into our workflows and systems. For this post, I’ve put together a few demos to explore Gemini's multimodal capabilities forvideo understanding. We’ll look at how these features can be applied to robotics-specific use cases, as well as how they can be used for general learning augmentation.

If you're not familiar with Gemini yet, here's aquick startfor running a basic "Hello World" example. Be sure to set yourGOOGLE_GEMINI_APIvariable so that your API key can be found (I forget this step pretty much every time :)).

With that, let's jump in.

## Analyzing a local file: Video to Action

In this first example, I have a video file saved locally that shows a bi-arm Aloha robot doing various tasks on a desk (if you'd like to use the same video to follow along, you can find ithere).

If I wanted to make this sequence repeatable with aVision-Language-Action (VLA)model, I’d first need to break the video down into subtasks. I wrote a small program that reviews the video and returns a structured list of actions, identifying the "actor" and the specific task for each segment.

from

google

import

genai

from

google.genai

import

types

import

time

import

json

import

pandas

as

pd

import

plotly.express

as

px

from

datetime

import

timedelta

client

=

genai
.
Client
()

myfile

=

client
.
files
.
upload
(
file
=
"
desk_organization.mp4
"
)

while

myfile
.
state

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
)


time
.
sleep
(
1
)


myfile

=

client
.
files
.
get
(
name
=
myfile
.
name
)

if

myfile
.
state
.
name

==

"
FAILED
"
:


raise

ValueError
(
myfile
.
state
.
name
)

print
(
"
Processed
"
)

prompt

=

"""

Review this video and break the actions into a structured JSON list.
Each object in the list must have:
-
"
actor
"
: The entity performing the action (e.g.,
'
Left Robot Arm
'
).
-
"
action
"
: A short description of the task.
-
"
start_s
"
: Start time in total seconds (integer).
-
"
end_s
"
: End time in total seconds (integer).

Output ONLY the raw JSON list.

"""

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
"
gemini-3-flash-preview
"
,


contents
=
[
myfile
,

prompt
],


config
=
types
.
GenerateContentConfig
(


response_mime_type
=
"
application/json
"
,


thinking_config
=
types
.
ThinkingConfig
(
thinking_budget
=-
1
)


),

)

print
(
response
.
text
)

Enter fullscreen mode

Exit fullscreen mode

Let's break this into smaller parts. First, I use Gemini'sFiles APIto upload the video. Theclient.files.uploadcommand used here will block the script until the file has been uploaded, and then the begins processing the file for use. So we don't accidentally try to access the file before it's ready, which will cause an error, I also have a loop that checks the status of the file before letting the program continue.

myfile

=

client
.
files
.
upload
(
file
=
"
desk_organization.mp4
"
)

while

myfile
.
state

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
)


time
.
sleep
(
1
)


myfile

=

client
.
files
.
get
(
name
=
myfile
.
name
)

if

myfile
.
state
.
name

==

"
FAILED
"
:


raise

ValueError
(
myfile
.
state
.
name
)

Enter fullscreen mode

Exit fullscreen mode

Next I have a very specific prompt about how I want the data to be returned to me so that I can get the actor, action, and starting and ending time for that action. I also use theresponse_mime_typeflag to specify that I only want JSON data returned to me.

prompt

=

"""

Review this video and break the actions into a structured JSON list.
Each object in the list must have:
-
"
actor
"
: The entity performing the action (e.g.,
'
Left Robot Arm
'
).
-
"
action
"
: A short description of the task.
-
"
start_s
"
: Start time in total seconds (integer).
-
"
end_s
"
: End time in total seconds (integer).

Output ONLY the raw JSON list.

"""

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
"
gemini-3-flash-preview
"
,


contents
=
[
myfile
,

prompt
],


config
=
types
.
GenerateContentConfig
(


response_mime_type
=
"
application/json
"
,


thinking_config
=
types
.
ThinkingConfig
(
thinking_budget
=-
1
)


),

)

Enter fullscreen mode

Exit fullscreen mode

At this point we can get the JSON data outlining the actions that the robots have taken, which can then be used to prompt a VLA to repeat the tasks.

[


{


"actor"
:

"Left Robot Arm"
,


"action"
:

"pick up the green marker"
,


"start_s"
:

0
,


"end_s"
:

3


},


{


"actor"
:

"Left Robot Arm"
,


"action"
:

"place the green marker in the wooden bowl"
,


"start_s"
:

3
,


"end_s"
:

6


},


{


"actor"
:

"Left Robot Arm"
,


"action"
:

"pick up the blue pen"
,


"start_s"
:

13
,


"end_s"
:

16


},


{


"actor"
:

"Left Robot Arm"
,


"action"
:

"place the blue pen in the pencil holder"
,


"start_s"
:

18
,


"end_s"
:

22


},


{


"actor"
:

"Right Robot Arm"
,


"action"
:

"pick up the red pen"
,


"start_s"
:

22
,


"end_s"
:

25


},


{


"actor"
:

"Right Robot Arm"
,


"action"
:

"place the red pen in the pencil holder"
,


"start_s"
:

25
,


"end_s"
:

28


}

]

Enter fullscreen mode

Exit fullscreen mode

Structured data is great for code, but for humans, visuals are better. I asked Gemini to write a script to turn that JSON into aGantt chartusing Plotly. This makes it easy to see the task orchestration and timestamps at a glance.

data

=

json
.
loads
(
response
.
text
)

df

=

pd
.
DataFrame
(
data
)

base_time

=

pd
.
to_datetime
(
"
2025-01-01
"
)

df
[
'
start_dt
'
]

=

df
[
'
start_s
'
].
apply
(
lambda

x
:

base_time

+

timedelta
(
seconds
=
x
))

df
[
'
end_dt
'
]

=

df
[
'
end_s
'
].
apply
(
lambda

x
:

base_time

+

timedelta
(
seconds
=
x
))

dynamic_height

=

150

+

(
len
(
df
[
'
actor
'
].
unique
())

*

60
)

fig

=

px
.
timeline
(


df
,


x_start
=
"
start_dt
"
,


x_end
=
"
end_dt
"
,


y
=
"
actor
"
,


color
=
"
actor
"
,


text
=
"
action
"
,


template
=
"
plotly_white
"
,


height
=
dynamic_height

)

fig
.
update_layout
(


title_text
=
"
Video Orchestration
"
,


title_x
=
0.5
,


showlegend
=
False
,


margin
=
dict
(
l
=
10
,

r
=
10
,

t
=
40
,

b
=
30
),


xaxis_title
=
None
,


yaxis_title
=
None
,


font
=
dict
(
size
=
11
)

)

fig
.
layout
.
xaxis
.
update
({


'
tickformat
'
:

'
%M:%S
'
,


'
fixedrange
'
:

True

})

fig
.
update_yaxes
(
autorange
=
"
reversed
"
,

fixedrange
=
True
)

fig
.
update_traces
(


textposition
=
'
inside
'
,


insidetextanchor
=
'
middle
'
,


marker_line_width
=
1
,


marker_line_color
=
"
white
"
,


width
=
0.6

)

fig
.
show
()

Enter fullscreen mode

Exit fullscreen mode

This gives us a clean, visual breakdown of the robot's performance:

## Understanding videos from YouTube

For my next experiment, I took some inspiration from this paper onMobility VLA. I wanted to try using a long YouTube video of a tour (specifically one from the former Egyptian Museum in Cairo because it was one of my favorites and I generally just loved Egypt the few times I've been), and then ask questions about things seen in that video.

Since I could potentially do this on a robot with its own mobility stack where I could return to a location based on a time stamp, I figured I'd also ask for a timestamp for when the video shows the largest item on the tour.

Luckily, the code for this is really straightforward. You just need to provide a YouTube link as afile_dataobject and send in your prompt.

from

google

import

genai

from

google.genai

import

types

client

=

genai
.
Client
()

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
models/gemini-3-flash-preview
'
,


contents
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


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=EdCReWs6-wI
'
)


),


types
.
Part
(
text
=
'
Please summarize the different things seen in this video and provide a timestamp for the location where the largest object is seen.
'
)


]


),

)

print
(
response
.
text
)

Enter fullscreen mode

Exit fullscreen mode

This will give you a response like:

The Egyptian Museum, also known as the Museum of Ancient Egyptian Antiquities, is a renowned institution in Cairo, Egypt. It is home to a vast and priceless collection of ancient Egyptian artifacts, including the world-famous treasures of Tutankhamun. The video displays various things like:

* **Museum exterior:** The video begins with an exterior shot of the museum at night.
* **Sarcophagi:** There are many sarcophagi of different sizes and materials, including stone, granite, and wood.
* **Statues:** The museum houses a wide range of statues representing pharaohs, gods, goddesses, and everyday people.
* **Wooden boats:** Ancient Egyptian wooden boats used for burial rituals are on display.
* **Display cases:** Many of the museum's smaller artifacts, such as jewelry, amulets, and pottery, are shown in display cases.

The largest object is seen at [05:54](https://www.youtube.com/watch?v=EdCReWs6-wI&t=352).

Enter fullscreen mode

Exit fullscreen mode

OK, so one downside: this isn'treallyuseful if I want to use the information in my robot code, as I'd have to do extra work to extract the timestamp. but it turns out there's a more organized way to do this using a Gemini capability calledstructured outputs.

To get the data back in a way I can use it, I'll still request a JSON mime type, but I'll also create some objects representing the data I want:

class

ItemSeen
(
BaseModel
):


object
:

str

=

Field
(
description
=
"
Object seen in the video
"
)


description
:

str

=

Field
(
description
=
"
Description of the object seen in the video
"
)

class

Navigation
(
BaseModel
):


itemsSeen
:

List
[
ItemSeen
]


timestamp
:

int

=

Field
(
description
=
"
Timestamp where the largest item is seen
"
)

Enter fullscreen mode

Exit fullscreen mode

Then I'll use those objects as a schema for the data by adding a config object to mygenerate_contentcall.

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
models/gemini-3-flash-preview
'
,


contents
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


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=EdCReWs6-wI
'
)


),


types
.
Part
(
text
=
'
Please summarize the different things seen in this video and provide a timestamp for the location where the largest object is seen.
'
)


]


),


config
=
{


"
response_mime_type
"
:

"
application/json
"
,


"
response_json_schema
"
:

Navigation
.
model_json_schema
(),


}

)

Enter fullscreen mode

Exit fullscreen mode

At this point I can extract the data returned into the model object and use it in my app. The output will look like this:

itemsSeen

=

[

ItemSeen
(
object
=
'
Pharaohs and Queens statues
'
,

description
=
'
Statues depicting different Pharaohs and Queens, carved from various materials such as stone and wood, showcasing traditional poses and royal regalia.
'
),

ItemSeen
(
object
=
'
Sarcophagi and mummy cases
'
,

description
=
'
Ornate containers used to hold mummies, including stone sarcophagi and wooden mummy cases adorned with intricate hieroglyphs and religious imagery.
'
),

ItemSeen
(
object
=
'
Animal-headed deities
'
,

description
=
'
Statues of gods and goddesses represented with animal heads, like the jackal-headed Anubis, falcon-headed Horus, and lioness-headed Sekhmet.
'
),

ItemSeen
(
object
=
'
Pyramidions
'
,

description
=
'
Small pyramid-shaped stones, often made of basalt or granite, that once capped the tops of pyramids or obelisks, inscribed with prayers and scenes.
'
),

ItemSeen
(
object
=
'
Ancient wooden boat
'
,

description
=
'
A well-preserved funerary boat made of wood, reconstructed to show how these vessels were used for symbolic journeys in the afterlife.
'
),

ItemSeen
(
object
=
'
Reliefs and stelae
'
,

description
=
'
Stone slabs and wall segments featuring carved or painted scenes and inscriptions, documenting the lives, achievements, and religious beliefs of the ancient Egyptians.
'
),

ItemSeen
(
object
=
'
Display cases with artifacts
'
,

description
=
'
Glass-enclosed cases containing smaller items such as jewelry, figurines, tools, and household objects, providing a glimpse into daily life and craftsmanship.
'
)

]

timestamp

=

361

Enter fullscreen mode

Exit fullscreen mode

## Querying multiple YouTube videos

So now that we know how to query against a YouTube video, let's take this a step further. With an API key that's tied to a paid account, I can run Gemini over10different YouTube videos with one call. This could be great for analyzing multiple camera feeds to check for task success, but since I don't have that data on hand, I'm going to focus on the fact that this field requires alotof constant learning and I need all of the help I can get.

For this example I'll load six robotics lectures from Stanford University (I have no affiliation with them or this content, I just really like and value free educational content) and ask Gemini to create some concise notes, as well as use Google Search to look up and give me a recommended reading list to support my robotics learning journey.

from

google

import

genai

from

google.genai

import

types

client

=

genai
.
Client
()

google_search_tool

=

types
.
Tool
(


google_search
=
types
.
GoogleSearch
()

)

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
models/gemini-3-flash-preview
'
,


contents
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


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=o5bW3C5OD6U
'
),


),


types
.
Part
(


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=PYh9k4cy25w
'
),


),


types
.
Part
(


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=RKFRO_G4YkA
'
),


),


types
.
Part
(


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=v18Jo2ILXZ8
'
),


),


types
.
Part
(


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=5uWtpDON7Vs
'
),


),


types
.
Part
(


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=05SuBLowwKM
'
),


),


types
.
Part
(
text
=
'
This is a set of six lectures for a robotics course. Please write concise notes for each video in markdown, then create a list of research papers and books that would be relevant to each course. Check reviews for books that you provide and mention why they would be worth reading to learn this material in depth.
'
)


]


),


config
=
types
.
GenerateContentConfig
(


tools
=
[
google_search_tool
],


),

)

print
(
response
.
text
)

Enter fullscreen mode

Exit fullscreen mode

Now if we run this we get... an error:

google.genai.errors.ClientError: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Please use fewer than 10800 images in your request to this model', 'status': 'INVALID_ARGUMENT'}}

Enter fullscreen mode

Exit fullscreen mode

What's happening here is that Gemini 3.0-Flash's context window supports a maximum of 10,800 images. At 1 frame per second, that's three hours of video, and the six long lectures exceed this limit.

To get around this, we can play around with some video settings since these are lectures that don't have a ton changing with each frame and aren't graphics-intensive. For starters, let's add amedia_resolutionproperty to theconfigobject to convert the video into a low resolution video when processing. You can find more about this property in the officialdocumentation here.

We can also lower the frame rate that gets processed on each video, so in this case we'll only look at one frame every ten seconds rather than one frame per second.

In the end we land on a simple script that looks like this:

from

google

import

genai

from

google.genai

import

types

client

=

genai
.
Client
()

google_search_tool

=

types
.
Tool
(


google_search
=
types
.
GoogleSearch
()

)

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
models/gemini-3-flash-preview
'
,


contents
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


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=o5bW3C5OD6U
'
),


video_metadata
=
types
.
VideoMetadata
(
fps
=
0.1
),


),


types
.
Part
(


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=PYh9k4cy25w
'
),


video_metadata
=
types
.
VideoMetadata
(
fps
=
0.1
)


),


types
.
Part
(


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=RKFRO_G4YkA
'
),


video_metadata
=
types
.
VideoMetadata
(
fps
=
0.1
)


),


types
.
Part
(


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=v18Jo2ILXZ8
'
),


video_metadata
=
types
.
VideoMetadata
(
fps
=
0.1
)


),


types
.
Part
(


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=5uWtpDON7Vs
'
),


video_metadata
=
types
.
VideoMetadata
(
fps
=
0.1
)


),


types
.
Part
(


file_data
=
types
.
FileData
(
file_uri
=
'
https://www.youtube.com/watch?v=05SuBLowwKM
'
),


video_metadata
=
types
.
VideoMetadata
(
fps
=
0.1
)


),


types
.
Part
(
text
=
'
This is a set of six lectures for a robotics course. Please write concise notes for each video in markdown, then create a list of research papers and books that would be relevant to each course. Check reviews for books that you provide and mention why they would be worth reading to learn this material in depth.
'
)


]


),


config
=
types
.
GenerateContentConfig
(


tools
=
[
google_search_tool
],


media_resolution
=
types
.
MediaResolution
.
MEDIA_RESOLUTION_LOW


),

)

print
(
response
.
text
)

Enter fullscreen mode

Exit fullscreen mode

which in turn gives us the following output:

Here are concise markdown notes for the six lectures featured in this robotics seminar, followed by curated lists of research papers and books to deepen your understanding of each specific domain.

---

# Lecture 1: Autonomous Navigation in Complex Outdoor Environments
**Speaker:** Jing Liang (Stanford/UMD)

### Concise Notes
* **Problem Definition:** Moving beyond obstacle avoidance to "traversability analysis"—understanding which surfaces (grass, gravel, etc.) a robot can actually handle.
* **VLM Integration:** Utilizing Vision-Language Models (VLMs) to translate natural language goals and visual cues into viable path Candidates.
* **Gaussian Splats for Mapping:** Implementing 3D Gaussian Splatting to estimate not just geometry, but semantic material types and physical properties (friction, hardness, density).
* **Companion Robotics:** Applying these navigation stacks to older adults ("longevity robots") to assist with outdoor exercise and health monitoring.
* **Dataset:** Introduction of the Global Navigation Dataset (GND) covering 10 campuses with multi-modal sensor data.

### Relevant Resources
**Research Papers:**
* *MaPNav: Trajectory Generator with Traversability Coverage for Outdoor Navigation* (Liang et al., 2024).
* *SplatFlow: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation* (Chopra et al., 2024).

**Books:**
* **"Probabilistic Robotics" by Sebastian Thrun, Wolfram Burgard, and Dieter Fox.**
 * *Review:* Regarded as the "bible" of modern navigation. It is essential for understanding the SLAM and state estimation fundamentals that Jing Liang’s complex environment navigation is built upon.

---

# Lecture 2: From Digital Humans to Safe Humanoids
**Speaker:** Yao Feng (Stanford)

### Concise Notes
* **GentleHumanoid Framework:** Focuses on safe physical contact. Instead of just following a path, the robot must regulate interaction forces.
* **Force Modeling:** Differentiates between *Resistive Contact* (robot hitting an object) and *Guiding Contact* (human pulling the robot’s hand).
* **Tunable Force:** Implements a safety threshold (e.g., limiting force to 5N or 15N) to ensure the robot "gives way" during a hug or assistance task.
* **Grounded Reasoning:** Uses "ChatPose" and "ChatHuman" to allow robots to predict human intent and next-frame poses from visual/textual data.

### Relevant Resources
**Research Papers:**
* *GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction* (Lu et al., 2024).
* *ChatPose: Chatting about 3D Human Pose* (Feng et al., 2024).

**Books:**
* **"Humanoid Robotics" by Shuuji Kajita et al.**
 * *Review:* A comprehensive guide to the kinematics and dynamics of two-legged machines. It helps bridge the gap between Feng’s "digital humans" and the physical constraints of a humanoid.

---

# Lecture 3: Resilient Autonomy in Extreme Environments
**Speaker:** Sebastian Scherer (Carnegie Mellon University)

### Concise Notes
* **Definition of Resilience:** The ability to maintain performance in "degraded" conditions (smoke, dust, total darkness, or GPS-denied areas).
* **MapAnything:** A unified feed-forward model that performs 3D reconstruction and metric-scale estimation from simple monocular video.
* **Multi-Modal Sensors:** Leveraging thermal cameras (AnyThermal) and Doppler radar to navigate when visual cameras fail due to glare or darkness.
* **Triage Challenge:** Application of these robots as "pre-first responders" to locate and assess casualties in disaster zones autonomously.

### Relevant Resources
**Research Papers:**
* *MapAnything: Unified 3D Reconstruction from any Visual Input* (Scherer Lab, 2024).
* *AnyThermal: A Single Backbone for Multiple Thermal Perception Tasks* (Li et al., 2024).

**Books:**
* **"Autonomous Mobile Robots" by Roland Siegwart and Illah Nourbakhsh.**
 * *Review:* Excellent for learning about the trade-offs between different sensor modalities (Lidar vs. Vision vs. Thermal), which is the core of Scherer's "resilience" strategy.

---4. **Lecture 4: Robot Motion Learning with Physics-Based PDE Priors**
**Speaker:** Abdul H. Qureshi (Purdue University)

### Concise Notes
* **Neural Time Fields (NTFields):** Using neural networks to solve the *Eikonal Partial Differential Equation (PDE)* for motion planning.
* **TD-Learning for Motion:** Borrowing Temporal Difference learning from RL to regularize gradients between consecutive points in a path.
* **Scalability:** This approach allows for planning in extremely high-dimensional spaces (up to 15-DOF for quadrupeds and arms) much faster than traditional sampling-based planners.
* **Unknown Environments:** The robot builds a "Time Field" map in real-time, treating navigation as following the gradient of arrival time.

### Relevant Resources
**Research Papers:**
* *Physics-Informed Neural Time Fields for Motion Planning* (Ni et al., 2023).
* *Domain Decomposition for Large Scale Neural Motion Planning* (Liu et al., 2024).

**Books:**
* **"Planning Algorithms" by Steven M. LaValle.**
 * *Review:* This is the definitive text on how robots find paths. Reading this is necessary to understand why Qureshi’s use of PDEs is such a radical and efficient departure from traditional RRT* or PRM methods.

---

# Lecture 5: Learning to Control Large Teams of Robots
**Speaker:** Eduardo Montijano (University of Zaragoza)

### Concise Notes
* **Distributed Policies:** Moving away from a "central brain" to local policies where each agent makes decisions based on its immediate neighbors.
* **Self-Attention Swarms:** Utilizing Transformer-like attention mechanisms so robots can handle a varying number of neighbors (scaling from 3 to 3,000 robots).
* **Port-Hamiltonian Systems:** Integrating energy-based physics equations into the neural network to ensure the learned behavior is physically stable and explainable.
* **Gen-Swarms:** Applying Generative AI (Diffusion models) to "draw" complex shapes (like a dragon) for drone shows, then using local controllers to achieve those shapes.

### Relevant Resources
**Research Papers:**
* *LEMURS: Learning Distributed Multi-Robot Interactions* (Sebastián et al., 2023).
* *Gen-Swarms: Generative AI for Swarm Robotics* (Pueyo et al., 2024).

**Books:**
* **"Graph Theoretic Methods in Multiagent Networks" by Mehran Mesbahi and Magnus Egerstedt.**
 * *Review:* Essential for understanding how local connectivity influences global swarm behavior. It provides the mathematical logic for the "neighborhood" approach discussed by Montijano.

---

# Lecture 6: Next Generation Dexterous Manipulation
**Speaker:** Monroe Kennedy III (Stanford)

### Concise Notes
* **The Manipulation Gap:** While robots can walk and flip, they still struggle with small, soft, or articulated objects (like tying shoelaces).
* **Optical Tactile Sensors (DenseTact):** Using internal cameras within soft "fingertips" to sense 4-axis stress fields (normal, shear, and torsion).
* **J-PARSE Algorithm:** Resolving "kinematic singularities" (when a robot arm gets stuck at full extension) through a safety Jacobian projection.
* **Cross-Modality Learning:** Combining vision and touch (Touch-GS) to create 3D Gaussian Splats of objects that are otherwise invisible to cameras (transparent or highly reflective surfaces).

### Relevant Resources
**Research Papers:**
* *DenseTact 2.0: High-Resolution Tactile Sensing for Robot Manipulation* (Do et al., 2023).
* *Touch-GS: Visual-Tactile Supervised 3D Gaussian Splatting* (Swann et al., 2024).

**Books:**
* **"Mechanics of Manipulation" by Matthew T. Mason.**
 * *Review:* This book focuses on the physics of pushing, grasping, and friction. It is vital for understanding the "force closure" and "form closure" concepts Kennedy uses to move beyond simple suction-cup grippers.

Enter fullscreen mode

Exit fullscreen mode

The output gives us concise notes for all lectures and curated reading lists. Having recently read one of the recommended books (Introduction to Autonomous Mobile Robotics by Siegwart and Nourbakhsh), I can say that I think the recommendations seem solid.

## Conclusion

This was a look into a newer capability for Gemini that you can try today with thegemini-3.0-flash-previewmodel. If you found it interesting or have other things you'd want to know about, definitely leave a comment.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
