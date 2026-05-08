---
title: GitHub - flutter/skills · GitHub
url: https://github.com/flutter/skills
site_name: github
content_file: github-github-flutterskills-github
fetched_at: '2026-05-08T12:08:28.271725'
original_url: https://github.com/flutter/skills
author: flutter
description: Contribute to flutter/skills development by creating an account on GitHub.
---

flutter

 

/

skills

Public

* NotificationsYou must be signed in to change notification settings
* Fork86
* Star1.5k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

270 Commits
270 Commits
.github
.github
 
 
resources
resources
 
 
skills
skills
 
 
tool
tool
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pubspec.yaml
pubspec.yaml
 
 
View all files

## Repository files navigation

# Flutter Agent Skills

Agent skills for Flutter, maintained by the Flutter team.
A collection of skills providing tailored instructions for happy path Flutter app development workflows. By giving the agent actual domain expertise and repeatable workflows, you drastically reduce mistakes and ensure agents reliably complete the task following best practices.

Skills are essentially simple folders of files that can be seen as complementary to MCP, where MCP gives an agent access to specialized tools and a Skill teaches the agent “how” to use tools for a specific task.

You can also install theAgent Skills for Dartfor Dart tasks.

## Installation

To install all skills into your project, run the following command.
The--agent universalflag puts it in the standard.agents/skillsfolder that most agents use.

npx skills add flutter/skills --skill 
'
*
'
 --agent universal

## Updating Skills

To update, run the following command:

npx skills update

## Available Skills

Skill

Description

Example prompt

flutter-add-integration-test

Configures Flutter Driver for app interaction and converts MCP actions into permanent integration tests. Use when adding integration testing to a project, exploring UI components via MCP, or automating user flows with the integration_test package.

Add an integration test that validates the checkout experience

flutter-add-widget-preview

Adds interactive widget previews to the project using the previews.dart system. Use when creating new UI components or updating existing screens to ensure consistent design and interactive testing.

Create a preview for the ProductCard widget with different price states

flutter-add-widget-test

Implement a component-level test using 
WidgetTester
 to verify UI rendering and user interactions (tapping, scrolling, entering text). Use when validating that a specific widget displays correct data and responds to events as expected.

Add a widget test for the CustomButton to verify the onTap callback is called

flutter-apply-architecture-best-practices

Architects a Flutter application using the recommended layered approach (UI, Logic, Data). Use when structuring a new project or refactoring for scalability.

Refactor the authentication flow to follow the recommended layered architecture

flutter-build-responsive-layout

Use 
LayoutBuilder
, 
MediaQuery
, or 
Expanded/Flexible
 to create a layout that adapts to different screen sizes. Use when you need the UI to look good on both mobile and tablet/desktop form factors.

Make the home screen responsive so it displays a grid on tablets and a list on phones

flutter-fix-layout-issues

Fixes Flutter layout errors (overflows, unbounded constraints) using Dart and Flutter MCP tools. Use when addressing "RenderFlex overflowed", "Vertical viewport was given unbounded height", or similar layout issues.

Fix the overflow error on the profile page when the keyboard is visible

flutter-implement-json-serialization

Create model classes with 
fromJson
 and 
toJson
 methods using 
dart:convert
. Use when manually mapping JSON keys to class properties for simple data structures.

Implement JSON serialization for the User model class

flutter-setup-declarative-routing

Configure 
MaterialApp.router
 using a package like 
go_router
 for advanced URL-based navigation. Use when developing web applications or mobile apps that require specific deep linking and browser history support.

Set up GoRouter with paths for home, details, and settings

flutter-setup-localization

Add 
flutter_localizations
 and 
intl
 dependencies, enable "generate true" in 
pubspec.yaml
, and create an 
l10n.yaml
 configuration file. Use when initializing localization support for a new Flutter project.

Setup localization and add English and Spanish translations

flutter-use-http-package

Use the 
http
 package to execute GET, POST, PUT, or DELETE requests. Use when you need to fetch from or send data to a REST API.

Use the http package to fetch the list of products from the API

## Contributing

We aren't accepting pull requests at this time, but we would love to hear your feedback!

Please seeCONTRIBUTING.mdfor more information.

## Code of Conduct

Please seeCODE_OF_CONDUCT.mdfor more information.

## About

 No description, website, or topics provided.
 

### Resources

 Readme

 

### License

 BSD-3-Clause license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.5k

 stars
 

### Watchers

17

 watching
 

### Forks

86

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Dart100.0%