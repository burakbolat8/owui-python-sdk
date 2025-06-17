import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.audio.AudioAPI._get")
def test_get_audio_models(mock_get, client):
    mock_get.return_value = [{"id": "audmodel1"}]
    models = client.audio.get_models()
    assert isinstance(models, list)
    assert models[0]["id"] == "audmodel1"

@patch("owui_sdk.api.audio.AudioAPI._post")
def test_speech(mock_post, client):
    mock_post.return_value = {"id": "speech1", "audio": "..."}
    speech = client.audio.speech(data={"text": "hello"})
    assert speech["id"] == "speech1"
    assert "audio" in speech 