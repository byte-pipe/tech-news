---
title: Pele · Mermaid diagrams as themeable SVG
url: https://pele.run/
date: 2026-10-17
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-18T14:20:11.390462
---

# Pele · Mermaid diagrams as themeable SVG

## Pele: Lightweight Mermaid Diagram Renderer for SVG

### Introduction
Pele is a lightweight library that renders Mermaid diagrams to SVG, themed with CSS variables. It offers direct dependencies, small screen adaptation, and themed configuration.

### Mermaid Syntax
The following Mermaid syntax is used to render the Mermaid diagram to SVG:
```markdown
Mermaid
1
flowchart
    TD
    A[Mermaid text]
    B[SVG]
3
B
    -- pele-bg
    : #fffcf0
    -- pele-fg
    : #100f0f
    -- pele-muted
    : #6f6e69
    -- pele-line
    : #100f0f
    -- pele-surface
    : #f2f0e5
    -- pele-surface-alt
    : #e6e4d9
    -- pele-border
    : #cecdc3
Pele
Themes
Variables
Light
Dark
Pele
Mermaid.js
Bundle size
gzip
230 kB
1.6 MB
Render time
0.05–0.3 ms
6–82 ms
Direct dependencies
0
23
Small screens
Adapts the layout
Scales the diagram
Theming
CSS variables
Theme configuration

Add Pele to your app using the API.

npm
pnpm
yarn
bun
1
npm
install pele
1
pnpm
add pele
1
yarn
add pele
1
bun
add pele
```

### Themed Rendering
Pele supports customization through CSS variables. The Mermaid syntax can be edited to replace variable names with the corresponding values.

```markdown
Mermaid
1
flowchart
    TD
    A[Mermaid text]
    B[ SVG]
3
B
    -- pele-bg
    : #e6e4d9 (Themed pele-bg variable)
    -- pele-fg
    : #f2f0e5 (Themed pele-fg variable)
    -- pele-muted
    : #6f6e69 (Themed pele-muted variable)
    -- pele-line
    : #100f0f
    -- pele-surface
    : #fffcf0 (Themed pele-surface variable)
    -- pele-surface-alt
    : #e6e4d9 (Themed pele-surface-alt variable)
    -- pele-border
    : #cecdc3
Pele
Themes
Variables
Light
Dark
Pele
Mermaid.js
Bundle size
gzip
230 kB
1.6 MB
Render time
0.05–0.3 ms
6–82 ms
Direct dependencies
0
23
Small screens
Adapts the layout
Scales the diagram
Theming
CSS variables
Theme configuration

Add Pele to your app using the API.
```

### API Integration
To integrate Pele into your app, add it using npm or yarn:
```bash
npm install pele
```

Then, pass the Mermaid syntax to the `render()` function and insert the returned SVG into your page:
```javascript
import pele from 'pele';

const rendered SVG = `
    flowchart LR
    4
    A[Mermaid text] --> B[SVG]
`;
document.querySelector('#diagram').innerHTML = pele.render(rendered SVG);
```
The rendered SVG will be displayed with the customized theme.