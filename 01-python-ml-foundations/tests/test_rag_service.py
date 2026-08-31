from app.rag_service import RagService


def test_build_prompt():
    rag_service = RagService()

    prompt = rag_service.build_prompt( "cloud infrastructure design", 2 )

    assert "cloud infrastructure design" in prompt
    assert "AWS Architecture design principles" in prompt