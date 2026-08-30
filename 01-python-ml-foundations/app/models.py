from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class Document:
    id: int
    title: str
    text: str
    category: str

class DocumentResponse(BaseModel):
    id: int
    title: str
    text: str
    category: str

class SearchResponse(BaseModel):
    results: list[DocumentResponse]

class SemanticSearchResponse(BaseModel):
    id: int
    title: str
    text: str
    category: str
    score: float

class SemanticSearchResults(BaseModel):
    results: list[SemanticSearchResponse]

class RetrievedDocument(BaseModel):
    id: int
    title: str
    text: str
    category: str
    distance: float

class RetrievalResponse(BaseModel):
    results: list[RetrievedDocument]