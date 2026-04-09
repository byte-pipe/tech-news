---
title: Quickshell
url: https://quickshell.org/
site_name: hackernews
fetched_at: '2025-08-10T16:06:42.730314'
original_url: https://quickshell.org/
author: abhinavk
date: '2025-08-10'
description: A fully user customizable desktop shell
---

Quickshell 0.2.0 has been released! | 2025-07-26






# Quickshell





## building blocks for your desktop























Configuration bysoramane(install)









Configuration byend_4(install)









Configuration byoutfoxxed(source code)









Configuration bypfajandbdebiase









Configuration byflicko(source code)









Configuration byvaxry









Quickshell is a toolkit for building status bars, widgets, lockscreens,
 and other desktop components using QtQuick. It can be used alongside your
 wayland compositor or window manager to build a complete desktop environment.More information






### Install





### Documentation






* ### See your changes in real timeQuickshell loads changes as soon as they're saved, letting you iterate as fast as you can type.
* ### Easy to use languageQuickshell is configured in QML, a simple language designed for creating flexible user interfaces.
 It also has LSP support.// a standard desktop windowFloatingWindow{Timer{// assign an id to the object, which can be// used to reference itid:timerpropertyboolinvert:false// a custom property// change the value of invert every half secondrunning:true;repeat:trueinterval:500// msonTriggered:timer.invert=!timer.invert}// change the window's color when timer.invert changescolor:timer.invert?"purple":"green"}// a standard desktop windowFloatingWindow{Timer{// assign an id to the// object, which can be// used to reference itid:timer// a custom propertypropertyboolinvert:false// change the value of invert// every half secondrunning:true;repeat:trueinterval:500// msonTriggered: {timer.invert=!timer.invert}}// change the window's color// when timer.invert changescolor:timer.invert? "purple": "green"}
* ### Extensive integrationsQuickshell comes with a large set of integrations, with new ones arriving all the time.
