---
title: Canon
url: https://tau.dev/2026/08/07/canon
date: 2026-08-12
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-19T04:07:12.974299
---

# Canon

# Canon

## Overview
- Created a web‑based game for my eight‑year‑old daughter so she can **make** her own games instead of just playing them.  
- Canon is a modern reinterpretation of classic MUDs (text‑based multi‑user dungeons) where every room, object, and interaction is player‑created and can be inspected, copied, and modified.  
- The experience is designed to be enjoyable for kids and nostalgic for adults who remember early internet text adventures.

## Inspiration from HyperCard
- HyperCard (1985) introduced the “card” metaphor: stacks of cards with buttons, text, images, and simple HyperTalk scripts.  
- As a child I built a Street‑Fighter‑style game by linking thousands of cards, discovering how powerful a fully editable environment could be.  
- HyperCard’s magic was its accessibility; its shortcomings were limited UI metaphors and an over‑natural‑language scripting language.  
- Canon aims to capture the same creative freedom while avoiding HyperCard’s constraints.

## Design Goals
- **Instant gratification:** Anything placed on screen becomes part of the game immediately.  
- **View source:** All content is built with the game’s own tools and is freely editable, copyable, and deconstructable.  
- **GUI for basics:** Simple actions can be wired through a graphical interface without writing code.  
- **Smooth learning curve:** Users can start with the GUI and gradually transition to raw scripting.  
- **Limited yet expressive language:** The custom scripting language **Cant** provides enough power for varied mechanics while remaining comprehensible for beginners.  

## Core Concepts
- The world consists of three primitive entities: **Players**, **Rooms**, and **Items**.  
- Players and Rooms are defined by text descriptions (and optional images) entered via a prompt.  
- Items are also described with text and images but include behavior and state through Cant scripts.  

### Example Cant item
```cant
item "Hooded Lantern" {
  describe "An iron lantern with a hinged hood."
  on "light" {
    narrate "{player}’s {item} swings open and warm light spills out."
  }
}
```
- This script creates a lantern that can be lit, producing narrative output for the player.

## Reception & Audience
- My daughter loves the ability to create and experiment within Canon.  
- The platform appeals to:
  - Adults who enjoy role‑playing or text‑adventure games.  
  - Anyone nostalgic for the telnet‑era MUDs and early web experiences.  
  - Parents and educators looking for an approachable introduction to programming concepts.