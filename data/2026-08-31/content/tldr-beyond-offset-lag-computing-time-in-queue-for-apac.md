---
title: 'Beyond Offset Lag: Computing Time in Queue for Apache Hudi Data Lake Pipelines at Petabyte Scale - InfoQ'
url: https://www.infoq.com/articles/beyond-offset-lag-kafka-apache-hudi/
site_name: tldr
content_file: tldr-beyond-offset-lag-computing-time-in-queue-for-apac
fetched_at: '2026-08-31T23:09:00.809879'
original_url: https://www.infoq.com/articles/beyond-offset-lag-kafka-apache-hudi/
date: '2026-08-31'
description: In this article, author Srikanth Mamidala discusses data lake architecture for analytics, reporting, and machine learning, and shows how to manage consumer lag metrics with Kafka and Apache Hudi.
tags:
- tldr
---

InfoQ HomepageArticlesBeyond Offset Lag: Computing Time in Queue for Apache Hudi Data Lake Pipelines at Petabyte Scale

 AI, ML & Data Engineering
 

Online InfoQ Architect Certification (Sept 14): The sociotechnical side of architecture. 

# Beyond Offset Lag: Computing Time in Queue for Apache Hudi Data Lake Pipelines at Petabyte Scale

Aug 26, 202615
									min read

by

* Srikanth Mamidala

reviewed by

* Srini Penchikala

#### Follow us on

Youtube
232K Followers

Linkedin
26K Followers

Instagram
New

RSS
19K Readers

X
57.1k Followers

Facebook
21K Likes

Bluesky
New

### Key Takeaways

* Kafka Offset lag tells you how far behind a consumer is rather than telling you how old the data is. For Apache Hudi pipelines, these measurements are two completely different things. Confusing them leads to data freshness SLA violations.
* The time-in-queue metric is computed by reading the Kafka checkpoint from the latest Hudi commit file in S3, seeking to that offset in the Kafka topic, and measuring the timestamp delta between that message and the current time. Changes to producers, consumers, or existing pipeline infrastructure are not required.
* The algorithm must handle the case where the latest Hudi commit contains no checkpoint metadata. For example, when a parallel legacy pipeline made the most recent commit, requiring the algorithm to walk back through commit history to find the most recent commit that contains checkpoint metadata.
* Once deployed, time-based lag becomes a first-class data contract metric. Pipeline owners can define custom freshness SLAs per pipeline and receive alerts when the lake data ages beyond their threshold.
* Offset monitoring and time-lag monitoring are complementary. Running both gives you a complete picture of pipeline health that neither metric provides on its own.

## The Problem

AtTwilio, the data lake is the foundation for analytics, reporting, and machine learning across the company’s product lines: messaging, email, voice, and more. Internal teams rely on this data to understand product usage, drive business decisions, and power machine learning models such as anomaly or fraud detection. The pipelines that feed this lake useApache Hudi Delta Streamerto land data from Kafka, processing overfive trillion recordsmonthly as of Q4 2025, across self-hosted Kafka clusters, peaking at 12.9 million messages per second onCyber Monday 2025. At thatscale, we realized it was critical to give pipeline owners a precise way to define and enforce custom freshness SLAs. We were looking for a signal that was actionable without adding any overhead to live pipelines.

Traditional consumer lag metrics like consumer offset lag (records-lag-max) and even Hudi’skafkaDelayCountlooked fine. It seemed like consumers were keeping up with Kafka, but downstream analytics teams kept reporting stale data that was sometimes hours old. The issue wasn't Kafka throughput; it was a visibility gap. Hudi Delta Streamer manages its own checkpoints, which are stored alongside the table data in S3 and separate from Kafka's consumer group offset tracking. Standard lag monitoring tools likeBurrowtrack a consumer group’s committed offsets, which Hudi doesn’t populate by default, so they had no awareness of whether Hudi had actually committed that data to the lake.

The real question we needed to answer was how far behind is the latest Hudi commit from the messages currently sitting in the Kafka topic?

## Rethinking Lag as Time

How far behind is the Hudi job from messages in the Kafka topic? In other words, we wanted to compute and report how long it has been since the first unconsumed message arrived in the Kafka topic after a successful Hudi commit.

### How Offset Tracking Works in Hudi

HoodieStreamer(formerly HoodieDeltaStreamer) utilizes a checkpoint mechanism to track exactly what data has been ingested and prevent reprocessing of that same data. For Kafka sources, this checkpoint represents the exact topic offsets (per partition) or timestamps that have been successfully processed and committed to storage.

* For checkpoint storage, the checkpoint is embedded directly in the.hoodiecommit files asdeltastreamer.checkpoint.key.
* In terms of resilience, upon failure or restart, HoodieStreamer reads the latest commit file, retrieves this key, and resumes reading from the exact offset it left off.
* Kafka offset is stored as a string:topicName,0:offset0,1:offset1.

From this timeline of events, we can find the latest commit using the Apache Hudi SDK and extract the per-partition offsets that were last successfully written to the lake.

What makes this approach practical is that it requires nothing new from the pipelines themselves. The offset that Hudi already commits to S3 and the timestamps already on Kafka messages are enough to compute the true data freshness. We compute it with an external job called the metrics reporter. The metrics reporter is purely an external observer that reads artifacts the system already produces, requiring neither new instrumentation nor producer changes.

Figure 1. Example of a high-level data pipeline employing Metrics Reporter.

The ingestion path details are shown in Figure 2 below. Hudi Delta Streamer commits the data and its offset checkpoint to S3. The metrics reporter reads the Hudi timeline to find the latest committed offset.

Figure 2. Metrics Reporter reading offsets from the Hudi timeline.

## How the Algorithm Works

The metrics reporter runs every fifteen minutes in production. For each pipeline, the reporter completes the following tasks:

* Fetch the latest Hudi commit from the active timeline in S3. Walk through commits in reverse chronological order, the most recent first, to find the latest commit that contains adeltastreamer.checkpoint.key. This approach gives us the per-partition offsets of the last successfully committed batch. This is the exact offset Hudi has already consumed and committed to the lake.
* Seek to the checkpoint offset in each Kafka partition. This seeking positions the consumer at the first message Hudi has not yet committed to the lake. That message is still in Kafka, having arrived after the last successful Hudi write.
* Read that message and get its timestamp X. This timestamp records when the data arrived in Kafka. It has been sitting there, waiting to be picked up by the next Hudi run.
* Compute lag:currentTimestamp - X = how long that data has been waiting
* Cap at seven days if lag exceeds the threshold. This cap prevents unbounded values for inactive or stopped pipelines. If no valid checkpoint is found within the search depth, the reporter suppresses the metric entirely rather than publishing a misleading value.

#### Quick Example

To clarify this approach, here is a full walkthrough with real numbers. Consider a topic orders-events with three partitions. The latest Hudi commit contains this checkpoint:

orders-events,0:1200,1:980,2:1450

These are next-to-read offsets. Hudi has committed all messages up through offset 1199 on partition 0, 979 on partition 1, and 1449 on partition 2. The reporter seeks each partition to its checkpoint offset and polls for the next record. It retrieves one candidate per partition:

Partition

Seek to offset

Record timestamp

0

1200

45 minutes ago

1

980

12 minutes ago

2

1450

45 minutes ago

The earliest timestamp across all partitions is forty-five minutes old. That is the oldest message currently waiting to be committed to the lake. The lag is forty-five minutes. If the pipeline’sslaInMinutesis thirty, the SLA ratio is45/30 = 1.5, capped at 1.0, which is fully breached. The ratio is always capped at 1.0 because a pipeline cannot be more than fully breached. Using a graded ratio is a design choice; see the section, Real-World Results, for why.

The following code walks through the implementation in three parts: the core algorithm covering the complete solution, fetching the Hudi checkpoint from S3 by parsing the timeline up to the configured max depth, and seeking to the Kafka offset to read the first message yet to be consumed.

#### Core Algorithm (Java)

In the code below,HoodieResultis a small wrapper holding the commit metadata and the parsed per-partition offsets,kafkaClientwraps a standard Kafka Consumer, andnextRecordperforms the seek and poll shown further below.



// Step 1: Read Hudi timeline from S3 and extract checkpoint offsets
HoodieResult hudiResult = findLatestCommitWithCheckpoint(tableName, tableBasePath, maxCommitDepth);

final Map<TopicPartition, Long> checkpointOffsets = hudiResult.getPartitionToCheckpoint()
    .entrySet().stream()
    .collect(Collectors.toMap(
        e -> new TopicPartition(topic, e.getKey()),
        Map.Entry::getValue
    ));

// Step 2 & 3: Seek to checkpoint offset and read the next available message
final Optional<ConsumerRecord<String, String>> nextRecord = kafkaClient.nextRecord(topic, checkpointOffsets);

// Step 4: Compute time-in-queue
nextRecord.ifPresent(record -> {
    long currentTimeMs = OffsetDateTime.now(Clock.systemUTC()).toInstant().toEpochMilli();
    Duration lag = Duration.ofMillis(Math.max(0L, currentTimeMs - record.timestamp()));
    long lagSeconds = lag.getSeconds();
    // emit lagSeconds to your metrics system
});

#### Fetching the Hudi Checkpoint from S3

The key is walking the Hudi active timeline and finding the most recent commit that contains checkpoint metadata. We use the Apache Hudi SDK'sHoodieTableMetaClientto read the.hoodie/timeline directory from S3.HoodieTableMetaClientuses Hadoop'sS3A filesystemunder the hood to access S3. It needs a Hadoop configuration to do so, which we take from theSparksession the reporter already runs in. No actual Spark data processing happens; Spark here is purely the runtime environment that gives the Hudi SDK its S3 access layer.



public static HoodieResult findLatestCommitWithCheckpoint(String datasetName, String basePath, int maxCommits) {
    // getActiveTimeline initializes a HoodieTableMetaClient against the table's S3 path and returns its active timeline.
    HoodieActiveTimeline timeline = getActiveTimeline(basePath);
    HoodieTimeline commits = timeline.getCommitsTimeline().filterCompletedInstants();

    // maxCommits is read from env var MAX_COMMIT_DEPTH, defaults to 100
    int depth = Math.min(maxCommits, commits.countInstants());
    
    // n=0 is the most recent commit, iterates in reverse chronological order
    for (int n = 0; n < depth; n++) {   
        HoodieInstant commit = commits.nthFromLastInstant(n).get();
        HoodieCommitMetadata metadata = HoodieCommitMetadata.fromBytes(
            timeline.getInstantDetails(commit).get(), HoodieCommitMetadata.class);

          // CHECKPOINT_KEY = "deltastreamer.checkpoint.key"
        if (metadata.getMetadata(CHECKPOINT_KEY) != null) {
            return new HoodieResult(metadata, commit.getTimestamp(), datasetName, n);
        }
    }
    return new HoodieResult(-1); // no checkpoint found
}

The checkpoint string has the format:topicName,0:offset0,1:offset1,...with one entry per partition. Importantly, Hudi stores these as next-to-read offsets, the resume point for the next run, not the last-consumed offset. So if Hudi last committed the message at offset 1199, it stores 1200. The Kafka consumer, seeking to offset 1200, is positioned at the first message not yet committed to the data lake.

#### Seeking to the Checkpoint in Kafka

Assign the partitions, seek each to its checkpoint offset, and return the earliest record across them.



// Assign partitions and seek to checkpoint offsets
consumer.assign(checkpointOffsets.keySet());
checkpointOffsets.forEach(consumer::seek);

// Poll and find the earliest record across all partitions
ConsumerRecord<String, String> earliest = null;
ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(500));
for (ConsumerRecord<String, String> record : records) {
    if (earliest == null || record.timestamp() < earliest.timestamp()) {
        earliest = record;
    }
}
// earliest.timestamp() is X — the timestamp of the first unconsumed message

The three code snippets explained above are the whole algorithm. Getting the happy path working was the easy part; making the metric reliable in production required handling a series of edge cases, which are covered below.

## Edge Cases and Considerations

### Clock Skew Across Producers

Because the lag metric uses the message timestamp set by the producer, producers whose system clocks drift ahead can make lag appear artificially low (or even negative). The algorithm floors the lag at zero usingMath.max(0L, currentTimeMs - record.timestamp()). Sustained negative raw values before the floor are a signal worth alerting on separately. They indicate clock skew that requires investigation.

### Multi-Partition Topics

At scale, Kafka topics have many partitions. The checkpoint stored in Hudi contains one offset per partition (as shown in the example above). The algorithm seeks each partition to its respective checkpoint offset and polls for the next available record. This approach provides one candidate message per partition. We then take the record with the earliest timestamp across all partitions, not the average nor the latest. That message represents the oldest data still waiting to be committed to the lake, which is the worst-case lag and the number that matters for SLA enforcement. Averaging would hide a slow partition. Using the latest number would hide a stuck partition.

### Multiple Hudi Table Writers and Kafka Checkpoints

In production, a Hudi table can have multiple writers and not all of them commit Kafka checkpoint metadata. This situation commonly arises during migrations, when a legacy pipeline and a new pipeline write to the same table simultaneously while the old one is being decommissioned.

This is exactly the situation we encountered. Our legacy setup used two pipelines. One read from Kafka and wrote raw data to S3. A second read from that S3 output, transformed the data, and wrote to the Hudi table.

That second pipeline was sourced from S3, not Kafka. So it never embedded adeltastreamer.checkpoint.keyin its commits. Our new framework reads directly from Kafka and writes to the same Hudi table. Its commits include the checkpoint key.

During the migration overlap, both pipelines were writing to the same table. When the legacy pipeline made the most recent commit, the original algorithm found no checkpoint metadata. It had nothing to seek to, so lag defaulted to the seven-day cap, producing false spikes in the lag graph that were not real data freshness failures.

Figure 3. This flow shows multiple writers on a shared Hudi table.

#### The Fix

The root cause was that the original algorithm only looked at the most recent commit. The real solution was to stop assuming the latest commit is the right one. We changed the algorithm to walk back through the timeline in reverse chronological order up toMAX_COMMIT_DEPTHcommits until it finds the most recent commit that actually contains adeltastreamer.checkpoint.key. Because only our new Kafka-sourced pipeline embeds this key, the walk-back skips over legacy pipeline commits and lands on a valid checkpoint. This solution prevented the false spikes without any external state.

If no commit with a checkpoint is found within the search depth, the reporter suppresses the metric entirely rather than publishing a potentially misleading value. A missing metric surfaces as a "No Data" alert in our alerting system, which is a more honest signal than a number that looks real but is not.

Figure 4. Walking the Hudi timeline in reverse to find a valid checkpoint.

#### Updated Algorithm

Fetch the latest commit from the Hudi timeline and walk back in reverse chronological order. Find the most recent commit that contains adeltastreamer.checkpoint.key;If none found withinMAX_COMMIT_DEPTH, suppress reporting entirely

* Seek to that offset in each partition
* Read the earliest message across all partitions and get timestamp X
* lag = currentTimestamp - X
* Cap at seven days

## Real-World Results

The metrics reporter runs every fifteen minutes via EventBridge on EMR Serverless. Each pipeline defines its own SLA threshold via aslaInMinutesfield in its onboarding YAML config:



metadata:
# alert if data is more than 30 minutes stale
slaInMinutes: 30

If omitted, the default is sixty minutes for streaming pipelines and 1440 minutes (twenty-four hours) for batch pipelines. The reporter convertsslaInMinutesto seconds internally. SLA breach is reported aslagSeconds / slaThresholdSeconds, a ratio between 0.0 and 1.0 (capped at 1.0), where 1.0 is a full breach. A pipeline at 0.7 is at seventy percent of its threshold. Dashboards show the progression toward breach rather than a binary flip from green to red. No changes were required to any existing pipeline; the reporter is purely an observation layer.

The algorithm described above is the result of several iterations in production. When we first deployed it, we immediately hit edge cases we had not anticipated. Each iteration produced either false positives or silent failures in the metric. Here is what we learned.

#### The Epoch Timestamp Trap

This issue was a total headache to track down. Our first iteration calculated lag aslatestKafkaRecord.timestamp() - hudiCommitTimestamp, assuming the gap would simply widen as Hudi fell behind. We didn't realize that when Hudi fails to locate a commit with checkpoint metadata, it doesn't error out. Instead, it silently defaults to a timestamp of epoch zero,19700101000000000. This string, formatted asyyyyMMddHHmmssSSS, translated to a millisecond zero, causing our metric to explode into an astronomical, meaningless number. AMath.max(0L,<value>)floor we had in place was useless here. The hard-learned lesson was that we had to explicitly guard against epoch defaults and pivot our logic. By switching tocurrentTime - timestamp_of_first_unconsumed_message, we finally started answering the right question, proving that sometimes, a missing metric is better than a hallucinated value.

#### The Latest Commit Is Not Always the Right Commit

The original algorithm simply reads the most recent commit from the Hudi timeline. During the migration overlap, when both the legacy pipeline and the new pipeline were writing to the same table, the most recent commit was frequently the legacy pipeline's, which had no checkpoint key. Changing to a depth-based walk-back (up toMAX_COMMIT_DEPTHcommits, defaulting to 100) solved this issue. The algorithm now skips over commits with no checkpoint key and finds the most recent valid one. We also started reporting commit depth (i.e., how many commits back we had to look) as a separate metric. A high commit depth is a leading indicator that something is wrong with the primary pipeline even before the lag metric crosses its threshold.

#### Missing Kafka Timestamps

Kafka allows producers to omit a message timestamp. When that happens, the record doesn't carry a null value. Kafka represents a missing timestamp with the sentinel -1 (ConsumerRecord.NO_TIMESTAMP). When the algorithm encountered a record with a -1 timestamp, it would attempt to compute lag from it and publish a garbage metric. The fix is to detect -1 timestamps explicitly and skip reporting for that pipeline. Like the epoch case, silence is more useful than a misleading number.

#### SLA as a Ratio, Not a Binary

An "SLA ratio" is not an industry term. Rather, it is a design choice we arrived at in production. Our initial SLA metric was binary, breached or not. The problem was that it only fired after the SLA was already missed. Engineers want to know when a pipeline is at seventy to eighty percent of its threshold so they can investigate before customers are impacted. Switching to a 0.0-1.0 ratio gives teams a leading signal, allowing them to set a warning at 0.7 and a critical alert at 1.0, instead of a single all-or-nothing threshold. This approach mirrors the SRE practice of tracking error-budget burn rate, with which you watch the budget consuming speed rather than only reacting once the budget is exhausted.

### What's Next

If you want to apply this pattern, you need three things:

* Access to your Hudi table's.hoodie/directory on S3
* A Kafka client to seek arbitrary offsets
* A scheduler to run the reporter periodically.

The core algorithm works for any Hudi Delta Streamer pipeline writing to S3. If you are onDelta Lakewith Structured Streaming, Spark stores Kafka offsets in the streaming checkpoint directory rather than the table metadata itself, but the principle is the same: Find the last committed Kafka offset from wherever your framework persists it, seek to that position, and compute the timestamp delta.

On our roadmap, we are evaluating this approach for ourIcebergpipelines as we migrate from Hudi. We are also exploring pairing this metric with anomaly detection libraries with open-source options likeProphetorLuminaire, rather than relying solely on fixed SLA thresholds.

### Common Questions

Will the metrics reporter interfere with HoodieStreamer's consumer group? No. The reporter uses a dedicated consumer group ID which is completely separate from HoodieStreamer's own group. It also setsenable.auto.commit=false, so it never commits offsets back to Kafka. It reads and discards. There is no risk of rebalancing or interfering with the ingestion pipeline.

What happens if a topic partition is empty? Ifconsumer.poll()returns no records after seeking to the checkpoint offset, the reporter treats this as an empty topic and reports zero lag. It does not hang. The five hundred millisecond poll timeout bounds the wait and an empty result is handled explicitly. The lag defaults to zero and is still reported to the metrics system.

 

## About the Author

 

 

 

#### Srikanth Mamidala

Show more
Show less

### Rate this Article

Adoption

Style

 Author Contacted

#### This content is in theAI, ML & Data Engineeringtopic

##### Related Topics:

* AI, ML & Data Engineering
* Messaging
* SOA
* Architecture
* Streaming
* Data Lake
* Data Pipelines
* Apache Kafka
* Enterprise Architecture

* #### Related Editorial
* #### Related Sponsors
* #### Related SponsorOctober 8, 2026, 12 PM EDT##### When AI Accelerates Development, Can Your CI Pipeline Keep Up?Presented by: Eric Metaj - Product Marketing Manager, Software Delivery at Datadog, and Rohin Chandra - Product Manager, CI/CD Optimization at Datadog
* October 8, 2026, 12 PM EDT##### When AI Accelerates Development, Can Your CI Pipeline Keep Up?Presented by: Eric Metaj - Product Marketing Manager, Software Delivery at Datadog, and Rohin Chandra - Product Manager, CI/CD Optimization at Datadog

### Related Content

### The InfoQNewsletter

A round-up of last week’s content on InfoQ sent out every Tuesday. Join a community of over 250,000 senior developers.View an example

Enter your e-mail address

Select your country

Select a country

I consent to InfoQ.com handling my data as explained in this 
Privacy Notice
.

We protect your privacy.