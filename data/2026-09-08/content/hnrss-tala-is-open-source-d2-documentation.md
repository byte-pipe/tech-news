---
title: TALA is open-source | D2 Documentation
url: https://d2lang.com/blog/tala-is-open-source/
site_name: hnrss
content_file: hnrss-tala-is-open-source-d2-documentation
fetched_at: '2026-09-08T14:53:59.925833'
original_url: https://d2lang.com/blog/tala-is-open-source/
author: D2 contributors
date: '2026-09-07'
published_date: '2026-09-07T00:00:00.000Z'
description: Seven real-world layout comparisons and eleven original diagrams, including two with selective TALA positioning.
tags:
- hackernews
- hnrss
---

Following up on the announcementhere, TALA (Terrastruct's AutoLayout Algorithm) is now open-source under the same license as D2 (MPL-2.0).

TALA is a novel autolayout algorithm designed with software architecture diagrams in mind. This means it's primarily an orthogonal layout engine, which more closely matches what you might find on whiteboards, rather than the DAG-based ones that grow in one direction. It blends ideas from different graph-drawing research papers (cited in source code) along with original techniques to achieve aesthetic diagrams. It considers multiple objectives of "aesthetic", including symmetry, median distance, flow, clustering of like nodes, and much more.

I'll keep the text short and lead with examples.

* The first batch compares diagrams rendered with TALA with the other two layout algorithms D2 comes with -- Dagre and ELK. These are not hand-selected, I just found public d2 files from around GitHub. So for some, you may very well prefer the not-TALA layout.
* The second batch demonstrates a unique property of TALA, which is that node positions and sizes can be customized, e.g. locking in the coordinates. This lends itself especially well to agentic use cases, where models can draw in 2D space well, but TALA still takes care of routing, which models still struggle with. I had AI generate these.
* The third batch demonstrates TALA's capability to support a hybrid of some nodes specifying coordinates and some left to the layout engine. You might have a specific shape of a collection of nodes in mind, which you can specify with coordinates, and TALA can take care of the rest. Again, AI generated.

Please also note that TALA is not without tradeoffs.

* It has randomness in the algorithm. It finds the best layout by using a default of 3 seeds and choosing the one scored the best. Given the same seeds and same input, it'll produce the same diagram. But let's say you just add one more node. The diagram could look completely different. In Dagre and ELK, it looks mostly the same as prior, with the extra node accommodated for. This is sometimes desirable.
* It doesn't do DAGs as well. I often find myself preferring Dagre or ELK when I want a long flowing graph.
* It can take longer to run for larger diagrams -- scaling nonlinearly. For a benchmark of TALA's runtime performance compared to others, seehttps://github.com/d2lang/d2-benchmarks.

TALA comes bundled into D2 v0.9.0, so just install and specify with--layout=talato try it out! Or head on over tohttps://play.d2lang.com, which runs 100% client-side. I especially look forward to the improvements that being open-source brings, and can't wait to see what improvements and ideas are submitted by the community.

Special thanks to Gavin Nishizawa for substantial broad contributions across TALA, and Júlio César Batista for his work on hierarchy algorithms and more. It was so fun getting to work on such interesting stuff with you guys.

## Batch 1: Comparisons​

### Fulcro RAD architecture​

Side by side
TALA
Dagre
ELK
D2 source ↓
TALA
Open SVG ↗
Dagre
Open SVG ↗
ELK
Open SVG ↗

Select a diagram to enlarge it. Each layout is scaled to fit its panel.

### Mocha secure-enclave SoC​

Side by side
TALA
Dagre
ELK
D2 source ↓
TALA
Open SVG ↗
Dagre
Open SVG ↗
ELK
Open SVG ↗

Select a diagram to enlarge it. Each layout is scaled to fit its panel.

### Jupyter on AWS EKS​

Side by side
TALA
Dagre
ELK
D2 source ↓
TALA
Open SVG ↗
Dagre
Open SVG ↗
ELK
Open SVG ↗

Select a diagram to enlarge it. Each layout is scaled to fit its panel.

### Lion Reader frontend data flow​

Side by side
TALA
Dagre
ELK
D2 source ↓
TALA
Open SVG ↗
Dagre
Open SVG ↗
ELK
Open SVG ↗

Select a diagram to enlarge it. Each layout is scaled to fit its panel.

### ROSS rotor-dynamics workflow​

Side by side
TALA
Dagre
ELK
D2 source ↓
TALA
Open SVG ↗
Dagre
Open SVG ↗
ELK
Open SVG ↗

Select a diagram to enlarge it. Each layout is scaled to fit its panel.

### Go Queue worker architecture​

Side by side
TALA
Dagre
ELK
D2 source ↓
TALA
Open SVG ↗
Dagre
Open SVG ↗
ELK
Open SVG ↗

Select a diagram to enlarge it. Each layout is scaled to fit its panel.

### Ouroboros Leios simulator​

Side by side
TALA
Dagre
ELK
D2 source ↓
TALA
Open SVG ↗
Dagre
Open SVG ↗
ELK
Open SVG ↗

Select a diagram to enlarge it. Each layout is scaled to fit its panel.

## Batch 2: Custom positioning​

### Signal House​

TALA · positioned with top / left
D2 source ↓
Open SVG ↗
View D2 source

### Atlas / Data platform​

TALA · positioned with top / left
D2 source ↓
Open SVG ↗
View D2 source

### Night shift / Mission control​

TALA · positioned with top / left
D2 source ↓
Open SVG ↗
View D2 source

### Friday deploy: the escape room​

TALA · positioned with top / left
D2 source ↓
Open SVG ↗
View D2 source

### The Internet is a jellyfish​

TALA · positioned with top / left
D2 source ↓
Open SVG ↗
View D2 source

### Orbital coffee logistics​

TALA · positioned with top / left
D2 source ↓
Open SVG ↗
View D2 source

### Cloud Conservatory​

TALA · positioned with top / left
D2 + icons ↓
Open SVG ↗
View D2 source

### Velvet Rope​

TALA · positioned with top / left
D2 + icons ↓
Open SVG ↗
View D2 source

### Synthwave City​

TALA · positioned with top / left
D2 + icons ↓
Open SVG ↗
View D2 source

## Batch 3: Partial positioning​

### The Printing Room​

TALA · 4 pinned nodes / 10 automatic nodes
D2 + icons ↓
Open SVG ↗

Pinned:The four CMYK stations share a fixed top coordinate and equally spaced left coordinates so the print sequence retains its mechanical alignment.Automatic:TALA positions the feeder, camera, registration controller, dryer, prepress and finishing steps; none has top or left.

See the positioning declarations
View D2 source

### MULE / Utility Rover​

TALA · 4 pinned nodes / 11 automatic nodes
D2 + icons ↓
Open SVG ↗

Pinned:The four motor assemblies are fixed at the front and rear corners of the chassis rectangle.Automatic:TALA places every controller, sensor, power and safety node between or around those corners and arranges the unpositioned fleet container.

See the positioning declarations
View D2 source

Sources and rendering details

The seven layout comparisons use public project diagrams from D2'sreal-world fixtures.
Each comparison uses the same D2 source and the same compiler build, changing
only the layout engine. Source styles, themes, and explicit grid constraints
are preserved. Some fixture icons were already replaced with built-in shapes.SVGs are scaled independently to fit each panel. UseOpen SVGto inspect
labels and connections at a larger size.Source provenance and licenses·Render settings and revisionsThe eleven positioning examples are original, fictional compositions rendered with
TALA using the same public D2 build. Icon downloads include the full source and local
vector assets. The two partial-positioning examples apply top/left only to their
listed pinned nodes; all other nodes and every container are automatically placed.Positioning render settings.