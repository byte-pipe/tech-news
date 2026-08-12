---
title: 'Agent Sandboxes: Giving AI Agents Their Own Little Linux Box (And Why You Should Care) - DEV Community'
url: https://dev.to/gde/agent-sandboxes-giving-ai-agents-their-own-little-linux-box-and-why-you-should-care-jl4
site_name: devto
content_file: devto-agent-sandboxes-giving-ai-agents-their-own-little
fetched_at: '2026-08-12T11:44:21.954625'
original_url: https://dev.to/gde/agent-sandboxes-giving-ai-agents-their-own-little-linux-box-and-why-you-should-care-jl4
author: Çalgan Aygün
date: '2026-08-07'
description: 'Sourced from: GKE Agent Sandbox docs, kubernetes-sigs/agent-sandbox So here is the thing. We... Tagged with ai, kubernetes, devops, security.'
tags: '#ai, #kubernetes, #devops, #security'
---

Sourced from:GKE Agent Sandbox docs,kubernetes-sigs/agent-sandbox

So here is the thing. We are asking AI agents to do increasingly wild stuff. Write code. Browse the web. Run shell commands. Spin up browsers. Click around. Deploy websites. Use a computer like a human would. And for the most part, they are doing it.

But there is a lurking problem that keeps platform engineers up at night.

Where the hell is this code running?

When you ask an agent to "run this script" or "install this package" or "check if that endpoint responds", you are effectively handing over a loaded gun to a very enthusiastic intern who has read every programming book but has absolutely zero survival instincts. That code could be malicious. Or buggy. Or it could just go nuclear on your host system because the agent decided torm -rf /thinking it was cleaning up temp files.

That is whereAgent Sandboxescome in.

Think of them as giving each agent its own airtight, disposable Linux container. A little VM crib. A playpen with rubber walls where they can run around and break things without ever touching your real infrastructure.

And here is the kicker: this is not some vaporware future concept. Google Cloud ships Agent Sandbox as a managed GKE feature, and the open-source project behind the Kubernetes APIs lives underkubernetes-sigs/agent-sandbox. You can run the open-source controller on your own Kubernetes cluster or use the managed GKE integration.

## What GKE Agent Sandbox Actually Is

Let me quote the docs directly so we are on the same page:

"GKE Agent Sandbox helps you manage isolated, stateful, and single-replica workloads on GKE. It is optimized for use cases like AI agent runtimes, where untrusted, LLM-generated code must be executed in a secure and performant environment."

What that means in plain English is:

You get a Kubernetes-native way to spin up a single, stateful container that behaves like a lightweight VM. It has a stable hostname, persistent storage that survives restarts, kernel-level isolation, and network policies that default to "deny all". Your agent can connect to it, do its thing, disconnect, come back later, and find everything exactly as it left it. Or it can get garbage collected after a TTL and disappear without a trace.

With aSandboxWarmPool, already-started sandboxes can be assigned in milliseconds instead of waiting for a cold Pod to schedule, pull an image, and start. Cold-start latency still depends on your cluster, scheduler, image, and runtime.

## The Architecture: CRDs All the Way Down

The whole thing is built on Kubernetes custom resource definitions. There are four main ones that matter:

### 1. Sandbox (the core)

This is the primitive. A single, stateful Pod with a stable hostname, optional persistent storage, and full lifecycle management. You create this, and the controller handles the rest -- Pod creation, network identity, volume provisioning, scheduled deletion, pausing, and resuming.

It is the answer to the question: "I want a Linux box that stays alive for my agent. How do I get one?"

### 2. SandboxTemplate (the blueprint)

Tired of writing the same YAML over and over? Templates let you codify runtime configuration once -- image, resource limits, runtime class (gVisor, Kata, standard), network policies, environment variables -- and reuse them everywhere. Platform teams define the templates. Developers just pick one and go.

### 3. SandboxClaim (the request)

This is the user-facing abstraction. In the currentv1beta1API, a developer or agent SDK creates aSandboxClaimthat references aSandboxWarmPool. The warm pool references theSandboxTemplate. The controller adopts an available pre-warmed sandbox from that pool, or creates capacity according to the pool configuration, and hands back a ready-to-use environment.

This is theClaim Modelin action. You separate thewhat(I need a sandbox) from thehow(here is where it runs on the cluster). And honestly? This is the pattern Kubernetes has needed for stateful workloads for a long time.

### 4. SandboxWarmPool (the performance hack)

Here is where it gets fast. ASandboxWarmPoolmaintains a set of pre-warmed Pod instances in a ready state. When a claim comes in, the controller instantly assigns a Pod from the pool instead of waiting for image pulls and container startup.

Warm pools reduce provisioning latency by keeping Sandbox instances pre-created and ready to be claimed. On GKE, Pod snapshots are a separate feature that can save and restore sandbox state for pause/resume and faster recovery; they are not required for a warm pool to work.

## Security: Default Deny Is the Only Way

Here is something that does not get talked about enough. When you give an agent a Linux box, you are trusting it with network access. A lot of agent sandbox solutions just throw a container at you and say "good luck".

GKE Agent Sandbox implements aDefault Denynetwork security posture. Out of the box, code inside a sandbox cannot access your internal networks, your GKE control plane, or anything it should not. You explicitly define allowed egress and ingress rules in yourSandboxTemplate.

Why does this matter? Because the most realistic threat from LLM-generated code is not "the AI becomes self-aware and takes over the world". It is "the AI wrote a Python script with a typo that accidentally hit the production database". Default deny prevents the accident. Fine-grained rules let you open specific doors when you need to (e.g., pip needs to reach PyPI, your agent needs to call an API).

## Isolation Runtimes: Pick Your Poison

The Sandbox CRD is runtime-agnostic. You can pair it with:

* Standard containers-- fast, familiar, but minimal isolation between workloads
* gVisor-- Google's user-space kernel. Gives you a second security boundary between your container and the host kernel. This is the recommended default for untrusted code execution.
* Kata Containers-- hardware-level VM isolation. Each sandbox gets its own lightweight VM with its own kernel. The heaviest isolation, but also the strongest.

The beauty of the API is that switching between these is a field change in yourSandboxTemplate. You do not redesign your architecture. You just changeruntimeClassName.

## Programmatic Access SDKs

You do not need to write Kubernetes YAML to use this. There are first-class client libraries:

* Python SDK-- high-level client for LangChain, Vertex AI Agentic SDK, or any Python agent framework. Create, query, manage, and destroy sandboxes from your agent code.
* Go SDK-- for platform engineers building controllers and services on top of Agent Sandbox.

Both SDKs abstract away the claim lifecycle. With the current Python SDK, your agent creates a sandbox withclient.create_sandbox(warmpool="python-sandbox-pool", namespace="default"). Behind the scenes, the SDK creates aSandboxClaim, the controller assigns a Sandbox from the warm pool, and the client returns a handle for command execution and file operations.

## The Comparison Table

Feature

GKE Agent Sandbox (managed)

kubernetes-sigs/agent-sandbox (open source)

Type

Managed GKE add-on

Self-installed Kubernetes controller

CRDs

Sandbox, SandboxTemplate, SandboxClaim, SandboxWarmPool

Sandbox, SandboxTemplate, SandboxClaim, SandboxWarmPool

Provisioning speed

Warm pools reduce claim latency to millisecond-scale assignment

Varies by cluster; warm pools avoid cold-start work

Isolation runtimes

gVisor is required for managed Agent Sandbox workloads

Runtime-agnostic through Kubernetes 
runtimeClassName

Network security

Default deny, fine-grained egress/ingress rules

Configurable via standard K8s NetworkPolicies

Snapshots

GKE Pod snapshots integrate with pause/resume

Platform/runtime dependent; not required for warm pools

SDKs

Python + Go

Python + Go

Lifecycle mgmt

Managed by Google (upgrades, patches)

Self-managed via controller

Limitations

Requires GKE 1.35.2-gke.1269000+ for full feature support

Compatibility is release-specific; pin and test a release

Licensing

Google Cloud SLA

Apache 2.0

Best for

Google Cloud native teams who want "it just works"

Multi-cloud, self-managed, air-gapped environments

## The Practical Takeaway

Agent Sandbox solves a real problem that has been getting more urgent by the month. As LLMs get better at generating code, the volume of untrusted code being executed in agent loops is going to explode. Every one of those executions is an opportunity for something to go wrong.

The old approach was: "just run it in a Docker container, it will be fine." A container can absolutely have a hostname and persistent volumes, but a one-off Docker workflow does not give you the Kubernetes-nativeSandboxlifecycle, claim/warm-pool allocation model, controller-managed identity, or stronger isolation runtime by itself. Those are the abstractions Agent Sandbox is adding.

Agent Sandbox gives you those lifecycle and allocation primitives on top of Kubernetes, with SDKs in Python and Go. Isolation strength still depends on the runtime you configure; the managed GKE feature enforces gVisor for sandbox workloads.

The open-source project underkubernetes-sigs/agent-sandboxis the bedrock. Google's managed GKE add-on is the "press this button and it works" version. Both are worth knowing about.

## A Reality Check (Because Nothing Is Perfect)

Latency is low but not zero.Even with warm pools and Pod snapshots, you are looking at hundreds of milliseconds to a second for sandbox assignment. For most agent use cases that is fine. For real-time loops that need sub-100ms responses, you will feel it.

State management is your problem.A sandbox is stateful by design. But what happens when an agent session crashes mid-execution? Do you keep the sandbox around? For how long? The TTL feature helps, but designing your garbage collection strategy is on you.

Network policy complexity is real.Default deny is great for security. But the first time your agent cannot pip install because egress to PyPI is blocked, you will spend time debugging. And the first time a client's script needs to reach an internal API, you will be writing policy rules. It is manageable. But it is not zero-effort.

Costs add up in warm pools.Each pre-warmed Pod is a running container burning CPU and memory while it waits. If you keep a pool of 20 sandboxes hot, you are paying for 20 idle containers. The pause/resume via Pod snapshots helps offset this, but it is something to budget for.

Monitoring is a blank canvas.Your existing Kubernetes monitoring? Probably set up for Deployments and StatefulSets. Ephemeral sandboxes that live for seconds to minutes are a different monitoring challenge. Log aggregation, metrics collection, cost attribution -- you are building some of this yourself.

## Getting Started

If you want to reproduce the open-source setup on a fresh Kubernetes cluster, the sequence below is complete: install the controllerand extensions, create an executable Python runtime template, create a warm pool, give an in-cluster client the required RBAC, and run the SDK from a normal Python Pod.

The commands below intentionally usekubectl apply -f - <<'EOF'so you do not need to write YAML files locally.

### 1. Install Agent Sandbox with the extension CRDs

As of this writing, the current upstream release isv0.5.3. Pinning the version makes the example reproducible instead of silently changing when a new release lands.

export 
VERSION
=
"v0.5.3"

kubectl apply 
-f
 
\

 https://github.com/kubernetes-sigs/agent-sandbox/releases/download/
${
VERSION
}
/sandbox-with-extensions.yaml

Enter fullscreen mode

Exit fullscreen mode

Wait for the controller components to come up:

kubectl get pods 
-n
 agent-sandbox-system

Enter fullscreen mode

Exit fullscreen mode

Verify that both the core and extension APIs are installed:

kubectl api-resources | 
grep
 
-i
 sandbox

Enter fullscreen mode

Exit fullscreen mode

You should see resources includingsandboxes,sandboxclaims,sandboxtemplates, andsandboxwarmpools.

### 2. Create a Python runtime template and warm pool

A plainpython:3.12-slimcontainer withsleep infinityisnot enoughforsandbox.commands.run(). The SDK sends HTTP requests to the runtime's/executeendpoint on port8888, so the sandbox image must implement that API.

The upstream Python runtime image does exactly that:

kubectl apply 
-f
 - 
<<
'
EOF
'
apiVersion: extensions.agents.x-k8s.io/v1beta1
kind: SandboxTemplate
metadata:
 name: python-sandbox-template
 namespace: default
spec:
 podTemplate:
 spec:
 containers:
 - name: python-sandbox
 image: registry.k8s.io/agent-sandbox/python-runtime-sandbox:v0.1.0
 imagePullPolicy: IfNotPresent
 ports:
 - containerPort: 8888
---
apiVersion: extensions.agents.x-k8s.io/v1beta1
kind: SandboxWarmPool
metadata:
 name: python-sandbox-pool
 namespace: default
spec:
 replicas: 1
 sandboxTemplateRef:
 name: python-sandbox-template

EOF

Enter fullscreen mode

Exit fullscreen mode

Verify that the template, pool, Sandbox, and Pod exist:

kubectl get sandboxtemplates,sandboxwarmpools,sandboxes,pods 
-n
 default

Enter fullscreen mode

Exit fullscreen mode

Wait until the warm-pool sandbox Pod isRunning.

### 3. Create a dedicated ServiceAccount and RBAC for the SDK client

Do not run the SDK with the namespace'sdefaultServiceAccount in a real deployment. Give the client its own ServiceAccount with the permissions it needs to create/delete claims and resolve the underlying Sandbox.

kubectl apply 
-f
 - 
<<
'
EOF
'
apiVersion: v1
kind: ServiceAccount
metadata:
 name: sandbox-client
 namespace: default
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
 name: sandbox-client
 namespace: default
rules:
- apiGroups:
 - agents.x-k8s.io
 resources:
 - sandboxes
 verbs:
 - get
 - list
 - watch
- apiGroups:
 - extensions.agents.x-k8s.io
 resources:
 - sandboxclaims
 verbs:
 - get
 - list
 - watch
 - create
 - delete
- apiGroups:
 - extensions.agents.x-k8s.io
 resources:
 - sandboxwarmpools
 - sandboxtemplates
 verbs:
 - get
 - list
 - watch
- apiGroups:
 - ""
 resources:
 - pods
 - services
 verbs:
 - get
 - list
 - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
 name: sandbox-client
 namespace: default
subjects:
- kind: ServiceAccount
 name: sandbox-client
 namespace: default
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: Role
 name: sandbox-client

EOF

Enter fullscreen mode

Exit fullscreen mode

Verify the critical permissions using the fully qualified resource name syntax supported bykubectl auth can-i:

kubectl auth can-i get sandboxes.agents.x-k8s.io 
\

 
--as
=
system:serviceaccount:default:sandbox-client 
\

 
-n
 default

kubectl auth can-i create sandboxclaims.extensions.agents.x-k8s.io 
\

 
--as
=
system:serviceaccount:default:sandbox-client 
\

 
-n
 default

kubectl auth can-i delete sandboxclaims.extensions.agents.x-k8s.io 
\

 
--as
=
system:serviceaccount:default:sandbox-client 
\

 
-n
 default

Enter fullscreen mode

Exit fullscreen mode

All three should returnyes.

### 4. Start a Python client Pod

The SDK can run locally usingkubectl port-forward, but that mode requireskubectlin the environment running the Python process. For this reproducible example, run the clientinside the clusterand useSandboxInClusterConnectionConfig, which connects directly to the sandbox runtime and does not spawnkubectl.

kubectl run python-pod 
\

 
--image
=
python:3.12-slim 
\

 
--restart
=
Never 
\

 
--overrides
=
'{"spec":{"serviceAccountName":"sandbox-client"}}'
 
\

 
--command
 
--
 
sleep 
infinity

Enter fullscreen mode

Exit fullscreen mode

Wait for it:

kubectl 
wait
 
--for
=
condition
=
Ready pod/python-pod 
-n
 default 
--timeout
=
120s

Enter fullscreen mode

Exit fullscreen mode

Install the Python SDK in that Pod, pinned to the controller release used above:

kubectl 
exec
 
-n
 default python-pod 
--
 
\

 pip 
install 
k8s-agent-sandbox
==
0.5.3

Enter fullscreen mode

Exit fullscreen mode

### 5. Create a sandbox and execute Python inside it

Run the client directly through stdin; no Python file is required:

kubectl 
exec
 
-i
 
-n
 default python-pod 
--
 python - 
<<
'
PY
'
from k8s_agent_sandbox import SandboxClient
from k8s_agent_sandbox.models import SandboxInClusterConnectionConfig

client = SandboxClient(
 connection_config=SandboxInClusterConnectionConfig()
)

sandbox = client.create_sandbox(
 warmpool="python-sandbox-pool",
 namespace="default",
)

try:
 result = sandbox.commands.run(
 'python3 -c 
\'
print("hello from my sandbox")
\'
'
 )
 print(result.stdout)
finally:
 sandbox.terminate()

PY

Enter fullscreen mode

Exit fullscreen mode

Expected output:

hello from my sandbox

Enter fullscreen mode

Exit fullscreen mode

At this point the complete path is working:

python-pod
 |
 | SandboxInClusterConnectionConfig
 v
SandboxClaim -> SandboxWarmPool -> Sandbox -> runtime Pod:8888
 |
 +-> POST /execute

Enter fullscreen mode

Exit fullscreen mode

### 6. Troubleshooting the three failures you are most likely to hit

If you get:

SandboxWarmPoolNotFoundError: SandboxWarmPool "python-sandbox-pool" not found

Enter fullscreen mode

Exit fullscreen mode

check that the warm pool exists in the same namespace:

kubectl get sandboxwarmpools 
-n
 default

Enter fullscreen mode

Exit fullscreen mode

If you get a403 Forbiddenmentioningsandboxclaimsorsandboxes, check the ServiceAccount RBAC:

kubectl auth can-i get sandboxes.agents.x-k8s.io 
\

 
--as
=
system:serviceaccount:default:sandbox-client 
\

 
-n
 default

Enter fullscreen mode

Exit fullscreen mode

If you get:

HTTPConnection(... port=8888): Failed to establish a new connection: Connection refused

Enter fullscreen mode

Exit fullscreen mode

check the image used by the sandbox Pod:

kubectl get pods 
-n
 default 
\

 
-o
 custom-columns
=
NAME:.metadata.name,IMAGE:.spec.containers[
*
]
.image,IP:.status.podIP

Enter fullscreen mode

Exit fullscreen mode

The sandbox must run a runtime server that implements/executeon port8888; a normal Python image that only sleeps will not work withsandbox.commands.run().

### 7. Clean up

kubectl delete pod python-pod 
-n
 default 
--ignore-not-found

kubectl delete sandboxwarmpool python-sandbox-pool 
-n
 default 
--ignore-not-found

kubectl delete sandboxtemplate python-sandbox-template 
-n
 default 
--ignore-not-found

kubectl delete rolebinding sandbox-client 
-n
 default 
--ignore-not-found

kubectl delete role sandbox-client 
-n
 default 
--ignore-not-found

kubectl delete serviceaccount sandbox-client 
-n
 default 
--ignore-not-found

Enter fullscreen mode

Exit fullscreen mode

### On GKE instead

For the managed GKE feature, Agent Sandbox requires GKE1.35.2-gke.1269000or later. On an existing Standard cluster, Google also requires a gVisor-enabled node pool before enabling Agent Sandbox. The current command uses the beta cluster surface and includes the cluster location:

gcloud beta container clusters update 
"
${
CLUSTER_NAME
}
"
 
\

 
--location
=
"
${
LOCATION
}
"
 
\

 
--enable-agent-sandbox

Enter fullscreen mode

Exit fullscreen mode

GKE additionally enforces sandbox workload requirements such asruntimeClassName: gvisor, disabling automatic ServiceAccount-token mounting, running as non-root, dropping Linux capabilities, setting CPU/memory limits, and scheduling onto the gVisor sandbox node pool. Use the managed GKE deployment manifest from the official GKE guide rather than the minimal self-managed template above.

## The Bottom Line

GKE Agent Sandbox -- and the open-sourcekubernetes-sigs/agent-sandboxproject it is built on -- is what happens when someone finally builds the right abstraction for agent runtimes. It is Kubernetes-native, which means it fits into existing infrastructure without fighting it. It is fast enough for interactive use. It is secure by default. And it has SDKs that let agents manage their own environments programmatically.

The era of "just run it in Docker and pray" is ending. The era of "give the agent its own Linux box, properly isolated, properly managed, properly fast" is here.

And honestly? It is about damn time.

## References

All the sourcing for this post:

* GKE Agent Sandbox documentation-- the primary source on the managed GKE add-on
* kubernetes-sigs/agent-sandbox(~3k stars) -- the open-source CNCF SIG project under SIG Apps
* Agent Sandbox documentation site-- full docs, getting started guides, Python/Go SDK references
* Agent Sandbox Python SDK-- programmatic sandbox management from Python
* Agent Sandbox Go SDK-- same, but for Go

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse