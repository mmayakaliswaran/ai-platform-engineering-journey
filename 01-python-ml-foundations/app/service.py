import numpy as np
from app.models import Document
from sentence_transformers import SentenceTransformer

def search(
        documents: list[Document],
        keyword: str,
        category: str | None = None
) -> list[Document]:
    selected_docs = [
        doc
        for doc in documents
        if (
                keyword.lower() in doc.title.lower()
                and (
                        category is None
                        or doc.category.lower() == category.lower()
                )
        )
    ]

    return selected_docs

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_search(
        documents: list[Document],
        query: str,
        top_k: int=2
) -> list[tuple[Document, float]]:
    document_embeddings = model.encode_document(
        [doc.text for doc in documents]
    )
    query_embedding = model.encode_query(query)

    scored_docs = [
        (
            doc,
            cosine_similarity(document_embedding, query_embedding)
        )
        for doc, document_embedding
        in zip(documents, document_embeddings)
    ]

    sorted_scores = sorted(
        scored_docs,
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_scores[:top_k]


def cosine_similarity(
        vector1,
        vector2
) -> float:
    return np.dot(vector1, vector2) / (
            np.linalg.norm(vector1)*np.linalg.norm(vector2)
    )