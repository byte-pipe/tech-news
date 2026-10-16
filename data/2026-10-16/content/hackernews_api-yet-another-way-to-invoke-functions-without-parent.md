---
title: yet another way to invoke functions without parentheses - bartosz's blog
url: https://blog.ikaes.de/yet-another-way-to-invoke-functions-without-parentheses/
site_name: hackernews_api
content_file: hackernews_api-yet-another-way-to-invoke-functions-without-parent
fetched_at: '2026-10-16T21:55:54.396710'
original_url: https://blog.ikaes.de/yet-another-way-to-invoke-functions-without-parentheses/
author: aragonite
date: '2026-10-13'
description: Yet another way to invoke functions without parentheses
tags:
- hackernews
- trending
---

# yet another way to invoke functions without parenthesesi found yet another way to invoke arbitrary functions in javascript without using parenthesesthis payload works by overwriting theprepareStackTracefunction of theErrorobject to generate arbitrary functions. it is usually usedto format stack tracesand is invoked when the attributestackof an error is accessed.the parameters of this function are the error and "a structured representation of the stack" , which is just an array of the code positions. it has the same function signature theFunction constructorwhich is used to generate javascript functions, as long as the second argument is valid javascript code.if we try to invoke the function which was generated using this method, we get a syntax error. it is to be expected, because a stack trace is not a valid javascript code, but anArrayof code positionsin order to make the payload work, we need to control the output of theArray.prototype.toString()function such that it returns our desired javascript payload. this can be done in two waysfirst we can simply overwrite it with a constant function which returns the payloador we can use prototype pollution to sneak our payload into another function, and then overwrite theArrayprototype. i found that we can stay in theErrorrealm and use itstoStringfunction which can be manipulated by polluting theObject.prototype.messagevariable. i am sure there are more ways to achieve this.now if we put everything together - the function generation using theprepareStackTracefunction and way to convert arrays into arbitrary strings, we can generate arbitrary javascript functionslast thing we have to do is to invoke our new function. luckily there aremany ways to do soand i chose thevalueOftrick. it works by overwriting the defaultvalueOffunction of our object and then invoking it as a primitive. alternatively, we can usetoStringand then concatenate the object with a string.the final payload is as follows. feel free to try it out in the browser console.Object.prototype.message='alert\x281337\x29';Array.prototype.toString=Error.prototype.toString;Error.prepareStackTrace = Function;const x = new Error;x.valueOf=x.stack;+x;