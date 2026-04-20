---
title: Apache Airflow 3.2.0: Data-Aware Workflows at Scale | Apache Airflow
url: https://airflow.apache.org/blog/airflow-3.2.0/
date: 2026-04-12
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-12T06:03:57.801317
---

# Apache Airflow 3.2.0: Data-Aware Workflows at Scale | Apache Airflow

# Apache Airflow 3.2.0: Data‑Aware Workflows at Scale – Summary

## Overview
- Release date: Tue Apr 7 2026.
- Highlights: Asset partitioning, multi‑team deployments, synchronous deadline‑alert callbacks, continued Task SDK separation.
- Primary goal: Enable more granular, enterprise‑scale, and data‑aware orchestration.

## Asset Partitioning (AIP‑76)
- Introduces partition‑driven scheduling: downstream DAGs fire only when the specific data partition they depend on changes.
- Key components:
  - **CronPartitionTimetable** – schedule DAGs by cron‑based partitions (also usable in Task SDK).
  - **Backfill for partitioned DAGs** – allows historical partition processing without re‑triggering downstream work.
  - **Multi‑asset partitions** – a single DAG can listen to partitions from multiple assets, enabling coordinated triggers.
  - Advanced tools: temporal/range partition mappers, partition key field on DAG run, and **PartitionedAssetTimetable** for custom resolution of multiple asset events.
- Example use case: three hourly ingestion DAGs write to separate assets; a downstream “combine” DAG runs only when all three assets have updated the same hourly partition.

## Multi‑Team Deployments (AIP‑67) – Experimental
- Allows isolated teams within one Airflow deployment, each with its own DAGs, connections, variables, pools, and executors.
- Benefits: resource and permission isolation without spinning up separate Airflow instances.
- Core capabilities:
  - Per‑team resource isolation (DAGs, connections, variables, pools).
  - Per‑team executor configuration (Celery, Kubernetes, Local, AWS ECS, etc.).
  - Team‑scoped authorization (Keycloak, Simple auth).
  - Team‑scoped secrets via environment‑variable naming conventions.
  - CLI commands for team management.
  - UI selector for team assignment in connection, variable, and pool forms.
  - Full API support with `team_name` field on relevant objects.
- Enabling: set `multi_team = True` in `airflow.cfg` or export `AIRFLOW__CORE__MULTI_TEAM=True`.

## Deadline Alerts – Synchronous Callbacks (AIP‑86) – Experimental
- Extends the 3.1 deadline‑alert system with **SyncCallback**, which runs directly on the executor (optionally targeting a specific executor).
- New features:
  - Multiple deadline thresholds per DAG via a list in the `deadline` parameter.
  - Missed‑deadline metadata exposed in the Grid API for monitoring.
  - Improved developer experience for custom `DeadlineReference` definitions.

## UI Enhancements
- **Human‑in‑the‑Loop (HITL) Approval History**: full audit trail of approvals and rejections displayed in the UI.
- **XCom Management**: add, edit, and delete XCom values directly from the interface.

## Release Resources
- PyPI: https://pypi.org/project/apache-airflow/3.2.0/
- Documentation: https://airflow.apache.org/docs/apache-airflow/3.2.0/
- Release notes: https://airflow.apache.org/docs/apache-airflow/3.2.0/release_notes.html
- Docker image: `docker pull apache/airflow:3.2.0`
- Constraints file: https://github.com/apache/airflow/tree/constraints-3.2.0
