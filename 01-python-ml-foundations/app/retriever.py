import chromadb
from sentence_transformers import SentenceTransformer
from app.models import RetrievedDocument

class Retriever:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="./chroma_data"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def search(
            self,
            query: str,
            top_k: int = 2
    ):

        query_embedding = self.model.encode_query(query)

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        retrieved_docs = generate_retrieved_documents(results)

        return retrieved_docs

def generate_retrieved_documents(results):

    response: list[RetrievedDocument] = []
    for id,document, metadata, distance in zip(
            results["ids"][0],
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
    ):
        document = RetrievedDocument(
            id=id,
            title=metadata['title'],
            category=metadata['category'],
            text=document,
            distance=distance
        )
        response.append(document)
    return response