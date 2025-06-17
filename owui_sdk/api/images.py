from typing import Optional, Dict, Any, List
from .base import BaseAPI

class ImagesAPI(BaseAPI):
    """API endpoints for image operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/images"

    def get_config(self) -> Dict[str, Any]:
        """Get image config."""
        return self._get("/config")

    def update_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Update image config."""
        return self._post("/config/update", json=config)

    def verify_config_url(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Verify image config URL."""
        return self._post("/config/url/verify", json=data)

    def get_image_config(self) -> Dict[str, Any]:
        """Get image config (image-specific)."""
        return self._get("/image/config")

    def update_image_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Update image config (image-specific)."""
        return self._post("/image/config/update", json=config)

    def get_models(self) -> List[Dict[str, Any]]:
        """Get available image models."""
        return self._get("/models")

    def generate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate an image."""
        return self._post("/generations", json=data) 