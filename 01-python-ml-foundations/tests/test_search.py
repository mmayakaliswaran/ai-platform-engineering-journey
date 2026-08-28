from app.service import search
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