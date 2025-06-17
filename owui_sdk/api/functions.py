from typing import Optional, Dict, Any, List
from .base import BaseAPI

class FunctionsAPI(BaseAPI):
    """API endpoints for function operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/functions"
    
    def get_functions(self) -> List[Dict[str, Any]]:
        """Get all available functions."""
        return self._get()
    
    def get_function(self, function_id: str) -> Dict[str, Any]:
        """
        Get a specific function.
        
        Args:
            function_id: ID of the function
        """
        return self._get(f"/{function_id}")
    
    def create_function(
        self,
        name: str,
        description: str,
        parameters: Dict[str, Any],
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new function.
        
        Args:
            name: Function name
            description: Function description
            parameters: Function parameters schema
            **kwargs: Additional function parameters
        """
        data = {
            "name": name,
            "description": description,
            "parameters": parameters,
            **kwargs
        }
        return self._post(json=data)
    
    def update_function(
        self,
        function_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a function.
        
        Args:
            function_id: ID of the function
            name: New function name
            description: New function description
            parameters: New function parameters schema
            **kwargs: Additional parameters
        """
        data = {
            "name": name,
            "description": description,
            "parameters": parameters,
            **kwargs
        }
        return self._put(f"/{function_id}", json=data)
    
    def delete_function(self, function_id: str) -> Dict[str, Any]:
        """
        Delete a function.
        
        Args:
            function_id: ID of the function
        """
        return self._delete(f"/{function_id}")
    
    def execute_function(
        self,
        function_id: str,
        arguments: Dict[str, Any],
        **kwargs
    ) -> Dict[str, Any]:
        """
        Execute a function.
        
        Args:
            function_id: ID of the function
            arguments: Function arguments
            **kwargs: Additional parameters
        """
        data = {
            "arguments": arguments,
            **kwargs
        }
        return self._post(f"/{function_id}/execute", json=data) 