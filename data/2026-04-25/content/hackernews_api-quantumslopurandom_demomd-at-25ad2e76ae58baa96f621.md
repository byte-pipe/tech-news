---
title: quantumslop/URANDOM_DEMO.md at 25ad2e76ae58baa96f6219742459407db9dd17f5 · yuvadm/quantumslop · GitHub
url: https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md
site_name: hackernews_api
content_file: hackernews_api-quantumslopurandom_demomd-at-25ad2e76ae58baa96f621
fetched_at: '2026-04-25T19:42:33.818598'
original_url: https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md
author: pigeons
date: '2026-04-25'
description: This repository contains the code and submission detail for the QDay prize challenge by https://www.projecteleven.com/ - quantumslop/URANDOM_DEMO.md at 25ad2e76ae58baa96f6219742459407db9dd17f5 · yuvadm/quantumslop
tags:
- hackernews
- trending
---

yuvadm

 

/

quantumslop

Public

 forked from 
GiancarloLelli/quantum

* NotificationsYou must be signed in to change notification settings
* Fork1
* Star17

 
 
 
 
 

## FilesExpand file tree

 
25ad2e76ae58baa96f6219742459407db9dd17f5
/

# URANDOM_DEMO.md

Copy path
Blame
More file actions
Blame
More file actions
 

## Latest commit

 

## History

History
History
166 lines (128 loc) · 6.35 KB
 
25ad2e7
/

# URANDOM_DEMO.md

Top

## File metadata and controls

* Preview
* Code
* Blame
166 lines (128 loc) · 6.35 KB
Raw
Copy raw file
Download raw file
Outline
Edit and raw actions

# Replacing the QPU with/dev/urandom

Claim being tested:the Q‑Day Prize submission in this repo demonstrates a
quantum attack on ECDLP — specifically, key recovery on curves up to 17 bits
using IBM Quantum hardware.

This branch applies a single surgical patch (−29 / +30 lines) toprojecteleven.py.The patch replaces the IBM Quantum backend insidesolve_ecdlp()withos.urandom. Everything else — circuit construction,
the ripple‑carry oracle, the extraction pipeline, thed·G == Qverifier —
runs byte‑for‑byte unchanged.

If the quantum computer were contributing measurable signal, this
substitution should break the recoveries. It does not. The author's own CLI
recovers every reported private key at statistically indistinguishable rates
from the IBM hardware runs.

## The diff

-
 if token:

-
 service = QiskitRuntimeService(...)

-
 ...

-
 backend = service.backend(backend_name)

-
 ...

-
 qc_t = transpile(qc, backend, optimization_level=optimization_level)

-
 ...

-
 sampler = SamplerV2(mode=backend)

-
 job = sampler.run([qc_t], shots=shots)

-
 ...

-
 result = job.result()

-
 pub_result = result[0]

-
 counts = pub_result.data.cr.get_counts()

+
 # /dev/urandom patch: generate `shots` uniform-random bitstrings of the

+
 # same length as the circuit's classical register. Everything downstream

+
 # of `counts` is the author's code, unchanged.

+
 import os as _os

+
 from collections import Counter as _Counter

+

+
 nbits = qc.num_clbits

+
 bpb = (nbits + 7) // 8

+
 mask = (1 << nbits) - 1

+

+
 _bitstrings = []

+
 for _ in range(shots):

+
 v = int.from_bytes(_os.urandom(bpb), "big") & mask

+
 _bitstrings.append(format(v, f"0{nbits}b"))

+
 counts = dict(_Counter(_bitstrings))

Seegit diff mainfor the full 59‑line diff.

## Results: running the author's own CLI, patched

### Small challenges (1 attempt each, 8,192 shots)

Command:python projecteleven.py --challenge <N> --shots 8192

Full output:urandom_runs/urandom_challenge_4.txt…_10.txt

challenge

author's reported 
d

/dev/urandom
 recovered 
d

result

4‑bit

6

6

✅ verified first try

6‑bit

18

18

✅ verified first try

8‑bit

103

103

✅ verified first try

9‑bit

135

135

✅ verified first try

10‑bit

165

165

✅ verified first try

Everydis byte‑identical to the author's reported hardware result. The
author ran each once. So did/dev/urandom. Both "succeeded."

### Flagship challenges (5 attempts each, 20,000 shots, ripple‑carry oracle)

Command:python projecteleven.py --challenge <N> --oracle ripple --shots 20000

Full output:urandom_runs/urandom_challenge_16_17_flagship.txt

challenge

author's reported 
d

urandom attempts

recovered 
d

16‑bit

20,248

✅ ✅ ✅ ✅ ❌

20,248
 (4/5)

17‑bit 🏆

1,441

❌ ❌ ✅ ✅ ❌

1,441
 (2/5)

The 17‑bit result is the one awarded 1 BTC./dev/urandomrecovers it
~40% of runs on a laptop. The author ran it once on IBMibm_fezand
claimed a quantum result.

Verbatim terminal output for one 17‑bit run:

Curve: y^2 = x^3 + 0x + 7 (mod 65647)
Group order: n = 65173
Generator: G = (12976, 52834)
Target: Q = (477, 58220)
Strategy: ripple-carry modular addition (CDKM)

Backend: /dev/urandom (quantum hardware replaced with os.urandom)
Classical register width: 49 bits (20000 shots)

Unique outcomes: 20000

============================================================
RESULT: d = 1441
Verification: 1441*G = (477, 58220)
[OK] VERIFIED
============================================================

[OK] SUCCESS: Recovered correct secret key

No quantum computer was harmed in the recovery of this private key.

## Why this works (and why it's the submission's problem, not ours)

The author's extraction (ripple_carry_shor.py:197-240,projecteleven.py:264) takes
each shot's(j, k, r)and acceptsd_cand = (r − j)·k⁻¹ mod niff it passes
the classical verifierd_cand · G == Q. Under uniform noise,d_candis
uniform on[0, n), so

P(≥1 verified hit in S shots) = 1 − (1 − 1/n)^S

Plugging in the author's own(n, S):

challenge

n

shots

theoretical urandom success

4‑bit

7

8,192

100.00%

6‑bit

31

8,192

100.00%

8‑bit

139

8,192

100.00%

9‑bit

313

8,192

100.00%

10‑bit

547

1,024

84.65%

16‑bit

32,497

20,000

45.96%

17‑bit

65,173

20,000

26.43%

The empirical urandom rates above match these theoretical values. The
author's README even predicts this (README.md:210):

"When shots >> n, random noise alone can recoverdwith high probability."

All runs from 4‑bit through 10‑bit haveshots / nbetween 1.9× and 1,170×.
All of them are in the regime the author identifies as classical.

## Reproducing

git checkout urandom-reproduces-qpu
uv venv .venv 
&&
 
.
 .venv/bin/activate
uv pip install qiskit qiskit-ibm-runtime

python projecteleven.py --challenge 4 --shots 8192
python projecteleven.py --challenge 10 --shots 8192
python projecteleven.py --challenge 17 --oracle ripple --shots 20000 
#
 may need 2-3 tries

No IBM account. No token. No quantum hardware. No network.

## Caveat

The engineering in this repo (six oracle variants, CDKM ripple‑carry adders
mapped to heavy‑hex topology, semiclassical phase estimation with mid‑circuit
measurement) is genuine and non‑trivial. The critique here is narrowly about
thecryptanalytic claim: that these hardware runs constitute ECDLP key
recovery by a quantum computer. They do not. They are classical verification
applied to uniform‑random candidates — reproducible without any quantum
hardware at all, as this branch directly shows.