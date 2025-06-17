import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.auths.AuthsAPI._post")
def test_signin(mock_post, client):
    mock_post.return_value = {"token": "abc"}
    result = client.auths.signin(data={"email": "a", "password": "b"})
    assert result["token"] == "abc"

@patch("owui_sdk.api.auths.AuthsAPI._post")
def test_signup(mock_post, client):
    mock_post.return_value = {"id": "user1"}
    result = client.auths.signup(data={"email": "a", "password": "b"})
    assert result["id"] == "user1" 