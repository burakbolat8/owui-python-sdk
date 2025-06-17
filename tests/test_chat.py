import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.chat.ChatAPI._post")
def test_create_completion(mock_post, client):
    mock_post.return_value = {"id": "completion1", "choices": []}
    response = client.chat.create_completion(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hi"}])
    assert response["id"] == "completion1"

@patch("owui_sdk.api.chat.ChatAPI._get")
def test_get_conversations(mock_get, client):
    mock_get.return_value = [{"id": "conv1"}]
    conversations = client.chat.get_conversations()
    assert isinstance(conversations, list)
    assert conversations[0]["id"] == "conv1" 