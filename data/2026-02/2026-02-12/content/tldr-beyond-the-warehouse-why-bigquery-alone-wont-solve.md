---
title: 'Beyond the Warehouse: Why BigQuery Alone Won’t Solve Your Data Problems - InfoQ'
url: https://www.infoq.com/presentations/bigquery-data-challenges/
site_name: tldr
content_file: tldr-beyond-the-warehouse-why-bigquery-alone-wont-solve
fetched_at: '2026-02-12T11:20:24.260288'
original_url: https://www.infoq.com/presentations/bigquery-data-challenges/
date: '2026-02-12'
description: Sarah Usher explains why relying solely on a data warehouse fails at scale. She shares a 3-layer data lifecycle (Raw, Curated, Use Case) to help engineering leaders build flexible, decoupled systems.
tags:
- tldr
---

InfoQ HomepagePresentationsBeyond the Warehouse: Why BigQuery Alone Won’t Solve Your Data Problems

 AI, ML & Data Engineering


QCon London (March 16-19, 2026): Learn proven architectural practices to scale your systems faster.

# Beyond the Warehouse: Why BigQuery Alone Won’t Solve Your Data Problems

View Presentation

* Vertical
* Horizontal
* Full

Speed:

* 1x
* 1.25x
* 1.5x
* 2x

Download

* Slides

44:51

## Summary

Sarah Usher discusses the architectural "breaking point" where warehouses like BigQuery struggle with latency and cost. She explains the necessity of a conceptual data lifecycle (Raw, Curated, Use Case) to regain control over lineage and innovation. She shares practical strategies to design a single source of truth that empowers both ML teams and analytics without bottlenecking scale.

## Bio

Sarah Usher is a software engineer specializing in data engineering, backend systems, and scalable system design. She has extensive experience across industries such as banking, insurance, developer security, and digital advertising. She has won awards for her mentorship and leadership.

## About the conference

Software is changing the world. QCon London empowers software development by facilitating the spread of knowledge and innovation in the developer community. A practitioner-driven conference, QCon is designed for technical team leads, architects, engineering directors, and project managers who influence innovation in their teams.

### INFOQ EVENTS

* March 5th, 2026, 11 AM EST#### Orchestrating Production-Ready AI Workflows with Apache AirflowPresented by: Tamara Fingerlin - Senior Developer Advocate at Astronomer, and Pranav Bahadur - Product Marketing Manager at Astronomer

## Transcript

Sarah Usher: I wanted to know, who of you considers yourselves not to be a data person? You are data people now. Some of my loves are really talking about big data and big data processing. I've been very lucky to do work like that. In the last few years, I've mostly ended up working at scale-ups and start-ups, and they have scale problems, but they're not usually about processing huge amounts of data. They're slightly different. A lot of them have bought into an idea that they can use one tool that does everything, and that one tool is the warehouse. I've picked on BigQuery today. For a certain period of time, it actually does work really well until it doesn't. We see the warehouse start to struggle, slow down, can no longer take in as many data sources as it used to without keeping the same latency. The data can become disorganized, difficult to find. There's a lot of confusion around what tables am I supposed to use.

If I can't get the data from the warehouse, where should I be going? People ask questions, where can I find this data? Very common. Struggle to innovate. A very simple example from my previous job is we had some product engineers want to use data from the warehouse, and the query that they wanted was very simple, SELECT * from some table. That query ran for about five minutes, which in analytics world is bearable, but in operational world is a no-go. They literally couldn't use the warehouse to do a simple product feature. It's expensive. These warehouses are incredibly powerful, and we're actually really lucky to be able to work with these technologies, but they scale by adding more machines, and those machines are not free. You often have to add very beefy machines to scale your processing. I've had to have a lot of these conversations with customers and clients, and it makes me very sad to tell them that they can't carry on the way that they have.

Who am I? My name is Sarah. I have worked across full stack and mobile, but I found my love in data. I mostly work on data platforms or data systems or data architecture. I also do a fair amount of system design consulting, mostly for free, which is not great for my bank balance, but has been really great for my exposure across how different companies do different types of architectures. At the moment, I'm actually on a break from building systems, and I'm currently building people. I'm very involved in the Women in Tech community. I run Tech Risers Women, which is focused on helping women who are already in tech stay in tech and move up the IC career track. I am the data engineering lead at Women in Data. I'm somewhat involved in Ladies of Code. I've been with them for a number of years, and I mostly run socials because that's fun. I do a fair amount of mentorship. It is my secret career weapon. It is a really great way to learn new things and reinforce what you already know. If you're not doing that, I highly suggest you give it a try.

## Use Case - Data for ML

We're going to walk through a use case today. Maybe you've had something like this come to your door. This is very common at mine. I've got a customer that says, I want to use my data for machine learning. I've gathered all this data. I've lovingly curated it into this beautiful warehouse, and I want to build some machine learning. I've already started, which is the fun part. They never call you in, they want to start. They've already started. What have we got? We have a customer churn service that is using some machine learning. This team uses some customer account data, and they've gone to the warehouse for the rest of their data. They couldn't just get everything through the warehouse. Why? Because it's slow. It was not fast enough. They want that customer account data as it comes in. They've bypassed the warehouse for that one particular dataset. They've built their own custom cleaning and machine learning pipeline. They output an S3 file into a bucket, and that serves as the model that goes into the churn service. What's wrong with this? A couple things I'm not a fan of.

One is, we're now making additional API calls to the service, which is bearable. We know how to scale services, so we can live. We are cleaning the data at least twice. Are we cleaning it up the same? I don't know. There is no standard for how to use S3 at this company. They're just coming up with something decent. Hopefully it has some dates and some entity names in there. It's not standard. This is running, and it's ok. You might say, Sarah, you're really nitpicking at this. We can live with this. Then my favorite thing happens. It gets repeated. Team number two comes along and says, "That's really cool. We also want to use the customer's data. We also want to build a machine learning service". There's now a pathway to do that. Gold, not gold. Doesn't matter. It's there. We copy and paste. Now we have almost double the amount of calls going to the customer account service. We have additional cleanup. Is it the same? I don't know. They're putting stuff in S3. Is it the same prefixes? I don't know. This is the core of the problem, I think.

These symptoms are usually part of a bigger problem. I want to zoom out and have a look at the rest of their architecture. I've chosen some tools here to color the picture. If you have similar, maybe change them for something you use in your mind's eye. We have services. We have some message queues. We've got some external data coming in through Fivetran. All the data goes into BigQuery, which is our chosen warehouse for this example. We do some analysis in Looker Studio. We are sending some data out in Fivetran. I refuse to say reverse ETL. We have the pipeline we just talked about. What is the problem here? It's happening at the first graph. We've already had to bypass our lovingly, beautifully curated warehouse to do a new use case in the system. We are asking a lot of this tool. They're very powerful tools, but they don't actually have to do absolutely everything.

## Data Lineage and Source of Truth

How do we fix this for this company? Before we look at solutions, we all need to be on the same page about a couple of things. We're going to talk about these. Then we're going to look at how we shift the design for this company. Lineage. Data lineage is the path that the data takes from origin, everywhere that it gets used all the way to effectively an end node where it's no longer queried. Lineage has always existed since we've been processing data, except that it's cool now.

If you pull up a new data catalog tool or observability tool or data reliability tool, one of the features it's going to give you is lineage because we figured out that being able to see where our data goes to is actually useful. Source of truth is my favorite. What does source of truth mean to you? To differentiate at least two types of sources, there's usually an original source, so the place that makes the data. I want you to think of this as something that you generally don't control. It might be an internal service, but that service is within the boundary of a different product team. It's not something you would necessarily change. That's original source. Single source of truth is something that you can control. Maybe you've taken a copy, maybe you clean it up, and you say that this is the source that everyone should use.

Most of the time when I'm talking about single source of truth, or source of truth, I mean the second one. They can, of course, be the same, which we will actually see later. Along with source of truth, when we say that word, a lot of people think about it as a system. The warehouse is the source of truth. The data lake is the source of truth. Why a system? Does it have to be the same system for every entity? I don't really know why we think about it that way. Is it just a nice way to draw a diagram? Is it easier to think about it that way when you're a smaller team? Sure, that's fair. It's a question, because when we define source of truth, it talks about authoritative and reliable data source, and provides the most valid and accurate information. It doesn't say system, and it doesn't say for all your data. This gives us some flexibility.

I look at source of truth differently. I look at source of truth as the place in which the lineage starts to split off. The reason I look at it this way is because I have been the engineer/victim that have had to go and figure out why a custom frontend doesn't match a Looker report, and I've had to go and dig and find out all the different places it's been changed until I find the common node effectively along the lineage graph, which has really made me see it like this.

## Data Lifecycle

I also like to suggest the idea that we can design our source of truth. We don't just have to put up with where it's landed in the lineage. We can control our lineage. We can design source of truth. I like to place it at the curated stage of the data lifecycle, which is white Sarah. This is the data lifecycle. You may know it by a different name. This is just what I call it, and where I've seen it. It is not my own creation. It is, in fact, a divergence of the medallion model that I've seen other companies use. The medallion model was a really simplistic yet genius idea that we should be organizing the data lake into categories of quality. Pretty simple idea: bronze, silver, and gold. Is this sounding familiar? That's great, but the reason that this has taken a different path is two reasons. One is the medallion model is sold very much within Databricks as a way to implement your lakehouse or your data lake, and they also tend to infer that your source of truth should be at layer 3, golden source. This one is slightly different. This is a conceptual model with which you can do any implementation, and ideally, your source of truth should be at layer 2.

In fact, the last place you want your source of truth is at layer 3. Sometimes it's acceptable to do it at layer 1. Quickly, just to go through these. Raw, pretty common name. Most people have solidified on raw data. It's unprocessed data stored as-is, or as original as possible, and as immutable. You've captured what you've captured, you don't want that to change, and as raw as possible. Sometimes changes are acceptable. I've had to work with data that was written with a custom serializer that I then had to custom deserialize. I don't really want to store that. I would take CSV over that any day. There are exceptions to every rule. Curated, you might see it called transformed, processed, cleaned. I like this word in particular. Usually what you're doing here, you're deduping, you are normalizing.

If you've got some IoT data coming in, maybe it's coming, some of the sensors in Fahrenheit, some of the sensors in Celsius. You want to normalize into Celsius. It usually still matches source. You don't change the shape a lot. You keep the same shape that you had, you just clean it up a little bit. Use case is then highly refined data that is for a specific use case. You'll take a copy of the curated data, but if that was in, say, Avro, you might then want to change it to Parquet for use in analytics. You may want to output it in an API for use in operational systems. It's going to look different depending on its use case. There's a little bit of a Backend for Frontend mentality here. It's very similar. Making the data suit the need.

What does this look like in reality? Just so you can see these concepts applied. You can use the data lifecycle in a warehouse. You might have a layer that's pretty raw. Then you'll curate your different entities, and you then will develop different tables for different use cases. If you're using multiple analytics systems, you might have tables that are useful for Looker. You might have tables that are useful for Tableau because they're slightly different. That sort of thing. Maybe you are more familiar with something like Athena. You do schema and read. Here we have an API that is dumping out raw data into an S3 bucket. We're then building our curation in Athena.

Then you've got some options for your third layer. You can do a physical output back into S3 for curated and use those for your use cases, or you can just build a query on a query and use that for your use case. A very trivialized mesh example where we just don't have a central data platform. Our product team is keeping raw data. I mean really raw. I don't mean migrations that then change things a little bit. I mean super raw. Then they're providing a curated view over the data which is then available through an API or through a message queue for different use cases. The use case here is our warehouse.

That is the data lifecycle. Again, this is a conceptual model with multiple different implementations. My question to you is, can you go back to your business and have a look and identify these stages? Because you might be surprised. A lot of people actually end up dropping the curated stage even though they do curation. They do all this work to clean the data and then they don't make it available anywhere else except for a particular use case. This is where we start to get reprocessing raw and we have people actually using use case data, and then combining lots of different tables and reprocessing them. Yes, I've seen some things. Bonus, most important, please store your raw data and store it in original state as possible.

As I mentioned, if it comes in CSV, then store it in CSV. If it comes in JSON, store it like that. If it comes with weird characters, store it like that, and put it in something that isn't going to stop you. I usually just go for files. They're straightforward. I tried to insert some weather data into BigQuery once and it said no. I said, excuse me. It didn't say anything back because it's not alive. I really just didn't appreciate that. It then made me think, now I don't want to use BigQuery. I want to use Snowflake instead, which I can do because I've stored the raw file and I can now replay through whatever tool I like.

## Shift the Design

Lineage. We can control lineage. It doesn't just have to happen. The data lifecycle should appear in your architecture. The source of truth is something that we can place and we can define where it is. We want to store our raw data. Back to our customer. How do we help them? This is the original picture, but I have removed the compute element and these are data flows. Hopefully the separation of storage and compute is somewhat familiar. This is just to make the picture a little easier to follow, really. As a reminder, we had everything funneling through the data warehouse. This was a problem for our churn team and they couldn't use the warehouse. This is my suggestion, is to start storing raw data. That's place number one.

As I say, my particular favorite is just to store it in S3 in files. Then number two is to then curate this data in a way that is much quicker than my warehouse is. I've worked on some really optimized warehouses that can be phenomenal. There's always one use case, and especially these days with data needing to move faster and faster, that they just really can't cater for or they weren't designed for that. These are just some examples, but I'm sure you've got more. There are some vendors with really cool tools out there. Just to give you an idea, you could use something like a distributed batch system like Spark, or maybe you want to go full streaming. That's ok, as long as you make your curated data available. My particular choice in this instance is to put that curated data in Avro in an S3 bucket.

Then my warehouse no longer has to be my data pipeline. I don't have to funnel through my warehouse. It can then sit in the use case layer. This saves some processing because it's no longer having to deal with raw data. It's no longer having to deal with the curation, and storing a bunch of that as well. It can just sit at the use case layer and be used for analytics. That's not reality because that was only one dataset. This is what it would look like at the end of the day, is I would still have my original pipeline for the rest of the reference data, but I would want to make sure that the raw stage is present and the curated stage is present in the warehouse. It often isn't. That is a change we need to make for this customer.

In addition, then we have our new pathway which is going through the raw and curated buckets, and we've chosen some compute that will do that for us. We're able to move some of our use cases onto our new path. Don't tell me this is hard because I know you all live through migrations that last four years, so you're used to things that look like this, except now this is a choice.

Our particular use case, so this is what it looked like before. We were bypassing the warehouse. We are putting our model output in S3, and we are using it in the churn service. Then we had another one doing this. Let's start with then the customer account data. That can go onto the new pipe, that we output our raw and curated data. Then we put use case data for both of our systems into a bucket. Now what we have here is we're not processing and collecting our raw data twice. We're not cleaning it up twice. We're doing both of those one time, which means the customer account service can descale again and calm down.

Our use case data is, there are two separate outputs for the two separate services and they can move on, but we also have a standard now. When we start to change things for our customers, it's not really just always about the architecture. There are processes and cultural changes that need to happen as well. This is a very simple one. I, as a human, I want to go to the S3 console and I want to be able to navigate it. Coming up with intuitive prefixes really is quite important to me. Something so simple, but we don't always think about it when we think about discoverability. We want to get all these tools, but it really starts with the basics. Then for our reference data that uses the path that used it before, fill in the rest of the files and we're good to go. If you don't like that implementation, that's ok. You can chuck it because you've stored your raw data, which means you can replay any architecture that you like.

## Recap

We just covered raw data. We discussed owning and designing our lineage and our single sources of truth. We've talked about the data lifecycle, and a per entity view. There is no rule. There is no law that says every path has to match. Hopefully you've taken something away that will help you and your customers go beyond the data warehouse. If you remember only one thing from this talk, it is to please store your raw data.

## Questions and Answers

Participant 1: I found your definition of the source of truth really interesting. That idea where it splits up, but you will often have multiple places where things seemingly split. How do you know that you have one single source of truth here and it's split? You don't actually have four sources of truth somewhere further down the line from which they split again.

Sarah Usher: Four sources of truth by definition means you have zero. I find, usually what people call the source of truth and then what is reality of the source of truth when you use my definition, they differ. I always take what they say with a pinch of salt in that case. What do you do? You have to move slowly into a position where you have that path and you have to think about what are the right implementations per dataset that then will serve the different sources downstream. Yes, it will absolutely start that way. It will start with, we've made a SSOT table in the warehouse and it's _final and _final final.

In reality, that data is actually splitting at the product team's API because other teams are using that microservice. That is then the source of truth. You then need to convince people that actually, this is the source of truth. Either everyone needs to migrate to this one so we flatten the pipeline or we just let people know, this is actually our source of truth and this is your then analytical source of truth. Just slap another thing in front, kind of thing. The single source of truth is somewhere else. It's just not where they decided it was.

Participant 1: Do you think there's maybe a difference between a single source of truth for the data and the use case? I'm used to the medallion approach. The golden dataset is a single source of truth for your use case specifically. I feel there's maybe a nuance to this. I think maybe you're talking about the truth of the data itself where I'm used to thinking about the truth of the use case, which might be a little bit different.

Sarah Usher: Maybe a common example could be, I mentioned using different analytics tools. What I have seen is folks will have really well-defined data in the warehouse and they'll then make copies of that for Looker and all sorts of other tools that they choose to use. They call that source of truth, source of truth, source of truth. I then call it analytical source of truth, analytical source of truth, analytical source of truth, because it isn't the one that everyone uses. It's a really good question you ask. For me, it is the one that is the hardest to change your paradigm on a little bit because it's so ingrained that we do this. We take data from somewhere, we build it, and now this is source of truth. Now please use this. Thank you. Goodbye. It doesn't happen. People will find the path of least resistance. Yes, I hear you. I call it something different. The reality is, if we drop source of truth and we just say, where does the data split? It isn't in that one that we've crafted in the warehouse. It's upstream. That's a fact. That's not a decision I've made.

Participant 2: You spoke of storing our raw data and our curated data in the warehouse. If we are talking of cloud, how would that look like? We are migrating into cloud now from traditional data warehouses. If we are talking of storing both our raw data and our curated data in the cloud, how does that architecture look like?

Sarah Usher: I usually advocate for storing your raw data in files. Just for me, it's the most standard, cheapest way to do it. That's my preference. If you want to store your raw data in another way, it just needs to conform to the definition. The definition is that it's unprocessed as much as possible and that's immutable. The distinction between my preference and the definition. Then when it comes to curation, the world is your oyster. Do you want to make that data available via an API that has a data contract? Because I will love that. Or do you want to just make it available via different files that have a different type? Do you want to say that everyone who gets this curated data has to go to this particular Kafka stream? Again, as long as it conforms to the definition. You've got lots of options.

Participant 3: How do you manage the coupling between the use cases datasets, as well as the curated or even source datasets? Because source data will change, use cases will change, but then you need to manage evolution and change.

Sarah Usher: Changes in source data, they change, but they cannot change historically because effectively then that's technically a new piece of source data. Everything else is up for grabs, but that is the one thing that cannot change. If I capture a record from an API today and it's version 1, and the team then does a migration, that effectively becomes version 2 for the capturing of the raw data, even if they haven't called it version 2. That's how raw data changes. In that sense, raw data then doesn't really change, it can just change in shape. I think part of your question was use cases that change.

Participant 3:Yes, use cases as well as the data modeling, which might evolve or ideally you design the perfect model first try, but if given fixed source data, your model will evolve then for the analytics use cases, and then over a year of development, you'll end up with a different model as well as the use cases will evolve as well.

Sarah Usher: Yes. This is why I like the idea of three instead of two. I often see two. I often see we've captured our raw data and then we've made it beautiful for this use case and then someone else comes along and they're like, "This is cool, you've made it all clean, but I actually need it slightly differently". Then your source of truth is raw, by split or flow. I've never seen a perfect model, but if I've kept my raw data, I have the ability to then evolve my model well over time. I can effectively drop absolutely everything I've built and rebuild it from scratch. I'm not saying that's easy and I'm not saying it happens in seconds, that's years of work. If you haven't kept what you've previously captured, that becomes inflexible and an impossibility. Dealing with change in data is inevitable, but we can make it easier on ourselves by giving ourselves the ability to replay through a different architecture and through a different schema and through different use cases. Let's say something simple. We have a new field that's gotten added to the dataset.

Then we need to do what we always do. We would then have to capture that field. We'd have to change the curated dataset to now have this field. Then we'd have to pull it through into the use cases that need it. None of this is going to change that, but what it hopefully means is that you know all the places that that needs to change, and you don't have to then change it in multiple places. When we looked at our first example, if we have that new field, we're now changing the API, we're changing the three different places that are cleaning it, and that's a very small example. Then we're changing the two models, the two pipelines that have to process it, the two things that output it and then the two services. Whereas if we can streamline and have our source of truth at level 2, at stage 2, we can change just the source, just the role, just the curated, and just the use case that needed that data. It gives you a bit more control, but it also optimizes those changes.

Participant 4: Following maybe this discussion, I was wondering if the step between the curated data and the use case is a pull process or a push process, and if data products or data catalog fits in this kind of stuff.

Sarah Usher: Yes, it can be either. The implementation is your choice. You could stream all of that and push it all the way through. You could build batches that will pull it all the way through. That's really your choice. A data catalog could fit almost anywhere, and you have to define what stage the schema or that data entity is at. I would personally start with the curated data, like what is a customer at company X? How does that look? Then you might choose to store your raw schemas so that they're discoverable. You might choose to store your use case schemas so that they're discoverable, but then you should classify them in the catalog.

Participant 5: It was a question for you about taking products or items that have gone through the use case part of the architecture. When we generate something in there that we want to then push back to become a data source that can be used in other areas, what approaches would you take? Where would you integrate it? Would you bring it into raw? Would you take it into curated? How would you handle that?

Sarah Usher: It depends on the change. I've seen this commonly with calculations. We get all this data, and then we put it through the lifecycle, but then we actually generate something new based on a calculation, and then I restart the lifecycle because now that is a new entity. Then dependent on your architecture, if you've got a catalog, then you log that in the catalog, and you have to do the whole lifecycle again for that new element.

Participant 5: A lot of what we're dealing with at the moment is financial metrics and so on. We're taking lots of raw data from financial systems, applying hierarchies, calculating them, but then we're finding that the organization wants to change and push some of those metrics back to managers and suppliers and so on. That in itself is creating new use cases and new products. In the one that you're proposing, you've got an option to take that initial use case and push it back to the curated layer and then serve the original use case from there and the other ones so you're no longer sharing it, or you could push it all the way back to raw.

Sarah Usher: It depends. Remember, not every entity has to go through the same architecture. It only has to go through the same lifecycle. Per entity, I could have a completely different lifecycle. It might make sense for the original data coming in to go through streaming and into my warehouse where it then actually gets made into use case data, but then for the metrics, it might make sense that their entire lifecycle lives within the warehouse. It's just about seeing, ok, now it's been created, it's now raw in the warehouse, I now curate it in the warehouse and I can see it, and then I make it available for my use cases.

If we're pulling it back, some of those use cases might be further APIs, they might be census or Fivetran integrations, and you can have as many of those as you like because you've got your curated sitting in your warehouse. That's why it's quite important to redefine some of these concepts that have really become ingrained and we see them in a certain way. We need to see it differently. We don't have to have a single system for everything. Not every piece of data needs to follow the same path, but we need to see stages conceptually. What is true is your tooling is going to change. What is a fact is that your data is going to have to go through different steps to be used. We can actually control that conceptually. We don't have to be beholden to a single technology and just deal with it. Just throw everything in the warehouse, even if it doesn't fit there. Just put everything in the data lake because that's how we do it. We don't have to follow those rules anymore.

Participant 6: I think we're moving from on-prem and we're going into the cloud and we're using the whole concept of data products. We still maintain a role, and then we've got a trusted, and then we've got a curated. At the curated layer, we can then now create source-oriented data products which actually mimic whatever that is entrusted. Then we can then also apply consumer-oriented data products which is a data product that you can apply business logic or consumer logic to it. Then we then now go through what we call a data curation process, which my colleague spoke about around data catalogs. Then we then now connect it to a data marketplace.

The data marketplace is where anyone who wants access to the data can literally just then now download it and do whatever that they do with it. What's key to us is to say that as long as between the source and raw, we maintain that system of record, then we are sorted from a data lineage perspective. That's just an overview that I wanted to just give to say, I think that's the approach that we're taking. What you do with the data, once it leaves the data marketplace, it's up to you. We then now are no longer worried about the single source of truth because the data was already curated, it was already processed and it's available for everyone to consume. We follow the medallion architecture, but then we just introduce the data aspect of say, how do we actually share the data?

Participant 7: You talked about the immutability of raw data?

Sarah Usher: Yes.

Participant 7: When you say immutability, what exactly do you mean here? Because obviously records can be updated.

Sarah Usher: Yes. What I mean is that ideally, you've captured a record at a certain state, and then if that record changes, you can retain that previous state.

Participant 7: Like event sourcing or something like that, where you would keep all the historic versions of it?

Sarah Usher: Potentially, but even more simplistically, like if I'm a product engineer and I have a table full of customers, those customers might change things. They might get married and change their names. They might move. They might live in different places. I just have my normal form table that I'm updating. Ideally, I've also then kept a log. Ok, this customer looked like this at this stage and they lived at 1, 2, 3 place. Then they lived at 3, 4, 5, 6 place, and I can basically just see those changes over time. That's what I mean by immutable.

Participant 7: We have a discussion quite often, which is, what happens when there's mistakes in the data? Do you fix your raw data or do you implement the fixes within your data warehouse?

Sarah Usher: This is again why I like the three because if I've had a mistake that now gets pulled into the curated layer, I can fix it there and I will always still have the original. If you think about it practically, it's nice to obviously have good raw data. That's often not a reality. As I say, there are exceptions to every rule. If you are dealing with a lot of raw data and it's going to cost you less money to reprocess your raw data, please be my guest. Break the rules.

In general, I want that to be a conscious decision. I want the engineer to say, I know that this should be immutable. I know I'm taking a risk, but the tradeoff is worth it. That's really all it comes down to when we do engineering. In an ideal world, as I say, a lot of us are not dealing with whatever number we're on now of bytes. We can afford to reprocess that data and we can keep those mistakes. I also like to keep the mistakes because sometimes they actually weren't mistakes. Sometimes we drop a field that we didn't mean to drop and now we have to retrieve all that data. Now we spend money anyway fixing all of that. I would rather just keep what I've captured so that I architecturally have the ability to be flexible about how I then process the data. Certainly, there are exceptions to every rule as long as you make conscious choices about them.

 

See morepresentations with transcripts

 

Recorded at:

Feb 04, 2026

by

* Sarah Usher

#### This content is in theAI, ML & Data Engineeringtopic

##### Related Topics:

* AI, ML & Data Engineering
* QCon London 2025
* Transcripts
* Scalability
* QCon Software Development Conference
* Performance
* InfoQ
* Google BigQuery

* #### Related Editorial
* #### Popular across InfoQ##### Cloudflare Demonstrates Moltworker, Bringing Self-Hosted AI Agents to the Edge##### Google Supercharges Gemini 3 Flash with Agentic Vision##### Next Moca Releases Agent Definition Language as an Open Source Specification##### MUI Releases Base UI 1 with 35 Accessible Components##### Waku: the Minimal React Framework Reaches Alpha##### [Video Podcast] Improving Valkey with Madelyn Olson
* ##### Cloudflare Demonstrates Moltworker, Bringing Self-Hosted AI Agents to the Edge
* ##### Google Supercharges Gemini 3 Flash with Agentic Vision
* ##### Next Moca Releases Agent Definition Language as an Open Source Specification
* ##### MUI Releases Base UI 1 with 35 Accessible Components
* ##### Waku: the Minimal React Framework Reaches Alpha
* ##### [Video Podcast] Improving Valkey with Madelyn Olson
