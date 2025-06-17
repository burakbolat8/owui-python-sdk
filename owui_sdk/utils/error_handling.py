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
        response: API response object
        
    Raises:
        APIError: Base API error
        AuthenticationError: Authentication error
        ValidationError: Validation error
        RateLimitError: Rate limit error
        ResourceNotFoundError: Resource not found error
    """
    if response.status_code == 401:
        raise AuthenticationError(
            "Authentication failed",
            response.status_code,
            response
        )
    
    if response.status_code == 403:
        raise AuthenticationError(
            "Insufficient permissions",
            response.status_code,
            response
        )
    
    if response.status_code == 404:
        raise ResourceNotFoundError(
            "Resource not found",
            response.status_code,
            response
        )
    
    if response.status_code == 422:
        raise ValidationError(
            "Invalid request data",
            response.status_code,
            response
        )
    
    if response.status_code == 429:
        raise RateLimitError(
            "Rate limit exceeded",
            response.status_code,
            response
        )
    
    if response.status_code >= 400:
        error_data = response.json() if response.content else {}
        error_message = error_data.get("message", "Unknown API error")
        raise APIError(
            error_message,
            response.status_code,
            response
        )

def handle_validation_error(error: Any) -> Dict[str, Any]:
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