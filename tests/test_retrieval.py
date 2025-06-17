import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.retrieval.RetrievalAPI._get")
def test_get_retrieval(mock_get, client):
    mock_get.return_value = {"status": "ok"}
    result = client.retrieval.get()
    assert result["status"] == "ok"

@patch("owui_sdk.api.retrieval.RetrievalAPI._post")
def test_embedding(mock_post, client):
    mock_post.return_value = {"embedding": [0.1, 0.2]}
    emb = client.retrieval.embedding(data={"text": "test"})
    assert "embedding" in emb 