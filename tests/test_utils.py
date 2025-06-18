import pytest
from owui_sdk.utils.validation import validate_api_key, validate_base_url
from owui_sdk.utils.error_handling import handle_api_error
from owui_sdk.exceptions import APIError, ValidationError

def test_validate_api_key():
    # Valid API key
    assert validate_api_key("sk-1234567890") is None
    
    # Invalid API keys
    with pytest.raises(ValidationError, match="API key must start with 'sk-'"):
        validate_api_key("invalid-key")
    
    with pytest.raises(ValidationError, match="API key cannot be empty"):
        validate_api_key("")
    
    with pytest.raises(ValidationError, match="API key cannot be None"):
        validate_api_key(None)

def test_validate_base_url():
    # Valid URLs
    assert validate_base_url("http://localhost:3000") is None
    assert validate_base_url("https://api.example.com") is None
    
    # Invalid URLs
    with pytest.raises(ValidationError, match="Base URL must start with http:// or https://"):
        validate_base_url("ftp://example.com")
    
    with pytest.raises(ValidationError, match="Base URL cannot be empty"):
        validate_base_url("")
    
    with pytest.raises(ValidationError, match="Base URL cannot be None"):
        validate_base_url(None)
    
    with pytest.raises(ValidationError, match="Base URL must start with http:// or https://"):
        validate_base_url("not-a-url")

def test_handle_api_error():
    # Test 404 error
    response = type('Response', (), {
        'status_code': 404,
        'text': 'Not Found',
        'json': lambda self: {'error': 'Not Found'}
    })()
    with pytest.raises(APIError, match="Not Found"):
        handle_api_error(response)
    
    # Test 500 error
    response = type('Response', (), {
        'status_code': 500,
        'text': 'Server Error',
        'json': lambda self: {'error': 'Server Error'}
    })()
    with pytest.raises(APIError, match="Server Error"):
        handle_api_error(response)
    
    # Test error with JSON response
    response = type('Response', (), {
        'status_code': 400,
        'json': lambda self: {'error': 'Bad Request'},
        'text': '{"error": "Bad Request"}'
    })()
    with pytest.raises(APIError, match="Bad Request"):
        handle_api_error(response) 