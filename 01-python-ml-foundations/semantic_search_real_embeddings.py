import numpy as np
from sentence_transformers import SentenceTransformer

documents = [
    "AWS cloud architecture",
    "Kubernetes deployment",
    "RAG architecture",
    "MCP tools",
    "Chocolate cake recipe"
]

query = "cloud infrastructure design"
model = SentenceTransformer('all-MiniLM-L6-v2')




def cosine_similarity(vector1, vector2):
    return (np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))

def rank_documents(
        documents,
        query,
        top_k=2
):
    document_embeddings = model.encode(documents)
    query_embedding = model.encode(query)

    cosine_sim_docs = {
        doc : cosine_similarity(embedding, query_embedding)
        for doc, embedding in zip(documents,document_embeddings)
    }
    return sorted(
        cosine_sim_docs.items(),
        key=lambda x: x[1],
        reverse=True
    )[:top_k]


if __name__ == "__main__":

    print("****************Start*********************************")
    for doc in rank_documents(documents, query):
        print(f"{doc[0]} : {doc[1]} ")
    print("****************End*********************************")

"""
                    Semantic Search
                          │
                     Query Vector
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
       Vector A        Vector B        Vector C
          │               │               │
          └───────────────┼───────────────┘
                          ▼
                  Cosine Similarity
                          │
                          ▼
                       Ranking
                       
                
                QUERY
                   │
                   ▼
              Query Vector
                   │
                   ▼
       ┌─────────────────────┐
       │ Vector Similarity   │
       └──────────┬──────────┘
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      Doc A     Doc B     Doc C
        │         │         │
        ▼         ▼         ▼
      0.99      0.98      0.35
        │         │         │
        └─────────┼─────────┘
                  ▼
                SORT
                  │
                  ▼
               TOP-K
                  │
                  ▼
          Relevant Documents
"""