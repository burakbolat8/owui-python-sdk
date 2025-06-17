import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.knowledge.KnowledgeAPI._get")
def test_get_all_knowledge(mock_get, client):
    mock_get.return_value = [{"id": "kb1"}]
    knowledge = client.knowledge.get_all()
    assert isinstance(knowledge, list)
    assert knowledge[0]["id"] == "kb1"

@patch("owui_sdk.api.knowledge.KnowledgeAPI._post")
def test_create_knowledge(mock_post, client):
    mock_post.return_value = {"id": "kb2", "name": "TestKB"}
    kb = client.knowledge.create(name="TestKB", description="desc")
    assert kb["id"] == "kb2"
    assert kb["name"] == "TestKB" 