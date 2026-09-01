from app.retriever import Retriever
from app.llm_client import LLMClient

class RagService:
    def __init__(self):
        self.retriever = Retriever()
        self.llm_client = LLMClient()

    def build_prompt(self,
                     question: str,
                     top_k: int = 2 ) -> str:
        retrieved_documents = self.retriever.search(question, top_k)

        context = "\n\n".join(doc.text for doc in retrieved_documents)

        prompt = f""" You are a helpful assistant. Answer the question using only the context provided below. Context: {context} Question: {question} Answer: """
        return prompt

    def answer(
            self,
            question: str,
            top_k: int = 2
    ) -> str:
        prompt = self.build_prompt(question, top_k)
        return self.llm_client.generate(prompt)