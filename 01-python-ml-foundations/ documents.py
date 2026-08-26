from dataclasses import dataclass

@dataclass
class Document:
    id: int
    title: str
    text: str
    category: str

spring = Document(1,"Spring Boot Microservices", "Spring Boot Microservices Architecture Design","Programming")
kn8s = Document(2, "Kubernetes Deployment", "Kubernetes Deployment Standards", "Cloud")
aws = Document(3, "AWS Architecture", "AWS Architecture design principles", "Cloud")
rag = Document(4, "RAG Architecture", "RAG Architecture design principles", "AI")
mcp = Document(5, "MCP Tools", "MCP Tools design guide", "AI")

all_docs = [spring,kn8s, aws, rag, mcp]

def search(keyword: str, category: str | None = None)  -> list[Document]:
    selected_docs = [doc for doc in all_docs if (keyword.lower() in doc.title.lower() and (category is None or doc.category.lower() == category.lower()) )]

    return selected_docs

if __name__ == "__main__":

    print("*******************Search*****************************")
    for doc in search("AWS"):
        print(f"Document Title : {doc.title}")

    print()
    print("*******************Search with lower case*****************************")
    for doc in search("AwS"):
        print(f"Document Title : {doc.title}")

    print()
    print("*******************Search By Category*****************************")

    for doc in search("Deployment","Cloud"):
        print(f"Document Title : {doc.title}")
    print()
    print("*******************Search By Category without Category*****************************")

    for doc in search("Architecture"):
        print(f"Document Title : {doc.title}")


