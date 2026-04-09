---
title: 'LL3M: Large Language 3D Modelers'
url: https://threedle.github.io/ll3m/
site_name: hackernews_api
fetched_at: '2025-08-18T10:02:41.619548'
original_url: https://threedle.github.io/ll3m/
author: simonpure
date: '2025-08-17'
description: 'LL3M: Large Language 3D Modelers'
tags:
- hackernews
- trending
---

# LL3M: Large Language 3D Modelers

Sining Lu
*

Guan Chen
*

Nam Anh Dinh

Itai Lang

Ari Holtzman

Rana Hanocka

University of Chicago

LL3M uses a team of large language models to write Python code that creates and edits 3D assets in Blender.Given user text instructions, the agents are capable of creating expressive shapes from scratch, and realizing
 complex, precise geometric manipulations in code.

 Whereas previous uses of code-writing LLMs for 3D creation have focused on specific subtasks or constrained
 procedural programs and primitives, our method is able to create unconstrained assets with geometry, layout, and
 appearance.

 With high-level code as a 3D representation, our pipeline is natively a loop of iterative refinement and
 co-creation: agents perform automatic code and visual self-critique, and users can provide continuous high-level
 feedback. Further editing avenues are enabled by the clear code and the parameters transparent in the generated
 Blender nodes and structures.

## Pipeline overview

Our method includes three phases: initial creation, automatic refinement, and user-guided refinement.
 These are conceptual phases in the creation process; each phase involves different agent roles of its own.
 The first
 phase creates an initial shape, where implausible configurations, like a disconnected backrest, as well as
 simplistic geometry areautomaticallycorrected and improved upon by the second phase. Afterwards, our system can accept
 additional edit
 instructions from the user, allowing forinteractiveanditerative3D asset generation.

Generating and refining iterativelyis thus the native mode of operation for LL3M.
 More than just error correction, the pipeline realizes an iterative, coarse-to-fine creation process,
 involving both automatic and user-guided refinement.

## Gallery

LL3M is capable of diverse shape generation. The results showcase detailed parts (e.g.
 the windmill architectural features) in intricate arrangements (e.g. the piano keys, the drum kit), and even a
 rich appearance (the skateboard) and material properties (the glossy lamp base). A notable feature of our approach
 is that each mesh is generated through interpretable, editable Blender code.

## Consistent stylization

Starting from different initial meshes produced by LL3M and the same
 refinement promptchange the style to steampunkLL3M successfully interprets and applies the same
 style concept to each hat. Each stylized mesh produces distinct variations, including both geometric modifications
 and appearance changes.

## Material editing

Given an initial mesh produced by our system, our system is capable of editing the materials on a specific part of
 the mesh (the blade of the knife), by creating comprehensive procedural materials via shader nodes.

## Iterative creation

LL3M enables multiple successive edits of the same 3D asset. The
 modifications are faithful to the user's instructions, editing only the specified element while preserving the
 character's identity.

## Interpretable code

Our method generates Blender code that is easy to understand and follow. The code
 is well-documented with descriptive comments, clear variable names, and structured logic. This interpretable
 code makes it easy to potentially change variables (e.g. the key width) or even algorithmic logic (e.g. the
 keyboard pattern).

## Transparent parameters

By generating shapes through Blender code, LL3M allows intuitive user edits by virtue of the interpretable
 parameters transparent in the code and in the generated Blender nodes and structures.
 For example, when generating a material, our system creates a full set of shader nodes. Users can then
 easily adjust visual attributes, such as tuning the color or stripe pattern directly in Blender to achieve the
 desired output.

## Generality & reuse of code

Despite visual differences, shapes often share high-level code patterns (such as loops, modifiers, and node
 setups) that recur across categories. This shared structure allows the model to transfer knowledge and generate
 diverse, editable, and modular code from a wide range of prompts.

## Scenes & hierarchies

LL3M is capable of generating multiple objects and arranging them with appropriate spatial relationships
 within a single scene. Our system achieves this task using complex operations such as instancing and parenting
 relationships to build the scene hierarchy.The coding agent can also use parenting for more complex single objects, such as a lamp, when explicitly prompted
 to.
 Doing so generates shapes with a human-readable hierarchical structure with parent-child
 relationships between parts within the scene. This enables scene graph behavior in Blender, where transformations
 applied to a parent propagate to its children. Each part in the graph is also assigned a meaningful semantic name.

## BibTeX

@misc{lu2025ll3m,
 title={LL3M: Large Language 3D Modelers},
 author={Sining Lu and Guan Chen and Nam Anh Dinh and Itai Lang and Ari Holtzman and Rana Hanocka},
 year={2025},
 eprint={2508.08228},
 archivePrefix={arXiv},
 primaryClass={cs.GR},
 url={https://arxiv.org/abs/2508.08228},
}
