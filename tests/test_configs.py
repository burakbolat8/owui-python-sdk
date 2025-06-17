import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.configs.ConfigsAPI._get")
def test_get_config_models(mock_get, client):
    mock_get.return_value = [{"id": "model1"}]
    models = client.configs.get_models()
    assert isinstance(models, list)
    assert models[0]["id"] == "model1"

@patch("owui_sdk.api.configs.ConfigsAPI._post")
def test_import_config(mock_post, client):
    mock_post.return_value = {"status": "imported"}
    result = client.configs.import_config(config={"key": "value"})
    assert result["status"] == "imported" 