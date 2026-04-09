---
title: Building an Agentic Medical Analysis System That Actually Thinks - DEV Community
url: https://dev.to/aws-builders/building-an-agentic-medical-analysis-system-that-actually-thinks-3dg1
site_name: devto
fetched_at: '2025-10-03T11:08:36.566929'
original_url: https://dev.to/aws-builders/building-an-agentic-medical-analysis-system-that-actually-thinks-3dg1
author: Marcos Henrique
date: '2025-09-29'
description: AI is not committed to truth, but rather to predictability and pleasing, which is why it sounds like... Tagged with ai, aws.
tags: '#ai, #aws'
---

AI is not committed to truth, but rather to predictability and pleasing, which is why it sounds like an emotional mirror programmed to return smiles 😀

Dissolving our cognitive dissonance 🫠

Strengthening information bubbles and inhibiting our critical thinking 😳

With this, I urge you:master AI before it masters you.

Past months were a dive into the chromatic abyss ofAI influencing the human being, so I want to highlight the quote above 👆 that I've been advocating in my recent speech about my perspective on how to implementAgent Event Driven ArchitectureoverAWS SummitandThe Developers Conference.

## Agents + Microservices = 💜

Here's something that'll blow your mind: what if your medical system didn't just process data, but actuallyreasonedabout it and looked likeDoctor Housebut without all those 💊s 😅, and could handle thousands of patients simultaneously to his full potential?

Welcome toagentic event-driven architecture, where I've takenSean Falconer's concept that"AI Agents are Microservices with Brains"and applied it to something life-critical: medical analysis, however we need to go one step back and as product engineers, we need to implement our efforts here in a much moreincrementalthan revolutionary way.In this transition, we expect to hone new skills, from our daily tracing to the analysis of decision patterns among multiple agents. Instead of focusing solely on availability, we mustmeasurethesuccessof ourobjectiveby exploring simulations of unexpected actions and how our agent behaves in relation to them.The clearest mindset shift is toembrace controlled unpredictability,that is, unlike deterministic service calls, agents make decisions at runtime that can generate different paths to the same destination.

* Service discovery becomes agent discovery.
* Routing becomes orchestration.
* Rate limiting becomes resource governance.

Ultimately, what does this mean?Wemust be critical in understanding and specifying what success is, and what it looks like,rather than a step-by-step description of how to achieve it.

In the traditional model, the path is fixed: one service calls another in a predefined order, like a script.In the agentic approach, an AI model chooses which services to use on the fly, based on context.Microservices become toolsthatAI triggersas needed.

Here, theMCPshines by standardising how AI agents receive contextual information, access tools, and process events.The MCP establishes a consistent interface layer between agents and the microservices they orchestrate.

## The "Aha!" Moment: Breaking the Monolithic Medical Mind

Traditional medical systems are like that one doctor who needs everything written down in triplicate:

* "Process this lab result"
* "Store that patient record"
* "Send this notification"

But what if your system could think like a medical resident who sees a glucose reading of350mg/dLand immediately starts a cascade of intelligent reasoning:

"Critical hyperglycemia... let me check this patient's history... ah, diabetic with poor control... this needs urgent endocrinology intervention within 24 hours."

That's exactly what happens when you marryautonomous AI agentswithevent-driven microservices architecture.

## The Agent Coordinator: Your Medical Analysis Conductor 🎼

At the heart of ouragents-microservices systemsits what we call theAgent Coordinator—built withVoltAgentfor maximum flexibility and powered by Amazon Nova Micro for medical reasoning.

Here's the real code from our system:

// From our actual agent-coordinator implementation

import

{

VoltAgent
,

Agent

}

from

"
@voltagent/core
"
;

import

{

VercelAIProvider

}

from

"
@voltagent/vercel-ai
"
;

import

{

BedrockRuntime

}

from

"
@aws-sdk/client-bedrock-runtime
"
;

export

class

MedicalAgentCoordinator

{


private

agent
:

Agent
;


private

memory
:

DynamoDBMemoryStore
;


private

eventBridge
:

EventBridgeClient
;


constructor
()

{


this
.
agent

=

new

Agent
({


name
:

"
medical-analysis-coordinator
"
,


instructions
:

`You are a medical analysis coordinator.
 Analyze laboratory results and patient history to determine:
 - Clinical urgency (0-24h, 1-7d, 30-90d)
 - Required specialists (endocrinology, cardiology, nephrology)
 - Risk factors and follow-up needs`
,


llm
:

new

VercelAIProvider
(),


model
:

novaMicro
(
"
nova-micro-v1
"
),


});


}

}

Enter fullscreen mode

Exit fullscreen mode

### The EventSymphonyBegins

When a lab result hits our S3 bucket, here's what happens:

// S3 triggers the event cascade

export

const

s3TriggerHandler

=

async
(
event
:

S3Event
)

=>

{


for
(
const

record

of

event
.
Records
)

{


const

{

bucket
,

object

}

=

record
.
s3
;


// Extract lab data


const

labData

=

await

extractLabResults
(
bucket
.
name
,

object
.
key
);


// Agent analyzes with full context


const

analysis

=

await

this
.
agent
.
analyze
({


labResults
:

labData
,


patientHistory
:

await

this
.
memory
.
getPatientContext
(
patientId
),


clinicalProtocols
:

MEDICAL_GUIDELINES


});


// Publish intelligent events based on analysis


await

this
.
publishMedicalEvents
(
analysis
);


}

};

Enter fullscreen mode

Exit fullscreen mode

## The Beautiful Event Cascade: Intelligence Breeding Intelligence

Here's where it gets sexy (in a nerdy way). Each agent decision createstyped eventsthat trigger specialized responses:

### Event 1: Medical Analysis Complete

interface

MedicalAnalysisEvent

{


eventType
:

'
medical.analysis.complete
'
;


patientId
:

string
;


findings
:

{


glucose
:

number
;


priority
:

'
URGENT
'

|

'
PRIORITY
'

|

'
ROUTINE
'
;


riskFactors
:

string
[];


};


recommendations
:

{


specialty
:

'
endocrinology
'

|

'
cardiology
'

|

'
nephrology
'

|

'
generalist
'
;


timeframe
:

'
0-24h
'

|

'
1-7d
'

|

'
30-90d
'
;


};

}

Enter fullscreen mode

Exit fullscreen mode

### Event 2: Memory Update Triggered

// The agent's persistent memory system

export

class

DynamoDBMemoryStore

{


async

updatePatientMemory
(
event
:

MedicalAnalysisEvent
)

{


const

memoryUpdate

=

{


patientId
:

event
.
patientId
,


lastAnalysis
:

event
.
findings
,


riskTrend
:

this
.
calculateRiskTrend
(
event
.
findings
),


urgentFlags
:

event
.
findings
.
priority

===

'
URGENT
'

?


[...
existing
.
urgentFlags
,

event
.
findings
]

:

existing
.
urgentFlags


};


await

this
.
dynamodb
.
putItem
({


TableName
:

'
PatientMemory
'
,


Item
:

memoryUpdate


});


// Publish memory update event for other agents


await

this
.
eventBridge
.
publish
(
'
patient.memory.updated
'
,

memoryUpdate
);


}

}

Enter fullscreen mode

Exit fullscreen mode

### Event 3: Appointment Creation Orchestrated

// Autonomous appointment scheduling based on medical urgency

export

const

appointmentHandler

=

async
(
event
:

MedicalAnalysisEvent
)

=>

{


const

appointmentData

=

{


patientId
:

event
.
patientId
,


specialty
:

event
.
recommendations
.
specialty
,


urgency
:

event
.
recommendations
.
timeframe
,


reason
:

`
${
event
.
findings
.
riskFactors
.
join
(
'
,
'
)}
 - Priority:
${
event
.
findings
.
priority
}
`
,


medicalContext
:

event
.
findings


};


await

this
.
eventBridge
.
publish
(
'
appointment.create.request
'
,

appointmentData
);

};

Enter fullscreen mode

Exit fullscreen mode

The beauty?Each microservice is autonomous. The appointment service doesn't need to understand medical analysis—it just responds to appointment events. The memory system doesn't care about scheduling—it maintains patient context and publishes memory updates.

## The Agent's Secret Sauce: VoltAgent's Flexible Memory

Here's where our approach gets innovative. Instead of using traditional vector databases for memory, we built aflexible DynamoDB-based memory systemthat gives our agents true persistence:

// Our custom memory implementation

interface

PatientMemoryContext

{


patientId
:

string
;


clinicalHistory
:

MedicalEvent
[];


glucosePattern
:

{


trend
:

'
improving
'

|

'
stable
'

|

'
declining
'
;


criticalEpisodes
:

number
;


lastCritical
:

Date
;


};


medications
:

CurrentMedication
[];


riskFactors
:

ClinicalRiskFactor
[];


preferences
:

PatientPreferences
;

}

// The agent reasons with full context

const

decision

=

await

this
.
agent
.
analyze
({


currentLab
:

newResults
,


context
:

await

this
.
memory
.
getFullContext
(
patientId
),


protocols
:

CLINICAL_GUIDELINES

});

Enter fullscreen mode

Exit fullscreen mode

### Why Not Vector Databases?

Vector databases are great for similarity search, but medical reasoning needsstructured, relational context:

* Temporal relationships: "Patient's glucose has been trending upward for 6 months"
* Clinical protocols: "Given diabetes + high creatinine, nephrology consultation needed"
* Patient-specific patterns: "This patient's glucose spikes correlate with medication non-adherence"

Our DynamoDB approach gives us:

* Structured medical relationships
* ACID transactionsfor critical medical data
* Query flexibilityfor complex medical reasoning
* Cost efficiencyat scale

## The Clinical Protocol Engine: Real Medical Intelligence

Our agents don't just wing it—they follow evidence-based medical protocols:

const

CLINICAL_PROTOCOLS

=

{


glucose
:

{


critical_high
:

{


threshold
:

300
,


urgency
:

'
0-24h
'
,


specialty
:

'
endocrinology
'
,


actions
:

[
'
immediate_notification
'
,

'
urgent_appointment
'
,

'
medication_review
'
]


},


critical_low
:

{


threshold
:

50
,


urgency
:

'
0-24h
'
,


specialty
:

'
emergency
'
,


actions
:

[
'
immediate_notification
'
,

'
emergency_protocol
'
]


}


},


creatinine
:

{


acute_elevation
:

{


threshold
:

3.0
,


urgency
:

'
0-24h
'
,


specialty
:

'
nephrology
'
,


actions
:

[
'
kidney_function_assessment
'
,

'
medication_adjustment
'
]


}


},


combined_risk
:

{


diabetes_kidney
:

{


conditions
:

[
'
high_glucose
'
,

'
elevated_creatinine
'
],


urgency
:

'
0-24h
'
,


specialty
:

'
endocrinology
'
,


coordination
:

[
'
nephrology_consult
'
]


}


}

};

Enter fullscreen mode

Exit fullscreen mode

## The VoltAgent Advantage: Beyond Simple Frameworks

VoltAgentgives us something special—a framework that bridges the gap between simple AI tools and complex enterprise needs:

// VoltAgent's workflow engine for complex medical processes

import

{

createWorkflowChain
,

andThen
,

andAgent

}

from

"
@voltagent/core
"
;

const

medicalAnalysisWorkflow

=

createWorkflowChain
({


id
:

"
medical-analysis-workflow
"
,


name
:

"
Comprehensive Medical Analysis
"
,


input
:

z
.
object
({


labResults
:

z
.
object
({


glucose
:

z
.
number
(),


creatinine
:

z
.
number
(),


hba1c
:

z
.
number
()


}),


patientId
:

z
.
string
()


})

})

.
andThen
({


name
:

"
fetch-patient-context
"
,


execute
:

async
(
data
)

=>

({


...
data
,


patientHistory
:

await

memory
.
getPatientContext
(
data
.
patientId
)


})

})

.
andAgent
(


(
data
)

=>

`Analyze these lab results:
${
JSON
.
stringify
(
data
.
labResults
)}

 for patient with history:
${
JSON
.
stringify
(
data
.
patientHistory
)}
`
,


medicalAgent
,


{

schema
:

MedicalAnalysisSchema

}

)

.
andThen
({


name
:

"
publish-medical-events
"
,


execute
:

async
(
data
)

=>

{


await

eventBridge
.
publishMedicalEvents
(
data
.
analysis
);


return

{

success
:

true
,

eventsPublished
:

data
.
analysis
.
events
.
length

};


}

});

Enter fullscreen mode

Exit fullscreen mode

Why VoltAgent over other frameworks?

* Modular architecture- Add voice, memory, or custom tools as needed
* Workflow orchestration- Complex medical processes, not just chat
* Provider flexibility- Switch between OpenAI, Anthropic, or Amazon models
* Enterprise-ready- Built for production, not just prototypes

## The Challenges: Let's Be Real

* PROMISE: "AI will automate complex workflows!"
* REALITY: "AI will consume your cloud budget, testing a zillion variations
of the same prompt to decide whether to call service A or B."

### First:

Agents only perform well if the interfaces they use are good. Poorly defined APIs, inconsistent behaviours, or poorly handled errors lead to ruined decisions. Unlike human developers, agents don't "guess"—they only act based on what they understand. Therefore, clarity, consistency, and good observability are essential.

### Second:

Agents bring uncertainty. Because actions are dynamic, planning is probabilistic, and results can vary. This requires new ways of testing, validating, and auditing workflows—not just with unit tests, but by looking at overall behaviour.

Building agentic medical systems isn't all sunshine and autonomous decisions. Here are the real challenges:

### 1.Medical Liability & Compliance

// Every decision must be auditable

interface

MedicalDecisionAudit

{


timestamp
:

Date
;


agentVersion
:

string
;


inputData
:

LabResults
;


reasoning
:

string
;


decision
:

MedicalRecommendation
;


protocolsApplied
:

string
[];


humanOversight
:

boolean
;

}

Enter fullscreen mode

Exit fullscreen mode

### 2.Event Ordering & Consistency

Medical events aren't always orderly. Lab results can arrive out of sequence, and agents must handle:

* Out-of-order events: "Lab from 2 days ago just arrived"
* Concurrent updates: Multiple agents updating patient memory simultaneously
* Temporal reasoning: Understanding medical timelines

### 3.Context Window Limitations

Even with persistent memory, agents have context limits:

// Smart context management for medical reasoning

class

MedicalContextManager

{


async

getRelevantContext
(
patientId
:

string
,

currentIssue
:

string
)

{


const

fullHistory

=

await

this
.
memory
.
getPatientHistory
(
patientId
);


// Intelligent context selection based on medical relevance


return

{


recentCritical
:

fullHistory
.
filter
(
event

=>


event
.
priority

===

'
URGENT
'

&&


this
.
isRecentlyRelevant
(
event
,

currentIssue
)


).
slice
(
0
,

10
),


chronicConditions
:

fullHistory
.
filter
(
event

=>


event
.
type

===

'
chronic_condition
'


),


medicationHistory
:

this
.
getRelevantMedications
(
fullHistory
,

currentIssue
)


};


}

}

Enter fullscreen mode

Exit fullscreen mode

### 4.The Memory Trade-off

Our structured memory approach trades some flexibility for medical accuracy:

Pros:

* Precise medical relationships
* ACID compliance for critical data
* Complex query capabilities
* Cost-effective at scale

Cons:

* Less flexible than vector search
* Requires structured medical ontology
* Manual schema evolution
* Complex relationship management

## The Real Magic: Medical Events in Action

Let's walk through a real scenario from our test suite:

// Test case: Critical hyperglycemia with kidney involvement

const

testScenario

=

{


patientId
:

"
patient-456
"
,


labResults
:

{


glucose
:

380
,

// Critical high


creatinine
:

2.8
,

// Elevated but not critical


hba1c
:

12.5

// Poor long-term control


},


patientHistory
:

{


conditions
:

[
"
type2_diabetes
"
,

"
hypertension
"
],


medications
:

[
"
metformin
"
,

"
lisinopril
"
],


lastVisit
:

"
2024-08-15
"


}

};

// Agent reasoning chain:

// 1. "Glucose 380 = URGENT (>300 threshold)"

// 2. "Creatinine 2.8 + diabetes = kidney concern"

// 3. "Combined risk = endocrinology + nephrology coordination"

// 4. "Generate events for urgent care"

const

expectedEvents

=

[


{


type
:

'
appointment.urgent.endocrinology
'
,


timeframe
:

'
0-24h
'
,


reason
:

'
Critical hyperglycemia with kidney involvement
'


},


{


type
:

'
consultation.nephrology
'
,


priority
:

'
high
'
,


reason
:

'
Diabetic kidney disease progression
'


},


{


type
:

'
medication.review.urgent
'
,


focus
:

'
glucose_control_optimization
'


}

];

Enter fullscreen mode

Exit fullscreen mode

## The Future: Scaling Medical Intelligence

This architecture isn't just about one agent—it's aboutecosystems of medical intelligencewhere we can place agent workflows that can communicate through event brokers

// Multi-specialty agent coordination

const

medicalSpecialistNetwork

=

{


endocrinology
:

new

MedicalAgent
({

specialty
:

'
diabetes_management
'

}),


cardiology
:

new

MedicalAgent
({

specialty
:

'
cardiovascular_risk
'

}),


nephrology
:

new

MedicalAgent
({

specialty
:

'
kidney_function
'

}),


emergency
:

new

MedicalAgent
({

specialty
:

'
critical_care
'

})

};

// Intelligent consultation routing

const

coordinateSpecialists

=

async
(
medicalFindings
)

=>

{


const

relevantSpecialists

=

determineSpecialists
(
medicalFindings
);


const

consultations

=

await

Promise
.
all
(


relevantSpecialists
.
map
(
specialist

=>


specialist
.
consult
(
medicalFindings
,

patientContext
)


)


);


return

synthesizeRecommendations
(
consultations
);

};

Enter fullscreen mode

Exit fullscreen mode

* 2024: "AI will automate everything!"
* 2025: "AI works best when it collaborates with deterministic systems."
* 2026: "The value is in intelligent orchestration, not total automation."

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
