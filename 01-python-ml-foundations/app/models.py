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