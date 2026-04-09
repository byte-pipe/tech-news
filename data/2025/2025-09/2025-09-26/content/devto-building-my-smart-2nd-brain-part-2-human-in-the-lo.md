---
title: 'Building My Smart 2nd Brain, Part 2: Human-in-the-Loop Querying with Robust Checkpointing - DEV Community'
url: https://dev.to/jimmyhott/building-my-smart-2nd-brain-part-2-human-in-the-loop-querying-with-robust-checkpointing-57ig
site_name: devto
fetched_at: '2025-09-26T11:06:33.239840'
original_url: https://dev.to/jimmyhott/building-my-smart-2nd-brain-part-2-human-in-the-loop-querying-with-robust-checkpointing-57ig
author: Jimmy
date: '2025-09-24'
description: From part 1, I kicked off the Smart 2nd Brain with two execution paths. Previously, we walked through... Tagged with python, ai, langchain, agentic.
tags: '#python, #ai, #langchain, #agentic'
---

Frompart 1, I kicked off the Smart 2nd Brain with two execution paths. Previously, we walked through the ingestion flow—splitting documents, generating embeddings, and storing them in a vector database. In this installment, we’ll switch gears to the query path and see how those embeddings power retrieval and human-in-the-loop answers.

### Asking the Brain

Now let's go through the query path:

 # =============================================================================
 # QUERY BRANCH
 # =============================================================================

 # Knowledge query pipeline
 graph.add_edge("retriever", "answer") # Retrieve -> Generate
 graph.add_edge("answer", "review") # Generate -> Review
 graph.add_edge("review", "validated_store") # Review -> Store
 graph.add_edge("validated_store", END) # Store -> End

Enter fullscreen mode

Exit fullscreen mode

First, the retriever node.

The retriever_node function queries the vector database based on the user’s input.

def retriever_node(self, state: KnowledgeState):

 if not state.user_input:
 state.logs = (state.logs or []) + ["No user_input provided for retrieval"]
 state.retrieved_docs = []
 return state

 try:
 # Try different retrieval strategies in order of preference
 if self.retriever:
 logger.info(f"🔍 Retrieving docs for query: {state.user_input}")
 results = self.retriever.get_relevant_documents(state.user_input)
 elif self.vectorstore:
 logger.info(f"🔍 Using vectorstore.similarity_search for query: {state.user_input}")
 results = self.vectorstore.similarity_search(state.user_input, k=5)
 else:
 results = []

 # Format retrieved documents for downstream processing
 state.retrieved_docs = [{"content": r.page_content, "metadata": r.metadata} for r in results]
 state.logs = (state.logs or []) + [f"Retrieved {len(state.retrieved_docs)} docs"]

 except Exception as e:
 logger.error(f"❌ Retrieval failed: {e}")
 state.retrieved_docs = []
 state.logs = (state.logs or []) + [f"Retrieval error: {str(e)}"]

 return state

Enter fullscreen mode

Exit fullscreen mode

Please note that it uses two approaches for search: one via theretrieverand another directly via thevector store.

try:
 # Try different retrieval strategies in order of preference
 if self.retriever:
 logger.info(f"🔍 Retrieving docs for query: {state.user_input}")
 results =self.retriever.get_relevant_documents(state.user_input)
 elif self.vectorstore:
 logger.info(f"🔍 Using vectorstore.similarity_search for query: {state.user_input}")
 results = self.vectorstore.similarity_search(state.user_input, k=5)
 else:
 results = []

Enter fullscreen mode

Exit fullscreen mode

A vector store is the database/index that stores embeddings and exposes low-level search primitives (e.g., similarity, filters), while a retriever is a higher-level interface that decides how to search, applies strategy (k, thresholds, filters, reranking), and returns documents via a consistent “get relevant docs” contract. In practice, a retriever is preferred because it abstracts backend specifics, enables easy swapping of stores, supports advanced strategies and fallbacks, and centralizes logic like query rewriting, multi-step retrieval, and graceful error handling—so applications stay flexible and robust as requirements or infrastructure change.

The retriever_node here will always prefer using retriever as long as one is provided. When initialize the state object, the retriever has to be created like this:

vectorstore = Chroma(
 collection_name="knowledge_base",
 embedding_function=embedding_model,
 persist_directory="./chroma_db",
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

Enter fullscreen mode

Exit fullscreen mode

embedding_model here is configured by AzureOpenAiEmbeddings, with the vectorstore object we use theas_retrievermethod to create the retreiver instance. The "k" parameter within search_kwargs specifies the number of top-k most similar (or relevant) documents to retrieve from the vector store during a similarity search.

If retriever is not available, similarity_search will be applied directly on the vectorstore object, bypassing the interface.

Once the relevant documents are retrieved, they can be sent to the answer node for processing using a LLM:

def answer_gen_node(self, state: KnowledgeState):

 if not self.llm or not state.user_input:
 state.logs = (state.logs or []) + ["⚠️ No LLM or user query provided"]
 return state

 try:
 # --- Build retrieved context ---
 context = "\n\n".join(
 [doc["content"] for doc in (state.retrieved_docs or [])]
 ) or "No relevant documents were retrieved."

 # --- Format conversation history ---
 conversation = "\n".join(
 [f"{m['role']}: {m['content']}" for m in (state.messages or [])]
 )

 # --- Load externalized prompt template ---
 prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "answer_prompt.txt"
 with open(prompt_path, "r", encoding="utf-8") as f:
 template = f.read()
 prompt = ChatPromptTemplate.from_template(template)
 chain = prompt | self.llm

 # --- Call language model with full context ---
 response = chain.invoke({
 "conversation": conversation,
 "query": state.user_input,
 "context": context
 })

 # --- Update state with generated answer ---
 state.generated_answer = response.content

 # Initialize messages array if not exists
 if not state.messages:
 state.messages = []

 # Add current user input and assistant response to conversation history
 # Note: Conversation memory is now managed by custom ConversationMemoryManager
 state.messages.append({"role": "user", "content": state.user_input})
 state.messages.append({"role": "assistant", "content": state.generated_answer})
 state.logs = (state.logs or []) + ["✅ Generated contextual answer with conversation history"]

 except Exception as e:
 state.generated_answer = None
 state.logs = (state.logs or []) + [f"❌ Answer generation failed: {e}"]

 return state

Enter fullscreen mode

Exit fullscreen mode

The answer node merges the user’s query with the documents retrieved by the retriever node and sends that context to the LLM. It loads the prompt from /prompts/answer_prompt.txt before invoking the model.

You are a helpful knowledge assistant with access to conversation history.

CONVERSATION HISTORY:
{conversation}

CURRENT USER QUESTION:
{query}

RETRIEVED KNOWLEDGE BASE CONTEXT:
{context}

INSTRUCTIONS:
- Use the conversation history to understand context and references
- Base your answer primarily on the retrieved knowledge base context
- If the knowledge base context is insufficient, say "I don't know based on available knowledge."
- Consider previous questions and answers to provide better context
- Keep the answer clear, concise, and contextually relevant
- If the user refers to something from earlier in the conversation, acknowledge it

Enter fullscreen mode

Exit fullscreen mode

Beyond the user query and retrieved documents, the conversation history is also injected to give the LLM richer context.

Note that the prompt includes an instruction like: “If the knowledge base context is insufficient, say ‘I don’t know based on available knowledge.’” This constrains the model to rely solely on the vector database rather than its pretrained knowledge. Whether you should strictly limit answers to the vector store is debatable, but we’ll adopt this constraint for now in this project.

Next comes the review stage, where HITL (Human-In-The-Loop) takes place.

def human_review_node(self, state: KnowledgeState):

 try:
 # Check for explicit human feedback
 feedback = getattr(state, "human_feedback", None)

 # Determine whether human review is required
 require_review = getattr(state, "require_human_review", None)
 if require_review is None:
 # Infer from knowledge_type when not explicitly set
 require_review = getattr(state, "knowledge_type", "conversational") in ("reusable", "verified")

 # If review is required, no feedback yet, and interrupt is available, pause the graph here
 if require_review and not feedback and interrupt is not None:
 # Message guides the API/UI to provide the required fields back
 _ = interrupt(
 "Awaiting human review: set 'human_feedback' to one of"
 " ['approved','rejected','edited'] and optionally set"
 " 'edited_answer' when feedback is 'edited'."
 )
 # Execution will resume here once feedback is supplied via the graph resume
 feedback = getattr(state, "human_feedback", None)

 if not feedback:
 # Auto-approval path when running headless or interrupt not available
 feedback = "approved"
 state.final_answer = state.generated_answer
 state.logs = (state.logs or []) + ["✅ Auto-approved answer"]

 elif feedback == "rejected":
 # Handle rejection - no final answer
 state.final_answer = None
 state.logs = (state.logs or []) + ["❌ Answer was rejected by human"]

 elif feedback == "edited":
 # Handle manual editing
 if hasattr(state, "edited_answer") and state.edited_answer:
 state.final_answer = state.edited_answer
 state.logs = (state.logs or []) + ["✏️ Human edited the answer"]
 else:
 state.final_answer = None
 state.logs = (state.logs or []) + ["⚠️ Edit requested but no edited_answer provided"]

 else:
 # Unknown feedback type - default to generated answer
 state.final_answer = state.generated_answer
 state.logs = (state.logs or []) + [f"⚠️ Unknown feedback '{feedback}', defaulting to generated answer"]

 # Save feedback for traceability
 state.human_feedback = feedback

 except Exception as e:
 # Error handling - default to generated answer
 state.final_answer = state.generated_answer
 state.human_feedback = "error"
 state.logs = (state.logs or []) + [f"❌ Human review failed: {e}"]

 return state

Enter fullscreen mode

Exit fullscreen mode

LangGraph supports HITL by allowing a running graph to pause at specific nodes and wait for external human input before continuing. The mechanism is theinterruptfunction: when a node calls interrupt(...) during execution, LangGraph saves the checkpointed state and returns control to the caller with a payload that indicates what inputs are expected (e.g., human_feedback, edited_answer). An external system (UI/API) collects the human response and then resumes the graph with those fields injected into the state.

If interrupt isn’t available or you’re running headless, you can implement fallbacks (like auto-approval) to keep the workflow progressing.

The human_review_node here orchestrates human-in-the-loop validation for generated answers. It first checks human_feedback and whether review is required (explicit via require_human_review or inferred when knowledge_type is reusable or verified). If review is required, no feedback is present, and interrupt is available, it calls interrupt(...) to pause execution and wait for external input, instructing the caller to provide human_feedback (approved, rejected, edited) and optionally edited_answer.

On resume (or when running headless), it applies the logic: auto-approve by default, reject clears final_answer, and edited sets final_answer to edited_answer (with a warning if missing). It records decisions in state.final_answer, state.human_feedback, and appends trace logs; errors fall back to using the generated answer.

Later when demonstrating the API and UI interfaces the HITL feature will be more apparent.

Now the generated result is approved, we can save it properly back to the vector DB:

def validated_store_node(self, state: KnowledgeState):

 logger.info(f"🔍 validated_store_node called with knowledge_type: {getattr(state, 'knowledge_type', 'None')}")
 logger.info(f"🔍 final_answer: {getattr(state, 'final_answer', 'None')}")
 logger.info(f"🔍 human_feedback: {getattr(state, 'human_feedback', 'None')}")
 try:
 # Check for answer to validate
 if not state.final_answer:
 logger.info("⚠️ No final_answer to validate, skipping")
 state.logs = (state.logs or []) + ["⚠️ No final_answer to validate, skipping"]
 return state

 # Check feedback status
 if state.human_feedback not in ("approved", "edited"):
 logger.info(f"ℹ️ Skipping validation because feedback = {state.human_feedback}")
 state.logs = (state.logs or []) + [f"ℹ️ Skipping validation because feedback = {state.human_feedback}"]
 return state

 # Determine knowledge type (default to conversational)
 knowledge_type = getattr(state, "knowledge_type", "conversational")

 # Always store in checkpoint memory for conversation continuity
 # Mark as validated at this point; downstream vector storage may refine status
 state.status = "validated"
 state.logs = (state.logs or []) + ["✅ Conversation history managed by LangGraph checkpoint memory (thread-isolated)"]

 # Check if content should also be stored in vector DB
 if knowledge_type in ("reusable", "verified"):
 try:
 # Create a document for vector storage
 from langchain.schema import Document

 # Prepare metadata for vector storage
 metadata = {
 "source": f"human_approved_{state.query_type}",
 "thread_id": getattr(state, "thread_id", "unknown"),
 "knowledge_type": knowledge_type,
 "human_feedback": state.human_feedback,
 "timestamp": datetime.datetime.now().isoformat(),
 "user_input": state.user_input or "unknown_query"
 }

 # Add any existing metadata
 if state.metadata:
 metadata.update(state.metadata)

 # Create document for vector storage
 doc = Document(
 page_content=state.final_answer,
 metadata=metadata
 )

 # Store in vector database
 if self.vectorstore:
 logger.info(f"📚 Attempting to store {knowledge_type} knowledge in vector DB...")
 logger.info(f"📚 Document content: {doc.page_content[:100]}...")
 logger.info(f"📚 Document metadata: {doc.metadata}")
 self.vectorstore.add_documents([doc])
 state.logs = (state.logs or []) + [f"✅ {knowledge_type.title()} knowledge stored in vector database"]
 # Refine status to indicate successful vector storage
 state.status = "stored"
 logger.info(f"📚 Successfully stored {knowledge_type} knowledge in vector DB")
 else:
 state.logs = (state.logs or []) + ["⚠️ Vector store not available, skipping vector storage"]
 # Refine status to indicate validation without vector storage
 state.status = "validated_no_store"
 logger.warning("⚠️ Vector store not available, skipping vector storage")

 except Exception as e:
 state.logs = (state.logs or []) + [f"❌ Failed to store in vector DB: {e}"]
 # Refine status to indicate vector storage failure after validation
 state.status = "store_failed"
 logger.error(f"Failed to store knowledge in vector DB: {e}")
 else:
 # Conversational content - checkpoint memory only
 state.logs = (state.logs or []) + ["💬 Conversational content stored in checkpoint memory only"]

 except Exception as e:
 state.status = "error"
 state.logs = (state.logs or []) + [f"❌ Validation failed: {e}"]

 return state

Enter fullscreen mode

Exit fullscreen mode

validated_store_node checks whether there’s a reviewed answer to persist, then records the validation outcome in the conversation’s checkpointed state and, if appropriate, promotes the answer into long‑term knowledge. It first exits early if there’s no final_answer or if human_feedback isn’t an approval/edited outcome. It then assembles a metadata payload (thread_id, source, timestamps, knowledge_type, feedback, user_input, plus any extra state metadata).

If the knowledge_type indicates the content is reusable/verified and a vectorstore is available, it wraps the final_answer as a LangChain Document with that metadata and attempts to add it to the vector database (e.g., Chroma). Errors in storage are caught and logged without breaking the run. If the content is conversational or storage isn’t configured, it skips vector persistence but still marks the state as validated so the conversation history is preserved via LangGraph checkpoints.

After this node, the execution of querying reaches to its end.

### Keeping Everything Pick‑Up‑Where‑You‑Left‑Off Friendly

LangGraph uses acheckpointerto persist graph state at well-defined boundaries so runs can pause, resume, and recover reliably. Each execution is associated with a thread (or run) ID; after each node transition, the current state snapshot—inputs, outputs, and metadata—is written to the checkpointer backend. On resume or retry, LangGraph reloads the latest committed snapshot for that thread, restoring variables and control flow without redoing completed work. This makes human-in-the-loop interrupts, failures, and restarts safe and idempotent, effectively giving you durable conversation history and step-by-step progress tracking.

LangGraph offers built-in checkpointers like SqliteSaver for durable, file-backed persistence and MemorySaver for fast but in-memory runs. Beyond these, you can integrate production stores via community patterns (e.g., Postgres/SQLAlchemy) or create your own by implementing the checkpointer interface against systems like Redis, DynamoDB, or S3.

In the Smart 2nd Brain system, we use theSqliteSaverto implement an easy checkpointer inside the MasterGraphBuilder class:

# Initialize SqliteSaver checkpointer (no external service required)
# Stores checkpoints in ./data/checkpoints.sqlite
os.makedirs("data", exist_ok=True)
sqlite_conn = sqlite3.connect("data/checkpoints.sqlite", check_same_thread=False)
self.checkpointer = SqliteSaver(sqlite_conn)

Enter fullscreen mode

Exit fullscreen mode

When the compile graph is returned, remember to include checkpointer as an argument:

# Compile the graph with checkpointing
return graph.compile(checkpointer=self.checkpointer)

Enter fullscreen mode

Exit fullscreen mode

See? Pretty simple to do.

I have just walkthrough all nodes in different execution paths, here is the code to build the graph object in runtime:

def get_graph_builder(request: Request) -> MasterGraphBuilder:

 # Use app.state; lazily initialize if missing
 graph_builder = getattr(request.app.state, "graph_builder", None)
 compiled_graph = getattr(request.app.state, "compiled_graph", None)

 if graph_builder is None:
 # Extract configuration from environment settings
 api_key = settings.openai_api_key
 azure_endpoint = settings.azure_openai_endpoint_url

 # Validate required configuration
 if not api_key:
 raise HTTPException(
 status_code=500,
 detail="OpenAI API key not configured"
 )

 try:
 # =============================================================================
 # MODEL INITIALIZATION
 # =============================================================================

 # Import Azure OpenAI models for embeddings and language generation
 from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI

 # Initialize Azure embedding model for document vectorization
 embedding_model = AzureOpenAIEmbeddings(
 azure_deployment="text-embedding-3-small", # Your embedding deployment name
 openai_api_version="2024-12-01-preview", # Azure OpenAI API version
 azure_endpoint=azure_endpoint, # Azure service endpoint
 openai_api_key=api_key # API key for authentication
 )

 # Initialize Azure language model for text generation and reasoning
 llm = AzureChatOpenAI(
 azure_deployment="gpt-4o", # Your LLM deployment name
 openai_api_version="2024-12-01-preview", # Azure OpenAI API version
 azure_endpoint=azure_endpoint, # Azure service endpoint
 openai_api_key=api_key, # API key for authentication
 temperature=0.1 # Low temperature for consistent outputs
 )

 # =============================================================================
 # VECTOR STORE INITIALIZATION
 # =============================================================================

 # Initialize ChromaDB vector store for document storage and retrieval
 from langchain_chroma import Chroma
 vectorstore = Chroma(
 collection_name="smart_second_brain", # Collection name for documents
 embedding_function=embedding_model, # Function to create embeddings
 persist_directory="./chroma_db" # Local storage directory
 )

 # =============================================================================
 # GRAPH BUILDER INITIALIZATION
 # =============================================================================

 # Create and configure the main workflow orchestrator
 graph_builder = MasterGraphBuilder(
 llm=llm, # Language model for reasoning
 embedding_model=embedding_model, # Embedding model for vectorization
 vectorstore=vectorstore, # Vector database for storage
 chromadb_dir="./chroma_db" # ChromaDB storage directory
 )

 # Compile the workflow for execution
 compiled_graph = graph_builder.build()
 request.app.state.graph_builder = graph_builder
 request.app.state.compiled_graph = compiled_graph
 logger.info("✅ Graph builder initialized with all models")

 except Exception as e:
 logger.error(f"❌ Failed to initialize graph builder: {e}")
 raise HTTPException(
 status_code=500,
 detail=f"Failed to initialize graph: {str(e)}"
 )

 return graph_builder

Enter fullscreen mode

Exit fullscreen mode

This method is used in the FastAPI layer, you can also see how the embedding model, LLM and the chroma database vector store are created and injected into the graph builder.

Once the caller get the compiled graph object, it can be executed by calling the invoke method.

### Wrapping Up: Core Logic Locked In — APIs and UI Coming Next

Now the core LangGraph implementation is wrapped up.

As a personal productivity tool, a clean, elegant UI matters — and we’ll front it with an API to control graph access and enable better testing. Don’t miss the next chapter: we’ll dive into the fun part with the API and user interface.

(The project source code will be provided when the entire series is concluded.)

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
