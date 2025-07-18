from typing import Optional, Dict, Any, List
from .base import BaseAPI
from ..models import Knowledge

class KnowledgeAPI(BaseAPI):
    """API endpoints for knowledge base operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/knowledge"

    def get_all(self) -> List[Knowledge]:
        """Get all knowledge bases."""
        data = self._get("/list")
        return [Knowledge(**kb) for kb in data]

    def get(self) -> List[Knowledge]:
        """Get knowledge (current user)."""
        data = self._get("")
        return [Knowledge(**kb) for kb in data]

    def get_by_name(self, name: str) -> Knowledge:
        """
        Get a knowledge base by its name.
        
        Args:
            name: The name of the knowledge base
            
        Returns:
            The knowledge base
        """
        data = self._get(f"/name/{name}")
        return Knowledge(**data)

    def create(self, name: str, description: Optional[str] = None) -> Knowledge:
        """
        Create a new knowledge base.
        
        Args:
            name: The name of the knowledge base
            description: Optional description
            
        Returns:
            The created knowledge base
        """
        data = self._post("", json={"name": name, "description": description})
        return Knowledge(**data)

    def reindex(self) -> Dict[str, Any]:
        """Reindex all knowledge files."""
        return self._post("/reindex")

    def get_by_id(self, knowledge_id: str) -> Knowledge:
        """Get knowledge by ID."""
        data = self._get(f"/{knowledge_id}")
        return Knowledge(**data)

    def update(self, knowledge_id: str, name: Optional[str] = None, description: Optional[str] = None, data: Optional[Dict[str, Any]] = None, access_control: Optional[Dict[str, Any]] = None) -> Knowledge:
        """Update knowledge by ID."""
        payload = {"name": name, "description": description, "data": data, "access_control": access_control}
        result = self._post(f"/{knowledge_id}/update", json=payload)
        return Knowledge(**result)

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

    def delete(self, kb_id: str) -> dict:
        """
        Delete a knowledge base.
        
        Args:
            kb_id: The ID of the knowledge base to delete
            
        Returns:
            The response data
        """
        return self._delete(f"/{kb_id}")

    def reset(self, knowledge_id: str) -> Dict[str, Any]:
        """Reset knowledge by ID."""
        return self._post(f"/{knowledge_id}/reset")

    def add_files_batch(self, knowledge_id: str, file_ids: List[str]) -> Dict[str, Any]:
        """Add multiple files to a knowledge base."""
        payload = {"file_id": file_ids}
        return self._post(f"/{knowledge_id}/files/batch/add", json=payload) 