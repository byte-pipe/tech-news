---
title: Theme Builder — Zed
url: https://zed.dev/theme-builder
date: 2026-05-09
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-10T07:47:01.202729
---

# Theme Builder — Zed

# Theme Builder — Zed

## Overview
- Theme Builder is only available on the desktop version of Zed; the web view can be used to browse existing theme extensions.  
- The interface is organized into sections such as **Colors** and **Syntax**, each containing groups of token definitions (e.g., Surface11, Border6, Text6, Icon4, etc.).  

## UI Controls
- **View Theme Extensions** – opens a list of available extensions.  
- **Create New Theme**, **Reset**, **Import**, **Export** – manage custom themes.  
- Breadcrumb navigation shows the current location: `zed.dev / main / Share`.  

## Sample Token Definitions
- **Surface11**  
  - Background: `#3b414dff`  
  - Surface background: `#2f343eff` (used for elevated surfaces, panels, overlays)  
  - Panel focus border: linked to `border.focused`  
  - Panel indent guides: `panel.indent_guide`, `panel.indent_guide_hover`, `panel.indent_guide_active`  
- Other token groups listed without detailed values: Border6, Text6, Icon4, Editor19, Navigation4, Element6, Ghost Element5, Drop Target2, Tabs3, Scrollbar6, Minimap4, Status42, Version Control8, Terminal28, Players24.  

## Example Code Included
- A **React** component named `MeetingScheduler` written in **TypeScript** demonstrates theme‑related UI logic.  
- **Key parts of the code**  
  - Interfaces: `Meeting`, `MeetingSchedulerProps`.  
  - Types: `MeetingStatus` (scheduled, running‑late, cancelled, eternal).  
  - Validation function `validateMeeting` checks attendee count.  
  - Constant `MEETING_EXCUSES` holds a list of preset excuse strings.  
  - State hooks manage meetings list, excuse index, loading flag.  
  - Refs for the form element and a numeric “sanity” counter.  
  - `useMemo` selects the current excuse based on the index.  
  - `useEffect` decrements the sanity counter every minute and logs a warning when it reaches zero.  
  - `handleCreateMeeting` validates attendees, creates a new meeting object (contains intentional type errors such as assigning a string to `actuallyStartsOnTime`), updates state, and invokes optional callbacks.  
  - Rendered UI includes a header with the current excuse, a form for meeting title and duration, a submit button that shows a loading state, and a list of created meetings.  
- Lint warnings highlighted in the snippet: unused variable, type mismatches, suggested `const` declaration, misspelled parameter name.  

## Editor Context
- Zed version **1.1.7** running on **macOS**.  
- File view shows staged changes (e.g., `src/services/coffee.ts`, `utils/monday.ts`) and untracked files (`src/utils/excuses.ts`, `meeting-survival.ts`).  
- Commit message placeholder: “Fixed the thing that broke the thing”.  
- The theme builder initialization message appears at the end of the view.