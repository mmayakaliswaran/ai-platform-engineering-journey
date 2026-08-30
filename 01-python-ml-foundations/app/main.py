from fastapi import FastAPI
from app.data import all_docs
from app.service import search, semantic_search
from app.models import DocumentResponse, Document, SearchResponse, SemanticSearchResponse, SemanticSearchResults

app = FastAPI()

@app.get("/")
async def docs():
    return  {"message": "AI Platform Engineering"}

@app.get("/documents/search",
         response_model=SearchResponse)
async def search_documents(
        keyword: str,
        category: str | None = None
):
    results = search(all_docs, keyword, category)
    response : list[DocumentResponse] = [
        generate_response(doc) for doc in results
    ]
    return SearchResponse(results=response)

def generate_response(
        document: Document,
) -> DocumentResponse:
    return DocumentResponse(
        id=document.id,
        title=document.title,
        text=document.text,
        category=document.category
    )

@app.get("/documents/semantic_search",
         response_model=SemanticSearchResults)
async def semantic_search_documents(
        query: str,
        top_k: int = 2
)->SearchResponse:
    results = semantic_search(all_docs, query, top_k)
    response : list[SemanticSearchResponse] = [
        generate_semantic_response(doc, score) for (doc,score) in results
    ]
    return SemanticSearchResults(results=response)

def generate_semantic_response(
        document: Document,
        score: float
) -> SemanticSearchResponse:
    return SemanticSearchResponse(
        id=document.id,
        title=document.title,
        text=document.text,
        category=document.category,
        score=score
    )

'''
HTTP Request
     ↓
FastAPI
     ↓
semantic_search()
     ↓
Document text → embedding
     ↓
Query → embedding
     ↓
Cosine similarity
     ↓
Ranking
     ↓
Top-K
     ↓
Pydantic response
     ↓
JSON
'''