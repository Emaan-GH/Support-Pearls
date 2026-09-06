 Live Demo Link : https://markz-mind-pn.streamlit.app
 
  SupportPearlz – AI Customer Support RAG Agent

SupportPearlz is an advanced Retrieval-Augmented Generation (RAG) customer support assistant built using Python, LangChain, and Streamlit. The application ingests company knowledge base documents, indexes them into a persistent vector store, and provides grounded, citation-backed answers to customer queries in a multi-turn conversational interface.

---

🌟 Key Features

* Multi-Format Document Ingestion: Supports indexing of heterogeneous source files (PDF, DOCX, Markdown, CSV, TXT).
* Persistent Vector Index: Uses disk-persisted vector storage to avoid costly re-embedding on app restarts.
* Semantic & Context-Aware Retrieval: Employs query condensation to handle follow-up questions and multi-turn context accurately.
* Grounded Generation & Source Attribution: Generates answers using strictly retrieved contexts with explicit document citations and location metadata.
* Strict Refusal & Safety Controls: Directs users to human support when queries fall outside the knowledge base or attempt prompt injection.
* Structured Output Parsing: Validates response objects (answers, citations, confidence levels) using Pydantic schemas.

---

 🛠️ Project Structure

```text
supportpearlz/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── data/
│   ├── knowledge_base/       # Source documents (PDF, MD, CSV, etc.)
│   └── vector_store/         # Persisted vector database (Git-ignored)
├── src/
│   ├── config.py             # Centralized settings and environment validation
│   ├── ingestion/
│   │   ├── loaders.py        # Dispatcher for multi-format document loading
│   │   ├── chunking.py       # Text splitting configurations
│   │   └── build_index.py    # CLI script to build or rebuild the vector index
│   ├── retrieval/
│   │   ├── vector_store.py   # Vector DB creation, persistence, and loading
│   │   └── retriever.py      # Retriever setup and relevance threshold filtering
│   ├── chains/
│   │   ├── prompts.py        # System prompt templates and grounding rules
│   │   ├── schemas.py        # Pydantic response models
│   │   ├── memory.py         # Conversation history and query condensation
│   │   └── rag_chain.py      # Main LCEL pipeline composition
│   └── utils/
│       └── logging_setup.py  # Centralized logging setup
├── app.py                    # Streamlit web application interface
└── app_cli.py                # Command-line interface for interactive chat