---
title: 'Building Hierarchical Agentic RAG Systems: Multi-Modal Reasoning with Autonomous Error Recovery - InfoQ'
url: https://www.infoq.com/articles/building-hierarchical-agentic-rag-systems/
site_name: tldr
content_file: tldr-building-hierarchical-agentic-rag-systems-multi-mo
fetched_at: '2026-04-16T11:58:55.730325'
original_url: https://www.infoq.com/articles/building-hierarchical-agentic-rag-systems/
date: '2026-04-16'
description: In this article, the author explores hierarchical agentic RAG systems that coordinate specialized workers through structured orchestration for enterprise-scale data analysis workflows.
tags:
- tldr
---

InfoQ HomepageArticlesBuilding Hierarchical Agentic RAG Systems: Multi-Modal Reasoning with Autonomous Error Recovery

 AI, ML & Data Engineering
 

Designing Data Layers for Agentic AI: Patterns for State, Memory, and Coordination at Scale (Webinar May 12th) 

# Building Hierarchical Agentic RAG Systems: Multi-Modal Reasoning with Autonomous Error Recovery

Apr 09, 202625
									min read

by

* Abhijit Ubale

reviewed by

* Arthur Casals

#### Write for InfoQ

Feed your curiosity.

Help 550k+ global 
senior developers 
each month stay ahead.
Get in touch

### Key Takeaways

* Traditional RAG systems struggle bridging structured SQL databases and unstructured document collections (a challenge we call the modality gap), leading to incomplete reasoning and hallucinations.
* Hierarchical multi-agent orchestration using a supervisor-worker topology enables decomposition of complex queries into specialized sub-tasks, achieving 84.5 percent accuracy on the EntQA enterprise benchmark (vs. 62.8 percent for flat-agent approaches).
* Autonomous error recovery through reflective retry mechanisms can detect and correct agent failures (SQL syntax errors, schema mismatches) before they propagate as hallucinations, reducing hallucination rates by sixty percent compared to standard RAG.
* Cloud-agnostic database adapters using the Adapter pattern allow the same orchestration logic to work seamlessly across Snowflake, Redshift, BigQuery, and other enterprise data warehouses.
* Deterministic control flow (via explicit state management) with schema awareness and safety constraints enables production-grade deployment of agentic systems while maintaining auditability and compliance requirements.

## Introduction

Enterprise AI teams face a persistent challenge: Most Retrieval-Augmented Generation (RAG) systems excel at either structured data queries or document search, but struggle when both are required simultaneously. A financial analyst who asked "Why are European operations underperforming?" needs data from both SQL databases (revenue, margins, and employee counts) and unstructured documents (market reports, competitive analysis, regulatory filings). Current RAG systems might return revenue data without regulatory context or surface market reports without quantitative validation, leaving analysts to manually bridge the gap. Current RAG approaches treat these modalities as separate concerns, forcing engineers to build custom orchestration layers or accept incomplete answers.This article explores architectural patterns for solving the modality gap through hierarchical multi-agent orchestration, using Protocol-H as a reference implementation to illustrate these concepts in practice. The patterns discussed, supervisor-worker topology with autonomous error recovery, build on LangGraph/LangChain agentic patterns used by teams at companies like xAI and Databricks. The accompanying opensource codedemonstrates these patterns deployed at enterprise scale with Docker/K8s, though readers can apply the same architectural principles using their preferred frameworks.

The architecture described in this article is based on a reference implementation and production-oriented experimentation with enterprise datasets; specific deployment details have been generalized to focus on the architectural patterns rather than any particular system implementation.

## The Modality Gap Problem: Why Traditional RAG Falls Short

Traditional RAG systems follow a linear pipeline: embed user query, retrieve documents, pass to LLM, and generate an answer. This works well for document-centric questions but breaks down in enterprise environments where data lives in multiple modalities.

* ##### The Agentic AI SRE built on AWS

#### Related Sponsor

Boost AWS effectiveness with Agentic AI — unify telemetry, reduce noise, and resolve incidents faster.Learn More.

Consider a customer churn analysis query: "Which customer segments have the highest churn rate, and what are the common reasons based on support tickets?" This requires:

* Structured reasoning (SQL): Join customer, transaction, and churn tables; compute segment-level churn percentages
* Semantic reasoning (vector search): Retrieve support tickets semantically related to churn
* Cross-modal synthesis: Correlate SQL results with document insights to identify causation

Most RAG systems attempt this in one pass:

Query → Retrieve documents + run one SQL query → LLM → Answer

The result is incomplete or hallucinated answers for several reasons.:With pre-committed retrieval, developers must first decide which SQL tables to query and which documents to retrieve, often missing relevant data. With limited context windows, even relevant results may not fit, preventing comprehensive synthesis in a single LLM pass. Initial SQL might identify high-churn segments but miss key support tickets; with no retry mechanism (such as iterative refinement), the system generates answers from incomplete data. LLMs generate confident-sounding answers even when working with partial data, especially when structured and unstructured signals conflict.

### Real-World Impact

In internal testing across three financial services internal evaluations (Q4 2025; n=~1,500 multi-hop queries), we found about thirty percent failed silently, defined as authoritative answers omitting more than twenty percent of relevant data points (e.g., missing regulatory context in performance analysis), with opaque reasoning paths hindering audits.

This is where hierarchical agentic reasoning enters the picture.

## The Hierarchical Agentic Solution Architecture Overview

Protocol-H introduces a supervisor-worker topology inspired by organizational hierarchies and human problem-solving:

Just as managers delegate specialized analysis to data analysts (SQL) and researchers (documents) before synthesizing insights, the supervisor breaks down queries while workers execute modality-specific tasks.

Figure 1: Protocol-H architecture. Supervisor routes queries to specialized SQL/vector workers with reflective retry for error handling inspired by organizational hierarchies (Source: Author;Protocol-H repo).

The key insight is specialization with orchestration: Each worker agent becomes expert at its modality (SQL or semantic search), while the supervisor manages the reasoning flow and handles complex, multi-hop scenarios.

### Component Deep Dive

#### The Supervisor Agent: Meta-Cognitive Orchestrator

The supervisor is the reasoning brain of the system. Rather than executing queries itself, it acts as a strategic director.

Core Responsibilities:

* Query analysis to determine if the question requires SQL, semantic search, or both
* Task decomposition to break complex queries into atomic steps (e.g., "First, find all customers in Europe; then retrieve their support tickets; then correlate with churn data")
* Worker routing to decide which worker(s) execute next based on task and current state
* Result synthesis combining worker outputs into a coherent final answer
* Error management to detect failures and trigger reflective retry

Implementation Pattern:



def supervisor_node(state: AgentState) -> Dict[str, Any]:
    """
    Supervisor routes queries to appropriate workers.
    
    Returns structured decision with:
    - next_worker: "sql_agent", "vector_agent", or "FINISH"
    - reasoning: Explanation of routing choice
    - task_description: Specific instruction for worker
    """
    
    # Analyze conversation history and current state
    supervisor_prompt = """
    You are an enterprise data reasoning expert. Given this question and what you
    know so far, decide the next reasoning step.
    
    Current question: {current_question}
    Results collected so far: {results_so_far}
    
    Decide: Do we need SQL query results? Document search? Or can we synthesize
    a final answer?
    
    Respond with: next_worker, reasoning, task_description
    """
   
   # Parse LLM response to structured decision object
   decision = llm.invoke(supervisor_prompt).parse() 
   
   #returning structured decision
    return {"next_step": decision.next_worker, ...}

#### The SQL Worker: Schema-Aware Query Engine

The SQL Worker specializes in deterministic, structured reasoning.

Key Features:

Schema Introspection

The SQL worker automatically discovers tables and columns via database metadata APIs (e.g.,INFORMATION_SCHEMA). Relationships are identified through two mechanisms: explicit foreign key constraints from metadata (treated as authoritative) and LLM-based heuristic inference using column naming conventions (e.g., matching customer_id across tables) when foreign keys are absent.

To mitigate correctness risks from inferred relationships several tools are used. Confidence scoring is employed via heuristic matches are scored by string similarity and naming convention strength; low-confidence inferences (similarity < 0.8) are flagged for explicit user confirmation rather than automatic use. Supervisor arbitration is employed via inferred relationships presented to the supervisor as ranked suggestions with confidence scores, not hard constraints; the supervisor must explicitly approve each join before query generation. Additionally, validation is done at runtime: Queries using inferred joins are executed with row-limit constraints first. If result sets appear anomalous (e.g., they are empty, Cartesian products, or type mismatches), the reflective retry mechanism triggers and the supervisor is alerted to reconsider the join’s validity. Finally, explicit foreign key precedence is employed: When metadata contains explicit foreign key constraints, heuristic inference is bypassed entirely for those tables.

Query Validation

Generated SQL is checked against schema before execution.

Dialect Optimization

In order to generate database-specific SQL (e.g., Snowflake, Redshift, or BigQuery) the target dialect and schema context is included in the LLM prompt, followed by a pre-execution syntax validation step. Complex dialect-specific features (e.g., Snowflake's QUALIFY and BigQuery's STRUCT) are a known limitation of this approach; the reflective retry mechanism handles failures, but first-pass correctness on advanced syntax isn't guaranteed. For dialect-heavy or compliance-sensitive use cases, such as regulated financial reporting requiring exact QUALIFY semantics or healthcare data with strict STRUCT validation, teams may prefer connector-level templates or query builders (e.g., SQLAlchemy, dbt) over LLM generation, using Protocol-H to orchestrate pre-validated query fragments rather than generating SQL from scratch.

Workflow:

Figure 2: Workflow.

Safety Mechanisms:

For SQL injection prevention through parameterized queries, all SQL is executed via parameterized query APIs (e.g., cursor.execute(query, params)) rather than string interpolation, ensuring user input is never interpreted as executable SQL. For row-level access control enforcement, the worker queries the database using the authenticated user's credentials and session context, delegating access control to the database's native RBAC rather than reimplementing it at the application layer. Query timeout is used to prevent runaway queries : Each query is executed with a configurable timeout (e.g., thirty seconds by default). If the timeout is exceeded, the query is cancelled and the supervisor is notified to either retry with a scoped-down query or return a partial result.

Result size is limited to protect memory. Query results are capped at a configurable row/byte limit before being passed to the LLM context, preventing oversized payloads from exhausting memory or exceeding token limits.

#### The Vector Worker: Semantic Search Agent

The vector worker handles semantic reasoning over documents.

Key Features:

* Semantic search is accomplished with embedded queries, search vector index, and retrieval of relevant documents.
* Hybrid retrieval combines BM25 keyword matching with dense vector cosine similarity search, merging ranked results via Reciprocal Rank Fusion (RRF). This approach balances precision (exact keyword matches for specific terms like table names or product codes) with recall (semantic similarity for conceptually related content), outperforming both as stand-alone methods.
* Relevance filtering applies thresholds to avoid spurious matches.
* Summarization extracts key insights from retrieved documents.

Key Challenges:

The cold start problem occurs when no relevant documents exist, and the worker returns an explicit null signal to the supervisor rather than fabricating results, triggering a fallback to SQL or a clarifying response to the user. Ambiguity resolution occurs when semantically broad queries that risk returning multiple conflicting interpretations are flagged by the worker, with the top-N results and their relevance scores surfaced to the supervisor for arbitration rather than blindly merging them. When recency is relevant (temporal awareness), retrieved documents can be ranked with a time-decay factor applied to relevance scores, ensuring recent filings, reports, or tickets are prioritized over older matches. This capability was not active in the EntQA benchmark tests reported in this article; the benchmark results reflect standard vector search without temporal weighting.

#### The Reflective Retry Mechanism: Autonomous Error Recovery

This is where Protocol-H differs fundamentally from standard agent systems. When a worker encounters an error, instead of propagating it as a hallucination, the system enters reflective retry mode.

Error Flow:

Figure 3: Reflective Retry Node – Autonomous Error Recovery Flow in Protocol-H.

Example: SQL Syntax Error Recovery



from pydantic import BaseModel
from typing import Optional

class RetryCorrection(BaseModel):
    corrected_query: Optional[str] = None
    alternative_strategy: Optional[str] = None


def reflective_retry_node(state: AgentState) -> Dict[str, Any]:
    """
    Autonomous error recovery mechanism.
    Returns: Dict containing corrected query or escalation signal.
    """
    error_msg = state.error_message

    retry_prompt = f"""
    A query failed with this error: {error_msg}

    Original task: {state.current_task}
    Available schema: {schema_info}

    Analyze the error and suggest a corrected approach.
    Common issues:
    - Misspelled table/column names
    - Incorrect JOIN syntax
    - Missing WHERE clauses
    - Type mismatches

    Respond with: corrected_query or alternative_strategy
    """

    # LLM returns a structured RetryCorrection object (Pydantic model)
    correction: RetryCorrection = llm.with_structured_output(
        RetryCorrection
    ).invoke(retry_prompt)

    # RetryCorrection has two optional fields:
    # - corrected_query: str  → revised SQL to retry
    # - alternative_strategy: str  → fallback if query can't be fixed
    return attempt_alternative_approach(correction)

This mechanism is associated with an approximate sixty percent reduction in hallucinations compared to standard RAG systems ( a 7.1 percent vs. a 28.5 percent hallucination rate, see Benchmark Results, Table 1). This figure reflects the overall Protocol-H architecture, including the supervisor-worker topology, schema-aware query generation, and reflective retry working in combination, not the retry mechanism in isolation. Errors are caught and corrected through this integrated design before they propagate to the final answer generation step.

Understanding the why behind Protocol-H's architecture is only half the picture. The supervisor-worker topology and reflective retry mechanism described above only deliver their promised benefits if the underlying implementation is equally robust. This section details the key architectural decisions, state management, database abstraction, and worker design, that translate the conceptual framework into a production-ready system.

## Implementation and Integration: Architecture Decisions

#### State Management with LangGraph

Protocol-H uses LangGraph's StateGraph for deterministic workflow orchestration:



class AgentState(TypedDict):
    messages: List[BaseMessage]          # Conversation history
    next_step: Literal["supervisor", "sql_agent", "vector_agent", "FINISH"]
    final_answer: Optional[str]         # Result when complete
    query_type: Optional[str]           # "sql", "semantic", or "multi-modal"
    retry_count: int                    # Track retry attempts
    error_message: Optional[str]        # Error context for debugging

StateGraph ensures deterministic execution (graph-level only). The control flow graph structure, meaning which nodes are visited and in what order, always follows the same path for the same input (enforced via temperature=0 for routing decisions). What is deterministic: node visitation order, state transitions, retry logic triggers, and which worker is invoked when. What is not deterministic: the specific text outputs generated by workers (SQL queries, document summaries, and reasoning explanations), which may vary between runs even with identical inputs due to LLM sampling. The orchestration logic and state transitions are fully reproducible and auditable; worker outputs are reproducible only in structure, not in verbatim content.

StateGraph is auditable with full traceability of decisions and data flow. It is has safety in mind, preventing loops with retry counters and timeouts.

#### Cloud-Agnostic Database Adapters

Using the Adapter Pattern, Protocol-H abstracts database specifics:



class BaseConnector(ABC):
    """Abstract interface for database connectors."""

    @abstractmethod
    def get_schema(self) -> List[TableSchema]:
        """Get available tables and columns."""
        pass

    @abstractmethod
    def execute_query(self, sql: str) -> QueryResult:
        """Execute SQL query safely."""
        pass


class SnowflakeConnector(BaseConnector):
    """Snowflake-specific implementation.
    
    Handles Snowflake dialect differences:
    - Identifiers are UPPERCASE by default
    - Uses LIMIT instead of TOP for row capping
    - Supports QUALIFY for window function filtering
    """

    def get_schema(self) -> List[TableSchema]:
        # Snowflake stores metadata in INFORMATION_SCHEMA
        # Identifiers must be uppercased for reliable matching
        result = self.connection.execute("""
            SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = UPPER(:schema)
        """, {"schema": self.schema_name})
        return [TableSchema.from_row(row) for row in result]

   def execute_query(self, sql: str) -> QueryResult:
    # Simplified illustration: production implementations should use 
    # cursor-based fetch limits or dialect-specific query hints rather 
    # than string wrapping, which can alter query semantics for 
    # statements with ORDER BY, existing LIMIT clauses, or CTEs.
    # See SnowflakeConnector in the repository for production-grade 
    # implementation using cursor.fetchmany().
    safe_sql = f"SELECT * FROM ({sql}) LIMIT {self.max_rows}"
    return QueryResult(rows=self.connection.execute(safe_sql).fetchall()))


class RedshiftConnector(BaseConnector):
    """Amazon Redshift implementation.
    # Dialect note: uses pg_catalog instead of INFORMATION_SCHEMA
    # and does not support QUALIFY — handled via subquery workaround
    """
    def execute_query(self, sql: str) -> QueryResult:
        # Redshift dialect handling
        pass

This design allows teams to swap database backends without modifying orchestration logic, which is critical for enterprises with heterogeneous infrastructure. In practice, each connector handles dialect-specific translation internally (e.g., Snowflake's uppercase identifiers, Redshift's pg_catalog metadata, and BigQuery's nested STRUCT types), so the supervisor and worker agents always interact with a normalized QueryResult interface regardless of the underlying engine. However, there are limitations worth noting: Highly dialect-specific features, such as Snowflake's QUALIFY, BigQuery's ARRAY_AGG, or Redshift's DISTKEY hints, may require connector-level customization and are not automatically abstracted. Teams adopting Protocol-H on new database backends should audit these edge cases before assuming full portability.

#### Specialized Worker Agents

Each worker runs its own ReAct loop (reasoning and acting):



def sql_worker_node(state: AgentState) -> Dict[str, Any]:
    """SQL Worker runs ReAct: Thought → Action → Observation."""
    
    # Step 1: Thought (structured reasoning)
    reasoning_prompt = f"""
    User asks: {state.current_question}
    Available tables: {schema}
    
    Respond with a structured reasoning object containing:
    - sql_query: the SQL to execute
    - explanation: reasoning for the query choice
    - confidence: self-assessed confidence score (0-1)
    """
    
    reasoning: SQLReasoning = llm.with_structured_output(SQLReasoning).invoke(reasoning_prompt)
    
    # Step 2: Action (execute SQL)
    query_result = db.execute(reasoning.sql_query)
    
    # Step 3: Observation (process results)
    formatted_result = format_for_synthesis(query_result)
    
    return {
        "messages": [..., ToolMessage(content=formatted_result)],
        "next_step": "supervisor"
    }

## Benchmark Results

The following approaches were evaluated.

Protocol-H was evaluated on the EntQA benchmark, a collection of two hundred enterprise questions requiring multi-hop reasoning over both SQL and document data.

Protocol-H: The hierarchical supervisor-worker architecture with reflective retry, as described in this article.

A flat agent, a single general-purpose LLM agent with access to both SQL and vector search tools but no hierarchical orchestration or specialized workers, was also evaluated. It represents the most common "just give the LLM all the tools" approach.

Finally, standardRAG was evaluated. It is a traditional retrieve-then-generate pipeline (embed query, retrieve documents, pass to LLM, and then generate an answer) with no agentic reasoning or SQL capability.

## Performance Comparison

Metric

Protocol-H

Flat Agent

Standard RAG

Tier 3 Accuracy (multi-hop questions)

84.5%

62.8%

45.2%

Hallucination Rate

7.1%

18.2%

28.5%

Avg. Reasoning Steps

3.2

1.8

1.0

Query Latency (p95)

2.1s

1.4s

0.8s

Table 1. Performance comparison.

Reasoning steps refer to the number of distinct tool invocations (SQL queries or vector searches) the system made before producing a final answer. Higher values indicate more thorough multi-hop reasoning; lower values suggest the system attempted to answer in fewer passes, which correlates with higher hallucination rates in this benchmark.

### Benchmark Methodology

EntQA is an internal benchmark developed by the Protocol-H team to evaluate multi-hop reasoning over heterogeneous enterprise data. It is not currently a public benchmark, though the evaluation scripts and anonymized question set are available in theProtocol-H repositoryfor reproducibility.

The dataset contains two hundred enterprise questions across three complexity tiers. Tier 1 (simple, n=60) has single-modality questions answerable with one SQL query or one vector search. Tier 2 (moderate, n=80) contains questions requiring one SQL query and one vector search with basic synthesis. Tier 3 (complex, n=60) is comprised of multi-hop questions requiring three or more reasoning steps across both modalities, with cross-modal synthesis (e.g., "Which customer segments have the highest churn rate, and what do their support tickets reveal about root causes?").

All reported accuracy figures refer to Tier 3 questions, representing the hardest and most enterprise-relevant subset.

Test setup:

* LLM: GPT-4o (all three systems) to isolate orchestration differences
* Embedding model: text-embedding-3-large (OpenAI)
* Vector store: Pinecone (standard tier)
* SQL backend: Snowflake Enterprise
* Hardware: Docker container, 4 vCPU / 16GB RAM
* Evaluation: Answer correctness scored by GPT-4o judge against ground-truth answers, with human spot-checks on twenty percent of responses. Limitation: GPT-4o serves as both the reasoning engine for all tested systems and the evaluation judge, which may introduce circularity bias; human spot-checks were used to validate judge reliability.
* Reproducibility: Full eval scripts, prompts, and ground-truth answers available in the repository. Note: Enterprise data sources used in EntQA are not publicly available; replication requires comparable SQL/vector datasets with similar schema complexity.

### Key Findings

Accuracy Gains

Hierarchical routing improved multi-hop accuracy by 34.6 percent relatively vs. flat agents (84.5% vs. 62.8%) and 87.0% relatively vs. standard RAG (84.5 percent vs. 45.2 percent). In absolute terms, these represent gains of 21.7 percentage points and 39.3 percentage points, respectively.

Latency Trade-off

Protocol-H's p95 latency of 2.1 second is approximately 1.3 seconds slower than standard RAG (0.8 seconds) and approximately 0.7 seconds slower than flat agents (1.4 seconds), driven by higher reasoning step counts (3.2 vs. 1.0 and 1.8). This overhead is the direct cost of multi-hop reasoning. For context, synchronous dashboard queries typically tolerate two to three second response times, placing Protocol-H within acceptable range for most analytics workloads.

For latency-sensitive use cases (e.g., real-time customer-facing applications), the asynchronous with webhooks pattern is recommended. The 2.1 second investment yields a 21.7 percent accuracy gain, a trade-off most enterprise analytics teams will find favorable where decision quality outweighs speed.

Robustness

On error-prone queries (intentional schema mismatches), Protocol-H recovered correctly eighty-nine percent of the time vs. twelve percent for flat agents.

## Production Deployment Considerations

## Safety and Compliance

Enterprise deployments require more than accuracy. Protocol-H implements:

Deterministic Control Flow

StateGraph ensures reproducible execution paths, which is critical for compliance audits.

Schema Awareness

At initialization, each worker queries database metadata (e.g., INFORMATION_SCHEMA) to build a runtime map of accessible tables and columns scoped to the authenticated user's RBAC permissions. Workers only generate queries against provably accessible data, preventing unauthorized queries before execution.

Policy Controls

Teams can define additional business rules in schema_policy.yaml (e.g., exclude_tables:['pii_raw']) to enforce data boundaries independently of database permissions, which is useful for multi-tenant deployments or regulatory segmentation.

Error Diagnostics

Full context answers why a query failed, rather than just providing a hallucinated answer.

Rate Limiting

Rate limiting prevents runaway agent behavior and protects infrastructure.

Result Validation

Before returning results to the supervisor, worker outputs pass through a configurable validation layer that checks for: numerical anomalies (e.g., revenue figures exceeding configured thresholds), null-dominant results (e.g., more than eighty percent NULL values suggesting a schema mismatch), empty result sets that should not be empty given the query context, and type mismatches between expected and returned data types. Failed validations trigger the Reflective Retry Node rather than propagating suspect data to the final answer.

### Deployment Patterns

Synchronous API



def create_orchestrator(
    db_connector: BaseConnector,
    vector_store: VectorStoreClient,
    policy_path: str = "config/schema_policy.yaml",
    llm_model: str = "gpt-4o",
    max_retries: int = 3
) -> ProtocolHOrchestrator:
    """
    Initializes the Protocol-H orchestration layer:
    - Loads schema_policy.yaml for access control rules
    - Instantiates the database connector (e.g., SnowflakeConnector)
    - Initializes the vector store client (e.g., Pinecone)
    - Wires Supervisor, SQL Worker, and Vector Worker into the StateGraph
    """
    ...

def get_compiled_app(self) -> CompiledStateGraph:
    """
    Compiles the StateGraph into an executable LangGraph app:
    - Validates node connections and edge definitions
    - Freezes the graph structure for deterministic execution
    - Returns a runnable object supporting .invoke() and .invoke_async()
    """
    ...

# --- Usage Example ---
from protocol_h.connectors import SnowflakeConnector
from protocol_h.vector import PineconeClient

# Initialize required connectors
db = SnowflakeConnector(
    account="your_account",
    warehouse="your_warehouse",
    role="analyst_role"
)
vector_store = PineconeClient(index_name="enterprise_docs")

# Create orchestrator with required dependencies
orchestrator = create_orchestrator(
    db_connector=db,
    vector_store=vector_store
)
app = orchestrator.get_compiled_app()

result = app.invoke({
    "messages": [HumanMessage(content="What's our top customer segment by revenue?")],
    "next_step": "supervisor",
})
print(result["final_answer"])

Asynchronous with Webhooks



# For longer-running queries, use LangGraph's native async API
import asyncio

result = await app.ainvoke({
    "messages": [...],
    "next_step": "supervisor",
})

Docker Containerization



# Stage 1: Build --- install dependencies in isolated layer
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt.
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime --- lean final image
FROM python:3.11-slim

WORKDIR /app

# Install curl for health check (not included in slim images)
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Security best practice: run as non-root user
RUN useradd --create-home appuser
USER appuser

# Copy only installed packages and app code from builder
COPY --from=builder /root/.local /home/appuser/.local
COPY src/ /app/src
COPY config/ /app/config

# Pass secrets via environment (injected at runtime by orchestrator/K8s)
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV SNOWFLAKE_ACCOUNT=${SNOWFLAKE_ACCOUNT}

# Health check: verify the app is responsive every 30s
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "main.py"]

## Common Challenges and Solutions: Schema Drift

Enterprise databases evolve: columns renamed, tables deprecated, new business logic introduced.

Protocol-H solves schema drift through two complementary mechanisms. First, it uses period schema validation. A lightweight background thread within the app runtime re-fetchesINFORMATION_SCHEMAmetadata at a configurable interval (default: twenty-four hours, or triggered on any 'unknown column' error) and updates each worker's in-memory schema map. For high-availability deployments, this can alternatively be implemented as a Kubernetes CronJob or external scheduler to avoid per-instance polling.

Next, graceful error handling with an alternative suggestion is provided. When a worker encounters an 'unknown column' error at query time, rather than failing silently it triggers the following recovery flow. The worker performs a fuzzy match against the current schema (e.g., detecting thatprofit_marginwas renamed tonet_margin) using string similarity scoring. If a likely match is found (similarity score greater than 0.8), the worker proposes the alternative column to the supervisor along with the original error context (e.g., 'Column profit_margin not found – did you mean net_margin?'). The supervisor decides whether to retry with the suggested column, request clarification, or escalate to the user. If no match is found, the supervisor is notified with a full diagnostic payload so it can reformulate the query or inform the user of the data gap.

This approach keeps schema drift from becoming a silent failure mode. Every drift-related error produces an actionable signal rather than a hallucinated answer.

### Hallucination on Complex Joins

When queries require three or more table joins, LLMs sometimes generate incorrect join conditions.

The reflective retry mechanism solves this problem by catching failed queries and suggests alternative join strategies, or breaks the query into smaller steps.

### Latency in Multi-Hop Scenarios

Each additional reasoning step introduces incremental latency overhead. In multi-hop scenarios requiring three to five sequential steps, total query latency may exceed synchronous user interface tolerance thresholds-

To solve this issue, implement result caching for common sub-queries. Use parallel execution where independent steps can run simultaneously. Protocol-H supports this approach via LangGraph's Send API while preserving deterministic graph structure. Determinism here refers to the orchestration logic (which nodes execute and in what order), not sequential execution. When a query requires both a SQL aggregation and a vector search with no dependency between them, the supervisor dispatches both workers concurrently via parallel graph branches; results are merged at a deterministic synchronization point before final synthesis. The control flow graph remains fully reproducible, only the worker-level execution is parallelized. (See Figure 1's parallel worker paths in the architecture overview.)

Cache schema information to avoid repeated introspections: Schema metadata is cached with a configurable TTL (default: twenty-four hours), matching the validation interval described in Schema Drift. This matching ensures caching and drift detection stay in sync. The cache is invalidated and refreshed on the same schedule as the background schema validation process, balancing performance (avoiding redundantINFORMATION_SCHEMAqueries within a session) with freshness (guaranteeing workers never operate on schema data older than the TTL window).

### Cost Management

Each agent invocation calls the LLM, which can accumulate costs at scale.

To manage cost, use faster, cheaper models for routing decisions (e.g., GPT-4o mini for supervisor). This is a general architectural recommendation for future cost optimization. Note that all benchmark results reported in this article (84.5 percent accuracy, 7.1 percent hallucination rate) were produced using GPT-4o for both supervisor and workers. We have not formally evaluated the cost/accuracy trade-off of mixed-model configurations; teams adopting this pattern should validate it against their own accuracy thresholds before deploying at scale. Also, cache reasoning results for identical queries and batch similar queries for efficiency.

### Lessons Learned

Specialization Is Better than Generalization

Dedicated SQL and Vector workers consistently outperform single general-purpose agents on their respective modalities, the SQL worker excels at structured reasoning, while the vector worker excels at semantic search. This specialization compounds into larger end-to-end gains.

Error Recovery Matters

In our internal testing (n=~1,500 multi-hop queries across three financial services deployments, Q4 2025), error analysis of hallucinated responses revealed that approximately sixty percent originated from unhandled execution errors, failed SQL queries, empty vector search results, or schema mismatches, that propagated silently to the final answer generation step, rather than from fundamental LLM reasoning flaws. This means recovery mechanisms are disproportionately valuable: Fixing error handling addresses the majority of hallucinations without requiring model improvements.

Schema Awareness is Critical

Workers that understand available data (schema, access controls) make better decisions than those working with raw data

Determinism Enables Trust

Enterprises value reproducible execution over maximum accuracy, deterministic workflow orchestration is a critical design requirement for production agentic systems. StateGraph's graph-level determinism (consistent node visitation order and state transitions given identical inputs) provides this reproducibility. Concretely, Protocol-H produces a traceable audit log of every decision: which workers were invoked, in what order, with what inputs. For enterprise teams operating under SOC 2, GDPR, or internal model governance requirements, this reproducibility is essential, it enables answers to be traced back to their exact data sources and reasoning steps, making compliance audits more tractable than with non-deterministic systems.

Multi-Modal Reasoning Requires Orchestration

No single agent can reason well over both SQL and semantic data; hierarchical delegation is essential.

## Looking Forward

The framework presented here is a snapshot of the current state of agentic RAG for enterprises. Emerging areas of research include:

Adaptive routing

Learning which worker combinations are most effective for different query types, currently under exploration via two complementary approaches. The first is query log analysis: Mining historical execution traces to identify which supervisor routing decisions correlated with high-accuracy, low-retry outcomes, then using these patterns to bias future routing decisions (e.g., 'financial period queries almost always require SQL first, then vector search for context'). The second is lightweight RL-based optimization: Framing the supervisor's routing decisions as a policy to be optimized, where the reward signal combines answer accuracy, hallucination rate, and query latency, allowing the system to learn query-type-specific routing strategies over time without manual tuning. Both approaches are in early-stage research; query log analysis is the nearer-term path given its lower implementation complexity.

Semantic caching

Cache vector search results to reduce redundant embeddings.

Cross-modal fusion

More sophisticated methods for combining SQL and semantic evidence.

Explainability

Generating human-readable explanations of multi-hop reasoning paths is arguably the most critical frontier for enterprise adoption. Today, Protocol-H produces full execution traces (which workers were invoked, in what order, with what inputs and outputs), but these are technical logs rather than business-readable explanations. The next step is translating these traces into natural language reasoning summaries, for example: "To answer your question about European underperformance, I first queried revenue and margin data by region (SQL), then retrieved the most recent regulatory filings and market reports for the EU (vector search), and found that declining margins in Germany correlate with new VAT compliance costs mentioned in three regulatory documents from Q3 2024". This level of transparency is essential for analyst trust, compliance audits, and model governance frameworks. The EU AI Act's requirements for high-risk AI systems include maintaining logs of AI system operation (Article 12), which encompasses decision traceability.

## Conclusion

The modality gap, which bridges structured and unstructured data in enterprise RAG systems, is not a technical limitation but an orchestration challenge. Protocol-H demonstrates that hierarchical multi-agent systems with autonomous error recovery can achieve enterprise-grade accuracy, safety, and auditability.

By separating concerns (supervisor orchestration vs. worker specialization) and implementing reflective retry mechanisms, teams can build agentic systems that reason reliably over heterogeneous enterprise data while maintaining determinism and compliance requirements.

For teams building enterprise agentic systems, the architectural insight is simple: Orchestrate before delegating, specialize before generalizing, and recover before propagating errors. Hierarchical multi-agent design with autonomous error handling enables reliable reasoning across heterogeneous data modalities, bridging the gap between theoretical promise and production-ready deployment. The reference implementation, Protocol-H, demonstrates these principles in practice, offering a foundation for teams to adapt these patterns to their own infrastructure and compliance requirements.

Code Examples: All code snippets are original Python implementations from the Protocol-H framework.

References:

* LangChain v0.3.x
* LangGraph v0.2.x
* OpenAI Python SDK v1.x
* GPT-4o (gpt-4o-2024-08-06) — used for Worker reasoning
* GPT-4o mini (gpt-4o-mini-2024-07-18) — recommended for Supervisor routing
* text-embedding-3-large — used for vector embeddings
* Pinecone v3.x
* Snowflake Connector for Python v3.x—Python Connector

Note: Version numbers reflect those used during benchmark testing (Q4 2025)

Open-source repository is availablehere.

 

## About the Author

 

 

 

#### Abhijit Ubale

Show more
Show less

### Rate this Article

Adoption

Style

 Author Contacted

#### This content is in theAI, ML & Data Engineeringtopic

##### Related Topics:

* Development
* Architecture & Design
* AI, ML & Data Engineering
* Retrieval-Augmented Generation
* Large language models
* Artificial Intelligence

* #### Related Editorial
* #### Popular across InfoQ##### Anthropic Releases Claude Mythos Preview with Cybersecurity Capabilities but Withholds Public Access##### Cloudflare Introduces EmDash: TypeScript CMS Positioned as WordPress Successor##### Java News Roundup: JDK 27 Release Schedule, Hibernate, LangChain4j, Keycloak, Helidon, Junie CLI##### Google Cloud Highlights Ongoing Work on PostgreSQL Core Capabilities##### GitHub Copilot CLI Reaches General Availability##### How SBOMs and Engineering Discipline Can Help You Avoid Trivy’s Compromise
* ##### Anthropic Releases Claude Mythos Preview with Cybersecurity Capabilities but Withholds Public Access
* ##### Cloudflare Introduces EmDash: TypeScript CMS Positioned as WordPress Successor
* ##### Java News Roundup: JDK 27 Release Schedule, Hibernate, LangChain4j, Keycloak, Helidon, Junie CLI
* ##### Google Cloud Highlights Ongoing Work on PostgreSQL Core Capabilities
* ##### GitHub Copilot CLI Reaches General Availability
* ##### How SBOMs and Engineering Discipline Can Help You Avoid Trivy’s Compromise

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