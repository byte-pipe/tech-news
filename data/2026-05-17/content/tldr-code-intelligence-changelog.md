---
title: Code Intelligence – Changelog
url: https://linear.app/changelog/2026-05-14-code-intelligence
site_name: tldr
content_file: tldr-code-intelligence-changelog
fetched_at: '2026-05-17T11:28:35.703569'
original_url: https://linear.app/changelog/2026-05-14-code-intelligence
date: '2026-05-17'
description: Linear changelog - New updates and improvements to Linear.
tags:
- tldr
---

Changelog
May 14, 2026
 Share

## Code Intelligence

Elapsed
00:00
Seek to:
00:00
 / 
Duration
00:00
Remaining
−
00:00
0.25
×
0.5
×
0.75
×
1
×
1.25
×
1.5
×
1.75
×
2
×

Code Intelligence gives Linear Agent controlled access to your codebase, turning repositories into shared product context your whole team can use.

With Code Intelligence, Linear Agent can reason about how your product actually works, not just what’s captured in issues, projects, and docs. Ask how a feature is implemented, why something behaves a certain way, what a change might affect, or which technical constraints should shape a plan or customer request without digging through the codebase or interrupting an engineer.

PMs can write sharper specs, Support and Sales can answer technical questions with more confidence, and Engineering can investigate bugs, regressions, and unfamiliar parts of the system faster.

To set up Code Intelligence, a workspace admin should:

1. Install theGitHub integrationand enable code access
2. Turn on Code Intelligence inAI Settings

From there, admins can choose which repositories to include and whether access is limited to members with existing GitHub permissions or available to the entire workspace.

Code Intelligence is now available in public beta for Business and Enterprise plans, and free to use during the beta period. See thedocsfor more details.

Fixes
* AgentFixed an issue where the agent chat could not be closed while an attachment modal was open
* AgentFixed natural-language confirmations in Slack threads being recognized while awaiting approval, even without an@Linearmention
* AndroidRemoved the non-responding Linear workspace user from mention autocomplete so only the agent variant appears
* BoardsFixed shared multi-team board views showing different status column orders to different viewers
* CommentsCmd/CtrlFnow expands collapsed comment threads when a hidden reply matches the search
* Customer requestsThe empty-stateAdd requestbutton on a project’s customer requests page now opens the create form
* DashboardsFixed double confirmation when deleting a new unnamed dashboard
* DocsFixed anchor links in the docs “On this page” sidebar replacing the URL hash correctly
* EditorFixed the overflow menu trigger on block images disappearing when the menu opened
* ImportsFixed migrated document issue links so fallback deep links open in the destination workspace
* InboxFixed a bug causing notifications for deleted issues to show up in inbox without issue details
* IntegrationsFixed Sentry installation getting stuck on “Continue in the Linear app” when started from Sentry’s directory
* IssuesFixed the status icon hit area in issue lists so near-edge clicks change status instead of opening the issue
* ProjectsFixed project progress tooltips behaving consistently across List, Board, and Timeline
* ProjectsPrevented project updates from being created with a start date after the target date
* ReleasesFixed release search by version
* ReleasesFixed release sync applying provided names to existing releases, not just newly created ones
* SlackFixed automation comments appearing in Slack as the Linear bot instead of “Linear (via Linear)”
* ZendeskFixed the Include message toggle reliably inserting the ticket message when enabled, even with a template applied
Improvements
* AgentLinear Agent can now resolve and unresolve comment threads, including in automation flows triggered in triage
* AgentsUsers can now queue follow-up messages while an agent is still working, and they’ll send when the current turn completes
* AndroidAdded a long-press menu for folders in Favorites with rename and remove actions
* CommentsAdded a hint below the comment input on duplicate issues pointing to the canonical issue
* DocumentsAdded a Last edited column and matching sort option to the team documents table
* DuplicatesIssue popovers now show the canonical issue when hovering over a duplicate
* FavoritesFavorited teams now show the Team Details hover card
* FavoritesAdded the ability to favorite a team
* IssuesAdded a delegation footer to issue cards in AI chat showing the agent name and live status
* IssuesAdded an animated desktop tab indicator for issues and pull request reviews when a coding agent is actively working
* NotificationsAdded an option to hide sidebar notification badges
* ProjectsAdded a No milestone quick filter at the bottom of the milestones list in the project sidebar
* ReleasesAdded contextual menu actions for attaching documents and links
* SettingsAdded a Manage button to the current plan card in billing settings with actions to switch plans, change billing period, or cancel
* SettingsAdded a Switch plan modal in billing settings for changing plans without leaving the page
* TeamShowed the team icon next to the Team documents group header in the Documents tab
API
* ProjectsAddedslackChannelIdandmicrosoftTeamsChannelIdfields onProjectto return the IDs of connected chat channels
* ReleasesAddedcreatedAt,startedAt, andcompletedAtfields to release inputs to support backdating
* SCIMSCIM user payloads now always populate user groups
MCP server
* save_projectno longer accepts issue-level label IDs, and label arrays sent as JSON strings are parsed instead of silently wiping existing labels
* AddedslackChannelIdandmicrosoftTeamsChannelIdfields onProjectto return the IDs of connected chat channels
* Addedinitiativeandcycleparameters to thesave_documenttool to create or reparent documents under an initiative or cycle
* Unknown tool parameters now return a validation error instead of being silently dropped
Keyboard shortcuts
* FixedAltlettershortcuts (e.g.,AltR) being treated as plain letter presses on Linux/Windows