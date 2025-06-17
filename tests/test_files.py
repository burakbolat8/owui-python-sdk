import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.files.FilesAPI._get")
def test_get_files(mock_get, client):
    mock_get.return_value = [{"id": "file1"}]
    files = client.files.get_files()
    assert isinstance(files, list)
    assert files[0]["id"] == "file1"

@patch("owui_sdk.api.files.FilesAPI._get")
def test_get_file(mock_get, client):
    mock_get.return_value = {"id": "file1", "name": "test.txt"}
    file = client.files.get_file("file1")
    assert file["id"] == "file1"
    assert file["name"] == "test.txt" 