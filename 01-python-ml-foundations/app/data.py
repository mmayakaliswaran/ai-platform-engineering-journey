from app.models import Document

spring = Document(
    1,
    "Spring Boot Microservices",
    "Spring Boot Microservices Architecture Design",
    "Programming"
)

kn8s = Document(
    2,
    "Kubernetes Deployment",
    "Kubernetes Deployment Standards",
    "Cloud"
)

aws = Document(
    3,
    "AWS Architecture",
    "AWS Architecture design principles",
    "Cloud"
)

rag = Document(
    4,
    "RAG Architecture",
    "RAG Architecture design principles",
    "AI"
)

mcp = Document(
    5,
    "MCP Tools",
    "MCP Tools design guide",
    "AI"
)

all_docs = [spring, kn8s, aws, rag, mcp]