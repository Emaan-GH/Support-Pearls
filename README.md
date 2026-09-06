---

 🛍️ 2. SupportPearlz AI Engine

SupportPearlz is a modern, action-oriented support engine built to automate e-commerce customer service, inquiry resolution, and order execution.

 🔑 Key Features
* Automated RAG Knowledge Base: Answers customer store inquiries instantly by retrieving relevant documentation using semantic vector search.
* Live Order Placement: In-app interface allowing customer service representatives or users to generate new orders directly.
* Real-Time Database Order Tracking: Instantly queries SQLite order databases using Order IDs (e.g., `ORD-1234`) to check shipment status.
* Access Key Protection: Ensures workspace security with session-level API key authentication.

 📁 Architecture & File Structure

supportpearlz/
├── app.py                  Main Streamlit interface & chat layout
├── database/
│   └── orders.db            SQLite database for order records
├── rag/
│   ├── retriever.py         Vector database retrieval engine
│   └── embeddings.py        Knowledge base embedding generator
└── utils/
└── auth.py              API Key authentication guardrail