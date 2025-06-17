import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.memories.MemoriesAPI._get")
def test_get_memories(mock_get, client):
    mock_get.return_value = [{"id": "mem1", "content": "test"}]
    memories = client.memories.get_memories()
    assert isinstance(memories, list)
    assert memories[0]["id"] == "mem1"

@patch("owui_sdk.api.memories.MemoriesAPI._post")
def test_add_memory(mock_post, client):
    mock_post.return_value = {"id": "mem2", "content": "added"}
    memory = client.memories.add_memory(content="added")
    assert memory["id"] == "mem2"
    assert memory["content"] == "added" 