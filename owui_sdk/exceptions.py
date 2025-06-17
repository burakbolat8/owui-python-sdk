class APIError(Exception):
    """Base exception for API errors."""
    def __init__(self, message: str, status_code: int = None, response: dict = None):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)

class AuthenticationError(APIError):
    """Raised when authentication fails."""
    pass

class ValidationError(APIError):
    """Raised when request validation fails."""
    pass

class RateLimitError(APIError):
    """Raised when rate limit is exceeded."""
    pass

class ResourceNotFoundError(APIError):
    """Raised when a requested resource is not found."""
    pass 