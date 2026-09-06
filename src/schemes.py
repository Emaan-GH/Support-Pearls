from pydantic import BaseModel, Field
from typing import List


class Source(BaseModel):
    document: str
    location: str
    chunk_id: str


class RAGResponse(BaseModel):
    answer: str
    sources: List[Source] = Field(default_factory=list)
    confidence: str
    answered: bool