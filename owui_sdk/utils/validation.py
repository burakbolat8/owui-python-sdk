import re
from typing import Optional
from ..exceptions import ValidationError

def validate_api_key(api_key: Optional[str]) -> None:
    """
    Validate API key format.
    
    Args:
        api_key: API key to validate
        
    Raises:
        ValidationError: If API key is invalid
    """
    if api_key is None:
        return
    
    if not isinstance(api_key, str):
        raise ValidationError("API key must be a string")
    
    if not api_key.strip():
        raise ValidationError("API key cannot be empty")
    
    # Add more specific validation rules if needed
    if len(api_key) < 32:
        raise ValidationError("API key must be at least 32 characters long")

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