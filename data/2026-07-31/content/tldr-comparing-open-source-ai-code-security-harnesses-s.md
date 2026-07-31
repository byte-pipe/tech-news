---
title: Comparing Open-Source AI Code Security Harnesses | Semgrep
url: https://semgrep.dev/blog/2026/comparing-open-source-ai-code-security-harnesses/
site_name: tldr
content_file: tldr-comparing-open-source-ai-code-security-harnesses-s
fetched_at: '2026-07-31T11:44:48.082828'
original_url: https://semgrep.dev/blog/2026/comparing-open-source-ai-code-security-harnesses/
date: '2026-07-31'
description: A guide to open-source AI tools for finding code vulnerabilities, comparing exploit generation, skill-boosted auditing, and SAST+LLM hybrid approaches.
tags:
- tldr
---

There's a huge new wave of open-source AI security projects that point a large language model at a codebase to find vulnerabilities. We looked at some popular (or less popular, but from interesting companies) OSS tools and compared how they work, and when you'd reach for each.

We find three complementary categories in the new world of harnesses: LLM-led exploitgen, LLM-skill-boosting, and SAST+LLM hybrids.

### LLM-led exploitgen

from the author of AFL, one of the most popular fuzzers

For this category, the harness' goal is achieving to a crashing end-state as an oracle for vulnerabilities. I think of this as a new form of fuzzing. These have been the hardest harnesses to use in practice as model guardrails prevent LLMs from generating exploits, so you'll need to be part of the inner circle of trusted access/cyber verification. Additionally, they are usually very narrowly scoped, focusing on just a few different types of vulnerabilities with a reliable exploit condition. But there is a lot of low hanging fruit in that category!

* defending-code-harness(6K stars, Apache license)(Anthropic's harness is unmaintained, see alsoour Semgrep fork): finds C/C++ memory bugs by crashing them in a sandbox and builds a verified patch

### LLM-skill-boosting vulnerability research

This approach adds skillsinsideLLMs to get them to reason about code the way a human vulnerability researcher would to identify vulnerabilities.

* security-audit-skill(Cloudflare, 2K stars, MIT license): 6-phase multi-agent audit with adversarial validation
* skills(Trail of Bits, 6K stars, CC-BY-SA license): ~40 plugins designed to distill the expert knowledge of a security consultant
* vulnhunter(CapitalOne, 500 stars, Apache license): 3 (find, fix, verify) composable Claude Code skills that form an automated remediation loop
* mantis(Google,  400 stars, Apache license): ~15 security-focused skills. "Intended to be a starting point rather than a rigid set of instructions."

### SAST+LLM hybrids

Using deterministic program analysis tools (e.g.: Semgrep, CodeQL) as inputs to LLMs to guide the search space.

* raptor(Community, 3K stars, MIT license)Maximalist approach (some overlap with exploitgen). Built on top of ClaudeCode. Includes static analysis (Semgrep, CodeQL) + fuzzing + exploit feasibility + SCA + patching.
* Maximalist approach (some overlap with exploitgen). Built on top of ClaudeCode. Includes static analysis (Semgrep, CodeQL) + fuzzing + exploit feasibility + SCA + patching.
* deepsec(Vercel Labs, 5K stars, Apache license)web/app-stack focused. Workflow is a regex-prefilter → AI investigation → revalidation
* web/app-stack focused. Workflow is a regex-prefilter → AI investigation → revalidation
* ai-deep-sast(Cisco, 50 stars, Apache license)A fast SAST scanner (optionally, fully local model) that LLM-triages Semgrep findings across 30+ languages
* A fast SAST scanner (optionally, fully local model) that LLM-triages Semgrep findings across 30+ languages
* VVAH(Visa, 600 stars, Apache license)A broad, deeply-agentic 11-stage SAST pipeline (42 languages) that threat-models, verifies adversarially, then proposes and validates fixes (without executing code)
* A broad, deeply-agentic 11-stage SAST pipeline (42 languages) that threat-models, verifies adversarially, then proposes and validates fixes (without executing code)

### Ideal use cases

There's a lot of overlap between these harnesses, and it's not clear that all of them will continue to be maintained. Still, I did my best to come up with some categorization of when each of these might make the most sense.

If you care about running fully local and offline:

* ai-deep-sast— fast, cheap, broad coverage. The only one that can runfully local. Trades depth/proof for breadth/speed.

If you're a vulnerability hunter:

* raptor— one platform spanning scanning, dataflow, fuzzing, exploit feasibility, and SCA, if you have the operational appetite.
* google/mantis –if you are going to invest a lot of time and want a starting point to iterate and develop your own skills.

If you're a C/C++ maintainer who wants high-confidence exploitable findings with verified patches:

* defending-code-harness

If you're running an appsec program and trying to optimize for time-to-reviewed-fix:

* VVAH: broad-language SAST with some real triage rigor (threat modeling, adversarial verify, exploit-chain synthesis, propose-and-validate-the-fix). Accepts a frontier-model dependency. No runnable PoC.

If you're a Next.js/Vercel shop:

* deepsec: cheap regex-first triage with an AI second look and PR-diff mode; static-only, multi-backend.

If you are already using Claude Code / Codex / another coding harness for vulnerability hunting, why not install all the skills?

* cloudflare/security-audit-skill— you already live in Claude Code and want a rigorous, adversarially-validated audit methodology with near-zero setup and no new infra.
* trailofbits/skills— you want atoolboxof specialist reviewers (native code, crypto constant-time, smart contracts) to compose into your own workflow, inside Claude Code or Codex.
* capitalone/vulnhunter– explicitly optimized for Claude Code specifically

### What's similar and different across these harnesses?

* Separation of vulnerability discovery from validation: almost every LLM+SAST harness does this, with many explicitly using separate models to do so. But Exploitgen harnesses tend to use the same model to both discover and generate the exploit.
* Blurring line between traditional static and dynamic analysis:ai-deep-sast, VVAH, and deepsec reason completely statically. defending-code-harness and raptor can reason and also compile and execute binaries to validate. The latter is a new hybrid analysis that is much closer to how human vulnerability research looks.
* Adversarial validation:where a second independent agent tries to falsify each finding (Cloudflare's Phase 3, VVAH S6, ToB's fp-check, and defending-code-harness fresh-container grader). This seems widely adopted as a good way to increase accuracy, especially when having a different model attempt to disprove findings.
* Language support is less of a differentiator:traditional SAST tools took a lot of time to add language support but LLMs generally support almost all languages out of the box. Although exploit-gen class of harnesses is more narrow in language support, the bottleneck is more the language-specific toolchain to build a binary than the language itself.
* The definition of "findings" variesacross the harnesses. E.g.:

Tool

Primary method

"Finding" is…

ai-deep-sast

Semgrep + LLM triage

A triaged static match

VVAH

11-stage agentic LLM pipeline

A verified candidate from LLM pipeline

raptor

Semgrep+CodeQL+AFL+++LLM

A verified static finding or LLM pipeline candidate (± PoC)

defending-code-harness

LLM agents craft crashing inputs

A reproducible crash (ASAN)

deepsec

regex prefilter + AI + revalidate

A re-validated static match

* Patch generation is a cool capability but still less common:LLM-led exploit generation tools are (obviously) executing code, producing POCs, and (less obviously) patches. Most of the SAST+LLM hybrids are not:

Tool

Executes code?

PoC

Patch

ai-deep-sast

No

✗

✗ (advice)

VVAH

No

✗

✓ propose + LLM-validate

raptor

Yes

✓ (fuzz/feasibility)

✓

defending-code-harness

Yes

✓

✓ execution-verified

deepsec

No

✗

✗

### A market leader emerges?

Will there be a reference open source LLM harness for the new era? We think not today, and likely many companies will build their own "shop jigs" (thanks to tptacek on HN for the anology)for vulnerability finding. An OSS leader may emerge later, but the field is moving too fast right now. That's also why some of these harnesses are being released but marked as "no external contributions accepted" or unmaintained; the field is simply moving too fast.

We at Semgrep do have something we're planning to announce here at Black Hat in August. Stay tuned!

The above was human-written; see below for LLM-generated summaries of some of the repos involved!

### Reference 1: LLM summaries of the LLM+SAST tools

#### ai-deep-sast (Cisco)

LLM summary:Hybrid SAST in Python. Semgrep does fast rule-based detection; an LLM triages each finding behind an "evidence gate" meant to surface only true positives. Afast scancan run a fully local, security-tuned 8B model (Foundation-Sec-8B) so no code leaves the machine; adeep scanhands function-level context to a frontier model. Markdown/JSON/JUnit output, CI severity gates. Its optional fully-local mode is a genuine privacy differentiator. Brand new (v1.0.0).

#### VVAH — visa-vulnerability-agentic-harness (Visa)

LLM summary:An agentic SAST pipeline (built on learnings from Anthropic's Project Glasswing) running an 11-stage flow: threat-model (STRIDE) → decompose into taint chunks → deep-dive with optional majority voting → adversarially verify each finding (a second reviewer tries to falsify it, assigns CVSS) → dedup → synthesize exploit chains → SARIF → propose a minimal fix → score that fix with an agentic panel (security-architect + pen-tester + cross-repo-analyzer). Vendor-neutral backends; default Sonnet 4.6 for detection, Opus 4.8 for remediation/validation. 42 languages + 6 specialist lenses. No code execution. Optimizes "Mean Time to Adapt" (discovery → validated fix). Apache 2.0; closed to external contributions.

#### raptor (community, MIT)

LLM summary:The maximalist — ~107K lines of Python orchestrating Semgrep, CodeQL, AFL++ fuzzing, Z3-based exploit feasibility, SCA, and multi-model consensus, fronted by Claude Code with loadable "expert personas." A six-stage exploitability-validation pipeline filters false positives before investing in exploit dev. Broadest capability surface; heaviest to operate.

#### defending-code-harness (Semgrep)

LLM summary:Agentic, execution-verified, focused onC/C++ memory-safety bugs. Agents craft malicious inputs; a "find" only counts once it crashes under AddressSanitizer andreproduces 3/3 times in an isolated container. An independent grader re-confirms in a fresh container, an LLM judge dedups semantically, and a patch agent produces a fix verified on aT0–T3 ladder(compiles → PoC stops → tests pass → survives re-attack). gVisor sandbox + egress allowlist. Narrow scope, but findings are real crashes, not opinions.

#### deepsec (Vercel Labs)

LLM summary:TypeScript monorepo (~37K LOC). A 198-matcher regex prefilter (gated by auto-detected tech stack) finds candidate sites for free; an AI investigation loop then reasons over context and auth boundaries; a revalidation pass cuts false positives ~50%. Read-only agent tools (no execution), sandboxed with bubblewrap/Seatbelt locally or Vercel microVMs for distributed runs. Multi-backend: default Codex GPT-5.5, or Claude Opus 4.8, or Pi (GLM 5.2). Strong web/app-framework coverage (Next.js, Django, etc.) plus IaC. --diff mode for PR review; reports per-batch token cost. No SARIF yet; findings as JSON/Markdown, no patches.

### Reference 2: LLM-summaries of the LLM-skill-boosting group

#### security-audit-skill (Cloudflare)

LLM summary:A Claude Code skill: ~1,200 lines of Markdown methodology + a zero-dependency Node validator, installed via npx skills add. Runs a6-phaseaudit — recon → parallel hunt (8–12+ agents by attack class) → adversarial validation (separate agents try todisproveeach finding) → report → schema-validated findings.json → independent Phase-6 verification against source. Language-agnostic; domain playbooks for memory-safety/binary, AI/LLM, web-protocol/auth, and client-side. May optionally build and run code to confirm. Output is a human report + a SARIF-like custom JSON schema (payloads and repro steps, not standalone exploits). MIT. The intelligence is whatever model hosts it; the skill is the methodology.

#### trailofbits/skills (Trail of Bits)

LLM summary:A marketplace of~40 plugins (~15 security-focused)for Claude Code and Codex (CC-BY-SA). Standouts:c-reviewandrust-reviewuse a deterministic Python planner to orchestrate parallel Claude workers (haiku/sonnet/opus) with shared prompt caching, then sequential dedup/false-positive judges, emittingSARIF 2.1.0;static-analysiswraps Semgrep + CodeQL;constant-time-analysisandzeroize-auditdrop to assembly/LLVM-IR to catch crypto timing leaks and compiler-eliminated secret wiping;fp-checkandvariant-analysisare triage/expansion methodologies. Deep bench fornative code, cryptography, and smart contracts(6 blockchains). Strength is breadth and domain depth; it's a toolbox, not one pipeline.

### Reference 3: LLM-generated "Pipelines vs. skills, at a glance"

Standalone pipelines

Agent-native skills

Deploy as

Installed program / CI job

Prompt pack inside Claude Code / Codex

Brings its own model calls

Yes

No — uses the host agent's model

Runs unattended in CI

Yes

Partially (agent must drive)

Sandbox

Its own (gVisor, microVM, OS-level)

Inherits the host agent's

Cost model

Per-run infra + tokens

Just tokens on your existing agent

Examples

ai-deep-sast, VVAH, raptor, DCH, deepsec

Cloudflare security-audit, ToB skills

### Reference 4: LLM-generated Capability matrix

"Skill" rows inherit host-agent behavior where noted.

Tool

Kind

Vuln scope

Languages

Output

Isolation

Default model(s)

License

ai-deep-sast

Pipeline

OWASP/CWE Top 25, secrets, AI/ML

30+

MD/JSON/JUnit

n/a (static)

Foundation-Sec-8B (local) / frontier

Apache 2.0

VVAH

Pipeline

77+ CWEs, 6 lenses

42

MD + SARIF

tool sandbox (no Bash)

Sonnet 4.6 / Opus 4.8

Apache 2.0¹

raptor

Pipeline

22 classes: mem+web+auth+logic

many + binaries

JSON+SARIF+SBOM

Landlock+seccomp+ns

multi-model (Claude/GPT/…)

MIT

defending-code-harness

Pipeline

C/C++ memory safety

C/C++ (ext.)

SARIF+patches

gVisor + egress allowlist

Claude (Opus/Sonnet)

Apache 2.0

deepsec

Pipeline

web/app + IaC + agentic-AI

10+

JSON/MD

bubblewrap/Seatbelt/microVM

Codex GPT-5.5 (or Claude/Pi)

see repo²

security-audit-skill

Skill

broad + native/AI/web/client playbooks

agnostic

MD + JSON schema

host agent's

host model

MIT

trailofbits/skills

Skills

native, crypto, smart-contract, +more

many + 6 chains

SARIF/MD/JSON

host agent's

haiku/sonnet/opus

CC-BY-SA 4.0

¹ closed to external contributions. ² confirm license in-repo before relying on it. ³ certain skills (e.g. constant-time, zeroize) compile/inspect assembly; most are read-only.