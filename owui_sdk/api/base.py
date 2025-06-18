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
        response = self.client.session.get(f"{self.endpoint}{path}", params=params)
        if response.status_code >= 400:
            handle_api_error(response)
        return response.json()
    
    def _get_raw(self, path: str = "", params: Optional[Dict[str, Any]] = None) -> bytes:
        """Make a GET request and return raw bytes."""
        response = self.client.session.get(f"{self.endpoint}{path}", params=params)
        if response.status_code >= 400:
            handle_api_error(response)
        return response.content
    
    def _post(
        self,
        path: str = "",
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a POST request to the endpoint."""
        response = self.client.post(f"{self.endpoint}{path}", json=json, data=data, files=files)
        if response.status_code >= 400:
            handle_api_error(response)
        return response.json()
    
    def _put(
        self,
        path: str = "",
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a PUT request to the endpoint."""
        response = self.client.put(f"{self.endpoint}{path}", json=json, data=data)
        if response.status_code >= 400:
            handle_api_error(response)
        return response.json()
    
    def _delete(self, path: str = "", params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a DELETE request to the endpoint."""
        response = self.client.delete(f"{self.endpoint}{path}", params=params)
        if response.status_code >= 400:
            handle_api_error(response)
        return response.json() 