import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.tools.ToolsAPI._get")
def test_get_tools(mock_get, client):
    mock_get.return_value = [{"id": "tool1"}]
    tools = client.tools.get_tools()
    assert isinstance(tools, list)
    assert tools[0]["id"] == "tool1"

@patch("owui_sdk.api.tools.ToolsAPI._post")
def test_create_tool(mock_post, client):
    mock_post.return_value = {"id": "tool2", "name": "TestTool"}
    tool = client.tools.create_tool(name="TestTool", description="desc", parameters={})
    assert tool["id"] == "tool2"
    assert tool["name"] == "TestTool" 