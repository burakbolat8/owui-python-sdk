import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.images.ImagesAPI._get")
def test_get_image_models(mock_get, client):
    mock_get.return_value = [{"id": "imgmodel1"}]
    models = client.images.get_models()
    assert isinstance(models, list)
    assert models[0]["id"] == "imgmodel1"

@patch("owui_sdk.api.images.ImagesAPI._post")
def test_generate_image(mock_post, client):
    mock_post.return_value = {"id": "img1", "url": "http://img"}
    img = client.images.generate(data={"prompt": "cat"})
    assert img["id"] == "img1"
    assert img["url"] == "http://img" 