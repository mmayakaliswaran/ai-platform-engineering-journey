from fastapi import FastAPI
from app.data import all_docs
from app.service import search
from app.models import DocumentResponse, Document, SearchResponse

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