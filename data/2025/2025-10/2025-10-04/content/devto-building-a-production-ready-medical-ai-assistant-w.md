---
title: Building a Production-Ready Medical AI Assistant with Python FastAPI, Tavili, Gemini & LangChain - DEV Community
url: https://dev.to/fonyuygita/building-a-production-ready-medical-ai-assistant-with-python-fastapi-tavili-gemini-langchain-5693
site_name: devto
fetched_at: '2025-10-04T11:08:48.346947'
original_url: https://dev.to/fonyuygita/building-a-production-ready-medical-ai-assistant-with-python-fastapi-tavili-gemini-langchain-5693
author: Fonyuy Gita
date: '2025-09-30'
description: 'Complete Guide: From Zero to Production Table of... Tagged with llm, tutorial, ai, python.'
tags: '#llm, #tutorial, #ai, #python'
---

## Complete Guide: From Zero to Production

## Table of Contents

1. Introduction
2. Why This Project Matters
3. Tech Stack Overview
4. Project Architecture
5. Prerequisites
6. Project Setup
7. Understanding Environment Variables
8. Code Implementation
9. Running the Application
10. Testing Your API
11. Common Issues & Solutions
12. Next Steps
13. GitHub Repo

## Introduction

This guide walks you through buildingMediCare AI- a production-ready medical assistant that can:

* Answer medical questions in English and French
* Extract text from medical records (handwritten or printed)
* Analyze lab results and provide insights
* Search latest medical research
* Give personalized health recommendations

We're usingLangChain Expression Language (LCEL)withGoogle Gemini 2.0- the latest AI model, completelyFREE.

## Why This Project Matters

### The Problem in Cameroon

1. Limited Healthcare Access- Many rural areas lack doctors
2. Language Barriers- English and French speakers need support
3. Medical Literacy- People struggle to understand medical reports
4. Cost- Healthcare consultations are expensive

### Our Solution

A free, AI-powered medical assistant that works offline (once deployed locally), understands both English and French, explains medical terms simply, provides evidence-based information, and respects privacy.

## Tech Stack Overview

Technology

Purpose

Why We Chose It

FastAPI

Backend framework

Fast, modern, auto-documentation

LangChain

AI orchestration

Chain AI operations easily

Google Gemini 2.0

AI model

Free, multimodal (text + vision)

Tavily AI

Medical research

1000 free searches/month

Pydantic

Data validation

Type safety, automatic validation

Python 3.11+

Programming language

Modern, readable, extensive libraries

LangChain helps us chain multiple AI operations together, use templates for consistent prompts, get structured outputs (JSON), and handle retries and errors gracefully.

## Project Architecture

backend/
├── app/
│ ├── __init__.py
│ ├── main.py # FastAPI application entry
│ ├── config.py # Environment & settings
│ ├── routes/
│ │ ├── health.py # Health check endpoints
│ │ ├── analysis.py # Medical analysis endpoints
│ │ └── research.py # Research endpoints
│ ├── services/
│ │ ├── gemini_service.py # Gemini Vision operations
│ │ └── tavily_service.py # Medical research
│ ├── chains/
│ │ ├── chat_chain.py # LangChain chat flows
│ │ └── analysis_chain.py # LangChain analysis flows
│ └── models/
│ └── schemas.py # Pydantic data models
├── requirements.txt
├── .env.example
└── README.md

Enter fullscreen mode

Exit fullscreen mode

## Prerequisites

Before starting, ensure you have:

* Python 3.11+ installed
* pip (Python package manager)
* Text editor (VS Code recommended)
* API Keys (free):Google Gemini API key:Get it hereTavily API key:Get it here
* Google Gemini API key:Get it here
* Tavily API key:Get it here

## Project Setup

### Step 1: Create Project Structure

mkdir
medicare-ai

cd
medicare-ai

mkdir
backend

cd
backend

mkdir

-p
 app/routes app/services app/chains app/models

Enter fullscreen mode

Exit fullscreen mode

### Step 2: Create Virtual Environment

python
-m
 venv venv

# Activate it

# On Windows:

venv
\S
cripts
\a
ctivate

# On Mac/Linux:

source
venv/bin/activate

Enter fullscreen mode

Exit fullscreen mode

### Step 3: Install Dependencies

Createrequirements.txt:

fastapi
uvicorn
python-dotenv
python-multipart
pydantic
pydantic-settings
langchain
langchain-core
langchain-google-genai
tavily-python
Pillow

Enter fullscreen mode

Exit fullscreen mode

Install everything:

pip
install

--upgrade
 pip
pip
install

-r
 requirements.txt

Enter fullscreen mode

Exit fullscreen mode

## Understanding Environment Variables

Environment variables keep sensitive information (API keys) separate from your code. This is crucial for security (API keys never go into version control), flexibility (change settings without changing code), and deployment (different configs for dev/staging/production).

We usePydantic Settingsinstead ofos.getenv()because it provides automatic type validation, built-in default values, field descriptions, full IDE autocomplete support, and detailed error messages.

### Create.envFile

Create.envin thebackend/folder:

GOOGLE_API_KEY=AIzaSy...your_key_here
TAVILY_API_KEY=tvly-...your_key_here
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
GEMINI_MODEL=gemini-2.0-flash-exp
TEMPERATURE=0.7
MAX_TOKENS=2048

Enter fullscreen mode

Exit fullscreen mode

IMPORTANT:Add.envto your.gitignore:

echo

".env"

>>
 .gitignore

Enter fullscreen mode

Exit fullscreen mode

Create.env.example(for documentation):

GOOGLE_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:3000
GEMINI_MODEL=gemini-2.0-flash-exp
TEMPERATURE=0.7
MAX_TOKENS=2048

Enter fullscreen mode

Exit fullscreen mode

## Code Implementation

### Configuration Management

Createapp/config.py:

This file manages all settings and creates our AI model instances using Pydantic Settings for automatic validation and type safety.

import

os

from

pydantic_settings

import

BaseSettings

from

pydantic

import

Field

from

langchain_google_genai

import

ChatGoogleGenerativeAI

from

functools

import

lru_cache

class

Settings
(
BaseSettings
):


google_api_key
:

str

=

Field
(...,

description
=
"
Google Gemini API key
"
)


tavily_api_key
:

str

=

Field
(...,

description
=
"
Tavily API key
"
)


host
:

str

=

Field
(
default
=
"
0.0.0.0
"
)


port
:

int

=

Field
(
default
=
8000
)


cors_origins
:

str

=

Field
(
default
=
"
http://localhost:3000
"
)


gemini_model
:

str

=

Field
(
default
=
"
gemini-2.0-flash-exp
"
)


temperature
:

float

=

Field
(
default
=
0.7
,

ge
=
0.0
,

le
=
2.0
)


max_tokens
:

int

=

Field
(
default
=
2048
,

ge
=
100
,

le
=
8192
)


max_file_size
:

int

=

Field
(
default
=
10

*

1024

*

1024
)


class

Config
:


env_file

=

"
.env
"


case_sensitive

=

False


@property


def

cors_origins_list
(
self
):


return

[
origin
.
strip
()

for

origin

in

self
.
cors_origins
.
split
(
"
,
"
)]

settings

=

Settings
()

@lru_cache
()

def

load_google_llm
():


return

ChatGoogleGenerativeAI
(


model
=
settings
.
gemini_model
,


google_api_key
=
settings
.
google_api_key
,


temperature
=
settings
.
temperature
,


max_output_tokens
=
settings
.
max_tokens
,


convert_system_message_to_human
=
True


)

@lru_cache
()

def

load_google_vision_llm
():


return

ChatGoogleGenerativeAI
(


model
=
settings
.
gemini_model
,


google_api_key
=
settings
.
google_api_key
,


temperature
=
0.5
,


max_output_tokens
=
settings
.
max_tokens
,


convert_system_message_to_human
=
True


)

Enter fullscreen mode

Exit fullscreen mode

What's happening here:Pydantic Settings automatically reads the.envfile, validates field types and ranges, and the@lru_cachedecorator creates the model once and reuses it for better performance. We have two LLM functions: one for chat with higher temperature (more creative), and one for vision with lower temperature (more consistent text extraction).

### Data Models with Pydantic

Createapp/models/schemas.py:

These models define the shape of our data for both incoming requests and outgoing responses. FastAPI uses these for automatic validation and documentation generation.

from

pydantic

import

BaseModel
,

Field

from

datetime

import

datetime

class

HealthCheckResponse
(
BaseModel
):


status
:

str


timestamp
:

datetime


message
:

str

class

ChatRequest
(
BaseModel
):


message
:

str

=

Field
(...,

min_length
=
1
,

max_length
=
1000
)


language
:

str

=

Field
(
default
=
"
en
"
,

pattern
=
"
^(en|fr)$
"
)

class

ChatResponse
(
BaseModel
):


response
:

str


language
:

str


timestamp
:

datetime

class

AnalysisRequest
(
BaseModel
):


text
:

str

=

Field
(...,

min_length
=
1
)


context
:

str

=

Field
(
default
=
""
)


language
:

str

=

Field
(
default
=
"
en
"
)

class

MedicalAnalysis
(
BaseModel
):


summary
:

str


key_findings
:

list
[
str
]


recommendations
:

list
[
str
]


next_steps
:

list
[
str
]

class

AnalysisResponse
(
BaseModel
):


summary
:

str


key_findings
:

list
[
str
]


recommendations
:

list
[
str
]


next_steps
:

list
[
str
]


disclaimer
:

str


language
:

str


timestamp
:

datetime

class

ImageAnalysisResponse
(
BaseModel
):


extracted_text
:

str


analysis
:

AnalysisResponse

class

ResearchRequest
(
BaseModel
):


query
:

str

=

Field
(...,

min_length
=
3
,

max_length
=
200
)


max_results
:

int

=

Field
(
default
=
5
,

ge
=
1
,

le
=
10
)


language
:

str

=

Field
(
default
=
"
en
"
)

class

ResearchResult
(
BaseModel
):


title
:

str


url
:

str


content
:

str


score
:

float

class

ResearchResponse
(
BaseModel
):


query
:

str


results
:

list
[
ResearchResult
]


summary
:

str


timestamp
:

datetime

Enter fullscreen mode

Exit fullscreen mode

Key points:Field validation withmin_length,max_length, andpatternis automatically checked by FastAPI. TheMedicalAnalysismodel is used by LangChain'sPydanticOutputParserto force structured JSON output from the AI. Nested models likeImageAnalysisResponsecontainingAnalysisResponseallow complex data structures.

### LangChain Chains

Createapp/chains/chat_chain.py:

This implements the chat chain using LangChain Expression Language (LCEL). The chain connects prompt templates, the LLM, and output parsers in a clean, readable way.

from

langchain_core.prompts

import

ChatPromptTemplate

from

langchain_core.output_parsers

import

StrOutputParser

from

app.config

import

load_google_llm

def

create_chat_chain
(
language
:

str

=

"
en
"
):


llm

=

load_google_llm
()


if

language

==

"
fr
"
:


system_message

=

"""
Vous êtes MediCare AI, un assistant médical IA pour le Cameroun.

Vos responsabilités:
- Fournir des informations médicales précises et basées sur des preuves
- Expliquer les concepts médicaux en termes simples
- Toujours recommander de consulter un professionnel de santé qualifié
- Être culturellement sensible au contexte camerounais

IMPORTANT: Vous n
'
êtes PAS un médecin. Ne donnez jamais de diagnostic définitif.
"""


else
:


system_message

=

"""
You are MediCare AI, a medical AI assistant for Cameroon.

Your responsibilities:
- Provide accurate, evidence-based medical information
- Explain medical concepts in simple terms
- Always recommend consulting qualified healthcare professionals
- Be culturally sensitive to the Cameroonian context

IMPORTANT: You are NOT a doctor. Never provide definitive diagnoses.
"""


prompt

=

ChatPromptTemplate
.
from_messages
([


(
"
system
"
,

system_message
),


(
"
user
"
,

"
{user_question}
"
)


])


parser

=

StrOutputParser
()


chain

=

prompt

|

llm

|

parser


return

chain

def

get_chat_response
(
message
:

str
,

language
:

str

=

"
en
"
):


chain

=

create_chat_chain
(
language
)


response

=

chain
.
invoke
({
"
user_question
"
:

message
})


return

response

Enter fullscreen mode

Exit fullscreen mode

LCEL explained:The pipe operatorprompt | llm | parsercreates a chain where the output of each step becomes the input of the next. This is cleaner than manually calling each component and provides built-in async support, error handling, and streaming capabilities.

Createapp/chains/analysis_chain.py:

This chain produces structured JSON output usingPydanticOutputParser, which forces the LLM to output data matching ourMedicalAnalysismodel.

from

langchain_core.prompts

import

ChatPromptTemplate

from

langchain_core.output_parsers

import

PydanticOutputParser

from

app.config

import

load_google_llm

from

app.models.schemas

import

MedicalAnalysis

def

create_analysis_chain
(
language
:

str

=

"
en
"
):


llm

=

load_google_llm
()


parser

=

PydanticOutputParser
(
pydantic_object
=
MedicalAnalysis
)


format_instructions

=

parser
.
get_format_instructions
()


if

language

==

"
fr
"
:


system_message

=

"""
Vous êtes un assistant médical IA analysant des dossiers médicaux.
Fournissez des informations claires, précises et actionnables.
Restez objectif et recommandez toujours une consultation médicale professionnelle.
"""


user_template

=

"""
Analysez ce dossier médical et fournissez une analyse structurée:

Dossier Médical:
{medical_text}

Contexte Additionnel:
{context}

{format_instructions}

Répondez UNIQUEMENT en JSON valide.
"""


else
:


system_message

=

"""
You are a medical AI assistant analyzing medical records.
Provide clear, accurate, and actionable insights.
Stay objective and always recommend professional medical consultation.
"""


user_template

=

"""
Analyze this medical record and provide a structured analysis:

Medical Record:
{medical_text}

Additional Context:
{context}

{format_instructions}

Respond ONLY with valid JSON.
"""


prompt

=

ChatPromptTemplate
.
from_messages
([


(
"
system
"
,

system_message
),


(
"
user
"
,

user_template
)


])


prompt

=

prompt
.
partial
(
format_instructions
=
format_instructions
)


chain

=

prompt

|

llm

|

parser


return

chain

def

analyze_medical_record
(
text
:

str
,

context
:

str

=

""
,

language
:

str

=

"
en
"
):


chain

=

create_analysis_chain
(
language
)


try
:


result

=

chain
.
invoke
({


"
medical_text
"
:

text
,


"
context
"
:

context

if

context

else

"
No additional context provided
"


})


return

result


except

Exception

as

e
:


print
(
f
"
Analysis error:
{
e
}
"
)


return

MedicalAnalysis
(


summary
=
f
"
Analysis completed but encountered formatting issues:
{
str
(
e
)[
:
200
]
}
"
,


key_findings
=
[
"
Analysis was performed but results need manual review
"
],


recommendations
=
[
"
Consult with a healthcare professional for detailed interpretation
"
],


next_steps
=
[
"
Schedule appointment with your doctor
"
,

"
Keep this record for your medical history
"
]


)

Enter fullscreen mode

Exit fullscreen mode

PydanticOutputParser magic:It automatically generates detailed JSON schema instructions that tell the LLM exactly how to format its response. The parser then validates the output and converts it to a Python object. The try-except block ensures we always return something useful, even if JSON parsing fails.

### Service Layer

Createapp/services/gemini_service.py:

This service handles vision-specific tasks like extracting text from medical record images.

from

langchain_core.messages

import

HumanMessage

from

app.config

import

load_google_vision_llm

import

base64

import

json

class

GeminiService
:


def

__init__
(
self
):


self
.
vision_llm

=

load_google_vision_llm
()


def

extract_text_from_image
(
self
,

image_bytes
:

bytes
):


try
:


image_b64

=

base64
.
b64encode
(
image_bytes
).
decode
(
'
utf-8
'
)


extraction_prompt

=

"""
You are a medical text extractor. Extract ALL text from this medical document/record.

Include:
- Patient information
- Test results
- Doctor
'
s notes
- Prescriptions
- Dates and measurements
- Any handwritten text

Format the output clearly and preserve the structure. If text is unclear, indicate with [unclear].

Extract all text now:
"""


message

=

HumanMessage
(


content
=
[


{
"
type
"
:

"
text
"
,

"
text
"
:

extraction_prompt
},


{
"
type
"
:

"
image_url
"
,

"
image_url
"
:

f
"
data:image/jpeg;base64,
{
image_b64
}
"
}


]


)


response

=

self
.
vision_llm
.
invoke
([
message
])


return

response
.
content


except

Exception

as

e
:


raise

Exception
(
f
"
Image text extraction error:
{
str
(
e
)
}
"
)


def

analyze_image_directly
(
self
,

image_bytes
:

bytes
,

language
:

str

=

"
en
"
):


try
:


image_b64

=

base64
.
b64encode
(
image_bytes
).
decode
(
'
utf-8
'
)


if

language

==

"
fr
"
:


prompt

=

"""
Analysez cette image de dossier médical et fournissez une analyse au format JSON avec ces clés:
- summary: Aperçu bref de ce que vous voyez
- key_findings: Liste des résultats importants
- recommendations: Recommandations de santé
- next_steps: Actions suggérées

Répondez UNIQUEMENT en JSON valide.
"""


else
:


prompt

=

"""
Analyze this medical record image and provide analysis in JSON format with these keys:
- summary: Brief overview of what you see
- key_findings: List of important findings
- recommendations: Health recommendations
- next_steps: Suggested actions

Respond ONLY with valid JSON.
"""


message

=

HumanMessage
(


content
=
[


{
"
type
"
:

"
text
"
,

"
text
"
:

prompt
},


{
"
type
"
:

"
image_url
"
,

"
image_url
"
:

f
"
data:image/jpeg;base64,
{
image_b64
}
"
}


]


)


response

=

self
.
vision_llm
.
invoke
([
message
])


result

=

json
.
loads
(
response
.
content
)


return

result


except

json
.
JSONDecodeError
:


return

{


"
summary
"
:

response
.
content
[:
500
],


"
key_findings
"
:

[
"
Analysis completed - see summary
"
],


"
recommendations
"
:

[
"
Consult with a healthcare professional
"
],


"
next_steps
"
:

[
"
Schedule appointment with your doctor
"
]


}


except

Exception

as

e
:


raise

Exception
(
f
"
Image analysis error:
{
str
(
e
)
}
"
)

gemini_service

=

GeminiService
()

Enter fullscreen mode

Exit fullscreen mode

Why base64?LangChain requires images in base64 format, which is the standard way to encode binary data as text. TheHumanMessageformat withtype: "image_url"is how LangChain handles multimodal content (text + images).

Createapp/services/tavily_service.py:

This service handles medical research searches using Tavily's AI-powered search engine.

from

tavily

import

TavilyClient

from

app.config

import

settings

class

TavilyService
:


def

__init__
(
self
):


self
.
client

=

TavilyClient
(
api_key
=
settings
.
tavily_api_key
)


def

search_medical_research
(
self
,

query
:

str
,

max_results
:

int

=

5
):


try
:


response

=

self
.
client
.
search
(


query
=
f
"
medical research
{
query
}
"
,


search_depth
=
"
advanced
"
,


max_results
=
max_results
,


include_domains
=
[


"
pubmed.ncbi.nlm.nih.gov
"
,


"
nih.gov
"
,


"
who.int
"
,


"
cdc.gov
"
,


"
mayoclinic.org
"
,


"
webmd.com
"
,


"
healthline.com
"
,


"
medicalnewstoday.com
"


]


)


return

response


except

Exception

as

e
:


raise

Exception
(
f
"
Research search error:
{
str
(
e
)
}
"
)


def

format_results
(
self
,

raw_results
):


formatted

=

[]


for

result

in

raw_results
.
get
(
"
results
"
,

[]):


formatted
.
append
({


"
title
"
:

result
.
get
(
"
title
"
,

"
Untitled
"
),


"
url
"
:

result
.
get
(
"
url
"
,

""
),


"
content
"
:

result
.
get
(
"
content
"
,

""
)[:
500
],


"
score
"
:

result
.
get
(
"
score
"
,

0.0
)


})


return

formatted

tavily_service

=

TavilyService
()

Enter fullscreen mode

Exit fullscreen mode

Domain filtering:By specifyinginclude_domains, we ensure results only come from trusted medical sources, avoiding blogs, forums, or unreliable websites.

### API Routes

Createapp/routes/health.py:

from

fastapi

import

APIRouter

from

app.models.schemas

import

HealthCheckResponse

from

datetime

import

datetime

router

=

APIRouter
(
prefix
=
"
/api
"
,

tags
=
[
"
Health
"
])

@router.get
(
"
/health
"
,

response_model
=
HealthCheckResponse
)

async

def

health_check
():


return

HealthCheckResponse
(


status
=
"
healthy
"
,


timestamp
=
datetime
.
now
(),


message
=
"
MediCare AI Backend is running!
"


)

Enter fullscreen mode

Exit fullscreen mode

Createapp/routes/analysis.py:

from

fastapi

import

APIRouter
,

UploadFile
,

File
,

Form
,

HTTPException

from

app.models.schemas

import

(


ChatRequest
,

ChatResponse
,


AnalysisRequest
,

AnalysisResponse
,


ImageAnalysisResponse

)

from

app.chains.chat_chain

import

get_chat_response

from

app.chains.analysis_chain

import

analyze_medical_record

from

app.services.gemini_service

import

gemini_service

from

datetime

import

datetime

router

=

APIRouter
(
prefix
=
"
/api
"
,

tags
=
[
"
Analysis
"
])

@router.post
(
"
/chat
"
,

response_model
=
ChatResponse
)

async

def

chat_with_ai
(
request
:

ChatRequest
):


try
:


response_text

=

get_chat_response
(


message
=
request
.
message
,


language
=
request
.
language


)


return

ChatResponse
(


response
=
response_text
,


language
=
request
.
language
,


timestamp
=
datetime
.
now
()


)


except

Exception

as

e
:


raise

HTTPException
(
status_code
=
500
,

detail
=
f
"
Chat error:
{
str
(
e
)
}
"
)

@router.post
(
"
/analyze-text
"
,

response_model
=
AnalysisResponse
)

async

def

analyze_medical_text
(
request
:

AnalysisRequest
):


try
:


analysis

=

analyze_medical_record
(


text
=
request
.
text
,


context
=
request
.
context
,


language
=
request
.
language


)


disclaimer

=

(


"
This analysis is for informational purposes only.
"


"
Always consult qualified healthcare professionals for medical advice.
"


)


return

AnalysisResponse
(


summary
=
analysis
.
summary
,


key_findings
=
analysis
.
key_findings
,


recommendations
=
analysis
.
recommendations
,


next_steps
=
analysis
.
next_steps
,


disclaimer
=
disclaimer
,


language
=
request
.
language
,


timestamp
=
datetime
.
now
()


)


except

Exception

as

e
:


raise

HTTPException
(
status_code
=
500
,

detail
=
f
"
Analysis error:
{
str
(
e
)
}
"
)

@router.post
(
"
/analyze-image
"
,

response_model
=
ImageAnalysisResponse
)

async

def

analyze_medical_image
(


file
:

UploadFile

=

File
(...),


language
:

str

=

Form
(
default
=
"
en
"
),


extract_text_only
:

bool

=

Form
(
default
=
False
)

):


if

not

file
.
content_type
.
startswith
(
"
image/
"
):


raise

HTTPException
(
status_code
=
400
,

detail
=
"
File must be an image
"
)


try
:


image_bytes

=

await

file
.
read
()


extracted_text

=

gemini_service
.
extract_text_from_image
(
image_bytes
)


if

extract_text_only
:


return

ImageAnalysisResponse
(


extracted_text
=
extracted_text
,


analysis
=
AnalysisResponse
(


summary
=
"
Text extraction completed
"
,


key_findings
=
[],


recommendations
=
[],


next_steps
=
[
"
Review the extracted text
"
,

"
Analyze if needed
"
],


disclaimer
=
"
Text extraction only - no analysis performed
"
,


language
=
language
,


timestamp
=
datetime
.
now
()


)


)


analysis

=

analyze_medical_record
(
text
=
extracted_text
,

language
=
language
)


disclaimer

=

(


"
This analysis is for informational purposes only.
"


"
Always consult qualified healthcare professionals for medical advice.
"


)


return

ImageAnalysisResponse
(


extracted_text
=
extracted_text
,


analysis
=
AnalysisResponse
(


summary
=
analysis
.
summary
,


key_findings
=
analysis
.
key_findings
,


recommendations
=
analysis
.
recommendations
,


next_steps
=
analysis
.
next_steps
,


disclaimer
=
disclaimer
,


language
=
language
,


timestamp
=
datetime
.
now
()


)


)


except

Exception

as

e
:


raise

HTTPException
(
status_code
=
500
,

detail
=
f
"
Image analysis error:
{
str
(
e
)
}
"
)

@router.post
(
"
/extract-text
"
)

async

def

extract_text_from_image
(
file
:

UploadFile

=

File
(...)):


if

not

file
.
content_type
.
startswith
(
"
image/
"
):


raise

HTTPException
(
status_code
=
400
,

detail
=
"
File must be an image
"
)


try
:


image_bytes

=

await

file
.
read
()


extracted_text

=

gemini_service
.
extract_text_from_image
(
image_bytes
)


return

{


"
extracted_text
"
:

extracted_text
,


"
timestamp
"
:

datetime
.
now
()


}


except

Exception

as

e
:


raise

HTTPException
(
status_code
=
500
,

detail
=
f
"
Text extraction error:
{
str
(
e
)
}
"
)

Enter fullscreen mode

Exit fullscreen mode

Two-step image processing:We first extract text using Gemini Vision (OCR), then analyze that text using our LangChain analysis chain. This provides more reliable results than single-step analysis.

Createapp/routes/research.py:

from

fastapi

import

APIRouter
,

HTTPException

from

app.models.schemas

import

ResearchRequest
,

ResearchResponse
,

ResearchResult

from

app.services.tavily_service

import

tavily_service

from

app.chains.chat_chain

import

get_chat_response

from

datetime

import

datetime

router

=

APIRouter
(
prefix
=
"
/api
"
,

tags
=
[
"
Research
"
])

@router.post
(
"
/research
"
,

response_model
=
ResearchResponse
)

async

def

search_medical_research
(
request
:

ResearchRequest
):


try
:


raw_results

=

tavily_service
.
search_medical_research
(


query
=
request
.
query
,


max_results
=
request
.
max_results


)


formatted_results

=

tavily_service
.
format_results
(
raw_results
)


results_text

=

"
\n\n
"
.
join
([


f
"
Source:
{
r
[
'
title
'
]
}
\n
{
r
[
'
content
'
]
}
"


for

r

in

formatted_results
[:
3
]


])


summary_prompt

=

f
"""
Based on these medical research results, provide a brief summary in 2-3 sentences:

{
results_text
}

Focus on the key takeaways and most important information.
"""


summary

=

get_chat_response
(
summary_prompt
,

request
.
language
)


research_results

=

[


ResearchResult
(


title
=
r
[
"
title
"
],


url
=
r
[
"
url
"
],


content
=
r
[
"
content
"
],


score
=
r
[
"
score
"
]


)


for

r

in

formatted_results


]


return

ResearchResponse
(


query
=
request
.
query
,


results
=
research_results
,


summary
=
summary
,


timestamp
=
datetime
.
now
()


)


except

Exception

as

e
:


raise

HTTPException
(
status_code
=
500
,

detail
=
f
"
Research error:
{
str
(
e
)
}
"
)

Enter fullscreen mode

Exit fullscreen mode

Why combine Tavily + LangChain?Tavily finds accurate, cited sources from trusted medical databases, while LangChain generates an easy-to-read summary. Users get both detailed sources and a quick overview.

### Main Application

Createapp/main.py:

from

fastapi

import

FastAPI

from

fastapi.middleware.cors

import

CORSMiddleware

from

app.config

import

settings

from

app.routes

import

health
,

analysis
,

research

app

=

FastAPI
(


title
=
"
MediCare AI Backend
"
,


description
=
"
Medical AI Assistant API for Cameroon - Powered by LangChain
"
,


version
=
"
2.0.0
"
,


docs_url
=
"
/docs
"
,


redoc_url
=
"
/redoc
"

)

app
.
add_middleware
(


CORSMiddleware
,


allow_origins
=
settings
.
cors_origins_list
,


allow_credentials
=
True
,


allow_methods
=
[
"
*
"
],


allow_headers
=
[
"
*
"
],

)

app
.
include_router
(
health
.
router
)

app
.
include_router
(
analysis
.
router
)

app
.
include_router
(
research
.
router
)

@app.get
(
"
/
"
)

async

def

root
():


return

{


"
message
"
:

"
Welcome to MediCare AI Backend
"
,


"
version
"
:

"
2.0.0
"
,


"
powered_by
"
:

"
LangChain + Google Gemini
"
,


"
docs
"
:

"
/docs
"
,


"
status
"
:

"
running
"


}

Enter fullscreen mode

Exit fullscreen mode

CORS explained:Cross-Origin Resource Sharing allows your frontend (React, Next.js) to make requests to this backend API. Without CORS middleware, browsers would block these requests for security reasons.

## Running the Application

### Final Setup Steps

1. Ensure you're in thebackenddirectory
2. Activate your virtual environment
3. Verify your.envfile has valid API keys
4. Start the server:

uvicorn app.main:app
--reload

Enter fullscreen mode

Exit fullscreen mode

The--reloadflag enables hot-reloading during development, so the server automatically restarts when you change code.

You should see output like:

INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO: Started reloader process
INFO: Application startup complete.

Enter fullscreen mode

Exit fullscreen mode

### Access the API

Open your browser to:

1. Interactive Documentation:http://localhost:8000/docs(Swagger UI)
2. Alternative Documentation:http://localhost:8000/redoc(ReDoc)
3. Root Endpoint:http://localhost:8000/

The/docsendpoint is particularly useful - it provides an interactive interface where you can test all endpoints directly in your browser.

## Testing Your API with Swagger UI

Testing your API has never been easier, thanks to FastAPI's automatically generated interactive documentation powered by Swagger UI. This built-in testing interface allows you to explore and test every endpoint without writing a single line of code or using command-line tools.

## Accessing Swagger UI

Once your server is running, open your browser and navigate to:

http://localhost:8000/docs

You'll see a beautiful, interactive interface that lists all your API endpoints organized by tags (Health, Analysis, Research). This documentation is automatically generated from your code, including all request/response models, field validations, and descriptions.

## Understanding the Swagger Interface

The Swagger UI displays:

* Endpoint paths- The URL for each API route
* HTTP methods- GET, POST, etc., color-coded for easy identification
* Request schemas- Expected input format with field types and validation rules
* Response schemas- What you'll get back, including status codes
* Try it out- Interactive testing functionality

## Testing Each Endpoint

### Test 1: Health Check (GET)

Let's start with the simplest endpoint to verify everything is working:

1. Locate theHealthsection
2. Click onGET /api/healthto expand it
3. Click the"Try it out"button (top right)
4. Click the blue"Execute"button
5. Scroll down to see theResponse

You should see a JSON response like:

{


"status"
:

"healthy"
,


"timestamp"
:

"2025-09-30T14:23:45.123456"
,


"message"
:

"MediCare AI Backend is running!"

}

Enter fullscreen mode

Exit fullscreen mode

What this tells you:Your FastAPI server is running correctly, and the basic routing is working.

### Test 2: Medical Chat (POST)

Now let's test the conversational AI capabilities:

1. FindPOST /api/chatunder theAnalysissection
2. Click to expand, then click"Try it out"
3. You'll see aRequest bodytext area with example JSON
4. Replace the example with your own question:

{


"message"
:

"What are the early signs of diabetes?"
,


"language"
:

"en"

}

Enter fullscreen mode

Exit fullscreen mode

1. Click"Execute"
2. Examine the response below

Expected response structure:

{


"response"
:

"Early signs of diabetes include frequent urination..."
,


"language"
:

"en"
,


"timestamp"
:

"2025-09-30T14:25:30.456789"

}

Enter fullscreen mode

Exit fullscreen mode

Try this too:Test the bilingual capability by changing"language": "fr"and asking the same question in French.

### Test 3: Text Analysis (POST)

This endpoint analyzes medical text and provides structured insights:

1. Navigate toPOST /api/analyze-text
2. Click"Try it out"
3. Enter sample medical data:

{


"text"
:

"Patient presents with elevated blood pressure (150/95 mmHg), fasting blood sugar of 126 mg/dL, and BMI of 32. Patient reports frequent headaches and fatigue."
,


"context"
:

"45-year-old male, sedentary lifestyle"
,


"language"
:

"en"

}

Enter fullscreen mode

Exit fullscreen mode

1. Click"Execute"

What to observe in the response:

* summary- A concise overview of the medical findings
* key_findings- Structured list of important observations
* recommendations- Health advice based on the data
* next_steps- Actionable items for the patient
* disclaimer- Legal/medical disclaimer

This demonstrates LangChain'sPydanticOutputParserin action - forcing the AI to return perfectly structured JSON every time.

### Test 4: Image Text Extraction (POST)

This is where Gemini Vision shines - extracting text from medical records, prescriptions, or lab reports:

1. FindPOST /api/extract-text
2. Click"Try it out"
3. You'll see afile uploadbutton - click to select an image
4. Choose a medical document image (prescription, lab report, or even handwritten notes)
5. Click"Execute"
6. Wait a few seconds for processing

Response format:

{


"extracted_text"
:

"Patient Name: John Doe
\n
Date: 2025-09-28
\n
Blood Test Results:
\n
Hemoglobin: 14.2 g/dL
\n
White Blood Cells: 7,500/μL
\n
..."
,


"timestamp"
:

"2025-09-30T14:30:15.789012"

}

Enter fullscreen mode

Exit fullscreen mode

Pro tip:Test with different image types - printed documents, handwritten prescriptions, photos of medical records - to see the OCR capabilities in action.

### Test 5: Full Image Analysis (POST)

This combines text extraction with AI analysis for complete medical record interpretation:

1. Go toPOST /api/analyze-image
2. Click"Try it out"
3. Upload a medical record image using thefileparameter
4. Setlanguageto "en" (or "fr" for French)
5. Leaveextract_text_onlyasfalse(unchecked)
6. Click"Execute"

Response structure:

{


"extracted_text"
:

"The complete OCR text from your image..."
,


"analysis"
:

{


"summary"
:

"This blood test shows..."
,


"key_findings"
:

[


"Hemoglobin levels are within normal range"
,


"Slightly elevated glucose levels detected"


],


"recommendations"
:

[


"Monitor blood sugar levels regularly"
,


"Consider dietary modifications"


],


"next_steps"
:

[


"Schedule follow-up in 3 months"
,


"Consult with an endocrinologist"


],


"disclaimer"
:

"This analysis is for informational purposes only..."
,


"language"
:

"en"
,


"timestamp"
:

"2025-09-30T14:35:42.345678"


}

}

Enter fullscreen mode

Exit fullscreen mode

What's happening behind the scenes:

1. Gemini Vision extracts all text from the image (OCR)
2. The extracted text is fed to the analysis chain
3. LangChain formats the output into structured JSON
4. You get both the raw text AND intelligent analysis

### Test 6: Medical Research Search (POST)

This endpoint searches trusted medical databases and summarizes findings:

1. LocatePOST /api/research
2. Click"Try it out"
3. Enter a research query:

{


"query"
:

"latest treatments for hypertension"
,


"max_results"
:

5
,


"language"
:

"en"

}

Enter fullscreen mode

Exit fullscreen mode

1. Click"Execute"
2. Wait for the search to complete (may take 5-10 seconds)

Response breakdown:

{


"query"
:

"latest treatments for hypertension"
,


"results"
:

[


{


"title"
:

"New Guidelines for Hypertension Treatment"
,


"url"
:

"https://pubmed.ncbi.nlm.nih.gov/..."
,


"content"
:

"Recent studies show that combination therapy..."
,


"score"
:

0.95


}


],


"summary"
:

"Recent research indicates that combination therapy with ACE inhibitors and calcium channel blockers shows promising results..."
,


"timestamp"
:

"2025-09-30T14:40:18.901234"

}

Enter fullscreen mode

Exit fullscreen mode

Key features:

* Trusted sources- Only results from medical databases (PubMed, WHO, CDC, etc.)
* Relevance scores- Higher scores mean more relevant results
* AI-generated summary- LangChain reads the top results and creates a concise summary
* Source citations- Every result includes the original URL

## Understanding Response Codes

Swagger UI shows HTTP status codes for each response:

* 200 OK- Request succeeded, here's your data
* 400 Bad Request- Your input didn't pass validation (check field requirements)
* 422 Unprocessable Entity- JSON structure is wrong or missing required fields
* 500 Internal Server Error- Something went wrong on the server (check logs)

When you see errors, Swagger UI displays the error details, making debugging straightforward.

## Advanced Testing Tips

### Test Field Validation

FastAPI automatically validates inputs based on your Pydantic models. Try breaking things intentionally:

1. Test minimum length:Try sending a chat message with just "hi" (below min_length)
2. Test maximum length:Send a 2000-character message (above max_length)
3. Test invalid language:Set language to "es" instead of "en" or "fr"
4. Test invalid file types:Upload a PDF to an image endpoint

Each test will return a detailed validation error explaining exactly what went wrong.

### Test the Alternative Documentation

FastAPI also generates ReDoc documentation athttp://localhost:8000/redoc. This provides:

* A cleaner, more readable layout
* Easier navigation for large APIs
* Better for sharing with frontend developers
* No testing capability (documentation only)

### Use Swagger's Schema Models

Click on anySchemaat the bottom of the Swagger UI page to see the complete data structure for requests and responses. This is invaluable when building a frontend or understanding the API contract.

### Monitor Server Logs

While testing in Swagger UI, watch your terminal where uvicorn is running. You'll see:

* Incoming requests with HTTP methods and paths
* Response status codes
* Any error tracebacks
* Processing times for each request

This real-time feedback helps you understand what's happening under the hood.

## Common Testing Scenarios

### Scenario 1: Patient Symptom Checker

1. Use/api/chatwith: "I have a persistent cough and fever for 3 days"
2. Observe how the AI provides information while recommending professional consultation

### Scenario 2: Lab Report Analysis

1. Upload a blood test image to/api/analyze-image
2. Review the extracted values and AI interpretation
3. Check that it flags abnormal results inkey_findings

### Scenario 3: Research Before Doctor Visit

1. Use/api/researchwith: "treatment options for type 2 diabetes"
2. Review the cited sources from medical journals
3. Read the AI-generated summary for quick understanding

### Scenario 4: Medication Information

1. Upload a prescription image to/api/extract-text
2. Copy the extracted medication names
3. Use/api/researchto learn about each medication

## Troubleshooting Test Failures

"Module not found" errors:

* Ensure all dependencies are installed:pip install -r requirements.txt
* Verify your virtual environment is activated

"Invalid API key" errors:

* Check your.envfile has valid keys
* Regenerate keys if necessary (links in Prerequisites section)

Image upload fails:

* Verify file is actually an image (JPEG, PNG)
* Check file size isn't too large (default limit: 10MB)
* Ensure file isn't corrupted

Slow response times:

* Vision and research endpoints take 5-15 seconds (normal)
* Check your internet connection for Tavily searches
* Monitor API rate limits if testing repeatedly

JSON parsing errors:

* Sometimes the LLM returns invalid JSON
* The code has fallback handlers for this
* Try rephrasing your query for better results

## Learning Resources

Now that you've built and tested a production-ready AI medical assistant, here are curated resources to deepen your understanding and expand your skills.

## Official Documentation

### Core Technologies

FastAPI- Modern, fast web framework for building APIs

* Official Docs:https://fastapi.tiangolo.com/
* Tutorial:https://fastapi.tiangolo.com/tutorial/
* Best Practices:https://fastapi.tiangolo.com/advanced/

LangChain- Framework for developing applications powered by LLMs

* Documentation:https://python.langchain.com/docs/get_started/introduction
* LCEL Guide:https://python.langchain.com/docs/expression_language/
* How-to Guides:https://python.langchain.com/docs/how_to/

Pydantic- Data validation using Python type annotations

* Documentation:https://docs.pydantic.dev/latest/
* Settings Management:https://docs.pydantic.dev/latest/concepts/pydantic_settings/
* Validation Guide:https://docs.pydantic.dev/latest/concepts/validators/

### AI Services

Google Gemini- Multimodal AI model (text + vision)

* API Documentation:https://ai.google.dev/docs
* Gemini API Cookbook:https://github.com/google-gemini/cookbook
* Vision Examples:https://ai.google.dev/tutorials/python_quickstart

Tavily AI- AI-powered search API for developers

* Documentation:https://docs.tavily.com/
* Python SDK:https://github.com/tavily-ai/tavily-python
* Search Examples:https://docs.tavily.com/docs/python-sdk/examples

## Video Tutorials

### FastAPI Mastery

* FastAPI Complete Courseby freeCodeCamp (4 hours):https://www.youtube.com/watch?v=0sOvCWFmrtA
* Building Production APIs with FastAPIby ArjanCodes:https://www.youtube.com/watch?v=SORiTsvnU28
* FastAPI + React Full Stackby Coding with Roby:https://www.youtube.com/watch?v=yWThSl1LVTs

### LangChain Deep Dives

* LangChain Crash Courseby Krish Naik:https://www.youtube.com/watch?v=_FpT1cwcSLg
* LangChain Expression Language (LCEL)by LangChain:https://www.youtube.com/watch?v=gKUoHhHvAZE
* Building Production LangChain Appsby Sam Witteveen:https://www.youtube.com/watch?v=k8TzFKmj56A

### AI Integration

* Google Gemini API Tutorial:https://www.youtube.com/watch?v=9PKbgWDrN8c
* Building AI Applications with Gemini:https://www.youtube.com/watch?v=5qiJGY9vshQ
* Multimodal AI with Vision LLMs:https://www.youtube.com/watch?v=wZcxuS8V_N8

## Interactive Learning Platforms

LangChain Academy(Free)

* Interactive courses on LangChain fundamentals
* Hands-on exercises with real code
* https://academy.langchain.com/

Google AI Studio(Free)

* Experiment with Gemini models directly
* Test prompts without writing code
* https://makersuite.google.com/

FastAPI Interactive Tutorial(Free)

* Learn by building actual projects
* Built into FastAPI documentation
* https://fastapi.tiangolo.com/tutorial/

## Books & Written Guides

"Designing Data-Intensive Applications"by Martin Kleppmann

* Understanding system architecture
* Building scalable backends
* Essential for production systems

"Prompt Engineering Guide"(Free Online)

* Comprehensive guide to AI prompting
* LangChain-specific techniques
* https://www.promptingguide.ai/

"The Pragmatic Programmer"by Andy Hunt & Dave Thomas

* Software engineering best practices
* Writing maintainable code
* Career-long reference book

## GitHub Repositories to Study

LangChain Templates

* Pre-built application templates
* https://github.com/langchain-ai/langchain/tree/master/templates

FastAPI Best Practices

* Project structure examples
* https://github.com/zhanymkanov/fastapi-best-practices

Production-Ready FastAPI

* Real-world application example
* https://github.com/tiangolo/full-stack-fastapi-postgresql

Gemini Cookbook

* Code examples for Gemini API
* https://github.com/google-gemini/cookbook

## Communities & Forums

LangChain Discord

* Active developer community
* Get help with specific issues
* https://discord.gg/langchain

FastAPI GitHub Discussions

* Official FastAPI community
* Feature requests and discussions
* https://github.com/tiangolo/fastapi/discussions

r/LangChain (Reddit)

* Community showcase and help
* https://reddit.com/r/LangChain

Stack Overflow

* Search:[fastapi],[langchain],[pydantic]
* Ask specific technical questions

## Advanced Topics to Explore

### After Mastering the Basics

1. Vector Databases & RAG

* Store medical documents in vector databases
* Implement Retrieval-Augmented Generation
* LangChain + Pinecone/Chroma/FAISS tutorials

2. Streaming Responses

* Real-time AI responses as they're generated
* FastAPI Server-Sent Events (SSE)
* LangChain streaming callbacks

3. Authentication & Authorization

* Secure your API with JWT tokens
* User management and permissions
* FastAPI Security documentation

4. Production Deployment

* Docker containerization
* Cloud deployment (AWS, GCP, Azure)
* CI/CD pipelines with GitHub Actions

5. Monitoring & Observability

* LangSmith for LangChain tracing
* Application performance monitoring (APM)
* Error tracking with Sentry

6. Testing & Quality Assurance

* Unit tests with pytest
* Integration tests for API endpoints
* LangChain testing utilities

## Follow These Experts

Twitter/X:

* @langchainai - LangChain updates
* @tiangolo- FastAPI creator
* @samuelcolvin- Pydantic creator
* @GoogleDeepMind - Gemini news

YouTube Channels:

* LangChain Official
* ArjanCodes (Python best practices)
* Krish Naik (AI tutorials)
* Patrick Loeber (Python & AI)

## Free API Credits & Tools

Google Cloud Free Tier

* $300 credit for new users
* Free Gemini API tier available
* https://cloud.google.com/free

Tavily AI

* 1000 free searches/month
* No credit card required
* https://tavily.com

Vercel/Railway/Render

* Free hosting for hobby projects
* Deploy FastAPI apps for free
* Easy CI/CD integration

## Final Advice

Start Small, Think Big:Begin with simple features, then gradually add complexity. The architecture we've built scales from prototype to production.

Read Other People's Code:The best way to improve is studying production codebases. All the repos listed above are excellent learning resources.

Build in Public:Share your progress on Twitter, LinkedIn, or GitHub. The community is supportive, and you'll get valuable feedback.

Focus on Fundamentals:Before chasing the latest AI model or framework, master Python, HTTP, APIs, and data structures. These never go out of style.

Keep Learning:AI technology evolves rapidly. Set aside time weekly to read documentation, watch tutorials, or experiment with new features.

Contribute Back:Once comfortable, contribute to open-source projects like LangChain or FastAPI. It's the best way to master a technology deeply.

## Github Repo

code here_______________

Github Repository

Good luck on your journey building AI-powered applications!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
