import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.models.ModelsAPI._get")
def test_get_all_models(mock_get, client):
    mock_get.return_value = [{"id": "model1"}, {"id": "model2"}]
    models = client.models.get_all()
    assert isinstance(models, list)
    assert models[0]["id"] == "model1"

@patch("owui_sdk.api.models.ModelsAPI._get")
def test_get_base_models(mock_get, client):
    mock_get.return_value = [{"id": "base1"}]
    base_models = client.models.get_base_models()
    assert isinstance(base_models, list)
    assert base_models[0]["id"] == "base1" 