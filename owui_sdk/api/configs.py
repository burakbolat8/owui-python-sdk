from typing import Optional, Dict, Any, List
from .base import BaseAPI

class ConfigsAPI(BaseAPI):
    """API endpoints for configuration operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/configs"

    def import_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Import configuration."""
        return self._post("/import", json=config)

    def export_config(self) -> Dict[str, Any]:
        """Export configuration."""
        return self._get("/export")

    def get_models(self) -> List[Dict[str, Any]]:
        """Get models configuration."""
        return self._get("/models")

    def get_suggestions(self) -> List[Dict[str, Any]]:
        """Get suggestions configuration."""
        return self._get("/suggestions")

    def get_banners(self) -> List[Dict[str, Any]]:
        """Get banners configuration."""
        return self._get("/banners")

    def get_direct_connections(self) -> List[Dict[str, Any]]:
        """Get direct connections configuration."""
        return self._get("/direct_connections")

    def get_tool_servers(self) -> List[Dict[str, Any]]:
        """Get tool servers configuration."""
        return self._get("/tool_servers")

    def verify_tool_servers(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Verify tool servers configuration."""
        return self._post("/tool_servers/verify", json=data)

    def get_code_execution(self) -> Dict[str, Any]:
        """Get code execution configuration."""
        return self._get("/code_execution") 