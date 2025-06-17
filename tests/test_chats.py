import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.chats.ChatsAPI._get")
def test_list_chats(mock_get, client):
    mock_get.return_value = [{"id": "chat1"}]
    chats = client.chats.list()
    assert isinstance(chats, list)
    assert chats[0]["id"] == "chat1"

@patch("owui_sdk.api.chats.ChatsAPI._post")
def test_new_chat(mock_post, client):
    mock_post.return_value = {"id": "chat2"}
    chat = client.chats.new(data={"title": "TestChat"})
    assert chat["id"] == "chat2" 