---
title: 'GNOME Calendar: A New Era of Accessibility Achieved in 90 Days | TheEvilSkeleton'
url: https://tesk.page/2025/07/25/gnome-calendar-a-new-era-of-accessibility-achieved-in-90-days/
site_name: lobsters
fetched_at: '2025-07-26T23:06:42.682227'
original_url: https://tesk.page/2025/07/25/gnome-calendar-a-new-era-of-accessibility-achieved-in-90-days/
author: TheEvilSkeleton
date: '2025-07-26'
published_date: '2025-07-25T00:00:00+00:00'
description: 'There is no calendaring app that I love more than GNOME Calendar. The design is slick, it works extremely well, it is touchpad friendly, and best of all, the community around it is just full of wonderful developers, designers, and contributors worth collaborating with, especially with the recent community growth and engagement over the past few years. Georges Stavracas and Jeff Fortin Tam are some of the best maintainers I have ever worked with. I cannot express how thankful I am of Jeff’s underappreciated superhuman capabilities to voluntarily coordinate huge initiatives and issue trackers. One of Jeff’s many initiatives is gnome-calendar#1036: the accessibility initiative, which is a big and detailed list of issues related to accessibility. In my opinion, GNOME Calendar’s biggest problem was the lack of accessibility support, which made the app completely unusable for people exclusively using a keyboard, or people relying on assistive technologies. This article will explain
  in details about the fundamental issues that held back accessibility in GNOME Calendar since the very beginning of its existence (12 years at a minimum), the progress we have made with accessibility as well as our thought process in achieving it, and the now and future of accessibility in GNOME Calendar.'
tags: a11y
---

Disclaimer(s)


This article is highly technical and goes into the inner workings of accessibility in GTK. In hopes to make it as clear as possible and avoid ambiguity, you may notice a lot of redundancy, such as reusing nouns instead of using pronouns. This may set the article’s tone as emotionless and robotic.






Table of Contents





Note


Please consider supporting my effort in making GNOME apps accessible for everybody. Thanks!LiberapayKo-fiGitHub Sponsors





## Introduction§



There is no calendaring app that I love more than GNOME Calendar. The design is slick, it works extremely well, it is touchpad friendly, and best of all, the community around it is just full of wonderful developers, designers, and contributors worth collaborating with, especially with the recent community growth and engagement over the past few years.Georges StavracasandJeff Fortin Tamare some of the best maintainers I have ever worked with. I cannot express how thankful I am of Jeff’s underappreciated superhuman capabilities to voluntarily coordinate huge initiatives and issue trackers.



One of Jeff’s many initiatives isgnome-calendar#1036:the accessibility initiative, which is a big and detailed list of issues related to accessibility. In my opinion, GNOME Calendar’s biggest problem was the lack of accessibility support, which made the app completely unusable for people exclusively using a keyboard, or people relying on assistive technologies.



This article will explain in details about the fundamental issues that held back accessibility in GNOME Calendar since the very beginning of its existence (12 years at a minimum), the progress we have made with accessibility as well as our thought process in achieving it, and the now and future of accessibility in GNOME Calendar.



## Calendaring Complications§



On a desktop or tablet form factor, GNOME Calendar has a month view and a week view, both of which are a grid comprising of cells representing a time frame. In the month view, each row is a week, and each cell is a day. In the week view, the time frame within cells varies on the zooming level.



There are mainly two reasons GNOME Calendar was inaccessible: firstly, the accessibility tree does not cover the logically and structurally complicated workflow and design that is a typical calendaring app; and secondly, the significant negative implications of accessibility due to reducing as much overhead as possible.



### Accessibility Trees Are Insufficient for Calendaring Apps§



Theaccessibility treeis rendered insufficient for calendaring apps, mainly because events are extremely versatile. Tailoring the entire interface and experience around that versatility pushes us to explore alternate and custom structures.



Events are highly flexible, because they are time-based. An event can last a couple of minutes, but it can as well last for hours, days, weeks, or even months. It can start in the middle of a day and end on the upcoming day; it can start by the end of a week and end at the beginning of the upcoming week. Essentially, events are limitless.



Since events can last more than a day, cell widgets cannot hold any event widget, because otherwise event widgets would not be capable of spanning across cells. As such, event widgets are overlaid on top of cell widgets and positioned based on the coordinates, width, and height of each widget. However, because cell widgets cannot hold a meaningful link with event widgets, there is no way to easily ensure there is a link between an event widget and a cell widget.



As a consequence, the visual representation of GNOME Calendar is fundamentally incompatible with accessibility trees. GNOME Calendar’s month and week views arevisually2.5 dimensional: A gridlayout by itself is structurallytwo-dimensional, but overlaying event widgets that is capable of spanning across cells adds an additional layer. Conversely, accessibility trees are fundamentallytwo-dimensional, so GNOME Calendar’s visual representation cannot be sufficiently adapted into atwo-dimensionallogical tree.



In summary, accessibility trees are insufficient for calendaring apps, because the versatility and high requirements of events prevents us from linking cell widgets with event widgets, so event widgets are instead overlaid on top, consequently making the visual representation2.5 dimensional; however,the additional layer makes it fundamentally impossible to adapt to atwo-dimensionalaccessibility tree.



### Negative Implications of Accessibility due to Maximizing Performance§



Unlike the majority of apps, GNOME Calendar’s layout and widgetry consist of custom widgets and complex calculations according to several factors, such as:


* the size of the window;
* the height and width of each cell widget to figure out if one or more event widgets can perceptibly fit inside a cell;
* the position of each event widget to figure out where to position the event widget, and where to reposition all the event widgets around it if necessary;
* what went wrong in my life to work on a calendaring app written in C.


Due to these complex calculations, along with the fact that it is also possible to have tens, hundreds, or even thousands of events in a calendar app, calendar apps always rely on maximizing performance as much as possible, while being at the mercy of the framework or toolkit.



One way to minimize that problem is by creating custom widgets that are minimal and only fulfill the purpose we absolutely need. However, this comes at the cost of needing to reimplement most functionality, including most, if not all accessibility features and semantics, such as keyboard focus, which severely impacted accessibility in GNOME Calendar.



While GTK’s widgets are great for general purpose use-cases and do not have any performance impact with limited instances of them, performance starts to deteriorate on weaker systems when there are hundreds, if not thousands of instances in the view, because they contain a lot of functionality that event widgets may not need.



In the case of theGtkButtonwidget, it has a custommultiplexer, it applies different styles for differentchild types, it implements theGtkActionableinterface for custom actions, and more technical characteristics. Other functionality-based widgets will have more capabilities that might impact performance with hundreds of instances.



To summarize, GNOME Calendar reduces overhead by creating minimal custom widgets that fulfill a specific purpose. This unfortunately severely impacted accessibility throughout the app and made it unusable with a keyboard, as some core functionalities, accessibility features and semantics were never (re)implemented.



## Improving the Existing Experience§



Despite being inaccessible as an app altogether, not every aspect was inaccessible in GNOME Calendar. Most areas throughout the app worked with a keyboard and/or assistive technologies, but they needed some changes to improve the experience. For this reason, this section is reserved specifically for mentioning the aspects that underwent a lot of improvements.



### Improving Focus Rings§



The first major step was to improve the focus ring situation throughout GNOME Calendar. Since the majority of widgets are custom widgets, many of them require to manually apply focus rings.!563addresses that bydeclaring custom CSS properties, to use as a base for focus rings.!399tweaks the style of the reminders popover in the event editor dialog, with theaddition of a focus ring.



We changed the behavior of the event notes box under the “Notes” section in the event editor dialog. Every time the user focuses on the event notes box, the focus ring appears and outlines the entire box until the user leaves focus. This was accomplished bysubclassing AdwPreferencesRowto inherit its style, thenapplying the.focusedclasswhenever the user focuses on the notes.



### Improving the Calendar Grid§



The calendar grid on the sidebar suffered from several issues when it came to keyboard navigation, namely:


* pressing↹would focus the next cell in the grid up until the last cell;
* when out of bounds, there would be no auditory feedback;
* on the last row, pressing↓would focus a blank element; and
* pressing→in left-to-right languages, or←in right-to-left languages, on the last column would move focus to a completely different widget.


While the calendar grid can be interacted with a keyboard, the keyboard experience was far from desired.!608addresses these issues by overriding theGtk.Widget.focus ()virtual method. Pressing↹orShift+↹skips the entire grid, and the grid iswrappedto allow focusing between the first and last columns with←and→, while notifying the user when out of bounds.



### Improving the Calendar List Box§




Note


The calendar list box holds a list of available calendars, all of which can be displayed or hidden from the week view and month view. Each row is aGtkListBoxRowthat holds aGtkCheckButton.





The calendar list box had several problems in regards to keyboard navigation and the information each row provided to assistive technologies.



The user was required to press↹a second time to get to the next row in the list. To elaborate: pressing↹once focused the row; pressing it another time moved focus to the check button within the row (bad); and finally pressing the third time focused the next row.



Row widgets had no actual purpose besides toggling the check button upon activation. Similarly, the only use for a check button widget inside each row was to display the “check mark” icon if the calendar was displayed. This meant that the check button widget held all the desired semantics, such as the “checkbox” role and the “checked” state; but worst of all, it was getting focus. Essentially, the check button widget was handling responsibilities that should have been handled by the row.



Both inconveniences were addressed by!588. The check button widget was replaced with a check mark icon usingGtkImage, a widget that does not grab focus. The accessible role of the row widget was changed to “checkbox”, and the code was adapted to handle the “checked” state.



## Implementing Accessibility Functionality§



Accessibility is often absolute: there is no ‘in-between’ state; either the usercanaccess functionality, or they cannot, which can potentially make the app completely unusable. This section goes in depth with the widgets that were not only entirely inaccessible but also rendered GNOME Calendar completely unusable with a keyboard and assistive technology.



### Making the Event Widget Accessible§




Note


GcalEventWidget, the name of the event widget within GNOME Calendar, is a colored rectangular toggle button containing the summary of an event.Activating it displays a popover that displays additional detail for that event.GcalEventWidget subclassesGtkWidget.





The biggest problem in GNOME Calendar, which also made it completely impossible to use the app with a keyboard, was the lack of a way to focus and activate event widgets with a keyboard. Essentially, one would be able to create events, but there would be no way to access them in GNOME Calendar.



Quite literally, this entire saga began all thanks to a dream I had, which was to make GcalEventWidget subclassGtkButtoninstead ofGtkWidgetdirectly. The thought process was:GtkButton already implements focus and activation with a keyboard, so inheriting it should therefore inherit focus and activation behavior.



In merge request!559, the initialimplementationindeed subclassed GtkButton. However, that implementation did not go through, due to the reason outlined in§ NegativeImplications of Accessibility due to Maximizing Performance.



Despite that, the initial implementation instead significantly helped us figure outexactlywhat were missing with GcalEventWidget: specifically, settingGtk.Widget:receives-defaultandGtk.Widget:focusableproperties to “True”.Gtk.Widget:receives-defaultmakes it so the widget can be activated how ever desired, andGtk.Widget:focusableallows it to become focusable with a keyboard. So, instead of subclassing GtkButton, we insteadreimplemented GtkButton’s functionalityin order to maintain performance.



While preliminary support for keyboard navigation was added into GcalEventWidget, accessible semantics for assistive technologies like screen readers were severely lacking. This was addressed by!587, which sets therole to “toggle-button”, to convey that GcalEventWidget is a toggle button. The merge request alsoindicates that the widget has a popupfor the event popover, and has the means toupdate the “pressed” stateof the widget.



In summary, we first made GcalEventWidget accessible with a keyboard by reimplementing some of GtkButton’s functionality. Then, we later added the means to appropriately convey information to assistive technologies. This was the worst offender, and was the primary reason why GNOME Calendar was unusable with a keyboard, but we finally managed to solve it!



### Making the Month and Year Spin Buttons Accessible§




Note


GcalMultiChoiceis the name of the customspin buttonwidget used for displaying and cycling through months and/or years.It comprises of a “decrement” button to the start, a flat toggle button in the middle that contains a label that displays the value, and an “increment” button to the end. Only the button in the middle can gain keyboard focus throughout GcalMultiChoice.In some circumstances, GcalMultiChoice can display a popover for increased granularity.





GcalMultiChoice was not interactable with a keyboard, because:


1. it did not react to↑and↓keys; and
2. the “decrement” and “increment” buttons were not focusable.


For a spin button widget, the “decrement” and “increment” buttons should generally remain unfocusable, because↑and↓keys already accomplish that behavior. Furthermore,GtkSpinButton’s “increment” (+) and “decrement” (-) buttons are not focusable either, and theDate Picker Spin Button Exampleby the ARIA Authoring Practices Guide (APG) avoids that functionality as well.



However, since GcalMultiChoice did not react to↑and↓keys, having the “decrement” and “increment” buttons be focusable would have been a somewhat acceptable workaround. Unfortunately, since those buttons were not focusable, and↑and↓keys were not supported, it was impossible to increment or decrement values in GcalMultiChoice with a keyboard without resorting to workarounds.



Additionally, GcalMultiChoice lacked the semantics to communicate with assistive technologies. So, for example, a screen reader would never say anything meaningful.



All of the above problems remained problems until merge request!603. For starters, it implementsGtkAccessibleandGtkAccessibleRange, and thenimplements keyboard navigation.



#### Implementing GtkAccessible and GtkAccessibleRange§



The merge request implements the GtkAccessible interface toretrieve information from the flat toggle button.



Fundamentally, since the toggle button was the only widget capable of gaining keyboard focus throughout GcalMultiChoice, this caused two distinct problems.



The first issue was that assistive technologies only retrieved semantic information from the flat toggle button, such as the type of widget (accessible role), its label, and its description. However, the toggle button was semanticallyjusta toggle button; since it contained semantics and provided information to assistive technologies, the information it provided was actually misleading, because it only provided information as a toggle button, not a spin button!



So, the solution to this is to strip the semantics from the flat toggle button. Setting its accessible role to “none” makes assistive technologies ignore its information. Then, setting the accessible role of thetop-level (GcalMultiChoice)to “spin-button” gives semantic meaning to assistive technologies, which allows the widget to appropriately convey these information, when focused.



This led to the second issue: Assistive technologies only retrieved information from the flat toggle button, not from the top-level. Generally, assistive technologies retrieve information from the focused widget. Since the toggle button was the only widget capable of gaining focus, it was also the only widget providing information to them; however, since its semantics were stripped, it had no information to share, and thus assistive technologies would retrieve absolutely nothing.



The solution to this is to override theGtk.Accessible.get_platform_state ()virtual method, which allows us to bridge communication between thestatesof child widgets and the top-level widget. In this case, both GcalMultiChoice and the flat toggle button share the state—if the flat toggle button is focused, then GcalMultiChoice is considered focused; and since GcalMultiChoice is focused, assistive technologies can then retrieve its information and state.



The last issue that needed to be addressed was that GcalMultiChoice was still not providing any of the values to assistive technologies. The solution to this is straightforward:implementing the GtkAccessibleRange interface, which makes it necessary to set values for the following accessible properties: “value-max”, “value-min”, “value-now”, and “value-text”.



After all this effort, GcalMultiChoice now provides correct semantics to assistive technologies. It appropriately reports its role, the current textual value, and whether it contains a popover.



To summarize:


* The flat toggle button was the only widget conveying information to assistive technologies, as it was the only widget capable of gaining focus and providing semantic information. To solve this, its semantics were stripped away.
* The top-level, being GcalMultiChoice, was assigned the “spin-button” role to provide semantics; however, it was still incapable of providing information to assistive technologies, because it was never getting focused. To solve this, the state of the toggle button, including the focused state, carried over to the top-level to allow assistive technologies to retrieve information from the top-level.
* GcalMultiChoice still did not provide its values to assistive technologies. This is solved by implementing the GtkAccessibleRange interface.


#### ProvidingTop-LevelSemantics to a Child Widget As Opposed to theTop-LevelWidget Is Discouraged§



As you read through the previous section, you may have asked yourself: “Why go through all of those obstacles and complications when you could have justre-assignedthe flat toggle button as “spin-button” and not worry about the top-level’s role and focus state?”



Semantics should be provided by the top-level, because they are represented by the top-level. What makes GcalMultiChoice a spin button is notjustthe flat toggle button, but it is the combination of all the child widgets/objects, event handlers (touch, key presses, and other inputs), accessibility attributes (role, states, relationships), widget properties, signals, and other characteristics. As such, we want to maintain that consistency for practically everything, including the state. The only exception to this is widgets whose sole purpose is to contain one or more elements, such asGtkBox.



This is especially important for when we want it to communicate with other widgets and APIs, such as theGtk.Widget::state-flags-changedsignal, theGtk.Widget.is_focus ()method, and other APIs where it is necessary to have the top-level represent data accurately and behave predictably. In the case of GcalMultiChoice, weset accessible labelsat the top-level. If we were tore-assignthe flat toggle button’s role as “spin-button”, and set the accessible label to the top-level, assistive technologies would only retrieve information from the toggle button while ignoring the labels defined at the top-level.



For the record, GtkSpinButton alsooverridesGtk.Accessible.get_platform_state ():


1
2
3
4
5
6
7
8
9
10
11
12
13
14

static

gboolean

gtk_spin_button_accessible_get_platform_state

(
GtkAccessible

*
self
,


GtkAccessiblePlatformState

state
)

{


return

gtk_editable_delegate_get_accessible_platform_state

(
GTK_EDITABLE

(
self
),

state
);

}

static

void

gtk_spin_button_accessible_init

(
GtkAccessibleInterface

*
iface
)

{


…


iface
->
get_platform_state

=

gtk_spin_button_accessible_get_platform_state
;

}



To be fair, assigning the “spin-button” role to the flat toggle button is unlikely to cause major issues, especially for an app.Re-assigningthe flat toggle button was my first instinct. Theinitial implementationdid just that as well. I was completely unaware of theGtk.Accessible.get_platform_state ()virtual method before finalizing the merge request, so I initially thought that was the correct way to do. Even if the toggle button had the “spin-button” role instead of the top-level, it would not have stopped us from implementing workarounds, such as a getter method that retrieves the flat toggle button that we can then use to manipulate it.



In summary, we want to provide semantics at the top-level, because they are structurally part of it. This comes with the benefit of making the widget easier to work with, because APIs can directly communicate with it, instead of resorting to workarounds.



## The Now and Future of Accessibility in GNOME Calendar§



All these accessibility improvements will be available on GNOME 49, but you can download and install the pre-release on the “Nightly GNOME Apps”DLCFlatpak remote onnightly.gnome.org.



In the foreseeable future, I want to continue working on!564, to make the month view itself accessible with a keyboard, as seen in the following:





A screen recording demoing keyboard navigation within the month view. Focus rings appear and disappear as the user moves focus between cells. Going out of bounds in the vertical axis scrolls the view to the direction, and going out of bounds in the horizontal axis moves focus to the logical sibling.




However, it is already adding 640 lines of code, and I can only see it increasing overtime. We also want to make cells in the week view accessible, but this will also be a monstrous merge request, just like the above merge request.



Most importantly, we want (and need) to collaborate and connect with people who rely on assistive technologies to use their computer, especially when everybody working on GNOME Calendar does not rely on assistive technologies themselves.



## Conclusion§



I am overwhelmingly satisfied of the progress we have made with accessibility on GNOME Calendar in six months. Just a year ago, if I was asked about what needs to be done to incorporate accessibility features in GNOME Calendar, I would have shamefully said “dude, I don’t know where to evenbegin”; but as of today, we somehow managed to turn GNOME Calendar into an actual, usable calendaring app for people who rely on assistive technologies and/or a keyboard.



Since this is still Disability Pride Month, and GNOME 49 is not out yet, I encourage you to get the alpha release of GNOME Calendar on the “Nightly GNOME Apps” Flatpak remote atnightly.gnome.org. The alpha release is in a state wherethe gays with disabilities can organize and do crimesusing GNOME Calendar 😎 /j
