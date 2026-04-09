---
title: Observable Notebooks 2.0 Technology Preview | Observable
url: https://observablehq.com/notebook-kit/
site_name: hackernews
fetched_at: '2025-07-30T07:05:07.089754'
original_url: https://observablehq.com/notebook-kit/
author: mbostock
date: '2025-07-30'
---

# Observable Notebooks 2.0Technology Preview

Thefuture of notebooks📓🔮 is here. We’re building the next generation of Observable Notebooks, and we’re excited to share a technology preview that you can start using today. 🚀

Specifically, we’re releasing two things:

1. Observable Notebook Kit- An open file format for notebooks, and accompanying tooling for generating static sites
2. Observable Desktop- A macOS desktop application for editing notebooks as local files, and with a radical new approach to AI

This is a technology preview, meaning our work isn’t done, but we would like you to try it out and give us your feedback. We’re taking a local-first approach: our plan is to bring these new notebooks, editor, and AI to the web in the near future, providing seamless collaboration and sharing through the Observable platform.

## Why we’re doing this

Our goals for Notebooks 2.0 are:

* Support file-based workflowsso you can do more with notebooks
* Adopt vanilla JavaScriptso notebooks are easier to learn, use, & reuse
* Modernize notebooksto support the latest syntax & libraries
* Render notebooks as fast static sitesfor the best reading experience

To achieve these goals, we’ve developed an opennotebook file formatand are releasingObservable Notebook Kit, an open-source command-line interface (and Vite plugin) for generating static sites from notebooks. You can use Notebook Kit for self-hosting and continuous deployment of notebooks, to deeply integrate notebooks into custom web applications, and more.

In addition to growing notebooks as reusable, extensible technology, we want to improve the experience of authoring notebooks. We are therefore also developingObservable Desktop, a desktop application for editing notebooks that brings the magic ✨ of Observable Notebooks to file-based workflows.

Our goals for a next-generation notebook editor are:

* Seamlessly integrate AIto boost creativity, learning, and productivity
* Streamline editingfor a clean look and feel, focused on coding

Notebooks are theperfectenvironment for coding with AI. The instant feedback you get with reactive coding, the lightweight composability and flexibility of cells, the ability to inspect and tinker to understand what the code is doing, the infinite variety of importable open-source libraries at your fingertips — notebooks enable AI to perform as a more effective teacher and muse, inviting you to collaborate with it, rather than treating it as a black box code generator.

Eventually, this new editor and AI will be coming to the web, giving you the same great authoring experience for notebooks — whether you want the convenience of instant sharing via an Observable workspace, or you prefer to work with local files and manage collaboration yourself (say through git).

You won’t need Observable Desktop to author notebooks — you can author notebooks in your preferred text editor, and then preview or build them using Notebook Kit. But our goal is to build the best-in-class editor for notebooks that supercharges your productivity with AI, combined with instant collaboration and sharing in Observable workspaces, together withObservable Canvasesfor rapid, cross-functional, visual exploration and presentation of data. We’d love for you to use our open-source, but we’re ready for your business, too.

## What’s new

### Notebook file format

The heart of Notebooks 2.0 is a simple, human-readable, and human-editable file format. It’s based on HTML, which means you get nice editing affordances in today’s text editors without needing special plugins. In addition, it’s easy to review diffs when storing notebooks in source control, to search, to find-and-replace, and countless other workflows.

The Observable Notebook file format consists of:

* a<notebook>root element,
* an optional<title>element, and
* one<script>element per cell.

Here’s a simple “hello world” notebook to demonstrate:

<!doctype html>

<
notebook
>
 <
title
>Hello, world!</
title
>
 <
script

id
=
"1"

type
=
"text/markdown"
>
 # Hello, world!
 </
script
>
 <
script

id
=
"2"

type
=
"module"

pinned
>
 1 + 2
 </
script
>
</
notebook
>

See theNotebook Kit documentationfor more on the notebook file format.

### Vanilla JavaScript

You no longer have to learn a nonstandard dialect,Observable JavaScript, to use Observable Notebooks; they’re now vanilla JavaScript. This also makes it easier to reuse code between notebooks and other web applications.

If you don’t know Observable JavaScript, this change will be largely invisible — JavaScript will “just work” like you expect. But if you’re familiar with past notebooks, here are some highlights:

* You declare top-level variables in cells with standardconstandlet, and cells can now expose as many top-level variables as they want rather than being limited to just one.
* You display content with thedisplay(…)function, and cells can display multiple things, even asynchronously. You likewise define reactive inputs with theview(…)function, and cells can have multiple reactive inputs rather than being limited to just one.
* You import libraries from npm (and JSR, the web, and local modules) with standard staticimportdeclarations rather than being limited torequireand dynamic imports.

See theNotebooks system guidefor more on JavaScript in notebooks. And see the gallery below for lots of examples.

### Themes and greater customizability

People love to customize the look-and-feel of notebooks — maybe you prefer a sans serif font, more pink 🦄, dark mode, whatever. Notebooks 2.0 allow styling via custom stylesheets. And notebooks are now “full bleed”, meaning they extend to the full width of the window rather than being limited to a central column. You can evenanimate colorful blobs as the background.

To make customization easier, we’ve also brought themes from Observable Framework back to notebooks. You can choose from a variety of beautiful, built-in colorways, suitable for both light and dark modes.

And when building static sites from notebooks, you can further customize the appearance of your built notebooks by adding a custom page template, say to add a header and footer. With themes and page templates together, you have complete control over the appearance of your notebooks.

### Modernized standard library

Notebooks 2.0 upgrades the built-ins available by default in notebooks. This includes upgrading core functions that aren’t strictly backwards compatible, namely themd,html, andtextagged template literals that power Markdown, HTML, and cells. In Notebooks 2.0, these are now powered by the latest versions ofmarkdown-it,Hypertext Literal, and.

Notebooks 2.0 also fully embraces JavaScript modules, removing built-in support forrequire(asynchronous module definitions) — the now-antiquated way of loading JavaScript modules that predatesimport. Thanks to vanilla JavaScript syntax, you can use standard static import declarations or dynamic import expressions. And you can import libraries from npm (npm:), JSR (jsr:), local modules, or remote servers. You can also import existing Observable notebooks (observable:).

### Notebooks as static sites

When you want to share your notebooks as a static site, install the open-source Notebook Kit:

npm install @observablehq/notebook-kit

Then define a couple scripts in yourpackage.json:

{
 "dependencies": {
 "@observablehq/notebook-kit": "^1.0.1"
 },
 "scripts": {
 "docs:preview": "notebooks preview --root docs",
 "docs:build": "notebooks build --root docs -- docs/*.html"
 }
}

Then run thenotebooks buildcommand:

npm run docs:build

This generates a.observable/distfolder containing the built site, which you can then deploy to your preferred static site hosting service, such as GitHub Pages, Vercel, or Netlify.

When building notebooks, we use static generation for Markdown and HTML cells: static content is statically rendered. This improves the user experience by accelerating the first contentful paint, and by reducing reflow during page load — your page appears instantly. It’s good for SEO, too, because static content is now readable by search engines without JavaScript.

Thebuildcommand is implemented on top ofVite, making it incredibly fast. If you prefer to author notebooks in a text editor rather than using Observable Desktop, you can use Vite’s preview server for a live preview as you edit.

npm run docs:preview

See theNotebook Kit documentationfor more.

When we bring the next-generation notebook editor to the web, you won’t need terminal commands to share notebooks — you’ll be able to share notebooks directly from the editor. We’ll also work on making it easy to transition between local and web-based development. But we’re providing this open-source tooling to give you flexibility and to enable deeper, custom notebook integrations. You should be able to do whatever you want with your notebooks.

## Desktop editor

If you’re interested in trying Notebooks 2.0 and give us feedback, and you’re on macOS, please download the technology preview of Observable Desktop:

 Download for macOS


Observable Desktop currently requires macOS 15+ and Apple Silicon. By downloading and using Observable Desktop, you agree to ourterms of service. An Observable account is required.

Here’s a short demo of authoring notebooks:

See theDesktop user guidefor help getting started.

## Gallery

These examples have been ported from the D3 gallery, along with a few of our other notebooks, and new examples.

Animated treemap

Antimeridian cutting

Arc diagram

Arc tween

Bar chart

Bar chart race

Bar chart transitions

Bivariate choropleth

Brushable parallel coordinates

Brushable scatterplot matrix

Brushable scatterplot

Bubble chart

Calendar

Chord diagram

Choropleth

Collapsible tree

Collision detection

Connected scatterplot

Density contours

Disjoint force-directed graph

Epicyclic gearing

Force-directed graph

Force-directed tree

Global temperature trends

Hertzsprung–Russell diagram

Hexbin map

Hierarchical bar chart

Hierarchical edge bundling

Hierarchical edge bundling

Horizon chart

Icelandic population by age

The impact of vaccines

Index chart

Inequality in American cities

Marey's trains

Mobile patent suits

Orthographic-to-equirectangular

Circle packing

Pannable area chart

Parabolic arcs

Parallel coordinates

Parallel sets

Pie chart update

Projection transitions

PSR B1919+21

Radial tidy tree

Ridgeline plot

Sankey diagram

Scatterplot matrix

Scatterplot tour

Smooth zooming

Stacked-to-grouped bars

Star map

Streamgraph transitions

Temporal force-directed graph

Tree of life

Tidy tree

Treemap

Versor dragging

Voronoi labels

Voronoi stippling

Walmart's growth

Wealth & health of nations

World tour

Zoom to bounding box

Zoomable area chart

Zoomable bar chart

Zoomable icicle

Zoomable circle packing

Zoomable sunburst

## We want your feedback

We have a variety of additional features and improvements planned for Notebooks 2.0, but we’d love your feedback to prioritize and guide development. We are usingGitHub IssuesandDiscussionsto receive feedback. Please upvote issues you care about by reacting with a 👍, and post new issues with your feedback or suggestions.

If you build something with Notebooks 2.0, we’d also love to see it! This page ishosted on GitHub, and we’d love to feature your work in the gallery above.
