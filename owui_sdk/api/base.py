from typing import Optional, Dict, Any, List, TYPE_CHECKING
import requests
from ..exceptions import APIError
from ..utils.error_handling import handle_api_error

if TYPE_CHECKING:
    from ..client import OpenWebUI

class BaseAPI:
    """Base API class with common functionality."""
    
    def __init__(self, client: "OpenWebUI"):
        """
        Initialize the API endpoint.
        
        Args:
            client: The OpenWebUI client instance
        """
        self.client = client
        self.endpoint = ""
    
    def _get(self, path: str = "", params: Optional[Dict[str, Any]] = None) -> Any:
        """Make a GET request to the API."""
        return self.client.get(f"{self.endpoint}{path}", params=params)
    
    def _get_raw(self, path: str = "", params: Optional[Dict[str, Any]] = None) -> bytes:
        """Make a GET request and return raw bytes."""
        return self.client.get(f"{self.endpoint}{path}", params=params, raw=True)
    
    def _post(
        self,
        path: str = "",
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a POST request to the endpoint."""
        return self.client.post(f"{self.endpoint}{path}", json=json, data=data, files=files)
    
    def _put(
        self,
        path: str = "",
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a PUT request to the endpoint."""
        return self.client.put(f"{self.endpoint}{path}", json=json, data=data)
    
    def _delete(self, path: str = "", params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a DELETE request to the endpoint."""
        return self.client.delete(f"{self.endpoint}{path}", params=params) 