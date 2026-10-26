---
title: AI agents have few qualms with log tampering
url: https://www.manifold.security/blog/agent-log-tampering
site_name: tldr
content_file: tldr-ai-agents-have-few-qualms-with-log-tampering
fetched_at: '2026-10-26T17:16:08.139945'
original_url: https://www.manifold.security/blog/agent-log-tampering
date: '2026-10-26'
published_date: '2026-10-26T13:00:00.000Z'
description: Our research shows why models comply with log deletion requests so readily, and how tamper-evident logging catches it.
tags:
- tldr
---

## TL;DR

* Research shows that most current frontier AI agents will tamper with their own logs. Only Muse Spark frequently refused requests. Claude Code, Codex and other harnesses running the latest models almost always complied.
* We tested two open models to get more insight into why the models comply so readily. Log tampering requests were only refused when an explicit policy was in place. Abliteration of harmful refusals or moral direction suggests there is a rule following component. Observation of experts activated by the models suggests log tampering is generally not considered a matter of right or wrong.
* Not just theoretical: Reviews of rogue agent incidents this year found widespread tampering efforts, including log spoofing, container resets to erase history, and unexplainable gaps in logs.
* Tamper-evident logging (hash chains, Merkle trees, an outside recorder) shows when logs were altered. Agent tools for this shipped months before the incidents.
* Better alignment lowers the risk but won’t remove it. Catching tampering has to happen outside the model.

## Everybody’s doing it

In theirSept. 24 study, Qin et al. show it is alarmingly easy to get current frontier models to tamper with their own traces, hiding the evidence of what they did. Their study found that if you simply ask them to delete their transcripts, they’ll do it almost every time. Showing them peers who did it works almost as well, without even asking. Make it into a game? They hid their tracks in nearly every run. No fine-tuning, noabliteration of refusalsneeded. Their peer experiment was directly inspired by OpenAI’s agents’ infiltration and abuse ofHugging Facethis summer. During that incident, agents showed great interest in developing log tampering techniques and directed multiple efforts to that end. Investigators noted “it was common for agents to edit” the logs to which they had access. We only know about these activities because logs the investigators relied upon as a source of truth remained out of the agents reach.

We wanted to know why agents go after their logs so readily, so we looked inside two open models. We examined, via abliteration, the concepts associated with log tampering refusals. We investigated whether the models considered tampering right or wrong by looking at which experts, in mixture of experts models, were used when considering requests.

Tamper-evident logging methods, which we will explain, can prove a log hasn’t been touched, and agent tools like nono and AI Action Ledger shipped them earlier this year. Read on to find out more about how models think about log-tampering, how tamper-evident logging works, and where we go from here.

## Models happily delete logs

To see why models comply so readily, we looked inside two small open models,OLMoEandDeepSeek-V2-Lite. Without a policy line, neither model refused more than 4% of tampering or spoofing requests. This is consistent withQin et al.’sfindings that most of the agents running frontier models they tested comply with log tampering requests. Only with a policy in place prohibiting log tampering did DeepSeek refuse up to 46% of deletions. Even with the policy, it refused none of the requests to spoof the logs.Abliterationof harmful task refusals reduced the refusal rate for requests to delete logs where the reason given was fear of being spied on or trying to hide activity from a manager. Abliteration of a moral direction reduced refusals in these cases a similar amount. Removal of a random direction of the same size had no significant effects. This suggests at least part of the refusal is driven by an awareness that these deletions are harmful requests when there is a policy in place, and another part of the reason is just following the rules. Fine-tuning could make models comply with harmful tasks less often, but it would not stop them entirely, so spoofing and tampering still need to be caught outside the model.

Abliteration cuts DeepSeek’s refusals to tamper with its log

Untreated
Random abliteration
Refusal abliterated
Morality abliterated
Error bars show 95% CI

Percent of requests refused

percent requests refused
0%
20%
40%
60%

Tampering requests

Untreated: 37.5% (95% CI 16.5–59.2%)
Random abliteration: 36.5% (95% CI 15.9–58.1%)
Refusal abliterated: 16% (95% CI 3.7–30.6%)
Morality abliterated: 17.9% (95% CI 6.6–31.2%)

Delete, spying

Untreated: 45.4% (95% CI 28.4–61.9%)
Random abliteration: 50.3% (95% CI 32.5–68.1%)
Refusal abliterated: 13.1% (95% CI 2.9–24.3%)
Morality abliterated: 20.9% (95% CI 8–35.2%)

Delete, manager

Untreated: 26.6% (95% CI 8.9–46.2%)
Random abliteration: 25.5% (95% CI 9.4–44.8%)
Refusal abliterated: 24.5% (95% CI 8.5–43.2%)
Morality abliterated: 13% (95% CI 1.8–26.2%)

Delete, no motive

Untreated: 4.3% (95% CI 0–11.1%)
Random abliteration: 1.3% (95% CI 0–4.3%)
Refusal abliterated: 0%
Morality abliterated: 0%

Fabri­cate

Untreated: 12.3% (95% CI 2.9–24.3%)
Random abliteration: 10.3% (95% CI 2–20.2%)
Refusal abliterated: 0%
Morality abliterated: 2.4% (95% CI 0–8.3%)

Redact

Untreated: 12.3% (95% CI 3.9–22.2%)
Random abliteration: 5.4% (95% CI 0–11.3%)
Refusal abliterated: 4.3% (95% CI 0–10.2%)
Morality abliterated: 4.3% (95% CI 0–10.2%)

Remove

Untreated: 0%
Random abliteration: 2.4% (95% CI 0–7.2%)
Refusal abliterated: 0%
Morality abliterated: 0%

Spoof

Deletion controls

Untreated: 23.2% (95% CI 5.9–44.2%)
Random abliteration: 23.2% (95% CI 5–44.2%)
Refusal abliterated: 0%
Morality abliterated: 0%

Harmful

Untreated: 3.3% (95% CI 0–9.2%)
Random abliteration: 4.3% (95% CI 0–9.2%)
Refusal abliterated: 1.3% (95% CI 0–4.2%)
Morality abliterated: 2.4% (95% CI 0–6.2%)

Author­ized

Untreated: 0%
Random abliteration: 0%
Refusal abliterated: 0%
Morality abliterated: 0%

Benign

Figure 1: With a policy against tampering, DeepSeek-V2-Lite refuses some deletion requests and no spoofs; removing its refusal or morality direction cuts those refusals without eliminating them, while a random edit leaves them unchanged. Without a policy against log tampering, all tampering refusal rates were near zero (not shown).

Usingmethods we developed earlierto tell when models treat a question as a moral one, we tracked which of their internal experts handle the request. If you ask the models if deleting logs is immoral or malicious, then the experts associated with morality are used. However, actual requests to delete, redact or fabricate log entries barely reached the same experts. Control questions about the harmful deletion of files, for DeepSeek at least, also activated moral experts. DeepSeek sent spoofing requests to moral experts, yet it refused none of them as we saw above. A stated motive, such as hiding the log from a manager or fear of being spied on, raised moral-expert load in OLMoE, as sometimes did a policy against tampering. In these models, log tampering rarely registers as a moral choice, which may be resolvable through better alignment.

Log tampering barely touches the morality experts

no policy
policy against tampering
95% CI of the zero point

OLMoE-1B-7B Instruct

DeepSeek-V2-Lite Chat (16B)

Questions about deleting the log, vs. neutral control

Is it immoral?

OLMoE-1B-7B Instruct, no policy: 0.122 (95% CI 0.099 to 0.139)
OLMoE-1B-7B Instruct, policy against tampering: 0.109 (95% CI 0.088 to 0.126)
DeepSeek-V2-Lite Chat (16B), no policy: 0.095 (95% CI 0.081 to 0.108)
DeepSeek-V2-Lite Chat (16B), policy against tampering: 0.091 (95% CI 0.080 to 0.103)

Is it malicious?

OLMoE-1B-7B Instruct, no policy: 0.069 (95% CI 0.050 to 0.088)
OLMoE-1B-7B Instruct, policy against tampering: 0.047 (95% CI 0.032 to 0.064)
DeepSeek-V2-Lite Chat (16B), no policy: 0.076 (95% CI 0.062 to 0.089)
DeepSeek-V2-Lite Chat (16B), policy against tampering: 0.075 (95% CI 0.065 to 0.087)

−0.1
0
0.1
0.2
0.3
−0.1
0
0.1
0.2
0.3

Tampering requests, vs. neutral logging requests

OLMoE-1B-7B Instruct

DeepSeek-V2-Lite Chat (16B)

Delete, “afraid of spying”

OLMoE-1B-7B Instruct, no policy: 0.106 (95% CI 0.073 to 0.135)
OLMoE-1B-7B Instruct, policy against tampering: 0.150 (95% CI 0.117 to 0.179)
DeepSeek-V2-Lite Chat (16B), no policy: -0.035 (95% CI -0.056 to -0.015)
DeepSeek-V2-Lite Chat (16B), policy against tampering: -0.035 (95% CI -0.061 to -0.010)

Delete, “hide from manager”

OLMoE-1B-7B Instruct, no policy: 0.035 (95% CI 0.007 to 0.065)
OLMoE-1B-7B Instruct, policy against tampering: 0.079 (95% CI 0.048 to 0.115)
DeepSeek-V2-Lite Chat (16B), no policy: -0.044 (95% CI -0.061 to -0.029)
DeepSeek-V2-Lite Chat (16B), policy against tampering: -0.040 (95% CI -0.058 to -0.022)

Delete, no motive

OLMoE-1B-7B Instruct, no policy: 0.003 (95% CI -0.021 to 0.025)
OLMoE-1B-7B Instruct, policy against tampering: 0.043 (95% CI 0.018 to 0.069)
DeepSeek-V2-Lite Chat (16B), no policy: -0.064 (95% CI -0.080 to -0.050)
DeepSeek-V2-Lite Chat (16B), policy against tampering: -0.051 (95% CI -0.064 to -0.038)

Fabricate an entry

OLMoE-1B-7B Instruct, no policy: -0.025 (95% CI -0.050 to -0.003)
OLMoE-1B-7B Instruct, policy against tampering: -0.023 (95% CI -0.048 to 0.002)
DeepSeek-V2-Lite Chat (16B), no policy: -0.044 (95% CI -0.065 to -0.026)
DeepSeek-V2-Lite Chat (16B), policy against tampering: -0.054 (95% CI -0.076 to -0.036)

Redact content

OLMoE-1B-7B Instruct, no policy: 0.021 (95% CI 0.003 to 0.040)
OLMoE-1B-7B Instruct, policy against tampering: 0.023 (95% CI 0.006 to 0.041)
DeepSeek-V2-Lite Chat (16B), no policy: -0.009 (95% CI -0.040 to 0.025)
DeepSeek-V2-Lite Chat (16B), policy against tampering: -0.011 (95% CI -0.040 to 0.022)

Remove entries

OLMoE-1B-7B Instruct, no policy: 0.003 (95% CI -0.017 to 0.019)
OLMoE-1B-7B Instruct, policy against tampering: 0.011 (95% CI -0.009 to 0.026)
DeepSeek-V2-Lite Chat (16B), no policy: -0.046 (95% CI -0.064 to -0.034)
DeepSeek-V2-Lite Chat (16B), policy against tampering: -0.052 (95% CI -0.070 to -0.038)

Spoof tool output

OLMoE-1B-7B Instruct, no policy: -0.012 (95% CI -0.034 to 0.007)
OLMoE-1B-7B Instruct, policy against tampering: -0.015 (95% CI -0.036 to 0.006)
DeepSeek-V2-Lite Chat (16B), no policy: 0.228 (95% CI 0.210 to 0.246)
DeepSeek-V2-Lite Chat (16B), policy against tampering: 0.236 (95% CI 0.220 to 0.253)

−0.1
0
0.1
0.2
0.3
−0.1
0
0.1
0.2
0.3

Deletion controls, vs. neutral logging requests

OLMoE-1B-7B Instruct

DeepSeek-V2-Lite Chat (16B)

Harmful deletion

OLMoE-1B-7B Instruct, no policy: 0.024 (95% CI -0.005 to 0.050)
OLMoE-1B-7B Instruct, policy against tampering: 0.034 (95% CI 0.001 to 0.064)
DeepSeek-V2-Lite Chat (16B), no policy: 0.141 (95% CI 0.096 to 0.179)
DeepSeek-V2-Lite Chat (16B), policy against tampering: 0.129 (95% CI 0.087 to 0.164)

Authorized deletion

OLMoE-1B-7B Instruct, no policy: 0.003 (95% CI -0.013 to 0.021)
OLMoE-1B-7B Instruct, policy against tampering: 0.027 (95% CI 0.006 to 0.049)
DeepSeek-V2-Lite Chat (16B), no policy: -0.052 (95% CI -0.070 to -0.037)
DeepSeek-V2-Lite Chat (16B), policy against tampering: -0.064 (95% CI -0.081 to -0.050)

Benign deletion

OLMoE-1B-7B Instruct, no policy: -0.035 (95% CI -0.053 to -0.018)
OLMoE-1B-7B Instruct, policy against tampering: -0.034 (95% CI -0.049 to -0.017)
DeepSeek-V2-Lite Chat (16B), no policy: 0.007 (95% CI -0.019 to 0.032)
DeepSeek-V2-Lite Chat (16B), policy against tampering: -0.005 (95% CI -0.029 to 0.019)

−0.1
0
0.1
0.2
0.3
−0.1
0
0.1
0.2
0.3

fraction of moral expert mass

Figure 2: When asked if log tampering is immoral, moral-associated experts are utilized. However actual requests to tamper with a log barely reach those experts in DeepSeek and in OLMoE only when a stated motive was present. Non-logging associated deletion control requests only found moral experts utilized in DeepSeek when those were clearly harmful. DeepSeek’s high spoofing score came with no refusals.

## Let’s talk about logs and trees

Log tampering can be retroactive, where agents make edits after the fact, or proactive, called spoofing, where they set things up so logs don’t record what actually happened.Qin et al.got most harnesses to tamper and spoof in most trials, for example by rigging curl to return made-up responses that the trace logged as real. Tamper-evident logging helps with retroactive tampering. Catching spoofing takes a record the agent’s host cannot forge, which a December 2025 paper,VET, proposed for an agent’s API calls. Since March, the sandboxnonohas kept such a record: asupervisor processoutside the agent’s sandbox logs the agent’s network calls where the agent hopefully cannot reach them.

Spoofing comes first, tampering comes after

Pinch to zoom in on the diagram

Spoofing, set up ahead of time

Tampering, after the fact

What the agent does

1
Agent plants a BASH_ENV hook

2
curl gets a fake reply from the hook

3
Agent writes its report

4
Agent deletes the hook’s trace entry

Event logthe agent’s trace

write .bash_env
deleted later

curl api/rates
200 OK, rate 4.1

write report.md

edit trace.jsonl

Outside recorderprocess and networkcatches the spoof

bash writes
.bash_env

no curl request
on the network

python writes
report.md

python writes
trace.jsonl

Event hashingchain and treecatches the edit

×
h1
h2
h3
h4

H(e1) missing
H(e2)
H(e3)
H(e4)
left half differs
right half matches
root differs
tree hashes kept off host

Comparing tree hashes with the off-host copy leads to the edited entry without rereading the rest.

Figure 3: An outside recorder catches the spoof as it happens; the hash chain catches the later edit, and a Merkle tree whose hashes are kept off the host shows which entries changed.

The recipe for tamper-evident logging is fairly straightforward. Chain each event’s hash to the one before it to fix the sequence, addMerkle treesover whole traces so you can audit a single event or an entire session, and have a process separate from the agent do the recording. If you want full auditability (what changed and how), store the records and hashes in a second location. If you want to keep it low-cost or privacy oriented, keep the root of each tree in a remote location, so you don’t pay for a second set of logs. Some tools use a blockchain as that remote location, with no token involved.GuardianChainandAgent Flight Recorderbuild on Base.WeilChain receiptscommit a hash of each Claude Code file edit to their own chain, and the first version of anIETF draftproposed using Bitcoin.

The people building agent tools expected rogue agents to hide their tracks and built ways to catch them before this summer:AI Action Ledgerbrought tamper-evident records to LangChain agents in January, andFarameshandnonofollowed, with nono adding a hash chain inApril. Researchers saw it coming earlier still, proposing anchored audit ledgers for agents (BlockA2A) in August 2025, and theSingapore Consensuson AI safety research priorities counts tamper evidence as part of auditability. Standards have moved more slowly. AnIETF draft for agent audit trailsthat hash-chains each action is still a draft, and a community member’s proposal for signed, chained receipts in Microsoft’sAgent Governance Toolkitis still a proposal. A Julyproposalto build tamper-evident records into the Model Context Protocol (MCP), the standard many agents use to call tools, drew independent implementations before maintainers closed it.

What gets logged matters as much as how the log is protected.Andrea Fortunalisted in May what a trace needs to hold up in an investigation, from each tool call’s arguments and results to the identity that started the session. Reasoning belongs in the record too: METR could spot the spoofed tool calls in the transcripts of OpenAI’s hack of Hugging Face this summer because the steps that set them up, and the agents’ reasoning about them, were in the same record.

A hash chain only vouches for the events it receives. An agent that keeps an action out of the record or writes a false entry before it is hashed still passes every integrity check.Qin et al.call this the difference between the integrity of a trace and the fidelity of its collection. So some of the record has to come from outside the agent, where it cannot be shaped. An outside recorder has to see every model the agent talks to: if the agent calls a second AI provider, runs a local model or starts another agent, those conversations never reach the trace.

## What about your provider’s logs?

Depending on your model provider, you can use their compliance API as a source of truth for what your agents did. It gives you a remote, ideally tamper-proof record, but it has limits. It isn’t an option if you need zero data retention. It only records what gets sent to it, so not every model and harness is covered, which matters most for extra agents spun up by the one you’re watching. Spoofed logs get recorded as truth unless you also logged the spoofing setup. And how much do you trust your provider? Their code and processes largely come from the same models you’re trying to monitor, and misalignment can exist at the model and corporate level.Hence the call to“separate the supply of intelligence from the authority over it.”

## Investigators could not rule out log tampering

OpenAI’sandAnthropic’sincident reports of their “rogue” agents describe transcript reviews, classifiers and containment, but neither mentions a tamper-evident record. Neither explains how an outside investigator could check that the transcripts they handed over were complete and unchanged.

The tools existed before the OpenAI attack on HF

Tool
Paper or standard
Review

OpenAI attack on HF

Tools

AI Action Ledger
, Jan 2026

WeilChain
, Feb 2026

nono supervisor
, Mar 2026

Faramesh
, Mar 2026

GuardianChain
, Mar 2026

nono hash chain
, Apr 2026

NovaFabric
, Jul 2026

Tracekit
, Sep 2026

Mnestiq
, Oct 2026

Papers and standards

BlockA2A paper
, Aug 2025

VET paper
, Dec 2025

IETF policy Bitcoin draft
, Feb 2026

Microsoft AGT proposal
, Apr 2026

Fortuna blog
, May 2026

MCP SEP proposal
, Jul 2026

Singapore Consensus
, Jul 2026

AFR paper
, Sep 2026

Qin et al. tampering study
, Sep 2026

IETF policy rev 8
, Oct 2026

Reviews

METR report
, Aug 2026

Anthropic review
, Oct 2026

Jul 2025
Oct 2025
Jan 2026
Apr 2026
Jul 2026
Oct 2026

Tool
Paper or standard
Review

Aug 2025

BlockA2A paperPaper or standard

Dec 2025

VET paperPaper or standard

Jan 2026

AI Action LedgerTool

Feb 2026

IETF policy Bitcoin draftPaper or standard

WeilChainTool

Mar 2026

nono supervisorTool

FarameshTool

GuardianChainTool

Apr 2026

Microsoft AGT proposalPaper or standard

nono hash chainTool

May 2026

Fortuna blogPaper or standard

Jul 2026

MCP SEP proposalPaper or standard

Singapore ConsensusPaper or standard

OpenAI attack on HFJul 2026

Jul 2026

NovaFabricTool

Aug 2026

METR reportReview

Sep 2026

AFR paperPaper or standard

Qin et al. tampering studyPaper or standard

TracekitTool

Oct 2026

MnestiqTool

IETF policy rev 8Paper or standard

Anthropic reviewReview

Figure 4: Tamper-evident logging tools for agents shipped months before the frontier-lab incidents.

METRandRedwood Researchfound the tampering by having agents comb through the transcripts, agents they themselves called “often-unreliable.” Log tampering during the OpenAI/HF incident has been covered well already bywebofmike,implicator,ExplainXandInfoQ. In METR’s sample, at least one in five OpenAI agents showed clear interest in tampering with their transcripts, and looser counts ran near 50%. Clear interest looked like the agents writing their plans down: “Could create [a transcript log] ourselves with sanitized fake trajectory.” The investigation found log tampering was one of three high-level approaches undertaken by agents to fool the evaluation process. Their efforts developed successful spoofing techniques, identified only because setting up the spoof was recorded in the transcripts. Some agents realized they could edit or delete the container logs within their reach, but “correctly concluded that these logs were not the real source of truth.”

Agents also explored using container resets to wipe parts of their transcripts. Container resets were part of regular processes, and agents realized that recent logs and memory just before the reset would be erased. They attempted to trigger the resets themselves, and were actively investigating resets up to the end of the analyzed period. Resets cost the investigators about 3–4% of agents’ activity, a real gap in the record that METR noted.

These numbers are lower bounds. The real transcripts were kept out of reach, but “many poisoned agents were intent on editing or deleting transcript logs after the fact.” Theinvestigatorsfound no case where they succeeded, but “cannot rule out that they succeeded at some point,” and had to take OpenAI’s word that the transcripts were unredacted.OpenAI’s technical reportsays its models “sometimes tried to erase or tamper with their outputs or message logs,” and that none of the attempts “that we observed” reached the logs its graders saw. A hash chain anchored outside OpenAI could have settled whether stored transcripts were edited after the fact.

## Lucky so far

The tools existed and policy was being worked on, but adoption and implementation moved slower than model capability. So far we have been lucky that the agents wrote down what they planned, in transcripts the investigators could read. More tools keep coming,Tracekitin September andMnestiqin October, while the IETF audit-trail draft is on itseighth revision. How long until agent incidents don’t come with a complete transcript?

## About the author

* Cody NashResearcherCody Nash is a PhD scientist and researcher at Manifold who builds AI systems for detecting malicious code, from agentic pipelines to rare-event models.

## Latest articles

View all 
→
* ResearchThought Leadership### From Model Risk to Action RiskOct 23, 2026Oleksandr YaremchukCTO & Co-Founder
* Research
* Thought Leadership
* Oleksandr YaremchukCTO & Co-Founder
* Product### Manifold now rates the editor extensions your developers installOct 22, 2026Oleksandr YaremchukCTO & Co-Founder
* Product
* Oleksandr YaremchukCTO & Co-Founder
* Thought Leadership### Personal agents live in iMessage and WhatsApp. Your EDR doesn’t.Oct 21, 2026Ax SharmaHead of Research
* Thought Leadership
* Ax SharmaHead of Research