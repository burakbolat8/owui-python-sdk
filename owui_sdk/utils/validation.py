"""Validation utilities for the SDK."""
from typing import Optional
import re
from ..exceptions import ValidationError

def validate_api_key(api_key: Optional[str]) -> None:
    """
    Validate the API key format.
    
    Args:
        api_key: The API key to validate
        
    Raises:
        ValidationError: If the API key is invalid
    """
    if api_key is None:
        raise ValidationError("API key cannot be None")
    if not api_key:
        raise ValidationError("API key cannot be empty")
    if not api_key.startswith("sk-"):
        raise ValidationError("API key must start with 'sk-'")

def validate_base_url(base_url: Optional[str]) -> None:
    """
    Validate the base URL format.
    
    Args:
        base_url: The base URL to validate
        
    Raises:
        ValidationError: If the base URL is invalid
    """
    if base_url is None:
        raise ValidationError("Base URL cannot be None")
    if not base_url:
        raise ValidationError("Base URL cannot be empty")
    if not base_url.startswith(("http://", "https://")):
        raise ValidationError("Base URL must start with http:// or https://")
    
    # Simple URL format validation
    url_pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    if not re.match(url_pattern, base_url):
        raise ValidationError("Invalid URL format")

def validate_oauth_token(token: Optional[str]) -> None:
    """
    Validate OAuth token format.
    
    Args:
        token: OAuth token to validate
        
    Raises:
        ValidationError: If OAuth token is invalid
    """
    if token is None:
        return
    
    if not isinstance(token, str):
        raise ValidationError("OAuth token must be a string")
    
    if not token.strip():
        raise ValidationError("OAuth token cannot be empty")
    
    # Basic JWT token format validation
    jwt_pattern = r'^[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$'
    if not re.match(jwt_pattern, token):
        raise ValidationError("Invalid OAuth token format") 