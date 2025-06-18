import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch
from owui_sdk.models.knowledge import Knowledge

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.knowledge.KnowledgeAPI._get")
def test_get_all_knowledge(mock_get, client):
    mock_get.return_value = [{"id": "kb1", "name": "Test KB", "description": "Test Description"}]
    knowledge = client.knowledge.get_all()
    assert isinstance(knowledge[0], Knowledge)
    assert knowledge[0].id == "kb1"
    assert knowledge[0].name == "Test KB"

@patch("owui_sdk.api.knowledge.KnowledgeAPI._post")
def test_create_knowledge(mock_post, client):
    mock_post.return_value = {"id": "kb2", "name": "TestKB", "description": "desc"}
    kb = client.knowledge.create(name="TestKB", description="desc")
    assert isinstance(kb, Knowledge)
    assert kb.id == "kb2"
    assert kb.name == "TestKB"
    assert kb.description == "desc"

@patch("owui_sdk.api.knowledge.KnowledgeAPI._get")
def test_get_knowledge_by_name(mock_get, client):
    mock_get.return_value = {"id": "kb3", "name": "SearchKB", "description": "Test"}
    kb = client.knowledge.get_by_name("SearchKB")
    assert isinstance(kb, Knowledge)
    assert kb.id == "kb3"
    assert kb.name == "SearchKB"

@patch("owui_sdk.api.knowledge.KnowledgeAPI._delete")
def test_delete_knowledge(mock_delete, client):
    mock_delete.return_value = {"success": True}
    result = client.knowledge.delete("kb4")
    assert result["success"] is True
    mock_delete.assert_called_once_with("/kb4") 