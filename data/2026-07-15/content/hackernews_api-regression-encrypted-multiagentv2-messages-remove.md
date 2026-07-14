---
title: 'Regression: encrypted MultiAgentV2 messages remove readable task audit trail · Issue #28058 · openai/codex · GitHub'
url: https://github.com/openai/codex/issues/28058
site_name: hackernews_api
content_file: hackernews_api-regression-encrypted-multiagentv2-messages-remove
fetched_at: '2026-07-15T04:47:32.377037'
original_url: https://github.com/openai/codex/issues/28058
author: embedding-shape
date: '2026-07-14'
description: 'What version of Codex CLI is running? Upstream main after #26210 (Encrypt multi-agent v2 message payloads, merged 2026-06-05). This appears to affect versions that include that change and enable MultiAgentV2 (post-0.137.0). What subscrip...'
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 openai

 

/

codex

Public

* NotificationsYou must be signed in to change notification settings
* Fork14.6k
* Star98k

# Regression: encrypted MultiAgentV2 messages remove readable task audit trail#28058

Open
Open
Regression: encrypted MultiAgentV2 messages remove readable task audit trail
#28058
Labels
CLI
Issues related to the Codex CLI
Issues related to the Codex CLI
bug
Something isn't working
Something isn't working
subagent
Issues involving subagents or multi-agent features
Issues involving subagents or multi-agent features

## Description

ignatremizov
opened 
on Jun 13, 2026
Issue body actions

### What version of Codex CLI is running?

Upstreammainafter#26210(Encrypt multi-agent v2 message payloads, merged 2026-06-05). This appears to affect versions that include that change and enable MultiAgentV2 (post-0.137.0).

### What subscription do you have?

Not subscription-specific.

### Which model were you using?

Not model-specific. This concerns MultiAgentV2spawn_agent,send_message, andfollowup_taskmessage handling.

### What platform is your computer?

Not platform-specific.

### What terminal emulator and version are you using (if applicable)?

Not terminal-specific.

### Codex doctor report

Not applicable. The regression is visible from the merged code behavior in#26210rather than from local environment state.

### What issue are you seeing?

#26210makes MultiAgentV2 agent task/message payloads opaque to Codex by marking the model-facingmessageparameter as encrypted, storing onlyInterAgentCommunication.encrypted_content, and leavingInterAgentCommunication.contentempty.

The encrypted delivery path is understandable as privacy hardening, but it also removes the human-readable task/message text from local rollout history, trace reduction, and parent-side audit/debug surfaces. That makes it difficult to answer basic questions such as:

* What task did thisspawn_agentcall give the child agent?
* What message was sent to a subagent?
* Why did a child thread exist when reviewing a rollout after the fact?

This is different from#26753, which reports request validation failures for encrypted tool schemas. This issue is about auditability and debuggability after the encrypted schema is accepted.

### What steps can reproduce the bug?

1. Use a build containingEncrypt multi-agent v2 message payloads#26210with MultiAgentV2 enabled. (aka post-0.137.0)
2. Have the model callspawn_agent,send_message, orfollowup_task.
3. Inspect the parent rollout/history/trace for the subagent task.
4. The task/message content is hidden behind ciphertext rather than being available as human-readable audit text.

### What is the expected behavior?

Codex should preserve a human-readable, structured audit copy of the subagent task/message while still allowing encrypted delivery to the recipient model.

A possible shape is to keep the encryptedmessagefield for model delivery, but add a separate non-encrypted audit field for the readable task text. The audit field should be persisted in rollout/history/trace metadata so users and maintainers can inspect what was delegated without needing to decrypt model-delivery ciphertext.

### Additional information

Related PR/issues:

* Encryption change:Encrypt multi-agent v2 message payloads#26210
* Related but distinct schema-validation issue:MultiAgentV2 encrypted spawn_agent schema returns 400: model not configured for encrypted tool use#26753

The goal is not necessarily to revert encrypted delivery. The concern is that encrypted delivery should not fully remove local human auditability for subagent delegation.

### Source analysis

UpstreamInterAgentCommunication::new_encrypted()deliberately initializescontentas an empty string and stores the payload only inencrypted_content:

codex/codex-rs/protocol/src/protocol.rs

Lines 735 to 791
 infde21ba

 
#
[
derive
(
Debug
,
 
Clone
,
 
Serialize
,
 
Deserialize
,
 
PartialEq
,
 
Eq
,
 
JsonSchema
,
 
TS
)
]
 

 
pub
 
struct
 
InterAgentCommunication
 
{
 

 
#
[
serde
(
default
,
 skip_serializing_if = 
"Option::is_none"
)
]
 

 
#
[
ts
(
optional
)
]
 

 
pub
 
id
:
 
Option
<
String
>
,
 

 
pub
 
author
:
 
AgentPath
,
 

 
pub
 
recipient
:
 
AgentPath
,
 

 
#
[
serde
(
default
)
]
 

 
pub
 
other_recipients
:
 
Vec
<
AgentPath
>
,
 

 
pub
 
content
:
 
String
,
 

 
#
[
serde
(
default
,
 skip_serializing_if = 
"Option::is_none"
)
]
 

 
#
[
ts
(
optional
)
]
 

 
pub
 
encrypted_content
:
 
Option
<
String
>
,
 

 
#
[
serde
(
default
,
 skip_serializing_if = 
"Option::is_none"
)
]
 

 
#
[
ts
(
optional
)
]
 

 
pub
 
internal_chat_message_metadata_passthrough
:
 
Option
<
InternalChatMessageMetadataPassthrough
>
,
 

 
pub
 
trigger_turn
:
 
bool
,
 

 
}
 

 

 
impl
 
InterAgentCommunication
 
{
 

 
pub
 
fn
 
new
(
 

 
author
:
 
AgentPath
,
 

 
recipient
:
 
AgentPath
,
 

 
other_recipients
:
 
Vec
<
AgentPath
>
,
 

 
content
:
 
String
,
 

 
trigger_turn
:
 
bool
,
 

 
)
 -> 
Self
 
{
 

 
Self
 
{
 

 
id
:
 
None
,
 

 author
,
 

 recipient
,
 

 other_recipients
,
 

 content
,
 

 
encrypted_content
:
 
None
,
 

 
internal_chat_message_metadata_passthrough
:
 
None
,
 

 trigger_turn
,
 

 
}
 

 
}
 

 

 
pub
 
fn
 
new_encrypted
(
 

 
author
:
 
AgentPath
,
 

 
recipient
:
 
AgentPath
,
 

 
other_recipients
:
 
Vec
<
AgentPath
>
,
 

 
encrypted_content
:
 
String
,
 

 
trigger_turn
:
 
bool
,
 

 
)
 -> 
Self
 
{
 

 
Self
 
{
 

 
id
:
 
None
,
 

 author
,
 

 recipient
,
 

 other_recipients
,
 

 
content
:
 
String
::
new
(
)
,
 

 
encrypted_content
:
 
Some
(
encrypted_content
)
,
 

 
internal_chat_message_metadata_passthrough
:
 
None
,
 

 trigger_turn
,
 

 
}
 

 
}
 

The conversion used for recipient history then emits only the encrypted payload wheneverencrypted_contentis present. Merely populating the runtimecontentfield would therefore not create a readable persistedResponseItem; the fix also needs an explicit local audit persistence path:

codex/codex-rs/protocol/src/protocol.rs

Lines 813 to 845
 infde21ba

 
pub
 
fn
 
to_model_input_item
(
&
self
)
 -> 
ResponseItem
 
{
 

 
let
 content = 
match
 
&
self
.
encrypted_content
 
{
 

 
Some
(
encrypted_content
)
 => 
{
 

 
let
 message_type = 
if
 
self
.
trigger_turn
 
{
 

 
"NEW_TASK"
 

 
}
 
else
 
{
 

 
"MESSAGE"
 

 
}
;
 

 
vec
!
[
 

 
AgentMessageInputContent
::
InputText
 
{
 

 text
:
 format!
(
 

 
"Message Type: {message_type}
\n
Task name: {}
\n
Sender: {}
\n
Payload:
\n
"
,
 

 
self
.
recipient
,
 
self
.
author 

 
)
,
 

 
}
,
 

 
AgentMessageInputContent
::
EncryptedContent
 
{
 

 encrypted_content
:
 encrypted_content
.
clone
(
)
,
 

 
}
,
 

 
]
 

 
}
 

 
None
 => 
vec
!
[
AgentMessageInputContent
::
InputText
 
{
 

 text
:
 
self
.
content
.
clone
(
)
,
 

 
}
]
,
 

 
}
;
 

 
ResponseItem
::
AgentMessage
 
{
 

 
id
:
 
self
.
id
.
clone
(
)
,
 

 
author
:
 
self
.
author
.
to_string
(
)
,
 

 
recipient
:
 
self
.
recipient
.
to_string
(
)
,
 

 content
,
 

 
internal_chat_message_metadata_passthrough
:
 
self
 

 
.
internal_chat_message_metadata_passthrough
 

 
.
clone
(
)
,
 

 
}
 

The current v2 message helper constructs encrypted communication with empty plaintext content:

codex/codex-rs/core/src/tools/handlers/multi_agents_v2.rs

Lines 54 to 65
 infde21ba

 
pub
(
super
)
 
fn
 
communication_from_tool_message
(
 

 
author
:
 
AgentPath
,
 

 
recipient
:
 
AgentPath
,
 

 
message
:
 
String
,
 

 
)
 -> 
InterAgentCommunication
 
{
 

 
InterAgentCommunication
::
new_encrypted
(
 

 author
,
 

 recipient
,
 

 
Vec
::
new
(
)
,
 

 message
,
 

 
/*trigger_turn*/
 
true
,
 

 
)
 

send_messageandfollowup_taskstill deserialize onlytargetplus the encryptedmessage, then pass that ciphertext directly through the shared helper. There is no plaintext companion available to persist:

codex/codex-rs/core/src/tools/handlers/multi_agents_v2/message_tool.rs

Lines 34 to 66
 infde21ba

 
#
[
derive
(
Debug
,
 
Deserialize
)
]
 

 
#
[
serde
(
deny_unknown_fields
)
]
 

 
/// Input for the MultiAgentV2 `send_message` tool.
 

 
pub
(
crate
)
 
struct
 
SendMessageArgs
 
{
 

 
pub
(
crate
)
 
target
:
 
String
,
 

 
pub
(
crate
)
 
message
:
 
String
,
 

 
}
 

 

 
#
[
derive
(
Debug
,
 
Deserialize
)
]
 

 
#
[
serde
(
deny_unknown_fields
)
]
 

 
/// Input for the MultiAgentV2 `followup_task` tool.
 

 
pub
(
crate
)
 
struct
 
FollowupTaskArgs
 
{
 

 
pub
(
crate
)
 
target
:
 
String
,
 

 
pub
(
crate
)
 
message
:
 
String
,
 

 
}
 

 

 
pub
(
super
)
 
fn
 
message_content
(
message
:
 
String
)
 -> 
Result
<
String
,
 
FunctionCallError
>
 
{
 

 
if
 message
.
trim
(
)
.
is_empty
(
)
 
{
 

 
return
 
Err
(
FunctionCallError
::
RespondToModel
(
 

 
"Empty message can't be sent to an agent"
.
to_string
(
)
,
 

 
)
)
;
 

 
}
 

 
Ok
(
message
)
 

 
}
 

 

 
/// Handles the shared MultiAgentV2 message flow for both `send_message` and `followup_task`.
 

 
pub
(
crate
)
 
async
 
fn
 
handle_message_string_tool
(
 

 
invocation
:
 
ToolInvocation
,
 

 
mode
:
 
MessageDeliveryMode
,
 

 
target
:
 
String
,
 

 
message
:
 
String
,
 

 
)
 -> 
Result
<
FunctionToolOutput
,
 
FunctionCallError
>
 
{
 

 
let
 message = 
message_content
(
message
)
?
;
 

codex/codex-rs/core/src/tools/handlers/multi_agents_v2/message_tool.rs

Lines 99 to 114
 infde21ba

 
let
 author = turn 

 
.
session_source
 

 
.
get_agent_path
(
)
 

 
.
unwrap_or_else
(
AgentPath
::
root
)
;
 

 
let
 communication = 

 
communication_from_tool_message
(
author
,
 receiver_agent_path
.
clone
(
)
,
 message
)
;
 

 
let
 kind = 
match
 mode 
{
 

 
MessageDeliveryMode
::
QueueOnly
 => 
AgentCommunicationKind
::
Message
,
 

 
MessageDeliveryMode
::
TriggerTurn
 => 
AgentCommunicationKind
::
Followup
,
 

 
}
;
 

 
let
 context = 
AgentCommunicationContext
::
new
(
kind
,
 session
.
thread_id
)
;
 

 
let
 result = session 

 
.
services
 

 
.
agent_control
 

 
.
send_inter_agent_communication
(
receiver_thread_id
,
 mode
.
apply
(
communication
)
,
 context
)
 

 
.
await
 

The receiver records the model-facingResponseItemproduced byto_model_input_item(). For encrypted communication that item contains the encrypted delivery payload, not readable audit text:

codex/codex-rs/core/src/session/mod.rs

Lines 2929 to 2957
 infde21ba

 
pub
(
crate
)
 
async
 
fn
 
record_inter_agent_communication
(
 

 
&
self
,
 

 
turn_context
:
 
&
TurnContext
,
 

 
mut
 
communication
:
 
InterAgentCommunication
,
 

 
)
 
{
 

 communication
.
set_turn_id_if_missing
(
&
turn_context
.
sub_id
)
;
 

 
let
 response_item = communication
.
to_model_input_item
(
)
;
 

 
let
 items = 
self
.
prepare_conversation_items_for_history
(
 

 turn_context
,
 

 std
::
slice
::
from_ref
(
&
response_item
)
,
 

 
)
;
 

 
let
 items = items
.
as_ref
(
)
;
 

 
let
 response_item = items
[
0
]
.
clone
(
)
;
 

 
{
 

 
let
 
mut
 state = 
self
.
state
.
lock
(
)
.
await
;
 

 state
.
current_time_reminder
.
note_recorded_items
(
items
)
;
 

 state
.
record_items
(
 

 items
.
iter
(
)
,
 

 turn_context
.
model_info
.
truncation_policy
.
into
(
)
,
 

 
)
;
 

 
}
 

 
self
.
persist_rollout_items
(
&
[
 

 
RolloutItem
::
InterAgentCommunicationMetadata
 
{
 

 
trigger_turn
:
 communication
.
trigger_turn
,
 

 
}
,
 

 
RolloutItem
::
ResponseItem
(
response_item
)
,
 

 
]
)
 

 
.
await
;
 

 
self
.
send_raw_response_items
(
turn_context
,
 items
)
.
await
;
 

The structured communication log has the same fallback: whencontentis empty, it recordsencrypted_contentas the event content:

codex/codex-rs/core/src/agent_communication.rs

Lines 44 to 66
 infde21ba

 
pub
(
crate
)
 
fn
 
emit_agent_communication_send
(
 

 
communication_id
:
 
&
str
,
 

 
context
:
 
&
AgentCommunicationContext
,
 

 
communication
:
 
&
InterAgentCommunication
,
 

 
receiver_thread_id
:
 
ThreadId
,
 

 
)
 
{
 

 tracing
::
info!
(
 

 target
:
 
AGENT_COMMUNICATION_TARGET
,
 

 
{
 

 event
.
name = 
"codex.agent_communication"
,
 

 communication_id
,
 

 kind = context
.
kind
.
as_str
(
)
,
 

 state = 
"send"
,
 

 sender_thread_id = %context
.
sender_thread_id
,
 

 receiver_thread_id = %receiver_thread_id
,
 

 content = 
if
 communication
.
content
.
is_empty
(
)
 
{
 

 communication
.
encrypted_content
.
as_deref
(
)
.
unwrap_or_default
(
)
 

 
}
 else 
{
 

 communication
.
content
.
as_str
(
)
 

 
}
,
 

 
}
,
 

 
"agent communication"
 

 
)
;
 

### Implementation / fix spec

A concrete implementation can preserve encrypted delivery and restore a local audit trail:

1. Keep the existing encryptedmessagefield as the delivery payload.
2. Add a required, non-encrypted plaintext companion to each v2 communication tool:* spawn_agent:task_message
* send_messageandfollowup_task: a consistently named plaintext audit field, such astask_messageormessage_text
3. Reject empty plaintext audit values at the handler boundary.
4. ConstructInterAgentCommunicationwith both:* encrypted_contentset to the encryptedmessage
* contentset to the plaintext audit copy
5. Keepto_model_input_item()behavior unchanged so the recipient model still receives ciphertext, not the local audit copy.
6. Persist the plaintext companion in the parent tool invocation/rollout and retain it in structured trace edges and local communication logs.
7. Match tool calls to delivered child items using ciphertext/IDs, not plaintext equality. The plaintext field is audit metadata and should not replace the encrypted delivery identity.
8. Bound the plaintext audit field with the same hard size limit as the corresponding delegated message so the new rollout/context item cannot grow without limit.

Thespawn_agenthalf of this shape is implemented in the following snapshot commit:

ignatremizov@df9a7c4

That prototype makestask_messagerequired in the v2 spawn schema:

v2spawn_agentschema and requiredtask_messagefield

It validates the field and places it inInterAgentCommunication.contentwhile leaving the encrypted delivery payload inencrypted_content:

plaintext audit validation

dual plaintext audit and encrypted delivery construction

It also teaches rollout-trace reduction to keep readable audit content while using the encrypted value only to correlate the tool invocation with delivery:

separate audit content from delivery-match content

correlate delivery while applying readable audit content

The remaining implementation work is to apply the same dual-content contract tosend_messageandfollowup_task, and to ensure every user-facing history/replay/debug surface reads the audit copy rather than falling back to provider ciphertext.

### Acceptance criteria

* Parent rollout/history shows the readable text for v2spawn_agent,send_message, andfollowup_task.
* The child model still receives only the encrypted delivery payload when encryption is enabled.
* Structured rollout-trace interaction edges carry bounded plaintextmessage_content.
* Communication logs use plaintext audit content when present and never substitute ciphertext into a field presented as readable message text.
* Resume/replay preserves the audit copy without injecting it into the child model context.
* Existing plaintext v1 communication behavior is unchanged.
* Regression tests cover all three v2 tools and assert both sides of the contract: readable local audit data and encrypted recipient-model input.
Reactions are currently unavailable

## Metadata

## Metadata