 Live Demo Link : https://markz-mind-pn.streamlit.app
 
 🚀 Enterprise AI Agent Suite

A comprehensive multi-agent platform featuring specialized AI workflows for Autonomous Business Intelligence and E-Commerce Customer Support Automation. Built with Streamlit, OpenAI, and custom Retrieval-Augmented Generation (RAG) pipelines.

---

 📸 Suite Overview

| Application | Primary Focus | Core Capabilities |
| :--- | :--- | :--- |

| SupportPearlz AI Engine | E-Commerce Support & Action Hub | Live Order Placement, Real-Time DB Tracking, RAG Knowledge Base |

---

⚡ 1. MarketMind AI Engine

MarketMind AI is an autonomous market research system designed to eliminate manual data gathering and hallucination risks in executive decision-making.

 🔑 Key Features
* Multi-Phase Planning Agent: Deconstructs complex research questions into structured execution phases.
* Autonomous Tool Execution: Dynamically triggers search tools, web scrapers, and data extractors.
* Evidence Verification & Quality Control Gate: Evaluates collected evidence to flag unverified claims, weak citations, or potential hallucinated data.
* Real-Time Cost & Token Accounting: Tracks prompt tokens, completion tokens, and estimated USD expenditure per request.
* Human-in-the-Loop Audit Gate: Allows reviewers to approve reports, request agent iterations, or reject outputs before deployment.

### 📁 Architecture & File Structure

supportpearlz/
├── app.py                  Main Streamlit interface & chat layout
├── database/
│   └── orders.db            SQLite database for order records
├── rag/
│   ├── retriever.py         Vector database retrieval engine
│   └── embeddings.py        Knowledge base embedding generator
└── utils/
└── auth.py              API Key authentication guardrail