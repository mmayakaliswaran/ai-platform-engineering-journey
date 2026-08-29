import numpy as np

documents = {
    "AWS Architecture": np.array([0.9, 0.8, 0.1]),
    "Kubernetes Deployment": np.array([0.8, 0.7, 0.2]),
    "RAG Architecture": np.array([0.1, 0.2, 0.9]),
    "MCP Tools": np.array([0.2, 0.1, 0.8])
}

query = np.array([0.85, 0.75, 0.15])

def cosine_similarity(vector1, vector2):
    return (np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))

def rank_documents(
        documents,
        query,
        top_k=2
):
    cosine_sim_docs = {
        doc : cosine_similarity(documents[doc], query)
        for doc in documents
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