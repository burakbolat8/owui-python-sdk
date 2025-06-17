from typing import Optional, Dict, Any, List
from .base import BaseAPI

class ToolsAPI(BaseAPI):
    """API endpoints for tool operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/tools"
    
    def get_tools(self) -> List[Dict[str, Any]]:
        """Get all available tools."""
        return self._get()
    
    def get_tool(self, tool_id: str) -> Dict[str, Any]:
        """
        Get a specific tool.
        
        Args:
            tool_id: ID of the tool
        """
        return self._get(f"/{tool_id}")
    
    def create_tool(
        self,
        name: str,
        description: str,
        parameters: Dict[str, Any],
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new tool.
        
        Args:
            name: Tool name
            description: Tool description
            parameters: Tool parameters schema
            **kwargs: Additional tool parameters
        """
        data = {
            "name": name,
            "description": description,
            "parameters": parameters,
            **kwargs
        }
        return self._post(json=data)
    
    def update_tool(
        self,
        tool_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a tool.
        
        Args:
            tool_id: ID of the tool
            name: New tool name
            description: New tool description
            parameters: New tool parameters schema
            **kwargs: Additional parameters
        """
        data = {
            "name": name,
            "description": description,
            "parameters": parameters,
            **kwargs
        }
        return self._put(f"/{tool_id}", json=data)
    
    def delete_tool(self, tool_id: str) -> Dict[str, Any]:
        """
        Delete a tool.
        
        Args:
            tool_id: ID of the tool
        """
        return self._delete(f"/{tool_id}")
    
    def execute_tool(
        self,
        tool_id: str,
        arguments: Dict[str, Any],
        **kwargs
    ) -> Dict[str, Any]:
        """
        Execute a tool.
        
        Args:
            tool_id: ID of the tool
            arguments: Tool arguments
            **kwargs: Additional parameters
        """
        data = {
            "arguments": arguments,
            **kwargs
        }
        return self._post(f"/{tool_id}/execute", json=data)
    
    def update_user_valves(
        self,
        tool_id: str,
        valves: Dict[str, Any],
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update user valves for a tool.
        
        Args:
            tool_id: ID of the tool
            valves: Valve configurations
            **kwargs: Additional parameters
        """
        data = {
            "valves": valves,
            **kwargs
        }
        return self._post(f"/{tool_id}/valves/user/update", json=data) 