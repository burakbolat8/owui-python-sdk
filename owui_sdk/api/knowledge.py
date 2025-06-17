from typing import Optional, Dict, Any, List
from .base import BaseAPI

class KnowledgeAPI(BaseAPI):
    """API endpoints for knowledge base operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/knowledge"

    def get_all(self) -> List[Dict[str, Any]]:
        """Get all knowledge bases."""
        return self._get("/list")

    def get(self) -> List[Dict[str, Any]]:
        """Get knowledge (current user)."""
        return self._get("")

    def create(self, name: str, description: str, data: Optional[Dict[str, Any]] = None, access_control: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create a new knowledge base."""
        payload = {"name": name, "description": description, "data": data, "access_control": access_control}
        return self._post("/create", json=payload)

    def reindex(self) -> Dict[str, Any]:
        """Reindex all knowledge files."""
        return self._post("/reindex")

    def get_by_id(self, knowledge_id: str) -> Dict[str, Any]:
        """Get knowledge by ID."""
        return self._get(f"/{knowledge_id}")

    def update(self, knowledge_id: str, name: Optional[str] = None, description: Optional[str] = None, data: Optional[Dict[str, Any]] = None, access_control: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Update knowledge by ID."""
        payload = {"name": name, "description": description, "data": data, "access_control": access_control}
        return self._post(f"/{knowledge_id}/update", json=payload)

    def add_file(self, knowledge_id: str, file_id: str) -> Dict[str, Any]:
        """Add a file to knowledge by ID."""
        payload = {"file_id": file_id}
        return self._post(f"/{knowledge_id}/file/add", json=payload)

    def update_file(self, knowledge_id: str, file_id: str) -> Dict[str, Any]:
        """Update a file from knowledge by ID."""
        payload = {"file_id": file_id}
        return self._post(f"/{knowledge_id}/file/update", json=payload)

    def remove_file(self, knowledge_id: str, file_id: str) -> Dict[str, Any]:
        """Remove a file from knowledge by ID."""
        payload = {"file_id": file_id}
        return self._post(f"/{knowledge_id}/file/remove", json=payload)

    def delete(self, knowledge_id: str) -> Dict[str, Any]:
        """Delete knowledge by ID."""
        return self._delete(f"/{knowledge_id}/delete")

    def reset(self, knowledge_id: str) -> Dict[str, Any]:
        """Reset knowledge by ID."""
        return self._post(f"/{knowledge_id}/reset")

    def add_files_batch(self, knowledge_id: str, file_ids: List[str]) -> Dict[str, Any]:
        """Add multiple files to a knowledge base."""
        payload = {"file_id": file_ids}
        return self._post(f"/{knowledge_id}/files/batch/add", json=payload) 