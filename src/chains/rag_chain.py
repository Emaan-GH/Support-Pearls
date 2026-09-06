import os
from pydantic import BaseModel, Field
from typing import List, Tuple, Optional


# System Prompt inside rag_chain.py
PROMPT_TEMPLATE = """
You are SupportPearlz AI, a helpful e-commerce support assistant.
Answer the user's question using ONLY the provided context below.

Context:
{context}

Question:
{question}

STRICT RULE:
If the answer cannot be found in the provided context, or if the question is completely unrelated to our store services, respond strictly with:
"Sorry, I cannot help with that query as it is outside our knowledge base. Please ask questions related to orders, shipping, or store policies."
"""


class SourceDocument(BaseModel):
    document: str = Field(default="Knowledge Base")
    location: str = Field(default="Section 1")
    chunk_id: str = Field(default="chunk_001")


class RAGResponse(BaseModel):
    answer: str
    confidence: str = Field(default="high")
    sources: List[SourceDocument] = Field(default_factory=list)


class SupportPearlzRAG:
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize RAG Chain with API Key.
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY")
        
        # Yahan aap apna vector store / LLM initialize kar sakte hain
        # e.g., self.vector_store = ...

    def ask(self, question: str, history: List[Tuple[str, str]] = None) -> RAGResponse:
        """
        Process the user query and return answer with sources.
        """
        # Demo / Placeholder response logic
        # Is ko baad mein apne actual LLM chain se replace kar dein
        
        sample_answer = (
            f"Thank you for reaching out! Regarding your query: '{question}', "
            "our store offers a 30-day money-back guarantee for all original items. "
            "You can initiate a return directly from your account dashboard."
        )


        
        sample_sources = [
            SourceDocument(
                document="Return_Policy_2026.pdf",
                location="Page 2, Section 3.1",
                chunk_id="doc_ret_042"
            )
        ]

        return RAGResponse(
            answer=sample_answer,
            confidence="High (94%)",
            sources=sample_sources
        )

    import os
from pydantic import BaseModel, Field
from typing import List, Tuple, Optional


class SourceDocument(BaseModel):
    document: str = Field(default="Knowledge Base")
    location: str = Field(default="Section 1")
    chunk_id: str = Field(default="chunk_001")


class RAGResponse(BaseModel):
    answer: str
    confidence: str = Field(default="high")
    sources: List[SourceDocument] = Field(default_factory=list)


class SupportPearlzRAG:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY")

    def ask(self, question: str, history: List[Tuple[str, str]] = None) -> RAGResponse:
        # Check if question is out-of-scope or unknown
        clean_q = question.lower().strip()
        
        if "policy" in clean_q or "return" in clean_q or "refund" in clean_q:
            answer = "Our store offers a 30-day money-back guarantee for all original unopened items. Returns can be initiated from your dashboard."
            confidence = "High (95%)"
            sources = [SourceDocument(document="Return_Policy.pdf", location="Page 1", chunk_id="doc_ret_01")]
        elif "shipping" in clean_q or "delivery" in clean_q:
            answer = "Standard shipping takes 3-5 business days across Pakistan. Free delivery is available on orders above PKR 3,000."
            confidence = "High (92%)"
            sources = [SourceDocument(document="Shipping_Info.pdf", location="Page 2", chunk_id="doc_shp_02")]
        else:
            answer = "Sorry, I cannot help with that query as it is outside our store knowledge base. Please ask questions related to store policies, products, or provide a valid Order ID."
            confidence = "Low (0%)"
            sources = []

        return RAGResponse(
            answer=answer,
            confidence=confidence,
            sources=sources
        )