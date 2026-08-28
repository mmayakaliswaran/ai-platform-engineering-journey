from app.models import Document

def search(
        documents: list[Document],
        keyword: str,
        category: str | None = None
) -> list[Document]:
    selected_docs = [
        doc
        for doc in documents
        if (
                keyword.lower() in doc.title.lower()
                and (
                        category is None
                        or doc.category.lower() == category.lower()
                )
        )
    ]

    return selected_docs