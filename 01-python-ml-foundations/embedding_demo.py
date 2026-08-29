import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "AWS cloud architecture",
    "Kubernetes deployment",
    "RAG architecture",
    "MCP tools",
    "Chocolate cake recipe"
]

query = "cloud infrastructure design"

documents_embeddings = model.encode(documents)
query_embeddings = model.encode(query)

def cosine_similarity(
        vector1,
        vector2
):
    return np.dot(vector1, vector2) / (
            np.linalg.norm(vector1) * np.linalg.norm(vector2)
    )

if __name__ == "__main__":
    for document, documents_embedding in zip(documents, documents_embeddings):
        similarity = cosine_similarity(query_embeddings, documents_embedding )
        print(f"{document} : {similarity}")

"""
                   User Query
                       │
                       ▼
                Embedding Model
                       │
                       ▼
                  Query Vector
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Document 1   Document 2   Document 3
          │            │            │
          ▼            ▼            ▼
      Embedding    Embedding    Embedding
          │            │            │
          └────────────┼────────────┘
                       ▼
               Cosine Similarity
                       │
                       ▼
                    Ranking
                       │
                       ▼
                    Top-K
"""