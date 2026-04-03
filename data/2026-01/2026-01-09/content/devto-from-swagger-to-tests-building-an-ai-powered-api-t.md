---
title: 'From Swagger to Tests: Building an AI-Powered API Test Generator with Python - DEV Community'
url: https://dev.to/m4rri4nne/from-swagger-to-tests-building-an-ai-powered-api-test-generator-with-python-3mf8
site_name: devto
fetched_at: '2026-01-09T11:07:47.614691'
original_url: https://dev.to/m4rri4nne/from-swagger-to-tests-building-an-ai-powered-api-test-generator-with-python-3mf8
author: Alicia Marianne 🇧🇷
date: '2026-01-03'
description: Working as a QA with APIs can be… well, kind of a nightmare sometimes. APIs are always changing,... Tagged with python, ai, api, testing.
tags: '#python, #ai, #api, #testing'
---

Working as a QA with APIs can be… well, kind of a nightmare sometimes. APIs are always changing, endpoints get added, status codes get updated, and keeping your tests in sync feels like chasing a moving target.

If you only look at your task board, it’s easy to lose track of what actually changed and what still needs testing.

In the projects I worked on, we had Swagger available for the API. And I thought:wait a minute… why not use AI and Swagger to save time generating tests?

And that’s how this little project started. In this post, I’ll walk you through how I did it, the challenges I faced, and some cool things you can do next.

## The Idea

The goal was simple: take the Swagger spec and extract all the useful info, like:

* HTTP methods
* Expected status codes
* Query parameters
* Request bodies

…and then generateboth positive and negative test scenariosautomatically.

For example, for a simpleGET /users/{id}endpoint, I wanted the output to look like this:

GET /users/
{
id
}

✔ Scenario: Retrieve a user with a valid ID
✔ Scenario: Validate 404
for
user not found
✘ Scenario: Missing ID parameter
✘ Scenario: Invalid format
for
ID

Enter fullscreen mode

Exit fullscreen mode

To make this work nicely, I used AI to create the scenarios based on the endpoint’s Swagger specification, following a template I defined.

## About the project

### Stack

* Python– fast, easy to parse data, integrate stuff
* Rich / Typer (CLI UX)– because a pretty CLI makes life better
* Gemini AI– super simple Python integration for AI prompts
* dotenv– to keep the AI keys safe

### Project Structure

api-test-generator/
├── README.md # Documentation of the project
├── requirements.txt # Dependências Python
├── main.py # Main function
│
├── output/ # Folder with generated tests
│ ├── get_Books.txt
│ ├── post_Books.txt
│
├── functions/ # Main functions of the project
│ ├── navigation.py # CLI navigation
│ ├── read_swagger.py # Read files and URL swaggers
│ └── test_generator.py # Generate tests and save them in the files
│
└── assets/ # theme and example for the project
 ├── swaggerexample.json
 └── theme.py

Enter fullscreen mode

Exit fullscreen mode

### How it works

┌──────────────────────────────┐
│ User / QA │
│ (CLI Interaction - Rich) │
└──────────────┬───────────────┘
 │
 ▼
┌──────────────────────────────┐
│ CLI Interface │
│ (Typer + Rich Menu) │
└──────────────┬───────────────┘
 │
 ▼
┌──────────────────────────────┐
│ Swagger/OpenAPI Loader │
│ - URL, Manual, or Local JSON│
│ - Validation & Parsing │
└──────────────┬───────────────┘
 │
 ▼
┌──────────────────────────────┐
│ API Specification Parser │
│ - Endpoints │
│ - Methods │
│ - Parameters │
│ - Responses / Status Codes │
└──────────────┬───────────────┘
 │
 ▼
┌──────────────────────────────┐
│ Gemini AI API │
│ (Test Case Generation) │
└──────────────┬───────────────┘
 │
 ▼
┌──────────────────────────────┐
│ Output Generator │
│ - Text file export (.txt) │
│ - Structured scenarios │
└──────────────────────────────┘

Enter fullscreen mode

Exit fullscreen mode

So basically: user interacts with CLI → loads Swagger → parses specs → builds a prompt → sends to AI → AI returns tests → saves to file.

## Code Highlights

### The test generator

The core idea here was: extractas much info as possiblefrom Swagger so the AI could generate meaningful tests.

Here’s the main function I wrote:

def

test_generator
(
path
,

method
,

swagger_data
):


print
(
f
"
Generating tests for
{
method
.
upper
()
}

{
path
}
...
"
)


details

=

swagger_data
[
"
paths
"
][
path
][
method
]


request_body

=

""


parameters

=

""


# Getting information about the endpoint


if

'
tags
'

not

in

details
:


endpoint_name

=

path


elif

len
(
details
[
'
tags
'
])

==

0
:


endpoint_name

=

path


else
:


endpoint_name

=

details
[
'
tags
'
][
0
]


if

'
requestBody
'

in

details
:


request_body

=

details
[
'
requestBody
'
]


if

'
parameters
'

in

details
:


parameters

=

details
[
'
parameters
'
]


prompt

=

(
f
"
Generate positive and negative tests for this endpoint:
{
path
}
 for the method
{
method
.
upper
()
}
"


f
"
considering the following specifications:
"


f
"
Name of the endpoint:
{
endpoint_name
}
"


f
"
Request body:
{
request_body
}
"


f
"
Query Parameters:
{
parameters
}
 and return the tests following this template:
{
theme
.
PROMPT_TEMPLATE
}
"
)


test_scenario

=

ai_connection
(
prompt
)


print
(
f
"
Exporting tests to file...
"
)


export_to_file
(
test_scenario
,

method
,

endpoint_name
)

Enter fullscreen mode

Exit fullscreen mode

### Connecting to Gemini AI

Connecting to the AI is simple: create a client, set the model, and pass the prompt:

def

ai_connection
(
prompt
):


load_dotenv
()


api_key

=

os
.
getenv
(
"
GOOGLE_API_KEY
"
)


client

=

genai
.
Client
(
api_key
=
api_key
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
"
gemini-2.5-flash
"
,


contents
=
prompt


)


return

response
.
text

Enter fullscreen mode

Exit fullscreen mode

And voilà. The AI returns something like:

POST /api/v1/Books
✔ Scenario: Successfully create a new book with all valid fields
✔ Scenario: Successfully create a new book with only mandatory fields
✔ Scenario: Successfully create a new book using
'text/json; v=1.0'
 content
type


✘ Scenario: Fail to create book due to missing
'title'
 field
✘ Scenario: Fail to create book due to missing
'author'
 field
✘ Scenario: Fail to create book due to missing
'isbn'
 field
✘ Scenario: Fail to create book with an
'isbn'
 that already exists
(
conflict
)

✘ Scenario: Fail to create book due to invalid
'isbn'
 format
(
e.g., too short, non-numeric where expected
)

✘ Scenario: Fail to create book due to
'publication_year'
 being a string instead of an integer
✘ Scenario: Fail to create book due to empty request body
✘ Scenario: Fail to create book due to malformed JSON
in
request body
✘ Scenario: Fail to create book with an empty
'title'
 string
✘ Scenario: Fail to create book with an empty
'author'
 string

Enter fullscreen mode

Exit fullscreen mode

## Challenges & Lessons Learned

Honestly, the hardest part wascleaning up Swagger dataand building prompts that make sense for the AI.Another challenge was designing a workflow that actually works in a CLI without feeling clunky.But in the end, it was super fun, and I learned a lot about AI-assisted testing.

## What’s Next

While building this, I started dreaming about all the things I could do next:

* Automatically generatePostman collectionsfrom these tests
* Integrate withtest management toolslike Zephyr or Xray
* Make it aservicethat monitors Swagger and updates tests whenever endpoints change
The possibilities are endless.

## Conclusion

This project really showed me thatAI + OpenAPI = massive time saver.

Instead of manually writing dozens of tests for every endpoint, I now have an automated system that generatesboth positive and negative scenarios in minutes.

Next steps? Think bigger: integrate it with CI/CD pipelines, plug it into test management tools, or even make it monitor APIs in real-time. Smarter, faster, and way less painful API testing—sounds like a win to me.

If you want to check out the full project, explore the code, or try it yourself, it’s all on my GitHub:API Test Generator.

Dive in, experiment, and see how much time you can save!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
