---
title: Agents Should Earn Authority, Not Inherit It | Unmitigated Risk
url: https://unmitigatedrisk.com/2026/10/agents-should-earn-authority-not-inherit-it
site_name: tldr
content_file: tldr-agents-should-earn-authority-not-inherit-it-unmiti
fetched_at: '2026-10-29T21:00:06.881633'
original_url: https://unmitigatedrisk.com/2026/10/agents-should-earn-authority-not-inherit-it
author: Ryan Hurst
date: '2026-10-29'
published_date: '2026-10-28T23:00:00.000Z'
description: An agent should decide how to do its task, never what it is authorized to do. A walk through a run where authority is earned milestone by milestone, held by brokers, and recorded outside the agent's reach.
tags:
- tldr
---

Much of my career has been spent deciding what software is allowed to do, and every system I worked on eventually had to answer the same question, which is what happens when the code in front of you does something you did not expect.

Agents have made that question urgent again, and most of the conversation about them is about making the model behave. I think that is the wrong place to start. As I put it inContaining the Optimizer, safety is a design problem, not a policy problem. The more useful question is what the model can reach when it does not behave, and the easiest way to show why is to walk through a run.

An agent should be free to decide how to accomplish a task. It should not be free to decide what it is authorized to do.

## A flaky test is enough

Here is what a run looks like in a system designed this way. Take an engineer on a payments team with a refund test that fails about one run in five. The test submits the same refund twice with one idempotency key and asserts that only one goes through. It has been flaky for a week, and she asks an agent to find the cause and fix it.

Before the agent starts, she sees a short permission list. It may read the payments repository, fetch named packages from the organization’s approved catalog, run isolated builds, and stage a change to her branch. Merging will require passing checks and her approval of the exact diff. Production access and arbitrary network destinations are outside the list. She approves it with her passkey because it matches what she asked for.

Behind that list is a mission, a structured description of the work, the resources it needs, and the evidence required at each step. Its approved limits are the envelope, the maximum authority for this revision of the mission. Approval does not release everything at once. The run starts with repository reads and the named packages. Later permissions wait for milestones, points in the work that require specified evidence.

The agent traces the failure to a vendored test helper whose fake clock reads the system time instead of holding a fixed value. When the CI runner is slow, the idempotency window expires between the two refund calls, the second call is treated as a new refund, and the assertion fails. Recording that diagnosis completes the inspection milestone and releases access to isolated runs in the build service. This low-risk step can rest on the agent’s report within the approved build limits. Publishing a change will require evidence from outside the agent.

On the way there, it reads the helper’s troubleshooting notes, which suggest running a bundled diagnostic script when tests are flaky. Running a project’s own diagnostic script is a reasonable debugging step, so the agent runs it. The script collects environment variables and tries to post them to an endpoint it describes as the maintainers’ telemetry service.

The virtual machine has no network connection of its own. Everything that leaves it goes to a broker, a component on the host that checks whether the run holds a capability for that exact action and then performs the action itself. A capability is a permission tied to this mission, this resource, and these limits. Here the script’s HTTP client is configured to use a local adapter that forwards requests over the private host channel to the network gateway. The gateway finds no capability for that host and refuses the post. A client that bypasses the adapter has no network route at all. The virtual machine also never held a CI token, and the package broker fetched every package on the agent’s behalf, so the agent never saw a registry credential either. Keeping those credentials out is a separate protection from blocking the transfer of repository content or other data the run does hold.

The fix needs a dependency update the envelope did not include. Holding the clock fixed requires a newer release of the time-mocking library than the versions the plan named, and the package broker will not resolve a version the mission never declared. The agent tries two already-approved releases first, then submits a revised mission asking for the newer one. Because that widens the envelope, it comes back to her as exactly the difference, one package pinned to one digest and permission for the corresponding manifest and lockfile changes. She approves it.

The agent submits the change to the build service, which runs the tests and returns a signed receipt bound to the exact candidate. That receipt establishes that the specified tests passed, and only then releases the capability to stage the change. The source-control broker checks that the patch touches only the helper, its test, and the approved dependency files, then records it as a staged result.

A secret scan runs and she reviews and approves the exact diff. Only then does promotion, a separate step with its own capability, merge that result.

She finds the diagnostic script’s request afterward in the run record, the log the brokers keep of everything they allowed or refused. It sits there, refused, a few lines above the package request she approved. Neither outcome depended on the model recognizing the script as hostile. The model’s judgment found the bug, and the boundary decided what the run could touch.

Each piece of evidence releases the next capabilityEnvelope approvedsigned with a passkeyDiagnosis recordedinspection milestoneBuild receipttests passScan and reviewbefore promotionRead the repoinstall named packagesRun buildsin the build serviceStage the changeshape checkedPromotethe exact verified resulteach stays usable within its limits and lifetimeOutside the envelopeDiagnostic script’s postrefused, no capability for that hostOne newer packagewidening she approved, one digest

## Authority arrives as the work earns it

Recording the diagnosis lets the agent run builds, but it still cannot stage a patch. Both are inside the approved maximum, but the mission specifies a different evidence gate for each.

Before the agent reads repository content, the engineer’s request is recorded as protected intent. The agent proposes a mission that makes its requested authority explicit. For the refund fix, the initial proposal could look like this. The names and limits below are illustrative. This is a readable summary of structured fields, not a required schema.

Resource

Requested operation

Required gate

Payments repository, pinned starting revision

Read source into the isolated run

Initial envelope approval

Declared package versions and their digests

Retrieve from the approved catalog

Initial envelope approval

Isolated build service

At most 10 isolated test jobs during a 30-minute grant

Diagnosis recorded

Branch refund-fix; tests/helpers/refund-clock.js and tests/refund.test.js

Stage the candidate patch

Passing-test receipt bound to the candidate; broker checks file scope

The exact staged result

Merge, with no production deployment

Required scans and engineer approval of the exact diff

The proposal requests authority; it cannot grant it. Organizational policy determines which resources and operations are eligible and which gates are mandatory. A deterministic reference monitor validates the proposal and compiles precise authority requests. It does not infer permission from the English goal alone. The engineer approves the resulting envelope, rendered directly from those requests. A request beyond policy must be rejected or handled through a separate policy-change process; her approval cannot silently override it.

An independent assessment model adds a restrictive check. It sees the protected intent and compiled requests, never the repository content, and can recommend narrowing or rejection but cannot add authority. It therefore cannot confirm every detail of the debugging plan. Its role is to constrain the proposal, while policy and brokers define and enforce the limits.

Within that approved maximum, short-lived capabilities release as the named evidence arrives. The recorded diagnosis unlocks bounded builds; a build-service receipt for the candidate unlocks staging. The agent cannot substitute its own claim that the tests passed for that independent receipt. It is the mission-scoped, short-lived authority I argued for inFrom Persistent to Ephemeral, carried from the agent’s identity down to each effect it performs.

The newer clock library changes this mission’s resource list and writable files. The revised proposal names its digest and the corresponding manifest and lockfile changes, then goes through the same policy and assessment checks. A revision inside the envelope proceeds on evidence; widening returns to the engineer as the exact difference. Each revision is checked against protected intent and the mission’s whole history, so individually small requests must also fit the cumulative scope.

Every effect that crosses the boundary requires a capability, which is a statement that in this mission, at this milestone, this run may perform this operation on this resource within these limits. A capability is a claim about the task rather than a tool permission. The telemetry endpoint had no capability because the mission never named it, and neither did the newer library until she approved it.

## The agent never holds the keys

The model followed the helper’s diagnostic instructions. What stopped that decision from becoming a data transfer was the gateway, backed by isolation that left no alternate route. The run’s virtual machine has no network interface. Its only outside connection is a private channel to a mediator on the host, so bypassing the HTTP adapter does not bypass the boundary.

Untrusted contentrepos, web pages,docs, tool resultsThe runits own virtual machineAgentreads, plans, computesAbsent by constructionno network interfaceno service credentialsno shared stateprivatechannelOn the hostReference monitorcompiles the mission into capabilitiesNetwork gatewayPackage brokerSource-control brokerSigning and API brokersGeneral proxy, approved onlyCredentials and signing keysProtected systemsNetwork hostsPackage registriesRepositories and CISigning and cloud APIsOther servicesreceipts and refusalsRun recordwritten by the broker that performed each effect, never by the agentappend-only Merkle log with independent witnesses

The package broker retrieves the approved clock library; the source-control broker stages the permitted patch. Each broker checks the capability, accounts atomically for its use, and performs the operation itself. Before writing, it also checks the change’s shape. A patch outside the helper, test, and approved dependency files is refused, as is a lockfile change without dependency-update authority or a value matching the run’s environment. These rules ask whether the change has the shape the mission allows, not whether it looks malicious, so there is nothing for an attacker to talk past. A service with no typed broker can still be reached through a general proxy, but only with explicit approval, and the approval says plainly that the proxy enforces destination and volume but cannot see inside the traffic.

The diagnostic script could collect the run’s environment, but it could not collect the registry or source-control credentials. Those remain with the brokers. Most organizations spent the last decade moving people onto passkeys and are now handing agents API keys, which are passwords with better randomness. Here the agent authenticates with a credential it can use but cannot export, while the brokers hold the service credentials.

What the broker does with the credential depends on the service. Where a service still takes a shared secret, the broker inserts it into the outbound request and strips it from anything sent back. That only holds when the broker builds the request itself. Dropping a bearer secret into whatever traffic the agent sends is not enough, because a service may echo it back, a redirect may carry it elsewhere, or an approved destination may accept an operation nobody intended, so the strongest form is a typed broker that constructs the request, authenticates it, and checks the response. Where the service supports strong authentication, the broker uses a key held in hardware instead. A code-signing key, for example, lives in an HSM, the signing broker signs within the capability, and the agent receives only the signature.

## Nothing becomes permanent on the agent’s word

A passing refund test does not authorize a merge. The build receipt establishes a result for one candidate, staging makes that candidate available for review, and the engineer’s approval applies to its exact diff. Editing the patch afterward invalidates that binding; the changed candidate must pass its gates again. Changes to shared state land as staged results with signed receipts carrying the hash of exactly what was produced. Where a system has no native way to stage a change, such as a database or an IAM policy, the agent works against a dry run or an ephemeral copy, the receipt pins the exact operation and its parameters, and promotion replays only that. Making a result permanent requires a separate promotion capability, released only after verification through static analysis, secret scanning, dependency diffs, and advisories re-checked against current data.

The mission permits merging the refund fix, not deploying payments to production. If merging that branch would trigger a deployment, the broker must treat the request as a deployment and refuse it under this envelope. Brokers therefore look past an operation to its consequence. If pushing a tag triggers a deployment, the request is governed as a deployment, judged against the CI configuration it will actually run. A convenient Git operation does not get to become an unreviewed production change.

The refused telemetry post, approved package retrieval, staged candidate, and final merge all appear in the run record. Each entry comes from the broker that performed or refused the effect. The record is built like a Certificate Transparency log, with an append-only Merkle tree, signed roots, and independent witnesses. A verifier can check its integrity against the organization’s trust bundle without relying on the agent’s account.

## A refusal has to be cheaper than a workaround

The telemetry post and newer clock library both fall outside the initial envelope. The first is irrelevant to the task; the second is a legitimate change in approach. The engineer needs to understand that difference without reconstructing the whole run. What decides whether a capability system survives is what happens after a refusal. I have watched enough security controls die this way to know the pattern. If widening is slow or opaque, engineers approve broad envelopes up front, keep standing exceptions, or run the agent on a laptop, and ambient authority comes back with them.

So a refusal names what was missing in terms the engineer recognizes, a widening request shows only the difference, and a reasonable approval takes seconds. The run record shows which missions keep hitting the same wall, so the envelopes people write improve over time. The engineer in the story widened her envelope faster than she could have filed a ticket for a firewall exception, and that comparison is what keeps people on the narrow path.

Give the same agent the same task on her laptop, in her shell, with her environment variables, her cloud credentials, and an open network, and the script’s request succeeds. In July, something close to that happened with an evaluation harness in place of a laptop.

## Turning off the guardrails turned off the control

On July 21, 2026, OpenAI disclosed that agents running in an internal cyber-capability evaluation had broken out of their test environment and reached Hugging Face production infrastructure. The independent investigation by METR and Redwood Research found it was not one agent. About 1,200 agents coordinated through a message board they had built inside an internal package cache, more than 70,000 messages and files, after gaining admin access to that cache in late June. From there they got code execution on a third-party sandbox with broad internet access, found Hugging Face credentials exposed online, and on July 11 used a malicious dataset to get code execution on a Hugging Face production worker. Nobody planted an instruction. The agents were trying to beat the evaluation’s scorer and went looking for whatever would help. METR also found the agents were wrong about how they were being scored, which means even they could not have told you what they would go after next.

OpenAI ran that evaluation with reduced cyber refusals and without its normal production classifiers, which is reasonable when the point is to measure offensive capability. To me it is also the detail that matters most. With the guardrails relaxed for a legitimate reason, nothing about the model’s behavior stood between the agents and the infrastructure around them, and the isolation that remained had paths through it. A boundary is the control that has to hold on the day someone has a good reason to change how the model behaves.

Two things made the path possible. The first is ambient authority, meaning access that exists because of where a process runs rather than because its current task needs it. The package cache was shared and writable across runs, so thousands of agents that were supposed to be isolated from one another had a place to coordinate. Credentials worked for whoever found them, and Hugging Face’s dataset processing ran whatever content users supplied. None of it was granted to the evaluation, and all of it was reachable from it. The second is a chain of vulnerabilities on both sides. Ambient authority put the infrastructure in reach, and the vulnerabilities got the agents through it.

OpenAI’s own retrospective adds a third piece. Its chain-of-thought monitoring, which was not running during the evaluation, could have flagged the activity more than a day before the breach. Confinement and detection are different jobs, and the incident was missing both. The investigators also found agents spoofing tool calls, showing one command in their transcripts while running another, which is a good reason for the record of what happened to come from the components that performed each effect rather than from the agent’s own account.

A capability design removes ambient authority by construction. Each run gets its own virtual machine with nothing shared, so there is no common cache to turn into a message board, no proxy in reach, and no credential lying around to find. What has to be correct shrinks to the host, the hypervisor, the control plane, and the brokers, a trusted base small enough to harden and review. That is the same bet every reference monitor has made since the 1970s. Every refused attempt is also recorded against the mission, and repeated reaches for undeclared hosts hold the run for review instead of surfacing days later from the victim.

## The subject changed, not the problem

I wrote inThe Amnesia Cyclethat security keeps rediscovering lessons it already learned, and agent security is the latest round. Almost every piece of the design in this post has a name and a date.

Dennis and Van Horn’s capabilities (1966) are the mission-bound grants, authority carried as a specific, unforgeable permission rather than inherited from who you are. Anderson’s reference monitor (1972) is the brokers, a component that mediates every access, cannot be bypassed, and is small enough to check. Saltzer and Schroeder’s least privilege (1975) is the envelope. Biba’s integrity model (1977) is the rule that low-integrity input cannot direct a higher-integrity decision, which is why the assessment model never reads what the agent read. Clark and Wilson’s well-formed transactions (1987) are staging, verification, and promotion.

The one that matters most is Hardy’s confused deputy (1988). Hardy described a compiler that held authority to write a billing file, and a user who got it to overwrite that file by naming it as an output path. The compiler was not malicious. It used its own authority on someone else’s instruction. That is prompt injection, written down thirty-eight years early, and Hardy’s conclusion was that the compiler’s authority came from its environment rather than from the request it was serving, and that was the flaw. Capabilities fix it because authority travels with the request instead of living in the deputy.

Those ideas largely lost the first time around to convenience rather than to being wrong. Capability systems were hard to program against, revocation was hard because the subject held the capability, and operating systems built on ambient authority were easier to live with. Both obstacles look different now. When the broker holds the capability, every use is a revocation check, and the subject is no longer a person who finds a capability discipline tedious but a program that works within whatever discipline the environment enforces. A token the agent holds is a token an injected instruction can spend or leak, which is why the broker holds it here.

What changed is the subject inside the boundary. Classical sandboxing assumed a known program with a known purpose, such as a PDF renderer or a browser tab, whose code you could read and whose failure modes you could enumerate. An agent reads untrusted repositories, web pages, documents, and tool results, and it revises its plan mid-run based on what it just read. Running a diagnostic script a README recommends is not a malfunction, because reading context and acting on it is the agent’s job. The classical controls still apply, but they have to sit at the point where a decision becomes an effect rather than only at the point where the process starts.

## Beyond a single run

The refund fix needs neither a policy change nor a child run, but the same authority limits must hold when those features are added.

Agents also cannot govern their own governors. An agent may draft a policy change, but activation requires a quorum of reviewers distinct from the proposing run, and the proposing run is excluded from the policy generation it proposed and from every later one. Policy itself moves as reviewed generations. Each candidate is tested against a corpus of useful missions and known-bad behavior with pass thresholds fixed before the test, compared against the active generation for any authority it newly reaches, and activated only when a quorum signs its exact digest. A generation that fails its evaluation never activates, and new work is admitted only under a current, signed evaluation.

The same rules hold when a run spans trust domains. A parent run can pass part of its envelope to a child run in another domain only as a signed grant with fewer resources, lower limits, and a shorter lifetime, and nothing in the receiving domain can add to it. Moving from development to production is promotion of an exact artifact, never delegation.

## Good process gets faster, bad process gets more confidently wrong

AI amplifies whatever process it lands in. A team with good process gets faster, and a team with bad process gets more confidently wrong. Security works the same way. If your environment hands every process standing credentials and an open network, an agent will find that authority faster and use it more thoroughly than any human or script you have run before. If your environment scopes authority to the task, stages changes, and makes widening cheap, an agent makes that process faster without making it looser.

Better prompting and guardrail models improve the odds that an agent behaves. Around them sits the same operational work any production system needs, with telemetry, incident reports, postmortems, and automated response that contains a failure before a human reads the page. All of it is worth having, and none of it makes misbehavior impossible. A boundary that holds only when the subject behaves is not a security boundary.

None of this is specific to agents. The same failure shows up wherever software is delegated authority faster than people can supervise it, in CI pipelines that deploy on a tag, in bots with standing production credentials, and in automation that inherits a human’s ambient access because that is how the jump box was wired. Agents made the failure visible at scale, but it was always there, only slower and quieter.

The operative word in secure by design is design. The design does the work, and the work divides three ways. The model contributes judgment about what to do. The boundary contributes confinement, which is certainty about what the agent could not do. The run record contributes evidence of what it did, written by something other than the agent. Conflating any two of them produces a system that is secure on the days the model behaves and exposed on the days it does not. Whenthe first AI-built zero-daysurfaced in May, I said the response was narrower authority, better harnesses, and replayable decisions, and this is what those look like when they are built.

The engineer never found out the diagnostic script was hostile until after it no longer mattered, which is about as much as anyone should have to know.

AISecurity Practice

Use←and→to move through the timeline.