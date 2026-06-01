---
title: Streaming an LLM response, in 4 GIFs - DEV Community
url: https://dev.to/jasmin/streaming-an-llm-response-in-4-gifs-16dh
site_name: devto
content_file: devto-streaming-an-llm-response-in-4-gifs-dev-community
fetched_at: '2026-06-02T06:00:34.895640'
original_url: https://dev.to/jasmin/streaming-an-llm-response-in-4-gifs-16dh
author: Jasmin Virdi
date: '2026-05-31'
description: We have watched tokens stream in from an LLM before where they appeared one at a time, like the model... Tagged with ai, javascript, webdev, tutorial.
tags: '#ai, #javascript, #webdev, #tutorial'
---

Perceived speed vs actual latency

We have watched tokens stream in from an LLM before where they appeared one at a time, like the model was typing. If you used the Anthropic SDK's .stream() method, it just worked and you probably never saw what was on the wire.

This post will majorly focus on how a stream response works and how bugs are handled by SDK behind the hood.

## 1. Why Streaming exists

To enable the streaming option we would need to make one change in the post request that is a single field"stream": trueand it will change the response experience.

Here are the pointers we take from the gif.

1. The left side shows no streaming as the cursor blinks for 4 seconds then the whole response lands at once.
2. The right side shows the streaming where the first word shows up in about 300 milliseconds. Words flow in as the model generates them.

Both the sides havesame model, same prompt, same total timeit is just the right side started giving response almost 4 seconds earlier. The 4 seconds wait time for a full reply feels broken. A streamed reply that finishes in four seconds feels fast.Streaming doesn't make the model faster it makes the wait disappear.

## 2. What's on the wire

When you setstream: true, the API stops sending a single JSON blob. It opens a persistent HTTP connection and pushes events down the line as the model generates them.The format is Server-Sent Events (SSE) a web standard.Any SSE debugger will read this stream.

Here's what comes through:

A few things to notice:

The text lives indelta.text, nested insidecontent_block_deltaevents. Those are the events we should look after.

stop_reasonmoved.In post 1, we saw it right there in the response JSON. Here, it arrives at the very end inside amessage_deltaevent, just beforemessage_stop. If the loop bails out as soon as the text stops arriving we will never see it.

Chunks don't line up with tokens or words.You might get"Hello"in one chunk and" world"in the next, or both in one. The network decides where the cuts happens and it is not the model, not the API.

That's what the SDK has been hiding from you.

## 3. Reading the stream

Streaming sounds complicated until we write the loop. It's just reading bytes, buffering them, splitting on blank lines, and parsing JSON.

Here's the flow:

1. The response body is aReadableStreamwhich can be iterated withfor await.
2. Each iteration gives us bytes which we can decode to string.
3. Buffer the string. A chunk might end mid-message.
4. Split the buffer on\n\n— that's the SSE message separator.
5. Keep the last item in the buffer. It might be incomplete.
6. For each complete message, find thedata:line, strip the prefix, and parse the JSON.
7. If the type iscontent_block_delta, printdelta.text.
8. If it'smessage_delta, you've got yourstop_reason.

Here is the complete sample code you can use to try out:

const
 
prompt
 
=
 
process
.
argv
[
2
]
 
??
 
"
Count to 10, slowly.
"
;

const
 
response
 
=
 
await
 
fetch
(
"
https://api.anthropic.com/v1/messages
"
,
 
{

 
method
:
 
"
POST
"
,

 
headers
:
 
{

 
"
x-api-key
"
:
 
process
.
env
.
ANTHROPIC_API_KEY
,

 
"
anthropic-version
"
:
 
"
2023-06-01
"
,

 
"
content-type
"
:
 
"
application/json
"
,

 
},

 
body
:
 
JSON
.
stringify
({

 
model
:
 
"
claude-opus-4-5
"
,

 
max_tokens
:
 
1024
,

 
stream
:
 
true
,

 
messages
:
 
[{
 
role
:
 
"
user
"
,
 
content
:
 
prompt
 
}],

 
}),

});

const
 
decoder
 
=
 
new
 
TextDecoder
();

let
 
buffer
 
=
 
""
;

for
 
await 
(
const
 
chunk
 
of
 
response
.
body
)
 
{

 
buffer
 
+=
 
decoder
.
decode
(
chunk
,
 
{
 
stream
:
 
true
 
});

 
const
 
messages
 
=
 
buffer
.
split
(
"
\n\n
"
);

 
buffer
 
=
 
messages
.
pop
()
 
??
 
""
;

 
for 
(
const
 
message
 
of
 
messages
)
 
{

 
const
 
dataLine
 
=
 
message
.
split
(
"
\n
"
).
find
(
l
 
=>
 
l
.
startsWith
(
"
data: 
"
));

 
if 
(
!
dataLine
)
 
continue
;

 
const
 
data
 
=
 
JSON
.
parse
(
dataLine
.
slice
(
6
));

 
if 
(
data
.
type
 
===
 
"
content_block_delta
"
 
&&
 
data
.
delta
.
type
 
===
 
"
text_delta
"
)
 
{

 
process
.
stdout
.
write
(
data
.
delta
.
text
);

 
}

 
if 
(
data
.
type
 
===
 
"
message_delta
"
)
 
{

 
process
.
stderr
.
write
(
`\n\n[stop_reason: 
${
data
.
delta
.
stop_reason
}
]\n`
);

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

The way it is working is that when the chunk ends in the middle of a messagesplit("\n\n")leaves an incomplete fragment as the last item.pop()pulls it back into the buffer so the next chunk can finish it. Without this line, every split message crashes the parser.

data.delta.type === "text_delta"this check matters because content_block_delta can carry other delta types too:input_json_deltafor tool arguments,thinking_deltafor extended thinking,signature_deltafor verification. For now we only care about text.

You can find the full implementationhere on GitHub as well.

## 4. Three bugs

The code above works on a good day. Here's what breaks it on a bad one.

The ghost stream.The issue is user navigates away with the stream keeps running and tokens keep arriving with nobody to read them. In order to fix this pass anAbortControllersignal tofetchand callabort()when you're done.

The fix is anAbortController:

const
 
controller
 
=
 
new
 
AbortController
();

const
 
response
 
=
 
await
 
fetch
(
url
,
 
{
 
signal
:
 
controller
.
signal
,
 
...
options
 
});

// later, when the user navigates away:

controller
.
abort
();

Enter fullscreen mode

Exit fullscreen mode

The silent truncation.The API can send anerrorevent mid stream during overload. If the loop only handlescontent_block_delta, the error gets skipped and you end up with a truncated response and no exception. The fix is to handledata.type === "error"explicitly.

if 
(
data
.
type
 
===
 
"
error
"
)
 
{

 
throw
 
new
 
Error
(
`Stream error: 
${
data
.
error
.
message
}
`
);

}

Enter fullscreen mode

Exit fullscreen mode

The split packet.A single SSE message can arrive in two TCP packets. Without buffering,JSON.parsethrows on the half. This is whatbuffer = messages.pop() ?? ""fixes, it holds the incomplete piece until the next chunk completes it.

### stop_reason, in a stream

In post 1,stop_reasonwas right there in the response JSON. In a stream, it's the same four valuesend_turn,max_tokens,tool_use,stop_sequencebut they arrive inside amessage_deltaevent near the end of the stream.

event: message_delta
data: {"type":"message_delta","delta":{"stop_reason":"end_turn",...}}

Enter fullscreen mode

Exit fullscreen mode

The same rule from post 1 applies: if you ignorestop_reason, you'll ship a bug. Amax_tokenscutoff in a streamed response looks exactly like a normal end of stream. You won't know the model was cut off unless you read this event.

### Three things to try before the next post

1.Run the streaming code. Then change"stream": truetofalseand run it again. Notice how long you wait before seeing anything. That gap is what your users feel.

2.Addconsole.error(chunk.length)inside thefor awaitloop, before any parsing. Run the code and watch the numbers. You'll see chunks of wildly different sizes it could be 8 bytes here, 400 bytes there. The network decides, not the model. Tokens and chunks are not the same thing.

3.Start a stream, then disconnect your wifi mid response. Watch what happens. The loop hangs, then eventually throws but only if we have added error handling. This sets up the error handling post later in the series.

### What's next

TinyAgent can now stream a response. Tokens land as they arrive.stop_reasonshows up at the end. It still has no memory though every call starts blank.

In the upcoming post series we will capture another important details. 😁

Happy Coding! 👩‍💻

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse