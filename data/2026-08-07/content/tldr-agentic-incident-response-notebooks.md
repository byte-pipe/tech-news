---
title: Agentic incident response notebooks
url: https://blog.cauchy.org/blog/incident-response-notebooks/
site_name: tldr
content_file: tldr-agentic-incident-response-notebooks
fetched_at: '2026-08-07T00:41:37.280603'
original_url: https://blog.cauchy.org/blog/incident-response-notebooks/
date: '2026-08-07'
description: A composable notebook interface for incident response, threat hunting, and threat intelligence workflows. Typed decorators bridge Splunk, Defender XDR, and Snowflake into DuckDB. An agent builds case-specific notebooks from alert context instead of maintaining templates.
tags:
- tldr
---

# Agentic incident response notebooks

 

BY
 
 
Kyrre Wahl Kongsgård
 
 
 

This post is based on work done at the DNB Cyber Defense Center on notebook-driven security operations. An earlier version of parts of this work was published on themarimo blogas a case study. This post covers what we built: a marimo-based interface for incident response, threat hunting, and threat intelligence workflows, from remote data source integration through agent-built case notebooks.

We built an incident response workflow aroundmarimonotebooks: one executable case environment for querying security platforms, joining evidence locally, deploying focused web applications, and giving agents the same context analysts use.

Incident response is integration work. Alerts and raw events may be in Splunk, Sentinel, or Defender XDR. Vulnerability data may live in Databricks, Snowflake, or another analytical backend. Other context is more on-demand: cloud control plane state, directory state, asset ownership, change tickets, threat intel feeds. The analyst has to pull those pieces into one explanation and document the decision.

Most security tools are good at one part of that job. SIEMs are good at search. Case systems are good at status and playbooks. Dashboards are good at showing well-defined views. But the middle of an investigation is exploratory: many tabs open, a notes document on the side, copied tables, rewritten queries, manual joins, and a growing explanation of what probably happened. We wanted an interface that preserves that flexibility while making the work executable, reproducible, and directly controllable by agents.

We also wanted the architecture to stay composable. Splunk, Defender XDR, and Snowflake are integrations, not hard dependencies. The same notebook surface should work if a query engine, data warehouse, or security platform is replaced with an open source equivalent, as long as the replacement can return typed tables and pass context into the workflow.

Your browser does not support the video tag.

A sped-up walkthrough of the agent building a case notebook end to end through
marimo-pair. The case shown is a simplified scenario triggered on a laptop
rather than a live alert, since real cases are confidential, and nothing on
screen is sensitive. Each cell is authored and executed by the agent, and the
finished notebook is the case file. The agent interface itself is covered
later in the post.

## Why marimo fits

We chose marimo because it treats a notebook as a reproducible program. In a traditional notebook, cells can be run out of order and outputs can depend on hidden state from earlier executions. Here, dependent cells recompute from the code that is actually visible. Change the host, time window, or selected row, and every dependent query and chart recomputes from the same state. That matters in incident response, where the conclusion should still be connected to the query and evidence that produced it.

The notebook also has a practical operational lifecycle. The file is plain Python, so it can be reviewed, versioned, moved, served as an app, exported as static HTML, or driven by an agent throughmarimo-pair. Those properties are what let one case notebook become the analyst workspace, the shared view, the archived report, and the agent handoff point.

It is also a practical base interface. The runtime already connects to analytical backends such as Snowflake, Databricks, ClickHouse, Postgres, BigQuery, and DuckDB. For security systems that do not expose a SQL interface, such as Splunk, Microsoft Sentinel, oradvanced hunting in Microsoft Defender XDR, we built an SDK for this use case: incident response notebooks that can run native SPL and KQL, cast the remote results into a typed dataframe, and continue the investigation in the notebook. In our notebooks, we usually use the ibis backend so Splunk results, Defender XDR events, and Snowflake tables can be joined locally through DuckDB.

The agent interface is the same notebook. Withmarimo-pair, an agent can create a new notebook or open a running one, execute temporary Python that can read notebook state, and make durable changes by writing and running Python and SQL cells in the live notebook. Those cells can call our SPL and KQL decorators, inspect outputs, and revise the notebook. The model is not filling a form from the outside. It is working inside the same analysis surface as the analyst, with code, outputs, and intermediate state in the loop.

Notebooks are not new to security operations. What changes here is the combination: the analyst context, the data sources, the executable analysis, and the agent all meet in one running notebook. Instead of maintaining one notebook template per alert type, the agent can build the notebook that this task needs. The same pattern carries naturally beyond investigations into threat hunting and threat intelligence.

There are three parts to the system. First, security data access: Splunk, Defender XDR, and other security tools keep their native query languages, but notebook code receives typed tables that can be joined locally. Second, the operational notebook: the same.pyfile works as an analyst workspace, a shared live view, a deployed app, or an archived report. Third, the agent loop: an agent can build and revise the case notebook from alert context, using the same data access patterns an analyst would use.

The common artifact is the case notebook. Everything below is about making that artifact useful: connected to the right data, executable and reproducible, easy to share or deploy, and editable by both analyst and agent.

The first problem is security data access. If the data is already available through a source marimo can access natively, you are ready to work. If not, we need a way to run the source’s native query language and bring the result back into the notebook.

## Connecting data sources

Security logs are often stored in SIEMs and security platforms such as Splunk, Sentinel, Elastic, and Defender XDR. To use those logs in a notebook, the first step is not a database connection. It is running the query the source already understands: SPL against Splunk, or KQL against Sentinel and advanced hunting in Microsoft Defender XDR.

The problem is what comes back. Splunk indexes events with default metadata fields, then derives many other fields through field discovery and search-time field extractions tied to a source, sourcetype, or host. The REST API can return search results as JSON, but that is still a loosely structured result set rather than a dataframe schema: fields can depend on the events and extraction rules that matched, and timestamps, numbers, multivalue fields, and nulls still need explicit handling. Long searches run as async jobs that need to be submitted, polled, and paginated. KQL sources have their own APIs and response formats. Before the result can be combined with Snowflake query results, filtered by widgets, or transformed in downstream cells, the notebook needs it in a dataframe or table shape with known column types.

The missing gap between a security platform and a notebook. A Splunk query can
be valid SPL, and Splunk can return valid JSON, but downstream cells still
need predictable columns and types. The SDK wraps the remote query, normalizes
the response, and returns the configured tabular format so the rest of the
notebook can join, filter, and display the result.

The SDK gives this pattern a small Python interface. You write a function that returns the native query string, optionally declare the expected columns and types, and the decorator handles authentication, execution, type conversion, and caching. A global backend option controls the tabular return type: Polars, pandas, PyArrow, or anibistable backed by an in-memory DuckDB connection. The notebook-facing result can then be joined, filtered, and reshaped with the rest of the investigation.

The interactive cells below illustrate the SDK’s API using mock Splunk and KQL services - the queries run against synthetic data in your browser rather than live security platforms. The real notebooks run server-side against production data, and these examples are simplified to show the shape of the code.

 
 
 

Loading…

 
 

import%20sys%0Aimport%20asyncio%0Aimport%20marimo%20as%20mo%0Afrom%20io%20import%20StringIO%0A%0Aif%20%22pyodide%22%20in%20sys.modules%3A%0A%20%20%20%20import%20micropip%0A%20%20%20%20import%20js%20%20%23%20type%3A%20ignore%5Bimport%5D%0A%20%20%20%20await%20micropip.install(js.location.origin%20%2B%20%22%2Fmarimo-islands%2Fcombined%2Fmock_sdk-0.1.0-py3-none-any.whl%22)%0A%20%20%20%20await%20micropip.install(%22polars%22)%0A%0Aimport%20polars%20as%20pl%0Afrom%20polars%20import%20DataFrame%2C%20col%0Afrom%20datetime%20import%20datetime%2C%20timedelta%0Aimport%20duckdb%0Aimport%20ibis%0Afrom%20mock_sdk%20import%20spl%2C%20kql%2C%20sf%2C%20options%2C%20rt%0Aoptions.backend%20%3D%20%22ibis%22%0A%0A%23%20%E2%94%80%E2%94%80%20Mock%20data%20for%20investigations%20section%20%E2%94%80%E2%94%80%0AT0%20%3D%20datetime(2026%2C%203%2C%2015%2C%2014%2C%2022%2C%200)%0AS0%20%3D%20datetime(2026%2C%203%2C%2018%2C%209%2C%2015%2C%200)%0A%0ALOLDRIVERS_CSV%20%3D%20(%0A%20%20%20%20%22sha256%2Cdriver%2Ccategory%2Cvendor%5Cn%22%0A%20%20%20%20%22bfc2ef3b404294fe2fa05a8b71c7f786b58519175b7202a69fe30f45e607ff1c%2Ctruesight.sys%2Cvulnerable_driver%2CRogueKiller%5Cn%22%0A%20%20%20%20%22d0b5d40b47c5e4ade27b72ab2e2c5c9e346bbe0c6e2a43ef04e649e7b8e5d2a1%2Crentdrv2.sys%2Cvulnerable_driver%2CKaspersky%5Cn%22%0A%20%20%20%20%226a4875ae86131a594019dec4abd46ac6ba47e57a88287b814d07d929858fe3e5%2Cgdrv.sys%2Cvulnerable_driver%2CGIGABYTE%22%0A)%0A%0A%23%20Save%20real%20SDK%20reference%20(unused%20but%20kept%20for%20clarity)%0A_spl_sdk%20%3D%20spl%0A_ddb%20%3D%20ibis.duckdb.from_connection(duckdb)%0A%0Adef%20ddb_table(name%2C%20data)%3A%0A%20%20%20%20%23%20Register%20any%20frame%20(polars%20%2F%20arrow%20%2F%20ibis)%20into%20the%20shared%20DuckDB%0A%20%20%20%20%23%20connection%20and%20return%20an%20ibis%20table%2C%20so%20marimo%20serves%20table%0A%20%20%20%20%23%20search%2C%20sort%2C%20and%20pagination%20from%20the%20kernel.%20In-memory%20frames%0A%20%20%20%20%23%20(ibis.memtable%2C%20a%20bare%20polars%20DataFrame)%20have%20no%20connection%0A%20%20%20%20%23%20behind%20them%2C%20so%20their%20search%20function%20never%20registers%20and%20the%0A%20%20%20%20%23%20table%20shows%20%22could%20not%20reach%20its%20function%20on%20the%20kernel%22.%0A%20%20%20%20arrow%20%3D%20(%0A%20%20%20%20%20%20%20%20data.to_arrow()%20if%20hasattr(data%2C%20%22to_arrow%22)%0A%20%20%20%20%20%20%20%20else%20data.to_pyarrow()%20if%20hasattr(data%2C%20%22to_pyarrow%22)%0A%20%20%20%20%20%20%20%20else%20data%0A%20%20%20%20)%0A%20%20%20%20return%20_ddb.create_table(name%2C%20arrow%2C%20overwrite%3DTrue)%0A%0Aclass%20SplMock%3A%0A%20%20%20%20_data%20%3D%20%7B%7D%0A%20%20%20%20_cache%20%3D%20%7B%7D%0A%20%20%20%20_fetch_count%20%3D%20%7B%7D%0A%20%20%20%20_remote_delay%20%3D%20%7B%7D%0A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20df(**kw)%3A%0A%20%20%20%20%20%20%20%20def%20decorator(fn)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20async%20def%20wrapper(*a%2C%20**kw2)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20table_name%20%3D%20kw2.pop(%22table_name%22%2C%20None)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20cache_key%20%3D%20(%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20fn.__name__%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20fn.__code__.co_code%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20tuple(sorted(kw2.items()))%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20table_name%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20kw.get(%22caching%22)%20and%20cache_key%20in%20SplMock._cache%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20SplMock._cache%5Bcache_key%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20SplMock._fetch_count%5Bfn.__name__%5D%20%3D%20SplMock._fetch_count.get(fn.__name__%2C%200)%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20await%20fn(*a)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20delay%20%3D%20SplMock._remote_delay.get(fn.__name__%2C%200)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20delay%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20await%20asyncio.sleep(delay)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20df%20%3D%20SplMock._data.get(fn.__name__%2C%20DataFrame())%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20df.is_empty()%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20df%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20table_name%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20result%20%3D%20_ddb.create_table(table_name%2C%20df.to_arrow()%2C%20overwrite%3DTrue)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20result%20%3D%20df%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20kw.get(%22caching%22)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20SplMock._cache%5Bcache_key%5D%20%3D%20result%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20result%0A%20%20%20%20%20%20%20%20%20%20%20%20wrapper.__name__%20%3D%20fn.__name__%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20wrapper%0A%20%20%20%20%20%20%20%20return%20decorator%0A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20fetch_count(name)%3A%0A%20%20%20%20%20%20%20%20return%20SplMock._fetch_count.get(name%2C%200)%0A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20clear_cache(name%3DNone)%3A%0A%20%20%20%20%20%20%20%20if%20name%20is%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20SplMock._cache.clear()%0A%20%20%20%20%20%20%20%20%20%20%20%20return%0A%20%20%20%20%20%20%20%20SplMock._cache%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20key%3A%20value%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20key%2C%20value%20in%20SplMock._cache.items()%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20key%5B0%5D%20!%3D%20name%0A%20%20%20%20%20%20%20%20%7D%0A%0Aspl%20%3D%20SplMock%0Aspl._data%20%3D%20%7B%0A%20%20%20%20%22proxy_events%22%3A%20DataFrame(%5B%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%2C%20%22host%22%3A%20%22ws01.corp%22%2C%20%22dest_domain%22%3A%20%22github.com%22%2C%20%22bytes_out%22%3A%201420%2C%20%22category%22%3A%20%22Software%2FTechnology%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%20%2B%20timedelta(minutes%3D2)%2C%20%22host%22%3A%20%22ws03.corp%22%2C%20%22dest_domain%22%3A%20%22api.github.com%22%2C%20%22bytes_out%22%3A%203200%2C%20%22category%22%3A%20%22Software%2FTechnology%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%20%2B%20timedelta(minutes%3D5)%2C%20%22host%22%3A%20%22ws01.corp%22%2C%20%22dest_domain%22%3A%20%22login.microsoftonline.com%22%2C%20%22bytes_out%22%3A%20890%2C%20%22category%22%3A%20%22Authentication%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%20%2B%20timedelta(minutes%3D8)%2C%20%22host%22%3A%20%22ws03.corp%22%2C%20%22dest_domain%22%3A%20%22pypi.org%22%2C%20%22bytes_out%22%3A%2015200%2C%20%22category%22%3A%20%22Software%2FTechnology%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%20%2B%20timedelta(minutes%3D12)%2C%20%22host%22%3A%20%22ws01.corp%22%2C%20%22dest_domain%22%3A%20%22storage.googleapis.com%22%2C%20%22bytes_out%22%3A%2042000%2C%20%22category%22%3A%20%22Business%22%7D%2C%0A%20%20%20%20%5D)%2C%0A%20%20%20%20%22proxy_narwhals%22%3A%20DataFrame(%5B%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%2C%20%22host%22%3A%20%22ws01.corp%22%2C%20%22src_ip%22%3A%20%2210.0.1.45%22%2C%20%22bytes_out%22%3A%201420%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%20%2B%20timedelta(minutes%3D2)%2C%20%22host%22%3A%20%22ws03.corp%22%2C%20%22src_ip%22%3A%20%2210.0.1.62%22%2C%20%22bytes_out%22%3A%203200%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%20%2B%20timedelta(minutes%3D5)%2C%20%22host%22%3A%20%22ws01.corp%22%2C%20%22src_ip%22%3A%20%2210.0.1.45%22%2C%20%22bytes_out%22%3A%20890%7D%2C%0A%20%20%20%20%5D)%2C%0A%20%20%20%20%22proxy_shorthand%22%3A%20DataFrame(%5B%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%2C%20%22host%22%3A%20%22ws01.corp%22%2C%20%22src_ip%22%3A%20%2210.0.1.45%22%2C%20%22bytes_out%22%3A%201420%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%20%2B%20timedelta(minutes%3D2)%2C%20%22host%22%3A%20%22ws03.corp%22%2C%20%22src_ip%22%3A%20%2210.0.1.62%22%2C%20%22bytes_out%22%3A%203200%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%20%2B%20timedelta(minutes%3D5)%2C%20%22host%22%3A%20%22ws01.corp%22%2C%20%22src_ip%22%3A%20%2210.0.1.45%22%2C%20%22bytes_out%22%3A%20890%7D%2C%0A%20%20%20%20%5D)%2C%0A%20%20%20%20%22web_stats%22%3A%20DataFrame(%5B%0A%20%20%20%20%20%20%20%20%7B%22user%22%3A%20%22alice%22%2C%20%22total_bytes%22%3A%2042000%2C%20%22request_count%22%3A%208%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22user%22%3A%20%22bob%22%2C%20%22total_bytes%22%3A%2015200%2C%20%22request_count%22%3A%204%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22user%22%3A%20%22SYSTEM%22%2C%20%22total_bytes%22%3A%204090%2C%20%22request_count%22%3A%205%7D%2C%0A%20%20%20%20%5D)%2C%0A%20%20%20%20%22driver_sha256_stats%22%3A%20DataFrame(%5B%0A%20%20%20%20%20%20%20%20%7B%22SHA256%22%3A%20%22bfc2ef3b404294fe2fa05a8b71c7f786b58519175b7202a69fe30f45e607ff1c%22%2C%20%22FileName%22%3A%20%22tru.sys%22%2C%20%22load_count%22%3A%206%2C%20%22device_count%22%3A%201%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22SHA256%22%3A%20%22a1b2c3d4e5f60718293a4b5c6d7e8f901234567890abcdef1234567890abcdef%22%2C%20%22FileName%22%3A%20%22intelppm.sys%22%2C%20%22load_count%22%3A%203%2C%20%22device_count%22%3A%201%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22SHA256%22%3A%20%221234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef%22%2C%20%22FileName%22%3A%20%22ndis.sys%22%2C%20%22load_count%22%3A%203%2C%20%22device_count%22%3A%201%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22SHA256%22%3A%20%22deadbeef0123456789abcdef0123456789abcdef0123456789abcdef01234567%22%2C%20%22FileName%22%3A%20%22fltMgr.sys%22%2C%20%22load_count%22%3A%203%2C%20%22device_count%22%3A%201%7D%2C%0A%20%20%20%20%5D)%2C%0A%20%20%20%20%22hit_load_events%22%3A%20DataFrame(%5B%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%2C%20%22DeviceName%22%3A%20%22WS-FINANCE-03%22%2C%20%22FileName%22%3A%20%22tru.sys%22%2C%20%22FolderPath%22%3A%20%22C%3A%5C%5CWindows%5C%5CTemp%5C%5Ctru.sys%22%2C%20%22SHA256%22%3A%20%22bfc2ef3b404294fe2fa05a8b71c7f786b58519175b7202a69fe30f45e607ff1c%22%2C%20%22InitiatingProcessFileName%22%3A%20%22services.exe%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20T0%20%2B%20timedelta(hours%3D6)%2C%20%22DeviceName%22%3A%20%22WS-FINANCE-03%22%2C%20%22FileName%22%3A%20%22tru.sys%22%2C%20%22FolderPath%22%3A%20%22C%3A%5C%5CWindows%5C%5CTemp%5C%5Ctru.sys%22%2C%20%22SHA256%22%3A%20%22bfc2ef3b404294fe2fa05a8b71c7f786b58519175b7202a69fe30f45e607ff1c%22%2C%20%22InitiatingProcessFileName%22%3A%20%22services.exe%22%7D%2C%0A%20%20%20%20%5D)%2C%0A%20%20%20%20%22c2_processes%22%3A%20DataFrame(%5B%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20S0%2C%20%22DeviceName%22%3A%20%22WS-DEV-07%22%2C%20%22FileName%22%3A%20%22WINWORD.EXE%22%2C%20%22ProcessCommandLine%22%3A%20'%22C%3A%5C%5CProgram%20Files%5C%5CMicrosoft%20Office%5C%5CRoot%5C%5COffice16%5C%5CWINWORD.EXE%22%20%2Fn%20%22Q1-Review-FINAL.docm%22'%2C%20%22InitiatingProcessFileName%22%3A%20%22explorer.exe%22%2C%20%22ProcessId%22%3A%205100%2C%20%22AccountName%22%3A%20%22sarah.chen%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20S0%20%2B%20timedelta(seconds%3D4)%2C%20%22DeviceName%22%3A%20%22WS-DEV-07%22%2C%20%22FileName%22%3A%20%22powershell.exe%22%2C%20%22ProcessCommandLine%22%3A%20%22powershell.exe%20-NoExit%20-Command%20%5BConsole%5D%3A%3AOutputEncoding%3D%5BText.UTF8Encoding%5D%3A%3AUTF8%22%2C%20%22InitiatingProcessFileName%22%3A%20%22WINWORD.EXE%22%2C%20%22ProcessId%22%3A%205444%2C%20%22AccountName%22%3A%20%22sarah.chen%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20S0%20%2B%20timedelta(seconds%3D30)%2C%20%22DeviceName%22%3A%20%22WS-DEV-07%22%2C%20%22FileName%22%3A%20%22notepad.exe%22%2C%20%22ProcessCommandLine%22%3A%20%22notepad.exe%22%2C%20%22InitiatingProcessFileName%22%3A%20%22powershell.exe%22%2C%20%22ProcessId%22%3A%205612%2C%20%22AccountName%22%3A%20%22sarah.chen%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20S0%20%2B%20timedelta(minutes%3D5)%2C%20%22DeviceName%22%3A%20%22WS-DEV-07%22%2C%20%22FileName%22%3A%20%22cmd.exe%22%2C%20%22ProcessCommandLine%22%3A%20%22cmd.exe%20%2Fc%20copy%20%5C%5C%5C%5CWS-FINANCE-03%5C%5CC%24%5C%5CWindows%5C%5CTemp%5C%5Cmaintenance.exe%22%2C%20%22InitiatingProcessFileName%22%3A%20%22powershell.exe%22%2C%20%22ProcessId%22%3A%206200%2C%20%22AccountName%22%3A%20%22SYSTEM%22%7D%2C%0A%20%20%20%20%5D)%2C%0A%20%20%20%20%22thread_injection%22%3A%20DataFrame(%5B%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20S0%20%2B%20timedelta(seconds%3D31)%2C%20%22DeviceName%22%3A%20%22WS-DEV-07%22%2C%20%22ActionType%22%3A%20%22CreateRemoteThreadApiCall%22%2C%20%22FileName%22%3A%20%22notepad.exe%22%2C%20%22InitiatingProcessId%22%3A%205444%2C%20%22InitiatingProcessFileName%22%3A%20%22powershell.exe%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20S0%20%2B%20timedelta(minutes%3D2)%2C%20%22DeviceName%22%3A%20%22WS-DEV-07%22%2C%20%22ActionType%22%3A%20%22CreateRemoteThreadApiCall%22%2C%20%22FileName%22%3A%20%22spoolsv.exe%22%2C%20%22InitiatingProcessId%22%3A%205444%2C%20%22InitiatingProcessFileName%22%3A%20%22powershell.exe%22%7D%2C%0A%20%20%20%20%5D)%2C%0A%20%20%20%20%22token_events%22%3A%20DataFrame(%5B%0A%20%20%20%20%20%20%20%20%7B%22_time%22%3A%20S0%20%2B%20timedelta(minutes%3D2%2C%20seconds%3D1)%2C%20%22DeviceName%22%3A%20%22WS-DEV-07%22%2C%20%22ActionType%22%3A%20%22ProcessPrimaryTokenModified%22%2C%20%22InitiatingProcessId%22%3A%205444%2C%20%22InitiatingProcessFileName%22%3A%20%22powershell.exe%22%2C%20%22NewPrivileges%22%3A%20%22SeDebugPrivilege%22%7D%2C%0A%20%20%20%20%5D)%2C%0A%7D%0A%0A%23%20%E2%94%80%E2%94%80%20RBA%20case%20mock%20data%20%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%E2%94%80%0ARBA_T%20%3D%20datetime(2026%2C%203%2C%206%2C%2011%2C%2013%2C%200)%20%20%20%23%20start%20of%20the%20admin%20session%0A%0Aspl._data%5B%22identity_info%22%5D%20%3D%20DataFrame(%5B%0A%20%20%20%20%7B%22AccountUpn%22%3A%20%22alex.reed%40example.com%22%2C%20%22AccountDisplayName%22%3A%20%22Alex%20Reed%22%2C%0A%20%20%20%20%20%20%22AccountName%22%3A%20%22areed%22%2C%20%22Department%22%3A%20%22Platform%20Engineering%22%2C%0A%20%20%20%20%20%20%22JobTitle%22%3A%20%22Senior%20Cloud%20Engineer%22%2C%20%22IsAccountEnabled%22%3A%20%22true%22%2C%0A%20%20%20%20%20%20%22Manager%22%3A%20%22casey.morgan%40example.com%22%2C%20%22GivenName%22%3A%20%22Alex%22%2C%20%22Surname%22%3A%20%22Reed%22%2C%0A%20%20%20%20%20%20%22EmailAddress%22%3A%20%22alex.reed%40example.com%22%2C%20%22AssignedRoles%22%3A%20%22%22%7D%2C%0A%5D)%0Aspl._data%5B%22mde_device_logons%22%5D%20%3D%20DataFrame(%5B%0A%20%20%20%20%7B%22DeviceName%22%3A%20%22MBP-AREED-01%22%2C%20%22logon_count%22%3A%20%2291%22%2C%20%22last_seen%22%3A%20%222026-03-06T12%3A15%3A00%22%2C%0A%20%20%20%20%20%20%22src_ips%22%3A%20%2210.0.10.55%22%2C%20%22logon_types%22%3A%20%22Interactive%22%2C%20%22is_local_admin%22%3A%20%22false%22%7D%2C%0A%5D)%0Aspl._data%5B%22pim_activation%22%5D%20%3D%20DataFrame(%5B%0A%20%20%20%20%7B%22_time%22%3A%20RBA_T%2C%20%22operationName%22%3A%20%22Add%20member%20to%20role%20completed%20(PIM%20activation)%22%2C%0A%20%20%20%20%20%20%22result%22%3A%20%22success%22%2C%20%22category%22%3A%20%22RoleManagement%22%2C%0A%20%20%20%20%20%20%22initiatedBy.user.userPrincipalName%22%3A%20%22alex.reed%40example.com%22%2C%0A%20%20%20%20%20%20%22targetResources%7B0%7D.displayName%22%3A%20%22Cloud%20Application%20Administrator%22%2C%0A%20%20%20%20%20%20%22targetResources%7B0%7D.type%22%3A%20%22Role%22%2C%20%22correlationId%22%3A%20%22a1b2-c3d4%22%7D%2C%0A%5D)%0Aspl._data%5B%22azure_ad_audit_timeline%22%5D%20%3D%20DataFrame(%5B%0A%20%20%20%20%7B%22_time%22%3A%20RBA_T%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22operationName%22%3A%20%22Add%20member%20to%20role%20completed%20(PIM%20activation)%22%2C%20%20%22category%22%3A%20%22RoleManagement%22%2C%20%20%20%22actor_upn%22%3A%20%22alex.reed%40example.com%22%2C%20%22target_name%22%3A%20%22Cloud%20Application%20Administrator%22%2C%20%22result%22%3A%20%22success%22%2C%20%22correlationId%22%3A%20%22a1b2-c3d4%22%7D%2C%0A%20%20%20%20%7B%22_time%22%3A%20RBA_T%20%2B%20timedelta(minutes%3D2)%2C%20%20%20%20%20%20%20%20%20%20%20%22operationName%22%3A%20%22Add%20service%20principal%22%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22category%22%3A%20%22ApplicationManagement%22%2C%20%22actor_upn%22%3A%20%22alex.reed%40example.com%22%2C%20%22target_name%22%3A%20%22Tailscale%22%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22result%22%3A%20%22success%22%2C%20%22correlationId%22%3A%20%22e5f6-a7b8%22%7D%2C%0A%20%20%20%20%7B%22_time%22%3A%20RBA_T%20%2B%20timedelta(minutes%3D3)%2C%20%20%20%20%20%20%20%20%20%20%20%22operationName%22%3A%20%22Add%20application%22%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22category%22%3A%20%22ApplicationManagement%22%2C%20%22actor_upn%22%3A%20%22alex.reed%40example.com%22%2C%20%22target_name%22%3A%20%22Tailscale%22%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22result%22%3A%20%22success%22%2C%20%22correlationId%22%3A%20%22e5f6-a7b8%22%7D%2C%0A%20%20%20%20%7B%22_time%22%3A%20RBA_T%20%2B%20timedelta(minutes%3D5)%2C%20%20%20%20%20%20%20%20%20%20%20%22operationName%22%3A%20%22Update%20application*Certificates%20and%20secrets%20management%22%2C%20%22category%22%3A%20%22ApplicationManagement%22%2C%20%22actor_upn%22%3A%20%22alex.reed%40example.com%22%2C%20%22target_name%22%3A%20%22Tailscale%22%2C%20%20%20%20%20%20%20%22result%22%3A%20%22success%22%2C%20%22correlationId%22%3A%20%22e5f6-a7b8%22%7D%2C%0A%20%20%20%20%7B%22_time%22%3A%20RBA_T%20%2B%20timedelta(minutes%3D6)%2C%20%20%20%20%20%20%20%20%20%20%20%22operationName%22%3A%20%22Add%20owner%20to%20application%22%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22category%22%3A%20%22ApplicationManagement%22%2C%20%22actor_upn%22%3A%20%22alex.reed%40example.com%22%2C%20%22target_name%22%3A%20%22Tailscale%22%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22result%22%3A%20%22success%22%2C%20%22correlationId%22%3A%20%22e5f6-a7b8%22%7D%2C%0A%20%20%20%20%7B%22_time%22%3A%20RBA_T%20%2B%20timedelta(minutes%3D7)%2C%20%20%20%20%20%20%20%20%20%20%20%22operationName%22%3A%20%22Consent%20to%20application%22%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22category%22%3A%20%22ApplicationManagement%22%2C%20%22actor_upn%22%3A%20%22alex.reed%40example.com%22%2C%20%22target_name%22%3A%20%22Tailscale%22%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22result%22%3A%20%22success%22%2C%20%22correlationId%22%3A%20%22e5f6-a7b8%22%7D%2C%0A%5D)%0Aspl._data%5B%22risk_events%22%5D%20%3D%20DataFrame(%5B%0A%20%20%20%20%7B%22_time%22%3A%20RBA_T%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22source%22%3A%20%22Azure%20AD%20PIM%20Role%20Assignment%20Activated%22%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%22risk_score%22%3A%2021.0%2C%20%22risk_message%22%3A%20%22PIM%20activation%20by%20alex.reed%40example.com%22%2C%20%22count%22%3A%202%7D%2C%0A%20%20%20%20%7B%22_time%22%3A%20RBA_T%20%2B%20timedelta(minutes%3D2)%2C%20%20%20%22source%22%3A%20%22Azure%20AD%20Service%20Principal%20Created%22%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22risk_score%22%3A%2020.0%2C%20%22risk_message%22%3A%20%22New%20SP%3A%20Tailscale%22%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22count%22%3A%201%7D%2C%0A%20%20%20%20%7B%22_time%22%3A%20RBA_T%20%2B%20timedelta(minutes%3D5)%2C%20%20%20%22source%22%3A%20%22Azure%20AD%20Service%20Principal%20New%20Client%20Credentials%22%2C%20%20%22risk_score%22%3A%2020.0%2C%20%22risk_message%22%3A%20%22Credentials%20added%20to%20Tailscale%22%2C%20%22count%22%3A%201%7D%2C%0A%20%20%20%20%7B%22_time%22%3A%20RBA_T%20%2B%20timedelta(minutes%3D7)%2C%20%20%20%22source%22%3A%20%22Azure%20AD%20OAuth%20Application%20Consent%20Granted%20By%20User%22%2C%20%22risk_score%22%3A%2017.0%2C%20%22risk_message%22%3A%20%22OAuth%20consent%3A%20openid%20User.Read%20email%22%2C%20%22count%22%3A%201%7D%2C%0A%5D)%0A%0Aclass%20KqlMock%3A%0A%20%20%20%20_data%20%3D%20%7B%7D%0A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20df(**kw)%3A%0A%20%20%20%20%20%20%20%20def%20decorator(fn)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20async%20def%20wrapper(*a%2C%20**kw2)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20table_name%20%3D%20kw2.pop(%22table_name%22%2C%20None)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20df%20%3D%20KqlMock._data.get(fn.__name__%2C%20DataFrame())%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20df.is_empty()%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20df%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20table_name%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20_ddb.create_table(table_name%2C%20df.to_arrow()%2C%20overwrite%3DTrue)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20df%0A%20%20%20%20%20%20%20%20%20%20%20%20wrapper.__name__%20%3D%20fn.__name__%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20wrapper%0A%20%20%20%20%20%20%20%20return%20decorator%0A%0Akql%20%3D%20KqlMock%0Akql._data%20%3D%20%7B%0A%20%20%20%20%22device_processes%22%3A%20DataFrame(%5B%0A%20%20%20%20%20%20%20%20%7B%22Timestamp%22%3A%20T0%2C%20%22DeviceName%22%3A%20%22ws01.corp%22%2C%20%22FileName%22%3A%20%22cmd.exe%22%2C%20%22InitiatingProcessFileName%22%3A%20%22explorer.exe%22%2C%20%22AccountName%22%3A%20%22alice%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22Timestamp%22%3A%20T0%20%2B%20timedelta(minutes%3D1)%2C%20%22DeviceName%22%3A%20%22ws03.corp%22%2C%20%22FileName%22%3A%20%22powershell.exe%22%2C%20%22InitiatingProcessFileName%22%3A%20%22svchost.exe%22%2C%20%22AccountName%22%3A%20%22SYSTEM%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22Timestamp%22%3A%20T0%20%2B%20timedelta(minutes%3D3)%2C%20%22DeviceName%22%3A%20%22ws01.corp%22%2C%20%22FileName%22%3A%20%22net.exe%22%2C%20%22InitiatingProcessFileName%22%3A%20%22powershell.exe%22%2C%20%22AccountName%22%3A%20%22bob%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22Timestamp%22%3A%20T0%20%2B%20timedelta(minutes%3D7)%2C%20%22DeviceName%22%3A%20%22ws03.corp%22%2C%20%22FileName%22%3A%20%22rundll32.exe%22%2C%20%22InitiatingProcessFileName%22%3A%20%22svchost.exe%22%2C%20%22AccountName%22%3A%20%22SYSTEM%22%7D%2C%0A%20%20%20%20%20%20%20%20%7B%22Timestamp%22%3A%20T0%20%2B%20timedelta(minutes%3D11)%2C%20%22DeviceName%22%3A%20%22ws01.corp%22%2C%20%22FileName%22%3A%20%22svchost.exe%22%2C%20%22InitiatingProcessFileName%22%3A%20%22services.exe%22%2C%20%22AccountName%22%3A%20%22SYSTEM%22%7D%2C%0A%20%20%20%20%5D)%2C%0A%7D%0A

 
 

Here is a Splunk query. The function returns SPL, and the decorator declaration specifies the expected output columns and their types. Thert()helper resolves relative time expressions such as"-1h"and"now"into the bounded time window that the decorator requires:

 
 
 

Loading…

 
 

%40spl.df(schema%3D%7B%0A%20%20%20%20%22_time%22%3A%20%22ts%22%2C%0A%20%20%20%20%22host%22%3A%20%22str%22%2C%0A%20%20%20%20%22dest_domain%22%3A%20%22str%22%2C%0A%20%20%20%20%22bytes_out%22%3A%20%22int%22%2C%0A%20%20%20%20%22category%22%3A%20%22str%22%2C%0A%7D)%0Aasync%20def%20proxy_events()%3A%0A%20%20%20%20return%20%22%22%22%0A%20%20%20%20search%20index%3Dwebproxy%20host%20IN%20(%22ws01.corp%22%2C%20%22ws03.corp%22)%0A%20%20%20%20%7C%20table%20_time%2C%20host%2C%20dest_domain%2C%20bytes_out%2C%20category%0A%20%20%20%20%22%22%22%0A%0Aevents%20%3D%20await%20proxy_events(%0A%20%20%20%20earliest_time%3Drt(%22-1h%22)%2C%0A%20%20%20%20latest_time%3Drt(%22now%22)%2C%0A%20%20%20%20table_name%3D%22proxy_events%22%2C%0A)%0Amo.ui.table(%0A%20%20%20%20events%2C%0A%20%20%20%20page_size%3D5%2C%0A%20%20%20%20selection%3DNone%2C%0A)%0A

 

The@spl.dfdecorator. The function returns SPL, the decorator
runs the search and casts every column according to the declared column types.
The decorator readsearliest_timeandlatest_timefrom call-time kwargs and enforces that both are set, so every remote search
has a bounded time window. The same function can then run over a short triage
window or a longer retroactive hunt. In this notebook the backend is ibis, so
the result is available as a table in the shared DuckDB connection.

Production notebooks usually declare column types with short strings such as"ts","str","int", and"float". The declaration does two things at once: it casts Splunk’s untyped JSON into proper column types, and it surfaces drift loudly. A Splunk index can contain multiple event categories, so a query that used to return one field set can suddenly include another category’s fields too. With an explicit declaration, that mismatch shows up as a cast error on the next run instead of as silently null columns downstream.

Those strings are deliberately backend-agnostic. Under the hood, the SDK maps each one onto the right dtype for the active tabular backend, so"ts"becomes the timestamp type that Polars, pandas, PyArrow, or ibis expects. That keeps the notebook code stable while the return type changes underneath it.

When exploring an unfamiliar index where the field set is unknown, the SDK can infer it once: it runs| fieldsummaryover a narrow time window and passes the result to apydantic-aiagent backed by a small LLM (for example, Haiku) with two tools -try_castto verify a guessed dtype against sample values, andcheck_datetimeto confirm a string parses as a timestamp. Inferred declarations are cached persistently so the LLM round trip happens once per index.

Inferring column types once. A narrow-window| fieldsummaryhands the agent each field with sample values, the agent proposes a type and
checks it withtry_castandcheck_datetime, and the
confirmed declaration is cached so the model runs once per index rather than
on every query. Hover a node for details.

Same pattern for KQL. Advanced hunting in Microsoft Defender XDR (and Microsoft Sentinel) returns typed responses via the Microsoft Graph security API, so no schema declaration is needed:

 
 
 

Loading…

 
 

%40kql.df()%0Aasync%20def%20device_processes()%3A%0A%20%20%20%20return%20%22%22%22%0A%20%20%20%20DeviceProcessEvents%0A%20%20%20%20%7C%20where%20DeviceName%20in%20(%22ws01.corp%22%2C%20%22ws03.corp%22)%0A%20%20%20%20%7C%20project%20Timestamp%2C%20DeviceName%2C%20FileName%2C%20InitiatingProcessFileName%2C%20AccountName%0A%20%20%20%20%7C%20take%20200%0A%20%20%20%20%22%22%22%0A%0Adevices%20%3D%20await%20device_processes(%0A%20%20%20%20earliest_time%3Drt(%22-1h%22)%2C%0A%20%20%20%20latest_time%3Drt(%22now%22)%2C%0A%20%20%20%20table_name%3D%22devices%22%2C%0A)%0Amo.ui.table(%0A%20%20%20%20devices%2C%0A%20%20%20%20page_size%3D5%2C%0A%20%20%20%20selection%3DNone%2C%0A)%0A

 

@kql.dfagainst advanced hunting in Microsoft Defender XDR. The
SDK infers types from the Graph API response. With the ibis backend selected,
the result lands in the same DuckDB connection as the Splunk table above.

For SQL-like analytical sources, there is no decorator. The client runs the source’s native query path, receives a result set, converts it through Arrow, and hands the notebook the configured tabular type:

 
 
 

Loading…

 
 

remote_result%20%3D%20sf.table(%22assets.vulnerability_findings%22).filter(%0A%20%20%20%20ibis._.cvss_score%20%3E%3D%207.0%2C%0A%20%20%20%20ibis._.host.isin(%5B%22ws01.corp%22%2C%20%22ws03.corp%22%5D)%2C%0A).select(%22host%22%2C%20%22cve_id%22%2C%20%22cvss_score%22%2C%20%22severity%22%2C%20%22owner_team%22)%0A%0Avulns%20%3D%20ddb_table(%22vulns%22%2C%20remote_result.to_pyarrow())%0A%0Amo.ui.table(%0A%20%20%20%20vulns%2C%0A%20%20%20%20page_size%3D5%2C%0A%20%20%20%20show_search%3DFalse%2C%0A%20%20%20%20selection%3DNone%2C%0A)%0A

 

sf.table()represents the SQL-source path. The remote system does
the database work, the result set comes back through Arrow, and the notebook
continues with the same dataframe or table interface used for the
security-platform results above.

## Async jobs, parallel fan-out, and caching

A oneshot Splunk search (@spl.df) uses the HTTP search endpoint and can time out on larger queries. Heavier searches, such as fleet-wide aggregations over endpoint telemetry, may need to run as server-side Splunk jobs. The SDK exposes both shapes as@spl.dfand@spl.job. The decision is simple:@spl.dffor the fast majority,@spl.jobfor anything that would time out or return more than a few thousand rows.@spl.jobalso surfaces a nested marimo progress bar so the analyst can see the search advance rather than stare at a spinning cell.

Two Splunk execution paths. Fast searches use the synchronous endpoint and
return rows directly. Longer searches create a server-side job, poll until the
job is done, page through the result set, and update a marimo progress bar
while the notebook waits.

Both decorators are async-native, so multiple jobs run concurrently withasyncio.gatherfrom the standard library. The RBA worked example below fans out across identity context, PIM history, device logons, the Azure AD audit timeline, and CMDB context indexed in Splunk. Serially that can take minutes. Withgather, the notebook waits as long as the slowest single fetch.

Caching remote queries.marimo’s reactive execution model is exactly what we want for investigation notebooks: change a widget, and every dependent cell updates. The catch is that a dependent cell may be a Splunk search, and moving a dropdown or slider should not submit the same remote query ten times. One-shot searches may time out quickly, async jobs may live only for a short period, and a case notebook gets re-run constantly while the analyst is working.

To guard against that, the SDK leans on marimo’s caching mechanics around the remote fetch boundary. marimo’s cache supports async functions, preserves cached values across cell re-runs unless the relevant source code changes, and keys on function arguments plus closed-over variables. In our case, that means the fetch cache can account for the Python cell definition, the resolved time window, the native query string, and the relevant execution options. A stable investigation window can be re-used across reactive re-runs, while changing the query function or asking for a genuinely different window goes back to the source.

The cache boundary in a reactive notebook. A widget change can re-run
downstream cells many times, but the remote fetch cell only goes back to
Splunk when the function definition, query, options, or resolved time window
changes. Cache hits let the rest of the notebook update without submitting
another remote search.

The tricky part is relative time. Splunk’s native time syntax uses expressions like"-24h"or"-7d@d". If you cache based on those strings, the key"-24h"hashes to the same value regardless of when the query actually ran. The analyst reopens their notebook the next morning, the cache hits, and they get yesterday’s data without any indication that it is stale.

The SDK addresses this withrt(), a function that resolves relative time expressions to absolute UTC timestamps at the moment of invocation. Same query, different hour, different cache entry:

# BAD: the string "-1h" never changes, so the cache key never changes

await connections(earliest_time="-1h", latest_time="now")

# GOOD: rt() resolves to an absolute timestamp at call time

await connections(earliest_time=rt("-1h"), latest_time=rt("now"))

The cell below illustrates the behavior using the mock SDK. The mocked remote boundary sleeps on a cache miss, then returns immediately on a hit. Both calls use identical resolved timestamps, so the second call finds the memory cache entry instead of submitting another search:

 
 
 

Loading…

 
 

 

Cold call versus cache hit. The demo uses a short artificial sleep to make the
remote boundary visible. In production the cold call can take seconds against
a loaded Splunk index, while the hit returns from local cache. The point is
the boundary: remote data is fetched once for a resolved window, then
downstream reactive cells can re-run without re-querying Splunk.

The SDK also raises an explicit error iflatest_timeis in the future: caching a window that has not yet closed would store incomplete results. And if you accidentally pass an unresolved relative string like"-24h"when caching is on, you get a warning in the console - the cache key would be the literal string, meaning it would never refresh. Thert()call is the guard.

Working the data locally.At this point the remote systems have already done their work. Splunk has returned proxy events, Defender XDR has returned process activity, and Snowflake has returned vulnerability findings. The SDK has landed each result as an ibis table backed by the same local DuckDB connection, so the investigation now continues entirely on local data. There is no further Splunk search or cross-product export to run. From here it is ordinary notebook work: join the tables on a shared key, filter and aggregate, and wire the result to interactive widgets that recompute reactively as the analyst drills in. The first move is the join, correlating the three sources on hostname:

 
 
 

Loading…

 
 

investigation%20%3D%20(%0A%20%20%20%20vulns.join(events%2C%20vulns.host%20%3D%3D%20events.host)%0A%20%20%20%20%20%20%20%20%20.join(devices%2C%20vulns.host%20%3D%3D%20devices.DeviceName)%0A%20%20%20%20%20%20%20%20%20.select(%0A%20%20%20%20%20%20%20%20%20%20%20%20%20vulns.host%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20vulns.cve_id%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20vulns.cvss_score%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20events.dest_domain%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20events.bytes_out%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20devices.FileName%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20devices.AccountName%2C%0A%20%20%20%20%20%20%20%20%20)%0A)%0Ainvestigation%20%3D%20ddb_table(%22investigation%22%2C%20investigation.to_pyarrow())%0Amo.ui.table(investigation%2C%20page_size%3D5%2C%20show_search%3DFalse%2C%20selection%3DNone)%0A

 

Three sources joined on hostname. Vulnerability findings from Snowflake
correlated with proxy traffic from Splunk and process activity from Defender
XDR. The join runs locally in DuckDB after the remote fetch boundary, which
means downstream cells can filter, aggregate, and display the result without
going back to the source systems.

Because marimo is reactive, adding a filter widget requires no callback wiring. The dropdown is a Python variable in the reactive DAG. Select a host and every downstream cell that depends on the joined table re-evaluates automatically:

 
 
 

Loading…

 
 

 

The filtered join for a single host. The shape of a playbook: pull from
multiple sources, join on a shared key, let the analyst drill down without
writing additional query logic.

## Worked examples

The three example notebooks below demonstrate the SDK, each built around a different analysis shape: a hash join against a threat intel feed, a temporal correlation across separate telemetry searches, and a parallel fan-out for identity and case context. The data, hostnames, identities, and verdicts in all three are synthetic.

 
 
 BYOVD driver hunting 
 Sliver C2 detection 
 RBA case triage 
 
 
 

Bring Your Own Vulnerable Driver attacks use legitimate but vulnerable kernel drivers to disable security tooling.LOLDriversmaintains a community-curated database of these drivers as SHA256 hashes. The hunting pattern: pull driver load telemetry, match against LOLDrivers, investigate anything that hits.

The smallest viable hunt loop: an external threat-intel feed (LOLDrivers)
joined against fleet driver-load telemetry. What matters in the diagram is
that neither source needs special treatment: the CSV reads into Polars, the
telemetry query returns a Polars dataframe, and the join happens inside the
notebook. No ETL into a security data lake first.

Load threat intelligence.Pull the LOLDrivers hash list into a local polars DataFrame. The reference set we match our telemetry against:

 
 
 

Loading…

 
 

 
 

The full LOLDrivers CSV contains over two thousand entries across vulnerable, malicious, and known-abused categories. Here we show a subset for clarity.

Query telemetry.Next, query Splunk for driver load events from Defender for Endpoint telemetry. Rather than pulling every raw event (millions of rows across a fleet), we run an aggregation that returns unique SHA256 hashes with load counts and device spread:

 
 
 

Loading…

 
 

 
 

Thestatscommand deduplicates at the hash level. Thousands of drivers load daily across the fleet, but we only compare unique hashes against LOLDrivers. Individual events come later, once we have a confirmed hit.

Join and identify hits.Join on SHA256. Anything that survives is a driver loaded in our environment that matches a known-vulnerable sample in LOLDrivers:

The join logic as a set intersection. LOLDrivers ships around two thousand
known-vulnerable and known-abused driver entries. The fleet loads a few
thousand distinct drivers a week. The intersection (highlighted) is what we
care about: drivers that are both loaded in our environment and catalogued as
vulnerable.

 
 
 

Loading…

 
 

 
 

One hit: truesight.sys, a known EDR killer catalogued by LOLDrivers. The same
join pattern works regardless of where your telemetry lives - swap the
data-retrieval decorator and the rest stays the same.

Drill down.Confirmed hit. Drill down on that hash to pull the raw load events - device name, folder path, initiating process - the context needed to decide whether this is malicious or a false positive:

 
 
 

Loading…

 
 

 
 

The driver loaded from C:\Windows\Temp on a single device, a non-standard path
for a kernel driver. Combined with the LOLDrivers match, a vulnerable signed
driver staged in a temp directory and loaded as a kernel service is the BYOVD
pattern, not a legitimate driver update. The specific event values here are
LLM-generated for illustration, since real telemetry is confidential. This
mirrors the shape of the production hunt in our environment: the LOLDrivers
community feed joined against endpoint driver-load telemetry, the join running
locally in DuckDB, with a click-to-investigate drilldown for each hit.

 

Sliver’sGetSystemprivilege escalation injects a remote thread into a SYSTEM-owned service (spoolsv.exe), which grants the implant’s token SeDebugPrivilege. Neither half is suspicious alone - cross-process thread creation happens legitimately, and SeDebugPrivilege is granted during normal UAC elevation. The detection, following Microsoft’sown hunting guidance, fires when both happen on the same device and PID within 30 seconds.

This notebook implements that temporal join over endpoint telemetry. One side looks for remote thread injection intospoolsv.exe. The other looks for a matching privilege change that grants SeDebugPrivilege. DuckDB joins them on device and process with a 30-second window. The point is doing the temporal correlation in the notebook rather than as a monolithic SPL.

The GetSystem technique as a sequence. The implant (powershell.exe, PID 5444)
injects a remote thread into spoolsv.exe, a SYSTEM-owned service. This causes
spoolsv to grant SeDebugPrivilege back to the initiating process. The dashed
box marks the detection surface: the same device and process appearing in both
a thread-injection event and a privilege-change event within 30 seconds.

Process creation chain.Full process creation chain for the host under investigation. NoticeAccountNametransitions fromsarah.chentoSYSTEMbetween the implant process and the post-escalation cmd.exe - that is the privilege escalation boundary:

 
 
 

Loading…

 
 

 
 

Classic phishing-to-C2 chain: WINWORD.EXE spawns powershell.exe (the implant), which spawns notepad.exe (sacrifice process) and eventually cmd.exe running as SYSTEM.

Thread injection events.Remote thread injection events for the implant process:

 
 
 

Loading…

 
 

 
 

Two injections from the same implant process. The notepad injection is a sacrifice process for Sliver’s Execute-Assembly (injects a .NET assembly into a throwaway process to avoid loading the CLR into the implant). The spoolsv injection is GetSystem - that is the one we care about.

Token manipulation.Privilege-change events for the same process. SeDebugPrivilege appears as the only privilege change:

 
 
 

Loading…

 
 

 
 

The Microsoft hunting guide checks specifically for SeDebugPriv being theonlychange in the modified privilege set, because that is how Sliver implements GetSystem.

Temporal join.The detection logic: filter to injections targeting spoolsv, join with token grants on PID, enforce the 30-second window. If a row survives all three conditions, GetSystem succeeded:

 
 
 

Loading…

 
 

 
 

One row returned: PID 5444 injected into spoolsv.exe and received
SeDebugPrivilege 1 second later. The detection fires here. Neither event alone
would be suspicious, but the combination within a tight time window on the
same PID is the signal.

 

Risk-Based Alerting aggregates individual detections against the same identity into a single scored notable. A case fires not because one detection crossed a threshold but because several weaker signals converged on the same user. The notebook’s job is to resolve those signals into a verdict: is this a threat, a misuse case, or a legitimate but noisy admin session?

This case shows Case #4821, where four Azure AD detections fired againstalex.reed@example.com(Platform Engineering) in a 7-minute window. Risk score: 78. The fan-out runs five context queries in parallel: identity, PIM activation history, device logons, the Azure AD audit timeline, and the user’s CMDB record indexed in Splunk. All run with persistent caching so re-running the notebook during the investigation pulls from EFS rather than re-hitting Splunk. The cells below walk through the first four.

In the full notebook, the contributing-rules table at the top is interactive: clicking a row spawns another Splunk search that fetches both the detection’s macro definition (the SPL behind the rule, with macros expanded) and the raw events that triggered the score on this case. The drilldown is rewritten on the fly to scope it to the risk object and window, then cached so the second click is instant.

Identity context.Resolve who the risk object is before looking at any events. The identity feed carries the user’s current department, job title, and manager. This query is cached persistently - the identity record does not change during a single investigation:

 
 
 

Loading…

 
 

 
 

The identity record foralex.reed@example.com. Department, job title, and
manager are the first context check: does this person have a legitimate reason
to be performing Azure AD operations? A Platform Engineering senior cloud
engineer does - this alone is not conclusive but sets the prior.

PIM activation history.PIM (Privileged Identity Management) gates access to high-privilege directory roles. Check whether the user activated an appropriate role before the Azure AD operations fired. The role name tells you what level of access was obtained:

 
 
 

Loading…

 
 

 
 

One PIM activation: Cloud Application Administrator at 11:13 UTC, 2 minutes
before the service principal operations begin. The expected control flow for
an engineer without standing admin rights, who has to request a time-limited
role, perform the work, and let the role expire. A mismatch here (wrong role,
activation after the operations, or no PIM at all) would be a strong red flag.

Device confirmation.Confirm the user’s registered workstation was active during the window. Device logon telemetry provides activity for the account. A foreign device or no device activity at the time of the Azure AD operations would shift the assessment:

 
 
 

Loading…

 
 

 
 

MBP-AREED-01, Alex’s registered MacBook, logged 91 sessions and was last seen
at 12:15 UTC - 62 minutes after the first PIM activation. The logon count is
consistent with an active work session, not a single targeted intrusion. If
the device were unknown to CMDB or had no MDE presence, the investigation
would go in a different direction.

Full audit timeline.Pull the complete Azure AD audit record for the session: all service principal, credential, consent, and PIM operations in chronological order. The sequence and correlationId clustering tell you whether this was one coherent session or operations spread across time:

 
 
 

Loading…

 
 

 
 

Six operations in 7 minutes under a single correlationId prefix, beginning
with the PIM activation. The sequence is PIM activation, service principal
creation, application registration, credential addition, owner grant, OAuth
consent - the expected provisioning order. Deviations from this sequence
(credentials before SP creation, consent without a matching SP, operations
hours apart) are the adversarial patterns to look for. All six operations
target Tailscale, consistent with an engineer registering an application to
set up the VPN. Verdict: high confidence benign, close with a brief
confirmation from the engineer.

 
 

The notebooks these demos illustrate are the same shape as the production hunts and triage workflows we run. Once the notebook is useful, the next question is how it becomes a shared operational surface rather than a file on one analyst’s machine.

## Deployment

Up to here the notebook has behaved like a local, single-user workspace: one analyst, one running notebook, one investigation. Turning that into a team tool raises a different question: how do you run the same notebook remotely so several people can reach it, and so notebooks and session state persist between runs and survive a restart?

We kept the answer deliberately simple. Everything runs on a single ECS cluster, and four services mount the same S3 bucket throughS3 Filesaccess points, so a file one service writes is immediately visible to the others. That shared storage is what lets one.pyfile move between the analyst workspace, a remote app view, and an agent-driven session without a deploy pipeline in between. Themarimoanddashboardsservices run notebook edit mode and app mode, covered in the next section. The other two,claude-tmuxandclaude-agent, are the agent interface, covered after that.

The shared storage topology. ECS services mount S3 Files access points and an
EFS volume. A notebook written by the agent task appears immediately in the
marimo UI. Session state persists on EFS across container restarts. The shared
mount is what lets the agent and the editor share state without an explicit
sync step. Hover a node for details.

S3 lifecycle policies make retention explicit: cached investigation data can be kept for a fixed maximum window, then expired automatically. The editor service is the shared runtime for notebook editing and agent pairing, with access controlled at the internal service boundary. Individual notebooks are accessed by URL path. The agent containers also carry Bedrock IAM permissions for model inference.

View mode.marimo’sview modelets a second user open the same notebook as a live read-only viewer without disconnecting the first. The viewer sees the editor’s cells and outputs update in real time, and either side can take over editing with one click. In practice this is how a second analyst or a team lead follows an investigation as it is being built. The important distinction is local versus remote use: the notebook remains one.pyfile, but the remote runtime lets several people and the agent share the same live state.

## Data apps

The same file also needs to work outside edit mode: as a live shared view, a focused app, or an exported report. marimo’sapp mode(marimo run) hides the code and lays out the cell outputs as a web application. We don’t runmarimo rundirectly. Thedashboardsservice is a thin FastAPI app that mounts marimo’sASGI appat/, withwith_dynamic_directorypointing at the dashboards S3 mount:

import marimo

from fastapi import FastAPI

server = marimo.create_asgi_app().with_dynamic_directory(

 path="/dashboard", directory="/app/dashboards"

)

app = FastAPI()

@app.get("/health")

async def health_check():

 return {"status": "healthy"}

app.mount("/", server.build())

The dashboards service is deliberately thin. FastAPI owns health checks and
process lifecycle, while marimo owns routing each notebook file to an app. The
dynamic directory points at the shared dashboards mount, so the served set can
change without restarting the container.

with_dynamic_directoryserves every.pyfile under the directory as its own app, discovered at request time rather than at boot. Drop a new file into the mount and it is live at the next URL hit. No rebuild, no restart, no registration. The container’s job is to be the runtime.

The trick is that the editor and the app read the same bucket. Themarimoservice mounts both access points (/app/notebooksfor working drafts,/app/dashboardsfor what gets served), while thedashboardsservice mounts only/app/dashboards. Because the editor can write directly into/app/dashboards, an analyst can edit a served notebook in place from the marimo instance andwith_dynamic_directorypicks up the change on the next request. There is no separate move, build, or deploy step. A notebook becomes an app the moment it lands in/app/dashboards, whether you edit it there directly ormvit across from/app/notebooks.

This shared mount is the convenient path, not the only one. The version-controlled data apps ship inside the container image, copied in when we rebuild it from GitHub, so the versioned set is always present on boot. The S3 mount sits on top of that as a fast self-service layer: an analyst can work on a notebook in the marimo editor and have it served as an app moments later, without waiting on an image build.

Two ECS services, one S3 bucket. The marimo editor mounts both access points,
the dashboards FastAPI app mounts only the dashboards one. Because the editor
can write to the dashboards mount, editing a notebook there serves it as an
app directly, with no move or deploy step.with_dynamic_directorypicks the file up on the next request.

The reactive execution model makes each served notebook more than a fixed dashboard. URL query parameters feed directly into the reactive DAG viamo.query_params(). The process tree notebook reads its scope from the URL:

query_params = mo.query_params()

device_name = query_params.get("device_name")

report_id = query_params.get("report_id")

process_id = query_params.get("process_id")

anchor_time = pendulum.parse(query_params.get("timestamp")).naive()

The app reads its scope from the URL. Those values become ordinary Python
variables in the reactive graph, so changing the URL parameter changes the
queries, joins, and visualizations that depend on it. The calling system only
needs to construct the link.

For app mode, the integration can be as simple as a URL. Any system that can construct a link can drive the app: change the device name in the URL and every SQL query, every join, every visualization downstream re-executes with the new scope. The analyst sees a pre-focused view of their case without touching code, and the calling system does not need to know anything about notebook internals. SOAR is one useful caller and context source: a playbook can build the case URL, pass the case identifier, and open the notebook already scoped to that incident.

Two such apps are below: the process tree explorer and the RBA case triage we just saw in notebook mode. The process tree app takes a device and timestamp from the URL and renders an interactive tree of process creation events. The RBA app takes a case ID and presents the full risk-based alert case in one view.

 
 
 Process tree explorer 
 RBA case triage 
 
 
 

The process tree app resolves the boot session from the timestamp, pulls all process creation events from Defender XDR, and renders an interactive tree with the anchor process highlighted. Selecting a node triggers reactive execution: downstream cells that show image loads, file writes, network connections, and registry modifications re-evaluate for the selected process. Click any node and choose “Load events” to see this in action.

Open in new tab

Process Tree Explorer. The header shows incident context (device, user, boot
session). The tree visualizes the full process hierarchy with the anchor
process highlighted. Click any node for detailed telemetry in the tabbed panel
below. This is a single marimo notebook running in app mode, using the same
ProcessTreeWidget from aprevious post.

 

The same Case #4821 from the worked example, in app mode. The app receives?case_id=4821, uses that identifier to fetch context from five sources in parallel (including SOAR), and drives all downstream queries from that single parameter. Risk-based alerting aggregates signals from many detection rules into a single case, and the app presents the full case in one view rather than five.

Open in new tab

RBA Case Triage in app mode, showing the same Case #4821 as the worked
example. The header carries the risk-object and device badges, the enrichment
panel aggregates context from Splunk ES, Defender XDR, Azure AD, CMDB data
indexed in Splunk, and SOAR, and the risk rules table shows each of the five
Azure AD detections that contributed to the score. Select a row to inspect the
SPL and the raw audit events. The analyst assesses the full case without
switching consoles.

 
 

## Agent interface

The last layer is the agent loop: not a separate interface, but another way to work inside the same notebook. One idea recurs across notebook-driven security operations: a templatized investigation notebook for each alert type, with its visualizations, cells, and runbook steps laid out in advance. When the alert fires, the notebook auto-fills and runs, and the analyst takes over from there.

Apple described a version of this in a 2019 presentation on their threat detection and response notebooks, and Microsoft’sMSTICPyhas long packaged the query, enrichment, and visualization building blocks for exactly this kind of investigation notebook.

In practice this is a lot to keep up. There are too many distinct signals and too much of the investigation is ad hoc, so a catalogue with one notebook per alert type drifts as detection rules evolve and becomes its own maintenance load.

The agent changes that. Instead of maintaining a template per alert, we give the agent skills and domain knowledge and let it build a case-specific notebook from scratch each time. The analyst inherits a working draft shaped to the alert rather than a stale generic template.

Two additional ECS services on the same cluster: a headless RunTask for automated builds, and a persistent tmux session for interactive use. Both mount S3 (so agent-built notebooks appear immediately in the editor) plus EFS at/home/nonroot/.claudefor session state. Conversation history, memory, and project configuration persist across container restarts and are shared between services. This shared EFS is what enables the handoff -/resumepicks up where the headless agent left off.

### The notebooks plugin

marimo-pairis the transport layer: a Claude Code skill, in practice a handful of shell scripts, that gives the agent direct control of a running notebook (add cells, execute, read outputs, delete). The scripts speak to the marimo server’s ordinary HTTP API rather than any custom protocol. To run code, a script finds the server in marimo’s local registry, looks up the active notebook session, and POSTs the code to the kernel’s execute endpoint tagged with that session id.

marimo runs the code in the real kernel and streams back stdout, stderr, and a final result or error, which the script returns to the agent. Adding, reading, and deleting cells work the same way. The effect is that the agent operates the notebook through the same kernel the analyst’s editor uses and sees the actual outputs, exactly as a person typing into a cell would. The walkthrough at the top of the post is this loop running on a simplified scenario triggered on a laptop, since real cases are confidential.

That assumes a notebook session already exists, which holds when an analyst has the editor open but not on a headless ECS task that starts cold. Ournotebooks plugincloses that gap. The admin skill handles the server lifecycle, file operations, exports, and session bootstrap that marimo-pair leaves out, so the agent can start with no analyst present. The rest of the plugin is domain guidance for the stack the agent writes against: SPL and ibis query patterns, marimo widgets and layout, investigation structure, and validation gates.

How the agent works inside one notebook. It reads the domain skills for what
to build (investigation structure, SPL and ibis patterns, display idioms, RBA
drilldowns), then acts: marimo-pair adds and runs cells on the HTTP kernel and
reads their output, while the admin skill handles files and sessions over REST
and WebSocket. The agent repeats this build, run, and inspect loop, revising
as it reads outputs, until the validate gate confirms the notebook is
complete. Hover a node for details.

The notebooks plugin structure. Skills define agent workflows as markdown
instructions. The admin skill handles server lifecycle, especially ensuring
marimo is running before attempting cell operations. References hold SDK
patterns and investigation templates. Hover a node for details.

marimo-pair knows how to write cells to a live kernel. The notebooks plugin knows what cells to write and in what order. The video at the top of the post shows the two layered together on a simplified, self-triggered scenario rather than a live case.

The handoff is easier to see as one shared runtime. A case system supplies alert context, a headless agent creates the first notebook, and the analyst takes over without losing the notebook state or the agent session. There are two human-facing branches: open the notebook in the marimo editor through the browser, or reconnect to the same Claude Code session throughttydandtmuxwith/resume. The editor talks to the live marimo kernel directly, while the interactive agent uses the same marimo-pair transport and notebooks plugin as the headless run.

The agent handoff. The top lane is the automated first draft: a case system
passes context into a dispatcher, the dispatcher starts a headless agent, and
the agent writes a case notebook. The bottom lane is human takeover: the
analyst opens the notebook in marimo and can also resume the agent throughttydandtmux. The browser path and the
interactive-agent path both work against the same live marimo kernel. The
implementation details matter less than the state boundary: notebook files and
agent session state have to survive the handoff.

The notebook is the right artifact when the analyst is likely to continue working - add cells, drill down, test another hypothesis, write a verdict. Every cell’s output is reproducible, so the notebook is also evidence that the agent did what it claims. For finished reports, marimo exports to static HTML, and for some workflows a custom HTML page may be the better final surface. The important distinction is whether the investigation should remain executable after the first draft.

## Summary

In this post we built an agentic incident response workflow around marimo. The goal was not to replace the security tools analysts already use, but to give incident response, threat hunting, and threat intelligence work a better execution surface: one case notebook where data access, analysis, evidence, explanation, and agent assistance can meet.

The first piece is data access in the form analysts actually use it. Splunk queries stay SPL, Defender XDR queries stay KQL, and analytical sources such as Snowflake keep their native interfaces. The SDK wraps those queries and returns typed tables, usually backed by DuckDB through ibis, so the notebook can join and filter results from multiple systems locally.

The second piece is the notebook as a stateful case artifact. The same.pyfile can run locally while an analyst explores, in a shared runtime while another person follows the live notebook, as an app when the case needs a focused interface, and as static HTML when the work should be archived. The important part is not the hosting arrangement. It is that code, outputs, widgets, cached remote results, and the analyst’s explanation stay attached to the same executable file.

The third piece is the agent handoff. marimo-pair gives the agent access to the live notebook kernel: it can add cells, execute them, read outputs, and revise. The notebooks plugin adds the domain knowledge around SPL, ibis, marimo layout, investigation structure, and validation gates. A headless run can produce the first draft, and the analyst can continue either in the browser editor or by resuming the same agent session. That continuity is the point: the notebook state and the agent state both survive the handoff.

The examples show the same pattern in several shapes: a BYOVD hash join against LOLDrivers, a temporal Sliver C2 correlation, risk-based alert triage, process-tree exploration, and an agent-built case notebook. The common thread is that the notebook stays close to the evidence. It is not only a report at the end of the investigation. It is the place where the investigation runs, where the intermediate joins and filters remain visible, and where the next question can still be asked.

There is an open design question here. Coding agents are very good at writing custom HTML, and for some case views that may be the fastest route: run the searches, render the result into a focused page, and give the analyst a polished interface. That can be enough when the artifact is mostly a view of results. The notebook approach makes a different tradeoff. Because the query code, transformations, outputs, and conclusion live in the same executable file, the case is reproducible in a way that a custom HTML view over already-materialized Splunk or Databricks results is not. The strategic question is whether the artifact is a finished view or the live investigation surface: executable, inspectable, resumable, and easy to extend.

There are still limitations. Agent-built notebooks are drafts, not verdicts, and need human review before conclusions are acted on. Isolation is still coarse, with cases sharing services at the directory level rather than running isolated per case, and the schema knowledge base has to be maintained as sources and parsers change. The natural end state is closer to a managed marimo workspace such asmolab: configurable runtimes, per-case isolation, persistent storage, sharing, agent pairing, and clean spin-up, spin-down, and archive semantics around each case.

## References and related work

* Scaling Security Threat Detection with Apache Spark and Databricks- Josh Gillner (Apple), Spark+AI Summit. An early public description of notebook-as-investigation-artifact at scale.
* MSTICPy- Microsoft’s Python toolkit of query, enrichment, and visualization building blocks for security investigation notebooks.
* marimo- reactive Python notebook.
* marimo-pair- agent interface for programmatic notebook construction.
* marimo case study: DNB- earlier write-up of parts of this work on the marimo blog.
* ibisandDuckDB- dataframe API and in-process query engine.
* narwhals- backend-agnostic tabular compatibility layer.
* LOLDrivers- community-curated database of vulnerable and malicious Windows drivers.
* Looking for the Sliver lining- Microsoft’s analysis of the Sliver C2 framework.
* anywidget- the framework behind ProcessTreeWidget, covered in aprevious post.
* S3 Files for Amazon ECS- persistent storage mount for hot-deploying notebooks.
 
* #incident-response
* #marimo
* #ibis
* #duckdb
* #splunk
* #kql
 
 
 
 
×