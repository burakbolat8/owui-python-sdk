import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.functions.FunctionsAPI._get")
def test_get_functions(mock_get, client):
    mock_get.return_value = [{"id": "func1"}]
    functions = client.functions.get_functions()
    assert isinstance(functions, list)
    assert functions[0]["id"] == "func1"

@patch("owui_sdk.api.functions.FunctionsAPI._post")
def test_create_function(mock_post, client):
    mock_post.return_value = {"id": "func2", "name": "TestFunc"}
    func = client.functions.create_function(name="TestFunc", description="desc", parameters={})
    assert func["id"] == "func2"
    assert func["name"] == "TestFunc" 