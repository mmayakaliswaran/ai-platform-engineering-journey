from app.retriever import Retriever

class RagService:
    def __init__(self):
        self.retriever = Retriever()

    def build_prompt(self,
                     question: str,
                     top_k: int = 2 ) -> str:
        retrieved_documents = self.retriever.search(question, top_k)

        context = "\n\n".join(doc.text for doc in retrieved_documents)

        prompt = f""" You are a helpful assistant. Answer the question using only the context provided below. Context: {context} Question: {question} Answer: """
        return prompt
    