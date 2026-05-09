---
title: Deploying a Multi-Agent System with Terraform and Cloud Run - DEV Community
url: https://dev.to/googleai/deploying-a-multi-agent-system-with-terraform-and-cloud-run-2a9c
site_name: devto
content_file: devto-deploying-a-multi-agent-system-with-terraform-and
fetched_at: '2026-05-09T19:57:44.566370'
original_url: https://dev.to/googleai/deploying-a-multi-agent-system-with-terraform-and-cloud-run-2a9c
author: Shir Meir Lador
date: '2026-05-07'
description: 'In support of our mission to accelerate the developer journey on Google Cloud, we built Dev Signal: a... Tagged with googlecloud, terraform, ai, agents.'
tags: '#googlecloud, #terraform, #ai, #agents'
---

In support of our mission to accelerate the developer journey on Google Cloud, we built Dev Signal: a multi-agent system designed to transform raw community signals into reliable technical guidance by automating the path from discovery to expert creation.

In the first three parts of this series, we laid the essential groundwork by establishing its core capabilities and local verification process:

Inpart 1, we standardize the agent's capabilities through the Model Context Protocol (MCP), connecting it to Reddit for trend discovery and Google Cloud Docs for technical grounding. Inpart 2, we built a multi-agent architecture and integrated the Vertex AI memory bank to allow the system to learn and persist user preferences across different conversations. Inpart 3, we verified the full end-to-end lifecycle locally using a dedicated test runner to ensure that research, content creation, and cloud-based memory retrieval were perfectly synchronized.

If you'd like to dive straight into the code, you can clone the repositoryhere.

## Deployment to Cloud Run and the Path to Production

To help you transition from this local prototype to a production service, this final part focuses on building the production backbone of your agent using the foundational deployment patterns provided by theAgent Starter Pack. We will implement the essential structural components required for monitoring, data integrity, and long-term state management in the cloud. You will learn to implement the application server and helper utilities needed for a production-ready deployment before provisioning secure, reproducible infrastructure with Terraform.

While the Dockerfile packages your agent's code and its specialized dependencies, such as Node.js for the Reddit MCP tool, Terraform is used to build the platform it lives on. Terraform automates the creation of your Artifact Registry, least-privilege service accounts, and Secret Manager integrations to ensure your API keys remain protected.

By the end of this part, you will have a standardized application framework deployed on Google Cloud Run and a roadmap for graduating your prototype through continuous evaluation, CI/CD and advanced observability.

## Production Utilities and Server: Building the System's Body

In this section, you implement the structural components required for monitoring and long-term state management in the cloud.

* The Application Server:Initializing the FastAPI server and establishing a vital connection to the Vertex AI memory bank.
* Implementing Telemetry:Enabling 'Agent Traces' for visibility into internal reasoning.

### The Application Server

Thefast_api_app.pyfile serves as the vital entry point for your agent, transforming the core logic into a production FastAPI server that acts as the "body" of your system. When deploying to Cloud Run, this server is essential because it provides the necessary web interface to listen for incoming HTTP requests and dispatch them to the agent for processing. Beyond basic serving, its most critical role is establishing a connection to the Vertex AI memory bank by defining aMEMORY_URI, which allows the ADK framework to persist and retrieve user preferences across different production sessions. Additionally, the application server initializes production-grade telemetry for real-time monitoring.

Go back to thedev_signal_agent folder.

cd
 ..

Enter fullscreen mode

Exit fullscreen mode

Paste the following code indev_signal_agent/fast_api_app.py:

import
 
os

from
 
fastapi
 
import
 
FastAPI

from
 
google.adk.cli.fast_api
 
import
 
get_fast_api_app

from
 
google.cloud
 
import
 
logging
 
as
 
cloud_logging

from
 
vertexai
 
import
 
agent_engines

from
 
dev_signal_agent.app_utils.env
 
import
 
init_environment

# --- Initialization & Secure Secret Retrieval ---
# We now unpack the SECRETS dictionary returned by our updated env.py

PROJECT_ID
,
 
MODEL_LOC
,
 
SERVICE_LOC
,
 
SECRETS
 
=
 
init_environment
()

logger
 
=
 
cloud_logging
.
Client
().
logger
(
__name__
)

# Access sensitive credentials from the SECRETS dictionary
# These keys stay in memory and are NOT injected into os.environ

REDDIT_CLIENT_ID
 
=
 
SECRETS
.
get
(
"
REDDIT_CLIENT_ID
"
)

REDDIT_CLIENT_SECRET
 
=
 
SECRETS
.
get
(
"
REDDIT_CLIENT_SECRET
"
)

REDDIT_USER_AGENT
 
=
 
SECRETS
.
get
(
"
REDDIT_USER_AGENT
"
)

DK_API_KEY
 
=
 
SECRETS
.
get
(
"
DK_API_KEY
"
)

# --- Configuration & Sessions ---

AGENT_DIR
 
=
 
os
.
path
.
dirname
(
os
.
path
.
dirname
(
os
.
path
.
abspath
(
__file__
)))

# Non-sensitive configuration uses environment variables

BUCKET
 
=
 
os
.
environ
.
get
(
"
AI_ASSETS_BUCKET
"
)

USE_IN_MEMORY
 
=
 
os
.
environ
.
get
(
"
USE_IN_MEMORY_SESSION
"
,
 
""
).
lower
()
 
in
 
(
"
true
"
,
 
"
1
"
)

# --- MEMORY BANK CONNECTION ---

def
 
_get_memory_bank_uri
():

 
if
 
USE_IN_MEMORY
:
 
return
 
None
,
 
None

 
# We use 'dev_signal_agent' as the display name for the Vertex AI memory bank

 
name
 
=
 
os
.
environ
.
get
(
"
AGENT_ENGINE_MEMORY_BANK_NAME
"
,
 
"
dev_signal_agent
"
)

 
existing
 
=
 
list
(
agent_engines
.
list
(
filter
=
f
"
display_name=
{
name
}
"
))

 
ae
 
=
 
existing
[
0
]
 
if
 
existing
 
else
 
agent_engines
.
create
(
display_name
=
name
)

 
uri
 
=
 
f
"
agentengine://
{
ae
.
resource_name
}
"

 
print
(
f
"
DEBUG: Connecting to Memory Bank: 
{
uri
}
 (display_name=
{
name
}
)
"
)

 
return
 
uri
,
 
uri

SESSION_URI
,
 
MEMORY_URI
 
=
 
_get_memory_bank_uri
()

# --- Initialize FastAPI with ADK ---

app
:
 
FastAPI
 
=
 
get_fast_api_app
(

 
agents_dir
=
AGENT_DIR
,

 
web
=
True
,

 
artifact_service_uri
=
f
"
gs://
{
BUCKET
}
"
 
if
 
BUCKET
 
else
 
None
,

 
allow_origins
=
os
.
getenv
(
"
ALLOW_ORIGINS
"
,
 
""
).
split
(
"
,
"
)
 
if
 
os
.
getenv
(
"
ALLOW_ORIGINS
"
)
 
else
 
None
,

 
session_service_uri
=
SESSION_URI
,

 
memory_service_uri
=
MEMORY_URI
,
 
# <--- Connects the Memory Bank

 
otel_to_cloud
=
True
,
 
# <--- Enables production telemetry

)

if
 
__name__
 
==
 
"
__main__
"
:

 
import
 
uvicorn

 
# Standard Cloud Run port is 8080

 
uvicorn
.
run
(
app
,
 
host
=
"
0.0.0.0
"
,
 
port
=
8080
)

Enter fullscreen mode

Exit fullscreen mode

### Implementing Telemetry

In a production environment, visibility into your agent's reasoning is critical. We leverage the built-in observability features of the Google ADK by setting theotel_to_cloud=Trueflag in our application server. This single parameter handles the majority of the instrumentation automatically, exporting "Agent Traces" directly to the Google Cloud Console. These traces provide a "visual waterfall" of the agent's operation, including individual agent thought processes, LLM invocations, and MCP tool calls.

#### Monitoring vs. Targeted Evaluation

It is essential to understand that production tracing is subject to sampling to balance performance and cost. Because Cloud Run captures only a subset of requests, not every individual user interaction will be visible.

* System Traces (Monitoring):Used to analyze behavior "at large," such as identifying latency bottlenecks or system timeouts.
* Reasoning Traces (Evaluation):High-quality evaluation mandates targeted trace capture. This means calling the agent specifically for a test case where you know you will evaluate that particular request in full detail.

#### Viewing the Trace

To see your traces, navigate to the Trace Explorer in the Google Cloud Console and filter for your service (e.g.,dev-signal). Clicking a specific Trace ID opens a Gantt chart that allows you to distinguish between cognitive reasoning failures (wrong decisions) and physical system issues (timeouts).

For advanced configurations, refer to the following documentation:

* Cloud Run Trace Sampling
* Configuring ADK Telemetry
* Multimodal Trace Capture
* BigQuery Agent Analytics Integration

## Infrastructure as Code: Provisioning Secure Cloud Resources

We utilize the infrastructure-as-code patterns provided by theAgent Starter Pack's security-first design. The starter pack builds the professional platform required to automate the creation of least-privilege service accounts and robust secret management in seconds.

Using Terraform ensures that your entire Google Cloud environment - from IAM roles to Secret Manager versions - is defined in reproducible, secure code. We break our infrastructure into the following logical blocks:

* Resources & Variables: Define the specific project, region, and sensitive API secrets used by the agent.
* Core Infrastructure: Enable essential APIs and provision a private Artifact Registry to host your agent's container images.
* Identity & Access Management (IAM): Configure specialized Service Accounts that strictly follow the Principle of Least Privilege to ensure your system remains secure.
* Secret Management: Securely ingest API credentials into Google Secret Manager for protected runtime access.
* Cloud Run Configuration: Define the container environment, resource limits, and automated secret injection for the final deployment.

To begin provisioning, return to the root folder of your project (dev-signal) and create the necessary deployment directories:

cd
 ..

mkdir 
deployment

cd 
deployment

mkdir 
terraform

cd 
terraform

Enter fullscreen mode

Exit fullscreen mode

### Terraform Resources and Variables

Thevariables.tffile defines the configurable parameters for your deployment, allowing you to customize the infrastructure without altering the underlying logic. It includes variables for theproject_id, the deploymentregion(defaulting tous-central1), and theservice_namefor your Cloud Run instance. Furthermore, it defines asecretsmap used to securely ingest sensitive API credentials—such as Reddit and Developer Knowledge keys—into Google Secret Manager for runtime access. This modular approach ensures your production environment remains reproducible, secure, and adaptable across different projects.

Paste the following code intodeployment/terraform/variables.tf:

variable
 
"project_id"
 
{

 
description
 
=
 
"The Google Cloud Project ID"

 
type
 
=
 
string

}

variable
 
"region"
 
{

 
description
 
=
 
"The Google Cloud region to deploy to"

 
type
 
=
 
string

 
default
 
=
 
"us-central1"

}

variable
 
"service_name"
 
{

 
description
 
=
 
"The name of the Cloud Run service"

 
type
 
=
 
string

 
default
 
=
 
"dev-signal"

}

variable
 
"secrets"
 
{

 
description
 
=
 
"A map of secret names and their values (e.g., REDDIT_CLIENT_ID, DK_API_KEY)"

 
type
 
=
 
map
(
string
)

 
default
 
=
 
{}

}

variable
 
"ai_assets_bucket"
 
{

 
description
 
=
 
"The GCS bucket for storing AI assets"

 
type
 
=
 
string

}

Enter fullscreen mode

Exit fullscreen mode

### Core Infrastructure Logic

We define our infrastructure in logical blocks. Here is what each part does:

1. Enable APIs: Ensures the project has the necessary services active (Cloud Run, Vertex AI, etc.). We usedisable_on_destroy = falseto prevent accidental data loss if the Terraform is destroyed.

Paste the following code intodeployment/terraform/main.tf:

resource
 
"google_project_service"
 
"services"
 
{

 
project
 
=
 
var
.
project_id

 
for_each
 
=
 
toset
([

 
"run.googleapis.com"
,

 
"artifactregistry.googleapis.com"
,

 
"cloudbuild.googleapis.com"
,

 
"aiplatform.googleapis.com"
,

 
"secretmanager.googleapis.com"
,

 
"logging.googleapis.com"

 
])

 
service
 
=
 
each
.
key

 
disable_on_destroy
 
=
 
false

}

Enter fullscreen mode

Exit fullscreen mode

2. Artifact Registry: Creates a private Docker registry to store our agent's container images.

resource
 
"google_artifact_registry_repository"
 
"repo"
 
{

 
location
 
=
 
var
.
region

 
project
 
=
 
var
.
project_id

 
repository_id
 
=
 
"dev-signal-repo"

 
description
 
=
 
"Docker repository for Dev Signal Agent"

 
format
 
=
 
"DOCKER"

 
depends_on
 
=
 
[
google_project_service
.
services
]

}

Enter fullscreen mode

Exit fullscreen mode

3. Service Account & IAM: Adhering to the Principle of Least Privilege- This is a critical security step. In accordance with the Principle of Least Privilege, we avoid using the default compute service account and instead provision a dedicated user-managed service account (dev-signal-sa). By designating this as the Cloud Run service identity, we can grant it only the minimum necessary permissions—specificallyroles/aiplatform.user,roles/logging.logWriter, androles/storage.objectAdmin. This granular access control ensures that the agent has the exact permissions required to interact with Vertex AI and Cloud Storage without over-granting access to other sensitive cloud resources, significantly reducing the potential impact of a compromised account. Learn morebest practices for using service accounts securely.

resource
 
"google_service_account"
 
"agent_sa"
 
{

 
project
 
=
 
var
.
project_id

 
account_id
 
=
 
"${var.service_name}-sa"

 
display_name
 
=
 
"Dev Signal Agent Service Account"

}

Enter fullscreen mode

Exit fullscreen mode

4. Secret Management: This handles your API keys securely. It creates secrets in Google Secret Manager and gives the agent's Service Account permission to access them at runtime.

resource
 
"google_secret_manager_secret"
 
"agent_secrets"
 
{

 
project
 
=
 
var
.
project_id

 
for_each
 
=
 
toset
(
keys
(
var
.
secrets
))

 
secret_id
 
=
 
each
.
key

 
replication
 
{

 
auto
 
{}

 
}

 
depends_on
 
=
 
[
google_project_service
.
services
]

}

resource
 
"google_secret_manager_secret_version"
 
"agent_secrets_version"
 
{

 
for_each
 
=
 
toset
(
keys
(
var
.
secrets
))

 
secret
 
=
 
google_secret_manager_secret
.
agent_secrets
[
each
.
key
].
id

 
secret_data
 
=
 
var
.
secrets
[
each
.
key
]

}

resource
 
"google_secret_manager_secret_iam_member"
 
"secret_accessor"
 
{

 
project
 
=
 
var
.
project_id

 
for_each
 
=
 
toset
(
keys
(
var
.
secrets
))

 
secret_id
 
=
 
google_secret_manager_secret
.
agent_secrets
[
each
.
key
].
id

 
role
 
=
 
"roles/secretmanager.secretAccessor"

 
member
 
=
 
"serviceAccount:${google_service_account.agent_sa.email}"

}

Enter fullscreen mode

Exit fullscreen mode

5. Cloud Run Configuration:

Security Best Practice:To satisfy production security standards, ourmain.tfgrants the Service Account thesecretmanager.secretAccessorrole. Our Python application then uses theSecret Manager SDKto pull these credentials directly into local memory at runtime, ensuring they never touch the container's environment configuration

# 6. Cloud Run Service Deployment

resource
 
"google_cloud_run_v2_service"
 
"default"
 
{

 
project
 
=
 
var
.
project_id

 
name
 
=
 
var
.
service_name

 
location
 
=
 
var
.
region

 
ingress
 
=
 
"INGRESS_TRAFFIC_ALL"

 
template
 
{

 
service_account
 
=
 
google_service_account
.
agent_sa
.
email

 
containers
 
{

 
image
 
=
 
"us-docker.pkg.dev/cloudrun/container/hello"
 
# Placeholder until first build

 
env
 
{

 
name
 
=
 
"GOOGLE_CLOUD_PROJECT"

 
value
 
=
 
var
.
project_id

 
}

 
env
 
{

 
name
 
=
 
"GOOGLE_CLOUD_LOCATION"

 
value
 
=
 
"global"

 
}

 
env
 
{

 
name
 
=
 
"GOOGLE_GENAI_USE_VERTEXAI"

 
value
 
=
 
"True"

 
}

 
env
 
{

 
name
 
=
 
"AI_ASSETS_BUCKET"

 
value
 
=
 
var
.
ai_assets_bucket

 
}

 
resources
 
{

 
limits
 
=
 
{

 
cpu
 
=
 
"1"

 
memory
 
=
 
"2Gi"

 
}

 
}

 
}

 
}

 
traffic
 
{

 
type
 
=
 
"TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST"

 
percent
 
=
 
100

 
}

Enter fullscreen mode

Exit fullscreen mode

### Provision the Infrastructure

Before we can deploy our code, we need to provision the Google Cloud infrastructure we just defined.

Initialize Terraform: This downloads the necessary provider plugins. Run this indeployment/terraformfolder:

terraform init

Enter fullscreen mode

Exit fullscreen mode

Create a Variables File:

Paste this code indeployment/terraform/terraform.tfvarsand update it with your project details and secrets.

project_id
 
=
 
"your-project-id"

region
 
=
 
"us-central1"

service_name
 
=
 
"dev-signal"

ai_assets_bucket
 
=
 
"your-bucket-name"

secrets
 
=
 
{

 
REDDIT_CLIENT_ID
 
=
 
"your_client_id"

 
REDDIT_CLIENT_SECRET
 
=
 
"your_client_secret"

 
REDDIT_USER_AGENT
 
=
 
"your_user_agent"

 
DK_API_KEY
 
=
 
"your_dk_api_key"

}

Enter fullscreen mode

Exit fullscreen mode

Plan configuration: This allows you to review the changes before they are applied. Run this in thedeployment/terraformfolder:

terraform plan 
-out
=
plan.tfplan

Enter fullscreen mode

Exit fullscreen mode

Apply Configuration: Once you have reviewed the plan and confirmed it does what you want, run:

terraform apply plan.tfplan

Enter fullscreen mode

Exit fullscreen mode

## Deployment: Containerization and the Cloud Build Pipeline

In this final stage of the build process, we package our agent's "body" and "brain" into a portable, production-ready container. This ensures that every component - from our Python logic to the Node.js environment required for the Reddit MCP tool - is bundled together with its exact dependencies.

We utilize aDockerfileto define this environment and aMakefileto orchestrate the deployment pipeline. When you trigger the deployment,Google Cloud Buildtakes your local source code, builds the container image according to the Dockerfile, and stores it in the private Artifact Registry created earlier by Terraform. Finally, the pipeline automatically updates your Cloud Run service to serve traffic using this fresh image, completing the journey from local code to a live, secure cloud workload.

Paste this code indev-signal/Dockerfile:

FROM
 python:3.12-slim

# Install Node.js and npm for MCP tools (like reddit-mcp)

RUN 
apt-get update 
&&
 apt-get 
install
 
-y
 
\

 curl 
\

 
&&
 curl 
-fsSL
 https://deb.nodesource.com/setup_20.x | bash - 
\

 
&&
 apt-get 
install
 
-y
 nodejs 
\

 
&&
 npm 
install
 
-g
 reddit-mcp 
\

 
&&
 apt-get clean 
\

 
&&
 
rm
 
-rf
 /var/lib/apt/lists/
*

RUN 
pip 
install
 
--no-cache-dir
 
uv
==
0.8.13

WORKDIR
 /code

COPY
 ./pyproject.toml ./README.md ./uv.lock* ./

COPY
 ./dev_signal_agent ./dev_signal_agent

RUN 
uv 
sync
 
--frozen

EXPOSE
 8080

CMD
 ["uv", "run", "uvicorn", "dev_signal_agent.fast_api_app:app", "--host", "0.0.0.0", "--port", "8080"]

Enter fullscreen mode

Exit fullscreen mode

TheMakefileautomates the build and deploys.

Paste this code indev-signal/Makefile:

PROJECT_ID
 
?=
 
$(
shell gcloud config get-value project
)

REGION
 
?=
 us-central1

IMAGE_REPO
 
?=
 dev-signal-repo

IMAGE
 
:=
 
$(
REGION
)
-docker
.pkg.dev/
$(
PROJECT_ID
)
/
$(
IMAGE_REPO
)
/agent:latest

# Deploy via Cloud Build & Container

docker-deploy
:

 
@
echo
 
"? Building and deploying to 
$(
PROJECT_ID
)
 via Cloud Build..."

 gcloud builds submit 
--tag
 
$(
IMAGE
)
 
--project
 
$(
PROJECT_ID
)
 .
 gcloud run services update dev-signal 
\

 
--image
 
$(
IMAGE
)
 
\

 
--region
 
$(
REGION
)
 
\

 
--project
 
$(
PROJECT_ID
)
 
\

 
--labels
 dev-tutorial
=
dev-signal-agent

Enter fullscreen mode

Exit fullscreen mode

### Deploy Application

Now that our infrastructure is ready, we can build and deploy the application code.

Run the following command from the root of your project:

make docker-deploy

Enter fullscreen mode

Exit fullscreen mode

What happens when you run this?

1. Build: Google Cloud Build takes your local code and theDockerfile, builds a container image, and stores it in the Artifact Registry.
2. Deploy: It updates the Cloud Run service defined in Terraform to use this new image.

When the deployment completes, you should get a message like this:

Service [dev-signal] revision [dev-signal...] has been deployed and is serving 100 percent of traffic.

Service URL: https://dev-signal-...-.us-central1.run.app

## Verification: Accessing and Testing Your Deployed Agent

Since production services are private by default, this section covers how to grant permissions and access the agent securely.

Managing IAM Permissions:Granting the necessaryrun.invokerrole to authorized users.

Secure Access via Cloud Run Proxy:Using thegcloudproxy to interact with your live service.

### Granting User Permissions

Before you can invoke the service, you must grant your Google account theroles/run.invokerrole for this specific service. Run the following command:

gcloud run services add-iam-policy-binding dev-signal 
\

 
--member
=
"user:
$(
gcloud config get-value account
)
"
 
\

 
--role
=
"roles/run.invoker"
 
\

 
--region
=
us-central1 
\

 
--project
=
$(
gcloud config get-value project
)

Enter fullscreen mode

Exit fullscreen mode

### Launch the Proxy

Now, access your private service securely via the proxy:

gcloud run services proxy dev-signal 
\

 
--region
 us-central1 
\

 
--project
 
$(
gcloud config get-value project
)

Enter fullscreen mode

Exit fullscreen mode

Visithttp://localhost:8080to chat with your deployed agent! See a possible test scenario inpart 3of the series.

## Summary

Congratulations! You have successfully builtDev Signal.

What we covered:

1. Tooling (MCP): You connected your agent toReddit,Google Docs, and aLocal Image Generatorusing the Model Context Protocol.
2. Architecture: You implemented aRoot Orchestratormanaging specialized agents (Scanner, Expert, Drafter).
3. Memory: You integratedVertex AI memory bankto give your agent long-term persistence across sessions.
4. Production: You deployed the entire stack toGoogle Cloud RunusingTerraformfor secure, reproducible infrastructure.

You now have a solid foundation for building sophisticated, stateful AI applications on Google Cloud.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse