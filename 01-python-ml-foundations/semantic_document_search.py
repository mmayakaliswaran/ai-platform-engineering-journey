import numpy as np

from app.models import Document
from app.data import all_docs
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def search_documents(
        documents : list[Document],
        query: str,
        top_k:int = 2
) -> list[tuple[Document,float]]:

    document_embeddings = model.encode_document(
        [doc.text for doc in documents]
    )

    query_embedding = model.encode_query(query)

    scored_documents = [(
        doc, cosine_similarity(query_embedding, document_embedding)
    )
        for doc, document_embedding
        in zip(documents, document_embeddings)
    ]

    return sorted(scored_documents,
                  key= lambda x:x[1],
                  reverse=True
                  ) [:top_k]

def cosine_similarity(
        vector1,
        vector2
):
    return np.dot(vector1, vector2) / (
            np.linalg.norm(vector1) * np.linalg.norm(vector2)
    )


if __name__ == "__main__":

    query = "cloud infrastructure design"

    for doc, score in search_documents(all_docs,query):
        print(f"{doc.title} : {score:.4f}")

"""
"cloud infrastructure design"
             │
             ▼
       Query Embedding
             │
             ▼
    ┌────────────────────┐
    │ Compare against    │
    │ document embeddings│
    └─────────┬──────────┘
              │
              ▼
       Cosine Similarity
              │
              ▼
           Ranking
              │
              ▼
          Top-K Docs
"""