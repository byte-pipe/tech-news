---
title: 'Observability at Scale: Mastering ADK Callbacks for Cost, Latency, and Auditability [GDE] - DEV Community'
url: https://dev.to/gde/observability-at-scale-mastering-adk-callbacks-for-cost-latency-and-auditability-1mo5
site_name: devto
content_file: devto-observability-at-scale-mastering-adk-callbacks-for
fetched_at: '2026-04-08T11:23:52.878485'
original_url: https://dev.to/gde/observability-at-scale-mastering-adk-callbacks-for-cost-latency-and-auditability-1mo5
author: Connie Leung
date: '2026-04-06'
description: AI orchestrators receive significant attention; however, when deployments become latent and costly,... Tagged with agents, tutorial, ai, typescript.
tags: '#agents, #tutorial, #ai, #typescript'
---

Bypassing redundant steps to cut LLM costs

AI orchestrators receive significant attention; however, when deployments become latent and costly, developers often overlook a critical capability: ADK callback hooks. The design patterns and best practices of callback hooks enable developers to refactor logic from agents to callback hooks to add observability, reduce cost and latency, and modify session state dynamically.

This post explores how to create callback hooks at various stages of an ADK agent to demonstrate the following design patterns:

* Logging and monitoring performance
* Managing dynamic state
* Modifying requests and responses
* Skipping steps conditionally

## Demo Overview

The orchestrator routes the project description tosequentialEvaluationAgent. ThesequentialEvaluationAgentconsists of project, anti-patterns, decision, recommendation, audit, upload, merger, and email subagents.

In theproject,anti-patterns,decision,recommendation, andmergersubagents, I implemented callback hooks to demonstrate their capabilities and practicality.

## Architecture

Google ADK stands for Agent Development Kit. It is an open source agent framework that enables developers to build and deploy AI agents in a convenient way.

The project, anti-patterns, decision, recommendation, and synthesis agents are LLM agents. These agents require Gemini to reason and generate text responses.

The Audit Trail, Cloud Storage, and Email agents integrate with external APIs or resources that trigger deterministic actions.

## Callback Types

ADK provides six types of callback hooks that are called before and after an agent is executed, before and after a model is executed, and before and after a tool is executed.

Callback Type

Description

beforeAgentCallback

Call before the new cycle of an agent

afterAgentCallback

Call after the agent cycle completes

beforeModelCallback

Call before the LLM is called

afterModelCallback

Call after the LLM returns a response

beforeToolCallback

Call before the tool is called

afterToolCallback

Call after the tool is called

## When and why I started using ADK callback hooks

When I used ADK web for local testing and debugging, my first priority was correctness. Performance and token usage had lower priorities until the agents were deployed to a QA environment.

When product managers and the QA team recognized apparent slowness and high cost, they would inform me. Next, I examined the agent to identify performance bottlenecks and deterministic steps that could be handled in callback hooks or application code.

## The Benefits of Callback

Using callback hooks offers several critical advantages in my subagents:

Type

Benefit

Short Circuit

Call
beforeModelCallback
 to validate session data and skip LLM flow when data is invalid

Separation of Concerns

Reset session data in the
beforeAgentCallback
 so that tool remains lean and focuses on business logic

Observability

Add logging in the
beforeAgentCallback
 and the
afterAgentCallback
 to log performance metrics

Dynamic State Management

Create a reusable
afterToolCallback
 to increment validation attempts and modify response status to FATAL_ERROR

## Prerequisites

### Requirements

* TypeScript 5.9.3 or later
* Node.js 24.13.0 or later
* npm 11.8.0 or later
* Docker (For running MailHog locally)
* Google ADK (For building the custom agent)
* Gemini in Vertex AI (to call the model in LLM agents, although not required for the custom agent)

Note: I used Gemini in Vertex AI for authentication due to regional availability. Gemini is currently unavailable in Hong Kong; therefore, I utilized Gemini in Vertex AI instead.

### Install npm dependencies

npm i
--save-exact
 @google/adk
npm i
--save-dev

--save-exact
 @google/adk-devtools
npm i
--save-exact
 nodemailer
npm i
--save-dev

--save-exact
 @types/nodemailer rimraf
npm i
--save-exact
 marked
npm i
--save-exact
 zod

Enter fullscreen mode

Exit fullscreen mode

I installed the required dependencies for building ADK agents, converting Markdown strings to HTML, and sending emails to MailHog during local testing.

Pinned dependencies ensure the versioning is the same in development and production environments for enterprise-level applications.

### Environment variables

Copy.env.exampleto.envand fill in the credentials:

GEMINI_MODEL_NAME="gemini-3.1-flash-lite-preview"
GOOGLE_CLOUD_PROJECT="<Google Cloud Project ID>"
GOOGLE_CLOUD_LOCATION="global"
GOOGLE_GENAI_USE_VERTEXAI=TRUE

# SMTP Settings (MailHog)
SMTP_HOST="localhost"
SMTP_PORT=1025
SMTP_USER=""
SMTP_PASS=""
SMTP_FROM="no-reply@test.local"
ADMIN_EMAIL="admin@test.local"

Enter fullscreen mode

Exit fullscreen mode

SMTP_HOST,SMTP_PORT,SMTP_USER,SMTP_PASS, are required to set upMailHogfor local email testing.

SMTP_FROMis a from email address that can be any string in local testing.

ADMIN_EMAILis an administrator email address receiving emails that theEmailAgentsends. It is an environment variable in my use case because it is the only recipient. If another scenario requires sending emails to customers, the environment variable should be removed.

## ADK Callback Patterns in Action

Here is how I implemented these four callback design patterns in practice.

### Logging and Monitoring

Callback used:beforeAgentCallbackandafterAgentCallback

TheagentStartCallbackstores the current time in milliseconds instart_timevariable in the session state.

import

{

SingleAgentCallback

}

from

'
@google/adk
'
;

export

const

START_TIME_KEY

=

'
start_time
'
;

export

const

agentStartCallback
:

SingleAgentCallback

=

(
context
)

=>

{


if
(
!
context

||

!
context
.
state
)

{


return

undefined
;


}


context
.
state
.
set
(
START_TIME_KEY
,

Date
.
now
());


return

undefined
;

};

Enter fullscreen mode

Exit fullscreen mode

TheagentEndCallbackobtains the start time from the session state and calculates the duration. Then, it usesconsole.logto log the performance metrics. The callback returnsundefinedso that any subagent always flows to the next one in the sequential workflow.

export

const

agentEndCallback
:

SingleAgentCallback

=

(
context
)

=>

{


if
(
!
context

||

!
context
.
state
)

{


return

undefined
;


}


const

now

=

Date
.
now
();


const

startTime

=

context
.
state
.
get
<
number
>
(
START_TIME_KEY
)

||

now
;


console
.
log
(


`Performance Metrics for Agent "
${
context
.
agentName
}
": Total Elapsed Time:
${(
now

-

startTime
)

/

1000
}
 seconds.`
,


);


return

undefined
;

};

Enter fullscreen mode

Exit fullscreen mode

Next, I call both callback hooks in the subagents to know how long they take to execute. The following example shows how I log the performance metric of aprojectsubagent.

export

function

createProjectAgent
(
model
:

string
)

{


const

projectAgent

=

new

LlmAgent
({


name
:

'
ProjectAgent
'
,


model
,


beforeAgentCallback
:

agentStartCallback
,


instruction
:

(
context
)

=>

{


...

LLM

instruction

....


},


afterAgentCallback
:

agentEndCallback
,


...


});


return

projectAgent
;

}

Enter fullscreen mode

Exit fullscreen mode

### Reset Session State

Callback used:beforeAgentCallback

The orchestrator resets variables in the session state before the agent lifecycle begins.

export

const

AUDIT_TRAIL_KEY

=

'
auditTrail
'
;

export

const

RECOMMENDATION_KEY

=

'
recommendation
'
;

export

const

CLOUD_STORAGE_KEY

=

'
cloudStorage
'
;

export

const

DECISION_KEY

=

'
decision
'
;

export

const

PROJECT_KEY

=

'
project
'
;

export

const

ANTI_PATTERNS_KEY

=

'
antiPatterns
'
;

export

const

MERGED_RESULTS_KEY

=

'
mergedResults
'
;

export

const

PROJECT_DESCRIPTION_KEY

=

'
project_description
'
;

export

const

VALIDATION_ATTEMPTS_KEY

=

'
validation_attempts
'
;

Enter fullscreen mode

Exit fullscreen mode

const

resetNewEvaluationCallback
:

SingleAgentCallback

=

(
context
)

=>

{


if
(
!
context

||

!
context
.
state
)

{


return

undefined
;


}


const

state

=

context
.
state
;


// Clear all previous evaluation data


state
.
set
(
PROJECT_KEY
,

null
);


state
.
set
(
ANTI_PATTERNS_KEY
,

null
);


state
.
set
(
DECISION_KEY
,

null
);


state
.
set
(
RECOMMENDATION_KEY
,

null
);


state
.
set
(
AUDIT_TRAIL_KEY
,

null
);


state
.
set
(
CLOUD_STORAGE_KEY
,

null
);


state
.
set
(
MERGED_RESULTS_KEY
,

null
);


state
.
set
(
VALIDATION_ATTEMPTS_KEY
,

0
);


console
.
log
(


`beforeAgentCallback: Agent
${
context
.
agentName
}
 has reset the session state for a new evaluation cycle.`
,


);


return

undefined
;

};

Enter fullscreen mode

Exit fullscreen mode

The orchestrator sets the variables tonullin thebeforeAgentCallback. In theprepareEvaluationTool, the orchestrator only replaces thedescriptionwith the new project description.

const

prepareEvaluationTool

=

new

FunctionTool
({


name
:

'
prepare_evaluation
'
,


description
:

'
Stores the new project description to prepare for a fresh evaluation.
'
,


parameters
:

z
.
object
({


description
:

z
.
string
().
describe
(
'
The validated project description from the user.
'
),


}),


execute
:

({

description

},

context
)

=>

{


if
(
!
context

||

!
context
.
state
)

{


return

{

status
:

'
ERROR
'
,

message
:

'
No session state found.
'

};


}


// Set the new description for the ProjectAgent to find


context
.
state
.
set
(
PROJECT_DESCRIPTION_KEY
,

description
);


return

{

status
:

'
SUCCESS
'
,

message
:

'
Description updated.
'

};


},

});

Enter fullscreen mode

Exit fullscreen mode

The tool logic is more efficient and the token usage is reduced.

export

const

rootAgent

=

new

LlmAgent
({


name
:

'
ProjectEvaluationAgent
'
,


model
:

'
gemini-3.1-flash-lite-preview
'
,


beforeAgentCallback
:

resetNewEvaluationCallback
,


instruction
:

`
 ... LLM instruction ....
 `
,


tools
:

[
prepareEvaluationTool
],


subAgents
:

[
sequentialEvaluationAgent
],

});

Enter fullscreen mode

Exit fullscreen mode

The orchestrator uses theresetNewEvaluationCallbackto reset the session variables, and theprepareEvaluationToolto replace the project description. Finally, thesequentialEvaluationAgentstarts the agentic workflow to derive a decision and generate the recommendation.

### Dynamic State Management

Prerequisite: The subagent uses tool calling to perform actionCallback used:afterToolCallback

The use case is to increment the value ofvalidation_attemptsin the session state. After consulting AI, theafterToolCallbackstage ofprojectanddecisionsubagents is the perfect location to increment it. Therefore, I define a meta-function that creates aafterToolCallbackto increment the validation attempts.

export

const

VALIDATION_ATTEMPTS_KEY

=

'
validation_attempts
'
;

Enter fullscreen mode

Exit fullscreen mode

export

const

MAX_ITERATIONS

=

3
;

Enter fullscreen mode

Exit fullscreen mode

import

{

AfterToolCallback

}

from

'
@google/adk
'
;

import

{

VALIDATION_ATTEMPTS_KEY

}

from

'
../output-keys.const.js
'
;

import

{

MAX_ITERATIONS

}

from

'
../validation.const.js
'
;

export

function

createAfterToolCallback
(
fatalErrorMessage
:

string
,

maxAttempts

=

MAX_ITERATIONS
):

AfterToolCallback

{


return
({

tool
,

context
,

response

})

=>

{


if
(
!
tool

||

!
context

||

!
context
.
state
)

{


return

undefined
;


}


const

toolName

=

tool
.
name
;


const

agentName

=

context
.
agentName
;


const

state

=

context
.
state
;


if
(
!
response

||

typeof

response

!==

'
object
'

||

!
(
'
status
'

in

response
))

{


return

undefined
;


}


// [1] Dynamic state management


const

attempts

=

(
state
.
get
<
number
>
(
VALIDATION_ATTEMPTS_KEY
)

||

0
)

+

1
;


state
.
set
(
VALIDATION_ATTEMPTS_KEY
,

attempts
);


// [2] Response modification


const

status

=

response
.
status

||

'
ERROR
'
;


if
(
status

===

'
ERROR
'

&&

attempts

>=

maxAttempts
)

{


context
.
actions
.
escalate

=

true
;


return

{


status
:

'
FATAL_ERROR
'
,


message
:

fatalErrorMessage
,


};


}


};

}

Enter fullscreen mode

Exit fullscreen mode

In bothprojectanddecisionsubagents, I invokecreateAfterToolCallbackto create their ownafterToolCallbackto increment the validation attempts.

const

projectAfterToolCallback

=

createAfterToolCallback
(


`STOP processing immediately. Max validation attempts reached. Return the most accurate data found so far or empty strings if none.`
,

);

Enter fullscreen mode

Exit fullscreen mode

const

decisionAfterToolCallback

=

createAfterToolCallback
(


`STOP processing immediately and output the final JSON schema with verdict: "None".`
,

);

Enter fullscreen mode

Exit fullscreen mode

Next, I call theprojectAfterToolCallbackin theafterToolCallbackstage of theprojectsubagent.

export

function

createProjectAgent
(
model
:

string
)

{


const

projectAgent

=

new

LlmAgent
({


name
:

'
ProjectAgent
'
,


model
,


beforeAgentCallback
:

agentStartCallback
,


instruction
:

(
context
)

=>

{


...

LLM

instruction

....


},


afterToolCallback
:

projectAfterToolCallback
,


afterAgentCallback
:

agentEndCallback
,


tools
:

[
validateProjectTool
],


...


});


return

projectAgent
;

}

Enter fullscreen mode

Exit fullscreen mode

Next, I call thedecisionAfterToolCallbackin theafterToolCallbackstage of thedecisionsubagent.

export

function

createDecisionTreeAgent
(
model
:

string
)

{


const

decisionTreeAgent

=

new

LlmAgent
({


name
:

'
DecisionTreeAgent
'
,


model
,


beforeAgentCallback
:

[
resetAttemptsCallback
,

agentStartCallback
],


instruction
:

(
context
)

=>

{


...

instruction

of

the

LLM

flow

...


},


afterToolCallback
:

decisionAfterToolCallback
,


afterAgentCallback
:

agentEndCallback
,


tools
:

[
validateDecisionTool
],


...


});


return

decisionTreeAgent
;

}

Enter fullscreen mode

Exit fullscreen mode

### Request/Response Modification

Prerequisite: The subagent uses tool calling to perform actionCallback used:AfterToolCallback

The sameAfterToolCallbackalso modifies the response when the number of validation attempts exceeds the maximum iterations.

When the status isERRORand the value ofvalidation_attemptsis at leastmaximum_iterations, thecontext.actions.escalateflag is set totrueto break out of the loop. Moreover, the status is changed toFATAL_ERRORand the custom fatal message is returned.

### Conditional Skipping of Steps

This is an important design pattern for avoiding unnecessary LLM executions.

Callback used:beforeModelCallback.

In my subagents, I run this callback to validate the session data. When a specific condition is met, the callback returns content immediately to skip the subsequent LLM flow.

#### Example 1

If theprojectagent is able to break down a project description into task, problem, constraint, and goal, the agent will return the breakdown immediately. Otherwise, the agent prompts Gemini to use reasoning to perform the breakdown.

import

{

SingleBeforeModelCallback

}

from

'
@google/adk
'
;

const

beforeModelCallback
:

SingleBeforeModelCallback

=

({

context

})

=>

{


const

{

project

}

=

getEvaluationContext
(
context
);


const

{

isCompleted

}

=

isProjectDetailsFilled
(
project
);


if
(
isCompleted
)

{


return

{


content
:

{


role
:

'
model
'
,


parts
:

[


{


text
:

JSON
.
stringify
(
project
),


},


],


},


};


}


return

undefined
;

};

Enter fullscreen mode

Exit fullscreen mode

Then,beforeModelCallbackis hooked to the beforeModelCallback stage of theprojectsubagent.

export

function

createProjectAgent
(
model
:

string
)

{


const

projectAgent

=

new

LlmAgent
({


name
:

'
ProjectAgent
'
,


model
,


description
:


'
Analyzes the user-provided project description to extract and structure its core components, including the primary task, underlying problem, ultimate goal, and architectural constraints.
'
,


beforeAgentCallback
:

agentStartCallback
,


beforeModelCallback
,


instruction
:

(
context
)

=>

{


const

{

projectDescription

}

=

getEvaluationContext
(
context
);


if
(
!
projectDescription
)

{


return

''
;


}


return

generateProjectBreakdownPrompt
(
projectDescription
);


},


afterToolCallback
:

projectAfterToolCallback
,


afterAgentCallback
:

agentEndCallback
,


tools
:

[
validateProjectTool
],


outputSchema
:

projectSchema
,


outputKey
:

PROJECT_KEY
,


disallowTransferToParent
:

true
,


disallowTransferToPeers
:

true
,


});


return

projectAgent
;

}

Enter fullscreen mode

Exit fullscreen mode

#### Example 2

Thedecisionagent verifies theverdictproperty in thebeforeModelCallback. If theverdictis notNone, the callback returns the valid decision immediately. TheverdictisNoneand the callback examines the project breakdown and the anti-patterns. When project breakdown and anti-patterns are provided, the callback returns undefined to trigger the LLM flow. Otherwise, thedecisionagent does not have valid inputs to derive the verdict. The callback returnsNonein this edge case.

import

{

SingleBeforeModelCallback

}

from

'
@google/adk
'
;

const

beforeModelCallback
:

SingleBeforeModelCallback

=

({

context

})

=>

{


const

{

decision

}

=

getEvaluationContext
(
context
);


if
(
decision

&&

decision
.
verdict

!==

'
None
'
)

{


return

{


content
:

{


role
:

'
model
'
,


parts
:

[


{


text
:

JSON
.
stringify
(
decision
),


},


],


},


};


}


const

{

project
,

antiPatterns

}

=

getEvaluationContext
(
context
);


const

{

isCompleted

}

=

isProjectDetailsFilled
(
project
);


if
(
isCompleted

&&

antiPatterns
)

{


return

undefined
;


}


return

{


content
:

{


role
:

'
model
'
,


parts
:

[


{


text
:

JSON
.
stringify
({


verdict
:

'
None
'
,


nodes
:

[],


}),


},


],


},


};

};

Enter fullscreen mode

Exit fullscreen mode

Then,beforeModelCallbackis hooked to thebeforeModelCallbackstage of theprojectsubagent.

export

function

createDecisionTreeAgent
(
model
:

string
)

{


const

decisionTreeAgent

=

new

LlmAgent
({


name
:

'
DecisionTreeAgent
'
,


model
,


beforeAgentCallback
:

[
resetAttemptsCallback
,

agentStartCallback
],


beforeModelCallback
,


instruction
:

(
context
)

=>

{


...

instruction

of

the

LLM

flow

...


},


afterToolCallback
:

decisionAfterToolCallback
,


afterAgentCallback
:

agentEndCallback
,


tools
:

[
validateDecisionTool
],


outputSchema
:

decisionSchema
,


outputKey
:

DECISION_KEY
,


disallowTransferToParent
:

true
,


disallowTransferToPeers
:

true
,


});


return

decisionTreeAgent
;

}

Enter fullscreen mode

Exit fullscreen mode

#### Example 3

Therecommendationagent uses thebeforeModelCallbackto examine the project breakdown, anti-patterns and verdict. There are two scenarios that need LLM to generate the recommendation. The first scenario is valid project breakdown, anti-patterns, and non-None verdict. The second scenario is incomplete project breakdown andNoneverdict. The LLM is instructed to describe the missing field in the project breakdown and how important the missing field is to obtain a valid decision. For other cases, the callback returns a static recommendation immediately and skip the subsequent LLM flow.

function

constructRecommendation
(
recommendation
:

string
)

{


return

{


content
:

{


role
:

'
model
'
,


parts
:

[


{


text
:

JSON
.
stringify
({


text
:

recommendation
,


}),


},


],


},


};

}

const

beforeModelCallback
:

SingleBeforeModelCallback

=

({

context

})

=>

{


const

{

project
,

antiPatterns
,

decision

}

=

getEvaluationContext
(
context
);


const

{

isCompleted

}

=

isProjectDetailsFilled
(
project
);


const

isDecisionNone

=

decision

&&

decision
.
verdict

===

'
None
'
;


if
((
isCompleted

&&

antiPatterns

&&

decision

&&

decision
.
verdict

!==

'
None
'
)

||

(
!
isCompleted

&&

isDecisionNone
))

{


return

undefined
;


}

else

if
(
isCompleted

&&

isDecisionNone
)

{


return

constructRecommendation
(


'
## Recommendation: Manual Review Required
\n\n
**Status:** Abnormal Case Detected
\n\n
The provided project is complete and valid, but the decision tree could not reach a conclusive verdict (Result: `None`).
\n\n
**Possible Reasons:**
\n
- The requirements fall outside of known architectural patterns.
\n
- There are conflicting constraints and goals that cannot be resolved automatically.
\n\n
**Next Steps:**
\n
- Review and refine the constraints or goals.
\n
- Escalate for manual architectural review.
'
,


);


}


return

constructRecommendation
(


'
## Recommendation: Data Required
\n\n
**Status:** Abnormal Case Detected
\n\n
No decision is reached.
'
,


);

};

Enter fullscreen mode

Exit fullscreen mode

Similar to the previousprojectanddecisionagents, thebeforeModelCallbackfunction is hooked to thebeforeModelCallbackstage of therecommendationagent.

export

function

createRecommendationAgent
(
model
:

string
)

{


const

recommendationAgent

=

new

LlmAgent
({


name
:

'
RecommendationAgent
'
,


model
,


beforeModelCallback
,


beforeAgentCallback
:

agentStartCallback
,


instruction
:

(
context
)

=>

{


const

{

project
,

antiPatterns
,

decision

}

=

getEvaluationContext
(
context
);


const

{

isCompleted
,

missingFields

}

=

isProjectDetailsFilled
(
project
);


if
(
project
)

{


if
(
!
isCompleted

&&

decision

&&

decision
.
verdict

===

'
None
'
)

{


console
.
log
(
'
RecommendationAgent -> generateFailedDecisionPrompt
'
);


return

generateFailedDecisionPrompt
(
project
,

missingFields
);


}

else

if
(
isCompleted

&&

antiPatterns

&&

decision

&&

decision
.
verdict

!==

'
None
'
)

{


console
.
log
(
'
RecommendationAgent -> generateRecommendationPrompt
'
);


return

generateRecommendationPrompt
(
project
,

antiPatterns
,

decision
);


}


}


return

'
Skipping LLM due to missing data.
'
;


},


afterAgentCallback
:

agentEndCallback
,


outputSchema
:

recommendationSchema
,


outputKey
:

RECOMMENDATION_KEY
,


disallowTransferToParent
:

true
,


disallowTransferToPeers
:

true
,


});


return

recommendationAgent
;

}

Enter fullscreen mode

Exit fullscreen mode

These are the callback design patterns that the agent adopts. In the next section, I describe how to launch the agent to observe the logging messages in the terminal.

## Environment Setup

I pulled the latest version of theMailHogDocker image from Docker Hub and started it locally to receive test emails and display them in the Web UI. Thedocker-compose.ymlfile contains the setup configuration.

services
:


mailhog
:


image
:

mailhog/mailhog


container_name
:

mailhog


ports
:


-

'
1025:1025'

# SMTP port


-

'
8025:8025'

# HTTP (Web UI) port


restart
:

always


networks
:


-

decision-tree-agent-network

networks
:


decision-tree-agent-network
:

Enter fullscreen mode

Exit fullscreen mode

The SMTP server listens on port 1025, and the Web UI is accessible athttp://localhost:8025.

docker compose up
-d

Enter fullscreen mode

Exit fullscreen mode

Start MailHog in Docker.

## Testing

Add scripts topackage.jsonto build and start the ADK web interface.


"scripts"
:

{


"prebuild"
:

"rimraf dist"
,


"build"
:

"npx tsc --project tsconfig.json"
,


"web"
:

"npm run build && npx @google/adk-devtools web --host 127.0.0.1 dist/agent.js"


}
,

Enter fullscreen mode

Exit fullscreen mode

* Open a terminal and typenpm run webto start the API server.
* Open a new browser tab and typehttp://localhost:8000.
* Paste the following text into the message box:

One of my favorite tech influencers just tweeted about a 'breakthrough in solid-state batteries.' Find which public company they might be referring to, check that company’s recent patent filings to see if it’s true, and then check their stock price to see if the market has already 'priced it in'.

Enter fullscreen mode

Exit fullscreen mode

* Ensure the root agent executes and halts when the email agent terminates. The orchestrator and the project agent trigger the callback hooks to reset the session state, log performance metrics, validate session data, increment the validation attempts, and modify the response.

* Similarly, both anti-patterns and decisions agents used thebeforeAgentCallbackandafterAgentCallbackto log performance metrics. They also used thebeforeModelCallbackto validate session data before calling the LLM to generate a response. Moreover, the decision agent incremented the validation attempts and modify the status toFATAL_ERRORwhen the validation attempts exceeded or equal to maximum iterations in theafterToolCallback.

* Similarly, both recommendation and merger agents used thebeforeAgentCallbackandafterAgentCallbackto log performance metrics. The recommendation agent also used thebeforeModelCallbackto validate session data before calling the LLM to generate a recommendation.

## Conclusion

ADK supports lifecycle callback hooks that are applicable to different use cases. In this post, I describe logging performance metrics in thebeforeAgentCallbackandafterAgentCallback. I refactored the reset session state logic in the orchestrator'sbeforeAgentCallbackto make the tool lean and cost efficient. TheafterToolCallbackescalated to a higher agent and modified the response status toFATAL_ERRORwhen the loop count in the validation-retry loop exceeded the maximum iterations. When skipping LLM calls conditionally, thebeforeModelCallbackreturned custom content immediately. Then, the agent did not add unnecessary time to the agent flow and did not consume tokens.

The takeaway: follow the design patterns and best practices of callback at various stages of an agent to log performance metrics, reduce cost and latency, and modify response.

## Resources

* Google Development Kit in TypeScript
* Types of Callbacks
* Design Patterns and Best Practices for Callbacks
* Build a Multi-Agent System with ADK, MCP, and Gemini
* Decision Tree Agent Repo

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
