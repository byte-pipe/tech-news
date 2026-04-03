---
title: Beyond the Linear CV - DEV Community
url: https://dev.to/pascal_cescato_692b7a8a20/beyond-the-linear-cv-3fik
site_name: devto
fetched_at: '2026-01-09T11:07:47.347976'
original_url: https://dev.to/pascal_cescato_692b7a8a20/beyond-the-linear-cv-3fik
author: Pascal CESCATO
date: '2026-01-04'
description: This is a submission for the New Year, New You Portfolio Challenge Presented by Google AI ... Tagged with devchallenge, googleaichallenge, portfolio, gemini.
tags: '#devchallenge, #googleaichallenge, #portfolio, #gemini'
---

Google AI Challenge Submission

This is a submission for theNew Year, New You Portfolio Challenge Presented by Google AI

## About Me

My professional path isn't linear. It's atypical, composed of pivots, skill acquisitions across different contexts, and transitions that traditional CVs struggle to represent.

For years, the challenge wasn't"how to write a CV"but rather:how to make a non-linear journey readable?

The classic portfolio format—chronological, linear, static—works well for continuous trajectories. It breaks down for everything else. This project emerged from that personal need:what if we stopped trying to flatten our careers into a timeline, and instead represented them as they truly are—a network of interconnected skills, projects, and experiences?

As we enter 2026, "New Year, New You" doesn't have to mean reinventing yourself. Sometimes it meansrepresenting yourself more accurately.

## Portfolio

Live Demo:AI Knowledge Graph CV Builder

### What You'll See

The app loads withmy CV as a demoso you can explore immediately:

* Network Graph: 30+ interconnected nodes showing skills, projects, and expertise domains

* Flow Diagram: Visual journey from skills → projects → specialized areas

* Skills Matrix: Heatmap showing which projects use which technologies

Zero friction: No upload required to see it in action. Click "Upload Your Own CV" when you want to try yours.

### Visualizing Career Evolution

To test the system's ability to capture career trajectories, I ran my own CV from 2021 vs 2025:

2021 Graph(37 nodes, 74 edges):

* Corporate-focused: Skyrock, Logic-Immo, Photobox
* Legacy tech: Flash/Zend_Amf, Palm webOS, ORACLE
* Broader scope: Lead Dev, Project Manager, Full-Stack Engineer

2025 Graph(30 nodes, 74 edges, +23% density):

* Independent: Freelance + personal projects
* Modern stack: Astro, LLM/RAG, Docker, PostgreSQL
* Focused expertise: Migration Engineering + AI Automation

What changed?

* -8 technologies (legacy tech retired)
* +2 concepts (AI Automation, Migration Engineering)
* +23% density (deeper specialization vs wider breadth)

The graph doesn't just show skills—it tells the story of a career pivotfrom corporate generalist to independent specialist.

This is exactly what traditional CVs fail to capture.

## Career Evolution: 2021 → 2025

Metric

2021

2025

Change

Nodes

37

30

-19% ↓

Edges

~74

74

=

Density

2.0

2.2

+23% ↑

Stack

Legacy + Modern

Modern only

🔄

Focus

Corporate generalist

Independent specialist

🎯

Key transitions:

* Out: Flash, ORACLE, Palm webOS, 5 corporate clients
* In: Astro, LLM/RAG, Docker, AI Automation, Migration Engineering
* Evolved: PHP 4→7, WordPress (legacy→modern), MySQL

The graph doesn't just track skills—it reveals strategic pivots.

## Real-World Testing

I tested the tool with three different profiles:

Senior Specialist(30 nodes, 2.47 density)

* Deep expertise in AI/Migration
* Modern stack (Astro, LLM, Docker)
* High interconnection within niche

Mid-Level Generalist(33 nodes, 2.42 density)

* Broad CMS expertise (WordPress, Magento, PrestaShop)
* Traditional e-commerce stack
* Skills distributed across varied projects

Junior Polyvalent(35 nodes, 2.57 density)

* Modern full-stack (MERN, Angular, Symfony)
* Creative skills (design, video)
* The matrix revealed interesting gaps: claimed Symfony expertise with no projects demonstrating it

Key insight: The tool adapts to different career stages and reveals actionable patterns—like skills declared but not proven in projects.

## How I Built It

### The Problem: Structure, Not Extraction

This isn't keyword extraction. It's about asking AI toreason about contextand produce a structured representation: nodes, relationships, and a graph-oriented vision.

Most CV parsers extract surface-level keywords. This project asks:"What are the semantic connections between my Python skills, my migration projects, and my AI automation expertise?"

### Tech Stack

AI Layer:

* Gemini Flash Preview 3.0for CV analysis
* Google AI Studiofor prompt engineering & iteration
* Custom system prompt with 6 levels of extraction rules

Visualization Layer:

* Streamlitfor the web interface (rapid prototyping)
* vis.js(via streamlit-agraph) for network graphs
* Plotlyfor Sankey flow diagrams & heatmaps

Deployment:

* Google Cloud Runfor containerized deployment (challenge requirement)
* Dockerfor containerization
* GitHub integrationfor CI/CD

Why streamlit-agraph for Network Visualization?

The Network Graph view usesstreamlit-agraph(a vis.js wrapper). During development, I evaluated several alternatives for displaying interactive network graphs in Streamlit. Here's the decision matrix that led to this choice:

Library

Responsive

Interactive

Force-Directed Layout

Dev Time

Verdict

streamlit-agraph

⚠️ Fixed canvas

✅ Full (click, zoom, pan)

✅ Automatic

~2 hours

✅
Selected

Plotly Graph Objects

✅ 100% responsive

⚠️ Limited interactions

❌ Manual positioning

~6 hours

❌ Too much effort

Pyvis

⚠️ HTML file generation

✅ Full

✅ Automatic

~4 hours

❌ Complex integration

NetworkX + Matplotlib

✅ Fully responsive

❌ Static image

✅ Automatic

~3 hours

❌ No interactivity

D3.js Custom

✅ 100% responsive

✅ Full control

✅ Custom

~8+ hours

❌ Time prohibitive

Decision rationale:

For this project,interactivity was the priority. The ability to click nodes, activate focus mode, and explore connections dynamically was more valuable than perfect responsive behavior in iframes.

streamlit-agraphdelivered:

✅ Zero-configuration force-directed layout (nodes position themselves)✅ Full interaction support (click handlers, zoom, pan)✅ Production-ready in ~2 hours of development✅ Professional visual quality out of the box

Trade-off accepted:

⚠️ Fixed canvas size (1400×900px) doesn't fill 100% of iframe width✅ Mitigation: Canvas size chosen to work well on 1440px+ screens (laptops/desktops)

Alternative approaches considered(Plotly, D3.js) would have provided better responsive behavior but at the cost of 3-4× development time and reduced interactivity.

Sostreamlit-agraph hit the sweet spotbetween functionality, visual quality, and development speed.

Note: For optimal experience, open thefull applicationdirectly.

### Responsive Strategy

While the canvas is fixed at 1400×900px, users cancollapse the sidebar(<<button) to gain ~250px of vertical space. This makes the app work perfectly even on 1366-1680px screens.

* Sidebar open: Full controls + graph (optimal on 1920px+)
* Sidebar closed: Full-screen graph (optimal on 1366px+)

User-controlled responsivenessproved more practical than attempting CSS magic with fixed-size canvas elements.

### Development Process

#### 1. Prompt Engineering in Google AI Studio

Before writing any application code, I spent time in AI Studio crafting the extraction prompt. This phase was critical:

LEVEL 1: Core entities (Person, Skills, Projects)
LEVEL 2: Relationships (USES, CREATED, MASTERS)
LEVEL 3: Technical relationships (PHP ENABLES WordPress)
LEVEL 4: Concepts & expertise domains
LEVEL 5: Temporal & contextual relationships
LEVEL 6: Bidirectional concept-project links ← Key innovation

Enter fullscreen mode

Exit fullscreen mode

Why this matters: A CV isn't just nodes, it's theconnectionsthat matter. "Python" isn't just a skill—it ENABLES AI Automation, which is IMPLEMENTED_IN multiple projects, which DEMONSTRATES Migration Engineering expertise.

The prompt evolved through 20+ iterations in AI Studio before integration.

#### 2. Multi-View Dashboard

Initial version had only the network graph. User feedback revealed a problem:different audiences need different views.

* Developerswant to explore connections (Network Graph)
* Recruitersneed quick visual narratives (Flow Diagram)
* Managerswant fast skill scanning (Skills Matrix)

The breakthrough was realizing this isn't three separate features—it'sthree perspectives on the same data.

#### 3. Iterative UX Refinement

Based on real user testing:

* V7.0: Multi-view dashboard
* V7.1-V7.6: Spacing optimization (nodes were overlapping)
* V8.0-V8.2: English interface + demo auto-loading

The demo CV auto-load was inspired by the challenge theme:show, don't tell. Let visitors see the result instantly instead of asking them to upload first.

#### 4. Deployment on Google Cloud Run

As required by the challenge, the app is deployed on Google Cloud Run. The deployment is straightforward:

* Containerized: Streamlit app packaged in Docker
* Serverless: Auto-scaling, pay-per-use
* Public URL: Accessible without authentication
* CI/CD: Connected to GitHub for automatic deployments

Cloud Run was chosen for its simplicity and alignment with the Google AI ecosystem.

### Google AI Tools Used

Google AI Studiowas essential for:

1. Rapid prompt iterationwithout deploying code
2. JSON validationto ensure consistent output structure
3. Token optimizationto stay within rate limits

Gemini Flash Preview 3.0chosen for:

* Multimodal capabilities(PDF → structured JSON)
* Large context window(handles long CVs)
* Structured outputwith consistent formatting
* Speedfor real-time extraction

### Design Decisions

#### Why Graphs?

Traditional CVs aretree structures(chronological). Professional identities aregraphs(relational). The mismatch creates information loss.

Example: My "WordPress to Astro Migration" project connects to:

* Astro framework (USES)
* WordPress (USES)
* Web Performance (DEMONSTRATES)
* Migration Engineering (DEMONSTRATES)
* SSG Ecosystem (IMPLEMENTED_IN)

A timeline can't represent this richness. A graph can.

#### Why Three Visualizations?

Network Graph: For exploration and discovery

* Best for: Deep dives, understanding connections
* Audience: Technical leads, fellow developers

Flow Diagram: For storytelling

* Best for: Quick pitches, visual narratives
* Audience: Recruiters, hiring managers

Skills Matrix: For scanning

* Best for: 30-second skill assessment
* Audience: HR, technical screeners

One visualization can't serve all audiences.This was the key insight.

#### Why Demo-First?

Inspired by product design principles:reduce friction to zero.

Before: "Upload your CV to see how it works" → 50% bounce rateAfter: "Here's mine already loaded, explore now" → Instant engagement

## What I'm Most Proud Of

### 1. Bidirectional Semantic Relationships

The graph doesn't just show that "Newsletter Engine uses Python"—it shows that:

* Python ENABLES AI Automation (capability)
* AI Automation is IMPLEMENTED_IN Newsletter Engine (evidence)
* Newsletter Engine DEMONSTRATES AI Automation (showcase)

Thisbidirectionalitycreates semantic completeness. Each project isn't just a container of technologies—it'sproof of conceptual expertise.

### 2. Dense Graph Quality (70+ Relationships)

Most CV extractors produce sparse graphs (1.0-1.5 edges per node). This achievesdensity 2.4(72 relationships for 30 nodes) by:

* Extracting ALL mentioned technologies (not just "main" skills)
* Creating technology chains (Docker RUNS_ON Linux)
* Linking related projects (wp2md RELATED_TO WordPress Migration)

A dense graph is atruthfulgraph.

### 3. Zero-Config Demo Experience

The app loads with my CV pre-analyzed. No authentication, no API keys to configure, no upload required.

This aligns with "New Year, New You"—the portfolioshows transformation immediatelyrather than promising it.

### 4. Real-Time Adaptation to Feedback

Every version (V1 → V8.2) incorporated user feedback:

* "Nodes overlap" → Mega Wide spacing mode
* "Labels unreadable" → Verdana sans-serif, size optimization
* "Need different views" → Multi-view dashboard
* "Too much friction" → Demo auto-loading

Built in public, refined through dialogue.

### 5. Technical Elegance

The entire extraction happens in asingle prompt. No multi-stage pipeline, no external tools.

response

=

model
.
generate_content
([


{
"
mime_type
"
:

"
application/pdf
"
,

"
data
"
:

cv_bytes
},


EXTRACTION_PROMPT

])

graph_data

=

json
.
loads
(
response
.
text
)

Enter fullscreen mode

Exit fullscreen mode

Input: PDF bytes + promptOutput: Complete knowledge graph

That's it. The complexity is in the prompt design (crafted in AI Studio), not the code.

## Personal Reflection: New Year, New Perspective

This project started as a personal need and became something more:an invitation to view professional identity differently.

We spend so much energy trying to fit our careers into templates. What if the template was wrong?

A knowledge graph doesn't judge whether your path was "correct." It simplyrepresents what is: the skills you have, the projects you built, and how they connect.

In the spirit of "New Year, New You," this isn't about reinventing yourself. It's aboutrepresenting yourself with more accuracy. Sometimes that's enough.

## Try It Yourself

🔗Live App:knowledge-graph-cv-837592265234.europe-west1.run.app

My CV is loaded by default—explore the three views, then upload your own.

📂Source Code:github.com/pcescato/knowledge-graph-cv

## Technical Metrics

* Extraction Time: ~15-25 seconds (Gemini Flash Preview 3.0)
* Average Graph: 25-35 nodes, 60-80 relationships
* Density: 2.0-2.8 (edges per node)
* Supported Formats: PDF only
* Visualizations: 3 (Network, Flow, Matrix)
* Languages: English interface

## What's Next?

This MVP was built in 3 days as a proof of concept for the Google AI Challenge.

Technical roadmap(not yet implemented):

* Export formats: JSON, GraphML, Neo4j cypher for data portability
* Comparison mode: Side-by-side CV analysis to track career evolution
* Skill gap analysis: Compare your graph against target job descriptions
* Temporal dimension: Visualize career progression over time

But I see potential beyond personal portfolios:

* HR Tech: Intelligent candidate matching based on skill graphs, not keywords
* Internal Talent Mapping: Companies understanding who knows what across teams
* Career Coaching: Visualizing skill gaps and growth paths

The graph-based approach reveals connections that traditional CVs hide. If you're building in this space or interested in exploring applications for recruitment, talent analytics, or knowledge management—I'd love to chat.

Special Note on Cost Management & Scraping:While scaling this project, I encountered an unexpected challenge: aggressive scraping. Specifically, bots from Iguane Solutions (a French provider claiming FinOps expertise) saturated my Cloud Run instances, causing a 150% cost spike. It's a textbook case of resource exhaustion. I had to pivot my strategy: implementing custom IP filtering and drastic resource capping (down to 368MiB). This project is now a dual-demonstration: Knowledge Graph AI and defensive Cloud cost management.

Thanks for reading!If this resonates with you, I'd love to hear your thoughts.

Does your career fit into a timeline, or is it a graph?💭

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (16 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
