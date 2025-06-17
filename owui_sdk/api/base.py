from typing import Optional, Dict, Any, List, TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import OpenWebUI

class BaseAPI:
    """Base class for all API endpoints."""
    
    def __init__(self, client: "OpenWebUI"):
        """
        Initialize the API endpoint.
        
        Args:
            client: The OpenWebUI client instance
        """
        self.client = client
        self.endpoint = ""
    
    def _get(self, path: str = "", params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request to the endpoint."""
        return self.client.get(f"{self.endpoint}{path}", params=params)
    
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