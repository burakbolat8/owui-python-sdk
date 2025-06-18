import pytest
from owui_sdk import OpenWebUI
from unittest.mock import patch, mock_open
import os
import base64
from owui_sdk.models.file import File

@pytest.fixture
def client():
    return OpenWebUI(base_url="http://testserver", api_key="test-key")

@patch("owui_sdk.api.files.FilesAPI._get")
def test_get_files(mock_get, client):
    mock_get.return_value = [{"id": "file1", "name": "test.txt"}]
    files = client.files.get_files()
    assert isinstance(files, list)
    assert files[0]["id"] == "file1"

@patch("owui_sdk.api.files.FilesAPI._get")
def test_get_file(mock_get, client):
    mock_get.return_value = {"id": "file2", "name": "test.pdf"}
    file = client.files.get_file("file2")
    assert isinstance(file, dict)
    assert file["id"] == "file2"

@patch("owui_sdk.api.files.FilesAPI._get_raw")
@patch("owui_sdk.api.files.FilesAPI.get_file")
def test_download_file_bytes(mock_get_file, mock_get_raw, client, tmp_path):
    # Mock file metadata
    mock_get_file.return_value = {
        "id": "file3",
        "filename": "test.pdf",
        "content_type": "application/pdf"
    }
    
    # Mock file content
    test_content = b"test file content"
    mock_get_raw.return_value = test_content
    
    # Test downloading as bytes
    content = client.files.download_file("file3")
    assert content == test_content
    mock_get_raw.assert_called_once_with("/file3/content", params={"attachment": True})

@patch("owui_sdk.api.files.FilesAPI._get_raw")
@patch("owui_sdk.api.files.FilesAPI.get_file")
def test_download_file_save(mock_get_file, mock_get_raw, client, tmp_path):
    # Mock file metadata
    mock_get_file.return_value = {
        "id": "file4",
        "filename": "test.pdf",
        "content_type": "application/pdf"
    }
    
    # Mock file content
    test_content = b"test file content"
    mock_get_raw.return_value = test_content
    
    # Test saving to specific path
    save_path = os.path.join(tmp_path, "downloaded.pdf")
    content = client.files.download_file("file4", save_path=save_path)
    
    assert os.path.exists(save_path)
    with open(save_path, "rb") as f:
        assert f.read() == test_content

@patch("owui_sdk.api.files.FilesAPI._get_raw")
@patch("owui_sdk.api.files.FilesAPI.get_file")
def test_download_file_base64(mock_get_file, mock_get_raw, client):
    # Mock file metadata
    mock_get_file.return_value = {
        "id": "file5",
        "filename": "test.pdf",
        "content_type": "application/pdf"
    }
    
    # Mock file content
    test_content = b"test file content"
    mock_get_raw.return_value = test_content
    
    # Test getting content as base64
    content = client.files.download_file("file5", return_base64=True)
    assert content == base64.b64encode(test_content).decode("utf-8") 