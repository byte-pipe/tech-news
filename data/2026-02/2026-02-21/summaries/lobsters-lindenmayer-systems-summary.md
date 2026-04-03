---
title: Lindenmayer Systems
url: https://justinpombrio.net/2026/02/16/l-systems.html
date: 2026-02-21
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-21T06:02:20.835046
---

# Lindenmayer Systems

# Lindenmayer Systems

This article introduces Lindeenmayer Systems (L-Systems) as a method for generating complex images, exemplified by the classic dragon curve. L-Systems utilize a starting string and a set of production rules to iteratively replace letters with sequences of instructions. These instructions are then followed by a "turtle" to draw the image.

## Turtles

The concept begins with the "turtle," a program that draws by moving forward and turning. The article uses a simple example of "f" (forward) and "+", "-" (right and left turns) to illustrate basic drawing.

## Angles

To create more intricate shapes, L-Systems can incorporate angles for turns, allowing for more complex paths. The hexagon is given as an example, using an angle of 1/6.

## Aristid Lindeenmayer

The core of the technique lies in the work of Aristid Lindeenmayer in 1968. L-Systems involve a start string and production rules that define how letters in the string are replaced with longer sequences of instructions. This process is repeated for a specified number of iterations.

## The Dragon Curve

The dragon curve is presented as a prime example of what can be generated with L-Systems. The article details the start string ("R") and the production rules (R -> Rf+L, L -> Rf-L), along with an angle of 1/4. It illustrates the progression through several iterations, showing how the complexity of the curve increases.

## Code

The author has implemented L-Systems as a Rust library. The provided code snippet shows the configuration for generating the dragon curve, including the start string, production rules, angle, and the option for implicit forward movement. The article notes that after approximately 22 iterations, the image stabilizes and further iterations only result in rotation.
