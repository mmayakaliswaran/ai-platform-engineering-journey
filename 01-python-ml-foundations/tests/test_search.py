from app.service import search, semantic_search
from app.data import all_docs
from app.models import Document

def test_search_case_insensitive():
    aws_document: Document = all_docs[2]
    expected_results: list[Document] = [aws_document]

    results: list[Document] = search(all_docs,"aws")

    assert expected_results == results

def test_search_different_keyword():
    kn8s_document: Document = all_docs[1]
    expected_results: list[Document] = [kn8s_document]

    results: list[Document] = search(all_docs,"deployment")

    assert expected_results == results

def test_search_category_filter():
    aws_document: Document = all_docs[2]
    expected_results: list[Document] = [aws_document]

    results: list[Document] =  search(all_docs, "architecture", "Cloud")

    assert expected_results == results

def test_search_category_filter_exclude():
    expected_results: list[Document] = []

    results: list[Document] =  search(all_docs, "architecture", "DB")

    assert expected_results == results

def test_search_no_match():
    expected_results: list[Document] = []

    results: list[Document] =  search(all_docs, "database")

    assert expected_results == results

def test_semantic_search_returns_topk():
    results: list[tuple[Document,float]] = semantic_search(all_docs, "cloud infrastructure design", 2)

    assert len(results) == 2
    assert results[0][0].title == "AWS Architecture"
    assert results[0][1] >= results[1][1]

def test_semantic_search_different_query():
    results: list[tuple[Document,float]] = semantic_search(all_docs, "container deployment")

    assert results[0][0].title == "Kubernetes Deployment"

def test_semantic_search_topk_greater_than_dataset():
    results: list[tuple[Document,float]] = semantic_search(all_docs, "container deployment",100)
    assert len(results) == 5
