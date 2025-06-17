from typing import Optional, Dict, Any, List
from .base import BaseAPI

class ModelsAPI(BaseAPI):
    """API endpoints for managing models."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/models"
    
    def get_all(self) -> List[Dict[str, Any]]:
        """Get all available models."""
        return self._get()
    
    def get_base_models(self) -> List[Dict[str, Any]]:
        """Get all base models."""
        return self._get("/base")
    
    def create(
        self,
        model: str,
        stream: Optional[bool] = None,
        path: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new model.
        
        Args:
            model: Model name
            stream: Whether to stream the response
            path: Model path
            **kwargs: Additional model parameters
        """
        data = {
            "model": model,
            "stream": stream,
            "path": path,
            **kwargs
        }
        return self._post(json=data)
    
    def push(
        self,
        name: str,
        insecure: Optional[bool] = None,
        stream: Optional[bool] = None
    ) -> Dict[str, Any]:
        """
        Push a model.
        
        Args:
            name: Model name
            insecure: Whether to use insecure connection
            stream: Whether to stream the response
        """
        data = {
            "name": name,
            "insecure": insecure,
            "stream": stream
        }
        return self._post("/push", json=data)
    
    def copy(self, source: str, destination: str) -> Dict[str, Any]:
        """
        Copy a model.
        
        Args:
            source: Source model name
            destination: Destination model name
        """
        data = {
            "source": source,
            "destination": destination
        }
        return self._post("/copy", json=data) 