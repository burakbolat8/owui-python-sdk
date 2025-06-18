"""Error handling utilities for the SDK."""
import json
from typing import Any, Dict, Optional
from requests import Response
from ..exceptions import (
    APIError,
    AuthenticationError,
    ValidationError,
    RateLimitError,
    ResourceNotFoundError
)

def handle_api_error(response: Response) -> None:
    """
    Handle API error responses.
    
    Args:
        response: The response object from the API
        
    Raises:
        APIError: With appropriate error message from the response
    """
    try:
        error_data = response.json()
        error_message = error_data.get('error', response.text)
    except (json.JSONDecodeError, AttributeError):
        error_message = response.text
    
    raise APIError(f"{error_message} (Status code: {response.status_code})")

def handle_request_error(error: Exception) -> None:
    """
    Handle request-related errors.
    
    Args:
        error: The exception that occurred
        
    Raises:
        APIError: With appropriate error message
    """
    raise APIError(f"Request failed: {str(error)}")

def handle_validation_error(error: Exception) -> None:
    """
    Handle validation errors.
    
    Args:
        error: The validation exception that occurred
        
    Raises:
        APIError: With appropriate error message
    """
    raise APIError(f"Validation failed: {str(error)}")

def handle_validation_error_formatted(error: Any) -> Dict[str, Any]:
    """
    Handle validation errors and format them for API responses.
    
    Args:
        error: Validation error object
        
    Returns:
        Formatted error response
    """
    if isinstance(error, ValidationError):
        return {
            "error": {
                "message": str(error),
                "type": "validation_error",
                "code": error.status_code
            }
        }
    
    return {
        "error": {
            "message": "Invalid request data",
            "type": "validation_error",
            "code": 422
        }
    } 