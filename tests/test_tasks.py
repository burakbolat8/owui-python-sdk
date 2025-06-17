import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.tasks.TasksAPI._get")
def test_get_tasks_config(mock_get, client):
    mock_get.return_value = {"config": "value"}
    config = client.tasks.get_config()
    assert config["config"] == "value"

@patch("owui_sdk.api.tasks.TasksAPI._post")
def test_title_completions(mock_post, client):
    mock_post.return_value = {"titles": ["Title1"]}
    result = client.tasks.title_completions(data={"input": "test"})
    assert "titles" in result 