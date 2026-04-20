---
title: Interview with Øyvind Kolås, GIMP developer - GIMP
url: https://www.gimp.org/news/2026/02/22/%C3%B8yvind-kol%C3%A5s-interview-ww2017/
date: 2026-02-26
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-02T08:26:36.210233
---

# Interview with Øyvind Kolås, GIMP developer - GIMP

# Interview with Øyvind Kolås, GIMP developer

## Participants
- Jehan (interviewer)
- Øyvind Kolås (also known as “Pippin”)
- Michael Schumacher (question contributor)
- Other contributors mentioned: Michael Natterer, Michael Schumacher, Simon Budig, Debarshi Ray

## Nickname and personal background
- Øyvind prefers his given name when it can be pronounced; otherwise he uses the nickname **Pippin**.
- The nickname comes from *Lord of the Rings*: he first used “Sméagol” on IRC in the mid‑1990s, then switched to “Pippin” because the hobbit is curious and fits his personality.
- He has read the books two or three times and watched the movies, which he finds “okay” but long.
- Artistic background: visual arts (painting, drawing) since teenage years; later moved into computer graphics, inspired by the demoscene and early programming tutorials.
- Formal education in fine arts followed by computer‑science studies; has been creating graphics since age 14‑15.

## Role in GIMP and GEGL
- Maintainer of GEGL (Generic Graphics Library) and babl, the color engine used by GIMP.
- GEGL is a modular library that lets developers build chains of image‑processing operations as a data‑flow graph (e.g., color adjustment → sharpening).
- Øyvand’s first GIMP contribution was a patch adding adaptive‑subdivision supersampling to perspective transform tools, improving moiré and aliasing issues.
- He entered the GIMP project after meeting contributors at a GNOME conference in Copenhagen (2001).

## GEGL’s impact on GIMP
- GEGL provides the underlying engine for most of GIMP’s layer processing, replacing the older 2.8 pipeline.
- Non‑destructive editing in GIMP 3.0 is enabled by GEGL’s graph‑based workflow, especially in the layers dialog.
- Implementing user‑friendly interfaces for effects (drop shadows, blurs, color adjustments) is challenging; prototypes are easy, but stable, long‑term solutions require careful design.

## Use of GIMP and other tools
- Øyvind uses GIMP when it fits the task; otherwise he employs other software or creates new tools if needed.

## Vision for the future
- If GIMP exists in 20 years, GEGL will likely still be part of it, at least the graph concept and many operations.
- Anticipates that current CPU‑based and OpenCL processing code may be replaced by newer technologies, while the API and overall architecture remain similar across applications that use GEGL (e.g., video editors, GNOME Photos).

## GitLab repository question
- Øyvand is aware of the parallel history of GIMP and GEGL repositories but does not know the detailed reasons for their recent merge; he only knows anecdotal stories.
