import chromadb
from app.data import all_docs
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./chroma_data")

model = SentenceTransformer("all-MiniLM-L6-v2")

collection = client.get_or_create_collection(
    name = "documents"
)

document_texts = [doc.text for doc in all_docs]
document_embeddings = model.encode_document(
    document_texts
)

for doc, embedding in zip(all_docs,document_embeddings):
    collection.upsert(
        ids=[str(doc.id)],
        documents=[doc.text],
        embeddings=[embedding.tolist()],
        metadatas=[{
            "title": doc.title,
            "category": doc.category
        }]
    )

print("Collection created successfully")
print("Collection name:", collection.name)
print("Document count:", collection.count())

print("****************************************\nStored documents:")

results = collection.get()

print("IDs:", results["ids"])
print("Documents:", results["documents"])
print("Metadata:", results["metadatas"])

query = "cloud infrastructure design"
query_embedding = model.encode_query(query)

query_results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=3,
    include=["documents", "metadatas", "distances"]
)

print("****************************************\nSemantic Search Results:")
print("Documents:", query_results["documents"])
print("Distances:", query_results["distances"])
print("Metadata:", query_results["metadatas"])


print("****************************************\nSemantic Search Results:")

for document, metadata, distance in zip(
        query_results["documents"][0],
        query_results["metadatas"][0],
        query_results["distances"][0]
):
    print(
        f"{metadata['title']} | "
        f"distance={distance:.4f} | "
        f"text={document}"
    )

"""
all_docs
   │
   ▼
SentenceTransformer
   │
   ├── encode_document()
   │
   ▼
Embeddings
   │
   ▼
ChromaDB
   │
   ▲
   │
   ├── Query embedding
   │
   │  encode_query()
   │
   ▼
Similarity Search
   │
   ▼
Top-K
             
             For Chroma's default distance metric here, lower distance = more similar.
             This is different from the cosine similarity numbers we calculated earlier, where higher = more similar.
"""