from app.retriever import Retriever


def test_retriever_returns_top_k():

    retriever = Retriever()

    results = retriever.search(
        "cloud infrastructure design",
        2
    )

    assert len(results) == 2