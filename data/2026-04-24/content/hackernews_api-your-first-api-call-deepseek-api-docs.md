---
title: Your First API Call | DeepSeek API Docs
url: https://api-docs.deepseek.com/
site_name: hackernews_api
content_file: hackernews_api-your-first-api-call-deepseek-api-docs
fetched_at: '2026-04-24T11:56:28.070358'
original_url: https://api-docs.deepseek.com/
author: impact_sy
date: '2026-04-24'
description: The DeepSeek API uses an API format compatible with OpenAI/Anthropic. By modifying the configuration, you can use the OpenAI/Anthropic SDK or softwares compatible with the OpenAI/Anthropic API to access the DeepSeek API.
tags:
- hackernews
- trending
---

On this page

# Your First API Call

The DeepSeek API uses an API format compatible with OpenAI/Anthropic. By modifying the configuration, you can use the OpenAI/Anthropic SDK or softwares compatible with the OpenAI/Anthropic API to access the DeepSeek API.

PARAM
VALUE
base_url (OpenAI)
https://api.deepseek.com
base_url (Anthropic)
https://api.deepseek.com/anthropic
api_key
apply for an 
API key
model
*
deepseek-v4-flash
deepseek-v4-pro
deepseek-chat
 (to be deprecated on 2026/07/24)
deepseek-reasoner
 (to be deprecated on 2026/07/24)

* The model namesdeepseek-chatanddeepseek-reasonerwill be deprecated on 2026/07/24. For compatibility, they correspond to the non-thinking mode and thinking mode ofdeepseek-v4-flash, respectively.

## Invoke The Chat API​

Once you have obtained an API key, you can access the DeepSeek model using the following example scripts in the OpenAI API format. This is a non-stream example, you can set thestreamparameter totrueto get stream response.

For examples using the Anthropic API format, please refer toAnthropic API.

* curl
* python
* nodejs
curl https://api.deepseek.com/chat/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ${DEEPSEEK_API_KEY}" \
 -d '{
 "model": "deepseek-v4-pro",
 "messages": [
 {"role": "system", "content": "You are a helpful assistant."},
 {"role": "user", "content": "Hello!"}
 ],
 "thinking": {"type": "enabled"},
 "reasoning_effort": "high",
 "stream": false
 }'
# Please install OpenAI SDK first: `pip3 install openai`
import
 os
from
 openai 
import
 OpenAI
client 
=
 OpenAI
(
 api_key
=
os
.
environ
.
get
(
'DEEPSEEK_API_KEY'
)
,
 base_url
=
"https://api.deepseek.com"
)
response 
=
 client
.
chat
.
completions
.
create
(
 model
=
"deepseek-v4-pro"
,
 messages
=
[
 
{
"role"
:
 
"system"
,
 
"content"
:
 
"You are a helpful assistant"
}
,
 
{
"role"
:
 
"user"
,
 
"content"
:
 
"Hello"
}
,
 
]
,
 stream
=
False
,
 reasoning_effort
=
"high"
,
 extra_body
=
{
"thinking"
:
 
{
"type"
:
 
"enabled"
}
}
)
print
(
response
.
choices
[
0
]
.
message
.
content
)
// Please install OpenAI SDK first: `npm install openai`
import
 
OpenAI
 
from
 
"openai"
;
const
 openai 
=
 
new
 
OpenAI
(
{
 
baseURL
:
 
'https://api.deepseek.com'
,
 
apiKey
:
 process
.
env
.
DEEPSEEK_API_KEY
,
}
)
;
async
 
function
 
main
(
)
 
{
 
const
 completion 
=
 
await
 openai
.
chat
.
completions
.
create
(
{
 
messages
:
 
[
{
 
role
:
 
"system"
,
 
content
:
 
"You are a helpful assistant."
 
}
]
,
 
model
:
 
"deepseek-v4-pro"
,
 
thinking
:
 
{
"type"
:
 
"enabled"
}
,
 
reasoning_effort
:
 
"high"
,
 
stream
:
 
false
,
 
}
)
;
 
console
.
log
(
completion
.
choices
[
0
]
.
message
.
content
)
;
}
main
(
)
;

* Invoke The Chat API