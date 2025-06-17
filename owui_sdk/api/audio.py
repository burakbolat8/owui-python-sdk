from typing import Optional, Dict, Any, List
from .base import BaseAPI

class AudioAPI(BaseAPI):
    """API endpoints for audio operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/audio"

    def get_config(self) -> Dict[str, Any]:
        """Get audio config."""
        return self._get("/config")

    def update_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Update audio config."""
        return self._post("/config/update", json=config)

    def speech(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate speech from text."""
        return self._post("/speech", json=data)

    def transcriptions(self, file) -> Dict[str, Any]:
        """Transcribe audio file."""
        files = {"file": file}
        return self._post("/transcriptions", files=files)

    def get_models(self) -> List[Dict[str, Any]]:
        """Get available audio models."""
        return self._get("/models")

    def get_voices(self) -> List[Dict[str, Any]]:
        """Get available voices."""
        return self._get("/voices") 