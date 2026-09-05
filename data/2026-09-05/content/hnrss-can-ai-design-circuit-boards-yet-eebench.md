---
title: Can AI design circuit boards yet? — EEBench
url: https://eebench.org/blog/can-ai-design-circuit-boards-yet/
site_name: hnrss
content_file: hnrss-can-ai-design-circuit-boards-yet-eebench
fetched_at: '2026-09-05T10:35:45.635358'
original_url: https://eebench.org/blog/can-ai-design-circuit-boards-yet/
date: '2026-09-04'
description: OpenAI showed GPT-6 Astra routing a PCB. We built EEBench to find out whether AI-designed circuits actually work.
tags:
- hackernews
- hnrss
---

We got pretty excited yesterday when OpenAI put a demo ofGPT-6 Astra working on a circuit board in KiCadon the front page of its
 launch post. It is cool to see electronics show up in a major model release like this.

We are obviously still some distance from asking an AI to build an entire phone in one prompt. The demo does
 raise a question we have been thinking about for a while, though: how do we measure whether the electronics an
 AI produces are actually any good?

## The models know a surprising amount about electronics

Our experience has been that current models know much more about electronics than their output in
 conventional design tools tends to show. They have read textbooks, datasheets, application notes and a lot of
 code.

You can have an agent operate a graphical CAD tool, but it spends a lot of time clicking around and keeping
 track of what is on screen. A lot of its context consists of coordinates, menus and application state.

EEBench usesatopileinstead. The circuit
 lives in declarative code, so the agent can work directly on components, connections and electrical
 constraints. It can change the design, build it, run a simulation and inspect what failed without leaving the
 project.

This has worked much better for us than asking a model to draw lines in a GUI. It also means the benchmark
 can spend less time testing computer use and more time testing electronics.

A small part of the starter design for one public EEBench task, in ato v2

.
ELEC
:
 
@STD
::
Import
 
{

 
.
project
 
&=
 
"electronics"

 
.
org
 
&=
 
"atopile"

}

.
Submission
:
 
@type
 
{

 
.
vin
:
 
ELEC
::
ElectricPower

 
.
vhold
:
 
ELEC
::
ElectricPower

 
.
vhold.lv
 
~
 
.
vin.lv

 
.
c_bank
:
 
ELEC
::
Capacitor
 
{

 
.
capacitance
 
&=
 
22uF
 
+/-
 
20%

 
.
max_voltage
 
&=
 
10V
..
25V

 
.
temperature_coefficient
 
&=
 
"X5R"

 
.
package
 
&=
 
"0805"

 
}

 
.
vhold.hv
 
~>
 
.
c_bank
 
~>
 
.
vhold.lv

}

## The real world is messy

One of the public tasks is based on a residential energy meter. When its 5 V supply disappears, the circuit
 has to keep the processor alive for another 20 ms so it can save the accumulated reading. The protected rail
 must stay above the processor's 3.0 V brownout threshold during that window.

Most models intuitively jump to the right base conclusion: add a capacitor.

A real capacitor makes the task more interesting. A ceramic part may provide much less than its advertised
 capacitance once it has voltage across it. Parts have tolerances. Adding more capacitance costs more, takes up
 space and makes the rail slower to recharge when the power returns. A design that works with nominal values
 can fail with the parts that arrive.

EEBench cuts the input power in simulation and measures what happens. It checks the voltage throughout the
 outage, the effective capacitance at the operating point, the recovery after power returns and the limits on
 package, dielectric, voltage rating and cost.

Saved ngspice output from that submission. The protected rail falls below the 3 V requirement
 after 0.85 ms.

Failed power-loss hold-up simulation

The protected rail starts near 4.55 volts and falls below the required 3 volt
 threshold after 0.85 milliseconds, long before the required 20 milliseconds.

0
5
10
15
20 ms

0
1
2
3
4
5 V

3 V minimum

fails at 0.85 ms

The meter is one of the easier tasks. In a harder analog task, the agent may have to synthesize a
 multiple-feedback low-pass filter around an op-amp, solve the resistor and capacitor ratios for the required
 poles, and keep its gain, cutoff frequency and Q inside their limits after every component is pushed to a
 worst-case tolerance corner. The harness rebuilds the SPICE deck for those corners, runs the AC and transient
 captures, binds measurements to named probes, and records each result against its lower and upper
 specification limits.

But getting the equations right is only part of electronics engineering. EEBench uses real manufacturer
 parts, with specifications extracted from their datasheets and carried into the SPICE model. The agent has to
 find a combination that works across those tolerance corners while also choosing parts that exist, can be
 ordered and are reasonably priced for the product. That trade-off between electrical performance, cost and
 supply is much closer to designing real hardware than picking ideal values from a textbook.

This is the part we find most interesting, because it is what electrical engineering eventually boils down
 to, just like every other engineering discipline: trade-offs.

## How the grading works

EEBench checks are fully deterministic. It builds the submitted design, constructs the circuit
 graph and bill of materials, and runs a set of SPICE simulations and design checks. Each requirement produces
 a measurement with a limit.

For the energy-meter task, the harness measures the protected rail while the input drops out and returns.
 Other tasks measure gain, thresholds, ripple, transient response and behavior at component-tolerance corners.
 The technical score is combined with cost efficiency against a reference bill of materials. Cost only helps
 once the circuit works.

This is similar to giving a coding agent a compiler and tests, except the tests are measuring voltages and
 component behavior..

EEBench V1 covers analog and digital design through simulation. It does not yet tell us whether a model can
 lay out, manufacture and bring up a complete product. We want to add those parts later. The current benchmark
 concentrates on the requirements, design and verification loop because that is where we can already grade
 useful engineering work objectively. The fullmethodology and sample result
 explorerare public.

## What we are seeing on the leaderboard

The September 1 results are encouraging. Claude Opus 5 scored 61.6% across the 13 tasks in EEBench V1. Grok
 4.6 came second at 57.1%, just ahead of Claude Fable 5.1 at 56.4%. A few months ago we would not have expected
 models to do this well.

1
Claude Opus 5
61.6%

2
Grok 4.6
57.1%

3
Claude Fable 5.1
56.4%

4
Claude Fable 5
54.3%

5
Claude Opus 4.8 Max
51.4%

See the full leaderboard and run details

There was another result we were especially happy to see: xAI included EEBench in theGrok 4.6 model
 card. It appears in the section on “engineering acceleration,” alongside evaluations for 3D modeling and
 parametric CAD. Their published run put Grok 4.6 at 60.0% with xhigh reasoning effort. Seeing a frontier lab
 use EEBench to describe a new model's engineering ability makes us think this is becoming a category people
 care about.

Anthropic's models have consistently done well in this environment. Grok's rise is also interesting. In itsGrok 4.6 launch post, xAI says the
 model received high-quality engineering data and RL training in domain-specific environments including
 computer-aided design. Its EEBench result fits that story.

The OpenAI models we have tested so far sit further down the table. GPT-5.5 scored 42.3%, while GPT-5.6 Sol
 scored 39.4%. We do not have a GPT-6 Astra result yet. After seeing it work on a board in KiCad, we would
 really like to find out how it handles these circuit-design tasks.

## Training environment

Once we had a simulation harness that could grade a circuit, we also had the beginnings of an RL environment
 for electronics. The same checks can be used as reward signals during post-training.

A failed run contains useful information. We can see which voltage missed its limit, which operating corner
 failed, or whether the model solved the problem with an unnecessarily expensive design. That gives a training
 loop more to work with than a model saying that a schematic looks plausible.

EEBench is the small, public view of this work. We are also starting to work directly with frontier labs that
 want to make their models better at electronics. If you work on evals or post-training, you cantalk to us about the larger
 evaluation suites and simulation-backed training environments we provide.

## So, can it design a circuit board?

For a useful and growing set of circuit problems, we think the answer is already yes. The scores also make it
 clear that there is plenty left to do. OpenAI choosing a PCB for one of Astra's first demos and xAI publishing
 EEBench in a model card both feel like early signs of the same thing: AI labs are starting to take electronics
 seriously.

There may be another data point very soon.Elon Musk has saidthat Grok 4.7 is coming within weeks after additional training on a
 large collection of SpaceX data, with the aim of making it especially good at engineering. The model is not
 out and the schedule may move, but if it arrives as described, we will be keen to put it on EEBench.

It looks like we are in for an interesting few weeks. We will keep adding harder tasks as the models improve,
 and we are looking forward to seeing how Astra and the next generation perform.

You cantry the same approach in atopiletoday. Give the agent a board you have been meaning to build and see how far it gets.

So, can AI design circuit boards yet? Some of them, yes. We still would not ask it to design a pacemaker and
 blindly install the result. But we are on the way there.

EEBench is built and funded by the team behind atopile. We pay for the public
 benchmark runs and do not sell benchmark scores.