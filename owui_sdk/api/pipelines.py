from typing import Optional, Dict, Any, List
from .base import BaseAPI

class PipelinesAPI(BaseAPI):
    """API endpoints for pipeline operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/pipelines"

    def list(self) -> List[Dict[str, Any]]:
        """Get all pipelines."""
        return self._get("/list")

    def upload(self, file, url_idx: int) -> Dict[str, Any]:
        """Upload a pipeline file."""
        files = {"file": file}
        data = {"urlIdx": url_idx}
        return self._post("/upload", files=files, data=data)

    def add(self, url: str, url_idx: int) -> Dict[str, Any]:
        """Add a pipeline by URL."""
        data = {"url": url, "urlIdx": url_idx}
        return self._post("/add", json=data)

    def delete(self, id: str, url_idx: int) -> Dict[str, Any]:
        """Delete a pipeline by ID and urlIdx."""
        data = {"id": id, "urlIdx": url_idx}
        return self._post("/delete", json=data)

    def get_all(self) -> List[Dict[str, Any]]:
        """Get all pipelines (alias for list)."""
        return self.list()

    def get(self) -> List[Dict[str, Any]]:
        """Get all pipelines (alias for list)."""
        return self.list()

    def get_valves(self, pipeline_id: str) -> Dict[str, Any]:
        """Get valves for a pipeline."""
        return self._get(f"/{pipeline_id}/valves")

    def get_valves_spec(self, pipeline_id: str) -> Dict[str, Any]:
        """Get valves spec for a pipeline."""
        return self._get(f"/{pipeline_id}/valves/spec")

    def update_valves(self, pipeline_id: str, valves: Dict[str, Any]) -> Dict[str, Any]:
        """Update valves for a pipeline."""
        return self._post(f"/{pipeline_id}/valves/update", json=valves) 