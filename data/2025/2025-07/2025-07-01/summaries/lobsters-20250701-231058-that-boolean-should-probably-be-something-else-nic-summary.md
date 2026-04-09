---
title: That boolean should probably be something else | nicole@web
url: https://ntietz.com/blog/that-boolean-should-probably-be-something-else/
date: 2025-07-01
site: lobsters
model: llama3.2:1b
summarized_at: 2025-07-01T23:10:58.186339
---

# That boolean should probably be something else | nicole@web

**Analysis**

The article discusses the potential benefits of using alternative types instead of Boolean in systems where a "true" or "false" value is not necessary. The author argues that Boolean can be overused and leads to lost data.

The article highlights three possible alternatives:

1. **Datetimes**: Representing temporal events (e.g., an email confirmation) as nullable columns rather than Booleans.
2. **Enums**: Using enumerations (enum classes) in place of basic Booleans, which improve design time and reduce bugs.
3. **TimeSeries data**: Storing timestamps instead of Boolean values for event-based systems.

**Market Indicators**

* User adoption: The author notes that these alternative types are not yet widely adopted, but there is potential for growth.
* Revenue mentions: There is no specific mention of revenue in the article, but we can assume it's essential to analyze user behavior and sales patterns when evaluating a successful solo developer business.

**Technical Feasibility**

* Complexity: These solutions require additional design and implementation efforts, including refactoring code to accommodate alternative types.
* Required skills: The author mentions that these solutions typically require knowledge of data storage techniques (e.g.,Enums) or temporal logic (e.g., Datetimes).
* Time investment: Implementing alternative types will likely require more time than using Booleans.

**Business Viability Signals**

* User willingness to pay: The article does not provide direct evidence for a profitable business.
* Existing competition: There is no indication of existing Booleans-based systems competing against solo developers with novel alternatives.
* Distribution channels: The author notes that there is no specific mention of how these alternative types would be distributed (e.g., GitHub, community forums).

**Actionable Insights**

1. **Refactor your code**: Even if the solution isn't immediately obvious, consider refactoring your existing Booleans-based systems to take advantage of alternative types.
2. **Choose enum classes carefully**: When creating enums, choose names that clearly indicate their purpose and use them consistently throughout your application.
3. **Invest in data storage techniques**: Learn about time-series data storage solutions (e.g., datetime) if you plan to work with temporal events or event-based systems.
4. **Evaluate user feedback**: As solo developers selling on platforms like GitHub, keep an eye out for issues that might be solved more effectively by using alternative types.

Overall, this solo developer business can benefit from applying these insights by evaluating the need and feasibility of adopting alternative types like Datetimes, Enums, or TimeSeries data.
