import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.channels.ChannelsAPI._get")
def test_list_channels(mock_get, client):
    mock_get.return_value = [{"id": "chan1"}]
    channels = client.channels.list()
    assert isinstance(channels, list)
    assert channels[0]["id"] == "chan1"

@patch("owui_sdk.api.channels.ChannelsAPI._post")
def test_create_channel(mock_post, client):
    mock_post.return_value = {"id": "chan2", "name": "TestChannel"}
    channel = client.channels.create(data={"name": "TestChannel"})
    assert channel["id"] == "chan2"
    assert channel["name"] == "TestChannel" 