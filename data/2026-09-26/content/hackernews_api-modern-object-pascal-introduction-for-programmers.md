---
title: Modern Object Pascal Introduction for Programmers | Castle Game Engine
url: https://castle-engine.io/modern_pascal
site_name: hackernews_api
content_file: hackernews_api-modern-object-pascal-introduction-for-programmers
fetched_at: '2026-09-26T21:49:03.891131'
original_url: https://castle-engine.io/modern_pascal
author: birdculture
date: '2026-09-24'
description: Modern Object Pascal Introduction for Programmers
tags:
- hackernews
- trending
---

// Just use this line in all modern FPC sources.

{$ifdef FPC}
 
{$mode objfpc}
{$H+}
{$J-}
 
{$endif}

// Below is needed for console programs on Windows,

// otherwise (with Delphi) the default is GUI program without console.

{$ifdef MSWINDOWS}
 
{$apptype CONSOLE}
 
{$endif}

program
 MyProgram;

begin

 WriteLn(
'
Hello world!
'
);

end
.