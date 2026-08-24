---
title: I Used React DataGrid to Build a Real Space Mission Explorer - DEV Community
url: https://dev.to/hadil/i-used-react-datagrid-to-build-a-real-space-mission-explorer-4g8b
site_name: devto
content_file: devto-i-used-react-datagrid-to-build-a-real-space-missio
fetched_at: '2026-08-24T19:27:14.439570'
original_url: https://dev.to/hadil/i-used-react-datagrid-to-build-a-real-space-mission-explorer-4g8b
author: Hadil Ben Abdallah
date: '2026-08-24'
description: 'I went through the documentation and feature list of React DataGrid, and I wrote React DataGrid: A... Tagged with webdev, programming, react, nextjs.'
tags: '#webdev, #programming, #react, #nextjs'
---

Puts a 100k-row space dataset to the test

I went through the documentation and feature list of React DataGrid, and I wroteReact DataGrid: A Free, Open-Source React Data Grid with an Enterprise Edition (An AG Grid Alternative)

Now I wanted to use it the way I would use any other data grid in a real project: start with a real dataset, build useful interactions around it, push the grid with a large number of records, and see where things get difficult.

So I built aSpace Mission & Satellite Explorer, a small flight-dynamics-style web application for exploring missions across different agencies, destinations, mission types, and decades.

The project works with a100,000-mission live archive, while a1,200-row client-side working setpowers the interactive analysis experience. That gave me a good opportunity to test much more than basic sorting and pagination, including filtering, faceted search, grouping, pivoting, row pinning, custom cell renderers, virtual scrolling, and server-side infinite scrolling.

I also built two other parts of the application around the same data: aMission Analyticspage for aggregating and visualizing the dataset, and aMission Detailspage where I used Tree Data to represent an individual mission's timeline.

This article is about what happened while building it, from setting up React DataGrid and configuring the first columns to working with 100,000 records and deciding whether I'd reach for it again in another data-heavy React project.

## TL;DR

I built a Space Mission Explorer withReact DataGridto see how it would handle a real application.

The project uses a1,200-row client-side datasetfor interactive analysis and a100,000-row live archiveloaded through server-side infinite scrolling.

Along the way, I used features including:

* multi-column sorting
* quick search
* faceted filtering
* row grouping
* row pinning
* a Pivot Table builder
* custom cell renderers
* virtual scrolling
* CSV/Excel export
* Tree Data for Mission Timelines

The integration was smoother than I expected. The API felt familiar from the beginning; most of the features I needed worked as expected from the documented examples with relatively little adjustment, and switching between the smaller working dataset and the full archive stayed responsive.

There were still a few areas that required more digging, which I'll cover later, but overall, building the project gave me a better impression of React DataGrid than I could have gotten from reading its feature list.

## What I Built: A Space Mission Explorer

I called the project anOrbital Index / Mission Data Terminal.

The idea was simple: take a large archive of fictionalized space-mission records and turn it into something developers could imagine using, a searchable, filterable interface where you can explore missions by agency, destination, status, mission type, launch date, duration, cost, and decade.

I deliberately chose this instead of building another generic CRUD dashboard because the dataset naturally creates the kinds of problems where a data grid becomes useful.

A mission record has enough structured fields to make filtering and sorting meaningful. Missions can be grouped by agency or destination. Costs and durations can be aggregated. And the mission itself has a natural hierarchy:

Launch → Earth Orbit → Translunar Injection → Lunar Orbit → Descent & Landing → Surface Operations → Return to Earth

That last part also gave me a reason to test Tree Data instead of adding it just to check another feature off a list.

The application ended up with three main pages:

* Mission Explorer:The main data-grid interface for searching, filtering, grouping, pivoting, editing, and exploring the mission archive.
* Mission Analytics:A chart-focused view that turns the same mission data into success rates, agency comparisons, destination distributions, duration statistics, and cost analysis.
* Mission Details:An individual mission view with metadata, crew and equipment information, related dossiers, and a hierarchical mission timeline.

The Explorer is where most of my React DataGrid testing happened. The Analytics page uses the same 1,200-row working dataset and aggregation logic to produce visualizations, while the Details page gave me a completely different use case for the grid's hierarchical data capabilities.

For the stack, I usedReact,TypeScript,Tailwind CSS,React DataGrid, the mission dataset, and a charting library for the analytics view.

One quick transparency note before I dive into the grid: I vibe-coded a small part of the initial project setup to avoid spending a big chunk of my time building boilerplate that wasn't really the point of this experiment.

The goal here wasn't to prove that I could build an entire space-mission website from scratch; it was to spend my time actually using React DataGrid in a realistic project and see how it handled the data, interactions, and scale.

I deliberately kept the project small enough to understand from end to end but complex enough that a basic<table>would start becoming a problem.

You can check out the full project and explore the missions yourself.

Live Demo 👀

GitHub Repository ⭐

## Setting Up React DataGrid

Once I had the project structure in place, I wanted to get the grid working before spending time on the rest of the interface. I started with the open-source package and kept the first render intentionally simple.

The installation was straightforward:

npm 
install 
react-open-source-grid

Enter fullscreen mode

Exit fullscreen mode

Then I imported the library's stylesheet:

import
 
'
react-open-source-grid/dist/lib/index.css
'
;

Enter fullscreen mode

Exit fullscreen mode

For the first test, I created a small grid with only a few mission fields:

const
 
columns
:
 
Column
[]
 
=
 
[

 
{
 
field
:
 
'
mission
'
,
 
headerName
:
 
'
Mission
'
,
 
width
:
 
200
 
},

 
{
 
field
:
 
'
agency
'
,
 
headerName
:
 
'
Agency
'
,
 
width
:
 
120
 
},

 
{
 
field
:
 
'
status
'
,
 
headerName
:
 
'
Status
'
,
 
width
:
 
140
 
},

 
{
 
field
:
 
'
launchDate
'
,
 
headerName
:
 
'
Launch Date
'
,
 
width
:
 
130
 
},

 
{
 
field
:
 
'
destination
'
,
 
headerName
:
 
'
Destination
'
,
 
width
:
 
150
 
},

];

Enter fullscreen mode

Exit fullscreen mode

From there, I defined typed columns forMission,Agency,Status,Launch Date,Destination,Mission Type, andDurationand mapped the dataset to them.

At this stage, the API felt familiar, so I didn't have to spend much time learning a completely unfamiliar grid model.

I also kept the React DataGridGitHub repositoryanddocumentationclose by while building, since this was a hands-on test.

## Building the Mission Explorer

I didn't want to build a grid with a few rows just to say I had used one. I wanted enough data and enough interactions to see whether the component could handle the kind of complexity you'd expect in a real application.

I ended up using two dataset modes: a1,200-row client-side working setfor interactive analysis, virtual scrolling, and a100,000-row live archivethat loads records on demand through server-side infinite scrolling.

The difference between the two modes was useful because it gave me two different ways to work with the same mission data instead of artificially creating a huge dataset just for benchmarking.

Mission Explorer page

 

### Sorting, Filtering, and Search

I started with the interactions I'd expect from any data grid. The column headers support sorting, including multi-column sorting, so I could do things like sort missions by agency and then by launch date without writing custom sorting logic myself.

For filtering, I had both the global search bar and individual column filters. The global search makes it easy to quickly find a mission, agency, or destination, while the filters directly under the column headers give me more control when I need to narrow down a specific field.

The sidebar filters were even more useful for this dataset. Instead of forcing me to type everything into a search box, thefaceted searchpanel lets me filter by Agency, Status, Destination, Mission Type, and Decade. Each facet also displays live counts, such asNASA (265)orSuccessful (839), so I can immediately see how much data each filter represents.

If I want to see only successful NASA missions to Mars from the 1990s, I can narrow the dataset from several different dimensions without building a complicated filter UI around the grid myself.

I also tested column resizing and reordering, and both were straightforward to use when adjusting the Explorer to different screen sizes and workflows.

Sorting, Filtering, and Search

 

### Grouping and Pinning

Once filtering was working, I wanted to see how the grid handled more analytical interactions.

React DataGrid lets me drag columns into the grouping area above the table. That means I can group missions by something like "Agency" and then further organize them by another field, instead of treating every mission as an isolated row.

Grouping and Pinning

 

I also pinned four reference missions to the top of the grid. This is a small feature, but I found it really useful when working with a large dataset because important records remain visible while I scroll through the rest of the archive.

### Pivot Table

The most interesting part of the Explorer was the built-inPivot Tablebuilder.

Instead of manually writing aggregation logic for every analysis I wanted to perform, I could choose aRow Group By,Pivot Column,Value Column, andAggregation, then apply the configuration directly from the interface. I could also toggle totals rows and a grand total column.

For example, I could group missions by agency, pivot them by destination, and aggregate values such as duration or cost. That turns the grid from a place where I simply browse records into something I can use to explore the dataset.

Pivot Table

 

### Custom Cells, Totals, and Export

I also used custom cell rendering to make the grid easier to scan. Mission statuses aren't displayed as plain text; they're represented with color-coded badges forSuccessful,Planned,Partial Success,Failed,Cancelled, andin progress. The working set also includes a totals footer that aggregates values such as duration and cost.

Around the grid, I added the controls I would actually expect to use in a production data table: a column picker, CSV and Excel export, a layout reset control, and four density options ranging fromUltra CompacttoComfortable.

Custom Cells and Totals

 

CSV and Excel export

 

What I liked most was being able to combine faceted filtering, grouping, pivoting, pinned rows, custom renderers, and export in the same interface without the page turning into a collection of disconnected controls.

## Building Mission Analytics

Once the Mission Explorer was working, I wanted to use the same dataset for something beyond browsing individual records. That's why I made the second page,Mission Analytics.

This page is deliberately chart-first. Instead of displaying another table, I used the same mission data and aggregation logic from the Explorer to create a set of visualizations that answer higher-level questions about mission history, agencies, destinations, and costs.

At the top, I added four summary cards:

* 1,200missions in scope
* 79.6%average success rate
* $669.12Bin program cost
* 1,543 daysaverage mission duration

Under those cards, the page contains five different visualizations: launch cadence by decade, agency reliability, destination distribution, success profile by mission type, and cost versus mission duration.

Mission Analytics page

 

### Launch Cadence and Agency Reliability

The first chart looks atLaunch Cadence by Decade, showing how the number of missions and successful missions changed across the different decades in the dataset.

This gives the archive a historical dimension that isn't obvious when you're looking at individual rows in the Explorer. Instead of asking which missions launched, I can start asking how mission activity changed over time.

Next, theAgency Reliabilitychart compares launch volume with average success rates across agencies such as NASA, SpaceX, Roscosmos, ESA, CNSA, ISRO, JAXA, and Blue Origin.

This is where the aggregation capabilities became useful. The chart isn't based on a separate dataset created just for the dashboard. It's derived from the same mission records I was already filtering, grouping, and analyzing in the Explorer.

Launch Cadence and Agency Reliability

 

### Destination, Mission Type, and Cost

The other three visualizations look at different dimensions of the same data.

TheDestination Distributionchart shows where missions in the archive are going, with destinations including Earth Orbit, the Moon, Mars, the Asteroid Belt, Deep Space, and Jupiter.

TheSuccess Profile by Mission Typetakes another angle by comparing success rates across mission types such as rovers, orbiters, flybys, robotic landers, space telescopes, and sample-return missions.

Finally, theCost vs. Mission Durationscatter plot lets me look at whether expensive missions also tend to have longer durations. Each point represents an individual mission, making it easier to spot unusually expensive or long-running programs.

What I found interesting here is that I didn't need to put another grid on this page for React DataGrid to remain useful. The grid's underlying dataset and aggregation logic are still doing the work; I'm simply presenting the results in a form that's easier to interpret visually.

Destination, Mission Type, and Cost

## Building the Mission Details Page

After working with the full archive, I wanted the third page to do the opposite: take me from100,000 missions down to one specific mission.

For this example, I usedMX-000006, Apollo VIII. The page brings the mission's main information together, including its launch date, duration, program cost, and crew, without forcing everything into another large table.

Mission Details Page

 

The most interesting part of this page, though, is theMission Timeline.

### Using Tree Data for a Real Mission Timeline

A mission isn't just a collection of unrelated fields. It naturally has an ordered structure: launch happens before orbital insertion, which happens before the mission's main operations, and so on.

That made the timeline a good place to useTree Data.

For Apollo VIII, I structured the mission into 5 phases:

Apollo VIII
├── Launch
├── Orbit Insertion
├── Payload Commissioning
├── Operations
└── Deorbit

Enter fullscreen mode

Exit fullscreen mode

Each phase has its ownCOMPLETEstatus badge and aT+day offset, so the timeline gives me both the hierarchy and the chronological context of the mission.

Tree Data for a Real Mission

 

This is one of the features that made more sense once I had a real application to build. I could have created a custom nested component for the timeline, but Tree Data already maps naturally to this kind of structured information.

The rest of the page contains theCrew Manifest,Payload & Equipment, andRelated Dossierssections. These keep the additional mission information accessible without turning the page into another dense data-management screen.

Crew Manifest, Payload & Equipment and Related Dossiers

 

At this point, I had all three parts of the application working together:

* Mission Explorerfor searching and manipulating the archive
* Mission Analyticsfor understanding the data at a higher level
* Mission Detailsfor drilling into an individual mission

This gave me a better environment for evaluating React DataGrid than a small demo table would have. I had real filtering, grouping, pivoting, hierarchical data, custom rendering, and large datasets all working in the same project.

## Theming & UI Customization

Once the functionality was working, I spent some time making the grid belong inside the application. The default data grid look would have worked, but it didn't really fit the dark, cyan-accentedflight dynamics terminalstyle I was going for.

I used theme variables to adapt the grid's appearance and added custom cell renderers for the mission status badges. The badges use different colors for states such as Successful, Planned, Partial Success, Failed, Cancelled, and in progress, which makes scanning the Explorer much easier.

I also used four density modes,Ultra Compact, Compact, Normal, and Comfortable, so the amount of information displayed per row can be adjusted without rebuilding the grid layout.

What I appreciated here is that customization didn't require me to fight the component's default styling. Most of the work was about making React DataGrid match the visual language of the project rather than trying to work around the grid itself.

## Developer Experience: What Was Easy and What Took More Work

The overall developer experience was one of the biggest positives from this project. Installation and getting the first working grid on screen took less time than I expected, and the API felt familiar.

Once the basic grid was running, adding sorting, filtering, grouping, and the Pivot Table builder was straightforward and aligned with the documented examples. The same was true for the Tree Data implementation on the Mission Details page. I wasn't constantly trying to figure out how to make the library do something it wasn't designed to do.

Accessibility was another area I paid attention to while working with the grid. I also tested keyboard navigation and paid attention to the grid's ARIA behavior while working through the interface. The documentation also gave me enough examples to understand the less common features I was using.

That said, not every part of the process was equally straightforward. The more specialized features required more time to understand than everyday operations such as sorting or filtering. The Pivot Table builder and Tree Data configuration were the areas where I spent more time checking examples and figuring out exactly how I wanted the data structured.

## React DataGrid vs. a Basic HTML Table: What I Would Choose

If I were only displaying five or ten rows of static data, I wouldn't reach for React DataGrid. A basic HTML table or lightweight React table would be simpler and would do the job well.

This project was a very different situation.

Once I needed100,000 missions, faceted search, multi-column sorting, grouping, pivoting, Tree Data, custom cell renderers, and server-side infinite scrolling, a basic table would have required me to build a large part of that functionality myself.

That's where React DataGrid made more sense. Instead of spending my time building and maintaining table infrastructure, I could focus on the actual application: how missions should be organized, what users should be able to explore, and how the analytics should work.

## Is React DataGrid Worth Using?

After building a project with it, I think React DataGrid makes sense for applications where the data itself is a major part of the user experience.

I'd particularly consider it for:

* Data-intensive dashboards
* Analytics applications
* Admin interfaces
* Financial applications
* Internal business tools
* Applications with large datasets
* Projects with complex filtering or grouping
* Applications with hierarchical data
* React applications that need server-side data loading

The Space Mission Explorer was a good test because it combined several of these requirements at once. I had a 1,200-row client-side working set for interactive analysis and a 100,000-mission live archive using server-side infinite scrolling.

## Final Thoughts

Building the Space Mission Explorer gave me a better perspective on React DataGrid than I could have gotten from a feature checklist alone.

I was able to take a real dataset, turn it into an interactive explorer for a 100,000-row mission archive, build analytics around it, and use Tree Data for a mission timeline without having to build the grid infrastructure myself.

For data-heavy React applications, that's ultimately what matters:

The grid should handle the complexity of the data so you can focus on building the product around it.

Thanks for reading! 🙏🏻 
 I hope you found this useful ✅ 
 Please react and follow for more 😍 
 Made with 💙 by 
Hadil Ben Abdallah

 
 

## Hadil Ben AbdallahFollow

Software Engineer • Technical Writer (300K+ readers & 20K+ followers) • Trusted by 10+ companies
I turn brands into websites people 💙 to use

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse