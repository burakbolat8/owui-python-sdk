import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.users.UsersAPI._get")
def test_get_users(mock_get, client):
    mock_get.return_value = [{"id": "user1"}]
    users = client.users.get_users()
    assert isinstance(users, list)
    assert users[0]["id"] == "user1"

@patch("owui_sdk.api.users.UsersAPI._post")
def test_create_user(mock_post, client):
    mock_post.return_value = {"id": "user2", "username": "testuser"}
    user = client.users.create_user(username="testuser", email="test@example.com", password="pw")
    assert user["id"] == "user2"
    assert user["username"] == "testuser" 