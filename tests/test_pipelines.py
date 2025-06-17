import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.pipelines.PipelinesAPI._get")
def test_list_pipelines(mock_get, client):
    mock_get.return_value = [{"id": "pipe1"}]
    pipelines = client.pipelines.list()
    assert isinstance(pipelines, list)
    assert pipelines[0]["id"] == "pipe1"

@patch("owui_sdk.api.pipelines.PipelinesAPI._post")
def test_add_pipeline(mock_post, client):
    mock_post.return_value = {"id": "pipe2", "url": "http://example.com"}
    pipe = client.pipelines.add(url="http://example.com", url_idx=1)
    assert pipe["id"] == "pipe2"
    assert pipe["url"] == "http://example.com" 